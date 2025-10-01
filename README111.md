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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f94be84-14ee-3f6a-bb5e-39921bbc9249 | -12.24583 | -47.80334 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d92a9569-8abc-3014-bb65-5c6da3aa66b1 | -12.83823 | -47.02929 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0862f025-6c4e-300c-9f48-652220f6ab1b | -12.46736 | -50.21865 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3949ff43-5814-3c8e-802b-f737fb227407 | -14.55516 | -48.24458 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3100872-5f94-351d-a1b8-a7f092953dbf | -12.82788 | -46.98044 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef7fe8d3-d85b-3c89-bf38-802db0e50361 | -9.51785 | -54.736 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b20796d0-2b0e-3989-ae5e-80d09c3596f4 | -11.76816 | -46.85302 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c2173a2-49b8-3605-adae-39e3204caf5b | -9.77466 | -46.21957 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e92ba1e-eedf-3199-9d31-a73021584a33 | -13.30254 | -48.70558 | 2025-10-01 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a797b011-a3a8-35f9-8de5-06d2d543ebf8 | -11.56661 | -50.19274 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 338c1f9c-0977-363b-930a-b305012070d0 | -15.99852 | -50.87391 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4dde62c-0d32-3f31-b85f-764d3db43a46 | -15.17465 | -49.08094 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 13697a3a-1c40-3f6e-b0d5-12c142816627 | -11.65869 | -45.31938 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b05170a7-1ece-3140-9beb-c7a229a06622 | -14.9129 | -47.82418 | 2025-10-01 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f9d0ec3b-614f-3509-a546-c49a2735c2f9 | -10.77803 | -45.36985 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2308b108-4cc0-365c-aa24-3295f1267184 | -9.53799 | -51.35762 | 2025-10-01 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4119bf61-ed1b-3b60-b43c-04509acc1450 | -10.28683 | -50.47069 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3b1adc1d-89fa-3c7d-8fe9-2942ddd573b9 | -12.85074 | -47.03086 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb39b554-5428-35b3-bb4a-c011aad9c8f1 | -12.84757 | -47.0231 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07f744ae-7492-3c33-838f-722fc538e534 | -11.15317 | -54.11793 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3bcdd60-0aa4-316a-9613-19cf67aeb1b0 | -12.86123 | -46.98566 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79a4dcc7-5ac8-3eca-8427-cb76b13e9978 | -15.27167 | -46.40808 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dd853428-4912-3499-9c2c-e2c57d377079 | -12.23447 | -47.81968 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7df19ccd-92c1-31fe-b489-183be4eedca9 | -9.854 | -44.60545 | 2025-10-01 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f01ec0f9-09dc-3f0b-8f5f-664fb668668d | -15.53201 | -45.21828 | 2025-10-01 04:51:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8bdc80e-a187-3925-9467-4d6ed25ee07b | -15.00746 | -56.03866 | 2025-10-01 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b268a9dd-1924-3c5d-886d-9b7e0aea719a | -10.47632 | -55.61898 | 2025-10-01 04:51:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50fef46d-6fbc-3689-96cd-425a78a1134d | -14.05281 | -47.97598 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3948c7de-7a9f-3dbf-b690-83c2f97956a0 | -12.37608 | -50.2015 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cfec940-48fb-3031-99cf-c2c120876c30 | -11.81246 | -44.99723 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6078152f-84df-3fc8-aebc-cb03222b7b83 | -9.93676 | -43.61654 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 275b8fef-28ed-34e8-be21-ec80f3074fa0 | -14.89272 | -48.13093 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9633dfae-483a-3cc6-bdef-c82aae28a6d7 | -14.98035 | -50.78436 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0482bde1-1596-3d51-9f7b-602573987f83 | -15.3617 | -44.15445 | 2025-10-01 04:51:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9788af8b-f200-3936-944d-f4dacf1570c4 | -10.17121 | -44.89729 | 2025-10-01 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d888561-4200-3ef5-ba8b-bcfc0514e0b5 | -12.21435 | -47.799 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21629623-9a0f-34b1-a025-c6df261beb60 | -9.89198 | -45.93723 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d45a16a-ce90-3d18-a94f-1f1ee973ff44 | -13.54372 | -47.27094 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f5d5941-3274-3a67-b07c-5ddcdbb3d48c | -14.62298 | -46.9834 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1776180-f8f6-3e81-a95c-70e567cf38d8 | -13.37744 | -47.31772 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ecaad66-8160-3279-88da-f6eac5afdee7 | -11.81717 | -44.99785 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9319fde9-f90a-3463-87d6-0a0f83cd5abf | -9.9322 | -43.65148 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1064e451-3d54-37e8-8a6b-c104014aa4eb | -8.11726 | -55.07453 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5fd211f-e4e2-3f56-a2f7-a29e6c3ea384 | -13.6676 | -48.05178 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 144e59d2-3a56-3bcc-8064-49ae379d3e81 | -13.7883 | -51.23333 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcfaf8e6-d191-392a-82c9-93564db83978 | -10.21802 | -43.04618 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ce127fea-78bc-3658-9b92-b2737d06a1b4 | -14.78539 | -45.77286 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b94de13d-2c1b-3789-bfb5-0261fbc7906e | -10.83748 | -45.40641 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ed50413-a754-355a-90a0-66d38c4e6f50 | -13.63222 | -47.64911 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5872318-e9d3-3394-8500-1dff3b9dc5d9 | -11.83526 | -44.96993 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49d2a0fb-3abf-34e5-aefb-2daf8c825b7d | -14.89349 | -48.36461 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c9e2668-e039-3391-ab60-f27700f8f538 | -9.7312 | -48.03042 | 2025-10-01 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 857bb88b-7b9b-34b8-bca0-4e7d042f8531 | -15.33953 | -47.93428 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b48de4b-3b23-3406-ba46-e2d512cacfae | -11.8273 | -44.99374 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbe8e485-8c60-39c8-8be0-22dadcb4e947 | -13.38016 | -48.08387 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 964046d5-ba50-3e7a-99c9-b08c6821c972 | -16.37682 | -47.06779 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1a94d78e-e557-3c58-a940-845cef9a3904 | -12.76984 | -46.90359 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eee3aecd-afc9-3a8f-a3a3-97c92204428e | -14.90263 | -47.21059 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a6ca38a-e329-31d8-8a91-fb411d6b4763 | -14.90656 | -47.20541 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3793215d-f9f0-3fbe-bd92-6d80582aaffb | -15.41479 | -52.72318 | 2025-10-01 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18a2d580-1f3e-3588-8608-31b294145731 | -15.76352 | -43.73925 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e7b1c2c-b9cd-3bf4-af6b-1892c58a75f0 | -8.86778 | -50.90175 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d851380b-12e8-3269-8ae7-6a8fdb0b210f | -12.86543 | -46.98612 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55341f00-3766-39a7-9e64-1451c6a68f31 | -11.86694 | -48.0235 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 853bf103-19a9-3ebf-8800-4999efc89541 | -12.28173 | -47.82553 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7b30f68-b922-3235-b06c-1f3e597105f7 | -12.87326 | -46.89834 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d39663f5-ae0e-3546-a1a7-8cec5c0e658a | -11.94859 | -47.07085 | 2025-10-01 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a28034d-df24-3b95-83d7-165db93dca69 | -9.936 | -43.62235 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c50a5f1-df78-3a56-82d5-e09bf43f39cb | -14.50351 | -48.42208 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0148a6c2-30c5-30da-bc39-0310b0a016fb | -13.23932 | -47.3258 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78b6641a-8dcf-36b7-aedc-a583fa1a899f | -10.80824 | -45.35093 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12dd021c-157a-3dc6-bbae-e0e4cb409609 | -9.43123 | -54.71786 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e8b3492-9ff7-3fc1-9029-2363a7fb7897 | -16.1894 | -50.0043 | 2025-10-01 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6a23503-0ce4-379a-b85b-a1f73e3f976e | -11.38138 | -45.06179 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26f76f12-9bf9-3aef-877c-e4d889b459f8 | -13.30697 | -48.70148 | 2025-10-01 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19cb6927-64c7-3301-bfea-4ce0e0368a10 | -11.84078 | -45.00052 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0c0d476-1235-3e2b-afe2-1552dae8a985 | -14.04885 | -47.97525 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2d73c2aa-0d01-309b-afc2-a1902467d93f | -10.04352 | -52.09582 | 2025-10-01 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0dae69e-038c-3e88-936f-efed0acdae63 | -10.75479 | -45.37152 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63515f13-ae32-384a-8889-dbaedbcc462b | -14.36261 | -47.14108 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d79b8c3c-fead-3752-8ddb-b15dfb050081 | -14.3535 | -45.92418 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d1ae0567-b981-3a83-8dec-0925ec5c4487 | -12.84962 | -46.94602 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44c343de-38d0-3c9e-90cd-8ae3db8ba1e2 | -13.62867 | -47.64494 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 189621c4-9d77-3e2f-818e-d953f0887f6c | -12.47606 | -50.25578 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 807a3ff7-f25f-3649-af3d-9a20ccc3fa29 | -11.12576 | -49.78048 | 2025-10-01 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53109361-f123-369d-9322-8d6b7d1cb6a0 | -10.03884 | -50.40628 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13171bfc-3c69-3463-a441-346201471379 | -9.48006 | -45.49788 | 2025-10-01 04:51:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fed16bdd-20b9-3462-84c7-c11842ee7e82 | -13.22983 | -48.45305 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44cc2bb0-ad33-3214-aa47-4d084a961225 | -13.29722 | -50.65739 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c659b7a-204a-38ce-9082-907cadb2cadc | -13.78496 | -48.00712 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6556ca4f-a9b6-3a1e-9c4e-a22701c80d6d | -16.38293 | -47.05491 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a39d88f7-7445-3f80-8ca2-a85a2f9b8232 | -12.79364 | -46.91776 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 963bf84e-abd0-3036-8a21-dbca6493a562 | -14.35171 | -45.93825 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 47cdc620-bc36-3e7a-8af1-306362bb9cc1 | -11.91909 | -47.9993 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48eeb243-1927-3f1f-a6d1-ed782f0f739a | -14.89873 | -48.11643 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 699c254c-92ef-3e5f-a58f-19ac7453c7e1 | -13.36225 | -48.09997 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc6827af-60fd-35d3-bcca-7370c53d6bef | -13.93482 | -48.09735 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 117b6585-659c-33f7-ad05-f2c39ba77cc0 | -13.77745 | -48.03209 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85b9436c-9401-3610-9181-fd5e68b588a9 | -12.82331 | -56.55468 | 2025-10-01 04:51:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bea16d65-2130-3cad-8182-f75fe878edc3 | -11.45501 | -44.97487 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README112.md)
