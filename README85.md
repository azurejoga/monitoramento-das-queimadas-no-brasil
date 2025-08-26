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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 309ead2c-72af-3863-9e1f-c9d7d081c978 | -8.60889 | -62.64944 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed0221e9-ece7-323e-9300-a5254c6d5dec | -8.98266 | -65.4127 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a68cb904-1063-3875-aeff-34e9d2812726 | -9.02463 | -65.72578 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bdb2857-b2e7-335e-8ac4-ec469e038edf | -9.16782 | -59.52538 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4e28e24-830d-3086-9c91-164555255192 | -9.00768 | -65.38408 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7fbcfea-b554-38b1-8010-4231d925fbc7 | -8.86686 | -62.44885 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f4fa49d6-9532-3b8d-b8ba-36d09fb79d58 | -10.25788 | -59.10243 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 890f577c-cc22-33e9-a53a-bf0c88e583cd | -9.80901 | -64.28851 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e74b9f29-fd9d-3be9-ac75-806e83329bc1 | -8.85259 | -62.4505 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 169d6555-b669-3b09-a15e-18f0688a00d2 | -9.65526 | -59.62859 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 334ce076-b243-3041-b862-bb2443e58cc7 | -9.81232 | -64.28902 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e3e6146-82ec-3cff-8a03-d5e65ca2d243 | -9.16627 | -59.50713 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8f18788-d600-3f56-9f22-cd85b1159e94 | -11.71217 | -63.66545 | 2025-08-26 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b9712bc-6dc0-32f8-a20a-a18b97d25718 | -8.55407 | -62.63782 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7db21a0-e1f7-319a-aa2a-98dbd56eba6a | -9.02194 | -65.69959 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e25c70de-0a9b-324b-bc6d-2167970ffc2e | -11.54229 | -52.1206 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| b6bcc226-fe15-30e8-a0f8-18a6c0f3b085 | -9.01802 | -65.70263 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6c6ae27-ef33-3c92-aebf-92530ed19589 | -8.97319 | -65.42932 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77abcd6b-bfba-3399-a7c8-fa09b6590f7b | -9.17672 | -59.46169 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 41bc5af8-1535-379e-9f5b-5038f8bb429b | -9.16486 | -59.5465 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55f168ec-f969-34a3-861b-da2f2d1e3aa4 | -9.19145 | -59.61822 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0167fcbf-1c18-3a5f-bfad-f76c44b88bbc | -11.5275 | -52.13074 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 65bf06ca-5cc6-3183-b100-7e9d0bf90d26 | -9.16219 | -60.7826 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 933444dd-d271-387f-ad3c-4e8841ebd4e0 | -8.99042 | -63.64592 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61661c33-000f-3e5f-8fa9-18fedf464c5c | -9.04196 | -65.72488 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bcca7ca-a91b-3cff-bacd-5b6d73c4fa25 | -9.09227 | -65.72563 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 700b9f50-f51d-3a89-b6e0-577f65176ff0 | -9.16634 | -59.53595 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 940fcb2a-5514-3d23-ae70-582f9c2b3f63 | -9.15588 | -59.55229 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4131fdc1-4de4-35b6-9214-d61ef4174715 | -10.42131 | -64.39677 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b42c6c62-49b8-38b8-abd7-a48048df8103 | -8.57615 | -62.62993 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25731a02-af64-318f-b5cb-5accf3c27126 | -9.17943 | -60.79435 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 230f0950-36af-3f69-9a56-1fad7355a780 | -8.23994 | -67.36687 | 2025-08-26 05:38:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 726c3ba4-75ae-384a-909a-def43a77b933 | -11.30747 | -55.10909 | 2025-08-26 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 19a142be-6b2a-30d6-bf65-36e65793efd3 | -11.57335 | -52.11127 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85297317-d339-3e29-9e2a-f77a077deb09 | -9.18436 | -59.52425 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e43b04f-f9f8-3d60-a0cd-060383279e25 | -12.22474 | -64.22942 | 2025-08-26 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cddb6d4e-413c-3fff-9649-c2c1793f2bc7 | -9.10238 | -62.67513 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5f7a8c1-e01c-36f7-979f-64627350ba3e | -9.09954 | -62.67089 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cc5bfa4-c1fe-35bf-9927-de81c6f69712 | -8.60078 | -62.58777 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 562c5c22-75b1-3500-8891-9efd0d335985 | -9.20946 | -59.4337 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f190a74-de6b-3e7f-be42-97ac827ec908 | -9.27415 | -56.90266 | 2025-08-26 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5df13cd0-7804-38ee-912f-e66892754e41 | -9.04809 | -65.72952 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae38f104-3c60-34d2-8104-ef8a2c84d84b | -10.89738 | -55.78188 | 2025-08-26 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2373da4e-6184-39bb-89d1-bf7d7a7cff76 | -9.09216 | -62.67356 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cdda3c9-c612-3f4b-a8a6-1f4bedb3056d | -9.20396 | -60.92706 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b250fcb8-733e-3b33-b23a-5bbbbc644825 | -9.82659 | -64.26266 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cad3ccea-5f2e-3a7c-84da-6c5fedda3de1 | -8.83944 | -62.44464 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 22685149-c12f-38c3-a464-8efba504ea00 | -8.98153 | -65.41977 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12d83d6b-8470-33f5-8f4b-63c63dad0eeb | -9.17133 | -59.52953 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63516f12-12d1-3404-bd5f-183f208d7903 | -9.96824 | -60.18436 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 248c9725-d499-3f1f-8d21-9e1d20c8ea7f | -8.51305 | -63.8759 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab028327-35ff-39e8-ab27-2f651ee2e7ac | -9.18936 | -59.51778 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0028d92a-dc08-3119-bf07-f77005b38e75 | -9.17682 | -59.51957 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00c9c030-80f2-3fae-a306-ccdedac68654 | -9.26222 | -59.79603 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ead3c93-333a-33f0-a0ce-7905c85592d6 | -8.60779 | -64.07619 | 2025-08-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ed56b8a5-e0ac-3ca8-9761-2b44aec01b7b | -9.06934 | -65.72559 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bef9ad51-3bb9-3787-9b9a-6969c6de8155 | -11.3132 | -62.25265 | 2025-08-26 05:38:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79c97e9d-90c7-3d17-8b52-bfd5aaa765af | -9.23606 | -60.91383 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6e31f52-ceeb-3772-9eac-da076ef1d38c | -8.81573 | -69.29268 | 2025-08-26 05:38:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2370c5a8-a7e9-3fd9-aecb-1b26fd39df62 | -8.88913 | -62.44074 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efa16e67-42a9-3458-9e8c-94843454a1a4 | -14.40446 | -51.94477 | 2025-08-26 05:38:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a92f9bc0-979e-38a8-8baa-7d4a4574ef5f | -8.56595 | -62.62838 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84f93737-27de-35c7-86ad-a221cfe75da6 | -9.01157 | -65.38108 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc2ab7e4-3bf5-3aca-82b2-7016c44ebd84 | -9.18482 | -60.79747 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67d047bb-d658-3558-9cd6-5b2bec71bc49 | -9.19097 | -60.80753 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de9a036c-be4c-3b3b-8398-77440b197db1 | -9.19288 | -59.52187 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3cf9bf4-646a-39d8-9fdf-7c70a3bdd66b | -8.5484 | -62.62941 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff6de204-de21-3812-b3a3-22a782c40e7f | -8.08489 | -70.19101 | 2025-08-26 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16545032-ad8c-3f9e-aa85-db0d4811da0f | -9.80011 | -64.25848 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfd99e7a-6298-3cf3-9aa0-271320432ff2 | -11.54094 | -52.13258 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 759fa4cd-17cb-3aad-844a-135dafb04843 | -8.89144 | -62.47182 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 204bca8f-2a76-3174-821a-32ca19a5267c | -8.35063 | -62.94213 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 81999c23-5773-3910-afa6-0cc16171e85d | -9.71228 | -61.28688 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f30e099-3356-3993-90f1-9489275a48f6 | -8.98655 | -65.40969 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0f252a0-5edd-3ac7-89ff-bf030cac00fb | -8.40449 | -63.78697 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b46e932f-1e76-36f0-a4ab-44a6bcfeb107 | -8.87541 | -62.43864 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fcc3185-3549-3ce7-8685-a183a9cb0219 | -12.30317 | -63.73745 | 2025-08-26 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fd4d875c-8a64-3fe5-8f77-a4d909758142 | -9.18577 | -59.45579 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c24c2135-986f-349c-a8c7-8a5455c8168d | -9.00797 | -65.70102 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89625a5d-106c-3096-af4c-d642299ee6d3 | -9.80065 | -64.25498 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd8aebf4-677b-36bd-9257-4690a4a3868a | -9.18175 | -60.79242 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c907c34e-105e-3e5b-a6fe-895ab9c8bd9c | -14.36499 | -51.91247 | 2025-08-26 05:38:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0950d5dc-1535-3811-aa7f-c857e971694f | -8.84916 | -62.44998 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a349328d-a289-38f4-b086-494eff253d2b | -9.10884 | -61.42715 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bef7c5c9-4d3f-39f0-8814-ba5e18594587 | -8.34053 | -62.94057 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fee9ab0c-5ffd-3462-841a-acf7500efb2b | -8.97596 | -65.43339 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48224c72-a57e-3331-8eae-953285c7e7b6 | -8.55691 | -62.64204 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca6aed81-3495-30a1-94e7-b022e33f4911 | -9.19194 | -59.61477 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7afaa780-b049-31b5-919e-8fb057f9fca1 | -9.27342 | -56.90798 | 2025-08-26 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 773d16a7-c4f8-35f1-b0f3-15f6701d1b28 | -11.50662 | -52.1344 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 4aac0f20-02e0-3226-ac93-82d4c088f19b | -9.25193 | -65.6235 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a62cb19-a484-33c5-b30b-30cd82b4b875 | -11.56994 | -52.11776 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bd693d83-b28e-32a3-8307-68da086f73c8 | -9.18133 | -59.51665 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1423413e-85e5-30f1-a413-8ad9d364b232 | -8.88286 | -62.45898 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d022ce5-a207-3d2d-8d5e-1e966bd556d1 | -9.08615 | -65.72095 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c36960b-f249-3a23-8f55-d987b93e3eb5 | -8.99988 | -65.41182 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbf2ed9e-7d6d-3aef-a43c-8a527e2c8015 | -8.55351 | -62.64151 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d366feb0-99c5-3a83-8461-a4224aacd471 | -9.81617 | -64.28606 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 279a7a88-bbc9-342f-acb3-ac2c66fd7796 | -9.03861 | -65.72435 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10f9928e-1889-3a45-b63b-29407b9bccec | -11.52078 | -52.12983 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |


[Clique aqui para ver as próximas entradas](README86.md)
