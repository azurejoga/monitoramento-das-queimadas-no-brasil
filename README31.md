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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ed0d3dc-efb3-3b28-8e25-e5999f8b799a | -3.23842 | -45.37945 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9665c650-a4be-3265-ad14-d4b2785952ae | -2.72667 | -46.6927 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efdff59b-bead-339d-83fa-f198bb65466a | -2.27406 | -56.17463 | 2024-11-11 04:18:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f67df440-4ef6-3229-9add-850a9e61b3ee | -2.41991 | -48.86026 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17e23c73-139d-3b1d-807f-d6781fc68043 | -2.99854 | -49.52089 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05d07146-e682-3ece-8e0c-69c1a285d920 | -4.87406 | -45.77117 | 2024-11-11 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8673de93-1c09-34c2-a89e-170345dac6f0 | -1.25313 | -55.76678 | 2024-11-11 04:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bb100875-3874-301e-98c7-73dee02bcd15 | -3.53261 | -45.705 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0c912a6e-b9b5-308d-bfb4-6461f8aebc6e | -3.57167 | -52.30442 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57ce0bd1-4874-30df-9b58-e21fb626ac22 | -2.7371 | -45.21297 | 2024-11-11 04:18:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80167fac-e8b5-3a35-84e1-0cd1a8a5604a | -2.56271 | -47.34302 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d88b977-0800-3846-b245-6a9a22dada4b | -4.31543 | -46.38618 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64812686-7c7c-3657-9619-9f612a35040b | -3.14463 | -45.96962 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49ded6de-66fb-343d-b8c5-d04f9576d94e | -2.82015 | -46.64806 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a82b497-c8af-33d9-b674-48ddc504fb9e | -2.55627 | -45.97302 | 2024-11-11 04:18:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d90c6cca-1712-367f-803b-7eead879b5ef | -1.0845 | -46.77439 | 2024-11-11 04:18:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5310a3f9-d212-340f-a5e7-319c65647a11 | -2.36757 | -46.79525 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4013b07-dbb8-3799-ae2e-2d8ad0685513 | -1.35218 | -52.54121 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bb0c737-113b-309f-87ad-03ba64a47aa3 | -4.61733 | -46.6893 | 2024-11-11 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bfb2438-2e9d-3a65-a4e2-4ec34e929339 | -2.63502 | -46.80421 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a474f41a-1bc1-305a-8f35-0a29105571fc | -1.51804 | -55.00805 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 329728a5-e9ac-3e7a-923d-c0643de3f609 | -5.31515 | -43.73241 | 2024-11-11 04:18:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ec8453c-536b-3eb3-b86d-1c7fba95e1e3 | -1.39222 | -55.68943 | 2024-11-11 04:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdf9eb03-79f8-3b1f-a276-4a901f982a90 | -4.02814 | -46.96296 | 2024-11-11 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42cc018b-c827-320d-bce6-b7ac00674e73 | -2.40937 | -46.30434 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78360eb7-f895-345c-b78f-693d948edaf8 | -4.12396 | -43.5859 | 2024-11-11 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5a26fbb-3398-3492-bc1f-a8e5b96e2760 | -2.36009 | -46.67989 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b855394e-406f-3e54-8d08-f7758d3a4011 | -1.39635 | -52.3666 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c223efcb-ca96-3469-b346-30b611288684 | -2.17083 | -48.32417 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b70077c5-1b2a-3262-b88d-22dde339fbb0 | -0.97852 | -53.18275 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a4f7c61-9411-3658-9878-69d0cc66c29b | -2.97868 | -46.98668 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ba0e85b-822c-35dc-9aa4-543ea7303933 | -2.87395 | -46.64289 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79db89b9-53e5-3348-a32d-153a6d7f17ea | -2.19433 | -48.38014 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| d4ffee76-ea22-3dcb-ae50-397475189b2e | -2.23468 | -53.66548 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 334fe111-9720-3e77-9b70-caaa2fab510f | -2.75296 | -49.35589 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7883615b-010c-3b1d-8bbb-e53d7e87e7c6 | -2.66427 | -46.78345 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a694601-8850-3235-84d6-f8a65d2b0470 | -3.8656 | -45.01284 | 2024-11-11 04:18:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8923bded-0983-3716-ae5a-f353be4a7f5a | -3.02144 | -50.97546 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c608981a-c4fe-3e37-ba2b-86c981a84f33 | -2.2285 | -48.3961 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| dfc1e99b-dc99-366e-a43e-f4c5275f2b75 | -2.61148 | -47.95369 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bb6b95c-2837-303a-832c-1150eb234a66 | -3.6902 | -44.77338 | 2024-11-11 04:18:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a38e4ea-c82a-396c-9d25-8ad808948eca | -1.67515 | -52.06015 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2ae8a5d-3c59-3cfe-8f1d-2a7c782e9c37 | -2.27081 | -56.17551 | 2024-11-11 04:18:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b88d446-c219-3637-9ab0-02bd02a5fa03 | -2.92581 | -49.48997 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 061eddc9-ac6c-3751-b751-30713568a0c0 | -2.60725 | -47.73668 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57bea301-915f-3f5d-9673-7efadc87353d | -3.25787 | -53.69974 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73c3bf61-5d55-38c7-9193-06a5b54e1d95 | -1.55371 | -51.85422 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4fa1907-c6a1-372d-a302-8799df59d2e1 | -2.3565 | -46.67932 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1afd47ec-d1af-3ef0-9d06-2d5c94b58ba1 | -2.61278 | -49.2361 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 852ae5c2-4388-3b7b-95f9-d84a9ee8a241 | -2.12307 | -48.89902 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c678556-8072-3647-bfb9-2ae6728cbf64 | -2.36075 | -46.67579 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf3369f1-c3f2-3a8e-bf37-86957cf18885 | -2.57267 | -46.5444 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a7cd574-9834-3dc2-a1ff-2c39ffdb21db | -3.81496 | -52.30994 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a2346a6-01b6-355f-9123-a0063a2f8098 | -2.61195 | -46.16302 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c4f39af-6d73-3c1b-895f-aceb48cbc41f | -1.8492 | -46.58429 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d69b0336-8251-3ea1-879a-dabe0ec3ecab | -2.75471 | -49.37212 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 898f2781-4461-35f2-a670-b10bbb748d21 | -2.17562 | -46.7588 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d48a2221-13fc-32ce-b482-3f1c18563db5 | -3.01714 | -53.2576 | 2024-11-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cf88bcf-27eb-3801-a39a-bd78a88ececd | -1.47787 | -52.09406 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 668ae8de-256e-3093-ae40-5df8b8b78f83 | -3.53603 | -45.70554 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88336941-9e96-3e4f-8ca5-ab5a4e7cefc7 | -2.8256 | -49.44306 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55d631ab-72f2-3be1-94b3-707e40a72403 | -3.24926 | -46.49068 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50165d4a-66d3-3171-9703-97f3974b540e | -2.10483 | -46.52128 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49db497c-aa96-377c-b09a-272874bdc9a2 | -3.73532 | -44.53053 | 2024-11-11 04:18:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| feba30aa-0c1b-3627-a11f-91b0af635b75 | -2.36823 | -46.79113 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de2421f9-af89-38ab-9b3d-79c1136d3974 | -2.45942 | -48.59368 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 271bb179-8c34-349b-93c0-ed2923ce22fb | -4.02164 | -46.95775 | 2024-11-11 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfd6567b-f320-362b-9218-1a1de4f393ff | -4.12729 | -43.58642 | 2024-11-11 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 436bc638-23f8-3a91-adb8-336cb1caaea2 | -2.24547 | -46.51281 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fb1d00ec-7943-30f2-b23d-da4eefa95642 | -2.24606 | -53.66736 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8ffb3bb-0920-3b7b-94bf-60b78bd96e37 | -1.98259 | -46.4496 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c038ca0-5896-3a40-a5ff-f47e6505903d | -1.40473 | -52.37495 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39822d79-9ed1-315d-82f4-bec82dd1be25 | -2.06245 | -46.2899 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5499bbcc-41c0-3c2c-972f-18e284fd58c7 | -4.61382 | -46.68874 | 2024-11-11 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d2dfd71-0b5b-391c-b2c7-1bec768dd7d3 | -3.1377 | -45.96854 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff67b4f1-89d9-3834-ab0f-163998a32252 | -1.44481 | -51.66988 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 246a333c-28c9-313b-a667-68c0e2cbbe93 | -1.63963 | -50.44297 | 2024-11-11 04:18:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf465de5-dbf4-324c-a5a2-75df1005348a | -4.07312 | -43.95346 | 2024-11-11 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbc13dac-505f-3ddd-b239-5ee186984fce | -1.56855 | -45.78123 | 2024-11-11 04:18:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0b02eb7b-1f7f-3432-b2df-01e8e5ff242c | -2.24494 | -46.50516 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a53e698-1385-3f88-9211-ac085c909f59 | -2.46707 | -50.39348 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e3a31fe-4196-3397-8757-f9a090be6793 | -3.26972 | -53.69788 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f56aa5e6-accd-3687-9dc9-71ddbbce7b26 | -2.06753 | -46.34235 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71d19bab-a675-35b4-9f16-d39c14df843e | -0.21707 | -51.19996 | 2024-11-11 04:18:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd5b6c0-839b-3703-98b0-4e1f550af517 | -2.09638 | -46.52829 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cab88698-4217-3741-9914-695ee5da7a90 | -4.70479 | -46.39104 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7665266c-6c17-333c-a185-a50c28bb151d | -2.01432 | -48.41098 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c254ebd4-a5f3-3ecd-8c0a-aa3ad90a93ee | -0.65013 | -51.71468 | 2024-11-11 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee857996-198b-31db-913a-c81407ecbd0d | -2.36211 | -46.5757 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de74ed27-dc26-31fc-bbe7-278f76be1610 | -3.29565 | -45.32876 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d328ce9-601a-343b-954d-eedec0197f56 | -3.02934 | -48.04435 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fc3764f-55ea-388a-b49d-9165daf4cd5d | -2.31049 | -48.28129 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a945ce8b-61c2-3214-8ba7-b0047d1f7afd | -1.4059 | -52.37485 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1059a015-eb46-38f3-9357-f9df576a4ebc | -3.62734 | -44.84605 | 2024-11-11 04:18:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e83191f-c429-3f53-91c1-06f836fa6a85 | -2.565 | -47.35241 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 693ffdf0-c615-3ad4-b78a-b4f58dfe6afb | -3.28239 | -46.41941 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecb6c707-c2b8-3d10-b79c-dc1977b2eda8 | -3.028 | -45.82095 | 2024-11-11 04:18:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 141d7c0d-e1ef-30d3-9151-ed491b992d3a | -1.82919 | -47.86632 | 2024-11-11 04:18:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7054c52a-f7af-3596-8ba2-c1f2ef366b7f | -2.42255 | -46.68141 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f63bced5-2ff5-3e2a-ad44-dd5ac07be64c | -0.64725 | -51.71647 | 2024-11-11 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README32.md)
