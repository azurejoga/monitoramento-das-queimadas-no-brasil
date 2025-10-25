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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9afea4d6-ff02-3a16-b87e-d812e481368f | -10.95419 | -44.89854 | 2025-10-25 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2772ef0-52ec-3fab-bd7c-73826c91698e | -10.63689 | -45.24128 | 2025-10-25 03:30:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b67dd5d-fbb0-3992-8b24-c1af64ded930 | -7.78336 | -45.39708 | 2025-10-25 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4997dd53-7ebc-321f-aa1e-02ad96e49366 | -6.55213 | -43.2341 | 2025-10-25 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 80229e60-c116-3c1f-929e-3df389945cdd | -11.42975 | -44.67834 | 2025-10-25 03:30:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fecc85c2-809b-3b92-b26e-a878c16f3871 | -7.64095 | -42.16848 | 2025-10-25 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24cc5027-ea81-3121-ab36-860e8c50902a | -8.6006 | -44.82529 | 2025-10-25 03:30:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77f0a903-382d-3a9b-81be-d9af6b3853da | -10.98171 | -44.7281 | 2025-10-25 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69e436a7-1464-3ca0-bea5-4280088652bc | -6.75817 | -44.20564 | 2025-10-25 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca645e98-cb17-33d1-a709-1ed5811c12e2 | -10.64333 | -45.24245 | 2025-10-25 03:30:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15a3e2a7-9f35-390e-9bf3-1a8fbc086cc6 | -12.06559 | -43.98972 | 2025-10-25 03:30:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01694a83-669a-3998-a017-7c93c3e63848 | -10.44783 | -44.96641 | 2025-10-25 03:30:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6c589333-4337-3ae9-983b-12f3882fe698 | -12.05982 | -43.98841 | 2025-10-25 03:30:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dafcdeb8-b67e-3111-86eb-55e89930c3ce | -10.88456 | -45.08238 | 2025-10-25 03:30:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8faeb4c5-f02d-375f-aeca-a6411f79badd | -7.14809 | -44.12363 | 2025-10-25 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed80e419-85b8-3007-ac64-2c02444042d4 | -10.41892 | -44.49617 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 84aa2173-056a-321a-9ea6-23146df16478 | -10.6372 | -45.23426 | 2025-10-25 03:30:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| adcede43-4e21-339e-a657-e149e1113850 | -10.63797 | -45.23597 | 2025-10-25 03:30:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b28ea25-ff81-37c6-b644-37f2c7edff9f | -6.76359 | -44.21222 | 2025-10-25 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 881123b2-d6ff-3c89-972d-9ad36649104c | -6.81012 | -42.39764 | 2025-10-25 03:30:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1483ef0b-54e0-3b44-93d6-913d583d90dd | -9.31905 | -45.20256 | 2025-10-25 03:30:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9cdf024a-b01e-3339-a467-9f581d42659e | -10.64364 | -45.23539 | 2025-10-25 03:30:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36f5a60b-4b2e-3ef1-9fca-2eaa8a3be3f3 | -10.56145 | -44.93604 | 2025-10-25 03:30:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 426846c5-b17d-3e75-be37-ea3e642df535 | -10.17418 | -44.66645 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17c144fa-c288-3ab3-9fc1-345772735273 | -12.4826 | -42.77044 | 2025-10-25 03:30:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2d63a8f-c84e-340a-b08e-e3b570b07937 | -7.59585 | -40.98877 | 2025-10-25 03:30:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a8e3b3ab-f321-3e83-8071-084d6d1b1176 | -7.58333 | -43.58116 | 2025-10-25 03:30:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d65eed6-a7da-3021-93bc-fcc67bf7566e | -6.64935 | -43.60921 | 2025-10-25 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 985eb8ca-f3a2-3589-85fa-c5f0cbbb215c | -8.60173 | -44.81944 | 2025-10-25 03:30:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93a17467-8d06-3a1f-9144-c5acc6f45b9c | -10.44989 | -44.96852 | 2025-10-25 03:30:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 73bc542f-626b-3359-845f-db73e7bc5b5c | -6.64315 | -43.60802 | 2025-10-25 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b08b2fdf-9b6c-397c-8bf7-4c46396639cd | -7.64583 | -42.17346 | 2025-10-25 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b89248af-81d2-3d69-b1dc-2b5f7474caa4 | -7.84884 | -40.90216 | 2025-10-25 03:30:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e183c13c-6a35-35a9-ae35-86fc6a72eb1f | -10.87823 | -45.08116 | 2025-10-25 03:30:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1b605a0-38ca-3f56-ab3c-b3b4ddc985d9 | -9.32009 | -45.19738 | 2025-10-25 03:30:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 390c61e1-e1b7-3818-8693-99fd88ab1805 | -6.81204 | -45.43456 | 2025-10-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 535778e2-ec8f-33a1-beec-58097c3d0208 | -7.645 | -42.1692 | 2025-10-25 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ae078a0-a8ec-3c44-8a1b-08b6985f40cd | -9.27288 | -40.53101 | 2025-10-25 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b54ff37a-f1d1-3028-bce2-3b609748c800 | -9.32348 | -45.18536 | 2025-10-25 03:30:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4674e418-de87-397b-8e9a-5f6b720f47a7 | -9.32035 | -45.20156 | 2025-10-25 03:30:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76eaf0ce-4cee-33a2-bba8-58ef46fbcddb | -7.58941 | -43.58242 | 2025-10-25 03:30:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0df7e91d-8030-33b0-bafd-0e3d8e981675 | -6.96558 | -43.49799 | 2025-10-25 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84eea627-7ebb-335c-9cfc-464a67388776 | -6.54482 | -41.68703 | 2025-10-25 03:30:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dcf79626-d035-3c53-b1d6-5e23092f6a09 | -6.6484 | -43.60567 | 2025-10-25 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39f653e3-066a-379b-83f6-c653c6dda76b | -10.41794 | -44.50118 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1e6d4df2-4c2e-35f0-951e-54b8a91ec260 | -7.79027 | -45.39772 | 2025-10-25 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17c9fce3-18be-3fb7-833f-61135b509e1c | -10.64441 | -45.23709 | 2025-10-25 03:30:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7309373d-81b7-3f3c-96dd-280f012b59fd | -11.98886 | -43.31503 | 2025-10-25 03:30:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb4cfed2-ec5b-321f-b368-359867ab3851 | -10.6426 | -45.24075 | 2025-10-25 03:30:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b652d1e9-f74c-325f-8dd5-37f615f3dec3 | -6.59628 | -42.0776 | 2025-10-25 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f43a779f-2fc5-3f37-80da-826c2c28a8fa | -6.76458 | -44.20692 | 2025-10-25 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fe2eaf3-d931-3cc6-ba3d-e7dda25d19f1 | -10.95322 | -44.90341 | 2025-10-25 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| baab5290-7ab8-366f-b01e-17215d3fce13 | -7.5851 | -43.57184 | 2025-10-25 03:30:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 44670096-23b7-301c-a573-52b9a1a97394 | -7.64428 | -42.17308 | 2025-10-25 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3f1d8923-a671-3e4d-b26b-2766eb9d4737 | -9.32246 | -45.19067 | 2025-10-25 03:30:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cce1f4e3-53a6-3b01-8630-88b3d19d0768 | -12.05912 | -43.98932 | 2025-10-25 03:30:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f43eaa58-0aa4-3ecc-b8ad-7ee4c180c2c9 | -9.32137 | -45.1963 | 2025-10-25 03:30:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b9ad205-15f5-3374-91bf-4e07f908151f | -10.45422 | -44.96738 | 2025-10-25 03:30:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec07ec0e-65ab-384b-93bd-8c65401ad2cc | -6.80513 | -42.39243 | 2025-10-25 03:30:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4cc3f229-24a3-3058-9dfb-5f41ee2cc166 | -10.41296 | -44.74573 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a134dee0-1bb7-313a-a379-53ae09274b7a | -10.42456 | -44.49485 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f59042a-786a-3f42-ab02-b6973fb2d4bf | -6.96472 | -43.50515 | 2025-10-25 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 132378d1-29d4-37e4-a997-5c72d91e4a41 | -9.3223 | -45.18633 | 2025-10-25 03:30:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e3d5f303-f59f-3934-aeb5-ff3bc069cbbe | -8.60284 | -44.81369 | 2025-10-25 03:30:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35333372-1ee9-3e8b-afe8-12f6cbb3245c | -12.08753 | -46.42754 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 3b287ca3-8675-3f83-9288-5bbbd7bfa666 | -12.29703 | -47.45191 | 2025-10-25 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ffe6a02d-1025-351e-a643-232a1a74e595 | -14.20187 | -47.31169 | 2025-10-25 03:32:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18a7b0b1-6cb6-35c8-89cd-7656c93089e4 | -12.08897 | -46.42078 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 93ecc783-b4b3-3c0d-824f-5ffa0836b2e4 | -15.21982 | -47.9172 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1389f204-5563-3103-9019-d93d2e856790 | -15.57652 | -43.22083 | 2025-10-25 03:32:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 318b7a6e-0975-3443-bcc2-bc8160732d0f | -14.71948 | -46.62057 | 2025-10-25 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 953f00b6-c762-3959-be3f-1969eb38d566 | -16.17154 | -45.08817 | 2025-10-25 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 621aac6e-4c1c-3a00-8976-8e7ace954d21 | -14.8666 | -48.10631 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 7ad56f58-6a87-370a-85a1-ee57e6b89d4e | -15.21813 | -47.92482 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b9c1acc-7127-3cc8-aa81-e0c0a1b5c212 | -12.08477 | -46.42653 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2909237c-8e4c-3adb-8718-4db3d7814831 | -16.17135 | -45.08941 | 2025-10-25 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b76dbf5b-9526-3458-8575-5561ba6e359c | -12.07823 | -46.4056 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e35e37bf-52f0-3464-854c-848f86531442 | -15.22521 | -47.92296 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b93b9935-59cd-39f0-be4a-1b07c99f3969 | -14.89935 | -47.8712 | 2025-10-25 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 990cb832-1e78-3cce-abc8-4b043b1e98cf | -15.58235 | -43.21863 | 2025-10-25 03:32:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ddf7fd70-19f7-315a-9178-84edec9cb8e2 | -14.76739 | -43.08078 | 2025-10-25 03:32:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 637ed97c-12b9-3f28-9a50-1141c626c96b | -15.23732 | -47.9334 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 922d0552-6227-38bf-ab3d-63ae5864d899 | -17.41644 | -46.87953 | 2025-10-25 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 81f7554a-d902-3afd-b3b8-3029b98cb0d1 | -15.23563 | -47.94083 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b98a0075-c66c-3329-a531-98f26d09cd66 | -14.86316 | -48.10071 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 618450e0-138f-315d-949e-40842db13b2b | -17.37087 | -45.49681 | 2025-10-25 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78647819-d6f5-3ab7-a26a-c2d9e215760c | -14.5422 | -48.02362 | 2025-10-25 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce7872d2-d9bf-3e25-afd0-eeb117c26493 | -14.86479 | -48.0933 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b1fb49c1-8372-3172-877a-1df119815ce8 | -15.58335 | -43.21781 | 2025-10-25 03:32:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9027334f-44e0-3b28-8259-fdb7d57bd53b | -13.45073 | -44.06761 | 2025-10-25 03:32:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b52d4417-05c0-38cf-ac18-a7dac2674738 | -13.45642 | -44.06876 | 2025-10-25 03:32:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97b593bb-55f2-3234-9600-428cdf686d4c | -16.17225 | -45.08521 | 2025-10-25 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81343609-221e-3d42-a99b-e37f3b748982 | -14.54044 | -48.01995 | 2025-10-25 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19214386-6e3b-3fc5-8b97-95f05979f817 | -14.20279 | -47.31266 | 2025-10-25 03:32:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c0d0f3c-3b17-30bc-a7c8-d47367a411a2 | -14.33685 | -43.74028 | 2025-10-25 03:32:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 27d2c2ed-8df0-3861-a635-2d5bfd4e9187 | -15.57683 | -43.22331 | 2025-10-25 03:32:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2da6c09e-1264-3836-93dd-01ed7fd91fc2 | -16.21457 | -46.47245 | 2025-10-25 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57e43d26-3895-3835-9bd7-3843f53a5279 | -12.0808 | -46.41189 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b81e8381-ec23-3757-9b68-ce431ecc2c5c | -14.89253 | -47.86921 | 2025-10-25 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49fe6de3-d4ac-3e36-bcb9-d089d24da51e | -17.38222 | -45.49949 | 2025-10-25 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README11.md)
