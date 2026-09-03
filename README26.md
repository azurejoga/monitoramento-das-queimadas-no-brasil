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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7c0cb28-3d8f-3118-8a00-2468b8b79e6d | -6.64809 | -59.43032 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66bff059-9d0e-38b8-af9e-aeb620653206 | -4.1204 | -51.02845 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7db9d5bc-846e-35ba-93f9-59432682a6cd | -3.80239 | -49.1111 | 2026-09-03 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da47b5e0-6d6b-3138-b1d5-de3170f5becf | -4.02917 | -38.23149 | 2026-09-03 04:38:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f5d76706-2703-3000-9eba-f2510586f7d2 | -4.63081 | -55.73111 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86218db6-eb98-3907-9f53-6cb1cafa0ab5 | -6.50607 | -53.61214 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 196435db-d6ea-302b-b7ec-1a173251db93 | -1.02094 | -53.72416 | 2026-09-03 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41fd1eeb-e55a-3046-a059-a5bfaed379d2 | -6.62248 | -55.22786 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25c7a675-ec09-30f2-a3d1-e88989ac3155 | -8.43329 | -54.69741 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f3c490cb-4fb1-35eb-9794-75e7976141f1 | -5.80547 | -43.64551 | 2026-09-03 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e969cd35-2b42-3f39-9bfa-f2d9641eef1b | -8.45743 | -54.64633 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 653b7f47-0f46-3e12-a2d3-17a89ce39026 | -7.6578 | -45.86665 | 2026-09-03 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62adbbe7-28dd-3e15-be7d-6ef5da636d2e | -4.10871 | -51.02286 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f20b939-f515-3352-ab96-dbe01690af14 | -6.15252 | -44.64908 | 2026-09-03 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eae62ce-b9e4-3b79-9abe-580e7a6123f3 | -3.0342 | -48.41357 | 2026-09-03 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41be510c-8d0f-3065-91c9-28609d408f7d | -7.92776 | -44.22589 | 2026-09-03 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8334eb1-b44f-34cb-a025-b0636340079a | -7.4091 | -49.74414 | 2026-09-03 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97baf777-1c9c-392e-8a84-9ce1907517a6 | -4.63015 | -55.73482 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89877f2b-0f2b-38b4-9c70-31a32713403c | -5.85682 | -57.55854 | 2026-09-03 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6d46166-aef6-3daa-a79f-eb51f33f8cc8 | -5.24829 | -55.89854 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6794ba60-dc0b-3a31-b084-e049e38bd981 | -6.26458 | -47.35162 | 2026-09-03 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b77943dc-b30d-399a-9470-16c800c7a6a0 | -3.45011 | -56.32063 | 2026-09-03 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7cae3ec7-ea07-3d17-b91a-600f8afe5ccd | -9.60118 | -40.34095 | 2026-09-03 04:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 76daa93c-5f3b-3d4a-9571-0b53955b0c04 | -5.54952 | -60.23044 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b86440eb-df9c-310d-8601-5b15b968abbb | -6.50223 | -53.61341 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8874d335-9b27-3dbf-a1ee-8174a4b888ef | -9.27322 | -45.65091 | 2026-09-03 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b966f337-d8c7-3312-86f4-7ec824d46ff3 | -7.04976 | -59.22514 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c84a9091-f94e-3b22-95de-e57bbcfb1381 | -5.23157 | -49.60107 | 2026-09-03 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 655ce1b3-3091-38dc-a1be-f74593c67759 | -6.67297 | -43.40714 | 2026-09-03 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77d23b56-eede-3d53-b853-9c95fb09da14 | -6.37162 | -45.9547 | 2026-09-03 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53499dd3-0a77-38bf-a119-80032b3bb8f1 | -5.45008 | -46.58335 | 2026-09-03 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b3cb317-716a-37ad-bb53-3362a9db3f8b | -6.1503 | -55.66909 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efdca783-01d2-3315-91b9-63038dbe03ab | -7.05088 | -59.21922 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe9fd5d6-3292-370d-88b4-024d7c5ecc29 | -5.8459 | -52.06645 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f30268a7-b318-37b8-8701-ba7d175acbb8 | -4.18541 | -47.84719 | 2026-09-03 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b44fc6e1-7654-39ca-a417-afd7908df851 | -6.15093 | -55.66558 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03094828-7d1d-3f29-9d2b-bf7a3511c70e | -6.30398 | -56.03817 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7b747dfa-9f85-39c8-9f3d-d52d71d2da6f | -6.76196 | -44.57051 | 2026-09-03 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61211379-23e5-3b80-8094-c30ff1c794ff | -6.77807 | -56.41749 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 167e994a-029d-39aa-9cd7-1cd1440cd9a2 | -6.39117 | -55.2294 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f641a16-f53c-3d31-a97f-5a4cd4965f22 | -6.67953 | -43.41241 | 2026-09-03 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b20afe5-98f4-320e-bca9-ecd8367b4217 | -6.68775 | -59.94048 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df7c38e2-a62e-3cf9-b903-b15033918cf8 | -3.18682 | -48.02022 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59058045-0d2b-3ec2-908c-dd6e1f3e1c2d | -6.64568 | -59.44344 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76d3f391-7a16-3211-83a6-c1c86c5fb1e5 | -6.64585 | -59.45018 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86a30cb8-015c-38ba-a105-69ec536fd3a1 | -3.43212 | -51.512 | 2026-09-03 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dee96e5c-6e9e-33d7-80cd-909b9ae58243 | -3.34229 | -42.79823 | 2026-09-03 04:38:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f270fe46-85d9-31f6-bf58-6b360c8115b2 | -6.75353 | -59.44502 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d65827ac-dfa1-3394-9bbf-f2c58e890e21 | -1.65593 | -55.03241 | 2026-09-03 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69789e9d-8be6-300f-8062-f444f4649e6c | -3.33452 | -42.80117 | 2026-09-03 04:38:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6bd555f-f970-306a-813b-e09c0739d335 | -6.6808 | -59.93901 | 2026-09-03 04:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53ad7b69-1014-3282-8acd-38ee991d98a5 | -8.71647 | -52.36157 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74a70952-0781-3526-90cb-285d1827fc10 | -5.82774 | -47.03734 | 2026-09-03 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3abc8207-2fd2-302f-8621-9bd3f18022a1 | -5.24952 | -55.90686 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a88c3f4-6f28-3e10-8eb2-d68113cb266b | -8.08231 | -50.95997 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81d2fc02-3b25-3661-82df-e18ae055a243 | -8.42544 | -54.71322 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21c755f8-6c16-394e-87b4-8e3005d6d18e | -1.50565 | -54.95935 | 2026-09-03 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1041e9b5-40e6-3573-a561-bfc4246c082d | -3.33389 | -42.8052 | 2026-09-03 04:38:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b16f23e8-ee1b-3bfd-8b3b-b9bfee791dd1 | -6.50308 | -53.60861 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92753bf3-df12-3838-a59f-cde213cccdd5 | -6.31302 | -56.05137 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 94e03630-3435-3d06-b760-bd0165ae25fc | -7.23696 | -42.75873 | 2026-09-03 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3003e821-543c-3804-a0c4-fa093eb0cbf2 | -7.82696 | -47.66922 | 2026-09-03 04:38:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f32305f0-0236-396a-8f68-8dafc2065e07 | -8.4296 | -46.89126 | 2026-09-03 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d8f79b2-97d3-3eb1-b082-fa6903c460a3 | -6.76021 | -59.4396 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cd8d9e7f-be6c-34e3-bfee-0a063fc9425c | -5.73192 | -43.27943 | 2026-09-03 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73d780a1-bfc1-3c5f-96fd-8b4e51f310f7 | -4.02345 | -47.72621 | 2026-09-03 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7d23747-ad6f-3d2b-b8ff-93933b86e699 | -2.66036 | -49.14114 | 2026-09-03 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 032de32f-411c-3ca2-8550-dbe4ce1be62d | -8.44014 | -54.68722 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a9cfd2c0-f053-3e07-be20-4dd36a1479b1 | -6.31016 | -56.03556 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f24c5ed5-3454-312d-af62-94d6b282f17e | -6.36606 | -55.21862 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ec0ba0a-5599-33f4-83ee-324839f5b930 | -8.95665 | -49.51517 | 2026-09-03 04:38:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a45ed6be-6b62-388c-a493-633825c9c86f | -4.69667 | -56.06456 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0985189d-ea6a-3a3b-ad14-290fb0eed052 | -2.70539 | -49.50637 | 2026-09-03 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fca4af35-3742-3579-965b-ab24cc4f23a0 | -7.56762 | -48.36132 | 2026-09-03 04:38:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e176f07-fadd-30bf-ac41-fa57f5f240ff | -3.12899 | -48.58949 | 2026-09-03 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c8ecdf4-b9ab-32c5-927c-ffb8d4473ab4 | -9.22163 | -45.76117 | 2026-09-03 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36d8752e-d252-300c-82b8-31b02d41f96e | -8.43432 | -54.74849 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 78550799-4dca-3f9d-aa6c-24344d80238a | -4.11283 | -51.02332 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3505d6bd-bb66-3d4c-b766-13540b221b73 | -8.43817 | -54.69834 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e2082e2-8bcc-3240-8743-a10da686cd35 | -2.26186 | -47.00859 | 2026-09-03 04:38:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| debb8bdc-115d-3a15-8eda-13a1a084430f | -6.94338 | -45.20268 | 2026-09-03 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b3119ed-c1b6-3e29-9572-fb946e61eeb3 | -7.73043 | -49.59015 | 2026-09-03 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8626bdd3-78bc-388b-b4d4-dd9c89ab0f1c | -6.64712 | -59.44352 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa4161c6-8991-3da5-ba0d-3a5893f89627 | -6.3655 | -55.22176 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 446302d8-92fb-3712-ade7-58e7fda27dae | -6.31989 | -56.045 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 51efe44b-96ec-3708-a8ae-eebba2c52a30 | -6.30453 | -56.04346 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5172975-03f8-3527-bbbb-b8f464919a5a | -1.46726 | -54.81607 | 2026-09-03 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d530421-2a74-37d0-8899-8414c7534c38 | -7.26209 | -47.52698 | 2026-09-03 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f9f9bfde-5870-320f-ac66-136f97e68a2a | -4.14453 | -51.07691 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e83f01c8-9ec1-3d73-8bd6-049ddf66483b | -4.97198 | -55.85685 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06d533c1-327c-3fa9-9786-40ebe2182418 | -2.38716 | -47.60433 | 2026-09-03 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccd7b1ad-535e-3206-89ca-0ef6dbc5a408 | -6.75469 | -59.43894 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a66891b0-503a-3133-8257-5868af640fe9 | -6.67891 | -43.41655 | 2026-09-03 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 06027604-3a86-320b-8fc2-c6ad55baa032 | -4.1486 | -51.07779 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bb714589-09a2-3979-9bd7-bea239674f1c | -6.32658 | -43.81785 | 2026-09-03 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5decb0eb-412b-3cff-87fe-a088f1b06801 | -2.26469 | -47.01275 | 2026-09-03 04:38:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 420744b1-8d03-3393-b2a7-e875563c65be | -7.32101 | -55.13572 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c32f73d-d82f-31a7-b2be-7c75388eca42 | -4.2683 | -55.15626 | 2026-09-03 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c89e0b28-7806-3e35-b376-ec7e292646db | -6.30582 | -56.036 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49ea780c-14b3-3119-bcc3-c05e7fa6a002 | -7.07734 | -44.35573 | 2026-09-03 04:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README27.md)
