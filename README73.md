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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e06d4c7-7e00-351a-bcd5-10085638558c | -1.06041 | -48.2599 | 2024-10-28 05:21:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a6931b2-4fdc-3cbd-a509-899d9ca411cb | -1.05532 | -48.25562 | 2024-10-28 05:21:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e1ab47b-4ad0-38c4-9228-b1ff5bd8bfae | -1.05434 | -48.25901 | 2024-10-28 05:21:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a733288-cd7c-3bf9-a081-0ac71c1a7101 | -2.81489 | -48.4375 | 2024-10-28 05:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 885e1c7d-0448-305b-9fce-e31915e37640 | -2.81419 | -48.44215 | 2024-10-28 05:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e2eb78b-9225-3a4a-bdb2-0e3953733da5 | -2.76079 | -48.71493 | 2024-10-28 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 273f15b1-cfd3-3324-ab18-dad97ae4fa64 | -2.76014 | -48.71933 | 2024-10-28 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dc1e621-25c8-3bd5-9cf1-f6031a70e49d | -2.52718 | -47.44455 | 2024-10-28 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 62feb22d-2a58-3e3b-a882-99e7fecfba42 | -2.52145 | -47.43833 | 2024-10-28 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2ffddf45-4bc3-33f1-a228-d294593e71ff | -2.52063 | -47.44378 | 2024-10-28 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2b44c07-df7a-369b-aec8-41011162ea1c | -2.51983 | -47.44913 | 2024-10-28 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7758519f-d5dc-328e-ac00-1206aca45d71 | -2.49634 | -48.059 | 2024-10-28 05:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 012b8eae-0a20-3b07-a486-16c1adcb2064 | -2.49562 | -48.06387 | 2024-10-28 05:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14fee702-6352-39d3-a758-1bf6b7863dce | -2.4116 | -48.54863 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 942df8ce-2aff-396a-93ae-d00ba2e859e8 | -2.41078 | -48.5467 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 87fac55d-eeff-336d-ad48-143f9224330f | -2.41009 | -48.55119 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3d73f765-b3df-3c02-9102-8e0fa08feaa9 | -2.4062 | -48.54317 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7dcf814e-1646-3c46-9a03-67d34a775ded | -2.40553 | -48.54769 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 87b58b3a-3669-37f8-97d3-8ae69368057a | -2.40487 | -48.5522 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 17b2a831-0c93-33d4-a952-9f811d72a748 | -2.40471 | -48.54577 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 428173e1-580f-3582-91b0-ea86bf43ed7d | -2.40402 | -48.55027 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 68e49439-d0f1-3e4a-be12-f0e39501de66 | -2.40013 | -48.54221 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0993857b-cdae-3db2-9829-6596bdd76a24 | -2.39947 | -48.54676 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| df458bd3-ac6d-362f-ac3a-634808e295c7 | -2.39864 | -48.54486 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cfa4818-06f1-3f1a-9034-e2d34fa15f95 | -2.39795 | -48.54936 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d05e1477-39a5-3eb3-915b-694ba8ea5716 | -2.39407 | -48.54123 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5561711-69f1-37f2-9de8-d20521b2a3e7 | -2.3934 | -48.54582 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f6e1787-6b49-3be8-8251-91ffaf5ccfd7 | -2.39258 | -48.54391 | 2024-10-28 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4aa17055-b074-35c0-bf53-bf854009ec93 | -2.36861 | -47.66694 | 2024-10-28 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5add2022-edc6-389f-8b76-95f7e0dbd854 | -2.36784 | -47.67211 | 2024-10-28 05:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 64877c35-85a6-37e6-b753-5c29c2e903d7 | -0.26642 | -48.78394 | 2024-10-28 05:21:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 548bacf2-e2b2-3f55-8d1a-235d2c57eee1 | -0.26579 | -48.78798 | 2024-10-28 05:21:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13bb86c2-fa2a-3ae4-9b5a-816e508b242f | -0.26063 | -48.78302 | 2024-10-28 05:21:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19e71e3e-d195-3baa-bf07-35a51ed312dc | -0.26 | -48.78706 | 2024-10-28 05:21:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25b1b01c-53fa-3bbe-a54b-9bff8c54b1fd | -2.88661 | -49.25528 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bb2e111-b54a-3442-9ff2-7475fa6f1494 | -2.886 | -49.25937 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d681aa8-8816-3518-a785-ecb594095283 | -2.88491 | -49.50276 | 2024-10-28 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c208d3a8-d371-3a83-b076-703c310bf8be | -2.88199 | -49.24621 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d7459e8a-6272-3108-80fb-713441836826 | -2.88138 | -49.25029 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3bf02957-cbdf-30fa-843b-37e13a44dd6b | -2.88078 | -49.25438 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 0d4be752-b082-3899-aee4-7dacdf96f7bf | -2.88017 | -49.25849 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1a3468dc-0a9c-3488-a180-72547ca65b4a | -2.87615 | -49.24533 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b6b19ebc-1919-3892-aa77-c642a367cbd7 | -2.87554 | -49.24941 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 77474510-88ca-314b-88df-d7ebc94e3a1f | -2.87494 | -49.25348 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 34dbb545-75d6-3163-b441-f7807b1e82d9 | -2.87433 | -49.25759 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 40d97ef7-4681-3192-a765-b0703aeec33c | -2.48104 | -50.27859 | 2024-10-28 05:21:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f40d094-6b4e-32df-9330-a1d9119cea5e | -2.48053 | -50.28205 | 2024-10-28 05:21:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79066366-1bcc-394d-8f0c-ea483d68e798 | -2.47459 | -50.28467 | 2024-10-28 05:21:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32c8cd12-6f41-3b10-85c8-bebe81b9af61 | -2.47409 | -50.28812 | 2024-10-28 05:21:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 831fa941-4f85-33ef-80db-3ebff5163ba3 | -2.47325 | -50.28691 | 2024-10-28 05:21:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d8ddc40-45bf-3937-86bf-ace6f5dfed0a | -2.46816 | -50.2907 | 2024-10-28 05:21:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e90c7530-97ad-338b-8da4-07acf738bfae | -2.4673 | -50.28952 | 2024-10-28 05:21:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12ca3ede-9660-3155-b6ee-e4fe1bb71d29 | -2.46084 | -50.41486 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8351ebb3-7a54-362d-a9b4-9ffd1068d2d4 | -2.45547 | -50.41402 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79269ad9-a190-35e7-ac4c-521fcf108ee5 | -2.8691 | -49.25257 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0775b9bc-e997-3b2f-8528-58e58d1a72f3 | -2.86849 | -49.25668 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eb047af-0fdf-30dc-950a-20b2ac131398 | -2.86508 | -49.23939 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ef5d9ba-9f83-338c-b30c-3fd7f3e91e1f | -2.86448 | -49.24347 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7e0bae1-d3e4-34d9-a2dd-f5359673703a | -2.86387 | -49.24757 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4692954-4d4a-374b-bf4d-1a1c1455b482 | -2.86327 | -49.25166 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fadb352-653f-381a-bd26-628835274ef7 | -2.86266 | -49.25579 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2327837-efec-30bc-9bf1-33520094eddf | -2.85864 | -49.2425 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4e9b705-7157-38e3-97b6-f13adba4a83d | -2.85805 | -49.24657 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3945be8-07fe-3d71-94e1-70a8603b2a34 | -2.85744 | -49.2507 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dbbcbfd-fbb4-3718-b77a-6323ed72c467 | -2.85683 | -49.25483 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3049c9a-4730-3ea3-b44e-47a17581e0f1 | -2.85622 | -49.25901 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be7a2d99-9f2e-3151-a6e2-b69465e2f4b4 | -2.85222 | -49.24561 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9a2fe28-fcfd-38ad-ab76-21ee10090a0d | -2.85161 | -49.24977 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d73bad6-d208-3fb8-91d9-f3ff48f32396 | -2.851 | -49.25393 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d84eaaf0-1cd5-3a48-8a1b-2c1bb4bbfc78 | -2.85038 | -49.25813 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dbb02ba-9fe8-3d7a-b276-9171954d3fa7 | -2.84814 | -49.24327 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52fe65df-0266-3982-a682-80d5d25a5cf6 | -2.84751 | -49.24738 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57065ada-9bc0-393d-ab63-bb075f47a679 | -2.84696 | -49.24072 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d911638-e956-300c-a8d5-2e6a91c42e3c | -2.84687 | -49.25154 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62e82829-dce4-318d-9c1a-fc7220ed62e8 | -2.84636 | -49.2448 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6b3f9f6-de3d-3962-97b3-1d3d749569f8 | -2.84576 | -49.24895 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7dd0c89-2d1d-3486-97b8-c3ee1d452bd2 | -2.84515 | -49.25312 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77103e69-ec3a-3f9e-9e45-8a3f57d0dae5 | -2.8423 | -49.24245 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64707dae-17df-3634-848d-44d1bd387ccc | -2.84166 | -49.24657 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 226d7c6f-8c67-3342-9769-8ac6ae25e069 | -2.84112 | -49.23985 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d25524d2-0a0a-33fd-be5c-ad366443b7ec | -2.84103 | -49.25072 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61055d92-54fb-34b5-b5ce-61ffa23b52d7 | -2.84051 | -49.24398 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b96cc4d4-7978-3468-ac92-6a9c949c9d99 | -2.84039 | -49.25486 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4533296e-1564-317d-8156-b0822a303069 | -2.83991 | -49.24811 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 956e6150-9f39-386e-b7bb-d88e11f88bf1 | -2.8393 | -49.25228 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc4dec7e-6047-369b-aaf7-c91bbeda31cf | -2.8387 | -49.25643 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f775cc1a-23d0-3529-afed-067706c27669 | -2.83582 | -49.24573 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0605ba3a-e661-3828-919b-86992822f61b | -2.83519 | -49.24986 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcbcd5b7-d864-3f8a-8d6e-6add2c31edcb | -2.83467 | -49.24311 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d8313e86-cefd-374f-940e-b872d756dfb9 | -2.83455 | -49.25401 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3971cdc2-1884-3c5a-a33e-6c1fe62e067c | -2.83407 | -49.24725 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f166502-addd-3a33-90b0-ebb7517b89da | -2.83392 | -49.25813 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 273d002b-af53-35a0-afee-1a2183d80fcb | -2.83347 | -49.25137 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 586fb052-2251-3f6f-a177-e9ad00348343 | -2.83286 | -49.25552 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bb42fa6-5c32-3ca8-8c6e-a484ab564ab9 | -2.83124 | -49.23659 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b09af57-db35-34b6-9f39-1f121571fa00 | -2.83061 | -49.24073 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7dacbd3b-bf62-3f69-8884-3b8cbd7b3d88 | -2.82998 | -49.24486 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 99f09f2c-f13c-366d-b844-f5e4c9377456 | -2.82943 | -49.23808 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aa66cf07-33c4-30d1-b700-22beb3c18f42 | -2.82883 | -49.24222 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 234be4ba-e14d-3dfb-bdda-cdfb8cf6c0a3 | -2.82823 | -49.24636 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README74.md)
