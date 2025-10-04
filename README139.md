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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c11ee82e-58dd-39f7-a1d9-4210a3b10df5 | -11.48096 | -45.02662 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| a8e5afe9-67eb-3ebd-a72e-f3a63b685273 | -12.87461 | -47.28646 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 9e028837-7ab9-37a3-a8bc-786bcf57c4c9 | -16.27839 | -47.09845 | 2025-10-04 12:19:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f7a33202-06c3-3067-bfd4-e2c08885db30 | -13.17522 | -50.89371 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 741fd1ff-d86e-3155-b742-c2d97abb2230 | -10.32546 | -50.33913 | 2025-10-04 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 43bfa4cc-1229-385e-80cf-353a822ec245 | -18.8902 | -44.6833 | 2025-10-04 12:19:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1ae789ce-a16b-30f3-9152-eabcae5bf88c | -11.07579 | -47.69389 | 2025-10-04 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 19e42529-fa19-388c-ba53-4cd3ab980ff0 | -11.10478 | -47.74375 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a179e950-f408-36d8-a1d9-f0ed0e96867d | -10.07463 | -48.18059 | 2025-10-04 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 446410bb-ae82-3304-8429-1e43b361f9b7 | -11.97643 | -51.47253 | 2025-10-04 12:19:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3e5bb1cb-c5b9-31c5-8c1c-ca0fc5eb80a7 | -9.96847 | -45.79372 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 87897609-72b2-39ee-87c9-7aa03a3627b6 | -11.07673 | -47.8767 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d2aeb3aa-33a0-3309-b9e8-b908bd57ac5c | -11.55501 | -47.69243 | 2025-10-04 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 92006586-03e6-3236-be2f-1918e675b9ce | -13.1192 | -47.83786 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 33700a86-a274-3230-a45a-f5de14d0042b | -10.71613 | -47.88225 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d829a0f0-7fcc-3d4a-a295-a6652664896b | -10.58504 | -48.72448 | 2025-10-04 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 8d7d853c-d956-3435-ae67-87621bd593f4 | -18.38244 | -46.56328 | 2025-10-04 12:19:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9556d62b-7f74-3772-9851-3284944df9f8 | -12.81392 | -46.86138 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 39e8a620-3009-3498-8791-263a82a7ef31 | -16.95177 | -48.16024 | 2025-10-04 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fbf790e2-fd23-30c9-9595-90a8171e7d49 | -15.61372 | -52.47724 | 2025-10-04 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 901ea5f9-bf9a-31a6-95a5-1a23deeab9d6 | -11.54743 | -47.68219 | 2025-10-04 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e711cb24-762c-38a3-8296-75e26bee8d86 | -12.08159 | -45.1963 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b0198014-9a54-34b9-a5d5-b5e1e8b2a474 | -14.92864 | -48.34235 | 2025-10-04 12:19:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4a8fe780-a385-38db-93aa-27930c0a2d7c | -16.96762 | -48.38077 | 2025-10-04 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 38afa0f4-26c6-30b8-aa88-9367a41d3d04 | -13.17684 | -50.88328 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| fb54ab94-fc7a-3c6f-8278-f6adc2914a24 | -16.08718 | -51.06703 | 2025-10-04 12:19:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6e1e0f5e-bc54-38c4-8991-492b7dddcb13 | -13.19863 | -50.99417 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e6531bfc-861c-3efa-8da2-171250d96aaa | -13.32128 | -48.10776 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c9aa38b2-f79a-355c-9ec9-9ad84b2e143b | -13.81498 | -43.17617 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| e6bea1a5-faf4-351e-863d-b2eaeb9d8923 | -11.49696 | -44.98248 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 12c16808-26e5-3c27-ac53-e0fcc14b8ecc | -14.88975 | -48.34943 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c05e4248-586f-39d2-8fcd-8f63d52a648d | -15.86269 | -46.25473 | 2025-10-04 12:19:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 4a807627-053a-31ed-9aa1-a9fd1a00f972 | -13.3187 | -48.12589 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| f8d209da-3fb3-3116-9133-d3abb7014198 | -9.17552 | -49.94699 | 2025-10-04 12:19:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 478d0a4a-b95f-3514-b1e1-ae5eff27f85a | -8.9085 | -46.59802 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| cea516e5-0642-3689-9c07-b2816447819e | -13.26336 | -47.20462 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 636ccd2a-a3b3-3cfa-8022-3b7fbcc78aa8 | -9.33381 | -45.65422 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| af467e60-5832-39c9-8a0e-0d25854e7dac | -14.89123 | -48.27502 | 2025-10-04 12:19:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 79439bca-2838-328f-ab14-620e854dcc43 | -14.22001 | -46.07029 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 216.2 |
| e5219689-0b3b-343b-8cc5-a97ec998d0d9 | -13.29346 | -47.58564 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 1cf1a922-3b80-35f7-9d99-f6e2e1898ceb | -14.63565 | -48.25607 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| c3abfed7-1bf9-3c19-a571-13779ff95520 | -12.30576 | -45.35902 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 280bf7f5-6914-3e8e-ba8f-55f0661fe5c1 | -12.53435 | -46.00922 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 348.7 |
| f6e8e88a-376c-3067-affa-a15a08903a07 | -11.68265 | -51.71055 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| da07f76d-407d-35f8-a1d8-8cdb65f86f79 | -10.93009 | -47.02662 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9a3450d4-8305-3797-ae5b-13d7dda0dac6 | -9.39963 | -46.44458 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b1daa833-3bca-34e4-a82f-82732a7ae730 | -11.12119 | -47.75522 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 7343f1ca-4140-30ee-bd12-582afa2027b1 | -12.40444 | -45.22936 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ed8027ed-c622-31c0-83b7-dd23fc96874c | -11.80168 | -48.92578 | 2025-10-04 12:19:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 7c14873d-7c3c-321f-9422-80c025ccd70e | -11.92247 | -46.3796 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 027cbeb6-8de2-3ea5-8de5-8f6e15aa8eff | -13.10885 | -47.91091 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| daa7ccbe-b467-3072-bd30-812a8ca7b914 | -13.11662 | -47.85613 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b45e6958-cc5a-3721-994c-bfc06c7aa274 | -12.40525 | -51.09399 | 2025-10-04 12:19:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 2ff0fcc1-143b-3134-b38c-ac23180e0c80 | -17.9975 | -49.81865 | 2025-10-04 12:19:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| b1e78826-2430-3ce2-86ac-c6b7dbe17c2a | -11.64376 | -46.86497 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 68ba3e65-1bd9-31d2-941d-06444e4143df | -9.28974 | -45.97507 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| d3b212cf-dc47-36cd-a71a-0032c57945ac | -13.46683 | -47.26453 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| dfd1bc82-2f2e-3634-89df-00191ec80163 | -11.81253 | -50.08529 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b0a6dfa5-1741-3e17-baac-fa62b09bcfc5 | -19.00462 | -48.08948 | 2025-10-04 12:19:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 117.5 |
| a1ab7166-d0ab-3115-be33-42aebfac2748 | -12.40381 | -45.22343 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| af2b76e3-6bac-380f-8a43-2cbb146df147 | -13.31641 | -47.617 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 60b44002-d148-3367-af7d-794bc6406e02 | -13.18122 | -50.98063 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 310.1 |
| 4385f37d-6458-3751-9887-2c20864692da | -13.16383 | -50.96711 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e57f8391-1307-319f-8e5e-9f72c5d1ff92 | -14.4445 | -46.37842 | 2025-10-04 12:19:00 | TERRA_M-T | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 268849eb-dc29-3607-905a-0f666ba66753 | -13.33175 | -47.57256 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 274f3b7e-8f60-3a67-a54c-baba22f518a2 | -14.98425 | -49.98853 | 2025-10-04 12:19:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4e5a4410-7bf5-3f1a-870f-82cb105dcbfb | -9.30023 | -45.96674 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9633982f-5b9a-3164-a609-193f426e6e59 | -14.91772 | -46.88765 | 2025-10-04 12:19:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 46d70794-1edf-3cbd-8dfc-26e7d019f78f | -11.86872 | -44.9515 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 19cd02c2-4706-39bb-8da1-6405412d7f50 | -13.29855 | -47.61445 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| a8aa398c-c4c8-3bb1-a071-d2f90a7eccca | -16.09459 | -51.0645 | 2025-10-04 12:19:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d5f15294-ae92-3724-a089-f173f79a514b | -11.92113 | -46.38942 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 3bd77aa7-320a-3aca-90bc-0a7f7313dee5 | -14.24751 | -46.11345 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 261d9092-7f5a-3be2-a0c7-40bd387064d7 | -15.61503 | -49.40396 | 2025-10-04 12:19:00 | TERRA_M-T | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 655e0e2d-d2eb-39d5-96a4-ce1b39060412 | -15.31444 | -46.30974 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 88831b19-c8df-31bb-887e-df32ac6e9f76 | -16.00685 | -50.92485 | 2025-10-04 12:19:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8520a167-aad2-309f-9f44-7a80b2f7e603 | -12.08762 | -45.15054 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c195f9ed-25e1-387c-8984-b5c14e67c15d | -13.29934 | -47.86726 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| f490d3ad-cf0c-3d70-af46-b27c96a2a47b | -12.65785 | -46.98864 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| cedd8a17-aaeb-3eba-a579-9d5c0cf44b2e | -12.81525 | -46.85181 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a2a483ac-384a-3142-8b68-2a627f163c0a | -16.0654 | -50.8995 | 2025-10-04 12:19:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8f7b0552-4b4a-3eb3-a896-482ffa42b0f6 | -16.43167 | -52.17364 | 2025-10-04 12:19:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c709483d-69a2-385d-ad2c-36b19230a70c | -11.79655 | -46.82567 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 48a1e696-b582-3ce0-a479-73ff8791e8d1 | -14.4186 | -52.87661 | 2025-10-04 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 727ea9eb-787d-34c0-905a-efbb8e9e1570 | -12.40694 | -51.08313 | 2025-10-04 12:19:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 80b0ebf3-7259-357a-9278-7aa8804cc772 | -11.2458 | -47.79475 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| cbb59347-6a7c-310a-87f6-a09fa45bf1ab | -11.92865 | -49.92903 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 712865cf-a2bf-3d71-b13e-30c1a19e7604 | -10.34331 | -48.17412 | 2025-10-04 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0e5e46fb-985c-3339-aa1c-dca2912da7e8 | -10.10691 | -48.3318 | 2025-10-04 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e9379a59-9d77-371a-8c82-8a051860c38e | -10.84019 | -47.20333 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 8647d760-e96e-36f8-9fa5-24924b124229 | -13.65858 | -47.86904 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 3b1499ba-79fd-38f8-982b-22c37b84084b | -17.5929 | -44.44894 | 2025-10-04 12:19:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 313106db-4ddf-3c5d-b5f9-44baefad8958 | -12.40591 | -45.21797 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 66ae8559-5996-3f61-8308-cfd50259a111 | -10.74006 | -47.90391 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5eb05450-33be-30f8-b21a-2c8c38ef7d89 | -8.99208 | -47.49947 | 2025-10-04 12:19:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5c379025-3f9a-3e83-a58b-73f0a55010c9 | -11.91211 | -46.24807 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| e36920b3-2e53-368e-bea8-dcfa931f9774 | -13.29217 | -47.5949 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| c7aeebc9-11a3-3bd4-9dbd-891cb7a5b570 | -14.22569 | -46.05625 | 2025-10-04 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 7ddb7e4e-b205-34f9-b584-7fa267f86f77 | -13.59706 | -48.17599 | 2025-10-04 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c2390446-2d1e-3a32-87d3-e115f61928f5 | -11.95924 | -49.3559 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |


[Clique aqui para ver as próximas entradas](README140.md)
