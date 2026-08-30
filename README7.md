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
| e9248041-2952-3580-bf24-5f827ef30223 | -6.6242 | -53.167198 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd5f79a9-0d4f-311c-ae3d-ccc5ce10e513 | -4.151 | -60.677601 | 2026-08-30 00:32:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d20b1ff-8df0-3d02-8a48-ca7193e9fe3f | -6.9335 | -55.709 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d1fc410-0915-3105-b52b-ea8a491119b7 | -5.9915 | -57.668499 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17856c9f-0ccf-3c00-af45-b7dc8c6e8f25 | -11.9186 | -55.8853 | 2026-08-30 00:32:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec4f1d2c-1f66-3e10-9d24-17d55213730f | -7.4907 | -55.301899 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 916b58c4-fad8-3b0e-befd-efd31d0d0cbe | -12.5602 | -55.719501 | 2026-08-30 00:32:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cef69575-ebe1-3187-9071-cdb6655b3d3a | -15.2261 | -57.6464 | 2026-08-30 00:32:00 | METOP-B | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d50c560-1e98-33e1-b8d4-ec3e221af7bd | -7.5709 | -61.317001 | 2026-08-30 00:32:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b07245e1-4b70-384d-af6a-ee9c6817541b | -8.5061 | -55.284599 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27fc2f63-28c7-307e-889b-c9bc5c91bbd1 | -9.9402 | -60.5117 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 802bc1b1-6f93-387b-8642-135a701e205f | -8.556 | -54.772598 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 870b2bdd-061f-3d7a-934a-daf85686e0eb | -7.5682 | -61.304298 | 2026-08-30 00:32:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd94c46-5e7a-3a30-8835-286db51bbc64 | -8.9435 | -62.337399 | 2026-08-30 00:32:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e90cf0d2-868b-3b54-9ba5-e9539fa96d41 | -4.1585 | -60.665199 | 2026-08-30 00:32:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fae1c137-b9a2-391f-bd3b-8de6f3a3f70d | -10.7469 | -54.027199 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7b92633-224e-3013-be53-8b5ab7e005d9 | -11.1621 | -51.297798 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c7171406-088f-3b07-a437-e0fe46d1db0c | -10.3528 | -49.971401 | 2026-08-30 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33fc6395-18f7-3abc-8778-1eb5af0a4d7f | -14.8922 | -47.732899 | 2026-08-30 00:32:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2da5829a-411f-381a-a001-58ddc7d3702e | -11.2002 | -53.981899 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf303df-8103-35bb-81cc-2969edd913b5 | -8.95 | -62.368801 | 2026-08-30 00:32:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 57fdddfc-02bb-33a4-b437-8bacf504defa | -10.7531 | -54.055 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2532efda-f2c0-3b1f-8d70-6f8c2f16de6b | -11.7698 | -54.504398 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 941e1b0a-b046-350f-bb39-01ea324779bb | -19.2283 | -46.716999 | 2026-08-30 00:32:00 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 10456281-e786-30ed-a781-ee5dcaf371d3 | -6.2607 | -55.418499 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11c67b0d-ec4b-341e-b661-14ae468f837a | -6.6899 | -60.110699 | 2026-08-30 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93d9fcf1-f9a7-3843-8781-be8c3283fe68 | -4.0863 | -54.101101 | 2026-08-30 00:32:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a6f7817-4727-3479-881c-4653c975d795 | -8.6112 | -54.7892 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e099187-73fd-35f8-99f9-50bab882ea68 | -11.8305 | -51.111099 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6686057e-2ecc-3f4c-a316-e30d19fceaa2 | -7.0579 | -55.666801 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac5015b5-da18-3a7c-96f5-67cd595807d5 | -9.707 | -60.714401 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf73f02-5338-3253-9577-ed4895f28164 | -5.8792 | -57.764801 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f839b5fc-dd59-365a-bea4-588306447b0a | -7.0726 | -59.702702 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9c2ce8f-c760-35e1-bf61-63a84b86d19e | -5.9881 | -55.7174 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed55551a-1720-3809-b8f3-7945fdbc3a51 | -8.9565 | -62.351101 | 2026-08-30 00:32:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 034ef61d-05ee-3950-938c-f6824e9debe9 | -9.1962 | -51.5396 | 2026-08-30 00:32:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4beb44ac-1393-3c9f-9fe9-b334fc0e9f3b | -10.7402 | -54.043301 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e5db62b-9de2-315d-a332-326a02c70618 | -10.7437 | -54.013199 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f2fd68a-1d99-394f-8529-e68cb713af68 | -7.3109 | -60.574299 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f6e651c-ccf9-3e64-8ce7-a26159ac6a84 | -7.0046 | -59.625198 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8985b31-de6a-3ebe-a431-832dec9e61ed | -10.7504 | -53.997002 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42e7e281-faeb-3137-9ead-a8bc1bdc60a1 | -7.3133 | -60.585499 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50784448-7acf-3e47-899d-cc3df308e71f | -5.8954 | -57.7453 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb118a15-d6e7-37bd-9cf4-57536ccffe2b | -8.6096 | -54.782299 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e35a19e2-d600-3137-9f45-6f42fc25ae39 | -13.8405 | -54.098301 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3785c5e5-4b04-32a8-bd0e-26635b51df26 | -4.0847 | -54.0938 | 2026-08-30 00:32:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85736cb0-09e2-3fd2-bcd1-f103672f1f51 | -4.6883 | -55.6619 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a42e46-68e0-3aa4-b93e-9fe49e1a20b1 | -6.1591 | -57.7757 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8170d5df-f1e6-31e9-970e-1ff02a10194d | -10.7453 | -54.020199 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 543b6b5d-5a2e-3a10-958b-2f1ad9a2bf47 | -14.1452 | -52.831699 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac910683-74ad-3536-80df-b5521f7b444e | -11.2455 | -54.0009 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4838268d-2337-3188-bb2e-5f4c8a052a9f | -13.8452 | -54.119499 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 183c2789-a947-3e00-83da-8055811dffd8 | -5.9857 | -57.781502 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40fc36b3-b023-34d0-8392-b45934137fa2 | -11.8286 | -51.102798 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77e55999-3c31-3708-99a3-16a5670de60b | -6.9402 | -55.693001 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1513c54d-056f-3944-bb81-b767e871e152 | -11.1886 | -55.085701 | 2026-08-30 00:32:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d96d646-5bc5-3b3f-8542-3b0987b47447 | -1.2445 | -55.694599 | 2026-08-30 00:32:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5fc35cd-06c3-3ccf-b585-e8f7009b8eb0 | -11.6337 | -54.5868 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b147a780-ba67-345c-a9f1-430d3d2bec02 | -7.5753 | -61.2897 | 2026-08-30 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1e378ab-e879-3080-9950-78b3fc20035c | -9.7096 | -60.726898 | 2026-08-30 00:32:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c139d5fa-82f9-3910-a7bc-d4a47eb00231 | -5.8775 | -57.757198 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6f80065-b687-309e-b7e9-0027376999f3 | -8.6029 | -54.798302 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4814626f-7a11-3c6e-99c4-7e8f6b089e89 | -6.755 | -55.6474 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c979c75c-e915-3c5c-a0d7-f10da493bf5a | -6.9106 | -59.4744 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41c408bd-b9de-31f7-99a9-ed5ea2ea732f | -6.1384 | -53.5205 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f717d417-b401-3c29-8832-b3bc58edabdc | -21.316299 | -51.3092 | 2026-08-30 00:32:00 | METOP-B | IRAPURU | SÃO PAULO | Brasil | 3521606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8de078ed-8769-3457-9d7c-b78c42d6a947 | -10.7551 | -54.017899 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e52f0565-ec6c-3187-8148-3a7b1a37aca6 | -6.9598 | -55.688599 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcca764b-5456-3ae1-af35-ad424e22c274 | -10.7526 | -50.872799 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63a3b31f-443e-3744-b970-a8c5cf057f0e | -3.7603 | -59.329601 | 2026-08-30 00:32:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7528e2cf-44c2-307b-a496-996db7fde856 | -6.9448 | -55.713699 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48865f5f-2c1f-3276-94c8-82c934f9e64b | -2.9358 | -51.471001 | 2026-08-30 00:32:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd3bc70-1c41-3688-b8c9-f702c9f749df | -3.6258 | -60.527699 | 2026-08-30 00:32:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 594d2376-0c5e-3dad-9b29-8f20f6f904d2 | -9.8857 | -60.249001 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16d4850b-eac3-3e8d-9490-77d69204c3c9 | -3.4886 | -54.642799 | 2026-08-30 00:32:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e00edaec-93b3-3484-ad72-e4aff2f72c01 | -5.9874 | -57.789101 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8d5cfc8-1525-3364-b20a-29fa4a7bfb4e | -7.065 | -59.7146 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17244512-1957-3b9c-84ba-beaaa16bbe08 | -3.4902 | -54.649899 | 2026-08-30 00:32:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d3270b4-c1ec-3bff-8fdd-a2b75a776890 | -6.7632 | -55.638302 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2a686b4-f189-3a7b-a762-71a59e9d754a | -11.291 | -54.019798 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6edf39ea-e811-3c3b-842d-f553ed2d62c8 | -14.4213 | -52.5481 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e879791-3dd7-3284-85f2-8115cd68a2a6 | -11.4421 | -61.449699 | 2026-08-30 00:32:00 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cca0e6d7-7c9c-37ae-9138-c56430ea1ef7 | -9.8954 | -60.247002 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9ebf7c-bee6-3e13-bf7a-4712c82390ce | 2.1781 | -50.688301 | 2026-08-30 00:32:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b38b6e19-c6c7-3123-99ad-780c88073df6 | -9.9552 | -53.988499 | 2026-08-30 00:32:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4d769fc-1ff7-3bb3-81bc-90d34f9bac38 | -5.8809 | -57.7724 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58feb46e-a24f-34b8-8c5d-66af94ddb743 | -11.244 | -53.9939 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d637a39e-c95f-3355-be06-5ef0d598dc24 | -9.0431 | -65.384499 | 2026-08-30 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3118a1c-2335-3090-b61e-ea7629e80ce3 | -11.711 | -54.517799 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 047b3472-cc7a-3686-9693-d7875572e21f | -4.2194 | -59.5476 | 2026-08-30 00:32:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 771b795b-1fb8-32c7-9a18-a0e991889fd4 | -8.6153 | -54.715698 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1641607-3223-393a-a5c3-c91c596e3592 | -10.9285 | -42.983002 | 2026-08-30 00:32:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb8894da-c433-3ad0-84f2-9b365e99f98b | -9.2536 | -57.512299 | 2026-08-30 00:32:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3643476-60eb-3556-b5a4-b542ea56a38c | -15.1221 | -53.564602 | 2026-08-30 00:32:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23814bd9-5e99-3804-b908-ded690fe6f45 | -14.7453 | -48.734798 | 2026-08-30 00:32:00 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5e015961-af10-315b-b68c-747f3e44f782 | -3.6302 | -60.547501 | 2026-08-30 00:32:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54a7b9e0-a857-37ed-bead-5c0773a2e483 | -6.6455 | -53.1702 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa614052-516a-34d7-b920-00b651ad4103 | -6.7482 | -55.663399 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec83d002-9122-3fa6-9d88-910d5b202983 | -9.6719 | -55.066502 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| afc77e17-5efc-383a-8f12-d6a543bf3555 | -6.9288 | -55.688301 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
