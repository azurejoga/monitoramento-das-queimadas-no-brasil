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
| fe0ecf6e-2234-38d5-8509-fda5231247ae | -10.86328 | -53.76828 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f2db453-d0ad-3bc0-9325-4fd0707e712c | -11.13766 | -53.93263 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cac2b63d-556b-3db7-b3d7-9f0f4d00fc20 | -14.41876 | -58.13655 | 2025-06-18 04:17:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc4b8884-671f-33db-a517-fbecc44dbc14 | -7.28043 | -50.00422 | 2025-06-18 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5edf77db-27c7-359f-a99f-c8f106dcd12a | -6.70379 | -42.78555 | 2025-06-18 04:17:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e5503138-c56f-370e-bcf8-cea191e1d2a2 | -11.13695 | -53.93633 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 82e770c2-871e-3f29-be14-6e5da3e8274b | -7.2512 | -44.64371 | 2025-06-18 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26c64b08-e9ba-3ab9-9b3a-7312c7f46f0a | -7.23162 | -43.10391 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7c69b98-98d4-3cf7-ac95-b971b609a501 | -6.14392 | -42.96771 | 2025-06-18 04:17:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 48eb959c-c110-3b6c-a645-3501faf0bac5 | -7.14337 | -46.5519 | 2025-06-18 04:17:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| edf444df-d2a2-3484-971e-1d2d0a53ceaa | -8.72184 | -49.02467 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 715e8319-4152-384c-9489-d7fb330a0855 | -10.57774 | -49.65631 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73ded0b3-d1c6-3ed2-a866-bd879ce72351 | -9.33016 | -47.83688 | 2025-06-18 04:17:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b597a86a-e50b-3217-9a94-6403f089462d | -10.6583 | -49.3696 | 2025-06-18 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c1129e5c-1ba8-39b9-ab45-5a951c94864b | -6.86705 | -44.83839 | 2025-06-18 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1afa5183-8bbd-36b0-87db-de1eca7ef728 | -11.13554 | -53.94368 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| b5897a7f-912c-3889-b67d-7c506b0ce340 | -7.80818 | -46.57285 | 2025-06-18 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f48588d3-dd51-3108-8adf-0fdc11ed65ee | -11.08278 | -55.05811 | 2025-06-18 04:17:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3fcb5262-7d42-3800-8319-508d30832503 | -8.88141 | -48.52256 | 2025-06-18 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db64274a-01eb-3956-9a6c-cc760e291642 | -6.67881 | -43.21941 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| bac1bc02-aa39-3e23-a1b2-c1b0625a744f | -7.2857 | -50.00057 | 2025-06-18 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c763c17c-ca3e-31ba-8b1e-5051e4661389 | -16.68207 | -43.88414 | 2025-06-18 04:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e12c431c-f716-344a-9c0d-28877c66315d | -7.54448 | -45.64387 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 806c4244-d3b2-3f05-a614-569b47845e4a | -17.59678 | -43.19771 | 2025-06-18 04:17:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 457f06f8-aac8-3b8b-8087-3e64e44ff18e | -7.54796 | -45.64444 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dea79a83-7b2e-3621-a527-18ce9e2c7b1f | -10.84565 | -53.77198 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5d91be0-979f-3338-b326-0054a5c30c1a | -8.32986 | -46.23154 | 2025-06-18 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65f0c23f-da29-306d-b51f-5dc1036025b1 | -6.37373 | -43.75577 | 2025-06-18 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6dd74ace-7d83-3b5f-abf2-682e4381f528 | -9.25606 | -50.03565 | 2025-06-18 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1fe7fc9-61e1-31a1-a643-6d9dd176f3df | -7.5451 | -45.64001 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b50cf71f-1b37-3a8f-b2df-a2fdfe4d01c7 | -15.57101 | -47.85651 | 2025-06-18 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 864369f2-73cc-3940-b5ab-037f41cba431 | -6.04347 | -44.04898 | 2025-06-18 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ef06413-56ab-3466-9934-619c666cff55 | -9.458 | -57.85278 | 2025-06-18 04:17:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6741661-a6f1-362d-8108-36c6fe951ef4 | -6.63449 | -41.71245 | 2025-06-18 04:17:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ef8d19e7-e678-3718-8fb5-ef68578ac920 | -7.60991 | -45.55546 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4181d181-d7b9-382f-b940-d1d41a9a35cb | -6.68651 | -43.19217 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9eed1d0a-2019-3276-9d4b-93456b46191c | -5.90908 | -43.44636 | 2025-06-18 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b26aaec9-6558-3e4c-b540-6997364aafa4 | -6.67432 | -43.18313 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ebdc696-df91-3e94-9b9a-aad9251cf473 | -16.5886 | -49.21925 | 2025-06-18 04:17:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 422944ec-f629-3425-adf6-3518f5c6536d | -9.20259 | -49.67486 | 2025-06-18 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 047baebd-1d8f-3716-a843-200fcf7a0d7c | -9.27812 | -49.61826 | 2025-06-18 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3728d27d-d38e-37df-9af1-270cbb96c4fe | -12.0979 | -48.47944 | 2025-06-18 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e690f0d-e34f-3c75-8483-e80c032de00b | -7.54324 | -45.65157 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 81206ce9-1981-37dd-bdab-e2d2c1463c35 | -9.49281 | -56.08957 | 2025-06-18 04:17:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 34f73136-bee3-3eae-89bf-382e9ea79601 | -11.57492 | -44.84154 | 2025-06-18 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b25c5e2-fcf6-30ea-9b7f-41c8eb7fae2a | -12.00362 | -46.48581 | 2025-06-18 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27e5804d-86fa-3ebf-b6fa-f17ade001b47 | -6.12295 | -42.53718 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 1fa86de5-f96e-3e2b-94bf-e17c21456ad9 | -11.91045 | -44.17583 | 2025-06-18 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6598a304-94bf-34ef-891b-2261447a0d4a | -9.10788 | -46.48072 | 2025-06-18 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b41d4a92-9193-31dc-b25e-25a8d38a52d8 | -9.86267 | -47.88846 | 2025-06-18 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e03658b-41f1-39fb-989a-a21bb9326114 | -12.20857 | -49.64804 | 2025-06-18 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f12bb45-556b-3d66-bbfc-f6ccfc352c31 | -7.02563 | -43.55569 | 2025-06-18 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 726fdc93-dce5-37de-a803-4ab7f85a89ee | -11.64649 | -54.14754 | 2025-06-18 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b32c89c2-85e0-3018-ac01-962e7c04021e | -10.23993 | -52.23289 | 2025-06-18 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c682eea2-e35d-319e-97eb-0f6a0c9ea495 | -6.14059 | -42.96719 | 2025-06-18 04:17:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e3ae546d-6ffc-3ad2-86d3-b962f4798b10 | -6.31839 | -43.74662 | 2025-06-18 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f27c08c-7acc-32bf-851c-79552ba1e4ca | -10.87813 | -54.3159 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b93dd29-d7b4-3f68-be1c-8eabff851c8e | -7.23549 | -43.10095 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 27e74809-a640-333e-80ce-0bc7b3eff8c1 | -6.65938 | -43.19144 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| e82e9a38-39c5-34e1-811f-58dd375a515b | -11.64719 | -54.14388 | 2025-06-18 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 157a6514-8118-3f96-a563-22c5655d9804 | -10.9253 | -56.84592 | 2025-06-18 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9c5f33f-d612-3ee8-8813-60da62d58901 | -9.49177 | -56.09502 | 2025-06-18 04:17:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 80b18b8f-336f-3fa6-8349-2a2f3e5621dc | -6.68922 | -43.68759 | 2025-06-18 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 986f1df1-0a1c-3aa1-9ab3-f409e145cce7 | -18.00794 | -49.39691 | 2025-06-18 04:17:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac1dd41a-a5f2-329d-a31c-ca09a6518fda | -15.56748 | -47.85596 | 2025-06-18 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e80e45f4-cd69-34a4-933e-df9e69538110 | -10.35707 | -57.24816 | 2025-06-18 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 374d7a56-6d86-3c1e-a977-4219e40bee04 | -6.11623 | -42.5147 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e807293-d470-32c4-8ad6-984a489e5eaa | -6.41548 | -44.80043 | 2025-06-18 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d984c7f-2c61-3a11-b618-be64973a4b6c | -11.79443 | -43.78754 | 2025-06-18 04:17:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44fd6fd7-f9ff-3f97-8cd7-b15e742c8552 | -6.12017 | -42.53317 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6cc0978d-5318-38b0-a37a-909b351c6e80 | -10.62588 | -54.91661 | 2025-06-18 04:17:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7955b67-fe35-325b-87b2-809d6c888258 | -8.07901 | -43.11267 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7407d834-0342-3d97-a6bd-4dd79d4ce5d3 | -11.13146 | -53.93533 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| af12c5ae-88b6-350d-a27f-770349c0880f | -10.66302 | -49.36666 | 2025-06-18 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c9baff2d-5888-34d6-82ab-cce173b3037d | -5.91185 | -43.45037 | 2025-06-18 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 337edd38-0fc8-3ec2-996b-c91c0fc721dc | -9.88333 | -47.81163 | 2025-06-18 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a73e83df-1179-3681-bfa6-0be10ea00359 | -19.05824 | -48.33388 | 2025-06-18 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab7a8dde-59ec-303f-8827-61944583c78e | -7.60929 | -45.55926 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95b2b4aa-f91b-3051-9118-fa9c4a63a687 | -5.61034 | -45.97439 | 2025-06-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d53df8c-7b68-3e63-b75c-bfa658164dd0 | -9.27688 | -49.61665 | 2025-06-18 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b109ccb-305b-307b-bd42-ee15b76e13fd | -8.0686 | -43.11826 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 52ab97a7-5129-37f3-a9b2-443eab11ead5 | -6.1395 | -42.97412 | 2025-06-18 04:17:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d789abe9-7af5-3a40-972b-841fab436f06 | -9.4651 | -57.85431 | 2025-06-18 04:17:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b1ec4be-357c-3f88-9def-921e56dd96d9 | -6.68568 | -43.04615 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93d07cf3-ce87-3414-86d4-235e7f24e3e8 | -7.21356 | -43.2186 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 658001a7-31c1-3b06-9499-82a8c7a7698e | -7.25911 | -44.63754 | 2025-06-18 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8dba1ce-4005-3f59-a998-bcbedcbf54f7 | -11.3347 | -45.21424 | 2025-06-18 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68ad14c0-7643-3299-9605-2ac575d45e88 | -16.17804 | -44.13089 | 2025-06-18 04:17:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 238c3a29-f86a-376b-9cd6-d311ad43f397 | -6.03229 | -44.05446 | 2025-06-18 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbc8b85e-bee3-3060-94ca-6b2a68b8b23f | -8.23776 | -46.39311 | 2025-06-18 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1def150-9ca3-3b5d-adbd-de1bf1f82377 | -12.00834 | -46.47873 | 2025-06-18 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68c34207-c465-33f7-8941-9509a0ed259f | -6.67936 | -43.21593 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7bda566b-f477-3733-ab9a-94e82b3eee9b | -8.10795 | -45.54948 | 2025-06-18 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb4a29f5-9b37-36f2-8d15-d6a420f576e2 | -5.90132 | -43.45227 | 2025-06-18 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efcffd68-4e98-3774-b505-fe7caacf4efb | -6.23951 | -43.36662 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4cab8da-2788-3855-b667-ac29d2496785 | -9.85889 | -47.88781 | 2025-06-18 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e72d7661-1a8d-30c4-b371-5cb4be9d7871 | -12.20792 | -49.65166 | 2025-06-18 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fac15fce-b090-3730-8743-db121e27646d | -6.6699 | -43.18954 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c7e83125-bd1e-3184-ab0b-40e2a34602f0 | -11.58158 | -44.84262 | 2025-06-18 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52480756-c161-33d8-946a-0ccf40e4e8a0 | -7.94519 | -48.04114 | 2025-06-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README12.md)
