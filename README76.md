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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 288a3aa2-00b6-3a55-ae04-a99d41f1f0dd | -21.30723 | -49.22215 | 2024-09-30 12:36:00 | TERRA_M-T | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 216.0 |
| aebb411e-29ae-39ec-b1a9-b6aef5791137 | -21.3056 | -49.23261 | 2024-09-30 12:36:00 | TERRA_M-T | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.4 |
| d7fcbd9e-f522-37c9-902a-4b61e37671cb | -22.64411 | -49.46722 | 2024-09-30 12:36:00 | TERRA_M-T | ESPÍRITO SANTO DO TURVO | SÃO PAULO | Brasil | 3515194 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7dfa7592-4d99-34ec-8038-40c99e1aeaea | -22.64245 | -49.47781 | 2024-09-30 12:36:00 | TERRA_M-T | ESPÍRITO SANTO DO TURVO | SÃO PAULO | Brasil | 3515194 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| faefd849-4249-3c93-bc50-0c90fe541b0a | -22.63649 | -49.45506 | 2024-09-30 12:36:00 | TERRA_M-T | ESPÍRITO SANTO DO TURVO | SÃO PAULO | Brasil | 3515194 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ea4310f5-e13d-38b7-a18a-9ac4c5cac748 | -22.63484 | -49.46554 | 2024-09-30 12:36:00 | TERRA_M-T | ESPÍRITO SANTO DO TURVO | SÃO PAULO | Brasil | 3515194 | 35 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 7db5edf5-eb68-3868-882e-529009e26cc1 | -22.63317 | -49.47612 | 2024-09-30 12:36:00 | TERRA_M-T | ESPÍRITO SANTO DO TURVO | SÃO PAULO | Brasil | 3515194 | 35 | 33 | nan | nan | nan | Cerrado | 33.3 |
| eea483f5-abe8-39f2-9511-ec8d7269bebc | -22.62557 | -49.46385 | 2024-09-30 12:36:00 | TERRA_M-T | ESPÍRITO SANTO DO TURVO | SÃO PAULO | Brasil | 3515194 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 647368b3-9e19-317a-aaa7-fa8d5c9becd3 | -25.89715 | -49.85975 | 2024-09-30 12:36:00 | TERRA_M-T | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| e83c6d89-24e6-3472-b909-2dc08738da75 | -20.53026 | -50.42192 | 2024-09-30 12:36:00 | TERRA_M-T | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 3e965b44-f95f-37a7-80cb-5c959c7911df | -20.52229 | -50.40773 | 2024-09-30 12:36:00 | TERRA_M-T | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.2 |
| 8b0609fa-6d8f-3ca1-8d36-2046ca21a9ec | -20.52025 | -50.41999 | 2024-09-30 12:36:00 | TERRA_M-T | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 181.1 |
| 3dfb5c99-214d-3c9e-8d0c-6591beb14247 | -20.51945 | -51.29667 | 2024-09-30 12:36:00 | TERRA_M-T | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 144.5 |
| 217393ae-26ff-3485-ae13-c38178d40604 | -20.5171 | -51.31071 | 2024-09-30 12:36:00 | TERRA_M-T | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| c04f95ff-4571-3a35-90fa-62f5d8fc1739 | -23.1106 | -50.40794 | 2024-09-30 12:36:00 | TERRA_M-T | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 036898a2-c74b-33b5-a645-ae182fc9769b | -23.10871 | -50.41945 | 2024-09-30 12:36:00 | TERRA_M-T | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 8cfabfed-8c49-332c-baa5-ba3e5771b1ae | -25.80296 | -51.64172 | 2024-09-30 12:36:00 | TERRA_M-T | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| efb1d99f-314f-36d5-aaf0-be8897f8bcfe | -23.28007 | -52.26094 | 2024-09-30 12:36:00 | TERRA_M-T | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 37.0 |
| 94824e7b-76df-383c-8b70-21ded868b187 | -23.22406 | -52.38744 | 2024-09-30 12:36:00 | TERRA_M-T | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 49.3 |
| c9850a7c-ec42-3c3b-8bd2-b006651325c5 | -23.22283 | -52.38103 | 2024-09-30 12:36:00 | TERRA_M-T | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| e278b6a5-202a-387c-965c-324d44a41afc | -23.22023 | -52.39626 | 2024-09-30 12:36:00 | TERRA_M-T | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.2 |
| fb7f833f-1ba0-370d-935e-0ebdb0c6bf7d | -21.65888 | -54.84266 | 2024-09-30 12:36:00 | TERRA_M-T | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 51.6 |
| b359f9f5-3245-33bd-9e7d-9b0a9ae24340 | -21.65438 | -54.86669 | 2024-09-30 12:36:00 | TERRA_M-T | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 62988421-4ea7-3b89-99e2-2f0545322a64 | -21.65264 | -54.84745 | 2024-09-30 12:36:00 | TERRA_M-T | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 8e7ece67-ac5b-373c-8ec9-9d9325b04fa5 | -28.51306 | -50.66212 | 2024-09-30 12:38:00 | TERRA_M-T | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 2e6ffba6-67f1-33a3-abf5-5c6fdc7c64f8 | -28.51135 | -50.67287 | 2024-09-30 12:38:00 | TERRA_M-T | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c27a3de4-f095-3170-993f-6867d5d3a58e | -27.16977 | -51.76517 | 2024-09-30 12:38:00 | TERRA_M-T | JABORÁ | SANTA CATARINA | Brasil | 4208609 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| b09e15d7-5f13-33ba-aff2-b902e4e6cf2b | -27.16771 | -51.77747 | 2024-09-30 12:38:00 | TERRA_M-T | JABORÁ | SANTA CATARINA | Brasil | 4208609 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 246f50aa-dc76-32ae-94ca-dfd8f5bc7300 | -19.68 | -48.82 | 2024-09-30 13:03:32 | MSG-03 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 424ad72a-3e72-3040-aac2-d40b3209280d | -19.67 | -48.76 | 2024-09-30 13:03:32 | MSG-03 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eba6d64d-6910-3115-a3dc-99712d24b58d | -18.88 | -49.17 | 2024-09-30 13:03:37 | MSG-03 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 664b144d-9243-3e01-b5e5-a24d005d3a24 | -12.07 | -50.05 | 2024-09-30 13:04:17 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7aff04d5-18cd-3980-b75a-2e6271629cb3 | -12.07 | -49.99 | 2024-09-30 13:04:17 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b340a21-2ec4-3255-afda-1a8c1562f0f4 | -12.1 | -50.06 | 2024-09-30 13:04:17 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9aaf2933-ed67-3eef-84e4-37d4620f4b71 | -10.71 | -45.92 | 2024-09-30 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a865192-bc00-3ff1-b4ec-41a52ed22a54 | -10.71 | -45.97 | 2024-09-30 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


