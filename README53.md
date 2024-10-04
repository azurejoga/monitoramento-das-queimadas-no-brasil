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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80128848-e0a8-342b-874f-7d2e2a8525be | -19.86882 | -42.34562 | 2024-10-04 03:19:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 48a31364-9389-3653-a55c-73d283682cbf | -19.85966 | -42.38776 | 2024-10-04 03:19:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 54042212-6684-3d65-8fd4-d15b40a53e0c | -19.85526 | -42.38127 | 2024-10-04 03:19:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2f138717-abc4-3747-b5b4-b58ca390c036 | -19.85421 | -42.38611 | 2024-10-04 03:19:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d2794dcf-d9da-3e3d-9564-be28080ad767 | -19.85103 | -42.374 | 2024-10-04 03:19:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 11762242-e5b4-312b-aad4-3fd7505168c1 | -19.84994 | -42.37899 | 2024-10-04 03:19:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 83ab4361-59d8-39b9-8ce7-2b974fc1bd47 | -19.84559 | -42.37233 | 2024-10-04 03:19:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| fb473eee-e218-36fa-bd40-0729e3406c33 | -19.84456 | -42.37703 | 2024-10-04 03:19:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 1ca6aefc-694d-3fec-858b-6156d694e542 | -20.5585 | -42.95647 | 2024-10-04 03:19:00 | NOAA-20 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e7b5fc2-eced-34bb-8f81-b00872bca056 | -20.5576 | -42.96049 | 2024-10-04 03:19:00 | NOAA-20 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 58ac5f9f-2116-3bf1-ad2b-eb190fb4b01f | -20.47114 | -43.1809 | 2024-10-04 03:19:00 | NOAA-20 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 82e54fc7-412c-38e8-8f40-1d3bbb17319f | -20.46451 | -43.18356 | 2024-10-04 03:19:00 | NOAA-20 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 08dda595-081f-3d7f-940e-8b49106311b8 | -20.46357 | -43.18781 | 2024-10-04 03:19:00 | NOAA-20 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9ab0b6a1-c477-367d-bcc3-86038e946016 | -20.45876 | -43.18228 | 2024-10-04 03:19:00 | NOAA-20 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cd14304e-6c99-3f7e-9777-aa439138c32f | -20.40264 | -43.10784 | 2024-10-04 03:19:00 | NOAA-20 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6f161dd3-c935-37f5-926a-37933c00117c | -20.40178 | -43.11178 | 2024-10-04 03:19:00 | NOAA-20 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ffdf44cf-946a-3b1f-9d56-39afcec90a13 | -20.39688 | -43.10667 | 2024-10-04 03:19:00 | NOAA-20 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a2907e0e-2dc8-3a52-9e67-18aaa5e46be7 | -20.39687 | -43.10902 | 2024-10-04 03:19:00 | NOAA-20 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 465d403a-8701-375b-916b-60d600503b41 | -20.39598 | -43.1108 | 2024-10-04 03:19:00 | NOAA-20 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ef4f8beb-c3de-30cc-997c-d9b4e4d2eb5d | -20.37644 | -43.25446 | 2024-10-04 03:19:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28aaecf5-38d9-332f-9418-01f7cc06484c | -20.2533 | -43.1813 | 2024-10-04 03:19:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 610b06e3-2d53-3e99-896d-f3a3c4058d41 | -20.25322 | -43.18194 | 2024-10-04 03:19:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 39ceb398-7a4b-3a8d-a820-37d62d1e552f | -20.24745 | -43.18062 | 2024-10-04 03:19:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 09ea4088-ba30-3949-89d3-88878eddf458 | -20.24652 | -43.18482 | 2024-10-04 03:19:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 85338ac3-8591-3eab-8a2f-ea7d77ac3a60 | -20.2398 | -43.18779 | 2024-10-04 03:19:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 3b2b09ed-bd36-3c2a-90cc-578ae1ff6fd2 | -20.23883 | -43.19215 | 2024-10-04 03:19:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| bea7cff8-5f1f-3c5b-96ca-ec4e4aa76445 | -20.1025 | -43.4263 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d5b990f8-1a1d-33c3-bbb3-d4f49673b5f9 | -20.10192 | -43.42888 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0de15a98-0081-3f62-85e2-7b52c099d630 | -20.10135 | -43.43142 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 37d181ac-6583-386c-a568-8300a170b5fb | -20.10097 | -43.42315 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 4d5c0c32-ee33-3266-bf70-3f886d243991 | -20.10077 | -43.43396 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 98e896fb-ab7e-37ca-9212-78dde8468201 | -20.10038 | -43.42575 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 60f63d53-21f0-3c04-864d-43f4034f3512 | -20.10015 | -43.43675 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| db2e921d-8026-3dce-b1ed-ba3138abbe1d | -20.09979 | -43.42829 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| 322a82fc-7d6c-35c2-b7e1-3b1446850315 | -20.09942 | -43.44 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f6059dbd-d8a1-3278-9347-60ac89088617 | -20.09919 | -43.43089 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| 40791b90-fb8f-3796-82c9-beb205faffe7 | -20.09858 | -43.43356 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| b37b9fad-d883-3b18-98e2-707a821eb6c1 | -20.09792 | -43.43642 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 57e41241-99d7-3be5-ba0b-45d5e7f0aa25 | -20.09719 | -43.4396 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7a5ef2b4-f2c7-3053-8558-c87eb17e149b | -20.09717 | -43.4226 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 8df33966-c109-38b0-ab62-d9a93007a141 | -20.0966 | -43.4251 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.4 |
| 52348ccd-f076-3120-a976-ff6d727fd6e0 | -20.09606 | -43.42751 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.4 |
| 66e0e341-26e7-36c8-a9cf-8e615647a564 | -20.09543 | -43.43032 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.7 |
| ec75a14d-aaaa-3bb1-a089-4989ee7242b1 | -20.09496 | -43.42245 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 21b24164-9ed5-3206-8a1d-b3fdfe16f72f | -20.09474 | -43.43337 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.7 |
| 0710f93d-7646-3a9a-b939-7bde840e0dd3 | -20.09436 | -43.42507 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1f59a146-a5ab-33da-9745-a7de55a57c2a | -20.09403 | -43.43653 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 035fa3c1-0098-3874-a3e4-9979d2887edf | -20.09374 | -43.42776 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 46ef40b1-e0fa-3ba7-93d7-e8b298a0cd60 | -20.09307 | -43.43069 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cfdce3d5-1105-3ccf-888d-fa1995f0573b | -20.09237 | -43.43371 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3f1f3f0b-ce20-395f-9ba3-21e6e875eb9a | -20.0917 | -43.41951 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 40e73f37-9d39-39e3-aa0b-e8bc0984f5d1 | -20.09099 | -43.42269 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3254d9a9-c056-3575-94bd-34956172d4d8 | -20.09088 | -43.4402 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2a2602cc-1dd9-3fb2-b133-042a20b57e63 | -20.09005 | -43.44376 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e831a159-7596-3aff-8e45-cc83432407c0 | -20.08948 | -43.41949 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 72c04d21-6c92-3c4f-a64f-884cacb83332 | -20.08873 | -43.42274 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 69adec5c-f35a-3d5c-adc1-8a00cc5b5a13 | -20.08801 | -43.42584 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4207d178-4e68-3044-b1e0-48653ba2d956 | -20.08765 | -43.43754 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6a955f40-ca97-39a5-92f2-19b7b0aa1529 | -20.0869 | -43.44086 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4a41b0a5-36de-3578-9179-f6db2d4fe675 | -20.08609 | -43.44449 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 969a6662-41d0-3843-bbeb-5f2407e153b9 | -20.08597 | -43.4347 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| df568bad-8e2d-32de-adcb-ee6bc5603c0e | -20.08525 | -43.43784 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ab17e014-b438-3f15-abd5-33762caf7008 | -20.08444 | -43.44131 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 792dd3b1-6e79-3a88-91e6-90274a1a50cb | -20.08359 | -43.44502 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e7cd8dd3-cce0-37b9-a20a-ac3cceca63a2 | -20.08339 | -43.42911 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| edf95d91-2ca7-3117-b0fc-2f6b3fbe4931 | -20.0827 | -43.43218 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 48303389-65a4-313e-91f0-4357d577606f | -20.08199 | -43.43531 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 145a8cf0-3731-3802-9166-11e84bc5d7fb | -20.08124 | -43.43863 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2bef1d61-c41b-331e-9f29-1000e0b9699e | -20.07955 | -43.44621 | 2024-10-04 03:19:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| c35d17c8-d332-3b42-82bb-19f31514e64f | -21.97029 | -43.33807 | 2024-10-04 03:19:00 | NOAA-20 | SIMÃO PEREIRA | MINAS GERAIS | Brasil | 3167509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1920a6c4-425a-3151-a278-ae6024531828 | -21.96773 | -43.33762 | 2024-10-04 03:19:00 | NOAA-20 | SIMÃO PEREIRA | MINAS GERAIS | Brasil | 3167509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c6b1f82e-11ae-3dae-8c54-4c9a6ee4f2d7 | -21.07966 | -42.86615 | 2024-10-04 03:19:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7fe37e74-988d-328b-a34b-53511cd86646 | -21.0741 | -42.86483 | 2024-10-04 03:19:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b77518f-5a07-3cc7-93fe-c035e4e2608a | -21.76244 | -45.55149 | 2024-10-04 03:19:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a5149f65-aff5-35fb-abdc-1456cb4a419f | -19.69995 | -46.79454 | 2024-10-04 03:19:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 5c2ebb52-7754-3f9c-aa73-e4540e55e979 | -20.31018 | -46.86606 | 2024-10-04 03:19:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2c565583-681e-3e89-b2b9-f5ecd203bf35 | -20.31202 | -46.85868 | 2024-10-04 03:19:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 19201151-bf9a-349f-af5a-8f9803fe823d | -19.42688 | -43.90335 | 2024-10-04 03:19:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 186d86a9-c610-3b64-895d-636cf054a5b1 | -19.42083 | -43.9017 | 2024-10-04 03:19:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c8c6746-2836-31bb-964f-62233a9e3cde | -21.76101 | -45.55727 | 2024-10-04 03:19:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fbdc490f-03f4-3531-a9c4-f7fa5aaccf24 | -20.52141 | -44.90229 | 2024-10-04 03:19:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eab5595c-9190-3b3a-bd9b-178f84dfd76d | -20.52025 | -44.90725 | 2024-10-04 03:19:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 317b2449-0fb2-3655-afd8-07cfb6f2181c | -20.51764 | -44.89875 | 2024-10-04 03:19:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5f19ae3a-69d3-3737-a784-0d8cac79a412 | -20.51646 | -44.90364 | 2024-10-04 03:19:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8a3b9915-5ff9-3fdf-a3dd-2ad8933fa4c5 | -20.51521 | -44.90886 | 2024-10-04 03:19:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dabe461d-72e9-3935-a87c-3c33da612be4 | -20.51513 | -44.90061 | 2024-10-04 03:19:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e509911d-d900-3cd1-b35d-9cd4c5e17a30 | -20.51396 | -44.90562 | 2024-10-04 03:19:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 35b0a01a-acc2-31e6-ba73-431a919c5fe0 | -21.76152 | -45.5535 | 2024-10-04 03:19:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b21b5105-a8a5-3a52-bec4-ab01e617a3f6 | -20.42376 | -43.76777 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0d8fe113-d0fa-33a4-a185-b9202aeec33f | -20.35217 | -43.88826 | 2024-10-04 03:19:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2d315ac8-c129-372e-a534-869f8da3e4ec | -20.34745 | -43.88133 | 2024-10-04 03:19:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0596185e-a3a7-300d-bd5d-e73c9176c732 | -20.34637 | -43.88602 | 2024-10-04 03:19:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 70531bce-fe4d-3867-91aa-d5401f07703e | -20.3455 | -43.88249 | 2024-10-04 03:19:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| aa60d4d4-3388-39fe-b503-7515dbdc22fa | -20.27607 | -44.1064 | 2024-10-04 03:19:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c08286d-49dc-3f4c-8874-ad3f5bf0eaa7 | -20.27493 | -44.11126 | 2024-10-04 03:19:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 185355cd-89d5-35a2-a4ac-d739efe6c751 | -20.15287 | -43.54875 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dacb61bd-dc28-33b5-8f42-79ec18b09ab0 | -20.15188 | -43.55313 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| afe5a5c9-2375-332a-875d-625e985c5c6c | -20.13947 | -43.86611 | 2024-10-04 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a075efc8-d293-36a5-8818-8b88e4d0c28d | -20.1332 | -43.86586 | 2024-10-04 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dc369214-bef3-39ee-9e04-ff8f2f80ea49 | -20.12756 | -43.52351 | 2024-10-04 03:19:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |


[Clique aqui para ver as próximas entradas](README54.md)
