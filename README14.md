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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9859a448-41cd-385e-bb3c-4232d17aadb4 | -7.0797 | -59.2157 | 2026-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 98c9dd74-24f5-3453-b8b1-580eb1a8d485 | -10.7598 | -54.0179 | 2026-08-26 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 730a44ba-6896-33bf-bd05-7d89889ef50a | -7.5104 | -61.3832 | 2026-08-26 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 152.1 |
| dba82781-1984-35fa-a087-9bb045a48027 | -6.6595 | -58.498 | 2026-08-26 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 59965310-98b1-3d70-bf63-26f7ee367c4d | -6.6226 | -58.4995 | 2026-08-26 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| afbdf246-ba6f-3405-b59a-ee2d6772c6d8 | -9.6024 | -55.1078 | 2026-08-26 03:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 850236bd-bfd5-3f92-b95a-54c04d23a438 | -20.51804 | -44.73146 | 2026-08-26 03:51:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| f68686e2-02b8-3a03-8c61-2c5ef1cb1d3c | -18.64726 | -47.29273 | 2026-08-26 03:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c71b7175-2f22-36ad-8f5b-127d0ea702cb | -20.25124 | -46.32759 | 2026-08-26 03:51:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 14233b91-6cad-3ac1-b1d5-f6fe3e95488d | -18.64587 | -47.29459 | 2026-08-26 03:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5fc71b1-2599-3ebc-a6a6-929d19d3489e | -18.65151 | -47.29604 | 2026-08-26 03:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7ba42ae-0104-3aa1-9321-bdce539f44f2 | -18.64824 | -47.28835 | 2026-08-26 03:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5c6baaf-3788-3aa4-a2a7-18f69b091b04 | -20.5201 | -44.72758 | 2026-08-26 03:51:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 4048e164-a5b4-3ef8-af0a-98b1d183a6e5 | -20.24605 | -46.32649 | 2026-08-26 03:51:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fe9b0e8-b732-3b6b-b31f-33bb5de7d6dd | -20.52363 | -44.7341 | 2026-08-26 03:51:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 027ad44d-f739-3370-92f2-3ebf7c56ede2 | -18.69798 | -46.59906 | 2026-08-26 03:51:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4b3f707-53fe-3b71-91cf-e00eb73de7e2 | -18.65288 | -47.29421 | 2026-08-26 03:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7aac211c-b6cc-3cbf-87d4-5afefbe1ebb1 | -18.69816 | -46.59577 | 2026-08-26 03:51:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2335709f-fdf7-31a5-a915-801c3fbf5ebb | -18.69741 | -46.59932 | 2026-08-26 03:51:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b16805a-f5ba-3f2a-bbde-223e7471b92f | -18.64683 | -47.29013 | 2026-08-26 03:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a2552dd-3b24-3dac-ad81-f203e3cf6a7d | -18.65243 | -47.29173 | 2026-08-26 03:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34ea4b86-f073-3253-88d3-334930f1b86a | -20.51897 | -44.73308 | 2026-08-26 03:51:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 7a720f7c-31d4-37bc-ad24-6bdc54f5db82 | -18.69875 | -46.59552 | 2026-08-26 03:51:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d242ed3-637b-3d8d-93de-d6bd53079f64 | -7.5289 | -61.3825 | 2026-08-26 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 129.3 |
| e1224b83-71b7-37c8-9222-322d1b3ac09a | 1.4917 | -55.9837 | 2026-08-26 04:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 30ed3cbe-0a49-372a-9b51-b6b4062f56d5 | 1.4734 | -55.9642 | 2026-08-26 04:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 2c99e3c6-1644-3950-90b9-a52f3c0131f2 | -6.6226 | -58.4995 | 2026-08-26 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 33328a4e-9d20-3380-9c53-ff8a82bd289b | -6.6595 | -58.498 | 2026-08-26 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 90351a07-86b5-33ee-9872-31b07c508cf5 | -6.641 | -58.4987 | 2026-08-26 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| de59bda0-4004-37fa-b617-3b5ad467a076 | -10.7598 | -54.0179 | 2026-08-26 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 6a8197db-3d6f-3dd2-a10b-632863a0d553 | -6.6409 | -58.5181 | 2026-08-26 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 71dc986d-2220-3a3c-905b-13d2835fa530 | -7.0613 | -59.2165 | 2026-08-26 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 774a5465-8d24-3ba3-a756-bce7cd2cbc90 | 1.4734 | -55.9839 | 2026-08-26 04:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 30e2b20b-b6dd-36d4-a213-37fa81140aaa | -7.0797 | -59.2157 | 2026-08-26 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 26217e47-8e29-3426-96a9-84c5a6269d0a | -10.7596 | -54.0384 | 2026-08-26 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 9749547d-8a39-3be5-9aeb-0c99614355e8 | -9.6024 | -55.1078 | 2026-08-26 04:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 1783199b-bcae-3fd9-b8a5-bc2d05f1a07b | -7.5104 | -61.3832 | 2026-08-26 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 139.7 |
| c8c56a6d-7044-3e9c-b898-56c55b740f14 | -7.5288 | -61.4015 | 2026-08-26 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| fadedc38-bac5-33be-a4ae-8439db441d6f | -6.2676 | -53.3768 | 2026-08-26 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9537d16e-5abf-3e7c-80de-f93c036954e0 | -10.3727 | -45.0537 | 2026-08-26 04:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 82f99784-ee2a-3fbb-ae9e-8a4c97f938c0 | -5.74197 | -43.27519 | 2026-08-26 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0709d6b1-ec6a-3847-9c97-4245889ae352 | -6.4419 | -41.54796 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2ac164d5-3836-3c95-9664-12fc683ca45e | -2.88674 | -48.8042 | 2026-08-26 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d0c13dd-ca39-3325-a90e-6bfab433dda4 | -5.97124 | -44.06435 | 2026-08-26 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32ec2112-4a36-376f-a0d8-d429a1ab8e32 | -3.5353 | -48.18779 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0a63f1e9-e8ba-329e-bcbe-f76d8f634e08 | -3.53117 | -48.18075 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3954bec3-bd99-306a-9d3b-108061b5d509 | -5.73763 | -43.27882 | 2026-08-26 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd05b030-d723-3416-bc07-471672291c6c | -4.94531 | -43.19656 | 2026-08-26 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d14c1a5-9b89-39b1-8902-9d2231eb98ca | -3.54207 | -48.17923 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dc06d66b-2191-35c4-8e6f-81b8d9e22c54 | -5.65882 | -46.95086 | 2026-08-26 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29b800db-8bd5-352a-b9bd-0600bea6b1be | -3.53064 | -48.18386 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d01b5bea-36cc-3d47-8018-b73362a17760 | -3.65561 | -39.86123 | 2026-08-26 04:06:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2de94ea5-ab78-3bac-89a3-e900fa7b0fc6 | -5.60069 | -45.65526 | 2026-08-26 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 200c50be-24be-3bde-82cb-8e10f95947ef | -3.85559 | -40.97199 | 2026-08-26 04:06:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d91d19a-b46d-3787-801e-8c7147f99acc | -4.94897 | -43.19715 | 2026-08-26 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7958b147-01e5-30d3-a68d-787909f96620 | -4.5586 | -49.51932 | 2026-08-26 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 510a29b7-35bd-3096-9283-7e2a1d6051f2 | -4.463 | -38.51056 | 2026-08-26 04:06:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3b7bbd4-1114-3681-adda-69ed12c91f0f | -6.91735 | -41.12191 | 2026-08-26 04:06:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5dd2e723-a60f-3543-b390-8a58ac801d82 | -2.04591 | -48.04326 | 2026-08-26 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ad0e11a1-38ff-3bf2-a9d6-c7798aee944f | -4.16928 | -42.4396 | 2026-08-26 04:06:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 73c8e54b-6ae3-33ef-a4a2-b28bb4e3de0c | -4.87315 | -44.30646 | 2026-08-26 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf5b717d-3dda-3930-bcf0-7a39e3bf889c | -6.42805 | -43.86158 | 2026-08-26 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a59c470-90c1-306b-bc17-0fdebf614fb5 | -5.51599 | -44.11845 | 2026-08-26 04:06:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8019b9ca-4f1c-30dd-aaf7-92cb7785dfcf | -5.51217 | -44.11782 | 2026-08-26 04:06:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01d2462d-d710-3a60-9515-e43650d50567 | -6.12579 | -44.06781 | 2026-08-26 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2db420cb-b44a-35a7-95f6-5cd49e07286e | -6.37003 | -43.28086 | 2026-08-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c85b640-b0a5-3f1c-9c34-13bb760a68d3 | -3.41074 | -39.2831 | 2026-08-26 04:06:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc7d01ab-6726-3464-9c4e-48a265ffb123 | -6.91459 | -41.11786 | 2026-08-26 04:06:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 08c7200b-273d-3863-9e18-45de614e9905 | -5.34571 | -45.16078 | 2026-08-26 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f7f0810c-5431-3085-8584-fd75f000e2f6 | -3.58723 | -50.68275 | 2026-08-26 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 98ed908d-25a0-3b5b-8d40-89457b259bc7 | -6.91515 | -41.11434 | 2026-08-26 04:06:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8b556de4-4111-3f6f-9880-ff667b8310c8 | -3.51103 | -48.03648 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77347c65-fbd6-3926-9137-520b8f0205ab | -5.63846 | -43.61007 | 2026-08-26 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f5db486-3309-3367-947a-306ba47df0e7 | -5.34511 | -45.1644 | 2026-08-26 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 29b6b1b1-f198-31f7-b6c0-7049f9e8e9f6 | -5.63275 | -44.94066 | 2026-08-26 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8c88c10-fbef-342f-adaa-d1e52ea0e123 | -3.5105 | -48.0397 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6aae97eb-6b89-3453-a2eb-a17d037f8cbb | -5.31469 | -37.33257 | 2026-08-26 04:06:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9720b29f-a977-3cd6-9778-579f81fb7e9e | -5.62956 | -44.83617 | 2026-08-26 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87396f46-c9a2-30ff-be21-3f376defd1d7 | -6.44527 | -41.5485 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 15810990-6795-3fcb-9cb6-6215b51bc818 | -2.79657 | -49.57942 | 2026-08-26 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee10e429-cb91-37f6-af34-f3ae41908da4 | -2.94234 | -40.18164 | 2026-08-26 04:06:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a410f1c-41dd-3d27-a934-5f4683d32c08 | -6.45802 | -43.091 | 2026-08-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 739ade86-cd36-30c1-a1d5-dcbedceb2a78 | -4.80539 | -45.76783 | 2026-08-26 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f189896f-3407-394d-b7e9-2d493207f041 | -5.77163 | -46.11163 | 2026-08-26 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f24536c7-56df-36ec-bb73-5376caed263f | -3.51615 | -48.0374 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fe384fb-4057-3812-95cf-f2cf2c7f7bc6 | -3.51153 | -48.03349 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa029bb8-960e-33cc-bc98-038f909d52c0 | -6.41419 | -42.78425 | 2026-08-26 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ffa11c16-8825-30c2-a398-32d4432fa991 | -6.45459 | -41.56454 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4a38bac-918e-32a0-95f1-e1c0e53f5477 | -5.92174 | -43.63788 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4441ab6-67eb-3476-901f-1dd33ffb4c39 | -2.88734 | -48.80068 | 2026-08-26 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da5eca6e-fb09-34cd-9343-28f0f10d8fcf | -5.14986 | -43.18284 | 2026-08-26 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 027ab2a7-e0f9-376d-bda8-c53696efa0f8 | -3.54155 | -48.18235 | 2026-08-26 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e38c7362-a8e9-3533-b4f9-018927afd663 | -2.98371 | -49.27564 | 2026-08-26 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 248ce441-c9ec-3aba-83e0-b4695fd27612 | -6.36936 | -43.28501 | 2026-08-26 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19ec19ef-92ca-387d-b3da-a6971aec018a | -4.84748 | -44.29209 | 2026-08-26 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39030db5-049f-3aa5-b3ab-f1185c7d04bf | -2.79523 | -49.58745 | 2026-08-26 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5078840e-0713-3ac4-995e-2317738be41a | -6.44683 | -41.54847 | 2026-08-26 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6ced2122-284e-3afb-80ef-961161708fe8 | -6.61144 | -42.54724 | 2026-08-26 04:06:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dac4c571-974d-3817-afa4-6a39afaf53a5 | -6.2437 | -44.79664 | 2026-08-26 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff6566e0-4c5e-37db-8dcc-ad33a7aef3c2 | -6.37787 | -44.37384 | 2026-08-26 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
