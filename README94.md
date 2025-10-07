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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f50c8030-57eb-316f-a52b-e3861a1dd84e | -11.04002 | -50.92062 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 2f359b6c-99c8-3141-bdc4-86a5eba96906 | -11.04254 | -50.92366 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 5f70f2c8-223d-3828-a326-88e11d235182 | -10.88118 | -51.02963 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| cc86fbae-95b0-37df-9f15-665a1f971365 | -10.45799 | -50.40995 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 57448f96-2a31-3f97-a809-c22012921e03 | -9.9083 | -60.1987 | 2025-10-07 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c1d4b8a-ae76-3c65-adea-b3a52676be75 | -9.02237 | -50.69085 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d29e683-34d7-3117-abd9-c6eb4923fd2b | -9.61682 | -57.19822 | 2025-10-07 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa7f22fd-711f-3ed3-819a-d23e78ba43bb | -10.39789 | -50.2986 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 19bcaa2c-6675-3cdc-b1ee-4e07bf4fef8b | -10.31936 | -51.45407 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb42d214-dfd1-36e4-9202-636ac6574aa8 | -14.92631 | -46.80507 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e04b91cf-5137-3b57-8285-ec9cead82632 | -14.75171 | -46.01748 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69673e18-e416-3a22-ab36-dbbe1ce9b555 | -11.0461 | -55.41496 | 2025-10-07 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c95a0dd9-e4ed-3018-a248-e358a765ae98 | -12.01935 | -47.78845 | 2025-10-07 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03a2851a-bad4-342a-90ae-6b505e147ca5 | -10.30285 | -50.40566 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6218d45-8a9c-3aef-adb4-555f625447fc | -8.97189 | -47.4935 | 2025-10-07 04:57:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 81f4e270-7072-30ab-9c1b-cb28fc00041f | -13.22037 | -48.46363 | 2025-10-07 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9a6f8340-2bd2-3408-97a8-f67c509fbfd1 | -13.70618 | -48.08018 | 2025-10-07 04:57:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b0ee572d-6550-386c-9fee-cf93e9a84d1c | -11.94612 | -46.4442 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d19bbff-f6f3-32d9-94ff-dfb23d1ab7fa | -14.64949 | -48.36112 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f190c864-5109-3b22-bafd-1e89ebb3614d | -8.17616 | -50.2963 | 2025-10-07 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4799acb8-a84d-35f0-8ba5-e86006c9ed64 | -12.61757 | -44.75131 | 2025-10-07 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbddea37-d418-3af9-ae85-e403d7481d46 | -12.90066 | -54.73862 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bc4b5b5f-7f19-3831-ba7f-14889f320aff | -14.92678 | -46.80128 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6eed4f4f-b3b4-32f0-922b-8c68f7c621e7 | -14.90516 | -46.83998 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d7921c9-637b-34a2-86f0-a3efcfb299a5 | -10.41919 | -51.63784 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9850cf5a-b3c3-301e-b8b8-95e3279fa7e4 | -10.33308 | -51.23491 | 2025-10-07 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 776c0302-d342-344c-822f-ac1dfdb0cacc | -10.42542 | -50.30262 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c773ad99-c43f-3853-81aa-2538c6ce5fd0 | -13.32733 | -47.55964 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0e61141-b200-34f2-b70b-4e00bc5a94c8 | -8.61928 | -54.97274 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 852c1d8f-8155-37fb-afda-f6a36821ceb1 | -13.67988 | -47.33852 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdb9b95f-afbf-3dd1-8b08-70ce79016ff1 | -14.75846 | -46.0565 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22f2adbc-de46-3db7-9db6-b5ec674337da | -8.74635 | -48.87058 | 2025-10-07 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 062c1d69-b01d-3f5a-9a8b-ffcdda76ac38 | -14.28903 | -45.85246 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c6f55bf-4940-3a62-9442-1689fe068eeb | -12.30022 | -55.10703 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d558416-3988-35cb-8cac-a9b85b30245f | -13.28304 | -47.17109 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46f305ae-5ad3-30bf-a824-0cf06c2e7606 | -9.33891 | -54.52456 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce272a4f-b6ad-3fe2-86b6-86a956d61666 | -15.60471 | -47.29308 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 26d2a88b-f546-34c7-ad86-e47857cb85ea | -15.2085 | -46.37603 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74e93883-3574-3fea-9e25-69a93a1a29f5 | -15.20214 | -46.38322 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 508b6ddd-c35f-3e75-9876-7e8813dfc12a | -14.93285 | -51.43232 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f57847c-1960-3ae9-b164-ed633b4e2294 | -8.14821 | -62.82954 | 2025-10-07 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93f770ee-236d-32c1-b2ad-12ddf3821b67 | -6.8215 | -63.08137 | 2025-10-07 04:57:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96e0a226-f5fb-3701-b6bf-e13a94a83a04 | -15.57987 | -47.26621 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d0237c8-dc47-32bc-b075-c41cb23d11b3 | -12.90011 | -54.7422 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 79bcf388-8b31-3d28-bd1b-ad2669775180 | -8.50066 | -49.13153 | 2025-10-07 04:57:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bae082fc-8fb4-39a6-9e09-10fa38536062 | -15.16945 | -52.76874 | 2025-10-07 04:57:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 700a7952-78b9-3d6f-bae2-15a4cbe64bae | -13.33623 | -47.77 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d25bd95-854a-30b5-a436-17c01f36470b | -10.07763 | -50.52444 | 2025-10-07 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2048b6ac-ce6e-39a0-b375-55b05674a408 | -12.16241 | -51.43887 | 2025-10-07 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 919fad29-23f7-3edd-8360-f4a9c018f6d7 | -11.80769 | -45.0476 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3e4f082-8600-3202-a1c4-577dbc5bbfbd | -15.26543 | -48.0592 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0109c63b-6fca-3485-aa01-4f850643e5bc | -13.32588 | -47.55802 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3b0e1c0-8ffa-3f8a-b71e-8cef6f94b944 | -6.82207 | -63.07816 | 2025-10-07 04:57:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42122a2e-e9bd-3723-8c99-9805c8a7a0f4 | -15.38914 | -48.00471 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 130abc1d-d807-3967-bd6f-16753979e66a | -14.92491 | -46.80797 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3afc1de-5ece-3a0c-8e9a-4503002d14ad | -14.6199 | -52.48994 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08a20e79-2780-3ec9-8571-03e62c301cf1 | -10.31871 | -51.45841 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8aec9f3-7d1d-3673-9a20-95efde012e32 | -7.93991 | -63.71137 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8beb69e6-e990-3d13-942f-d22b9c5bc08e | -10.26724 | -44.38117 | 2025-10-07 04:57:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4c7feff-d074-397b-a51d-f39df2d23b0f | -9.61631 | -54.31442 | 2025-10-07 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b26fd679-3cbd-3e1c-b6dd-ecddc663fa53 | -11.94775 | -51.4833 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3978b739-f7ca-345d-8e4f-6ad85c2f027e | -11.93972 | -46.45288 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 649ac142-ba7b-3e64-90e6-822369e62b77 | -14.71363 | -48.35056 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6456e293-a57c-3b22-a90a-8cc9f3c4fc7a | -10.92237 | -47.07896 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 565770cb-5d4c-3369-a6de-14c2d585c833 | -10.19391 | -46.02988 | 2025-10-07 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce3c5801-a439-3498-97c0-cad56ce3961a | -14.28509 | -45.83707 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb1dabb6-92fe-361b-a955-a3fa89974dce | -14.73931 | -46.02719 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6f1f74da-bd21-3cca-a0c3-2566011dfdbe | -13.36666 | -47.23421 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 063c4370-1f9c-3292-852d-0dd7108c0cc7 | -9.32237 | -62.41072 | 2025-10-07 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2019521e-251a-3581-a8f4-f99e01d46081 | -10.95523 | -51.18458 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65e7e5aa-42b6-3074-8a83-3db7afec7554 | -14.93034 | -51.42167 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4253b876-35af-3799-b261-7cb848b249be | -14.94466 | -46.82299 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d96a1f32-67e3-3967-abaf-bbcf16a4503e | -6.86378 | -59.96707 | 2025-10-07 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79150aa5-1a2a-3314-ac6c-371e859c55ba | -13.71156 | -48.07598 | 2025-10-07 04:57:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b27b703-77ad-3168-b97f-fff591d0c15d | -12.91285 | -54.72594 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1ce8dc8-fcae-32ce-a324-4ff415ff45a1 | -11.83597 | -44.91375 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31a827d8-6db4-342b-b83d-f160aa6f7af5 | -7.51382 | -63.4358 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46cdd904-6bf5-323d-a23f-69a00bc8ca5e | -8.62314 | -54.99122 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d469a495-8a09-3d43-bb60-ddacf8c99431 | -13.68764 | -47.95926 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bfa2bf4-17ef-3782-96eb-c48d3d5ea69f | -13.59252 | -48.6915 | 2025-10-07 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b04bd6db-68bf-3449-a3f6-4d58b4590d6e | -11.9401 | -46.44989 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 718a5361-fab6-3b41-ba18-0265d98b8a33 | -10.39307 | -45.37749 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ed54352-8c3e-3d93-b37f-78eee728ead3 | -10.38289 | -50.29451 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbaade2c-07ca-3781-bccd-a576b0452525 | -15.3622 | -47.30293 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4aa60881-d66d-3832-97f9-5931f1ae9540 | -15.60271 | -47.29482 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47b0db76-0dc4-3f93-a62d-f08da261c772 | -11.84813 | -44.91978 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc22e769-50fb-3b42-bcfe-023c025f9eeb | -13.6883 | -47.95409 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 533d3f76-7920-3bb7-ab02-9cca68193ac7 | -11.50365 | -44.97489 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7cde907-a3c7-3ea5-9b96-16bf74d6f389 | -11.29037 | -49.99593 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39b84206-4fc2-39ef-876b-090690f34377 | -9.6694 | -54.99162 | 2025-10-07 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5995a54f-36a3-3cec-a233-861fc2e40f99 | -13.22782 | -51.68209 | 2025-10-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93200fe0-2930-3202-b39e-58f69cd28885 | -10.3861 | -50.29688 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 096db457-2410-34dc-a73a-87985f837b6a | -11.67602 | -46.34538 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b81c2c0-1fe5-3d8f-9bc6-f2174bc8bdda | -10.41436 | -45.3854 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f03a96ad-fdf5-3fa0-9254-ab88713e5e11 | -12.89791 | -54.75646 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4df68ba-ca18-38f0-9f0b-677db18ad1bc | -11.86717 | -56.88596 | 2025-10-07 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0a09bac5-bece-34f2-adf7-56d1c35d2610 | -13.23952 | -47.23747 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69d7f17b-a716-3cf9-bb61-8746a200eef4 | -9.50655 | -51.34504 | 2025-10-07 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d117fc5-6685-39cd-8765-a2d1596b7ee1 | -10.32403 | -46.932 | 2025-10-07 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ff7e5289-28b3-388c-8e3a-5d708a5cd828 | -9.78634 | -59.96367 | 2025-10-07 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README95.md)
