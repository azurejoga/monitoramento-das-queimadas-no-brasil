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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb25c183-fd0d-3324-87b5-417e73ef060a | -20.36362 | -46.75765 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fb01395b-a96e-3947-a2d4-07b913c56b97 | -14.75604 | -55.38605 | 2025-08-24 04:36:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 542c2663-5ffd-33cc-ada2-8b540290603d | -17.06099 | -47.15579 | 2025-08-24 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19d0ef90-79c4-3fcf-b46c-bd1b18550ce0 | -14.80138 | -47.92249 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b89e924-858e-35c7-a281-350ce28dad05 | -18.04178 | -50.61006 | 2025-08-24 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7be365e-b7bf-3173-943f-c9ecdf9d721f | -14.28516 | -48.0258 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2ff5d47d-7af2-3bcc-bb96-a156e52f12de | -15.04844 | -48.52208 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36ee1a52-6021-3b59-ba9c-ff8cdf41ca08 | -20.37006 | -46.73818 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b097c8ba-e96b-36e9-91a1-0886c428d0b3 | -14.29259 | -60.37623 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d13f7a5e-2e84-37a5-948a-6be7651a2ea6 | -20.37395 | -46.73847 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a67fb029-36ef-3547-911a-50f93441be39 | -14.32728 | -58.59464 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81c9093c-aaaa-3823-b78e-1b936cdeb982 | -20.12031 | -45.36564 | 2025-08-24 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c4191b1e-35b1-371c-96ed-3366411841fa | -14.33291 | -58.59273 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cdeb218-55c9-3e9c-b9b8-ccff4b316273 | -17.064 | -47.16076 | 2025-08-24 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7079945-f137-3449-9cf6-482dbc014bc4 | -20.3733 | -46.74348 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b795b42c-c952-387c-9212-7329d35cfac0 | -16.96205 | -49.7224 | 2025-08-24 04:36:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b162139-dac6-3d93-b1ca-beda4ebfda43 | -15.3365 | -56.23672 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8235939-1d8d-3c5f-a778-2239cbcad097 | -19.73092 | -47.9841 | 2025-08-24 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3917c5a1-0deb-307f-9d91-baf3e53aec2a | -14.82276 | -55.97408 | 2025-08-24 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| da2400cc-2040-3b06-8d38-fcef8f3a6422 | -14.80425 | -47.92681 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a08a4d7f-cb44-3937-958b-2effd36aa838 | -15.09535 | -48.65715 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9995a7b6-1857-3c22-b0ba-63467d98cd65 | -15.12667 | -48.63206 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51b35a52-7f00-37ff-9104-f20bb136bafc | -20.35845 | -46.73687 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2142e35-3668-3728-8010-ea35ed5794d7 | -16.78711 | -51.3582 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1fe8934f-c534-30e5-8ceb-d7cde3386306 | -14.81056 | -47.93158 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3ef4bdc6-f5cc-31d2-8ee7-3bec8345d460 | -18.75504 | -45.09911 | 2025-08-24 04:36:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 96197a0e-22a2-31ec-96c1-f3310455e288 | -17.3904 | -42.62366 | 2025-08-24 04:36:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac324236-dc20-308b-a531-49ec636b400f | -18.42532 | -47.93235 | 2025-08-24 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d34c9db-3c34-3ee7-8790-7fbb281a6eba | -15.2952 | -56.15694 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 4ff3ea41-ce72-3d21-a605-3c8281a85c26 | -13.69052 | -57.75542 | 2025-08-24 04:36:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02c69785-041b-3102-928a-e1dfe1bd5326 | -16.4924 | -52.55851 | 2025-08-24 04:36:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64d974b3-ce3a-31a5-ac8b-2886b5c82b9b | -20.36688 | -46.76274 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0441dde3-d51c-3625-a548-72e7b43a5a28 | -16.40162 | -49.94143 | 2025-08-24 04:36:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86101804-f38d-3b7f-9ab9-e66f97be8a4f | -19.65761 | -48.48977 | 2025-08-24 04:36:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd163b44-c52a-3c83-af5c-3f20ee5cae1d | -14.46725 | -47.71783 | 2025-08-24 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 051069d0-9fe7-3d82-a5c4-53168bdeea54 | -15.65028 | -52.71096 | 2025-08-24 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6c00914-f2a3-3ace-8e0a-02d96a428934 | -15.65376 | -52.71157 | 2025-08-24 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ad67dc7-d33f-3213-ae25-b6c4d97f0e15 | -15.22711 | -48.21548 | 2025-08-24 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0c022b4-b8e3-3b22-87e7-dd29d68761a4 | -16.79768 | -51.35634 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f1803067-b0e3-37d9-b833-c6169356c80b | -18.62531 | -46.38296 | 2025-08-24 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f61ef17d-8aa9-35e9-b611-8ab2d0c5cf9c | -19.86692 | -42.13389 | 2025-08-24 04:36:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a7bafa93-a8b5-30d0-a7a7-d1e5216b1154 | -15.08702 | -48.68986 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b6dcd2a-e8dc-3a8d-83a0-2e73093e324e | -14.34125 | -58.5953 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5c6aa9f-e1cd-3de8-8643-ee69e9711d23 | -14.79227 | -47.93675 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7088157e-6377-33a0-9528-10175265705d | -11.99531 | -61.02 | 2025-08-24 04:36:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 38fe1804-b1bd-37df-adda-03b43dcb40c9 | -16.414 | -49.14476 | 2025-08-24 04:36:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a53e9934-bbc5-329f-a699-4084abca9d41 | -14.66378 | -56.5771 | 2025-08-24 04:36:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c44a9a96-4179-3b7f-b6c8-2b6270f2c248 | -14.46632 | -52.07662 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3b76ea5-5c66-3401-9889-e73182aec7a3 | -15.13396 | -48.62944 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b913eee8-3477-3282-aef0-025be31cd35a | -14.77418 | -45.49462 | 2025-08-24 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21c156dc-aefd-3ec8-9f8c-d1eb0825766f | -15.04617 | -48.51424 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 556f94f2-d01b-357d-a67c-767a6b3a4aa5 | -15.6796 | -53.87407 | 2025-08-24 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3d0a11e-907a-315f-b254-1b0b1c40e05c | -20.74524 | -41.77039 | 2025-08-24 04:36:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a0057e85-0cda-3678-b358-231d5436f4a5 | -15.06867 | -48.52536 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc5a9c7f-43af-378c-b990-0f12acc71939 | -19.56281 | -46.98664 | 2025-08-24 04:36:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 002bc6a9-8cfe-3ac1-8bdf-f38a1c58bfc4 | -16.97087 | -45.68993 | 2025-08-24 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2991f0fe-13a2-365c-af33-a89b198f633c | -14.78336 | -45.38778 | 2025-08-24 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3af665f-8955-3094-9773-f1a07f5e8dee | -14.46522 | -52.04062 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5416f435-99ed-3aef-b12d-2a0740ed1034 | -14.34632 | -58.59627 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d3ddd2d-659f-369f-b36a-87814e85bb4c | -14.80244 | -59.63079 | 2025-08-24 04:36:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df35c05a-9679-3198-b963-04b1464b0ff4 | -16.04932 | -48.12443 | 2025-08-24 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 751ed251-de1b-3ac2-ad1e-7c3707d6b659 | -14.85129 | -47.96417 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 301c0d86-0742-3edc-b31e-d6372e7ec475 | -14.80656 | -47.93495 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1214698-a538-3568-8413-f70393ea20c1 | -17.41792 | -48.10168 | 2025-08-24 04:36:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4f5375d-3965-3557-827f-94c216e26e32 | -14.79513 | -47.94112 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fce7e2e8-8133-31f9-b556-2bd7e724777a | -14.50571 | -53.09371 | 2025-08-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3260ff00-2ca6-36bf-84f1-705f4f99238b | -20.07965 | -46.11388 | 2025-08-24 04:36:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 793ba666-b233-3ae0-9b82-e08c148fee86 | -17.60942 | -44.30354 | 2025-08-24 04:36:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 300d7923-2be0-3ab3-9c5e-0db436b2fb99 | -20.73947 | -41.77408 | 2025-08-24 04:36:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| bfae9ffd-4fb4-3b53-a342-2fccd82b74cb | -16.39291 | -49.64488 | 2025-08-24 04:36:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab22a015-7ee7-3ff9-b2f7-c1f3bbe5b111 | -15.97653 | -48.33445 | 2025-08-24 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c16f621a-c738-3cbb-b730-0384d96f9926 | -14.76144 | -45.37436 | 2025-08-24 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 512b2ba9-403d-3b15-a6d1-58613929e4ad | -14.40223 | -49.7695 | 2025-08-24 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3df8ec61-f0e2-35df-b696-df18638f4afb | -15.0364 | -48.1824 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddef5b91-c574-3ed2-b586-e9310abcd4c1 | -20.35523 | -46.73138 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d65d10a5-ce0f-387c-bd2a-5c77954354ec | -16.41486 | -49.94361 | 2025-08-24 04:36:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 520f547d-7bf4-359e-bce6-693b6ec44670 | -14.50066 | -53.10157 | 2025-08-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0528c6e-a575-3b1a-9227-717369462e57 | -14.32786 | -58.59163 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b3ab04a-51f4-3622-a551-eab65ba80ca0 | -16.30982 | -48.18769 | 2025-08-24 04:36:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8073e9a6-bd16-36c4-b729-807a3f0af7b5 | -14.81112 | -47.92777 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 69b2c487-b9ab-320a-8d49-9efc44f8ab15 | -20.97184 | -42.86798 | 2025-08-24 04:36:00 | NOAA-21 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f66fc44-5511-3985-ae66-f3cf3a3cf452 | -12.58774 | -60.36309 | 2025-08-24 04:36:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a29a6968-8871-3ec2-ab22-545321a5d739 | -14.28963 | -60.37185 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 055c68bd-ace1-3fc4-8002-77174f48ff8a | -14.29847 | -60.37636 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcec2709-c019-3f6e-9c84-2df487eea311 | -15.09254 | -48.65289 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b042e0ce-5481-3df2-be0c-bcc46b38f101 | -14.77264 | -55.91534 | 2025-08-24 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 10317d46-86f7-3f72-aba8-404797834e45 | -12.58762 | -60.35704 | 2025-08-24 04:36:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abc61201-f823-3044-bc4c-39690eda448d | -15.0409 | -48.17546 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16c7045f-f172-37f8-be65-bacac3bb417c | -14.46976 | -52.07722 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37d24961-92ae-34df-9f98-644c53506c5a | -19.25713 | -42.05194 | 2025-08-24 04:36:00 | NOAA-21 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d1746f4-0e0e-3a15-81c3-579ce1c07dc7 | -16.30926 | -48.19146 | 2025-08-24 04:36:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 394c189f-e4e6-30ed-b8d2-4f82d78946fd | -17.60791 | -44.30135 | 2025-08-24 04:36:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5dcd2835-ccb1-3871-8fa8-c0fd5574f734 | -15.11272 | -48.65613 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be2fa7bc-36a0-3b0c-b7eb-377e375bc91d | -15.31718 | -56.15686 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fd305f0-a505-3183-923d-b291e8589cc2 | -15.11553 | -48.66037 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c88223f-30b1-3439-ace2-24d3334eea58 | -16.41542 | -49.94003 | 2025-08-24 04:36:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6beebb9-15e3-3bf6-8879-7524e6943db1 | -15.06853 | -46.48246 | 2025-08-24 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2900d63a-f2fc-3cf9-9df5-58a45f5f44f5 | -18.03848 | -50.6095 | 2025-08-24 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02cb0bce-d6d3-36f8-83dc-329a41e5af10 | -14.81285 | -47.93974 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a1a3f337-b23f-3ff1-a5d9-aacda355d37a | -14.2846 | -48.02951 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README49.md)
