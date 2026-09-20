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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 005f5b65-b643-3f38-82be-21b753437447 | -10.31472 | -50.2038 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0a81ffe-5fc5-3717-aac7-0e4bf1f7eddb | -11.78674 | -49.82414 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed9a0e42-fee4-3fbb-bdb4-6333ed9c1ae4 | -10.86576 | -57.15458 | 2026-09-20 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bc83597-fa4f-3b7c-b464-cfccab422c54 | -9.78904 | -45.07447 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5ac5a18-cb98-3f58-bf41-dac20ff6b75f | -11.45168 | -45.37535 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 622361a9-1357-3e42-8f7c-c020987887ca | -9.8359 | -46.42916 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8e4a831-3760-39ac-914f-350c95ba4f78 | -11.03624 | -48.29934 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fb954b9-d94f-3c86-8cfa-373a31b59ad2 | -7.34898 | -44.47353 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b304c14d-1d53-3491-a4f4-16f1e0a2e5f2 | -5.85867 | -52.03133 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1fa934fb-ae77-3274-8704-85904fbfc44d | -9.6777 | -48.0841 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0da11412-ae4b-35f8-b89a-c2e2a3f108b5 | -13.02395 | -46.92239 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06d32a4a-1913-3458-9a4b-06b7bfb0bd98 | -5.97933 | -57.7799 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41fd3995-6b23-3bed-ace6-fe32ae25f824 | -13.31893 | -51.29174 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0acfaccc-2e3c-3e62-b1f7-1809a29a8efd | -5.84073 | -53.52551 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e729b459-a4ab-371b-a9fa-8ad41c9c26e5 | -12.01097 | -51.47615 | 2026-09-20 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34974105-f04c-34c5-9371-8ae9fa142696 | -11.04056 | -48.28885 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1fe7d43-de2e-3c3f-9455-267584d952e2 | -11.04356 | -47.67487 | 2026-09-20 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e1f75ab-8f93-36d3-8981-d2c472ac8c29 | -9.28837 | -48.93862 | 2026-09-20 04:40:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e149938-8489-3b25-8009-a0aff0bb43c0 | -9.17391 | -46.48173 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49a86a3e-49c0-3497-9e50-8ec198b020f3 | -9.6685 | -54.31571 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 743f27ef-cc31-322e-80fd-e307ad7ee877 | -13.73559 | -48.79053 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2acae9f-bbf4-3d28-bf19-faad1751e5aa | -9.3456 | -48.34044 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3350fa93-9359-36da-9373-edda9aff0b3f | -7.91111 | -45.25193 | 2026-09-20 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36cd7246-e23c-381b-8ebc-2db9973739a1 | -11.01015 | -48.31339 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f47a3729-464c-3b8d-aa7a-ff160d80546c | -11.03402 | -48.31352 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 481c88e8-7f10-3425-b25e-781aaa1c05bd | -11.02071 | -48.28953 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d29a20a4-39de-3a82-beaf-40b5f7b44ed4 | -10.1376 | -47.68301 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b735e57e-f800-330c-9843-8e7340fba9bb | -10.5703 | -46.54448 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| df2145d8-9ce4-3b8d-919c-d357e5054848 | -7.49376 | -46.71371 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d330f06-ff15-3e9c-beb2-2c813eff75f3 | -5.83988 | -53.49877 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c67c9510-1039-32ec-9ee1-07ec0636ea52 | -7.62745 | -45.42582 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cabe3537-933d-3692-8ae7-bce5858e5515 | -8.17372 | -54.74727 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3cf3a67-63ca-383a-849a-427739fff678 | -8.76238 | -48.65784 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c669c5d1-fc16-3746-a5cb-e48140d204a5 | -9.26387 | -48.21288 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c2d99bd-cb4c-3a1a-a757-574b229f5a2d | -5.74363 | -57.60231 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e2f802b-fb2f-39b8-b87f-62ebe56069e4 | -13.9297 | -50.08405 | 2026-09-20 04:40:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cc4e683-c5d8-3f3c-a51a-c7ffa9aa99dc | -12.75748 | -46.13873 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faddbccd-3ef3-3b12-a07c-dad7e293ad6e | -10.09917 | -48.42874 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4828f03b-f0e9-374e-9e78-6cdd0d34a746 | -10.41229 | -48.94153 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eabd56e1-cfcc-3daa-9eaa-f6ba3a945b51 | -7.19089 | -47.87673 | 2026-09-20 04:40:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 516d4b4d-fe22-3881-a7b9-f7fe432310f7 | -8.38135 | -47.19406 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 363d2aa4-ec6a-3821-ace6-5728abfab169 | -13.31985 | -51.74904 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85673aee-1474-38b8-96bf-fb6ffba6e6ce | -11.7786 | -54.53358 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a63a5b10-9970-3ea4-bf1e-2fb5fe2baa5f | -8.87105 | -45.94786 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a1cf010-0821-380c-9395-083e41a2aedc | -5.844 | -53.50647 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1379cbc1-1c20-3823-8267-c8706bcf1516 | -7.7584 | -44.87794 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc7943e3-3239-3242-b7cf-d4d64699a20a | -6.09793 | -57.68239 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fbf18e84-122c-3fd1-b00e-b3dc40038d62 | -6.99409 | -49.80415 | 2026-09-20 04:40:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0c8527d-2905-35b7-9779-a1b176482f2a | -7.55554 | -61.33139 | 2026-09-20 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c3ba523-ce3c-30af-8cd8-e39ff7eac939 | -11.45909 | -45.70268 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e72859f-7124-33c0-a46b-8be8765fb942 | -12.15605 | -47.02621 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9478a005-3b0c-3b90-b976-2efc3ba76e94 | -11.05118 | -47.96146 | 2026-09-20 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbfab8af-5ffe-3b39-8cc1-30ea7905d5cd | -10.40788 | -48.92648 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b28974a-e36b-36f1-b4f2-f338b2bfbbbc | -9.26774 | -48.2099 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a836241-5e5c-3228-8c45-2c90889de25e | -8.38005 | -45.63622 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acfee684-b435-349a-8593-097fc9e5e45c | -10.31631 | -50.21517 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19e792e7-a30e-38d5-bba3-b97d176e8eec | -13.62796 | -46.96471 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91cba17c-cc20-3a1c-b056-bfa858b1aa37 | -11.27362 | -54.12932 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93077ef9-3fb0-3b3d-9f9c-2d788bff549f | -5.8403 | -53.52234 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1be0e070-6360-3884-abf6-9abe1b8955ab | -11.48231 | -47.75731 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 585364ec-014f-335a-85ed-6cf519312f0c | -8.46212 | -57.62635 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b13d797-1860-3476-8e63-9560809cf050 | -11.74841 | -54.56178 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 600a0d61-a95d-3b1e-8b90-7c6d5e4f7da9 | -10.88852 | -53.98583 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ff109ae-51bf-3f23-9d80-d58e9da8dac1 | -10.87114 | -54.08443 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b5b6329-b5d4-36b3-8816-0b37bedf7d04 | -9.28375 | -48.19453 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66b70e77-6116-3a0d-9837-ca9133ed5ac1 | -10.2634 | -45.48571 | 2026-09-20 04:40:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5948ec6b-f4f7-3f6a-8b77-6a665c2006be | -9.02021 | -48.74525 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6cade25-59cb-38cb-934e-31e407693d29 | -7.76522 | -46.69917 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78250c29-29c6-3f42-ad13-67c8efc40446 | -10.47309 | -46.2989 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e1de3ae-f202-35e2-a0b4-a6f34d4e60d3 | -11.03581 | -54.16545 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ff65c97-4762-3cb2-aa1b-2775bb9bcabc | -11.87811 | -47.66016 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a9a4336-2d9a-3509-ba9f-7bdab1b3e7b4 | -11.03304 | -54.15756 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90b06163-8482-3e20-a31a-d1d892258a01 | -11.2247 | -54.06873 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96a0aeb9-487c-3972-840f-6eeb4579ca72 | -11.48571 | -47.78034 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ecb7310-5a5f-3614-ab87-563d7ac125de | -8.29778 | -50.82094 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d0644c22-b9fc-312e-9d2e-6457acd680f6 | -9.82082 | -46.43455 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9584318-b599-3bcc-90f4-b67f809f50a0 | -9.92647 | -48.38299 | 2026-09-20 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d25c13b1-b7ac-3409-9965-eb164d0d9ff1 | -7.55036 | -45.43606 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e24260cf-962a-3584-896b-3f2cb3b02eea | -13.95076 | -47.86017 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8e6809b-4c5d-36b3-bf80-6eccd3dc3914 | -12.53105 | -50.03417 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60d8b9bd-49aa-3537-9a05-46ce0b1c3d81 | -11.86886 | -48.9858 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2622bffa-61c6-365f-be91-6546487e7135 | -11.48409 | -51.48028 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae6d6ed-569e-3b05-aa7f-d5454c97cb46 | -10.30983 | -50.25487 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d39b670-67c4-335e-83a3-7005da7f4cfd | -10.49046 | -48.09698 | 2026-09-20 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73bd7284-25f4-3aa1-8345-c1462d2f41f4 | -10.27558 | -50.26431 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 60cb5dcc-cb5f-3222-99b1-1780a98e8c5a | -10.38431 | -48.31882 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2e882b1-4705-3520-aa18-707e4b1f07e4 | -12.40249 | -54.4082 | 2026-09-20 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9407220a-ca15-3601-99a4-25dd51949de1 | -8.0515 | -46.24961 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5ad2dd03-3e82-3735-9bac-277dbbe2c2a1 | -12.29047 | -47.11385 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 595562b8-979b-3400-b894-345bf4ad6e73 | -6.0902 | -56.47188 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58c657f3-3afc-3aaa-a45d-b63f7bcc7171 | -11.21187 | -54.07179 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ad474e5d-f215-3fea-a040-f7e158185cdf | -9.62538 | -45.38187 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a426938-2655-37f2-be8b-c2ae1fda45b3 | -9.83644 | -46.40177 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 815842d7-b131-3806-ab01-8fe4d51ae0cf | -11.865 | -48.98878 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ccee7e6a-133b-3d47-8b50-90de6ac64f1f | -10.31101 | -50.24765 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25350d03-90b1-3bdb-8bb3-a89e8b45665e | -10.77641 | -46.34738 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7440c90-f258-3721-9750-edbbbbfad6f8 | -10.78476 | -50.86749 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a86d4df-8b68-3da2-82c6-e188bd548e6b | -8.37112 | -45.64708 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b25ba818-8b86-3e4c-b7c4-ba79b4b3e96d | -9.18468 | -60.77429 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0e664e4-8d8e-35bd-a7c2-6541d70899f7 | -7.39726 | -47.77423 | 2026-09-20 04:40:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README77.md)
