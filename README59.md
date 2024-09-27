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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a314a3d9-d5c1-3941-bf70-a336ae384046 | -17.06288 | -41.14908 | 2024-09-27 03:49:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a7ced671-1441-36f9-ab59-afd36277b2d1 | -17.04913 | -41.14685 | 2024-09-27 03:49:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d891903e-4632-3885-a0fb-b406ae4e8f8b | -16.86196 | -40.04385 | 2024-09-27 03:49:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5cc81ad1-066b-3e0a-b4d6-31cae91397c6 | -16.71702 | -41.01451 | 2024-09-27 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 20b4d23a-5c27-3ce3-8174-2e1d63ddbac0 | -17.93492 | -41.2063 | 2024-09-27 03:49:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| edbcc111-5311-3f4b-9c81-ee45ca210790 | -17.93152 | -41.20559 | 2024-09-27 03:49:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bdaadff2-2cb0-3f65-8901-3547147a9d53 | -17.87024 | -41.36355 | 2024-09-27 03:49:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a8a91d7-a6e2-3cee-9a9c-e1cad6c62b0f | -16.9796 | -41.20677 | 2024-09-27 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 08ffd7e7-1b17-3d3e-87a3-2b681211b38f | -16.97895 | -41.21066 | 2024-09-27 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1e28016-8b6b-3998-83ca-f8172cc42036 | -18.99329 | -41.0465 | 2024-09-27 03:49:00 | NOAA-20 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0061658e-eaad-3fae-a873-1b2e78dbf0f3 | -18.10325 | -40.45971 | 2024-09-27 03:49:00 | NOAA-20 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bee7a7ab-569b-3d0f-bca5-3f0e385da050 | -19.16145 | -41.38878 | 2024-09-27 03:49:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 7547edfa-8a3b-391f-a134-03221dcc8c03 | -19.15806 | -41.38813 | 2024-09-27 03:49:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| abd57d37-744a-3d44-965c-7ecc821c1ca0 | -19.15466 | -41.38749 | 2024-09-27 03:49:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 8fda634a-70be-34c6-8a79-0117d2673d11 | -19.15254 | -41.37916 | 2024-09-27 03:49:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 6e44f9e9-6e44-323d-abf1-79baab452c57 | -19.1519 | -41.383 | 2024-09-27 03:49:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 0befff1d-4d2a-329a-a03e-b0b546d8a942 | -19.14914 | -41.3785 | 2024-09-27 03:49:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a98d1c3e-8d66-3e1a-b31a-04da6e299e53 | -19.14639 | -41.37401 | 2024-09-27 03:49:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9d4fcac4-504e-3a16-9dc1-89885240ea86 | -18.5831 | -41.34134 | 2024-09-27 03:49:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 26e1cf80-acec-3ce9-b527-3a15d662a933 | -20.67893 | -40.96349 | 2024-09-27 03:49:00 | NOAA-20 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 112cc382-557e-3299-82ca-3c5599d22c39 | -20.65038 | -41.07454 | 2024-09-27 03:49:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0d5e6db3-fc63-323c-ac68-4621286340ab | -20.64769 | -41.06997 | 2024-09-27 03:49:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7e950752-022e-3cbc-906a-d6fc299c0fc8 | -20.64706 | -41.07378 | 2024-09-27 03:49:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 75e49dc9-aa10-3da7-a148-a17b2c4f98a9 | -20.64437 | -41.06925 | 2024-09-27 03:49:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9f3a02b4-a01d-30a0-9ff0-5b075cbe5fca | -20.64375 | -41.07304 | 2024-09-27 03:49:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1fde4bef-ccef-3d18-bd00-2f19dcbf8569 | -20.54553 | -40.93164 | 2024-09-27 03:49:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 76a8044e-7d9a-3db6-9ffd-474841c469a2 | -20.54492 | -40.93539 | 2024-09-27 03:49:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f3a862a0-eabf-3576-b4cb-75e82b9f613a | -20.30561 | -41.14385 | 2024-09-27 03:49:00 | NOAA-20 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e80ee33-bcaa-379d-a043-c6fdf7549066 | -20.30499 | -41.14762 | 2024-09-27 03:49:00 | NOAA-20 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 599968df-e740-3595-89c6-0d305ed0e99d | -20.30375 | -41.14377 | 2024-09-27 03:49:00 | NOAA-20 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c4f6b899-4964-3e1e-9c1a-b7b77fad7bab | -20.30314 | -41.14757 | 2024-09-27 03:49:00 | NOAA-20 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b5dbd97-927f-309c-95de-631136626d5a | -20.29702 | -41.21648 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a19ebb7b-f8aa-36e7-823d-6f61beda756e | -20.29366 | -41.21585 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 39cb467c-5dc0-3f59-ae97-aea028842de3 | -20.28792 | -41.43795 | 2024-09-27 03:49:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| caa13d3d-7359-3055-8b64-a54443bf07da | -20.27877 | -41.32621 | 2024-09-27 03:49:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 749e23bf-d530-3ea3-b338-355a70b7c5bf | -20.2754 | -41.32559 | 2024-09-27 03:49:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f84251ac-12f1-3fe9-a0eb-d19e062a88bd | -20.27397 | -41.32571 | 2024-09-27 03:49:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f48bb116-4a96-3751-84a9-3e2edd164d79 | -20.25605 | -41.28707 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c9755e92-4278-3c30-adb0-cbfef8db26ef | -20.25229 | -41.30994 | 2024-09-27 03:49:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7ed10457-ea2e-3fee-9ac1-1d7d8eb9b343 | -20.19685 | -41.85391 | 2024-09-27 03:49:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 543a0a5a-3352-3f32-b3e4-fcc93e9651d9 | -20.19343 | -41.85327 | 2024-09-27 03:49:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5acaa6e0-3c31-3bad-95af-55509163563f | -20.19277 | -41.85717 | 2024-09-27 03:49:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed163fc6-ae5c-32d6-90e1-0b900ce1bbfe | -20.17974 | -41.45409 | 2024-09-27 03:49:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2a31c1d4-c72b-3cf2-b0b3-1f790860a8c1 | -20.90694 | -41.3631 | 2024-09-27 03:49:00 | NOAA-20 | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e3526536-95be-3bd7-b094-2447ec433e45 | -20.90356 | -41.36258 | 2024-09-27 03:49:00 | NOAA-20 | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 54903e2e-272b-3e9a-805a-99294a0dd0f8 | -20.90294 | -41.36634 | 2024-09-27 03:49:00 | NOAA-20 | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 20bc15cf-71ee-32f4-b914-e17c24d803e2 | -20.88022 | -41.31514 | 2024-09-27 03:49:00 | NOAA-20 | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 301458db-2fd4-3be2-bacb-be87d2863d29 | -20.78148 | -41.48586 | 2024-09-27 03:49:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cac9e9fe-ba69-3501-82b3-bf515e14ff73 | -20.7781 | -41.48532 | 2024-09-27 03:49:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f0130848-a339-37d0-b4d3-dd9bb0372e6f | -20.77716 | -41.85044 | 2024-09-27 03:49:00 | NOAA-20 | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e7ebb26a-39df-3daa-93c4-4597d8be0d8f | -20.77651 | -41.85431 | 2024-09-27 03:49:00 | NOAA-20 | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5b7ca102-5b19-3d60-bf29-c343c46f5d5b | -20.77375 | -41.84986 | 2024-09-27 03:49:00 | NOAA-20 | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0d78327e-2fdd-3622-b7e6-eeaa3aa7e87f | -20.77309 | -41.85377 | 2024-09-27 03:49:00 | NOAA-20 | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| df86d9bc-67ac-39a0-84f7-3efadb20d4d6 | -20.62514 | -41.20647 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| ad7319b6-af14-354d-9ad0-3ba6776f288a | -20.62496 | -41.35386 | 2024-09-27 03:49:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2cb776bb-019d-3a56-8bc4-c8daa2887210 | -20.61809 | -41.22821 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2811a9de-7860-3af9-bf58-20032ea0c65f | -20.61647 | -41.22855 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 82b9e3a0-ac6c-3e23-9b40-a5f00e78283d | -20.61524 | -41.23611 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 04b1d375-f56a-346f-b86d-4b9ed9dbe247 | -20.61461 | -41.23993 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 54212a71-f946-39ac-b2fd-93a161015848 | -20.59933 | -41.24876 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3114327f-103f-3ef5-b792-3cd835257f73 | -20.59845 | -41.23308 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 73185832-3350-3344-86f3-cbe04fb35842 | -20.59722 | -41.24054 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3c488f8b-f554-30e9-9406-02c8467ea8be | -20.5966 | -41.24434 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 265db8ef-eacd-3d64-8302-7e443ae029ae | -20.59598 | -41.24809 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c8192bf8-4412-37fa-ad21-4c13496e6700 | -20.59509 | -41.23251 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 43e473c5-9af2-3d97-adc9-a5cbdf6c0a61 | -20.59448 | -41.23617 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fabcb01d-af21-34ef-8cae-6ee78fa31ebd | -20.59386 | -41.23993 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fca2ee9c-6947-34f7-9d8c-b13f71bf15c6 | -20.59233 | -41.22823 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| ebdef50a-e467-3e11-8bc0-57c016ff0713 | -20.59172 | -41.23196 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1912bda9-a3f9-370c-896a-1fa59a731196 | -20.59111 | -41.23566 | 2024-09-27 03:49:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cf79ce0a-0d4b-32f5-b6b7-e8db0cbeb0b9 | -20.53636 | -41.88236 | 2024-09-27 03:49:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d86bdbe-27ea-3777-86f4-ca4203804128 | -20.53568 | -41.88641 | 2024-09-27 03:49:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 84b003fe-f59d-36b7-8865-cea938d50ef4 | -20.51829 | -41.96811 | 2024-09-27 03:49:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| 70dd0dd7-c578-33d5-8c9f-c5d9957a33f0 | -20.51761 | -41.97209 | 2024-09-27 03:49:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| 55770cfd-9b84-3ffe-9d47-a1e88eb2232a | -20.51488 | -41.9674 | 2024-09-27 03:49:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| 1b69b9c0-7dcc-3f62-a4d4-2eefa569a596 | -20.51284 | -41.97936 | 2024-09-27 03:49:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 430e103c-fc6d-3bc0-a895-ff2cb478d62d | -20.51215 | -41.9627 | 2024-09-27 03:49:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 02466787-ece3-343c-a43a-d3efe386089d | -20.51147 | -41.9667 | 2024-09-27 03:49:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f4afabaf-890b-3538-ac83-d8061b896aa8 | -20.50944 | -41.97863 | 2024-09-27 03:49:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 3650fc32-cb75-341b-9fa2-413bc895925f | -20.43494 | -42.00525 | 2024-09-27 03:49:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 4629cfbb-3df1-3234-990b-3002a7509e2d | -20.43427 | -42.00921 | 2024-09-27 03:49:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bb631cc6-db8b-383c-af23-69d93d79d14f | -20.43359 | -42.01322 | 2024-09-27 03:49:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 111550ad-4af3-3616-9cb2-4bfa978543b8 | -20.4322 | -42.02144 | 2024-09-27 03:49:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6698a473-4744-3dab-85fd-2d2434936b2c | -20.43152 | -42.02549 | 2024-09-27 03:49:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d9c6e34e-14d1-3465-88a2-f331c1a1447e | -20.4315 | -42.00468 | 2024-09-27 03:49:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 476f1540-b035-3193-834e-f99f4c03dd94 | -20.43084 | -42.00861 | 2024-09-27 03:49:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 659796a0-7d45-3426-ad84-293c5a0192c8 | -20.42805 | -42.00418 | 2024-09-27 03:49:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 32e3a44c-cb7f-3b9b-927f-db83653b776e | -20.42739 | -42.0081 | 2024-09-27 03:49:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 06017dc1-0fd7-3073-b6df-4cf489d16eb2 | -20.41381 | -41.88012 | 2024-09-27 03:49:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 601f604d-5177-37bc-ac61-e4a9a6d964d3 | -20.41043 | -41.87932 | 2024-09-27 03:49:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5fbf0b89-26ce-3d8c-a7ca-972e46225e11 | -20.40973 | -41.88343 | 2024-09-27 03:49:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6f481f43-c0e2-3462-920e-57e453153cf9 | -20.40635 | -41.88256 | 2024-09-27 03:49:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ebb5ba16-b1ba-3240-82a6-bb0b70a6333a | -20.3745 | -41.6961 | 2024-09-27 03:49:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f4d0999-fefb-3a1c-8590-239d69f1187c | -22.30371 | -41.88009 | 2024-09-27 03:49:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 49e958b6-bd12-3f3f-ae0f-3eb64f15db16 | -21.93264 | -41.55439 | 2024-09-27 03:49:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b727d4a9-17ed-3010-96fb-c155938c7a20 | -21.93201 | -41.55822 | 2024-09-27 03:49:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 28b9ee88-a7fb-372c-a872-1a1cead528f9 | -21.74514 | -41.37087 | 2024-09-27 03:49:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| daab3570-983c-3228-8189-2e844cbb0c48 | -21.7418 | -41.37024 | 2024-09-27 03:49:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a6c4a32a-f588-3407-b2bd-4cac641a9b0f | -21.70691 | -41.81297 | 2024-09-27 03:49:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 77c49658-fb5a-3b13-975b-5d38b5638f66 | -21.60183 | -41.87791 | 2024-09-27 03:49:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |


[Clique aqui para ver as próximas entradas](README60.md)
