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
| d338dc18-3eb4-3698-a698-748c2b4e7a95 | -15.7642 | -59.4872 | 2025-09-25 00:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 37eaae41-259b-3d59-a8c2-4f4254f773b2 | -21.0131 | -50.0217 | 2025-09-25 00:30:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.0 |
| b4f0c995-8310-3e99-b947-e7b7ea63f995 | -17.9312 | -55.8548 | 2025-09-25 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 27d196b5-7616-3c9e-849c-77b40b64de78 | -17.951 | -55.8522 | 2025-09-25 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| a55c64fe-1597-321e-97e4-ac85da2cae20 | -2.9291 | -48.2966 | 2025-09-25 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 139cbeda-5578-38c6-bcda-1cfab4e965f6 | -3.823 | -50.9765 | 2025-09-25 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3793823c-543a-31df-a8ab-b669ee08e735 | -2.9291 | -48.3181 | 2025-09-25 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f2f9bdf4-d34d-377a-a1f5-3a6440a88e26 | -6.4131 | -43.0724 | 2025-09-25 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 2428d34c-1205-305e-bf74-d24938725282 | -20.9726 | -50.0077 | 2025-09-25 00:30:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| e0b94492-319d-3b36-be90-3d26eb5d2034 | -6.4317 | -43.0942 | 2025-09-25 00:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 296.2 |
| 705dbef8-2228-3476-bdee-b1ab5fc610cc | -3.2176 | -54.9632 | 2025-09-25 00:30:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| dba198ee-cd22-311b-b991-4decbb91a8e4 | -16.02075 | -42.12547 | 2025-09-25 00:30:00 | TERRA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 3b144edb-07ff-38ac-9dc2-db82b6ae8078 | -16.02035 | -42.13123 | 2025-09-25 00:30:00 | TERRA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 7fc8e603-d412-312c-a920-99b113b2250a | -18.26016 | -51.13334 | 2025-09-25 00:30:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 19b126a9-9370-35ad-8b28-4f91c37e5ac1 | -10.59273 | -44.07944 | 2025-09-25 00:33:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e94dd86d-454a-3e1c-9b18-64bebbd3326e | -12.31299 | -44.21361 | 2025-09-25 00:33:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d9d37133-c28e-3d1a-a93f-afb8313f4067 | -12.05686 | -44.82302 | 2025-09-25 00:33:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 841b0734-6a46-390b-9c07-92decd4b2659 | -13.39928 | -47.41716 | 2025-09-25 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30f75059-d5b9-38a4-a6f1-515ff6bae16c | -6.68133 | -43.13835 | 2025-09-25 00:33:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| c7226d93-9b5b-3947-bb1b-c1a44f19168f | -9.55522 | -47.53671 | 2025-09-25 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1d7a6342-42d3-32e0-a3c2-32b0910c0d47 | -11.63883 | -44.43008 | 2025-09-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8cef9b2b-5084-3d6b-afd4-0bee28841cf4 | -11.67558 | -44.39971 | 2025-09-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ce183781-c816-332a-9c58-7c145a019a42 | -10.83806 | -44.82878 | 2025-09-25 00:33:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 63fae7cb-9c2b-3a5a-991d-0cf2b9e2c864 | -11.67585 | -44.40564 | 2025-09-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 663d3c66-17f0-3a79-be86-40ed7d4383c1 | -6.42222 | -43.08918 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 560.0 |
| bbc86c5b-d564-351b-bdde-44f05cde4227 | -10.30121 | -45.22192 | 2025-09-25 00:33:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1d9bb3fc-08f5-3f3a-8afb-1e7a17a9bfa9 | -8.47809 | -45.01704 | 2025-09-25 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 3862c837-62db-305c-9c5b-75e2ea414aaf | -13.90941 | -43.34206 | 2025-09-25 00:33:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| ecf1c446-e65b-39b7-8553-04cf2d3bb278 | -11.69417 | -44.39044 | 2025-09-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7dbc2225-81ab-38bd-88f0-3e372871af0b | -12.86502 | -44.67423 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f552ac7b-bc94-3466-8a5c-deea76f0111c | -9.25017 | -46.56753 | 2025-09-25 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff31296c-f9c0-30b9-905f-0118ad733cb9 | -6.42494 | -43.10677 | 2025-09-25 00:33:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 2d700a82-630f-34f4-bcdf-2f1f4f6c30d5 | -7.31766 | -45.76361 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 1a2aa8f7-fbd4-3f22-a684-b923a45e0ba3 | -8.47632 | -45.00522 | 2025-09-25 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 27b88c20-328e-3040-a644-edec98d8a7ed | -12.41556 | -44.75383 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0faf93aa-32e2-3236-b819-a8aac5e1dc51 | -11.61416 | -44.33559 | 2025-09-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c8d55c19-f3c4-3f3d-80ee-aab264c85474 | -8.84777 | -46.20658 | 2025-09-25 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8615e5b9-1d5d-308f-8254-c8af4dea730d | -11.11482 | -44.89528 | 2025-09-25 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c2f08ed3-ca7f-30dd-87f6-4fcd7f9f88c2 | -11.80122 | -45.58614 | 2025-09-25 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 10947dae-9824-3a8f-b629-3fc6db32a5bb | -11.53184 | -43.65627 | 2025-09-25 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d93a2e08-316c-331d-af74-c9e1a10d7407 | -7.26219 | -44.90282 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| a52ecf90-5539-3dda-81c0-0eb3fdea7888 | -12.4075 | -44.76653 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b740e765-0b90-366c-97cb-e4e368be0c80 | -12.43458 | -47.96531 | 2025-09-25 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 63906499-94dc-3382-acf7-55c5eedc908f | -6.54952 | -43.84123 | 2025-09-25 00:33:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 36646d6f-f725-313c-bfb3-9c71f330a469 | -7.24029 | -47.34486 | 2025-09-25 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 71d440bd-5447-3d7c-b6c1-6321f9c70125 | -12.43582 | -47.9743 | 2025-09-25 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ca8f14a-439a-3700-97e0-539bc823e1ee | -11.616 | -44.34769 | 2025-09-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 16208608-cb12-3df4-b351-aa02695e9b19 | -11.63562 | -45.35217 | 2025-09-25 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f1c57413-6a80-3d8d-a093-05fd146c8cb2 | -11.52975 | -43.64263 | 2025-09-25 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ab6a02b9-5e47-3e35-b98c-cc549ca80a48 | -11.79971 | -45.57593 | 2025-09-25 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| af096a35-8202-3712-b5dd-331c861a354c | -12.51859 | -48.10322 | 2025-09-25 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a44fe68e-f8f6-3bf7-bf11-1840b6c5109a | -12.40582 | -44.75541 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bcc32353-1aec-3440-840d-7a2bd7fcd6df | -13.559 | -44.51305 | 2025-09-25 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b99ff48-17f1-312a-8135-ebf865d5296a | -6.41942 | -43.07102 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 186.7 |
| d861e031-63ab-3d81-8f02-c2d25e9e8c36 | -11.40316 | -44.97006 | 2025-09-25 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e0538a23-6e8f-3467-a3d0-48a623cd2f14 | -6.41891 | -43.09525 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 10680ea1-59b4-398b-8497-c1bdcc9be21e | -12.85582 | -45.29514 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3a0278f9-a262-3b64-a91a-d8a2c8d3cb11 | -11.69601 | -44.4024 | 2025-09-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 145b125f-b0d6-3a1b-ad71-c08577a12a7d | -11.79184 | -45.58752 | 2025-09-25 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c6a190ba-4316-3cc8-8c2e-9cbc9b39c250 | -7.04248 | -46.4106 | 2025-09-25 00:33:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f53fe001-25e9-368d-87cd-64919cb62390 | -12.41388 | -44.74266 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 61671884-79e1-30bd-95cb-fe8db6812548 | -6.6893 | -43.14349 | 2025-09-25 00:33:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f888399d-6491-3abc-b084-7ed6c8f26913 | -7.30001 | -47.96841 | 2025-09-25 00:33:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 72b8b831-d9a7-3778-8850-fe327c7bca3b | -7.31603 | -45.75245 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| ae79a60f-fa6f-3250-bd54-c641384d24a3 | -6.34713 | -43.35803 | 2025-09-25 00:33:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c86c72b1-41b5-33f2-95a1-1915301fe8da | -13.90428 | -43.34934 | 2025-09-25 00:33:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 28d7f5ff-fc1f-37cc-bf08-453b171b0edc | -14.05316 | -43.0867 | 2025-09-25 00:33:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 659d2cc3-ed15-3d20-9f2c-03e98b40a28b | -7.04397 | -46.42101 | 2025-09-25 00:33:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ce47fe19-9bc0-334c-a4ef-d0eb7182fafa | -11.40141 | -44.9585 | 2025-09-25 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 11c2279b-2f66-35a1-ac90-cc571709c739 | -7.44297 | -46.12744 | 2025-09-25 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 85cd6e56-bb65-3703-abb1-f47b346b601d | -12.32524 | -47.84109 | 2025-09-25 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bd3eb69f-e9cf-3b10-b21e-10f6c4ee0219 | -10.93775 | -44.27275 | 2025-09-25 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 555d2634-dbbc-3e02-9ccf-842f3652bfef | -9.05615 | -47.01385 | 2025-09-25 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fc284a89-ddf1-351a-b25d-0a6bb6199e41 | -6.59631 | -44.61624 | 2025-09-25 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e2629010-b09a-30de-9a6e-b1efcfbcc336 | -11.64354 | -45.34011 | 2025-09-25 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1511305d-4236-35bc-b997-76bc78c231cf | -6.41626 | -43.0772 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 235.4 |
| cbf32d0c-360a-314f-844e-a7e867370d71 | -10.57608 | -43.82322 | 2025-09-25 00:33:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 702eea58-e710-3629-943b-d538aeeff04e | -6.56518 | -42.06083 | 2025-09-25 00:33:00 | TERRA_M-M | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 99685a87-a82c-3114-9310-2d1e0d64fb87 | -9.15221 | -46.65777 | 2025-09-25 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d3557fa-9e74-3994-bcd6-76267153ff9f | -11.64514 | -45.35078 | 2025-09-25 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3abc23ef-a57f-3f13-a940-bfff7724ba2a | -8.49837 | -45.01366 | 2025-09-25 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2b78a037-bb4c-3385-bbe8-299beb669763 | -9.14514 | -46.66454 | 2025-09-25 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1163da25-df2b-362b-94e4-8739a224f061 | -12.85529 | -44.67579 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eda27beb-27b0-3a2e-8664-9734b6728c15 | -14.52112 | -47.79649 | 2025-09-25 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3adf978c-341c-38ac-b3cb-46833286c7bd | -9.56409 | -47.53542 | 2025-09-25 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f451c3d9-8398-35a0-84d9-9922f74d2ac1 | -13.46669 | -47.82376 | 2025-09-25 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1b5b9998-11e6-3d5c-bdeb-608ef81a5a26 | -7.99989 | -45.72549 | 2025-09-25 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1b65e2de-2066-32fd-80c7-8eba94ca42c4 | -11.64711 | -44.41654 | 2025-09-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b1af5e80-6151-3d0b-960e-57094cba7c81 | -11.11309 | -44.88393 | 2025-09-25 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| fa018239-7f2a-308f-beba-218b629cf8f3 | -12.54258 | -45.80116 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| da461b18-cdc9-3c1d-ae09-9cd892614c8e | -11.78882 | -45.56707 | 2025-09-25 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2a5d8ab4-2dd5-340e-b527-6030994081c4 | -8.84631 | -46.19651 | 2025-09-25 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 83bcbe2b-37c7-3810-bbcf-b454a8f0415a | -7.81259 | -46.89799 | 2025-09-25 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a05c220-ff52-318b-98c8-7af59b9c81af | -8.48822 | -45.0153 | 2025-09-25 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9306bc6d-8478-3ba7-8a73-f14cf17bd961 | -11.79033 | -45.5773 | 2025-09-25 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ee348fd4-d7e4-39af-a888-e96494e83af7 | -11.66727 | -44.4133 | 2025-09-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b52920e4-1b38-320e-b9fe-f9157e54c47c | -12.54113 | -45.79131 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5ff5f0f3-3d89-38be-96f6-58aced18e04e | -11.49146 | -43.53686 | 2025-09-25 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4cab8ab3-a226-35fd-be03-76350568cb43 | -6.74765 | -46.41962 | 2025-09-25 00:33:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f0029f4d-86ec-3338-b6b6-512155557af1 | -12.50976 | -48.10451 | 2025-09-25 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README3.md)
