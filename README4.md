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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a259df0-331a-3e99-9bac-c31c229087b4 | -13.3655 | -61.3376 | 2024-11-01 00:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 69f48876-52e9-33ee-9a7d-61283695648b | -16.9012 | -57.5108 | 2024-11-01 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 0fd971cf-9fb7-3639-afa5-7ad6ad62d681 | -16.9204 | -57.5291 | 2024-11-01 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| eff24307-1b75-38bf-8a71-97ae63d6791a | -16.9207 | -57.5086 | 2024-11-01 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| ab7f877b-47af-351d-97da-c4e52a7eb785 | -17.7249 | -57.5368 | 2024-11-01 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 7f632e65-ddda-30ed-95cb-6f8e7ba28805 | -19.4874 | -56.6437 | 2024-11-01 00:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 1d2c7b99-c8d1-3586-922b-021fd3bd7a3b | -19.4878 | -56.6227 | 2024-11-01 00:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| d4230bb5-3450-3b70-9378-61c71ca42f9f | -19.4882 | -56.6017 | 2024-11-01 00:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.0 |
| ec30607c-ebd0-39e3-9a39-fafd2de9d353 | -19.5079 | -56.6199 | 2024-11-01 00:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 0aed344b-7fd1-33cb-ac20-291476d19820 | -19.5083 | -56.5989 | 2024-11-01 00:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.7 |
| c885311e-d7b9-33c7-b1c3-1e48bc4cbcbd | -19.5087 | -56.5779 | 2024-11-01 00:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 06940c28-6614-34b3-b1d8-4ba11be13dc4 | -1.2292 | -47.7516 | 2024-11-01 00:35:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 12049e03-cd69-3ad9-b554-96728271284e | -1.2292 | -47.7299 | 2024-11-01 00:35:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 0a5e1f27-a657-34f2-9f98-501bca47865d | -1.2477 | -47.7297 | 2024-11-01 00:35:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9f75c0db-db19-389e-89a7-47096781438b | -1.8471 | -52.308 | 2024-11-01 00:35:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e0593a49-9d0a-3b8c-ad88-e6b24e243d1b | -1.8654 | -52.3282 | 2024-11-01 00:35:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a922a8db-09f6-359c-9bc3-1b279db8f8d5 | -1.8654 | -52.3077 | 2024-11-01 00:35:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 9d4b9dc7-23f3-303d-af74-bd5ce5d9f19d | -2.1695 | -48.7252 | 2024-11-01 00:35:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d9e69edb-b085-3e7e-9db6-db558fb9e1c9 | -2.3545 | -48.678 | 2024-11-01 00:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 02b57c05-7885-384a-9fda-baa46f601b59 | -2.6062 | -45.5839 | 2024-11-01 00:35:21 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 323b16ee-54ad-33af-a64d-c5d81940448f | -3.0353 | -49.4901 | 2024-11-01 00:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 279.3 |
| 5dd0b986-6140-3815-b164-bd1b123b9709 | -3.0354 | -49.4688 | 2024-11-01 00:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 316.9 |
| 890b2bfe-66dd-3c5c-b2d9-64dee091864a | -3.0538 | -49.4895 | 2024-11-01 00:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 484.1 |
| 4a06b408-222f-3024-a214-e9efdd381c52 | -3.0539 | -49.4683 | 2024-11-01 00:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 551.6 |
| e23dab6e-6a9a-3038-b330-8d067e9987b1 | -3.055 | -54.1675 | 2024-11-01 00:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 96fe7008-2525-3029-9a4b-499fdb49065f | -3.0893 | -45.5672 | 2024-11-01 00:35:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9827798a-7588-357c-a26f-98483ccf99e5 | -3.1078 | -45.5665 | 2024-11-01 00:35:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 0624d1d8-c13f-39af-bb46-d568c42abb74 | -3.1281 | -54.266 | 2024-11-01 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 305d7a1a-ebe6-3580-8c54-f2d4ecdb91eb | -3.2719 | -50.3473 | 2024-11-01 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5dcb6b56-b231-3e49-8a39-c27ae53c38f7 | -3.3572 | -44.0591 | 2024-11-01 00:35:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 52e37851-bf65-394f-a99c-a2843fa03cd0 | -3.5446 | -47.3855 | 2024-11-01 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 989c0c97-64fc-3b45-8ce9-daad4fb3e56e | -3.5631 | -47.3847 | 2024-11-01 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 194.2 |
| 3bd27b11-d730-3417-80d2-fb4d419a59d5 | -3.5632 | -47.3629 | 2024-11-01 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 13f583f3-3aeb-3a1d-a707-5dfb572da659 | -3.5817 | -47.384 | 2024-11-01 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| fb50baec-fc05-343f-b08e-508db0f08aec | -3.7703 | -43.5323 | 2024-11-01 00:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 21ef8d91-02b9-31eb-b0de-5eefd93b5bdb | -3.8144 | -48.9729 | 2024-11-01 00:35:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e0cbca65-f3fb-3f18-9713-c5446e4a7402 | -4.3163 | -45.6466 | 2024-11-01 00:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 7651c59a-dc33-339f-a5d8-df255d70a510 | -4.3164 | -45.6241 | 2024-11-01 00:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 2d2c894b-0261-3cb9-b308-e63034da3ff7 | -4.3867 | -43.4757 | 2024-11-01 00:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 282.3 |
| 544c4f06-b1ca-3890-8b67-3d77bfec8a5c | -4.3869 | -43.4525 | 2024-11-01 00:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| a31cf153-39f5-38d2-b7db-312fc7cf73a8 | -4.4054 | -43.4746 | 2024-11-01 00:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 297.6 |
| 0a932d78-9331-319b-9772-bc2cd6e7ed33 | -4.4056 | -43.4514 | 2024-11-01 00:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| cebfa474-0a38-33e5-b245-9e5b2690dad2 | -4.9209 | -47.0566 | 2024-11-01 00:35:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 65b76d75-3bea-3516-a8a4-877e8f6704f1 | -4.9211 | -47.0346 | 2024-11-01 00:35:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c4204062-19b0-3e67-a722-6ef3597a4bd2 | -5.0447 | -47.9671 | 2024-11-01 00:35:35 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c85098b1-600e-3712-98fa-2cb04817ccf1 | -6.1039 | -43.9824 | 2024-11-01 00:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 053aa48e-51dc-3034-ab7d-ae12d4bb0f81 | -6.1041 | -43.9593 | 2024-11-01 00:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 10d83a31-0d5c-3cf0-8fa6-ea2cad8f0307 | -6.1043 | -43.9362 | 2024-11-01 00:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 17be76c6-05f3-3142-b974-151ab6594e81 | -6.1226 | -43.9809 | 2024-11-01 00:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 35813585-533a-38ce-896b-734fb48303a9 | -6.1229 | -43.9578 | 2024-11-01 00:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 189.9 |
| bf1cdbef-0a6a-303f-ad5d-60f76e8038b9 | -6.1231 | -43.9347 | 2024-11-01 00:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| edc9ac52-f028-34cb-a8ca-85e9c5d0dc65 | -10.0885 | -68.3828 | 2024-11-01 00:36:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 90daf154-de91-3730-a13a-d85c03b58cc3 | -10.0886 | -68.3642 | 2024-11-01 00:36:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 75d6bf94-dd87-3540-bde6-8c94fd79fc55 | -10.1071 | -68.3823 | 2024-11-01 00:36:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f98c9c51-9c51-3c66-a541-16fb1ec6f905 | -10.1072 | -68.3638 | 2024-11-01 00:36:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 227dfddf-6c5e-39a3-9968-bf2b5cb49b73 | -10.6819 | -65.002 | 2024-11-01 00:36:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 5d871032-f950-33f1-8ef0-9005f43ec33d | -10.682 | -64.9831 | 2024-11-01 00:36:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e6504d8d-5190-39fb-aeb0-5373724b448f | -10.9808 | -45.1335 | 2024-11-01 00:36:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 7a64fdd5-cb43-31f7-9790-44462b1b1480 | -10.9811 | -45.1104 | 2024-11-01 00:36:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 34103768-a23f-39db-9d30-e40410df5b86 | -11.0003 | -45.1078 | 2024-11-01 00:36:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| ea0385c7-5385-31e0-a1c0-c0a1dcdb765e | -16.9012 | -57.5108 | 2024-11-01 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| f190364a-2851-303a-8af5-13265e50c78f | -16.9204 | -57.5291 | 2024-11-01 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| adb34b95-2cce-3496-a0ce-bac742e606c1 | -16.9207 | -57.5086 | 2024-11-01 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 66dc767c-9c2d-3724-a0c3-23378768b7ce | -19.4878 | -56.6227 | 2024-11-01 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 0ca4569d-0eed-30b7-8517-c9dc07a16e6c | -19.4882 | -56.6017 | 2024-11-01 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| b235c273-fae9-34ca-9288-3f83e70d960d | -19.5059 | -56.7249 | 2024-11-01 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| fc0abaa6-4b4d-357a-9d3d-8183274dac1e | -19.5063 | -56.7039 | 2024-11-01 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 249f1e9b-20b3-34c5-806c-0aa8c3a52329 | -19.5079 | -56.6199 | 2024-11-01 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| d86e16ec-8e79-3e58-b24a-de8ef179a9d2 | -19.5083 | -56.5989 | 2024-11-01 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 9d56f6fb-a7d3-3daf-8ce8-b754af8c635f | -19.526 | -56.7221 | 2024-11-01 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| c97820a8-d8ec-3e68-bb25-348314f7f5c2 | -19.5264 | -56.7011 | 2024-11-01 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.2 |
| d074a523-6344-3d4d-9182-cdadad6caef5 | -1.2292 | -47.7516 | 2024-11-01 00:45:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 65b06919-946b-3b77-81f6-314c9baef602 | -1.2292 | -47.7299 | 2024-11-01 00:45:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1c99bfca-302b-30a8-8916-3a362f7bc372 | -1.8471 | -52.308 | 2024-11-01 00:45:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| ed35051e-c670-3d71-86d3-1022c1796f44 | -1.8654 | -52.3077 | 2024-11-01 00:45:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 4712574a-a51d-3f9c-bc63-7d3639c7f68d | -2.1695 | -48.7252 | 2024-11-01 00:45:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0eafeba2-090e-3866-b70f-62a863221f41 | -2.3545 | -48.678 | 2024-11-01 00:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f889f580-50b6-3700-af74-e7c3e8fa1278 | -3.0354 | -49.4688 | 2024-11-01 00:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 301.9 |
| 80671794-25fc-3fa2-b13e-020c145eb970 | -3.0353 | -49.4901 | 2024-11-01 00:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 266.0 |
| c905d7b4-bba0-35dc-83c8-bf106f052f63 | -3.0538 | -49.4895 | 2024-11-01 00:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 451.0 |
| da07d77d-b662-3a10-b388-1bfe7ca5bd62 | -3.0539 | -49.4683 | 2024-11-01 00:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 492.7 |
| 2abac788-eb6e-36ee-a534-998e45860a66 | -3.055 | -54.1675 | 2024-11-01 00:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a6ed35db-8f9e-3b20-9390-91a503c4eaad | -3.2719 | -50.3473 | 2024-11-01 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 219a12d4-de86-372f-9e8e-b4ca30482dec | -3.5446 | -47.3855 | 2024-11-01 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 56224811-5255-354c-86cc-82478e18832a | -3.5631 | -47.3847 | 2024-11-01 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 221.9 |
| d37d4d2a-4d11-36ac-a9c9-64893a02f95f | -3.5632 | -47.3629 | 2024-11-01 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 8a94dddb-d88c-37e4-9862-e06b116cefce | -3.5817 | -47.384 | 2024-11-01 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d8b2b37a-f630-3ff8-bdb9-488a3fe60e8b | -3.7703 | -43.5323 | 2024-11-01 00:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 09eb41c6-7277-3fb9-9805-47fbaef4b432 | -4.3163 | -45.6466 | 2024-11-01 00:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 773dba04-d3af-321c-be12-8ad5bcd528af | -4.3164 | -45.6241 | 2024-11-01 00:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 023d2788-f040-3ab4-85f8-0082475eaac9 | -4.3866 | -43.4989 | 2024-11-01 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 4f1ce38a-820d-3571-bb97-67385724e5dd | -4.3867 | -43.4757 | 2024-11-01 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 541.7 |
| f3b6fe4d-c1ac-346e-9fe1-85eec57c1ab5 | -4.3869 | -43.4525 | 2024-11-01 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 182.5 |
| e2121882-f416-3b50-a25d-e05f7a10094d | -4.4053 | -43.4978 | 2024-11-01 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 29a8dae7-986c-3ff2-a0f8-df5f6ee3c0c1 | -4.4054 | -43.4746 | 2024-11-01 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 411.0 |
| 27a32b29-90a2-3a8a-8309-f7c778d123b0 | -4.4056 | -43.4514 | 2024-11-01 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 4db07868-a7f9-341a-a9bb-b847d79bb7b4 | -4.4369 | -44.3259 | 2024-11-01 00:45:31 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5e68e083-44ba-33ef-b7c9-dc45a1d716b7 | -4.4554 | -44.3477 | 2024-11-01 00:45:31 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| dddaf938-cbb7-3be0-96ed-f877ee11ef75 | -4.4555 | -44.3248 | 2024-11-01 00:45:31 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 238.7 |
| c75f3b67-2671-3dc3-a5a8-ebf5c4d7fe41 | -4.9023 | -47.0577 | 2024-11-01 00:45:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |


[Clique aqui para ver as próximas entradas](README5.md)
