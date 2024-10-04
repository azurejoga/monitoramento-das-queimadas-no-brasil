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
| d7ec801c-4bac-3725-bd7f-65c8eb636cb4 | -12.8238 | -62.4959 | 2024-10-04 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ce07ca83-cf0c-343c-b64c-b784306e2749 | -12.824 | -62.4766 | 2024-10-04 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 19418ea4-4915-30b6-ba30-68e684a1646d | -12.9831 | -51.129 | 2024-10-04 00:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 1b4e3af3-87d2-3d16-bed1-a24ff39bee1a | -13.0594 | -51.1409 | 2024-10-04 00:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| ad814161-0e20-3c48-98a5-f987d27915e1 | -13.0598 | -51.1195 | 2024-10-04 00:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 4fd8728e-5a7d-3eb4-a4ff-07d80700f708 | -13.0786 | -51.1385 | 2024-10-04 00:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 4e01d9da-434e-3387-8c79-697630d3588b | -13.079 | -51.1171 | 2024-10-04 00:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9d791942-b5d8-395d-9e5b-3042372eb7ef | -13.0975 | -51.1575 | 2024-10-04 00:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 3849128a-536d-3c4e-8444-f353aedb2beb | -13.3976 | -61.957 | 2024-10-04 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| cf42b6a1-b4b1-3c5a-aee2-d599a3ae7eb4 | -13.9845 | -44.0236 | 2024-10-04 00:46:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 6b2aa519-5203-330e-a364-b0d4ba9a5813 | -14.004 | -44.0201 | 2024-10-04 00:46:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 5739a2a5-03e8-3a20-8095-a8a77b07b5ac | -14.7944 | -48.005 | 2024-10-04 00:46:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 9e77bd6d-24f6-3add-a121-a32ead3bf0af | -14.7939 | -48.0275 | 2024-10-04 00:46:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 146.4 |
| bd9dd070-c317-3e89-ab40-e29725da3e0e | -14.8134 | -48.0243 | 2024-10-04 00:46:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 39884e9e-ac0a-36df-8ba3-f0ad78d047b3 | -15.748 | -49.9586 | 2024-10-04 00:46:34 | GOES-16 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 101.5 |
| eaebec41-320d-3047-993c-28d6a8f79d76 | -15.7676 | -49.9555 | 2024-10-04 00:46:34 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 131.3 |
| e3c5a254-5b13-3ba8-ad4e-037fbfc56ccf | -16.0732 | -50.3014 | 2024-10-04 00:46:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 553d00fb-1ffb-3149-80db-53fad22fef64 | -16.1094 | -50.4489 | 2024-10-04 00:46:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 492c5c10-accb-33e9-8e4d-17d27ce4aaee | -16.1098 | -50.427 | 2024-10-04 00:46:36 | GOES-16 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2425008a-cf58-397b-a5f5-3fc540514fc9 | -16.4148 | -57.4028 | 2024-10-04 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| b2782851-3808-3a18-a2cd-68f83278d82d | -16.4151 | -57.3823 | 2024-10-04 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 4ffc0275-c386-30a2-8922-1d452aa75a96 | -16.4554 | -57.2962 | 2024-10-04 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 2b208e5b-d261-393c-a22f-3424aa2c5842 | -16.5935 | -57.1988 | 2024-10-04 00:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 8166112c-75a1-3c3a-b154-5ef8fb399e83 | -16.5938 | -57.1783 | 2024-10-04 00:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |
| 404042c6-adf3-35ed-a060-1d96ed6231f3 | -16.9302 | -47.1224 | 2024-10-04 00:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2a16ec4a-a7ea-3f8d-a9e7-3197c27754ce | -16.613 | -57.1965 | 2024-10-04 00:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| f7243b56-1cd2-36c3-8193-00d5d4e44bce | -16.6133 | -57.176 | 2024-10-04 00:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| b26c2bd7-1938-38a4-94ae-62a2b62388d0 | -16.7606 | -57.7512 | 2024-10-04 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.0 |
| 5e750409-0f10-31f4-8a50-d0b487f2d057 | -16.7663 | -57.3833 | 2024-10-04 00:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 0002fee3-075e-3910-b737-495baf29c98f | -16.779 | -57.8306 | 2024-10-04 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| b522a89b-5620-3b7f-b068-5dafe352e53c | -16.7849 | -57.4425 | 2024-10-04 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 3a78dfb0-c821-3d0b-9c8c-3144839921c4 | -16.7856 | -57.4015 | 2024-10-04 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 20a0f41a-3960-3e52-b74b-02d9d1d4c804 | -16.7859 | -57.3811 | 2024-10-04 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 170.8 |
| 56893f6d-8966-3e44-a360-e5c4a6303e0d | -16.7985 | -57.8284 | 2024-10-04 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| a4a2e378-84f8-3ddb-8eab-33efcc30b89c | -16.8055 | -57.3788 | 2024-10-04 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.3 |
| 6543d5a8-d593-3932-9787-fa99012bfe17 | -16.843 | -57.4767 | 2024-10-04 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 14f7602c-ec54-3f41-8cdc-7c19513dd345 | -16.8433 | -57.4562 | 2024-10-04 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 32f626d1-0cee-31ea-919a-33127468abbe | -16.9087 | -55.843 | 2024-10-04 00:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 517766d3-6c3c-3d3e-9802-1c341b3682c0 | -16.9283 | -55.8405 | 2024-10-04 00:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 2645dd7d-017a-34fb-a7b9-7bd9700b3c25 | -16.9287 | -55.8197 | 2024-10-04 00:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 299f6021-acce-30be-97c1-886e1f3ba7e4 | -17.3844 | -42.6235 | 2024-10-04 00:46:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| f5363f6a-d06f-34ab-9977-f0f00bf88de2 | -17.8383 | -40.1059 | 2024-10-04 00:46:44 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 117.0 |
| ec4bbff5-a1fd-3714-85c5-1c55d3548d98 | -18.8413 | -42.8985 | 2024-10-04 00:46:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.7 |
| 6c851b0d-cd64-3ce3-b640-f62dc2f0c991 | -18.8609 | -42.9182 | 2024-10-04 00:46:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| 0d1caec7-2e48-3a8c-969a-9ab6a3662314 | -18.8617 | -42.8932 | 2024-10-04 00:46:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.0 |
| 7a106ed0-a37c-332b-8f28-b12dcd7fb1d0 | -18.8613 | -43.5837 | 2024-10-04 00:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.6 |
| 0836e392-4a33-3c02-8598-e984b6319ac0 | -18.862 | -43.559 | 2024-10-04 00:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| 00f7f76c-0cc2-380e-b5a5-c13cc54e29f3 | -18.8816 | -43.5785 | 2024-10-04 00:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 5dc4e1ed-0e2e-3d4a-9370-8fc6dd3867d1 | -19.4899 | -42.8746 | 2024-10-04 00:46:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| 582ca229-6334-3676-8c61-8622f2914f7e | -19.5104 | -42.8691 | 2024-10-04 00:46:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.9 |
| f248039e-87c4-3b10-85f6-9189cd67dcef | -19.9901 | -48.7144 | 2024-10-04 00:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9d2feff5-6f33-3633-bdfd-068830ad3b98 | -19.9907 | -48.6913 | 2024-10-04 00:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 021d3d4d-3940-3628-a47f-f5d67058c0f0 | -20.0104 | -48.71 | 2024-10-04 00:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 08874958-a5c4-3db2-9335-64cb5a635e2f | -20.0111 | -48.6869 | 2024-10-04 00:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 7d3f09a1-8c58-3a51-a810-30c34e1d1ccf | -20.4591 | -43.1795 | 2024-10-04 00:46:58 | GOES-16 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.2 |
| 91ba8a93-8295-3642-905e-d284753407e3 | -20.4797 | -43.1736 | 2024-10-04 00:46:58 | GOES-16 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| 5d8e4050-1b67-3a54-882a-7ea29d5d9cd3 | -21.3334 | -48.8044 | 2024-10-04 00:47:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 9bd02c1e-f414-3c92-beb5-8c91aa71bc26 | -21.3541 | -48.7996 | 2024-10-04 00:47:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.9 |
| 925643fa-b3cd-3f8b-aa5c-97083b47155d | -21.5684 | -48.4942 | 2024-10-04 00:47:05 | GOES-16 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 89.0 |
| df47a46d-e6f7-3126-bdb9-4e989603e782 | 2.3198 | -50.904099 | 2024-10-04 00:47:05 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1896a1ef-5e7e-3b61-835a-cb9f8a82b888 | 2.3182 | -50.911098 | 2024-10-04 00:47:05 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d9e24e60-1838-3c88-a0c8-c3f0878d6ade | -21.7981 | -48.3926 | 2024-10-04 00:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 83a5ce17-191d-344c-a276-efd96062dca1 | -21.7988 | -48.3691 | 2024-10-04 00:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 1f61fa11-e7eb-396d-aacb-0073a05cc208 | -21.8079 | -48.7626 | 2024-10-04 00:47:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 81.0 |
| bc15c2cd-77ac-3303-bc8d-1d866719ed6a | -21.8175 | -48.4346 | 2024-10-04 00:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 63334689-3051-3d35-a7ed-a22de5622d2b | -21.8196 | -48.3641 | 2024-10-04 00:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1cb6408a-382a-37bd-b3f5-f498bc35c79e | -21.8383 | -48.4296 | 2024-10-04 00:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 03f00b0f-f7c7-335a-9fb2-92ef43be536a | -21.8591 | -48.4245 | 2024-10-04 00:47:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 5fc0e588-69cf-3d3e-9ad4-334414323a4c | 3.2319 | -51.198299 | 2024-10-04 00:47:21 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 09e4ea79-2e15-3e78-9ee1-1d49a12d8e63 | 3.2302 | -51.205299 | 2024-10-04 00:47:21 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 73e8ba66-6970-3695-a332-c5ff71f244e2 | -3.2349 | -50.3695 | 2024-10-04 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 464d8bf5-f157-33cf-80d3-a12813dcc7fe | -3.2534 | -50.3689 | 2024-10-04 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 30a523a2-aa31-3a67-8177-2fc289a9d48d | -3.2899 | -50.4725 | 2024-10-04 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 3842191d-4534-3795-b616-8bbfd32bfe2f | -3.2899 | -50.4516 | 2024-10-04 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 264.9 |
| dc4b4151-0143-3fd9-b7b7-93d04021b231 | -3.29 | -50.4306 | 2024-10-04 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3cbcea73-ea41-31d7-8195-7ca88ffb8779 | -3.3083 | -50.4719 | 2024-10-04 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| e32567a3-59ca-3dd0-9eab-8b5921428101 | -3.3084 | -50.451 | 2024-10-04 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 189.5 |
| c1ada2a9-b77c-3c1e-92de-5ebd2482ccff | -3.3085 | -50.43 | 2024-10-04 00:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 38e1be6f-0aa2-321a-817c-4982b0253c70 | -3.4915 | -50.8004 | 2024-10-04 00:55:26 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 07b1138d-04e5-3b81-bb3e-9ba50e175470 | -4.0949 | -48.4894 | 2024-10-04 00:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 5846bef5-3369-3f2b-acb7-2cfba85c4590 | -4.4657 | -42.8877 | 2024-10-04 00:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 6dd941f8-a2a2-33b0-b213-19d7cbd8e3fc | -4.5375 | -43.304 | 2024-10-04 00:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| add13748-f887-31c3-9cb9-3092558c4aff | -4.5949 | -45.7436 | 2024-10-04 00:55:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 38.4 |
| cdbec56a-26f1-3b8b-b034-3a8766637b5f | -4.6684 | -45.8961 | 2024-10-04 00:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| c2660988-e26b-30d5-b2c2-a95ac4352280 | -4.6686 | -45.8738 | 2024-10-04 00:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 111.6 |
| e9039f2b-5d51-3c9b-82f7-a86899c2adef | -4.687 | -45.8951 | 2024-10-04 00:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ddacb74b-c522-3225-9672-fae16e7fae00 | -4.6872 | -45.8727 | 2024-10-04 00:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 312a4bf8-2fc9-31f7-b2a6-d1faca2ade7f | -4.6873 | -45.8504 | 2024-10-04 00:55:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 26f43d48-28e7-3efc-92b6-31455b75aee7 | -5.5033 | -48.8046 | 2024-10-04 00:55:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 68f35744-295b-3895-a62a-8436aa2528b4 | -5.5218 | -48.8035 | 2024-10-04 00:55:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| dd19d57b-9296-3719-a80a-cf5fd64df717 | -5.8214 | -44.1426 | 2024-10-04 00:55:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| e86bbbe3-fdda-3744-b6bb-3b38db78b45a | -5.8216 | -44.1196 | 2024-10-04 00:55:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 4e9c4702-1ba6-3701-8e62-116b522bd632 | -6.2524 | -44.132 | 2024-10-04 00:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| f2692bdf-9c8e-3845-af44-28ea93e0a825 | -7.3821 | -72.9355 | 2024-10-04 00:55:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 8daaeb06-131e-3c0a-9329-c043702a0623 | -7.8539 | -45.3611 | 2024-10-04 00:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b6dc0872-fedb-3ca5-be07-11c9fb4f42d6 | -7.8541 | -45.3384 | 2024-10-04 00:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| a9644c60-617b-3eb9-a6aa-1bc74bd21f11 | -7.8164 | -50.543 | 2024-10-04 00:55:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 20c8f4c0-e45b-3c63-a45a-1568cd38dcb7 | -7.8166 | -50.5219 | 2024-10-04 00:55:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4556b8e3-18c8-39bb-939c-e41b05654b51 | -7.8351 | -50.5416 | 2024-10-04 00:55:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 484253f8-dd9e-336d-9bad-3533bd1ef00e | -7.8353 | -50.5204 | 2024-10-04 00:55:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |


[Clique aqui para ver as próximas entradas](README20.md)
