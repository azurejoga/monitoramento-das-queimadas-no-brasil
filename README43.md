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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b69ff2ce-e1b9-38a8-9fe6-5ef968c4f867 | -8.99009 | -65.41241 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35b583e2-2f4f-31fa-844e-a9b3e042ff36 | -9.08055 | -67.86723 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9e9da63-32a5-3be1-b61d-67b94b5e25e2 | -8.99112 | -60.5849 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fbbb22d-2159-3987-938f-1ad1f0f82a50 | -9.21837 | -63.64922 | 2026-09-10 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 732ce9ce-571a-3976-bda4-11b1eae2eff3 | -8.67706 | -62.45971 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c93d9cd9-c3df-3558-a6b8-1abc2320e60e | -10.57753 | -68.77218 | 2026-09-10 06:08:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 452dfcaa-a53e-3366-8a7b-edccedba3038 | -9.03835 | -65.41492 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1dae5dc-28d5-34fb-9071-484faf9e1507 | -9.21437 | -63.6436 | 2026-09-10 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 421832b1-8c73-34f5-a41d-5e59d527bbba | -6.76822 | -59.43349 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f362973-cc46-3151-b695-4c68dd4e1992 | -9.91666 | -67.87677 | 2026-09-10 06:08:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be1a9f5f-ef57-38cd-8f73-da0efb7f358a | -9.92028 | -67.87729 | 2026-09-10 06:08:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 384ef547-35a3-3bc0-afc2-cdd9226ed899 | -10.57811 | -68.76826 | 2026-09-10 06:08:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da7473c4-7088-37a7-ae96-492d9237e3d8 | -7.24465 | -59.52338 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53f61841-0f0b-3387-a13e-31837f036238 | -9.21905 | -63.64428 | 2026-09-10 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69ecee66-e5c4-3f1d-ade1-033e44115667 | -9.20259 | -65.77872 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3d5e380-0955-32f6-9482-495fc553d46d | -9.91965 | -67.88148 | 2026-09-10 06:08:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d0f86dd-4b92-3c40-b279-af95a4296432 | -10.85578 | -60.83914 | 2026-09-10 06:08:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55d92be9-5a60-3899-8f7a-c882f1e3fd19 | -9.04196 | -65.41928 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5aa4b996-1249-3f65-8454-cf1edd7083cf | -9.2351 | -65.75409 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 366b56ac-b92b-38ec-b367-38f3fb8e792d | -9.96099 | -67.21779 | 2026-09-10 06:08:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c4c2a89-8c8b-35a6-901e-ba563f29b211 | -6.50516 | -58.38046 | 2026-09-10 06:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f635d912-21a0-305a-908c-f3736f932eef | -6.7657 | -58.6138 | 2026-09-10 06:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1113a0bd-7c6f-3db9-9a93-98b41c168412 | -9.22305 | -63.64988 | 2026-09-10 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15aa4bf8-40c3-394d-a134-0eef2f31da0a | -8.83848 | -70.7144 | 2026-09-10 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 343ef5d4-8fa0-34f6-8699-eb89ee8d8096 | -9.3748 | -68.82462 | 2026-09-10 06:08:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1feea431-a3fd-3237-924e-5da50c39eea9 | -6.77202 | -58.61469 | 2026-09-10 06:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23a8ff1a-db2f-3361-b8a7-a0a5d3d7b363 | -6.82122 | -58.99354 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1744a0b7-4e89-353f-9404-e117315c6615 | -10.85629 | -60.83511 | 2026-09-10 06:08:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa48a171-e1bb-3fe8-b44f-aa7c13403f4f | -9.04717 | -65.41233 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97ccf6f2-40ce-3a87-bcc1-53fbaf3bd992 | -7.23923 | -59.51801 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adb7f80b-4a64-36d6-93e3-938b5620710e | -9.15622 | -68.24901 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7210662a-60c5-363a-99dc-a9b4c562631c | -9.48403 | -68.49377 | 2026-09-10 06:08:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2768c233-909a-32b2-a50c-22bb5c0a936c | -6.82738 | -58.9945 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16d4ead5-e136-3d2d-9f00-c4ba23a9e48b | -6.46077 | -62.86825 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c7ec9dd-0a9e-3eae-92eb-4ca2044e8e5c | -12.15766 | -64.13846 | 2026-09-10 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa75d391-2341-3635-8f39-cc45bdd33057 | -9.30452 | -67.69825 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 184a5f77-cce2-30a1-aa4b-5df871937c0c | -8.89474 | -61.43306 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 012da178-8d54-364b-b394-98a13617accb | -6.82057 | -58.99835 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22b85c7d-664a-393b-8782-845feb40dc52 | -10.11709 | -68.60941 | 2026-09-10 06:08:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ef5226c-59ba-3cba-9266-62e3e449b60f | -9.04249 | -65.41551 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82d369ae-8232-3842-94ea-5f440fb13136 | -9.21974 | -63.63934 | 2026-09-10 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5a4148b-e188-3330-b812-39e6c4e07a6a | -8.62428 | -66.50929 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f28bb23-79c6-3262-983e-ffcf8719bd97 | -6.76507 | -58.61859 | 2026-09-10 06:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdf7588f-d8f5-3fd0-8bf9-d5a02e8acf43 | -6.80854 | -60.13435 | 2026-09-10 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1daa87ec-d2d0-32e4-8edc-f0386fd5fda4 | -9.2031 | -65.77512 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3a07ad1-f4d7-3763-ad66-6102d2b9bac8 | -6.95426 | -59.7641 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af279aa6-1268-3e85-9d45-7b3cf4e34361 | -6.8998 | -62.98233 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56070a0a-5e31-3393-a846-c9ee4e0b3722 | -6.55437 | -62.89841 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 480a0811-e9e3-39b1-a2b0-7bf70ee9ad37 | -10.62258 | -68.61341 | 2026-09-10 06:08:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05753723-d5cb-3ab0-812f-763ec266dcec | -8.9064 | -61.4414 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c85efff0-a738-3840-bc9a-2a6aca904536 | -6.55511 | -62.89331 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0000cfc9-bb99-359e-bb2a-d3fe0e703038 | -8.99163 | -60.58099 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835fd18c-cd0c-3ef7-9011-0cd9514d6397 | -6.77779 | -58.90154 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a29611e-dd03-34fa-b299-a124d7a769d0 | -6.82186 | -58.98876 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 003a1b50-f968-3de1-9fd3-117e6cc18870 | -6.63656 | -59.43892 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 588f038f-0560-3e89-90d0-21a95480bb49 | -6.78531 | -58.89289 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90347881-8b96-359b-a5a2-b09971feeb76 | -10.61872 | -67.92818 | 2026-09-10 06:08:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31674914-789f-3a72-99f5-d47627d8c88c | -8.89521 | -61.42957 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c792422e-ef42-3555-bf66-e201627c56fc | -8.82186 | -62.48395 | 2026-09-10 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a36b056-ef0f-31f2-8b76-ad9cba4a1644 | -10.62236 | -67.92873 | 2026-09-10 06:08:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc5f76c0-675c-324d-a521-252aef067455 | -6.55038 | -62.89261 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8eb5a13e-974e-3b2b-aa5b-82894286e0bb | -8.89427 | -61.43653 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 274af2c4-cc8f-39fb-a790-c454cc66f314 | -9.04062 | -65.74886 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 384bf2b8-009f-3b38-8f25-90bb469bd388 | -8.9807 | -60.57524 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f38ff5d-b19d-35fa-834d-227b31f0e3df | -6.79153 | -58.89365 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6fa56e41-8c24-3cfb-9e01-d4179a5dc369 | -6.26897 | -62.74261 | 2026-09-10 06:08:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e8a422d-0680-3478-9db9-9bbd356e9367 | -6.55986 | -62.89398 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c19256e3-e0e3-33b6-a110-cae2fe8b7a89 | -8.8832 | -70.83924 | 2026-09-10 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 678b00f6-4091-3f6c-bd38-0da0bfa50fff | -8.99216 | -60.577 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3839e3fa-9605-38ae-84d7-927e614e66fa | -7.23865 | -59.52248 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b656791f-4e77-380d-be34-93f9d69d886f | -6.78333 | -58.90725 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f0ce934-6fb0-35cd-9519-434afc05c75c | -9.03761 | -65.74113 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c042d2a8-7214-339f-8063-435e5f158c6f | -8.88932 | -61.4323 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7872fa3-f0ee-322f-957f-63d69aa0ec21 | -6.80284 | -58.94871 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 900a9f38-a29a-3a69-84fd-72dcdc4016a1 | -6.78465 | -58.89769 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 978f4d05-5552-3619-ad02-1f176b8d7434 | -8.15594 | -62.90186 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58c9cfc7-fb44-3b34-b402-25d9dd73306d | -8.7329 | -62.38924 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7bc4601-2000-344b-91e7-44b51bbaa5fb | -9.0461 | -65.41988 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54bd26f9-2f4f-337b-ae65-15ccc323da43 | -5.91724 | -63.47351 | 2026-09-10 06:08:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e151e24-7337-31ac-adc9-91cbcf0d2fe0 | -7.39543 | -72.80113 | 2026-09-10 06:08:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a616fbc2-04c5-3469-ad3d-38031eea1b0f | -6.79642 | -58.90403 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b82c1e-7653-3c91-8859-520a31f53405 | -8.43637 | -70.09678 | 2026-09-10 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96846b99-52c5-34d2-b8c2-e803cc99e151 | -9.47082 | -66.58369 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ddc9ffb-d1f7-30dc-aabf-2d43ca745b34 | -6.54963 | -62.8977 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ed73f6fa-edf2-307e-9e2d-f4785687c338 | -8.89332 | -61.44349 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fad9595-3ad1-3859-95fc-4b3b86b479ac | -6.79086 | -58.89847 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd750e1e-b8d1-3fa6-a5dd-ef782855b5ee | -6.7902 | -58.90329 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 334ebe57-4954-3232-a2cb-aaabaec9a321 | -6.76297 | -58.96362 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 571de642-7e17-3ef6-b07e-3098d22b4187 | -8.73331 | -62.38625 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b1a541c-0da6-32ac-ab28-ca0ed39eb072 | -8.99736 | -60.58189 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc1bc409-5613-35aa-9518-72beb9868434 | -9.04303 | -65.41174 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6505b69-5618-360a-a880-c96d33e97a8b | -6.50373 | -58.39097 | 2026-09-10 06:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72e6ef0e-3fda-3328-a73a-a941afabe36e | -9.23711 | -65.59416 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5a90c43-73ec-3024-b873-aa28b19ddb63 | -7.2422 | -59.52542 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d79ed0b5-9481-3abd-9156-5353836c8cf2 | -4.06424 | -69.5873 | 2026-09-10 06:08:00 | NOAA-20 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d1c4761d-8737-3c7c-9fae-3caf8cc0ff4d | -6.77976 | -58.88721 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1112389a-d26a-3392-8705-23a8dd67a353 | -6.79614 | -58.89721 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f34df22-fef7-3bfa-99b5-cfd766735794 | -6.54815 | -62.90784 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94f1cb90-e0a7-3076-a5f3-b2ddcee5ecb1 | -6.54889 | -62.90279 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2140394e-435c-3d39-91f6-df9b8bc7be94 | -9.00415 | -65.40296 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README44.md)
