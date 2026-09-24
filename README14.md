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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b8b5a83-77e8-3495-87e2-f69854dfa43e | -8.358 | -45.5919 | 2026-09-24 00:38:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d617972e-73ba-3c1c-925a-31eb0acbb9e6 | -11.2678 | -51.3391 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7cb571ec-75c6-3b21-8828-6ffecdbf1a0e | -12.4106 | -46.958302 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 690cffca-4255-3024-b329-da104f945526 | -2.171 | -48.3218 | 2026-09-24 00:38:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5f3f6f8-2aa2-395b-a44b-c3b45237ead3 | -7.4622 | -44.554798 | 2026-09-24 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7aee3e9e-7410-3c0f-b37e-1215ad8752a5 | -3.4424 | -50.0839 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d218cc21-b208-32aa-9333-7da12f4c918d | -5.8373 | -49.874699 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9d31df8-e2fd-3e77-b091-659a3bd98070 | -3.0432 | -46.919102 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 135b9e77-7dc2-38c3-b994-50a7323e1b09 | -12.4075 | -46.944401 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cd295f1-1ab5-3c0b-844f-bd116cef1682 | -1.4243 | -54.597 | 2026-09-24 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e47fe34d-2bbf-3bcc-b35b-fed46dd967ce | -5.0035 | -45.549801 | 2026-09-24 00:38:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb097794-d981-3c02-82e6-d46630309ef1 | -5.847 | -46.110199 | 2026-09-24 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2fb6277-0923-37ab-b4bc-34e65465e8ce | -10.6489 | -51.319 | 2026-09-24 00:38:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19af9e57-4cb9-3bfb-8d78-0567c212bf81 | -18.344601 | -46.407001 | 2026-09-24 00:38:00 | METOP-C | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7b6c1feb-569f-3150-91ef-3d22016a895c | -11.2619 | -51.359699 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 614b9906-8d32-3f10-8092-7e894729642a | -2.2043 | -48.152599 | 2026-09-24 00:38:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43b033ad-83b8-3a31-b0d1-8957aad8783c | -11.9604 | -50.746101 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d9f7dc5-8e0f-3e6c-ac71-56796e1f7d29 | -7.6714 | -45.482201 | 2026-09-24 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86055087-f0d8-3edc-8dcc-0b751357e500 | -10.9643 | -54.076302 | 2026-09-24 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 325a61f5-1548-36e6-b75f-84df7bfd1675 | -11.1288 | -48.310902 | 2026-09-24 00:38:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bcc04d40-41a4-3261-873f-f587d8912eef | -1.1954 | -54.135201 | 2026-09-24 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b405f71a-2201-3f52-8b1d-c588c42fd952 | -7.0279 | -44.638699 | 2026-09-24 00:38:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba6b99a2-c97e-3676-9860-b6c588157038 | -6.6072 | -59.920399 | 2026-09-24 00:38:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d128a277-da6b-3d36-9ef8-5b57d38b4514 | -6.713 | -44.1394 | 2026-09-24 00:38:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c6773b7-9715-3cc4-a07b-ea29845136a5 | -9.5939 | -47.765701 | 2026-09-24 00:38:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65df18a8-4876-3bf7-b5c5-6614c6d0c43c | -5.2246 | -49.221401 | 2026-09-24 00:38:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbff1f45-98f5-3e7f-9c4b-77f895933770 | -2.7595 | -57.0075 | 2026-09-24 00:38:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 226e4672-508a-3934-8a86-ee37c732c88d | -4.5633 | -44.078999 | 2026-09-24 00:38:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e99c665-c512-34e3-ab54-7b6a9b7d3818 | -4.4106 | -55.062901 | 2026-09-24 00:38:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a15fb3fe-8e92-3d0d-9aab-bc4ee0f83269 | -3.4537 | -50.0886 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b87a2668-1660-38cd-b886-58a9b0cf2687 | -4.1206 | -51.071201 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 936a813a-1b9e-3661-b38e-f17fb26f619f | -3.2679 | -49.1427 | 2026-09-24 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e22e385a-3482-3223-8d10-ebc77651869c | -3.1831 | -48.013199 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e18fd6bd-ec4b-3276-82ba-3b75988c4346 | -5.8389 | -49.881802 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c84678e4-330e-3029-9d7e-3152bd61b60c | -5.2321 | -49.299301 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84098dd8-f795-3787-ac40-ee2a2dbd520e | -10.6508 | -51.328098 | 2026-09-24 00:38:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4cdfb68-687c-31a7-8ebc-791f8d0b1d32 | -10.2099 | -44.1637 | 2026-09-24 00:38:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db7909c0-8293-395c-8a52-c9b1d1dfdd42 | -10.198 | -44.157501 | 2026-09-24 00:38:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0cf1ff1c-8c51-3795-a3ff-0027986bec0d | -8.4657 | -48.697601 | 2026-09-24 00:38:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5f922e2f-6f4d-3066-9832-09bedc263ea3 | -0.9295 | -47.545799 | 2026-09-24 00:38:00 | METOP-C | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92a31d78-4c27-30df-9d43-9a34edb29575 | -5.8556 | -49.774101 | 2026-09-24 00:38:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4118e352-0e63-3c0a-9dc6-4c0460e47590 | -10.8975 | -53.949902 | 2026-09-24 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53c9292c-0d74-3fc9-b459-5567d1c2c414 | -8.1239 | -54.808601 | 2026-09-24 00:38:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d043d7d-191a-3bb4-ae64-a79af4985bc1 | -6.5769 | -44.131802 | 2026-09-24 00:38:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32b1e06f-4b2b-3ade-a877-96e4f422359d | -5.7876 | -50.201099 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d97f5d9-4904-33b3-a32b-8bbd51b33c76 | -10.2809 | -49.958698 | 2026-09-24 00:38:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbee32a1-c86f-3a55-ab9d-8a57cff0417b | -6.2676 | -43.270901 | 2026-09-24 00:38:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2630999-a3d2-32a7-ba99-337e9b6b4d3a | -1.6279 | -54.904301 | 2026-09-24 00:38:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6a29ae5-12f6-3ed0-8512-2c4defde2b5d | -13.4624 | -46.277901 | 2026-09-24 00:38:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 76aca811-4cb5-3a00-bdc5-2c6bdc20bd6d | -12.1502 | -47.355801 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 690f340d-1dc5-3308-b82a-ea0672d2d972 | -9.2639 | -46.2421 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7528a26-dc63-31c1-b33b-8cc4196a8300 | -5.5704 | -42.303699 | 2026-09-24 00:38:00 | METOP-C | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bcc3d67e-7248-3ccf-93d8-dbfd8e6be30d | -3.2082 | -50.819199 | 2026-09-24 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcb0ab74-ff0e-3cb2-80eb-3c59913afa06 | -11.2325 | -51.3661 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3a0747b-54fd-3263-afe8-1fd929ad3e6e | -1.2609 | -57.0243 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d316d7b-4f2e-3ea8-9904-f89f89f66361 | -6.4209 | -43.479698 | 2026-09-24 00:38:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 187c7470-a109-3190-a500-72f210b88366 | -7.4257 | -47.351501 | 2026-09-24 00:38:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66db8a9d-df77-3bbc-8df6-3f1a260412c2 | -5.8178 | -47.761299 | 2026-09-24 00:38:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cafea8ab-3edc-3cb0-bb3a-711b753b9ce0 | -2.9816 | -54.264999 | 2026-09-24 00:38:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d0d3254-ea03-355c-8593-a75ee234f653 | -7.2756 | -46.7925 | 2026-09-24 00:38:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e9eaa35-2e01-3d1f-b0cc-477ff4cd4432 | -12.1967 | -47.015099 | 2026-09-24 00:38:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e20913a4-71d4-3261-98a8-8a8ce903af9a | -8.7469 | -44.2682 | 2026-09-24 00:38:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c6344a99-6545-38aa-a49e-98d93ad67777 | -15.4646 | -47.912498 | 2026-09-24 00:38:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 59f18d5b-0afe-3982-8b31-3059a3a34663 | -10.9072 | -53.947899 | 2026-09-24 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40253da4-34c0-3e7e-a8bb-58f94c3b0ace | -7.683 | -45.487801 | 2026-09-24 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf19fd28-a3f4-3d80-8088-8094de1c1801 | -11.2384 | -51.345402 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3c89f39-da5b-3ddd-a698-f3df4f0ee353 | -6.4275 | -59.926201 | 2026-09-24 00:38:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9dbcb84c-e5fe-3600-9725-3e29cfbdefcc | -3.0663 | -49.567501 | 2026-09-24 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d70e03bf-e3cb-3050-98c7-0d232d87e2b8 | -2.7969 | -51.364498 | 2026-09-24 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60257be5-e84e-3dcc-92e7-ef10703dcc8e | 3.8387 | -51.793201 | 2026-09-24 00:38:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 33e2a5b1-0ec2-31a9-b79f-9fe69f22754f | -6.2107 | -47.496601 | 2026-09-24 00:38:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c488c1e-090e-3c5e-820a-045c8b96995f | -8.9219 | -43.877102 | 2026-09-24 00:38:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af254cc1-ce84-3b08-99bc-f0ae8c73ecf1 | -2.8297 | -46.710899 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3d31fcd-d906-3d1d-aec2-192f3a63525f | -4.8125 | -43.523499 | 2026-09-24 00:38:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9f2eb5a-5451-38ab-8a3a-a044bf93ce45 | -5.6589 | -42.5844 | 2026-09-24 00:38:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c433dfd-c599-3233-a5b5-17119ab681fb | -2.1157 | -49.515099 | 2026-09-24 00:38:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1378e8a2-90b5-3e88-ba63-ac739c7c4ec9 | -2.9274 | -48.7388 | 2026-09-24 00:38:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3506382-de63-3db7-9181-c056291860a4 | -12.0131 | -47.799099 | 2026-09-24 00:38:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f651efb6-5f29-30bc-a394-bdb010f96ac5 | -8.8975 | -45.911098 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8204efed-1fbf-3f73-ab31-f2f9b62942b0 | -12.1224 | -47.369499 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f31abaaa-033e-33e9-af57-efabad689b45 | -12.124 | -47.376499 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49b81398-3496-3909-9db3-1c71e322521a | -5.8162 | -47.754398 | 2026-09-24 00:38:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbc51595-2e3d-312b-b330-9fd802c3ceb6 | -11.2698 | -51.3484 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b7bdc66b-fe09-39a1-a85f-a63b6dc1bbbf | -8.7868 | -45.8349 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 48c1e5af-927d-381c-b2c5-939ed1f900b1 | -3.1603 | -54.6026 | 2026-09-24 00:38:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 051f5de0-eb73-3564-9733-b573b2b4005c | -13.7824 | -54.053001 | 2026-09-24 00:38:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 01359098-ff54-325d-9f52-6c50a5ffc454 | -10.6117 | -48.945 | 2026-09-24 00:38:00 | METOP-C | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14250301-7dfd-31ea-bb2a-d0ccb3c779dc | -11.9319 | -48.218601 | 2026-09-24 00:38:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a54399d-25ff-332d-9bf1-7d6dc4ca0cb3 | -3.5497 | -43.4543 | 2026-09-24 00:38:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb5de01e-6dc8-3fea-987d-bc0870ddf84c | -13.0773 | -47.400398 | 2026-09-24 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb4d01d4-8ba7-3d42-82de-f27786540477 | -7.087 | -52.7556 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c33219b-7436-3963-ba44-1725e7e8dcaa | -6.7272 | -44.155899 | 2026-09-24 00:38:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76b26199-fb18-3214-baa7-eb6d2954f2da | 1.5718 | -55.821602 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0de4952-ba5d-37a7-8712-249d3bd9190a | -7.4741 | -44.561199 | 2026-09-24 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a8083e7c-5cbd-34c3-ac2f-b789804b6919 | -11.7947 | -50.977402 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 222769ba-cf07-3bab-aeb5-352a80bc7fe1 | -5.5771 | -42.288601 | 2026-09-24 00:38:00 | METOP-C | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1188636e-0b11-3614-9d13-72c1e87f9ee1 | -5.5817 | -60.161201 | 2026-09-24 00:38:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c20d390-e965-333f-96a4-f670be9c0eec | -3.1058 | -51.047901 | 2026-09-24 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93cf3aa2-6a2b-3d71-a7be-b433c52ca0bb | -7.4301 | -49.859299 | 2026-09-24 00:38:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdde6b55-521e-325a-947a-e12734c5d7d5 | -6.4184 | -43.469299 | 2026-09-24 00:38:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README15.md)
