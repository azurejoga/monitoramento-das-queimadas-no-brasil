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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81fe359c-6cef-3bba-aec5-8a9a40d98c3f | -12.84931 | -44.39824 | 2026-07-31 05:16:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc640830-d8c8-3941-933d-597567d75c53 | -6.56587 | -55.14378 | 2026-07-31 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e1752cf-d0fd-3a1a-85a2-e0615f39131a | -6.55491 | -56.53905 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee06b2e0-e444-3ce0-9eea-f8c6e98580f0 | -11.74334 | -48.91116 | 2026-07-31 05:16:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92a9f0c6-8f90-34e3-92bc-cf8512cfaef9 | -8.99687 | -45.18079 | 2026-07-31 05:16:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23853060-7b4d-360e-a257-83d9f1ef312b | -6.54363 | -55.15467 | 2026-07-31 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c6ecac8-b9f8-373b-943f-d3a96c82a05e | -6.56532 | -55.14729 | 2026-07-31 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf148f79-c26d-382a-bb0d-0a3a72ff4655 | -12.62071 | -44.62837 | 2026-07-31 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1860f359-5d80-3ff9-9cbd-0e5fbc7f0b24 | -6.88639 | -44.77853 | 2026-07-31 05:16:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ff4a3e0-d475-3473-95a1-42ae338756b5 | -11.44838 | -50.10101 | 2026-07-31 05:16:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb0f1b64-688f-3a88-b4ae-9d5c360f7863 | -6.17366 | -55.52909 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 171a9c7c-637b-3973-ad6e-8f692aa010d6 | -8.44235 | -51.49708 | 2026-07-31 05:16:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 635ab036-4f8b-37a8-9d22-2ec4cfde6584 | -6.17753 | -55.52615 | 2026-07-31 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48fc9d0c-0a65-3d98-81a7-3d4e4b65e9c9 | -11.8312 | -45.60749 | 2026-07-31 05:16:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4279cc6-6f1d-3f2b-93a3-9a2176f75ee7 | -6.56921 | -55.14431 | 2026-07-31 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9d50b01-4e2f-33e7-9c04-b883f93f8f66 | -14.38181 | -48.05643 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8c78032-b3cf-38bb-93dd-0c43068e2616 | -13.94571 | -46.18436 | 2026-07-31 05:18:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c9022a4-793a-3e86-9e83-37bdfcc92514 | -14.36466 | -48.05964 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e0675a4-2a0c-3156-9a11-fd1b89552fea | -15.62059 | -55.94892 | 2026-07-31 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 335c53d4-12e0-3085-bd13-448049c14697 | -14.37978 | -48.07408 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da3b4b11-d7e2-35cc-851d-91b2b3fb48b6 | -14.83341 | -48.52415 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ae0dd26-a7cb-32ab-8849-cf1129ad01b7 | -14.37459 | -48.0706 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08fffee4-2b79-3df8-a9ba-beadffbd70f6 | -14.35989 | -48.05885 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4f7b370-57ec-35d2-a4c9-cb12a739b015 | -14.37666 | -48.0526 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49d9fb81-cc4d-3679-9e28-caacf72f4077 | -14.05368 | -46.22087 | 2026-07-31 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c39202b6-9146-35af-b41f-44bb61e4988f | -14.36157 | -48.04493 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41eae2e2-559b-387b-8347-776cea4ee436 | -12.98774 | -53.80133 | 2026-07-31 05:18:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 971d6fdc-dd8d-3de4-84d0-2cb01cc114e5 | -14.37496 | -48.06737 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9515897b-6013-36cd-87a4-e585ddcb70ae | -16.40526 | -53.33504 | 2026-07-31 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 458231cf-e02d-3f8c-89a7-3027cba5ee4f | -14.35601 | -48.04463 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24422706-e929-3281-9992-5cb15b0b30eb | -14.38578 | -48.07053 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1aaa9752-c999-3876-a4c3-fa1f4dc37994 | -14.36677 | -48.04108 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13e904a3-4afc-309d-af37-b636735edfdf | -14.06657 | -46.21749 | 2026-07-31 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40d5ae81-39a4-3ffa-8dc6-aa5c94ab1388 | -13.90617 | -53.93616 | 2026-07-31 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46401d78-5f4b-3fb6-9d01-a95d691b2bcd | -14.83378 | -48.52108 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d57b3bf-bfc3-3224-9447-726395eb8d7f | -14.37576 | -48.06036 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0122f5b2-f318-300f-a40a-e2f842356e0c | -14.40588 | -48.04194 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9876c0c-0de4-38f2-b88f-884ef7439963 | -15.54282 | -56.0289 | 2026-07-31 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a96f82e8-9348-3fba-afc8-435dfb8090a3 | -14.37534 | -48.06405 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7307eaf5-aaf1-3555-a994-a91443c36cad | -14.38465 | -48.08028 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 730bf48e-539e-3e21-ae24-97af7296edbf | -14.83578 | -48.52715 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5fbae12-e664-35ee-a0a6-9d0c6d1d8209 | -14.07223 | -46.22293 | 2026-07-31 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 292b5370-647f-3a2a-814b-b8fca8c8b1a7 | -14.39178 | -48.06698 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24ce58a2-2ed5-319c-8e4f-0b9522ad0bc2 | -14.83079 | -48.52299 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec654301-0943-3504-be2e-31ec067d501d | -14.36071 | -48.05209 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22645fe1-2b8d-3df9-86f3-e117d80b6327 | -14.38502 | -48.07705 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8c0b71a-f175-3e15-a9d0-edde48a3b8b5 | -14.35478 | -48.05479 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73633c93-0126-32ad-9a5c-3a4d65ee1dd4 | -14.39778 | -48.06351 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e339502d-9707-3110-95aa-614cfb7ff6af | -14.3603 | -48.05548 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06d61ada-6813-3717-b551-af6a4b1f8579 | -14.37941 | -48.07721 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec2404a9-2b47-392d-981e-d149f037a026 | -14.38092 | -48.06422 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72264416-c83e-3fea-a7e8-cb5204a38604 | -14.3654 | -48.05953 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3634fb58-55b5-3d55-bc2a-99171c5e2e2f | -14.36507 | -48.05601 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9af62446-2f8b-30df-a217-3216bc30434c | -14.06039 | -46.21674 | 2026-07-31 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf12bab5-43c1-3aa8-b924-e092bd3732c5 | -14.05986 | -46.22158 | 2026-07-31 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db7d8d74-c737-31ae-8a3e-dcb322dcd6e1 | -14.35954 | -48.05552 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da91ac40-7acf-39c0-bd27-0bf41d0a3047 | -14.07174 | -46.2274 | 2026-07-31 05:18:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7f95f95-a52e-356f-9f2e-97b27d5d09b0 | -18.81451 | -53.13956 | 2026-07-31 05:18:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cec7e6b-cb49-3e4f-afa8-15db7e7359fa | -13.94679 | -46.18895 | 2026-07-31 05:18:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a099e3d-deb3-3088-b7d7-d8c6bb63e953 | -14.38656 | -48.06371 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5276daba-aa8b-3777-8d4e-0e3d31c1c881 | -14.38135 | -48.06044 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be0302cd-b3fa-3bb5-a637-30d5a3f5d58e | -14.05418 | -46.22228 | 2026-07-31 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2e5104c-f951-3119-b571-25a53d23ccd3 | -13.96071 | -49.14864 | 2026-07-31 05:18:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 949f7c33-cb31-3d1f-91b3-ec039ecc38a6 | -14.3613 | -48.04 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 546d24f2-ecd4-344f-9087-18353fc238fc | -18.36635 | -46.51539 | 2026-07-31 05:18:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25a31890-ba2d-3215-8ab2-0342eb25957f | -14.83612 | -48.52413 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91c9949c-a1ab-3806-8f30-56f618fa404a | -16.40127 | -53.33447 | 2026-07-31 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f76cc252-179f-3057-a6ec-98b26dc8064a | -14.39218 | -48.06351 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e12f7edd-d0ae-3e95-a1b8-48f36840ed3e | -13.74598 | -51.87878 | 2026-07-31 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5d40c99-c746-3a6f-a5ba-ad21da39357e | -14.35438 | -48.05164 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8893874-ca43-3091-82c3-b6e1ac26df6b | -14.22111 | -51.91593 | 2026-07-31 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 335e272a-6ed1-3bf6-a194-c4fd5c515b29 | -14.38617 | -48.06713 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e74717db-d9cb-3f37-9019-331ca52e255a | -14.83303 | -48.52726 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01590a60-35e5-386c-b38f-348c6b4017f5 | -14.39696 | -48.07049 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c29f8aaf-6784-3902-af35-ed1b245ef126 | -18.80983 | -53.143 | 2026-07-31 05:18:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cdec5c4-0792-3bc3-8402-fb0a32f91423 | -14.07274 | -46.21826 | 2026-07-31 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93be608a-7f48-3af9-ae16-26466a2b511d | -14.83006 | -48.52945 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcabf821-530d-3d06-8967-aeeff674dc2e | -17.53134 | -45.30775 | 2026-07-31 05:18:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4751d4d7-2b0c-3b36-b435-0a331dc0ef33 | -14.34969 | -48.05063 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f19a8bcf-e662-35b3-b49c-7fecd3e918ac | -14.38052 | -48.06762 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eb40dd79-4197-3683-a418-0e1d56ff5b38 | -14.40544 | -48.04571 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c74b338-b490-3072-adc7-ed3c85b3bfb0 | -18.814 | -53.14361 | 2026-07-31 05:18:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff0bda31-f0d2-363f-be5b-778c397b9bc6 | -14.06092 | -46.21814 | 2026-07-31 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 655d9a6d-1e0f-3ec3-8adb-c9063d9de1d5 | -14.39819 | -48.05997 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 498825e0-61df-3dcc-83e9-465bab01813d | -14.38226 | -48.05255 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b5d96f0-1b8a-3c02-acf7-f33f49b02b58 | -14.21209 | -51.91875 | 2026-07-31 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b7b66d6-5747-3fb9-bb49-7eeb6b06e631 | -14.35992 | -48.05215 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cfac9bb-9b4a-3959-bb6b-c2680a03cd67 | -14.83646 | -48.52116 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3fc88d0-6954-3f15-b423-cd480062b5a8 | -17.53191 | -45.30145 | 2026-07-31 05:18:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85d4939f-b5ce-3480-a8bd-e45d968421e8 | -14.39737 | -48.06702 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdb7cfea-a2a1-3ef6-bdce-09bc985e8a1f | -13.95524 | -49.15102 | 2026-07-31 05:18:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1af1fd4-a2c8-3f78-96e9-0f644e34cca6 | -16.40055 | -53.33987 | 2026-07-31 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0270ffe3-818b-3f72-8e55-3fccb4bbef6f | -14.38014 | -48.07095 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4293d2f3-6813-3c7e-a634-e652ebf12c89 | -14.83265 | -48.53045 | 2026-07-31 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad221196-862f-34a4-94f5-470903cf9d0f | -13.94518 | -46.18926 | 2026-07-31 05:18:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0d2281a-00b3-3e27-b4c8-a873aa2a3753 | -13.96108 | -49.14563 | 2026-07-31 05:18:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5514e1a-62e4-3512-b9e8-9ce41b9174b6 | -22.1578 | -56.0217 | 2026-07-31 05:20:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 811a5d8b-707f-3e4f-a99c-bdc3f8508ca6 | -21.37797 | -56.83439 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7882dea4-f9cd-3d76-9eb8-74f7dd542169 | -19.23458 | -56.74557 | 2026-07-31 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 1622c093-fd3b-3eb6-aa0a-d3b682a34cb6 | -22.15856 | -56.01209 | 2026-07-31 05:21:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README13.md)
