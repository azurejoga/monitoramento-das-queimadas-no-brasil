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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 181dd675-a670-34d6-9939-9757cbf237b0 | -9.33877 | -68.23508 | 2026-09-10 06:08:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 967f9e4e-9d52-3b69-9044-bbe2b527ab27 | -8.89285 | -61.44697 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfe6e1cc-b2c9-3457-aab7-6201065f609c | -8.88885 | -61.43579 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86614f80-3ce2-3194-a0c0-f16df2ebacae | -9.04663 | -65.41611 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5583794-793d-3144-98db-9bf3fb6ae5b6 | -6.82802 | -58.98972 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01251911-a80c-331e-b80a-437e48a54347 | -8.6779 | -62.45814 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4dbf18d-ab4d-31b4-bb42-3cbbe3a1b87e | -8.68676 | -62.46403 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c73b985e-e988-3ccc-ab4c-405c868a24a1 | -11.41979 | -62.10855 | 2026-09-10 06:08:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d45cf719-ad3b-383d-8b6a-877d096fbc1d | -8.67749 | -62.46109 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15f45870-3909-300d-98ad-39c22d9a0d3f | -6.55586 | -62.88819 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c3784e2-0791-34c1-95cd-fe67afe0364d | -9.0036 | -65.40671 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc162a6f-a559-3d7f-99d8-b83083db635e | -8.90685 | -61.43787 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af0f2f5d-0049-3fe0-83a7-e53749a10791 | -9.16379 | -58.31703 | 2026-09-10 06:08:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1f407e41-954d-3ec8-9c2c-40daee6d4b3c | -7.24346 | -59.51628 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16ccb649-f07d-3256-8d7c-0c39e522c549 | -8.73339 | -69.49326 | 2026-09-10 06:08:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5e8ee0c-25c3-35d9-adb6-4565b2fd9c03 | -6.77713 | -58.90634 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46d37b1b-cfb3-3403-8de6-ab87795fa109 | -9.03782 | -65.41869 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf5e462a-000d-365c-9811-2163ea5b55d6 | -9.00001 | -65.40236 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 48885658-a503-3aed-bb57-3da538bdf1f1 | -6.77845 | -58.89676 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf4c33ed-aad1-34fa-9b9c-0dd9e0d25de8 | -6.8016 | -58.95166 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 23fece3a-54a4-3e5e-bb97-405f138c5a98 | -6.79551 | -58.90207 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ca60b07-264a-30f4-8a30-8a7d1b0cdbb3 | -10.85679 | -60.83107 | 2026-09-10 06:08:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 996e5c31-4a0b-38f3-8fab-7036a99bb12d | -6.78991 | -58.8965 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e51890f0-3b8f-3d85-a8db-7f50f3608042 | -6.79597 | -58.95277 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9131783-4d0a-34ec-91c3-22dd2a345049 | -10.57676 | -68.76859 | 2026-09-10 06:08:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f70b500-9551-39db-b3d0-c349e46afdbd | -9.08269 | -67.86623 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c790468a-aa1d-3e56-98ad-53ffdfb7d1c8 | -8.99423 | -65.41303 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba55b6e7-4bbf-30ae-a48b-f383c5d216ae | -8.90465 | -61.44138 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67505a53-5bac-395c-8a1c-10c636521d47 | -7.92001 | -72.37901 | 2026-09-10 06:08:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcd584b7-3e48-37e7-91f1-9acab2224569 | -7.1408 | -73.11753 | 2026-09-10 06:08:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6c3c063-8f32-30d9-9a42-3e8fe16de4af | -7.28453 | -70.01466 | 2026-09-10 06:08:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1f8aa6f-0519-3fce-ae4b-0d22f3c08610 | -6.79055 | -58.89167 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 628f5957-434a-3daa-ab5a-0e0cb0f6f972 | -8.66587 | -66.56151 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3de4ab40-bc74-355d-bf4a-d04f7fac5161 | -8.99313 | -65.42052 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e241fc0d-54bf-355a-b019-6f17f1d7419c | -6.78399 | -58.90245 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20ad5033-6905-332a-9825-599ae9a8aa86 | -10.8505 | -60.8343 | 2026-09-10 06:08:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02901363-814e-3a70-9546-2b26c02022e2 | -9.15211 | -68.25242 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74f5e8e6-9897-3e2a-9f9d-65e95dcb8125 | -9.30516 | -67.69402 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2795ebc4-da3c-3e4a-b56e-d0fa056d5beb | -9.08209 | -67.87035 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63d77cbc-0293-31e0-aa5b-3a9a559a307d | -7.24525 | -59.51878 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46718a0a-3ad6-3c20-b32e-a814b163808e | -6.78928 | -58.90131 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c2711db6-76f8-34d3-9aea-681f4793350d | -6.80908 | -60.13049 | 2026-09-10 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f28fa51-a6ec-3981-a257-64870f18c5de | -9.43536 | -67.57281 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd182be3-d31e-395b-95d5-812678da6eed | -9.15126 | -58.30941 | 2026-09-10 06:08:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9946b110-e61f-396b-a896-2346adb9dd36 | -8.87989 | -70.83871 | 2026-09-10 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ddead6c-2165-34b3-9734-99d053072bcc | -7.24285 | -59.52073 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de35c8f2-4514-3f86-aea5-92ca73dc9b0b | -8.98954 | -65.41616 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd209839-6cb1-381b-a948-0a70437dc3c7 | -9.13433 | -64.41132 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1bde3a3-cf0b-330c-8268-0bb7b27006a4 | -11.42022 | -62.10512 | 2026-09-10 06:08:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 938acda1-d74b-30d1-931a-dc31334d4e42 | -10.57616 | -68.7725 | 2026-09-10 06:08:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f54de633-3362-3ae6-adac-47846d2e9779 | -10.19443 | -68.76876 | 2026-09-10 06:08:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de4d9c7d-2582-3f72-b2fe-40d55b3ffbab | -6.78597 | -58.88807 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a30c17c8-e0a3-3e22-9611-fec0bad5cc3f | -6.50443 | -58.38579 | 2026-09-10 06:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 163f53fd-2fa1-32b1-939f-bb86a2208fb9 | -8.88838 | -61.43927 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4a78347-8fc1-3c88-a2ee-9c5fef98b812 | -6.95484 | -59.75985 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e52c3bf-cbf4-38b0-9a1f-9aa0304ef86e | -9.22373 | -63.64496 | 2026-09-10 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4314fa44-c77b-3499-8c44-fcbf4951f3e7 | -6.79219 | -58.88885 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11a110f2-fa1c-31c8-b127-aaeb6a094925 | -9.16981 | -68.20634 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be807dda-1a5f-3513-9153-9ad8253fbfc1 | -8.8938 | -61.44 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b4710ee-6a1f-362e-8cae-b5d5115f8932 | -8.68171 | -62.46336 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc2e7276-d2c3-3cf5-a865-a710fa4ca287 | -9.14918 | -68.24791 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d78b36d8-10de-39dc-83b7-9b5234af83c4 | -8.89922 | -61.44071 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0fb0a67-07c8-32d4-bb98-963a447ed28e | -8.82147 | -62.48682 | 2026-09-10 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 998c74fb-e85b-392d-8cac-95b6ae524927 | -9.15716 | -58.31613 | 2026-09-10 06:08:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ecb6e7f-e803-31bd-b1d9-b16aff7da73e | -9.15788 | -58.31039 | 2026-09-10 06:08:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be2ef6e0-607e-3202-85fa-513984004210 | -8.88979 | -61.42881 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5add7665-23ce-33e2-9b3c-2b7ce5e7774c | -8.98539 | -60.58399 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14912e7e-ad4c-3a41-9636-16eccdef3d47 | -6.55363 | -62.90347 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9416f52-d494-3ccd-80d8-af66d36067de | -6.79709 | -58.89919 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83f4aec2-0326-37ca-b0bf-eef67fdae298 | -8.98453 | -65.39244 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e052ff82-69e8-3742-8951-b857a6fe0790 | -6.80218 | -58.95345 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 088f8d3d-b2a2-30e3-a854-44217ebfd7f5 | -6.96015 | -59.76491 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98848053-be75-3d41-a108-ca578c5c5fe3 | -8.89875 | -61.44418 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ef30cec-b660-3ff9-9bcc-20e1757e4463 | -9.96385 | -64.76247 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 681d4ec9-cc9f-345c-907d-9f69142d21fe | -13.28889 | -61.8064 | 2026-09-10 06:10:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8b0cd7a-50db-39ad-9c0c-7302ea1ddf87 | -13.30543 | -61.66685 | 2026-09-10 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef182a3c-e598-371f-b9fe-83122a09624c | -13.29451 | -61.8071 | 2026-09-10 06:10:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33438596-0e5d-39ef-b4f8-aad80055ba0d | -13.31156 | -61.66364 | 2026-09-10 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 775138d3-c6d2-3127-922d-30ab4db4049b | -13.2921 | -61.63328 | 2026-09-10 06:10:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9072017-3f76-31b9-a645-b0f5cff6dba9 | -13.28642 | -61.63258 | 2026-09-10 06:10:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8c6a089-5333-3677-9e5c-5e483c2e5d12 | -13.28688 | -61.62864 | 2026-09-10 06:10:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 603f36c2-300d-3057-8e8a-0a84ed0d4633 | -13.30589 | -61.66293 | 2026-09-10 06:10:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18ed92a1-23e5-374c-b211-d6b74c3ac640 | -12.86 | -44.36 | 2026-09-10 06:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d21e3bd0-066d-317a-9660-c943dce97d03 | -12.83 | -44.35 | 2026-09-10 06:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ebcfe6a-d942-3777-8674-7c1f6d7a9ab8 | -12.8359 | -44.3422 | 2026-09-10 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 8fa2bfb4-920a-3d11-9810-3e59a4ef0283 | -12.8363 | -44.3186 | 2026-09-10 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 61acec64-39a7-3bb4-a9e1-b20aa34e7fc6 | -13.4453 | -43.8366 | 2026-09-10 06:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 6fc34b28-4e67-3fbd-bf82-f91266ab80f8 | -12.8359 | -44.3422 | 2026-09-10 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 3bb963c6-16e5-3bd8-968a-67b9d27dd4a9 | -12.8552 | -44.3389 | 2026-09-10 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 0684f84f-1e7f-389b-9e13-94a9c5ce0ac6 | -12.8557 | -44.3154 | 2026-09-10 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 70975a83-c092-35a3-962e-ac32e05cc1a5 | -12.8363 | -44.3186 | 2026-09-10 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| fb9c78d1-5025-3af5-b650-f9a107c1331d | -12.86 | -44.36 | 2026-09-10 06:30:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17fcf0a2-28b3-34e3-bbae-70757c4d4631 | 0.25496 | -51.45113 | 2026-09-10 06:35:00 | AQUA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 9f4e94b0-2db1-346a-93d7-cf11dba82126 | 0.2523 | -51.45891 | 2026-09-10 06:35:00 | AQUA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 9fdd5628-aab8-31b7-a100-d73a5a8dfba7 | -4.36107 | -47.78179 | 2026-09-10 06:37:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b552c239-c8d6-3c1d-91ec-2b8ec3e7cd2c | -9.70382 | -43.39998 | 2026-09-10 06:37:00 | AQUA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 937adf13-d42f-3b7a-9f7e-824231aac081 | -10.07185 | -45.48161 | 2026-09-10 06:37:00 | AQUA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2a9e184c-1620-3d4d-a1a8-5adc8723faac | -7.48742 | -45.2747 | 2026-09-10 06:37:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8fa4799a-84ab-382f-82ab-5c20fe55648c | -2.93697 | -50.45559 | 2026-09-10 06:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f2c4d860-a08d-3295-9d9e-09921d02b0e2 | -9.67877 | -43.43923 | 2026-09-10 06:37:00 | AQUA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |


[Clique aqui para ver as próximas entradas](README45.md)
