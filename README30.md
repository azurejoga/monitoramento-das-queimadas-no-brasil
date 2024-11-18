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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12b1993b-a0bc-3ad7-bf2d-93d05b25563f | -2.37476 | -53.6831 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c07a4042-8be9-35bf-9186-7538c377a147 | -3.39891 | -50.28737 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5b5d0088-e2a9-322e-bd69-60edc2e6131a | -1.77013 | -50.74792 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b4a9dee-6281-3fcb-ab3d-d0edd70d9ea3 | -2.72321 | -51.81117 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9853e4f8-6328-3b03-a8cf-0a7aa7d075ca | -1.32318 | -51.86989 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67124d58-f748-3351-8982-4ff36bfd61d3 | -2.3429 | -54.59279 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd5be088-2b6d-30d6-9986-90511ff312a2 | -3.45768 | -50.01222 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa9ef8c7-08eb-3ab1-a4de-582105f483bc | -2.69837 | -49.28749 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97b18f11-196b-3e81-83b7-5389b29ee263 | -1.81529 | -46.53615 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5aef9c3c-24dc-372d-ba16-34d9ac297823 | -2.68024 | -52.44173 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3100430c-bb43-3bdb-956b-83de5b23a93e | 2.24006 | -55.82743 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e494e41-bc29-3669-b7c9-22e1f0ae3d63 | -1.33248 | -51.87384 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5606bee2-a491-3ffe-a8d5-938bdcd4e3ef | -2.54524 | -54.3191 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e6e598a-0a80-3133-bb08-9d6baaa93bb0 | -1.32803 | -51.86234 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 748affa7-9887-3f28-9a23-73de6a666267 | -1.62684 | -55.14888 | 2024-11-18 05:03:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a53318ad-e6bc-3c8e-8c5b-c91711ca89ea | -1.17441 | -49.14114 | 2024-11-18 05:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e785d6e-f8c6-3a13-b578-fd4f3b0c8e91 | -3.53265 | -50.25626 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62db9935-abff-3bd8-b397-e807c76001ff | -2.58398 | -51.71764 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ac93fe52-73ca-33d3-af37-5ef23f4fe03f | -1.13702 | -54.10093 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be31c5d6-8019-394d-a3bc-a362c7de9f5c | -3.16431 | -46.59942 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62b519d6-a0d4-3095-beb9-12e5972199c7 | -3.32649 | -53.19447 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d44f65d1-32da-381a-89cd-fd51403746cd | -1.06514 | -52.38975 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 115663f4-6544-3788-82e4-009ee56f0eca | -2.9668 | -53.86174 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80084e7b-d75f-36f2-bfa2-cb88f809bc81 | -3.37281 | -53.32754 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7277b7eb-5ffb-31c3-8f83-7f9f9f8b5345 | -3.49108 | -53.98944 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38696982-484d-396c-ba9f-ac04dafe6e7b | -3.52938 | -50.25494 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3337270-2fe0-3dbc-9b46-363c70491544 | -3.33766 | -50.50208 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 99291e81-f2b7-3ab0-9aed-049d3f692b27 | -3.56741 | -50.24991 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62eb503c-c3cf-339a-b58d-0d2cf3be818e | -3.71063 | -53.75359 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2bbaa31a-59d5-3b6e-b6d1-980c22115317 | -1.60473 | -52.5082 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c072919a-6c88-38a3-82e3-d94bc5a963b8 | -3.18201 | -53.24574 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ee2c2bf8-00c9-34a1-8838-e2198962821f | -4.27093 | -50.58915 | 2024-11-18 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 730c7828-2dd6-3d1c-b0c6-3d36e9b65470 | -3.19037 | -53.2355 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d9e6209-6fe0-3d4d-9968-d355ef379c38 | -3.10934 | -53.10021 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 43c00836-8e81-35fb-bfdc-c4bd7d81a718 | 0.9689 | -51.13882 | 2024-11-18 05:03:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f6beda6-c9b1-3880-8cd8-f90083c6b297 | -1.63309 | -53.29827 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cac4e779-1881-3a51-ac5e-4d08425277c5 | -1.17079 | -49.10867 | 2024-11-18 05:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d228b5e-74eb-3973-96ce-87f1178f2cf8 | -4.27144 | -50.58569 | 2024-11-18 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5b32664b-bbf8-32c1-a645-6fab88d8a2e6 | -2.85155 | -54.00758 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31190c7e-fc65-3775-8fcb-d477aa8586ec | -3.56388 | -50.24578 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d141ca82-f6d8-36a6-89b2-fde0e5ec2074 | -1.44188 | -53.38315 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e7a14648-6f44-39dd-9e6f-6d26df160d33 | -1.44832 | -52.68017 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a1c7faa-9523-3a00-a7a2-adbb656bc9b9 | -3.07092 | -53.28262 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 93649983-69a4-3655-a2ca-bd070e43b8be | -2.58763 | -51.7182 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e7a5120d-2706-34c4-a458-0c1f8a53baa4 | -3.61558 | -50.15044 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe4b2b28-f3de-39ae-9d25-1ae5c1db6e4f | -3.67001 | -54.65348 | 2024-11-18 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a423d5de-9226-37f2-8fbb-521e33a9ce1d | -4.78666 | -46.48069 | 2024-11-18 05:03:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8470006d-ae7a-3d8e-8f8d-3f0347d35fe5 | -3.58805 | -50.52193 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e7ea714-01dd-37b4-b69e-a51377badece | -1.33853 | -51.85812 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10d7df6e-74fc-3a2e-904e-c312dc928d11 | -2.68123 | -52.98656 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 566234cf-b640-3a6a-806b-621e6f457db5 | -3.37453 | -53.31646 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c40fa7e5-ab9a-3a69-b4dc-67de61930658 | -2.61496 | -54.32985 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 911e5e09-7f1a-3edf-ac65-8626bdf3f0b1 | -1.43574 | -55.23818 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3a4493d-2181-36fd-9900-eb4ebccfc378 | -3.18637 | -53.23873 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d121c81-9b42-3572-8d82-484d2de2f26a | -3.57959 | -50.25164 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0732314e-3097-36df-b747-b3e63c4c8388 | -2.54068 | -54.28278 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e86e7e-4f69-3193-aa27-028c3f41ae47 | -1.90166 | -46.44792 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56a6c339-feaf-36ad-b4ab-13efb6ae6967 | -2.29657 | -49.13129 | 2024-11-18 05:03:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f269f522-776d-3388-9ba7-742221957aaa | -2.62774 | -46.83523 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ef1f91db-68ed-3261-803c-a67c849ac1ab | -2.23496 | -53.6036 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd59d1c3-4ab8-37e0-924f-62d02a45d3bf | -3.36864 | -46.12819 | 2024-11-18 05:03:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87553a6f-00f1-386d-a521-1077fc4dd08e | -0.93129 | -51.64263 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b9e676b-1c67-35ee-b679-b09e3ec418fb | -0.93333 | -51.6412 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d73bceb7-572b-3309-8016-090f14e78a83 | -2.8693 | -51.78681 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f6c65706-2047-3218-b6ee-5010a419b130 | -2.2985 | -49.12914 | 2024-11-18 05:03:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 273bdfd5-caed-3e8b-ac18-5c6c9a0daa14 | -3.37566 | -53.33177 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56f3c351-7b36-34f4-9733-bec07e666c37 | -2.59636 | -48.30255 | 2024-11-18 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05857b9d-68dc-370c-9472-9c57013b2b0e | -0.92973 | -51.64066 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1ad4cf6-c481-3169-8d64-03887f3ff621 | -1.60913 | -52.40993 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41ecadee-c3b9-3ea0-864f-fcfffdc4e551 | -3.7718 | -50.16238 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d9286b9f-4ef7-33be-8059-22e1795c49b3 | -2.59129 | -51.71876 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d1e959a-5f3e-3782-807b-da40bdfb16fe | -1.14085 | -51.69294 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f745077-b7f9-3b2b-a8c4-3284796bb48f | -2.97806 | -49.11787 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f8dc90c3-1dec-319b-9a21-4de5b244c8f4 | -2.92714 | -53.89569 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d88d059a-bafe-306b-a100-bbf99c454700 | -1.44181 | -55.11257 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50e32293-fcce-3f4e-83c4-81cd74cfe0d5 | -2.95627 | -53.92936 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b50d588b-13e8-3b23-95b5-856d553e0f88 | -3.06046 | -54.39556 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62b0dded-8092-3c08-853f-46229d51f84f | -3.33626 | -53.35989 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8f2c4d8-8e29-3679-9206-cc4f0cd76d24 | -3.0977 | -51.31832 | 2024-11-18 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e693a5c-fcf9-3c7e-bf43-fa702765da73 | -3.53343 | -50.25555 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 973a7c29-12e1-332b-9a99-8823e1ff6743 | -1.51754 | -52.2286 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35cf9e3b-8e81-38b2-88e2-f717dddb1c74 | -2.90247 | -53.05446 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8478c9d-50d5-34a0-87cc-7001f1479364 | -1.63253 | -53.30189 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbf01d3c-67ec-3f5f-9346-5eeb0cd25d49 | -3.33868 | -50.49527 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6152bba2-55d8-38df-98fa-35ccb55e3206 | -2.8549 | -54.0081 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 017696ae-c752-37b4-9b2b-e43b99dfb6f0 | -0.94655 | -51.72335 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab798f21-a10f-3086-b377-713329cadb47 | -3.05713 | -54.39505 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f61c79d-c7bd-32c9-8619-925a08a62ed9 | -3.14164 | -52.9809 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 69f0b849-bbcc-33f5-8e6e-bd3c1e4d03dc | -1.43514 | -53.38212 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e1dbdb28-a191-3832-b4b1-9f0a95c6fe15 | -0.93329 | -51.73807 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0091afd1-6b92-36f1-9684-4814a5d354f9 | -2.64185 | -53.97877 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 189f120c-1a00-3713-a6a2-80d795e5d7eb | -1.63479 | -53.28743 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca19493c-2234-3b60-acb2-7a0ed8484be7 | -3.57048 | -45.21236 | 2024-11-18 05:03:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 168deb81-f1b1-3c59-8419-953b947d1f67 | -3.46079 | -50.01177 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ac90d44-2865-3c42-b1eb-882c220723d0 | -3.56336 | -50.24929 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed912757-0a4c-3bd8-90e5-be9228441858 | -3.57501 | -50.25458 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d57bf721-e3e8-3941-8123-aa2a334209e7 | -1.20327 | -51.77754 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0ef2e39f-43f7-318b-97cb-708951e742b7 | -2.55572 | -53.98743 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f97b933-9995-34ea-a3fc-96f1d26e5a28 | -2.79778 | -54.00673 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40d982fe-34d4-36ac-8c47-aa667345f907 | -1.7058 | -45.82992 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README31.md)
