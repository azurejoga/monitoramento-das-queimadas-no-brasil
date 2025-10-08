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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09093686-b062-382a-b3c7-8054ac50946f | -9.04022 | -50.62365 | 2025-10-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a5e97e1-a316-3875-be23-61f117822194 | -5.14948 | -46.09473 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6dcd7f6c-bd62-30a1-894a-929371caf87b | -4.69417 | -46.46901 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bed0d3e2-6030-34ed-ac08-059814f78b55 | -8.4126 | -46.80653 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca04e505-8409-333c-9da9-6841f8baf243 | -8.70497 | -47.87145 | 2025-10-08 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82fdf422-459c-3d93-ad41-97ef15499235 | -3.81289 | -49.4605 | 2025-10-08 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63a6bead-05e8-3aef-907a-0552bab617ff | -3.78946 | -50.37726 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1760ddbb-7ac4-3f71-bb62-95bf5424f7e2 | -8.9697 | -47.48268 | 2025-10-08 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d1d991e-de17-328f-8ff6-8db3bab524e2 | -9.63164 | -57.02373 | 2025-10-08 04:38:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b2d3e5d-4dab-3037-9719-ee5ae0c01420 | -10.34998 | -51.85284 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dad77aaa-d402-3eaf-89d0-7999b2135589 | -11.87178 | -44.93731 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f21ec961-d5fc-3340-a33b-ca7a2787b02d | -8.67982 | -47.07578 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd033ffd-f6f0-3064-8b74-e5631f9f0081 | -7.09955 | -48.2976 | 2025-10-08 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33ff8efc-57a1-3714-b8cb-e336f964efe9 | -5.72568 | -43.61524 | 2025-10-08 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbe2a7ed-bed6-32db-a2a9-d9f8358b814f | -7.79105 | -44.22749 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d7153b2-c70c-3059-a644-417b563befd4 | -11.30095 | -48.26851 | 2025-10-08 04:38:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d045fa75-afd8-3a45-98d9-cd95660915c0 | -10.64249 | -47.45612 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db07f5a5-944b-32d0-91e5-21e5128037a7 | -5.85112 | -43.41335 | 2025-10-08 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15133a61-e068-37b2-9a15-53bdd26fc060 | -11.7106 | -46.36123 | 2025-10-08 04:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e58807a8-c388-3497-9367-bfc38f5d4ce2 | -11.14375 | -47.7524 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5b7fd65-6138-3faf-874e-1baa7fb67968 | -8.39627 | -49.73708 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdc62791-3d61-3479-bd98-78a69d5a58ed | -9.00409 | -45.50805 | 2025-10-08 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d059890-9918-39d5-b321-70297bacfda1 | -7.34788 | -43.86605 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9cc0a1c7-2703-3282-a295-ea7cbcb9b3cd | -6.98365 | -45.19044 | 2025-10-08 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29b46691-02d7-3d98-9c19-11a2e68e7ee2 | -7.47466 | -43.12846 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7d446c5b-18e7-363e-a27f-f0ac2e066071 | -7.46166 | -43.02795 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ebc2493b-e469-3313-8902-ff64bebcf87b | -8.37249 | -47.75729 | 2025-10-08 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25934191-9629-3da9-b886-0bef667fca72 | -7.1347 | -45.92887 | 2025-10-08 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23188361-56ff-32a1-af13-bf1d7fce3a63 | -10.60846 | -48.67751 | 2025-10-08 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4184de47-250f-3076-aa40-fdc7f88b0f40 | -8.85767 | -46.77583 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e16eb36-cb97-3854-a0a9-cdb07bdc28bb | -4.91883 | -48.54528 | 2025-10-08 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 762aa163-7ffa-3148-bd08-4f313b86c831 | -4.68136 | -45.84059 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3198f36-f6fb-32bd-b4a4-f7a7ccc9dc32 | -7.44513 | -43.14613 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9b79f48d-d7ba-3a4d-9725-c82d1a972bac | -4.50893 | -46.35498 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3768fc16-ab80-36fd-a089-26cb888be487 | -7.82401 | -44.14704 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 906d7c45-36b4-3ed2-9196-313c8cf8277c | -7.6184 | -44.13353 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5dea9ef-50ae-3b8a-a8b4-a38f13a871bf | -11.50196 | -44.96749 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bd82127-76c8-3205-8d91-5e693b1db05b | -10.48107 | -49.36845 | 2025-10-08 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00bcc443-5505-37ba-905d-a4c611e1dc85 | -10.43429 | -51.63385 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6430c93-1916-3a74-95f2-bd293c4c2b2f | -8.25575 | -50.08852 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fabda8b5-acff-36ef-a741-400a8446caca | -4.50109 | -49.3845 | 2025-10-08 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89164759-a378-3dcd-b122-4407de0d0372 | -8.1927 | -44.11291 | 2025-10-08 04:38:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc8158a6-c20f-3a7c-a851-0ee75f6d71ba | -9.54354 | -47.76817 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a422edb-cfa6-36be-abee-22f157164ee6 | -5.32645 | -43.80839 | 2025-10-08 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c032fee4-a682-3ba6-b305-f1c04916e32c | -9.32624 | -60.60352 | 2025-10-08 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70d34677-926e-360e-9764-e4efc8c4b897 | -8.2266 | -44.17317 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 486bbe51-35d5-3d6e-93ea-da8edfb459e5 | -7.79971 | -46.02401 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a40b2e6-60a9-3775-890c-1946f44f93e4 | -8.93071 | -47.35393 | 2025-10-08 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2709668a-53fb-3ed4-b925-bf2569e04127 | -9.32586 | -60.60165 | 2025-10-08 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e35ae93d-38a9-34ae-8eee-e2927fa5a0b7 | -7.78747 | -44.22316 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67ca846e-e3b4-30a7-a084-a50197830420 | -6.25524 | -45.04804 | 2025-10-08 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 448ed74b-9800-35d2-9192-1fd5aca51716 | -11.22536 | -47.76371 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1135f138-b92c-30dd-b4af-786649c9e6fe | -8.22328 | -44.19598 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6efcafc8-1352-310b-88fe-568d46462316 | -7.79077 | -44.20066 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae9f49b3-9a53-389a-94d1-15621f99c975 | -6.22161 | -44.30412 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eab0fa13-8c5a-3de2-a764-dccd4e555df2 | -10.67937 | -47.54803 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ac65449-79f5-3b5e-86e7-1911a1cd8f3c | -7.24651 | -44.11571 | 2025-10-08 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ca033b4-a686-3062-9fc2-6f92a04fffe1 | -10.37351 | -48.13263 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d9200d5-4cfc-374c-b659-c66edb3dd03c | -5.71667 | -44.66006 | 2025-10-08 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87086700-77b3-3adc-bb07-8a543b9b9396 | -8.5224 | -46.23621 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26bad4c5-00b7-3d31-b4ff-d078c01f0ccd | -5.16779 | -46.23243 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3952bdaa-b384-306b-bdce-0ce69aa42725 | -10.38672 | -48.1338 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ac998eb-eafa-3449-8d18-a1661aa991f6 | -5.31593 | -43.08679 | 2025-10-08 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e0639d78-3dfd-32e8-9c11-572e39c0afc2 | -4.69708 | -44.96818 | 2025-10-08 04:38:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db98a656-da42-3959-af29-2a45e561c263 | -10.4337 | -51.63749 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dac57dc-f5ab-3daf-9a12-f09c152d79a1 | -8.40564 | -49.74213 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c81bff8-8666-3743-92e8-e00ea38e6141 | -8.2552 | -50.092 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1401aad1-e6da-373a-a0c7-17393951d29b | -8.86546 | -46.77283 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 219a6d8c-fe07-3733-8205-474192a08c68 | -4.13205 | -47.65152 | 2025-10-08 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca5e3989-bc08-36a3-8510-af35d2d75a0b | -6.75745 | -43.76802 | 2025-10-08 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a941ffb-e476-369a-901d-ca3e2138ad79 | -5.50968 | -45.9192 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f98e7414-406e-3d73-a74b-eed86d732d58 | -8.92282 | -46.5845 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 39d2cc3d-d408-33f9-88f7-5d9fd1be5aac | -9.61851 | -54.32116 | 2025-10-08 04:38:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e32d6aa9-b831-3806-8788-45e01204738f | -5.77617 | -45.7429 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01f35ffc-a41a-39be-be8a-9920a97ee8df | -10.90966 | -47.13914 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c122df4-a3f1-3e95-a324-172dc9be015c | -9.67006 | -49.95172 | 2025-10-08 04:38:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 34e33c38-173b-3c6c-9883-8adda3f1ac19 | -4.7044 | -50.8627 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82f14490-a376-3dd4-b448-211a7fafc483 | -4.33488 | -46.54955 | 2025-10-08 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63b2bf12-f4ec-33a6-8cbf-f987c84a54da | -11.72153 | -44.29954 | 2025-10-08 04:38:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6899b9f5-431c-39dd-b704-b20945dbffee | -4.62416 | -47.41717 | 2025-10-08 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ddea6921-a893-3cc9-bcd4-b07fe8f1b9f9 | -9.68803 | -45.68303 | 2025-10-08 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a381e230-c97a-34a6-acfa-e593b9c55617 | -4.87046 | -46.82711 | 2025-10-08 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b12691d7-f4cb-39c9-a498-7318b7d9ed24 | -6.70312 | -58.80829 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb09231f-9370-39ba-876c-d10135e66b24 | -7.43631 | -43.14481 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 68a5f1d4-476b-377e-ad24-4f3eaf8bc443 | -6.32134 | -41.60952 | 2025-10-08 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 931af6dd-f19f-3efe-8524-1de5961ce5b4 | -6.69648 | -58.81423 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eb7ca85-3b59-374e-aad3-c7a8e818110b | -7.96626 | -47.71207 | 2025-10-08 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b05bec9f-5efa-30ab-9fba-f02d2a742303 | -4.87104 | -46.82335 | 2025-10-08 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 951bf8d3-9c39-3562-91d9-318601239de9 | -9.78891 | -47.74489 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03146e93-7913-3649-b068-cf8122c36eb1 | -5.71012 | -45.68658 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc3eebe0-5086-3459-a115-709cd9972be0 | -7.2631 | -44.1174 | 2025-10-08 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c6aa340-1d12-365d-8ece-248f4cff61c3 | -9.17451 | -47.82193 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e59520b-a74d-3c94-9a28-73be7cd52f4a | -8.17609 | -50.16157 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bc03753-829d-33bc-ac78-6817d5c87f75 | -6.13003 | -44.60139 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76ff156f-b2d2-39a9-bc9d-af24a098bcde | -10.36228 | -46.36423 | 2025-10-08 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9c7967d-e945-3a8f-80a2-4e86d4fa4e8e | -8.52304 | -46.23186 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ac11016-01b4-336f-b095-a12d99006ebc | -7.79409 | -42.62227 | 2025-10-08 04:38:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c265186e-0265-35aa-9db9-e077a134e687 | -10.04565 | -48.28596 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4073ff18-7a90-36a0-8c9b-1639428e9f5a | -7.44313 | -43.12825 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6c9ac1e6-ec20-3ccb-aef6-840b4289f2f4 | -6.00415 | -43.75111 | 2025-10-08 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README71.md)
