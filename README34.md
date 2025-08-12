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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e19b4a-b2eb-3405-975e-090f531efc02 | -12.5742 | -47.0006 | 2025-08-12 05:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0fc71c91-0b0a-32d5-af9b-0f4d0aee7c45 | -16.2957 | -52.923 | 2025-08-12 05:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 98338d1d-c0a5-37c1-8329-e6a2f11caf60 | -17.6549 | -46.6757 | 2025-08-12 05:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 144.3 |
| f372e278-fd69-3cb3-877e-350b90b3c04d | -13.3619 | -50.2423 | 2025-08-12 05:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 9a692b40-4b48-3b1a-8360-2b493d4c1650 | -9.723 | -49.4806 | 2025-08-12 05:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 8e9a30fc-eaac-3f2a-8b55-3cdaa46b405e | -13.3427 | -50.2448 | 2025-08-12 05:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| fcb2d07c-f40f-3cb1-9dba-3c0f15fdf182 | -17.6544 | -46.699 | 2025-08-12 05:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 67.6 |
| b670c41d-5c08-35db-ae0f-cfae8d437e9f | -17.6749 | -46.6715 | 2025-08-12 05:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 57c491f4-5939-3ff4-aa14-0ca54efea8ba | -16.2961 | -52.9016 | 2025-08-12 05:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| a375607b-c417-378b-812a-4d75a809a0c9 | -7.1482 | -60.1366 | 2025-08-12 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| c382b637-bb7d-3403-8788-c5359fc7663e | -8.9401 | -60.7288 | 2025-08-12 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d1de39a2-0126-3ccc-821a-fcdb206fe20d | -16.3153 | -52.9201 | 2025-08-12 05:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 8767f67a-b2e2-3e98-a5b5-4f52b1a56bf4 | -16.2957 | -52.923 | 2025-08-12 05:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 63f7da03-939e-3715-971d-9a94acc38f79 | -13.3619 | -50.2423 | 2025-08-12 05:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 1cce271f-2476-3539-becf-4ea64023f605 | -3.9684 | -47.8901 | 2025-08-12 05:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| f96197c6-ee54-3655-b7bf-ce8f666d5522 | -16.3153 | -52.9201 | 2025-08-12 05:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 7ff56ebe-8f78-3430-b5ad-fd3c7d3323b6 | -8.9401 | -60.7288 | 2025-08-12 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 04a4fdb9-507d-3297-9d68-50b052a242bb | -13.3427 | -50.2448 | 2025-08-12 05:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5995d29c-7c56-328d-933b-929639d61fdb | -13.3615 | -50.2639 | 2025-08-12 05:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 300d5dbc-8a3c-381a-a74c-9d3ca701b7bf | -16.2961 | -52.9016 | 2025-08-12 05:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 05aea571-3aed-318f-b36b-6f4b146a02ee | -6.5856 | -44.564 | 2025-08-12 05:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 0ac23431-c84e-3d00-98a4-e65964788ca3 | -12.555 | -47.0034 | 2025-08-12 05:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 923aee20-d054-350e-b5c6-a39c3bf7de57 | -9.7041 | -49.4825 | 2025-08-12 05:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| f7cfd788-c1ed-36e5-8318-0deb99906d2b | -17.6549 | -46.6757 | 2025-08-12 05:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 1971ebfc-e51f-312d-9d36-a881d11ed4b9 | -8.5211 | -43.3063 | 2025-08-12 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 6588753c-c301-3e1e-8c53-5b89c253987d | -13.3423 | -50.2665 | 2025-08-12 05:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 50.1 |
| c1f2718f-b9f5-30d5-ab7c-cabeae3f21a8 | -7.1298 | -60.1374 | 2025-08-12 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| ea446c03-a8cd-3ada-b527-a72d6783cd1d | -8.5222 | -43.30912 | 2025-08-12 05:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 50fd03d5-bc77-3d5d-94b5-6ae2d111d3b6 | -3.96652 | -47.86663 | 2025-08-12 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 002206ae-2ac5-3275-83b8-fa1037c6ede6 | -6.46004 | -44.57601 | 2025-08-12 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| df06b4ee-382f-35ff-a0df-2295982479fe | -3.97384 | -47.87426 | 2025-08-12 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| ae4b0501-0205-3752-9bae-4401c9473997 | -9.06806 | -45.05127 | 2025-08-12 05:44:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 68d85ce9-b5dc-3114-a874-a96b40e36fac | -6.71921 | -43.57416 | 2025-08-12 05:44:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f9716292-edb9-31be-923a-8e243eedaa18 | -8.52076 | -43.319 | 2025-08-12 05:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b7def3c3-758c-3aac-8c31-58e8bb64cec3 | -4.59767 | -43.3112 | 2025-08-12 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e3ddd66-2883-3ed4-ab3e-95c2de1a2462 | -6.5718 | -44.56309 | 2025-08-12 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 45d0cd3a-ba8a-363f-8563-6138de9f8123 | -3.96364 | -47.87304 | 2025-08-12 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| ee3d2bbc-78f0-3df0-8828-be58e667a72b | -3.96176 | -47.88496 | 2025-08-12 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| dbe99cd8-7b50-3e0d-ac26-6e8b57dc3669 | -6.61056 | -43.87654 | 2025-08-12 05:44:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5447ca67-dd89-3989-90d5-09c8523f4a9c | -9.06673 | -45.06018 | 2025-08-12 05:44:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc9a223e-24ed-3d5f-8872-837e6076f095 | -3.83026 | -47.74341 | 2025-08-12 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 0749f41f-7e96-3353-84fd-75f10a4b6b9d | -6.58192 | -44.55557 | 2025-08-12 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 736d9bc3-a81a-3221-90fa-288a080e99c5 | -7.41914 | -43.96041 | 2025-08-12 05:44:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c139abea-ee31-3e73-8c77-e3c8bc536879 | -8.51294 | -43.30779 | 2025-08-12 05:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| b9efcbe4-0322-339c-99d7-371345b5094d | -6.6079 | -43.89468 | 2025-08-12 05:44:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 256c09dc-37b0-355c-a402-c36e991d5fc8 | -6.59071 | -44.55686 | 2025-08-12 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| cabaa62b-fe3a-3426-9de3-c91fc067b1aa | -6.57312 | -44.55428 | 2025-08-12 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8e360f12-9e0e-3b5c-880d-4ed539071742 | -5.481 | -44.38225 | 2025-08-12 05:44:00 | AQUA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4008dc98-bf4e-3931-9715-c167043fd2cb | -6.57048 | -44.5719 | 2025-08-12 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 68c82cc6-338c-3610-8820-389f11530a53 | -6.60923 | -43.88562 | 2025-08-12 05:44:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 61ccb5d8-a7cc-3647-a346-3dac5fc39f21 | -4.30831 | -48.0974 | 2025-08-12 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9981eea5-1648-3c08-b425-44c21ee1cd3d | -6.22093 | -43.32243 | 2025-08-12 05:44:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 730e3ba5-b50e-3215-b3c8-14ed1917c448 | -6.57928 | -44.57318 | 2025-08-12 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7a92e083-5633-3a67-b6a9-a97dbffa5fff | -3.96471 | -47.87861 | 2025-08-12 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| d615fd1c-4b50-3acb-80e9-b79ed6abf1c0 | -3.97194 | -47.88628 | 2025-08-12 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d66afc34-2f7e-3187-b343-f6767bd0a47c | -6.5806 | -44.56438 | 2025-08-12 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 797b1ed5-2e72-3800-92d6-0bef234321b0 | -13.35435 | -50.23639 | 2025-08-12 05:46:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 6accb667-a353-33ed-833d-3c3aaba00bad | -15.90118 | -44.2956 | 2025-08-12 05:46:00 | AQUA_M-M | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 30b1b28c-f389-3249-8990-c4c7e2439eaf | -10.35709 | -50.8171 | 2025-08-12 05:46:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cb078069-28ee-3c36-bb92-d2007818f673 | -11.7338 | -50.0992 | 2025-08-12 05:46:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ed174e6f-3739-37c8-95f8-5a8ee6443a9b | -9.92406 | -46.18089 | 2025-08-12 05:46:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b7e6bd01-12ed-35e7-bfb0-b306e550357e | -14.63825 | -45.85661 | 2025-08-12 05:46:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fae39555-920a-31e9-9239-ca9f5f23118e | -11.8103 | -44.93335 | 2025-08-12 05:46:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 091d14df-cd5d-35d3-832a-f1a91a1e3867 | -12.56558 | -46.98639 | 2025-08-12 05:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 336dda3d-2d7b-34b0-8f7d-5fac908b33d4 | -12.56279 | -47.00459 | 2025-08-12 05:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| fe212d9c-46c7-3566-ad75-b4829c1716e6 | -12.4973 | -46.33745 | 2025-08-12 05:46:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 62e36e86-9b38-39dd-abdf-9da9d0244633 | -9.71671 | -49.46933 | 2025-08-12 05:46:00 | AQUA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d6138dfe-4868-3062-a71e-2f1fcd993a69 | -13.1112 | -46.86777 | 2025-08-12 05:46:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 24e5f2e8-3605-322f-b22d-5eed9bd94a7a | -10.35449 | -50.83261 | 2025-08-12 05:46:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 57200a75-40b1-320d-8a2d-d4f8296effa7 | -14.03559 | -47.40761 | 2025-08-12 05:46:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5c5d2f85-3b76-3891-a21e-98d4e07e860c | -12.5614 | -47.01366 | 2025-08-12 05:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 71203293-67ed-3419-97f7-b3d541df7aa2 | -13.57901 | -46.94506 | 2025-08-12 05:46:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 89446f67-a7f1-34f4-bc70-312ffa078ff0 | -15.90267 | -44.28476 | 2025-08-12 05:46:00 | AQUA_M-M | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f11a838d-c879-3252-bc41-cb20212fbd54 | -11.46488 | -50.14931 | 2025-08-12 05:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 29299c4e-a587-34e8-9614-95fbbc7d4ec5 | -9.7717 | -48.7504 | 2025-08-12 05:46:00 | AQUA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c69007b2-2199-3828-a041-ec106a6ed4f9 | -10.34573 | -50.81527 | 2025-08-12 05:46:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 72033e22-9d71-3c5e-a591-719d4e50b756 | -8.56046 | -54.71176 | 2025-08-12 05:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| e5ec53c0-db37-3754-80ff-a8e6c74e0838 | -14.11639 | -45.38334 | 2025-08-12 05:46:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e19caf12-2fe4-3f8a-bc03-a43fff09de44 | -11.75894 | -45.03171 | 2025-08-12 05:46:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 811352a5-c4be-33a9-8f9f-9c25208e503f | -12.76859 | -45.45309 | 2025-08-12 05:46:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 430f616f-90af-397d-b3ab-d9f05a188495 | -9.71462 | -49.48197 | 2025-08-12 05:46:00 | AQUA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d16fe2d3-c9f7-3dc5-9c81-dad5e1d38cc9 | -10.9661 | -49.56461 | 2025-08-12 05:46:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d810c628-3fb5-32ca-aa10-fc0027ec6335 | -8.56977 | -54.70578 | 2025-08-12 05:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 23f419ff-5fdf-3601-b895-98ee7a3577c2 | -13.34408 | -50.23452 | 2025-08-12 05:46:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 80077b09-5a90-3b22-abf7-70b75eca3dcc | -11.45958 | -50.14256 | 2025-08-12 05:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a01fcd98-1e05-37d7-8030-e71479bfdd2a | -12.77746 | -45.45442 | 2025-08-12 05:46:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 42d4c156-5d19-3550-8347-3319ae15c9a2 | -13.34197 | -50.24726 | 2025-08-12 05:46:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 91d10d7d-a3cb-36fa-b2aa-59e97fb2287b | -13.33167 | -50.24546 | 2025-08-12 05:46:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fd2686fd-365f-3a6b-bea6-08f2175e5569 | -9.71803 | -49.47671 | 2025-08-12 05:46:00 | AQUA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 82845268-692f-33b3-b365-6ae4dae34c6f | -14.6396 | -45.84738 | 2025-08-12 05:46:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 48c8e697-d3c4-38a6-9cbe-d12db0d241eb | -12.55253 | -47.01236 | 2025-08-12 05:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 827c3578-c722-30f2-86cf-98c0cfb69bac | -12.55533 | -46.99414 | 2025-08-12 05:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b1495f65-df4e-3210-8ca9-1160cb4ed2d9 | -12.56418 | -46.99549 | 2025-08-12 05:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| fca37ad2-f353-39ab-8f8d-1a13c11b9863 | -12.55672 | -46.98504 | 2025-08-12 05:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5389a735-ea05-3b21-b686-fefa2d5a6c55 | -9.91524 | -46.17959 | 2025-08-12 05:46:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| a3bb2f5d-ef20-33f6-836f-5ddd7d404901 | -12.55393 | -47.00328 | 2025-08-12 05:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9c3a4b5a-de0a-3748-93c2-52eefd615088 | -13.12002 | -46.8691 | 2025-08-12 05:46:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c6bbe1c-e874-3ef0-9893-1206812c2a5d | -13.35226 | -50.2491 | 2025-08-12 05:46:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 69e1d13c-eaa4-33b1-83ff-af43dade96f4 | -9.70764 | -49.47511 | 2025-08-12 05:46:00 | AQUA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 12f3464c-bed4-3c2e-92af-669b70f05599 | -14.45018 | -47.8369 | 2025-08-12 05:46:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README35.md)
