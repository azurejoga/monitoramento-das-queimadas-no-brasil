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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 178d83bb-e271-36a3-935c-a1e35dda5f4c | -7.5534 | -61.17635 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0da9d5e4-9d3c-3a17-8e9e-2db72e02a451 | -7.60859 | -60.94426 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f698b36-ffc8-3617-a476-1975791be0d5 | -6.65098 | -58.79969 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30fe955d-42e8-34d6-bff8-ed218ac02a65 | -6.75495 | -58.67988 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8394124-e717-3e53-8223-89f0416bb88f | -9.10261 | -60.92188 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b885ebe-5e20-3179-b60f-c1739e2fc261 | -6.76677 | -58.66948 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16409a1f-23f4-3cb9-be10-75961cd6a121 | -6.76527 | -58.66934 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01ceaea3-7040-3e60-af07-58ab736beb89 | -6.94553 | -59.06663 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5221dd9f-2e43-313f-bc91-09de80132cf9 | -7.59981 | -60.9429 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9056d97-6313-3d6b-828d-8431168cd6e1 | -6.75537 | -58.67692 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25c80c1c-0291-333d-951f-0b1330b05aaa | -6.67435 | -58.74028 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 73a69e80-461d-3c95-b728-71f21f3e3b8b | -8.39825 | -62.68899 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9c42a1e-04b4-3353-9c80-387c0136613c | -6.80057 | -59.42444 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a0dfdbd-8ee1-3540-a3e7-cb109158de59 | -7.55714 | -61.18108 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 54608bb9-473c-3867-bb8d-4c09de53dd00 | -8.5312 | -54.82483 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffa11ce0-fadd-3be3-a2d7-3df88505a23f | -7.56832 | -61.19543 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40b5d789-7055-375e-b1df-ebf077c1d93a | -7.05652 | -59.8383 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e346dea-8bd3-3adb-baaa-064d8490e30f | -6.94519 | -59.07846 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f357f548-b1ba-3f83-a6d6-bf91a765191f | -8.70483 | -62.89977 | 2026-08-23 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 82a26bb7-bfef-328a-b69a-507cab446bac | -6.77076 | -58.667 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7af12042-1a66-3215-8754-e58210a2bf96 | -6.93607 | -59.07127 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5dd0bd09-bf30-32c1-a56e-773859aa252f | -6.94207 | -59.3205 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9740f78e-53a4-3bb0-8b43-fa96127e69bb | -6.54755 | -58.51689 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe882ae0-d98b-307f-9447-f2a1837e9a5a | -7.65894 | -63.34166 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a42b87f-84da-32ab-a378-e32e45165569 | -6.8919 | -59.40541 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1121b5c-b73a-3909-bbef-4112679842ba | -8.9197 | -60.71931 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67d6e036-9250-3c7d-bb2c-7500ade95a3a | -6.67222 | -58.79361 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e102a4aa-44c4-3f75-8756-2302ab80a2eb | -9.19402 | -59.45192 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2d7acef2-1aec-3a0d-83fe-70e0f8d9faaf | -6.82465 | -59.6707 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 84108fef-6bb6-3c6c-bd7f-38bc00b88b9c | -9.52409 | -68.63725 | 2026-08-23 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a648d29-da24-3210-a161-bd0038dc9913 | -8.92753 | -60.72984 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6930067-af7d-37e2-916f-62169ab0bd56 | -6.75585 | -58.71013 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac16a529-885e-3d1d-9d14-259ec98a756f | -6.70621 | -58.73318 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4804c922-36e6-328d-a7c2-c0d8c0f6efcd | -7.46238 | -62.31283 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 938ac2f6-2a66-336e-b8a1-a1157b69bcf4 | -7.78905 | -61.43074 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7e68f88-e26c-39d4-aaa7-fa742e158662 | -9.17909 | -59.4497 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1234a29c-1b4c-330e-979e-23a9da40d690 | -6.76479 | -58.7115 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d243408a-1a87-3b42-a75b-bd51f129e47a | -10.56032 | -61.45408 | 2026-08-23 05:50:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2d05880-4b0e-3ce9-bcf6-a8e9f09e1c8f | -9.17071 | -58.33616 | 2026-08-23 05:50:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 725e8025-d725-3f37-8342-84f4d53faf82 | -6.79658 | -59.80053 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3c35a161-4cfb-3d43-a7b3-cc1c7311e48a | -9.51153 | -60.50017 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c985736-7ea5-3574-bfc3-4ff2fac0e82f | -6.80712 | -59.65782 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0808e33d-e88e-3639-ab1f-828847e6ded0 | -6.78618 | -59.42569 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d47fc58f-ca2f-33ff-b735-c79314cfc0db | -7.36365 | -72.66209 | 2026-08-23 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 654a5f55-6b5e-3dfb-9dc0-f4761c330514 | -6.72631 | -58.58762 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fcc56f8-a5c0-3af1-9474-f2799c384ef5 | -7.84503 | -56.57576 | 2026-08-23 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bee1f2e-9dc4-3ef4-ab10-4e803185ca43 | -6.80022 | -59.67246 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8d8bd98-47b7-38bb-83ed-cff146e075ec | -6.80094 | -59.66735 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74d8a299-815f-3565-88d6-4580f726cbeb | -6.77288 | -59.44731 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4dde0698-d392-398a-9e05-eaf617f5f277 | -6.80276 | -59.40847 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ce4958c-af96-3c82-addc-61bcf917d494 | -6.85077 | -58.98381 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13a59d5d-5098-3d52-a6d2-d0ce92473027 | -9.05487 | -68.6783 | 2026-08-23 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39473865-425b-3fe9-b2fc-221e90e3a868 | -7.44048 | -59.77965 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7f9e957c-d551-37f4-ac89-8b8228bef972 | -6.76288 | -58.68718 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d58dfda9-0833-3d11-9981-7c091547b898 | -9.85877 | -60.10175 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7201b660-a740-31ee-bbab-0c0999e2427d | -9.03643 | -60.44621 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c189c055-afa7-3aad-a3d8-e213784e4d37 | -6.79269 | -58.65798 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05a0cbe5-1525-317b-8c63-4e8012b6ef56 | -6.79021 | -59.42827 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d20de4d-797a-392c-8ff7-995897c09fda | -10.65575 | -69.34625 | 2026-08-23 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5b6558b-f2b3-3772-87c6-1374926be5dc | -7.59653 | -61.2309 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c0da455-88ad-3ea9-b4c7-887fef56e05d | -6.66347 | -58.74472 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f47a4d1a-26d8-3b6b-acb7-4fefa383a6ea | -7.62199 | -61.60546 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82ee383d-00e0-38f7-8087-c16f6a7a63c8 | -6.68566 | -58.73284 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be23416d-ec1d-3a4c-9c7a-b8b7078c5dbf | -6.80613 | -59.41977 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4671f40-d48f-340d-8d25-41dc2c1168b6 | -7.61667 | -61.61263 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10070f0b-8ba0-3e99-b502-2f8273062c25 | -9.2036 | -59.56895 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4bf7ba8-bfad-39d3-ba87-b29be58e90fa | -9.85734 | -60.11249 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a54804b0-d0b2-3012-99d4-0ee18338bbfa | -7.78591 | -61.42706 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2eeed16b-3698-3a0d-baf2-8a88fa56b2d4 | -6.76296 | -58.65977 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acf1e55b-f56d-3aff-a123-69c201f190b0 | -6.82392 | -59.67588 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7b16a7a8-f730-3e92-9ed9-e3285e8984a1 | -6.80221 | -59.58904 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1f66f4a6-59ad-311f-abd9-40666dc54acf | -9.43026 | -68.0676 | 2026-08-23 05:50:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2c7e356-b784-30f3-80fe-2a2750d9b08f | -7.78961 | -61.4267 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d10d17f-5fde-31f1-9ed2-9cf91ca92d90 | -8.53712 | -54.83165 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5eac349b-c5b6-31a8-bc4f-a3de1de6a06a | -7.97646 | -63.6544 | 2026-08-23 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cc2b6294-4dfd-3016-b1fa-25ea603bdef1 | -6.77795 | -59.65878 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cb85467-2e9e-302c-8abb-e09932ffc009 | -6.69031 | -58.73652 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 124d388c-1bc9-3aa4-91c9-4dbfd0069525 | -6.67354 | -58.74627 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 52728b2f-b096-3302-89ca-52ba263e39b9 | -8.40616 | -62.69019 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ddf6e4b-29cf-30be-9cc9-73db4212cc1f | -6.79691 | -59.66157 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdb94033-000e-3c24-b1b8-98f3a3987c47 | -9.11753 | -61.59436 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fad3842-55cc-3c84-961d-5fdf086414c2 | -9.21295 | -60.90338 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3dd937a-6a94-35e8-b6fd-c5e13f44c77d | -9.18981 | -59.44546 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a32e8f42-3554-3105-901d-44e7b50a27af | -6.94059 | -59.06584 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f2a5108-6422-3638-8dfa-f0514d9de02b | -7.49358 | -55.3332 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aecc958d-deaa-3acf-87f6-5d23d4913aa4 | -6.68404 | -58.74469 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 7472c771-d558-3e6a-9e8c-1dc5ca07303d | -8.89237 | -60.5424 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bc0bc75-ac95-3750-813d-6e6d461e85fd | -6.84921 | -58.98789 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ecd8071-0c41-33bd-82d0-48a0f5c7f188 | -9.11324 | -61.59368 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c2fa5cc-d0ed-3b90-a01d-92aff84780a0 | -6.87743 | -59.40315 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 514ed9f7-b624-33a6-8d4d-9ecb75ef292a | -6.69534 | -58.73734 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4693f940-4aa1-3765-ac35-ca59b26d0ed7 | -6.9372 | -59.31984 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac1f1d7a-54a3-3101-8218-7a90e05764d7 | -9.10839 | -61.59708 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a65d9b00-ed24-38d8-a72e-c3b0d5f03d89 | -8.94957 | -60.57021 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2121726d-ed5a-3cc2-9659-18030e94cf80 | -9.18406 | -59.45045 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4de5d82b-a929-3c27-9755-28dfe1c4548f | -9.11268 | -61.59775 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8be55f72-acac-3a0c-b923-28fd5f56904b | -6.70788 | -58.72113 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1703334a-48c4-353a-9ed8-8258656b8f40 | -9.17607 | -58.33699 | 2026-08-23 05:50:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f4c1247-81cc-36d9-b564-ce71bb59c8c7 | -9.15467 | -59.48116 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 007e0968-4d52-37d5-8485-d01bacf082f4 | -6.86447 | -59.03186 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README62.md)
