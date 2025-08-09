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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 143a3414-669a-368d-ab34-9e85111fad55 | -6.09169 | -59.92903 | 2025-08-09 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1fa3f37-9aa3-38bf-a1e9-868e3cb1b37f | -9.86554 | -49.96696 | 2025-08-09 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c210160-524c-3f54-8708-8e4ed5652e0e | -8.90697 | -60.547 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48fbe036-457f-3167-bf11-a14db91d85b2 | -9.94019 | -60.477 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da2d35f4-2bea-3e20-bdee-20586773d10d | -6.59937 | -43.37068 | 2025-08-09 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b152dc73-142e-3dec-b23e-0566607f994f | -9.5215 | -45.41289 | 2025-08-09 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55039b75-6160-37ce-a299-0fba47634c46 | -5.00687 | -56.03802 | 2025-08-09 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20b4d4d9-1e57-3458-8213-54a16128dc21 | -9.92752 | -60.484 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93b62ec0-7bc0-3ac2-a71f-1bb93723ebb8 | -5.81495 | -59.22736 | 2025-08-09 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f2214bc-f9fd-3c00-821b-0d9ddf8cadfe | -8.86331 | -47.27343 | 2025-08-09 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37a4c4e2-3eb5-32a6-9abc-34200f45d930 | -6.54881 | -43.18938 | 2025-08-09 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d98ef0d-bf59-3794-a7cb-94162e68cf6b | -7.05409 | -59.21005 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d5ae98b2-7291-37c7-be0a-7348d87b146b | -9.02934 | -59.75965 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e764c36-98f3-3ce7-b707-edd1ace7c3e8 | -7.40749 | -59.99686 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71ca13e0-27d0-3c6b-b455-1c350b34a7b5 | -7.06937 | -59.16138 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7413c5d9-bc0d-3d47-b375-c2cc0f3b6ec6 | -10.17998 | -49.50869 | 2025-08-09 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc102350-50f4-310a-ad68-51e1a2f8df9d | -7.25891 | -44.66296 | 2025-08-09 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ccdc941b-6d04-3c73-8053-498cc66a4ecd | -6.60261 | -43.37954 | 2025-08-09 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8ed3c9be-31fe-3e2a-a081-bd1c6c59d0f4 | -10.74598 | -48.18676 | 2025-08-09 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f405cd04-d030-33e6-9b53-0bd1845de238 | -5.00025 | -56.03698 | 2025-08-09 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0654d404-6ecc-30e3-9e73-8c634baf80e2 | -9.02999 | -59.75566 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91fd9557-322b-30c4-af1c-2a965103a5bf | -7.07573 | -59.17765 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 26a43702-b19c-3392-abeb-725294a9c1c1 | -9.92021 | -60.45958 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c860e7a8-69da-34c5-859e-73f90153b9e4 | -6.15778 | -55.80636 | 2025-08-09 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7365ae22-e926-307c-b4cc-09d5081d3ca0 | -8.91962 | -60.74503 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03abf1a0-7be4-32bf-a915-892f23d7b560 | -10.88038 | -56.09528 | 2025-08-09 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 521ba5f6-4ae0-360f-a461-1a11ef8ecb5d | -12.56494 | -47.11819 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2527df4a-52f0-3660-960b-3e1d8d3645f8 | -11.0872 | -50.46762 | 2025-08-09 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2c000da-dfad-314a-832d-68a61c481018 | -11.32559 | -55.22189 | 2025-08-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 552fdb41-dd28-338a-a9f7-c08f84f452b8 | -7.0723 | -59.1661 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d2624f7d-d305-3ce6-aa9d-8872f3d4a4cd | -14.53021 | -52.11948 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a61a9ec-00f3-376d-8dff-1168ef60ba5c | -13.62791 | -49.01424 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce29bdfc-c6f0-3194-8897-1b2ccd3cbb16 | -13.05092 | -56.85059 | 2025-08-09 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93122d18-8763-33b7-80f1-1d31b527f287 | -12.49707 | -54.41423 | 2025-08-09 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 153239bb-d826-3d4a-bf85-df3fddede8c5 | -13.62855 | -49.00906 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 651279b2-97dc-3c72-96f2-417ee8a7607f | -14.39313 | -56.34659 | 2025-08-09 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cef3b0d-1522-33f8-b7af-d86ffc36733b | -17.51227 | -50.29367 | 2025-08-09 05:06:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3f53a1c-c53a-3edd-b6f8-727f2165f3f7 | -15.91262 | -48.95763 | 2025-08-09 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a5479e7-331e-327a-b9ac-5725dcf34e55 | -13.55351 | -55.25023 | 2025-08-09 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7f6189ec-4325-357a-877e-b02ee1647d6f | -14.52968 | -52.12337 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9691f4b-ddea-3481-918f-0288ec7a0cce | -13.61003 | -48.9919 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aaf86e24-18a2-3910-99f7-6a39c7268dea | -15.91784 | -48.95864 | 2025-08-09 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 999ad593-d3dd-387d-99a8-b8ecaff7dab3 | -14.53074 | -52.11557 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed12f128-158a-376e-a3bc-d646e8f0b7a4 | -14.37836 | -50.32198 | 2025-08-09 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93fa7c3d-4b9d-3f80-ba2c-d56f673d6b4a | -13.6054 | -48.98757 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6e2eb456-9fd3-3c09-bd5e-49d174894cc0 | -13.61252 | -49.0136 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62c86f55-f16a-3300-847e-4f1ddf632f76 | -14.50471 | -52.11969 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d2d5bb46-8488-369f-9ce4-55109eb4ecc7 | -13.55292 | -55.25412 | 2025-08-09 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 48076752-f546-344c-8f06-1e11946503e0 | -13.6276 | -49.01669 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c21aee9-3b44-31ae-833b-eec646811cb6 | -13.61795 | -49.01138 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a8d96fe-1c68-3d6b-b759-0488b921ad1d | -13.04705 | -56.8536 | 2025-08-09 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eee1067-2ac7-396e-a475-56e1a82fffc9 | -13.6186 | -49.0061 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23a37ec8-afaa-3773-a2e1-e41dbb3de296 | -14.49689 | -52.11462 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d48b681-a13b-3bfd-8ffa-2656e644f854 | -13.04982 | -56.85769 | 2025-08-09 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0875a06-5094-3f60-afb3-216b444b0983 | -13.6323 | -49.02032 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dab9fa8b-1b24-3c2a-a132-17b9fdab5bdd | -13.61317 | -49.00829 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 943c3af5-fc57-3c7b-8698-4ed8754f4017 | -12.49587 | -54.41695 | 2025-08-09 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8d7e720-6b26-3e9c-a1be-4f5aaf58f0dc | -13.59996 | -48.98983 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e29f87bd-f46d-3e53-a664-5dd617ab2672 | -13.0476 | -56.85005 | 2025-08-09 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0f47dac-3f5e-3649-a785-b7f76427b662 | -13.05424 | -56.85113 | 2025-08-09 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df5f2785-f81a-314e-bd7d-8049de94354f | -18.54037 | -48.22393 | 2025-08-09 05:06:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| be998a55-249a-3a9e-a813-04880f1360eb | -13.61046 | -48.98844 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cb89581-f65f-3069-8eac-f711d880af56 | -13.55004 | -55.24972 | 2025-08-09 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9bb83fe5-2f75-3379-b96a-77ede78c689d | -14.50106 | -52.1152 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02ce73ef-2a36-32f2-a745-83cde25acdac | -16.98669 | -49.29815 | 2025-08-09 05:06:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22cee08c-fcdb-34ae-b3cf-28e271db6cc0 | -13.62297 | -49.01245 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d6a7510-f863-36ac-83f5-5c9666f8305b | -18.5408 | -48.21989 | 2025-08-09 05:06:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7172eb3b-3d3c-35a6-837a-d5842810ceda | -13.60462 | -48.99395 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aef6276b-e620-3877-88fc-432582bb12c8 | -16.98111 | -49.3008 | 2025-08-09 05:06:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cca44aa3-24e1-3dae-b5f9-c154e706bab3 | -13.04318 | -56.85661 | 2025-08-09 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4741c6ac-4efa-308c-af4c-a7b4af63e192 | -13.04428 | -56.84951 | 2025-08-09 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30560c88-69c1-3a72-9b59-25cc94c891f1 | -17.5136 | -50.2822 | 2025-08-09 05:06:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c2d50ec-a6fb-3a75-8ee4-ff087be1199e | -14.45512 | -52.07692 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c4db059-ec4c-338d-8522-b745247be408 | -13.04484 | -56.84596 | 2025-08-09 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f125e218-c225-3a18-89bf-7a52bbc3c029 | -13.62329 | -49.00986 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1828979-4bbc-3bb4-8a14-b4e293794630 | -13.61828 | -49.00874 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3cd3600-a764-3562-a7fd-55b6657dc348 | -13.05037 | -56.85414 | 2025-08-09 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 021e4f3c-229e-3482-bd98-b8d1530c7c6a | -13.61285 | -49.01089 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb542250-7dfe-3d3d-937c-e8932f49596a | -13.62002 | -48.9947 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7fd61111-1481-307f-ae59-2dca03e738b5 | -13.03986 | -56.85606 | 2025-08-09 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f42963d2-59cc-39d8-a56f-750123aa48c1 | -14.49741 | -52.11072 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef43fda5-af28-396d-a97f-33186ff66813 | -13.62264 | -49.01512 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 830d796f-8ea6-334a-aeef-9615699253f6 | -13.54945 | -55.2536 | 2025-08-09 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 12717561-385a-3168-8c74-732c93cb6f7b | -13.60501 | -48.99077 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a365d522-5a47-3cc0-8fd5-122da5ef28f0 | -13.60579 | -48.98442 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c85be99-ecdf-3325-93d2-be4b8b2e67fd | -16.96161 | -51.05139 | 2025-08-09 05:06:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1698437d-4767-3065-812e-fcea3db3c8a5 | -17.52341 | -50.28355 | 2025-08-09 05:06:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a071cbd-129a-3130-bf4e-7e98d5d9b330 | -14.45145 | -52.0724 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74c117d3-e561-348d-83c1-d0dca31824c6 | -13.60618 | -48.98128 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51034f71-e608-3c2c-8e99-b93a7dc65763 | -13.62822 | -49.01168 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b91a32ab-cd83-3ae0-bcef-f13476839d2d | -13.54887 | -55.25748 | 2025-08-09 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0313db28-abc0-3dd9-a5c3-db4798104307 | -14.45002 | -52.07269 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94c2450f-0665-37bb-bce7-6209865ba57c | -13.61963 | -48.99783 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f95d62c9-2bef-3271-ae07-5c0f2438994e | -18.54317 | -48.21965 | 2025-08-09 05:06:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| de0567d3-bcf7-3afb-80c8-dd112f4fbc73 | -16.96222 | -51.04634 | 2025-08-09 05:06:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29db4711-7efe-302e-ad22-583733a751ab | -13.62362 | -49.00728 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba2d9dcc-11c3-3fcb-8023-f704582f242c | -13.61503 | -48.99324 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52e0bf49-2a08-3601-9fe0-77d52cb9eaee | -18.5465 | -48.22052 | 2025-08-09 05:06:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d859c758-b1e0-3021-8e0e-d98aef58ff3f | -13.55639 | -55.25463 | 2025-08-09 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7154ce37-8fd1-344f-a505-5eadfaf7a5a1 | -13.63261 | -49.01783 | 2025-08-09 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README29.md)
