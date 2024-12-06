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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf7e0d69-75e6-3754-b293-c567e4d133f4 | -3.10813 | -54.06422 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fae81293-0ea0-3921-aa85-76d709428894 | -3.29157 | -53.82618 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3122a96a-057d-3d9b-8d19-15f300431abb | -3.60481 | -54.55019 | 2024-12-06 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1a9002a-fa0f-3406-96ef-3e08ef44c977 | -3.4006 | -42.29856 | 2024-12-06 04:50:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0283e8d-7df3-3009-96d4-26f3120dc91f | -3.11751 | -54.06117 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20a75e2e-18bb-3299-b426-66a4b22bfbbd | -2.46827 | -54.01369 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d4828eb-25ac-3c10-945b-b8cad6c1844e | -1.68642 | -52.78703 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6faed243-6178-3456-ac82-061695f70f5a | -1.34786 | -51.38026 | 2024-12-06 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dacbcbf-231a-3936-8597-de39abd9f3de | -1.67604 | -52.56113 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f04c1937-3099-315b-bf9f-9d21d321e9e5 | 2.42352 | -60.64671 | 2024-12-06 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08c7906a-9433-30aa-82b4-db0c84d9d21d | -2.52721 | -53.97985 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82ff5074-a4fd-3f77-bde0-64d309074977 | -1.53841 | -52.68024 | 2024-12-06 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d041e654-62fc-3917-a28a-1aa046679755 | -1.70439 | -52.78254 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a08e2a77-346a-34e7-a349-a321ca0fd34b | -1.90103 | -52.61741 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 157cb797-3db9-344b-8c46-5ee41cdf9687 | -2.49536 | -54.1125 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04330012-e350-31d3-a515-f90ee0ab9fbd | -1.67511 | -52.78573 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77bed74d-b144-3311-836d-816d4865a506 | -3.82346 | -54.7622 | 2024-12-06 04:50:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a476e41-6eab-366c-bcdf-98c29874d1c9 | -1.65938 | -52.75413 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39a8022e-bda5-35d9-8f68-7fdc5d2657f4 | -1.81713 | -52.73458 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc7a3205-4fb2-37fa-bac5-d1ecab7c0037 | -1.6984 | -52.57183 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9248cf70-2c24-375d-b1da-dd509ce41b8b | -1.6794 | -52.56165 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| db631819-fa9c-3e80-9395-1e87ff2c2253 | -3.11404 | -54.06062 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bffc05d-72c7-3bf1-8328-0f7989ce7a3f | -2.46694 | -54.01415 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c33b251b-8923-3466-894c-540a93efb41c | -3.12278 | -53.98448 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36d3ba70-8036-30e6-b12b-b3ae17bd548b | -3.17536 | -53.96611 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b243876-b825-3d56-b3dd-a268a250aa32 | -1.72801 | -52.65554 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba84d0a9-5377-334b-85ee-41360284374c | -1.67438 | -52.57169 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5bd4ba2b-d2c7-3d1f-940d-6ad76cfdaa98 | -2.36707 | -53.91661 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af5b4353-f301-312f-8413-2732c58a33d2 | -3.68603 | -54.31223 | 2024-12-06 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4050f7b2-5a8f-37b4-8b53-fc0400c20cfd | -2.52373 | -53.97932 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8d64625-79af-3286-a861-21da7206d53f | -2.26903 | -53.82808 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 669f2a46-eb67-3577-b338-aee42aba668d | -3.09772 | -54.06261 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40872753-cb99-3aee-9ad3-116ff6d4e787 | -6.11918 | -46.92954 | 2024-12-06 04:50:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6f4795c-0818-3628-8a8f-929e999821c0 | -6.93353 | -42.82998 | 2024-12-06 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 679e165c-1f76-3c64-bf2b-cfb27859174f | -2.47128 | -53.71629 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 641cb1cb-89f1-37a4-9a03-60ef6c344eac | -1.69259 | -52.79163 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cfb37ec3-399d-37dc-a0d0-0efe7dd78e28 | 3.23372 | -61.03329 | 2024-12-06 04:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 068f1220-d6bf-3649-88bf-b6755323389f | -2.38123 | -53.71399 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45a18294-0f5d-3fa6-b024-f8af0b80f734 | -1.67884 | -52.56517 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c90fe51f-1a28-33c7-b294-41bacc155dd8 | -1.6766 | -52.55761 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 995af76c-f8fd-32cb-bae7-83c675819af2 | -3.11873 | -54.05357 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 857fb797-826e-316b-bee4-b0420c3c2b1e | -1.47172 | -52.68103 | 2024-12-06 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3a7f884-989f-30ae-b537-5816271ef472 | -1.71 | -52.7907 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 159ddbee-efd8-3b53-8453-96bd77049b8b | 3.23435 | -61.03748 | 2024-12-06 04:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc9b9d2e-c58c-3e5b-853c-a692c53e6084 | -2.74752 | -54.15812 | 2024-12-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 868eee14-d528-305c-b2ea-cdec30b5738b | 2.47919 | -60.69503 | 2024-12-06 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbdcf8bc-0abf-3a8b-9f45-4c987732e92d | 2.62112 | -60.41022 | 2024-12-06 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f38c31d-55af-3c66-8634-da718dcfc143 | -2.5548 | -54.03094 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf77e145-bd74-3c8e-9527-e8baca6c25b1 | -1.90009 | -52.84908 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2cd3503-5347-3330-bd54-88cdd8b81aed | -11.82095 | -57.82543 | 2024-12-06 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a1935c3-6062-3f32-a599-c973ca397ec8 | -11.20773 | -53.82169 | 2024-12-06 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b73f4d2f-8e1d-3bd9-96fc-11de17ea8781 | -6.83852 | -47.30237 | 2024-12-06 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28b56f2c-0928-3f91-8a80-cf576caf657b | -11.82472 | -57.82609 | 2024-12-06 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d6ebb82-675f-30a2-bf08-1f11962de4d6 | -12.86078 | -51.93261 | 2024-12-06 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19a1574a-4ace-391d-9f0d-39503cce9f0e | -11.73517 | -54.31198 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d481da3-ae64-370b-a5b2-caf7508e5955 | -12.24291 | -52.45646 | 2024-12-06 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f6ce146-9cdd-3553-bcf1-77f179bde620 | -11.72604 | -54.31067 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb082b60-9c76-3ccc-a872-b94f44afa79c | -12.24236 | -52.46014 | 2024-12-06 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a9b3e33-c247-36a6-acc7-bf87b9406e4e | -11.32738 | -54.05021 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6eb6ae8d-93e4-3a7b-a443-646e4c6d8ab5 | -12.86021 | -51.93649 | 2024-12-06 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d62471-d144-3694-af41-94ccead82ed6 | -11.73184 | -54.31144 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4cd45c7-9d48-30b5-a70b-a8d31bac0b77 | -12.2418 | -52.46383 | 2024-12-06 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e68b5467-25cc-355b-914f-f01fc19a5316 | -6.77838 | -46.46595 | 2024-12-06 04:53:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b941eeed-1333-3a17-8a81-39dc2ea79124 | -13.22823 | -43.97506 | 2024-12-06 04:53:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a6089d9-e60e-3ea0-8bad-b61e70038bb9 | -11.32128 | -54.0456 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bde0958-3f57-3919-82a4-19cf75562cf6 | -11.20441 | -53.82115 | 2024-12-06 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16c27eb7-3c7a-3679-82cf-15ee18b05990 | -12.85964 | -51.94035 | 2024-12-06 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1ed86a7-905b-326a-b98a-ce1104faa400 | -13.62024 | -44.0938 | 2024-12-06 04:53:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58939498-57d0-3fac-8568-582348c92bdf | -13.62068 | -44.09002 | 2024-12-06 04:53:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23abcfd5-a3ba-3a2f-ab42-943e0f8cd611 | -6.76184 | -46.51957 | 2024-12-06 04:53:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b58f4543-c986-3cbc-aab4-1b5b96872afb | -11.32461 | -54.04615 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c86cab58-333e-3a58-848c-399ce618e403 | -8.02683 | -47.68496 | 2024-12-06 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39e56ff6-03d2-3609-8330-41af599a24cf | -11.72881 | -54.31475 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 627e4e05-65ae-3cdc-b1f4-f8922ad8ff24 | -6.86974 | -47.24098 | 2024-12-06 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e02a0ed1-067b-3cf6-8124-c3ea67c7fddb | -12.07344 | -48.38877 | 2024-12-06 04:53:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8d924ad-69d8-3b03-9f7b-1d735c91db4b | -8.02271 | -47.68436 | 2024-12-06 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e7705ae-5d11-38c3-bae3-d1d868d88487 | -8.02629 | -47.68867 | 2024-12-06 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3732776c-f887-3f1f-8e05-ce375fb5bccd | -11.72937 | -54.31121 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1376822f-e94c-3640-b329-5e9bfbd7e354 | -10.15086 | -47.54473 | 2024-12-06 04:53:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd13a8ae-d52d-3136-b0a2-1ae7bb1a3afd | -13.615 | -44.08925 | 2024-12-06 04:53:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc70313a-1012-35a0-bed8-dcd6c39be64f | -8.01806 | -47.68747 | 2024-12-06 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fbce946-73e4-3af4-95b8-73bd9915417a | -11.72993 | -54.30767 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 314d584d-daee-3e43-a030-b6e7ddabab9b | -6.85283 | -47.32003 | 2024-12-06 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff7ecfa2-4157-345d-a4ad-929d0b001686 | -11.82553 | -57.82145 | 2024-12-06 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9f495f0-860a-3506-9483-ae23a9f04a7d | -7.48399 | -47.48689 | 2024-12-06 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d721e5eb-c1dd-3c66-844d-241b27bbd8f7 | -11.82255 | -57.81618 | 2024-12-06 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a727c367-819a-32b1-aeea-eefdb370d4b6 | -12.59636 | -54.38723 | 2024-12-06 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3451d92c-ca8f-37f2-bece-aa14c5da49dc | -18.97514 | -42.38099 | 2024-12-06 04:53:00 | NPP-375D | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 56a78cd8-b825-39b5-9ca7-86122c35cd1d | -7.12591 | -55.11604 | 2024-12-06 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd677141-2d22-34ff-8cd4-a4a7177ff1f1 | -8.02217 | -47.68808 | 2024-12-06 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8b72ef2-42b7-317b-9343-1669bdc41adb | -11.7266 | -54.30713 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f72755da-be01-3038-8778-1dc37fdf641f | -9.65554 | -51.49704 | 2024-12-06 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1111b544-25cd-3bd9-a83f-766baa2034ef | -12.59303 | -54.38668 | 2024-12-06 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bec921b9-7716-3d21-ac69-10f4e74d5597 | -6.72027 | -47.20036 | 2024-12-06 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dba97553-ff3e-323f-ab04-83e739af2b61 | -6.85339 | -47.3163 | 2024-12-06 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c08e6194-b65a-3597-b69d-94cc2ffe2325 | -6.87391 | -47.24154 | 2024-12-06 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7464f0a6-d6c2-3290-a70d-bdd04907d0c5 | -18.97569 | -42.37487 | 2024-12-06 04:53:00 | NPP-375D | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9c7c1e0c-076b-33de-bf63-5dd2e453ec96 | -12.85907 | -51.94422 | 2024-12-06 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73ccb954-d72a-33cf-8dc8-8bec57ce4992 | -8.27533 | -48.0266 | 2024-12-06 04:53:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4652b60-cfcd-3478-b9ee-c85946f600a5 | -11.06007 | -45.38174 | 2024-12-06 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README7.md)
