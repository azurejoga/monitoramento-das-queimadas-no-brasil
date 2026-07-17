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
| d386d324-653c-3c94-ac6a-425634d6f83b | -19.852301 | -57.969898 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| af12e172-772a-3d46-8823-53ca525e17c4 | -13.431 | -43.849499 | 2026-07-17 00:41:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 99cf0dd9-adbd-3ca7-ad8d-d3e30e724bbd | -19.8426 | -57.972 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3fb7cd34-9e38-3916-9c97-67cbbe33da67 | -9.4533 | -63.995602 | 2026-07-17 00:41:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8f6731ba-80dd-384a-95d7-ad942b726855 | -22.2673 | -55.9865 | 2026-07-17 00:41:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 153f8278-bc72-3dea-8c59-dce88ae362ac | -19.873699 | -57.974998 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b736aebb-1633-3a33-aebe-15dae08d7a9a | -19.871901 | -57.965698 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d779e0b8-3044-3d92-b38f-a2e2799e7afa | -7.9578 | -49.6418 | 2026-07-17 00:41:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59d9eb2c-bc61-341f-8cdc-34ceb8c0cfb9 | -19.881701 | -57.963501 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5236743f-c628-320d-9f87-4929e089ce00 | -22.244499 | -52.853699 | 2026-07-17 00:41:00 | METOP-B | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 166ea688-15b0-350c-b0ba-42b1a07dd8d6 | -22.228399 | -56.098801 | 2026-07-17 00:41:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 095a5afa-4505-3527-8b0b-559ff045197b | -19.835199 | -57.934799 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9aff1881-32db-35e3-9d0d-90652750f0bc | -19.8505 | -57.960602 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 94d7b16d-ea80-3cab-8be8-683fd1211a06 | -19.827299 | -57.946201 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c47293b8-dd37-304f-82ee-9aa05ae9d8ff | -19.825399 | -57.936901 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| df8bf4ff-aa98-3007-ba42-205d12e269ca | -10.0332 | -51.6493 | 2026-07-17 00:41:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eee8f7ec-1007-3b95-8438-aa260976799f | -21.6698 | -56.321602 | 2026-07-17 00:41:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e2ca9544-12e1-3f31-95da-e3884bbd6ab5 | -22.9193 | -49.200901 | 2026-07-17 00:41:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6e3a1e07-4b13-3939-8d8b-503a59d3f1e7 | -19.8603 | -57.9585 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d320f6ba-b106-357e-a0ea-baedb73ba7f3 | -19.854099 | -57.979198 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 636fc82b-0278-3f7e-a29b-9f7f2a7a5585 | -19.8309 | -57.964802 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ce3e9b28-cfc5-3e44-ac7d-3bdf8da83aa2 | -19.815599 | -57.939098 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b94920d7-2d59-34b7-a29c-b8c0e31cf5d5 | -20.6504 | -50.111301 | 2026-07-17 00:41:00 | METOP-B | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fec4256e-ef00-39d7-97ad-07e7d2e99266 | -19.8389 | -57.9534 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 436bae58-7bd9-365e-9e26-73d5c86bb25e | -21.7659 | -56.291 | 2026-07-17 00:41:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| afe99d0c-ef41-3af9-a80b-d5c6197a0e8d | -20.645901 | -50.092899 | 2026-07-17 00:41:00 | METOP-B | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ef38d898-542a-32f6-a34c-dbc27db004bb | -22.238199 | -56.0966 | 2026-07-17 00:41:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 82fe29cf-d355-3f24-bab3-4958da9627b9 | -2.3244 | -60.0546 | 2026-07-17 00:41:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3c7d325-76c5-3f5c-928a-5a5f447ceac4 | -10.825 | -46.550701 | 2026-07-17 00:41:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e65bf7a-e4ed-3f8d-b3b6-7197a2d4f249 | -8.5033 | -48.062401 | 2026-07-17 00:41:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0b15a0e-af7e-316a-bc7f-6be260fe7d80 | -8.5079 | -48.080799 | 2026-07-17 00:41:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6eb2508e-84ec-3ba4-8a87-77a5066a97b1 | -21.7773 | -56.2971 | 2026-07-17 00:41:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| beb16c0a-9613-3fa1-a803-3fc5248be052 | -12.4505 | -49.5741 | 2026-07-17 00:41:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3dd4c924-7489-39c0-8d4c-0eb7a6688b6d | -19.8193 | -57.9576 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c6797061-b33a-3ddd-8207-0c3a435b78b7 | -12.6574 | -48.2178 | 2026-07-17 00:41:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac88296c-620b-3abf-a9f0-bba93d075817 | -10.8092 | -45.1338 | 2026-07-17 00:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 8d1306ea-e0d8-3ce3-8069-217f843ac33d | -10.8283 | -45.1312 | 2026-07-17 00:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| cddcb16a-17af-3c39-b3b8-551b62f64081 | -19.8637 | -57.989 | 2026-07-17 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.8 |
| f97061ce-d8bd-3eee-84e2-453ec7f3d6dc | -9.4582 | -64.033 | 2026-07-17 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 22cbefe4-efd1-3285-b496-95c750c22bb1 | -10.8287 | -45.1082 | 2026-07-17 00:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 25f34032-59e0-3fc9-b3d8-4dad6afb296b | -22.9154 | -49.1927 | 2026-07-17 00:50:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 70160615-0750-3d75-8eb7-3039bea3431d | -10.8092 | -45.1338 | 2026-07-17 01:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 638d93a1-b49e-30bf-bbaa-70a9f2bfea94 | -10.8283 | -45.1312 | 2026-07-17 01:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 9e355bdf-29ea-31f1-a3d5-2eb6f6830c83 | -10.8287 | -45.1082 | 2026-07-17 01:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 685b2443-e5e5-366a-ae1b-98980f3eaf47 | -13.4448 | -43.8604 | 2026-07-17 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c650970f-f86c-36c7-8375-b0bd5e7ba5a0 | -20.6411 | -41.4033 | 2026-07-17 01:00:00 | GOES-19 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| 03b56c60-05be-3767-bc3b-2898ebcf108a | -22.916201 | -49.205799 | 2026-07-17 01:06:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 86fb57bf-14b7-3e4b-b0da-e5afb83307a7 | -19.8281 | -57.9501 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f66df71-d1c5-30bb-8e3f-0d72f597f302 | -9.5141 | -47.122799 | 2026-07-17 01:06:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 491dbdee-d177-3b0c-94cb-f129e2daddb8 | -12.4584 | -49.582199 | 2026-07-17 01:06:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa23e487-20b3-300d-b4e6-f2bd28b576cc | -20.6516 | -50.099201 | 2026-07-17 01:06:00 | METOP-C | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27b398c6-b9a0-325c-88a3-d420b57aad77 | -7.9705 | -49.648998 | 2026-07-17 01:06:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfc1ff77-bbc0-3547-80f7-8c45619a54de | -12.4487 | -49.584599 | 2026-07-17 01:06:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb4546cf-c7bb-3995-a16d-491504b54351 | -28.545 | -50.332901 | 2026-07-17 01:06:00 | METOP-C | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 13effd6c-9c68-382b-81ab-c9597533b31d | -9.4495 | -64.036003 | 2026-07-17 01:06:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1c62ae1-3d7e-36fb-a9af-5574487e0500 | -10.8296 | -45.130299 | 2026-07-17 01:06:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| beed84a5-52cd-35e7-b6d8-bd25b3f471f8 | -22.2547 | -52.867298 | 2026-07-17 01:06:00 | METOP-C | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63b365a9-5091-3165-bc5f-ce587b77019a | -21.6649 | -56.3363 | 2026-07-17 01:06:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6633bc68-cf22-311c-92d8-4e609385bc9e | -12.6893 | -48.208302 | 2026-07-17 01:06:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7efa8289-c1f0-3804-9190-9d5f2de08b67 | -19.8347 | -57.985401 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 775cf147-d168-3389-bf55-f41170fdaf37 | -22.914301 | -49.197701 | 2026-07-17 01:06:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d85084bf-399b-3bd9-b525-a8703eb81c98 | -8.5135 | -48.073399 | 2026-07-17 01:06:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b5332b7-8bdc-3a69-b4e4-8b3b22b0bdf9 | -20.655199 | -50.114799 | 2026-07-17 01:06:00 | METOP-C | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c5a739b6-93ad-3ea9-9e20-ecabe2566323 | -12.4608 | -49.5919 | 2026-07-17 01:06:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 358281c7-1ecd-31c8-95fd-f5af48b303b3 | -7.9678 | -49.637901 | 2026-07-17 01:06:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4318c358-31d8-3ceb-b70a-29a2c2fdf8fe | -12.663 | -48.227501 | 2026-07-17 01:06:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 422b1823-4933-312b-b2b7-add50e9074ea | -21.3531 | -51.044998 | 2026-07-17 01:06:00 | METOP-C | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4c32d54-e9c1-35d7-a71b-7fb4c8ba9e70 | -19.864 | -57.979401 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bd7ef96a-e97c-366d-b748-91d045e644a7 | -9.4454 | -64.015404 | 2026-07-17 01:06:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 79af9da7-f710-3a92-baf3-b9282aa81c6f | -9.4551 | -64.013496 | 2026-07-17 01:06:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e73aef73-0f22-31b7-893d-02a3bb795d5b | -19.851999 | -57.969601 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2279e732-b969-30af-b7cc-1d6e38484852 | -19.825899 | -57.9384 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 60873243-ee26-3699-aa37-4db9381e9b31 | -10.8252 | -45.152901 | 2026-07-17 01:06:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c51f0ede-2d3d-3766-987b-c8ae9c3a2586 | -22.9259 | -49.203201 | 2026-07-17 01:06:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c494284a-0a46-3505-9273-38202c0dee46 | -12.6601 | -48.215801 | 2026-07-17 01:06:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fc35b1c-795f-307c-bc65-24911578f224 | -19.180201 | -47.352402 | 2026-07-17 01:06:00 | METOP-C | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 368e1739-a822-3f6d-9c61-2684385a915b | -13.4485 | -43.8713 | 2026-07-17 01:06:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5e795e-3510-3713-8894-17ae1fdd3e82 | -9.9129 | -53.365299 | 2026-07-17 01:06:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00cfac16-f401-3fd0-a222-f083b3aae72e | -19.830299 | -57.961899 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7c7a6c96-d06a-3b75-91fd-54a843d2ee08 | -21.7607 | -56.305199 | 2026-07-17 01:06:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e346cd12-cafd-396c-97e2-a286ecd903fa | -19.1775 | -47.341702 | 2026-07-17 01:06:00 | METOP-C | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 31f0d68f-1210-31e5-b836-2db57680a5ad | -9.5678 | -48.665901 | 2026-07-17 01:06:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 741fc03b-7e1e-38d4-8883-c8a34cf39f3c | -13.433 | -43.851898 | 2026-07-17 01:06:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6059fa17-e9c6-3f23-96cd-7c9c6486a890 | -12.4463 | -49.574799 | 2026-07-17 01:06:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ff1c929-b840-30f9-8d1e-def5090bd796 | -19.8356 | -57.936401 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 22496163-8aa4-3560-9835-4fc41005e9c8 | -21.660999 | -56.316101 | 2026-07-17 01:06:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a0828601-027b-3964-bb38-ce1a76d0f5ae | -19.820499 | -57.963902 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b4593307-fdfa-3514-90de-0a728ac791de | -10.8199 | -45.1329 | 2026-07-17 01:06:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 378bcece-54a4-3144-8576-3818b07e313c | -21.768499 | -56.293098 | 2026-07-17 01:06:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dc667abe-58e8-339e-b470-e133efdaee36 | -19.8183 | -57.952099 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5c61ddf9-956f-36f6-9f8e-2dfac8ac3f1c | -22.230101 | -56.099899 | 2026-07-17 01:06:00 | METOP-C | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9193b7ea-b35c-3906-8ab0-cf85a0700310 | -12.4561 | -49.572399 | 2026-07-17 01:06:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb632b94-f04e-38a5-a362-da51afb2fd51 | -19.822701 | -57.975601 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 063f3093-3636-3125-a59a-c30c2764becf | -22.2465 | -52.8773 | 2026-07-17 01:06:00 | METOP-C | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0549e88c-4e5d-32e1-a9bd-cab507c4789d | -21.770399 | -56.303101 | 2026-07-17 01:06:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5d0a31ac-91a7-3bed-b714-166cf97c655b | -8.5169 | -48.087299 | 2026-07-17 01:06:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bff5936d-6aaf-3673-a2e8-cffcd2828bf4 | -20.6467 | -41.391201 | 2026-07-17 01:06:00 | METOP-C | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6392b5e8-11c5-3bce-9343-7bbe5e7ab75e | -21.758801 | -56.2952 | 2026-07-17 01:06:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f3ad2964-a7b1-346c-8479-3e385cf3687d | -13.4426 | -43.849201 | 2026-07-17 01:06:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8070badf-cc1b-3b3d-badd-fa93d3185002 | -22.924 | -49.195099 | 2026-07-17 01:06:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
