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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96130628-aadb-36d0-a4ad-e64a74043300 | -5.703 | -44.838 | 2025-10-06 03:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 760c9372-7db7-309f-b7f8-d802c83718e7 | -8.6327 | -46.3208 | 2025-10-06 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 272c0b09-d4d7-3fa4-bd77-4157978f8c3e | -11.0037 | -51.1635 | 2025-10-06 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 04f0ba78-3b6b-3e08-be94-8d8932b6d23d | -14.6131 | -52.5163 | 2025-10-06 03:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 578c5840-ca29-31a8-9d47-ee482ae2dca2 | -17.981 | -57.5468 | 2025-10-06 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 477eef3d-fa9d-3e9d-8ab9-9108aa2371f2 | -17.8621 | -57.5818 | 2025-10-06 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 67f3da63-3414-30c4-bd03-e24cbca5e1aa | -5.7028 | -44.8607 | 2025-10-06 03:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a018632b-ec79-30e3-81c6-89c09d430d72 | -18.1366 | -53.3946 | 2025-10-06 03:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.2 |
| fa7d4a4c-2e7f-30fe-aa2a-01132981541b | -10.3162 | -50.278 | 2025-10-06 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| dce611ff-e7d5-3121-a24e-9921ec2a641b | -14.6131 | -52.5163 | 2025-10-06 03:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f89db11c-08ec-3353-b2a0-928b55383be7 | -18.1366 | -53.3946 | 2025-10-06 03:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 1248b837-75a3-37d2-ad04-9fd0a11142c5 | -10.4099 | -50.3324 | 2025-10-06 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 809886d4-ccff-39aa-95b6-03c5f1af921f | -9.3162 | -46.0005 | 2025-10-06 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 53656411-ef23-35dd-b057-af7b239c5e7a | -17.8617 | -57.6024 | 2025-10-06 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 9097de78-61d2-39f8-afd3-e53e80b22014 | -14.6135 | -52.495 | 2025-10-06 03:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c7ece315-ac9e-392b-8656-9a1c491d9cac | -17.981 | -57.5468 | 2025-10-06 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 7bf8becb-8789-39b1-a2ab-b657a88abb61 | -8.6144 | -46.2778 | 2025-10-06 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 5c57e706-a1b7-3471-aea2-7015dd239592 | -8.633 | -46.2984 | 2025-10-06 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 16cecb5a-1713-33e7-9df4-8eefe5f39f17 | -11.0037 | -51.1635 | 2025-10-06 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| af52ba07-b298-3957-8091-ed7eaf455f59 | -8.6327 | -46.3208 | 2025-10-06 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| d6cd3f82-0a75-37d3-b8f8-dca7b6777eb8 | -12.4472 | -45.5415 | 2025-10-06 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 9c9ef67b-a73d-3211-8fdd-4709f155f5f2 | -5.7028 | -44.8607 | 2025-10-06 03:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1444ebe2-a467-375e-8849-b77e100c49a5 | -17.8621 | -57.5818 | 2025-10-06 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| f0687c01-6d93-3114-aca4-34c2622524ce | -8.6141 | -46.3003 | 2025-10-06 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 13143aa1-3596-3caa-8b7e-fb07a18d035e | -5.703 | -44.838 | 2025-10-06 03:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 8961eb90-71a9-33a7-8d46-18c037691e0e | -18.1366 | -53.3946 | 2025-10-06 03:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 4199c0a1-0158-34cb-a302-e78f0bf3f934 | -17.8621 | -57.5818 | 2025-10-06 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 5d8b2b49-7104-340e-ba55-f8316024cf8b | -11.0037 | -51.1635 | 2025-10-06 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d8c1813e-3a31-31c5-a746-3df34c940898 | -17.981 | -57.5468 | 2025-10-06 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| a22ef7d6-f6cf-38a8-9ab7-8d067c93ee50 | -18.1167 | -53.3977 | 2025-10-06 03:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e336ed92-684b-3784-8ef9-db5dffd2eee3 | -10.4285 | -50.3518 | 2025-10-06 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 2ccf0e6f-cf22-3542-984b-7cc0a5cf225a | -8.6144 | -46.2778 | 2025-10-06 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d9939762-bc50-36c3-9115-b148bcb53255 | -8.633 | -46.2984 | 2025-10-06 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1f7de746-8f52-32f8-bfcc-6b7c08fe0b19 | -14.6135 | -52.495 | 2025-10-06 03:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ba4b6d88-84be-36d8-a3d7-37fc273acb62 | -18.0008 | -57.5444 | 2025-10-06 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 31ca5ba3-cddb-3e1f-9b5a-27329dc9cf1d | -10.3162 | -50.278 | 2025-10-06 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 3707c376-72da-3078-9fb5-1b210fd51571 | -9.3162 | -46.0005 | 2025-10-06 03:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 16f358a6-c609-31f1-9e92-3e033756fe7e | -17.8818 | -57.5794 | 2025-10-06 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| e8199b1e-5111-3683-924d-345ceea56bbf | -8.6139 | -46.3227 | 2025-10-06 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| d30aabb5-f0be-3b8a-b622-42766cecb3a9 | -10.4099 | -50.3324 | 2025-10-06 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 4f9988d1-bd3c-3845-969b-90883b1cb70e | -13.0779 | -47.8234 | 2025-10-06 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 15735638-fc1e-39d1-bc4d-13c8a01e6273 | -14.6131 | -52.5163 | 2025-10-06 03:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 880db302-9c96-3def-be20-dad9a1f9f75d | -8.6327 | -46.3208 | 2025-10-06 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 47aaf03b-bb25-3097-bff9-9393fb12c518 | -10.3165 | -50.2566 | 2025-10-06 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 02348cb0-0827-30a4-b11d-eb74c7c401a6 | -8.6141 | -46.3003 | 2025-10-06 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ee39ed98-2117-39d0-af28-05e2fcb93425 | -9.3165 | -45.9779 | 2025-10-06 03:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 69aa5cb1-2fa1-3981-a1e0-12c754994874 | -8.6327 | -46.3208 | 2025-10-06 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 567ed29e-80fa-3418-b774-27b79354aee6 | -18.0008 | -57.5444 | 2025-10-06 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.2 |
| a2ab8ba8-9ba1-3272-8e45-3f7460a02a8b | -17.8818 | -57.5794 | 2025-10-06 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 35988e01-0c18-3ee6-8f83-d40584be5be6 | -18.1366 | -53.3946 | 2025-10-06 03:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 269c2186-2816-3cb5-a103-ea6568eb995f | -11.0037 | -51.1635 | 2025-10-06 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| de73de9d-94c6-316d-add0-ae1e128b3477 | -10.4285 | -50.3518 | 2025-10-06 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 973fd805-4afb-3d61-856f-967ae6e33062 | -18.1167 | -53.3977 | 2025-10-06 03:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 88114d98-1bb8-37a4-8582-c5f18085cf04 | -17.8815 | -57.6 | 2025-10-06 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 03729f7b-58b9-3eee-bc7a-25481d0eff48 | -10.3724 | -50.3149 | 2025-10-06 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0098a29a-6710-3a1d-8441-b2928d5559dd | -17.981 | -57.5468 | 2025-10-06 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 32c012bb-780c-3458-9d61-4f876cff684e | -17.8617 | -57.6024 | 2025-10-06 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 41e2e095-460c-3fc7-ad77-a8e9a7f411a2 | -17.8621 | -57.5818 | 2025-10-06 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 2711e560-82da-38f8-b15a-8149fd3adcbe | -9.3162 | -46.0005 | 2025-10-06 03:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c494b951-07d5-345d-a79f-79dcc02f85e9 | -6.05483 | -44.09033 | 2025-10-06 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94426a45-a76f-375b-bcf8-0eb5425fd0d6 | -6.42658 | -44.62456 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13120814-d4c2-3a6c-948d-d5d8b983742a | -5.41186 | -41.07135 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a294531f-62e6-36a0-bb3b-fd2d30c4a4cf | -5.33191 | -43.37779 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d64ab47-eb7f-3459-962f-53af10487ccb | -6.07099 | -43.48861 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 059888cc-5e59-3922-b0dd-0cfab912b717 | -4.77181 | -46.61239 | 2025-10-06 03:34:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 781fbbb7-c1e9-3654-a6da-4f4d14f6c044 | -6.23924 | -44.26128 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d9c7d4d-34a0-3391-b857-12d9f39576b3 | -7.02633 | -42.30175 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ca8444ed-345e-36e3-847a-fe79b7115def | -7.24648 | -44.13783 | 2025-10-06 03:34:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca9fefa9-248c-30d7-8801-bec9af16a321 | -6.43361 | -44.62011 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32e3a18c-470e-391d-a120-cc0f528708db | -7.03096 | -42.30571 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aca3f498-c4d8-331b-90fa-a374dec254ad | -5.64043 | -37.79902 | 2025-10-06 03:34:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 660f8734-c73a-36c2-b3c7-5facdd1bb845 | -7.52301 | -41.28045 | 2025-10-06 03:34:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7e948dd6-e4aa-30b1-b450-d6d5a3043bce | -4.94471 | -44.58961 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 126b3b34-80b0-360b-8051-b255651d6597 | -6.36404 | -44.65948 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12f274e2-f51d-310a-adfc-a4eb8bd4fe36 | -6.18628 | -38.89331 | 2025-10-06 03:34:00 | NOAA-20 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e6f93548-406d-3275-a708-26db1454441a | -7.68417 | -42.58477 | 2025-10-06 03:34:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b2bad920-2d1b-3610-b902-0266c25b65c2 | -6.99752 | -47.47464 | 2025-10-06 03:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 49876edc-b435-3292-a97a-55c532851bed | -5.50955 | -43.45741 | 2025-10-06 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ff7ea43-91ef-3003-b6c4-7cc35984ff81 | -7.3577 | -45.22773 | 2025-10-06 03:34:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5003dbad-eed7-35f0-b1ce-d4042064a929 | -6.69551 | -42.16042 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9c15467d-b514-37eb-877f-4c3af98be3c7 | -5.58891 | -37.30052 | 2025-10-06 03:34:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e5a900e3-b561-3afb-b29b-9b8eb662b801 | -7.43032 | -41.13391 | 2025-10-06 03:34:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d5bd2137-875c-35c9-9ae9-d6d539c00332 | -7.00782 | -42.80477 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 949261dd-275a-3bac-9132-6cd2ccdd610f | -7.47176 | -42.62447 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d7c762ed-24d0-33b0-9702-b64adc2e5258 | -6.69178 | -41.39033 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b903d25c-832e-32c5-8534-7b488ef41153 | -6.04212 | -42.55869 | 2025-10-06 03:34:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1dfcec6-da53-3ba6-b7f8-9a82704122f3 | -7.42085 | -41.13233 | 2025-10-06 03:34:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| be586407-89a9-3a79-91ea-5ba801a54b36 | -6.03948 | -42.55484 | 2025-10-06 03:34:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 81a07359-c211-33b2-abb1-efb35bc0f21b | -7.2095 | -45.89593 | 2025-10-06 03:34:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9cf2d89-a566-3743-8f05-1b793f5d0ec5 | -6.84438 | -45.48252 | 2025-10-06 03:34:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25e5ed54-5ee8-397f-8ed0-4d7e43d55a99 | -6.63905 | -41.98528 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 46298026-0168-379e-8607-d71c7d1ccc4a | -6.11149 | -43.8706 | 2025-10-06 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a05ec35-bc23-3e8a-9429-b653c8b3b326 | -6.06786 | -43.48668 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 240e6559-d28f-351e-a477-9082ce2fa843 | -6.2496 | -44.25708 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fda322d9-8a4e-3c91-a179-317e05a06692 | -6.63345 | -41.98737 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b0e4fb0-f2f5-3cfc-9ff7-f339956a20a2 | -7.71268 | -42.39662 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b560aebf-a6d6-3ee0-bc59-b54ea2cbd7eb | -7.252 | -44.13943 | 2025-10-06 03:34:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 86e64d9c-85ac-3b2d-9659-11fc15a488ab | -6.99709 | -42.83406 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 40ba5190-ee5c-3006-aa19-5d1c0d4d78b9 | -5.18154 | -35.83598 | 2025-10-06 03:34:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b77fc602-c23a-32b7-aaa2-6c2616f5b9df | -6.78824 | -38.76171 | 2025-10-06 03:34:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
