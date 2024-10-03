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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 880d5b72-0fad-33a8-96ba-8ea1a8e281d0 | -18.53891 | -42.24693 | 2024-10-03 04:53:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2720acce-aa7c-36c0-be4a-faf65245ecf2 | -18.5324 | -42.24405 | 2024-10-03 04:53:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 554fed70-14d8-35b6-9777-75c8a4259dcd | -18.53191 | -42.2496 | 2024-10-03 04:53:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 95d426d3-60d6-35bc-97b7-c4e905532ea9 | -18.52675 | -42.23142 | 2024-10-03 04:53:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 40ff92c3-8e5e-3a52-9948-bb88fe042269 | -18.29611 | -42.17247 | 2024-10-03 04:53:00 | NPP-375D | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 94ba6dd6-5d05-36d7-8ea9-b0d285e8e853 | -18.29427 | -42.16924 | 2024-10-03 04:53:00 | NPP-375D | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 82007c31-14ee-34bb-b8be-e6bec6fde19b | -18.2935 | -42.17742 | 2024-10-03 04:53:00 | NPP-375D | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 91f04fc6-82d9-33ee-b683-657690f25086 | -18.07358 | -42.62171 | 2024-10-03 04:53:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c56db7a1-9d36-3c25-961f-037d236d4650 | -18.06698 | -42.62173 | 2024-10-03 04:53:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 542da32c-80ab-378a-bb20-8d18f652be51 | -18.06038 | -42.62178 | 2024-10-03 04:53:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ee9f0fde-76de-3de8-a90f-db478d22ae85 | -18.05442 | -42.61493 | 2024-10-03 04:53:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9b96e7a9-5f51-30ec-9f57-18d540609555 | -18.05377 | -42.62206 | 2024-10-03 04:53:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 168c14c0-6761-32f6-b1c7-827bd0661a2a | -19.04118 | -43.19813 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a2fa4528-c093-372c-a0fc-2234989d5b19 | -19.04078 | -43.20261 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| dda12411-4649-3e04-b781-e133ef878211 | -19.03472 | -43.19851 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 9a04e5c5-b988-3d0a-aead-8f2abdcd4178 | -19.03431 | -43.20302 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 52d62cc7-b627-358e-9e47-c03d0d77ced8 | -19.03344 | -43.19826 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a544fd5e-d3ed-3293-b6ba-25e36c6c8c02 | -19.03301 | -43.20275 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f1974748-a4b6-3f44-8c02-8b22a0c708a4 | -19.02827 | -43.19866 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| add65a48-fc71-396d-a35c-a83dfa9e0690 | -19.02787 | -43.20317 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 99ce18d0-aa59-39d9-b114-fa61cb0a3b54 | -19.02699 | -43.19835 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 74522d40-0f01-3aa6-8491-1e86d142b403 | -19.02655 | -43.20297 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 55641026-62d6-3abd-8592-250522f519bb | -19.02186 | -43.19844 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 530352d7-7b92-356e-bf4f-eea18a1dc908 | -19.02142 | -43.20337 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 44893671-11b1-37c0-8b90-4be812580f1e | -19.02058 | -43.19806 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5999b3c1-4b19-3646-bdb0-b3decbd1fb97 | -19.02011 | -43.20296 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b18934c9-7ccd-3600-aa68-5516e470ac87 | -19.0151 | -43.20212 | 2024-10-03 04:53:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c38a5edd-ef56-37d9-9630-feb1af283788 | -18.84289 | -42.93148 | 2024-10-03 04:53:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c40bb5ba-feb7-339f-80e3-2a5e88cd7f82 | -18.84266 | -42.93157 | 2024-10-03 04:53:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b50f9260-1b5f-38de-aa12-040c24d5f978 | -18.84238 | -42.93681 | 2024-10-03 04:53:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5347358d-3a16-3a83-9f88-0ab22421f999 | -18.84219 | -42.93689 | 2024-10-03 04:53:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 06f9d2a6-3ac4-30f7-81b1-80c1127ea05b | -18.83733 | -42.92127 | 2024-10-03 04:53:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| dafc86c4-72e6-38f8-bb2b-1b85af7c4608 | -18.83704 | -42.92127 | 2024-10-03 04:53:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e9288891-87c0-3200-80be-b97c4db98c90 | -18.83098 | -42.91942 | 2024-10-03 04:53:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| cbb5aeb5-cee6-3a1e-a649-5fcfb4fb6041 | -18.83068 | -42.91939 | 2024-10-03 04:53:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a3e141fd-6e03-3449-8c21-59116749f7b3 | -18.83049 | -42.92455 | 2024-10-03 04:53:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 42429277-a20b-38d7-93e3-71a41688fe67 | -18.83023 | -42.92454 | 2024-10-03 04:53:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 962539d3-661e-32e9-ae84-1e35fcec63f8 | -18.32776 | -43.06119 | 2024-10-03 04:53:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a3bff4db-b4b9-3d45-a01e-f2c7b9fc81d3 | -18.2639 | -43.0325 | 2024-10-03 04:53:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f1e6907d-d144-3f31-8feb-e64ac9e3308e | -18.26335 | -43.0383 | 2024-10-03 04:53:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c8988292-dd6a-3631-aaf0-618145187e45 | -20.85279 | -42.23169 | 2024-10-03 04:53:00 | NPP-375D | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 792fee75-15cc-3d9d-97d2-7332ad08b280 | -20.80617 | -42.29764 | 2024-10-03 04:53:00 | NPP-375D | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 10f217dd-6508-367d-a47c-cb924fbac62a | -20.21488 | -42.47031 | 2024-10-03 04:53:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 897f050e-3a7f-3692-9873-67f2be929d2c | -20.21437 | -42.47635 | 2024-10-03 04:53:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 02fb727a-f15e-34c4-a9f7-4f6c0ed06b3b | -20.21107 | -42.46892 | 2024-10-03 04:53:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 997122a7-f810-3db6-b1dd-3cc11079e418 | -20.2106 | -42.47497 | 2024-10-03 04:53:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 3846fa72-d899-353d-91e4-e5833c3548f8 | -20.21014 | -42.48081 | 2024-10-03 04:53:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f89c481f-7375-365a-b535-eeb80ce9d271 | -20.20816 | -42.46954 | 2024-10-03 04:53:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 16091ed9-c788-318c-b5d3-7439661b34fb | -20.20767 | -42.47533 | 2024-10-03 04:53:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c1645132-441e-34fe-9279-afff635c4b70 | -20.20718 | -42.48112 | 2024-10-03 04:53:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 575614aa-6a03-356e-be76-9af8d348a8e1 | -20.2067 | -42.4869 | 2024-10-03 04:53:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 218ad54a-53a7-3492-b24d-ffa7e82813e4 | -20.203 | -42.48552 | 2024-10-03 04:53:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f6562a93-112f-3e1b-bea7-a704668dfb0d | -19.89197 | -42.10924 | 2024-10-03 04:53:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f76fddf9-cb6f-3a72-b845-0cac87f51fc3 | -19.8855 | -42.10403 | 2024-10-03 04:53:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| 355426d9-b180-39a0-97a6-3aa572889402 | -19.88509 | -42.10902 | 2024-10-03 04:53:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| 04792ec7-a030-3151-9191-dc8ef2f7b23e | -19.88469 | -42.11388 | 2024-10-03 04:53:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| b5dc2edc-f9b5-3ac0-86fc-10568d712e06 | -19.85682 | -42.37048 | 2024-10-03 04:53:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5bd5ceab-64cf-36a5-8e73-47bd979f8d80 | -19.85642 | -42.37537 | 2024-10-03 04:53:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5c70e09b-f641-36db-9791-57cdd2b706ff | -19.6835 | -42.03135 | 2024-10-03 04:53:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ea5e3a24-00bf-3d8d-b4f6-4451ec7b9380 | -19.68296 | -42.03799 | 2024-10-03 04:53:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 30aa3fd7-6c3e-3f0b-a958-4eb5dfedc867 | -19.50649 | -42.88695 | 2024-10-03 04:53:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 54914d19-c214-3df7-aa57-34fcf37fdd66 | -19.50093 | -42.87514 | 2024-10-03 04:53:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f60d6ab6-12c9-3a4c-928d-8c9b7042ff8d | -19.5003 | -42.88243 | 2024-10-03 04:53:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 18364813-863b-3303-8807-1e2bfbeeb501 | -19.49986 | -42.8875 | 2024-10-03 04:53:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2209eb6b-d806-3855-8438-26c6e0d1abfc | -19.44583 | -43.06059 | 2024-10-03 04:53:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 9b9a7a85-52d5-3801-905a-5120083e0fc6 | -19.4457 | -43.06026 | 2024-10-03 04:53:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7a5d1135-7395-336a-9462-84b3374fa86b | -19.44537 | -43.06558 | 2024-10-03 04:53:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b8f16404-19a1-3a76-bb08-a744817afeb5 | -19.44526 | -43.06532 | 2024-10-03 04:53:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 41947796-9f47-36ea-9f05-e04e7ab989c2 | -20.48001 | -43.18081 | 2024-10-03 04:53:00 | NPP-375D | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 704b3484-4999-35d4-8a62-fc5a6c40c299 | -20.4742 | -43.1778 | 2024-10-03 04:53:00 | NPP-375D | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dafad696-130c-3945-a646-55f67c0ed7c3 | -20.47372 | -43.18324 | 2024-10-03 04:53:00 | NPP-375D | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3a219b1a-d5b9-3443-b8f9-2ab3638548fd | -20.47356 | -43.17979 | 2024-10-03 04:53:00 | NPP-375D | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4804ee10-d5e5-3214-8542-cf13b80f4208 | -20.28153 | -43.5158 | 2024-10-03 04:53:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 878ea44e-930b-378f-a245-d089a9e9ba16 | -20.28089 | -43.52315 | 2024-10-03 04:53:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2f9c739f-85ad-3e18-8558-0286c7c73d8b | -20.07213 | -43.2168 | 2024-10-03 04:53:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dac3b959-e127-3659-aad8-ee5c5cf85c83 | -20.06569 | -43.21615 | 2024-10-03 04:53:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aa57ea25-51f6-3fc8-a68e-942b5aab6e87 | -22.28935 | -42.47919 | 2024-10-03 04:53:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dc7f0b1d-381e-383a-bb65-c7facc7a0f0d | -22.28887 | -42.48617 | 2024-10-03 04:53:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 77717aca-78ca-36b9-b2b9-9f99ddc6d2f8 | -22.28846 | -42.48027 | 2024-10-03 04:53:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 98b36004-df08-35da-84af-478fb8aef353 | -22.28794 | -42.48719 | 2024-10-03 04:53:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| eae4c5e7-9426-35a0-958c-5ecabfddef65 | -22.28255 | -42.47771 | 2024-10-03 04:53:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4eb31937-2218-3d03-90a9-59738e93b593 | -22.16646 | -42.54445 | 2024-10-03 04:53:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 875c76f0-46c0-3ce9-a06e-9f2678ffe061 | -22.16011 | -42.53748 | 2024-10-03 04:53:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2db25704-b004-343f-936e-816a0be30a85 | -22.15962 | -42.544 | 2024-10-03 04:53:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 174d4378-a428-309c-988d-1bb4f1723694 | -22.15289 | -42.54222 | 2024-10-03 04:53:00 | NPP-375D | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b7460e5e-36b4-32b3-8ccc-ecad0b174c90 | -21.79023 | -42.48344 | 2024-10-03 04:53:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7fb88763-8140-3d64-ad79-f717ccee6428 | -21.7897 | -42.49077 | 2024-10-03 04:53:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 802bd561-4848-3b8b-a4e4-8f629177f6a7 | -21.78965 | -42.48473 | 2024-10-03 04:53:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9216246c-0a1d-305d-ab8e-8351c5502550 | -21.78908 | -42.49203 | 2024-10-03 04:53:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f410ca43-ca44-37f9-ad3b-620ddf98e200 | -21.00314 | -42.60658 | 2024-10-03 04:53:00 | NPP-375D | SÃO SEBASTIÃO DA VARGEM ALEGRE | MINAS GERAIS | Brasil | 3164431 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9675b31e-5e32-3945-9e71-809a627bd3bc | -20.99686 | -42.6004 | 2024-10-03 04:53:00 | NPP-375D | SÃO SEBASTIÃO DA VARGEM ALEGRE | MINAS GERAIS | Brasil | 3164431 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 18e94a47-cfa7-3fa1-a041-dfad7f76b377 | -22.05617 | -42.97115 | 2024-10-03 04:53:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3571b478-69c4-3531-b960-821fb0427a53 | -16.35133 | -43.69517 | 2024-10-03 04:53:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d664c2b-01d5-3fac-ae04-d32732c3219f | -17.2556 | -43.18116 | 2024-10-03 04:53:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1fb74c1-3de6-3733-b08b-ead4e7f63095 | -19.2742 | -43.76486 | 2024-10-03 04:53:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4527fb16-eba5-3734-8dc2-7748ee97fb46 | -19.27376 | -43.76943 | 2024-10-03 04:53:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c7b9360e-7e72-3b13-9a87-259fa23036d4 | -19.27343 | -43.76557 | 2024-10-03 04:53:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 00cee7d3-e440-3043-a068-dadbae2dd03f | -19.27328 | -43.77433 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ade8854b-b804-3d04-8a4d-4824ff6e51f6 | -19.27302 | -43.77018 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 77eae070-64b7-378a-a41c-7349c2ee1c00 | -19.27279 | -43.77942 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README143.md)
