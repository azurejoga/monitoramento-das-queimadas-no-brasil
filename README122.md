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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cd59383-56d6-3f92-b7e0-0fa0be9086f7 | -10.8544 | -53.9891 | 2026-09-19 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 812a4d87-1526-39c4-a58b-9a44235b5db4 | -3.3494 | -59.8097 | 2026-09-19 15:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 85bab86e-6e00-3f07-8323-afa81f151445 | -11.3609 | -44.1286 | 2026-09-19 15:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 0d1743d6-f8b7-326b-8769-32febd88c3a3 | -7.8598 | -44.8595 | 2026-09-19 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 260.0 |
| ba93ac1d-289b-3a48-8523-a88c7c6a6726 | -8.7734 | -48.6651 | 2026-09-19 15:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 1a9738c5-f8b6-3494-bde3-c5e85b61f84b | -9.5308 | -51.3485 | 2026-09-19 15:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 8fc95b47-5ae2-3e2a-b7a1-531c01bbbaef | -11.318 | -51.7218 | 2026-09-19 15:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 136.9 |
| dfbeea04-84b7-3799-9ec3-eb931f80646a | -8.9412 | -44.3995 | 2026-09-19 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 129.3 |
| e02ca2f0-13c9-30a8-906d-e9bbfe021e75 | -11.8549 | -50.0437 | 2026-09-19 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| eb2ed204-fde1-36b6-bc1a-37a1245347e7 | -8.3771 | -45.6716 | 2026-09-19 15:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| c59bb2e9-b23b-3e61-aadd-74414390471f | -5.6596 | -43.3906 | 2026-09-19 15:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 50a29b23-695a-3072-9e7a-409a884ae2f2 | -7.6572 | -46.1237 | 2026-09-19 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 469.9 |
| 9ba3d107-2aeb-349b-9713-8d68208e85c3 | -5.9465 | -44.7974 | 2026-09-19 15:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 581f3793-8005-367e-a86a-9f97c08e06fb | -12.4182 | -45.0385 | 2026-09-19 15:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 8fb978be-0be9-3576-9fb6-46bcb73ebb66 | -2.8975 | -57.7793 | 2026-09-19 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 09ff4857-4d3d-3e2d-86dd-601e8a0c4be0 | -10.567 | -51.3137 | 2026-09-19 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 83947e2d-2f75-3485-81fb-a7a5719d6fa9 | -11.0614 | -49.7477 | 2026-09-19 15:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 04b85708-c3a4-3f10-8751-9ce2f2832d38 | -7.7118 | -44.6451 | 2026-09-19 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 711.4 |
| fb8e8b08-d28b-3593-b270-29697fa63eed | -11.0611 | -49.7693 | 2026-09-19 15:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 161.1 |
| a1949f11-19ef-3715-8fee-fd336c44b35e | -11.0062 | -48.3407 | 2026-09-19 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0b9c4f56-a184-3b95-a12f-10272d7e605e | -4.5205 | -55.4615 | 2026-09-19 15:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 146d2ff3-4714-358b-b7c3-5f1d9681def4 | -5.6408 | -43.392 | 2026-09-19 15:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 00138041-5ad0-3aa7-b9e7-5fd30884a3b0 | -11.3429 | -44.0611 | 2026-09-19 15:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| a69e1c9e-8d6f-320b-8e3a-b6a704474155 | -13.6274 | -48.2988 | 2026-09-19 15:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5aeb32da-e8da-3f85-8b33-51bccad882bd | -7.5703 | -57.6962 | 2026-09-19 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 180e07c5-647c-39a1-b0ee-411009e402bf | -2.458 | -57.9033 | 2026-09-19 15:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9d91d0dd-99ed-348c-84a1-d4cc55933787 | -11.7823 | -49.8152 | 2026-09-19 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9a8be714-c445-3bab-9d71-3d00400e6546 | -1.2357 | -55.73 | 2026-09-19 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| ea06a1e8-1abf-3a4f-9ed9-c943a1849f8c | -8.3365 | -50.8608 | 2026-09-19 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2e29276e-597b-39b7-a470-195b37a79bcb | -6.9224 | -55.0376 | 2026-09-19 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| c0e94bb0-ed92-330a-ba7c-f4fd401ddb9e | -10.913 | -50.8762 | 2026-09-19 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 3f65f0a6-a2a4-3b07-8426-dca8f3c19a08 | -9.3611 | -48.3032 | 2026-09-19 15:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 5988ac93-51c1-3474-9808-db4581d3842e | -5.3838 | -55.8857 | 2026-09-19 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 04740e3c-2e34-3f94-be5d-0e5990bbd19e | -10.7733 | -46.1869 | 2026-09-19 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 681a085b-de13-3ea4-b5e6-927c585a9129 | -10.1145 | -48.4205 | 2026-09-19 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ccaa2a9e-1a5c-3cf6-a85f-fd227c60dca9 | -10.4733 | -51.2597 | 2026-09-19 15:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 7075f94b-ea02-309c-8fef-519ebad92ef4 | -8.6171 | -54.6126 | 2026-09-19 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 482ab3cc-af03-3a99-b421-ffeaaa3b3532 | -8.4112 | -54.7073 | 2026-09-19 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 6a876b5b-d401-392e-97f0-aebf557c90fe | -10.9133 | -50.8549 | 2026-09-19 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 345e6c45-4d3a-37f3-a5c8-fc19d04dca72 | -8.7919 | -48.6851 | 2026-09-19 15:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 303.6 |
| 81d7e268-0e44-3cfa-a50b-62c104726688 | -11.1742 | -42.7855 | 2026-09-19 15:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 17620ea5-6772-3c60-99f1-01ec9dac7aea | -10.0956 | -48.4226 | 2026-09-19 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| bdb5062c-ee99-3dfd-a770-c756da8a5de8 | -9.0167 | -48.7505 | 2026-09-19 15:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 1748b953-8181-39dd-af4e-769a448dd589 | -10.7736 | -46.1643 | 2026-09-19 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 00572123-efb1-3fa7-8ce9-63e9be028e3d | -7.5704 | -57.6766 | 2026-09-19 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 5ed08f9d-2a8c-3bc6-9d65-c4d7cedfe359 | -3.4462 | -57.9812 | 2026-09-19 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 009e2c0f-cb7c-38b6-a422-d2842ae79134 | -10.5667 | -51.3349 | 2026-09-19 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 0f42460e-1556-3180-b1e6-7d3bb34c8a68 | -11.0065 | -48.3187 | 2026-09-19 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 8ebb1045-5bbb-32c1-b4f3-0cacea27090b | -11.7313 | -50.68 | 2026-09-19 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| e2661d6d-6353-37c3-b4ec-7d47c8b7d80e | -12.2688 | -49.1907 | 2026-09-19 15:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 982839d4-b21c-313c-8228-3478be5bd77f | -3.3311 | -59.8101 | 2026-09-19 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 8b7c4acc-073b-3a9a-9981-8134d0e40b2f | -10.7715 | -46.3001 | 2026-09-19 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 183.3 |
| bb16da16-9ecf-3292-87ad-efc6dc104918 | -11.318 | -51.7218 | 2026-09-19 15:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 8e9f180a-4829-38de-9603-a3547c8ee29c | -3.331 | -59.8292 | 2026-09-19 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 99a12c3e-056b-3bb4-87a0-1034940e7874 | -4.5021 | -55.482 | 2026-09-19 15:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 7edda7a3-10dd-3f3c-b4e9-9355e37d49d5 | -11.3604 | -44.1521 | 2026-09-19 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 28f24465-a83e-3dfd-93e2-f3b1d81fe374 | -13.6274 | -48.2988 | 2026-09-19 15:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| bc1c8826-2ef6-3a20-aeef-7c7730857b52 | -8.7731 | -48.6868 | 2026-09-19 15:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 192.2 |
| d1b0cf93-7376-3cbe-8181-6a8805980e09 | -10.5667 | -51.3349 | 2026-09-19 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 0b45762b-9779-32f5-9efa-43df3790eeb8 | -10.7736 | -46.1643 | 2026-09-19 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.1 |
| e12e4956-275a-39f7-98c6-9f1084fe0ad3 | -1.2357 | -55.73 | 2026-09-19 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 39aafd61-7e16-3700-928a-e6e723f39633 | -12.2883 | -49.1664 | 2026-09-19 15:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 51ef0b54-c16e-399a-8a6c-03dd35661fdd | -9.2603 | -45.939 | 2026-09-19 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 244.5 |
| 36423196-b311-3c51-81a1-971f5f8f4008 | -7.7844 | -44.8669 | 2026-09-19 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 5cfc58c7-31a9-365c-b6b9-da9ac1195b52 | -11.7823 | -49.8152 | 2026-09-19 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 4bb1b9f8-aceb-33f6-8976-5babea211538 | -8.4112 | -54.7073 | 2026-09-19 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 476cd315-7854-3897-852d-3907b38c0943 | -7.1553 | -47.4971 | 2026-09-19 15:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 6b6be458-3e38-30e9-b8c8-614776861f14 | -11.083 | -48.2875 | 2026-09-19 15:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c964fe14-4dd9-3516-8a0f-9475f71844cd | -11.1035 | -49.4623 | 2026-09-19 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 234.6 |
| 8cf7a476-5a4a-342f-9711-f6924ca68066 | -1.5858 | -54.4552 | 2026-09-19 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| f4ab6494-a09e-3536-a6fa-1bd70d7c80f4 | -10.7133 | -50.258 | 2026-09-19 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 181.0 |
| b708c124-a747-397a-bdce-a6f8348d925d | -7.6572 | -46.1237 | 2026-09-19 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 520.6 |
| 4a54d1d0-bd5d-358a-bd09-ce04fec52ef9 | -11.8549 | -50.0437 | 2026-09-19 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 56b5b1c2-4726-342d-a894-d3a1fec0b1fb | -5.7431 | -57.5814 | 2026-09-19 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a52d63a6-debc-3d8c-8dc6-1c235ef87b04 | -8.7919 | -48.6851 | 2026-09-19 15:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 241.9 |
| 0eb97361-cd3a-3346-8b03-08c83f2827b8 | -9.0358 | -48.727 | 2026-09-19 15:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 154.8 |
| a44b4059-48e0-3075-ac9d-908a2558bc9b | -8.6173 | -54.5924 | 2026-09-19 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 183.3 |
| de034bab-e695-3653-b055-4f5f0e7ded51 | -11.3433 | -44.0376 | 2026-09-19 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 763b3255-69d2-3adf-a4d0-004b23250ce5 | -3.3637 | -61.3282 | 2026-09-19 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 60a143eb-5299-3941-a1f5-1d626a08b375 | -10.0956 | -48.4226 | 2026-09-19 15:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 197.3 |
| c1978415-9533-3e9d-b584-c79a9d72f2ee | -3.6077 | -59.0577 | 2026-09-19 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 350b0692-94e1-325a-a7db-0eb3fd1d40a7 | -6.9224 | -55.0376 | 2026-09-19 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| c28ced83-e25e-3e01-97c6-e74fa6375747 | -10.7991 | -50.9093 | 2026-09-19 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 30d46671-07da-3b74-9e51-884bd4ff79e5 | -3.1514 | -58.644 | 2026-09-19 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| a872362e-22ab-3f68-9734-0871c517c870 | -7.7631 | -46.7167 | 2026-09-19 15:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| e76a3f5b-7d6a-3721-bc25-5e06880461c8 | -5.8968 | -59.9336 | 2026-09-19 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e2367ca3-4b19-32d4-9d9c-cb64a8338e7f | -9.7501 | -46.0863 | 2026-09-19 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 27111cf1-9dfc-3a33-8b9f-042054456d32 | -10.6703 | -50.6465 | 2026-09-19 15:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 7a865cf5-63d0-3457-9892-abb503c39926 | -11.1038 | -49.4406 | 2026-09-19 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| d52d172c-8cbf-31e9-a204-efb513ffc3dc | -5.6596 | -43.3906 | 2026-09-19 15:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| c7db8203-c18b-370a-88ca-1aacbc11ea00 | -10.567 | -51.3137 | 2026-09-19 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 69e0a34f-f36c-393e-bdaf-47966fafb51b | -9.0355 | -48.7487 | 2026-09-19 15:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 3e9b6a7e-c5f4-3b46-9e1d-e9930bcd856f | -3.7311 | -60.6018 | 2026-09-19 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ef36e1ad-f5ee-3205-8f57-0ed9612ce502 | -7.7656 | -44.8688 | 2026-09-19 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 2b9148af-2c81-31ef-80cd-e884beca5871 | -9.2567 | -46.2098 | 2026-09-19 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 326c9678-5343-324f-b71a-97b4f1249367 | -11.0065 | -48.3187 | 2026-09-19 15:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| cf18db5d-5c75-3fd5-83a5-37f2cb54c7f7 | -6.2585 | -41.6617 | 2026-09-19 15:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| 0ff65afb-8698-3979-b9a6-38bad4e44e46 | -10.6039 | -46.0728 | 2026-09-19 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.1 |
| abed1271-9661-39a2-94f3-c536861df2bd | -3.382 | -61.309 | 2026-09-19 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 113.6 |
| cf8a136e-8081-338f-aaa4-183c81ec823c | -9.3614 | -48.2814 | 2026-09-19 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |


[Clique aqui para ver as próximas entradas](README123.md)
