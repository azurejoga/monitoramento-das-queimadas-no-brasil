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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a0e17ae-cc95-3a76-acf7-4903b7ce86cc | -7.53649 | -57.80709 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7ccc9513-18fa-3ed4-b961-10dd0c39ceb8 | -5.61614 | -42.72845 | 2026-08-31 16:50:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1ba68ed6-aea9-3138-80ae-5ecfc695e195 | -6.81594 | -43.54018 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 0c9fc2fa-ae86-315c-af2a-01278d4b5faa | -11.19766 | -46.10868 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| c9dc0afa-bbcd-3f2a-9a42-3b1d0688f397 | -9.17782 | -59.6334 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5965e0ca-4d3c-3a8d-b4f1-2e411ed7056c | -8.39874 | -44.99074 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 337ad51e-7726-37c6-8b3f-f3707967affb | -9.65955 | -46.06551 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c5f649db-0dd1-3d0e-9388-6ef26394bae0 | -6.93797 | -55.62861 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 69843f22-c985-3ca9-a2ab-d8323fdf2ebc | -9.67709 | -50.84798 | 2026-08-31 16:50:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 42cb9878-12f5-3143-a559-3b582bdf5b32 | -10.15793 | -45.76094 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7390dfc7-f2fc-3b8a-a29b-b9e7d441fd31 | -10.19606 | -40.08267 | 2026-08-31 16:50:00 | NOAA-20 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 1b7d6871-4112-3a72-9a28-fc0ec0a2ad72 | -11.68405 | -46.74586 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 220b7d7b-65e5-35b5-bb83-0f9a6feed230 | -13.27918 | -51.60662 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| dd1631f4-10f2-3fa0-856b-e06a03120cf6 | -7.62787 | -44.9216 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cb1b5dde-ee77-3592-a11e-bb8c57a54cb7 | -9.43316 | -37.83191 | 2026-08-31 16:50:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5ca9e941-7002-37d9-859a-d75a115b626e | -6.58647 | -35.20886 | 2026-08-31 16:50:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| b33d718c-a0bb-3d46-a414-8d8075e4c9b8 | -8.91815 | -44.16634 | 2026-08-31 16:50:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e9949bdf-16fc-36df-9111-15533cc54318 | -4.14153 | -38.57994 | 2026-08-31 16:50:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| deb86141-93fc-3895-9d9f-5903d90d351f | -11.36478 | -45.42407 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 6bf0c388-a62c-3a2d-bc52-8652ddca44eb | -13.46777 | -51.40873 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 1a2242c7-2a2b-3572-8e8c-f0617db00f6b | -13.54159 | -59.75393 | 2026-08-31 16:50:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 608bb90b-62ee-3426-a44c-d162456f8456 | -8.91815 | -45.03323 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 282275cc-b44d-3f80-81e8-e6486f0b58ea | -5.90339 | -46.12561 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8591ea09-15d4-3d83-9537-802616665890 | -13.27096 | -51.60299 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 83374d6a-e8a2-3af7-9752-b3d70c45663e | -7.52439 | -55.33459 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 16314a68-ed25-399d-be78-d1ad75fffd83 | -6.91597 | -55.70034 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5c330ee7-8b97-3487-a836-bf09c16faca8 | -11.04355 | -49.6734 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f3e7a5e1-72b9-373b-8235-94e4a58d6921 | -6.68937 | -52.88312 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 23c4409e-cc7d-35a5-9ec5-6d1191fc3fed | -10.0202 | -46.15755 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 5008f609-7d77-3730-b2a6-7d243dd11091 | -8.21777 | -54.9341 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3c3115a2-77f9-3c94-a998-8305c41c171d | -12.17478 | -50.5247 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d5245c14-761c-31fc-abce-0ef0e7066ae6 | -7.78933 | -44.0795 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 1ea20989-c365-328b-afc2-22d9f5dab24c | -7.09979 | -45.7897 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 7e5b59d3-21fd-305d-a791-e5e2d385a481 | -13.47664 | -57.03243 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 91eca617-c4bd-3a42-ba77-12327d63ad08 | -10.09812 | -50.28434 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b2073217-6a92-3c81-a659-5a989142f13f | -6.9386 | -55.63307 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| d798a303-779a-38f3-90fe-09265101d029 | -7.52405 | -44.44854 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 41fbc035-a1f3-34fa-90cb-8727c3491246 | -8.88568 | -46.02572 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c66a9b08-6425-3c2f-91ea-52d6c38ed327 | -5.58435 | -42.33592 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e144f8ca-78b5-3fb7-a23b-fcfb765092e8 | -6.91146 | -55.70098 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 22cb16da-30d5-3eae-be7f-fb01aa17713b | -11.16092 | -45.04101 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 77f81166-6cf3-3c58-a6c4-95ab6097bf5e | -10.02062 | -45.55846 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 67abc674-8062-37b7-823f-8c156205783e | -13.97302 | -54.40125 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 321bc324-5786-3143-9ea3-392c3ff70d23 | -7.52243 | -60.72897 | 2026-08-31 16:50:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 97e6e17a-2eec-39a3-ba6a-b72bdcb6b89c | -10.1555 | -45.74571 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fbac69fb-3ae5-39a1-a3f7-6b1d9d9eb6c7 | -7.98268 | -46.51998 | 2026-08-31 16:50:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a1f5ef36-0916-340e-baad-2141897f6cd4 | -10.75125 | -54.06327 | 2026-08-31 16:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2412ca51-7b91-3a37-b0b3-dee2f430672b | -11.91307 | -45.05333 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e3ed6474-14f2-3eef-9c36-15f637f0485f | -5.90044 | -46.13024 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 21f49da8-d5a5-37d1-8884-9ea367bbe6fc | -8.74874 | -46.46761 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fcafb931-3cb5-30cb-a689-313df915a4f1 | -7.75416 | -62.31141 | 2026-08-31 16:50:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f2465337-0806-3dbe-b937-26195deafbfa | -7.85187 | -45.17851 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 75e51f47-ad99-30f8-927c-c1a6aaab07dd | -8.24131 | -54.94354 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d25fe563-8cd4-3014-b6db-17179c96a43f | -5.76566 | -44.1284 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 32c16760-cfa6-3ff7-a18e-4cc17d5f0bc5 | -12.87996 | -45.84186 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 3aceb170-2a75-37df-898b-83ddfe95274f | -10.15092 | -45.76201 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| aa7e3735-1aa7-3562-b4bc-cae5b4994a6f | -6.81946 | -43.53571 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 4eab3bf8-6cad-3a1d-a524-d5f946126d90 | -11.24789 | -51.26126 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f0bbaaa3-9e00-3a99-9a3e-26c605b0fa35 | -13.27032 | -51.59834 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a52efde5-fe0c-3835-88fd-08c846e56bd0 | -11.24383 | -45.14556 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| aa82cc8b-0ac1-3602-9236-159f6c6d6903 | -11.2188 | -46.10919 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| c146cd94-f309-3f0d-adb1-2f71a07d2bab | -9.66053 | -48.27894 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1d05be00-77ee-345e-ac45-cc46ed321bba | -10.8453 | -46.00753 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fd05a3b7-23fb-32c6-99c5-c3bbbb432aa1 | -6.84472 | -41.69323 | 2026-08-31 16:50:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| 70850306-1988-30c7-ae58-ff506d75e644 | -8.85312 | -47.08243 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4c842735-ad12-33e6-9bed-b7d9f913779a | -11.04945 | -47.11863 | 2026-08-31 16:50:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ffa6ed5-d27f-32b5-b57a-4be1971e68a8 | -12.11246 | -45.02917 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 08eb4ba6-a090-34f8-b077-829b384cfaf2 | -8.07509 | -43.61216 | 2026-08-31 16:50:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 67054134-0f5c-3c46-a609-ab318efe7f63 | -6.923 | -55.7178 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d0f64476-c3a7-3274-88ee-4ff018c9066f | -10.02378 | -45.55426 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bdf2003b-ca52-3768-b7a1-2b9fd5c7f1a3 | -8.97004 | -50.8116 | 2026-08-31 16:50:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cc79fb36-4f8e-30bc-a796-137ddc3956da | -8.73967 | -39.00845 | 2026-08-31 16:50:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 6038d8b6-eae0-31bd-baeb-a7333bec9ca0 | -11.2074 | -45.10109 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a4af5687-b42d-3fa5-8c7f-26c9e35e52b5 | -6.68415 | -38.49324 | 2026-08-31 16:50:00 | NOAA-20 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e2aa68ca-d36a-3138-870d-7745126d2db0 | -7.92727 | -61.3496 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2b749784-f11f-3111-98f2-8a9e0a127bbd | -13.84445 | -54.09145 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2c79c07e-e130-3515-ab1a-61280b6d9720 | -12.92004 | -45.85032 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7be9a94c-c269-33e0-8bf6-b95d71c03327 | -10.45435 | -46.74691 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 73104662-d385-3925-b4ae-89fd609d4992 | -14.12039 | -52.80332 | 2026-08-31 16:50:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fd1e0520-c6fa-385e-b504-e9282212d8bb | -11.48198 | -58.52243 | 2026-08-31 16:50:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 3df3690b-517e-31cb-9612-e8b4a754eac6 | -11.24989 | -45.11522 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 11e150e6-7fd7-357b-a537-d71d164e15ac | -8.53348 | -55.26575 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e7d9534c-c9f9-37a2-b16e-325bf636ba4a | -11.51644 | -46.93196 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e65530cc-7f6e-37fe-a121-53229f091345 | -8.0395 | -61.72673 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b92fa271-8dfc-39ce-845d-757424c02d46 | -11.91239 | -45.04921 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b72b7872-1dc7-3b3d-85d7-7d25031d4ffa | -7.636 | -44.82722 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 07f3d4f9-c597-37fe-86e0-35ee7daec8c9 | -13.40328 | -51.66796 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9933c026-2f0b-3187-bbd0-9063237d76d2 | -9.16262 | -60.93764 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 66d2f5c0-56e9-3afd-8db3-bc0fa9556a8d | -8.50523 | -55.29245 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 74550077-6fda-35d5-80bf-153dffab2f9e | -7.6368 | -46.73047 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 35e2eaf0-7418-3600-b2c4-a4d561cf2e66 | -11.2103 | -45.09638 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 1ce28a6b-fe7b-3cc5-a60b-eae62519f650 | -6.93987 | -55.64197 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 37303a27-a5ec-334e-8a5b-605cfeac613b | -11.21371 | -50.61777 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 33012822-22be-3683-a5dd-aba2c0809893 | -11.19972 | -46.12075 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 653b5676-f218-3dac-a93a-ab99e6e4718b | -7.61313 | -57.61996 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c993e908-ed74-33b1-8ce6-03da18ab2edc | -8.81138 | -62.49343 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 7645a192-c7c8-3211-822a-8b2b3825eafc | -12.07841 | -47.20756 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 717116d5-548b-3eed-92ea-c8f66c0df2f3 | -8.61411 | -54.78152 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6e877c30-8d2e-317e-9692-c618246e49ef | -9.64852 | -46.0633 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9b6d296e-1501-3dda-a3bc-a2ca6ccb546e | -11.79739 | -47.67345 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |


[Clique aqui para ver as próximas entradas](README163.md)
