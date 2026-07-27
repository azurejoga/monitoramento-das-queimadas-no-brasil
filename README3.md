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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53185119-86b9-31e3-9456-8190d40e5ead | -2.76926 | -48.57217 | 2026-07-27 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39a1d2ae-324a-31e5-af00-627f29b7634f | -7.20433 | -44.8791 | 2026-07-27 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e8a1648-c1f4-3362-815c-da6f5fff760c | -6.92282 | -38.65827 | 2026-07-27 04:14:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c79a4e3-1fbe-3d93-a0f7-013461dd534d | -3.42328 | -43.16474 | 2026-07-27 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71d5f556-779e-31a2-bc3a-6b08f18aa6c2 | -8.73296 | -44.31803 | 2026-07-27 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6d28feb-252e-3e12-991a-a6e39e8708d3 | -5.46593 | -45.39837 | 2026-07-27 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8e06b51-a6c1-3e91-8e1d-bea6804db9b1 | -3.96223 | -43.11086 | 2026-07-27 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75215017-9c4a-3f0c-91db-eaf845918b8c | -2.04637 | -48.04072 | 2026-07-27 04:14:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ccf587f-10ed-3b2f-97dc-0185d1a37573 | -6.95751 | -42.1101 | 2026-07-27 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 682df7c3-f994-35ca-9424-a3f9f53be35d | -8.3665 | -45.38371 | 2026-07-27 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83d31dfc-2f72-3717-b89c-eafe35c401a8 | -4.94741 | -37.93911 | 2026-07-27 04:14:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 155c452d-6c8d-337a-87c3-6ac69f02508d | -4.00166 | -43.29486 | 2026-07-27 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac904b70-4033-3d07-a03a-b9ad698a3e83 | -7.90024 | -48.05449 | 2026-07-27 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c38cf521-f454-3217-8566-c6a5a0a0c809 | -3.91764 | -47.82033 | 2026-07-27 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73de8a5b-fdb3-342b-905b-255eefd88995 | -2.76326 | -49.46661 | 2026-07-27 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc17d1e6-2650-30b8-a3d7-784794d7d0d7 | -10.94 | -43.05 | 2026-07-27 04:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8bb72b2d-4547-3647-b2d7-1fa2cd18398f | -13.08913 | -43.56907 | 2026-07-27 04:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b52483d7-0486-353a-bad9-4974668f31a6 | -13.69403 | -51.9047 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc132aa4-8056-34fb-9f8a-69a01f1155e8 | -14.24019 | -54.56361 | 2026-07-27 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3beee126-cc36-39cb-a685-915a1149da57 | -10.9442 | -43.0619 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 892f5cae-ec9d-3ae2-af82-08ad12556073 | -23.3788 | -46.93156 | 2026-07-27 04:17:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| fe76daf8-2fba-3fcb-ba7f-387ca277db34 | -11.44619 | -47.53008 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5546fe45-bb77-32ac-9b6a-dfd8dcc2d363 | -10.94474 | -43.05832 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 6e6d3dee-c23a-3faa-9a65-de7bec3481c6 | -14.42832 | -43.76081 | 2026-07-27 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08a3be9e-5ad8-35ce-a06b-c61c5a651c2e | -14.49163 | -49.15359 | 2026-07-27 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62e2dbc4-33ec-30ae-8d97-663944c040f3 | -15.47788 | -42.21106 | 2026-07-27 04:17:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a0673da-b9c3-3e72-9803-265cdcc5340e | -14.36375 | -54.92 | 2026-07-27 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c8d8bb31-b829-3349-911d-0843a977cc83 | -12.32175 | -50.37956 | 2026-07-27 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5908ffa-f1bc-3d8a-96c0-c492933776f3 | -13.68922 | -51.90428 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 125f0387-15bf-33c0-9559-6f43ae57319c | -9.63399 | -45.51956 | 2026-07-27 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3710406d-efec-3df1-a326-26ac1de0bca1 | -10.93259 | -43.05257 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| df71bf89-33a5-3108-8968-247081db9cab | -11.49262 | -47.5413 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a05d972-b596-3de2-8e38-2bb2c5218368 | -12.32083 | -47.18912 | 2026-07-27 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac72c083-2a2c-3952-8cce-898076ee7fde | -13.76558 | -47.14522 | 2026-07-27 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7af72021-d9e3-3943-aa4c-5618e52d6d67 | -20.41996 | -48.62693 | 2026-07-27 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 192508c5-21e8-3fce-ba8d-c5b1db982417 | -10.93806 | -43.05728 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 69e3abc5-c1ce-384f-a953-363083064bc1 | -12.32435 | -47.1897 | 2026-07-27 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a84d95b0-c478-3d05-926a-268e1873ee03 | -11.46439 | -47.53241 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0306c0f-1e4e-3b27-a5da-dea1454f141a | -12.09994 | -45.80487 | 2026-07-27 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6c98934-9663-3c34-aa60-0904a05aacf6 | -14.35905 | -54.91505 | 2026-07-27 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| db47b39b-16de-31b6-a893-dc07db6cd903 | -23.37102 | -46.93785 | 2026-07-27 04:17:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 145b4648-9d57-36cf-b66d-4cdde782a506 | -11.49479 | -47.5506 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdbb10b9-711c-3bcc-b2b7-2a8827807795 | -15.87447 | -43.59857 | 2026-07-27 04:17:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d2e29f3-778e-3683-9c6b-7a84bdce216d | -13.70079 | -51.89261 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d306bacb-e013-3935-8110-d08c74ab7187 | -10.93204 | -43.05615 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cdce87dc-a734-3297-940b-7d1ace2ad6c1 | -15.96202 | -52.21139 | 2026-07-27 04:17:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d847da8e-6502-3de7-8ad9-23cc20daf11d | -14.3645 | -54.91629 | 2026-07-27 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 9a363d9d-83e0-3647-ae9e-99d00154102c | -13.69313 | -51.90944 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7f180f0a-6a7f-3954-9d7e-1ac0d2a24212 | -10.93752 | -43.06086 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a31c9b01-4a9e-3f0d-8483-fefcde6fc919 | -10.93914 | -43.05012 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 4b62841f-05f0-3a01-b639-9d5ebe46a112 | -11.7662 | -46.56401 | 2026-07-27 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 152a5b61-7731-3585-a0e3-f2dfa347043b | -14.70331 | -44.65515 | 2026-07-27 04:17:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d477a0f1-7bb2-3a6b-b7fa-95d81d76960c | -15.84426 | -47.95366 | 2026-07-27 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 954276ac-d60f-3b48-b1f2-756d5d002059 | -12.33052 | -47.17421 | 2026-07-27 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 079376f5-e648-361e-a7c9-adc1d64e8672 | -13.68957 | -51.90332 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48054f17-bcad-32a8-b67e-b94ced015205 | -11.49438 | -50.15996 | 2026-07-27 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f8b2135-65f5-3905-9e52-46b415264c5f | -11.98906 | -45.56009 | 2026-07-27 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbf7316a-7116-37c9-9d16-068b8ca3bcc5 | -10.34589 | -48.32629 | 2026-07-27 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3c0627f-212c-39e9-84f6-7ef1f1a80e26 | -14.50188 | -48.93734 | 2026-07-27 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9237054-3f42-35d4-adc9-159f7568982c | -14.36524 | -54.91259 | 2026-07-27 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ad5bddbc-ae2a-3cdb-8526-bab534dc3885 | -11.43896 | -47.52892 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7295dbe8-257e-36af-9882-1c7bb5146343 | -14.82977 | -41.96641 | 2026-07-27 04:17:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c64af8ef-520b-3286-b3d5-131398e9a330 | -20.79088 | -57.93719 | 2026-07-27 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| afb4caa0-ea20-3e29-908e-241c2d20555d | -11.46942 | -47.52453 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2598abdc-c89f-3015-be32-cd7a873cf331 | -23.37549 | -46.93095 | 2026-07-27 04:17:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| daca2e16-7d65-3c0b-abc2-406c41be7896 | -12.32215 | -47.18107 | 2026-07-27 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d079fa5-9eee-396f-b947-72478a868de2 | -10.94194 | -43.05422 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| e5972b94-3c4d-3db0-81da-6823d88251da | -11.49556 | -47.54597 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dab90c43-c006-3f44-acc9-d3379b7c228d | -10.53751 | -48.61984 | 2026-07-27 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd816e6e-ce5c-32f8-a015-13d6b76889a9 | -11.25667 | -41.90472 | 2026-07-27 04:17:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b078267b-c622-30b1-b51d-b2b485e7a93c | -12.32501 | -47.18568 | 2026-07-27 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cf23987-c284-3b3e-8cd7-14047f03375b | -23.37159 | -46.9341 | 2026-07-27 04:17:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a9c650a8-644e-3ab6-be72-9a64416e5b4e | -14.3484 | -54.93954 | 2026-07-27 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83dee454-15ab-319e-b02a-7047201766e9 | -12.32568 | -47.18165 | 2026-07-27 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aed51b5a-c5aa-3cba-9e9c-3b6b92c81777 | -13.69223 | -51.91417 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cd8772da-f225-34e0-a237-ea2f7bc605af | -22.86367 | -43.53044 | 2026-07-27 04:17:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 56d89a59-cd0f-3a4f-91f9-fc157d3b806c | -14.2395 | -54.56707 | 2026-07-27 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e3b62de-4b4f-363c-9b80-2c7829dbf916 | -9.40257 | -48.94355 | 2026-07-27 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aca3a754-be91-36c1-afc0-682e9d360708 | -11.46223 | -47.52312 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab6da3b1-ed86-341f-b9db-f3a6a7e803d1 | -10.53666 | -48.62482 | 2026-07-27 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d98f9fc-d585-3e7a-a23c-d57071249bd6 | -10.53362 | -48.61917 | 2026-07-27 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd31c3f0-9e52-395b-98cd-1b2f6d6875aa | -14.35978 | -54.91137 | 2026-07-27 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b8468cd5-fef9-33e2-8153-4a328d2d16e1 | -10.93538 | -43.05667 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 91cc8290-df38-36bd-b0cb-c442058d8922 | -23.57434 | -45.76437 | 2026-07-27 04:17:00 | NOAA-21 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b3bac527-c071-3af1-9b5c-2991cbd2c2b1 | -13.63509 | -44.44127 | 2026-07-27 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 805cf29e-aa4a-392a-8b32-5699f95d262d | -11.89003 | -43.83215 | 2026-07-27 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8937c640-6c23-387d-86d5-ae5f1c920824 | -11.48382 | -47.52728 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7dee7867-d4f3-38fa-9477-f070956e2ec7 | -11.98848 | -45.56369 | 2026-07-27 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76f3545d-d086-3dc7-8cfc-01f2406e722e | -11.76557 | -46.56785 | 2026-07-27 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d7f74e8-0c19-3410-8445-d3fe18df9ac9 | -13.70123 | -51.89163 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 05ee72b2-5d60-3cb4-af30-ef79839b80c3 | -11.10086 | -45.30763 | 2026-07-27 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d95a4b9c-f36d-3a9c-a572-b754519af3e5 | -12.32245 | -50.37555 | 2026-07-27 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15e4c8b2-5562-3f05-844e-9939c7c67d1e | -11.45863 | -47.52246 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d061846-98ab-343b-a6a7-a3529363f847 | -11.26848 | -47.69193 | 2026-07-27 04:17:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a14269b7-ec97-3f4c-a40b-934b87e726cd | -14.3583 | -54.91877 | 2026-07-27 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a01fdd32-21ca-3844-bc62-6c632247d16a | -12.32149 | -47.1851 | 2026-07-27 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3332dbb3-7c23-3289-bca5-3481d22384ec | -11.45571 | -47.51773 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0071c960-cc25-3751-9a6c-230224182ed2 | -11.44257 | -47.5295 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38bb8b03-bb63-351a-a4f9-64e6a7c4f169 | -12.30133 | -50.3717 | 2026-07-27 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 326adaec-07e8-3d36-b21a-ac18a92bf4d3 | -10.92925 | -43.05205 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |


[Clique aqui para ver as próximas entradas](README4.md)
