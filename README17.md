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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd12f6cb-3204-34b2-a1f3-19df32dc0d19 | -12.19681 | -43.47725 | 2026-09-16 03:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35a8763e-4d54-3d98-9c8c-e8b6899c7db4 | -10.78154 | -46.20753 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0d43918-4075-3586-800f-e2ca629db714 | -8.78586 | -45.89972 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4919769-9d31-33ce-84d1-bd3d06a75bcf | -11.20118 | -42.82027 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fddfe5b2-e291-3083-a64d-8056145cf637 | -9.10564 | -45.72758 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bbde31ee-ae14-3934-85d5-068bbe546fbc | -13.29508 | -51.27163 | 2026-09-16 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f489d804-9589-3717-829a-c576fe2c1b53 | -10.46367 | -44.94787 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c819dee-67d7-3012-941f-fb705b33b4ec | -12.19607 | -43.4789 | 2026-09-16 03:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d3b9592c-fa70-3ff5-a69f-f55a76e711bd | -9.79545 | -46.49338 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b34aa1bc-d2f8-36f8-b4a0-7598a182b860 | -11.2165 | -43.43364 | 2026-09-16 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3ac5ede-bcef-3a57-9f16-247f8d74b3bb | -9.11054 | -45.73223 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d2b6768a-012e-39a4-9a0f-e09a5dc12761 | -11.1988 | -42.83358 | 2026-09-16 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9322225e-5a70-39f5-b46d-5ad7f4327f10 | -8.78014 | -45.89887 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0521097-45d8-3878-a214-abbb67a83d08 | -12.53096 | -47.11106 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ff58e6c1-9f72-36db-8b10-d90346a8d0b1 | -15.88755 | -40.22671 | 2026-09-16 03:55:00 | NPP-375D | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 852efbc3-380a-3ef2-956c-711a9acb22ec | -12.53177 | -47.10694 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 431a4d95-c5e8-3de4-9281-92e8965e5ec2 | -9.57463 | -46.58636 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc11efb0-c555-3a47-80ac-8099a53784df | -15.89181 | -40.22326 | 2026-09-16 03:55:00 | NPP-375D | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 04784d88-5099-399a-af29-734228de40bd | -11.19834 | -42.81054 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d74dec4-a275-3680-9c32-d0107d289920 | -9.22747 | -46.70078 | 2026-09-16 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38ae66ed-eccc-3b0c-9955-534d7fedc27c | -10.84791 | -46.17971 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e1a49b4-a4f2-30b6-a68d-0aa9e0622456 | -11.13753 | -40.48208 | 2026-09-16 03:55:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| c9cc3ed7-1ece-3fec-a19b-633990253bfc | -10.84714 | -46.18368 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1654bdb2-32f2-3e41-a298-dcb07daf0db3 | -11.34412 | -47.31581 | 2026-09-16 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1ecd38c-b236-3cb3-84a0-f523a04e2417 | -14.22774 | -48.51189 | 2026-09-16 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8308f760-745f-3c98-96d4-07349ab5c287 | -8.85524 | -44.9124 | 2026-09-16 03:55:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18fa4fb3-8dd7-3311-b4c0-1206288d06cb | -9.80053 | -46.50006 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b24055e1-ff0c-3c08-ac49-7fd91ab49665 | -11.97667 | -44.93326 | 2026-09-16 03:55:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abacb18d-caac-3104-87a0-5bc1ae569f97 | -12.53014 | -47.11518 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 16a19959-8ddb-37e8-9767-c5329869e9dd | -11.53987 | -46.86113 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07522ec1-39e0-3478-b2d8-38c75b977d4b | -11.19674 | -42.81945 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 287c27c4-fcbf-3354-b2ab-aa0b81109c66 | -8.54836 | -44.49998 | 2026-09-16 03:55:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17b50b05-9782-3cdf-a4e9-d9390b6e7289 | -15.2751 | -42.80337 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7a8061a-40b8-3ff4-b24a-24988ddb1cf9 | -11.62208 | -46.95867 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9457fb9-7943-3c34-9a9c-d123e474ddd8 | -13.55525 | -43.53151 | 2026-09-16 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6c0c875-f95a-3d16-92f9-285c956106d0 | -11.17095 | -42.81005 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6dd15e03-cede-31e0-b29c-8cfc7cffe790 | -11.31555 | -47.24186 | 2026-09-16 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c479d718-b223-3b05-a90f-45f6204965b3 | -9.10496 | -45.73121 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 22ce78da-2d4c-3756-aa4a-5f4950c565b9 | -13.75761 | -42.51407 | 2026-09-16 03:55:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51c122ad-7e7a-329c-b3fb-2b1d6bf93c4c | -11.89457 | -43.8283 | 2026-09-16 03:55:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0a4d617f-2675-3bfa-909c-02eb1bf94d94 | -9.07461 | -42.99485 | 2026-09-16 03:55:00 | NPP-375D | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 819f6236-2a68-3450-8451-00c763887251 | -15.6075 | -42.40051 | 2026-09-16 03:55:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1a3784e-55f8-36b4-a646-5a56c23cb0a9 | -12.55727 | -47.09854 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59f26bcc-d73d-3869-adb6-fbe573a9c6bc | -11.34722 | -47.31503 | 2026-09-16 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e97254dd-90c7-30f9-af65-90bc19aae323 | -10.59631 | -47.75336 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0e5d012-f1fd-3218-bb2c-9313489432fa | -10.36566 | -45.13007 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fe2b05c-c978-33ff-b7b0-67313133a372 | -8.85191 | -44.90064 | 2026-09-16 03:55:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55f74147-42d6-380a-978e-25b26d3063ca | -16.31072 | -42.0405 | 2026-09-16 03:55:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a9af9d5f-68e5-3b3d-8e92-b05d5aa31ee9 | -8.84723 | -44.89622 | 2026-09-16 03:55:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15d1b038-b8f1-3fa2-8066-7b807a5a2977 | -11.25498 | -46.57214 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e327272e-f4a5-3e13-b7fd-641aa3d2cf0b | -15.24836 | -49.10695 | 2026-09-16 03:55:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2e50a8c-ec7b-3bdb-941c-70b117bfa95f | -11.34633 | -47.31947 | 2026-09-16 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2810113c-e1da-3be8-813f-3a95d621334f | -10.10388 | -45.56847 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9c9df1f-c35e-3eed-901d-7c3019af5a35 | -10.10329 | -45.57156 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f95c4ffa-0df8-384a-a222-5f192993a304 | -10.59445 | -47.76287 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 412680e2-ea41-31be-98b7-286aa72a5b74 | -10.84868 | -46.17576 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c2eb541-0371-30a4-8bfd-08a1fdec0dab | -10.83859 | -46.19796 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b839a93-2b9b-3a3f-9e78-c6b1af21571e | -9.77811 | -46.48994 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71d85c57-d00f-3468-a7bc-5d54be85736e | -9.75973 | -46.58385 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 21c2f166-27ab-3596-b183-cab1dc45a625 | -16.78265 | -39.46128 | 2026-09-16 03:55:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 43b99fe1-4aa2-3b87-ab29-3242f7d4e611 | -11.54087 | -46.8553 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 349dc3c2-7b85-3495-beeb-edc3f03128bb | -16.78027 | -39.43323 | 2026-09-16 03:55:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 055e3193-641b-3640-99b1-102d7750366b | -10.59307 | -47.76226 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 252b2a07-1f7a-3fda-b4ff-f251954b36e8 | -15.60816 | -42.39686 | 2026-09-16 03:55:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f9d5412-8795-35f4-914e-84ce10f7ec36 | -12.31573 | -47.96505 | 2026-09-16 03:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04644e00-c629-3ddc-a55d-9c47d2af4608 | -15.88225 | -39.93824 | 2026-09-16 03:55:00 | NPP-375D | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d133f103-51f2-3281-baa7-795695cd7da9 | -9.76116 | -46.58169 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a05f957f-c49d-3f28-b613-4c728d195914 | -9.49214 | -45.44757 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3026dc36-6b22-391b-b405-7539e885df3c | -10.5841 | -47.75024 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f626efe-6df5-3be6-9ffb-d161c744551b | -9.75569 | -46.48336 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e09d7f8a-fbd7-3ba4-8d49-cbe73b8e904b | -11.89005 | -43.81967 | 2026-09-16 03:55:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| af572a00-8dcd-3207-837c-3f00b21c7181 | -10.41007 | -48.66442 | 2026-09-16 03:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09fd7010-4f94-3710-b3d2-204267a0c709 | -15.28242 | -42.81003 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d306eafd-18e1-35fa-96a1-10299bc46824 | -13.4521 | -41.60948 | 2026-09-16 03:55:00 | NPP-375D | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6a7e9f0-204b-35a0-80df-054048466bdf | -10.30638 | -45.27304 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68dfc71a-89f7-36e8-abbb-3aff65e90c60 | -11.16971 | -42.79164 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 599464b1-5e74-375f-b2dc-97d8912ac185 | -10.09419 | -45.61942 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19649c7f-c93e-380d-a8f3-d8f518e95a38 | -10.90091 | -46.29641 | 2026-09-16 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab4e8cbf-dc2a-3cfc-9faf-33a20903715e | -9.10005 | -45.7266 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 863641d6-0495-36c2-9566-5f8b3ab26e01 | -9.53617 | -45.4226 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d877e51c-4a6a-30cd-af7e-c1f80db1499e | -9.79553 | -46.49474 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bb557a8-97d7-3a22-9840-403207159ab6 | -11.2479 | -43.44459 | 2026-09-16 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02e83b54-3c16-30ec-a2ea-271f54eee96d | -10.89822 | -46.29674 | 2026-09-16 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cc3a609-ddcb-3fd8-8e6e-6c727a7998f2 | -12.15173 | -47.99483 | 2026-09-16 03:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7df4d78-5e7a-3589-9cb8-116a2198b6c2 | -10.10444 | -45.56551 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fbd7bf5-bc5e-34a7-9f51-530eb7bfe9d3 | -15.36595 | -42.19564 | 2026-09-16 03:55:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| dddc84ea-961e-3f69-8f4b-d6dda6ca8d36 | -15.29494 | -42.78836 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d070bed-27d7-354c-9c23-643e62443999 | -11.24254 | -43.4736 | 2026-09-16 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f71accd-3c6b-3a06-8445-7bbe7b98e358 | -10.10923 | -45.56988 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e4aabd4-0279-3109-b464-367d3533bef7 | -8.85594 | -44.90859 | 2026-09-16 03:55:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2495110c-0482-3209-8402-fc923c2e51cd | -9.84169 | -48.36203 | 2026-09-16 03:55:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72f661c1-fa1c-3cc7-801a-363d5a3e44d7 | -15.8847 | -40.22193 | 2026-09-16 03:55:00 | NPP-375D | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 543a040b-9c4d-324c-a55a-de3fe41fcb2e | -15.2791 | -42.80484 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5019a85c-83e6-3a87-afbd-f479f3f56a72 | -9.54766 | -45.42119 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1069a90-781a-33e4-8f9e-c9b3d5ad8de0 | -10.83794 | -46.20131 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c947e702-6177-3420-a880-66473a402200 | -10.11346 | -45.57721 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 928dd2be-01c7-3797-802f-ef3de6c2fee8 | -9.76844 | -46.57509 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acd00502-da0b-3d81-914a-1b1368319cb4 | -8.84245 | -44.89238 | 2026-09-16 03:55:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7782af70-7e48-36e9-92a5-fcc3ade5cd79 | -15.63447 | -39.8028 | 2026-09-16 03:55:00 | NPP-375D | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 03a7bd26-5eb3-3edb-9a96-e62b288dc080 | -13.63414 | -45.97211 | 2026-09-16 03:55:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README18.md)
