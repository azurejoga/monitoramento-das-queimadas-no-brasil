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
| 5ddc9751-700f-3f6f-99a6-5f0ba82048fa | -23.28747 | -45.61181 | 2024-10-01 04:17:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c3c8ed89-b754-3836-a2e7-851d89dbf672 | -23.07936 | -45.40336 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 9824cb29-89f7-3790-ae36-df8f3f1477a4 | -23.07713 | -45.39508 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 07fef80b-132b-3ac8-801e-f017ffbcc8d7 | -23.07655 | -45.39897 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 1ce81c14-8685-33ab-a6d1-c59e494411cd | -23.07598 | -45.40285 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| ee7fc9ae-1969-3b2e-ac12-94f5836d0f39 | -23.07374 | -45.39459 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 23a4b3ac-d5a2-3b1b-a8ab-9951f27bb828 | -23.07259 | -45.40232 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 106d39b4-479e-3318-adbf-4af7d7742a4e | -23.07203 | -45.40615 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 37571e8f-6366-3794-9be8-0d60af3ad339 | -23.07035 | -45.39407 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 67e6ed74-4965-3443-bd27-7c46352404d4 | -23.06978 | -45.39792 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1a52aca6-c8f2-3a45-b732-00f919fbaacb | -23.06922 | -45.40173 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 97daa1d4-5612-3175-b178-3e0eaa68fb92 | -23.06866 | -45.40554 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| b7b02d51-8c3f-3185-99b3-ef354576d74e | -23.06809 | -45.40935 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7301b853-b289-3605-b194-542be9b8b445 | -23.06642 | -45.39728 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 83afa178-2064-3cbc-be7e-076adbfdfe4e | -23.0653 | -45.40487 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| d4a47c12-6899-3362-8449-d53ea4ab28c0 | -23.06473 | -45.4087 | 2024-10-01 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e6221a2c-66f9-352a-8ed2-c9d80cf98d68 | -23.06387 | -45.70412 | 2024-10-01 04:17:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7671f60c-13e5-3db4-8ef9-3d0057164971 | -22.92331 | -45.49215 | 2024-10-01 04:17:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 134dd8fc-67a2-3d5e-86c2-6586281ecf55 | -22.91575 | -45.37961 | 2024-10-01 04:17:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9a2b3a4f-d174-3447-a6d1-18aa2e73fa76 | -22.87744 | -45.1856 | 2024-10-01 04:17:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c193acb3-a43b-354f-803e-3da35629331a | -22.87405 | -45.18503 | 2024-10-01 04:17:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 51f674c4-5708-33a7-aad0-9dfa12bd5027 | -19.08424 | -46.25287 | 2024-10-01 04:17:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 218ee4e3-4dde-3b23-a8b1-6937c76e2ca1 | -19.08093 | -46.25229 | 2024-10-01 04:17:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e5518dd-4a96-3879-9886-bedaf39e4451 | -18.97811 | -45.08144 | 2024-10-01 04:17:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1aa2366d-567f-365c-806f-5a4a01e33ab6 | -18.96685 | -45.46297 | 2024-10-01 04:17:00 | NOAA-20 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 172e6c4f-143b-3f21-8fed-64bf9da23a13 | -18.80883 | -45.80195 | 2024-10-01 04:17:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7b080247-9b18-38ec-a217-4ed96f14c7c1 | -18.79771 | -44.88593 | 2024-10-01 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 424e3b07-ef8b-3091-bcf7-f2a3ebcb6b42 | -20.59752 | -46.24026 | 2024-10-01 04:17:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d3a5f20-6fbd-31d7-a055-775026468698 | -20.59694 | -46.24393 | 2024-10-01 04:17:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25fc0b77-2048-3f6d-8856-b2aeaa758335 | -20.54591 | -46.28781 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| edacb064-908f-3b27-a2ee-0d7e978b1013 | -20.5382 | -46.29401 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 49829beb-6d30-3e1b-8b49-273b1bd6396c | -20.53547 | -46.28976 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ab5aac08-c4b2-397c-9874-207275337ce7 | -20.53489 | -46.29343 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8f3944f7-f416-30fb-b927-133486fb4609 | -20.53215 | -46.28917 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 455fc59e-efb6-3f90-a54c-28ca7c08b938 | -20.53158 | -46.29284 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5fe12db-366d-34bc-ac97-b74d1710749c | -20.52826 | -46.29226 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e38001a-216f-365b-97ef-85ea974ca73f | -20.52711 | -46.29961 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ecb47846-52fd-32fa-8cfb-c8ef07d9be2c | -20.5238 | -46.29902 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab1beeb8-9439-321b-9b39-eed6c316f177 | -20.52049 | -46.29843 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea30543e-9078-3103-aaa2-79a38955702b | -20.51991 | -46.3021 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4a47631-ad03-3193-aa96-d3322478db25 | -20.5166 | -46.30152 | 2024-10-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b953d3a-daa0-3ca7-80cb-e505043073e8 | -20.95815 | -45.50841 | 2024-10-01 04:17:00 | NOAA-20 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45d9db54-05ea-3f9c-adf0-5011cd041782 | -20.31193 | -45.5874 | 2024-10-01 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe98b7db-7c82-304f-a70a-bfa0d69e95da | -20.30918 | -45.58312 | 2024-10-01 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbfc1f8b-d9a8-3e25-b2a3-973e345a25dc | -20.09268 | -45.26559 | 2024-10-01 04:17:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9b1647ef-2a09-3f26-aa3c-944f868c59cf | -20.00039 | -45.06652 | 2024-10-01 04:17:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b42c15c-e5e1-3af0-87ee-3bc1ca14ec21 | -19.72007 | -45.50654 | 2024-10-01 04:17:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29d50e6d-7abf-3726-9b8e-69d344bc61b7 | -19.70152 | -45.60514 | 2024-10-01 04:17:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58a81978-cd3b-312c-89bd-4e4f562f0fd3 | -20.81423 | -45.29731 | 2024-10-01 04:17:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b9cb93dd-0f84-3121-9acf-3d7b40b5d23c | -22.38148 | -45.80157 | 2024-10-01 04:17:00 | NOAA-20 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9f8db80f-ba69-3f73-a2f8-b249c8eaa0f4 | -22.37928 | -45.79345 | 2024-10-01 04:17:00 | NOAA-20 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1eef3dff-b6fa-3d05-9398-ae2fba7153ec | -22.3787 | -45.79726 | 2024-10-01 04:17:00 | NOAA-20 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| afe3bb40-3d65-347e-9836-419782d531c5 | -22.37814 | -45.80098 | 2024-10-01 04:17:00 | NOAA-20 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8173bd34-f15c-3771-89f9-001e09c5dcc7 | -22.12343 | -45.91973 | 2024-10-01 04:17:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 79bae7b8-e6fb-3df0-b969-4e2ba1a1a80f | -21.52607 | -45.87569 | 2024-10-01 04:17:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4305b2d3-1532-3ec9-8052-836a1cb4bda3 | -21.5255 | -45.87941 | 2024-10-01 04:17:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2985348d-bfa8-3a1b-a5b3-0eb628febe42 | -21.52274 | -45.8751 | 2024-10-01 04:17:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bd4cb5db-06df-3a8a-be61-9d3b8b137361 | -21.33471 | -46.432 | 2024-10-01 04:17:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b921cce9-7b39-366f-989d-662e0e5e31f4 | -21.33413 | -46.43569 | 2024-10-01 04:17:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 548c43a1-d034-3b3a-baff-f5d15f6fa2bd | -21.3314 | -46.4314 | 2024-10-01 04:17:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 038d9456-adb4-3b5b-9d1d-1a1c7e4ddba9 | -21.31154 | -46.64415 | 2024-10-01 04:17:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| fb413980-1743-37a8-9ed4-3fd4db0d4226 | -21.31096 | -46.64785 | 2024-10-01 04:17:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| c096292e-b468-3549-8bee-0a41b2406fc6 | -21.31038 | -46.65155 | 2024-10-01 04:17:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c81d0be9-75c8-38b2-a33c-8c62db19b171 | -21.30824 | -46.64356 | 2024-10-01 04:17:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| dc30fdc3-1daa-3fb5-9932-a1cd5317ae4a | -22.96125 | -45.96197 | 2024-10-01 04:17:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 140daa3b-1fe0-36a9-ab03-18b2fa87ddcc | -22.95791 | -45.96143 | 2024-10-01 04:17:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 116e44ab-d119-334e-b678-77ce58deb212 | -22.95733 | -45.96528 | 2024-10-01 04:17:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2d835653-08f5-3eb6-8e00-009ac8a4da96 | -22.67725 | -47.05133 | 2024-10-01 04:17:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 8fd310a9-c257-3749-a493-1a53d4c45ba6 | -22.67394 | -47.05072 | 2024-10-01 04:17:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e1d72aa-23d9-3468-950e-ba1e1a8835df | -22.67122 | -47.04637 | 2024-10-01 04:17:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c80c203-8e8f-3a9d-ad7c-42c128173342 | -23.70329 | -46.47741 | 2024-10-01 04:17:00 | NOAA-20 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3d04824a-db77-3a73-99c0-9ea0a369ede2 | -23.48496 | -47.22696 | 2024-10-01 04:17:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7d3043ca-e942-3049-b555-5eb138296e4e | -23.48358 | -47.14948 | 2024-10-01 04:17:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f8d69009-ccb0-3bd1-acca-bc2311be2813 | -23.40627 | -46.55784 | 2024-10-01 04:17:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd9dedee-34b0-35b5-8983-60df2f980359 | -23.36236 | -46.99355 | 2024-10-01 04:17:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eb3ab164-2dce-328c-afda-67c8b49e0b28 | -23.33883 | -46.77336 | 2024-10-01 04:17:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 90348443-8271-38bc-a7c0-9f662a745b47 | -23.27587 | -46.6542 | 2024-10-01 04:17:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a1ca5cd1-cd40-3ed3-a575-8f5e493934f8 | -23.27256 | -46.65359 | 2024-10-01 04:17:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b0707f24-f969-360c-ba45-7e75894c9350 | -23.20107 | -46.41357 | 2024-10-01 04:17:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c5a8efa-31ba-3405-a0a9-c8c6117a03cc | -23.15664 | -46.3285 | 2024-10-01 04:17:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4c9aac7f-3d38-3d2f-b09e-71af38a01fd6 | -23.1201 | -46.4109 | 2024-10-01 04:17:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 078d69ed-7197-3fd3-b31d-d46271788c6b | -23.11952 | -46.41465 | 2024-10-01 04:17:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c63863c7-46a0-3d19-99ca-c8176b4bc152 | -23.10282 | -46.58899 | 2024-10-01 04:17:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b3e40c66-281f-3c4f-953c-37fab1c20cdd | -23.10224 | -46.59274 | 2024-10-01 04:17:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 89f4ad53-baf2-3626-9227-12751efa3927 | -23.10166 | -46.59649 | 2024-10-01 04:17:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d97fdfa-770f-3a1c-ad64-790782532782 | -23.0986 | -46.39549 | 2024-10-01 04:17:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| af22114a-ea7e-3625-af5a-7f7c6550ad78 | -23.09802 | -46.39922 | 2024-10-01 04:17:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fc1c6d31-be1f-3d29-9425-6d9d633ddced | -23.09544 | -46.61463 | 2024-10-01 04:17:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1d61b401-dc01-37ff-ba02-1e8aeaf1ef80 | -23.09528 | -46.39491 | 2024-10-01 04:17:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2c8616e9-d69f-3224-82bc-413a0ddf6472 | -23.0947 | -46.39864 | 2024-10-01 04:17:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9881a833-e9ad-350e-825b-458ffc338ff0 | -23.09311 | -46.38679 | 2024-10-01 04:17:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 692fd6e1-0e24-34d8-8c02-6812c6e2034a | -23.06336 | -46.18475 | 2024-10-01 04:17:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 16069985-3e6b-3cae-9f4c-17d5f7c43866 | -22.78195 | -46.8166 | 2024-10-01 04:17:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 981b8453-2504-3f99-b215-332e4b3b2970 | -22.77864 | -46.81599 | 2024-10-01 04:17:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| bfe0daf1-cfe8-33df-9a91-55ec5db3f40f | -22.76929 | -46.81044 | 2024-10-01 04:17:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 492e49ff-3a5c-36b8-ad9f-f64fe8c8103d | -22.73073 | -47.03369 | 2024-10-01 04:17:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9b191795-2b46-3a0c-81df-0e4e56e134bd | -22.72536 | -46.68035 | 2024-10-01 04:17:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ec407480-a2f5-3d53-8171-fb54199cd042 | -22.72478 | -46.68408 | 2024-10-01 04:17:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b066700d-8cac-3c61-b502-bfc52b2b8fae | -22.72263 | -46.67603 | 2024-10-01 04:17:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 4792dd7a-4893-3fc4-bdba-2ac71ba81d3f | -22.72205 | -46.67976 | 2024-10-01 04:17:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |


[Clique aqui para ver as próximas entradas](README92.md)
