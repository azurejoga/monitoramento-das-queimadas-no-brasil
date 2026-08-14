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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c96ca3df-bbbd-3997-ab95-c8f8fdd9984a | -13.23806 | -54.25671 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3427c55e-0c90-3950-9802-a2fa995e03d6 | -11.07327 | -50.95206 | 2026-08-14 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fe8576fd-0ce4-35f9-9b42-6b62268ce80f | -13.25548 | -50.37623 | 2026-08-14 04:14:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55f2b52a-1b68-36ff-b081-5dc4adf7a93b | -14.95308 | -46.62186 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12479d75-cb77-39c5-afce-ed50efd9877a | -11.48521 | -45.09562 | 2026-08-14 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2816b7ad-2b28-330f-b41a-865007b1b0e1 | -13.27513 | -54.236 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 523d4ee6-d001-38b5-8469-b2b66a700886 | -14.44791 | -45.69789 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| adb2bf5b-816d-35be-9ff9-a861e38a5400 | -13.2292 | -54.26672 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c8fb4939-6f8b-34b6-b177-b9eec2be7bdd | -12.52252 | -55.79216 | 2026-08-14 04:14:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd0da538-3753-38f8-be6c-5f08a5084a13 | -13.23924 | -54.25107 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e2aa732-747f-371c-8237-9ba00cf0df6b | -10.29541 | -46.65254 | 2026-08-14 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a21d27e9-7c04-32c7-9d65-8748bad5b5ca | -13.25208 | -54.24879 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd6aa5b0-7eec-32c3-8026-82ca6ba73f89 | -13.28627 | -54.21548 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a630dc7-e044-3828-a2c1-2e85b70461e2 | -14.93703 | -46.62214 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d28b7f77-27b6-3b97-9177-b6d7d05a042a | -7.51184 | -47.4896 | 2026-08-14 04:14:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d891916f-6966-3e0e-8f09-35f36405c59d | -13.24041 | -54.24546 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b88e346-c0d4-38f9-918c-990c99c89df7 | -10.9764 | -50.53583 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea2ca05a-1403-3950-85e2-511aa80c8f67 | -14.46803 | -45.69227 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c8fbf77-a669-318d-bb03-5cbcabc2a003 | -15.14305 | -41.56157 | 2026-08-14 04:14:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 929549eb-412b-36bf-8079-5562dc3e5616 | -11.93297 | -46.33022 | 2026-08-14 04:14:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c46a0de-66df-3dc5-b924-d925e696b9bc | -13.2445 | -54.2583 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 368bcdab-e470-3b52-a65b-29bd3250c108 | -10.73218 | -47.92275 | 2026-08-14 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b18f7953-3b95-3b22-a10f-cf058584c170 | -13.22786 | -54.26682 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f973acb9-6565-3432-9f1a-e950a1499a24 | -11.50781 | -54.61157 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0806a3f-b8c4-3623-a525-ec31a0955e2d | -7.80858 | -44.11927 | 2026-08-14 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49d2cc9f-b861-34dd-89ce-9643a47909e8 | -14.29393 | -45.26654 | 2026-08-14 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40aa310c-89c9-3dd0-8b90-12125e6602a4 | -11.30311 | -44.82671 | 2026-08-14 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00489f8b-931a-39d9-ac33-d6e0eb6e97b7 | -14.47477 | -45.68171 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9045c8de-a0c4-330c-872c-69a9ca0bdfc5 | -14.47174 | -45.69296 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 767408b7-aae9-3962-b8bd-06d78fd81a3e | -14.29757 | -45.2672 | 2026-08-14 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b961ea22-ef9d-341f-a1cb-51c246e1fe9e | -14.47036 | -45.67867 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f792a0a1-5c61-3878-b0d9-54c05b52ce40 | -13.28393 | -54.22645 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2ca640a9-fcb1-320e-b02f-421bbf12c134 | -11.42804 | -43.92032 | 2026-08-14 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a0daf2f-8a70-3c74-9aeb-93cf84c2e206 | -14.4442 | -45.6972 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 92ec261a-ebcd-343a-a573-c70cf1cc15b3 | -9.59726 | -49.32292 | 2026-08-14 04:14:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 893aa1f9-fb6e-330d-be4d-0f593a5ae9a6 | -9.12792 | -46.39891 | 2026-08-14 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad5c6c90-bacc-3429-bdb1-3f3d06338f62 | -7.71139 | -46.23336 | 2026-08-14 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb0fea39-2f01-3945-8d6e-21874650ce4c | -12.71383 | -48.45445 | 2026-08-14 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 022f42a3-bd38-36cc-a569-f0add23ffb87 | -12.03243 | -47.81906 | 2026-08-14 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70abf222-0153-30ab-a13c-e92b033d1bfe | -10.83124 | -50.32337 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a45df05e-7fa7-3a79-831b-1c834691d589 | -13.76295 | -42.61849 | 2026-08-14 04:14:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 94dc0623-f8d0-3cc9-bf46-70601f21bced | -11.88242 | -45.95254 | 2026-08-14 04:14:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2650d22-3c32-3b5b-9848-a247069653a7 | -12.03427 | -47.81276 | 2026-08-14 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 963df985-b494-3b1e-90b1-a50682e9dc36 | -14.47768 | -45.68691 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce5ffc5b-c1b0-39a9-97a3-672016ceef46 | -14.64507 | -40.88509 | 2026-08-14 04:14:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b8a0cd6e-a2c4-318a-ba5d-1f10e5e6d47c | -10.82063 | -50.32125 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 013492da-2f91-3260-b384-368fb6c6aecc | -9.1237 | -46.39822 | 2026-08-14 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 557ec86f-f62c-35a3-868a-79787d47a2b3 | -13.38305 | -42.39318 | 2026-08-14 04:14:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2372feac-2980-30d7-949a-fa96e532829d | -14.93996 | -46.62827 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65b6bbea-4bfa-3178-b3e9-d42e6bc3b156 | -11.06297 | -50.94622 | 2026-08-14 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cfd8392-00e4-3982-b3a5-729b303f6d8e | -13.65299 | -46.25185 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0a57bab-f2ad-3938-a469-c7ed180f509a | -13.2331 | -54.27394 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4324f490-f688-3dbf-9dfa-72598fdf518f | -13.24684 | -54.2471 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc1f14db-4a23-3851-8aca-a75d8a9657c0 | -14.95516 | -46.6103 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df119666-9a5e-3a23-bc13-d7dacd1f8271 | -11.50107 | -54.60983 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b6a00fa2-a6cf-3356-a42e-616293ac5dfc | -14.23897 | -45.41005 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3142482-97df-388b-8c10-2e966604593c | -13.55919 | -46.25845 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d793fefa-8a55-323a-acdf-dcd721ba765c | -11.32021 | -45.21994 | 2026-08-14 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e037702c-2558-3e4e-99a8-1d8bcaff92ba | -14.44869 | -45.69336 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83c117b3-79f5-3a0f-aed1-9b1843d3b4ee | -14.94177 | -46.61798 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b80963d-3875-3bc0-b9e4-4587f3817cad | -14.47329 | -45.68388 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8a10c46c-bb93-3f51-bcc6-75a7607e2a98 | -11.4944 | -54.64164 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| da836eb6-d8d5-3da3-be2f-9272ef507cd9 | -13.39087 | -42.38715 | 2026-08-14 04:14:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| cb8958c6-fe20-381a-b78d-3b156dfc0805 | -11.47135 | -44.56332 | 2026-08-14 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ad75523-4217-3d34-a716-328fed6ff97f | -14.29682 | -45.27156 | 2026-08-14 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 341f9648-2d35-312a-8796-a1b4c3f1565d | -7.8081 | -44.11698 | 2026-08-14 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8471d882-c9b0-36a6-9553-35350c58aedb | -13.56398 | -46.25405 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 98fbb5d3-9294-3e38-b8b9-5832eed2545d | -13.22661 | -54.27256 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f411fc84-f680-39bd-a7a6-60cd9213a165 | -13.24204 | -54.26396 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbc72101-c986-3393-bd96-c5d4696db26f | -13.22799 | -54.27247 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 942846d0-1c3c-3829-8e41-5a4f681bb998 | -11.80386 | -51.80862 | 2026-08-14 04:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7693441e-4639-32cc-9ece-faa012ec9814 | -11.49167 | -54.62074 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 75c2f644-ab06-33f4-8978-e3a4f9cb694b | -13.27089 | -54.22892 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea8b682f-3723-36d8-98db-48d3778c6c95 | -11.88545 | -45.95829 | 2026-08-14 04:14:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af7c6049-90dc-3973-8c6f-ca216345d104 | -13.24933 | -54.23013 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee1ff0be-0d9b-3c55-987d-bf77fa1cffca | -13.55829 | -46.26353 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 707467a1-5f7c-3db0-abf1-d2ee6f6b3a94 | -11.33342 | -46.23131 | 2026-08-14 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c444d61e-47e0-39e4-8076-d26fa851053e | -12.71198 | -48.4392 | 2026-08-14 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b3e260b-8c20-3ddd-a624-fa67b803ed71 | -15.01035 | -41.95033 | 2026-08-14 04:14:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0ec2157e-d813-3095-9862-da43a3cb4f83 | -12.01199 | -46.40162 | 2026-08-14 04:14:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6425627-8cea-35c3-9a71-66262ec65644 | -13.24567 | -54.24712 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 829a54f1-4f9d-3d14-b965-4bbcf1ff8ce3 | -13.27978 | -54.21425 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ef7ef1a-e21e-34e1-aff9-a145029857e9 | -14.97612 | -46.60547 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| be572912-ce96-3c55-b943-59b94f97f152 | -13.28509 | -54.22101 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e87398d3-5d82-3056-8d20-df3041917c35 | -13.2408 | -54.2697 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b42efba4-184f-3fff-a028-3ce67cf52fc9 | -14.46587 | -45.68252 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d212dd8-9803-3b34-bef8-2c70dcc15e5a | -13.23558 | -54.26245 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c245b155-ef4a-3aba-9c81-ca68569d1509 | -13.25039 | -54.23005 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18e5e51b-adba-3e8c-a02f-3ec732ab5b45 | -11.06989 | -50.93995 | 2026-08-14 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e4fb15f-8404-3a68-b761-73932861eaa5 | -10.9852 | -50.54834 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 324dfd68-5a95-321b-b92c-df2280e01421 | -13.86071 | -43.64421 | 2026-08-14 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35f6bbd9-3993-32d5-b5f8-c7beea53ce34 | -14.47316 | -45.69077 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb0b1265-fa31-37d3-bbb3-37c9c4c77a4b | -11.45388 | -44.55584 | 2026-08-14 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 234fd622-fe66-3824-a6f8-09287328c730 | -11.48338 | -54.62715 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cfc0497d-af21-3ee9-9436-eb1e998066cd | -13.56102 | -46.24809 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d8b3d74-3a78-3000-91df-41f820a4bd99 | -14.95594 | -46.6059 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca69fb66-3b90-35e9-ac5b-657f6e8c0f45 | -14.72885 | -48.23022 | 2026-08-14 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 984e63ec-75a7-31f3-adb9-a14af4002d3c | -12.73118 | -48.43676 | 2026-08-14 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c167913-5286-3a5b-87f1-1e5acd54cb5c | -11.47571 | -44.55967 | 2026-08-14 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94c889b7-389b-3be2-8959-88813d2ecd71 | -9.98077 | -53.95713 | 2026-08-14 04:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |


[Clique aqui para ver as próximas entradas](README15.md)
