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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08951635-6352-35d9-8037-7b6cc5e29142 | -12.8097 | -48.42287 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d1135ae3-6495-3044-b69f-a0d5c4052298 | -12.78765 | -48.40251 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 057c7e59-d9df-349e-884b-953842df6a48 | -15.14896 | -43.79631 | 2026-08-21 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2856473-c8a9-3ff8-bf1c-34ff1a9f8457 | -13.43547 | -51.80754 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ffa448f-42ef-37d6-b4a1-8c75ab17aef8 | -12.83018 | -48.45065 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 153150e6-b45e-37cd-82d1-2f9723ee9308 | -13.25671 | -51.62922 | 2026-08-21 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e0aeeaad-0059-36ee-ac82-caab2e8baccb | -11.99803 | -53.42907 | 2026-08-21 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01b3324e-652a-3e30-8184-6e12407a1c80 | -14.44919 | -45.62144 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f99dc68c-064c-386e-8549-10492d4d6ab3 | -7.77786 | -46.0448 | 2026-08-21 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de674b6d-aad4-383d-98be-ee241275038b | -12.83853 | -48.43422 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19d763ef-9413-38ba-9429-d5cd28315d03 | -8.44678 | -46.96193 | 2026-08-21 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d88a05e9-e194-328a-8603-2fbf40bdf5c7 | -14.46126 | -45.62383 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee073c33-84da-335f-85bd-0b8d8049a25f | -12.75434 | -48.46903 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4dc55e0-4e28-3c02-955a-41afd609cd1f | -14.44986 | -45.61781 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e97a4465-2057-3593-93d8-1982eb0421a0 | -8.16379 | -46.73015 | 2026-08-21 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 673bb31c-a311-390a-9c19-8438e4345c9d | -9.05666 | -50.88916 | 2026-08-21 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b7ec584-13d7-34a5-9ff9-ac8b93dd2670 | -10.30779 | -50.37982 | 2026-08-21 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fbc16df-be62-342e-9d98-adc8371b2bf0 | -12.26538 | -43.16905 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| bf56049e-95f6-3383-8f25-219108bfc1d5 | -9.80024 | -46.64472 | 2026-08-21 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 781ff5e2-d706-3ff5-9795-0619aeb91f65 | -8.6856 | -47.49215 | 2026-08-21 04:02:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 965735b2-6251-3ff3-983f-0000e7cb02cd | -12.84366 | -48.43441 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49d43cf3-aede-3921-99cd-9917ea629aa3 | -13.38073 | -54.38976 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 70a6161d-e4db-3aee-a4a2-a323337a8408 | -13.39092 | -54.37699 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7d6890e6-6e91-33eb-bb71-c66d0be201df | -12.85952 | -48.43254 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a0ecd24-56d1-390f-94d0-046908702dd1 | -13.4384 | -51.79361 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44ac9c80-1f39-3a83-bf2f-5b10656450c2 | -8.0892 | -51.6635 | 2026-08-21 04:02:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d9b5160-89b9-37b3-8b56-83b0db82e227 | -12.25309 | -43.1755 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a10bf1a0-c177-32ac-b3ee-7b5b0432c069 | -9.594 | -41.80133 | 2026-08-21 04:02:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 91e05b93-a12c-3594-a0dc-df1b70a1dec3 | -9.01013 | -40.99739 | 2026-08-21 04:02:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fb943937-4ffb-3e39-a2f9-e9d1929ae403 | -14.45454 | -45.61495 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c2abe11c-f110-3ba5-9345-32b1f5ae1e23 | -10.77841 | -50.30352 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9bdc347-8e75-3127-9c73-e5ecf360426b | -12.80565 | -48.41711 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 68a0f3cd-e4bf-378a-81c9-8cc1554b9335 | -14.72494 | -47.14174 | 2026-08-21 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcad0fe4-d52d-348e-b388-947e058926bc | -10.74895 | -47.90693 | 2026-08-21 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae98f010-c007-3a06-966f-4a10c8fe018f | -12.8567 | -48.42031 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df2111a8-b823-3ef9-a7a3-7042f80f2520 | -7.77869 | -46.04006 | 2026-08-21 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 33a0d662-8f38-3c2e-9298-01b5ec6646a7 | -13.74759 | -51.86497 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f73a475e-d741-342c-a960-393bb5a693a6 | -13.38932 | -54.38433 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c17f9699-b740-351e-9acb-5e3c74618920 | -12.22456 | -43.16303 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb93c511-7014-3ca1-a42d-a3c52487b230 | -15.44066 | -41.38787 | 2026-08-21 04:02:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f38b4f50-b8a2-374b-8e1e-6ada34e765ea | -10.52099 | -50.78152 | 2026-08-21 04:02:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05bfd486-8d46-39aa-a329-f83019c518f2 | -8.15897 | -46.72923 | 2026-08-21 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f665eb3-e3c4-37a7-8e0e-e97ad346b66a | -9.05778 | -50.88332 | 2026-08-21 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b83f198c-ae4e-3977-963d-7e65ea86957a | -12.74875 | -44.53337 | 2026-08-21 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e79b76e-b460-3328-a971-b02b0dfc3433 | -10.81997 | -50.99976 | 2026-08-21 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4032f7b2-aba6-377a-a4d4-c970a0c3be25 | -7.70519 | -46.60088 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85284518-7f2b-3abe-a183-55f0504ac885 | -11.35636 | -46.34687 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70bb7b4d-b306-3101-993f-702b0735643c | -12.81018 | -48.42009 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38317d2e-3185-3565-b653-0a8653977099 | -12.5057 | -47.85206 | 2026-08-21 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e732ec78-c87a-3241-b673-3e5f33d226ed | -11.21183 | -54.00846 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fa7b273-1b4f-3a9c-ba1e-89fc2e91e2ed | -12.44237 | -43.40587 | 2026-08-21 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4fc8fc8-793d-32ff-b4fd-146a44d8baee | -8.68612 | -47.48926 | 2026-08-21 04:02:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2a58550-59ce-31a1-b9bf-593e621edb87 | -14.45118 | -45.61055 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 35448384-054e-38b6-aa88-7e1d16411532 | -10.65535 | -49.02163 | 2026-08-21 04:02:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f92982a4-1b9f-35c8-aa3d-d799d47d03e7 | -8.45851 | -46.95279 | 2026-08-21 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bca89c6e-ab62-3db2-9874-860fd24cc072 | -10.63685 | -51.60541 | 2026-08-21 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 065c71cd-ce74-354b-837b-4f6388f3fee6 | -12.74745 | -48.47795 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2fe00cc0-51a0-3c45-967a-91280b0afb4d | -10.74766 | -50.33686 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec5b0b4c-117e-38fb-9cc3-466251c08af6 | -8.71234 | -49.61167 | 2026-08-21 04:02:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bd22616-fa0f-3488-8e5a-e0a966c5a0e4 | -12.43948 | -43.40084 | 2026-08-21 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 128735e3-00dc-3e9d-8f78-508dba8efe13 | -13.37521 | -54.3812 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 4c267224-f20e-3b4a-bec2-42e90f7324a9 | -12.83544 | -48.45019 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22aa6e73-9de0-3f1f-959c-33f70d2e4b3c | -8.45264 | -46.95737 | 2026-08-21 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c131cef-1c88-3e58-85a1-bd1053088b7b | -12.22819 | -43.16363 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa65bea7-365e-3b35-b6b9-ed5bf3a5b323 | -12.83442 | -48.4555 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3414aa18-b117-3eb9-b3a7-be1bb6d73c58 | -12.43872 | -43.40521 | 2026-08-21 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48315b32-d864-343a-96ae-ff09ebc74b01 | -13.45501 | -51.7741 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1a8841d-3478-3ae0-8bdb-49650aba4613 | -12.26613 | -43.16465 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 224821d8-8c20-34b4-b679-9b2c21d1be7a | -11.37751 | -47.21043 | 2026-08-21 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 63042dd1-3270-3ab6-babf-52c5395ee110 | -13.39137 | -54.39157 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a80b5095-6aac-3642-8435-4766e5b55008 | -12.8042 | -48.4244 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5152cf4f-eda1-3b56-8cd2-0e0d7189735d | -9.79652 | -46.63871 | 2026-08-21 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c2fe590-c636-3929-9397-b91bb95835b3 | -10.6607 | -49.02284 | 2026-08-21 04:02:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbcdd63e-cd86-3c82-8475-7f03201993a3 | -10.7643 | -50.31382 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 378b0304-63c8-32dd-b7f4-581ca241c820 | -12.25817 | -43.16761 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| dc5cf418-96e8-3042-9315-71a83ab941d8 | -10.90222 | -50.28317 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b29aa81-c80c-3f8a-928c-2af084611c0a | -12.73193 | -48.47761 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1315fd5-b23b-394c-9f6e-56c29b55f2c4 | -13.7837 | -43.18182 | 2026-08-21 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ac7fa011-c74a-3aed-ad1e-2f37be280b7a | -13.39483 | -54.39299 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d9ca5af9-9668-3f49-8602-65039910dbf4 | -14.72409 | -47.14626 | 2026-08-21 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 311a670d-05d3-32a9-9f45-9fc8474ba3b0 | -11.18888 | -54.01067 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56947cf7-4b44-3a72-9ffd-8f173995bfe8 | -8.11029 | -50.04453 | 2026-08-21 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00e42cc0-b41d-34a7-aac9-0dccb9489c06 | -12.80513 | -48.41948 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c7db383-7c73-3ed1-acb9-4e902efd5819 | -11.32651 | -45.02004 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29d60e1d-9d7d-3ffe-8df5-457d27ee959c | -10.65603 | -49.01809 | 2026-08-21 04:02:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fd1a998-0171-312f-9c00-903d821c80e5 | -13.43425 | -51.81376 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c95268a3-ac11-3e3e-b10a-8d07d1e5c7a4 | -14.45052 | -45.61417 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ad02475d-1ee6-39fc-a7b9-461e23385a77 | -11.37082 | -46.3684 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3afe4e2-e042-36f0-aec6-62653167b1b3 | -12.78864 | -48.45217 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 733dd761-461a-33d9-8292-a448c202397b | -8.09467 | -51.67066 | 2026-08-21 04:02:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70adc273-b308-3a98-b5ae-112b924547fd | -11.35467 | -46.01029 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed843507-d6dc-31cd-a5cb-da23ef8ced04 | -13.44065 | -43.8398 | 2026-08-21 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 34d7069d-932b-3799-89ad-26cd3be15c32 | -9.05053 | -50.88746 | 2026-08-21 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de979d01-1036-33a2-a10a-82e1c0cba716 | -10.75764 | -50.31685 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 059fe6d5-8b72-358e-9610-87620e408856 | -10.52074 | -50.77708 | 2026-08-21 04:02:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b2c3492a-e651-3a06-99c9-dcf60f611ec7 | -15.44399 | -41.38844 | 2026-08-21 04:02:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| a8835dc8-f621-3ff4-8a6d-9721412afed5 | -9.44401 | -51.62872 | 2026-08-21 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6512baa2-7c06-35c9-b615-eeaac6db7349 | -12.24584 | -43.17425 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c89d94ac-3ed7-3163-8fcf-dfccf95fd250 | -14.45922 | -45.61215 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15bc15f1-4dc9-3ea1-88d0-77d9952dd897 | -13.38384 | -54.37556 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |


[Clique aqui para ver as próximas entradas](README27.md)
