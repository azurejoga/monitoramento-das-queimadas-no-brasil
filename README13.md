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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3710bee-349c-3ad5-aee5-2f623f89ef97 | -3.33323 | -52.59854 | 2025-09-24 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0695dbb7-2fe1-3a5a-942c-6a99270a5f45 | 0.9504 | -51.19404 | 2025-09-24 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f073364-a64d-3823-831c-30cb33ed5199 | -2.30784 | -48.14653 | 2025-09-24 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4357a2ab-9010-3472-a1b1-e5f760b790ce | -4.79675 | -43.53532 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 29b59753-f293-3668-beef-4a244887e2da | -2.30415 | -48.14595 | 2025-09-24 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5edc09c-0cc0-3281-87cf-8ab4194b4e8b | 0.94711 | -51.19455 | 2025-09-24 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e90ef5a-3d50-36a4-80fe-d6a75cc96c8e | -4.07566 | -48.04419 | 2025-09-24 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd251ac3-9327-320b-98a0-5423fe350fd7 | -3.16468 | -41.64899 | 2025-09-24 04:49:00 | NOAA-21 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 18456236-88ed-3221-9c12-f97334291896 | -3.86309 | -40.35913 | 2025-09-24 04:49:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5ba5e762-c7cb-3673-9906-0db7d621b7ab | -4.19508 | -47.16543 | 2025-09-24 04:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38fdca0e-e7fa-3a57-841c-2a691f52c7be | -3.15237 | -49.1161 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee1f331d-dd81-3f9a-af48-0ab6be9f343b | -4.79684 | -43.54 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ad9006f6-73f9-35bc-b18e-afb280c2ebe1 | -0.9103 | -47.54401 | 2025-09-24 04:49:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c5a1ee8f-06e0-306d-bd42-2f3d148c421e | 1.34221 | -50.69765 | 2025-09-24 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a6bbdee-6518-30f7-97ad-00f7c1fb0892 | -2.79504 | -49.5952 | 2025-09-24 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 176a9596-e4f2-3d99-be21-1ce566aaa86f | -4.79207 | -43.53603 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 953e26be-a84d-3cdd-a470-416c396130b6 | -2.30718 | -48.15088 | 2025-09-24 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9be265ff-5ac7-305c-be52-1e4fc8308ddc | -2.95973 | -52.50443 | 2025-09-24 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d75ca44e-9690-3d96-b369-5dc5bf214ded | -4.7518 | -43.62484 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d10374da-6405-3b10-b542-6b106ea999fd | -3.42018 | -52.67294 | 2025-09-24 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6409dac-c987-3373-99a8-78cb45521b49 | -1.76891 | -55.49929 | 2025-09-24 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c65cb821-dad0-3630-9806-36ef9294286b | -4.08016 | -48.04017 | 2025-09-24 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a407eda2-6d53-37d5-8f11-7cd611a634eb | -2.97591 | -49.06228 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5a1b10d-3147-33ce-8008-3641b974e05a | -3.69241 | -49.01863 | 2025-09-24 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 850934f0-82c9-3435-906a-3c70f83e8ddf | -3.41963 | -52.67641 | 2025-09-24 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b475785-d7f7-373d-b3f5-e6ac88433174 | -5.49396 | -39.17237 | 2025-09-24 04:49:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2e56f043-5960-3692-be52-08fa99a81a49 | 2.59101 | -51.6538 | 2025-09-24 04:49:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d038cb9a-51b2-3ba1-89e8-cb539170cc63 | -3.3032 | -42.1719 | 2025-09-24 04:49:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7e8bd6f6-192c-3ca6-bacd-8b2cefa6cfa5 | -2.74436 | -49.55616 | 2025-09-24 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f48dc1ab-18ee-3bd3-9fb9-0f0aa9000c8b | -3.64459 | -51.867 | 2025-09-24 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee4a1e2b-b145-3e94-abc0-994703636f3c | -3.159 | -49.47915 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07139d1d-5a4a-3322-b58c-25174e17dbd6 | -3.15959 | -49.47525 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cedf1e04-a637-3d81-aee9-599aeb1dae32 | -3.69304 | -49.01452 | 2025-09-24 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0efec40-1658-38cd-aa47-b03e906cb972 | 0.93776 | -51.19949 | 2025-09-24 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75a6e574-d840-3f18-9807-c0af8d814eb7 | -3.17535 | -52.86515 | 2025-09-24 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 902fbf49-a823-3f0b-adfa-a73421677e84 | -3.64199 | -51.90522 | 2025-09-24 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 329e76da-e507-3d16-8659-2a63ca3bb0f0 | 3.06649 | -61.12985 | 2025-09-24 04:49:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5ee35fc4-9d09-3341-8ac8-89c01a47e2f1 | -3.40246 | -44.34403 | 2025-09-24 04:49:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5cfd2b9-d904-3dcf-a84f-354d1896a8df | -3.15592 | -49.11665 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b8d9c51-3186-3078-8ea0-3387c55e40cf | -4.20166 | -46.81641 | 2025-09-24 04:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d48fdd4-2fbb-3f10-bd41-29c8b36e8be3 | -1.08829 | -54.10954 | 2025-09-24 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58450a0b-6fc0-33bb-9655-4fcb2203ac7f | -3.21606 | -49.17382 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e08112d-d8ca-33eb-b68a-1f9e03f8c0c5 | -3.62443 | -51.90953 | 2025-09-24 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40dfec25-fa6a-3cc8-be90-3bc5b508d828 | -2.42638 | -47.15398 | 2025-09-24 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 857e65a8-bd58-339c-b24a-51bceb2f630e | -2.96688 | -49.56987 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b57dd8c-31f1-322b-a79b-d482df2a974a | -2.25116 | -47.88079 | 2025-09-24 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c268851-a31d-3326-9384-b13c645bd631 | -3.19111 | -51.7005 | 2025-09-24 04:49:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d29d6974-2c0b-3660-b490-572439fb526c | -3.19138 | -48.8131 | 2025-09-24 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 954cbc65-f47d-3e0d-aba6-dcdc347f6ab6 | -4.79154 | -43.53455 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dfbaf26-17a9-3370-94af-fddae9d86f04 | -2.78703 | -49.57838 | 2025-09-24 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc82db30-24b5-3e04-ace9-dabc0522c786 | -1.8015 | -47.70369 | 2025-09-24 04:49:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92014d97-7ac3-3476-ae6f-88ab15cebf1c | -1.12254 | -54.15018 | 2025-09-24 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fa6bdae-0c97-3831-bb14-d34529e7cdc1 | -3.34381 | -51.63682 | 2025-09-24 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 360f01b1-0f41-3c82-856a-54149f0b1bff | -3.27597 | -52.42034 | 2025-09-24 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a05e5bb-6947-38b2-95f6-fb2814c97113 | -3.41607 | -52.67504 | 2025-09-24 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 48bb8a3a-e66b-3095-97b7-6e486e4b68b6 | -3.39445 | -47.49943 | 2025-09-24 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89007821-1379-310d-a8b2-da61737da837 | 0.60585 | -51.38844 | 2025-09-24 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f25bdce0-d713-3edf-84ae-1a788777b23a | -2.25421 | -47.88589 | 2025-09-24 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbbb2a00-1bc4-3122-8521-e0f6df0e9895 | -3.64488 | -48.32402 | 2025-09-24 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1c80bed6-e7c9-3959-9f40-c526ca77ce5e | 1.34275 | -50.70108 | 2025-09-24 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7e2796c-4b1a-3360-9e61-fd815a47efdd | -2.35713 | -48.89141 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 921523a5-b021-3cc4-bbdf-e493f296b8f7 | -1.80527 | -47.70427 | 2025-09-24 04:49:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 009a7b9e-d2e5-311a-85ea-6363d70dd9fb | -3.95038 | -49.4427 | 2025-09-24 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4a11d88-61ff-3a56-b8a1-9d828381a946 | -3.62773 | -51.91003 | 2025-09-24 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f759e2de-f6c4-3a27-a7de-632510536faf | -1.0918 | -54.11007 | 2025-09-24 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3458eb8-98a3-39e9-ad84-c083a6ba26c4 | -4.76445 | -42.09128 | 2025-09-24 04:49:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ceaf8f0e-70b5-328d-9cdc-2ac9dbb54770 | -4.2011 | -46.82014 | 2025-09-24 04:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b2108b0-403f-3ea5-8a65-73af694e68a6 | -6.53729 | -44.22401 | 2025-09-24 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10014d5b-5ed0-3990-b5eb-7103cfd7c6bd | -5.64476 | -43.91879 | 2025-09-24 04:51:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 72b856a4-86ed-3265-80cf-5f4ef4cb2e98 | -5.47297 | -44.69009 | 2025-09-24 04:51:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4bae482-9299-3f08-a850-f4a67d8501e7 | -10.62944 | -49.05764 | 2025-09-24 04:51:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0a2fd25-1fb1-32b5-8a17-3c7131e262c9 | -9.73619 | -46.66315 | 2025-09-24 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 98f2a277-3af5-3efa-9611-c92b80f7ca8a | -4.3122 | -48.09531 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 864d4253-6f43-367c-951c-7cb6bf2361bc | -9.69316 | -48.90381 | 2025-09-24 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1aa1b838-96c6-3c42-b974-92d363d2f3d3 | -3.4994 | -53.44605 | 2025-09-24 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 72b5b445-64a3-351f-a37b-c0ccc3b5672c | -3.77844 | -52.12313 | 2025-09-24 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f378a743-ae2c-30ff-b516-04e1989d8f13 | -7.19922 | -46.67294 | 2025-09-24 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5d3d9b1-4aa1-3731-9ce3-c0b7904d83c1 | -11.64364 | -44.3532 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 359c1ff4-a639-324a-9144-6769e2ac3164 | -5.63398 | -51.94263 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 573f9c75-eedc-38cb-9736-3c6c0b4c3f4a | -8.32214 | -46.22227 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9d4736e-0ad9-3238-8089-d6afd68a1abb | -4.96047 | -47.82252 | 2025-09-24 04:51:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66c6d1ac-c550-3ee6-b9d1-adc6f17cc28c | -7.36703 | -47.04203 | 2025-09-24 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03692215-cf85-3279-b028-db8244d89734 | -3.66591 | -52.03884 | 2025-09-24 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2958534-a1bb-3f5b-be2d-97931ed967c0 | -8.55302 | -44.96388 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91677d96-c6fa-32de-96d8-0156a31a203a | -7.82725 | -47.86392 | 2025-09-24 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| caba9f94-f14b-3b26-adf7-de027db4a0c3 | -5.84463 | -42.64839 | 2025-09-24 04:51:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3b147feb-e36f-34ab-9c7c-0366c0d2c2d6 | -4.11076 | -51.08078 | 2025-09-24 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b913876-9ad4-3469-a4e4-9ebf732b7b2b | -8.54722 | -44.96906 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1143c0a3-a4f7-32ec-a5e0-101543a5c734 | -5.38862 | -42.26535 | 2025-09-24 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 919b6a90-c3de-3bd9-b13c-cddf1a22d143 | -5.24339 | -43.71957 | 2025-09-24 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 80ef1574-3ae6-3dd9-aafa-ba1b2e3423c5 | -5.30325 | -44.81082 | 2025-09-24 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5135dede-0b70-3b75-9cc0-0591a55f653e | -5.63005 | -45.73299 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7ab000a1-b92f-3549-b6df-963c753ceaee | -7.28347 | -41.86525 | 2025-09-24 04:51:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b243d464-8d3d-3975-a910-1e33018d0767 | -11.52747 | -43.6701 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38af46f7-f734-3cbb-88e4-0425f5165063 | -3.77786 | -51.40783 | 2025-09-24 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bcdc067-702a-3b9f-bec9-350ab9a56fa8 | -8.52093 | -45.01269 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a6169ab-177b-3493-a753-6eaf40a83a60 | -5.6505 | -43.61094 | 2025-09-24 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f46d9de-1e10-3f0c-a1f5-b61742a966fd | -4.41752 | -55.69184 | 2025-09-24 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c3ff7d2-4a9c-386c-b4a2-e8879f16f94c | -4.32986 | -48.39026 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f36e2c36-878f-3e02-abec-bd2d66cdd676 | -10.62764 | -53.8874 | 2025-09-24 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README14.md)
