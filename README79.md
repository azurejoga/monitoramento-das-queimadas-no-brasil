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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83518515-77c1-30d7-902c-4492da6e667e | -13.9919 | -54.0189 | 2026-08-29 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 60c1f1d1-69e5-3bd3-b0f0-2241f26b8ed5 | -8.9428 | -63.2797 | 2026-08-29 14:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 148.1 |
| e55d73a4-0241-3ed3-92e5-178737036daf | -6.7885 | -55.6436 | 2026-08-29 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c6d84c77-370d-3ad3-8bd9-b0845f2fd6d9 | -14.2024 | -52.8643 | 2026-08-29 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b24927a4-a307-360b-88bc-05b70cc45dfd | -8.9613 | -63.279 | 2026-08-29 14:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 44433b1d-7982-307e-8a7d-db8df416cd3c | -6.77 | -55.6445 | 2026-08-29 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 2c9a4f64-b06f-39d9-951e-b06754a4424e | -11.5039 | -46.9471 | 2026-08-29 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| aff13fdd-fb4c-3301-8ec7-e639d7634938 | -6.6315 | -43.7533 | 2026-08-29 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 320.1 |
| c171203d-7fb9-3f2b-95e5-2c186f77dcbd | -9.6022 | -55.128 | 2026-08-29 14:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d49b37d0-47a0-33d3-bb98-7946e4908331 | -13.3254 | -46.9333 | 2026-08-29 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| e136b49a-cd89-3f14-9355-49db1f8e827e | -8.0113 | -48.0161 | 2026-08-29 14:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 56c8d1d1-8637-3d86-861c-0c240670bb8b | -10.4794 | -64.5012 | 2026-08-29 14:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 22c0d486-9459-32ab-a0d8-bbf8edaa7b6e | -14.1835 | -52.8456 | 2026-08-29 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 8dc268c8-20e2-3f52-884e-1526d868b2cb | -12.2093 | -50.5386 | 2026-08-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c2f42c11-33a5-339e-abb1-31360c31b9fa | -14.4138 | -51.7559 | 2026-08-29 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 9d6757f7-3ee0-3dff-b1e1-6f192206f60d | -7.5478 | -61.3056 | 2026-08-29 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 97.5 |
| f9ec6afd-ee31-3921-8ce0-f15c73e3f6ab | -9.971 | -53.9214 | 2026-08-29 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 200.8 |
| 7f10049f-fc04-358f-8e9d-f20f274e52da | -8.5968 | -54.7957 | 2026-08-29 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 01f7c74c-6c6d-3675-8fbd-0a7e5b05ef9e | -11.2317 | -53.9958 | 2026-08-29 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 3c2638ee-7ccf-3df2-a68a-5337458e33ed | -7.9169 | -61.3671 | 2026-08-29 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c71f3765-759f-338f-a714-51b9096f0e20 | -11.2489 | -45.0732 | 2026-08-29 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 9559445a-5b4f-3031-945d-47450fc6fc07 | -5.8895 | -57.7513 | 2026-08-29 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 93b3b851-d2a0-3c65-94cb-967376b4548e | -12.9221 | -45.8582 | 2026-08-29 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8a7bc4cf-92ea-33c0-8b31-c693f352dc33 | -8.6154 | -54.7945 | 2026-08-29 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 14a2f724-d1e2-3843-bf57-042fc85e9ada | -6.9303 | -45.6931 | 2026-08-29 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| e2a4eb8c-cebb-3340-b174-ea49b80f2d19 | -15.3655 | -52.6703 | 2026-08-29 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a5c70f96-e33b-38ce-baa2-b5662f0e7070 | -7.3479 | -55.1544 | 2026-08-29 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| cad4b519-b661-3806-b6af-f2e2ea3e158c | -11.1726 | -51.2728 | 2026-08-29 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e20a198a-6f72-3bcb-8092-d45365157899 | -9.9708 | -53.9419 | 2026-08-29 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 183.4 |
| e15544c9-510c-3f2c-803d-5e011d3575c2 | -7.5662 | -61.3049 | 2026-08-29 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 211.7 |
| f918269c-7c4d-3d77-acc6-1db13e14b741 | -15.3849 | -52.6677 | 2026-08-29 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 11321e7b-39a7-38fb-86a2-385829a9d7af | -5.8894 | -57.7708 | 2026-08-29 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 38630bae-f98c-3057-ade0-1e685056362c | -14.4142 | -51.7345 | 2026-08-29 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 28a1bc93-52a4-3323-abdd-9003892ed8ab | -9.2094 | -51.5444 | 2026-08-29 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5bf8c468-a903-3f78-b2b6-6e08123a20d4 | -14.4335 | -51.7319 | 2026-08-29 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a9d9fc75-08ea-30aa-88af-59ba0d249b7d | -5.1426 | -49.9324 | 2026-08-29 14:00:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| cecd5999-c46a-30e2-8578-b761dd47012d | -9.621 | -55.1266 | 2026-08-29 14:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f4e778e0-5d40-352c-b71f-a48b9d0675ba | -10.8235 | -50.5026 | 2026-08-29 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 9f94551b-6d65-3de7-9f05-9a56486daec8 | -11.1639 | -45.5897 | 2026-08-29 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 5263f7c1-81a0-3590-b566-1d4f65196a91 | -8.116 | -45.4715 | 2026-08-29 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 17c91cf8-d955-3ef8-a2aa-a3affdc1c2b4 | -14.2027 | -52.8432 | 2026-08-29 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| f4f4010e-0aa7-3287-916a-f5d4920e7244 | -6.6317 | -43.73 | 2026-08-29 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 491.5 |
| ab132a04-f5c1-32fd-9cc0-5e90200f55f0 | -10.8804 | -50.4965 | 2026-08-29 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 33935d65-865e-3667-860d-cab1e9d14d77 | -8.9613 | -63.279 | 2026-08-29 14:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 150.6 |
| d66db6ef-b66c-3afb-a82d-26291ce63d10 | -13.3061 | -46.9363 | 2026-08-29 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 12b9e1df-f35c-3d11-a537-30c7318b9ce4 | -6.6317 | -43.73 | 2026-08-29 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 449.8 |
| c2106ac7-9cf1-3481-8489-feb620632bfb | -9.9708 | -53.9419 | 2026-08-29 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 131.3 |
| ce85f067-5b8b-3a55-ab5c-ccf4f9635b34 | -10.8232 | -50.5239 | 2026-08-29 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 57a71395-3e87-3f77-ba0d-fbbb316788a4 | -11.5039 | -46.9471 | 2026-08-29 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| d4d5f60c-ffb2-3b00-8099-8a0340c633d0 | -11.1913 | -51.292 | 2026-08-29 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 8d0a2233-7250-3b9e-8573-a67a0e314d20 | -11.0244 | -49.6872 | 2026-08-29 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| aa8a0cb1-3c78-39b2-822d-214db7c71c39 | -14.2024 | -52.8643 | 2026-08-29 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 2b978be9-b168-36b7-91b8-6650c30a387a | -14.1642 | -52.848 | 2026-08-29 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 205e528c-3b92-31df-9f90-f9aff6122bbb | -11.7028 | -47.6129 | 2026-08-29 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d6c4837f-7f0d-3100-8002-b33dacd0d32d | -11.0057 | -49.6677 | 2026-08-29 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 69eb2e18-f283-371d-8a9e-291817e929a0 | -13.4128 | -51.7997 | 2026-08-29 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| e3571ced-bc96-32ab-9194-ee9d430b25a4 | -11.0443 | -57.2222 | 2026-08-29 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 60182e67-c653-3cf3-b378-bbcb5ef86f5f | -10.8235 | -50.5026 | 2026-08-29 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| d1eb968a-8916-355f-978e-83ba71dcdfac | -7.5662 | -61.3049 | 2026-08-29 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 198.7 |
| 6d3537d2-3a53-385e-9ad2-df628ee02ca4 | -11.7024 | -47.6352 | 2026-08-29 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1c73c28b-a8ee-3860-a6ce-58de7cefe61a | -8.5968 | -54.7957 | 2026-08-29 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 328a28b1-d8ed-3553-9b84-9f2f1cfecf3b | -8.0113 | -48.0161 | 2026-08-29 14:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| cdccf396-fa4f-32a9-bc40-87ac2bb29870 | -12.2284 | -50.5363 | 2026-08-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8842ba6d-3630-30d8-b6c3-43ba1c4e2d0e | -10.7791 | -53.9752 | 2026-08-29 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| a7322137-ceb4-364c-8d36-0e1744e8b7a0 | -6.6315 | -43.7533 | 2026-08-29 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 301.7 |
| 7db788f6-2eba-3e0c-92c4-841374bb0a17 | -10.798 | -53.9736 | 2026-08-29 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| adaa753e-63b1-3c39-ac28-88a116919920 | -10.8425 | -50.5005 | 2026-08-29 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 0c2a1042-2e29-3772-b4fe-a44fb2492a7f | -11.2317 | -53.9958 | 2026-08-29 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 79c90a8f-b974-37d6-b4d8-91f27d80d06a | -12.9221 | -45.8582 | 2026-08-29 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 6073c6c1-0886-3439-a37a-7c9ee998bdcf | -15.3849 | -52.6677 | 2026-08-29 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 76fa86e4-b970-3a20-92fb-f0dd7a4dbf96 | -13.3254 | -46.9333 | 2026-08-29 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 7c56a7d2-946e-3b2b-a9b9-26015da259dd | -12.2093 | -50.5386 | 2026-08-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 923b3b76-2223-3431-9666-aefe3874d2bf | -9.971 | -53.9214 | 2026-08-29 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 563059f9-a96a-3ac7-bd2c-2455e56bef93 | -9.8739 | -60.2955 | 2026-08-29 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| bfb6d3d9-9f99-37c3-a7f4-44b7f6d14f98 | 2.2375 | -50.7515 | 2026-08-29 14:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 87.7 |
| e401c163-5b1a-3023-bc25-816e4df6b667 | -6.8571 | -59.4179 | 2026-08-29 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 7ab932bb-a9e1-34e0-8c46-24363546d999 | -11.1916 | -51.2708 | 2026-08-29 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 163e7e5d-e1fd-3acd-bd95-358abd8af945 | -10.8804 | -50.4965 | 2026-08-29 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ee7f3814-eb60-3129-89fe-3fdb268ef3f9 | -6.7885 | -55.6436 | 2026-08-29 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| c4e59dbc-fd0f-301d-a74e-81eff054c39d | -14.4193 | -52.5625 | 2026-08-29 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e0a119ae-47ba-3a69-a11d-d45a77003174 | -6.1657 | -57.7793 | 2026-08-29 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 5783961b-f435-39fc-ac79-35d6d442cfa4 | -13.9919 | -54.0189 | 2026-08-29 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 0eed1c60-dda2-3681-92f2-445504826d8e | -14.2027 | -52.8432 | 2026-08-29 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 30f926de-4b05-3df7-a84b-4f6d562e1737 | -7.9838 | -45.5072 | 2026-08-29 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 883fc17a-773c-386b-af51-511054f69774 | -5.8895 | -57.7513 | 2026-08-29 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7d666c8f-f2d2-3831-aa97-fb9d9e224f70 | -6.77 | -55.6445 | 2026-08-29 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 1a2b5824-4f28-3e43-a057-9758929e2abd | -10.4794 | -64.5012 | 2026-08-29 14:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b4c40dba-3b54-37f3-9877-5ac54360353a | -14.4138 | -51.7559 | 2026-08-29 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 28bdeec4-38fd-3302-8810-31c5d48be892 | -11.1726 | -51.2728 | 2026-08-29 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| c84bbcb5-7064-3424-941e-70bf403032a2 | -11.1723 | -51.294 | 2026-08-29 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 147.4 |
| ccf27eca-d0fc-386d-b589-6e4369cfbfb0 | -14.1835 | -52.8456 | 2026-08-29 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 152.1 |
| bdf27b3a-b1b5-3807-a693-e4e6ade446a4 | -13.325 | -46.956 | 2026-08-29 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d5e3a548-97bc-38f3-9e3d-46fea56b7421 | -8.9428 | -63.2797 | 2026-08-29 14:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 70d5cd1e-2336-3087-8114-6e43c9ae15c3 | -17.2938 | -46.0291 | 2026-08-29 14:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 57763473-fadb-3be5-a8f8-ac3731ffac09 | -11.1639 | -45.5897 | 2026-08-29 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 2a2fec9e-d7e2-39d5-9289-1e61aa6f78e5 | -7.5478 | -61.3056 | 2026-08-29 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| c71ada04-921a-3833-b874-236617aef6e5 | -14.4142 | -51.7345 | 2026-08-29 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 154.2 |
| db38eb41-d6ef-302d-b937-74ba5bb25f7c | -6.8202 | -59.4194 | 2026-08-29 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 89dee129-5b80-3002-8e37-a3f130fd592f | -11.0244 | -49.6872 | 2026-08-29 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 86b3ef01-8079-3dd7-9c54-14a1e0086828 | -11.6975 | -54.5467 | 2026-08-29 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |


[Clique aqui para ver as próximas entradas](README80.md)
