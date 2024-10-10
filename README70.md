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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa8e7e66-6e04-36aa-88d7-aeaea17325e5 | -7.17162 | -44.068 | 2024-10-10 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 518d38c2-4e99-345c-a404-cfce8cdcd6ee | -9.93683 | -44.06688 | 2024-10-10 04:19:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1cf524c-a68e-3ff9-96cd-d23023c9b115 | -9.93401 | -44.06276 | 2024-10-10 04:19:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19fb7a03-bd43-3d88-8731-965c48890074 | -9.71398 | -45.47529 | 2024-10-10 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55d2e806-2a59-3f9c-896f-81716cb62fcd | -9.71343 | -45.47879 | 2024-10-10 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e66d64d-8b5c-3f68-8b51-ff35ba45fd3f | -9.55997 | -44.4295 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 803a5d1a-2ab8-31eb-a09b-22229cfbca9e | -9.55943 | -44.43304 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dd7572d-eedd-389b-8714-15a5ea060289 | -9.55888 | -44.43658 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74c0be65-d8f4-3da3-80e9-fab97f0def6a | -9.55723 | -44.44719 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73247b51-c90e-3aeb-9f73-cb9e050201ab | -9.55663 | -44.42897 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2eda3357-20d0-3ba9-9edf-2b0fd7f16f94 | -9.55608 | -44.43251 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d52c9b16-895b-3547-b723-0e681e4bda92 | -9.51028 | -44.07177 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffa65b04-9169-33b4-9696-e538c2d056a2 | -9.4263 | -44.13911 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07f42168-81e4-3cda-9c03-747af8e325d7 | -10.18536 | -43.87774 | 2024-10-10 04:19:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 169175f6-684e-3710-bf88-ac14972e20b1 | -9.53991 | -44.42634 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61f8809d-83f8-3bd4-8a01-53eb1b4a5b3c | -9.53602 | -44.42935 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 509535b9-5136-32da-b05a-0a689d48f8d5 | -9.52824 | -44.43537 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddf251b9-9da0-3671-9969-c4cffddbe189 | -9.5249 | -44.43484 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af3361a6-d2aa-3208-995d-bae41db8eb8c | -9.52435 | -44.43837 | 2024-10-10 04:19:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03221d2a-d0d7-3e5a-a863-e3a800889bce | -10.12522 | -45.20721 | 2024-10-10 04:19:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7410657-9608-3db2-b086-4cf10cf0daeb | -10.12467 | -45.21072 | 2024-10-10 04:19:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d8408810-43fd-3c57-a43f-a5e9560d5a3e | -10.1219 | -45.20669 | 2024-10-10 04:19:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce02dc66-4659-33b6-afcf-f36275c8272d | -10.12135 | -45.2102 | 2024-10-10 04:19:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc859412-a4c7-39ac-9c61-9d7e0896bdd3 | -10.11802 | -45.20967 | 2024-10-10 04:19:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5e850fe-62f2-34bc-b993-46846e773906 | -13.80204 | -44.62493 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b959b323-7251-3eb3-b788-3db86e64b92c | -13.79864 | -44.62439 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae48ab15-ec5e-3eda-b09f-6cf06d422cd2 | -9.88052 | -35.97568 | 2024-10-10 04:19:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ecfeac65-dbd3-30ac-ade1-1116dd72cf7b | -9.87962 | -35.98265 | 2024-10-10 04:19:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| a6c1d622-b560-37e7-a898-8e904ccf84e1 | -9.87465 | -35.97848 | 2024-10-10 04:19:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 00173c4b-1087-358a-b532-1e8ba0b3e3bf | -9.8742 | -35.98197 | 2024-10-10 04:19:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| d7ea1614-4bab-3cba-9ddd-e5e45ef34946 | -10.20547 | -36.22096 | 2024-10-10 04:19:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 62046036-bb0e-36a7-a498-063710000522 | -10.20502 | -36.22441 | 2024-10-10 04:19:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ddcf27e9-c72c-3b6d-9878-c377fed56445 | -10.2001 | -36.2203 | 2024-10-10 04:19:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 9b743db5-57fa-3898-b2c9-d42721182a41 | -10.19966 | -36.22371 | 2024-10-10 04:19:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 88a172f0-99c5-3bcc-8406-93323a31c7f9 | -7.94502 | -38.34725 | 2024-10-10 04:19:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 18fe2ac9-7fd7-3e0e-ad7c-3841f2540b73 | -8.62309 | -40.3893 | 2024-10-10 04:19:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 75e88edb-55db-3030-9b4a-76a70460c294 | -8.56833 | -40.65962 | 2024-10-10 04:19:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 19641efa-5ec5-35c8-91bb-fa89648b4f37 | -13.63002 | -40.87558 | 2024-10-10 04:19:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9e8e2a11-8e81-31b2-9c22-6b1fac610e44 | -13.97757 | -41.8752 | 2024-10-10 04:19:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 69316f1a-2cfd-349c-89e1-a1da05378ba6 | -13.97686 | -41.8802 | 2024-10-10 04:19:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 84e44782-be63-3b4c-b9ca-9f65c5a15efa | -13.97434 | -41.87758 | 2024-10-10 04:19:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4917083b-ebfe-3c8b-8dc6-7d62c95a162c | -13.76492 | -41.83743 | 2024-10-10 04:19:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 842c364e-9344-327a-87f1-0518627455d0 | -13.76415 | -41.83533 | 2024-10-10 04:19:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0923f88a-ccfa-3abc-bf1f-c79e67867bcf | -7.99218 | -40.97291 | 2024-10-10 04:19:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f5ff15b1-9b17-3a7e-8811-9a6383b79f35 | -7.61437 | -41.71922 | 2024-10-10 04:19:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a85484ff-6e0f-3944-a8f3-f38020c94bf2 | -7.36225 | -42.19084 | 2024-10-10 04:19:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ee4a8eb7-5b3b-3bec-8822-fde0544e4fe2 | -7.35931 | -42.18635 | 2024-10-10 04:19:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 27c987a0-5364-32ef-ac71-5ff9f319dc06 | -7.35872 | -42.1903 | 2024-10-10 04:19:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f5617c59-75de-3ae4-9efa-b0cee5017fca | -7.35579 | -42.1858 | 2024-10-10 04:19:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a1ac4b5-27ab-3fb0-85be-d1c8ab7fab9a | -7.3485 | -42.18927 | 2024-10-10 04:19:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd40adca-8fa1-3575-98b7-a4f6956a04cf | -7.3479 | -42.19319 | 2024-10-10 04:19:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0503298b-30d1-3a26-841d-9df440f3f072 | -7.34438 | -42.19263 | 2024-10-10 04:19:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b3e00c54-fb09-368c-addf-4d00a54264ca | -8.06581 | -41.10283 | 2024-10-10 04:19:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8b8eb38f-a34a-3f3f-b714-343c08eb7f57 | -10.7988 | -42.44852 | 2024-10-10 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ff8b8e2-9b5d-3312-837c-91e791a1a45c | -10.21655 | -42.45808 | 2024-10-10 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0805774-558c-3dda-964e-23f27be1b47b | -10.21296 | -42.45753 | 2024-10-10 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f74e6083-017e-3f27-8252-38f45121d550 | -10.20641 | -42.45234 | 2024-10-10 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c543d409-ac15-3f4e-962e-6fe734f6b7b4 | -11.95382 | -41.77226 | 2024-10-10 04:19:00 | NPP-375D | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b7bb6cc2-cfb3-3990-8c0d-a11968c37b16 | -11.21764 | -41.60239 | 2024-10-10 04:19:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef7de673-26d8-38c8-91e0-8d19e3a58b27 | -11.08858 | -41.5375 | 2024-10-10 04:19:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1ebaa554-12b7-3ce0-9e2c-bcaf05d0a0d0 | -11.03193 | -42.89532 | 2024-10-10 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2cc79b4b-eba6-308a-8963-677a7f06f127 | -11.02878 | -42.89532 | 2024-10-10 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e65cabf3-c722-310a-bbd3-01fef61e922e | -11.02838 | -42.89477 | 2024-10-10 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b6676f5c-942c-3909-a30f-f2f9eb8158ec | -11.0278 | -42.89879 | 2024-10-10 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c59e6484-391a-3734-8e6e-84aec933d736 | -11.02585 | -42.89076 | 2024-10-10 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71302c13-5139-367b-b993-0ac993cd3813 | -11.02543 | -42.89021 | 2024-10-10 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa30f3e7-ea94-35d3-8ee1-a95562fb9943 | -11.02524 | -42.89477 | 2024-10-10 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15bf0bca-9066-3612-b246-b80ad74079c6 | -11.01763 | -42.87309 | 2024-10-10 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4fdda3fe-109a-314a-9796-abf2cc52c4f2 | -14.03641 | -42.80516 | 2024-10-10 04:19:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8ee9448d-ff25-3f24-b1bb-7982634838d3 | -13.84885 | -42.63802 | 2024-10-10 04:19:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 092c83dc-b2de-30f2-9c41-fae1331ede97 | -13.82769 | -42.4129 | 2024-10-10 04:19:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ba23d65f-5f19-3e98-819a-32fcb88ac457 | -13.72026 | -43.0913 | 2024-10-10 04:19:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 25c4cf1f-10d9-37fd-8eed-dedaf84fff61 | -7.82934 | -42.45852 | 2024-10-10 04:19:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fe543552-83e0-37a7-87fc-e0d19cf5bf97 | -7.82874 | -42.46243 | 2024-10-10 04:19:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 71faf1a0-8fc7-3d3d-ba48-d58e8fdb07bc | -7.82814 | -42.46637 | 2024-10-10 04:19:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 79820545-9b5a-3625-9e28-80ad8fed7d62 | -7.82465 | -42.46579 | 2024-10-10 04:19:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d2e0c38c-c690-3c19-9a6b-67a653045996 | -7.79371 | -43.09964 | 2024-10-10 04:19:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 08fa3b0b-27b6-3a47-b3a5-8f4aefec99a5 | -7.79029 | -43.09911 | 2024-10-10 04:19:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 505365ba-1371-3be5-b9d0-1ac213632794 | -7.78973 | -43.10278 | 2024-10-10 04:19:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 30f4e3e1-6dd2-31d6-a333-48f3a05a7c77 | -7.77997 | -43.07497 | 2024-10-10 04:19:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 74008d4e-cae5-3b86-b6a4-263b27553b69 | -7.77712 | -43.07075 | 2024-10-10 04:19:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f42f7518-0dd0-3701-bf8c-825fdd0f1882 | -7.77438 | -43.11176 | 2024-10-10 04:19:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 73edf2fb-28c4-3790-975d-1268343580d7 | -7.7737 | -43.07021 | 2024-10-10 04:19:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6856964f-cc01-382b-9d5f-1783a2170611 | -7.77096 | -43.11123 | 2024-10-10 04:19:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 15266021-83f0-338b-a1f9-53a9efbf89a4 | -7.72998 | -43.03743 | 2024-10-10 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fd4c78c1-a8a2-3c87-8e9a-f5ddbb0edd03 | -7.72655 | -43.0369 | 2024-10-10 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 68bec83a-5913-3dc3-9ff4-0e13007bad30 | -7.72599 | -43.0406 | 2024-10-10 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8fdc9971-23b7-3d96-ad4d-9c568129d7a9 | -7.6917 | -42.98972 | 2024-10-10 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6c3cfe40-ebdc-388a-9e3a-55ad69985d60 | -7.69114 | -42.99341 | 2024-10-10 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0d632e86-d72a-3299-91d8-4de4b477a217 | -7.68827 | -42.98919 | 2024-10-10 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4610034c-35c5-3a39-8ac9-9520e16973df | -7.68771 | -42.99289 | 2024-10-10 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f60898f6-fd09-3110-bf06-e0a2cd46973f | -7.68429 | -42.99234 | 2024-10-10 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7da45863-45d6-354f-987d-0dce73f252d1 | -7.67367 | -42.49077 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 38d5f1cd-b451-345b-9b26-4c52b03a08e5 | -7.67309 | -42.49461 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e56c16a2-a149-3b61-8149-712bed3a5b95 | -7.67018 | -42.49023 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 14efd118-e4ab-3a64-bc7b-2cf04d9d624e | -7.6696 | -42.49408 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 56b0d4a5-71be-31e8-b660-183f587cd750 | -7.66727 | -42.48585 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 01f88b88-f4e6-35d7-ab1f-fedf8bf62b95 | -7.6644 | -42.40987 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 02d0a140-4c9a-343b-939e-174fa8b94616 | -7.66382 | -42.41378 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a23eb166-c5d0-3f19-b01c-564e448b0e12 | -7.66147 | -42.54786 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README71.md)
