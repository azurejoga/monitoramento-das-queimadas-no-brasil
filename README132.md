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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a478874-7091-3015-9d24-16252d3bbb93 | -8.0278 | -61.3816 | 2026-09-20 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 943291cc-0e60-3a54-a9c2-8c37deba691f | -9.2567 | -46.2098 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| d176e30d-0a7d-3471-a988-24da4777ec69 | -8.0708 | -55.3321 | 2026-09-20 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 04683d00-f2db-310f-a029-01a014e8a303 | -9.2676 | -48.2472 | 2026-09-20 14:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6529d23a-c9a8-3306-8dd9-8c8294b42876 | -13.9448 | -47.8494 | 2026-09-20 14:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| e9761491-5dba-3d61-a96d-fc312ea8a887 | 2.2003 | -50.8981 | 2026-09-20 14:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 27be3546-fe1c-38fc-bde7-e7e02c322b80 | -11.4732 | -45.3635 | 2026-09-20 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| fc292977-1f8e-3de6-996f-a0d0d0639bec | -2.8974 | -57.7987 | 2026-09-20 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| a7d53226-c524-3a19-99c0-c37d123116d6 | -7.3259 | -55.6153 | 2026-09-20 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 213.0 |
| c2178b3b-4106-33d4-8d76-7b51e65d10ce | -11.1225 | -49.4601 | 2026-09-20 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 6036e435-d220-3393-ad3f-bb80f0df0f11 | -6.7185 | -55.0684 | 2026-09-20 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 7dda42d9-cce6-3767-a3a2-caa159ce7674 | -7.3289 | -55.2155 | 2026-09-20 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| bef3c68f-464b-3aef-bc61-a4886dd39fa1 | -10.8364 | -50.9479 | 2026-09-20 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 344.2 |
| 9206f193-5e7b-30d0-8ede-570f4c727a73 | -12.0076 | -50.0254 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b169803d-fe19-3425-9c86-113f6a71fdb0 | -7.0455 | -43.6928 | 2026-09-20 14:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 9b971a24-7097-3a9d-a4f0-a3a392ed5330 | -11.0614 | -49.7477 | 2026-09-20 14:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 172.1 |
| ce59551c-ec16-3185-bb79-089d6555b506 | -12.2344 | -50.1488 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| f7a9849c-3b50-3d68-96a1-ff1c239e829e | -6.3656 | -58.2966 | 2026-09-20 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 3da7fc25-7e6f-393b-a5fa-241566c251ba | -9.6202 | -45.8981 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 2445df39-243c-3a5f-b6c5-935cc2ba7f7d | -3.331 | -59.8292 | 2026-09-20 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e587703a-86b5-36fa-a313-0a8cc7d61c9f | -8.0706 | -55.3522 | 2026-09-20 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5af86142-ba53-3c77-9929-59b92eea3aec | -2.9143 | -58.3401 | 2026-09-20 14:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 69771a78-e14b-30e2-b767-2adc7619caf2 | -9.2865 | -48.2453 | 2026-09-20 14:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 2c5c7a0e-6a3b-3cdb-9f17-0483d48878d9 | -3.3492 | -59.867 | 2026-09-20 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 82898beb-f1e2-38c0-9d77-d6e76a9d58e9 | -8.4376 | -46.8757 | 2026-09-20 14:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 363e90d8-d69c-3ef3-8e33-5dcef50649be | -3.4049 | -59.5794 | 2026-09-20 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2635632e-8750-32f0-8e57-412820885075 | -6.8032 | -59.1693 | 2026-09-20 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 36aad0df-379d-3b54-8642-53eebaab00b4 | -9.0544 | -48.7469 | 2026-09-20 14:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 191.1 |
| 6763ad46-dd91-3722-91ad-a5da8f0d93b9 | -11.3612 | -51.3374 | 2026-09-20 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 74f5209b-922b-3506-9f8b-712f9dfcf184 | -8.0894 | -55.331 | 2026-09-20 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| fb1324dd-f58f-34a1-a589-cb9416448076 | -12.8053 | -54.0669 | 2026-09-20 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 44acd0ed-b9cc-36e5-97b3-8e06853ed0ea | -7.0098 | -45.257 | 2026-09-20 14:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 290b7b24-7615-3b7e-a5e8-a35e2451750a | -13.9641 | -47.8464 | 2026-09-20 14:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 113afabf-6bd3-39bb-b93e-9fcc03e36f61 | -11.9678 | -50.1379 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| eb25f612-d09a-3129-a7ee-be857a519b6e | -1.5858 | -54.4353 | 2026-09-20 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7c76b91b-474d-3b06-8e2b-97778c1e533d | -8.3581 | -47.2378 | 2026-09-20 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 22281b95-9123-376c-a0a7-23696b0ab470 | -12.6423 | -50.9144 | 2026-09-20 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 8f1c9ff6-b798-3726-8659-a029c82c457d | -8.883 | -45.9124 | 2026-09-20 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 0b732a28-899c-361e-a3cf-6dad2c06aa40 | -11.0506 | -54.9309 | 2026-09-20 14:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 323.9 |
| fb2149e4-9277-3987-a694-22f490d0d439 | -6.4301 | -59.9916 | 2026-09-20 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| be3a4460-90be-3bb2-a13a-86be26684cfc | -11.3621 | -44.0582 | 2026-09-20 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 333079e8-3b01-310e-9cdc-6d066b65ac19 | -9.257 | -46.1873 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 33fc2fe2-324c-32c2-b9cc-75c25b74cef6 | -10.9692 | -57.208 | 2026-09-20 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6227d25b-c80f-3b1f-bda1-cd1090811e30 | -13.9637 | -47.8688 | 2026-09-20 14:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 596220ce-4bf4-364b-809e-f750cdf11fef | -3.6947 | -60.5645 | 2026-09-20 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 168.2 |
| 0d468cf7-f897-3ad3-b857-133cdee9f9f4 | -9.0353 | -48.7704 | 2026-09-20 14:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 73171a2e-357d-3083-a691-8cd7ada97e5c | -3.6762 | -60.6219 | 2026-09-20 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 96719834-9d15-32fd-ae57-8395fa5e3905 | -8.1688 | -54.7432 | 2026-09-20 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 31c3b39a-c69d-3b8d-8d6b-c4255dcff997 | -8.1871 | -54.7824 | 2026-09-20 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 36494abb-ba32-3763-9cdf-b93daa648f21 | -6.3655 | -58.316 | 2026-09-20 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 41aacaaa-b748-34af-82ac-beab846155ff | -6.4486 | -59.9717 | 2026-09-20 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 438.5 |
| 7658f205-2d7a-3dcf-b674-f8abb7e2d56d | -14.0421 | -52.0812 | 2026-09-20 14:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f8a038a4-6f60-3add-8e48-e559c37cf5f0 | -7.1203 | -42.083 | 2026-09-20 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 79682f0f-ada3-3388-8489-29bed3c15ba2 | -9.8397 | -46.4361 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 346.1 |
| b59d6b73-1ef0-378a-a7da-e1e264c719a5 | -7.3564 | -44.4726 | 2026-09-20 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 08055a6c-5c78-3749-89ea-d10ad62cc51a | -3.4428 | -59.0996 | 2026-09-20 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 8597904d-c138-3b51-a14f-f73ef4adb77e | -8.4737 | -47.0053 | 2026-09-20 14:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 29792227-eb86-3a50-b756-6dfe5d2a6f4e | -9.2606 | -45.9164 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| d7320026-150b-3f3c-b786-65af95452f78 | -9.8313 | -48.4073 | 2026-09-20 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 150.9 |
| f5a3612a-5fed-3836-9272-c0505c77c48f | -9.8136 | -48.3218 | 2026-09-20 14:50:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c0cab195-eeab-3efc-843c-fd66450d9592 | -11.3417 | -44.1314 | 2026-09-20 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| d47636d9-d754-3f32-bca3-888132ab4778 | -8.1684 | -54.7836 | 2026-09-20 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ccbfbf5a-52dd-3eb1-87a9-529b178a4530 | -7.3073 | -55.6163 | 2026-09-20 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2e117aa1-a4f1-386b-9728-ad8cfa69d5df | -12.8701 | -51.0148 | 2026-09-20 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 8728d5f4-d5a3-30c1-851e-acf532bf9964 | -9.7154 | -45.8644 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8f546356-1f52-35df-bd47-821134013e7f | -2.8779 | -58.2828 | 2026-09-20 14:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 83f0783d-6837-303d-a9fb-956498e54dd9 | -6.2026 | -57.7778 | 2026-09-20 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c4ad794a-8504-3a6d-af3a-e1857f810c2c | -11.2149 | -48.3594 | 2026-09-20 14:50:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 450f7b40-7987-36b2-a349-b5ca49797b87 | -10.0975 | -45.6597 | 2026-09-20 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| a280dc60-c5e6-3284-b009-bbe7d1e5a91a | -3.3454 | -42.7597 | 2026-09-20 14:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 40c45e90-a92e-3e81-b144-d2741adab161 | -10.7466 | -50.5959 | 2026-09-20 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 193.2 |
| d180d3c0-dfe0-3f47-8a97-7f9aeba9aea8 | -5.9982 | -52.183 | 2026-09-20 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ebf764f6-0671-3ca0-9030-c881c00cd69c | -11.0259 | -48.2944 | 2026-09-20 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 65c1d060-40c6-3dd1-b88e-6bff538ba155 | -10.7842 | -50.6133 | 2026-09-20 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 953f9bf8-5148-3368-9752-99412d0f8ceb | -6.737 | -55.0674 | 2026-09-20 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 04af6f53-27e9-3434-9f73-bf4f16f19f66 | 2.2003 | -50.8981 | 2026-09-20 15:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a1ba6697-4772-3e3a-9fee-993abf42a351 | -4.0759 | -52.1259 | 2026-09-20 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| e00b177d-c951-3e7f-881f-4bedb263b35f | -11.1222 | -49.4818 | 2026-09-20 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| f15c224a-0672-353f-a4b1-8a1bd106139b | -9.8502 | -48.4053 | 2026-09-20 15:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 281.6 |
| 56d08a8a-484e-3d52-afd0-f96c278ed0dc | -10.9665 | -49.7583 | 2026-09-20 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| eefbac96-0a64-3c7e-9504-6f5a28e9cc63 | -11.9352 | -49.7752 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| af3a901a-3121-37a5-95bb-292bd0a56826 | -12.1516 | -47.0608 | 2026-09-20 15:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 4a975a5d-67f6-3949-954b-16b21ad46f6f | -7.5703 | -57.6962 | 2026-09-20 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| c64aeea8-3bc6-3f57-b3fd-7ca70574dc8a | -6.1839 | -47.5039 | 2026-09-20 15:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d4408962-9704-35a4-a4d8-1aac258f03ef | -7.2519 | -55.5994 | 2026-09-20 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 488cc39a-2aa6-3660-9eab-7ea5a0f0a081 | -7.0615 | -47.5265 | 2026-09-20 15:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ead6bca9-f9b1-379b-a89f-5b208a28b896 | -2.9157 | -57.8177 | 2026-09-20 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 38933f99-9ec0-3cd3-813c-b52d9bc211d8 | -10.41 | -48.933 | 2026-09-20 15:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| bde3c605-4420-3fa6-8f14-193b4ec5cbc4 | -6.3199 | -59.9381 | 2026-09-20 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 27c28928-234a-31c5-8146-483db8d674c8 | -10.8367 | -50.9266 | 2026-09-20 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 252.3 |
| 792b60d8-e187-34b6-9761-351484579362 | -2.8009 | -59.8957 | 2026-09-20 15:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 93034061-3a6f-3a96-9fbf-98e6af8d777d | -10.4541 | -51.2827 | 2026-09-20 15:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 70637c90-1dbd-3707-b2bf-cb0f5faaff53 | -2.9143 | -58.3401 | 2026-09-20 15:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 122.6 |
| dd63a28d-b037-3dd5-9779-880cddb3ef00 | -12.0454 | -50.0424 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| ab38509a-8439-3f02-be63-3a050e2a3b71 | -2.8975 | -57.7793 | 2026-09-20 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a19db803-da9a-359e-8cb6-69911e71f0ef | -2.9326 | -58.3397 | 2026-09-20 15:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5d985222-8441-3116-a918-5e81f8082f2c | -9.6205 | -45.8755 | 2026-09-20 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5b920b30-b475-315a-89b7-ba08e85c0841 | -11.2149 | -48.3594 | 2026-09-20 15:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6e8ab942-2ca9-3fde-a842-1d4179853b97 | -6.595 | -45.4953 | 2026-09-20 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1d4e90fb-bbd1-3939-ad7d-3acabaa1d47f | -8.0706 | -55.3522 | 2026-09-20 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |


[Clique aqui para ver as próximas entradas](README133.md)
