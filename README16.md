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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 506d88e2-88d7-3380-8bef-8b2715a4b6a9 | -2.13 | -53.25397 | 2024-11-07 00:58:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 99c74f68-f668-39db-b889-7fa125a2032a | -1.14812 | -53.74909 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| df37a171-0b6d-3268-ade3-673f42e31b44 | 0.69053 | -51.44199 | 2024-11-07 00:58:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9f252f6c-5416-3ad1-98cb-6c0517fec6af | -1.18874 | -53.91882 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1e27d3db-885d-3129-b73c-30ad1e3babe8 | -1.18696 | -53.90577 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 23a243a6-77f9-35fb-81da-cd876655d099 | -0.04009 | -50.79934 | 2024-11-07 00:58:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d28bec36-bf4e-39b4-86ab-b54721e175d3 | -0.40427 | -51.56255 | 2024-11-07 00:58:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 84a0fb89-c2e3-35c7-8686-f5c7e9379d17 | -0.84648 | -52.83795 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 30b64eda-b2ed-3aa8-a9f1-3130d69b3c47 | 3.35832 | -51.28539 | 2024-11-07 00:58:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0d15fce6-83b2-3a32-8091-d42e63ee8532 | -1.55351 | -52.27068 | 2024-11-07 00:58:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| afddd2b8-174f-36e5-9bd9-3a135bb16df6 | 3.61565 | -51.35786 | 2024-11-07 00:58:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 519639d9-2495-333e-863d-5fb4912108ad | -2.23679 | -53.67684 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 9ad88a8c-6c3f-30e0-8914-53a5e1092ab7 | -0.29934 | -51.40392 | 2024-11-07 00:58:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c5ce182a-e51b-325d-89e1-bfbaff3e8d63 | -1.06304 | -53.67187 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8f85024b-3e2d-3200-b30f-afc219f058c9 | -1.39828 | -54.10774 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 005358f5-c659-35c3-a6e4-7be196ec401a | -1.16109 | -53.71692 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 1ca7123d-414a-3219-81bf-3633b4264a4f | -1.2214 | -46.36362 | 2024-11-07 00:58:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 16a2e0da-2155-3a3c-9771-43949d065ef6 | -0.84796 | -52.84877 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| bfa2f626-e9b5-384e-83de-f81f07862475 | -1.3901 | -52.21183 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 67ffdc62-6c04-35fc-92a0-c25ce8c0e31e | -1.52737 | -52.22204 | 2024-11-07 00:58:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ff4720c8-e6ad-3769-974c-5b8c6c6a4181 | -1.22804 | -54.54568 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 1636328f-507d-3255-b6fc-3d968e178e99 | -2.24269 | -53.68161 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| deab0f97-c2d1-33d0-a467-0a1d3b9a3fee | -1.76326 | -54.19199 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1c03d380-f733-3710-a610-b332f77b23d7 | -1.19754 | -53.90434 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| bcaaa22b-f989-35a1-b950-90ba31eb6b37 | -1.19178 | -46.66755 | 2024-11-07 00:58:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 71482a54-86e7-3946-b03a-a8ce1863fb64 | -1.28407 | -54.13393 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 33cef9d5-9e5f-32b4-9623-1f19e37b3bb4 | -1.3958 | -52.21515 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b18f494c-1802-3d23-b6af-0771f9b5b02f | -1.18521 | -53.89299 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| b95e3fd0-903a-37f5-97a9-7ef0724bab1e | -1.62257 | -52.24424 | 2024-11-07 00:58:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f310523f-7c16-33e2-9d67-4e2e73bbdde1 | -1.47947 | -52.08403 | 2024-11-07 00:58:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 772e83fc-5861-37ba-b961-5e12c0e09832 | -1.20255 | -54.20703 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b352a1a0-3596-3cbb-9f84-9476c8e11679 | -1.13841 | -53.70622 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| cceabe35-daac-36d4-a242-ea8c55f06e0f | -1.20096 | -53.62278 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 610ffb0d-73fb-37cf-a448-22b0cbf92fdd | 0.69951 | -51.44325 | 2024-11-07 00:58:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9bcbcb06-8af7-3a33-89f2-9af480775a76 | 3.51963 | -51.2421 | 2024-11-07 00:58:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ef1a4202-1f54-37be-8bb2-524a9eba4d8f | 0.16304 | -51.06427 | 2024-11-07 00:58:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 567eba97-f302-3173-99cb-a40cb8a5dd3e | -1.37831 | -52.26545 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 405731e4-d0ad-3b12-8a52-820fd24345e1 | -1.14017 | -53.7193 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3441e86a-1cbe-39b7-984d-c2cbfed41a7c | 1.91134 | -50.87788 | 2024-11-07 00:58:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 36076df1-08ea-3abf-a34f-71cee30a5edd | -1.2053 | -54.20105 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f68fd956-e978-38ec-abe9-6ce3a50f9020 | -1.1446 | -53.72437 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| e2e6899c-c63b-35de-b944-1229eb8a1ef9 | -1.38723 | -52.19153 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 8300ede8-a203-3623-80cf-0a41e873acf4 | -1.38866 | -52.20168 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| e4e52ab2-c7bd-3e29-b515-cf89e83b073d | 1.35835 | -50.94309 | 2024-11-07 00:58:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 22.8 |
| a13ab75a-8288-37d1-987e-b3296b35ac00 | -0.90541 | -51.65389 | 2024-11-07 00:58:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4b6e94fa-f8f7-3f02-b425-e30869feeea7 | -2.23507 | -53.66399 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| da92b0d5-db87-3736-bc46-b8ad145ccc98 | -2.17045 | -53.70505 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dddb6311-a25f-3cfc-9381-7652f9f306bd | -1.72494 | -53.28608 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 45b74a97-645a-35fc-a4de-557c3bd8e744 | -1.53119 | -52.17991 | 2024-11-07 00:58:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 81b78b68-d96e-3422-a227-8b92be17efd6 | -1.32212 | -54.64322 | 2024-11-07 00:58:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 47261e23-0574-314c-a8ca-c5c61596b94f | -1.13234 | -53.71292 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8c215583-a4a7-3214-825d-c9ed551b050c | 3.60305 | -51.30533 | 2024-11-07 00:58:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b6edc7b8-1fae-3fbd-9bb2-32cd257cdb9a | -1.14638 | -53.73682 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| f5130603-d0e2-3638-8ab1-95c4877d8c3a | -1.39303 | -52.19482 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 1564a284-cf05-3fbd-b6f0-5ef20623c4bc | 3.81587 | -51.76117 | 2024-11-07 00:58:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1a22d2c1-80c3-37ad-8f66-db82d7de3626 | -2.24088 | -53.66879 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| abab6d86-0e36-3df3-a6fe-2821bb74342b | -2.23031 | -53.67023 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 31277eb0-73fd-371d-9afa-f1f4451586c9 | -1.1628 | -53.72942 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| e27779d8-d365-34e3-82f0-9a2484a1b95e | -1.53554 | -52.00478 | 2024-11-07 00:58:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d12b5da6-9d69-3f03-9548-452cd647ab45 | -1.9521 | -53.07452 | 2024-11-07 00:58:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c66c3a97-047e-3c62-8434-875bb15ac5c9 | -1.82173 | -53.68647 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d9b30893-85a8-374c-9dcd-7aeea1ca0150 | 0.53986 | -50.80007 | 2024-11-07 00:58:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2d955c7f-8706-3a36-9cf4-cb24274330f7 | -0.17453 | -51.4996 | 2024-11-07 00:58:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1fd64fae-6d2d-3096-a468-6cf6ad742ed4 | -1.06133 | -53.65938 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e79d817e-e524-32bd-a9a8-77086d5d563e | -1.13759 | -54.21597 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 493983d2-e7bd-3073-beb0-199adf193b2c | 1.98325 | -50.89431 | 2024-11-07 00:58:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b61daccd-f290-3cbb-b04e-bdc5a682aa59 | 3.61441 | -51.3667 | 2024-11-07 00:58:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 5bfcc0de-96fb-395b-9f53-7c0df9cb3e8e | -1.15404 | -53.74316 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| cdfeca61-abb6-39a9-b178-f87bcb0bfbe6 | -1.14278 | -53.71162 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 065d8d95-e0e0-3a37-8937-32bb2d01d7f0 | -1.39165 | -52.18465 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ad1472e2-3f00-38dd-8403-257d7bc10b50 | -1.22604 | -54.53143 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8221cb2d-d650-33a4-a778-3c2bdf813d7e | 0.53863 | -50.80891 | 2024-11-07 00:58:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cab23afd-a24f-3c75-813c-f4400700ffb8 | -2.8352 | -48.6648 | 2024-11-07 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e55e61e0-8a63-312f-a8be-ee3519f89d9f | -3.7033 | -48.9986 | 2024-11-07 01:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 2760b36c-7828-34e1-875e-3643444387b5 | -5.0342 | -46.83 | 2024-11-07 01:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 8b600f19-8ba5-3c96-8be7-bc7f1ff3cadc | -5.0154 | -46.8531 | 2024-11-07 01:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| b251c5ed-1c10-3817-b743-b3abadeb0025 | -3.0207 | -53.443 | 2024-11-07 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 2847d8c7-9c0a-3158-a950-f5c59b7f577e | -2.8537 | -48.6642 | 2024-11-07 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 151.6 |
| fa892745-f6c7-31d0-b3ca-06f35ad5b54b | -1.1283 | -53.7179 | 2024-11-07 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8075b773-d1b7-3b8f-943f-0415a71f6e41 | -4.522 | -42.8608 | 2024-11-07 01:00:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 40af1a79-3637-3265-837f-b4185061d54f | -5.034 | -46.8521 | 2024-11-07 01:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 121.6 |
| e943a657-2b03-3bde-92ff-f2284a668164 | -4.5033 | -42.862 | 2024-11-07 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 29d07bfd-2e6d-3f55-b6ce-cdc7c603f134 | -2.6044 | -51.3043 | 2024-11-07 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 4b96e204-784d-371a-8dcf-c87e6fff27f1 | -2.82 | -52.9613 | 2024-11-07 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 07945985-c72f-383e-a812-0bac4918c5d8 | -2.8351 | -48.6862 | 2024-11-07 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ffb3a477-0673-35c8-951a-8bb844714b94 | -1.1831 | -53.8985 | 2024-11-07 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5db16e57-156a-30cc-951e-7a8d6129a037 | -5.1395 | -47.7008 | 2024-11-07 01:00:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| d81195ba-7a33-3460-8494-ac6b012c4ce1 | -4.5218 | -42.8843 | 2024-11-07 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 4140ce7b-184e-3312-a35b-435becdd33ec | -1.2014 | -53.8983 | 2024-11-07 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| bcd0dcdf-67a7-3eb1-9cba-290b2d7f279b | -3.4564 | -50.3832 | 2024-11-07 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 50c62e74-3c39-3c63-93ab-3df8d760afa7 | -3.1617 | -50.2038 | 2024-11-07 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7490ef6c-0718-3ef5-bd89-37d20d588cab | -1.1466 | -53.7177 | 2024-11-07 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 4589fd92-8493-3b0c-9924-2a639038d9e9 | -5.0155 | -46.8311 | 2024-11-07 01:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 617a7c78-b518-38ad-9ed2-fd5194a972f3 | -2.8536 | -48.6856 | 2024-11-07 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| c02a37a9-eb90-3a5a-bf35-50817163d76c | -1.1466 | -53.7379 | 2024-11-07 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 378a9a69-f4ea-3b7e-a210-e0f4ab1aff4a | -2.4319 | -53.6584 | 2024-11-07 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| fce57ca2-f117-3543-a0ec-b6ef2111a43c | -3.967 | -48.15 | 2024-11-07 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d255aad5-b3a2-36e3-a110-70d5bf9a58b8 | -4.5031 | -42.8854 | 2024-11-07 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 74f7b1d9-e952-3148-968f-9b038e3f9844 | -3.9669 | -48.1716 | 2024-11-07 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 398cbd20-774f-30fe-a870-16cc0927b096 | -2.6228 | -51.3038 | 2024-11-07 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |


[Clique aqui para ver as próximas entradas](README17.md)
