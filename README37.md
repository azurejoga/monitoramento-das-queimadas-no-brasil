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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f3dcbe8-4a79-3f02-8ac7-baf81f9bd44a | -2.06975 | -53.29452 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94c36906-3703-3a2b-9c1b-a6ba4ff3c629 | -1.37856 | -52.41016 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b97a9d67-12c5-392f-96cc-336d6fcd54e9 | -3.34292 | -46.42379 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1bf9351-a96a-3d9c-8731-38b75111a4cf | -3.57117 | -52.30746 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 069d1d6e-7fd9-32d4-9009-3c65c5814392 | -1.98089 | -46.81243 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8281f4ea-71bd-32fc-83a1-9c0047c64a72 | -3.10595 | -45.96739 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92b5cabe-1306-340e-a931-9d7d3bc96202 | -2.63437 | -49.5251 | 2024-11-11 04:18:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffd9e2fd-cc60-3333-90c1-42d9fc65d38b | -1.84986 | -46.58017 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 760fd8d3-49f6-3bfb-99d9-239b9fbb455d | -2.08556 | -46.48084 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ae778e1-2270-353b-b258-1bcb235fb2f9 | -1.49048 | -51.74014 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d147b6c0-bf7b-36fe-b05e-0a85ec17941c | -3.09265 | -49.55092 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0084ded2-53ca-3621-91c9-6bebe7321318 | -2.41278 | -46.26057 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0304958-82e5-373a-bb44-10fec659702b | -2.87692 | -45.36814 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 036b3683-6a64-3120-9d86-7c33ca398e7f | -1.97725 | -46.8101 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebbee9a7-9e9b-3111-bb9c-37be6cc09e21 | -3.24236 | -46.30553 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb32b9ee-c5b0-3078-aec0-46efe802fa3f | -2.24775 | -53.73852 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 68a0592d-e3ba-3f78-b1b1-c2071f4ccdaa | -3.5564 | -44.95774 | 2024-11-11 04:18:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a237b3af-0391-3ca8-8e95-c85470cc7cf6 | -2.28785 | -48.54773 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5ada212-f38b-313e-ad2b-c78b701007da | 0.4503 | -50.96376 | 2024-11-11 04:18:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2e317cc-78d6-3618-b80d-41719bc7e8d0 | -2.97673 | -47.91679 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 150c50ff-d5d3-35d5-8b7a-d3314af58ed8 | -2.39821 | -48.50659 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0af7b27-3b5d-3098-84bd-63d7b4d0d150 | -1.35257 | -49.07819 | 2024-11-11 04:18:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f0a059a-f5c0-39cc-9220-63f14e1b58cd | -2.1769 | -46.70378 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21f01c3e-a50a-33f2-aca1-09f1537dbfc6 | -5.09496 | -45.5406 | 2024-11-11 04:18:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3e67a17-0fcd-3064-a4a1-0ded5385c9fa | -3.11227 | -45.97223 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 870da37c-3dca-30f0-a04e-a2f6e7567399 | -2.63029 | -46.16505 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddcbc7e6-80e4-374b-8ebb-eb568dc11a9b | -2.37251 | -46.74091 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fe8c03e-b0df-3d0c-98d9-3f0b3cf45aa0 | -2.97802 | -46.99084 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 260aab76-dfed-33b2-bcf5-8a65fdfee180 | -1.40061 | -52.37397 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d1f5158-fc55-3b0c-af6f-b1f983fce5ee | -2.12805 | -48.55808 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26e5c49d-7dfb-31cd-9189-2e183eee04e0 | -2.29844 | -46.52525 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff23c450-855c-363c-a14f-f0bd10408365 | -4.68233 | -46.37582 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f40c228-117a-32c9-a2cc-6b1b91ffbbee | -0.03749 | -50.77657 | 2024-11-11 04:18:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63122375-6971-31d1-8135-673874c0b9a2 | -2.41469 | -46.52182 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4975dd93-d486-359a-966e-83d693ed2fd0 | -3.03242 | -48.04972 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95da0abc-8a5d-3d93-a24a-0085a2faf170 | -1.51335 | -54.99766 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cdcc3bb-cb94-3322-8d02-031fe6406651 | -2.84408 | -48.67614 | 2024-11-11 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58180f70-e611-3ad6-91ae-ae23840b57be | -2.6754 | -46.80624 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dde345a-bb20-344f-8e7c-50982d93b502 | -3.78372 | -46.66798 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c0aa402-a323-31f4-bf54-e644e1ab47bc | -2.2232 | -46.41109 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48cdc71b-08d5-3063-a317-f0406034d78b | -2.65078 | -46.79827 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59fed549-29e1-32e9-ba57-c4b8139bfc6a | -5.3777 | -42.76897 | 2024-11-11 04:18:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0ac5ebbb-6e3e-311b-a602-4cb01bc94dfa | -3.47904 | -53.4915 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09339177-4546-3219-b45b-66effbd08c39 | -2.69342 | -46.80923 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 841e895f-8ebc-3b26-ad28-918f8b8ede63 | -1.71671 | -52.47651 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c16240d9-4836-3e29-940f-b49b15acb670 | -2.23727 | -48.39226 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29e6e35a-450a-311f-aca6-0ee1e2154be1 | -3.03551 | -48.05511 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8241b57c-b80f-3ee9-bfb1-7c8c943a2ad1 | -4.5916 | -47.07341 | 2024-11-11 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5cbdda13-8c3f-3f04-9f92-8fe230f04acc | -3.19816 | -50.27887 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0a4eeb68-98fa-3c65-8480-449cc18f5264 | -2.39616 | -46.77862 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef18479c-853a-3af2-94df-5e7c74ed258c | -4.02388 | -46.96655 | 2024-11-11 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc6566f6-7e91-3570-82b9-54e108cae98c | -1.51596 | -55.00209 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 509f6043-849e-3c52-aa24-ee398faa3438 | -2.10418 | -46.52536 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45132966-5a28-3e2a-9c53-d1bbe3a7f1b6 | -3.54179 | -43.17468 | 2024-11-11 04:18:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 243f50db-640c-3a9f-b234-2c94576019ad | -2.22709 | -53.67614 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| a0109bc3-fe40-3f06-9dbb-0df802532f7a | -3.88209 | -52.39132 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37408b1d-9d1b-3259-a74c-1d7f63507adc | -2.92519 | -49.49387 | 2024-11-11 04:18:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79b18202-634c-305a-96cd-83b686af3b86 | -3.68663 | -45.24302 | 2024-11-11 04:18:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 485a0aca-ddde-31b9-a505-3f7f4cb35f90 | -2.4124 | -46.51322 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f01cb5c-083d-3861-b052-30874d089ef6 | -2.55754 | -45.5323 | 2024-11-11 04:18:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1293322-9be5-3743-b4c6-af3b724ce6c0 | -3.73199 | -44.53001 | 2024-11-11 04:18:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e0579db-8048-3b1d-b4e9-1297417b9726 | -3.00278 | -49.52158 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea3277bb-66bc-31d6-8e3b-08ca4967a6cb | -1.62059 | -52.53147 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abe51ccb-57db-3716-913c-baaa5ab22007 | -2.22616 | -48.38519 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df66b7fe-aed5-3de2-a2f8-b8aea2528c9e | -3.06088 | -48.04459 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bdc772c4-7223-341f-8a07-9b82e01eca14 | -4.5426 | -43.57242 | 2024-11-11 04:18:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07b92bef-27d7-37c7-ab14-b8c2ff5f78d9 | -1.40112 | -52.37072 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a9423be-ee83-3dc4-b787-3588637ff3bb | -2.2445 | -48.3802 | 2024-11-11 04:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 8a09836a-386d-3ef4-9250-82cf984cb552 | -2.2482 | -53.6619 | 2024-11-11 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 26b5dc15-f4c5-33aa-822d-7a34b92b7080 | -2.2114 | -53.6626 | 2024-11-11 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c4690dba-343f-3084-acdc-6e2ca3989d0d | -3.1458 | -54.4859 | 2024-11-11 04:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 93d0e0aa-5a11-3f51-8c5f-ba85735a45e7 | -2.248 | -53.7426 | 2024-11-11 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 2eb6dc14-a74e-3163-905d-29a202e68460 | -2.2259 | -48.4021 | 2024-11-11 04:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 389df347-e2e3-30cb-880b-b8a04e17e6c9 | -2.2663 | -53.7422 | 2024-11-11 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7a4e9f68-2775-3421-bd01-ecfe5e9377c5 | -2.226 | -48.3806 | 2024-11-11 04:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| d2372019-e6f7-39d6-886b-1e423eb40b31 | -17.2933 | -57.4857 | 2024-11-11 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| be5e2646-94c5-3b26-8347-c53a67d4f4ad | -17.5872 | -57.5328 | 2024-11-11 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 7bfe6a0b-de83-32ca-919e-68c6ffdffd82 | -2.248 | -53.7224 | 2024-11-11 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 0f53a85b-5a08-321b-97c2-114e0be54447 | -17.2737 | -57.488 | 2024-11-11 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 613aee59-1a20-35ab-94c9-2122e659f637 | -17.6073 | -57.5099 | 2024-11-11 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.4 |
| 41e08f3a-4ed8-350c-8e5d-04cb4dde0f7f | -2.2298 | -53.6623 | 2024-11-11 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| c4440650-c9bd-3726-9cbf-899e07b3bcf6 | -17.6463 | -57.5257 | 2024-11-11 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 3ba27367-14a3-3d7b-8a1c-0a326792157e | -17.6266 | -57.5281 | 2024-11-11 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.4 |
| 83b757cc-010e-370c-a56d-80899e08b98c | -17.5875 | -57.5122 | 2024-11-11 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 63fed01a-bd3b-3daa-b02d-9551012f45f9 | -17.2936 | -57.4652 | 2024-11-11 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 48702c2f-fd1d-3e88-87d1-f433b60d32e0 | -2.2444 | -48.4017 | 2024-11-11 04:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 6a23ab04-a87d-3c1e-854b-a6341891147b | -2.2297 | -53.6824 | 2024-11-11 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a393cdf7-3276-327d-aa02-b4a9e3664bdd | -2.189 | -48.3815 | 2024-11-11 04:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 09079426-e988-3540-a5f5-bbcbdcb3bf51 | -17.6069 | -57.5304 | 2024-11-11 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.2 |
| 135649d2-a23e-3311-ad2f-173c4a778992 | -2.7587 | -49.3497 | 2024-11-11 04:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c8b84474-0f52-3749-9157-03100ef56eef | -7.43656 | -39.7658 | 2024-11-11 04:21:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 37f7e5b3-fdea-3176-834c-ddfc5865ec99 | -9.10784 | -35.56487 | 2024-11-11 04:21:00 | NPP-375D | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b8f95420-e7fa-38dd-b5b2-806a85a3b828 | -7.43193 | -39.76922 | 2024-11-11 04:21:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b045c732-922e-36d4-a103-eb327b2d6187 | -7.43249 | -39.76534 | 2024-11-11 04:21:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7e871127-0ff7-3370-8038-435dc1065437 | -6.95097 | -47.78686 | 2024-11-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed09592f-8b60-3a15-958c-7c4311ae0fea | -7.63179 | -40.04451 | 2024-11-11 04:21:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d488b5fc-21d2-3779-8831-ded73404f309 | -9.5968 | -36.01729 | 2024-11-11 04:21:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4d97ab19-f572-38e1-be3d-ca9db1278885 | -7.62704 | -40.0491 | 2024-11-11 04:21:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d5081b89-0989-3a7b-8c85-94c24c5b3b63 | -7.62781 | -40.04389 | 2024-11-11 04:21:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 391c453d-34fe-3e03-ab60-c9c605b8922e | -7.43711 | -39.76202 | 2024-11-11 04:21:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
