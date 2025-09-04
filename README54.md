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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bdc25d3-9f0b-3fd1-bcd0-47e88b03b253 | -2.95672 | -49.36044 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbcbf174-ae7c-356c-a223-b3c036569823 | -3.22502 | -47.12836 | 2025-09-04 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27b86f68-927a-32f3-bf4a-0f79f30526f9 | -3.47711 | -50.53886 | 2025-09-04 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52bc3253-f279-3f77-926f-f0eb14119392 | -2.87473 | -49.47365 | 2025-09-04 04:51:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3677304-1215-31cb-9424-d5cc6fad9fe1 | -1.94884 | -52.08402 | 2025-09-04 04:51:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1aa9c31c-b441-3bd2-9422-e228bd31a68e | -4.29328 | -48.60609 | 2025-09-04 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74fc12b4-a2a7-327e-bc64-ec5fef0bb43a | -2.51103 | -51.91 | 2025-09-04 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 125f44bf-7e8a-311e-88d7-9d84e3713c4a | -4.35325 | -48.72325 | 2025-09-04 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5aeef27-5053-3f80-8a8a-d7e90f04ff4a | -5.03438 | -42.47542 | 2025-09-04 04:51:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c62a4491-1821-3b66-8779-fb5b021fad4f | -2.51326 | -51.91743 | 2025-09-04 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc105c8c-8b55-324e-8cd2-818952d1beef | -2.95961 | -49.36485 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b27217e9-da5c-3208-9a71-8e24da62c194 | -2.96372 | -49.36153 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 028d56b7-08de-353e-8188-290d55e3f449 | -4.78333 | -43.81823 | 2025-09-04 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8749876-fe0c-3520-8abd-b21857176bb5 | -4.77971 | -43.82043 | 2025-09-04 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65cff0f5-2023-3e97-b285-0db1e5bf6b4e | -3.16987 | -48.80577 | 2025-09-04 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0acda00-d03e-334c-9f0e-b4711d61d819 | -2.96433 | -49.35767 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 59298275-1a47-3b24-a5df-90e82629e288 | -2.93262 | -48.8222 | 2025-09-04 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a3ac3a9-19b1-317a-9346-f1cd2a33e13d | -2.78283 | -49.61934 | 2025-09-04 04:51:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d50847c-5ffe-3b36-b260-1be4be1e47fd | 1.08919 | -51.31019 | 2025-09-04 04:51:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e502baa6-9ac6-3d4a-9af7-775a139989f2 | -6.12774 | -44.1465 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cd43040-1af9-365f-b812-8bb3715f9c42 | -5.62785 | -51.13885 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54faeb89-b883-3019-953c-bc6801d6f6d4 | -8.72714 | -47.00414 | 2025-09-04 04:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0e32466-0265-38ec-aabb-0bad99225a61 | -7.80573 | -46.0837 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 247c2592-b701-3698-a4ac-341812eae731 | -6.24521 | -43.54757 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 262aa5ea-79c5-381d-b058-9fa9fee2e178 | -8.45304 | -47.34486 | 2025-09-04 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a139faba-08a0-3bd5-92dc-d382e98c2a4e | -6.16878 | -55.72017 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b6f73f0-5332-3017-a4a9-d5e4af4c7733 | -8.01596 | -44.04139 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd66c251-aac3-3ce9-9151-e9fa62e80afa | -6.25841 | -43.29412 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c4a8dc5-0067-3943-8f87-fd2331f5a039 | -10.45531 | -50.38262 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ee672ff-bca5-31be-866c-5a0286c5598f | -6.23031 | -43.538 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88dc860c-dbfe-3892-9edf-4b7989556591 | -6.02221 | -46.67664 | 2025-09-04 04:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0626d639-d95b-3479-ab96-e300373dec19 | -6.3396 | -45.67533 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f999eb57-de0d-3a83-987c-a3bb08349436 | -7.97403 | -55.31099 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9686480d-0dfc-37f9-bc10-480870e790bc | -6.16947 | -55.71591 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2bbd983-afbe-356b-809a-67b13862917e | -6.24487 | -42.59698 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a8591e5d-d714-3143-9f4f-522a42028d7d | -8.01247 | -50.09491 | 2025-09-04 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7572790b-35a7-3f5c-a130-878e314a5109 | -8.36638 | -48.332 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e80717b-b675-3cac-9459-2d50649336f9 | -8.05057 | -44.13899 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c5653f4-c9e1-37be-bd73-f59985f70704 | -6.0734 | -53.82351 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5d41241-f643-398d-a6e0-a63ee7c26a9f | -6.27315 | -43.50279 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05a59a37-8acd-3fb7-97e0-57ddf7610792 | -6.54096 | -43.91124 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cab51fb2-12dd-309c-948f-56d0a86c2b99 | -5.89378 | -44.34952 | 2025-09-04 04:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d5a27daf-f384-3802-a943-dfb7bb9a703a | -6.49245 | -44.10673 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8edf6628-013d-3d23-98b3-895935bd87f7 | -9.33388 | -55.21509 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8a411c8-ccdb-3d3c-ab81-133d724dfb4b | -6.55104 | -42.95612 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37f3ee3b-6a6a-3d16-87e3-d49b5ff1c853 | -6.78212 | -44.08709 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2affed59-9d6f-3722-8141-486812df5c0d | -5.69993 | -45.17312 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 11dc204d-5ba7-3d3a-98f8-5ce08d30d35d | -11.24257 | -44.96257 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74f1c59a-d857-34af-8566-ba79f27c1001 | -10.43063 | -50.37461 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 1f735067-b854-3e70-b984-a37c80df02ef | -6.88175 | -45.5639 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6271335-0df2-3e5d-9e48-1d461089e058 | -8.53555 | -51.32516 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a77f1221-7f3e-3030-bf76-b66309a2cf93 | -8.89684 | -45.82069 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05720088-be77-3347-8694-007445601ccb | -9.95856 | -51.64497 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ce44314-be6b-376a-91e5-be1f72d94d7e | -8.02022 | -44.78388 | 2025-09-04 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2bc777ea-0197-374a-97d7-bbafa9ae3ca1 | -8.05627 | -44.1364 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 628b4088-9c21-367a-9824-546ed2a5ec87 | -10.75291 | -48.27394 | 2025-09-04 04:53:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b98cdff-6970-3f91-b752-8a9b89858cb1 | -9.43309 | -46.77642 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b72ff2cf-6f15-3ea4-acd5-2acf4395b21c | -8.06314 | -52.37471 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d04b605-3710-3e06-8ae1-817c4ad8c7ca | -6.50021 | -44.08868 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08343d3e-d14c-3fd1-9002-25c41c199777 | -7.938 | -44.94085 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1b9fb81c-0fc0-374f-8867-ebd4295f7eb8 | -8.61172 | -40.312 | 2025-09-04 04:53:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aaf17b42-68cc-31d9-98c9-cd6172a5b19c | -10.64702 | -44.84315 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54258ac8-1d7d-37e5-b435-d61e7fdfcef1 | -7.94167 | -44.94583 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3a4ddfa9-7782-3b10-a60c-3d7ffe35a0ae | -8.08195 | -45.359 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e63c037-93fa-34d4-9bb6-7e2147434137 | -6.22443 | -43.55603 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaf3b960-21d2-3045-8c9d-334c3f0cd84b | -3.69834 | -53.75381 | 2025-09-04 04:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be12067a-b1ac-3d79-a7f9-fee5acfe4b5e | -5.88715 | -51.95402 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2cdcc672-8020-3e35-a464-e12013715eaf | -6.73297 | -45.9241 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6175cd5a-4c0a-3534-a2ad-641379acf16a | -6.74415 | -58.72872 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bc9c7373-1797-3cf6-99c1-406155277095 | -7.93597 | -44.95047 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 26a2e312-0a88-34bc-9561-f57d8dab6861 | -6.50684 | -43.07747 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59766405-aae3-32d6-8a7e-9595bfbeac9a | -8.05587 | -44.13639 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ae39a15-9aec-35a8-b24f-d394cbdef20a | -7.05571 | -50.86086 | 2025-09-04 04:53:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 62f263bb-89bb-3294-802e-9ab70841fd9b | -9.70347 | -48.9547 | 2025-09-04 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 040da248-b4ec-3aef-900a-237422b08889 | -8.36887 | -48.3426 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2a8e101-979b-317d-9e2d-286e1ab00c21 | -6.23549 | -43.40499 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3f98c51-e0e5-323b-a882-931840a12fe7 | -5.27235 | -55.95931 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8a17696d-e9b9-3397-a7cf-af5dbdf6a5de | -6.78682 | -44.09096 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e066eae7-44c5-37a4-9646-b6c67b89dd01 | -3.69774 | -53.7575 | 2025-09-04 04:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e7883b1-1edc-3de4-aa2d-2b5ac275743c | -7.69207 | -48.73767 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3e1b477a-1524-3667-8c33-ee2f4d2a7cb8 | -7.63732 | -46.55471 | 2025-09-04 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9812904d-1989-3a26-9afd-8dbffd3429ac | -6.87532 | -58.93529 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fe8eaf3-1bf5-3e8a-b5db-c5f413f4d9d0 | -10.04139 | -48.13649 | 2025-09-04 04:53:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3abf0aa1-7941-3291-9cb7-4e74c4383ea1 | -6.46985 | -53.39823 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3208b23a-515b-3c82-9a0f-067f9148de4c | -8.03009 | -45.37927 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e9968611-e265-34ef-b8d5-7b9cf165d35f | -8.86428 | -52.02461 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0678cb6e-ef31-376a-94bf-d8c58ab2fe21 | -7.71648 | -50.31361 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e3f6ecb-4c77-3a4a-8c56-0ea8415c2d9f | -7.18886 | -44.16796 | 2025-09-04 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f6b6323-931c-326e-a29f-98af63576a17 | -8.72627 | -47.00484 | 2025-09-04 04:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f04caf91-379f-3c55-be71-70cd94eefd31 | -6.73329 | -45.92573 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff12c3c2-2b35-39d0-81df-0744f3810e39 | -7.0523 | -50.86024 | 2025-09-04 04:53:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8864055e-ea0d-338f-a5eb-dd8abf02a349 | -8.05673 | -44.13307 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c5c7bb0-0455-3a50-aee5-e6c70b67f40b | -5.86565 | -46.12395 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c02bb78d-ad62-3a19-870c-633b9e7fad40 | -6.73359 | -45.91988 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a367d89-a0f2-3c77-86d6-897297bd92ff | -11.03564 | -45.13399 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c600f5f-d72d-3f5c-8fde-f5092d4a7ed6 | -11.38913 | -43.56583 | 2025-09-04 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c490c975-2792-301d-998c-dcf56288b580 | -8.8966 | -45.79292 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b80742ce-7cba-3828-aa3f-563baadf8e83 | -6.20078 | -43.34154 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aaba93a7-d78d-3f7a-a77b-d70cd2edc07b | -6.354 | -43.76443 | 2025-09-04 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd672a29-d1a8-3ea8-8804-95fa4b49e1c4 | -5.69594 | -45.16741 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README55.md)
