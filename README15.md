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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2ae3f01-075b-318e-8fc8-6fb7cd0acf9b | -1.5898 | -52.2505 | 2024-11-28 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 38f1c0b5-2151-38c4-b6e0-8b047dc17632 | -1.5713 | -52.2713 | 2024-11-28 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b1f845f7-6c68-3fb4-98bd-694d5ab2585b | -6.1737 | -42.5985 | 2024-11-28 00:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| fdd88787-fffe-39f5-8197-ffee80153e5e | -3.6963 | -43.4199 | 2024-11-28 00:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5521d0e1-76e5-316b-b8bf-466ff42d9671 | -6.1048 | -48.0327 | 2024-11-28 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 166.7 |
| d03c2a57-22f1-3c2c-be23-204df9b93505 | -3.9674 | -48.0851 | 2024-11-28 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 14ac88b0-877c-35b1-bd66-b070cc35b25c | -4.7907 | -44.4423 | 2024-11-28 00:40:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| d9513743-0f7a-3e40-8db1-3dc4864c4839 | -6.0862 | -48.0339 | 2024-11-28 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 987d82e9-5f26-3077-82f6-dcdaac8ee7f0 | -3.1114 | -53.8041 | 2024-11-28 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| cc978d6f-a65f-3ef0-b989-c63704ba2473 | -2.861 | -46.8406 | 2024-11-28 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 44f05462-b8a1-3fa5-a631-21089ab85ff4 | -6.1735 | -42.6221 | 2024-11-28 00:40:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 710b4cb4-5a4a-3807-83e2-1b3309ef87db | -3.4022 | -50.1119 | 2024-11-28 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| cb9dbd14-02a2-3925-89a5-dea8c19320b9 | -4.772 | -44.4434 | 2024-11-28 00:40:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 222.9 |
| d4c125df-114c-3dda-846b-1cb8981e87cc | -1.5897 | -52.271 | 2024-11-28 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 176.3 |
| a25760d4-64bb-3560-b0bb-115ee01a6284 | -3.6643 | -45.7899 | 2024-11-28 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 92bdebb7-a2a9-3aa8-9eb6-6fa3c843e60b | -1.3329 | -51.9257 | 2024-11-28 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 7821dad8-3207-35c9-8347-e823045f7ffd | -1.3145 | -51.9259 | 2024-11-28 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 3486442c-21bc-3471-aaa4-e2c29b089715 | -2.8794 | -46.862 | 2024-11-28 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 76511f78-9682-37bb-934c-99c79753fc24 | -2.7234 | -48.9034 | 2024-11-28 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 9b50b487-8352-38da-b34a-d51d5c832066 | -2.7419 | -48.9029 | 2024-11-28 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f2c67837-4451-3aeb-841e-3179c33e4675 | -3.3837 | -50.1125 | 2024-11-28 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| d426314f-d8af-3c70-813e-bed696b17a2e | -2.5963 | -53.9771 | 2024-11-28 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 50cc21d6-0ce1-348b-b384-775b75a966b3 | -4.7722 | -44.4205 | 2024-11-28 00:40:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 659.7 |
| 9e88293b-159f-35c1-a3cb-0e2864bc52bc | -2.8347 | -54.1125 | 2024-11-28 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9df7c136-b7fe-30b7-9b2f-f578e3d5839a | -5.9788 | -45.3621 | 2024-11-28 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 6c6e8d22-79c5-3442-8117-952b086ada65 | -4.7908 | -44.4194 | 2024-11-28 00:40:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 239.0 |
| 1870f581-e374-374b-9cfb-17a05f455020 | -2.8795 | -46.84 | 2024-11-28 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 62c7d49a-994f-381d-bea9-259d8648effb | -6.1047 | -48.0544 | 2024-11-28 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4c2ff0d4-dd1f-371b-82b5-8cf4a44bcf82 | -6.1041 | -43.9593 | 2024-11-28 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| ca639060-9e0f-3975-9d06-d5c734f6386f | -1.3329 | -51.9463 | 2024-11-28 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 0ee01444-9fa8-3d7a-bee3-28b3563b576f | -2.8609 | -46.8626 | 2024-11-28 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 83e8171a-eaee-31e0-86bd-280e8594224c | -18.784 | -55.8416 | 2024-11-28 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 9643f00b-d217-3119-b779-f08425771731 | -4.7723 | -44.3976 | 2024-11-28 00:40:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 962c24d0-132f-3da6-b667-90f89b79b82c | -2.8424 | -46.8413 | 2024-11-28 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b4bbcef5-8db4-3132-b762-09768e39494c | -5.979 | -45.3395 | 2024-11-28 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| bfa71d70-4ef8-35f4-b4c1-a3e34c7f12ff | -6.086 | -48.0557 | 2024-11-28 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 2433e966-ff4e-345e-98d9-595d5640907b | -1.805 | -52.742401 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 928eadbb-67fb-3ca9-a476-e4315a180947 | -1.0065 | -51.7183 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f3e54839-3f5d-3e46-beac-2bec40f4a208 | -1.6365 | -52.453098 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1f6d6c-f079-388a-be1e-5b6957d446a2 | -1.664 | -52.939301 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce019bff-0515-3506-a64f-35fc740cc236 | -0.995 | -53.674099 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c763d2c3-8c34-3d9e-a2d7-b563a7d0d38c | -1.3207 | -51.922699 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c3859b7-8564-3cf6-8d97-08a3c7ac8f4b | -1.1327 | -53.736401 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8d37ae-7b95-3a12-bdc2-3fdca274c332 | -1.6634 | -52.708801 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e81a0a8-daf3-3506-81f0-7ae1e63ab7e7 | -1.1005 | -53.365101 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97ffe3f9-a29e-311d-a5a7-fdd09cec853f | -1.6868 | -52.493099 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76fa26f0-5eeb-3ea3-bcbf-f825e1f35f9f | -1.7134 | -54.713001 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5039514b-442c-38c7-b7fd-fcde1a9a059f | -1.6283 | -52.462299 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e416065-caa7-3bb2-a10a-32f576aa6e1c | -1.6954 | -52.439999 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f7edb91-0895-36b3-92fe-a622664bb846 | -1.6856 | -52.4422 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d4f9c6-6d22-3224-b2b0-4a23163aad7e | 1.249 | -55.9673 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98096ea5-4eb3-3a27-b791-1142059d9e30 | 1.8912 | -55.7253 | 2024-11-28 00:41:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 634b083c-b63c-31b8-8d07-ac4aff3a5ee0 | 1.2359 | -55.933899 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9b1948-3aa5-3f10-a2b1-94ce42911934 | -1.1447 | -53.698101 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4760ed4e-1893-3bd1-8f89-d805cd614df5 | -8.1279 | -47.992802 | 2024-11-28 00:41:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0125e731-1767-3539-9deb-2d815ef46c71 | -1.3928 | -55.0284 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c05158a-e9e6-3c27-a80a-34f7cb9c5c79 | -1.7052 | -52.6199 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc020166-8c11-3e05-804d-3960cb767a83 | -8.4996 | -43.273201 | 2024-11-28 00:41:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7b3f24ae-528d-38d6-b55e-5e9b9f4071e0 | -1.6464 | -52.450901 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c46002c-ebbe-395d-9241-8f627b6c9d29 | -1.4509 | -52.589199 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53188087-3a1d-3775-85f5-6da56ab5cb1d | 1.901 | -55.727501 | 2024-11-28 00:41:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b18b8b7a-bdd3-3af7-8da5-876db43128a7 | -2.0435 | -54.669701 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5105eb6-4871-3e8a-829c-8f284fd21676 | -1.1696 | -53.671101 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22b79620-2112-33a8-b2ab-9187f96aac2a | -1.6037 | -52.262299 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 405882a5-96c8-3a1e-b2cb-c6f534b6a75c | -1.0507 | -52.4147 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a69008d8-c272-33a7-aaea-b0505392c7ab | -1.4704 | -54.503101 | 2024-11-28 00:41:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf41ec1d-dd75-3d55-8be5-377db3f94c99 | -1.7372 | -52.032501 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce014e9-98dd-3fec-bc95-48b7e4d7edda | -1.0976 | -54.037399 | 2024-11-28 00:41:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24ca50b6-f768-3210-9d04-41f987263535 | -1.1598 | -53.673302 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ced1b979-4af8-3a5f-a7ec-c2ba7362112b | -1.4371 | -52.664902 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89bb8ad2-f5a8-3e71-b782-d17625d06a21 | -2.1453 | -54.847599 | 2024-11-28 00:41:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05949e43-d82d-3cc0-bfbe-d138fb990284 | -1.3782 | -55.009201 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9cd20ec-eafb-341b-ae40-c0c6587a6a64 | -1.173 | -53.549099 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdcb6c07-730c-3f85-90d2-77915bcc30f6 | -1.6887 | -52.4561 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cba62aa-06a3-3774-ba02-3e2313c179b9 | -1.3871 | -53.6301 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4d62ab7-b807-3782-b92b-3f1dd1671b5b | -1.1349 | -53.700199 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdab5e60-f789-3e14-be0c-a8625c5042be | -6.494 | -47.8862 | 2024-11-28 00:41:00 | METOP-B | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cea067a-14e1-31b7-8e0d-4d4379bb3c56 | -1.1677 | -53.571701 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16af415c-1d2e-370a-a797-3a3833a39716 | -7.6888 | -42.990398 | 2024-11-28 00:41:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 54c402b2-66f3-3777-948b-540b1a462e4e | -6.0964 | -43.987202 | 2024-11-28 00:41:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e0c0945-a8cc-3a5d-97f7-1578889975e5 | -1.7083 | -52.633701 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1818f56-28cd-3fc9-b9f7-29f1c8c86702 | -1.1165 | -53.390202 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac7efcdc-ecf4-321f-8031-5133f6817c46 | -1.5825 | -52.259701 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b21f32e-ddee-3704-be79-a4057c4e2f64 | -7.8108 | -50.002701 | 2024-11-28 00:41:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf2331b3-bc9c-3015-9fba-841700d4d712 | -1.239 | -51.789101 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0132e3d5-5961-31ed-b218-1dc54bd3ab2f | -0.9555 | -51.629299 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb07894-d904-3256-93b3-86905e552903 | -1.622 | -52.616501 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65ba41b1-49c5-3e82-bf70-10fd947f6a52 | -1.418 | -53.402 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa38da0-8c96-3509-ba9f-2574ed1634ba | -1.6738 | -52.4814 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80baa8ac-9094-3620-b90a-39d1c448544a | -6.092 | -43.9692 | 2024-11-28 00:41:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2e800fb-3b83-3ae5-985c-7b85104ac737 | 1.2376 | -55.926601 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c86f679b-0a55-34af-806c-89bdfc749123 | -1.3758 | -52.1203 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 007bf39f-66c4-3f33-8819-6a30e05bd30e | -1.5591 | -52.019798 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 392005f1-63d5-3e13-a5b9-19ebeb2e3358 | -1.0892 | -53.3605 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcf75994-d970-3551-a3e0-d710154a8888 | -1.0907 | -53.367298 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eb9f2e3-6973-3939-9ace-855a0872015b | -1.5207 | -52.214298 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8784fda-9a97-331d-8444-b6f6f10e843f | 1.2408 | -55.957901 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a17131e1-1f35-30e5-aaa2-18a28d693afd | -1.2074 | -53.8843 | 2024-11-28 00:41:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8305658-b98f-37d1-ac58-e0ba882e3d74 | -1.2029 | -51.766701 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce9af98e-75a6-3692-8542-f78bc5e34649 | -6.1643 | -42.635601 | 2024-11-28 00:41:00 | METOP-B | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README16.md)
