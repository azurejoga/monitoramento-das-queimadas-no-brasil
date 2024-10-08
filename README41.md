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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f53b5009-d3bd-3a44-93ea-9ec97d8d9853 | -20.42558 | -47.67271 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb7d8803-1aaf-31ce-b055-84443572c5d5 | -20.42542 | -47.66466 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dce1c299-70c4-332d-becd-55b57d9a7cb6 | -20.42487 | -47.67601 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d460d1e3-3428-3fbc-89c8-ce1bf6ac1234 | -20.42478 | -47.65152 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0eeddb5-b8f8-3f07-8dfa-e1d2d4c388a7 | -20.42475 | -47.66791 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8cd7601d-58e5-38eb-9d77-359b1066276f | -20.42456 | -47.64306 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da0ab6e0-a0a3-3f31-be0a-af929f869b0d | -20.42416 | -47.6793 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b56ed2f-2d0a-3327-af58-fe850fc2e529 | -20.42407 | -47.67117 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de98e754-b8f5-3056-9cd9-3f3bd3e82ee8 | -20.42402 | -47.65503 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e07a102-be03-3dac-9c2b-c5a7eebf1393 | -20.42384 | -47.6465 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5467546-0032-35c5-bc3a-b5b6c838501e | -20.42345 | -47.68256 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19a2eb06-7eec-3739-b414-94bec8a27760 | -20.42339 | -47.67443 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fff41bc1-157b-315e-a924-d96d5f49c365 | -20.42327 | -47.65851 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d465cb7d-c842-3ed4-8f0f-ece086ab1495 | -20.42272 | -47.67768 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6ba02b0-abdc-37a2-bdda-a33cf3255802 | -20.42253 | -47.66193 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cd33582-733e-3c1d-9f43-7fbc35d7487d | -20.42239 | -47.65348 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d69140b8-8446-3a0a-8767-49e47e0bdeef | -20.42204 | -47.68093 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0bac62c-3f5a-3d17-875c-8ab48b4a87f0 | -20.42184 | -47.66516 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1b51d6fa-52cc-35c1-827b-51a387ae1495 | -20.42182 | -47.64037 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1785da9f-a6f5-3c02-83fa-1e82e6d98e36 | -20.42167 | -47.65694 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ab9c87a-a2cc-336d-8951-13d7cfa48e31 | -20.42136 | -47.68419 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78b7fc01-b121-3b40-ae10-a6404872cff8 | -20.42115 | -47.66834 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9f054642-5314-367c-b704-a81de4ebfedd | -20.42107 | -47.64384 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6d46718-6d15-3053-b90a-ba988357ddcb | -20.42097 | -47.66029 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| abec22e0-05f6-3508-b4f0-aa84845ce0bf | -20.42047 | -47.67148 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d99960dd-29ba-34dd-bec1-be0ebff8300e | -20.42033 | -47.64725 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 384b4c39-cbc2-3a07-8b9e-95f498d45681 | -20.4203 | -47.66355 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9b0fac29-db13-33e9-9957-ef97fd707a62 | -20.41979 | -47.67464 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ccdd8f4-9e04-3e23-9ed8-fa3639df30eb | -20.41964 | -47.66669 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 32967670-325b-3640-892f-94cc38adf24b | -20.41961 | -47.65059 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f202902-fad7-353e-90dc-3daceeaff986 | -20.41939 | -47.64216 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88bd7a4a-ddf6-333e-8b3a-eee6509ee861 | -20.41899 | -47.6698 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b59d3ec-aa69-3585-b9da-34dad355554d | -20.41891 | -47.65388 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a958865-71aa-34f0-8b8a-1dda190eb2c1 | -20.41869 | -47.64553 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b27436b-97eb-37b1-a66b-4bf2782457b0 | -20.41834 | -47.67293 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbc29323-2bfd-342c-9b54-a0dbbab02cde | -20.418 | -47.64883 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 620facf0-68fe-3dd8-ac9d-224a1b5b17f6 | -20.41732 | -47.65209 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40a95002-1798-3daf-a94c-463e6b9f84ac | -20.41549 | -47.66968 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93f73dca-b995-3978-b798-b8adb1ab16ce | -20.41527 | -47.64588 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f0982ab-9658-3474-bedd-54b24f6a249e | -20.41458 | -47.64907 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 048c636f-d089-34e3-9718-e3690a3df1ac | -20.02472 | -46.71447 | 2024-10-08 03:45:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f531ec3-8317-3f42-b9b6-672a471ba927 | -20.02348 | -46.72049 | 2024-10-08 03:45:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1eb5e63-a16f-3694-aaec-9b1f48078318 | -20.36866 | -48.84867 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 380.9 |
| 64554d73-416e-3a96-8b21-40545153a3a3 | -20.36781 | -48.8568 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 5d1d3ebb-dc47-39e4-947c-8f3e66a14d89 | -20.36596 | -48.86073 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 233.5 |
| a6653eb2-fd0b-33f6-a1aa-97aff70433c0 | -20.35603 | -48.85769 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 2ab2ce65-1749-39e3-9d9d-f9f7273702eb | -20.35514 | -48.86177 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 53bc8285-0e04-38d4-b0dc-36cf6ff04459 | -20.35427 | -48.86578 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a326920-f85e-394c-b2be-3736f8bac4b6 | -20.35255 | -48.87367 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3343a3f1-3bef-30f6-a3f5-224bf54568c0 | -20.35232 | -48.84814 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 173232a9-cea3-3423-809f-74a0c44da851 | -20.35171 | -48.87756 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7408d49-bf9e-366c-901a-896e5a07496f | -20.34879 | -48.86435 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d725abf-98a7-3eb9-bb51-35c6d6c13157 | -20.34597 | -48.8507 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fa2c8cd-bce4-3b7d-a051-c4e930fa9a95 | -20.34419 | -48.85884 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71fa4b95-aeeb-3e66-b7d7-eb5b21f5317d | -20.3433 | -48.86292 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b1beb93-ac58-31f8-b923-5f24c29ad7c6 | -20.3413 | -48.84555 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88bad444-1394-3526-914d-b5f1b9365603 | -19.54464 | -49.49629 | 2024-10-08 03:45:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8607cf69-80d9-3af2-af59-7976926fd021 | -19.55041 | -49.49786 | 2024-10-08 03:45:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d192ba56-3bba-3ffb-8086-d31343a07b79 | -20.3632 | -48.85135 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 1cd06a41-e689-383a-b4c4-283f049572ba | -20.36233 | -48.85533 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 7f9c8c28-3b5d-3e54-acf0-07cd19ffa905 | -20.36147 | -48.85932 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d89334ef-e247-3362-93fe-326e130038b2 | -20.36061 | -48.8633 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.3 |
| a87bef99-b5ed-3b6b-9b84-632fe9adc3b9 | -20.35862 | -48.84579 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 201.4 |
| e99a54b9-1420-389a-a5a1-5c1b42b9a256 | -20.35317 | -48.84421 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 201.4 |
| c15b64c0-e3be-3155-beba-dfcc5686bbf5 | -20.35057 | -48.85615 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 0f4eeec5-0965-38d3-a686-9e15004d790c | -20.34967 | -48.86029 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6227f202-49b0-3f46-ae4c-eb815b03e7e7 | -20.34683 | -48.84673 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2a307d7-f9f7-3d9d-8f92-2b09ec7b8cc9 | -20.39057 | -48.85864 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 393e4238-f186-3008-be60-2fa757480bb4 | -20.39051 | -48.85461 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 324d903a-8a48-3db9-b480-cedd307123dd | -20.38965 | -48.8585 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d34ecd9d-23ed-3210-8a87-49b7bb600715 | -20.38877 | -48.86241 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 98fb28c8-775a-3b90-ba6f-aaf68ed40c25 | -20.38759 | -48.84559 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 64d82266-d7ed-31ce-8cb1-45a2479b57ba | -20.38677 | -48.84942 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 115.3 |
| f0a11a59-8b72-3857-b5b8-93b5ab02eb9c | -20.38595 | -48.85323 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 58711eb6-83fc-37cb-994e-1eb5c08b1afe | -20.3859 | -48.84929 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 91.7 |
| de94f5bb-7ce2-3578-8a9a-2a6ea145ee34 | -20.38511 | -48.85712 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 857cea1e-f625-3749-88cb-a0502637c73f | -20.38506 | -48.85308 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 09306168-a77b-3d83-8286-5486a38c21a8 | -20.38425 | -48.86107 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.1 |
| c676d0dc-c17a-3d04-b968-c52cb69c21ee | -20.38419 | -48.85698 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ac95c40c-8bce-329c-9045-7b01f3b16276 | -20.3833 | -48.86094 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 598f885a-2e25-33ae-8e8e-eb96775c59ca | -20.38215 | -48.84402 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 17ea69aa-20ce-38e5-be2e-4285f0be3793 | -20.38132 | -48.84783 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 5dfd6a8c-ded4-36aa-a392-f2d079461d94 | -20.38131 | -48.84392 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 6dac99fe-5224-30f9-9965-0db551a6280f | -20.3805 | -48.85163 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 217.0 |
| a5528f5f-49fc-3338-81da-1d431d0cea11 | -20.38046 | -48.84771 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c306ae92-653c-3fe0-988a-bc3269bf410c | -20.37966 | -48.85553 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 217.0 |
| f90e5fb8-fe4d-3370-af24-7a918d9bffdf | -20.37961 | -48.85152 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 693d2cd9-68b2-328b-8261-a4a74cd871c3 | -20.37879 | -48.85957 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 319.0 |
| f188d33a-9bc1-3613-80de-b3b6c0cd93a5 | -20.37874 | -48.85543 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4450df31-cb7c-3855-a4b6-61aa2846c8ef | -20.37783 | -48.85948 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 9d8db637-d98b-37d1-8df2-ef6c276fd738 | -20.37588 | -48.84628 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 139.7 |
| ef031c81-76a6-3e38-bbc4-4768332d9fef | -20.37503 | -48.85018 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 217.0 |
| db18f7fe-666d-3678-88c4-277569c31c70 | -20.37501 | -48.84619 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 1f391603-0f36-39c8-b3ca-a5a54ed27e52 | -20.39948 | -48.84033 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 24ecfd8f-68c1-3d64-ad7c-4e894f5a91d0 | -20.3986 | -48.8443 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 35fa6081-6b90-3387-8cb6-2d137ea4a555 | -20.398 | -48.87304 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30becdd8-015b-3a2b-8cfd-ae52a0c38cea | -20.39772 | -48.84822 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 1af65cda-b4f2-38d5-b737-136d06a9abc6 | -20.39715 | -48.87691 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f225c268-8e66-3caa-90af-66d71070ed50 | -20.39686 | -48.85211 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8a5c0675-61f1-3a04-9cc4-c6a6b5fb66d5 | -20.39629 | -48.88076 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README42.md)
