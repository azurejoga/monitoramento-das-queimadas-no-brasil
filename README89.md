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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d2f8164-4da3-3062-8292-3892c62b2caf | -9.02621 | -65.71167 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a5c85413-23f5-3da8-902d-c1ca40088939 | -8.61414 | -62.6025 | 2025-08-24 06:59:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c6d2ffa9-34c3-3b91-87db-77c5656fafd6 | -9.20206 | -60.78928 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| c954539a-ed62-3f6f-aaba-2e76ffcbae08 | -14.65062 | -56.56371 | 2025-08-24 06:59:00 | AQUA_M-M | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b94f3c4b-1679-3bc5-b04a-0ef92c2ae654 | -9.00526 | -63.62966 | 2025-08-24 06:59:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d6fd0627-d224-3234-8a7d-88828d730de1 | -10.41983 | -64.42701 | 2025-08-24 06:59:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 46767d8c-0433-3a80-aefa-08b49a3197c9 | -9.15536 | -59.45538 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 0029e43f-7819-38cd-9f9a-6982d346afbc | -8.99945 | -65.69683 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3063b12f-0983-3f2a-9712-364be7487b67 | -9.04515 | -65.71465 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f511fa1f-7bb6-3943-be8a-00e3f1c58c57 | -9.16556 | -60.80919 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2346c45f-f1de-38c6-94fd-20875eaf65cf | -9.0151 | -65.38017 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 224cf607-0507-32da-9a5c-164ca3317587 | -8.88642 | -62.39595 | 2025-08-24 06:59:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6c3d5407-d170-38e2-80d3-26c1850fac7e | -9.00892 | -65.69828 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| e29e63ba-9450-351a-befe-24b146658261 | -8.63236 | -62.62015 | 2025-08-24 06:59:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2b9e0635-c127-3af0-8367-e7d3f36bd319 | -8.91034 | -62.41783 | 2025-08-24 06:59:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 29da66c3-8eff-374a-9b3c-ab17f4b1e3e5 | -9.14501 | -59.45391 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| b1567256-31d0-3383-9c4c-fe0c98c45f80 | -11.99237 | -61.0224 | 2025-08-24 06:59:00 | AQUA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| bf266846-1d21-312b-bd14-216c6223ecd3 | -9.15863 | -59.50675 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 39e10ef5-2300-35da-8862-48cef8a0c73e | -9.65044 | -59.63778 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 42eeef6a-2d1f-35fb-8a06-147735ba8bee | -9.02001 | -65.68946 | 2025-08-24 06:59:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 790bac89-01e9-3630-a8ee-b54bd6af72c0 | -9.16217 | -59.48183 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 7225e3ba-15ad-3321-afd1-f706e8b45bdf | -12.58741 | -60.35049 | 2025-08-24 06:59:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5bfdd5c7-9117-394a-9fb1-820d4f3a9b69 | -9.15359 | -59.46796 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d6248361-e509-3fb1-89cf-20be1de01dbf | -9.15183 | -59.4804 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 5d835581-b213-3f63-bc10-0daaa3f15b86 | -9.81524 | -64.26335 | 2025-08-24 06:59:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1c521353-f5b2-3ea1-ac6a-a2be34769d0b | -12.58576 | -60.36269 | 2025-08-24 06:59:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ae7c9023-0507-3149-87dc-9aa1f6da1e7f | -9.15007 | -59.49285 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 86dafd65-d74d-3850-adc8-f1127aada1e6 | -9.1321 | -60.77293 | 2025-08-24 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fde67cc8-c812-38ff-9b74-e340f3c7ed03 | -14.8157 | -47.9118 | 2025-08-24 07:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 076a9e5d-de95-37fd-9b2d-ceeef393d65d | -17.6176 | -44.298 | 2025-08-24 07:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 27980d95-e76e-3f6f-882c-66cf0be959f5 | -9.0232 | -65.6982 | 2025-08-24 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a84bc7b6-3098-3639-b7ac-6d18e4ccb9e7 | -20.3599 | -51.68 | 2025-08-24 07:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 96f5870d-d74d-3c28-aa67-2eb9037f1858 | -14.8153 | -47.9343 | 2025-08-24 07:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 0ac00461-89b2-39b6-90b2-bd173404ad1f | -20.3396 | -51.6839 | 2025-08-24 07:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 9cbd19c8-02e8-3740-b266-a3adc1187a5a | -21.0607 | -49.0283 | 2025-08-24 07:00:00 | GOES-19 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.8 |
| 582e022b-2490-3d68-b33d-3b3e51a58f11 | -20.3594 | -51.7023 | 2025-08-24 07:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2383a4bc-8344-361d-9ccd-f905ebf5c599 | -9.1536 | -59.464 | 2025-08-24 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 8eea4432-336f-3b46-bb84-8a0eab55264f | -9.1535 | -59.4834 | 2025-08-24 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1c3f890c-9cd1-393c-b230-37ce4425469a | -18.9418 | -47.9294 | 2025-08-24 07:00:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 170caa41-a570-365a-a17c-609d6293b39e | -9.1536 | -59.464 | 2025-08-24 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e74b1521-5745-3226-ba05-7b5b6b030042 | -9.0232 | -65.6982 | 2025-08-24 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 373df04e-6b57-39a9-9f03-0a4c5b998636 | -20.3594 | -51.7023 | 2025-08-24 07:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3f860aa9-9185-3f06-ab4f-747f3aa45cc9 | -9.1535 | -59.4834 | 2025-08-24 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8dc269b8-68ce-35fa-98de-65ae163f13ae | -20.3599 | -51.68 | 2025-08-24 07:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 60a10db0-e4eb-3e69-85e0-f6f6393b963f | -14.8157 | -47.9118 | 2025-08-24 07:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| ea699349-10d0-3cc8-ad26-f31c2847abfe | -17.6176 | -44.298 | 2025-08-24 07:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| bfaf065f-9b97-3a5b-a258-bf315cba6f66 | -18.9418 | -47.9294 | 2025-08-24 07:10:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 656b7d25-9cda-3c5c-aa21-7235e452b911 | -20.3599 | -51.68 | 2025-08-24 07:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 70f230d5-7b2b-3f13-851f-807c0cd7f585 | -20.3594 | -51.7023 | 2025-08-24 07:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 2ced0f87-b4f7-38fe-9254-8231ba92c3fb | -9.0232 | -65.6982 | 2025-08-24 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ce8561a1-8017-3246-aa22-aaabd7b7f824 | -9.1536 | -59.464 | 2025-08-24 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a78ee404-fe14-35e3-a297-f2c02d9cfa69 | -20.3396 | -51.6839 | 2025-08-24 07:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 5ce82af3-a675-3720-8016-af40d69cb7ab | -9.1535 | -59.4834 | 2025-08-24 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9aa19838-897c-3103-b982-e5cb415497a0 | -14.8157 | -47.9118 | 2025-08-24 07:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| eab014aa-ce9a-39f0-b467-a6dd29783c77 | -20.3599 | -51.68 | 2025-08-24 07:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 33faa0b7-c3cf-3b8c-b331-c348413ea715 | -9.1536 | -59.464 | 2025-08-24 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e428f9f1-2402-3b99-966b-b81ee99bd9c6 | -20.3396 | -51.6839 | 2025-08-24 07:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 83064220-6bec-3e55-b297-ddb786c5e38b | -20.3594 | -51.7023 | 2025-08-24 07:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 4d99854f-32b5-3daf-98cb-3094aa3ca15c | -9.1535 | -59.4834 | 2025-08-24 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c0c7d386-3ae9-3fc6-af27-980daa964258 | -14.8153 | -47.9343 | 2025-08-24 07:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 7e67bc5c-32d7-3d3e-8e91-908c152b891b | -14.8157 | -47.9118 | 2025-08-24 07:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a3b81c9f-6bbf-3988-a4c0-850f866d8d11 | -9.0232 | -65.6982 | 2025-08-24 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9dd4512e-2d82-3f53-9e00-8796c748312f | -18.9418 | -47.9294 | 2025-08-24 07:40:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 40.3 |
| a4c416c9-e9ca-31f4-a4a4-7571bd76be12 | -9.0232 | -65.6982 | 2025-08-24 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8cfb447b-506a-3865-bc01-0acfbace1516 | -14.8157 | -47.9118 | 2025-08-24 07:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c00dc23a-be62-3e83-9ca2-830927dc72de | -9.1536 | -59.464 | 2025-08-24 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 26ae4b5f-a280-3840-8293-9334ef489721 | -20.3599 | -51.68 | 2025-08-24 07:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 100.9 |
| ac742462-c7e0-3f25-9784-db2aa45691b5 | -9.1535 | -59.4834 | 2025-08-24 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 4c4bd71a-8fd2-36c2-902d-27e4928e25aa | -20.3594 | -51.7023 | 2025-08-24 07:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 66.7 |
| adb6d38c-8377-39fa-b688-d6da58ffcd3c | -9.0232 | -65.6982 | 2025-08-24 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 5d24c918-6c08-3a2f-a205-d389a03ab917 | -20.3599 | -51.68 | 2025-08-24 07:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 6dccfd8f-fc89-378b-ad73-d95cbf1f07f6 | -9.1535 | -59.4834 | 2025-08-24 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bf4f7dc0-eb60-33a6-9568-ebbf8e77b7f8 | -20.3594 | -51.7023 | 2025-08-24 07:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 7e3500ee-be57-3b81-9750-4c65349d4f20 | -14.8157 | -47.9118 | 2025-08-24 07:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| de19e72e-ab45-37a2-895c-325402a3f7cf | -9.1536 | -59.464 | 2025-08-24 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0e664d55-f08b-3782-9fd0-fbf7dd44c2ff | -21.0607 | -49.0283 | 2025-08-24 08:00:00 | GOES-19 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.4 |
| 9d886b55-cbf0-38d0-b4a0-b31ef2415715 | -14.8157 | -47.9118 | 2025-08-24 08:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| cdf70257-9147-30d9-bac6-b5cd2b3117f6 | -14.8153 | -47.9343 | 2025-08-24 08:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 096b8c36-6d5a-341e-89a9-d52d5f6a56ea | -9.1535 | -59.4834 | 2025-08-24 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| be6396f5-2c1e-3e25-acaa-59490d087f14 | -9.1536 | -59.464 | 2025-08-24 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c8d9989f-211e-30c0-b0c9-f014f76ed6a1 | -16.4138 | -49.9379 | 2025-08-24 08:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| df8e604c-58c0-3cef-a3dd-08c788606ffe | -9.0232 | -65.6982 | 2025-08-24 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8ccb4343-71b6-3607-a5e5-7894eb6d505c | -20.3599 | -51.68 | 2025-08-24 08:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 38b4d8bb-9229-3397-9b67-990db969a74a | -20.3594 | -51.7023 | 2025-08-24 08:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 908bac93-b1e6-35b4-8aa9-949516907479 | -16.4335 | -49.9346 | 2025-08-24 08:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 2cb053be-a717-3642-8e11-56628ec9ccfb | -16.4138 | -49.9379 | 2025-08-24 08:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e830ab3b-42fe-37ec-85eb-ac6c2360de94 | -9.1535 | -59.4834 | 2025-08-24 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| aa4e1964-85f2-355d-bc9e-29eb8561b8c6 | -9.0232 | -65.6982 | 2025-08-24 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f8553618-c8eb-324f-b092-3dbaea84ac3a | -20.3594 | -51.7023 | 2025-08-24 08:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 640f3cb4-63f3-37c9-8c24-cf55758aa16d | -14.8157 | -47.9118 | 2025-08-24 08:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 1ef94c3b-f035-338b-9b00-8ef070a0030f | -9.1536 | -59.464 | 2025-08-24 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b6d17b23-3865-3b67-89cb-422c4791bb43 | -20.3599 | -51.68 | 2025-08-24 08:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 97.4 |
| e792b639-553d-3f23-8a30-5b13a98897e2 | -21.0607 | -49.0283 | 2025-08-24 08:10:00 | GOES-19 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| f28199fb-46f3-39d3-83a2-95ff0339a881 | -14.8153 | -47.9343 | 2025-08-24 08:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| b9914148-c917-3233-8b7a-cc43cdcb1943 | -14.8157 | -47.9118 | 2025-08-24 08:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 0e546e4c-57c4-3413-b4b6-10063c46ee99 | -9.1536 | -59.464 | 2025-08-24 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ab23157f-bbb6-308d-924a-d65600b70f91 | -9.1535 | -59.4834 | 2025-08-24 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 7e256a32-d59d-3f3f-9706-959a2d48f5fc | -20.3599 | -51.68 | 2025-08-24 08:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 197f59e5-5608-3795-a719-f2025aa492f1 | -20.3594 | -51.7023 | 2025-08-24 08:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 62a5e8d4-1cc7-3a2d-92e6-cc1748e16036 | -9.0232 | -65.6982 | 2025-08-24 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |


[Clique aqui para ver as próximas entradas](README90.md)
