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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db28d209-56c0-3a8c-863f-05db5c796f33 | -8.97274 | -52.7836 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e945ff8-00b6-3e81-abe0-dec872610083 | -8.96327 | -52.77837 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62c75aeb-4d98-34e1-a54f-1ccc126344b2 | -8.94777 | -52.77603 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1ee9f28-f90a-3bf0-9665-aab85b5b3353 | -8.94099 | -52.79698 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e30c0a8-af6f-3c0d-98c2-749b1e7a7fc2 | -8.93764 | -52.79643 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4a6fc87-9ea6-3aac-bd9e-4d1611b69af6 | -8.93372 | -52.79946 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e72d5d3c-3764-3e6b-b121-718070e2014d | -8.9298 | -52.80249 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22aa1ab0-c3be-3547-9255-6cad615dd3bc | -8.92644 | -52.80196 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8194904-cd11-303c-bfbc-fdb77f34905a | -8.92383 | -52.75384 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ba65ef1-4485-314c-85e8-86c477bac045 | -8.9208 | -52.81575 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0623ef96-b800-3989-ab79-8538173e46a0 | -8.9047 | -52.78743 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f89cfa6c-cfe1-3bcb-a4a3-ca7bfc0c870d | -8.89915 | -52.77918 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79beacee-548d-3e18-8887-df9dc0ce53aa | -8.87985 | -53.04963 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2a55fa3-aecc-3b4f-83fe-443ac5241a1c | -8.87926 | -53.05326 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5fed424-1e48-3f41-906a-6c680238f6a5 | -8.87648 | -53.04904 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 669ee3fe-a140-30ab-99f2-5955409f2dd9 | -8.87512 | -52.99297 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 598f4191-55f3-3bd7-9157-77dd77a421d4 | -8.86781 | -52.99541 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff58a1d9-4f70-32d9-9d5e-09b5db523182 | -8.86767 | -53.01775 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bebd46a-f6c6-3ebb-a4ab-0e5b17a6c227 | -8.86503 | -52.99123 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a4d068c-bb74-37a3-9d55-efba1cb66edf | -8.8646 | -53.05828 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 385480f4-cc1f-34d7-ab79-56b719b43446 | -8.8643 | -53.01718 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1654a950-335c-3f74-88da-115d17b9ec6e | -8.86137 | -53.0354 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1270cf3f-9b59-3b0b-9eea-7de7e2cb42e6 | -8.86051 | -52.99781 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88fbfb09-0593-32b1-85f4-cd9df78cb02e | -8.85654 | -53.00097 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08941614-8a25-34d8-8677-894b1b215363 | -8.85596 | -53.00463 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17037c05-b498-3219-8ffe-1d6b0069175c | -8.65665 | -53.08515 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd0ded41-6718-3c86-a2f3-a36e173fa3f8 | -8.56204 | -51.80105 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ebb4a42-4e4a-3f0a-a856-8e3e73c39625 | -8.54772 | -51.80586 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d314964-d2e7-3e2a-aedf-d57a4a08d690 | -8.54386 | -51.8088 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebd600ca-6e57-31b9-880c-90ee92f6eaaa | -8.25787 | -51.79199 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1fca253-eb8a-3022-860c-29b3fc3eebda | -8.07053 | -51.64445 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c153ff7-484e-3f3c-9782-3937602decd8 | -8.0671 | -52.80064 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62364407-2e7b-3f1a-90f0-65cde122dc5a | -9.18393 | -52.03659 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87d2142c-3598-3abc-978a-acebcf0b02a2 | -9.03826 | -52.09911 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f34f9d7-9fba-3cd2-81c7-d87e12c6677f | -9.03605 | -52.11308 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 660dfb7f-ee97-3286-b7bb-4972a46f815c | -9.03164 | -52.09802 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e068d8ae-5276-3f69-83b0-52d8fe09439e | -8.94259 | -52.12344 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 773d88a5-644d-3d6c-aaac-5793f3f14480 | -9.35671 | -52.5107 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d01ac7b-910e-3778-bb31-59fff79cb367 | -9.3366 | -52.55096 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05af6da0-ae14-392c-b9d3-e03c37dbad40 | -9.06335 | -52.96056 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9658c701-0d03-37ba-ade4-937a53998622 | -9.03936 | -52.11362 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ef473ed-ed6f-33ee-80db-6cb9774c89dd | -9.03908 | -52.98255 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2d6b777-91dd-33c8-857c-d814649d605c | -9.03881 | -52.09562 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69be801c-a0e5-3718-b3c0-1c92a682a6d7 | -9.02833 | -52.09748 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c90bf6b-e477-3457-a4a9-12b96c324e7f | -9.02777 | -52.10097 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6464457-91df-3bfe-b50d-6e4a535aae97 | -9.02501 | -52.09697 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a24038ea-2c21-3df2-96d2-26302d463b5e | -8.98777 | -52.79698 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ba724b7-4e21-3ee4-8bfa-c0b69a8dd4d0 | -8.98556 | -52.78933 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 710b78cc-e863-3e14-a517-61135dc45cc3 | -8.96939 | -52.78305 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8df3c537-5d45-3241-b25d-90b837eedd3c | -8.96604 | -52.78249 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3499914c-4708-3733-96e9-623663c021f8 | -8.96117 | -52.77823 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51725c41-1370-38f9-ae5c-92dcf1eec0fb | -8.95782 | -52.77769 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a826cfa-9dcb-33f6-a314-8556318b2522 | -8.95447 | -52.77714 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f46d5070-630a-31bd-a421-14593df4bc61 | -8.95055 | -52.78016 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbcd6c6f-0e01-3bbf-a714-578228a7e7ba | -8.94314 | -52.11995 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c796114-9f31-345f-9599-071ca3ad3db6 | -8.94204 | -52.12695 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa93c296-18a3-3ac5-a09a-92587c0b9392 | -8.92587 | -52.80554 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07bfa7b4-ae9f-3f23-afe8-9ee5100f73cc | -8.9253 | -52.80913 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 673ba3f9-50c0-3703-8464-a7dccf586c84 | -8.92472 | -52.81271 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 039bc834-5705-32d2-9f1a-f56f3ee08188 | -8.91753 | -52.79317 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9845ffc1-5572-31eb-ba01-c0afaa9bfc43 | -8.91418 | -52.79263 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13614c61-2fff-3804-ad8b-eef9a0ae348a | -8.91083 | -52.79209 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7adc808a-7907-37c3-83ea-844a026e3124 | -8.8958 | -52.77865 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0bf83af-b6aa-37a1-a834-b27624e4b3cd | -8.87906 | -52.98993 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02c40638-ec68-39b2-8688-d99dcaf92ee4 | -8.87589 | -53.05267 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2470a486-b9bb-3093-a8fe-a6eec0741350 | -8.86857 | -53.05518 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 456cf7db-d602-3739-aa54-505ac885d2dc | -8.86839 | -52.99183 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c3ed6e8-c07b-3083-906d-5e742bdc100f | -8.86708 | -53.0214 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c080b0c-037a-3f87-9977-504640808b1c | -8.86519 | -53.05462 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56c996da-679c-3fcd-ae5d-a87479e482ab | -8.86299 | -53.04681 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd559d2a-126a-31e2-be28-19df63bcda4e | -8.86254 | -53.02812 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dad4d609-5407-36a3-93c4-de2fa07fb811 | -8.86166 | -52.99067 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88b88768-caff-3d83-b0f7-3bea8497af0b | -8.86109 | -52.9942 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 434a13aa-5362-36a6-869c-25d096244550 | -8.8602 | -53.04267 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a9cf713-5692-352e-b7d0-6e73377c85bf | -8.85772 | -52.99369 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8eeaf5c6-289d-3b8e-923a-06159b7c0e8f | -8.85714 | -52.99731 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d4b183b-62dc-3ad1-828c-d3d08e98035e | -8.66019 | -53.06315 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2f44379-7b0a-34c2-be96-f3c1ffe42716 | -9.78283 | -53.1769 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb269632-80cf-3e43-ada8-cff274158e4a | -9.78224 | -53.18052 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 814c14d1-2f4f-319a-b985-1ce86a41a25c | -9.78123 | -53.1655 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4580f995-743a-3347-8141-6c5eadfb7e00 | -9.78064 | -53.16912 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fb218de-dd46-3c5b-a11c-a85513797935 | -9.78005 | -53.17273 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5a2e756-35b8-3d35-a415-b5394cb39dd5 | -9.77946 | -53.17635 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 729ed5fb-1df9-3922-9226-cf39437416c3 | -9.77786 | -53.16495 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74054f24-3000-3596-8da3-2096b9bfd687 | -9.77231 | -53.1566 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c03c15b-c4c1-3d45-a06b-ab832cdfd0f3 | -9.77069 | -53.15664 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 470632a1-a0e0-3940-b159-b3bebaa814ae | -9.7606 | -53.15499 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcc2ab18-d298-35e4-8b63-dd8d78994c69 | -9.75445 | -53.15027 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f57d6c6e-875b-3e5f-9df2-de590d0bf155 | -9.75108 | -53.14972 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2a1ad66-e8ac-375e-bcf6-418634927c09 | -9.74876 | -53.1642 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 963c4bb2-cdaf-39d2-a0e9-07b9d4cd5c20 | -9.74655 | -53.15642 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df2dab14-73b9-301d-8916-3180eb493256 | -9.74539 | -53.16365 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21f4c795-ce3d-3570-a7fb-6eedb57127a8 | -9.734 | -53.19154 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6ce304d-7290-3290-8bb7-dacdcbcab07d | -9.73063 | -53.19099 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9b9f2c9-ce2b-349c-a265-368abe969a9c | -9.72448 | -53.18626 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 205d48e1-e77b-3a8f-872d-f3fd5d2fc38b | -9.71701 | -52.82706 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce7ba3c1-cb2c-3489-8739-276fcff920d7 | -9.71643 | -52.83062 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e2fdc24-9506-3b5c-98c1-9b0cb3f9695a | -9.71529 | -52.83773 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ccfcbc1c-aaf9-35fc-9fbf-54ba8c9d5ec2 | -9.71395 | -52.83001 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d89d0ab7-8660-3443-8bca-cc347bba5b76 | -9.71338 | -52.83358 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README109.md)
