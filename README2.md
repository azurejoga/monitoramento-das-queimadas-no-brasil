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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9adda417-a73d-3197-b52c-2e5bf31fe377 | -7.7567 | -44.0415 | 2025-10-09 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 07bbeb7a-6805-3da4-a0ed-053b8377a1e5 | -5.3061 | -45.3861 | 2025-10-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 928fa62a-8a14-3db5-9a91-5e4e95e5eef3 | -4.278 | -48.8891 | 2025-10-09 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 345ce2d0-68ad-3cce-bf6a-991ef1d6f388 | -14.4717 | -52.8937 | 2025-10-09 00:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5bfbaa3d-7f00-31ff-99c5-b12a4418b3ed | -10.7452 | -49.3296 | 2025-10-09 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9e8d6973-4425-364b-bd79-c8ff1a8acf31 | -4.4445 | -43.2397 | 2025-10-09 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| caef07ea-4309-359b-9275-9d88be2d7829 | -4.4632 | -43.2386 | 2025-10-09 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6f0ef658-9c5b-37d1-869f-25649c247e91 | -6.6995 | -46.2946 | 2025-10-09 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 311.4 |
| 51cdad23-5c55-351c-b964-26ab39a43277 | -5.7979 | -44.6715 | 2025-10-09 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| f36308b5-6827-30ad-b65a-4bf2fd18912f | -5.7981 | -44.6487 | 2025-10-09 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f34b3254-09f7-3e63-99fd-aef6ac3299d7 | -7.7755 | -44.0396 | 2025-10-09 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 93728a72-079d-31af-bd4a-27ea479da676 | -9.1018 | -47.9575 | 2025-10-09 00:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 79c42eb9-f90d-30b7-8bd4-bd2200a96c76 | -13.7913 | -45.8321 | 2025-10-09 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 94fcca32-bd40-399c-9209-44aa49392207 | -4.2781 | -48.8677 | 2025-10-09 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f72d0cec-d990-3500-a32f-36758da34ff6 | -14.4334 | -43.9635 | 2025-10-09 00:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 591.0 |
| 20eb7328-803b-3820-8765-14c7b6b52135 | -17.8413 | -57.6459 | 2025-10-09 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| e85332ca-4786-3961-83ea-b3ac357e14a1 | -6.6808 | -46.2961 | 2025-10-09 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 297.9 |
| 31ad865e-6600-3220-81a3-91f04b6c767d | -13.8108 | -45.8288 | 2025-10-09 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 188ff33b-b004-3a67-bae5-9932fe682df9 | -9.6866 | -49.3766 | 2025-10-09 00:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| db9c58da-fb45-337c-8b15-f27b086f6a71 | -7.7758 | -44.0164 | 2025-10-09 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 9141731f-0a39-368a-b7db-9e9a372156ae | -10.8743 | -50.9439 | 2025-10-09 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9fed2096-ae20-302b-94a3-33ca324bb733 | -4.9894 | -45.3159 | 2025-10-09 00:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 8b257646-9b0b-31ac-99ca-80f4fa621de6 | -13.7909 | -45.8552 | 2025-10-09 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 325.2 |
| 583baf19-4a04-39e8-a56e-527ebb0bd534 | -15.316 | -43.8377 | 2025-10-09 00:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 99469d3d-5889-34e2-a0ce-9df3034050a0 | -9.0829 | -47.9594 | 2025-10-09 00:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 208ce0eb-a4e6-3969-b378-84a91e0dfa38 | -4.278 | -48.8891 | 2025-10-09 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| a70614b8-3ee1-32df-acc8-8481f0f805fb | -4.4446 | -43.2164 | 2025-10-09 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| b6e85099-6d7f-311f-9b67-3e21f0fbc669 | -7.7569 | -44.0183 | 2025-10-09 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 9e0cc4d7-7b69-3124-af2f-0510f375c8e1 | -14.4523 | -52.8961 | 2025-10-09 00:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 1f6c99b0-6732-3712-b566-587679ebf525 | -14.4329 | -43.9874 | 2025-10-09 00:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 334.6 |
| 7e898760-c917-34fe-9651-62c2a0157b47 | -7.7567 | -44.0415 | 2025-10-09 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 215.6 |
| c1e39650-8ce1-3565-b816-7ae464d8a67b | -4.9708 | -45.317 | 2025-10-09 00:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 295125b5-29fb-3929-95fb-1a5898a85150 | -18.9974 | -43.0805 | 2025-10-09 00:20:00 | GOES-19 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.9 |
| 6c27feda-3904-3c84-af82-f0454ae46e75 | -14.4133 | -43.9911 | 2025-10-09 00:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 313.0 |
| ce67b4c5-4596-3534-857f-d0f49008eb70 | -16.3955 | -46.3741 | 2025-10-09 00:20:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 7c6449e9-4eb0-3554-bbb4-ed97e7d3cfea | -14.4713 | -52.9148 | 2025-10-09 00:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| bf550db6-97dc-3577-af77-c820adcf731a | -10.8554 | -44.6431 | 2025-10-09 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 05444665-43f2-37a9-85cc-495eb3f17701 | -16.3757 | -46.3779 | 2025-10-09 00:20:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 162.2 |
| e5ddc7ae-4474-3c94-a5ac-9c630b1f8ea7 | -13.7904 | -45.8782 | 2025-10-09 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 679bf24f-23d0-3195-b36f-4b0522334c63 | -4.4633 | -43.2152 | 2025-10-09 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 8b599988-256b-35d2-8dea-3562090fa0ac | -8.1993 | -43.3424 | 2025-10-09 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 9abb7f28-ff6f-33d7-ab78-f35117fc1dfd | -14.4717 | -52.8937 | 2025-10-09 00:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 7ad48d7c-2616-3bb2-9119-a7d949af88d8 | -14.4138 | -43.9672 | 2025-10-09 00:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 536.9 |
| 8f9bf8c9-ae43-32ff-807f-9523735dcb99 | -5.043 | -45.6278 | 2025-10-09 00:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 64d8795f-85ab-357f-aa52-6608ea21f4cd | -9.0832 | -47.9374 | 2025-10-09 00:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 33ee89b8-ecc2-3344-a2d3-e41fabc09a31 | -13.7714 | -45.8584 | 2025-10-09 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 07deed6d-9597-316e-a697-d62535dd234d | -10.8745 | -44.6404 | 2025-10-09 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| f73e8474-c6f3-365c-ac35-305cc24470f0 | -13.8103 | -45.8519 | 2025-10-09 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| ddda7c10-b058-382e-a32a-961cfbf2f3ec | -6.6806 | -46.3184 | 2025-10-09 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 840ac4d2-5e34-32f0-b9fd-48c101261ac4 | -6.6993 | -46.3169 | 2025-10-09 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 9ebceb30-7b10-36ab-8787-f4e20e6159fb | -14.4133 | -43.9911 | 2025-10-09 00:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 320.1 |
| 33a19508-c8db-36ad-93c0-833ea2371c43 | -14.4329 | -43.9874 | 2025-10-09 00:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 293.6 |
| 5eb33c49-1678-321e-9def-b4cbd730902a | -14.4717 | -52.8937 | 2025-10-09 00:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 965b9b67-4484-3db8-9ad0-4390135b5c0a | -4.4632 | -43.2386 | 2025-10-09 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 291c65ab-4105-3f95-8669-66b17a67b868 | -8.6292 | -45.1228 | 2025-10-09 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 0c9bfd33-37cf-338e-9d14-93e8e6f03844 | -16.3757 | -46.3779 | 2025-10-09 00:30:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 26ed7246-f3e9-38cc-913d-c980e418f52a | -21.3862 | -49.1154 | 2025-10-09 00:30:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| cdc1bde4-70c0-3129-ae25-246531ee42ad | -10.8554 | -44.6431 | 2025-10-09 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 8e0972ea-c5fb-369c-a756-d95e0d33705f | -21.3856 | -49.1385 | 2025-10-09 00:30:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.0 |
| 7df97be0-5895-3ffb-a242-213db0f63afc | -13.7909 | -45.8552 | 2025-10-09 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 486.7 |
| 0bf1f261-158b-3b5d-9e14-55900c498bc8 | -14.4138 | -43.9672 | 2025-10-09 00:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 488.1 |
| bb52685b-eb23-3216-abac-2e396493aed0 | -13.8108 | -45.8288 | 2025-10-09 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 27471be0-2ce8-3831-b7e5-d244e682d029 | -14.452 | -52.9172 | 2025-10-09 00:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 13112f3e-a480-3b9c-b1d6-52f38e4e85fb | -9.0829 | -47.9594 | 2025-10-09 00:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 142.2 |
| da030775-890e-3f39-81b9-4fb034de3823 | -5.46 | -44.8322 | 2025-10-09 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a71b6e36-d7e1-34b2-b145-f2027fcd4140 | -8.5218 | -46.1526 | 2025-10-09 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| e6bc79f3-692d-3cf3-bc7a-3bd2bb1e796b | -5.4602 | -44.8095 | 2025-10-09 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 5eee5330-b8ff-3ed1-b763-30cb49d61d99 | -6.6806 | -46.3184 | 2025-10-09 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 66634a46-ae39-3e2b-9d8a-77ce299fd710 | -5.043 | -45.6278 | 2025-10-09 00:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| aeca28eb-e611-36e4-8fba-b6925c8c78f0 | -13.8103 | -45.8519 | 2025-10-09 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 173.1 |
| dadc880d-5b8a-3c73-8220-6fc5004abc38 | -7.7758 | -44.0164 | 2025-10-09 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 30a6035f-966b-3ce8-820b-ffe633fd5ca5 | -7.7755 | -44.0396 | 2025-10-09 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 8ea97dfc-c612-30a0-9813-064b636dbc42 | -4.278 | -48.8891 | 2025-10-09 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 0f660404-4ede-371c-b29c-598066464b93 | -13.7714 | -45.8584 | 2025-10-09 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a5ce6e81-8395-3090-be1a-8c8f636d20ca | -9.6869 | -49.355 | 2025-10-09 00:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1295fe97-6c5c-363f-a012-20b448188df0 | -21.4069 | -49.1106 | 2025-10-09 00:30:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.6 |
| 25921910-e536-3b37-aaff-257a657c9c6b | -10.8558 | -44.6199 | 2025-10-09 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 9cbabd6e-4b90-3ba8-a9f0-882c494d9520 | -9.1018 | -47.9575 | 2025-10-09 00:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 44979e82-d849-3eb7-8f5a-cfc5fb00d2bc | -4.4633 | -43.2152 | 2025-10-09 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 67ec34e7-76fa-309b-9b20-62df49cf75ff | -7.7567 | -44.0415 | 2025-10-09 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 216.4 |
| 3d9bc819-d3b1-36a2-bee4-e5bc3044c078 | -9.0832 | -47.9374 | 2025-10-09 00:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 2d436342-3085-3333-8c62-b3a359c8ed24 | -13.7913 | -45.8321 | 2025-10-09 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 225.3 |
| 203951c5-f3bc-33ed-996e-08193e055d2f | -14.4334 | -43.9635 | 2025-10-09 00:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 449.6 |
| bd1cf0cb-9af0-3553-b6f5-860943d491c1 | -5.4413 | -44.8335 | 2025-10-09 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 5aa829bc-5254-3fa3-ba2b-7cce5a46eefd | -7.7569 | -44.0183 | 2025-10-09 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 6eeec9e6-ee69-3349-8f05-640dbaac00c8 | -6.6995 | -46.2946 | 2025-10-09 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 276.2 |
| f4e1a46f-1bd0-3641-a05b-16efafd8cd84 | -13.7904 | -45.8782 | 2025-10-09 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 6727bccf-32de-31c3-93a8-65482c26648d | -4.9708 | -45.317 | 2025-10-09 00:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 94850efb-21b9-3773-ab13-8ef2568e253e | -21.4062 | -49.1338 | 2025-10-09 00:30:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.1 |
| e48a8f31-ab16-396c-b8d7-b8349baef8aa | -17.8413 | -57.6459 | 2025-10-09 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 05160c88-bd56-3594-bea7-eab613e96dea | -14.4339 | -43.9396 | 2025-10-09 00:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 143122ed-8d49-3ee1-8081-7c14d452616c | -5.4415 | -44.8107 | 2025-10-09 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| cfb5036e-c571-322e-ad62-9ce6e938fb2d | -16.3955 | -46.3741 | 2025-10-09 00:30:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 5fa0c6ce-7b29-3ec2-9a3f-8f7e95ba4bb5 | -14.4713 | -52.9148 | 2025-10-09 00:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 6875c76b-82db-3563-b61b-f6cabfcd2141 | -8.1993 | -43.3424 | 2025-10-09 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.4 |
| 45fbd5af-60f9-3955-b70b-39c9db82c3b0 | -4.2781 | -48.8677 | 2025-10-09 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7e38d9cf-6899-3d45-8375-81e59ba319fe | -6.6993 | -46.3169 | 2025-10-09 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 17af34c8-af55-3011-9a4f-fc6275a5ff08 | -9.6866 | -49.3766 | 2025-10-09 00:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 44fd68bd-c625-3766-a882-a655dde84a3d | -9.7055 | -49.3747 | 2025-10-09 00:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 66f133f4-b9b6-3117-97ce-ab5cbf5a0a7c | -6.6808 | -46.2961 | 2025-10-09 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 325.3 |


[Clique aqui para ver as próximas entradas](README3.md)
