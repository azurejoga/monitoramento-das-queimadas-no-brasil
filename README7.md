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
| a2972458-e42f-3ddb-90bd-4ff8b68bb6fd | -4.94643 | -44.91709 | 2025-12-04 04:21:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 497290fc-2ea2-30b5-bc9f-351bccfcf1cf | -2.64026 | -48.53894 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1908719-b4ac-368e-9a5d-9edb949b387b | -4.52436 | -44.65919 | 2025-12-04 04:21:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d5dfb8f-8055-36f3-a982-2baae84fa319 | -4.26063 | -44.15168 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cee41c73-2c2f-3511-ba13-2f6e7fcb353a | -2.42338 | -45.80422 | 2025-12-04 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44655738-0a4b-3d21-bcc9-259af24e2d45 | -1.42454 | -53.01252 | 2025-12-04 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79656d56-f3af-3a45-98cc-544557e62ee4 | -9.32999 | -36.95802 | 2025-12-04 04:21:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| add8832e-6810-316f-ab5d-a2ec7ae489b7 | -2.79148 | -47.43197 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b5cbf87-bd6e-3d4f-84fc-5578769cbda6 | -4.34713 | -46.13898 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4acc4e2a-4d2e-3891-a60c-0e0fc1407620 | -2.06287 | -45.35719 | 2025-12-04 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d663418-481a-3dbe-8017-69e1ec8dc96a | -3.32925 | -44.38586 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46af6857-c5d7-3c66-a834-5cd79dffe6f8 | -3.95221 | -42.59285 | 2025-12-04 04:21:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 836d18f8-734d-3118-b8b7-3bcb62590426 | -4.72964 | -45.70353 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c8aae76-393d-367b-95e1-0cc226808385 | -10.42896 | -40.54883 | 2025-12-04 04:21:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4802f56d-8b47-3207-b69a-a95075ed609e | -4.82739 | -43.19784 | 2025-12-04 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07967675-a45b-3254-ba97-34e7df0c792f | -3.1438 | -49.41343 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fa1bfa3-7d45-3ba8-90f9-5a364078b1f5 | -4.69743 | -46.43054 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56a08187-01df-3f08-8b8a-dff772992042 | -5.3475 | -42.11779 | 2025-12-04 04:21:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5265f44-7056-3822-800f-471500218cf1 | -4.77702 | -46.13084 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc2abb1e-c3de-38a1-9c20-daf917f5c6ea | -2.89988 | -40.22094 | 2025-12-04 04:21:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93f9e963-8acb-3e94-bd84-d46a071b2d27 | -1.83752 | -46.5868 | 2025-12-04 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d9fd936-9dfe-39f8-beb4-4b827f879483 | -3.29141 | -45.35754 | 2025-12-04 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75f74b69-ff2b-39d6-94ad-079422d6526f | -5.86292 | -41.49014 | 2025-12-04 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 888e7f74-1727-3193-bc2b-5b1d1d5846c9 | -3.32871 | -44.38931 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d11cd59a-37bc-3a4c-9de9-002521b763b9 | -4.90258 | -44.50335 | 2025-12-04 04:21:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3010f8a-9a99-3013-903e-1f8654005d5e | -2.96921 | -49.62526 | 2025-12-04 04:21:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dd8afbe-04db-38dc-ba42-d52fdbdb37ca | -6.68298 | -39.49834 | 2025-12-04 04:21:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 465b0374-11d3-3365-97ce-c6b498930d61 | -6.21432 | -38.52509 | 2025-12-04 04:21:00 | NOAA-21 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bff56e7a-aca5-3692-ac38-f88e61e4ee55 | -4.54457 | -45.69316 | 2025-12-04 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd738a49-fc7a-3fb8-b950-68dd1c7b3d53 | -2.8601 | -45.39668 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80c2357f-8445-3f38-86d6-4eda41b3fec0 | -2.69587 | -49.16854 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b74653d5-970f-321b-92e2-57f5a79c37b5 | -6.58701 | -42.8861 | 2025-12-04 04:21:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 523159a1-fd05-39e2-83e2-92da71b9a91e | -6.43571 | -44.79255 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0dccead6-356c-3778-a311-2cdba76b64c4 | -4.55834 | -45.80224 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0c00c88e-de4c-399b-885e-f0708b0ef3eb | -6.32741 | -39.82475 | 2025-12-04 04:21:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 225ca0f9-c8cc-35ab-b18f-b2eb5f8143f9 | -2.60708 | -49.25679 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08c32d4c-d38e-31ea-9bda-d82fd850fa86 | -3.38545 | -47.27859 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9febaf3-1d64-3a56-a1a7-a0530fbd6df1 | -3.8163 | -46.07619 | 2025-12-04 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cef16a20-2f5a-3164-bb0e-d812e8ef1011 | -3.85285 | -47.04823 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7381be4-b5d4-386c-a9dc-091c58c2b971 | -5.64033 | -39.45702 | 2025-12-04 04:21:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4af6291-decc-334a-b3a3-0566245b9e86 | -9.30691 | -35.63589 | 2025-12-04 04:21:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a06abc74-e5ca-3810-803e-7594c99552db | -2.26501 | -45.05126 | 2025-12-04 04:21:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fce37f2-9ed9-3ba4-9f82-6b51249b4d04 | -2.53745 | -45.3722 | 2025-12-04 04:21:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 058a975a-fe87-3dd9-9616-664de9030cb0 | -2.38168 | -49.39161 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e720cef2-5a86-30b7-afae-27179c8397c7 | -6.4291 | -44.79152 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adb5c5f9-6bae-3bc7-984f-ef9b50489253 | -4.21472 | -44.25024 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a884b177-5bed-3311-8b15-2c08fc6d2612 | -6.489 | -43.90614 | 2025-12-04 04:21:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a214379e-1433-3a20-87e9-17654ce27175 | -2.60654 | -47.76898 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49a64d4f-a3e7-3329-b38e-77c63d346822 | -5.58884 | -46.14632 | 2025-12-04 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16b2fad6-37eb-3533-b2b8-edcf44598ddd | -4.79085 | -45.62191 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19777236-54eb-3ae4-9c3d-8f5556a8b762 | -3.07423 | -46.65237 | 2025-12-04 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 421d2460-2007-369d-9d2e-f9e720fc9797 | -2.63789 | -48.03224 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afe92ff7-ba67-3e39-842b-2a86d8661aff | -2.70277 | -49.31001 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d743e7e-09b8-3c3b-a189-b5bb4160ea92 | -4.85764 | -42.47576 | 2025-12-04 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c2e04e29-877c-3f69-8f09-d34e14eda97f | -3.33453 | -45.6627 | 2025-12-04 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2230af38-f5eb-3ec5-9ca4-7f8d0294ee55 | -1.43057 | -53.00977 | 2025-12-04 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a9c6e72-3259-38ea-8cee-645556439c45 | -2.39005 | -49.39293 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c269514-f4ea-3725-b561-c5527bff0622 | -6.33625 | -41.40239 | 2025-12-04 04:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a50d800a-f555-3e9c-982b-bdfe6182412b | -5.79387 | -43.74039 | 2025-12-04 04:21:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b680ff6e-f344-328d-a60d-616904094689 | -4.32143 | -50.93725 | 2025-12-04 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3de36be5-6f89-35c2-9e30-fdbf05b16824 | -2.06345 | -45.35357 | 2025-12-04 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fb9e1c2-f0b5-3eee-997e-3e1c5e3ca26e | -4.49821 | -45.76704 | 2025-12-04 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3039ba67-61b2-31c6-a1b8-47469e420004 | -3.23066 | -46.8559 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 053d714c-514f-31e5-a745-b7f4993ef407 | -3.04543 | -48.42212 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7822afdf-5b70-3865-92c3-9883f1a5da7b | -5.8364 | -43.26978 | 2025-12-04 04:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60f0dc27-ae92-3d75-854e-dd6d32af582c | -2.36431 | -47.68326 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c055b20a-c179-3c16-9e70-a74423ee9324 | -4.92883 | -44.70536 | 2025-12-04 04:21:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ba8f1a8-1f79-34a3-86d7-cd7172186cb4 | -3.71934 | -44.63121 | 2025-12-04 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ad2836f-809a-33bd-bd57-0092d39cfd8f | -2.42801 | -50.29588 | 2025-12-04 04:21:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ad2707-a3b0-34bd-acfd-9c48f7010415 | -6.42856 | -44.79498 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16de7318-579d-3693-954d-58dd93405212 | -2.64624 | -51.62701 | 2025-12-04 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddab461f-ad57-3676-93b2-7f84ff409c3c | -2.60651 | -49.18079 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9290054-c21e-3bb9-8b78-15ca8ecbd808 | -4.07752 | -43.69212 | 2025-12-04 04:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9190f339-5e61-33d4-bbe3-21d773b66e69 | -2.48471 | -47.827 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 423fdea8-db00-3457-acc1-44366ded2da4 | -4.51053 | -46.08169 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dfe91ff-3dd2-35f4-baa5-7aa225b468fc | -2.85531 | -44.99836 | 2025-12-04 04:21:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a22696a3-a274-3b19-981c-652a89666cc8 | -5.29102 | -43.84706 | 2025-12-04 04:21:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b6516a9-0340-358f-b270-1ae9434d1270 | -1.35611 | -53.22459 | 2025-12-04 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e5703e8-c3fd-3c4a-addb-c4cfae58e00e | -4.20811 | -44.24921 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4863982a-238e-3e56-93dc-a0b4096b1325 | -5.03078 | -39.38156 | 2025-12-04 04:21:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05d36603-7581-339d-888c-fd56212fad52 | -2.5414 | -45.36912 | 2025-12-04 04:21:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 1ea66ba7-8cc1-31ea-8164-5b02387aef3c | -4.25228 | -49.2496 | 2025-12-04 04:21:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5a5c9cc-48f9-37a7-9f56-bbf4af8bf986 | -5.99903 | -42.28387 | 2025-12-04 04:21:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6ce0bdb5-2be4-3b54-b234-6a0d7ef6d743 | -2.90784 | -48.73023 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 038f2777-bba8-336d-b9b7-befb54e517d2 | -4.69683 | -46.43433 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30c9e0b2-979f-36d4-a7a2-122427fe8125 | -5.03425 | -44.83559 | 2025-12-04 04:21:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3f74ffc-7c03-33fd-a39f-506ab1550666 | -4.21335 | -46.35938 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50e8ff72-ff88-3351-8442-95638b7561dc | -2.70218 | -49.31375 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ce55fab-86f2-3156-9899-1d431c6066d1 | -2.96128 | -44.36615 | 2025-12-04 04:21:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e049262f-1c71-3d58-a5cc-e842b8e64e0a | -2.56625 | -49.06592 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cba223a-79fd-3b03-b6f2-cc52118f5b0c | -2.60235 | -49.25988 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a744b07c-0820-35fd-b061-842d9a15ebc5 | -4.55229 | -47.90952 | 2025-12-04 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9e8b857-9d5a-3862-99fb-5149c1375a06 | -7.21915 | -45.04437 | 2025-12-04 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9750f26-7eaf-3e22-a5d3-3fa9febb1cdd | -2.63429 | -47.31143 | 2025-12-04 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ebb3a843-b484-3bf8-8147-497d70fdf8d9 | -4.47543 | -44.25626 | 2025-12-04 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3667d846-0255-37e0-820f-a630b781f53f | -4.02593 | -47.33799 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70c48791-5185-3a3c-b7f8-bd1cb8dac682 | -4.10385 | -46.31976 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e508f258-070e-3f55-b7a8-af3f4d99fcec | -4.1209 | -50.68505 | 2025-12-04 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca980b17-b3e2-3b20-81ef-f80d87180c99 | -7.61636 | -39.04352 | 2025-12-04 04:21:00 | NOAA-21 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4b30a73d-b3d3-3f0b-8519-014a0a93dd87 | -2.8665 | -45.24737 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README8.md)
