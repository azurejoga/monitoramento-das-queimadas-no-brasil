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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 245f422d-6552-3149-8712-f9a911357e67 | -6.9304 | -43.7023 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48fe6644-76ef-34c1-98a1-a98936072215 | -6.41391 | -51.2316 | 2026-07-08 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af4f35ec-6e7a-3d24-869b-494748264a82 | -4.34929 | -47.76794 | 2026-07-08 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7182dcd-57e4-3360-8308-45fbd022f5ff | -6.9233 | -43.70135 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 832f7f1a-878a-3259-ae37-76791aaf6d17 | -6.9455 | -43.69706 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 65943f14-7605-36ad-b8f2-d9c7147e3ea0 | -6.94369 | -43.71128 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c7a60980-759f-3fc2-87ae-dc2ae2c70c8d | -5.66708 | -44.30729 | 2026-07-08 05:10:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 01a838dd-0125-37be-b235-0385f6e24b54 | -5.30791 | -47.24552 | 2026-07-08 05:10:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d0eb652-7805-37a4-8a58-9565e281d0f9 | -6.9224 | -43.70845 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 494e7379-d9cc-3e1e-ac16-5189f146f45e | -6.93748 | -43.70337 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a9103e3-6d3f-3f99-929e-bc3340ca5309 | -5.6619 | -44.31679 | 2026-07-08 05:10:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0494b9bc-54c8-3eb5-91ce-a8479c4b8b1d | -4.34881 | -47.7713 | 2026-07-08 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c2f04a7-1909-3865-9e47-f796c162808e | -6.22994 | -55.62902 | 2026-07-08 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 319d5567-e957-3547-a4d8-f286f6e8028a | -7.64447 | -50.02064 | 2026-07-08 05:10:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d0d502cb-7fa4-365d-87aa-4fa2984d22bb | -7.89691 | -48.25707 | 2026-07-08 05:10:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 197363a7-9701-3e8c-a670-36ffbb1b23c4 | -5.33828 | -44.71267 | 2026-07-08 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96d9c02f-a1b9-35ff-acf2-61ad054ed9f9 | -4.34399 | -47.76706 | 2026-07-08 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e70420eb-22b4-3381-9257-34795c844cf6 | -5.79972 | -43.79928 | 2026-07-08 05:10:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d22bc518-3c73-3781-8de0-c34f907c0928 | -12.13665 | -48.25751 | 2026-07-08 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a638a8f0-6cb8-3431-a7d6-38e25e8b04e1 | -13.33758 | -54.37528 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da5150ce-ab53-39a1-abc7-da3536f72ae3 | -13.3285 | -54.38398 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cfeae6c-7881-3781-9511-a5a53e5a842d | -8.73688 | -49.44915 | 2026-07-08 05:12:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 712ca358-3367-3b13-b742-b326c5f375af | -9.37498 | -44.72693 | 2026-07-08 05:12:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4868e575-6f13-3d25-801a-f55106130473 | -9.37579 | -44.72026 | 2026-07-08 05:12:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 215df6e9-327c-30af-a64c-3115d9910583 | -9.37214 | -48.80802 | 2026-07-08 05:12:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47851e0d-f88e-3943-a9c0-6243616a6645 | -8.73727 | -49.4462 | 2026-07-08 05:12:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1bb18a1f-6319-3fd0-91d7-79fc30de0f82 | -13.53521 | -52.94374 | 2026-07-08 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bce3def-cb9e-34c0-9544-a0d4c1336036 | -9.56904 | -49.10492 | 2026-07-08 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbe1e1df-53c2-38a0-818b-3fcba190da1a | -13.28047 | -54.40582 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 77012993-c449-3724-91c2-da06cdf9fdaa | -9.33624 | -47.91462 | 2026-07-08 05:12:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5408350a-b726-3d62-935d-883050c6bffb | -13.33625 | -54.3851 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e302f2ee-0b93-34a2-900b-eb49dfc0fc18 | -8.72802 | -54.54721 | 2026-07-08 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b46cc901-756b-3f2c-96ca-d776635fc035 | -10.03662 | -49.62439 | 2026-07-08 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 370c96b0-76c4-33f5-b302-07a941182f97 | -12.84645 | -58.30794 | 2026-07-08 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20eb5ae9-341f-3fdb-8ee7-330a2f4abfc1 | -13.91426 | -47.34499 | 2026-07-08 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 621d5796-f94b-32e8-bc81-f3cba61db274 | -9.36639 | -48.81059 | 2026-07-08 05:12:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a71bebbf-a278-3f7c-b9f8-cdaafa10ee16 | -9.73891 | -49.03288 | 2026-07-08 05:12:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 50f03dcb-fac3-39de-80cc-a38820042c0d | -8.73224 | -49.44534 | 2026-07-08 05:12:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3071e3b-c26a-3a36-b511-56fcaf7541bc | -13.91377 | -47.34958 | 2026-07-08 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d53f9d3e-99e6-36c1-a5c6-60cc5c6a77ec | -9.26196 | -59.81683 | 2026-07-08 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18d8947f-f5f0-31e5-801e-d7b34f711e2c | -9.30893 | -51.92029 | 2026-07-08 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6fbfc2c2-b240-3ca8-88cd-e0432bf81c30 | -13.94999 | -45.22812 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e2e23bab-60ed-3888-823b-9d94f2569974 | -13.77059 | -46.28484 | 2026-07-08 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9b5ab353-79e7-3255-8e10-5e95e5eaab82 | -12.35346 | -47.42619 | 2026-07-08 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b6b9f90-4882-3f64-b8ea-d782ccbda5dc | -10.26341 | -59.03078 | 2026-07-08 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d483448-f3b1-3195-b453-f6fb9d6679ce | -12.50377 | -48.25798 | 2026-07-08 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6851f998-1dad-3619-a616-9a77c45d1265 | -11.90995 | -55.90829 | 2026-07-08 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6edfe67a-15e3-30fe-8af4-9259c57c5ba2 | -9.22003 | -48.58469 | 2026-07-08 05:12:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1abb525a-2b0f-3907-b7a5-a75a2005ba6d | -12.13568 | -48.26557 | 2026-07-08 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0011d836-c656-3efb-b116-85d02f314a99 | -10.03623 | -49.62737 | 2026-07-08 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a38836c-ce3b-351a-805c-8e03bcae4056 | -9.33394 | -47.91248 | 2026-07-08 05:12:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7c19e91-6245-3bec-836e-49e303d1626a | -9.22094 | -48.57777 | 2026-07-08 05:12:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 99557baa-8a3c-36a4-93b0-17cc575dfa97 | -13.77487 | -46.29058 | 2026-07-08 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa2493cf-29d1-37cf-80e2-9e0fc0247c22 | -13.33237 | -54.38454 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d7605db-c65c-35a2-9911-1b03bf9e4d43 | -13.53946 | -52.94442 | 2026-07-08 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 743f9aa9-7e1b-3fa3-b434-dab392422b56 | -9.33676 | -47.91068 | 2026-07-08 05:12:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a58bfa5-455f-373a-a163-b5b4b6d3e414 | -12.13616 | -48.26162 | 2026-07-08 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb781347-b9a6-32e2-abd1-e4a6b7aefe50 | -13.27911 | -54.4156 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 56da9973-2156-36fe-a2c0-0b61668b5138 | -13.54 | -52.94027 | 2026-07-08 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3fceef2c-3d9d-3c43-aab4-fce506024310 | -13.76885 | -46.28406 | 2026-07-08 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 085ccae3-354a-39ab-a8b5-2e7582e2ad54 | -13.27851 | -45.1721 | 2026-07-08 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5485ecda-0d14-3f9f-9294-f94efe5b0a71 | -13.47349 | -49.91415 | 2026-07-08 05:12:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 767c04d2-d276-3a47-bc51-517fb4520f8f | -13.53096 | -52.94303 | 2026-07-08 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70bce33c-16d5-3032-b08f-d2a60e04948a | -11.80576 | -52.52866 | 2026-07-08 05:12:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 043a8cf6-f424-3690-8673-4b4caae4e5d8 | -12.36007 | -47.4222 | 2026-07-08 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3b47106-b68a-3dc8-b0a0-f68052cd030d | -13.34146 | -54.37583 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0ef90b1-26a4-33c6-9abb-a8b3893ab10f | -11.32562 | -54.47861 | 2026-07-08 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 187d19a0-7f1c-33b6-b97e-634d23f0afcc | -8.59723 | -48.01394 | 2026-07-08 05:12:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90062bcf-7e2b-386a-ab9a-95cb831df554 | -13.34534 | -54.37638 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1b9ee6d-2b13-36c4-91fe-4b527c008f0a | -9.5047 | -58.38316 | 2026-07-08 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf705c0f-990b-3cf1-a652-6b98643ea302 | -12.35401 | -47.4215 | 2026-07-08 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3279922-30e1-376b-ac9d-d290c75a1210 | -9.78095 | -63.50396 | 2026-07-08 05:12:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d36a288-2643-39ff-a3dc-bda97c087b29 | -9.33909 | -47.91729 | 2026-07-08 05:12:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 054d7098-c16f-33ad-b33b-c769e512d682 | -13.94932 | -45.23515 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97b88892-ac21-3383-8808-4b82375d3cd7 | -10.48327 | -54.7988 | 2026-07-08 05:12:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f26b228-f193-31b6-a3ef-b70fce58aafb | -10.25677 | -59.02971 | 2026-07-08 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 574a506a-9a12-3a68-ab32-5046edc98c0b | -9.22048 | -48.58123 | 2026-07-08 05:12:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 10effc53-6f03-3798-be6f-e0bbfec9a78d | -13.2855 | -45.17307 | 2026-07-08 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 497577ea-dbe9-36aa-a464-5f14e5905de1 | -9.7385 | -49.03611 | 2026-07-08 05:12:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 233020bf-888d-367b-89da-ea9c80469881 | -13.28433 | -54.40641 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2ca9099-86da-39e2-82ae-ac1f9dbb20bc | -12.35529 | -47.42213 | 2026-07-08 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5120e3e8-e3ef-38ca-b9b4-7df9e074b080 | -13.28482 | -45.1798 | 2026-07-08 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e32bfa9f-59f0-3905-9388-a930273d17a9 | -9.37659 | -44.71844 | 2026-07-08 05:12:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 469cd212-c04d-39a1-8f09-661ecd4e228e | -11.96594 | -46.95193 | 2026-07-08 05:12:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82e4c4dd-8397-31f2-8a1c-5ebcc8db7e69 | -13.76826 | -46.28989 | 2026-07-08 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0bc63cb9-ab28-361f-a350-20cfacf91aff | -9.37583 | -44.72512 | 2026-07-08 05:12:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0ecd70a-163b-3b2d-98d8-5ce05761ec1a | -13.47835 | -49.91806 | 2026-07-08 05:12:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28648c18-5584-3f5b-805f-14b76aff76e0 | -13.2882 | -54.407 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9b6d437-2c40-3677-b159-4d1f8ba6ae81 | -13.95767 | -45.22212 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6cd77145-9348-32a7-a0ae-b8ad6e88b080 | -9.2318 | -48.57866 | 2026-07-08 05:12:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 76aaa5c0-f819-3944-9a21-3611a278e14f | -13.29593 | -54.4081 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45fb1c33-c877-3077-bffc-7da5f600da11 | -9.30467 | -51.91947 | 2026-07-08 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 795d4e34-e664-3587-b55c-776524c0893a | -13.27979 | -54.41072 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3388c704-2427-3c2d-bc6a-87b1bae40823 | -11.32629 | -54.47396 | 2026-07-08 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9b04a202-5115-3ccb-bd95-a0068729d351 | -13.28502 | -54.40152 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 296b68a5-c510-31db-a3a9-c48fd7658d72 | -13.95111 | -45.23488 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 29d2f225-8dd1-30f9-8631-36b3597c8241 | -9.30952 | -51.91611 | 2026-07-08 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a510519-d881-313e-a119-a4fb2c0725cf | -9.22591 | -48.58168 | 2026-07-08 05:12:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c493c858-dd32-348e-8776-94fc52c39275 | -12.49849 | -48.25308 | 2026-07-08 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85ee3d3f-fbdf-3c4c-9e65-00df2ad9a2ad | -13.54053 | -52.93612 | 2026-07-08 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README21.md)
