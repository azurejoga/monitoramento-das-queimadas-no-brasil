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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21026ef9-b8a1-3d85-827a-bab1b7344f95 | -18.1938 | -53.35568 | 2025-10-05 06:14:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c450e24d-8c72-37b9-b8af-a91da13bc5b0 | -13.45583 | -47.28662 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ab5f1ab5-1c9a-3db3-ba10-6a5c8ee50ad1 | -13.73639 | -51.29864 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4203ed03-5a89-3141-9126-14017337480e | -18.3343 | -45.87994 | 2025-10-05 06:14:00 | AQUA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 71f950b6-6728-33f5-8aa6-3fbb2c330629 | -18.23798 | -53.3629 | 2025-10-05 06:14:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8774e2d2-f651-36c4-ba97-d1020cb91e37 | -13.13697 | -47.97855 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 93e8a0a5-f094-3ffe-833e-9e7c8ffc5e8c | -7.75911 | -73.06934 | 2025-10-05 06:25:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82eb15ce-861e-3948-b052-f8728e216f77 | -7.36739 | -72.46188 | 2025-10-05 06:25:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf9e1087-ad94-3d3a-85b0-449dfb736816 | -7.91695 | -71.78249 | 2025-10-05 06:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb209ebb-51cf-312b-94c9-2c51976e416d | -9.71457 | -67.46797 | 2025-10-05 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a459971-38ba-3c37-b56b-8e17bb310128 | -11.76363 | -64.93092 | 2025-10-05 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4986eff-4885-3704-b0a2-9ad19493811a | -11.76429 | -64.92506 | 2025-10-05 06:27:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a084bfa-66e4-3613-ae71-824c62c4e3db | -8.42991 | -70.12392 | 2025-10-05 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e76d0d8-6e45-36e4-aadf-78a7d56d4b45 | -8.4357 | -70.11541 | 2025-10-05 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3fa733d-8c88-36fd-80a9-3a17c6c75215 | -9.71503 | -67.46434 | 2025-10-05 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5accb78a-7937-3a67-b56c-e86829a0bf2b | -8.43054 | -70.11933 | 2025-10-05 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 75c692d6-8c58-3a47-a685-416fa7f325b3 | -8.32135 | -70.19518 | 2025-10-05 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28d2708d-3c4d-3292-9aea-3d6ba20e0b6e | -10.80114 | -69.03584 | 2025-10-05 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c06b45b-32bd-3a82-94f4-a3d7185acdae | -8.4338 | -70.12916 | 2025-10-05 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a214ea77-40aa-3aa7-ad7b-33e6f5cecc4c | -8.42602 | -70.11868 | 2025-10-05 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3068ca8a-ba33-347f-a4ce-923489e67d51 | -8.42539 | -70.12328 | 2025-10-05 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df45ff0a-a062-3ddc-a83d-14be860e6755 | -8.42928 | -70.12852 | 2025-10-05 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 519d7ae3-53c4-3d10-9cf8-1633ec42de7e | -10.38698 | -67.96219 | 2025-10-05 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 126a822a-afa3-3516-97ea-ac5cec8c96bf | -10.38651 | -67.96574 | 2025-10-05 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5748f41-0515-3a53-b43f-c9fb2f995a95 | -10.80076 | -69.03886 | 2025-10-05 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de0899e2-3202-3169-a11c-6c6e24c18a62 | -9.15902 | -67.85334 | 2025-10-05 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 302b2ef0-38ac-3880-adf9-5ef30d4e60fa | -10.80581 | -69.03951 | 2025-10-05 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5be03fc4-c5af-3b4a-a4c0-a9e3093258f4 | -8.43443 | -70.12457 | 2025-10-05 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eff87807-8f7a-3d84-b7bb-4a70532a111c | -8.43507 | -70.12 | 2025-10-05 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 654c11d2-1e6c-3d49-89ca-bba8733b4c01 | -18.2569 | -53.3329 | 2025-10-05 06:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 164.6 |
| de4c2a0a-a03f-383b-9d6c-dfc4fd385ffa | -18.2565 | -53.3544 | 2025-10-05 06:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 91.7 |
| b1904fbd-5d4f-342b-a657-240452dfa216 | -18.2565 | -53.3544 | 2025-10-05 06:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ac8bbbf4-2091-34d4-bd4c-4baf28efff54 | -18.2569 | -53.3329 | 2025-10-05 06:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 7567e012-e1de-36f9-ba99-b1c5ebe796f1 | -8.4284 | -70.12447 | 2025-10-05 06:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3d8f30f-91e7-3383-bf69-2e7dc424341f | -8.42812 | -70.12517 | 2025-10-05 06:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66f79e47-9ec8-3417-aa4f-f47158f47a16 | -8.4273 | -70.13145 | 2025-10-05 06:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebc2f446-cac6-3cba-abf4-dc90be595a5a | -8.42122 | -70.1243 | 2025-10-05 06:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d496b4fc-3245-38c8-99a7-3a2c4e122377 | -8.42151 | -70.12357 | 2025-10-05 06:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4d74438-0bb5-3d8d-8710-89becc74457e | -8.42762 | -70.13078 | 2025-10-05 06:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a6b5dca-9853-3f95-8f56-9314f2f671e0 | -18.2569 | -53.3329 | 2025-10-05 07:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 76679a64-2d72-38f9-82d7-e5f38b594380 | -18.2565 | -53.3544 | 2025-10-05 07:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 55ba90c0-2648-3daa-a067-8d51636003b8 | -18.2769 | -53.3298 | 2025-10-05 07:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 848227ca-2a3b-3c98-bc03-80bb92418c96 | -15.5824 | -52.4916 | 2025-10-05 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 09dee8b0-9516-3e5f-93ca-3af69a03f193 | -15.6015 | -52.5102 | 2025-10-05 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e7c52d8e-cd0c-3aad-b173-984b8e718c30 | -18.2565 | -53.3544 | 2025-10-05 07:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6c5da9fc-6851-3d8e-9dfb-d096536b5ce1 | -18.2569 | -53.3329 | 2025-10-05 07:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 56059195-9bea-3ea7-a060-43e6196c7d75 | -15.582 | -52.5129 | 2025-10-05 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 761b255b-bca4-3522-98d1-22d223e20716 | -18.2769 | -53.3298 | 2025-10-05 07:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 94957314-b671-365f-86f2-fadf22e15b81 | -18.2569 | -53.3329 | 2025-10-05 07:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 05a288c2-5bb1-3378-98f1-7393d5b51698 | -15.582 | -52.5129 | 2025-10-05 07:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6363a100-fe10-3bf2-a942-4b699b25c8ad | -18.3345 | -45.8734 | 2025-10-05 07:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c11466bd-c19f-3235-850d-1b689f2fc2b7 | -18.2565 | -53.3544 | 2025-10-05 07:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b4d8b655-41f6-318d-a712-e8853b75e3a6 | -15.6015 | -52.5102 | 2025-10-05 07:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b3a1e935-57e4-35ff-94d2-63b783bef5b7 | -18.2565 | -53.3544 | 2025-10-05 07:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c11ee121-2a59-3b59-90e0-51bf9b031c69 | -18.2569 | -53.3329 | 2025-10-05 07:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 142.9 |
| a566f411-75a6-3892-baad-7050a583fab6 | -17.9605 | -57.5904 | 2025-10-05 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.3 |
| 80e7beb1-ad32-3acd-b847-7233eb533f7f | -18.2569 | -53.3329 | 2025-10-05 07:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 2916e992-23bf-3e94-8616-ac718328f556 | -19.0155 | -50.6045 | 2025-10-05 07:50:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 157.1 |
| f4bcd086-8de7-3c29-b106-acca975bbd16 | -19.016 | -50.5821 | 2025-10-05 07:50:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 98.2 |
| bf0aab3c-7bd2-3f58-ba45-ec027e72ab11 | -17.9605 | -57.5904 | 2025-10-05 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 9bdf95ea-a96c-3048-83a0-175f71127af5 | -18.9953 | -50.6082 | 2025-10-05 07:50:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 65.3 |
| 70b63891-5d62-3db1-a1ba-cf31740c3be9 | -8.42775 | -70.11796 | 2025-10-05 07:52:00 | AQUA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b3e7124d-e979-39fb-8651-352095bdc424 | -19.0155 | -50.6045 | 2025-10-05 08:00:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| 68b66b7a-94eb-3114-9826-589dd2ef6243 | -13.3233 | -48.077 | 2025-10-05 08:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 3a4adc26-103f-3dc1-acbc-3b7fed815d6a | -13.304 | -48.0798 | 2025-10-05 08:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 5c4eae80-cd73-3c5d-945b-49fef0f690df | -10.9494 | -47.0858 | 2025-10-05 09:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 159.4 |
| a4d98027-81dd-3f5a-b90d-31be7c5c4514 | -10.9497 | -47.0634 | 2025-10-05 09:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| bc5556fd-1ca0-3ca8-8155-0ab65d6b718e | -10.9494 | -47.0858 | 2025-10-05 09:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| f129ea18-286c-308f-a3e3-0f701a543f38 | -10.9494 | -47.0858 | 2025-10-05 10:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ab62ffd9-9e2d-34d9-a84b-0912f2a0e7f7 | -10.1954 | -46.7307 | 2025-10-05 10:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 51c3039a-73fd-32e3-ac91-fd82c8212e50 | -18.1968 | -53.3638 | 2025-10-05 10:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 01718aa7-656b-3a08-ab45-375d93ea47b9 | -18.1769 | -53.3669 | 2025-10-05 10:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3f4971a1-df3f-3ff0-89d1-6b19c07fdc85 | -10.9494 | -47.0858 | 2025-10-05 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b5bb3864-a759-3c90-96b0-e6a550ffcb4d | -10.9497 | -47.0634 | 2025-10-05 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| efdf18e1-e4b7-3941-9f6c-8d506abc1761 | -10.1954 | -46.7307 | 2025-10-05 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| a363262c-e736-3971-88a9-a3c4280740e4 | -10.9497 | -47.0634 | 2025-10-05 11:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9297e17d-01dc-303d-bf22-3a665cfe60d0 | -10.9494 | -47.0858 | 2025-10-05 11:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9ca28be2-bf50-30c8-8bc3-049ae1b50894 | -12.7102 | -45.8682 | 2025-10-05 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| c178cb5f-89ef-384d-a914-7a2e169dc9bc | -11.823 | -45.0596 | 2025-10-05 11:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 592483eb-bd34-3547-8c1c-9db82d2b472e | -10.9501 | -47.041 | 2025-10-05 11:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 7081e35e-e46d-3ea3-b77e-44d97e9a4360 | -18.1968 | -53.3638 | 2025-10-05 11:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 3275bfcb-afe7-3d51-a174-f3bbda08c180 | -10.9494 | -47.0858 | 2025-10-05 11:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 930314cc-88e9-3794-94b5-066fab41e63c | -10.9497 | -47.0634 | 2025-10-05 11:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| e8a67dd2-170d-3db6-867c-1723817add51 | -15.6903 | -46.2782 | 2025-10-05 11:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 235.0 |
| 0d7789a8-1b21-33d8-93f6-f1025d3311f8 | -12.6913 | -45.8482 | 2025-10-05 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e67b9a2b-b80a-341c-bfb4-2ef52bdcf4a7 | -12.7106 | -45.8452 | 2025-10-05 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 339.7 |
| 67528f50-02e7-3490-8501-2baa4f115112 | -15.71 | -46.2745 | 2025-10-05 11:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 7bc5690b-9d67-348a-ad5a-854a8142511d | -18.1769 | -53.3669 | 2025-10-05 11:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 83.6 |
| d38202f1-8a05-3757-a793-108f1fe99ae6 | -12.8954 | -47.2909 | 2025-10-05 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| d4cfb83c-4f95-3708-9bd4-812e48777e2f | -7.74472 | -42.51935 | 2025-10-05 11:19:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 46.5 |
| e683af59-e9c4-36f2-844f-0afd4720f361 | -8.02679 | -39.46893 | 2025-10-05 11:19:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 4deab1f5-998b-3b1e-846d-2ed5acae7e44 | -7.42127 | -38.30822 | 2025-10-05 11:19:00 | TERRA_M-M | DIAMANTE | PARAÍBA | Brasil | 2505600 | 25 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 5b35f068-c6e1-30af-8214-784311685ecf | -7.3223 | -37.99765 | 2025-10-05 11:19:00 | TERRA_M-M | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 7d7f6c9c-a6ec-33e8-887f-d73887b1b19a | -7.43346 | -38.30995 | 2025-10-05 11:19:00 | TERRA_M-M | DIAMANTE | PARAÍBA | Brasil | 2505600 | 25 | 33 | nan | nan | nan | Caatinga | 14.5 |
| fa0a020c-0a21-3043-ba8b-77c21e148938 | -11.8234 | -45.0364 | 2025-10-05 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 0436dec0-0c24-3c5e-aaf0-56e5cb3bef72 | -10.9494 | -47.0858 | 2025-10-05 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 0e48e049-75ca-3209-a16e-8ddbf3c28d94 | -10.9501 | -47.041 | 2025-10-05 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| c1633a61-b238-3cab-af99-3dd646a2bdde | -11.823 | -45.0596 | 2025-10-05 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 4ce7b601-730b-324e-844a-9ce07bd31119 | -10.9497 | -47.0634 | 2025-10-05 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 2f6ab97b-ebd7-34cc-8e60-9831cef0dc42 | -18.1769 | -53.3669 | 2025-10-05 11:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 76.0 |


[Clique aqui para ver as próximas entradas](README151.md)
