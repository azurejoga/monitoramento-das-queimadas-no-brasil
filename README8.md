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
| d2d99551-1617-3ee6-97a8-3d421330032a | -11.2467 | -46.504799 | 2025-09-07 00:45:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2166500c-2652-35b4-a74c-10ae3bfc43d1 | -5.9919 | -44.159599 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 231d7bb7-ddf4-3a30-a162-19f1c31f5217 | -17.5467 | -44.4132 | 2025-09-07 00:45:00 | METOP-C | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d2254b31-f6f4-3c3e-be59-4f7d268f488b | -10.7144 | -48.59 | 2025-09-07 00:45:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3374c869-554f-396b-b99a-b658a668ad27 | -22.769899 | -51.309898 | 2025-09-07 00:45:00 | METOP-C | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc3e780a-4320-3e4e-992f-60c032d91346 | -5.8592 | -51.954399 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 250f54de-fd81-30fb-9f71-ebbae5dda048 | -4.1641 | -42.042301 | 2025-09-07 00:45:00 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 814eeb4a-6290-3485-99e0-fdbccf9624c3 | -12.8331 | -48.023701 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1482d3c-42b3-3e67-a6da-0db65593a92b | -9.7006 | -49.4856 | 2025-09-07 00:45:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4098f516-2a69-3e5a-a6ff-0329f2fe4d77 | -7.7365 | -48.824299 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 547506d0-1072-31fe-b7b4-8fff17124e23 | -13.8165 | -43.872501 | 2025-09-07 00:45:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7e10db1-913f-3fb3-b621-af14c2c9a39d | -6.9367 | -50.977901 | 2025-09-07 00:45:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5246112-159e-3400-a850-d5dab1c64e1c | -17.3484 | -42.640701 | 2025-09-07 00:45:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d93a81c6-4310-3e1b-a5a4-13cbf00e371d | -11.3814 | -43.557899 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7866b0ac-0127-3add-b6f8-7676eb790cc3 | -7.0101 | -44.965599 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6cb5ff0-ca14-3d19-9553-f7d85a9e1415 | -3.4015 | -50.294498 | 2025-09-07 00:45:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 911e3b85-69bb-3055-80aa-9d7514184098 | -11.5733 | -47.742401 | 2025-09-07 00:45:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca619457-384d-3043-aab0-674f141060ca | -8.0395 | -52.377399 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa470c3-247d-3b0c-9169-a8631f7b7b5e | -10.6015 | -44.349701 | 2025-09-07 00:45:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e919c837-4406-3900-941f-450482c3bad1 | -11.1333 | -48.392101 | 2025-09-07 00:45:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5025b69b-9085-32cb-9298-6c78626980d8 | -4.4699 | -48.124298 | 2025-09-07 00:45:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88944fd2-c33f-36e2-8297-66c9b1e3a117 | -5.9597 | -53.6036 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb650c9-1766-3c14-9db6-2bed3a4941c5 | -11.1897 | -55.027199 | 2025-09-07 00:45:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f308329-b926-3ec1-98b2-98778626615a | -6.802 | -52.8176 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f6614a7-2899-3bc7-9348-f94fedeb3296 | -11.4008 | -43.637402 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa236bd2-82f5-33b2-823c-c6d3565f83ad | -6.8076 | -50.8619 | 2025-09-07 00:45:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d6c0576-903e-3b9b-9ed6-5a518511dc0b | -20.539101 | -46.453098 | 2025-09-07 00:45:00 | METOP-C | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d8102308-0593-356b-adc0-3fe80b33f646 | -8.3357 | -52.557999 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6bbdd4-e8e9-378a-8d44-29fb528f64e8 | -10.3782 | -44.969398 | 2025-09-07 00:45:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa9f0e53-daed-3e7a-b7d5-6e03f86f5d20 | -10.1423 | -48.749298 | 2025-09-07 00:45:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2cd61b0-97f2-39aa-bfb3-d5b01431c41f | -6.1828 | -53.266998 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88ff053c-b2a8-3df0-b3c4-287e704a991d | -13.819 | -46.2868 | 2025-09-07 00:45:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1122deb5-e845-34fa-a962-5f1cdf26ec40 | -11.1318 | -48.385201 | 2025-09-07 00:45:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1bf7bf9-c1b6-3899-8da1-27103c476f6f | -11.4153 | -43.654701 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 371f3311-dc94-3235-ba56-9e538b5ce51e | -12.9308 | -48.0453 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4443a66a-c457-32a3-a92c-b87d59d3267f | -6.954 | -46.517399 | 2025-09-07 00:45:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52f8e2e9-7c3e-3f3f-b349-04c7509b21ab | -19.934401 | -43.612202 | 2025-09-07 00:45:00 | METOP-C | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe5ef909-7e97-31af-8c6c-8873e580eef9 | -11.3935 | -43.6077 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 70804896-8b1a-3dd9-ab13-df0a792509db | -2.7734 | -49.625198 | 2025-09-07 00:45:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec1c4a34-8259-3de5-8951-43c72653f09f | -8.4958 | -51.326302 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 690a2073-17ee-30e5-b8e9-33ee54e004bc | -13.8288 | -46.2845 | 2025-09-07 00:45:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8eb78f26-2c77-38e7-aa52-0c7c4624f398 | -8.1444 | -44.873699 | 2025-09-07 00:45:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0d15df10-54e4-33a8-b08d-ebfc52d5bef0 | -10.1408 | -48.742401 | 2025-09-07 00:45:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6423059-0be9-3fae-95fa-282ffb9a413a | -16.5294 | -45.1021 | 2025-09-07 00:45:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 039c5c47-929b-364c-8564-c9b912b5433a | -7.3522 | -44.325401 | 2025-09-07 00:45:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 803244c6-61dd-3be7-a2bb-d96d312ba21d | -12.8218 | -48.018902 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cebdf07-5b29-3a79-806b-5566ba1f0468 | -9.8349 | -48.848301 | 2025-09-07 00:45:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa14ed7-6e59-3467-8d91-13eb020c0786 | -10.1489 | -46.226898 | 2025-09-07 00:45:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec62b52d-51ce-30a7-ab4c-57da8b1e8feb | -6.1906 | -53.255901 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b457a9c6-6d45-34f7-a7c0-58c63e57599e | -11.8013 | -48.246399 | 2025-09-07 00:45:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74bd7366-f1de-38da-b5be-3a7ae41e9c41 | -5.6797 | -48.135502 | 2025-09-07 00:45:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 52cd2d05-0865-3f29-a3b6-8af69e2066e7 | -6.8412 | -52.809101 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3755cf2d-3586-3ee3-bb07-595122c6dc22 | -14.7386 | -47.5149 | 2025-09-07 00:45:00 | METOP-C | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45fcfba7-8e90-3373-9d92-389afcc9c779 | -5.5721 | -51.9128 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eb58dda-e5e5-33e9-b66f-3ea5676a339d | -5.7918 | -45.658401 | 2025-09-07 00:45:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3174d37-c557-308b-b7ce-58cf7d46d9a7 | -8.3358 | -48.288898 | 2025-09-07 00:45:00 | METOP-C | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba9f7c86-82e1-3c59-bb00-4bf356032361 | -6.2644 | -43.493099 | 2025-09-07 00:45:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea66291-ab94-3218-8c7e-fe359486d1e5 | -13.7616 | -52.7659 | 2025-09-07 00:45:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb1a774f-be76-37c0-98df-35dbf3132894 | -13.8514 | -46.248402 | 2025-09-07 00:45:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2683f0e8-f4d5-3ace-9b39-2897add95463 | -6.1967 | -43.596802 | 2025-09-07 00:45:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 257f06de-958f-3f8b-b252-2b71faed7dce | -7.6609 | -47.3335 | 2025-09-07 00:45:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fe81a65-c109-3ab1-bd62-a27e679429a1 | -5.725 | -45.376301 | 2025-09-07 00:45:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63ac7798-6434-34ab-bf1d-82eb787e6d9d | -1.9187 | -56.581402 | 2025-09-07 00:45:00 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af310171-cede-32d7-84c3-07a7c191c0b1 | -3.1951 | -54.966 | 2025-09-07 00:45:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96e6599d-f124-381c-90fa-77aeb8163005 | -10.7159 | -48.596901 | 2025-09-07 00:45:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b72fd37f-5f05-3ee5-8dc4-c02b9efb19f7 | -2.4231 | -49.312901 | 2025-09-07 00:45:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd59234-1c70-393e-99a0-69263f453324 | -11.7953 | -50.584301 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 801ed5a3-004f-35e5-a866-fe33d1b2594c | -19.8834 | -41.439602 | 2025-09-07 00:45:00 | METOP-C | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4955ed13-c896-3b55-8e51-5f3af6f76754 | -5.9724 | -44.1642 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3693c119-050e-3cf4-bc73-42f6724680f0 | -6.4763 | -43.986698 | 2025-09-07 00:45:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3f3a27c-60bd-3a62-9b03-e894b4c9c82e | -5.6795 | -45.445499 | 2025-09-07 00:45:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6373e30-220b-3b18-8c64-b7c55327a43d | -8.3455 | -52.555801 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 522e329c-d595-35b5-953e-d7d369ee9b9a | -8.061 | -52.381599 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fe65788-e5c0-30ef-9766-97fcbfe20e4f | -12.7695 | -52.9519 | 2025-09-07 00:45:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da4991ac-8382-3b48-8209-4b9ff2d5b7ae | -6.1375 | -44.250599 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d82725a-dfb4-333f-a5c3-48a7d50aec9d | -2.4215 | -49.306 | 2025-09-07 00:45:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64342636-5a7c-3ed9-a892-d6e206669fd1 | -19.8957 | -41.447201 | 2025-09-07 00:45:00 | METOP-C | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db65e076-53a0-3b6f-a26e-9fbe0ff73f77 | -11.1014 | -52.025501 | 2025-09-07 00:45:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d6c52e3-bf40-393f-b9a4-ac886ba82128 | -12.8316 | -48.016701 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 869f6995-2159-312e-ae4d-c4903598b701 | -19.886 | -41.449902 | 2025-09-07 00:45:00 | METOP-C | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a70f26d8-f0cb-3dde-b6d4-53e226b6990f | -6.9351 | -50.970699 | 2025-09-07 00:45:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2610f951-74cd-3349-96f0-a99fa66d6cc6 | -3.5789 | -47.5298 | 2025-09-07 00:45:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dff1f457-b5f3-3e85-a4f1-b69e4fc9c55b | -13.042 | -47.126801 | 2025-09-07 00:45:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18454473-4618-357e-862e-e95b182bb288 | -19.893101 | -41.436901 | 2025-09-07 00:45:00 | METOP-C | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f759c728-58f8-3c32-b1f8-db7d2bf3a860 | -11.1994 | -55.025101 | 2025-09-07 00:45:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74656919-6f90-37d7-8714-cac07308b491 | -21.335501 | -48.573799 | 2025-09-07 00:45:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c43d6b65-d061-3cb1-a40b-2def1bd0fa78 | -9.6738 | -51.0756 | 2025-09-07 00:45:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85e8ded3-07c6-3478-8ab1-beeed65eceec | -6.6205 | -53.343899 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5492cd0-2a72-34d4-9377-c605febaead8 | -13.0335 | -48.043701 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ea9ad39-52bf-35c3-abd8-dfb2e33caab7 | -4.8864 | -49.9338 | 2025-09-07 00:45:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8db97871-3534-3061-a212-161b960c65d1 | -8.3326 | -48.275002 | 2025-09-07 00:45:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d97bbc5-be87-3270-8d3f-f55a80f4d33c | -11.6045 | -47.1581 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd6a5a14-478c-3dc6-8fa8-ab3930adfad0 | -17.694401 | -47.6581 | 2025-09-07 00:45:00 | METOP-C | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0847631b-f1f3-311a-abe4-259bcd95dc60 | -9.6755 | -51.083401 | 2025-09-07 00:45:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36b1b4a6-7d66-37c3-82ea-ab590a547603 | -6.8044 | -50.8475 | 2025-09-07 00:45:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4518da5f-e71e-3763-b616-5f3d398775b0 | -7.0124 | -44.974998 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bf3bae5-b49e-34ab-873a-d5e80b2e9c42 | -6.2034 | -42.646999 | 2025-09-07 00:45:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a504af89-ade1-30eb-8df1-48e80684626d | -9.6853 | -51.0812 | 2025-09-07 00:45:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98e9cbac-1a04-3008-a572-0c0fc55cec5f | -7.0544 | -50.860298 | 2025-09-07 00:45:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e90242cf-2682-3e95-9b14-94fdcaab5a46 | -8.1733 | -44.7784 | 2025-09-07 00:45:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
