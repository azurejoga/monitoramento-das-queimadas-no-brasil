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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e05eaf9e-526a-3429-90a8-2f17f09a162e | -10.18791 | -49.95985 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 169786a1-320f-3030-ab67-39e0f85f4d54 | -10.16339 | -49.98882 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b4eea5a-e68e-3a58-af63-22053d2bb3f5 | -10.15888 | -49.99177 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1202b0f5-df76-3934-bb32-46f08abd31fb | -10.15839 | -49.99532 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a75b8385-234c-3e1d-a96d-3711956efc30 | -10.15438 | -49.99471 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e93e4730-8864-3d40-8802-4243508fc1e8 | -10.1539 | -49.99826 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 395a47f0-19a2-3293-8ba9-56921f199804 | -10.15341 | -50.0018 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc6b2199-8a9c-3fde-b797-e21f8bb2d4b8 | -10.15292 | -50.00534 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3677e56e-e787-3188-8246-c9e8d0a80a7b | -10.15243 | -50.00887 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d219fc55-a6b9-31bc-8b26-4c30cbfcd757 | -10.1494 | -50.0012 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bba6aa3-74e7-3e15-92c0-92b06f60f302 | -10.14843 | -50.00827 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 160ed209-623c-3da8-baee-44eeb93fe9b1 | -10.14794 | -50.0118 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28df26f6-156f-37bb-87f4-63cfc41058b2 | -10.14393 | -50.01122 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79d5c653-12f0-384c-b9ef-0e6d2099d5c7 | -10.14228 | -50.01056 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a9b7084-40b2-3ff5-b2c0-1d3626ebcce7 | -10.14177 | -50.01408 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 657bbbc4-22bf-31ec-8c26-94ae90434ac6 | -10.14126 | -50.01759 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 416e8f2e-ca54-3d19-ab0a-55396e8c9f2c | -10.13944 | -50.01415 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b182091f-2a30-318e-a416-a53749201714 | -10.12627 | -50.00819 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2766ef1e-55f6-3bee-95f9-68a64e89fa0d | -10.12576 | -50.01172 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 504d139a-7fd8-3062-b3d0-b2a50e495d56 | -10.12226 | -50.00761 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9e181a5a-9c1e-3f7f-b58d-9e17f1950b0b | -10.11375 | -50.00994 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24346de9-d653-30ff-8d85-334e90c103cb | -10.10975 | -50.00935 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d668f8d-4146-3e2d-9522-0808a4130610 | -10.10925 | -50.01287 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c17fc212-769f-3ddf-87a8-076cde0a2f09 | -10.10525 | -50.01228 | 2024-09-26 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97481865-8516-3a9d-9e1e-ea16d6718b77 | -3.53943 | -49.18554 | 2024-09-26 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91f2df3b-c597-31f3-87db-627ed7ec4cf9 | -3.24927 | -50.4769 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 161b7757-9f96-363b-99f5-7458ae450556 | -3.23805 | -50.45997 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 787fedb8-d054-3b87-8d82-5909480461b0 | -3.23448 | -50.45942 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aef44caa-ad93-3190-b7d8-38716cf1a878 | -3.23385 | -50.46346 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7fd4c60-9f02-3bce-b894-662bcba24957 | -3.23036 | -50.32068 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8898084a-58ca-3678-ae52-8f85a5e2f45f | -3.23028 | -50.46289 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41812694-be4c-3759-84c4-01064f7a4023 | -3.22972 | -50.32479 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 23bf4215-c521-3bcd-9de9-f1d8de8f74cc | -3.22677 | -50.32012 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6a1eabbc-dfcd-3f52-b6ca-7df3384f353f | -3.22613 | -50.32425 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e40082ae-dd37-38aa-8653-85e131ce28c7 | -3.22317 | -50.31958 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eda8d21-0f2b-3c4b-90a6-60d236ddc655 | -3.18445 | -50.284 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 898b1faa-6a58-3d66-9c6a-cb30ccee9509 | -3.18382 | -50.28814 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51324a74-c1b6-3a4a-84fe-23d4b6ae0b4c | -3.1832 | -50.29227 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd9971b6-25dc-33e9-a13a-d26c471bc98b | -3.18023 | -50.28758 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e828ef0-8684-3dd9-8d7a-ef5b5e943e3e | -3.1796 | -50.29172 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b87fc40-beba-35f3-a1da-9907420b941d | -3.17663 | -50.28702 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cfcad7d-9e7b-39a6-abce-5de5113b1304 | -3.176 | -50.29116 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18138864-745e-3b9a-a3ba-687fbc8e56cb | -3.17241 | -50.2906 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8997f8e1-d8b8-36df-9b07-f24a2b8719c0 | -3.17178 | -50.29473 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72a68010-cf33-38b6-b3bd-8c133f07ed75 | -3.14889 | -50.2878 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e71e361-3e3e-37d0-833b-78eb86729344 | -3.14594 | -50.28312 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5d7f88e-ffc2-30db-951a-e792c2e42ad3 | -3.1453 | -50.28725 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f6b46da-310d-3d5a-ad4a-8ae5f2373582 | -3.14234 | -50.28257 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ac6eda68-6539-375f-87a9-4e0a767f3ca7 | -3.1417 | -50.2867 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 987d073a-205b-34cb-9560-a9a9df18ee7e | -3.13875 | -50.28202 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b3fc04ac-0b69-3101-94ba-1ab197829f04 | -3.06359 | -50.41294 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e060009b-bd7f-3b12-9930-41beb44bd252 | -2.96821 | -49.10069 | 2024-09-26 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e15e0435-6f69-36dd-b71c-c164070c0f80 | -2.95534 | -49.36159 | 2024-09-26 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8296910f-e637-3d7d-8a98-295af05bc040 | -2.95462 | -49.36618 | 2024-09-26 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4792e09-233c-33ed-8710-fe7a485f464c | -2.95226 | -49.35645 | 2024-09-26 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 033a6951-32e9-31a1-89d9-1754c2caf23c | -2.95156 | -49.36102 | 2024-09-26 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b98448f0-2112-3f4c-8a12-673c67a0be4b | -2.95085 | -49.3656 | 2024-09-26 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fabf8fe2-31fc-365a-b772-9312c55307a8 | -2.8296 | -49.14433 | 2024-09-26 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 317858e1-c9ba-34b9-a2f7-3c2cbbf45410 | -2.80082 | -49.58431 | 2024-09-26 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4e4c5ba-a3af-3417-a60a-0affe8f7a4d7 | -5.03346 | -49.76736 | 2024-09-26 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09904737-de39-32b1-8899-cdaf106b1601 | -4.77676 | -49.44159 | 2024-09-26 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c378d258-1220-3f4e-a5ff-422a9e7eb122 | -4.77602 | -49.44643 | 2024-09-26 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ea28748-e4a7-3c2e-9aa7-aef55b584f99 | -4.609 | -50.32339 | 2024-09-26 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3089db85-dfb6-3f69-8065-2cc0deedc633 | -4.58648 | -50.80909 | 2024-09-26 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a9fd937-84f2-3f00-8a1d-dfa402791d6f | -4.51285 | -50.81431 | 2024-09-26 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac567a2a-2816-3e42-ab02-6b4f45379909 | -4.31932 | -50.75367 | 2024-09-26 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cfeb3ffc-e894-3ef1-a35a-b065f371e5e8 | -3.95554 | -49.94344 | 2024-09-26 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99866275-99cc-395f-89ea-5c9c15c306f4 | -3.67491 | -49.79826 | 2024-09-26 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57f3f0b3-8aec-3ac5-8f15-1c1daf24f354 | -3.67285 | -49.80017 | 2024-09-26 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4cb945c6-c0b6-3022-a2b0-67c8da8449dc | -3.58874 | -50.5796 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39612140-2646-37e8-ab10-9e42d24ccaf1 | -3.57706 | -50.3784 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9f4c333-f529-3bba-af5a-87c8b50d6519 | -3.57513 | -50.3908 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f9ba84c-4242-30f1-8893-2e146ee3a177 | -3.57345 | -50.37792 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae37cf3-ca37-3eea-aea2-1119c1f8bbea | -3.5709 | -50.39434 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2b51913-6d3f-31b3-8596-1205b53778c1 | -3.56985 | -50.37741 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3d4394e-2c37-3990-9042-d857bf66e70b | -3.56798 | -50.57232 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47b31cfc-658a-3474-ac60-e7a02948b475 | -3.56736 | -50.57639 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 69881b60-8e2f-35e6-9fd3-a74e04528336 | -3.56626 | -50.37682 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b90514a-4f6d-33f5-9d36-686f03778b0a | -3.56562 | -50.38094 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fec9b77-fce4-344b-b398-d870bd675dab | -3.56498 | -50.38503 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79e76194-3f1d-303b-83e6-4a97a5c7f070 | -3.5638 | -50.57586 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 085998ca-37f5-3f4c-a041-24f55e499bc4 | -3.56267 | -50.37624 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| ef9e474f-1612-3194-8a8b-d5330d593330 | -3.56202 | -50.38038 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| dacb8f36-09dc-3d4b-9585-2dd7658b1b2f | -3.56139 | -50.38447 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08d0138a-1da2-3a1b-9297-78ea2e47a503 | -3.55907 | -50.37568 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 553e0e4d-3c91-3287-a5a1-51e77de30797 | -3.55843 | -50.37982 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 12ed85b2-ff42-317f-a1f6-bd9f9f39001a | -5.4893 | -50.74601 | 2024-09-26 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac588875-a5d3-3e0f-9816-60817a9cf4dc | -9.18784 | -50.34306 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4d43b25-d7ea-395b-8141-b86a7464e496 | -9.18397 | -50.34248 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e681dd4-1391-3366-abfc-f84fa807f8c2 | -9.18326 | -50.34737 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82f724f6-1276-32d5-b44e-b62e7d826e25 | -8.03537 | -50.44397 | 2024-09-26 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d85bc090-88b6-3798-9f4a-9da7512fc907 | -9.34602 | -51.07159 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 38a6239e-fdd4-376c-8cd9-f93c62197e37 | -9.34539 | -51.076 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d28cb814-6dc8-3cb9-b2c1-bd48ae48c9db | -9.3438 | -51.07272 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2fc3738c-aa40-36b1-89b1-cf5f70a6d543 | -9.34314 | -51.07714 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d05ebbd5-e881-3425-88b8-c6f212356791 | -9.34248 | -51.08156 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 313e666d-ed7b-3211-90b0-47ad5e5dcc01 | -9.3423 | -51.07102 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 075bc9e9-a3c7-3404-a227-edba2d96dc0f | -9.34167 | -51.07547 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0072e1d6-64c2-3dfe-81cc-b62e6362fed3 | -9.34103 | -51.07992 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abb34ad2-f945-3910-8b80-9f4e59ad0410 | -9.34009 | -51.07215 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README92.md)
