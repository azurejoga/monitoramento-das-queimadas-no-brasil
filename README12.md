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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23a632b4-7a23-3e22-bf9c-acc2b5125e42 | -15.91923 | -43.51494 | 2025-07-01 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d7ffde3-0ea4-3466-82d5-f3fd8e8b4b7f | -14.3812 | -50.32405 | 2025-07-01 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8df2a8b5-40b2-3075-b7a4-d8386f6a8ecc | -13.71457 | -45.61807 | 2025-07-01 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f90a8f34-4bd0-334e-9434-958d9e922a04 | -12.9772 | -54.68777 | 2025-07-01 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ebb6d4e-360d-357e-969d-9c47169f5015 | -15.92472 | -43.51567 | 2025-07-01 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4660539-c316-3fd4-9678-1bfe8643364f | -15.07828 | -48.9427 | 2025-07-01 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 104a0d58-749d-3f93-ae36-e6bc4380eae4 | -12.82577 | -47.36596 | 2025-07-01 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d9373d3-93c5-3718-9ffd-b8fd7aaefbd0 | -15.17748 | -52.29593 | 2025-07-01 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c977eb70-53e5-3fdb-931d-7b93a3fa55f3 | -16.34734 | -43.69634 | 2025-07-01 04:49:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25afd5a9-0d1b-372a-aa61-32527e1bfc65 | -12.10227 | -54.57751 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cde2062-a5d1-3f24-8944-6c560c2e3634 | -12.01247 | -62.83324 | 2025-07-01 04:49:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01818d97-9eeb-3a41-b2fa-40ecc7c00b33 | -18.29502 | -44.68611 | 2025-07-01 04:49:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1648f3d3-109a-326b-a3a6-b732eef1d16b | -12.63216 | -54.21879 | 2025-07-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d0d84b68-6570-38f2-bb44-4d5d1bea5ce6 | -12.97036 | -54.68661 | 2025-07-01 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| af60537e-3221-3e08-b7e7-245160ff3117 | -12.63034 | -54.22992 | 2025-07-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cc97f88-b887-3879-9a7b-045aaa1b2279 | -13.65186 | -46.81202 | 2025-07-01 04:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7430ba82-2ce1-3e6e-a780-e7afcfa47cf8 | -12.10353 | -54.56992 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44dc8733-baea-3b6c-a863-51b4ec6277d0 | -14.20224 | -45.51973 | 2025-07-01 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7704d941-27ee-3c52-9faf-7626a60226b0 | -15.92433 | -43.51935 | 2025-07-01 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c7fbef1-4830-3df5-bda5-912aa32145f4 | -12.6254 | -54.21766 | 2025-07-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48fe47bb-1998-320f-b7fd-911e648730df | -12.82934 | -47.37017 | 2025-07-01 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9225929c-05d2-3547-9396-5908b237c1ea | -11.82882 | -62.76833 | 2025-07-01 04:49:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a52c84a-45a0-33e1-8859-5037218b9f71 | -12.63554 | -54.21936 | 2025-07-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c000ca8c-4c4f-3dab-bf56-9300ce126130 | -14.82344 | -48.31787 | 2025-07-01 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfb978c4-f57f-3979-813b-469a1520b135 | -14.62086 | -46.81488 | 2025-07-01 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cbefc0f-5fcc-300a-8ea9-95ccbd4a178e | -15.56992 | -47.8543 | 2025-07-01 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce21008e-8766-3102-bf42-e19ae778ed8e | -13.72917 | -49.00647 | 2025-07-01 04:49:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ca5c96d5-d2dc-3132-894a-dac695a4a619 | -11.8311 | -62.77371 | 2025-07-01 04:49:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c05cbbea-0787-397d-88f5-be0bd7b7c53c | -12.82527 | -47.3696 | 2025-07-01 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abcbb145-f607-3ee7-bfd6-2b4c08a51e1a | -12.62696 | -54.22935 | 2025-07-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb88703f-3e84-3a2b-9485-efa94493e60e | -16.68444 | -43.88391 | 2025-07-01 04:49:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05a374df-fd1f-3f95-b9a5-ae2c0f0aaf7f | -14.21887 | -45.50119 | 2025-07-01 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ec949ae-76c9-34aa-9f56-d93e82905a80 | -13.7053 | -45.61688 | 2025-07-01 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e38f3e5-10b2-3620-86d7-63435f4938da | -14.21163 | -45.52106 | 2025-07-01 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d86b037-b062-3616-bae4-48e329a8ec82 | -12.09799 | -54.66728 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5648a9ee-5431-3be1-8432-89c83702e740 | -14.13514 | -46.34453 | 2025-07-01 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 255de387-bd0c-3826-8a81-77536c3a9687 | -12.5705 | -48.88536 | 2025-07-01 04:49:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 152a4c3a-2674-32ac-a363-b0df59e7b6c0 | -12.62323 | -54.20969 | 2025-07-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a73fc38d-149a-330c-b425-5cc40664dfbb | -11.74728 | -54.72443 | 2025-07-01 04:49:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaba7ad0-59b2-3cc2-98e9-915dd5223513 | -13.41903 | -47.82301 | 2025-07-01 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bf71284-050d-3e41-9884-b6ea6fd414f9 | -12.62479 | -54.22137 | 2025-07-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3be53d4e-f5c0-32dc-9b47-189e8287b19a | -16.55664 | -49.42485 | 2025-07-01 04:49:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bd66fd0-4847-36a7-af9e-b91e2a850235 | -12.01322 | -62.82936 | 2025-07-01 04:49:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a56a2d2f-8bb7-3c4f-a6d5-a924871cc487 | -17.93815 | -48.91951 | 2025-07-01 04:49:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e223de2-ec4d-3c5d-91dc-b6aa4d259e81 | -12.98125 | -54.68456 | 2025-07-01 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e50b4fd-ba30-33b1-913f-30155bdb2fb1 | -12.99276 | -54.67871 | 2025-07-01 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2a151f3-9aa1-398c-8592-650f545e4b19 | -12.10571 | -54.57808 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 799e99b2-3258-3c77-a208-e205bccb78d3 | -14.44265 | -48.87466 | 2025-07-01 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f38ef69-aee4-3686-b8a9-168c4540d08a | -12.09735 | -54.67113 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8566b834-b59f-348d-9d34-100d43c62afe | -12.10696 | -54.57049 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65188f59-783e-3560-9662-a8871ce46c75 | -12.63614 | -54.21566 | 2025-07-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0d410153-3852-34a3-ab0f-7cbbfbe80fb3 | -12.09455 | -54.66671 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97f4e739-cdce-3bd7-9fbd-343fb00a4b8c | -18.2898 | -44.68525 | 2025-07-01 04:49:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e1fca5f-4d4a-3c53-b795-ebc513563f17 | -14.38063 | -50.32807 | 2025-07-01 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbf943f1-a28d-3b87-bfff-1eb9cbda7255 | -16.56041 | -49.42541 | 2025-07-01 04:49:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de01360c-fc6b-3cb2-92cc-a69ed3f81acf | -12.10633 | -54.57428 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a447172-9bcc-31e0-bdee-e6041066b075 | -14.20756 | -45.5153 | 2025-07-01 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 506c7775-6afe-3505-8792-ef80946a9c0f | -11.83368 | -62.77345 | 2025-07-01 04:49:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 047b4e23-b632-304a-9768-18ecc341e258 | -14.20631 | -45.52546 | 2025-07-01 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae0f7b1c-3f34-3380-8d21-acb0cae9192c | -13.27525 | -45.09158 | 2025-07-01 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c12d510-4a59-33d9-92e6-0b6ccec0b161 | -14.20693 | -45.52039 | 2025-07-01 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5879020-a308-312f-88fe-34a72ecde9d4 | -11.7752 | -54.36433 | 2025-07-01 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2df9b840-acdc-3d84-8e7a-ea2307510fe7 | -13.17693 | -53.56451 | 2025-07-01 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22ea08b1-9e7e-391d-871d-ed93b934347d | -14.40442 | -51.57309 | 2025-07-01 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14012402-d9a9-3022-a389-b2a4a0dfd3ce | -13.71359 | -45.61888 | 2025-07-01 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7dd37ec-4702-30f4-8f9d-84265d7eb276 | -13.41855 | -47.82642 | 2025-07-01 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11498874-4a3e-30b2-9b53-229dc88a9787 | -13.01005 | -53.41592 | 2025-07-01 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd7ccf79-7fc3-3d81-97d2-9c4c13ccd5f4 | -12.09391 | -54.67056 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94cf8ee3-b1b9-3cb8-bcbb-c335533865b7 | -12.62878 | -54.21822 | 2025-07-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ca5ac611-77ad-3065-9df4-c5284d06fd56 | -13.41458 | -47.82576 | 2025-07-01 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 573e0c39-8843-3c9c-80db-76e2bb08ac98 | -12.97378 | -54.68719 | 2025-07-01 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 947f254b-6429-3b59-9031-bea9ed450e8c | -16.56105 | -49.42334 | 2025-07-01 04:49:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 197c5fdd-11fa-3c01-bb0d-46d6f09f33d3 | -12.09947 | -54.57314 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38dc11d5-4abe-3a00-b262-3011d24ef7a8 | -12.97845 | -54.68019 | 2025-07-01 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bcb45b1-3c0c-371f-8214-8e3044c3ad4e | -18.0598 | -44.4944 | 2025-07-01 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0541fb4f-6c5e-393c-8f04-b795c73f2471 | -20.7633 | -46.77053 | 2025-07-01 04:51:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1ed98fd6-dc76-3838-85b2-f644d0679ea3 | -24.11133 | -51.8564 | 2025-07-01 04:51:00 | NOAA-21 | GODOY MOREIRA | PARANÁ | Brasil | 4108551 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2f8fed68-6422-3134-b8f7-ecbfb7678e73 | -21.7501 | -48.11874 | 2025-07-01 04:51:00 | NOAA-21 | AMÉRICO BRASILIENSE | SÃO PAULO | Brasil | 3501707 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0894d8a-64f3-3e4c-94dd-031b553ae5b1 | -21.53608 | -51.77831 | 2025-07-01 04:51:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 65160e1b-7f1f-3228-89ab-191ae04f72f1 | -20.80928 | -44.63258 | 2025-07-01 04:51:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c44e4967-1120-3ea3-99af-373f2c6d1c21 | -21.13189 | -48.59072 | 2025-07-01 04:51:00 | NOAA-21 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1a952252-f143-3395-acc9-66e2f561a254 | -21.19358 | -44.93872 | 2025-07-01 04:51:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f29b74a4-e3c7-366e-be8d-75a37821fc32 | -19.98084 | -47.17955 | 2025-07-01 04:51:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a6f8eb9-5ddb-3351-9c36-6e57b1fe879a | -20.80385 | -44.63193 | 2025-07-01 04:51:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 12dfd8a8-92a7-3eaa-a983-ed7c6e723cf1 | -18.42945 | -54.55917 | 2025-07-01 04:51:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 019c4cad-2891-3694-952b-0a18fc00e820 | -6.2943 | -43.6891 | 2025-07-01 05:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 9a1f85c1-43cf-3d81-ae9e-f7748d9a858e | -6.2945 | -43.6659 | 2025-07-01 05:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 37c39979-f1ea-3465-8812-53b3c65d6299 | -6.2943 | -43.6891 | 2025-07-01 05:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 752bdb82-1893-3bc9-ad1e-5bfe86ff1ea9 | 2.7519 | -60.36674 | 2025-07-01 05:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95fe9f89-127b-3763-b285-4799a51dbbe3 | -2.16943 | -52.45852 | 2025-07-01 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4691c487-f4ee-38b0-8cfe-2d850c949d76 | -6.17591 | -47.27634 | 2025-07-01 05:12:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 590816ca-0b5d-39eb-8acb-4e6ff709ee8d | -2.91125 | -54.48758 | 2025-07-01 05:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fdcc59c-c464-3093-b497-4bdccd6ae088 | -4.54931 | -48.01045 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e790624a-daab-327b-9387-85e456709444 | -6.28925 | -43.68037 | 2025-07-01 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 55439df7-d7f0-3055-8187-cd9f72f88c79 | -8.72352 | -47.9833 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 947c1835-f6a6-38a3-a1a3-833c131d8f36 | -7.16123 | -49.51441 | 2025-07-01 05:12:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0464be56-4f6f-3e48-9fc2-9d6586f0593d | -7.09722 | -49.16745 | 2025-07-01 05:12:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94ac3f92-6e71-3617-a230-d61cd2e407da | -4.31993 | -48.08075 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cbf0852-2a14-390a-889e-5d11cd614a39 | -4.31945 | -48.084 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0436ac20-cfdc-322a-8f44-0e274982a7f3 | -6.28121 | -43.68626 | 2025-07-01 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README13.md)
