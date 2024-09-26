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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23a6d5de-78f3-3165-be00-cf41d36b23a4 | -8.57841 | -53.35155 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f369824b-847d-3b26-a383-ca68887f461e | -8.53418 | -54.58272 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0c4f1367-5f46-3239-95d7-ea8f8a142b85 | -8.5336 | -54.56488 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cae7e57e-8bfc-3665-8e56-6143c47cfda9 | -8.53305 | -54.56834 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a97ad85-15e8-3ff3-a616-335d1d1fde4c | -8.53197 | -54.57527 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ac475a61-a2f7-3c43-a223-df7dd48c98c2 | -8.53142 | -54.57874 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1ab2773f-6703-3783-b056-84b7a9baea45 | -8.53088 | -54.5822 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c422e52-333f-302e-87ef-cb1179e31583 | -8.53084 | -54.56089 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ff98368-9775-363d-8b5f-3f2e10c46f79 | -8.53034 | -54.58566 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 267909f2-a4dc-373b-9bbf-8db5838cf58f | -8.52925 | -54.59259 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 101ceb9d-ddd3-31d0-9a76-d76732cd55b2 | -8.52921 | -54.57129 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d07634b0-f2b9-3b2e-afb9-ac9c19ae6984 | -8.52871 | -54.59605 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee575519-8aa8-3900-92a5-607b2ee225aa | -8.52867 | -54.57475 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b3ece73-dca5-3ea1-bae8-4e9c78dc1b2e | -8.52812 | -54.57821 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 016d5db8-5d05-31b0-b0f6-8d604c0e149e | -8.52758 | -54.58168 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6353493-87c3-315b-9e6d-305119e27b0c | -8.52704 | -54.58514 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0bbc6af-de8a-3509-ab0c-9c72c3420355 | -8.52699 | -54.56384 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a7261da-8534-3b4e-bcf7-21a0a13fe92a | -8.52595 | -54.59207 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1472312c-a94b-3443-ac68-10e75384e918 | -8.52537 | -54.57423 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d991145-2a3b-3bb7-a104-00f778770476 | -8.52482 | -54.57769 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a337fd5a-cd3a-3433-a887-af2633d8a7cb | -8.52207 | -54.57371 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f19c592c-34c9-39f3-9572-f718d8de0c3a | -8.52152 | -54.57717 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 764b4a68-4329-317b-86a0-a2915b575c04 | -8.52098 | -54.58064 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b84d314-02c3-3ce9-8015-7ed947a4624f | -8.51601 | -54.5692 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3a9e470-7030-35e9-9d06-3a52615fc153 | -8.50005 | -54.56313 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efa1430a-02f8-36cd-80df-067c59274152 | -8.4968 | -54.58392 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3efbbd63-f95f-3ae2-bdee-1a76b99fd20e | -8.49675 | -54.56261 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 719e668b-de54-3830-ba55-6fd14e219d75 | -8.46536 | -54.6286 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 625020b4-b652-396d-954f-0abc626b7561 | -8.46482 | -54.63206 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 255c36e7-54fb-34aa-b839-7eb716cb6931 | -8.45224 | -54.6691 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45ece116-3e7e-3bd5-a1f4-80e17f539055 | -8.45166 | -54.65127 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4f074d4-45a7-3b5b-bcc9-9f20de509e1f | -8.44894 | -54.66858 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e807219-7fff-3c30-8f08-93790d56923b | -8.44727 | -54.65767 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a405500-f59d-3bc0-b62c-a4bd3c863d91 | -8.44564 | -54.66806 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dc9b1f0-5a86-34a4-aa94-892a7ab8c1b6 | -8.44071 | -54.67792 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6b11f75-18b8-38d5-98d7-4adfeca2776a | -8.44042 | -54.52885 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 742d39a7-7499-30cf-a812-51d10f357dc0 | -8.43741 | -54.6774 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f4469de-9b28-33b5-b6e2-a8b63d8eb04d | -8.43357 | -54.68034 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e77d3625-a82d-3313-a592-6762212159ae | -8.43027 | -54.67982 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72862273-b2e5-3333-a5b4-6f11975f4262 | -8.42972 | -54.68328 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a3d4dce-9dbc-35ad-8575-30cbe85d8f2e | -8.42755 | -54.69714 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94890687-22eb-3087-a171-541081e60338 | -8.42727 | -54.54807 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1657bc2-d789-3161-a0bc-07a0fdccb186 | -8.42646 | -54.70406 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d64aca59-c968-3bc7-b65c-df7bb0abc78d | -8.42588 | -54.68622 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3b66e1b-b50b-3eb5-9784-717e01e185a4 | -8.42533 | -54.68969 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73c1f0bc-65d7-3149-b46f-da89830b4abd | -8.42451 | -54.54408 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a6a1d32-30aa-32b7-804e-00274a592a21 | -8.42425 | -54.69661 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 780045e8-5675-395d-b30e-4a3713c36c8a | -8.4237 | -54.70008 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e71d8846-b1c6-3d88-ad1c-c9c98192dfa3 | -8.42258 | -54.6857 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 718883ef-a33d-37a9-8218-b18360c5567e | -8.42067 | -54.54702 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21359a53-b386-3050-a6e1-56b7efd84ebc | -8.4204 | -54.69955 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 608aba06-691e-3294-90f6-5833ac4b1b47 | -8.42013 | -54.55049 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 403811b0-87fa-321b-ba72-c6447122348b | -8.40317 | -54.59394 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f4629ff-24b2-3883-9799-e50e1705971e | -8.34672 | -54.6695 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d473c98a-628d-31bf-a762-4cb9ea68f875 | -8.3336 | -54.70996 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 743c1be5-ad56-3960-8a5d-5dc4bbc4eccf | -8.32805 | -54.68074 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9026242-b0bc-3564-8102-efb3d96658cc | -8.32584 | -54.67329 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22288b33-e886-3c36-b840-edc9f028b66a | -8.32529 | -54.67676 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 442435ef-589e-3590-8994-8192e91fbe62 | -8.30002 | -54.68696 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5b205f3-4606-3f58-9fb4-bc90493ec826 | -8.29726 | -54.68297 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b304ce0d-a933-3fc4-b4f4-9c23b412c349 | -8.29672 | -54.68644 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e94881a-678b-3e93-8171-690e1e0c5c44 | -8.29619 | -54.68987 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 459ab8be-d5ca-35aa-b98e-ecbda41d3a1d | -8.29396 | -54.68245 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25f23dfd-8d8e-3635-a6c8-dddd9479a5e3 | -8.29342 | -54.68592 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7965f3c9-4a7d-3c8d-ab69-c03947af3948 | -8.29289 | -54.68934 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20dbed60-a04b-385f-93e8-4a28c5e075c6 | -8.2698 | -54.6857 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f19cb2b1-9c9e-3b98-bdea-adfe217947a5 | -8.08942 | -53.19534 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46b68422-ac5c-39d0-b3a3-fe7149b29549 | -8.08887 | -53.19893 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3052a71-6b5b-364d-87ca-54403f9a6b7a | -8.08046 | -53.1866 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 603b8919-476e-38ee-93ce-a94d2d3c9bfd | -8.08003 | -53.23422 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0012ec8-b8b0-3589-8c6e-9fdc6788d684 | -8.07948 | -53.23778 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a51e4966-5d3c-3c74-913f-b3b62cc71320 | -8.07613 | -53.23728 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1c72f5c-587b-3db2-8664-9383746aa549 | -8.07559 | -53.24083 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23bc9a8c-1836-31e2-8125-99bd3a080697 | -8.07223 | -53.24032 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a64e7a98-593f-3567-802d-b9c7740b5060 | -8.06984 | -53.18862 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f8ed016-fde6-3de1-915e-194eee4f8c39 | -8.06594 | -53.19172 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4c30989-2c07-3ea1-af86-a54a9328a1d4 | -8.06553 | -53.23928 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 03ea4c0d-0c80-3763-be8c-68854ee0bbd0 | -8.06368 | -53.18397 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eac5425c-d05c-3c56-9105-364f588b805c | -8.06314 | -53.18758 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d524cdd8-4211-3e09-bcc2-5924bcf68418 | -8.06273 | -53.23517 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc61e6ff-ddd4-34b6-8b03-d1364a954d73 | -8.06218 | -53.23874 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6f4b202-e42b-3909-b9b7-158988ff3ff8 | -8.06102 | -53.22395 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc92885c-1d62-308a-a0a5-d7bde909c03d | -8.06047 | -53.22751 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed2ed73c-8dea-305c-bcff-293dd0b52b61 | -8.06033 | -53.18345 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4481781f-ae3a-3689-9146-8b8cbf1b5d45 | -8.05993 | -53.23108 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62e3a4f4-ce05-333f-94bb-eff25b5e894f | -8.05938 | -53.23465 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c144d8f2-7fa2-3bba-97c7-3b2fbc402b17 | -8.05657 | -53.23059 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| af67f42d-0c94-3e6c-adcf-2b58ac05b881 | -8.05268 | -53.23362 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8dd9859-935e-397f-bb6d-632913e84945 | -8.79786 | -54.68194 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eb19235-dff7-39fc-ae18-9ebc50db7df7 | -8.79732 | -54.68541 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f69f8609-cd50-31e7-a17e-f1c5c428cf5a | -8.79402 | -54.68488 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d6364a3-c49a-3f9e-a383-e6ac4a2cb69c | -8.79348 | -54.68835 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a44815ac-772a-3cbb-9ce4-2c2e70527592 | -8.75352 | -54.74522 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fcc65a6-fda9-3a71-858d-d2e5ebdaed8c | -8.75022 | -54.7447 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0405b5c8-90c3-3dc3-aabb-d6979798ef21 | -8.74967 | -54.74817 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 222408ac-9219-33bf-8e1f-a57846da1992 | -8.74637 | -54.74764 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d347235b-6ac1-382d-9a11-5d74e1cffa83 | -8.71722 | -54.73947 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2880da5-4f53-353b-b31c-78e6a8cc3980 | -8.71667 | -54.74294 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b9c8894-c9ae-38db-a64f-0d6e225c72a7 | -8.71404 | -54.80282 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3eed5dd1-c814-3633-b60b-4e8f63beb7ca | -8.71337 | -54.74242 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README98.md)
