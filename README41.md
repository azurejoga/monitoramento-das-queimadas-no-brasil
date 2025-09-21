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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a1d2f3e-ced5-336c-95d6-87cbb9b5ce81 | -18.46428 | -47.24926 | 2025-09-21 04:59:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18340eea-b17c-3908-90a6-d92998ee137c | -19.07394 | -49.00226 | 2025-09-21 04:59:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd31de12-8faf-3bdb-b5c4-d34f6148ca96 | -15.96788 | -59.41178 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 250a36d2-a73f-330d-9486-b923125509cd | -15.97356 | -59.42149 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e3dc3a7-9b44-3061-a1b1-98103db98c38 | -15.93269 | -59.43328 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 67b8461b-c6bd-3091-900a-8d28abaf55e4 | -15.92343 | -59.4444 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 53222313-2543-3046-95b1-40c2c26099fe | -19.62035 | -57.73259 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7bed2a2d-57c5-3ed0-9bef-8f1560953959 | -14.81367 | -51.38435 | 2025-09-21 04:59:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b32c68ec-d68a-3de9-ae3b-730487050f56 | -15.88015 | -47.29728 | 2025-09-21 04:59:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7faa348b-c4f0-3b9c-8406-fa726a75101d | -15.87376 | -47.30685 | 2025-09-21 04:59:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab56868a-25fb-374c-b260-20e436b3a7e8 | -15.77178 | -59.43526 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3170fadd-1e0b-3bf7-987a-cd7002b2388d | -15.41263 | -58.77824 | 2025-09-21 04:59:00 | NOAA-20 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88a57182-6b0b-3f22-9257-ade7efb2479d | -15.81943 | -59.50253 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27329657-6351-3975-b2e6-5f2567468d13 | -14.74182 | -60.21204 | 2025-09-21 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 136eb8e8-5901-314b-b60a-cf88981b4734 | -15.79007 | -59.47942 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 793186b8-b476-3c4d-900f-c49b7ac9b784 | -14.38152 | -60.3347 | 2025-09-21 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7648ac9-e08a-3447-bd62-b162627de948 | -15.68087 | -56.12675 | 2025-09-21 04:59:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccaf4303-fe7d-3ac9-85e9-9645f450adab | -15.79566 | -56.17483 | 2025-09-21 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4cc8a346-2e6b-33e7-94fa-d5a25b1aa7de | -15.29348 | -59.41822 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 992862af-af06-3510-ab2d-fd65acdc49ee | -15.99438 | -47.27443 | 2025-09-21 04:59:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ad3e4f8-bf01-3531-b1d0-bb4e2b8dfc16 | -15.27399 | -56.85153 | 2025-09-21 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0a1e91fe-4a50-3363-b4b6-a786df1e4226 | -15.28988 | -59.41763 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91705f84-64d8-3d55-8bf0-47df2836181a | -15.27616 | -56.85928 | 2025-09-21 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac66c376-575b-3421-9425-a3aa9bdd96ed | -15.99477 | -47.27103 | 2025-09-21 04:59:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ddc2c2d-0176-31dd-beb9-ce7a1c96343f | -15.77376 | -59.46667 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29413064-f4fe-351a-9253-42fd8ffca39b | -15.27674 | -56.85567 | 2025-09-21 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 103fe817-917a-35a8-8820-d5101398a1f4 | -15.41613 | -58.77885 | 2025-09-21 04:59:00 | NOAA-20 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a86b662a-007b-3949-b513-4f226bcd9133 | -15.46795 | -49.96991 | 2025-09-21 04:59:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45a66822-3359-3907-a0ce-32f4bffe49ba | -15.29128 | -59.41632 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea21391e-a260-35ac-a44d-1d93c1847d7b | -15.81869 | -59.50694 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8436b34d-c055-346b-962c-b4237a8a732b | -15.82153 | -59.51202 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0bddaa62-7984-3f26-b836-d902816bbb26 | -15.69081 | -46.99501 | 2025-09-21 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 373ad96f-585a-3d00-af42-1b92a3e4d1a2 | -15.81644 | -59.52019 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 2a8fa75d-b70a-38bd-826b-f6a6bd4d8da3 | -15.29419 | -59.42096 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29273821-f0eb-38dc-8d9e-0ad22692cf04 | -15.76815 | -59.45632 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abef36df-4c0b-31e3-aff3-41986a794265 | -15.76888 | -59.45209 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d9de794-cf4d-37ec-b458-14ac4bbd7b5b | -14.78887 | -51.36413 | 2025-09-21 04:59:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90ecb472-bfa4-36d4-b8f1-0c92f02cc23e | -15.82078 | -59.51647 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3ff87eb5-d871-3387-b15b-ff1bc724feb5 | -15.27501 | -56.86649 | 2025-09-21 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5705964b-164c-33aa-a8f2-2e04871fbe92 | -15.25019 | -50.22579 | 2025-09-21 04:59:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 439232cb-301f-3c69-9a0c-fb75e0f0e05b | -15.29278 | -59.42237 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05fdee7f-0df5-3fa6-a60a-8330dc8d21c6 | -15.99964 | -47.27494 | 2025-09-21 04:59:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6670ccdd-400a-3e3c-80cb-ccd9a8bb0540 | -14.36612 | -60.2963 | 2025-09-21 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 477f693c-c078-3382-8ad8-d100ef9937e3 | -15.26491 | -51.47331 | 2025-09-21 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40ee7152-a36b-3cd6-862e-041f1295d877 | -15.27342 | -56.85513 | 2025-09-21 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 82adeeba-0d99-3d29-9f45-43bcb181aec5 | -15.41963 | -58.77947 | 2025-09-21 04:59:00 | NOAA-20 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa5d269d-21c4-337d-9fb1-04b2c5f2b807 | -15.81507 | -59.50646 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e71a8d4-1df3-35ca-b85f-5612cb62901d | -15.90755 | -43.05485 | 2025-09-21 04:59:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7f01758f-8a85-33e6-9ffd-7566b53aef30 | -15.26422 | -51.47845 | 2025-09-21 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cae21121-15f3-337e-89f7-edcd3267d60c | -15.81285 | -59.51952 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 09e54d1c-5f03-30a4-a8a2-47ed880e4768 | -14.36995 | -60.29692 | 2025-09-21 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc857077-deb7-3fd5-9f4e-7cd176401783 | -15.29059 | -59.42028 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc35e66b-4815-36dc-81b7-51a44955afb6 | -15.69121 | -46.99148 | 2025-09-21 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15c3b84b-26d0-3d1d-a84a-70608b3df509 | -15.27559 | -56.86288 | 2025-09-21 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9c5497f5-1a74-3d07-be51-755423efd46b | -15.77607 | -59.4318 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2762167-c1e9-3a96-86b5-d5ae1fff7d61 | -15.27284 | -56.85874 | 2025-09-21 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ca4160a0-5a20-3db3-a521-4e14d1e8ea1d | -15.90597 | -43.05286 | 2025-09-21 04:59:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5f978fca-02dc-37c6-80dd-46738532e3b9 | -15.82438 | -59.51705 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e731886e-8311-3aba-90a5-e5635ce3d3e0 | -15.87414 | -47.30351 | 2025-09-21 04:59:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f131c80-b967-3db5-be69-e9ce2fafef52 | -15.79841 | -56.17896 | 2025-09-21 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 37e8904d-4a71-355f-a5f3-14a922653a15 | -15.77457 | -59.46193 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a55dc265-ee01-3eea-81ff-3d0e20071028 | -15.70142 | -46.99665 | 2025-09-21 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9426fa9a-1129-3758-9bf1-37cd89671abf | -15.2685 | -56.84322 | 2025-09-21 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 692aeb68-9f28-30c9-9580-fc82181112b2 | -15.81792 | -59.51147 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56317130-535a-37aa-8901-928cda0bcc77 | -15.70632 | -47.00097 | 2025-09-21 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d7bffa0-5dbe-33e1-9f73-cd908d463332 | -14.8176 | -51.38492 | 2025-09-21 04:59:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90531194-6fde-39a0-b4cb-a4bf03f11735 | -15.82514 | -59.51255 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0aa7bea4-e8f5-3523-9a75-1d5115daca4f | -15.82014 | -59.49835 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 869fc0c4-40a2-32a7-9ecc-c6aa1f801c80 | -15.90814 | -43.04873 | 2025-09-21 04:59:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d93b8c05-dde8-3c1a-9470-360a25c2cf0c | -23.1442 | -47.62632 | 2025-09-21 05:01:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9139361e-5f07-3a53-ba89-c33e834643f8 | -20.59878 | -56.73403 | 2025-09-21 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2142d7e4-6b1f-3920-8c2f-42014ab04602 | -28.28974 | -50.37431 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a1ee089d-e4fa-36c4-8697-208dc1ab3a32 | -23.21686 | -47.03079 | 2025-09-21 05:01:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85d79f2f-2f88-38b6-a49d-d482d3be2fe7 | -20.54162 | -56.14721 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2a6354d-a0fd-343e-a02e-86fa0283bb49 | -23.08771 | -45.55083 | 2025-09-21 05:01:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2e4ae424-f258-3ae7-914b-085ac595a534 | -22.47072 | -48.21358 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f87aff72-8c32-37f0-8ca8-7021d0c83397 | -23.14381 | -47.63042 | 2025-09-21 05:01:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bc1d2c1c-82c3-340d-8eca-617baee2a329 | -22.26664 | -56.01641 | 2025-09-21 05:01:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 360139be-24e7-32c3-819f-f8c8101dd8e7 | -23.14458 | -47.62229 | 2025-09-21 05:01:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b534a734-b11e-31db-8912-b46a1979b5e0 | -28.28749 | -50.34204 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 978089b3-1fbd-3c9a-befb-82884c644e21 | -26.17074 | -51.7298 | 2025-09-21 05:01:00 | NOAA-20 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 45bb0766-bdb6-3b73-acd8-1d5980453367 | -22.28055 | -54.16943 | 2025-09-21 05:01:00 | NOAA-20 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fc2a5fe3-6529-3857-8cb7-8cc4cea37145 | -20.54441 | -56.15159 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb52f2be-9ffd-3642-9626-4abdd431441d | -24.7556 | -48.81987 | 2025-09-21 05:01:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| eb272838-e708-3edc-9631-d5ebf92a879d | -28.28702 | -50.34751 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b962e818-dcd3-3810-9392-beb0ee3d9c36 | -21.31959 | -51.66487 | 2025-09-21 05:01:00 | NOAA-20 | NOVA GUATAPORANGA | SÃO PAULO | Brasil | 3533106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3125d3c6-6b30-3dc3-b5bd-344fb94bf7b5 | -26.17917 | -51.73581 | 2025-09-21 05:01:00 | NOAA-20 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bb824126-9325-38c3-be88-09a2a12f0955 | -20.53489 | -56.14607 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 977b01f1-bd84-36d9-bb84-24c9cc5db78d | -24.75063 | -48.8158 | 2025-09-21 05:01:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1d550918-051c-3762-b6d8-f76413736a98 | -20.6083 | -56.71658 | 2025-09-21 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ee52517-f33f-34bb-a009-c6befcac6fb7 | -22.77981 | -55.36874 | 2025-09-21 05:01:00 | NOAA-20 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0c57699f-0924-3a28-983e-834ff0ecf74c | -20.60268 | -56.73091 | 2025-09-21 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| febece73-64cc-37e9-9af0-9c90b413eb86 | -22.47539 | -48.22123 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69ce9b51-9077-335d-8969-5a1b4561d2b0 | -26.17572 | -51.7256 | 2025-09-21 05:01:00 | NOAA-20 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cab2e98c-43b3-3c1e-a7fe-9d7536162421 | -23.24284 | -50.85355 | 2025-09-21 05:01:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 561e8f15-3dd2-3a6e-9e7b-3fbe7b38007b | -22.47507 | -48.22465 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac1f33ee-0f01-357c-9491-1b0fe6d97a8f | -20.85716 | -55.16784 | 2025-09-21 05:01:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eefe3c72-1730-30ef-b82e-509e971007d2 | -23.50818 | -46.97744 | 2025-09-21 05:01:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 02d869d0-829b-398c-9e83-cb42dfa9f1fe | -25.05069 | -52.19622 | 2025-09-21 05:01:00 | NOAA-20 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4949d9fb-f511-35ba-a430-a9ece5cf88e8 | -28.28693 | -50.34846 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |


[Clique aqui para ver as próximas entradas](README42.md)
