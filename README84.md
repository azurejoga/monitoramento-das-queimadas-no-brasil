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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e39d6a70-e167-3029-a17d-1190c339cb87 | -18.83887 | -42.91751 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a7d698b8-83e2-3692-99d6-c03af35c438c | -18.83662 | -42.97875 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0068b1a7-89d3-3c65-adaa-c6f40f12cbe9 | -18.83551 | -42.9169 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d5e7f100-9d84-3f6d-8ae8-a176064e0269 | -18.83495 | -42.92066 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 89c46ce2-a511-385f-8991-2a94b60bbf7b | -18.83325 | -42.97822 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c9a5ff23-1c97-33fa-b3b5-cc132cfb4f94 | -18.83216 | -42.91628 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1cec9984-0d9a-3398-a07d-fcaf41e3ed8a | -18.83213 | -42.98572 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f3bef467-ae4c-3f5b-9379-e9e56180a5c4 | -18.8316 | -42.92004 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9f7bf1c1-1791-3b00-b8db-56c98d03b1ef | -18.82989 | -42.97768 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b685c4c1-c72d-3ba9-9f02-eae1927786bc | -18.82877 | -42.9852 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 251185b7-7f5d-3a2b-bb06-4a340e07c651 | -18.82821 | -42.98896 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 0dfd4462-00d9-365e-9f97-e330588e4f6d | -18.82541 | -42.98466 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 23393311-7ee6-3f7a-9255-bbe457994afc | -18.82485 | -42.98841 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 9a5154ff-5836-3747-9019-88036ce0aa1c | -19.04419 | -43.20402 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b19e9f14-2750-3abe-bd68-4dc1d0b1f0ae | -19.04362 | -43.20776 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 114d99fd-9b14-34e0-ba07-97c2caa43e1d | -19.03858 | -43.19567 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c315588b-971f-316e-a67b-2e0aa9add0db | -19.03522 | -43.19517 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7030294f-134d-3baa-b13c-6a71846b1a39 | -19.03187 | -43.19466 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 695928c3-48f1-3922-a0c8-b22fff2b1a77 | -19.02963 | -43.18672 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 79344434-2b6a-3749-a753-df0b9e016688 | -19.02907 | -43.19044 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 774f51d0-bcfa-38e9-8e75-4040c5fe4ffd | -19.02851 | -43.19415 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| eb1e7338-476a-329a-9848-b37c8e8f5fe5 | -19.02684 | -43.18247 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8ccf96f7-c887-31de-aca8-edf05e637bb0 | -19.02628 | -43.18618 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 690eaaf2-d08c-3416-a7e0-9d7aba62a237 | -19.02572 | -43.18989 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| ee69cf53-980c-3b13-b49c-fb580907bb7c | -19.02517 | -43.1936 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| ea9639ce-46b8-35df-9d3e-e0ea28cb0c98 | -19.02461 | -43.1973 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 6f35dc52-702c-3586-8c68-9d9c284bb7fc | -19.02293 | -43.18563 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 28a4b317-72e9-3fe1-9448-7aab760cb861 | -19.02238 | -43.18933 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e4fbbfe5-80de-39df-a729-52a3097be68c | -19.02185 | -43.21563 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 105d9a08-db0c-35ca-8177-cc2b6343d97a | -19.02182 | -43.19305 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5dce970c-2d41-3329-97f6-687be1e0b8ec | -19.01958 | -43.18509 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 457729d6-dcbe-3d9f-a060-5edd79c2b973 | -19.01794 | -43.21876 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0418de07-d875-3e30-b400-53177aa699e6 | -19.01679 | -43.18087 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| c019d088-b93e-36ae-9d65-92daca839953 | -19.01625 | -43.20721 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a5b5dd2a-3724-3d62-8a22-cb16362d1b8d | -19.01623 | -43.18456 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9a537e87-38e8-36ea-9363-a3d7f3327619 | -19.01571 | -43.21084 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 89bbaffa-f0bd-33fd-a025-499231ce1846 | -19.01512 | -43.19196 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c63757ce-51eb-3634-aa51-bcda4bb3a297 | -19.01399 | -43.17661 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| 7a711cce-4069-3b3a-88cb-b8a0d65da52a | -19.01344 | -43.18034 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| bd0e4e12-e0fa-3458-9898-67bcc34f40b7 | -19.01288 | -43.18403 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 99ac3baf-6dee-35c2-ab10-029dc64fcac9 | -19.01181 | -43.21394 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0dacb9b2-b10c-3db8-8c59-2f6e3cabd437 | -19.01011 | -43.2024 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74c6af46-bb7d-3b06-adb1-be7a5a6eb2a9 | -19.01009 | -43.17978 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b566aecc-189e-3070-b7d1-874da7458928 | -19.00957 | -43.20605 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 61cc7443-37f8-3e6f-ac1b-64c92cf879f7 | -19.00953 | -43.18346 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cb88c323-a771-3909-9666-0df50c5295c6 | -19.00564 | -43.18653 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| abd914a2-879f-31bc-923f-c19baee0eacc | -19.00453 | -43.19388 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| adbc7739-a7c5-3c5a-8a26-a25cf6491aef | -18.97888 | -43.20473 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2cf60969-375a-3009-9f1d-5a936261c970 | -18.97777 | -43.21218 | 2024-10-04 04:12:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7c323560-2dea-3d86-a354-8674690a41e6 | -18.97609 | -43.20047 | 2024-10-04 04:12:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 61410b5b-c829-3b21-9b98-7652fa81e7d7 | -18.97554 | -43.20418 | 2024-10-04 04:12:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 25380000-21f1-3731-91e5-adb2517de854 | -18.97498 | -43.2079 | 2024-10-04 04:12:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a8f4f6d3-31d0-31c6-8021-9a80796398e7 | -18.97442 | -43.21162 | 2024-10-04 04:12:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73f9549c-1bda-3f10-831c-fd7631273222 | -18.97387 | -43.21534 | 2024-10-04 04:12:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0c330155-33c9-3f61-a3a9-f22fd199350f | -18.97331 | -43.21906 | 2024-10-04 04:12:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f732ac91-0a16-392d-837e-6abca8c4db67 | -18.97275 | -43.19992 | 2024-10-04 04:12:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 68b38e2c-82ff-365f-9209-9a7fdd46c41b | -18.93624 | -42.59312 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| af132c55-1440-3522-a756-131b7d840cf0 | -18.92406 | -42.84216 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d7f0bad5-716b-38a7-b339-82307a9e3717 | -19.28864 | -42.88443 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 864c3ac8-69ae-327f-914e-3c6f80f5dd70 | -19.28641 | -42.8761 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 55e2b48d-63d9-38c6-8044-732fc1de51ef | -19.28583 | -42.88001 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| acedb1e9-4684-3ba4-a67b-72d0ff8c1856 | -19.28526 | -42.88387 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 832c1d41-e638-3fe9-80ef-9fdfd8085b4d | -19.28245 | -42.87949 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 53282605-3f69-3aa5-b0f2-a45512613418 | -19.28188 | -42.88332 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 562c957e-d6e4-3a13-8001-3f18232cfd75 | -19.27907 | -42.87894 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8f945248-74b3-36de-be9e-013fca9e611a | -19.27628 | -42.8744 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a9b801af-33f9-37b4-8689-7a7d6328edb2 | -19.2757 | -42.87831 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 497500f3-868a-3927-99b4-5e079f8e7457 | -19.27065 | -42.86562 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7544f295-620f-3075-9f13-644f2c62a46e | -19.27009 | -42.86935 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cdfb1bed-bfc9-3f92-8fc1-f10ceac488f3 | -19.26727 | -42.86507 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 855985b7-595e-38d7-b4e4-7538e0db78ad | -19.26672 | -42.86879 | 2024-10-04 04:12:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| fdcae3f0-e159-3f08-836e-06592ea0abbb | -20.2811 | -43.51376 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 930371d5-bddb-33a4-b8c9-b0c3abd976c7 | -20.41679 | -43.55482 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 107b9956-7ed1-3789-b406-0800b96dbf41 | -20.27881 | -43.52898 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 30787dbf-4820-3443-be51-b94d05f95531 | -20.27155 | -43.53172 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 76f391b9-5867-31e3-8260-bc734f74a72e | -20.26992 | -43.51971 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e9a696cd-6794-32b9-90c7-7800061d0bb1 | -20.26877 | -43.52742 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6346b54d-76b7-3d96-b1be-646b3581c95b | -20.26601 | -43.52289 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7426dfcc-9a79-3e00-a243-9db6b2598a13 | -20.26544 | -43.52676 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5d5d7f41-9b09-3bd6-b6d4-8e08e98e3560 | -20.26486 | -43.53058 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a7a66021-6930-3cc7-864e-c5eb7c6e6e5c | -20.10421 | -43.42719 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b3a72d24-8570-3c6e-9258-88f67545aa41 | -20.0969 | -43.43015 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| af5a8a2e-daab-3199-b4c4-01603b7933b0 | -20.09204 | -43.41681 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 662246f0-5cab-30f7-b25c-075e57ba52ae | -20.08635 | -43.43184 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d6444ebc-a6d4-3173-b6c3-0e9c4e80bfe8 | -20.08575 | -43.43583 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6c939c37-f5b6-3b25-96ef-e8821558cf7a | -20.08243 | -43.43508 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d1525058-1dad-3bee-af0b-0814b6b6ec5b | -20.08184 | -43.43898 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d0c58581-fd16-3933-a495-62d76b6516e9 | -20.10086 | -43.42665 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| e92a0d49-eb7e-397c-baa3-982886947f55 | -20.09813 | -43.422 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 84b77ec5-6d85-379b-a3e5-962be1909d32 | -20.09751 | -43.42608 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 9b656001-6845-3d2c-a080-2d5106c9815c | -20.09479 | -43.42136 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fdb354bd-170e-33c4-a822-9c5e4d8be59f | -20.08966 | -43.43261 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 041f498c-8ca7-3147-8ae9-39efc81eaf5b | -20.08907 | -43.43658 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bf17bf5d-10f1-383a-82e3-1d057ec432f3 | -20.08848 | -43.44049 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 75cf19e5-f877-30ad-bac6-a4a64ede7e86 | -20.08516 | -43.43974 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 80f40921-f1b9-3aeb-99d4-62a8a82f63a6 | -20.08127 | -43.44283 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4e60939d-cb25-3de9-b50c-8a67ded89267 | -19.89161 | -42.10268 | 2024-10-04 04:12:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c1380fad-3209-319c-a752-b8366164c44c | -19.89104 | -42.10665 | 2024-10-04 04:12:00 | NOAA-21 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 18e5f894-0a1c-3d9e-92a8-33e77a829dc2 | -19.7706 | -42.16728 | 2024-10-04 04:12:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c08e7bbb-fb3f-3d11-8589-d018db648464 | -19.62255 | -42.25598 | 2024-10-04 04:12:00 | NOAA-21 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README85.md)
