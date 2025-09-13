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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff24e50a-4f6c-3516-bc1a-ac58de3601a3 | -11.8284 | -50.5406 | 2025-09-13 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d80874a9-aaa3-3363-89c2-e4c15cef6887 | -14.1694 | -46.2965 | 2025-09-13 10:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 130.8 |
| aa5fd180-d264-38a3-8a1c-2f5988a7799a | -9.2658 | -59.3997 | 2025-09-13 10:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 0fd44971-80dc-35c8-8b79-2509c4040b40 | -14.2083 | -46.2899 | 2025-09-13 10:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 4604eff7-dcf3-30ec-b147-afc81e0a0f35 | -14.1698 | -46.2735 | 2025-09-13 10:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 225.2 |
| a15f1ad4-a407-30e9-ba9e-a7a6520197c3 | -11.8284 | -50.5406 | 2025-09-13 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 818a0bc4-e7cc-3367-904b-f1ebd20674a6 | -11.8478 | -50.517 | 2025-09-13 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 3117ce2b-27ec-3d1a-b7b2-c188ffa08bc4 | -14.1893 | -46.2702 | 2025-09-13 10:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| fe3444eb-1d60-3c63-a7f0-45ef9fdaf873 | -14.2083 | -46.2899 | 2025-09-13 10:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 380.1 |
| 9e0901eb-beee-34ed-8293-885705b1cf84 | -14.29 | -46.0924 | 2025-09-13 10:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 41b444bc-33e0-397d-ac6f-3a601db0e00b | -14.2273 | -46.3096 | 2025-09-13 10:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 66fc6a84-76f1-35d7-9529-ff8b79b74fbf | -14.1698 | -46.2735 | 2025-09-13 10:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 150.3 |
| e2940a73-52e8-332f-9d23-2473766b0b08 | -11.7903 | -50.545 | 2025-09-13 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.2 |
| d55bf5b7-6837-318b-9dc9-ead3d95e6a79 | -11.8094 | -50.5428 | 2025-09-13 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 213.5 |
| d457f1f2-2ba3-3e2e-8bf6-2c40b1bcca5e | -14.2078 | -46.3129 | 2025-09-13 10:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 231.0 |
| 00eba042-1eb8-39ed-9c54-1d8163490933 | -14.8712 | -49.0173 | 2025-09-13 10:50:00 | GOES-19 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 655c4af3-2bc4-366b-acb5-e6c729bc0544 | -14.3095 | -46.089 | 2025-09-13 10:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 181.0 |
| d41c1d8f-2835-3441-bde4-c62183918e6c | -11.8475 | -50.5384 | 2025-09-13 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| d767fdb1-6a37-3f87-97bf-94aa894a1247 | -14.2277 | -46.2866 | 2025-09-13 10:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| cddb67aa-95c9-33c8-9665-f25841ed25f9 | -13.2222 | -51.7382 | 2025-09-13 10:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 192.1 |
| ed948070-60a4-397a-b92f-dd065494b9ce | -11.8097 | -50.5214 | 2025-09-13 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 3fbbb3c9-c4ed-30ac-ba3f-d798258bb15d | -14.8708 | -49.0395 | 2025-09-13 10:50:00 | GOES-19 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 142.6 |
| ca1c56f4-0fc3-3784-94fd-c5a351f6dbb5 | -14.2277 | -46.2866 | 2025-09-13 11:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 197.9 |
| b058ed2b-eaed-3ac6-8861-872f8ff55eb4 | -12.8263 | -47.9263 | 2025-09-13 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| ca21262b-ee9c-3022-b682-a5a4a010d8f5 | -11.8284 | -50.5406 | 2025-09-13 11:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 8d0ce610-634a-39d1-9eb7-4277941befa0 | -9.2658 | -59.3997 | 2025-09-13 11:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| fbd3f6a4-0cba-38d5-87f3-187fa32ae0e5 | -11.8094 | -50.5428 | 2025-09-13 11:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 575709a6-e82e-3eff-a7ea-cb9a371f183f | -14.2273 | -46.3096 | 2025-09-13 11:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 14445285-d357-328e-9b65-73d34b0818da | -14.1698 | -46.2735 | 2025-09-13 11:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| a529a777-4630-362c-bd6d-96831c711f51 | -11.7903 | -50.545 | 2025-09-13 11:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| d73da18f-50cc-364f-a512-490d25e0156c | -11.8475 | -50.5384 | 2025-09-13 11:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| b6cda9d2-718b-3d61-9c9f-4030299119a8 | -10.9283 | -47.2223 | 2025-09-13 11:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 546aa99e-3b21-36c7-9680-6d4ab0e4622d | -14.2083 | -46.2899 | 2025-09-13 11:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 281.0 |
| 7cb6ee96-1a3b-3149-bc96-d5b17e39dc82 | -14.2078 | -46.3129 | 2025-09-13 11:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 165.6 |
| b1b0419c-b2a6-3fd9-9c59-67db82a5e8b8 | -11.8475 | -50.5384 | 2025-09-13 11:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| bb000087-0c13-3fc5-84b2-a7b230743b7a | -11.8284 | -50.5406 | 2025-09-13 11:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 855c67bb-d3dc-38fc-9f62-fddfb4480c32 | -14.29 | -46.0924 | 2025-09-13 11:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 1f11f918-1a08-3aae-995d-25db548fa14f | -12.8263 | -47.9263 | 2025-09-13 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| a7d1c9b7-ab30-32d5-b628-be6e2095b03d | -15.0672 | -47.9823 | 2025-09-13 11:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 415f14d9-ee2a-379e-8963-cd68b867ec2b | -15.0477 | -47.9856 | 2025-09-13 11:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 165.5 |
| c3cad9ea-43c0-3307-ab44-da020d543ffc | -9.2658 | -59.3997 | 2025-09-13 11:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 5c06178d-5591-31fb-adbc-9a56cca773a8 | -11.8094 | -50.5428 | 2025-09-13 11:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 227.4 |
| 4c27f46d-6c48-3029-aad6-77675b869bf7 | -11.7903 | -50.545 | 2025-09-13 11:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 30de0d89-4c3a-33fb-8461-1d0fa71cc6e8 | -12.8259 | -47.9486 | 2025-09-13 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| c20bac33-8471-325b-b72a-9fec42d9158b | -11.7204 | -46.5579 | 2025-09-13 11:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| ddc1cdcf-b64d-3624-9250-c0a9bc16f87c | -11.7391 | -46.5779 | 2025-09-13 11:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| b1632de0-b546-3aff-ae42-d55ac09b77e9 | -9.2658 | -59.3997 | 2025-09-13 11:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 884c91af-b586-37c9-ab8f-53ef32a7efdf | -15.8648 | -47.2322 | 2025-09-13 11:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7c7ec117-190e-375a-98db-2d9aa9a08dc0 | -15.0477 | -47.9856 | 2025-09-13 11:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 294.8 |
| 8ec7eb51-ac4a-3064-a04f-158adee7c33d | -11.8094 | -50.5428 | 2025-09-13 11:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 233.2 |
| 39c1b166-c3df-3930-ab02-0d827e04afde | -10.9283 | -47.2223 | 2025-09-13 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 3897f33d-cbf7-3eb4-8d02-869912407ae7 | -11.7391 | -46.5779 | 2025-09-13 11:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 5dda89d3-06d1-3084-9217-7211ce4ae722 | -11.7903 | -50.545 | 2025-09-13 11:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| cf0045fe-acc7-34aa-b9ee-8d01968d669b | -11.8284 | -50.5406 | 2025-09-13 11:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 38b6469e-9241-30a1-9eca-ecca4dda4174 | -14.29 | -46.0924 | 2025-09-13 11:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 139d4796-494d-3306-bb7a-ae761e47d285 | -12.8263 | -47.9263 | 2025-09-13 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 48f726b8-2801-34a1-8b74-30b1a150d371 | -12.8456 | -47.9236 | 2025-09-13 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| aa2750c3-db34-33ed-bca6-d29cdd9a0d76 | -14.29 | -46.0924 | 2025-09-13 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 5e38fe55-2955-3ba4-aa8c-9bb30a76f567 | -12.9402 | -47.9991 | 2025-09-13 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 597cc0e8-10bc-3c7a-a65a-c96d468b3db3 | -15.4713 | -47.3256 | 2025-09-13 11:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 2e5de132-1b89-3ab3-b02e-d79fbcd33e79 | -11.8094 | -50.5428 | 2025-09-13 11:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 200.2 |
| efce348c-b95d-33da-a48c-44629cc1bae7 | -12.8259 | -47.9486 | 2025-09-13 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e332599e-1d1c-3a48-9b3c-3a29b7715f75 | -16.4527 | -49.044 | 2025-09-13 11:30:00 | GOES-19 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 00e65622-56a8-3197-b121-a21554dc4268 | -16.433 | -49.0474 | 2025-09-13 11:30:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| a34c882a-a1a6-3b5a-8d99-dfdf18729b9c | -15.8648 | -47.2322 | 2025-09-13 11:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d2bc4fd0-7014-3883-8687-def1c05fc30a | -15.0477 | -47.9856 | 2025-09-13 11:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 0a71ab9b-17d8-3291-8e3d-39c059c7b65a | -15.4517 | -47.3291 | 2025-09-13 11:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 9be077f1-db04-3f2c-92e1-374ce0f870b7 | -12.8263 | -47.9263 | 2025-09-13 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 3da883df-6741-3a30-87f1-1171957d863b | -4.3667 | -38.72051 | 2025-09-13 11:36:00 | TERRA_M-M | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 8c9169a6-a53c-36a0-8887-b1f201108c8a | -10.05601 | -39.47087 | 2025-09-13 11:36:00 | TERRA_M-M | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| df1949a2-73ac-3e6d-ba51-526eafe81628 | -7.12958 | -38.55552 | 2025-09-13 11:36:00 | TERRA_M-M | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| cc805dee-978c-3c59-bc1d-6dcd9e73666f | -7.60109 | -44.68531 | 2025-09-13 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 44a44613-6dac-3e4a-85fc-f168aeec15ff | -7.86571 | -38.13757 | 2025-09-13 11:36:00 | TERRA_M-M | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 1ae81a16-6ff6-32c0-ae4a-ebcbe500c965 | -5.24812 | -40.83803 | 2025-09-13 11:36:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 51.0 |
| 968979c9-6b4d-3a35-8af3-73fea09a301f | -7.86433 | -38.14693 | 2025-09-13 11:36:00 | TERRA_M-M | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c4f3035b-e298-30eb-ba11-68281c428b05 | -7.6912 | -45.16451 | 2025-09-13 11:36:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 9ee81ea4-c79f-3d54-968d-8f6d0ba220dc | -7.39545 | -44.3435 | 2025-09-13 11:36:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| bbdda69d-a8b3-376f-806b-5795d8b9c3d4 | -5.25028 | -40.82373 | 2025-09-13 11:36:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 6566c8a5-d799-3a1f-b5da-5427b0ededff | -7.52982 | -44.37781 | 2025-09-13 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 393a971e-090c-3dff-ae37-280c15a111d6 | -7.42912 | -44.43277 | 2025-09-13 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e0b4e626-a2e6-365f-b930-cf5bb82b5777 | -7.5267 | -44.36998 | 2025-09-13 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| f41d68ee-8636-3463-82b3-8120c89b3849 | -8.95269 | -44.45206 | 2025-09-13 11:36:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 1821e800-d487-3959-8b29-a7c7479f7049 | -7.55204 | -35.12251 | 2025-09-13 11:36:00 | TERRA_M-M | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| f221bc78-bbc4-393a-83a7-ca189268e95e | -7.43333 | -44.40698 | 2025-09-13 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.5 |
| c3253823-d7c7-34dc-b26d-6a373e92cb29 | -7.21578 | -43.82942 | 2025-09-13 11:36:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 6619fe86-819c-3f99-a274-de8e47b70d63 | -7.39897 | -44.35001 | 2025-09-13 11:36:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 7dfe9e75-9468-3040-8b43-7cfdfc9a4067 | -10.63639 | -39.42049 | 2025-09-13 11:36:00 | TERRA_M-M | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| a052c247-5569-3ad6-8498-5b891ed77d85 | -11.72301 | -46.55132 | 2025-09-13 11:38:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 0c961fc4-81c6-376d-b69b-2e2303aa2af3 | -10.66243 | -46.2928 | 2025-09-13 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 3de5ed85-c042-3e8f-8afe-9d3f4b78ee35 | -13.99531 | -44.7832 | 2025-09-13 11:38:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 93855790-8478-3c71-96ea-e63fcd99cb7b | -14.16512 | -46.16039 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6bd96ea8-b075-3da8-9f7a-51fe24e572d0 | -14.82588 | -40.92954 | 2025-09-13 11:38:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 9a1d1a73-104b-3f72-8953-b2e79dec9e5e | -16.32528 | -43.09272 | 2025-09-13 11:38:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e88b0d16-9276-3551-8496-ed47db8a03ed | -16.3216 | -42.29343 | 2025-09-13 11:38:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| d909d17f-85cc-3081-a7db-1a635041f308 | -15.45408 | -47.34106 | 2025-09-13 11:38:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 7d5981b0-4eca-3648-b282-df858df920f7 | -14.16699 | -46.24879 | 2025-09-13 11:38:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 4db57cec-4225-3062-99ad-cef8d7ff4c5f | -14.29969 | -46.08521 | 2025-09-13 11:38:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 79121083-e28a-3900-970c-e11e4ef6a582 | -16.32118 | -42.31234 | 2025-09-13 11:38:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.1 |
| 7e051d92-710d-3a53-aaa4-82fee6bf1481 | -12.84227 | -47.93275 | 2025-09-13 11:38:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 233.2 |
| 1a14a596-b178-3238-a76e-5ad13b86c088 | -13.23573 | -43.75751 | 2025-09-13 11:38:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |


[Clique aqui para ver as próximas entradas](README121.md)
