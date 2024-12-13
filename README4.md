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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 283d5730-579c-3e9e-96b2-8cbc5912e722 | -4.21773 | -49.22187 | 2024-12-13 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| e9a27174-1a00-394c-b515-54f5e228965b | -7.57896 | -35.14588 | 2024-12-13 00:20:00 | TERRA_M-M | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 4d750bd4-6bfc-3f24-8edd-005fcb4efbf1 | -2.96715 | -40.23294 | 2024-12-13 00:20:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 23ac845d-ce7a-3f54-ba8e-0ef4af40180a | -4.53929 | -43.29792 | 2024-12-13 00:20:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0f8e6d40-a9aa-38d2-b467-8f468c4b997e | -4.65089 | -43.82293 | 2024-12-13 00:20:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 097148ef-f264-3dc8-9a85-7b67051c287d | -6.05924 | -44.04925 | 2024-12-13 00:20:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| e0013da1-292a-3e3e-8372-9fe3e5c1aba2 | -5.6271 | -44.84599 | 2024-12-13 00:20:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2ce920de-0aae-39ed-b5c6-54d51a3a7e04 | -3.36176 | -42.27372 | 2024-12-13 00:20:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a2b3f09f-44a0-38cb-ae87-79727b17a215 | -8.56575 | -36.42564 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 8d47ae2a-e634-306f-8a11-8889db6663cf | -11.77802 | -44.18126 | 2024-12-13 00:20:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f30d1f7b-003a-34fa-a110-3d98658557eb | -3.00324 | -40.22189 | 2024-12-13 00:20:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 842b760f-9c84-3a40-a430-ecc77b076ab5 | -6.92729 | -43.51923 | 2024-12-13 00:20:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 30c1174b-004c-3d3c-9604-9fdcb2b7d741 | -3.14707 | -46.3402 | 2024-12-13 00:20:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 79c33925-bebf-314b-a27a-b1cac5232829 | -4.25124 | -41.91989 | 2024-12-13 00:20:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 70dc4d2d-8cb4-339d-98ed-8a0943fb81fc | -3.0702 | -40.0423 | 2024-12-13 00:20:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 883418c0-dd63-30ef-b890-34f7cafd15c8 | -6.38367 | -35.45531 | 2024-12-13 00:20:00 | TERRA_M-M | SANTO ANTÔNIO | RIO GRANDE DO NORTE | Brasil | 2411502 | 24 | 33 | nan | nan | nan | Caatinga | 48.2 |
| ba3f9ab3-6452-3198-9463-794358fc5756 | -6.21043 | -43.27718 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 47843d01-73a5-3e01-aed5-e64b393e36ed | -5.46094 | -44.80818 | 2024-12-13 00:20:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 6fa4720a-2eb1-36fd-b6cc-b30ba2667a83 | -6.91704 | -43.52059 | 2024-12-13 00:20:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0f11f0c4-cd07-3519-82de-3227a37b235a | -0.75221 | -47.76208 | 2024-12-13 00:22:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 3e89b692-e35e-3640-a5f2-449a5dc5145c | -6.9349 | -43.4934 | 2024-12-13 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 755fd8e3-ace5-32ef-b0ae-a514569e9239 | -12.5497 | -57.7196 | 2024-12-13 00:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| fc0a078c-9a5c-34e9-ab09-66f512d78b42 | -2.4923 | -51.8233 | 2024-12-13 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 9f1b6e0a-60f9-3ffc-8549-d684ee2f8318 | -13.0641 | -52.0538 | 2024-12-13 00:30:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 24c17108-ff04-370d-abd4-e4c9d9639930 | -12.5495 | -57.7395 | 2024-12-13 00:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ba2a6c9f-67af-3281-af8f-7d29856c5e40 | -2.4924 | -51.7821 | 2024-12-13 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| dffdf6c8-7ae2-3c23-ae70-bb6015c1c58b | -1.62 | -46.6747 | 2024-12-13 00:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| bbfaa151-c887-35c0-8ae5-83c6a04dd1a1 | -2.5107 | -51.8228 | 2024-12-13 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 80d7b759-bfff-3eda-b20c-d33704a70232 | -6.9158 | -43.5185 | 2024-12-13 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 249.0 |
| 869d6c27-54e0-351e-9793-f2ed769f6c09 | -14.7848 | -52.642 | 2024-12-13 00:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d1fc14e4-2f26-3832-b80d-93f2ed68f8fb | -13.0644 | -52.0326 | 2024-12-13 00:30:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| b3cdf7a4-ccd6-318a-92b4-bdce52185fdf | -3.1449 | -45.5875 | 2024-12-13 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| cedf5118-a677-39d1-8a61-8c9ff273e117 | -2.7464 | -52.963 | 2024-12-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| cec93db2-b5d8-3b77-9a59-8e21b3ebada4 | -14.7655 | -52.6446 | 2024-12-13 00:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8fe9ada9-7ae7-3944-8871-4a259256edf7 | -2.8196 | -53.0832 | 2024-12-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a3a13978-35b5-3de1-abfd-6b3941674d38 | -5.211 | -43.2833 | 2024-12-13 00:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 9eb37aee-a6c7-3cbf-b655-3da701c5f2ac | -13.0836 | -52.0304 | 2024-12-13 00:30:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 04cd9f36-98b9-3019-9d0c-a3f33f3aef45 | -3.2685 | -46.9362 | 2024-12-13 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 812e113b-4372-3068-8ea6-15f0cdef328e | -2.5108 | -51.7817 | 2024-12-13 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a779c2e9-f533-3e68-898d-398dd09d8045 | -11.1959 | -53.8348 | 2024-12-13 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| f99fb0aa-d737-3bbd-b372-daf55b4e1d6c | -3.2935 | -45.6041 | 2024-12-13 00:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 68faf87a-b13a-3b38-b1e0-91c543da175d | -11.2148 | -53.833 | 2024-12-13 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9fc1a0d8-58ff-3f9c-a706-c580c7c1612e | -3.4784 | -45.7979 | 2024-12-13 00:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c6a84203-2775-363d-9436-c9b2b76de677 | -13.0648 | -52.0115 | 2024-12-13 00:30:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ae3b567b-8522-3da6-a4e7-36e33e8537c1 | -2.5108 | -51.8023 | 2024-12-13 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 4f9a991e-9f4d-3bd7-ad04-38ebb19a0a52 | -12.5307 | -57.7211 | 2024-12-13 00:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| fb6159c0-79da-3dee-9707-a0c865e1c18e | -3.15 | -53.2776 | 2024-12-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e9a22885-2de3-3da4-9f0a-725459b1048b | -5.2298 | -43.282 | 2024-12-13 00:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e2256209-76eb-3a71-b8ec-3a989c8da426 | -3.2686 | -46.9142 | 2024-12-13 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f39f0ff2-8e01-3f77-97df-76ee576f8d45 | -6.9161 | -43.4952 | 2024-12-13 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 13ecc827-0180-3a16-912a-f8ec6c22ac1e | -13.6933 | -54.7555 | 2024-12-13 00:30:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 98e27456-10b9-3314-ad5d-ce72bca2d350 | -6.9346 | -43.5168 | 2024-12-13 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 66474311-dc7a-306f-9c77-1cf3c3ff199b | -5.2108 | -43.3067 | 2024-12-13 00:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 3d0335d7-8fb8-3512-b530-eddba67813c2 | -2.8196 | -53.0629 | 2024-12-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0e4aa63f-3cdc-3a35-9988-3c7f60315165 | -11.2151 | -53.8125 | 2024-12-13 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c0c43091-0874-3de3-9ee8-52547244e37a | -2.4923 | -51.8027 | 2024-12-13 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 245.9 |
| d623a6ee-203c-36a6-bb38-b9b141739871 | -11.1962 | -53.8142 | 2024-12-13 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0da760f4-5e38-31ed-9424-c30bc1e2628a | -11.2151 | -53.8125 | 2024-12-13 00:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| db5f4828-aa71-3a4c-ad33-736a9e8fc6f8 | -0.767 | -47.7567 | 2024-12-13 00:40:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5e2ac876-27c2-3ec6-9083-e257f37f086d | -13.0641 | -52.0538 | 2024-12-13 00:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 621f6499-0eef-3310-ab75-b256c79cb5b6 | -13.6933 | -54.7555 | 2024-12-13 00:40:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e7d01693-7509-3cac-a3c8-a35a42db0664 | -12.5497 | -57.7196 | 2024-12-13 00:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 1eb60d6e-02ad-3508-a447-5dda9a006db9 | -12.5307 | -57.7211 | 2024-12-13 00:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 05dbd832-478a-38d2-b5a3-52726c23b7e0 | -13.0648 | -52.0115 | 2024-12-13 00:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| b54b84f8-7fa2-3d91-931d-fb2c333fd3b9 | -13.0836 | -52.0304 | 2024-12-13 00:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 495e5a38-7c75-30d2-a941-f8b67145ec3f | -6.9158 | -43.5185 | 2024-12-13 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 266.5 |
| a5f4e244-8da9-3485-b3f7-531a88ffad0a | -2.8196 | -53.0832 | 2024-12-13 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5ee0b1a8-1078-3827-9c2a-060519e90429 | -12.5499 | -57.6996 | 2024-12-13 00:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 24940c45-1232-3729-b9e8-0cf1d060e5ec | -2.4924 | -51.7821 | 2024-12-13 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d325df3e-efa7-31af-b9e0-3a08ec8af645 | -1.62 | -46.6526 | 2024-12-13 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 103e3e72-6971-3ca1-8aee-7989677544dd | -3.4784 | -45.7979 | 2024-12-13 00:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 283d6acf-1857-34af-8af1-2141b01c0d57 | -14.7848 | -52.642 | 2024-12-13 00:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| ae9c47c5-5ae1-32bf-b5ce-d0319f598473 | -5.211 | -43.2833 | 2024-12-13 00:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 6cc978f6-6630-356b-99d0-ae9b696c9591 | -12.5495 | -57.7395 | 2024-12-13 00:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f66d8e32-e34c-3ddc-9540-d6775d23c1fd | -1.62 | -46.6747 | 2024-12-13 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c1965a5f-ee75-3d74-97b8-bfb273b4b10d | -2.7464 | -52.963 | 2024-12-13 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 97ae041d-b472-38b2-968c-d3ac95c48c5a | -14.7655 | -52.6446 | 2024-12-13 00:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a9ec8375-3490-3aef-96f8-dae9c3fe10a5 | -11.1962 | -53.8142 | 2024-12-13 00:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| b7264f91-249e-3169-86d9-df39666bc478 | -6.9346 | -43.5168 | 2024-12-13 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 238.2 |
| a0b99a63-226b-3570-b05f-a6c68629b966 | -2.0076 | -54.5092 | 2024-12-13 00:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 1f3aaa4a-1ea0-3615-8583-82e58e7ffafd | -0.7486 | -47.7569 | 2024-12-13 00:40:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| fbdc5fa2-303c-3ea1-90bd-e8cee1967eb4 | -5.2108 | -43.3067 | 2024-12-13 00:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 4b4cd7da-bc84-34f8-8cd4-3e975bb62f3e | -3.1449 | -45.5875 | 2024-12-13 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f55c3593-a90e-3f44-9bfb-4781a52cb238 | -6.9161 | -43.4952 | 2024-12-13 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 4b711018-7d7d-3980-9025-501860760994 | -6.9349 | -43.4934 | 2024-12-13 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| ad8f8b03-28d8-3cfc-a6bf-9af73b63ea72 | -11.2148 | -53.833 | 2024-12-13 00:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 805a59c4-6668-34ca-ac53-b6c2b1af44bf | -11.1959 | -53.8348 | 2024-12-13 00:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| ac4688c2-80c6-3dec-9944-509dd6bb1c7e | -2.5108 | -51.8023 | 2024-12-13 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 2c092bbe-360e-3378-bad0-66474105e48d | -1.6385 | -46.6743 | 2024-12-13 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| d1c1c156-abd5-37e9-9637-9f8fadc3674e | -13.0453 | -52.0349 | 2024-12-13 00:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ca831d23-2a97-3cbf-a506-e118b0ddf0de | -2.5107 | -51.8228 | 2024-12-13 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 67293a5e-158d-35f1-bf6e-8ca0d17fae24 | -2.4923 | -51.8027 | 2024-12-13 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 215.9 |
| 8840b4ba-988e-37cb-93b1-88a03d30785b | -2.4923 | -51.8233 | 2024-12-13 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 97bd52f3-4514-32f1-8180-f565ae8c0908 | -13.0644 | -52.0326 | 2024-12-13 00:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 19ca80e1-c436-30a9-9d78-58faa89d62e9 | -2.8196 | -53.0629 | 2024-12-13 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9407ecaa-b374-34ec-8a0e-ea57a1153658 | -2.5108 | -51.7817 | 2024-12-13 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a868c428-028a-3233-965f-fb7c7759674a | -3.4784 | -45.7979 | 2024-12-13 00:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 48f21725-cbb8-3a75-a9da-63256a9a8058 | -2.4924 | -51.7821 | 2024-12-13 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 0110c2a2-7b2c-3aea-baea-bbfe6179e0d3 | -12.5497 | -57.7196 | 2024-12-13 00:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9e9249e6-d246-3768-902d-66671bd9f67d | -2.4923 | -51.8233 | 2024-12-13 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |


[Clique aqui para ver as próximas entradas](README5.md)
