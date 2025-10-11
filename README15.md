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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b72f26b4-0497-3bc2-8947-1845992c3995 | -13.24579 | -46.48143 | 2025-10-11 03:45:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ad34873-83ee-3d80-ab65-5c10e6d4b146 | -14.01134 | -47.06424 | 2025-10-11 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7bde56d-d8ad-3baa-a454-b0a09078eca8 | -16.32249 | -45.05939 | 2025-10-11 03:45:00 | NOAA-20 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 994ac173-54f5-3617-97c1-d2e811cf145b | -16.29551 | -43.08579 | 2025-10-11 03:45:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9753ea9-447a-3580-8bda-2c816a8adb36 | -13.24029 | -46.48035 | 2025-10-11 03:45:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34798f76-b0b1-3aed-a5b9-0407a46e5c34 | -14.98688 | -45.56499 | 2025-10-11 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33ba4bc0-a6da-328d-b5c2-4ba730a97c00 | -17.37138 | -46.65535 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49533c8d-f643-3d1c-8397-0fb1664558fc | -14.95465 | -46.75146 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f357fe4-06da-3329-81c8-891d44d11327 | -13.85539 | -45.8504 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e897aa32-8be5-34c5-9146-d8227f362f64 | -14.70405 | -47.44206 | 2025-10-11 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49c4606f-35b6-3159-ad8b-9e8703c2d677 | -16.59497 | -41.11412 | 2025-10-11 03:45:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f83d77ed-9a73-3bed-8787-5a48962b3077 | -13.48766 | -48.11591 | 2025-10-11 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bca97d76-8916-32bf-b225-79b232c3cff2 | -19.7416 | -43.52283 | 2025-10-11 03:45:00 | NOAA-20 | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3836e2a-4690-3ebc-b7a8-4904410762c3 | -15.00856 | -47.56981 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c1ea6be-ada0-39ee-a9dc-df00c111c06d | -17.38813 | -46.86309 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccfcc3e0-e4e5-31ad-aea2-83b3ff12bcbe | -18.13002 | -44.34215 | 2025-10-11 03:45:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58ae3b5d-e5b2-34a1-9361-622aab4ad667 | -15.6034 | -42.67157 | 2025-10-11 03:45:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b0d32db-a296-3848-b7b2-27dcc5aea193 | -17.49132 | -43.33282 | 2025-10-11 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| af7f4ffc-606b-3764-80c3-ab2e4040cb87 | -13.32383 | -47.13147 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c220d3f2-a86c-340b-a750-96da786882f0 | -14.74147 | -46.11577 | 2025-10-11 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4a9d467-54f4-3dde-8327-689034eaf263 | -13.31697 | -47.13021 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2052178a-af66-357d-930d-87a7c260ea2f | -14.94921 | -46.75051 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bf13b6c4-2ebe-3cd8-a845-c5573032b525 | -14.27856 | -45.90522 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1acb72c0-9654-3635-b416-7d4413b99d11 | -13.28524 | -47.1403 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23756d5d-7100-3770-bf9b-b9231ea46f69 | -12.74019 | -48.65773 | 2025-10-11 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f27a9659-131c-3f28-b80c-80411345af00 | -13.3011 | -48.49174 | 2025-10-11 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94c8d805-ddd6-3b10-a328-90b3fe7cf3e7 | -17.37004 | -46.66181 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dccd0860-1e2a-3145-a88a-c00d5b3ff2a9 | -13.8417 | -45.81017 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 806bbb1f-d46f-3bcb-9cde-60037f27dc69 | -16.1889 | -43.6683 | 2025-10-11 03:45:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ce3189f-f975-3907-a0e7-05b7d370816d | -20.46746 | -42.45023 | 2025-10-11 03:45:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bf0d443e-e484-3d6f-8407-f586c3c27501 | -13.30842 | -48.48769 | 2025-10-11 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 173baefe-289c-378f-b837-6b0dcdfba3bf | -14.70478 | -47.43856 | 2025-10-11 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a49ff28d-5b13-3b93-bdc3-42c0596fec6c | -14.92681 | -46.77176 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36c47286-815e-3015-8fbe-797e6b49b383 | -15.70553 | -46.63593 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c73d61a3-6b2c-3662-a225-40d0358aea33 | -13.25514 | -46.49199 | 2025-10-11 03:45:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e40a709e-1994-31d3-9726-6a333f8e0434 | -14.94293 | -46.74726 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 10076101-dd4d-3b99-bebf-d70774578fbb | -15.68946 | -46.64169 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3750a47a-3252-3e11-b2a1-23caacc79a66 | -14.93657 | -46.75097 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bbd5d726-e5b9-3eea-ac47-8c9db7d0c10a | -13.28613 | -47.13588 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dd35887-a55e-3c85-b692-3b3862898e9f | -15.64843 | -42.6499 | 2025-10-11 03:45:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60200dfe-f57e-3de8-a952-dd881ca26968 | -14.93171 | -46.75336 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 669c7d0b-c910-372f-89e9-82d3455b8ea7 | -14.93039 | -46.75374 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 562fd5a4-5c07-34bf-84a0-ef99244eefd1 | -17.64564 | -44.4303 | 2025-10-11 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90e2e8f8-c9b3-34f2-8e63-3e05f5845f08 | -17.20526 | -47.33572 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 325750a8-219e-3df0-80ae-9c10f0d32206 | -14.74531 | -46.12428 | 2025-10-11 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68f5ad78-a050-3bcc-84df-bc68131b9576 | -16.30177 | -47.17538 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 927d9357-848a-3fd3-89d1-6f0b3d616e93 | -13.24972 | -46.49052 | 2025-10-11 03:45:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| efd84c67-3dd9-3f34-9ea8-4deee93ede12 | -16.31022 | -47.16185 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab837065-feb6-3680-9bbd-62c30c550af1 | -13.29951 | -47.12841 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| edb5f247-68b2-37f7-b964-7a4f1e4a7103 | -15.06537 | -46.60504 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b19f2569-0262-350f-b682-b03612df8eb3 | -15.70597 | -46.64187 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af235a82-5d91-381e-ad49-1f0279f221c7 | -14.94436 | -46.74666 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c8dfef66-986a-30b6-8775-8adc92dfd7a1 | -14.94084 | -46.7578 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 48939f63-6bd2-3c79-8670-c0736a4e7aae | -17.38876 | -46.86 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fcfd338-cd07-3fa6-a5f3-8ee488c9e4a5 | -15.01359 | -47.5741 | 2025-10-11 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8acec6f0-d7cf-39da-9611-c12b1ef81075 | -15.12974 | -42.60126 | 2025-10-11 03:45:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 279cc29f-cad4-337a-acf1-7fbd5b944fa4 | -14.93653 | -46.75734 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34c2d8f9-e712-3dd2-821f-f6af6da3b184 | -15.70321 | -46.6281 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c7e48c1-c0d2-3176-92ef-725fb0a7477d | -13.79911 | -43.13289 | 2025-10-11 03:45:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c589d807-03cc-3dc6-82eb-312fd1061df2 | -15.31778 | -46.19295 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f3c3e1c-0382-3107-aa70-c5476ba38ee1 | -14.959 | -41.69468 | 2025-10-11 03:45:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cc4992b4-7e42-3bf4-8bc0-af1a2fec5ede | -16.59206 | -41.10901 | 2025-10-11 03:45:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| aeae6543-c9ef-3a9e-9293-93218b5de87f | -16.30405 | -47.16436 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2dd0d4c-825d-3778-96ad-8d1d69f8336b | -14.74086 | -46.11893 | 2025-10-11 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5decc97-26f4-3f7a-9638-9f0b3b9d4dd5 | -15.83052 | -42.02744 | 2025-10-11 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bd4ffc01-c0f1-3e61-8a68-aa6dbc8f903e | -14.74141 | -46.11675 | 2025-10-11 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d4653b3-14e3-32ed-b363-03a3478afe48 | -13.32568 | -47.12251 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b32f5a98-06c8-3172-be9e-ba001a719c96 | -15.70425 | -46.64209 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62e2ed99-0fe1-31c4-b890-57c9df0411d6 | -13.79482 | -45.39139 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e21c0f2e-e200-336a-bd55-046978cfee2d | -14.92954 | -46.76389 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b0fe121-d64d-38f8-a538-65e4aac2c611 | -12.74536 | -48.6646 | 2025-10-11 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| db064f50-3ff9-38b2-ab84-c99f2f2af71e | -14.93587 | -46.75452 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f5761a6c-2fa8-325d-88c0-cc75096b4191 | -13.40979 | -47.24045 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed6bd411-7137-3075-a523-6dac0917ee02 | -16.29625 | -43.08189 | 2025-10-11 03:45:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9783ee2e-c8a9-3069-ae13-6564640aa5e4 | -16.18764 | -43.66964 | 2025-10-11 03:45:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c92271cd-9f39-3d83-8502-f9a1afa6ebc3 | -14.95084 | -45.58885 | 2025-10-11 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6baed700-c073-3350-b644-73c31f084e1b | -14.01202 | -47.06092 | 2025-10-11 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3102ee18-7f2f-38bb-a8d1-cfb3e187dd64 | -13.81394 | -44.12774 | 2025-10-11 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e11feb9-d564-388e-bf00-1b39c2b8d243 | -15.90741 | -42.56351 | 2025-10-11 03:45:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f56a8e5c-9073-39e2-9bd0-0a33bbd6be76 | -18.13042 | -44.34093 | 2025-10-11 03:45:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52db43b1-5828-39fc-b228-78e47d39fdb1 | -17.21409 | -47.65359 | 2025-10-11 03:45:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d8e281e-90c4-3db4-bf74-0c76735c5f5a | -14.74077 | -46.11992 | 2025-10-11 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52f0a47c-b170-3b9c-8b12-41321eed2665 | -16.29508 | -43.08277 | 2025-10-11 03:45:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a56cbeb-67f0-342b-b1a2-a3bf53e3c000 | -13.8391 | -45.79607 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ac25b29-6456-3e60-a714-5c8984a53fe7 | -14.94619 | -45.59155 | 2025-10-11 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a91691e-9cfc-329b-88ca-7259bdcadb03 | -18.13395 | -44.3461 | 2025-10-11 03:45:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c7bdba9-0822-36b9-bd18-8428e8a0605a | -17.6704 | -46.81476 | 2025-10-11 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64940d6c-267c-3e71-96bc-8bb855145757 | -14.92879 | -46.76756 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aa8a142-a7da-3364-ba20-855c17724c14 | -14.14704 | -43.9976 | 2025-10-11 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c89fe4f-8f6b-3dbb-96e8-4ea48bf95257 | -15.67968 | -48.13277 | 2025-10-11 03:45:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e99daacb-fd9c-306b-877d-9593b5a85b7e | -22.54488 | -52.05579 | 2025-10-11 03:47:00 | NOAA-20 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ae0b6975-3402-3b24-876a-aaf4bca4fadb | -22.54013 | -52.0512 | 2025-10-11 03:47:00 | NOAA-20 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7f642dcc-c515-36dd-a592-80b344ca920c | -22.54653 | -52.05274 | 2025-10-11 03:47:00 | NOAA-20 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7a49c35b-b8d9-3fa2-a491-5f140de99ad2 | -13.2252 | -42.3414 | 2025-10-11 03:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 334.1 |
| f5d46fa1-08e8-3e69-95dc-993e9eab67f7 | -13.2257 | -42.317 | 2025-10-11 03:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 131.9 |
| 1a88245a-fde0-3496-9fca-a17b27acaebc | -8.1996 | -43.3189 | 2025-10-11 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 2ea8e35c-77ac-3680-a6df-822d23059e6a | -17.2722 | -46.8932 | 2025-10-11 03:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 04a54361-9d03-394c-9a2e-85b7b0e05a4b | -13.2057 | -42.345 | 2025-10-11 03:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 260.1 |
| c8e318e7-ee72-335f-bbe9-d91ea4e4c3cc | -13.2062 | -42.3206 | 2025-10-11 03:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 103.1 |
| c5217528-8802-359b-8912-9674d238692d | -10.5274 | -47.3601 | 2025-10-11 04:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |


[Clique aqui para ver as próximas entradas](README16.md)
