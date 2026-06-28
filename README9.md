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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49de0ead-0fbf-3914-99cd-e6cbb34943e0 | -12.092 | -52.0176 | 2026-06-28 03:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 511e30cc-5c04-3dd0-aaf2-bda745174e32 | -12.1937 | -52.8866 | 2026-06-28 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 8789563b-0c30-358b-9ee8-d90954842f39 | -12.194 | -52.8657 | 2026-06-28 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 2ff0e2a1-e1fe-3cec-afa3-ee0feb5706a6 | -10.2942 | -57.1182 | 2026-06-28 03:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6d6dd071-2c6c-31c8-adc4-fd600fd2620c | -17.3034 | -42.6678 | 2026-06-28 03:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 69a1d65c-2f7e-3c1a-9be8-06565e490e76 | -12.4651 | -58.5009 | 2026-06-28 03:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| ee4b4fc6-eb20-3f21-b48b-2494d12a148c | -10.3128 | -57.1367 | 2026-06-28 03:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 9e3cad32-0e8f-3eaa-8135-94a68642d026 | -11.2279 | -54.3036 | 2026-06-28 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| ebe43fc5-c0d5-36da-9d5f-bb1b9c9d862c | -12.1934 | -52.9075 | 2026-06-28 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 8c224a32-ad1f-3155-9d52-c73dbd5f4d13 | -12.2128 | -52.8846 | 2026-06-28 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ba9038b0-e5c5-3258-8191-d81877789927 | -10.313 | -57.1169 | 2026-06-28 03:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 07ee2704-e46e-327f-b4f0-a0ff2237f766 | -11.60818 | -43.1097 | 2026-06-28 03:17:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 528a9f24-e177-3186-a075-ce715843fedf | -11.60932 | -43.11699 | 2026-06-28 03:17:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d4802a21-c528-3f05-a4a5-b32a7ad66b04 | -11.60389 | -43.10945 | 2026-06-28 03:17:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4fadc75a-b7b7-302b-85d3-b360fb8e4473 | -11.60694 | -43.11584 | 2026-06-28 03:17:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| d33a7687-8d71-32a9-ad40-c3b53daf23cc | -11.60261 | -43.11558 | 2026-06-28 03:17:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 388d2d47-6b7a-3c6d-8598-61b93b2153ff | -11.6106 | -43.11086 | 2026-06-28 03:17:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| da028d7a-636b-3ada-aae0-88d205a14e6d | -17.97292 | -44.56712 | 2026-06-28 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08bf712b-e875-3f5d-9c59-43ccde802a9a | -17.30402 | -42.65621 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 665666cd-cd74-3659-96df-5c55d62f90de | -17.49557 | -39.45267 | 2026-06-28 03:19:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e5149eab-fc13-34d1-8ede-b393bda32943 | -17.30987 | -42.65781 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| aa4d26a1-bef8-35ae-a859-60d01d8a40c9 | -13.29327 | -43.55046 | 2026-06-28 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f42bcf7-80c9-3f9e-9db2-5ec3ec7fd894 | -17.34638 | -42.63241 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8245c8ac-c021-3833-80ea-30f8a9fe7dbd | -17.31306 | -42.65579 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0c353a14-49ce-3eb4-a259-39442b72633a | -17.3082 | -42.64953 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c682a3a9-09e9-3e74-b0d0-468d79c0d3ae | -17.35326 | -42.62918 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01f38944-9e19-313c-b673-5799b431c9da | -17.30722 | -42.65416 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 45.5 |
| e23ba168-4168-35f9-8903-b0d57dbe7662 | -17.34738 | -42.62781 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f811d9d2-36be-3a93-a7ac-3ba1403711c1 | -17.30621 | -42.65889 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 45.5 |
| faf18123-dd9c-3c37-92e6-0c7400652a26 | -17.31089 | -42.65316 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 30a212ec-964b-3f18-9326-caae07d7cc43 | -17.30296 | -42.661 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3bf61d53-0300-3bc9-955e-43d27de4ccdd | -17.30504 | -42.65157 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| f40db45c-8dba-3145-b56b-61ae02812c89 | -17.30521 | -42.66359 | 2026-06-28 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3e67b11b-45b1-3fcc-9ef0-d9bcd8cb8321 | -10.313 | -57.1169 | 2026-06-28 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 9f8a5bee-84be-3533-9ba7-1a4fb2303cc7 | -10.2941 | -57.138 | 2026-06-28 03:20:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ff899667-9dec-3b43-86fc-23ad25cdf63b | -12.4651 | -58.5009 | 2026-06-28 03:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 69374944-991c-3ba1-a8f0-8856cc09eea1 | -12.2128 | -52.8846 | 2026-06-28 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 3d34ada4-00a7-3b0e-a252-02a1aa8e4c91 | -12.6048 | -57.8743 | 2026-06-28 03:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 92f18a65-bdfe-3927-b78a-65f40a326707 | -12.092 | -52.0176 | 2026-06-28 03:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d72bd140-ab09-379f-8e35-54b72b7efa97 | -12.1934 | -52.9075 | 2026-06-28 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 42b031be-3115-3435-b631-090e00383d10 | -12.1937 | -52.8866 | 2026-06-28 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 143.8 |
| c86ec26c-2c26-3176-85f1-5ed32e7fbd8c | -11.209 | -54.3053 | 2026-06-28 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 572768b1-5fce-3bf9-b856-c042c41af182 | -12.1747 | -52.8886 | 2026-06-28 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| fa550103-5647-3e51-8525-f6266799cdf1 | -12.2131 | -52.8637 | 2026-06-28 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 57552f7d-5567-3ffe-a9c4-7e3736c80179 | -11.2279 | -54.3036 | 2026-06-28 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 03a3e04a-674f-3909-8fb6-23f0a294bb17 | -12.194 | -52.8657 | 2026-06-28 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 5d1deeb1-3dcf-348a-a9e7-6c1c6b64b4ca | -10.3128 | -57.1367 | 2026-06-28 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 4d5d181b-6d0e-3f82-b943-083e32ef5453 | -17.3041 | -42.643 | 2026-06-28 03:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 54ecd275-4b62-3a88-b03d-f9f502c1028c | -20.39544 | -45.27635 | 2026-06-28 03:21:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4bdc7555-9021-337f-a3b6-c4a4e8ec056a | -11.2279 | -54.3036 | 2026-06-28 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 74dd720e-3efa-3340-915a-d5c319ae7e56 | -12.4651 | -58.5009 | 2026-06-28 03:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 0ef8b8e3-5af0-3124-9ff3-0b760f08189e | -11.209 | -54.3053 | 2026-06-28 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| fc837a89-5f2b-3e92-a07e-6e0ba239026b | -10.3128 | -57.1367 | 2026-06-28 03:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1ca03b4d-2455-30c4-b442-99ee6e653971 | -12.1934 | -52.9075 | 2026-06-28 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 38044a90-c832-3856-8c86-6f16d012f381 | -12.1937 | -52.8866 | 2026-06-28 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 803383b7-c17d-396b-905b-b81649f175d2 | -12.092 | -52.0176 | 2026-06-28 03:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 97b9cf3d-3f78-3d46-8cb2-6b6e9e989dba | -12.2131 | -52.8637 | 2026-06-28 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 9a61a26d-67c0-39ea-8a43-fb1c61429e41 | -12.194 | -52.8657 | 2026-06-28 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 290f849a-4ab2-3c1d-a360-67dfad8f2a0a | -12.2128 | -52.8846 | 2026-06-28 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 46343e9f-15cc-32c2-a090-25bf9b928f13 | -10.2942 | -57.1182 | 2026-06-28 03:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3bd2f437-f9f9-3fc9-b6e3-bb729d76822f | -10.2941 | -57.138 | 2026-06-28 03:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b09cf7ca-6fe5-3211-864b-184c8214d446 | -17.3041 | -42.643 | 2026-06-28 03:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 07804a26-3863-32a4-8369-81dc3991c7d9 | -10.313 | -57.1169 | 2026-06-28 03:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 58dcfb12-2457-373c-a999-c2f378235b23 | -10.313 | -57.1169 | 2026-06-28 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 485fd7d8-af3f-3356-877f-8f4cb2b671f9 | -12.1747 | -52.8886 | 2026-06-28 03:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| dc0afc56-a89a-3097-90c0-619a70f1f821 | -12.194 | -52.8657 | 2026-06-28 03:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| e40a6def-9354-3d7f-98f9-d34aae1369c0 | -12.2131 | -52.8637 | 2026-06-28 03:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| f38dce14-1c9e-3f95-b733-18d98b477f18 | -12.1937 | -52.8866 | 2026-06-28 03:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 94f5c8ae-a944-3212-a879-69cc4166fde5 | -12.1934 | -52.9075 | 2026-06-28 03:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 5c1b26eb-0f9f-310b-aa31-8e2ad87de1c6 | -17.3041 | -42.643 | 2026-06-28 03:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 3363f672-8cec-3d60-80a3-58796d93bc00 | -11.209 | -54.3053 | 2026-06-28 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 77bb695b-6c02-338e-83eb-60d5c774a5a6 | -10.2942 | -57.1182 | 2026-06-28 03:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8c1535ac-67d3-3cff-80d2-fd7391119c4a | -11.209 | -54.3053 | 2026-06-28 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 168.2 |
| 8bed9528-9703-3c25-ac74-3c22de1af7cb | -17.3041 | -42.643 | 2026-06-28 03:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| e3f5a51b-bb90-3e13-a692-d7b1aa6edad1 | -12.2131 | -52.8637 | 2026-06-28 03:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 503813c8-1ab9-336f-9af2-0781751b1c8c | -12.1934 | -52.9075 | 2026-06-28 03:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 25c62852-e98a-31a4-9fa6-845f54df4abd | -11.2093 | -54.2848 | 2026-06-28 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6f35a177-50ed-339e-848d-8bfcda94b7a8 | -12.092 | -52.0176 | 2026-06-28 03:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 392c768b-6fdc-3a17-9b58-f5d4bf69a10a | -11.2279 | -54.3036 | 2026-06-28 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 396d2514-6b1e-3125-913d-00928178c948 | -12.194 | -52.8657 | 2026-06-28 03:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 659ec61c-75db-3bc3-a42a-a8e4be7a8795 | -10.2942 | -57.1182 | 2026-06-28 03:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| af9597b5-1ce2-34d3-9d18-2608628c0167 | -12.2128 | -52.8846 | 2026-06-28 03:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 1bedd1ed-646d-37b5-9317-4e70fa7dcb18 | -12.1937 | -52.8866 | 2026-06-28 03:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 7f2d81cc-4318-323e-937c-aa317ebf97e9 | -10.2941 | -57.138 | 2026-06-28 03:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 096244fc-ef3d-301a-948f-f18d97dd5302 | -2.94987 | -39.92484 | 2026-06-28 03:51:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f7d50834-624c-33d4-b54c-b36cfe1e4f98 | -6.99786 | -45.01303 | 2026-06-28 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0a4a66cb-0e11-3eae-a419-d672817fff38 | -6.99852 | -45.00944 | 2026-06-28 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 03c1e323-2b15-3a4c-a2fd-34a00de99ff3 | -2.9546 | -39.92183 | 2026-06-28 03:51:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b937661b-b6a1-30be-a340-a9f57762131c | -6.99917 | -45.00584 | 2026-06-28 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 72720ee1-2bd2-3c8c-a683-8823302ce45e | -13.28875 | -43.54927 | 2026-06-28 03:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 455d5b50-f7e0-3d8e-8bca-8722fb16c940 | -11.91852 | -43.40502 | 2026-06-28 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beb83956-4a98-39c6-8633-f1d288314bfe | -12.26526 | -43.51889 | 2026-06-28 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9154d6ff-b9f5-3389-a83a-ae12e8dbf8bf | -12.26975 | -43.51978 | 2026-06-28 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38847aea-d5af-3033-b6ce-b8bf6da19fc7 | -11.60987 | -43.11088 | 2026-06-28 03:53:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 26880536-97a4-315a-a030-022cb87df439 | -10.84087 | -49.13297 | 2026-06-28 03:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8758e3a6-7611-37db-b7aa-59fdd9db237b | -13.29128 | -43.55264 | 2026-06-28 03:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 167ffc4b-49df-38b6-9e28-6e5a07f92dea | -12.27915 | -50.10823 | 2026-06-28 03:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a505139a-fede-34a1-82aa-c242c1c0e53c | -13.95225 | -47.34288 | 2026-06-28 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4555755c-c10e-3096-9106-c110d5498a3c | -14.04286 | -46.33472 | 2026-06-28 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c5cb89c-e5ce-3005-abb7-49e12c5317a8 | -13.88735 | -47.17608 | 2026-06-28 03:53:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README10.md)
