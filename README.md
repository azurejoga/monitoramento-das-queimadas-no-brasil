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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23e0972b-ec63-3bb5-a204-97805336530c | -15.9077 | -56.233 | 2026-08-31 00:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 41031fbc-00e3-3dd9-8bbf-fac38067b0c0 | -6.2537 | -55.4308 | 2026-08-31 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| d540dfe5-f99b-33db-b8a1-ed4874e93c3d | -5.9451 | -57.6906 | 2026-08-31 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7c69461c-c7b5-3e53-abc8-ec65a22d6271 | -18.3108 | -52.6569 | 2026-08-31 00:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 7db3cfdf-1fe0-3d3f-bd3b-dad595df1dfb | -18.2908 | -52.6602 | 2026-08-31 00:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d9b4c39c-1a66-3f9d-81a0-d44bd1fe55ff | -5.871 | -57.7715 | 2026-08-31 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 1daa91b7-edb8-3575-abbc-5695dc056539 | -10.7407 | -54.0401 | 2026-08-31 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 242610e9-3e74-3d80-ba95-c5eeca4632f2 | -10.7596 | -54.0384 | 2026-08-31 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6606d7b7-d415-3e27-b3c2-5019a21fddef | -14.1831 | -52.8667 | 2026-08-31 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| f296de1e-132e-3ada-b4aa-481f2910c1aa | -6.6036 | -58.5972 | 2026-08-31 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5598ad35-1724-3210-8369-6af2f1587829 | -12.9212 | -45.9041 | 2026-08-31 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 83ce8ad2-0490-3f62-ac9a-b47a105b8fae | -8.799 | -62.4905 | 2026-08-31 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| cd174383-0599-3678-abf0-2355fc96b1f7 | -5.2547 | -55.9105 | 2026-08-31 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 431.2 |
| aab6dbee-79de-32fe-9f1a-5f326e96a6c2 | -4.9604 | -55.8424 | 2026-08-31 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a5d76c8c-7a5c-3e97-9610-1e96b1b99dae | -6.9361 | -55.7157 | 2026-08-31 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 07ebb11c-5b51-3460-830d-974ac2c7c7d7 | -14.6064 | -54.0921 | 2026-08-31 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| dda0b149-2bc9-36e0-a8da-0b3e8fb9bc11 | -18.2904 | -52.6818 | 2026-08-31 00:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| ab9004f2-10dc-3a8d-84a3-ed5de4398acc | -7.6251 | -55.2987 | 2026-08-31 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 05327740-1b68-3005-93e6-e574579bc495 | -7.7034 | -63.3249 | 2026-08-31 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 18516993-ffef-3db3-9ac6-02d0ac13ab2d | -10.781 | -50.8475 | 2026-08-31 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e3121eb6-3820-3591-b6a8-9bbdb70f14f2 | -7.3118 | -60.5897 | 2026-08-31 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7cb52e5a-31d6-3f2b-99cd-83fd1e261c3c | -5.598 | -43.9978 | 2026-08-31 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 337415bd-983d-3189-b0d8-b810793327d9 | -14.6061 | -54.113 | 2026-08-31 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| bd84e1c7-c49d-36ba-bca4-095fe2e77b43 | -5.2363 | -55.8914 | 2026-08-31 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 8d8ffef1-e505-3cd5-ba58-6071bb0bd37c | -5.2546 | -55.9303 | 2026-08-31 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3bbb6297-35cf-39d8-a41e-6d1e58d654c5 | -5.2731 | -55.9098 | 2026-08-31 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0ef44802-b00d-3940-8cb3-411085550a5d | -6.9367 | -55.636 | 2026-08-31 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7abeac1b-bcf4-3978-9bab-72d4e51e91e4 | -8.9481 | -62.3704 | 2026-08-31 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e49c710d-3fb0-3c6a-b4a3-484e57148336 | -1.6042 | -54.415 | 2026-08-31 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 58b81061-6b94-3346-9240-c31207ef42c3 | -4.85 | -55.8266 | 2026-08-31 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 0b2b7c80-9c08-39e7-a489-9c71b22733a2 | -6.9363 | -55.6958 | 2026-08-31 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 10f263ff-7209-3dbd-a136-e2e427808525 | -19.154 | -57.3978 | 2026-08-31 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.7 |
| f9529a1f-fdae-3038-a190-ef3987bb0298 | -7.5321 | -55.3241 | 2026-08-31 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 22b786f1-e713-3f81-a8f2-4f9ff68cf8a8 | -7.3302 | -60.589 | 2026-08-31 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 123d5bb8-8b7c-39bc-b8bd-6354a22f496a | -5.2548 | -55.8907 | 2026-08-31 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 276.5 |
| d9b02958-3b77-3858-8e2a-37d508d23443 | -4.1515 | -60.7068 | 2026-08-31 00:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4a8308c4-1383-3dfc-83f6-a7ba4d4637a6 | -5.2362 | -55.9112 | 2026-08-31 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 768cbb1c-f123-39d8-905e-4fa6949d8f56 | -7.532 | -55.3441 | 2026-08-31 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2349d222-e428-3e70-94db-6f6a7592bee6 | -8.799 | -62.4905 | 2026-08-31 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 41442737-e07b-34ab-a584-2dc52bc1994e | -4.1515 | -60.7068 | 2026-08-31 00:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7356f59b-c115-3569-8ac6-cfc5d5fca36b | -10.7621 | -50.8495 | 2026-08-31 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 900ff3bb-06d3-34c8-b954-0e3c83e6e69a | -6.9367 | -55.636 | 2026-08-31 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 16ca3028-aa22-3dec-836f-1761e4092718 | -14.5868 | -54.1153 | 2026-08-31 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 4ffdb22b-c384-3204-90a9-7f84f7c08e67 | -7.3301 | -60.6081 | 2026-08-31 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 90837162-9187-3021-86d4-6b0270d9ffa5 | -15.9077 | -56.233 | 2026-08-31 00:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| f1c9edf3-eec0-34f5-ad68-1fa6b1dbd938 | -7.532 | -55.3441 | 2026-08-31 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| e7d6f4ca-f2ee-344e-b169-f148a3b10af8 | -7.7034 | -63.3249 | 2026-08-31 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d729a623-cf4d-3dbb-8ff0-b6c23e661019 | -5.871 | -57.7715 | 2026-08-31 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2a739460-ba1f-3c08-a9d2-a536b5d19f5a | -14.1831 | -52.8667 | 2026-08-31 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 40cf46d4-f691-386a-b603-902d0e2668db | -6.2537 | -55.4308 | 2026-08-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 184f3b11-14c9-3e1c-b389-2ffce4648e0e | -10.781 | -50.8475 | 2026-08-31 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a1d380df-f197-3e7f-a48e-5a7616468807 | -4.85 | -55.8266 | 2026-08-31 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 25d48a9b-20b4-3878-9a01-f1a374f3595a | -14.6064 | -54.0921 | 2026-08-31 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 6202ab04-7c11-3aa2-9351-c816ac88a182 | -5.9451 | -57.6906 | 2026-08-31 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| cfa37d6a-3172-394a-85bb-df73312f048b | -5.2362 | -55.9112 | 2026-08-31 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 8b304d07-7a78-32d9-892b-148be144b493 | -8.9481 | -62.3704 | 2026-08-31 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 6add1686-f20f-3da5-bdd1-1a0eeec290e1 | -5.2548 | -55.8907 | 2026-08-31 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 255.7 |
| 7101319c-8562-3ff7-98d0-306181f4853b | -10.7807 | -50.8688 | 2026-08-31 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e3cbff9e-f813-3514-a0e1-a4225bad09d9 | -14.5871 | -54.0944 | 2026-08-31 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 02a26949-ef2c-3f41-ae62-87fc4a3d6122 | -11.0936 | -51.5134 | 2026-08-31 00:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 410591aa-e3bd-3c02-8fa4-db004e5e8617 | -19.154 | -57.3978 | 2026-08-31 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 38a8e579-57d8-3c4d-b1fc-ca27afc26807 | -18.3108 | -52.6569 | 2026-08-31 00:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 21df0325-af11-3104-b01c-5807cfb3ab3d | -7.3302 | -60.589 | 2026-08-31 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 207d0f0d-979d-3254-9a80-72c01458c227 | -5.2547 | -55.9105 | 2026-08-31 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 419.0 |
| e105ba5c-a269-34d7-9bb7-6120be6e7fa4 | -15.7676 | -49.9555 | 2026-08-31 00:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 13665444-ff34-3f3c-8c3f-905178f97b73 | -14.6061 | -54.113 | 2026-08-31 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| de42e894-35fe-39c5-8c60-211c5e084fe9 | -18.2908 | -52.6602 | 2026-08-31 00:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| f14d5560-7683-3bad-9e87-199650b59fb5 | -5.2546 | -55.9303 | 2026-08-31 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 417cf547-451a-37b4-94d6-0a469ecd869f | -18.2904 | -52.6818 | 2026-08-31 00:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 7f80ca5b-7a53-3985-93e7-f9917fab1851 | -6.6036 | -58.5972 | 2026-08-31 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d01e0da0-cbce-3e91-b01e-8f3b2657d4d1 | -14.1828 | -52.8878 | 2026-08-31 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 9930e554-7b67-348a-8ac4-bcc4fc363929 | -15.908 | -56.2125 | 2026-08-31 00:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 7370dcc1-b307-363d-ba6e-ecd7d3fc8dd1 | -10.8022 | -50.6752 | 2026-08-31 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f4be433c-2547-3f54-adee-c594aa9474a7 | -10.8212 | -50.6732 | 2026-08-31 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 705a5945-eadd-36b7-a737-9f17f7459346 | -10.7596 | -54.0384 | 2026-08-31 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8e3f0c96-1f86-37c7-9a1c-ba892e06f8e1 | -12.9212 | -45.9041 | 2026-08-31 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 30648f94-5d10-306c-aa0c-90d9cd8fe0d0 | -10.7407 | -54.0401 | 2026-08-31 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 74053dd8-6702-311c-ba01-c7fdbfd3e5e3 | -7.5321 | -55.3241 | 2026-08-31 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 234d5694-b68a-3a37-a2d5-b038ee789e1c | -5.598 | -43.9978 | 2026-08-31 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 563e3187-9155-3aca-85b9-3c075e62d2e8 | -5.2363 | -55.8914 | 2026-08-31 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 0d519ba8-abcc-385d-ae45-e462d0165764 | -8.2272 | -49.045601 | 2026-08-31 00:11:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9465e071-735d-3f4c-9f4f-2123aa6ae392 | -10.5715 | -50.369801 | 2026-08-31 00:11:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a5d9199-5412-383f-bd99-3e4d118022cc | -11.1837 | -55.0914 | 2026-08-31 00:11:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd246188-12ef-3ef1-a1a5-874f50a7f718 | -7.5237 | -55.337299 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4141a352-27c6-3cfc-9186-f924b2289e14 | -5.8724 | -51.7188 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27ebc051-3fdd-3702-aa25-9e61fabe67d7 | -14.4439 | -52.5345 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7636cdca-2d10-393a-80c5-20f287daee1b | -11.9164 | -45.0653 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06a216d3-847e-35fe-ba50-fde911725abb | -4.9603 | -55.824299 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7b714cd-a32d-34db-8959-10732508cd9e | -9.6757 | -46.553101 | 2026-08-31 00:11:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0148f11e-972d-3746-8e44-88d19740ba64 | -7.6215 | -44.926201 | 2026-08-31 00:11:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e05179ab-a6fb-3167-9a0b-3d1826fd1ac2 | -5.2511 | -55.891399 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff59653-5586-3f5a-be15-ecfcc8f3b347 | -15.3627 | -52.690601 | 2026-08-31 00:11:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1d507dc-b06b-38ec-b09d-72ca37de7c5f | -11.4964 | -50.3218 | 2026-08-31 00:11:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afcbcada-c5e7-3b01-a128-25a822e690f9 | -15.4255 | -52.698601 | 2026-08-31 00:11:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6deb61af-4c1a-384e-bc2a-0d4d30ff94a1 | -8.101 | -45.470001 | 2026-08-31 00:11:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 760ec75d-4181-3a27-9b16-3a32956f8794 | -15.9172 | -56.2089 | 2026-08-31 00:11:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a93b4a4c-a186-3da2-9d92-3ab0448e26ef | -11.2206 | -45.091801 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f91b45a-6da5-326a-8ac7-a0f2af9c3261 | -10.1449 | -45.737202 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8b1fe46d-a267-377d-bae7-10b4b7ac85c4 | -5.862 | -57.540699 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5ba0e36-6e02-30ab-ab32-cbdc64740803 | -12.1294 | -47.260601 | 2026-08-31 00:11:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
