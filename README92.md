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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53de2ffd-a7c4-3a99-af32-fe68243cd617 | -9.20814 | -64.44464 | 2026-09-24 13:04:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 98556968-359a-32f4-8ea5-62c272e6325d | -9.04315 | -66.05818 | 2026-09-24 13:04:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 76c2fc1c-93f2-3c93-b3ce-92d08842ae47 | -9.13764 | -67.94274 | 2026-09-24 13:04:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a95e9b1d-76ef-3edb-9651-93edcf7085bc | -8.1786 | -64.04685 | 2026-09-24 13:04:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c3298a63-205b-326c-8a2e-a8245d458406 | -12.76327 | -57.73145 | 2026-09-24 13:04:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 649e5a12-d6c5-3d76-861f-813f9e68f39a | -9.9332 | -60.71254 | 2026-09-24 13:04:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| d41243b3-e794-3c8b-9e3b-e1bbcc1e970d | -9.01721 | -60.51867 | 2026-09-24 13:04:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 5c56fb3b-877b-3296-a6c6-82bee5019d00 | -9.72609 | -65.0172 | 2026-09-24 13:04:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6f71b11c-a87b-312c-bb48-9fa3fade72ab | -7.89477 | -61.16041 | 2026-09-24 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| a21b7ff8-86f5-32ae-b603-8f610ceee604 | -9.11039 | -65.37749 | 2026-09-24 13:04:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b63f67d1-c7f8-3eae-b725-bcf7e5a3fbd4 | -8.89614 | -62.5419 | 2026-09-24 13:04:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a751fde3-025f-3a50-a910-94b5e19a4949 | -7.82456 | -63.42475 | 2026-09-24 13:04:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 35ead346-5242-3ec3-aa9a-4cb0d987c23a | -9.14948 | -60.93917 | 2026-09-24 13:04:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 5817690f-313b-32a2-8b68-95b5301086b1 | -7.81988 | -63.4306 | 2026-09-24 13:04:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d1cde881-4204-3320-af25-7d187fa1db49 | -7.28576 | -59.63778 | 2026-09-24 13:04:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| e57d6281-ac59-33eb-9745-27bef99e92ca | -7.28112 | -59.63202 | 2026-09-24 13:04:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 6bafcd9e-7595-3f3e-a88c-9b8b374bcb31 | -8.18018 | -64.03519 | 2026-09-24 13:04:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c0ac66e2-f30f-33bf-99f8-ae688dbb430e | -8.64979 | -67.02561 | 2026-09-24 13:04:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d0849b23-dcfe-31a8-8154-38180f309eb7 | -9.04444 | -66.04875 | 2026-09-24 13:04:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 18f33319-dae8-3595-bdd8-b85e34c4d1b8 | -12.7639 | -57.73649 | 2026-09-24 13:04:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| fe4ce75a-039f-3dd7-95d9-593da4632856 | -8.92692 | -61.47732 | 2026-09-24 13:04:00 | TERRA_M-T | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 24cc8e58-23c1-374b-8e6f-3c316dba8e79 | -9.56007 | -65.98589 | 2026-09-24 13:04:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 886e31bd-d085-3fbf-8b40-615ad8bb193f | -8.88474 | -62.54047 | 2026-09-24 13:04:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 31.3 |
| da58e666-bc32-37ca-b29c-41c7f14d123f | -9.50775 | -66.76166 | 2026-09-24 13:04:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ee78b4e3-9f54-3cb2-94ff-226b1398ed5c | -9.04574 | -66.03932 | 2026-09-24 13:04:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d65b2838-a38a-376d-8bb8-a46f7df12ff1 | -9.19155 | -65.78309 | 2026-09-24 13:04:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6a6a52cd-8c34-333e-b286-68f220d0996a | -9.0474 | -65.42017 | 2026-09-24 13:04:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2c3afee1-b6ce-3189-a3e5-1ac3e32cc7fb | -9.02227 | -60.51383 | 2026-09-24 13:04:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 96ecf49d-0bae-33bc-84be-d0c403cf8475 | -9.49705 | -64.03328 | 2026-09-24 13:04:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 006eddf9-abd0-3f16-99de-226af4d65f91 | -7.82283 | -63.43744 | 2026-09-24 13:04:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 04221694-d78a-3cc7-b454-cd24235ab413 | -10.7006 | -60.73954 | 2026-09-24 13:04:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| c0d90467-c545-3682-9403-43001b8ec493 | -10.71418 | -60.74116 | 2026-09-24 13:04:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 5e38106a-b0fa-3819-818d-d80e8f330859 | -9.04875 | -65.41013 | 2026-09-24 13:04:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9c20324a-1cf5-3027-9902-96af0c311ea0 | -9.48948 | -64.02633 | 2026-09-24 13:04:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 54e9b6c8-8243-3496-ae3a-ba4d80879cc3 | -8.59126 | -62.50932 | 2026-09-24 13:04:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2c4271cf-f604-3dab-a603-8c9b84aa1d53 | -7.58321 | -63.45771 | 2026-09-24 13:04:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2d9ca08a-b430-329f-8e26-98b554f2c4bd | -8.4307 | -47.4515 | 2026-09-24 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 8a688ee7-faec-32be-a860-bd33054f271a | -8.3761 | -47.3023 | 2026-09-24 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1012b953-9d89-315c-b48e-419b5623d93b | -8.5989 | -44.5531 | 2026-09-24 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 421cc38c-124e-3adc-8473-22927e7435aa | -9.6111 | -43.9243 | 2026-09-24 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 128.5 |
| c3b6a37f-12a8-3966-ba5f-c53ddccdb815 | -11.3246 | -44.0169 | 2026-09-24 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 0d087539-150e-3a4d-8e01-fbd8cd3e0943 | -8.2529 | -48.2128 | 2026-09-24 13:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5dba6c7d-9343-33e1-900d-d5facd41991e | -11.436 | -44.211 | 2026-09-24 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| cc1d5399-c159-3cf6-8658-07b51ca323ab | -8.8914 | -62.5436 | 2026-09-24 13:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 756a4f47-8a19-3ecc-96ed-e9f431315df2 | -9.6302 | -43.9219 | 2026-09-24 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 168.4 |
| 90fda08e-c57c-3bd6-ac04-43b6ead9e3d7 | -5.6016 | -60.1919 | 2026-09-24 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 2b028520-bf34-344e-9107-2f90c72164d8 | -8.9208 | -45.9084 | 2026-09-24 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 612e5ddd-b562-39f3-940f-a5ffc1fc6e11 | -10.93 | -43.86 | 2026-09-24 13:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| adbf2af9-cc70-3afa-a554-f2beae301fcd | -10.14 | -50.28 | 2026-09-24 13:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8038f7c2-5d67-31aa-b32a-caf162fa6d03 | -10.08 | -50.26 | 2026-09-24 13:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89ac5c05-36b1-3ec1-86ab-4fc94aefe71f | -10.08 | -50.21 | 2026-09-24 13:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe4659db-9f6e-3556-8698-cabdcf360e43 | -10.96 | -43.87 | 2026-09-24 13:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e5d952e6-145f-38c2-8550-381ee1a10096 | -10.11 | -50.27 | 2026-09-24 13:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3208b5ae-5d31-36b1-bbc9-d6d8f5b3b649 | -10.14 | -50.23 | 2026-09-24 13:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5083c535-e901-372f-8618-434121d4bfb7 | -10.11 | -50.22 | 2026-09-24 13:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c9b7052-65e3-341f-81b3-c6965b7b1eff | -11.325 | -43.9934 | 2026-09-24 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| ad121e7e-199d-37b1-a41f-3447fb85d77c | -11.3054 | -44.0198 | 2026-09-24 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 686c6607-9180-3c82-bc5c-8e0da1642d76 | -9.6111 | -43.9243 | 2026-09-24 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 143.0 |
| 450a7b63-e5f5-3e6c-abbd-d01e5844434b | -11.305 | -44.0432 | 2026-09-24 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| a7eed71b-8351-3849-a880-5fd27b1ceb7f | -9.2796 | -45.9143 | 2026-09-24 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| cbb8a1fb-315b-30c2-85ca-e26a1a55a79d | -8.3761 | -47.3023 | 2026-09-24 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| fa1397ef-c97f-3f62-8911-ef9abdb114ed | -5.6016 | -60.1919 | 2026-09-24 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 8be1afed-7b7f-3552-bd81-c5cf42f983a3 | -8.8728 | -62.5444 | 2026-09-24 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ca27740f-017b-3179-bfc7-a04b26c70ef7 | -8.8914 | -62.5436 | 2026-09-24 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 141.0 |
| c4c5235e-9f81-30cf-9145-50bb1d7ddbbe | -14.7017 | -48.7559 | 2026-09-24 13:20:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d21ebcd2-ba5a-3b27-946f-7b21d36a7c74 | -8.7732 | -45.6529 | 2026-09-24 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6e8012d7-7ac6-3890-9cac-35f33d834f99 | -11.4364 | -44.1876 | 2026-09-24 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| a70fcf3f-b4f9-3c19-a93c-25c4aa2666ab | -8.2529 | -48.2128 | 2026-09-24 13:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 221eca56-9950-3a4f-9749-c8bb1eaad498 | -8.8915 | -62.5246 | 2026-09-24 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 7ea7d3ff-6b52-32b1-9713-714f26e2509a | -11.3246 | -44.0169 | 2026-09-24 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 893515a3-ea1d-30c8-959c-d7a8487c49ce | -11.436 | -44.211 | 2026-09-24 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| d4ce78f1-7513-311b-9d0d-71d21489e00b | -8.4305 | -47.4736 | 2026-09-24 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5e955c68-56ab-39d4-8592-7081d06bb46d | -9.6302 | -43.9219 | 2026-09-24 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 183.3 |
| c3011fe7-8b99-3fdb-89d6-edf0a99a097b | -8.4495 | -47.4497 | 2026-09-24 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| b36c5855-7a03-33b6-8d26-798c30fb2c2f | -8.4307 | -47.4515 | 2026-09-24 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 59c7ff4a-f42a-35e0-8035-fac3c1735bce | -8.4493 | -47.4718 | 2026-09-24 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8cbc47b6-901c-3b31-a5af-d96a76c02096 | -13.2057 | -51.5703 | 2026-09-24 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| de293dd4-8266-3f74-9f39-be13bbcb0029 | -9.5735 | -46.5337 | 2026-09-24 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| df19b3a2-fee2-30f2-ad01-cf325f7faf93 | -8.8914 | -62.5436 | 2026-09-24 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 8577a56e-e2dd-334b-89dc-048d64edc5fc | -11.1541 | -42.8364 | 2026-09-24 13:30:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 6e69608c-486d-3807-9684-80cdc3605980 | -8.3761 | -47.3023 | 2026-09-24 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| cf8d35ef-de68-366e-99c2-a7bd53b54cdb | -8.4495 | -47.4497 | 2026-09-24 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 3c10e6fe-e87a-3b4e-9dc7-e5c52dca6a78 | -11.436 | -44.211 | 2026-09-24 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 0b28b468-e928-3ca9-aef8-ac43984fb18f | -8.4307 | -47.4515 | 2026-09-24 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2512bcf4-5f9e-32c1-8d97-4324b2e3533b | -11.325 | -43.9934 | 2026-09-24 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| d0429047-135a-3088-83a6-3372f0aaca6d | -11.3058 | -43.9963 | 2026-09-24 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 5250b641-15eb-3bf7-bd7e-78656bf01c55 | -9.5738 | -46.5113 | 2026-09-24 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f8de8da2-bed7-3eaa-8857-5152c6b7af8a | -13.168 | -51.5324 | 2026-09-24 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ef6f726f-59a5-3948-80f5-d99ae336e395 | -11.4364 | -44.1876 | 2026-09-24 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| bed2f673-99db-37ef-af1e-b7be6ace3501 | -6.6631 | -55.0512 | 2026-09-24 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 88833147-7f20-3b0d-8dbc-18c7b02ae250 | -11.1353 | -42.8154 | 2026-09-24 13:30:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 6b479e51-2a02-30f0-b8c7-c5856b88d02e | -8.9208 | -45.9084 | 2026-09-24 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 161.0 |
| bb07fb02-36ff-31d0-9445-e4c059b7184a | -11.305 | -44.0432 | 2026-09-24 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| ac2bdf52-482e-34b8-a42b-511f3f91595f | -11.1358 | -42.7914 | 2026-09-24 13:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 100.6 |
| b7065fb5-b561-3d7e-9234-39d1d79460f8 | -9.6298 | -43.9453 | 2026-09-24 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 3d3d9ec0-6bd5-360c-92b8-39b079a6f184 | -11.4551 | -44.2082 | 2026-09-24 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| c88c405b-5722-39a6-bceb-dc312a1ea4b3 | -5.6016 | -60.1919 | 2026-09-24 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| f88d6cde-6720-3552-931f-ff35d26f55ac | -8.2529 | -48.2128 | 2026-09-24 13:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d77b1a59-4edf-3bbf-b25b-fffb26c56e58 | -6.6815 | -55.0703 | 2026-09-24 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 00ab2b4a-d6d2-3b9a-8e40-984d29da92ed | -10.1107 | -46.0435 | 2026-09-24 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |


[Clique aqui para ver as próximas entradas](README93.md)
