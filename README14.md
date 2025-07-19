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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30b4f532-cf59-38e2-a75c-f0a5c0c675ed | -14.84306 | -49.12699 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f71f8918-a5da-3bb4-b131-8b9cb8a192c5 | -11.82532 | -48.21371 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7cde1a41-804e-314f-bf65-053b1c243191 | -16.44716 | -49.96844 | 2025-07-19 04:10:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f982f83-2335-33a1-865a-8bb1c150414f | -14.70379 | -45.064 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fc7af54-4465-3ba0-a560-fd54f71cfdae | -15.99499 | -49.8196 | 2025-07-19 04:10:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1465731a-a551-3a57-a0cb-e443e2684fe1 | -11.96257 | -47.01503 | 2025-07-19 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5af5d1d9-5616-3773-9a66-39cea209dcb6 | -14.19821 | -45.33527 | 2025-07-19 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 225713e9-7439-3cb5-9724-1f8c9ecca9a9 | -14.1976 | -45.33905 | 2025-07-19 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ce49e81-b4df-31f0-ab26-9f3817708768 | -12.99124 | -46.92094 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e8b105f-b084-3016-8b1e-89c19222c107 | -14.47972 | -46.35878 | 2025-07-19 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32ce80ab-b9fa-351f-abc8-0fc70bf040d6 | -17.65125 | -44.20987 | 2025-07-19 04:10:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 867101af-f309-3619-bd28-f8b802497ece | -12.90237 | -48.92065 | 2025-07-19 04:10:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70ae8e27-2022-330e-9604-75812b2b5198 | -12.5716 | -44.75535 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da6437d8-9e8b-3e85-86d3-db1a611f15b2 | -12.09269 | -44.73679 | 2025-07-19 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5f4e5f4-3768-3d72-9edc-21e294a9d856 | -11.47603 | -47.32627 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca7e4593-ef45-37c9-b902-03cab503b692 | -12.0933 | -44.73304 | 2025-07-19 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 346accc3-64f2-3009-91e7-72519474bb30 | -11.96604 | -47.01833 | 2025-07-19 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 118460b9-81c1-3400-9565-062b839cafc8 | -10.98719 | -49.39266 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17c3ca14-a654-32c8-9296-d6c1a928d1f8 | -12.03893 | -48.75734 | 2025-07-19 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37e05642-2209-3c6d-b9d3-240bd275dc39 | -14.71052 | -45.06516 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d533167-785b-3889-9cc0-b3ed2bfd52a6 | -13.60752 | -45.63779 | 2025-07-19 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6c1e5b6-0fc6-31b8-9d89-d336380591c2 | -11.96522 | -47.023 | 2025-07-19 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52c6f775-eaf8-3d01-99bc-f4d294d05461 | -14.70102 | -45.05976 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cefeb06-b552-34e8-8822-fe781354be6f | -12.57499 | -44.75591 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 262d5f62-961d-3965-8a4e-cf274e7b656b | -12.43119 | -45.3748 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3925c3e-ea11-3cce-9dd5-4ae714dee6d4 | -11.72854 | -48.19297 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| bb724f41-4d3c-37db-a539-a06063619257 | -11.73261 | -48.19367 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 67777388-9982-3241-8762-526bbffd1759 | -14.72062 | -45.0669 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b7d40df-026c-359e-bdbf-a7e619244ac1 | -12.36245 | -50.3401 | 2025-07-19 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e98bb9d1-ed70-372a-83ab-3bc2b7054034 | -18.05221 | -47.94455 | 2025-07-19 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6900e9b-c68c-3524-9bd9-2197d4018446 | -11.9689 | -45.47106 | 2025-07-19 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 747a381d-68fd-3e05-b286-ce2b08d62079 | -14.70439 | -45.06033 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26cef0ff-3b5e-3aec-8965-d1f6aa3b534f | -16.04415 | -43.72393 | 2025-07-19 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c473d85b-d69f-3b36-a87f-c050c69564a0 | -12.0899 | -44.73248 | 2025-07-19 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c1a7902-1c7c-32ce-aa5b-1a1fdb9b751d | -16.22583 | -47.95529 | 2025-07-19 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82f54cfd-f97b-33b7-b7c5-93efd832435e | -12.42836 | -45.37033 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfded7af-8bd1-344f-ac3c-0c2969096b8a | -10.8067 | -46.76763 | 2025-07-19 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a19169f6-e12f-366e-9680-98428872afd5 | -12.09609 | -44.73734 | 2025-07-19 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b7b53b4-f6e7-378b-8873-5b39306edf79 | -11.56585 | -47.08266 | 2025-07-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e8f9e31-9abc-3213-ba11-38014fcce051 | -12.71701 | -47.79573 | 2025-07-19 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 81bdbd47-f4b0-3e17-9b47-80b15f87cac9 | -12.13915 | -50.24121 | 2025-07-19 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bd66451-5ad7-37de-96b1-e1aa4b42d896 | -11.56042 | -47.09144 | 2025-07-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f597b10b-b811-35c3-b851-78e53684c9fd | -10.75313 | -52.76311 | 2025-07-19 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abff709e-a9dc-3ddb-9cd8-58d3e79254a0 | -12.429 | -45.36646 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f572ec86-3a30-3167-aa3c-c8d8a0e31719 | -14.201 | -45.33963 | 2025-07-19 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17d8faad-0032-3acd-b240-23b682a46543 | -11.47516 | -47.3236 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07ea6e0b-8b4a-360f-9370-344d5d5da3f9 | -14.83556 | -49.12163 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0948f9e4-d8f2-3130-aa0a-0972dc6b2bf4 | -11.48075 | -47.32209 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0d655252-240b-3769-aaa3-c0b67f1d70d2 | -12.97017 | -46.91864 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88cd7b99-c9af-3b4a-a8fb-8ee07939798d | -14.69557 | -45.06233 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5135f7ae-7220-301a-b15a-53d432ebfb54 | -12.37348 | -50.332 | 2025-07-19 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 807d65ed-ad25-3472-85cc-9056f21dbf10 | -10.37564 | -49.91519 | 2025-07-19 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db238bfe-ef07-3dd8-b824-1188a4602ae7 | -14.6986 | -45.07449 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ac3c79c-8154-3070-84fa-01449617ceb0 | -14.69981 | -45.06713 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 089b364b-d922-3a37-aba0-cd78a5b270fb | -12.71678 | -47.79805 | 2025-07-19 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8bef102f-0403-3519-b374-026bc32620aa | -15.72313 | -46.86649 | 2025-07-19 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17bc3fdc-0410-3fd9-a392-fd9854add344 | -14.75405 | -48.26363 | 2025-07-19 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33fb29b5-72b3-3b7d-855f-7dddafd659fd | -10.8152 | -49.29136 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25384069-20d1-364b-9870-75378a8774fb | -15.70134 | -48.12748 | 2025-07-19 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64d528f2-d3ca-39ae-ac6f-ebccab83a408 | -11.48762 | -47.32835 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 54461bc1-6ece-3705-bb66-f2df949f9a2f | -18.47292 | -39.97754 | 2025-07-19 04:10:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fbd578f8-533b-3ba6-b77e-664ee4fafcc8 | -14.48325 | -46.35939 | 2025-07-19 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e00d9aab-5350-38c5-b69c-0494babfc663 | -11.48376 | -47.32765 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e9c42d10-a1c2-3ba7-acbb-c95d0787c8bd | -14.70138 | -45.07872 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81725596-779c-341b-a23c-2536aa0be06a | -11.57184 | -47.09343 | 2025-07-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 73e5c7fe-7ac9-324a-a06f-805cceb60fb3 | -10.4188 | -48.61378 | 2025-07-19 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ac47e77-b421-38fd-afbb-a71915949555 | -17.91854 | -45.56323 | 2025-07-19 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9963ca42-4ae9-3621-9362-cd1b6d8235bd | -14.7501 | -48.26328 | 2025-07-19 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb33fc9e-b07d-317f-b983-9e10c026ea40 | -11.56342 | -47.09681 | 2025-07-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e54d959-9c4e-3975-8341-9cb56603b72f | -17.55412 | -44.24518 | 2025-07-19 04:10:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92c77f7a-4972-38e4-bdb2-1a6314f4f0fb | -15.89791 | -43.46104 | 2025-07-19 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32cb50d3-eec6-3114-9372-0917948e5bd6 | -10.42308 | -48.6145 | 2025-07-19 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08ef5535-b602-3c94-bf08-1347bf314af3 | -11.96556 | -47.02038 | 2025-07-19 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ed83e19-0044-391e-961a-8492200a6dd5 | -11.3721 | -54.3431 | 2025-07-19 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aad502e4-eefa-3839-a11e-af416910688c | -15.50272 | -47.83643 | 2025-07-19 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 798b67bd-3f70-3dde-9a70-a3e05a14e08a | -12.36334 | -50.33517 | 2025-07-19 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8778174-a3a0-303c-8748-ddfd55353411 | -12.99486 | -46.94414 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fe501c35-9274-3693-a72c-19b294f31b28 | -11.55661 | -47.0908 | 2025-07-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 199e40f6-32f6-3dd4-8b90-1cb7a8e7058a | -14.83897 | -49.12624 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b6315a5-2759-30d6-8f57-10a821a1e5e9 | -12.42426 | -45.37363 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a31200cd-acef-3418-8c0a-80f2c961a1f9 | -11.73186 | -48.52646 | 2025-07-19 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61b8f970-88cc-3d79-8e8e-6f671a087e30 | -15.7906 | -43.05302 | 2025-07-19 04:10:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d72c93b7-0a6e-307d-a6ac-b3758895a84d | -12.99113 | -46.94368 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| be5ea2c6-629e-3f43-b2bc-2238ff1ae1f9 | -10.72926 | -46.78823 | 2025-07-19 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d87d470b-ef29-328e-b1a2-e1638afc8844 | -11.56423 | -47.09209 | 2025-07-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85e2e9ee-a125-36ab-b7f1-4a5dc80ef514 | -11.83004 | -48.21072 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4098954-0c99-3c1d-8d15-8d605098c9b8 | -16.89783 | -52.6801 | 2025-07-19 04:10:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f834ecf-a3a2-37d8-b117-1732a80623f8 | -11.48372 | -47.32009 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fce0b25b-bc65-33c8-a939-9351029d057e | -14.69921 | -45.07082 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f44962a7-972b-3443-8fc5-25c72c4a2c11 | -18.21644 | -47.88701 | 2025-07-19 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6b8cec0-ffc9-3b65-8a78-8a307a5fcfef | -14.20502 | -45.33644 | 2025-07-19 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfe39668-3290-33ea-a467-cbbf53beca8a | -11.72981 | -48.1857 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| c8eb021d-30ca-312f-aa69-ed864d94008e | -11.46272 | -48.15635 | 2025-07-19 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78180f42-ad25-3c6b-822d-ac8d4ffb6f54 | -13.60688 | -45.64171 | 2025-07-19 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79b4d072-ca7c-3bbc-bcab-e616dcf72bb7 | -14.71389 | -45.06573 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36855242-8724-3c7e-8ced-7905f24cc904 | -14.69765 | -45.05919 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42f7f05b-6848-3f8d-943c-aa5d1d3725a6 | -10.68147 | -49.67919 | 2025-07-19 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e353f51-02af-36c8-8d81-9db4fd9b69b6 | -12.4208 | -45.37304 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dd557b8-56dd-3884-a1a4-a494059d8a5b | -12.99564 | -46.9396 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36c8924e-9b72-3ad5-ad56-1e324318ec86 | -10.68232 | -49.67448 | 2025-07-19 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README15.md)
