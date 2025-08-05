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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6eadb70a-a982-3cf9-900b-27cd2aae80cd | -7.0946 | -44.3589 | 2025-08-05 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 7fc75cf5-09ac-336b-99de-ef3a04a85c47 | -5.7887 | -43.6134 | 2025-08-05 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| fb641c18-215a-38d4-8dd5-442f25b7210a | -8.0117 | -43.2455 | 2025-08-05 13:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| bca0df5a-ae8f-3068-8754-07d22afc062f | -8.012 | -43.2219 | 2025-08-05 13:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 246.8 |
| a6b25f81-b98f-322b-b051-e6c53d5c45b5 | -7.838 | -45.1127 | 2025-08-05 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 9c42eaae-2131-37c1-93f5-e782d18f17df | -7.7616 | -45.2111 | 2025-08-05 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bb574ad6-42b5-3672-8a86-30d437ae1565 | -7.0757 | -44.3606 | 2025-08-05 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 164.2 |
| d76a26b4-93d7-38dc-a757-904d14630109 | -6.2173 | -45.8621 | 2025-08-05 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 66eea5ff-94b4-3ee5-ad4a-b57d29641158 | -6.2789 | -45.2716 | 2025-08-05 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 7ca06dec-31e2-3737-b7b3-ae14544eb1a6 | -7.994 | -43.1534 | 2025-08-05 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| b4f8b74c-db79-3fca-ac11-f3b4585c02d2 | -8.0117 | -43.2455 | 2025-08-05 14:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| c4aa8e53-967b-3059-981f-02ac9d5d212e | -7.9928 | -43.2475 | 2025-08-05 14:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 7f9d4f82-8182-3c03-8b6d-f8eefea59483 | -7.7613 | -45.2338 | 2025-08-05 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 206.2 |
| 387ceee4-9884-35a8-8cd2-6c4600774da0 | -7.0943 | -44.3819 | 2025-08-05 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 9e9b2f7b-cefd-3b38-a253-c8f1d568d55b | -8.5321 | -46.8442 | 2025-08-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f4c6f3b9-0f71-3b19-a141-348b1be3893e | -8.0123 | -43.1984 | 2025-08-05 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 3c99f7a1-ca7c-305e-8876-368573f49774 | -13.0723 | -56.9131 | 2025-08-05 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1e91b1fc-6495-3c92-92ae-8e0174b8d6fd | -7.7616 | -45.2111 | 2025-08-05 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 75a7d72f-a539-306b-bda6-782f2735160e | -7.9934 | -43.2005 | 2025-08-05 14:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| fdbede63-ff45-37b1-a041-0cc8a31f1b0a | -7.0946 | -44.3589 | 2025-08-05 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 68ef6f8b-e1e8-3583-886a-47b1092f7ba1 | -13.0538 | -56.8746 | 2025-08-05 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7d430941-1780-343d-ac8f-adf415f4d55b | -6.5009 | -45.5479 | 2025-08-05 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 00823442-60b8-3c93-95c5-2c21bf4cbdb7 | -9.1677 | -40.6026 | 2025-08-05 14:00:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 90.3 |
| af5dedb1-50fe-33b3-8c6b-8f2f01a9276d | -7.0755 | -44.3836 | 2025-08-05 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 91df1393-3580-3c8d-bc1f-31ffb8d56640 | -6.2932 | -45.7441 | 2025-08-05 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| cee3f02c-950a-3fff-8d12-70f137a346ca | -5.7887 | -43.6134 | 2025-08-05 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| b9a0d134-a2b8-310b-99b9-b132a6a9e7d4 | -6.2743 | -45.768 | 2025-08-05 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b75905a3-eb0c-3df3-b4e9-ac9a4dbe6c40 | -13.0726 | -56.893 | 2025-08-05 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f3777dd1-9d01-3c1a-9b69-f98127b0d20c | -7.7425 | -45.2356 | 2025-08-05 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 3fa92e44-9fe2-35f1-8ede-2a5d8bf7d9d1 | -7.8383 | -45.0899 | 2025-08-05 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 258d9786-3c15-3796-9d0e-a06771c4c602 | -7.9931 | -43.224 | 2025-08-05 14:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 200.1 |
| 34799c27-5ba4-3d76-a703-b9671de7a227 | -8.0126 | -43.1749 | 2025-08-05 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| f88db9f9-3a0e-388f-95c8-19d0af20fc6a | -13.0914 | -56.9114 | 2025-08-05 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| f31be97f-a85f-3414-96a7-5d2605ef8480 | -7.838 | -45.1127 | 2025-08-05 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 143.3 |
| f6f47b59-5928-3579-a34b-743b7dc1d92a | -7.0757 | -44.3606 | 2025-08-05 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 03c8148d-a6ae-3139-a07f-ce65cfa14e5b | -10.9298 | -48.3717 | 2025-08-05 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ed1be24b-9a43-3735-a98b-d778efd1d154 | -8.3661 | -46.571 | 2025-08-05 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d085fe74-d78b-3783-8049-589a9c21c030 | -8.9478 | -46.7354 | 2025-08-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 74041467-773f-3e04-b0ba-57f0396aa7e0 | -6.433 | -44.8279 | 2025-08-05 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| e755e451-8d7d-3e33-aefa-90fcb68693c0 | -8.012 | -43.2219 | 2025-08-05 14:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 183.1 |
| c7dbf3ba-1b4f-3d8c-ae5a-8bd718c15461 | -7.7613 | -45.2338 | 2025-08-05 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 0d956ca1-7bb6-3924-8883-fa7d0074b1cd | -5.7887 | -43.6134 | 2025-08-05 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 7f624e6d-5d8c-3d33-87f8-017a6e1a8847 | -7.9931 | -43.224 | 2025-08-05 14:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 199.4 |
| fd3ba8c8-90a9-32de-b8b8-6a815f0e7367 | -13.0538 | -56.8746 | 2025-08-05 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 86b1c017-a2d8-33ee-9fa8-689acc653c2f | -2.9371 | -42.2827 | 2025-08-05 14:10:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 6ad11476-1195-376c-9d40-06fb1dd2c0a0 | -7.0757 | -44.3606 | 2025-08-05 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 11da7402-b22b-31b6-9845-ca065a1e49b4 | -8.0117 | -43.2455 | 2025-08-05 14:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 679fd498-f59f-363c-8838-d088acc96c66 | -6.3317 | -45.6287 | 2025-08-05 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b65c1cfc-14fa-32a4-b098-6974635d3a00 | -7.8383 | -45.0899 | 2025-08-05 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 327.6 |
| 7005a7b8-bfba-3a70-a4b2-719cd05e7b0e | -6.2789 | -45.2716 | 2025-08-05 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 53704d75-8d3e-309b-9503-57eeb6bde0fd | -10.7842 | -45.5037 | 2025-08-05 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 39cc4c11-6320-3bb0-8c3b-5329c9164a0b | -13.0726 | -56.893 | 2025-08-05 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 09223df9-d5c0-3f87-ba74-84e33ec9c2b1 | -8.7442 | -46.4437 | 2025-08-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 49c3d204-9d43-34f4-82ff-541258769c4b | -8.0123 | -43.1984 | 2025-08-05 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| a3a119df-e5a4-3e2e-b939-a71ba57bd3b4 | -7.7425 | -45.2356 | 2025-08-05 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 9b48a812-4e44-3b66-9368-5d26b1d3e53b | -7.0943 | -44.3819 | 2025-08-05 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7372a304-dff4-399b-b2f1-8d1d7b74b712 | -8.5321 | -46.8442 | 2025-08-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 992ea2fa-db77-301c-a675-467f4774e57a | -8.9478 | -46.7354 | 2025-08-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 641d9532-c3c1-386b-b01a-424d7f65de87 | -7.9943 | -43.1298 | 2025-08-05 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 188940c1-5945-3a8c-a65c-02e79c420816 | -7.0946 | -44.3589 | 2025-08-05 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 75020367-a717-3cd2-8db3-48593fc6f1a8 | -13.0723 | -56.9131 | 2025-08-05 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 1be102b0-30ad-315d-bb3a-b5575e2d0bfc | -6.2932 | -45.7441 | 2025-08-05 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 01367dd9-c02f-3b4f-b157-f3d6198463c9 | -7.838 | -45.1127 | 2025-08-05 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 287.8 |
| 7ceea13b-b272-33a8-a29a-486f21cc48a3 | -8.0126 | -43.1749 | 2025-08-05 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 4a737b2a-aa40-3faf-bbdc-fbd633def189 | -7.994 | -43.1534 | 2025-08-05 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 336f94d6-69f1-341c-8fe6-8bf2901db0f0 | -6.2743 | -45.768 | 2025-08-05 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b2b0690d-c72a-3181-95b8-2c6b43d95015 | -13.0914 | -56.9114 | 2025-08-05 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 836699b4-157b-35ef-b922-0e08f9d26ffc | -7.9934 | -43.2005 | 2025-08-05 14:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| ada6834c-841a-3631-a3a1-87b7ec4d1bfe | -7.7616 | -45.2111 | 2025-08-05 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 06df90c3-c2e1-3df9-8200-90e76f2cf90f | -8.3661 | -46.571 | 2025-08-05 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 81fbf42b-0bef-39db-94e9-77a2e781223a | -5.9249 | -45.1171 | 2025-08-05 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 07da3270-106e-35b6-8828-94c7795bee90 | -8.012 | -43.2219 | 2025-08-05 14:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 175.9 |
| 90888ce7-dce4-3aca-8372-69e7d1812bbc | -7.7613 | -45.2338 | 2025-08-05 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 13fab7d0-5d1d-3b91-8e22-092bb6be4bd2 | -7.838 | -45.1127 | 2025-08-05 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 142.0 |
| bacab95d-3a97-3993-a9d3-39882fb7ba1f | -6.9736 | -43.3965 | 2025-08-05 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 46de3b3d-3486-3acc-8d0c-c04f5b45bead | -10.5776 | -50.507 | 2025-08-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 7e1efd4b-1610-32cc-bcbd-ffbd96cfac63 | -8.0123 | -43.1984 | 2025-08-05 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 43f631ac-dd8f-3d8d-a143-963084d9e464 | -13.0914 | -56.9114 | 2025-08-05 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| da23acb7-6cc9-3913-822a-6de0fe3859d0 | -13.0726 | -56.893 | 2025-08-05 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 95e2b7ce-0fc7-38d2-b13f-8d929ed74fc1 | -7.0757 | -44.3606 | 2025-08-05 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 6688293f-c88a-3cb8-aad4-f9dbbe1d92eb | -8.0117 | -43.2455 | 2025-08-05 14:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| ea63dc30-1d5d-3693-bf98-875e59f5c1c4 | -7.9931 | -43.224 | 2025-08-05 14:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 251.1 |
| 6c911b85-858b-3d75-a472-0fa761af9b35 | -7.0943 | -44.3819 | 2025-08-05 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 456b0b7b-a3b8-3560-932f-be6e282866c5 | -13.0538 | -56.8746 | 2025-08-05 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 48801ef5-d713-3201-bee5-093a401b3761 | -5.7887 | -43.6134 | 2025-08-05 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| ee942c11-84bc-3aa3-bed7-8cacfdecda1f | -7.9928 | -43.2475 | 2025-08-05 14:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| e5bff1ff-41f0-3378-afcb-edd1314f08ec | -7.9943 | -43.1298 | 2025-08-05 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| d0a1a614-d147-32d4-b8ce-4869c6b07243 | -6.2789 | -45.2716 | 2025-08-05 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7ca83409-8b98-3611-9f26-a81a45f7c0b8 | -6.2932 | -45.7441 | 2025-08-05 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 74f1e014-7d86-3025-afea-17e8448bc25e | -7.7425 | -45.2356 | 2025-08-05 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 138.9 |
| c91320e2-5828-3a6a-a6c6-c26749ec555e | -8.3475 | -46.5505 | 2025-08-05 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 434be64e-4bcf-3912-a964-5c30ceb9f5b4 | -7.0946 | -44.3589 | 2025-08-05 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| ebcc9181-f756-36eb-a7b6-b4853168d6f2 | -6.236 | -45.8607 | 2025-08-05 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| ee27e2ab-64b6-358c-8b96-e78cdb2e634b | -8.3661 | -46.571 | 2025-08-05 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| eba7ea04-6e9e-3d86-965d-98bf95161daf | -7.8383 | -45.0899 | 2025-08-05 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 85ecb2d8-6907-341e-9495-ac8fe5d0e937 | -8.012 | -43.2219 | 2025-08-05 14:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 228.6 |
| 5c99094a-1f1f-3bbb-9244-83e475cdbf26 | -7.994 | -43.1534 | 2025-08-05 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| deab2775-3cd0-35d3-9267-d36ff6d916e7 | -8.0126 | -43.1749 | 2025-08-05 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 775e9590-9a80-3cca-beae-a98d51363f2d | -6.2173 | -45.8621 | 2025-08-05 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f1a5b003-1407-3b59-893a-3b60173904bc | -11.7474 | -45.0014 | 2025-08-05 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |


[Clique aqui para ver as próximas entradas](README34.md)
