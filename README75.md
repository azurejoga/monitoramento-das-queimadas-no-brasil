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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 619985c3-dc97-39ed-b25f-aa0bfb4e79c7 | -1.63715 | -55.12722 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c086f3ab-671e-3423-a0a2-ee8b4db5f7e4 | -2.05287 | -56.8653 | 2026-10-02 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 6ffe4ae5-929a-36d6-b814-3ee54ae8c061 | -3.16987 | -54.08067 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f20629e0-adf1-354a-9725-a337e00a01b0 | -5.13934 | -49.87184 | 2026-10-02 05:33:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf12b1a6-e1cb-31b5-b1f4-81802d86fbcf | -3.1444 | -53.74351 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b35d2af-7777-30c3-ab6b-e648468b95c9 | -1.26243 | -54.55608 | 2026-10-02 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f1147bba-8bd2-3199-9b42-5dc876ed6afd | -3.16329 | -54.09561 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5ae548a-09d7-367e-830e-d34c109836d7 | -4.45328 | -54.9073 | 2026-10-02 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22da26e3-37f4-3d45-a7ed-ba67449afff0 | -2.93022 | -54.15662 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abb7afc3-a465-31a8-8285-b85270c5cfcc | -3.01833 | -53.89089 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1b48781-461c-34c7-bed1-365e075f7e46 | -4.28169 | -50.78476 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7411cab4-6ab3-3826-8ef9-ecede9f587aa | -3.2875 | -53.85551 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ca0b4a3-e6dd-325f-ad0f-c6124f0aebb3 | -4.28041 | -50.75654 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1449541-57dc-3e30-8a8b-c3314798bea8 | -2.89888 | -54.13737 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4f7ca43-3bb3-315e-a66b-3963a7d13136 | -4.2783 | -50.77055 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35292bb7-14a5-39c4-b930-c0b04d55357e | -4.30128 | -50.77321 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb23c176-1177-3108-bbc0-8148d9214787 | -2.21771 | -53.69878 | 2026-10-02 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ec89ecc-a861-33ea-84e1-4b0937ebc050 | -1.69589 | -55.10688 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac985ad4-7839-368c-ba2a-01615de817ed | -1.61246 | -55.13316 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1a87148-dc06-3114-8dd5-3ce3fb6759e3 | -3.1566 | -54.08253 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adf75e4d-d38b-3fe2-bf9f-9a7a45c12618 | -3.86461 | -55.81944 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 371707d7-b805-3e64-b0e4-89a7cab7f3b5 | -4.2777 | -50.78357 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e261bf7-1c92-3b43-ae5d-42d1262dd698 | -3.17656 | -54.09367 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7411a606-1417-31f5-a13a-f47d285c1dfe | -4.05973 | -51.11609 | 2026-10-02 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4cc9c46-db56-3e2e-9a70-a5505c0eb1b6 | -5.12374 | -56.02265 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcff8ecd-eae3-34c3-9ba8-ea61a8392583 | -3.17174 | -54.09697 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8120fae8-5f85-31a6-9e82-dd6589fa3250 | -3.69046 | -55.48854 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 698cf7b6-9e39-3a17-b40a-4b8b66fb6806 | -4.29439 | -50.78264 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 803e07ac-e382-3ded-a918-df29d4824de1 | -3.01467 | -53.88625 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee7f93bb-57e8-3c9c-bc04-8a864379f7e0 | -3.28509 | -53.84273 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 5ed06415-74ab-3c71-a32d-a21c6a8c158f | -2.99167 | -51.04347 | 2026-10-02 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0da002d-3154-3608-bcf0-d36f607e5cab | -2.90244 | -54.08688 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26e18fd8-5e25-3296-9835-0d0cd67583f5 | -4.05922 | -51.11959 | 2026-10-02 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a9e88b9-1283-3e72-b75e-bc8c7742ce32 | -4.28358 | -50.78106 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efa606c8-92a1-3d3c-8284-12e17e9b52ec | -4.14477 | -53.94606 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2662b999-9ff3-3f65-a5d3-9c3ef8a7d6a3 | -1.63105 | -55.14091 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a85c4c8-2dad-36a1-b693-9ffdfb7b0444 | -3.69145 | -55.48564 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 984922fc-5902-3145-8403-7089335534a4 | -4.60626 | -50.91703 | 2026-10-02 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2169befb-6483-3506-89cd-9902e8dfd8eb | -3.22156 | -54.31139 | 2026-10-02 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df7324d8-e7b7-3eb5-9f11-75417ef064d1 | -2.89829 | -54.14119 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 08ff66dd-1f41-3fbd-ac38-751a6e08ac6a | -2.89469 | -54.13673 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8608c652-f274-32d2-913b-8216784eae58 | -4.26364 | -50.75773 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c74f8084-4a5d-36e6-9977-62d5b31e258d | -2.4638 | -56.07868 | 2026-10-02 05:33:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a3d4d4b-0bec-380e-a509-d70f4521b1c7 | -4.29488 | -50.77925 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 658d936f-c3ea-3389-b587-74b21e2b435c | -1.34028 | -54.69539 | 2026-10-02 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d45376b2-91eb-37f1-8824-1e9bc12d89a5 | -3.07384 | -54.36993 | 2026-10-02 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ac7afe8-30ba-3254-8975-1606326e8050 | -4.2652 | -50.74723 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cba19600-27e9-38e8-a0e5-eaf33c47db9d | -3.04588 | -53.88272 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccfd9fab-af3e-3eaa-a10d-3e5f37412470 | -0.42087 | -51.98916 | 2026-10-02 05:33:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 961eefdf-7ec0-3efc-a0ad-8b1bd5c75196 | -5.8555 | -53.47522 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d078e493-614f-3370-a921-89e5e38b2e02 | -4.29249 | -50.78637 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb680da8-12c2-3145-a88d-1ba00a652609 | -3.26957 | -54.27662 | 2026-10-02 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2d6a7d6-0a88-3c90-a4d7-1fd897e23193 | -2.57017 | -49.99626 | 2026-10-02 05:33:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db34e865-3969-3bb6-a20e-6928c13583b8 | -3.56939 | -54.61973 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68b9adfd-95ca-37ab-b39f-537e3dc2d960 | -3.04283 | -53.8741 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3883c87-a2d5-3639-865d-30ed15b3574a | -4.31651 | -50.78247 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b3910fe-428b-36ef-9271-1c3c6ad1fd09 | -3.29834 | -57.85595 | 2026-10-02 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce49b846-ba14-3e87-aa01-63c2aa1d3960 | -1.65913 | -55.21342 | 2026-10-02 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a329e12-c0dc-3bbf-aa11-98c3343a78b9 | -3.15906 | -54.09496 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a426284-5fee-39f3-b6eb-033f7278607e | -5.65732 | -51.36473 | 2026-10-02 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 017a0ffc-8a4f-3cbb-9635-8b24cfdf3b0b | -4.27041 | -50.78632 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3963520-f4c5-3502-bc2c-8f239c7a0741 | -5.68016 | -50.09465 | 2026-10-02 05:33:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 481a2024-c934-3ea2-a7ef-30cc3c7642f4 | -4.27419 | -50.76944 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a45f0e56-da8e-31f0-a6a9-59dda66c173e | -5.26628 | -56.05102 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c874b2f-4ce7-370d-a5df-0511190d5313 | -1.60473 | -55.13196 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34dd0786-779d-3bf4-92f1-cd14d3310c19 | -7.39962 | -55.20377 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 29416aea-a22a-3030-87f7-09d56609b098 | -6.3903 | -56.4105 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ba66a39-f8fc-3503-83ef-8e562b955cdc | -6.40939 | -56.41342 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d2f5281-c470-303a-a532-c1feddfa7ad5 | -5.98077 | -55.37841 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aea25a7e-02e6-3d06-80f5-491f9df05722 | -7.48467 | -55.00277 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 649d1b59-4ab9-3c67-8d1a-28fe2b77e5b9 | -7.75093 | -49.20261 | 2026-10-02 05:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad014156-ebe4-3219-8932-fa2e6fb5d537 | -8.1625 | -54.80422 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c2dd5a8-f5c7-3dae-be92-320b57db57f0 | -8.55036 | -54.56416 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af772378-9e19-3144-8108-33e2e56a1bca | -6.40488 | -56.41747 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82898e0f-10f4-31d4-bdce-9c8e5de7cdb8 | -6.08001 | -53.30611 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8416a3a9-623e-39bf-b460-730c2fd5402e | -8.1817 | -54.79426 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d447def2-8b2c-3ce9-b63b-156e5061c775 | -7.05502 | -55.6433 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eec22f2-99b3-33cc-b406-4fc7091a7bda | -11.31027 | -50.92389 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eea3955-dbc7-3928-b9e8-5d308eb7ee29 | -7.2739 | -55.58895 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed39e12c-8083-333e-81dc-7c418638547d | -7.33728 | -55.57962 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad4d34ad-00b5-386f-81f2-556bbb9cd814 | -6.83827 | -55.26885 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16a66c0a-68bc-335d-a20e-0d0da2bcb5f2 | -10.26519 | -49.66377 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d75623f-7c7c-369b-84b7-e4a4a5220b17 | -7.83441 | -55.13721 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c75d33f-1beb-3bf5-92e3-504206aa2f88 | -6.40698 | -56.40353 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88e466a6-925d-3535-b436-131ce6223aca | -7.83208 | -55.12519 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed61f71b-d44d-31b0-9ad9-0888cb9f1864 | -8.07882 | -54.88194 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e516f34a-cac8-3e79-9a71-f0ca29cb1ab2 | -7.83974 | -55.13008 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c61ab8c3-00fc-3351-b30f-77caef0c26bb | -7.63695 | -55.04592 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 462d3a9d-6f5c-3fb8-8357-4e1cad6da521 | -7.19725 | -52.60958 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f1dafe7e-f816-39ab-8a00-ce91c02353dc | -8.1631 | -54.80008 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5eda80e-0d31-3720-83f9-0c8796534ae6 | -7.28095 | -55.59756 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fd534d8-78e9-3018-a109-80991005054e | -7.82728 | -55.12845 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36d920e7-325b-3058-b545-04b2c4e68b92 | -8.08255 | -54.88657 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45d01bc6-a942-3029-a577-7ea2a5176a84 | -8.16206 | -54.8378 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f28272b-b4f0-3da4-ab62-7058e01f10e6 | -8.08194 | -54.89069 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d7e9126-1761-3dca-8313-36dc91e5e8a8 | -7.34951 | -55.58139 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f584d54-93ef-3082-a076-d6ffa3d41bae | -7.39545 | -55.2031 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 87049dc2-792a-365d-b774-beb1c04c0afe | -8.25053 | -54.65593 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6da65c5c-4036-3194-9db8-4fbcfc53ae37 | -6.40176 | -56.41227 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c6d1f89-5127-3e23-a140-c2e595db7bf0 | -8.30869 | -54.72011 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README76.md)
