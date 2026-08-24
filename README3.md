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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3334de5-b37f-3e53-a3ed-b2131266ab17 | -10.43244 | -50.43417 | 2026-08-24 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 18c0726e-6626-3994-a98f-15fd39b347bf | -11.15925 | -54.0079 | 2026-08-24 00:09:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 487453ac-1e22-3b56-a215-c02ad9baf3a7 | -10.87269 | -51.02849 | 2026-08-24 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 38d05c3d-c37e-3262-b6a3-9e2a2f746e6c | -8.57959 | -55.27614 | 2026-08-24 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cf95617d-211c-3a73-aae3-f60b02b5cc54 | -6.34018 | -54.75974 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| dcb543ba-7461-3fe7-87fa-6009521d0a07 | -4.4838 | -54.86746 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5bbdc06d-7886-3762-abbd-a6ed72ed62e2 | -6.62506 | -53.35804 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 584b2d76-0a33-380b-89db-50451398f737 | -10.79743 | -50.95214 | 2026-08-24 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 8a0130b5-c359-342b-8ab5-0ef997d91c5d | -6.38677 | -54.98132 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 80e50ba3-a48e-3336-b7c1-f6a99d288adb | -6.82576 | -52.50582 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cd9d8769-3024-323f-874a-a0392171c701 | -6.74103 | -59.65556 | 2026-08-24 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e6bacf58-8946-3798-aea6-7cd82ef866fc | -3.5421 | -48.17849 | 2026-08-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c0c6080a-d250-3824-818e-b55810f2ffd0 | -8.57272 | -49.97482 | 2026-08-24 00:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f118f59a-4204-3310-b0a1-0d7e3e1e49e2 | -6.32979 | -54.76112 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a137afc1-cd8d-374f-974f-942d529e6cda | -7.23771 | -49.86598 | 2026-08-24 00:09:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 13f4e99a-7bcf-3c98-aadb-c539479dccab | -6.22727 | -55.62095 | 2026-08-24 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 3fcdf310-b3a9-3b74-b699-2697e5085b0e | -8.58277 | -49.98245 | 2026-08-24 00:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f50a9367-fcf1-367d-a205-c3e3c7c02714 | -2.56002 | -47.26022 | 2026-08-24 00:09:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6ce790e8-8c9a-3efa-8d75-8f874470a096 | -6.86192 | -59.41236 | 2026-08-24 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 2cf2bb2d-2bb9-3212-92a6-0ac425046b42 | -6.22056 | -55.92386 | 2026-08-24 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 404eb5ac-882c-3b66-8c10-fc72b13b84ec | -6.14639 | -57.93489 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| abf8e7b3-2835-3207-9e5e-7bbe1a9dca2e | -6.86481 | -59.41768 | 2026-08-24 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 05847046-ca76-3378-a663-6f702ac60a12 | -9.67857 | -55.08523 | 2026-08-24 00:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 8417ac8f-e7b3-33f1-9c8c-45821101875b | -6.33787 | -54.76645 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 4c233b6b-2501-31e6-b6ba-319c8b1b9244 | -8.10242 | -47.49194 | 2026-08-24 00:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ed55f925-215e-3d8b-a2cb-2667f3b8e974 | -10.79867 | -50.96127 | 2026-08-24 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 740292ac-a6f5-3a3f-bf3e-c29eb4b8e221 | -5.97532 | -52.21368 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 30f4926d-af13-3782-b1ac-23a6114f8405 | -5.93807 | -57.73368 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 6d3bdc7f-6b56-3b44-87f5-adb06ac7f5f2 | -6.83489 | -52.50465 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| cd64489f-8511-3273-87a9-07cd24d96b5a | -10.01434 | -46.83064 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0377f181-84cf-3421-ae88-c842af9b5917 | -3.59777 | -54.05091 | 2026-08-24 00:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 088cfe3e-2f95-3aa9-b3e2-65fedadd079f | -6.33627 | -54.75394 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| f884737c-1153-3162-a3d7-5a3b1ef22554 | -5.51059 | -49.57837 | 2026-08-24 00:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d16722e9-b237-37a3-86ca-7182d48f9d72 | -7.97043 | -45.25447 | 2026-08-24 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 8306032c-03fd-3db5-893b-cc160c52a6e0 | -11.59461 | -56.29034 | 2026-08-24 00:09:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 948a50e6-3069-3f1a-b87f-64425697c3a9 | -11.20808 | -55.04419 | 2026-08-24 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6bd08b9d-2a57-39dd-b0e8-42dc1a0e1379 | -5.01025 | -56.13753 | 2026-08-24 00:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 5fa9a943-6b18-31c9-8049-2a57445f6a84 | -5.72859 | -51.95556 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c3d44336-bcce-3d70-9851-196d343abe8d | -7.28558 | -45.35915 | 2026-08-24 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d209753d-58dd-33ed-8617-3a2ed3e346ac | -10.82594 | -50.95111 | 2026-08-24 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| d5f9b1aa-c813-3e6f-9d86-0849b66cee4f | -3.01396 | -51.05169 | 2026-08-24 00:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d10ad1f-26b7-339f-bd6d-5f9bebb140b0 | -8.57396 | -49.98373 | 2026-08-24 00:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b1944844-d29e-3eb1-9d58-edf4034f3b6a | -6.23739 | -49.96618 | 2026-08-24 00:09:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 76805d55-11ff-3f53-8e24-44a73f703e59 | -8.79814 | -48.31434 | 2026-08-24 00:09:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e71c0531-6784-33a2-9fb5-99b6a447d826 | -6.11939 | -57.82831 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 029feda6-1e40-39ca-aea3-03692956c3dc | -6.41371 | -48.58469 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 759cb8fb-ef4b-3d17-86e2-30853573fccd | -7.98462 | -45.26904 | 2026-08-24 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 35476a23-3759-3922-9694-ac62716ab891 | -4.42273 | -54.94236 | 2026-08-24 00:09:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c4d452c7-9397-3c98-a3c8-2688ec1dc41e | -8.09477 | -51.67095 | 2026-08-24 00:09:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3f17b586-1467-370c-87e9-0a78a36cbd5c | -7.98209 | -45.25262 | 2026-08-24 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 839198e3-143e-34e8-870a-541db9286268 | -10.36468 | -50.39839 | 2026-08-24 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dca9a200-74f1-36b6-89cb-a506ca62b924 | -6.3385 | -54.74726 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 3ac575fe-3730-3e00-8b25-e489171fb8f2 | -5.97655 | -52.22272 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ec0cbf01-1c38-376b-a202-3846fa32ba90 | -10.73391 | -47.97769 | 2026-08-24 00:09:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| fa3ccb5f-0868-3589-91cb-e69b8703aa6c | -3.26251 | -49.52806 | 2026-08-24 00:09:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0fe2d2cb-0087-3f38-ae7c-c1b153d9e31d | -5.06802 | -49.38555 | 2026-08-24 00:09:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a5ab05e1-ee19-3e3a-9adb-c7c42a7ba128 | -5.78517 | -57.55684 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| bce132c3-e201-305e-bcf6-1ffac626014f | -8.10324 | -47.4855 | 2026-08-24 00:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 2ef7c253-5588-3c76-b8b1-3f1b37621dda | -2.57095 | -47.25861 | 2026-08-24 00:09:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d840d33b-7981-3a9c-993e-e40171d3a06f | -3.96799 | -48.95753 | 2026-08-24 00:09:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 6056f58d-9932-3043-a90b-05e72fdd2891 | -5.0772 | -49.38423 | 2026-08-24 00:09:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f3752d89-dfa3-3d5a-badb-f6863e0b97bd | -1.50438 | -53.8868 | 2026-08-24 00:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b43b178f-5460-391d-ae32-1aecc21705fc | -5.99492 | -52.14865 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5dfed521-6983-37bb-8fc3-f4a671aa40d8 | -10.81703 | -50.95236 | 2026-08-24 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7c6caaf6-cb4c-30a7-81dc-fb61a98ebbee | -6.61192 | -58.3933 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 566170f8-2b3e-3f07-b435-d3149ba4cc4a | -5.00857 | -47.07112 | 2026-08-24 00:09:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c0d61190-5896-3ac7-bd0e-7b4e1fed8821 | -7.25748 | -49.86653 | 2026-08-24 00:09:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4e740585-3d9e-388b-b612-0258288e2acb | -5.77489 | -57.57859 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f0074298-e3e3-38ac-9882-900471b2f797 | -10.80813 | -50.95362 | 2026-08-24 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 055f5257-13c0-347d-8c60-39605c073385 | -9.22564 | -60.39133 | 2026-08-24 00:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 48088b27-1f2d-3078-94ac-fd6a7e4210c4 | -7.97295 | -45.27078 | 2026-08-24 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 47.1 |
| a4b33257-c604-3ac7-9cdf-70b9036addec | -10.37349 | -50.39713 | 2026-08-24 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 10675959-7870-34af-a093-9e4996620ebb | -6.01406 | -52.15548 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b2ca243d-da5d-3de7-b27e-c5935d0dc11f | -6.63319 | -53.34637 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a287a810-bae4-3d88-ad84-cc3d0608189f | -2.50248 | -48.14026 | 2026-08-24 00:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ee34decb-a88b-3b69-91e7-49d06178bf79 | -4.99888 | -56.13882 | 2026-08-24 00:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 4e1d5555-3442-35d7-a649-b549bcb22121 | -2.56892 | -47.24453 | 2026-08-24 00:09:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1c160baa-6a3d-3201-a92b-43af5c6d0141 | -8.87885 | -50.59632 | 2026-08-24 00:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0dda0187-e6cc-3473-a09a-b1d05c7f5ed0 | -7.37662 | -45.81177 | 2026-08-24 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 08d648cb-f33b-39d7-95fa-7af6db7f76bf | -5.69313 | -53.74305 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a5c06f01-44eb-363f-b6b1-a171176d1c64 | -6.22212 | -55.92924 | 2026-08-24 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 776e486e-2ffb-3c1d-b7b3-cd8771ff4f7e | -6.68849 | -58.73484 | 2026-08-24 00:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5ca44393-c366-3922-a590-0fb17fb8c2bc | -7.48705 | -55.34153 | 2026-08-24 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f83724a6-0ed9-3d4b-9ee6-e2467c0a768c | -8.10082 | -47.48074 | 2026-08-24 00:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c2c25588-247c-343a-8d4f-badb52154e45 | -7.26505 | -49.92041 | 2026-08-24 00:09:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4742eaf5-06d9-3726-b2d2-997c8126fa60 | -10.73536 | -47.98783 | 2026-08-24 00:09:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9feabe74-3b66-32f2-9d70-df48b3af527d | -6.61706 | -58.38597 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5caa384e-e7e2-3854-a4ef-198df3868eb6 | -5.7865 | -57.57081 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 02f15632-41ef-379d-afc5-f82740902b13 | -7.36307 | -45.79832 | 2026-08-24 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 358.7 |
| 43babe05-0fee-3c07-9e10-0e69a4bad014 | -10.406 | -50.43794 | 2026-08-24 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9766caa6-2693-39d1-9b05-9cee9df9385b | -7.97547 | -45.28708 | 2026-08-24 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6c8bdf93-f6fc-3e63-b041-05438912da37 | -10.72181 | -47.95934 | 2026-08-24 00:09:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e2774822-93f6-3b44-bd66-a386859cc626 | -6.25977 | -55.42125 | 2026-08-24 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0b32910c-673b-391d-ae49-cfbceb02b71f | -5.78155 | -50.19933 | 2026-08-24 00:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f70f6a16-11d7-3c3e-9ba6-29db54ad49fa | -9.4654 | -56.922 | 2026-08-24 00:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| b251675d-6595-3fd0-91ea-8407c3f83cb9 | -9.68038 | -55.10027 | 2026-08-24 00:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 5c4d3d99-aadb-3079-8316-bb837a6492e8 | -7.37437 | -45.79657 | 2026-08-24 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| feb0cf6a-8275-3673-8343-9a2ae58bd0a0 | -5.06665 | -49.37592 | 2026-08-24 00:09:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 9cf489d5-ad03-3738-b827-baf1fe7de995 | -11.69007 | -54.59014 | 2026-08-24 00:09:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e7b69968-2e7b-3b6f-a09b-efc4acfd97c7 | -8.54593 | -55.28035 | 2026-08-24 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |


[Clique aqui para ver as próximas entradas](README4.md)
