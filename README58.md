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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1033926d-c013-3194-a6d2-370bddc4ab77 | -7.4553 | -72.72251 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e437d92-d051-3792-9b91-2cbd7e5686ea | -7.44466 | -73.17861 | 2024-10-20 06:14:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e623845d-88b4-38fb-b695-d54795e3c158 | -7.43612 | -72.82346 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 18021a9f-8d97-3a63-9a32-b35f09a51429 | -7.39719 | -72.7887 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c2cde0e-c4cc-32f9-a841-fedb0c2c18b0 | -7.39386 | -72.78819 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2afc197-cd18-30c0-899f-f471ff948603 | -7.39047 | -72.96283 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d322476-d8b3-375b-8734-786b3771ec95 | -7.38731 | -72.59718 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf9c0eb1-6230-3309-8030-70049587554d | -7.37414 | -72.87096 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb79073a-a279-3aa8-a853-374476e59057 | -7.37372 | -72.91736 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1efdef08-85f8-35ab-a0da-e1da419465ff | -7.36803 | -72.86643 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1332d170-1292-3f95-8c81-6cbfe95635cc | -7.36749 | -72.86992 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa29ba23-fa00-3b92-9b35-639388ef0cc5 | -7.36566 | -72.86632 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 764cfaff-e480-3231-85a8-0673810a2897 | -7.36512 | -72.8698 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 568908b1-2833-3298-a59d-c5eded4b3e32 | -7.36452 | -72.85184 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ed9d4d9-5ab4-3080-8be8-ca393efdfb40 | -7.36234 | -72.8658 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f4161bd-6b2b-39a3-8316-507394c3f9a5 | -7.36179 | -72.86929 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 96afb046-7bd9-3f6d-aba5-9c6f3e7156f4 | -7.36124 | -72.87278 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e06f87e1-a8df-3d8e-b981-b6d0382a43ef | -7.3612 | -72.85132 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a343949-cb75-30b0-a4c3-80e41e8982fb | -7.35846 | -72.86876 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0454be81-89f7-3dfc-bc5f-728c070227e9 | -7.35737 | -72.87574 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d065e47-d30b-3f4c-9923-89e977513f1d | -7.35026 | -72.92107 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae9a8511-d498-3d15-9da6-82e26ce61f88 | -7.3447 | -72.91305 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd153ecb-626a-3874-9eb7-93ffe1dc784b | -7.33997 | -73.03006 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aeb23bd5-91ec-3bf9-8131-bd9133833773 | -7.3277 | -72.76019 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7da4db9e-0df1-34ff-9e2c-9e335458eaa9 | -7.32648 | -72.94232 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73d7c8af-e8a5-31c0-93fe-a4c963c350b4 | -7.32491 | -72.75616 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 872bf63d-cada-3764-8ac6-803a6b39e135 | -7.32437 | -72.75966 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6956453-e8d0-36ba-83f6-fab4180f3d0c | -7.32158 | -72.75564 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a244d039-65a6-3253-bd3b-fdba2a75fc92 | -7.32103 | -72.75914 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9609c8a1-58b2-30b8-a814-6e0ab7e03909 | -7.31825 | -72.75512 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e075bfb-1908-3937-a245-480832b38ba6 | -7.3177 | -72.75862 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd8eb333-c6fc-3ea2-98ff-1b3ee4dcfd76 | -7.29099 | -72.92961 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9124acaa-2174-3baf-a035-8913ce5fe81d | -7.2797 | -73.06693 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0ce1dfa-439a-36ec-8333-0fabc343f020 | -7.27915 | -73.0704 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21411c4f-d93d-3156-b95e-d7a229401a54 | -7.26332 | -72.67493 | 2024-10-20 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2321e5e-bcb7-3a40-906a-aaaffbd7fc65 | -6.95453 | -71.49508 | 2024-10-20 06:14:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0183147c-7b82-33b1-8c54-523d8fca334e | -7.27671 | -73.07133 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93940b2e-6aac-333e-a02d-9e21a1df70d8 | -7.31705 | -72.75853 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edc2ed7b-c5fe-35e6-bb9f-4c599d6f725a | -7.32166 | -72.7592 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 906f91dd-fa63-39f1-8541-c25896295ce0 | -7.32627 | -72.75986 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 750373c7-7dae-36a8-af4d-898ca35aa77a | -7.35648 | -72.87689 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a65e5f9-1940-3e5b-9c6b-0456b4cc4da0 | -7.35713 | -72.8722 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32ebd40c-61bc-34cf-b104-d2fc2dd98eb2 | -7.35779 | -72.86749 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4e18de7c-6627-30ff-8ab0-682a674f8e49 | -7.36171 | -72.87286 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 67e36895-6cdf-37e7-afc9-234e8d06b03f | -7.36237 | -72.86813 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5271cedd-57cb-3846-acae-2a01de759f53 | -7.36259 | -72.62847 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48f83994-430e-3589-a965-3d1db7bd1a41 | -7.36434 | -72.6273 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ff0011c-3c95-32f8-8442-a4e80920c8ed | -7.36629 | -72.8735 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f16a0c7-2f36-3aa1-ac5a-c7dc6c4fa4b4 | -7.36695 | -72.86879 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46b38c0e-5f0d-3885-b46f-ebe9029ccb7f | -7.39205 | -72.79032 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee09f2a2-495c-3e31-a876-18a40eb2c8b1 | -7.39666 | -72.79097 | 2024-10-20 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eadaa8f1-f8d5-30f9-9d90-18c4e24540fb | -7.57508 | -73.05103 | 2024-10-20 06:37:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e41238d-14c7-321c-9d64-3e84fb048a39 | -7.57962 | -73.05167 | 2024-10-20 06:37:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0146ae57-be22-3c3e-a573-354aec8ea644 | -7.58027 | -73.04704 | 2024-10-20 06:37:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58cfaa3a-8ba7-372a-be6e-fdc274787787 | -7.65505 | -73.24554 | 2024-10-20 06:37:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e2cd581-0d9d-38bb-9851-d5a21dcf3a10 | -7.70093 | -73.05241 | 2024-10-20 06:37:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55ae5390-4f35-3936-bea0-e8c9b8b34517 | -7.70159 | -73.04778 | 2024-10-20 06:37:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37615dd5-3697-394d-a4f0-5e33c631d23f | -7.70225 | -73.0431 | 2024-10-20 06:37:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b9ecb9c-88b0-31df-9a82-87a5a7f78038 | -7.70547 | -73.05305 | 2024-10-20 06:37:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cb95984-e398-3bc3-9127-ebf9c6481666 | -7.70614 | -73.04839 | 2024-10-20 06:37:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef0f54f0-4348-3021-b929-a4e73dbacae2 | -7.70681 | -73.04372 | 2024-10-20 06:37:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a927f304-7b3c-3b6c-94e5-143342b0e888 | -7.76785 | -73.07907 | 2024-10-20 06:37:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14b2d0e3-1195-310a-8ee7-8aea8bee8dc0 | -7.76849 | -73.07444 | 2024-10-20 06:37:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a75d08d3-9dae-31cf-97e0-b81ce67d03d7 | -8.33077 | -72.61581 | 2024-10-20 06:37:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 66eae125-3bc8-3f02-b5aa-4e8a0bac512b | -8.33453 | -72.61451 | 2024-10-20 06:37:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de1f5490-bdfc-35ea-a1fe-92a096877a4e | -8.33526 | -72.60944 | 2024-10-20 06:37:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88c3ca8f-8c3d-30f7-8596-7ae182ae01b1 | -8.33687 | -72.60632 | 2024-10-20 06:37:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bd5dec7-8ad5-3817-8071-9dd9077374d7 | -8.33999 | -72.61008 | 2024-10-20 06:37:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 800eda07-8d43-3e3f-b7ae-a5998ce22b81 | -7.36378 | -72.86428 | 2024-10-20 06:59:00 | AQUA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 4d38b2d3-11a5-3d87-983f-091ba95a8909 | -7.3623 | -72.87394 | 2024-10-20 06:59:00 | AQUA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 90b02ecc-3bf3-3ff5-aa57-439c9e25bca2 | -7.70607 | -73.04064 | 2024-10-20 06:59:00 | AQUA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| db371cb4-a038-3c4b-ad65-08204b8d47b0 | -7.58379 | -73.0462 | 2024-10-20 06:59:00 | AQUA_M-M | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f0826b36-642e-30e9-a7d3-e3d3f139c77e | -12.5147 | -63.3014 | 2024-10-20 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 31301a87-5309-308e-b38e-5f81c583a8bc | -12.5147 | -63.3014 | 2024-10-20 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 4598a6bc-1e31-3769-81b7-67872346501f | -12.5147 | -63.3014 | 2024-10-20 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 9a0e6019-258a-3b25-bc6e-69919bd1bd0b | -12.5147 | -63.3014 | 2024-10-20 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| c0bdf0bc-8784-362f-94ee-ceac345cbc7b | -12.5147 | -63.3014 | 2024-10-20 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 96e8d1e4-cfd0-3170-a2e4-15aa50cbd8c5 | -12.5147 | -63.3014 | 2024-10-20 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 65e236bf-0a16-316c-a016-84d0682fa0c5 | -12.5147 | -63.3014 | 2024-10-20 08:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d9ac10ee-1aff-3744-b0a2-183457a134d9 | -12.5147 | -63.3014 | 2024-10-20 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.7 |
| a4c7a653-91ff-3531-a5b9-96bfe715d8e2 | -12.5147 | -63.3014 | 2024-10-20 12:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| f32e6382-48f1-3313-91fd-ed05d1e1b41a | -12.5147 | -63.3014 | 2024-10-20 12:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 93250fe3-ec54-385f-b935-8050985d4090 | -1.0976 | -49.1915 | 2024-10-20 12:55:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d939ede8-15da-34db-b545-660932ee1938 | -12.5147 | -63.3014 | 2024-10-20 12:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f5a9c8ca-6758-3974-b39b-811ae6089bf9 | -1.0976 | -49.1915 | 2024-10-20 13:05:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 62c189cb-1a7e-3cf3-a82a-a37cf98161eb | -1.1161 | -49.1913 | 2024-10-20 13:05:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| bddb0cf7-b2c4-369d-a5b0-d69d6d129cf2 | -12.5147 | -63.3014 | 2024-10-20 13:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 751c012e-a27a-36bd-b83a-c417c6c57390 | -12.5338 | -63.2812 | 2024-10-20 13:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 9acb0f8e-bc86-3be0-9ccf-b9f3a8bb6c1f | -12.5336 | -63.3003 | 2024-10-20 13:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| b752553b-3f4b-3701-83e8-7c68bee66058 | -1.0792 | -49.1917 | 2024-10-20 13:15:12 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6413324e-6280-3f2a-a6db-62e7aa1309a2 | -12.5338 | -63.2812 | 2024-10-20 13:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 27e957cb-e8ad-3499-9d61-d38155d06ea2 | -12.5336 | -63.3003 | 2024-10-20 13:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 7cc22634-0266-3e9b-92e4-ed515037a263 | -12.5147 | -63.3014 | 2024-10-20 13:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 92ef992c-dd4c-3cb3-9352-c14b5533fa74 | -18.2184 | -56.379 | 2024-10-20 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.4 |
| b4335f84-5607-34bd-9c39-3ed84414e3ed | -1.0976 | -49.1915 | 2024-10-20 13:25:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| ba972037-fad6-316c-90dd-ccda6fa2b8c1 | -1.0792 | -49.1917 | 2024-10-20 13:25:12 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c8da41bd-c457-3095-8c75-0eb7b69bb53e | -1.1161 | -49.1913 | 2024-10-20 13:25:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1befe3fb-07c1-3440-8bc0-897824a2ef43 | -1.1348 | -49.0421 | 2024-10-20 13:25:13 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| bc32f49f-2261-3c95-af50-d32692b1c01e | -1.4671 | -48.9737 | 2024-10-20 13:25:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1f99bf93-8e84-3251-b9a9-5b6c2d12d8bf | -2.4824 | -49.102 | 2024-10-20 13:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |


[Clique aqui para ver as próximas entradas](README59.md)
