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
| 116f49ba-804d-3d35-a6c0-7231ba058f03 | 1.77041 | -60.231 | 2026-07-19 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 813ac0e3-0fa4-385f-9d16-ba0574512895 | 0.96796 | -60.40911 | 2026-07-19 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5393a243-77d7-394f-8998-0e8b41bc4516 | 1.76602 | -60.23162 | 2026-07-19 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db2ec858-10f9-31e2-9212-cd3034b0655c | 0.75376 | -60.45289 | 2026-07-19 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 355616be-8839-371f-8635-c3d13d12a4df | -4.03729 | -49.24401 | 2026-07-19 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6224c124-ef47-37d3-8182-6c29a1cae4bf | -8.94434 | -47.61078 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 98f69239-adb0-3662-83c0-ec56396e899c | -8.36159 | -45.39563 | 2026-07-19 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2c3d5c03-1e29-326a-b0c8-91f65174a096 | -8.36762 | -45.39577 | 2026-07-19 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f63b566-806b-3126-90c7-17914c996afe | -6.13084 | -55.80556 | 2026-07-19 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b253a0d-b430-3bb3-927b-fbe05e306cfa | -8.94476 | -47.60768 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6196613a-2b6d-38f6-a836-8413600f8ede | -8.36472 | -45.39864 | 2026-07-19 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 99f5379f-4e98-38c0-b7d5-3d9a4c736841 | -4.01624 | -48.95876 | 2026-07-19 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73901c84-755c-3fd9-8bbc-1cc9ebd043f5 | -8.93442 | -47.6062 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 875342a8-6e70-34c6-b22a-5362211690be | -6.73831 | -44.36839 | 2026-07-19 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 455545ef-f821-34cd-b14c-51eb48ab9732 | -8.36711 | -45.39969 | 2026-07-19 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99571370-3008-379a-b06f-ddd418def7a7 | -8.94518 | -47.60459 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 18efa8a2-5d53-3772-a0f0-9edb51fcdad7 | -7.69285 | -55.36404 | 2026-07-19 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 916cfb2c-4215-35e7-959b-8380b01933d7 | -6.1442 | -55.81126 | 2026-07-19 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b7af625-fdc7-30d5-94e6-f7443c71a0bf | -1.58934 | -50.43843 | 2026-07-19 05:04:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 608d01f1-4b8e-3b3a-9995-f30bfaf3a3ac | -8.94637 | -47.60772 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8611108-3718-3615-8d0b-80bb2dda496e | -2.77653 | -49.45987 | 2026-07-19 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 652361ef-4ad8-3520-8d8b-55f3cda5d9d0 | -4.14474 | -49.27891 | 2026-07-19 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 786e5f4f-1cf4-3975-af03-da04763cfcbb | -6.1303 | -55.80901 | 2026-07-19 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d361fe54-2a78-30a3-92a2-d8a152045bf1 | -5.71184 | -45.66394 | 2026-07-19 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 995259cb-c940-3927-8250-fc788f4c4b42 | -4.09002 | -47.31329 | 2026-07-19 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2128a660-3b8e-3c44-98bd-0ad690dea20d | -8.72934 | -47.83119 | 2026-07-19 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f0adf81-c648-3694-bdf1-0fbb5ac14649 | -8.62274 | -50.0243 | 2026-07-19 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 948df9fb-e37f-3ef9-a603-5f4c5add5def | -3.97141 | -47.20364 | 2026-07-19 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40c140b2-f206-3546-bbb6-7d1724355101 | -4.58503 | -46.29877 | 2026-07-19 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea7a2dc0-eb47-3bf0-a67a-d697a52711c7 | -6.89039 | -59.01251 | 2026-07-19 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9532a44f-aa14-3ab2-9e35-a42f95ff649b | -2.8007 | -49.52497 | 2026-07-19 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a2d511bd-7e55-3066-b284-8cc84f9fddfb | -4.03668 | -49.24812 | 2026-07-19 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbabb97e-fd2b-3faf-a16c-2bea2800b029 | -7.68954 | -55.36353 | 2026-07-19 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10c207c9-264a-34a6-948c-9c4ebd367527 | -3.07823 | -52.90429 | 2026-07-19 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f698c34e-7991-35b8-b834-70844e74ec30 | -8.94951 | -47.61152 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d81f1a9-8b1d-3c74-b0ee-985765957db9 | -5.9367 | -43.64631 | 2026-07-19 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 933b7702-eef1-3391-855f-9756fb6a5e3b | -8.94199 | -47.60072 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b9662c5b-52dc-3fd9-80f0-cccd6c443892 | -7.69008 | -55.36004 | 2026-07-19 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9985e979-feab-3476-b3d3-7fdbab0248b6 | -8.36111 | -45.3993 | 2026-07-19 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8e960f4c-8906-3431-98c5-d435ebf2f05e | -4.03976 | -49.25695 | 2026-07-19 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4561925-3278-3133-bc2b-2de88e0a187b | -7.11791 | -44.047 | 2026-07-19 05:04:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b43a47a1-8135-3b37-97dd-78f797be5d93 | -7.11859 | -44.04178 | 2026-07-19 05:04:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b13e8469-6946-3ba0-b01b-5d4a82820668 | -4.0165 | -48.96099 | 2026-07-19 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7bf55b2-9207-3c8a-95b9-475b9ff1bec8 | -2.7883 | -49.5231 | 2026-07-19 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52d391cd-455c-30e0-bc95-06dfd6da03b5 | -8.93959 | -47.60694 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5a010e09-7d9d-3e83-92fc-cb111ca85ed1 | -8.94001 | -47.60382 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7e6ff75b-c8d0-3cfd-9f3a-262b7dca0ad9 | -4.58457 | -46.30199 | 2026-07-19 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26cd627e-f4c0-3339-bf5b-56ab0daaa749 | -8.62342 | -50.02663 | 2026-07-19 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26188891-440b-371d-b6cf-a9047b8effe1 | -4.65142 | -56.06388 | 2026-07-19 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16daa511-b129-3adf-a796-79c03fe13800 | -8.9416 | -47.60384 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1a570f43-951d-38e9-9059-685bc88ebf7c | -6.89399 | -59.01311 | 2026-07-19 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9184e26-0916-3b9b-9694-f1a4a188a4e8 | -6.73208 | -44.36766 | 2026-07-19 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7608eaab-db52-358c-bd2e-e069cd57e2a4 | -2.83134 | -48.86556 | 2026-07-19 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9a44d89-a8bb-3918-b1c9-b76e0332cca5 | -5.9303 | -43.64529 | 2026-07-19 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7df60b38-a52c-3855-b8e8-723d6b9818a3 | -2.78068 | -49.46051 | 2026-07-19 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d6c259e-ea16-3dcc-ab26-7752cdf08328 | -6.1336 | -55.80952 | 2026-07-19 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 562113ab-da0d-333f-9204-6abb7cf471d4 | -8.36521 | -45.39475 | 2026-07-19 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 77f635d9-551c-3a6a-8423-84f6634d0333 | -8.94597 | -47.61082 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 300de1ae-6568-3e94-b914-15346431287c | -8.94043 | -47.60072 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 68c216a5-17d5-39c8-9b6c-77fd375c633e | -2.82782 | -52.29868 | 2026-07-19 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7546f926-2742-3406-975b-f02c8ce6c109 | -5.9383 | -43.64616 | 2026-07-19 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b982e82-8f2e-3e9d-8a6e-5335184bcc70 | -6.90323 | -45.67107 | 2026-07-19 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08954d60-affa-3358-85da-5891216f5a31 | -8.72974 | -47.82816 | 2026-07-19 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 066ae08f-1c32-35f4-9da3-d668db543e7d | -2.78012 | -49.46428 | 2026-07-19 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ef50747-402d-38fe-8850-6a504731081a | -4.03607 | -49.25225 | 2026-07-19 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 175f8454-6a77-3b37-81fa-223e74bd3939 | -2.79243 | -49.52372 | 2026-07-19 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 299f7c45-b6a2-3d98-a25a-fcb3d3641a96 | -8.9412 | -47.60696 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf281e94-a965-301b-a04a-2c5c300fc10f | -5.93189 | -43.64512 | 2026-07-19 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53eb13d2-80e2-32b6-958c-99220005a039 | -8.92967 | -47.60236 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36d159a4-21f5-3e2a-9401-1ff2c880754d | -8.93484 | -47.60308 | 2026-07-19 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6443c14b-6923-3b44-b8da-1f54fe23f64f | -12.07935 | -53.35214 | 2026-07-19 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 9d34cff2-1e59-339c-a5da-41b4069334eb | -9.0814 | -50.59426 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b75a861-53a1-3b47-9d3a-ed753f9eabee | -10.81769 | -50.23339 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 162329f2-d12a-3434-a784-4f5f413c51e4 | -11.66073 | -49.76354 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f43a848-753b-3a14-a5dd-f836ebdd81ae | -11.74571 | -57.81329 | 2026-07-19 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49b701d5-046e-3764-ba1b-b96b03289d9e | -11.77404 | -45.97253 | 2026-07-19 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 059e9898-ed7f-375f-b9f7-0d59c1f452d4 | -9.10511 | -50.60982 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59edbcad-1c24-3c1e-908f-4000c175cd7e | -14.00938 | -53.99176 | 2026-07-19 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f34bef6-3445-3cd6-829f-2e326b676d47 | -9.09551 | -59.39945 | 2026-07-19 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bd18d1b-4cb9-30b4-a6d0-e398e82c69a5 | -9.95505 | -50.55455 | 2026-07-19 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88cf570b-1214-340c-97a3-fd8fe2fc591c | -9.4979 | -46.67001 | 2026-07-19 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9df86c3-1f8d-3b63-b39e-2d9cf6c9066d | -9.47983 | -57.31758 | 2026-07-19 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec2750e9-b356-3148-b04b-239bd24e96eb | -9.96042 | -48.85894 | 2026-07-19 05:06:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 681f01c9-552b-3e7b-a335-eeeda41e15c2 | -11.97558 | -47.10397 | 2026-07-19 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bab2d47e-8e00-3cd9-9867-4f028ca45484 | -10.72137 | -46.57473 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 122401c2-1fb8-3ead-b156-417480a71941 | -10.91722 | -50.36122 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e55b3870-745f-38b7-92cd-3f754b349f10 | -10.71008 | -46.62014 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79c3075d-5646-3922-b1ac-314cac0e322b | -10.89223 | -50.31305 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce078163-f269-324c-9b4f-d8c6004d2d75 | -13.73574 | -51.87523 | 2026-07-19 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8337a71c-8ed1-39f5-86c4-096615089da3 | -9.09093 | -50.58757 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9915adee-c442-3776-a368-06d30c8ba6d9 | -13.35139 | -54.31392 | 2026-07-19 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2689e5f0-3098-3d4f-972e-f892573b0c8c | -12.66635 | -48.21953 | 2026-07-19 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9614e8db-df7f-3887-b295-144dee1bbfa0 | -10.92484 | -50.37116 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 000cf68f-767c-3cc1-a761-e6a9dc90e143 | -11.9742 | -47.11531 | 2026-07-19 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fd50493-7ad9-36ae-ac01-4dc90a8989f5 | -9.07718 | -50.59365 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d5db5f9-51fc-324d-9e04-1aa5d10e24a3 | -12.01178 | -50.56369 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2959f382-68b8-31de-9e4c-76d422d35b03 | -12.00182 | -50.57121 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdf4680a-ef97-3d98-b35b-8e11d4c73328 | -11.38599 | -47.51256 | 2026-07-19 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6466a70-7b15-3f3f-ab7f-850eea83eefd | -13.67141 | -48.79065 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 05bbc046-f319-353d-8a60-2135b8f7335f | -11.96863 | -47.11457 | 2026-07-19 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README10.md)
