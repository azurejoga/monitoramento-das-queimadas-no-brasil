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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dce5414-64e0-3514-896e-202e28cd10db | -6.4355 | -44.5764 | 2025-08-27 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 167.6 |
| daed60b3-31dc-3dad-98aa-6e88dd231afe | -13.3843 | -46.879 | 2025-08-27 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f23c1be3-f7b6-3978-a138-554cc114291f | -8.948 | -65.9429 | 2025-08-27 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 99e2a9ae-b670-3e09-97d9-5d5fb6aaeeee | -10.7019 | -47.1165 | 2025-08-27 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 8095c18f-b355-3fa4-8449-21a280d3010f | -8.4593 | -43.6879 | 2025-08-27 13:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 659a16ba-0c3a-343b-8d74-1280e23b3957 | -8.8841 | -60.7699 | 2025-08-27 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 595.7 |
| 9b0fd378-4c62-3de1-a449-13d66c161d65 | -13.4036 | -46.876 | 2025-08-27 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 938be585-9b14-3981-85a4-57f0f9364472 | -12.7259 | -48.1846 | 2025-08-27 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| e4c6241f-615a-334c-8dc3-e60b88f64213 | -8.9295 | -65.9435 | 2025-08-27 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 60878edb-9f29-32aa-ad4e-0b537c898a18 | -13.6291 | -48.2097 | 2025-08-27 13:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 129.3 |
| aaf8143d-9a9c-3433-bb1d-358d287c7464 | -6.8413 | -58.9552 | 2025-08-27 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5aa7f6cc-95d9-387c-a4ba-bda608a5a883 | -12.8036 | -48.1294 | 2025-08-27 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| d701b9df-db8b-3212-a16b-7b00804f5832 | -9.4062 | -60.5326 | 2025-08-27 13:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 2508c2e9-a28d-3df7-a41a-5159279485fd | -6.8772 | -43.6152 | 2025-08-27 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 8c8734c8-e553-38e8-9942-2f4b9a45ba7d | -12.9266 | -44.6314 | 2025-08-27 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 8a50bfc3-bdc1-3aeb-9062-5899dc670773 | -6.1783 | -44.0457 | 2025-08-27 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 8bb6312b-450f-38d4-aa22-4d65f985c758 | -8.8842 | -60.7507 | 2025-08-27 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 341.8 |
| 8d168584-c33b-3f39-aab3-504e0442ab4c | -11.3146 | -43.5008 | 2025-08-27 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 3aaa5dec-29f3-3cac-bbe8-03a07ff25f0a | -13.6097 | -48.2126 | 2025-08-27 13:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 9b33b5f4-eb80-30f7-80f2-93fdda8058f3 | -8.2707 | -45.1377 | 2025-08-27 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 849b787e-9ab3-3926-aca4-426f5b56e2c4 | -6.8875 | -44.4004 | 2025-08-27 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a0354813-8688-32a3-b954-83e74ab8c3e6 | -9.418 | -48.2756 | 2025-08-27 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 29e2ad09-b3b8-3b8a-a258-c09c347f5932 | -13.0674 | -46.3153 | 2025-08-27 13:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 2f1c3f06-a4fc-33d4-abd9-2548c28f9c36 | -8.459 | -43.7113 | 2025-08-27 13:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a0166af3-156d-3afd-8af5-7297ae9e356e | -13.4032 | -46.8987 | 2025-08-27 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f82a8ee1-5646-31dd-8b37-b52f368d8557 | -8.4593 | -43.6879 | 2025-08-27 13:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 243.5 |
| f36acac6-7118-30a9-b48e-f80620eacdd0 | -6.8774 | -43.5919 | 2025-08-27 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 282.9 |
| b5269a8f-ec71-35c3-be99-a35098f1ea1d | -12.9266 | -44.6314 | 2025-08-27 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 30bc6fe1-33cb-3527-aac2-6fd73d6d1ea2 | -8.8839 | -60.7891 | 2025-08-27 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7b671a84-9096-31e4-8fd0-9d6296723038 | -12.7447 | -48.2041 | 2025-08-27 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 0ba60454-df14-38e3-99ec-cfc0bc253e46 | -13.5193 | -46.8805 | 2025-08-27 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| c9cdeead-0fcd-380e-a366-20e3d1208360 | -13.6102 | -48.1903 | 2025-08-27 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f54e4a91-a7f9-3f54-ab2b-69874e32ddda | -9.4064 | -60.5133 | 2025-08-27 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 1557f4d8-44c5-332a-a5a8-791a75ff8c1b | -12.5764 | -44.8047 | 2025-08-27 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| aea9fb7e-7f93-39a3-8e17-23b4d5af562f | -13.6097 | -48.2126 | 2025-08-27 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 281.1 |
| 9a13ae8b-6ebd-3963-b627-bec8e815653b | -11.1583 | -44.7859 | 2025-08-27 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| ee9a0ca0-45ce-3ee3-9d0f-af05afd878c2 | -12.7259 | -48.1846 | 2025-08-27 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 97c2fc8d-f607-32b9-b148-b7aabcf4e42e | -6.8413 | -58.9552 | 2025-08-27 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| dfc7d675-9940-39d2-8c21-8e868db7f03d | -8.9026 | -60.769 | 2025-08-27 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 092f72c3-c1f7-3947-8528-41f1fad31e65 | -13.3843 | -46.879 | 2025-08-27 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f924748e-7409-36d8-a2d7-02efbc7860fb | -7.1103 | -44.6329 | 2025-08-27 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 400a61d2-2805-3db0-8ae8-77ba849c5999 | -9.6574 | -64.9845 | 2025-08-27 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f9c93d85-08fd-3ea2-bb4f-d072c9627b48 | -8.8855 | -47.1861 | 2025-08-27 13:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| beb6df1f-99bd-351d-91a6-c371edbe74dd | -6.8772 | -43.6152 | 2025-08-27 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 197.5 |
| d79bbecb-f13b-3c7d-8898-001b1e1bb16c | -9.4062 | -60.5326 | 2025-08-27 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| c3277557-6c12-39ea-8d41-fc13febec882 | -12.784 | -48.1543 | 2025-08-27 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f6441c71-d480-3a87-89fe-1d5472f184a0 | -6.4355 | -44.5764 | 2025-08-27 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| aa623375-0dfb-348b-9324-f34f235fb3ac | -10.0977 | -62.9085 | 2025-08-27 13:30:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 81.7 |
| dc89d87d-e0a4-35fa-bc57-95fe697fe818 | -8.4596 | -43.6645 | 2025-08-27 13:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 159.5 |
| ce346f58-0301-3b99-98d5-99600b852dde | -6.1783 | -44.0457 | 2025-08-27 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4b7df38f-c1e5-3354-8a35-28aa88d13c45 | -10.4879 | -51.5953 | 2025-08-27 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 515beb81-0f14-37d6-a03c-5ff9bb0d7999 | -8.8842 | -60.7507 | 2025-08-27 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 207.4 |
| 66ee67af-c972-3c0f-9611-f2666590f128 | -12.7843 | -48.1321 | 2025-08-27 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3c377868-b27f-3588-816e-e8b292700aae | -11.5694 | -47.6081 | 2025-08-27 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 48907d27-018b-36ce-932a-4cba9f64bcc4 | -13.4036 | -46.876 | 2025-08-27 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| aaf6f5f9-9df1-34c1-8e6c-d16cc6224c41 | -12.8036 | -48.1294 | 2025-08-27 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 6f7d545e-200c-31b0-a8bc-d9ec8e93889c | -13.3838 | -46.9017 | 2025-08-27 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d77562d4-70e4-321a-b57f-550ccad523d6 | -6.4357 | -44.5535 | 2025-08-27 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 96e604c4-3af5-3e9f-b0cd-a7fe5d0939e3 | -7.4414 | -42.0501 | 2025-08-27 13:30:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 118.7 |
| 8042dc9a-05a4-3ed0-af21-4a2e840bb958 | -12.7067 | -48.1873 | 2025-08-27 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| eff3a66c-8556-3800-a98c-5cb2d8515e17 | -13.6291 | -48.2097 | 2025-08-27 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 189.0 |
| bddca8dd-6bfa-35c8-a26f-9643aac6f2c3 | -7.6414 | -42.6718 | 2025-08-27 13:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 198.2 |
| 4b4da0fa-115f-33a2-91ca-922ccf4aa532 | -10.6825 | -47.1412 | 2025-08-27 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 66a06fe1-45c6-3b0a-bdc0-e4953e5f0433 | -13.404 | -46.8533 | 2025-08-27 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 19698b89-17a2-3143-b5fa-0737eb3573b3 | -7.6411 | -42.6955 | 2025-08-27 13:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 245.5 |
| 16f84bd0-3178-30a5-ac79-c9c596c87472 | -12.7263 | -48.1624 | 2025-08-27 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 538e41e6-ec65-3c3a-9646-8687e5baa2f6 | -7.7741 | -51.0512 | 2025-08-27 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a72254fa-b4b0-3d8a-b974-e77fe8dd7d5e | -9.1009 | -49.5621 | 2025-08-27 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| d6380db9-54b7-3039-8858-d0c41d225d38 | -10.7015 | -47.1388 | 2025-08-27 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| f51e840c-a6c1-3b4c-b8df-2a1b26786ccc | -5.663 | -45.136 | 2025-08-27 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 2d6438d6-65ff-3865-af76-2bc440b57cef | -9.9249 | -54.7192 | 2025-08-27 13:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| abb321ed-ee2f-3c1a-a9b7-b9331a848a5a | -8.8841 | -60.7699 | 2025-08-27 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 342.0 |
| d363bfec-e106-3e86-a51c-8c80ebedaf77 | -8.4593 | -43.6879 | 2025-08-27 13:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 9fe5568c-e839-3046-b925-b987ada08ef0 | -13.3834 | -46.9244 | 2025-08-27 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5b379ca9-1378-3aca-8dc8-b3e990860388 | -11.3338 | -43.4979 | 2025-08-27 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 2c8ae497-4efb-3802-8869-f01d6146f347 | -11.9208 | -47.1375 | 2025-08-27 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| d034973b-846c-3744-b0df-e526120c81da | -6.4355 | -44.5764 | 2025-08-27 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 009389f0-7ceb-307d-b123-1dcf0b6ff726 | -12.784 | -48.1543 | 2025-08-27 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| c158c77a-35d7-3d90-a068-f661b48aa31e | -11.3146 | -43.5008 | 2025-08-27 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 222.0 |
| fdd27ad9-b1c8-369a-98d0-62803254b509 | -12.7643 | -48.1792 | 2025-08-27 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 88f33e40-e510-3cf5-8ffc-f28abfe0a676 | -9.1004 | -49.605 | 2025-08-27 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9960dc67-ef68-34c1-85ed-24349ee04b7c | -13.404 | -46.8533 | 2025-08-27 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 000e1454-cf2a-3605-9c8e-e2b4b08d5456 | -12.7263 | -48.1624 | 2025-08-27 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 87a1bcc4-5848-3a69-a914-5f7603cddea3 | -13.0674 | -46.3153 | 2025-08-27 13:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 136.6 |
| ba808933-a547-3b28-98ff-e662e6dcbd2b | -13.6291 | -48.2097 | 2025-08-27 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 75d4f967-971c-390f-af3f-ca99ac9d50e4 | -6.8875 | -44.4004 | 2025-08-27 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 6f3815be-5621-3626-976d-f476b09aa6a7 | -7.6414 | -42.6718 | 2025-08-27 13:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 216.1 |
| f129d19c-3a5f-3dc9-b7a7-9500642ecf4d | -6.4357 | -44.5535 | 2025-08-27 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| d925d4cb-a344-3c25-aa75-20f407c6fdb2 | -8.4596 | -43.6645 | 2025-08-27 13:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 315aca0d-1b82-33aa-a3c6-4d5209f651f0 | -10.6628 | -47.1881 | 2025-08-27 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c5c08b51-be9d-3e54-9a0e-327d6bc8f2e1 | -9.0816 | -49.6068 | 2025-08-27 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| e0b45656-9e4f-3caa-909b-7c56df31bb33 | -8.8841 | -60.7699 | 2025-08-27 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 380.6 |
| 1c7fdcdb-3158-391f-931e-6a0e1afcd24e | -12.7259 | -48.1846 | 2025-08-27 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3983d31b-ffb2-3acb-9e37-cb5e07bdab89 | -6.1783 | -44.0457 | 2025-08-27 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 4b108f97-4c1e-3170-9829-9280fe60cd2e | -13.4999 | -46.8836 | 2025-08-27 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 6d0ac058-0ec8-38d8-8bda-a494394a305c | -7.4414 | -42.0501 | 2025-08-27 13:40:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| 6742cfc7-a044-312f-a49f-2eaac5593f1f | -9.9249 | -54.7192 | 2025-08-27 13:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d5d80f06-216e-322c-8b2b-a3e7c0a91220 | -10.7015 | -47.1388 | 2025-08-27 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 09b98b97-acc0-3e02-8dc7-1a804fe2ca31 | -10.7019 | -47.1165 | 2025-08-27 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 38804960-1be8-343f-9d36-a80a85bee329 | -12.8036 | -48.1294 | 2025-08-27 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |


[Clique aqui para ver as próximas entradas](README95.md)
