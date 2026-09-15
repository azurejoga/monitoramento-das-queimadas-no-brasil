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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5295047b-1eaa-36a8-b6c6-d392e8672ff9 | -10.2926 | -45.3161 | 2026-09-15 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 5e4d0096-d954-3a17-9dad-62fbb3e1f91c | -9.3567 | -50.1796 | 2026-09-15 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| f6ffed88-dbe8-3faa-b10a-1f8615ea503f | -1.2268 | -49.1899 | 2026-09-15 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5a22b1f5-7d99-3c4b-bdf2-4aed15e15770 | -9.1337 | -65.8253 | 2026-09-15 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 4d984888-0553-3199-a3e1-5b8341f1a6f8 | -15.5974 | -53.8426 | 2026-09-15 16:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 620bc5ad-a350-3c57-9f42-9b1bb844e226 | -3.2734 | -60.9327 | 2026-09-15 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 986670ec-45f8-3afe-916f-50db5372d11c | -2.6601 | -57.5507 | 2026-09-15 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| fda92a06-4362-351e-9c38-3cd9257c9b97 | 1.3817 | -56.1029 | 2026-09-15 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 877fb277-eca3-3705-bddb-2542ed58202b | -2.6603 | -57.4924 | 2026-09-15 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ef1f05f4-f21d-3ecd-b4ac-5387d8c4fefc | -9.3575 | -50.1156 | 2026-09-15 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| a31f987a-bc82-3ce3-9d7c-d85f697e386d | -8.37 | -54.73 | 2026-09-15 16:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa4b79c-723b-3b77-81d8-0b51344b6ab4 | -14.6 | -41.69 | 2026-09-15 16:15:00 | MSG-03 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3fce38a2-ecf1-3bb7-9237-cbb939bdfd43 | -15.51 | -43.87 | 2026-09-15 16:15:00 | MSG-03 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9d07bf18-b726-3c90-81e6-ddb3156e9b2f | -9.3572 | -50.137 | 2026-09-15 16:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 7e19b3a0-c802-3086-a37c-2df4fbb1e21a | -3.9708 | -60.0067 | 2026-09-15 16:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| f4c86430-a2d3-3c6f-99c4-5df85127c98d | -15.5974 | -53.8426 | 2026-09-15 16:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| e06de5c4-bef6-3e80-aef2-1509aef995ae | -9.7133 | -64.9637 | 2026-09-15 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a172d7f2-ccd1-3333-aa16-03e334aea2b4 | -8.638 | -44.4567 | 2026-09-15 16:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 47832f16-34b6-3555-b8b2-3ceb165ce215 | -2.6603 | -57.4924 | 2026-09-15 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 74df7f6e-3d65-323f-8869-2bdef41eb961 | -2.6968 | -57.5112 | 2026-09-15 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 84775f5b-bc34-3839-9d4f-27767e4fe265 | -2.9723 | -57.214 | 2026-09-15 16:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 5c776222-b625-35b9-9a48-8127ae4783eb | -12.1265 | -44.199 | 2026-09-15 16:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 1d0a0d48-881d-3e94-9a4b-920944ea816b | 1.3817 | -56.1029 | 2026-09-15 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d67000cc-be6c-3977-9172-fb337cccb053 | -10.312 | -45.2907 | 2026-09-15 16:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 343f29ad-d14a-38c0-be44-eb5842e67b16 | -9.7687 | -46.1067 | 2026-09-15 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| d9d56da6-8492-3ebc-bb7a-2382386c1a8a | -8.638 | -44.4567 | 2026-09-15 16:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 247.3 |
| f30a94c3-ff0e-3b08-ac17-bb77928937e1 | -9.376 | -50.1352 | 2026-09-15 16:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 966c62fd-5f8f-3869-9d3e-c3f692000c8e | -9.7687 | -46.1067 | 2026-09-15 16:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| a0d45602-e9e9-353b-aa0f-5ee23e261890 | -1.2268 | -49.1899 | 2026-09-15 16:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 4a6be3ff-12e7-3f9b-b37b-fdaac989886e | -2.6968 | -57.5112 | 2026-09-15 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| b88f4e7d-795a-33a4-a5c5-329782f75696 | -2.6603 | -57.4924 | 2026-09-15 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 586c5cb4-e7a6-3050-af3f-5a0d10a413d8 | -8.638 | -44.4567 | 2026-09-15 16:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 204.2 |
| e212b273-e1a3-3991-97dd-a1f2a238be0a | -1.2268 | -49.1899 | 2026-09-15 16:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| b8103324-e67e-39e9-b006-b4d8c3fe4367 | -9.376 | -50.1352 | 2026-09-15 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 02f7ce6a-a5a8-3463-8e41-91c09edde139 | -9.7687 | -46.1067 | 2026-09-15 16:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 8726d98d-3624-350f-9f3d-1e60edc8019e | -2.6968 | -57.5112 | 2026-09-15 16:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| fa3dd92b-c7c3-37fc-b680-1afa0bfb10f8 | -1.2268 | -49.1899 | 2026-09-15 16:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e1b06a76-b162-398f-8647-480b9be25df2 | -9.376 | -50.1352 | 2026-09-15 16:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| b0737e3b-8c62-32bb-a282-b5b5d1eae135 | -8.638 | -44.4567 | 2026-09-15 16:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 20d9c6d6-08ed-3b4a-bc1e-ad31cfa1c12e | -12.1265 | -44.199 | 2026-09-15 16:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| a85c97dd-6bdf-3d18-ab18-8119f6a82796 | -9.7687 | -46.1067 | 2026-09-15 16:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| fd39ff76-f569-39a6-af78-f004fbd32392 | -1.2268 | -49.1899 | 2026-09-15 17:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 00d1600a-82a5-376b-9d8e-275be818f39b | -2.6968 | -57.5112 | 2026-09-15 17:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 00258110-84f8-301a-8563-f808354be8f6 | -8.638 | -44.4567 | 2026-09-15 17:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 64cdb67a-b9aa-3657-98e6-12e659d524f2 | 4.2971 | -60.9501 | 2026-09-15 17:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 2026a076-7a0b-3f74-85dd-35cd34e8b6a1 | -8.638 | -44.4567 | 2026-09-15 17:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 980d593b-781a-35eb-9077-5d8717c01d2b | -3.7311 | -60.6018 | 2026-09-15 17:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 02510ef6-5400-3490-a129-d18a17a2e297 | -1.2268 | -49.1899 | 2026-09-15 17:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 7c6989fe-a033-384a-8891-0889ca380e05 | -5.55 | -44.33 | 2026-09-15 17:15:00 | MSG-03 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2e533a1-8d33-330a-884e-ed5d0de7467d | -4.66 | -42.07 | 2026-09-15 17:15:00 | MSG-03 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 876244c8-3d68-330f-9edb-4b06279f4828 | -14.57 | -41.73 | 2026-09-15 17:15:00 | MSG-03 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 628d1099-59a8-3b91-8ffa-753285c1fc4d | -5.58 | -44.33 | 2026-09-15 17:15:00 | MSG-03 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85e4b9c6-a652-362b-8a8b-209ed8f2c29f | -8.63 | -44.53 | 2026-09-15 17:15:00 | MSG-03 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 61862cc9-1abe-3740-924b-db15287e2ef1 | -14.99 | -40.98 | 2026-09-15 17:15:00 | MSG-03 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7bfffede-84a9-34cb-bb9e-ccbe4fbf7b9e | -5.55 | -44.28 | 2026-09-15 17:15:00 | MSG-03 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99b69c52-039b-310c-a2fd-5d388babe81b | -15.02 | -40.98 | 2026-09-15 17:15:00 | MSG-03 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7441b80-7a4b-3bec-a9ad-856fea98d99d | -9.7687 | -46.1067 | 2026-09-15 17:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 213.4 |
| bc4541b7-ba25-3736-a07d-568fd1d5dc3f | -3.4462 | -57.9812 | 2026-09-15 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2f4827f8-5292-35b0-a523-90005f64ee83 | -12.6821 | -54.7174 | 2026-09-15 17:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c6ee4dc9-06be-3a8c-8000-e0ef31ad4957 | 4.2971 | -60.9501 | 2026-09-15 17:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 75.7 |
| d20b0a3b-f48c-36d5-ba2e-9e2b8ca6f717 | -3.4279 | -57.9816 | 2026-09-15 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ab0f42e3-310d-3186-a11a-a57bb1333db0 | -1.3007 | -49.1464 | 2026-09-15 17:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| ba5efc39-f338-31bc-8359-c9e019798aa0 | -3.4461 | -58.0005 | 2026-09-15 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 577d77d8-0b07-37f0-9421-f3f9411ac5f0 | -3.4278 | -58.0009 | 2026-09-15 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f9549026-8c69-3a3f-a75e-4c4928b29681 | -8.638 | -44.4567 | 2026-09-15 17:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 15f46192-0481-3dff-9b24-3b5785a98705 | -12.6636 | -54.6782 | 2026-09-15 17:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 8bd6852f-948e-3376-a5ef-f0e1fc4fd135 | -8.638 | -44.4567 | 2026-09-15 17:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 301.9 |
| 9f193feb-cac5-363b-b792-ba5a32e0969a | 1.2243 | -50.7475 | 2026-09-15 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a9fe858d-cd69-3549-ba74-cf3ecce285d0 | -3.4278 | -58.0009 | 2026-09-15 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 3530c312-d462-33ac-91eb-7a1e1c4a3e2f | -9.6104 | -46.5967 | 2026-09-15 17:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3ea25ae3-432f-3771-85d2-8fc0d0ba3451 | -3.4461 | -58.0005 | 2026-09-15 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 6eff54d4-2e53-3150-9ba0-816cb8163014 | -3.4462 | -57.9812 | 2026-09-15 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 3d86836d-1cbd-3681-845b-85b08f21f847 | -9.7687 | -46.1067 | 2026-09-15 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 243.2 |
| 73f6e720-9818-3582-969e-7e30f4bffd4b | -2.6603 | -57.4924 | 2026-09-15 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b3e6e9e3-66fd-3678-911a-4d6915a2011f | -3.4279 | -57.9816 | 2026-09-15 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0749a5d3-b291-35af-bbc6-a22571bd192b | -1.3007 | -49.1464 | 2026-09-15 17:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 82c7bd6a-7a62-351e-a2cc-1b77461fd7d7 | -8.6191 | -44.4588 | 2026-09-15 17:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 5638aa64-c539-3757-9d3f-a19c0971bcd8 | -11.3638 | -43.9642 | 2026-09-15 17:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 89954f8b-e910-394c-864a-1d64a02663a4 | -12.6826 | -54.6763 | 2026-09-15 17:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| de2b8c69-d74f-30ea-80f9-7e859cce1fb2 | -2.6785 | -57.531 | 2026-09-15 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c5c8dea1-4f1c-38fb-88dd-3974abeee8a1 | -7.0823 | -42.1107 | 2026-09-15 17:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 84ed8816-7543-3a62-b760-162ae5198989 | -3.3137 | -59.4664 | 2026-09-15 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 523edba0-20da-317f-9b00-430d30e18513 | -2.7149 | -57.5886 | 2026-09-15 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| c43013f5-c6d4-3127-a2ab-e65a97e71094 | -8.638 | -44.4567 | 2026-09-15 17:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 88fcfb70-5328-3c90-8d4c-4fcae5eaaa52 | -3.4462 | -57.9812 | 2026-09-15 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 143ba8ea-66f8-3cbb-b597-799fa9656744 | -11.3642 | -43.9407 | 2026-09-15 17:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 8dc4df75-a693-3704-a564-4b491761b492 | -7.6193 | -46.1495 | 2026-09-15 17:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 2b491687-25c1-318d-9a56-8f25413f67e6 | -9.3575 | -50.1156 | 2026-09-15 17:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 89476583-6670-3385-822a-8b89f0e46fad | -15.5588 | -53.8266 | 2026-09-15 17:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 7ccf5f75-d345-3ca2-bc4f-97a800bcaf9f | -15.2859 | -53.9037 | 2026-09-15 17:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 67ef5b6a-116c-3139-aa82-f0e3cefd5fab | -9.3572 | -50.137 | 2026-09-15 17:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 455c6404-a672-36dd-bd7a-df0bc11e2a7e | -3.4003 | -61.3087 | 2026-09-15 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 30b34338-14b6-3abb-b09e-b326f46da59b | -3.4279 | -57.9816 | 2026-09-15 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 340df92c-ea7a-364a-9566-75715e96b1b9 | -9.7687 | -46.1067 | 2026-09-15 17:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 13cc9ba3-b0f8-3eb3-9cb4-b19f970b813e | -3.2954 | -59.4667 | 2026-09-15 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 6f536c1f-3336-3804-8ce0-b647f6ee1162 | -8.8459 | -45.8713 | 2026-09-15 17:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d8b62196-ae9c-3c33-9fa1-1a96154a56d1 | -2.7149 | -57.608 | 2026-09-15 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 1e87c5c2-aef6-33eb-9dd7-649a934e8b32 | -1.3007 | -49.1464 | 2026-09-15 17:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9e8e4795-6cd9-3589-8a07-159a653433f3 | -11.193 | -42.8065 | 2026-09-15 17:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 273.6 |
| defe49c3-1b4d-3836-94e4-2b78df084e4a | -9.6104 | -46.5967 | 2026-09-15 17:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |


[Clique aqui para ver as próximas entradas](README89.md)
