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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c43d32e-e0c2-3c37-8c2e-8407749d86d8 | -8.82705 | -68.97209 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 0873a80d-7c4c-3e63-9f80-46bea1926202 | -8.54934 | -70.47738 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6e465d12-bcbd-3806-889f-02c8e4020cb6 | -6.86971 | -56.52123 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| bae495c2-6dd8-3dc8-a0df-36b3a9be9f98 | -7.00792 | -59.5677 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ec4b12c0-2361-37cb-b48b-60f39dd35cd8 | -4.30583 | -59.47352 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 59433689-100e-38a3-bd0b-2ee1a4e311d6 | -6.69592 | -60.11964 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d9c7add1-e198-3caa-ae60-2b6a1319020a | -4.96747 | -56.27301 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1f00586c-0c86-3147-95ba-77033614769e | -6.78729 | -59.42493 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 73d69573-d00a-3e5f-93b5-7759f3c63011 | -6.83905 | -59.94089 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f6c645ae-fa2c-3216-b89e-9ec88ae1aef7 | -8.95259 | -69.46753 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 299ae453-512c-367b-b070-0171ac504c41 | -6.00465 | -57.8361 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 88bdb3d1-e370-3be2-b0e7-f1ac73f2c1a1 | -7.3465 | -72.93805 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| dae60f2d-f86e-3044-8ca9-76cb1d82bd3a | -7.59098 | -61.32858 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6790112-00c1-3536-ac8a-fb55225e54c6 | -8.45184 | -70.70014 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 47be6b4d-f98f-3531-bf3a-47078def406f | -8.05215 | -70.20118 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ee93e70b-6723-373d-b37c-fc360cd45153 | -6.06464 | -57.96454 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a92efa7d-fae6-3987-91b9-7ccda08243e6 | -7.00118 | -59.57323 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bf94227c-7893-3d5d-9778-c3df32b24557 | -6.81487 | -59.71839 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e315d253-077a-3e2c-a59a-0bea62db0552 | -7.00453 | -59.52262 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c18729e4-ef07-3ee3-b702-cfe591ad084b | -6.16953 | -57.78585 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 05735a6d-0045-367b-b120-f14f6260541e | -8.93592 | -68.91602 | 2026-08-28 17:47:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 780b53a2-08c9-3076-b5cb-9575bac4d8c0 | -6.86699 | -59.03264 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| c712fe88-bc4d-315f-be10-f7d077b7d344 | -6.6494 | -58.49544 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9f259b68-8b60-3312-85d7-481ef4697cda | -6.38421 | -65.24015 | 2026-08-28 17:47:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 132f9b0b-c8be-36b7-b1db-c645bbbcc22d | -6.91748 | -59.48137 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0b3e0627-9e24-3b55-b267-2cb206699507 | -6.00339 | -57.82858 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 277ec19f-af46-358f-8674-6078afeba661 | -8.15433 | -64.00208 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 46886e61-62d7-3dfb-8bdb-98449d129c9b | -8.54927 | -71.47775 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 785c9bf5-d644-3538-921a-73710e4f600f | -8.50502 | -71.45867 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0dfdec71-0eb7-3301-92b9-c914400c685b | -8.0272 | -69.88945 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c8efee04-2736-3dc5-be5d-4eb40be913e7 | -7.91465 | -61.31483 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9fa90d34-0c01-374a-919a-354ef4bbae19 | -6.31944 | -54.73809 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 46da52c1-58d3-365d-bd7f-792745ef476a | -8.21525 | -70.49812 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d2fda8a-daa9-389e-b610-eea77a205c49 | -3.77297 | -62.01041 | 2026-08-28 17:47:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 886786b0-b481-3550-9f44-ebe6fdbf9eee | -7.47836 | -61.41496 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| f6d9142c-2327-3849-8f28-0c23eeaff82b | -6.58371 | -55.43885 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 657799a2-da37-35ef-91f0-ecbe9f9b44c1 | -4.31228 | -59.47071 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e4a4179d-65ed-3028-9bdf-2d69fb19b3e6 | -7.60236 | -61.33436 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6bc73cb6-d166-3beb-aa45-ad7a254223b3 | -6.08216 | -53.81495 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 75895ee5-9204-3920-bc97-2524efcb255e | -6.77906 | -55.68499 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 64c78ebb-cc66-30bd-bc3f-2290df87b790 | -6.94598 | -58.94841 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 331085a9-047d-3596-a2c9-aca625ec0305 | -4.15025 | -60.76388 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 158.6 |
| b72e9c6c-92df-3dcd-8869-4656dfbdd621 | -7.92215 | -61.36264 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e5bf8792-a0cb-3aae-8add-dba9ed4b7f5e | -3.43431 | -59.39806 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c383f112-9d91-321b-b307-dc645f8b02f1 | -6.78352 | -59.42549 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| e595c8b8-026f-3694-ad7c-0dbc5f13fc88 | -7.82367 | -73.40179 | 2026-08-28 17:47:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 52aab54c-f540-3161-92f8-402db93cd6db | -4.05971 | -60.63988 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1f84863e-25f0-3c88-b270-3c162cfe41bf | -9.03146 | -71.43259 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f4ac95c2-2bae-3d16-8d7f-887c2f93edb9 | -7.91933 | -61.36684 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cfefa72a-3f3e-3ca5-bd74-f424d05f4644 | -6.6591 | -58.5046 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2758c41e-919e-3ab7-9613-35f711336986 | -7.92273 | -61.36631 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c80960d-750f-319b-a7ed-5dc3a92830bd | -6.7986 | -58.98786 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d6ef6966-d950-3dae-9a2f-993e49afe852 | -9.0818 | -68.47703 | 2026-08-28 17:47:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5f2e41f0-79f1-3bb7-96c2-60f10d4d42b2 | -3.43115 | -59.40373 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6998857c-4141-39c2-aac1-b0ac44917e01 | -7.579 | -61.31906 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d981e4af-432e-313b-b317-35adf9dcdc46 | -6.98938 | -60.66106 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 85155060-2ec9-333a-af39-a8fcaeacb460 | -8.64213 | -66.53218 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 303ee324-0ddb-3d62-a7f7-45d489d5699b | -8.32725 | -70.744 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 452e65d1-db6f-3ffc-9ef3-3180b3ea8ab6 | -6.32047 | -54.74416 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8d2eccc3-9db1-30db-a4cd-7abfc89205be | -6.94883 | -59.48558 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4f1b0a27-615f-3cfe-9039-f90d660a2935 | -7.62397 | -61.33857 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| abe8b1c0-8625-3580-9c66-8be7b5f9737d | -8.22073 | -70.50258 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 22.7 |
| ebc8f349-c47a-3a4e-a69a-de784c1a9c17 | -8.277 | -72.75851 | 2026-08-28 17:47:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 290b1d3c-5194-3c05-935f-2d7f789c5e45 | -7.50877 | -71.93237 | 2026-08-28 17:47:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33108d86-3fed-338c-9a99-19805ff8a0e9 | -8.96923 | -70.62218 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d9b845d7-c3cd-39b9-9ef5-ee121a82834b | -9.50902 | -68.57561 | 2026-08-28 17:47:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e77781a5-6c64-371b-b10b-72a2efa92d7b | -8.68049 | -62.95185 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3a0b230d-faa4-3bfc-9728-453930d196e8 | -8.82215 | -68.96856 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 300005d7-2144-338d-bc18-01d690cfb8cc | -8.28022 | -72.82576 | 2026-08-28 17:47:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 21.9 |
| ce212e48-f325-3b64-a4ea-0b0c69b74adb | -7.92555 | -70.66036 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 36.0 |
| c8c2796f-9ea4-3b8f-881a-dffe2bd8917c | -8.43316 | -70.69857 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eff40abd-c922-337b-8d17-cca119273089 | -4.31201 | -59.46262 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 35e2aaff-1a79-34f2-b1f0-6c1809afb32e | -6.89328 | -59.95095 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 286fbfc1-1b3d-3b84-b5d9-65959be3e176 | -8.79514 | -70.83214 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 72314af6-9b0b-39db-90aa-a42b7e7ab020 | -7.5795 | -61.3 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 395f090e-bba3-3c4f-af4f-55ec4d228cc4 | -6.016 | -57.82655 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 48c21219-3c48-3534-88dc-5c24f9eca6cf | -4.20028 | -55.24068 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| be6d956b-8241-3553-8dc6-be57439d62dd | -8.02395 | -69.89938 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1551ea7d-9428-3b32-b106-26e5c13969aa | -7.57609 | -61.30053 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 78ee1120-bc27-38af-92d7-cd043a6da7b3 | -7.02378 | -55.70797 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7ba5dada-bce1-3829-9d86-785d3b53da18 | -8.9152 | -70.86699 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 83b578b7-0b60-3bd4-a6e8-c381d17c1810 | -3.5474 | -54.49162 | 2026-08-28 17:47:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f695c8e3-8032-3097-8bcc-5033155d2b55 | -8.56917 | -64.17055 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 2dbb0c2a-7266-32a1-be04-46ef74ce5762 | -5.88481 | -57.76766 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 263.3 |
| 3e0a80cb-1261-308d-99b1-1c003119dbae | -7.5904 | -61.32488 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 62c6f5b7-bd96-39dc-8578-2ca4105c9f80 | -6.9429 | -59.08863 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a4c7911b-d301-3247-91b0-28160d5f4806 | -8.87551 | -71.47546 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 21.7 |
| e7bde0c6-22be-3153-ac3a-955f19a30603 | -6.73839 | -59.64448 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1d17acfd-d5c8-3ff4-9220-5d1ca053b3b4 | -8.90446 | -72.70773 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08c0d330-e374-3381-9f44-030e962b0b91 | -2.96052 | -60.97912 | 2026-08-28 17:47:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dce0f6ec-3f47-3485-9422-36141fce3ed5 | -6.6926 | -59.43523 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 93f47c84-8326-3afc-9107-9ea5cf977f6d | -7.4968 | -55.28162 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| d2b820df-a58c-37b0-9ac1-104d7ecf7b8c | -4.45659 | -55.38932 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9a821e88-144f-3b8e-9ef1-acc3af182cd0 | -9.07811 | -70.09152 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fbeda303-6a47-3c49-bb0f-7718c2e8073d | -6.84567 | -59.93548 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ee821088-d83c-3755-96b6-0580175e0951 | -6.16467 | -57.78256 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 37fd788c-fde9-37b0-9bef-f3f89ebd8702 | -8.55412 | -70.47672 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7744ea99-9bb7-340a-ade6-47fc442e047b | -9.45125 | -72.11748 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 72a896dd-b35f-3f4d-9699-588e0f642506 | -6.87161 | -59.03674 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e6827867-a799-3974-aca5-fde49c044059 | -8.21144 | -70.4361 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README151.md)
