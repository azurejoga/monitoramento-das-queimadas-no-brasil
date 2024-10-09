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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be8b724e-5cd6-3f08-9233-1649833d3957 | -16.94662 | -56.77647 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4c9d9d8a-fb43-315b-8ab6-38da4cac1195 | -16.94653 | -57.48237 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4cc9c0d5-4f4e-382c-b80a-10f5eec020e7 | -16.94631 | -57.50687 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7fcf3b80-7412-3037-8f02-8282328ecca3 | -16.94601 | -57.46186 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9b60b3c2-40d5-318b-bffe-092ff5d19180 | -16.9458 | -57.48631 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 41f41cdd-4c2c-3002-b23c-b68de8fecc7c | -16.94564 | -56.78183 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1fb05ce2-cd52-3416-b087-244761f72504 | -16.94558 | -57.51083 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4349b674-af63-3189-b3d4-2dcc90866d68 | -16.94528 | -57.4658 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 42166b4b-5402-3a73-9c05-7f344d465b85 | -16.94507 | -57.49026 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b604c1e0-f0f6-36f9-b928-d9d96081622f | -16.94476 | -57.44536 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 224f5e1c-aad6-3e65-a112-2744d6c6bea2 | -16.94466 | -56.7872 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ce2ce37b-90c6-3ea8-8ebd-889ad707d7a9 | -16.94455 | -57.46973 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 58631ea8-25b9-300b-aed0-e3e4807f05a8 | -16.94434 | -57.4942 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| cb66316b-109c-336b-89ed-b94f1ccefc34 | -16.94404 | -57.44928 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 274a5b2e-7881-33fd-861d-243e9c529067 | -16.94361 | -57.49814 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 700ea727-8c39-3c23-8559-b4dafd135ea3 | -16.94331 | -57.45318 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a5fe1e49-5d74-360f-ad57-67cd3a801848 | -16.9431 | -57.47759 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b5f04059-a83a-364d-9101-73052ae8f442 | -16.94288 | -57.50209 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b9f21b24-5c62-3827-8a3f-a07b6f1cbd71 | -16.94258 | -57.4571 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 89bde344-614d-3900-be48-241e7f59d99c | -16.94237 | -57.48153 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d23b9a22-0476-3420-8921-ca470d8a74f9 | -16.94215 | -57.50603 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 05456f4d-23ab-33cb-b446-f9a370efa8aa | -16.94186 | -57.46103 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 97d4c725-35d9-369a-a027-0f9549b3fa3e | -16.94166 | -56.78104 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e999b509-4264-34e3-991d-66c9db616822 | -16.94164 | -57.48547 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fad4332f-2bdd-3b88-aece-8993bcf0ae37 | -16.94141 | -57.50998 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8480cf17-7571-3cc7-a36b-223e08959678 | -16.94113 | -57.46495 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6f345246-0b51-3ccd-b921-023c7de10711 | -16.9409 | -57.48941 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| dce37338-9426-3ede-9414-f0528331e234 | -16.94068 | -57.51394 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 877b6b8d-dcc9-3cf3-9837-f50921f83321 | -16.9404 | -57.46888 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b42857bf-43c9-3b5a-91a2-d2b9a04d03c8 | -16.94018 | -57.49334 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 1a9a4c77-7bf7-3314-9694-a8b1a4bf3c8d | -16.93995 | -57.5179 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5d014507-ceaf-36c9-9746-6ea95c295b0c | -16.93988 | -57.44843 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c538d87a-daf1-33fe-a27d-39b4b9a70558 | -16.93967 | -57.47281 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 610d2fef-7b32-37fc-ba5f-400a815d0900 | -16.93944 | -57.49729 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d4efd9fc-16fc-3c5a-abfd-fc8022f27eb7 | -16.93894 | -57.47674 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1a0ed9cc-cdb8-3ad7-96a2-823f050bd202 | -16.93871 | -57.50124 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 74df67d5-0c81-3376-8001-63e70212eb1a | -16.93821 | -57.48067 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a46a6c9e-e56e-340c-9e60-bc7d1fd14d21 | -16.93798 | -57.50519 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| d1004926-ac6c-36da-88fc-0e52afb3b09e | -16.93767 | -56.78025 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 35140464-2496-33f1-babe-21e4a5ea051b | -16.93747 | -57.48462 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 7bec9ab8-1c6c-3339-99d2-99680bc58c73 | -16.93724 | -57.50914 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 27b6cc00-ca0c-3260-99b2-4fc33424084a | -16.93697 | -57.46412 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 269e8900-1478-3704-bde0-e115196ff666 | -16.93674 | -57.48856 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 54861057-fe6b-3139-b122-62d4bd746502 | -16.93651 | -57.51309 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8067cb67-cfe8-3b9f-8435-39e151cead78 | -16.93624 | -57.46804 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ed287089-a336-341a-b3a3-8feec341b3e4 | -16.93601 | -57.4925 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d45f48d4-c614-3e8d-a8c2-0c8e7bb0ef4a | -16.93578 | -57.51705 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fff0fc4b-192a-33bd-afd5-3c48713cd30c | -16.93551 | -57.47197 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 73479e5e-7440-3d18-bf6d-696a93349bfb | -16.93528 | -57.49644 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| cf86c45b-6da2-39e6-9248-a2faecb64100 | -16.935 | -57.45149 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9110a0f9-30bb-3354-a69f-e1e095f91927 | -16.93454 | -57.50039 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 2223c2da-2c6d-3938-a136-60385ca60223 | -16.93381 | -57.50434 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| a4175535-a8fe-3b21-910f-6611df689123 | -16.93354 | -57.45934 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c39b736f-3fde-3b06-bc7d-8ad60d5c226a | -16.93331 | -57.48377 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 021fffe2-caf3-343e-a0a3-eae2e86849c2 | -16.93307 | -57.50829 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b69eab20-74c8-3c27-b40b-14eb58c3b783 | -16.93258 | -57.48771 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1c479b2f-3119-3e8d-8ed3-40ea52645bf7 | -16.93234 | -57.51224 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f5c6d53a-46eb-3531-a768-6844026b385d | -16.93208 | -57.46719 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8aa26cf8-8f19-3c83-ae03-befbd94a37e7 | -16.93185 | -57.49165 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1db8f686-bd36-3868-b7c7-16a8028a6a04 | -16.9316 | -57.5162 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 81226928-9da7-3c5a-9580-6f0a6747bdac | -16.93135 | -57.47111 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3966a904-c3df-30e8-ab9f-7c9b6fc82921 | -16.93111 | -57.4956 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f971d8c0-1fc0-3d1e-9543-e4d0cf76fd64 | -16.93062 | -57.47504 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2e78c92b-f306-3a76-abb6-0ee98646a9e8 | -16.93038 | -57.49955 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| fbc677c3-6330-37e8-b4b0-5312644fc951 | -16.93012 | -57.45456 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ff309782-f91c-347a-8950-d702e9384e6b | -16.92989 | -57.47898 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7f1d2e7a-3d99-3672-bff0-4454b60f8c52 | -16.92964 | -57.50349 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| fed51d3d-be56-35f1-a1fd-5a89f372fdd5 | -16.92939 | -57.45848 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| da1b9bc8-c27c-356b-bfca-6e4fb097e086 | -16.92891 | -57.50745 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 42496fc2-e117-3663-a894-427c11c5543f | -16.92866 | -57.46241 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f0fd2369-2d9e-3b31-a444-2106852e57f4 | -16.92817 | -57.5114 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5cea06f9-7aa5-3ac9-aa01-b6898f76bb5f | -16.92793 | -57.46634 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 536a2728-7268-3c8f-b1f8-8f3f35f626c0 | -16.92743 | -57.51536 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| fb8617e1-70a5-3727-b80b-54a8e54e6024 | -16.92719 | -57.47026 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fde31c8b-b49b-3720-b035-627f3b077ec0 | -16.92695 | -57.49475 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 00e562ff-11ea-3a67-b292-7179eabea667 | -16.92646 | -57.4742 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7f29f047-7a1a-3d5f-b628-13a23b03a54c | -16.92621 | -57.4987 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 8f0ae4fe-9fe3-3f6c-be1c-94eeb5d906c7 | -16.92395 | -55.80819 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e0b0cc91-95c5-3a75-b90c-d886607fae99 | -16.92377 | -57.46548 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 872a2d7f-d393-38f1-9104-44dcaad08f7d | -16.92352 | -57.48996 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 00212a0d-5fb2-3bde-80ec-b55ea3aaf0b8 | -16.92311 | -55.81293 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| daef4963-15bc-31a1-93a8-ccf3274b8e83 | -16.92278 | -57.4939 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 60fde6cf-c0a1-3218-8ce0-b9eb6c48ca5d | -16.92018 | -55.80745 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 378174a6-07f7-3868-a0ef-7efb124857d1 | -16.91936 | -57.48911 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8bc510ae-1430-3d7c-b81e-2c22bd318802 | -16.91934 | -55.81221 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fd433847-b81f-33c0-bf27-0f38536c3500 | -16.91725 | -55.80197 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 7d20b5ab-c792-351d-9ff3-6366734e01e3 | -16.91641 | -55.80672 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1c3d1dcd-6c4d-30f8-bf4c-75979f2e5e47 | -16.91556 | -55.81147 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6c4dc31c-9f3d-360a-bb8a-eb78a3e7f9cf | -16.91472 | -55.81623 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| e022bd2f-558b-3d7e-8ae9-f13c20506689 | -16.91432 | -55.79651 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.6 |
| 1796959e-bab9-30b1-8b21-3a77fdd8b433 | -16.91348 | -55.80124 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.6 |
| 696f37b7-f5cd-3270-8e2a-147a7146e041 | -16.91264 | -55.80598 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 36f538f0-c59d-3761-acf6-3490af1af000 | -16.91179 | -55.81074 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| ecf3f964-2b6e-36c9-b799-dc5481e05324 | -16.91139 | -55.79106 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 1f1e89cd-dcd6-388f-8346-374f7e90ae3d | -16.91095 | -55.81551 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ee3c1b9a-c938-3538-9b8d-4d1da4ed5604 | -16.91055 | -55.79578 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.6 |
| e4f5957b-e8a6-3acf-b451-c50547494550 | -16.90971 | -55.80051 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.6 |
| 965a9698-627d-3dd7-8681-ae3f7e93bc8b | -16.90887 | -55.80526 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2bbabc42-636d-32bb-b5a0-96518945e26c | -16.90846 | -55.7856 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 380cd62f-0030-3d03-b188-7c0691fcb29c | -16.90802 | -55.81002 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |


[Clique aqui para ver as próximas entradas](README137.md)
