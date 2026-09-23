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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da32d6c7-16a4-3e9b-85f4-3fa1b9aead9f | -3.10375 | -60.72187 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d17aaebe-05dc-332b-8c72-6813e6bea130 | -3.15481 | -60.62473 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6e774e2-5ce3-3fba-bd51-c9e4c8744a7b | -11.12585 | -51.05777 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e35d7367-57a9-3bed-9663-03b4318641d5 | -6.23571 | -51.00618 | 2026-09-23 05:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85fe7ace-1285-3fea-933b-3685f4f53b25 | -7.88034 | -61.17954 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fbdf6d9b-0c57-3afa-988a-3a519cc79a21 | -10.95848 | -50.60681 | 2026-09-23 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e72b0c4-5d6d-3bbd-8c7d-d98052aeb231 | -11.63509 | -50.94392 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0518284e-2712-3f7a-bd9b-d837229f9f50 | -7.49877 | -63.88018 | 2026-09-23 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 051cc8e8-299c-3ea1-a383-9405261fc492 | -3.68256 | -60.56733 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cef9b07-e39b-3a22-a2b0-c6d739557607 | -2.40866 | -58.28377 | 2026-09-23 05:23:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7d3254d-34fd-3b2b-9a91-b332e2e6cc86 | -2.96043 | -54.0859 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f0ea062-7d67-397e-9287-e8a2df1755b9 | -4.55858 | -54.91777 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8902c6c4-e314-3f22-838f-eda927b6089e | -10.04858 | -50.22019 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3d47c5a6-a75a-3f92-a0e1-895e95610e33 | -3.81539 | -58.88335 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87360211-bf0f-3395-a572-21af0c61cd1e | -3.25215 | -53.96091 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6a9930f3-8e2b-3f63-95d6-05d356ea659b | -5.61972 | -45.24306 | 2026-09-23 05:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c7791af9-c65f-37dd-90f1-40fe79b1552b | -5.76338 | -45.11961 | 2026-09-23 05:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7570bc4d-868f-3218-a4f0-281d54839ac3 | -12.35604 | -50.15189 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5de6fff2-851e-3153-bb94-2bab677ab5a8 | -9.15952 | -51.53415 | 2026-09-23 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29aa71ab-48e0-391c-a94f-2a17b67269b1 | -4.00321 | -52.09193 | 2026-09-23 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc5c167c-b2bd-3b9f-b8fd-c977c9c69368 | -3.04293 | -61.25886 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 128ad7a0-a9a0-3343-b8b1-e84bd318e239 | -7.53285 | -61.50224 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47940921-bd9b-3537-9b92-9269002438aa | -3.94012 | -59.6369 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23e0c682-6ad8-35ac-b09b-78be3e9486cb | -10.30153 | -50.52554 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da29c3c4-2071-39bf-9a4f-1ef65e052614 | -3.30175 | -57.74874 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03080b4f-5873-394e-8b21-2c1c8941d991 | -8.52527 | -67.00652 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| add2b481-051e-3911-9155-12610455aead | -8.92928 | -61.48071 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c417adec-4b9d-3a29-91d7-4bf117876559 | -10.45088 | -51.28358 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5728de5-e090-3b96-a434-a51dae4ef42d | -3.58143 | -59.0726 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5df41af-43e8-360d-92f5-6a66a259c039 | -10.87068 | -50.15485 | 2026-09-23 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26251f61-3214-39ad-96a0-035f7216a008 | -9.10745 | -60.95092 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae0fdd04-2d84-3b48-9486-c4354c4e5b9b | -4.0587 | -59.83309 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3b8cf1d-4899-3b46-81aa-109f7fe6d780 | -8.04601 | -61.32393 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fc6af93-6f39-3432-ad89-3f3ec412bb3a | -11.65285 | -50.97802 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fc9e520-bfaf-3eb8-a104-9bd975e2a727 | -3.77753 | -59.59359 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5130f98d-03cd-3cb5-83f8-ecfbed206435 | -3.67761 | -60.62026 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41fd076f-34d7-3961-9ed7-30b3c203190c | -4.47836 | -55.49062 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 796448c7-a9cf-38fb-96a6-d44f670a497e | -9.55453 | -65.99768 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0106b517-d4e2-3015-9690-984535eabbb2 | -10.26692 | -49.97156 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 156072a0-08ef-3167-a195-6f3529a2a94a | -3.1492 | -48.07475 | 2026-09-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 685e4083-7c9e-3bbb-b328-6046ccde822b | -10.45662 | -50.36298 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e632b2a9-0b83-3b37-932e-62e080f69744 | -3.86391 | -57.15047 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73c53071-2e1e-3b26-bd91-b9dd7c4070e6 | -3.60974 | -60.56394 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b464a83d-d051-3345-a511-adabd72e19c4 | -5.82549 | -52.02544 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1986262f-e012-3bf3-a21f-37b27fcbe8dd | -10.28455 | -50.52012 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 20ff048a-dde8-37e0-bf7a-b37f9efb4f90 | -3.07189 | -54.39252 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7e8b4e6-60b7-3861-bd02-3b37fe50d341 | -11.64746 | -50.97732 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3f6b0af-a0e2-3472-ae3b-274ba799614d | -2.93886 | -57.78827 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e2e1078-0f07-3b7e-b66f-b1352e337f58 | -10.29518 | -50.53193 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f0662711-76c5-36a3-b9fc-84a5ac443757 | -9.707 | -58.13724 | 2026-09-23 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae885a55-12c3-3cd1-b4d4-9cfe92432e1a | -10.31558 | -50.5021 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a52250e-1bcb-3f11-bb8a-7b550df92f46 | -5.28151 | -47.2589 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b92eca7-673a-314c-9f3d-49033b07989a | -9.55604 | -65.98933 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cac7f908-d3fe-325e-9c6c-338d84d47aeb | -3.13158 | -61.24649 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13483c1c-3eda-3ce5-bbbd-3df5dc6371c9 | -7.87295 | -61.1821 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16aa3ca6-3f93-3106-9197-761e9e9d0de1 | -8.05155 | -61.26799 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d86936c4-b3b6-3554-a698-5ab37767b6ab | -9.16248 | -61.36415 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a86e4ce-8586-3db3-8eb5-5922bdeb88d1 | -3.63097 | -58.91041 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97a5b6ce-8285-31d9-9ce8-8035439e3281 | -5.37328 | -56.01935 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 651464c8-a169-3b75-8dfe-f8a221813996 | -3.95812 | -59.35276 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9ce64c8-33b3-3a66-b1c5-d41205fa7679 | -3.07882 | -58.40661 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50da23e1-8e3d-3a78-a42d-e3cf4d313ad3 | -10.2638 | -49.97507 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3153b39-8d38-31ff-8c7c-17127b449329 | -8.2349 | -62.83329 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05de6c71-73ae-3c80-a9c9-5b5704428b96 | -3.45095 | -57.4934 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04f58f0c-2fe3-3eec-8671-df54da24f3c3 | -9.16587 | -61.36472 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6250bee3-58d3-3760-b533-13566ac9bf80 | -10.26076 | -49.97466 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d107fd39-55d9-3b7f-a12b-b82f8361c32e | -3.24981 | -53.95044 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd88bf48-70e5-381b-b288-7904b8b823cc | -4.0257 | -59.84603 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df6553bd-15db-379f-9868-10c437e8c296 | -9.56034 | -65.99007 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70b1c5ae-24f9-32c0-adb8-6321f357f0db | -3.83305 | -59.39045 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e6ce69e-8f21-327a-a61d-003a81613462 | -1.90924 | -58.26104 | 2026-09-23 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80493ea3-f564-3b92-8ed5-5192967429f7 | -3.10941 | -61.09192 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 387344a5-1b08-382c-ab92-e34cc1e56802 | -10.28972 | -50.5312 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4101eb78-a26a-3e5e-baa1-425d56d13a52 | -9.11532 | -60.94486 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34c0f0d3-b259-3b78-a9ac-9c24cdbf6fc5 | -5.74202 | -53.46566 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e628568-6da5-30ef-b26c-52e3e122d106 | -4.32674 | -55.43392 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef8b74db-ed4d-3230-bae5-655a5cee1183 | -10.04303 | -50.21946 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 803896ec-d15e-3cb6-a14f-9cc427323b5a | -8.02537 | -61.34331 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3bcb18f-1dc7-32c4-8efb-ecb8a4942839 | -11.63922 | -50.95506 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a400ef6c-b61e-3968-ae38-cd9c84e2209e | -11.6986 | -50.78725 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42948598-1382-32ba-8246-cea30b9d7081 | -10.30464 | -50.50065 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6d1ff955-be1b-319d-893a-aec9c364bbd5 | -2.46962 | -57.91989 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 989be459-33b2-3cd6-a8e7-890526d88f5b | -10.29285 | -49.11826 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb968f8d-5c83-36f6-a94f-15b6d86b0a3a | -9.08743 | -60.95481 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22bc029c-42e0-34dd-a4ea-16d728dde24e | -3.90015 | -59.3546 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4468526-c2f5-336f-acd0-b2cd62bc6414 | -3.8187 | -58.88387 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2b84eda-d3bd-3f21-bfb1-07173bf64f14 | -9.1019 | -60.97187 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e190c9fb-5347-3369-b1a4-6db64c9a0c2e | -8.00631 | -61.37441 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfbf92cc-6dce-3321-976d-9a23bd7fb409 | -3.07638 | -54.38861 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ffb8fae-fc05-35f5-91b0-503a236bb020 | -3.68525 | -60.59458 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89b4f7f6-df11-3ac4-9176-ebd2adf3271a | -3.93632 | -49.99307 | 2026-09-23 05:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91ad02c6-a8fd-340b-be51-57f2d16d1133 | -2.82106 | -49.23811 | 2026-09-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da95f513-eee1-3579-8a90-a4386f17c22b | -11.71177 | -50.77075 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eaed05f9-18d5-38a9-9340-611c5b96164c | -3.68241 | -60.5903 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ff5fb2f-e3d1-32cf-9abf-cc068b8cc698 | -3.8281 | -59.33608 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3559bca6-4139-3ecc-8ee2-40482b2fcba5 | -3.44355 | -56.4963 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83d4b596-21bc-3f22-9a67-6966f0071da6 | -4.06839 | -56.22208 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67e39d3f-1725-309f-80f7-3b37fc6d5719 | -3.93956 | -59.64043 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc1e4993-7826-39b4-bc05-30ad4deb4741 | -3.7348 | -59.43223 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9f75a66-20a6-321f-b17e-992449031f8d | -10.04349 | -50.21576 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |


[Clique aqui para ver as próximas entradas](README104.md)
