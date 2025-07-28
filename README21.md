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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a52296f4-2a5d-3131-98ca-c03065e8cba2 | -14.1322 | -45.2878 | 2025-07-28 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 1afdf433-c7b2-37c4-978e-4d9038503075 | -10.6172 | -45.2282 | 2025-07-28 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 591fc68b-d97d-358e-a4b9-ecf5f0d2e83f | -7.1074 | -44.9074 | 2025-07-28 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 810c5d7d-36af-39d4-bfcf-e5029a3ec821 | -2.8984 | -42.5674 | 2025-07-28 13:50:00 | GOES-19 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| feec54a0-805a-3c13-91e9-31617ebe9a14 | -7.0881 | -44.9547 | 2025-07-28 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 1b040f7b-3ce4-3fa7-9686-c933bb05fd4f | -10.6363 | -45.2257 | 2025-07-28 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| d7200afe-8c5e-373c-9845-636b564df697 | -14.1327 | -45.2644 | 2025-07-28 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| d3bbc434-8573-3ce4-bd31-6c4a451e0cda | -7.1071 | -44.9302 | 2025-07-28 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 64a22275-1ebd-38a1-a61b-75aa4c5bb5c6 | -10.8417 | -46.6739 | 2025-07-28 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| ea0c235b-51f4-3823-8190-ce56672b415b | -7.0881 | -44.9547 | 2025-07-28 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 303a06fa-f4bb-3914-be82-e7ddf9b48a97 | -7.1071 | -44.9302 | 2025-07-28 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 8ca8e6fc-2b2b-3e7b-bebf-be8c1dd95636 | -7.1074 | -44.9074 | 2025-07-28 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 62515ced-7c4b-3e07-af29-042b26f5e0bf | -7.0883 | -44.9319 | 2025-07-28 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 24914f8a-d81e-3552-b665-d10d05689860 | -10.4347 | -47.2155 | 2025-07-28 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 6fd9bef0-400f-3c03-ad20-4107d5368190 | -7.1069 | -44.953 | 2025-07-28 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| aa5706b0-7bf4-3054-af2b-9939dc1d9f34 | -10.4154 | -47.2401 | 2025-07-28 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 34b6aa3f-5613-3de5-9d7f-d0ac3613e944 | -7.0881 | -44.9547 | 2025-07-28 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 93002686-2477-3658-bb9a-b7012b19aaa2 | -14.1322 | -45.2878 | 2025-07-28 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 439a86f1-aa02-3538-878d-a3d95f223e1a | -7.1074 | -44.9074 | 2025-07-28 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| d885c683-7cc0-3b55-be99-70684601055f | -7.1071 | -44.9302 | 2025-07-28 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| d49cdfba-e7b1-3a41-b569-e1d766c0a469 | -10.6172 | -45.2282 | 2025-07-28 14:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 49fea024-b914-3818-adaa-4d2c367aa028 | -13.4873 | -45.5601 | 2025-07-28 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a75e5c1b-301e-35aa-af3d-c75f978f178d | -7.3389 | -44.3593 | 2025-07-28 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 45040cfc-c59b-3019-99d1-bfb0ffcdde90 | -14.1327 | -45.2644 | 2025-07-28 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 72e01614-7b53-306f-ab21-037f855f4d35 | -14.5098 | -48.6529 | 2025-07-28 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| bed95077-40fb-36cd-badf-659ea37c7303 | -14.1322 | -45.2878 | 2025-07-28 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e00da0b8-4615-3be6-bb75-e839e20e753a | -7.1071 | -44.9302 | 2025-07-28 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 2ac77bc4-7f02-3aba-b5fe-cdc1f6554f79 | -7.0881 | -44.9547 | 2025-07-28 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 394381da-f17b-387f-bb02-8078fe9f74e7 | -10.6172 | -45.2282 | 2025-07-28 14:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 6eb07ccf-43fd-3de5-972b-83228fa38f33 | -10.8608 | -46.6715 | 2025-07-28 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 42733690-174e-3903-b3f1-6a0483bc47c5 | -7.1074 | -44.9074 | 2025-07-28 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 4712e6bc-8b15-303e-9b27-19edb96efd0b | -7.1071 | -44.9302 | 2025-07-28 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 6687df94-383b-3dab-8ec7-9768001ef85f | -10.6172 | -45.2282 | 2025-07-28 14:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2171f189-9726-3f15-963d-8da880e03f31 | -7.1074 | -44.9074 | 2025-07-28 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 383c1a51-468f-3a59-9ea3-7dc93543d749 | -8.8698 | -48.4605 | 2025-07-28 14:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| acc84e9d-ad10-3643-aff8-6514aae9b8c1 | -13.4873 | -45.5601 | 2025-07-28 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 4f84b4cb-1304-3013-af40-62f4f85abb01 | -7.0881 | -44.9547 | 2025-07-28 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 1d7b85b4-7834-3062-9a71-521430c7a012 | -14.1322 | -45.2878 | 2025-07-28 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| e0eb0ddd-ce69-3886-864f-2bfeab5f8de6 | -14.1327 | -45.2644 | 2025-07-28 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 502ba95a-4d70-3d34-9a5e-18ef6bfca16f | -14.1322 | -45.2878 | 2025-07-28 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 1e5fca38-e28e-3c7a-8857-cf5e227da05c | -13.4873 | -45.5601 | 2025-07-28 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 6360e39f-f1fb-3a49-9652-c111a330a70e | -14.1327 | -45.2644 | 2025-07-28 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| ff642c4f-c30f-38bf-89a3-d2fed398459d | -7.1074 | -44.9074 | 2025-07-28 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 85ee89e7-fbc3-3b38-8f93-cd924c4c490d | -7.1071 | -44.9302 | 2025-07-28 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 795b5cec-276d-3812-baff-3ab9c7db51d8 | -7.0881 | -44.9547 | 2025-07-28 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 79f3a888-6478-34e4-9dc1-388f729d7b54 | -8.8698 | -48.4605 | 2025-07-28 14:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 5a329932-f0d5-3091-a96b-0590a8ef06d5 | -10.6172 | -45.2282 | 2025-07-28 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |


