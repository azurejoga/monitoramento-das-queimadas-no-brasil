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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 038b2d4e-2e45-3b8e-a349-662c813188ec | -22.78691 | -43.75678 | 2025-02-19 03:32:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a676443c-a6b6-325e-96b6-4e68a9844dad | -20.20808 | -40.73386 | 2025-02-19 03:32:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 22b21962-0567-35c2-85c7-614d1cb68d84 | -20.29706 | -46.52138 | 2025-02-19 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| de0a7111-9018-385f-9f7f-0f184efdcf93 | -22.04175 | -42.57045 | 2025-02-19 03:32:00 | NOAA-20 | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 27657556-fa79-3b04-8c12-3d1f030ed29d | -19.68442 | -40.931 | 2025-02-19 03:32:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3f24a8af-5985-324f-81ca-0e64e2fa14b4 | -19.67951 | -40.93433 | 2025-02-19 03:32:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 66a85c42-6d55-3e84-a879-e903e7d6a38a | -20.5528 | -40.93108 | 2025-02-19 03:32:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| beb3930c-a020-322d-a860-0848cbb7b4ff | -20.79352 | -42.30194 | 2025-02-19 03:32:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 797ce877-32e6-39de-b965-05d568beb6c0 | -22.95161 | -42.68865 | 2025-02-19 03:32:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e11b7193-0ba4-3f28-92d3-a7eb4be724b9 | -19.21152 | -39.71088 | 2025-02-19 03:32:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ce398525-47cc-32fc-ae38-6200855ef142 | -22.67648 | -42.85777 | 2025-02-19 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4429f15e-88aa-330c-9475-dac4d1ad3eb1 | -20.20877 | -40.73021 | 2025-02-19 03:32:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eccbab4b-bfbe-35e3-a792-52be4b387132 | -20.22414 | -46.4946 | 2025-02-19 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e237ca41-23bc-36a4-aeab-9b21fdc4cc17 | -22.75868 | -42.40097 | 2025-02-19 03:32:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 890b950a-0f28-3292-ad1e-3d8cd0d440de | -19.71812 | -40.35139 | 2025-02-19 03:32:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a13fd882-a156-3365-b9ab-0a5fc7a19215 | -20.55753 | -40.92838 | 2025-02-19 03:32:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 1ecafcd5-88dc-3f51-aa0d-a117c8ee065b | -20.2195 | -46.48829 | 2025-02-19 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94de7fce-4417-356e-963c-cbbf5c878abd | -20.5535 | -40.92736 | 2025-02-19 03:32:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 4dc4d86c-a701-32b7-8729-40167e806765 | -18.6947 | -40.01215 | 2025-02-19 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b0486b49-6255-32ab-b2a6-3f169d57bd32 | -19.16626 | -40.13282 | 2025-02-19 03:32:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7e8414fd-a49a-3a9f-a5d5-c7bfa24f19ee | -20.29705 | -46.52046 | 2025-02-19 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d9fc6376-a953-3dcc-a4ce-213ee846fabf | -20.29803 | -46.51701 | 2025-02-19 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cafa068-b79f-36d7-a89e-0084f36f95b3 | -20.34851 | -40.36073 | 2025-02-19 03:32:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ef31e6fd-2f06-3912-8a1c-068e3ccf8827 | -22.80472 | -42.37075 | 2025-02-19 03:32:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ea8a0ec8-3d42-3f47-b557-3ef2530628be | -18.3342 | -54.4301 | 2025-02-19 03:50:00 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c8707bb7-f0c1-312a-8089-87c9b2f1637b | -6.5631 | -51.1126 | 2025-02-19 04:20:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0e469b76-96f5-3621-aa94-a133beaa50be | -5.98628 | -35.3755 | 2025-02-19 04:21:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6dda2c91-9a44-3dc2-8c55-46517fdd860a | -5.64704 | -45.90965 | 2025-02-19 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c11fe98f-8085-3949-8e6c-600a7cdd1517 | -5.38615 | -45.21111 | 2025-02-19 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32741578-4648-392a-95cc-1849fbd0dd92 | -9.27122 | -47.90989 | 2025-02-19 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 247f17d4-f8d5-3952-8588-15c9d433faf4 | -8.14681 | -44.39681 | 2025-02-19 04:21:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3a3aa64-0aa9-3faf-8623-a2a2ccb85490 | -5.67554 | -45.23209 | 2025-02-19 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85ea7942-82f4-332e-bead-bd1df8164602 | -3.26967 | -42.37734 | 2025-02-19 04:21:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e8b49694-e345-3ff9-8886-ae72964a66b9 | -3.93789 | -41.48698 | 2025-02-19 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e29b06f0-56b1-3b09-9334-61dccc0db647 | -10.82489 | -37.16524 | 2025-02-19 04:21:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 032f4b21-b195-31ab-ae57-ec1a2a5843e5 | -5.8797 | -48.10611 | 2025-02-19 04:21:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1aa18dbb-f1fb-3719-851c-524a5f6eaae6 | -7.3088 | -46.20264 | 2025-02-19 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c93e70a-152d-3768-8e87-31311eadf614 | -6.73241 | -38.9633 | 2025-02-19 04:21:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5a0a8d2a-89e7-3855-aa4b-150c395d677a | -5.38669 | -45.20763 | 2025-02-19 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7b7e89b-5f17-345a-b0e1-11fd5f1a496d | -3.27304 | -42.37785 | 2025-02-19 04:21:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b249b5b8-3cb5-30a3-a21d-7dcbd5235581 | -9.27187 | -47.90597 | 2025-02-19 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce838217-05eb-3ea0-99c8-82a1803df177 | -8.1251 | -43.14179 | 2025-02-19 04:21:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c070ae6f-3678-3362-bf51-2e5a9de7a8b4 | -6.73651 | -35.20899 | 2025-02-19 04:21:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 33d4131f-9b16-35c4-b9a9-f3943c9450c9 | -9.81557 | -36.99327 | 2025-02-19 04:21:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d5b535aa-75f2-3333-a6b9-20b3c9db84b5 | -5.98581 | -35.37892 | 2025-02-19 04:21:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8cd35f25-2b07-39c7-b427-488c05c77d15 | -7.73385 | -38.96962 | 2025-02-19 04:21:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3adc18e9-c2a0-302c-9668-6b67ca0f07c1 | -5.87603 | -48.10553 | 2025-02-19 04:21:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| affbc157-a58c-30fa-9381-0048e8319aa5 | -6.74203 | -35.20947 | 2025-02-19 04:21:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 445b82e8-8e06-373c-96df-ded027bf0357 | -6.2165 | -48.06772 | 2025-02-19 04:21:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39dbe83c-8e98-371c-869e-59bd82cf8e45 | -6.73603 | -35.21256 | 2025-02-19 04:21:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 41ac3a9d-3ba6-377d-a386-f96fd7e6da4e | -5.09837 | -47.44427 | 2025-02-19 04:21:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8f81a0b-c7b9-3981-b59d-6459f4d5ed9e | -6.21721 | -48.0634 | 2025-02-19 04:21:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8807563d-9b32-30e1-88d6-3fa2b8b19837 | -3.2747 | -42.37772 | 2025-02-19 04:21:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9edd547f-f9ae-352c-912f-e4902fc67cf9 | -8.12566 | -43.13805 | 2025-02-19 04:21:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a7ee273b-c8ee-339f-96e8-edf197ecb062 | -6.74155 | -35.21303 | 2025-02-19 04:21:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 945ab0c2-fa46-3908-931d-e067075202d8 | -5.64648 | -45.91323 | 2025-02-19 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 262c8ced-f9b6-3504-9379-6f9a19cce4f3 | -6.21358 | -48.06276 | 2025-02-19 04:21:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76ceb99f-a621-3fc1-b1f9-16b41f618448 | -15.70159 | -50.51678 | 2025-02-19 04:23:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24c0f69f-2aac-315b-ad0e-d3580af09461 | -10.54642 | -45.21893 | 2025-02-19 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a809932c-080c-3a90-81e2-4e0b4ec114cd | -20.30107 | -46.5197 | 2025-02-19 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c212f325-e961-3200-943a-b2500d1c644f | -11.02489 | -45.18403 | 2025-02-19 04:23:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e03e019-5c24-36ee-a9df-ef93c14f8541 | -22.67861 | -42.85424 | 2025-02-19 04:23:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 138ce336-93be-3c83-b856-89e412097236 | -12.24937 | -45.44436 | 2025-02-19 04:23:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5bd166e-1ffa-3b39-91fa-6e18858021ce | -22.78535 | -43.75682 | 2025-02-19 04:23:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 56f21c02-3c51-3fc9-af3e-95143c25da13 | -17.45898 | -44.38732 | 2025-02-19 04:23:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc29ef7b-0b85-3ad4-b6c7-19bd11cb0eca | -16.29696 | -45.09564 | 2025-02-19 04:23:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 375b62a5-220f-3c3c-b07e-177ee38edf6b | -11.02544 | -45.18052 | 2025-02-19 04:23:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3071a915-ccfa-3a2b-90b3-540ce73ed8b6 | -15.81393 | -42.11628 | 2025-02-19 04:23:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 42d93224-0386-32ac-bdc2-46898617f5a2 | -13.79694 | -41.70522 | 2025-02-19 04:23:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a7340878-195d-39fd-9498-034bd949276d | -17.47725 | -47.01926 | 2025-02-19 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad327892-383f-3f5e-91c1-9dd9e984db79 | -9.98323 | -48.08024 | 2025-02-19 04:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1381a84-7e32-31f8-988d-9708e1ecf72d | -10.56019 | -46.88142 | 2025-02-19 04:23:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8131843d-7289-381b-a750-4045ac4658ab | -10.36138 | -44.9208 | 2025-02-19 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ca34f9a-cfbc-32d5-b868-c5dbe62f8688 | -22.047 | -42.56895 | 2025-02-19 04:23:00 | NOAA-21 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de3b22d2-b9b3-392c-97e9-afbf5fc0951a | -15.24207 | -51.46075 | 2025-02-19 04:23:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7c5face-1f29-3fa3-828c-6d4b9d38f3ce | -14.68942 | -47.30816 | 2025-02-19 04:23:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8024c9e3-1d9a-3314-82f1-2ec7e40b1451 | -11.57583 | -47.64072 | 2025-02-19 04:23:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 924f0690-6d3f-310d-b61c-5d47ed45f760 | -10.54312 | -45.2184 | 2025-02-19 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da150948-be2d-3d71-bdd6-4e50131c918d | -10.56296 | -46.88556 | 2025-02-19 04:23:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac6cd181-5ad2-3781-885b-f648203aa341 | -10.54366 | -45.21491 | 2025-02-19 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ffe8321-4fa0-376d-a012-3189c123ceec | -11.11185 | -45.12585 | 2025-02-19 04:23:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c64eca3-18d7-3a5a-a5de-34cff9a416a0 | -12.08342 | -54.58406 | 2025-02-19 04:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e60f9e7-c178-3750-90e2-903585b54733 | -21.36281 | -46.15262 | 2025-02-19 04:23:00 | NOAA-21 | AREADO | MINAS GERAIS | Brasil | 3104304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a5a1a25-b6df-3eac-a457-9dca6bf464cb | -22.70099 | -43.34643 | 2025-02-19 04:23:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c9b5c738-758b-3e80-a8c5-03e744f86479 | -22.8574 | -42.98209 | 2025-02-19 04:23:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e1f4c220-f478-3650-b0f6-dee895e9eeaf | -15.10707 | -42.46849 | 2025-02-19 04:23:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c44c898c-e050-3a24-83a3-0bf919e9a971 | -13.79762 | -41.70015 | 2025-02-19 04:23:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 90ee0968-3c35-384d-9521-00061cc181f7 | -22.0475 | -42.56483 | 2025-02-19 04:23:00 | NOAA-21 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e494602-aa56-3416-b28e-ac5f7d8c6968 | -14.69273 | -47.30872 | 2025-02-19 04:23:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85bafd9c-0906-3993-a8c7-56bd8bde2667 | -16.37687 | -46.87649 | 2025-02-19 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da2efb18-7465-31b1-a4e2-631386ba85ea | -21.12153 | -44.2385 | 2025-02-19 04:23:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6e3fec43-0628-3aad-b556-858daf19f57f | -11.57643 | -47.63698 | 2025-02-19 04:23:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e3d3122-eb6c-3b7d-9329-a4b2f64d351c | -20.76609 | -46.76884 | 2025-02-19 04:23:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| afb5c120-7ee8-36a2-9366-c5bb2a5aaad9 | -13.79685 | -41.70374 | 2025-02-19 04:23:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 53bf5791-41f6-30f3-9226-0cdd578d8cf1 | -9.99246 | -48.08981 | 2025-02-19 04:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8b2fb647-16e7-3a85-a5f2-11426a887a14 | -9.98896 | -48.08926 | 2025-02-19 04:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 131ce519-372d-35d0-9528-2844705bd114 | -13.79757 | -41.69867 | 2025-02-19 04:23:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9d75b2cf-0467-31b9-91c1-46542281d41c | -10.54057 | -46.89665 | 2025-02-19 04:23:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a4061be-4473-3f83-b7ef-82dcba5133c1 | -17.52865 | -39.41376 | 2025-02-19 04:23:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ec3eac70-5a24-3b88-8aab-557122c7febd | -22.90143 | -43.75365 | 2025-02-19 04:23:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |


[Clique aqui para ver as próximas entradas](README3.md)
