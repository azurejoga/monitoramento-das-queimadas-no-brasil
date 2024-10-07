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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd431e18-0823-31fb-945c-87af011a8d6b | -16.547001 | -57.128201 | 2024-10-07 00:26:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f122206-e8a5-37ae-a24b-5c1686289b97 | -17.6283 | -53.088 | 2024-10-07 00:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| c28e131f-565a-3985-b4c2-5ad802149731 | -17.6481 | -53.0849 | 2024-10-07 00:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 187.2 |
| e9c675bf-136d-3540-8079-c97e947bd33f | -17.6485 | -53.0634 | 2024-10-07 00:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 105.1 |
| c7b0c8e3-c25b-3e1b-b753-dfc37497cb94 | -17.6679 | -53.0819 | 2024-10-07 00:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 171.0 |
| b67c7ac4-58a2-34c2-bffd-0e9a8b22e71e | -17.6684 | -53.0604 | 2024-10-07 00:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 43ceaa53-6f37-3940-a681-7e9a95782b90 | -16.414 | -57.222099 | 2024-10-07 00:26:46 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 442550ae-342e-357b-9e0c-56dfad6f7537 | -16.419701 | -57.257198 | 2024-10-07 00:26:46 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c327f344-2929-3a6c-a822-9f4417a9611b | -16.4044 | -57.223701 | 2024-10-07 00:26:46 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 98c62400-9f40-3555-81ab-8b6803aa2403 | -16.410101 | -57.258801 | 2024-10-07 00:26:46 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c746f05-288a-3813-a38c-3d6d9e2d0797 | -16.394699 | -57.225399 | 2024-10-07 00:26:46 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 827c417a-3dc3-35be-9f41-8abbbea77387 | -13.3973 | -42.221298 | 2024-10-07 00:26:47 | METOP-B | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 33a9580d-70da-38b7-94ba-21361f33e72d | -14.1016 | -45.507 | 2024-10-07 00:26:47 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d056dfef-9edb-35ed-99ed-b85563deaedc | -14.1031 | -45.514 | 2024-10-07 00:26:47 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11a50e6f-9842-3407-a009-038aee2fff69 | -13.8318 | -44.614399 | 2024-10-07 00:26:48 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cefe97a2-0a53-3d0c-8ab3-88f3a772883f | -13.8334 | -44.621498 | 2024-10-07 00:26:48 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 498c38c9-fbcf-3f4a-8049-6070a80d1854 | -13.8349 | -44.628502 | 2024-10-07 00:26:48 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e669ce0-7955-32c5-b7e2-26a95e8edf88 | -14.0696 | -45.454899 | 2024-10-07 00:26:48 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a9a6499-1081-3d96-9862-71e86cf273db | -14.0711 | -45.462002 | 2024-10-07 00:26:48 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 504a6531-130c-32d5-8760-19e268eb6fc8 | -14.0624 | -45.5159 | 2024-10-07 00:26:48 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a45bb91-3137-3fce-b83d-908a66e57055 | -13.8286 | -44.6003 | 2024-10-07 00:26:48 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46483ead-926b-3936-bde8-6c1866ebcce6 | -13.8302 | -44.607399 | 2024-10-07 00:26:48 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 213c150a-2d69-376e-8a1d-8e2130f01770 | -18.5968 | -47.3109 | 2024-10-07 00:26:49 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 5c79db42-1ccf-3770-92b7-b1600f2b7178 | -18.4718 | -53.5134 | 2024-10-07 00:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 11f4ece4-7512-3032-a6fc-150285f67425 | -18.4722 | -53.4919 | 2024-10-07 00:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 34.3 |
| e474fc8a-90e8-3014-a80f-a214ac1fce53 | -13.8204 | -44.609699 | 2024-10-07 00:26:49 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad8ddcbb-847e-3749-895d-87d7b5b7cc3c | -13.822 | -44.616699 | 2024-10-07 00:26:49 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f9fc9932-dd78-3864-9694-cb6311c90095 | -13.8236 | -44.623798 | 2024-10-07 00:26:49 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7858a40a-25ea-321f-be0a-905f36b2d1a8 | -13.8251 | -44.630798 | 2024-10-07 00:26:49 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e036c085-9c82-3f29-b6f6-2b4576b0db35 | -13.8267 | -44.637901 | 2024-10-07 00:26:49 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 725e245f-ff5c-3de1-8fa2-481bdd243ef2 | -13.8138 | -44.626099 | 2024-10-07 00:26:49 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ff16a8f-edd8-368b-a42b-3c20f5f2d96d | -13.8153 | -44.633099 | 2024-10-07 00:26:49 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e98cf7f-7651-30d6-8bd5-e69bda8edb63 | -14.2117 | -46.439301 | 2024-10-07 00:26:49 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20b1a9f8-20bd-39c9-a60c-2b889ca59cf9 | -14.2133 | -46.446602 | 2024-10-07 00:26:49 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d11300ab-1717-3e84-a135-c811def9b91c | -14.2149 | -46.453999 | 2024-10-07 00:26:49 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ef5da3d5-b5ff-30ff-a970-0cb64e61281f | -14.2003 | -46.434101 | 2024-10-07 00:26:49 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bc530a72-ec3e-3b61-a1cc-a00355bbd2b6 | -14.2035 | -46.448799 | 2024-10-07 00:26:49 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6cc1814b-b1fc-3a6e-b80b-f6d8a70c0882 | -12.7088 | -40.203098 | 2024-10-07 00:26:50 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6aff33e8-9c87-3a0e-a4ee-0de38abf1940 | -12.7113 | -40.213699 | 2024-10-07 00:26:50 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ed929683-e01e-3422-a61f-cd0c67d37211 | -12.6991 | -40.205601 | 2024-10-07 00:26:50 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5df67089-d74c-3567-af00-7f225986198e | -12.7016 | -40.216202 | 2024-10-07 00:26:50 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6419367d-5af0-3331-bbc9-5dab13bf3d15 | -18.6391 | -57.2578 | 2024-10-07 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 5e911d75-b735-3b6f-8959-7965cf9f963c | -18.659 | -57.2552 | 2024-10-07 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| f223b329-41ff-305f-93a9-718bd2089a22 | -14.2815 | -47.392101 | 2024-10-07 00:26:51 | METOP-B | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9389a5d3-149f-3422-b97a-8cb53266bee2 | -14.2832 | -47.400002 | 2024-10-07 00:26:51 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44f00067-6726-350b-b614-8082f6e1aa8b | -14.2849 | -47.407902 | 2024-10-07 00:26:51 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f222f76a-daa7-3c62-8975-359987611c35 | -14.2734 | -47.402199 | 2024-10-07 00:26:51 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 36ddbc43-ce38-3cd6-991c-231b741d69d7 | -15.0747 | -51.424999 | 2024-10-07 00:26:51 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6d5e0386-630a-320e-a7b7-82dfeae38e29 | -15.9678 | -57.155201 | 2024-10-07 00:26:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b370c876-eb59-3fb0-93b1-8b844e24012d | -15.9526 | -57.122898 | 2024-10-07 00:26:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9534543b-db10-3499-97fa-051e2ea3ef41 | -15.9582 | -57.156898 | 2024-10-07 00:26:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99c8ee82-995e-3e99-a9ee-076d81baf705 | -15.9639 | -57.1912 | 2024-10-07 00:26:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 840f9fb6-e77e-3432-9182-62ef072b8fa3 | -15.9486 | -57.158501 | 2024-10-07 00:26:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 710c1162-30ee-35a6-b35a-0e1c528cc5c1 | -19.8318 | -42.3542 | 2024-10-07 00:26:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| 740bd1ee-decf-3a9e-8d6c-be3d47b1082a | -20.1026 | -49.0562 | 2024-10-07 00:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 531dcfd2-dda9-3f39-947b-c0c84af12031 | -20.1223 | -49.0748 | 2024-10-07 00:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 2fa2a477-cafa-37f9-b6ff-a2f99ed6f3cf | -20.1229 | -49.0518 | 2024-10-07 00:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 521.2 |
| 3881e149-da5f-3722-958c-d7518e3cedcf | -20.1236 | -49.0288 | 2024-10-07 00:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 174.5 |
| de1510c3-832e-39c4-9396-710ef9ce3e6e | -20.4661 | -47.6592 | 2024-10-07 00:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 151.9 |
| cb4028d0-d449-3185-a3a6-d3ab1db0b806 | -20.4866 | -47.6544 | 2024-10-07 00:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 125.6 |
| e1023141-a946-3612-bd41-f85d5880a852 | -21.0712 | -47.2331 | 2024-10-07 00:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 341.8 |
| f227ab87-88fe-3b95-979c-875f62467f46 | -21.0719 | -47.2094 | 2024-10-07 00:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 1eb5cccc-fc0e-3a66-ad1d-5291e1c86008 | -21.0919 | -47.228 | 2024-10-07 00:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 4bee4086-4dbd-3914-a256-50847438fcc7 | -21.0926 | -47.2043 | 2024-10-07 00:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c6110138-85d4-36ec-a7fc-0a27a62cec3c | -13.615 | -48.120201 | 2024-10-07 00:27:04 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a489a26-e261-3eda-8506-2e7574099106 | -13.6168 | -48.128502 | 2024-10-07 00:27:04 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 35f2498f-18f5-39d2-ae82-caf581295769 | -21.5843 | -47.9536 | 2024-10-07 00:27:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c6dc646e-e5ff-333b-b398-818fd83a9226 | -21.585 | -47.93 | 2024-10-07 00:27:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d4e4c059-4778-3277-8799-cb1f3e5f8ae1 | -21.605 | -47.9485 | 2024-10-07 00:27:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 105.1 |
| c1e3f521-592e-32f3-9220-478806f2ccd6 | -13.5839 | -48.118301 | 2024-10-07 00:27:05 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec894b28-a51b-3936-a820-161e7d834ae3 | -13.5741 | -48.120499 | 2024-10-07 00:27:05 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c3aaafd2-7676-3b55-8a84-2ec74c5604f3 | -13.6349 | -48.460098 | 2024-10-07 00:27:05 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7a32eb17-9b8a-33f5-a45f-c719026e28ed | -13.6367 | -48.4687 | 2024-10-07 00:27:05 | METOP-B | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9fc75bb3-aec9-304f-93cc-315591167bdc | -13.6251 | -48.4622 | 2024-10-07 00:27:05 | METOP-B | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c1a02b26-fb26-349b-a171-8076d6b577b7 | -13.6269 | -48.470798 | 2024-10-07 00:27:05 | METOP-B | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b325a6f6-3418-38e8-adc0-c7edbf16cabd | -13.5578 | -48.630901 | 2024-10-07 00:27:07 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8a3eb57a-d9d1-3814-9c08-2c4a9ddccf8c | -13.5596 | -48.639599 | 2024-10-07 00:27:07 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 19af107b-bd59-33cc-95df-91863a948bff | -13.548 | -48.632999 | 2024-10-07 00:27:07 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 88ca5762-c6b6-3ae4-a30a-0b84c4d6c7bf | -11.9257 | -50.077301 | 2024-10-07 00:27:07 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39e7eb9f-fe06-3e2d-98c3-26e6d4555e1c | -11.9298 | -50.097301 | 2024-10-07 00:27:07 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d192afc-28a4-320d-922f-7060a8a20618 | -11.9319 | -50.1073 | 2024-10-07 00:27:07 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| acc6f6a6-5ca7-38af-b134-f214c500216d | -22.1974 | -48.1778 | 2024-10-07 00:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a375494e-86c8-377a-848b-31309ddf9515 | -22.1981 | -48.1541 | 2024-10-07 00:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 6871f40f-3ad2-3a0b-861c-6f530cd1338e | -22.2183 | -48.1726 | 2024-10-07 00:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 116.3 |
| b6a6c9d8-5c31-3294-863c-767e1089ba01 | -22.219 | -48.1489 | 2024-10-07 00:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 6b1d2351-d309-3d6d-a0ac-58b24be8cb14 | -13.9226 | -50.8284 | 2024-10-07 00:27:08 | METOP-B | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5bf9d8d4-ac58-31e7-89ba-7c4a5d89f3e5 | -11.9179 | -50.089401 | 2024-10-07 00:27:08 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2830818a-cc2a-3c97-b9cd-79021944b760 | -11.92 | -50.0994 | 2024-10-07 00:27:08 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc7fe426-6663-3b61-a68d-2695b2463fff | -22.3713 | -48.6032 | 2024-10-07 00:27:09 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| 52f5b0b4-6823-317f-9ad0-c62035704e9b | -12.9039 | -46.947498 | 2024-10-07 00:27:12 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d695c7c-f4e2-30fe-8160-d23673900b37 | -12.8941 | -46.949699 | 2024-10-07 00:27:12 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c117160-5173-3dd6-96a2-44d5dbc47fed | -13.5798 | -50.284599 | 2024-10-07 00:27:12 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd0e3f02-5aaa-3e66-afc5-b8e93f8b183d | -13.582 | -50.295502 | 2024-10-07 00:27:12 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 71e104f2-a0e8-3e76-be83-23a4c6ad66dd | -13.5842 | -50.306301 | 2024-10-07 00:27:12 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b0dc2718-9df4-3130-b6dd-32b2dd9c9969 | -13.5678 | -50.275799 | 2024-10-07 00:27:12 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8d4477ea-ed97-33ba-b249-4b79c94dd28e | -13.57 | -50.286598 | 2024-10-07 00:27:12 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c46aa073-676c-32c9-9ebc-aba2ef8c504a | -13.5722 | -50.297501 | 2024-10-07 00:27:12 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c89fe6ce-f8d2-3fa2-8d75-3ee058f054e8 | -13.5744 | -50.3083 | 2024-10-07 00:27:12 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5766b7b7-b8a7-3844-b98c-e14f45a6dc51 | -13.341 | -49.312599 | 2024-10-07 00:27:13 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 70bf6892-2806-3564-9f2a-80e5b4057ffd | -12.9766 | -47.621498 | 2024-10-07 00:27:13 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
