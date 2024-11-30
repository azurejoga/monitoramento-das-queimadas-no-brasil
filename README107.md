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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0e88619-8c97-3d2e-9444-bc37f1ab007a | 0.98676 | -50.26724 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c81b0021-98f1-3bb0-b5a7-ba0f90917882 | -2.94663 | -49.44658 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa9b53a0-ed3d-3566-ad76-a579767a785a | -1.61759 | -52.45553 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6abefd97-3d0b-35ec-83b8-c398237b6fb8 | -1.24419 | -51.79325 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f3359fbd-c6dc-389a-a24b-2162f7adbc56 | -2.88482 | -51.72089 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d8e99f8-6270-337f-8867-80fcd0e67c14 | -1.21268 | -54.19212 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02338171-2715-3164-af6f-bf4265bbc519 | -2.77781 | -53.94402 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 408b2fd6-13fd-30f5-baf6-5e3782ec8c30 | -1.09466 | -53.37037 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4036d3e3-24c6-39f5-9a20-2e963496d855 | -3.58003 | -50.34196 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ffc8fa1-4b7e-3752-b4e4-e0feb421f121 | -2.73853 | -54.10661 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8748afd-e57e-3aac-af87-f48dbcfff086 | -2.40265 | -48.23248 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba0ce2b4-3a5a-3e62-95d9-b23840563adc | -3.25907 | -53.6371 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 133b671d-edb2-3e31-aada-f57c71881da4 | -1.16039 | -53.68317 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f1a2d9c-12e7-3cf9-8d1a-5ba64489680e | -3.10578 | -54.04527 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fd0303e-01be-32c2-97f9-7d335baec0fe | -2.8339 | -54.09979 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d13505ca-c4b7-39c4-9325-3c9f83b6b149 | -3.08038 | -54.12697 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd37f598-4d1a-3c02-8b91-2f85bb55f900 | -1.59507 | -53.82534 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dcbe705-b294-33a4-92e0-aad1ec94151f | 0.88381 | -51.98172 | 2024-11-30 05:01:00 | NPP-375D | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13826ac0-4426-3343-9304-f22a00df2bff | -3.09414 | -54.01778 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 372f22c6-a7e7-3abf-9764-36f40b32079e | -2.46926 | -46.56219 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 338419b8-8556-377f-bf8a-6daf7c5eb7ab | -1.7242 | -55.7558 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47211743-427c-3037-9c65-bfd67479705e | 1.89125 | -55.72023 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c48be8c2-4718-369f-ae3f-29c7d66c9266 | -2.88827 | -54.16178 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b92b8812-c728-39d3-9912-dacb2f881ebc | -2.79704 | -54.05111 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b22f1871-5868-36f8-9145-5b54c731d4b2 | -3.08312 | -53.75918 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cdb905c-202a-3b0d-8bd9-92ddfdec603b | -0.82291 | -51.85795 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 59ae6796-be8b-34ac-b11d-ef02b6b1e85a | -3.16229 | -49.01967 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 595e6cc6-9cde-3eb5-9c49-1666ac888461 | -2.98431 | -53.29542 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea52a949-55f5-3651-8e50-cb8f5af0005d | -3.23619 | -50.25054 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b19a8e2-5ca6-3582-b6f1-6dac8e28e680 | -2.46224 | -55.2811 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5599fd3-5565-3762-af55-9dbf08c6d744 | -3.82606 | -50.13735 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6e82a73-7b06-3ce0-8cb5-0027038984cf | -1.16071 | -53.5503 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c2011a3-ff4c-3109-9350-f5fc8f29808c | -3.26728 | -50.20812 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 04102490-a626-330d-89a4-f63243c32771 | -2.59017 | -53.96846 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3e92be5-3bc7-3ac4-bf42-fe39b7ca69a6 | -1.07299 | -55.26671 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff735dcf-9b26-346a-91ec-3d62f63c7172 | -1.58862 | -51.25877 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 689886a0-08e8-370c-b87a-942c89cf414d | -2.97128 | -53.28959 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d680ef7-cfaf-3726-834b-f7c92286d35a | -2.80263 | -54.05914 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fbc2255-ed5e-3b0d-a40a-7b2888aea302 | -0.95932 | -51.65813 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3149b0fb-465c-3499-8bdd-9ed32adaabcb | -2.97865 | -53.28702 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b8fa6c2-0936-39d8-8409-eb82496ff091 | -2.9707 | -53.29323 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a14294b1-f7e7-36eb-ab1b-f70c890fb9db | -3.0792 | -53.7622 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fe73b8f-c871-3ceb-8014-9459b2f8060d | -3.9161 | -54.01434 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58100785-4daf-3830-b758-f9c62b2d38ab | -1.29259 | -51.36552 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bc69465-8372-3fce-a3b2-ecc4e45b202a | -2.51777 | -48.18303 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45b4b34e-6176-3503-864c-7ce4daa0da81 | -2.81145 | -54.02464 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3686b304-940e-34be-98d7-4a6493b3e31c | -3.12748 | -46.05479 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96fca4fa-8157-3d07-b69a-4f75bdc51896 | -2.76457 | -54.04981 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 987630d6-c368-366d-a970-73f091da90c8 | -3.91767 | -53.67007 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0d6dd1a-c0fc-33c4-a9dc-9dcf46ecb1e2 | -2.94823 | -49.44299 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fc1e300-39d1-3a3b-987f-00a6c1794598 | -2.03117 | -53.49942 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05a3bd16-ea49-3c8c-aedf-09a2f1c1c268 | -2.01041 | -51.1863 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18a3153a-7868-3e98-9fe9-8536d4c1a8a1 | -3.14204 | -53.83406 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f7921d2-fae7-3e3f-9d58-f4ee4ac9317d | -3.09638 | -54.02532 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a6bc5a0-9a11-3034-8410-e910496e314e | -3.74537 | -54.67601 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c917f9cd-5732-3046-92fb-d4f7c5bc8489 | -0.05634 | -51.59607 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 726448ca-3401-3b52-b201-bfacf1e643ac | -4.41649 | -46.14534 | 2024-11-30 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a18be490-6387-39c2-a70f-d9a58c817649 | -3.5414 | -50.18407 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42ddec86-68e7-39f1-ae74-c703fbd55e43 | -3.30332 | -53.6912 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a81e47d-f43c-3e09-9548-d6fbeadd66bd | -3.57419 | -52.00864 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb00dcd4-e93d-350b-a1b8-e54f22c1dfa7 | -2.61756 | -51.76402 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5f561fc-301e-3fc6-bf47-6f7871f8640b | -2.82772 | -54.07378 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45747647-1530-3bbd-ba53-f2087c5d6c90 | -1.18793 | -53.87283 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2daccd4-0aeb-3981-97ed-59f094b025e0 | -2.84809 | -53.96565 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7385b0d-3e68-3f8d-83fc-a626e1bd94ad | 0.97782 | -50.25944 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 693191be-735a-3c95-8acc-f904c2d8c745 | -2.23849 | -47.98911 | 2024-11-30 05:01:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4651d9a6-a387-3e5b-aeaf-1fb0925d99fc | -2.76461 | -54.0713 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a755e5ca-2ac4-39d1-ac13-3e6f8998895b | 0.73993 | -50.86907 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 712172b9-d32d-3d47-b51d-549724c18c4f | -1.61395 | -52.35441 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2745975-e39a-3a4f-911f-7cb3f05d9e34 | -1.42213 | -54.94493 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bcec38e-d379-3826-a22c-aea9aa15325e | -1.35437 | -51.37508 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba1d0462-6c45-3b55-bd2c-3e47b60aa81c | -2.8332 | -54.03877 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e52c0cf-3593-337a-acbb-f20baab9a087 | -3.48914 | -53.82151 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b21520e-458b-3eed-a98a-07b6f4fa5277 | -3.29038 | -53.68552 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6a7bf1a-6295-3f4b-b0b3-1163d42f1ccd | -3.9891 | -48.94135 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f9535033-09fe-3327-916f-b7480cd3953a | -1.43193 | -54.30441 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1100152-36d5-3668-82af-a7e8133184a7 | -2.74284 | -54.03568 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6406499-ed3b-36af-bafe-9e6c5933c554 | 1.20406 | -55.94473 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa2f685f-4d95-3b47-895d-c6d7a2b319d8 | -2.71921 | -47.55182 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a765a472-fb30-38de-8a4f-fa1b2aa92dc7 | -3.75973 | -49.94519 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8772fb41-4c67-3c5a-a3a3-ebb74fccafee | -1.19181 | -53.86984 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| affc624f-bd37-3736-a343-e9c87ef3bbfb | -1.59628 | -52.28499 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64fdb2f0-0f5f-3485-ab34-a97c59c0dc3f | -3.69463 | -47.12847 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a988af48-5087-3bb1-b626-d09479476cc2 | 0.89192 | -51.98829 | 2024-11-30 05:01:00 | NPP-375D | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 90116431-883e-3941-a821-ccd09ceffd76 | 1.99424 | -60.56384 | 2024-11-30 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92f9b10b-366f-3186-932b-6b69b669e35a | -1.83408 | -54.52258 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 590d74c5-82f5-3a78-acaf-8fcc17adcdb4 | -1.09523 | -53.38861 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 99c0f2f6-8077-30fc-a46c-5178dd176205 | -0.25143 | -53.75889 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1e98a5d5-1f4d-3a7c-8d08-d51b1358b24b | -3.26412 | -51.62535 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca113c2f-6972-391b-a3c7-ee4fc58d6c3e | -2.62181 | -51.76043 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7acb1cc-8dcf-3162-82de-35666fca210a | -3.45407 | -54.56643 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 565fab57-da02-3a4a-8174-97817b214899 | -3.26939 | -50.20573 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0202df43-1232-34fc-bb59-094494c1a1d6 | -3.49195 | -53.8256 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00cf850c-0ec7-3980-be32-de9a54959248 | -4.06707 | -46.68081 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 003c7d8b-21fb-3dae-87d9-44dff5f00ea1 | -3.69744 | -50.1687 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 328c3db5-5a8c-393d-891e-972bf6a0e0eb | -4.06038 | -49.06418 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 212bbdd2-ca80-3181-a3c0-9d3320af3eed | -4.06102 | -49.05997 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0658a79-566d-321e-8f0a-dc587d3702b5 | -4.08067 | -54.56473 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39d5255a-1b9f-34f6-b6ea-a7c13638453a | -2.76025 | -54.12069 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bfc0540-e226-3ca8-ae65-83a3000b8ee7 | -2.35046 | -49.01283 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README108.md)
