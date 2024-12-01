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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09a457e3-fda2-32b4-9156-3c0e288c3b43 | -4.47355 | -50.77186 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e17ac91-3235-357e-9057-5258c4c9234c | -3.09725 | -54.01759 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7b87dc7-8439-3bb8-98e2-373a0c370019 | -3.919 | -50.11681 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b9d7c1a-2883-32ef-a916-bd8c5c47880e | -3.22217 | -51.7178 | 2024-12-01 05:08:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b00639e1-06a5-3dd0-9281-b5a13313ad41 | -3.14206 | -53.84348 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cca83842-2b03-3924-a732-3aa2498512cd | -3.75171 | -52.2711 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c1c1f2d-197c-319e-a570-f2fc5d4eba4b | -3.32427 | -52.07804 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2180fa03-08bf-3ce4-87da-caaf77b4194e | -2.35173 | -52.73595 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1579148e-2baa-35bc-bd94-d4088c4139f5 | -3.68881 | -51.81767 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 649233ff-55eb-3c07-910a-9c679989fbcc | -2.53373 | -54.03754 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43e34ee4-87ac-3880-a09d-e972b99b4e2d | -2.8269 | -54.03043 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3bb8d0f3-b4a1-3cf4-9972-3b359752d5a0 | -1.69968 | -52.64642 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee3113b0-2807-371e-9be6-bab8bf7995d8 | -2.42118 | -54.01659 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10f089b9-5966-37e6-8c34-cf4d2172dd04 | -4.29125 | -54.67775 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08a57f21-c9ba-3141-9738-7226f67c63d5 | -2.52856 | -54.25483 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| add94dc7-f01e-3629-a749-1bcddb361e12 | -1.41117 | -54.52151 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48adbd29-6433-34bc-87f1-81453fe05faf | -3.51632 | -62.75731 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a2de966-d86b-348a-97ca-484461a9b120 | -2.53427 | -54.05717 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6fa7d106-95f0-3faf-a959-0c4221b491ba | -3.14266 | -53.83957 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f12c1a9d-9f19-39de-a3a7-27d41ce5bf79 | -2.94093 | -54.41951 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9a37709-3c37-32cb-b711-bd10aac3fab8 | -3.26304 | -53.64479 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2da0b133-face-38a0-89d0-e92dda47cabb | -2.03684 | -55.7746 | 2024-12-01 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 852f6540-f744-3013-9062-dc7634f825b9 | -2.81158 | -53.05034 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7bccb65d-a4ad-353c-b4e6-1df343dcaeee | -2.94168 | -53.22525 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed742695-d841-3f9a-b77b-d7711c7f9028 | -3.26009 | -53.6402 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 465408c9-ae0e-374e-8316-0a597c51d00b | -1.74377 | -52.31193 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1bf785e0-b257-3c83-809a-20815dae9592 | -3.83043 | -50.14194 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3fcdb57-b36e-3f35-838d-c86168eb92ac | -4.09851 | -48.83165 | 2024-12-01 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 841dcbf3-f1fa-317c-8021-d1707716d183 | -3.4654 | -53.88204 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a13277f8-ec59-37d0-8725-1997685cf974 | -2.23277 | -54.93692 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31bbc034-c623-3a79-b272-98ffc6051193 | -3.1051 | -50.36099 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76b87123-948a-3763-9458-1288a3a00079 | -1.89605 | -53.01878 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 105ccd82-a065-3e7c-867e-914e3347e5f1 | -2.45078 | -54.00939 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 931e47c5-aa35-3a3b-bb2b-65a1563b9de2 | -3.09025 | -54.01649 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09e5b9a0-df8b-35fd-945b-b35a810f64b1 | -3.9627 | -50.19151 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aab02594-f76b-3cc9-b00a-aeb2dd8f4eec | -2.87462 | -54.12298 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc6bddec-699d-380c-876e-ce3091938fee | -3.52087 | -51.1369 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe41840a-f3ce-363b-b05d-ab0f7996ff79 | -3.17958 | -53.25829 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcc58dd0-283c-3a35-a7ff-835f40136a9d | -2.77915 | -54.03891 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 205e68b3-c31d-354b-99ec-f455a5fb83fa | -1.59932 | -53.82964 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f08f68a-8f7c-3bcd-b43a-e4c8ee251bbd | -2.44141 | -53.62579 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6675c49b-e7a9-3621-a4f2-fe07c09866b0 | -1.47833 | -55.19693 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3e64126-38fa-3701-9a44-1decae97ec12 | -1.2735 | -54.55145 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41f5b2d3-1fd8-3e59-9c33-8939980c491f | -2.73163 | -49.37415 | 2024-12-01 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 61f6068d-31c1-3f3e-95b9-fd738d2939c3 | -2.93033 | -51.44592 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79b0e883-faab-353f-8ab6-fc4bd2233e01 | -3.16406 | -53.23853 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8626f955-cab2-354f-b065-d5d857ee164f | -2.19668 | -53.77904 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb2d6f8b-2c54-35e9-9456-83d43018afbe | -3.30522 | -51.10544 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ebdb56f-9126-30e8-9d0f-536afc6074de | -2.45265 | -53.62343 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c3048177-85fa-3372-ba3e-a8b33f72ee8f | -2.88199 | -54.00583 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c6d58eb-3fba-3484-a973-3f17b074a0e9 | -2.84047 | -54.09024 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deb1dcdb-56dd-3518-8b53-28d808cd9998 | -2.59538 | -54.23421 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85ac3152-e7db-37c4-8c39-82cc0266f4c9 | -2.60487 | -54.08375 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10b2df63-85a4-3087-8b81-adedd882b8f3 | -2.84253 | -54.04465 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38d16021-8932-3a91-b63f-7fc0a3891704 | -3.25172 | -53.6472 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a37fffb-2df8-3a91-a1f2-71cdeb923aae | -3.26696 | -50.20977 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e0cea720-5b81-35d4-8202-e79b9514e537 | -3.09375 | -54.01704 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 937c1125-7ec0-3908-a57d-09ab0d69fd7a | -3.69438 | -51.80793 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dd086e4-889a-36ed-abb6-5362048c6a47 | -3.26787 | -54.10272 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2334dda-5e30-35a0-9b29-29fca4970dbc | -3.28536 | -50.62986 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2f1aa5f-3efb-36e2-b172-5711eb01f9ac | -1.62222 | -53.88826 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c5589e5-5c62-3fe8-bf78-3a24467027bd | -2.04078 | -54.66437 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39bb52df-e64c-3504-80ea-59b27482b127 | -2.82387 | -55.58382 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a59ac93e-228f-3ac7-bb35-bf86df1dc106 | -3.05605 | -51.05885 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92fa9761-e216-35e1-b051-87d99e334d8a | -3.34343 | -53.28903 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c4f979e-1a08-3cab-b4e5-00dc4fdeaabb | -8.119 | -55.28437 | 2024-12-01 05:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f06f96ee-78fc-350e-b748-5374409fae77 | -1.64927 | -52.75371 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22c2acdf-9ca7-3c3e-924e-2dd65a888c51 | -3.1926 | -54.3339 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56d253bc-2186-3e93-9681-7894a4e9e9b1 | -2.89262 | -51.576 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c51565b1-1476-30cd-9956-cb5900a88987 | -1.76348 | -55.65374 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdc9edc8-23c0-3db3-8c28-71950c9f5de3 | -3.27047 | -51.47833 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1316e3b8-9c60-3a5c-85e3-2a64d61be76f | -2.87039 | -53.98816 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6bca0496-76d8-31b3-9c94-bcaa95d23bcb | -1.60056 | -52.28716 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0144af0b-d7a5-351a-b1e0-1e9a471bfd06 | -3.72351 | -54.52439 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cae223b5-f1c4-3b74-92de-e904ae5870be | -3.75486 | -52.27637 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 793a68c6-a766-3c50-94cb-df877c4a21f8 | -2.80067 | -54.03827 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7750470-0ca4-3ec1-b51c-cbaf912bc5aa | -4.76066 | -50.99072 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5546878-7f79-34d5-98cc-89f1b70ce19d | -2.56793 | -54.34143 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 119ef698-aa50-3ec4-9cb8-e2815efef257 | -2.7667 | -54.11947 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| decd54c7-149e-3dfa-83bd-a50562f5fc72 | -1.6978 | -52.46138 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5973130f-3d5a-31e3-a2ca-1a353431d009 | -4.00335 | -44.76286 | 2024-12-01 05:08:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 30789b1b-293f-3ca2-acbe-be473bd9ffcf | -3.7556 | -52.27158 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 161246af-4994-3e26-bc6a-9abfc0f13341 | -3.48704 | -53.81234 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e941875-428c-3ea2-9537-2c7efda1ae84 | -3.30666 | -50.03725 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a81395dd-ddfe-3b17-a0a3-379f2633bf28 | -3.87448 | -50.1531 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c368f29-bd78-3286-a173-7d7e35860cd8 | -3.01516 | -51.79014 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19a7da14-c3f1-364a-b964-ac1dc7223533 | -2.60306 | -54.22315 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77ce8681-444d-33c3-9d81-5f754c1b231c | -2.42696 | -54.0253 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7536c0e-73a9-3bfa-a829-f835f9621fce | -2.76833 | -55.35281 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51e2caa8-cb45-3d1a-9aad-92289b234195 | -1.37057 | -53.64334 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae31cb89-615f-384d-ae15-7d4af5d58f85 | -2.99512 | -51.06882 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ccddce3d-e403-312e-bcf7-386120cb5bae | -2.87789 | -46.80457 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26ef3a3f-5400-3f72-83a9-10f622494513 | -3.32031 | -53.29423 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c904ab27-e95e-3c07-a11a-ef8223d242ae | -3.09335 | -54.13564 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f26bf55-72dd-3f42-9a7d-d4874377481e | -2.89578 | -55.23118 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bbadd13-e356-38bb-9d27-fd502f62d645 | -3.53158 | -62.77261 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be0db0e1-d7c9-3d79-9442-510964ac07f7 | -2.83057 | -54.09794 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae45a3bf-e892-300e-b1ad-afb291c17e60 | -3.18233 | -45.35455 | 2024-12-01 05:08:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 979c8684-8c74-31b7-befd-7bb546bb87b6 | -2.4171 | -54.00942 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4120930e-c210-323f-a1b1-c483953eaef6 | -2.47514 | -54.01319 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README83.md)
