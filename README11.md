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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 588979bd-20aa-3299-9858-88c2b834a4cf | -3.3209 | -54.910599 | 2025-09-06 01:05:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f430a65-1472-38ed-97bc-86fbef9a9ed6 | -18.138399 | -51.7803 | 2025-09-06 01:05:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 53bb04bd-3700-3eaf-a8a5-4b43e9ce8209 | -5.9797 | -53.599602 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d95f7e9f-2c74-325f-88f3-06b978c27f8c | -6.189 | -53.254902 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 990f88f6-6c7f-3ac6-a89f-61856d4da659 | -8.0624 | -52.344799 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87a5efbc-50c8-3644-b38e-096784f8570a | -6.1808 | -53.264198 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94934fb3-2a5f-3c4d-ac59-d58850e4a203 | -14.5839 | -48.097 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7c81afa2-14ef-38fe-895f-626ae34e445b | -10.8916 | -51.636398 | 2025-09-06 01:05:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4047d545-12f5-3fb8-8216-8b8a538cbd82 | -22.249701 | -48.747101 | 2025-09-06 01:05:00 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0bf57605-8c03-3e01-9836-51d00eecda5e | -12.5083 | -53.879002 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07a734c3-2381-390a-97fc-a111e816da58 | -22.829599 | -49.198399 | 2025-09-06 01:05:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 71f4cbea-c279-3795-96d2-af93e8bdb5fc | -15.5493 | -49.821201 | 2025-09-06 01:05:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5ff45430-8582-3e4b-a57f-702c3a2034f8 | -11.2193 | -55.024601 | 2025-09-06 01:05:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f80c8318-eb92-3b7e-a732-1364f51a13d5 | -12.497 | -53.874199 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfb9f930-3780-3abf-8abd-6193d5f3c086 | -8.5142 | -51.3204 | 2025-09-06 01:05:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5d24fc5-2ad4-388f-a99e-f221bb287f2e | -4.3772 | -48.077801 | 2025-09-06 01:05:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 305b3ef8-9a05-37d4-bb46-80b232f07498 | -22.6523 | -46.8298 | 2025-09-06 01:05:00 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40e7e917-ebcc-360d-8fd3-6d557010c5e6 | -10.1382 | -55.159901 | 2025-09-06 01:05:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0a6a545-73f0-3fb1-b05d-0893020f8859 | -10.2015 | -49.728901 | 2025-09-06 01:05:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcaa38dc-c005-34c8-a188-ae11af768b32 | -12.4774 | -53.8787 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec0ce3b6-0965-397f-9806-9389c8509758 | -14.8948 | -49.462399 | 2025-09-06 01:05:00 | METOP-C | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 40401afb-54ee-379a-ada7-1846b3467e4e | -15.7265 | -53.585602 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0aa3d54-0f70-3adb-81b5-626dd12276fd | -15.182 | -52.386501 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 393f07eb-d78a-3ae1-b028-8097161b82c1 | -16.294201 | -50.4832 | 2025-09-06 01:05:00 | METOP-C | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db86be85-fd1e-3a5f-b8ac-48f2dabf3f60 | -15.7135 | -53.573299 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62f67547-4ff3-39ad-9767-0292c8716592 | -5.9273 | -51.998001 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 383a28d7-cddc-34da-b379-66c80d32e47c | -6.1542 | -53.684898 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fec362aa-4295-3716-9695-08e8ba5f1bb9 | -8.3701 | -52.557899 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54197fc1-0e9a-31c6-a515-db4fd5ccc5bc | -10.0288 | -48.127399 | 2025-09-06 01:05:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05d289da-cf81-3d56-bffb-5889ae20906a | -11.1048 | -52.019901 | 2025-09-06 01:05:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21f48923-ca9a-35ad-a3b3-a4ac5b72baff | -12.996 | -54.8274 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c559fcd-e880-354e-a475-f637ea526a23 | -5.9291 | -52.005798 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdaa873d-1edf-3cef-b78b-aea556652f3b | -12.9503 | -54.806499 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f456157-1be8-3650-8130-d7e5cca4e308 | -15.1934 | -52.3913 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6fdac32-ea30-304e-86d8-259437ba3010 | -6.2724 | -53.437 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bcecaa0-c12e-30e0-8c85-99b680fcedaf | -12.9634 | -54.819099 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2a298e8-10b6-3884-b4a3-5957525dcce7 | -7.7279 | -50.312698 | 2025-09-06 01:05:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 748d0b40-368b-3fd4-b951-475b3d821cc4 | -13.0123 | -54.8549 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ae0d535b-841a-3af8-8c96-360bbb345e7e | -5.9834 | -44.753101 | 2025-09-06 01:05:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bda92fd-01d0-339b-a20e-1d1d19a4def0 | -12.4872 | -53.8764 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 882fc093-cf62-3c04-ae87-a79cb3bdb0bf | -5.4751 | -60.127399 | 2025-09-06 01:05:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3af88afa-01db-341c-9c93-76b772fcc021 | -11.6153 | -52.218498 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 016dc26c-8564-3a48-8468-92576b75b6a0 | -13.5454 | -48.126701 | 2025-09-06 01:05:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 859d559f-09c4-3b5b-88dd-7dbddeedfced | -11.9998 | -47.777199 | 2025-09-06 01:05:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f17b607-de11-3282-bc43-3d1f93533577 | -5.5787 | -51.919498 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 388a66df-83e3-33a1-82f2-f5b7123b8169 | -19.401899 | -44.320801 | 2025-09-06 01:05:00 | METOP-C | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 259b95f5-7625-31a8-8178-a6229e08b3b5 | -11.5439 | -47.317101 | 2025-09-06 01:05:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b0f38a0-88e3-34ad-9018-c39783dae168 | -6.3172 | -58.1842 | 2025-09-06 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67b8357d-3013-3356-9211-0ae9018efb03 | -5.9715 | -53.608799 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89bcceec-f7a2-3bdc-9f52-6e9baa313537 | -3.2439 | -50.803398 | 2025-09-06 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02d4111e-3bd0-3d11-95e2-a3214d8624ea | -14.8249 | -48.192699 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 211f2782-5463-3e24-8338-566d7a58d2db | -16.320299 | -52.9636 | 2025-09-06 01:05:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f82f11eb-209f-37e1-bf7b-e819653c80cc | -11.2014 | -55.036201 | 2025-09-06 01:05:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e35ceb93-478a-3666-97e9-a25bead30ed3 | -18.440701 | -45.9412 | 2025-09-06 01:05:00 | METOP-C | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6a2e86c3-4d2f-3b00-920b-2f098a0cf036 | -15.5398 | -48.405102 | 2025-09-06 01:05:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 129501a1-1c3e-30d9-8a26-8b588ec0a9d3 | -9.9686 | -51.664398 | 2025-09-06 01:05:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ee33f88-218e-3e94-8f5d-57ef14b713d6 | -4.5066 | -42.946602 | 2025-09-06 01:05:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a52a0780-3a0f-351e-b213-40cdea854743 | -12.4758 | -53.871601 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3fbbb6c0-2aeb-31d4-8acd-6579f76f89cc | -7.3306 | -48.492001 | 2025-09-06 01:05:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28485f12-50a0-3e9d-a1ad-35ca14d0d786 | -20.527399 | -46.469898 | 2025-09-06 01:05:00 | METOP-C | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5fb3e2b8-7f78-3668-9db5-ad3b42919e17 | -5.9763 | -43.631302 | 2025-09-06 01:05:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 643348f8-25c0-345c-b38e-38e7f5fa0010 | -16.723101 | -49.405701 | 2025-09-06 01:05:00 | METOP-C | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8c882cd6-d661-3fbc-b825-757e55c3eed0 | -22.251499 | -48.755001 | 2025-09-06 01:05:00 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 68aa75de-6393-30fb-9603-6e4077e0b800 | -13.0074 | -54.8326 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 512fc710-6c79-3dca-b009-00d0ea1a168c | -6.8182 | -52.808601 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc70735f-564f-3224-9d86-16be5cbc10b0 | -15.5891 | -52.9165 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2174aa96-62eb-3254-ba1e-154e3208258c | -6.8655 | -52.790199 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a8364c3-b236-3d43-b897-a808c7d5a021 | -6.661 | -48.409801 | 2025-09-06 01:05:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2f646859-ce56-3de4-ac40-396426ff4ba4 | -15.5512 | -49.8293 | 2025-09-06 01:05:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a2113a87-3a2a-30e9-adf3-9858447c2944 | -9.6799 | -51.095699 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 650c30c7-bf87-349e-b50e-30ccb8461d0b | -14.2602 | -52.187099 | 2025-09-06 01:05:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f5624d3-6a86-3a36-afc1-36ea40bf1923 | -3.2341 | -50.805599 | 2025-09-06 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bfa2bc5-eb68-3b4e-954c-4a5a9ebba3ca | -8.3404 | -52.519001 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b660523c-3198-311b-963d-181ee29d6767 | -15.7053 | -53.582901 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 750c0784-a415-3377-bdc9-05d4d9bbf4d2 | -10.4402 | -53.618599 | 2025-09-06 01:05:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2589cfa1-e8cb-30c1-921c-7508d264b09d | -9.8429 | -48.845299 | 2025-09-06 01:05:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81bf10f4-e1e0-3988-b8d5-50c1c0c8906f | -11.8149 | -51.433201 | 2025-09-06 01:05:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78b925df-2013-3bf0-a7f0-0acdb1165e0a | -14.9046 | -49.459999 | 2025-09-06 01:05:00 | METOP-C | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 89f1565a-a329-3923-806f-cc589d4bb249 | -15.7313 | -53.607399 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ebd32f3-e880-3c8d-9aed-d0270fedc9bc | -11.095 | -52.022202 | 2025-09-06 01:05:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6cb7de5-eead-3f10-840d-80bff9f1e1ea | -11.4677 | -55.544899 | 2025-09-06 01:05:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2905fc25-df33-3aef-97c3-e59454d8539a | -9.7251 | -51.068199 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 752420c7-b772-386e-93d7-0bf952c56cf9 | -11.861 | -51.453701 | 2025-09-06 01:05:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d3ded04-1bf0-3385-8c61-823a29a6c308 | -8.3505 | -52.5625 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb5d1e9f-a7e2-38ed-929a-c6d1d1a3dc99 | -15.8522 | -52.295399 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aee24ba4-5cce-30a0-8b15-3a069c60494b | -12.1837 | -53.901199 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4463ee3b-d624-3afd-848c-6d7e11f10cd0 | -22.243601 | -48.765598 | 2025-09-06 01:05:00 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 64de85eb-db1f-38c7-9564-6ebb7346a373 | -12.9912 | -54.805199 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9b0a84d-9230-3401-bdf0-d4131c5d6b52 | -11.6267 | -52.2234 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7354744a-2452-3193-bc6b-4080518d7b2f | -15.5712 | -52.9282 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d52c1748-0e75-3b4c-b3b5-0d3cbf8c94db | -15.0684 | -48.129902 | 2025-09-06 01:05:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 88d9c2cc-312c-3037-9ade-f9b55bb32600 | -6.8199 | -52.815899 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb57ef69-cdc5-3af3-b077-57c898244135 | -12.952 | -54.8139 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1fa79461-359e-333a-88d0-3b015f176a21 | -10.6055 | -44.331699 | 2025-09-06 01:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26f4ac1e-4de7-3f09-96f1-da1b82db4224 | -10.13 | -55.1693 | 2025-09-06 01:05:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69c46fb1-2b30-3459-9419-2ac9f382c130 | -8.0595 | -52.376499 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d14b10f1-e3a3-3ecf-becb-070151c95bf5 | -11.4792 | -55.550201 | 2025-09-06 01:05:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f819d219-58cf-3ddd-a43b-19abd1691702 | -10.6108 | -44.351799 | 2025-09-06 01:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d817df5f-d2e8-38a4-92ea-34e4d00cd419 | -6.5325 | -49.500702 | 2025-09-06 01:05:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1910367-2e65-3758-b82a-0cfba68ebe4a | -10.3139 | -51.463001 | 2025-09-06 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
