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
| 881a071e-740a-3db0-976b-2a2678363340 | -23.47631 | -47.17237 | 2025-07-18 03:40:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cc5c145d-70d8-3c11-8672-2ec44e1470e1 | -21.5611 | -43.66641 | 2025-07-18 03:40:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a2a0b951-f127-3cef-af1b-71487d05a839 | -23.95968 | -48.11452 | 2025-07-18 03:40:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75ab2638-2e59-3e42-8be7-ebd49d709874 | -23.95887 | -48.11804 | 2025-07-18 03:40:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e46b74e5-a3b5-37f0-ab0c-db307a53ab41 | -21.07732 | -43.14792 | 2025-07-18 03:40:00 | NOAA-20 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a744b423-0119-3116-9c97-c08ab57f7531 | -23.70472 | -51.66127 | 2025-07-18 03:40:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 2642d637-a91a-3ed4-bef4-a095231f16ba | -21.67309 | -41.6897 | 2025-07-18 03:40:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5bc87696-70f1-3647-ae46-d29ffe77010d | -23.22293 | -49.51326 | 2025-07-18 03:40:00 | NOAA-20 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fa447805-c026-30a1-ae1e-01c33eab70fc | -22.91918 | -47.1955 | 2025-07-18 03:40:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d53ef43c-46fe-3843-8cef-4fd08ce72da7 | -23.69984 | -51.6531 | 2025-07-18 03:40:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 3b484574-4651-382e-87a8-bba358994741 | -20.99466 | -42.96749 | 2025-07-18 03:40:00 | NOAA-20 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 89a544df-c9e9-3ba6-a76d-606b0bc158e9 | -19.8894 | -46.05272 | 2025-07-18 03:40:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea3e8f86-6fb6-3ec5-af41-6e3bfa09a491 | -22.67727 | -47.64349 | 2025-07-18 03:40:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 76a6550e-7293-3d54-b0c9-78b3d015aaf9 | -23.9556 | -48.12053 | 2025-07-18 03:40:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b6f14548-89bc-3447-bf10-82a5f38d31e4 | -20.91077 | -49.06976 | 2025-07-18 03:40:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f6a08b0a-ebc3-3d9d-bc1a-9ee2be04156b | -19.89007 | -46.04952 | 2025-07-18 03:40:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 218a563f-1024-3668-acc7-ed8483556b76 | -20.99257 | -42.96811 | 2025-07-18 03:40:00 | NOAA-20 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0ac036dd-f1ea-34d4-8b4d-3c024f2e54dd | -22.2443 | -49.92537 | 2025-07-18 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f808ebf-9cf1-341d-8174-9def96a80172 | -23.24318 | -46.20085 | 2025-07-18 03:40:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 39885173-4e7f-36ee-b1d8-227305b0b127 | -22.67809 | -47.63987 | 2025-07-18 03:40:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 26fcf0b4-a6d2-35de-985a-776591f8252a | -25.42106 | -49.09655 | 2025-07-18 03:40:00 | NOAA-20 | PIRAQUARA | PARANÁ | Brasil | 4119509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 14e9fef1-ce19-39de-b8d1-1c555a24020b | -23.96252 | -48.11471 | 2025-07-18 03:40:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4936d9c2-d1a8-3451-b038-76f15b401da7 | -23.22173 | -49.51828 | 2025-07-18 03:40:00 | NOAA-20 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3c612d1d-921e-367a-954c-cb39c34092ed | -23.96049 | -48.11102 | 2025-07-18 03:40:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8d44f581-625e-3635-9fb0-86c628be0ba4 | -22.58067 | -44.08139 | 2025-07-18 03:40:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| aa4630a1-dcca-3601-9214-ddbd2816612f | -20.99139 | -49.76904 | 2025-07-18 03:40:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9baddc21-ba2b-3433-a2fd-8a4fa82cb98c | -23.95804 | -48.12164 | 2025-07-18 03:40:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 496cb72b-a271-3462-8b42-b25f3eae9c3d | -20.9533 | -44.33751 | 2025-07-18 03:40:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1cffea01-7443-37b2-a716-f77dd6437e1a | -22.04588 | -47.8928 | 2025-07-18 03:40:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 852308ee-bb94-3a64-98ef-79ce00c9a437 | -22.34684 | -47.16322 | 2025-07-18 03:40:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1db618d-a09d-3a49-ac5f-9c88f740b2d0 | -22.55959 | -42.13683 | 2025-07-18 03:40:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ff71f6c5-f24a-3c78-a9a7-e2f3492a6b71 | -22.24545 | -49.92046 | 2025-07-18 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9aa3409d-f8d3-38ae-9fae-d72b81a4a541 | -22.41794 | -48.15283 | 2025-07-18 03:40:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b94c7365-a911-3e65-9882-b31eda96a58f | -21.67277 | -41.68643 | 2025-07-18 03:40:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b5094957-1885-36ad-add5-039a1e96263f | -22.55699 | -42.14009 | 2025-07-18 03:40:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5cbaa8c7-36d8-39b0-a908-e6659ea59cf3 | -22.56082 | -42.14093 | 2025-07-18 03:40:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc08b7c1-22a9-36e4-af9f-726d435a5cb5 | -22.91991 | -47.19216 | 2025-07-18 03:40:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3676acee-89d2-3ba5-8c4a-b5cfaf741a06 | -22.34608 | -47.16668 | 2025-07-18 03:40:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f20ad01-0f35-388f-9979-5d4584e9ec83 | -22.41844 | -48.15509 | 2025-07-18 03:40:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bfd2265-51b5-3b23-967e-96e9dd37bfde | -23.69816 | -51.65969 | 2025-07-18 03:40:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 78047aaf-a0ca-3fc9-b7bc-1d8b6be0014b | -20.99013 | -49.77437 | 2025-07-18 03:40:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4a04cb65-38be-3adf-b41b-78cb6afc8d30 | -21.67398 | -41.68475 | 2025-07-18 03:40:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3e6697d2-92c2-3f1f-ae63-65bf952263bf | -23.96094 | -48.12178 | 2025-07-18 03:40:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 597ce134-0e3f-39b5-b030-912f8e2f1106 | -22.41699 | -48.15694 | 2025-07-18 03:40:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0639541b-e9b0-39e2-b08d-7de5a68bbcff | -25.42459 | -49.1062 | 2025-07-18 03:40:00 | NOAA-20 | PIRAQUARA | PARANÁ | Brasil | 4119509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| af06eb01-e93f-3f0e-9757-20c6b88cd21c | -22.55862 | -42.14192 | 2025-07-18 03:40:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 98ed59d1-d69e-387b-9310-1f090d55e958 | -5.1934 | -45.4835 | 2025-07-18 03:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 7bd9ca46-9365-3de0-9811-601683b20d29 | -3.3957 | -47.5003 | 2025-07-18 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9b160f06-9e7d-35a2-9b40-409866560247 | -11.7317 | -48.1849 | 2025-07-18 03:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 9e8b0ceb-c386-30e0-8276-7208028346c6 | -3.3958 | -47.4785 | 2025-07-18 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| a3f6facd-bfc3-3a24-a0dc-dca927e4cffc | -8.0886 | -43.1431 | 2025-07-18 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 25410e22-8b08-3679-878f-cda59fc05bde | -5.6569 | -43.6929 | 2025-07-18 03:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a63161a4-825c-3b6d-91ad-b2f7c4dfb903 | -5.6567 | -43.7161 | 2025-07-18 03:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 201.9 |
| f7afbdbe-77b3-3534-ba2d-5cd41961bb22 | -22.4267 | -48.1439 | 2025-07-18 04:00:00 | GOES-19 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 99f31042-2156-35a2-b614-bc8c51915554 | -3.3958 | -47.4785 | 2025-07-18 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 03d63bc4-af89-36cd-bf75-25a9e5866c83 | -11.7317 | -48.1849 | 2025-07-18 04:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 5adb03f9-f122-3d8a-9c1b-b9c0a19d33da | -3.3957 | -47.5003 | 2025-07-18 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7f0cedbf-1049-373a-8762-5716eb86a61d | -11.7508 | -48.1825 | 2025-07-18 04:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 9ea5b42a-0bfa-351a-a693-0e32dcf455ba | -5.6379 | -43.7175 | 2025-07-18 04:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| efd4eb07-ea1d-3871-95a9-c7e05f778b0c | -9.5028 | -47.5642 | 2025-07-18 04:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| f314434f-bc98-33b6-802b-b816960df9c9 | -8.0886 | -43.1431 | 2025-07-18 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 7e476b22-a4bd-3fa8-8e78-a6d3bb0849a9 | -5.6567 | -43.7161 | 2025-07-18 04:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 187.1 |
| aa9272d1-40dd-3c2e-86b0-5baed5fcd7af | -11.7317 | -48.1849 | 2025-07-18 04:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 0d9a859d-c001-31c1-b16d-03b9a1835378 | -3.3957 | -47.5003 | 2025-07-18 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 56d999f8-c76d-357b-a90c-4bd199824371 | -5.6379 | -43.7175 | 2025-07-18 04:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 7bd19d94-7849-3e85-ada5-a388ecaeb5c1 | -5.6569 | -43.6929 | 2025-07-18 04:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 39aaf3bd-6e0b-329d-b80d-e56e5e7dd181 | -3.3772 | -47.4792 | 2025-07-18 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f92b1c61-ffe4-30a5-b78f-91775931b3b8 | -11.7508 | -48.1825 | 2025-07-18 04:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5bb21b11-5fbb-36a2-b0c9-a7a0ab92388d | -5.1934 | -45.4835 | 2025-07-18 04:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 2761a9cd-816c-3284-a90c-d834720c5a72 | -3.3958 | -47.4785 | 2025-07-18 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 82581ae8-d976-39e5-8bac-c923ad6cffc8 | -5.6567 | -43.7161 | 2025-07-18 04:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 06e62c4b-d8a8-3dfc-bd71-3b3a626b9271 | -11.7508 | -48.1825 | 2025-07-18 04:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 06623612-c92a-323a-9dcf-982f0006dd3c | -3.3957 | -47.5003 | 2025-07-18 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 7ad92fe2-13e1-3ebc-a1c3-b7bd223e551f | -8.0886 | -43.1431 | 2025-07-18 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| ebee0dad-9ae2-35cf-969a-b65048416566 | -3.3958 | -47.4785 | 2025-07-18 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 8fd0e5da-07a0-3517-b573-53e0a225d8a2 | -22.4267 | -48.1439 | 2025-07-18 04:20:00 | GOES-19 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 58f7ba61-2857-34ed-9e1c-8d1cd2334386 | -11.7317 | -48.1849 | 2025-07-18 04:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 1fff1161-ddf6-3982-929b-c71b94a06cd5 | -5.6379 | -43.7175 | 2025-07-18 04:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 6458412f-2034-3832-81d8-ae70747bd17f | -5.6567 | -43.7161 | 2025-07-18 04:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| b30b7ed5-a8a9-31db-9b36-b1302086fcbc | -4.81615 | -47.32269 | 2025-07-18 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45ed907e-700a-31ef-938e-ceb10bd37f71 | -4.10645 | -48.2035 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 674a11f7-61e4-3edc-b12d-b05b738f91b7 | -2.63297 | -47.30524 | 2025-07-18 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba80bf30-544f-3190-ab8a-cb2ab7cbf281 | -7.7132 | -45.87666 | 2025-07-18 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 761c7929-ff18-311e-b1a4-1d81a91bdddc | -4.6453 | -43.11984 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ff41bae-fcae-3005-84e2-40ee0619b79c | -5.79926 | -43.62783 | 2025-07-18 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c43d86c-4806-39e0-9ba6-776a63f66662 | -2.7162 | -47.69201 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bbaceeb-5bbf-39e0-8e9a-8e8c0ba8ce5d | -7.01795 | -43.87778 | 2025-07-18 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0b4473b-bada-3afc-9bd6-f2f60a6c7dd0 | -6.51037 | -43.51952 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9438185e-8f10-3af8-80ca-f70a5322047f | -7.25987 | -44.50641 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc3fabb4-985f-360a-8f32-769518f47b64 | -7.47943 | -37.41183 | 2025-07-18 04:25:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dbd8f780-8909-3da3-9d0f-43c3c4280e95 | -7.35369 | -44.19188 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ba9d82d2-2d86-3b73-8356-fc0265baa757 | -5.36509 | -45.12373 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d595d0bf-7b04-33ea-b3cf-27baf1a4da97 | -6.55332 | -43.62133 | 2025-07-18 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d57447e-c035-3e46-b0ff-36fc69900b58 | -4.10992 | -48.20405 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a93912ee-0fbb-37e7-8d8b-ee986d3830b1 | -2.91839 | -48.24004 | 2025-07-18 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7210dc56-8d52-3cf3-aa1f-6e94f432429f | -3.39178 | -47.48589 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 1d47ba7d-e14e-3e0e-a3e7-e6c832f096cc | -5.65158 | -43.71844 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 7307d07f-4248-320f-92da-23552bde5425 | -7.24067 | -42.84794 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c08f082-94e4-300f-b85e-e95257a008c3 | -7.45595 | -44.693 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 138b00e8-30be-3bb1-8101-01db808ad428 | -5.78423 | -45.07241 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README11.md)
