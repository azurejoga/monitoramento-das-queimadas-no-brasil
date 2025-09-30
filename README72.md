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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8405fa1c-77fc-3778-8bd0-8741abc0d4a9 | -15.92859 | -46.20997 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f6da70ec-5c02-3963-89b9-c7bffcc0d040 | -15.29681 | -46.40791 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 756a33bd-21a9-3ef1-9735-62af31d95110 | -15.2492 | -48.75307 | 2025-09-30 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 403f41a1-4c9a-3121-bcd4-b30b01d90d32 | -14.75119 | -45.66357 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b61c6bdc-9d0f-3577-b352-272b1e799e87 | -15.05794 | -46.96594 | 2025-09-30 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4b99cda9-9d28-345c-9c40-f6a36c7b54f9 | -15.5438 | -47.8679 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cb073e99-c39e-3c39-9345-6e039eb48e7a | -15.16638 | -46.42315 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fb91383-3ef3-313e-bc3b-4bbc8514f44e | -15.23021 | -48.02786 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77de2c51-06e7-32e5-86b5-c9c16d4c3dbe | -14.55072 | -48.48192 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4af0f289-597d-3517-9f56-4916da7a2fe1 | -13.76232 | -54.73587 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 46e35394-16f6-3d62-9dbd-fc2a5e932986 | -20.0881 | -43.90374 | 2025-09-30 04:42:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aaff7d7b-9d48-3bd4-9f44-f55de15437ce | -14.91776 | -50.00052 | 2025-09-30 04:42:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e71c3f4e-a7f4-3e0e-8db0-4f5eec659910 | -14.55141 | -48.25307 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3ec5d34-395a-34a4-b57a-6146c9ab1b1a | -17.72197 | -46.63477 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a98109a2-57db-3b80-be6f-5b982a1e2c13 | -14.28348 | -52.94564 | 2025-09-30 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4d1c07b-4a19-3538-a08a-4fad2b40b245 | -14.6977 | -48.23307 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ccdcdc0c-a1b4-34d0-809d-75f40a1a5b70 | -18.46489 | -40.56934 | 2025-09-30 04:42:00 | NOAA-21 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 61a5d404-011d-3f94-b137-7af606942c06 | -15.38269 | -47.07666 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 634813e5-bf7a-3449-85c5-5893dba15b91 | -14.51541 | -48.40152 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b1b4889-3f81-3c02-8f5b-3f4f09f6b270 | -15.78528 | -43.65947 | 2025-09-30 04:42:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ad515c8-4f2a-3163-9af3-14dc747e7355 | -14.58261 | -48.28136 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3705aa37-10d3-356b-83f8-4fd6176d2ad4 | -15.84708 | -54.97303 | 2025-09-30 04:42:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98331edc-f68f-32d1-8f8b-3b049cc29013 | -14.64633 | -46.97005 | 2025-09-30 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9f5d6f3-678b-3d23-ada5-924eb00c6339 | -15.93367 | -48.12484 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eeaac44c-4be2-3f4e-9608-5177beea0522 | -14.76489 | -45.7541 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c3f465c-0a44-3ca1-b5ce-2c6320efe277 | -14.51879 | -48.01579 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a54f9e1-2a8c-3bea-9992-e8d3ced9a9af | -17.90686 | -57.58804 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f92686be-ca95-3084-9a90-f3cea28a3a36 | -13.87978 | -57.65917 | 2025-09-30 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86ec8657-0e48-32bc-87b0-ebb3e68620f7 | -14.53412 | -48.2459 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9775ebec-578a-3ef0-84de-c6b3e241d59f | -14.69845 | -48.13895 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43b36183-1e31-3880-b982-9490289de4c2 | -13.7667 | -54.73218 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a964dd3a-cb36-3a7f-a803-5fd796db0492 | -17.50283 | -43.47527 | 2025-09-30 04:42:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b72c5a6-f6fe-351d-b4e3-5ee3873bf406 | -14.7102 | -48.14371 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7c873379-d759-3f8a-a9cd-316dbbb167f6 | -19.52487 | -43.90289 | 2025-09-30 04:42:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc448d93-48ca-3bc4-b149-092738b9cdd3 | -15.43275 | -44.99561 | 2025-09-30 04:42:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf534618-b533-3f15-b99c-e2beb2a5a07f | -14.55901 | -48.47457 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84c80b78-e742-3471-b34f-5bdaf89998ec | -15.62386 | -46.25297 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8e901b9-ba2d-39d4-a61e-5581b9883f10 | -15.07123 | -45.05329 | 2025-09-30 04:42:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e2124636-15ed-3210-ba19-97a768da63f0 | -19.22672 | -45.81643 | 2025-09-30 04:42:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d8dab04-3b72-348c-bd24-fb364adc7c77 | -14.52135 | -48.38557 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f80785f-0410-3757-8e38-0d5da9b06597 | -19.69954 | -43.68898 | 2025-09-30 04:42:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76d58241-ad6b-3929-a69d-05145f23890e | -15.84793 | -49.49118 | 2025-09-30 04:42:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b7b7b71-d09c-32eb-8746-bd0c56e14e0e | -15.41569 | -48.2217 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b03e2af-966c-31a9-aec7-a7cef02a2a65 | -14.53884 | -48.49016 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fb69d81f-5402-31e0-b4af-0282bf762cea | -17.73809 | -46.67244 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bda4c97-fdf7-3707-ac0b-26f852dbdb42 | -19.84978 | -43.8119 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3e89207f-7487-35e9-9662-9930b2ea3879 | -16.38563 | -47.03234 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5f180ba-17e6-33ee-b461-069a889a9fdd | -15.3904 | -47.07793 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ec36c51f-bf20-3815-9033-171420c1a718 | -14.25128 | -52.95163 | 2025-09-30 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d899a8b-8b36-3ab3-910a-06cd64df9445 | -15.11886 | -46.46072 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2298bbf0-dae9-3bdd-8ec5-e08ba5540576 | -14.52306 | -48.42405 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d6ffa5a-36a8-3376-b077-378e98539444 | -15.33127 | -46.27118 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21e7365c-d536-3b96-b54c-9477c39e0340 | -15.24907 | -49.70789 | 2025-09-30 04:42:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa45b492-8b5a-3fd1-af37-aa568023f4cb | -14.56847 | -48.45894 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c165ee2-13f4-341d-8905-0d2737cc44a2 | -17.09952 | -48.57248 | 2025-09-30 04:42:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 010bec34-4d58-36f9-a300-a1981393711b | -15.32947 | -43.80442 | 2025-09-30 04:42:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1badea25-2930-33be-ac4c-de26a08960d2 | -19.76237 | -49.32362 | 2025-09-30 04:42:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 47ee3e42-eb5d-3838-a8ba-8b09e0740e55 | -15.40293 | -44.98228 | 2025-09-30 04:42:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc672f68-4173-36f1-af60-f4cca8a5d8a4 | -15.28365 | -47.85685 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a12865bb-5276-369d-96fb-42e9d7d07c96 | -17.87588 | -49.39037 | 2025-09-30 04:42:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82bfb171-65cc-3ddf-bcd5-93143574629a | -20.39208 | -43.67793 | 2025-09-30 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e66dcce7-6eb5-3b8a-ac22-ade0cd1e372a | -15.27936 | -47.88824 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51d14a0b-ed79-33e6-a709-20322aff4cfb | -18.12295 | -42.19808 | 2025-09-30 04:42:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 34be08d7-3005-3e16-83e6-edc2dc0ddeeb | -14.81462 | -48.75724 | 2025-09-30 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e088838f-dfe1-3feb-b072-5b7ee8c2bd8c | -14.5178 | -48.38494 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b5e1f4e-5a17-3fb8-911b-9efde7a66c24 | -14.56407 | -48.24156 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7b8dda4-3b4b-3143-a664-5b5bd4e4bb3d | -19.30079 | -46.2479 | 2025-09-30 04:42:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41b171a5-02e2-32ee-9f77-dbdcb812d4b2 | -17.70577 | -46.66909 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff0616a9-e2f8-3e49-8e57-f803671438f9 | -14.79037 | -48.31933 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3aafd008-7f00-3020-93d0-c9c197bfb9de | -16.20642 | -52.82364 | 2025-09-30 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33b7668e-891f-352f-8ba5-4569fe49d378 | -15.27525 | -49.26733 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3e20d6a-54f7-3e1a-aacc-3c39aeabca96 | -15.27872 | -49.26774 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af704a46-6498-3df0-9cf9-a97214deba6c | -15.26842 | -49.50359 | 2025-09-30 04:42:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e760c10-ac01-3cc1-b5ef-ab909fc56c15 | -15.21237 | -50.09565 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e6ab7c9-a4b3-3e4d-89de-6dc729be82b7 | -15.24183 | -48.02494 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e5462bc-6595-3964-9bdc-740d71284359 | -14.56373 | -48.46678 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 714393f7-216a-31cb-9403-446e27af32d5 | -16.42947 | -47.03378 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a80113e7-d4c7-3c59-a777-8eb448aba167 | -15.28479 | -47.85502 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0dc81f49-c531-3439-8f71-06ade28e0aaf | -16.3935 | -47.03333 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a682c10-46ff-33dd-8266-ec54857ae27f | -15.54012 | -47.86721 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ee1d341-7a54-3c5e-bff9-7538c9e6dd60 | -15.2769 | -47.85112 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ac3dce8-4b21-3fb7-80e7-e4ec044f4f50 | -14.52594 | -48.47927 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1c3b0c6a-da56-3f62-9f4f-2dfa2f505c08 | -18.5351 | -46.04879 | 2025-09-30 04:42:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3396dbc0-b120-34f7-adb0-973980d72ee7 | -19.85005 | -43.66508 | 2025-09-30 04:42:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 111ec138-4bbc-3d49-bda6-c2a910062b9b | -15.23698 | -50.0923 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 905c7887-aa0b-31bc-be57-75227fe78938 | -18.05781 | -43.65215 | 2025-09-30 04:42:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79a9b4af-e4dd-326f-ae7b-c168fb375765 | -15.28109 | -47.85452 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34b75c46-107d-3907-b79e-2c0f0dfc4774 | -17.3959 | -47.13472 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6538ab3-d275-30a0-ae92-a56af173879c | -15.20846 | -50.09878 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7821eafd-7e7e-3e4d-8384-186db1ed3a1b | -20.0656 | -46.79111 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 032a5ee5-29aa-3467-8135-b03bea7cf002 | -13.7594 | -54.73091 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 903b984f-0bd0-3edb-8c39-143e65e367dd | -14.73442 | -45.66122 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c8432141-f609-3a01-ae71-9f91468bfe0c | -15.73092 | -48.89782 | 2025-09-30 04:42:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b16ba043-e6e2-3a68-8fb5-8b790eafc3c1 | -15.27876 | -47.8926 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a1b19767-805d-32a2-8cc8-41e27f3ddbef | -19.85859 | -43.81241 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e7eb4d19-d89d-3086-bd32-0e48bab9eb3b | -14.71682 | -48.25373 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c17e367f-b233-3a9a-9ea4-093e16c908d3 | -15.2683 | -49.26653 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de95bd73-705a-398a-bc80-4208b4cf3f2a | -15.55651 | -47.91213 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b788069e-4491-3007-bca7-f1a94c14d156 | -14.55679 | -48.26656 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d8d8543-2421-3195-b843-b31e13bd0311 | -17.39378 | -47.15075 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README73.md)
