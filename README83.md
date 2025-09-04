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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e5c5c97-4093-3338-a5e9-089033f813e4 | -10.45639 | -50.38427 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c73945b-3b66-3635-91bb-8dbb2dfb792a | -7.68498 | -48.73863 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d8012b3-1872-3b28-91d3-33354ec8e8ff | -10.10917 | -54.79768 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ad536a8-1e30-3209-bf5c-fe16a9a96e39 | -6.67649 | -48.40197 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 579f7c3a-2236-3fb8-9062-cad16c6d5b82 | -6.73886 | -59.08607 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95985076-37b6-361c-8f07-242953b4536e | -3.90019 | -54.68798 | 2025-09-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88c4a68d-cc23-3752-901a-474d0e6dd73d | -9.60618 | -47.04718 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 47611e4f-116d-312f-a5cb-6f3869f2c444 | -7.68606 | -48.73071 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02ad72af-3de6-31e6-91cd-ec97b288709a | -6.66447 | -60.02703 | 2025-09-04 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea047162-6f6d-3f9a-813a-021c19f9106b | -7.77392 | -50.96174 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fac91ea-28a2-3c15-bae7-ea48b9a6d831 | -8.365 | -48.33672 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b03ccbe9-3cd4-3f93-8942-3a1144ed28ed | -3.87121 | -52.16271 | 2025-09-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c6e8fcc-f333-31dd-8dfe-3bca981833e7 | -9.32565 | -55.21909 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 967544c5-379b-3c41-b475-f2cc99005f86 | -5.65618 | -51.27179 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3e70042-cf81-3624-8489-9ba4b4c51df7 | -6.83746 | -59.36413 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 669b87f9-da65-3d39-a6d5-e33df6691b0e | -6.16874 | -55.71359 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5408fad7-611f-3605-9bc6-ef0fdce0de76 | -8.53038 | -51.32635 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b3d80f4a-5d57-3a06-a127-051ce3b5e0d6 | -6.76521 | -59.66947 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1806caa-295d-35d4-9b8e-76158c0c6c91 | -5.00061 | -56.25699 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| e0dae0b9-e33f-3c66-80df-985ad078cb68 | -6.78077 | -63.13061 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0bf28d13-56c0-39e5-883e-9295384a8db7 | -7.26916 | -57.5607 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ba16207-8d0d-3c4f-bab2-2916d40d773d | -7.70514 | -50.29069 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8bd82c3c-41f1-3949-bb62-f417d52c2b53 | -9.33023 | -55.21479 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04082a71-14e3-36b0-b9b9-38c15a59debf | -5.88711 | -51.94849 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 33f2fd2a-59f0-3c36-9036-f33fba91468e | -6.62554 | -58.55325 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ada9dfc0-97bd-31f5-9fc6-2382bf17615f | -7.33517 | -59.65356 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 685291d7-1303-34c1-ab3c-f5348b720874 | -6.32792 | -45.68153 | 2025-09-04 05:16:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f0b6219-0745-3f49-ac43-79ea36ed48a2 | -6.87824 | -59.98546 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86b97a63-ae23-3afe-8df1-b8463f4f6f58 | -9.60093 | -47.03428 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf2720e8-e493-37a5-b681-c88c6799f5e1 | -9.53049 | -58.33926 | 2025-09-04 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b849a031-142b-38e3-a69d-522c94bab1d9 | -9.49473 | -57.81914 | 2025-09-04 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d78ea8e7-66f9-38e1-b71c-7319c5d334f1 | -7.68466 | -48.7328 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce4702b0-1abb-3693-9711-0bf6a1abdbe3 | -10.1127 | -54.80186 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1141ec0b-c584-3687-8e1c-92d1f92b40ce | -5.61132 | -57.34541 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7f9e239-40b7-384c-af71-11a35ad00943 | -4.99618 | -56.25287 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 0819caa8-8416-3a62-82bf-c436e12f0249 | -6.93929 | -59.64394 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b7b7501c-cbc9-3768-ac8c-c5ed59d53559 | -9.60414 | -47.03426 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2fae118-702c-3e31-a1f7-b219e06cd8f4 | -8.36383 | -48.34556 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e017ec13-022f-3269-93f9-b7fc7f467e66 | -3.43347 | -59.57804 | 2025-09-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab742820-88ed-3079-b07f-77c8739e4ae8 | -7.74481 | -48.77396 | 2025-09-04 05:16:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12c42362-418a-302d-906c-7426d4a4d842 | -9.97886 | -51.62719 | 2025-09-04 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 007a1063-9e70-3100-9da7-ee24455d1dc8 | -10.48743 | -53.64653 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8f7d1ac-fc4d-3c03-97fa-cddcd811a586 | -6.6825 | -48.41609 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e9536658-9571-3a44-993e-20943ed54cc2 | -6.6755 | -48.40942 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a84ae58-de59-3fcc-a67b-37ee23038828 | -9.61426 | -47.03617 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94019057-c092-32a1-87ba-90b5e4eafe5f | -10.96966 | -49.75778 | 2025-09-04 05:16:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf08c1a6-bf94-3e5c-84fa-42dae7035be2 | -6.16926 | -55.71682 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77224484-27b9-329a-9c4e-6636444bc7dc | -10.9637 | -49.74807 | 2025-09-04 05:16:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9710fd24-b418-34f6-80f1-f7444fcc056f | -6.94336 | -62.9906 | 2025-09-04 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 207dbed3-41e8-3472-9df8-5629580aafba | -6.1681 | -55.71774 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d45c5ff-af94-3fca-8191-4a0375ff5149 | -3.43403 | -59.57449 | 2025-09-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 106afe22-adc7-366b-91ef-8700f692e953 | -6.84223 | -46.40171 | 2025-09-04 05:16:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efcbf09e-4823-3d8a-82cf-9bbf09b22af3 | -7.2703 | -57.55339 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30c57593-816c-3da9-a3f1-2e2baf252ba2 | -5.61191 | -57.36395 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57e368f8-f4df-330c-b540-db63607ffe3f | -6.67458 | -58.76001 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8686ec0d-2431-37d7-a9d6-03263c5ed9ee | -10.45121 | -54.78475 | 2025-09-04 05:16:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81b84619-eafb-36c4-bf37-db3410cadf3e | -7.68679 | -50.27401 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed12c65b-9223-3959-bf51-3372c5b397fd | -6.88118 | -59.0873 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 873f4229-bf00-3957-a486-a7b3a7f834f9 | -6.77544 | -63.13923 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 215f4959-aca5-3734-8004-f9f361aecaff | -9.06772 | -46.99593 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 945b7d1d-2ccb-38c7-a6cb-c91baf6c4c6e | -5.61076 | -57.34902 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc2c8be8-32f2-369f-8bdf-9452dedaa473 | -10.27233 | -54.26746 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63a6605a-efc3-3bc4-8c4f-fb40266efd96 | -10.97414 | -49.75755 | 2025-09-04 05:16:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5c2fcbb-2c5e-3a96-9d01-21131bae7bef | -5.6854 | -45.59819 | 2025-09-04 05:16:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a5ff541-af57-3d9e-8677-d87b66005755 | -10.97619 | -46.84726 | 2025-09-04 05:16:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9be8640c-a2e8-35fb-8731-2e5a58dc28bc | -6.74511 | -58.72138 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3d659820-3719-3407-9a78-6b6656acf80b | -9.06587 | -46.99196 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c10ce1c-a25f-37ca-ba7a-21933afda4e7 | -7.69049 | -48.73384 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c92c1fe0-3dfd-3f18-9e4f-30637aa88ec6 | -5.61136 | -57.36755 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20d630bd-76a1-39e3-9b66-86f136f266da | -6.02512 | -46.66688 | 2025-09-04 05:16:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a80eb1c2-74e6-371b-a81e-f591521a70b8 | -10.4633 | -53.62407 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db543093-a22c-3aa2-be68-57f00499baf7 | -7.02211 | -59.65652 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47b64814-3fb3-3188-8b5f-369f7fe4f255 | -6.67115 | -60.02811 | 2025-09-04 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76718403-85b4-3749-af29-397b013c91ab | -7.69081 | -48.7396 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c7eea31-9148-3453-b803-4752aaca4840 | -10.47603 | -53.63188 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac1aa056-a4bd-3e82-b051-7624b7794a78 | -5.61474 | -57.36804 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f4f5af61-a4c4-36e4-993c-f5ffa94735e1 | -6.2286 | -55.93371 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94548e9d-5379-36c0-a8dc-ce797c26c8cc | -5.30985 | -55.86203 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49685b5f-c797-3a30-a320-cb052c5d4ac0 | -10.05264 | -46.06954 | 2025-09-04 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78548800-89c2-3c45-8ffd-31194b84981e | -9.32882 | -55.22454 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7f63876-288a-3e31-8cf3-78e0408b6003 | -7.9668 | -55.29319 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1338ff9d-009d-3c89-934a-a264171245f3 | -9.05228 | -54.95063 | 2025-09-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34f1c544-c93a-3c0e-b3e5-55dae2c377de | -6.78 | -63.13523 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9bdf67c-af76-385e-903c-6995830c8f05 | -9.97812 | -51.63259 | 2025-09-04 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2de20249-a817-3bb7-8e6a-d8ef82b17254 | -10.45079 | -53.61784 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54d56874-0e3c-3f33-bd3b-ef7acf096eb5 | -10.96393 | -49.75704 | 2025-09-04 05:16:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5277cc48-4aea-3470-b0b7-7f3fd27a2dca | -10.49925 | -50.4404 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d332fbd7-8d47-3f34-abe8-1d7756b7fe6a | -5.39272 | -55.90988 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1fd8f05-dc22-3ae7-bb8b-601bd93bd02f | -6.63253 | -56.26678 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e594154a-e74b-3c00-8e02-35e257573b94 | -6.93277 | -62.89153 | 2025-09-04 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fee2a31-195e-3357-9160-8de7463f816e | -9.33872 | -55.21095 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc5e21af-9752-36cb-bd6b-390995ac2cd5 | -7.97547 | -55.31352 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5fc2059-f075-3437-8330-589ac4a77a72 | -8.37045 | -52.54613 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8193af7-2895-33f0-8c07-d7db6bb834f1 | -6.74238 | -58.73871 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 8821d045-09e4-35bb-8824-b5e511ae565a | -10.96841 | -49.75682 | 2025-09-04 05:16:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 046ded97-c384-3bb8-9c38-fdf753c17190 | -6.17159 | -47.28381 | 2025-09-04 05:16:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64110dab-7536-3bf3-a77a-c258f208d513 | -5.2684 | -50.76547 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09d74b01-4390-3dad-a3b5-07435552a826 | -6.77243 | -63.13396 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d32d871-bc08-34b7-b71d-9884e088a2c0 | -8.52653 | -51.31274 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 237a8667-bed4-390c-8ab9-0661a14539c8 | -10.44332 | -50.39192 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README84.md)
