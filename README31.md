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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 652b3a06-f12d-31c5-baa7-f61082880717 | -12.41997 | -44.21273 | 2025-10-16 03:47:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cd6e5f9-16ac-3d7d-8cb7-04c211c471bf | -6.41947 | -39.60252 | 2025-10-16 03:47:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8554374f-1f48-3650-b3b1-085c4155f683 | -6.18094 | -44.30844 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f51aac5c-f6a8-3a97-a3de-0d5596ef1d2c | -6.05938 | -41.88651 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b9c9c3d6-3984-3474-a136-3cc33c379681 | -5.85853 | -42.82067 | 2025-10-16 03:47:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6ca00068-fca5-3882-bac2-131377113dab | -4.95528 | -45.09992 | 2025-10-16 03:47:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76fd64c2-9071-3bf7-8e31-cafc650aff33 | -5.46814 | -44.64604 | 2025-10-16 03:47:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20388e65-bbb4-33ab-8aeb-6999cc2ce2fc | -5.50836 | -47.30569 | 2025-10-16 03:47:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 63a0b115-6d2b-384b-81b8-c5601688660a | -5.87627 | -43.85521 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90dda777-b261-374f-9e80-864709a3d516 | -4.38962 | -43.45746 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4f2f013-7ce7-3e5e-a7a8-31c7a43a2275 | -10.0551 | -43.84692 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24dbb89e-1a11-3ac7-be65-477dad7946c4 | -5.83804 | -42.34825 | 2025-10-16 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7333ea29-3107-3efa-b404-84c4b65f04b9 | -10.63516 | -44.41771 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cac984f7-c16d-36fc-b57d-789c18ce0fc8 | -10.71968 | -47.59189 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d7fb423-5a30-3c9d-acc6-24dabfe82854 | -6.18014 | -42.60329 | 2025-10-16 03:47:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| addb4645-4d06-317e-96e0-be50938d2bed | -5.75852 | -43.05921 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 008d73ee-f562-313a-9640-0f5e9be50d9d | -6.57676 | -42.97892 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51730752-7ff9-363d-a709-7ba46a56c0c8 | -5.8578 | -43.87763 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b3142d8-973a-3034-8343-1c039f4601dc | -4.77787 | -43.92698 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3ef328d2-c795-3ee0-be6a-970f4b558fd5 | -6.1406 | -41.78054 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6e7f21d8-a833-3088-b65f-76f6973f46a4 | -4.35552 | -46.77687 | 2025-10-16 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4a24ed1-5165-3ef4-9ad1-69ded3771355 | -10.87799 | -48.80008 | 2025-10-16 03:47:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bde006b8-6beb-31ce-8ba0-4b88ab022b4b | -10.12996 | -44.57876 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a79031c7-a9bd-3276-a639-a73c31f5893f | -6.40983 | -42.55434 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a0c0ed1e-1b28-3011-865a-682b20996aa9 | -10.22094 | -43.9054 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e8b7496-2faf-3bc1-937e-cee49bcdac7b | -6.19279 | -43.29773 | 2025-10-16 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cebdb6c-f40d-3ef0-b1ba-6c8c44145961 | -10.22456 | -43.91069 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d0b0fad-47f8-3186-a8dc-8c40c96aeee9 | -12.65234 | -41.25245 | 2025-10-16 03:47:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 537610ce-3562-396f-92dd-1132d16447e3 | -6.18333 | -41.72509 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 531c49ee-e040-3619-8b6c-4f8de90edd89 | -10.8045 | -44.00619 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed95915a-3888-3571-b20b-6a34bf9e9d50 | -5.87116 | -43.88503 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 504afdfd-b057-3082-9d3a-71ec95316af3 | -4.41885 | -40.17823 | 2025-10-16 03:47:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b3d383ba-345e-3188-90c9-a80902f1c4f5 | -5.87465 | -42.80556 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cce1d959-566d-3915-a891-42da7a30a222 | -4.35553 | -45.5322 | 2025-10-16 03:47:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d0aadf1-62a7-38d9-9c7a-eb33358a24d7 | -9.6944 | -44.50919 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7538915e-f842-35f6-8bdc-44b388abcdb6 | -6.42621 | -42.09595 | 2025-10-16 03:47:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cbc93f37-8f35-39be-a935-9cceb6e6e416 | -9.25712 | -45.26627 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ab2739f-bdeb-3eef-98e9-a90a466d8cc0 | -11.49313 | -44.10316 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1275e91e-8394-367a-8a9c-4df71d916dbc | -6.57016 | -42.96444 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e522351-b2b5-38ac-81ac-b444e9eed4ea | -11.79317 | -44.22256 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86cf8027-6065-301a-8b97-c0ea24058559 | -6.17921 | -44.30075 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e0f0f5c-c6a7-3d19-b1cc-8792b687594c | -10.64723 | -45.24198 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| acc6c8e0-29a1-3f94-80a6-1bac1394e6d3 | -4.87858 | -43.33213 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c85423a8-7578-3182-971d-63e74b1d921a | -5.8732 | -42.81423 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 24f5a91c-689f-306b-bc1f-49a5481991fc | -12.63872 | -44.30393 | 2025-10-16 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d48cea5d-c92d-3b39-beee-87688e72034d | -11.47587 | -44.14909 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee146c5c-a055-3acc-98e6-6e1c7c332750 | -6.0651 | -44.3065 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dcccfbd-817e-39d4-bc30-359ca6fd8a3a | -10.13709 | -44.56539 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 811a6e02-53cf-3ace-a646-813b2d6fe418 | -6.17303 | -43.4412 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39d8d6c4-2546-3ca3-9915-71905830a660 | -10.33461 | -45.17353 | 2025-10-16 03:47:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 840a3519-814e-3af3-a8c5-383c344ee007 | -5.47487 | -42.92554 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 0e59d1ec-c2ed-368c-b81a-a8b71bc01e84 | -5.71968 | -44.52825 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8941e112-601b-3884-9e2f-5e461fc0bf8d | -6.25437 | -42.90892 | 2025-10-16 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d9a6880-3470-3668-aa66-6bf753c491c2 | -9.22561 | -48.60637 | 2025-10-16 03:47:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2d1890fa-ff4f-3df3-9488-7d34a76ec3aa | -6.56429 | -42.97231 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc49777a-2e61-3c8f-bc8e-3a3d26017df0 | -5.2963 | -41.17867 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b40ed37b-c51e-35e8-9284-28369bff6d8b | -5.43271 | -44.22831 | 2025-10-16 03:47:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aad8c90e-90bb-3dfc-bf2d-2efe1768d3fc | -11.45724 | -44.17706 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24fb4c2a-ff2f-34b7-ad29-edde9ebba6ca | -5.91416 | -42.83811 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2c51f96c-dbeb-3e42-9c28-d6cfd604f455 | -5.24817 | -41.02503 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 68c5e3f8-40aa-355b-adb6-9b73bd9b6e60 | -6.0492 | -41.8964 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49bd82a9-164b-3672-a973-f10a4ebbd6b4 | -5.86727 | -43.87929 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec5d5b76-128f-33be-9a7a-c122a5b64350 | -6.40243 | -42.52024 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3b272d75-0c89-3b71-aa42-ce357dbc4a50 | -5.87541 | -43.86028 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5749317b-3095-3ef7-9f04-32e0691a1fb9 | -5.44461 | -41.0079 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bffcadd6-ae34-303a-bb24-7a46bec3af20 | -6.52965 | -42.20417 | 2025-10-16 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 016e29ad-592f-39c3-aac2-41cd6a1067d6 | -6.1401 | -41.75833 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8f03db9e-c5ab-3469-9502-033e89fdfca7 | -6.18689 | -44.10897 | 2025-10-16 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cda34583-ab92-37ab-b0bb-b07b5fdf1a3f | -5.36383 | -42.72702 | 2025-10-16 03:47:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 462c230f-c390-3ec9-b10c-5fa3f9d1ce06 | -5.82364 | -42.3293 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0d24bfb6-fe02-32ee-9bcf-4fec42d3ce80 | -10.27177 | -47.89351 | 2025-10-16 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de38bdf4-659f-3605-a4dd-7e497ca621bb | -5.86087 | -43.88811 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c587c753-34f7-3d7e-bffc-1b295aae4831 | -10.05147 | -43.8417 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9684be4b-be01-3a74-9295-992bd9861f21 | -9.68161 | -44.52741 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d1b3fc61-4e35-39bf-bec0-c234c3a56656 | -9.08731 | -47.95526 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3f8d3805-d562-39ff-8a0c-84cfd4911dff | -12.67274 | -43.43786 | 2025-10-16 03:47:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| b9c2be1d-3e39-39e8-8bb0-fa765001bf6b | -9.15623 | -46.869 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 70399687-07df-34b3-9bca-148b08afedd5 | -5.8916 | -42.83997 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fd98035d-4c7e-35e5-8c4d-24ed6b2c1b07 | -6.33615 | -44.01032 | 2025-10-16 03:47:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a3e4795-ad9a-339a-aade-b0d847ce6ed4 | -10.05776 | -43.85518 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 296adb55-4187-3b0e-9619-3eb2ece03420 | -6.16902 | -41.78683 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dec03e07-7b6a-3f1d-9f62-d64ebb23f645 | -5.07309 | -41.19262 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9faad565-510e-3fac-bd70-a83b67ac918b | -6.3899 | -41.93242 | 2025-10-16 03:47:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ff43c56b-6837-3a1a-a3c8-c13d8f693001 | -5.83512 | -42.33939 | 2025-10-16 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 21683db7-2349-3c6c-ba21-038e7439175e | -6.78538 | -40.80975 | 2025-10-16 03:47:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 72a1dc1a-2761-3b0d-bd3f-8c601573ae93 | -5.30198 | -49.57939 | 2025-10-16 03:47:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9186adb-8f16-3bb9-8af7-de422f1f8639 | -10.12442 | -44.58314 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5dfa5c43-26d7-39dc-94fc-e78584fe44da | -10.05495 | -43.84557 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bf50d74-c7d5-3ff4-a273-012fe386693f | -5.85286 | -42.33825 | 2025-10-16 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 55135bae-e591-3600-bb21-0fefd6d4c347 | -6.04478 | -41.93449 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5e6dbb8b-a529-36ca-92e8-01a3ffd0f287 | -6.33652 | -44.01288 | 2025-10-16 03:47:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6190e386-6195-3d50-975a-c36a05313036 | -5.87157 | -43.85423 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59fe0d91-a01b-3ac6-927c-4feded8919bb | -5.96546 | -42.8838 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cb86ae86-257a-35e8-9d10-c882d425dcaa | -6.45209 | -43.37583 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 771c4980-d371-34d2-8c40-916e6a7d873c | -3.61033 | -41.58314 | 2025-10-16 03:47:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e0f2ce3-615d-32bc-b0e5-a250f1e23a42 | -11.42797 | -44.0643 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36ead654-5fb8-3459-b6b6-d3c697b5388c | -6.09948 | -40.88451 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d253c0aa-8368-3cbc-ae3e-4eaa3dbca307 | -12.5721 | -43.78109 | 2025-10-16 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5295d7db-83fd-3725-9661-31583bfeae84 | -4.37206 | -43.38737 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 69d8a4a5-3c9e-3d66-ac8f-4939971220f2 | -4.41604 | -42.89354 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
