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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be9146dc-4531-3349-915d-3abec7ae565e | -13.12825 | -50.8825 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e851117-a6da-362c-8466-c63989b64a12 | -15.61261 | -52.4695 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1d26417-ed0a-3442-a3c5-b7a16df8e34c | -14.69093 | -48.34957 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0aeb02d-f90e-3fab-8ec4-4bdb0ddd88bb | -16.02084 | -50.9596 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bcc53ad9-eaf9-3943-85c9-c99596c5aef8 | -15.60468 | -52.45783 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5aeef7f-9f61-30a9-abc5-e75b9f2ff32c | -11.22374 | -54.86805 | 2025-10-05 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0cae9a6-39e8-3afa-b19c-1066030b6bf2 | -14.68741 | -48.3616 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6688f0e3-c245-368b-8ea7-9e94b37397b3 | -17.95807 | -57.55724 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 117a6576-6da2-37e9-8091-43c6c7880d18 | -17.84994 | -57.63253 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9aebf4ca-6e38-3a38-a3ea-226478bea75b | -14.08188 | -50.15526 | 2025-10-05 05:16:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e38d04fc-1b40-3eea-869a-0468ce2bddaf | -16.073 | -51.08786 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 635439de-fca1-3259-9617-a9387d7e50b3 | -15.20832 | -56.84541 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e76cef0-4b13-3348-bdaf-fa124eb26efd | -13.57008 | -48.16927 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ffb6da3-c7fe-3d8c-874b-2617b59933b9 | -14.01074 | -48.21501 | 2025-10-05 05:16:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8363c097-168b-3a49-9b5b-d730d0405877 | -13.28498 | -47.61751 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca7248cb-21b5-3c97-bc26-1ea2aa4aeeae | -13.33374 | -47.7832 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d67cf39d-58a7-3000-a85b-d6f188ba66f6 | -11.22002 | -54.86752 | 2025-10-05 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4afa6044-549c-3f1c-b806-daf8b22b2963 | -14.66397 | -48.35498 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4aa5412b-8d72-313d-b56c-d6dd8c120dd1 | -15.36025 | -47.98423 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a384fa3-bed2-3980-91dc-64d65477361e | -17.97853 | -51.14079 | 2025-10-05 05:16:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d078643-22cf-335f-93b6-d6048a94175d | -13.73549 | -51.30305 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47eb837a-547f-305e-9696-0d10ec4e2665 | -12.46572 | -45.52365 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f3341da-176f-3e12-9aa9-42223851c425 | -18.18447 | -53.36121 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14f971ac-d745-386f-9bf0-a0091ebbccef | -13.29017 | -47.62645 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f6ce7d2a-37b5-394f-99a6-bdc516268ade | -16.94933 | -52.68116 | 2025-10-05 05:16:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c922074-9c82-37a0-adac-3426d7b7801b | -14.68429 | -48.29817 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be547d6c-3641-3366-b9c8-1b77a7514f45 | -15.59543 | -52.45688 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34acdc5e-5095-34b3-9093-7fefb473c66d | -13.26678 | -47.8267 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c5190af-358a-3090-bbbc-7bf394a24048 | -12.42777 | -54.49876 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 828e4c46-2ef0-3b9b-b323-e73089ecf650 | -13.1332 | -50.88316 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 753810e3-36c5-3a5a-8b77-316fcea7ad97 | -13.30036 | -47.80586 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45863b8d-e717-3e67-8a04-0d6e3e7c0ee2 | -18.24673 | -53.35368 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b2115dd-45df-340f-813f-4f8cb56e824c | -12.59547 | -48.14085 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 45cdcef9-0b0a-3d8a-81cf-5ac2681e402a | -14.33646 | -47.6652 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c0072843-978d-3908-a59e-e657968e7aca | -15.23995 | -56.77489 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52125900-1e1a-3ac6-923b-f6f26ceb3ce1 | -13.30301 | -47.62327 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bbc7b54-6577-3e2a-85bd-57b46362504b | -12.81193 | -50.53728 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 817144fe-2bab-30f6-8c8f-bb02afc63a43 | -18.17537 | -53.36094 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 311a70c5-fe1d-3bb3-85a4-50f5c74933ef | -13.13845 | -50.88481 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| ed11ae9e-231e-31a8-944c-719730d52807 | -12.97563 | -51.04095 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96ec3519-8786-305b-b960-7282c2ab9d11 | -12.96656 | -51.03416 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f99f3808-b8ca-3ff4-90f3-52e26d419ac9 | -17.85753 | -57.62964 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9215d07c-9906-3fbe-bfad-80cbd909fdef | -13.09515 | -47.91742 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cbc7a60-832f-36ed-bc3a-0a5a8fde6ed5 | -19.00947 | -50.59642 | 2025-10-05 05:16:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 02153f08-75c0-358f-b063-34e3588408d4 | -17.9605 | -57.56532 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8e95e319-f8e3-3b99-bfb8-8f212ad1a1f6 | -17.56977 | -46.08237 | 2025-10-05 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8910c63-1c3d-3912-950c-aa7cbfd5a0d5 | -15.30239 | -46.31194 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae2ca844-83d6-3093-ab1a-0f3fc0369a21 | -11.91269 | -55.90732 | 2025-10-05 05:16:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d251ef73-ebe0-3018-bd3b-8027015ef857 | -12.89193 | -47.31641 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68be1442-79fd-3c00-9712-82cc8452b6ac | -13.15826 | -50.88748 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 312eeae4-2e65-3d7d-bc6e-8d9fb01f6d0e | -12.30342 | -55.14062 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b414cef-6acc-3bd2-90f9-a60500ad5c30 | -16.04425 | -50.93742 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7ee4cd8-0569-3483-87c6-415b88ffebe1 | -12.94273 | -54.72572 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f736445-ffcd-356b-9ec9-640725875db2 | -14.08715 | -50.15594 | 2025-10-05 05:16:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df33ec20-e8de-328b-bc0a-ba977e15b6a9 | -13.30721 | -48.1201 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd22ad2a-ffa0-3017-b862-98451c4dc35c | -16.0365 | -51.0474 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01b008ec-d9aa-3c8c-9629-ecb72e049362 | -14.33033 | -47.6835 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fab29a23-5eb7-3add-a220-12dce326c924 | -12.31327 | -55.15115 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f21f7af5-5731-3e0b-8e45-26948bd19d91 | -13.07758 | -47.89916 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c5ef40a-3140-3b30-a7b9-5addc14b1554 | -12.98123 | -51.03614 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e145bafe-bfff-3f9b-b6ae-a72fc6adced3 | -13.08586 | -47.94533 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0af2b54-539b-3a98-96d3-bb8b2883fd30 | -9.65163 | -67.40176 | 2025-10-05 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 513df476-a917-3c23-9a8b-ce0a034713fb | -14.75644 | -54.66659 | 2025-10-05 05:16:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8e1b3b0-0646-3696-a465-467f578eda97 | -17.87286 | -57.59838 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b0037dcc-9109-39cf-a405-47b93d0b5c72 | -13.30382 | -48.09719 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84853c60-868e-340b-bacd-7b280cf20bbc | -13.93899 | -48.18172 | 2025-10-05 05:16:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92ab0ba5-0acb-3cf5-83a7-5c0b60709590 | -14.69566 | -48.3423 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73053f02-5c46-3e9c-9b2e-00799f6aad17 | -14.66858 | -48.31394 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 404bcc33-7524-3070-a7da-2168a5f9c389 | -15.50912 | -46.85641 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a005211a-b11b-3098-9ca3-123f4e979fad | -10.83832 | -57.16906 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97fc99ec-214a-32ba-a3cc-3363db31ca67 | -12.22595 | -56.63889 | 2025-10-05 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7850886c-31da-3b5d-8cc0-de0d14c7b3b3 | -17.94824 | -57.60034 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 68c32db8-4a6e-3267-9705-cb8e0c25627e | -12.30297 | -55.11766 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ebf7a33-35f7-3e5a-887e-6498cecb3fd5 | -15.37934 | -47.93574 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0491bbd7-eb17-31ae-9959-1dcf5e0b09fa | -12.93932 | -51.0137 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e43dbff-5bb0-3f4a-aa57-71c67aa68258 | -13.28548 | -47.61324 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18cbfa02-ddf8-3d80-af5c-0f1c13847281 | -13.34452 | -47.57797 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed0ccdbe-10f9-3dae-937d-dab45d6962dd | -11.39561 | -55.1684 | 2025-10-05 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8089601-d5e4-35c5-874f-beb2a1dbae0c | -12.57512 | -48.16088 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa53da11-f505-3bed-ba52-cf76de9fb79f | -13.34869 | -47.19606 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6eea682-25c3-3e97-ae8d-be9401c0e691 | -12.89137 | -47.32127 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 600c8bf3-d1a0-35bc-87ea-4385375e3054 | -17.7234 | -56.77827 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7dd9c97d-5adc-3b34-9457-019ee7bbdb4a | -12.322 | -55.14337 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9f4ac06-ca3f-35d9-bbdc-44f0367c689c | -13.30669 | -48.12463 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42a466b9-f3a6-347f-89ac-2db02785d65d | -15.36269 | -47.97349 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bf6b4af-3ed0-3809-a7ca-ab212657aed2 | -13.43485 | -47.28232 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8b30b93-a42d-3226-a120-b9e936401552 | -16.53407 | -47.76831 | 2025-10-05 05:16:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57717440-06ce-3731-8d94-644d519a661e | -16.33544 | -48.06749 | 2025-10-05 05:16:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01abb74f-b5c7-3d21-9afe-47bffafd24b7 | -14.68554 | -48.27117 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ba468d9-334d-338d-975e-fa4e1ed1276a | -13.27519 | -47.59428 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57f25218-7e95-3640-a945-9806af70ffe1 | -13.14139 | -47.96034 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e99853a8-586f-3579-9c2f-356cadc9f3ce | -15.60319 | -52.50805 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b4b35588-01db-3732-a0a0-d8d5f1d0fcae | -14.33547 | -47.69358 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6518f0ed-93b9-3a95-beea-5d232553c0ed | -15.50267 | -46.85419 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf684bd2-ce90-337d-9192-4ee0737d920a | -11.31736 | -53.96194 | 2025-10-05 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd50f5ea-e474-3bac-bf45-e1840f172081 | -13.43281 | -47.27583 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13384aa2-b410-388e-b6b1-ea55bd510bf6 | -13.43808 | -47.28611 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6e45b7d-0166-3c7f-a9cd-0218f518340e | -13.34421 | -48.06257 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4065e92c-d61a-3ddf-a616-67cfac87ba00 | -15.98433 | -50.91464 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0376f80-e6b3-3f51-9279-e9e528924a81 | -17.9371 | -57.60286 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |


[Clique aqui para ver as próximas entradas](README137.md)
