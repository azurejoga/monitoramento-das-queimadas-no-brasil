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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e584cf4d-5392-3063-ac6c-7f0612671c1c | -10.3512 | -50.4876 | 2025-09-14 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 097b8af4-cb2d-39fb-bea0-cb8cf58ca2d3 | -10.9452 | -47.3538 | 2025-09-14 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 9224ce97-e76e-303e-96fa-020e203687b7 | -12.9294 | -54.7333 | 2025-09-14 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 701.8 |
| 48b61ccd-061b-3a75-8064-26b6da6f1b96 | -12.8212 | -47.1445 | 2025-09-14 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 181.2 |
| d1aa2051-c771-3943-9f17-6ab603ba9167 | -10.7477 | -50.5106 | 2025-09-14 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| da3de494-16b4-3bef-8b6b-3bcb4742c54c | -8.9368 | -46.132 | 2025-09-14 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 309.2 |
| 5efb3835-c0dd-34f8-9937-57745d9b1af7 | -8.6404 | -45.7122 | 2025-09-14 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 971e6a13-aad2-3ec1-917d-26a97f0096e9 | -14.3747 | -52.927 | 2025-09-14 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 84891c3b-43e5-3a1f-89c3-7d99352eeb50 | -8.979 | -45.7892 | 2025-09-14 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 26ca5323-6ec1-3d4c-af0b-1cab6f38c0fe | -7.5267 | -44.3874 | 2025-09-14 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 980c30a7-62cb-32e0-84a6-a52346f70c4c | -6.3165 | -43.3381 | 2025-09-14 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 5ba15574-ec1d-3317-a7fd-b4caad6461e4 | -8.9173 | -46.179 | 2025-09-14 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 340.3 |
| 4123ff96-6ea7-31c9-a4ad-d5c8e4a999be | -8.9371 | -46.1094 | 2025-09-14 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 61500887-9e0c-37c5-bcb9-1dee66884221 | -8.8893 | -45.4363 | 2025-09-14 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 9ff1e587-1274-32d8-8da8-1128f2db790d | -8.9176 | -46.1565 | 2025-09-14 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d846db6c-1475-3f99-90a4-5dd55adc3b49 | -11.4303 | -50.479 | 2025-09-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d3b21492-e626-33fe-87d4-23865c3ea30d | -12.8019 | -47.1474 | 2025-09-14 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 03cdc921-85ea-3627-900f-d94963017457 | -11.4473 | -46.9097 | 2025-09-14 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 408042c9-4fb2-34a1-835b-d584d1677b61 | -14.4779 | -47.3368 | 2025-09-14 14:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 59746db6-d5ae-3b59-9a99-2e6b935d7049 | -11.7024 | -46.4927 | 2025-09-14 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| c34e0f77-6d1b-302b-b5fc-a3eb73894819 | -12.9101 | -54.7558 | 2025-09-14 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| d9034a98-482e-368d-9776-67cf1a188ffb | -10.3512 | -50.4876 | 2025-09-14 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 92b91a0d-2165-384e-9e5e-fafda0e91e78 | -13.5876 | -51.6715 | 2025-09-14 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fefe3d2c-ddc2-3768-aa8c-4d5546d26f15 | -12.1044 | -47.5816 | 2025-09-14 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3269c307-58c8-333c-817b-e83b1f908681 | -14.1703 | -46.2505 | 2025-09-14 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 60d48acd-3a02-37a1-ac52-77e5a78f1622 | -11.2885 | -51.1122 | 2025-09-14 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c72981df-c276-3759-8d57-c0f1d92b1702 | -10.7667 | -50.5086 | 2025-09-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 41cc9c49-43a0-3b85-912e-f579e5a84238 | -10.0509 | -50.3686 | 2025-09-14 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 183c817d-381b-3d00-bbe0-8cf117cd8c94 | -10.9286 | -47.2 | 2025-09-14 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| e936227b-c8a2-321b-bf84-f1e74cdf54d6 | -8.9076 | -45.4797 | 2025-09-14 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8e7f574d-99d9-3227-9f62-ad0d67e58a47 | -11.7215 | -46.49 | 2025-09-14 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 3b7e8405-33fe-3438-b144-e0d2feef99c0 | -11.2695 | -51.1142 | 2025-09-14 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 77286646-b301-3b94-b6b8-911a077a7b7b | -10.7474 | -50.5319 | 2025-09-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 0e5d8754-332e-3f3a-ba3c-d572c1c8dca3 | -9.019 | -47.0616 | 2025-09-14 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 391a62c2-8920-37d7-8f79-f0722364b384 | -12.9292 | -54.7538 | 2025-09-14 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 326.5 |
| 7c7b186e-f955-3c54-bdce-501cc317ee18 | -12.8208 | -47.1671 | 2025-09-14 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| de28c36b-3aa4-3eba-bf26-cc1c10e615bf | -16.673 | -49.7615 | 2025-09-14 14:30:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 1cb2d144-5a7f-3e17-ae84-c0819d318446 | -10.3509 | -50.5089 | 2025-09-14 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 59955eae-593f-3d4a-aa50-0a2b565122f9 | -8.9979 | -45.7871 | 2025-09-14 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 154.4 |
| dda1e020-377c-310a-a8ae-82c8a5dacdbf | -11.1149 | -51.3423 | 2025-09-14 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5f3b7c5b-16b8-3987-962f-705efa9394e9 | -9.8838 | -50.1719 | 2025-09-14 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7937a435-2968-308b-a5cb-01084413bb9c | -8.4522 | -47.2288 | 2025-09-14 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 96b83bcd-1de0-3919-92df-a6c6077db079 | -12.9482 | -54.7519 | 2025-09-14 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 718ad365-812b-3af7-9c09-e9917678ce60 | -14.4137 | -52.901 | 2025-09-14 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d29c8a75-d1f3-3c44-88dc-7a213916abe0 | -10.8991 | -45.4656 | 2025-09-14 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 344.8 |
| 9bdd03fe-d73a-3b6b-bceb-ec91daa779d0 | -12.442 | -46.8847 | 2025-09-14 14:30:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 149f073c-6bde-3224-bb16-2ef300fb6f1a | -15.2186 | -50.129 | 2025-09-14 14:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 69116af7-0642-351f-86c8-1e7a443f1179 | -10.9262 | -47.3561 | 2025-09-14 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| b4034fe1-049e-348e-b436-2d417a116af3 | -10.7472 | -50.5533 | 2025-09-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 3a4694c9-f60c-3fbe-b03b-1550ad74a163 | -15.943 | -47.2407 | 2025-09-14 14:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2cb675ea-f65f-328f-accc-05fdbe98a853 | -10.9182 | -45.463 | 2025-09-14 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 358.1 |
| a5162ebe-33cb-3b1c-af55-d3da2b0db9d7 | -10.8803 | -45.4452 | 2025-09-14 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 89f1af2a-24c2-3a2c-99cf-163a9bcd1d57 | -9.976 | -50.3334 | 2025-09-14 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 116c8857-2b2a-3625-ab66-8227a89fb6d6 | -6.1065 | -47.8368 | 2025-09-14 14:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4292485f-36cc-348e-85c1-3fb99466dc59 | -8.8984 | -46.181 | 2025-09-14 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 1f4e205e-30da-36a4-ba31-f9b17490ff06 | -10.9452 | -47.3538 | 2025-09-14 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 986f19f0-bade-3f9a-898f-f25bb443f60c | -12.1427 | -47.5763 | 2025-09-14 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| bce30b28-64b0-389c-9383-21ea9628d9bd | -11.353 | -43.495 | 2025-09-14 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 200.8 |
| d4d6208f-aa94-31d1-acac-c17fabc48a3d | -10.7477 | -50.5106 | 2025-09-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0c4e43a0-1ebd-350f-ada8-f1c864ae4ece | -10.9096 | -47.2023 | 2025-09-14 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 8fdb3650-b8f8-3058-80ca-068ba712fae4 | -10.75 | -46.4607 | 2025-09-14 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| df2d010c-99be-3456-81c8-eddca6ce2db1 | -10.7579 | -44.7721 | 2025-09-14 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 365d7051-401b-32a3-8b8b-0abd0c09fcb2 | -12.7675 | -48.0013 | 2025-09-14 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| f1b15beb-571e-38c7-bb3b-64c7e7b64ad7 | -15.18 | -50.113 | 2025-09-14 14:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 6b451339-255a-3fa6-8e79-929008ca687b | -11.3259 | -51.1505 | 2025-09-14 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5a938f87-e189-328e-859e-c5eadc9815d7 | -9.0193 | -47.0394 | 2025-09-14 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| b7b41803-a3b0-39cc-8c00-0debe021af31 | -8.9362 | -46.177 | 2025-09-14 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 0acd14bc-2e32-3644-af05-1dd1f88a4ec6 | -8.9976 | -45.8098 | 2025-09-14 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 42b64ce1-82e7-3f8a-a325-89c6f49f384c | -7.5281 | -47.642 | 2025-09-14 14:30:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| a6ecd0ec-679f-3f9b-b131-7a985015f368 | -7.8995 | -46.2805 | 2025-09-14 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 355d6bdb-9064-3c1e-9def-ecd936f8ec1b | -9.8646 | -50.1951 | 2025-09-14 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 2a183a27-de0e-3e6d-8ee9-c3367c853edc | -11.1893 | -51.4401 | 2025-09-14 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c5728335-ce70-3f3b-83e8-5de47e904dd9 | -14.1708 | -46.2275 | 2025-09-14 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 121.4 |
| fe6c36a5-f241-36fd-aa73-ab661927835b | -11.3262 | -51.1293 | 2025-09-14 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 682e22c9-4239-3a2f-bf33-048bcd99ba62 | -14.329 | -46.0857 | 2025-09-14 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 324.4 |
| df521930-d87e-3b76-868c-2f4b9687b641 | -8.7871 | -46.0353 | 2025-09-14 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| d9545f16-2219-3db9-81b0-ac6e586c55eb | -16.0056 | -47.9555 | 2025-09-14 14:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 1b65d0a7-10b6-3dd2-b2b8-a98958ec6fec | -8.956 | -46.1074 | 2025-09-14 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| f43c55d3-0be1-392b-be95-f128f54a68c4 | -10.9477 | -47.1976 | 2025-09-14 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| db6d420f-6c8b-33a0-96c3-28b36a38ba5c | -15.7591 | -53.4846 | 2025-09-14 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7696c238-ec9a-3639-970b-4807589ff18b | -10.5451 | -51.5476 | 2025-09-14 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| e8372bce-5a3a-3c6b-9cd4-986fa33bba57 | -11.3184 | -50.3418 | 2025-09-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 8a14b9d9-b2b1-3c93-b9fe-9b36bd4114bd | -22.4993 | -50.6273 | 2025-09-14 14:30:00 | GOES-19 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 585af448-8443-3ef6-a6f1-5c4fff58d5ac | -12.0856 | -47.5618 | 2025-09-14 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 38f2096b-fddd-3cff-a5af-c614c32a0d83 | -11.2882 | -51.1334 | 2025-09-14 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f0fd90ef-b777-352b-8b40-14812d2c6b8c | -15.1995 | -50.1101 | 2025-09-14 14:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 42511cc4-2162-3c1e-9135-5ae57faf01f6 | -13.5879 | -51.6502 | 2025-09-14 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c32f7eec-0637-34a4-bb3d-0678a30c97f2 | -11.3722 | -43.4921 | 2025-09-14 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| c6e50f53-d3bc-3370-bb36-a15c9d54e257 | -15.0477 | -47.9856 | 2025-09-14 14:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 03429c20-e386-3abd-890f-a0ea6ae5f259 | -9.9754 | -50.3761 | 2025-09-14 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 29112918-2eb6-3db5-a812-de51f2ce5df3 | -11.3831 | -47.3429 | 2025-09-14 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0ccfcfdb-069c-3ed3-aefa-533b786ff5a6 | -12.9103 | -54.7352 | 2025-09-14 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 216.6 |
| 85eb2e30-f329-31b9-aaf1-e73180029b9a | -11.0563 | -51.4751 | 2025-09-14 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 33be641d-4d8b-38a5-8b44-b835fca9823d | -11.7219 | -46.4674 | 2025-09-14 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| cfbd60d1-a07d-3de0-994b-596cb67b28bb | -10.8994 | -45.4426 | 2025-09-14 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| c3a2125a-21e4-3103-8f4c-40111908101f | -11.464 | -50.7741 | 2025-09-14 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e2db7874-ab39-387a-aa3e-b67aa30b0b20 | -12.7671 | -48.0236 | 2025-09-14 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 76a16133-e2fd-357e-b41e-54649d8faa92 | -11.2888 | -51.0909 | 2025-09-14 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 6499437a-94b7-3da4-9511-bca390d7bf1b | -10.5586 | -51.9661 | 2025-09-14 14:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| b2ec7e31-a80d-3319-acac-0ee4a6de0efe | -9.9571 | -50.3353 | 2025-09-14 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |


[Clique aqui para ver as próximas entradas](README91.md)
