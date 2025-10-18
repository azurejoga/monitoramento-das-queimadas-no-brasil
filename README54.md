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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64b4d1ae-4368-358a-8c5e-afc2f7f59606 | -9.58993 | -47.8503 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac7efddb-3a3a-3001-b12c-971032b49d25 | -10.41873 | -47.74916 | 2025-10-18 04:29:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e779e23e-76ce-321d-9bd2-7a4c9978188a | -6.3495 | -45.75452 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdb4b773-741a-3b98-943f-749945bde2e8 | -8.60883 | -40.19147 | 2025-10-18 04:29:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 0e7bc85c-49e0-3580-a322-f5814ab95ab8 | -7.54655 | -46.91382 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c945bea9-0bb0-386e-8bb3-80cc2b92cd63 | -10.24049 | -44.06352 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a2cb902-0197-3baa-92f8-f1695f13d124 | -3.80074 | -51.64791 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b437be1-ebb0-3f41-82ba-8b3a08b190fd | -8.63334 | -54.62999 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4f676c4-6ce4-389f-91de-5219515dec49 | -7.71015 | -47.84757 | 2025-10-18 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b35d9a6-2765-3ec7-8b82-3d549675ffed | -8.82553 | -50.05023 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9fbe7f1-f5e6-34e5-8c1a-8c72b6394374 | -8.44195 | -44.17175 | 2025-10-18 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 703468da-be2e-3310-9269-48e92cf06e69 | -7.02434 | -41.81625 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3f8a52cb-7794-3057-ad49-886b456e54d2 | -10.53329 | -43.36661 | 2025-10-18 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 83806f2c-cd5b-3caa-b3a8-d56090e98fb3 | -10.51342 | -43.42338 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c2bc5ce-61fd-364c-9489-84e6a368e5e8 | -6.13195 | -44.30185 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e8ea33b-d018-3304-8343-9141b3f04445 | -10.52482 | -43.39809 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1df2da3-7e65-335f-a256-3d9b7b1364e9 | -8.38125 | -49.73021 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92160ac9-e28a-3735-88e1-ac50e5a6c9c2 | -7.11901 | -44.73014 | 2025-10-18 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1acbe17a-3978-35df-8727-b52015bf0b47 | -8.13268 | -49.10528 | 2025-10-18 04:29:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b5b2212-1945-3a1a-8ec3-3623407a0973 | -10.25625 | -44.03157 | 2025-10-18 04:29:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83e5f204-3eed-34a4-9962-39ce90cbd948 | -9.66201 | -48.52911 | 2025-10-18 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9631582a-841d-3cd4-a05e-35a2f97848f8 | -8.54498 | -50.07566 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74d441d8-1068-3f0a-8248-f2c92d685c14 | -8.38674 | -46.24644 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dff8bff-c9dd-3337-8670-63e4962682f9 | -6.89056 | -45.45739 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10fc1746-1b47-3c5c-aec9-7f5dbdf9d6d5 | -5.90947 | -49.41998 | 2025-10-18 04:29:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74a02d06-9087-3477-9f9c-3d53d853596c | -10.24531 | -44.05585 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f588621-4e1b-3ff3-9d38-5eb3f8cd5b13 | -7.83 | -44.12367 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dfa5b08b-b385-3fce-8bcf-d7c9f76e4832 | -10.46211 | -44.12445 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4489452-371c-325b-b27f-cebd1b75bfb2 | -10.49136 | -43.44309 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ea43fa8f-fbaa-3247-a06b-f8233e100ec8 | -6.88437 | -45.43107 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42345137-2179-386a-98b6-9c4c0992a2dd | -4.8446 | -46.72059 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71189e16-8cd5-326a-9aec-6b13ce39982a | -6.43536 | -43.3806 | 2025-10-18 04:29:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 290bcda5-ed1f-388c-b40a-0c62afceb1a7 | -9.08126 | -48.03106 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fa91de0-310e-34f4-ab73-e1cc22cea9e8 | -10.49577 | -43.43914 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 1e72451c-952d-3861-97a1-8bdff9a600ad | -3.78507 | -51.77056 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 095a0ee2-9e93-37bb-a29b-60c83576aff6 | -7.06525 | -45.61436 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83a4e9dc-5dc7-3e58-b994-e606681e7ec5 | -10.47846 | -47.73338 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2426555-608c-31d4-bd5e-3621e88c5133 | -7.11233 | -44.81973 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d54fca83-5960-3481-b9a1-9b5eb0e48198 | -7.06191 | -45.61383 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62d84673-9e06-352d-bf03-fd19c04725c9 | -6.37699 | -44.70516 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 696e80ab-03d6-337a-91cf-6f6ac7997fe0 | -7.16464 | -42.37881 | 2025-10-18 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 27d5b03e-cae2-3d39-bda2-c3f4e36a2f8f | -10.49247 | -43.46177 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| edfa7d83-225a-3967-8e92-dba6d9a6c106 | -6.69381 | -44.27746 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af9df5af-aee7-3b98-aa38-3e6745cf39e7 | -6.12096 | -46.15632 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c447141b-208f-34ed-8ddb-312c636a6eab | -5.25597 | -50.90766 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a51af76-1f63-36ee-8cae-1f18d8c539cb | -10.62978 | -42.3056 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 87f42d5c-705a-371a-91f5-6965a9930e3d | -8.56312 | -45.43227 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| daca0a26-b27d-34cb-875c-c166049f4983 | -8.36613 | -46.20365 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0c2e540-6c5a-36c8-8bd3-1670a6dda61e | -7.71331 | -47.85506 | 2025-10-18 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef9d4b8f-5c70-34d6-85be-afad1f6427c0 | -5.30198 | -44.84406 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ca1d88d-797a-33b3-a20c-d1bbb0d6cd28 | -6.14338 | -44.45584 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d34686e8-4643-35c3-a921-daa8fe0d23e0 | -10.83895 | -44.39667 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0191dac3-f511-3fa3-86f2-46597fec8423 | -6.14172 | -44.28411 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52240e91-b754-3d37-8ad2-195129b0b041 | -8.58793 | -45.42871 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b15c53eb-951d-3698-adf5-0a1d5e330395 | -3.86116 | -52.23029 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acbf237c-9a4f-3f32-b4af-0b35681ca7de | -5.22473 | -44.77741 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af6cce3c-6cff-3c4d-b576-d9aa12e7fbf2 | -5.30142 | -44.84764 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 160b5f01-0263-37be-8a09-bd3e3bdee0e1 | -9.37358 | -44.62669 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d0430c7-3427-3ecf-bbd1-9f005ff7ae35 | -10.46345 | -44.06433 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fff0976-2e53-3345-8bfd-10e0ae3b94de | -6.99055 | -45.20268 | 2025-10-18 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 417d6bbf-798a-381c-a01a-6dc95f8911a0 | -10.29803 | -44.02483 | 2025-10-18 04:29:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39b463af-c601-3ab2-97c1-0759f3900bdf | -7.44055 | -44.74874 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4b7ebd1-c1be-3d53-a433-9c6c23831a9e | -8.54047 | -50.0808 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8538dcd-a1d9-336a-9623-3b8869a922f1 | -4.9976 | -43.85541 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91567994-cbe8-324a-828a-936e58fce62c | -6.94246 | -43.6879 | 2025-10-18 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fbb01f5e-ead8-35a5-ba98-878c9576c751 | -8.43635 | -48.69959 | 2025-10-18 04:29:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 446f3d2d-bc88-30db-9d3e-4ff925a9ed37 | -5.51746 | -45.90855 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05df2509-4a3c-370e-8894-c6475edb4cc6 | -9.666 | -48.52604 | 2025-10-18 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a56c8e0-0a49-34ac-b104-27998864bd24 | -6.14341 | -44.29605 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61af6a7e-aa1b-3bc7-9dd6-2d59adc069fd | -7.74615 | -42.5111 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5f890474-abcf-3194-8354-191b26786955 | -8.316 | -43.44756 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf9fe6d3-5acb-34d0-8589-3859df70d69b | -7.57864 | -44.98468 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92b704cb-e5f2-31e7-b9be-d77b17bf3207 | -10.23873 | -44.07372 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d3f1c6c-3119-344a-936c-065ceebefc0f | -5.55809 | -46.38024 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37e9b2bd-9db6-30d1-a4a9-85f52d2b466c | -10.7062 | -44.55071 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81407d7a-c72e-34a7-aef6-c14703cf90e6 | -10.23466 | -44.05158 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f09ed7c6-c4ac-3623-8fdd-cd5137a85695 | -10.252 | -44.03531 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b924f03d-4e9a-33ad-908b-e5cbade63098 | -10.25688 | -44.02719 | 2025-10-18 04:29:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f1372be-b3a4-3a75-afcc-51fe95754bd5 | -7.80133 | -54.93977 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11fddbfa-4e4d-3ccd-99c3-b970e245a4a5 | -6.30518 | -44.71666 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e93705a7-64b9-3d99-a02b-1df2bbcb864c | -7.24868 | -49.5164 | 2025-10-18 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8574ed1e-af17-3cd9-b6f6-09b2b53a162c | -10.69553 | -44.54913 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2884e08d-c1da-3359-9c89-88b66458fb57 | -7.8591 | -44.23952 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8f4dffc-af24-3e30-a927-f44cbeccd977 | -3.79074 | -51.7631 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9695078d-42e3-35e2-b035-752755ee5735 | -6.33732 | -46.34724 | 2025-10-18 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab129e39-4d4c-3cc9-8fb6-04f1c032633c | -6.73948 | -43.81279 | 2025-10-18 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2c4117de-500c-3f9c-9dfc-91514643fdeb | -7.01685 | -41.83217 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a107bcfd-2d64-3fc0-9973-1d2b6b94265d | -9.19388 | -46.87232 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94c4ab05-a3e8-3405-a297-e7bc6ffbda23 | -8.24273 | -44.01214 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71bb7c7c-1f47-35a6-a748-4fe7253764bd | -7.43575 | -44.75982 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6219ade7-0889-3017-a37f-3df2211c565b | -10.11624 | -44.54818 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 192e7530-1b93-3682-b6a3-24c4fbf34406 | -6.98732 | -38.43113 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9923861b-c600-38bc-88c1-1c280d44619e | -9.72275 | -44.55678 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 69fd08a5-1658-340d-b5b9-f7fcd36e2144 | -5.21267 | -47.5025 | 2025-10-18 04:29:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59aa67b9-4d26-3633-95ec-0f65222dc64b | -7.59284 | -44.98302 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c28af26-5481-3482-ae9a-c53c799630a3 | -7.97127 | -45.1527 | 2025-10-18 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a343eeef-4055-37b1-90c2-f1868b5c0e78 | -6.95979 | -47.12067 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd3df9ec-5250-3acd-acd2-54b79956a771 | -8.83363 | -49.69135 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66ac4f23-28ae-3fbd-a0cf-394c53690ffa | -10.42652 | -47.74317 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40ac2cba-30f1-3d89-a3fb-08aac3f5d0eb | -9.09308 | -47.82816 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
