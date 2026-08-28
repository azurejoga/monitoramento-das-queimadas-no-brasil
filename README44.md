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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbddbfde-26c3-3e18-bf26-fd8f92f713fa | -11.74571 | -54.5216 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 863d1a52-568d-3159-9000-c25a7953d52a | -10.76857 | -50.64181 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdffa791-de92-31a5-9147-724a22cae4c8 | -11.02098 | -49.66184 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7e904f4-3bef-370b-baaf-be7e51598639 | -13.43601 | -53.98922 | 2026-08-28 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 090607b8-f5b8-3d07-a9d2-5d96f0882ae5 | -14.11378 | -44.384 | 2026-08-28 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed1157e4-f690-3bca-99fa-29782c5f4e8c | -9.43256 | -51.69656 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 10414ef0-5cfe-3ad1-8569-3407d3925a1f | -11.46631 | -46.94955 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22239ca6-cc9f-3131-80a8-18873400f2f0 | -10.9009 | -46.62744 | 2026-08-28 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7660c4b-d4e3-3234-ba2d-8dc96633d6a2 | -6.83684 | -55.61004 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 289b5ac9-d17e-38a0-9f6f-04c6d314403a | -11.01821 | -45.07001 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 045616a1-31c2-3411-867a-8aae7aed5505 | -13.74913 | -52.01987 | 2026-08-28 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f7f9f32-e8af-3165-a9d1-2757dc9b529a | -11.16287 | -51.22243 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2413514-c23b-326a-afdf-437d639dcf06 | -8.1621 | -54.95391 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e23bed3-f2da-3ec5-8e06-3cc49e245577 | -11.73826 | -54.5203 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eb074eb-ada0-3ea0-9b3c-a8a59211848e | -9.40579 | -51.64721 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e437f95-1975-3e70-93ba-4a6219ce5a03 | -14.9418 | -52.59577 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d49dbad-462c-375e-bb1e-ee8e80056cc9 | -11.53845 | -45.51698 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e26dd13-901b-3d31-9297-423bfecce747 | -8.59825 | -54.77878 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7745a813-161f-3ee5-b972-64af8ba3990f | -10.3241 | -49.96578 | 2026-08-28 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec9b0090-c9c3-3837-b5b3-5f613cffc848 | -14.31634 | -49.25146 | 2026-08-28 04:51:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 626849a9-3b05-36e9-9532-9f436220b709 | -8.80774 | -50.07803 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1ddef0f-1359-34de-ba97-3933381c7bed | -11.19855 | -55.09325 | 2026-08-28 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2cf809e-5ec6-3c47-82cd-0827a68de01d | -13.612 | -45.78076 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88a27a73-0ea2-3a20-ba9b-69ec70af9a8c | -6.9793 | -55.64331 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8f7c57e-73fe-38a8-b8c7-01d904181607 | -9.45091 | -51.71404 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea0ac0e5-8d10-3826-ba0c-36cdcf1c7288 | -11.18953 | -51.22684 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9f184727-f069-3b61-96ca-7e06432de265 | -8.11694 | -51.66537 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6624331-1b4b-3b37-b65c-015ad1df4c24 | -8.95246 | -50.166 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8fda0358-58f6-33d0-9894-d69ec35708cd | -10.76157 | -54.04724 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4831af2a-ed89-3026-a4a6-86d27fd70217 | -10.9938 | -51.09663 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdaca95a-27b3-34b0-a850-42ddf8d0d60e | -14.49685 | -53.40288 | 2026-08-28 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 257e6207-91ba-32bf-bdf1-c8994b42459c | -14.86589 | -52.60951 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1e6e6c4c-9a25-3455-a7d7-70deeee04d40 | -13.41777 | -51.79168 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83f325a1-df93-3b4e-a92c-9ece63517d2d | -8.81848 | -49.62151 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6305545-152c-30fe-92c8-1bf237efd006 | -11.63955 | -46.73441 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dc74265-d5dd-38ec-96e6-a41f1ef34dbc | -9.87079 | -60.25269 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ca329a7-14b6-3496-ab8e-060d2fffe299 | -11.82029 | -47.2112 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a14c1454-6134-3bd7-8238-50e636611c43 | -8.79988 | -50.50676 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2bd0fb3-10ac-3300-8f37-c43cf3b49cb5 | -9.42752 | -51.59866 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4efca297-9f80-3033-b22c-08a4b17b2616 | -10.79943 | -54.01583 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 848574d7-ad34-362b-8208-c94ff896b652 | -11.53386 | -45.51996 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3eb4cbe0-a26d-37a4-970e-4caa53a223e9 | -8.59174 | -54.79337 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12014889-3afa-32bc-8ebb-14ec1496c05d | -12.42256 | -43.41527 | 2026-08-28 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a0fdb90-0aa9-332e-9f08-dbe5488174d9 | -12.42855 | -42.89344 | 2026-08-28 04:51:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 808af1c6-0101-3c57-b0ff-c164a1d141cc | -12.28607 | -50.58755 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9942b5af-f43b-362d-8392-4234fce8e3e8 | -8.01275 | -48.40625 | 2026-08-28 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 462f7716-3200-327c-8d5b-aa008c7f65be | -11.76875 | -47.63607 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 985670ab-859b-39d4-adb6-32ee17e2339e | -13.4138 | -51.41103 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 47d0ce54-3cb9-32b5-a693-53d63846329d | -11.1701 | -51.22 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5a004db-8348-3fd3-8bd7-3662d051ccb4 | -10.01367 | -46.40845 | 2026-08-28 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 802db996-9501-33af-adff-f9af1dc51b97 | -9.46378 | -51.59288 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2e07c43-deeb-3cd9-8cd7-ecc17d34c0c0 | -8.79501 | -50.07242 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24575944-653d-335e-9180-1bc96f473372 | -10.79434 | -54.00148 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1024e77-824a-3fff-a081-a278723721e3 | -12.28163 | -50.59408 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f17db02-6623-3eaa-a0ee-de7f73c684c7 | -11.64267 | -46.73969 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3aee0bb-0202-37e2-a187-3f6953f4f802 | -10.3291 | -49.9774 | 2026-08-28 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dcb6d19-fff4-322d-b4d4-5e4fddff80d7 | -10.53684 | -50.78019 | 2026-08-28 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef56bc48-8241-3c90-a323-26dc0d9c29ca | -10.80234 | -54.02084 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e558f1c-8f75-375d-9626-1bc968f295b5 | -11.1662 | -51.22299 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 185eecd1-cc08-394b-96ab-6fc719b1f47d | -14.875 | -52.59597 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5cb1c05c-a7da-3530-bb01-39f6c1a70084 | -11.00702 | -49.66328 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51d6cb33-860a-35c4-aae2-ffa260356790 | -8.94472 | -62.40652 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10684246-b885-3d3c-b609-1a88cf7f2bf7 | -8.59166 | -54.78481 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2af52953-00d8-3e05-a78e-c9c1efc07a0d | -14.29765 | -51.72906 | 2026-08-28 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b5487b8-61e9-3848-8af7-1b32355f8297 | -11.27367 | -54.02077 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7021c9b-12ea-3e83-86a1-0ac13481c2f0 | -9.86867 | -60.26361 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26790c80-1b98-3282-8fa6-f577e5e1a7c9 | -8.5974 | -54.78387 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45434264-32ca-3e0c-aa54-56bd46e1e243 | -14.15178 | -52.82896 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 525ba0a9-598c-3f33-9446-f45071269a0c | -11.62533 | -54.59106 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 398c7b07-18c9-36a6-933c-30cbc480561d | -12.78831 | -46.44653 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 369bab3d-d1e8-3eeb-8f54-19bc22e424fa | -14.91108 | -43.40943 | 2026-08-28 04:51:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fddd6fce-ea34-311f-bf52-6507ca132af3 | -11.65092 | -46.73612 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 38277464-bdf9-39ec-8ad7-13aa02252526 | -13.4049 | -51.80782 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9a89037-5bda-314d-8f0d-c2caceb5c8a9 | -11.24013 | -45.04879 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e442990c-5c83-321e-b54b-047f5aa518b7 | -8.78278 | -49.95604 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac77f64f-f0be-3328-91c2-75816614507b | -11.72323 | -54.54081 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b646029e-8639-3cd8-87b5-c1800f157b9d | -11.22301 | -53.99181 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cc1b393-210d-396f-9a90-603720357e4c | -8.95328 | -62.39708 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0f311a8-1871-3fd6-9dee-99d3519f4913 | -8.77614 | -49.95498 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca17f49-45ef-377d-9d06-42eb04e0113b | -11.71872 | -54.54467 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0f31dda-19a3-3c34-bb1b-00982ea8a6ec | -13.37444 | -41.34822 | 2026-08-28 04:51:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f923d2d3-dbed-3dd9-934a-3a72bf724528 | -14.42723 | -52.59904 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b03ce8d-a562-3d58-8f65-d8dd68739a9e | -14.149 | -52.82468 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11be50f0-c0f8-3c6c-afc4-f282f8dff73b | -10.95375 | -46.25951 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcf7c9fa-5529-3d1d-9042-39dca8406c0f | -10.78572 | -53.99316 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd343a18-372d-39e4-8ac6-6ee3355f1af0 | -12.26943 | -50.58484 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e668fa5-d393-31e7-9242-c41f25dcc215 | -8.02321 | -51.80945 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd4141dc-3907-3096-bf2f-22f3cc9373f5 | -8.94507 | -62.40514 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 206e4704-688e-3403-ad54-c3e41b10bc8b | -11.27075 | -54.01586 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0abef8a-89b0-396d-baaa-9384fed9510c | -6.96572 | -55.64516 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6779f52f-b68c-3e36-aff2-b74ec6d8c78b | -13.83874 | -54.04287 | 2026-08-28 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5e4f16b-9d84-3d3b-a123-124a2ad62587 | -8.98885 | -52.38478 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf16e6e5-55ab-3003-a3eb-cea25abd4daa | -9.22646 | -51.5663 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2647b223-a413-321a-ba57-b56c8d1f6f67 | -14.60367 | -47.97665 | 2026-08-28 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04d37fca-d95e-35a4-9128-e1800bc5dd7d | -10.50949 | -64.51217 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 67ff2b75-1bf0-38cc-b083-10ebca8b70ba | -9.44413 | -51.71295 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb85848c-4711-3f0e-a982-d20c542c6446 | -8.33182 | -47.63113 | 2026-08-28 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c41ee4d-66a2-313e-b67d-c0eba2529392 | -8.60527 | -54.71237 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acc625f7-4479-3680-bc3d-cc1db8c2c59b | -9.2175 | -51.55733 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 858e0dc8-c0f1-37c8-8ecb-a9b69dc5a85d | -11.47813 | -46.94699 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README45.md)
