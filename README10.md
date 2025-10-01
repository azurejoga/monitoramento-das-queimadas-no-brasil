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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc8d6cb7-714f-34cd-b157-cdc49879aafb | -17.786 | -48.6196 | 2025-10-01 02:20:00 | GOES-19 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ec00570e-d5b9-39f7-95ee-92d9cef09414 | -15.1389 | -46.4485 | 2025-10-01 02:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 3258eac8-447a-3099-a7f6-75a099863ce2 | -13.8065 | -51.2164 | 2025-10-01 02:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 171.8 |
| e31dfcad-8a6a-35e7-a959-26f895a8cedc | -3.1012 | -47.0301 | 2025-10-01 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| e9258075-d053-3af4-a939-20dac43638c1 | -13.7869 | -51.2404 | 2025-10-01 02:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 29aae42b-3f77-3c3b-8bd9-a5158c73c840 | -9.4394 | -54.5739 | 2025-10-01 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ca2e1a27-7ce2-3bb3-acf2-69c7bd4655ec | -14.7826 | -45.7981 | 2025-10-01 02:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 872033b7-4983-3ac8-ab05-699adc048428 | -9.938 | -43.6718 | 2025-10-01 02:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 24f999d8-b44f-3ce7-a920-297211b2f2fa | -5.6361 | -43.9258 | 2025-10-01 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| fac9ce12-6601-343a-860a-f8fa57c352e3 | -3.1013 | -47.0082 | 2025-10-01 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 201.4 |
| c4b09176-897f-382f-a129-86c82ac5b8be | -9.3089 | -54.5229 | 2025-10-01 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| faf8eb30-2672-3fe3-9a4d-1bf77771dd2a | -9.9383 | -43.6483 | 2025-10-01 02:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 6783fbe8-4f80-36a2-a8e8-f25903964903 | -13.7873 | -51.2189 | 2025-10-01 02:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 416ffd17-6ec4-301d-9ff3-8a1605ce038b | -11.8434 | -44.9872 | 2025-10-01 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 28ff9a60-1273-3556-9b3b-eca38d578afc | -13.1973 | -50.9095 | 2025-10-01 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 668b5129-2466-3ece-8218-d8ab53898c85 | -6.153 | -44.736 | 2025-10-01 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 82748129-17aa-36b3-a40b-f0b55d9c48b1 | -3.1012 | -47.0301 | 2025-10-01 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 092255a8-d5c3-3505-b840-eddd0666d8fc | -15.1615 | -49.082 | 2025-10-01 02:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 5639cff0-592d-384e-899b-92be9a0292d9 | -14.9087 | -48.1208 | 2025-10-01 02:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 0f1939dd-78e0-3da9-a827-bea93937ea7f | -14.7831 | -45.7749 | 2025-10-01 02:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8fb30495-8e88-3424-8522-e57fbe145de4 | -13.2165 | -50.9071 | 2025-10-01 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6a74dab1-73e6-39c4-8fc5-3703c5e31128 | -9.3089 | -54.5229 | 2025-10-01 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| e40b3e2f-2177-3bb5-888a-db47e8faeb1b | -13.8065 | -51.2164 | 2025-10-01 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| eb0c2c32-f7f9-3272-bb55-172cb374284e | -15.181 | -49.0788 | 2025-10-01 02:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 125.7 |
| a32bdad7-1edb-31f5-b551-0d05b9caac67 | -14.3519 | -45.9206 | 2025-10-01 02:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 18f77713-25e7-3269-a193-0f58c6a885d5 | -11.8246 | -44.9669 | 2025-10-01 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| b7d33ec9-a755-3ad4-9f72-e2c4ee04f834 | -3.0827 | -47.0088 | 2025-10-01 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 2eab633f-a85a-353d-8067-0f52e97949e7 | -22.5946 | -46.7698 | 2025-10-01 02:30:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| 09f2b089-6e76-363e-b27f-07a4c5f71ec6 | -9.4394 | -54.5739 | 2025-10-01 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 36916896-0424-3770-b9a2-4775aa63230e | -14.1931 | -46.086 | 2025-10-01 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| e394d442-214a-3817-9c16-2d0e168fba35 | -3.0826 | -47.0308 | 2025-10-01 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 15ed6940-cc0f-3963-b8af-7fe4f60cd442 | -13.9396 | -48.1182 | 2025-10-01 02:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 95cf96dd-e655-3b5b-a5ac-52cb2f5ea0c2 | -14.7826 | -45.7981 | 2025-10-01 02:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| f390cd87-cda0-3d32-96de-a3f56423010d | -14.3524 | -45.8974 | 2025-10-01 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 8c6da8dc-2e98-3f0a-b0f8-a66380dbf7c7 | -13.7873 | -51.2189 | 2025-10-01 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| faa36725-09b7-345c-9235-c2c738861a34 | -14.1921 | -46.1321 | 2025-10-01 02:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d326e312-0a33-3676-924e-daeaed4c9b5c | -5.6361 | -43.9258 | 2025-10-01 02:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 14e17741-1cb5-3435-a8af-57b1a37cfb41 | -14.1926 | -46.1091 | 2025-10-01 02:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 234.6 |
| b3954dae-91f7-3bb5-9495-dc339cfed5ae | -16.2562 | -50.9275 | 2025-10-01 02:30:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 50981e00-96d1-354b-92f5-65ffd170f530 | -11.805 | -44.9929 | 2025-10-01 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 58eabd2c-ac36-3100-8ebd-c5b6c2b2d0cd | -5.8657 | -43.3981 | 2025-10-01 02:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b6e4104c-2e14-3f35-879f-67bfc80059d8 | -15.1806 | -49.1011 | 2025-10-01 02:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 542437be-da84-31f1-be5f-719ce3519b3a | -11.8438 | -44.964 | 2025-10-01 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 75f84d13-4edc-3ffc-b845-e3b4b33aa63e | -6.1342 | -44.7375 | 2025-10-01 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| c5b4d942-1e11-345d-bf96-a26ac18d4baa | -22.5687 | -51.1123 | 2025-10-01 02:30:00 | GOES-19 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 0e7b5f7d-921f-3c57-9098-cabc10f83681 | -14.1732 | -46.1124 | 2025-10-01 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 0d06179d-ae09-3788-8961-8d2b7c8b99ab | -11.8242 | -44.9901 | 2025-10-01 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 8d372444-d692-3ff7-9a74-b7809fc77dd6 | -11.8054 | -44.9697 | 2025-10-01 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 809a3080-1474-389b-94bc-b1ceb8c0ec32 | -14.2121 | -46.1058 | 2025-10-01 02:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| d0d62178-aca0-3954-83d4-cfb0655b7ca8 | -3.1013 | -47.0082 | 2025-10-01 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 6499d002-e626-37d9-83c4-0332e26af494 | -9.3089 | -54.5229 | 2025-10-01 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a768cd76-78dc-3367-80c3-529158a2269c | -11.8246 | -44.9669 | 2025-10-01 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| feef8e98-730c-30f5-887d-b1f7dd7186e1 | -14.8026 | -45.7713 | 2025-10-01 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| ecf590df-4d43-3e48-8416-cc8cb19ad43e | -14.7826 | -45.7981 | 2025-10-01 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1aba2d74-3dcf-3833-b8c2-a4f144c6b238 | -3.0827 | -47.0088 | 2025-10-01 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 902e9e7c-5b4a-36a1-a025-d888d6931870 | -15.1389 | -46.4485 | 2025-10-01 02:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 5836ce4d-65f8-33a4-a954-31b67f8badd6 | -11.8438 | -44.964 | 2025-10-01 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| e422a3bf-2b6a-32f9-904b-482ae5affd4a | -14.7831 | -45.7749 | 2025-10-01 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 086edbd6-11bc-3de8-b14c-3ab3e98fd7f0 | -22.5687 | -51.1123 | 2025-10-01 02:40:00 | GOES-19 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 1fab1df4-d04b-3143-b583-430f64e1d2cb | -6.153 | -44.736 | 2025-10-01 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 6558bf5e-ce92-3373-a11a-adbdc09cf6e7 | -14.8021 | -45.7946 | 2025-10-01 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 3c6e8347-a083-3938-8683-6d392065e36c | -14.1926 | -46.1091 | 2025-10-01 02:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 3d816670-4c83-3e84-86dd-5577324ba1b3 | -14.1921 | -46.1321 | 2025-10-01 02:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d0224947-b9d6-3e76-a4ef-9ec21380a0c0 | -11.805 | -44.9929 | 2025-10-01 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 0137281e-eff5-335e-9499-f632ee31c54c | -11.8054 | -44.9697 | 2025-10-01 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 90844b65-092c-3492-b3c7-6d5f208aa957 | -3.1013 | -47.0082 | 2025-10-01 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 83652e08-4631-38de-8017-38e6a1c4a4d2 | -3.1012 | -47.0301 | 2025-10-01 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 0e1b852d-4adb-3951-805e-52407cc17b5a | -20.6309 | -46.2046 | 2025-10-01 02:40:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| b86fee26-fcd0-3e0a-b739-356036e7aad5 | -10.9773 | -46.5217 | 2025-10-01 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 3ae60252-2eea-38b5-84ca-54b898e20ba9 | -5.6361 | -43.9258 | 2025-10-01 02:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 02473f93-6ba2-39fa-82f1-213cf1f9331e | -10.9769 | -46.5443 | 2025-10-01 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 0255b9a2-e5c4-30a5-98b0-a76cb2bddef8 | -6.1342 | -44.7375 | 2025-10-01 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| fee64c43-7f15-3897-97c2-2261316e6c3d | -13.1973 | -50.9095 | 2025-10-01 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 63bfaf65-c7cb-375f-8573-474de9da0866 | -6.2408 | -45.3424 | 2025-10-01 02:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 65637099-444a-36ed-835d-2e92f84fd515 | -13.2165 | -50.9071 | 2025-10-01 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 62baf610-6b5e-3051-8a18-576f7c405c0c | -9.938 | -43.6718 | 2025-10-01 02:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 54510adf-14c2-34e1-8efa-50371957f943 | -16.2562 | -50.9275 | 2025-10-01 02:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| e55c096c-4be0-344e-bab6-6b7675bebfda | -11.8434 | -44.9872 | 2025-10-01 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| aecf32ba-c6b8-3947-8611-6869f490c7f5 | -14.3519 | -45.9206 | 2025-10-01 02:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 9de9ba6a-965c-38da-a7ae-713c81c97ae4 | -14.1732 | -46.1124 | 2025-10-01 02:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| c3d7c8d9-0d3e-3c87-8204-74da30863fe8 | -11.8242 | -44.9901 | 2025-10-01 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 175.2 |
| e8fcd5c8-492a-3d94-905e-e1e1efa435ef | -14.8021 | -45.7946 | 2025-10-01 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| b3929805-973d-3ca9-9e73-676750040ab1 | -3.1012 | -47.0301 | 2025-10-01 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| cb6caf5d-1e65-377e-824c-2d9adbce6c16 | -14.8026 | -45.7713 | 2025-10-01 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 927aea5a-c53d-3f4e-a81a-cab07a0c86e3 | -14.7831 | -45.7749 | 2025-10-01 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 0f350579-3431-37b0-9c77-fdb21f7441ba | -9.2902 | -54.5242 | 2025-10-01 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d3d546b5-c240-35e0-894c-a6d27dfe3f20 | -14.1926 | -46.1091 | 2025-10-01 02:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 7affb023-ec25-3367-b394-311858bd520d | -14.1921 | -46.1321 | 2025-10-01 02:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 6e085194-cfbf-3325-953c-f9155e8e74ef | -14.7826 | -45.7981 | 2025-10-01 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e79ee073-e1af-32b1-af5d-2f56ae29d764 | -16.2562 | -50.9275 | 2025-10-01 02:50:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7c06ee53-af02-3b57-a90b-dcc0492a972d | -3.1013 | -47.0082 | 2025-10-01 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 41597774-210d-3d01-8112-1a5adcd4f4c2 | -14.2121 | -46.1058 | 2025-10-01 02:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 09e234fd-7269-3117-9eb0-4c9571e86f88 | -23.1604 | -50.0841 | 2025-10-01 02:50:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 130.0 |
| cd926102-0c57-3857-9d0b-c518a9d0553e | -9.3089 | -54.5229 | 2025-10-01 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5a156925-1f17-3efd-850c-e67d21aa51c7 | -15.181 | -49.0788 | 2025-10-01 02:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f7d8041b-3c72-3e08-b7a1-97ee6490fb9b | -14.3519 | -45.9206 | 2025-10-01 02:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a9e50069-a1b2-3312-95d2-26344aa72318 | -5.6361 | -43.9258 | 2025-10-01 02:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9605f053-a0a3-33c9-ba08-511f574f9807 | -6.2408 | -45.3424 | 2025-10-01 02:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 90cc1394-67c4-366c-bca9-9f00756cedc0 | -11.6285 | -47.4892 | 2025-10-01 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 12805eb9-2e6d-3782-90f5-4f7bdd5c6b89 | -13.2165 | -50.9071 | 2025-10-01 02:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |


[Clique aqui para ver as próximas entradas](README11.md)
