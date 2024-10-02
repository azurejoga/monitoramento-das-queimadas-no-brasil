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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d3bd017-e7c7-3e22-a0c3-93f9b5447b6c | -9.50031 | -67.1149 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72f7aeac-5d2c-3fea-81bc-30945356bd8b | -9.49563 | -67.11061 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 396bfe62-d989-3e7d-98ec-bf7cce06236b | -9.49502 | -67.11388 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3569e7d-5563-313a-89d9-fb05e8c047d9 | -9.44801 | -67.16006 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c72cd3ea-3363-3923-a5af-632d9660f727 | -9.44522 | -67.15566 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a05a501-9236-3bfa-8630-d64cfd6b167f | -9.44461 | -67.15903 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11fb8bfd-5945-348e-92ec-ec6db6613aab | -9.44334 | -67.15571 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41c339e4-ea6f-3f47-90f0-08282825da8f | -9.44271 | -67.15907 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8133689c-879d-313a-89b1-878dce7a2f27 | -7.64561 | -67.19693 | 2024-10-02 05:10:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09f2d805-684b-3919-9943-d9ce7e5487d6 | -7.64495 | -67.20051 | 2024-10-02 05:10:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 968a4df1-2524-3139-a5ed-868970d5b366 | -7.64013 | -67.19588 | 2024-10-02 05:10:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 034a9ad7-c0b0-3447-9ec1-b0c6ab8b65ff | -7.63947 | -67.19947 | 2024-10-02 05:10:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16fef102-b38d-30cc-8fa5-9ff8d36d0857 | -7.63882 | -67.20307 | 2024-10-02 05:10:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79f54fb1-98d0-30a1-8477-a24c4e9d15d4 | -9.18471 | -68.29018 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d931965d-827d-396e-a713-deff4fb9cb0d | -9.18394 | -68.29424 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0256ad4a-6b06-3f15-8448-23606b4c0e12 | -9.17895 | -68.28918 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8d461eb-6685-38a6-953e-4a8a54523b63 | -8.78181 | -68.7229 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 262acd2c-21c8-3363-9ebf-9acbe0f31c46 | -8.78098 | -68.72729 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecadfb83-2e3a-380b-99e7-721c91418eff | -9.36488 | -67.56708 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6042495-5416-399b-aa1e-6256c9cf80e5 | -9.3601 | -67.56236 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9fa8004-47e1-362b-ad29-29707710a8f5 | -9.35945 | -67.56592 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cbea00b-e85e-3470-84ba-0aede997b5c9 | -9.31355 | -67.66138 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2173504-03de-39fd-945a-da16797ab044 | -9.31287 | -67.66501 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2bdeb36-3d8b-3639-9a05-64bbcb2b964e | -9.30738 | -67.66393 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5254d4e-e97d-3aac-9e18-f8fc747cc12c | -9.30671 | -67.66758 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4027d80-d4c5-33f4-90db-847d94640a0c | -9.28301 | -67.82613 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f9cb37d-cd9c-32fb-a2b3-f3372186a4f0 | -9.28232 | -67.82983 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40e57420-6911-3fd1-a060-8deea12b1dc0 | -9.27977 | -67.59885 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bcfc6b2-00b8-380a-8fe7-baa43df094af | -9.27959 | -67.84454 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1439fb3d-5580-32bc-b4a6-1da56e245dfd | -9.27891 | -67.84819 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2048ec2c-e879-3cea-95f4-4d625b63cc14 | -9.27398 | -67.60249 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30218426-cb3f-3497-80a2-4ce5b6d52879 | -9.27362 | -67.6014 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a86cbd6e-1fc8-3436-9fa2-bf6daf6bc15f | -9.27294 | -67.605 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03c36cf0-60f6-3ba5-9fc9-01493281cfc6 | -9.27268 | -67.60971 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 796e4b94-93fc-3743-99bd-2736e7a72995 | -9.27227 | -67.6086 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 772084ca-8d9d-3976-a5cb-10ef2d801ffd | -9.27202 | -67.61333 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec113ebb-35e6-3f6b-9580-d6fb68ce8ceb | -9.27159 | -67.61221 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 981808c8-c29d-3bb6-9f20-823bb925f63a | -9.2685 | -67.60146 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4ccc6a5-a971-3b26-8dd0-77f5b54ae2ed | -9.26814 | -67.60038 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46ef0460-89c9-37b0-a392-12add2e36add | -9.26171 | -67.60762 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 971878d6-357d-3f22-84b8-e8b27599b4e6 | -9.2613 | -67.60654 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1db14a9-5f1f-36eb-bd97-c4e0daa5dd76 | -9.26106 | -67.61122 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9116ad67-57e1-3e1c-a6c2-3da5a36a101e | -9.26062 | -67.61014 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd2b4621-a3c4-370c-9116-aebcb23769b7 | -9.0812 | -67.57128 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c9e7983-9805-3eb9-9b1d-72f2ad903d21 | -9.08053 | -67.57487 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d3d60b3-ecbe-30d7-8764-99f1167c7c28 | -9.01445 | -67.38353 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 726cb8e8-ec57-35f1-9d47-fe856b98bd1c | -9.0138 | -67.38703 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ede7d94-a5cc-3b0c-998f-0948bb95e478 | -9.00267 | -67.44694 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9548810-313c-3b1a-a7e2-37e7d804f8b1 | -8.99792 | -67.35181 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad4932e1-a482-33b4-8f4f-a2b375527874 | -8.99728 | -67.35522 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96b789e1-b677-3601-a222-43be7d9fe500 | -8.99723 | -67.44587 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c47ae50c-95e5-3bb1-853d-80e5015771a9 | -8.9966 | -67.35176 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ce4ea36-9add-3957-b902-83cc9022cb58 | -8.99658 | -67.44939 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01278170-18bc-355d-8640-1a408af17def | -8.99599 | -67.35518 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e972b8e-6d07-3236-a457-345cc7ccda2f | -8.99251 | -67.35075 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d43d7f7-08ad-31d0-9f1b-bc090a2d0970 | -8.99187 | -67.35418 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 750843e2-122c-3854-8eb0-df21f93e1ff8 | -8.99119 | -67.35069 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9189345d-5124-3c9a-89df-8bcbe00f91ae | -8.99029 | -67.42268 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65347ec1-7bd9-3d5d-bd0a-630cfce44488 | -8.922 | -67.39163 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 536b81a5-400b-342f-b817-c7ea84995131 | -8.92136 | -67.39513 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c95768ba-90f3-3d2b-8f70-c03c958d608e | -8.92071 | -67.39864 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef9c3c45-5890-3156-805e-7de8e2961583 | -8.91657 | -67.39061 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd22e4ce-4630-392a-9df9-0f94000dc5fe | -8.91592 | -67.3941 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52f90fc9-7108-3e54-84f1-e09ff638f002 | -9.19898 | -67.39799 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2182161-1ed7-3fc0-bf4c-3b8c01cf1ccf | -9.19356 | -67.397 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23aefea9-6b67-38c4-9f2a-dcad979ceeb9 | -5.95195 | -43.26923 | 2024-10-02 05:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6b7b41df-eefd-31f5-903b-2cdc3c3f0b5c | -5.94474 | -43.26805 | 2024-10-02 05:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6df3346d-7df0-3f42-a5ae-07062c478d65 | -5.88794 | -43.72174 | 2024-10-02 05:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f45547e5-0ee3-326d-93a4-61adef9ee814 | -5.88504 | -43.71985 | 2024-10-02 05:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca358e3b-2b6a-326c-b589-e13af475c211 | -5.88415 | -43.72659 | 2024-10-02 05:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c83184d-aa58-34b9-9ba9-43a1c17ad6b5 | -5.8809 | -43.72071 | 2024-10-02 05:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2997c8df-a223-3fef-a12e-a9bb420ee35d | -6.39994 | -44.74872 | 2024-10-02 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9ae5fe5-cd1b-3f9c-b530-9ab0b502f303 | -6.39916 | -44.75455 | 2024-10-02 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e4ce9c70-d911-3642-9965-afc4d3f92a99 | -7.70055 | -44.92774 | 2024-10-02 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3a30418-33d7-3db7-bc8f-14fd083d8617 | -7.69384 | -44.92685 | 2024-10-02 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8e6e7fd-1379-35b4-aacf-59447928a9b7 | -7.57411 | -45.01098 | 2024-10-02 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4a8c5ed-f910-31ef-9c4f-61c467be4dd6 | -7.5674 | -45.01039 | 2024-10-02 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 428f1af6-f02c-3793-a29a-128cf0b12e4a | -6.602 | -44.17955 | 2024-10-02 05:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30be852b-bd62-3914-888f-6f78fa9344aa | -6.59502 | -44.179 | 2024-10-02 05:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2c07dc5-cc0e-301e-ad75-9a60cd67e4df | -9.01918 | -45.21733 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d2ff9eb-9191-30dd-a0b1-af6832339ce3 | -9.01839 | -45.22398 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7d62675-cf57-3842-b575-618c73e801fc | -9.01766 | -45.23006 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d1a8e70-cdcc-3c46-adb2-51f1db4f3bc7 | -9.01685 | -45.21735 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a040b87f-1847-3513-af36-0b4fdd3ee7a1 | -9.01602 | -45.22392 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a97d4ad6-8599-3642-bdec-e339961e0d89 | -9.01526 | -45.22998 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf4662c5-a4fd-3875-a119-45b8ba93a29f | -9.01104 | -45.22849 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7a347dc-f4f6-3cf5-b7ff-58c6a467ac6f | -8.89649 | -44.09583 | 2024-10-02 05:10:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47ff2d6e-fc13-34e0-bf33-63c398129ddd | -8.89568 | -44.10255 | 2024-10-02 05:10:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 609418b6-2c4d-3a20-a2ac-bb9413a970b0 | -8.89297 | -44.09639 | 2024-10-02 05:10:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73bc187d-6b10-37c3-adec-ae5e73886f17 | -8.7104 | -45.22688 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9feb434a-9cfb-3dbc-a249-c8616b2b24e1 | -8.70302 | -45.2318 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6794935-a483-3266-a264-4f47363c4507 | -8.70235 | -45.2374 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3791ef8d-20d7-34ff-9e75-2f36e00a9f17 | -8.69853 | -45.23722 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb64953f-c0db-386f-8f15-a5b5a3681de9 | -8.69559 | -45.23718 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62ae6417-e68d-3721-9f46-fc1a56dbfc9f | -8.69251 | -45.2312 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63614818-9022-3fa5-bc07-9ce01f9d6957 | -8.69179 | -45.23684 | 2024-10-02 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 433f7a32-4c69-3d0d-a941-d6b2b0f4bb1a | -8.20904 | -44.35838 | 2024-10-02 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cdbfc61-7432-3fbd-b42d-ba231cfc81da | -8.20787 | -44.35752 | 2024-10-02 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f33e40a-1758-3e20-aed3-7c00899263f1 | -8.20709 | -44.36386 | 2024-10-02 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96599610-bd57-36e8-b0de-1cd595646896 | -8.20198 | -44.35804 | 2024-10-02 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README129.md)
