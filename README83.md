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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 589d3ef1-bc07-325f-ba27-3f073e4c2ad7 | -12.8055 | -48.0182 | 2025-09-07 07:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| f5df2b62-cc24-36d8-8d62-2410bac1fe9f | -12.9482 | -54.7519 | 2025-09-07 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a705dc02-2b51-3c14-b7d4-ff9daa5a4e5f | -13.8407 | -46.2598 | 2025-09-07 07:10:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 194e7b74-6afb-3533-9a15-39e458a9e264 | -12.948 | -54.7724 | 2025-09-07 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 172.0 |
| cf1d38d2-4fd2-3b4e-91bf-be2b4a75b726 | -12.8055 | -48.0182 | 2025-09-07 07:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 4ba675fb-d740-3d38-9bc1-f3b79d34f090 | -12.9289 | -54.7744 | 2025-09-07 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 27c475a0-8b05-341e-af2d-5706c555d2c1 | -11.3198 | -46.5444 | 2025-09-07 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| f51b2a6c-197c-3e19-bd93-dd705ce09d86 | -12.9292 | -54.7538 | 2025-09-07 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fa2a416f-2f0b-3419-b77d-6028df440bec | -12.9482 | -54.7519 | 2025-09-07 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| f585414c-e7d9-3f17-b926-25279395e79f | -12.948 | -54.7724 | 2025-09-07 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 136.9 |
| f7aea886-0042-38b1-a34c-47033791a757 | -19.4898 | -47.7646 | 2025-09-07 07:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| ddb9f5a0-e899-3424-85c0-6cb7afdafb0f | -19.4695 | -47.7691 | 2025-09-07 07:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1c376bd9-3371-3bf5-b8c7-9f56a83c2bc6 | -12.9289 | -54.7744 | 2025-09-07 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| e7a5bdf9-804c-3204-956d-7f01f9e72e32 | -12.9482 | -54.7519 | 2025-09-07 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| adb7611a-4ba1-3148-af96-1563a59233d2 | -12.9292 | -54.7538 | 2025-09-07 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 8a55ae66-d97c-3064-b579-8a9279d6bbe6 | -19.4898 | -47.7646 | 2025-09-07 07:30:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f802b204-df00-3938-b9ef-cfdfeea9546e | -12.948 | -54.7724 | 2025-09-07 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 077b4eb1-e3ce-3eac-98f9-f505e4e2d0de | -12.8055 | -48.0182 | 2025-09-07 07:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 92d83bc1-c90f-389c-9ce0-f2d15585e33d | -19.4695 | -47.7691 | 2025-09-07 07:30:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 00996479-841e-3040-8a87-7597f68adf37 | -19.4891 | -47.7879 | 2025-09-07 07:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 2a005894-2459-31c2-8c4a-a916f87057f5 | -12.9289 | -54.7744 | 2025-09-07 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6c1b92e9-6d3b-3f76-8479-3a8bf7bcfc6f | -12.948 | -54.7724 | 2025-09-07 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 7ff689c6-42c3-3364-af9f-7563410cfbb6 | -12.9289 | -54.7744 | 2025-09-07 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| a346cd14-383e-3447-b6ae-182242e3f101 | -12.8055 | -48.0182 | 2025-09-07 07:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| a9cccf65-2d0b-3440-b445-0a6bbc582be2 | -12.8059 | -47.9959 | 2025-09-07 07:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 1379a022-b3f9-3fa6-8b83-7ede6ffd18b2 | -12.9289 | -54.7744 | 2025-09-07 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 7c0d7f6e-c640-3be4-b6bf-ffb5658206fa | -12.948 | -54.7724 | 2025-09-07 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 50aba493-a8d8-36d1-9659-9e876298a69c | -12.8055 | -48.0182 | 2025-09-07 07:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 23c789bd-d783-383b-b49b-2647da8316b4 | -12.9482 | -54.7519 | 2025-09-07 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 76f35230-d11f-3cda-8476-80af8c9461f3 | -12.9289 | -54.7744 | 2025-09-07 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| e62d6e9e-627f-3a9e-bcdb-67526f243419 | -12.9482 | -54.7519 | 2025-09-07 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| a346eac4-22e9-3d3e-bc34-1d9fdced4dbe | -12.948 | -54.7724 | 2025-09-07 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 7a8ef44c-c110-3554-b042-d1953f65d369 | -12.8055 | -48.0182 | 2025-09-07 08:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b9dd17e0-e34a-32ce-857d-ff1c3af448a1 | -12.9289 | -54.7744 | 2025-09-07 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 750a6849-d2a7-3e47-885f-5f17f0b9f623 | -12.9482 | -54.7519 | 2025-09-07 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 0503d10f-2d15-3413-a54e-ed89f93f5dce | -12.948 | -54.7724 | 2025-09-07 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 8ba812e2-cc51-3eb5-b4f7-ffe548533f26 | -12.948 | -54.7724 | 2025-09-07 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| f8eb7ef0-44cb-39fb-b61e-2da607c54b6e | -12.9482 | -54.7519 | 2025-09-07 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 8f81f614-6d31-3412-bdd7-26ca05e7c90b | -12.9289 | -54.7744 | 2025-09-07 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 43fb9e81-1307-3466-b007-1f1ce4a60d6b | -12.948 | -54.7724 | 2025-09-07 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 1f917e6f-7b4d-37ed-bc3c-d2c0c7837da6 | -10.5869 | -48.4772 | 2025-09-07 08:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 89d9628b-2a34-305a-86c3-a82cf7384de9 | -12.9289 | -54.7744 | 2025-09-07 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 0e9fa113-deb1-385e-8ade-caedb7ab0732 | -22.4068 | -47.4401 | 2025-09-07 08:30:00 | GOES-19 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| 7535982b-4a85-335d-9d21-771b3b760e58 | -12.9482 | -54.7519 | 2025-09-07 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 437a56cf-0d23-38cd-9efa-731ce763139f | -12.9482 | -54.7519 | 2025-09-07 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 57607cc1-bb61-346e-b9ce-459bc7b23efe | -12.9289 | -54.7744 | 2025-09-07 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| e0c96825-6b62-3089-aeb2-353c3bc29f3c | -12.948 | -54.7724 | 2025-09-07 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 606a45ef-1147-3d0a-b55a-3b29b6ed2fed | -8.6912 | -54.6682 | 2025-09-07 08:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 6d56905b-d854-3b97-afc0-054573ad6b21 | -8.6725 | -54.6695 | 2025-09-07 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c32985a7-a6a0-39dd-9bb4-627731c3cb7d | -8.691 | -54.6884 | 2025-09-07 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4ae2e6f4-ee4e-32a3-a6b8-fca4fa301d28 | -8.6912 | -54.6682 | 2025-09-07 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 330.6 |
| 68245a9c-3f23-3bd5-96ec-631221efc3d6 | -8.7098 | -54.6669 | 2025-09-07 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| ffe54694-14d3-3d48-99c9-9202ce7d2f36 | -12.9289 | -54.7744 | 2025-09-07 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f324a1ee-51ba-3304-8d2b-7a5610f0e934 | -12.948 | -54.7724 | 2025-09-07 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 8141965e-6cd2-3542-b38c-745a08b7cc60 | -8.7096 | -54.6871 | 2025-09-07 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 757701dc-8cd7-3890-afd4-754af08a2c18 | -12.9482 | -54.7519 | 2025-09-07 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| fd44bd65-543e-3338-b270-f123e91ae7fd | -8.6913 | -54.648 | 2025-09-07 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 45081088-dd14-3db9-8979-024f1028a6fc | -12.948 | -54.7724 | 2025-09-07 09:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 864632e6-c92f-3b43-96b6-091909d450ab | -8.6913 | -54.648 | 2025-09-07 09:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 1e1fef74-7065-321c-878a-0bc0f4c6cb16 | -8.6912 | -54.6682 | 2025-09-07 09:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 686adf1c-36bf-3e28-8f9e-a62b0771b868 | -12.9289 | -54.7744 | 2025-09-07 09:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| cc7d61b9-b1c4-399f-8e93-8a168dc0a1c0 | -12.9482 | -54.7519 | 2025-09-07 09:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 59493e39-a789-3f2c-9fe5-753b7d69a774 | -8.6912 | -54.6682 | 2025-09-07 09:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 12100a02-f250-327d-ab04-b181f7850a6c | -8.6913 | -54.648 | 2025-09-07 09:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 0be4a182-e336-3ef6-b0dc-f943055e9e02 | -8.6725 | -54.6695 | 2025-09-07 09:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 5325d535-0e73-3aab-8b86-d883088eebb3 | -8.6912 | -54.6682 | 2025-09-07 09:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 231.5 |
| dc106c19-c23f-3ec4-ba78-0be2acbc2032 | -8.6912 | -54.6682 | 2025-09-07 10:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 187.4 |
| b9f8d272-ef17-33b2-86b3-5a56bc221864 | -8.6913 | -54.648 | 2025-09-07 10:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 8dfbf5a1-38fc-39d2-8977-2340f012d5b7 | -8.6912 | -54.6682 | 2025-09-07 10:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 266.1 |
| 477385ac-440b-32c6-9af5-21bb03358e90 | -14.4882 | -48.7671 | 2025-09-07 10:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 63e7d670-ff68-35e8-8e01-601706c2a921 | -8.6913 | -54.648 | 2025-09-07 10:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 7fee9fa7-08d5-328e-ba6e-13b43786e04b | -14.4877 | -48.7893 | 2025-09-07 10:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 6f8bfbc0-c021-351d-b1a7-a55d051f78c1 | -10.6059 | -48.475 | 2025-09-07 10:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 91aa90f5-55cd-32d0-8305-5fd5b4a5766e | -14.4882 | -48.7671 | 2025-09-07 10:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 0637d1a6-4784-31de-8350-9a220a867b9c | -8.6912 | -54.6682 | 2025-09-07 10:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| bf283a7b-9314-3f55-8955-4acb69cf6c85 | -8.6912 | -54.6682 | 2025-09-07 10:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 268738e0-ca89-346d-9177-6ec3c50870a5 | -14.4882 | -48.7671 | 2025-09-07 10:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 1d91969c-4aff-38d6-b635-37b1f94be474 | -5.8793 | -43.9538 | 2025-09-07 10:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 8c6fada8-4eea-33ab-930c-4aad79dfbc60 | -14.4877 | -48.7893 | 2025-09-07 10:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 0dfebb82-505b-3354-9675-557278350855 | -10.6059 | -48.475 | 2025-09-07 10:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| ce41232a-5902-347d-90a5-4355fb52a644 | -10.6059 | -48.475 | 2025-09-07 10:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| b7bb59f2-cb2b-37b3-891b-d1f918db6249 | -5.9899 | -44.1528 | 2025-09-07 10:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 9c12d7fe-6a54-3418-bd37-3bb1fae2cff3 | -14.4877 | -48.7893 | 2025-09-07 10:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| a425d887-6cdb-3aed-8bae-57602dcde7e4 | -14.4882 | -48.7671 | 2025-09-07 10:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| c82d4f76-c5eb-3750-8642-cc87223fa410 | -14.4882 | -48.7671 | 2025-09-07 10:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 963f8bb1-fdbe-39d5-a433-bf5872eff81e | -12.8248 | -48.0155 | 2025-09-07 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c4bf49d2-6e81-3313-a96c-96af347ad7e3 | -19.4891 | -47.7879 | 2025-09-07 10:50:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 19673f91-be88-34dd-a08e-3973f8bf47c8 | -14.4877 | -48.7893 | 2025-09-07 10:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 85956bc0-89fd-3074-9a3b-8f921c91b777 | -19.4898 | -47.7646 | 2025-09-07 10:50:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 2ec14adc-accc-326c-893a-52848ee0f333 | -5.9899 | -44.1528 | 2025-09-07 10:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 7e078cb0-a284-383a-8c6a-8e8d3ab669c1 | -5.80793 | -36.63618 | 2025-09-07 10:58:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 3799cac2-2306-3c39-8bd5-b029271a4da9 | -5.79045 | -36.63346 | 2025-09-07 10:58:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 41.8 |
| f4fd4c6e-c0e0-3bbe-9067-7776344f8870 | -12.8248 | -48.0155 | 2025-09-07 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 73df5d72-4d53-39a5-b469-c927a7843cf2 | -19.4898 | -47.7646 | 2025-09-07 11:00:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 68267d00-9b2e-31fa-9e07-fe266f65a640 | -14.4882 | -48.7671 | 2025-09-07 11:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 118.4 |
| e38e809a-23b6-3c78-afe8-b5078c340e24 | -5.9899 | -44.1528 | 2025-09-07 11:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 3f565ffd-8126-35cb-83e0-8a45603f7847 | -19.4891 | -47.7879 | 2025-09-07 11:00:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 428.9 |
| 226c5c5c-7eb9-3ce9-807e-82ff3032f5f5 | -5.9899 | -44.1528 | 2025-09-07 11:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 231.9 |
| 4fcbebe2-9dd0-33fe-b489-73b8121049ab | -19.4891 | -47.7879 | 2025-09-07 11:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 90ab277c-39bb-367b-9ccb-f099bdc646c2 | -14.4882 | -48.7671 | 2025-09-07 11:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 172.7 |


[Clique aqui para ver as próximas entradas](README84.md)
