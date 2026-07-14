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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f2ce8d8-8f24-3e62-bba5-0a409fe9915e | -16.89019 | -49.0731 | 2026-07-14 05:01:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20255538-f407-33ff-87de-6f3ae4ad45cb | -21.14926 | -50.46641 | 2026-07-14 05:01:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46552c20-9a56-311f-b451-c1490a3120af | -20.14926 | -56.3414 | 2026-07-14 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c175fcf8-2b3a-3c57-a766-c033546b1c6e | -18.16942 | -46.91132 | 2026-07-14 05:01:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ce419e7-f1e0-3266-8cf7-f194ebb65900 | -15.92436 | -58.00164 | 2026-07-14 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| eba05daa-f357-3f83-bb9f-56bf9a927e02 | -18.78275 | -52.40662 | 2026-07-14 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d900d437-4eb6-35f0-b94f-20f1a4a9e08a | -18.17927 | -46.92393 | 2026-07-14 05:01:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40f2a663-bb47-320f-9e36-dc232c24c0a6 | -18.77888 | -52.40599 | 2026-07-14 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bf5eec3a-921c-3003-82fc-bc767d0cb625 | -18.78187 | -52.40503 | 2026-07-14 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d9555a63-38a5-33c9-9584-f78ac2b1886c | -19.7166 | -50.21015 | 2026-07-14 05:01:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7510f45b-ffd2-3644-89c6-f5b7cba1ff25 | -18.16905 | -46.91496 | 2026-07-14 05:01:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d1b8e9f1-9244-3568-81da-1afd19d69388 | -21.27726 | -56.03614 | 2026-07-14 05:01:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef3b9dc7-2b53-3d8c-b546-6d76667197a7 | -21.27783 | -56.03229 | 2026-07-14 05:01:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3b3edda-731f-3237-9b7c-982c2eddf67f | -18.16395 | -46.91026 | 2026-07-14 05:01:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfe71cd2-13c8-3151-8d87-37b0ec307f5c | -18.1738 | -46.923 | 2026-07-14 05:01:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9cf4d9c-e35d-3209-b72e-def20c6fa205 | -16.41745 | -54.64694 | 2026-07-14 05:01:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68bf8989-2530-368c-af76-237d0b0bb704 | -16.67477 | -56.48241 | 2026-07-14 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 193c52cf-194e-396c-8a04-f2a796d73e5a | -20.65427 | -48.67643 | 2026-07-14 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2cf0ed0f-3404-317c-beca-5127c83d6d22 | -20.70543 | -50.51794 | 2026-07-14 05:01:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aefc6125-760c-34d4-9a46-485323200ba5 | -18.17891 | -46.92752 | 2026-07-14 05:01:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 877e378f-793b-3721-816e-98a81fa55c87 | -23.79672 | -48.44745 | 2026-07-14 05:01:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1ebf7573-46ca-32d9-9fa9-aa458d276efe | -22.79258 | -49.35411 | 2026-07-14 05:01:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 416c1e05-181d-3345-a648-ce4b2053ad7d | -18.17853 | -46.93118 | 2026-07-14 05:01:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a75e8b51-6d77-328b-8208-d4f7de256f5a | -18.78663 | -52.40724 | 2026-07-14 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0634bb45-a827-3ce0-b8e2-4669b8c00a81 | -16.12484 | -59.21185 | 2026-07-14 05:01:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 935fbc75-27a5-3dbf-8dac-5685834f90eb | -18.78119 | -52.41017 | 2026-07-14 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 506227f2-5259-3a12-8bae-abafd99d641b | -20.65394 | -48.67964 | 2026-07-14 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e0eac9a4-5a04-3504-bfb3-a45f4422ad4b | -18.78728 | -52.4021 | 2026-07-14 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5da8744-55ec-38dd-8fff-a125650bd524 | -20.08072 | -57.12466 | 2026-07-14 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96aaa423-6aaf-31f0-a542-1587c72236ea | -22.79184 | -49.35431 | 2026-07-14 05:01:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9c2a834-d2fb-3b2f-b44e-e909feaa2ae7 | -18.78341 | -52.40146 | 2026-07-14 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 441ac77f-db76-3c83-8774-3bb96c13a82d | -16.41815 | -54.64677 | 2026-07-14 05:01:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29d51b92-31e4-30be-8913-6b82d9739f58 | -28.6269 | -56.00519 | 2026-07-14 05:04:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 3ca02765-b6e6-3197-b975-348e494024eb | -29.66001 | -52.6659 | 2026-07-14 05:04:00 | NOAA-21 | VALE DO SOL | RIO GRANDE DO SUL | Brasil | 4322533 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 73b0ea89-0f10-3ebc-bd34-8d74a1bac9fe | -10.0731 | -50.1104 | 2026-07-14 05:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 48ecb50a-cf22-31a6-b389-0dd5d4936040 | -10.0731 | -50.1104 | 2026-07-14 05:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 60159e25-d687-3093-a55f-66fa5091c10a | -10.0731 | -50.1104 | 2026-07-14 05:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 168465c5-0a88-30ab-945f-c834d36f7710 | -10.0542 | -50.1123 | 2026-07-14 05:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9211549d-ba61-3933-84d2-7c189c17e9a2 | -10.0731 | -50.1104 | 2026-07-14 05:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 8b328d6b-e72e-3421-8b84-89d9c2405508 | -10.0731 | -50.1104 | 2026-07-14 05:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 38945213-250d-3963-b4aa-e4405a467839 | -9.86326 | -57.80523 | 2026-07-14 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18f08254-5b70-39eb-8d98-2774c255b37b | -11.27023 | -55.78891 | 2026-07-14 05:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6141074-704e-30b1-ad97-327f92862334 | -12.87932 | -58.27428 | 2026-07-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df0ac9c8-0ce5-31f0-bbdb-7b633bdf18db | -12.87791 | -58.28601 | 2026-07-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6ff805c-4651-3c61-896d-073b4eb8fb0e | -12.87317 | -58.27744 | 2026-07-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e1c664c-6bf9-3b61-b21a-6a300a19204b | -12.87364 | -58.27353 | 2026-07-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 799677d6-59be-3740-a22e-1a1bf0c89514 | -12.8727 | -58.28133 | 2026-07-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15f87a12-f754-3977-9a52-05d3fa44893d | -11.27607 | -55.79535 | 2026-07-14 05:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a5df9f5-25ee-306c-8959-f418a0d853ef | -12.87224 | -58.28518 | 2026-07-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f376ae12-26d4-3bdc-b4a6-960193d4b428 | -9.55062 | -65.68018 | 2026-07-14 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0d63adc-10b6-3687-b4e9-63e8536d5d4c | -9.6701 | -67.22209 | 2026-07-14 05:53:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf4674bd-9753-36c6-972c-d25bc18c0210 | -6.48663 | -42.22215 | 2026-07-14 05:55:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 5cdda2dd-fba2-3536-955e-48b2e2cfabd9 | -8.60624 | -63.45692 | 2026-07-14 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acee6170-7e87-3df1-a8ac-7adea295b58b | -10.0542 | -50.1123 | 2026-07-14 06:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 8a7dce32-211f-330b-b6d1-3e4aa66d0134 | -10.0731 | -50.1104 | 2026-07-14 06:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| cd1ce524-20db-36da-8528-aaa6fad38db6 | -10.0731 | -50.1104 | 2026-07-14 06:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| ddb7ff62-add5-3ffa-8b43-060abf7faed3 | -10.0731 | -50.1104 | 2026-07-14 06:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 0ee77166-653a-3855-bce9-b9679c7fb3c7 | -10.0731 | -50.1104 | 2026-07-14 06:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| dd6f304c-d579-324d-ab55-f655c97be3a5 | -10.0731 | -50.1104 | 2026-07-14 06:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 490ad349-3e76-37a6-a251-484f3cfd0d5d | -10.0542 | -50.1123 | 2026-07-14 06:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 96c076f0-2bcf-34f6-aa07-dc4439e81f71 | -10.0731 | -50.1104 | 2026-07-14 06:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 064522c3-24f3-314b-8320-da735011bdfa | -10.0731 | -50.1104 | 2026-07-14 07:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ad75a8e8-c642-32b9-9d15-b56268065f94 | -10.0731 | -50.1104 | 2026-07-14 07:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d11da4af-eb8f-3872-89df-b2356b4481a4 | -10.0731 | -50.1104 | 2026-07-14 07:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3f333521-ee26-3ba1-9720-e0105f614e31 | -10.0731 | -50.1104 | 2026-07-14 07:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| bd684562-0648-3e45-89ca-b6f34f09a253 | -10.0731 | -50.1104 | 2026-07-14 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 55f135bc-4d4f-37bc-961c-042666300ab7 | -2.96222 | -48.99194 | 2026-07-14 12:02:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| ea661fae-ad1f-343a-b4f0-41d975ac4b1f | -3.68758 | -49.41612 | 2026-07-14 12:02:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 760a0989-a008-388d-bcd8-3fde69fc6ee8 | -2.96348 | -48.98314 | 2026-07-14 12:02:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6d40e2fd-49ca-31ef-b1cb-f5249411e2ae | -10.06402 | -50.12008 | 2026-07-14 12:04:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 3ba93a42-3c94-3f7f-a43d-2e1d0e6804bc | -12.45944 | -46.51669 | 2026-07-14 12:04:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6481003e-7819-3a46-9616-28796deeaad0 | -10.06529 | -50.11101 | 2026-07-14 12:04:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f1432ee0-f6c6-37e8-8754-7f2eedb0015e | -11.2661 | -50.6244 | 2026-07-14 12:04:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7374ba4a-0c5c-3b5e-a07f-afca81eb22da | -9.51627 | -47.14016 | 2026-07-14 12:04:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c7619a82-2af7-3784-bd47-76c1bfab5050 | -10.05386 | -50.1279 | 2026-07-14 12:04:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 72181b25-6597-3c09-a8c7-dd88700ee65a | -15.5791 | -47.40014 | 2026-07-14 12:04:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 44.5 |
| b73a148b-5cd4-3c11-b01e-03900f5d3285 | -12.42508 | -48.72504 | 2026-07-14 12:04:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 16875790-7691-3753-a4c9-0404731d933b | -10.80951 | -48.57285 | 2026-07-14 12:04:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e878b534-4ca6-3aa2-b99c-6a75b6a5dec6 | -15.57729 | -47.41506 | 2026-07-14 12:04:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.7 |
| abe144ee-cce1-37eb-be1a-e8f5fdf2f633 | -8.27486 | -48.18715 | 2026-07-14 12:04:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d31e8e95-5144-3750-9ade-86473006e1f7 | -11.6386 | -45.19358 | 2026-07-14 12:04:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 56164a21-24bb-3b1f-9538-52912c4109b4 | -12.44248 | -49.57677 | 2026-07-14 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4f378987-4899-3712-85f8-c6db1b7d5b7c | -11.55242 | -52.79102 | 2026-07-14 12:04:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 68464b0d-97d3-3abd-8f6d-463f3b30b113 | -15.69031 | -43.27692 | 2026-07-14 12:04:00 | TERRA_M-T | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 34.2 |
| a8df8692-9b63-3c37-af3e-2e99ca46a066 | -10.05513 | -50.11884 | 2026-07-14 12:04:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b8f3babf-4b4a-304d-a244-abd47b7a96f9 | -10.52967 | -50.15147 | 2026-07-14 12:04:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bed05c79-57aa-31cd-8e9f-421b166aa134 | -8.73039 | -47.82918 | 2026-07-14 12:04:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 53d0ae20-93d9-3f17-a459-4a0e80628607 | -9.14289 | -47.79631 | 2026-07-14 12:04:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1e9622e3-f802-3784-99e2-0c01cf1f18db | -15.68666 | -43.28296 | 2026-07-14 12:04:00 | TERRA_M-T | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 43.8 |
| 2c1cb957-1062-3029-b87d-2c1a5d9c5ca5 | -16.33642 | -43.60468 | 2026-07-14 12:06:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 3013d5ff-9473-3de4-b278-8f8a513df7c4 | -18.77737 | -52.40826 | 2026-07-14 12:06:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f575b1ff-afb3-3f6d-93b9-0425d1d2e3ef | -17.11778 | -49.98895 | 2026-07-14 12:06:00 | TERRA_M-T | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| fb78fffe-493c-3824-9759-8c52e8238169 | -17.11636 | -49.99969 | 2026-07-14 12:06:00 | TERRA_M-T | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 27b79c35-774f-3c3f-aab7-a7852043c8aa | -18.78621 | -52.40961 | 2026-07-14 12:06:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7bb37046-0979-30ac-9301-22a11bc7ab5c | -18.78751 | -52.40029 | 2026-07-14 12:06:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 109f51de-690e-395b-95da-01bc06d93517 | -18.15914 | -46.90766 | 2026-07-14 12:06:00 | TERRA_M-T | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 5e4954f3-8b52-3b9e-aa69-c1c14d7847bb | -18.16916 | -46.92726 | 2026-07-14 12:06:00 | TERRA_M-T | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 0ed7567d-2916-3367-b0a3-b44ba131a926 | -16.33451 | -43.6099 | 2026-07-14 12:06:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| ed466d76-5ecb-380c-b373-7889cffa7e45 | -17.58826 | -46.51798 | 2026-07-14 12:06:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 7dd36134-c28e-3308-8460-d275abdabdc9 | -18.15717 | -46.92567 | 2026-07-14 12:06:00 | TERRA_M-T | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 25.6 |


[Clique aqui para ver as próximas entradas](README8.md)
