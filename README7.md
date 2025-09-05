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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7be0bcd-aece-3345-a443-b97c34ee29ea | -15.3151 | -53.050201 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2aded27e-4ac4-3a90-af3c-8ad878b8fdd9 | -11.6917 | -51.463699 | 2025-09-05 00:36:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3d38b92-769e-3193-8e8b-01ece67e0810 | -16.1852 | -52.983501 | 2025-09-05 00:36:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8cdf3076-7542-3641-996d-54ef1d4e6054 | -9.8183 | -51.661499 | 2025-09-05 00:36:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac76538c-0b08-3612-943d-e890f3b2c789 | -3.5317 | -49.044701 | 2025-09-05 00:36:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1a40a28-b780-35ea-8cdd-3e6f9e7cf41d | -9.8236 | -51.684601 | 2025-09-05 00:36:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43b932e3-1546-30be-b9bb-7e7345039ed2 | -5.407 | -46.226002 | 2025-09-05 00:36:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6025c573-fd06-37bd-8b7a-3e5bbe18a9c0 | -9.0921 | -57.094898 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7fec20c2-8555-37ee-9dee-19d443da8d5e | -8.9287 | -47.010601 | 2025-09-05 00:36:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91da4588-8b22-37f9-9b06-2d2194805f2c | -22.938299 | -48.951698 | 2025-09-05 00:36:00 | METOP-B | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b074d16b-d115-3371-8853-a8eff7a402db | -11.7129 | -51.466702 | 2025-09-05 00:36:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb20407a-74ab-392e-a729-4b4815ef656f | -9.8219 | -51.676899 | 2025-09-05 00:36:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94e10224-14fd-32d0-bf58-bafc65525598 | -6.128 | -53.561001 | 2025-09-05 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5afe835-3b08-3dd4-bfc1-ce43d4ea4957 | -8.919 | -47.013 | 2025-09-05 00:36:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4341fdb2-603f-35f8-84b4-1c354268b4b8 | -16.183701 | -52.976398 | 2025-09-05 00:36:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15f7573a-1cb0-3ca0-8632-a7ac00825199 | -12.0478 | -53.9146 | 2025-09-05 00:36:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db752a6b-9b45-36b3-ba94-5d38187f0449 | -11.4902 | -52.2519 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2457a78-b05a-3a3a-be7a-773ddfa323e6 | -11.5105 | -54.559101 | 2025-09-05 00:36:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3fcaf9be-2d65-3811-af1e-4714b6b176e1 | -22.518299 | -46.8531 | 2025-09-05 00:36:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 07c9e363-dbbb-3496-b148-8a7cfd15f513 | -10.8916 | -52.068699 | 2025-09-05 00:36:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd4b239-c551-33c6-beb6-541e053f26a5 | -6.0905 | -43.314602 | 2025-09-05 00:36:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25f08aaa-1bfb-3716-9976-44bf5e2332f9 | -5.4495 | -45.055302 | 2025-09-05 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1feb251b-11b6-3bff-81fe-067ead6e65a9 | -11.0605 | -55.040401 | 2025-09-05 00:36:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b41e38c-fe67-3fd6-b96d-5ab2390bac21 | -12.038 | -53.916901 | 2025-09-05 00:36:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da196111-ddf6-3a12-9f48-dcb5afcfd8c5 | -24.1789 | -50.7486 | 2025-09-05 00:36:00 | METOP-B | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69b3c961-bba5-3233-860d-c69c81acebab | -11.5089 | -54.552101 | 2025-09-05 00:36:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc196009-fb05-373f-8212-3e883325505e | -15.4023 | -48.439602 | 2025-09-05 00:36:00 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a6650f34-3c7e-37fd-a12b-dd5647ba2496 | -10.9584 | -52.045399 | 2025-09-05 00:36:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dee40a6b-edba-3680-9560-cf66435fa309 | -7.938 | -45.3759 | 2025-09-05 00:36:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b3fb0781-219a-300e-8747-3b087e7d49d0 | -5.3509 | -60.1329 | 2025-09-05 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b59a3c8a-2368-392a-9436-86e8c48942af | -9.8201 | -51.669201 | 2025-09-05 00:36:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecb5a146-60c4-3846-966b-1fa15fa5df65 | -7.5449 | -50.313099 | 2025-09-05 00:36:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca8a2a2-e198-333a-b9a4-c5d4dda81d06 | -5.9017 | -46.025299 | 2025-09-05 00:36:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 031d5f82-d119-37d6-8d10-f591c660173c | -22.1369 | -47.163502 | 2025-09-05 00:36:00 | METOP-B | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4fe887ed-54ea-3dd7-a975-38776d30fa10 | -9.9474 | -48.101799 | 2025-09-05 00:36:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e655307d-ce4a-34c6-adb3-b6cedbffcf16 | -3.5347 | -49.057598 | 2025-09-05 00:36:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b022387-071d-3ac4-b775-86f68753d5d7 | -10.3534 | -50.455502 | 2025-09-05 00:36:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0cc7bfb-b81d-3bcc-9a4c-02788c38976b | -2.6342 | -49.646999 | 2025-09-05 00:36:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb4b9663-6349-33b3-b0f9-467fc8989e2c | -22.134701 | -49.599499 | 2025-09-05 00:36:00 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fbe21696-3793-3b2b-9876-694e80c7e4a7 | -11.0589 | -55.033199 | 2025-09-05 00:36:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2c4579e-95a2-3f07-b914-1c49e728ee30 | -7.8463 | -45.4613 | 2025-09-05 00:36:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b8aa96be-5f6e-3e75-83b1-495e788107c1 | -22.489599 | -46.777901 | 2025-09-05 00:36:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fcf3c31f-1b3e-38c7-9b06-54ba2f333bb2 | -4.022 | -56.151699 | 2025-09-05 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6636d88e-638d-30fc-ba26-a8943ee34a87 | -6.4338 | -44.565498 | 2025-09-05 00:36:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96d1b964-3587-3196-9c08-5d82912784de | -9.8281 | -51.659199 | 2025-09-05 00:36:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb8e8d9a-8560-3ea5-88ee-c5a2d3debbe8 | -18.7239 | -46.398201 | 2025-09-05 00:36:00 | METOP-B | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ed4ad807-6bdf-3f64-9622-8f8b05855155 | -19.5441 | -54.826199 | 2025-09-05 00:36:00 | METOP-B | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| babacbb0-418e-3e10-8fbe-1de816556234 | -6.6631 | -52.832298 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1abb6e-35bd-3800-981c-ac1333b0cb5b | -4.1279 | -48.215401 | 2025-09-05 00:36:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e0a85bc-0c0d-3be9-96d9-d9ab48877112 | -9.0841 | -57.105202 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c452f99c-14f8-3640-84e9-fc987dccc7fc | -8.3756 | -51.355099 | 2025-09-05 00:36:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe6908d8-3106-393a-b716-17fbb3f6e9b8 | -10.8933 | -52.076099 | 2025-09-05 00:36:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51db8fab-827f-3fb3-9015-37e3bf9ab2dc | -7.6526 | -52.1553 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e12d11f-4682-3640-aeae-2cb8eb76be02 | -3.5286 | -49.0317 | 2025-09-05 00:36:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24d1679d-8411-3c97-8cc9-c2e252b5274e | -9.8901 | -48.376999 | 2025-09-05 00:36:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09f90bd2-033d-3713-988e-7bebeedb1287 | -15.6912 | -51.7724 | 2025-09-05 00:36:00 | METOP-B | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e481b1da-7c77-3f17-8923-bfa02202eb18 | -9.1581 | -56.8297 | 2025-09-05 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bbb3342-8afa-3bae-8c2b-8be01ae060c9 | -6.7041 | -52.830799 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 570c887e-e7ff-3868-b5a9-4670c5f5a341 | -11.4493 | -52.208 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 616853de-f949-31cb-a2cd-7f07ab1f28b3 | -15.6181 | -53.640301 | 2025-09-05 00:36:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e55847df-d7c2-33b1-bd57-2e3a05ca84b4 | -23.251301 | -46.882 | 2025-09-05 00:36:00 | METOP-B | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 118c1b91-b350-3f7b-ae22-1af57e6f040a | -11.7147 | -51.4743 | 2025-09-05 00:36:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d9b186d-c6d6-3563-a721-4d0e2e7de0f6 | -6.1968 | -47.115398 | 2025-09-05 00:36:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0852098e-cf22-378e-9315-5672807cc2a2 | -17.385 | -46.641399 | 2025-09-05 00:36:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 605fb9a3-33d4-3b8c-9c4c-8c4b4792c70b | -6.7284 | -52.801899 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aebc14c-c2e7-3339-8365-c2a3f94525b0 | -22.1392 | -47.172901 | 2025-09-05 00:36:00 | METOP-B | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 80c8b343-7cbc-3b16-b7bb-e371374c5b68 | -15.6928 | -51.779598 | 2025-09-05 00:36:00 | METOP-B | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f19fc203-322c-3d89-b10a-ebac54969e93 | -3.1795 | -54.922298 | 2025-09-05 00:36:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd094a9-e4f8-3623-835e-5949b6f58f9b | -8.3835 | -51.344601 | 2025-09-05 00:36:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a0f47ba-591d-327c-8964-72c37d4810d3 | -6.6926 | -52.8256 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b22f9b95-ef67-35e7-a027-008c8c003070 | -11.4558 | -52.1912 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 149bf3d8-a980-3f19-b007-1459ff4b5561 | -15.5676 | -53.644199 | 2025-09-05 00:36:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 636dbd1b-e38d-3f75-bd71-ee5b15153cc9 | -5.5794 | -49.314499 | 2025-09-05 00:36:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85ded696-7ad8-3786-8a07-c643b5f72d40 | -10.3337 | -53.659901 | 2025-09-05 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37ae4fec-58a0-31bd-be39-0291e62d5763 | -9.5652 | -51.102299 | 2025-09-05 00:36:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec29f4f6-f30d-3e28-bdde-0f35186ddc62 | -9.5535 | -51.0965 | 2025-09-05 00:36:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a36a3898-e809-32d1-96e1-0c2a2a2738a9 | -12.9613 | -57.132401 | 2025-09-05 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 744e1c26-2270-3ed8-b0d0-73760a766943 | -9.9479 | -54.7971 | 2025-09-05 00:36:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87220a57-36dd-321f-9fe3-4a0c5d566ffc | -11.4362 | -52.195801 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 767c3926-cc38-3df9-b948-e0b6a8660c55 | -8.5127 | -54.868099 | 2025-09-05 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00b49f73-f300-3b10-baa7-abb9132774d7 | -9.1995 | -55.228901 | 2025-09-05 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a78d2b0-ba35-33d4-ab6c-8bf28b6f1d73 | -11.4721 | -52.217999 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc605a42-d103-336b-9ef9-59eeb93075b8 | -18.398001 | -48.289501 | 2025-09-05 00:36:00 | METOP-B | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 03b57e03-be4f-396d-a418-b073ce8099d0 | -15.3182 | -53.0644 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0bd4d75-b055-3064-b6e0-40cbef6f86e7 | -8.3719 | -51.338699 | 2025-09-05 00:36:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff9a067-6956-3d55-b3b5-7ba5a09c46bb | -15.5887 | -53.646999 | 2025-09-05 00:36:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf3d07e7-d36f-3aff-8a9c-a5bbe9f127d0 | -10.3079 | -53.6366 | 2025-09-05 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdce36c8-7ef6-3d9d-8e48-d347768a4dcc | -11.4705 | -52.210701 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5aeab575-a652-3183-b392-7fd1369b0b85 | -10.619 | -48.318199 | 2025-09-05 00:36:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| beb8e603-ede3-3b07-ac58-354df06dc517 | -8.9128 | -47.030102 | 2025-09-05 00:36:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd29e752-057a-3014-a555-370ffd8f87cc | -5.3532 | -60.1436 | 2025-09-05 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d550882-3402-3eae-b599-47713ccd48ea | -9.9959 | -55.015202 | 2025-09-05 00:36:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11fc5860-64a8-3413-8e3e-0ac57cfd46d8 | -8.4789 | -55.087002 | 2025-09-05 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c540005-c8c5-307c-934f-0ae1cf0c9677 | -6.7198 | -45.596699 | 2025-09-05 00:36:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 477ad588-068d-3d3a-9130-6ad546bd4528 | -6.4493 | -44.586498 | 2025-09-05 00:36:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9124cbad-92ed-36fe-9969-eb92a1ebe931 | -11.6323 | -50.672298 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 758a4f2a-8821-3529-bb9e-c82095a9eb45 | -9.0823 | -57.097099 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d745f0a-5c3a-3631-a75a-fa85e33c89c4 | -9.5614 | -51.085999 | 2025-09-05 00:36:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c2f062d-4c69-32c4-b652-a6df0908deb1 | -9.6535 | -48.337002 | 2025-09-05 00:36:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28aa50d0-51c4-34e9-b0f7-ad82dec0737e | -12.9576 | -57.1143 | 2025-09-05 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
