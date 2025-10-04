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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aacfed8-8161-36f8-85d7-a57cf99fcfb6 | -11.8814 | -45.0047 | 2025-10-04 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 9490c2c8-1a0c-3d3d-9910-3a4f162ff63e | -13.5119 | -47.2655 | 2025-10-04 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 77a13566-773d-3cfe-9afc-b5b51e44339e | -12.8761 | -47.2937 | 2025-10-04 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 63ed824a-20b3-3d52-b4a1-14d344743589 | -9.1114 | -44.4029 | 2025-10-04 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| c0d982da-252a-380e-a786-3af8065cbaf9 | -13.116 | -47.8401 | 2025-10-04 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 762007ac-27ba-3259-97fa-889bd61e9dd1 | -14.9881 | -49.9892 | 2025-10-04 13:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 03ab94c6-5dab-3503-a377-8920b7f2c845 | -14.3899 | -45.9601 | 2025-10-04 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 93858122-0e12-3af4-9dd4-c265c41dc3c4 | -9.1901 | -49.9604 | 2025-10-04 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 217.2 |
| 5fb2782c-ca2e-3588-ac99-10b3bd73d64a | -10.5835 | -48.7178 | 2025-10-04 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c89df8f2-04de-304f-b82a-2e71db15b876 | -16.097 | -51.0611 | 2025-10-04 13:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 37881b0b-f57f-39f8-80a2-7e29eaaaf886 | -14.5941 | -52.4976 | 2025-10-04 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ab1482d8-4c04-3953-aa1e-e2e4f3896c0d | -10.1462 | -50.2952 | 2025-10-04 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 98f6bcaf-3e9e-3cbd-9e26-d060ac1c9530 | -13.996 | -48.1987 | 2025-10-04 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 58d98dc8-ea64-3790-876f-ca4abd78dce2 | -7.8593 | -48.2037 | 2025-10-04 13:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 7543f930-defb-376a-94b6-adfde48e68bf | -12.9471 | -50.9838 | 2025-10-04 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 31ad2bf9-e865-38ea-8e06-2886c658ca0c | -8.8526 | -46.812 | 2025-10-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 0712d749-d7a0-3250-957a-1a5002e2ca19 | -7.7491 | -46.2944 | 2025-10-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| b02aa905-4504-3b48-8bcc-e285d0922cd7 | -15.5206 | -46.8609 | 2025-10-04 13:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 075cd3ae-cf96-3cdc-8ca6-49fb3d36a74b | -11.3079 | -53.9477 | 2025-10-04 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e894bd2a-38d2-3a16-b208-ef65a15424a5 | -11.1268 | -47.9077 | 2025-10-04 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 767910bc-f312-31ee-82ff-ac99e6b19959 | -7.6458 | -45.4716 | 2025-10-04 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 57d8550c-ea42-3d0b-b9a3-f8d5cf5a43c9 | -13.2426 | -47.2391 | 2025-10-04 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f0cd666e-a8a2-3fce-8835-c7d6ae994e80 | -13.3127 | -47.61 | 2025-10-04 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 29321c8c-dba6-3a08-aba3-84bac5dfd062 | -11.4877 | -46.7696 | 2025-10-04 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 2e206199-141a-327c-a337-4e318374c3d5 | -9.9628 | -45.7897 | 2025-10-04 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| e5806c0f-d356-3761-9f1c-226a414962b4 | -15.3601 | -47.9554 | 2025-10-04 13:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 9ba20261-6375-3650-b591-4b0860c41598 | -15.5408 | -46.8344 | 2025-10-04 13:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 649bb3c3-85b7-3989-8df3-98349404c86c | -10.127 | -50.3184 | 2025-10-04 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 58442961-0f19-3392-840f-c0bc2e2b3119 | -7.7687 | -46.2255 | 2025-10-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 58131661-3db4-35f8-9e7a-d2cd8613cbe5 | -13.3233 | -48.077 | 2025-10-04 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 2a56cee1-64b7-334d-8d43-212f08ba10a7 | -7.0558 | -42.7782 | 2025-10-04 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 138.3 |
| 0d3a8a86-e39e-3f83-8c92-d32c0f83be36 | -11.5492 | -47.6773 | 2025-10-04 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e50227c9-7ca4-30f5-826b-33dbf0a7d723 | -6.287 | -44.428 | 2025-10-04 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 0b4290d0-263e-31f5-a8f4-836d36571694 | -7.7743 | -42.6103 | 2025-10-04 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 110.6 |
| 18b159e9-938b-3d47-91e1-62666d1b0af6 | -7.7941 | -42.5369 | 2025-10-04 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 1e1c7608-4aac-307c-835f-3b07d55a19a6 | -11.5069 | -46.7671 | 2025-10-04 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 231.3 |
| 1cb88853-4b0e-3219-9a34-6f53955ff324 | -7.8127 | -42.5587 | 2025-10-04 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 22b7744c-6be5-38b4-98f2-00e65e1ffc40 | -9.1716 | -49.9408 | 2025-10-04 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| cff03b86-9d8c-304f-89ea-6cfe2df3889f | -10.1459 | -50.3165 | 2025-10-04 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 7a7b2283-f1b1-3a9a-86f9-8cf2d310730e | -12.3853 | -50.2595 | 2025-10-04 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 263.6 |
| 3a974651-c87e-31bd-8f86-b0cf7cc559b2 | -7.0604 | -45.7946 | 2025-10-04 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 592beedc-8099-3392-8c9e-9837ad2ed68b | -7.0046 | -42.3091 | 2025-10-04 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 95ecab6b-79ae-3a09-8071-883e0eca611f | -8.5458 | -47.264 | 2025-10-04 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 305beda4-1e66-3523-9756-36ae480e2ad6 | -7.7872 | -46.2462 | 2025-10-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 991374c7-a5e2-3dd2-bc99-118465d9a2cd | -10.1081 | -50.3203 | 2025-10-04 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b3d10828-100b-3e3a-b14e-faaab089e87e | -13.7473 | -51.3097 | 2025-10-04 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 136.6 |
| e922ba20-54aa-3b44-9bee-7d2c3dffa7ac | -10.2973 | -50.2799 | 2025-10-04 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 9af8c1e1-65fa-3339-93f2-8d22740bf019 | -8.5601 | -47.6373 | 2025-10-04 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 047b7b7c-4d1a-33cf-8a8d-45f026add01f | -9.3274 | -54.5418 | 2025-10-04 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 8a927453-09f5-3ee2-94ac-81c1bde1f160 | -9.648 | -54.3143 | 2025-10-04 13:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 64585790-9148-3400-83bb-4e5ffc43925f | -11.6841 | -45.3333 | 2025-10-04 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 1e211452-7ac9-3b5c-aa8a-13daf60046b3 | -7.7935 | -42.5845 | 2025-10-04 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 123.7 |
| 1fe07b45-5a5f-354b-bbae-abf288b9ccf6 | -8.8529 | -46.7897 | 2025-10-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 9cda710b-d8ba-30ab-80e9-9189e4ef1bcf | -8.1372 | -50.2428 | 2025-10-04 13:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c312cc22-66f8-3777-bd40-1e6d835479f7 | -12.3222 | -50.6322 | 2025-10-04 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d862a085-8773-39bd-a455-a3a1a72baee5 | -8.8534 | -46.7451 | 2025-10-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 5660f7cf-2d54-3ce4-8874-9cbe414b9578 | -7.813 | -42.5349 | 2025-10-04 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 134.3 |
| ef52eef3-7b8a-3a10-89e6-06832a7c1568 | -13.0968 | -47.8429 | 2025-10-04 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 24e193c7-b9d9-38b3-b665-aec9a37ba5d3 | -13.2938 | -47.5905 | 2025-10-04 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 4f64803f-6b8d-3fce-b431-b55c0dc77965 | -15.5402 | -46.8574 | 2025-10-04 13:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 138.2 |
| d487858b-8205-3e03-a3c4-b3f0b363f276 | -11.5256 | -46.7871 | 2025-10-04 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 288.3 |
| 93d6895f-7269-388b-a918-6fb26fc384bf | -13.3032 | -48.1244 | 2025-10-04 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 5879609c-e070-3430-a707-54084777c88a | -10.1273 | -50.2971 | 2025-10-04 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3e43de4c-e271-39d1-addb-7562b6ee984b | -13.2934 | -47.6129 | 2025-10-04 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d1bd96ed-f04d-3bc3-bbd2-1906d80b8c01 | -18.3133 | -47.4403 | 2025-10-04 13:50:00 | GOES-19 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 408c9fff-dc20-3556-8e13-e2097321b84b | -7.7489 | -46.3168 | 2025-10-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 5d836dcc-2f4e-353e-a891-9f75826b8e7f | -14.3904 | -45.9369 | 2025-10-04 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9893151a-9087-33c1-96cd-f0516bf3cc5c | -7.7684 | -46.2479 | 2025-10-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 9f4c106b-5396-3a09-a0f6-6033584c0cf8 | -6.0616 | -42.537 | 2025-10-04 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 135.2 |
| 5109c376-1911-3ef9-b532-60d6f812e339 | -11.8818 | -44.9815 | 2025-10-04 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| ac09e6e5-1e2d-3eae-8af8-e353cf8591b5 | -13.9383 | -48.1852 | 2025-10-04 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 920846d6-627a-372f-b0df-436f138f51b9 | -7.4416 | -46.9666 | 2025-10-04 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| daf34fb3-74aa-3d34-9985-b7dff11286b1 | -14.5748 | -52.5001 | 2025-10-04 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| d2ee0667-365d-3367-958c-a6370570f937 | -13.3225 | -48.1216 | 2025-10-04 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| cc64a19e-1182-3ba1-9f75-1fcdbb750611 | -14.2754 | -45.8647 | 2025-10-04 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3a2b1313-7844-35ce-9239-2bed4b201a2e | -11.825 | -44.9437 | 2025-10-04 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| eb9032f2-a885-38ff-a23c-c4559601d2f6 | -7.5504 | -42.3965 | 2025-10-04 13:50:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 127.4 |
| b5d7c303-10a3-3210-b5ed-7a427e27fc0f | -10.1839 | -50.2914 | 2025-10-04 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 0dcff945-2992-342e-9c5e-b8c007c260d6 | -9.6293 | -54.3158 | 2025-10-04 13:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ccc48718-5f4c-3e72-9f1d-65c5eb03087e | -9.1713 | -49.9622 | 2025-10-04 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| e73dd8d0-7c58-3c41-9980-e28c1248652d | -12.7194 | -48.5611 | 2025-10-04 13:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 5a32b56f-6559-3672-943e-2c450dafb6ff | -11.4988 | -44.9915 | 2025-10-04 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 90223e25-dd35-315d-9880-f1eec90a0f3d | -11.8635 | -44.938 | 2025-10-04 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 8270e759-a2d3-3eb6-8eac-55fe7f640a19 | -6.3673 | -43.8916 | 2025-10-04 13:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| afce8245-d98e-3fa6-b3da-3c3efae55b7a | -7.878 | -48.2021 | 2025-10-04 13:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 138.6 |
| c408072c-c4a8-36e5-8699-f0f4cb1de103 | -11.4414 | -43.9057 | 2025-10-04 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 27228619-043b-3fb4-a724-b52844b6f1e8 | -9.3209 | -45.6607 | 2025-10-04 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 9d6a20d2-8916-3925-a3d8-e2dfdb5ee33f | -11.8442 | -44.9408 | 2025-10-04 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 246.3 |
| f72b1caa-d6ed-3a73-8e34-56599b6bb159 | -15.5206 | -46.8609 | 2025-10-04 14:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 101.7 |
| de3c1b60-3715-3b5a-bbac-eba38607f9be | -6.0618 | -42.5133 | 2025-10-04 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 116.9 |
| 9224cb6a-4a56-3a80-866d-3df23dd63e4f | -5.8951 | -44.275 | 2025-10-04 14:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 2262af5a-5891-34db-8dec-d9f150b71017 | -12.8401 | -50.504 | 2025-10-04 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 8975d189-5a15-3a6b-9ea8-55e6f7b737f0 | -11.4877 | -46.7696 | 2025-10-04 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 197af8e0-79ed-3d26-a885-da293f0270d0 | -7.7687 | -46.2255 | 2025-10-04 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a83d719d-70e5-3daa-a632-89ea8791d24a | -12.6512 | -46.9894 | 2025-10-04 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 2f38bfff-530d-3173-b8fc-f1327a1f4a50 | -8.2314 | -46.8289 | 2025-10-04 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 347d2307-ac34-36f2-b174-4f1676b0e66e | -14.8268 | -54.7926 | 2025-10-04 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 2b13077b-af33-3fb2-b312-61675e2003b5 | -6.5044 | -45.1859 | 2025-10-04 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| df0f76c2-440d-3706-8c17-7b4ec81bd689 | -5.8927 | -42.5273 | 2025-10-04 14:00:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 4bf24bd7-cec9-3377-9fa5-f437a916f077 | -13.2938 | -47.5905 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |


[Clique aqui para ver as próximas entradas](README152.md)
