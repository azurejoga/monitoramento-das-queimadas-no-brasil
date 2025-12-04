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
| fa47ef13-69e6-3e38-b33e-6265b1292ce1 | -2.41461 | -45.79546 | 2025-12-04 05:10:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7371919f-4013-38ce-bc29-7c023df92633 | -2.92449 | -48.22941 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d8c14b0-4296-316f-9c94-d9757f6ff25a | -2.06503 | -45.35782 | 2025-12-04 05:10:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fbe9b9e-0e50-3e84-a71f-07d91a2f2a02 | -2.4282 | -50.2963 | 2025-12-04 05:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4254074e-f799-3c71-aabe-1d89cf0c0b25 | -2.64525 | -51.62646 | 2025-12-04 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ec5f795-b5ed-3e9e-b6ed-72da395e299b | -2.54186 | -49.4541 | 2025-12-04 05:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84efa656-5ac3-34c6-b478-c7424a8e9d54 | -4.55511 | -45.8086 | 2025-12-04 05:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e61c8c50-c9f6-3455-9e71-fa0abd9dcfa3 | -1.68457 | -54.25019 | 2025-12-04 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca8544b3-1bdd-3978-8ece-e8ea4fc98440 | -4.26012 | -44.15522 | 2025-12-04 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c895226-f5b4-3a6f-959a-523e27dc7b05 | -4.7782 | -46.13099 | 2025-12-04 05:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63cc8ee3-defc-316d-8807-d9ec23053c0b | -4.32908 | -48.76779 | 2025-12-04 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 930c019d-4d1f-3557-8f66-d972a61c64f4 | -2.38812 | -49.39251 | 2025-12-04 05:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 067d880f-9bc6-34c1-a6bb-0e955b8cbcea | -2.63379 | -47.31504 | 2025-12-04 05:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f37a8f4-2b61-33e8-9be0-4a0f553476ab | -6.42252 | -44.79469 | 2025-12-04 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf397a18-09cd-3c01-bcbb-638cce917f87 | -2.42321 | -45.79884 | 2025-12-04 05:10:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de53d4f4-089b-3de0-8f09-b4ede9dbb113 | -4.05113 | -46.61075 | 2025-12-04 05:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a52fd8f-7989-38ba-8c6c-fcd3057a41da | -3.04407 | -48.42743 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6910ec16-5a06-3494-b0d0-d0e6663a9073 | -2.92405 | -48.23239 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c76d5b32-06f6-3aa5-9ac8-813bf9312141 | -2.60621 | -49.25137 | 2025-12-04 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c7a4b4e-b473-3e40-bd31-ea656121d985 | -0.3746 | -52.04929 | 2025-12-04 05:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9d54bee-210b-38d3-a562-388b4136270d | -2.41725 | -45.79796 | 2025-12-04 05:10:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb9e0d3e-f9d8-3456-aeab-27b88693571f | -1.66957 | -45.79301 | 2025-12-04 05:10:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50cd181d-6ff1-3e7e-b97f-f07d4fe83abc | -5.98868 | -44.60217 | 2025-12-04 05:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7fe94233-a5cf-342a-90f8-dc2705cd1b7b | -1.87648 | -50.9646 | 2025-12-04 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9415266-d80d-30b7-9a59-7de77007dd52 | -4.0326 | -46.97662 | 2025-12-04 05:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa89f971-dbd5-3928-9bc3-6527e6f13273 | -2.70443 | -49.31483 | 2025-12-04 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e7d0a4e-7e66-32d9-9396-0f56eb4ee263 | -0.37465 | -52.05159 | 2025-12-04 05:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34fedfce-9ead-399e-a591-05324e98916d | -1.13106 | -52.58588 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad8b1416-f617-316a-808b-b60452db23d8 | -2.57619 | -49.09557 | 2025-12-04 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 609a30b1-0e41-3007-843d-d38e1bb86191 | -3.04912 | -48.42815 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0610270e-01bc-34f5-be36-ccc2318efed7 | -2.41846 | -48.59758 | 2025-12-04 05:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03ec0496-bdb8-3f72-9507-6dae959fe756 | -2.53182 | -49.45754 | 2025-12-04 05:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0f3da41e-c854-3b88-a026-4d6000cb8a41 | -4.06367 | -46.56512 | 2025-12-04 05:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cd23d998-f92e-377b-9327-83cd780f4eb4 | -2.14395 | -47.8786 | 2025-12-04 05:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 234b77cd-d46f-32dc-92ee-80727db7a4c7 | -7.22056 | -45.0505 | 2025-12-04 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee095fd0-6793-3feb-9fcf-f526b2e66787 | -4.33451 | -48.76579 | 2025-12-04 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d14b399-620d-3846-94d2-2f031922ea8f | -2.79159 | -47.43337 | 2025-12-04 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7af1170b-4cc3-3c2f-9030-4fd6284559a5 | -2.57622 | -49.09518 | 2025-12-04 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e07ad6eb-30ee-39a8-8161-40afe5b6d37d | -1.12122 | -53.45053 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e873345-4984-3402-b4a1-a2048f3bf678 | -2.63686 | -48.0328 | 2025-12-04 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9972853-e9c5-33ac-82ac-b9d8a1898230 | -2.07946 | -48.37155 | 2025-12-04 05:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 255349d5-2417-3bce-9436-69ddaadd0b8e | -4.25331 | -44.15458 | 2025-12-04 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb599385-e02a-3f86-a072-b5fa4392ea95 | -2.63127 | -48.03505 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9d07ff9-1e7e-3a15-bbca-53d7533c8a22 | -4.47721 | -44.26017 | 2025-12-04 05:10:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6bbd9d0-dfd8-3d87-b6a4-2b1a0906847b | -2.13834 | -47.88079 | 2025-12-04 05:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4756bfb0-0291-379d-9df9-7b4afe135581 | -4.69414 | -46.43694 | 2025-12-04 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11dc29f6-88e0-3877-9855-c0ccf237beb4 | -1.6689 | -45.79726 | 2025-12-04 05:10:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3bfa770-f856-34e6-8c2c-93f1087e4490 | -2.63595 | -48.03896 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bea2bc11-4880-37a4-bc7a-812514527b1c | -4.69183 | -46.43913 | 2025-12-04 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5fd1621-18b2-3f13-a71e-b3be432522f3 | -3.84559 | -47.8343 | 2025-12-04 05:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aa34812-5e94-36f3-a907-89a1ceda8673 | -4.344 | -46.14417 | 2025-12-04 05:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc878190-0baf-355d-bbd6-f1c462c8bc7a | -2.78519 | -47.4393 | 2025-12-04 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 189fa23a-8516-3373-85c6-ef1d2d5c10b3 | -2.64578 | -51.62294 | 2025-12-04 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 072cb516-3a94-3c84-bcd2-a81ae7a05755 | -2.53647 | -49.45827 | 2025-12-04 05:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e3bb0a98-64c9-31df-a2b9-cb2cc6b253b0 | -1.12263 | -54.19353 | 2025-12-04 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c2a7036e-fe7e-3d35-9e39-a9d7d614819c | -4.00675 | -46.54956 | 2025-12-04 05:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11bb0180-f318-37d9-8a8f-0a51df8a5896 | -5.02648 | -43.9777 | 2025-12-04 05:10:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1dd600e3-913d-3dd4-9189-f3243bbe4ac5 | -4.34463 | -46.1398 | 2025-12-04 05:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e0cbcbf-c50b-3082-904a-3e79e2e4f3bd | -2.14348 | -47.88168 | 2025-12-04 05:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fe276f5-f49b-3f5f-912e-76a5c9d8f079 | -4.67466 | -46.38943 | 2025-12-04 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f78d1a0-c755-3498-9922-e2cebc349278 | -2.37955 | -49.38615 | 2025-12-04 05:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6b42fda-43f8-36d6-954e-8a71550d66f7 | -4.00615 | -46.55357 | 2025-12-04 05:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ed66ccc-ba64-36a3-a377-130b8ba2026a | -4.33384 | -48.7667 | 2025-12-04 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 821a8c8a-4d86-3b6b-bdd9-a33bf07a7339 | -0.41528 | -51.6243 | 2025-12-04 05:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43f16d54-4edf-3080-91d6-981031940873 | -3.84511 | -47.8376 | 2025-12-04 05:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c856e80-b801-3400-a51c-1f87169573d5 | -1.42318 | -53.01067 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 517249ed-b5bd-3ef3-ba1c-411e87648e57 | -1.69653 | -46.15444 | 2025-12-04 05:10:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 619efc30-3c12-3c73-a83d-5156f85fb89a | -3.22447 | -48.62393 | 2025-12-04 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 033d7cc6-b336-31b8-a6bf-0be8b66e8338 | -1.69591 | -46.15844 | 2025-12-04 05:10:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09443eb2-060e-3008-8b88-b6bb81cea0cb | -2.43648 | -50.27144 | 2025-12-04 05:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b066df89-83e2-38c3-80bd-ecb10b05df98 | -4.49777 | -45.7731 | 2025-12-04 05:10:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc2bb771-8bdf-3291-9804-e2d1e2551987 | -2.07903 | -48.37437 | 2025-12-04 05:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c332468-7dd2-3b56-b81c-21372074f3ae | -4.54939 | -45.80608 | 2025-12-04 05:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91f071ca-bb75-3f9c-a09e-e09b5ca4771e | -2.0641 | -45.36022 | 2025-12-04 05:10:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87d06334-b83a-3dd4-81ed-8e4605865a44 | -3.04035 | -48.41785 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9807809c-1d30-33d5-9fb4-1b0c2da729d3 | -2.53109 | -49.46239 | 2025-12-04 05:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0baa4ff2-dd36-3f38-bec5-b78a637d363f | -2.42522 | -45.80603 | 2025-12-04 05:10:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04cc22e6-c86a-36c6-90c1-5c87875081fa | -7.21689 | -45.04908 | 2025-12-04 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a602eb51-6e24-38d6-9774-fa15d251e862 | -12.29674 | -57.3675 | 2025-12-04 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 26f95978-dd38-3935-b679-9f586719566f | -20.9186 | -56.36665 | 2025-12-04 05:14:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83a0a25f-5ac6-3d59-a85e-606d61115eb6 | -19.62542 | -56.84592 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 11288f58-c619-37af-b14c-b45ec7b21143 | -19.6404 | -56.76338 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 47ddcaf4-1006-3aae-a024-0d5cd35b41eb | -20.9134 | -56.37627 | 2025-12-04 05:14:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 260415c7-9bfa-3882-8f3f-893fd9d7fae7 | -19.63977 | -56.76802 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 218047a3-be88-39b4-b2e3-008a745a688a | -19.61804 | -56.8448 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c8c9c427-61f5-38d6-b264-dcc1fc36ea90 | -19.63236 | -56.7669 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 29ff9f48-160a-37f6-9a48-02d76aab5a85 | -19.63161 | -56.82809 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 9758ed6b-25d5-354c-9bae-8ec8f293a942 | -19.63468 | -56.83326 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f2fdc31a-2f7f-3052-ac3d-97826f17a8db | -19.61497 | -56.83965 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a2c18bd2-2d59-37e1-8dd0-caa2acf825d1 | -19.63607 | -56.76746 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 18f19f20-61b4-3cb0-9d4e-9b233ec78f56 | -20.91792 | -56.37176 | 2025-12-04 05:14:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1cc09deb-2e35-3fb0-8f95-c3a53c49633e | -19.63099 | -56.8327 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 12441493-dea9-3462-a888-195fe4346490 | -19.63406 | -56.83786 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 552870cc-2e0b-3022-a037-16b206028f04 | -20.91725 | -56.37686 | 2025-12-04 05:14:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5ea68d59-7004-3004-a0cc-120175e7b4af | -19.63036 | -56.8373 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 5c994b82-0111-33b6-8aad-6ca4be2645cd | -19.62173 | -56.84536 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c6267c71-57de-3475-b4dc-ff01e4360d68 | -19.63531 | -56.82866 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4664216c-90e6-3125-a735-a847b8904c87 | -19.63343 | -56.84246 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 593fcecc-f5f5-39ac-9ab9-1c0ac30f470d | -19.62974 | -56.8419 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 9a303570-17ed-3172-ac5b-168add5601c9 | -20.92177 | -56.37236 | 2025-12-04 05:14:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README21.md)
