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

## Dados Diários - Página 294

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a410467-f5d5-375e-817b-da4dcf5f97f5 | -2.5903 | -56.1839 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| e542309e-f16e-3e54-a13a-d4804a26af89 | -1.1094 | -54.1802 | 2026-10-09 18:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| afedb639-48e1-3916-b37b-3dc6f7f49eab | -5.246 | -48.4103 | 2026-10-09 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 47e11c0f-75f6-3e7c-b740-e1613895438e | -3.5138 | -49.9395 | 2026-10-09 18:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 26754e7e-266d-346c-ae05-048da8a8ccfd | -3.9121 | -55.8964 | 2026-10-09 18:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 0b09bc81-f064-39db-8f01-10997973f7a4 | -3.2357 | -50.1805 | 2026-10-09 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b9e8be88-7741-3873-b4f2-bc84fc75ac12 | -3.6622 | -59.1717 | 2026-10-09 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 919386d2-cef4-3821-87f7-3cffa0530b4c | -10.5107 | -47.2065 | 2026-10-09 18:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 1ba62ad6-5fe0-304e-b1fb-0c051fcbc1e5 | -15.2535 | -42.3741 | 2026-10-09 18:40:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 466.5 |
| 1821526a-e440-3775-b559-b153689b6608 | -9.9198 | -44.8585 | 2026-10-09 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 425.1 |
| fb7b97f9-7f22-3ceb-a76f-aada08571d5b | -11.8499 | -43.5835 | 2026-10-09 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 273.5 |
| 4a9a9673-2085-39e4-bb2c-14cd7c81468c | -10.4334 | -47.3046 | 2026-10-09 18:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 233.4 |
| d2397ae8-3936-38b7-b7f4-b1308306ee26 | -14.4535 | -43.9359 | 2026-10-09 18:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 370.5 |
| 0894605f-fee7-392f-95f2-4a2dda06f0b7 | -3.3129 | -54.0001 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 4ca53d9b-8305-321a-9f7e-891712fddf83 | -12.3708 | -46.5789 | 2026-10-09 18:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 330.6 |
| 03de1eeb-ccbb-36cb-8480-609d573a9657 | -3.8593 | -51.1208 | 2026-10-09 18:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 87a2920e-edff-3672-a326-afb2b1ccefdb | -3.7561 | -58.4382 | 2026-10-09 18:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| fb11c6c0-a3eb-309a-b960-2b52d96dd18f | -10.4147 | -47.2846 | 2026-10-09 18:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 6594cb7c-5d60-37d6-92cd-d8db5a740cc8 | -3.0007 | -53.9075 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 237.1 |
| 9ca427ac-978d-3f05-b17a-9ffa275b79b6 | -15.4029 | -41.8985 | 2026-10-09 18:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 394.6 |
| 5874e8d5-1ab9-3d9d-b547-307161f11d8b | -9.8828 | -44.794 | 2026-10-09 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 01a3e7e4-26e4-3659-9220-73e2995ec3eb | -18.3335 | -42.3598 | 2026-10-09 18:40:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 137.8 |
| 355b929a-2fa2-31bd-bafc-c06c7e1a6756 | -3.8594 | -51.1 | 2026-10-09 18:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 93951a01-93d4-3a8e-824e-449753ab8fed | -4.7404 | -55.6522 | 2026-10-09 18:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d64e2175-507c-3a13-a494-04daa3036503 | -9.718 | -45.6828 | 2026-10-09 18:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 54289430-cb07-3065-973f-be3921410431 | -14.0662 | -43.8424 | 2026-10-09 18:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 08fb78db-36b6-3e1d-a429-e0905cf98583 | -12.2123 | -44.7457 | 2026-10-09 18:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 48e1e389-b319-32bd-8ff3-7243d02ae1ad | -13.6896 | -49.107 | 2026-10-09 18:40:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 6453cb70-951f-3b30-99fb-aee35d7221aa | -3.2085 | -57.87 | 2026-10-09 18:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ecdc25af-1426-3a8f-93bd-2675a0e6f83c | -9.4496 | -44.5936 | 2026-10-09 18:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| b23df899-ca43-37a9-8f14-59bc8436308a | -2.7335 | -57.4717 | 2026-10-09 18:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d709d4ce-05a4-3cc5-b416-e4df5d057e47 | -10.2488 | -49.6636 | 2026-10-09 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 43137e2f-c93b-3d72-ae3e-04dd252a09e6 | -3.188 | -58.6241 | 2026-10-09 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 10a12319-d9b3-39cc-86bc-ae1f2d2356d1 | -17.4575 | -45.075 | 2026-10-09 18:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 49ebfb44-4860-3fdb-b1ab-a28e41e91550 | -10.491 | -47.2533 | 2026-10-09 18:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 3d53bbf4-e4ba-3f4e-9f9b-8dc4a67fa963 | -14.0667 | -43.8185 | 2026-10-09 18:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| a8b3cdf9-0acb-3066-bb37-92ad7f7cd7a9 | -7.4886 | -42.8295 | 2026-10-09 18:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 145.2 |
| 3b3248f3-c046-32f2-90b1-0ae101d0ff06 | -3.4462 | -57.9812 | 2026-10-09 18:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 854f4aee-6e4a-34ce-925d-e235d457c696 | -8.1878 | -45.7584 | 2026-10-09 18:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3b4e89df-5489-30b2-8264-bc4053d4efb8 | -9.75 | -44.7875 | 2026-10-09 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 2a93b82b-8acd-3fdf-880f-79fe53a6c4c6 | -16.2353 | -44.053 | 2026-10-09 18:40:00 | GOES-19 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 93.3 |
| c82cb30a-e239-31f2-9ee4-3b05b729e751 | -2.9819 | -54.0488 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 5f5af039-5da2-348e-b78a-89033a65866a | -2.5171 | -56.1262 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 9ca8b557-9051-331e-bec6-90dc798ff358 | -12.811 | -44.627 | 2026-10-09 18:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| f2226b20-485c-36be-bb56-49f13bb90286 | -10.2317 | -46.8382 | 2026-10-09 18:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| be688a2a-e0e8-39fd-b26f-8bb9507e2b7d | -8.9308 | -45.1584 | 2026-10-09 18:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 321.4 |
| 6a02cb84-2567-3970-bdb7-19f281bac3aa | -2.4577 | -58.0194 | 2026-10-09 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| f068fc70-8f2c-3a23-800d-c677b5e3ee70 | -2.0577 | -56.8591 | 2026-10-09 18:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| cd16d5b4-ed92-3260-a96c-a2f4856f2dbb | -3.571 | -59.0777 | 2026-10-09 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e69df6c5-ed11-3e3b-bfe1-b44f9fbd6ce3 | -8.9119 | -45.1605 | 2026-10-09 18:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 6bfbf520-4682-3869-9aaf-408ba54427ce | -6.7078 | -47.3783 | 2026-10-09 18:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 36e0bdc8-c3ff-32e4-b7ad-e405d81dc658 | -2.9267 | -54.0702 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4b5c90d8-42bd-3919-b355-0c735a083b0c | -11.014 | -45.4272 | 2026-10-09 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 1fd66c95-70b5-3e1c-880e-b9ae391875ab | -12.193 | -44.7487 | 2026-10-09 18:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b7a741fc-c6aa-385e-a58f-6307bf6bc8df | -2.5492 | -58.0373 | 2026-10-09 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 114.4 |
| d9138dbb-8a50-33cd-8bd5-72faf9e7ab57 | -2.9267 | -54.0501 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 941a1f79-735b-3e07-a4c8-714d68fe4c6a | -2.5721 | -56.1449 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |


