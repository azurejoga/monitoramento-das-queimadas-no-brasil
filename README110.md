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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9595932c-c3a6-3308-b203-0d4a8c9d2a81 | -9.15345 | -60.66275 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 456539b1-0e89-390b-829b-a06c2962c587 | -9.15059 | -60.65822 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6d9b05c-6076-3959-8c54-05af742afc96 | -9.14708 | -60.65765 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| abeca383-812d-3254-95d6-2591c85edb99 | -9.14643 | -60.6616 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5e30ea34-3d34-3ce2-b64f-37fcf9dbe94a | -9.14356 | -60.65708 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f29eba5-e8b0-3fdc-82f1-b1339d905b46 | -9.14291 | -60.66102 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2a4051bc-b3e8-3014-a26a-3ac7c55578a5 | -9.14005 | -60.6565 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d310d28-2ef7-31e2-a06d-eb40f8adfdca | -9.1394 | -60.66045 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e2cd350-2b93-3467-adbd-576cdc52ea87 | -9.13654 | -60.65593 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8c53dc0-f73e-3e0c-a399-a367f0e70b34 | -9.13237 | -60.6593 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33e26de2-6ce4-373c-bba0-0d0dcb2f1114 | -9.27558 | -60.82567 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b69a67e-d2cd-33c0-96f4-12163bb5652a | -9.27022 | -60.79182 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6d5b1d4-6403-30c7-824d-32cfd7c7e070 | -9.25427 | -60.40886 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66eae263-2a82-3fda-9b69-036ff0f1245f | -9.25374 | -60.47661 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 349a5b37-6a5a-3ff3-92ba-026d191903e7 | -9.25026 | -60.47604 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 528f0969-7014-35f2-8619-e11344bb5713 | -9.16112 | -60.65997 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ae82a60-ff4d-3161-96a1-98c619713fb3 | -9.15761 | -60.65938 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6a5b46b-fc2a-354a-a08b-5897e6938f04 | -9.1541 | -60.65879 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efb8da7e-c853-3843-a038-27395f7dc60f | -9.14994 | -60.66217 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8f3a7b3-90fb-34ac-adb3-a7cfaff52900 | -9.13589 | -60.65987 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f579ed72-7bbb-3d65-a78b-ba80324b1be2 | -9.13172 | -60.66325 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4739a23c-f65c-3722-9a09-5cd96f1fdbb1 | -9.12886 | -60.65872 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba36087a-004d-3956-8439-dfcc89985336 | -9.1282 | -60.66269 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a850dfbd-a3b9-3561-b0d3-9ef20bd35b22 | -9.12535 | -60.65815 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac2e0622-d229-3a0b-86e7-679d3dfa67f3 | -9.12327 | -60.40054 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f104cc0c-d928-384d-8aaa-9fb5b66e7dba | -9.12183 | -60.65757 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d38b272b-f4f9-35f9-8322-a8b5fa6191f1 | -9.11979 | -60.39997 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2530e00a-e51a-377e-872f-7fe61cead3eb | -9.48778 | -61.01252 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 116cf256-a102-3fcc-98da-cfd807c6d0fa | -9.48117 | -61.01243 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e5fd206-1e79-3613-812a-9cb07ffa3cb2 | -10.34999 | -60.20347 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4f600ff-1a2a-3194-a578-0e2c0e1d54cb | -9.94763 | -60.12691 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a33d61c-70ec-3283-bbda-916fd474ca11 | -9.9201 | -59.90859 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b76ebe2-92b0-3764-b99e-750b143503b2 | -9.91949 | -59.9123 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcb1fca7-74d4-35a9-8e03-59bc0d060faf | -9.88097 | -60.32124 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35640cc7-aec8-327f-9966-c16ae1dc19b2 | -9.87815 | -60.31688 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 205a649b-dfda-3742-907a-3f832e49c6d7 | -9.87753 | -60.32068 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f23df8a-e99c-3fe4-a473-0e393c51c13f | -9.87409 | -60.32011 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29c96692-3234-304f-8f10-db57bbfc0717 | -9.87127 | -60.31574 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d9dc1d8-b5ca-308a-9e29-ee5f740fda6c | -9.87065 | -60.31954 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94d37857-8646-3855-8eed-1893d18157e1 | -9.8697 | -60.30374 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f671b10b-d9a0-32b4-be9e-81497726198b | -9.86783 | -60.31518 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0303d6a-d08c-3fdb-958d-b2e75e982e6f | -9.86688 | -60.29938 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df0432e7-d58b-3790-95a1-8586edabdcbd | -9.86626 | -60.30319 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22d63876-5258-35c7-95e9-c37cee5196ce | -9.86407 | -60.29502 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56d913b9-8a28-335a-83ae-c2181a78399e | -9.86344 | -60.29882 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90cf8157-3890-3095-86d4-62a9d7497b7a | -9.86282 | -60.30264 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84b04a6e-65df-3381-a3c6-12bf9ba1df5b | -9.86001 | -60.29826 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ab94f7f-8e61-35fc-b0c1-fdf6b2c76938 | -9.85938 | -60.30207 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a44470d-1f74-376a-860f-13c89a262916 | -9.85876 | -60.30587 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00babca7-255c-365a-9a0d-66b8aca7c0a2 | -9.85814 | -60.30967 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 523cff8c-92e4-3c97-9941-18314dfafb4d | -9.85751 | -60.31348 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba2af8e2-ed0a-389b-a6ac-99edb51c3e58 | -9.85657 | -60.29768 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 429fe1fe-1672-38b3-bf3a-e22639df2223 | -9.85595 | -60.30149 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1539161f-fa24-319e-b3d9-241f906fa412 | -9.85532 | -60.3053 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a88df564-67e0-3b64-9e1d-cf411c00ed8b | -9.8547 | -60.30909 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a72d4ee-7c3e-3dd1-9174-35bd2763f283 | -9.85408 | -60.31291 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a636306a-804b-3d27-b6b2-776c33911e57 | -9.85313 | -60.29712 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ca3db36-4275-315d-9d33-b4a583ed97f7 | -9.85251 | -60.30092 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e11e7f85-737c-3e88-ad44-558a66b1bd34 | -9.85188 | -60.30472 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2718a154-09bd-36e9-84d0-10373afddf3b | -9.85126 | -60.30854 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1df2219-fd68-3f1f-9661-8a4c715981f7 | -9.85094 | -60.28894 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 00967cbb-c1cb-326e-944f-805b9aa23e2f | -9.85032 | -60.29274 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 49586bc3-1a19-3698-9bba-908853e744a6 | -9.8497 | -60.29654 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b75f086-a235-3b1c-869f-e752f944fa2c | -9.84907 | -60.30035 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72feab80-0408-3d85-b227-55e041e69a59 | -9.84845 | -60.30415 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75aa16c8-5b33-31db-896b-313507e740a1 | -9.84751 | -60.28839 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf5feacd-4a5c-3c38-b872-e5255f1270fa | -9.84688 | -60.29218 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11912d55-505f-3163-8e7c-ba3ab91b5624 | -9.84626 | -60.29597 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34db2beb-e488-3633-9286-2a83e4d5d6ef | -9.84564 | -60.29978 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69297777-5535-368f-a319-f72a69f5925b | -9.84501 | -60.30358 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e977a912-5a00-3409-8541-7e6be9af47cb | -9.84407 | -60.28783 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ea00b5b-f87a-3134-8306-af7fa8432b7d | -9.84345 | -60.29162 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8295623a-6c64-327a-9733-ae4f97378a8b | -9.80816 | -60.46264 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90ed9749-5a0c-3303-9431-8637ae4b7f83 | -9.79933 | -60.47305 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b8fdbd8-f2fd-3921-b71c-7c9cc35528fa | -9.79869 | -60.47691 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecb38f18-a55a-3e0c-bcd4-4b73640a0450 | -9.79587 | -60.47245 | 2024-10-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37f2029f-39f1-38a6-bef2-1594a0e25531 | -9.48422 | -61.01194 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44a61611-d1fe-36f7-824e-9a886904c8cd | -9.48353 | -61.01601 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b47547a-1cb7-370e-b5da-a07d73694eea | -9.48066 | -61.01136 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24d63d3e-6d54-384a-baf3-6b8d23909919 | -10.37985 | -61.17624 | 2024-10-06 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 713c11bc-46b7-3c69-8207-3fa484d3ee73 | -10.37849 | -61.18438 | 2024-10-06 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15ade6ed-c1ef-3076-a5f6-67f2b0abcc69 | -10.3763 | -61.17565 | 2024-10-06 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abf8b309-1b5e-361a-b031-45dc1e98e1c4 | -10.37562 | -61.17972 | 2024-10-06 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2987c99-3692-3238-ae0b-daa00edcf5f4 | -10.37494 | -61.18378 | 2024-10-06 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d69d8a23-5ead-3d22-9b74-930498efe108 | -7.28032 | -61.08927 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 386ed8ce-a1a5-328c-987d-a314f548d988 | -7.98122 | -61.3931 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7544dff-9f9e-36c1-b1a5-292c35c1fb3a | -7.9805 | -61.39749 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 025726f8-34c1-3254-bcd5-aaf8898e098f | -7.97977 | -61.40189 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5047d27e-c285-3116-b225-90ce9f5d332c | -7.97752 | -61.3925 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7e23f1f-3141-3a25-99db-d12781eee590 | -7.9768 | -61.3969 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0642dd36-fefb-3c98-b094-e5bec7b8e71e | -7.97607 | -61.4013 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c77fbf7e-e928-3211-83f4-ce6f41cd7ce1 | -7.93235 | -61.27692 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9532c789-c0f1-335a-9788-9272ac9b6971 | -7.9294 | -61.27199 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5ffbe74-ace9-34fe-b9bd-1d649e6ca6c7 | -7.92868 | -61.27633 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f765b0bf-bd14-3194-affc-553eb2a4ce44 | -7.92573 | -61.27139 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae3236ae-f96b-3a2e-bd6d-c359ab9a29df | -7.925 | -61.27574 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91677a31-254b-373b-9502-5c9c1d39bf63 | -7.89898 | -61.52139 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 316652bf-1054-330e-ab24-2b5f8a6d3573 | -7.88942 | -61.46458 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1518db45-97c6-3aa5-bfbd-6371f04b957d | -7.77147 | -61.0929 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a45285f3-b9cc-38f8-a926-3053160f2b35 | -9.25179 | -62.24475 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README111.md)
