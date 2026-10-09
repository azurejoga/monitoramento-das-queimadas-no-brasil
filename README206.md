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

## Dados Diários - Página 206

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a19af7d-ab4f-3328-8471-24c6c0f67667 | -3.45498 | -59.26539 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b398f3f2-dfab-3aef-910e-dfb7edcd0af7 | -2.57156 | -57.7867 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 094bbc3e-43e1-34e8-ba49-0d9b0af37a1d | -1.44908 | -54.47062 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 190e507c-af1f-37a7-b136-bfe3b4ac6f52 | -3.9655 | -51.86903 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9ef7598-ba9b-32e7-882b-407018e72254 | -9.71889 | -46.9529 | 2026-10-09 05:23:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afe77301-5612-36b4-9044-260953b54285 | -3.46218 | -59.26295 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c1a2a2f-4456-3cd9-afa5-5562b5aec832 | -2.36043 | -48.88367 | 2026-10-09 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3d67190-4578-3583-beb4-92231c0739f3 | -2.51584 | -56.26402 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab4bcc80-008d-3a3c-b231-0b0c3a255c72 | -3.01766 | -54.0457 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdb04dd6-158a-3858-9115-7d44b709d176 | -3.0084 | -57.16903 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45807dfc-f226-321b-b149-573f07e186e3 | -3.17104 | -50.45087 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1557246-aaeb-3714-b9f9-319d3442ff7f | -3.69285 | -60.54278 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca262207-525e-3eb2-abe2-1b8c001b6ae3 | -10.308 | -59.45351 | 2026-10-09 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ef63f85-f601-358b-b048-12220299d50b | -10.24566 | -59.0272 | 2026-10-09 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5d0d7c9-e10f-3f75-9750-79f15c32586e | -3.51448 | -54.53219 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caf81401-abe9-3dbc-ae87-fde3e8ddfbab | -3.84483 | -55.91417 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 831f4a3a-0276-396b-b8f6-c0b8ab57a9b9 | -3.99075 | -59.3572 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 869a5950-eb6a-3645-9886-e025bcdc965d | -6.92221 | -59.27753 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a41771-1951-3f36-b7b3-d7f17539de07 | -3.25732 | -54.03441 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 213a9f66-71ee-374f-8126-1efd1e80e090 | -3.00876 | -54.24483 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f73f0fa1-8158-38c8-bce1-c046b856b3b3 | -3.43959 | -57.96944 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99957810-16f9-3333-bfef-b54409fb4de3 | -3.76623 | -57.16566 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4e0f91c-9f9d-3370-969e-a8eac63ec261 | -2.57756 | -56.18179 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e443cac-e1f1-3683-94f3-6e4011994031 | -3.28197 | -57.84877 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00b67756-6c1b-3b40-961d-816acc6805fe | -3.42976 | -60.21361 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4bade76-44b3-3850-b56a-d63b67c7dc24 | -3.46652 | -60.2495 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24408442-d863-35bd-be2a-dec4454a3de5 | -2.5828 | -56.15207 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 207277cf-8417-352e-a1ac-d5d07a1e9b29 | -1.4075 | -55.41682 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24dfde85-02a8-32f9-8cef-1087070f943e | -3.11748 | -53.7935 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4f1b448f-e94f-3b64-a8b4-382bbf3a3a12 | -2.581 | -56.18232 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f55f6720-c86b-3b98-8785-d593c7a66406 | -3.30465 | -54.06146 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 300ee340-6036-32a3-a6f6-3530389ca81e | -7.22854 | -55.08488 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32676a96-551d-32f0-b173-af91bc4d863c | -6.99975 | -59.10897 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51af56ee-ded6-3b36-95f7-f876e0cbae79 | -3.91371 | -55.74994 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8aa4c4e1-5c38-38e5-a5c4-a3e92878347b | -3.47576 | -59.51612 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0275ee7-e572-3ecc-adbd-500a069e386e | -8.49287 | -54.62582 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51bd70f3-72dc-3677-ba5c-738cc67e1ef7 | -8.70107 | -62.419 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3e782fb-7f4e-37af-aebf-4cdd08099281 | -2.48297 | -56.11352 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ba51e79-b041-3432-9d63-530c1b950ea0 | -4.53167 | -49.67306 | 2026-10-09 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c729cd8-ac0d-3e29-b358-1f0d4dc60be3 | -3.6693 | -54.50599 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed1f9df8-0a48-3f79-ba9b-a3902d9a5c1e | -2.51869 | -56.26826 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3a160ef-7fee-3e81-a148-000df0f0e501 | -11.89986 | -46.56848 | 2026-10-09 05:23:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46039c9e-4a40-38db-83f6-1f17f3fb2856 | -3.26702 | -50.39339 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19b88d74-af52-369e-a200-eaad3144a1d5 | -3.4606 | -59.56786 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1f41cc5-b688-3a92-94ea-7d732ad4de8e | -3.10884 | -54.17078 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b217c43-32d8-3cf4-8b74-a9d7372c5ca3 | -2.88281 | -54.16285 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd3a93df-190d-3f5a-afd6-4cf545a8d7ec | -3.11962 | -54.17719 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c7fa1e2f-baea-372f-baf6-523041ddceb4 | -2.3119 | -57.98969 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc3c2e17-23a1-36fe-b4da-8a5b687e2650 | -2.98729 | -48.91755 | 2026-10-09 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 417ebf62-b86b-33ee-bbef-b5c89f6c549d | -3.35611 | -50.41393 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3ec2c71b-f04e-3677-923f-e155f51e8605 | -3.86407 | -55.83621 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddebce1c-954c-3f1b-8c48-72c29e250b78 | -3.63651 | -60.6298 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa4df29-ee4c-3197-89fe-82875b00a30c | -3.30429 | -53.69734 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca52f0fe-6be2-3096-989c-c035d5cd244c | -2.49963 | -56.11989 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5be014a-9e1f-38ad-af96-0d3875684953 | -3.41255 | -59.57481 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3afa2291-326d-340a-83b5-606a27ed5d8a | -4.46868 | -55.90166 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cae95e6-2a65-37fa-ae19-19dcbff362c3 | -2.49332 | -56.11508 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5aad28f-9e6c-39b4-9851-7a4d5c3fe10b | -3.04604 | -54.15447 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6baf0237-17bc-3ce6-b1fc-641b1d8db8b7 | -3.26799 | -54.01632 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1d532e3-6f4b-349e-81c5-eb2403e65a04 | 1.69067 | -55.61509 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0596c35d-1502-37b1-84ac-cd13e5d6024b | -1.63 | -55.1287 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41791109-2f0b-3c6c-b39d-4998eb6356b2 | -7.21633 | -55.08792 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ecf1da6d-22a2-3853-9759-68803c0ed31b | -2.97777 | -54.07381 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4421e66-aef3-3f46-96af-ede81ea3ef58 | -1.40021 | -57.93028 | 2026-10-09 05:23:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10295fbe-090b-3eac-824e-8516f09e7ca5 | -3.5994 | -61.63993 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e46d60a3-a0e8-334a-b539-ee177afad84a | -2.88969 | -54.16881 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbd16be2-2112-33a2-89d5-923b9d40191e | -4.6176 | -49.21009 | 2026-10-09 05:23:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25bca26e-8b22-386d-8dae-14e110efe376 | -3.58187 | -55.60323 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd04df88-d65b-310f-9459-4f47d0dfa555 | -3.744 | -59.62732 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e009771f-a4ce-3001-b37d-e24aa53fb4ec | -2.46786 | -56.08088 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b14d687a-8d00-36b5-b024-9c1193f37033 | -3.43444 | -59.35155 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5d80a80-cf16-3f1c-84fc-0fff2f99cca9 | -6.95056 | -59.52687 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d41cd4f-697c-3bb5-810e-f5aa843e033b | -3.85572 | -55.9602 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab5595d0-5558-36fb-bdea-3c51911391ad | -3.60203 | -54.66794 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25fd06e8-41a5-318b-8cfb-3879b794b340 | -3.55815 | -59.47156 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7978354-f207-3714-a103-67984d823a8f | -3.08361 | -58.09315 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03c545e1-5469-32bc-8782-e6bdecb70c82 | -3.43177 | -54.54021 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f453882d-ede7-37f9-84ca-aa6b38c8a1d3 | -3.00048 | -54.76929 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 285f477b-ed5f-35c6-b99f-0a6c36963c97 | -3.50658 | -59.34501 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0b861fa-6991-3b13-9697-aee53c203df4 | -3.4835 | -54.73522 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5ca7a64-93b3-307e-bf20-d3e4ec209b6c | -3.39517 | -50.21715 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebdbc152-b1aa-345f-9823-72d17e90acc9 | -4.00003 | -56.24586 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 09f02ccf-4243-346f-893b-99aebcf0e29d | -2.77062 | -57.62289 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cad5650-a46a-303f-bf5f-95f06e61ca8d | -2.47862 | -58.07217 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9480563f-8126-37aa-9965-1ac07a9b2c11 | -3.27611 | -54.06693 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98716cc2-25b3-3faa-bba5-8785e369fa2e | -3.01202 | -54.1202 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7186b98-df25-38dd-a98e-75298cc30c64 | -2.97188 | -54.11174 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdfe4f13-db90-31a5-bcb1-f81fdb1cb6e4 | -8.49237 | -54.62931 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eaf15155-1ec1-355a-9c16-b15a93d9d7aa | -3.73858 | -59.46797 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 664aeda5-09e3-37a4-9ba1-82f1cfef0dac | -3.22295 | -53.96727 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bee1e7f7-4c64-3f8b-b4fa-8290932bd544 | -3.20696 | -53.86438 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 193dbc41-e865-3ede-9bca-ac1749bc48cf | -9.8675 | -50.49348 | 2026-10-09 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c184beb5-df41-3919-a009-76948af308f4 | -3.90835 | -59.59518 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0879194-cc9b-3b8f-8b3d-f75a81064d8e | -3.78283 | -58.59164 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa6de7c2-be17-3e86-b477-8c22beb8a5ab | -3.18015 | -58.83488 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e8afc17-7668-3f74-9322-e16200c1e993 | -3.82872 | -55.972 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cbbfe91-71a6-373b-a064-0eece9a34bac | -9.88471 | -50.48872 | 2026-10-09 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a64a57d-7477-336e-b5f8-bf0278274166 | -1.31683 | -55.43963 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65935654-7460-3fb6-9324-0a0a95e50265 | -3.48655 | -59.38483 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee457fd3-882a-367e-9b29-fbe8a7696b39 | -1.52439 | -54.56427 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README207.md)
