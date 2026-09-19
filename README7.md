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
| 2f19b365-6142-3119-b32f-8aaef53624a5 | -13.6274 | -46.9203 | 2026-09-19 00:19:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c6a37f2-aae8-300e-ab02-4ccec94979c6 | -10.8642 | -56.1894 | 2026-09-19 00:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2935082f-56c7-3dc8-9a1e-b1c241b72fc6 | -11.0403 | -48.3041 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7cde418-1f2b-3ea8-ad1f-63ee9c00e20c | -8.4965 | -57.6063 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d07d59-149b-33d7-8542-3d1e1273ae17 | -5.6508 | -51.695099 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05a679e1-bec0-3d7c-a97a-57764679c593 | -12.9984 | -46.926201 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 494d43b5-49ba-3c3a-9448-c67811aca23d | -13.6155 | -48.323002 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 46f845fd-6d58-3d68-8a8d-27d3dfafea96 | -18.406 | -49.1642 | 2026-09-19 00:19:00 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 568005de-c4bc-3ec0-8465-494d0e5e2b54 | -6.6631 | -50.8876 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63bdb37e-60ef-3b60-90c0-fc462bdc95c2 | -13.0167 | -48.6357 | 2026-09-19 00:19:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1eda3d5-d5a7-3ec8-984c-a7cd3fc67bf9 | -12.9699 | -46.980301 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c7e59a3-ba03-3c87-9fd5-eef37e475ec5 | -6.6647 | -50.894699 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6247568-c611-322a-9622-b532ff98c667 | -2.728 | -49.459301 | 2026-09-19 00:19:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee2311a3-7fe0-38f8-86b3-f1783807f68c | -9.9768 | -50.271198 | 2026-09-19 00:19:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b1e6c5a-9f92-31d9-b72e-de12bb977945 | -11.0593 | -49.772598 | 2026-09-19 00:19:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0c00974-f8c5-30c5-8248-16e6d01f8cdd | -9.998 | -50.2738 | 2026-09-19 00:19:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5dd9e6d-fe1a-300f-ba3e-acd7e01d9607 | -12.5869 | -49.099701 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79c685a8-0b20-3a15-804a-b9d0043bfa3e | -5.8891 | -53.533001 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 338ae7a2-190f-3975-8d11-5191fb2cb975 | -4.5106 | -54.965801 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 398ab4ec-69c2-3ff5-80c4-290862e7f63b | -3.7437 | -44.392601 | 2026-09-19 00:19:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dcd6a91c-c97d-3774-9218-dcaea1ca31be | -18.402901 | -49.1497 | 2026-09-19 00:19:00 | METOP-B | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09a0e5a9-d76e-3d46-b49e-8557bc6cb620 | -10.8417 | -50.175701 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe2b55d1-63fb-32fc-926d-4589eb00ca9d | -5.81 | -49.864101 | 2026-09-19 00:19:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1cd41a3-8497-3687-83a3-daed41d5f6ae | -6.3669 | -58.2971 | 2026-09-19 00:19:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4782e5d6-1c92-3f08-91cc-a966b4de98ca | -13.0081 | -46.923801 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a63fa6a-f7a9-392d-a72b-cfa1cf26f630 | -4.7975 | -56.214001 | 2026-09-19 00:19:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3da6f3c-355e-35fd-87a6-b85d981a17d3 | -15.6693 | -52.7393 | 2026-09-19 00:19:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8cc43e2-af08-36cb-af7e-7d3ce58eddb5 | -14.2608 | -52.814899 | 2026-09-19 00:19:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ffdb69d0-c7f7-3c2d-927e-a96f6d6e6a04 | -11.0696 | -48.2971 | 2026-09-19 00:19:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1dab4972-2000-38fe-a96e-43ede2cc55aa | -12.5967 | -49.097401 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 780d4e32-2fd5-3078-8554-e1e81dc9afcf | -4.4323 | -44.357399 | 2026-09-19 00:19:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6db93876-f2ff-34a2-8594-da192705b233 | -10.8315 | -50.9067 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1359793d-9ddf-35bf-a67a-358f446173e7 | -10.8544 | -56.191502 | 2026-09-19 00:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f03b76e8-408a-30c0-a42c-af373fea6bfa | -7.567 | -57.651699 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e5db7d9-6155-3ecf-8cb9-fbe4efe83bb8 | -9.9093 | -46.579102 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0705daf-7935-3fa6-9e9f-9ef2110811b1 | -10.2352 | -48.836601 | 2026-09-19 00:19:00 | METOP-B | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e34b86f2-eb34-388e-b257-52d9b4994d9e | -5.3141 | -49.145199 | 2026-09-19 00:19:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e3945f5-0d0f-37cd-82a4-049e0f2e82e9 | -5.1325 | -56.196999 | 2026-09-19 00:19:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ce565ff-96f7-3795-bdb2-396d2903efca | -10.8331 | -50.913601 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c9b6bb6-0d77-366c-ac57-8c00061209ec | -8.3655 | -47.246399 | 2026-09-19 00:19:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8aed67e7-3654-3f19-89bb-2027e89f5454 | -9.0416 | -48.7183 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ad587dac-b9a7-3b4a-a380-ffa7e918e2e7 | -6.4846 | -43.804501 | 2026-09-19 00:19:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0148b651-ba31-3df2-9a7d-7fa0a2dcaf0a | -11.9865 | -52.4533 | 2026-09-19 00:19:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fad1c7c4-a5d5-3ff1-a64d-021833a665f9 | -14.1312 | -45.152302 | 2026-09-19 00:19:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 787bf61b-14b6-3448-81be-b185d28c9a40 | -7.6268 | -46.0951 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 630c34b2-082b-325e-9cef-ed2892a52617 | -11.3671 | -44.0938 | 2026-09-19 00:19:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f81b1483-acd9-3d40-9e83-d14d2c8ab032 | -4.3556 | -55.424999 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 153e1241-d475-3150-aea7-4dc994dbb779 | -17.954599 | -45.1222 | 2026-09-19 00:19:00 | METOP-B | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 92ccafa0-e239-3c70-99ab-0f799dd7dd6f | -12.5852 | -49.0923 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89e4f8e6-7baf-39d9-a18e-e1f78bd3ebc1 | -10.9182 | -53.971699 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48682f42-a0ee-333a-88eb-e7c8b7bd9b87 | -17.9522 | -45.1124 | 2026-09-19 00:19:00 | METOP-B | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 893b1bb6-57fd-311f-8e39-679a0022554e | -19.5644 | -47.657902 | 2026-09-19 00:19:00 | METOP-B | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3f685416-c44a-3b03-b8a9-62a13d980606 | -9.03 | -48.712601 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8ccfc4ce-92a6-3046-9ee6-c711a47d6e55 | -4.0629 | -56.236401 | 2026-09-19 00:19:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff1eb83d-f67e-33c1-9d86-99e7b82c5f1b | -9.9345 | -45.275101 | 2026-09-19 00:19:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7550d89-3f42-3d2b-9a07-2c112707d63e | -7.6296 | -46.106899 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1fd5754-573c-34de-bdfd-7a6b7b1b214b | -5.8083 | -49.8564 | 2026-09-19 00:19:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5b41bfa-4422-37c2-9ede-d85c5b0c52f3 | -10.8433 | -50.1828 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10ea7be4-8e04-349e-ab06-ed80cb3ca855 | -4.8096 | -56.083099 | 2026-09-19 00:19:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab00ede-97bc-3598-b48e-5914a218a245 | -1.4125 | -49.424801 | 2026-09-19 00:19:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ed4d1c4-ac98-3832-80e8-e7cffbb5b176 | -12.1443 | -46.9846 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b606277e-4e86-3a21-9209-d987ec9dd7c1 | -1.2007 | -54.2104 | 2026-09-19 00:19:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2222855b-397c-3fb2-9a9e-4b3afce3f9ae | -12.6041 | -50.911201 | 2026-09-19 00:19:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea7346d0-ca70-3a46-8c7e-0067b8c6cbc9 | -10.8768 | -54.065701 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d9596a2-dbdc-3bb1-aac4-52f5ab67295f | -5.9005 | -53.537998 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48088192-732d-3017-8d44-a2aee4867e00 | -6.6302 | -51.241299 | 2026-09-19 00:19:00 | METOP-B | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1510db5b-975e-3ccb-8c97-4979ef0597d3 | -6.6565 | -50.9039 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 034132d5-2415-3677-bc16-d4b4311fc663 | -9.8346 | -50.644199 | 2026-09-19 00:19:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dae7f429-baa6-33c2-ab5b-fff0658c3a2a | -14.1445 | -45.206402 | 2026-09-19 00:19:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 664d6b1c-45f4-3228-bd8b-26326893827b | -8.4408 | -45.708199 | 2026-09-19 00:19:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 83c843d3-6bea-3634-b165-8863f0329766 | -8.8648 | -49.738499 | 2026-09-19 00:19:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 943d2291-e868-310c-84d6-8dada0b19c97 | -14.169 | -47.024799 | 2026-09-19 00:19:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1421662e-e477-3e92-9382-8ca0812ff52d | -6.3642 | -58.284599 | 2026-09-19 00:19:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db82ef2e-c157-3767-b2d6-e7117e29f876 | -9.0435 | -48.726299 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 00fe26e0-6af4-333d-9927-5e170e38288b | -4.2564 | -48.539001 | 2026-09-19 00:19:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92dc7b06-9f3a-3180-add1-228ad5919043 | -10.577 | -46.607399 | 2026-09-19 00:19:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b4c4428-db2d-3019-86e4-43b5e61d4d6a | -13.6413 | -46.935501 | 2026-09-19 00:19:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9a821e51-e629-379c-92b4-c149ea6fa173 | -10.5972 | -46.090599 | 2026-09-19 00:19:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 791d6ea1-9bb8-371a-abe8-1ff678cb907a | -5.6056 | -45.2243 | 2026-09-19 00:19:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d10cc00-9131-3638-a644-3981b92443b8 | -6.65 | -50.920399 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad5bb051-4bf9-34b3-b144-1a9216e4a691 | -1.589 | -54.424099 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77e8a2d7-b932-37f9-87ff-f1fdc235a5bf | -7.8631 | -46.435902 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 148548e1-c752-3dbe-8ead-b7bef7bda339 | -10.1684 | -48.460701 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1975ffa9-cb60-32b8-bc69-b1b135a5e986 | -8.0824 | -50.963402 | 2026-09-19 00:19:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f620170d-ace2-3fa4-94f8-8be60475f284 | -11.1448 | -54.024601 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb05053b-3d31-32c7-8148-00ad11cdcc1c | -11.1273 | -47.706299 | 2026-09-19 00:19:00 | METOP-B | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c09fd117-d8b3-3ac3-acac-e634a1063abf | -4.3962 | -43.610802 | 2026-09-19 00:19:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5f18740-4ff9-3dbf-bf3e-a3bf7b2de467 | -4.4242 | -55.5023 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd7890f5-b030-3c55-87ab-16eda16c8f6d | -12.3357 | -50.723099 | 2026-09-19 00:19:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e569a7a6-97e5-3755-9103-4998b8bc29b0 | -11.312 | -47.264301 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25e47d04-f6c7-3368-b480-14061f2b2a07 | -1.2162 | -47.714802 | 2026-09-19 00:19:00 | METOP-B | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 013333d0-336e-31b0-bb8a-65bc99b19f14 | -10.71 | -60.7169 | 2026-09-19 00:19:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27d035ad-5b2c-38b3-b159-69979793b7af | -1.2135 | -47.7034 | 2026-09-19 00:19:00 | METOP-B | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 518646e0-2b7d-3951-be8e-64ac2bb83822 | -6.9285 | -55.0247 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88325929-ca00-3db0-a252-066f010cfa79 | -10.8319 | -50.178001 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 253e228c-6c97-39a6-8cb1-ac192006bfef | -5.8411 | -49.865101 | 2026-09-19 00:19:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a613b2ba-5c05-3080-afec-c80d3f81340b | -10.9695 | -49.740501 | 2026-09-19 00:19:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c70d221f-9172-377a-8711-9c41b2c74b2a | -19.5627 | -47.650398 | 2026-09-19 00:19:00 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 78b66d36-64f7-30fe-bcc6-a77f20779a0d | -3.7395 | -44.375 | 2026-09-19 00:19:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a5fa21a-41ac-3e12-a257-f943c054bdb3 | -13.2313 | -46.9062 | 2026-09-19 00:19:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
