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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 678c70f5-81b1-3371-aa46-46366d956776 | -1.58924 | -50.43417 | 2024-11-09 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 384950c9-b030-3a99-b75d-9e0dc94d258b | -2.7701 | -51.60822 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 301c9c02-74b4-39a6-b9ce-c9227e621742 | -4.48844 | -48.49241 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32dbf832-b867-39bd-89e9-5f82caeb0d1e | -0.36669 | -51.64047 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b02ac6ed-9ad0-327a-8fcb-581c46b56fb5 | -3.62058 | -50.19534 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34a1f1a8-3bb0-3369-96d1-03dacb82af19 | -2.41072 | -48.38967 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b43ffdd6-f208-3955-aa5f-029ee32c7690 | -5.98133 | -45.36969 | 2024-11-09 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb759f6c-6820-3051-9296-64f1b1ef2cf2 | -1.46536 | -53.41842 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20a6487d-120c-3f59-9f63-b1df7b113e6b | -5.19954 | -47.46067 | 2024-11-09 04:55:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13342036-88c4-3990-b814-93301cdf1f5a | -1.67861 | -53.18018 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93d3145b-3134-3f11-b477-345e35ed431d | -2.87875 | -50.41679 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80f059fb-0aaf-3641-a8c5-5cd65aef6920 | -2.90693 | -50.4004 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7941ecf2-9ec7-3b60-b09e-8ac8a7d44dd5 | -1.34207 | -52.18253 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dfcbcb8-6573-36ce-87ff-2c80f53482de | -2.83426 | -51.8041 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| def52f56-7aab-3bd8-8de0-840e90d120c9 | -3.28248 | -51.52412 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff0376a7-ac06-3412-aadf-3eef8a373da8 | -1.39293 | -52.13356 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f86c200-6c31-3368-9ffc-7442e91ee6f7 | -2.85229 | -51.77732 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19ca24f0-952b-34e3-892b-ba47dc09a779 | -2.22054 | -46.43215 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60b74c9b-bde7-34c0-b23b-23788c122736 | -3.72795 | -53.40574 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23ff6af5-684f-31b4-ae51-6feb3bfc464e | -2.56788 | -48.25632 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4de63af9-0131-3dee-aaa2-9106959c13c8 | -2.27276 | -51.12989 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43ec09b8-e798-36a1-9843-4293e62f4c45 | -2.74394 | -53.20566 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c3358c3-ab3a-3076-8717-50d31df83755 | -3.51069 | -51.67152 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59050d9b-bd0c-3679-bd67-9c162e963092 | -4.66748 | -44.34081 | 2024-11-09 04:55:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c450c109-1a98-3255-88d1-67aa8ee5e768 | -2.87866 | -51.47138 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a777c7fd-66f5-38ec-83a6-b6dc014ed3b2 | -5.13624 | -50.61147 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5456e161-2795-305f-91fa-9435110634de | -2.56958 | -47.34095 | 2024-11-09 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bc9f8e7-c149-31b0-95b2-78469eade00b | -2.82281 | -52.96358 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dd5f477-b6db-3a7c-ac82-2eabfab3c7ed | -2.1572 | -50.51349 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e402d42a-34f1-368b-ac05-2f266a217f67 | -3.01132 | -53.44206 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 064fa24b-61c8-3b72-bab6-60e72b1a4d20 | -2.19968 | -49.52172 | 2024-11-09 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ea23663-5e89-3804-a192-5f63d7715329 | -1.56069 | -51.17111 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a43ae792-f443-3939-8b4b-dbae3f5ea415 | -2.56912 | -54.03982 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02cc783c-9683-353c-81b0-aef7887ee05f | -4.63182 | -46.53607 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29aa32aa-dd7e-36f3-9ed6-2105c0752d63 | -2.37638 | -53.84522 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01adda5d-a424-332b-8a8f-87a981e383e4 | -3.1181 | -53.70936 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dd9a68e-3dc3-3681-a886-d35165bc736e | -3.02567 | -48.02713 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 084cd2a3-3223-3d7d-88ab-16dd792216ee | -2.63209 | -46.77383 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c2de6c5-ca90-30c6-a478-55fe6375bbc2 | -1.55859 | -52.2839 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9518170e-c669-3214-902f-3c42248ab3c0 | -3.60162 | -51.24205 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 997423fa-ae4c-38e0-bf6f-e29648d496a1 | -3.14538 | -52.97886 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fdccb02-37ee-3a98-a425-387fd21e9cc3 | -1.46269 | -51.4841 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e54a5590-3138-3454-9019-18ea519cf837 | -1.9396 | -51.40469 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9ab803c6-c732-3eec-9677-c0efc6e1348a | -4.05528 | -48.25724 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7902ec5-b35d-3125-b799-a769f9108db8 | -3.6045 | -51.2464 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f805b775-7b65-31f7-8c63-fb8f8f0d9c84 | -1.82663 | -53.72354 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33b441b2-c76c-3e9c-8c34-6f0256ae0ee3 | -2.40926 | -48.87438 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e89cf73e-117e-3cb7-8459-ceacb7e3a295 | -1.24493 | -51.76136 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 131a5c14-d613-3cfd-8405-afb654909432 | -7.45433 | -43.5769 | 2024-11-09 04:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfe965b0-90c3-3013-9b26-a8fc1bcf6df0 | -3.53023 | -50.32484 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a531a64-b8fb-3104-9f61-02a90962920b | -3.03089 | -51.01429 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50e855cb-968a-343e-acf2-90dbf5ac3f49 | -3.32245 | -53.18666 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11e69c4d-4e4f-3a75-b6f6-8f81f5628326 | -2.93223 | -51.53243 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6de8cdae-492b-3e70-97f3-aefebb172144 | -3.5405 | -51.02925 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ad77bfd-faf3-3e80-8f77-9b4600645132 | -4.29081 | -48.64837 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ea0a93f-952f-3310-a887-886503cd42a9 | -1.51174 | -52.17697 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 705a4675-6e87-395a-928a-6d8c2768e74c | -3.7887 | -46.13842 | 2024-11-09 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1125981-5e08-3d13-8982-2bef6d2d9907 | -3.58941 | -47.35396 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 9d49b9a0-103a-3750-9f92-03a1dd915267 | -1.72765 | -52.46307 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59922e57-c3ed-325a-9ca8-907fe9c87a36 | -2.19753 | -48.37388 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2348026-6b0a-34d1-8a70-8235549926da | -2.25473 | -53.73377 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7200dfca-e3b0-36db-966a-dc2d58b12143 | -1.72908 | -52.36733 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 174e1cb5-0cf6-3626-8923-ef14d6d51d7e | -2.37945 | -50.40723 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 423004bf-9f3b-3181-973d-4c69833fc53f | -1.14706 | -53.65283 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e6a3239-fe3c-3d35-a8da-27b29b7ed61b | -3.77042 | -51.34393 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffda3642-9d63-3838-a7c3-0d54db0d8441 | -3.38571 | -52.35522 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e07452df-2fc8-3f21-a77a-1a817d5dfea8 | -1.42058 | -53.91368 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52791b74-5d0e-3e24-9de0-aef2b2825c67 | -1.34266 | -51.42522 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0e0f210-cce1-3d70-aa07-24c0bba5c2bb | -2.17233 | -46.44359 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13df380c-84b0-3b19-a029-5087a788f045 | -0.9084 | -52.56942 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee0c42bb-378f-32c0-b692-d12bded6c3db | -2.23665 | -50.69673 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 332a6454-9244-3899-8afc-c93282001fa9 | -4.52865 | -50.95582 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2488b112-f5f9-326e-b325-1861d9c58121 | -2.19392 | -53.2609 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a2a99f6-b721-3f76-815b-1bddce0d5579 | -2.65788 | -49.86804 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 396f6498-eee3-343f-9d69-e1ec3b9e06f0 | -5.27278 | -44.76875 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 186cf62b-5a60-3a69-9a81-63127625e067 | -2.87923 | -51.4677 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 914c9a27-c12e-3b0f-97cd-a736a42aa9fe | -3.2381 | -45.12281 | 2024-11-09 04:55:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90cfa294-975d-3417-89e5-622e99d647e2 | -1.38307 | -55.32073 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a3fb915-81ae-3950-b091-9ff16c206646 | -5.11308 | -47.13753 | 2024-11-09 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d2388d1-720d-3917-8cc1-6313bbdb8ed3 | -3.03337 | -54.07281 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f0a2e70-8356-3e2b-8d5a-8634bcbced03 | -4.95292 | -48.45092 | 2024-11-09 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f90a3fe3-5f85-3a06-b1f5-9e3ecf5a6947 | -2.62762 | -46.77315 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64076848-74b5-3a30-bbfe-302fcdf900f5 | -2.99851 | -49.24193 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 61b72c2c-73df-3566-b9bf-190105b1562f | -1.33873 | -52.18202 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b90d127-c7e0-324f-835d-51d4f2cdc592 | -2.20168 | -50.78223 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b53af927-c5d3-33b6-afda-967b8aa980cc | -2.83372 | -52.9158 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8d89e4d-c04a-3027-8568-8ad07e14fb4b | -2.7351 | -51.72185 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feec8329-da1c-3f64-a5f4-df1fc179d253 | -3.29404 | -49.17385 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e8782b5-e5dd-3ed3-8796-55f5badcce15 | -1.69425 | -51.92101 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e142c5c-b3da-327f-b56f-edd91304b4a7 | -3.17409 | -50.21633 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4320d0dc-5092-3e07-96a1-aaca991a6dce | -1.75664 | -52.68419 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48afedf7-1d75-3ec4-bdbb-412053dda25d | -1.45873 | -51.48718 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e15ae460-c200-3ec0-bd14-15ea8fb60023 | -3.22132 | -50.20039 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3098d34b-f866-303e-9fb9-ba449701579e | -4.13828 | -54.98793 | 2024-11-09 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a832ea0-226b-3b9e-9ff7-50bccc15f30f | -2.84531 | -53.97892 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee453d6e-630a-3cf6-b0e1-b285ac30c12d | -2.57931 | -49.13483 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 811ba3f4-a153-35b0-a62a-9cc638849381 | -3.97045 | -48.18825 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 45e4827a-1f8d-3a35-981a-073dbbbf8a9b | -3.25269 | -50.44981 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4170b580-36fa-346c-8ca2-a464a5dc6742 | -1.43098 | -52.2394 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2572539c-60b4-3262-bbc8-489cfd06c499 | -1.42044 | -52.24134 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README97.md)
