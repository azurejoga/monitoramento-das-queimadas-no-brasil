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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4fb682a-6caa-3aa2-bcab-1879dae5c56b | -18.19032 | -48.37862 | 2026-09-21 00:18:00 | TERRA_M-M | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 11470191-62f6-3db4-8f9b-a95d6d78e218 | -17.55105 | -44.35351 | 2026-09-21 00:18:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| a5645f7e-0106-3950-be84-81d7137255fb | -18.54209 | -48.2014 | 2026-09-21 00:18:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1742daf3-84cc-3253-8855-8be40125b096 | -7.5889 | -57.6757 | 2026-09-21 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 604f95d1-f9d4-3d6e-9d73-351b10b11e65 | -10.6875 | -50.7722 | 2026-09-21 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c06d5cb3-7b08-3119-8471-6b05e8794216 | -10.485 | -50.3674 | 2026-09-21 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 4dae829d-afe3-3eb5-8435-ea248137911b | -6.2026 | -57.7778 | 2026-09-21 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0adf5ab5-cfbc-3420-95ec-4094aa3d4805 | -10.7624 | -50.8282 | 2026-09-21 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| feabea33-6742-31b8-9a96-c6d3ad3a5c23 | -10.7067 | -50.749 | 2026-09-21 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 78ef6c86-eee1-3c4d-939b-9b07be096c68 | -11.8014 | -49.8129 | 2026-09-21 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 8d417d5c-0176-357d-96ef-a4dcac863032 | -7.6075 | -57.6747 | 2026-09-21 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e498cbf9-f434-3bd0-b55a-003ddd777e01 | -6.7464 | -59.4223 | 2026-09-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| aa671d3f-9cad-3257-94f7-f75eacb499de | -6.4485 | -59.9909 | 2026-09-21 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 2da62fd4-f149-30ed-b9cd-15415d066959 | -7.5703 | -57.6962 | 2026-09-21 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 0d0c72a4-8b88-3997-bf63-b8d487181f4d | -10.7626 | -50.8069 | 2026-09-21 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 35343a74-7080-376f-aaaf-c665857d2fde | -4.3542 | -55.6455 | 2026-09-21 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6beff41d-53ab-374d-89b1-1407b2c9448f | -10.4853 | -50.346 | 2026-09-21 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 44d4f279-7335-3583-b55f-411fc0d70b23 | -6.8754 | -63.107 | 2026-09-21 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| d273283f-215b-3dd3-9b70-272462069901 | -10.7816 | -50.805 | 2026-09-21 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 9928568d-eaa0-3079-8505-b28f04b81fa2 | -7.5888 | -57.6953 | 2026-09-21 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| c96d3ba0-d4d1-3e11-b731-26e86d03af88 | -10.7253 | -50.7683 | 2026-09-21 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 5ee708d4-e10c-3dd0-a4ec-14b505c75ce2 | -6.467 | -59.9902 | 2026-09-21 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c11445a8-8226-3ff5-8978-321898a0a1f0 | -10.8285 | -50.1386 | 2026-09-21 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 10e2b5f4-5a56-31d2-bbd4-bb4a9751ef78 | -10.7813 | -50.8262 | 2026-09-21 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 98396642-84da-34ae-a1f3-075635b2e56a | -9.5593 | -66.0545 | 2026-09-21 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| b0b5262e-e7b5-30fa-8393-37fe0d621b1a | -11.041 | -54.1567 | 2026-09-21 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| aa93b743-ae17-3cdd-84ee-6ca3b11e80a6 | -3.753 | -59.419 | 2026-09-21 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 46305dfd-9097-3f20-9a21-efee1e88c426 | -7.5704 | -57.6766 | 2026-09-21 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 0a2d23fa-b28b-3169-8981-5d48eb9fd596 | -3.6946 | -60.5835 | 2026-09-21 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 424295f2-b714-3bb1-a597-e7f05c30928c | -10.8096 | -50.1407 | 2026-09-21 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| d05923a7-43a1-3fcb-9a9d-59d463ef28a0 | -2.8791 | -57.8184 | 2026-09-21 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| d635b75a-6f62-3ab1-a2e7-25d013dbdfe0 | -10.4664 | -50.3479 | 2026-09-21 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d14bd5a2-b563-38b0-a02d-2af73d6fe00d | -10.7064 | -50.7703 | 2026-09-21 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 252.7 |
| 74325bfe-b0eb-30b6-9e37-9bcdfe9ee938 | -5.2168 | -56.1096 | 2026-09-21 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 3a7857bc-bf16-3721-afab-f53fde3d44e9 | -11.0509 | -54.9106 | 2026-09-21 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| dac64739-6ba7-33b6-8417-65ee656a8bbc | -6.4671 | -59.9711 | 2026-09-21 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| c69f3c73-5bf6-370e-9d71-86739a864f19 | -7.2519 | -55.5994 | 2026-09-21 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 1d934779-2d34-3be3-bb73-158ff1dc8344 | -6.3195 | -60.0147 | 2026-09-21 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d24dbfea-cada-3c00-a8ec-68b315e98cae | -10.9112 | -53.9635 | 2026-09-21 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 06bc255d-6802-3cfd-b3f0-5a5a6220d971 | -4.3541 | -55.6653 | 2026-09-21 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f725c691-adcb-3e47-a078-561ee425ae1e | -6.4486 | -59.9717 | 2026-09-21 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 958e9cda-ef44-3691-a94a-b1c5334dd258 | -9.5594 | -66.0359 | 2026-09-21 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 5d74c336-67e5-3291-babd-3de5f0c8d7a9 | -7.5891 | -57.6561 | 2026-09-21 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e37f2c93-1bc3-34e4-aee6-eed1a89d8ddb | -2.8791 | -57.799 | 2026-09-21 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 50d63ad9-88d0-36af-a73d-97780f3e35f1 | -10.6878 | -50.751 | 2026-09-21 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 2831fe02-1421-355c-a528-acb8c04c5ff0 | -3.0717 | -61.2764 | 2026-09-21 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| e5ae26ce-9ac2-3c7f-b049-c92d9393ca5a | -5.7615 | -57.5807 | 2026-09-21 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 08131782-f76d-3372-8c92-8571cb62d30a | -9.69015 | -54.3542 | 2026-09-21 00:20:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d8bbebfc-4f75-339f-b9d8-63553a020806 | -10.38664 | -50.23815 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e0a6cd65-06b7-346f-ab71-325189f25789 | -10.54037 | -57.44661 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| ea27ce6d-6500-3c3d-9589-6afe3e209d27 | -11.93892 | -46.50735 | 2026-09-21 00:20:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| b94677fb-0c58-3de4-8590-b72efc6ddca5 | -10.34044 | -50.20812 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 173796a0-44a9-326e-ab49-4e640e805097 | -8.61252 | -54.62529 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cb867ebb-e516-3e71-ade0-6dce8f67a0a3 | -13.8737 | -48.59783 | 2026-09-21 00:20:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| fb565076-99b4-34d7-ad72-c2a57845d2d6 | -11.05487 | -54.90874 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 0c6e634d-661b-35a4-b3e5-c866646d2774 | -10.9256 | -53.956 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 39a53238-9680-393c-b61b-aece9719e1d0 | -10.90161 | -53.97766 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 17f54fe7-9fcb-31c4-9d81-d582ae7cb11d | -10.2215 | -53.91829 | 2026-09-21 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5ba5a69c-9136-3f13-9731-4ae4f4ba1445 | -12.31269 | -50.16918 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 27a69101-20d5-3665-b433-09c5473a63a0 | -7.41981 | -44.75333 | 2026-09-21 00:20:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 82bfae01-e306-34a0-8fc7-137978e3f18b | -10.88218 | -54.09892 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 696148f2-286b-3036-9aa4-9ff5d708b8bb | -8.18466 | -54.7345 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 4c77175f-6823-3d86-a226-e24d4ae06b7f | -15.45498 | -48.46501 | 2026-09-21 00:20:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| ca110a0e-60f6-37b3-aea2-94823af2de2b | -11.47163 | -47.77272 | 2026-09-21 00:20:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 4bf31beb-ea98-34a9-884c-0ffc5636e057 | -11.03444 | -54.14454 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| d872e9a4-53c6-30b9-b406-2eb7edcba2d2 | -11.79701 | -49.8041 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 3316a7ca-a727-3cee-922a-0fdef6d1bfbb | -11.03449 | -57.24576 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bbe2a6e5-ebe5-3792-ada5-3718775aa7c1 | -12.30595 | -50.67905 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4408ad74-2f90-3b2b-8ab7-79a7124cff65 | -11.03566 | -54.15351 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a9642085-489e-38b3-81b5-912ee7dddf26 | -12.02744 | -51.49665 | 2026-09-21 00:20:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 07ee07c4-17b4-3e49-a1aa-c4c05ac93425 | -10.38725 | -50.31205 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| aad12360-ae32-3f35-8bd4-6f25b9e4f591 | -10.38314 | -51.86683 | 2026-09-21 00:20:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 24f03358-e150-364a-bc4c-f2c1d4555043 | -12.54716 | -50.08949 | 2026-09-21 00:20:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d400b466-140b-3044-8118-e0cbb86c1849 | -10.85652 | -50.15892 | 2026-09-21 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7dd5f3d1-b9c2-3475-9aac-6ad7f85de829 | -11.75557 | -54.57293 | 2026-09-21 00:20:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 07a65bdc-ef38-3b2e-b3c4-5f1e9645eae6 | -10.86392 | -53.96485 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 17e97d39-7ff5-3a1c-98da-756df53edbae | -12.32674 | -50.68681 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| e6a51ae1-5db3-3e5a-8c57-7a7a7a1e5ac5 | -12.31871 | -50.69912 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 59c0c625-bdfd-32f8-aa52-c3ad4bdc4aef | -10.43294 | -50.34158 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| fdfd3dc4-e8aa-3b06-ab0b-96fa0b938e24 | -11.05361 | -54.89942 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c7ded3a4-f7e0-3238-809a-f78d90d1dc89 | -10.88398 | -53.98018 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cea680d7-c93c-340b-b4b4-23f07ab50452 | -11.80911 | -49.81483 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| d70ca2b7-632d-32ba-b3cb-5d3738bf8ddb | -10.21147 | -53.91066 | 2026-09-21 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a47d4ff1-d803-34fb-9a74-b6d553a955ca | -16.03726 | -52.52916 | 2026-09-21 00:20:00 | TERRA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b5bd5513-cf06-3021-8bf8-69fe5c8a797d | -11.03838 | -54.10741 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12505440-8ba0-3a57-beeb-a4c9081aaf3e | -12.32831 | -50.6976 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a10b668c-fc8b-3a6f-99b1-e300ad7d756c | -11.04588 | -54.90998 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 22ca8c80-6efb-330e-aa25-163d885ef1d1 | -8.19074 | -54.77896 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 57fe548c-12b4-33b3-8a6f-e973bb082303 | -11.22873 | -54.08621 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4985117f-4267-3bb6-9c37-50eda4a66ec2 | -9.96362 | -47.98013 | 2026-09-21 00:20:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 169c37b8-1a03-31ea-b4e8-fdb124ef117d | -8.79029 | -48.73315 | 2026-09-21 00:20:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 17.3 |
| e048dd25-cffd-3d5c-92bc-f3edb26875dc | -13.32803 | -51.30074 | 2026-09-21 00:20:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5feecd1d-3051-3280-869a-c79d09a6744e | -8.83487 | -50.48409 | 2026-09-21 00:20:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 9e68cc59-3ccd-35a6-b265-0a1128caedc5 | -11.27385 | -54.13744 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 325d9857-ec4e-3a5f-b851-9c089d0205e5 | -14.07603 | -52.08647 | 2026-09-21 00:20:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2bde32cd-ff0e-3cc2-859f-817064602af5 | -7.08495 | -46.2938 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a6e75304-91bb-34f2-a38f-bb3080f41a2e | -13.93626 | -47.84011 | 2026-09-21 00:20:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 7f619817-70d3-32a8-93be-87b9b3afc78a | -11.03321 | -54.13556 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| df012a20-b96a-3e5a-9b2f-64a57380c9f8 | -9.46443 | -54.92641 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 59811556-54c4-357b-938c-bd28aa58783c | -16.04311 | -52.98184 | 2026-09-21 00:20:00 | TERRA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 39.0 |


[Clique aqui para ver as próximas entradas](README3.md)
