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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbe59b7b-ad29-38a4-b837-6b6b2694d5c6 | -7.7885 | -44.5228 | 2025-10-05 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 951d170b-727b-3b34-9016-6a3e13081a7f | -15.5832 | -52.4488 | 2025-10-05 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d5b578a6-c007-3cc4-8033-6cea4c1e9695 | -11.2429 | -47.7827 | 2025-10-05 13:30:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 38fab63f-6d87-3185-a591-fa304037cc1a | -8.5581 | -46.2611 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 79e75418-b9fa-3be0-b02f-1aa6fd3dbc95 | -13.7473 | -51.3097 | 2025-10-05 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 08c97ece-539d-3722-903a-e52d32effa96 | -8.677 | -45.7988 | 2025-10-05 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4da76d0c-12a5-3c5d-be16-4a0739818b46 | -11.5264 | -46.742 | 2025-10-05 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| dbef39bf-6a04-30f6-a8c1-fb568ff9abcb | -8.5953 | -46.3022 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| dd7dd001-79ce-31d7-ac83-e2ed1421422f | -7.7938 | -42.5607 | 2025-10-05 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| 17f82c89-aecc-3248-818b-51d66e5b9eca | -19.0155 | -50.6045 | 2025-10-05 13:30:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 178.3 |
| 6b1bbafc-c111-3841-aff9-dd3fff2c824e | -7.0558 | -42.7782 | 2025-10-05 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| eb986cfb-cc3e-30c7-86f1-50c814f75b3a | -7.699 | -42.5946 | 2025-10-05 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| c93984c6-c56b-38e0-aa42-24cac11bc39d | -7.0367 | -42.8036 | 2025-10-05 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 161.5 |
| 5b8fc641-e277-3d5b-b37f-8183872ffd96 | -12.5672 | -54.7698 | 2025-10-05 13:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 42b78f21-a27e-3010-a9c9-717e8f970d59 | -11.526 | -46.7645 | 2025-10-05 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 361.6 |
| 1eb4bee8-0cdb-35ba-ae93-f3cbf3f9a57b | -7.7308 | -46.2513 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 510877d4-5dc0-3468-b67b-6160b2b0ecdf | -11.4298 | -43.4833 | 2025-10-05 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 03be4ef0-fdd7-3e42-8c37-20b0fe38beda | -7.2416 | -42.9957 | 2025-10-05 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 6c125ae8-bf35-334f-807d-821ee273ab1c | -17.9408 | -57.5928 | 2025-10-05 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| f3b1c958-d612-3739-bb95-7b5dbe82b5a1 | -15.5824 | -52.4916 | 2025-10-05 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 8608c11e-41d8-34c4-a588-726c10bbf7b4 | -12.5487 | -54.7307 | 2025-10-05 13:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| bf59abb5-82db-393f-b944-8fa1571fc9a1 | -10.8093 | -48.8229 | 2025-10-05 13:30:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 9b07fc45-ca82-3b43-ae3f-f420a4d061b4 | -8.595 | -46.3246 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| c1e2c523-4d7c-3046-ae7c-60c6683c3e56 | -9.5791 | -46.1286 | 2025-10-05 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| bc524e4e-fc40-3059-a892-5ee304363028 | -15.2211 | -56.8006 | 2025-10-05 13:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 2695c97e-bc60-315f-becc-2b2240236df8 | -12.5675 | -54.7493 | 2025-10-05 13:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 02deb2fe-d0c3-3a11-b2e8-69fb76c24024 | -7.4464 | -46.5223 | 2025-10-05 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| af3ce83c-2db0-3ed3-aa8e-5bfcbd036021 | -9.2439 | -51.8133 | 2025-10-05 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| d838d186-112f-3446-bb24-8755057e86bf | -9.6287 | -46.6394 | 2025-10-05 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 7f3a7d8c-d14b-3d27-86fb-eda00d9a3bc6 | -11.0313 | -46.7171 | 2025-10-05 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| de9aeeec-a14f-33a7-92a1-33d14f5aad77 | -15.582 | -52.5129 | 2025-10-05 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 500.5 |
| 4ac8b8b1-8061-3dd3-b901-67ae2551af03 | -9.2973 | -46.0026 | 2025-10-05 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| fa08d780-9ae8-30a2-9c0b-13d22be7ce5c | -17.986 | -51.144 | 2025-10-05 13:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 3300154c-5e03-3a44-806a-a50e0f6d6766 | -7.4276 | -46.5239 | 2025-10-05 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 84c885e8-d1cf-3145-a4ba-af14c165c2e6 | -15.1352 | -45.7337 | 2025-10-05 13:30:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 118.2 |
| ee38c868-f87d-3e7c-b449-fa31306a4f2c | -7.712 | -46.2531 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 326.0 |
| b7894ef1-932e-350e-a84b-a452d5f88f14 | -18.2569 | -53.3329 | 2025-10-05 13:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 594e2421-1df8-3e05-b8e2-f883991acb86 | -9.3749 | -45.8584 | 2025-10-05 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ca6c800c-4ca7-32f5-a857-3c9f6ae41d0a | -8.8803 | -47.6061 | 2025-10-05 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| bfe20ad1-96f1-351a-93ad-c27707246a5a | -8.1891 | -44.1357 | 2025-10-05 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| eff91864-22e6-380d-a9d8-662e5508f28a | -7.5078 | -41.2719 | 2025-10-05 13:30:00 | GOES-19 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 7d8c28ee-2fe7-370e-bf11-fc863d9f7337 | -9.1114 | -44.4029 | 2025-10-05 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 23c0c50e-5d79-367f-bae5-222ace97ae16 | -7.7118 | -46.2754 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 1fe8ce2c-60d9-36a4-afae-0d8449b5634f | -8.8618 | -46.0949 | 2025-10-05 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 93a84ead-56fc-3d4a-88c9-7ff8ed1639dd | -8.5578 | -46.2836 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 830b1fcb-e3e3-3a05-8326-d1257ffdc35d | -9.5794 | -46.106 | 2025-10-05 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 4768ed04-a907-3568-9289-e26a72278293 | -10.9497 | -47.0634 | 2025-10-05 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 59660eec-52aa-3050-a839-6d887dd49f28 | -7.7743 | -42.6103 | 2025-10-05 13:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 228.7 |
| e67abe24-2e10-32a1-9ee7-707dc913b7a0 | -16.0966 | -51.0829 | 2025-10-05 13:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 7caddf4d-21c2-326c-b93b-09e7edb57c0a | -21.6888 | -50.0559 | 2025-10-05 13:30:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.6 |
| 2b6392a6-2172-3db3-b7ae-4526fcf585f1 | -13.6909 | -51.2315 | 2025-10-05 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 115e2245-a7dc-3f64-9d8a-f0a04b305299 | -10.1497 | -45.9709 | 2025-10-05 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| fde9a05c-86cb-323b-b3b0-8de90ed48fc7 | -13.7284 | -51.2908 | 2025-10-05 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 161.4 |
| c7ddbc80-702c-327c-b22d-1a3808b40752 | -11.0978 | -49.8513 | 2025-10-05 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 04a36543-d32f-3332-9e28-1a5ff3c6b31c | -15.6015 | -52.5102 | 2025-10-05 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 229.0 |
| f8d8c463-c6ff-3527-ba64-be2de7eb78e0 | -10.386 | -45.4184 | 2025-10-05 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 42a135ac-ba7e-3fbe-bbe0-975ffc0ecbe0 | -8.5761 | -46.3266 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0565acd2-b602-37fc-af0d-1e8e0ab78030 | -8.5956 | -46.2798 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1eeb80c1-2879-344e-9a4c-8c12f7e58f07 | -11.0316 | -46.6946 | 2025-10-05 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 278.8 |
| 19b3ddc4-3734-3567-b878-a260447b3e77 | -8.5407 | -47.6831 | 2025-10-05 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 798177a1-cd48-36c9-aa46-50364fdefbff | -7.6993 | -42.5708 | 2025-10-05 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| afd7af0d-e81a-3016-b612-78dc4d9fff15 | -11.0126 | -46.6971 | 2025-10-05 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 298c1ac9-7fd5-3f44-b7eb-17e95de49b2e | -17.9661 | -51.1474 | 2025-10-05 13:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 114.8 |
| bbc66555-ed7f-33c7-8b54-db3f64f2fa1c | -11.5069 | -46.7671 | 2025-10-05 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 159.4 |
| bce43240-0c8c-3afa-bb63-2caa30bf8b09 | -8.539 | -46.2855 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| f1421d4a-71fa-3f8c-86d6-1a3d5c3149b6 | -7.0369 | -42.78 | 2025-10-05 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 178.1 |
| 32e6004b-2bde-3383-afae-dad91cdd1e6b | -13.7476 | -51.2883 | 2025-10-05 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| b43e2360-c5dc-3086-bba0-b73e604d4adf | -16.077 | -51.0859 | 2025-10-05 13:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 11b83581-6794-32be-bd14-5365ddd81375 | -18.2366 | -53.3576 | 2025-10-05 13:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 48c9b3c0-570d-369f-9ca8-c8305604b0a6 | -7.7932 | -42.6082 | 2025-10-05 13:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 9c552315-49c8-3bdc-8568-833749fd1d8a | -7.7306 | -46.2737 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 199486c1-d498-382c-abee-a2ec8f702c39 | -7.8127 | -42.5587 | 2025-10-05 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| c1aa2513-8a92-3ec5-9f22-c1a332c4a075 | -12.2876 | -49.2101 | 2025-10-05 13:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| cd1ec9ef-6a49-3995-a774-9d0481240582 | -10.4054 | -45.3931 | 2025-10-05 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 7bff72bf-1317-3169-8ff8-6552d27b5b4c | -17.9605 | -57.5904 | 2025-10-05 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 3735f7ab-e1c4-36a7-85fb-b923aff8efa0 | -12.5866 | -54.7474 | 2025-10-05 13:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 97e8ffac-1c04-3f9c-81be-8ef8e10e6d21 | -7.7123 | -46.2307 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e6385903-7ab4-35e2-819b-4123996be642 | -7.7746 | -42.5865 | 2025-10-05 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| f9ec5f61-0272-3a8b-b7a6-a85839934716 | -17.9404 | -57.6134 | 2025-10-05 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 77ba5bab-fe37-3736-9963-45bddfbca5cb | -8.8807 | -46.0929 | 2025-10-05 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 69492549-bda4-3c80-b69b-8d6f15a91f20 | -7.4672 | -43.0438 | 2025-10-05 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 5aab1573-d6e9-329c-a908-a4383229a8aa | -9.921 | -50.2109 | 2025-10-05 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6a81cc15-69a8-3b85-bd4b-bccfe73bec74 | -11.449 | -43.4803 | 2025-10-05 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| f9247cfe-9966-3494-be81-8699fa0514b8 | -7.7554 | -42.6123 | 2025-10-05 13:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 31f23925-0cf1-3b49-9f21-3b9238b0f942 | -7.7935 | -42.5845 | 2025-10-05 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 129.2 |
| 43cbd4ec-3342-318e-8022-ef9b0898b955 | -12.9179 | -45.075 | 2025-10-05 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| fa53c8f8-ed64-31e9-b4c2-bdbc6fce1e24 | -7.2392 | -44.8727 | 2025-10-05 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 57b8e58a-9cdc-3765-b27d-5579a70c14c6 | -8.5393 | -46.2631 | 2025-10-05 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| d92a409e-2523-3723-9f36-292a07123429 | -13.728 | -51.3122 | 2025-10-05 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 269.6 |
| c81b32a5-4991-3326-a41a-132c3c556896 | -18.1968 | -53.3638 | 2025-10-05 13:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 75cf3f4d-a6b0-3c81-9d2b-25d0e939a042 | -7.4669 | -43.0674 | 2025-10-05 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| 4b00a142-4fa1-3653-92ea-ad3595da0149 | -10.1943 | -45.5339 | 2025-10-05 13:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 149.4 |
| c296f520-63cf-313f-866a-eb44a7a117b5 | -15.6019 | -52.4888 | 2025-10-05 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a07ff821-4466-3fa6-92a7-c5dec9e766a9 | -12.5863 | -54.7679 | 2025-10-05 13:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 183.3 |
| f36d0e79-2fd4-35d4-b03b-89208e33ca54 | -7.4279 | -46.5016 | 2025-10-05 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 6f1ff04c-7348-36bb-80ac-ee40d7defd22 | -10.0504 | -50.4113 | 2025-10-05 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 467a9483-efde-3541-8ea0-b6f06a2a61cf | -16.077 | -51.0859 | 2025-10-05 13:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 1afefe02-ffd2-3c22-a5d7-2360b755dcbc | -11.823 | -45.0596 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 331.8 |
| 7ca8df2d-b227-3233-82c4-a0a1a0759fe6 | -10.1497 | -45.9709 | 2025-10-05 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a44cc0e7-5f72-3141-b9b2-74ab592def49 | -8.1891 | -44.1357 | 2025-10-05 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |


[Clique aqui para ver as próximas entradas](README159.md)
