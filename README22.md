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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e349cbc-60f7-3026-8703-cb7de9e18161 | -11.86819 | -52.25705 | 2025-07-16 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fcf264e-1584-3dce-9ac6-9473e0d1d0cc | -10.10513 | -58.21913 | 2025-07-16 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfbf18c5-b626-33a2-9cb1-33aaca38f127 | -12.58055 | -56.97816 | 2025-07-16 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cbd5c84-95d5-3543-b226-5f3129639ca4 | -9.24655 | -58.76956 | 2025-07-16 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 563cff8b-212f-32c6-99ff-e34a87d7bd0b | -12.4823 | -46.92329 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd408387-60aa-3899-b8ca-42ccac3cc094 | -11.87632 | -55.45221 | 2025-07-16 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1f27481-ae1f-3ffb-af03-73552db398e9 | -9.86937 | -60.29677 | 2025-07-16 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 945d762f-4a61-374e-b591-7554a05edbae | -9.84895 | -47.87654 | 2025-07-16 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbd41b22-2899-3354-9495-facaba28bbec | -13.01497 | -45.06559 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| dc742700-9dfc-3f15-88f9-f80bfabc633b | -10.59168 | -55.43729 | 2025-07-16 05:06:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c15eedcf-682e-3997-912e-cd6933b9dcb8 | -9.77957 | -57.4238 | 2025-07-16 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8060c891-ffdd-3255-ab3a-df943a5aca2f | -13.0221 | -45.06077 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 25cdc6be-7ae8-3317-a80b-48c47ed230ca | -13.02273 | -45.0551 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 50b44e2d-5ced-30c9-8d0b-ad413ec7894e | -8.68908 | -64.12367 | 2025-07-16 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4decb11-7b3f-3b6b-9166-1e0d4a4e94fa | -10.57131 | -49.11753 | 2025-07-16 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a57bf491-d121-3051-8bb4-00d89d0d7602 | -9.7409 | -48.63589 | 2025-07-16 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee5bbfb1-eed7-3400-8014-dfaa2351d066 | -11.45431 | -45.09901 | 2025-07-16 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5223380-24c5-3739-8656-a5c34d65d5e0 | -12.48233 | -46.93456 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b2443c4-2ae1-3cf3-b48f-82704351ed02 | -14.31363 | -52.74574 | 2025-07-16 05:06:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c885331-46f0-36ce-8941-42ae1d52474a | -11.95201 | -48.41589 | 2025-07-16 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2921bc45-548e-39e2-b352-b4b6393f4bb4 | -9.02548 | -61.23577 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df711aa3-f0c9-34b2-9dad-4d80f238c08b | -14.58902 | -48.1167 | 2025-07-16 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01ef1cad-1541-393d-a4a9-832e6b6bc8c9 | -14.59349 | -48.11783 | 2025-07-16 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f85b7895-a0bf-3348-a63f-76e773c33caf | -12.48706 | -46.93223 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbe221f0-778c-35b4-b5f0-aecb789c97f3 | -12.489 | -46.92719 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92d22ec8-e376-3943-b7bc-28c7af2ba685 | -12.0195 | -47.78126 | 2025-07-16 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3e2dc99-fd70-3c02-a14d-1ffd4772d6eb | -13.01435 | -45.07116 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9a8324cd-29a5-31d0-85f3-37a2ee0d1b8d | -11.47098 | -47.30818 | 2025-07-16 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33c315ce-baa9-39b9-af76-6006680bd12f | -14.60265 | -48.6675 | 2025-07-16 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| caccbd5a-1269-3097-b6bd-67c41d7f36cd | -12.99565 | -44.87936 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6d4836e-eb0a-3c73-8052-238ca8f6632f | -10.67894 | -56.54731 | 2025-07-16 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 04d22c4e-3ccd-33db-aa59-bad4ff336ea2 | -10.32019 | -49.91917 | 2025-07-16 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c105a0f-41a0-3c2c-8da3-04d6add86f89 | -11.49209 | -48.07458 | 2025-07-16 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 212103c5-4284-3f27-97d3-44e4f0984d62 | -9.01937 | -61.2244 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b23c190b-5440-30e4-93a5-90cb6057b938 | -10.6506 | -49.47652 | 2025-07-16 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 42434ba8-9501-3a56-a962-8b02a3f6270d | -10.27862 | -47.61655 | 2025-07-16 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e86ce8d4-969f-3a31-90a1-efda7a18af39 | -12.4708 | -46.9217 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05fab0eb-c237-3f34-ae19-97b2da053a22 | -10.65215 | -44.48725 | 2025-07-16 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfc7778f-9992-3ca0-91a9-9a13661a8323 | -9.66743 | -49.89362 | 2025-07-16 05:06:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80c18c23-6837-302d-a079-eab2ce494e54 | -12.48279 | -46.93048 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eeb044b-fbd5-3758-913d-121a9936210d | -8.55809 | -64.19521 | 2025-07-16 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 167c5b0d-76cc-35b7-aeae-bd11bf5c37fb | -9.85415 | -47.87741 | 2025-07-16 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93d07955-7a60-3c92-ab44-22eb9c296194 | -13.16603 | -50.78295 | 2025-07-16 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c09faea5-7306-3141-bf54-a3c9acd506a2 | -9.66076 | -63.22294 | 2025-07-16 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a06218b-de4f-3d84-8367-62830526815f | -9.01908 | -61.22718 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 701858bf-9ac9-3414-af94-d62825e4bb2e | -12.99628 | -44.87353 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14ed8dfd-7fa4-3e5e-b4e9-415a008f5cc3 | -12.48755 | -46.92814 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c33be388-4385-39b1-9d95-af3c99d3ec97 | -14.60226 | -48.67076 | 2025-07-16 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 821ddf87-aae1-3f07-8721-2dfa800274c8 | -10.96325 | -49.25342 | 2025-07-16 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e83bc633-bcfe-322b-9bd1-365ca7eef7f2 | -12.07352 | -43.47693 | 2025-07-16 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b3de4042-17e9-30ba-a410-3bba9e59bbcf | -12.48804 | -46.92406 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bc913ee-0553-3b85-bbec-5164f89bd7b7 | -12.48371 | -46.9223 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2a6b484-342e-36ce-af5e-705b4169134c | -10.05839 | -59.11241 | 2025-07-16 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5c1d5b3-ad19-3327-91a2-7578dff13c65 | -13.91459 | -49.52711 | 2025-07-16 05:06:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 493c7e3e-6855-319c-92c0-483bea874dac | -12.49379 | -46.92485 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aca44409-9707-3dcb-a97b-694163876f1c | -9.70815 | -56.18526 | 2025-07-16 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b98f359d-04f8-32bd-bf44-943c7ef04025 | -12.02489 | -47.78209 | 2025-07-16 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ef52a806-d9e7-389c-9d54-b5f9bfc9c735 | -9.96432 | -64.96128 | 2025-07-16 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98b9ae12-07fb-3adf-9ec4-ec7e56015d7f | -10.22766 | -55.45941 | 2025-07-16 05:06:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e89a99f-ec26-3227-98b9-77e43fc66402 | -11.94682 | -48.41525 | 2025-07-16 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b845f138-b7be-3a13-a4b9-57742495ca3c | -9.0185 | -61.22941 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5414ad7-8f12-3d14-a5d9-a737c80ee427 | -10.28214 | -47.61929 | 2025-07-16 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 005f4adf-ddbb-3531-858b-91d794a7701b | -9.02891 | -59.54462 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0806919-04e4-3f0f-b8cb-71a1fb02e5e1 | -12.62468 | -54.22868 | 2025-07-16 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3141747-5971-3b83-b88f-1b983ec854b6 | -10.56851 | -49.13882 | 2025-07-16 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3936b81d-13ed-33bb-a371-11b109f2b901 | -11.49706 | -48.07746 | 2025-07-16 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff40461d-cf34-3eb1-a769-2526757ca8ca | -11.47512 | -47.32007 | 2025-07-16 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62e84e7d-adb0-301d-b36f-fb797538b69b | -12.5659 | -48.88786 | 2025-07-16 05:06:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 963da019-6c45-3465-beef-17b22489858d | -12.04069 | -48.76661 | 2025-07-16 05:06:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0ccb13a7-8b0a-3f22-ab0e-b231e2207107 | -14.59312 | -48.12092 | 2025-07-16 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdeb01df-4565-3dd3-bda1-ff7e0037446b | -12.03563 | -48.76588 | 2025-07-16 05:06:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ed446e7-db87-3c2e-8b68-a8c2db29cbcd | -10.10455 | -58.22276 | 2025-07-16 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b85cd84-fa44-30b9-9a3b-0a6a0b504d49 | -14.59425 | -48.11957 | 2025-07-16 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ad2ff8e-267b-3afd-927c-ee78d00e342a | -12.48132 | -46.93143 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7179b66-916d-3c10-a15c-f2382780c9a5 | -11.37592 | -54.3457 | 2025-07-16 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b90ff295-14ac-30a1-97b8-2b5623149c7b | -9.0182 | -59.54287 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2484c753-2e2f-318f-8750-bdbbdc763c2c | -10.28395 | -47.61735 | 2025-07-16 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30442879-9f78-3746-8567-76099b51e826 | -12.02534 | -47.77845 | 2025-07-16 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 12e95063-57f9-3e3c-8f3f-4926ef5c4127 | -10.0562 | -59.1041 | 2025-07-16 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 855b354f-e1cc-31a9-8684-c5d730798dd5 | -11.18697 | -48.62168 | 2025-07-16 05:06:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b9e84ce-5762-347d-919e-814ce114e371 | -11.95121 | -48.42226 | 2025-07-16 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 38edd456-ee48-374e-9d00-4ddfc06b4eb9 | -10.64588 | -49.47579 | 2025-07-16 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a3e58d2-e64a-3cfd-b01d-9a9f9c0e8bac | -11.95161 | -48.41907 | 2025-07-16 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a829f1cd-3c83-337e-83ba-5eded227260e | -10.06186 | -59.11298 | 2025-07-16 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c497d76-eb47-36ea-acf7-7b00fb7c3d44 | -14.5887 | -48.11959 | 2025-07-16 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 677a832c-7d46-3d71-b923-9c32dcb25599 | -12.47703 | -46.91843 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0526f266-ba43-3c52-84fe-4fc418f3ed8a | -9.71741 | -61.29129 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9da30877-8b9b-3a89-a303-fafebae4ccf8 | -10.90006 | -49.2157 | 2025-07-16 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 39bd7ead-e9e7-3e09-81e2-b5a7f8268ea6 | -9.71825 | -61.28632 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e5312d9-d812-3dce-82a6-edfbc7d5aa95 | -12.6233 | -54.22534 | 2025-07-16 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58f0e48b-b56a-3f88-8ea8-cc38f1adfa09 | -11.18658 | -48.62467 | 2025-07-16 05:06:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 668315f0-9a31-3f12-9f7a-edbebe8a446a | -12.62528 | -54.22449 | 2025-07-16 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b33a4023-4b22-3c94-ad91-3ffae9c4bed0 | -10.0603 | -59.10079 | 2025-07-16 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a6f1c46-1a69-33a6-b9b9-0a718f3e9209 | -10.28256 | -47.61591 | 2025-07-16 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3dea35b-7246-38dd-b61f-324f5786400d | -9.01991 | -61.22216 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96290077-1865-3699-8a98-dc5042983ca4 | -9.02415 | -61.22004 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e95940c-ba5c-326a-870b-2d212f24c1af | -9.95938 | -64.96039 | 2025-07-16 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e76219f-2c7d-3477-859f-adb07ec466e4 | -12.49521 | -46.92389 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc17c863-60ef-3a2c-9af8-a43620be4b85 | -9.64854 | -63.44632 | 2025-07-16 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1902690-c0bc-31a5-a98a-06cea2b132f3 | -10.57612 | -49.11839 | 2025-07-16 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README23.md)
