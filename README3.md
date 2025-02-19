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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b337b4e-64e0-3917-86db-c7c09381a403 | -16.61483 | -43.33915 | 2025-02-19 04:23:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36d80375-5c4b-3265-9767-d47d7d7d4c8c | -15.5685 | -47.85624 | 2025-02-19 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 473340f4-d09c-3587-818e-4acf49dcf013 | -17.5045 | -39.95481 | 2025-02-19 04:23:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ab10a03c-75d4-3268-8262-d74acf6694b3 | -11.11239 | -45.12234 | 2025-02-19 04:23:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e92415d0-6814-31f2-b6a3-9194cbe1f483 | -10.94449 | -45.17514 | 2025-02-19 04:23:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60ff258b-4cef-31c8-8fbe-c89601495028 | -20.30162 | -46.516 | 2025-02-19 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e379b7ba-d658-321b-8ac3-cb857734b39b | -11.75996 | -47.72015 | 2025-02-19 04:23:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15d1b8e0-109e-320a-a206-c4e19a12a32b | -22.95383 | -42.68568 | 2025-02-19 04:23:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0a3791ea-0ce2-3ffc-b1e0-6202a87ab036 | -15.62318 | -46.18743 | 2025-02-19 04:23:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0db0085-1f38-3dbc-b1e2-d069f00c6bbb | -22.46067 | -49.28625 | 2025-02-19 04:23:00 | NOAA-21 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c00cce1-3ce6-3c64-9641-cf6c1039ec3c | -10.98732 | -44.49858 | 2025-02-19 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18f2e0c9-24f1-3bc2-bba8-98b1ceb8997c | -20.17258 | -47.28508 | 2025-02-19 04:23:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 514e057d-d0c0-386d-b14f-2bb655c40693 | -12.08284 | -54.58714 | 2025-02-19 04:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cb19497-d44d-32aa-a795-58e7c37df6c0 | -16.6812 | -43.88406 | 2025-02-19 04:23:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fb9dc6a-b372-3ea8-bc5a-14595857987e | -15.05526 | -42.42486 | 2025-02-19 04:23:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ca04e417-ec9a-3809-90ea-94d004cc73e9 | -20.30721 | -46.31306 | 2025-02-19 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dbc54e3-6a1a-323e-91c0-baeea15c6190 | -20.31059 | -46.3136 | 2025-02-19 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9a02ea57-e055-3ffa-be37-c88adc12a2fd | -20.76378 | -46.76928 | 2025-02-19 04:23:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d8a89112-5e59-3ee8-bfb1-848a5f6350f3 | -11.03002 | -45.06239 | 2025-02-19 04:23:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8c6ddfd-ecf1-379f-9a55-2c764e80d6ad | -15.81784 | -42.11687 | 2025-02-19 04:23:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0c1113f-1ec4-3f72-9a2e-54231c28621c | -11.58382 | -47.63436 | 2025-02-19 04:23:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36a87741-d8d5-3e72-9f6d-eb5c28887ff2 | -22.67402 | -42.85762 | 2025-02-19 04:23:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 61081be6-7940-3e03-be54-688cc3a5f001 | -22.75909 | -42.40039 | 2025-02-19 04:23:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dee1e698-401d-3d51-a96c-82a2881b58ae | -20.73325 | -54.60077 | 2025-02-19 04:23:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f5d60bc-66c1-375f-b4ba-766c82c0d7b1 | -11.02874 | -45.18104 | 2025-02-19 04:23:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29d75046-71eb-38b5-a271-cc4665901f9e | -21.12037 | -44.23527 | 2025-02-19 04:23:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1dd90eae-6a20-32b4-b6df-c29add4cb89d | -15.55994 | -47.73922 | 2025-02-19 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44ad3d18-6a17-37ed-a7cc-1b63e7f5ea1a | -10.9478 | -45.17567 | 2025-02-19 04:23:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e4dd8ca-243d-3cf3-8883-bd2c8fb8152a | -15.07857 | -48.94497 | 2025-02-19 04:23:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e682eef-520c-37c3-bef4-0426db20a3de | -20.55476 | -40.9301 | 2025-02-19 04:25:00 | NOAA-21 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7f7411cd-2d70-3d32-a3cb-142f95dfa782 | -17.7438 | -56.31062 | 2025-02-19 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1cc27c91-743e-3ee0-8b09-45eeac63258a | -23.98667 | -48.91626 | 2025-02-19 04:25:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8db929f7-d8ac-3fcf-ba7f-581127d009bf | -19.1696 | -40.13247 | 2025-02-19 04:25:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bc4097af-5e40-342e-b466-ea404bcaf663 | -20.55535 | -40.92513 | 2025-02-19 04:25:00 | NOAA-21 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| be87e647-f81e-308f-9282-30f1933ee89a | -19.28653 | -50.11246 | 2025-02-19 04:25:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d1f285c-b49b-35be-8322-b127373781e9 | -17.98016 | -47.21865 | 2025-02-19 04:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 224539bf-b78c-333a-b3d6-00690fc92fb6 | -29.87307 | -51.15895 | 2025-02-19 04:25:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 1b60cf55-34ef-311f-8b72-a3187a57ec06 | -20.22185 | -46.48453 | 2025-02-19 04:25:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2254062-7cc1-3567-a9c0-75d7ae1a4fdd | -19.53941 | -45.90943 | 2025-02-19 04:25:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f074dac-1416-38af-8b95-57e58555b35b | -20.40323 | -43.75523 | 2025-02-19 04:25:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aa3175ee-5e20-3da8-bf9a-9b28c323caf0 | -20.22409 | -46.49261 | 2025-02-19 04:25:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83b13ee2-672f-356a-b8ba-4d5283790735 | -20.55694 | -40.92661 | 2025-02-19 04:25:00 | NOAA-21 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 681cb474-fd90-37f9-a568-98fa71e031d1 | -19.98163 | -44.85977 | 2025-02-19 04:25:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c56eea9-f342-36b8-b3e5-a2e46d5858df | -20.60191 | -43.12344 | 2025-02-19 04:25:00 | NOAA-21 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f83628ae-c2d3-31e5-b531-f5e155cf9832 | -30.14965 | -52.02548 | 2025-02-19 04:25:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 7065b190-e268-3ace-811c-b4264078bc64 | -20.22465 | -46.48884 | 2025-02-19 04:25:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87e5ce91-1b6a-3c96-a550-a9d2e7b6dcce | -19.70129 | -44.77407 | 2025-02-19 04:25:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d35afc16-6531-33d8-94b6-85e43bc296db | -20.22129 | -46.4883 | 2025-02-19 04:25:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f10c2786-1e63-3b9b-89be-ddeced70ec9a | -20.55988 | -40.92552 | 2025-02-19 04:25:00 | NOAA-21 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ba50cbf5-603b-37d2-b785-e00f4a6164b8 | -19.45537 | -45.30786 | 2025-02-19 04:25:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa4f2d49-7803-3c25-99a9-055533a67d76 | -29.89121 | -51.23269 | 2025-02-19 04:25:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 8eb4edbb-470c-3cdf-9be5-ddde6f74b652 | -18.29627 | -44.13518 | 2025-02-19 04:25:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb40c5fa-5253-37fd-be59-610c9e230f3f | -19.53658 | -45.90494 | 2025-02-19 04:25:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb1aeb96-2b4e-3d5a-a633-f314b4164cf6 | -18.72079 | -49.16301 | 2025-02-19 04:25:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64b3b702-79a6-3a46-beac-c5b26fc2a4de | -3.27434 | -42.37992 | 2025-02-19 04:44:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4ce2456-08a9-38eb-a22d-2e7b5b846614 | -3.26959 | -42.38009 | 2025-02-19 04:44:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39f44501-9171-3a6e-846e-312a325a5886 | -3.27522 | -42.37423 | 2025-02-19 04:44:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adde22d1-6825-3814-81ff-8126dfd37954 | -3.27041 | -42.37445 | 2025-02-19 04:44:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99bef1eb-0a09-3e85-a498-2a2df1f9af23 | -3.27542 | -42.3751 | 2025-02-19 04:44:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3815f196-9d2d-3ac9-be53-e35eee9bff56 | -3.27458 | -42.38077 | 2025-02-19 04:44:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e57aea11-f891-3dfd-83af-0430f03dc0c5 | -3.26935 | -42.37924 | 2025-02-19 04:44:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36a7c793-3d8c-3167-81dc-93e552bd478e | -6.21566 | -48.06075 | 2025-02-19 04:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc7c7b59-5c5a-3f0c-9d3a-2ca121a1618a | -10.55926 | -46.88142 | 2025-02-19 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f10bbb18-cb81-3b1d-bd23-cd5c11936127 | -11.11264 | -45.12232 | 2025-02-19 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb34387a-78dc-3969-ade8-bd3f36785a0e | -5.64875 | -45.91077 | 2025-02-19 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4e880cd-a5c9-39f2-bea8-251bf13e26a5 | -9.99071 | -48.08754 | 2025-02-19 04:46:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59b26de7-b72d-343d-891a-ef0c66711593 | -11.03102 | -45.06057 | 2025-02-19 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77cc620a-f379-3729-b82a-5222a8e2f0db | -6.21505 | -48.06484 | 2025-02-19 04:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7678a5d5-f796-3404-b21a-90b766917a11 | -9.27028 | -47.90657 | 2025-02-19 04:46:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26155dd5-2295-3f2a-929f-0f2a9c90714f | -11.11034 | -45.12328 | 2025-02-19 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84b0b961-4e86-37b6-a88a-e106d342d577 | -4.13047 | -54.8977 | 2025-02-19 04:46:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca43501b-dfb2-3cc2-8625-353cf191251e | -5.67479 | -45.23092 | 2025-02-19 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34f9d940-45ea-3ae1-b7a1-7ded4424188f | -6.73181 | -38.95951 | 2025-02-19 04:46:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a731da6b-2e21-3a92-8963-b253e2411b70 | -11.57743 | -47.63706 | 2025-02-19 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52963450-e24b-3668-9620-4017c552e93a | -5.87788 | -48.1052 | 2025-02-19 04:46:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b562288-27e5-3b7b-8a12-04ef8812c1f9 | -8.12359 | -43.13997 | 2025-02-19 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cae02469-42a0-3b5c-b54a-cf2312485338 | -9.98451 | -48.0772 | 2025-02-19 04:46:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e978f202-221f-3024-a5df-748f8ab444be | -11.57672 | -47.64209 | 2025-02-19 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e470b17-ff51-382e-90a3-137ff911876b | -5.8743 | -48.10465 | 2025-02-19 04:46:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a38277e4-b20b-34fa-bc79-74f87257b353 | -11.57348 | -47.6365 | 2025-02-19 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac5b913d-6c0f-3646-b5a6-84276c8f60fe | -8.12868 | -43.14064 | 2025-02-19 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b3a2bef4-6144-33e1-816e-400526ced839 | -14.68511 | -53.38692 | 2025-02-19 04:48:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd8fca10-8348-3d5e-baed-ca8093ed01dc | -15.24078 | -51.45827 | 2025-02-19 04:48:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 603a60e1-3c42-3128-9812-8c32958f5142 | -14.97726 | -50.7669 | 2025-02-19 04:48:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46c0b739-eb51-3bd2-9b51-9bab9427917a | -18.29421 | -44.13802 | 2025-02-19 04:48:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67e73f97-07b8-3b58-a669-6df3cdea993f | -16.20056 | -56.76094 | 2025-02-19 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d666757-ca36-3f38-84fd-bac54a9221f6 | -17.47526 | -47.01936 | 2025-02-19 04:48:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3a6dbd8-e28a-36df-86e5-2de64c3d585c | -16.37502 | -46.87468 | 2025-02-19 04:48:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b0ae146-7bec-3b57-8a9e-9827dcd52910 | -14.68235 | -53.38279 | 2025-02-19 04:48:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3063be34-ef24-3a72-86a5-28454f28c14e | -12.24971 | -45.44217 | 2025-02-19 04:48:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4e32cbe-8eba-348a-b819-5620823ef7a2 | -13.7955 | -41.69972 | 2025-02-19 04:48:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 705eabde-4860-301e-ac21-1fd34a5c2498 | -15.79745 | -51.27684 | 2025-02-19 04:48:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f3e5a23-11ad-3971-8e62-0555dbed30b4 | -15.70031 | -50.51748 | 2025-02-19 04:48:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82b05a1a-f282-31b9-a866-db404ecf4193 | -14.68567 | -53.38335 | 2025-02-19 04:48:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75b8a3a2-9697-308c-92c2-1f16c10a3791 | -15.56954 | -47.85695 | 2025-02-19 04:48:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1c66674-c7a9-3cad-81f1-2f4777d5012a | -13.795 | -41.70428 | 2025-02-19 04:48:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 59548fa6-18ba-3d52-b3e7-b2ab4546a58d | -12.51145 | -60.63692 | 2025-02-19 04:48:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8debb86-2492-319a-adf1-b53a6511933f | -17.47138 | -47.01412 | 2025-02-19 04:48:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f73f62e1-f4e9-3a8a-8f89-5431ba5ff86d | -14.68178 | -53.38636 | 2025-02-19 04:48:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 199dc7d4-9dd5-33fe-8978-75ea7abcaad5 | -15.07821 | -48.94448 | 2025-02-19 04:48:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README4.md)
