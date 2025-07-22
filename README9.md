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
| 5438339c-90a9-3ac1-a9c0-1d8532080d62 | -13.68826 | -45.6805 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7132a7f8-7f0e-342e-b24e-07b7ea6097fd | -11.73065 | -48.18501 | 2025-07-22 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ef01cd25-36c4-33b2-acea-e48f16430e30 | -15.91716 | -42.61402 | 2025-07-22 04:02:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a3b2f82b-c22e-3473-a756-da2912589a7d | -11.73517 | -48.18586 | 2025-07-22 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 77894ca4-b468-3642-b612-c2e43a0204c7 | -11.46151 | -48.16221 | 2025-07-22 04:02:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bcc3be3b-716e-3227-b30c-34075c04b4e1 | -8.51377 | -43.30047 | 2025-07-22 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 0dea8ca2-dc57-3f58-a917-f4c9187a7e69 | -14.38463 | -47.75827 | 2025-07-22 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c094bdf-1791-3134-b373-396385ebb3a4 | -11.729 | -48.19423 | 2025-07-22 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 551a1d8d-5bb1-3667-bc35-eeb8ea138790 | -8.58496 | -44.32109 | 2025-07-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a888cb77-8936-3e1f-996e-c335e0ed2b0e | -13.67777 | -44.22246 | 2025-07-22 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc8e2bf9-718e-3fa2-a804-9217cc56854a | -15.9287 | -43.51664 | 2025-07-22 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 580d66ac-5b08-3bcf-ada4-95910b43701a | -13.89431 | -44.01786 | 2025-07-22 04:02:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51fb27d1-9ce5-30c7-b5d9-588e1fad0cf2 | -8.91557 | -47.35775 | 2025-07-22 04:02:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3326682-4f6c-36cf-99e2-6590338dcfa7 | -10.61324 | -45.2389 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b6b5af1e-53e9-39e7-b819-e0553e9208ff | -10.61023 | -45.23349 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed8d2291-95b9-3731-9867-a15623c26947 | -15.78694 | -43.40124 | 2025-07-22 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a04c88bc-64ac-330d-8dfa-656ec54d4450 | -8.46908 | -49.61923 | 2025-07-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0444d02-5a75-35f6-a851-d0b2802f9b36 | -14.38196 | -47.74913 | 2025-07-22 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b8e8630-7d50-3f24-9f7d-6468f9e5e6bf | -7.51857 | -49.44547 | 2025-07-22 04:02:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 120730f1-eed2-3ddc-a3c6-e24aca6c9b5f | -15.78635 | -43.40489 | 2025-07-22 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ae3eeec-35b3-3774-9f87-fe383ab5c5e5 | -9.91636 | -47.83248 | 2025-07-22 04:02:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10e6b264-61e4-3035-9b3b-94a34bc940ea | -10.56148 | -50.38142 | 2025-07-22 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b68be4b4-31d0-3893-b997-fe2420bff3a9 | -8.58051 | -44.32491 | 2025-07-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f55ceddc-7e59-36a5-aa72-e1ec5a7d72b5 | -13.66609 | -46.53004 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 206de325-dc83-33cf-aeaf-4913b2cd0d37 | -9.67696 | -49.90137 | 2025-07-22 04:02:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b87887e-c464-3650-b092-8454ebc73a94 | -9.57159 | -44.51266 | 2025-07-22 04:02:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bf14023-98e6-32ab-9a95-f5209dda8104 | -11.48735 | -43.22937 | 2025-07-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 164d456f-67e9-397d-b9fb-0678f27139e8 | -11.767 | -44.30482 | 2025-07-22 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 813f530f-2867-37df-8352-e5259329f3b2 | -15.56129 | -44.75956 | 2025-07-22 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcd9ed62-b069-3a67-86ae-d05398a9a1b7 | -12.46507 | -45.85781 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab387a9c-2059-38b5-8063-7c25ef46724b | -10.2284 | -48.06652 | 2025-07-22 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b266ec5-cb70-365a-bb9b-243017c694be | -14.38617 | -47.74979 | 2025-07-22 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7417f0df-0bd0-3d56-9da6-16dd06d4690e | -15.61846 | -41.33488 | 2025-07-22 04:02:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b4b824d3-65bc-3acd-9692-bee6a81f482a | -8.58125 | -44.32045 | 2025-07-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ae6980a-abfa-3769-a2ce-5b17e56387ac | -11.90716 | -44.07155 | 2025-07-22 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1efd5603-7ef9-3140-a102-520687b9e47a | -15.56197 | -44.75554 | 2025-07-22 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc56ba53-ce17-3f4b-bc75-47fca97d1310 | -9.5753 | -44.51328 | 2025-07-22 04:02:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fd3f116-de99-31ea-af15-2d8adef2d960 | -9.49414 | -40.56598 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5e56d414-2fd7-3b1e-b5dc-208a366867ba | -11.72983 | -48.1896 | 2025-07-22 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ec0acb14-22e1-32a2-b203-1aa3b1383920 | -11.56809 | -44.84117 | 2025-07-22 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b789ca9-12a3-35f5-bad3-463629fe2b3f | -12.68154 | -45.65919 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cebcf6c7-515f-3027-bee5-ae562b889e9b | -9.62887 | -40.59492 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ae99971b-2c1a-3362-b425-aacf9f9ce4b7 | -9.4936 | -40.56946 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 23036e19-b8f5-3851-8e0a-b72b73efe3e7 | -8.51246 | -43.30847 | 2025-07-22 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| b888a0ef-5827-36c6-b465-81847fda5b2e | -11.86115 | -44.51244 | 2025-07-22 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 38dfb210-2fb2-37dd-9812-6eeb3bb4e687 | -11.81216 | -44.26919 | 2025-07-22 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f61e8593-90ac-3f22-b272-d80276747645 | -11.5695 | -44.83893 | 2025-07-22 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7e13446-ca84-3ca1-9c6f-0db5a80ac20e | -14.38037 | -47.75784 | 2025-07-22 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5ad69cbb-25e2-3308-b044-a98cf03765cf | -9.50021 | -40.57051 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b177bd47-5e8b-3d98-8178-c28f53ab355d | -10.63085 | -45.22738 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11eda9ff-b85e-3246-9c1b-ca0c14819bbf | -14.77693 | -48.28459 | 2025-07-22 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25abf54c-a6bb-3e0c-b4e6-d8d431e58950 | -8.28863 | -44.96378 | 2025-07-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09f1cfc3-583b-33ed-9d29-7efcf0c3854a | -13.65032 | -45.72139 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 732fad99-7bdb-3d73-9b62-f2c4ff8e1f36 | -12.65399 | -45.05509 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4de6c427-e900-39c1-9e65-4694be9fcd0c | -8.28922 | -44.96589 | 2025-07-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e265c91f-4e07-39d1-8023-c2beb6c76094 | -13.69279 | -45.67657 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b0f2cf31-4d67-3683-9897-1f0b2909abef | -15.61513 | -41.33433 | 2025-07-22 04:02:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 84d292ff-f9d8-36a1-a30f-693f251e5f8c | -13.69631 | -45.70102 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59825691-63a6-30e3-b998-d20a8f7b30d2 | -14.21007 | -43.96078 | 2025-07-22 04:02:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55feca93-fae1-3279-945d-8db23d71d8dd | -12.25885 | -44.77658 | 2025-07-22 04:02:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4224bb30-0432-355e-b117-17144d2fde07 | -12.4762 | -45.87194 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1203d5a-0536-366a-91ce-5d0338f5d6b7 | -13.65408 | -45.72203 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 431e6a09-d9f4-31a2-80bd-075f68b4abbe | -10.62706 | -45.22667 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6ee6fb92-24e1-36c6-8478-9e4703bc8b96 | -12.71437 | -47.80003 | 2025-07-22 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e66bac17-d951-3f31-a1aa-2a6e082d3eeb | -14.6445 | -46.8303 | 2025-07-22 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 05a8917e-22c2-3158-8489-bc308d80ff29 | -14.38885 | -47.75893 | 2025-07-22 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a214c52-456f-353d-b92b-b0de312c6674 | -8.91637 | -47.35321 | 2025-07-22 04:02:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c96692a9-27d6-3065-93ee-70f58962dce1 | -11.57101 | -44.84621 | 2025-07-22 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc822019-fe54-37b5-b0f6-93d6693ea363 | -14.64356 | -46.83552 | 2025-07-22 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 15a35bf2-f923-3a79-a1f4-f540f7d97bf5 | -15.9307 | -43.51591 | 2025-07-22 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d69b2851-8bd6-3c76-92da-55863c779f1e | -11.57317 | -44.83957 | 2025-07-22 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85108d27-650e-32ac-a5fa-b17c1acc2f2c | -8.37596 | -47.6144 | 2025-07-22 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 451d8fdc-fec9-3e13-807c-294135b02bd4 | -11.30599 | -55.1193 | 2025-07-22 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ccfcb36-5c42-3382-b802-6d3d098d7bed | -13.49182 | -45.51225 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe87ee9b-d5fc-3855-ab4a-56fa1113821c | -11.81146 | -44.27331 | 2025-07-22 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc01baec-b826-3ba6-927a-a35f0ced5632 | -8.51024 | -43.29988 | 2025-07-22 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae88ed78-ec9f-3139-9ec6-1aba98a421b6 | -8.29393 | -44.96171 | 2025-07-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86ee038e-b96d-3eb4-8cc7-cd56538cdad3 | -10.77501 | -46.78305 | 2025-07-22 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d92b57e2-441a-3ff4-ae56-ccc2491482bb | -9.57084 | -44.51709 | 2025-07-22 04:02:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0edb9c43-c508-3ff4-922f-5560ba4caaf6 | -13.64871 | -45.7307 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b9d1fca-0600-388a-875b-2441beeedbe4 | -8.51311 | -43.30447 | 2025-07-22 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| c93eaedc-e332-3fe8-b98a-283cdd8219e0 | -11.18939 | -48.62071 | 2025-07-22 04:02:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 02f5f92e-f979-3335-a800-be72e647771b | -14.37959 | -47.7621 | 2025-07-22 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b624472-7d68-30b7-a5c2-91dd914f49fa | -11.75961 | -46.29499 | 2025-07-22 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 239fe139-681a-3a94-9249-577652de541e | -9.91268 | -47.82677 | 2025-07-22 04:02:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6664658-ca98-3e52-b5be-ed945c1233b5 | -14.20727 | -43.95633 | 2025-07-22 04:02:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4e66295-ca35-3a98-9f91-01b4abde8102 | -11.50076 | -47.27338 | 2025-07-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74a81185-08da-3550-907a-eb7c8ff32e54 | -13.69178 | -45.70496 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6021e5f8-afd1-3275-a94c-903424433492 | -10.62246 | -45.23067 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a2f8ad3-7ba5-37d6-b885-211b304c22ef | -9.06148 | -45.06474 | 2025-07-22 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5b7ffa5-93eb-359f-91b3-f315f6c88e9a | -13.30399 | -42.40034 | 2025-07-22 04:02:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8a3d47d9-b94a-3cf0-8ceb-304c488b27a4 | -8.51599 | -43.30906 | 2025-07-22 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f6d380d6-51db-3fde-aeb6-673073da4e4b | -10.61786 | -45.23476 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d3fa0f58-3ddc-3705-b9d0-61509c298834 | -13.49475 | -45.51751 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c170f31d-b9cc-3b0e-aae6-9fde97072a26 | -9.91721 | -47.82769 | 2025-07-22 04:02:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38390604-df4b-33bf-b4b5-f6c3e11bd27a | -14.19347 | -45.33818 | 2025-07-22 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 739553cb-347b-36c9-938c-ee447fa3f2a1 | -8.92174 | -44.45001 | 2025-07-22 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9fd9214-7942-3cd8-bfb2-0e3537d18e63 | -10.55614 | -50.38036 | 2025-07-22 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7a3ad17-3445-3d1a-9ddc-7f4067e2d7e1 | -9.06065 | -45.0696 | 2025-07-22 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d1f2917-c0f0-3cee-ab64-ec967891b83d | -10.67851 | -46.76245 | 2025-07-22 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README10.md)
