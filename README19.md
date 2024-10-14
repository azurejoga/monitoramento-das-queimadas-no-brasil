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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2096ebfb-ccb9-3a88-933d-aaf4dd2e0207 | -2.58778 | -51.86088 | 2024-10-14 01:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 48be8e4f-7ea1-3d7b-a877-4a57a1b882b8 | -2.58623 | -51.84993 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 449ba2c7-2824-3b57-8996-249f36f8ac01 | -2.57799 | -51.86235 | 2024-10-14 01:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c1befaee-5598-3627-88e0-e9aedbe939a4 | -2.57644 | -51.85136 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0f5466ab-ca0d-3037-b993-eaa0cbe4eba5 | -2.56791 | -54.01152 | 2024-10-14 01:20:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 94b7ec58-a189-34ae-aa98-905675b5ed4e | -2.5273 | -49.02232 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 3e0b7cc2-2833-37d3-b551-0ad6738eb79b | -2.47299 | -48.19576 | 2024-10-14 01:20:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2aac0fee-093a-368c-a5f9-5ea6c8381c01 | -2.44891 | -46.93372 | 2024-10-14 01:20:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 8a1938c5-9672-34cc-b87f-c7da82cc8b11 | -2.44708 | -46.93968 | 2024-10-14 01:20:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 29300d77-3088-3f82-a5e2-3440dbd60461 | -2.44501 | -46.90813 | 2024-10-14 01:20:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ff09dd05-5a26-3195-8e83-43da28b5d7ef | -2.44334 | -46.91385 | 2024-10-14 01:20:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| b894332a-6f98-3983-946d-c624e2aca43d | -2.442 | -54.83029 | 2024-10-14 01:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e53bdd11-9f15-34f5-a7dd-13c2bd540fdb | -2.42254 | -46.16191 | 2024-10-14 01:20:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 50677e3f-62dc-3ab4-ac73-4be097408e6a | -2.26257 | -53.4808 | 2024-10-14 01:20:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 28cb87ff-ce3f-3454-ae43-c4658cc72f26 | -2.25353 | -53.48211 | 2024-10-14 01:20:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0117ecc0-e743-30de-a80a-999b6703fe41 | -10.37598 | -61.20245 | 2024-10-14 01:20:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 141e5f01-499f-3966-9c30-d96dc9f66a93 | -10.05332 | -59.00299 | 2024-10-14 01:20:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f3c5dafd-ce76-33ab-bb2a-01574234625d | -1.93668 | -52.09752 | 2024-10-14 01:20:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 07b7da4f-5052-3173-a965-4b30ef702a8f | -1.72243 | -52.53289 | 2024-10-14 01:20:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fe9d0541-ffdd-3e95-9dc9-0ac051ceb124 | -1.72096 | -52.52262 | 2024-10-14 01:20:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 648228ea-3ac0-320f-96e7-54802831ec67 | -1.69087 | -53.81078 | 2024-10-14 01:20:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2c3f7d5c-f6ee-3f98-a3ed-02bf538752e6 | -1.64919 | -55.09555 | 2024-10-14 01:20:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| be542a3a-051f-3d47-9d47-88ef1c5ed30d | -1.64797 | -55.08678 | 2024-10-14 01:20:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0b7b18c5-c5ec-31c4-a05e-e464d5abbbc1 | -1.42288 | -53.47488 | 2024-10-14 01:20:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 3437dcf5-237c-322c-8559-25bad1165086 | -1.42157 | -53.46552 | 2024-10-14 01:20:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d26d84d0-75b9-33d5-bc4b-ef457d8e9cf5 | -1.34663 | -56.0358 | 2024-10-14 01:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2bacaad2-c366-3d3f-bca1-004de00ab02e | -9.1004 | -61.17577 | 2024-10-14 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 26b3e3f7-77ef-31e2-aa58-e9b9e127f17d | -7.87055 | -44.00163 | 2024-10-14 01:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 51cef427-c8a3-3ab8-b2b2-4f69ba16c0b8 | -7.86464 | -44.00815 | 2024-10-14 01:20:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| be89ffa2-ee82-30da-813b-cf147afa2009 | 0.79851 | -51.92723 | 2024-10-14 01:20:00 | TERRA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e20f2e69-8870-355f-98ef-2f2f80316d8a | -9.76179 | -55.35382 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5d1e8be2-d18d-3e44-a859-fab4d5bf4067 | -9.76046 | -55.34381 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 65522b79-c49d-3443-b65a-41c037a56620 | -9.73262 | -52.85262 | 2024-10-14 01:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bbc4de3b-ebec-3b70-8b5c-340b8b53dde3 | -9.72884 | -52.82573 | 2024-10-14 01:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9c526f6-21c0-36a8-a221-aa964d0e5fc3 | -9.72758 | -52.81679 | 2024-10-14 01:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7b1c6727-1dc7-30f3-8b23-9124fcd1c426 | -9.71873 | -52.81812 | 2024-10-14 01:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 15cc8278-eeca-3bfe-886d-140d0fed6be4 | -9.71617 | -52.86413 | 2024-10-14 01:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4752683a-a7c0-347b-b37a-f7286c34fcaa | -9.71492 | -52.8552 | 2024-10-14 01:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 229f8751-f817-3f8d-b90b-f15e2bb34c7e | -9.70988 | -52.81945 | 2024-10-14 01:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 717e0d32-e906-378d-8076-fd80117ea95d | -9.70228 | -52.82964 | 2024-10-14 01:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| af15c47f-e679-3dee-9f64-8b0a13fcec3a | -9.49356 | -50.97876 | 2024-10-14 01:20:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9ae1afa4-2930-3991-a251-498017631d0f | -9.43112 | -53.20314 | 2024-10-14 01:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8ff15205-e16d-3990-8df4-3600bc820f2c | -9.42988 | -53.19425 | 2024-10-14 01:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fd953905-2645-3848-9cd2-59407a1c86cf | -9.33684 | -52.85261 | 2024-10-14 01:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 3947d513-6aea-3865-bfdd-96d70c78b926 | -9.33558 | -52.8437 | 2024-10-14 01:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| e7c07b9f-00c5-310e-8242-b3d4767afe05 | -9.33041 | -52.5502 | 2024-10-14 01:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9ca11764-1b96-3fa6-a8f2-e474d55c36e7 | -9.17035 | -51.493 | 2024-10-14 01:20:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8c97aa2d-2e4f-3c40-baf9-e0a297aa2014 | -9.11472 | -61.17411 | 2024-10-14 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 6fdad010-9ceb-371d-8589-e7606999cac0 | -9.11171 | -61.14856 | 2024-10-14 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 272236e4-9dcf-3ae1-a401-83c7473c489d | -9.11167 | -61.18093 | 2024-10-14 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 39832c30-c7e5-3f04-ad4f-002a0026f6cf | -9.10848 | -61.15541 | 2024-10-14 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 671941d8-6075-326a-8222-bb4dac9bc38f | -9.09735 | -61.18259 | 2024-10-14 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 6b56bdad-f549-387c-a696-ab06631e4e19 | -9.09418 | -61.15703 | 2024-10-14 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| ab107700-d3ce-3ce5-91f7-85e2f99dd5de | -9.04338 | -53.00214 | 2024-10-14 01:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 48f5cfee-2e7c-3ed6-be7a-3f37e952009a | -9.03587 | -52.94844 | 2024-10-14 01:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0fbafb1d-ee99-3d18-973c-bf65d1041899 | -8.9785 | -47.74508 | 2024-10-14 01:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bd97b2c8-d1ad-378f-83d1-a0167ec73ea0 | -8.91335 | -47.91919 | 2024-10-14 01:20:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 54d51ed0-de08-3dbe-84b1-88f4a9aaf249 | -8.88935 | -50.13062 | 2024-10-14 01:20:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e16d4b27-6842-3065-81fd-d38b4a09b0a7 | -8.85433 | -53.03278 | 2024-10-14 01:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 02f47959-8403-3809-97c8-436ffecd771e | -8.85308 | -53.0239 | 2024-10-14 01:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4eb82598-28ff-3b05-b779-7bc4475d6c04 | -8.71307 | -46.63712 | 2024-10-14 01:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c1ea2515-aeab-3c2f-bf26-bf618203fc2b | -8.48127 | -48.62923 | 2024-10-14 01:20:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 0fc55873-b135-3ff0-aa33-359b35ba4121 | -8.47897 | -48.61399 | 2024-10-14 01:20:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c525294a-4011-3add-8e97-711ad1e4514b | -8.02727 | -49.64838 | 2024-10-14 01:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f730f4b1-a6a4-3a2f-9ddd-2ab9b5ebd932 | -8.0253 | -49.63543 | 2024-10-14 01:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| a8cb1042-8b8b-3a69-9bec-387ac21019ae | -7.96226 | -49.0764 | 2024-10-14 01:20:00 | TERRA_M-M | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 55.4 |
| db9fc752-5250-342d-b1fd-7f8ae11ac6c0 | -7.96008 | -49.06209 | 2024-10-14 01:20:00 | TERRA_M-M | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 155.3 |
| bb15850e-3db3-34f0-8cc0-132730488900 | -7.95203 | -63.64863 | 2024-10-14 01:20:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 70d0c821-92f2-3947-98cf-91e4d3e04ab9 | -7.94861 | -63.65596 | 2024-10-14 01:20:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4bfdcc31-6234-3aef-bd48-3deca1a7b28c | -7.9476 | -63.6104 | 2024-10-14 01:20:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| ef4446a6-e8b3-3a6f-8ddd-c4fd8f61e25c | -7.94393 | -63.61778 | 2024-10-14 01:20:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ecf37289-54f0-3702-951d-f15c9e6a49e7 | -7.87144 | -54.71163 | 2024-10-14 01:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1422d339-7734-316b-85e3-438fcd7533a1 | -7.8702 | -54.70255 | 2024-10-14 01:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b681ae07-1680-3478-8a21-d3a205004442 | -7.85319 | -50.18826 | 2024-10-14 01:20:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 12d47e0c-7412-32c5-90ea-6152e0f62606 | -7.76615 | -50.57131 | 2024-10-14 01:20:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8ee30275-85c1-334b-9038-2b96f6f208e5 | -7.76452 | -50.56005 | 2024-10-14 01:20:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6a3e31b7-09c2-37e9-be7c-8287a168d62c | -7.66518 | -47.32587 | 2024-10-14 01:20:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4748a26d-2226-35c3-8edd-55aa20e5104c | -7.271 | -44.96989 | 2024-10-14 01:20:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| f8a225db-d1d9-3452-b736-5fdacfade8da | -7.26648 | -44.96531 | 2024-10-14 01:20:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 48497701-4b6b-34ca-b93e-9dac1d34a3aa | -7.2555 | -44.97211 | 2024-10-14 01:20:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 3ad0cfe6-ddb5-3a12-9b42-ab99ef669681 | -7.25098 | -44.96754 | 2024-10-14 01:20:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 23a8ad8a-8f17-3840-94db-0c43c0ab3d28 | -6.23487 | -46.45622 | 2024-10-14 01:20:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 607ba40f-c4e7-3fb6-bf44-801fbb5402e0 | -6.19513 | -50.88875 | 2024-10-14 01:20:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| efafa224-81e1-3bb6-bc1b-e97bda94b88b | -5.99666 | -53.35338 | 2024-10-14 01:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 72e8ceca-183f-300a-be7d-fa33a2f258bf | -5.60934 | -48.95507 | 2024-10-14 01:20:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2bf6701f-4f45-3b8c-a662-777d451cc297 | -5.2223 | -46.01656 | 2024-10-14 01:20:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 03df061e-0fe0-3b50-95b7-7d05f3689923 | -5.16959 | -45.39209 | 2024-10-14 01:20:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 798883cf-8561-3fd5-89da-b177e8c40ac7 | -5.159 | -45.39905 | 2024-10-14 01:20:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| c08eb45a-1c1e-309a-8da0-ac8fb3684db7 | -5.06463 | -45.88188 | 2024-10-14 01:20:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 30.3 |
| b4f7c4b7-8e37-363e-93d2-37ec98cff3fc | -5.06307 | -45.87661 | 2024-10-14 01:20:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 1b915e73-30ad-3ef9-961c-b4d461487a2f | -5.06209 | -48.07271 | 2024-10-14 01:20:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 4ce929c4-ce81-37a6-8147-32cd5b71ed74 | -5.05926 | -48.05391 | 2024-10-14 01:20:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 2e734ae2-9c85-3dc9-8081-2278c0c61c89 | -4.90358 | -46.02808 | 2024-10-14 01:20:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e34a7a3f-ffe4-3b03-bae2-d778904cbab7 | -4.90023 | -46.00524 | 2024-10-14 01:20:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 14f8bd31-9b1a-3168-bf06-52bfa850f2df | -4.89918 | -45.99997 | 2024-10-14 01:20:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 109cae40-7af0-3a7f-889c-f31ec1c1f40c | -4.71058 | -46.15742 | 2024-10-14 01:20:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 332028d2-ea24-3840-9278-c7e7f794e32f | -4.71048 | -46.16316 | 2024-10-14 01:20:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 702439ef-ed46-38be-a73f-d51d1227a36d | -4.70708 | -47.30231 | 2024-10-14 01:20:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 31dae91d-b2b2-3768-9ec6-7c4c13fcde25 | -4.65893 | -46.81088 | 2024-10-14 01:20:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 10308676-962b-3f0b-b486-d14017da654b | -4.65436 | -46.81697 | 2024-10-14 01:20:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 26.6 |


[Clique aqui para ver as próximas entradas](README20.md)
