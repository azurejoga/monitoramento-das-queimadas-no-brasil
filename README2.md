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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49d92cf4-2a15-3f62-a6be-731bf5805a15 | -16.16561 | -58.49976 | 2026-05-07 01:11:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.1 |
| 7f0a46de-ce07-389a-83a8-6215d33bc8fe | -12.76748 | -59.00214 | 2026-05-07 01:11:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4127ff28-12ef-3688-8035-b11ea8ec5f75 | -12.50124 | -58.48061 | 2026-05-07 01:11:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| cc438278-f23c-3c8b-9a9d-456d0a6d3b74 | -12.49893 | -58.46598 | 2026-05-07 01:11:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4862e9f2-788a-3fc1-b4c9-5837903973ee | -16.1671 | -58.49285 | 2026-05-07 01:11:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.5 |
| 7c6f3d88-2a6f-3d81-92e5-8a1bd74fcf92 | -16.16357 | -58.487 | 2026-05-07 01:11:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.9 |
| f2da2319-8e3e-3332-9709-74d35668d4a6 | -12.49027 | -58.48242 | 2026-05-07 01:11:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 39e84f99-3775-319a-8f70-1cd09babb743 | -12.77797 | -59.00038 | 2026-05-07 01:11:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| f78cb6b1-089c-3e81-896d-8d3fae689133 | -12.78 | -59.0135 | 2026-05-07 01:11:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| ca21ef6d-f33b-3c43-9a5b-810b969f2859 | -21.715 | -48.4126 | 2026-05-07 03:20:00 | GOES-19 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 81c333fe-d79b-33b8-953f-ad113d8ac550 | -8.16413 | -35.80432 | 2026-05-07 03:25:00 | NPP-375D | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 79c1ec78-236a-35f8-a0aa-c4ae352bb7de | -10.55428 | -42.43706 | 2026-05-07 03:25:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 73a607a9-1c8e-304d-a01f-10b7d23ec7eb | -8.90442 | -36.90172 | 2026-05-07 03:25:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 736b2d91-4f99-3bf2-bedf-93e958f4cca2 | -9.2501 | -40.24186 | 2026-05-07 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 189f0366-2a4a-3bf9-896d-eb3c827f09db | -10.55538 | -42.43161 | 2026-05-07 03:25:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 15ddc843-608a-34b0-b77b-bab99d16312d | -12.85038 | -43.75681 | 2026-05-07 03:28:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb3deec4-1891-35e7-8596-ad7bbc6d3426 | -11.79151 | -43.63512 | 2026-05-07 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2f82465-875e-3650-9255-46fce44f8834 | -12.86516 | -43.75362 | 2026-05-07 03:28:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ede9e7b4-8c61-3fa5-b28d-5722b3c085b1 | -12.86387 | -43.75972 | 2026-05-07 03:28:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a23ce569-85cc-36dd-ac73-1970ad0c9770 | -11.7834 | -43.63979 | 2026-05-07 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d8c5b50-728e-3e6d-8bb9-438a0d40dcf8 | -12.85713 | -43.75827 | 2026-05-07 03:28:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7654ba01-1e2f-3ef5-b6c5-00fa3700d189 | -20.23184 | -46.85152 | 2026-05-07 03:30:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72939e50-7dc5-3f3c-96e8-64a00b5329d7 | -20.22547 | -46.84727 | 2026-05-07 03:30:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 731003e7-48b2-3356-b616-e9fed191a8e9 | -20.22954 | -46.84984 | 2026-05-07 03:30:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f9d6c63-5fc1-36f5-903b-96250d820377 | -8.22048 | -36.11502 | 2026-05-07 03:45:00 | NOAA-20 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f37b22b3-fc01-3eb0-ada1-3272417f0e7b | -5.7751 | -45.12512 | 2026-05-07 03:45:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ed5b777-48ac-3c5f-aec1-d99962f749fd | -5.77439 | -45.12912 | 2026-05-07 03:45:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd185adc-d765-3ec3-83b0-a7b64e5fd30b | -8.9087 | -37.34354 | 2026-05-07 03:45:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b27f85c2-3817-33d4-a8ae-b5fa8a8d1018 | -8.90316 | -36.89962 | 2026-05-07 03:45:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a91df4a2-1458-3805-a7a2-bd87070cdeb1 | -5.7758 | -45.12114 | 2026-05-07 03:45:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eef4d352-77f6-3b0e-9ac3-bbd3e3c906ef | -5.53276 | -35.52052 | 2026-05-07 03:45:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6605db02-bc9d-3ca3-85a2-d22e6ae1a8b5 | -6.01992 | -35.49113 | 2026-05-07 03:45:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 23248289-4d14-32b3-ae73-a6fdea8253ad | -8.84327 | -36.55433 | 2026-05-07 03:45:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9de639bc-7f98-36b5-82a8-5988296d12ff | -8.35038 | -36.30126 | 2026-05-07 03:45:00 | NOAA-20 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6cfe548b-5099-367a-9cd6-c5bc5aa7a821 | -7.3653 | -39.75383 | 2026-05-07 03:45:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e7dc744e-d031-3797-9540-d386cb78f5cd | -19.13445 | -44.6202 | 2026-05-07 03:47:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 047ed091-ef8b-3bae-89ec-f76b890aa99a | -14.8583 | -48.56303 | 2026-05-07 03:47:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d8c7144b-3888-3ce5-aeb1-9e4edf71e764 | -11.79258 | -43.63268 | 2026-05-07 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1fda464-1905-3dc3-a9f6-c65bb3646b3a | -19.1333 | -44.62129 | 2026-05-07 03:47:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01b50c85-9dfb-393d-9e0f-28e2938b08d2 | -12.27433 | -43.55034 | 2026-05-07 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3bc561c-5441-31ed-9d13-9a679c419201 | -13.95361 | -47.5523 | 2026-05-07 03:47:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f8becef-c449-3173-97bf-d114ddf6536a | -15.83801 | -39.18393 | 2026-05-07 03:47:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8607ec03-e5c5-31e4-a353-79690a131f5d | -14.90032 | -45.18103 | 2026-05-07 03:47:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc98ce04-dc2b-3603-a8d3-19f167cff54f | -11.61775 | -48.05509 | 2026-05-07 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 323b57fd-e23d-3448-b90e-afa5268a1fae | -14.13259 | -45.34498 | 2026-05-07 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82d19ff0-50b3-3156-9e7e-4ef1a3bcf4ae | -10.63915 | -48.00879 | 2026-05-07 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca75ce0e-cd18-3a7b-b593-96df247b0370 | -14.03938 | -47.60416 | 2026-05-07 03:47:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6780b05-09a3-359d-a5ed-80fe3070b356 | -8.30454 | -45.39842 | 2026-05-07 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c062ed3-4152-3fdf-a37a-0a7c409a9ac7 | -8.30949 | -45.40274 | 2026-05-07 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1b26ab5-6fc5-32ab-84c0-549000347716 | -10.63611 | -48.00885 | 2026-05-07 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 880a4c93-9be1-32ac-9c8f-278e362abd52 | -10.55206 | -42.43296 | 2026-05-07 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0255c200-97d9-378b-8753-df898ac0a1eb | -20.22437 | -46.84575 | 2026-05-07 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 533c5838-0930-360a-bc40-4e38ce1d1b95 | -9.01059 | -41.99529 | 2026-05-07 03:47:00 | NOAA-20 | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2169f693-a830-30f3-af2d-632e72eed31a | -12.34467 | -50.01637 | 2026-05-07 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3ad695b8-8605-3a1d-9855-d136815eca1e | -8.3102 | -45.39883 | 2026-05-07 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f0af9de-0edc-3c53-aa4a-10b1cc31a8d1 | -11.78705 | -43.63668 | 2026-05-07 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cb175f5-f774-32d3-82b7-1008085c156f | -8.72555 | -47.98209 | 2026-05-07 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d571cd7-91a0-3322-a2df-99b0dde540aa | -12.85538 | -43.75528 | 2026-05-07 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2e476ad-9324-3033-8ff0-12e64697f1b7 | -12.85997 | -43.75616 | 2026-05-07 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5730b22-deb0-3695-9595-db9d9deb0f3b | -11.94697 | -43.37995 | 2026-05-07 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b056b9f2-6cb5-36e4-aed8-896022c8976d | -15.84143 | -39.18454 | 2026-05-07 03:47:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4f2681d3-f6da-3f51-b2d8-1495904cdc24 | -8.72443 | -47.98774 | 2026-05-07 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd346eb9-8832-31f6-ac53-91a7d8030e1e | -11.61156 | -48.0539 | 2026-05-07 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e3428b5-2a0c-37c4-8bf9-62d3dd114a9b | -13.95458 | -47.5475 | 2026-05-07 03:47:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9de3e69d-f70e-3e65-b1bf-99a83d86cde4 | -14.85993 | -48.56208 | 2026-05-07 03:47:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7d72b672-1a7e-3421-87c2-9ab28999d0b9 | -14.0441 | -47.61046 | 2026-05-07 03:47:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 713b7e4e-59ba-3c2b-833a-22c7c70aedb2 | -11.78794 | -43.6318 | 2026-05-07 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c625017-9f20-3e5b-80db-7b98425e20ee | -12.86085 | -43.75134 | 2026-05-07 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c46c9bd2-c299-30d0-99dc-c35bc866cf38 | -21.3297 | -47.08136 | 2026-05-07 03:47:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0699c156-c88e-3f00-bdbf-6c102871def7 | -14.86098 | -48.55718 | 2026-05-07 03:47:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 94ef7c04-6987-3d76-9900-d95b5fe9939b | -8.72492 | -47.98471 | 2026-05-07 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 363576ec-5200-368d-8b03-ccb25d71bc14 | -20.22912 | -46.84748 | 2026-05-07 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3725ea89-fb3f-323c-a5bc-6b11ef33f4f1 | -13.62783 | -47.81977 | 2026-05-07 03:47:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07072fbf-c6a3-3bf2-b0b2-5cf52f05521f | -12.75585 | -46.96521 | 2026-05-07 03:47:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bd5ccf4-64cc-3847-b4f8-91916cff63ad | -12.85449 | -43.76009 | 2026-05-07 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bbf5a97-7511-3407-b908-4f83a24e07cd | -14.86201 | -48.55239 | 2026-05-07 03:47:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ff335f6-0248-3de2-8b7b-27d1d4e8b8a9 | -10.63284 | -48.00777 | 2026-05-07 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 099c6e5f-fa8f-3353-ac91-64763fd47672 | -11.60282 | -48.05663 | 2026-05-07 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d585002e-6b3a-3c70-9236-768ddd81c0b9 | -12.27425 | -43.55322 | 2026-05-07 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83ef9bf3-beaa-35a4-90c6-ef4205d2da77 | -14.13172 | -45.34941 | 2026-05-07 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d88461d8-50f1-38a7-bf3c-a58c7d3a8f27 | -14.12673 | -45.34844 | 2026-05-07 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d005bbf-12db-3e5b-bf27-ebd9ea51f03d | -8.72599 | -47.97903 | 2026-05-07 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a2097d5-49a2-3078-b5d0-d2a13ad7f6b3 | -12.75666 | -46.96115 | 2026-05-07 03:47:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bdfe70e-3493-331b-9ff2-5f15fc98eafb | -12.85078 | -43.75439 | 2026-05-07 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3c3c4ae-7ddf-3569-9b50-f794c26f9dfe | -14.86031 | -48.55337 | 2026-05-07 03:47:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3a67f98-7654-3697-b59f-9f92c9ed776c | -20.22702 | -46.84201 | 2026-05-07 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb055959-7027-37a5-9d14-a1c7c1f95e77 | -20.23036 | -46.8414 | 2026-05-07 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15e02752-c8c5-3df9-bf87-5fe7ba28220b | -14.12556 | -45.35439 | 2026-05-07 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 185e6e7f-e1f2-3dd6-a982-bb28df50a9fe | -10.55567 | -42.43803 | 2026-05-07 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8438819a-b1cd-3202-a24a-a54cc707474f | -14.12615 | -45.35141 | 2026-05-07 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c18389b6-8d88-3a0c-ac5a-570d8e061a41 | -12.86456 | -43.75704 | 2026-05-07 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4fb3f9d-e0f6-3a8a-8773-a7a7d7efddaa | -11.94609 | -43.38477 | 2026-05-07 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08486fc9-9245-3579-88e1-9fb228e344dc | -14.12057 | -45.35342 | 2026-05-07 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a8e0a04-29b4-38b1-922d-a35b1ce36540 | -11.61624 | -48.05399 | 2026-05-07 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83bc0f0f-c910-3cc9-be8a-2bc10c68bb19 | -11.61004 | -48.05282 | 2026-05-07 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07a330c2-25af-3e81-bd58-95fb621a3e8d | -11.60438 | -48.05769 | 2026-05-07 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fdf9a66-f660-352a-9150-5813ef24e794 | -14.85931 | -48.5582 | 2026-05-07 03:47:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47870ef8-5a92-3ffb-9137-236702d56e41 | -14.12761 | -45.34398 | 2026-05-07 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3d17aa3-9f53-37c1-b527-64e87d9543e0 | -21.3357 | -47.07699 | 2026-05-07 03:47:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebda794e-a714-374c-bae1-d2591226be5c | -12.2789 | -43.55124 | 2026-05-07 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
