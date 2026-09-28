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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b57736f-3b36-36dc-aa69-6715ce080874 | -10.22492 | -49.99743 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb031573-c76e-38c8-a5b7-3e9710a8a79c | -3.28987 | -50.31282 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 005607a6-af9e-3109-b898-b31414c03eb3 | -4.31203 | -50.39856 | 2026-09-28 05:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c908c726-22fa-31c0-9a03-e6cae6e81f85 | -11.19009 | -44.80325 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 7ae81425-b144-3bd7-9876-311781bf9d96 | -6.69024 | -59.97104 | 2026-09-28 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 354d24d8-e785-3948-b0ed-884e654c11a6 | -7.62646 | -45.52415 | 2026-09-28 05:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 786bd4a5-386a-3ce7-935a-8863b7ecb5e1 | -8.23932 | -45.43526 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1449db0-4d21-3411-9110-bb552878a42f | -9.14877 | -45.63493 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 407aea1e-c89e-3016-92c0-230d7f854584 | -6.00369 | -47.39022 | 2026-09-28 05:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 170b8897-2a2a-36c5-9a39-9e54b49fc9bb | -10.20923 | -49.99147 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 279f5d93-d7c6-3627-a13b-1f3eed966149 | -11.19538 | -44.80573 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8afd3f9e-0442-3028-8338-d88ee649a410 | -7.45964 | -55.00333 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1900ec0-b612-3514-84d2-a2426933cfd8 | -10.80538 | -48.7308 | 2026-09-28 05:10:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5f7726ca-9b44-3434-adcb-2868a2dc9c81 | -11.19063 | -44.79905 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| bdd6836d-99d4-31f6-b1c5-e7f811f882d6 | -9.47652 | -46.39109 | 2026-09-28 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21be2fa3-c3f6-3807-b8d4-14474f4af63e | -10.11373 | -50.19492 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb1a2cca-be9c-3cc1-aa9b-17a386132dd7 | -3.22943 | -54.31963 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8520f6f-2bad-3162-8b9b-b478b480137e | -9.98493 | -50.14255 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ccf36b71-16b0-3bb4-9979-991ede84a5c2 | -6.99193 | -42.70251 | 2026-09-28 05:10:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3906ec48-d697-343d-83ab-c78aab4dfeb3 | -8.01357 | -43.73833 | 2026-09-28 05:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb47a761-9fa8-36ae-8087-91d151fc7ba5 | -7.82868 | -55.1342 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2aa8b1c1-c5f8-35d1-b824-b5e04803cc88 | -3.41091 | -48.33681 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5b622f6-54c6-3c03-a809-ebc1bcd0a0f7 | -9.07315 | -49.87072 | 2026-09-28 05:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d62c180-d5df-3ecd-a7b1-110043efd3af | -9.15326 | -45.64236 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37a1a762-6f91-3d9c-adec-afc71c2fd1a8 | -7.69169 | -54.76453 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4652b1ba-6aa1-3907-8627-2e613ba1de30 | -2.05319 | -56.87144 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f4285b1-08d9-38cd-a280-ddc45fa9206f | -6.69668 | -45.65165 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34d33a5b-c302-39a6-ae53-167fe1a75b45 | -3.41475 | -48.33337 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d8eb742-6f6d-36e8-89c1-fb5a754fd43e | -3.23381 | -50.57726 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9d7e0951-d480-38c3-899d-9803946df4f1 | -3.00969 | -54.20974 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1b0107d-956e-3327-b179-04ce578163b9 | -3.41555 | -48.33387 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7799aa5f-630a-3222-89fb-5d04459b75cb | -6.31492 | -43.60878 | 2026-09-28 05:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d05e945e-6141-3438-8ea0-05f07a5c8632 | -5.73096 | -43.27768 | 2026-09-28 05:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 599a18f9-e18c-3ee5-8ae3-d94c3c289486 | -7.3846 | -47.01074 | 2026-09-28 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74765f87-d532-3488-a6bd-10c3c166a49f | -7.27972 | -55.57668 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7ee51c6-022b-32d6-975a-70e5d33b39d1 | -7.82478 | -55.13718 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8c2dea6-60d6-3437-958f-7f3e10f5a96e | -8.67156 | -48.96423 | 2026-09-28 05:10:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb5f6a9c-4bbb-3992-ba95-214a83c7caf1 | -9.15056 | -45.63938 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24c3eb6d-aa3a-306b-8679-7951fe70f4f1 | -2.89376 | -54.16998 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b04997c8-0a57-34ed-91ea-0f6a13f96ea9 | -9.77755 | -48.21688 | 2026-09-28 05:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1533651-5d71-3336-bca7-513b1deb5746 | -9.14611 | -45.63197 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfc0f568-396d-3590-b969-bd4525421d0b | -5.72169 | -53.44926 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51eff3f4-7169-3f62-a25d-8f075e75a54a | -8.06984 | -55.33554 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3c004b5-4c55-3205-adba-862fb2db0e43 | -10.11924 | -50.18513 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efa9f3ce-fa42-3569-b243-3bf03824c86b | -6.59686 | -47.16328 | 2026-09-28 05:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66e8003b-cb75-35af-9d0d-4cea38eb50e4 | -7.9926 | -44.81749 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c69baf1-5b18-34b9-94f9-f269cb0fd925 | -8.41474 | -44.87129 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2b2d7c3-4cad-31cb-beec-c64f8206909f | -3.99904 | -50.64105 | 2026-09-28 05:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c76efee-31de-3ee1-be0e-ccb759b3665e | -8.09905 | -44.00442 | 2026-09-28 05:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3882f0e8-2fcf-3480-9831-f3e18d42693a | -2.27006 | -57.01431 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| d83a048a-1bfc-3fab-8523-9a72d3f7b121 | -3.43147 | -50.33735 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6284530a-359a-3044-bfd8-34b7c8cd84a3 | -10.20669 | -50.0093 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e1060bf-85da-3417-bdce-79ece1771c7c | -9.82843 | -45.26343 | 2026-09-28 05:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 128f62fb-4f19-3ad1-9cbd-07f879da5b5f | -5.307 | -55.82865 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba7a0117-841c-3e1b-875c-64bb885ed74c | -3.10223 | -50.32096 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58d46420-dfb0-3aac-8555-fc83e2d9f793 | -3.97122 | -59.34408 | 2026-09-28 05:10:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94a76f2f-503c-3db3-9aea-a7b55cb3e88f | -6.89335 | -59.84401 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 490a6bc7-b8e3-3946-a69e-ec76e89597d8 | -4.00265 | -50.64155 | 2026-09-28 05:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5ed14c3-3cae-3480-bf50-6994b7e0e3a9 | -10.2972 | -48.15902 | 2026-09-28 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a2407b8-6ee2-397f-807b-be9e52f44691 | -11.18474 | -44.79589 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| dd206573-cc5f-3cb1-9b26-13eb04eeb278 | -9.77331 | -44.83652 | 2026-09-28 05:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c8093d9-9a88-3eea-bb82-bf0f5ba56732 | -3.15629 | -54.09657 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f224171-8975-3402-9b57-ebbd2533c68a | -10.69081 | -47.8116 | 2026-09-28 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 23ed8fec-8a41-33af-953d-c69bfcc5d00e | -3.10585 | -50.32151 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c373b11-163b-3475-a6dd-e202aced22ce | -9.14584 | -49.96799 | 2026-09-28 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cb942ff-7f16-3894-bc89-d80f5f0c6aec | -2.8943 | -54.08052 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7eda59f-431e-342c-b4df-1c2738d08d5e | -8.23059 | -45.4814 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8d39432-3907-3dec-bf84-8b2b2afeb71f | -6.7749 | -46.68582 | 2026-09-28 05:10:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4ef8a33-7a28-321e-8a79-1ea250daaa81 | -7.82422 | -55.1407 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2d8baaf-5ef8-3cef-95d7-6ecdf6a648f0 | -2.56584 | -57.37932 | 2026-09-28 05:10:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 284740c6-881d-3fc1-b827-2359aa6b7f2c | -8.23322 | -45.48108 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86d36c24-f3ce-3ee4-bd0f-56404da9386a | -7.55984 | -61.35652 | 2026-09-28 05:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8106fa8-0d3b-3abd-a45c-06e0d179c6e8 | -2.12096 | -56.88497 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb2b2aa0-6674-3896-a1ba-1035c44eb475 | -8.43257 | -44.86545 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac0ab0ca-c7d4-30a9-8c58-a41c5d4b769e | -3.10658 | -51.27732 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39bccc49-c290-34e2-b766-dc40bccd788c | -3.2014 | -51.03738 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 034f965c-3deb-3963-9a6b-37e6b0bee38f | -2.96068 | -54.08738 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daa420a2-940f-33ad-aacc-cbef7c87025e | -3.03203 | -51.47012 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb58d37f-796b-39a0-a500-22c8bbeda340 | -8.27829 | -54.71144 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 327535dc-00b8-37c6-9b46-f35b11798d64 | -8.66598 | -45.41511 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dfe0749-f015-3df9-9c51-b3e3ecea9da6 | -7.27634 | -55.57614 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02624118-68b6-305a-972a-9912ebb30e9d | -9.15147 | -45.63269 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21bc542e-5864-33fe-b957-90c0da58009c | -9.99043 | -50.13272 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ac0d1d1a-c4fb-3521-875b-f13cc1bd4566 | -10.21937 | -49.97838 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43722cb3-d924-370e-bed1-e9b4b63ee1f6 | -8.65467 | -45.41727 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e05f8fc6-4cfa-3669-8f89-8510a5a70aac | -6.6958 | -59.96396 | 2026-09-28 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23a0561a-add0-316f-842d-24ce0065268c | -10.22138 | -49.99327 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b16d112-2d0c-3173-afe9-74730a42a702 | -6.13958 | -44.13754 | 2026-09-28 05:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41c44cb7-5fa0-30ee-a258-9a46bab72598 | -7.46576 | -55.00789 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc62a2f2-60bb-360f-9e46-f3c04e5baf03 | -6.71585 | -45.5952 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b40b439f-f7b1-355a-bec6-798a9ac80fd8 | -6.74407 | -55.08309 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaf8fc50-60d6-3a6d-9c51-dfcbe2dd807a | -2.88595 | -54.08994 | 2026-09-28 05:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d81e2da2-5806-302d-913b-1278d6378398 | -6.68931 | -45.97445 | 2026-09-28 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af8fc8e5-b8b1-3dca-b4c9-df87255c0185 | -7.49584 | -54.96965 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2791d6a-f626-326b-9d5b-5c8731abda73 | -9.1738 | -45.77583 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33e830d6-136a-3c83-a752-d52128be5e53 | -7.7166 | -44.90812 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b997fa9-f04c-3e18-866a-0ab7b16e4044 | -6.71115 | -45.58821 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98558207-7b82-345d-8d1e-0d52c76badb0 | -4.78655 | -49.11692 | 2026-09-28 05:10:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23f63899-7d21-383d-80dd-199453a57600 | -6.81965 | -46.13655 | 2026-09-28 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 48ddeb04-7a73-3082-a777-13351522f958 | -10.69126 | -47.81334 | 2026-09-28 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README51.md)
