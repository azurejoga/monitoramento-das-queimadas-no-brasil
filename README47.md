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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61c3ddf8-484e-3f76-8dc6-ade025a2fac2 | -11.84784 | -49.22945 | 2025-11-18 04:50:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c5ec4c89-9e39-308b-8453-f07205604c9f | -8.86615 | -47.32122 | 2025-11-18 04:50:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccca29bc-b118-314a-ae17-f98a5326fcb3 | -13.21697 | -53.76662 | 2025-11-18 04:50:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 114e5517-ca78-346a-809b-74cb8ec9d719 | -12.07016 | -48.19407 | 2025-11-18 04:50:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fef04e68-c5b4-3f87-8d8a-e367e281ca76 | -12.8704 | -46.41215 | 2025-11-18 04:50:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4732ca2-4d77-36eb-bac5-1475d46f8218 | -12.89188 | -54.72433 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 661a4bba-ce90-3de9-9621-d79e18cd2a7a | -6.99388 | -46.1839 | 2025-11-18 04:50:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5444ac31-bad5-3b53-9aab-dfad9b0f8cef | -10.50989 | -43.95971 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e6795e2-5ecd-39ed-b2bb-19088743031b | -10.87399 | -49.5436 | 2025-11-18 04:50:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 970269a7-5689-37d2-83c2-ceacd9a2ffa3 | -14.59201 | -47.99028 | 2025-11-18 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a17e5da-b384-39a3-bdda-901eba3cc252 | -15.47255 | -43.18029 | 2025-11-18 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 79c50275-2000-3cb3-a213-a99385b36b79 | -14.59015 | -47.99373 | 2025-11-18 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c5bfaf8-26fe-32b0-98d3-400abd1f20f3 | -15.47298 | -43.17653 | 2025-11-18 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a6518717-6c1c-34dd-a71b-8dfd68d135b6 | -14.59087 | -47.98859 | 2025-11-18 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46ff6fc1-cfd6-3c2a-96eb-5f3ab6d7b64e | -14.40144 | -48.28403 | 2025-11-18 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a99a4d1d-b708-3f9a-a874-24b7eb7be146 | -14.59525 | -47.99649 | 2025-11-18 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91b8e15f-4059-3d44-93fa-d84a3d56be1a | -14.59478 | -47.98969 | 2025-11-18 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ad6bc3c4-65ef-3b7a-b734-01b6dc52b809 | -13.8032 | -52.79514 | 2025-11-18 04:53:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b2d9d05-75a8-3c01-af67-ae4befbf8f59 | -19.21036 | -40.5757 | 2025-11-18 04:53:00 | NPP-375D | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6345e240-358b-37ba-9071-2a123fc3d5d5 | -29.88887 | -51.23016 | 2025-11-18 04:55:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 86284c04-3037-34b1-8815-2cf196636c9b | -29.1563 | -50.81442 | 2025-11-18 04:55:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| eca55444-b180-304d-96ab-057ab4893e86 | -29.88818 | -51.23611 | 2025-11-18 04:55:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 01a4fbbc-c3a7-3041-9b43-f9aca4ce3510 | -9.3969 | -48.4523 | 2025-11-18 05:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 865ab077-c582-3f87-b597-b47fac528154 | -1.9292 | -48.7946 | 2025-11-18 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 6a8e1d16-9187-324b-bcb1-c83452290f1a | -4.195 | -44.2247 | 2025-11-18 05:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| a2d3cc24-af6f-3584-bf3e-e6a843a28401 | -4.1764 | -44.2257 | 2025-11-18 05:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 4be06437-385d-3294-9af7-d9ef5bddb419 | -9.8919 | -44.1914 | 2025-11-18 05:00:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 9bef2226-72f8-314c-8768-d3c086c3c370 | -4.6547 | -47.9444 | 2025-11-18 05:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3d06c63f-f2bb-3785-9e71-449858df2201 | -1.41935 | -48.90342 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 828422c7-86a1-3281-a05d-0f632caca799 | -1.43906 | -48.90837 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 495887a8-36c0-31b7-9d2b-b6416a0660e3 | -1.91989 | -48.80521 | 2025-11-18 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 9a129337-0134-33d6-bb81-0bb484978a13 | -1.92069 | -48.79998 | 2025-11-18 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4123c4f6-b50a-360b-8bba-3a6399953a54 | -1.42881 | -48.90483 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 98dd2d43-3c52-3d86-83c1-60e3d2c6362a | -1.34392 | -49.32046 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fafa89f1-6bcb-3568-b43e-6c60631779d3 | -2.29429 | -47.23388 | 2025-11-18 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0b320b8-4f02-3c36-9370-0303a13df2ec | -1.32941 | -49.32307 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b517f399-6339-3927-953c-407ff54a63c0 | 0.05605 | -51.11341 | 2025-11-18 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ded20198-4769-3388-82c6-ecccd1d7c1ae | -0.98057 | -52.44756 | 2025-11-18 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b05af7a0-fd01-31a3-9a15-ba2331e0347f | -1.91588 | -48.79929 | 2025-11-18 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ca742a9-0913-3235-b221-bce8d88e8286 | -1.42487 | -48.90614 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 185a7c2f-7276-3a19-b5b4-3a06e3ee3e7b | -1.33858 | -49.32449 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d73aa907-df6d-3e4a-afb6-c27967f93300 | -1.43354 | -48.90557 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6d85f8f-7e33-3111-afd5-b84a6e8918e4 | 0.81191 | -51.85036 | 2025-11-18 05:08:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a7029b8e-2874-349c-b94b-c688e3743e39 | -1.32482 | -49.32236 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89489b97-929a-31ea-bad4-57fca98d08c4 | -1.33015 | -49.31835 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 18dc244c-ba58-3702-8fe2-ef84d93edfba | -1.43036 | -48.90182 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4fab7d0f-b61f-35b9-aa20-07d7186eb863 | -0.83312 | -48.6418 | 2025-11-18 05:08:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e4129c89-3b95-3e4d-8eef-02a6c710e2b2 | -2.29482 | -47.23044 | 2025-11-18 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 170385cb-ed8e-3da0-8f16-a19134fde727 | -1.4351 | -48.90257 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae3a844a-953d-3d35-a8cf-4b56531116f2 | -0.9783 | -52.45019 | 2025-11-18 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15ab193d-753e-3ac1-9ccf-ae4877242720 | -0.97685 | -52.44699 | 2025-11-18 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4dbdaed-a785-3c08-83c0-72c1e69c8d08 | -1.76344 | -47.2656 | 2025-11-18 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 297f53f6-a64a-3664-a8b7-86015416d03f | -0.97898 | -52.44576 | 2025-11-18 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 454b146e-33f0-38a3-8679-8858d76be0a4 | -0.83244 | -48.64521 | 2025-11-18 05:08:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b817a6b2-4a21-3ad4-9aec-ca9b47ff5643 | -0.82849 | -48.63934 | 2025-11-18 05:08:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d0ff5548-bf56-3629-8196-64755a18b7f4 | 3.61877 | -60.00327 | 2025-11-18 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a4b1da8-157b-3ccf-8544-c61a607310ed | -0.59682 | -52.16005 | 2025-11-18 05:08:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f454cd26-7c21-356c-8727-4506c4cc7ac0 | -1.32556 | -49.31764 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df6b8bd3-bd8e-3395-8dcb-3fb2dccea1bf | 3.66376 | -51.30111 | 2025-11-18 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b95bd765-fc7b-3cc6-96cc-14a005b2709a | -0.99198 | -47.07712 | 2025-11-18 05:08:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ea83057a-787f-3bfe-b206-7cbb397d99f5 | -1.33474 | -49.31905 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0fe324cb-b4fa-3594-8a30-e3614b3efb22 | 3.6593 | -51.29722 | 2025-11-18 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18484235-86d2-3fb8-b24e-09b79b31e3d0 | -1.334 | -49.32377 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9db3750-a78d-3f95-9897-f601478c0699 | -0.98664 | -47.07634 | 2025-11-18 05:08:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ce64da7-d000-342c-8ca3-d5f74c26bee8 | -1.4296 | -48.90686 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d30a1261-439b-3d95-bd89-377fe784efe5 | -1.42408 | -48.90413 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 116cdc57-11bf-364b-b81f-ecdba86ca835 | -1.42013 | -48.90542 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07a9a1f3-b6a1-3a76-929e-2e0fb895e8b7 | -1.92149 | -48.79475 | 2025-11-18 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d931b576-cc6c-3deb-b8b4-17e7c4069b62 | 3.66303 | -51.29662 | 2025-11-18 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bf2b669-6472-3541-b98c-599eecc3b77c | -1.91508 | -48.8045 | 2025-11-18 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53d8bf7c-ca9b-3934-b4f1-692fbd8c2235 | -1.43747 | -48.91136 | 2025-11-18 05:08:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f9043d6-4da1-3dc8-90ff-ff4af608f7b9 | -1.33933 | -49.31976 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e9629fb4-2348-3a57-bb18-6e9a67e85f04 | -0.59752 | -52.1555 | 2025-11-18 05:08:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 998b0a8f-d382-3a2c-8f1b-0a057af0628e | -0.59648 | -52.15786 | 2025-11-18 05:08:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c12d771c-8e9a-3a91-83b6-844d2a5ab5b4 | -0.82835 | -48.64106 | 2025-11-18 05:08:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d88765ce-45fc-307c-9e51-fda02b2ee738 | -0.8817 | -51.99638 | 2025-11-18 05:08:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 883eb93e-18d8-306c-a65e-13964878aec6 | -1.34318 | -49.32518 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 26e89072-451d-3f7f-9c5c-19e1ccc3afe1 | -1.32023 | -49.32166 | 2025-11-18 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f8bb59c-9d8f-3aea-944b-d8d13be96fb3 | 3.9884 | -51.68642 | 2025-11-18 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aabaf8b6-24a0-3288-93ce-9a0a54105f17 | -0.82767 | -48.64448 | 2025-11-18 05:08:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| de2aa6a2-63de-32e9-b3fb-fffc23d6278e | -1.9107 | -48.795 | 2025-11-18 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 2ad1fb0e-26f7-376e-98a4-b1676d873f81 | -9.3969 | -48.4523 | 2025-11-18 05:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 0565c66f-20e8-3574-8702-f7a8d008448e | -1.9292 | -48.7946 | 2025-11-18 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 6be91d4c-31d2-3589-bcfc-25950dda69d5 | -9.8729 | -44.1938 | 2025-11-18 05:10:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 3c1c2272-ae52-38b6-b5d9-eaa3092c2034 | -9.8923 | -44.1681 | 2025-11-18 05:10:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 459e9f6c-b4b4-35c5-aca6-746f7db36a5e | -9.8919 | -44.1914 | 2025-11-18 05:10:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| d7671586-e3cc-314b-a22f-7eae07548f68 | -4.13858 | -46.35751 | 2025-11-18 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 123feb3d-df92-3961-a0d6-34b60eb9a545 | -3.48425 | -52.35469 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 874beb16-1622-322f-abde-eeb4e6adffee | -3.231 | -50.49532 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed63feed-ef4a-39c1-98f6-446b41290937 | -2.94157 | -50.39103 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69617702-ff80-323d-a7f8-b2c34a0e46e4 | -4.22942 | -46.34207 | 2025-11-18 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca81dfdd-c3ad-377d-8652-45a4d083d75f | -2.51531 | -47.82388 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4be31ee0-fd94-3f5e-9886-30cf112f698e | -1.83973 | -55.24707 | 2025-11-18 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8d70f20-067c-3eba-bf45-e15587a73c04 | -6.44069 | -43.8148 | 2025-11-18 05:10:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 46cf444a-efb5-3b32-a528-7fe26e8cebcc | -5.03693 | -46.82695 | 2025-11-18 05:10:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e00c2538-e52f-394c-92fb-bfdf57f82a5c | -3.65382 | -50.80143 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92bd9e81-5098-3632-93ee-91b4a25edeed | -3.23222 | -50.49451 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2fd6d3c-7637-3411-894b-70d0a60f95f0 | -8.38416 | -44.0721 | 2025-11-18 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 029fb3ab-1ee6-3e63-a339-f6d83fa2d73e | -4.17366 | -44.23762 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 090ab38c-0e00-37cd-8145-ae386005eec6 | -3.14723 | -53.13773 | 2025-11-18 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README48.md)
