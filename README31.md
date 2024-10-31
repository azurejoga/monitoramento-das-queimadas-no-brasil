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
| 41be134c-49ac-3d16-a63c-318ebf8286cf | -2.52396 | -48.46137 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34173779-c5e6-3427-a031-e2d9f5e48e72 | -2.52332 | -48.46559 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64a52498-c55a-36e8-8244-e019346c9e3c | -2.52268 | -48.46981 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5a8ea910-2fe1-3753-ac39-d3544cfe099f | -2.52204 | -48.47401 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e23ac81c-887d-3733-88db-25fbc7112044 | -2.52097 | -48.45661 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76e060c2-6b60-3e35-9edc-83ab106b4fff | -2.52033 | -48.46083 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d4825ce-da04-3861-8ccf-8f536d479f1f | -2.51969 | -48.46503 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1564bc3e-ce47-3271-b5d1-5361f16b0f0f | -2.51905 | -48.46924 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0541aa6c-3db2-3bd4-8c59-7dca2dc492f2 | -2.51841 | -48.47346 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fe030c6-6acc-3b27-82b8-edc58f3111b9 | -2.5167 | -48.46026 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c4d5cb4-aac4-3d71-880a-354465ed9279 | -2.51606 | -48.46447 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 018b9267-5f9b-3e5e-828e-0baf619a2e98 | -2.51577 | -48.46123 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4cc4ebe6-2048-3111-b1bb-bf3651e2b7a2 | -2.51542 | -48.46867 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ff0414f9-ec8c-3e4a-82e4-1aeec1eaf0b5 | -2.51511 | -48.46543 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8634c1ba-a21d-3049-b031-ee480c39d866 | -2.51444 | -48.46962 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d5122fc-72e6-340b-a6b8-e7dcdf4936fa | -2.51179 | -48.46812 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a11ce63d-9c6f-39bc-a97e-d546e27d9833 | -2.51081 | -48.46906 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5cb3a75-5b73-3ec6-9e90-56b1526da3d7 | -2.42812 | -48.25787 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ff87c11-4e5e-3f65-a70d-579d9afc4ed1 | -2.42393 | -48.35623 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8f27afc-290a-3296-b5bd-74b88c345aaf | -2.42362 | -48.35776 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a2c03b0-05b3-39ce-a50c-6e9a95a1c1c8 | 0.08653 | -49.87305 | 2024-10-31 04:46:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a57f53b-01fa-3e41-8bfa-c31e3cf18f2b | 0.08597 | -49.86951 | 2024-10-31 04:46:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6124f479-cb60-3685-b541-0081ce1cce83 | 0.08542 | -49.86596 | 2024-10-31 04:46:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dbc0aa7-c95f-32b7-85da-cb25e9894141 | 0.08206 | -49.86648 | 2024-10-31 04:46:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82effb60-a4a0-337f-bad0-8447e353ed97 | -0.61094 | -49.44386 | 2024-10-31 04:46:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 014d9c06-d78d-3e23-8c8c-864831b968c9 | -0.21596 | -48.9912 | 2024-10-31 04:46:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15f47f44-0a24-382b-99e3-05343f054ad5 | -2.01215 | -50.25341 | 2024-10-31 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea01eb8b-c6d5-3caf-bba4-11bff9e4d5d3 | -2.7491 | -49.30584 | 2024-10-31 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dba0b678-3566-36c5-953e-eb5ba0adfcfa | -2.55352 | -49.8682 | 2024-10-31 04:46:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3954bb22-015f-37c3-a92b-12bddcb6819b | -2.44538 | -50.29767 | 2024-10-31 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d66de5b-9416-324e-a33d-ab6219d0390a | -2.35992 | -50.32524 | 2024-10-31 04:46:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c6a39d3-c06f-354f-a91e-365c61e0e811 | 1.14956 | -50.73543 | 2024-10-31 04:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e88906a8-b337-3fee-ae4e-0f0f32fc820c | 1.13346 | -50.93844 | 2024-10-31 04:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26c02e68-8517-3839-9360-7d61135c831a | 1.13292 | -50.93501 | 2024-10-31 04:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c755b51c-08e4-34ba-8c58-c59f1110cd8f | 1.13016 | -50.93895 | 2024-10-31 04:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbf22dd8-9c32-3739-a013-a4e5688c9278 | 1.1169 | -50.96206 | 2024-10-31 04:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bbcd01e-7784-3e34-b045-bd439ea4de67 | 0.3265 | -50.79731 | 2024-10-31 04:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9456574-0c72-33d1-8e68-1102b7c80b72 | 0.29705 | -51.21652 | 2024-10-31 04:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3597568a-0af1-30df-b010-775b763726ee | 0.06066 | -51.07485 | 2024-10-31 04:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b087f1a-4a4e-3d5a-bddf-2933632d9dee | 0.0579 | -51.07879 | 2024-10-31 04:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 935ff6a7-891b-3ce1-ad8a-01e1eec80062 | 0.05736 | -51.07536 | 2024-10-31 04:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11c7aba1-bda2-3e73-be8c-c533c6851cdd | -0.04872 | -51.43584 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32b82b8a-e9cf-365e-815b-90c640d70003 | 0.44866 | -50.2767 | 2024-10-31 04:46:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63184ee8-792d-3c2e-af56-4807f821986c | -0.70094 | -50.35564 | 2024-10-31 04:46:00 | NOAA-20 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1799f28-b6b6-32ca-b4fc-13ccb9c07f05 | -0.16278 | -50.40763 | 2024-10-31 04:46:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 343d106d-fd6f-3b2f-838b-9b7f1cc12b47 | -1.36627 | -51.42062 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 604dd0fb-baee-3ed9-b98d-3ddf4d3a3bc4 | -1.36519 | -51.42748 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48322cc6-3fac-3c3c-8518-aea0601220ac | -1.36465 | -51.43091 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3987041d-d44a-33c3-8b5b-60f5b69cd458 | -2.18584 | -50.78933 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c9e06c4-d4e3-3721-b1b0-0134b8f63680 | -2.11776 | -51.11613 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c574947-f16a-3059-8dbc-41d712895884 | -1.8687 | -51.01309 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d92820b-dfd3-355c-ac39-93135ee2fdf1 | -1.52261 | -51.50864 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e6dfd70-39fa-35c4-b71f-bc74d5ee8865 | -1.44672 | -51.47216 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 756f29cd-da7e-3424-a8f1-5942baf5620d | -2.33192 | -50.59306 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 45423abe-5da7-3b70-920b-9da9965bb740 | -2.32858 | -50.59255 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d40ee66-4b4e-3d60-b264-695fabdd45c4 | -2.25608 | -50.68926 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b303d3c-4741-3742-9422-b332f3a47fd5 | -2.25275 | -50.68874 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6c0553b-0300-3675-a9c5-e396d5bde052 | -2.2522 | -50.69224 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d8a372a7-cd84-30d1-8d8c-e14498f2db48 | -2.58329 | -50.66026 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb2bc389-f2c4-3d0e-8044-e9392138c996 | -2.56769 | -50.65065 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51ae2a02-f40b-3755-8ea0-91853489abf5 | -2.56714 | -50.65416 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af8bbf1a-51e9-309c-9eb1-5ef117a5e76d | -2.56435 | -50.65013 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97fc90ab-e8ed-36fe-8ca3-ad48e123fd3f | -2.5638 | -50.65365 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d0fd099-7a02-3153-8289-8afbc1b59c69 | -2.50665 | -50.71318 | 2024-10-31 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b0f65b8-009a-38b7-9bbe-f5ff804e2ad6 | 1.12108 | -52.59071 | 2024-10-31 04:46:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75195019-fa1d-38c2-99bf-9204d8cfecf5 | 1.07491 | -52.49438 | 2024-10-31 04:46:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de1b15f0-9797-3639-ad51-51a678444071 | 1.01151 | -52.21946 | 2024-10-31 04:46:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c3539bb-be36-3a28-b139-38c57f29f94e | 1.00924 | -52.21965 | 2024-10-31 04:46:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07ec34e6-da82-37ff-a6ff-75e8da48c470 | 0.9519 | -52.09486 | 2024-10-31 04:46:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2e9a91c-76d4-3af6-9ff2-4b430b44a7e2 | -0.69502 | -51.99493 | 2024-10-31 04:46:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9edecb4-80ff-3710-9fb8-5af192ea0651 | -0.69448 | -51.99838 | 2024-10-31 04:46:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 149262e4-d711-34b5-a994-25f994f8ac17 | -0.69325 | -51.6803 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2768d0e2-f4d0-329b-a58a-22d7803e40c6 | -0.69271 | -51.68374 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2108e690-d01a-3658-aa5f-b98f1c4d6848 | -0.68995 | -51.67979 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f73e99f4-d593-3cfc-9541-3f560e7cc36c | -0.68941 | -51.68322 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bb062f5-97d0-31b8-bb94-0880e34efcd4 | -0.16177 | -51.66773 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6596bb1c-c82a-3c27-8b1f-6897d6765009 | -0.15847 | -51.66721 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2ddf199c-308d-3763-aed9-72a9e99c44bd | -0.15811 | -51.56159 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2f8e11cd-ef45-3ded-8804-e8fa884ff1e8 | -0.15757 | -51.56502 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdaf0f49-d301-372a-8696-a1f9633a90a4 | -1.82134 | -53.23563 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf7fddd1-09ed-3f72-aef7-8a0e52d111ce | -1.60236 | -53.20148 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 566cff56-b1b5-3b7a-8ebf-abbb95c86064 | -1.60179 | -53.2051 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9239a8a6-5c7f-3c19-ad6f-c0beff080953 | -1.58286 | -53.10596 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2feb7a45-c6e4-398e-a927-9f7ff5237f67 | -1.58265 | -53.1945 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a53527-056b-3357-92aa-9a5139ec8c0b | -1.57948 | -53.10543 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82054db9-3637-3796-ba19-bcddfcbbac49 | -1.57891 | -53.10903 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad063f9e-a8de-3b46-9b62-edaf4fc20176 | -1.5787 | -53.19757 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48e9aadd-0e3c-3d3e-9e28-f59c87bf7b78 | -1.57553 | -53.1085 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c92c1a31-c4cc-3dad-9529-14330875abc5 | -1.57496 | -53.1121 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9896abbf-317d-32f3-afee-2494a5644a13 | -2.11747 | -52.34874 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5585885-1590-3123-9fb8-897050872d4b | -1.83197 | -52.43536 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14209627-cdc6-3065-b8b3-bb7bf24fccce | -1.77106 | -52.30499 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbc93d55-0b1a-3a78-99c6-33d7d42686b3 | -1.76774 | -52.30448 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3297ba0f-0606-3877-8869-d9d4eb154498 | -1.70276 | -52.50089 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c654561-fe69-34bd-a1b3-013089268ab7 | -1.69112 | -52.50981 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39654ceb-cbfe-39fb-80b5-5353acb49128 | -1.68235 | -52.71677 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe28bdf7-6e58-3053-bdba-dd318d149f02 | -1.65062 | -52.65776 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff2ad473-2ac1-3daa-818c-6776ceffb3d8 | -1.64728 | -52.65724 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a8be0c4-176b-3d68-8290-d6690268d30f | -1.64394 | -52.65672 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a00730d7-b869-3388-9b1b-85fc7d6774b5 | -1.6428 | -52.58079 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README32.md)
