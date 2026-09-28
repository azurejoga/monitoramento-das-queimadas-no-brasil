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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 354bf486-dac5-3edc-87c2-94d60b2ac3b2 | -12.76719 | -54.03654 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 171268bb-fa7c-3073-8ff5-8656bf2c0d8e | -10.01824 | -50.24189 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 42e57c4a-35a6-3c15-8349-cabdec21999e | -10.54871 | -57.43768 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 92607f98-872a-37f2-80df-de4d15368e1b | -12.11802 | -57.16985 | 2026-09-28 17:09:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 9860e90f-73db-35f3-ab34-213484c02769 | -7.59659 | -55.70308 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6d7bddd0-86a7-30f8-bd62-3d0e888bc822 | -9.07888 | -49.87566 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 13f2fae4-fe07-33e2-9d07-9337d6e767ea | -11.17689 | -45.134 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5c28d888-9a24-340c-9b4b-833c81a39954 | -8.23782 | -45.40294 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b494040f-7bdc-3215-afda-9bdb0c8b57e7 | -9.50773 | -46.35601 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 5243a10a-c8d5-360f-a2e4-34765282f0d6 | -5.25213 | -44.933 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0dff2dc0-98d9-34c0-8ddf-1acd8aeafd0a | -9.32823 | -45.35834 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 54f777c6-df87-3f64-bc9f-d60b1399c0ce | -8.52738 | -45.85328 | 2026-09-28 17:09:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8dc1685f-c2a6-3880-8ae1-a391e7a49ce2 | -8.2671 | -54.70541 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ed21e921-0a39-3b8f-8786-3e1d7c7358a5 | -6.64808 | -55.09819 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1e550b1e-4b7a-3a29-a1d6-a2c5eee4ed3e | -12.80641 | -54.00508 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f141b04a-4df2-31ec-811f-80d67450c187 | -11.20415 | -44.76249 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 87676201-fab0-37c6-a900-398c094a96f1 | -9.77124 | -44.83209 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a22241f1-59f7-3a3e-9439-f330b17abe31 | -8.64834 | -45.35025 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.9 |
| d05d9abb-d43d-38fa-bb4c-00b9660141f7 | -9.71408 | -47.7641 | 2026-09-28 17:09:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 83a40e05-d80d-3e61-a41d-bd6124190de6 | -11.14468 | -48.31798 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1ba2b1b3-5f6c-3620-a785-a1ad5c60518a | -8.24275 | -45.46588 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 1c2cce5a-919d-34d4-abff-52615a5dded1 | -12.07658 | -48.54752 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b29646e6-f1d2-353c-88ec-4a1168e69450 | -10.9599 | -50.67046 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 84df67eb-e25a-380b-87e1-e778b4252a78 | -8.28873 | -54.73353 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 350b2b7d-76cc-3aec-8644-2d5e4ed1488a | -11.52333 | -47.39557 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 40f12868-63e0-32d9-af7e-01ac2a4ea783 | -9.49622 | -46.35361 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| df9fbd72-1d6f-3af5-ac95-74fb1a1d71d6 | -9.134 | -56.5612 | 2026-09-28 17:09:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d11d19c7-b7d1-3d1a-8d78-8ab7bc837cf5 | -11.57114 | -47.39422 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 684801c3-8a97-3c12-aaae-181d8a3af903 | -9.76636 | -44.83673 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| d0242274-42e9-31cd-923e-79b8c3d68154 | -6.1651 | -52.82996 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c3f2e16a-8bf9-33b5-bb1c-a7760e0eb32f | -9.0421 | -49.63163 | 2026-09-28 17:09:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 43101351-2369-3c5e-b032-c447415124ee | -9.8147 | -46.28468 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 96bf7ccf-3fe1-35b0-97fb-259c8f8044e8 | -11.18267 | -44.79694 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 5e190288-0558-384c-a679-582910e59aa1 | -10.12355 | -50.19661 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 8cbbd445-7287-3134-9ce4-581b58963037 | -10.73908 | -48.76675 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 0792d8ce-f81a-3ccf-955c-1e140e8c06f4 | -11.07158 | -60.68697 | 2026-09-28 17:09:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 08806c0b-fe8e-3054-9a2c-d2dc793a71ee | -7.38123 | -60.60971 | 2026-09-28 17:09:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f860e21b-c555-35d6-b8ed-ecd7712e3645 | -10.25723 | -44.59894 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77ee9137-cc22-3531-996c-05b725f2c287 | -7.36863 | -45.40423 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9bb3717d-c8d9-301a-8a4b-fd509b739b4d | -8.86277 | -50.65661 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e7cf68cd-ef53-389e-b41c-6ef93c077843 | -10.91254 | -43.8629 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8d46208a-e17d-39f0-b02c-52d296c4fc75 | -5.42155 | -45.89008 | 2026-09-28 17:09:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 08190119-c0e3-3ca3-9ef4-446fe794361d | -7.82968 | -55.13316 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6e1075d2-df27-3cc5-9296-2ef4dde616e3 | -10.20105 | -46.68988 | 2026-09-28 17:09:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 191c84ac-f1d3-3a51-82c5-58364db78bf9 | -10.60754 | -48.71054 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fc8deaed-95e1-34ca-a5d8-7716f15bd2f5 | -5.73235 | -43.28026 | 2026-09-28 17:09:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| ab520bec-c69b-3f20-827f-dea7c42a3c6d | -7.98829 | -43.25962 | 2026-09-28 17:09:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| cf78c3f3-e0c6-37f6-a12b-a89bd237b7fd | -9.17662 | -60.77979 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5a9d7a99-f24d-3b10-a43e-36956d31bd72 | -11.85988 | -47.08248 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 339d61ad-89e4-36ec-ae69-fb8e6ef012ac | -7.14897 | -47.55068 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ebaee1bd-9978-3969-bb09-a79a21f13d77 | -12.28439 | -50.26267 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4046070f-8551-3909-bb73-c0967a148e91 | -11.11595 | -51.18277 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9a21c700-b79e-3bbf-9011-f95a13074923 | -9.491 | -60.39663 | 2026-09-28 17:09:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 9df33d1e-e757-3845-a03a-5f1ea80acd82 | -10.8252 | -57.19705 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 6e517d2f-f902-3149-a99a-7a7a5dfe06cc | -8.97723 | -44.16149 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c24f693c-96e8-38e9-bf94-ce8f282b1d9a | -9.40143 | -46.39714 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 251ceef7-9c05-3f86-a226-1e7bfd777cf1 | -8.22465 | -45.45902 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 81e52965-7ec3-32b4-b7fa-e03e75abc9d7 | -10.92869 | -50.66653 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 65cd2cf6-842a-3cdd-879a-f5fe7d3177fb | -9.45631 | -45.96389 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0803cdff-7094-3462-bacc-8db29f96315a | -6.51857 | -54.96269 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| ba130f55-f59d-3f44-a3db-8099ecf5f360 | -10.21556 | -49.99995 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| cbf8e225-83ca-3473-8f09-6516d887169f | -9.44507 | -41.82883 | 2026-09-28 17:09:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 92.3 |
| a4ff2ce1-4c88-33f3-a2b0-01e110515aa6 | -12.07937 | -48.53906 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2ac00f0a-cbac-336e-9743-634db67832bb | -9.79288 | -48.21933 | 2026-09-28 17:09:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1e7054ef-e626-3a58-85fc-15a38791611f | -11.90774 | -49.99106 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 94b71304-2272-3eea-bd64-8c25dd4c5de9 | -7.31016 | -44.60073 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0df2def3-510f-3193-b57d-a9a1af04dba4 | -8.64566 | -45.75674 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4c1a3de0-2c9a-3cf5-bf96-2cfd1d7289cb | -7.23452 | -44.8458 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9ea76455-7dc7-3ce7-a2b9-77c73d28fd6d | -5.42255 | -45.89069 | 2026-09-28 17:09:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d1d71acc-ed31-3b46-ae0f-d6c3bf0ca8af | -11.54516 | -47.3797 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| dc3df318-6095-39d1-b594-707cbf49e88e | -8.2252 | -45.46211 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7b25fca3-400f-397d-8ab2-48aa707e7676 | -7.69333 | -54.75414 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d6541ba2-07d6-3738-8f88-7c240ea0d987 | -9.07582 | -51.54282 | 2026-09-28 17:09:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14fbe070-60f0-3ca2-8a26-92aab271782a | -10.95086 | -43.87584 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 64a3544a-32a1-3d20-a8b3-f929445ce371 | -12.06518 | -48.54039 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| e216b7a3-c20c-3466-afda-5cfce08a2a2c | -9.28383 | -46.5779 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a922aeb6-753f-3d68-8226-c25b129dddc3 | -7.69215 | -54.76855 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 627a34bb-2d68-3878-8172-3b7d0e33b08d | -7.55898 | -55.01062 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ae89a5c3-a4f2-3826-baa8-7f29c0840365 | -10.27216 | -44.61756 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 8009fa08-b7b2-3c51-bff7-3f47ff36227f | -10.45384 | -61.30214 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 5558a72f-489f-3606-9141-dd19806a7356 | -9.5211 | -46.37613 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8693d1ef-87f4-3ba7-bfdd-9f814669d9b4 | -9.14467 | -49.97569 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 137d7a9d-dea7-301b-a7a8-a13de1cab663 | -11.08275 | -48.89249 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 265261a4-ebe5-389d-aba8-fe249cc48cd6 | -11.02053 | -49.70594 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 53b18f8d-207f-30e7-ab86-a10c1c51368c | -7.56491 | -55.02307 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a35b12ff-bb7e-3434-a5d0-c65cb12c7d19 | -7.36517 | -60.58534 | 2026-09-28 17:09:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2bace90d-5062-3247-9af0-653d87c98665 | -12.39643 | -50.23618 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 160ad2e6-00fa-3cfe-9fc0-8a5065080a4d | -11.84997 | -50.90002 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 06c8859d-c556-3131-a2bb-d9677e273227 | -4.94312 | -45.10356 | 2026-09-28 17:09:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 59aa7b39-db13-3c19-95c7-359675431433 | -6.12736 | -53.05276 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8a190a7c-2780-3c09-84f9-5b2c5f49e6e9 | -6.14468 | -52.79266 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ab16706d-51ac-31ab-9717-b200e6abd5bd | -11.50982 | -47.39838 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1fbd1316-aa27-3b27-89ff-d80cfd3cfc6a | -10.70391 | -44.43734 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 256f86c0-ec63-364a-b351-9e42afbe9bd3 | -9.93372 | -50.24431 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 76319655-a2d3-3460-ab85-09cb915df649 | -11.10254 | -47.31137 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| acb68674-90aa-3620-a260-e33766933947 | -7.28227 | -44.30856 | 2026-09-28 17:09:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0a55dce2-b69f-3b23-86a7-4b0c4142b195 | -11.15751 | -48.46958 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 676138d1-4376-3ff2-881a-c6e5fdaa38cc | -6.3432 | -55.32692 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1dcf26c9-0a8d-3ed7-98e1-1c8dbf32cc4f | -12.14377 | -59.88078 | 2026-09-28 17:09:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8d049082-63ba-37e2-8afe-b5cd8d174628 | -11.45124 | -44.92344 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README149.md)
