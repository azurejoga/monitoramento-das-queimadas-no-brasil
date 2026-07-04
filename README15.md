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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4596fd90-ae2e-3c45-abdb-947f93c454c2 | -9.96714 | -54.93643 | 2026-07-04 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5014cede-58f5-3dbc-8781-941c06152435 | -11.48781 | -52.92228 | 2026-07-04 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f4b2e93-d915-396b-9ad8-e381d42010f6 | -7.90856 | -48.25172 | 2026-07-04 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aed85443-9f0b-33a0-bbf2-486cfe8e9f3a | -9.04277 | -47.74254 | 2026-07-04 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df574514-02c9-3b22-a469-61a8e1cc310a | -6.42787 | -55.79263 | 2026-07-04 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4170a358-e7dd-32b8-9a7b-dffcd6c321a0 | -12.75439 | -44.53992 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 81cdaaa2-63ec-3075-bfd8-04cc333dd202 | -11.43794 | -46.57234 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 14315884-ae87-3c74-bdb1-b3963233e28a | -10.30173 | -57.12739 | 2026-07-04 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 769556bb-710e-357e-a205-670e3efca751 | -12.35329 | -47.90438 | 2026-07-04 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 339053d1-441b-30bd-a86d-d882f57552a6 | -6.61049 | -55.2921 | 2026-07-04 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c37a54c-5c59-38f2-a2ca-eb4200991514 | -10.92929 | -43.04089 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1b2bbcbb-5e53-334a-9c10-fbc49013521c | -12.75766 | -44.56174 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2ee964de-82a3-30a4-ac2d-fff7c1dd1400 | -11.38022 | -47.81661 | 2026-07-04 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a54078c-31e5-3a3f-ae96-2b8b12ae2f17 | -9.38198 | -58.20518 | 2026-07-04 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3833ed3-6e34-35d4-8284-e2a7951e91b0 | -7.74048 | -44.17453 | 2026-07-04 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b89a8b54-718b-3158-86de-643f845db190 | -7.51233 | -49.52372 | 2026-07-04 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2dcaf3c1-5448-330d-b501-1dd27f2610d4 | -8.76277 | -47.40459 | 2026-07-04 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b94af307-6fcc-34c6-b176-354a22d0e338 | -12.76531 | -44.54062 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 06795db6-9c1d-3657-b228-f25a866d4392 | -11.45707 | -46.55553 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8309c13-5e20-3f0e-99a6-edda48c3105f | -12.75562 | -44.53937 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 4d32acac-d43d-3a6e-ad63-15636e760311 | -7.23263 | -47.1184 | 2026-07-04 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 760a3d52-0807-3f3a-a1db-7b29b7e61223 | -6.9298 | -43.71097 | 2026-07-04 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d50a5134-427f-3d4a-8c64-d77b49936265 | -4.92638 | -47.54303 | 2026-07-04 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c747d04-3444-3a56-8b1f-7e9506ed24b6 | -10.90701 | -56.8569 | 2026-07-04 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c3c524eb-7439-3a18-bcd7-db8801f9c231 | -12.7579 | -44.55149 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f4c9f008-6ecf-3eae-b05b-8383e095c846 | -11.48837 | -52.91874 | 2026-07-04 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c688b0c9-aad0-39e6-9bf2-f28129ebcb4b | -6.1868 | -45.34267 | 2026-07-04 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d85c188-8dc0-35a1-bca3-0577f14dfd0b | -9.60005 | -56.92307 | 2026-07-04 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ee22aed-fd7c-3dc2-9485-dba6f9f15a03 | -12.75836 | -44.55634 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6d2a2725-99fb-3dcb-aa7e-b93cb2fc1624 | -12.7646 | -44.54609 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 9767ac5d-2ca8-3c57-ae68-cd2742deaf8b | -10.9285 | -43.0473 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| b5ee0e64-aff6-396a-8f2e-bdd9b9f1656c | -6.70671 | -51.8839 | 2026-07-04 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c85b12c-1f1b-3616-bdd7-b64ae5a4eeea | -8.55056 | -47.23908 | 2026-07-04 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5575374e-6c33-3098-8e88-532b7692c503 | -10.92889 | -43.04409 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 004945e5-1cad-3930-8f1e-66e946fbc3a5 | -10.12266 | -52.08441 | 2026-07-04 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac61daa4-5962-34ec-b929-6bc3edf3b63f | -6.93451 | -43.71163 | 2026-07-04 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03e9c4f0-5586-3d3a-b787-ac76569f40a9 | -10.39053 | -56.76514 | 2026-07-04 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ed090a3-8759-35d0-9847-2d04d6534f22 | -12.75422 | -44.55026 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0882a088-8275-3e01-bfea-3b072dc6711e | -11.50864 | -47.40871 | 2026-07-04 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8059bd7a-8044-382a-9fca-cebb9a5023d2 | -5.78346 | -43.89513 | 2026-07-04 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08f521fd-4e2f-3ba0-9a99-0c09512e2d35 | -7.00577 | -42.76734 | 2026-07-04 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fb3fc80e-cc2f-3c0f-9a32-8704ba2c70d7 | -12.75856 | -44.54604 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| c13291a9-8361-3c0e-ae96-04b4c9f52241 | -8.08645 | -47.15984 | 2026-07-04 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f56ef825-cd3b-3658-99d9-e37b3adbf939 | -7.00923 | -42.77968 | 2026-07-04 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16763862-9824-346d-9356-1fd99fe4fb05 | -4.50209 | -50.92663 | 2026-07-04 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e6eb2ef-ff1a-358b-9d97-64df2cf9d457 | -11.33047 | -46.90541 | 2026-07-04 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48039509-a1d1-3320-82f6-ce2fed4ccf82 | -12.7432 | -44.52108 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8fbf7065-2c72-3e0a-ae3b-aac80dac4889 | -10.12157 | -52.09138 | 2026-07-04 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8210660-39e4-3a2a-9b11-4fa2f46f9a55 | -5.79333 | -45.06511 | 2026-07-04 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cee14108-bed9-3e4b-9be9-0994962ca6dd | -8.86156 | -62.22514 | 2026-07-04 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f2f40fca-7ce7-350c-83ea-cdf8ca59c238 | -11.44314 | -46.565 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d1bf402-f9d7-351e-b4cd-b222aac4c570 | -12.52402 | -48.28901 | 2026-07-04 04:46:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78ce1b67-d38e-37a9-a3d1-39f4b331ffe3 | -5.79847 | -43.63211 | 2026-07-04 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 563e5259-37de-3b14-b4b1-bbf7ab912908 | -10.93412 | -43.0448 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| c81d79e4-2374-3ed3-8695-b758c33932ff | -9.38282 | -58.20689 | 2026-07-04 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ab9bcb2-3ce2-3972-bfae-8dcf8978020c | -13.24336 | -54.34727 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 2b4fb568-9254-3515-bc34-3d6e0e499c19 | -14.19549 | -45.42682 | 2026-07-04 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 250cb75a-9327-3193-a808-8d90a57db0c2 | -11.634 | -59.01384 | 2026-07-04 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed35d423-d3d1-3266-974b-afbc0c5e4b73 | -13.23656 | -54.34614 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 713262c2-af8d-3f9d-b993-f5130525fe54 | -13.23717 | -54.34241 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 87506a75-4eb0-3951-813e-58ca3e5faaf2 | -12.44466 | -49.45714 | 2026-07-04 04:49:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80d7d9e0-b44f-358c-861e-983159d1c66f | -13.22885 | -54.37185 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e4d6b13-9ffc-34c1-a059-9198e3bfc5ae | -12.68092 | -48.2181 | 2026-07-04 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d22cbeed-45f4-35f7-84d7-83cf2a5412f8 | -18.77342 | -47.62334 | 2026-07-04 04:49:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a964a9ed-f030-3911-a8b7-d7ab860c2b55 | -13.24587 | -54.37471 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5efad25-0132-3bd3-aad8-c630cee7229f | -11.63124 | -59.02012 | 2026-07-04 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6c308ab-393e-36d9-bdeb-6ff8896366fa | -13.23381 | -54.38429 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f81a0d8-3ee8-326f-a717-ee4596b80c4b | -13.22296 | -54.34383 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7762eaeb-0405-3f3c-8dd8-3247733e6dec | -13.25356 | -54.34897 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eb370041-3d86-3f43-801e-bb3e7ea53250 | -13.23164 | -54.37619 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 878ee566-bea6-3d12-83f2-5ff4b1f37960 | -14.16317 | -47.78679 | 2026-07-04 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 715055a7-c460-3d1a-ae96-562e079801fb | -13.23316 | -54.34556 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 0efc9c8b-c3b0-3bf1-b02e-80c05a09586b | -13.25818 | -54.34205 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a386d7de-0a83-338d-825a-b7f7130bdc35 | -13.23377 | -54.34183 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4f31b5b4-2128-353f-8ac4-76992d949c59 | -13.22823 | -54.37562 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 33e25e45-00e2-3668-bdcb-dbe82e3020db | -13.23627 | -54.36924 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fe4615c-dd6c-388a-8ef0-f697ba3c675f | -14.16243 | -47.7831 | 2026-07-04 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f09337ee-9550-3178-a81a-7d37ab004a1c | -11.62863 | -59.0177 | 2026-07-04 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6fe6cba-1566-339e-9cb4-7f8b6b7ffda3 | -13.24676 | -54.34784 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8239fa30-30cf-37ee-8fb4-789f1df74a08 | -13.22979 | -54.38749 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aab49df3-9698-3ec3-a8c6-525f7ac91eff | -13.22793 | -54.39883 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1335c4b7-e1ec-3aa8-be15-190fdd01e6c3 | -13.24057 | -54.34297 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0eeac09f-a788-36ba-84eb-8f7e1a722377 | -13.23935 | -54.35045 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 0f24562a-1d17-3919-8518-a1023ef14342 | -13.25138 | -54.34092 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5073a624-ea97-3e60-9ad8-01c87f56f844 | -13.4437 | -43.85329 | 2026-07-04 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da158f03-de2c-3328-a173-4e6f816fe67d | -13.25975 | -54.35385 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de9e9164-5315-34ac-a9f5-583559c7bd31 | -13.2239 | -54.40202 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4474e3e-2a6d-3529-ba72-170870d047a8 | -13.24275 | -54.35102 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 0549fc21-5166-3dc3-99ec-74492a0fddc3 | -13.23443 | -54.38052 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01049d73-4346-39d4-b5bc-6a24bd07bc81 | -13.25077 | -54.34466 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 80e27e6c-e688-3f88-9765-eec403278025 | -13.24397 | -54.34354 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f8ae62df-1f55-318c-8c80-ef7f2b985e38 | -18.76914 | -47.62275 | 2026-07-04 04:49:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f775130-612b-3884-91e2-c391621b2685 | -12.43227 | -58.41575 | 2026-07-04 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03cf7f5d-9145-3f47-960a-16b10318f7f1 | -17.54835 | -46.94788 | 2026-07-04 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88ee4535-401d-3732-acad-cbcb7ba9bbad | -14.17843 | -52.88617 | 2026-07-04 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fd41d2f-7a2d-3baf-b65a-bf20ec39060e | -13.23906 | -54.37357 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bbe0550-1cbc-35a1-857f-a7cb35ac343b | -18.72019 | -47.53568 | 2026-07-04 04:49:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4702df64-b206-393b-ab0f-21d24ad5af54 | -13.23255 | -54.34929 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 8d382e4e-52c9-3d4b-bde8-036eec9708f0 | -17.69163 | -48.64046 | 2026-07-04 04:49:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 395e769b-4bd5-37d9-a229-98a6067a5b4f | -13.22669 | -54.36373 | 2026-07-04 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README16.md)
