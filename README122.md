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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75a2d4a1-39c8-3924-9a71-db468c348f85 | -8.59865 | -46.52686 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d93c4f5-c9f4-3dc9-a4f2-721441936733 | -8.59416 | -46.52635 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 085bb48f-79ec-31db-b5b2-f799176e09dc | -8.58968 | -46.5258 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fcb4db2-c961-3154-8e87-1b031a57ad49 | -8.58521 | -46.52521 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20eded74-8783-375a-9c61-e87e2cd53df5 | -8.49469 | -46.85478 | 2024-10-03 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76024d05-7308-389e-80e9-89722a8b3bd3 | -8.49424 | -46.85246 | 2024-10-03 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c7c2c69-be23-36cd-93b1-d79e1ed04a9f | -8.43322 | -46.30936 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88328a25-57ce-343f-807e-94b78d3669eb | -8.43264 | -46.84736 | 2024-10-03 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6b21f61-4bca-39e8-acfc-2fbae3c66e98 | -8.43203 | -46.85169 | 2024-10-03 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ac4cd2b-2ef7-3fdc-bf95-abd6b6c4b25a | -8.43065 | -46.29483 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a40f3085-1de4-3b23-849d-1559ba392aeb | -8.43001 | -46.29942 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d16d8bcb-f567-3ab8-8639-35d6ba7ce1f1 | -8.42935 | -46.30404 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c398e5e-a2d0-37c1-811f-759da292573b | -8.42867 | -46.30887 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb1d5538-43d7-379b-8ac3-4432c3680c74 | -8.42828 | -46.84668 | 2024-10-03 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6a2cdc8-1dfd-3532-9db2-ef840f8696d5 | -8.42767 | -46.85105 | 2024-10-03 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7af669be-9d76-3091-8028-6314f5ff39e0 | -8.42549 | -46.2987 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32a9896d-a180-36c9-90b6-52ee431731ad | -8.42483 | -46.30336 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 670a7006-f2e9-3ea7-9575-e637df3c6d5c | -8.42415 | -46.30822 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 522c6b2a-10c6-3a47-a961-665c64abebc5 | -8.42393 | -46.846 | 2024-10-03 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ef4714a-6b12-3625-89ea-802d3afbd4ad | -8.42333 | -46.85028 | 2024-10-03 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4485f565-48d1-3ba7-9c3b-222d4cb9eed0 | -8.41963 | -46.3075 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f4a6c98-1be1-31c9-97e3-6d8aadeef227 | -8.41513 | -46.30668 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31025f68-aa10-3da4-8db2-bc67ea0dd465 | -8.41446 | -46.31148 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c250b655-3d79-3ef6-8da6-fa4040f73378 | -8.40863 | -46.32018 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2f644ab-216d-398e-9841-a0ff07e6c357 | -8.40801 | -46.32468 | 2024-10-03 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d53acb0-b9d2-3060-acfd-4d3e50704f42 | -10.72822 | -46.18513 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a0bd0fd-422b-33f8-978c-0a7ecab327ad | -10.72757 | -46.19017 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1e3c978-ea5d-32b2-b297-385d3f9862ca | -10.72692 | -46.19522 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d85a2415-d4e6-3ea6-9612-5a83b0e630d6 | -10.72627 | -46.20019 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3c2f39c-f3ec-347a-b619-70fee681aa89 | -10.72495 | -46.19861 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ce419d2-ece0-3f51-9900-2403c8fb06ee | -10.72362 | -46.17316 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e391871e-4145-3ee0-8053-ec7525c4b4c3 | -10.71958 | -46.16747 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37077d31-260f-32c6-bc5c-93c5fc8a5c88 | -10.72428 | -46.20347 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c155d6b7-069b-344b-913a-da13233f68c9 | -10.72361 | -46.20838 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73242e1c-e43e-3c88-b74d-4dc86b9b691a | -10.72293 | -46.21332 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ccdc916-c363-31ca-a615-c8eb030c4106 | -10.72091 | -46.20459 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48c7e139-8f96-3d20-bba3-f04a139b524f | -10.72027 | -46.20951 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27fdeebc-373d-3de6-8489-fb46096a0f19 | -10.71963 | -46.21446 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79c7797e-1baa-3024-ac27-2e5c73cf6545 | -10.71888 | -46.20784 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d932c2a-3c25-3147-9b86-b049c390e732 | -10.71821 | -46.21275 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36bfdcfc-ba88-33a3-9613-925de178ad15 | -10.70534 | -46.20153 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2efac2d2-8768-3d11-b404-3b31724225b1 | -10.69929 | -46.21074 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 360119ac-1714-3708-a037-98f55e1b7f14 | -9.91532 | -45.90282 | 2024-10-03 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08b864f7-e225-3648-b77c-8e7721539968 | -9.91513 | -45.90023 | 2024-10-03 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1cb404c-7c9d-36ef-8b3a-dc3a43f69604 | -10.11101 | -46.56941 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5076f7c8-4059-3566-9f01-62e351964849 | -10.10707 | -46.56427 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c8d0e66-be21-327b-8930-6a8e75250ea9 | -10.10644 | -46.56883 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65e982b0-227a-3457-a6b0-da80bf3897e9 | -10.10251 | -46.56368 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0eab86ca-e9d3-3517-880c-04917836237f | -12.00264 | -47.34987 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16ad5318-3c7a-320c-bed7-b3a286abc32b | -11.81833 | -47.59212 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaf32423-f6ec-3812-8ee1-2022f5a90547 | -11.80254 | -47.57774 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 627bc09e-3606-37e1-ad2c-34ef11d39df2 | -11.70703 | -47.71857 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85deea38-d67c-3403-8ac4-35fadc17c4da | -11.70475 | -47.70337 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e6f9e53-3d19-3cf8-b557-910115b8b256 | -11.70324 | -47.71422 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54697404-5faa-3802-8663-845b71168c06 | -11.70192 | -47.70168 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a8fe9b3f-ca7b-37d6-ace3-813d612bd022 | -11.70143 | -47.70539 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 567920bc-4e45-3c61-a555-1a2b15091777 | -11.70096 | -47.70893 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6cb2e395-6e0e-3bb1-9176-acbe951abe0c | -11.70036 | -47.70327 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40064609-2e64-36c7-b9d9-457a7dde3dc3 | -11.69985 | -47.70691 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b338800-0dfb-39c7-8337-a6ac708034cc | -11.69936 | -47.71042 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f85c3997-44c7-3158-aac2-21e98188029f | -11.69785 | -47.72134 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb667204-3f5b-309a-972f-dafd01e191c9 | -11.69652 | -47.6992 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 337d058c-20b0-33c5-ae99-1e9d986f4601 | -11.69019 | -47.71315 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d50c88eb-f41d-359a-be68-be111999cc2c | -11.68308 | -47.70096 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ee97481-6618-3da7-a808-885ee90b1108 | -11.68208 | -47.70823 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a7d12f3b-7231-3df8-8c3a-a213713f6c07 | -11.6816 | -47.71168 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b7f864d7-633e-3145-b60a-c62060d3e3d2 | -11.67881 | -47.7 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9028ece8-f2ce-3593-9f65-25c6004a325a | -11.67829 | -47.70384 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22abb304-8669-31b9-be45-29a5b03d5112 | -12.19681 | -46.75861 | 2024-10-03 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0156b70-64f4-3497-9afd-1371f03a6526 | -12.19217 | -46.75801 | 2024-10-03 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 99b10cf5-6364-34f7-b6ce-7fc331a94105 | -12.18815 | -46.75258 | 2024-10-03 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f08c6dcc-7522-340e-8f3d-8eb1892a2214 | -12.18352 | -46.75192 | 2024-10-03 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a631be35-3584-34ab-90b0-240cb464b926 | -11.25381 | -46.92353 | 2024-10-03 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0697db5-0f90-3424-ab6d-3a5040518667 | -11.2499 | -46.91847 | 2024-10-03 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f7a34d3-78ee-330d-a9bc-8e8bf20fb686 | -11.24929 | -46.92293 | 2024-10-03 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f44cc2a8-c298-345c-9785-a0f9e4060760 | -11.01884 | -46.50131 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca7ae493-05d9-3881-9eb0-b549f2bc29f0 | -11.01668 | -46.50225 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d3b45e5-a602-386d-ada4-fba6232c193c | -11.01425 | -46.50034 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd57756e-9a0f-3fdf-b6a4-559dbbb9a412 | -11.01143 | -46.4864 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae5d4ad1-e8ae-3d80-95d7-67727aaf6097 | -11.01085 | -46.49062 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 211eb6e1-0041-3827-9869-e37d0e57d32f | -11.00919 | -46.48714 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4633034-d66f-3dd0-9a68-91adb59e8c41 | -10.94514 | -46.59312 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b717b033-7ee1-3a6f-83bd-b2b4958fec07 | -10.94054 | -46.59243 | 2024-10-03 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 315c7dd5-8770-3a42-8446-559f4bd81f7e | -11.81776 | -47.59628 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf092858-eb0e-359d-852e-7558f1d7b71a | -11.81452 | -47.58758 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58eb940b-ec33-3ad3-9416-ee13258f181e | -11.8031 | -47.5737 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3620bfcb-7f74-3055-8af3-80f2a4502faa | -11.802 | -47.58174 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9996fd34-67a7-38e8-a9ed-1ed46830b132 | -11.79928 | -47.56908 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd4401a8-b0dc-3487-8cd9-92aebad44867 | -11.79871 | -47.57325 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00d409b7-4bb6-31e4-84f8-f2d2783bac79 | -11.70088 | -47.69946 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 05faf9ce-fd33-3eb0-bf78-80e1d5aeb30e | -11.6995 | -47.71991 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3f9af25-5397-39cd-99d8-5d3f0a1db40a | -11.69836 | -47.71764 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b84114d4-efe9-30aa-a727-c7a65392180e | -11.6922 | -47.69859 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7a985d8-6e98-34e2-8e6f-a3222ad0b944 | -11.69165 | -47.70263 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b8fd292-de03-35c0-8177-dde86c9696ab | -11.68791 | -47.69786 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85422539-a1e4-3b03-b5b5-e5341887e105 | -11.68734 | -47.70194 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57d1535e-facb-3031-858c-a704799c1713 | -11.68589 | -47.71249 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| abd8738d-38c3-370f-af72-8dc058ba58d0 | -11.68539 | -47.71607 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 45b0e64d-195e-32cf-acde-27c976feeac9 | -11.6778 | -47.70738 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 004eb7b6-135f-392b-b59b-c6cfcf5c0a04 | -11.67732 | -47.71086 | 2024-10-03 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README123.md)
