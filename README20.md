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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52ef8752-7a42-38cb-88c7-caf189a00fa4 | -10.16398 | -53.9264 | 2025-06-26 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6854c4c2-0dec-3cdb-ab20-c7c47a4afe5b | -11.81115 | -57.3481 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c94624b2-c69d-34e0-8064-72702ddb88fb | -9.7919 | -57.42023 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 849f9bde-ae3e-3234-898a-b6c329a261e9 | -11.06506 | -55.36923 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd63b1d2-2e6b-35ec-9147-5d76b6bc2ed0 | -11.84 | -57.86195 | 2025-06-26 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1209285c-0b5f-3c79-a364-0c4fbf16f81e | -10.83047 | -53.74002 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e14e4c8b-fa56-372a-a776-198fd3d72395 | -9.79135 | -57.42406 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4963b63a-2665-3453-a729-41b53661d52b | -11.57072 | -52.10281 | 2025-06-26 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b30158c5-04b1-368d-8e59-18adf89878b5 | -9.57605 | -63.20742 | 2025-06-26 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 70c2dd97-6f74-3c1f-bb9a-95c06902f96c | -11.13874 | -53.93776 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcdabbff-b6e8-36d2-bfdc-37cee5a3a105 | -10.30247 | -57.13336 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33b2c25e-95e7-397b-a362-8f4b4d12cf3b | -12.6178 | -57.8758 | 2025-06-26 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd233b49-2aa3-36f2-adfb-813a98287fc5 | -11.61518 | -58.28379 | 2025-06-26 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61265dde-c461-3831-856a-4dadecc10b6a | -11.06144 | -55.37216 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 65670355-1a74-3234-9af3-09d7132a48b6 | -11.82672 | -51.25338 | 2025-06-26 05:29:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80d9d51a-845d-3371-ad40-10e769b3f619 | -10.82703 | -53.74026 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5524f1e-5efa-35ed-87ae-7daebc4d3497 | -10.8279 | -53.73315 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e094f1ee-a39b-3ad9-ab07-3fa954f0fb8f | -10.82505 | -53.73937 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0efb1bb5-8b74-3f2b-9ca8-1fe92b98f6cc | -11.13557 | -58.61397 | 2025-06-26 05:29:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 972b1f50-582b-33d1-b5ad-6686430cde47 | -11.13166 | -58.61335 | 2025-06-26 05:29:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 157341c7-060f-3d51-9b6c-1ebc904453fb | -13.52108 | -56.57511 | 2025-06-26 05:29:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7797b685-b9f6-3e33-ac54-de5f7499c68a | -10.82204 | -53.73598 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8615050-8b58-33c1-b491-a5752cfca0c4 | -10.29765 | -57.13684 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f526115f-32b8-3086-89c1-151369c0f126 | -10.83094 | -53.7365 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 561e48e3-6463-3b48-a1e4-b9d3f088d44b | -10.30136 | -57.14147 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72e5d984-8a94-32a9-9ff3-1f87faca14e4 | -12.52739 | -57.18957 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ed3d9b8-0f5b-37d5-9761-314eb17d69e5 | -13.29487 | -57.08387 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57741240-cc4e-3024-b56b-5a35b61769ef | -9.06195 | -61.45656 | 2025-06-26 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 636ac2fd-a312-35b7-aef8-a4b5ac9063ac | -11.8321 | -62.76897 | 2025-06-26 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a77bf6ed-bb6e-3758-b90c-1cbd072aafbe | -10.82458 | -53.74291 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e5e2d68-8264-3841-92b0-9e1746552ae7 | -11.8057 | -57.3559 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c3c1e509-c88e-33d3-a809-331499820415 | -11.6192 | -58.28442 | 2025-06-26 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d073e08-021e-3ad6-812e-907b84416635 | -10.81962 | -53.73867 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b06ed0f4-344f-340a-aa76-23b563b410f0 | -11.5713 | -52.0981 | 2025-06-26 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5308b31-f6fa-3bda-a1fa-0071c4f35413 | -11.82706 | -57.76994 | 2025-06-26 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc3fdfa1-ab02-3efa-ab71-6a2e7c164321 | -11.06923 | -55.37534 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 726b6656-1586-3aea-902d-40dff412fcd8 | -11.06994 | -55.36983 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1d37ba6-8aa2-3cbb-8cf0-762bef4e649e | -10.87994 | -56.45396 | 2025-06-26 05:29:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0926ed85-5d2a-3f12-81c3-3d000a221d1e | -12.58578 | -57.3877 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42b10913-613b-3bf9-a802-489b8af26bd3 | -10.70523 | -59.1272 | 2025-06-26 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 754c2614-bceb-32ba-85e7-a4575f907f25 | -11.07409 | -55.37603 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 621ce8c8-c88a-3f04-b4ac-b2215781f314 | -10.87544 | -56.45331 | 2025-06-26 05:29:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c075c9c4-d8df-3442-81b6-8f25dffa22b1 | -9.92677 | -59.90374 | 2025-06-26 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 758bc898-af00-3375-bc6c-98f8c0083f63 | -11.56521 | -52.09733 | 2025-06-26 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b44dda3-dbe6-3b8d-8f81-c20b5952fea5 | -10.8201 | -53.73504 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a3f3647-97eb-3501-a5ad-e5c350c8a029 | -11.06365 | -55.38021 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 753d7981-0510-3ca2-a008-185748fc41eb | -10.30192 | -57.13741 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb5550cb-bad4-3260-a9bd-fc9fa30c4a7a | -12.02101 | -57.09094 | 2025-06-26 05:29:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f893fdfa-4cdc-3867-811e-f269bc538bb9 | -9.25363 | -63.29117 | 2025-06-26 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8a5f1c9-e3e2-3936-956c-5302948fa26f | -13.29282 | -57.0848 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bded905-9117-35e5-91f5-d87a8ac0ab73 | -9.79494 | -57.42852 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c41b8bfd-a6b7-34a0-a721-9bbb2e1782ae | -11.24131 | -49.49012 | 2025-06-26 05:29:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58a43de9-2d68-3bfd-b2fd-d870c9b90f85 | -11.82547 | -51.26416 | 2025-06-26 05:29:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 591cece4-ba71-3286-b04e-d53955d111be | -11.80627 | -57.35173 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df74dad9-59f5-3014-86de-ed7a1a8e1efd | -10.06618 | -55.55619 | 2025-06-26 05:29:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94b1b156-3340-35ec-887b-d3ec5f386c91 | -11.13895 | -53.91517 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35d1a238-8198-3947-91e5-24ec68a16d9b | -9.57991 | -63.20446 | 2025-06-26 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c549d18-47bb-3686-92bb-4d5fae99cef1 | -10.82116 | -53.74315 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36b10876-d3e8-39cf-911b-6982e8f1380b | -8.7238 | -64.15867 | 2025-06-26 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fed69d9-1a97-3634-a5e9-eae8a2737972 | -13.09922 | -52.29554 | 2025-06-26 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acb0c071-422c-34ea-bb4f-98dc596e4dc1 | -10.709 | -59.12782 | 2025-06-26 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86e1f105-d194-3775-99d9-1c684c263932 | -11.81057 | -57.35231 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2aa1164-dc80-3058-a37a-fe9657794c66 | -11.57121 | -52.10489 | 2025-06-26 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46a6144d-7053-3e5d-abcc-fc02c5ff6350 | -11.80586 | -55.07507 | 2025-06-26 05:29:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 764c52d9-9fc2-3516-a6d8-10f8f2353a7b | -11.13313 | -53.91784 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95a8f1ca-c1e3-368f-b7c3-6ea0c68c1e0e | -11.81 | -57.35648 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ab264ab-3176-3946-a952-9e06a50589da | -10.82551 | -53.7358 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d8dc647-2994-3e29-bdf2-774e53c77219 | -13.29616 | -57.09431 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6f45e81-34a4-3c6f-9a21-146dc25edc23 | -10.30303 | -57.1293 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e833af2-fc6b-3a1e-9db1-758aa8abedd9 | -11.82932 | -62.7649 | 2025-06-26 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cd3cc4d-b3a2-35a2-8f33-72a6210d2cb7 | -10.71586 | -59.13373 | 2025-06-26 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 714f8687-c208-3946-bf07-2c41852bff36 | -11.6035 | -55.53782 | 2025-06-26 05:29:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8bc43f0-81d9-39e8-ad9b-fe070b4c0112 | -11.83895 | -51.26049 | 2025-06-26 05:29:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46ae01fa-4a10-321f-8e14-a57fd945bde3 | -10.82834 | -53.72959 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8333358-5db5-3265-ab74-57c03c33253e | -12.61726 | -57.87977 | 2025-06-26 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7827134-5406-3de5-86bf-1492be5e0c12 | -11.56622 | -52.09468 | 2025-06-26 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44cf0b42-f5cf-33f1-b179-c053df1c88c1 | -12.02539 | -57.0916 | 2025-06-26 05:29:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e843ed66-555b-306c-a410-ad05e0a8fde2 | -9.25087 | -63.28714 | 2025-06-26 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17700575-b9b0-3134-930c-c6f00dd38d44 | -10.2982 | -57.13277 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3452abf8-42ec-3dd4-924e-95437e2f6c1e | -11.60835 | -55.53848 | 2025-06-26 05:29:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 13b38c96-b033-3814-902a-2db251b609a6 | -10.8748 | -56.45794 | 2025-06-26 05:29:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8389c0fa-dbea-36b5-ab7e-ace13f5a5424 | -11.13804 | -53.92212 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22a7022c-9545-33af-bcf3-acff8949cc15 | -11.91495 | -54.81577 | 2025-06-26 05:29:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0df713c3-f4c5-38a4-a1a8-01a182594b20 | -11.84052 | -57.85814 | 2025-06-26 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea7df611-e637-32b1-a3e5-70e5747892f7 | -11.06069 | -55.37762 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac9ee0bb-e8c0-3fb4-a5fa-f9ccd34ff157 | -11.14042 | -53.92421 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc19b519-c920-3316-8efc-e8b99ec9a81d | -11.14411 | -53.9385 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec64fda5-ed0b-31e5-86a4-a2d0ef3908dd | -12.02157 | -57.08666 | 2025-06-26 05:29:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19a6844c-78ed-3588-a2df-dbe3683d640b | -12.02596 | -57.08732 | 2025-06-26 05:29:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03886779-f527-3812-9576-8283c7538dd5 | -11.80623 | -55.07217 | 2025-06-26 05:29:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85d06adb-f3db-3934-8365-8d32f51472c8 | -12.61361 | -57.87519 | 2025-06-26 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f958f5ca-e90e-319a-b207-58b564c6d061 | -12.00593 | -63.35233 | 2025-06-26 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4691af88-c07a-3018-9202-fe30c21a5b56 | -9.79606 | -57.42083 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1fff9c9-547b-3827-bd92-8fb8b2a87776 | -11.05948 | -55.37405 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d024babe-64a8-38b2-a4c5-75034af4a26e | -12.59068 | -57.38413 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7e40c7e-b2a5-38bc-adc2-a971db8839cf | -8.72716 | -64.15923 | 2025-06-26 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbbfad76-6f70-36ef-a7be-89af75177aac | -11.06672 | -55.07244 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a09261c-887d-3b34-8956-371e5d790278 | -11.91572 | -54.80967 | 2025-06-26 05:29:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67c3febb-5b24-3f0e-9414-d3c54056a0b7 | -9.7955 | -57.42469 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc512115-0731-3b52-8904-e471e5d10d5b | -14.90796 | -54.32813 | 2025-06-26 05:29:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)
