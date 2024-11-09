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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d372b62-8a53-3775-8d73-ae01e0191fd4 | -4.75567 | -48.3644 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc5a1515-ebc6-3507-98b2-a4a6fbe4e780 | -3.22012 | -50.20248 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9fbfba1e-f277-3568-8eb1-8c2ddf3db2bc | -2.80886 | -51.49477 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 197ffce9-b554-3ccf-b26d-0bdda2e3c5ef | -2.86351 | -48.45209 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d7a33e4-32f6-33ed-9566-41fb63675bf9 | -3.5371 | -52.17086 | 2024-11-09 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 079f4398-95ef-3ca6-8869-ea21e75737ea | -3.46855 | -51.061 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ba2821a-6f49-3581-bd1b-cb1725f2f8b6 | -3.02771 | -50.36642 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6f90e60-8e08-3bac-9c7d-b99afadfbd03 | -5.63017 | -44.82838 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f928010e-af97-3c5d-b04c-d24f1b21f244 | -3.3344 | -51.2447 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 198198c2-0e91-3ec6-bd2b-cf1c93b0a1cb | -2.33325 | -52.76242 | 2024-11-09 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3c3648a5-d082-31b2-8c95-5b1cff2fee3b | -3.22937 | -50.44299 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bca1f182-3c90-38a4-a9b2-2778c49d797f | -3.47586 | -50.80259 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d70d7503-fb20-3254-aeb2-f863f2735cb1 | -11.09838 | -43.34375 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| de797989-56cc-371a-99f2-684421ac22cc | -4.37783 | -48.58086 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a671248-8ab3-33e3-abad-9cba97efd0bf | -2.19095 | -53.62859 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d77f39a-5916-3ba8-855c-5d8bdf14551e | -3.35509 | -50.26786 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d3955e60-26e5-3032-a85f-f568a2471771 | -3.01758 | -51.04259 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1feb32cd-f998-317b-999b-fcf1f6af244d | -3.29764 | -46.41422 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d4e0ede9-a9d9-3b8f-a1f3-ceb35f0fa100 | -3.26542 | -50.14741 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e39f521-0e97-38e7-bc29-ba2b702a7bc5 | -3.88817 | -46.61992 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8c974b0-7274-3b91-9f51-1961d60a4e09 | -3.58765 | -47.35036 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8681d4fe-80fa-3be1-be22-468006f59ef3 | -4.23494 | -47.56108 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 516f299b-b01b-3b6d-9c02-a7efb07e14f7 | -4.14961 | -46.57846 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adfa87c7-428d-36dc-8004-2a8f55c8f02a | -3.02785 | -48.03555 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00a236c3-efea-349c-a1e0-cf7b15917876 | -2.89628 | -49.37928 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbf5469c-523e-3d5c-bafb-ab23a9d0465d | -2.84354 | -49.44474 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50ca7b6b-7616-31d6-97ff-3a562487ae5c | -3.25658 | -48.74305 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f78a60b6-aa3c-3792-9c22-35bbb5468e13 | -3.77805 | -47.76345 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f75fcdee-99db-3584-a585-e0e249362da6 | -2.97581 | -50.29932 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 259ec6db-d203-30d3-898e-925c8f215c30 | -3.78883 | -51.29018 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c552765b-8d84-3d14-a578-6e1991d0551b | -3.97693 | -48.18817 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e66c4658-c2f6-365b-b848-6d81b6e87b8c | -8.14427 | -49.65801 | 2024-11-09 04:33:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c94dc67-867d-3fe7-bd7b-e93048de3572 | -3.97748 | -48.1847 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 29c2bff8-7ef7-3082-baac-9c86e85c7be7 | -2.83782 | -49.4361 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c9347d9c-e996-3d92-8bb8-840427c482ab | -3.57067 | -44.56069 | 2024-11-09 04:33:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0dc45b94-06ea-3659-bb91-4d76a4cd984e | -4.0997 | -48.51187 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 387f6ddc-a9f9-38e2-bd76-f74f4f700c9a | -2.61055 | -51.30377 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 565cc71a-f027-3b33-8371-2311c3f5e342 | -3.3385 | -46.65578 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a03f0687-8e63-3afc-8f8c-e3c605f12ee2 | -4.2098 | -48.54708 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a7391d6b-c2a7-3a51-a0c6-9ea35b5df7e3 | -2.6114 | -51.74393 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36226ac2-213a-38ec-bdca-4fc4968999a8 | -3.52066 | -51.24669 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab4b0d63-bf3a-3cfb-99ee-9d3d9ebb2fdc | -3.09754 | -53.32389 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e596f2d5-2ff1-35cf-980c-1c6dcb97f7f6 | -3.0834 | -49.57501 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d616f04-f2c9-3ad1-b4cf-746e1d612f43 | -5.63313 | -44.83301 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37be79ba-160d-32e0-884d-ce0eb0447c5a | -4.23993 | -47.57241 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4860ed27-7ff4-33b6-9bce-26f323d85a01 | -2.67621 | -51.81762 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| b0058967-9743-3a9a-8d30-42350391a339 | -3.06829 | -48.05962 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c758e0f6-f414-36fe-94cd-26f5f02a459d | -4.73171 | -48.98862 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75728644-5d00-3d74-a8cb-4757aa329b7c | -3.02282 | -53.87136 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd506ba3-cb62-3bba-b173-15dd273bc955 | -2.92771 | -48.66992 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8c5f993-48d0-3278-8917-d6e9d50367d3 | -2.86423 | -49.22459 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d60deb7d-fd15-3c98-84e4-1c4dd75c2073 | -3.63713 | -50.18271 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 211c53de-16d5-3ed0-80da-384e9992cb13 | -3.7519 | -52.40158 | 2024-11-09 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dba66a8-cf2f-3355-b994-f1a4762fd14e | -3.88656 | -52.39384 | 2024-11-09 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27a70864-5899-3e73-a120-99d2c9b81fb3 | -6.66225 | -47.10703 | 2024-11-09 04:33:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ad1ab2c-4dae-38c9-8ccd-a08099fc704f | -3.51993 | -51.25122 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c92640b-43ed-3926-9aae-b632d616b498 | -4.20591 | -48.55008 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 0f8f24db-3fef-3859-be24-be388803b194 | -3.05211 | -51.06634 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bab11a6-e73f-3a51-92b8-e58407e57304 | -4.18248 | -49.99083 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe53b2da-f613-33b4-a336-a6d7cfe38e76 | -4.2517 | -48.53904 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bb1693b2-2b4e-328c-82af-3da638d5084e | -3.11581 | -53.71191 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bfee539-72f2-32e2-8d30-b545575de864 | -4.11658 | -46.87943 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd683ff2-3e89-3bf5-b8db-ba8d640f72d0 | -2.71719 | -51.71178 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6b15958-d62c-3162-8afd-82b71fca7dcd | -4.94947 | -48.45181 | 2024-11-09 04:33:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de666553-7b6f-301d-8748-ceda108eb57f | -2.77076 | -51.60727 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf4bd65b-bec3-3902-97df-18bad39db890 | -5.73436 | -43.51192 | 2024-11-09 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 679f4d83-b741-30ee-82a9-79666231d09b | -6.24659 | -39.7109 | 2024-11-09 04:33:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 883264cf-3b1e-31f6-aca1-620e07c70f5c | -5.41295 | -47.13824 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b8888fa-34dd-3ea5-8907-f43c78a1e8a3 | -4.97168 | -46.49657 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40a17ab2-351c-30c5-a6fa-493b4ff004e6 | -4.51704 | -45.69392 | 2024-11-09 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 635d26b1-565b-30f6-92c1-5d960ba568e6 | -4.44006 | -43.64212 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c86c4aa-c5a9-32c6-9097-d4e8fe9c25e1 | -3.32649 | -49.09953 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90dbc032-490a-3d5a-a58b-eeccb0eee033 | -5.1136 | -37.56946 | 2024-11-09 04:33:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e8975b16-e18c-38b5-bf35-021911038642 | -2.68107 | -50.96304 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4bca723e-ac9e-3bbd-876f-6785acace481 | -3.25321 | -48.74253 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf789e79-4ae3-371b-974d-028100224371 | -2.92925 | -49.84158 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1eef2309-e029-369a-97d5-ead0f2d8d91f | -4.27025 | -47.0735 | 2024-11-09 04:33:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f23684fd-1124-3ac0-aca5-839f8d7b579a | -3.95363 | -48.16311 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f8ff4b13-9ab2-3dd6-8c0b-5e459a277659 | -3.57076 | -53.52833 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4888cff-2add-3060-8c62-c746d191e000 | -4.73617 | -49.00396 | 2024-11-09 04:33:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0749b214-1e40-39bc-8801-56054cbda461 | -3.50129 | -51.14387 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68ddc765-bb5a-331f-9d6b-107c05e15667 | -2.84262 | -49.82009 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04401ac4-d4ad-378c-ae50-82e705170771 | -2.24116 | -53.73197 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cae52c2-b4b2-3f98-8761-0c2d7ba27c96 | -2.78052 | -52.87057 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f45c88e-f466-3778-85a0-fbc470cae998 | -4.12974 | -46.86023 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6028adb5-6612-300d-bda9-d04f67ce5028 | -3.97377 | -46.41843 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c85f14d-efb1-3acd-8927-0c34e5f7a830 | -2.93051 | -48.67403 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b521cd8-d756-30d0-8110-5df26c862f1d | -6.18242 | -45.4401 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00c5718c-6ab5-3cb4-80b0-a00138ecbe42 | -2.93693 | -51.0587 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 167cf1c0-6b0a-373f-83ac-3a64f3f5b75c | -2.91927 | -49.36377 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 34f5c702-89d8-31bc-8171-ce07a95f3b24 | -4.22923 | -48.5321 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb988f33-88a2-3210-a0c4-c2ea65515572 | -3.44139 | -51.11154 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37df9c7a-4ebe-34ff-9224-6e81ea09a7e3 | -3.89305 | -50.23712 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d040bee1-64c3-31f5-8218-088acd6e9476 | -10.04424 | -50.58322 | 2024-11-09 04:33:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4683de8b-8336-3347-920b-d761bbfe7e64 | -5.33068 | -44.0332 | 2024-11-09 04:33:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19664bed-62ae-3ff1-8d81-48b2b5c39728 | -5.99871 | -46.09599 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96681dfa-0821-3810-89fa-99b3d7922832 | -3.26188 | -46.31596 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83ed9a77-2591-35e8-a31a-de9465e04bc1 | -3.59858 | -50.24257 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad0415a8-dcd1-341e-b525-70c8004c121e | -4.11392 | -46.10376 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe8392fc-b542-319d-9905-26c9722e76d5 | -2.86445 | -50.32658 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README62.md)
