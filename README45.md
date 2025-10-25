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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a049e45-3065-3f48-b9ee-67d332aca58e | -14.53547 | -47.94315 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 43d2a741-932f-32e7-b228-9d9b9cc8c215 | -15.47371 | -50.45924 | 2025-10-25 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7aa6183e-6a27-30c9-a1cc-2cde0cc994cd | -13.91478 | -48.40875 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c58f213-c7f1-3930-92aa-3832b9b768cb | -16.29045 | -58.39517 | 2025-10-25 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4ee0473a-dc7a-3b3d-ba69-2269d8729636 | -14.90923 | -52.44668 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81625442-6f2a-3a07-b99b-786c085a4eaa | -19.87388 | -46.97662 | 2025-10-25 04:21:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff8a8cde-e5fb-3e2c-91ed-b9040ee86fb9 | -18.17055 | -51.76733 | 2025-10-25 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 609fe849-5f6c-340d-a822-52802678599e | -15.13497 | -47.93143 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7f15ccae-7014-31cf-abff-bf0c49dcc3ce | -14.37892 | -51.52304 | 2025-10-25 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f9007a5-48b3-33a8-9c9f-c574d2655a1b | -14.49985 | -47.90677 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8be55b3a-d857-3cd8-97b9-76afee0d0a22 | -21.07192 | -43.63892 | 2025-10-25 04:21:00 | NOAA-20 | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6e2f3604-8159-3bee-a01c-275ae01dc603 | -15.53368 | -45.70033 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01958786-3fc2-316f-9808-7631a02689ff | -19.7617 | -48.29233 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 41e2c793-e908-3eaf-a9af-8f3399b83833 | -15.00447 | -49.98599 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f319a4b4-aa49-3e02-a900-1b98a1207dd9 | -14.1748 | -47.31586 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1315079-5b35-3e2d-afb3-dd585741f267 | -15.44211 | -48.5773 | 2025-10-25 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbe95add-94f8-3ebd-a238-3cd0ccdbf42d | -14.87162 | -48.10285 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d3944bba-4622-3f0e-8d88-37a7b54bf1e3 | -16.06631 | -46.61983 | 2025-10-25 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f358d8ad-fc30-3e59-a516-cb1d9d7f8b27 | -15.8419 | -49.10506 | 2025-10-25 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e829d45c-3edf-3db3-a999-a7b936bdbc50 | -19.63052 | -46.13601 | 2025-10-25 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 942b79d9-24df-382a-bbbd-b4514f66de74 | -15.50274 | -50.44625 | 2025-10-25 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8bdb68b-c9ad-35bd-8784-cecd833d012e | -19.32941 | -49.08575 | 2025-10-25 04:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96b74be1-e048-35c1-9c78-06878f194bc9 | -14.54411 | -48.01783 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab019588-a813-3810-8745-3842783cb722 | -17.61796 | -46.59626 | 2025-10-25 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40cd2a7b-dbef-36c9-ae7c-b707768da77c | -14.44171 | -48.06933 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41a3cb5d-30bf-33e2-a489-442851d00800 | -18.24643 | -44.19194 | 2025-10-25 04:21:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d9aa405-1719-31b1-a62e-a1e714b34e5e | -19.86001 | -44.30383 | 2025-10-25 04:21:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cffcfdbd-48d6-365d-a3c0-398123aa2d62 | -14.71884 | -46.84904 | 2025-10-25 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b99b4b2-29ef-3242-b12f-f93f0b4fcdf2 | -16.58788 | -43.5023 | 2025-10-25 04:21:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cc955427-ea80-3d92-a51f-055792934423 | -18.36928 | -43.65913 | 2025-10-25 04:21:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f7a73bc-3f26-3e33-a453-a44e324282f9 | -17.33446 | -45.69677 | 2025-10-25 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91bf2983-9140-38dc-871a-4c24b5cd4fe8 | -19.87664 | -46.98085 | 2025-10-25 04:21:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e00244f3-92f2-3a76-b568-a514b0f05cd1 | -14.38496 | -51.53534 | 2025-10-25 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4120265-2e86-37db-9838-6e9ccb7175ca | -14.45719 | -47.93419 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd38d24a-f8dc-37a8-adc7-d62db770f096 | -14.86863 | -48.07909 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b65773e6-cd83-3fb4-b43b-7ea15fde9d38 | -15.23382 | -47.92857 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 546b2595-57f7-39f1-907d-2ca77f5e6225 | -14.3843 | -51.53895 | 2025-10-25 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 500f6709-2f53-3902-9d6d-3fadf9d9e72b | -14.18146 | -47.317 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 375bcdeb-6a63-3909-94b8-e379a4f4fd73 | -14.53706 | -48.0398 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab846108-8e0c-3eec-bd55-c3cdb1122116 | -15.93828 | -56.11621 | 2025-10-25 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7da61439-c298-375b-a62d-ca4f8feaa6d2 | -14.93395 | -48.12524 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3f36627-2dda-39ae-945f-452c4a529e88 | -14.32717 | -46.61978 | 2025-10-25 04:21:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c6be8a0-7d54-3365-8f57-0a14cb37e7e8 | -17.21353 | -47.65439 | 2025-10-25 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfb4b889-aeff-3e9c-ab28-c7819a1f2ee7 | -18.90035 | -44.40532 | 2025-10-25 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43825d34-37ac-3a5d-b607-d837564b829c | -14.47131 | -47.93271 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ebe4f004-08db-36dd-ab38-38fd1961e2f8 | -15.24389 | -47.93033 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f42a29b-d46d-3a0b-92e0-cc26a0dd86f4 | -14.81035 | -48.44882 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc2b344d-5d44-302a-a3b8-3ad911b959e2 | -14.92474 | -48.13894 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0fd56da1-89b4-318f-ac1a-067c5c0adc43 | -19.62645 | -46.13215 | 2025-10-25 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5834af36-94d4-3623-afde-9748167a07c4 | -13.91543 | -48.40481 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dae34b6-7931-353d-bf32-4f045c91b48d | -14.47289 | -47.90221 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94f5b4d9-21ff-3da6-8bc4-8dc9273b12bc | -19.87722 | -45.83609 | 2025-10-25 04:21:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae47c45f-047d-3d17-9c36-91c5fe79e02e | -14.54162 | -47.9479 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 905b8c09-9629-35ee-b1e8-9a8aae3452a3 | -19.2939 | -46.80027 | 2025-10-25 04:21:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b6a36dd-6740-399e-933c-eabe46e73b7b | -16.2206 | -46.48032 | 2025-10-25 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 348a38bf-d914-3a8c-9e26-aadc780b3164 | -17.37661 | -45.48427 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9840214a-28f1-31b5-a6c1-711a5aa15b01 | -14.5179 | -47.94464 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dcf963f-5896-3c5e-90bc-5cf5cb1ac251 | -13.88179 | -48.35209 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb194e04-e398-32ba-baf8-d68149c125b7 | -16.16694 | -45.08015 | 2025-10-25 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 300bc496-0259-3148-b818-b5ae9aa1fc87 | -17.38285 | -46.16237 | 2025-10-25 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3dc3b3d-50be-3f00-8357-be6e3c2e01b8 | -14.86825 | -48.10227 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ea13eafc-e53e-3471-a4a4-be528fbcd18c | -18.56116 | -50.27541 | 2025-10-25 04:21:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 64ec1850-e363-36eb-a4dd-7f45ef406896 | -14.93162 | -48.52126 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae701d72-eadb-35b9-b751-2a587276b062 | -19.83568 | -46.13745 | 2025-10-25 04:21:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a11b6c66-4f5a-38f0-b9cc-d01b77b5343f | -20.10963 | -45.84795 | 2025-10-25 04:21:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d29726c2-8aae-347d-acb7-226ff5045e36 | -14.86525 | -48.07851 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 12db8747-b5ed-3dab-84d4-2ece6ae05fc5 | -14.02962 | -46.65375 | 2025-10-25 04:21:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1df0fa9-4c79-36b7-a5e8-964a4c949266 | -14.20008 | -44.8069 | 2025-10-25 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a43b72f5-8d49-3081-9f0a-417bd5df70d4 | -19.84933 | -49.06564 | 2025-10-25 04:21:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8bf2a9d5-8b2f-3ba1-99e6-3b5704fe246e | -17.47049 | -45.99231 | 2025-10-25 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e7cc760-f503-387d-abca-628f7e8b597f | -20.3858 | -45.91946 | 2025-10-25 04:21:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7274ab10-8bf7-3fee-99a1-1b6f9d7250a1 | -13.89415 | -48.40523 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 596e0c05-924f-378e-8535-f6905b943722 | -14.87262 | -48.07595 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cdd366a-9496-3e44-822b-117cad2fdcda | -21.15332 | -48.51651 | 2025-10-25 04:21:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 95615709-7002-32c7-928b-1e2d72e972ec | -18.76872 | -47.63875 | 2025-10-25 04:21:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 824e0178-43ff-39d9-9f4a-fb914c5adbbf | -20.38921 | -45.92003 | 2025-10-25 04:21:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5306fb70-3ab6-32b8-80f4-de8ddc9097a2 | -19.6516 | -53.56506 | 2025-10-25 04:21:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 077040a7-23e5-385f-866a-39fb381cb3a3 | -13.83481 | -48.50574 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66db9171-5dcc-3b4d-be43-62c7507993d3 | -14.56768 | -49.83924 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5de57409-12a4-3141-86bd-b48008bb0e43 | -19.0219 | -49.24314 | 2025-10-25 04:21:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b18977d-78f3-357c-850d-2e89cc016f49 | -14.92412 | -48.14276 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3758dd2c-eb8f-35a0-a083-14d14e1bbb80 | -14.29004 | -48.11301 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33a6ff7c-9932-3b63-a7ad-47acb5ced915 | -14.86924 | -48.07538 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dddb3b1d-09b7-3097-adbf-7b0347575ca6 | -16.17316 | -45.08502 | 2025-10-25 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c04aa294-1e01-3b6e-8620-b4c1618252ba | -15.19314 | -44.07342 | 2025-10-25 04:21:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 015f7671-cd70-3125-ac34-3bec2bbc6e84 | -18.16856 | -51.75654 | 2025-10-25 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 32122faa-51be-397d-8808-0cd72c70822d | -14.19987 | -47.30894 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d2048210-61a4-38f5-a925-59b250fbdd83 | -16.25017 | -50.07688 | 2025-10-25 04:21:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17945844-791f-3634-9e36-8f1e2bef8636 | -17.38111 | -45.50059 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0023cdd2-2e15-3f3c-90ec-609d91980368 | -15.00368 | -49.99049 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea02f862-17bd-3a01-a95d-4c68b5c0b935 | -14.56333 | -54.17615 | 2025-10-25 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27389e2a-80a7-33de-8dbd-9dcbbc67764d | -17.47327 | -45.99655 | 2025-10-25 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f820d9c-2449-3f1b-8aed-355d7c54e27e | -20.76083 | -43.23089 | 2025-10-25 04:21:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.4 |
| e3e68c95-9105-3dcd-9aa0-8e4e04bfb9fb | -13.88103 | -48.39905 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ee9bf88-b1f7-359c-8cfe-a81c3d83c72c | -15.47886 | -44.17182 | 2025-10-25 04:21:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eea3910-f759-3e19-a972-2f640c8accd2 | -14.4747 | -47.9332 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82b29512-c8d7-3ff2-870f-295e71317027 | -19.04972 | -54.01229 | 2025-10-25 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b3bffda-5d2e-3508-aceb-702c1f2fec67 | -15.23321 | -47.93227 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 592881bf-4ce4-3ff3-ab8b-f7e16528d5ed | -14.27015 | -47.33482 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ac0ef28-82b6-331a-a1f4-6cc615307ba2 | -15.30374 | -42.96274 | 2025-10-25 04:21:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README46.md)
