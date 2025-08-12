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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cf1ed82-5276-3e3a-b28e-4a719da0c37c | -16.29708 | -52.91836 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f6c4a81c-7a85-36a1-bc97-ab2a6511197a | -16.29832 | -52.90956 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c421868-46df-3dcb-b1c6-fa3faa244100 | -22.19595 | -54.76837 | 2025-08-12 05:01:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 545a6e81-7a74-3ba3-be34-71aadfa0a0bd | -18.60998 | -43.90466 | 2025-08-12 05:01:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2ceee28f-52b1-38de-b8e5-0bb019a75520 | -16.28965 | -52.91738 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e1ee2c07-fded-35b0-9f0f-f402d67c96d5 | -19.30165 | -48.43033 | 2025-08-12 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 972d330a-0245-371a-b8d3-7a39d6482da7 | -16.98892 | -49.20897 | 2025-08-12 05:01:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c2ec325-94c1-3e10-b41d-479983c94316 | -16.30766 | -52.91372 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| dd838171-80b3-31db-ae17-21f436005508 | -17.65855 | -46.67343 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1ef53f53-819c-3e9b-87c3-d2d3a64433a8 | -16.30025 | -52.91259 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 65d59c42-1596-389f-b88a-f86e21064dec | -17.64811 | -46.66396 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78253213-1524-3993-9aee-24214464609c | -16.30337 | -52.91749 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3c6eb9a9-0121-3eb5-b051-ef223c1e07dd | -17.57067 | -45.32456 | 2025-08-12 05:01:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b5b51ab-2dba-32b2-8c15-c2e8a372f110 | -17.64606 | -46.68375 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8cdc5e04-937f-3d93-9cfc-70165668215c | -17.96284 | -44.30109 | 2025-08-12 05:01:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2590a5d-e6de-328d-97d9-8ef95a82f837 | -17.66211 | -46.69392 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6d25009f-907f-304b-80b2-b8669a412154 | -17.65292 | -46.67264 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6d83d6c6-e1d0-398a-8dd1-6d4c78d9fa14 | -19.72075 | -46.22562 | 2025-08-12 05:01:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1e4dba0-c2e7-3093-a712-9ef0b634f273 | -19.30132 | -48.43344 | 2025-08-12 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57e85ac1-1640-3009-8249-01189e0a5961 | -17.66376 | -46.67814 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 07981839-0bfa-3ad9-9b74-7ba89f18d466 | -16.29028 | -52.91293 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4cfe9ae9-bd5e-3460-a25b-7e913ffdc353 | -18.63677 | -46.83477 | 2025-08-12 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c4358ad-e93e-3c7f-a61f-f7a06b568b80 | -22.9883 | -49.027 | 2025-08-12 05:01:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3e6a3a8c-e8bc-3a03-96a1-99095b4b6862 | -16.29092 | -52.90838 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6e218f82-54bb-3462-a650-eef8f6dac3d0 | -18.61288 | -43.90591 | 2025-08-12 05:01:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 91eac44e-d91e-310f-bf57-95f6f1fc2a64 | -16.30707 | -52.91809 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 969e36c7-ec29-3f9d-b118-f4791014cbc1 | -17.64043 | -46.68304 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8482e25-e801-3e2e-883b-fdbbf972d9f9 | -16.29768 | -52.91408 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ade70a1f-f2f8-304e-bd22-76455d0e3e70 | -17.56357 | -45.33382 | 2025-08-12 05:01:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d47262d-0536-329b-a129-f89aa70d4ae0 | -19.07807 | -46.1898 | 2025-08-12 05:01:00 | NOAA-21 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62369000-5408-3c7c-98a7-d4746619398b | -17.56404 | -45.32894 | 2025-08-12 05:01:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38fa7330-268e-305e-9801-dc981bc99031 | -22.98625 | -49.0298 | 2025-08-12 05:01:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3e80478c-3f09-3594-84d4-5ade31bd34de | -17.65087 | -46.69244 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 107ff6b5-03c5-38b3-9331-31a224e4d9db | -16.39716 | -50.89175 | 2025-08-12 05:01:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b93fa690-d869-377e-bc4e-be3a9349b245 | -23.97768 | -49.65112 | 2025-08-12 05:04:00 | NOAA-21 | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31e23eec-8e7d-3a74-9a5d-05a502bba227 | -8.5211 | -43.3063 | 2025-08-12 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 94ada57b-efed-34a3-810b-a9ec342c169a | -3.9684 | -47.8901 | 2025-08-12 05:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 7fd520d4-e587-3a68-8896-bfc303ceb858 | -8.9401 | -60.7288 | 2025-08-12 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| ebf32695-0f48-392b-853f-817a92815d8f | -13.3427 | -50.2448 | 2025-08-12 05:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 96e9894d-8209-3cfa-89e6-c7ec9cd882e9 | -7.1483 | -60.1174 | 2025-08-12 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 6f8803fd-0882-382b-b8c6-ea3374481621 | -12.555 | -47.0034 | 2025-08-12 05:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 66bb8032-e266-3a1d-b983-a4c9edb114f9 | -16.3157 | -52.8988 | 2025-08-12 05:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2381e336-18cf-3f57-a34d-acb43d23f032 | -17.6544 | -46.699 | 2025-08-12 05:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 53.7 |
| d0b7c9f2-b190-34d1-9510-2a6425d146f7 | -16.3153 | -52.9201 | 2025-08-12 05:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| be1223ce-ced8-3e73-a17d-d3c2ea8d8cef | -17.6549 | -46.6757 | 2025-08-12 05:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 136.4 |
| c4b8b33e-eef5-379f-8cdc-f2d29b6aac93 | -7.1299 | -60.1182 | 2025-08-12 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 565305c0-01bb-32da-8d1f-f9127492a348 | -12.5742 | -47.0006 | 2025-08-12 05:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2f2e323a-d3a4-3c5a-a4e6-98d1976723d9 | -16.2957 | -52.923 | 2025-08-12 05:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9f3061f1-f4b6-398b-afa0-48485535d4e5 | -16.2961 | -52.9016 | 2025-08-12 05:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| cb4cdf4c-3bc1-341d-b9d8-2fd21ca7af1b | -3.9686 | -47.8684 | 2025-08-12 05:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| abc7f8df-9e19-3c51-be17-0517fd5bece3 | -13.3427 | -50.2448 | 2025-08-12 05:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a0686b02-d2e7-3e87-827f-7e9959b540f0 | -12.5742 | -47.0006 | 2025-08-12 05:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3cfaf32a-07ce-38b1-8084-b93884b70cc9 | -8.9401 | -60.7288 | 2025-08-12 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5bfcd9e2-d2e0-33b8-b186-06b6fcb188ec | -16.2961 | -52.9016 | 2025-08-12 05:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 41cd4e5d-a0a2-3591-a0df-dbcd09142dc0 | -16.3157 | -52.8988 | 2025-08-12 05:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 4a66b74f-6765-3c93-a440-527f5a20f310 | -17.6549 | -46.6757 | 2025-08-12 05:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 821ff2d3-ed1c-3aa5-8175-aa1a08d1bf20 | -8.5208 | -43.3298 | 2025-08-12 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.9 |
| c4a2642d-48bf-35d5-b3cc-56281c555130 | -17.6544 | -46.699 | 2025-08-12 05:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| dfa8a0e7-6129-3eda-99b6-9fe6856f0cf9 | -3.9684 | -47.8901 | 2025-08-12 05:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6f489085-071f-3e72-b413-74817e6c32ca | -17.6749 | -46.6715 | 2025-08-12 05:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a584a2fb-02ad-3ea9-9413-fc97ee8e7b96 | -16.3153 | -52.9201 | 2025-08-12 05:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 001ffd23-ea7b-3fa5-a675-a85f28118011 | -16.2957 | -52.923 | 2025-08-12 05:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 23e88585-bd5a-33c7-b233-ff15af6f5cc4 | -8.5211 | -43.3063 | 2025-08-12 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| deaca4af-5b8d-39b3-b489-005d3bd7c8e9 | -12.555 | -47.0034 | 2025-08-12 05:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| db8cecc2-13c7-3c79-ae7d-f1d87e94ea1d | -5.84801 | -59.91371 | 2025-08-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fdbfa24-b142-3ca2-842d-2b497541c45f | -4.28828 | -48.05809 | 2025-08-12 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7e54a6b-001c-32e8-807e-c1acbc0cb8e3 | -5.89053 | -57.74387 | 2025-08-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dee64b71-13c6-3295-8f2c-4ad8ce78316a | -3.83627 | -47.74542 | 2025-08-12 05:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8b4c15e5-cfdb-396f-8138-881adb7970ab | -3.83553 | -47.75062 | 2025-08-12 05:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 17526bfb-03df-379d-87b0-380849d98053 | -6.30283 | -51.4006 | 2025-08-12 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f19cc68f-8d6a-3a36-91be-1e0d59af200f | -3.97016 | -47.87476 | 2025-08-12 05:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5d1bbde3-1dc0-34ca-89ee-75b3fa4390fd | -4.31293 | -48.10361 | 2025-08-12 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa855635-8d01-34f4-a8b1-82bd7ace1c30 | -5.84469 | -59.91319 | 2025-08-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac471ac2-2704-3103-89bb-665b7c01325e | -5.88993 | -57.74787 | 2025-08-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 236ec49b-8a5a-3f34-b31a-eb604182bafa | -4.31448 | -48.10463 | 2025-08-12 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10bb8bd2-bec9-3998-b526-6a94a26447a3 | -4.30652 | -48.10274 | 2025-08-12 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 96adb2c5-f320-3c37-b3ad-21227c80c191 | -4.0391 | -54.90902 | 2025-08-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fa2b2bb-7a2c-3ed7-86a5-f93868fb739f | -6.30815 | -51.40131 | 2025-08-12 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd9ebfb9-1440-3321-8720-1d02a0a8b0b6 | -4.30808 | -48.10373 | 2025-08-12 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01e50e76-a51b-3abf-b06f-c8bed5a1ca30 | -5.84747 | -59.91718 | 2025-08-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66751c22-9621-3d85-b455-39418805cf03 | -4.59105 | -56.07446 | 2025-08-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6844723e-433a-39da-8b49-16d1ab07f521 | -4.30729 | -48.09755 | 2025-08-12 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cae4b23-6123-308c-9c94-1f1c7d8ab6d1 | -5.8864 | -57.74734 | 2025-08-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ae6d905-ef88-33bf-b64e-c820039926bf | -3.96865 | -47.88522 | 2025-08-12 05:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0431d031-8179-35d1-8cdf-9c77b12f7dc0 | -4.31369 | -48.09843 | 2025-08-12 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1da6e4f-21f1-3784-bd52-a46de8cd13ef | -3.96302 | -47.87852 | 2025-08-12 05:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a1106221-cc95-3667-a86c-952b7a97d39c | -5.887 | -57.74335 | 2025-08-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eed8b6e2-7dc4-3040-8ae2-2cc2043d5e4d | -4.29474 | -48.05874 | 2025-08-12 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 892a4fd9-122e-3959-ac75-14e1021eea93 | -6.30862 | -51.39795 | 2025-08-12 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dbbad1f-f2f1-3096-b046-bd4defd33798 | -3.97578 | -47.88148 | 2025-08-12 05:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7370116f-ac5f-3fa9-a286-e3292982dd79 | -4.30881 | -48.09853 | 2025-08-12 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbd9dc1a-95ce-377d-b24e-e93dae4c9f80 | -4.04316 | -54.9095 | 2025-08-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9178bce-223f-329f-93a8-84907ae70a73 | -3.9694 | -47.88 | 2025-08-12 05:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c817b834-8e3c-3e63-8caf-b44fbf544c2c | -9.93816 | -60.48816 | 2025-08-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c0de32f-ff87-3cbc-827a-af9081c975ef | -9.88846 | -58.56694 | 2025-08-12 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33b25616-adac-37f0-a76a-0af3fb489536 | -9.92535 | -60.48251 | 2025-08-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 455e785f-21aa-3a54-b22c-9c0441e9751f | -7.47192 | -60.40764 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e91d5948-e5ba-3a04-ba9d-ab94a0a08fc9 | -9.37125 | -61.53334 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d1f8c6f-a58b-3ac0-9a70-2ce0b1c2f158 | -10.34422 | -50.82737 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db88bd7f-5c84-307f-86cb-767245bae028 | -3.43818 | -49.04296 | 2025-08-12 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README30.md)
