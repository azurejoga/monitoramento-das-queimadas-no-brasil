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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05830e22-93a1-37d2-9370-8bfcd4eca1b4 | -12.00298 | -63.51574 | 2024-10-19 06:22:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f4cb8ef0-6888-3767-bb2e-8058a6327c79 | -9.0345 | -67.4455 | 2024-10-19 06:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 8f2e76e6-0593-3454-8d27-e9c452950667 | -8.94012 | -65.90491 | 2024-10-19 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e98fb44-9aba-3971-8e66-f7685dd62c9f | -8.93418 | -65.89824 | 2024-10-19 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c3303c4-6543-3607-bdef-79f197dd4b94 | -8.93346 | -65.9041 | 2024-10-19 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d482cabb-d3c0-3d99-8ab4-e17c74fce4c8 | -9.50329 | -67.10037 | 2024-10-19 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1887893-e8ef-36b4-92a6-d209e68da91b | -9.50269 | -67.10525 | 2024-10-19 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a41efc0-c66a-3791-a77a-a152176347bd | -9.16499 | -68.25962 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2ff2eac-1251-30f9-9289-a221205a0270 | -9.04417 | -67.44864 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 066f084e-171c-32df-b420-dff53eebaac1 | -9.04375 | -67.44725 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e91a75d5-86f0-371e-8dd5-320e830075fc | -9.0436 | -67.45317 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ebe5d58-f127-374f-b615-41159e1214f9 | -9.04315 | -67.45178 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 67e16f67-0e71-3cf6-862d-aa444b2375c7 | -9.04303 | -67.45772 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7f35f192-7f8b-3e4e-9c46-45faf62f93a3 | -9.04255 | -67.45631 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f31b0f4b-d9a1-3ac2-803b-88a4d09a5c81 | -9.04246 | -67.46226 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0b8888a1-c274-313a-822e-b4b702abbbc2 | -9.04195 | -67.46084 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3aa81193-2748-3637-9fdb-ee042eb19aad | -9.03812 | -67.44781 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 827d8a27-d24f-3474-82d0-bab176ae3f2b | -9.03755 | -67.45234 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2813ae87-74ff-3191-8dcf-7b5c99517eb4 | -9.0371 | -67.45096 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5baa4e30-359e-3cd1-8eb3-38e64873fbbf | -9.03698 | -67.45687 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb00c458-ebd0-3af0-a19f-99eb6eed96cd | -9.0365 | -67.45548 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 98e020ed-53ac-3197-99c6-c057a6178665 | -9.03642 | -67.4614 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2989d914-5e8b-3206-9c83-a3cf38dadf9e | -9.0359 | -67.46 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 60dc8b66-20ed-3f5c-84c9-e85ccda5ff2e | -9.03585 | -67.46593 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e9d443d9-9ee4-3331-9c43-797f6da41e4a | -9.0353 | -67.46452 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9933afcc-ded6-3a14-bbec-23545473feb0 | -9.03263 | -67.4424 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7bf39c4-8dbd-366d-a89d-4e0703778f93 | -9.03207 | -67.44696 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05751240-9523-3e27-afdf-8c9339d1eaf1 | -9.03165 | -67.44559 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18a38fd1-b2ab-3f44-ab5d-5ffabd7e759e | -9.03093 | -67.45602 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a92b344e-4f9c-320c-8376-9c18f2d5e05b | -9.03037 | -67.46054 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb83492d-9e82-3041-9d50-e3bc672fb8f6 | -9.41329 | -68.85064 | 2024-10-19 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ed82b37-5483-3417-93cb-881337b251eb | -10.76659 | -68.80976 | 2024-10-19 06:31:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7df86ce-7c85-3174-b27a-7df5815b4b90 | -10.76293 | -68.80692 | 2024-10-19 06:31:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51597e1c-3c70-3973-ac06-6c20ac6875c3 | -10.76245 | -68.81084 | 2024-10-19 06:31:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a604c11-968a-35d6-a86d-75ea7b6bd82d | -10.76091 | -68.80902 | 2024-10-19 06:31:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58f5d6e1-cccd-3f97-a470-10dbe79c7723 | -5.71695 | -68.6847 | 2024-10-19 06:31:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cd710ae5-3f8b-3725-b2e2-85c8f507bdf4 | -5.71648 | -68.68802 | 2024-10-19 06:31:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 445fe7a0-dc19-3c76-8726-1b124d8439b1 | -5.71162 | -68.68391 | 2024-10-19 06:31:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4550ba0a-6b90-37a8-854b-ea68928901aa | -7.79246 | -70.0562 | 2024-10-19 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c36043c5-e574-3817-8d09-b4c0170b45e3 | -8.02313 | -70.07483 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d90eac80-d39f-3664-87b7-6b5638ae46ec | -8.87742 | -69.33952 | 2024-10-19 06:31:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc6f685d-1d11-3c88-a593-b5a2bdde9f36 | -8.87558 | -69.33891 | 2024-10-19 06:31:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33910cc5-77a6-3679-b266-982c23baf126 | -8.76644 | -68.88188 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9723b8b7-0c96-32f0-9687-43d76f8c115b | -8.76598 | -68.88541 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e290884c-b0c6-3453-9bb9-0385dd1d1372 | -8.72523 | -68.93511 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a24709bb-68e3-3af8-a961-5a68ef9ef5ac | -8.72475 | -68.93864 | 2024-10-19 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5adecd13-9792-3421-8a80-b1ef90ec41a6 | -8.62208 | -69.73426 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24dd48c6-37b6-3aae-ac48-cdd0062d5e55 | -8.62072 | -69.73367 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 796bc83a-0d9f-37f0-a931-e7f0f728321a | -8.6173 | -69.73046 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7609dbb-ed80-345f-b10f-1001f72dcd25 | -8.6169 | -69.73359 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0eb755d1-33e5-3a0a-9281-b0d4e7fa5189 | -8.61608 | -69.73978 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6113e3ec-71da-37f5-9581-02117a4d7313 | -8.61553 | -69.73301 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37e3dbde-9d39-3fd3-841b-d2eb80589d54 | -8.5598 | -69.98505 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7754294a-bf8f-3b98-bb97-c422869f96d5 | -8.5547 | -69.98441 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e7acfbe-3075-3c82-aef8-f6b428a5f674 | -8.55429 | -69.98741 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47d8001b-0a3e-3ae1-82f7-deaa446d9776 | -8.52261 | -69.99191 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37969d8d-501e-3105-9bfb-dd8adcab7ce1 | -8.5222 | -69.99491 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d425c897-03fc-38c1-a2d4-e675c994547e | -8.39975 | -70.1134 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 012a721b-a5ba-3688-bcad-5137a80d0643 | -6.68556 | -70.04182 | 2024-10-19 06:31:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 181743cd-7260-322b-b2cd-83b41dec915f | -8.2002 | -70.2342 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b8d92b9-144e-3c74-a029-3f7c096c443d | -8.85482 | -71.33604 | 2024-10-19 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18d9b86c-9480-391f-b23f-7b55a926c285 | -8.56146 | -70.49421 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f185db0c-d76e-3bb9-9fe9-999f28f53e3f | -8.50172 | -71.43077 | 2024-10-19 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f451b52-ed2e-3fb1-bae8-276ed521d214 | -8.39384 | -70.53589 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d88fb41-6230-3e6a-bca0-64f457933542 | -8.392 | -70.53471 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 193f7629-d08e-3176-aca1-1c0fcdd222d5 | -8.38896 | -70.5352 | 2024-10-19 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d73edf8-a1d9-3dae-b644-b112cf0aa035 | -7.84018 | -72.76389 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6100d746-9917-3f6f-b93d-8074c4d97fe6 | -7.82405 | -72.8457 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b940c8a-f50c-30f7-ad89-80f0af139dc7 | -7.82351 | -72.84938 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dff857a-e265-3f6b-ad25-727daf0c374b | -7.81507 | -72.87847 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2484b245-baca-3372-a431-f9ac824de7ee | -7.81094 | -72.8779 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f24d631-ecc3-3b40-9b8e-9c3a33036e59 | -7.78379 | -73.09341 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86237834-8578-33a7-94ac-d92b52499a40 | -7.78326 | -73.097 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0393bf0-6565-33fd-972c-754fa855ee5b | -7.77971 | -73.09286 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c40425b-0906-3ff7-9003-439bd9540307 | -7.77816 | -73.10358 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df91d6cb-776d-3e6c-b572-aacf7e78217a | -7.70373 | -73.04536 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5dd2455-d0a1-387f-bdb8-0f5acfaa1223 | -7.69966 | -73.04478 | 2024-10-19 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e6d4e87-a935-3398-9f24-ab557b78bd69 | -7.67262 | -73.05912 | 2024-10-19 06:31:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ab7093d-0577-3938-9891-2d134b68efe1 | -7.6721 | -73.06271 | 2024-10-19 06:31:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c6a7013-c00a-3bc6-9d50-6e81975c4b12 | -7.66805 | -73.06206 | 2024-10-19 06:31:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52a195d3-c4db-3c4d-becd-894118cbde7c | -7.61619 | -73.04721 | 2024-10-19 06:31:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34828444-6428-3852-a8dc-180f00c81745 | -7.36817 | -72.84867 | 2024-10-19 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0626dd89-de67-3f98-8a4f-ed4f069033c5 | -7.3351 | -72.47993 | 2024-10-19 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ea822fa-03cb-34f5-8ddf-d86b902b5917 | -7.32433 | -72.75634 | 2024-10-19 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e1e11ab9-c81c-3d91-bd81-43405613ff38 | -7.32378 | -72.76005 | 2024-10-19 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| c9fb03d4-7162-34ce-ac02-475630e2f7ba | -7.32021 | -72.75573 | 2024-10-19 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 516a4ece-88a5-3e0a-b037-21a7121bf9f6 | -7.31966 | -72.75944 | 2024-10-19 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| daa193d9-5528-33a7-a727-d3a55e67eafc | -6.92645 | -71.50134 | 2024-10-19 06:31:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c309cfa-06de-3b15-86dd-0621cf040aeb | -7.65787 | -73.24497 | 2024-10-19 06:31:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31775187-fe32-34cb-a6df-614f1b655ff9 | -7.65386 | -73.24438 | 2024-10-19 06:31:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f72edbb2-fa30-34a7-95ce-b4054126e7bf | -10.89308 | -69.42702 | 2024-10-19 06:33:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff75c2a0-24b3-358b-b28d-361f44b95982 | -10.88761 | -69.42633 | 2024-10-19 06:33:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e30f45e-c955-33c9-9ccd-7e1f5583dc64 | -7.3271 | -72.7538 | 2024-10-19 06:45:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 90052e21-bd21-33c7-87a4-87354fd68547 | -9.0344 | -67.4641 | 2024-10-19 06:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| af7c54f3-0395-3b12-95ed-2505d68de5dd | -9.0345 | -67.4455 | 2024-10-19 06:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 37251d43-a410-3743-8fad-85f4c9b65416 | -12.023 | -63.4998 | 2024-10-19 06:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 30029148-c629-3146-8890-84e0aec2ca98 | -12.004 | -63.5199 | 2024-10-19 06:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3b08b5fc-8a6d-3160-a6d7-7195611517bd | -12.0041 | -63.5008 | 2024-10-19 06:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 62a68fb3-078d-3a43-a458-82df326d574c | -12.0228 | -63.5189 | 2024-10-19 06:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9ce775e7-2c99-399f-a214-2aa203452d22 | -7.3271 | -72.7538 | 2024-10-19 06:55:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |


[Clique aqui para ver as próximas entradas](README50.md)
