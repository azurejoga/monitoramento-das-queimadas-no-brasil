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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18dbb64a-1af6-3efb-9261-2e23915c37e6 | -3.63672 | -51.52144 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0337b98-fc25-3766-8107-cfa91d66e374 | -0.74574 | -52.41385 | 2024-11-24 04:53:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fe66a41-d02f-37b4-b39b-127c71630bb2 | -3.03445 | -49.45473 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d9270d39-cc29-31d6-9f83-0e39522241e8 | -3.07933 | -53.83883 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c7318a8-4102-3ed2-bc36-0d1d141b620a | -2.25359 | -50.35536 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d7967de-d7d4-3c89-8d11-bca6161b0440 | -0.94208 | -51.65824 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 323b5b1d-e4cc-3dc5-90e2-dbbf28340b1c | -0.39257 | -51.45286 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c30b60a9-e882-3e55-b9f1-e2bda0b0e1b9 | -3.17219 | -49.07213 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3254138-a21e-3a8a-b7ed-d93f52880adf | -2.70417 | -46.28988 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a40e0c88-b2d0-3d48-a0c8-a48f032c5931 | -1.19783 | -51.76099 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3381b951-66e9-3d55-8170-7601cc8670e3 | -0.10227 | -51.74078 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62513d4f-985e-3248-a5cf-4be950f7f9ca | -2.87432 | -45.83021 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2065ea79-4223-3695-be2e-7fa851be061d | -2.0372 | -52.0966 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e6da91e4-5406-3c8c-81a3-f7464b590497 | -2.90288 | -54.60137 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fed0e924-6ccd-33dc-940b-db095eb7dd0c | -1.1992 | -51.9727 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d102535f-512a-31f9-b8b6-dfbc67fa6830 | -2.77563 | -48.64976 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9dd2f96-821d-35ba-a103-3cd1b98e8ebe | -2.70096 | -46.28183 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9dd39fdb-56f5-3764-8316-2ae152900d87 | -4.52599 | -49.81414 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07eb5572-a5a6-300c-aa3b-e6d8664f5218 | -1.40295 | -49.39041 | 2024-11-24 04:53:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c519bd3-8272-3e6c-adec-f4f847f7b8a7 | -3.68951 | -47.11625 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ff21ab2-8291-382a-b66d-447577c623f1 | -2.45716 | -49.90209 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43c3a564-f418-364a-9120-688ef9f3befc | -2.69792 | -46.1032 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30f88298-4cd9-3852-88ec-8ebc6da81714 | -3.18565 | -54.32213 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b9865d5-2e86-3a31-8abb-f39d1503cd4e | -1.8197 | -50.9802 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6aeb8bc-0bb7-3109-8124-47913a33bc5f | -4.62558 | -46.04563 | 2024-11-24 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1939befb-4b91-3e74-badc-8a94b098c204 | -1.06293 | -51.75423 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acfd32c3-22ce-36b5-bfe1-ed4661298e78 | -3.23447 | -54.10012 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e59d1735-fdf7-3b6f-86e0-7571038afc84 | -2.16357 | -50.45593 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d185bd75-57a8-34a4-ad20-041f60078034 | -1.06938 | -46.80184 | 2024-11-24 04:53:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95e45f5f-f458-32b8-b450-5d0fc9874c9f | -2.94661 | -51.43254 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2d5673c-f9e6-3808-813a-898ca824feb7 | -2.31604 | -46.3365 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fbcabff-96cf-3c52-bd92-fe5788a6a7f6 | -3.88077 | -52.35786 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4405ad1e-0a3b-3856-b3d5-213f84e0d6f6 | -3.67457 | -51.73706 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a29a4927-90e5-35cb-a646-f707c865af29 | -3.24812 | -53.27038 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e1eda956-3eb5-3711-8e8c-87975a46caa7 | -2.82398 | -54.09797 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d6ecdb6-65c9-3906-9c98-30fda319780b | -2.12539 | -50.76217 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e62c039-2753-3c9a-8397-1466f6e2c2f5 | -3.09856 | -54.55887 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d85d2afe-c63c-3530-8191-de4139033b18 | -1.2167 | -51.94726 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ca23bde-cebe-3e10-84dc-c857bb950195 | -3.64224 | -50.2235 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c416065f-19af-30ea-82d9-510a150ae9b6 | -2.46901 | -53.96723 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b252ef7-2ae8-355c-944b-bc1be6294166 | 0.08922 | -51.48582 | 2024-11-24 04:53:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93cf253f-6640-3652-8c0e-99aa02a8069c | -2.76083 | -54.07638 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6ca2bdd-5127-39ae-96fb-6f5206761604 | -3.63825 | -50.2267 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8399077-7e00-39df-9dec-bd475eb18d38 | -2.40377 | -49.05449 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e20a898b-c6b6-32b0-ae5a-aba89adecdea | -3.19364 | -48.58551 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d588a4df-090c-33e3-8357-72190521254e | -1.30729 | -51.86987 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b807ffd-9086-3132-86c8-24fd675f96c0 | -2.3996 | -49.05796 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0016ee44-63e8-3a32-a8d5-7fbe6c32dfc2 | -2.86244 | -49.84341 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a3c2861-88d2-30e8-9181-9ff9df0a9ecc | -2.37565 | -49.84044 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fec919b-2ac2-367b-bcdf-16867ad096d8 | -3.50875 | -53.81174 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 16576d93-d1ab-3d83-8d79-855407be2f59 | -2.85855 | -51.27649 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f03797cf-986f-35a0-83d5-cfe6b17d01cb | -1.77801 | -50.9417 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a1e25a4-4bd9-32de-8b35-3c7350050733 | -2.23357 | -50.50657 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8952c3bd-b272-3294-9eea-8d47b755abb4 | -3.49609 | -50.46931 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac49d74e-4917-3b9c-8a35-ca3e7502d936 | -4.0586 | -53.65537 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfdc94e0-fb11-392f-9122-96c16634be87 | -3.67825 | -50.21759 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e1b173a-a7bb-3105-9573-9b5c11eda1eb | -3.10666 | -45.78612 | 2024-11-24 04:53:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c86d243-c2d9-3628-89e4-fe48df3cc9c1 | -1.81604 | -46.63836 | 2024-11-24 04:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea537780-1e92-3f52-b0e6-08785d37d7a7 | -1.25159 | -51.74544 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38ae3f68-b9dd-3cae-8c25-aede5a8c0f35 | -3.98806 | -47.72654 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2cb6fafd-ce78-358e-aa98-0747f131dcc4 | -3.27903 | -53.82121 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2f85162-4104-3f90-b6ca-833eed13dcf8 | -3.61314 | -54.74422 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23b0a82a-f20c-3183-942f-b53f055b8f0e | -3.86903 | -47.05809 | 2024-11-24 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37006041-f356-3074-a285-70643a13005e | -3.2953 | -45.72878 | 2024-11-24 04:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| efa26f14-1430-35d4-b21a-2a5cc54b59f1 | -3.04599 | -53.42783 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd1f4e55-2df5-37b7-bbde-8254a054b110 | -2.59957 | -46.26651 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6301c4f2-7d92-384e-b94e-cd0e1429aeb3 | -2.1753 | -48.55877 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c472a051-1274-306a-bc86-9fee24cdea25 | -2.45954 | -53.69424 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 740975b5-091b-35ae-b3cd-31d6a9031259 | -1.26159 | -51.76803 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ddac3711-17b3-3a72-9f33-9dc342a53ffa | -0.03844 | -51.60804 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcaacc69-5e69-3e99-b530-e24716070889 | -2.76024 | -54.0801 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9caef27b-f413-36f3-b8a3-2a8501b6b0f6 | -2.70052 | -46.28531 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be88fb0f-48ac-3328-9ead-b5d4cf4f494f | -4.63721 | -46.87681 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7aebd49-e763-3645-9585-fde48df50592 | -2.7388 | -46.08401 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8391552-0116-3408-9bd7-373ddbbb3ed2 | -3.12605 | -54.18573 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2d79529-99c3-304e-80a4-ac82ec45688f | -1.38993 | -51.14064 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df81b597-7ca7-3bcc-a74c-26539fd25a78 | -4.01769 | -46.97925 | 2024-11-24 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8508714b-1f0f-3cfd-9d2c-31343f26e77a | -3.84352 | -44.05344 | 2024-11-24 04:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e1099edb-0454-3412-85b1-3f49e2b6cf66 | -2.70897 | -46.28663 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d17f0f52-0e10-3712-97ee-cd55bd47962a | -2.91889 | -50.3189 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa09c8c1-2a4b-35eb-aad8-809078d2cc26 | -1.95346 | -49.53054 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe42de26-825d-362c-be53-2033db8096f2 | -1.24169 | -51.74392 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c286592-4336-3a52-95ec-d01c954b9aa7 | -2.36994 | -49.83189 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da92caab-66cc-391a-a39a-aab17e53256e | -3.17582 | -46.54725 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9962e7cc-26a2-33f2-96ab-b0692ed2bf8d | -2.38687 | -50.33115 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79a5476f-0a05-3ec7-9a77-32221ea91c45 | -5.11984 | -46.17212 | 2024-11-24 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc747340-ad1c-376c-8c54-3c0b52a801ff | -3.97164 | -46.72876 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a86ee838-5af7-3a6b-b110-ec34ab1d048f | -0.98411 | -51.71382 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d9703f0-6d2f-3c93-8550-8dbcc06926a5 | -2.48546 | -47.09315 | 2024-11-24 04:53:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c0ded46-325b-3cb8-9cbb-9f1d09214f31 | -3.38214 | -50.33981 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2bd2fcf-8659-3446-b72a-e18d3529ed65 | -2.94321 | -51.41074 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3514352-ef2f-3fe4-a8c2-65fdb9882a0c | -3.25884 | -52.85345 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61a76b59-7391-3e5d-b622-833f504a9227 | -1.47072 | -55.10346 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 582112b0-5a42-3da2-8899-a775289ce105 | -2.0334 | -51.3574 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ce9afcd-92c0-3bad-84a6-7d98abdb5c60 | -1.1157 | -53.39799 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5aa6def-9655-316d-9833-7de717fa8c33 | -2.95378 | -51.43011 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4085d691-a5c5-32b3-8a1d-976e94e87aef | -2.69995 | -46.28922 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d715625b-a406-3a82-9b0c-1da560d6db90 | -5.10372 | -43.14093 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8d94847-19f7-3b30-9a8e-5bf73eaf6802 | -3.53759 | -53.07177 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d831103-067f-348b-bd60-f7460e250bde | -0.81766 | -52.82724 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README45.md)
