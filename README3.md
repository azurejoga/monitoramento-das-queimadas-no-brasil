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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 862b3b05-fb25-3c5b-a133-e749f391ed3e | -5.6363 | -43.384102 | 2025-08-20 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 507f0616-dff2-3ea5-ae24-a5cecbdda151 | -5.326 | -43.923901 | 2025-08-20 00:14:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab673271-82aa-3a62-b925-98476699fd80 | -4.3112 | -48.105801 | 2025-08-20 00:14:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24d64056-ed0b-341c-bfb8-60b8b66cf9f2 | -6.8693 | -43.596001 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e68c289d-ff1a-3a08-967c-d738c7a83535 | -6.6827 | -43.682301 | 2025-08-20 00:14:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48e36332-376d-3f10-9788-606402738e98 | -8.0227 | -47.664799 | 2025-08-20 00:14:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd1450d0-64f6-3bcb-9bd5-33d5543bf6c7 | -6.3198 | -43.762798 | 2025-08-20 00:14:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03c6ecaf-857d-3c45-b3bb-7969c9e56a54 | -6.7155 | -44.331699 | 2025-08-20 00:14:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b90aa981-d5b1-3a4f-ba28-ce9533acfab8 | -8.0155 | -47.678501 | 2025-08-20 00:14:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25e38f0b-aa1b-3988-834f-516f25d6169e | -3.2632 | -49.148899 | 2025-08-20 00:14:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdc40ce3-17c2-3724-bfc2-a2ee57999711 | -22.706699 | -42.144699 | 2025-08-20 00:14:00 | METOP-C | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cccfb4c6-3902-34e0-bbde-f6c011eb94bd | -13.6749 | -44.223202 | 2025-08-20 00:14:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf5872f1-6326-3623-ae4d-4f3c06b657ed | -2.3731 | -47.658699 | 2025-08-20 00:14:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 500e0aca-0824-3d13-9b0f-94b7dfcce853 | -5.4815 | -42.165199 | 2025-08-20 00:14:00 | METOP-C | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e829eec6-efd0-349f-90db-609f7750a5d7 | -8.7893 | -45.481701 | 2025-08-20 00:14:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f53f55d-da8c-34d5-bae5-a04d7abe858b | -6.3182 | -43.755699 | 2025-08-20 00:14:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11a92b79-06f3-3753-bd67-95e73229e165 | -2.3829 | -47.656502 | 2025-08-20 00:14:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37ecbbe5-54fc-3897-8da3-9f466cf4cc82 | -8.1379 | -49.499901 | 2025-08-20 00:14:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bac9c8a-1ea2-3cfa-8814-69bd562ce091 | -5.6394 | -43.397999 | 2025-08-20 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d935cd6-4a53-3588-ab6f-00d27a6d6f57 | -20.951401 | -46.109798 | 2025-08-20 00:14:00 | METOP-C | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c857ed8-d7b1-3ef6-ac23-c7388875cad4 | -22.704901 | -42.135502 | 2025-08-20 00:14:00 | METOP-C | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d8e9acf-ef0a-3c50-a3f9-85174cbece83 | -5.4634 | -48.871799 | 2025-08-20 00:14:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf6b443-5f28-3874-8f18-74d03c709c0b | -6.9804 | -43.586201 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ab0b8020-9fa3-3587-b056-0f29d7304fa1 | -13.0278 | -46.818298 | 2025-08-20 00:14:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af81d381-9c26-3efb-818e-8a5214afdfa5 | -7.028 | -44.3018 | 2025-08-20 00:14:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83807f17-b555-38a8-9310-67ddf90ec35a | -3.9853 | -42.523201 | 2025-08-20 00:14:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c35a2a80-acfc-3e64-97c0-66139f493bbe | -3.9951 | -42.521 | 2025-08-20 00:14:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ebf33d5-2209-30d7-9609-bc80cce0ef9e | -7.5766 | -45.428001 | 2025-08-20 00:14:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd43078-178c-398a-b556-a063cf688182 | -13.4048 | -46.3685 | 2025-08-20 00:14:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 745efa41-ae61-3b06-b75a-2d3cfc1a6db1 | -8.1693 | -47.3479 | 2025-08-20 00:14:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e69001a1-4def-345b-bd3e-a7ab2a4c6539 | -6.3166 | -43.7486 | 2025-08-20 00:14:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbb006e8-b054-37d3-89a3-73ffedc303dc | -9.9118 | -49.283699 | 2025-08-20 00:14:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 649f2717-d717-34c8-acaa-f263d1f16eba | -8.2922 | -46.353802 | 2025-08-20 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d163f2cb-76ae-3ffe-aeac-9506db02485e | -4.4304 | -47.7663 | 2025-08-20 00:14:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87edacac-2a7b-3f5a-93e5-9d26288b5da4 | -5.4913 | -42.162998 | 2025-08-20 00:14:00 | METOP-C | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 762c4ffa-2789-3ecd-b2b0-ee2bf34575b2 | -9.524 | -42.944698 | 2025-08-20 00:14:00 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| db7ee7cc-4f2b-3219-977d-f3c8e0cc9879 | -4.9114 | -43.234299 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd769895-f183-3bed-bc3f-936d5b56cc20 | -4.2917 | -48.064301 | 2025-08-20 00:14:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93cd7a28-b5a9-3645-be73-40fde557f6b9 | -7.6626 | -45.259602 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d02b3b53-243b-317f-a6a5-ee5c4297b68e | -7.7931 | -45.152901 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a61da845-ddf4-30c8-988d-5bde232e2a1f | -15.5486 | -42.283699 | 2025-08-20 00:14:00 | METOP-C | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1bba4b-dca2-374c-8ca6-2f33ca20c633 | -6.0609 | -44.121799 | 2025-08-20 00:14:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab06479c-aaab-384c-8603-5b2098d44840 | -9.5019 | -43.168301 | 2025-08-20 00:14:00 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8c0507e7-c723-310e-864e-f90d89492c6e | -5.9759 | -43.6091 | 2025-08-20 00:14:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 251d2d5b-400e-3e9c-bcb6-0b79eb913f9d | -12.9436 | -46.157799 | 2025-08-20 00:14:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 666ba20b-cb16-3a36-87f1-6d96934213a7 | -3.6911 | -44.212898 | 2025-08-20 00:14:00 | METOP-C | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd36cb64-2994-395d-866c-7f262f2fb1cc | -6.6479 | -43.893101 | 2025-08-20 00:14:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1563d08b-e3b2-3abc-83ad-3ca34fc6197e | -20.3377 | -51.726799 | 2025-08-20 00:14:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9b7ab10b-6480-3b29-9022-ee85cff5711a | -7.2468 | -50.1908 | 2025-08-20 00:14:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e468338-f1cb-3e85-9f37-fe13518267de | -5.8746 | -48.1343 | 2025-08-20 00:14:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf6fd428-f3b5-32d6-9748-15a70c6cccfa | -13.8735 | -45.5695 | 2025-08-20 00:14:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5ee709e-af54-3849-ad23-db7ccab3d27c | -6.9428 | -42.8741 | 2025-08-20 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd5510b4-cc1d-3e86-8689-0f2fa29934bd | -21.354401 | -41.9184 | 2025-08-20 00:14:00 | METOP-C | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb1049a5-b5cd-3780-95e7-a60cbac1e1f0 | -13.0852 | -51.898899 | 2025-08-20 00:14:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c47a138b-a6aa-3aaf-b243-20812fab0e63 | -12.9481 | -46.179901 | 2025-08-20 00:14:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e00080eb-49af-3067-ab44-c48e75ba01fd | -6.8512 | -43.607399 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4f864f3f-0ba0-3f3a-aaa7-759889e54f99 | -8.2174 | -44.423199 | 2025-08-20 00:14:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d187355-1c42-3e45-820c-0535d42ed15b | -7.0637 | -46.876099 | 2025-08-20 00:14:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65541f58-05c0-3569-af80-c6174591a258 | -7.6369 | -45.2827 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4babd47-7f3f-3308-931e-847c25ae9560 | -7.5747 | -45.419498 | 2025-08-20 00:14:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e453e016-14ad-3ecb-b23b-40a70a43caaa | -7.6467 | -45.280602 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b29c3613-9c4c-3f0a-bb0a-f967fd69bd64 | -6.9705 | -43.588402 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e8d7886-ad41-3344-9c95-b1b5e3603c12 | -5.8695 | -48.111198 | 2025-08-20 00:14:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dee1c2c0-283c-3765-a044-5cf0f3480182 | -21.504101 | -45.474602 | 2025-08-20 00:14:00 | METOP-C | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9b15213d-1a8b-33bc-86ca-8a1c5ec8b55b | -3.2282 | -46.803398 | 2025-08-20 00:14:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 382f8370-c06a-3dc6-b215-e51bcdc7f930 | -5.6379 | -43.391102 | 2025-08-20 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39170d48-9277-38be-85b2-78352602963c | -3.6895 | -44.205898 | 2025-08-20 00:14:00 | METOP-C | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c5e4fef-7445-39e7-8cac-e6698244242e | -7.2196 | -44.699299 | 2025-08-20 00:14:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d71a77c5-8442-3cc9-9914-e63678fecbfb | -18.677799 | -46.989201 | 2025-08-20 00:14:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1c12ecaf-6f94-3695-8599-16010657f9b0 | -5.3276 | -43.931 | 2025-08-20 00:14:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 686b73bc-eb40-3dec-8e3c-847d6b13e970 | -6.8611 | -43.605301 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 186ccd07-3e0e-3dd4-a5b1-4ceac79e6b49 | -2.7715 | -48.603401 | 2025-08-20 00:14:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a7c237b-9cec-3fb7-9b5d-6e7ba43733f2 | -13.1 | -51.9244 | 2025-08-20 00:14:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74016c94-fdd5-3ce3-90fa-3f7499521adb | -6.1263 | -42.955502 | 2025-08-20 00:14:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a8381928-f71a-3dea-817d-61684ffca579 | -4.4206 | -47.768398 | 2025-08-20 00:14:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e570481a-d018-3513-9402-82249cbf2641 | -5.6159 | -43.4762 | 2025-08-20 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4770760d-841f-3027-9ca6-a0f9e23624a0 | -6.8643 | -43.619499 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27b4c792-3b1d-37e0-b685-f72fcf3e7e62 | -8.0252 | -47.676498 | 2025-08-20 00:14:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77980c1a-c0a9-3c75-a061-2a6308ca2639 | -6.9526 | -42.871899 | 2025-08-20 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 051ecad8-172e-33d9-bc03-64771c7c9f8f | -7.2699 | -50.203602 | 2025-08-20 00:14:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a865be-4689-37af-a9e8-4d1e1e35046b | -4.2941 | -48.075199 | 2025-08-20 00:14:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3573f3ee-0074-386f-9017-799d09315484 | -12.9556 | -46.166801 | 2025-08-20 00:14:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ffe5f091-4e74-30ab-bcd1-6078a3467471 | -11.9721 | -46.787601 | 2025-08-20 00:14:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9fe61d83-5c82-3a26-a52c-9fc9ac432db9 | -5.6631 | -43.5023 | 2025-08-20 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 323e6e09-24cb-3ce1-b565-77ac33ead74e | -5.872 | -48.1227 | 2025-08-20 00:14:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a60c629-25e6-3a78-89d4-4ae09f481a96 | -5.1123 | -43.211102 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d10c22e8-90e3-36a9-9a03-a1af2676ee85 | -5.6143 | -43.469299 | 2025-08-20 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99e548df-088a-34e1-9728-c6bf98b66ccf | -12.8095 | -48.566601 | 2025-08-20 00:14:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b68577c0-a4d7-3a99-8063-c941b1fe9475 | -18.307899 | -48.8596 | 2025-08-20 00:14:00 | METOP-C | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b04423b5-70b8-387c-bd97-12ec46a5f379 | -6.9444 | -42.881001 | 2025-08-20 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8481c745-1d7b-38ac-9e44-f5ca3f8dd1e6 | -3.8174 | -41.5704 | 2025-08-20 00:14:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| da37c70e-6ab6-3aa9-a8af-a282b522651e | -11.7517 | -48.197601 | 2025-08-20 00:14:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fafd9540-4ebc-393b-8e80-4cb212095205 | -2.3753 | -47.668301 | 2025-08-20 00:14:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c0e521c-76fc-35c0-b508-bacead94b621 | -3.9724 | -42.511799 | 2025-08-20 00:14:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e6cafa0-f323-37e8-a71c-08d9104cadae | -5.1096 | -43.1539 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed6d4843-8841-3fae-9cb6-f462b05b6b5e | -6.4799 | -43.742298 | 2025-08-20 00:14:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ac44de2-4d7d-3b60-a6b1-d927357ffde1 | -6.398 | -44.2929 | 2025-08-20 00:14:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbb139fd-15ee-3b00-ba6d-ee97b88c45fb | -12.9819 | -45.2103 | 2025-08-20 00:14:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 381921fd-0541-30e1-82bd-20efa239b8f7 | -6.9738 | -42.874401 | 2025-08-20 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ee678040-d777-3858-8e2a-79d478efe558 | -6.056 | -44.145699 | 2025-08-20 00:14:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
