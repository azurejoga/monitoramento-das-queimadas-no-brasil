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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0efc8ead-00e9-3192-be7c-acbae2ad3855 | -6.8019 | -59.4008 | 2026-08-22 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a57b9f9e-bf59-3c4b-a7cd-dd3e1af4b9ef | -6.7833 | -59.4208 | 2026-08-22 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 2fa61859-b386-3bc1-9f0e-b1bf36d73ba7 | -6.8188 | -59.6696 | 2026-08-22 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3c84f443-d32a-3be9-88f2-f56e9a1bb340 | -6.8202 | -59.4194 | 2026-08-22 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b33a11f7-eedd-3e33-9334-4ad53139aa4f | -20.6358 | -47.4322 | 2026-08-22 05:40:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8c4e1ba5-8ef2-387b-85d4-706b35fd7f45 | -6.7691 | -58.6873 | 2026-08-22 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4c1b79ee-a043-37b8-9691-b1f742994387 | -6.8018 | -59.4201 | 2026-08-22 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 228.9 |
| 7e58751d-cc33-3994-afcb-d10114a7a84f | -8.3903 | -62.6963 | 2026-08-22 05:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 213.5 |
| ca2b2496-a6c2-3598-a1ec-3eca82c37600 | -6.8202 | -59.4194 | 2026-08-22 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| fff27d2e-1cfb-399b-b143-cd5020a529b3 | -17.9144 | -44.3976 | 2026-08-22 05:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| af08358c-d2c0-31b4-a4c0-24a0d237e734 | -6.7833 | -59.4208 | 2026-08-22 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 143.8 |
| d4123f52-7acf-3db6-b258-6c4e622d83b9 | -6.8188 | -59.6696 | 2026-08-22 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 3a49f340-1390-327d-8bd7-e5d574673eae | -8.5406 | -54.8197 | 2026-08-22 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e141f1ca-62b0-382f-b598-44b81a460d22 | -8.3904 | -62.6774 | 2026-08-22 05:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 249.3 |
| c5082d77-20a2-35b2-8ef2-af2381163b54 | -17.9137 | -44.4218 | 2026-08-22 05:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 04698131-65ef-3210-8c9a-b0828f0dc927 | -14.3744 | -51.8038 | 2026-08-22 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 7ea39cc7-06c1-31b4-989d-dc0d70c119d8 | -8.5404 | -54.8398 | 2026-08-22 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 6c385d57-9c08-3a33-9ca5-e6839f0f10a5 | -6.7507 | -58.6687 | 2026-08-22 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 67d35db4-fb93-3aaa-b0b2-a01746a7ff81 | -8.3718 | -62.697 | 2026-08-22 05:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 1a5ba2d5-133a-328e-a41e-e5c9c3758a7b | -8.3719 | -62.6781 | 2026-08-22 05:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0d2322de-99d4-3ddc-afda-2abc04c36513 | -8.522 | -54.8209 | 2026-08-22 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 83add19e-70b5-3173-b414-7195247ab46f | -6.8017 | -59.4394 | 2026-08-22 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| e58d9ff3-308d-3041-9f17-dddc9f153c26 | -14.3937 | -51.8012 | 2026-08-22 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 65209e3d-e381-3fa5-8488-7b956bce98d1 | -6.7692 | -58.6679 | 2026-08-22 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 4f0db28c-04d1-3fa6-9fac-4e017b3cfa94 | -20.6358 | -47.4322 | 2026-08-22 05:50:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 44.0 |
| c00c17c5-a77d-30d4-83a0-92468afbb644 | -6.8019 | -59.4008 | 2026-08-22 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 64129408-96f1-3baa-8bb1-ed1b038be04d | -9.1722 | -59.4629 | 2026-08-22 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 7b6e8368-600b-380c-aecc-207961112683 | -6.7832 | -59.4401 | 2026-08-22 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 5dd7cb18-3acb-3fdd-b8f9-893d095d6404 | -6.7832 | -59.4401 | 2026-08-22 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 492854f3-b9af-3509-8fb1-05801d9b5ef2 | -6.8019 | -59.4008 | 2026-08-22 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| eb682b15-fed7-3957-94a7-d4a6240a2efb | -9.1722 | -59.4629 | 2026-08-22 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 461b2359-4e2c-3540-b957-26b232b389f8 | -8.5404 | -54.8398 | 2026-08-22 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| aa72fb70-25b0-377b-9f7d-3135d5672933 | -8.3904 | -62.6774 | 2026-08-22 06:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 179.3 |
| 2738848b-de38-35bb-81ad-20963a46b0b1 | -6.7507 | -58.6687 | 2026-08-22 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2c59a2e8-332e-3194-afdd-1a5441fcc530 | -14.3744 | -51.8038 | 2026-08-22 06:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 2bbcd8d6-6518-387d-b5d9-98460e0145cb | -6.7833 | -59.4208 | 2026-08-22 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.4 |
| fbbe6615-909f-3768-89d7-8f46b92534dd | -17.9137 | -44.4218 | 2026-08-22 06:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 4599ee37-bbcf-3164-8be5-ae13332f56e6 | -8.3903 | -62.6963 | 2026-08-22 06:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 221.9 |
| 00b18bee-e1ee-3fa2-91c2-ee129b71c952 | -6.8017 | -59.4394 | 2026-08-22 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 2803c24c-2a8a-3fc6-b7d0-a3c143e0ec08 | -17.9144 | -44.3976 | 2026-08-22 06:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a01f5d12-ea25-318e-bc32-ecb9338ffd33 | -8.3718 | -62.697 | 2026-08-22 06:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 08a3cae1-c55a-36bf-b114-b7b69a2a1222 | -8.5406 | -54.8197 | 2026-08-22 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c7450f46-800e-338a-804f-cd16a767d7b0 | -6.8202 | -59.4194 | 2026-08-22 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a1f96834-17a0-3de8-a7eb-15507a2de7c3 | -6.7692 | -58.6679 | 2026-08-22 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 2ffc2b4b-5ca1-3c60-9d95-b64ed9665e8e | -6.8018 | -59.4201 | 2026-08-22 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 223.1 |
| 57297d91-dcdb-3e17-bb83-06cb6e36b151 | -6.8188 | -59.6696 | 2026-08-22 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8bcbba61-6ce5-3e1b-b6ae-8eb2cac8bc2e | -8.3719 | -62.6781 | 2026-08-22 06:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 511d1f39-e10e-3f44-9b0e-eb457eee16dc | -8.522 | -54.8209 | 2026-08-22 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9caf0c90-37b9-36c4-9906-023328760aea | -6.7691 | -58.6873 | 2026-08-22 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 813fdce1-8ed4-3964-9460-5e605105f65e | -11.60158 | -46.54617 | 2026-08-22 06:03:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 56e89064-02dd-3a48-b54f-1e97d23b95df | -12.75323 | -48.39789 | 2026-08-22 06:03:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 3f1d8cf7-4153-3130-a054-33702a53daa2 | -11.59798 | -46.54089 | 2026-08-22 06:03:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 236fabe7-8208-3c48-8275-252c878d014b | -12.26702 | -43.17247 | 2026-08-22 06:03:00 | AQUA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 088c98b1-c4ec-3659-8078-5343338c61d1 | -12.26583 | -43.16482 | 2026-08-22 06:03:00 | AQUA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 2acc2174-c075-3b32-8df4-12c09539fecd | -16.52182 | -42.12559 | 2026-08-22 06:05:00 | AQUA_M-M | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| bfeed32a-8489-38b3-9138-0265985a640e | -16.95226 | -46.11416 | 2026-08-22 06:05:00 | AQUA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 6ca34bf5-f1a7-3b4c-a709-4d062065fdd5 | -18.92055 | -43.58997 | 2026-08-22 06:08:00 | AQUA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| bbab45f7-4a63-346e-8e4f-3729ca2895eb | -18.27893 | -43.3126 | 2026-08-22 06:08:00 | AQUA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fef18cd0-0daf-346d-a96a-03605ef6fd4e | -18.08196 | -46.94449 | 2026-08-22 06:08:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 077cf664-f11e-3380-b0d1-1bcc37a69ea5 | -18.27698 | -43.32397 | 2026-08-22 06:08:00 | AQUA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9698da6d-5913-3825-a416-498c37b83f64 | -17.91793 | -44.38286 | 2026-08-22 06:08:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 551b1ff4-8547-3d86-922c-ba23065431cc | -18.0855 | -46.93764 | 2026-08-22 06:08:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| a34d4786-0b2c-3390-987a-44a29241d0a5 | -17.95439 | -42.72055 | 2026-08-22 06:08:00 | AQUA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 2698f58b-0276-3694-9580-6e6b9cda2f80 | -17.91539 | -44.39722 | 2026-08-22 06:08:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 8e389117-dbf7-3541-9e28-13065f90ea23 | -20.62521 | -47.4381 | 2026-08-22 06:08:00 | AQUA_M-M | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 5f6395ca-e3dd-3f60-bf68-9f015a030ee3 | -17.91282 | -44.4118 | 2026-08-22 06:08:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 250bec29-e9b8-3d12-9c7f-bead27119848 | -18.33876 | -42.46107 | 2026-08-22 06:08:00 | AQUA_M-M | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| aab33f98-9d5d-3b42-b794-60428413d0e2 | -17.96632 | -44.42152 | 2026-08-22 06:08:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 3477af5b-25fb-3cca-ac23-370bd9bf2558 | -20.46655 | -43.39229 | 2026-08-22 06:08:00 | AQUA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 9aa798cc-8d58-3cb6-bd50-e226e54c6167 | -17.95256 | -42.73161 | 2026-08-22 06:08:00 | AQUA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 316502ad-c1f9-3d5a-bd61-cd3ffd5fc786 | -17.91028 | -44.42613 | 2026-08-22 06:08:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d41e8c05-c8d3-3083-824c-784f8b49d33c | -6.764 | -58.70677 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe28c831-d05a-3b3b-8a77-fd0d9a425ea8 | -6.86164 | -59.03468 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4f4e9b8-6952-333a-8395-a95ea59fc271 | -6.93766 | -59.31065 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6bdb3094-108a-3ce8-bf8c-637728c56286 | -6.9042 | -58.99027 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b80d2d9-1293-3f19-a9a4-c2dc07fba5ef | -9.1046 | -60.91938 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6c9cf9ca-3841-3874-8caa-919f6d0c643e | -9.17995 | -59.45389 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f144c9e6-795f-3161-ac53-75a310158a5b | -6.54152 | -58.52288 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| aa8f8680-3e14-39ad-bac7-2a736c979851 | -8.40538 | -62.68308 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea648207-222d-3031-b710-ce9afbfdd7dd | -8.41037 | -62.68741 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c966d021-6662-3dd5-9710-a5537b6c9cd2 | -8.9025 | -60.59854 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1b22312-86f2-3ba4-bb16-9da29addae71 | -6.81513 | -59.38663 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| dad8c702-3b6a-3be0-85f9-6f2aa7824f3c | -6.76119 | -58.67436 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| eebd8c1a-9c5a-3f3f-b046-2acbb2571315 | -6.79824 | -59.41294 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| af64915a-efd1-3b4a-8621-692abb7cdc79 | -6.13577 | -59.89935 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a97dd3a1-92d6-3a91-a606-27d84c470fa0 | -6.80326 | -58.62309 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43dc33ac-b55b-3cf4-a2fd-d401b6cc2067 | -6.81579 | -59.42077 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 82f58984-c6f4-318c-8b16-fc874d1bff88 | -6.81946 | -59.40457 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a94d27a6-1eea-36e8-af7c-4e5d62286ae9 | -6.949 | -59.3106 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e15f8617-da3a-32b6-927c-b8a6b6ffae6d | -7.39662 | -64.63277 | 2026-08-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88a0f378-b6b8-3366-88c1-2956afcc1d87 | -7.59737 | -60.93819 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02d5c546-c00a-31c2-bd1e-f7fa6928f914 | -8.95788 | -60.59548 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3513e52b-bafa-3f9c-925b-d27e01632031 | -9.15816 | -59.46338 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e61f4fee-5a1a-32a5-8378-ff22b44c7266 | -6.76807 | -58.67529 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 52ee3b0b-ba8d-3c75-a0da-d324863718a8 | -9.17409 | -59.46475 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4c6c0ab6-d4c2-3772-9bf4-a6989dac1eb2 | -6.13 | -59.91454 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5a976fe-3f97-3197-9076-73f33080ec3b | -6.79412 | -59.59245 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 432389c7-5473-383a-8cec-403e0cb0267a | -6.80329 | -59.42547 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 8fa2883a-266d-3850-8699-e4612ce949d2 | -6.79595 | -59.43033 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 98a49aa3-acfa-3140-b87d-3562160d8b9e | -7.0236 | -59.55605 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README77.md)
