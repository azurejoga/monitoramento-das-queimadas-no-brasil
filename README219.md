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

## Dados Diários - Página 219

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11a947db-7457-3eca-ad85-de0537a008ba | -6.9334 | -43.67399 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 9f17fd96-f7f0-33e3-aadb-455cc808ccd0 | -7.19302 | -52.62344 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a7d8966-a64b-374b-9412-939a5c6daadc | -6.36609 | -42.91547 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0eeadf53-e425-3503-a4b7-3cb76a0d51d1 | -8.95699 | -47.55261 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0aa57b0a-1206-393d-9f18-6c0f90893f3a | -9.44989 | -44.62378 | 2026-10-07 16:37:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 42d92314-90b0-366b-9aae-d0861ae2d173 | -6.33321 | -38.8623 | 2026-10-07 16:37:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 4293af8a-1e82-37bd-a359-36799ccaf16e | -6.04706 | -42.59425 | 2026-10-07 16:37:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| d4e391e9-2c1b-3a68-afda-b7596bb75e33 | -6.70393 | -44.98465 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d60b8c8b-fc79-3a3c-a8b0-2584122c7db4 | -10.88409 | -46.6844 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| d396b534-2ee9-33a0-87b2-d6ed6042d574 | -8.60777 | -47.15628 | 2026-10-07 16:37:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bd6c5be5-6786-31f7-8e8f-8484b328595d | -7.53176 | -45.87445 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b53d1666-6d68-35cc-9b64-179dccd834dc | -6.71339 | -44.04402 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2fa08883-04ed-3301-bb1f-3ae1ab30eb48 | -6.31609 | -43.48707 | 2026-10-07 16:37:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a67aac32-3a1a-3a37-8dbb-c8e41cefeb5c | -9.88917 | -44.83465 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 9b2031ec-243b-34f9-9a1b-0c2798ee72c6 | -5.60943 | -45.58776 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eb597483-ad33-3810-ae08-28a6479d9c8e | -7.75581 | -54.95155 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| fad7f210-713e-3f98-958f-7451c8009715 | -6.84946 | -41.76908 | 2026-10-07 16:37:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 8bada54e-7c5b-352a-ad84-95ed32cb808d | -3.77125 | -41.71718 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 46.7 |
| dc214ce8-36c2-3418-9487-6016da97dadb | -9.57906 | -46.20816 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ee609a5-609b-3bac-baad-c6c7cbda5704 | -4.26837 | -49.98724 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9a798f75-d923-3d67-964c-910eebb04962 | -5.24358 | -50.91288 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 21fe6956-b4ee-3881-bc5b-bfa148a0a6fd | -15.92344 | -40.0225 | 2026-10-07 16:37:00 | NPP-375 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 06d7567d-3bed-386e-8f89-c6f2afb54860 | -8.74503 | -47.87533 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 402d53f6-98e7-3b71-9b99-5fef9a901ee1 | -3.76792 | -41.78834 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 036a9698-c522-3528-a110-04c5f0eb19e5 | -7.76627 | -43.79334 | 2026-10-07 16:37:00 | NPP-375 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 79aa1f4a-e863-34da-8a4b-776f441d9be3 | -3.36211 | -41.91181 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c03d22b7-9b92-368d-9c30-a5c0f71b38e1 | -6.31384 | -53.31259 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 47a6006c-b5fa-3bdd-b5a9-6ce6a189096d | -9.83344 | -46.24758 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 396417a2-3bc1-31f8-9a01-0d734f341770 | -7.03105 | -50.68619 | 2026-10-07 16:37:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9425dbfe-4a61-3b54-9ff5-93439f1690c3 | -4.80335 | -42.74499 | 2026-10-07 16:37:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d0e61454-7cca-37ff-aed7-44deedc4073f | -15.09156 | -41.44046 | 2026-10-07 16:37:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 78fac19e-6363-3a9a-918b-f556229bd94b | -5.71272 | -37.70943 | 2026-10-07 16:37:00 | NPP-375 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a743c55b-2ec0-3789-ae14-6a267f696d1b | -3.73427 | -44.97183 | 2026-10-07 16:37:00 | NPP-375 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 9db086cc-8b80-33bd-b122-18d0ebdda38a | -6.93889 | -45.26899 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5026f434-aa33-3b51-8e21-d9c35abcc3c8 | -7.2085 | -55.09393 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| ff338568-1149-3b06-9986-e9ded4ff8070 | -3.38391 | -43.3803 | 2026-10-07 16:37:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3c924a6c-53b3-3454-a021-8ecfae153299 | -7.27573 | -46.153 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ca929376-2366-3d82-a286-c4e42ca9dd73 | -4.10094 | -42.62445 | 2026-10-07 16:37:00 | NPP-375 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 97f47bc7-96b7-30ef-8e73-220b795b83dc | -4.83279 | -40.72431 | 2026-10-07 16:37:00 | NPP-375 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 3746c9ad-27eb-38cf-aa19-a0c83b837b2e | -10.34247 | -46.24337 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 168beb72-2f58-3c4a-8d72-31b1163c5c05 | -7.39422 | -46.22292 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 69276950-fe82-3a42-9712-7d6155566883 | -7.07893 | -52.68227 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 29b8151b-5fde-34aa-ae5f-b46c788574fd | -4.27295 | -39.54784 | 2026-10-07 16:37:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e66e3b4e-4344-3d92-9d20-2cd3afadf5d9 | -5.71128 | -41.68875 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| fbdf0dbf-80f1-3f44-b635-4800e2961ccb | -5.48776 | -39.72443 | 2026-10-07 16:37:00 | NPP-375 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 401db429-f96a-371f-b5d5-297f9ef8e03f | -3.89427 | -44.11552 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7cfabadb-c320-3cd3-9b9c-7adf371f7fa9 | -5.93956 | -46.63291 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fc5ea5a2-df8c-3646-83e8-5e69bba85ca8 | -9.94712 | -43.55231 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6d543229-0379-3ad0-8c69-9781d86ace36 | -8.11355 | -50.93046 | 2026-10-07 16:37:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| de9316c4-55cc-3b3e-8712-3f794b8290c1 | -6.65093 | -43.76954 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5b55e29e-be5c-3c46-b1e9-287396d356ca | -15.46044 | -47.27302 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 740cfab7-9810-318d-82af-273b8d402e89 | -8.96148 | -47.55675 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 264e2364-4452-3660-a629-a677cf39dc13 | -4.62765 | -48.86227 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4ce7c5cb-9dda-3f14-929f-236f5146160c | -6.15327 | -52.65638 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fb28a924-66f4-3335-9a1f-17c30d1a2e5b | -9.37121 | -46.26256 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 5df42241-1b46-38ef-b612-0c5b657e2b43 | -7.00174 | -56.4937 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 868ea3c3-2437-3663-89e5-d31475c75d72 | -6.07101 | -44.1103 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dfb1cefc-bc07-3291-b443-610d4174b1a2 | -4.17227 | -42.1055 | 2026-10-07 16:37:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| dff31418-ddb7-3ae3-93ae-90bc42ee88da | -3.1044 | -42.95426 | 2026-10-07 16:37:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ab1da213-efd4-3856-bb3b-ea82f5162877 | -6.23568 | -52.68268 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 66f09582-3b37-3382-8a64-cf915e12c2e9 | -4.58631 | -40.7747 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cbead00f-acb2-379d-98e7-843e8413a0ea | -8.91565 | -44.54922 | 2026-10-07 16:37:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 076507f6-bef2-30b2-931c-748006e4c0c9 | -4.91992 | -43.22589 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 72a367c8-db28-3196-9f39-fe74078eae6c | -15.22638 | -39.94886 | 2026-10-07 16:37:00 | NPP-375 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 47274435-c700-3de2-94cf-fac7027c8ca6 | -8.68664 | -41.2056 | 2026-10-07 16:37:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 36.1 |
| bac429c3-29f8-347c-a9a9-fad3d678134a | -6.48278 | -52.80759 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 79b36fbb-34e7-3bb1-b850-182159f5a3db | -7.20494 | -55.12057 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c6d5ef0c-8bab-315e-82aa-cb8eb08f71a1 | -6.00922 | -53.5016 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1498d27d-77fc-3cad-89ac-e300e8588c2b | -11.20422 | -49.41903 | 2026-10-07 16:37:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 96c1f58b-fc5e-3603-b060-26381f8b03c5 | -10.12993 | -46.85569 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 10c6c97a-6e71-30aa-af32-10a5abd2ec60 | -8.01243 | -47.17313 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 112a6857-8c1a-3fb3-a600-3bf16d70aac8 | -8.97735 | -48.94101 | 2026-10-07 16:37:00 | NPP-375 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 86a3f642-35a5-3755-82c0-c242dd80209e | -9.37897 | -45.92186 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a6ec29ca-de49-36d7-8335-769b8e0ed12b | -4.20374 | -41.76022 | 2026-10-07 16:37:00 | NPP-375 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| b6fcd575-eae8-3ed7-ab6b-015a48aad8f3 | -5.97018 | -43.87391 | 2026-10-07 16:37:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e3d0c26c-3beb-37dc-ba56-ba0b11d52833 | -15.96715 | -40.70824 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ef8716a4-8af8-3692-8833-e739418335fd | -4.17648 | -42.04084 | 2026-10-07 16:37:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 20c859f1-48bf-3a0b-ab7b-ddc6f52c7d3d | -17.5196 | -45.46399 | 2026-10-07 16:37:00 | NPP-375 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1fec2142-8501-3224-aadd-415f03f9aed1 | -7.75641 | -54.95624 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 7444e3a4-22d9-3920-ab10-ef903a1b28d5 | -7.1675 | -41.99314 | 2026-10-07 16:37:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 0b5ae0a0-bdc8-3ebb-a9c5-0e96bdd3ea97 | -8.1984 | -36.7617 | 2026-10-07 16:37:00 | NPP-375 | POÇÃO | PERNAMBUCO | Brasil | 2611200 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1845fd5d-8d67-3665-a213-bb68c509b2e9 | -6.69408 | -38.70131 | 2026-10-07 16:37:00 | NPP-375 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b8dcf853-ab2c-3359-b3e7-00256d0d19ed | -5.87196 | -51.1588 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c728cf4f-f761-39bf-8a13-69348950c4a9 | -5.23908 | -50.91351 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 845ffdc4-e404-3bc5-92b7-ac5abf4841d6 | -9.91754 | -44.81538 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0c685f17-2c9e-3a61-8d8a-f02db76f0232 | -8.04552 | -45.6095 | 2026-10-07 16:37:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 46f7f266-200b-3d05-9f56-d1b7a668f4ef | -10.64252 | -48.71615 | 2026-10-07 16:37:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8815da6-714e-3283-9ced-a107ed2217b5 | -3.12723 | -42.92048 | 2026-10-07 16:37:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bdd1a8aa-a378-3cbf-acb5-79076ffcd91d | -5.88367 | -45.97297 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ebed29da-054e-38ca-89c0-afa831fa7ac9 | -7.53323 | -45.39646 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ba910173-6087-379f-b380-4cb149f18ad1 | -6.14957 | -52.64703 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f8d268b4-6f06-3268-9eb4-60efbea79d26 | -5.74028 | -53.45771 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 38388d53-e48c-3b70-a21d-dddc81601a8c | -10.8658 | -50.6879 | 2026-10-07 16:37:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 66c40b74-5bf2-3a8c-88e2-17511b753d96 | -8.51295 | -48.17949 | 2026-10-07 16:37:00 | NPP-375 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d8117321-6abb-3cae-908f-04ece36f55a8 | -9.31234 | -48.49374 | 2026-10-07 16:37:00 | NPP-375 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e867d794-6f24-3faf-a5eb-62d9e6509cc4 | -6.37558 | -42.93219 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a73505d7-5663-32b3-ac6e-57379ad454e1 | -3.58358 | -39.14448 | 2026-10-07 16:37:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fb393ad2-b8f6-3bcc-8599-17c485d5ab7a | -16.0604 | -39.85717 | 2026-10-07 16:37:00 | NPP-375 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 96288238-4bf1-380f-afcf-aafb34b5477c | -6.43596 | -44.84637 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 505cc06d-541f-34ab-94e0-3e1d9c5dedc9 | -5.93935 | -53.48489 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README220.md)
