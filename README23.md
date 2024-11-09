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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4573b6b-4288-3af8-943e-8e992d9f5613 | -11.1073 | -43.319 | 2024-11-09 03:50:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 4213e7a0-9855-3563-b5ca-eb48bac49924 | -11.0877 | -43.3456 | 2024-11-09 03:50:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 209.4 |
| e7a469a1-1b7e-3d06-929b-3b9076287b7a | -2.2318 | -46.5508 | 2024-11-09 03:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| ccb732c0-ddba-3324-a735-52f8c4c85fb5 | -3.9668 | -48.1932 | 2024-11-09 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 476138b5-8026-30cb-8a50-07b4c9384b61 | -3.6003 | -47.3614 | 2024-11-09 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 415b49a3-0681-322a-97a7-24b51525b002 | -3.1327 | -52.9736 | 2024-11-09 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8d3c2d00-0f2d-32e6-bde6-fbe20c9db071 | -2.2479 | -53.7627 | 2024-11-09 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b27d1bc0-3ba8-3911-be83-f7face0be27d | -3.5819 | -47.3403 | 2024-11-09 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| b4c71b97-de87-34b2-9244-699f817b631a | -11.1068 | -43.3428 | 2024-11-09 03:50:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 33aa6dd6-6615-36db-9e43-860f73fd987e | -3.6004 | -47.3395 | 2024-11-09 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 199.1 |
| 4213268b-2692-382e-8dd8-19fe16326f5d | -10.2198 | -36.2621 | 2024-11-09 04:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| df251273-2328-3c5c-954f-ceb8c3b38d24 | -3.1511 | -52.9731 | 2024-11-09 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 18576d79-afd7-3b26-836f-71d1f72b4f50 | -11.0881 | -43.3219 | 2024-11-09 04:00:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| b9494c0b-8d10-3a69-93f0-3fe3d8f4ac8c | -11.1068 | -43.3428 | 2024-11-09 04:00:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 12b64926-9e51-3220-bbc5-f03f98a18e72 | -3.967 | -48.15 | 2024-11-09 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 208a332b-7801-361a-af11-894856c277bc | -3.5818 | -47.3621 | 2024-11-09 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8282eec0-fba9-3e16-8af4-ba7178d2a2b0 | -3.9853 | -48.1924 | 2024-11-09 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 989e6c1b-4347-32b2-955f-584f4b89292f | -4.2486 | -47.5729 | 2024-11-09 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 0770942e-2dc9-336c-b018-5d76eac3ebf5 | -3.9669 | -48.1716 | 2024-11-09 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 210.7 |
| d21a282f-38d0-3b1a-953a-aefa2659c115 | -10.2203 | -36.235 | 2024-11-09 04:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 108.6 |
| c55c3b27-56e3-318a-9393-8037f3168c72 | -1.5163 | -52.1901 | 2024-11-09 04:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| e573bed9-072a-3b30-814a-262257f5719b | -2.6764 | -51.8189 | 2024-11-09 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0efadabe-9298-3ce2-a03c-10ef9ed6fc2e | -4.2484 | -47.5947 | 2024-11-09 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 842c3278-f7e5-314c-9e11-a4f79959588e | -3.735 | -54.2292 | 2024-11-09 04:00:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8d4dfe25-c31d-31e8-8c44-a67121f60421 | -3.9668 | -48.1932 | 2024-11-09 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 25d45dfe-979c-30af-8026-8b16ef4d2c34 | -3.6003 | -47.3614 | 2024-11-09 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 7248cedc-7c17-37ab-b6cd-e2eafd840752 | -3.9854 | -48.1708 | 2024-11-09 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| f6c7e637-afff-3e3f-bdf5-e1b419331fc4 | -11.0877 | -43.3456 | 2024-11-09 04:00:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 493a0796-fa4a-350b-b280-a3ade276fa48 | -3.0865 | -50.5625 | 2024-11-09 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1ae1b56e-3911-333e-8b82-0ab6e965ef85 | -3.5819 | -47.3403 | 2024-11-09 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| ae655f65-efcd-3d6b-909e-92ffde432743 | -2.2318 | -46.5508 | 2024-11-09 04:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 75542629-b4c3-3b2f-92cb-36bcfeb389c0 | -3.1327 | -52.9736 | 2024-11-09 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 000877e4-61ea-382b-a62d-ce174184a9ef | -3.6004 | -47.3395 | 2024-11-09 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 191.0 |
| 1f6721b7-122e-3caa-a8db-46f83d64c44c | -2.2479 | -53.7627 | 2024-11-09 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 719c50cc-2b58-39c9-9da4-074cf5bda8a3 | -11.09 | -43.36 | 2024-11-09 04:00:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2557ed8d-6fce-3e4a-a3a6-7656e9efb8c4 | -1.5164 | -52.1696 | 2024-11-09 04:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 79fa2984-211c-3ce3-b356-fbe3f4011dca | -3.9668 | -48.1932 | 2024-11-09 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| db2e091d-5843-334b-846e-192a465a818f | -3.9854 | -48.1708 | 2024-11-09 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 430df817-c805-3399-a8be-2600b1063647 | -2.4104 | -48.5265 | 2024-11-09 04:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| a2304080-9934-3dcd-a7ce-8595f40d57c6 | -3.5819 | -47.3403 | 2024-11-09 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| eeb0f069-8d59-31b2-a732-6022f29fa5e8 | -3.1511 | -52.9731 | 2024-11-09 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d7915eb1-25c5-3d35-8f10-eeaf2bd64c49 | -3.0865 | -50.5625 | 2024-11-09 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| cafe5a45-af62-3111-bd72-b234f626dbd2 | -2.2295 | -53.7631 | 2024-11-09 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a4419455-bfe2-3e05-989e-03db3813c8c1 | -4.2033 | -45.8538 | 2024-11-09 04:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c63be0b8-5bd4-32bf-b0d3-e9a481a41a42 | -2.6764 | -51.8189 | 2024-11-09 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3cc91d52-5a47-30df-9f8b-74626b645669 | -11.0877 | -43.3456 | 2024-11-09 04:10:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 8a9ee52f-efbc-3299-b155-079f6e6c3841 | -3.6004 | -47.3395 | 2024-11-09 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| bacb2325-5111-361e-ac71-bd2503f4edad | -3.5818 | -47.3621 | 2024-11-09 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| dc197b97-bae2-3dd7-991b-a6ab92ae0a70 | -11.1068 | -43.3428 | 2024-11-09 04:10:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 155.5 |
| 55726e2d-b62d-3e83-a82c-208785e6ab55 | -3.6003 | -47.3614 | 2024-11-09 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 7fb07b0c-b2c8-3ca4-939b-89fe89936719 | -4.2486 | -47.5729 | 2024-11-09 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 41f482af-29ca-30b0-8718-a4d9e7ae26e1 | -11.0881 | -43.3219 | 2024-11-09 04:10:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| dc333b73-9113-3de8-93c3-c84c8a89ce87 | -11.1073 | -43.319 | 2024-11-09 04:10:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 94.9 |
| ae4e79d6-a0c5-3701-80a9-7ee5b6590bc0 | -4.2671 | -47.572 | 2024-11-09 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 09a70924-58bc-3569-bba6-56a34c17cc92 | -4.2058 | -48.5491 | 2024-11-09 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 632e6128-1290-3b53-b995-66c3e33654d6 | -3.9669 | -48.1716 | 2024-11-09 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 217.9 |
| 32a700f5-1e08-3a30-ace7-55d9e7203079 | -2.2295 | -53.7832 | 2024-11-09 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c7ad61e6-2f19-3df5-afd2-e0055da21eb0 | -3.9853 | -48.1924 | 2024-11-09 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 1135978d-fee6-34d0-b8bc-12fff3dd1d45 | -3.5819 | -47.3403 | 2024-11-09 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 2739f6df-7f0f-33d3-9a54-d3c970c43b3d | -4.2058 | -48.5491 | 2024-11-09 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4a6a6421-a373-3e3e-80c7-51dacd5ff7c9 | -4.2033 | -45.8538 | 2024-11-09 04:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 11304d4e-51e9-32f0-b75f-14416249963c | -4.2486 | -47.5729 | 2024-11-09 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 179.2 |
| a4f265c9-a95e-386f-bc4c-877f251f8e34 | -3.0865 | -50.5625 | 2024-11-09 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 7c68e1cc-262a-3351-b037-3b2bf4f0357e | -3.9668 | -48.1932 | 2024-11-09 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 9c874d95-4211-3eef-94dd-d59a7c5c3f08 | -4.2484 | -47.5947 | 2024-11-09 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e9334a97-7ed1-3105-ba7d-b729bb0645a2 | -3.1511 | -52.9731 | 2024-11-09 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 00eb6ea9-17bc-35ae-ba2a-5104e92d0f89 | -3.6003 | -47.3614 | 2024-11-09 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 1eb3e3f3-0c42-37d6-a19a-96f0c4b09f3d | -11.1073 | -43.319 | 2024-11-09 04:20:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 76.6 |
| b9d5573c-3165-3621-b234-83d0798a997c | -3.9853 | -48.1924 | 2024-11-09 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 5dd41168-3a10-3074-a032-1ad4797eb290 | -11.0877 | -43.3456 | 2024-11-09 04:20:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 226.4 |
| 896c7da6-8d09-372e-859d-3b1c5e667a0e | -3.1327 | -52.9736 | 2024-11-09 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 261f9002-3c96-3444-b3b4-3c0178d1a63e | -2.2479 | -53.7627 | 2024-11-09 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2e9ba1db-5125-3b56-85dc-7fd24d213bc0 | -3.9854 | -48.1708 | 2024-11-09 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 55127d73-b423-3683-b749-335d16155722 | -4.2487 | -47.5511 | 2024-11-09 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 92994e7d-1849-377d-9a4c-85112588272b | -11.1068 | -43.3428 | 2024-11-09 04:20:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 0f5af2f0-c63b-3c67-996e-58e7d443b2bf | -3.9669 | -48.1716 | 2024-11-09 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 224.4 |
| 272c5676-c49f-3ef6-ae32-c9db8843201c | -11.0881 | -43.3219 | 2024-11-09 04:20:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| ed0015d9-1087-3ad3-93c0-ee7b0e2535d8 | -3.6004 | -47.3395 | 2024-11-09 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 5154dc98-f150-37d4-ac95-1efcebd3b266 | -2.2479 | -53.7829 | 2024-11-09 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 1462df25-d97c-324c-8fd6-95c933d563de | -11.0877 | -43.3456 | 2024-11-09 04:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 56b0b104-4e74-36e3-bbe8-725c4c29f54c | -4.2486 | -47.5729 | 2024-11-09 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 208.7 |
| bc07fa8c-402a-3625-b4b1-b874081b0798 | -3.6004 | -47.3395 | 2024-11-09 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 257f8052-635c-3adc-9083-418c95f3c599 | -3.0865 | -50.5625 | 2024-11-09 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| f560781f-e159-38db-8732-353d62de4665 | -1.5163 | -52.1901 | 2024-11-09 04:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a2648319-7f30-3061-a81c-6f3bd56edc7a | -4.2032 | -45.8762 | 2024-11-09 04:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 546e7fd0-f5b0-3881-843b-ba763064294e | -4.2484 | -47.5947 | 2024-11-09 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 030f7848-cf9e-326f-8f13-bb25b392a3f2 | -4.2219 | -45.8529 | 2024-11-09 04:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 9cdb9335-ded4-3d84-a936-7e349397f203 | -4.2033 | -45.8538 | 2024-11-09 04:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 26ac5ef3-3b31-3ccd-a6b0-af72f54fca93 | -3.9669 | -48.1716 | 2024-11-09 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 218.2 |
| dbfe90c3-c393-3819-abba-70ef5ceac504 | -10.2203 | -36.235 | 2024-11-09 04:30:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.9 |
| 7c0e5175-ea62-33e0-a3d9-7b542c7ac783 | -3.6003 | -47.3614 | 2024-11-09 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 5f3a4578-d4e2-304a-8f65-377aad585213 | -3.9853 | -48.1924 | 2024-11-09 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ab499519-bb2f-3224-b21a-89c437be18a9 | -11.0881 | -43.3219 | 2024-11-09 04:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| d96e8c09-2c09-3875-8160-95c561be39a7 | -3.5818 | -47.3621 | 2024-11-09 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 68418038-79dc-38fa-808a-1c4242a629cd | -3.9668 | -48.1932 | 2024-11-09 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 173.4 |
| 6b9a80c7-ffb7-352a-8f41-03cac0522fe9 | -3.5819 | -47.3403 | 2024-11-09 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| ec458379-3215-3a73-9865-288c06721f87 | -11.1068 | -43.3428 | 2024-11-09 04:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 01c98a4a-4e24-3a58-aa71-32c46e07240a | -2.2318 | -46.5508 | 2024-11-09 04:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 8bc4eeaf-970f-3b97-98f9-0c12c0571999 | -4.2058 | -48.5491 | 2024-11-09 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 5a6f6710-bce2-3c26-ba17-8830c15b1bf3 | -3.9854 | -48.1708 | 2024-11-09 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |


[Clique aqui para ver as próximas entradas](README24.md)
