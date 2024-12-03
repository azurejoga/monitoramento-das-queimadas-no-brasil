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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92aa0572-4960-31b1-b840-205134e79d3f | -1.75767 | -52.80862 | 2024-12-03 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 376f9d79-d034-30cb-ba1c-8fe141447302 | -3.26879 | -53.6264 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5c7d7c20-d910-31bf-a333-b4b42c8a3ff3 | -1.24347 | -54.53714 | 2024-12-03 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0c55ab6-6364-38d7-9799-aa3789d0e97c | -2.20788 | -53.78612 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4e5d260-9520-3543-a3aa-bedb28ce7d66 | -3.30063 | -53.66214 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7f231ad0-4185-3887-839b-c1883efe7c89 | -2.32959 | -53.80909 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9cabcc5-47ef-3f8b-a291-b560cade1c14 | -1.06622 | -62.65121 | 2024-12-03 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0982fcb0-0487-3932-b5b0-00f226cd50cb | -1.5188 | -60.32295 | 2024-12-03 05:46:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b51ed678-61f8-3d09-8835-d7945374dce4 | -2.75819 | -55.33665 | 2024-12-03 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05b64f2e-6c60-3fa1-9476-c0d9c427c600 | 1.32678 | -60.72513 | 2024-12-03 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 600b4e8d-1790-3eb9-bbca-fc51942e566b | -2.97492 | -53.87431 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc56504c-f0db-3404-af72-61c211955100 | -3.29977 | -53.66818 | 2024-12-03 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66c3e268-76d0-3a4c-b414-9901fe410935 | -2.33601 | -53.81263 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ed9f6a3-cad3-3244-8b42-ba80389e9c8a | 2.73736 | -60.38939 | 2024-12-03 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2658cf56-b2a3-39d4-8f66-cab20a478698 | -1.51822 | -60.3267 | 2024-12-03 05:46:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34e9b449-37e3-3d37-b726-48f7db9a35e4 | 0.91884 | -59.70116 | 2024-12-03 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f39b1d7c-5996-3db4-a587-f53a1670768f | -2.63371 | -53.35897 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 986abac6-f92d-3764-94e6-85f70278254e | -0.8591 | -52.70572 | 2024-12-03 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a42855f2-344a-32fe-91d0-40cfef848578 | -3.17857 | -54.32954 | 2024-12-03 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a242dad9-b4b0-3af6-ab02-a90640daa737 | -3.08083 | -53.37421 | 2024-12-03 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa14162f-06de-3160-906d-4943b26ca0f3 | -1.50777 | -60.39398 | 2024-12-03 05:46:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7a24c0d-a9d4-3b5e-a4d3-c7e993a7ecaf | -1.75874 | -52.80307 | 2024-12-03 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b562bf49-bf41-31a0-8f1e-6c2964123cee | -2.20869 | -53.78082 | 2024-12-03 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f9e36919-950a-39fd-a766-66a016148231 | -1.07948 | -53.45811 | 2024-12-03 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 22fe2f7f-9c35-3d69-871e-77613aee9188 | -3.18414 | -54.33598 | 2024-12-03 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57d07092-39c9-3dc2-9afa-ce4c9d97c4bd | -9.18489 | -62.38946 | 2024-12-03 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 116ec97f-48c4-395d-a932-7e7f820622dc | -10.05115 | -59.11415 | 2024-12-03 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d22efd9-0ab4-3c79-85bd-5b79ea17de77 | -10.05075 | -59.11719 | 2024-12-03 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ed3b97e-957d-3bfc-aee6-d8b02cb96256 | -9.18947 | -62.38648 | 2024-12-03 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91aae13e-c8bf-30cd-8580-88764b1e585e | -9.51593 | -62.93775 | 2024-12-03 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5724e6a6-c5de-39df-8105-aa4bd461d7fb | -9.19288 | -63.44115 | 2024-12-03 05:48:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aee803c3-f07d-354f-9e8b-3bec9d9fdf6b | -10.05549 | -59.12091 | 2024-12-03 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e7e6b31-2d6e-3f4b-938f-248146c06e7c | -9.03084 | -63.5265 | 2024-12-03 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f8f5473-c269-32bc-b477-b835cddb2237 | -10.05589 | -59.11789 | 2024-12-03 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fc14c47-fbcb-3b8c-ad76-d6ee4060468c | -10.05509 | -59.12395 | 2024-12-03 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42a09ae9-a4b0-3d40-aea7-10adba7124d8 | -9.03016 | -63.53109 | 2024-12-03 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01173dee-fa0f-3dd6-a1a1-0a91ac0fe121 | -9.18895 | -62.39006 | 2024-12-03 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ccc8fc6-5d3c-329e-8dab-87126ca13210 | -12.70684 | -58.22305 | 2024-12-03 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f3ecbc8-8d37-3c0f-8060-6e4f143f3dcc | -9.66106 | -62.44268 | 2024-12-03 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a64c5dfa-a3a1-3b48-9c5b-9a90f4760d91 | -12.70591 | -58.2308 | 2024-12-03 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f59b78fc-8aa0-3f2d-8be6-7441f18b1d20 | -12.70915 | -58.20367 | 2024-12-03 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ae67375-ed73-3636-9099-c57178ab0bae | -12.70116 | -58.22245 | 2024-12-03 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7af2054d-5b56-310e-bb1f-6db22c066b29 | -12.70776 | -58.21533 | 2024-12-03 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38f61388-0a44-3b9e-a53a-47b4cc2042c0 | -10.45972 | -58.68106 | 2024-12-03 05:50:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1aa4a19-2448-395c-80e8-735b09ec5579 | -12.7073 | -58.21918 | 2024-12-03 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 64d9d3d3-57e4-3fde-8b9d-59a0204b7188 | -12.70637 | -58.22694 | 2024-12-03 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 87ba3f31-fbff-3217-9623-cd2b16577d2e | -10.46548 | -58.67849 | 2024-12-03 05:50:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce05b9a8-79e5-3477-b995-f9d206344720 | -10.46016 | -58.67772 | 2024-12-03 05:50:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e82f549-74f5-3629-a265-57bf2bf0df7d | -10.45396 | -58.68366 | 2024-12-03 05:50:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab87b379-b5b5-3f32-b2d4-0163e93ebbfb | -12.70869 | -58.20755 | 2024-12-03 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7abd4d8d-169f-3251-bc60-c049f61639de | -3.34 | -46.02 | 2024-12-03 06:00:00 | MSG-03 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4fdc30f1-be7a-3ef8-adf1-ee39ad60ff73 | 3.11658 | -60.32291 | 2024-12-03 06:07:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccaf7cd0-e74c-3625-a088-f68af788a1bb | 3.12174 | -60.31767 | 2024-12-03 06:07:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc96aea3-33db-33c1-98d5-1907846ebb66 | 3.11585 | -60.31867 | 2024-12-03 06:07:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bb1beca-0cb0-37ca-a88b-b7b20aff0278 | -9.93873 | -68.93645 | 2024-12-03 06:12:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6412f2b7-551a-3742-b3b4-0acc352c0369 | -7.30801 | -72.60417 | 2024-12-03 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7840115f-30e1-3ce9-bff1-d619d9caecd3 | 2.73197 | -60.3815 | 2024-12-03 06:41:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| aa9a9723-3ca5-3934-b8c5-718249d7148d | 3.13083 | -60.29727 | 2024-12-03 06:41:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7e01afe1-0fe0-3676-aa34-2a047a3ec80f | 3.12892 | -60.28461 | 2024-12-03 06:41:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d8d682cd-875c-3308-a32c-b9894c8f5678 | -0.8227 | -47.5826 | 2024-12-03 10:20:00 | GOES-16 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| dd159f78-971d-39c3-85f3-60f9924f0f90 | -0.8227 | -47.5826 | 2024-12-03 10:30:00 | GOES-16 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| c7fdbfa5-bb9f-3421-8d46-a4c6c003310e | -0.8227 | -47.5826 | 2024-12-03 10:40:00 | GOES-16 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 02dd01f7-b672-302d-b3af-af1927bd2da3 | -0.8227 | -47.5826 | 2024-12-03 10:50:00 | GOES-16 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 61ef848a-2af3-3c29-89f4-d5450718d80a | -2.9789 | -45.3242 | 2024-12-03 10:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 3f0fbb56-415b-388b-bee2-f2b71135af91 | -2.9974 | -45.3235 | 2024-12-03 10:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 909d6f87-ceba-3c3d-9152-e6f4dbd24213 | -2.979 | -45.3017 | 2024-12-03 11:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| d616961d-7f28-37c8-8a5a-72a302b2593c | -5.1181 | -43.1964 | 2024-12-03 12:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 2c16bda0-22d5-392a-8906-2ad52bb8414f | -1.33754 | -46.94528 | 2024-12-03 12:36:00 | TERRA_M-T | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 4fd2abf1-2b1e-3a69-b81f-d859c2336ff5 | -0.82108 | -47.58575 | 2024-12-03 12:36:00 | TERRA_M-T | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 8500aefc-7393-3815-a145-250927cf1723 | -0.85164 | -48.72098 | 2024-12-03 12:36:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d964a38b-b52e-38dd-87fa-cde628d808a9 | -1.22893 | -47.74964 | 2024-12-03 12:36:00 | TERRA_M-T | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 607b054d-4e23-35c1-b9da-9ae1bc1b7120 | -6.37629 | -45.67511 | 2024-12-03 12:38:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f3547d63-d098-302f-907f-4f97ea881114 | -7.56886 | -45.72274 | 2024-12-03 12:38:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| ec41fd5b-bc0c-3ece-9326-edb294c39b97 | -2.6266 | -43.77493 | 2024-12-03 12:38:00 | TERRA_M-T | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| f2727210-48b6-3c29-bd36-d04e453f3200 | -4.00018 | -43.25119 | 2024-12-03 12:38:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 285627bc-3902-39ca-a333-d137af392b5c | -2.62793 | -43.76551 | 2024-12-03 12:38:00 | TERRA_M-T | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a49c682e-0be7-3320-bb49-2cc347bf4b8b | -3.46999 | -41.61 | 2024-12-03 12:38:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 51.8 |
| 368ff89c-ec73-3ada-a597-49908565aea5 | -3.81962 | -47.63926 | 2024-12-03 12:38:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 41a26a9f-8213-3eeb-a8ab-545886c7056f | -4.05246 | -47.0011 | 2024-12-03 12:38:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5e2c5e70-be41-3b30-9485-625449d6317f | -4.55988 | -46.62288 | 2024-12-03 12:38:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ece5f5d0-661d-3071-b0d4-c783e054826f | -3.32592 | -46.60629 | 2024-12-03 12:38:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 366b28cb-0fca-364c-ace4-34c0d7cadbef | -3.00448 | -43.84246 | 2024-12-03 12:38:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3181bcbe-96c3-3345-b6c2-edd33cc577ef | -2.9302 | -40.67661 | 2024-12-03 12:38:00 | TERRA_M-T | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 1bed9939-16d1-36f8-82b5-9670e03eaa38 | -3.78038 | -44.74151 | 2024-12-03 12:38:00 | TERRA_M-T | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5ac712e3-0e44-3848-80e8-f2e8b85e0696 | -3.70224 | -47.1225 | 2024-12-03 12:38:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7023db70-50f3-31f2-b060-f7c56738ebc6 | -3.35868 | -41.98032 | 2024-12-03 12:38:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 198.9 |
| afb95862-8a60-3438-941f-02e0932f576e | -9.1711 | -43.1133 | 2024-12-03 12:38:00 | TERRA_M-T | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 262034f6-3017-3bb5-b544-456c2c10c7a8 | -6.20346 | -44.82215 | 2024-12-03 12:38:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 400f369b-29c8-3fbc-b5bd-def7a251328a | -2.29309 | -45.51999 | 2024-12-03 12:38:00 | TERRA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 63535733-5912-32e2-8e7c-587f7669ac71 | -4.05224 | -46.81416 | 2024-12-03 12:38:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7d73087c-6202-3319-863d-acd19f488286 | -3.67253 | -42.37069 | 2024-12-03 12:38:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 9a0f3aaa-4f2d-3a99-bec7-64fc46cbbe4e | -7.37744 | -39.0148 | 2024-12-03 12:38:00 | TERRA_M-T | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 25.5 |
| dd2133ac-d897-3217-96e5-3fe4ae458a4c | -6.20215 | -44.83137 | 2024-12-03 12:38:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 2138b7a5-26cb-3348-940d-8a40936b7567 | -2.93538 | -42.08447 | 2024-12-03 12:38:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dfe84505-1b97-3ebd-95e1-f3f31c80d07e | -3.47173 | -41.59721 | 2024-12-03 12:38:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| b272c314-1cc7-3cf0-b896-3260059f8b70 | -3.16735 | -46.55298 | 2024-12-03 12:38:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 25d0029a-cc38-31f2-87f0-4af85a92846e | -1.58587 | -47.53299 | 2024-12-03 12:38:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5b85beaa-fd24-33d4-b407-4a8ef47123e8 | -3.35699 | -41.99244 | 2024-12-03 12:38:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 258.6 |
| ea548182-dd2d-3ef3-9f56-b9d968e1be13 | -3.82908 | -46.57055 | 2024-12-03 12:38:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 62f6069f-1611-38ba-b2d1-3f34219e6d9d | -8.34454 | -41.71135 | 2024-12-03 12:38:00 | TERRA_M-T | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |


[Clique aqui para ver as próximas entradas](README66.md)
