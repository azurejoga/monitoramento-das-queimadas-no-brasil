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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1a14649-c348-333f-983b-96bc932490fe | -13.77399 | -52.71272 | 2026-09-24 05:06:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b63a8c41-9d71-33fa-bb97-ad318bf813df | -12.32263 | -50.2315 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bb3ff3c-3a82-334c-a64e-703b8593239a | -11.7959 | -50.97983 | 2026-09-24 05:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a36c468-ab80-3579-924a-82443b5eb5c7 | -9.00604 | -57.13593 | 2026-09-24 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fcab4d7-0ef5-32bb-9e19-f99a1bf006b7 | -12.15151 | -50.75291 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d19f5cb-f8bb-3409-a031-4e217ccbcb61 | -11.65608 | -43.49525 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7b4c6b24-5c17-30f7-a91e-1438ad3c6875 | -14.57172 | -54.13404 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e70190c0-73a4-3551-949e-ff43b46c808a | -12.14741 | -50.72352 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d7d60bdf-69d2-337a-ae4e-c6564b28ae7d | -10.61232 | -54.0089 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a38c58ae-6c01-3cf5-a21f-eb05665a2c36 | -11.41846 | -47.39922 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0425aca0-1725-357a-b314-4c1bc75fa9a9 | -10.90658 | -53.94263 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55988d0a-b54b-38f3-bd7a-9e33a5c55e09 | -7.89906 | -61.17227 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c6523c58-ba23-3a7e-ab83-007c936f4e3c | -11.20756 | -54.12704 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e34b188f-dbf6-30b9-8f94-efd996f3bbbf | -10.89627 | -51.52249 | 2026-09-24 05:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0c0efd9-5c14-3e30-955c-a21a1a0f8bf8 | -10.61792 | -53.99494 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50217632-19a4-3771-a11c-f406e291dec3 | -10.70228 | -48.72437 | 2026-09-24 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0332ec9-56f3-3605-b8aa-f4de066d49cd | -12.3138 | -50.20295 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20d7b398-57aa-3217-8f8c-db87df89a813 | -12.01354 | -50.31295 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf81e220-bf7e-3f94-bb1d-04007cd7a84c | -7.88428 | -61.17878 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a72753e5-db68-38a2-994e-8c5848c45191 | -7.88353 | -61.18307 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc13195c-b337-3c0d-9484-769fe8f6f2ad | -11.39028 | -47.37672 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a9cd1d0-a384-38a8-93b7-35be09b156c0 | -12.15249 | -50.74585 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5b32f3d-4c91-39b2-95bd-9673c3d8f081 | -11.39208 | -47.36338 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45915615-46cf-3b1e-9fb3-b98a7ad1c6fe | -12.13696 | -50.74001 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b93381ef-28a9-37f4-8712-db4047d98fc9 | -11.43807 | -44.20818 | 2026-09-24 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| ff6b6047-d457-3c96-85f3-9e5bf452cf85 | -9.84286 | -48.50164 | 2026-09-24 05:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c62dab4d-222a-3b10-9e40-19348f38e546 | -10.61903 | -53.98769 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9730f7e4-7539-3b9d-b1e9-57bfc117e887 | -11.95609 | -50.75306 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4f622a1-f9df-365a-848e-8dcf50f45879 | -10.22547 | -57.82879 | 2026-09-24 05:06:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5abb3f3e-802b-3e44-805d-9c697d3dec8b | -14.62751 | -50.60785 | 2026-09-24 05:06:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b1a017c-98b8-38fd-99d1-37daf93b2589 | -10.13953 | -50.21816 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf652f51-913e-32e6-bdbb-bf5222018a1a | -11.93748 | -50.74054 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e8beca5e-ce2c-361c-9b17-d99a5c693f78 | -12.1395 | -50.75116 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b686e260-73da-354e-b2a8-75ff8e54630c | -10.27669 | -49.95341 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88684028-8735-3cd4-a335-82c59959e57a | -9.49741 | -64.03685 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e609df64-08f0-3a80-8977-243bd5417dfe | -10.90713 | -53.93897 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81af4e2c-c520-3efe-ae2a-393bd5054104 | -10.45025 | -46.29006 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01fb9b79-5e06-3a98-a537-c964c31cb7e8 | -10.27151 | -49.96023 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2380dd0a-62a5-3ba6-bebc-7c2009a18458 | -11.86116 | -49.94948 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d52d8dd-6b93-379a-b19d-139eac973bf0 | -11.42773 | -47.40554 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f613f64-58d2-367c-8128-738c58047acc | -10.25399 | -50.28922 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e48196f-1083-3ce4-8d0b-3e2b2e2618f0 | -7.89098 | -61.16649 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ae53342-ea21-3c48-bdf8-741ea3cec9c9 | -10.44982 | -46.29326 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ddfb8e8-0d5a-38b0-99d9-fa89d0599314 | -11.01124 | -49.70836 | 2026-09-24 05:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41689ee7-e158-362d-98ed-c8adcd736990 | -11.41281 | -47.40382 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4fcf6d00-014a-3998-8a48-4982863c1678 | -8.49915 | -57.61447 | 2026-09-24 05:06:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 624cd468-a794-34d5-b4bb-171a2602dd66 | -12.10897 | -50.03024 | 2026-09-24 05:06:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e09cc28e-ce22-32c0-9091-ce5db2a084d3 | -10.41692 | -49.36547 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d9f72595-eb20-33cf-b9d0-094e64ca8ebc | -13.41258 | -60.00555 | 2026-09-24 05:06:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 484e3117-ee0e-3150-a048-ea9783425dae | -11.39523 | -47.37749 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 900e12a8-2907-33d1-847a-f137fdfac2c4 | -10.97861 | -54.09187 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52a773c3-c988-3a56-8193-bdda124b6200 | -14.62434 | -50.59946 | 2026-09-24 05:06:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a129ec19-afd0-3e5f-8f03-f354a52e3b10 | -12.12446 | -50.74179 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1090c0e7-6fcf-3f5b-b93b-99d49c8713c5 | -11.92248 | -50.73122 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e24d711b-52ff-3081-bb7d-8b0dcc9f6d96 | -9.04031 | -65.42353 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8bb40e0-529d-3e68-b337-31dd29acab27 | -12.42002 | -46.96394 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6087e444-c0a2-3114-84ed-f659b9ad034e | -11.86482 | -49.95398 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9789855f-9fd8-3eed-929e-c4aa061f2210 | -9.13324 | -57.55216 | 2026-09-24 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cb0d733-0220-3643-94e3-a44e50b9e787 | -10.43683 | -46.26972 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 265bbb12-b627-3d7a-a30a-b6dca6f46542 | -12.6889 | -47.02694 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfdb4cfc-8392-358e-bf52-1ca2b5e25736 | -10.28025 | -49.95771 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e9d386ac-5d20-37b2-92be-a393f13288b0 | -10.26795 | -49.95592 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a8dfce2-7d3d-39fb-b186-373a1cf5ec96 | -10.42007 | -49.37419 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4e3b047d-6283-3f36-b301-1a02f33fcc21 | -12.13857 | -45.63082 | 2026-09-24 05:06:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d89e3474-68ea-3776-a481-d02251c0132b | -8.6829 | -62.89582 | 2026-09-24 05:06:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c65ae46-f51c-3c3d-a58d-e4e036ae24b0 | -8.4512 | -57.6188 | 2026-09-24 05:06:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bb479d94-094a-36fd-8371-4630505ae152 | -12.70277 | -47.00086 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44f1eba6-13a0-3d9f-8c90-ba22cbb6cc79 | -14.62905 | -50.59606 | 2026-09-24 05:06:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69ee19ce-fdd4-399f-899c-5f0f35fc0e57 | -13.7888 | -54.06459 | 2026-09-24 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b628b78d-daf1-391a-a12d-ffd129d869c7 | -10.71068 | -48.72984 | 2026-09-24 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76e0089d-a607-3045-9944-ec7674856fe8 | -9.85892 | -48.50116 | 2026-09-24 05:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62381b5f-ff54-3bee-959f-84871f3ed43a | -14.55909 | -54.12401 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f696eb5f-4ef9-35b2-bec6-cf5c69b96e48 | -11.40291 | -47.40235 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e7069ce7-c2ef-370f-9f84-6a6497aa25c5 | -12.12543 | -50.73474 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6a1ac4a3-d3ad-36ec-b374-d85a28bd47ed | -7.87912 | -61.18231 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac749717-6ad9-3c2e-8d74-b89f41efaacf | -10.91221 | -53.951 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef94e42e-9a44-3ce4-a37f-fa5652bd3e3d | -12.15717 | -47.35921 | 2026-09-24 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c7388b7-908f-3778-9137-a13930f0ee70 | -12.11868 | -47.38195 | 2026-09-24 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 715211a0-4390-3147-a810-0f06e5bfef6f | -10.61848 | -53.99132 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4a74785-25e7-3470-bbc9-b029fda33bc4 | -12.13988 | -50.71881 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a354e69d-1a8a-31e0-bf5a-1a5056deb6c8 | -11.65067 | -43.49596 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2175c94e-60b5-3e31-9115-07d235137328 | -12.41119 | -46.94998 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04822d6d-293a-35e1-8db0-5177416b5da8 | -11.91752 | -50.73764 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 51b10c3c-7f83-3c7d-82c8-bb166e7692b4 | -13.4627 | -46.26525 | 2026-09-24 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 877b522b-ef21-3ce3-a8c3-affdb47d5fc9 | -11.64547 | -43.48444 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0648f4e8-705a-3c99-bc37-8f439b19c0f7 | -13.78823 | -54.06838 | 2026-09-24 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 127f8785-93c3-3a8d-b66e-26deb7230f01 | -11.64966 | -43.49446 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 394335b1-73be-3ed4-8f51-376e3191a4e5 | -11.12312 | -48.30499 | 2026-09-24 05:06:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9784a276-52f7-3363-a223-be7e98e0c294 | -10.41749 | -49.36143 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 16930ee4-4d22-34c2-91d4-6ae0046a870a | -11.43425 | -44.18847 | 2026-09-24 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 62aa3974-1d88-3110-a77f-b86c8e401f19 | -10.38283 | -54.41386 | 2026-09-24 05:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8258a593-79f9-3f82-8297-0ce32d7e2ef9 | -14.56828 | -54.13348 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 451b579b-26a9-3315-8c2f-e2f01fa8fc44 | -11.62846 | -50.6055 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 32cf65fe-7e22-3023-b9d8-368854d05f4c | -12.92878 | -50.91499 | 2026-09-24 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d5752c6-c196-30cc-9e45-70cf5a831fac | -11.94147 | -50.74112 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3a3e4f36-1c7b-3474-8824-912f02106fef | -12.00412 | -52.46695 | 2026-09-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 3206da9c-c095-3087-bcd2-5512fac0570f | -11.635 | -50.61725 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b20d5ce5-8b33-3218-9815-c5674e198131 | -13.93629 | -47.82485 | 2026-09-24 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0919b2c-989b-3279-8c24-e754dcfef39a | -13.17546 | -51.54346 | 2026-09-24 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b57e732-9146-386d-951d-bac51983a780 | -10.90602 | -53.94629 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README78.md)
