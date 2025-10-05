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
| d035d3e9-ec1b-3982-911b-9a14bc7e5c4a | -17.58714 | -44.41689 | 2025-10-05 03:55:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10e372c8-051c-380d-8f52-6ece87d0c6a1 | -11.81299 | -45.07407 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22d31bc4-fc3e-33bc-9a3b-44fbc1393611 | -14.3238 | -47.6708 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a9276c00-aac6-3243-a78b-33204cbb634e | -13.73446 | -51.27611 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4f838ae-3da7-3d8a-840a-d15334e18835 | -16.88032 | -49.39729 | 2025-10-05 03:55:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93cd8b70-5bf3-3233-ab07-a63438235330 | -13.14782 | -50.94267 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e2d0ab86-e3f2-389a-a627-ac254d318c2a | -14.6768 | -48.36412 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 920b6959-1260-39ba-b041-41048154a5d8 | -14.31862 | -47.69822 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e8dfa8ff-24e7-326e-b7a3-da07322d4f28 | -15.31527 | -46.36829 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f538f4e-fa2d-30a0-8dde-bab6d5576176 | -11.91816 | -46.24843 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4abd45dd-7277-3bd2-87f4-bf6d7ceab747 | -14.66306 | -48.35614 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80db3a34-3283-3862-a183-7fa7dfa687ad | -13.2865 | -47.82903 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9bc73a4-2bd8-3cea-bc24-af447faaffa2 | -11.85477 | -45.05602 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cedcc484-ce68-30ed-a643-946b48b81a54 | -13.28319 | -47.58786 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1f2c8619-050a-3638-8f51-90ed5f616f41 | -10.3595 | -48.17291 | 2025-10-05 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b881d20-a937-36ca-b449-d1efa3118940 | -11.23852 | -47.78669 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c10d106-06a3-329a-a71b-44f8fd4ef41c | -14.33146 | -47.682 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b58a85c6-cc92-30cc-aac0-19d0c4ef166e | -10.83836 | -47.97818 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ef94370-1a9d-32e8-b6b1-95a452f68a6d | -12.11419 | -50.90389 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 823a6951-3472-3e60-be0f-df305b30a9b1 | -13.11015 | -47.93515 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 795fe387-0d81-33e5-b858-80d47dbb6340 | -13.43428 | -47.28007 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba9ba4a2-1ff6-31c0-90e1-5b90f98cc20e | -16.00116 | -50.93282 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac15623e-7d87-3288-9a7b-ab57122381d2 | -13.27816 | -47.61233 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db80afa6-b96f-3292-a558-1e77cee0a37f | -11.4988 | -44.98253 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75fb44c7-3f97-3399-a58d-ba46ab48dc67 | -13.47256 | -47.22954 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dc29878-45a1-346c-9e71-48b9e711ac10 | -13.72755 | -51.27934 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 926382d7-cc7d-3c29-bd3f-d01832286228 | -14.66331 | -48.36415 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71118c62-ae2b-38fd-82a3-40c2a12b8168 | -11.1035 | -47.76288 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef864b81-e79c-32dc-9e08-a20a4e4f6563 | -13.28479 | -47.60599 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5285b195-b2e4-32f2-8bb4-67f05f58396b | -13.72522 | -48.09835 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de603d29-a939-3d1d-aa97-af12702ca2f2 | -13.30244 | -48.09802 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 190c8b2b-7d09-3410-b0a9-4a4263739dfa | -14.30057 | -52.92196 | 2025-10-05 03:55:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ec22da4-7681-3b72-9e8f-46daae338031 | -13.72869 | -48.07994 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 940f65d5-4331-3837-bf38-53901e36ab00 | -11.09964 | -47.75576 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0968ad5-fbd6-315e-8233-f78045cd3413 | -13.2734 | -47.61127 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e4f4326-fe69-3a6d-b895-d0009661f176 | -11.8603 | -45.04897 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4107f566-d89e-3c1c-93fa-3f6986349a65 | -12.45566 | -44.63894 | 2025-10-05 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2dca454e-f3d1-3c76-ae7e-1086abf582e0 | -11.53743 | -47.68076 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d690e3cb-0e1c-3c77-bd8d-49131a09d17b | -15.35417 | -46.30021 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41991a94-0699-38d5-af30-5d64f63120bf | -11.50088 | -44.99482 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6516fe7d-6aa4-303a-b5c2-026311c98e8c | -14.58885 | -52.46502 | 2025-10-05 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44ba62a4-3820-3e07-aee0-7cd746cf1f10 | -12.46235 | -45.52684 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55675676-d145-30d4-be67-050414e3ff0f | -10.6083 | -49.13309 | 2025-10-05 03:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c81f8b62-1d52-3137-b5c7-1df9e34012b0 | -13.45832 | -47.29175 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e1311e0-b5f4-36a1-8dd2-96a82b190649 | -14.69247 | -48.34534 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38a7ce65-0f8e-31e7-b376-a1d4a9c213bf | -13.30299 | -48.09109 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1cb44f9e-0b59-3010-9e2d-7bd7a605f772 | -17.24619 | -46.80279 | 2025-10-05 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f1ebe36-63d4-324e-ada0-915f13b37f78 | -15.6055 | -46.95066 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 411a6d46-8102-3e06-8baf-099684b8f1f5 | -13.23198 | -47.82439 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9763883f-b49a-3e46-9a21-1ae5231bb9ac | -15.71052 | -46.27894 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fe3a84f-b4b7-3779-932c-c33bbe7ab0e4 | -14.9923 | -49.98281 | 2025-10-05 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db8a5e8a-abc2-32fa-b431-37de6fcfa9c2 | -16.26476 | -47.11131 | 2025-10-05 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b297f7b4-1b32-3e84-95aa-6e6411305dfd | -14.67119 | -48.28668 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e6247e3-559d-3120-897c-8c0cb8503b8b | -11.05465 | -47.77859 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2a8b3fb-7fbe-389d-9e7d-7d6f6b4b38bf | -11.48535 | -44.97727 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d319ca2e-9078-3bf1-a37e-2e5ff37c6477 | -12.894 | -47.32394 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 96606d15-4435-34c2-a293-5cfaa0a3082e | -11.23112 | -47.7984 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6805b42d-afd5-3578-834d-39b54d646ec7 | -16.34337 | -51.47721 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 334dd4f7-cef3-3b7e-a409-4645200fd8fc | -16.0508 | -48.10015 | 2025-10-05 03:55:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cfa148c8-63e5-303f-bc11-3e717c7c76be | -13.29953 | -47.81341 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 604438c0-0de0-3198-8883-3d2c6a2c9fe6 | -11.11136 | -49.86443 | 2025-10-05 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3d105ad-284d-3d2d-99c2-0c5c43f0344f | -11.23283 | -47.78928 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 805dc890-4f71-3b1a-a5f8-2d311ec07d7f | -17.34885 | -41.89054 | 2025-10-05 03:55:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b5315f41-92f9-3023-8779-731db8ec0f08 | -12.89501 | -47.31872 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4af465a2-8c01-3407-94d9-0d716799487d | -11.67572 | -43.89771 | 2025-10-05 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e5394bb-ed08-32a6-b8fb-4bce8451aa75 | -13.14371 | -50.93243 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ce6cfc0b-9695-31f2-bc46-7e134c2f369d | -12.12659 | -49.43045 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35cca4e2-f0d5-36ba-b8fd-b394f3d5d38b | -13.71322 | -47.34908 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e26f4415-9688-39a0-8736-0ce0375f49b9 | -13.72164 | -48.09892 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6628b50-b381-3daa-a22b-bb39cea7f7a4 | -17.25044 | -46.80353 | 2025-10-05 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 887b8a1c-2925-3a9f-b36d-6e313652366f | -14.27481 | -45.87174 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3543625b-0e3f-3f5b-8e46-62d06cead0f8 | -13.91443 | -48.19138 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4dfe5f0f-89f1-3580-b1f5-cb56b9577c5c | -15.32727 | -46.37491 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 041fcf24-1ce1-3285-84ce-94f74ac11221 | -15.58327 | -52.48963 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a5ab0f9-0cd2-3752-85ff-43de91f53194 | -11.13067 | -47.92492 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2cb2acf-9511-3ff8-b80a-ca54b6c8e431 | -15.23079 | -49.30217 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7de3b6a-19a9-3f0c-8732-e2d635d192a2 | -14.67806 | -48.36684 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 2a435959-bde1-36fb-98f8-86980c289221 | -14.31549 | -45.8628 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2ae00d1-8b52-33e7-819b-6ee531a508b0 | -13.3464 | -47.19375 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13f92395-9d67-3404-bfae-97aa2a18cbb1 | -15.53737 | -46.80712 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f5962dc-81ee-35f8-acb8-fbcc0193e973 | -15.68538 | -46.27366 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee0f8785-e318-3ac9-b53f-f45ce942bda0 | -13.13019 | -47.97162 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fd75dd5-03f4-3cab-b743-4060d4130c1e | -13.1195 | -47.96692 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4e10c84-69da-3d64-b36a-ba4b10de6c89 | -12.82867 | -48.32664 | 2025-10-05 03:55:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d03c102-1534-366c-884b-7b9562dcf885 | -14.5825 | -52.46378 | 2025-10-05 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 362c24b1-8963-3c39-a56f-a213e1dafb26 | -11.48566 | -45.0317 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a3923ee-6611-3eb6-8dfd-1e136c7814f8 | -12.39081 | -51.10752 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 405349fc-0cb2-3ee9-9c5c-7163545a8d3f | -15.12545 | -45.73862 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6e9a54b-bea4-3060-8104-beff58c154ad | -10.84419 | -47.98728 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dff2c57-832c-3b3a-be76-96290c516b71 | -11.48474 | -44.98082 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43151a82-3492-3378-a416-071f6234dc97 | -14.46346 | -46.33912 | 2025-10-05 03:55:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7232f74-830d-34af-973d-4caca2140218 | -11.52867 | -47.67277 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 88d3377c-8e6f-35ef-b578-22e5d033b5af | -13.32372 | -43.03708 | 2025-10-05 03:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ecdd1e0-c5f7-343a-8145-e6b77bc1b8c1 | -11.8157 | -45.05905 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e4d38b40-b4a2-32b4-9903-00c9f2408efb | -11.83343 | -45.05571 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e567a4dc-c8d0-3518-b481-626deb95a1bc | -15.82289 | -42.61449 | 2025-10-05 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 83d231e2-3cb4-304e-bcc1-211d2d4383cc | -15.98243 | -50.91018 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2485412a-7d1c-3fa3-96cb-45e6de7bce43 | -14.6756 | -48.37052 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4afc4ca9-34b2-3b54-881d-2f1f57adf19f | -13.36857 | -47.55354 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4268454-e48e-3634-bf5e-8e946fd33deb | -15.80258 | -46.27588 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README56.md)
