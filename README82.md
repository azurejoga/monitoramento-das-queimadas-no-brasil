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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59399b60-2767-3de2-9d14-3318948a18f4 | -1.92864 | -46.45127 | 2024-11-21 12:48:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b5ba2785-d126-3328-b9b5-20c1a4b09e27 | -3.26209 | -50.82143 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| dde44c43-76fa-311c-a271-5249cc841694 | -3.50455 | -44.71397 | 2024-11-21 12:48:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 60a9441a-c9ca-3400-b24a-f1b0123ba99c | -1.46824 | -47.53855 | 2024-11-21 12:48:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 5b7e5409-3fac-3585-b987-a838d030028d | -3.51022 | -42.03465 | 2024-11-21 12:48:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 58.9 |
| db0a98c5-c210-3071-982a-7ea6c95fb0da | -4.11277 | -51.04678 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 903b7e37-d832-363b-a14d-f369222698e7 | -2.63628 | -46.21706 | 2024-11-21 12:48:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c7914243-c5db-3b10-9696-66c6c4efedb3 | -2.84148 | -51.81613 | 2024-11-21 12:48:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7b854650-75be-390d-855a-9771d4fde9ff | -3.39913 | -50.2529 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 20597131-3dcd-373a-85d8-234290fed0de | -2.94696 | -53.71028 | 2024-11-21 12:48:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 0b1cb4fa-da31-3a30-b552-d2235a7a3757 | -3.30059 | -50.36023 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| a45092ff-6ab5-3ff1-a266-187dc3af0668 | -3.59315 | -43.63552 | 2024-11-21 12:48:00 | TERRA_M-T | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| e6bfd380-df58-342c-9c2a-1a67c7379af1 | -2.38778 | -46.02193 | 2024-11-21 12:48:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 2f70fb2c-dcef-3e65-af2e-9c73c24df0b2 | -5.075 | -46.81693 | 2024-11-21 12:48:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 9ca404e9-a305-35cb-aa3c-c574b5c027ad | -6.23048 | -44.82547 | 2024-11-21 12:48:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 9220c4df-a6a0-3fe8-9988-4bb71bd67b9a | -4.93602 | -48.50798 | 2024-11-21 12:48:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 049477cb-0e2b-3ce8-bead-ff7296e924d0 | -4.14456 | -43.88284 | 2024-11-21 12:48:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| e681f3eb-9a54-38c1-9d56-23c93aa3cb70 | -3.50694 | -44.72109 | 2024-11-21 12:48:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 5ef6de49-b622-3397-8ed3-c0fd66071092 | -4.92719 | -48.50674 | 2024-11-21 12:48:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| d8687de1-7df7-32a7-9c34-1c22cdb6e576 | -4.50732 | -43.48854 | 2024-11-21 12:48:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 5d2e4531-f297-3048-92c4-b0236425c7d1 | -1.47855 | -52.5059 | 2024-11-21 12:48:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 5a987efd-aac6-37fe-bb98-d3731f90427e | -6.04808 | -46.06323 | 2024-11-21 12:48:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 096065ca-8b4c-3479-9a62-0c18c44ba793 | -1.99222 | -47.48029 | 2024-11-21 12:48:00 | TERRA_M-T | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| b465459b-ac59-390b-91ea-5cafa420c0d3 | -3.36487 | -43.46222 | 2024-11-21 12:48:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d5426647-a9f9-361a-b8e0-27776aebaa3e | -2.56023 | -50.64048 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f36b4009-d5f5-3e76-b3ee-6b7b4c6a6326 | -3.7324 | -42.52021 | 2024-11-21 12:48:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 600c434d-c9e3-3e23-9d8a-338426004197 | -1.55474 | -47.31546 | 2024-11-21 12:48:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f97f55a3-a2a0-3930-b7c0-40af0b7104a5 | -3.59522 | -43.62043 | 2024-11-21 12:48:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5aa6549e-4c20-321f-ad35-7611755356be | -4.11125 | -51.05707 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 4053e077-8401-3bcd-8c7a-8c3887facffe | -3.35475 | -50.18177 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5838d6e6-b861-3875-b9ee-cf95036f354f | -2.41129 | -48.61349 | 2024-11-21 12:48:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c872742e-c6c3-3054-9df4-7d58575d3c77 | -4.66299 | -46.53755 | 2024-11-21 12:48:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 414.1 |
| 3f249f3b-b575-3a06-a88a-8a2ba64965cd | -2.69496 | -46.25154 | 2024-11-21 12:48:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 98250d8a-d032-3fc5-868b-86914078de15 | -4.21161 | -48.72434 | 2024-11-21 12:48:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3228a2e8-fbb7-3f73-aa24-0a4b8bd23557 | -5.06308 | -45.05635 | 2024-11-21 12:48:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 88e28548-6a32-3b89-bfc2-4da4075ed368 | -3.03417 | -49.46834 | 2024-11-21 12:48:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 447dd226-e4b4-387e-88ea-4df154d88330 | -4.83105 | -48.84572 | 2024-11-21 12:48:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bb80d94d-7329-3874-967a-e38da336f49c | -4.7377 | -44.07946 | 2024-11-21 12:48:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 10aed955-b808-3e5a-aeaa-90e0b7ae949d | -4.16077 | -43.92987 | 2024-11-21 12:48:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1eef3081-e4aa-3b7f-916d-f107f41ad934 | -5.3206 | -47.30092 | 2024-11-21 12:48:00 | TERRA_M-T | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 39b15dc2-6377-3514-86d2-e8ef494558d2 | -4.16282 | -43.91535 | 2024-11-21 12:48:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 74b62200-c0a7-3301-83c1-1a52593659c8 | -3.84807 | -44.53296 | 2024-11-21 12:48:00 | TERRA_M-T | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3a80a896-2096-36d7-ab6f-9d4c1df8c470 | -3.07354 | -49.1987 | 2024-11-21 12:48:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 8a2a2725-7b75-36bf-9ea7-0752d9f645a8 | -5.45923 | -43.21939 | 2024-11-21 12:48:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 8cac3c86-a7c8-3b47-9aaf-82f661d0d8f5 | -4.74372 | -49.89376 | 2024-11-21 12:48:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 54ad0f65-6555-3b55-8119-2cc4a8b2a5d6 | -3.28453 | -53.8343 | 2024-11-21 12:48:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6d0e711b-b4f4-38e5-b699-d16ebb1e0dc7 | -6.12467 | -42.52202 | 2024-11-21 12:48:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 44931031-46ea-33c4-bd54-d26593dd5313 | -3.0118 | -51.00581 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f6ff2749-4866-34c7-8588-1c5cfca9d654 | -5.35766 | -46.45834 | 2024-11-21 12:48:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b5d59428-ac7b-31f8-b401-1802d6b7e206 | -1.67815 | -47.03704 | 2024-11-21 12:48:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 50fa80c2-a327-314a-96c0-174532d7f346 | -2.6338 | -47.96176 | 2024-11-21 12:48:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 95fe4165-90dd-3abe-90ea-7860d33fc333 | -4.00733 | -46.09629 | 2024-11-21 12:48:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c33545a1-8027-3768-8f3d-a3346408dce4 | -5.55225 | -44.33234 | 2024-11-21 12:48:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 585e5032-1fe3-3bca-b98a-21067f492b68 | -4.05889 | -49.27902 | 2024-11-21 12:48:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6536185f-2a79-3175-ae59-cc0a290cd751 | -5.10519 | -43.17646 | 2024-11-21 12:48:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d2bc5506-6790-3587-92e9-9eee08da98fb | -1.96531 | -46.45636 | 2024-11-21 12:48:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 322abed1-e3c5-333b-b64b-850c025379cc | -4.73573 | -44.09385 | 2024-11-21 12:48:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 2cb38744-b6e9-3c61-96db-a84f9e847e56 | -3.94673 | -44.06361 | 2024-11-21 12:48:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a114d3b4-f098-3e9a-b229-1468466a2071 | -2.10499 | -50.01194 | 2024-11-21 12:48:00 | TERRA_M-T | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| a868f10b-745b-387d-a259-0a38e183da0f | -3.6922 | -42.13787 | 2024-11-21 12:48:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 2433e71c-b0db-351b-b8f0-0abbcd41f7c1 | -1.45785 | -47.92253 | 2024-11-21 12:48:00 | TERRA_M-T | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 903f9551-5712-36f8-95f2-3b7254dd84c3 | -6.03209 | -46.10624 | 2024-11-21 12:48:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 41866dcb-1c5d-3be0-b62d-b03cb26d4ced | -2.44824 | -49.75111 | 2024-11-21 12:48:00 | TERRA_M-T | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0d9a70e7-2718-3603-beed-42518d2d0546 | -4.34329 | -48.32737 | 2024-11-21 12:48:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| aaebd822-1144-394e-bc52-2eec9b533b31 | -1.97377 | -46.45385 | 2024-11-21 12:48:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f19c3522-e825-36fd-a635-7e2c18891091 | -4.13161 | -50.16532 | 2024-11-21 12:48:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c5e9b54e-a98c-39f4-aa9f-0e6bbe150be2 | -3.36392 | -50.18301 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 12613972-4125-3159-8b63-309105d7fa95 | -3.29917 | -50.36992 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 372272c1-2978-3028-8577-0a4e6ade3e1a | -2.86715 | -49.85112 | 2024-11-21 12:48:00 | TERRA_M-T | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 4b0f4649-9204-3ada-965c-a4bdade9be08 | -5.00699 | -44.79604 | 2024-11-21 12:48:00 | TERRA_M-T | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e97348d3-e40f-34cb-a10d-033c4d974223 | -4.74242 | -48.05566 | 2024-11-21 12:48:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 77f2a109-057e-31ed-bc74-4193d1f95f7d | -3.26322 | -50.61564 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e2cc4b63-86dc-3949-987f-219d53bd383e | -3.5369 | -50.44252 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| ff145ff5-2d51-3472-8593-6d08d3a8a7b0 | -3.50904 | -42.0401 | 2024-11-21 12:48:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 487442a9-23a8-3443-bacb-e48855008cd3 | -3.19114 | -48.57533 | 2024-11-21 12:48:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 747f073d-94a2-3cc4-a06a-767f2ce5d239 | -3.54706 | -42.14605 | 2024-11-21 12:48:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 883f41ad-ce1f-3192-bce6-18ff78421fc7 | -3.51405 | -50.22652 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2a2a77df-9e2a-37ae-b0b6-3bc265b5ace1 | -3.50873 | -44.70863 | 2024-11-21 12:48:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ee440c49-106d-3d53-b688-454eb4a8011b | -3.54394 | -50.52326 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1b2f5f79-d833-372e-a636-d37fd99e3527 | -3.69486 | -42.11798 | 2024-11-21 12:48:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| da639d2c-de4c-322d-a9b1-8f464adbe07c | -2.25157 | -49.20108 | 2024-11-21 12:48:00 | TERRA_M-T | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| bbc00f29-2e68-334d-9b86-10317828d54c | -4.51123 | -43.48253 | 2024-11-21 12:48:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4ea1d2b5-cf1f-38dd-94c0-8ea3c5f49a00 | -4.96289 | -49.84462 | 2024-11-21 12:48:00 | TERRA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9d744551-3394-3ae9-805c-dd16739c0993 | -0.91781 | -47.82787 | 2024-11-21 12:48:00 | TERRA_M-T | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 2cbcafd2-453c-3c09-8bc3-a3e4d07ac9a7 | -2.48242 | -48.05966 | 2024-11-21 12:48:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dbc20ff7-d920-3a20-b86a-05384341416d | -1.42781 | -46.01956 | 2024-11-21 12:48:00 | TERRA_M-T | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 09abd790-a3dd-3508-93cf-186b24da06f6 | -4.67379 | -46.52879 | 2024-11-21 12:48:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| dc33dbe2-8a94-346c-914a-ef92eaab5f67 | -4.27951 | -43.74024 | 2024-11-21 12:48:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| c5636b4e-c21a-3ce5-9758-e2c8e5d10239 | -2.94114 | -44.09875 | 2024-11-21 12:48:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| d17e559e-5640-366e-b421-2cd86bab04e2 | -3.40434 | -46.24669 | 2024-11-21 12:48:00 | TERRA_M-T | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| e1734d28-5b78-3ec1-830d-2c2ade105ffd | -0.93804 | -47.75025 | 2024-11-21 12:48:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b62d9191-1b5c-3b63-b920-386a8f6c977a | -5.55423 | -44.31798 | 2024-11-21 12:48:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 97125275-6043-3c80-b597-12f43fabf14e | -3.20696 | -42.70599 | 2024-11-21 12:48:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| ffec1af1-f67b-35a4-9339-08e511e9ee41 | -2.6343 | -47.96 | 2024-11-21 12:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 32a4088e-5b7a-34f0-a924-8c6f12c7b068 | -2.0259 | -54.5289 | 2024-11-21 12:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| bd157cfb-4349-3c4a-b141-4626153c02d9 | -3.2951 | -53.8395 | 2024-11-21 12:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1fcff8a2-ef75-3321-943d-5d856e743202 | -6.1182 | -42.5086 | 2024-11-21 12:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| ceb8d1d1-aec2-3ca0-8b83-8ec59a9869d5 | -5.4548 | -43.2426 | 2024-11-21 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| de359853-f830-3db9-b67f-bb0233072e6c | -10.42477 | -44.48056 | 2024-11-21 12:50:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 14b86fd1-44b7-3b9b-89b3-a36a877675cd | -10.10147 | -45.9306 | 2024-11-21 12:50:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |


[Clique aqui para ver as próximas entradas](README83.md)
