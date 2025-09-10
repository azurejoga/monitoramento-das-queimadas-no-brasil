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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 765e0a0b-893a-382b-8de1-5116a07420f1 | -12.6078 | -56.97117 | 2025-09-10 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb333dc6-ada5-37a1-8628-0d4399147cf1 | -15.51366 | -48.38233 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 389c3c1e-e679-3dad-a2c7-a46161c80a84 | -11.21126 | -54.98384 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 351c5da2-5cf0-363f-81b9-93f96c8194cc | -15.86201 | -56.0855 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 106bc7ba-3482-31fe-b247-fe4ca04dc4e2 | -15.16365 | -47.95109 | 2025-09-10 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c05b07fd-2232-3f01-950e-d93a706e8084 | -19.91733 | -46.16062 | 2025-09-10 04:44:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c552362-1fd4-3c34-81a3-709f9f3ef264 | -16.46828 | -50.66828 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d237c47c-485c-35af-b7f7-d0121919bbf5 | -17.71922 | -44.44687 | 2025-09-10 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36c167aa-8e5b-3a51-b7ce-74a65438d9a0 | -15.90807 | -50.18167 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84bbfd58-aa3b-38b3-86de-21c22ced4f57 | -15.4782 | -49.38058 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbf8a557-5712-3f0e-a96b-d4cf8d3c3e11 | -12.99862 | -48.03788 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fa78da2-a8c7-37f3-b19f-7ddacf22265f | -15.02339 | -50.08842 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 80b0db43-18a6-32c9-b1de-58b2d5892b81 | -13.20028 | -43.37647 | 2025-09-10 04:44:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f5a65ee-d2ca-33f5-a3c0-7971b2ae0eb4 | -16.48359 | -51.97947 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef18ccd6-857e-3b17-a600-196e6cca8b8d | -15.76019 | -53.50292 | 2025-09-10 04:44:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 898514d3-a7b8-38c5-8ee3-2b801f23136d | -11.76633 | -50.58085 | 2025-09-10 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1744c00a-09f0-314c-bf36-48a725a2f0d9 | -11.29448 | -53.96638 | 2025-09-10 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfedd30f-5f25-3510-943d-8e63ce852d86 | -15.80875 | -52.24377 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d97e7a6b-6bef-3d55-ba93-8274497df8b9 | -19.30304 | -43.25941 | 2025-09-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6d67449-a8c6-3d2b-b732-ad4ef25e49a5 | -12.18669 | -50.63801 | 2025-09-10 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c2fb9c0-4bbf-38c2-bebb-15d1d3bc2777 | -15.80599 | -52.23961 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abd83c43-afc3-3b03-a080-4016b02cb9d9 | -16.52026 | -55.13559 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 299ae4a9-3be5-311b-b59d-98d6f1352818 | -15.95683 | -50.22718 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29f9e117-011b-3d45-87cb-1290c9beb496 | -13.97288 | -48.22345 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd0ecb3e-7f5d-38e6-b5f7-aa7ec89c444d | -15.87584 | -52.1999 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c178f46f-0877-3fcc-97cb-8264e0c1c6f6 | -12.01993 | -51.03081 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9940aee6-6ab8-3995-acc7-4a9ec9ebffb4 | -15.10428 | -53.70678 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7714bb7-39a2-370e-af9e-0522d05d8c4a | -15.24996 | -53.78783 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb3e224b-97ee-3821-8a4d-2d4f8d2d2859 | -12.95971 | -54.75694 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e539cb94-31b8-34b6-9d4a-8f35061a22bd | -13.19275 | -45.28256 | 2025-09-10 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82db7c66-4684-3fa3-ab24-72169300394a | -13.9811 | -46.66132 | 2025-09-10 04:44:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf69dc70-47a5-3bdb-a783-b1f45cdef7e3 | -16.34945 | -52.94123 | 2025-09-10 04:44:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b8c52db-1e1e-39f4-a0e5-0b99646c3b78 | -19.53838 | -46.09432 | 2025-09-10 04:44:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af2e1115-d853-3f3c-a292-0ce36061da32 | -12.93086 | -54.78957 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d86be9bb-66ef-3288-8320-f710908ec9b0 | -12.00146 | -50.98079 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| de67c6a6-7a3d-3386-bb7b-0222c93f8bf9 | -15.17531 | -47.94842 | 2025-09-10 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3d7f4c3-226a-32fa-a4c1-61a41722fddc | -16.45419 | -51.97081 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 004b606e-10c1-31e9-8ab0-f96b46562741 | -12.94346 | -54.80613 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 853e6ea3-1617-3646-bebb-7bfd72f4e663 | -14.92396 | -55.91794 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88ed7b92-0f62-3a6e-885b-a9c9a4e4b5d1 | -13.01831 | -48.03883 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24708287-70f8-3020-8d00-8f02ccd0e89c | -16.62267 | -49.76284 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e8b21e2-e661-311c-9557-0282a412c3ad | -16.47164 | -50.66883 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9471eac-6d72-3c4a-a153-f7e74b9d00c2 | -12.99566 | -48.03321 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85e5abef-d20e-3c4b-979f-0369db385e3a | -13.2245 | -51.77043 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa95f2e3-11ba-3d6e-a093-717ffd38d6f1 | -12.93167 | -54.78494 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ace3e6b-9aa2-37b6-894a-80a640bcadbb | -18.14297 | -51.72609 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a89c8541-7927-3029-b75e-043ddc9bf2af | -13.64545 | -46.97947 | 2025-09-10 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ee3bd8e-7e0a-3ea1-b8f0-d62bac5b0924 | -19.53402 | -46.09373 | 2025-09-10 04:44:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 397846d8-885f-365d-9280-f1c7c42b6845 | -13.12015 | -54.92457 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cf78073-d3aa-3833-9aa3-4dbe8263f838 | -15.15873 | -52.31969 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4353c81c-519d-3079-a77f-d3488b9402de | -15.25412 | -53.7845 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1456a698-7bcf-362e-8df3-f180bc7de357 | -14.65703 | -44.05031 | 2025-09-10 04:44:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 862d72fb-f48b-3b04-810b-95833427297d | -12.20443 | -53.86489 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0c64b3f2-dba6-3dcc-99f4-c7766238ce68 | -12.95676 | -54.75169 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 809e5fe0-5358-3fa9-ab30-7521d051f5c3 | -14.75527 | -45.33311 | 2025-09-10 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d97efed-531c-3504-bc5c-29c3a884f800 | -18.00619 | -47.11682 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a8d2d59-dc0a-300f-a687-d91e7347b85f | -11.20872 | -54.99864 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70106718-385d-3505-8268-948b02c49db5 | -14.85531 | -49.53844 | 2025-09-10 04:44:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2042dfa-cf7a-3fb4-abe0-75c0537fb287 | -18.1324 | -51.72802 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9583bdff-72f5-34df-8ef6-4a65033c4aa7 | -18.01677 | -47.12931 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c175a3e8-bbf4-3092-abf6-0958b471b0f3 | -15.80642 | -52.25824 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71895452-b084-3663-abba-b6e3ff3b2784 | -16.45304 | -51.97802 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e639d7ea-010a-3751-ad9f-a75ddd23c587 | -13.01769 | -48.01782 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bd441b7-2dc1-344a-96df-ed8d1bfd6160 | -17.18354 | -50.15582 | 2025-09-10 04:44:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18dfbc1f-c164-3e88-86de-a44ddbc3ab18 | -12.95006 | -54.74583 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b972f7a-402b-3d0a-9e83-b4d0b7145bab | -12.6136 | -56.96365 | 2025-09-10 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b0ea65a-aa26-3e79-87e1-730d15ecef2c | -16.1448 | -47.89111 | 2025-09-10 04:44:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cad5c1b0-31e5-3d2c-91fc-0f27d0f47526 | -16.34548 | -52.94431 | 2025-09-10 04:44:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0656fa85-db9e-3a5e-9cb7-a26b0140f4f8 | -15.01579 | -48.02017 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32577f4b-5432-3d66-9093-6b4919f9a6ae | -14.89322 | -55.86562 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00d8f59b-5877-308c-8d75-a3ee911bc70d | -16.45752 | -51.97137 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7525ddbe-b4c1-326f-9ed7-99d312ad5cc9 | -14.33467 | -47.29776 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 872359af-97ee-3fc2-ac55-135af2e81361 | -15.78319 | -43.13145 | 2025-09-10 04:44:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 409f4806-632b-3845-b670-2e5127424076 | -15.14898 | -44.02563 | 2025-09-10 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a861ce10-a3ac-3729-9dfd-92c476599e81 | -12.05211 | -51.04336 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfbdaffa-0e73-3e7e-8467-b85593de9599 | -16.05194 | -49.96624 | 2025-09-10 04:44:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dcedf3c-f9fb-3b4c-98ed-80cf996e004d | -19.29077 | -47.98346 | 2025-09-10 04:44:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c01775aa-663b-3f94-b832-ac8550679f89 | -12.20371 | -53.86912 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e9d20fda-f80a-301a-ba6a-4b8715eda3c0 | -16.29316 | -45.6875 | 2025-09-10 04:44:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31b61cb6-e325-3f4d-abd8-b2ab47c57459 | -17.18411 | -50.15198 | 2025-09-10 04:44:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc239076-17f9-391b-a77d-b1e0530fe85e | -18.35603 | -49.34198 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c52ede8-0423-3290-9859-22e9dbf074f8 | -15.13834 | -52.39523 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 616519d8-375b-3376-8337-a534dd39a0f6 | -17.30804 | -46.74701 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 158a895a-19fe-32db-964f-97a9009d9125 | -15.80367 | -52.25401 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d514b9bc-bdd3-3995-a992-b7a07f84914e | -16.122 | -55.86607 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5319b787-a245-3030-b562-50787e9698d9 | -13.92585 | -48.2561 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53b9c994-1184-3ce9-aed0-169cfe861471 | -12.94266 | -54.81077 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58bd35ed-6a3b-3020-beaa-3c7c1bb158fc | -11.94635 | -51.04796 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2cfc94f-b183-3bab-b335-c33c05dc51a7 | -16.41045 | -50.8881 | 2025-09-10 04:44:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87204f0d-4383-33f3-a12a-d6537b93932c | -13.94549 | -48.26136 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55bd793d-6277-3b61-a1df-8b54e6a91583 | -15.93822 | -50.23558 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d8012a39-a95b-3278-8391-f2a4f5452736 | -15.84418 | -52.26861 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b84ec15f-06a7-3809-abec-db538b8b3188 | -18.00554 | -47.12183 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 894132cc-54e2-3e0f-9b6c-7576e7df4e60 | -12.96689 | -44.01564 | 2025-09-10 04:44:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ead09006-8267-32d1-8e03-cae6e2e70fd7 | -18.33292 | -49.32512 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e07fe0f2-9005-3581-b816-6ed809f35320 | -17.5581 | -44.54214 | 2025-09-10 04:44:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6934a897-04fc-31b8-b52f-ffa279afa66f | -19.46736 | -43.70987 | 2025-09-10 04:44:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68e758a5-4c41-3119-b175-ab91beada616 | -14.56178 | -52.16371 | 2025-09-10 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a4f3348-1034-3675-938b-80bed49bb704 | -15.17897 | -47.94903 | 2025-09-10 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e521d515-e827-3227-9785-1b79a421fe80 | -18.02255 | -47.1473 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |


[Clique aqui para ver as próximas entradas](README81.md)
