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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c5f1c82-7473-3ff5-b68d-93da8f85c578 | -0.97624 | -51.7121 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b64f74e-f1d4-347e-ac4b-cc312ee8c9e2 | -3.93966 | -48.14769 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81a38e1d-b10c-3209-9d12-b374607118e6 | -1.29467 | -51.73176 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 46f49d0e-cb7b-3830-bcf6-c0472e0019b0 | -3.96028 | -49.95471 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cda2295-833c-3197-b04b-f69a7ea07960 | -1.35842 | -54.6561 | 2024-11-25 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e98b802c-2ad4-3fee-8571-679bcafece9f | -4.72452 | -50.83447 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 775df35d-9dce-343d-9f69-f44860f28e03 | -3.03456 | -54.02244 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99486801-1d0d-392e-a326-949e6a2cf7cf | -3.87869 | -52.35751 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e01c73e6-9499-38da-9c5f-a13dda7890d3 | -2.63054 | -51.76778 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b8296c1-e822-3e4a-b91a-6ab168b435f9 | -2.82155 | -51.7972 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70698274-a776-308f-8c7c-eda48c5c5d7b | -2.92763 | -53.07078 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7776893a-b7a6-3b27-be1b-e9c5d7b7e7cb | -3.61141 | -54.74374 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2344049b-7808-3c45-b63c-2a77efe0dbba | -1.69015 | -52.61213 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e9437a0-ef8f-328a-84fb-1fd8252c95b8 | -2.77084 | -54.04514 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dc55136-e11e-38c6-a304-9a4668410d30 | -1.73894 | -52.79707 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b225d1a2-edc8-36fb-becb-a73b892137ff | -0.28137 | -51.51764 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32fdb901-0a5a-306e-921e-991d4566a565 | -1.44377 | -53.40372 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16bfba6b-a1ac-3244-a7e8-646a04af2585 | -3.14213 | -53.91813 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a4429b8-5bb6-3608-9c15-81b55b4055d3 | -4.62708 | -50.54773 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a954009-6e60-3359-85c3-4ca4b4625b58 | -3.28497 | -54.11138 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f362ebb9-d608-3838-9c02-c0bfe525c9f1 | -1.29131 | -51.73124 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce935cb8-2d98-3468-a53f-e82d30046c0a | -3.61714 | -52.20406 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4c83e7c-e994-313f-9c93-57e2f9675a04 | -2.84711 | -53.98917 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0800cf7f-a248-3086-a757-8a44c8951861 | -1.38971 | -52.32824 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 783e27f3-6f7e-35fb-8de6-0b166d0689df | -1.13264 | -53.65714 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac283adf-1570-3587-a25b-0d805cea35e9 | -2.33911 | -52.18198 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73ed36fc-1139-3eeb-b654-cde0d2557748 | -2.8139 | -54.09115 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5182fbae-21af-3e23-b2e3-a4cdbc473f55 | -4.37618 | -48.49969 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46d8ce44-209e-3556-8ef4-3b278e185137 | -3.96967 | -49.94273 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9eb37965-fea4-3f80-8d5a-4d2cb0244c7b | -2.46288 | -53.70127 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f817a9a6-2e57-3df2-8958-3fde9ca9b00c | -3.28689 | -53.66763 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 108f296a-9335-329c-921d-e3f10f361ff0 | -3.37758 | -54.67819 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd380939-7952-3492-8edf-00b7f69ad8d1 | -3.89433 | -52.3017 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83793ee3-38b0-3431-8b13-3d3b1078a138 | -3.05963 | -53.21898 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9bac3e22-d907-3eeb-a5fe-fe0b22555bc2 | -4.69303 | -47.18325 | 2024-11-25 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30c06640-2481-3f9e-b210-5dba5160db4b | -1.23472 | -51.74063 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0d618d9-0af6-38f6-8aae-f8ce0d2d6559 | -1.29019 | -51.73833 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f7e9abd-3628-3632-b0a1-c5def6d1d06b | -0.91683 | -51.65211 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ff68a7f-477a-3c31-bc19-dd5cf8a75b9e | -2.69146 | -52.44435 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c9ce454-1d5c-365a-ba35-478132d982fd | -1.13932 | -53.65815 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d55108a-d948-35da-8d0c-83c959f5a29f | -1.14274 | -51.67932 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd10c7b4-97d1-39f3-8b2c-b5e7be0c2d98 | -0.95105 | -51.71906 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb49c5b0-551d-3575-a25d-a7580c0c443f | -4.24157 | -48.69923 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0adde0e5-8a51-39ec-a5fb-0fcf0fb3e2b3 | -1.22529 | -51.80075 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a570f813-25be-333e-b2f9-b2f2102ab93e | -0.04543 | -53.25601 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c27cbc8-ccb2-3a71-ae44-03d2c93fe219 | -2.99884 | -52.51008 | 2024-11-25 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8ac5ae2-ca4b-3996-80b5-9532d02a8106 | -1.15768 | -53.67166 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aca02a0a-02d6-3b9f-a7c3-31ef23bb8912 | -2.8477 | -54.00711 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d1c3bc5-d14a-33f3-acec-7ebf1cd70d03 | 0.845 | -51.8381 | 2024-11-25 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 740d03a7-eeaf-3ee6-bd6a-a5760305f090 | -1.47533 | -51.95883 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3093b1cd-a7e7-3757-8fd5-ac31aa01fcb3 | -2.82226 | -54.1032 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e41a028-8604-3d40-bb94-e684c2c7c1d8 | -3.16702 | -51.09879 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 245f10c6-0126-307e-bcfe-28bc176cb673 | -1.38081 | -52.31975 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9181a09-007c-3efa-9de0-42dc2f6fb300 | -2.58883 | -51.72119 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9943753e-f5ab-32f4-a327-1ac591b6bf67 | -1.1128 | -53.39765 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6aa9d6f-83a1-3f09-9e18-cd1a33bd3ab8 | -1.54911 | -52.58336 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a6d80b1b-4a4a-3681-852c-8f42de579904 | -0.81811 | -51.61475 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 897256b3-809e-3813-88d3-18f62580916b | -3.51951 | -53.82481 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e4af574-7c23-3000-9101-9c88bf07f178 | -1.39501 | -55.205 | 2024-11-25 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f02cd031-dd1e-30ca-b2cc-8584ba0eefe8 | -2.92508 | -54.33179 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5b05575-ae82-3a21-849a-c22a17ecbf61 | -0.92186 | -51.64199 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68a6fc10-26c5-3d56-a32c-666927c25003 | -0.96616 | -51.71054 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7d3aef7-a8d2-3c2e-9ff8-55870afff971 | -2.76589 | -54.07655 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b1795d9-4e07-354c-b96f-798ae20bee81 | -1.59231 | -52.59007 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2e07baa-13df-3a91-81a2-aa761c6e800c | -3.55015 | -51.51002 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d682d8d6-3bf1-3543-b223-07f8331795c9 | -2.82665 | -54.05381 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15f8b6f7-60f3-34fa-b9f3-616e80adadd7 | -1.63788 | -52.10587 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8c1ea9b-fde3-35ac-a358-7ce76f57eda6 | -0.27591 | -51.61816 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e538a3ef-9faa-3b78-95fc-61092aa9d585 | -2.17292 | -53.77707 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e32d274e-4a4b-303c-8e69-9eb901f4b2e7 | -1.77056 | -53.62514 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2685d107-728f-3804-8044-b31671895097 | -2.85546 | -54.00119 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 549ec23c-51d0-3fc4-9760-5a5beaff5198 | -0.74504 | -51.94951 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db8c4afc-0c67-3a05-90a1-711b5f320a5d | -1.07171 | -53.35586 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 539108d2-f5e1-39b3-9f19-8d4c7e9c7da0 | -3.86917 | -52.35239 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2d7077b-28f2-362f-b63e-f3dd019e0e2f | -4.84091 | -50.80511 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e27c5254-1e06-318c-97a4-ddad618d99d0 | -1.36542 | -53.8364 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a435958-9d09-35c0-8b99-0cbdf90a48f8 | -3.68439 | -47.12601 | 2024-11-25 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aebf551f-e1bd-335d-a154-5674bd91e94c | -1.36597 | -53.8329 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f92ffe20-1a57-382c-bd73-6f0601b3f10a | -0.79623 | -51.60045 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd4740bd-e057-3238-87c2-4c354d0c044e | -2.79139 | -48.56468 | 2024-11-25 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4439feda-aee6-39a6-9952-674292b42bc6 | -2.17622 | -52.08079 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f63bae44-689f-3854-b7ed-2702fd6664a6 | -1.38469 | -55.17997 | 2024-11-25 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fba208a7-6728-347d-a479-8d7d2e79bb45 | -2.82783 | -54.11124 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b636e2b9-b8be-3ed2-a2f7-7940c003f34c | -3.63799 | -52.24741 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fee8d768-fbdf-382a-9437-132311495911 | -1.72113 | -52.75897 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e56490f-54d8-336b-b6c3-2979cc00e3e9 | -2.78177 | -52.87848 | 2024-11-25 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42b0f801-65b7-359c-b8cf-a29999c689ba | -2.64064 | -54.28334 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15e4b9b0-3aa2-331c-bacd-9a6d51cd0f79 | -2.76366 | -54.06904 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dda34540-c413-3668-a14e-a63c92fa598f | -3.55359 | -51.51054 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1820aa7c-1eb3-3f46-a595-47c560b9ff97 | -1.24094 | -51.7887 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b03a0e2b-a29e-38a6-a8ce-5512ae14e3ad | -2.27016 | -51.23458 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 830018af-3ca4-3305-9c4f-5e71b76ea4d0 | -2.79997 | -54.07109 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcecb8ab-267c-3acc-8b1a-d8442728083a | -2.78827 | -54.03709 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aa811a8-4621-3694-9536-95a93ec48434 | -2.98616 | -53.4265 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8537cce6-3a45-32e3-a602-1ed918cd117e | -1.22127 | -51.73854 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb638d0f-413b-39e9-89e2-e11fe2a06083 | -3.55186 | -51.52168 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4863292f-c993-3929-9c02-25799fda2844 | -1.62484 | -52.44249 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ec6eda6d-aeae-3e41-9ec5-e21d06a8806b | -2.32268 | -51.30332 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 349c264f-e518-3a7f-9012-43d602653816 | -0.36775 | -51.54896 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7f56532-0626-3834-8514-5b59a4f44c01 | -1.69348 | -52.61265 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README34.md)
