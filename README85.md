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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe82211a-14af-3631-a269-4e664576f9bf | -10.5168 | -64.4997 | 2026-08-28 15:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| e2b24c0f-a5a3-3c56-b3f2-d293f545d5b2 | -8.6881 | -49.5353 | 2026-08-28 15:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 615c76c8-9458-32c9-9d61-c1648a7d7663 | -10.5404 | -50.4683 | 2026-08-28 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| c860056a-59e6-3761-a5a6-72fb3373e8b6 | -6.2693 | -53.1322 | 2026-08-28 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 999891fd-4994-3904-9b00-7df54b39dde0 | -10.498 | -64.5193 | 2026-08-28 15:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 18f7011a-29b0-3bd3-bb40-5542326b2a3f | -10.7407 | -54.0401 | 2026-08-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 765c8bda-493a-3e6b-ba70-90198cdb56e4 | -6.8358 | -59.9379 | 2026-08-28 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 26eb08f6-4c46-3ba2-9650-3f8383cbd7f1 | -9.2477 | -57.0697 | 2026-08-28 15:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 6ad1cc6d-a6b8-353d-a25c-cafed7f1df80 | -11.7167 | -54.5244 | 2026-08-28 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 597503c6-623d-39bd-89d9-0b2fe49c33bb | -8.5968 | -54.7957 | 2026-08-28 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 811c41c1-6c4f-3816-bb86-c9b2b3bb627d | -11.269 | -54.0334 | 2026-08-28 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 9c7bb3df-32a2-39fc-ad69-23e59d56b3ce | -14.1645 | -52.8269 | 2026-08-28 15:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e9055fa9-10c5-3de3-9183-7d8df4bf270b | -4.9031 | -56.2593 | 2026-08-28 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 91711841-3e06-3362-b6c1-59c8a1a63a3c | -8.5969 | -54.7755 | 2026-08-28 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 207.8 |
| 7aec1186-76b4-30f8-9515-73a377d13f99 | -8.5779 | -54.8172 | 2026-08-28 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 7338063b-d0a9-3ccd-9e2e-512762b64e8d | -6.1473 | -57.78 | 2026-08-28 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| edd88600-4bd5-39ea-83c8-05bddaabb45d | -14.6024 | -53.1508 | 2026-08-28 15:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 4e69b56a-320d-399d-ba21-c7e5a08c1649 | -11.2125 | -54.0181 | 2026-08-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 053a8035-f88c-3fc7-a524-b06f2ab5641a | -10.7598 | -54.0179 | 2026-08-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 64540f49-3598-309d-a85d-b41bc068ae9c | -8.8031 | -70.785 | 2026-08-28 15:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 90.5 |
| dc55f863-992a-3fb3-8eea-aee899a5af44 | -6.7451 | -59.6533 | 2026-08-28 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f04fed4d-26a5-3ca1-ad1c-76b510641f11 | -10.7787 | -54.0163 | 2026-08-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b279f732-0403-3b16-a080-adab313e9caa | -6.8542 | -59.9372 | 2026-08-28 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 5f32b134-745c-39ef-b63d-bf3b9dd43256 | -10.8422 | -50.5219 | 2026-08-28 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 8803d28f-6bc2-32fe-9e17-86817bf186db | -8.3717 | -62.716 | 2026-08-28 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 048c0c85-c03c-3b26-97b9-5e6253df786a | -7.3479 | -55.1544 | 2026-08-28 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| e89ed12a-8f20-3b5d-8e8d-3d43ac67e056 | -8.6694 | -49.5369 | 2026-08-28 15:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 30e292ac-33bc-3e65-939f-66376071ef0b | -10.8232 | -50.5239 | 2026-08-28 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| e65cc4fd-2db3-381f-8283-424b2d76d6d8 | -15.09387 | -39.70719 | 2026-08-28 15:44:00 | NPP-375 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4c89db97-95a4-3d7e-a6d8-212c3dd21f7d | -16.41511 | -43.05413 | 2026-08-28 15:44:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e9eadd2b-f252-30ec-a1e4-a3b3b1fcf820 | -14.88331 | -40.68533 | 2026-08-28 15:44:00 | NPP-375 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 27c0d09c-f6e8-3415-8774-b4bbcd2719a5 | -14.90912 | -40.94277 | 2026-08-28 15:44:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 3b326446-33fa-39e2-9755-614810733554 | -14.93634 | -42.19467 | 2026-08-28 15:44:00 | NPP-375 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8bc8439f-06fd-36b1-8fb1-7eb4e010a2a0 | -14.48613 | -40.62503 | 2026-08-28 15:44:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 91c9d59c-7883-3f69-a0d2-403a91f41523 | -15.5828 | -41.77843 | 2026-08-28 15:44:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d21f3de8-d881-334e-a55e-7e658ea076a7 | -14.90354 | -40.94815 | 2026-08-28 15:44:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 5e2f1485-5e15-3871-9182-98abdcc8e19c | -17.93572 | -42.60954 | 2026-08-28 15:44:00 | NPP-375 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| fb81fa90-b69e-372a-88ed-be6c122af186 | -16.40808 | -43.05484 | 2026-08-28 15:44:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e4d4ea92-b3e6-3730-9e1d-c70e65d7f67c | -14.90999 | -40.94392 | 2026-08-28 15:44:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| a061c9c2-3d61-3503-9c24-392f94d45d78 | -16.38172 | -42.98229 | 2026-08-28 15:44:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4c5a6081-5edf-3b94-b9b3-60fbcf2412b6 | -17.5172 | -42.00848 | 2026-08-28 15:44:00 | NPP-375 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 6071de88-ea30-3c4b-9735-41efbf3bb9a1 | -15.48973 | -41.15155 | 2026-08-28 15:44:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.5 |
| 30a50b67-350e-3e2b-b449-0b40f689ac10 | -15.49334 | -41.14786 | 2026-08-28 15:44:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 6c4c8eeb-30ea-3444-b90d-3a9ca8224963 | -14.90965 | -40.94756 | 2026-08-28 15:44:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 3dcf0cf3-9cec-3c03-b331-0292a98e7cf8 | -14.8812 | -40.68917 | 2026-08-28 15:44:00 | NPP-375 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 36de17c7-8a67-3ea3-9c5e-26c302fb1b8a | -14.90388 | -40.94452 | 2026-08-28 15:44:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 0e29f13f-4e54-3669-99d7-d7cb1f837505 | -16.41002 | -43.05605 | 2026-08-28 15:44:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c7a13259-866b-3b85-88c1-ed81893c9123 | -15.49384 | -41.15285 | 2026-08-28 15:44:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 5e08d96f-1317-3343-a74a-8ee280e597a8 | -15.30721 | -41.40841 | 2026-08-28 15:44:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| bd25e926-9bd5-3f3b-9a22-9768d841c809 | -17.52032 | -42.00656 | 2026-08-28 15:44:00 | NPP-375 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 06a8b956-445a-3c90-9e50-ea212572dd08 | -17.80808 | -42.25051 | 2026-08-28 15:44:00 | NPP-375 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| eb3d30a0-766b-3d0e-be9d-8e9972273b57 | -16.38025 | -42.98096 | 2026-08-28 15:44:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e2978a42-d927-3fc9-baf9-0500ded6a9c6 | -10.21643 | -38.52317 | 2026-08-28 15:46:00 | NPP-375 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 91c02d02-8f44-3fa3-82e8-0eab798c7a5f | -7.08183 | -42.19447 | 2026-08-28 15:46:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a1bfdab2-4a46-3c84-b847-b6fd56b4ce75 | -12.86971 | -44.3603 | 2026-08-28 15:46:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a029441b-9bd1-3d38-9307-cd058435d787 | -7.31358 | -42.9645 | 2026-08-28 15:46:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 19785c25-e51d-3807-81a6-e29bce19223c | -12.86909 | -44.3522 | 2026-08-28 15:46:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0a0c8c70-cc97-3f0a-b9b6-e7d9bc9ec8ca | -7.62565 | -44.82075 | 2026-08-28 15:46:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 051b0d79-2b97-3e1e-b82f-d22bf40eeae1 | -7.21093 | -42.76038 | 2026-08-28 15:46:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 88c0d4d5-106c-3f5a-960b-884f3d10e513 | -7.20344 | -42.73618 | 2026-08-28 15:46:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 7389e564-a79f-33aa-b073-44657b93b58a | -7.29207 | -38.87024 | 2026-08-28 15:46:00 | NPP-375 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 3e706918-f254-33f0-8782-f3933ccac7fd | -8.03678 | -44.15918 | 2026-08-28 15:46:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| eb76e674-0d71-3937-8830-1c919b7d1f59 | -12.4978 | -43.76925 | 2026-08-28 15:46:00 | NPP-375 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0b66a74-fc46-318e-8cdf-7e98fbadb2f0 | -13.82243 | -42.17228 | 2026-08-28 15:46:00 | NPP-375 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b56f4a79-8b6d-3bef-8fce-d760e8d2f342 | -12.62012 | -40.31211 | 2026-08-28 15:46:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 786f4443-defd-38f8-9803-5540b7e4d69b | -7.7168 | -43.92133 | 2026-08-28 15:46:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5068110e-df23-310e-9178-637c6d1a799c | -11.41356 | -42.30579 | 2026-08-28 15:46:00 | NPP-375 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| aaf0ad58-0d0b-3e9d-abcb-76674484bc23 | -8.50949 | -39.58395 | 2026-08-28 15:46:00 | NPP-375 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2a2c2db6-226d-310c-b2d9-7020bcf4b4a2 | -12.86178 | -44.35285 | 2026-08-28 15:46:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| dbbf36c4-7c80-324e-bd80-0752a09bbfe0 | -7.81382 | -43.88858 | 2026-08-28 15:46:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2559552d-99ea-3055-84e8-950454f7a24b | -8.22007 | -36.10595 | 2026-08-28 15:46:00 | NPP-375 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e983a523-a104-3611-8fd3-149190155e12 | -9.79539 | -43.5514 | 2026-08-28 15:46:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 457e348b-281c-3f71-b698-587428c321f6 | -13.7521 | -43.50397 | 2026-08-28 15:46:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 556dcfae-40e6-3e5e-b429-730e2b0db8af | -8.51155 | -39.58504 | 2026-08-28 15:46:00 | NPP-375 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a91f2ea9-d945-3bbf-97b5-b23ab0af5ebe | -12.86984 | -44.3597 | 2026-08-28 15:46:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d1767ec0-dd34-37d2-acd5-bca9346d5a11 | -9.06584 | -40.16154 | 2026-08-28 15:46:00 | NPP-375 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dc2bc658-12dd-3de0-a38b-7e2c9cf44c41 | -8.69898 | -39.23144 | 2026-08-28 15:46:00 | NPP-375 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| abd3b1f9-8968-37d6-9bc8-94b58b4c9179 | -7.07703 | -42.20424 | 2026-08-28 15:46:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 4456df4e-9496-3f9f-8db0-d31fa6a63c85 | -9.99536 | -36.38169 | 2026-08-28 15:46:00 | NPP-375 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 6c944d0d-6094-3e76-82c9-17de31927f3a | -12.09417 | -39.70462 | 2026-08-28 15:46:00 | NPP-375 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 31895c05-5b51-3a3a-9691-eb4f1ad2dc13 | -13.11353 | -40.88349 | 2026-08-28 15:46:00 | NPP-375 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 69753bd8-7fee-3d5a-8500-5a07fa493f7e | -10.00012 | -36.38499 | 2026-08-28 15:46:00 | NPP-375 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| c04d5ace-502e-3645-861b-77cab8db44d2 | -7.28726 | -38.87077 | 2026-08-28 15:46:00 | NPP-375 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 8829e3d0-0e05-3921-8da2-ab7d504eae4f | -14.07878 | -42.30221 | 2026-08-28 15:46:00 | NPP-375 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 016f8eb4-7c0d-3020-9636-3a462ff27c03 | -8.50642 | -39.58574 | 2026-08-28 15:46:00 | NPP-375 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8ce6a92a-1e8b-3222-ae9e-4cc5e97fd130 | -7.09657 | -42.82589 | 2026-08-28 15:46:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 69668187-4132-3ba5-ab2c-5cc922631e94 | -6.91773 | -38.49024 | 2026-08-28 15:46:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a70bbb50-137f-36cd-8166-fd5b79516639 | -13.12326 | -39.90816 | 2026-08-28 15:46:00 | NPP-375 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a0b21853-6e85-374b-bb65-84ce927945cb | -7.73843 | -44.73673 | 2026-08-28 15:46:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f182bf30-8694-36d3-a8bb-b9f256b83de4 | -9.04099 | -41.61046 | 2026-08-28 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b18ca981-086a-3cfb-afbe-8e621fbbc173 | -9.7968 | -43.5632 | 2026-08-28 15:46:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 3063f3ec-e533-37e0-9aa6-e69cc14ac6af | -7.81311 | -43.88288 | 2026-08-28 15:46:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ded047e1-3734-3b3c-be1e-acd2acde9ed7 | -7.81089 | -43.88544 | 2026-08-28 15:46:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8a1147f6-dba0-3327-9a95-f726b0cf7366 | -7.19721 | -42.73673 | 2026-08-28 15:46:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b19112f7-c77b-3cfc-978c-837ffbe1396f | -12.4985 | -43.77599 | 2026-08-28 15:46:00 | NPP-375 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11858b81-59c7-3bd3-a5c5-fa3bc600c14b | -8.31425 | -39.02036 | 2026-08-28 15:46:00 | NPP-375 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| f104ec41-446c-3e9a-9e8a-ba74cece5692 | -7.26867 | -45.34795 | 2026-08-28 15:46:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7e85c0a0-7a54-355f-b1bb-944ba7b3e9d0 | -7.52886 | -44.45973 | 2026-08-28 15:46:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b724a13f-e8f3-36e1-97d6-69c31cd4b917 | -12.49282 | -43.77074 | 2026-08-28 15:46:00 | NPP-375 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3b23eaad-8f69-3e0d-a042-62acae26f5a8 | -7.62269 | -44.81625 | 2026-08-28 15:46:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |


[Clique aqui para ver as próximas entradas](README86.md)
