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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 865f8f42-64c2-336b-b2d8-0dc490510dee | -8.96476 | -65.94931 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cd66f095-5c7b-3622-a9e8-bf725ca0028c | -8.93141 | -65.9314 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8424a70e-bb64-371a-a9b8-0b7e97d78a65 | -9.64885 | -64.995 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47ef2c35-67e7-3481-8194-7b40dd95708e | -8.89893 | -62.46913 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 339ef7ed-7b4c-36d0-9748-f9ab1c9327d0 | -9.39457 | -62.49372 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51952f80-654b-35de-9021-4c34072702a6 | -8.50371 | -69.80271 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b908489-ee00-392b-8f27-20a17708179e | -8.95034 | -65.95602 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| a10a0f49-4d4a-3580-84e2-54afc55fdf81 | -8.10735 | -71.24269 | 2025-08-27 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fe54297-a229-33f1-bb88-cd43cad3ffcb | -8.11068 | -71.24321 | 2025-08-27 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72ee9602-0cf7-345a-94ff-73390ae532cf | -9.41134 | -60.50755 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c9e388a-6c05-36d6-9187-90617e20bdcf | -10.09967 | -62.89663 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d4bd7bc-b499-3f12-8ed8-b9645c26db69 | -7.47626 | -61.34167 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c165534-083b-3beb-91ce-a40d8ccc25e8 | -8.1079 | -61.48262 | 2025-08-27 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f7a84db-36d9-340e-8045-f81c0d2ee6af | -14.77066 | -59.72875 | 2025-08-27 06:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e43660ce-0926-3fd3-9395-2583f87bcfa3 | -8.90032 | -60.76504 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76c57f6f-a28f-3b5f-98d7-65f8634f63f2 | -9.1349 | -65.28245 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bddb78d0-ffd0-388e-aafa-fb990c6d6f85 | -9.40016 | -62.49454 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7054686-ea91-3805-8d5a-abb1ec0233b7 | -8.95294 | -63.36836 | 2025-08-27 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d23e6f53-9c4f-379b-8f62-06e398cf1a4e | -9.64497 | -59.63267 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e26fabfa-ae4c-3c63-943b-0333eec522eb | -8.90468 | -60.76744 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 070597c3-c00b-3286-95a5-0959a1dcd3ba | -8.89906 | -60.7747 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb55ab25-03ce-3856-87e0-ddaf1cc27a03 | -9.79769 | -64.25085 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c324084a-1353-3421-a342-afec47fc4234 | -8.92701 | -65.93074 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d8af194b-7490-3c1f-996b-d53eda2924eb | -8.96447 | -65.95245 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1b05f39b-b3b5-3b32-98eb-becb1ca796de | -9.80017 | -64.27029 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc0a4b86-37f0-33c0-baa9-f02e9d3da9d5 | -8.10238 | -71.25272 | 2025-08-27 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 915f4a6c-6a78-347c-ba3a-6e2567aaeccf | -8.99871 | -65.4198 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0808c0f-033c-362c-96e9-b3e649de0305 | -9.16496 | -59.55254 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6c51b0c1-59fc-3ab3-a19c-c8278e936d02 | -7.3883 | -64.36216 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 210d2e06-9f23-3503-8551-588fa5f3b5cc | -8.94656 | -65.95112 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b6e728b3-4359-39f6-97f3-e4ec6ca13cf0 | -9.66868 | -67.51125 | 2025-08-27 06:08:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 545397fe-7ad9-3a18-8653-e70d30d00d23 | -9.67418 | -67.50141 | 2025-08-27 06:08:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6efd1e57-4719-3523-8ad3-156281fbb842 | -9.16157 | -59.5533 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 690a9152-9530-32b3-94df-e69c44af9a3b | -9.40625 | -62.49158 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c338a3e-cf83-3d2e-8781-6d85182aa9e1 | -8.84565 | -62.44309 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ec6dae5-14e4-360f-bce3-838ee7339cee | -9.39609 | -60.52647 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| abef5afb-d0a2-3bda-927d-59dfc3cbbe58 | -10.1038 | -62.90787 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e850ac33-ec43-3576-9a96-7ca52cb5c829 | -8.97368 | -67.48096 | 2025-08-27 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25489144-cee1-3f38-86fd-3ebe939d8a52 | -8.91882 | -65.9252 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4358a97d-efd0-33bf-9b1f-d2317bbbfbfd | -8.93777 | -65.9498 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9f6721cf-7980-3d72-9174-9ae8f6b3a8d5 | -6.8412 | -58.9746 | 2025-08-27 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b4055e04-a597-32de-8406-ae623950ba7a | -10.079 | -62.9094 | 2025-08-27 06:10:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 326174e4-58c6-393d-9b85-a051f013f018 | -12.8036 | -48.1294 | 2025-08-27 06:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5d5e4725-c25e-3cda-95c8-c6f4057b9bd9 | -9.4064 | -60.5133 | 2025-08-27 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 006ed7d8-007f-391e-8a8c-68a28a3d05ea | -12.7847 | -48.1099 | 2025-08-27 06:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 9e55122f-985a-3bc3-8368-41be89cc0d85 | -9.4062 | -60.5326 | 2025-08-27 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| bf8d5bf0-c9ca-3083-9520-ca3e137b9b51 | -10.0977 | -62.9085 | 2025-08-27 06:10:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| a8c7e987-885d-3459-a423-c860dd013ea3 | -12.7843 | -48.1321 | 2025-08-27 06:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 409b83db-54e2-39fb-8afa-bbe19b0e87dd | -9.4062 | -60.5326 | 2025-08-27 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1cbf7be5-5004-3553-a517-a0b778a4f96d | -10.079 | -62.9094 | 2025-08-27 06:20:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| cc49f348-e96b-3869-ba3f-54323783e037 | -14.4109 | -51.9269 | 2025-08-27 06:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 4c7b727b-610b-3490-8462-04821032d4f7 | -12.7843 | -48.1321 | 2025-08-27 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 6943c6ff-0001-31a9-a80c-f4bb6dadf22e | -9.4064 | -60.5133 | 2025-08-27 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 915dbd17-c795-3b7c-aa84-9e8cfc26700f | -12.7847 | -48.1099 | 2025-08-27 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c0429e2c-2838-3073-938e-b15d5fcf5c84 | -10.0977 | -62.9085 | 2025-08-27 06:20:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b183d630-dcde-3b37-a8bf-34a0c5bc1e2e | -13.423 | -46.873 | 2025-08-27 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| fb458afa-1e33-3dc5-a9cb-d2ad63b380fa | -13.4234 | -46.8503 | 2025-08-27 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e824e9e1-815d-3f7a-9f59-8f75912dea81 | -12.7843 | -48.1321 | 2025-08-27 06:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 27a42c2a-f36e-3273-a807-0aaaf5a723f4 | -13.4427 | -46.8473 | 2025-08-27 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 200a1c03-3eef-31e8-a034-bc79026b3f7c | -10.079 | -62.9094 | 2025-08-27 06:30:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 756341b2-fc8c-3882-82e4-694c56257ea3 | -14.4109 | -51.9269 | 2025-08-27 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 162.6 |
| f981983c-3b31-35a8-8d61-dd1024cba922 | -9.4062 | -60.5326 | 2025-08-27 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e82a0012-c4d7-3f06-9f15-bd5df79af540 | -13.4423 | -46.87 | 2025-08-27 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a69a17cd-0947-3b31-aa30-139c795e61d6 | -14.3915 | -51.9294 | 2025-08-27 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 4091b5a9-015c-3e78-9e79-83473c1b2bd7 | -9.4064 | -60.5133 | 2025-08-27 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 1dcb9896-c240-3722-ae2d-bfc5f57ffb2b | -14.4105 | -51.9482 | 2025-08-27 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 8732be8e-9505-3251-b2f0-0cff54e3f4b5 | -10.0977 | -62.9085 | 2025-08-27 06:30:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 2da85584-4e6d-3fc0-b0df-4d198dc55d89 | -12.7847 | -48.1099 | 2025-08-27 06:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 1ea1ba1a-a7f2-3fac-b8ef-670a1bad193a | -14.3912 | -51.9508 | 2025-08-27 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 72925326-ffc3-3a7b-8722-6e9a6af367b3 | -10.0977 | -62.9085 | 2025-08-27 06:40:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 28d4976e-6667-3e8a-840d-3f9b8c7eb2a2 | -13.4427 | -46.8473 | 2025-08-27 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 529ea99d-cd76-3281-805d-accf68355dc7 | -9.4064 | -60.5133 | 2025-08-27 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 28824c64-8efb-3e76-9b73-cbc2c7ec3d76 | -9.4062 | -60.5326 | 2025-08-27 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c77f4dd5-e50c-3ae8-9d16-d4d2b15cc754 | -6.8412 | -58.9746 | 2025-08-27 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0e8855f7-1955-3331-a0dd-2783fca152be | -13.4234 | -46.8503 | 2025-08-27 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9406cde7-1f09-3906-b416-67206ba6f9e0 | -6.8413 | -58.9552 | 2025-08-27 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 44efb6ca-a0c9-3e0e-b8e7-708c4b4f0fa8 | -13.423 | -46.873 | 2025-08-27 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 21a30778-f572-3c34-9759-5139d9591c9a | -14.4109 | -51.9269 | 2025-08-27 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| db3ee1a3-2b4b-3695-931d-adf3766ea219 | -10.079 | -62.9094 | 2025-08-27 06:40:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f529cdbe-be71-359a-a73f-02c5e481b04f | -12.804 | -48.1072 | 2025-08-27 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4a7a9406-52ad-3c99-a38a-158925d0b1c3 | -12.7847 | -48.1099 | 2025-08-27 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a8aa84fd-0a29-32a6-aea9-3d66a60ce21a | -9.4064 | -60.5133 | 2025-08-27 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 991606f1-6b94-3859-a5a8-c51c8355d923 | -9.4062 | -60.5326 | 2025-08-27 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| fb1d41ba-8868-325c-b9cc-ba8faf53de03 | -6.8412 | -58.9746 | 2025-08-27 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| e35d4fab-8e23-3efa-b129-b03cd74309db | -8.948 | -65.9429 | 2025-08-27 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 68f8e520-be25-3c79-81aa-8d2aaf0db1d3 | -10.0977 | -62.9085 | 2025-08-27 06:50:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c1102d11-cc45-3e82-b605-0e433e2aad29 | -12.8036 | -48.1294 | 2025-08-27 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f0c42e37-6abc-3d19-968a-c669d5bb823a | -8.9665 | -65.9424 | 2025-08-27 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 26f5ed2b-faf5-3d8c-ac05-dd407ca210ff | -6.8413 | -58.9552 | 2025-08-27 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| a31db681-62d6-371b-899a-dd3056cf5f4f | -12.7843 | -48.1321 | 2025-08-27 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| cef654e7-8ada-3583-ae67-ec3307f76353 | -13.4427 | -46.8473 | 2025-08-27 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d7f063b8-9c72-3d5a-99c6-b50fb4e79e39 | -8.9295 | -65.9435 | 2025-08-27 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 7eb51382-eafe-39b7-85c9-27561d00eaa5 | -8.9664 | -65.961 | 2025-08-27 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 1221165d-3aeb-3592-a190-a471b2a7bcab | -8.9296 | -65.9248 | 2025-08-27 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 56d3abc1-f23b-30cd-8be5-7db6bda33b45 | -8.9479 | -65.9616 | 2025-08-27 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| edeede01-105a-3f70-9045-8b78eb8812de | -8.9294 | -65.9621 | 2025-08-27 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| bc3ec023-fdb6-3da2-86f5-e474265df589 | -8.9664 | -65.961 | 2025-08-27 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 14c3240c-cae4-34a5-a101-fc79e2b238ac | -8.9295 | -65.9435 | 2025-08-27 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 431e4f82-bf3a-3a4a-9b20-0d3a891d7c22 | -9.4064 | -60.5133 | 2025-08-27 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 89951c12-ab8b-3742-8954-e085ad6eba7a | -8.948 | -65.9429 | 2025-08-27 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |


[Clique aqui para ver as próximas entradas](README87.md)
