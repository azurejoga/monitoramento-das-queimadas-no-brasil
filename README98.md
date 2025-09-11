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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad01fb16-9684-3803-a178-3c88d1dcf3d4 | -15.11898 | -52.3981 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6879bdfa-717e-3b14-be56-ac8d5101beed | -12.93193 | -54.75319 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8119ce9-9931-3633-82be-a0145406fd3f | -11.3563 | -46.5288 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e0c78f8-904d-3869-bab3-1097c09c17bb | -12.5282 | -45.34414 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9727669-e98d-39d1-9025-86165dd158bb | -12.96033 | -46.7363 | 2025-09-11 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b7f8769-05fc-3caf-bbe7-4352c02a8dc7 | -13.18745 | -51.76513 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39802ad5-ccc8-37c2-bfa8-aa5a3c8e83d2 | -14.39775 | -47.31751 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 187b775b-3dcf-3b27-b4cc-c7e042456621 | -12.10166 | -51.0148 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b4c8e01-211d-34b8-9c01-15690b1bc643 | -12.0005 | -47.59329 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 85d643be-5728-3762-98ad-e4ad21b31e00 | -10.17492 | -46.1878 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e54962d-2ad5-39b7-b255-71992072c60a | -11.39424 | -43.53008 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15834a22-46a9-30d9-aa1b-d3b1b022f588 | -16.29779 | -50.05194 | 2025-09-11 04:46:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70d23faf-2cd4-3719-81c0-f66a5fa57f5f | -9.90329 | -49.91051 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a87a8c72-076b-3ded-934f-a9fd0d147848 | -11.45971 | -43.60937 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 290b9ce2-e21b-3ae7-a85b-0c5e79645673 | -9.98415 | -51.69486 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f9a0a13-c3d1-33a9-8517-c44cdb8cbc44 | -12.91962 | -54.76303 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 989a29c6-8eba-3883-a9a3-747be727d277 | -9.71947 | -48.33585 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a7d63fb-7f10-31e4-a87a-25ad83982474 | -12.04708 | -47.60501 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92d5985d-b778-3557-95b5-cb9cc035d732 | -11.12746 | -52.02575 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60c50cca-ce06-3fe7-bb71-4e12c7584d48 | -11.48287 | -43.67062 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9b8ed28-acf3-3c24-b952-370b098e2dcf | -15.74988 | -53.50328 | 2025-09-11 04:46:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64e27e7f-6db7-34af-9e13-f58ac5bdf9b1 | -10.65976 | -48.6417 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37b7b0d4-e326-368b-81b9-3be94ffa98cd | -11.15451 | -52.04808 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12e7da58-83f3-3f67-b3da-a4e450fe3962 | -11.12636 | -52.05432 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc6db365-154e-3b6a-96b7-c939bc5861b8 | -11.36506 | -46.55812 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| f960f401-184b-33df-bbc9-0595caa91909 | -11.40453 | -43.55178 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e2bc5e3-1952-37c8-b465-486f99f24f12 | -10.37575 | -50.52905 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a2d1db7-9c71-302f-8ca7-21415ed3e116 | -11.6832 | -46.89952 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5de5ff6a-fb79-3a23-afb0-ef7116730998 | -11.04467 | -49.74362 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 103e3d4c-32ba-3650-9cc5-3f0bd46de9fa | -8.92306 | -51.05726 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 483f876f-32e8-3000-95a1-4f7174b69a40 | -12.94644 | -54.81564 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b1d8db9-7765-3456-bad7-0c78f91d7ebf | -15.13185 | -52.4224 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02027707-7725-393d-b715-91897324e4f6 | -10.54243 | -49.8937 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4c8f29b-82f7-3a91-9f5b-822a8d8ab2b5 | -9.70583 | -43.53956 | 2025-09-11 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4926b7ba-3b81-3603-9baf-4dd93f45bf67 | -14.28087 | -54.74739 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2817c1b4-8486-3c1b-8f3d-779c932fad18 | -9.80365 | -47.76126 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 275e71b0-3f3d-3cfd-b06e-f5b1f2d20ba5 | -9.97476 | -55.04744 | 2025-09-11 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38ebf027-2cd6-328d-94fb-a57383f1dd28 | -12.93474 | -54.75766 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60f1c684-d836-393b-ad4e-b5a51417e484 | -10.56198 | -51.49655 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff78c544-5fa2-3538-9eb1-6751c682fc82 | -11.49932 | -43.66376 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf7d1a77-18fb-37be-bc57-d4653e074eda | -12.02315 | -47.5755 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed84e83c-044c-35bf-b58a-5a927add90b7 | -15.55852 | -54.74681 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 917edc0f-085f-35b2-a4b1-caba0a9dbdc6 | -11.95865 | -46.65523 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09398c96-3957-39ba-8f69-13f52526b834 | -13.89548 | -47.98951 | 2025-09-11 04:46:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4ca95f0-ff24-3070-b3fa-694b59d87f7b | -15.15067 | -52.41094 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f7eb92d-3987-30c5-a016-8cd4d62def04 | -9.08538 | -50.47099 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2401b42-d4c5-3f07-bc67-112b7d3cc809 | -10.41116 | -50.52341 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6b98b9a-f336-31ba-bd91-57309d3f3d5b | -14.78767 | -48.23825 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 792cb814-5677-3bbf-85af-5db0acdef020 | -11.72104 | -48.25305 | 2025-09-11 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a8d6b3c-c166-361e-9bc3-3d525992b5f6 | -15.62621 | -47.53576 | 2025-09-11 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0714479b-afc4-3cd6-bbe6-5dcc24f31940 | -9.02165 | -49.77116 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1486be3-7b28-385d-9a6b-b123a05e06b1 | -12.40541 | -63.81881 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0902ea52-2172-3679-8ff5-38ec20b33e7b | -11.48927 | -43.64442 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77e0d916-2aa0-321c-b966-820062c20962 | -11.98796 | -47.59662 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 151f25ef-0bf7-3825-a9e7-fded13327ddc | -9.78788 | -51.1034 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2196cf7e-cff6-3e62-bb4f-8cd71d39d196 | -11.13077 | -52.02628 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8df0147b-c68b-3be2-9550-73294ea99431 | -11.46875 | -43.6198 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b172ffd-cfe4-3586-b365-979b8b430bd7 | -15.48547 | -49.36109 | 2025-09-11 04:46:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb8c3096-ceaf-33e4-b595-7e63fda9a08e | -12.82394 | -52.93671 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc0601a5-78ee-3531-8721-390e3da56bb6 | -11.03879 | -46.05194 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd0e1219-8eb7-3899-b578-1a20c6629fc2 | -12.42361 | -47.79631 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6560ebd-6dcd-344f-9e0a-3a1a4dceb165 | -12.12571 | -44.85063 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 38858e79-1add-37bb-a624-5e9fd5d5e9a3 | -11.8804 | -58.81831 | 2025-09-11 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e985a185-3fc6-3ea5-b806-59e1ead05358 | -9.01879 | -49.7669 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bcaf69a4-9433-3600-9029-160cd8af7f06 | -10.48211 | -49.37456 | 2025-09-11 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8c9f74fa-08ae-335f-9b8f-bffd30d7ace8 | -11.35468 | -56.32594 | 2025-09-11 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b44270c-579f-3178-ab76-16f24805f284 | -8.8488 | -52.00221 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ab1135b-f921-3fcf-9789-678e1a1b6ba3 | -12.93173 | -54.79706 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63b3288d-3cc5-381a-a2bb-6b6108601070 | -14.13714 | -45.41495 | 2025-09-11 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9de25d5-005a-33d8-8e0a-5025afcc8a68 | -10.54209 | -51.51503 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 717666b7-5bcd-3ead-88d2-b11293005276 | -9.05359 | -50.49899 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45923187-703d-33ab-8fee-79e5ab63fb25 | -13.25966 | -51.76203 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 998b7f67-0c28-3aa2-8a9d-75b247fdb8e6 | -15.22792 | -44.03878 | 2025-09-11 04:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e22caf82-cc52-37b1-95f7-1fec6d5972f2 | -11.71727 | -48.25248 | 2025-09-11 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0332494e-bfaf-3de1-a353-6adbdcf68f2e | -10.14775 | -46.16748 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5815808a-14ab-396d-b33d-46dde6100af9 | -12.03872 | -50.94149 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b639befd-00d4-30b6-80c5-bef6a9758b51 | -11.82023 | -46.75097 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f6779f4-7565-370e-b50e-a9ac0db22137 | -10.37826 | -48.83198 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c280e13-a057-3f5a-a982-503ae907ffc7 | -9.07292 | -49.82472 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75d581f1-20e0-3731-ad0e-54bad209bf7f | -12.1332 | -44.86719 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b69ac2c-bbc7-3be6-b8d2-8d45e3a889d4 | -12.96365 | -54.75476 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 171136e2-2c68-38e0-b248-fa46645e87fd | -15.09824 | -50.06884 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c7c9988-32cc-3519-a5f2-e8af5acaeec6 | -14.88803 | -55.84841 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd519ca5-983e-3f62-a04c-fe715c24b03a | -10.26434 | -48.82113 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86beb4cd-71a6-3f0a-8e1d-5e48006b80c0 | -14.50803 | -53.95974 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e61144d1-aa53-3c8a-8283-67faa6e70568 | -11.46367 | -43.69859 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c637d66e-2da7-308b-a730-f24b710ea550 | -9.211 | -51.81741 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa810e33-d7ee-37e4-877f-898faffc2b5f | -11.88476 | -58.8194 | 2025-09-11 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3357a217-5211-31e3-b9a4-e0013b7d360b | -12.92113 | -54.77526 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ebe5aab-acfd-3208-a61c-23ec66fd7a97 | -11.14236 | -52.06049 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b571377-69b5-3cdf-98c3-afabb58c7980 | -11.60645 | -52.21798 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5d38001-789d-341e-9e33-e0db1f3fc3a2 | -9.08259 | -49.80719 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc0b0af3-9c9a-30e7-a54a-930b1ffa7df4 | -11.48476 | -43.68079 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbb53771-1b62-3b5f-b2bb-9c581c1bc6c9 | -14.88231 | -55.83904 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2add4c68-9f5b-30b9-bfac-2e72d93dd783 | -12.24162 | -47.32587 | 2025-09-11 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3eb402c-906d-31f1-b86a-ae8df1ab126e | -10.31185 | -48.79837 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 59a879bd-1887-378c-a50d-c0b89ad2e2b1 | -11.35109 | -46.50436 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 02a66f86-c71b-38c8-8d05-2caa857b5493 | -9.09281 | -49.85435 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83c0f545-eb33-3192-bb12-7e895cf44094 | -9.77559 | -51.09797 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 834a74a5-0bf5-34e8-bfda-43e3f558ac39 | -9.03134 | -49.77646 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README99.md)
