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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 891107c8-88a1-3a24-9880-cd37024b8495 | -8.8963 | -62.4284 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a0e6888-3279-35f2-85a2-73ea551cd039 | -7.31485 | -59.61155 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c6922cf-53dc-3e97-9afc-09d9079b9a06 | -9.18137 | -59.5906 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 923eeccd-586b-3c5d-beff-91af9905f698 | -9.19242 | -59.6412 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55bf0456-1c66-34d9-962d-2ab47e1a0949 | -9.16812 | -59.58861 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1618e24-434b-3757-9ace-8868daa2cc31 | -8.89149 | -62.40985 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcdf92a9-9593-3940-9334-1431f7741bda | -9.50883 | -60.55684 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 941dd0aa-9602-338c-b320-0ba89d595821 | -5.74518 | -57.5929 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| c770a4d6-6405-3c4e-9b63-fea4cb553150 | -9.19503 | -59.65474 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e8a5b6d-8394-3159-b787-b122567e5117 | -7.29302 | -59.64121 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c2317f5-088f-3a91-8567-c4ee6b5dc8ef | -6.57722 | -59.87473 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97adf211-b21a-3628-b397-b5da206a03eb | -11.32955 | -55.22362 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 702fde30-0432-3653-a816-9d27ef260237 | -9.92452 | -60.48365 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c430d479-7ff4-3dab-aee3-fa7fdd0306aa | -9.82436 | -64.27367 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 357e3b96-6dc0-3574-82bf-b0c33eb15368 | -9.51419 | -60.51874 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b68dd441-9e10-3d64-92c3-33689468acf0 | -9.20505 | -59.45019 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 449e445f-4234-392a-8f09-cb29f9e7f366 | -9.21913 | -60.78552 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69d22fb5-6645-3a88-8529-69e18e626e6b | -7.10097 | -59.77473 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1e17b98-30e7-37e6-9720-8ab9256133f5 | -9.8312 | -64.27472 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e618cd70-66bf-3f2e-8455-df8a445cab81 | -7.80952 | -63.55552 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 093ac570-236c-3046-bf61-6f29e84c50f4 | -9.18984 | -59.6273 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abeaa4a2-062f-37d5-bbbb-a3d4da41bf5f | -7.43176 | -60.62789 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6c441f0b-79ec-370a-9312-ea2d750e5ed5 | -5.75482 | -57.59429 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e5b03406-af74-3c54-ae71-fb1da843d578 | -9.51823 | -60.55043 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb999181-3216-310c-ae36-63d348b889d1 | -9.2171 | -60.80012 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 034a5d03-d012-3e36-bd48-b9e58d706b29 | -8.89566 | -62.43276 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f57e0a7-85e3-33c4-9c02-d201f84e5524 | -8.99863 | -67.71748 | 2025-08-23 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f3269b2-c252-3ae5-86a2-954ade4b6626 | -9.9608 | -60.18731 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 53673e5f-af9d-36a7-b8ec-ebe0d61ab490 | -9.15843 | -59.59787 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b9f7d59-8b2b-34f9-8a21-cfb263cd2af4 | -8.69777 | -62.87807 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b3e9639f-94ec-399e-ad48-dafe54149193 | -9.16455 | -59.68089 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81365443-3504-3069-932f-7321f3e835db | -10.55198 | -62.74065 | 2025-08-23 05:42:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43dd8820-416b-3aae-be28-6a7d9cc78662 | -8.69988 | -62.87707 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 20f353fe-8145-3e3d-98b9-ea090394a16f | -9.17135 | -59.59795 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1133a046-7944-3089-ae83-4b876159f558 | -8.87792 | -62.42563 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9360b40-ec2c-342f-91d1-cff831ca1ced | -9.5213 | -60.55869 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb6da781-573d-3338-8c22-1b951cd8d6f1 | -8.89326 | -62.42348 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aea48da6-c4db-3ba9-bbcf-d539c0a49176 | -9.50746 | -60.50609 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25601a5d-5a70-3d92-9351-028465d11e1f | -9.19562 | -59.46456 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca5859e6-892a-3118-9992-d97df27e2d29 | -9.21032 | -59.4781 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dbe9c42-697d-3824-a2c1-f33d9c26a598 | -9.03059 | -59.01602 | 2025-08-23 05:42:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bde09b6d-0b85-3627-bd07-1637ed1f5663 | -8.67923 | -62.87949 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 434d8ede-d77c-3717-bf55-456b76ebc228 | -9.51056 | -60.51433 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d74c24cc-a989-3f96-b4a8-233276892974 | -9.25938 | -59.77541 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06e0dc2a-7903-3ab6-91eb-ba3173a9dc83 | -8.69928 | -62.8812 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 54c9c29e-5dd9-3bcb-a005-d7a99510a736 | -6.31039 | -59.8916 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 861df9a9-fa8c-33ee-a6a0-952c8e10b94d | -6.63234 | -58.5421 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c6c96f5-8cc8-3527-aef9-ed5689f5fab3 | -9.03125 | -59.01131 | 2025-08-23 05:42:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14df62a2-d2c7-31c5-b53d-9f189a6077a2 | -6.89784 | -59.89714 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdcf1da1-17ab-35f5-a40f-a6dc6409eb18 | -7.78123 | -61.57323 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f342bd0-2763-32a4-b38e-901e0b9da5fc | -9.95207 | -60.19998 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 66097c0b-aaac-3166-8ab5-47f3fff37ca4 | -8.61874 | -62.61124 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad930bd3-03d5-31c1-bc4b-dadada706510 | -9.15985 | -59.6819 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c69aa8a0-5c2e-3455-88b3-72b675a21ef3 | -5.79532 | -59.22406 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6afd6c3b-8acc-3901-80e3-62bd705c750f | -9.20322 | -59.46359 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ce014ae-cab8-3da9-8cbc-bdeb01361bef | -11.32289 | -55.22767 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3887bd93-10aa-33ec-9064-864d9d468bcd | -9.82492 | -64.26993 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cd98903-d36f-323b-9611-bab20a3b21f8 | -9.19484 | -59.62365 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b21e1c9-aa70-3b7f-8f45-030c5cb37e36 | -9.03074 | -59.01332 | 2025-08-23 05:42:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b07e2ef-d810-33f0-9184-defa1f2018dc | -6.87764 | -59.82382 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3dd6b666-2d6a-3e26-ba2d-0fe6f5729fe3 | -7.62721 | -63.49038 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8494ada9-c5ff-34b3-9218-29c63cf337de | -9.1729 | -59.59119 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b996efa-1940-3e43-88dc-3cc413f00ba9 | -6.31096 | -59.88784 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ea60374-b1fe-399a-8728-2276f99a4a0b | -9.84602 | -64.29227 | 2025-08-23 05:42:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7badd7aa-c363-3122-9e77-35fa15059430 | -5.87709 | -57.7634 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 950622a8-c49c-3667-9433-50964fd75731 | -8.88831 | -62.43166 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4c5e71f-5c7a-3fc7-a184-8db607de994c | -7.73661 | -67.06551 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 756750a4-2d47-3ec5-bea5-824c3fd979e2 | -8.86742 | -62.3995 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02330c9f-bad2-33cc-8789-613bbc491566 | -9.52871 | -60.53643 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e78f21a-1866-3c5f-8253-cf0977fa23af | -9.95221 | -60.18611 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 42a36e1c-c9e6-347e-b306-ad61bafa655c | -9.17104 | -59.60413 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b5a8558-8a66-3921-994c-edfc236b88e3 | -9.20526 | -59.48195 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c996ff8-84f3-3f1f-b261-d675bd7314c5 | -7.90627 | -61.51229 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1177ff2a-8359-35ce-9fe9-53190340915b | -9.22636 | -59.75063 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f3f5d07-c153-3627-be03-f9071327a4d0 | -9.24903 | -59.62224 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6c46f2d-b992-32c0-9047-67e30d96f2e0 | -6.62067 | -60.01177 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db21ef60-1d1a-383c-9f38-bf03ea6cf830 | -9.65498 | -59.63718 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0710487-057a-3c63-91df-6b0315379bb3 | -9.24783 | -61.0206 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 080e4daf-68a8-3075-b35f-b47851e668ae | -6.69074 | -58.86224 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a650cf32-cab3-39b0-be40-f7bdcacc27d6 | -8.62215 | -62.63765 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 998f94a0-dde4-3b04-8beb-b6d91fd32b6f | -7.7293 | -67.06802 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee7843ad-30a6-3760-8191-f464d565227e | -7.29536 | -59.62506 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad0eaea1-efbc-387d-b3be-b6df94722845 | -9.95651 | -60.18671 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 4dded36a-d55d-3390-bf5d-33a4b4999f1d | -5.75406 | -57.59952 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 04714ea8-e934-3df3-bf69-2e27ecce80a6 | -6.8742 | -59.82296 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aba0318a-8fa6-3384-9048-e647a331b6c0 | -8.87728 | -62.43 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f5f7e43-354e-311d-b3d2-71765366632b | -9.20988 | -59.6125 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed8853bb-3d42-37a6-b6de-e2984d5f960a | -9.1949 | -59.45792 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1011d8e-21dd-3c7f-917c-7f7d0580dcc9 | -9.94586 | -60.16842 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 587d8b96-c452-33e2-a870-43309e821170 | -5.61517 | -60.22773 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98bc2f8c-e02e-3a4d-ad8e-491d0f6bd178 | -8.87424 | -62.42509 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49b819bf-1416-3354-b3e7-db133d8dea5b | -8.88463 | -62.43111 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f9cb739-8033-37e7-827d-ab330e75b655 | -9.16725 | -59.59917 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a456a551-f72d-3d87-a331-039a420eef76 | -6.63301 | -58.54023 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bed9e8f4-9ccf-3796-89fe-bcac0f2c1ab8 | -11.2018 | -55.03932 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6aa5a2dd-c145-3469-9c89-b5d3c366277c | -11.1141 | -62.66826 | 2025-08-23 05:42:00 | NOAA-20 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 549339a7-ffbf-3481-a692-65e5037f937b | -6.87475 | -59.81903 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| fe728477-240b-30f9-88bb-0d44cdcd31fb | -8.89262 | -62.42785 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e77374c1-61b9-3bbb-bc82-f7c0a8c50e67 | -7.80262 | -63.55446 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2229a79a-0c2e-3053-a9b7-ba1d377404f7 | -9.9476 | -60.17002 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README76.md)
