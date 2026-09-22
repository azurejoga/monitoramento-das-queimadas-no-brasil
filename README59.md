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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5922c72-7fa8-3eed-be05-ffc2e9ba8128 | -6.79759 | -58.79086 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9dc41dd7-2eb9-3074-b4c2-581502e50314 | -6.77727 | -55.48795 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fda45c09-b95a-3e2a-a3ec-990d45680414 | -8.80758 | -48.76046 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a947d285-8d59-3062-8d24-3d3941237f97 | -8.83372 | -49.23894 | 2026-09-22 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7274135d-db33-3b78-aaf1-728779a40bad | -8.12568 | -62.87683 | 2026-09-22 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f026086-39ed-360c-a46f-cff24ab2f851 | -8.62798 | -54.63266 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf64cfed-3e49-3844-b4d6-2d5780ef14df | -9.7277 | -54.3505 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae32604c-9919-34c3-92bd-764b2feada6e | -5.75771 | -45.08572 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 20c42d7c-2e6f-3156-ad1d-ca003e30c1af | -8.74544 | -52.35688 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2efe827b-c653-3220-a487-71d8981515cf | -4.71579 | -49.84099 | 2026-09-22 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1f90a83-f906-3f4a-9db4-59b610c6e6d3 | -3.72164 | -60.57993 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31cf4e8c-71d9-3602-a8d5-2805f1a6c3b0 | -5.75402 | -45.08096 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 7a19ca1b-493e-3b62-b0a9-432f081f8dc9 | -3.28788 | -57.85521 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 53b9bee7-f74d-3712-abe6-07aa5c6ca935 | -10.87544 | -50.15805 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84b84993-a162-374f-97a5-67aca8e51b61 | -8.79343 | -44.27404 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6dfeb3ba-a40e-36ff-8617-6632a7d837ce | -6.74385 | -59.07648 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76a4c620-c987-3e7a-aad9-cbc426f7b3b9 | -6.46525 | -59.97033 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ad5dba6-1a34-3163-981c-02f12832ccd1 | -8.46457 | -50.90789 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0300553e-ae6c-3982-a8be-d8b1b780614e | -7.13725 | -48.43662 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 890cc54e-c384-3951-9bcf-493bf0cb3337 | -10.69162 | -48.71861 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd7ac59c-b801-3c21-a176-2390776472eb | -5.68389 | -43.42862 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fd5c1ed-1c94-3e2c-88e0-63a0e6fbadf6 | -6.13898 | -59.94145 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 234c5e4e-4759-3ab5-8022-f49cae0dc866 | -5.87239 | -52.06321 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 170b4637-39a2-3ea9-a69c-8aca51de90c9 | -3.05225 | -54.41416 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 339d8f96-a666-3968-ae75-4abec407e1dd | -5.65576 | -43.41938 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8045a1f2-657f-3456-809e-fcd9b0d9db7f | -5.87572 | -52.06374 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a27203d6-0177-38b7-b061-0213b1bc911a | -7.24913 | -55.59348 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 732c3da7-1a0b-3400-b54b-4523218ad348 | -4.66268 | -42.08883 | 2026-09-22 04:46:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 45168b83-7f76-3546-b514-43d9e4520d1d | -6.42752 | -55.6088 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 805f5637-0bfb-3267-8cbc-61058aba4ab9 | -10.25502 | -45.49067 | 2026-09-22 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22230424-9368-38c4-8f8d-a09e9351d9e8 | -6.29278 | -57.74552 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee87adb8-469b-3801-8d80-61ed7383f73c | -3.48302 | -59.56436 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96dcc479-bfd2-3d90-a4e7-8b399cfce5e2 | -3.45401 | -50.60718 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c12f627c-2e3b-3388-a4d3-272571074680 | -2.89708 | -60.05797 | 2026-09-22 04:46:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea30217c-85d5-32ce-8741-ce6fd9d7ee93 | -6.9765 | -47.50565 | 2026-09-22 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c448f8e4-e944-37e1-9108-4e23b0813f6e | -6.19175 | -57.77365 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2f36d23-2ff1-33b2-85b9-4e2f31b4d90e | -7.94606 | -45.64322 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e87df1a7-dbee-3741-b039-702203a239a7 | -5.62319 | -43.3714 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0333b185-bc2a-38c6-9431-fe40c17310b1 | -6.0121 | -47.90506 | 2026-09-22 04:46:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76761a2a-9429-3718-a96b-3da03583a24f | -4.52244 | -55.66301 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc207109-a19f-353a-9fb1-f465abb30510 | -3.46152 | -59.5308 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 527d6930-9ea8-3411-8ef7-d05bb76b7b27 | -4.30682 | -49.12309 | 2026-09-22 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bbffc7a5-b025-3db1-ad2a-941d7f75508e | -5.88035 | -51.57928 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f19a85dd-5a6e-3c6a-adf5-93e9118b6ef2 | -8.14835 | -54.81145 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7052f2f-290c-3c04-911b-bef2087c62cb | -6.79102 | -59.94991 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d605db9c-728a-3961-9d34-ad92982f91af | -3.36425 | -50.76566 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55e2ec4d-7900-340f-8996-96416ca0f31f | -8.60712 | -54.60419 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5274e7c-06f0-3fd5-9d59-04a322888cb5 | -6.64628 | -50.06628 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96a20db1-4836-3b8a-bfd0-ace36373e1c7 | -3.57971 | -54.56243 | 2026-09-22 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85e31a73-5eab-3b29-8807-faded9130820 | -6.44834 | -48.44245 | 2026-09-22 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d525d6e-1707-3c97-99ab-78a64b82d1c7 | -10.84453 | -50.15331 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53ebb077-f278-3d01-a2fb-43fa3e4e78e3 | -6.4857 | -44.16869 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f7a5a17-3b5a-3590-afef-b5a81cf478e5 | -4.18369 | -51.24697 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3278cde3-6fda-3bcc-88a7-f126ab4cba31 | -6.10415 | -57.67884 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2ad413fd-b937-37f7-ac3c-573c8c25f681 | -4.30344 | -49.12257 | 2026-09-22 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b71f29a-247c-3fb9-a81d-071d43fd225c | -8.89824 | -62.37189 | 2026-09-22 04:46:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0641fcd-fd8e-399e-9c71-69045e9ac460 | -5.81959 | -53.51395 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e4a1c58-011b-3e21-9020-a3e349418717 | -3.44741 | -50.60616 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7d43e43-69f9-3c5e-8336-8949d1a003be | -11.15056 | -42.84184 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 62d67e48-64e4-3cc9-9f12-9f7fd5f01560 | -5.93799 | -59.97898 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42362aca-1b1d-395a-bfe9-2780ff4b10ca | -7.83464 | -45.2581 | 2026-09-22 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57238e06-b377-398c-93e9-eb2c106e041b | -2.40804 | -58.27895 | 2026-09-22 04:46:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 917fe0fb-5e78-3533-88ec-5467ec27b52a | -6.09331 | -55.56088 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d40b12de-283a-3fd8-a178-4fa3882bfede | -3.45508 | -50.60031 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee66d5ac-dbd8-3ae8-9c3b-fddd7e1fd28f | -5.82617 | -52.20398 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7ae7a37-b7fd-3086-8567-0dd4fac10cfe | -10.68251 | -50.76241 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abb84ba4-899b-370e-bfc3-19720f98b228 | -3.82045 | -50.63307 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faab0f3f-a618-3244-9af5-147a8bd0c7bf | -8.92128 | -50.90039 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1be4d7af-1e8a-337c-a7e6-f3bc2e8ff940 | -3.06574 | -54.40242 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6818d8b-0e47-3272-811b-ebe5bcfc6e57 | -9.53768 | -45.38645 | 2026-09-22 04:46:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5829c736-bd42-3000-a79c-3f3933e60b37 | -6.66207 | -50.8859 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3af041bc-32e8-3e65-8a84-db03fc7f6627 | -4.27659 | -55.44547 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a4b36dc-a4e0-3405-978c-8e9dcfbc33a7 | -11.67313 | -43.46561 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15140989-50c7-3918-92a1-e40e74fab753 | -5.68463 | -43.42349 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3ccef16-3a98-360e-aebd-3a81201ff2bf | -10.84509 | -50.14951 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaad42e8-ae5c-3e27-ad97-f4361cc01e6d | -6.44761 | -59.96954 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f62aa24-57fa-3e4d-915e-824fd19f9381 | -5.83573 | -52.12228 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7741c41-276f-3af2-9b93-b6e05efcd351 | -8.25586 | -55.29441 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f1ac9b5e-4c11-317d-88d9-6fa43ab6bf4d | -3.9058 | -60.59325 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c5c191e-3dfe-3fb7-a200-54a6e20aa9c5 | -6.25049 | -57.77913 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ac722a0-a188-3dc6-9bf3-aa0b1f9df3e7 | -11.4129 | -45.37877 | 2026-09-22 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d394289f-15fb-3694-9733-8dda9d6be2fb | -6.03736 | -53.27788 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d8d1379-af9b-3f16-b11f-9c1d80536c8b | -7.94122 | -45.64665 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d04f81ee-cf5e-331a-8ac0-ffa4b39739ed | -6.0012 | -55.67997 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc29a251-91d6-3eed-a109-e6cd466b0962 | -7.12779 | -48.42688 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4cc58c50-b2f1-3fdd-a6c9-a8c9d21e30eb | -9.23702 | -57.14895 | 2026-09-22 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 665c1db7-6312-3fa8-9f30-3ead037264b8 | -3.39299 | -59.52252 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4874c932-5c3e-30a9-a6ee-2e4899b5516b | -8.77913 | -49.95304 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 641bbcab-0349-3f2f-a475-1fe3765fb026 | -6.00348 | -57.7127 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56721507-b619-3713-8a33-16576d0c9166 | -9.39553 | -51.59516 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e6a5ae9-f278-3290-89da-9e1e78ed1557 | -8.25643 | -50.86866 | 2026-09-22 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fe4c754-2715-3042-b165-786d34e1fe75 | -6.69937 | -59.95999 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4964c26-2e54-3872-a4e0-22cae686d7bb | -6.55205 | -45.5692 | 2026-09-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44b0e095-c98e-3a64-9d01-8c63e4a1c36f | -6.92347 | -59.62744 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0649ecb-97cb-3cb1-853d-9cdae8479659 | -9.08003 | -60.43751 | 2026-09-22 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8246efd-1d62-3a7f-838c-6e5d22442b79 | -4.22314 | -48.62009 | 2026-09-22 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9145005d-433f-39be-8adc-d13ee6476128 | -5.85745 | -52.02839 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42b95eb1-b306-3ef7-8ff1-8951df68f40c | -6.91242 | -42.96229 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c977d3bc-6d4c-3cf8-ac18-9a65dd4f7ee5 | -4.79136 | -56.01004 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cca15fc-97dd-32b7-903e-b61e8ec0963b | -5.91407 | -57.68108 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README60.md)
