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
| 068de774-2551-35b3-b81b-9c7d7d1ceb23 | -11.79334 | -43.62809 | 2026-04-13 04:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1a0ea19-d19d-3680-8339-3f4ed16f6041 | -11.80162 | -43.62932 | 2026-04-13 04:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3aa5c9ba-47e3-378b-8859-2f3d74ddd511 | -11.80577 | -43.62993 | 2026-04-13 04:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32d615cd-532a-3188-9eee-98b781150441 | -9.80016 | -37.47252 | 2026-04-13 04:36:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 781efdf6-5e33-3cf9-b947-4820e6453599 | -11.80215 | -43.62548 | 2026-04-13 04:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4d6d654-3150-33d0-80b3-a6e44940a1b0 | -9.80079 | -37.47569 | 2026-04-13 04:36:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bf56f9f9-b198-3088-b874-9d5f8c1bf4d5 | -11.80058 | -43.63698 | 2026-04-13 04:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1bd4edae-1a49-3b87-8667-bfe0cd9a0774 | -11.80524 | -43.63377 | 2026-04-13 04:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2eec831b-68d0-378a-a52b-8e9608d5e3d6 | -11.80938 | -43.6344 | 2026-04-13 04:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1df1000-0c18-3eeb-b2fd-193eae6d6341 | -11.02812 | -45.13581 | 2026-04-13 04:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 76caa4c3-36a1-30a5-b695-463de4476b1f | -9.79956 | -37.47716 | 2026-04-13 04:36:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 399c790a-e315-3bd5-8076-eeea9e39c06b | -11.8011 | -43.63315 | 2026-04-13 04:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 29907dca-57a1-3552-8024-100f511dad39 | -11.03102 | -45.13382 | 2026-04-13 04:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a1bc9647-b4be-3adc-af29-59ac6463bf75 | -11.80886 | -43.63823 | 2026-04-13 04:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e3cbd9f-a9fb-3442-856d-9ad0de7b437f | -19.42229 | -50.5047 | 2026-04-13 04:38:00 | NOAA-20 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9172b878-f80b-35bc-a8ec-3736ad9f4c8d | -18.78826 | -51.93679 | 2026-04-13 04:38:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a10c285b-75d1-30c9-8e86-307ffdbdef6b | -20.13449 | -46.7599 | 2026-04-13 04:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 470c1b18-ecc9-39e2-bc5a-06c192f27460 | -20.13383 | -46.76488 | 2026-04-13 04:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ee94577-a888-34a2-bdb5-5f3473da9481 | -15.71726 | -60.05671 | 2026-04-13 04:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97cb5e3c-2289-33a6-9242-8af7aaeafb15 | -18.47977 | -44.35532 | 2026-04-13 04:38:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d338081c-aa67-36ed-b505-95ddffb281b3 | -21.25338 | -48.57961 | 2026-04-13 04:38:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 058a5edb-f7f6-3c1a-8c23-13a5f09ff1f5 | -21.25397 | -48.5754 | 2026-04-13 04:38:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae6a7c44-89a1-3d76-a3ee-7b9be3eaccea | -15.71104 | -60.05923 | 2026-04-13 04:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d425e202-10d2-359e-9704-5f4093cc0520 | 1.0846 | -60.5226 | 2026-04-13 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 3008ada9-f48f-3ee8-ac56-520eba2a0650 | 1.1028 | -60.5414 | 2026-04-13 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.9 |
| c17816ad-4f59-310a-8e85-fac901f72553 | 1.1028 | -60.5225 | 2026-04-13 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 139.7 |
| cb53f056-4f92-354b-be5b-e5a5e8ffbf4d | 1.1028 | -60.5035 | 2026-04-13 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.5 |
| aa338b23-58db-30c8-9b02-8861effc38b1 | 1.121 | -60.5413 | 2026-04-13 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8830fca8-8c7f-3115-bf92-7d5d6bbd9e05 | 1.121 | -60.5224 | 2026-04-13 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a23c3ca1-3407-30e5-b604-5bb760ad4d91 | -23.42668 | -46.75901 | 2026-04-13 04:40:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0b04a639-127f-3f30-a398-c9943a7b5603 | -22.28525 | -48.08464 | 2026-04-13 04:40:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fce9e60-0bb5-3137-978d-d2648147dd1b | -22.2883 | -48.08975 | 2026-04-13 04:40:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 838b640a-e117-381c-9fd8-ca427251aceb | -23.42882 | -46.7576 | 2026-04-13 04:40:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ec71eb41-6ec5-3758-aef7-10aca8bd401c | -21.80331 | -49.62197 | 2026-04-13 04:40:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| a5962b28-3c40-3ead-b455-2e23df0a79c0 | -22.28527 | -48.08698 | 2026-04-13 04:40:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe26d719-658e-3577-a0b9-6e6f75afedce | -21.80731 | -49.61857 | 2026-04-13 04:40:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| a383d0d6-e8eb-3cbd-8a1b-511d11525790 | 1.0846 | -60.5226 | 2026-04-13 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 75182890-d6be-3789-8463-c73a25474216 | 1.1028 | -60.5035 | 2026-04-13 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.3 |
| c20a2061-97cb-3e71-a598-42ac076c7116 | 1.1028 | -60.5414 | 2026-04-13 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 8025252d-1985-3a99-865e-901bee983b22 | 1.121 | -60.5413 | 2026-04-13 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 17409b19-99ce-3299-9848-2105407745ed | 1.121 | -60.5224 | 2026-04-13 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1a019483-5f3f-3679-8212-42610da31522 | 1.1028 | -60.5225 | 2026-04-13 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 5074913b-e052-326d-93f2-93257a4e6f06 | 1.1028 | -60.5414 | 2026-04-13 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 125.2 |
| fffb67bc-d054-3bad-9edd-7cd4d4f0fd80 | 1.121 | -60.5224 | 2026-04-13 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6ef49b67-4641-3b04-b278-f890138f452a | 1.1028 | -60.5035 | 2026-04-13 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 7aefc25e-61a1-37bf-a3a1-b98429c87fa0 | 1.1028 | -60.5225 | 2026-04-13 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 174.6 |
| dfbd6a4b-75f8-36bc-94c2-1cf0445eb1e6 | 1.121 | -60.5413 | 2026-04-13 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 9010167c-0000-3173-acd8-3fb58904ad3c | 1.1028 | -60.5225 | 2026-04-13 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a731b773-094d-3256-af71-75d0a0437b1d | 1.121 | -60.5224 | 2026-04-13 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.7 |
| a038594a-447a-3131-bdb4-21af1f183e03 | 1.121 | -60.5413 | 2026-04-13 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 8583dd3c-07af-33a4-bfc9-83811ae211cc | 1.1028 | -60.5414 | 2026-04-13 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.3 |
| cf9d87b8-9955-3c62-8cac-e7eebd28d7fc | 1.1028 | -60.5225 | 2026-04-13 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 23ddc6c7-4298-38c5-bcd4-4de8ae44b6a7 | 1.1028 | -60.5414 | 2026-04-13 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 416d26f1-78ce-3761-abd9-f3c14c4550fb | 1.10451 | -60.54081 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65313388-3d3a-336d-8820-9d6135481449 | 1.83696 | -60.73806 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efa88d90-aec0-32a8-ab13-a2d2ca90177a | 3.31186 | -61.22758 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55b4b82d-a1bb-3cab-8d03-cde101568e8f | 1.34445 | -60.66315 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c811cb78-003f-30ac-ade1-9d703e7a97a7 | 3.331 | -61.23307 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29b0fcb3-fc42-3db0-a9e1-102ed01fb2e9 | 2.20298 | -60.81095 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42ef270e-e5ab-39b5-a191-0e6f698f36c2 | 2.52591 | -61.67301 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2e66b17-bbe5-3c72-b818-59edb8e1399b | 3.88189 | -61.84111 | 2026-04-13 05:23:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec6e5f87-de9a-3aa8-9797-226f454dc003 | 2.37915 | -60.95795 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a44fb79-6afa-340a-acef-e87cf2fa8eda | 1.11075 | -60.53611 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15e64ae2-1d37-3b59-a8bb-99120bb494ef | 3.87886 | -61.84614 | 2026-04-13 05:23:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9245bf5-948c-30e1-87ef-6f07d1825f68 | 2.52228 | -61.67355 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fc8acd8-1181-3a19-9e51-6a12103cfa57 | 1.10961 | -60.52879 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 541082e8-de01-3620-958b-290d51d41917 | 1.10621 | -60.52931 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d650644d-448b-378a-a7b2-7dc3b1435428 | 1.3747 | -60.65476 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a80db5c-d9ab-3a02-95af-8dca72eb537d | 2.01912 | -61.09416 | 2026-04-13 05:23:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f9fc189-aeff-39d6-8c7f-29303f9cb4ad | 1.11642 | -60.52775 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe25d030-e5dc-3d23-af36-9ec9433194b2 | 2.39144 | -60.96799 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16b0e82e-98bc-3924-bf61-81c2a40bc040 | 3.23635 | -61.20558 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8261fb08-1b08-3db6-a598-66b4a159b388 | 1.10507 | -60.522 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21ec8741-d070-3eb6-af87-d21f77f0d92d | 2.37644 | -60.19019 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e678f708-1a7f-336d-b977-074069de7cf5 | 3.31248 | -61.23163 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a48f9aa7-1cb2-3587-a690-d0ac1cb2695a | 2.08202 | -60.53249 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb4eac92-2d13-3229-8f08-a8d21f39450d | 1.09997 | -60.53401 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1c827b5-5391-3219-a3d9-2db0d0563f86 | 1.096 | -60.53088 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 047b60d2-8968-339c-b25c-6bd16e0379b2 | 3.23215 | -61.20206 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d9450a9-d939-34d5-85bc-56b840edae6a | 3.87817 | -61.84167 | 2026-04-13 05:23:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 964ba97b-326a-3b8d-b80b-1ce965626744 | 1.11132 | -60.53976 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98eaf634-4727-3d0c-9e50-e676dc760364 | 1.09317 | -60.53506 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8203c0a-df6e-3d16-b1b8-639c8d0c00f6 | 1.10281 | -60.52983 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 005287bf-7a73-3503-a645-b4227e93b699 | 2.37974 | -60.96181 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91e0b674-607d-3a8b-9439-9bd1bcca8549 | 1.10224 | -60.52618 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a10bdcd-9856-370b-bbdf-b65799d67600 | 2.41114 | -60.70575 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3db23ed-2be3-3064-b195-c56fbbf429e7 | 1.11699 | -60.5314 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a461e559-c9ac-30d1-9247-ee24b45b6538 | 2.37565 | -60.95847 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c55fef85-1a55-3a38-a4eb-0e25b2727a17 | 1.10904 | -60.52514 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bedf31a-db83-30d7-8ca3-f50664e85cc1 | 2.377 | -60.19384 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b24d7454-96a3-3978-89f4-158fbc7cbe46 | 4.3043 | -59.72462 | 2026-04-13 05:23:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f999ab4-9f89-317b-afb1-8e16fa9ebb98 | 1.11472 | -60.53925 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6681e9da-2a00-38f0-81ee-b1b996a062b2 | 2.02263 | -61.09363 | 2026-04-13 05:23:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75154b91-5994-30ec-8e40-ff5add18584c | 2.35216 | -60.44199 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 070364d8-2812-38a1-808c-8a48cad01182 | 1.09657 | -60.53455 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 140d7e68-24f3-3fd1-9006-5f80854f513f | 1.11756 | -60.53507 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36bf1e59-92e6-3d70-ae50-7859455e28b1 | 1.34788 | -60.66262 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb9f41da-163d-3f30-9d2e-ec88dae1ead0 | 3.33081 | -61.20819 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93e1d393-8d37-30d6-9cf3-c13313647d61 | 2.08145 | -60.52873 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1754532a-f9b2-3475-8d3b-5751d15552a9 | 2.38826 | -61.77398 | 2026-04-13 05:23:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README4.md)
