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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f3f24f8-3d3e-334d-8919-cd0a84ec5045 | -3.42623 | -61.32826 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e74095c1-e478-331c-bd85-bb4fe25659a9 | -3.52922 | -59.61549 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 40c33814-8539-31d7-937a-f470fd7e0bdb | -3.6108 | -60.57944 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b95cc0e5-3040-36e5-aa5d-c4da0e96e4e7 | -4.25543 | -60.00674 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92783edc-6817-3017-a170-22b0fadf0374 | -9.14855 | -61.18667 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc9d9649-13a4-3fbf-a926-c3e23d3d99ae | -10.25924 | -49.98626 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92bee083-ec8e-3376-a528-ba8595d64498 | -3.34036 | -59.85851 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 38573f84-852d-3a01-9850-8b012ff870df | 0.78779 | -59.20264 | 2026-09-23 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bd3120f-d762-31a8-8ce2-e8194e20a847 | -9.1123 | -61.60563 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b49d7907-df72-3a73-9fc1-8c11ab0f61c8 | -8.92806 | -61.48809 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d44f7c1-ffcd-3aa5-a2ea-475201073cdf | -5.75615 | -45.1189 | 2026-09-23 05:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9cb83317-5dd1-39ca-8f1f-661052b86904 | -9.1468 | -61.19753 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 631b7244-b202-359a-b882-2ffc999f671c | -7.55656 | -61.48682 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dde866d-ecc6-30ed-87f4-c5a83d37b63c | -10.31101 | -50.49424 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c777ef0f-43ac-3f23-b74e-8c96c720b99a | -2.95585 | -54.09007 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc65a54b-fb16-348e-969f-c3ac1190e2ca | -3.40239 | -61.2956 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e12b8db6-8cf7-380c-af85-4b7da2128a37 | -3.28419 | -57.85971 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab1026d1-3118-3d8e-85a9-41d9281c592a | -9.09126 | -60.97382 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eded757f-177e-374d-b2e9-633c767df68e | -4.02513 | -59.84958 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 408f1788-e1d2-3818-a1d4-651be5b1daa4 | -3.07074 | -54.39868 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c3b730-3719-32c2-9433-b649adadc0db | -2.45461 | -49.21931 | 2026-09-23 05:23:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 34632f83-808d-345e-b0ee-5d3758616a57 | -3.07275 | -58.40214 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8132744-d9c7-3137-ada8-b05e4475103c | -3.22403 | -46.94619 | 2026-09-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 326eec14-d99c-3135-aa7c-3d11e293dbca | -3.07117 | -54.3971 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 838111c6-83d8-3b20-96b3-1b7bde0a7340 | -8.31569 | -62.88887 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1136ac93-78a6-3f12-a315-75e83c29c58c | -10.26641 | -49.9754 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e8d9236-221f-35d6-bc80-00c80660cfaf | -4.06968 | -59.86415 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 655031c0-0992-3015-8176-aa30a1c3bc36 | 0.98059 | -59.37964 | 2026-09-23 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e1e5b88-a9dd-3ded-aba2-57eb77733285 | -3.7501 | -58.8656 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f0fa670-1c0d-373d-b5e4-81eac723e3bd | -9.92385 | -48.47735 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46c0038c-e2bd-3ab1-a843-1ab571781227 | -4.29696 | -49.13049 | 2026-09-23 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba018983-b63c-37f6-9150-19c7debd13c7 | -4.15233 | -50.45968 | 2026-09-23 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 37e0965b-738b-3a43-9de6-4112b535bc55 | -4.16078 | -60.77605 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 404da191-551d-3c6c-be9e-c9dbb03784b5 | -3.58607 | -54.52082 | 2026-09-23 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1558ec6a-584d-3b7b-b8d7-7eaa93d03adf | -1.94259 | -56.59098 | 2026-09-23 05:23:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a27ff52e-8ce2-30d5-8a0a-16fefded1e75 | -10.2654 | -49.98311 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db2615b1-e9e6-34cf-9683-a971c06cc700 | -9.34843 | -61.16737 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97857880-ff7d-3897-acc4-fdfde5d2e9ac | -4.16139 | -60.77229 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64ebdb0d-69ea-309e-a2a9-2e4b45dedc58 | -9.16076 | -59.55695 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7416d3a-a90d-3a39-a8e5-9ceaa0b2f196 | -11.70139 | -50.80938 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b551eaad-8c67-34fa-88f9-e934083901a7 | -10.91176 | -53.93779 | 2026-09-23 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fffc1da2-4ff9-3c5e-bac2-c9d89e9bc267 | -2.62694 | -51.70521 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26b5e2ec-0390-3e80-b6f5-311411321de7 | -5.77487 | -47.15771 | 2026-09-23 05:23:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1c8dbe6-067c-3693-9662-19d4d1a4bce7 | -3.81208 | -58.88282 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e034949-fcd7-3a63-9adb-24cfd5858012 | -9.04219 | -66.05028 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3abea2cd-83fa-3b02-8e4b-6a21b6115257 | -9.09826 | -61.43292 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2398f69b-f39a-3d4f-9cb5-531b2e388aec | -3.1893 | -60.43006 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a22878f-9bbf-3efc-bf9a-fc0c57f7d303 | -3.32761 | -59.80889 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0c8291e-73b6-3e03-bada-11a253ec4594 | -4.21985 | -50.66224 | 2026-09-23 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed7861f2-dfeb-35ea-a3a6-2b0a6a04639d | -10.29452 | -50.52866 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46b5b8d5-01d8-3810-96fc-ec0f3ced35ca | -7.8291 | -63.41404 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0be4b81a-d51c-3b8e-8783-0b329d91677c | -6.78387 | -48.68125 | 2026-09-23 05:23:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e7a143c-5415-3d78-b92f-92a517c402c1 | -10.70916 | -48.72401 | 2026-09-23 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b016645-aa73-315c-a72a-fc4c5b24f08b | -3.68045 | -60.62455 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 309db135-4edb-3d2a-b27f-466e3b2f207d | -2.4541 | -49.2226 | 2026-09-23 05:23:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3eb82ec1-e006-3651-93b2-8c112fba0e52 | -1.14456 | -54.15869 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da1f9b83-69c4-3cfe-a059-8ca879a5d341 | -3.82589 | -59.32859 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a49b55a-837f-3604-a134-9889b99e6ada | -5.80611 | -49.15759 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b839c2c-a22a-3d1c-bf7b-62c2fbeb2edb | -9.15529 | -61.18778 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2d2859a-c3fa-3e19-968e-0d4b0c994c1e | -2.88861 | -57.28717 | 2026-09-23 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1cda16e-011c-32a8-a087-027129ee38be | -8.23922 | -62.82967 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6704e3e9-ea25-3742-8038-be293d72a0a7 | -11.10987 | -51.05566 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 241e4ff7-1e6a-312f-8345-b874abd3dfb2 | -3.25326 | -53.95857 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16dc077d-4502-3d69-a31a-137e0b0b71f9 | -4.56719 | -55.06044 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6e46ff5-735e-3997-8772-263b96dcb33a | -10.25173 | -50.20892 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ea71c88-ae88-34a8-ab15-e883a7ab0814 | -3.38654 | -57.94342 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6219be7-d059-3cdb-9329-398822b10164 | -2.93554 | -57.78774 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9ea464a-7ddc-34c8-ae96-bae2ebde90e3 | -11.78093 | -50.98042 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7ae37de-7282-30c8-b4c2-7c9f75a750d7 | -10.27769 | -50.53003 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d80e56b8-c802-32ab-9a65-b1672173e569 | -9.30639 | -60.30919 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26ad0fbc-15b9-3be3-8e68-75aab3c02b0b | -9.84049 | -46.38457 | 2026-09-23 05:23:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6f0c88ec-2f2f-3421-b8ad-03736ce609d4 | -3.20871 | -50.91878 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63ca85dc-7aff-31c8-918e-486850dc8b46 | -3.35825 | -61.30156 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f90ae04-7cfa-3ba8-9914-670d4fa5c856 | -5.56873 | -52.02327 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d34248c-8fd4-32d0-b803-265a7ec152ca | -9.18884 | -65.86047 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a7ef5b3-1d03-30b5-99b9-8437b8d943b1 | -3.04324 | -54.40228 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4b3328c-72b7-3288-a697-7ef697a0615d | -10.29124 | -50.55341 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c6fdd04-bb90-3655-8b03-705862207503 | -3.65007 | -58.76859 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 521610c7-4d36-3b96-8bbe-c82ef1e82fd5 | -1.21957 | -54.55627 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a9e4baf-d6d7-339f-9848-5cca784e17f4 | -3.55782 | -59.96647 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c8a60c9-f124-3965-8f01-b709cabb1e54 | -3.11358 | -61.08853 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba363fab-ac3b-3a7c-b407-80a9ef48ff7a | -11.7063 | -50.77005 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bb5f6f8-8eee-37df-bd9a-e490e60e8814 | -9.08885 | -61.01024 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3eceb36f-0836-33b7-91a8-5d60f5202a9c | -10.04256 | -50.22314 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a706c9d9-9d1a-38aa-925d-4864248c9f86 | -4.32573 | -55.43486 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6100ce60-b382-3525-83d7-3f721c4d4f3f | -5.50665 | -51.71532 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4db403de-cb80-32c6-bf15-24ef887f15eb | -9.11415 | -60.95202 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 911811d7-e233-3d02-88d0-5d098b5209e2 | -3.3303 | -57.99837 | 2026-09-23 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9eeaef5c-c02b-39ef-8208-765b22811722 | -5.61515 | -45.24763 | 2026-09-23 05:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5bba0f11-84f8-38a4-abf6-ac1dcb30b3e1 | -6.12763 | -52.76445 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4344d6f-22ff-3a2f-99c6-91dd137ee385 | -9.07511 | -61.42535 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d06f23a-ca3d-3fa3-bf9a-278ba4bf510a | -3.6444 | -60.60727 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f438ead7-420c-3446-8a80-1a914b5733fe | -3.19557 | -60.43488 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d291c226-3ec9-3fc8-b2a1-a5e789c4fa4b | -4.05814 | -59.83664 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f5fa3f7-66e6-31ac-98b0-fa845325f334 | -3.14982 | -48.07071 | 2026-09-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d32adaa9-63e2-3a62-8540-a1bd4d5e0f73 | -4.05457 | -56.31029 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9054e25-a130-3bf1-adf7-82f0bb05e732 | -10.30509 | -50.49707 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 71dd9d07-7336-3ef6-9800-2af7c8f56c94 | -11.12094 | -51.05371 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b86e67b3-4ea8-391f-aa35-c0a53d44a78f | -2.74412 | -51.54985 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94c396ac-070b-3b9b-8ee7-2ce4c2b27f21 | -4.45333 | -55.02257 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README105.md)
