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
| b535acf8-acb7-36c2-88fa-2d69c868c96d | -14.69172 | -48.11975 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2415966-b7e3-388b-871e-554b086a1cea | -13.66337 | -48.08215 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f24a47de-4038-3d56-b255-164a0baa726f | -14.76135 | -45.75288 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db56eabd-df25-38fc-b6e9-4c9bfb31c6ce | -12.66273 | -46.86882 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d45d36e-dfdc-3be8-bddf-55df4fc2ad59 | -11.59288 | -45.04251 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2eff1ac-1160-3ff7-b515-f15e4e22be35 | -12.83864 | -46.86936 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2b160c5-9673-3968-85d6-f34927adcfde | -13.0622 | -47.0834 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f996616f-232e-3150-bf27-e3219095f48f | -9.42764 | -54.71726 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dac220a0-35fd-33a4-b0ae-f7619697f4d8 | -14.6753 | -45.29171 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c1471e5-38a0-3084-9d2a-bf5564e16f3a | -11.08585 | -47.83594 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b85c1b0d-7c8b-3222-9e90-16d6a4766561 | -10.63175 | -48.58981 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a20cef40-8ff7-3a20-8b2e-eeb70cd9eedf | -13.33335 | -47.87415 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c3885c0-810b-3057-ab80-3cbb3dbf9b4d | -11.20008 | -47.19958 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b994469-5c6d-3f87-ae9d-8e127f738704 | -15.26694 | -51.47945 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 216f43e5-2c1b-3da4-8da8-556e9d8a2714 | -15.66788 | -45.23917 | 2025-10-01 04:51:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6019429e-5488-3561-aab3-ca299b438477 | -12.47576 | -54.42502 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f37ab50-cf4c-3bff-87ff-da792a56ae97 | -9.94303 | -43.64693 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fe18548-b379-327e-af59-7e846bb89a47 | -11.96268 | -46.59555 | 2025-10-01 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 174a6ea2-7b87-3a6f-b338-514f96ce2b9c | -12.66103 | -46.88112 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a1368c6-28bb-3bec-90b0-63ab88bbd662 | -11.05702 | -47.83448 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac582e66-c818-3256-ad90-8fed89bf56a0 | -15.38974 | -49.19048 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dfc61e9f-c69d-37dd-813e-3656efe598ce | -15.75194 | -43.69493 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef292ee0-fb11-3cf9-b38f-b4eb82bd092c | -12.86224 | -46.9474 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7a4edd5-bad3-3670-a1b6-d30278d79be3 | -11.94551 | -47.06287 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0198f1dc-e0ec-3101-9425-42259c0564f3 | -14.6107 | -45.03281 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 885befac-f5e3-3b9e-959f-d112ac282c57 | -14.68211 | -45.27639 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f18a14da-da77-30ee-8c42-f94416d0ba32 | -14.51907 | -48.36399 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b714223a-3e7e-3ad2-93c4-a5f5252a8d34 | -14.50674 | -48.48364 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f1ba3505-1822-3b1e-aea8-5f716c1c9486 | -13.33489 | -47.83323 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4767b807-8439-3eeb-8fe0-8cec20a96e5f | -13.6546 | -48.02934 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a505821-c8f2-3715-91dd-8fe84eac7fbd | -9.60711 | -50.89425 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 094c16d2-294e-3ef9-99e6-e93d1e3ebd36 | -11.40342 | -44.89592 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a250b2a-10c8-3ada-a21c-1c0d729e56e6 | -14.50068 | -48.44218 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99fa7717-0b52-348e-a896-529ef75a5eec | -13.33076 | -47.86348 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6645a675-842c-300c-a4bf-e7f1395d1071 | -10.33349 | -50.50729 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a50863d-3228-3298-815f-94e195a91a71 | -10.23825 | -52.69485 | 2025-10-01 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7dda9569-7d06-34cb-b205-cfda7fe8f66b | -13.76231 | -48.40227 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ba2a4e6-131f-3eaa-b87a-046e41ecbe1e | -13.54125 | -47.25795 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80bfae3c-e18d-3024-be79-a38aaebf3504 | -12.43071 | -50.17014 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5591abd2-2beb-399c-aebc-77c88fbfc814 | -14.90959 | -51.6764 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5c622d2a-e8a4-3710-8fe1-4178634635fc | -12.8299 | -47.02809 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df18ab76-9099-32b6-b9f9-1325fa0543af | -15.14104 | -46.41843 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b78e98b8-bfb5-3d43-8275-22000bbcec63 | -12.16084 | -47.89456 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 767c31bc-3d32-3fa7-8f6a-f361160d1ead | -14.04447 | -47.99214 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d82fc74-f57b-3063-aa27-638f4abd1f7d | -12.76459 | -46.91062 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b888e6a-4ac2-396b-97db-91327e2db09e | -14.62726 | -46.984 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4f9230e-e70c-3de9-8fc0-e5dc075d9c5b | -13.35833 | -48.09937 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c591c83-72df-3f9b-ac48-ad18c0d83254 | -13.65781 | -48.03531 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b0d4ef4-0b86-3a64-8305-aa14a5552798 | -10.82025 | -46.63521 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52f16e79-1f47-3811-8461-628e9b340708 | -11.46693 | -44.97335 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b83c684-6744-3588-ba61-736a6e57b565 | -16.08567 | -51.0437 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5035d27-33dc-36fd-802c-1d6f4919b3a7 | -10.48003 | -55.61961 | 2025-10-01 04:51:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9880ab4-45b6-3a37-b0ce-2427c1910d5b | -14.78822 | -46.97132 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20b9af37-cddc-30ba-88eb-010cfc63b329 | -11.16067 | -54.11532 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df8de1e5-cab6-3d01-9c50-fb6ac4152302 | -11.65409 | -47.49985 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 689c3565-ae19-3a3b-8901-b5a50ffcd3f5 | -11.38865 | -44.89872 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc84adb6-9c43-36aa-b035-9a0dc2aae580 | -11.45725 | -45.08387 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9730522-7a0b-32d9-a30f-61c6f4b71fdb | -12.83041 | -47.02435 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e73b5b92-0233-3664-8015-42f4fb8b3899 | -13.32815 | -47.85294 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1c6853f1-2bd9-3cad-bd7b-1a7157636dfa | -14.49608 | -48.4466 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14c6d999-2ef2-3854-bb11-e8914b4f5aa9 | -14.99044 | -46.96215 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a43c377-055b-38c4-9f9e-0af1b9af4a70 | -13.91193 | -48.08784 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b0091f2-b7d3-3e2a-bbd2-70a6966b349c | -13.30319 | -48.70094 | 2025-10-01 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3be3f412-56bf-32fc-9fd4-7edbe26eeaaf | -11.64616 | -47.49854 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3eda7c1b-1669-39c0-a08c-babff599596a | -15.16066 | -49.09785 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf400299-e7ec-38e9-9fe1-4d933ac84744 | -10.33107 | -48.19104 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5cd2a5b-c277-3d17-aa7b-8f822a612e37 | -12.90573 | -54.75199 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c83dd3cd-0749-31a2-bb84-8a780a59794e | -15.34446 | -47.83791 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1aac2bcf-39ab-36a9-9c00-117fad0bbd54 | -16.02612 | -50.88537 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c75172e-71ec-3cb0-a469-5262faa21783 | -13.91445 | -48.08166 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b8888ae-7691-399d-b4e0-17cf86e4a10f | -11.46466 | -51.51036 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c9bfd62-0473-3107-a4e1-47626cc88d5d | -13.9145 | -48.09869 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98200855-c9e2-3298-a40d-483cb9b8da03 | -10.50908 | -47.29667 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3915461-b11e-3950-936c-d8fbbfe00dcf | -13.29926 | -47.58103 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 258e4e60-7906-388c-9c52-79449e8ac824 | -10.91279 | -44.78875 | 2025-10-01 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8141ddd2-034e-30c6-95a5-760f6e60f922 | -12.22947 | -53.88029 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6a6e2fe-28b8-3402-a9c8-5d7095da1748 | -11.63276 | -47.49487 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d5582540-89b7-38e8-98c5-57f304214267 | -16.4028 | -47.03884 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3545708c-bb76-3132-9b16-273b041fd1dc | -15.27808 | -47.83571 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4884cfaf-beb4-3523-afc3-d4dbe1e5ccc2 | -11.60747 | -45.04027 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5dc348b-5c89-311c-8a81-1f22c79a13d8 | -13.91724 | -48.07827 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 536df3ec-a3b6-34b1-b85b-b8fb99cbc55b | -14.79092 | -45.80449 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fd806b07-46c8-312b-a0c1-a862797affdd | -13.65392 | -47.30902 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9134604a-659c-3f93-92f7-00580cd329eb | -14.35468 | -45.91488 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 61e482da-61d9-3fa5-b1be-9a70182a5dbf | -14.13996 | -49.19564 | 2025-10-01 04:51:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b9d5f8e-bf68-3ab8-8577-347ff6c32009 | -10.33794 | -48.19637 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a12fa5c6-7c39-3f52-ac87-58dfeda016fc | -12.70838 | -46.88382 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0229e3b8-6f52-301e-ac0f-a76ea7b4e4b6 | -10.6281 | -48.5891 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94870f43-8acc-3ef6-b245-491fb441bc9d | -11.05907 | -47.8205 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 70366dbc-092e-3152-836b-ed341bda17b9 | -13.67224 | -48.04741 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0af83253-306f-3e27-a698-652016692c03 | -14.78942 | -45.77855 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 662fb9ae-ebcc-3a33-a39f-e823e1ff82da | -13.96972 | -44.8894 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f09380a-4934-39bd-95c8-494d4d06b5fa | -11.46891 | -44.99475 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52e667d3-0bc7-34af-bc32-178d84c31a85 | -11.83689 | -48.06821 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 07d006b2-1ce7-35b4-aa3b-3e3c09b604ec | -14.68323 | -45.18903 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e2d45ca-89b8-3d65-b146-be17de53e4ec | -14.58756 | -48.30181 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c243960d-822b-35fe-a184-1a4856e1f471 | -11.27643 | -47.81279 | 2025-10-01 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 393caf42-b153-35e5-9fd3-e767fc3369cb | -13.7796 | -47.98746 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| deef5c6d-877a-315f-8375-bcd1e2193b86 | -14.89035 | -48.13418 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d1c3ee0-1124-3038-b066-809d8c207385 | -9.92991 | -43.66903 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README95.md)
