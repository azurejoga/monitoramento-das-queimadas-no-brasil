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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29442f57-32a0-3250-86fe-76f9bf5ade0f | -12.39141 | -38.00223 | 2024-10-03 03:36:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2baaeef8-ba93-301f-830c-16c49ae78913 | -12.3896 | -38.00305 | 2024-10-03 03:36:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5dd6c815-6983-3f74-bc71-0fa9c423d536 | -12.34595 | -38.06479 | 2024-10-03 03:36:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 33fec051-b875-38ee-951d-35180ef7efb9 | -12.34164 | -38.06839 | 2024-10-03 03:36:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 40ef1fc2-4c57-3ddb-b21f-aaed79b844e4 | -11.84098 | -43.82862 | 2024-10-03 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27522dbc-0f00-3aec-8592-842068ce14c5 | -11.84036 | -43.83188 | 2024-10-03 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aea87075-f056-302c-bb30-7562438469e3 | -11.83576 | -43.82758 | 2024-10-03 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb4c1b56-2787-31a5-9a03-0dfcf3339e39 | -11.83514 | -43.83083 | 2024-10-03 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 770ced89-f2e7-3d6e-a2a5-b2f1a0aafd17 | -11.56192 | -42.18422 | 2024-10-03 03:36:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c1167fc2-e0e6-3975-aa94-e33e5ec265b9 | -11.56079 | -42.18366 | 2024-10-03 03:36:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a22c9a62-38b3-377c-b47c-23b01e948ab0 | -11.27787 | -43.39756 | 2024-10-03 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22472839-2cb7-3fef-8293-18609d0659b1 | -11.27451 | -43.38716 | 2024-10-03 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bd6abad-8c86-3b89-a36b-3799e190edbe | -11.27333 | -43.39343 | 2024-10-03 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f230d731-5c2d-39f8-9e80-ae7f696fa852 | -11.27274 | -43.39656 | 2024-10-03 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 437c6674-e118-3acd-ba48-72ea8c002917 | -11.27216 | -43.39967 | 2024-10-03 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a8ef2d5-4060-35b0-afef-15f6e0fe0c42 | -11.26587 | -43.40488 | 2024-10-03 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b6624050-aa0e-3c89-a651-b3c205bb4287 | -11.26528 | -43.40801 | 2024-10-03 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8f256c01-6cc4-3d4c-9ac9-ec9a1f51edf7 | -11.21159 | -41.06461 | 2024-10-03 03:36:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 660d286f-ccb5-33fc-9671-703838d504aa | -11.21098 | -41.06659 | 2024-10-03 03:36:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b8576607-c72d-377c-a140-390a8c3c3a42 | -11.16232 | -43.46458 | 2024-10-03 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 346ee777-63ab-3f0b-94af-de456dd50673 | -10.66626 | -44.50084 | 2024-10-03 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1179ff5e-baf3-314c-8fe3-f748ce808aed | -10.6607 | -44.4997 | 2024-10-03 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2a7e106-eb26-308c-aea4-64f855af7fa6 | -10.65999 | -44.50347 | 2024-10-03 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 393ea39d-d41b-35a5-a1e9-7844ec28b4b4 | -10.65514 | -44.49858 | 2024-10-03 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf2ec292-70c2-3d3a-8e7a-90aaa458ed5b | -10.65443 | -44.50235 | 2024-10-03 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7c23af8-defd-3c8a-8c3f-abf69a376c15 | -13.26302 | -48.58981 | 2024-10-03 03:36:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5d3e8ae-5b13-3d4b-bd6a-ad816951c809 | -12.47699 | -47.49634 | 2024-10-03 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f4e9186-a3c1-3751-994d-40f844fca67b | -12.4766 | -47.50133 | 2024-10-03 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c457015b-e9f2-352f-8369-9c835012543c | -12.47579 | -47.50204 | 2024-10-03 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d27ced04-26c0-3501-b793-b6949411cbe1 | -12.47013 | -47.49993 | 2024-10-03 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dd01456-5bde-3832-b934-9af777aa5004 | -12.28297 | -47.65609 | 2024-10-03 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b242c10a-9e83-3443-a93b-2e389f2dd59f | -12.28174 | -47.66206 | 2024-10-03 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0382068b-fd8e-339b-8ea0-3db2ea6c99c1 | -12.19798 | -46.76325 | 2024-10-03 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8e6f0bd3-4d37-307f-9f09-7aa1c721ae1d | -12.19472 | -46.76101 | 2024-10-03 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f0756777-a93e-3351-8646-ada2f14e7d06 | -12.19372 | -46.76604 | 2024-10-03 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2180557e-72f2-3e9d-aa8f-9c517f2f83c0 | -12.19176 | -46.76187 | 2024-10-03 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b4c50ae-7fd6-3914-ac07-b4bb527b0506 | -12.18851 | -46.75957 | 2024-10-03 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70e8e590-ec89-3eda-bb6d-1eab28c27010 | -12.1875 | -46.76465 | 2024-10-03 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8bde4a8c-e9d3-36f9-aca8-6c98384b0f09 | -12.18662 | -46.75528 | 2024-10-03 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2b1cd1cb-357c-36b0-b742-e82cd2f9133f | -12.18555 | -46.76047 | 2024-10-03 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cc1d92b4-d7e8-3ba9-987d-3b12ca397157 | -12.18229 | -46.75819 | 2024-10-03 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed193bc2-b5f4-3536-a8e1-b835fadc36ae | -12.18038 | -46.75402 | 2024-10-03 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b6a0d31-aec7-36f2-8b40-6edab9fffe6a | -11.81673 | -47.59843 | 2024-10-03 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 360884f4-78ab-3a18-9e2a-d7d286e794af | -11.81156 | -47.59025 | 2024-10-03 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 881aacb4-baf7-38e0-82cb-4678624a83ec | -11.6941 | -47.705 | 2024-10-03 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a5690041-0662-38d4-868f-9d402dc7963b | -11.68927 | -47.7108 | 2024-10-03 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24ce6134-ebe8-341d-91f3-d6c8124f540a | -11.68521 | -47.7145 | 2024-10-03 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5b5e1ec-f3bb-38ed-94cd-76d857b395e9 | -11.68246 | -47.71025 | 2024-10-03 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d595849c-740a-330f-92d2-b3f45864a63f | -11.67838 | -47.71402 | 2024-10-03 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d2dc058-a5ff-3cfa-94e9-c6877bac68bc | -11.67557 | -47.71012 | 2024-10-03 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c2e5d09-16e0-32df-8115-2aa6978eea5f | -11.32638 | -46.83482 | 2024-10-03 03:36:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cec72372-436d-39cf-a7b9-e737a1b66a83 | -11.32009 | -46.83319 | 2024-10-03 03:36:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab58666e-c102-325b-b0f8-65841628010d | -10.59787 | -48.09596 | 2024-10-03 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bfabed03-79bf-3c44-aa62-ad79100eb959 | -10.59698 | -48.09531 | 2024-10-03 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 11c8b32b-ba05-3465-a9f9-e2706ff7a53a | -10.47 | -48.19038 | 2024-10-03 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2c4533df-6ffa-359b-afc5-5aed7b12ea03 | -10.46314 | -48.18846 | 2024-10-03 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b14cd30-6a85-3916-94e9-ba11a6854005 | -10.8942 | -63.8971 | 2024-10-03 03:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1d97d8a5-3063-33a5-b8a5-dcca767d8eb5 | -11.2565 | -60.6019 | 2024-10-03 03:36:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c10cef96-83de-31fd-8100-56e631100409 | -11.6931 | -64.9974 | 2024-10-03 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 29fae535-e0a0-37d2-b0d9-d4137d2426d0 | -11.6932 | -64.9785 | 2024-10-03 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 15b7945d-24b1-3b7c-8ebd-34fae4e19e6d | -12.4038 | -63.0009 | 2024-10-03 03:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 186.9 |
| 211f5f76-9b95-398b-a4fc-0849c24d8227 | -12.404 | -62.9817 | 2024-10-03 03:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.5 |
| da8e7efe-7543-3f63-8f82-007642735021 | -12.4227 | -62.9999 | 2024-10-03 03:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 6e486eb2-5f69-3b72-86fb-1e17f35604b9 | -12.6295 | -63.1225 | 2024-10-03 03:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f1782191-fd33-3cfd-86a0-b52a84dba401 | -12.6484 | -63.1214 | 2024-10-03 03:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8a4f2ade-dce4-30cf-97f8-b4ca55d05886 | -12.8802 | -62.5503 | 2024-10-03 03:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 57a6489c-1913-3500-85a2-dc01cc7fcf0f | -12.8996 | -62.4913 | 2024-10-03 03:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 117.9 |
| c961f924-0fc0-34ef-96d1-1db32e93567d | -12.8998 | -62.472 | 2024-10-03 03:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 1f050bea-023f-34e1-8b6b-a08afb9aef22 | -12.8999 | -62.4527 | 2024-10-03 03:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 4bc1dd97-b326-3a2d-9c7c-37428aa0023c | -12.9166 | -62.7214 | 2024-10-03 03:36:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 64af7879-35fd-3f08-b7c2-2a894dc65470 | -12.9167 | -62.7022 | 2024-10-03 03:36:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 82c4acd8-d1e4-3ba3-ae4c-08bd661af384 | -16.3515 | -50.1024 | 2024-10-03 03:36:37 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 487dbf2b-d5c6-39ed-ac91-2dabf8d3ba30 | -16.5582 | -58.2407 | 2024-10-03 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 7bbdfec4-15a2-3a4f-a064-2a4d838af98b | -16.5588 | -58.2001 | 2024-10-03 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.4 |
| 5d8e5a74-3dda-3e4b-8bc8-50b2263e3cd7 | -16.5783 | -58.198 | 2024-10-03 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 651a8764-9881-3e7a-b9de-a34686d46c86 | -16.578 | -58.2183 | 2024-10-03 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| f0d0eadc-7eb2-3491-8e5c-78a279595511 | -16.5585 | -58.2204 | 2024-10-03 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.2 |
| 32e7e804-20ba-3918-bde8-89c0dd522178 | -16.6688 | -57.374 | 2024-10-03 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 6471eba7-ab4b-39e6-bba1-3bdf69f530db | -16.6884 | -57.3718 | 2024-10-03 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 2ce2fbd1-2214-3a2a-8df8-b1e1a2d089e4 | -16.779 | -57.8306 | 2024-10-03 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 06915c46-463f-3c36-aeb8-e869c8b6254b | -16.5973 | -58.2365 | 2024-10-03 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 74c46781-e16e-3efe-a80c-c66f00699d1a | -16.6685 | -57.3945 | 2024-10-03 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| 4b206c6d-8c90-3dbe-a88d-947d6f5639f4 | -16.7985 | -57.8284 | 2024-10-03 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 4289d034-d46d-313b-ab4f-3ebbb9d32ef6 | -16.898 | -57.7153 | 2024-10-03 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| ae756924-0aa3-3e87-90bd-2ecaafb2b627 | -16.8983 | -57.6949 | 2024-10-03 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| c541a2c7-7393-38a6-b641-222ddc6bc6e4 | -16.9176 | -57.7131 | 2024-10-03 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 8d2fcff2-b2e6-32c4-9eda-219a4d220eb9 | -16.9179 | -57.6926 | 2024-10-03 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| b610c2f7-fc51-3580-9407-38d5de1877fe | -19.0344 | -43.1944 | 2024-10-03 03:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| b748d7e5-38cf-3b96-b3ec-41472fce5eda | -16.11065 | -50.44508 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4eaa2ea3-cb5a-312b-9aa0-d1fc08c08acb | -22.83755 | -48.41722 | 2024-10-03 03:38:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2e70ab7-28a5-3828-8cee-319460d403fa | -22.83679 | -48.42049 | 2024-10-03 03:38:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd7ebaa7-7a28-3518-a56b-6b8507498735 | -22.68369 | -50.47657 | 2024-10-03 03:38:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 143602c0-a6e0-330a-aecf-7f010187096c | -22.6823 | -50.48229 | 2024-10-03 03:38:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b23c38bb-41f0-3a68-9a06-8dd23286a253 | -22.66419 | -42.51904 | 2024-10-03 03:38:00 | NOAA-20 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 34c0b854-c8cc-3382-9200-e9018c4798c4 | -22.38705 | -43.39433 | 2024-10-03 03:38:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6d839985-bb39-3fcf-b41a-8f93bf17b507 | -22.38391 | -49.26595 | 2024-10-03 03:38:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 96cf3bd2-96b4-3d7f-a6e8-a603ffd3a0b2 | -22.38323 | -49.26013 | 2024-10-03 03:38:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 36db8983-a0eb-3aa6-9a60-9804d4bc20f0 | -22.38218 | -49.26471 | 2024-10-03 03:38:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6367e230-781d-3938-a3bd-a5197f12911a | -22.38127 | -50.23751 | 2024-10-03 03:38:00 | NOAA-20 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8e480cc9-a5cc-39b8-b55a-fc52eb217d18 | -22.38019 | -43.5196 | 2024-10-03 03:38:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README68.md)
