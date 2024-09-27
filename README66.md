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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76c81e95-552c-31c6-a8f7-04ea5e8f2c1b | -23.34785 | -46.33234 | 2024-09-27 03:51:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c367911f-ceab-3e75-a70e-12abed5ea35f | -23.34708 | -46.3363 | 2024-09-27 03:51:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4b3896fa-2224-345a-b14b-80677a2f85a9 | -23.26319 | -46.40226 | 2024-09-27 03:51:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e87e6352-418e-3a0f-84c8-be97d234f388 | -23.22595 | -46.63923 | 2024-09-27 03:51:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 516e3f73-4ee4-3331-9c59-a69e55992dce | -23.22194 | -46.43876 | 2024-09-27 03:51:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1e9e05a5-d5be-3815-a43b-88cd2fecee1d | -23.22182 | -46.63821 | 2024-09-27 03:51:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3023aba0-bb2f-3da3-a625-7a9a3db04e71 | -23.21783 | -46.43793 | 2024-09-27 03:51:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 39a61210-208f-3b33-a882-9c4040c8d8a7 | -23.19746 | -46.45448 | 2024-09-27 03:51:00 | NOAA-20 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b78bb963-fecf-39f2-a232-23917a7fe683 | -23.17882 | -46.33988 | 2024-09-27 03:51:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9d743437-1d27-3255-a6fa-e71e67d9fdaf | -23.16967 | -46.32111 | 2024-09-27 03:51:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4967f567-43e8-38c3-991d-67127a283cfa | -23.16562 | -46.32008 | 2024-09-27 03:51:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 16ad2ac7-c7e7-3f0e-bcc3-cfb64f931381 | -23.09145 | -46.39447 | 2024-09-27 03:51:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4a873f68-c8ad-3f83-a518-16605e395c7e | -22.89906 | -46.43546 | 2024-09-27 03:51:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5c746d40-d560-310d-9956-2d1186fd7479 | -22.95849 | -45.95618 | 2024-09-27 03:51:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4a313ef5-d764-3116-8db9-7aee7c33361f | -22.95789 | -45.95927 | 2024-09-27 03:51:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a4010196-a168-3a42-8519-9d0a7cf7668f | -22.95452 | -45.95512 | 2024-09-27 03:51:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 665cb9b0-3d8b-33a5-a00c-558e77f71861 | -22.95391 | -45.95825 | 2024-09-27 03:51:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 248cd8ea-2081-37ae-806e-8eec4422284e | -22.9533 | -45.96138 | 2024-09-27 03:51:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 61dd1c14-f9db-3d14-9238-132b8e91c399 | -22.75973 | -46.74493 | 2024-09-27 03:51:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| a006f852-fd14-3757-9cd2-604a498574d2 | -22.75551 | -46.74398 | 2024-09-27 03:51:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| afd8afa4-ec1c-3e61-9124-89bd08b42695 | -22.74373 | -46.73685 | 2024-09-27 03:51:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| bedd5a44-03d4-3e23-9ef2-29382f272012 | -22.74285 | -46.74136 | 2024-09-27 03:51:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 34213f83-d017-3c8a-973d-9287cfcd5024 | -22.74031 | -46.73191 | 2024-09-27 03:51:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5b126ff7-c8c9-3f02-9517-b20958bfd00c | -22.70199 | -46.34721 | 2024-09-27 03:51:00 | NOAA-20 | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e0e06a3f-2497-3457-a1bd-d5394359de88 | -22.69793 | -46.34604 | 2024-09-27 03:51:00 | NOAA-20 | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 01678917-bf12-39ff-b7a2-2a7968bbcf0e | -22.22721 | -48.62447 | 2024-09-27 03:51:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| e98322c7-8589-374e-88ba-16ca3d4a7ba4 | -22.22603 | -48.6301 | 2024-09-27 03:51:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| ec79e380-4dbb-3563-bdc9-635a08f2c56d | -22.22355 | -48.61808 | 2024-09-27 03:51:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| cc55e9d7-f281-3dc2-8ec4-bbc64c6b8072 | -22.2224 | -48.62355 | 2024-09-27 03:51:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 65e2af33-fad7-3ae8-ab73-36deeb58681d | -22.22124 | -48.62903 | 2024-09-27 03:51:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 6a4524b3-8fe4-33c6-a88e-37bb3569c97a | -22.21757 | -48.62268 | 2024-09-27 03:51:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 38ceec20-569d-3a99-8e06-e27ddfd04baa | -22.21641 | -48.62819 | 2024-09-27 03:51:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 4015dcce-e47c-3a83-bc62-53d520b0f15e | -2.8611 | -51.6699 | 2024-09-27 03:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 7d4fed54-3b86-3f79-a9e9-f8287fcb730e | -2.8795 | -51.6695 | 2024-09-27 03:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 1fa0cd7e-a97a-387b-9632-23674bda7042 | -3.0107 | -51.0652 | 2024-09-27 03:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| d8c85d89-bfa7-390a-b2db-21b416435ed8 | -3.2136 | -46.7843 | 2024-09-27 03:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| b469c926-bb54-3227-bf70-8d4f66c0ad86 | -3.2321 | -46.7836 | 2024-09-27 03:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7e863bdd-1aa7-3802-99c7-2ad34e220a99 | -5.4157 | -43.4319 | 2024-09-27 03:55:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 837c10f0-46b6-3450-b2eb-394ca38eb7c8 | -5.397 | -43.4332 | 2024-09-27 03:55:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8ff9448e-882d-3231-a7f9-e5d7fd848238 | -7.4605 | -60.4114 | 2024-09-27 03:55:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e2f1b980-2ad9-3266-9f89-dbe44eaed90b | -7.4606 | -60.3923 | 2024-09-27 03:55:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| dabb9b86-3511-3749-9245-c34f19feee4e | -7.5682 | -49.2001 | 2024-09-27 03:55:49 | GOES-16 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 541e2283-ab45-3748-9e0c-1ea8e78f00c0 | -7.5684 | -49.1786 | 2024-09-27 03:55:49 | GOES-16 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c9bedc29-c720-3df6-b112-a3ab2076bf2a | -7.5869 | -49.1986 | 2024-09-27 03:55:49 | GOES-16 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 38debf9b-8b18-33df-998f-23341e09f7f7 | -7.5289 | -61.3825 | 2024-09-27 03:55:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4c6a57e1-a12f-3f6d-8c32-5b49f94c35c3 | -7.5888 | -60.5785 | 2024-09-27 03:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7e2ddad2-9cba-3733-98a8-ae7062281b77 | -7.5887 | -60.5976 | 2024-09-27 03:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0200360d-336e-3b6a-b578-3d0d6f3f021b | -7.77 | -61.2015 | 2024-09-27 03:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b530c87d-85d4-3023-8320-8423fe93d13b | -7.7886 | -61.1817 | 2024-09-27 03:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 760e532d-1f08-3256-8ee0-23f17320e641 | -7.8156 | -54.7252 | 2024-09-27 03:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 0ccfa718-2ece-36f5-932f-af72b6df00df | -7.7701 | -61.1825 | 2024-09-27 03:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5b7bd2d5-0ca0-3d73-bdd3-e3b79d752d87 | -7.9175 | -61.2718 | 2024-09-27 03:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a5e6d441-7543-3756-b7fc-2144fc3ffa1f | -7.9174 | -61.2909 | 2024-09-27 03:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2632133f-ab51-3f11-9e58-198406f53aff | -8.6101 | -63.1226 | 2024-09-27 03:55:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b96b2ac4-ea73-35fd-ad1d-c3f6a2d7d3b6 | -8.8117 | -67.6732 | 2024-09-27 03:55:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 2aa359ec-ca74-3469-9939-a3953ff26df3 | -8.8116 | -67.6917 | 2024-09-27 03:55:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| db75827b-ab13-32c3-a410-4445b7a5d5ef | -9.1032 | -61.3343 | 2024-09-27 03:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 3586b3c4-1459-3e00-afba-5b6959f8c286 | -9.103 | -61.3534 | 2024-09-27 03:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| a0e09170-42c5-306d-a369-dfb7273fe3ac | -9.1029 | -61.3726 | 2024-09-27 03:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 9d992f5f-3e9f-3a97-bff7-3149a9640db6 | -9.1216 | -61.3526 | 2024-09-27 03:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 7066df6f-679b-356c-a6fb-49a014737445 | -9.1215 | -61.3717 | 2024-09-27 03:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 6dc97c17-429c-356f-b681-b43766703bad | -9.602 | -50.1139 | 2024-09-27 03:56:01 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f8a8f9ee-99cf-38b4-9ac3-2ffe8f8ac9d7 | -9.6018 | -50.1352 | 2024-09-27 03:56:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 7048bf5a-389c-38f0-afbb-4364a25ffb59 | -9.5829 | -50.137 | 2024-09-27 03:56:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 1d1e18ad-69a6-3c4e-ab00-f78ae76dcb1f | -9.6275 | -63.6678 | 2024-09-27 03:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 5faad06d-4b8f-326e-95b6-dcf516899e64 | -10.1501 | -49.9956 | 2024-09-27 03:56:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| a2ec96bb-ba69-3c3a-afbb-71331c4e6e73 | -10.1498 | -50.0171 | 2024-09-27 03:56:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e7a1efc9-ba5f-3666-a919-6a4695bd8998 | -10.1312 | -49.9976 | 2024-09-27 03:56:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| cdfc53fa-7251-3347-8958-2ede01c42a87 | -10.1309 | -50.019 | 2024-09-27 03:56:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 7197a353-7e80-3e0d-86f5-8170c25bbcef | -10.3672 | -53.7858 | 2024-09-27 03:56:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| a0b933d4-a0f5-31f1-935a-c8e361820947 | -10.6639 | -45.8838 | 2024-09-27 03:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 9c742f01-e6e7-3d7e-82cf-18eb10d180dd | -10.6643 | -45.861 | 2024-09-27 03:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| f2f7b864-3305-3f33-8b92-d25acf2ea05d | -10.7214 | -51.0657 | 2024-09-27 03:56:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b2aaa59f-f0f0-37af-afa5-09ae5fefcf47 | -10.7211 | -51.0869 | 2024-09-27 03:56:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b8cf12dc-8329-38b0-bdea-69224be3385f | -10.9267 | -54.2488 | 2024-09-27 03:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| b19fc7c1-fae1-3f78-ab3c-d05b80db4341 | -10.9264 | -54.2692 | 2024-09-27 03:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 8a72195d-b9df-38a5-8a4e-c352cec31e26 | -11.2695 | -46.1216 | 2024-09-27 03:56:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ed20bad3-7d18-3ba6-aee7-e6d1f47e76ef | -11.2223 | -54.7735 | 2024-09-27 03:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 0a2103dc-db7a-30ff-a895-e97cf57d7e55 | -11.2034 | -54.7752 | 2024-09-27 03:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 4cebe7d6-c590-388d-8fa1-82d2f7cdbf72 | -12.6829 | -54.6558 | 2024-09-27 03:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 98d3a54d-402a-3bd0-8fe2-79f0b4caff2b | -12.6826 | -54.6763 | 2024-09-27 03:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 21c8d720-2133-34c2-9e82-0545a694e593 | -12.6824 | -54.6968 | 2024-09-27 03:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 85a31238-176b-3e50-9d63-a4bb21a270b9 | -12.6639 | -54.6577 | 2024-09-27 03:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| e5310a52-3518-3539-a551-fb50c8bfcbaa | -12.6636 | -54.6782 | 2024-09-27 03:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ef14815d-2db7-373c-87aa-388dddd499f4 | -16.0793 | -51.9709 | 2024-09-27 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| f8144913-b3a8-32d5-af75-34a010979518 | -16.0989 | -51.968 | 2024-09-27 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 246.7 |
| 6c70eb55-211b-3006-b0db-342bd93f7ba9 | -16.0993 | -51.9465 | 2024-09-27 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 706e2469-8fad-39e6-9d90-5800bb1c8964 | -16.1185 | -51.9651 | 2024-09-27 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 118.5 |
| e6e4ca23-5c3e-3b13-81a5-ec5bc4b13d6a | -16.1189 | -51.9436 | 2024-09-27 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 1298ec25-515f-3653-b0b3-83fa0d4392af | -16.7329 | -55.8237 | 2024-09-27 03:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 995975cf-60f4-3675-b506-3741d4129043 | -16.7325 | -55.8445 | 2024-09-27 03:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 644c9729-0a7b-3e6d-9761-e51edc6488bc | -16.8933 | -58.0213 | 2024-09-27 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 5c0f88b5-c55c-3250-9b51-a7bcd5d76de8 | -16.893 | -58.0417 | 2024-09-27 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 0ae58b4c-a7af-318d-932d-49871230150e | -19.3977 | -42.5753 | 2024-09-27 03:56:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| aaa03363-32fc-3122-9517-a3ae983abe18 | -19.6129 | -42.8411 | 2024-09-27 03:56:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.6 |
| c8148177-267d-3629-94db-3700e4b90f17 | -19.6136 | -42.8159 | 2024-09-27 03:56:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 134.4 |
| 5bb533da-15a3-38cb-9004-bd8b31e85938 | -19.9921 | -47.1621 | 2024-09-27 03:56:57 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 34528780-7441-3059-95f5-39e2dceaa4be | -20.182 | -43.5299 | 2024-09-27 03:56:57 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.4 |
| f17f1710-f1c5-308b-ac80-6707abd75a35 | -20.1828 | -43.5049 | 2024-09-27 03:56:57 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| a135827d-d0a9-3b89-a7f2-6472247855dc | -20.5199 | -41.952 | 2024-09-27 03:56:59 | GOES-16 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |


[Clique aqui para ver as próximas entradas](README67.md)
