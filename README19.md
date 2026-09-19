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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fded0ff-f495-3f84-8979-56ea90c2f7c4 | -10.8502 | -50.192699 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcbb8512-be78-3051-b9c2-3e5bbfa7693c | -12.4044 | -46.897499 | 2026-09-19 00:41:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76ac78ae-b697-3884-a2e2-59ae618b4c35 | -3.5588 | -50.2915 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50148b7e-05c7-3268-a357-91d60d0d6a17 | -5.3212 | -48.9832 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce2c0bf-3063-354a-8ba1-04f9ea34fbf3 | -12.349 | -50.704102 | 2026-09-19 00:41:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7147142f-7c69-3da0-ab67-fe4ae5360e47 | -4.3617 | -47.7799 | 2026-09-19 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04f28caa-0518-3b53-bca0-322e48f7f956 | -4.2774 | -46.535 | 2026-09-19 00:41:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd692dfa-9bb2-3069-a5b9-855d7dbad8e1 | -5.1945 | -49.328899 | 2026-09-19 00:41:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7a2691b-874d-3675-88c2-3997de98c48a | -2.8278 | -50.476501 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93f150af-adf5-3511-b10a-9470648cf172 | -8.4476 | -45.702801 | 2026-09-19 00:41:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c6d31fd-e45c-3150-bbdd-9caad30a2e81 | -10.0496 | -44.881302 | 2026-09-19 00:41:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b75a07b-6d0a-3de5-8a5a-24aeef47caf9 | -6.9847 | -49.761902 | 2026-09-19 00:41:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95bfbc7c-92e2-3cf8-b45d-715a9195d0f2 | -1.1744 | -49.298302 | 2026-09-19 00:41:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bc11098-012b-39e6-875d-fa20eeefed61 | -6.6572 | -50.908298 | 2026-09-19 00:41:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c793ecbe-dc09-37d7-8589-75e527e2adb5 | -14.1791 | -47.853001 | 2026-09-19 00:41:00 | METOP-C | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c866a8a4-9f7c-3385-9be0-3a02ccf76d6c | -11.0561 | -49.776199 | 2026-09-19 00:41:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 938aef86-4727-3543-a296-8e03725b07fc | -7.557 | -49.604301 | 2026-09-19 00:41:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84147bf3-e57d-3cf8-bec8-11c3c229fdd4 | -10.3632 | -48.890099 | 2026-09-19 00:41:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e162ce4-f1ce-3ce1-88dc-1a84f2e2b837 | -7.8149 | -44.9543 | 2026-09-19 00:41:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 276b6c85-9bcf-3b76-a250-1377acf41d05 | -5.9121 | -52.125401 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc45b96a-0581-300e-a1be-9d039bf97ca6 | -2.6592 | -49.474499 | 2026-09-19 00:41:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cdba227-9bed-342d-b126-1c57bd2c9e0e | -10.9664 | -49.742901 | 2026-09-19 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a151b2c6-3301-3e83-9b4b-587671a19d72 | -11.0611 | -49.752201 | 2026-09-19 00:41:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e69f95b-4ecb-349e-bf4b-faa8f86d3303 | -9.7618 | -45.060398 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 013f89eb-494c-32a2-8b5b-d795906a2565 | -6.9904 | -42.194901 | 2026-09-19 00:41:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 84462141-f4df-3663-b2ae-0970b3ab914b | -11.9732 | -52.445099 | 2026-09-19 00:41:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8a11d16-76f2-3d44-8626-3c28d67ac782 | -10.8735 | -54.065399 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8d64328-79bb-384d-98b3-c08234051625 | -4.3825 | -55.252899 | 2026-09-19 00:41:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4473e5ed-79b2-3ed2-973f-01a90dfc2e24 | -5.229 | -49.2995 | 2026-09-19 00:41:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa0882a3-dc64-3ec9-a4b2-b0c2026154e4 | -5.2541 | -49.408901 | 2026-09-19 00:41:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d10f873b-5531-3202-a60b-6906ba81fc2c | -11.0997 | -49.463501 | 2026-09-19 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 787f3dac-59e5-3afe-b653-ad0525c0851a | -5.8435 | -49.866001 | 2026-09-19 00:41:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0576069-1036-32e7-b973-c1781345db9e | -9.9279 | -53.985699 | 2026-09-19 00:41:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9eec60b4-eebc-3900-8293-c241e885c020 | -9.0024 | -44.9095 | 2026-09-19 00:41:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c5fedf1d-be7f-3304-8185-611df7aef4c2 | -13.6525 | -46.9394 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b172c6d9-9ded-370e-bec4-2dae9f6966a4 | -2.818 | -50.478699 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad420302-ef73-3deb-9b4a-e2fdff78ce4b | -12.5959 | -49.111 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93246c28-8cf1-37f5-98af-a40f75e3fbcd | -9.7995 | -46.090302 | 2026-09-19 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61d74727-249d-324c-9847-abf2683c671a | -4.4851 | -55.4841 | 2026-09-19 00:41:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0eacaf6-0f8f-35a0-83b0-cad51a6a51b4 | -3.239 | -46.946201 | 2026-09-19 00:41:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28ed8c6f-98fa-3cb9-9d25-488840e54d37 | -1.2262 | -55.723999 | 2026-09-19 00:41:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64f1e685-1561-3896-9f29-dc7272dd91fe | -12.395 | -45.049301 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 987dc153-7672-3db4-a6ff-3e68db898345 | -17.3256 | -46.626701 | 2026-09-19 00:41:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2a569275-82ee-36d2-a23e-06c7f741b50f | -11.1013 | -49.470699 | 2026-09-19 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4bcf974-70d1-3b67-93c1-b0cdf1e884e8 | -13.6182 | -46.925201 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4cf7ef9e-0d92-3247-877d-246b1ed2c383 | -1.5878 | -55.553101 | 2026-09-19 00:41:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5577bf24-ad16-349b-88a8-86a8300f8546 | -11.2995 | -47.2537 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a0f2c00-6605-3d2c-9aac-129973b4c38b | -3.0215 | -51.186798 | 2026-09-19 00:41:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9eced7a-2557-33bf-9b9b-fb6f81570f0f | -10.9778 | -49.748001 | 2026-09-19 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e2b85fd-e477-3ae8-b9d7-41c14dabfee1 | -9.6967 | -54.823898 | 2026-09-19 00:41:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 859eef36-853e-3e13-9e42-b5da520468d3 | -5.8377 | -47.780701 | 2026-09-19 00:41:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75e2fb3a-c61b-307f-a5ac-04a6e190284d | -9.238 | -46.2066 | 2026-09-19 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf3f3030-77fc-359b-82ff-551712e63649 | -5.2966 | -50.089699 | 2026-09-19 00:41:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6985249c-9e24-3178-81ff-91ea1c625f61 | -8.3674 | -47.251701 | 2026-09-19 00:41:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99e0b2c7-dc9e-31d7-ac3a-47d8a5ec939e | -12.9935 | -46.990501 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6fbb91d-e401-3e6d-88f3-e8adfef57a4b | -7.364 | -44.6236 | 2026-09-19 00:41:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e994959d-6797-3a3f-88ad-89e51af3c511 | -9.0504 | -48.737499 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| adb9907f-3f9e-3967-98f7-ad8bbac177aa | -11.3513 | -44.147202 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b637e0e7-b0eb-3360-adc2-147e268a9a1f | -12.1613 | -47.007099 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 284f8b07-763f-3fe4-b5da-c8d0e8d7cef3 | -13.628 | -46.922798 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1d1e91f-a9f6-30ab-b1de-ab0fbace7fc8 | -5.5202 | -43.7766 | 2026-09-19 00:41:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09c411e5-5ffc-39f4-99f0-93587606b75c | -5.3183 | -49.149899 | 2026-09-19 00:41:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfb18633-5029-3c52-8c5a-cf842b2e03d8 | -2.2907 | -47.880299 | 2026-09-19 00:41:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a02f88b-30c4-3b6f-a598-99d0bfd9666b | -11.2802 | -43.5144 | 2026-09-19 00:41:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf6a574f-d17a-3c9e-9bcc-909a987cdd63 | -3.6387 | -49.965401 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4924f477-087a-3191-b6f5-92225dd31cbb | -3.3614 | -50.464901 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b586b801-ae95-3b79-9e28-84b9985926ab | -5.882 | -53.555901 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b21bed7b-bc45-3d57-9234-28cafa7308f1 | -6.5785 | -44.1464 | 2026-09-19 00:41:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2305e6bf-2fdf-3e7a-8047-b00fa7021489 | -3.7214 | -54.636398 | 2026-09-19 00:41:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12ea8e53-4a91-37d8-a57e-4788d0e4304b | -2.0344 | -48.778801 | 2026-09-19 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc4e6a8e-3f31-3391-a0d4-2a0287c33e21 | -7.8655 | -46.430698 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa0e6129-6e2d-3de7-afd2-6ef6ce20c82b | -13.0098 | -46.926899 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6e00c6f-977e-36bd-8375-319eab744754 | -3.8177 | -50.746201 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11c47e28-e2f6-3772-9862-3730c98c7a42 | -5.9928 | -51.797401 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1a534c7-53ea-366f-9a91-c0e395b57067 | -12.9999 | -46.974098 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c104da4-6ce8-34eb-8063-6cb58bacb83f | -4.1439 | -48.219501 | 2026-09-19 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e48fcd0-690b-3d89-a072-5143fd171fbd | -3.5202 | -50.798 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b55d6af2-15d7-35a5-8520-75febd18cb40 | -5.8974 | -53.532902 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc8f65f-03e3-3dd3-9e34-c13dd460112c | -10.8256 | -50.174801 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0683eac-196f-3d60-92d4-fb348d245ab4 | -12.4145 | -45.044498 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 32ee7a2c-6f4c-3bb5-a59d-95fd978dccbf | -7.6719 | -46.134602 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7291c27f-9464-3e50-8404-f3ef5c50f536 | -11.3739 | -44.1124 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57e5aa8b-2c25-3d33-afe1-05cfde406515 | -12.1482 | -46.995201 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4428a6c1-0885-3abe-b46f-703046ea2c3c | -12.5845 | -49.105999 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97aa8c25-7403-3734-902e-9b69f8a67603 | -12.5763 | -49.115398 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6fcc57c-d45d-3260-adbc-e66a947a2796 | -11.9753 | -52.454899 | 2026-09-19 00:41:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b5378b9-09ea-3e45-ac95-bcb682aed04a | -11.2978 | -47.246601 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17e584f8-33df-3b81-a266-40f0c55f2645 | -10.6051 | -50.247299 | 2026-09-19 00:41:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a2d6c60-a138-331c-88a2-32c25ab6e8e1 | -7.018 | -44.644199 | 2026-09-19 00:41:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45abae37-5d36-3039-964c-1f653db33e0c | -12.8476 | -44.3904 | 2026-09-19 00:41:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 899a73a0-a27e-392f-aa5d-a051414f74f3 | -2.8133 | -50.458199 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35090c4f-0f3e-3a1d-9bae-b6cf58fc50a3 | -11.9155 | -50.1292 | 2026-09-19 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9edc805-174d-3b7a-ae80-d97ce6813847 | -15.0774 | -49.6021 | 2026-09-19 00:41:00 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c28df5ae-3c68-3f55-b33d-791a371101b0 | -14.677 | -46.681702 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 331819d0-7c74-3413-bbd8-6cd6527b70a6 | -11.0791 | -48.2742 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7579b2f8-27c2-317b-8a04-440d668cf5ea | -7.8692 | -46.446201 | 2026-09-19 00:41:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41c32ef6-3ac7-35ca-825f-2d2e1ffa6537 | -13.0624 | -47.382198 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d541c9ef-20b9-3659-aca1-5e8085d35820 | -8.4773 | -44.529598 | 2026-09-19 00:41:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0b263234-bc90-31cc-804c-a55258e55677 | -13.6834 | -48.5853 | 2026-09-19 00:41:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bfb37fd2-7632-3e34-8438-3446a40fd07c | -8.3688 | -47.2132 | 2026-09-19 00:41:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README20.md)
