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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ddd00c6-5f2d-3cde-8b0e-1a95d17778ae | -9.9639 | -49.8002 | 2025-05-23 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 091c685e-c35e-3951-adca-36ed2371228c | -11.7796 | -44.2762 | 2025-05-23 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 4837437e-a582-3a39-80f8-c4ce6bb9b9fc | -13.9821 | -55.9947 | 2025-05-23 00:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 1564b53e-ed5d-32e4-8aa9-3fb782240baf | -11.7988 | -44.2733 | 2025-05-23 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| fc03e391-e295-33d9-887a-d493bae02c56 | -13.9818 | -56.0151 | 2025-05-23 00:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 150.5 |
| f9ff2f9d-739a-31f6-ac35-6b7e889156ee | -12.2943 | -52.4995 | 2025-05-23 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ebe6c71e-e6d5-33d1-984b-4026fc9b125a | -21.7206 | -55.3638 | 2025-05-23 00:00:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7c341a82-4bb3-34e3-a508-6349f1a256dd | -12.3324 | -49.9857 | 2025-05-23 00:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d9a76812-fad0-36e8-8b87-d17b6a21fae6 | -9.0291 | -47.7452 | 2025-05-23 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0b8ce8a7-755e-37e4-ab75-0daf0c63508f | -9.048 | -47.7434 | 2025-05-23 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| b81d0dd5-fce8-3cab-a25d-fbb41ba29402 | -20.8593 | -53.7387 | 2025-05-23 00:00:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e78faad3-26d3-3a9c-bab6-f4666cb2cab7 | -7.0695 | -44.9335 | 2025-05-23 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 516c310b-f701-3623-8da7-d6d8c6abab14 | -6.2224 | -43.3693 | 2025-05-23 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 683fb20c-60f6-3e5f-b4bb-f083c6837d3d | -20.8588 | -53.7605 | 2025-05-23 00:00:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f1d0658a-fb8b-3a32-8659-456b7466f7df | -5.576 | -45.203602 | 2025-05-23 00:07:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff2eff8d-9242-309b-9199-c0dba44b40d7 | -7.2074 | -43.132 | 2025-05-23 00:07:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c143876a-ac8b-3cb3-a690-a3c80d442bc5 | -12.2699 | -44.5947 | 2025-05-23 00:07:00 | METOP-B | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6956e2b5-d806-3f1a-86b8-1a9654bdeaad | -15.1372 | -43.966301 | 2025-05-23 00:07:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8dc58a20-f158-36c0-80d3-cfb93fa5dfeb | -6.2233 | -43.381802 | 2025-05-23 00:07:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0be21af-d870-38c6-be22-95bface0a52e | -15.2599 | -51.4603 | 2025-05-23 00:07:00 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 91f8d243-00f4-3e55-a3e1-140fbfef8f90 | -11.7766 | -44.275002 | 2025-05-23 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1576633-d4e9-3fa7-8c40-f42793dda5fb | -11.5541 | -47.4533 | 2025-05-23 00:07:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76ea5ff4-07ce-3952-b848-570ff1a17b20 | -12.2772 | -52.464001 | 2025-05-23 00:07:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 577f1a42-d79d-35f5-b42f-6d3e605def47 | -7.0614 | -44.935699 | 2025-05-23 00:07:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87df39d6-715e-3483-8610-d087435dd613 | -14.047 | -53.344002 | 2025-05-23 00:07:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f746e95-d659-3b10-b447-5d46e4499c88 | -11.7864 | -44.2728 | 2025-05-23 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bba4138a-dbc4-3328-ae39-9fdab81b4863 | -15.4149 | -41.400799 | 2025-05-23 00:07:00 | METOP-B | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c04d3322-2599-3fac-a721-ae528fa8c001 | -11.5077 | -48.544998 | 2025-05-23 00:07:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d345a350-e7eb-3102-b7d1-7d8b0bf61c22 | -14.0411 | -53.366199 | 2025-05-23 00:07:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b2a3ab9-90f1-3aa2-bac6-a822f22e2912 | -6.9341 | -42.796101 | 2025-05-23 00:07:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a512319e-ebb4-3242-a029-352e0dc7b2b2 | -12.3947 | -49.979301 | 2025-05-23 00:07:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6cb7fa7-d691-3a3d-9afe-55f632150d91 | -9.962 | -49.808701 | 2025-05-23 00:07:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 264a8036-b75b-3190-b828-65cff9ce67ce | -11.7797 | -44.289001 | 2025-05-23 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47b72881-a504-310c-9eef-13a24d17effa | -11.7781 | -44.282001 | 2025-05-23 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cdf66acc-a7ea-38fc-b76c-871cda7d3ff7 | -6.2198 | -43.366299 | 2025-05-23 00:07:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b802ca1-97e3-33e6-aac5-df8a773119eb | -12.3337 | -49.98 | 2025-05-23 00:07:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 269ed66d-6a81-3c25-8e0d-5bcbb1922397 | -6.2162 | -43.350899 | 2025-05-23 00:07:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46fcae48-d7b0-39d8-8f6c-7610c6a139e2 | -9.0389 | -47.733002 | 2025-05-23 00:07:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2862b147-ab28-3a7d-bee4-a9a341c37e6c | -13.0892 | -52.270199 | 2025-05-23 00:07:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5345b653-22fd-3dc5-bcba-fc5b3767c1ef | -8.1186 | -46.4403 | 2025-05-23 00:07:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4407f48-71eb-3f25-b069-b83842b9aeab | -10.7041 | -48.811401 | 2025-05-23 00:07:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8656f0c3-b332-3d43-bc79-e4787e2a7026 | -10.6561 | -49.461899 | 2025-05-23 00:07:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd052fd2-19a9-356e-8b7d-7687624779b1 | -12.3314 | -49.968601 | 2025-05-23 00:07:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8a0d0c6-05bd-324b-98a9-b60b3308a2dd | -6.218 | -43.358601 | 2025-05-23 00:07:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 635e5411-5757-380b-8327-b25d5ec5167c | -7.9737 | -46.949001 | 2025-05-23 00:07:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 634c7443-77c0-355a-88c5-6678ebc8b8e9 | -6.9439 | -42.7938 | 2025-05-23 00:07:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6381cdc8-2ec5-3cd8-9aa6-ea7fd1283357 | -20.848499 | -53.706699 | 2025-05-23 00:07:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bac6fb65-675d-3b3e-9430-4703afdc865f | -12.2934 | -52.495499 | 2025-05-23 00:07:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5451b27-2b27-3d6b-b712-0ba78f5cdbc9 | -5.5729 | -45.189701 | 2025-05-23 00:07:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36487e83-8f42-30b5-8aab-27d75a10806e | -6.2278 | -43.3564 | 2025-05-23 00:07:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f07d1c5-b80d-36bf-bc41-3f541757b083 | -11.9362 | -43.929501 | 2025-05-23 00:07:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1543f45a-119b-3804-a2f2-2b5fe9292602 | -7.1976 | -43.134201 | 2025-05-23 00:07:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e67cdc81-87c0-3118-9989-2de3a54fccca | -9.9522 | -49.810699 | 2025-05-23 00:07:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fdb3cf7c-1baa-3622-af2f-d5aabecbb416 | -5.5745 | -45.196701 | 2025-05-23 00:07:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8aef9324-c455-315a-a4b3-3547f222b74c | -7.7096 | -45.665501 | 2025-05-23 00:07:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97bf9f15-146b-333e-9655-8771d5bf208c | -12.4142 | -49.975201 | 2025-05-23 00:07:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 086f26cf-73bf-3517-a91c-60b890787bcc | -11.9652 | -44.1511 | 2025-05-23 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 378b8ab1-989f-32cf-8a7e-2093621dc57d | -8.1217 | -46.4543 | 2025-05-23 00:07:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50ba1080-5a38-3173-8cd9-934e2b5086cd | -20.852699 | -53.734001 | 2025-05-23 00:07:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0693ceca-c948-3cd4-b1ff-f94f63022707 | -15.4167 | -41.4086 | 2025-05-23 00:07:00 | METOP-B | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0631f9d8-df63-3573-8768-59f6ffd9237a | -7.063 | -44.942699 | 2025-05-23 00:07:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b52cc498-b39e-39fe-8775-2092e8a2badb | -11.7879 | -44.2798 | 2025-05-23 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f1df813-001d-3880-8de8-8f7717d43667 | -12.0638 | -47.342999 | 2025-05-23 00:07:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a44fcef-0b80-3504-865f-f99c83c148b9 | -8.6745 | -48.279099 | 2025-05-23 00:07:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d65ea016-16c7-3bfe-adc4-a1293635dca6 | -10.6386 | -49.476101 | 2025-05-23 00:07:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 488c8a99-67af-3ff4-bd21-165d941bf867 | -12.3141 | -49.984001 | 2025-05-23 00:07:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ac4472a-636c-3bc0-b53e-a4ef62310b10 | -9.9577 | -49.7882 | 2025-05-23 00:07:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 844ea957-92d9-39c3-a5e0-29d33580a504 | -12.2869 | -52.462101 | 2025-05-23 00:07:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be02c561-5ccf-391d-b34d-14a87ff072c5 | -9.021 | -47.745098 | 2025-05-23 00:07:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b146924-250c-3cc1-a284-8feb5d51d291 | -12.3924 | -49.967899 | 2025-05-23 00:07:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fb63ee1-9c8f-3aea-a50b-3c6bc37260b7 | -6.2216 | -43.374001 | 2025-05-23 00:07:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6442b879-cc2c-3e2e-b98d-f60624ac2943 | -7.7065 | -45.651798 | 2025-05-23 00:07:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0199a7ad-5940-3bae-bf84-96b8266ebda1 | -12.2714 | -44.601601 | 2025-05-23 00:07:00 | METOP-B | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2342fe04-448d-3d86-acdc-5537da1d41f8 | -12.3216 | -49.9706 | 2025-05-23 00:07:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0978d66e-8133-3524-935b-00a777663aef | -12.0736 | -47.340801 | 2025-05-23 00:07:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 091f3d0d-6f25-33f4-8304-dcabda98d7a6 | -9.0226 | -47.752899 | 2025-05-23 00:07:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c54c5ab9-3b51-3878-82fe-10514ed3d20d | -7.2057 | -43.124199 | 2025-05-23 00:07:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2f4c816e-0f3c-3f90-b34b-275e668b6842 | -9.9599 | -49.798401 | 2025-05-23 00:07:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1532bc9-850f-3f19-928d-96d071656b5e | -11.7895 | -44.2868 | 2025-05-23 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0ea1fd2-4d21-358c-980a-1b7cbc6e4f8d | -9.0193 | -47.737301 | 2025-05-23 00:07:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ce74d1e-0dfc-3994-bc0f-8cacc8bcaafa | -12.2805 | -52.480701 | 2025-05-23 00:07:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61ab94fc-6c6c-365a-b7d6-36652e7926fb | -6.6897 | -44.159801 | 2025-05-23 00:07:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6059a36e-e01e-3c9e-a8c5-d0580c272259 | -11.5096 | -48.554199 | 2025-05-23 00:07:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0933e03-68d5-3dbf-aa99-ca4504bf107d | -9.0406 | -47.740799 | 2025-05-23 00:07:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df7a99c2-013c-33a3-a113-e9a0de0133db | -7.2332 | -43.109699 | 2025-05-23 00:07:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d76d9f6d-075f-3fed-ad5a-b7783ba4d78b | -12.8421 | -47.388699 | 2025-05-23 00:07:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89a64e2f-ae8e-3778-baa6-f3e4291785d9 | -10.4867 | -42.410599 | 2025-05-23 00:07:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b0d1182f-1e39-3b6d-b90e-14bf1ea7ec02 | -12.8519 | -47.3866 | 2025-05-23 00:07:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7af5abc2-74b5-32d1-adb1-1dce18f6583f | -11.9264 | -43.931801 | 2025-05-23 00:07:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79d0f0b1-66f1-3032-9024-c5d880149781 | -9.9501 | -49.800499 | 2025-05-23 00:07:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26e80412-685b-3dea-bedf-95557c15eab3 | -12.3239 | -49.981998 | 2025-05-23 00:07:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53020f73-4816-3ac6-bb20-dde04e722538 | -10.7158 | -48.818501 | 2025-05-23 00:07:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3d0a0fa-5bd5-3a91-818c-379b559d57a0 | -10.6484 | -49.473999 | 2025-05-23 00:07:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9eed7b77-3660-378c-a855-850ca464ef52 | -13.9652 | -55.9529 | 2025-05-23 00:07:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a5d0c82-d0ec-3b0f-b0ce-425d3080503f | -20.8389 | -53.708302 | 2025-05-23 00:07:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2218220a-267b-3a17-a1d8-0e95d1a6a24c | -7.0583 | -44.921902 | 2025-05-23 00:07:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 389187aa-ca82-3877-8999-13b2aad7e755 | -10.6582 | -49.471901 | 2025-05-23 00:07:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04e4a795-535e-3b96-a49e-307c1cbba60e | -6.226 | -43.348701 | 2025-05-23 00:07:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b8591c9-b03f-33f8-8432-8f8e432aaef0 | -5.7713 | -43.613701 | 2025-05-23 00:07:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 156d6958-bbd7-352a-a965-59fea59c3139 | -12.4119 | -49.963799 | 2025-05-23 00:07:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
