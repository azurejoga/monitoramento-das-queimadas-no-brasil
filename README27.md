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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b99a548-982b-302a-b9f0-2da6dff0f3f8 | -3.20852 | -46.81114 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 65fbc0b9-cd2d-3fa2-a086-74c14cfb1dd7 | -3.47173 | -53.96655 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb3002a6-6212-3d72-8bbc-838b06eb8fab | -4.82872 | -47.31373 | 2024-12-10 04:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 389ab243-76d1-32e2-8651-a9d265f8a9b9 | -3.05843 | -54.24867 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 891353c1-6737-38e9-9271-820f1e23679e | -3.70354 | -52.38206 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 550f647d-64f8-3e97-9bda-7558080cd848 | -1.49864 | -53.43085 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d62e9a97-8b05-381f-8e9b-5eb4f220eb04 | -10.88256 | -54.75198 | 2024-12-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b37ee60f-f0ca-3088-8585-83ee769838a7 | -3.61327 | -50.56819 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8118191c-0b64-3e2b-91e8-36f77b58f3e0 | -3.51567 | -52.19101 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a69f43f3-0079-3d1e-8f17-8c100a605e3e | -3.06593 | -54.24592 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a8da723-5096-31c7-b82f-9aa5f76c5d6f | -13.93859 | -44.35785 | 2024-12-10 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de391936-af41-33b6-9822-653ac0180825 | -5.62306 | -44.83883 | 2024-12-10 04:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04c65c0f-4ec3-31fb-a2f7-de202f7e047c | -12.56808 | -51.30663 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1123d493-205a-37f2-97de-3f53157b89d3 | -11.41707 | -54.31865 | 2024-12-10 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1cff76b-4cc8-3bfd-b259-37f6e09fd3ab | -10.67743 | -55.92336 | 2024-12-10 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d26879f4-9a85-3ab4-b928-88c341ce2dfc | -3.16001 | -51.32973 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39ae6ca9-8f2e-3db3-a050-53bed1436e2e | -3.11499 | -54.0698 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0198cb68-18e5-3011-ae71-87524e38a035 | -10.44978 | -44.89304 | 2024-12-10 04:53:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4d92b502-7b96-3be6-ad36-c3722d8245d9 | -11.69224 | -57.44751 | 2024-12-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| deaee5b7-e26a-3ed8-ba81-25f675cc84ba | -2.88474 | -49.0154 | 2024-12-10 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16413d10-0d5e-3a7f-82bb-b8321ae317c8 | -2.829 | -53.05702 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e24f13ea-87d1-392a-9e39-378c24c1851b | -2.61396 | -54.23898 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e68c3c1e-a833-3930-8036-aa9df03941b1 | -10.40042 | -51.76534 | 2024-12-10 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44e4a27c-3281-3329-a3d0-f6e9b9489a05 | -2.37543 | -53.86187 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d514f9b-efd9-3c92-b908-321d938f689a | -11.14837 | -54.23176 | 2024-12-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e279650-592a-3214-9cfd-d6a601399343 | -2.91839 | -52.96354 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c7da63a3-a957-3b58-a4c9-90a89745a9d8 | -2.45197 | -53.70804 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dce3c5b3-b453-3b49-8bfc-d4c1d95e9831 | -3.60643 | -53.13206 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4fd58028-0ab9-349f-a7fb-0924d72eed07 | -12.24725 | -52.44407 | 2024-12-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2333b610-a52e-3851-bb4f-4a14e879c0eb | -3.12702 | -54.06025 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79d83fc9-348e-3381-841e-97d7db79fcc0 | -12.48127 | -51.43258 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6d35475-4ffe-3c57-95a7-a0c3d96fb4ce | -3.23739 | -42.43219 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a584401-7d6c-322b-a6d4-81aaa31f35b1 | -2.78828 | -52.86119 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad702981-932b-3ec5-8137-98f44f2325d9 | -4.59774 | -49.17369 | 2024-12-10 04:53:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 437a58d1-ba76-313a-96e5-c26e40c2e630 | -2.61681 | -54.24331 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb9a913d-9564-32b1-a8ef-aea41a9c717f | -3.52789 | -54.59379 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 934508e9-41f5-3587-ac5e-c59d44f75724 | -12.32063 | -51.51711 | 2024-12-10 04:53:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a256bb62-fe8e-30dd-930d-b89305220080 | -3.80974 | -52.24779 | 2024-12-10 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 510b1e73-83c8-3dd0-84b7-6b913eaacc3c | -2.69448 | -52.91802 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c96f3ef6-2eea-34d6-b31d-f61608e4cf22 | -4.54612 | -48.01796 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| add7e113-6c25-3e30-8d66-0f42f2a6b275 | -2.78958 | -53.22034 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0828e76-8c53-3022-85b7-ebd9c69096a3 | -3.58652 | -53.7318 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52212071-3da6-3cad-87c7-47b22ef57814 | -1.40323 | -51.58216 | 2024-12-10 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82de7d48-e5d9-3a3a-b60f-442bd4a5a5f5 | -3.11098 | -54.07299 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46f9630f-68d7-3180-aeea-dbaa48482851 | -6.92184 | -43.5122 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8460a541-ba45-3fd3-9876-bc83396c9185 | -2.81444 | -52.97605 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7cf8a759-47ea-37a9-8d9a-66c35236365d | -2.45881 | -53.66427 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3eaa2448-c952-3e75-884e-9b61da7fb067 | -4.39576 | -47.76629 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ebd1730-88f9-3361-8419-ce176c722e17 | -4.63782 | -49.4926 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8c8cd375-6e82-3feb-85c0-640200af2b48 | -3.09687 | -53.73689 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d4c8f53-f47c-3022-aca8-598262f0f085 | -2.22232 | -53.7182 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8e7a677-ed7d-31db-a3b6-92a592519546 | -3.10758 | -53.75713 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80ef124f-bbf0-30d6-b182-b492c7fa2b1a | -12.57164 | -51.30717 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41825a26-ada3-322a-8769-aeaee2ad16b3 | -3.06869 | -54.07414 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbe432aa-2096-3d38-a396-8f5f8e9ad80b | -3.12027 | -54.03648 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5331a6b-7a3d-3168-af98-b419f03c8c80 | -3.20798 | -46.81482 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89a7acbe-6ae1-3682-b115-01c70c549282 | -9.18618 | -63.44102 | 2024-12-10 04:53:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 511fb5df-1432-336d-a419-635b15e26088 | -4.54538 | -48.02279 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6230acb2-6a59-3109-aa47-ba3d1d1f74ef | -6.91049 | -43.51403 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2f42db5-3c32-3d5a-a4bd-6e0b977e2f6e | -12.36911 | -54.1668 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 501f3d7d-8df0-3d00-aa8d-70ff44381ee6 | -5.20917 | -44.65459 | 2024-12-10 04:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5499e9d8-0879-3b35-9a46-df6435f05642 | -3.09767 | -53.25044 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af1b00c9-50fa-38c0-ae2d-d4a7470ca8b4 | -2.97112 | -53.93463 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2844912f-2690-34b1-93f9-e3675f21b1f9 | -11.7823 | -55.12626 | 2024-12-10 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68a4bc16-d521-3707-8508-e08150bfa322 | -4.38618 | -47.74957 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ef0a707-25c7-3184-b5ae-5900e559d874 | -3.10259 | -53.90559 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffb403d4-958a-3259-9026-ed80c2596acc | -2.59052 | -53.96697 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 600402c8-fa84-3e64-b738-8671d05d2f19 | -3.08312 | -54.04972 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f166b282-8d6e-3e2a-9929-60d059c5f0c0 | -2.37781 | -53.67062 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c7808a5-b284-3656-90c7-6bbb81f16352 | -2.44857 | -53.70753 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 918bf0f7-382b-3948-bd01-072cec542b26 | -1.64423 | -45.92014 | 2024-12-10 04:53:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17758e56-a882-3588-92b4-c21bbfd6e4b6 | -1.67473 | -54.3457 | 2024-12-10 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aedb8fb8-6bbd-3f05-9e05-73fb498134af | -2.57681 | -54.34707 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66da7c24-8f6c-3f00-85ab-699b93061b5f | -2.91895 | -52.96003 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a4ea0498-b021-372a-844b-97cfb36b452d | -2.38554 | -53.7317 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2abafa86-1aa7-381b-92f1-ebb571e16feb | -12.24385 | -52.44355 | 2024-12-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3c6b0f1-bf60-364d-a737-5f7613432d5b | -4.14997 | -49.31435 | 2024-12-10 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27dda101-014f-3b67-81e1-4f8354abee03 | -3.35346 | -53.80648 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44779caf-550a-3122-86f1-e7cdba661535 | -3.23845 | -42.42489 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1752270d-9fca-334c-81c9-4583a27886b2 | -5.57955 | -45.20827 | 2024-12-10 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 115a5d6c-e73f-37d8-b50e-c9bff081c6aa | -3.5297 | -54.59352 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 594124a0-3af0-39dd-80c4-94a8a3538c39 | -3.12419 | -54.056 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd615921-5114-3f2a-bff1-b0ce73fa2d70 | -10.42525 | -56.26672 | 2024-12-10 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 408f294a-f941-38fd-a176-b1253934f9ce | -3.51102 | -54.49715 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb541505-6ea8-3e35-89e9-cdf5cc3efc1b | -1.49921 | -53.4272 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af674a7b-0d12-350d-82c5-ba51f2365b3f | -5.91671 | -48.06166 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af5b2003-176e-3bf5-86fa-2464f47b4638 | -1.96946 | -48.43165 | 2024-12-10 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aceb0966-a9e3-3f54-aec0-3fd6cc03573c | -3.1231 | -54.0407 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e478e85-ae7f-3094-bcf8-0e447e936daf | -2.08226 | -53.39905 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73019258-5c14-392c-89dd-5c31c3371fae | -3.4383 | -50.151 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3410c27-7f9a-3686-b02c-5f81874c9afb | -12.36801 | -54.17383 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7f0a571-0472-3e8d-aa3c-42f6152a9316 | -2.61516 | -54.23145 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a369d39-b89f-34c2-9219-f2d3ded6fcfb | -1.61451 | -54.94175 | 2024-12-10 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 629dc8c6-b52f-39a1-af6f-18b99e21cbe3 | -12.85478 | -51.93891 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a0019875-152f-39a2-bab7-1604a5e42ffd | -3.35007 | -53.80596 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9919c906-cc8d-3ef8-b948-e921d8ada863 | -3.69916 | -50.94213 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6c747e1-dc7b-35b6-9b28-54fc092728d1 | -4.57236 | -48.91821 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab8fc4c8-985e-3e41-843e-5e35f2b0db70 | -1.6541 | -55.07566 | 2024-12-10 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78e58d73-bef2-3096-853b-280799d847e7 | -2.99021 | -52.85334 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c1afbcaf-aaca-3699-a0de-81345a92a76c | -3.09326 | -54.07412 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
