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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d358900-9f3a-3ce9-a2bd-73b88680467f | -1.70809 | -52.45138 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 886437b1-4df4-387d-8254-c0e1aff9432d | -2.47674 | -46.56491 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4703c433-67c6-30ff-9fc0-20f0f562faa4 | -3.27184 | -46.45572 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97212560-33a4-396c-a139-e7487bb2057d | -3.9829 | -46.72979 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7458d5a9-c522-3150-9a2e-cd4b71c4ec40 | -2.59404 | -46.27232 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0740ccc9-2f8c-3114-9a5d-b4d59dd59dd5 | -3.19741 | -46.36639 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98f9ce59-89f7-3498-884a-eb8261e200d9 | -3.26574 | -46.45124 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b97e461c-747d-331e-ac29-6858be4febb8 | -2.56571 | -53.39887 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb1881f9-3ec5-34a7-a1fc-013fb1387542 | -3.17296 | -46.32705 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb0f01f-c013-3ec1-9ac9-a8c24b011ccd | -3.21065 | -53.1189 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71beed30-6307-3512-a2b4-edec01a2ecf7 | -4.04962 | -46.99833 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b157a705-0d97-3a13-86e9-8d0eb961ab0f | -4.32753 | -48.0998 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3200e0ed-071a-3b13-9fcb-83d057d0411e | -2.77457 | -55.36011 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7ad4311-b5a7-3733-a414-d9821dc302d8 | -2.67929 | -46.14021 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 633ba79f-c305-3e95-92d3-c5c946f3e27d | -2.54523 | -46.56153 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 373b36f2-14b6-3d2a-8fe8-22440c5b2fef | -3.94534 | -46.92519 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d90f8ecb-d05a-367f-87e3-8c325d58a6c4 | -3.96723 | -46.65644 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98fc4b8e-1cfa-3abc-baa8-7e44f8992239 | -3.47561 | -49.92929 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be933ea4-2a86-3f08-b67a-49fd92397012 | -5.80181 | -46.47551 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 2c3319dc-732c-35e3-b50b-207a20f51891 | -4.40258 | -45.35271 | 2024-12-03 04:29:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 718bc174-da23-3dce-8c17-ffd3bc14dc87 | -3.31034 | -50.08378 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd0d2136-e11d-3701-8553-927e8e2f862b | -4.11298 | -48.53519 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6e89c39-f58e-3881-9331-f02c0dee35e5 | -2.80185 | -53.05208 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88ee6566-ff85-3fde-8a0f-c50866409536 | -5.80686 | -46.48714 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| bd3b61ad-b227-3843-a8f9-a79c48807dce | -5.16888 | -43.74151 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3da0cdc-d405-38bc-a025-959430751cdd | -4.16855 | -46.56376 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 272f41bf-e407-3c58-8d7d-d2830ca3de31 | -1.73764 | -52.62331 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 048ab324-8a2d-3fd6-a010-cb8e9d4946e1 | -2.2596 | -53.6122 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7dd97bc-63c1-36c1-9ae4-9934451304a3 | -3.55841 | -50.17934 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55c2f2de-8fd6-322e-b323-8cf8235264d7 | -2.54506 | -53.41352 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6a2914c-a893-3177-9f91-8ef19afe4a3e | -2.56641 | -53.39444 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a0e4d8f-c555-36d4-86a3-04c37445da38 | -4.31755 | -48.09822 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bf3cc0f-d73d-3386-ae89-6358888fc844 | -2.302 | -47.2877 | 2024-12-03 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c5af44e-1bd3-3d66-942c-a1b846290c8f | -3.46194 | -49.9684 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65659e0e-8b50-3e23-ad12-492f8345bf07 | -3.79064 | -46.69947 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 979839c5-4710-3ebf-be22-3d4c5df56b94 | -2.80985 | -53.05762 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2084101-97ad-32db-b521-71b7018fdcb3 | -2.04457 | -51.19943 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f182869c-7cc8-3e22-90b0-47264e15c41a | -2.31248 | -47.2858 | 2024-12-03 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1eaab6fa-e069-34dc-9f27-67162cdf095b | -3.70486 | -50.26483 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04b4e303-f895-30b9-93b3-6d106ac3b5fd | -2.54506 | -47.12504 | 2024-12-03 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a39961a6-9169-33b9-95e4-e074f45dc0df | -4.05099 | -46.81463 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d116e5c1-ccd2-36e9-b4d0-7656d3e41cf0 | -3.41822 | -54.02991 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aa9f830-5b50-3968-85ca-4ff94e36b6a5 | -2.85164 | -45.3885 | 2024-12-03 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 80681206-69ba-36d4-be68-f15d333ab95b | -3.92317 | -48.14387 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b688f02b-97bd-300e-ad67-da474960d2d5 | -3.52672 | -51.15903 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dcc1a7c-1a4c-3c67-9aae-1d5234777d77 | -2.84101 | -54.10929 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a8e99ba-e6a0-31b2-8f6e-c626a1398801 | -2.33263 | -45.86087 | 2024-12-03 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ae43433-5d79-3563-9d67-91ad1c1cc259 | -4.42877 | -45.79055 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ca2aa8fc-8255-37c6-bcdc-c8ad15d53aad | -2.56553 | -46.34579 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78c1cf59-39d0-3d91-8b85-abdd8fa927e5 | -6.75334 | -47.08025 | 2024-12-03 04:29:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc11b864-adb0-3b32-ba54-d0b14265a075 | -6.12264 | -43.95868 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 49d769eb-0559-3b4a-b336-ff539ad7287b | -2.42856 | -46.4834 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33a6b572-aff9-3474-80d2-9fd04eb8a0ac | -3.34091 | -46.05627 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ffa1bc0c-062b-3be2-94f1-0e5ad25cf4e2 | -5.79791 | -46.47853 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| e8fefaa0-d343-30b5-83e0-a8bbf3e771b6 | -5.54422 | -43.89898 | 2024-12-03 04:29:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa85b814-4758-3a83-8553-36b2cb0c01d2 | -3.80496 | -46.69463 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e22e82a4-ec92-383a-9086-8806aee47434 | -3.80111 | -46.69757 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed516d44-ebdd-34ce-bbfd-3e6331b67ed1 | -4.14874 | -48.22194 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20f31a7c-74ff-3b37-bfab-719562c48592 | -5.40741 | -45.15318 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ac9b754-cb44-3470-9166-32ffc4319ef3 | -4.30306 | -48.23213 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b2480fc-a9b5-3796-8d0a-815c2b8ae521 | -2.59334 | -46.016 | 2024-12-03 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e31ff56-ec67-3c45-a2b6-b1b9e5939562 | -5.53437 | -46.45238 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ac32a49-e5a7-3cdc-9369-374f85274436 | -3.83067 | -46.61713 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4c19963-ca17-306f-ae05-c6524bf4d5f7 | -2.5673 | -46.57201 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f0b114c-8c4a-3df5-9171-078455be78d7 | -3.35159 | -44.36509 | 2024-12-03 04:29:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b703804-d5bd-3079-97e5-48e49f86c6d3 | -3.14966 | -50.34198 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b006fb6f-2a75-3b7c-9221-34bf42d0b181 | -4.29642 | -48.20952 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dea05d1d-e5a2-32a7-88d3-4bb92de63eb2 | -2.6418 | -46.11984 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21544257-7054-3195-aff3-f28cede03c4c | -3.26762 | -53.62677 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1a12d29c-ccd8-31c2-94e0-263ef9c95bfc | -4.01018 | -53.82849 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0cf1ea8-1b17-3084-91a5-0a5ec2ad2919 | -3.85636 | -46.51822 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65a1d4dc-edf9-3a70-8756-59d7e40949d0 | -3.81483 | -46.67493 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b40fa3e-dd48-35c9-9783-29a7ce81c94c | -4.01822 | -49.95798 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 322f9aa4-5bb3-3757-91d3-bc2846e4680e | -5.83562 | -44.02261 | 2024-12-03 04:29:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 611a015e-7a55-3359-aecb-6a2527ef51ca | -3.5059 | -50.05855 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70bc4e2a-fdec-3153-ba2f-53858a3ce62e | -2.63658 | -51.76172 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b63e295-1235-3818-9024-d9a17645d425 | -2.37087 | -53.85411 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08a2841e-2c8e-365a-a3d2-859e7bb4e937 | -1.74497 | -52.78502 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3395feb1-b6b4-361b-b4df-aadd534b949a | -3.95605 | -44.04873 | 2024-12-03 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7689b4e8-8f91-35c0-99fc-873b6ad88e90 | -3.93259 | -46.70423 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b0c4bbf-9381-333d-95de-a67b55b28d91 | -3.36082 | -50.05753 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc384bf-38b3-343f-bb3a-5fdcd1c2339f | -1.78613 | -52.74952 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc09dfcb-1bd6-3c11-9a9e-b17eaaa244a2 | -3.11969 | -45.99361 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b57feb65-0906-3d61-8a85-171d7aea005b | -4.47633 | -45.71598 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3699d510-e40e-3129-9b97-d35a706828a5 | -3.08596 | -46.55799 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d92e059-6427-398e-8f6b-4a443f427f8d | -3.31823 | -44.91202 | 2024-12-03 04:29:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7f86664-f286-3310-a89f-7d68e3098fe1 | -3.33703 | -46.05932 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e4a55c91-a587-342b-aff8-58350f5e7e40 | -3.05101 | -54.50413 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33269a4f-19b2-3c70-8648-2c99a6384c22 | -5.59578 | -46.44723 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44310b7c-829f-3352-9902-c00b4fed217e | -3.25939 | -53.62088 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9dd83db1-3e18-3dd4-9373-dee2113abbaf | -2.6133 | -51.81775 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56240db4-23d3-352e-9b98-aa352cc64bd2 | -1.73805 | -52.63757 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b382390d-d895-3f1d-a842-cbd9c58cbad7 | -2.46177 | -46.53086 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fad3b6a-7c59-394d-a261-401fd04cbe48 | -3.43458 | -50.24939 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6abaa1f0-49d9-3d60-9fd6-aecc50c268ed | -1.70871 | -52.44746 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff994cac-efd0-3948-903c-921dc9f92be2 | -3.2941 | -53.6752 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0ce11c6-0ea8-3985-83bb-c154d218f6ae | -4.0345 | -46.83328 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd12dc12-3c49-3a70-b687-c3ab29223ad8 | -2.57226 | -46.19444 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5eddb33-cedb-3c5b-b5c5-5ee37212a572 | -1.90186 | -52.89883 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e5c1dc8-c434-3aa8-bcea-38cafb8b4f5f | -4.82419 | -47.32051 | 2024-12-03 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README42.md)
