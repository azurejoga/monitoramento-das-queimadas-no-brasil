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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5996a682-adef-3c1a-b79a-fed13c8f582b | -15.30148 | -47.94876 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60d68210-1eb7-3c15-b825-540cbfb3678c | -15.21929 | -56.85346 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8f2856d-fbba-36d2-8d7a-07128ab9a23a | -18.23746 | -53.33738 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 402514ed-cbf8-3bf5-be68-a3580cec0b91 | -15.24086 | -56.77313 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f728545-b2f0-3c66-9510-f52e4f6b4a73 | -15.20566 | -47.20075 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02a172a3-6d22-33b4-96f7-9608c15908cf | -14.98844 | -49.98102 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e75a47f-1590-31f3-9ffe-bc17d0299f94 | -14.09666 | -46.34853 | 2025-10-05 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c43f04d-9753-345a-a3af-8bc4100e1e38 | -13.7894 | -47.83103 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 478ba1a0-ea46-3375-803f-80015cb88c68 | -15.61653 | -52.496 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b4259f9-8f72-3eef-864c-1758075fb7d0 | -14.61792 | -48.12471 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4befcd16-ebee-3c4b-b09a-ffec9163bdc2 | -14.6448 | -48.31402 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f694024-28c0-3858-b023-221f46d8a827 | -14.85649 | -60.06953 | 2025-10-05 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8350a17f-2c38-30f2-8de9-b9bb6e5198e3 | -15.35997 | -47.98225 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d09e3497-29fc-3661-9645-c149b2fe6908 | -13.73313 | -51.26818 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 760529b9-801f-3c9a-81b3-c6f130f0ba8d | -18.18724 | -53.35493 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e48f0d6-508e-3e77-b35f-eeb47f39b959 | -15.12158 | -45.73561 | 2025-10-05 04:49:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21823dfe-d3c9-3610-ba69-db3e81d94cb6 | -14.31788 | -45.86023 | 2025-10-05 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d1724f7-fc5b-3b36-a0e5-b3fd6e5531ba | -14.66963 | -48.36653 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2e271214-a735-3ba5-a706-d5e315136b9b | -16.05188 | -50.93768 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7516048a-1b9f-33c0-9dcc-4f62b5339fde | -18.2043 | -53.37635 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0fe83749-ebb8-343b-b89d-d58ed5950ac2 | -15.00897 | -56.04854 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b57c7b97-20d1-39ac-a801-06b2e8f37f19 | -14.7983 | -44.89795 | 2025-10-05 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ff0cd4f7-1379-362b-b93a-221a3c156885 | -15.55206 | -46.8524 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39a6e3cd-7cbf-316a-b75b-988d79ad96f4 | -18.1551 | -53.32024 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7a57633-7661-3385-9303-624deab8bdc9 | -15.2331 | -49.30173 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9266fdb-727d-3275-b048-3ec6fb5c0964 | -16.36448 | -47.05959 | 2025-10-05 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 330e8e1b-328a-3822-a03e-b79d7d39d38a | -18.18394 | -53.3544 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4190a1a-3706-3e0e-a63e-6daaa0078e71 | -14.32166 | -47.67284 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cdc9d8d5-8348-3305-87f4-ff82769deb7f | -15.60761 | -46.95 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6bf844d-6f50-3d30-8f47-3ced7762170a | -16.04784 | -50.94113 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 38857574-f9cd-3b48-abdd-9cfaaeee66e9 | -12.90367 | -54.74449 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52212d38-cd1a-3498-9c3b-b3d4bb859407 | -16.43842 | -52.16312 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29453f11-4ad3-3bce-880c-5fd0fe9963ac | -14.93204 | -46.92253 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edd15111-a4a3-3495-bc5a-098bfec05bf6 | -12.94822 | -54.72808 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cf6cb05-8d8b-37aa-8f82-e376f2124064 | -17.95055 | -47.01942 | 2025-10-05 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95f79490-bfb7-35b3-83ac-bf3754f42583 | -14.97953 | -49.99242 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c85e9988-65b6-3733-be19-9fdb88e31475 | -17.70423 | -56.76762 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c99d9279-8520-3895-a429-dd2aef36560b | -13.73152 | -48.08149 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d10f704f-5d38-3e65-aa3e-7239bf474696 | -14.68631 | -48.3014 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a8a5b8e-3a9d-3dfb-a1ef-08af3d88b217 | -15.22695 | -49.2915 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 365da1cd-efbb-3ec2-8623-5fb78406f254 | -14.68404 | -48.34789 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce09e0b0-97d4-3380-8776-83cacdf2bf22 | -15.9157 | -48.83097 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 12bdc70d-ff96-3534-b586-2dc20d26d888 | -15.23716 | -56.77267 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92149843-705f-3ef2-9a42-438a88b75c6b | -15.19681 | -56.83001 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acc086e5-91a9-3a37-be16-77bc431a8fd2 | -14.68742 | -45.1748 | 2025-10-05 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe17a63a-e0d3-3aef-b08f-ede4421f95de | -16.3481 | -51.47454 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c74a2774-d93c-3634-956c-a97de0133c0c | -15.31807 | -56.93487 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d9483267-17f4-39e9-80b7-6b9d2a647a90 | -15.60823 | -52.46133 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 062c1108-6881-357b-9a5a-9090362398cc | -15.28788 | -47.33066 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dd0f32b-efd8-3f74-b431-db0a925a7912 | -14.30258 | -52.91881 | 2025-10-05 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9efdea65-1507-3bde-a6af-284e866c3581 | -14.16522 | -44.67986 | 2025-10-05 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73253941-2206-3a11-9872-2e9a9411b16b | -17.95808 | -48.53849 | 2025-10-05 04:49:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28357ff6-b55b-34fd-9f87-a7e7218fda3e | -14.60062 | -52.49195 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c85d7067-16a4-3cf7-b9f9-e6ee74999d53 | -16.07797 | -51.07407 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bff9beb8-7f3f-3f80-9d06-3f43da888e2e | -14.92975 | -46.83997 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8b8992d3-5a02-34fe-85ec-c6eccc4cca03 | -18.24457 | -53.35723 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1fa0b060-89ba-3e3a-bbd1-0492c98c64a7 | -14.67289 | -48.37179 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bdff0c5d-90f0-37a2-b3a5-f0f25a27dc1b | -18.2523 | -53.35115 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 264be39a-d0ab-3b06-a8d5-c3821ff53157 | -19.50717 | -50.37135 | 2025-10-05 04:49:00 | NOAA-21 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1d99ab0-7d78-3942-b564-9b495f68e02c | -16.38829 | -52.15458 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d4fc78a-6823-3836-94b7-e971660d27bd | -17.89637 | -57.63805 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2e7ee9c0-d241-3f9a-acea-5fbc9c9843ea | -17.89182 | -57.64206 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c7ca5b41-a29c-3951-b4b4-d82e3746b7c9 | -13.73609 | -48.07715 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ac44d99-91cf-3b7e-928d-03f174a09e93 | -16.38385 | -52.16131 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aabb500c-3510-3192-859c-853d3afabf40 | -14.33062 | -47.6674 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 832464df-48df-35cc-8a68-5fbeecd21eca | -16.00964 | -50.84725 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d36a3f5c-a2a3-3cc3-9e7b-af6a116b8b67 | -12.90178 | -54.75605 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f6b8e01-6273-35c9-8a70-1f8cef47b288 | -17.71577 | -56.74359 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bd1ef5cc-b86e-3325-bb5b-d5a1cb575f1c | -14.87925 | -48.26443 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f177dc01-4759-3bab-a2f1-312828f200c7 | -16.10098 | -51.06154 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19eefedf-af65-3c35-8e6d-a7dbc8b306d0 | -15.91638 | -48.8259 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ac89cee5-aef1-318c-b865-aa4d92db46a6 | -17.56197 | -46.7809 | 2025-10-05 04:49:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae605bdf-f778-3ae5-a8ef-b81af426a58a | -15.59552 | -52.45556 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40803767-d8db-3c8e-8e7f-409d30af951a | -14.68015 | -48.3473 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28d86eaf-f6ff-345c-aa10-e59ad2c4b449 | -15.60108 | -52.50814 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93450485-4981-3013-9ba1-fd113a55574f | -16.9211 | -52.04977 | 2025-10-05 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0197ac7b-619b-381b-95aa-814fbf719298 | -17.92609 | -57.60006 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5304321d-b816-3776-b6bb-a3f5bb540630 | -15.22508 | -56.79855 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f139121c-97ed-3254-8938-be0fac98a4a8 | -15.26004 | -52.9096 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb5c5f70-7500-36ed-8b86-e0fe19febb2d | -15.35596 | -47.98158 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 476d70ed-03cb-347e-a206-1cca135affb4 | -13.73539 | -51.27608 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38c82603-be9d-38e0-afa3-4b795ba53d5c | -15.99172 | -50.92131 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f409e7e8-6d81-3425-8658-0371b2d1a2f9 | -15.00608 | -55.55117 | 2025-10-05 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61a6a349-eefc-3a31-9c3c-cdc854d62b1e | -14.58275 | -52.45216 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 835b0d09-d496-37c2-aae2-173fc0a20ca5 | -14.75375 | -54.65454 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb2efd91-28bb-3038-83ce-44a561f934cf | -14.66779 | -48.35065 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4a3465d-f95c-36ba-a875-79a0d2dd33b2 | -14.93257 | -46.91853 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6079a7d0-f88c-3b1b-9edf-b4016b4b8c76 | -14.61498 | -52.53072 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a21fe46-055a-35cf-8e6c-7fe187c53ded | -14.33677 | -47.6833 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c4e31d1-921b-3437-b993-f373d4d05068 | -16.06686 | -50.90763 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 408fe905-0efc-3910-961f-37ff10e30576 | -17.7106 | -56.77316 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ffa88adc-3377-318c-b7f9-43b744acfcfa | -18.26053 | -53.36371 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7ba8f285-a8e7-39dc-a12d-c18a8f866abb | -14.66642 | -48.36084 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d6fcd2d-c9f1-39a0-a387-b56e7aaaea76 | -15.01252 | -56.0492 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddf87db3-cb39-3a85-b51f-7f3a54d39a81 | -16.03998 | -51.04435 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6eba06b2-b2e3-355a-bffe-c7fe0f8c4525 | -15.69549 | -46.27337 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 832ca58b-3f97-3670-93ae-b406fe8e958c | -15.35689 | -47.97445 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f17c4df2-04a7-3086-bbcf-c8c9dc461d26 | -15.91186 | -48.83038 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cfe3a4ed-bdf8-38ed-9afd-d02c6b8ad58d | -14.8708 | -48.15086 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e9177d9-00fd-315c-b2f3-e1ce044e2b9c | -17.88811 | -57.64137 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |


[Clique aqui para ver as próximas entradas](README107.md)
