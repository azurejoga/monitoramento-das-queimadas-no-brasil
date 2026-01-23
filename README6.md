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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fe046d9-76d8-3612-89a5-f2e43f8fd583 | -20.34036 | -57.86733 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 0446d89d-d3a6-3b32-9aae-f0fa8b5fc2d8 | -28.5451 | -54.22642 | 2026-01-23 04:40:00 | NOAA-20 | EUGÊNIO DE CASTRO | RIO GRANDE DO SUL | Brasil | 4307831 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 92eebf2e-44f6-3e60-8c75-7b9bd4d03957 | -30.09764 | -51.10788 | 2026-01-23 04:40:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| d618da3c-5085-3cd4-aa7a-ee6f27cc21ae | -25.72041 | -51.59185 | 2026-01-23 04:40:00 | NOAA-20 | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4f807cb5-db7f-35c5-982e-e58beb337ba5 | -29.88417 | -51.2171 | 2026-01-23 04:40:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 3483cf9d-bb8e-38e4-9c97-9e22342707f3 | -27.09469 | -50.52686 | 2026-01-23 04:40:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 25d53f94-8f18-3381-8376-2b9a9babf8b3 | -31.61614 | -51.40825 | 2026-01-23 04:40:00 | NOAA-20 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 25c65d80-ce01-36ef-a59e-84ab68cbf2f2 | -27.56265 | -48.65818 | 2026-01-23 04:40:00 | NOAA-20 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bf0f2f97-23cf-3b4f-a77e-ffda2d5b00da | -27.09817 | -50.52745 | 2026-01-23 04:40:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 387ddd8d-d9b4-3acc-95d7-ec5cc8c1e867 | -28.10946 | -55.02452 | 2026-01-23 04:40:00 | NOAA-20 | ROQUE GONZALES | RIO GRANDE DO SUL | Brasil | 4316303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 216a11f9-02f6-3017-8008-af43c12b63aa | -29.88928 | -51.23149 | 2026-01-23 04:40:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 573cba97-1b75-334e-a6d8-a06c0757db9c | -10.1058 | -36.1748 | 2026-01-23 05:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 42.6 |
| 456509d3-d6a6-371a-9462-465ef813f2e9 | 1.13167 | -60.52618 | 2026-01-23 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9fb9205-e249-3b9f-b7d5-63a77321a5b6 | 3.35266 | -60.10885 | 2026-01-23 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca9feb49-4691-3a23-a375-7b66030f3cda | 4.40662 | -60.60206 | 2026-01-23 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7a291cd-2374-3eee-9dd8-25f94e1573fa | 1.29033 | -60.42505 | 2026-01-23 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e77ce19-6ff9-379c-a423-4946ecbda3bf | 1.69095 | -60.35613 | 2026-01-23 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2bdd702-bd77-3892-8089-2a46465d3773 | 1.13504 | -60.52566 | 2026-01-23 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ea2d86a-4f9a-34c1-ab92-8be36362ffe7 | 4.4337 | -60.61697 | 2026-01-23 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 128c0ca6-1602-36e0-8d90-da265df5c002 | 4.4077 | -60.60141 | 2026-01-23 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d946e228-b18a-37c8-91a5-624fadfcc479 | 4.32323 | -60.44373 | 2026-01-23 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9c3420f-f29d-349b-bd29-73422f11e79e | 4.76488 | -60.28048 | 2026-01-23 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8c5c0e36-dd5e-3664-8170-d934970f1460 | 1.13392 | -60.51847 | 2026-01-23 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a162b36-209e-3983-9d2e-b5248250ce37 | 4.32666 | -60.44312 | 2026-01-23 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdb077ca-f974-3321-9b88-a58c306acd8c | 3.35493 | -60.10111 | 2026-01-23 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01b18d17-8d85-39e4-8460-6fb010dfced9 | 4.27303 | -60.64082 | 2026-01-23 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0b95c06-68db-32ec-9a83-0ddedfc82142 | 1.28753 | -60.42913 | 2026-01-23 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb58332a-ff64-32c8-af73-2e17675f2138 | 3.35988 | -60.54644 | 2026-01-23 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f14c139e-6a06-33a5-b747-e9dcddca64e1 | 1.28697 | -60.42557 | 2026-01-23 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8eefa7ee-2f8f-37c0-ad7b-5bef1b9d4f24 | 2.51529 | -60.98827 | 2026-01-23 05:22:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82ee8b1f-7fcc-3be3-8900-20137fbcecb5 | 3.35091 | -60.10884 | 2026-01-23 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3c03995-3ed0-3585-b367-230bf982f58a | 0.8354 | -60.47683 | 2026-01-23 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0af44719-f8b6-3767-891b-db221d9fd654 | 1.12659 | -60.5275 | 2026-01-23 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c978567b-2973-39d5-9306-4d8f5e43db49 | 3.3521 | -60.10524 | 2026-01-23 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95934410-4cb0-3e21-8dfd-0425492273eb | 4.40078 | -60.60254 | 2026-01-23 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c64ab091-d4d7-3582-81cc-e3508d1404b4 | 4.42388 | -60.09746 | 2026-01-23 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6af1e54b-9ff7-3e11-91ee-ba8e209739b3 | 4.00973 | -60.909 | 2026-01-23 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2281c00-2e22-39ac-aa50-a4703459c291 | 4.40424 | -60.60199 | 2026-01-23 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a1ff3df-09a6-32e9-816b-11c696e92ecd | 3.61571 | -60.36017 | 2026-01-23 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5026e7e-815f-3be7-9826-ce59996cbd9a | 3.3177 | -60.07324 | 2026-01-23 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 465a4d01-ddce-3c27-97cd-adc96520aed8 | 4.27594 | -60.63668 | 2026-01-23 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43461b21-6d5f-34d8-a21f-154c7d54cd50 | 1.41468 | -60.74662 | 2026-01-23 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60b47796-216b-366e-8412-e5f9ad80476d | -2.09145 | -53.51423 | 2026-01-23 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3d9608f-3a46-35b9-9041-41daea54ece3 | -2.09081 | -53.51836 | 2026-01-23 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 179d9c07-e54b-3d32-a18a-1ffed57b8a8c | 4.91962 | -60.28301 | 2026-01-23 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f18fba06-6831-3486-aaff-a34fce9e82c3 | 1.28472 | -60.43323 | 2026-01-23 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acd04d57-615c-3556-b061-450d79cf787d | 4.27246 | -60.63713 | 2026-01-23 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e336ee4e-aa89-3a03-a0dc-aef8efafc7b4 | -15.59657 | -59.29517 | 2026-01-23 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e59daabe-ce70-37fc-a4a3-c9eba91d45c7 | -15.77852 | -59.1431 | 2026-01-23 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4306eea3-b843-3b48-b6d6-a7de850ab301 | -15.41636 | -56.29719 | 2026-01-23 05:25:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe346916-c4ae-3b9c-ab95-ad0f3d205ce1 | -15.60022 | -59.29575 | 2026-01-23 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c385bdf5-0f72-3342-8254-71719fe84558 | -15.77482 | -59.14258 | 2026-01-23 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d790aee-4ea0-31ef-811b-4cfa0cd1d334 | -15.96578 | -57.58063 | 2026-01-23 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01e350ec-238d-3ca2-b68f-e0f510cf3045 | -24.00216 | -52.56203 | 2026-01-23 05:27:00 | NOAA-21 | ARARUNA | PARANÁ | Brasil | 4101705 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 57459811-a11c-3083-8c18-8ac21d205211 | -22.02553 | -56.33962 | 2026-01-23 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c901b0e0-05b5-391b-8277-d6ef985099e1 | -19.67807 | -56.86825 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 17820a2e-badd-3844-b785-f69cc3d065e3 | -20.37702 | -57.87541 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 72f4d492-7b8f-3e8d-9523-15fb9c13c5f9 | -21.19416 | -56.92793 | 2026-01-23 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c8b0467-73fa-3fa8-be47-14108b8cc9c6 | -16.26338 | -58.3208 | 2026-01-23 05:27:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 56e76396-5112-3c76-a870-4345587eb144 | -20.33515 | -57.86527 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4468da91-08e1-358f-9754-55b97f0fdcb6 | -19.6691 | -56.86702 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 596e6891-23f4-3908-8d93-846dc731539e | -20.36108 | -57.86468 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 79709702-c917-3010-af0f-d8d72790e8ec | -20.34413 | -57.86229 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 0fcb916c-b07c-3f71-93b1-b90cfd152da9 | -16.26465 | -58.31708 | 2026-01-23 05:27:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2b4f6b3f-0a3e-30b4-b06a-cb1efab2772f | -18.30715 | -54.57879 | 2026-01-23 05:27:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10928eec-8457-3246-87f8-ff9315bb52b1 | -18.31229 | -54.5793 | 2026-01-23 05:27:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dbcc4c8-b3ab-3738-8c0d-6e1f336faf0d | -20.34463 | -57.85811 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e135d7dd-e70d-3356-9e21-c6ab76fdb943 | -22.59934 | -54.92699 | 2026-01-23 05:27:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8f49cdc3-7284-3a24-9390-a71a51a56e06 | -16.44847 | -58.16576 | 2026-01-23 05:27:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| bf499d1e-48ea-3ded-b324-b098e7ecc0ba | -19.32562 | -54.02783 | 2026-01-23 05:27:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ed0579e-3cfc-3ea1-bd15-3296e4d093e0 | -19.67058 | -56.87074 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 927a1598-0789-31c6-a855-53f41f28a96c | -20.38447 | -57.88494 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 3dfc1e2e-5881-39d7-b971-735bbf88e0b4 | -19.17833 | -57.54601 | 2026-01-23 05:27:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ff567729-557d-3fa5-966d-46cf2ae2cb31 | -20.37279 | -57.87482 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7eaf6dc6-ac57-38eb-9a65-4aa919a4f8eb | -20.38498 | -57.88077 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e1d5cf6b-3145-3d09-8259-5a508c57c2fa | -20.33091 | -57.86467 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 12bde900-913b-346e-8796-c91da8a48d2d | -20.36482 | -57.86945 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 98556ae5-9955-360d-9800-dca0afb32a73 | -19.67506 | -56.87134 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 670eb203-514a-38e1-8e98-4474f97c5076 | -21.7791 | -56.28363 | 2026-01-23 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 980bca93-bc2b-3e1e-9967-b012492925cb | -18.31194 | -54.58238 | 2026-01-23 05:27:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8e225f0-ed15-3c0b-87a1-dcac5b22a4f5 | -19.68201 | -56.87357 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 8bde3c8f-2386-3b0b-ac9e-b98f5f4e6772 | -19.67563 | -56.86664 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f99e492c-dbb1-3d41-92cb-60a4bf3ed611 | -19.68505 | -56.9264 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e3550b63-d4a4-3592-9b3a-8b1ae78391d1 | -20.33939 | -57.86587 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 83dbe660-87d1-30db-89f7-50eb434951f1 | -19.6865 | -56.87419 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 8123112b-d65b-3143-9f81-4e6567725a08 | -19.66857 | -56.87173 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4dfcc329-e2f9-3c08-844e-023029a9a7fc | -19.68112 | -56.9211 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8250b26b-f0c0-369a-82b2-5ff26cdf0e6f | -21.5362 | -57.53893 | 2026-01-23 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 134567d2-b859-33bf-91d0-9a3128b65a19 | -19.6661 | -56.87013 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 719c986a-89d5-3d96-a2f7-5bed45e78b7d | -19.17461 | -57.54085 | 2026-01-23 05:27:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e45bf7bc-b983-35af-adc2-4d8c15da187c | -19.68596 | -56.87889 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| caade1a9-ccf3-3bc4-9bb1-adfc3ed62794 | -21.19818 | -56.93335 | 2026-01-23 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afeda9c1-32f9-3b37-973d-afdf9de9ddc9 | -20.38075 | -57.88018 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7729879f-85a6-3052-b019-8bad61383d35 | -22.02076 | -56.33885 | 2026-01-23 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da302bfd-426c-3b38-806e-0b2b3e325c11 | -19.67359 | -56.86764 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c8c28c10-110d-310b-a44d-4309853a78d6 | -19.45501 | -53.98626 | 2026-01-23 05:27:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c60257cb-7e8b-39cd-a62a-dd64ba204fb2 | -19.66409 | -56.87111 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cd65b3d0-ce8f-30f9-9b77-16d622da49fc | -21.7839 | -56.28418 | 2026-01-23 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4515d43-2f95-35cd-bd3b-a157e50d911e | -19.67954 | -56.87195 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 748e340f-1712-38b0-a706-da8fc76f8751 | -19.32524 | -54.03143 | 2026-01-23 05:27:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README7.md)
