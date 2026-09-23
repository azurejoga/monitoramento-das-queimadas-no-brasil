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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fddca632-c839-397a-8ee0-28edae6a8c72 | -13.19068 | -51.56479 | 2026-09-23 05:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa028917-86f2-3b14-ab9f-082114933a56 | -14.63135 | -45.64334 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dad30fb9-872d-3f38-bf74-9de9bcdee751 | -14.40724 | -42.10847 | 2026-09-23 05:06:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2234c8b6-885b-33af-91ba-542c1fbebb16 | -14.6252 | -45.64935 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb77e522-eea6-35b7-9907-c0e299a69773 | -14.62169 | -45.63562 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d29d4574-3852-3c72-b5fe-29c9ba0d0cda | -14.69127 | -45.58456 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aba0abdb-d47a-3bbc-8610-45e42f809b31 | -13.70511 | -48.78833 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c6baf9f-2ed8-3c0d-b887-1701d43a7797 | -14.63429 | -45.66341 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b829855d-3c4b-3627-b5e9-ffdb5f88f18f | -14.6358 | -45.65049 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76da7c0b-f139-3a55-838e-8040f9893342 | -14.63041 | -45.64998 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57997951-f61d-336b-af04-0de87bb6dc12 | -14.69574 | -45.59159 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 61ed2e67-ecc7-3aa5-b98b-954b5b43c147 | -13.1876 | -51.56581 | 2026-09-23 05:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 223e7cc4-d844-3147-b43d-cba5298a016b | -11.99471 | -52.46357 | 2026-09-23 05:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1abe4670-4a28-33c5-883e-2cc0cbb2ef7f | -14.71096 | -45.59734 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08d21da0-6808-3b61-9986-644bc1c79916 | -13.93166 | -47.85181 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a6d36e3-7f2c-33e9-bb1a-1ee244f956a5 | -14.60597 | -45.63385 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 937b62cb-69a1-3ea0-b628-65032e1d0252 | -14.61598 | -45.63841 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f9fa43e-3945-307c-a505-d864dbc6cbd6 | -12.07315 | -50.05215 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 154e6272-e081-3152-b812-837085147059 | -15.64788 | -43.52843 | 2026-09-23 05:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2df66e0-8b13-3f49-a4f9-6dd627935c7e | -12.41132 | -46.98457 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef5aad3c-2f47-3f4e-bcbd-1116c5ba9873 | -13.02031 | -48.64326 | 2026-09-23 05:06:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad19e043-7e6f-3583-906e-cfafa86ef77b | -13.45666 | -46.27119 | 2026-09-23 05:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44918b1c-e23a-3423-93ae-8f7196816cca | -12.53983 | -50.06994 | 2026-09-23 05:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa01128a-6152-33b8-98f6-fe8a6948b4ed | -14.63081 | -45.64673 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6658df0b-8c57-362c-a162-2928506b4488 | -13.19174 | -51.56233 | 2026-09-23 05:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0a686b-2cac-3c5b-b161-0050800d1f7e | -14.63 | -45.65321 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3db19e2c-dc92-346d-97a1-d983e2d8c155 | -14.62119 | -45.63906 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6db2630c-9d8f-331c-9c25-3711d2f1f797 | -14.63619 | -45.64717 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9d95565-e924-3fb8-bc59-e774fc52af7e | -12.40929 | -46.96476 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e42b00a-e78f-3ba6-b4b0-90c38e9659c4 | -14.59595 | -45.62937 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 85ef269c-2912-3ff2-bd69-fbfaf53bebe8 | -12.53606 | -50.06936 | 2026-09-23 05:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8d3c303-2712-3bf1-9158-df7825db3fd7 | -14.61158 | -45.63124 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 464c0871-06b2-302d-814e-1b334ff1f345 | -10.65998 | -58.75755 | 2026-09-23 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c98804f-7f8c-3dc7-b89a-1b6d5b9cce7e | -14.61559 | -45.64162 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a343a64c-1c66-3278-b3c8-54507a56423c | -14.96813 | -47.54018 | 2026-09-23 05:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53b42fc0-f485-310e-b16b-c47e51fdda55 | -14.66439 | -45.58748 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66ac86d1-9b10-344b-a289-c3fac9840010 | -12.41787 | -46.97084 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 06f1f226-7a64-389a-85c0-7e3ec8e6bf27 | -14.664 | -45.59079 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39a92da7-dac3-3761-8992-0b395f4c4686 | -14.62056 | -45.64535 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1dbec83b-bc4e-3d54-bd73-2bae533c7bbe | -14.62881 | -45.66283 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc2e1405-cc81-3aac-b04f-69bb24feebad | -12.42247 | -46.9715 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d604da93-be2f-3c22-806c-534eb5d2a1a0 | -14.70133 | -45.58923 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5893146b-1cd0-3dc1-8cc3-c5a19abf12f6 | -14.71135 | -45.59417 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 533133ae-65be-3ecf-a06f-7e72b2e28df2 | -14.60518 | -45.64033 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1161a90f-c23a-3e0d-a9c6-9aaa73e2a63b | -14.62464 | -45.65566 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 475c892c-6e41-3854-bd80-a0910ff77b3a | -14.59634 | -45.62614 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cea8e01f-3296-3595-b0f5-2510fc9d3a93 | -12.42312 | -46.96671 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7d73c01e-593a-3a20-9eca-42332c86c820 | -13.92457 | -47.83741 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e8c01d2a-9556-36f6-b3d2-66cbd756a4bf | -14.96348 | -47.53995 | 2026-09-23 05:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afab39e3-d54e-384f-98b2-c97ba4b35b8d | -13.71393 | -48.78572 | 2026-09-23 05:06:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b717cc61-1bd6-39bd-b43d-52b3aef2d3a5 | -13.92517 | -47.83293 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4beca5e-0b46-3496-b606-9eaea4bca728 | -13.85548 | -48.59021 | 2026-09-23 05:06:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e3ed6d6-dd89-3efc-888d-8df9f8d8cd04 | -10.85111 | -57.15741 | 2026-09-23 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b822a987-df35-37df-bc89-0a8d11d1c01a | -11.96425 | -50.08494 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d28b884-c6d1-3298-b45c-2fe1e8ef4de9 | -13.05016 | -48.73256 | 2026-09-23 05:06:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7283680f-9f7c-3522-b200-41a1f903da0e | -12.41455 | -46.96062 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7190d8aa-9246-389d-9740-92e6e51a9da3 | -13.07068 | -47.41162 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ab9660d0-6159-3b44-8f80-92ca49c06dbb | -12.07601 | -50.08531 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fae9141e-eda2-3529-8309-27539a9f4922 | -14.63174 | -45.64005 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4265e61c-f58d-3e25-9352-4e0a7b54fbc4 | -13.50349 | -46.89218 | 2026-09-23 05:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bcc1a0ac-d27f-3220-a1ca-dd8ce3c4aa3e | -13.30531 | -47.89221 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bd05e82-5179-3e6e-9da0-cc391ae9c4ff | -14.6965 | -45.58521 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f276a95-546b-33ba-9350-a760f8366e37 | -14.29714 | -43.18837 | 2026-09-23 05:06:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 80f742f7-e0bc-357b-9a56-8877d2b68787 | -14.6248 | -45.65255 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 982b5269-40a5-3e00-bb31-8878e0ffc646 | -14.61639 | -45.63514 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 458f4953-76e6-3a5e-a649-45b0f229f914 | -14.626 | -45.64289 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e98b9c91-5ebf-3a28-8e69-1ed7d79608d3 | -14.70055 | -45.59569 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 761e07c6-689d-37c0-82d3-a0694a44420b | -12.32266 | -50.16002 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ddfc4b80-6eba-3ec6-9b56-cb7782c1fde8 | -14.6909 | -45.58767 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 05f58874-108c-3bf9-9bf0-84487be9bb0b | -12.4139 | -46.9654 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 52ec581a-d841-31a0-a93c-9393b28dec03 | -12.41916 | -46.96127 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92ee078d-1229-3da9-a45d-318ddef545ce | -13.29706 | -47.88701 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ff57749-dd64-3336-83be-f13386c31ecc | -13.86764 | -48.56356 | 2026-09-23 05:06:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ed4531a-44d4-32f8-94ba-cf34bf93dfbe | -14.59673 | -45.62291 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1121c035-9a3d-384a-8b47-c990206d3fde | -12.8021 | -50.91234 | 2026-09-23 05:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e2e6c72-c6d1-3292-80f1-185e37d570b3 | -14.61118 | -45.63451 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 852feb1f-9073-3106-b202-15e5237ae89c | -14.60037 | -45.63646 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42767ade-b8ec-3887-bad7-254dca0692ef | -14.59998 | -45.63968 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8713bbda-a274-3b6d-b2fc-c60ad97f71e3 | -12.40865 | -46.96954 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 854d75e1-c558-3246-b83d-c8bcf0c59a48 | -12.42377 | -46.96191 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a992b3b-bfc2-3b69-84a4-a1967fe31326 | -14.69612 | -45.58837 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 15bd5f19-2be8-3bf1-be02-f381b41bfbb9 | -10.65746 | -58.77188 | 2026-09-23 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84b55a7d-1ad5-3fc3-b1ab-305b706ba6d8 | -14.60637 | -45.63058 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2a46c8e9-a229-3760-9eba-4f29ffdfac72 | -14.69014 | -45.59403 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1bb8ab74-1073-37c1-9510-cbf1849ea281 | -14.29728 | -43.18944 | 2026-09-23 05:06:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| db157ef4-d959-3461-abbd-9d1f98d0f3d1 | -10.66151 | -58.77274 | 2026-09-23 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 463fbad5-dcd6-3936-a223-5729aaee8808 | -14.641 | -45.65117 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 394c34a8-58c1-319e-b0a1-e426d1a00ede | -10.65872 | -58.76476 | 2026-09-23 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 705181da-91e5-3e45-b54e-0f792add76d7 | -14.75407 | -47.15075 | 2026-09-23 05:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccfa74a6-5618-3a05-9093-c90f5f4179a4 | -12.32309 | -50.15757 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2caae731-b987-3c2b-85a6-7286e26259ff | -10.65594 | -58.75668 | 2026-09-23 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab31b190-32a2-3189-aec9-1daec7ae65b9 | -13.71296 | -48.79293 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62d470ae-4f75-3496-b249-707089cd72e4 | -13.30204 | -47.88311 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 167c1b2b-bdbb-31f9-ad75-a2620a78b103 | -13.8623 | -48.57138 | 2026-09-23 05:06:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd9926b7-d644-36a4-97bf-63737c1a1c9e | -14.75341 | -47.15579 | 2026-09-23 05:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98c812f6-409e-30e8-83f0-3e8302613f9d | -15.64837 | -43.52388 | 2026-09-23 05:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb4560b5-a431-3ce0-a180-c914cb9e9f43 | -14.63926 | -45.62091 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a94fa25f-77ee-398a-9e77-962a1357214f | -14.62093 | -45.64214 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c51f9adb-4642-348e-8744-372d0b7cdcdd | -10.87841 | -57.17574 | 2026-09-23 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1881320c-7e6c-3c5c-828a-bd94a8f17a61 | -14.96486 | -46.41908 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README98.md)
