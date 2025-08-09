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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d56c329b-1901-3ce8-9855-ee7a8cbdbbda | -11.79449 | -44.924 | 2025-08-09 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 52e00b82-e2c5-3a4e-8186-bb9ef662c63a | -11.10722 | -50.49427 | 2025-08-09 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 540e0617-32b5-3b50-94e8-e6254d413c29 | -16.25148 | -48.44938 | 2025-08-09 00:48:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5a62db9c-cf96-3aff-9a80-29f02a7bca2d | -9.05495 | -45.07174 | 2025-08-09 00:48:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bb4331d9-190a-3466-8691-81fe448cbc92 | -13.05216 | -43.86699 | 2025-08-09 00:48:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b4ad4485-3951-35c4-a4f0-5a1b4f527b5e | -11.7817 | -47.40011 | 2025-08-09 00:48:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2f0de711-4997-3846-9c1c-0561469f992f | -14.35968 | -47.10285 | 2025-08-09 00:48:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6a1e86fd-9167-3c96-9014-1bcccc46be50 | -13.55067 | -55.24841 | 2025-08-09 00:48:00 | TERRA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 30.3 |
| ad905d93-08be-333c-a66b-ce881743cada | -12.03561 | -47.52067 | 2025-08-09 00:48:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b5da4a6e-7add-321d-8e6f-ec8dc2f4ba03 | -13.55248 | -55.26369 | 2025-08-09 00:48:00 | TERRA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 3adf6665-f958-3817-8f1a-6d2f2a758903 | -11.92736 | -44.553 | 2025-08-09 00:48:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7f9b953d-6131-33d9-9eac-41f14848c44e | -11.32748 | -55.23098 | 2025-08-09 00:48:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b2e0cfe2-aa5e-3e78-be9a-2a81e6c4c5b6 | -13.04874 | -43.84654 | 2025-08-09 00:48:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 272.9 |
| 8eb50564-2951-3e16-96c0-d33ef0641553 | -13.07447 | -43.84186 | 2025-08-09 00:48:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d940a725-e205-30b2-9383-53be85b493a9 | -11.93682 | -44.53193 | 2025-08-09 00:48:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| a8e1b493-87cc-3474-a3a3-7eb0352e229a | -10.18427 | -49.50884 | 2025-08-09 00:48:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3d999e68-140b-3098-9cb6-357086278952 | -12.05228 | -51.88043 | 2025-08-09 00:48:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5fe8660d-e5f4-329e-9b74-4dca196ee75e | -11.10848 | -50.50328 | 2025-08-09 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 3d1cae52-cd3b-3cef-bd2e-fdada6092432 | -5.2262 | -46.0642 | 2025-08-09 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 00e574cc-7336-3581-9a4f-7fbf0eb495bb | -13.0386 | -43.8604 | 2025-08-09 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 0f1e5aca-93d4-36a6-bc42-58b3a6eeb374 | -13.0584 | -43.8333 | 2025-08-09 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| bacc1716-bb0d-3fb8-aec0-706894a8e02a | -19.8124 | -47.0634 | 2025-08-09 00:50:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 143.0 |
| f526106c-62ae-378a-ba66-912ef55b804f | -17.5093 | -50.3023 | 2025-08-09 00:50:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 07293ddc-afeb-3352-9966-2174c7c0bbcf | -13.039 | -43.8367 | 2025-08-09 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 7d9add15-bf6a-3696-a863-4385ef908889 | -6.5856 | -44.564 | 2025-08-09 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| fec22661-c410-3fa8-90d5-25547a27166f | -3.4255 | -49.0303 | 2025-08-09 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9c6aa0ee-d629-32cb-8660-f78e5d77dbd3 | -8.9401 | -60.7288 | 2025-08-09 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9241a316-0ad7-3b11-b331-83aebf039142 | -8.9399 | -60.7481 | 2025-08-09 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 441389df-be47-383f-813b-a3ddca2ebd7e | -13.058 | -43.8571 | 2025-08-09 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| b5c7f5c2-060a-3a30-bd1b-28edf0565346 | -5.2075 | -46.0653 | 2025-08-09 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 23628dd0-e68e-39d5-9182-6e599794721a | -17.5098 | -50.2801 | 2025-08-09 00:50:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 934966e7-05d7-3c20-857d-db8fa5ee4614 | -17.5296 | -50.2766 | 2025-08-09 00:50:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 38ffa5c5-543a-38c2-befe-f2196332ffc5 | -8.9213 | -60.7489 | 2025-08-09 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| b9c51703-a270-30bc-bf7b-ce7de7de488f | -3.4254 | -49.0517 | 2025-08-09 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 649bef21-9658-34f2-9025-67ec497a229f | -17.5291 | -50.2988 | 2025-08-09 00:50:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 248.0 |
| 1a177319-03d5-36b8-b980-ec2a47395fd1 | -19.8328 | -47.0586 | 2025-08-09 00:50:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 86a870e4-d985-36ff-887d-b4859ce15a47 | -8.9215 | -60.7297 | 2025-08-09 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9c66b760-9767-3697-81b6-15e57f637a2f | -11.9279 | -44.5569 | 2025-08-09 00:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| da30cb3e-fc27-3fea-a9fa-1f88b2d12940 | -7.07413 | -59.20567 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 7b4a69b2-3caf-3a8b-8f26-8021222a7d08 | -3.42444 | -49.03434 | 2025-08-09 00:50:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 496f7c4b-71ab-333e-869b-1bc002f03e6e | -4.8694 | -47.75689 | 2025-08-09 00:50:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 03865478-7c01-3f3f-9229-076d80cd9680 | -3.96744 | -47.87846 | 2025-08-09 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 91126664-58c8-38de-8a0d-741c08517d4d | -3.84468 | -47.74217 | 2025-08-09 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 44e6f09d-cb99-3385-8b97-d06447325e27 | -8.05971 | -46.33164 | 2025-08-09 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 936b2fc4-c539-3ccb-b779-e2c91a0c56a8 | -3.43636 | -49.04487 | 2025-08-09 00:50:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 935d2761-165d-38d1-8a11-3cb5323837aa | -6.05224 | -43.75048 | 2025-08-09 00:50:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| ff0524ea-32b3-31ec-abdd-2db41934c6c5 | -7.06837 | -59.15823 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1316.3 |
| 375400c0-38d9-3b17-91c2-ce9bc29af76b | -4.4766 | -48.11882 | 2025-08-09 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 463dbe44-8747-34f5-a3c8-b55e9e33dc47 | -7.05187 | -59.19072 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 606.6 |
| 8f7d4a9c-c346-3e2f-b218-6648eb9f0871 | -9.93833 | -60.50094 | 2025-08-09 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| a532a5d3-3ed0-3609-a787-055de7b7612e | -7.0881 | -59.20399 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 309.9 |
| e3b27d63-bba5-330b-ba01-6c300706e4c8 | -7.95751 | -49.39804 | 2025-08-09 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 092f3ea4-464d-3b07-8b55-ad534bd78843 | -6.63038 | -47.29489 | 2025-08-09 00:50:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 94961baa-faff-3f78-853c-de12b84bbb23 | -7.04891 | -59.16749 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 55f00483-33be-3550-9af7-f767dfbbddc4 | -4.4746 | -48.10537 | 2025-08-09 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 42c44ae9-a01b-3449-bc3d-5360e46dee9b | -2.6207 | -54.72803 | 2025-08-09 00:50:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 053d8481-eecf-35a4-86d2-98bab80eefb6 | -6.17358 | -46.154 | 2025-08-09 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dff74277-1125-376f-9a7f-fcb533d9f6aa | -8.93098 | -60.75916 | 2025-08-09 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 163.3 |
| f36cafd4-fbeb-38f2-9921-208596aab22e | -3.4279 | -49.05821 | 2025-08-09 00:50:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0d4e9597-9fd1-3bfc-b4cc-5c798397ee03 | -5.07911 | -48.31091 | 2025-08-09 00:50:00 | TERRA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 32b90719-c7cd-39db-ae0f-2544067c5372 | -7.07668 | -59.16362 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2178.0 |
| a4a7b133-4ecc-3c71-b8e8-5950f1366506 | -7.05493 | -59.21482 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 358.0 |
| 3dda942d-bdb2-3fca-9e99-5b78ad8b6e82 | -7.0658 | -59.18896 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1032.7 |
| f92bcb02-affb-32f7-8dce-e12824d3337a | -5.20393 | -46.06803 | 2025-08-09 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c8f75329-aebb-32c5-9182-4390b767337d | -8.04951 | -46.32312 | 2025-08-09 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 802e2114-dde8-3bee-98dd-05ded0b7d054 | -4.81797 | -47.3177 | 2025-08-09 00:50:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2d0fa4e2-8c19-32b8-a382-9badc88561dd | -8.93843 | -60.7516 | 2025-08-09 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 87a3dee6-300e-3ef5-a608-d23906f52bee | -3.42618 | -49.04636 | 2025-08-09 00:50:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5887214c-c25b-31d4-b4bc-02e03b64f253 | -8.92222 | -60.75349 | 2025-08-09 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 466cbd56-fceb-3c72-953f-32b1e8745d79 | -3.84674 | -47.75653 | 2025-08-09 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 3e900448-122a-3c68-96e9-591ca6dcc297 | -7.06306 | -59.23162 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c1af3a1d-9f73-3ac6-9c44-8cecebb2b069 | -7.05449 | -59.16021 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| f6f83dc8-048e-37bc-8246-9d9bbf8cdbb8 | -6.61933 | -47.29646 | 2025-08-09 00:50:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 80b70ca9-f495-39c0-a61b-e68dc0e7938a | -7.07975 | -59.18731 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1360.0 |
| 1495080a-bb6a-3f6f-b533-d7fc8c74b9bc | -7.11022 | -46.10859 | 2025-08-09 00:50:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| c04f084d-19e6-3194-9fb4-d1f8dd5ee3ea | -7.11776 | -46.11891 | 2025-08-09 00:50:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 13e4b406-27b8-3ebc-9f39-5c375cf66446 | -4.29502 | -48.06142 | 2025-08-09 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 7d95d830-0f01-3893-9414-b318bb6a90b9 | -6.06707 | -43.74822 | 2025-08-09 00:50:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| eb0dd0c8-253a-37d5-95f4-7dd9bf87ebff | -4.47133 | -48.11234 | 2025-08-09 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 357a6721-2a1c-37e0-9d13-ba8bb10f2753 | -7.08287 | -59.21134 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 204.0 |
| 6c7c8880-aa26-3c45-9739-450deac06730 | -6.58666 | -44.5942 | 2025-08-09 00:50:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 34839a98-5891-3390-8ba6-31cbf8ce2270 | -8.92675 | -60.72477 | 2025-08-09 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 77121858-311d-3e90-aa96-a873e0ff6dcf | -5.21915 | -46.08422 | 2025-08-09 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 9b634726-c849-36ba-a748-71fba6a84e81 | -6.57346 | -44.5549 | 2025-08-09 00:50:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7388fe2e-07ed-39d0-9896-cf75cf8b18c0 | -7.07122 | -59.18167 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2612.3 |
| c19a6c1a-803a-3241-9fd7-2529ddf15075 | -5.21639 | -46.06592 | 2025-08-09 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 667ed887-1dd1-35f6-990d-fcd3ea4a16cf | -6.57707 | -44.57831 | 2025-08-09 00:50:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 7e682007-2fce-32a5-aa71-5ec9c3220b49 | -7.09059 | -59.16183 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| cd8d3a97-5764-3502-8a52-cef45af24e27 | -4.87282 | -47.76481 | 2025-08-09 00:50:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a4ef5422-b4b8-39a1-b7d8-31dd990ec57b | -7.08515 | -59.17991 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 556.5 |
| dbd92d08-389e-3f6b-a7ff-8a9c61e79711 | -7.09683 | -59.20957 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| f0602f7e-7f7d-319f-9859-0c61700907bb | -7.0937 | -59.18562 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 6269e4be-47b0-322e-881f-db36a28c577e | -7.9669 | -49.39669 | 2025-08-09 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f4a9f703-71c8-3f9a-ab04-ca3dcba214c8 | -7.115 | -46.10123 | 2025-08-09 00:50:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 6897dace-2a60-3759-bdff-7d3c1fd61404 | -7.06281 | -59.16564 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 826.2 |
| df8a700f-3489-39ff-a3fa-06c5fa115d73 | -7.90759 | -45.55347 | 2025-08-09 00:50:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9ef0d7ab-c824-3e3f-a445-4710433c29b8 | -7.08226 | -59.15628 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 440.5 |
| ebb1453f-cbe3-3346-8c3c-b125dbc48b0a | -3.65245 | -48.32787 | 2025-08-09 00:50:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7bf6e94f-4b9e-3f25-b0c1-585c38f0b434 | -3.96945 | -47.8926 | 2025-08-09 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2f71afac-2711-3c30-a968-22beb43c6b31 | -4.29704 | -48.07507 | 2025-08-09 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |


[Clique aqui para ver as próximas entradas](README6.md)
