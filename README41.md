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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec55cd2f-db76-3af4-94c8-067b01538f34 | -2.18472 | -53.43688 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a07f777-af4b-3806-965b-04ccc0a34dfc | -2.17429 | -53.26023 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb25e6a7-1f3d-3a0e-9aa8-c1419fc96ec0 | -2.14867 | -53.35654 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47313c1e-665b-3cc1-bef1-9e036a0a6019 | -3.5459 | -53.02264 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca78f2e5-460c-3381-ba14-d349bc355e09 | -3.54368 | -53.01508 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a99e4e9-bc6d-30b7-a6fb-0dd5884634d3 | -3.5242 | -52.96545 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fc9f679-1370-30c1-86af-7701f2d78441 | -3.52252 | -53.55533 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3d97be1-d939-3239-8667-22faa6bc4f2d | -3.52248 | -52.82549 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc0f79f2-c194-3c7b-8b88-53e4e264ef3b | -3.52192 | -52.82897 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7599532-3929-30e1-af34-f7227c259edc | -3.51915 | -52.82497 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0393d6a4-77b0-35ab-afa7-73a63bc056af | -3.4784 | -53.29856 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13fea971-afa5-3645-95d0-21eb0cbcd8d0 | -3.46958 | -52.85944 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0238d062-6671-3d08-98af-03670c7ca994 | -3.4583 | -53.27351 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13ed04bc-48dd-3aff-a375-9af24c51bdc2 | -3.24094 | -52.8417 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58165d20-89cb-3b90-84b6-a51b93581662 | -3.07527 | -53.24571 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01d94e4d-caa5-342b-ae09-b1afab444b93 | -3.07415 | -53.25283 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5df3dfd5-cdd2-38a6-ba95-cdc8ffcbdcc7 | -3.07079 | -53.25232 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| af14d8ec-b209-386f-8abf-cdc750c65770 | -3.06855 | -53.24469 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3603ef2-7a03-31ea-be67-dd6b7a3d35bb | -3.06575 | -53.24062 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b94e4f5-c490-3739-b20e-8f266f09487d | -4.2943 | -53.71312 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16a29ceb-c8cc-33db-bc3c-316a4be92095 | -3.92658 | -53.6666 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f578099f-7e6c-3ce3-ad55-fb6f28f7d352 | -3.92601 | -53.67022 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab2d44ec-6a19-3ef2-b5cd-2ec0a1282e82 | -3.92262 | -53.6697 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91a86413-6136-3479-ba27-bad51ea0a931 | -3.91177 | -52.38715 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e8fb2b8-2ce2-35ef-b7ec-401989fcb386 | -3.88071 | -52.32182 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52c50ce6-cccc-31a9-a520-57c81b59cd2b | -3.88017 | -52.32526 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a03fd71d-7a2d-379b-820b-589fd60c0d67 | -3.87263 | -53.82973 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c682ce54-ea18-30a0-86f3-b2f477487abc | -3.79235 | -52.3891 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 751d97c1-6c0f-34e9-8181-068de1a1be85 | -3.79184 | -52.41372 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a5b193f-6b6b-3bda-b0de-9f50c7eb6a78 | -3.7913 | -52.41717 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29cd42bf-f980-3d47-8406-83f9748549cb | -3.78959 | -52.38514 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 272a762c-4442-33b7-8e82-57dd1bc905e9 | -3.78904 | -52.38858 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e5f6dae-aaa1-34a2-812b-e60a55fb46bc | -3.7885 | -52.39202 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8d1a80f-90ec-3795-a327-425e320a5fb4 | -3.78628 | -52.38463 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fcd19ab-4ff7-37ab-8299-b7afe29d5258 | -3.78574 | -52.38807 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c37ccbb0-181c-38e5-909f-a31118ddce54 | -3.76755 | -53.38414 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a0c7697-e0b4-3aaf-a840-6ad5bf90c05c | -3.73384 | -53.77104 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a80f7631-dd24-3657-8124-8123f024cbe2 | -3.72627 | -52.3752 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 771fe8e4-d716-3dd0-8d00-01ef8581bec8 | -3.66017 | -53.63594 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 990d04a5-bcd8-30e8-91dd-9efa59f61697 | -3.60744 | -53.70569 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0abec0e-c31b-3e26-a968-a1523da5e0d8 | -3.56475 | -53.75505 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21703fc7-1ac3-3248-86c6-fc77d644fecb | -3.56416 | -53.75871 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3a7490f-a475-3ba0-a7e9-43a798ed8bb2 | -3.56135 | -53.75452 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3da3b45-7480-3571-90ae-ba80ac40ea4f | -3.56076 | -53.75818 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3bc7600-9eae-3c13-8051-b1671d3e97f2 | -2.07745 | -53.5634 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 784939ca-51d6-30a3-9718-efb07ee8fe00 | -1.95307 | -54.75389 | 2024-10-23 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 475fdeee-2cd1-34d6-a204-1aebc2168c22 | -1.88637 | -54.58011 | 2024-10-23 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 671ea8fa-baaf-3029-9792-98cfbdec8e6d | -1.8041 | -53.69312 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc436985-222d-375a-be19-865d24e7976e | -1.75461 | -53.71621 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce00422f-0a61-3ea5-9b43-ac7003f0b40b | -1.75117 | -53.71568 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 730db9c1-830c-3697-92cc-61bc9d4640e2 | -2.13591 | -53.96809 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfd09285-5edc-3678-a182-a907634880cf | -3.10954 | -54.1632 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cd73aff-0e1e-3ace-8f3b-5ab9e1ba754e | -3.10548 | -54.16643 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b69216c8-72d6-3fce-93e3-c314f68e6415 | -3.10488 | -54.17021 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 37fd9ba2-1c4f-34f9-9bc9-ef1e48ec1d64 | -3.10261 | -54.16212 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 5fd5f1a3-c481-3070-9603-6a5084e3ce1f | -3.10201 | -54.16589 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 03b7e97b-1ae0-3944-aaf1-b34f14d111fd | -3.09855 | -54.16535 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85753672-7812-39be-982b-804bf65778f8 | -3.09734 | -54.17292 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdd50517-3896-342e-a9ff-385ffd3de993 | -3.09628 | -54.15729 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 772e293f-60d6-3905-9e68-e8d50d69079f | -3.09387 | -54.17238 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aefe8298-1e1d-3629-b6fd-c009825e5136 | -3.09254 | -54.97559 | 2024-10-23 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88812802-73aa-330f-996e-1ac41a5d2d6d | -3.09222 | -54.16052 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0cb41de-b5b2-3132-922c-9e02d2609d9e | -3.09161 | -54.1643 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dcea687-51a2-31ab-9c1b-893cc5106218 | -3.09041 | -54.17186 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7172654b-592a-3079-8131-f07f3a0a2d9c | -3.08875 | -54.15999 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81012e62-6f7b-3d1f-911f-efb6f838e7c0 | -3.08407 | -54.16702 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 025b58d5-90e7-3f2e-b68d-7b734ce172fb | -3.08347 | -54.1708 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3fc1693-126a-3b94-9959-adc320741756 | -3.08 | -54.17027 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 463b69be-f877-3631-81ac-947796984252 | -3.0794 | -54.17405 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2726df8-3499-3c10-b6ff-bc10650de841 | -3.07056 | -53.83421 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6821229-f70b-3792-bae5-e332b933fa52 | -3.06998 | -53.8379 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 115cb143-5286-3ea0-bf2d-8dcf98065901 | -3.05317 | -53.89972 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2f4d958-5565-3670-b210-91faddf1b38f | -3.05258 | -53.90344 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63a23747-a379-34a7-89ad-af8b28a6ab50 | -3.05033 | -53.89546 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 931d72af-5e64-3b88-91cc-3f8847694f51 | -3.05032 | -54.85655 | 2024-10-23 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11449a84-a621-34f4-9215-b0363dc552ce | -3.04974 | -53.89919 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2026e92f-ca2c-3d5f-9acd-38da76fcb53e | -3.04942 | -54.85536 | 2024-10-23 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 559ad270-72fd-3d0a-bda7-0d497e506db1 | -2.95061 | -53.70508 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19dbe5a0-790a-3a74-8463-d679158556a0 | -2.95002 | -53.70876 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f46bc5b9-fcff-3b96-9415-c89974e30bad | -2.94438 | -53.70034 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6deacbdc-bcba-3fec-95e1-6188df8939b9 | -2.90243 | -54.25344 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a834e4f3-3842-3a5c-9582-fb15c34fe07a | -2.89485 | -54.25621 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d64b3a5c-f09c-365f-98b4-0e8dc1121498 | -2.89137 | -54.25564 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2e75658-86d0-36f1-b796-4d21f3176a3f | -2.88497 | -54.11681 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a674390b-dc81-3d69-8fec-7285e5a64b0e | -2.8677 | -53.96333 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 378762bf-9176-30dc-a884-19dd1df7fd0b | -2.86731 | -54.47565 | 2024-10-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd598b0e-1191-3d31-8880-636d38d32e99 | -2.8672 | -53.96278 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06638b5c-c158-3e72-b9e2-dd485c085fe1 | -2.84002 | -53.98219 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4406deed-7f6c-3f6a-9246-a9a58147aebd | -2.83943 | -53.98595 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecf17f7c-9fb4-3799-a9fb-a1b04dfaed5b | -2.80567 | -53.95386 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1e45271-05dc-37ad-bc31-ce53a7055eba | -2.80359 | -54.78592 | 2024-10-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e66a4fc0-e6d0-3314-9164-d7d63bc2a4e0 | -2.77634 | -54.72751 | 2024-10-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bbb7d8d-bca5-3e6f-8a37-7668baa98dbe | -2.77277 | -54.72697 | 2024-10-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d9b9d31-d826-3f46-94c9-a4b83fa66f9f | -2.77213 | -54.73095 | 2024-10-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2509542-6e1f-37af-89d4-57d236367abd | -2.76074 | -54.03574 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 607cc855-edaf-3ac9-87dd-78f705275289 | -2.75728 | -54.0352 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f62645a2-c007-3144-b0fd-f7dcd07a00a2 | -2.75383 | -54.03467 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c88c5d79-a32b-30f1-9e71-a6eb1bf9f375 | -2.75037 | -54.03413 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f0ecd8f9-4cfd-3a1b-8a40-a0ee1e5e6ab2 | -2.73542 | -54.14895 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9952b25-9525-3f60-8802-1d78aad870a3 | -2.58152 | -54.01582 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README42.md)
