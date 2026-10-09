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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c45bc686-afdf-3ab9-bd9c-ff0edf26fc8a | -6.0024 | -40.935 | 2026-10-09 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 186.2 |
| cbc02fa8-e706-39a2-8b90-a3c69be045ac | -3.2576 | -54.0418 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 2a4257d5-f74b-334d-9c50-cda868b193b8 | -7.1997 | -55.1427 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| f79a06c2-7d94-3df1-b480-7eedbbdc97eb | -12.2343 | -57.1271 | 2026-10-09 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 8b2713b2-0b84-39e3-a43a-f373786e122b | -1.5489 | -54.5556 | 2026-10-09 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8e618b88-3977-3db7-9571-0713eeeed97c | -2.499 | -56.0675 | 2026-10-09 00:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2e3ee17e-71ad-3cea-a3c4-9fe5c49a82e8 | -3.0002 | -54.0684 | 2026-10-09 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| d3b39259-3b55-3e9a-977c-8c776f233072 | -5.7679 | -43.8467 | 2026-10-09 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ff347600-3647-3d6e-b6a9-3b41e12da382 | 4.4436 | -60.9467 | 2026-10-09 00:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 91c73a69-56ce-3acf-a45d-aac87f87e2a3 | -1.1094 | -54.1802 | 2026-10-09 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| dffa894e-096f-3a70-9e8b-5e69784b0fe3 | -3.1879 | -58.6433 | 2026-10-09 00:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3658ac8a-2a2a-3590-9a66-d988d3fc015b | -8.505 | -54.6404 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 88f41bc7-1a9d-392a-8c5d-f2400022d12a | -8.9113 | -45.2062 | 2026-10-09 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 6009229d-5401-30d5-bd0c-f18ddc4d73ca | -3.0186 | -54.068 | 2026-10-09 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ef0f00bc-5d23-3685-ae6a-55d484341e70 | -8.7234 | -45.1355 | 2026-10-09 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| e3a300bc-7720-35eb-9c09-19d9cfb78f0b | -12.0251 | -43.4609 | 2026-10-09 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| e5c3158c-18d4-3628-8052-485db18b7776 | -3.364 | -50.4072 | 2026-10-09 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 27ca1f6f-eec0-3982-bb20-93a55e2e3357 | -5.7119 | -53.4658 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| fa0b95d8-8b6c-3836-bc22-3304380279ba | -5.6934 | -53.4667 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| f1856211-c778-3830-add8-7a1687fb8c60 | -8.6301 | -66.7886 | 2026-10-09 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 944751ed-0c1e-3a8a-9943-1de79ed9d313 | -7.2182 | -55.1416 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| bd6396d6-47b8-32b5-9550-e4a6833e15d0 | -3.9912 | -59.356 | 2026-10-09 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 02730df5-d3a8-314a-862d-013402f49241 | -3.1109 | -53.945 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 1a65e0b0-a081-322b-9872-83fb6ed13c55 | -3.3455 | -50.4078 | 2026-10-09 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 537d5e38-1000-3771-910f-ea1dc9f63b71 | -3.1108 | -53.9652 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 64c0aa1a-c92a-3888-8d19-c44d7ebc3a54 | -6.7363 | -55.1675 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e3a4833f-190a-3bb2-92ba-ab738bd38bb4 | -5.7116 | -53.5065 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| de601dc0-8043-34f7-98bd-f43579e78e0a | -12.2154 | -57.1287 | 2026-10-09 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9a9e2ccc-f75b-387f-abfd-3e5d81e33082 | -11.8692 | -43.5805 | 2026-10-09 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 6f9669ee-24bf-30ee-b956-179e587b97e8 | -7.2367 | -55.1406 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2caa7309-b67d-3784-b0e4-d4bb1c8bf8bd | -3.2057 | -58.8546 | 2026-10-09 00:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| b7892eb5-2cf3-394c-8b6c-464c008862e2 | -6.4903 | -62.8554 | 2026-10-09 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 94e25893-6adb-3231-ae7d-79a543ca11f6 | -15.4287 | -43.2373 | 2026-10-09 00:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 127.8 |
| b5492fdd-705a-3a17-b54f-e783feede396 | -12.2346 | -57.1071 | 2026-10-09 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 2b9a132d-2f17-3517-8a8d-5c3e13ff476e | -3.0925 | -53.9455 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| b9b6672a-fca0-3a2e-8a6c-a9936d8a99b8 | -11.4128 | -46.6897 | 2026-10-09 00:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| aab37c8c-4aaa-3ff7-81bd-9a8122cafdf0 | -7.2187 | -55.0815 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f9b35398-86d1-307b-b89d-faef0112969a | -12.2158 | -57.0887 | 2026-10-09 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 65c2b818-b8a4-3214-88c8-a312fea7196f | -7.218 | -55.1617 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 3006d580-e772-3d53-bcec-7266724a5403 | -8.7231 | -45.1583 | 2026-10-09 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.4 |
| ec52e68c-5842-3bf5-ae3e-6f2679dbca89 | -5.7492 | -43.8481 | 2026-10-09 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 9085848c-c084-38e3-b894-bd308cb522d9 | -5.9833 | -40.961 | 2026-10-09 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 131.7 |
| d9ac69ee-86c9-3b0b-b7d9-8556d3dc5996 | -3.2577 | -54.0217 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| cbf140a5-ca53-34a4-8e99-c2300f35438a | -21.69297 | -56.52402 | 2026-10-09 00:33:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 02f36d85-6145-305e-9d57-cc3775201465 | -17.83031 | -52.35664 | 2026-10-09 00:33:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| db395644-8e88-3904-b38a-168b1da98ac9 | -14.97434 | -47.54578 | 2026-10-09 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 34.3 |
| f9f4387c-c74b-3065-8731-6572c8ceaf04 | -17.82821 | -52.3435 | 2026-10-09 00:33:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 319d2188-8e86-3908-9690-2706a92e4dc9 | -18.28732 | -49.50655 | 2026-10-09 00:33:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| cc318b66-8aa3-3d11-9e23-f310b53dc383 | -17.84682 | -52.39347 | 2026-10-09 00:33:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ac12330c-2eed-3d0d-9125-fda5d7142c33 | -21.97323 | -55.93406 | 2026-10-09 00:33:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7b763874-f03b-3c74-8a47-cb495612e464 | -16.51394 | -52.58479 | 2026-10-09 00:33:00 | TERRA_M-M | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a9ea1a5f-6a85-30ed-8422-06939c0f19ea | -18.29086 | -49.52674 | 2026-10-09 00:33:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 297f173f-1870-37fe-89cc-fd65d0c37246 | -21.67639 | -55.11114 | 2026-10-09 00:33:00 | TERRA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6b943670-8fb2-3fc0-a8b8-019e3ec13cb9 | -17.17745 | -51.74657 | 2026-10-09 00:33:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2145c784-061c-3a0b-b2ab-0573c8b807d8 | -7.23191 | -55.08024 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 17def91b-cf23-395e-a9e6-c5bd7a23b84e | -9.90003 | -58.1236 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3e584703-0d02-339f-a3e4-1605e08c9108 | -6.20709 | -55.21412 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4ee664cc-d347-3389-a2ec-9b1fb6837e6d | -7.7556 | -54.95218 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9bf4a526-4773-380f-adb1-74101d232209 | -6.64123 | -62.91196 | 2026-10-09 00:35:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f030bf0c-1966-3a7e-bc20-4853e8a2fb1c | -9.49452 | -57.26048 | 2026-10-09 00:35:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a9e079d-9c20-37cd-a031-50b8b0afdea5 | -6.73968 | -55.14764 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 30716596-2b25-377d-9325-efe82b3a784f | -7.08194 | -52.67633 | 2026-10-09 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a2186bcd-6c32-3482-aaf1-56220f6f993d | -7.20517 | -55.1814 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dedaae57-6a90-30d7-b623-5e7c85c72c34 | -13.79234 | -52.80553 | 2026-10-09 00:35:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3cf7dc08-fbba-3ef8-a204-d554cfc306c4 | -6.85097 | -59.40357 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d72c390b-bba0-3f85-94a5-bccde26f6ea5 | -12.21672 | -57.09923 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| a257bfdf-bed6-32a5-ae23-360ce0ac3295 | -7.20346 | -55.16973 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 18ae8723-e268-3aa7-b897-3125aefcac6a | -10.53434 | -56.79226 | 2026-10-09 00:35:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9c5753fe-84ac-3bbe-9701-2f8b7876efec | -9.69102 | -58.09037 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 318e368b-f9fb-3d18-9bf8-e8e671b214a1 | -13.16753 | -54.35904 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9fd88165-5e72-3777-80d4-8e0d78bfca58 | -6.44864 | -55.04773 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| c7517f2e-5033-3c76-adcd-1de0ce0e8810 | -14.87993 | -50.30688 | 2026-10-09 00:35:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| e8bdf0d4-1592-3a1c-bd33-c3384e512e2c | -6.12226 | -55.69291 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4f0c384b-becc-3dbe-8336-12522d4f11f5 | -7.22353 | -55.09414 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 232c292c-c5f1-3fb3-b5e7-a31e05177211 | -5.99177 | -55.35743 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 105cfc75-53cb-3caa-88af-96d178e26117 | -12.11456 | -57.15741 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7a2bb011-adcf-3eb7-afad-7396090e2e67 | -7.19254 | -52.63461 | 2026-10-09 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f2970b1a-333b-3a03-9431-7b67949987b9 | -12.21163 | -57.12759 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2c967616-12f6-3a69-8df3-27276ceec005 | -9.25318 | -60.87732 | 2026-10-09 00:35:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| d1350f40-0d37-3d83-ba58-d5a94a627e0c | -13.20012 | -54.37668 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b76ebc6b-bdfd-3b2c-b484-6f2be67798c7 | -7.58251 | -61.54719 | 2026-10-09 00:35:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 6cb8d1fb-d8f2-33bc-a902-363a058469c6 | -6.511 | -55.40548 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 88ebf47d-1c24-381d-8ed7-7a2fc2bb8a75 | -5.71167 | -53.47005 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e6c0d658-068a-3636-a2f8-1c4049882ae9 | -7.21853 | -55.13123 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f690c482-a51a-3e4e-b636-dac580014520 | -6.10565 | -55.71825 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e09e7b07-38d7-37d7-ba30-16f715db1fd4 | -5.69989 | -53.47205 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 2777c808-bfe7-3b7d-97b1-a76495d1b759 | -6.53089 | -55.26398 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9af0e85c-2797-3207-bb21-a2d8ad5d4ab4 | -14.55925 | -50.03934 | 2026-10-09 00:35:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| bd284477-0ab6-3e07-b4ca-bc542af7424c | -7.22867 | -55.12981 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5d73d795-4b8f-3bc6-b483-afcd8421ba6f | -9.6898 | -58.08148 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 444c85b4-20ee-3cb8-a284-a67f255ce4b1 | -5.99536 | -55.37518 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 2ca18a22-4df2-3bd2-b973-4b0b83274913 | -10.01728 | -48.01808 | 2026-10-09 00:35:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 7e5de213-5a0f-38a2-a0a7-c3e13fcc4c60 | -7.18976 | -52.61646 | 2026-10-09 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 78d64cde-1c05-378e-a7e8-2ca459637aee | -7.17748 | -52.61867 | 2026-10-09 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 654dc53a-a7d7-3d16-9e06-33969b396bd8 | -9.61642 | -55.07922 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 49d71f2e-b190-344d-be8b-b26cf915d392 | -11.14353 | -54.80758 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 6f44989f-e709-3730-9197-2a2a2fd63d72 | -6.94702 | -59.36558 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fe6cfcf3-970c-3798-8c2c-48e649e028d4 | -6.51268 | -55.41709 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2be1a394-e9db-376f-856d-2923481ead5e | -6.50932 | -55.39384 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 45febc99-e379-310f-9689-c5b92347f005 | -6.74319 | -55.17173 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README36.md)
