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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03b8f0b1-108f-34f9-8657-5fb71ddb0dc8 | -4.2856 | -50.75761 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7333252e-ee11-3f42-b87c-b8a954b5f13e | -6.11518 | -55.70207 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 79e12c77-23ba-3af5-924c-9692733b6bd4 | -7.84152 | -55.13869 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 179e5707-1abc-3ac6-90bc-26da09ddc762 | -6.00512 | -53.54037 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| efc1b669-1110-3a05-b263-8988a590cba9 | -4.28199 | -50.75707 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 314b496c-1ee6-3512-b568-bf6d2df9bb33 | -7.55199 | -55.03193 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de8fd0fe-816a-3066-9971-a13eb7127123 | -7.53081 | -55.61836 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d27cc29d-1354-3e5d-a541-fd2e8e43ae65 | -6.87224 | -55.56384 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5bc2020-3f69-3a7f-872d-da7af0781e21 | -7.46 | -54.98842 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f94b3f55-4fee-3f9c-abd4-bd043e6e946c | -8.08978 | -54.87971 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 029dce25-fb82-3974-927b-aaac5d466464 | -3.59774 | -54.55426 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21a834f5-2a21-3498-b912-7d97b9297e1d | -7.63399 | -55.07333 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06dcfa8c-f4cf-3d65-97fa-0c80ef0564d2 | -4.29763 | -49.09295 | 2026-10-02 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3678838b-2625-3658-a303-cf610aeac7aa | -5.89694 | -53.49157 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c06b48aa-8c60-3b14-bd0c-3ec849b962bf | -1.26167 | -54.56296 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ae248cb-fcda-3d2b-abcc-6c56b825db2d | -6.03404 | -53.87864 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bd72dc3-5b28-3160-a01d-fa31df9f659c | -3.74859 | -47.15067 | 2026-10-02 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15993bf0-494e-3f97-b25d-801e5a711b9b | -1.46556 | -48.90742 | 2026-10-02 04:57:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ad56248-d293-333c-ba87-54a997dcc946 | -7.40659 | -55.58721 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6eca24db-cbee-3582-b1c3-442ef8499569 | -3.45643 | -50.61636 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e22b576e-39b7-3a50-8a21-96b1b8f83ccc | -4.26099 | -50.74964 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5fa5e648-03c8-3b8e-a7fe-cf8421b86778 | -2.85811 | -54.12984 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 885a7e3e-6f7b-3560-b76d-65b73899534d | -2.05454 | -56.86287 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8da6bcd4-7f56-3ec9-a9dc-6167c4537094 | -7.46335 | -55.01022 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4fda97b-eb85-34d1-8110-5b1ddcdff458 | -3.12108 | -50.28436 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 755992c7-e5b6-36ca-8a35-e7cf9d884d51 | -7.49573 | -54.97631 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4ecbd37-5d56-36aa-8bcf-caea8da88fb9 | -6.24451 | -53.13496 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9313b4e-6c5b-338a-81d5-d0f32f250059 | -7.52456 | -47.33595 | 2026-10-02 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f2a4b2a-1bd8-30d5-8718-9b134fe39b50 | -5.7608 | -45.13181 | 2026-10-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6078ce58-f7da-3dcb-8e88-fa08bb629cf5 | -6.15116 | -53.31982 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12fa5371-7f41-3009-92bb-5a695251e2c4 | -6.00405 | -53.54733 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24f9d53f-79fc-38a2-898e-f9f222abfb70 | -6.15134 | -52.74231 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fa995e5-b96c-318f-b4ca-7bcaec4af760 | -2.46033 | -56.0842 | 2026-10-02 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3578e5a-981b-3337-b2db-771a78e5560c | -2.91208 | -54.1311 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5c6521a-6997-3afe-a00f-720d4c817ada | -4.25864 | -50.74073 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 324047e3-827c-328d-b236-f73ecaaddffd | -6.68425 | -52.9711 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb483c4c-28ba-3288-8514-33f5eca8f9b3 | -5.86676 | -50.16136 | 2026-10-02 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f5245218-769f-35b1-bc0a-45b8d609cdc2 | -4.86383 | -56.03487 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a01b56c0-c7c9-36ee-97ab-d8031de3097d | -5.86698 | -53.48713 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 114b236e-808b-36e6-966b-359ce1f173cb | -7.27321 | -55.59143 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb90889a-fc7a-39c1-a5c5-f97ece2e111f | -6.2501 | -53.1431 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1997e6db-5422-3312-bdf3-91ed3b1af3a9 | -4.25503 | -50.74019 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb5fc59d-f4b6-36f9-9795-e77a82b6cc59 | -3.0219 | -54.23293 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ce782b2-e113-3f05-85f3-1246954d4f34 | -6.19675 | -53.17836 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a460e49c-8894-3c64-8c4d-4c13ecffe9d3 | -6.1854 | -52.90255 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e330d68d-9ae8-34da-8cb0-72ba96df7826 | -8.18302 | -54.8022 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4375e2e-2a15-33f3-9117-1cea9c74addd | -9.5237 | -45.32895 | 2026-10-02 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 090497d7-2313-3993-9396-4eda6f7e1c07 | -2.60985 | -48.25497 | 2026-10-02 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4519eb5d-cff0-3db6-9753-4ad159644bdc | -2.93759 | -54.18448 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e56fc3a6-c1ec-3ccf-af9f-36cd5bfc3a03 | -7.63068 | -55.07281 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aab0a17-f2b0-35c1-be33-916716ddebae | -3.21119 | -54.97871 | 2026-10-02 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd104ca1-48cf-31bf-b811-ccf27c34dabc | -3.1783 | -54.10247 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c578101-53ce-37fa-ba90-590f3fa74d5b | -4.28605 | -50.77897 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1784ebe-3b2a-371c-a622-800f26d0a66b | -7.45615 | -54.99136 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62c14e0b-2ae4-3aee-913d-c6d21f40f30d | -7.71865 | -54.81369 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3cce9fd-cfd1-39c3-b0b9-2cc2d6c88f53 | -4.27181 | -50.75124 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b76f739c-a4a8-3139-991f-58b4d2e591bd | -3.14009 | -53.74157 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cf5055df-10dd-33ca-856b-406e33332639 | -1.65682 | -55.21544 | 2026-10-02 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42938d0c-cef2-3a10-b709-03646a5dc93d | -6.33005 | -43.36206 | 2026-10-02 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a881ad94-efcb-3dbd-a23d-c8f455fa750e | -4.26037 | -50.75381 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aa32622e-49ff-3346-8c35-4b5e8737393c | -4.27289 | -50.76856 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b9be7a7-e1f3-372e-828e-fb901af3b44b | -8.07881 | -54.88507 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da15e000-f7f6-3836-a879-cb127d2b272b | -3.12174 | -50.28012 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a24562b1-1594-3f0f-b548-6819c623a5f9 | -3.61786 | -51.80306 | 2026-10-02 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d953464e-78b8-39c0-b4bc-7dbbca8c603b | -6.41121 | -56.39875 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e06dae63-c7e6-3b4f-bc25-f856680ed1ff | -2.27053 | -48.74793 | 2026-10-02 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a5491b5-ddb6-3467-82ef-8c2a0445c8d7 | -7.73059 | -54.75889 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41b145b0-9b2b-3102-af34-2bbec1ccb96d | -2.89893 | -54.15025 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b6214317-f1fc-32e5-a35d-52fc9f772479 | -6.85214 | -55.54268 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d83c71b-b47e-3916-8fad-99492931c01d | -3.42936 | -56.94563 | 2026-10-02 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fae70b72-fb5d-3163-b9db-4469e3b28455 | -2.05022 | -56.86653 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 0fa5d878-3221-3cc6-a3f8-69ecdbe5c2cc | -2.92314 | -54.14692 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecf03b76-f705-3783-8d21-6547a4c521c9 | -3.01743 | -53.89407 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a50f2ef-26df-3e04-aaac-e6a31ef330bd | -8.24075 | -54.78362 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13b345f7-448a-367a-8bc7-2c5fd2f05cf8 | -8.16717 | -54.83873 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16354538-ed7e-3de2-8807-4e02dff50bdb | -7.88354 | -54.74105 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 658e9d22-c773-3729-9f70-1b57da9927a4 | -4.24721 | -50.74319 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68ebdae8-64ea-3d65-a408-0e74153aff06 | -3.17607 | -54.09507 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 90d7c43c-f017-333a-abc4-7a495207ea43 | -7.88493 | -44.18179 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cd1e0359-6a02-3df0-8f3b-14ef77892a5d | -7.04183 | -55.63408 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb123597-cf38-3c8e-8553-c74096468228 | -5.90251 | -53.49955 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52d27cd4-7cad-30c6-be7f-dbd5965e38c6 | -6.2484 | -53.13192 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c50adc1-db00-3d0b-80c8-bcfef9e3d863 | -4.27056 | -50.7596 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1beeced0-89b4-3d08-b850-28193ba043d5 | -3.27076 | -50.08802 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc009c3b-0a73-3546-afd9-94475961eebe | -7.56701 | -55.13026 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d2fd05e-ada5-3766-81b8-3a61437aecaf | -6.43415 | -55.62142 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e81ef967-be43-3d13-a2b5-90077dfc8c00 | -2.93145 | -54.15879 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 905d9fd2-0faf-3d35-adbf-122440dc17b6 | -7.89008 | -54.72081 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b813f84c-a680-3a6d-a89e-f6cd574061c5 | -7.55195 | -55.01064 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24960f9a-f7cb-37c0-b3ab-eb0072da4ead | -7.45561 | -54.99483 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f1c4774-c53e-3682-bb4f-c282c19a4070 | -6.3415 | -43.36828 | 2026-10-02 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b52d9bed-6744-3e33-b468-455384d0afc4 | -6.75406 | -55.08572 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 790cd329-a68d-32e0-9410-2a998cd034a2 | -6.67304 | -52.97675 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d814cc91-36d1-3b8e-a9fc-4ebaaf6086d7 | -7.84206 | -55.13522 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41bc92cc-7fbe-3e69-b49c-2b937d2bbf9a | -3.29845 | -50.32581 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7c4d0c7-5db6-320b-b597-14a35b9bfa45 | -7.51293 | -55.04357 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc240f18-2e6e-3728-b17a-248161178487 | -7.19537 | -52.60956 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a5414a9f-0bcb-37a6-af04-d41af13065a3 | -3.5972 | -54.55774 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 077d03e0-e8a0-3c9b-88c5-cd36742b0fec | -4.04338 | -54.23183 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19c65e7f-5966-3910-b95b-f2bd480fc2f8 | -3.17938 | -54.09558 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README57.md)
