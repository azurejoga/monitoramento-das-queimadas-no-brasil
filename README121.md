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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 359e62f6-021b-3793-a351-1de4d3cae776 | -3.9625 | -48.9883 | 2024-11-09 13:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| dd5e8f00-293a-3305-b456-41a4b47af4f9 | -1.5347 | -52.1694 | 2024-11-09 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| c1246665-e2d2-3f34-a47d-0aeb414cf54a | -3.0504 | -50.3542 | 2024-11-09 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e3ed9f45-2b14-35aa-a413-afbbd679f22f | -2.3604 | -46.8776 | 2024-11-09 13:40:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 511fc893-2e02-35ac-97c5-116758af6799 | -2.3605 | -46.8557 | 2024-11-09 13:40:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 504e35c9-665d-37d6-8252-8e552e4add0d | -17.6083 | -57.4482 | 2024-11-09 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 2ff5bcc8-1c3f-3162-84d8-c76304928f6a | -3.2538 | -50.2639 | 2024-11-09 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 94a6fa37-6467-361d-a2c7-c7cebda81a94 | -1.5164 | -52.1491 | 2024-11-09 13:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 0e0b8982-82dd-3f23-8a78-a8128038a9a9 | -6.9974 | -41.3016 | 2024-11-09 13:50:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 8822f795-575a-31ae-96f5-e72b5d539fcb | -2.2479 | -53.7627 | 2024-11-09 13:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 80e34bd0-7df5-393c-92a8-f9db916951de | -2.646 | -49.8819 | 2024-11-09 13:50:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| f93b3555-0301-3848-9316-8d2eed351db8 | -4.1246 | -43.5833 | 2024-11-09 13:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 90d1a4fe-4bc9-30e7-8e8e-7878607d1758 | -0.3034 | -51.7071 | 2024-11-09 13:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 323466c8-15ea-3098-80f8-93401a45b9e5 | -3.6111 | -48.9167 | 2024-11-09 13:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a9e5e146-8d30-3dc9-8d89-b37034eeee86 | -3.944 | -48.989 | 2024-11-09 13:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 9de28e6f-786f-3853-b85f-84b40b7aa158 | -5.7287 | -41.9942 | 2024-11-09 13:50:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 3a77a9aa-8486-313b-b7df-bcb3fbbee261 | -0.2115 | -51.6455 | 2024-11-09 13:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 77.4 |
| e3631001-23d1-3361-ab25-c76d2ef5d467 | -3.5462 | -43.5663 | 2024-11-09 13:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 18da0200-3997-3669-ad86-8b6fcd50fe76 | -6.1363 | -42.578 | 2024-11-09 13:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 858373cf-2b6e-3f48-839a-074b788788ef | -2.3604 | -46.8776 | 2024-11-09 13:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 6592d0c0-3830-31e1-b774-6c9361b67efa | -2.2803 | -48.744 | 2024-11-09 13:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 49fb24d3-ecf9-370f-a1b8-933ec2a1ee3c | -3.9002 | -50.3042 | 2024-11-09 13:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 369d016e-7108-30c1-9732-bbf814d2f933 | -3.125 | -50.1629 | 2024-11-09 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ed994706-f704-3a9d-8358-f19c681425e4 | -5.4413 | -44.8335 | 2024-11-09 13:50:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b16db0ae-316d-33ce-acc8-4f5c099105c8 | -2.3732 | -48.5918 | 2024-11-09 13:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 0cf4679d-1d23-374c-9a61-d85cd7556099 | -0.6177 | -49.5351 | 2024-11-09 13:50:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c0d3f960-8d85-3c20-a83f-07533c61a736 | -2.3605 | -46.8557 | 2024-11-09 13:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 92566c62-7a50-35fc-8f5f-57a7c472e814 | -5.4359 | -43.2673 | 2024-11-09 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 4d558f3d-a48d-3b03-99a3-2de6b76ad934 | -3.2154 | -50.6213 | 2024-11-09 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 3a6efadc-c6e1-31da-a880-e6cb064b6396 | -5.4734 | -43.2646 | 2024-11-09 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 21a5eb8d-b916-303c-b4bc-905c21f7f1bc | -3.525 | -44.0286 | 2024-11-09 13:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 424b7df6-3f8d-38d3-9d50-46f453e72516 | -2.2322 | -46.4182 | 2024-11-09 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| bcd6caa1-4f9e-373f-ad3c-2045d65b8a78 | -2.4551 | -46.3014 | 2024-11-09 13:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c06e4d03-a576-3ce5-8dc9-1c301e334ba5 | -2.3555 | -54.7627 | 2024-11-09 13:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8ab65a1e-312b-323f-86c5-583b12f7f6cf | -2.2318 | -46.5508 | 2024-11-09 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3647c1f9-2ae7-32ad-b423-9160c5341800 | -2.4365 | -46.3241 | 2024-11-09 13:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 341b3572-fffe-36db-8469-4059edf133d1 | -0.2299 | -51.6455 | 2024-11-09 13:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 40c99c59-53a9-365e-817d-ceb73b21a644 | -7.1778 | -42.0055 | 2024-11-09 13:50:00 | GOES-16 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| a69f2c82-fb3b-3c3f-9e59-8972f4413ed6 | -3.2353 | -50.2645 | 2024-11-09 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 321.9 |
| 0f714d3e-fa81-3a9d-9528-35dc22816bab | -1.498 | -52.1699 | 2024-11-09 13:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 230fcc91-0e95-3944-90fc-a1896958d311 | -2.2804 | -48.7226 | 2024-11-09 13:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 50f333fe-25b2-36f0-8306-699e2b115348 | -5.7146 | -43.5261 | 2024-11-09 13:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c30e7dde-17f6-384a-81f0-2e20d86615d3 | -3.125 | -50.1419 | 2024-11-09 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| f7a73b28-381b-3290-9b85-84e4590a7065 | -5.4544 | -43.2893 | 2024-11-09 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b8e71777-ec0d-332a-adfd-7900ee89d4ad | -2.379 | -46.8552 | 2024-11-09 13:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 01ad19ab-3e42-3daf-a038-72b215d959f9 | -2.5781 | -48.1777 | 2024-11-09 13:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f84c9fb6-d35d-3fd2-a64c-66f20f415497 | -2.2479 | -53.7829 | 2024-11-09 13:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 197.7 |
| b2c996eb-500b-3c2b-b0d2-8af5dcfc39d6 | -1.5163 | -52.2106 | 2024-11-09 13:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 90199436-ddf9-39a9-a7f8-455a26f0a980 | -4.2032 | -45.8762 | 2024-11-09 13:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1d09ba63-dcec-3ba2-a707-1313f260b3e4 | -4.5713 | -43.789 | 2024-11-09 13:50:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 710bb5c7-068c-340a-b210-a4f9c03fc568 | -2.3733 | -48.5703 | 2024-11-09 13:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| f0c9d953-10af-3521-810e-0a1f6d01f5d6 | -6.1366 | -42.5544 | 2024-11-09 13:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| b7dd98ff-e1c5-3fb4-9da2-2b4f687ce6fe | -3.9624 | -49.0096 | 2024-11-09 13:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d7cede88-a528-3e48-bf8a-f141744f4470 | -5.4546 | -43.2659 | 2024-11-09 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 181.4 |
| f14b2002-ab8b-3275-8988-a8c51d8cfbf9 | -1.5347 | -52.1694 | 2024-11-09 13:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| f232949e-bed9-3db8-88cc-e4904c1f593f | -2.6758 | -46.7806 | 2024-11-09 13:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 232fabc5-5962-3d0f-a836-933a169b8655 | -17.6079 | -57.4688 | 2024-11-09 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 2df80ae7-f6ab-3e14-86ff-26b10847d037 | -7.0702 | -41.5359 | 2024-11-09 13:50:00 | GOES-16 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| a0e866a1-c01e-30d3-bf61-9eb7621f8f84 | -4.807 | -44.7606 | 2024-11-09 13:50:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 241.7 |
| ec031573-1072-39f4-b07a-bc91de99f35d | -2.2988 | -48.7436 | 2024-11-09 13:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| f737a875-bae0-3473-b207-5bb8ded00a83 | -2.6459 | -49.903 | 2024-11-09 13:50:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 05d23e0a-c9a0-3190-9acb-c951879561d7 | -3.0504 | -50.3542 | 2024-11-09 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 6e002f41-3ed6-3d25-b745-fe1c639e787f | -2.0835 | -46.5324 | 2024-11-09 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 2eb337d8-a79d-3b9e-9b35-577fd47eeaac | -4.2033 | -45.8538 | 2024-11-09 13:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 250.6 |
| 0a8eb248-2f6f-33b8-8d33-15449c4dba22 | -3.8194 | -44.6778 | 2024-11-09 13:50:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 145b0908-fc39-3ec3-a4ba-58f4bb618af7 | -3.0319 | -50.3547 | 2024-11-09 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 2179141a-9b5b-3395-9f48-00610f19cb49 | -2.2295 | -53.7631 | 2024-11-09 13:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| dbc21db6-5a8b-34a3-a724-c58d381bdc7e | -2.3918 | -48.5699 | 2024-11-09 13:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 720e514c-5cef-3def-b8d2-d5b70702fe40 | -3.9483 | -48.1724 | 2024-11-09 13:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4e3a74ce-26d3-3ce6-a47d-470ea12b9c11 | -2.4104 | -48.5265 | 2024-11-09 13:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 9bb08299-9750-3707-af75-86391ac98eed | -6.1836 | -45.4597 | 2024-11-09 13:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 7002d064-600c-39b3-a082-6d7d19f153c2 | -2.455 | -46.3235 | 2024-11-09 13:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 194.5 |
| 37d0cc59-a08d-3add-9f93-83b513d8b8bd | -3.9625 | -48.9883 | 2024-11-09 13:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 7fe30e7a-a9fe-3be5-bad3-95e607aa544c | -0.3034 | -51.7277 | 2024-11-09 13:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 77997064-c683-330d-a016-3302bcd546a5 | -5.4359 | -43.2673 | 2024-11-09 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 061faea2-3646-336e-af50-99c58c704ee6 | -2.3605 | -46.8557 | 2024-11-09 14:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 43797e91-6387-3f8e-aee6-e1ea106867f2 | -6.1836 | -45.4597 | 2024-11-09 14:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 2a09add2-8f22-38b6-a167-01fdd3ce79dd | -5.455 | -43.2192 | 2024-11-09 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 0ffdd257-4b66-3b03-8071-7e049bb1886f | -2.6459 | -49.903 | 2024-11-09 14:00:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| dd470b81-6be7-3af5-87eb-c91590538595 | -2.379 | -46.8552 | 2024-11-09 14:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 32e4457c-12d1-3bbe-851f-0e61095d44df | -3.6111 | -48.9167 | 2024-11-09 14:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| f3e46094-1bf3-3289-957b-f85f9da4924d | -1.5163 | -52.2106 | 2024-11-09 14:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f3384984-51de-3413-81be-720d593ade7f | -3.032 | -50.3338 | 2024-11-09 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 97e662ff-e278-3454-bafd-b48e3c98837a | -2.2315 | -46.6169 | 2024-11-09 14:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 50642d27-72cf-3687-a4de-b21557eb0e69 | 3.7462 | -51.6224 | 2024-11-09 14:00:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 9c084d5e-3d60-344d-991a-dfa0e5809934 | -3.9624 | -49.0096 | 2024-11-09 14:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 6862da88-d7c4-3d25-8a3b-e31b50706458 | -7.0702 | -41.5359 | 2024-11-09 14:00:00 | GOES-16 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| a2f186b1-6ac0-3026-8eee-e0715aa452e6 | -2.578 | -48.1992 | 2024-11-09 14:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 0aa57ba9-b631-334f-8f16-ad01dab58329 | -6.1363 | -42.578 | 2024-11-09 14:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 1b821d96-75bb-3d8e-994e-b65b546c8900 | -7.089 | -41.534 | 2024-11-09 14:00:00 | GOES-16 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| c129e0ef-930a-3e44-a67c-1f97e9b95de8 | -2.2318 | -46.5508 | 2024-11-09 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 584cc5a8-600b-300e-bacf-6ae8b9e5a1da | -7.1778 | -42.0055 | 2024-11-09 14:00:00 | GOES-16 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| c89d6846-7ebc-363e-9b59-e6a84c763735 | -3.9485 | -48.1508 | 2024-11-09 14:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0ad38701-cce9-33fc-8e65-39f6bd4c888c | -4.807 | -44.7606 | 2024-11-09 14:00:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 217.1 |
| ea57f113-672c-3e68-a672-343f3da6ec30 | -3.125 | -50.1629 | 2024-11-09 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 4e0b2e61-ab85-3688-99f9-0d3eaf10ca4d | -0.6177 | -49.5351 | 2024-11-09 14:00:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| f96c6d16-963e-3d07-8dd7-e65c2af980c3 | -2.3918 | -48.5699 | 2024-11-09 14:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d4648dc6-9a88-39fe-9d36-7f282183c7fa | -2.2479 | -53.7627 | 2024-11-09 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| cfbc94bf-abda-3788-a582-c5a7afbec958 | -2.5781 | -48.1777 | 2024-11-09 14:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 3ae517dc-d7f9-39d8-bcc5-a2d9483051f3 | -0.2299 | -51.6455 | 2024-11-09 14:00:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 125.0 |


[Clique aqui para ver as próximas entradas](README122.md)
