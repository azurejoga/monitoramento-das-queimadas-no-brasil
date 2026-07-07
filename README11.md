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
| 5c2b952c-0541-3608-be2a-844ab5232821 | -5.8066 | -43.80488 | 2026-07-07 04:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f7d6240-9949-3cb0-9bc3-6547a496593a | -5.80462 | -43.80108 | 2026-07-07 04:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3fd56c30-85e2-3e2f-b702-25240de01863 | -6.44004 | -44.57881 | 2026-07-07 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4841f63-8024-3c06-b1ba-586852b93e54 | -6.91577 | -43.70653 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c2b7c6db-67fb-344b-9642-c4c842ec99d8 | -5.75631 | -43.18854 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f11cad9f-863a-352c-aa6e-c4e9753bf080 | -6.93681 | -43.70276 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1195014-842d-33c2-876a-923a270f52c1 | -5.31051 | -43.69032 | 2026-07-07 04:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc100277-ba1f-3f4e-86c6-82031d27087c | -7.90321 | -48.25171 | 2026-07-07 04:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6a8aba2-b7dc-3e3b-8d5f-474d0e1deb50 | -4.38394 | -43.34715 | 2026-07-07 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e342d863-106a-3cc6-a686-b9661c2d5ec9 | -5.90984 | -43.85682 | 2026-07-07 04:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a343b8ed-9653-3a4e-add8-a5144e2d9f4a | -4.14862 | -43.10345 | 2026-07-07 04:23:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d62f53d7-07d9-3a4c-8885-0ef24a5cd6e2 | -9.23178 | -38.40794 | 2026-07-07 04:23:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7fa8175f-647d-3ef5-8c53-60ba07fe43af | -8.04549 | -45.04227 | 2026-07-07 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5eae286-c257-3bb8-8b02-67fb5d5eac74 | -8.34359 | -46.48703 | 2026-07-07 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 307fc51f-f8fa-3416-98af-6abc96ddd284 | -2.97886 | -49.26853 | 2026-07-07 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66a3d702-f3ec-3bf4-904b-bce5e9a4decd | -6.90801 | -43.71243 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 348e922d-9314-30db-bb11-415cf2bf1662 | -8.03874 | -45.04117 | 2026-07-07 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9bbcf81-a6de-3150-a191-52414b32a625 | -6.90181 | -43.71161 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dcedeec-51fa-3212-91ca-4643c1b00d61 | -6.59708 | -51.69754 | 2026-07-07 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71f8f009-f17e-3cf4-b106-7d11e2e8cb09 | -6.93072 | -43.69823 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0da8b189-44a5-3d2e-abc9-6d992f83e054 | -6.90366 | -39.55005 | 2026-07-07 04:23:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2d4535d7-b51a-32f6-95c0-d1407e077cbf | -5.74647 | -46.15343 | 2026-07-07 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14f08772-febe-3b30-a03f-f4ddffe29bd6 | -6.95718 | -44.55116 | 2026-07-07 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b393bddb-bd32-3039-ba6b-efa20042ee73 | -6.91244 | -43.706 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1210d9c0-7297-37fd-9820-9f2b5b710dd6 | -6.91189 | -43.70948 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 92f96c58-16f5-3a7e-af3e-c7067eb183eb | -4.069 | -46.37676 | 2026-07-07 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c70e40c6-a140-3b91-9e26-795330380ff0 | -3.98323 | -48.42972 | 2026-07-07 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b2c6298-77c5-300a-8bc9-74b7cd061d43 | -4.14917 | -43.09999 | 2026-07-07 04:23:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 620e368c-d6ac-3ec2-aabe-de7612e583fe | -6.90857 | -43.70895 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e768c1fd-5ae8-3c2a-bd4e-79b4c8abdb25 | -4.37785 | -43.36399 | 2026-07-07 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c1425a5-9d74-3467-b769-689becb6b9de | -8.12742 | -47.11407 | 2026-07-07 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eb8b70b-7ddd-30c0-b294-6f6acba834f4 | -6.93072 | -43.71961 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6e215d0-6210-3aac-ab27-dbc973f9092a | -6.91078 | -43.71643 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 21d05d19-3bab-3d3b-be13-a0bea13f5f0b | -9.43809 | -40.32404 | 2026-07-07 04:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| eceffe2b-38d8-3c31-951b-ecaaa54515b1 | -7.63904 | -50.02673 | 2026-07-07 04:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9829d304-1e55-3901-9962-4c11dd0e5938 | -9.44181 | -40.3246 | 2026-07-07 04:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5618ea0c-4915-3d5b-8a0e-69708e4a5791 | -4.3482 | -47.76388 | 2026-07-07 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b99fe39b-a69e-3133-b3dd-6b6f66a483df | -8.03932 | -45.03757 | 2026-07-07 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e970bf82-cdce-33c2-950a-7db048a5a6cb | -7.64421 | -50.02321 | 2026-07-07 04:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3927957-418b-33fd-9c5a-0a603370bc6e | -6.90291 | -43.70465 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78f37a4a-66b7-3cba-8eba-ee7747a496c4 | -6.90912 | -43.70547 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73f3503f-fcc8-3a4b-beec-72b48c0152ec | -8.11643 | -47.11216 | 2026-07-07 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d6b09c95-40c1-352d-bc8f-49c75eceb595 | -7.01102 | -42.78403 | 2026-07-07 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 14485298-944b-3586-bffd-db13bb51e644 | -4.37729 | -43.36746 | 2026-07-07 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d9a2d1b-d60f-3ca7-a3d9-0152048d46c9 | -4.83329 | -44.07204 | 2026-07-07 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fb073c7-8bba-33e2-aa38-8ab144a1f477 | -8.12011 | -47.11271 | 2026-07-07 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c974bae5-c883-3914-ba63-525900caf939 | -4.28896 | -48.3561 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1bb6fb56-5a4c-3042-ba6c-dd88a6efd488 | -4.28419 | -48.35902 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7a385b1b-774f-3565-a8fd-467e5c6a0122 | -6.93736 | -43.69928 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9145fd31-a127-3405-99a4-8e2badbf4b96 | -4.83164 | -44.06087 | 2026-07-07 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 61f8a246-5048-3152-bc4a-b377b916bc48 | -5.82776 | -43.4838 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cffdef82-50cd-36b8-aa76-b47c6bbae334 | -6.91466 | -43.71349 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| eff8417a-fdc1-3372-9b5c-7e783c0713f0 | -7.10328 | -46.51503 | 2026-07-07 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fdb2ab0-b9e3-3581-969a-9c2042a02063 | -4.2848 | -48.35529 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0b9a82d5-4b08-3405-be88-3c7054d12874 | -5.82886 | -43.47686 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b13e0b00-f704-3cda-b831-d5a55227440d | -6.89848 | -43.71108 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8565b58e-d296-31fa-b0db-c10730c63dea | -5.9104 | -43.85333 | 2026-07-07 04:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc2e48eb-aad5-3490-9a37-ee5e92f3fa53 | -5.50258 | -44.07996 | 2026-07-07 04:23:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aba43c3a-42a5-3091-9233-861dac3c6f9d | -3.87446 | -42.9785 | 2026-07-07 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3756efd-816b-3aff-8dc9-c2c35beca33b | -6.93127 | -43.71613 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7a41d61-c54a-3eba-92a5-d0a0734ed05d | -3.77889 | -41.60669 | 2026-07-07 04:23:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1148527c-16dc-3053-9aa6-918adb6388d2 | -6.2936 | -43.63964 | 2026-07-07 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27a64056-a920-3ddf-9f33-652781a347b0 | -6.29693 | -43.64016 | 2026-07-07 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e32ffa2-eaa9-3d56-bab5-271610cfa059 | -8.12304 | -47.1177 | 2026-07-07 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf35ef6c-fe09-37b7-ba65-491c6b594687 | -5.83108 | -43.48433 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6949dd7e-588d-3207-b27b-bbe31a9a18ec | -5.75299 | -43.18801 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8cad4a0c-847e-3972-83da-19096f970ead | -7.00655 | -42.76898 | 2026-07-07 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2f356368-05f9-3af3-99fa-47e087d9f897 | -3.87501 | -42.97504 | 2026-07-07 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3ec6417-62fd-37f0-804b-d6a24a16efed | -14.01556 | -47.37568 | 2026-07-07 04:25:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2eb16830-7153-3cb8-bf15-9e64fb93c74a | -11.68206 | -44.5672 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cbb3740-10a4-3dcd-b093-eff2550dd0da | -10.9391 | -43.06903 | 2026-07-07 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 8b5fe314-859e-3e71-8ada-03c5705e2155 | -13.54313 | -52.91426 | 2026-07-07 04:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd4cce82-4884-3927-969d-04920b76844f | -12.50644 | -48.26229 | 2026-07-07 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b90821b-9d04-3b7d-a90b-101263d7cec9 | -9.57579 | -48.1785 | 2026-07-07 04:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 395eb3da-063b-34e5-a49b-4cca05065003 | -9.31216 | -51.91901 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35e6ebc3-9ee9-3497-be96-ce7c26732c6e | -12.45014 | -49.57805 | 2026-07-07 04:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7f4169f-9bf0-3124-b163-f7cbef1417d9 | -13.32637 | -54.37129 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f395e8bb-845a-3479-941d-de381b3b6774 | -11.48811 | -52.91872 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2952f83a-5e49-3687-bf1d-800f049e27a3 | -13.29576 | -54.35731 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a0a0807-32c9-3c83-ba82-f8029425173b | -13.26128 | -54.35046 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dec62663-586a-3146-af21-878e5d4527a2 | -13.31966 | -54.37709 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5be29bc9-548c-3340-9b35-932814e67269 | -13.27705 | -54.33964 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e56777ff-e208-346f-9009-2b0a0bc01272 | -12.5072 | -48.25786 | 2026-07-07 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51656288-d313-33ab-b9e9-5091cfdb9158 | -11.67652 | -44.55908 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d4e659f4-7024-3af0-904e-0ba67563d398 | -12.79022 | -44.51254 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45a7120a-79a9-3277-9237-a4e1fa770e61 | -13.26324 | -54.34034 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5cc37e9f-295e-3037-bb71-a7ca0b3c335d | -13.25836 | -54.34961 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce325bc8-2184-334b-9a00-adaba3cdf6e8 | -11.99316 | -45.13916 | 2026-07-07 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17319dfe-1f8e-3258-a0bc-d99e5504b020 | -13.3111 | -54.36409 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bf0388a-a75b-33d4-86fd-221d8e88a9e6 | -11.65767 | -44.57044 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b392c29-bca3-3456-9c99-727eaab5af3a | -13.28504 | -54.3553 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b22489e-70b2-382a-a566-d0a5086bd9ab | -13.31641 | -54.36537 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c1c2505-3ab5-371b-82fa-e738ff8c9d7e | -11.68538 | -44.56775 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 208cebfc-2336-3cc5-b800-ce6c94a112d7 | -13.25717 | -54.22917 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1b90b3e-318e-3c64-95aa-44b7549831fc | -11.67153 | -44.5691 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c052366-3ea7-371c-b09b-86ab14060426 | -12.75639 | -44.55418 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15f75f1e-113f-3b1c-a1aa-f6f479508625 | -9.28058 | -48.21406 | 2026-07-07 04:25:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efacc556-4f80-3f51-8070-e4e8bf9757d6 | -13.27726 | -54.35403 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3778439c-eea6-3109-84d3-b2c9ca608419 | -13.26639 | -54.33731 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a75acce7-6354-311c-bb13-f44b1b549fb6 | -11.67432 | -44.55149 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
