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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 422cd339-4598-3f3d-84be-5291e8802e28 | -14.87204 | -48.21668 | 2025-10-10 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 61fbfcf9-179c-3943-a503-8f73be800318 | -15.41381 | -47.99117 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d793b916-4737-3583-9f14-ebe24d856fff | -14.27092 | -45.91129 | 2025-10-10 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3307e47b-b106-3a76-b000-999739de1b91 | -17.8903 | -57.51173 | 2025-10-10 00:33:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 4e1bf461-830c-39f7-b813-f2477669cc9b | -13.52319 | -48.11237 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40973bf6-6069-36b8-9ba3-a1877acb0323 | -12.43328 | -45.78823 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0d9e98f7-c9a2-386a-a98f-6ce95f3e5078 | -15.46784 | -48.53592 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| e8cbc96c-dcf8-3de0-befc-2a23dcf7249a | -13.38739 | -44.23653 | 2025-10-10 00:33:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8ff5df00-e3b3-333a-b7b6-6c745799ae55 | -9.65494 | -43.84934 | 2025-10-10 00:33:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 8ede36cb-7ae1-31d5-843b-038632123dc6 | -16.67602 | -47.59546 | 2025-10-10 00:33:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c588afb9-8a47-3be6-9bdf-79628c18f5b1 | -13.29424 | -47.1352 | 2025-10-10 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 81f533e0-7e43-3bd5-b6fa-a434050948e7 | -14.83989 | -48.44621 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c8501a9f-e64e-37a5-a20b-76ad9c32a8b6 | -10.85897 | -47.58143 | 2025-10-10 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19a7b0d9-e714-357a-9e88-1f51382e373b | -4.50406 | -45.88202 | 2025-10-10 00:35:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fbf0a0af-fc9c-30c7-b7b8-7cfe601eae10 | -6.58505 | -44.63646 | 2025-10-10 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 3fd7fba7-3a91-3d0a-97e9-29c1234708f4 | -5.47497 | -44.06065 | 2025-10-10 00:35:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8d85ecbe-0171-32d2-a0ca-2c582fdcbdca | -4.23657 | -45.9853 | 2025-10-10 00:35:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 22ccd51c-07d1-31af-bf70-434eb9660d5c | -7.20273 | -45.4822 | 2025-10-10 00:35:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3b889ee9-75a4-3571-8ae8-bec86434b306 | -7.80365 | -46.02543 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0f581b7e-91c0-38e1-8e4b-a2f233b130d7 | -7.04717 | -45.04566 | 2025-10-10 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 92feb220-47f2-31c0-9f0a-4012feda1168 | -3.7769 | -49.14428 | 2025-10-10 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bece0baa-a4b4-3b11-a900-f710a313305d | -4.65045 | -43.20131 | 2025-10-10 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| abc9ef8f-94df-30a7-9537-92478f58e6f7 | -3.00013 | -48.73643 | 2025-10-10 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c50862f5-8b62-36bd-829f-7378dba6254f | -5.65323 | -45.95895 | 2025-10-10 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7794f43e-9c32-3d68-be2a-3c7f00afda6f | -4.05631 | -45.27512 | 2025-10-10 00:35:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e7ed9f00-3e67-310c-b828-491e5494b4e6 | -5.6534 | -43.60419 | 2025-10-10 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d0bae74e-7da3-3278-aa8c-eb7e0fe385a4 | -2.6847 | -48.39508 | 2025-10-10 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c0d75c16-649e-35ec-8058-a25f29c99ed2 | -3.88162 | -50.97113 | 2025-10-10 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 739af47c-0bc7-3d07-8b17-1fa662873dda | -3.5967 | -48.97987 | 2025-10-10 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| db6e0ec9-444d-3470-8b0e-f9c509ba2476 | -6.81866 | -42.79586 | 2025-10-10 00:35:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 980923fc-bce3-318e-a289-5300444960a4 | -3.7064 | -50.97121 | 2025-10-10 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bee1b2a6-0491-3b12-9213-039c9fa2aa4d | -5.44417 | -43.51563 | 2025-10-10 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| e192056d-74eb-3bd8-8441-c10257292282 | -5.14557 | -46.26828 | 2025-10-10 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 27ac506f-1929-38aa-931e-c7686681528e | -5.10524 | -45.21375 | 2025-10-10 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3c4c2e18-03d4-3d0a-b0db-c6f30d18838f | -4.05608 | -45.28083 | 2025-10-10 00:35:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 77aa24f9-72d9-3d61-a32c-2686c7f94e76 | -8.49874 | -46.16283 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 307f847f-43fa-393d-bd80-4901537a58ce | -4.5021 | -45.86888 | 2025-10-10 00:35:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 99b6ee89-6d4d-3340-a72d-2ff9e26fffde | -2.94459 | -49.33213 | 2025-10-10 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 28b5002a-2094-3b89-a80b-a083de65e2a9 | -3.39122 | -50.15313 | 2025-10-10 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e6fd4329-40cb-3878-b5f5-7c888b0a1aaf | -6.6377 | -43.67859 | 2025-10-10 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| fc656cee-c938-365d-93d3-6d28238717ec | -5.92858 | -43.32655 | 2025-10-10 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 8b13f183-4da0-3ecf-8bfc-49598bb28dae | -3.69106 | -49.19007 | 2025-10-10 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 89c2486a-40ea-3e75-b4bf-4e1362e1b6ad | -3.15378 | -49.17461 | 2025-10-10 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ba87198-a8dc-39b0-8e1e-763f9fffc8e2 | -5.13545 | -46.26989 | 2025-10-10 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 01b03917-6cd2-3b05-8060-f3cf50cb8269 | -3.78663 | -49.42157 | 2025-10-10 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cedf97f3-0dec-33fe-a158-85448fdd11f0 | -5.10317 | -45.19955 | 2025-10-10 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f823ffc1-99f5-327c-8113-4e605017c7ce | -5.4607 | -43.52627 | 2025-10-10 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 519def42-655f-302e-b785-60c88ddc4df2 | -7.78752 | -46.54879 | 2025-10-10 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 63689c77-18cb-3358-b873-34e82e02c478 | -8.18605 | -43.3316 | 2025-10-10 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 10b34a10-3490-3631-b798-8f27f9f809c4 | -3.14372 | -49.03773 | 2025-10-10 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a4e69a8c-4313-3c05-bbea-bea0346ed81d | -6.23634 | -43.62167 | 2025-10-10 00:35:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d993a1a9-681d-35f4-ac2c-15c5131ef565 | -6.02083 | -45.8804 | 2025-10-10 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7c6f9bb3-44b6-3c20-b0dc-6e6068a2ec0f | -6.59401 | -44.61964 | 2025-10-10 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ea81f35c-1e2c-302d-9955-c29026a288b9 | -8.88865 | -46.01588 | 2025-10-10 00:35:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6ea14273-2eca-3503-abd8-3bbdf92bc8c5 | -8.52827 | -46.14108 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a0612683-f558-3f06-82c4-f4a6e18a15ba | -4.49715 | -45.8756 | 2025-10-10 00:35:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 332fb105-a474-37ae-83bf-b3331ade73f0 | -5.05318 | -45.85566 | 2025-10-10 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b44659b-799d-3b8c-8919-f0e31d56efee | -6.66857 | -47.74858 | 2025-10-10 00:35:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7b512baf-9bb9-358f-a203-8c5ea23a3d07 | -5.64296 | -45.96056 | 2025-10-10 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a253dd0d-ecb0-3934-b03e-a873b5fc5c91 | -5.25904 | -45.23545 | 2025-10-10 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1549a19f-754c-3555-8e39-01620ce674bc | -5.93149 | -43.34584 | 2025-10-10 00:35:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8ac8c3e9-1087-3214-a66b-636b51b09563 | -2.94584 | -49.3411 | 2025-10-10 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| b13a7f85-62fb-3139-8a70-b94f45dc2c7b | -4.2384 | -45.99823 | 2025-10-10 00:35:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5101ba43-fd2b-3325-95a5-3dbeb0be2a9d | -7.77494 | -44.05528 | 2025-10-10 00:35:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 21cef14d-14e5-31e6-8fa9-5c7b55da5d14 | -8.52526 | -44.60202 | 2025-10-10 00:35:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d1c0a1ab-74cc-3e40-8078-46f90083528c | -8.50689 | -46.15046 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 43b17059-95fe-3f82-b846-3cbb4bf9585a | -3.53273 | -48.92112 | 2025-10-10 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| fe8947d5-3827-33ef-a462-fcb68f90040a | -5.65503 | -45.97123 | 2025-10-10 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| fcfced76-d632-324a-a54f-c6b8fe506d95 | -5.95999 | -44.22858 | 2025-10-10 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c7452a66-a9ca-3e95-88cf-128c6c1b1f52 | -3.78786 | -49.43043 | 2025-10-10 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 8b69278c-5493-3357-86ed-650c1cf57497 | -3.57721 | -49.43625 | 2025-10-10 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04e81a9f-88e2-3367-9dd4-54f8edf37003 | -5.48524 | -43.08175 | 2025-10-10 00:35:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f1fe7a10-0fd5-3b02-89cb-aaa5380d67c1 | -5.83433 | -44.08477 | 2025-10-10 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 64004b1d-16ca-3604-85bb-e845b81ef195 | -5.44533 | -43.50961 | 2025-10-10 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 4999fc7b-f311-308d-a6f0-93134614260a | -5.48221 | -43.06104 | 2025-10-10 00:35:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 8c743bc2-994c-39fa-8322-9df36eae4afb | -7.41114 | -45.93276 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d5636928-cab7-3e87-9cca-7833bc6417b2 | -8.20787 | -43.35835 | 2025-10-10 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 2fcfb16e-ef98-3e64-889a-b3dfcef27605 | -7.39941 | -45.9227 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6fef79b8-a108-3e3b-aeb6-35c1b7ac8ffc | -6.82191 | -42.81651 | 2025-10-10 00:35:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 501e3752-242e-3285-aab7-58d615ff11a0 | -8.90814 | -46.01278 | 2025-10-10 00:35:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c45f74f9-95c8-3c8a-9852-e329c8ebe458 | -5.45666 | -43.51347 | 2025-10-10 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 743b73ef-39ee-326b-898f-ae47e7300c42 | -5.28052 | -46.49186 | 2025-10-10 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c38041ee-9f8f-3b21-b20e-fffef2225296 | -6.46008 | -44.5701 | 2025-10-10 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8235d2b0-8f28-36bc-ae3e-356971c6bed4 | -2.49562 | -47.57344 | 2025-10-10 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c758bdb5-8220-3f3c-bd60-4fa132f10e3b | -5.4833 | -43.0756 | 2025-10-10 00:35:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 3b336f1d-6b8b-3619-966c-914f59173c4a | -8.13842 | -47.38984 | 2025-10-10 00:35:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a547c8f8-01fe-34c4-b643-65fcf10be6aa | -3.83878 | -49.26299 | 2025-10-10 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7736e4b3-30f7-3638-8f07-e06eb3266db2 | -4.50643 | -50.21875 | 2025-10-10 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1cabada1-81bd-3af1-a477-33aa022ee2fb | -8.49716 | -46.1519 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5d9afa35-efab-3b72-bf3a-2850f5661ae9 | -5.45783 | -43.50753 | 2025-10-10 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 07865deb-c2c6-3715-94e2-652b0e54599c | -3.56984 | -43.52157 | 2025-10-10 00:35:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 42523b7d-0dcb-3db2-a7ee-6cfa80656906 | -7.63239 | -46.81827 | 2025-10-10 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 408ab105-6e5d-3226-9c3e-5fd42e9aaac5 | -8.20513 | -43.34075 | 2025-10-10 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.8 |
| d018352e-3bb5-3f99-8d79-de1c75769d79 | -3.79521 | -51.14626 | 2025-10-10 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2af589ad-8cb3-34df-9106-786570702f22 | -3.39 | -50.14437 | 2025-10-10 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7369f9ac-b334-3336-b603-518153b0f1cd | -8.17132 | -43.31592 | 2025-10-10 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| dcbcd05e-74cf-3c39-908a-b4c126d8c8ee | -3.38879 | -50.1356 | 2025-10-10 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0b3f9467-6a35-3fb8-8229-a4f079e99e8a | -7.41946 | -45.91965 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| ef74c3f6-8a12-3832-ab96-75e975476b1f | -4.82427 | -44.33996 | 2025-10-10 00:35:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| cf82fc2d-e903-3d31-a593-e7842ebcc439 | -5.64476 | -45.97274 | 2025-10-10 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |


[Clique aqui para ver as próximas entradas](README6.md)
