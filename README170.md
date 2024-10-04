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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa639fc2-9104-3c1f-a264-8cc0dd18f1c8 | -16.57045 | -58.20164 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0e08790f-3df0-3535-ac6a-dfecfb5f8eaf | -16.56706 | -58.20104 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0ace5475-ec74-3117-8146-824804358ccf | -16.56528 | -58.27504 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e7188014-9f76-3ed2-87dc-4eaa89a5520a | -16.56465 | -58.27885 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 63dea587-61e3-3a13-9657-d50ce6cece13 | -16.56188 | -58.27443 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7c3d3468-97cc-3c26-9e45-4df338eae027 | -16.54418 | -58.21254 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 892799ad-8f03-3bf2-b0c8-393a3a92678f | -16.54354 | -58.21633 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0fb6bf76-78ca-3a7b-994f-08e67450d888 | -16.54291 | -58.22013 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b92de271-9eab-332f-b5ff-50ed4520603d | -16.54078 | -58.21193 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1f62d2fa-843a-3d34-a3c6-617661316f23 | -16.53802 | -58.20754 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a283374d-4af9-334c-8f06-4066e51937b2 | -16.53762 | -58.23091 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 08bcb718-d1a5-3d29-9f61-6f150ab1df9d | -16.53739 | -58.21133 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4c474737-5af9-3f7a-86b2-233c6e1bf08a | -16.53612 | -58.21891 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0eb3b27e-1fd8-3197-86e9-882e319d0803 | -16.53549 | -58.22271 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 80e413a0-65d8-32e5-864c-66bb20b4ea45 | -16.53422 | -58.23029 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d66ce5bd-ba05-39b7-8b81-63fab56eaa35 | -16.53399 | -58.21072 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3e61cfce-e0d7-3a0f-83c3-98f3996b0254 | -16.53359 | -58.2341 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6e8b876f-65af-32e8-b97c-565d75a55501 | -16.53336 | -58.21452 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 45dc5b85-f86c-36ee-8182-9c08c8dd6e83 | -16.53272 | -58.21831 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7e114c89-bbfb-37d0-81cf-d4cf4f2e2315 | -15.16898 | -59.32088 | 2024-10-04 04:57:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13a4545a-b5f9-3ff1-ae4d-96ce61da6a5f | -15.12487 | -59.02927 | 2024-10-04 04:57:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82d400a5-6143-3c1b-a77a-5deeb3546de0 | -15.12132 | -59.02864 | 2024-10-04 04:57:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e59fb4-99c4-3e5a-9ae7-0681cb144b22 | -15.40518 | -58.53302 | 2024-10-04 04:57:00 | NOAA-20 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b2e4258-3465-383a-8ce5-69bd8c8dfd71 | -15.38516 | -58.15008 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c96bd6fb-be76-343a-87d2-71ccb1740b9e | -15.38242 | -58.1454 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f435f1e-fc7b-3bfd-971d-37cb7b6e96bb | -15.37156 | -58.14725 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcbea2c6-ae2e-3d66-8241-4542e3648e58 | -15.36409 | -58.14988 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b6ad977-66e0-319f-b808-87bd6571b975 | -15.36345 | -58.15366 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a056f280-4b32-34a5-ad77-365b5d44eb83 | -15.36066 | -58.14933 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87648214-2e86-37e2-9c8f-fbae489bb984 | -15.36003 | -58.15308 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5dfacf4-0fbc-3c1f-8238-9ce0fb3178fd | -15.3594 | -58.15688 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f3a1d31-d6f1-3746-9b6a-790a776d2401 | -15.35723 | -58.1488 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d85c3484-9af7-3836-9ec3-8775b7067c9b | -15.3566 | -58.15255 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc949d91-cc91-36ab-9f3d-f10489ec10cb | -15.35597 | -58.15631 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5045c157-ddf4-385e-ae83-e97048d94019 | -15.35317 | -58.15201 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9daf3a9-539a-3e6e-b8f8-0033a317dd96 | -15.27657 | -58.19146 | 2024-10-04 04:57:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c93cb507-e0a5-3c90-b24b-56748c3ef14a | -11.77036 | -58.89006 | 2024-10-04 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2df22d6b-9cf5-3a0b-9050-93040e4010f4 | -11.76669 | -58.88942 | 2024-10-04 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8fa2707f-efbf-347c-a14b-40d0067e5ad5 | -11.76302 | -58.88879 | 2024-10-04 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9974117-ee41-3951-8bda-2b38ff14021b | -11.67682 | -58.88962 | 2024-10-04 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85217a46-1e8d-37fc-b99d-9b872945aa06 | -14.17782 | -60.25574 | 2024-10-04 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34cb2170-05b9-3c29-8d2b-ce2dafc15b9d | -14.17698 | -60.26061 | 2024-10-04 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36b8dd74-3d8d-3d7f-a586-15797f511f4a | -14.174 | -60.25503 | 2024-10-04 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2370d66e-4cb4-307e-835d-3e5d4196beb3 | -15.1779 | -59.44184 | 2024-10-04 04:57:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3569f78a-4721-31d3-847b-f886f3f4479a | -15.17716 | -59.44613 | 2024-10-04 04:57:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6774809-0dd6-3bf0-997c-f732e6d4cddd | -9.92736 | -60.14407 | 2024-10-04 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d0d2d81-d8d7-3775-bff5-3d201efcab27 | -9.92674 | -60.14767 | 2024-10-04 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58460a06-ae5c-3453-99c4-c8f0a992ab83 | -9.90734 | -60.28378 | 2024-10-04 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03627833-364a-3f7b-b975-9344e18857de | -9.9067 | -60.28741 | 2024-10-04 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f56230d1-05d0-335a-84a3-3aa7a13f3360 | -9.90606 | -60.29113 | 2024-10-04 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f52d9669-4e50-3a2e-8598-b55d9f9f7233 | -9.90262 | -60.28664 | 2024-10-04 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8a7d411-b2f2-3963-bcd5-311a5be5cbca | -9.90197 | -60.29035 | 2024-10-04 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20dcedcf-0b35-3609-a076-7722c3a0dca1 | -9.48962 | -60.35918 | 2024-10-04 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20c9218a-449a-3a75-9a34-7fd37b8446f7 | -9.48898 | -60.36297 | 2024-10-04 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e547939c-cbb9-3845-9951-7b840aa514e6 | -9.39428 | -61.04321 | 2024-10-04 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 849707f0-ecdb-3cfd-8a6e-4c7246d8ab26 | -9.39356 | -61.04744 | 2024-10-04 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59606891-77cb-36db-ae22-3072a7084c47 | -9.38921 | -61.04667 | 2024-10-04 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 420479b2-9419-377b-9858-137c5f36d405 | -9.38777 | -61.05507 | 2024-10-04 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88c10110-fdf0-3cd0-815e-d683720fcc96 | -11.27084 | -60.59063 | 2024-10-04 04:57:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8481ce7-0bfd-36d6-98ee-95d7b330f50f | -12.73044 | -61.11374 | 2024-10-04 04:57:00 | NOAA-20 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ede6fc1e-865c-3bf4-aede-bddfbdbf79da | -9.16351 | -61.67204 | 2024-10-04 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3ca8b8a-a323-3ef3-8e72-c36bdcea83dd | -9.16269 | -61.6767 | 2024-10-04 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78dfc4e6-68dc-3d41-835e-1ea31ceb740f | -9.09342 | -61.13729 | 2024-10-04 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed8a627e-2745-32a0-86e3-29a38b882808 | -9.08903 | -61.13653 | 2024-10-04 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 835479eb-f6d4-307d-a78f-591041b8396d | -8.88178 | -61.82702 | 2024-10-04 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dce4631-3338-3ef5-897b-0c74f9410cde | -8.87717 | -61.82618 | 2024-10-04 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47693b43-e64c-3199-9684-74415871dc2b | -10.12888 | -62.75994 | 2024-10-04 04:57:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e95ce3ae-2476-3068-90be-696a31175ed7 | -10.12789 | -62.76546 | 2024-10-04 04:57:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cec08097-bb6c-30ac-b7f3-4f76d20ce814 | -10.12307 | -62.76454 | 2024-10-04 04:57:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 836d0756-b7b7-3467-9445-20eb736f953d | -10.12406 | -62.75909 | 2024-10-04 04:57:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cf6ada6-ec56-31ba-baca-96c2839ff6ac | -10.11824 | -62.76376 | 2024-10-04 04:57:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e4edf42-93d1-3ce0-a502-edd4d5e684cb | -10.51006 | -62.50384 | 2024-10-04 04:57:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 157d19bc-d80f-3bc2-a14f-fb51146c523e | -11.54952 | -62.41728 | 2024-10-04 04:57:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f77f3147-069b-3c36-8e19-a88bc1343694 | -9.33832 | -63.22118 | 2024-10-04 04:57:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d334eca-5097-3b34-a6fd-0202f0ec181b | -21.92604 | -48.41342 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e98e8d92-67d3-3440-a2f6-eabf8b6ad5a8 | -21.92081 | -48.41287 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c448bcce-11c9-3b5e-b41b-5cdcc4f86362 | -21.91557 | -48.41243 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04e71841-ed82-32ad-ba11-054521558307 | -21.91525 | -48.4156 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 927ba4fc-f305-3f10-8de0-9f4e7453f287 | -21.90999 | -48.41529 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fc19ee0-8755-3c67-9666-864ce8c00bb0 | -21.89873 | -48.47425 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c15c144-af0e-3cb0-8d57-30935d39f93d | -21.89841 | -48.47745 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3700f03-67ae-375c-8ca7-800cc05a4966 | -21.8975 | -48.4343 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f11da467-859d-321c-81b8-fdb5c36bfbbd | -21.89717 | -48.43757 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f26c0e8d-39be-33f0-a2b8-8aa706f0f7ab | -21.89317 | -48.47723 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a45b00a4-71ee-38a4-b695-94f4ca4529cd | -21.89285 | -48.48036 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c90eca95-43f7-30ed-90dc-580e15c9496d | -21.88729 | -48.48328 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e309ff2-89a5-34e9-8c57-7202e5843b7f | -21.8832 | -48.41902 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f9e2b615-7865-37e6-9aca-233499e9414a | -21.88287 | -48.42233 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67fa4152-8370-3ac1-b475-eb9e147a012a | -21.88252 | -48.42578 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 212ae65c-0314-396e-931c-97eb7d05c166 | -21.87766 | -48.42164 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| edd445e1-fc51-386a-8fdb-65476eb6ab08 | -21.8721 | -48.42437 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be0abe1a-4d11-33d2-86d9-d146b79aaf42 | -21.85681 | -48.41885 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e68df1d-5d28-3a90-b37c-66e34810f6bb | -21.85159 | -48.41814 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73afb32d-8342-3259-a6d2-cf6139b37f37 | -21.85126 | -48.4215 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db1e9b00-7075-3543-8729-403afdf823e2 | -21.85062 | -48.42805 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba092d25-9579-38d3-b624-ef35927a6bc2 | -21.8503 | -48.43139 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 545ec49d-91ad-3840-8b34-6ad1e2a78d61 | -21.84898 | -48.44482 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c0afe2b-6220-3dee-a3ef-ef4f150ddf10 | -21.84605 | -48.4208 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 972d9e61-48e0-3dfc-82a2-4bf9b92bf72a | -21.84573 | -48.4241 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f196f9ee-9ae2-36d3-bd93-52d44b568af2 | -21.84541 | -48.42743 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README171.md)
