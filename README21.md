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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a44b29c0-69f7-33d4-ab01-88cb7146c831 | -4.26436 | -43.71764 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c85f4d29-fc6a-3b90-9a8e-8a4fb5623311 | -7.77868 | -40.73116 | 2025-10-30 04:04:00 | NPP-375D | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a3808a04-b7ff-3e01-8712-48d0dffc6202 | -4.25437 | -43.70626 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24d7077d-fbca-3769-b252-190757bddeee | -6.13983 | -41.69268 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 923858b2-7c76-3ac3-bdce-5bf528f3044d | -3.53376 | -47.55339 | 2025-10-30 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb6c3581-0781-384a-8525-947138a17f2d | -6.23594 | -42.53242 | 2025-10-30 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a8489056-d243-3841-80a0-45a9dcd375d3 | -7.38134 | -47.62291 | 2025-10-30 04:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a45d71ca-8727-3bfa-aa4e-3d0c36dec86c | -6.61922 | -47.18139 | 2025-10-30 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b3c338d-c2da-3366-9a61-4eb9cd691e34 | -5.70246 | -43.15821 | 2025-10-30 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 092e5532-e6b1-3cd5-bb4e-b9617eef86c9 | -3.84077 | -49.3819 | 2025-10-30 04:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bea8a5d4-0e7c-371e-9c37-5e88eb9d672b | -5.79152 | -40.81709 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e1bd19a1-b728-30cb-9b42-70571dcde92e | -7.93342 | -45.48424 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1732125b-39fb-369b-8fd8-1a5446fd75dc | -4.85186 | -45.42385 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3786a428-dca3-36be-b120-32b5597385f7 | -6.14152 | -41.59482 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 12fbd414-ff7f-36d6-a87b-d4fe09734750 | -7.26307 | -45.0242 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9415d319-a60d-307b-9c00-e01ada72adbb | -6.22952 | -42.52729 | 2025-10-30 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d5102a2-72af-33ed-a54c-e0691cc53866 | -3.67869 | -47.63018 | 2025-10-30 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6093c01a-516d-35cd-8684-a4c2b816e6cf | -4.66813 | -46.01852 | 2025-10-30 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c199ea2-9133-3f91-818a-2b9c044f39f0 | -6.1272 | -41.70582 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e49b7e87-0448-3d15-a909-8c427cc80e79 | -7.30874 | -47.81736 | 2025-10-30 04:04:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75b069b0-2a9f-3d86-92d0-731e72d7029f | -4.31709 | -48.22748 | 2025-10-30 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8100453-1085-3577-95f4-0729cb9fe1f4 | -5.04192 | -44.87873 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aad3db5-fcb7-35cf-b0be-d9fca3926eac | -6.18961 | -41.57985 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b97d8091-4e4c-3e15-994d-d3cd23aa2fce | -5.58765 | -46.55052 | 2025-10-30 04:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0bb38ef-f9e3-34e9-ae1d-ff9bb6082443 | -6.13878 | -41.67734 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 183d8501-4638-3087-8f99-cbca661f8360 | -5.84678 | -40.81507 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a250791-3a9b-3984-94bf-531b94a3a42c | -3.2248 | -46.88206 | 2025-10-30 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7571321d-294e-3047-a667-4fd041586504 | -6.22536 | -42.53071 | 2025-10-30 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a5b4c1f3-debd-399b-b808-2ae83f4e0e5a | -7.66393 | -43.91188 | 2025-10-30 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c28005c-acd7-3b53-8512-38e52659ed4d | -7.3257 | -42.487 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cca2c44d-2805-3290-a930-2e0463b0f2c6 | -7.42013 | -45.97552 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8dcaa424-bbf7-3496-8bba-a9150d219762 | -7.38812 | -47.64013 | 2025-10-30 04:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2aeea8f3-a87c-3d58-b6e4-5bc89cd80e55 | -4.84406 | -45.84935 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4eaf945-bf02-3c7f-887f-d482849e030e | -3.67551 | -47.62594 | 2025-10-30 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1599b2da-0db5-3dba-a3fa-34339622a4b2 | -6.12779 | -41.70216 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c4591112-2858-322c-9095-171697d447b2 | -5.03867 | -43.61234 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| e7582fa8-dd43-34b3-9b48-85cd2796d9db | -7.1239 | -46.99876 | 2025-10-30 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1a71c54-885e-32b3-9232-b4e2642ccca1 | -4.89189 | -45.43832 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19d28d4c-223d-3d4e-b031-a7588adfe72e | -3.00971 | -51.382 | 2025-10-30 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fa35990-f59d-3b47-93a9-d5d5fd7c4afa | -7.80474 | -46.45511 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 19c63266-774b-3266-b68f-1227a80656f5 | -7.45914 | -46.84797 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ca09dd9-c367-326a-a036-26bbd81fb8e9 | -2.76632 | -45.39758 | 2025-10-30 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d0b924f5-10cd-3394-a6c1-48dd9b85b6be | -4.33046 | -47.89511 | 2025-10-30 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ea2249f-ca4c-35d8-956e-7ca059f311e6 | -4.22494 | -45.57611 | 2025-10-30 04:04:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 845071d4-4954-3d96-a57c-7bc303141112 | -7.75819 | -46.4906 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bf7ed08-7d2d-3338-b10a-9a5bb73e2b6a | -7.92553 | -45.50555 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fbcbb57c-4ae8-3d16-bfbd-2d622361f601 | -6.40308 | -47.07403 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26113972-bacd-3be2-a56d-97345f813dda | -5.06504 | -40.4719 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 82908c7c-e981-3882-9296-943343613e3a | -7.0613 | -44.9375 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee75aca6-4aaa-3857-8959-2c66e6a63a1e | -6.91676 | -42.24975 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8558da0c-d93b-3744-92f1-1da92dfbaa4b | -5.79208 | -40.81357 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 756e80bd-7621-385b-9739-455044ecbab6 | -3.48375 | -49.89843 | 2025-10-30 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68966ce4-67fa-3d7d-980a-252a01f52bbd | -7.37504 | -42.45481 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 968034a4-1db1-3077-8138-cefeb0d4da8d | -7.27094 | -46.88444 | 2025-10-30 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b6b357c-8786-3210-9abd-e5d77693a5ef | -7.924 | -45.49022 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3cd5929a-30f6-3842-844d-ce1427fd9cbb | -7.0604 | -44.94282 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9caf5ce-8d4a-38e0-add3-e181746dfee8 | -5.84318 | -45.54227 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b3e0fcd-f3ab-3c24-98d0-734c2d46e5d1 | -6.91268 | -42.25297 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7ce25c57-0dfa-3219-b65c-2c3d9a9206b0 | -4.98604 | -45.51762 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06dc0983-3d29-3500-aa9a-040349a70afc | -6.14383 | -41.68959 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 87819c94-26a9-3d41-8e11-2ab5d6d57e48 | -4.05551 | -44.26048 | 2025-10-30 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c17b9479-a852-325f-8531-9d7b2496e7ae | -8.65693 | -41.03718 | 2025-10-30 04:04:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 200dbdf1-d9b0-30bd-93da-fb12c30ff536 | -7.541 | -44.04546 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 644fad6e-9685-3ab4-b693-6f8b1ed5e3e9 | -4.05066 | -44.265 | 2025-10-30 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7ba3c80-0695-3d7b-89d0-7eb2ec44060f | -7.61873 | -43.58092 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 407582e7-7b08-30dd-af04-236dfad15484 | -6.55812 | -42.3502 | 2025-10-30 04:04:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f67b4647-0610-38ff-9268-06d7330d8d6e | -6.97993 | -42.66467 | 2025-10-30 04:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d96eb69c-539f-39f7-888c-75bf347d4b43 | -7.61364 | -43.58891 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90daf58f-b11b-355a-80f5-ab65aa1e19ae | -6.01986 | -41.97657 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 84634872-6b3a-37c0-8c1e-f45e8c63b6cc | -6.11977 | -41.70841 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f8f76b36-f799-35bc-a065-325157f8b144 | -4.2659 | -43.70822 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1bfd4cb2-ae98-3da3-bf30-41532986d308 | -5.43199 | -45.33741 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3606106d-e8a6-3641-92a1-660f0a44ad74 | -3.31311 | -44.14799 | 2025-10-30 04:04:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4b4c137-af03-30ff-b58b-4b7ce4fcb137 | -5.72467 | -44.40544 | 2025-10-30 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 72ed8b90-af5f-38ae-a14e-a3f6f4990a07 | -6.91553 | -42.25735 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3dd69a04-3c0a-33e9-9a8f-8c58e5200582 | -3.2313 | -46.87273 | 2025-10-30 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f7029be4-cf1c-3680-b5af-ff7c0d661d06 | -5.25349 | -44.27643 | 2025-10-30 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11390fe5-9c59-334f-9f69-7c56c4a75752 | -7.87273 | -44.23447 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cc4f7a8-921b-370b-9368-be87c090ef61 | -6.71091 | -38.21014 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e513d2a5-8502-3aa2-b3ab-b379972dcb9a | -6.11634 | -41.70787 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9e70c477-02bb-3eaf-8b4b-b3e789c596a2 | -4.94502 | -45.62001 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c2c5c09-45dc-314a-bb39-c2d9a7f43e98 | -3.63089 | -43.91831 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e134545-d667-3fd8-825a-8e9cd281d98d | -5.49402 | -42.07869 | 2025-10-30 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd007a50-0bf7-3585-92ed-61c5a5f66399 | -6.12672 | -41.8626 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 769d8f53-8529-35cd-9e89-96f1b07b3772 | -3.79795 | -43.90141 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 1131b0b7-7200-3891-b496-cd909f24553f | -3.93313 | -44.1966 | 2025-10-30 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 903e2a86-b123-36e5-9fc9-9872abfd0106 | -4.68889 | -45.59631 | 2025-10-30 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 568d8b1c-a144-379d-8983-6d8effc9fe3a | -7.59542 | -43.60796 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fec3b15-cb72-3a93-843b-b9dd4170b4e2 | -6.85574 | -46.29303 | 2025-10-30 04:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6f94388-dd6b-3fd9-9378-100fa2feeee6 | -6.31109 | -42.10829 | 2025-10-30 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5547f4ec-828f-3e2a-942d-6d29a19b2fde | -6.28061 | -35.51218 | 2025-10-30 04:04:00 | NPP-375D | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 55430b3f-cfc5-38b5-8908-af5d7d8ba352 | -5.23842 | -44.29436 | 2025-10-30 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cabd7b9-4cbe-3b22-bd76-7fa656c93d80 | -7.38359 | -42.46806 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 510c2cf7-e0a1-358e-9674-9032a26dfea9 | -6.26604 | -42.72527 | 2025-10-30 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 24bce815-15c2-3a18-bdda-71461ab63418 | -5.40997 | -46.01262 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06cfb24f-0c6b-3f78-8202-dfd25bf4ba49 | -6.9505 | -40.91538 | 2025-10-30 04:04:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 016e3f89-ca88-3437-85b2-b72b556fd7d4 | -7.15027 | -44.86076 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 871fb9a6-247f-3685-a164-29d18d52f21a | -7.79387 | -46.41457 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6b109d75-ed76-3ef8-85a9-e7279f3cde48 | -5.40925 | -46.01698 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea06afa0-f7ed-3a29-aaf6-919a348ee767 | -6.1744 | -41.60787 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
