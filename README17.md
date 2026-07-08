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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef9a14c5-3fa7-320c-8844-61f233cacb03 | -12.78843 | -44.45619 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 24a2a95e-d69d-36ea-86ab-543fa8bbd516 | -14.86107 | -48.31361 | 2026-07-08 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf59e634-7233-3180-a0b0-6f591ebaebe3 | -12.74701 | -44.44995 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5a9c9e6f-9346-392b-a754-59088eacd7b6 | -13.44116 | -43.85361 | 2026-07-08 04:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2d59c2e-36e8-3a0b-adb1-991413d16a7a | -8.59687 | -48.01499 | 2026-07-08 04:25:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a87cc78c-4b16-3280-8afe-a0ad69874e6a | -12.35734 | -47.42181 | 2026-07-08 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35dbc1c8-b5dc-3da1-8b91-0d6a76b472f9 | -14.23041 | -45.41951 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2d90e54-3b62-3517-ad9d-0db643215d82 | -10.92959 | -43.05563 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 276297fd-7cc8-3c1a-b93f-43a71d02015c | -14.86046 | -48.31736 | 2026-07-08 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91058b2e-abcd-3493-ba7b-077bdf7aa3b5 | -10.92251 | -43.05455 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d1da3cb-f7cb-35bd-815e-e0e98b68cea7 | -10.9237 | -43.04647 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7757b175-4bf8-3308-b88a-89da09f7de0d | -12.49733 | -48.25586 | 2026-07-08 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32408caa-f735-3aef-8aee-088a029821e1 | -9.23329 | -50.14718 | 2026-07-08 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a237c90d-c528-3378-af8a-5a32ca200ba0 | -13.95568 | -45.21178 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b5e2a45-37fa-3df0-a326-84fb38a6cbf9 | -13.7659 | -46.28672 | 2026-07-08 04:25:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4e29017-8038-3b8e-aaf9-e0a8ae563e80 | -11.80581 | -52.52623 | 2026-07-08 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f18574e9-b3f8-34d1-96fb-5e5a213ffd85 | -13.33439 | -54.37711 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e58d87d3-f6c2-3cca-ac2c-482e1b68d6a9 | -9.36693 | -48.80659 | 2026-07-08 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b3cc6015-f577-37a6-9c06-7416453818d2 | -11.96431 | -46.95102 | 2026-07-08 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a69b3079-0249-3f33-a18a-996de1c2066c | -9.3084 | -51.9167 | 2026-07-08 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f2301258-a439-3601-af53-af66b9684ad2 | -10.942 | -43.04512 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cab0a73-b8ee-3c13-a377-d03c1c31697a | -8.11854 | -47.88203 | 2026-07-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2f3435ba-6d64-39b8-a52e-7852c5a71716 | -13.29267 | -44.61657 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6cdd676-1bd0-3a31-8975-499390f11fe0 | -8.73703 | -49.44723 | 2026-07-08 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b9830e7d-d1fd-39b7-b67a-79467427063b | -9.56708 | -49.1097 | 2026-07-08 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd2c4c02-6f74-3af2-86f0-60cb34ebfa05 | -14.23095 | -45.43823 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e50ba51e-50bc-3193-82bb-ed4cce81d605 | -12.50076 | -48.25644 | 2026-07-08 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbe5a4f2-7980-3017-8c5d-a144b42c1e63 | -12.35399 | -47.42123 | 2026-07-08 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 919c2bda-f7d9-32d2-9d93-81ab133c2393 | -13.52738 | -52.94652 | 2026-07-08 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 848cebb3-20f2-3ccd-89c6-39e3ae57888e | -8.19972 | -49.47884 | 2026-07-08 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 228a9536-3b71-3412-8827-6794c0583682 | -13.27399 | -45.17197 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47758f8f-91ef-3e57-9bdb-5dee969a7738 | -9.3753 | -44.72223 | 2026-07-08 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb0b4496-ccf4-3c02-9d84-9de2501605d5 | -12.76305 | -44.5325 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4277d483-9bfa-334d-993f-4cad765680e8 | -13.27678 | -45.17613 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c3fd94f-9a80-3318-bc34-144c4bf2ecd8 | -10.92724 | -43.04701 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f153b26c-f017-3c92-8768-436f8f32daab | -10.89482 | -44.31445 | 2026-07-08 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1460f9a0-c949-3801-b05d-c1b61e9d45aa | -13.94815 | -45.22564 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 57b71adf-8506-3787-b9b1-4df4c8ba3f73 | -13.82342 | -44.05558 | 2026-07-08 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2968ff5c-72f6-3088-ad91-b1e34799aad6 | -13.28292 | -45.18084 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d48bc520-5fe2-339c-8546-e2ccd90db782 | -9.74137 | -49.03417 | 2026-07-08 04:25:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 221853fb-9ed7-32cb-ab5f-ec1f4a1aa0d9 | -13.5276 | -52.94529 | 2026-07-08 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3af8525-5974-3a60-9fb9-622b4c20da26 | -14.23151 | -45.43459 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e58fdfa8-7cc4-3ae3-9a51-24466ba5dde8 | -10.94789 | -43.05428 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| deb87913-a675-30c6-ba9e-c90cfed2e5db | -11.93024 | -44.70932 | 2026-07-08 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78bcc429-fb42-3d2a-bab1-241183b7a9ba | -13.532 | -52.94606 | 2026-07-08 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 992648f4-7f06-3d67-8971-92dfdc9a103b | -14.48772 | -46.72863 | 2026-07-08 04:25:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7caf87b-5cf5-308b-a845-98ad84afb66c | -10.03521 | -49.62546 | 2026-07-08 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c3c5892-4470-3de7-868b-e2f76cd5f4fd | -14.85769 | -48.31308 | 2026-07-08 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60d5cddb-edf7-3976-b91f-78beb578c8d4 | -12.79525 | -44.45724 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 244e54af-6f6a-3122-b250-efc1c006c6e5 | -8.59818 | -48.00701 | 2026-07-08 04:25:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 51c612e6-43f9-3e64-b4d7-95814b542045 | -12.75204 | -44.53098 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ac55acb6-6dfe-3002-8b9c-065e42767d98 | -13.91565 | -47.35216 | 2026-07-08 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6773829b-9ba8-31a7-aee8-48a156ac03ff | -12.36069 | -47.42237 | 2026-07-08 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2150044a-2309-370f-a29d-8189a8dda42f | -13.95903 | -45.21233 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74d634b7-aa44-3bc9-b379-82e62b754830 | -12.76022 | -44.52824 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 0bb88f34-37fb-33c0-8e13-dc1be5092fc9 | -13.5192 | -43.98734 | 2026-07-08 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b1da455-2ec5-38d1-a95b-7185a79725f3 | -12.36405 | -47.42294 | 2026-07-08 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cba64e19-021b-3e14-aecd-ca461057b682 | -15.57639 | -48.23801 | 2026-07-08 04:25:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 206109ba-d926-366f-86a3-2099f6736356 | -14.23207 | -45.43095 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e82a70f-43e3-3a4f-a1dd-36142c944e35 | -11.96764 | -46.95157 | 2026-07-08 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 87530a45-e11e-3762-8259-fbdc1a0961da | -9.33461 | -47.91732 | 2026-07-08 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1117200a-c0cf-3994-ae09-b9e42c4c5748 | -10.03145 | -49.62481 | 2026-07-08 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04ca10fd-4558-341f-b9d8-bcceb54b44fb | -10.83082 | -49.37912 | 2026-07-08 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67a85311-bcb7-3f5a-adc0-70500cd5c11e | -9.37585 | -44.7187 | 2026-07-08 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11c6f0e2-4294-386d-9e11-1867646ae1ff | -12.32545 | -45.85688 | 2026-07-08 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd3f5899-62c8-3a76-b2f3-9c4a40ef781e | -13.53882 | -52.93386 | 2026-07-08 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81de5b63-c1e7-351f-a94e-05bfb55bef5c | -12.78222 | -44.47439 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdd86b1a-fdb8-30e9-8ac5-c4d7677e0f23 | -15.81475 | -41.89632 | 2026-07-08 04:25:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e7e3d1a7-89d5-3c03-9e85-364ec734515a | -9.22864 | -48.57777 | 2026-07-08 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cd0f19c0-25b4-3f59-8d24-2da91c318d27 | -11.69845 | -44.14079 | 2026-07-08 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 066f354d-5f97-3741-b211-a348a6002e4f | -9.15576 | -46.47189 | 2026-07-08 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef95a689-7523-3097-875b-b311b220da8e | -13.28403 | -45.17359 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bb79a78-fa01-35a3-a0b5-1aaafb2d9d42 | -13.27454 | -45.16835 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5043dd6-4be6-357c-9684-0cf5c4e66828 | -8.59531 | -48.0024 | 2026-07-08 04:25:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcf4359a-7488-3632-877e-38ebb213639b | -9.56783 | -49.1053 | 2026-07-08 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 863f1468-c58e-3009-a1cf-e32cc91a4c42 | -14.80847 | -43.56364 | 2026-07-08 04:25:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 450e7222-e391-3457-b05a-3a96e5b24f2c | -11.32209 | -54.47603 | 2026-07-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0e62064-eb8c-3c6a-96e6-f0207d7d98f9 | -10.92429 | -43.04244 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7e0d578-77c7-31fd-b817-f6ebc87fdbb1 | -12.78106 | -44.45888 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 78dccf57-d8c3-3d51-afae-ce6652c886f6 | -13.53994 | -49.30068 | 2026-07-08 04:25:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3474a4f-b242-3558-b097-11246de43032 | -12.45443 | -49.58566 | 2026-07-08 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99617912-05b7-3e24-998f-07e0d9d1305b | -13.28734 | -54.41334 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e31f17f-1a01-3d29-ab26-66f1ff505225 | -12.62955 | -44.65216 | 2026-07-08 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31c49782-82d2-3da0-b882-9a8c46f4ac4b | -13.94759 | -45.22929 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0fe8a24-fd0d-3ada-a2c8-27095226eb48 | -13.32852 | -54.38166 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd625599-a35c-3a12-b2ec-9bdf7f2f00d9 | -13.95151 | -45.22617 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4fa3ffa1-bedf-3826-aa20-d7806b14e117 | -15.16726 | -43.82353 | 2026-07-08 04:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72cecaa1-e57b-3e4b-8ca5-099d6389e1b1 | -13.77196 | -46.29135 | 2026-07-08 04:25:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c31b827-b4c0-39c1-bc50-b8c4b1997337 | -15.16369 | -43.82298 | 2026-07-08 04:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18febdf2-0b8d-37a8-bea0-b0b3c5e4724e | -9.73843 | -49.02919 | 2026-07-08 04:25:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e01a76b7-bace-3577-afc3-fcf3335482d7 | -14.08086 | -47.29615 | 2026-07-08 04:25:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef4899ad-7bb8-3932-bdda-5426898a3f9d | -9.33525 | -47.91344 | 2026-07-08 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecc3e6e8-3385-3a44-9005-554f8a3f7c92 | -12.85034 | -44.39279 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1886b63e-7b36-38b1-8d8e-ac1898fdfa30 | -11.96489 | -46.94745 | 2026-07-08 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 751a46fe-aa76-35a1-81b8-0113b94335b9 | -15.81076 | -41.89564 | 2026-07-08 04:25:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ae94a7b5-d610-3746-a854-941af45c8c7d | -13.91016 | -47.34388 | 2026-07-08 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5321234b-e0c0-36f5-a263-15092c555604 | -15.23608 | -48.57443 | 2026-07-08 04:25:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bbd5008-10ea-33da-8e7d-acc33805a52f | -13.28124 | -45.16943 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ba72406-a5e5-3e5a-b162-75e16d1ff48b | -13.29217 | -54.41436 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15379e37-20db-3354-afd7-32147779cf87 | -13.27734 | -45.17251 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README18.md)
