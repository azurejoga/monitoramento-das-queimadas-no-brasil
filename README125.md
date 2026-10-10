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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f7eaaf0-d920-31d5-a2c7-01428ac5f34a | -3.57855 | -54.71988 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bccf11d2-b884-3cbb-b8ae-81b572917c5d | -4.30991 | -54.79996 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 094b2b80-e2ac-39e2-acfa-9d5654f818e4 | -3.64537 | -54.51237 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f914e31b-e14d-3a8c-9fba-2b6acfa84848 | -6.32542 | -54.79618 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d406073a-fb6a-3c2e-9319-416845ea7c35 | -4.73459 | -55.67482 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63ddd934-a4c8-3c18-ab21-2fd6373414c3 | -3.38316 | -44.48375 | 2026-10-10 05:04:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce88665a-c026-31dd-ba18-7077203b1ab8 | -3.27845 | -54.70164 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85597fad-797d-39be-8c18-3915973df4dd | -6.45098 | -55.28488 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ca0b32e-d135-30cc-ba81-466d863e261f | -2.45542 | -57.89271 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 697e3c93-5251-3b98-8d85-a333ec8692a0 | -6.12296 | -55.70162 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c9bd7d8-c337-348d-8fd7-dcc201e18aa1 | -2.20967 | -50.82484 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b236632e-2d29-38e7-817d-b05e8f90e59c | -3.66882 | -55.54156 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea75a158-2180-3b05-9941-736f4fc8bb95 | -6.67102 | -55.10158 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6efc23f0-4637-360f-932e-90ea430e17c0 | -3.60023 | -54.66945 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b044ec4e-8bd8-33a7-84fc-817919d18fe5 | -6.04373 | -59.92774 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c18d29b-946c-3301-ac67-351f49473e29 | -3.2172 | -49.43388 | 2026-10-10 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f2249c0-4ab5-3196-a3fe-b50ad8d81d6e | -1.27226 | -55.74508 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8dce1ad-07b0-38c0-8b74-13589d396914 | -4.23531 | -48.72586 | 2026-10-10 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69113512-b09e-30b3-9bff-5a8cbaf444a9 | -3.20963 | -53.85529 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2bcea5f-1413-3a50-b02a-9cb1de696293 | -6.47162 | -55.45446 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c1ec837-f610-3b07-bbf5-406b45c7865a | -4.39784 | -46.52937 | 2026-10-10 05:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c6dfea0-7168-356f-99e6-69e495b90e6a | -4.31053 | -50.79076 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6392ceb2-6d19-38f6-9ffc-a530945ff06f | -2.91993 | -54.0745 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 782a6e96-b716-3430-be98-702dc8acd9a8 | -5.98776 | -55.3807 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 913e24a1-90df-31ff-b833-87427bbc9535 | -3.52221 | -59.2276 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cafe85a-ac07-3315-80f0-ea6a54a0fad7 | -3.00552 | -54.1128 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64ebc219-623e-300e-a6f4-05c42d8780e9 | -7.22487 | -55.14372 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a39a1589-81d4-31b1-bb4d-608a9db43783 | -4.57683 | -54.95681 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4dc92049-7f8f-3e6a-be73-be5f0a79c895 | -6.25981 | -55.90125 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 312f41b3-3eb1-3aca-8a4a-ed519e075c94 | -6.32946 | -59.95909 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccea0176-cb07-38c0-9156-4afa8944ca61 | -2.87199 | -54.1626 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e38d0e73-e901-3c2c-a227-847164cea25d | -2.5125 | -56.1645 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44154ded-2be9-34ae-b0d2-72d5ed6ea595 | -7.19388 | -55.18885 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02edd84d-cb0d-393e-844b-71f6c80c8a81 | -3.20695 | -50.55411 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b327512c-e1d8-3ec8-b7af-abfca18a28ba | -3.18202 | -50.59656 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6a65cf6-c9c1-3ece-9a16-7da9f2a8a7c2 | -5.19138 | -60.31291 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8243388-2cd7-31de-a140-64fcaab038de | -2.67815 | -54.63221 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d446fe7c-823d-3e82-b177-a5abdb02e7de | -3.26553 | -54.01566 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d66c36de-d32a-347b-9a10-4479892b2452 | -6.06603 | -44.66919 | 2026-10-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 335c56af-faf5-3075-a966-97836c6f9e12 | -2.99591 | -53.917 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58138be2-59fc-3901-83ab-ad6968201f66 | -2.73758 | -51.54687 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1afd086-bc69-3586-866f-870cf4c8bfd6 | -3.86404 | -55.96384 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1548cc42-2202-3946-99ca-616235e02133 | -6.50535 | -53.61391 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5c1d08a-8bc1-38ee-8d4c-1ac97862db79 | -2.99479 | -53.9027 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18c03cff-15f0-35c6-a435-523ab823d640 | -2.41749 | -58.00187 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b4331aa-fe29-3a3b-bdb2-5fad6340b57e | -5.86401 | -55.7014 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc3b9e60-86a5-3206-a93c-e9ab0d3d3e02 | -2.99919 | -53.89633 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d871431-e9af-3f8b-92cd-add6b42440d4 | -3.01613 | -54.21724 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a09975f-cabd-3923-9d91-63a0018530c7 | -3.89073 | -52.19186 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a8c5f68-deff-399a-af3e-1e408d4ec7d2 | -4.75469 | -55.68541 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 459452ca-d51f-3792-968c-3c7b0fbcc88a | -8.25391 | -46.43315 | 2026-10-10 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdc8a9ea-c36f-32b3-bd73-1cf089f191bd | -3.20302 | -53.85425 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea1e163a-c7a6-3fe7-88db-6979ac59c87d | -6.48581 | -55.95616 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44dafbd2-44ef-3984-9711-953745741127 | -6.45488 | -55.28191 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cbc64bd-73ee-3adc-bc39-1b94bb542dd4 | -2.96416 | -54.18073 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6abaa49e-7a4b-3eca-943d-58e080a0bf5d | -7.10064 | -41.76176 | 2026-10-10 05:04:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| ece0a7fe-6d6b-36ea-b577-aa63812b5a0e | -7.23649 | -55.17743 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12ed88a1-c9ec-389b-8109-ec8850985afb | -3.28178 | -54.70216 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e005942-42a1-3dd5-bb9d-16cb2b847e85 | -1.1817 | -54.17381 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd9b5877-5377-3c2c-b26d-08ec09d19be1 | -7.937 | -49.74699 | 2026-10-10 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39276107-8323-38c3-a0e8-c96411463708 | -1.29187 | -55.71244 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d30732e-0120-3932-a419-1343ae05572e | -3.44872 | -59.54967 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dd87ca3-24a0-3347-a75b-e8b9b3e6e8f1 | -1.18598 | -55.67208 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb4bfad6-0f3d-34cc-8904-171872de95a6 | -3.5714 | -54.3793 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 246ce3a3-d877-384b-8416-1c0c6a341dab | -4.8193 | -56.08588 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf9bf203-d977-3a78-a29c-914bcb47b024 | -3.85149 | -51.93121 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6c6aea1-398a-3b58-8a24-17b1d32c905e | -3.15998 | -58.62799 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d315df56-9f76-3263-9559-a5925e94970d | -3.95936 | -51.89015 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db6d48f2-ae9a-39e9-966e-9244d90f1ec9 | -3.27134 | -54.06642 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03f1dfeb-dcff-3661-be75-fb550182aea5 | -3.74736 | -59.4721 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d530ba95-3f21-3dcd-9d99-0494a95a7e9f | -2.50171 | -58.07655 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4db95142-a0ac-3a9f-9ecb-24cee09a3530 | -2.51583 | -57.74036 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf4ba1ef-98b7-3488-87d2-0f420c3365d9 | -3.6365 | -54.52521 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea9d934c-2f7c-3a1e-aa7e-25395daaae45 | -5.95675 | -48.91813 | 2026-10-10 05:04:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 464da388-385e-306e-88db-5fddffb81eb5 | -2.74597 | -54.12112 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e45bed5-23e9-33f0-856a-6d2fc9d0a4a1 | -3.31264 | -54.01995 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7db225e-fc3e-322d-afb5-4bd8d8aa09c2 | -2.73714 | -54.1339 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f966c045-f206-369d-8742-ba3ef25b6e31 | -3.15473 | -54.09359 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9e1d8fb-6e4b-3124-b2d6-699bf4dcac4a | -3.98342 | -59.35543 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d41f1d19-cf99-37aa-bb75-e1a5d429eb59 | -2.54633 | -57.38431 | 2026-10-10 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d30d1236-3fed-305f-a73d-dfa403e8d2ce | -4.93492 | -47.4429 | 2026-10-10 05:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09ad4416-0e7e-3e62-90cc-712d365c7e59 | -4.17816 | -48.74657 | 2026-10-10 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2a6b708-c701-3092-8707-67353921c75d | -6.44018 | -55.05722 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa235889-fc07-389f-8d7e-d8851a8b49b6 | -8.3561 | -48.14553 | 2026-10-10 05:04:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5511bd5b-0c81-3a71-a598-7b4f823bb0a0 | -7.20549 | -55.2014 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 185b098f-e740-3383-b634-2b546e5f5cb7 | -2.92269 | -54.07848 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4efecf52-a575-3a39-af94-62dd3f1224be | -3.00638 | -54.79229 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15234250-4202-385f-a663-12ef9027bda0 | -1.28649 | -55.42134 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3104ac5-c56c-34c8-bda1-0ed55a035e73 | -3.01276 | -51.01401 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3942783d-e574-3ce7-9ff3-df62a98a5fbc | -6.37719 | -56.23543 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52f44a8b-cf81-3275-8ed6-a321ea181d31 | -6.34099 | -55.31421 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3018faa3-82f4-31a4-9ada-d8e090a30a60 | -3.74237 | -57.26192 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2018cfe4-342c-38a4-ba8a-ffb6beec407a | -2.58588 | -56.18031 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56a4b2ee-a0a2-3a6c-8d2a-a11f1f71ac17 | -3.93004 | -55.72932 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb0d68d1-a83f-3fc6-bd34-cd04e2e41eef | -2.51152 | -56.14827 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bda099f-6c9d-3c48-9ee8-f996db9e9ca2 | -3.31022 | -53.86445 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 258700bf-9478-39bb-bca3-546406b1a089 | -1.21704 | -55.65706 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9e72bf7-658c-3fe4-ba93-0ea5645ae94c | -3.99994 | -51.0167 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a7d7e6c-215b-3366-8701-6a89cfd00e0b | -6.43941 | -55.27588 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b15949a3-235e-352e-93c3-ce4a5b65dfb0 | -2.8344 | -54.12123 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README126.md)
