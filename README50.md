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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e0eb69c-9863-37ee-a936-43dd7f75e0e3 | -15.93774 | -48.16423 | 2026-09-15 04:36:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c5c131c-aa53-3f56-9079-26ddfcf5c1e6 | -16.51638 | -47.80156 | 2026-09-15 04:36:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98c1a614-1eb9-321f-ace4-93017a96de65 | -15.60138 | -53.78441 | 2026-09-15 04:36:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efc1d08e-f156-3c87-a16d-f69d822409dc | -15.58457 | -48.83171 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83aa06f4-e5ab-334f-acbf-6aa53e41d6ff | -18.16349 | -51.74945 | 2026-09-15 04:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dab4d801-637b-3f7b-b9e8-52d8942ac70a | -18.16768 | -51.76706 | 2026-09-15 04:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d567d2e2-a6ef-377b-94bc-ee3fda5eed0b | -16.96576 | -43.36755 | 2026-09-15 04:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d93ec87-d4d3-3210-b2d0-b46f54e1fb70 | -15.53937 | -48.81669 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6e96c26-433d-34e1-b543-9b42265e0dbc | -18.16001 | -51.76976 | 2026-09-15 04:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a13d0d3f-bf4c-3dd4-9684-bb392b534221 | -17.35344 | -47.17161 | 2026-09-15 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcc2c9be-c292-3706-b7f0-5eea11f72ac1 | -18.16071 | -51.7657 | 2026-09-15 04:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b01aab76-86b8-3292-b7bc-ae775b48ec42 | -15.57702 | -48.79374 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38424e43-e4bc-3dea-b964-ce0cffa382c0 | -18.13595 | -42.85308 | 2026-09-15 04:36:00 | NOAA-20 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e2263754-7583-37a6-813b-86fce7addddc | -17.45907 | -43.64092 | 2026-09-15 04:36:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b3a4283-41f7-3a64-80cc-7527785643db | -15.36031 | -52.99409 | 2026-09-15 04:36:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3ee2041-7528-365e-889b-f8185f0dbcb4 | -15.55375 | -48.8118 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b34d862-d3f1-37be-ab84-5c3b30fef634 | -17.31923 | -46.9092 | 2026-09-15 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8369d8b-86b2-3523-b726-c6d50f3b556f | -15.5405 | -48.80956 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a8c76a5-690a-3f22-88f4-bb04fc0fe992 | -18.86945 | -42.00983 | 2026-09-15 04:36:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd85b864-5e98-3a99-9a2f-9448ec3937dd | -15.55762 | -48.5745 | 2026-09-15 04:36:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac19407d-ab53-31d6-9538-504a6f6f1dee | -15.55442 | -48.78626 | 2026-09-15 04:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cfaf93d-fe02-37fb-a5cb-dbcbf4815bf6 | -15.58514 | -48.82814 | 2026-09-15 04:36:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ffb69d6-21bb-31da-be02-a9c15d5319b0 | -16.47766 | -43.42322 | 2026-09-15 04:36:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 473f21fc-ce72-30aa-ad19-0fbf2060a7e9 | -29.15332 | -55.87874 | 2026-09-15 04:40:00 | NOAA-20 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 62173a61-43cd-3874-be12-91f3dc893493 | -31.31872 | -54.15944 | 2026-09-15 04:40:00 | NOAA-20 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 631439cf-9f2d-3097-81db-7a8b77157a90 | 4.40816 | -60.4189 | 2026-09-15 05:14:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4604bb28-6bd9-393f-bbe3-4e6cc10a6805 | 4.29421 | -60.94395 | 2026-09-15 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 828f8039-6cd6-37aa-9483-67b9cd8eda41 | 4.29488 | -60.94847 | 2026-09-15 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 81b7622b-c847-36dc-81ae-6b06139e2afc | 4.29247 | -60.95861 | 2026-09-15 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3f1a446-3ada-34d1-ab29-e1331cb068ae | 4.49608 | -61.17347 | 2026-09-15 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 42bb2171-36ef-3fe4-bb8d-2d8beb9515f5 | 4.30883 | -60.23719 | 2026-09-15 05:14:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f1992bd-c3c1-3b7a-af96-fde1b7aa974c | 4.36354 | -60.3253 | 2026-09-15 05:14:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 704b4d7b-912f-36df-af5c-8944c56d7b92 | 4.38339 | -59.76677 | 2026-09-15 05:14:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 982052c4-4eec-3da7-a716-9b5381430102 | 4.29555 | -60.95302 | 2026-09-15 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bddbb779-4f95-3db9-ac20-47d70dec31bf | 4.29179 | -60.95403 | 2026-09-15 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73e1d855-04c4-3d43-9177-444b96b6451e | -3.33202 | -58.12454 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db730954-c307-3fae-b55e-b33f5fae1807 | -2.65475 | -57.51686 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| afecf9e1-3409-3f53-96a2-781076139282 | -3.42167 | -58.22636 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e70691b7-3e2c-3739-842a-ace0f9fd4ceb | -2.7066 | -57.6207 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46c47c6f-b35d-3cf5-bb3d-86c224cb72c8 | -3.07422 | -51.07755 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 26f92634-7ad1-36d1-ace2-f8c0e7add4eb | -3.11161 | -61.09573 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67284849-a0fd-37cc-9033-f586f4547244 | -2.89246 | -50.4358 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3a975f64-8e11-3f7b-ac36-b14225f94e9a | -1.68501 | -55.90174 | 2026-09-15 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c5e401a1-0700-3e24-85e5-c20128eddef7 | -3.17741 | -61.11396 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d23339c4-3e14-3b11-905c-8c30f1b722ce | -2.88968 | -50.43601 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a363293a-2520-3589-8f92-195c5df5a8fb | -3.37647 | -50.39636 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fb804fd-7c2a-38c3-8efe-3dffa3b96861 | -1.87436 | -60.04457 | 2026-09-15 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e19b56ef-9570-30ec-9c48-faa35af3f531 | -2.94941 | -50.40577 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b426bbe-fbd3-34af-9bcf-abc2ea1b7d34 | -3.12516 | -59.03669 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c895144b-8291-3bbc-83a1-19ee7592880c | -2.77868 | -58.13972 | 2026-09-15 05:16:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80b55842-9cdb-3440-a632-ad18770074bf | -2.89895 | -56.94925 | 2026-09-15 05:16:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89a7421e-6596-3136-8030-b81a64187fa2 | -2.70657 | -60.01851 | 2026-09-15 05:16:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 233acf71-29ac-31ec-b40f-a97bd910ab7e | -3.45533 | -58.40459 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13342d9b-0c3f-3561-b4b2-a4e7c23ea316 | -4.38565 | -55.2041 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1995152b-45df-3bd9-85e9-3b84f81661cb | -2.94531 | -50.39952 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e4e1f87-1e6f-3044-8311-0edbe52bfe1d | -2.91908 | -50.40676 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 336c64ab-4113-3f76-8a67-3699e128d5a0 | -3.42221 | -58.22293 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08ffd3fe-4ebe-3d0f-aec9-62ab0b289c4e | -3.83678 | -55.86256 | 2026-09-15 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e70331c-41f4-3f0d-ae1c-9b0ac74a6ce4 | -3.35212 | -59.82349 | 2026-09-15 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 955f2890-06bf-346b-a0e1-f60395ed6a03 | -2.78595 | -51.37112 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 315af780-35cc-3482-abcf-c39d84fa0d80 | -4.38262 | -55.19933 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7528b63c-f9e9-31b0-b92e-977f20cb815d | -2.64715 | -59.37263 | 2026-09-15 05:16:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7f9cc62-3a2f-35f0-b2d4-2e7d8b38905b | -3.19356 | -61.12782 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 614f57c3-7454-3e66-a595-8848f9f23866 | -3.84953 | -51.75961 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 262798dc-c3be-3f55-88e5-9e671ad2170d | -2.97458 | -54.16117 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4194e28-425b-31a1-ad21-ca2cedfd684b | -3.26453 | -54.52123 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adc58f8c-beb0-329c-a9f7-5eb11ce91739 | -2.78092 | -58.14709 | 2026-09-15 05:16:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b490da1d-a879-31a1-a778-94d3a58b2e21 | -2.89584 | -50.4138 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c40f63b0-5023-33ac-8159-3fb82c81aef8 | -4.36232 | -47.78101 | 2026-09-15 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4fdaed8b-d875-3615-bb14-f8c7a5468753 | -2.89416 | -50.42478 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f06b8e95-724e-3859-b639-93c216a88494 | -3.54465 | -53.99065 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7dd367e0-7a9c-3e36-9575-f544a03b3bc2 | -3.3386 | -53.26805 | 2026-09-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6914af86-ff50-3d38-910f-5be8884d6b19 | -2.95923 | -50.40737 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc32c079-dc52-36b8-a516-17c81136b61c | -2.93055 | -50.39723 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2677ced-e518-31c2-8902-8346f5bfcddb | -4.51783 | -54.97214 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 007e9265-8e90-39d4-9cd1-da05bc648506 | -3.33532 | -58.12505 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ec5d0cd-dca3-3f72-95a4-6c869973ed89 | -2.82934 | -49.23033 | 2026-09-15 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 693d5902-2dc2-37c6-8c4c-d82ebe65fd03 | -3.54392 | -53.98898 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 824bb353-09f5-3346-a619-07b633db4eab | -1.22231 | -54.12957 | 2026-09-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66e4e63b-59ab-32d3-a9f9-8d8bc641efc4 | -2.32399 | -47.20104 | 2026-09-15 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1f4cd46-88ad-324a-aa71-5e60c9a6a2a0 | -2.91819 | -54.172 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f217efa5-043b-3057-ab75-1299ed529ce2 | -2.88925 | -50.42403 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 81658b8c-d8df-396b-ab92-ece3ac5f63d4 | -2.91013 | -50.43346 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c6219b7c-0834-30ee-b9f3-e680a172d3cf | -1.23181 | -54.09343 | 2026-09-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e85fae9-c11f-3567-9bf6-0bec1a31b256 | 2.69723 | -60.30136 | 2026-09-15 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77e56d74-a36b-3c36-b0b3-42d4c3ac26bc | -2.91416 | -50.406 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3682fc8e-a128-3dcc-ac7e-b237f8d45667 | -2.90844 | -50.41074 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 411a94f6-c648-390a-a030-cdc1a46b05f6 | -3.25634 | -54.52462 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 487f5315-1813-3b56-bb21-321025ee1072 | -3.17243 | -58.64856 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbf1697b-004e-3de3-9423-7a3990144c7d | -2.91665 | -50.42327 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 114efaa2-eacd-3f92-a70b-bdbc930e81c2 | -3.17326 | -61.11737 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0849c8d7-8cd6-3c97-992f-a70b455f164a | -3.25714 | -54.28793 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5256520f-7619-3c89-acef-5b5470c04366 | -1.2301 | -54.13757 | 2026-09-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac955f86-9c42-3738-95e1-812dd6779380 | -2.70767 | -57.61377 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d5706682-a549-3c59-82cd-de350c76637a | -2.71153 | -57.61082 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1a3b81a1-e2ab-3d8a-ad03-e1d5199883e7 | -3.54854 | -53.99122 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 8fff80c5-b9d7-36df-b1d4-3e7f3f6e2c79 | -3.16973 | -61.11682 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 053a19fa-4b7a-3044-81ce-338d70ec4573 | -3.48446 | -59.47819 | 2026-09-15 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25867b0b-8da8-3cd0-b240-334f08f86326 | -2.82983 | -49.22701 | 2026-09-15 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e3ce094b-7f6e-31af-aeaf-920c05f7f21a | -2.6971 | -57.59441 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README51.md)
