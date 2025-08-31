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
| 1438eddc-c0fc-3061-a065-0d35fb2c925d | -11.3112 | -43.69 | 2025-08-31 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 32d0583c-0bab-3034-8e4d-0f5d9ef22826 | -11.2929 | -43.6456 | 2025-08-31 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| b7610492-3e07-37b9-ab29-8f25c220a5c6 | -4.1604 | -46.7881 | 2025-08-31 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 8a38b8ba-0e55-315c-b8e0-3af80eec1739 | -11.3116 | -43.6664 | 2025-08-31 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2bcea387-8d91-3cf7-a81f-d8d9d4798802 | -8.875 | -45.0961 | 2025-08-31 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e15e2b14-375b-3c32-8b78-7b10c47a24bc | -3.8146 | -48.9515 | 2025-08-31 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 367ed17e-5448-3aac-a235-1e5e625927fd | -10.5937 | -44.331 | 2025-08-31 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 84e77b82-f6c8-33fe-bbe8-da38ac10b6a8 | -7.0951 | -44.3128 | 2025-08-31 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 246.5 |
| 02f1d738-de9d-38e4-84ca-35ff96dbd83b | -10.9515 | -50.8296 | 2025-08-31 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| b9482583-fdd3-31bc-b871-a193720a8273 | -6.1853 | -43.3257 | 2025-08-31 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 8fbeb8e8-b076-3c52-9cfe-7d52576e5e34 | -8.8939 | -45.094 | 2025-08-31 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 8a2035e8-c6b1-3db7-9096-ae8570302a7e | -7.1139 | -44.3111 | 2025-08-31 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 2dc022d5-1484-3529-816c-8c71bc777010 | -10.3126 | -59.2023 | 2025-08-31 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c3c6c980-bbbd-3f6a-a0c6-3befc9fd5657 | -11.3504 | -43.637 | 2025-08-31 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| fb331676-0a62-3978-ad56-10283e1986f5 | -8.6849 | -66.9355 | 2025-08-31 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 038465b3-6ca2-3934-8f42-68dc952799e3 | -7.9265 | -63.0158 | 2025-08-31 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| b6f35a80-2350-3f29-8020-5116554a6f0d | -9.2745 | -67.6433 | 2025-08-31 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 203a056b-0e42-38fe-a45b-294357405040 | -7.908 | -63.0164 | 2025-08-31 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 6a7534d3-3e4f-319e-8d98-a43daaad89e1 | -11.3304 | -43.6871 | 2025-08-31 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 2cca30c1-c002-3828-92bf-d4d991037ae1 | -9.0615 | -65.4169 | 2025-08-31 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| db213625-3f55-37e7-955a-9ad23a17c594 | -9.0614 | -65.4355 | 2025-08-31 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 658cb844-c809-30c9-89f3-d715300df574 | -16.2025 | -52.6807 | 2025-08-31 00:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 17d1adbe-9616-3cb3-87d5-bf90408b48a2 | -11.3308 | -43.6635 | 2025-08-31 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 93b3c6e0-d985-326a-9536-93d9c0a70db5 | -16.2221 | -52.6778 | 2025-08-31 00:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 3b65b0c3-a37b-34d4-8cf4-abd83ff43784 | -16.2217 | -52.6992 | 2025-08-31 00:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| df2c375e-3fb4-3652-b0ae-3f2355f4d644 | -9.0799 | -65.4349 | 2025-08-31 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 520919df-3057-3581-af9f-06f3a028a00e | -16.2225 | -52.6565 | 2025-08-31 00:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| bce3d020-9270-393c-8d05-7d7e8e77bfd2 | -6.1665 | -43.3273 | 2025-08-31 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| d696da7f-3bfe-3754-915b-add7cfe7e90b | -7.0774 | -63.1948 | 2025-08-31 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 25d1161e-e991-3479-9e89-3d2a47c60118 | -18.64943 | -42.49665 | 2025-08-31 00:26:00 | TERRA_M-M | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| f2d70f84-b473-304f-adfd-86cd637ecd4c | -22.73398 | -47.01573 | 2025-08-31 00:26:00 | TERRA_M-M | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 26e9c240-c8df-34f1-bc59-2f8cf57465e9 | -20.09295 | -47.74416 | 2025-08-31 00:26:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 511c07a2-57f3-314d-8ab0-3daab71c1a16 | -20.09588 | -47.73802 | 2025-08-31 00:26:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d8a1861f-9388-3af9-849f-3134310a134a | -19.09486 | -48.30746 | 2025-08-31 00:26:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5dae9482-cbfb-3e61-97b2-f074351cad8d | -20.09723 | -47.74918 | 2025-08-31 00:26:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| fc90089e-5546-333d-abf1-b24350d5281f | -22.21108 | -45.87053 | 2025-08-31 00:26:00 | TERRA_M-M | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| d3103a8a-6549-376d-b774-fdd36e6e32fc | -19.10467 | -48.3061 | 2025-08-31 00:26:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 6680a015-d554-32b2-bed6-22239ae68a9d | -19.09345 | -48.29587 | 2025-08-31 00:26:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 73202b73-5386-3f4a-987a-6635e57e086d | -19.98776 | -46.99723 | 2025-08-31 00:26:00 | TERRA_M-M | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d4203131-e185-39af-aeac-d0990a21be4c | -20.09438 | -47.75542 | 2025-08-31 00:26:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dfb4f6be-a38b-3a0f-8c17-fbb58caab732 | -13.34518 | -46.98497 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d9ac4b9b-4fe4-3ce6-b534-5dbf3821ecc3 | -13.34781 | -46.93831 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5a463613-257e-3703-80f9-9b6da7d36789 | -13.40557 | -46.95163 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 33089a46-6c6e-32ef-90e6-e8ab0f4c78a0 | -14.03749 | -44.57628 | 2025-08-31 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 38868e2b-549c-3139-b818-a881ede5d54b | -16.08217 | -43.62402 | 2025-08-31 00:28:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b84bd79c-8174-3e49-af89-7d836d47772b | -13.36038 | -46.96416 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 30482668-f6e8-3efd-9635-91e942df5dad | -16.97673 | -49.30328 | 2025-08-31 00:28:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 222756c3-4745-3c67-81ec-c199d7233dfe | -11.83306 | -46.43523 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 2701fd2f-f6d7-330a-8b70-abd2bdc3ac4d | -11.80683 | -46.4543 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 36a97616-7042-3045-a1e2-8632c750335b | -11.81441 | -46.44394 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2fd0df68-e79c-35f8-a4f4-7ec57c3c5e59 | -13.30946 | -44.27119 | 2025-08-31 00:28:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2f5dc312-24e2-30c3-840e-7b3b6c201d6f | -17.15355 | -46.0828 | 2025-08-31 00:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cb5a15f5-48a7-34c1-8360-48cd7bb23b34 | -13.35279 | -46.97458 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 93e378e6-d117-3f54-90b7-0d1b1319b3de | -17.9678 | -42.99033 | 2025-08-31 00:28:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 229fe73e-808a-3407-ae07-4bdde4c3a3ae | -11.36518 | -43.60501 | 2025-08-31 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 542df190-8969-3dc4-9a4b-c6c8e59ee26b | -12.88312 | -48.8862 | 2025-08-31 00:28:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 39afc146-a37c-3f05-8089-418b5174e0f4 | -13.57688 | -46.92374 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0fa643fa-21ab-3a11-a586-56c83328bd57 | -18.43916 | -47.24342 | 2025-08-31 00:28:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 786d522b-0599-3e5d-9659-08efb3fe52b1 | -12.63487 | -48.20094 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| bfa5c98c-15ae-3a3e-8c04-880712ec8760 | -11.822 | -46.43364 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 95eace64-c6b3-376c-b164-3a94b110449b | -13.99965 | -46.32241 | 2025-08-31 00:28:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 639b2a77-2697-3ca3-99a8-01f09d579c95 | -12.40121 | -46.47983 | 2025-08-31 00:28:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 18162bb0-2f9b-32a2-884d-6183ad405956 | -14.54755 | -52.00147 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5c25070e-6061-3213-bdcd-aa3c8a835b8e | -11.3487 | -43.63151 | 2025-08-31 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4fff2e5b-0ee3-34ce-a272-6a8244e14408 | -12.10377 | -44.72305 | 2025-08-31 00:28:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e8576402-7dd9-31ff-a40f-d338b5bbed89 | -13.33108 | -43.18891 | 2025-08-31 00:28:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a2955bf8-f9ba-37de-a627-307e94aa1718 | -14.55076 | -51.97776 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 39.0 |
| e73e88c6-81ba-3a19-8c2b-46825f19d45c | -11.80809 | -46.46328 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b8d698f6-470b-3a05-a9cf-5bc638931eca | -17.47919 | -47.00189 | 2025-08-31 00:28:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 332e7c6e-a1f1-36a6-9959-cb7761e912a9 | -15.11289 | -47.88289 | 2025-08-31 00:28:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c77635fc-838c-34dc-9cd3-e3b23f72af7f | -11.86082 | -46.50454 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7aff6fab-f06c-3bc9-848b-01b3237520d1 | -11.82659 | -46.79019 | 2025-08-31 00:28:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2459dab-2556-3dc2-ba6a-3a6d7f6818b8 | -13.30869 | -46.91631 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8cd92d37-1ba2-37cc-b9b5-de0d4dce3803 | -13.47857 | -46.94361 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c60ec0be-4738-3b1e-a7ed-2e9042c12f81 | -13.35914 | -46.95511 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 142b882e-69dc-3eeb-8c48-a340fe7ea24b | -13.36922 | -46.96283 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8651d11a-2752-3f41-86e1-2babcd4e83d2 | -13.54305 | -46.95296 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 616b6a96-8e94-35ea-9931-0f5ba768da3f | -16.23894 | -52.66439 | 2025-08-31 00:28:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 96a63924-fe6e-3f4b-abc6-b09654ec1967 | -11.89491 | -46.49031 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 96ac5c49-722f-329c-b155-a57b51be2206 | -13.33896 | -46.93961 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d636bc6a-bced-3c94-9161-05569db4779f | -13.5443 | -46.96209 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| e0163079-c527-3fc1-9b5c-79a7bfb990c3 | -11.90123 | -46.47102 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2ada8e8-7efe-3bf4-abde-b1541945d2c7 | -18.06604 | -45.95863 | 2025-08-31 00:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 869e91cd-b601-3350-a2ce-9de31e6fd088 | -11.79167 | -46.47488 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 117437e2-812c-3062-af15-7af2d5994849 | -13.67009 | -46.93141 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0065980a-6dfe-3188-9edd-493e6fb9be2a | -11.34253 | -43.52344 | 2025-08-31 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b59bfc41-0e35-3137-b8e6-1348f58fe3c5 | -12.41761 | -46.46823 | 2025-08-31 00:28:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a39fa2d-3021-3a68-9183-3e5ed2cf667f | -11.35694 | -43.61832 | 2025-08-31 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 37bad4f8-764f-3ede-946d-50c6e870ae41 | -13.4975 | -46.95011 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 0d44b4d4-b446-3847-8ba7-20d551df3bc1 | -12.83989 | -48.15008 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3701104d-f44b-3d4a-8f76-69b0ae51d64f | -11.86208 | -46.51353 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c7ee6eda-7c17-3c95-ad03-d61f955c10f7 | -11.36806 | -43.55591 | 2025-08-31 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ff834e79-a025-3029-b485-d2f7eafb77dc | -18.06478 | -45.94935 | 2025-08-31 00:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 5131598d-e41a-3738-b044-03d2be69dcd7 | -13.67148 | -46.87548 | 2025-08-31 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62d75a00-fd02-32fc-9d2c-c3b10f701f57 | -13.51009 | -46.97616 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 1bd5dd24-0242-3d16-a28d-1f30aca166eb | -18.50956 | -49.02916 | 2025-08-31 00:28:00 | TERRA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| f03ec287-c8d9-3dd1-baa0-d32e7765092b | -16.21513 | -52.68823 | 2025-08-31 00:28:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 183.9 |
| f9750945-9091-349f-bd70-5772805e24e3 | -12.09595 | -44.73458 | 2025-08-31 00:28:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 220ef3c6-2364-3043-827d-4025f6609f68 | -12.64924 | -48.16953 | 2025-08-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 55a58633-c4c3-369d-b45a-2c1bcab24cdb | -13.51894 | -46.97486 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |


[Clique aqui para ver as próximas entradas](README3.md)
