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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b437dcb-4484-30ec-8079-861e732b6d89 | -10.61339 | -60.48781 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc0a5747-4286-32b5-9818-c6786ad33588 | -11.38069 | -55.15913 | 2026-10-10 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8270a827-5a04-30f3-80cf-66ccb956638f | -14.45833 | -43.95396 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b2b4afb-cc29-378d-a1e1-d4c56b9b5b78 | -13.91958 | -47.84595 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b899fdea-0c93-322b-8a39-bfa4e682137a | -8.24639 | -54.7239 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23085bfd-1913-363c-8e75-52a80c2bcbc1 | -13.15017 | -54.35811 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bd26221-84da-3766-95e8-a8526386ff32 | -11.38731 | -55.1602 | 2026-10-10 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 473b6e47-6bf6-3919-ab23-e1fa4fa2d228 | -13.10991 | -46.35772 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df25c7fc-d654-3d3a-aa91-7fd8c7cdfaa5 | -12.23114 | -57.12977 | 2026-10-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6bbd1658-c1c2-3c84-bef0-b770217748f7 | -7.44971 | -63.64262 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2314c9d3-221c-3e46-ba49-bb7b94c49c58 | -14.45358 | -43.93681 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2495b70b-7f22-39dc-a5f1-7cd154785c8c | -7.0012 | -59.09517 | 2026-10-10 05:06:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 05a44d4d-8036-3571-a72e-4f78553286c9 | -9.28308 | -47.38924 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c966baeb-cd71-363c-9a8e-a9a3e45d255d | -8.13266 | -54.81925 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b095f76-2124-3338-8a0c-a01954ef8716 | -8.69356 | -62.4201 | 2026-10-10 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71ec0519-60a2-304e-899b-1da09e441656 | -8.30017 | -50.80412 | 2026-10-10 05:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7de3522-b18d-391b-a161-9652c859f669 | -8.17638 | -54.71629 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98e51adc-89f0-357a-ada2-3f012198dcc4 | -11.86874 | -48.03219 | 2026-10-10 05:06:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf02ce96-99a4-3b46-b9e3-d37cd946dc50 | -11.82888 | -43.58688 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 217f575e-dd07-3b2a-ba35-2d6eeefee203 | -11.66681 | -56.76723 | 2026-10-10 05:06:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ac664c8-63e0-39d8-9561-0fa8a22b476b | -13.52855 | -47.42675 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f6586bf-1215-3639-aa29-25c8ab63e35f | -11.98295 | -43.50887 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c0eb3d6-6d38-365a-9914-c5806d9bad31 | -14.73127 | -48.20906 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 112d012d-2567-371a-a7d1-e8c28d38a5f8 | -8.7762 | -49.60675 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec92aee5-0101-37eb-930e-4c92a1ddfddc | -13.39305 | -43.88245 | 2026-10-10 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ef2b311-befc-3bbb-b877-912dc98c68b6 | -13.53046 | -47.42516 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f866f67-34d4-3e9a-933d-17613a45679e | -11.3669 | -54.0229 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 810e02c1-f8cd-3f18-a59a-4a1a2fbc8da0 | -13.53408 | -47.42374 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ae18e3c-6042-3f7c-a04a-d5359657b3bf | -9.27611 | -47.40458 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa1e95fb-e41e-38b2-8dbb-09c048382c06 | -9.11915 | -45.81681 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85b1222a-c158-3b01-ad8f-a011eaca4e50 | -10.90065 | -44.82965 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14143f20-065f-3973-9fe3-38cc37ccc85c | -8.25631 | -54.72548 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa11fd4e-339a-32df-9a57-29d948af1516 | -13.50493 | -48.60798 | 2026-10-10 05:06:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80fa05db-f227-3328-ab3b-7dc5b7106d52 | -7.44357 | -63.55783 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a96a638-bc0b-3ce1-a78b-190615f8a37d | -14.71366 | -48.23116 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8708c9f0-b25c-3c28-95dd-c6ca13d339a7 | -9.49931 | -57.2465 | 2026-10-10 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 121e509a-5a83-3eb7-ae86-7c6f637c4659 | -11.75783 | -46.79636 | 2026-10-10 05:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68637b6b-0c0e-3d5e-8d3d-81ae3319cd94 | -10.59788 | -60.48141 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 942a0bcf-b6de-3c7a-ba87-da97fc78dec1 | -11.73515 | -44.95255 | 2026-10-10 05:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb5f4495-4f30-3235-82d9-d533d555987f | -11.0961 | -43.99414 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de86cfc8-d83f-3606-93a3-b8c3abe22298 | -11.37793 | -55.15508 | 2026-10-10 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78527d4a-c85d-360f-a605-2944894380b0 | -12.77281 | -44.88966 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cf0f270-f13b-3da9-9773-8289b2922830 | -10.89786 | -44.80402 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc04a0e0-ce07-36cb-8a9f-7c8cbebd6d35 | -9.51458 | -54.67305 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa842630-938a-3af4-9c9b-0afa5877b948 | -11.07976 | -44.12483 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f1d4e7d-3b5d-3974-9002-9e9921b4a29d | -11.08701 | -44.11615 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf617fed-7742-3643-833d-4352bc1146a7 | -7.90794 | -54.71547 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a816c9d-7169-3586-8bc8-0c920ec98db0 | -7.44403 | -63.55481 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8426dabb-447c-3301-91b6-54a62436ca00 | -11.36859 | -54.03441 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1a9e613-799f-3785-a8b3-a5bf438e5142 | -14.52714 | -48.04605 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5012fead-29d0-3905-98d3-e77fcb0143d6 | -11.02104 | -49.09851 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 659aed59-75f0-35c5-b6e5-d044c2fe7d37 | -11.98371 | -43.45366 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 225c80b1-ecdd-30d5-b02b-16a25aaf0ea0 | -12.29169 | -63.36666 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eafd3da4-6a5d-3aa4-adb8-eb141d436390 | -10.45017 | -47.84436 | 2026-10-10 05:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a67fcab-aad2-3fd8-8061-8fc6f6775bf8 | -7.89251 | -54.72723 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d61a88d-de56-3e99-b2a3-ad33fe06b32b | -11.18115 | -45.32677 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e0434dc-16f9-398a-87e9-524d734bf1db | -9.25475 | -62.30879 | 2026-10-10 05:06:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b3f83d9-1e57-3402-a01c-559a4eaba6ce | -11.89959 | -46.56446 | 2026-10-10 05:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c671246d-1993-3de7-b728-494c387d4b82 | -13.25409 | -42.25414 | 2026-10-10 05:06:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fb6a2bc3-70c6-3440-9853-cb479a855858 | -12.26135 | -44.75743 | 2026-10-10 05:06:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4ea6d04-0f66-31f9-9456-8740081c773e | -10.27816 | -43.95158 | 2026-10-10 05:06:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41d2c6af-0a56-3261-a178-adc440b308ff | -11.90971 | -46.56925 | 2026-10-10 05:06:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 377cce2a-670f-3a26-bed2-64b3ecb916e5 | -7.43822 | -63.55708 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3970463-e74e-3ed7-8b9d-078ff45a3154 | -13.36817 | -43.91626 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 443c410e-dd1e-327e-9e14-5e57fda1a1d1 | -11.96754 | -43.47378 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c875783-8fd7-3f4d-8ce6-e678f8f6ae23 | -12.26444 | -44.75533 | 2026-10-10 05:06:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ddcd646-6526-3826-bb28-3e08d4b76962 | -11.67321 | -46.78619 | 2026-10-10 05:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 742a73c9-b29a-30b7-9777-2c73dbbb84c4 | -11.95388 | -43.47884 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2160c769-d427-31a9-ba5a-2d807366ae3e | -7.47872 | -63.45274 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e7a88fb-db68-3945-9634-fa961b5e2894 | -8.07848 | -55.30978 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d4ac37a-1f43-3116-b0da-3adf1f102290 | -9.21453 | -51.88046 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63c82ac9-85cc-3764-94f7-91118782f1d3 | -8.26733 | -54.72012 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63a4c05c-ed75-313a-a8a4-545598d630c7 | -11.86105 | -43.55005 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 737ceadd-4eff-3f25-8747-67b5ca75ed93 | -14.05564 | -43.83985 | 2026-10-10 05:06:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b3fe912-1ad0-38f5-a400-cd14274668e7 | -11.96104 | -43.47348 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ed8ee37-7f03-31e6-9819-e1bbeb5007fb | -10.60128 | -60.4857 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 5e56ae3c-8f6d-3741-84a4-8b2a9ac9ebf3 | -10.24566 | -49.68462 | 2026-10-10 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e4ebf28-247c-36d7-9ca3-b87f479725ac | -14.71156 | -48.22841 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f7fbdc4-8df1-3638-9028-4c6c7d286edc | -8.5882 | -53.09932 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43b78ff7-e4d7-3689-96b9-030931c739df | -11.927 | -46.7716 | 2026-10-10 05:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4094911-a2c6-3c70-879b-15fb947f4e77 | -8.6504 | -54.53186 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2409026c-6dff-3485-bfdf-91283893835b | -13.77651 | -48.12421 | 2026-10-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5081edc-5752-3a1d-beac-77e3ed05b6b3 | -11.48218 | -54.61741 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e67e63a-f3b4-3885-9a82-22f403dedd62 | -10.38489 | -57.77953 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f3ef462-ffa8-31ab-844d-8b4ab743b448 | -14.3291 | -44.65672 | 2026-10-10 05:06:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71b09127-9dc3-3699-841c-16298b1e72bd | -7.92668 | -54.72556 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9ee8dbc-fc06-342b-8187-53ddd8f424a2 | -14.56017 | -48.02277 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c95fe823-acc1-39a8-9b79-661eca69faa3 | -11.95896 | -43.49116 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf167490-af94-39b7-b267-5f1f5cf79a9a | -11.92221 | -46.76752 | 2026-10-10 05:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1abf357-e328-3b99-a81f-aeb3a9febb4b | -12.72998 | -47.01307 | 2026-10-10 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2cafb86-4a3d-325c-9631-1cecc010e414 | -9.75385 | -53.89959 | 2026-10-10 05:06:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea575a31-89e1-3f5b-a049-ce8c1b5fe931 | -11.90447 | -55.90607 | 2026-10-10 05:06:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fef40032-1bfa-3a77-92ce-4a5a26ad3517 | -13.15243 | -54.36601 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e410df61-e058-38e8-9e36-a6f3e3171abb | -12.37354 | -46.61182 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e252eed-2751-3d08-a561-910121af27a3 | -11.76228 | -45.46277 | 2026-10-10 05:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 73e0ce19-5cbb-3c4a-ad51-e69c927420df | -8.10996 | -55.32559 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a25646d-16dd-36bc-b178-79904b4957f1 | -13.36999 | -43.89997 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a7b0eef-8e64-3157-9255-c615f652261c | -12.36865 | -46.60781 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbcad001-e61c-31fb-822b-f696f5b0fc6b | -12.15283 | -55.43114 | 2026-10-10 05:06:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ee9e3f0-d213-3533-b1d5-e7ab5f35c38e | -15.02611 | -46.25463 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README134.md)
