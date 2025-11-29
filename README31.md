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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ba80c41-3ce7-351d-a2b9-32b439523a1f | -7.35714 | -37.34355 | 2025-11-29 11:19:00 | TERRA_M-M | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 8d5a9ca8-4178-3922-9eb1-3c241502ed82 | -7.26231 | -37.88189 | 2025-11-29 11:19:00 | TERRA_M-M | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 11.8 |
| dddd6b55-9484-3997-89a1-4e693a661b28 | -7.25754 | -37.88894 | 2025-11-29 11:19:00 | TERRA_M-M | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 16bcc6d0-618c-3f0c-bc28-691f4005dadb | -7.82104 | -37.39571 | 2025-11-29 11:19:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 21.2 |
| af3e39d7-71a8-32bd-96cb-c3f95d28ecd4 | -7.97425 | -37.59901 | 2025-11-29 11:19:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d89619ff-7c03-3868-a4b4-43a55c480d36 | -7.79385 | -37.24575 | 2025-11-29 11:19:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 84a9a71a-7219-333f-b3d2-05f2bea384fe | -7.55824 | -38.71556 | 2025-11-29 11:19:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 74ac2534-8b66-395d-ab4a-f782c07e1662 | -20.1813 | -52.3754 | 2025-11-29 11:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 750b273f-f817-3885-8e83-6295e4e13971 | -2.8666 | -45.508 | 2025-11-29 11:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 369.5 |
| 15622c85-ba2c-30d8-80fc-ca70f3d6ce83 | -2.848 | -45.5086 | 2025-11-29 11:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 979.3 |
| 1c0f6c97-e824-3351-ba78-e9bb59734fa0 | -2.848 | -45.5086 | 2025-11-29 11:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 802.5 |
| 7a3377e8-c122-3eda-9ba6-a46329c48495 | -20.1813 | -52.3754 | 2025-11-29 11:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 38a917c3-54a8-3ae2-8448-12af1b0d337d | -20.1813 | -52.3754 | 2025-11-29 11:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 129.2 |
| d4871803-217c-3ba2-8992-cde99b25f477 | -20.1813 | -52.3754 | 2025-11-29 11:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 144.5 |
| d0255477-b4c0-331d-aeae-211fc1e070c4 | -20.1813 | -52.3754 | 2025-11-29 12:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 57b7cb23-893d-30b0-886c-327a3fb2a20c | -20.1813 | -52.3754 | 2025-11-29 12:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 134.0 |
| f00c3085-5f75-31be-9854-b22d0f9a2b94 | -20.1813 | -52.3754 | 2025-11-29 12:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 4df9b69a-7805-3166-957f-bff0b108d613 | -7.975 | -37.5971 | 2025-11-29 12:30:00 | GOES-19 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 277.6 |
| f972df20-71e8-3a1f-a846-8891494c3288 | -20.1813 | -52.3754 | 2025-11-29 12:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 2caeefa4-048f-3e71-8126-c76f039f09b9 | -7.975 | -37.5971 | 2025-11-29 12:40:00 | GOES-19 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 154.0 |
| 0f00dba2-ae09-3f26-a641-86428f55603c | -20.1813 | -52.3754 | 2025-11-29 12:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 7d11b6ea-0d19-3158-9dd3-597119a33cb1 | -20.1813 | -52.3754 | 2025-11-29 12:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 143.4 |
| e926fcf9-b458-3bf9-a283-80256c1c5a06 | 3.3341 | -51.32109 | 2025-11-29 12:55:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 8839ad26-df8a-3d25-8d45-0d129af0a597 | -1.33679 | -55.50447 | 2025-11-29 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 407c4cb6-f7c1-3868-8e74-aadf14f90257 | -1.81496 | -55.77602 | 2025-11-29 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4c65aff7-db62-3316-b345-c7fabbae67db | 3.34516 | -51.31947 | 2025-11-29 12:55:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 298b8e03-10b5-3195-94ba-2bf6faf819ee | -1.41001 | -55.37872 | 2025-11-29 12:55:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3becec40-dff3-3d67-98be-c40b17b23f51 | -11.26785 | -53.9613 | 2025-11-29 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 7be1cee7-2d3e-3d9d-93bc-4f1216ffe8af | -12.77839 | -54.80654 | 2025-11-29 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2d3df3c1-c797-3823-afaa-178e2cd9a5e6 | -11.5992 | -51.96904 | 2025-11-29 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 122438b6-ff7b-39d4-b44a-6fed84745f60 | -11.27926 | -53.96282 | 2025-11-29 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a6c6d108-b0dd-3c50-be7f-1a3649d9f2d4 | -13.04831 | -53.71566 | 2025-11-29 12:57:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e1c1f289-cf39-35e6-9b77-d2c51970bf1e | -12.78736 | -54.80182 | 2025-11-29 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| a82ca8da-eaef-3d77-ae56-7d68e1dcc410 | -11.72192 | -52.4776 | 2025-11-29 12:57:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 6095313c-841b-3958-83fe-cec4823eee08 | -13.01125 | -53.47004 | 2025-11-29 12:57:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 48dce67e-b184-3d93-8719-852314749f72 | -11.49116 | -51.92089 | 2025-11-29 12:57:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 36c67245-2d56-3615-ac57-f2d548243ce6 | -12.15748 | -57.02149 | 2025-11-29 12:57:00 | TERRA_M-T | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b9e33d43-4a16-34f9-9073-b698a65676f5 | -11.4857 | -51.92569 | 2025-11-29 12:57:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| c530095b-db66-34cf-9742-1b20ff66738e | -11.63803 | -52.84517 | 2025-11-29 12:57:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b3df82a7-952a-341a-aa64-6da4d004620c | -12.78012 | -54.79234 | 2025-11-29 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5bd38fdf-846d-391f-913d-e9d58c8f60b8 | -19.90055 | -57.44275 | 2025-11-29 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 61ed47c7-2f26-3e67-9731-ce4a585c7332 | -15.58039 | -60.10509 | 2025-11-29 12:59:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f94e666d-69f7-353e-b51d-d315c70d2846 | -20.44221 | -57.91851 | 2025-11-29 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 66cb30c1-ff57-39c5-92c8-5bac7994b45c | -16.23092 | -58.81931 | 2025-11-29 12:59:00 | TERRA_M-T | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| cb3532ec-00b1-3fba-9e19-02581ab7f22f | -14.92025 | -57.28717 | 2025-11-29 12:59:00 | TERRA_M-T | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7520381d-08b4-390d-8352-0ac66ddea82b | -14.87063 | -57.7957 | 2025-11-29 12:59:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 1b93a7e4-f4ec-3ea7-8d18-d2474e9c3a8f | -15.90155 | -59.65376 | 2025-11-29 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ad525c3e-f985-33ce-9a33-bdd7611276cc | -13.97892 | -54.43763 | 2025-11-29 12:59:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| d12dc431-e864-3c8f-b0a5-fd352eae3c15 | -20.18033 | -52.37698 | 2025-11-29 12:59:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 1b63c603-2257-32ed-a8ae-5762b98026d9 | -22.0514 | -56.34304 | 2025-11-29 12:59:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 23.6 |
| c04e0589-ff42-38c4-9c5d-4256d745b9a0 | -20.42938 | -53.56713 | 2025-11-29 12:59:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 89418f86-9e81-31ec-812f-4024e33f1290 | -21.63156 | -55.15975 | 2025-11-29 12:59:00 | TERRA_M-T | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 70df4529-0215-319b-adf3-35b81637a3b8 | -14.87201 | -57.7856 | 2025-11-29 12:59:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a1e2c963-69f8-3a3c-9fa5-6186d1ee6205 | -13.54358 | -59.88903 | 2025-11-29 12:59:00 | TERRA_M-T | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 46791a0f-78a4-3b89-812c-d23be93b61f1 | -17.20527 | -53.49346 | 2025-11-29 12:59:00 | TERRA_M-T | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 244983d0-544c-3a8d-979d-3e35a5edde3c | -13.66559 | -59.37031 | 2025-11-29 12:59:00 | TERRA_M-T | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c4e73f6c-1d53-3102-beee-722b05d40808 | -17.20294 | -53.51445 | 2025-11-29 12:59:00 | TERRA_M-T | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| bec08acd-74b4-39bd-a1ef-21df26b2a30f | -23.66205 | -53.55989 | 2025-11-29 12:59:00 | TERRA_M-T | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| 9e3e724a-1a7e-37d3-a525-e14834d6f37e | -20.18031 | -52.3717 | 2025-11-29 12:59:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 063fa76c-c613-3b2a-be8e-3f2ce995b108 | -20.45203 | -57.91985 | 2025-11-29 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| e2658642-5802-3759-964c-4509315511d8 | -15.57907 | -60.11419 | 2025-11-29 12:59:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 278d4bae-d3ff-3953-b18f-b470b72b6dc2 | -20.1813 | -52.3754 | 2025-11-29 13:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 5f5728e0-babe-3a0a-a900-9fde4cb5150d | -25.75123 | -50.77739 | 2025-11-29 13:01:00 | TERRA_M-T | RIO AZUL | PARANÁ | Brasil | 4122008 | 41 | 33 | nan | nan | nan | Mata Atlântica | 53.1 |
| 3a7446bf-dc4c-3f99-ac5a-c2658812d894 | -20.1813 | -52.3754 | 2025-11-29 13:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 134.8 |
| b7294990-23d6-3e60-9526-b9d5c4c5fb7f | -17.4954 | -57.133 | 2025-11-29 13:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| d4edd024-da11-3d3d-9686-8bfc163c201d | -20.1813 | -52.3754 | 2025-11-29 13:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 145.1 |
| a93c5525-4157-3572-a0af-697609db6101 | -20.4076 | -57.9577 | 2025-11-29 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 2645a0a2-0d3c-3bc7-aa59-985e49932199 | -20.1813 | -52.3754 | 2025-11-29 13:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 84faa38c-db60-306e-84db-da05b5407bf7 | -20.4073 | -57.9786 | 2025-11-29 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 8f0c41de-db65-351d-8c38-61f709ea394f | -4.966 | -41.1881 | 2025-11-29 13:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| e21b6caf-2353-39c2-8e7b-fd315c6eb156 | -17.4954 | -57.133 | 2025-11-29 13:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 190397a0-ee46-3cd9-b109-edb35182eca6 | -20.4279 | -57.955 | 2025-11-29 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 3658be2c-f1e1-39f2-821f-ad0e6e992803 | -20.3874 | -57.9605 | 2025-11-29 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| fd5bb28a-3132-3da7-84e3-eae8fe283ef5 | -20.4485 | -57.9313 | 2025-11-29 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 2ecfc58d-1139-3123-ab27-37f84305e4be | -4.9662 | -41.1639 | 2025-11-29 13:40:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 117.4 |
| 7c168c15-bbd5-3147-985b-8841101ebf4d | -17.4954 | -57.133 | 2025-11-29 13:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| a55d8291-befa-3187-96d8-d7ca0c706f65 | -4.9472 | -41.1895 | 2025-11-29 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 19064716-56a0-3b75-ae6d-8775d8474c4f | -20.3878 | -57.9396 | 2025-11-29 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 0e1f62fb-9eb4-3412-92e2-1c9b6d3c3f09 | -4.966 | -41.1881 | 2025-11-29 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 19824180-7106-314a-889d-b3d01550e361 | -20.1813 | -52.3754 | 2025-11-29 13:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 154.8 |
| c1c80cf9-8ef1-3ca1-8d3e-bd4460b74034 | -6.5344 | -38.8736 | 2025-11-29 13:40:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 0e8e6d9c-b12a-3568-afee-535ea6e60827 | -20.3878 | -57.9396 | 2025-11-29 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 0d86f54f-b378-32ed-84a7-ebda4de23b0d | -20.4073 | -57.9786 | 2025-11-29 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 7c1c2d3f-4b1b-3ca1-a9fc-625f98928250 | -20.4076 | -57.9577 | 2025-11-29 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.7 |
| b91994a0-686b-3d22-b984-0d168d64521b | -20.4279 | -57.955 | 2025-11-29 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| c300d0d2-853d-35ed-a366-aefd209791f1 | -20.1813 | -52.3754 | 2025-11-29 13:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 1e11ea1f-a287-3535-8aa6-0d0df9bc4f05 | -20.3874 | -57.9605 | 2025-11-29 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.8 |
| ef2f4338-dc8c-36a1-a16b-f12b8718d65d | -17.4954 | -57.133 | 2025-11-29 13:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 3fbbcae4-0006-3cd1-a00f-f374f518a68c | -20.408 | -57.9368 | 2025-11-29 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 4a66e307-fe22-3823-a4e6-e3bd4ac4a64f | -20.1813 | -52.3754 | 2025-11-29 14:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 134.6 |
| cbc11aab-183a-3f67-97f4-293acc9b198f | -19.8937 | -57.4441 | 2025-11-29 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 231f994a-1180-36f1-91be-8cafc46133cc | -17.4954 | -57.133 | 2025-11-29 14:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| c0105759-e20b-3501-9612-4afba8370ce2 | -20.3878 | -57.9396 | 2025-11-29 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 7e8e678d-30bb-30da-89ca-1c10b5fc8754 | -20.4283 | -57.9341 | 2025-11-29 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 69681a06-a2e7-32dc-8010-d871155ae731 | -20.408 | -57.9368 | 2025-11-29 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| fbfc1cb4-786c-37ac-9a99-332265d33496 | -20.4489 | -57.9104 | 2025-11-29 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 9071e94c-f346-39e3-9c39-7b0c836c5767 | -20.1813 | -52.3754 | 2025-11-29 14:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 144.3 |
| f9fed8a4-e2c5-321e-a1e3-3644a4f3dcc3 | -20.4485 | -57.9313 | 2025-11-29 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.7 |
| ca8183e2-5f77-3bb6-bbf4-bbc0c754b3db | -17.4954 | -57.133 | 2025-11-29 14:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |


