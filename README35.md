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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecc42a55-edf8-3516-9c3f-0ce6e7ea1c5c | -2.81727 | -54.13598 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1810acdf-44fd-30dd-9bf3-cc40526e7c97 | -2.85134 | -51.29535 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f6613eb-c216-3957-8b31-8d59cd0835d9 | -3.41881 | -48.33895 | 2026-10-05 04:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7debe435-d6a1-3aa6-9751-39e8e6896c21 | -6.89868 | -43.68999 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b04ba88-4500-39a3-b977-1550c34da474 | -2.81969 | -54.1209 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1550308c-7389-3166-ab90-64b0093d0c9e | -7.11497 | -55.72206 | 2026-10-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ae3f8939-b5b5-3062-8131-a3ddbd3b1849 | -2.89896 | -54.12879 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90fea9af-0935-3352-8eca-b2dd8a879c3c | -8.67773 | -54.54887 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8a66db38-15e5-37ec-ba59-42de8e468fb8 | -3.47022 | -50.10136 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 407aae13-b8fd-3369-a766-24828eef86a1 | -6.00712 | -53.52769 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e36566d-8928-319d-9ecb-3a728fa408f7 | -2.79738 | -54.10579 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd7ec97a-8a6b-3667-ae59-5f6f07887b07 | -3.18119 | -50.53732 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9c4e835-4f1a-31a5-99a3-cbeb3c5d7c08 | -3.65309 | -55.31751 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ace23cdf-fa1d-398e-a0de-672f2dae77d4 | -2.5823 | -51.87866 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9e879e8-dc7e-3a00-83fc-060fe31ac0be | -3.28024 | -54.18067 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d5a49552-3567-371b-9ccb-41b68ca30b10 | -3.90549 | -49.69891 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6ba24d7-81c6-35b2-a6b3-50d8dfaf666d | -2.93522 | -54.12301 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19031368-13c4-3554-84ca-d69912cd5aef | -3.07208 | -54.16733 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 47ef3316-4d15-3b72-b56c-afb4de4d8b2b | -3.50573 | -54.60931 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 540120eb-25f1-3f75-a8ae-b1c7d6f52ac5 | -3.29757 | -53.8528 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83e0276b-a235-39a4-95ee-02662d1e80ca | -6.12382 | -53.0513 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7a03ef6-4752-3f1c-b7d4-4b921516a087 | -6.04871 | -53.28769 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbd4c011-0ce4-3b0c-94b8-91cf39f6355b | -1.24914 | -55.88351 | 2026-10-05 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c2b6213-21c9-3758-a17f-40f535c2cfd7 | -3.47139 | -50.09391 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fe354fb-1ece-3b2b-acd4-a385f8745b16 | -6.26611 | -52.86079 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0d6ebaf-10f4-3f1d-b2e2-0d435637a749 | -2.22297 | -53.70875 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 031081d0-f476-376b-9804-0d61eabcea94 | -6.89614 | -43.6689 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f047839b-b349-387b-9b9b-96de933f7445 | -3.9066 | -49.71466 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac91bd94-dc9f-32fd-ab5f-f20eb0016599 | -3.1374 | -53.73425 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebf85f0a-65bc-386f-98f4-c3034766c44d | -3.7016 | -50.66147 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 598673bf-65b6-3ff6-90d3-59c25b92e385 | -2.96874 | -54.0899 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 835cf920-9da6-3679-8967-e4b5518ceaa6 | -3.46506 | -54.59491 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 83455417-eab7-3656-886e-97e025b10ade | -7.2224 | -55.19867 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7929b29c-4a3e-37b2-a450-40fa2dd185be | -3.80756 | -50.85403 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67ed1c19-5933-32c6-a011-5f28e41878f5 | -3.05844 | -54.23081 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d50de597-8bb4-3762-8b9c-77940684710a | -6.27731 | -55.41599 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cc86da6-8fbb-3a17-88e5-25701b3217bb | -1.88057 | -56.28301 | 2026-10-05 04:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 75163984-2edc-30bf-b3a4-073402db5cd5 | -6.00435 | -53.52366 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c30e9b6-8cf3-3a25-9735-15d83c0bad55 | -2.90057 | -54.07521 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01b58de5-a774-31cc-b0eb-7b8e40295206 | -2.8215 | -54.10962 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3d1da70-726d-309e-b1c1-ccf93f203a86 | -7.50969 | -54.98605 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1009b40a-2178-3238-8486-ebe53a8c0635 | -3.40001 | -50.14816 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af26ebab-3c89-35bd-8d51-1165d82e53f7 | -3.10899 | -53.75962 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 36becb5f-0448-34f3-9fae-d3cd8a60173e | -4.45865 | -54.96618 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0cb0229-fec5-38ac-9e7f-fecbf0c66ffa | -2.9472 | -54.1365 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f73432a6-2657-3ce2-9de2-c854afb5bfe4 | -6.24075 | -52.84969 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ae3cf46-6de6-3522-8f1e-d0e96e0dacb2 | -3.76383 | -49.56497 | 2026-10-05 04:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20ad8cee-7fc4-3f69-a718-699ad112bac1 | -3.11414 | -53.74922 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55549327-c73e-346f-bbc4-28708471f54d | -2.85024 | -51.30228 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9f0a8f90-0a9f-31bd-84d6-d99884bcd2c8 | -3.00031 | -54.21779 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9689118-4f40-3404-834d-92bb4c7072d1 | -4.06005 | -51.12578 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6104b8e6-476e-3fbe-8166-f51f7033b0ce | -4.59674 | -49.62897 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 23ade889-5591-34b7-b0c3-16e29dde699a | -3.50923 | -54.60987 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9805dbdf-ac90-3ce0-94e3-24157abd4955 | -3.02171 | -53.88893 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bde4ae8-d3cb-307f-a85a-534c27825858 | -2.97503 | -54.09474 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd6b78bc-aefe-3450-a335-7d180ba6e7ee | -6.21554 | -52.68691 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 864f3cb0-95a8-3b9f-b509-30f70089d84c | -2.82072 | -54.13653 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32acc86c-d3c6-3965-84cb-357e417c74b8 | -2.5828 | -51.8541 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4503b7a1-9a69-3c5b-ac29-dc2595578599 | -6.31652 | -43.34413 | 2026-10-05 04:57:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13a05895-4745-3212-8056-e9f7844a184d | -3.86322 | -55.82657 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5513b34e-b636-332f-880b-ab7ea836318f | -8.66536 | -54.56157 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03664ae6-65fa-3587-a4f5-df7eb60e3d0d | -4.0539 | -51.12127 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a11b5ce-bb55-35b3-a58b-c129f3aa5c38 | -3.12794 | -50.34004 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00d79395-87c7-3882-801a-31969ed0e117 | -3.57692 | -55.55973 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a517a4fb-57ea-3ffb-a423-6914f19b0b7d | -4.08155 | -48.96151 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 512cdbf6-93e6-3a14-813c-a01f6af40f66 | -3.10958 | -53.75597 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f260ce87-963d-3055-bc5c-c435b501ffed | -3.13012 | -53.71444 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 4155b7f6-e348-3769-81b1-63fac71971c4 | -6.89566 | -43.67231 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efdc4057-40e9-33b7-befc-9391e8632cc1 | -6.16398 | -55.37852 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 949f90b8-89c9-3acf-b4e1-4111ada1ec33 | -3.10337 | -53.75125 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d8b6415b-b721-3ddb-b437-e705080dbd7c | -3.90816 | -49.71025 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2e33fea-bbda-3ba6-8821-05bf706463ad | -2.82779 | -54.11448 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f7072d5-6d6b-3992-a10d-d35d8a327762 | -3.39942 | -50.15187 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0190cb80-c0f8-3489-87b2-e4e633176691 | -2.97495 | -54.77834 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d46e68f-a05c-3143-a070-a04a9c06172b | -6.90642 | -43.67375 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75b83454-c276-3305-898a-7228987da155 | -2.68896 | -49.03495 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e48c09be-bdab-315e-93c2-a58c5ce314f9 | -5.89105 | -53.63877 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c9e8246-b5a1-3450-b426-fb9274b6b457 | -2.49724 | -56.14513 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4eecf6e5-cb02-3608-ada6-5057f0a56056 | -6.41866 | -51.95702 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 250b8a47-2e3c-330c-abcb-099f795f2fef | -3.0508 | -54.16778 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3fb4ca3-2bf5-3364-bcb6-a257fbfff238 | -2.85881 | -53.92073 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a5c5cd8-b2c0-36e1-b226-8ba2a91ada6e | -3.07029 | -54.17857 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 772f7536-0986-3083-8d14-cd83ff9f33f3 | -7.45162 | -63.56185 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d3fb655-6b03-35ce-b19b-84e4e02942fd | -4.28073 | -50.27223 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc07e361-72da-3522-85cc-190541cdbb84 | -2.75575 | -51.55677 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e5bba26-c34d-396b-99c8-1f87ca4a9b20 | -7.4408 | -63.55725 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb42678e-e674-3e64-aecf-0f7914fdacf7 | -7.22523 | -55.20306 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c28befd1-eb1f-349e-9f7d-76c02c6b5736 | -7.43856 | -63.5696 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d24861d6-137f-34e5-877c-dc6aed12c59d | -5.98869 | -53.64344 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ba53a67-7319-38b0-924a-10fe8302a9ae | -5.96853 | -55.37617 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08189c56-7ee8-3768-a07d-259540044598 | -2.78765 | -54.10041 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12487ca8-f68c-365f-a917-8ba7ce034457 | -2.93178 | -54.12246 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 439db3d2-4f6b-391e-8f3d-ac0b7de7e0bb | -3.00906 | -50.47014 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58106e80-6862-3f16-ab81-883e29d43f3d | -2.9657 | -48.92378 | 2026-10-05 04:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdfd94a8-9130-353f-a75b-2744e88e21d7 | -5.84173 | -53.8192 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e41643b-06c9-30e5-9582-8e1a27434660 | -3.54955 | -49.35975 | 2026-10-05 04:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 819c591f-95bf-38eb-9802-db188d8b8fdf | -8.6531 | -54.55217 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbd23dcb-4c58-3c02-967c-041d33703a7e | -2.91438 | -54.14282 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8ea6215-997a-38ff-859d-883d8b147d6b | -2.91637 | -54.10846 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1385bd30-249b-3fdb-8b3f-c4ad2173d1e6 | -8.6693 | -54.55853 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README36.md)
