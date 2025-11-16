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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bcf0405-308a-3094-abe0-e34b04da4de6 | -4.09625 | -43.35076 | 2025-11-16 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4a16f0d-d9d8-3bde-add1-920c640e6062 | -2.68609 | -49.08239 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d382ba74-c517-3322-bb0a-c5ff3f02f9cc | -1.9401 | -47.04088 | 2025-11-16 04:06:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef7cd4f8-5c47-3286-b0c3-d2309dfc4dd0 | -2.88582 | -53.29134 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a6e5a152-abdd-39e0-8e0f-1914ddea2d11 | -3.45241 | -51.02947 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d077af1-fc1f-3a24-95cd-2625389dc261 | -5.21843 | -44.51355 | 2025-11-16 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01a4df7d-9785-3e03-9168-df6104261652 | -1.16454 | -49.20572 | 2025-11-16 04:06:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36f4cf69-34ee-3d10-a950-bb8dc111e9ac | -3.34625 | -45.54661 | 2025-11-16 04:06:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d576ed1a-435e-38f0-9619-fd6c6926ea10 | -5.48225 | -40.97441 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 989e6622-1cf7-3608-98ec-6dc00b6a85d4 | -5.48501 | -40.97837 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1fbff4d-cec1-3648-b5d9-08d637410458 | -5.47234 | -40.97285 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 771fa69c-5be0-3a06-9a4c-856f7b7b6c4f | -5.03813 | -42.74933 | 2025-11-16 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f1de5ee-a0c3-38cc-9926-6adbcad7dbda | -1.19321 | -53.73382 | 2025-11-16 04:06:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a913e752-15bd-3639-98a6-7d304ef58775 | -5.09073 | -41.47368 | 2025-11-16 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad00f5d0-ea0f-3afd-9857-32868fdf4a82 | -5.34273 | -43.04284 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b3b073ff-19a3-3350-8bdb-3b4c1c252249 | -4.89067 | -45.01957 | 2025-11-16 04:06:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aaa048a0-fe9c-3a10-adf7-ed8cdd4ab9f7 | -4.8045 | -41.69339 | 2025-11-16 04:06:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e047984d-7ebd-33a5-9437-3dadbe848c0e | -12.06689 | -48.22252 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0a408b0-906f-3774-8ff9-e44c8e4a3481 | -8.06585 | -43.10564 | 2025-11-16 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 47b4523c-446f-3f5a-a5a5-5d6282eb589c | -5.58039 | -46.14406 | 2025-11-16 04:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6ed9a3f-c8bc-3738-bbe4-9e1c1a57973e | -10.00262 | -44.76548 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36dd9d63-f193-3694-953c-4bac6fb2187a | -8.90314 | -44.43467 | 2025-11-16 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 058fb645-10d6-3459-b54b-f151f4452130 | -5.99622 | -41.91499 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c71ba33-87b1-30af-bf93-7942077892ff | -7.05112 | -43.95096 | 2025-11-16 04:08:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cad98b4-14f4-3360-b580-ff424d7f69b4 | -5.92484 | -42.25664 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4adaeed1-e4e6-372a-a7f9-c4292c311701 | -13.30162 | -42.96347 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 68af156a-8678-329b-a9d8-f7297b768dd4 | -6.86062 | -47.35902 | 2025-11-16 04:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0b65609-068c-32c8-b4b2-12f54787a354 | -12.4029 | -48.09361 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27d364f5-b989-3484-85f5-9939acc86459 | -10.83226 | -48.0346 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6626698e-14d1-3772-bea6-c7ab95473464 | -9.34208 | -46.57661 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af22d526-b290-30f5-84f3-6b01d16905ab | -6.78046 | -44.29594 | 2025-11-16 04:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b16c4c0-8b56-30ca-820d-eb7cee668b63 | -6.28912 | -41.75974 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 120fe91d-ecc9-37ee-9f26-644eb49a95a4 | -12.45947 | -43.79338 | 2025-11-16 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1e91107-8fc5-36ec-9f74-a0314f0a4a1b | -6.31705 | -41.82025 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 38c15eae-646f-318c-886f-fbe86451cc19 | -12.20559 | -49.61375 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 149867ba-9b55-3bdf-88dd-e15ae4ccc44c | -6.77706 | -43.54526 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91ec9baa-2b8a-3bb9-aa50-e2bd0b652c5b | -9.72299 | -43.96341 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 083488e6-f6b0-3741-accd-25750282d06a | -11.15832 | -49.45098 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 12a0cd6f-29fd-3df0-9ee3-3f0db835b657 | -8.72833 | -44.10526 | 2025-11-16 04:08:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c67ac793-8d17-3ce9-922d-0b154fab300e | -12.65144 | -43.25079 | 2025-11-16 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68e66efc-9494-3edc-9e0e-3d37d12fa818 | -12.65885 | -47.17348 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94490328-cd43-3fe7-bbea-cecf154bbbd4 | -10.62949 | -44.60107 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 198000f7-5163-3117-a8ee-db8eca3a89a8 | -7.04356 | -42.25289 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26f79e91-4c3c-3f60-a160-210722d926d1 | -12.04604 | -43.50998 | 2025-11-16 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 57aa267b-d8b4-3c48-b9ef-504f06fec710 | -7.22042 | -47.98196 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d9b3605-dd8b-3db4-a7c8-dff44280bded | -9.44997 | -44.86272 | 2025-11-16 04:08:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f5e56f6-7b83-3ad7-b990-4d9c8fe9a04e | -10.80346 | -47.98972 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c302604-6553-306e-90a3-81c9d2873839 | -12.40483 | -47.54944 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a087dedf-5a94-3a1e-87d1-1cfe32b5a439 | -4.8373 | -47.54905 | 2025-11-16 04:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23e6ccd6-cbdb-3c0f-8377-a8384cc7e473 | -6.57478 | -43.79827 | 2025-11-16 04:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db186fa4-d7a0-3b7b-825a-b32a76ba6b4e | -9.74432 | -43.96693 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 466040b5-7d8f-3871-b048-53a5c600266b | -11.79303 | -48.08849 | 2025-11-16 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17935987-1069-36b2-a403-602581eb3762 | -8.20845 | -43.56857 | 2025-11-16 04:08:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd387f06-09b5-37b2-b41f-ac405ef8e767 | -10.54471 | -44.11246 | 2025-11-16 04:08:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13052b62-d931-3ce5-912f-b4d2a5ca77a1 | -6.44927 | -47.27681 | 2025-11-16 04:08:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2c937bd-2a29-3686-bf6a-df3122f45300 | -8.745 | -48.31586 | 2025-11-16 04:08:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f83e3c06-b8a4-361b-a103-7199e2cc7816 | -5.22015 | -46.92146 | 2025-11-16 04:08:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 128d5434-bf5f-3299-a10f-71e13c743b63 | -8.55433 | -41.37601 | 2025-11-16 04:08:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 00e3cb24-1cfd-33dd-932b-dae40dc5af9b | -5.44825 | -47.01223 | 2025-11-16 04:08:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 319eb45f-b157-3e79-a17f-16613a138ab8 | -10.54692 | -47.92286 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f564b6bd-8dcf-380c-b428-28a5e708f52b | -10.3924 | -49.05721 | 2025-11-16 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4955a651-9f00-3c48-82f8-9c97e0842f9e | -9.02489 | -46.87774 | 2025-11-16 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f4c6ac4-1a5d-3901-94aa-64efbb3c7181 | -6.45062 | -42.36882 | 2025-11-16 04:08:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| bf960e3a-c25b-3cb8-9dd2-c5075a19d3bb | -4.80643 | -48.3423 | 2025-11-16 04:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 425e4d97-f58b-34be-b031-26fe2647a241 | -8.45868 | -45.13976 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cab5cec0-62de-3e7c-8845-d3514fc7df70 | -8.10164 | -46.03725 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0abd10d5-6726-3478-8fa6-d9032934217e | -10.82228 | -44.64918 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c212f3dd-cf69-32bd-95d2-2f60349bbff7 | -10.0007 | -44.77717 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf16df3a-c83f-3952-a63a-4a7f54a08836 | -8.86878 | -44.40512 | 2025-11-16 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5712471-7a35-3f02-a8a7-730ed58ff437 | -10.70277 | -44.52006 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9623751-6064-364e-8e53-82d8008fb4e3 | -6.69848 | -40.79899 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 964b74e1-f086-3f5a-8a3d-2a6b3fed5dda | -11.41884 | -43.33054 | 2025-11-16 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4693e910-6bec-35c0-9c8f-fdd7131a0b63 | -6.54239 | -38.17479 | 2025-11-16 04:08:00 | NOAA-20 | LASTRO | PARAÍBA | Brasil | 2508406 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| edd970bd-4eca-3989-8c64-d58c461aeea8 | -9.05846 | -44.79535 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5e9781a-caf3-3b41-b267-02622483ffca | -5.63005 | -43.92814 | 2025-11-16 04:08:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 17c670c3-d716-317a-a5e9-803e31489a83 | -6.39895 | -42.28915 | 2025-11-16 04:08:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a347ec8f-3540-3ab9-9ccd-67cfaa468307 | -12.67747 | -46.77461 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbb5a9aa-55b4-32f9-a246-9f12b123289f | -7.09195 | -42.73858 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dd515d87-cd8e-3343-963b-624679d72145 | -4.838 | -47.54492 | 2025-11-16 04:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6027ab3b-b42c-3859-9247-a3128b0e9023 | -11.78959 | -44.16677 | 2025-11-16 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 285204aa-47cf-349e-a1c4-29dc758ccfd0 | -6.14533 | -43.35003 | 2025-11-16 04:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3b81f2d-5b11-302a-b6ad-39533fde2c61 | -9.74673 | -43.95224 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 538e1a5a-09bb-39eb-ad31-5e6029b30899 | -6.77746 | -41.44448 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bcdb23bc-af26-33ad-bec7-7c3c1788428b | -8.31355 | -45.40942 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27c776f2-8a96-3660-b3be-0bb4c32047c3 | -11.56889 | -42.42658 | 2025-11-16 04:08:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c65868d9-60e6-314b-a5c5-90589bce695b | -12.06259 | -48.19881 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d58ed332-442a-337e-ad88-1b0736090ecb | -7.40682 | -40.06874 | 2025-11-16 04:08:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a204daab-7629-344b-8014-c8e733bd85d6 | -6.58397 | -44.67161 | 2025-11-16 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 400baf0c-8acc-35ed-aa0e-ce0384f9ca2c | -9.14709 | -45.15777 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b94904cf-ed2c-3bd0-8aa9-ad70f6d7aa4f | -7.05458 | -43.95151 | 2025-11-16 04:08:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e7941dd-5086-31ca-9688-41c956c3aeaf | -7.71899 | -47.29021 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b88cdf3-ecbe-3a36-beae-4a50f97f71d6 | -6.36123 | -39.62768 | 2025-11-16 04:08:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 471fdf1a-e81c-3a99-9946-c25ce5e56f9f | -6.06412 | -41.55044 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| beaecb3c-739b-3af0-ac31-75150a12c7d0 | -12.40409 | -47.55203 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 881edbd7-7c86-385f-8824-222f2d783b7c | -10.87249 | -49.54577 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6f34189-ec8a-3403-99d5-0fbcd3be1f0d | -10.16982 | -44.49651 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a3631bd-2ec6-3220-8974-44c81b165c84 | -5.48321 | -44.8405 | 2025-11-16 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4dae469b-7300-3714-b7ff-9106f1dcfe23 | -10.1633 | -44.51477 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3154a75e-6830-3d82-82c4-9eb2ac79cdb4 | -6.66618 | -43.77373 | 2025-11-16 04:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb3078c4-ca0a-37f5-9ad3-821a11d3cf8d | -5.99181 | -41.92139 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README33.md)
