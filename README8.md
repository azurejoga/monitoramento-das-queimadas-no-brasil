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
| 476a37c0-73b6-3a67-9f24-e3747ff9372d | -11.5436 | -52.120701 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8c8e542-b255-32b4-b51c-b220d1e0cec0 | -15.6445 | -52.7187 | 2025-08-26 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50f90b29-8deb-3a93-b0a6-20e7357a1b9a | -11.4432 | -47.2854 | 2025-08-26 00:39:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a693d91-0e81-353a-9d10-a8885370da56 | -13.6037 | -48.1544 | 2025-08-26 00:39:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fb420bf2-bd57-345e-bcc1-bfece0f95872 | -11.5592 | -52.0994 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10db8861-f408-3039-8866-603c61a41901 | -13.4434 | -51.152901 | 2025-08-26 00:39:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0cde072-b33e-3401-ad0b-2ecf64084984 | -13.4021 | -51.767799 | 2025-08-26 00:39:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31a35cc2-4353-39c3-8841-d06d76ee8f61 | -11.1471 | -44.735802 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5182fae5-c64f-371c-959e-6dabf7711626 | -12.4411 | -48.717201 | 2025-08-26 00:39:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28b3a4ad-5221-3f04-b2d8-97184181ceee | -13.0096 | -56.878502 | 2025-08-26 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25cf0c40-ccd3-3655-9ac1-3e82ce95c90c | -13.1542 | -45.2738 | 2025-08-26 00:39:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9345eac5-f8f6-3edf-9d9d-8db7165327eb | -14.3649 | -51.911098 | 2025-08-26 00:39:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b47b8c03-d0a3-38a9-8f69-b8ed6285415f | -13.6101 | -48.138599 | 2025-08-26 00:39:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20d2a424-733e-37ca-8b4c-81fe2f89c134 | -11.1342 | -44.7654 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 770c6d0d-0f0f-3703-8629-e67749585d11 | -11.565 | -52.124298 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3067b127-8d6e-34a8-81fe-4668f1dd6d2f | -11.3053 | -55.100101 | 2025-08-26 00:39:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0130ab33-f8fe-3e29-a112-747e2e0491f1 | -11.567 | -52.1325 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76ff33d1-7b5d-3841-b02f-4b6c74572172 | -12.7573 | -48.117901 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f421aae9-bf49-3f46-92b6-b617e0a3dfac | -13.4609 | -51.139198 | 2025-08-26 00:39:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e26c385-42c8-32f2-b320-5339b2c243f2 | -14.4341 | -56.437099 | 2025-08-26 00:39:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3968778-aca9-3b22-98d1-f164d822e1f3 | -11.6118 | -46.367001 | 2025-08-26 00:39:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a282e29-815f-38c7-8914-6d5af03c2f8a | -11.5552 | -52.126598 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 634621f5-3fe1-307c-aedf-9bc55e4e345f | -11.5455 | -52.129002 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19ffd4e1-c2de-3740-8514-c0fccbfbaacb | -13.5908 | -48.185902 | 2025-08-26 00:39:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 03e4f0e2-9b5d-34be-87c8-eba409bc7240 | -10.88 | -55.780899 | 2025-08-26 00:39:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92088cf3-33a2-324e-aae5-2b45c170f228 | -14.7841 | -49.162701 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09b71bd6-ddef-333c-b2e8-7a1f1484545b | -15.1087 | -48.631901 | 2025-08-26 00:39:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e83cc40d-66b1-3f5d-ad62-000d3735b92f | -11.5514 | -52.1101 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5804287e-3612-3d9d-80a4-60b31fdf0ca4 | -13.6004 | -48.141201 | 2025-08-26 00:39:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e1abac0b-74cd-3974-8ed5-5e7925079123 | -10.8815 | -55.787899 | 2025-08-26 00:39:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13ccddaa-465e-35b6-ad55-20c5530d8068 | -13.7166 | -52.009701 | 2025-08-26 00:39:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c080d117-5460-3d78-8035-3f5240a7fee9 | -13.463 | -51.148102 | 2025-08-26 00:39:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe1c48b7-73d4-34da-b49b-d7e857db7661 | -14.2522 | -53.0368 | 2025-08-26 00:39:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b85224a-1938-3d60-b3f4-9e0c2f0a365c | -15.0233 | -48.163898 | 2025-08-26 00:39:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8743a846-70c0-319e-9278-dcb7d912a6b6 | -14.6472 | -49.068699 | 2025-08-26 00:39:00 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b737cb29-5f38-3417-bca6-e18c40506cc3 | -12.78 | -48.126598 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92f6c6d7-0bad-3236-939b-b2e30d15db13 | -10.7413 | -47.037899 | 2025-08-26 00:39:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4f63b81-d0be-331d-a7e7-bb6adaeb229d | -12.7413 | -48.1366 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bff5bf2-fa36-32cf-98ec-0546531fb74d | -10.7553 | -47.0527 | 2025-08-26 00:39:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5b691d6-a50f-3a42-a979-f562a0820f1a | -11.5671 | -52.088799 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d01b581-2bc8-3c1b-9a2e-d19b24848351 | -13.0484 | -46.2943 | 2025-08-26 00:39:00 | METOP-B | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0f219f33-e0f6-369d-9404-6e307e67c311 | -12.6714 | -47.857601 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65689be1-8adc-3718-8490-da8bb363fb00 | -10.7053 | -55.134201 | 2025-08-26 00:39:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97154972-7101-3e37-88fc-b096b7de29ec | -13.4295 | -51.1376 | 2025-08-26 00:39:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92964e85-08fe-3c84-934d-2667fea54f64 | -13.3962 | -51.786701 | 2025-08-26 00:39:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4333b13-3d2b-31f3-94e2-384fba47a5a0 | -13.4337 | -51.1553 | 2025-08-26 00:39:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5f5b996-fd0c-3a86-aa5f-748fc2ce0330 | -12.7704 | -48.129101 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0feed4cf-ebc9-3b57-ba0d-c2d57df5bc32 | -15.017 | -48.138699 | 2025-08-26 00:39:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b44043d3-d349-315c-ad55-8ccbfd2ccb0f | -15.656 | -52.723701 | 2025-08-26 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 615d1c18-0814-3ab6-b7f2-fb91101c8528 | -13.4511 | -51.141602 | 2025-08-26 00:39:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 232e374d-829b-3e1e-9c41-482fc7db64ba | -13.4532 | -51.150501 | 2025-08-26 00:39:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e1a44e6-43be-36d1-8f20-3c721e1245d7 | -12.767 | -48.115398 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6e7a869-692b-3c83-a187-e932656ad504 | -14.6403 | -49.082401 | 2025-08-26 00:39:00 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f28a4819-c1c5-35e4-9aaa-ce6f31f7061e | -12.7607 | -48.131599 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02059af8-788a-3373-b19d-be5a70aef61a | -13.5876 | -48.172699 | 2025-08-26 00:39:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 577be7d4-e739-3569-bfac-b5c9498f76e0 | -9.5688 | -48.620701 | 2025-08-26 00:39:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1f78ca0-edd6-3f71-b4ca-3d99dc45a619 | -11.6169 | -44.839699 | 2025-08-26 00:39:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa2ad7b0-ad79-388b-a10e-865ac3557263 | -14.363 | -51.903099 | 2025-08-26 00:39:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 235a8c55-b812-3351-a672-efe10b47d87e | -10.8018 | -48.309502 | 2025-08-26 00:39:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad7f6b3c-74a1-3350-8da5-9b72c4b4fa29 | -11.1374 | -44.7384 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b91e2a1-8483-3f7d-9f5d-10abd75b5deb | -13.7148 | -52.001701 | 2025-08-26 00:39:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6534f82b-51ee-3a3c-8e3a-3ff7c6f51d7e | -16.247801 | -58.695999 | 2025-08-26 00:39:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52856995-e50e-379d-8bb1-25514b517b56 | -10.7406 | -47.0671 | 2025-08-26 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 012be2c2-1ba2-3c22-8975-6d5ac7350ff0 | -6.9128 | -59.3578 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 4d200c69-43c7-34bc-858e-7f179f0a50a0 | -6.8044 | -58.9568 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 5a96fa15-8eea-3cca-aa9b-feefe4597bbc | -11.1587 | -44.7627 | 2025-08-26 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 419.2 |
| 983ee4a9-cd16-347b-8ba0-b5d10d8ad9a3 | -6.8412 | -58.9746 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| ee239ddd-4c90-3fe6-a8cf-11dc52988579 | -8.9873 | -65.4379 | 2025-08-26 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c71a64fb-c28e-3fce-bebd-be96bcc2c574 | -11.1583 | -44.7859 | 2025-08-26 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 6fa36df2-30a1-3932-9c9e-8a64ad29a106 | -11.1779 | -44.76 | 2025-08-26 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 502309c5-e498-399b-a73e-dc4bc48b3f00 | -7.4224 | -60.6236 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| be7f1c6a-126d-3739-ba04-620dcfeff6d2 | -9.181 | -60.8131 | 2025-08-26 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9830d92f-8f2f-318f-aeb3-042899a3d446 | -6.7476 | -62.8664 | 2025-08-26 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 985b53ed-9a84-324b-ba0e-ca287626c28d | -9.1722 | -59.4629 | 2025-08-26 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| e1160fe6-8cbf-3d78-887f-156fc0eaf1fd | -9.1677 | -40.6026 | 2025-08-26 00:40:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 6f1df14b-bbe1-306b-bee1-3e1453ce5168 | -6.766 | -62.8659 | 2025-08-26 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 2afa5c06-bdf9-33b1-9275-17b31d7a47da | -4.9606 | -55.8028 | 2025-08-26 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 1a87f4e3-94d2-3c30-ac62-ff0fc71d2f03 | -8.3209 | -50.5667 | 2025-08-26 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 30651a5d-f410-3b00-8c2a-1d4e21ac0c8c | -10.76 | -47.0424 | 2025-08-26 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| d21c5b27-8035-32ce-9648-9b402ac0c7a6 | -9.023 | -65.7355 | 2025-08-26 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| e15356b8-a089-3212-b0da-d6f132af34e4 | -8.8364 | -62.4321 | 2025-08-26 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 47a99264-1310-3ce8-814a-d149564b5bb2 | -11.1396 | -44.7654 | 2025-08-26 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| c2b44730-7c85-39bd-a0d4-63ed15056706 | -6.2459 | -60.0174 | 2025-08-26 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.5 |
| e5a37055-3f1f-3223-bf37-a4bffaa54de4 | -13.1648 | -45.2665 | 2025-08-26 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 68235e7b-2ba1-39e2-8a48-58530c7839e5 | -6.8229 | -58.956 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 284.6 |
| e7edc6d3-4fc0-32fd-8e12-dccb56f3869f | -7.5388 | -63.0481 | 2025-08-26 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| cf0e6925-6009-327d-b23d-dc6d0e76f30f | -10.7597 | -47.0648 | 2025-08-26 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 878b4e26-dbc6-3aad-8475-99054889b896 | -7.3854 | -64.3662 | 2025-08-26 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 16cbce42-fa66-3608-9a6d-5b5c4511c29c | -9.191 | -59.4425 | 2025-08-26 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| f02dd429-a5c1-318a-9c94-dcd9f75f1d76 | -7.3854 | -64.3475 | 2025-08-26 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 235.5 |
| 6d00e596-bfec-3568-8e7f-a8c6fd0679dd | -11.2937 | -55.1129 | 2025-08-26 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| c00dab5b-d9f0-32ea-8530-99221c7fac66 | -8.9874 | -65.4192 | 2025-08-26 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 47df23d9-c66e-313c-abf4-2c82f0a6b737 | -7.3541 | -59.6669 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 4f84946d-2faa-38a0-92ab-11608051977d | -8.8363 | -62.451 | 2025-08-26 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 2bf372ae-0a93-31ba-8260-8403819dbb84 | -6.8043 | -58.9761 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 266.0 |
| 856bd4ff-e2f5-31ff-9aa5-9c6d7fe349e4 | -6.7145 | -58.5539 | 2025-08-26 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 9e6e3d36-ce3d-39ba-89b1-31c917651d59 | -8.8734 | -62.4495 | 2025-08-26 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 23e0ad5f-11af-390a-8733-66fbd949ee84 | -6.9313 | -59.357 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ed4712ae-e996-3eda-9ab1-63407038af12 | -9.1812 | -60.7939 | 2025-08-26 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2232be2e-ede2-3e07-9bf2-9c6425c7eed4 | -14.6567 | -49.0729 | 2025-08-26 00:40:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |


[Clique aqui para ver as próximas entradas](README9.md)
