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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a47ae65c-e21b-3a46-a1d6-c63b900fc96f | -17.81393 | -53.76674 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c861c8db-13a3-3f07-ae9c-7ac4844bdb2c | -17.81256 | -53.75343 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 239d9b72-e50e-39f2-ae51-3f0db3c7bf3a | -17.81182 | -53.75763 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3085a12-8463-39a6-b1ac-3ae70b741833 | -17.80826 | -53.75686 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 304762c4-3724-307c-bbe0-4b946397fdf1 | -17.80713 | -53.75373 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45a6dbfd-4d16-3a5a-bf29-ff6718b1a590 | -17.80287 | -53.75702 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f66a0411-cbe7-3869-ba27-59341f5818e8 | -17.79715 | -53.74722 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9c1cd97-c809-3389-bd67-77c9caf3e19c | -17.79356 | -53.74654 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab4de16a-b81d-3079-8ad3-9d54e73a6fb4 | -17.76597 | -53.12019 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 157f74a5-3d98-3b29-81c3-b597e0adbf06 | -17.7136 | -53.04028 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d02714d-8b01-3fc6-a0ac-4ed6eb551dea | -17.71292 | -53.04432 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f968f529-ea43-352f-af9d-63a89644b43f | -17.71162 | -53.03892 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7fe15ce-5cfa-3967-a0b8-a48742fade96 | -17.71092 | -53.04295 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6659e21-26d9-3f76-8480-802950687f44 | -17.71012 | -53.03966 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b91d8efe-77cf-37de-964e-dd5645896ddf | -17.70944 | -53.04369 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8fb38aa-51c7-37c5-a3a2-41834c116d29 | -17.70596 | -53.04306 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7129e73-49ff-36fb-b21f-58bd33cc4a9f | -17.70247 | -53.04244 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 550f02d1-69b8-3ee6-a9ba-6490d53d81bd | -17.69899 | -53.04182 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7080469-e78b-3d4e-ae8e-337d336f3796 | -17.6955 | -53.04121 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de3decd3-ca39-31b4-b6c4-d4fa8af1044d | -17.69202 | -53.0406 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31ab03c6-5044-3929-9825-a8864e50df78 | -17.68538 | -52.63811 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 561cc85b-300a-3929-8ec5-40d2c61f99ff | -17.68225 | -53.03468 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53bd3509-d93d-33db-b9b7-8df4cc94e8b2 | -17.67809 | -53.03806 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d61a446d-75d5-33bb-aef1-b428e1222e44 | -17.67461 | -53.03743 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6516a711-ab06-37b9-8541-73900cce4a3c | -17.6697 | -53.0241 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 54998fc2-fe6a-3f8a-9b66-d2be70eb60df | -17.66553 | -53.02749 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 53eff4cd-a92d-346a-a9c8-723056a966a1 | -17.665 | -53.0941 | 2024-10-08 04:36:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd4cde86-8f22-32e0-8034-d3f42c2e9863 | -17.6643 | -53.09818 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a39a9d7-3687-3a84-bb38-e7cacfc0fd18 | -17.66206 | -53.02684 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aa013bb2-0360-337c-939d-639712ed0337 | -17.66137 | -53.03086 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e578d0af-4ab6-357b-8f5f-18041d89dc39 | -17.6579 | -53.03019 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e3b0e4e2-782e-30e3-8c08-ba677dc847a2 | -17.65721 | -53.03421 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5f0dd29c-23a5-34ea-aa12-45083a513ed4 | -17.65374 | -53.03354 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 77b9c88a-b894-3ea1-8529-0b67d35c7eda | -17.81614 | -53.75414 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73f10f3d-dd0b-3926-9c56-18daa4938115 | -17.8154 | -53.75836 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bff3311e-46e6-33fd-b8fc-637470ca0b0b | -17.81071 | -53.75446 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41a084f3-517c-32c2-90b1-9fa035653644 | -17.81 | -53.75861 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7511ecb-d8e9-3cb4-92dd-e14740466b98 | -17.80643 | -53.75782 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2d29746-2793-32e5-956e-01d84fa98cc5 | -17.80617 | -53.74773 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db19c52c-a7b5-32a9-b527-3a7a0aa71c94 | -17.80541 | -53.75199 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95480e74-466e-31ec-b093-59709010d9d0 | -17.80469 | -53.75611 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9ad88b0-e756-39f6-9393-e517f88b995f | -17.80429 | -53.74875 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b165019-aefc-3e0d-bb4c-c90a6f27d55f | -17.80356 | -53.75296 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b14b85e3-e37b-3760-810c-005fa4dd0cd0 | -17.80072 | -53.74797 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 401f518e-5135-3958-ac03-d5610817c226 | -17.7691 | -53.75951 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff1c42b2-9c1e-3e26-a10c-4fd5182ddac7 | -18.54769 | -52.63847 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15f74bda-a233-3804-afd6-9f2e7a6b909a | -18.54494 | -52.63397 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 94c54612-ad14-35e4-b3b1-7e7547c50b05 | -18.54445 | -52.63464 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b7acb022-e8da-3f25-9206-38e68c2ac265 | -18.54428 | -52.63783 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 580e04a6-cdfc-33e2-bd84-c789f511e230 | -18.49832 | -53.45326 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9541d826-2ddd-3df0-9785-3ef8d9e4b892 | -18.49622 | -53.44429 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 78ca6844-129f-38dc-849a-516572984e29 | -18.49552 | -53.44842 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1a584301-fa13-3e6c-aba1-9c288d7260b3 | -18.49482 | -53.45255 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0dd1c4f7-4aaa-304e-8c75-d154de9f17e9 | -18.49342 | -53.4395 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 767e4d1d-c2f1-309a-92c3-532a87b9505f | -18.49272 | -53.44361 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 38c99731-510b-388b-9ce5-18f57a0d45d3 | -18.48781 | -53.45112 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f244381d-cace-3919-ad09-95e583f7978e | -18.48712 | -53.45521 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 22a84319-024b-3190-8012-1bbe81782273 | -18.4864 | -53.45939 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 81eb60a2-b5ca-367c-baa3-d5432b5f7003 | -18.48499 | -53.44644 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dc4d667f-4a70-3888-ac63-3bcddbec7ade | -18.48491 | -53.48935 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e425910-cfd8-3193-a570-2770ceca0e03 | -18.48429 | -53.45053 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b59da907-a0bc-3963-8f03-cd5a6af03f3d | -18.48359 | -53.45463 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 658b2d06-2f4e-31dc-92d4-78667fadfcea | -18.4814 | -53.48869 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf5993f7-6488-3373-9aaa-81c9c9087a64 | -18.4807 | -53.49278 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6c85ebe-5e04-3d54-9e7a-e35dd2986ba7 | -18.48 | -53.49688 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2158b513-accd-36ff-a094-e7a7525840a2 | -18.47929 | -53.50103 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe4ab4ac-fc74-34e6-b056-21d1994d94e0 | -18.42595 | -52.64949 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5c13eae-b829-3bc3-a33a-033d176ec80f | -13.2984 | -53.70591 | 2024-10-08 04:36:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acdf7b1e-ca0e-3ac8-b605-4ef0047aadac | -13.29378 | -53.70995 | 2024-10-08 04:36:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 807c8922-f1e4-33cb-821c-aab07593f520 | -13.28998 | -53.70923 | 2024-10-08 04:36:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc1ddc8e-903b-3b68-ab65-32d47e21eb25 | -13.28915 | -53.71399 | 2024-10-08 04:36:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15a0e9b9-460c-3dd4-b6b0-c8eae73629b9 | -13.28618 | -53.70854 | 2024-10-08 04:36:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c69acd88-ac9a-3734-a880-6c50c3bffa4a | -13.28237 | -53.70787 | 2024-10-08 04:36:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc06c2f0-13b3-34c2-81b1-3887c9077c7c | -13.28154 | -53.71262 | 2024-10-08 04:36:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 995b4a31-d1b1-353f-9965-c7dc7ba09bf9 | -14.83646 | -53.88566 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b281090a-fcd0-3e1a-9abf-d5db73715267 | -14.82813 | -53.88902 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f38bf281-f6c8-3751-a34b-7a6a3baf0103 | -14.82651 | -53.89839 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d1263a0c-ed71-304b-a37b-3bfd16034435 | -14.8103 | -53.92479 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08b5ebbd-c121-3969-8a3f-d8cf6b9e6599 | -14.8057 | -53.92891 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 120686f4-e6cf-307c-9a3d-e1f4eddd36eb | -14.80487 | -53.9337 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 525f443d-0773-3475-b183-68c4957302bd | -14.80109 | -53.93306 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f7553e9-f053-3d93-a895-f9b90c3a5e10 | -14.80652 | -53.9242 | 2024-10-08 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e57e03ec-317e-3868-a752-9ed7377d644a | -16.47523 | -53.9688 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 482bfe6c-068f-3634-9410-1a0b4212f16b | -16.46782 | -53.92492 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d23fb9cf-3629-3075-bc56-5d4bdb6d56b5 | -16.46663 | -53.91032 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 473675dc-0469-3ce9-93ee-41ca3085847f | -16.46581 | -53.91492 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3853b2d-4743-3328-bf62-3a73711aa136 | -16.46496 | -53.91964 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba88c2f6-b9cb-3cd2-b503-2c8aa5a8429c | -16.46279 | -53.91655 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbb332bf-2681-3b3e-b1a8-b1941dfec370 | -16.45831 | -53.92052 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b5674f8-818e-32e6-ba08-a4307dc27395 | -15.35894 | -53.72885 | 2024-10-08 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6abb14ce-6504-308e-bd36-e8060927fdd2 | -16.49892 | -53.96404 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a84d8e0-763b-3c72-af33-c41dcbab47a6 | -16.49604 | -53.95876 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01c8db18-5438-3b50-8c57-9078f27dc4a9 | -16.49077 | -53.96708 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9dd5120d-ab7d-3c83-b6af-3f4c7b0860eb | -16.48995 | -53.97169 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11afd677-386e-3017-9c7d-9f956893036f | -16.47686 | -53.91688 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9dd0a38-d04b-3fdd-b9d6-6b10b9def18d | -16.47387 | -53.91834 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43ddd5e7-3421-3935-84c0-93870c80e78e | -16.47104 | -53.9127 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f2eea35-dde9-3549-8a6e-9c56064f1c57 | -16.47037 | -53.91069 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c627be3f-6653-3de6-991e-fea7782be0e7 | -16.46732 | -53.91229 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab7853bd-5987-355f-8158-9d89fdc581d9 | -16.4665 | -53.91705 | 2024-10-08 04:36:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README65.md)
