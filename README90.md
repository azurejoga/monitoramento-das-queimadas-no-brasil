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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92e9e822-2c13-317d-9b37-a0c00dfd2426 | -9.699 | -54.8176 | 2026-09-18 07:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ff55032b-e929-3b82-b5bc-c6acff576383 | -9.7177 | -54.8162 | 2026-09-18 07:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| f52c7f08-b9ce-3a9d-a0a9-efa700074519 | -10.6568 | -50.2426 | 2026-09-18 07:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 02f2f786-a69a-3b8c-86af-c29a5e4d71d6 | -10.6571 | -50.2212 | 2026-09-18 07:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 4a551173-76f2-3b81-94cd-2c5357eebc90 | -10.6755 | -50.262 | 2026-09-18 08:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 10e6df0f-c542-3299-8efc-49283a0f455c | -10.6571 | -50.2212 | 2026-09-18 08:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 108b4db2-f619-3b82-8adb-b35ef4213c0e | -10.6944 | -50.26 | 2026-09-18 08:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 6aa579b5-ef68-31a6-bd83-eb05ff158a92 | -10.6758 | -50.2406 | 2026-09-18 08:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| f2631748-565e-32b6-bcd2-9a2ae252e4a5 | -9.7177 | -54.8162 | 2026-09-18 08:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 8b224893-3336-37ac-88e2-05b4b5d0bab1 | -10.6568 | -50.2426 | 2026-09-18 08:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e9ec1e48-a86c-3bb1-a51e-732c23852be5 | -10.6755 | -50.262 | 2026-09-18 08:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b343a791-e60f-3d26-a501-3c4548f4cad7 | -10.6758 | -50.2406 | 2026-09-18 08:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5db49fe6-c46b-37c1-b917-5eb6e84c8a3c | -10.6571 | -50.2212 | 2026-09-18 08:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 9a721ed6-9bf2-31ec-b89f-977adf1a1ccf | -9.7177 | -54.8162 | 2026-09-18 08:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 416ea34a-3146-3094-b3d7-7f2c68129a9e | -10.6568 | -50.2426 | 2026-09-18 08:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 226358c3-f709-38de-9095-1a175e89f990 | -10.6758 | -50.2406 | 2026-09-18 08:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 8d585bc4-25b7-3e84-bf49-cf38650bd87b | -10.6755 | -50.262 | 2026-09-18 08:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| efcb1c2e-ae29-3944-97a6-d97bbc0730be | -10.6944 | -50.26 | 2026-09-18 08:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 81e790c4-92dd-3e23-bf88-df22b19978c5 | -9.7177 | -54.8162 | 2026-09-18 08:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| db04a21b-a750-317b-bc41-14cc7287ba19 | -10.6944 | -50.26 | 2026-09-18 08:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c0af8e2d-dac1-382f-a6ef-22e91da60e7a | -10.6755 | -50.262 | 2026-09-18 08:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| e01465ad-8655-33db-bed0-05b7cd7eaead | -10.6758 | -50.2406 | 2026-09-18 08:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 9f9fe3a1-1bf2-340a-b138-13465dc26d00 | -9.7177 | -54.8162 | 2026-09-18 08:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 22d70366-1b36-37bc-8461-7f26c80c39ee | -9.7177 | -54.8162 | 2026-09-18 08:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| b379433e-200d-38ff-b22b-6851beb6ebf7 | -9.699 | -54.8176 | 2026-09-18 08:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e2b64843-8d7c-3502-8914-2b6652b69a30 | -9.7177 | -54.8162 | 2026-09-18 08:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| bc068e19-8c64-3b87-83e7-c4f9dfb184e4 | -7.03 | -44.67 | 2026-09-18 09:15:00 | MSG-03 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0286da-cd16-3fce-b71e-51babd8bb590 | -11.8115 | -46.8158 | 2026-09-18 09:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 2f1f1ecc-ad91-36c3-80fa-facdaf9dbed3 | -7.0161 | -44.6642 | 2026-09-18 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 3bcec631-e06f-3e45-8336-3f04bb5915ba | -7.0349 | -44.6625 | 2026-09-18 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 232.6 |
| e33cbf76-89e8-3c2d-96d8-0d844cacf454 | -7.0352 | -44.6396 | 2026-09-18 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 11927dff-05b7-3632-803f-8f69e1e06e5b | -7.0349 | -44.6625 | 2026-09-18 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 565a5447-1def-39ad-9526-1002396cd70e | -7.0161 | -44.6642 | 2026-09-18 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 182.0 |
| fc9f4bad-f951-335c-8af3-ef30f6c4811a | -7.0086 | -43.6264 | 2026-09-18 10:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 6256cec0-52fa-3e30-b82b-be254151e228 | -7.0161 | -44.6642 | 2026-09-18 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 7f60a920-fda8-349e-9aa3-d0e1b8bf244c | -7.0349 | -44.6625 | 2026-09-18 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 179.1 |
| d9d3e70e-59e7-3b8e-8f32-08246f531bb1 | -7.0161 | -44.6642 | 2026-09-18 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 210.8 |
| 25e182f8-b812-3e2c-986c-065aafe670f9 | -7.0349 | -44.6625 | 2026-09-18 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 217.4 |
| c6faf777-8d3d-3e4b-8ce9-c3c9b52f697a | -7.0086 | -43.6264 | 2026-09-18 10:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 8b82dbca-a5e7-3528-8825-1fcd0670af50 | -7.0275 | -43.6247 | 2026-09-18 10:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 140.0 |
| fb6b38fd-c1e5-394b-8772-790b39437f22 | -6.96889 | -37.98975 | 2026-09-18 10:47:00 | TERRA_M-M | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 87d964a5-76cc-3013-8520-26e276295a9c | -7.0161 | -44.6642 | 2026-09-18 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 240.9 |
| cb0aa214-4143-3491-ae96-4b23a88914b6 | -7.0086 | -43.6264 | 2026-09-18 10:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 197.2 |
| fc25eed1-1c50-3220-913f-b009b9520406 | -7.0349 | -44.6625 | 2026-09-18 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 4a5b3376-c2ca-3f27-ae74-5501715aa9cd | -7.0164 | -44.6413 | 2026-09-18 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f040cf8c-574e-3744-8999-59a3aa237743 | -7.0275 | -43.6247 | 2026-09-18 10:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| fb20ee94-b071-389c-bb55-4acb0902c661 | -7.0086 | -43.6264 | 2026-09-18 11:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 249.7 |
| acc33142-6f97-3c26-9801-584716e28acc | -7.0164 | -44.6413 | 2026-09-18 11:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| a7550b21-7435-3034-977b-250a9781b3e3 | -7.0161 | -44.6642 | 2026-09-18 11:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 368.5 |
| e69e7515-91c4-30c9-8bc8-6052ebb0e183 | -11.8115 | -46.8158 | 2026-09-18 11:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| cab5aa68-8e15-34f7-ac45-f135c8c4d1f0 | -9.8316 | -48.3854 | 2026-09-18 11:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| acdcfaba-6f5e-39ba-b764-977fea61a5e8 | -13.6725 | -45.9668 | 2026-09-18 11:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 753ee0db-9caf-3eb6-8db0-db719b043b64 | -7.0275 | -43.6247 | 2026-09-18 11:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 9c3258a3-0436-38c8-943b-1b0326862ceb | -9.8316 | -48.3854 | 2026-09-18 11:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 958bdbf1-4a62-35ce-a289-825437ef8742 | -13.6725 | -45.9668 | 2026-09-18 11:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 257.1 |
| 61b853bf-61b5-3694-9fda-aa2653296352 | -7.0086 | -43.6264 | 2026-09-18 11:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 146.2 |
| af9055d9-a157-3a63-b125-68b4f7aeb89b | -7.0161 | -44.6642 | 2026-09-18 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 352.6 |
| a5b52e29-4138-3fc1-a541-620711d7c93d | -9.8505 | -48.3834 | 2026-09-18 11:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a93d3105-9cae-33ac-9c91-3bf13eb8c808 | -7.0164 | -44.6413 | 2026-09-18 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| bd5b3734-9771-3bc2-8267-5d5fd886ce8b | -7.0275 | -43.6247 | 2026-09-18 11:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 9ffbf186-0257-3d7b-81e1-a7ced5b1d1ab | -7.01 | -43.62 | 2026-09-18 11:15:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5396d8d0-2fc3-3a92-a997-3b211acdd297 | -7.03 | -44.67 | 2026-09-18 11:15:00 | MSG-03 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 379ae256-a9ff-36d8-8b53-34c238e2e120 | -7.0275 | -43.6247 | 2026-09-18 11:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 483d30cd-4bd2-3ca5-b462-9a24873827eb | -13.6725 | -45.9668 | 2026-09-18 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 312.0 |
| 65c283ab-9662-3532-a8af-2bbd199f34b1 | -7.0164 | -44.6413 | 2026-09-18 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 015bec7c-3b92-3343-964d-a63226b81b18 | -11.8115 | -46.8158 | 2026-09-18 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 84ef0551-78ef-3f48-abd9-171e49b77d8d | -13.6531 | -45.97 | 2026-09-18 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8f5766a0-fb79-387d-8d4d-55ddf89b9fdf | -13.6721 | -45.9898 | 2026-09-18 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| d9bdd1a0-63e6-3de7-a473-d704dc6d5655 | -9.8316 | -48.3854 | 2026-09-18 11:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| c43c523c-40cf-3d07-a148-5f4fe6afc6f2 | -7.0161 | -44.6642 | 2026-09-18 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 344.6 |
| 2e598714-2dc4-354d-8ff7-8dfe9412eb34 | -7.0352 | -44.6396 | 2026-09-18 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8f141e4f-b543-387b-9590-98e69f500789 | -11.064 | -48.2898 | 2026-09-18 11:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 9ab44140-5876-3787-a80e-050141721e84 | -7.0164 | -44.6413 | 2026-09-18 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 152.8 |
| b4a6725e-6a62-3397-a751-f02e7285c0a8 | -10.6944 | -50.26 | 2026-09-18 11:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 84c0ecdf-e48d-3a2b-9364-69e3b6fbce16 | -13.6721 | -45.9898 | 2026-09-18 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| b04ff0b8-1f1e-3edb-abfc-f1b908ef30ff | -7.0161 | -44.6642 | 2026-09-18 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 406.3 |
| 2afd5c0e-58e0-352a-b24c-951cb2c14c9c | -8.4675 | -44.4984 | 2026-09-18 11:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| f4a9db7c-788f-3e4d-8579-d8a6320ce9e0 | -9.8316 | -48.3854 | 2026-09-18 11:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| a739dd51-f2a6-313c-a3c3-ab2080074293 | -13.4303 | -51.9036 | 2026-09-18 11:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ecf4c0a4-cc8d-302b-a664-1cf3cf012571 | -13.6531 | -45.97 | 2026-09-18 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| a117c67f-f86c-3b50-b556-b54bb886864e | -13.6725 | -45.9668 | 2026-09-18 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 339.5 |
| e31dea9e-3de9-30ef-815e-514b27d92712 | -11.8115 | -46.8158 | 2026-09-18 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8cd23021-b7a9-32da-a2a9-ba9e2958c5a3 | -11.2975 | -43.3851 | 2026-09-18 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| a93a5f44-ccaf-3741-8f8e-73be18654bff | -9.8502 | -48.4053 | 2026-09-18 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f50bf30f-38be-3aaf-961d-419774773cb7 | -9.8505 | -48.3834 | 2026-09-18 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| c504d2ad-6fd5-36f1-be12-3ad1c2e1b095 | -11.8115 | -46.8158 | 2026-09-18 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 7501f34a-68ab-3cc6-8bac-1729989c7417 | -12.5149 | -47.0991 | 2026-09-18 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2efd0a53-0976-3333-ac03-aa6d00141ee7 | -12.5345 | -47.0738 | 2026-09-18 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 72e34d8e-71f3-3cb2-bd9f-770d76d03dfc | -7.0164 | -44.6413 | 2026-09-18 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 16b0610e-9dfa-3f29-b635-6144693814d4 | -12.6235 | -50.8953 | 2026-09-18 11:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 84427396-2a84-3d2e-9715-34cdcf376ba9 | -7.0352 | -44.6396 | 2026-09-18 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 171.9 |
| a2c4ec31-44f8-3c1f-8f99-4222efc380bb | -9.8316 | -48.3854 | 2026-09-18 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 185.2 |
| c6b513ba-b52b-3b8c-8736-5debd2dafd76 | -13.6531 | -45.97 | 2026-09-18 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 27b0b00b-709d-390e-98f6-2356fadbddda | -13.6725 | -45.9668 | 2026-09-18 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 441.2 |
| c1d80ea6-2382-33fb-9f79-4ae538cc5104 | -12.5153 | -47.0766 | 2026-09-18 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a91e1bb6-c279-3f8a-ac96-9885a8089f60 | -13.4303 | -51.9036 | 2026-09-18 11:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 51e69fe4-f1fb-3a05-b3d4-12087d5ae4f1 | -11.064 | -48.2898 | 2026-09-18 11:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 6427ae1c-d050-3978-aa3b-96366ad9beeb | -11.2975 | -43.3851 | 2026-09-18 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| bc9ce2a4-38ed-3576-9f4c-c7bf317dda69 | -7.0161 | -44.6642 | 2026-09-18 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 308.8 |
| 5bb33873-3403-356b-a614-976b63f572e9 | -13.6531 | -45.97 | 2026-09-18 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |


[Clique aqui para ver as próximas entradas](README91.md)
