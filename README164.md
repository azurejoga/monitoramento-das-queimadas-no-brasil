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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b717f379-c68e-3157-9c42-e65714aca1f4 | -7.41487 | -55.16301 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eb711b5e-44aa-35bb-b8ad-6795754f3108 | -12.09839 | -47.16077 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 511b6878-c22b-3b57-a9db-0416c8107b7b | -11.69933 | -47.61007 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3b4bd56f-f971-3bca-bd34-9df985105b69 | -7.91087 | -44.25727 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 430a861c-8420-3caf-a30a-0b8db5161cd3 | -9.67213 | -47.93352 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b145ef68-7caf-32d3-be11-8dbc18f76093 | -11.04016 | -49.67391 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 73dad839-d3e4-3820-b8fe-ffabd64cfe0e | -7.6362 | -46.72667 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2d2b75a8-22f8-3628-9112-2cee0848f286 | -10.11637 | -50.28931 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 69da7596-e8d3-3aa0-b086-f760ab68a6c3 | -12.09534 | -44.99066 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d31430d6-08eb-3c9f-8c13-1aa28a35382e | -9.65894 | -46.06166 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a54925fc-af66-3d33-a515-dc0aca4eb44c | -7.25607 | -39.21551 | 2026-08-31 16:50:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 21c2c7ec-4802-34b5-86a2-e9fbae842d92 | -10.46542 | -46.55362 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 52db0882-9858-3ff8-8eec-3d023f953402 | -11.49097 | -50.34023 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8a0576a2-cadb-3da1-9c85-1ad3284aadd6 | -10.11741 | -45.84376 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 3c57e836-0969-3de8-b254-9fdb4a705f87 | -10.02349 | -45.55386 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 97ed876e-5ef9-3409-a37c-28fb2a0c692c | -8.92181 | -45.03254 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1bc419d5-709a-322c-bb86-b9897fbb8ff4 | -6.76661 | -48.11062 | 2026-08-31 16:50:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 093a6e44-16f9-318e-bca5-9d4de64adbb4 | -13.83176 | -54.02858 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1e15ed0a-6362-3046-b8d9-ea71ff54d250 | -7.215 | -42.73829 | 2026-08-31 16:50:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 999e1141-78da-3499-b1a1-5756d29266f2 | -9.80154 | -59.43277 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 2000a384-0b9c-3609-bae6-02bacbc08353 | -10.09465 | -46.62201 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5a69e2a2-e334-3acb-8a1f-17de130661e7 | -10.09921 | -50.29188 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 14aa08e4-9dff-329d-b086-1039b57ed1f5 | -12.0901 | -47.15119 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 28ed692b-c4ed-38f9-b03a-6008073a4cc7 | -12.10005 | -45.06481 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 06ed3335-a263-3acf-9fae-fe1e742d9e55 | -11.67453 | -47.60324 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 23e21658-bd90-3d86-96c4-b06dc37983f5 | -11.20384 | -45.10165 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 05940773-c6be-3f34-80cb-025d4cf3092c | -12.567 | -45.08343 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a941ac19-d289-3435-ade5-1fcc611a96d1 | -10.82737 | -50.68922 | 2026-08-31 16:50:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a95259d2-812e-33a9-b1e3-22af9b22ef3e | -10.82273 | -50.68182 | 2026-08-31 16:50:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| fdd98d69-444d-3f27-8f23-0524b14aadca | -6.49989 | -41.85676 | 2026-08-31 16:50:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 15bcf279-9cab-36f6-9331-8eafe0ce6187 | -8.36373 | -57.67638 | 2026-08-31 16:50:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2bc7eb0-6e8e-371d-a849-b8c0fc3b7372 | -5.58627 | -45.33833 | 2026-08-31 16:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4489a430-7919-3830-a12c-e250cf1e3657 | -11.91731 | -45.05695 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4cc09589-e2f7-3bf2-8350-bb8841b37727 | -10.75179 | -54.06736 | 2026-08-31 16:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ab2f4936-b525-33b0-8f92-630581f3a7ef | -8.13054 | -45.58289 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e27aa554-e152-36cf-8869-f8d3b6e76382 | -11.24856 | -45.10694 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d24ce4c-f6a1-3753-b535-e3ac1de21542 | -7.91312 | -44.24662 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 04c4dad4-0f9a-3eaa-9eaf-cf196e49a9fa | -11.19442 | -45.04387 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| aa17e359-9320-347a-8c3d-aa5158680564 | -7.5802 | -61.37839 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c747e8c0-32c8-3f5f-91f5-7bf31e6173d3 | -12.09086 | -45.7519 | 2026-08-31 16:50:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 211bbae2-ea90-3516-a59a-95d7777972cc | -11.19645 | -46.10118 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 9fcb807c-b9e5-33c7-bfcd-01a0fb65fab7 | -13.42217 | -51.38248 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e421a060-bfcd-3a6d-8468-a36e16e94b7b | -9.64791 | -46.05943 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 425bc4fe-1b6a-3822-b250-fef7020e1c7a | -9.6819 | -46.54076 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 99d48c04-3f43-3f31-8378-65318567fa3d | -8.7372 | -46.46162 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8d3c754f-310f-3cc3-918c-de5ce4e2f547 | -9.15968 | -59.53846 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 3e2a9caa-4cc7-305d-ba80-1bb67f39b3f5 | -9.39791 | -51.65983 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 61245712-5c75-3dc5-a507-391d18002074 | -5.59127 | -42.32041 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| ed6b2cb1-9b1a-30fe-b3b1-a1194d5bb097 | -7.24988 | -39.21273 | 2026-08-31 16:50:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 3cfef06d-4dd7-3f04-a3c2-9a82f1fff5de | -11.21639 | -46.09421 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 048b614c-a23a-3bc2-af77-07eb7922d5ee | -8.63201 | -47.46538 | 2026-08-31 16:50:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 184e0a3c-b62b-3331-8b49-47df26f17eb2 | -7.98606 | -44.35175 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d040cb8c-7599-3eef-8cc4-d9f8c2b15277 | -7.56024 | -49.68479 | 2026-08-31 16:50:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| eee4fef9-623a-395f-802d-24c32f5d65cf | -8.14935 | -45.46868 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2adcaa9d-46a6-3a3b-a592-c469c7df577a | -10.07745 | -45.86219 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2c882c03-d431-3a9c-bb2b-696bae4d2b79 | -11.21839 | -45.32479 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 44bb533a-3530-3321-bd4a-2938342d4f0a | -11.63557 | -49.41732 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 17be33c2-258c-3cdf-9e9a-4fe505aef12f | -9.42429 | -45.67899 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 92972732-baf2-3071-8bd9-443ef211e45e | -7.51973 | -60.4819 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 74778047-6d5f-3f12-b868-ce135be8fd8e | -5.59246 | -42.33113 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f34eac5d-0426-3350-a424-616c80c9b3db | -11.69531 | -54.60713 | 2026-08-31 16:50:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 91c7f076-0bb4-3e96-bc02-fe3fdd0b27b0 | -7.99528 | -44.32758 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 92903e88-45e9-39c5-94af-798ef2e42ff8 | -8.39431 | -44.98687 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 671fc5e3-f7af-3d29-abb1-b664c7544417 | -6.40609 | -49.92669 | 2026-08-31 16:50:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 784a9b6a-e537-3886-85e7-d2058847ed2a | -12.10883 | -45.8426 | 2026-08-31 16:50:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e8e3322e-5361-3274-a9ad-4edf8ac654f7 | -6.64693 | -53.18213 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 537989eb-1083-302e-a9e6-77c719ced571 | -5.62774 | -45.57316 | 2026-08-31 16:50:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cab8b623-4840-3420-8aca-57c7dd5253f9 | -11.71034 | -47.61552 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 89f8c7ea-c8be-3ce3-9384-c9f642842b7f | -11.23456 | -45.37972 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d6f2400d-767d-322c-a887-b8e6a08ead25 | -11.20673 | -45.09696 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| da34fc5b-512c-3c36-889c-dbcb663db1e0 | -11.19097 | -55.10894 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 09f1730d-21e7-3c4e-ba32-3c6ed7ecff7a | -8.94192 | -50.1965 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6be60642-ca7c-3c73-86c9-b1dae2aebfbc | -6.61269 | -48.69706 | 2026-08-31 16:50:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 72a8d2b9-88f4-3354-9601-c14c6c4a234c | -12.07339 | -44.99001 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 32fc2cdc-22ea-380c-9c68-e3beb5c16ee3 | -11.93359 | -45.06747 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 56b2dc4a-9f41-3cb6-8baf-c34167bcbce5 | -7.41427 | -55.15879 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| de6d3b1c-fa96-3d13-9cf4-93194fa2290b | -12.09449 | -45.00792 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 22c346dd-57af-3549-958a-6f24bd9f79b6 | -11.48593 | -50.28139 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 59efd20a-3f5f-3ec9-a894-58dd72873d7d | -8.49617 | -45.5311 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2ea1e09e-48d8-3a44-8bff-11a0b2aad412 | -9.57257 | -60.8376 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f0dd7c2e-b030-3683-a33c-30442f9da485 | -10.34592 | -49.97171 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0c5f98e6-9cc8-3d2a-9ee6-a98accf4bd74 | -10.95905 | -48.40629 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 547a3507-c738-3c4a-9518-b1de5034106b | -6.81532 | -43.53644 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 73b45d93-09f5-34da-9e05-9639eda6d449 | -13.82731 | -54.02913 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a154c061-966c-3616-9536-11249a61240e | -7.98393 | -44.28357 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 4c122710-a0c0-388c-bf2b-804ea75b87a8 | -7.64533 | -46.71745 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d82b8700-1cd0-312b-b768-ff45c921126e | -11.2281 | -45.09339 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| faf1b3a2-f3f2-353a-83f0-447f1cd82be4 | -11.25252 | -45.13155 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 435dedf0-eefc-32a8-90b6-0ff1a6e7cf9b | -13.47152 | -51.40819 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 882ed559-208c-36cd-a1d4-33fd5426bdae | -11.67338 | -47.61779 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a5fe66bd-84c8-38f0-9825-09eff94fb6f1 | -10.12312 | -45.83475 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8dff0fa4-cb31-3e06-bd56-afc806d5266a | -13.40642 | -51.66268 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6cee9134-7f71-3cbf-aa29-300f08288f22 | -8.08789 | -45.45683 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eb3157f1-850d-38ca-b6c7-61d7c085beda | -10.02217 | -45.56694 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 476b6c43-3b41-3dae-8705-31da228be6b2 | -12.10384 | -45.00148 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8c96f5c0-d08f-35c9-bf51-4ffa89307071 | -6.61523 | -47.63549 | 2026-08-31 16:50:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3cd39299-e28b-3dca-ba12-eab19736cf18 | -10.85704 | -45.32988 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 11601c7d-c9ae-3a66-9e94-7ad250dc8914 | -7.96216 | -43.86095 | 2026-08-31 16:50:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3450eb18-55d1-323f-a1d7-75d8d553a401 | -7.63235 | -44.92554 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 5f03874a-c4fc-357e-966c-7bbb4f31a7e0 | -6.85498 | -43.82679 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README165.md)
