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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b28861eb-98b7-3204-ba22-a7b93d7d9d74 | -12.8 | -51.19 | 2024-09-26 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec946511-316e-3707-96f0-5685903cd5c1 | -12.77 | -51.18 | 2024-09-26 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1cbe5f8-2bf4-39e4-b13d-47ffea183b24 | -12.83 | -51.15 | 2024-09-26 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eee2871b-9222-358e-9574-a532897e742f | -12.83 | -51.2 | 2024-09-26 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da16ebea-d037-316f-b617-2752b46cf89a | -12.8 | -51.14 | 2024-09-26 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0bbf1793-e4c8-3b3d-875b-7b0c7ad9a278 | -10.01 | -53.48 | 2024-09-26 04:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48aa7ba5-d592-32dc-a00b-df5af5a6191c | -2.6785 | -57.531 | 2024-09-26 04:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d31d0780-69d8-3a8e-947e-106c66fa625b | -2.6968 | -57.5307 | 2024-09-26 04:05:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d0a1c6db-315b-3b76-8161-e723496cd4fb | -3.5673 | -50.3794 | 2024-09-26 04:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 44f9b18a-b889-3f9f-b2f0-128dc4755ad6 | -6.949 | -63.1048 | 2024-09-26 04:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 21e0ead6-33ea-36b5-950e-152041b40aa0 | -6.9489 | -63.1236 | 2024-09-26 04:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| af904008-7043-343a-b712-e5f2a74b3fa0 | -6.9306 | -63.1053 | 2024-09-26 04:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 32472ea7-f63f-339b-9642-e107db6acd20 | -6.9305 | -63.1241 | 2024-09-26 04:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 4f23d0bd-cac5-3183-b049-edc20c8e9b61 | -7.3639 | -55.4935 | 2024-09-26 04:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 09ed61ea-62dc-3d5f-a722-816659dac1a8 | -7.3637 | -55.5134 | 2024-09-26 04:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 165.2 |
| b9a3d31a-d216-31bd-abb7-2a9341696012 | -7.3089 | -61.1053 | 2024-09-26 04:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 54e19aad-fc63-33dc-8749-4f705a9ac752 | -7.2906 | -61.0869 | 2024-09-26 04:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 82c57e8f-bd69-31b3-a508-19aa5e02e222 | -7.2905 | -61.106 | 2024-09-26 04:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| bf1ce32b-a76c-36be-8262-ff767c00b352 | -7.3823 | -55.5124 | 2024-09-26 04:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 8e223b1f-9a09-3c38-8fcf-0225c63c9407 | -7.3824 | -55.4924 | 2024-09-26 04:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| efa0e27f-0490-3f54-ae1c-23df56237fa5 | -7.8154 | -54.7453 | 2024-09-26 04:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 50b3591d-3c18-3cbc-8e75-c1ff75acc55f | -7.8156 | -54.7252 | 2024-09-26 04:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 229f276a-2d60-3ee9-a26f-7677e6d6907a | -8.1393 | -61.3007 | 2024-09-26 04:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 2c922e78-07b9-3f22-9e1a-fd1a66614f70 | -8.1394 | -61.2817 | 2024-09-26 04:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 6674874b-cb5f-3f75-8411-3e7bb24af973 | -8.3155 | -54.9956 | 2024-09-26 04:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 4fa9ad7c-d1a8-3154-bdb8-9d7cc28bd318 | -8.8098 | -58.2172 | 2024-09-26 04:05:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 1c932a37-fa89-349d-87fd-f3348b1e5e90 | -9.086 | -61.1245 | 2024-09-26 04:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4ffb712b-f94c-3893-9222-82168bf4d878 | -9.1046 | -61.1237 | 2024-09-26 04:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 79f31da8-f68e-3768-b0db-bdd5db782389 | -7.06868 | -41.15644 | 2024-09-26 04:06:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 442d1bf5-d9f6-38f7-9268-8236b907754f | -6.78785 | -41.23671 | 2024-09-26 04:06:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5df37108-08ee-3aa6-9edb-b6f2a1ec4b7b | -6.78508 | -41.23273 | 2024-09-26 04:06:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b22dae4e-7be3-33ab-bf26-5cbd12d054a9 | -6.57776 | -41.83769 | 2024-09-26 04:06:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 74825345-ba9d-36b5-abba-68c5fee00c88 | -6.57721 | -41.84117 | 2024-09-26 04:06:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c110a880-1112-395c-a619-75000bb27bd2 | -7.30244 | -42.02454 | 2024-09-26 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a8de8837-a632-37d5-a5e6-4239060e02bf | -7.29968 | -42.02054 | 2024-09-26 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8b2c1a2c-2d0b-3fb3-89c1-0c19f6e1b432 | -7.29582 | -42.02349 | 2024-09-26 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e8b8eb07-cd3d-3ccc-a200-4623d919938e | -7.04957 | -42.05535 | 2024-09-26 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a0731fa1-bdd3-3a28-9c7a-9852fbb6572e | -7.04902 | -42.05882 | 2024-09-26 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dac5654c-9342-3bcb-81a0-510569b820ad | -7.02527 | -42.05841 | 2024-09-26 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48fbfd0c-067e-3c76-9294-fabc80bac409 | -6.92248 | -41.97846 | 2024-09-26 04:06:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 419e4aed-3b56-3fb6-9c89-ebd7fea5b9c5 | -6.92193 | -41.98194 | 2024-09-26 04:06:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9bf84d1c-c4a2-3e9f-86ee-2b9113aee800 | -8.36506 | -41.3998 | 2024-09-26 04:06:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d186582-b603-3087-9489-23576fb050b4 | -8.10779 | -41.4166 | 2024-09-26 04:06:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07fd0d89-aed9-391e-a863-797f54f9b67b | -8.27369 | -41.26764 | 2024-09-26 04:06:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5210773c-69ce-34ec-aa6b-31aa3f847c87 | -8.36511 | -41.13883 | 2024-09-26 04:06:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c5db5b98-8e56-34af-8ff4-2fb1e5652577 | -8.19053 | -41.36489 | 2024-09-26 04:06:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5cc8c1c8-b2bc-3793-8814-0795f43f27f2 | -12.58918 | -42.4198 | 2024-09-26 04:06:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2e1bb55c-d5b5-3662-9a1e-6e6758dcce87 | -6.34729 | -43.15312 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 095ff358-3934-3c98-bcd0-95b32dc67b1b | -6.34669 | -43.1568 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c89d2323-358f-3e0b-b9ca-a19ae04df17e | -6.34269 | -43.15993 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39c80107-55ba-3905-adac-e6122712044b | -6.33869 | -43.16308 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37d1e4e4-8582-3ddb-a0d5-78ff6254579f | -7.98207 | -42.83785 | 2024-09-26 04:06:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| adce9b6d-8712-3eda-95ed-83293bf5a6e5 | -7.97425 | -42.84387 | 2024-09-26 04:06:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98994916-b8eb-37cd-b085-c4df25a32836 | -7.97034 | -42.84688 | 2024-09-26 04:06:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f9f3f14e-6d7b-3c76-968b-437d7b071620 | -7.91895 | -42.67529 | 2024-09-26 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c04a5c71-613e-350e-93a9-4c8369e3a7a3 | -7.90187 | -42.68053 | 2024-09-26 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4f3910eb-f254-3b6c-b960-d48ecdddf1e7 | -7.89853 | -42.68 | 2024-09-26 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f6969cd-a2f7-3fad-9c47-fbc33d92cc06 | -7.86723 | -43.14663 | 2024-09-26 04:06:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1862d37d-21fa-3cb1-b8e6-52a1f7c41b0e | -7.59293 | -42.29195 | 2024-09-26 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 07f36e76-0664-38d4-b49d-2a70723fac66 | -7.59238 | -42.29545 | 2024-09-26 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| e6577ea5-525c-35a7-92c8-0c50508b85bc | -7.58961 | -42.29141 | 2024-09-26 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 0da70980-5a7d-39f7-9112-dd8a771365ce | -7.58906 | -42.2949 | 2024-09-26 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 5665c720-ca99-39a5-bc63-547045d01130 | -7.5885 | -42.2984 | 2024-09-26 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 648446f5-324f-3701-aee0-4a8b6957e5e3 | -7.47755 | -43.7569 | 2024-09-26 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f8a16415-2e94-34f6-b198-fb6afd38fe99 | -7.22423 | -42.45288 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 319722ba-b587-3375-8940-2e7cc1049fd8 | -7.22146 | -42.44881 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d0e32433-98d7-3038-ac06-122cd32c6351 | -7.2209 | -42.45233 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e5b4681b-e93e-3469-9c2d-1c8c18cb4098 | -7.22033 | -42.45585 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7d58617d-0544-3c05-8489-5f8f8a07510a | -7.21813 | -42.44827 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0d29050b-2ef8-3463-8f68-6db42e818aa4 | -7.2058 | -42.5041 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 617cb8b5-18d2-37b5-8ece-23e38d52c22b | -7.20528 | -42.48593 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dea43dbe-d349-3e18-b7b2-996f629bac6e | -7.20523 | -42.50765 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 41124837-da71-3571-b634-dcd4a21c8c12 | -7.20359 | -42.49651 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4485f546-5771-3e41-8f2d-604077f37992 | -7.12972 | -42.51337 | 2024-09-26 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 109dcd1f-be7a-340d-b7cd-1cbd0b303b62 | -7.04232 | -42.82385 | 2024-09-26 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c214c125-d56c-3536-b253-3b33801ccc3b | -6.95942 | -42.47523 | 2024-09-26 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b4c52982-9975-34d3-84b3-17ef2d2a7b14 | -6.95608 | -42.47471 | 2024-09-26 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7e435d48-2765-3c7f-94e8-2481d7284836 | -7.36675 | -43.33318 | 2024-09-26 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 513d79c7-78ea-3b85-8ca1-17becde4939c | -6.85653 | -43.10211 | 2024-09-26 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c10aca3c-8fd1-3434-b239-918956b2fabb | -6.85314 | -43.10155 | 2024-09-26 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 625b586e-d95b-3216-8866-b9b62dddb706 | -6.78768 | -43.07613 | 2024-09-26 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a40a4ff-1475-383e-83aa-19a876eb9a1b | -6.71653 | -43.55924 | 2024-09-26 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40696f2c-0a27-30f2-b7fb-bc601a3b8000 | -6.68407 | -43.54735 | 2024-09-26 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c249933-7327-394c-b999-bd48842aeb84 | -6.68063 | -43.54678 | 2024-09-26 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c632712c-8b17-3652-b9c1-55eb5ba3c6dd | -6.54989 | -43.15874 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9304f6ac-e803-39f2-a208-4663c1800086 | -6.54929 | -43.16242 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1de74fde-1055-3455-9527-88ff401113f2 | -6.54595 | -43.0271 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5d12ce8-e7c3-3f4c-b4c3-f7b1f9899f8e | -6.54538 | -43.03073 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ba0c7d4d-0435-3ecf-9700-e5b41eeaa249 | -6.54256 | -43.02655 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a7514d7-2f96-3407-842d-6a032d1fad57 | -6.54199 | -43.03018 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f42e87b7-21d6-304e-83de-fbeb7325c246 | -6.54141 | -43.03382 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 689b4b15-3552-36d6-acbd-e2247d41a07b | -6.46669 | -43.30502 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59075658-82ef-38f7-b64b-e787ffe87c00 | -6.4661 | -43.30871 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f87a48b-1f0e-3cc8-9325-5c57ff4832fb | -6.46386 | -43.30076 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb46eee8-9e50-3823-9619-a572183448e2 | -6.46045 | -43.30018 | 2024-09-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ce4fd3f-d1ba-36bf-b28a-4e098b34fa57 | -8.06907 | -42.88852 | 2024-09-26 04:06:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9a40e91e-dd3b-3532-9023-c9aa57504dc9 | -8.06686 | -42.88088 | 2024-09-26 04:06:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0716a1e9-f18c-3734-a650-8a0d26581022 | -8.06629 | -42.88444 | 2024-09-26 04:06:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5831fdfe-c291-3701-bdfd-ae517798f41d | -8.06572 | -42.88801 | 2024-09-26 04:06:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee830760-a45d-3174-a94e-37d71c845bd7 | -7.96344 | -43.82912 | 2024-09-26 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README60.md)
