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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a19cc08-9c01-33d4-b3d3-e0580327821f | -2.49386 | -49.04803 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0870e713-47cf-372d-8e46-d7f4168f5959 | -3.46982 | -50.53388 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c6c6ea70-1bd8-3a69-9f0b-ae336c23423c | -3.092 | -54.12663 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d6a3071-7b91-3b09-96c2-346d76ef3ff6 | -2.5727 | -51.83704 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2daf5bda-0e36-31b1-8560-79075f34eeb4 | -3.2894 | -53.66806 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 375cf2a9-0701-300c-8a49-07c5b6ca7eae | -0.92246 | -51.63514 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 833d162b-9215-380b-bdab-41832a85ff9b | -3.2322 | -54.09911 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0daaa4c3-e106-38e2-9e96-8d71b926f398 | -2.839 | -48.47253 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f6aa263-79c8-3766-819f-7d42ce4609df | 1.22879 | -55.9339 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2feb13b-a55b-336c-8152-149cecbe041c | -1.71821 | -52.77053 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9fbb498e-9d62-3578-ac6e-24450db73d54 | -2.78937 | -52.99018 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83cd9a4e-f383-3b97-bf16-a7fa6b405c36 | -1.72546 | -52.78933 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cefdf2c-f9c6-37b3-b56c-6ad929cf5da3 | -4.05901 | -49.97096 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0f1aa6d-2352-376c-8de4-70d63b2cce9f | 1.25154 | -55.91335 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9e3c61-55bf-3029-b562-dbf66617879e | -1.70881 | -52.76554 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 953ea751-bcac-3959-b667-0e4d13497812 | -2.60156 | -54.21556 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd2a3cff-cb22-3b2b-9a69-2308cca33c50 | -1.57832 | -52.27076 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a140573-fdf1-3cbb-b95b-f1a990692078 | -2.59652 | -54.03096 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43d1dba8-07db-3d99-86fb-0f5512de1c85 | -1.35244 | -52.93583 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3ac0ca0-f8f4-3cc8-9750-e64aae1fe405 | -1.56797 | -51.98304 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a7ba612-9792-395d-a694-c9911218a96b | -5.76593 | -43.3979 | 2024-11-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9009f5f2-b29e-3f79-af8f-a5f7ca9c3576 | -3.96656 | -47.94605 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0ce7ab22-dec2-3aa7-8222-93e99569e308 | -1.62539 | -53.86811 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 19655921-174f-3c56-ad23-aff867aeb366 | -4.91309 | -44.02991 | 2024-11-29 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42362e1c-d0cf-39dc-9b1a-4ad7c149a01a | -3.96009 | -48.82932 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a132c23e-08ea-3bd5-899d-8f15a1685eea | -3.04168 | -54.03363 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cab49a2b-58c6-3203-9800-3bf749544a41 | -2.40949 | -57.72263 | 2024-11-29 04:57:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37343fd0-5b6e-38a2-ba33-5674311476f0 | 0.71786 | -51.46459 | 2024-11-29 04:57:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b5c8b926-6802-346d-a322-358c82051073 | -1.81172 | -52.19149 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caeee58f-5d51-39d3-8fe6-fd097497ad2a | -3.24685 | -50.59606 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d85e80b7-4995-30ec-92fc-b5d84a11923f | -3.25078 | -53.63029 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d836f8d2-3185-3e97-8424-be18b79a165c | -3.53289 | -50.19322 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56a35ae6-5f98-322b-b586-70a8a8b0fe9b | -3.61902 | -50.19087 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8306f3d6-c08c-331e-948c-cbe3e257cb2f | -2.18252 | -53.26223 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c35fd93-e147-393b-8fbc-4a2c4bdf8f6e | -1.95016 | -52.96174 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a9db340-f907-3f5e-9262-8d2ab128298e | -1.31729 | -51.73935 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 83fa9016-0340-354b-aeb9-957efce06829 | -1.58834 | -52.2723 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7cf1f4d5-fb84-38f9-9079-03d6c9ca3a3c | -1.98593 | -50.66972 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50b3c5ec-0029-3ae2-9b32-17c4a8f1c6a2 | -2.75847 | -54.12737 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b0fe7b4-6f4f-3075-a9ef-5fb6b9703bc2 | -3.73277 | -54.22738 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6abc3d5-6f78-3749-98e8-c30e34bd784e | -3.50175 | -53.81062 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 990987c9-caa4-3854-9a4b-41e3ba58782b | -1.70272 | -52.76107 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef5713ed-71c3-347c-8451-47d49f25721d | -1.41374 | -54.80814 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a896a933-ddc3-30a3-8e07-f68bab0a8d47 | -2.6662 | -48.7868 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| e97e99e6-5e12-3864-a1fa-791ae7332f38 | -3.74163 | -50.79178 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5c0276c7-fa8f-338d-88ff-618fd8a5b798 | -2.79237 | -54.214 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c510b04a-32a0-3c53-a77b-d17cf966e88e | -2.36474 | -54.35971 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4df2b9b-020f-39c6-b461-0c720c943c4c | -3.12839 | -51.04057 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5513ee72-b8b8-3a82-8e74-be380ee8840e | -3.70335 | -47.12854 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e99c382-14c2-3e24-9d4e-a6454eb6127b | -3.20711 | -53.84509 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71345d78-23d4-367d-ad42-8aa201b6b28a | -1.60216 | -54.64351 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04d51d09-b885-35de-b49c-84c34ed45219 | -2.69418 | -48.65704 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4099e2b-2e28-3df1-9a97-bca3faf76645 | -1.70013 | -52.45069 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 2d7b9b81-f39c-351b-836e-a5916c98d1f8 | -1.408 | -51.58599 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3d90154-d898-35ff-b244-b2c216217ae2 | -0.81671 | -51.61498 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82881015-612a-3d4c-94d0-eb861318c235 | -1.02975 | -52.16784 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c752c8bf-1fa5-3c75-be26-d9118126d3ca | -2.31721 | -51.96185 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7274d78a-9e38-3e4e-bc48-2665f7d64277 | 1.28366 | -55.92979 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fabf72e-0bf3-31b2-b7a5-f58f6446474d | -1.00063 | -51.72054 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42232b56-61b7-35f4-bdff-98a101333b47 | -3.64267 | -50.28367 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4133ece2-4185-31e8-9b41-9ab716c8033a | -1.71266 | -52.7626 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a66701ad-0c45-32d7-8321-a3eb1e0c3080 | -3.68075 | -54.44868 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91ee320e-3888-3c92-9ac1-349a7498b367 | -3.27776 | -50.0182 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33a6fa53-5738-3039-b778-43412fef72f8 | -1.27059 | -51.62902 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 323a1f2e-e33e-309d-b456-aeb0f0ec2744 | -2.25598 | -53.74867 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83bcf798-d9bb-32e7-9abc-d329b6d56c7b | -2.55193 | -53.98866 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbc1d258-8818-3aea-921b-54aa9c592596 | -3.34703 | -49.50629 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b63e7a53-8a46-37de-b646-c9c00c50ffa1 | -2.53501 | -54.03196 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec9dd42f-80a8-3c53-9e05-6de2ef2cee8d | -3.64029 | -54.2089 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ff3b5b7-eabc-327f-a038-bfde3c0112e3 | -1.20081 | -52.09742 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9f7c344-af9e-3c05-a2f8-1b5ef220968b | -3.0737 | -53.91538 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9de30443-9fde-3787-a357-2edb319c68e5 | -3.11767 | -53.26421 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5067e3a-23e6-3dc3-af6e-8fc038985d79 | -2.59834 | -54.08424 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 502edba0-42f4-321a-b99a-c7c42d634585 | 1.8512 | -55.79852 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 535724c7-9646-3eb4-9257-b6acfeb4f7b7 | -2.57584 | -54.29318 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16633d3f-69d8-3325-9498-dcf991b80323 | -1.11109 | -53.2177 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 885febb5-8230-3733-b8dd-8d33a869f111 | -3.70701 | -51.80334 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59b79695-8d31-3502-8bcc-d35df531aae0 | -2.80303 | -48.68052 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed2a51ab-53b0-34e2-8c01-ea136485ca1a | -1.52403 | -52.03111 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3479818-34f2-30ef-ad45-f34c0d8c83ff | -3.05329 | -54.04599 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b8886963-30fa-321b-9638-0f06076534db | -3.09935 | -53.72942 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc6a0af0-e628-32ce-b5e6-3a2d7b21ecb4 | -3.04054 | -48.51753 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bca4fdf1-51c8-3944-b322-2265117281c0 | -1.13445 | -53.80839 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aee90d1b-518f-39d4-be81-0cd966dbe5a0 | -3.26199 | -53.82208 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a501f2c2-9f41-37f8-abff-e408c97aaafc | -1.28413 | -51.65335 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 168e96ff-0e12-3dcb-860b-9f6a204b0518 | -1.36417 | -52.24827 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf273529-5de9-3a6b-b314-0c3e4c027be9 | -2.4539 | -54.0089 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28a88a51-eb59-3a18-8dfb-a8c319625503 | -4.66615 | -42.38018 | 2024-11-29 04:57:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ede15d21-adf6-3e33-94a6-5645e9fd7ddc | -3.15889 | -53.23877 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c75ce8f3-9f6f-3a31-8998-56ace07e023e | -1.27387 | -52.69753 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 040e336d-e535-3fd6-8da5-6de2f2c1d543 | -2.79515 | -54.04477 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd5cb4da-519d-3569-931a-0c46c55f7626 | -2.4512 | -54.02612 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae63e4fe-c938-342d-b8cb-216db526feae | -3.41691 | -53.21904 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abc6445d-8723-3d4c-aab3-ba85463a0ca4 | -3.55639 | -51.66659 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d009fcd2-8102-3f6f-8f52-9c953dd65be1 | -3.54746 | -50.41608 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| caa2e320-dba9-3792-b191-eba08695a2f3 | -2.60926 | -54.20969 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b1914c8-8c3f-340f-a214-0426d8c4bb38 | -4.43101 | -46.58188 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1c76db0a-a7fe-3593-bec7-6db3ab49c58b | -3.37408 | -50.17556 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf028fce-b4f7-3948-9e76-dab3dea3c7c1 | -2.8273 | -54.09912 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40ea6113-f06d-33d1-a010-40f17a9cde9e | -1.78847 | -52.73524 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README44.md)
