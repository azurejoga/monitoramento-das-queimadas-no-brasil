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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebb2a5c1-8b9b-3549-879a-1468fbf35950 | -11.0937 | -44.0975 | 2026-10-10 00:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 5a13097b-086e-3a04-a62b-6d536d3982aa | -8.537 | -66.9764 | 2026-10-10 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a7f56fab-12d2-39d3-8a9d-d5cca46f81a0 | -3.3128 | -54.0202 | 2026-10-10 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e628edb8-e6d4-31b8-a5fc-ce61a517cc24 | -4.5929 | -55.7168 | 2026-10-10 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 5955e914-1955-3fe2-834f-c65dd113a3d6 | -12.2156 | -57.1087 | 2026-10-10 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7e39efdf-7e27-39db-87fd-cc8ac9158ef6 | -7.0228 | -47.661 | 2026-10-10 00:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 76280061-b837-3fa1-b8a5-5335167a3060 | -9.362 | -64.6573 | 2026-10-10 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 8fc790ad-d017-318b-992e-7cbc2b251439 | -12.2876 | -63.3903 | 2026-10-10 00:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e9dbe41a-4703-3170-b014-b481e71401e9 | -7.1825 | -52.6283 | 2026-10-10 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| b990180c-3a1e-351a-ac27-e6e8cb14ae37 | -7.5162 | -45.3024 | 2026-10-10 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 8db0af1b-90ac-3ac0-932d-de4858ee4061 | -4.3767 | -54.7493 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 22ae3618-ca05-3724-b966-58584e54bb14 | -3.2737 | -54.6826 | 2026-10-10 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a5f51c11-b73f-3f70-80e7-4bf7f28269cd | -3.7495 | -60.5824 | 2026-10-10 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c8272cad-dd62-3c3a-bb0f-85286489e316 | -9.1015 | -54.7 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 288ccc73-1e41-3e60-a05d-a562cc44f52e | -4.6096 | -49.2156 | 2026-10-10 00:10:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 03b1025b-b033-3b63-b896-83f196922ea8 | -11.6562 | -43.6846 | 2026-10-10 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2a876b60-f7dc-31bf-812e-283f6af8fe55 | -3.8391 | -55.7799 | 2026-10-10 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 2c7ce56f-1695-328c-93e2-f9d03e25bc3c | -12.1017 | -57.1383 | 2026-10-10 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ee433cb3-4fff-3bb1-83d5-4dddd31d9182 | -14.453 | -43.9598 | 2026-10-10 00:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 357.1 |
| 1202ec65-f666-386d-b84c-5bbf54d0f5f1 | -7.5159 | -45.3251 | 2026-10-10 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 9585a630-fdf4-3774-bc92-296609d7e0b6 | -7.9086 | -54.7194 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 22dc75f4-d02d-3dc6-bfef-2df5dc4df494 | -7.2009 | -52.6477 | 2026-10-10 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 680d8fe9-5174-32c9-b59f-9a43e5d2a5c3 | -4.4506 | -47.9329 | 2026-10-10 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 53a6482e-2146-3773-834e-eec6b656b19d | -7.9272 | -54.7182 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| e01c8ce6-4974-35e5-b823-28c80e8dda51 | -3.9912 | -59.356 | 2026-10-10 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 2fe8608e-4a96-3c1c-8309-ec735e727e2a | -12.3064 | -63.3893 | 2026-10-10 00:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 7feca757-d3fc-3c81-a136-7151be748732 | -7.4977 | -54.9854 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2d56e76a-2f1c-3efe-8599-8758f6c35a6d | -3.9911 | -59.3752 | 2026-10-10 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 96b189df-f59c-35d3-a724-72b5db770610 | -4.3582 | -54.77 | 2026-10-10 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 47e1878d-a832-3c5f-b331-25238fecd381 | -12.2879 | -63.352 | 2026-10-10 00:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| d7e5f435-33d1-3d5e-ab4f-205feac4006a | -12.2158 | -57.0887 | 2026-10-10 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8ce23e0c-4027-348a-9896-a3610eaf138b | -7.5347 | -45.3233 | 2026-10-10 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 05f4b464-34e8-378a-820e-2110673bc7e4 | -3.1284 | -54.1857 | 2026-10-10 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 4765db5b-cd56-3534-b2b6-2821786a3941 | -4.812 | -56.0849 | 2026-10-10 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 076fdaf5-28ab-37d8-af07-a954872614c4 | -3.1114 | -53.7839 | 2026-10-10 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f59e6673-3600-3b36-aa62-e9a459ba673b | -5.7378 | -45.1307 | 2026-10-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 76a79490-c512-3fbb-9ddc-23f752dc44b4 | -12.2152 | -57.1488 | 2026-10-10 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1a357b39-3eaa-3667-bf6b-8c54266fd074 | -9.6367 | -48.8628 | 2026-10-10 00:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6696a2c9-f323-3ede-baac-37f101862c82 | -13.3666 | -43.8979 | 2026-10-10 00:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 14c503c9-33c8-3394-b196-ae09b1e889f4 | -4.4507 | -47.9112 | 2026-10-10 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 5ad7e759-1552-3691-9fff-a3645a07a7a0 | -5.7565 | -45.1293 | 2026-10-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 3ad9368b-8629-3a54-b3ff-1dd9b46a73c7 | -6.441 | -55.0624 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d6116c7d-a24c-335f-bb13-a8e9727433c5 | -12.0825 | -57.1598 | 2026-10-10 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ebcaac13-8388-3cd2-871b-4ecb5a2a1158 | -5.7059 | -49.05 | 2026-10-10 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| e53d1e60-826a-3aeb-ab7b-825cc788bc9b | -4.421 | -49.7766 | 2026-10-10 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| c391fc89-22ad-3474-82f4-021a407bf468 | -3.5807 | -51.5039 | 2026-10-10 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 01e4a072-0826-3984-a5d1-2fe8b2ca05a3 | -3.2736 | -54.7025 | 2026-10-10 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3a6f35d7-9827-3ce5-9605-a2a07eb03f18 | -3.6907 | -47.815 | 2026-10-10 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 196d301b-8294-394e-988d-2dad50c87404 | -11.0741 | -44.1237 | 2026-10-10 00:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b8c686ec-d970-3a5c-a6eb-6e31bc72a6d9 | -3.549 | -54.7551 | 2026-10-10 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f407d5bc-13f3-3a11-a314-630766dd817b | -3.6048 | -54.5936 | 2026-10-10 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9c16ff85-0316-3a3d-9dd1-04ae06914cea | -3.7494 | -60.6014 | 2026-10-10 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 57586b3f-3843-327a-874c-fad9d7b315f9 | -4.3766 | -54.7693 | 2026-10-10 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 1178680c-6354-387b-9eac-60998f40bd25 | -12.2877 | -63.3711 | 2026-10-10 00:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 86c7bc82-df2b-3ac6-a18c-bddd75606994 | -12.2343 | -57.1271 | 2026-10-10 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5a3dd13a-001c-3028-b013-adf473e2515b | -7.5161 | -55.0044 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6c833e45-2b7d-3b5f-95c7-0d013ffe5819 | -7.4975 | -55.0055 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 39ad8140-8b69-3b6f-8e36-62c9fadf8d8a | -9.2973 | -47.4092 | 2026-10-10 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| e205d3f7-8e90-3d72-9c22-70fa24a37bab | -4.4344 | -47.5421 | 2026-10-10 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 75767870-c679-3090-b459-6168d77a2439 | -3.5676 | -54.6946 | 2026-10-10 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 48578a04-9143-343f-b852-2446bf919cea | -6.633 | -59.9457 | 2026-10-10 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| e7ddc7a9-ca22-31a9-8714-f8004f2234d3 | -3.8749 | -55.9961 | 2026-10-10 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| af597d94-417f-319d-b1de-164aab7b0bfd | -7.535 | -45.3006 | 2026-10-10 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 1056ea72-77b0-3adc-90ef-f9947d6825d9 | -4.3582 | -54.75 | 2026-10-10 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| cae58d64-b33f-3624-9933-e740addccd24 | -6.6145 | -59.9464 | 2026-10-10 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 6804a407-1a2c-3adb-8004-08d9ea1a92d4 | -6.4751 | -55.4999 | 2026-10-10 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| f8ad7c95-6d85-3647-b301-b0c8636f14ab | -7.2011 | -52.6272 | 2026-10-10 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 7b590402-e373-3e29-8d9b-ec5da4ceb9dc | -9.2976 | -47.3871 | 2026-10-10 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 6381bfcc-1766-348d-8c93-08ceaa5c9150 | -9.6364 | -48.8845 | 2026-10-10 00:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| db0b6454-c84a-38b1-a79d-6928cbf1bd96 | -1.2723 | -55.7494 | 2026-10-10 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f095e3b3-185e-3cf4-b128-766fa3547593 | -9.2784 | -47.4112 | 2026-10-10 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 3dc6f25b-2b69-3335-8375-a20b362cf025 | -17.2903 | -40.3318 | 2026-10-10 00:10:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| 861904c2-6875-36fc-848e-68731a2ca856 | -9.3805 | -64.6567 | 2026-10-10 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 0a0fed2a-c621-3e54-a1d0-5d45b8e1ef17 | -3.5864 | -54.5942 | 2026-10-10 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| cb6b8b19-6a2c-3ea7-9a14-40e18c9453f8 | -6.4411 | -55.0424 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| cd69a56e-879b-3319-a700-3135924a5a14 | -6.4567 | -55.4809 | 2026-10-10 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3e13d9cb-c838-35b5-b500-02f8d6e4535c | -3.2204 | -49.4205 | 2026-10-10 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 394baf16-c919-32ac-a125-aaeeb8327a26 | -17.2895 | -40.3576 | 2026-10-10 00:10:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 158.9 |
| f45849d2-afba-36d5-8d5b-554540e59366 | -12.3067 | -63.351 | 2026-10-10 00:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 5d9f2149-35fd-3b3f-8dd4-0f1ca4bc0b43 | -12.1015 | -57.1583 | 2026-10-10 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| ba1e808f-2b3c-3a89-9bf5-15f52ec85c08 | -3.2031 | -53.8621 | 2026-10-10 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4c434e24-1f3e-35f6-9d93-5489ae89e46e | -3.839 | -55.7997 | 2026-10-10 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 15c43e66-39aa-3ae6-bcfb-2d79b14ad8b8 | -3.2203 | -49.4417 | 2026-10-10 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 98c87def-a8d9-3dce-8c18-8bf580372683 | -3.2577 | -54.0217 | 2026-10-10 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 6ef3ba1e-7b96-32a5-8264-9e474e1d674a | -12.2154 | -57.1287 | 2026-10-10 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| a4e7d45c-85a3-395b-85ab-7d8c6a9a18bd | -14.4726 | -43.956 | 2026-10-10 00:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 264.3 |
| ade59b42-e310-377b-98db-951b5e6241aa | -3.1842 | -60.0607 | 2026-10-10 00:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a23d8b4c-ac7a-347c-ba5b-88a6b36d7d39 | -13.386 | -43.8945 | 2026-10-10 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| a4cbf9df-d9b1-3fb5-8e1d-adc37ece0d7a | -3.3139 | -59.4089 | 2026-10-10 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f2aaa808-c834-31e8-8921-0e456b3cb451 | -3.1842 | -60.0416 | 2026-10-10 00:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 852873a4-98fd-33ae-a588-c2bb97c12504 | -5.9587 | -55.3448 | 2026-10-10 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f4b4b468-484e-3ffd-8818-c3fcec1fdc39 | -17.3097 | -40.3523 | 2026-10-10 00:10:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.2 |
| 86c2c49e-9174-31cb-9a8c-03b7bddfee36 | -14.4535 | -43.9359 | 2026-10-10 00:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 235.9 |
| f27dc95f-c0eb-3a31-9243-62ec5b37f65b | -3.9729 | -59.3564 | 2026-10-10 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 341c1fa4-6181-36d2-960a-72991dddf1b8 | -7.5162 | -54.9844 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9ef3ab95-ef38-31db-a79e-184daa4d673f | -3.5491 | -54.7351 | 2026-10-10 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| a5bafd68-8465-3f24-b923-c81cf4db5222 | -3.7311 | -60.6018 | 2026-10-10 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 3e6712a2-ab10-35bf-8a6d-40f61c24b46e | -5.6873 | -49.0511 | 2026-10-10 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 43111863-4565-314b-91f0-4d403e5cd47d | -3.0375 | -53.8865 | 2026-10-10 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1a16f30c-973b-38c3-9b5f-2ee94344b34d | -3.8573 | -55.7992 | 2026-10-10 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |


[Clique aqui para ver as próximas entradas](README10.md)
