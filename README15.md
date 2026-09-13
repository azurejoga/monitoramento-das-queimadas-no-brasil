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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65e881d8-1b3d-32be-b7f1-a01c7f80794f | -3.728 | -61.7555 | 2026-09-13 01:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 331247ed-923b-33eb-aa3a-504d4aaca85b | -9.1337 | -65.8253 | 2026-09-13 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d1d81d80-cf3d-316b-8cf5-ddcb3edd3c19 | -11.354 | -46.7874 | 2026-09-13 01:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| ef43fc26-be2c-3eee-b6ee-b6648c0adebf | -2.6785 | -57.531 | 2026-09-13 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 412ba7ed-7a0e-36d9-ac76-d6791423e2f4 | -15.5595 | -53.7845 | 2026-09-13 01:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 2f78c96f-8973-3950-915f-3ec18606834d | -6.6021 | -58.849 | 2026-09-13 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| bb28ba76-8a51-32c7-bd40-ff2b3528f065 | -2.6602 | -57.5313 | 2026-09-13 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 27f5fff6-5572-382a-89f4-64fd5e25eb3b | -2.6601 | -57.5507 | 2026-09-13 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 7d009179-f653-3022-bb64-919f83d5962e | -10.6824 | -54.1884 | 2026-09-13 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| c9e34767-9b24-3420-b59e-5d5d7328e75e | -8.5417 | -54.6985 | 2026-09-13 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3d9cc8cd-ecd8-36bb-8681-7cda564c394d | -6.863 | -55.5801 | 2026-09-13 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e4c29b40-f5f6-3923-9e03-89759fa233ff | -6.2832 | -59.9202 | 2026-09-13 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 87434d94-ef3e-3d12-a9f3-000cabe04b43 | -2.6784 | -57.5504 | 2026-09-13 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9c78859a-bade-3062-b2a3-3d6e3ba857f6 | -2.6785 | -57.5115 | 2026-09-13 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| af98dd54-83dc-3ac6-aee9-998f3efdc994 | -6.8445 | -55.581 | 2026-09-13 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 2e8b3e42-1c1e-30dd-9c30-48205f91b0c1 | -3.3293 | -42.2893 | 2026-09-13 01:10:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| fe035395-3699-3c72-bbd4-97dc291751e0 | -8.5415 | -54.7187 | 2026-09-13 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 892bfd3a-90da-3b29-9b18-96b84f749731 | -6.8632 | -55.5601 | 2026-09-13 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 7f3ee63d-19c7-3411-8c3b-163c8547ae48 | -10.5473 | -51.379 | 2026-09-13 01:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1da96625-7d2e-316b-bbb8-9cea6a4eb28a | -6.0915 | -57.8602 | 2026-09-13 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 168741dc-dab8-384f-bd34-f961918cf27d | -15.5592 | -53.8056 | 2026-09-13 01:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| d32c0375-2cb4-3bf8-a7e7-5261512ca253 | -10.7018 | -54.1458 | 2026-09-13 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e7e05b3f-92b1-3bf5-923f-4dc93706d34c | -10.69 | -54.2 | 2026-09-13 01:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85a3557e-a3ef-3da7-8169-51d7ffd8afb7 | -6.863 | -55.5801 | 2026-09-13 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 1a9c80e7-d34b-3d3f-be80-23ceb898d5c8 | -10.6829 | -54.1475 | 2026-09-13 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 6b6d8461-f0c2-3e4f-96d4-59d08043053c | -6.8445 | -55.581 | 2026-09-13 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 892bcfe1-3c25-3f61-b828-80183a513a5b | -6.0731 | -57.861 | 2026-09-13 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| abbfaf30-7968-3537-89cc-1c5b3b747b83 | -9.3951 | -50.1121 | 2026-09-13 01:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7c74394b-90cf-33ba-87c3-07e03dd1bb11 | -8.5417 | -54.6985 | 2026-09-13 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| bf20e06f-3630-3244-a0af-8fb378d044d2 | -10.7015 | -54.1663 | 2026-09-13 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 3b903001-7469-33c0-826f-86ef10c593e2 | -9.3954 | -50.0908 | 2026-09-13 01:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| abfa2688-aabf-3c62-8f24-cf39f61e9479 | -12.8543 | -44.386 | 2026-09-13 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| d519fe22-28b7-31c2-badc-6f0a027076bc | -10.6824 | -54.1884 | 2026-09-13 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| fd4711b1-6518-3694-bc15-49d567bab6be | -2.6601 | -57.5507 | 2026-09-13 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 929968c0-e212-317e-a208-8bb224552ac8 | -2.6785 | -57.531 | 2026-09-13 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9d461d26-21a9-3eb9-b147-686a13790702 | -10.7018 | -54.1458 | 2026-09-13 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 16efd9a0-bf1a-36cb-bd7b-d77605cde579 | -2.6784 | -57.5504 | 2026-09-13 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 51a96c92-a622-3934-9f2f-8ef4a839e91a | -6.1111 | -57.6645 | 2026-09-13 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 278e2842-fccb-3dea-9512-aa98814b0e82 | -6.0915 | -57.8602 | 2026-09-13 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| c0dc02de-a81e-31ac-80bf-e49df682895b | -2.6602 | -57.5119 | 2026-09-13 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| e60f3848-d6a9-347c-87e0-54b84641c68c | -10.6827 | -54.1679 | 2026-09-13 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 259.8 |
| c958a0ca-508b-34cf-8428-a5c5ed0ca982 | -2.6602 | -57.5313 | 2026-09-13 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| e1ba419e-aaac-3d41-9e43-fec6b5c62060 | -3.728 | -61.7555 | 2026-09-13 01:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| bc0afbbc-0d11-3a56-90af-54f36bccbb71 | -8.5415 | -54.7187 | 2026-09-13 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d9acdfa8-e2d3-3a5b-963f-8f4172d60707 | -2.6785 | -57.5115 | 2026-09-13 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 78c8e38c-6c6f-3592-81af-f725a8f644b7 | -10.6431 | -45.9999 | 2026-09-13 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 23afb072-1fe2-31fc-94aa-634840da6908 | -9.1337 | -65.8253 | 2026-09-13 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| c11a219f-247e-3f4d-a160-cd32ea59abe9 | -6.6021 | -58.849 | 2026-09-13 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5b41bb2c-8813-399c-a21d-0ea59934b0ab | -10.6827 | -54.1679 | 2026-09-13 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 3aeec337-c10c-31ab-8323-ffaa5325546e | -6.0731 | -57.861 | 2026-09-13 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| ecae26e5-bfb6-35af-9fcb-84abedee8566 | -8.5415 | -54.7187 | 2026-09-13 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b9a23e65-141b-37b2-974c-2301dabc545a | -6.8445 | -55.581 | 2026-09-13 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6a21ae9b-2508-3924-b601-2fb5c1210eee | -2.6784 | -57.5504 | 2026-09-13 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 846cfdb9-4f82-3695-927e-dac1fd2ebe0e | -6.6021 | -58.849 | 2026-09-13 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5e4973af-b3e6-3186-82e5-4b7dadb894ac | -8.5417 | -54.6985 | 2026-09-13 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| d81cb767-45bd-35cb-b886-5118ec6c9127 | -2.6785 | -57.531 | 2026-09-13 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 1d94248d-64df-3a18-b966-f3fba955ace3 | -9.3954 | -50.0908 | 2026-09-13 01:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e9517c79-bd04-319a-b132-b2668c591810 | -10.6413 | -46.1133 | 2026-09-13 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 579d2539-5619-3a3e-9167-4eed4b37baf7 | -2.6602 | -57.5313 | 2026-09-13 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 26.1 |
| bafbd91e-6aea-3202-aea0-dbea1157ff91 | -10.7015 | -54.1663 | 2026-09-13 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9d737824-e72b-3bd2-a65d-331888218629 | -10.6417 | -46.0906 | 2026-09-13 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| b0063178-46aa-3d0a-8071-467ad1beac47 | -5.1254 | -55.9748 | 2026-09-13 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 17e7a4b8-75ae-319b-96d9-6a8ae5f8f59e | -9.1337 | -65.8253 | 2026-09-13 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ad6a6f22-82a9-38ce-b4d7-034ed38704e3 | -6.863 | -55.5801 | 2026-09-13 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 72d89aba-cd4a-3e48-84dc-0461f6aa6c14 | -6.1295 | -57.6637 | 2026-09-13 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 50d3d496-27b0-3cc4-be50-9ee0c9801e80 | -3.3293 | -42.2893 | 2026-09-13 01:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 89cd0937-c033-3a31-92c0-2eecd9b6d823 | -17.6155 | -46.6607 | 2026-09-13 01:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6c5e5c08-bb8b-3105-bb68-9bda29e6c785 | -3.728 | -61.7555 | 2026-09-13 01:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8afe8dc1-aea4-32d7-9647-0f1da5a3978c | -12.8736 | -44.3828 | 2026-09-13 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| c6c8d6b5-afad-3d1d-8014-0b3af83f6094 | -12.8543 | -44.386 | 2026-09-13 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| cfb7319c-310e-3cd0-b27f-8892d98b6196 | -10.6829 | -54.1475 | 2026-09-13 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| c6fe1318-a61e-3c9f-bd16-ffd4ba5aa686 | -6.1111 | -57.6645 | 2026-09-13 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e50c00ad-3abb-3421-b6fb-0d29706c411e | -6.0915 | -57.8602 | 2026-09-13 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| ef46c1eb-13c7-3bfa-8784-fcd414fa38a1 | -5.8206 | -53.8052 | 2026-09-13 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| aceeb767-9162-35b2-8fe2-e4ebf9f96cc1 | -10.7015 | -54.1663 | 2026-09-13 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| e004d599-2f9f-37a2-8a80-be3f3f30b269 | -2.6784 | -57.5504 | 2026-09-13 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 0da8fedc-dd5a-31c0-9e45-3f557d6454ba | -10.6827 | -54.1679 | 2026-09-13 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 174.2 |
| fad5246d-15f2-33ee-8069-303f8b10a70c | -6.6021 | -58.849 | 2026-09-13 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b3b801d5-bd0b-3673-89a4-59719986a52c | -8.5417 | -54.6985 | 2026-09-13 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 03ec6f8c-4648-3edd-b7c7-978241714cbb | -2.6785 | -57.531 | 2026-09-13 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 91b1bbe4-075a-38de-8684-c829525c1bc2 | -5.8206 | -53.8052 | 2026-09-13 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 333b0b8e-c126-323b-9f06-047c0e879d41 | -6.0731 | -57.861 | 2026-09-13 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 8635f371-9801-311d-af0a-eca16c7d560a | -9.1337 | -65.8253 | 2026-09-13 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4570f884-4321-36dc-b97b-08452213548d | -2.6602 | -57.5313 | 2026-09-13 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 8b9a7630-1632-3a93-bd27-a7af01157afb | -12.8543 | -44.386 | 2026-09-13 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 3fbfa637-6f1e-3979-ad77-483783be57d4 | -3.3293 | -42.2893 | 2026-09-13 01:40:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 9e78bf17-a36b-366c-abf5-c16229ff3376 | -2.6785 | -57.5115 | 2026-09-13 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 648bae75-3e27-3415-8116-8eedfb3290a1 | -6.863 | -55.5801 | 2026-09-13 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 4e2b015a-2a26-3776-974f-6d0669d44512 | -3.728 | -61.7555 | 2026-09-13 01:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a11ce006-e287-3397-961e-cbbc1a5afd88 | -10.6413 | -46.1133 | 2026-09-13 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 70dbc099-318a-3c11-aabd-cd82a8207636 | -5.1254 | -55.9748 | 2026-09-13 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| cfc51489-e1b5-3c7d-b23b-80ead547737d | -10.6417 | -46.0906 | 2026-09-13 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 5c68d7dc-f22f-3aec-aa15-b9830200b8fe | -9.8992 | -47.5874 | 2026-09-13 01:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 170a1782-fa3a-3889-b28a-8458c84cea3f | -6.1111 | -57.6645 | 2026-09-13 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ee2e2022-1b4b-3440-8422-409d6ee9b598 | -10.6829 | -54.1475 | 2026-09-13 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| ba41cefd-fb9d-393b-b168-010b05038f73 | -7.73786 | -73.08313 | 2026-09-13 01:41:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ad49dc8-74c4-3425-8a53-59fe669e4275 | -8.75766 | -71.03723 | 2026-09-13 01:41:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33916c52-6f3d-32e1-addb-7c144db4723c | -8.75778 | -71.03088 | 2026-09-13 01:41:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 690e43d3-e43f-3673-ab10-869ab0572376 | -8.54899 | -70.86754 | 2026-09-13 01:41:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a3210523-e990-30cb-b7d4-42fc3102ad56 | -8.75602 | -71.02579 | 2026-09-13 01:41:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README16.md)
