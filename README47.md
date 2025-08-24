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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f09c585a-f556-37be-bed7-a48c1453f356 | -14.81868 | -55.97448 | 2025-08-24 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40eff739-3a93-365e-9ab7-f2845d626a11 | -14.78946 | -59.62699 | 2025-08-24 04:36:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3ddd95a-5a19-3823-8c2f-558a60c4410c | -15.06547 | -46.47749 | 2025-08-24 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56c0acef-62a5-31a5-9221-3032e82df6f8 | -15.29944 | -56.15776 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e117e55d-2a9a-3f48-b637-51e6b2180294 | -14.54832 | -49.1106 | 2025-08-24 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0f348e8-6dfb-3db2-a4cf-64433b6a8c8f | -14.79206 | -59.62688 | 2025-08-24 04:36:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7811ce20-1d01-341f-a328-dfa7372e7520 | -20.00077 | -50.2667 | 2025-08-24 04:36:00 | NOAA-21 | INDIAPORÃ | SÃO PAULO | Brasil | 3520707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 941c7b4b-27d9-3f8c-bc7f-f3b27abe78f2 | -15.91403 | -52.20838 | 2025-08-24 04:36:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ded5e8d3-2638-3d8d-a36a-4d73781abc40 | -17.39456 | -42.62983 | 2025-08-24 04:36:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c1996ea-c3a0-3778-b8a6-57c900efb31e | -16.40769 | -49.94611 | 2025-08-24 04:36:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6b2e8c1-3109-3a24-be28-6f6cd1328155 | -14.27948 | -48.01721 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 960ca0db-4e63-32ed-bb8d-6d718550ae8f | -20.3533 | -46.74636 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d724c09-9ad9-364a-9caf-a346f93cd4d6 | -16.48896 | -52.55789 | 2025-08-24 04:36:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df4d1044-bd29-3aa9-ab6e-2297c9ff59f1 | -18.02539 | -51.08219 | 2025-08-24 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c89cd71f-d713-36ab-be06-b11321d6382a | -14.84373 | -48.32277 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a74fb591-e41e-3529-907f-11d6474c30a5 | -15.95079 | -44.02274 | 2025-08-24 04:36:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de73ff54-8016-3971-89a5-15182cfb3281 | -20.36752 | -46.75782 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e21fd45c-49ca-3c4a-b971-befbaaa20c2f | -16.63103 | -48.87931 | 2025-08-24 04:36:00 | NOAA-21 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a49ed43-bdd6-3b24-84be-2826d448a67d | -15.00621 | -48.48103 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b0f1aaf-8af3-3407-b3c6-2ac0979e106c | -14.79134 | -59.63038 | 2025-08-24 04:36:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1a05415d-3446-3fc7-b176-150b0f0ceb76 | -15.11162 | -48.66349 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e0afcbe-2850-3ccb-83c7-340ce408f2cd | -14.79283 | -47.93296 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5aa2b0d9-8062-32ce-97fa-9daaafe73f56 | -18.92496 | -45.7807 | 2025-08-24 04:36:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4aa4d9f9-3d38-3e98-97a9-11c4b65f4d12 | -15.54798 | -56.17888 | 2025-08-24 04:36:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64f360ed-25a4-36bc-83d9-6844aa4a641d | -20.36231 | -46.73738 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c78b083-8f3a-3d4e-90a6-4cfacd227daf | -15.11217 | -48.65981 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb951190-22b3-3fa6-a47c-082c11384b7c | -20.08436 | -46.10893 | 2025-08-24 04:36:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c6808f4-8360-3a18-bfbc-4fd5d5a3d030 | -15.7242 | -56.05335 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 66194012-2602-3e0d-af91-b37f794b1b14 | -14.80538 | -47.91913 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5b59b498-8c52-3ae0-ab65-681488d5e06c | -20.73443 | -41.77053 | 2025-08-24 04:36:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c441e1a4-ab6d-3f58-9e5d-06be37788736 | -14.80999 | -47.93541 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9b9ce007-ebbf-3cef-8e58-8a56506a11c2 | -14.3644 | -51.94852 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6232ebf8-be33-38c7-ad37-709c7ec67966 | -14.91823 | -47.31913 | 2025-08-24 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b860fdc-8cb3-3986-978b-6d40707db822 | -15.52377 | -47.33108 | 2025-08-24 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c118266-559e-33b1-8316-9b53cc42770a | -14.94661 | -48.00648 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67e64d69-51e1-3a25-9815-6495ec048ead | -16.4235 | -49.15004 | 2025-08-24 04:36:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6182663d-fb86-3962-bd99-9a9b1797146f | -17.59346 | -46.09504 | 2025-08-24 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f916ef6-d5f5-376e-a726-c755398df4b5 | -14.50961 | -51.9217 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b8c6ea9f-4bf9-3c6b-9ee6-918afda57d0d | -16.41873 | -49.94057 | 2025-08-24 04:36:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aaf8a9c-c9fa-354e-a025-e407f69a2600 | -14.7776 | -55.91206 | 2025-08-24 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c2db2be-57be-3383-b9d6-f8b4202e1053 | -14.93749 | -48.02073 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| badd1389-3621-36fa-8fc3-e8ef41a01864 | -14.46458 | -52.04447 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 111dbcfe-a6e1-3b35-8de1-96f4b3fac2f6 | -16.78828 | -51.35092 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 668e851e-e550-397c-ae91-47bcf89049cf | -15.67881 | -53.87863 | 2025-08-24 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00d1c6b1-c22c-337f-9c09-a1bde00092e0 | -19.93923 | -47.4908 | 2025-08-24 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31db5f57-99de-3066-b156-2b5e609c4178 | -16.79103 | -51.35515 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 3664dbfd-0cc4-31ad-bf4b-a908914f9e08 | -14.29987 | -58.49216 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cd014be-eec2-3fb5-98ea-fd6c6b9e5686 | -15.96624 | -43.01874 | 2025-08-24 04:36:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f28b7386-3e69-3701-bfc4-cc02b9b01f0c | -14.29475 | -60.37563 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0b328ad-e373-36ac-ac2b-ee428ecdb01f | -16.42405 | -49.14635 | 2025-08-24 04:36:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0133f5f5-f715-3ace-bb72-1719b0d6be39 | -14.28664 | -60.37641 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03c2140d-b30e-3e23-a4d3-3cc525059674 | -14.80712 | -47.93112 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ce2d0be2-8b83-337b-8c03-82a3c2075b5f | -20.36487 | -46.74794 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a6e70e5-c51c-3695-a652-379efb33e12d | -17.59606 | -46.10537 | 2025-08-24 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 194cc7c9-7be7-308d-8bfd-867a97a79771 | -18.75554 | -45.09515 | 2025-08-24 04:36:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 4be8af98-67de-3bbf-8a6d-ef5bbe54f8f1 | -14.46872 | -53.08348 | 2025-08-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a861d88-415b-3241-a17d-52bc57559cfe | -14.81628 | -47.94028 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1eb16eac-52a9-363e-b945-0ada7c3054ed | -13.02401 | -56.87307 | 2025-08-24 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fdfa7961-905d-3785-9a54-9b1be1ad4543 | -14.82291 | -55.97526 | 2025-08-24 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a3eda53-d2b1-3467-a016-a85e8185d274 | -14.16641 | -50.59474 | 2025-08-24 04:36:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c48c12e-8734-392a-bf34-152ad13a377f | -16.71273 | -49.05928 | 2025-08-24 04:36:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e68d618b-2c21-3aa4-adb2-892ad55c1d28 | -15.08928 | -48.69777 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b5f2ee5-8b0b-37e9-82e2-199a8fc9a405 | -18.02151 | -51.08525 | 2025-08-24 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5648d22b-00f7-3b30-9642-4ad0d584c1be | -20.08107 | -46.12055 | 2025-08-24 04:36:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aa5fbcb0-4f5e-3938-b0a8-a44ca0dac72c | -18.39764 | -46.84205 | 2025-08-24 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77eaf426-eabc-3a44-b381-28d5939d40fb | -17.41386 | -48.10511 | 2025-08-24 04:36:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44a4751a-77b1-36c1-93cb-cb05f5de886b | -14.33114 | -58.59322 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9261621-f7e4-3b30-9a7c-daa3aaf76a4f | -18.39701 | -46.84678 | 2025-08-24 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 276ff9b4-9d5a-3201-8e4c-dba6ec3d140a | -15.52916 | -54.74888 | 2025-08-24 04:36:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02fd8d39-5007-33cd-b000-af92559318fb | -14.79689 | -59.63059 | 2025-08-24 04:36:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3ed81bf0-4f52-31ee-8304-0d0f9e6ddd1f | -19.94292 | -47.49134 | 2025-08-24 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1591e1d6-1fde-326b-87ba-720d2347f6ea | -16.79494 | -51.35212 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 32.6 |
| b42cbaa0-dadd-33b4-8b46-b576735d44f7 | -14.29335 | -60.3724 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04ff1cef-9a86-372d-8001-f2bff1a8b684 | -19.92706 | -44.21228 | 2025-08-24 04:36:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6efff765-0b24-3efa-b5ac-4f5f1883b1a8 | -12.59348 | -60.35815 | 2025-08-24 04:36:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 776bf67b-48b1-33ef-a0e8-2615d6a30375 | -17.59283 | -46.0999 | 2025-08-24 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fc418c4-1b00-3568-b59c-b36b240271e8 | -14.53435 | -53.23113 | 2025-08-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66540305-4f7a-33d6-8200-fd67969a509a | -14.82365 | -55.97118 | 2025-08-24 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c921d7b-5641-3a16-9c5c-96194442c788 | -15.08873 | -48.70145 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad6fb70d-e579-3ecc-becc-128208a57fb9 | -19.63058 | -43.18123 | 2025-08-24 04:36:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| beb12fcd-52a2-381e-800a-530e3c2e34b1 | -14.58218 | -54.50942 | 2025-08-24 04:36:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e39fdd0a-45a2-3ec8-9d0f-933288094f75 | -15.32067 | -56.16182 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b8626103-2c93-3ec5-b48a-a36c45bf34e3 | -14.79015 | -59.62347 | 2025-08-24 04:36:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e101b9c-7544-300e-a5be-4ce7f383b147 | -16.48661 | -46.75036 | 2025-08-24 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e688ed00-bff5-3178-9a0a-11c1d2a13902 | -17.82933 | -44.54992 | 2025-08-24 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5404d1b5-20e9-3fb2-ba49-4ab489284cab | -17.59862 | -46.10418 | 2025-08-24 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b9d1eab-2717-3a0a-bdb6-b8b63aaa73cd | -14.47051 | -53.08307 | 2025-08-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b04d4f0-de3e-3285-9070-f562afefa02d | -11.99343 | -61.02943 | 2025-08-24 04:36:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 03b69d46-9002-3a70-9b18-ed71d84652df | -17.39358 | -42.63033 | 2025-08-24 04:36:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f01a9ba7-67f5-35ce-8147-62e62f9fc9e0 | -14.79339 | -47.92916 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3aedd28-74c9-3c55-b4b8-492c13798bd6 | -17.39521 | -42.62436 | 2025-08-24 04:36:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf2fa2a4-de04-37f7-873b-83d79b2769b5 | -20.36753 | -46.72738 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0d1180a-cbe5-3d81-9e60-6152df5c9817 | -18.03791 | -50.61312 | 2025-08-24 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b204ad48-5b1d-39db-8ef6-02ff036a7e9a | -15.00848 | -48.48903 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e09793aa-619f-336b-b033-43e1ab5d9d6c | -15.23052 | -48.21601 | 2025-08-24 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a59dc3e4-0ff5-3912-8848-e471801d2277 | -14.36309 | -50.70538 | 2025-08-24 04:36:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e9026f6-d9ca-3e65-bd0b-382f6a1f052e | -16.42125 | -49.14213 | 2025-08-24 04:36:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ea65af0-0142-3fd2-908a-97effbf7e6e1 | -19.83638 | -47.53471 | 2025-08-24 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02a622a6-8d35-35e2-9dc7-1e83d39a8a8e | -14.7804 | -45.38867 | 2025-08-24 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55cb4fcd-25e5-39ca-be99-210cb307d7d8 | -14.87707 | -47.60012 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README48.md)
