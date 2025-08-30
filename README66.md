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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfbd8413-595f-36bf-a648-c1520f07e71c | -10.48015 | -57.96697 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a3532d0-3547-3bce-a588-b1412f9cddf4 | -9.46317 | -62.36257 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1702162e-1d05-35ea-b938-7f70a1d13072 | -9.58467 | -54.48598 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2efaec2-ee8e-3efe-886d-ae0f1dbbd88c | -8.90826 | -62.10442 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7fc567c9-dc90-3198-983a-511960a8ed87 | -9.12341 | -65.81686 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a3c66af-a919-35f5-b89c-c4d31207c3b1 | -9.69713 | -48.31512 | 2025-08-30 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04f2bdd7-de06-3045-809b-a1c34b6fcd51 | -8.1049 | -44.99925 | 2025-08-30 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 079a5b6d-9275-320f-af67-7a2503f378e9 | -10.66493 | -48.72627 | 2025-08-30 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa680030-30fa-351b-a1e7-3acb14d4b10c | -5.87708 | -50.29381 | 2025-08-30 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef84ce8c-a43d-302e-845b-3e685b19e800 | -8.34577 | -62.9294 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 467582b8-3aee-3604-a93f-8c3d803e48de | -9.13304 | -65.81864 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eafe92db-c796-3d80-ac24-325f217073b6 | -10.99841 | -46.9661 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f8d7e382-ce8c-3ec6-85d7-1b27b0933d46 | -7.71864 | -50.30245 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b5dd8f1e-eee6-3491-9265-2b9110fa1c30 | -10.71937 | -47.00829 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f37d06c5-0458-3c5d-a4fb-8eba8d631235 | -7.95474 | -46.39006 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88a785ef-a561-351c-86cb-80e0078eba50 | -10.07491 | -54.93213 | 2025-08-30 05:10:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4167acc-52d2-3520-86cd-2d02479af616 | -9.11378 | -65.78767 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 018e73fb-9017-32c5-80cd-057ea0844932 | -9.10822 | -65.76886 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| a142d3b3-28a4-3b88-94e4-51cad795a79c | -8.87536 | -60.74024 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3af7c62-75a0-31dc-9088-3c36a7376d6e | -7.77935 | -45.47176 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a140371-4eaf-3205-af04-4baea7a82030 | -9.44872 | -60.54362 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2358a00-73b1-32cc-aa3e-f46f0134e012 | -7.355 | -70.12606 | 2025-08-30 05:10:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b072606-1da7-336e-b8a7-9856350f18ab | -9.32132 | -56.90539 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28cea770-dd41-3271-914e-45c2a968dd64 | -8.18389 | -61.37472 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a4f890e-01f4-3a55-8d77-cbd0842bc67f | -8.77032 | -68.69892 | 2025-08-30 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b54e846-7450-328f-a0ee-e1db88aa20f7 | -10.46299 | -57.94634 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df3f3bc9-272e-3111-91bb-9ea581c54fd7 | -11.00376 | -46.86824 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e788083b-4965-3afc-bfce-59b5f8f8f6a5 | -6.12396 | -57.57299 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b3693ca-6f30-3423-9fbd-e49442131e63 | -11.88296 | -46.39772 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1ed3c6b0-cb35-3dc8-97eb-da3ade51f9e9 | -10.46023 | -57.94231 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e74d42c-c8ae-332c-b652-1b2399cb0840 | -7.39897 | -60.59305 | 2025-08-30 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f355b803-eaa3-3de7-aa82-2b079fa32619 | -11.15127 | -47.14566 | 2025-08-30 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7e524ca3-61f3-35a1-85c9-6571e07dc859 | -4.89974 | -55.84856 | 2025-08-30 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 948b4609-3046-3097-bdcb-d8aee038355a | -6.34521 | -58.1708 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6becaba1-fbcc-3a9b-a78f-f9a94df68c6c | -9.15091 | -59.5777 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d54d800-ef47-3386-a16e-5e6ec78bdf7c | -10.06872 | -58.36001 | 2025-08-30 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21424650-606b-3453-a25d-25f1534b1dd1 | -5.32308 | -55.94237 | 2025-08-30 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd75e4cf-1a1e-3a00-8195-7465a6e66be9 | -9.27706 | -60.46098 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b347e83-c923-31a2-8a5a-d550850c379e | -9.14071 | -49.62241 | 2025-08-30 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd6a4a2d-6077-30f0-b7b4-3fc7f20b3701 | -10.3248 | -59.18243 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59d3a53e-f56f-3cdd-9a84-71aa18ba38fd | -7.09464 | -63.1405 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43b5aa6c-6168-3e9f-804b-8ffe02151523 | -9.50498 | -45.39076 | 2025-08-30 05:10:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfcca4d5-c4ca-37e0-945b-b8367dad78f2 | -11.87043 | -46.39251 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 566000d0-6dde-3576-83ce-2ce0dda315df | -7.09727 | -44.31448 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 109c77c9-50e4-3c5b-981a-8e85b7db7352 | -7.62157 | -60.8523 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1063edd6-20be-3313-9a66-d7e369f7a9c2 | -11.86352 | -46.45086 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f86f83a5-ad05-3a2b-aff4-9d61cfe89ec4 | -9.41364 | -60.57436 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 008172ec-c942-30d4-ae50-32ea6a3facb7 | -9.10913 | -65.76365 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| dec66cb1-01b0-34b5-9d49-9bd7e5c4cd1b | -9.44565 | -62.34975 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e057c5d8-90ca-36b7-8fa6-2aad6e31bd27 | -11.85718 | -46.39746 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4048ef88-3f22-3973-8c53-ed5a842c941d | -9.20258 | -59.54518 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34de01db-3ac0-3929-9ae9-9d7c4243a871 | -8.55862 | -63.02795 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4bd0bc2d-73cc-3e9c-8a10-90614fdc5295 | -11.5838 | -46.36503 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dce72db6-ded2-3fad-b08d-add1ee31d250 | -11.85664 | -46.39796 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1accdc46-dcd3-34b6-a756-219bff2123f5 | -11.89049 | -46.39339 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 012f7b8d-873e-3573-98e1-7d51e645a5da | -9.30099 | -56.81403 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56c2ae5f-f2fb-3426-b1a8-e886ba337359 | -5.99838 | -57.8512 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a8b14fc-b203-35a2-9cdb-ecef490f5fd9 | -7.75382 | -45.46417 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f95c7598-6294-3e21-8138-b63d0529905d | -8.77148 | -68.70106 | 2025-08-30 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 831bb917-5559-3f51-89ad-7bd5bbdc509f | -11.8453 | -46.38249 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3703fdab-0d51-3931-97d4-7fc6ef118ea0 | -7.90046 | -44.7875 | 2025-08-30 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3017c7cf-f9d3-3cd2-a8ce-2d6e303c5695 | -10.99395 | -46.95082 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f30e0470-35fe-3d0a-a58e-621ec453438f | -7.89887 | -63.0036 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37cfba84-8613-3952-9189-e5f739ac5809 | -7.11757 | -44.59544 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab0818b8-fb37-3fc0-adea-12231abf14ce | -7.40224 | -44.2878 | 2025-08-30 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b213efd-61cb-3d42-9d6a-d21840575ac9 | -10.99898 | -46.96135 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 39ec8f98-24ca-33ed-b408-a62a2f3470eb | -7.43483 | -44.80679 | 2025-08-30 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b1aa6c4-e272-3c8d-9a19-e3e4ab9ba2bb | -9.58294 | -54.47195 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e7f40a2-b15d-3e16-8aa5-bc9c656abcf7 | -9.44424 | -62.33477 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f233f5a3-b5fd-364d-88d3-2cfb2e8490f2 | -9.27243 | -65.92429 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc7118da-1034-36f5-989a-b038bd4c7c10 | -8.67491 | -62.43454 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e7b5d44-885e-343b-a5de-130c51fa8af5 | -9.44041 | -62.33416 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6562c571-7416-359c-8236-edde586bc35b | -8.18021 | -61.37411 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a4d99c6-66ff-3a71-b689-c9f933f8da1c | -11.87651 | -46.45191 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e7da9d6-f618-3563-8f17-1e0c4655d1d4 | -9.44823 | -60.56004 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 74f2edb4-38f5-3724-994a-4feba22bcdb8 | -9.45727 | -62.32732 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 6ac46aa4-15c6-3d81-be24-1d68ffa01477 | -10.99363 | -46.8468 | 2025-08-30 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62017abc-2e88-379e-864c-df2728790917 | -7.71684 | -50.28095 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 46db2183-af84-3b94-81f5-f5b41a2afe9c | -7.80457 | -63.55663 | 2025-08-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75c95370-a61e-38eb-835b-33eb515c5691 | -10.02642 | -46.0346 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8af3166a-d95e-3725-9d70-d802803727b3 | -9.04377 | -60.4912 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28fe429b-8eed-3072-a293-cb0c53f1c35a | -9.10705 | -65.77006 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 959536b6-ec4f-398c-957f-81e4520cce6d | -10.64594 | -48.65707 | 2025-08-30 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a069d76-c490-37ed-ae9f-00fe46de6e67 | -7.96107 | -46.38242 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 670cc51d-5c41-3cba-8a37-04639dba444b | -7.39246 | -45.93378 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 906e1be6-2490-3c3f-85b1-e3214fe1f6f3 | -8.51323 | -54.71508 | 2025-08-30 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7831529-50ed-3f21-aa82-d55bfb350ede | -10.0208 | -46.03076 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26e7bf35-fd13-3386-b5f8-0bddae0c4b4a | -10.3425 | -59.19993 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7607eb85-9122-302e-ae95-20e6bfd9c69f | -9.12238 | -65.7676 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c04bf46b-060e-37eb-8102-4d320de5b33f | -6.88035 | -56.47322 | 2025-08-30 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 324a488b-d7ea-3cac-baac-795f7eb2a9a7 | -10.06651 | -58.3525 | 2025-08-30 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e9962b9-c157-3777-a9f6-e09372490e85 | -10.36907 | -57.80915 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf5073e7-dd2e-30aa-9fdc-ee67b9fb412d | -10.33917 | -59.19938 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2c044a7-ff9c-3e00-be84-dc9c46799d99 | -9.45698 | -60.53701 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e54e9f2d-e95f-3b94-9a67-2c32f383ec22 | -9.45188 | -62.33606 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 29.1 |
| f9683873-4ff3-3eff-8251-648a5e863b8c | -11.83579 | -46.46386 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9e78d101-de8b-3924-9675-6e1aa906f954 | -9.44347 | -60.5673 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| de38d975-69da-3c59-9bb4-c05f60c0c887 | -11.83116 | -46.44748 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6cf77dba-8ef3-321e-8f1d-c43c7024956d | -9.15371 | -59.58189 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62a58612-326a-36ec-af80-ee29bf854dd3 | -7.12234 | -44.60229 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README67.md)
