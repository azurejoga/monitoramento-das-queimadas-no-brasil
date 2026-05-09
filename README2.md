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
| f2cd7112-0f5e-31af-b1ee-b9455f43bbaf | -9.64503 | -42.96367 | 2026-05-09 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c75c2049-b10f-3c42-ad10-0ecd7978ee16 | -12.13622 | -40.89455 | 2026-05-09 03:55:00 | NOAA-21 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6e8efc4-667f-3f09-9f63-1e36d9dfc0be | -13.88992 | -43.7645 | 2026-05-09 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f3844ba-6710-3cf3-9f12-397770839d5a | -13.36407 | -43.12635 | 2026-05-09 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 43cb4392-5151-3185-88e4-9933543403f5 | -11.82508 | -47.3298 | 2026-05-09 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0e6a9574-4697-3e99-a8d6-cfd3f197d0c0 | -18.64669 | -46.5073 | 2026-05-09 03:57:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 31e728df-7fc9-3a4e-81f7-315784154328 | -11.4199 | -47.09166 | 2026-05-09 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e262d051-4b6b-3029-b5f5-a031f0ec9738 | -15.76882 | -43.23878 | 2026-05-09 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0b65afd-87e0-3ac7-9330-a78410beba81 | -10.6708 | -49.70543 | 2026-05-09 03:57:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ed6dab7c-328f-3b65-8f26-22c2e46f0d0f | -12.35084 | -40.42187 | 2026-05-09 03:57:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1485a739-27e6-35c9-864d-8aab0470b4cf | -12.85848 | -43.76108 | 2026-05-09 03:57:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2736a58c-ddf2-3c67-b2f7-d61325c02f3a | -11.77593 | -43.65388 | 2026-05-09 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3f6887f5-4adb-3c2a-a756-8891b482b59e | -11.41959 | -47.09378 | 2026-05-09 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50b0a197-d659-373e-a564-16f423da04a2 | -11.82407 | -47.33517 | 2026-05-09 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1d504bf7-df40-35ba-b3e8-9f64934ad349 | -19.21154 | -44.89436 | 2026-05-09 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ceb8afa-72c8-35c1-a4fd-7fdcb1a0b9dd | -11.60025 | -47.10434 | 2026-05-09 03:57:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 07c83584-e744-3645-9c54-6923f2ee135f | -11.77513 | -43.6586 | 2026-05-09 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8b185604-73b2-3c51-ba8a-5b5e6ca2d35f | -13.36121 | -43.12128 | 2026-05-09 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e51e0ea2-d966-39fe-9e39-67162eb4d00c | -11.93961 | -43.37508 | 2026-05-09 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8b53a34-57dc-3803-81f5-9dbb95fbb633 | -14.90003 | -45.18512 | 2026-05-09 03:57:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdf2e5bb-aeaa-3589-b923-0591a919eb76 | -16.41957 | -54.91441 | 2026-05-09 03:57:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18ff1344-6d5d-3875-ad7e-9a42f3384b5f | -14.13966 | -45.38567 | 2026-05-09 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16fe8113-7dc3-39c0-b375-6b908f33b0e5 | -15.7695 | -43.23474 | 2026-05-09 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9b2a0ee-47a4-3ea1-9666-7d1d3a6056d3 | -19.59976 | -40.35288 | 2026-05-09 03:57:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3d1c55f-12ac-3d2a-babc-91d6bb1b470d | -11.94178 | -43.38502 | 2026-05-09 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5c77cd6-22b4-3b60-8e4b-c6c357262cc1 | -11.76972 | -44.09329 | 2026-05-09 03:57:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d3b6d88f-35d4-3918-8f11-5318f63c4472 | -13.36974 | -43.20299 | 2026-05-09 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4a03eb5a-95ab-3c1a-ac59-59bb2083cdd8 | -11.77752 | -44.09466 | 2026-05-09 03:57:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 99ce4732-92bb-3aee-b319-1c40638a7685 | -11.76533 | -43.64724 | 2026-05-09 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1596fb30-cf90-3115-860f-a92cb7564c05 | -11.94335 | -43.37567 | 2026-05-09 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12ae8566-c73c-3c0b-bc9b-d6263936469d | -14.14578 | -45.39831 | 2026-05-09 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 351f078a-d5ab-3595-9155-bfa1b7a1b2c8 | -13.36901 | -43.20731 | 2026-05-09 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b53bdb5c-c9d0-388b-a3a1-6622fae6716e | -11.76832 | -43.6526 | 2026-05-09 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d832856-f74b-32bb-9c53-59776677b49f | -11.77893 | -43.65924 | 2026-05-09 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 120a3542-6afd-3329-8be3-c3b8c06f3d26 | -11.42057 | -47.08853 | 2026-05-09 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5974d6f6-1846-376e-add2-d09e3dc8f8c1 | -11.81987 | -47.33653 | 2026-05-09 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76f2ca0a-8a46-37c7-ba36-227725cb6845 | -11.82084 | -47.33115 | 2026-05-09 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4c9fc40-1869-3bc2-aebd-f07a09816965 | -14.65442 | -40.99874 | 2026-05-09 03:57:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 069fe78b-866f-37c6-8cf4-73130bfe9f4e | -16.41253 | -54.91296 | 2026-05-09 03:57:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 922b03c2-0070-315b-86fc-bb8a748c04e4 | -16.35573 | -43.8814 | 2026-05-09 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11b16211-7f77-36b9-8b92-cbcd1e93d089 | -12.86224 | -43.76173 | 2026-05-09 03:57:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e24ab3fc-5b5a-3b77-9df6-fe6140f320e8 | -15.77236 | -43.23934 | 2026-05-09 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa3a9b6a-2662-309c-b921-67622ec911b7 | -13.68491 | -44.29148 | 2026-05-09 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17cf7537-f7ba-3930-86e1-093bd9c4f7c8 | -18.07592 | -46.3692 | 2026-05-09 03:57:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c66fffc-aefb-323e-be00-f462590723ee | -11.79443 | -47.0964 | 2026-05-09 03:57:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ded22155-aec6-3296-b322-8edfad890e0c | -11.77813 | -43.66395 | 2026-05-09 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d3d3f99-3e89-360e-b467-09c751020e49 | -11.77212 | -43.65324 | 2026-05-09 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5040e29d-8543-3cd8-bba8-56df16fe3de8 | -13.36045 | -43.12573 | 2026-05-09 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1d851e40-0497-335f-9cb5-220cff1b4f21 | -11.93882 | -43.3798 | 2026-05-09 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 813b7f2c-b8d4-3a8c-ad3c-ce081a919f9a | -12.85927 | -43.75642 | 2026-05-09 03:57:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7b7aa9c-75ce-3331-884c-150ef1dd3caf | -18.29329 | -45.13183 | 2026-05-09 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 158212af-c5b9-3b80-a573-b48f25ce34bd | -13.81452 | -42.88912 | 2026-05-09 03:57:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91075e59-e738-3a81-8f3c-f7787714fb87 | -11.94255 | -43.38043 | 2026-05-09 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cd5c455-609d-39f3-b0a8-f1a46a156687 | -12.86303 | -43.75708 | 2026-05-09 03:57:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 32768499-e316-3730-a0d0-58b742033b97 | -14.139 | -45.38935 | 2026-05-09 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e3b1c8e-10e2-39c1-a1c1-d16533d125b3 | -11.9785 | -46.78954 | 2026-05-09 03:57:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f57653ff-e618-3192-aaa7-3b3ae27fb5b1 | -13.66624 | -52.19476 | 2026-05-09 03:57:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| debbd5d6-2314-3d20-95f7-82adcaf5d75b | -11.80011 | -47.09217 | 2026-05-09 03:57:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8c84ffe-7a70-3540-8fe3-5e15a937295f | -13.81097 | -42.88849 | 2026-05-09 03:57:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5eff685e-62f6-3862-a572-b9563dd05ffb | -11.78194 | -43.66457 | 2026-05-09 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cfc3714-1b49-38d9-b359-b4d26b0449b8 | -19.20788 | -44.89367 | 2026-05-09 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89f20f16-5103-3e88-b3bd-a2f060959808 | -13.08524 | -44.20741 | 2026-05-09 03:57:00 | NOAA-21 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15ca897c-e188-379c-b1a7-64662669ac26 | -14.90699 | -43.55832 | 2026-05-09 03:57:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59263c86-dd73-3ca8-86be-3eac938f5e8d | -11.82306 | -47.34059 | 2026-05-09 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fafbea95-3833-32ad-8a1a-bfd749d57a1c | -10.66507 | -49.70432 | 2026-05-09 03:57:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4c8cfe93-03d7-3c54-b297-03112731c6ba | -11.81926 | -47.33428 | 2026-05-09 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d81fc096-9d10-3478-b66c-2d89575d57e1 | -13.81121 | -43.6548 | 2026-05-09 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 666bc3be-4fa3-3ab7-8226-ab52bfa6ccb8 | -15.22397 | -50.85976 | 2026-05-09 03:57:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d60809bf-cc88-3462-85c5-80bcacb6e69b | -22.85612 | -43.08101 | 2026-05-09 04:00:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a49812f0-847d-3bb4-9c4b-2bdab86ea3fd | -22.40915 | -46.62031 | 2026-05-09 04:00:00 | NOAA-21 | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 191e23f4-d51a-332b-889e-5a2bbfff7f34 | -22.67548 | -43.4768 | 2026-05-09 04:00:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 22a03829-f1e5-3a15-8266-6afc3d1057ab | -22.4078 | -46.61706 | 2026-05-09 04:00:00 | NOAA-21 | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 33df1c25-07d6-3474-8c76-59d38fef04e8 | -21.52898 | -47.13593 | 2026-05-09 04:00:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bae74144-e270-30db-92d0-35279b55ee2e | -23.49963 | -47.18357 | 2026-05-09 04:00:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0af91f7c-4080-3efe-bdf6-92280e7a8a86 | -22.90219 | -43.48719 | 2026-05-09 04:00:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 3113412a-c088-3eb3-bb05-ac825ea29689 | -22.41163 | -46.61784 | 2026-05-09 04:00:00 | NOAA-21 | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| bb16c37a-238a-34c8-a5ed-93c8113d2e29 | -22.71178 | -43.63546 | 2026-05-09 04:00:00 | NOAA-21 | JAPERI | RIO DE JANEIRO | Brasil | 3302270 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fbe79c73-156f-3cf7-ae27-d498b46f7c3f | -23.49977 | -47.18632 | 2026-05-09 04:00:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 58efb0ef-6d0e-313c-a43d-ebfebff4b245 | -21.53298 | -47.13671 | 2026-05-09 04:00:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 384d2a33-67aa-3a02-b0e7-7a67368d2078 | -21.53699 | -47.13752 | 2026-05-09 04:00:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33c86ee5-8894-3ce6-906f-a686af898ebe | -21.33789 | -47.03271 | 2026-05-09 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 61f168a1-4273-35c6-91d8-e40c7b34ee44 | -21.12078 | -43.79111 | 2026-05-09 04:00:00 | NOAA-21 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a86c9e4e-3abd-392d-9d0e-a4c61cad1f56 | -21.33458 | -47.02821 | 2026-05-09 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a55a7977-8e67-3938-a731-573ed146ab19 | -19.91353 | -44.04645 | 2026-05-09 04:00:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 82085021-9ecd-3e52-b68f-8bca922cc923 | -21.33391 | -47.03185 | 2026-05-09 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 414a3b5c-3af2-3159-ab93-a137102e6c33 | -21.33925 | -47.02538 | 2026-05-09 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7db1067a-20a5-3800-94fd-c8ace299dc90 | -21.33526 | -47.02457 | 2026-05-09 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f2910568-2a19-3121-838e-a534db1ecd40 | -21.33857 | -47.02905 | 2026-05-09 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8faa4f76-15eb-3cf4-8ce3-9b2b7ad5c131 | -20.25224 | -46.09667 | 2026-05-09 04:00:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e6f2da7-1f05-340a-b8ce-32b86272e1b0 | -21.12419 | -43.79178 | 2026-05-09 04:00:00 | NOAA-21 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 534cb438-0912-3147-8fd1-db66986da7ca | -18.48671 | -51.68988 | 2026-05-09 04:00:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71bf3029-9b38-3e84-a14e-d4525113aa9b | -29.90741 | -51.14829 | 2026-05-09 04:02:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 9d4e323c-7f17-3296-a0f2-7ab6ec68277f | -6.32353 | -44.63842 | 2026-05-09 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a056c3f7-d6e2-3fc5-be6b-90a8c4afbb82 | -6.3285 | -44.62854 | 2026-05-09 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce39943d-069c-316c-a859-c221891b6c77 | -5.78452 | -45.13257 | 2026-05-09 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc2005af-73cb-31ce-9e16-7b3d46c4162b | -6.32408 | -44.63496 | 2026-05-09 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e9a7962-ae42-3469-bca8-fee1788d3392 | -6.32685 | -44.63895 | 2026-05-09 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecb8551c-eaf5-3a71-9b69-4e685116f534 | -6.21965 | -55.64358 | 2026-05-09 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 754b32a2-df71-341c-ad59-1c123e97e1df | -6.18872 | -44.86969 | 2026-05-09 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9996e0d6-a9b3-33aa-ba21-efe4f0179d62 | -6.04809 | -47.89177 | 2026-05-09 04:27:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
