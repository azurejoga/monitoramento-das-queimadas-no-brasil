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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff984988-7092-3f9b-86d6-918a8fceec7c | -17.59669 | -46.10049 | 2025-08-24 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40874681-0e71-3139-b335-03e7e76a9459 | -15.1306 | -48.62886 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a390323-2e8f-3025-9558-19e1097c9f4a | -20.08175 | -46.11503 | 2025-08-24 04:36:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 89ee92b7-9b1f-3d93-a30e-e5a66ac10aff | -14.49421 | -53.09599 | 2025-08-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ab8c2d1-4e67-3932-8b4b-b98879b19e2f | -17.40807 | -48.12042 | 2025-08-24 04:36:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ce860b3-e7d8-3ec6-b176-05be435087b8 | -14.2888 | -60.3758 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9178888a-b01f-34cf-a3e1-8de29bef2e9f | -14.46866 | -52.04121 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04278dd3-eaec-3774-ab6c-52345d9f6881 | -14.80439 | -55.90858 | 2025-08-24 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abf8885c-80eb-3089-83fa-6bda5b19ecdf | -14.79762 | -59.62701 | 2025-08-24 04:36:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbbd35e7-82b6-347f-982b-745e7c3e39fe | -14.29176 | -60.38037 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c62ed855-1886-3fbb-9de8-8d3d0c28e18e | -17.66102 | -50.12754 | 2025-08-24 04:36:00 | NOAA-21 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ebe6b26-7bee-3019-a017-1a613620f4ce | -14.47041 | -52.07335 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc30ce00-1240-3537-add7-61929eef4fd9 | -18.39637 | -46.85159 | 2025-08-24 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 608bb861-6913-33e4-8671-38840f8121fc | -16.41735 | -49.1453 | 2025-08-24 04:36:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf716200-a3e2-30cf-8710-2bec27937d58 | -16.79552 | -51.34848 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4b1b5f16-153e-3073-9ff2-1190572563c4 | -16.79435 | -51.35575 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 2f8e4b9e-cabc-33fc-a5a0-f65003a121e4 | -15.12946 | -48.63645 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca38ffb9-dbda-3bc2-ac62-b592ed62fe25 | -15.04562 | -48.51787 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c88dbe3-c615-3255-9695-3aa63b9c2cf7 | -17.60737 | -44.30558 | 2025-08-24 04:36:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd4e11f2-259c-345d-ab8e-ab6f794522ce | -14.79458 | -47.94489 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c889686-c483-337a-8232-cc055d5d7993 | -11.99336 | -61.02466 | 2025-08-24 04:36:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f4fd88f3-b37b-350a-8e1a-80b700876b81 | -15.0398 | -48.18295 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a52c404-a9ec-357c-9694-b00531d069c1 | -14.98039 | -50.18192 | 2025-08-24 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad8dc7cf-81af-3e33-bb8b-08327bcf3d8c | -18.65182 | -48.14311 | 2025-08-24 04:36:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9422c964-7101-344a-b5e2-9d295c43fe1d | -14.80482 | -47.92296 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9fa59fb7-ec61-3e86-8369-57f0b1cbb958 | -14.98426 | -50.17891 | 2025-08-24 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff794bf3-251b-3174-8db0-e6ec78c7ca62 | -17.3942 | -42.62485 | 2025-08-24 04:36:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 72a5280c-bbf2-3e76-9b95-d8001dd33a56 | -14.79278 | -59.6233 | 2025-08-24 04:36:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ca94217-e60d-372c-90ae-c28ede8a3705 | -14.83341 | -49.20052 | 2025-08-24 04:36:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59e5d715-c02c-38d2-b2cf-9fa39702b0ce | -19.62996 | -43.18681 | 2025-08-24 04:36:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 2140940a-5726-365e-9d8a-304b3f966db2 | -20.20165 | -47.02504 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4c599a7-8371-3451-83d0-c14b1ecd82da | -16.0758 | -47.84307 | 2025-08-24 04:36:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3e83c4b-8adb-39e1-9f49-aab826dc3950 | -15.67513 | -53.87796 | 2025-08-24 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e1337510-2b52-33b0-ae96-7ac8a1ab96c0 | -16.51918 | -46.73215 | 2025-08-24 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9bd1b02-f8d2-3017-a9cd-f6f63c828352 | -16.79044 | -51.3588 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c46d75d3-7883-30a6-ac32-2e878341f7c2 | -14.98314 | -50.18602 | 2025-08-24 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d234961-d952-3ccc-b335-f3884acb6dc3 | -20.98219 | -41.84903 | 2025-08-24 04:36:00 | NOAA-21 | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cd0302c9-3fd5-3c28-b1b0-ffe341289347 | -14.85051 | -48.32373 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 141511b3-4a89-36cb-af06-b77c56c0f6cd | -19.6541 | -48.48928 | 2025-08-24 04:36:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa1a6a3a-6956-38a2-8b61-e061b48c7af2 | -17.28395 | -46.76171 | 2025-08-24 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9760477-9f4f-311b-a99b-d6b94c29f20b | -14.27608 | -48.01661 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d77cb71b-ad21-3886-9b15-55b89912f440 | -14.33738 | -58.59685 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7552e206-91d3-333b-9b72-45601d564919 | -19.9941 | -50.26558 | 2025-08-24 04:36:00 | NOAA-21 | INDIAPORÃ | SÃO PAULO | Brasil | 3520707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ce077447-c83b-3870-a69b-0da7dc998fa6 | -18.93057 | -45.7807 | 2025-08-24 04:36:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d65038a-104d-3c11-9339-6102c3ee3f47 | -17.83657 | -50.81288 | 2025-08-24 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a3bff5ed-fd5c-33ce-8a2f-d9084408a9ae | -16.4274 | -49.14686 | 2025-08-24 04:36:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9728c81f-a390-3b45-bad9-0277664a9f33 | -14.94319 | -48.00596 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbb09a44-e732-3d76-806a-1e050f4abd2b | -19.86176 | -42.13327 | 2025-08-24 04:36:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f760cad1-b466-3160-9d06-c9cc1982cbf8 | -14.80882 | -47.91966 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| be7c20ed-20c4-3f5a-b2bd-4dd7de4c9325 | -17.40749 | -48.1244 | 2025-08-24 04:36:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ef90014-5a80-3268-9126-4632ef74e4c0 | -11.99437 | -61.02469 | 2025-08-24 04:36:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a1cfb07c-fc03-347a-8439-640237116e36 | -17.04291 | -47.17955 | 2025-08-24 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c35b9ccb-d468-38a7-8354-dcae38d4a1d8 | -15.92087 | -52.20957 | 2025-08-24 04:36:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a363401-6012-326e-97e6-609dfabc290c | -17.59476 | -46.10361 | 2025-08-24 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05513b39-e473-369e-bb5a-c036b0df3376 | -17.38974 | -42.62912 | 2025-08-24 04:36:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ae5b1eb5-d98d-3810-bbb7-1ed6da15bf23 | -14.85073 | -47.96796 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f8b66de-e6d4-367e-8933-cf9bcabda79c | -14.40278 | -49.76596 | 2025-08-24 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebc074da-59f7-3ccc-8d63-ef246ff95125 | -14.94655 | -48.00632 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73f918cb-8a17-3eb9-a54b-20ce5e17705d | -20.90377 | -42.64543 | 2025-08-24 04:36:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 27c01c35-6f4d-34b2-9a56-6724f73909c6 | -14.79116 | -47.94429 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa9d7fc8-b245-310c-b06f-b598782882f4 | -20.98617 | -41.84941 | 2025-08-24 04:36:00 | NOAA-21 | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0f35f24c-05df-304d-8488-a6a107b5222f | -14.93636 | -48.00483 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeb2f3f6-d9a5-3bcf-828e-e2a1d264eba2 | -20.07893 | -46.11939 | 2025-08-24 04:36:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f38d5c1b-258b-3d77-bee8-75d92f75a6a2 | -17.38335 | -44.27173 | 2025-08-24 04:36:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9ebafb5-1816-364b-af8e-9d1325a94a7c | -15.13282 | -48.63701 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7f4582e-e93a-36c9-8b24-52bba6e3cd1b | -15.05822 | -48.66307 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b219be36-b1c7-3209-bf98-995f522e3945 | -20.73983 | -41.77052 | 2025-08-24 04:36:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f883c5f7-37d7-3cbe-be8f-84087295bb6a | -14.91998 | -44.8566 | 2025-08-24 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 749ce594-3d7d-35e8-8a69-d7838b1d0713 | -19.94351 | -47.48698 | 2025-08-24 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c05b0c31-ab84-3151-9757-dc9a7039f78a | -19.73151 | -47.97978 | 2025-08-24 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2077ffb7-5ec3-3bb5-afe1-6257b35325e4 | -15.64893 | -52.71892 | 2025-08-24 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fd6d3af-6ada-3a6b-82d1-5ada6ea15006 | -14.37851 | -49.10859 | 2025-08-24 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3db73eee-f7ab-3cb7-838e-6a59d0dd110b | -14.9837 | -50.18246 | 2025-08-24 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e70419cb-7bb4-3098-ba7e-9ed86345eb01 | -15.04897 | -48.49552 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cb5c35f-a24f-36ea-b794-0ac2a9a12c8f | -16.07249 | -47.94015 | 2025-08-24 04:36:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7073ebfa-618c-336c-9441-9898e6c0292c | -19.62934 | -43.19231 | 2025-08-24 04:36:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 3bbd40eb-35f6-301c-8736-f3180b59aac0 | -15.53512 | -54.7604 | 2025-08-24 04:36:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87438312-14fd-3687-aafa-ee957615bd9a | -15.32491 | -56.16264 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f9ddb12d-f135-3630-8efb-c74a7b83d2f0 | -17.6051 | -44.30283 | 2025-08-24 04:36:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 36.5 |
| a3b4e78d-1f2f-3afa-a690-c937b9882a18 | -15.23709 | -43.8524 | 2025-08-24 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce6486cc-1ad9-3b65-936d-4318652906ce | -20.361 | -46.74758 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f64787f-1cdf-3f0d-acd5-658e18659501 | -19.63477 | -43.18718 | 2025-08-24 04:36:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 7016eeb9-5dc1-314d-b726-5496a0e4b010 | -16.7877 | -51.35456 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c56ad47-6a75-35c2-889d-48be00f64d7f | -15.54858 | -56.17886 | 2025-08-24 04:36:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca41f4ff-bfb6-31b7-8fd0-2a1309cc21a4 | -15.04035 | -48.17923 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0002a08-7026-39ec-a799-f94ea96e2167 | -14.81224 | -47.92018 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 33152bdb-4c5c-3dcf-bb64-a44c0f6ae6cf | -14.87994 | -47.60474 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 861b43be-0076-3486-948b-60d31f6d99e1 | -14.30059 | -60.37602 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f44542a4-6469-390d-8cb1-c42c54e4a12c | -16.49765 | -46.7519 | 2025-08-24 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5224d9fb-2aa7-3d8c-ab05-10404fb5e4b6 | -15.9209 | -52.20953 | 2025-08-24 04:36:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19131439-e9e8-39cf-b5d9-ce902db5cf1b | -16.79885 | -51.34906 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 528e75ba-5e7b-3e70-9778-16ef52bbe9a9 | -20.08312 | -46.10394 | 2025-08-24 04:36:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe2eb0d2-cb80-370d-b044-a3a1e1a470b6 | -11.99433 | -61.01995 | 2025-08-24 04:36:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 006c095c-03c0-3fb6-8821-08458798bced | -14.80769 | -47.92729 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2a8a2f56-a19b-3269-8f91-47c6cc80b3d8 | -20.35909 | -46.73184 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9c59a1e-f195-30be-bce0-9349d3f5dde3 | -15.3002 | -56.15361 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a2395505-1a36-3a6f-bccd-ee7d78863245 | -17.60845 | -44.2971 | 2025-08-24 04:36:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 2847c595-086c-30dd-b6d6-1f73f6c3bb06 | -19.92653 | -44.21685 | 2025-08-24 04:36:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b66d6c36-cbd5-36aa-a651-5ca3d7eff67d | -20.35715 | -46.74696 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4047dfb7-0cb2-3dd9-9780-7bf9d4c344dd | -14.33559 | -58.59732 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README47.md)
