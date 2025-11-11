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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4bb0c78-9450-3416-b160-c5a72c0950d0 | -18.474 | -53.4058 | 2025-11-11 03:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3c5b18b4-02c0-3baf-9a13-d9efbd9a3301 | -19.742 | -58.0672 | 2025-11-11 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 5aeaba84-bb30-3916-9160-7b5bcbe876ee | -18.3827 | -54.9942 | 2025-11-11 03:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 6efe48ee-5076-3a3b-930e-ab16565a44d7 | -5.4241 | -44.6524 | 2025-11-11 03:10:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 1675dcf5-5c8c-39ea-97d8-6aeabf376262 | -4.7204 | -46.4497 | 2025-11-11 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 1db47097-38b2-3369-b41f-3aa7d0acf82e | -18.4026 | -54.9913 | 2025-11-11 03:10:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 91.8 |
| d1e0142a-0da0-3246-b580-8b349151a54a | -18.474 | -53.4058 | 2025-11-11 03:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4d0075aa-e2b2-365e-908b-c2e5192a6920 | -7.13067 | -41.26223 | 2025-11-11 03:10:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 09147c3a-9e89-3e93-aab1-70ed675707c3 | -4.45436 | -38.39083 | 2025-11-11 03:10:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 15e683fb-d2f1-3025-a981-2cf52e7f483a | -4.45348 | -38.39581 | 2025-11-11 03:10:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ae4df3d1-64f5-3960-aa43-28639733dbe1 | -6.59287 | -35.25274 | 2025-11-11 03:10:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 7.1 |
| bbc463eb-4d79-3046-a5bb-cdaa0aa0ab77 | -7.06808 | -39.68045 | 2025-11-11 03:10:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 54c06d26-1f0e-33d1-bb48-c6e38afa85ee | -6.59495 | -35.249 | 2025-11-11 03:10:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 967d4b93-5b11-32c6-b10a-07d9eaab1519 | -5.32703 | -35.55463 | 2025-11-11 03:10:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 44209a10-c3bc-3aab-a11a-b0407b27e3ce | -9.91115 | -36.52288 | 2025-11-11 03:10:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a0b3b25f-abe1-3914-825b-a06cc08d6450 | -6.86013 | -35.17494 | 2025-11-11 03:10:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ba98ccde-87c8-327f-89a9-d428e0e67167 | -6.71796 | -38.55326 | 2025-11-11 03:10:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d27479dd-c559-379c-bce6-bc4b6cddd446 | -6.7188 | -38.54862 | 2025-11-11 03:10:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a4385fe0-a1ad-3cb4-81dc-d39e60c58b0f | -6.85519 | -35.1743 | 2025-11-11 03:10:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8da441ad-54c3-367f-a99a-3461d606cc28 | -6.59783 | -35.25354 | 2025-11-11 03:10:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3c07c6bf-989e-3cb2-9b14-aa9746ebb6b6 | -6.594 | -35.25437 | 2025-11-11 03:10:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a0c6256b-919a-3a12-a08a-6b126a105c01 | -6.3346 | -38.92567 | 2025-11-11 03:10:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0266e9a2-024e-35bf-aff1-41d5f70de09f | -8.84776 | -35.75036 | 2025-11-11 03:10:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 89a7c5ab-1853-33d6-bc5d-cfdaf83b0ec9 | -5.33218 | -35.55557 | 2025-11-11 03:10:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f27fda6-e292-3825-8b04-a5bfef4af479 | -7.06909 | -39.67499 | 2025-11-11 03:10:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6582f93a-8f0d-30f7-97ce-3916caf68552 | -6.85616 | -35.16877 | 2025-11-11 03:10:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| eaf32bb6-e116-355f-890a-8b02eb10b1c0 | -5.4241 | -44.6524 | 2025-11-11 03:20:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6f46cef0-f2e3-3324-95e8-157eb9bcd143 | -4.7204 | -46.4497 | 2025-11-11 03:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| f5e55ba8-5c5d-3ad5-bc23-3f7bd031166d | -5.4241 | -44.6524 | 2025-11-11 03:30:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 49ace37b-4f18-33c9-88a9-12805b91a8cb | -4.7204 | -46.4497 | 2025-11-11 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| f1150228-4ffc-3257-bb30-9af38e0ddfcf | -18.474 | -53.4058 | 2025-11-11 03:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 70a0447f-8b56-39a7-a3af-bdd562a01946 | -3.85235 | -41.57896 | 2025-11-11 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 73c6864a-a7d0-3c98-92ed-34b720e76cc9 | -3.85182 | -41.58205 | 2025-11-11 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a2eda83-af4f-3f14-b977-1eeff136999c | -3.8575 | -41.57981 | 2025-11-11 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11f2b79b-3210-30b3-a6a4-718211419093 | -2.88946 | -40.48849 | 2025-11-11 03:38:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 467bb1fd-d60b-386a-a721-e13012e1cd00 | -4.45046 | -38.39579 | 2025-11-11 03:38:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| bf470a0e-4e79-3355-a47e-1de6b446bd97 | -4.45105 | -38.39216 | 2025-11-11 03:38:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3f42fa6c-e310-3d44-b757-2d0271d07e2d | -3.85644 | -41.58598 | 2025-11-11 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3461547f-3dd2-3fd7-8332-2acc1693c858 | -4.45574 | -38.3892 | 2025-11-11 03:38:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0597034d-1ae0-3534-8a8d-ceb145dbfb16 | -4.45515 | -38.39284 | 2025-11-11 03:38:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ef19ad59-bafb-3d19-96f6-e511162db308 | -3.43063 | -42.42482 | 2025-11-11 03:38:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 47d83518-8411-3fdb-9008-4fc78ba9ecbb | -3.85697 | -41.5829 | 2025-11-11 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 172cc53b-a870-3ca3-8c6d-7ba4889c88ac | -4.45925 | -38.39354 | 2025-11-11 03:38:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7a8b042-0b68-3bd9-9fcc-1bf99136c259 | -3.43124 | -42.4212 | 2025-11-11 03:38:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3420f686-f47f-3599-9f2d-1683d39a4ec7 | -3.85288 | -41.57587 | 2025-11-11 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb8c7981-3702-3f34-b6c0-c6d8599d224d | -5.33253 | -35.55537 | 2025-11-11 03:38:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 62090a20-f337-35d9-819a-018d0b940219 | -5.32906 | -35.55479 | 2025-11-11 03:38:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d4d5ed6a-e602-3884-9314-0d1e3775cb82 | -2.88858 | -40.49381 | 2025-11-11 03:38:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 795f7be0-d62f-37ff-8f9c-c438ae66855b | -4.23425 | -38.0424 | 2025-11-11 03:38:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f8657c2f-e757-3cfa-8ae0-ed6dd8acc94b | -4.7204 | -46.4497 | 2025-11-11 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| fc7399e0-b965-311e-a431-87038bf08df4 | -5.4241 | -44.6524 | 2025-11-11 03:40:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5f174526-30dd-3a6c-8d8f-f84b235236c8 | -6.06959 | -45.80658 | 2025-11-11 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4482031-510c-3682-b977-9557445ddda7 | -5.6434 | -41.07647 | 2025-11-11 03:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c6563eeb-f4b0-3735-87f4-3cc4654563f5 | -5.64147 | -41.07715 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 16a23115-852d-3664-993d-52d3fa0029ac | -9.67063 | -43.91159 | 2025-11-11 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 93eaf92b-3bf4-37f7-9505-08bdd9a9c0e8 | -11.04977 | -45.40723 | 2025-11-11 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 61a45e99-01ef-3cff-b581-1925e282dd70 | -5.42709 | -44.83727 | 2025-11-11 03:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c887bce5-3368-3855-ac41-2830a7bd959e | -7.13547 | -41.25097 | 2025-11-11 03:40:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5be2ac69-aa43-3263-8b76-0a438bb11c7c | -5.42243 | -44.84042 | 2025-11-11 03:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cbbbda6d-7bc0-3bac-87b1-736a8e18aae8 | -5.51322 | -44.39626 | 2025-11-11 03:40:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 964899f1-80ca-36c5-9b6d-1f1eb7f7cb29 | -6.44221 | -45.66615 | 2025-11-11 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a7937238-4651-3839-ac69-02cea7e02057 | -5.42935 | -44.65057 | 2025-11-11 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 244f2639-1546-3e74-a559-406873ea8bc3 | -4.74175 | -44.59962 | 2025-11-11 03:40:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee277d3a-d269-32c6-8545-45f6bf1de80e | -10.36712 | -39.40104 | 2025-11-11 03:40:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3734b7a-f893-362d-ad40-5c29fdefd1de | -10.50091 | -44.94148 | 2025-11-11 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d764c63-6bc5-3d85-b5d1-a6e0e964b8c3 | -6.54705 | -44.46341 | 2025-11-11 03:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2eb74137-0bb1-38dc-a87e-dffee8851d20 | -6.85818 | -35.17217 | 2025-11-11 03:40:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a302013d-cff5-3648-a0d3-e73edd4a4725 | -9.97751 | -44.45365 | 2025-11-11 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 827354ed-2f7a-3785-983b-47d662fed5b6 | -6.0898 | -41.55584 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fbbca2fd-287f-3327-a508-c49c307bd5ac | -10.84652 | -44.94334 | 2025-11-11 03:40:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b4d36e3c-3ef4-3d5e-80d6-039477cdfdf0 | -5.75208 | -40.80736 | 2025-11-11 03:40:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a449a135-da04-3bf4-864f-c7311c3ee1c0 | -9.66815 | -41.16768 | 2025-11-11 03:40:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d3368819-f1cc-3f77-8be7-dcd3a19409da | -5.39933 | -46.00535 | 2025-11-11 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6ccdaad-654e-3a33-9ef2-43bcdf3ab982 | -5.50723 | -44.39499 | 2025-11-11 03:40:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f49abf0-316a-30bd-9d43-a86f852f7399 | -5.42434 | -44.64841 | 2025-11-11 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6c4bf9e8-2713-3ed2-98e5-9e5d33d962ac | -10.2247 | -44.03902 | 2025-11-11 03:40:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| eb47e5be-1d6d-3a12-a443-6100da2f2a37 | -5.42091 | -44.83606 | 2025-11-11 03:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26ccd055-9fd2-36a4-9265-1d0533f50563 | -6.87062 | -39.10386 | 2025-11-11 03:40:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 54e4df5a-3620-3546-8552-7b4ba1874ace | -7.06972 | -39.68051 | 2025-11-11 03:40:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 57dd54e2-f69f-3020-bbda-7e03a83f408e | -11.05801 | -45.39604 | 2025-11-11 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70d5b02e-2da8-33fa-bd5d-7f3371ef309d | -8.50094 | -40.59051 | 2025-11-11 03:40:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6abb4c44-2f69-3053-bca7-950fcc7efd2b | -10.85224 | -44.94432 | 2025-11-11 03:40:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05af6023-c932-3343-9283-d5ad4df16bc1 | -6.37258 | -41.07272 | 2025-11-11 03:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1f47034d-ea88-3074-bef6-7bcf95f00d40 | -5.64052 | -41.08253 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7820fba6-ff56-336e-9b82-f8c72991e7a8 | -5.40555 | -45.24419 | 2025-11-11 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9e1c733-84d6-35b2-b4ad-7b53394ca873 | -7.13432 | -41.2601 | 2025-11-11 03:40:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f43f6551-ccd7-3e36-b458-7336472ca07e | -11.16971 | -43.57256 | 2025-11-11 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59bb4b39-e000-36d0-acfb-f94706bfccc6 | -5.40701 | -46.00103 | 2025-11-11 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dce8eeee-0715-345c-8361-927e07192fa6 | -5.60957 | -41.07104 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 29de4b24-9b28-36d8-9cb0-31bc7f4fa3f8 | -10.50663 | -44.94265 | 2025-11-11 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80f4fd7e-03d2-3afb-b07d-d33f99dbcd10 | -6.87124 | -39.10019 | 2025-11-11 03:40:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74ec60db-1661-3766-af97-a8e13c317495 | -7.07042 | -39.67649 | 2025-11-11 03:40:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6b753496-2fd2-30f9-9a74-8afc455044f8 | -6.07031 | -45.80916 | 2025-11-11 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3feab6f-fbef-31f5-9a1b-f569f28f2b72 | -7.19526 | -40.17178 | 2025-11-11 03:40:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c364dbf4-a002-3cfd-b6bc-905cac16b976 | -5.63768 | -41.08099 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3c85a27b-1f50-3ea2-beb3-e7aa40a61a90 | -4.72122 | -46.45263 | 2025-11-11 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| d697e9ef-bce3-3c90-827a-f774053186ea | -4.58545 | -44.31195 | 2025-11-11 03:40:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7bf04f6-f778-345d-86b7-a8bb0b3f31d5 | -6.83119 | -38.35048 | 2025-11-11 03:40:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 66136ff0-cc41-32fe-b446-a788e2a7bbd9 | -11.17431 | -43.57669 | 2025-11-11 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c986216-6669-30e3-8a45-e9c205282c5b | -9.67723 | -43.90829 | 2025-11-11 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README9.md)
