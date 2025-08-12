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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82cd61aa-a9ad-318e-b205-c837fe2fa111 | -12.66865 | -46.97207 | 2025-08-12 05:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0b42d0b8-378a-3c45-a5a8-5c07269ccf6f | -11.66438 | -50.12774 | 2025-08-12 05:46:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| eec547a1-9dfd-3150-8529-e62cf9e665b2 | -18.60726 | -43.91008 | 2025-08-12 05:48:00 | AQUA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 8104669c-69dc-3701-a672-b40c44ee4412 | -19.29461 | -48.42914 | 2025-08-12 05:48:00 | AQUA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6ce16bc9-5a45-3706-94c8-78383b9cf426 | -17.64901 | -46.66327 | 2025-08-12 05:48:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.0 |
| e3fff821-f336-3cc3-9dee-5855738b4f0a | -16.28676 | -52.89646 | 2025-08-12 05:48:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b5cc9dbd-5ab0-3dc8-ae1c-de331234d616 | -19.217 | -46.79436 | 2025-08-12 05:48:00 | AQUA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6004bd58-5d6b-3eae-a22c-559da3b0fca1 | -17.65516 | -46.68327 | 2025-08-12 05:48:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e08f9ca1-d45c-342a-a25f-8fcd546a2d37 | -17.57149 | -45.32879 | 2025-08-12 05:48:00 | AQUA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 46.6 |
| c49211f1-a20f-3a41-a460-a28fb94b50f9 | -17.63867 | -46.66462 | 2025-08-12 05:48:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| a05f79f4-1556-3902-8ce2-16ced9f18675 | -19.21563 | -46.80383 | 2025-08-12 05:48:00 | AQUA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 40.2 |
| cf42b3ab-1afa-3a84-ae04-7e858a897fd9 | -16.30739 | -52.91874 | 2025-08-12 05:48:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 41.1 |
| d5ca0e82-b8f5-3d33-a58c-622c4da0f18a | -16.28364 | -52.91382 | 2025-08-12 05:48:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d03e3e26-0a14-31bf-b479-d636269524c0 | -17.65652 | -46.67397 | 2025-08-12 05:48:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 38d0c707-fac8-3e0d-bdd5-e937ac4af5d3 | -16.31057 | -52.90083 | 2025-08-12 05:48:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 49b7ee1b-cdec-3278-97ed-e2c0da370489 | -17.56223 | -45.32745 | 2025-08-12 05:48:00 | AQUA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7c25db13-1d99-3a59-b421-f24dae5877f6 | -16.2955 | -52.91638 | 2025-08-12 05:48:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| aee705c2-293d-3f1a-9d1f-bfc5900ba470 | -17.64766 | -46.67257 | 2025-08-12 05:48:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 98735359-643d-3ab0-9f14-f883457408d4 | -9.88896 | -58.56522 | 2025-08-12 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12d6d8ee-a1dc-3aaf-8ab7-b1b6fa5566bb | -9.19727 | -59.6661 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c92abd4-48ee-392f-b1a4-6604a29996d0 | -9.38082 | -61.53578 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ad57c6-3886-3bb6-9ac9-8a9fbb3f425a | -9.18569 | -59.66357 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 464dda44-3b86-3682-a1db-d1aa797f94b0 | -8.56374 | -54.69382 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 249e888e-da85-341f-968e-08a056c11add | -8.94873 | -68.50368 | 2025-08-12 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51204639-477d-3e0b-9ea2-665677a4dc04 | -7.0607 | -59.18795 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07e43dc7-a9cf-3e7a-9b94-b8ad16b9534a | -10.34934 | -57.60592 | 2025-08-12 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac8a2454-ad9b-36d3-aaa6-4e5dfea65995 | -9.19137 | -59.6587 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7a1166e-6bf2-3d12-8ce6-b58db22a9263 | -7.06563 | -59.18859 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d706bafc-20f7-3986-b946-247d92160c8e | -7.0838 | -59.20212 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f92bce93-48b8-3e3f-96b5-3e50317375ef | -7.96164 | -63.49564 | 2025-08-12 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 393c5af1-4ddd-366d-9b1b-dfec463c0539 | -9.38744 | -61.53093 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 14513fe9-7cc3-33c6-b579-3776507b57e4 | -8.56971 | -54.7008 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbf86f5e-4e8c-3e7c-9c13-9fe91294bcf0 | -8.57045 | -54.69479 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2aa49b60-80c1-3d44-aabf-cd6765ef1711 | -9.37821 | -61.53382 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bae438b1-887d-33d8-bed9-7761798fcd16 | -8.57255 | -54.70969 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e8d2c2b-e178-3ffa-a9bc-4cb1d24f71d7 | -9.17587 | -59.6621 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 030741a2-4fed-3bed-a0d4-70ef07b91978 | -7.44379 | -67.73316 | 2025-08-12 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43d42209-2f15-34a6-848d-2b23abcf3255 | -7.25551 | -59.99603 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfa0814b-ffab-3cf4-a6aa-504e99f8d695 | -10.34479 | -57.60607 | 2025-08-12 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac8c346b-e71d-3856-96a5-9ac014440ccc | -9.38515 | -61.5364 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ea5fd8a5-8c0f-36d4-ad21-35698d1c0299 | -8.56824 | -54.71292 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 918e6a37-059f-31f7-b269-046d99fe56e3 | -9.38801 | -61.52674 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c78541d-022a-32d0-81ca-35049d6fb917 | -8.56522 | -54.6816 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f7e737e-194c-3ddf-bc96-f1d9a890bb3a | -7.13879 | -60.13037 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 95b96d69-c03c-38b6-8a2f-2d331098cea3 | -8.56898 | -54.70683 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0dde6e1e-887b-3808-8182-ab89084ed621 | -8.5793 | -54.71034 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7317dd76-f186-3a02-b72a-11dcad9d8b60 | -8.93832 | -60.73456 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7f4d7daa-0fcc-332f-a0b6-87858b6fff2c | -7.06333 | -59.2051 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 135643e7-000d-3bc3-994c-590425101775 | -8.56506 | -54.71485 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b5f5d2b0-3d3e-37cc-a208-c0d9f0a5bf7c | -8.57422 | -54.71983 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0ed89412-ee42-3fb9-813e-3893c83c6543 | -9.20047 | -59.66529 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6735e5f1-848d-393b-9583-c287df876053 | -9.46818 | -65.60021 | 2025-08-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 658d84f6-913e-3075-a0a3-22e2ee5c15ae | -8.56301 | -54.69984 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e01bf056-9779-307d-bf0b-7813eaaefee7 | -7.14014 | -60.12075 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2b4a0d85-3442-3edf-9360-f1aba3c48694 | -9.46983 | -57.84056 | 2025-08-12 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f21e62f0-06d6-3d07-a4e2-321b0d84b87e | -10.31034 | -54.16369 | 2025-08-12 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbf4e170-c9f4-3732-b0f3-11fd2c9c9d97 | -7.13947 | -60.12555 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1b8dd633-c483-33bb-913b-595a78020143 | -9.38575 | -61.53225 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6a03ef98-7184-33fb-9a82-f91498bf20ce | -8.55704 | -54.67073 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62708c2c-0639-3032-baaf-27db76bea205 | -9.37335 | -61.52621 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3556723f-ac81-3e78-b587-0641f4452fc0 | -8.95207 | -68.50422 | 2025-08-12 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 333f1ae0-0b01-3c68-b380-f6329c0aa0ae | -7.06257 | -59.21051 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9814d76-5839-3795-ae66-619a7b76daf0 | -8.93052 | -60.75697 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63d98ca9-25c3-33ef-9eac-f21fa41f661e | -6.97022 | -59.28036 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8fa3130b-a1ee-3aaa-b3ab-2f8c932366c8 | -6.97355 | -59.29197 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 153ad3be-ae7b-35ce-976b-e1934e0f4cd8 | -7.06826 | -59.2057 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1212be58-bf9c-36b1-bfb1-8b285334fd6b | -8.56154 | -54.71193 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e29cef07-93d6-3dec-94d5-e85f6a36aa60 | -9.37934 | -61.52548 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 121eaf48-cec2-30c8-b4b5-afcc760d238f | -8.92598 | -60.75633 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 944e5875-d7f3-3a7a-80bf-4d6abad8ca5c | -9.39007 | -61.53288 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4e390914-668f-3188-af33-cd0e9db8b3e0 | -7.13552 | -60.1201 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0087f815-c34c-3369-8bd1-4fa039613b65 | -7.12957 | -60.12896 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c9bc44f-7dbe-3a2c-a79d-644254b2ae51 | -9.20292 | -59.66116 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e135fbf2-050f-34b9-814b-6bc2defd61a3 | -8.92987 | -60.72873 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e8c0ced-f8d3-35da-8e93-4c23359bd556 | -9.38948 | -61.53702 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 23e80f6e-7d0b-3fa9-a23b-4bab1bbcf81e | -7.07966 | -59.19595 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90dc6955-7fe7-3872-bb3e-5519512356b1 | -7.48391 | -68.33736 | 2025-08-12 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8051669a-eeab-36ee-aeeb-f12a6f5d6e16 | -7.13485 | -60.12488 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2f708eba-e2ad-3891-a022-6636659cc103 | -9.53612 | -66.14308 | 2025-08-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b489213-8bbe-335a-a0c6-908a60696d92 | -9.38261 | -61.52328 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b8bee0b-a97e-39ea-84b4-73b6f7bc94ad | -9.0354 | -59.75847 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9eb53fdd-c8ea-3a0b-ad68-9b9074a0b29f | -7.07811 | -59.20695 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 30514ffa-fb64-372c-a464-b46f5a2aa6e2 | -9.37275 | -61.53037 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63d42485-ac27-34c3-83e2-e495734c85f6 | -9.18155 | -59.65721 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3791dbc-0490-398e-b778-46b119d117f2 | -7.13418 | -60.12966 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4ddbe67d-7635-3094-9e4b-8c42d97f43c6 | -9.37828 | -61.52267 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 221685b3-0848-3f90-903a-2b5abf5d72de | -8.93117 | -60.75238 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e9ba7b9-31d8-32e3-8ad0-f40f3a3fff15 | -8.57496 | -54.71373 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 431330f4-40ab-36d6-86f6-0d138e67f47a | -9.64755 | -62.91466 | 2025-08-12 05:48:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb088e3d-1953-3fe5-a9a5-7db242ba6452 | -9.38141 | -61.53162 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3750b365-3e90-3315-af46-ec05b24e06c8 | -9.38254 | -61.53445 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a08158ca-0508-3600-a66b-c8c63d37e907 | -10.31821 | -54.15794 | 2025-08-12 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fae44f4-8d66-34d9-8e8f-9897fa765bbc | -7.44324 | -67.73664 | 2025-08-12 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a867d699-1f41-35fb-a088-443dff962450 | -8.56447 | -54.6878 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f420cbbb-c69e-31ef-856d-a13510b0b2f2 | -7.13091 | -60.11937 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e5973b55-fb56-3105-a2cb-bd3e2b313093 | -7.0675 | -59.21114 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2325d75a-8862-3276-ad64-7a495db5eea5 | -7.13349 | -60.13459 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a4eada89-9fce-3e5f-b48e-517d5618dfdf | -7.06902 | -59.20027 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c77d862a-d4b1-3858-9c6f-43ec4be13369 | -9.38687 | -61.53508 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1481a6d4-2e2f-3e83-be71-69f0f807da35 | -9.5395 | -66.14362 | 2025-08-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README36.md)
