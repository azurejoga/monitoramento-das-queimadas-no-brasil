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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14040146-212b-3467-9b7d-fbc945c3d659 | -6.32831 | -43.93524 | 2026-09-23 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30344168-ef76-3fa9-a2ce-0aeffabf38cd | -7.18938 | -50.83696 | 2026-09-23 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cad4340-6c7a-3896-90be-8df89be58fbe | -11.64649 | -50.95235 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d37f3014-1451-3db9-91e1-dccd114b44fc | -7.85764 | -54.70458 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f402f392-d7dd-377e-bdf9-2d3adf72fe56 | -6.6882 | -55.05513 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79545912-e7b9-3030-9aa9-723a4ce22fb5 | -4.06999 | -56.22168 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93f3cbd0-87e4-35e9-ae4b-d2010ee584d1 | -7.5455 | -47.32743 | 2026-09-23 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e5c8dd1-14f6-34f9-b489-19e6da820cae | -9.84071 | -46.38474 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cda1182a-b974-3935-9f22-59326af06bdd | -6.32317 | -43.93184 | 2026-09-23 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0eabbc53-c2df-33dd-88de-7b7de49a42e4 | -6.19438 | -57.77702 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d289dd6-dde4-37cc-848f-836c02ffad46 | -11.13209 | -49.45076 | 2026-09-23 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7bf6e00f-59ee-3935-8af7-fb42f2c96e37 | -7.09298 | -52.75008 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1294ea35-6d1b-38d6-8bbf-d8925240bbe0 | -4.52614 | -54.97219 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eac83d7e-b049-3e8c-9811-fc8bd9bf08c2 | -8.25762 | -50.87182 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c571ad8-d6c6-35b4-b397-61d35178b05f | -6.61193 | -59.96977 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c4f8e72-59b6-3391-b845-de8e7cfb48d8 | -5.24462 | -48.19273 | 2026-09-23 05:04:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f7e3ad97-aa23-3d94-ba5b-a2a9505f4213 | -8.86591 | -50.1906 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26d9d326-ef7a-388f-872f-578a8d4dbda0 | -6.6187 | -59.98644 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fab8285e-28cb-3f69-95cb-c0a97e61ea8e | -7.42389 | -49.83719 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e76d13f5-6d40-30ec-bf93-768c2b68f3d8 | -3.83207 | -59.39 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1ee163a-3516-3acf-981e-93f011d4c38e | -6.74674 | -55.09261 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7599dbd3-979b-3142-9410-24be680cc36d | -6.29631 | -57.73979 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85fabb0f-7b03-3b0a-9dd0-78e2ed3be549 | -8.12051 | -44.43212 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 137e4f4a-553b-3384-a2dd-6d0db68fa8ea | -5.87554 | -52.0619 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8a2c029-406f-3d9c-aa5e-9e47c874b73f | -5.60922 | -45.94178 | 2026-09-23 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dded929f-f1e9-3bd6-b8e9-e79735ee08e7 | -5.81336 | -57.74035 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89ed2cc3-1933-3c9f-bac7-854312a1b205 | -11.10957 | -48.30868 | 2026-09-23 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 12a5d814-4fd2-324a-944c-4a22b37a47d8 | -4.45488 | -55.07281 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00f83100-95bc-3d2f-9b52-3e0b3bf17f72 | -3.60967 | -60.57078 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc01ef3e-e1b3-33e1-846c-907a01a4efac | -3.81418 | -58.88608 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 887e811c-1412-3c72-a7aa-f6c9067bca53 | -5.122 | -48.79461 | 2026-09-23 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c857a7b-27c4-3f28-a21d-46c274cbfc92 | -8.45474 | -48.69363 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20b43950-3f64-399c-8b5f-d767f65ef6dc | -10.70336 | -48.7047 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9fd7fdd1-f993-39c9-827a-5bf27f92b807 | -9.55944 | -46.5403 | 2026-09-23 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5401e65-544c-3c55-b7c6-2a1446198862 | -3.39959 | -61.05514 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8b231c0-a260-3444-ae08-09c8c7fecfc6 | -11.64057 | -50.94305 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 08602d46-ddd8-324f-865c-a35b6e8a2e5f | -6.78719 | -48.68521 | 2026-09-23 05:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 39d1c483-112d-3b89-ab2b-2607eb3a9239 | -6.35553 | -58.2846 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74e6186d-03e4-3dab-940d-eca19c92b9cc | -6.62203 | -57.98143 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0c44d71-06f7-33a5-abb3-8832fc89e5ee | -10.29463 | -50.54047 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1c4af22-bbbe-39c8-938a-92b8206a6b8e | -6.53129 | -55.35437 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92ac4ae5-f22f-3ebe-8152-bbaf3d6f87ce | -6.08206 | -57.62947 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2743fec5-877c-3a8c-a6b4-bd425391d782 | -4.56208 | -54.92365 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bd9a2a2-6b5e-3b9c-b10e-f4e077080d8d | -9.69761 | -58.13858 | 2026-09-23 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1163f862-ceef-34d4-8e63-29be4524d827 | -11.68762 | -43.45347 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97198dfd-f60b-30e3-a6c3-42c01f421f5d | -11.35767 | -44.20948 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 976427f0-2599-36e9-bd04-2d4add60f14f | -6.62386 | -59.92408 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e7b3d95-c6c6-30be-9198-dccc58699af7 | -5.82755 | -52.19678 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f87606e-c5c1-3342-abfc-8ddb8a4a5bbb | -10.90214 | -53.96121 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96f4bc91-89ab-36a8-9379-7fe003907851 | -8.08429 | -44.3396 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d97813e-0bd0-38b1-80e2-afe86884eb7d | -6.09814 | -57.6831 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f0d5a70-ca8f-3c4c-9a36-07cc4600b405 | -3.65136 | -57.08098 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e99ead2-2f6e-3514-bd59-80d8fc45ad88 | -9.16995 | -51.46975 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2961cac3-d5a8-3ff1-ac58-716df73a99a7 | -6.7841 | -48.67995 | 2026-09-23 05:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 987dd2fe-b772-3e79-97a4-a7845a7f60e7 | -6.52124 | -43.54615 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6552cd54-7dbb-3469-ab20-7331b9c6532d | -6.97865 | -47.49187 | 2026-09-23 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77e90d33-418c-3c67-8420-bb70284e0ecf | -8.18978 | -54.724 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b4082cf-374c-32ce-a8fe-38c60252003b | -5.87567 | -52.12604 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98cce888-462f-3deb-8179-778423913564 | -6.0698 | -57.80169 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a426068-b8d3-37fc-bd52-6bac7857b760 | -8.08741 | -54.94818 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7cd9058-029d-361c-8f94-f694ccedc36f | -6.34985 | -57.771 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49accf5b-837f-3717-b213-a24c5a5cffde | -6.62169 | -59.91493 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b66e0d01-e270-32a7-9776-634a5f64811e | -3.54263 | -62.08141 | 2026-09-23 05:04:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44e85816-a370-3395-8c80-4cc44c13367d | -4.51351 | -54.98255 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 652b87b4-e33a-33cd-b63e-4ee7c8dc9b2d | -6.16086 | -57.72657 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac1e2b66-65d6-3c67-ab5f-40304ff9a83a | -8.15181 | -49.54867 | 2026-09-23 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eda3aca6-ec9c-3a5f-a3b1-270e503de15e | -4.44771 | -55.0717 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8df07cde-4058-3993-9b87-609541bb1131 | -8.49378 | -57.60767 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c63de8f1-8152-36b1-ac0c-cc67b2e28e5a | -6.68185 | -58.57316 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96b5a273-9b80-33ff-b9c3-a322ea0de6e7 | -3.58901 | -54.51743 | 2026-09-23 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c26cc4c5-d7df-3364-bfec-076766be1375 | -6.92843 | -46.56652 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed18d43b-5543-32fb-ab43-30961f937d88 | -5.74569 | -51.92326 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62eea39c-a56a-3013-abe3-78b0e280e2ab | -4.25752 | -60.01051 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d97baab3-3dac-3d0a-a782-320d09f8eb8f | -3.10612 | -60.71945 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d09ac11-1da7-368b-80b8-07212042e9f1 | -6.07323 | -51.73098 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80d0e818-dfec-3146-8e28-f8bd8181ec16 | -10.26356 | -49.97676 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad25987c-9479-3fcd-affd-7b80a657500c | -7.08876 | -61.08949 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4baec1e8-433c-31e9-ae05-882ea698bd69 | -7.45661 | -61.37988 | 2026-09-23 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c3e10914-01c3-3978-80da-c435786e7e97 | -7.32515 | -46.7561 | 2026-09-23 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cc08bd5-cbfc-3d0e-b560-256b1b165ce3 | -7.87309 | -44.97165 | 2026-09-23 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b870f55b-f1a8-3cd8-925d-1094410f1e54 | -3.68398 | -60.57083 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c9fee3e-f63b-3da1-94fc-c6bf4c8da8cd | -8.44795 | -55.02497 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0de895f-be57-31ff-ae69-aae07fd46c6f | -8.20183 | -54.71462 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e0a88eb6-6f26-3e13-ac5e-146e1d27460d | -3.11192 | -61.09493 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5bb925c-f06a-3f24-9f09-dffd7de72169 | -6.90077 | -46.56843 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ba35cd1-a9a3-3816-861a-7c8568fad7e1 | -3.74811 | -58.86374 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9821ca5-508d-3c6f-bd20-ef68afd7c1b8 | -11.12909 | -42.79527 | 2026-09-23 05:04:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 58459e19-dadb-3e47-ae11-92fe53c73964 | -6.92961 | -46.55824 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62fd2c1e-ae24-31f7-b046-989df4f00ba8 | -8.25093 | -54.77959 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec1865ee-d455-3a9d-bda5-ca1beac1442f | -7.32789 | -55.60078 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3419220-b4c9-35e5-9985-408d254b5a42 | -11.13728 | -42.77838 | 2026-09-23 05:04:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfeb8d09-d9da-3b2e-b53f-d46141505277 | -4.42486 | -55.07644 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45367607-bad5-3faf-9d49-60436175109b | -4.15583 | -60.79194 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15983670-d253-3fec-8b9d-4b00370feeeb | -6.32228 | -43.93795 | 2026-09-23 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0889283-c36c-3be5-aeb6-0de6771efdda | -10.45919 | -50.36222 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41b6568f-5332-3ee5-b500-1558c79a3205 | -3.14009 | -61.39181 | 2026-09-23 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb681d47-72e1-3b74-99de-17d77525736f | -8.18636 | -54.72344 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9672919-6218-30b2-bb7d-41f7a523e72b | -8.20404 | -54.72256 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44ed5011-5c5c-3971-bbff-80d867b8e344 | -3.68704 | -60.55254 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dd02ad7-4fca-3c96-a9e2-f1eacce4212e | -7.41179 | -42.64114 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README91.md)
