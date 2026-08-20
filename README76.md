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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69c712fd-2fe0-37fc-94ba-018ad16bf854 | -14.218 | -51.931 | 2026-08-20 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| f067ae46-7c26-306a-bda7-121389419ea2 | -8.2967 | -62.9079 | 2026-08-20 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 2a655964-5886-3e7b-bfa9-7e0d8043607f | -6.9129 | -59.3385 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 4a8c90ec-5b05-3074-9a82-3ee769f0ce55 | -14.2373 | -51.9284 | 2026-08-20 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 298.1 |
| 9c01307f-67f8-33de-b29e-7c8374fdd525 | -5.7903 | -55.7301 | 2026-08-20 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 3b069edd-5fbb-3a1d-ab7e-178988a9d3b1 | -5.6022 | -45.704 | 2026-08-20 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 357bce8b-8988-3dea-b17d-5d05d1ba1c73 | -13.5876 | -51.6715 | 2026-08-20 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| d022f3dd-e4a9-3411-8039-e7eff46168ac | -5.6024 | -45.6815 | 2026-08-20 14:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 907f8c17-573b-3f97-b973-4bfc9544cf82 | -9.4256 | -60.4353 | 2026-08-20 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 4d195228-7e59-307f-8a2b-4736218b51c5 | -7.4444 | -60.0092 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 7a7eb017-ca80-37bb-8e7b-bd62c43b1d06 | -6.7645 | -59.4794 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 273dd2c7-ca96-3474-99c3-82ebfb734e71 | -6.7123 | -58.9412 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 843966a9-db6e-303e-ab31-e28be6b9fd76 | -6.8991 | -55.7176 | 2026-08-20 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8fffde82-5b82-333c-8788-ff3d6965fc8d | -7.022 | -45.8878 | 2026-08-20 14:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 3050ac2f-5023-3efa-b795-ab05aa55f980 | -11.1747 | -54.0216 | 2026-08-20 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 143.0 |
| cfa2194a-5d97-3cb2-9513-9505e2411a1b | -13.6621 | -51.811 | 2026-08-20 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 1e7756d0-8162-3d9b-9cc3-411c925549a4 | -10.4084 | -61.2108 | 2026-08-20 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 04eb7a16-1420-3c62-a555-f9a5f3d029a1 | -11.2191 | -55.0382 | 2026-08-20 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 17b5e981-a8af-3035-bdac-d608f09618c9 | -7.7702 | -61.1634 | 2026-08-20 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f031de8f-5053-3284-bdb8-0512c7e8e95e | -22.7788 | -47.533 | 2026-08-20 14:40:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.3 |
| 64f12e2a-da24-374b-a8fe-1c047db2c6e7 | -9.2071 | -59.771 | 2026-08-20 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 205.6 |
| 0fca313b-3b13-3412-83fb-b8fe16e1b604 | -10.9023 | -50.2805 | 2026-08-20 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 4d04294a-52b3-34ee-a8a3-9c7b47c6c48e | -11.1936 | -54.0199 | 2026-08-20 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 316.9 |
| 74f6ca74-385e-317c-9a9c-907eb1c49349 | -11.1939 | -53.9993 | 2026-08-20 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 295.8 |
| 6d997d54-94b3-3a7f-a57c-d195a0f6e704 | -6.6745 | -59.0973 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 05136058-9611-39df-a7ed-14038117dd48 | -15.2069 | -52.8613 | 2026-08-20 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 2c5e62f9-57f4-3af3-aaf1-7b8ad25d6c2d | -6.6142 | -45.4486 | 2026-08-20 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 243.5 |
| 72cb60a7-0b6f-319b-acc5-ee86b524f784 | -8.2792 | -47.5538 | 2026-08-20 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| f71599e6-7f3b-3407-865a-3220914c1317 | -10.4085 | -61.1915 | 2026-08-20 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f32554d6-2790-3ccb-9a5b-e646d1fdb15d | -5.8088 | -55.7095 | 2026-08-20 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 195.6 |
| 0f1330ea-c249-3d11-aefe-623327dc8762 | -9.4071 | -60.417 | 2026-08-20 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| fd180cf3-3801-330e-9b4b-c70de6eed30c | -6.6938 | -58.942 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |


