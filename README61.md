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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13c652b7-acdf-301c-b2a0-34fb5db25a48 | -4.53458 | -56.12186 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 679dee5c-e926-3dd6-9d3d-81442aa4c3cf | -4.53402 | -56.12534 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 823c2e58-eefe-3c15-bb4e-b4ac4e990fe8 | -4.53345 | -56.12888 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 94f74376-1c49-3d3a-ae18-caad7815b8d7 | -4.51733 | -55.55078 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59fb44ec-88b7-315c-9a2d-87cc8d35e3b6 | -4.5093 | -55.66095 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2adb5d04-6067-3915-93a7-859426e50773 | -1.45293 | -57.81472 | 2024-11-03 04:46:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51c0245c-cfbb-3a9b-b856-70fabcf7bd5c | -3.01281 | -56.93187 | 2024-11-03 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e89848c1-284d-3341-90f9-9f17211609bb | -2.95466 | -56.7654 | 2024-11-03 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3aee7e84-9c66-39ad-b37d-566a5842f33b | -3.53955 | -56.89287 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f02de0f-77cc-3625-a247-6b7010ee85b1 | -3.44635 | -56.93229 | 2024-11-03 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05ef8458-ec84-362d-a1f2-dfe2e577e452 | -3.44562 | -56.93669 | 2024-11-03 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca74791f-be45-3b80-bb8d-00ccdfd2a2a3 | -2.59621 | -56.99894 | 2024-11-03 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b65450ca-9544-3589-8b28-622013f6a00d | -2.58168 | -57.57339 | 2024-11-03 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 766d770d-c15e-3ae2-ba56-37c7f4f255b2 | -2.58092 | -57.5696 | 2024-11-03 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0abc695-25ff-37a9-b571-ad6fad819984 | -2.57854 | -57.5847 | 2024-11-03 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32c99bb3-1252-377e-aee0-bebe33e0caae | -2.56739 | -57.11835 | 2024-11-03 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 979c7134-e258-3724-9842-ffa03aa3c1b6 | -2.56662 | -57.12304 | 2024-11-03 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 83135619-cdc6-32de-83c3-f1534a075dc3 | -2.67733 | -46.7498 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fddd8113-9fd7-31af-a1ef-58c9d0de08b9 | -2.67497 | -46.74066 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f78a3167-d2e9-322a-a16b-091978cd8eeb | -2.67432 | -46.74495 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20ae4959-2b37-38c0-97a1-b0939ec6a274 | -2.67367 | -46.74923 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bec8305c-fc03-3416-a565-c8e2c3438afc | -2.67302 | -46.75349 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0db18c7-5bc2-3abd-a913-486c1cd74406 | -2.67195 | -46.73579 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b1af801-f93c-3f9c-acef-8a4b5bea4c30 | -2.67173 | -46.76205 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72543450-7abe-3c12-bb4f-2c8fdf566510 | -2.67131 | -46.74008 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b812e277-7fc8-34d8-9e43-87f3e71a9ce1 | -2.67001 | -46.74866 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17bf7476-aded-3321-9b54-bf9dded9d55c | -2.66936 | -46.75293 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b608283-33d0-39de-815a-12f6a596ecd6 | -2.66872 | -46.75721 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5011b443-4379-3523-826a-f71175803816 | -2.66807 | -46.76149 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d58c789d-479a-3ac1-9f13-d47d8c3407bf | -2.6657 | -46.75238 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04e124e2-67f8-339e-b097-bc6ed1f72201 | -2.66506 | -46.75665 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff604e58-2a84-30a9-8237-43478a20cdb3 | -2.67863 | -46.74124 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48ac2e80-0de5-3a4c-85cb-a7d6951bd53f | -2.67798 | -46.74552 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4efb889a-e159-3022-abfe-f4b9cda9d882 | -6.90015 | -38.56219 | 2024-11-03 04:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e648a134-43a3-3b24-9c26-86eba0682d4a | -6.89938 | -38.56803 | 2024-11-03 04:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f23a2f51-b315-303b-b473-c1c8e6124927 | -6.85833 | -38.46641 | 2024-11-03 04:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2ec7956a-fd0f-39c8-82fa-b4900bb92d4e | -6.85452 | -38.46433 | 2024-11-03 04:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 22be3476-e6c4-33fc-a1ec-c1f3d078b84b | -6.85374 | -38.47013 | 2024-11-03 04:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e3b0ee97-9349-3166-ad66-19fe3571b337 | -6.52873 | -41.48693 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 42a03c70-ff02-324a-981d-1893dae6e7dc | -6.52826 | -41.49051 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 805cec6e-83c9-315e-b2c4-8be3c6a17756 | -6.52811 | -41.48829 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 30aa5151-cf08-384a-a32e-3ffa8b1a3af7 | -6.52779 | -41.49411 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 01951527-be8c-3293-ae9a-8ee6db2d7437 | -6.52761 | -41.49186 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| e3fe82ac-b6d9-3ce8-8e2d-2bda0d60dd34 | -6.52314 | -41.48373 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 1a7ffe7b-d015-37fb-aeec-ff5ec3f1fcf6 | -6.52265 | -41.48727 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 6529f919-48dd-3539-b8c6-f437f1d1a2b1 | -6.52215 | -41.49088 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 60a04ebd-2b4c-3e69-bed2-ad665423772d | -6.52164 | -41.4945 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| d0beaa40-0714-3e43-b638-13725ad0d9d6 | -6.51719 | -41.48629 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 9aded0ee-ab3f-39ef-9d43-e66110d6ee46 | -6.51669 | -41.48986 | 2024-11-03 04:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 85e7466b-e97f-3988-9c94-6302a52f324e | -8.49474 | -42.09555 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| abdad347-e67c-35d7-8ed1-1f3c979e6d67 | -8.24172 | -42.2219 | 2024-11-03 04:46:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 544bd4ed-ab71-3b1d-8f7d-cd9f47bd0306 | -10.58009 | -41.48225 | 2024-11-03 04:46:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7c44c6d8-eac6-3119-adef-d870081ba573 | -10.57994 | -41.48294 | 2024-11-03 04:46:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d933e5cf-6e42-3b48-a73a-e6340f13d350 | -10.57963 | -41.48613 | 2024-11-03 04:46:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 17c9494e-0eb3-35e7-ab29-374dd3891068 | -10.57945 | -41.48683 | 2024-11-03 04:46:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6686199b-b3df-32a8-9d09-3b9e74312559 | -5.47194 | -43.17544 | 2024-11-03 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74e4f03b-cd15-32de-a99b-2a6b099f13cc | -5.2954 | -43.07675 | 2024-11-03 04:46:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7dcccfaf-c7ef-32ba-8956-11b13aaa7e46 | -5.29057 | -43.07594 | 2024-11-03 04:46:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 21f8cba7-7b0b-38b8-aef7-a3c3f80aa729 | -7.66123 | -42.76002 | 2024-11-03 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c061dfac-74cb-3109-88c2-e6141fbcd1cc | -7.66082 | -42.76312 | 2024-11-03 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ead6e3d6-ea66-39a0-90d9-6e262551dd88 | -7.65611 | -42.75928 | 2024-11-03 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 159b9cd9-26b1-3e5d-901c-a9f57ccbd4e8 | -7.54596 | -42.86079 | 2024-11-03 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a6dd8bf-447e-33f0-aef2-119588069403 | -8.33947 | -43.5742 | 2024-11-03 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf410073-b14f-3029-84f5-4f408a91ec72 | -8.32967 | -43.57295 | 2024-11-03 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3096574-5958-350d-8189-c05150a1d542 | -8.32894 | -43.5784 | 2024-11-03 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ea8a398-4cba-3d69-a11b-77e40291e008 | -8.0072 | -43.34935 | 2024-11-03 04:46:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c558e2d7-e43e-38ee-b880-86e87a06aa22 | -9.79271 | -43.87329 | 2024-11-03 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 330dc04b-4523-3851-af11-3511372cce4e | -3.40199 | -44.16346 | 2024-11-03 04:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7de24d9-0bcf-3c6f-b3c8-36cda75c5392 | -3.40138 | -44.16761 | 2024-11-03 04:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bed75563-1c3a-368a-b99c-a423f3f2aa53 | -3.13618 | -44.16878 | 2024-11-03 04:46:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d513098d-b2c0-3a6a-8972-7a31c01385d7 | -3.13444 | -44.17036 | 2024-11-03 04:46:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9fbab387-b90b-332b-be66-39217158cc71 | -4.41194 | -43.4567 | 2024-11-03 04:46:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bafd15f7-f370-3a97-9f28-44e907672c82 | -4.4105 | -43.46645 | 2024-11-03 04:46:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6d1f2b1-7960-39a0-ad5a-8651ef5e6dcf | -4.40728 | -43.45607 | 2024-11-03 04:46:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d620db39-29dd-33eb-9db8-770f13e6a101 | -4.40656 | -43.46095 | 2024-11-03 04:46:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b05416bf-cd10-330c-af8b-284211e714ea | -6.11835 | -43.97364 | 2024-11-03 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf6cb477-3b6c-35f4-9a19-3537e0a5ed3a | -6.18484 | -44.52205 | 2024-11-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7368112-c1b2-30f9-a118-0c14d2eafeed | -6.18417 | -44.52672 | 2024-11-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 292aa711-d688-389c-aba8-fa0e80adff92 | -6.10601 | -44.75935 | 2024-11-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e05d68b0-cc20-3959-bc38-f9ed3b137dfe | -6.10542 | -44.76355 | 2024-11-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48368b41-c961-33a0-bc95-140c86846df4 | -5.42054 | -43.36218 | 2024-11-03 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a49405e5-a6ca-3892-b0de-92a8ea126ded | -5.41643 | -43.36289 | 2024-11-03 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4cb541ae-aa58-3e99-bb3f-3a5f7ce48ac3 | -5.41577 | -43.36161 | 2024-11-03 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eba4b34d-f487-3027-8c7e-7a4f88e77fed | -5.16152 | -44.22924 | 2024-11-03 04:46:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 240f2b72-3ccb-33d9-9174-7e925fc8c03c | -5.06338 | -44.22461 | 2024-11-03 04:46:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee502baf-b517-39ab-8d41-4b17e2038476 | -7.45428 | -44.73103 | 2024-11-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6ee0fe8-4e47-3ac6-b687-282a8b4d8198 | -7.44921 | -44.73472 | 2024-11-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62f51719-dd59-3afc-a411-887b4375ef1e | -7.44667 | -44.7205 | 2024-11-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 147fe6e3-a04b-377d-af79-3b5f84b526aa | -7.44603 | -44.72501 | 2024-11-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06867f71-73e9-3795-b2d0-13688133608d | -7.44414 | -44.73837 | 2024-11-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 837641bb-f710-37bc-9335-53d7aa47bcb4 | -7.42761 | -44.7266 | 2024-11-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17f4a82b-6388-34e3-a20c-209a2f8bdba1 | -7.42254 | -44.73035 | 2024-11-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26db10a8-d786-3d14-a128-6acf3d14e821 | -7.41808 | -44.72969 | 2024-11-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16f6636e-2d00-3af9-a3d4-0d5f555f1f52 | -7.18358 | -44.95985 | 2024-11-03 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53fd527a-810b-3fab-a9aa-be68f4a3de55 | -6.90719 | -44.62617 | 2024-11-03 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3343b0d4-5071-32d0-9824-2a8cb74b38c3 | -8.48609 | -45.48745 | 2024-11-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab485edb-0b91-3e2c-a3bf-0a0914aca692 | -3.41321 | -44.95897 | 2024-11-03 04:46:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0079ad85-f2a6-3833-80bb-613455166674 | -3.27369 | -45.35583 | 2024-11-03 04:46:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ce17427-1803-3d9d-aeec-210bd76e86e1 | -3.15621 | -45.0603 | 2024-11-03 04:46:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94577f5f-5267-3f7d-b5a2-360b01ae2f75 | -3.06649 | -45.92244 | 2024-11-03 04:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README62.md)
