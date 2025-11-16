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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b30a266a-6cf7-332c-8c41-9174bebfca67 | -6.52964 | -39.64901 | 2025-11-16 04:08:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fff8029e-03bb-3d1d-a367-9d2a8489dd7d | -8.57708 | -46.05128 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b936b4df-69ab-3f29-af4b-a025c6958183 | -10.531 | -44.8391 | 2025-11-16 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f4b2f7c-ceec-3429-b87a-154c7207ee96 | -7.71295 | -47.30072 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0948d4c-f2a2-39f8-a5ae-6a9bb35dca54 | -10.00198 | -44.76937 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef78d19b-dbd2-32f1-9fdf-aaf8ac69296c | -11.70997 | -48.87048 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8da11624-9f04-36e5-bfa5-38114023d85d | -6.30866 | -43.79146 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| f83281e3-0206-36d5-a9cd-51e59150314f | -10.32644 | -44.26694 | 2025-11-16 04:08:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57c3bac0-4c95-3fc4-98ea-a8c0a19e0f87 | -7.33183 | -39.9634 | 2025-11-16 04:08:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c5e22284-cb42-3180-80d2-08926d8d5536 | -8.3143 | -45.40477 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2cae93a-a1e7-3146-918f-a6a338492d5d | -12.40229 | -48.0971 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be58d3ae-7581-389d-a3cc-36f488e25e6d | -10.61808 | -44.58894 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 584e470a-7a37-31ff-831c-b24b5b9ad51b | -10.54505 | -47.93355 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6f3ecfd-ffb1-3c3d-989d-7c354ff0f8d1 | -12.00019 | -49.27348 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9f8eaefc-bc9f-3a0e-a412-33175881e7cb | -6.41555 | -42.33473 | 2025-11-16 04:08:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8f22a32b-7d98-37a4-ac67-08331d638ede | -5.49029 | -46.9164 | 2025-11-16 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9abab02-8fc8-3903-8ac8-6fba53f60cb6 | -6.08621 | -41.60331 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e7292c9a-9178-3663-a266-3f75d729ed3f | -10.18186 | -44.4012 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49e868cd-ffcf-3b77-a819-b78235eec39b | -7.22479 | -47.98267 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23eb6d69-7659-32f0-b975-f35fd2b3032c | -11.97709 | -44.96421 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d7192af-9470-3d79-95b5-9bb47d205edf | -10.84647 | -44.09388 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eeccfd42-0a05-33a0-bfe1-0714fc0e4fe3 | -6.05535 | -46.60986 | 2025-11-16 04:08:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe40a403-f7a9-3bc5-9f7b-777eb17f68b1 | -6.09118 | -41.6147 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b8ef0865-e409-3c10-80ed-2fff30147288 | -8.55386 | -47.78986 | 2025-11-16 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58b2b991-4523-35f0-9e00-372917f32fc9 | -7.04853 | -42.243 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d019df4a-8237-3677-8f64-243c91df3ce2 | -7.71014 | -47.29229 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac280877-4dc9-3382-856e-0fedf772febe | -12.21268 | -49.54952 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5e029f6-0245-3588-958a-2b4474039fd6 | -9.72638 | -43.96398 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 99cec0bd-5286-357f-8a53-ef1fa0b48928 | -11.91502 | -46.18842 | 2025-11-16 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea1c4c52-dbcd-3ded-a067-4dd0cc74cdf1 | -7.79937 | -41.01373 | 2025-11-16 04:08:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f8402d80-86c2-3d19-9dda-d2c9b720aac7 | -12.63621 | -45.07703 | 2025-11-16 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c56db9e-dc63-3d0f-9ea0-d1ce67dac30b | -11.99939 | -49.27781 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 8480b79e-68e8-3d0e-a3b8-c422099a143a | -7.21606 | -47.98118 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9ef1a4e-fa6b-3b0a-86d1-3dbe77847f1f | -7.11879 | -46.15421 | 2025-11-16 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 174b2407-a4ef-37e0-8418-cdad38e23646 | -10.70152 | -44.52767 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e896614-daf2-3b73-9ede-43ca374705dc | -6.05778 | -41.74036 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e54b39b6-a1fc-38ec-aa15-3b680a2b1f93 | -7.22569 | -47.98115 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db44f3be-2749-376b-af18-b36061fe7a67 | -6.95251 | -38.72119 | 2025-11-16 04:08:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 745bb773-6dd5-3b3f-90bb-f4cf7570d294 | -8.09951 | -46.02937 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 363718ce-a20b-321e-afc6-9f95371917c5 | -7.3723 | -43.31554 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd90e604-f438-3e29-9263-27f70e2fdbc3 | -10.70845 | -44.03076 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 583187fa-3e1a-3bb7-a2c1-f7528ed71cba | -6.99252 | -45.61427 | 2025-11-16 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0715d9e9-b838-3da2-9b3e-cf26c6160c0a | -5.63956 | -47.74557 | 2025-11-16 04:08:00 | NOAA-20 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f40d149b-ee23-3669-869a-bde3034cf791 | -6.30457 | -43.79474 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 78a7cbab-18ad-3017-8fd0-f4ae091ea69e | -12.06345 | -48.21807 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b2620296-3875-3f31-a5be-0b72cd7433db | -12.4589 | -43.79694 | 2025-11-16 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5c181dd-d88a-3bea-8a70-c4b72021ed9b | -12.69076 | -43.43125 | 2025-11-16 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 565b8df3-c641-3a9c-bd08-b833b52c6d47 | -10.70899 | -44.52505 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 94473370-df94-35ec-bbfb-5a38624da276 | -6.3121 | -43.7804 | 2025-11-16 04:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 3b8c4e53-93e4-3bcf-8a35-aaa57aaeec55 | -4.4246 | -43.4038 | 2025-11-16 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 360d15b3-7d41-380a-8c7e-2bc5afbfeb92 | -12.0004 | -49.2683 | 2025-11-16 04:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 407d8ea7-0db3-33e3-b57e-0c651e682828 | -2.5238 | -47.8115 | 2025-11-16 04:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 92796d0e-2bf4-3620-9150-5162f1429da1 | -13.81119 | -42.5483 | 2025-11-16 04:10:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| bb6985a1-129c-372d-bbf7-ae031761868c | -14.49713 | -47.98702 | 2025-11-16 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 886af2dd-bf6d-39d4-aec9-3c33fa67072e | -19.73846 | -48.16195 | 2025-11-16 04:10:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2f4da30-a9f0-3419-ab99-1417c0bdce7b | -14.67963 | -46.55475 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c0d0ac0b-1b7b-3259-b4fa-edb1cd70deb7 | -16.5282 | -43.56762 | 2025-11-16 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab5a7fb5-58c5-3823-8da0-06c6857796ab | -14.66241 | -46.59032 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1f0a215-43e0-3f51-bd6c-01b940aba212 | -14.65162 | -46.58857 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9d9a3dae-d759-392b-b3ee-0483fe82829f | -14.67113 | -46.53985 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dcb73e2d-dc7b-3096-aad9-a93d17c92c8e | -15.47381 | -43.18772 | 2025-11-16 04:10:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b92bb84b-7b46-31d2-a106-4b7fc46e3239 | -13.82562 | -43.77206 | 2025-11-16 04:10:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 244c26ab-0bbe-3c5c-b1a1-2f7ea1f52d45 | -12.84772 | -46.42016 | 2025-11-16 04:10:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67cbd67a-0b59-3459-b0f1-ee09fa8d8cc6 | -14.64805 | -46.56657 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 223e13f6-eb96-3805-9c9f-6c148d1ee5ac | -14.64358 | -46.59224 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b18582e9-e7a6-3c29-8743-eb05887ccfe9 | -17.01039 | -47.77578 | 2025-11-16 04:10:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d126810a-77d3-3c85-9513-8ae52d52a84b | -13.3114 | -47.3802 | 2025-11-16 04:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60d832f0-6611-3f77-bf5c-db67221c6984 | -14.71085 | -48.09594 | 2025-11-16 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc3e0a46-e7a1-34fa-a8ac-e92e2d1ec08e | -12.66428 | -47.16468 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52694169-abd0-38a1-af15-a1b77af91748 | -12.66265 | -47.17414 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d877b19-261d-3e51-a122-fbd859d77b6f | -13.81799 | -44.44918 | 2025-11-16 04:10:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6945e780-30d9-3375-bf0c-bd910783da84 | -13.87018 | -46.84875 | 2025-11-16 04:10:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a372c875-b224-3d07-87ef-280ed2eb8992 | -18.71387 | -43.00544 | 2025-11-16 04:10:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4abaf33-d236-3e0e-96c4-97a024fad13d | -15.3789 | -39.31017 | 2025-11-16 04:10:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5961275f-e7a9-3084-9787-6b1b2dffae85 | -14.48974 | -46.6294 | 2025-11-16 04:10:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ea8294d7-6b43-3c6d-ad1e-4efe058f65c0 | -15.47326 | -43.1913 | 2025-11-16 04:10:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a9f18cda-a6c4-37a3-82e6-9a7d06ebdf29 | -17.53476 | -46.63176 | 2025-11-16 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12ef2498-ea79-35da-86d5-dbf525b07958 | -13.3988 | -44.14511 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 638b139c-5275-3c19-b799-6e6e315b436b | -12.85719 | -46.43048 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b80dc05-f18d-3d0a-8846-b72a81c120be | -12.67486 | -47.17144 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8088ef31-7ec3-3bf1-af7e-bc5addd2e6fc | -14.65665 | -46.58086 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6a8914b-4683-34d9-9088-af20ff79d457 | -12.85503 | -46.42125 | 2025-11-16 04:10:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3be82e78-c9a7-3616-ac07-0038d04533b3 | -14.64524 | -46.57304 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cb5ef38-1945-32b5-b52a-0eb024382f71 | -12.67947 | -47.16743 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1763fba4-444d-351c-aa43-8cef356545ef | -12.8058 | -46.44493 | 2025-11-16 04:10:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16bad8ee-169d-3ca7-b633-1a6f72ec7eb7 | -17.77882 | -43.86459 | 2025-11-16 04:10:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6de878c-ecb6-3a8e-914d-a590a3717656 | -12.86166 | -46.78149 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2d76329-759c-32f8-a0f6-286190ca5109 | -13.79346 | -46.90349 | 2025-11-16 04:10:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d763f20f-53f1-3a94-87e0-3c4dbe227b2c | -16.34879 | -46.64702 | 2025-11-16 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cf78765-691c-3cb1-b736-713a9ad385b0 | -14.68108 | -46.54629 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36d726fe-cbd9-3504-89d3-ffd51b4b2490 | -13.86806 | -46.83921 | 2025-11-16 04:10:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d17edbdf-5eca-38e0-a77a-0937712cc341 | -16.47413 | -41.10412 | 2025-11-16 04:10:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d837d02e-e248-38a9-955b-95da4bd2e083 | -13.55789 | -44.10447 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb251777-0d71-3c37-81cf-ac28a9c86544 | -16.34948 | -46.64297 | 2025-11-16 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49a03b73-e476-397a-bb0a-73c93c22dee8 | -16.56292 | -47.60393 | 2025-11-16 04:10:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26074748-2866-3e29-a719-f069299349de | -14.64309 | -46.56384 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0dfc3683-9d28-3d62-bf48-c8002830b251 | -14.64453 | -46.57725 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6708ee6-021b-313e-bf43-4fc4d53e1430 | -19.13708 | -48.73088 | 2025-11-16 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a217920-4cb9-339a-a77f-f099643da09d | -14.66688 | -46.54314 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 06f51429-c14d-33a6-ab1a-714b05aeeca5 | -13.97611 | -48.7755 | 2025-11-16 04:10:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README45.md)
