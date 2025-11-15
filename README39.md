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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cee770b-0cd6-333b-bafa-7eea4bd142f5 | -9.01832 | -44.17509 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae47f6df-c562-3a38-9366-f13f474ef9aa | -4.36318 | -47.22775 | 2025-11-15 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1cfff0a-2590-33cf-b160-fe45157cf4aa | -7.4495 | -42.76451 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 947aeac7-7515-3471-8644-0c24091dfbde | -4.47173 | -42.88066 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf1f2fc6-5fb1-3f8a-ae31-0186260d5c62 | -3.92036 | -49.87427 | 2025-11-15 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24a3f96c-fd2b-36a0-8460-0712db65a177 | -6.14502 | -48.04419 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 42589581-1fd2-38ce-bb77-d237dcaf073a | -7.44446 | -42.77296 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a36df8fb-30e4-379e-8745-2d3c52ed5873 | -7.45053 | -42.77095 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b159ee5d-f852-3081-bf65-585790772b0e | -5.84188 | -46.66619 | 2025-11-15 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd859c4b-9599-3630-9fd0-6b407a3aff1e | -6.10607 | -44.22193 | 2025-11-15 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de027a26-ecad-3853-8e31-a152738e2769 | -9.48893 | -47.28229 | 2025-11-15 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dfcc888c-4142-387b-b9b8-54df791509fc | -5.53802 | -44.9478 | 2025-11-15 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5827983-d0bf-3f02-8545-55768cd914e9 | -6.00159 | -45.39424 | 2025-11-15 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1d388e7-4798-38ff-9b30-2890612c50da | -3.10771 | -45.4958 | 2025-11-15 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57e871fe-c3f1-3d44-b1a5-703d664a6d8a | -9.81602 | -45.33272 | 2025-11-15 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a4065d84-3f57-3b82-b07d-46b6d3229bff | -5.34785 | -44.77348 | 2025-11-15 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dacff8f-6581-3923-b0be-65e93d3bb797 | -4.19193 | -45.45155 | 2025-11-15 04:25:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98b1c3c0-094f-30b6-85c1-8fe08446dd8c | -6.77504 | -46.22292 | 2025-11-15 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e099abc5-86c4-3969-b42c-69d6451405aa | -7.43226 | -45.23228 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1889cf1f-3c49-3e90-8ec8-061e4182940e | -3.99875 | -47.66986 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f10fa15-fca4-36a0-8bf9-443591ce46ff | -3.88097 | -47.17778 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81e44b3b-8a98-3bf0-815e-810b79704b60 | -4.00654 | -48.80617 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b9af594-caec-3d64-98a1-962aab898fc3 | -2.51408 | -47.81329 | 2025-11-15 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 0177ac8c-5a05-3422-8a9f-f3b6f4e2895a | -6.08177 | -44.87902 | 2025-11-15 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5db5fcc6-3e93-3c20-9aaa-401ed739228b | -2.63738 | -45.76258 | 2025-11-15 04:25:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf2be705-518e-39e0-89c0-9d14eaef49fd | -5.84072 | -47.56398 | 2025-11-15 04:25:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4dcc2e6-2923-3874-b099-8081103affb1 | -8.38549 | -46.99783 | 2025-11-15 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6ef6506-563f-3d00-8d32-d144538d8742 | -3.59515 | -54.67609 | 2025-11-15 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 338a93ff-96d8-3efc-b1a5-c9697055516a | -7.26647 | -48.02734 | 2025-11-15 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f59c454-a64f-3dcb-9ca5-52a16d0818e4 | -7.52425 | -47.19881 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46a1db53-cbb5-3031-944e-8474d93aed87 | -4.39385 | -44.07854 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bafc91a0-eba7-371f-9e4f-82503fabb142 | -10.42995 | -40.54895 | 2025-11-15 04:25:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0378918f-7397-3b24-8de4-e7323fb09f98 | -2.51817 | -47.81 | 2025-11-15 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 750413d0-2542-3737-9d08-bf3b7f704798 | -9.44202 | -44.86767 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8947b12a-88bc-3623-ad73-0a9548850924 | -6.82239 | -48.82927 | 2025-11-15 04:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cddb7f5-4f52-3a5b-b63c-0587ed2d929f | -8.38824 | -47.00184 | 2025-11-15 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05cef90b-cf1d-38d4-b1fb-8423365aad68 | -3.85796 | -49.14067 | 2025-11-15 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5a0f6e6-32dc-3f60-9215-09bdabe7a04a | -4.30846 | -46.00541 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c2a288a-f505-354b-8ed2-19060a859ce3 | -6.02354 | -47.97209 | 2025-11-15 04:25:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9abeef3d-3e33-3b34-9009-508f065bf659 | -3.86075 | -49.12365 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 07d5e4d0-1da7-35fc-ab20-825f44a42055 | -5.73183 | -46.54554 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9310db03-78c7-3575-b2ab-eef2bf697adf | -4.56138 | -46.14827 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5158eaab-b0c8-3f05-8a0f-87d179c21dfa | -6.28084 | -41.76108 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7d6b5d4f-ff81-3114-9356-1405dae41583 | -9.80619 | -42.21321 | 2025-11-15 04:25:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 1fb3c2c0-f0df-30ae-ada1-213d417a0c7a | -9.02769 | -46.89091 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 281fbd41-981f-3069-beee-3d68049202f4 | -5.42785 | -43.17814 | 2025-11-15 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b52fbd0a-edf6-3f20-ba52-c32a7aab083d | -5.0536 | -44.6807 | 2025-11-15 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45e6c1bd-fc8b-3562-baab-3a403836976a | -2.15169 | -48.29211 | 2025-11-15 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac3a1b97-94e5-370b-b0bc-de2617e6d002 | -5.55193 | -46.80141 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82c13c40-136e-36e3-ad80-5578d76cb449 | -7.88206 | -48.3921 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a341814-14db-3831-bcd9-472400832495 | -9.75395 | -43.97234 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dc553d7-ca4c-38f2-ad97-c4cbb1dd3b8a | -4.46991 | -45.65056 | 2025-11-15 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d03cff17-0e78-393a-8eea-fdc0a9680d84 | -4.18975 | -51.02422 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95f40305-b37c-3f09-85d6-fa5a6afe49f9 | -10.17808 | -44.39315 | 2025-11-15 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fdf0cab-f111-307e-9503-b1499f5bb755 | -3.22543 | -45.48235 | 2025-11-15 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c0f6864c-f99b-3807-890b-1a5b37815079 | -3.01741 | -49.43675 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38d0f9a2-c3a5-363c-a95e-816fddd7ebcc | -4.82018 | -47.59921 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 17e21f05-d684-3a86-9e64-b208ff157fab | -4.64831 | -47.95036 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e91de73c-3873-3f99-a0bb-0307be622f6a | -7.33092 | -40.37167 | 2025-11-15 04:25:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da4215d0-68d9-39c5-9760-9ef3e17fa78f | -3.28074 | -45.45592 | 2025-11-15 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cc73a46-3594-3b59-9b00-dd158a8dc769 | -4.75858 | -50.68281 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cc68d91-6824-37d4-99f4-b7cb11198ae0 | -4.54164 | -43.22199 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| d5b20d9b-7304-3a27-a99d-1073f17997da | -4.5947 | -44.31678 | 2025-11-15 04:25:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef653e29-0a7d-3ca9-9ff4-3b634d06ef2c | -4.35822 | -50.78904 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb800096-2a59-3b00-9bdc-ee45304bcbb9 | -4.19046 | -43.80998 | 2025-11-15 04:25:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9aec97e-8b27-3617-bd40-11b0758344e0 | -4.75363 | -48.83141 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e9e535d-56b0-3df2-ad57-dba4764259bc | -2.71272 | -47.39911 | 2025-11-15 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58bb4e7d-ce3a-33df-a439-82025bec0053 | -5.50945 | -40.54746 | 2025-11-15 04:25:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6ae0eebb-4f00-3496-8060-95aaf3327b45 | -5.52978 | -41.76734 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f5acb553-3bff-348f-ae4c-1e9f7186b6c7 | -9.02273 | -46.87944 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed61e4fd-3bc6-3908-bea4-a0c3f96e48ca | -7.44749 | -42.76588 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c42cada9-52df-348b-82f6-cb4af3785ff6 | -3.40477 | -46.90572 | 2025-11-15 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97ad0fa1-86bf-366c-9eb4-2fdb9e606b4f | -4.40048 | -50.43711 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6708a75-c07a-3b29-8f0a-012ee2eb038d | -7.065 | -48.32251 | 2025-11-15 04:25:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f7840a0-ceee-3a27-a54c-89b267552b4f | -5.3881 | -44.8453 | 2025-11-15 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 77e83fac-db0b-32b5-837e-21adcc477aa6 | -3.14174 | -52.2658 | 2025-11-15 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8942183-6d85-3f42-afca-9266cd1487cf | -5.57284 | -47.09863 | 2025-11-15 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecefd0f2-3bc7-397f-bdbb-5a479781b87a | -8.73553 | -46.52394 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9949c33-3ba5-3765-ad70-3697902193c0 | -6.03455 | -45.81223 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaea2c9c-ddbe-3f55-99f3-7f091d114559 | -3.36325 | -49.50719 | 2025-11-15 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 900ea456-da99-3abb-9aab-0b4434ba4250 | -4.25608 | -44.19897 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 764acfef-12b0-3437-bf26-7e528ed36c3e | -4.46429 | -50.54003 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0272dd3f-005c-3e80-b9ea-3215e17bc85d | -3.52602 | -50.87631 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f5cacda-801e-3815-ab2d-c2c4938dfba8 | -3.4542 | -53.50967 | 2025-11-15 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93f6dc60-6ce2-390c-a887-4ed0c26108ec | -7.30239 | -46.19639 | 2025-11-15 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b942f63-10d3-34e1-b02d-c99f32682f7c | -5.30047 | -45.07723 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 586cf83a-bd61-31ce-a8f0-3d37710ec496 | -4.74614 | -41.57132 | 2025-11-15 04:25:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dcef53d7-396d-3ccd-ac60-fa2965f8a2c0 | -8.73079 | -45.66337 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18c3f034-f7e1-392c-a014-66755f7d21b4 | -3.22574 | -46.29813 | 2025-11-15 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ba061fa-396f-345a-b04d-a8427b994864 | -4.65676 | -45.04511 | 2025-11-15 04:25:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e12ff48b-6848-37a1-9774-37bf287e258c | -9.44547 | -44.86817 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ea7b023-63e8-3501-aa2c-d23615a50f52 | -3.23766 | -50.80457 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b9d6477-7a03-3194-8a91-a6ba9074cf08 | -8.74938 | -48.31744 | 2025-11-15 04:25:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bd33c70-3a14-3ffc-8eff-a19bb9301533 | -3.28296 | -53.82183 | 2025-11-15 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e14522f0-6a81-3add-8850-f2af74f118f3 | -4.46824 | -50.54063 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f086e8d0-7ebe-3bef-8107-5ba7c66a2835 | -4.87908 | -45.36123 | 2025-11-15 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ddadcf3-8bcb-377d-a779-beb5203de6da | -4.65246 | -46.58012 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f1bf6b0-6e1b-3fb7-a3c2-54a529d2d22f | -3.87247 | -50.77133 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f77bfea-21c9-3742-82f0-82c569b558ea | -3.65644 | -44.79639 | 2025-11-15 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 244bc2d8-c1c3-3a40-b810-84175ff595e6 | -2.71212 | -47.40283 | 2025-11-15 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README40.md)
