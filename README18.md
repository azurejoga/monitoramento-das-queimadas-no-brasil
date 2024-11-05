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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4bdd5b7-3786-3224-9456-723504c1af27 | -7.26217 | -38.9491 | 2024-11-05 04:08:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 051bb638-ca3a-3926-b264-c900e864f81e | -3.94053 | -45.57109 | 2024-11-05 04:08:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3083fd77-8abf-3b85-9557-838dac120329 | -5.86198 | -42.66268 | 2024-11-05 04:08:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1824d2cd-d988-3ae0-b9b3-052c1b8e7609 | -1.93755 | -46.42995 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de63e972-dc3c-33e3-83c5-caa576a680d4 | -4.02247 | -43.23641 | 2024-11-05 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 261ef952-bb68-3cdc-9002-45daaee8db64 | -5.34604 | -41.616 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbab949b-153d-34aa-9d37-6c240e75092d | -4.67403 | -41.75751 | 2024-11-05 04:08:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df29be12-37fb-3f8c-abf7-05e94b4e46f1 | -3.12036 | -51.10419 | 2024-11-05 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7469f2ba-541b-3815-b417-f030e3e0ffee | -5.43193 | -42.64978 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6703a8bb-3414-3fae-8d8b-676ed0a2007a | -5.97758 | -45.36831 | 2024-11-05 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 685738f4-1733-3b81-941b-10da55059add | 0.26549 | -51.32504 | 2024-11-05 04:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91d8a8e5-e5b0-3151-a80e-5f1474aed7e8 | -4.38218 | -41.70794 | 2024-11-05 04:08:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2c28e8ad-87b6-34c7-b36c-31bfd4049b47 | -4.28443 | -48.64389 | 2024-11-05 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0581941e-b0ad-3c36-b8ce-e2ae390b16f3 | -4.26304 | -50.72689 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f9314a3-94da-3f6f-8ec3-21790e7a1654 | -5.61411 | -43.69622 | 2024-11-05 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f60a5fd4-b72a-3090-9629-0c19b0112d0d | -4.45526 | -42.19513 | 2024-11-05 04:08:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 33fd86cf-db4b-32e3-8cc6-bd8e5e8b8338 | -5.93755 | -43.64887 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbc9f36e-a7f3-3966-9e3e-b2eca601fdca | -2.81043 | -51.49178 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3aa35d13-0b7d-3d69-9a3a-ef20f05378ce | -4.59391 | -49.5201 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7367e7df-8d5b-3b93-a6f2-2010f663301b | -3.11482 | -51.11005 | 2024-11-05 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d6ca5ed-81da-3719-b263-6bbbe798e130 | -6.74969 | -42.07889 | 2024-11-05 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0464e6b3-cf23-32ee-946b-5b16aa5f7b0e | -3.08206 | -54.51323 | 2024-11-05 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 30d93746-adff-3a40-b2f9-c18e9f4d38cd | -4.42248 | -45.84874 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3925c991-6081-3cd8-a322-9d06bd8ea1bb | -5.62346 | -42.44739 | 2024-11-05 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ecba32c-2d4f-3c1a-a3ed-f6d9a8435458 | -7.40695 | -45.56812 | 2024-11-05 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e4e9237-cbea-3fb3-a110-ba647b0cbd43 | -5.30206 | -46.26017 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b2b547d-2976-3b07-aee8-edec14c73518 | -2.65452 | -48.56565 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 846f64d3-714e-3a34-b0f9-b8501d284c35 | -4.92766 | -42.93188 | 2024-11-05 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4270a48-033b-3539-9897-23edf50c6df5 | -1.04038 | -47.79404 | 2024-11-05 04:08:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed9ba6f9-3fa1-32b8-924f-8c16e2378060 | -4.47976 | -46.46394 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 349ebc3c-9f13-3997-bd8d-20df3bb5eb9a | -5.47684 | -43.18672 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a152b3db-58e8-3f55-a713-7284e4d3a768 | -3.82798 | -44.13653 | 2024-11-05 04:08:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34f24921-b6a6-3c23-ab2f-c5187c642daf | -4.71623 | -46.42226 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad0ae103-5442-31bd-aa14-6b53ca0c3dfc | -2.65087 | -46.76571 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5c6ab3b-fd3a-35c9-b6ef-5b5dfa4da5e9 | -4.71563 | -46.42595 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7b81e34b-8c19-3a51-a54a-4d242183900a | -6.09804 | -43.9636 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a4094710-82e5-3dc2-9fcb-5093c4e5e6ef | -6.09866 | -43.95971 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c15dd6a0-2120-37b3-aabc-dd0bde165060 | -4.22926 | -44.23373 | 2024-11-05 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb2bf5bd-901c-3608-a1d5-df02c077e542 | -4.53802 | -46.41284 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9b6fac7-ee97-340f-abfa-b7901030f352 | -3.4547 | -47.66982 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab158fcc-6381-3229-8fe9-022ec03a3435 | -5.44734 | -48.20835 | 2024-11-05 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aeff68f8-9ab0-35d4-a967-8a51ba719f7c | -3.53876 | -47.38547 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d35866bd-668d-3f10-8003-bba8b6d6c368 | -5.47709 | -48.61296 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd0c2f79-b457-3ab2-bf65-6a7289f13c0a | -7.25569 | -45.41943 | 2024-11-05 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34f58879-b1f4-307d-bb59-8621fbdc880c | -4.54563 | -46.41754 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cea2a9c8-2663-3be8-9d0d-c0ae1fab286a | -5.47823 | -47.57184 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be994f69-31c4-3dbd-978b-11586ffd79e3 | -4.9407 | -42.71888 | 2024-11-05 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6020ab8a-4cb0-3aa2-b6da-ee12ce453482 | -3.22031 | -53.10382 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6124c838-1fe8-352c-96aa-68957351f581 | -8.13983 | -35.32517 | 2024-11-05 04:08:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 76824f04-297f-300e-80c1-c4a4e9c824c3 | -3.5624 | -47.37994 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e954f00-3bc9-3eda-9552-b4ea22be3e19 | -7.03982 | -38.71993 | 2024-11-05 04:08:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b7888c4-685e-3217-b13c-a043ebd394bb | -3.03385 | -53.25966 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 537ed867-d743-3901-8cdb-f7844a1c55ff | -8.30766 | -44.93352 | 2024-11-05 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb84fbaf-9ae4-3057-a69a-53b0fee79014 | -5.48424 | -41.66591 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 548636e8-2977-3c41-827e-ee27ad6e7044 | -2.30912 | -45.55511 | 2024-11-05 04:08:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be480b8d-b952-3f7a-a914-f678ca418fc2 | -5.34978 | -46.48189 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21cebdb0-3157-3bc5-b755-bd83362c8683 | -3.97154 | -48.15822 | 2024-11-05 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba102ba8-78a2-3047-88c9-098535b08fc8 | -8.32702 | -43.59641 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84d32936-d70f-33da-b02b-a8b00bad4484 | -4.05096 | -46.93713 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4eae5ce2-2b80-3678-8ce1-32eeddcb9aff | -6.03317 | -44.03292 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ea7dcc3-61b7-391e-9a1c-1ad769ae20ee | -3.04424 | -53.27824 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57d687af-fa49-3bb6-bd39-9b45006d6fd3 | -4.88633 | -46.71169 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73498734-a73e-3528-9c9d-c541f30f6fec | -5.5189 | -41.66484 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9840c0ee-15a2-3d66-be19-cadc3350fa41 | -6.51327 | -41.41521 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c634f5f7-76d1-3f64-b80b-88e0eadb6a30 | -2.9522 | -45.48428 | 2024-11-05 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a8648ea-4737-3529-9d44-8347dd9b9a23 | -4.26917 | -50.72412 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b935e8b-5c28-3476-852c-730b3701246d | -8.31527 | -43.58321 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d6dcedb-5d2a-33ee-949e-eb893e0ffd49 | -5.94306 | -42.66453 | 2024-11-05 04:08:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c791fb2e-7da3-3d60-a7a3-5a1ee59bf0ab | -3.55579 | -47.39258 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| bd024abd-2a1c-37a3-8f3a-f88620b60bd8 | -2.6501 | -48.57417 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 5120b863-2b4b-37f6-82e2-324848442159 | -3.73607 | -44.54481 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8643a08c-9bd3-3d5c-9163-6717ff22384a | -2.92691 | -48.61953 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af3e4abb-f8fa-3177-bb3f-aeef3db839b8 | -5.31697 | -43.3328 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 902f6de2-5700-34ee-aec3-3d0368e5824b | -6.13114 | -44.70081 | 2024-11-05 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bd3be92d-8c3b-3fa7-acd7-99a40afe6129 | -4.37492 | -47.2426 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21127b04-7c65-3590-883c-8235f43d0b8d | -5.9353 | -43.64075 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5d11a93-07f3-3a4e-8384-8af52417a855 | -5.34573 | -46.48122 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dcfc8ea-98c6-3de7-bbe4-0bc3296736a8 | -6.23149 | -39.62916 | 2024-11-05 04:08:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 55c34c25-aae6-3323-b62b-38b944f9dad0 | -5.3492 | -46.48544 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 95c9c41d-b087-3d4d-98a6-6ddf5b1b1090 | -4.39455 | -44.59998 | 2024-11-05 04:08:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d609739c-bdc3-32e2-9d63-9072cc49c22c | -5.08095 | -45.55918 | 2024-11-05 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d303ae9e-082f-3ad2-b19b-3a7c4865e756 | -5.69621 | -45.83711 | 2024-11-05 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 839a78bd-d69d-3c7f-8855-01a9fcbb8c03 | -8.28892 | -40.97248 | 2024-11-05 04:08:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1d588d1-313b-3da8-8a4c-c853de4440e5 | -4.65564 | -46.02508 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07743bac-2280-32c7-9572-3e634cc42e42 | -5.2229 | -47.47134 | 2024-11-05 04:08:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3defabf2-1e0d-3525-a16f-15049fdee2fc | -5.51836 | -41.66829 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ebf6c8f-9b6a-37fe-a146-2d1cbfb426e7 | -6.14994 | -43.43927 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c534a1c1-642c-3755-8763-7cab2142f32c | -4.03271 | -46.64869 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 784ee7e7-6f81-332c-a195-ab5b87d00c65 | -2.6585 | -48.5718 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 812cafee-88ba-3223-9ded-2b32c5049dcf | -5.99033 | -43.42645 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cba65639-807c-3f5f-8eef-55170fc82666 | -4.56699 | -45.80249 | 2024-11-05 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3452656e-f6c2-3f97-b396-95241479c629 | -2.17797 | -48.85946 | 2024-11-05 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0432f682-aaaf-33ed-beaa-3c882596692b | -5.61186 | -41.65455 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6184f00f-d643-3d46-be70-052cd555acac | -3.11908 | -51.11206 | 2024-11-05 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a7068954-c470-3b14-b0bd-50358d1037dd | -5.6676 | -41.92879 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 46fa2ba1-8520-3b23-b42e-393b04f0b516 | -5.37351 | -46.46379 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8c5427f-8679-3246-96db-aa7ab386dd58 | -5.00047 | -46.89519 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a20571a-e05e-3516-98dd-c6ab6bbc9098 | -4.40682 | -43.11531 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 67090f35-117c-313c-9ac2-8dd65fd86db3 | -7.13039 | -46.01393 | 2024-11-05 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddd171c8-cc77-3a2d-916b-4a9bf583d4a4 | -6.94448 | -39.50432 | 2024-11-05 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)
