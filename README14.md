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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d2896ca-5be0-305d-ba49-21b7294d380f | -20.72658 | -56.65194 | 2025-07-05 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4b9ca399-e4b6-3b49-9589-f2d03b4bc53e | -19.57485 | -54.45197 | 2025-07-05 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2108ebce-44a1-3a6b-89c1-d0e66b6a5bc0 | -18.45867 | -54.70804 | 2025-07-05 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46804ca9-406d-36d4-889b-f91c82b678c0 | -17.76163 | -52.44839 | 2025-07-05 05:14:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08489d5f-471b-3699-b531-b832f0463ca2 | -18.33752 | -52.04581 | 2025-07-05 05:14:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5712dab1-1888-3d6e-9009-c0eec3896e1f | -19.08484 | -56.05463 | 2025-07-05 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| dc67c62e-451f-3e33-b5aa-e4c1c91c5d37 | -20.44212 | -50.73017 | 2025-07-05 05:14:00 | NOAA-21 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ced2ecf2-f06f-3729-bd0e-fbafcefb72dc | -18.51751 | -56.41256 | 2025-07-05 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| d8d8403b-ec31-3577-8d4c-dcb1621ff169 | -19.09022 | -56.0542 | 2025-07-05 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d11a01b4-b324-35a3-a617-e939c6a80304 | -18.33817 | -52.04007 | 2025-07-05 05:14:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bff2d4d4-d735-3765-a036-d097fe893e4b | -20.73035 | -56.65258 | 2025-07-05 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fdd63e0-622c-3781-b009-c7b6973d7543 | -19.08867 | -56.05519 | 2025-07-05 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e028d06d-bf98-3535-8b8b-060e720612f8 | -19.09315 | -56.05078 | 2025-07-05 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8a07a0c0-2373-3d57-a815-84db78ca9eca | -18.66843 | -55.74287 | 2025-07-05 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 068f1dff-e3d9-373f-85ad-0e18a0239c13 | -21.95695 | -57.58831 | 2025-07-05 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94c42b2b-9dbd-3f7e-9927-febf61c5ac1f | -21.60869 | -53.8151 | 2025-07-05 05:16:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b231f29-eef5-3935-be99-64a702e6f8fa | -21.85148 | -56.74553 | 2025-07-05 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 046f4ea1-bddb-3c1b-ab13-d4789f4c08fe | -21.89927 | -56.73713 | 2025-07-05 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d050e50d-9519-3d9a-b07e-573a44aaa759 | -21.89545 | -56.73656 | 2025-07-05 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c6d8b43-9f19-3e3f-88a8-4e24163b94b8 | -21.60896 | -53.81608 | 2025-07-05 05:16:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46308c30-ee38-3eb9-9fbc-225262f01605 | -21.95754 | -57.58385 | 2025-07-05 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0882c12-7615-3daf-9538-7f39a003e47b | -21.89861 | -56.74217 | 2025-07-05 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b12887ea-4448-30f3-b2e2-faf2dae2752a | -7.89183 | -61.47269 | 2025-07-05 05:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38a15294-ab76-3806-bd87-30a1c27883b5 | -9.4902 | -62.02282 | 2025-07-05 05:38:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b4f11b9-09b5-34d5-99ac-524ce8346269 | -9.50956 | -65.58827 | 2025-07-05 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c927c8c7-38dd-38b0-bb5a-48afd9e8c183 | -11.05257 | -56.7384 | 2025-07-05 05:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f96fc45-48e5-3653-ade3-e3d76a4d8cc1 | -11.4355 | -61.42438 | 2025-07-05 05:38:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c7c0ef1-443a-39e9-9688-f624c3a9be46 | -9.79286 | -64.76376 | 2025-07-05 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51942cba-a06b-3ce5-8bb3-be976298da73 | -10.10554 | -58.22412 | 2025-07-05 05:38:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c27299d-1955-3c97-84e4-01cdc861d77c | -9.63228 | -61.46598 | 2025-07-05 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04a5fc91-182d-38b8-83ca-3452acfb7758 | -7.89818 | -55.41967 | 2025-07-05 05:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 194c1d85-3259-3603-8950-9614bb07a9cf | -9.92058 | -59.90816 | 2025-07-05 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 195a64d7-bf7e-33ba-a213-8d74530cb1b1 | -8.98026 | -68.9773 | 2025-07-05 05:38:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2ce9808-3df7-34df-819f-3012d55d6544 | -11.05078 | -56.74311 | 2025-07-05 05:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c29d6c3-bf09-3e01-8846-a32615150845 | -8.97755 | -68.97487 | 2025-07-05 05:38:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e184672d-a5aa-3ed0-9d16-c5d30ba0627e | -10.30218 | -57.13785 | 2025-07-05 05:38:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b84e2128-bcea-38e6-b249-2495626b20fd | -8.38366 | -51.06989 | 2025-07-05 05:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 893036b8-2d14-37dc-8f87-5715c5d52fec | -10.30696 | -57.13846 | 2025-07-05 05:38:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99458e2a-01f0-3131-8d3c-989ae0349a8c | -7.89065 | -63.04317 | 2025-07-05 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab1709d7-9752-32f0-88a7-b7ffe3101f47 | -8.71942 | -64.17264 | 2025-07-05 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df23eb78-ff43-3959-9741-3a09cffe810c | -9.51013 | -65.58469 | 2025-07-05 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44182932-e0e6-3c92-8b98-758269ea1219 | -11.02158 | -56.2627 | 2025-07-05 05:38:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5d7b91d-7dc9-3039-a1e8-a636654499af | -9.63057 | -61.46051 | 2025-07-05 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff50e447-028a-3d68-8562-819077f7f2a9 | -8.37618 | -51.06986 | 2025-07-05 05:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26194f67-2857-3504-bb38-b568a222f4fe | -9.69051 | -65.48896 | 2025-07-05 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ab33562-6454-3eb6-8ff0-bef8369a8306 | -11.48277 | -60.65636 | 2025-07-05 05:38:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37a92d26-4a5c-3199-9e13-52462062b09b | -7.91792 | -61.56007 | 2025-07-05 05:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01dbab5c-bb5e-3502-acf8-8efae855f3a8 | -11.05154 | -56.73749 | 2025-07-05 05:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5391687a-eef4-3d93-b1c8-d0d287bf2825 | -9.63417 | -61.46104 | 2025-07-05 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cc91f8c-1f2c-3039-a4ea-9cbc76960a65 | -7.8901 | -63.04672 | 2025-07-05 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77628fe4-0d79-3e31-bcc8-478343009fa7 | -9.68919 | -64.62876 | 2025-07-05 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0b54478-a686-3c21-95a1-c16f8ef99fe8 | -7.8951 | -63.03659 | 2025-07-05 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45947e73-c999-3f06-838d-fc0f98f25f6d | -9.68994 | -65.49253 | 2025-07-05 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64ef1147-5fb3-33db-b715-aebdaf952f2b | -11.04762 | -56.73766 | 2025-07-05 05:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4698205-15d4-3372-b8be-2a57027c94bd | -9.32512 | -62.67384 | 2025-07-05 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 814bce0e-702d-310b-8a6b-272cb0324e8c | -9.63291 | -61.46184 | 2025-07-05 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60e1386c-f9f9-38c1-bc86-e94d73d00346 | -10.05641 | -59.36248 | 2025-07-05 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5818028e-57ff-3680-8b3d-394a3b91431e | -5.87822 | -50.14867 | 2025-07-05 05:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 661821dc-f919-3b31-aa7c-e0fae25f241f | -7.90336 | -55.42042 | 2025-07-05 05:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a41c73a-3146-3bea-8e5d-f1f404e6e3c6 | -9.85635 | -65.23892 | 2025-07-05 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d26b8bbb-7718-3d74-90ab-ed5236f07ce6 | -8.38306 | -51.07076 | 2025-07-05 05:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c037a79-9206-3364-bc6f-14297614970a | -11.05185 | -56.74402 | 2025-07-05 05:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 041918fd-d602-3aee-8300-cf442aa87951 | -7.89455 | -63.04014 | 2025-07-05 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac858acc-6fa2-3c76-944b-f4b28cb75793 | -10.13293 | -58.21378 | 2025-07-05 05:38:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8033f169-8e10-3524-bca7-2f28f5718668 | -11.02197 | -56.25968 | 2025-07-05 05:38:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54b9dbdd-a80b-3f75-9848-1741e9147360 | -8.37678 | -51.06895 | 2025-07-05 05:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b00f43c7-5537-3fda-9393-9424aa63f6df | -12.58104 | -56.9704 | 2025-07-05 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0998b91-e1d4-39c2-a4ac-8aad4eaadfac | -19.75316 | -54.0013 | 2025-07-05 05:40:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b5acb81-9359-3ca7-a80a-f5bdeedbf9fb | -18.65782 | -55.74352 | 2025-07-05 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1351df1c-a563-318b-98e1-5e35f5228800 | -19.74657 | -54.00088 | 2025-07-05 05:40:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ae3cfde-ea94-361b-a1cf-70171bb930d9 | -12.01865 | -63.78605 | 2025-07-05 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7c68734-4c51-3fe1-b190-e577063adfe7 | -19.57661 | -54.45633 | 2025-07-05 05:40:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f12ec87c-3976-3e51-86f7-529376ded034 | -18.33662 | -52.04436 | 2025-07-05 05:40:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1622e21b-106d-3090-8850-fe8346040dfa | -12.01921 | -63.78242 | 2025-07-05 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8b9618e-c659-3105-8607-49a150d73a6e | -18.66951 | -55.74482 | 2025-07-05 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9a8f5b94-b328-3d6c-8566-da87e63f3a8c | -19.08302 | -56.05506 | 2025-07-05 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 0335984a-be04-385a-9f32-d1277bbb554e | -11.59 | -61.21048 | 2025-07-05 05:40:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f30cf423-4b17-39ee-b892-e9acf9b30625 | -18.66367 | -55.74417 | 2025-07-05 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 40b2cab8-4141-3da2-b9c9-41783b1524d2 | -19.08878 | -56.05571 | 2025-07-05 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 72ecfe71-5fe4-3942-b074-42f65c90f3f5 | -20.72856 | -56.652 | 2025-07-05 05:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57ecd5a2-da5f-36d3-aeff-b525f2129a1b | -20.72254 | -56.65525 | 2025-07-05 05:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 889e420a-b72b-35ce-a0cc-da038cca982d | -21.8963 | -56.73952 | 2025-07-05 05:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2edbd6bf-6652-3dc6-962f-03a7a0ef8c8d | -21.89098 | -56.73479 | 2025-07-05 05:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06acdacf-dd16-3b68-9baf-813af8516d66 | -20.72063 | -56.65293 | 2025-07-05 05:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c41ca7ea-b615-33a6-95ef-769bb67c5450 | -20.72021 | -56.65706 | 2025-07-05 05:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20ab29b9-ad8f-378c-8344-9903e8b2ca62 | -20.72814 | -56.6565 | 2025-07-05 05:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d854d30f-f737-3907-9f82-1675c0eced08 | -21.89669 | -56.73534 | 2025-07-05 05:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08f6936c-2127-3691-8abf-19f48e111cae | -6.87417 | -48.15989 | 2025-07-05 05:44:00 | AQUA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8cbeae76-ff62-38cc-9c1c-ea7dc4a0d9c8 | -9.58189 | -44.60857 | 2025-07-05 05:44:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 25ef41cf-428b-3921-966f-d527d435f4ff | -3.48121 | -48.44028 | 2025-07-05 05:44:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 53a22d62-3ff8-3b8c-8f94-b56f5dd72e9f | -11.87907 | -44.86535 | 2025-07-05 05:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 17530a32-8a6d-3de2-a779-aab1566155a3 | -12.01253 | -47.75646 | 2025-07-05 05:44:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 02303089-5033-3ce6-9277-0a16cdeaa3fa | -6.67662 | -43.15358 | 2025-07-05 05:44:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 798ef4f9-4d29-3940-9b02-70544a1b3df1 | -12.01114 | -47.76558 | 2025-07-05 05:44:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f34a401b-77ed-3b48-8ed2-1de8f314cdd8 | -11.8776 | -44.87547 | 2025-07-05 05:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7531df19-f62b-3bd8-b51f-830887b0ed53 | -9.614 | -49.01573 | 2025-07-05 05:44:00 | AQUA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d4022862-074b-3156-83ee-9443a78dd02f | -5.99054 | -43.73518 | 2025-07-05 05:44:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6c3b74c6-e833-3938-aca1-fe73f21d7b13 | -6.01325 | -44.5252 | 2025-07-05 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cc1da940-8217-38d6-a75d-2e2883bada0a | -11.44704 | -45.10788 | 2025-07-05 05:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0e508887-c9fb-39b4-83ee-da1e74ef55b7 | -6.87254 | -48.17017 | 2025-07-05 05:44:00 | AQUA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README15.md)
