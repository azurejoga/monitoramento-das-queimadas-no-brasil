# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f68121f-bf24-3bb6-9721-5ca712937ea7 | -11.01461 | -45.25382 | 2026-01-17 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42c7e58a-4127-390d-8450-a0a18003dff2 | -5.47352 | -45.40798 | 2026-01-17 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23a46c12-4feb-365b-892c-c9f41acf9a87 | -8.4359 | -44.02159 | 2026-01-17 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddd34f0d-1132-3ed4-9000-b0a0ee3e93db | -7.05292 | -45.05118 | 2026-01-17 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 926394f7-65a4-3c17-8c5c-92b8e7c6f10d | -3.99328 | -47.21494 | 2026-01-17 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cee5804-3eeb-3ac2-bb53-c96ce21561ab | -10.77755 | -44.4226 | 2026-01-17 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a40ee12-30fa-3046-8d44-9ed695da056a | -8.97891 | -48.07748 | 2026-01-17 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eacf300c-4a1b-3cd1-9103-3198e64c7761 | -9.76268 | -48.27585 | 2026-01-17 04:25:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2464a5e0-10cd-32b6-bc54-466356f07689 | -8.98598 | -48.07872 | 2026-01-17 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| feddc718-9e8f-370b-9533-cc17f72f8159 | -5.71443 | -44.1379 | 2026-01-17 04:25:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58a85bc9-fa70-3101-a3e6-abab330a76b5 | -7.52726 | -37.02916 | 2026-01-17 04:25:00 | NPP-375D | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0422768b-0140-3ae2-a263-6e3eddef806b | -8.42634 | -44.01638 | 2026-01-17 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1319a3c8-5502-3836-84c6-8004615e53ad | -6.98731 | -42.86365 | 2026-01-17 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c3c6d5cb-ce1b-3bc5-90a1-942938e83c20 | -6.22249 | -44.16036 | 2026-01-17 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 824acfa4-5222-3c64-94fc-599b1ff2225c | -6.42071 | -43.77246 | 2026-01-17 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68db22e1-ae94-3272-9611-8c94726505d0 | -10.56343 | -44.3187 | 2026-01-17 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1f11b9cf-2684-3165-87d6-6fd8b40688d6 | -8.4955 | -39.93029 | 2026-01-17 04:25:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 34a53372-183b-3f01-9679-0fb8e88b132a | -11.23617 | -48.09614 | 2026-01-17 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f68cf2e5-b254-3266-aaa7-4eb56922dd29 | -8.23525 | -46.24721 | 2026-01-17 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 186cb2ce-ce52-348e-9ad4-f569cb951f43 | -9.77109 | -48.269 | 2026-01-17 04:25:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c7d793d-ff4d-366f-862a-9703ba7cae7c | -9.65492 | -46.23689 | 2026-01-17 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03c16378-5114-3296-bc15-29cf65f17471 | -8.2561 | -48.28627 | 2026-01-17 04:25:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d95fe4c4-ea69-3734-bd21-676a083b6bbf | -6.94286 | -45.85096 | 2026-01-17 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a41dc231-3450-3d95-9ed1-881f0cb2ef60 | -6.5568 | -43.59296 | 2026-01-17 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40a66dd9-291c-3c3a-b119-138312dc70b9 | -8.43506 | -48.69479 | 2026-01-17 04:25:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fb9cfc6-50bc-3038-8eeb-1bb6643ca276 | -9.65215 | -46.23282 | 2026-01-17 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ec45bb8-17da-3fb8-9bc0-4f65e2e482d5 | -8.09888 | -45.68273 | 2026-01-17 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6478eaae-bf8c-3ed3-bff3-6c6954762f71 | -8.97122 | -48.54216 | 2026-01-17 04:25:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c88f92f0-a830-35f1-b42b-5ce8fc327479 | -10.3412 | -44.8274 | 2026-01-17 04:25:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4f77d0d-80ba-3016-8949-c1241a909b59 | -9.64824 | -46.23581 | 2026-01-17 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 536be8c3-8e47-30bb-a916-db25bd38c363 | -11.4027 | -41.41167 | 2026-01-17 04:25:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c09d533d-0aad-3476-b6b0-1afbe5b5a2b7 | -5.4366 | -44.03716 | 2026-01-17 04:25:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e72cf52f-88ee-3111-b7a3-4a1c0873fe65 | -8.88013 | -44.7827 | 2026-01-17 04:25:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f360fb5d-6506-3119-abda-eedbb420dd6f | -7.25598 | -43.06153 | 2026-01-17 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9f4bb479-93d6-361d-8290-183ddafdc85a | -6.70083 | -43.06628 | 2026-01-17 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20b2b6f0-8c8d-31f7-8850-aad49f4629ca | -10.53074 | -43.62145 | 2026-01-17 04:25:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e649d4b3-35bb-335a-9690-dbd583e1424c | -8.43533 | -44.0252 | 2026-01-17 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 449a5d17-bad5-3ba6-846c-f37d5dd3caec | -5.5672 | -45.45498 | 2026-01-17 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a04ea619-4a4e-3bce-b79d-3d8be67cf765 | -11.04704 | -45.41185 | 2026-01-17 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0403101-fad6-3a88-bee4-35f4e5b9a8e6 | -8.25182 | -48.28979 | 2026-01-17 04:25:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46cd4bde-d2a0-370d-a752-c0d986285e96 | -10.41254 | -44.88571 | 2026-01-17 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d376fca4-f2fb-3f93-8711-8cc835d9b270 | -6.94677 | -45.84797 | 2026-01-17 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bc98482-4271-3cd5-ad5c-1f67dab32a39 | -10.19481 | -44.89573 | 2026-01-17 04:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f0cf952-5663-364a-bfc2-96fc25f31eb1 | -8.44795 | -45.12683 | 2026-01-17 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 581b153c-3bac-3ed4-85b5-37de5fc744c6 | -8.43252 | -44.02105 | 2026-01-17 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b983caaa-ccbd-37f2-8749-57b886d282b8 | -9.75846 | -48.27938 | 2026-01-17 04:25:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2d7e83b-cd96-3040-a01e-cfe72ac37910 | -7.24254 | -44.27304 | 2026-01-17 04:25:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1288bb3-5b29-3fa6-8192-df5008fe0450 | -8.42972 | -44.0169 | 2026-01-17 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b735d1a-a10d-3eea-bb4d-3dc61fc6f086 | -7.18319 | -44.95403 | 2026-01-17 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23c61663-ac74-38a3-81a0-ff50cc9f5f1f | -7.25942 | -43.06207 | 2026-01-17 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 006b71ac-a7a0-3498-a6a1-0378da3df5d7 | -10.81199 | -47.56752 | 2026-01-17 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3ea7ee9-4207-3f4c-a153-dde300895046 | -10.33838 | -36.70995 | 2026-01-17 04:25:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 44d50d1a-7330-391e-b487-77a9156eb34a | -12.0932 | -42.8068 | 2026-01-17 04:25:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b361f0d-36d9-3d9d-b9cf-22e889ad47a8 | -6.94621 | -45.85151 | 2026-01-17 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87da9347-48b7-3623-b04e-0f32230fc350 | -9.65101 | -46.23988 | 2026-01-17 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f6a6430-a947-33ff-87e1-1b08ff56dfef | -6.98672 | -42.86745 | 2026-01-17 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cc51dda7-2211-3bf7-98a4-9415a416bc75 | -8.4378 | -48.69315 | 2026-01-17 04:25:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5214e6c2-9794-3d02-a00b-36e977050c12 | -10.78094 | -44.42313 | 2026-01-17 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 708e612a-2917-36d3-80d3-de90ef7ca815 | -10.19201 | -44.89165 | 2026-01-17 04:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbae1725-6f72-34ed-95c2-4ed809285954 | -8.43196 | -44.02466 | 2026-01-17 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9228a554-2bd6-3e8b-9312-8f3ee0b5a773 | -5.5295 | -43.68532 | 2026-01-17 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7743c2b9-15b5-3a45-80d3-0364f208eba5 | -9.65826 | -46.23744 | 2026-01-17 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b2eb134-d729-3c41-bc46-73409ca5b366 | -10.33797 | -36.71315 | 2026-01-17 04:25:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5bb48941-e90c-3882-9e93-f5cf0463ca86 | -7.2392 | -44.27251 | 2026-01-17 04:25:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef0b4cd5-5a0c-3b55-b646-b42e2099a289 | -6.4194 | -43.77262 | 2026-01-17 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e941452-5dce-33c4-89e2-ceccc3cbd3ee | -10.41199 | -44.88927 | 2026-01-17 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb026e75-5848-30d6-a923-49d27a5f5004 | -6.54632 | -40.50926 | 2026-01-17 04:25:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2d69a856-eb04-3036-ac13-c7cdbfc91b79 | -5.56386 | -45.45444 | 2026-01-17 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a9ac615-de7c-3061-9a7f-e6e11b8bfa2b | -7.23975 | -44.269 | 2026-01-17 04:25:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7368446-7bfb-3a95-8381-de67b9aa8c9f | -6.94342 | -45.84742 | 2026-01-17 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8b6fdff-b8b8-342c-bbe5-911f1bf914bc | -8.23918 | -46.24419 | 2026-01-17 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60b5032f-5ae4-30ee-b705-696bb9acd4d8 | -11.04759 | -45.40832 | 2026-01-17 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22e21524-4f86-331f-8487-1603cd1103f3 | -9.37946 | -47.07684 | 2026-01-17 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35565965-70d1-3e01-82b4-8dafee78450c | -10.41534 | -44.8898 | 2026-01-17 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e9d7f7a-3561-3f55-99c3-3549e7903861 | -6.96391 | -46.2225 | 2026-01-17 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56377ca4-e98c-36dc-be38-edb81f8d4e94 | -8.97969 | -48.07878 | 2026-01-17 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f70f565b-e84f-3bd3-83b7-90372962f4b4 | -10.33358 | -36.71432 | 2026-01-17 04:25:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc10be9d-272d-3dfc-9c04-ec02cd0c0735 | -5.37614 | -43.19489 | 2026-01-17 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40c4eb5a-15b0-355b-998c-3a48c42dcd02 | -3.43138 | -49.22649 | 2026-01-17 04:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b53db353-8c26-35e1-a39c-e24647a178c0 | -8.97616 | -48.07814 | 2026-01-17 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cc44fc4-7477-3622-81ab-c2df876f0a24 | -5.45615 | -44.70576 | 2026-01-17 04:25:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1e7b541-cf7c-35bc-a733-a65e5a0a20ad | -8.43365 | -44.01382 | 2026-01-17 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c20857e-a51c-3f7b-9ca0-b7e5b65e18d5 | -5.45669 | -44.70229 | 2026-01-17 04:25:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7268f8f7-af2b-352c-a6e7-fad160bbd656 | -10.48233 | -49.35812 | 2026-01-17 04:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24f5c1d4-b006-3083-ab20-2c71dabc97ea | -8.43873 | -48.6954 | 2026-01-17 04:25:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20755cd1-ac2b-3bf8-82d1-36f65d584423 | -8.43309 | -44.01744 | 2026-01-17 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf291422-8577-3ef8-b84b-cc34dc2495b3 | -10.48159 | -49.36255 | 2026-01-17 04:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d5d6015-0ef7-38f4-b0c2-daaeb520ffc0 | -6.19385 | -44.61943 | 2026-01-17 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44e1ed8a-805f-350f-83f4-665fa0076d3c | -9.65436 | -46.24042 | 2026-01-17 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55d77daa-c7c2-37f1-baa3-b6583ee832a2 | -8.01382 | -45.04699 | 2026-01-17 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b69664c-d542-35d4-9f0f-9b102edbf58e | -3.88773 | -47.5906 | 2026-01-17 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 49a4a166-b25a-3369-8732-bf26dd52dcda | -9.65158 | -46.23635 | 2026-01-17 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d461262-6f04-3c77-901e-a037377d5d9d | -9.64679 | -41.89766 | 2026-01-17 04:25:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0ed2f60c-bcbe-318e-a727-e5ca886efb38 | -5.53285 | -43.68584 | 2026-01-17 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0e1ab3c-4386-3f42-811f-a47d65901504 | -8.43028 | -44.01329 | 2026-01-17 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f717870-0f65-3cfb-b920-2e841cc4965e | -9.37606 | -47.07627 | 2026-01-17 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dde0b415-be04-3db6-98ce-5b0c97228d6d | -11.01406 | -45.25736 | 2026-01-17 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aa009df-f70e-3056-95e0-c4575ffb588e | -8.01714 | -45.04752 | 2026-01-17 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1456f3d7-c457-312d-9cd1-de4fd0430563 | -13.50533 | -46.70279 | 2026-01-17 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f28a15b0-691f-3c98-9b33-3e243a6556b6 | -15.89251 | -43.45023 | 2026-01-17 04:27:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README6.md)
