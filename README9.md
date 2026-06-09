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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c092344-bf3a-36eb-91d2-4993ab6b543d | -11.33601 | -51.39408 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8be400a-0458-3cae-bbf7-3e4e6933da05 | -13.496 | -56.57195 | 2026-06-09 04:49:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c9448db-b103-35ea-8be6-32f9260ae338 | -12.36115 | -47.89146 | 2026-06-09 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4644656-ecc9-35cc-902a-ab032aa02e8f | -8.7142 | -47.92057 | 2026-06-09 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b59d92f-a6c0-3a9e-b175-29baa2511ec2 | -12.46473 | -51.46258 | 2026-06-09 04:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e4391fe-5a8d-384a-94ba-a79100d15748 | -3.96073 | -43.11937 | 2026-06-09 04:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cf1b0d1-80ba-324d-9b7b-dc952faa8717 | -11.55021 | -52.8077 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c229a01f-3910-3cce-bd16-a24eeecc0dcc | -10.57343 | -57.31825 | 2026-06-09 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23c2aa23-a520-3be9-a5f1-fb9453029080 | -7.59757 | -46.47011 | 2026-06-09 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4a132f15-545f-3b23-904b-6c95d1620756 | -9.76525 | -47.43932 | 2026-06-09 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f07277a-fb93-3495-809d-40d56256a060 | -9.20954 | -58.06764 | 2026-06-09 04:49:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc9ca1fa-19bb-3585-9379-0cd80503ff82 | -10.64754 | -49.38668 | 2026-06-09 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b92f2a80-4a52-3c4f-a87e-5a6aeaf38785 | -10.16269 | -51.65645 | 2026-06-09 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 934d63d2-aaa1-39b5-bbe9-533304665864 | -7.59956 | -46.47361 | 2026-06-09 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2a2fe4f-1a71-3de3-a503-5b34cca9cf2b | -9.76947 | -47.43575 | 2026-06-09 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51d0ed1a-3e32-30de-bd8f-0c53779899de | -15.62684 | -42.48847 | 2026-06-09 04:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2278239-8217-3fb9-9a93-bda0b678e3e0 | -9.30269 | -45.48397 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8c3c6fc0-ff4f-3115-8440-36c27901f8d6 | -7.59587 | -46.47305 | 2026-06-09 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ce0ea44-6fd5-379f-89fb-a55cf3e3f29c | -9.08044 | -50.60471 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcaf76e7-963b-3aca-81b9-e6c4461d78ae | -9.212 | -47.33663 | 2026-06-09 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e0dea0b-4d67-327b-9073-8b29a5b96c83 | -12.05299 | -49.76498 | 2026-06-09 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c95b2a40-f67b-3e07-bdb4-6e6b87d2f098 | -12.43345 | -58.47063 | 2026-06-09 04:49:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 72f16204-d1e3-3aed-bfb8-f3ee216c8da7 | -10.57449 | -57.32112 | 2026-06-09 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f246979-2e7f-3bc3-9910-735087ea5e92 | -11.54301 | -52.78697 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7439f82f-7bab-3ada-8f82-789f671d6421 | -9.07434 | -50.60014 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5ae507a3-a2e1-385f-a51b-56f5d9c4b195 | -11.33267 | -51.39352 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d273288d-308f-3fd4-ab07-9ec5bf4a5820 | -10.64361 | -49.38976 | 2026-06-09 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 0d975de5-3c72-3447-aca9-68c6e3a3652d | -10.15085 | -47.64862 | 2026-06-09 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4687d289-3263-3f6e-a146-60db57bbb70f | -10.2317 | -47.42776 | 2026-06-09 04:49:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a583609-a5a6-3ef9-9ddf-4f6f5e74bb64 | -9.62245 | -49.02376 | 2026-06-09 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d596acf-9065-3817-bc6e-16495b9be401 | -11.26678 | -44.52859 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a2e40f8-6671-3149-877f-673b0ab9dd5e | -12.03586 | -47.80096 | 2026-06-09 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ed8e2af-78f6-3ed7-bfd7-0c1d2a8f01ac | -10.42527 | -49.4481 | 2026-06-09 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a35be862-4a88-3d0a-8885-ae36a3fe4764 | -10.85507 | -53.73751 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6653320a-497f-371b-ab85-153ecaa0a65b | -11.55366 | -52.80827 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d2fccd9-c996-34fd-b6cd-8eb5551ac974 | -10.59558 | -53.47539 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8567ede-0713-3b72-a665-907f3f5f925d | -9.07489 | -50.59664 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3168e20a-330b-35b3-82c3-12f4c08ec5e6 | -9.29619 | -45.47242 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 84243698-abe0-368f-8090-f36d797b920b | -3.9564 | -43.11872 | 2026-06-09 04:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1039826-1b6d-3ae4-8b05-b4ad1459f110 | -10.57001 | -57.32023 | 2026-06-09 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3703c99-5165-3ffa-a749-1d6406edb384 | -7.37651 | -49.85582 | 2026-06-09 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89d0eed1-9e7d-37ee-ae26-6e4e98b37f23 | -10.45471 | -48.12009 | 2026-06-09 04:49:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 540e12b7-9265-3189-94e6-ce61f855d565 | -10.6481 | -49.38306 | 2026-06-09 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 430781fb-e474-32f4-8c68-9c201d78c1bf | -13.96031 | -46.18333 | 2026-06-09 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3209b9cd-82ce-3811-9695-ffbd6f4dda26 | -11.05189 | -56.92697 | 2026-06-09 04:49:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 997b4e87-49b3-39d4-a197-04367864dfd2 | -9.29219 | -45.47184 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d20e7b95-50f4-3bb5-bad2-c3a9eb22740b | -11.55457 | -52.78114 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6868874e-eee8-3e12-a37a-bd8dab3396cf | -11.54645 | -52.78754 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5ec2e5eb-f351-36d5-810a-46bf11165b83 | -9.22205 | -48.56496 | 2026-06-09 04:49:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e36fcad-dbe2-3afd-be85-35b707a0b270 | -9.30994 | -45.49031 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 54160ac3-0576-3344-a3a7-98aed9e73ccc | -13.95979 | -46.18706 | 2026-06-09 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7b5219d-87cd-3053-9009-35b4f7dcb03f | -10.91898 | -54.11432 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39d4d39e-9832-380d-a3b2-edc3744af339 | -10.85799 | -53.74227 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a693732e-b7b0-3824-8a59-f813dd80d825 | -11.54019 | -52.7826 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| be99f4d6-874a-3109-b472-54916311d61b | -11.66462 | -47.94474 | 2026-06-09 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb67176d-2f62-3f48-8141-0d8247d6bfe2 | -9.14346 | -49.83961 | 2026-06-09 04:49:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 219dee6f-e24c-3857-8454-9a025e50821b | -9.07322 | -50.60715 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 563e3f67-cb44-3ae6-9d81-c2c844b86a52 | -9.33886 | -47.90838 | 2026-06-09 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 998f3696-6217-30cd-a430-368406b00199 | -12.36415 | -47.89627 | 2026-06-09 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 64992c8a-0577-3cf4-821e-828845a3c33f | -11.55114 | -52.78055 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9793d6f2-6bef-3e23-b320-f7a3af745333 | -13.25278 | -44.3968 | 2026-06-09 04:49:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 65574ad1-be5c-32bb-b65c-44b03c96ca74 | -9.69416 | -47.69553 | 2026-06-09 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c1ed772-0e24-3fe0-9240-1f41bd2c535c | -14.30187 | -49.24545 | 2026-06-09 04:49:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5abf6d91-d0e3-3a60-81c8-cc455b82dde9 | -13.25775 | -44.39928 | 2026-06-09 04:49:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a1afc5cc-ca0a-3241-b276-8702b48542d6 | -10.17558 | -51.66226 | 2026-06-09 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d75f5e0c-d4f1-3a64-b675-9ae63f6f2048 | -13.96388 | -46.18755 | 2026-06-09 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 560d9b30-4f3c-37f9-8aec-048d23c6d9eb | -12.43509 | -58.46708 | 2026-06-09 04:49:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4de45f8e-7606-319b-a024-fa39a845adb4 | -15.17705 | -43.85143 | 2026-06-09 04:49:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e5531d4-871a-319f-9998-e93edf2d60eb | -9.31394 | -45.49087 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b8964ca1-caa8-3693-9f8d-71608dd221ea | -12.05356 | -49.76135 | 2026-06-09 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 719d672d-51b1-3a3b-b1c3-2db4d12c5b1d | -8.74677 | -49.46694 | 2026-06-09 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f07cd27d-99b0-3d04-8813-c97f39c613ed | -13.80967 | -52.90175 | 2026-06-09 04:49:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9a000a5-1584-3f63-aab9-928444261ee6 | -7.89678 | -47.09452 | 2026-06-09 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b5814d2-fed8-3ff2-b656-2a40d8d2244a | -9.89284 | -47.85909 | 2026-06-09 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5048765c-8e73-3299-884e-3fbc63c42c14 | -7.6002 | -46.46927 | 2026-06-09 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 37b909ad-6e38-39c6-bb4c-09d327a1b647 | -8.74287 | -49.46994 | 2026-06-09 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2854fddb-fba9-3b7c-b267-0b5c750513a0 | -11.02406 | -44.31897 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 815546ae-91f3-3b0f-9981-9aceefbefe0f | -11.47379 | -57.11411 | 2026-06-09 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68aea1b5-b53a-3306-911f-da3d8020db9a | -14.39844 | -43.80346 | 2026-06-09 04:49:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64a9ce70-4b2a-35a5-a31d-c3990bfcbf77 | -9.30669 | -45.48453 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 275555bb-684a-3b2e-ba28-9713f86606c4 | -13.68717 | -52.96534 | 2026-06-09 04:49:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5a55deb-3fe2-3f19-8595-26da37ccf85d | -10.59362 | -53.47802 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21045b78-7c24-3279-9533-68b09b69b0f7 | -11.26778 | -53.97167 | 2026-06-09 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e28122d-7e37-3226-9080-8c0ee65cd202 | -10.64472 | -49.38253 | 2026-06-09 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 860ee3d3-3518-34de-92c0-d81ef79bed44 | -13.36505 | -43.20661 | 2026-06-09 04:49:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0b459fa7-9639-38a7-b715-6f74c9978744 | -8.71479 | -47.91672 | 2026-06-09 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a79a2806-b864-34ee-b7b5-0a365ed17535 | -14.30104 | -49.24219 | 2026-06-09 04:49:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1beccc1-c1c4-3e10-a0ab-6658d025c9ce | -12.43791 | -58.47787 | 2026-06-09 04:49:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4ad03eca-daf6-38bb-9f63-85e216ac81a4 | -7.70288 | -49.34584 | 2026-06-09 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8502c4cd-029b-3949-b241-e609c8f582d6 | -12.03561 | -47.80334 | 2026-06-09 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c5175f35-1ba4-3d69-9503-3f554f66e7a7 | -8.97425 | -47.9831 | 2026-06-09 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cf435898-b997-35ae-9128-8566df74cce1 | -12.43977 | -58.468 | 2026-06-09 04:49:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c0ee876-cd9b-3ae8-a967-05937a042ec5 | -12.48269 | -46.26809 | 2026-06-09 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 637c10f9-6a2c-3fec-9470-fedef180bc4d | -9.07655 | -50.60768 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d351383-2646-333e-8850-5656f2b51fa4 | -9.29944 | -45.4782 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 884ca5c3-5e32-3f36-b2d7-bee3e8e72f72 | -11.62463 | -55.19114 | 2026-06-09 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ab7aed6-4a3f-3eb3-aa5e-8aa129fb44d7 | -12.47159 | -55.13309 | 2026-06-09 04:49:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76ff7b2e-7fb2-3bc0-b9ea-335fab39f641 | -9.29544 | -45.47764 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c93584d-e4da-3ff4-b99c-406c1f75ce1a | -10.77184 | -54.09971 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c25a295b-2bba-3d9c-ab10-840dfdca08a0 | -9.22548 | -48.56547 | 2026-06-09 04:49:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README10.md)
