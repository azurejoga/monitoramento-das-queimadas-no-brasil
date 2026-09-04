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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0fd9803-afe1-3bb8-a7e6-efaa072f638e | -7.88037 | -71.76085 | 2026-09-04 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4301891-8dac-360e-a0cb-38c101d6b008 | -9.04378 | -65.74505 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff6e4bbc-4727-3979-82ed-fa88b4548734 | -9.03916 | -65.74142 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70445b0f-72b7-387f-aabd-48fce53242cf | -6.99736 | -62.99337 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daf3d835-41be-346d-88aa-87171b7717e1 | -10.28669 | -68.83566 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26502572-d62a-33c6-b3f3-033edb403830 | -7.79318 | -70.05673 | 2026-09-04 06:20:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cdbf412-8eb4-345e-84c9-2a319208be6c | -9.03876 | -65.74432 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4524f7b5-e83e-3058-88ec-5da211849bf6 | -10.20107 | -69.08941 | 2026-09-04 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95bb9099-2129-397a-987b-642440306b6c | -7.55268 | -61.34864 | 2026-09-04 06:20:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b94a2d16-becd-3061-8bc1-be7c2baa1717 | -6.99205 | -62.98835 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8250dc0e-ddae-3ac7-9107-3c6da21a12f9 | -10.2887 | -68.85141 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c716b4c-1964-31ac-b6ed-6b430892edc8 | -9.1169 | -65.49943 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 596119f9-3eca-3b86-91e6-63c5341dd178 | -6.68591 | -59.9694 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a3480f99-ea44-35d9-a7bf-3e7156e4472f | -9.0215 | -65.45277 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a93f1411-a800-32d6-893f-2ab0ef44c3a6 | -8.17033 | -62.77834 | 2026-09-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bef2e18-0fd6-3c10-964a-c62fbc4f0dd3 | -8.8906 | -71.31638 | 2026-09-04 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84603e2f-7687-35e0-8173-9ae7b2602702 | -9.04444 | -70.89634 | 2026-09-04 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e856d7a2-8a62-335d-a7b6-8c0c630ce4a1 | -8.92412 | -69.47252 | 2026-09-04 06:20:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97d82895-8cb6-31e4-aa7c-b468e1121f60 | -9.10626 | -65.50102 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9fe79ec-152d-3ca2-b933-03b80217c235 | -9.04418 | -65.74217 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32c8e002-b7b2-3c51-ab3b-5cf19bf0690e | -7.87637 | -71.76407 | 2026-09-04 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdd0581e-35fc-3671-b8f9-da6cd61e7a24 | -6.14843 | -59.94479 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8469ec5e-64d2-3b92-925a-a1ff5db103c4 | -8.82015 | -68.67622 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31d52ccb-5af5-35ed-ad7a-63da433fb30f | -6.99793 | -62.98916 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc731d18-4426-3a33-9d6d-5e74d2cd69df | -8.86732 | -68.49667 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 759daa76-4147-31d9-a863-60e64ea6f8e4 | -7.88724 | -71.73882 | 2026-09-04 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4e8f5ce-4444-3f39-b047-7e5fd4b81168 | -6.6753 | -59.94125 | 2026-09-04 06:20:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91e070c0-d050-31b8-9a54-d13d89fa6480 | -8.3367 | -70.73142 | 2026-09-04 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83f1c953-8c3a-3cb8-ba7e-c13ededf076e | -8.60226 | -67.18797 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 498f361c-8759-35fd-b67e-d56e1464c894 | -8.60744 | -67.18405 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5d27cbdf-fb9c-3667-ae3f-540b75921789 | -7.38779 | -72.80004 | 2026-09-04 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 017ddafd-01a1-3c24-8633-80af2e51f3a5 | -8.48175 | -70.61653 | 2026-09-04 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 706da6f0-f66f-3de6-ab2c-630341593409 | -6.67798 | -59.97519 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 32c96584-3a03-3523-8991-4c276be935ab | -8.59968 | -67.17357 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| e2466dcf-00d5-3249-96b6-d4b2f8193a1b | -4.10034 | -60.66101 | 2026-09-04 06:20:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67e96fd6-0172-3e9f-afe6-4336a0547e38 | -9.74234 | -69.07446 | 2026-09-04 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b654f944-0fae-3ef3-ae44-32954617cdf6 | -10.29177 | -68.85962 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 274132ce-d058-3601-a362-cb1392e784e7 | -8.56568 | -63.19672 | 2026-09-04 06:20:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ea8c715-cdb0-338f-94f5-6fb4df7b338e | -6.67973 | -59.96194 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7ae745c6-a5bf-3566-8952-190c5f790209 | -8.5255 | -67.16489 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98b55eff-2717-3a8c-ad33-b59468b9985c | -9.04339 | -65.74791 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b37f6250-624b-3361-8ae1-3aab610b8de4 | -8.87563 | -68.49786 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5261b003-467f-36b5-adb3-5f603a43e2a5 | -6.68235 | -59.94213 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6558a2b7-cebb-332f-a3af-e74f42358997 | -7.87694 | -71.76031 | 2026-09-04 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d57092ed-2dce-3a39-ba20-140434420411 | -8.6357 | -67.01767 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13aa9b1a-3cac-335e-8b7c-7dfbe28b6bfe | -8.60356 | -67.17883 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 9de2b21a-011b-378c-970a-13312364b23a | -9.24789 | -68.22338 | 2026-09-04 06:20:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42630f71-cf0e-3af1-a55b-f96c63e07fd6 | -9.04883 | -65.74567 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 905f8ed7-6ab1-301e-b39e-4b95e87837fe | -6.67265 | -59.96133 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c61a4ffb-2381-33e9-af92-b3b271252511 | -9.01796 | -70.90086 | 2026-09-04 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7eb1b5b-89c9-308f-a03d-17ab56f73013 | -7.78408 | -63.38616 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f88ac7dc-c278-3ee3-90ba-f7e87f82d593 | -9.04824 | -65.7451 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22e2e9b7-44c9-3c9e-8145-c1e632db3428 | -9.53515 | -68.63136 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0da97634-2519-3f6c-a553-fbea2c24730b | -9.11137 | -65.50177 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e27a70f-1a97-32b0-be18-7f8811e759e1 | -3.757 | -61.75769 | 2026-09-04 06:20:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b97bb2de-dc49-3a49-9c26-640be23616c1 | -6.66735 | -59.94715 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd26854a-a0b1-3ae2-95d9-9b2a0326951e | -7.89068 | -71.73936 | 2026-09-04 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc60cd8d-322b-30c1-aeb7-83eed63be0a3 | -9.02953 | -65.7369 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52615ce3-71a3-3135-97bb-3935621b562b | -7.78352 | -63.39021 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 446daf93-66b9-3bc5-ab90-67a1655792d0 | -8.59516 | -67.17292 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d2a985b-5b15-3c71-bca7-696281a024ca | -7.55341 | -61.34301 | 2026-09-04 06:20:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb37df87-83d9-3bfa-a75e-39e9c7415b85 | -8.16864 | -62.78057 | 2026-09-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dbcaeb3-df44-34e1-8195-ce4fd7f2ef56 | -9.73777 | -69.07746 | 2026-09-04 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e752a9c-5902-3bd6-9ba1-a9a8ea32738e | -10.20055 | -69.09301 | 2026-09-04 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95a3dc94-fec6-3f82-924a-550b8bd10f73 | -9.049 | -65.73931 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91024600-3c49-374c-8341-3efc532e2f21 | -10.2903 | -68.84003 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be0703c8-229a-3dce-b8ce-9cfb96f03419 | -7.73125 | -61.65144 | 2026-09-04 06:20:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 875dfc5e-1e70-32b7-8ba7-5db0ac6019d9 | -8.56624 | -63.1924 | 2026-09-04 06:20:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 249454fa-459d-3cd2-9dd2-b6d29cf051a9 | -7.37723 | -72.6758 | 2026-09-04 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd329481-defc-3a45-93b7-de749af7603b | -7.73971 | -67.06927 | 2026-09-04 06:20:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc819c88-731b-3b0e-ba95-b69abd76a0c8 | -9.04786 | -65.74798 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9415602c-530e-3757-898e-736532814a1e | -6.68501 | -59.97616 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6e4302da-0f38-3a5b-898b-36d9c583602b | -6.70799 | -62.85958 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aeaaca8e-e1f2-38ef-b727-cd40b3c73c54 | -8.86395 | -68.86078 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff80ebb8-21d8-3cfb-a613-db6b5bbb1077 | -9.02191 | -65.44974 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fbc237d-8082-3ecc-8620-5294eb14d5d2 | -9.04923 | -65.74277 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9ebf7da-5b7b-3e70-a010-1f96509f067a | -9.00465 | -70.56589 | 2026-09-04 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c54008ca-10a8-329b-8364-93980b12e0b2 | -7.01025 | -62.98656 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72d556ea-820a-3d47-a318-c29c4e452c77 | -10.20114 | -69.08855 | 2026-09-04 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d76602c-c8b5-324f-9fa8-529bde86db6a | -10.28977 | -68.84382 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4749072a-4992-3130-ba74-648d795b6460 | -4.09953 | -60.6665 | 2026-09-04 06:20:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 506025f4-c4be-3565-8652-02d49a65919e | -7.73769 | -61.65239 | 2026-09-04 06:20:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f0b9d8b-759f-3e99-bbe6-d873b862a781 | -9.02232 | -65.44669 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d91f4a7-b4b0-3ee8-b6d5-396a1f121e2e | -8.80751 | -69.02649 | 2026-09-04 06:20:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89026e0d-62a5-340f-ae93-fcb86d92aa5a | -9.02993 | -65.73401 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7af0a95f-8dc6-3a7f-8e2f-4609bc012abe | -10.20064 | -69.09217 | 2026-09-04 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62c5579d-a686-3276-a97b-38707babc5dc | -6.35725 | -65.48756 | 2026-09-04 06:20:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87eefcc5-e26c-3f18-acd9-0e29a327b7b1 | -8.70725 | -69.99864 | 2026-09-04 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7101d130-12c4-3ae6-a19d-4f260ec45380 | -7.78473 | -63.38581 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb8b3545-e28a-3cff-a699-9a68ae0e00d6 | -9.10707 | -65.49493 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4fdfd28-3ce9-3fc4-937b-15b7b9d31bed | -9.04862 | -65.7422 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06f1dcb7-8da3-37da-adf2-7694aab2adc8 | -10.28763 | -68.859 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0e2d4b1-3f2c-3e74-a5ce-1234d62bda78 | -6.69119 | -59.98353 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9c536ad2-956c-3feb-9d6d-2e9ecfc23215 | -8.95332 | -71.25935 | 2026-09-04 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acc1cd7a-44a1-386e-8fdd-a28289a93bd1 | -7.55194 | -61.35424 | 2026-09-04 06:20:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7984f76-f3d1-3a6d-80e1-0e4e5f89e1c0 | -9.11218 | -65.4957 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b1f0873-7eff-32cd-ad7e-b1b76044dd53 | -9.1762 | -68.27005 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d755da3-2456-3a29-b963-2adbcaff1fd0 | -8.71102 | -69.99921 | 2026-09-04 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d13327b-03a0-3d38-8a8f-bdd7ebc2e367 | -7.01612 | -62.98738 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f73d5ec-a7ca-3475-8f9e-b0be22772985 | -3.77522 | -61.76035 | 2026-09-04 06:20:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README39.md)
