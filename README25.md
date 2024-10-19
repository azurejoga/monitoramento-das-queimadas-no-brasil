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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f0eb791-b843-3f79-ab68-f7d19aaef34f | -16.8673 | -42.10777 | 2024-10-19 04:29:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| b1e0eb88-91cf-3c27-bcc0-d0a1f94d968c | -16.66908 | -42.08118 | 2024-10-19 04:29:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 98262d9e-d161-37bf-a15e-ff65ac8037a6 | -18.72372 | -41.76564 | 2024-10-19 04:29:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8e70a600-2306-3952-8fd4-748e259dd1b9 | -18.43228 | -42.2636 | 2024-10-19 04:29:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 80244c33-b191-3a4c-be51-2bf6de1c56cf | -18.4278 | -42.26322 | 2024-10-19 04:29:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 50f9f490-6351-3f19-a369-14770c212ffb | -18.40917 | -42.49433 | 2024-10-19 04:29:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2aca86ad-0105-3de1-a188-852f1064df2b | -18.29954 | -42.22287 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 109e994e-9270-3000-8120-930585a18abd | -18.29881 | -42.21567 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 31378b51-f900-3da7-a793-4a3781ef8f93 | -18.2983 | -42.22007 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 85868658-227c-3455-9d87-a2d9a9b21bca | -18.29781 | -42.2242 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3b87cb41-8cf8-3013-8550-20cb3f6ad30d | -18.29555 | -42.21849 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9f679aa9-ec78-3176-9c8a-30fdc9e7ef59 | -18.29429 | -42.2156 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 319bfc99-8a5e-35dd-80f3-b46bfa1b0b80 | -18.2938 | -42.21978 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 049b0d95-65ea-3078-9a5d-b7ccdb421c0f | -18.29106 | -42.21807 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| da9be957-d991-302d-b835-4e8f6e3c08cb | -18.2524 | -42.23783 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7e6e14a8-1956-3e01-92ba-50df2b6126b5 | -18.25183 | -42.24255 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 774e10f3-20ce-38aa-b317-716e99263748 | -18.23174 | -42.4437 | 2024-10-19 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0de87314-5c70-37e6-a27e-72dcc4bee0a6 | -18.09942 | -42.92044 | 2024-10-19 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ade77236-028c-39d7-aff2-dbf5c24aa8dd | -18.09923 | -42.91918 | 2024-10-19 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c71faa9a-28cd-3001-9796-1ee96c2691bf | -20.2477 | -42.98589 | 2024-10-19 04:29:00 | NOAA-21 | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 380f6aa0-eb44-3a1c-bf16-4ebcf9666501 | -15.61542 | -42.89826 | 2024-10-19 04:29:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b01f5b6-bbdb-3cf3-98d1-399ff1d1db45 | -15.61492 | -42.90202 | 2024-10-19 04:29:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9cbb055-4440-37ef-a281-4184292a72ec | -15.52573 | -43.13615 | 2024-10-19 04:29:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 804ee3c6-0ffd-328a-8fa1-a274c6008e09 | -15.52169 | -43.13556 | 2024-10-19 04:29:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2276251d-8cde-38b6-b67e-28b9ba43953b | -15.51764 | -43.13494 | 2024-10-19 04:29:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8a8ad83-e51e-33e8-8906-05691c803387 | -17.44025 | -43.65391 | 2024-10-19 04:29:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e60a50f8-a47a-3167-9952-c520a6fc9e6d | -16.83283 | -43.32079 | 2024-10-19 04:29:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49318b78-f211-34c1-a071-3172465ea4e7 | -18.69696 | -43.19806 | 2024-10-19 04:29:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7684ca76-e8b9-38d8-b991-8ad16fbb2033 | -16.71946 | -50.34723 | 2024-10-19 04:29:00 | NOAA-21 | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 158b7dcd-2758-3b83-af78-89ee5ade8d49 | -13.13622 | -54.92688 | 2024-10-19 04:29:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88b12980-7a51-3612-b1cd-9e25743395c1 | -21.00267 | -47.65598 | 2024-10-19 04:32:00 | NOAA-21 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2ea7916-da2f-3251-b2cd-9347ea8a4fa4 | -2.9489 | -52.9174 | 2024-10-19 04:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ad37fb48-8d0f-3089-b172-3936fe58d3fa | -2.9489 | -52.897 | 2024-10-19 04:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| bf53f615-0c1f-31c0-a0fc-7eb4d5ad435d | -3.4202 | -50.2164 | 2024-10-19 04:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 8e5522b3-4450-3509-bdcc-156762267fb6 | -3.4387 | -50.2158 | 2024-10-19 04:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 48a6fc17-2f59-37c6-bf2b-4a458f687620 | -3.4388 | -50.1948 | 2024-10-19 04:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f0254a97-81d4-3b6e-980d-0ad33a8a7b5d | -4.6873 | -45.8504 | 2024-10-19 04:35:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 10992346-06f8-3052-b5ed-6bd2602ef59d | -4.6875 | -45.828 | 2024-10-19 04:35:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 93.6 |
| cecf72fd-6a36-316b-bc95-54d4aa192f2b | -4.706 | -45.8493 | 2024-10-19 04:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 2b4e0ce9-6ddf-3e9e-9d50-cd6ba7c7ab1f | -4.7061 | -45.8269 | 2024-10-19 04:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 166.2 |
| af565035-34a7-31eb-b5f6-6f11c262c54e | -4.7246 | -45.8482 | 2024-10-19 04:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 4c19ac5a-a93b-3455-be77-c2ab7966d74c | -9.0344 | -67.4641 | 2024-10-19 04:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 6408b6e2-fefb-3145-aea8-c86c9fd7b678 | -9.0345 | -67.4455 | 2024-10-19 04:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 62725687-e3a1-3c3b-90f9-febaa0fa2c3b | -9.053 | -67.4451 | 2024-10-19 04:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| d3d7ad7b-366c-3c35-8f53-a9e4d84880a5 | -12.496 | -63.2832 | 2024-10-19 04:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7aea3c74-a958-3888-9a1a-2843bf8e49db | -12.5147 | -63.3014 | 2024-10-19 04:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| cd287eb5-b86f-39fb-8804-ea5f268a2330 | -12.5149 | -63.2822 | 2024-10-19 04:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0d09c494-0061-3533-aeb2-b1bbd6ff28d0 | -12.5336 | -63.3003 | 2024-10-19 04:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2ff1a620-3b79-3370-ba13-683680c7f6aa | -12.5338 | -63.2812 | 2024-10-19 04:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 46f1b4ea-f6e7-34fa-b841-8745cd7b8a03 | -4.71096 | -45.82914 | 2024-10-19 04:40:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 5a1e0e00-abe7-3729-8593-752dc1638ebe | -4.69402 | -45.82621 | 2024-10-19 04:40:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| bac48542-4025-3c08-b041-d5da6acca079 | -5.25465 | -37.50395 | 2024-10-19 04:40:00 | AQUA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 733b8888-44d0-38f0-a03c-56484391fd7e | -18.42596 | -42.25957 | 2024-10-19 04:44:00 | AQUA_M-M | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| dd0c46f3-f9ff-3b2e-81f0-6d6328f2175b | -2.9489 | -52.9174 | 2024-10-19 04:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| bf696b65-33ec-3fd1-92ba-1a86255ce4d1 | -2.9489 | -52.897 | 2024-10-19 04:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 075042b0-53e0-3812-bdd3-39975905f143 | -2.9673 | -52.9169 | 2024-10-19 04:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| fc9b3e9a-81b1-3b3c-8ef5-6c38de8947f4 | -3.4203 | -50.1954 | 2024-10-19 04:45:23 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 945a390c-a4ef-3d62-99d8-f79183cef7ce | -3.4202 | -50.2164 | 2024-10-19 04:45:23 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 158ef164-e444-3801-bd0f-b5a95ebee0e4 | -3.4387 | -50.2158 | 2024-10-19 04:45:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 3569b268-1dda-3dbd-a0e0-12d01969ce18 | -3.4388 | -50.1948 | 2024-10-19 04:45:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 03b2baad-3488-367e-9f73-fdadde12ff89 | -4.6873 | -45.8504 | 2024-10-19 04:45:30 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6398e3e5-5e1a-320e-87c3-cd1039bbe6a1 | -4.706 | -45.8493 | 2024-10-19 04:45:31 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 278.3 |
| 9c49c791-d120-39fa-a3cc-35a6e4ed4736 | -4.7061 | -45.8269 | 2024-10-19 04:45:31 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 206.2 |
| 43f36ba3-f9cf-3ce8-bca8-31d69f85cbf9 | -5.5716 | -44.8927 | 2024-10-19 04:45:35 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 84777854-e200-3e35-8cd5-ccc608ca5005 | -5.5718 | -44.87 | 2024-10-19 04:45:35 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 9b761a35-23f5-3393-ac5b-baddd90a1045 | -9.0344 | -67.4641 | 2024-10-19 04:45:56 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| f4fa3705-9edd-3f4b-8d7a-50e02c37b36d | -9.0345 | -67.4455 | 2024-10-19 04:45:56 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e65ca92d-73c4-3273-b548-9edc6022d52f | -9.053 | -67.4636 | 2024-10-19 04:45:56 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| c59350e1-76e2-3b87-b48b-a1a5c3ad25c8 | -9.053 | -67.4451 | 2024-10-19 04:45:56 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 2ba23668-d563-3caa-a714-ed3fc34a302e | 1.91907 | -50.85915 | 2024-10-19 04:46:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 006a9c52-6ced-3710-a0f1-d034dcdef588 | 1.72999 | -50.99079 | 2024-10-19 04:46:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 286dd69a-1931-3ccd-8e66-f1bdb71a58de | 1.72667 | -50.99131 | 2024-10-19 04:46:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c05c3b41-669a-3f14-9b40-5493d5b78589 | 1.45495 | -50.72715 | 2024-10-19 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61cc1bed-bc70-34d8-837f-6184369493c6 | 0.01502 | -51.14603 | 2024-10-19 04:46:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79c63596-0187-3389-a8e9-996aa989aeed | 0.00317 | -51.22194 | 2024-10-19 04:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d32ac15-70e2-3a6b-afbc-5d4429554568 | 3.05257 | -51.46751 | 2024-10-19 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 756fcf9d-24d8-3bda-929c-8b0d5f5c0615 | 3.05202 | -51.46396 | 2024-10-19 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9968b628-102f-33f9-9c3f-a67691928d9d | 2.47804 | -50.9913 | 2024-10-19 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd0d3f9f-8d46-36bf-a76f-765e8013da17 | 2.4775 | -50.98784 | 2024-10-19 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16b0409a-2413-3169-aa5a-88497d4d8d8a | 1.11928 | -52.32967 | 2024-10-19 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15813d45-2d68-3f2c-b84c-8dcd70bd6850 | 1.01154 | -52.21756 | 2024-10-19 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01752bc1-f225-3a00-b4de-bcc6503aa1d8 | 1.00816 | -52.21807 | 2024-10-19 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0de9a98-c552-350a-9f40-4f96d89de2b7 | 0.56514 | -51.43824 | 2024-10-19 04:46:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 992cb02b-0139-3393-820e-7b42feb5769a | -12.0041 | -63.5008 | 2024-10-19 04:46:12 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 63537af2-89a3-3796-a424-9f009fd2e526 | -12.0228 | -63.5189 | 2024-10-19 04:46:12 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 27fe4c2c-5333-31c4-b96a-94e42b18caaf | -12.023 | -63.4998 | 2024-10-19 04:46:12 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 0e01249c-afb5-3e1e-8266-e7bc0564f5c5 | -12.5147 | -63.3014 | 2024-10-19 04:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a2cc0e0f-74a4-33df-8156-1d8f74f80bf5 | -12.5149 | -63.2822 | 2024-10-19 04:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 56ace524-f9b1-3e50-8cba-ad9cf05ee55c | -12.5338 | -63.2812 | 2024-10-19 04:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 82e33ba3-0cdf-333a-b97e-6d6014d0ab12 | -2.05934 | -48.63538 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b8f0bc8-fa78-34cd-92aa-cd0434f41d11 | -2.94442 | -39.95632 | 2024-10-19 04:49:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3484da71-b695-3a35-bf7c-18797720a7af | -3.56157 | -42.0379 | 2024-10-19 04:49:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 238fef40-b465-337a-96a9-9e08bc58808f | -3.56101 | -42.04161 | 2024-10-19 04:49:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3409d547-437a-3c11-9190-88dfc9ac1cb3 | -5.92362 | -42.95821 | 2024-10-19 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 00e766c2-7a9c-3c92-a85d-8d66adb1f77b | -5.92314 | -42.9617 | 2024-10-19 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4ebe6639-51ca-3159-8207-2ced9ca3188f | -3.28024 | -50.17414 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85a887a5-11e1-3fc1-8e4f-7d1704dcc818 | -3.28542 | -50.94422 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d78ee8ec-d826-32f8-a50f-e628485b8b83 | -4.0718 | -42.91102 | 2024-10-19 04:49:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76305e2c-87b4-30eb-a0f1-8bfe24a7663b | -4.07129 | -42.91441 | 2024-10-19 04:49:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f13edeb7-58f4-35f8-b616-23a6f8000e74 | -4.49133 | -43.92567 | 2024-10-19 04:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
