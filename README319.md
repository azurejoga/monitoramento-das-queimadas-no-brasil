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

## Dados Diários - Página 319

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5a14032-ca6c-3259-a681-ef37b93983ab | -12.16473 | -39.91563 | 2026-10-08 16:37:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 4676ff55-c623-32be-afc1-71eba0e96afc | -12.18797 | -44.82455 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 5130e9fa-3ff3-3617-9f01-cef7c6c86dcc | -8.80804 | -45.80146 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d5b158a8-7777-3de4-b3f6-5958055b3df7 | -11.08972 | -44.01807 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5e581d4a-2718-36d2-a903-bdd1e077a5e1 | -7.76408 | -44.17836 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 895c813a-f16a-3a65-b8e3-295cbd193e29 | -6.18974 | -37.85729 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a01a1942-83cc-3638-bd11-3ef08d430c33 | -11.08195 | -44.01202 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 96d06d12-763a-3a43-bd1d-a9559d80816b | -19.07263 | -48.63826 | 2026-10-08 16:37:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b28dd1d0-04ef-3ac6-83a4-5d18217a4126 | -8.33839 | -45.03622 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 745dfb66-8339-387e-a991-09b37079aeb3 | -6.43946 | -45.93379 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 960a42f9-a00a-3d54-ac2f-3b56725c54eb | -13.55741 | -49.15335 | 2026-10-08 16:37:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 02912e33-14d0-34b9-858a-c58788ff0376 | -8.18525 | -45.7649 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 86d0ffc6-493f-3ff1-9f46-289ea6ac2135 | -6.05181 | -42.58913 | 2026-10-08 16:37:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| f2ea1890-ac3a-3694-acf1-c5547c1e4088 | -8.77951 | -47.26334 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a5702caa-b077-3412-a00a-91be79f351f1 | -9.83931 | -47.48598 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0f2a664-f546-37c5-9547-4d33b556ce01 | -6.68654 | -42.29836 | 2026-10-08 16:37:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| d81e00b3-07fd-3eaa-a97c-2214e2142352 | -10.39266 | -46.25676 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8cc868a0-f0b0-3d32-96ef-5594307f702b | -9.97498 | -43.57376 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 6b3457b7-e8d9-38d8-a046-5fc2b0a33f1d | -8.28189 | -45.73163 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4becce5e-ec53-3fed-8709-158043cdb7d5 | -13.1216 | -46.35529 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 573aca08-4a1e-3ad5-aece-057f198db492 | -7.42517 | -47.33278 | 2026-10-08 16:37:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 387a52ed-fac4-38ca-a274-57f8de9c750f | -12.19442 | -48.42331 | 2026-10-08 16:37:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 54f3d56c-79df-3e4c-a2eb-2d0bc999f68d | -18.3564 | -42.76708 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 3d0c810e-6348-355a-b9b1-a258dff22a23 | -8.96388 | -45.15284 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 777a0948-d79c-3c8c-bfc8-8560a07c8e77 | -8.07849 | -45.62184 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 28e88ae0-0300-32e7-84be-bff5432e849b | -12.02668 | -43.44915 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 313.3 |
| 4deb992e-77f3-3e81-b5f1-06433cdf7f93 | -10.33665 | -47.75931 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7ef4d7e1-7b49-3b0d-8f72-f0b70cbd552c | -6.34464 | -44.87443 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8f15b50f-0452-3016-829b-bfff434b8f6f | -6.32624 | -37.75236 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 27cdaca3-7f83-3c16-bf8f-ebe4be626e54 | -11.6489 | -43.68129 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| e77ccd0c-7d50-3fc4-98fc-fee0612f8e5c | -9.81624 | -45.69428 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e6f9e85f-d8dc-300c-bd4e-bb10a788dc65 | -6.6374 | -44.88186 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0e73cbb0-ed92-3937-901d-8964e7a4be42 | -5.72586 | -41.77971 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 66276b22-56f3-374c-ba69-dee7d8611db6 | -7.10195 | -42.52963 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 33d95def-4e6b-395e-a713-9f25e335863e | -6.53382 | -45.39692 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 250221a3-24dc-38fc-b07b-28b132947423 | -11.60538 | -43.64395 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5da18b97-2bf7-3e10-9235-6b34ca03ef5e | -6.99553 | -41.48079 | 2026-10-08 16:37:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| fdc73d12-7eec-3cd0-a39e-9a77d0531966 | -10.35022 | -47.75333 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c3b6d2c7-f1f0-3765-aeab-1314d157c091 | -12.24013 | -44.74432 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9fa3edea-8ed1-3958-94e9-d2a64b4249f9 | -11.762 | -45.48612 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fb12324b-4602-3771-bc53-dc7bc43d46ab | -9.43841 | -41.73645 | 2026-10-08 16:37:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ea2d2ac3-7e1c-3cb3-ab1f-c2487ef4ef3e | -8.07796 | -45.61837 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 4968ea44-ad19-3169-a905-9636695c3762 | -5.37284 | -38.28328 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| fef9b2ab-9791-3f42-b32a-889d761691bb | -7.1838 | -44.32692 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 95fb77ff-730a-33c4-92e2-289b9bf715fe | -11.85637 | -47.3868 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 37591c32-2b81-364a-afec-ddf8ef856952 | -9.80875 | -44.77654 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7418811c-2b04-3ff1-a0ce-1c02bb2adc87 | -11.22024 | -41.58447 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 413e6b57-c134-3e32-abb3-b796a6b88aa6 | -10.93931 | -45.38205 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0f49b015-32b5-3b2a-97b1-8d00da06f6d6 | -7.21708 | -44.15445 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 90cb23fc-c9a8-3eab-868a-f865f908aeeb | -9.90097 | -45.20165 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d0f2f33f-9c01-316a-8903-4e88f7212a1b | -18.18506 | -42.58072 | 2026-10-08 16:37:00 | NOAA-20 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0e6c4e52-75a5-349b-baf7-1085093e9f57 | -6.0595 | -42.91954 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c104ed66-f677-39ea-b1df-64673135ceb4 | -6.58144 | -43.04082 | 2026-10-08 16:37:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 970655c5-4881-30fa-9a9e-38c8d312df61 | -7.21665 | -44.28448 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9a50ad32-4429-32c4-af61-a80c104b50a4 | -6.97028 | -43.89901 | 2026-10-08 16:37:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ee6e719f-9303-32a8-8034-2e2d69043bb9 | -11.15021 | -47.29371 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cc343989-36bf-3c91-9ac7-1070c99a5ff4 | -9.84521 | -47.85465 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| da3f1f75-8ebb-3620-b692-8839b487b8bf | -11.9643 | -47.76574 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0c4260eb-0e69-3519-8f6d-501d8e5f99bb | -13.13971 | -46.33704 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 23c42730-6171-3d0b-8187-8e1eb973a045 | -10.52862 | -57.75797 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e6b4a792-a3eb-373c-9701-c49b7008159f | -5.7126 | -41.7227 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 969eba91-ef65-3492-904a-00c471e7e1e4 | -11.04656 | -53.99932 | 2026-10-08 16:37:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a676f146-a7d2-3bd7-a957-dbdd0dd24b66 | -10.25315 | -49.67544 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9e5aeebe-1ee0-3284-b760-709073784358 | -12.23853 | -44.73376 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e10bcfe1-8194-36b5-9f58-66b20a5210db | -10.4552 | -47.28892 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 784985e3-725a-3a81-a1c6-780bb2bc26eb | -6.37986 | -45.78733 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cb71eed0-9b83-3cdb-b361-f27ef8667fb1 | -11.22469 | -45.25056 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e40cd7a1-3286-3f8d-9a35-f8fb8384f233 | -11.8523 | -47.35869 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 47728b82-fc3c-39b5-872a-4f48a32e6eab | -12.17591 | -44.81204 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 70e29380-df3f-30cc-8bd7-aa03222eccc7 | -11.77864 | -45.57446 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| bd95461d-3274-3936-bc10-d093d435ed58 | -7.18941 | -44.34093 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 62b60042-06be-3a31-983c-e20a8417d434 | -9.09186 | -47.58379 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 88c8a7b0-e195-3561-9fcb-714f4c6d1b6f | -10.47332 | -47.85597 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 623efbfb-5eb5-3213-b86e-1470f2fc2d0a | -11.36311 | -41.52174 | 2026-10-08 16:37:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 97a5e23b-5ab9-3f96-847c-9c460ac09a85 | -10.3443 | -47.76238 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0ebd67dc-8277-3b48-a614-d3ecc01748f7 | -8.34941 | -47.66944 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33025946-3a39-382b-8ad4-6db99a00083d | -18.2606 | -42.17927 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 324cda20-4059-305a-910c-2ed3a9d0c60e | -7.85816 | -44.9596 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c7859906-d53f-3888-8aa9-552f08ff5ec5 | -7.05355 | -44.3216 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2aff831f-dea1-3711-bc30-1abf806e7d91 | -7.38689 | -46.2053 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f8710b4d-9969-396c-bef1-44f4af5285f0 | -10.86699 | -45.55573 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b19286b4-3671-3008-a077-eb7fc4a112b5 | -7.88883 | -55.01153 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9086b423-7f5a-39df-b397-2e1a3cf17522 | -11.6321 | -43.59536 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 591263b7-d45f-39d5-b607-8485d6a2da3c | -5.70487 | -41.72393 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 27cc341c-4324-3352-a3da-e7a19fecc856 | -9.83861 | -46.17896 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| faab174e-b847-347a-be76-6cc827bf2e81 | -8.78934 | -47.59326 | 2026-10-08 16:37:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7fdde691-ab39-3f4d-9694-bf4e3c24c0ea | -6.32028 | -37.74768 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 18bae9e0-45c3-38b5-a481-2ae15cfbdc41 | -6.36451 | -42.53025 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 4d1db160-75ab-31f9-b46d-090e6dfb6531 | -9.53399 | -45.62173 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 8e3b243e-754a-3666-9e93-0be2f9479e67 | -11.34637 | -39.85579 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 19.9 |
| b1ba63c8-a2c5-367a-a113-211778567e5f | -12.72024 | -45.81675 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 92ff32c5-ae04-3139-88e1-ea95711bb60d | -17.33964 | -41.38817 | 2026-10-08 16:37:00 | NOAA-20 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 022158a3-3b27-3378-93e6-d30a372cf30d | -8.35632 | -47.66844 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ef19c847-cdfa-3204-8182-088be5383883 | -7.31689 | -41.78748 | 2026-10-08 16:37:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| fd7b4f0c-e05b-3e4a-adb6-c765f205e0cf | -6.16958 | -44.85928 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| f39bd963-3cba-37a0-b155-6a17d9e7a990 | -6.85172 | -41.76299 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c1773312-4230-3e89-8785-078e86d83885 | -11.20199 | -49.4266 | 2026-10-08 16:37:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1f3547cd-33ad-3a43-8093-e5a1dfae15fb | -6.40504 | -44.9556 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| ee971347-1722-3aeb-bff2-f786b91b06a3 | -6.83682 | -39.54956 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 07190133-2a2a-3d45-8ff9-c8780ce7c79f | -6.74583 | -44.14245 | 2026-10-08 16:37:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README320.md)
