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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8d75cd0-60ed-3590-9aac-c34ea68f6432 | -2.43028 | -46.28266 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77e9863b-839c-32be-bf0c-e2ab8252a9e4 | -1.13492 | -51.68465 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44db174c-1a00-37eb-b394-6a2083f171d3 | -3.12177 | -45.90266 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0af70ac-41a6-31bf-9e84-4188792cc32e | -2.64939 | -46.2065 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4e3bc59-8d3d-3529-8b88-ca3b8ff730e4 | -2.21089 | -48.40324 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5e06f29-22f4-362b-8213-a5afd908b6be | -2.68498 | -46.69344 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7544161d-384c-31c4-9150-861f6f269a93 | -3.94407 | -46.70272 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bdc1bd1-2cf8-3044-9602-1abf35398540 | -2.20254 | -46.04462 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d395a17e-93e7-30f0-8f81-e6933e5fd738 | -0.9047 | -51.73966 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7ed39ac-4aa2-3c7b-945d-aaddc3acbda9 | -1.79795 | -48.4393 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3f46976-7cf6-3c90-9b89-8999d7f09b04 | -2.93751 | -48.32616 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd028c62-c156-344d-bdc3-03702c8a46ba | -3.5065 | -51.0232 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 721f954f-db63-3fa2-94f5-770489cc1709 | -2.65484 | -46.21478 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ecc284f3-5e30-3e78-a399-2c16daf58fa2 | -3.35215 | -46.42635 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce9bc151-db51-343e-9f53-37ba9fd55c0b | -1.9091 | -46.5717 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0abc8b24-a2b5-3066-b23a-6372689d32e0 | -4.30156 | -48.07964 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdc272b7-df6d-3d99-adaa-f1bfb4aae57d | -4.37322 | -48.56903 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd3a724e-9784-398b-80b6-ef390063118f | -2.10457 | -46.5392 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 232f9ca2-a0f4-35a7-b3d8-67e3042b90ab | -2.94087 | -48.32669 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c882789b-1a50-37d7-8c0a-2d1db1ac7984 | -4.79962 | -50.80363 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a528b214-a7ba-3545-93d3-94dbaa683010 | -3.93877 | -46.41005 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea511874-3260-37fd-b656-fb2b5373523c | -4.10266 | -46.88346 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb3efea1-e851-354d-9754-c6873d55417b | -0.95106 | -52.41574 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc7f76fd-9ea6-3f8c-b4ee-a26125f4e167 | -2.66816 | -49.12017 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ba4c1a1-61cc-34c2-b6b4-1d162de40b90 | -2.24062 | -48.69774 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dad1ee7-25c3-3d97-8c43-fb9b50f22354 | -2.17972 | -49.10763 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58083531-03ad-3396-a441-d702505c8699 | -3.84119 | -51.30652 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b95b4cb3-5432-3cde-a638-14eb10494ed1 | -2.11301 | -46.42068 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7cd3a78-b719-34c8-8e2d-ca4429b751b5 | -2.25478 | -48.38803 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26a63cba-1323-30c8-81db-0e510ead617b | -2.65217 | -46.21049 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c2295c2-62f1-3ebc-bc36-9882424df9bb | -3.84873 | -46.6385 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49f6b685-f03d-33fb-8a2c-29d161e09281 | -4.15838 | -43.91939 | 2024-11-17 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d963f08e-2c79-3dec-860f-6bf50a5d4b6d | -2.035 | -46.37676 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c9014c5-168d-3b3b-b1fa-b68c8af48294 | -2.05036 | -48.43728 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d48104a-7765-315c-9b19-d1375e5e2594 | -3.37261 | -52.71634 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be1911af-225d-31f1-bccf-017ba06f2a87 | -2.17627 | -48.39438 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b64603e-6f09-3d8b-b881-8daa224df2d1 | -4.25608 | -48.53606 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3a43f21b-fb98-302f-bb7d-ada6e72eba29 | -2.62721 | -48.56347 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 95071217-e02c-36b9-956e-6b854aff6a5d | -3.526 | -50.26102 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 37a33f01-6cd9-3517-9d13-8b5ae79dc6fa | -3.13572 | -45.90118 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73966e7c-a58e-3106-b67c-4ed3928a4a15 | -3.65663 | -42.26516 | 2024-11-17 04:29:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a116da77-acc5-3692-b383-5265dd509547 | -4.19004 | -48.56905 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beab329f-ed07-3958-8173-2c749a48b285 | -4.64198 | -45.2834 | 2024-11-17 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dfd769c-b48e-33ad-931a-ce3eabe52236 | -4.33581 | -48.61767 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7846bbcd-0d31-3130-a006-108415ac4e10 | -2.67301 | -46.18554 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0184d0fd-fc88-3262-8729-63b7c07f5b46 | -5.40764 | -46.35543 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b8fedd6-0072-3d21-834c-1ffb2d0a996b | -2.39708 | -47.93859 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00f384c7-31b7-3989-9ac3-4679013bb181 | -3.53232 | -50.2569 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4cd2cfe4-4b60-35b8-8359-4750d6592f0f | -4.55838 | -48.00343 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 6ea8d9e9-60c9-3512-a707-513110575b34 | -3.25583 | -46.54269 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cced7a22-a945-3613-93b9-86d0d45e7978 | -1.84246 | -46.2829 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2483f7ac-b602-3b2c-85c2-a5944e0a4515 | -5.58167 | -44.87194 | 2024-11-17 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e4b73b4f-f25e-37f1-95c6-049eafb30973 | -3.61227 | -50.14828 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 514264e1-83c8-3c6a-af88-0be2b464768d | -1.13895 | -51.68531 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f533df09-6f99-37c1-8317-409be9d1536e | -2.60067 | -47.55366 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0355da33-b3fe-34fe-bd29-f363798ebb8c | -5.18033 | -38.00031 | 2024-11-17 04:29:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eb8f97a9-33ad-3ebc-9b0d-a1f627b6db77 | -3.33174 | -50.49675 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a977ccd7-9a81-3298-ae54-feb9acdbfe44 | -2.97533 | -53.86205 | 2024-11-17 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc0971de-2f7c-3cf7-9e2e-83e5c4d07b6e | -4.64588 | -45.00676 | 2024-11-17 04:29:00 | NOAA-20 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e0372b2-1a66-3f76-ad40-2b36c1dc1823 | -3.69502 | -51.08205 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e81ea967-5220-39c8-8d4b-e6ed0429574f | -1.20441 | -51.76832 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7f7b48e-cec2-3a26-ad56-b2e693149dc2 | -3.17198 | -46.6001 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09e3ca80-c702-3c43-9d6f-617b032ee035 | -3.52567 | -50.23986 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94276932-cc88-3ecc-9c4f-835b26c76d89 | -1.2925 | -51.73851 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bfa6bc17-c798-3312-af02-80dec7abe03f | -3.89092 | -46.6519 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0047b835-4a20-3f55-9a05-f1826d01684e | -0.95594 | -52.41245 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| deeb1f85-a5f3-34f4-9c62-0f58e7f3364e | -4.16144 | -50.02131 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 033eb92f-e4a4-331c-983c-03e123816f99 | -2.42227 | -46.52889 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a9db919-46fd-322e-8386-cb240447b915 | -3.10569 | -45.98324 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab277f21-7f6a-30d2-ad33-9b2154f4b8c7 | -2.85909 | -46.66749 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 334d3059-e21d-3b5e-8853-1ad7ce1c9d75 | -3.80746 | -46.51122 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4e3ca03-e02e-3b47-b926-d0ece6768554 | -4.26833 | -48.54529 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4d6986b3-de1d-317d-9adc-b25785af8e59 | -4.16361 | -50.3266 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c082d6e3-08b7-3598-8707-a1e8810c93ea | -4.66939 | -46.7341 | 2024-11-17 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11c1a0bd-d9ae-38e3-a9b9-d47d92da97ea | -2.65183 | -46.83962 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da205b6b-1dc5-3727-9545-bc17ab06dd71 | -2.67802 | -46.19699 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1c48eab5-2d28-345b-9c93-d0d17442b765 | -5.58782 | -45.21061 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1a3bf8c2-ead6-37ca-9a26-77b91b9a528e | -3.89524 | -46.62419 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0469b895-4323-3fd2-b5a9-c7bb266eedae | -3.86421 | -46.43093 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fee0cdb-29b2-3743-befc-34000b51b6dc | -2.1568 | -50.70958 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 467d993b-c25f-313f-ad69-763f13a68b10 | -4.51021 | -45.70376 | 2024-11-17 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14e3bafd-562c-3e23-9dc0-e2b072140359 | -2.23847 | -46.83426 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec4f3fc9-317a-3088-90a4-2bb873bce792 | -4.37073 | -40.58992 | 2024-11-17 04:29:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3cda92af-c07e-36b0-9660-10154a19ef85 | -2.54651 | -47.12207 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5769ffe-c032-3dad-991b-d2e2ba7f31bf | -6.88111 | -44.77212 | 2024-11-17 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f21f24c-a262-3d26-9e62-daa8f2c481e0 | -0.88354 | -51.79531 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7de9b40f-577f-3113-91c9-4e7e2376ecee | -3.84819 | -46.64196 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed270812-b001-3c06-b4d5-0dced822f061 | -1.23134 | -47.36016 | 2024-11-17 04:29:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 511a96ef-5ed2-3e3b-9c09-5edfb22a502e | -3.34679 | -46.06779 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6ae04506-e25a-35b0-b622-ce79ec6f77a7 | -2.94757 | -48.32774 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78046833-2640-3921-87bb-ea88b797d163 | -3.49841 | -43.78465 | 2024-11-17 04:29:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a74dfcde-5161-33ad-aed2-b3cb7f1897a3 | -2.67674 | -46.70273 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32729281-a63f-39ce-a38e-2315db889a50 | -1.20902 | -51.76542 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29886006-5fdc-341a-99e5-287c5d591837 | -3.70983 | -51.84119 | 2024-11-17 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9e118c6-e366-3148-8add-a7087a491e0a | -4.10158 | -46.89035 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46528d86-43fc-33aa-a761-8e52cd4939fa | -2.42173 | -46.53233 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2284bbc-e5ec-3393-8396-3356c8894862 | -4.37892 | -48.08508 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c08fedb1-c91b-3313-ad97-c7b30acf989f | -5.08506 | -42.56445 | 2024-11-17 04:29:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8f7b067f-bd87-3005-8b48-2cae5ea663ce | -2.6163 | -54.15757 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1595cf67-3bf8-3634-88a3-0ecb2931879f | -4.26555 | -48.54121 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README51.md)
