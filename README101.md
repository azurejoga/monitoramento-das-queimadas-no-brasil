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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fb53c0a-0ef6-3a13-85e8-34c55b3e55e0 | -15.59938 | -52.57545 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 65ea5190-f0f0-3d83-9683-e6e4eef888b5 | -15.562 | -52.44752 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f14ce47-4b84-3817-90e4-99cb2c227556 | -15.22138 | -56.77908 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be2ec8f7-e571-313c-8a16-633741683605 | -16.04156 | -50.99294 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c42d0c60-c00a-37e0-a3c1-c10b42a01e7f | -15.22311 | -56.7683 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f055c010-0b1a-3bdf-9a2b-42d61c0d43c6 | -16.01675 | -51.05602 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d074a8fb-412f-3fe4-81c2-d2272c76e1dc | -20.08309 | -49.59555 | 2025-10-07 04:59:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 22cbef02-d5f9-391b-894f-6679a6e3fcff | -20.39569 | -46.89663 | 2025-10-07 04:59:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 219a03b6-068a-33b7-8f8f-91b129960264 | -22.54326 | -44.45991 | 2025-10-07 04:59:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 8ba8d533-1831-3169-8cf7-b24128d96a98 | -15.20113 | -56.82005 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc5d387c-1772-3c32-ba44-9ddaad5d6c58 | -18.51751 | -43.91618 | 2025-10-07 04:59:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f08b8a2c-aab9-3515-ac09-31e6a866a496 | -21.90084 | -44.88139 | 2025-10-07 04:59:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2afb43b6-4874-36b6-a459-dec36b0151ba | -15.18495 | -56.83572 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b108ef6-c122-3531-b23e-fe89920f6d25 | -20.58776 | -46.31021 | 2025-10-07 04:59:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee44e2da-0e27-3ee1-9ff2-2bcc4e0746d9 | -20.11878 | -44.4113 | 2025-10-07 04:59:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 91c29327-2ffe-3f0c-9254-c9adef4bc450 | -15.21921 | -56.77132 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f19f5a27-fe3b-318d-8b7c-59a7b2d3b6a2 | -15.03482 | -56.02968 | 2025-10-07 04:59:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f69b5e38-2cff-3f99-a1ed-11ac67116814 | -15.22296 | -56.79045 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da46197e-9b6c-35b6-a2ba-087356dd760d | -17.25049 | -46.93017 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6fcecb8a-39d5-37dc-8293-44cd43a9a032 | -15.20504 | -56.81702 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a871278-734b-37f8-a306-55cccf222a2d | -18.77575 | -44.62112 | 2025-10-07 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 404fc229-170d-394e-9770-1f0a0df469b3 | -17.96086 | -44.41112 | 2025-10-07 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0c10a3d-e4a7-3c3c-8924-432cd7582c5f | -16.34564 | -48.13023 | 2025-10-07 04:59:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ad5b6e4-60e2-3506-ac89-7a7d464b3fca | -15.99763 | -50.94918 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14beaa54-03bf-398a-8928-162353a2dbdc | -22.0246 | -49.71838 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 3b8913ab-bfa5-388c-8d22-57e234a11219 | -15.03813 | -56.03023 | 2025-10-07 04:59:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5efb4a4-4e73-3a24-ace5-68edbeaea33d | -21.08344 | -46.90733 | 2025-10-07 04:59:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e359ba8d-9016-36c5-85a2-162b3661e47c | -16.33921 | -47.05997 | 2025-10-07 04:59:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51eadb8f-70f7-3dac-a8ff-9931d321a2a3 | -15.01377 | -56.0554 | 2025-10-07 04:59:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 218497dd-a85b-3ed1-be71-169121440887 | -16.01955 | -50.97119 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58c93275-b3ae-3de4-a879-23abe60ea579 | -16.01363 | -51.04836 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a5cd4e6b-5955-3d4c-96d5-233485c1379f | -15.21863 | -56.77492 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a0f373a-e495-3bf0-a7e7-39f6f05c4e3e | -16.05838 | -50.99099 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d46bef7b-5649-3cd0-8406-d6ee5de66843 | -16.06201 | -50.99484 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b27a7bc-227e-377b-bcec-0007b95ab114 | -20.05348 | -49.54694 | 2025-10-07 04:59:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 029c1acc-4b02-3eab-a001-71cfa410ea68 | -16.39939 | -53.32151 | 2025-10-07 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a926b612-8747-3f1a-9c1b-3ba694afebfc | -22.01503 | -49.71704 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 42c15a89-6e4c-3fd2-a275-13ef5b840a74 | -15.21979 | -56.76773 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b5735e1-13d0-31a3-87b0-35fb4581c7a7 | -20.1189 | -44.4147 | 2025-10-07 04:59:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9b2351ef-af6d-334f-938d-6e6de1298345 | -15.59327 | -52.56535 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 557f3bc4-ec2b-384f-abf9-968653f657ad | -16.28338 | -50.98083 | 2025-10-07 04:59:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4ac4aaf8-e7d1-39c0-935a-f43ff4db8c38 | -15.60367 | -52.57168 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3c8f3a41-9d5e-3fe7-89cd-c12cfa194ba7 | -21.18652 | -45.61527 | 2025-10-07 04:59:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 20a55451-1720-39b8-8e23-b69a65e09406 | -16.0104 | -50.82376 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e14beb36-7235-3e53-bc08-cdbd5f32ade4 | -21.07853 | -46.89848 | 2025-10-07 04:59:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 40a39c97-b156-3c56-8d00-cf0f48130130 | -16.10573 | -48.94098 | 2025-10-07 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1803fcfd-c8bd-35c3-a1a5-d74613e36983 | -18.51336 | -43.90827 | 2025-10-07 04:59:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33f9e01c-71c5-3387-a111-7030c08e860c | -15.58834 | -52.54672 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c13e858-ab7a-3e44-aa6a-b69a75312f22 | -16.10977 | -48.94664 | 2025-10-07 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ac4f8983-2822-3c0c-92d4-03a8fae917dc | -15.03095 | -56.03269 | 2025-10-07 04:59:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36b6658e-a7fe-348a-929e-56ef740c83d7 | -15.99836 | -59.52901 | 2025-10-07 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ed5687f-12db-35d5-a2ea-e7258704788e | -17.25014 | -46.93348 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 940c0480-2ee4-31da-a778-1ff0ee5df893 | -20.11236 | -44.40926 | 2025-10-07 04:59:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 45650d47-f6b1-3825-876b-0c83f2ea0f06 | -17.97982 | -44.99354 | 2025-10-07 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6740ad0a-49be-3d47-9ef6-ca93dd03be7e | -20.0595 | -49.54994 | 2025-10-07 04:59:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 5f752b97-ac1c-3d5e-a763-4fdcdb722093 | -16.01547 | -50.97071 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80507b01-0871-3d85-9efa-12b4c3fd902b | -21.19271 | -45.61539 | 2025-10-07 04:59:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 351cebf3-9815-3fc0-ae9b-2292ab8c1c9b | -15.03207 | -56.02557 | 2025-10-07 04:59:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a8da9d4-d6f2-3cfa-85e7-3c04b9d7ce5d | -15.65394 | -56.0225 | 2025-10-07 04:59:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e0330794-03c7-3fd2-829e-81c5fb58e7a6 | -15.97047 | -50.84105 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 19071a6c-26b3-337f-8d5e-c8d4c5eb58d7 | -22.55033 | -44.45537 | 2025-10-07 04:59:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 16977510-2f28-363c-9995-affcb2f6dc45 | -15.58958 | -52.56485 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00861020-8df9-31b4-bd6a-24c206b4d243 | -15.19059 | -56.82188 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccc189b1-f3bc-3dc4-a00b-56af012bc923 | -16.39221 | -53.32063 | 2025-10-07 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86c823f7-af0a-31cc-81ba-4c50bfabfa12 | -17.71633 | -56.76992 | 2025-10-07 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 455aa7c3-0d7b-34b9-874d-211e2b632f82 | -17.17259 | -43.46009 | 2025-10-07 04:59:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0b537c1-02d5-3134-97fd-9b7c1bb0db07 | -16.29153 | -50.98202 | 2025-10-07 04:59:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ab6e0ac-a822-3b63-8946-9d49f4bef099 | -15.55831 | -52.44687 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6216b46-150d-37a3-a790-35eca4fb78dc | -20.9418 | -46.71801 | 2025-10-07 04:59:00 | NOAA-20 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0d88a96a-eada-3508-aff1-f45f635db793 | -15.9623 | -50.83961 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25559e2a-44b2-3ba0-ab09-7e74ce9f4820 | -19.6427 | -55.74413 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 459387a8-db6f-3c3a-816b-0f6c00772788 | -20.05412 | -49.54155 | 2025-10-07 04:59:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0def6d14-9dfe-386d-9315-cb967956205d | -21.07599 | -46.90065 | 2025-10-07 04:59:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4ad1acf-d7f8-3622-a632-8d7e759b3cdf | -15.58406 | -52.55047 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b5bcc70c-84c2-32e0-a25c-e2fb0c614d4d | -21.49135 | -46.02454 | 2025-10-07 04:59:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 30df48d4-c157-3206-b21e-5a639e76b3bc | -16.04501 | -50.96674 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c32bacba-b390-394e-aaef-d8deb7afc4f3 | -15.99602 | -50.83744 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06a82b81-b7c0-3a34-9570-56acef268882 | -21.90687 | -44.88753 | 2025-10-07 04:59:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 80512046-9bbc-35be-b70e-0ae99a1bab1f | -15.03426 | -56.03324 | 2025-10-07 04:59:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bc52661-9afc-384d-bf92-8cee977dce84 | -15.1867 | -56.82486 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40935fdc-d89b-3c5d-b4bc-95634f6a60d6 | -21.51541 | -45.60511 | 2025-10-07 04:59:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 86250c7d-cf70-360f-bcb7-2629cf26fdcf | -16.11502 | -48.94244 | 2025-10-07 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b60004d6-003a-3ce3-89e2-2c114283cc73 | -19.63316 | -55.73866 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e9fd9d49-bfb4-32d0-b98c-ccc6e409b586 | -20.05597 | -49.53855 | 2025-10-07 04:59:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 628411cc-a673-32a8-8c90-0b92518a4394 | -15.55525 | -52.44176 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3991713-2b7e-3b8d-ae38-65490bec7861 | -18.97281 | -47.82572 | 2025-10-07 04:59:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e6f2f996-d5d2-3f47-952a-58027fb1ece3 | -17.61145 | -46.6863 | 2025-10-07 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c42c5791-6c19-3535-9f1c-b38b95c39309 | -19.38165 | -47.42753 | 2025-10-07 04:59:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b67f929-d591-3a33-92d5-60298cb4554d | -21.07809 | -46.90324 | 2025-10-07 04:59:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4dbd489d-e527-3a97-bb95-014e2de46346 | -15.6573 | -51.33045 | 2025-10-07 04:59:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c9b5876-76da-34dc-ac9a-0d99e18d6a55 | -15.98893 | -59.54074 | 2025-10-07 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1b4bf1b-e557-3fcc-98c4-f322dfe4e07c | -20.20559 | -43.91815 | 2025-10-07 04:59:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f87f66ec-3e60-35c0-9da6-d94fc92d2b69 | -22.00842 | -49.73312 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ed791a45-19d1-32d3-a27b-f669ec41f3bf | -18.01354 | -44.96707 | 2025-10-07 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d545906-a064-3330-ab8d-424e74bc324d | -17.35061 | -46.83233 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6fca1f3-1e47-3856-aefd-5db93f0908fd | -16.11037 | -48.94173 | 2025-10-07 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9ea88fa3-76c9-3f7b-89f8-720bda029680 | -17.34855 | -46.8383 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 476a70f1-b715-301f-8e5c-be5398412d3f | -18.9721 | -47.83247 | 2025-10-07 04:59:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 41400722-64e9-3ae7-bffb-d73a23da49eb | -21.67219 | -51.15471 | 2025-10-07 04:59:00 | NOAA-20 | ADAMANTINA | SÃO PAULO | Brasil | 3500105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f7e2a721-76fa-3566-a653-b5d7ada629f9 | -18.28821 | -45.45763 | 2025-10-07 04:59:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README102.md)
