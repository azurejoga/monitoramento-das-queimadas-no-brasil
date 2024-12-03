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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2121f988-a9f8-392e-b7cb-4647daf506d5 | -3.2592 | -53.648201 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdf0a7e5-17e4-301b-ada7-7b6684d17ac5 | -3.3917 | -50.3078 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa84f2c0-6d2f-3aa7-8344-f37b10b549f3 | -1.6896 | -52.623199 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57a48c55-0583-397e-8cf1-a991ec540fd5 | -1.1653 | -53.4062 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd8223f4-925d-3d9b-8e48-750f5fb268cd | -3.0276 | -53.3955 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10731bc4-ff8c-3d26-85c9-5794874b8701 | -3.8166 | -46.559399 | 2024-12-03 00:37:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1fca75d6-8a14-331d-af29-7344ecf833cb | -4.1515 | -48.583199 | 2024-12-03 00:37:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d28236f-9296-3055-ae36-ff0142b4a10c | -3.0342 | -49.372398 | 2024-12-03 00:37:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85bc650a-ffc6-361e-a11b-f4a5431c7651 | -1.7543 | -52.773201 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0243c5b3-a6ee-3593-a6df-dcd271a85f67 | -3.5209 | -46.173599 | 2024-12-03 00:37:00 | METOP-B | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24f5f7cc-b99d-30af-ac52-a43d12b0e70d | -2.2065 | -53.775799 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8932d612-3368-3cf1-b477-3d07a9ef4d52 | -3.0389 | -54.089901 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30827677-f8a2-3925-8cbb-e3db9b34cc28 | -6.0156 | -42.513901 | 2024-12-03 00:37:00 | METOP-B | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4418d964-e774-3d70-9d59-a96d60022508 | -4.2675 | -50.6689 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d849b4ee-bbcb-3256-9c22-83f291fb3b36 | -2.2818 | -46.368801 | 2024-12-03 00:37:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8fac72b-f89a-3ddc-b326-1fe2a5c4eae1 | -4.525 | -42.917301 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e535cb7-af9e-3c41-871e-77dc0e3ec9d9 | -1.3824 | -53.5466 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fdda7c2-073f-392d-aa84-3d2f5bd094f2 | -1.0785 | -53.432499 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 492019d1-ee23-32d9-84d6-b24ab1a3cc4d | -3.5914 | -50.369999 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2df1c2-c353-3eca-9003-58b67ab4cdd4 | -4.0356 | -54.221001 | 2024-12-03 00:37:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 835b273a-3a5a-38fe-83b4-60d4e65ee050 | -3.185 | -54.3288 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a76f18db-289d-3eb6-b205-4b89c793bb11 | -4.1858 | -50.672298 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37a6d3ef-772d-3d6b-a2f0-4c0b31b097cc | -2.6658 | -46.607101 | 2024-12-03 00:37:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| efbd3cfa-0f78-34ee-8f11-0dab6fd17e78 | -4.4029 | -49.769501 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef302ac8-f86d-3a48-8356-1e09f2654853 | -4.8828 | -50.927799 | 2024-12-03 00:37:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb60c412-aebb-37f1-aa9d-d60dc5eb6041 | -3.3348 | -46.036301 | 2024-12-03 00:37:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5a6d946-1dfc-397d-9968-54cdb233824c | -3.4953 | -49.451302 | 2024-12-03 00:37:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d174979-21c0-3e39-b6dd-b53ec60c5db5 | -4.7335 | -45.121799 | 2024-12-03 00:37:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acc7fddd-3664-346b-9b23-62336a8c0d18 | -3.2267 | -51.716999 | 2024-12-03 00:37:00 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9d973d2-2fbf-3342-a25e-72de47f48c35 | -4.194 | -50.663101 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 548897f5-4765-3796-83e8-dad5fc325e1e | -6.1603 | -42.601898 | 2024-12-03 00:37:00 | METOP-B | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e7994cbb-17b4-3a6f-9fe0-27044f67f72e | -4.5394 | -42.934399 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2ab30e6-2eaa-3268-a009-fc705a4c3fb4 | -1.6948 | -52.6007 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cec4950b-6703-3013-8572-ee3b0d5b5aeb | -5.8025 | -46.467499 | 2024-12-03 00:37:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc22cf3b-6c0c-390c-b064-b12f6a0e3e34 | -1.3243 | -54.9827 | 2024-12-03 00:37:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cae6204a-dbc6-303b-9d29-8a2e8f866266 | -2.7846 | -55.347 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39501660-4cf4-3bc6-b334-d4e92652d6d9 | -6.018 | -46.245399 | 2024-12-03 00:37:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9cbadce-50f3-3c95-86ef-fc48cfcc5cab | -3.251 | -53.657501 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8032d35a-aab8-36d8-addb-4ee367192278 | -1.7236 | -52.6371 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7340b49f-0d7a-374d-a7a5-f7e854a0fdcf | -1.7347 | -52.777599 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6814cad-4bbd-3eef-b695-1ed1e6febab9 | -6.0984 | -43.951698 | 2024-12-03 00:37:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5efc38bb-04de-37b6-8015-b2a6c27e93dd | -2.358 | -53.854099 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6faf31b0-2bf6-3fdc-bd00-51a7d7590ec3 | -3.3138 | -49.9202 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9ce4130-e900-364d-af62-9381169679e1 | -4.1855 | -51.171101 | 2024-12-03 00:37:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47984dff-39ad-31c8-a841-80f31125c446 | -6.6671 | -46.375999 | 2024-12-03 00:37:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07e2066e-2b01-3de1-99dd-dad47a325f6d | -1.7589 | -52.793701 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d769710-0a1f-37eb-9824-1ba0f563044f | -3.0818 | -53.361599 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d791c62-1214-319e-8027-f98fbb924d1a | -2.3626 | -53.920399 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cc06f01-9b08-323e-afe3-35fef113bfa9 | -1.2584 | -55.8806 | 2024-12-03 00:37:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f483dd3d-8513-3c60-8ac2-23a70f4e02f6 | -4.0351 | -46.923199 | 2024-12-03 00:37:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b1f30a2-73c7-37f5-a99d-3839fb95466c | -2.9804 | -53.874599 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4a0e5e3-6764-3e58-96c4-e3afbadf6e77 | -2.4572 | -47.2174 | 2024-12-03 00:37:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f813b7ea-1b71-32a1-a770-fe9d8435e787 | -1.7387 | -52.6124 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab1c7faf-b1d9-31bb-abb7-5254e19a2426 | -3.2859 | -54.135601 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3dd16e1-ef44-3e3f-a55b-cfed2f913a6b | -3.0681 | -53.254799 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f68a8460-d637-34f5-ae5d-d130acc84e7c | -2.444 | -54.007801 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bdbdd2e-80c9-3dd3-9bf6-c9a6f8eca11e | -2.0712 | -50.709999 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62c4f325-d5c2-3e5e-9494-76711ba92944 | -2.3371 | -53.806599 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c10fd9d-0c50-3d4d-b7dd-eb08f85ae682 | -4.1594 | -48.572498 | 2024-12-03 00:37:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 310fe775-709c-3f45-afb7-6eff9bb24c58 | -3.1712 | -53.622799 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b394c29c-cf71-393a-b02d-cf419973b1b1 | -3.0939 | -53.278301 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 890d567a-329d-3623-8ffe-2c94bda51ee4 | -4.4769 | -46.346802 | 2024-12-03 00:37:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 632d8f5a-891d-3be6-8fd2-da920d7243c3 | -1.5133 | -54.540798 | 2024-12-03 00:37:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6641a71f-4bad-3f42-9867-bf6ac3ac2865 | -1.8381 | -46.003899 | 2024-12-03 00:37:00 | METOP-B | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6f04365-291c-3f5b-81d6-3b344e7e96a6 | -3.5036 | -53.820099 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e1de492-8925-3733-af25-eb19fb0b4a6e | -2.7072 | -47.5434 | 2024-12-03 00:37:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f188f10-0912-3f7c-8bd8-cbedb45dc3e9 | -3.0955 | -53.285198 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b493b15a-103c-3913-8131-5b171b66ed3c | -5.0949 | -43.198002 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ba79ef6-31ca-3d61-bb39-237390b433a3 | -1.7101 | -52.440102 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 661fcee1-cc3b-3b4c-ac2f-0520f185f90a | -2.8276 | -49.8218 | 2024-12-03 00:37:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2898e14-4964-3ecc-b408-1b80a9fd20fe | -3.1735 | -54.323502 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f8c739a-52f9-3e30-90b1-049f8ef1c630 | -2.2601 | -53.601501 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 179d0463-0270-3eed-a2eb-84e5be416ca1 | -5.8123 | -46.465199 | 2024-12-03 00:37:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fded6aca-9d64-31c8-9c0c-c30bf7bb11a8 | -0.8348 | -48.712601 | 2024-12-03 00:37:00 | METOP-B | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1b39d82-5396-399b-aa86-970b697a5ed8 | -3.2691 | -50.312302 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6967ee99-5d71-318e-ac45-5a83539b03ec | -3.4955 | -53.829498 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1134c913-9b02-3ffe-a3f2-b7f3592c8d17 | -4.3174 | -48.0961 | 2024-12-03 00:37:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9b8b29c-b1f9-3952-af93-172eb8627088 | -3.4906 | -53.8078 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eca9b87-e066-3c9c-ace8-e42a5685770c | -2.1874 | -54.0116 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c946b0f7-4157-386f-833a-91271984e81f | -2.9772 | -53.860298 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44f8f1d6-97bd-3dd0-937f-8c58adefa742 | -2.4622 | -53.951099 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7185a4b-a6b8-3032-9101-780dce876f09 | -5.0905 | -43.179798 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f6ef054-c257-368d-9c2b-c4ce4889b7bb | -1.0661 | -53.377499 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b48c2150-e601-35f9-9e28-821fb7edd2c3 | -4.7433 | -45.119499 | 2024-12-03 00:37:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b58fe93-179d-3c1c-8d8e-c69d2d53de1e | -6.8124 | -46.773399 | 2024-12-03 00:37:00 | METOP-B | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a05910a8-e34f-3d1c-9b08-3e28969b1ce1 | -4.7368 | -45.0923 | 2024-12-03 00:37:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9fc8cbd8-1762-3b16-932d-63286e2f265a | -3.3772 | -50.697102 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbca2352-cc4d-3aa7-8f24-6a538af9395d | -3.2658 | -53.631802 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66527420-3673-3a1f-806e-9c1413147a43 | -3.0209 | -54.0555 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e69c7908-5fa6-3ca3-a9ac-643daa1fb226 | -3.3404 | -50.172798 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96bbc147-3364-35df-9ea8-c4612246416b | -3.3383 | -51.207401 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a03d182-ae75-3b5f-adca-9dff29e09cfe | -2.4592 | -53.6166 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51e40500-6c99-3317-8202-afcae7de4755 | -2.8956 | -51.574501 | 2024-12-03 00:37:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d04a3665-dac7-3b63-8049-07f8e2d699f0 | -1.7491 | -52.795898 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 326c838d-63ec-3173-b5a8-56383e82be23 | -1.584 | -52.246498 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c4d4bff-78ac-3347-bb00-d47add5671c3 | -5.561 | -44.882702 | 2024-12-03 00:37:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d0a3267-b504-3e11-a415-23a682795d0e | -1.6537 | -52.7384 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebf47e87-b244-399d-87c8-68634937dcdc | -2.4396 | -53.620899 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6325cede-b7e8-32bd-bf06-ffd5ac960684 | -4.0454 | -54.2188 | 2024-12-03 00:37:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f081bd42-2574-3fd1-9638-11a5852bc5be | -4.1634 | -48.187698 | 2024-12-03 00:37:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
