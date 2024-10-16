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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 549bb409-b354-311e-9b75-70b27e8190a4 | -23.6581 | -55.23578 | 2024-10-16 04:36:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a2a7870-c6c1-31f3-b9fe-d178c7f4a10e | -23.6573 | -55.24021 | 2024-10-16 04:36:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6863246a-af05-3757-8375-ed2d2c7423f3 | -23.65638 | -55.2375 | 2024-10-16 04:36:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a041fdba-96e8-3c82-9cdb-02b764747b6a | -10.2439 | -47.3046 | 2024-10-16 04:36:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| febaa06e-b15c-34cb-94ff-7db6255cf1a0 | -10.2442 | -47.2824 | 2024-10-16 04:36:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4e065625-9b20-3397-ae36-411eec5670c8 | -10.2628 | -47.3024 | 2024-10-16 04:36:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 638d1582-118b-3d8e-9f92-9d97188aa7e4 | -11.7104 | -65.2235 | 2024-10-16 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 30411704-a06c-3ac2-94bb-8cdb57a74c08 | -16.9995 | -57.4791 | 2024-10-16 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 58c03dfc-96df-3ec1-b6f9-b613cd8dad49 | -17.0191 | -57.4768 | 2024-10-16 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 3d6a6351-6408-3afc-b98d-26166d482628 | -17.0194 | -57.4563 | 2024-10-16 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| e7a35449-23bb-3dff-8a01-9a230703dd77 | -17.1667 | -56.8232 | 2024-10-16 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| a60b57a8-2cf1-3cbd-8729-cc5b303dd0d0 | -16.9998 | -57.4586 | 2024-10-16 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 7d477a6d-ab0c-3e2e-aa38-cd1042b5df8b | -18.2742 | -56.5795 | 2024-10-16 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.7 |
| a830159f-c99e-3f20-b8f2-be926c91c6d0 | -18.2739 | -56.6003 | 2024-10-16 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.3 |
| e852817c-0834-3876-b47d-e21a442139c3 | -18.2544 | -56.5821 | 2024-10-16 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 5482e006-14ca-3958-af57-9b00baf3cdda | -18.254 | -56.6029 | 2024-10-16 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| fdc8091a-f3a2-352b-a791-f7bcabea701c | -19.5816 | -56.9653 | 2024-10-16 04:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.3 |
| 592606e4-1413-3d68-891e-ec95cd3ec2c9 | -19.6013 | -56.9834 | 2024-10-16 04:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 93a899b9-493b-38b0-a927-0ad6d12b6414 | -19.5812 | -56.9862 | 2024-10-16 04:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.3 |
| 9c74ad4c-84cf-3cce-87b9-972bb231cbf3 | -30.13234 | -51.31977 | 2024-10-16 04:38:00 | NOAA-20 | GUAÍBA | RIO GRANDE DO SUL | Brasil | 4309308 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| adbeacaf-77e4-3d87-9707-4c99a95ccd0a | -29.92029 | -51.11102 | 2024-10-16 04:38:00 | NOAA-20 | CACHOEIRINHA | RIO GRANDE DO SUL | Brasil | 4303103 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| de7a1654-1e35-301b-bd18-29a33270fb9f | -29.81344 | -51.17752 | 2024-10-16 04:38:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| ac8c3215-fc5c-3bc3-b6ca-da57e7acdbc5 | -2.6119 | -49.0772 | 2024-10-16 04:45:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| da7f9a97-3094-3b58-ac3e-1c343f6d5cfb | -3.1283 | -54.2259 | 2024-10-16 04:45:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c924ceb0-7e56-3ff7-ba21-728d0ab54212 | -3.1099 | -54.2263 | 2024-10-16 04:45:21 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 226dc7f0-2c35-3c77-96d7-1e509c902b86 | -3.9581 | -46.422 | 2024-10-16 04:45:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 3187787e-8bf1-353c-9930-79052e7e6b98 | -9.9588 | -47.3816 | 2024-10-16 04:45:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 076f992e-12d0-3dec-8e24-4c783e4a186c | -10.2628 | -47.3024 | 2024-10-16 04:46:01 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| a0387db0-d6a7-3de0-bbcd-af9b97a22e82 | -10.2442 | -47.2824 | 2024-10-16 04:46:01 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 37cabf69-ec56-3ab2-9dfa-65ed9fa7918b | -10.2439 | -47.3046 | 2024-10-16 04:46:01 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 770a5fc0-c7f1-3785-a15e-9991a07e1cf1 | -11.7104 | -65.2235 | 2024-10-16 04:46:10 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 52475c49-0c91-3ed3-9b62-a805a0be9065 | -11.7292 | -65.2227 | 2024-10-16 04:46:10 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| efd3d34f-fc41-3488-85a4-f523a5e98040 | -17.2081 | -56.6946 | 2024-10-16 04:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 294b3329-e8b1-3557-8399-8a70657f850b | -18.2739 | -56.6003 | 2024-10-16 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| b133bad1-d392-3cd9-873f-76f63d7ef531 | -18.2544 | -56.5821 | 2024-10-16 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| fe43c83f-ce59-35d3-9cdf-d446bec87f51 | -18.2742 | -56.5795 | 2024-10-16 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| f060ee42-69dd-33e4-afb2-89774d32b016 | 1.0016 | -52.2164 | 2024-10-16 04:54:59 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 3de78484-c98f-32e0-be24-b45aef06afc4 | -2.6118 | -49.0985 | 2024-10-16 04:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c3274d72-af6f-32c0-b2cf-567cf4dec08a | -3.0687 | -50.3746 | 2024-10-16 04:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6c85eb18-5292-30cc-9771-5b3338db77b2 | -3.0688 | -50.3536 | 2024-10-16 04:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 3bc7f904-932f-3c54-ae4b-f37c7a41e31b | -3.958 | -46.4442 | 2024-10-16 04:55:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| c235989a-7113-32b9-a4bf-590328e0e3ed | -3.9581 | -46.422 | 2024-10-16 04:55:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 4853f746-2a52-3ffd-b5f3-ec8523e8e2c4 | -6.2547 | -45.8593 | 2024-10-16 04:55:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 06761120-37bf-3e49-b2ac-fbe6f0b1f2a2 | -9.1709 | -46.9792 | 2024-10-16 04:55:56 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| ce5a8184-344b-30e8-b154-b5a9cd48d2d4 | -10.2439 | -47.3046 | 2024-10-16 04:56:02 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 51b2455c-bb8a-3336-a365-9a8c1d9d9a8e | -10.2442 | -47.2824 | 2024-10-16 04:56:02 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| b9668411-adc9-3714-88df-cba9b4434d59 | -10.2628 | -47.3024 | 2024-10-16 04:56:02 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 65f0975f-581b-3f54-8af1-12e56fdbe345 | -10.2632 | -47.2802 | 2024-10-16 04:56:02 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 406d5a32-c96b-3e9f-9c23-248b104d82a3 | -11.6917 | -65.2243 | 2024-10-16 04:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 0b73710c-619d-3982-a2a7-5847538b2419 | -11.7104 | -65.2235 | 2024-10-16 04:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c5a4b20c-dc91-31cd-9e19-a148e49eac02 | 1.0016 | -52.2164 | 2024-10-16 05:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 56a5949a-3c3e-3349-9627-de1863cac4b9 | -2.6118 | -49.0985 | 2024-10-16 05:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c81618f5-3cec-395c-acbf-f04adbcf426b | -3.0688 | -50.3536 | 2024-10-16 05:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b791ab16-8699-34e4-8ce1-b3a374a2669d | -3.1099 | -54.2263 | 2024-10-16 05:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d1c0c495-e675-3664-8c1b-a350c65a10de | -3.0687 | -50.3746 | 2024-10-16 05:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0bf70893-c5ca-33e8-a35a-7de68eebe334 | -3.9581 | -46.422 | 2024-10-16 05:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 20a6b4e9-bbf1-397e-937a-710bc4c765f4 | -3.0687 | -50.3746 | 2024-10-16 05:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| b1ed01f4-9644-377f-a509-0d0b63919238 | -3.0688 | -50.3536 | 2024-10-16 05:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 8c02f524-11a8-34d8-a85f-654b5a4c7ec5 | -3.1099 | -54.2263 | 2024-10-16 05:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 1afb4f1c-d7ff-3681-88f8-84fbeb8e8e90 | -3.11 | -54.2063 | 2024-10-16 05:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0c652810-1a42-3909-ad84-9eca7bae0527 | -3.1283 | -54.2259 | 2024-10-16 05:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8afea19f-2c23-3b6e-bcae-e7c3e6eeecbb | -7.78077 | -66.96048 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0104cac3-952c-3702-a2a7-4cba5ef0abba | -8.45773 | -66.96243 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d8baa1a-6fbd-3df5-9a8b-2e118a4b368d | -8.45701 | -66.96648 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 499d87fa-d752-32b3-99ad-69093af0334c | -8.45477 | -66.95876 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88b6a134-58fc-3ecc-a416-af58eac3d204 | -8.45418 | -66.95765 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6d3cbad-02e0-3adf-b6eb-513d82dcb4b6 | -8.45409 | -66.96283 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 445a4c03-ffb8-33df-9863-4f666d224b53 | -8.45347 | -66.96171 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8241572-4fe8-3b1a-962f-683fa6105e3b | -8.45341 | -66.96686 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6c75ea7-65ac-3e15-8256-38e0b46b945d | -8.45276 | -66.96574 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6abbe09f-4f08-3406-a200-e8d636f6e9d2 | -8.44983 | -66.96207 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 937b3d3f-6065-3c05-9153-b04abcec009c | -7.60965 | -67.35672 | 2024-10-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 755953d4-be81-374a-a0f2-e413b9e2ace4 | -2.43691 | -50.23649 | 2024-10-16 05:23:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 415a3b16-1eb9-3ced-a819-09011757a1f3 | -1.97905 | -46.36235 | 2024-10-16 05:23:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a91b0763-8e85-390d-ad33-8ef6232f5554 | -1.97219 | -46.36113 | 2024-10-16 05:23:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d132803f-f197-33ca-9bfb-d17bfa3122e0 | -3.29301 | -46.55268 | 2024-10-16 05:23:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f0d09c0-ad07-3c4a-9992-cd83266d7d9a | -3.29208 | -46.55915 | 2024-10-16 05:23:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c71e226-8ac2-346a-bd20-1842b41dc3ec | -3.28877 | -47.12711 | 2024-10-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b0467ca4-c72b-3765-b823-a477ffb72f04 | -3.28582 | -47.12232 | 2024-10-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| af7eb03d-59b7-3501-8627-99ca2e09b286 | -3.28518 | -46.55791 | 2024-10-16 05:23:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1199cd90-710b-3d9a-9f3f-ea76e0c4f88c | -3.28499 | -47.12788 | 2024-10-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 13f901ef-0f32-36a7-b260-f5c18f2b3390 | -3.28206 | -47.12623 | 2024-10-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2463fa19-42c0-3906-a725-84b61931071f | -2.33563 | -46.48492 | 2024-10-16 05:23:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b2b0a246-a1c5-3bef-98a6-11892d42f30f | -2.32784 | -46.49017 | 2024-10-16 05:23:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 372b0d99-9e7f-35fa-b981-87c11abbfad8 | -2.32716 | -46.48874 | 2024-10-16 05:23:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b63cd76-3d6c-318c-9d05-502bbfa79fd6 | -2.28511 | -45.88554 | 2024-10-16 05:23:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5eb2fa9d-8c0b-3e5a-a07d-729ae8245f13 | -4.74482 | -46.61736 | 2024-10-16 05:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2de64bc-efde-38e6-aa4f-9408c2c72ce4 | -4.73871 | -46.60987 | 2024-10-16 05:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86574e67-40ee-3763-b7cf-9552e4582473 | -4.73383 | -46.54326 | 2024-10-16 05:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d49e057c-914d-3dec-aba9-1270cb0f3aa7 | -4.73155 | -46.54127 | 2024-10-16 05:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f7fdd161-366e-3368-b5ea-4fbaef0907c8 | -4.73051 | -46.54901 | 2024-10-16 05:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 75c3504e-9c8a-30b7-8a7f-a708926b112a | -4.72677 | -46.54226 | 2024-10-16 05:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fdd6d0ab-b3df-300e-9d39-38b98c418ffe | -3.95968 | -46.42938 | 2024-10-16 05:23:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 27.2 |
| ac0b8efd-64fe-311b-9b5b-b88f4e27ad6b | -3.95868 | -46.43639 | 2024-10-16 05:23:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 323ae027-d839-30c7-b8b3-165ce28f9eab | -3.95153 | -46.43619 | 2024-10-16 05:23:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 95cc00ce-70fe-3e9c-91c3-482901879e0a | -3.93458 | -46.40353 | 2024-10-16 05:23:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0266404d-683f-37dd-a08e-7fc968130dae | -3.93353 | -46.411 | 2024-10-16 05:23:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22f126d8-f7a7-36a3-b7ce-3c568c1cf037 | -9.99533 | -48.64298 | 2024-10-16 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e23a37ff-7378-31bd-8d25-fa5b9805c9e2 | -1.44007 | -47.4107 | 2024-10-16 05:23:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bfad0e94-5526-314f-a1d1-5d8163781d7c | -1.43877 | -47.41072 | 2024-10-16 05:23:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |


[Clique aqui para ver as próximas entradas](README56.md)
