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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98b397c3-8f3c-350b-aece-8f0f1f70a5b1 | -11.52102 | -43.623 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49c9ca54-4820-370e-87cf-bd746b8debd6 | -20.25474 | -55.50433 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ab1116d-9e78-37c9-85b6-4c53b12b6924 | -20.37155 | -58.06692 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1a38a0ef-5f9a-3735-a1ea-c5b8b7bc7818 | -18.04944 | -43.84446 | 2025-09-22 04:19:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca194940-7d65-336c-84fd-c647f9379115 | -11.51824 | -43.61891 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a283fd3-40f0-3ff8-a4c6-ed46323baa29 | -10.00117 | -46.27091 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79df2ed8-45de-38b5-97f9-99cee17bd530 | -15.0441 | -55.29247 | 2025-09-22 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6dca608a-d184-3fd6-a856-1fe7d9f44d27 | -15.15699 | -49.58486 | 2025-09-22 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5e74ef7c-1450-39b2-ac2e-e78f6bd0fcdf | -19.44021 | -45.17738 | 2025-09-22 04:19:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea564ee6-19c3-34cd-aef4-c55a7390a8ad | -20.40487 | -54.86331 | 2025-09-22 04:19:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8910f603-2b58-3347-8339-9a64fc1ef3f4 | -22.41434 | -46.78458 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e26608e-0dd8-33e7-825d-d9ba34bdd8a4 | -15.5353 | -44.32106 | 2025-09-22 04:19:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e9eb07f-8c5e-3be8-a05a-dbe3fc93a648 | -20.91077 | -46.22111 | 2025-09-22 04:19:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 73f24145-079c-34d2-b8bf-f6e346a934ff | -21.06613 | -46.98663 | 2025-09-22 04:19:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa390508-1afa-3da2-9646-8e139563ab4a | -20.54973 | -56.15239 | 2025-09-22 04:19:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc6bf4c6-568c-3d9b-b24d-1c257b6e6b19 | -17.60439 | -44.16343 | 2025-09-22 04:19:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b341f7c2-1196-3b86-88fe-34003ed75f87 | -10.37768 | -46.06675 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d7973a7-fe9d-39bd-a4f2-38ed03c634f3 | -19.40392 | -44.33006 | 2025-09-22 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a83f75bb-62a1-3ef0-bc1d-37bcead39c17 | -15.95877 | -59.38253 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7b9e4ff1-5f87-39e2-971d-6d597f058012 | -11.50327 | -43.56889 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90b7abc3-d98c-3e01-8cd0-a85ed4e7e499 | -10.36387 | -46.0645 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 585ad7f4-ff5f-3cc9-bbce-999d49aa473f | -19.86534 | -46.10205 | 2025-09-22 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9521a00-c15b-3206-bc7d-d084b3a050ac | -15.9489 | -59.39375 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c10834d3-9583-30aa-a778-f0e6c999ec10 | -10.34703 | -46.07034 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a31362f-169b-375e-b3a9-d3e0d6dad140 | -20.4645 | -44.99616 | 2025-09-22 04:19:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9ac3450-42a0-3e66-8e08-568b1a7e1bfd | -10.38143 | -46.08701 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae369ef2-4da9-3970-8095-ffedaaf99856 | -10.25603 | -46.06274 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1126d805-451e-35af-911c-2fee3a125a9a | -14.77219 | -48.60847 | 2025-09-22 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b02827dd-d1b3-384b-8656-bed41e24facf | -15.42804 | -46.19388 | 2025-09-22 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f98c3a5-eff5-3f0b-b806-88722a0d59c2 | -20.274 | -55.4927 | 2025-09-22 04:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 90.5 |
| cf7a5fdd-70f2-3c89-a05c-63d22284f741 | -15.9591 | -59.3887 | 2025-09-22 04:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 866eed3c-cea6-39bc-91c2-8a1686d55ba2 | -15.9594 | -59.3687 | 2025-09-22 04:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 64758893-cde4-377c-bca5-5b7057cb5b20 | -20.2537 | -55.4959 | 2025-09-22 04:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 622e7739-cc21-3b60-b276-f81eecaee959 | -15.8412 | -59.5199 | 2025-09-22 04:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| cb329b7c-cac2-3348-9b54-d8344edb66b4 | -16.0163 | -59.4633 | 2025-09-22 04:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 843ab86a-8b9f-35f2-a9fc-5de2171733e3 | -22.91165 | -47.43701 | 2025-09-22 04:21:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1cc42bf0-60f2-3378-88fd-a0073c922513 | -21.83666 | -53.96013 | 2025-09-22 04:21:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c8bac2c1-896b-3326-8d76-0e6f4df31818 | -22.91105 | -47.44077 | 2025-09-22 04:21:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9f177038-02ea-39a9-975f-af126181a963 | -23.05355 | -46.80147 | 2025-09-22 04:21:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fe653570-ff57-3b17-8af9-a4a126c02492 | -21.83646 | -53.95789 | 2025-09-22 04:21:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de235bdd-7222-3540-a883-93e821481119 | -22.72525 | -50.66777 | 2025-09-22 04:21:00 | NPP-375D | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 5cf54afc-2fb6-3624-89c4-d6ebf58be0a9 | -21.83294 | -53.95197 | 2025-09-22 04:21:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 356a656c-1e73-3f11-bcb6-48ca3c6c68f6 | -23.05296 | -46.80523 | 2025-09-22 04:21:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6f94d625-bba8-3a0c-b541-97c77f37736c | -21.83416 | -53.94941 | 2025-09-22 04:21:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8473431-3de9-3fb6-90ba-3edc9e18bd6c | -21.83515 | -53.9446 | 2025-09-22 04:21:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 438b1136-bd8e-3c52-adb6-410bd77781eb | -22.72808 | -50.6732 | 2025-09-22 04:21:00 | NPP-375D | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 0299c9d5-d4cd-3f05-a42a-61874baf0e90 | -21.8339 | -53.94713 | 2025-09-22 04:21:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65e8aa2e-52e7-3d37-be37-e2d49ef63250 | -22.72723 | -50.67784 | 2025-09-22 04:21:00 | NPP-375D | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f76d156c-0313-357c-b160-9c1ec0de3449 | -23.80129 | -46.8401 | 2025-09-22 04:21:00 | NPP-375D | EMBU-GUAÇU | SÃO PAULO | Brasil | 3515103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| fee44eb7-826c-36bb-8274-8d3aa130d885 | -22.86822 | -46.58263 | 2025-09-22 04:21:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 515cf8b1-4cbf-32be-8e04-8cb9df09b40f | -21.83068 | -53.94349 | 2025-09-22 04:21:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 190b3ec2-94b3-33aa-81b3-ca343f377ef5 | -22.72891 | -50.66859 | 2025-09-22 04:21:00 | NPP-375D | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| dc07c31c-74f1-3d66-badb-cf39550463dd | -22.73174 | -50.67401 | 2025-09-22 04:21:00 | NPP-375D | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6aee1dc6-bd76-36ff-b346-a9c5b3110b2d | -21.84115 | -53.96119 | 2025-09-22 04:21:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a28cde5b-1221-3482-b629-b44d5c573ea5 | -21.83485 | -53.94231 | 2025-09-22 04:21:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfa0e145-155f-3cc8-8c15-c7aee19262a4 | -21.8355 | -53.96273 | 2025-09-22 04:21:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 828c366d-a9c1-35ec-81ab-88697a8000ee | -22.72441 | -50.67239 | 2025-09-22 04:21:00 | NPP-375D | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4b596831-ed83-32f3-9fd1-047cb8158ecc | -22.9488 | -46.07986 | 2025-09-22 04:21:00 | NPP-375D | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d64885fe-fdc0-39c1-98e8-9dc7c54fed73 | -22.72357 | -50.67705 | 2025-09-22 04:21:00 | NPP-375D | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5c2f6216-82e1-3e4e-8d49-5774250b600c | -2.45652 | -47.27611 | 2025-09-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cda0fef-d870-33f3-acbb-53f6fe0846ed | -3.14121 | -44.42805 | 2025-09-22 04:36:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79058d8a-9377-37a5-9909-8e264c129316 | -3.16006 | -44.32857 | 2025-09-22 04:36:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a670928-8646-322e-8220-40346a1df94f | 0.53156 | -50.91541 | 2025-09-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c663a0e-57b6-3590-aab6-e477eeb63df3 | -2.25243 | -47.88128 | 2025-09-22 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac06557f-6bf2-370c-b2c6-baefa9fbcaf7 | -3.13619 | -44.42095 | 2025-09-22 04:36:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 176b7034-9d7a-3541-a976-88b8c56e6a89 | -0.95197 | -47.35915 | 2025-09-22 04:36:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b651f3a-54d6-3420-ba03-db57df26a723 | 0.52797 | -50.91599 | 2025-09-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b51fdd2c-f32f-353e-b797-effd6e6db7c6 | -2.41208 | -48.33367 | 2025-09-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be0aff0d-fef3-3b1e-8e80-b81f4fb2f622 | -0.95015 | -47.35175 | 2025-09-22 04:36:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe4c19b7-d3b7-3294-b998-83d445ec9b90 | -1.97041 | -47.68863 | 2025-09-22 04:36:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2ffc3bc-2bb8-36ee-a11d-85a052170eaf | -2.40931 | -48.32972 | 2025-09-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9bca6f1-e0b9-39a7-81c6-4ea4829308fb | -2.7868 | -45.48703 | 2025-09-22 04:36:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a26fe02f-7b1e-3c21-923a-0aeca240513f | -3.21746 | -43.33199 | 2025-09-22 04:36:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42924aab-9906-3c9a-82f5-95f02881dd43 | -1.34294 | -47.74652 | 2025-09-22 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be20f0dd-fb64-3634-b336-43984d032aa5 | -2.25575 | -47.88179 | 2025-09-22 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e69d2eb-54d2-38c0-8962-c203b2b53685 | -0.94627 | -47.35471 | 2025-09-22 04:36:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea567131-7028-3cac-866d-f34effd4f07e | -2.26507 | -47.84425 | 2025-09-22 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e8b946f-74c1-39a7-a6b2-cf245d4f91e2 | -2.41262 | -48.33023 | 2025-09-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4308fcd8-1322-35e5-b5b8-2496fb148059 | -1.63128 | -48.67587 | 2025-09-22 04:36:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79764d93-4281-3b33-bac8-7de01ec78a2d | -3.13929 | -44.42626 | 2025-09-22 04:36:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f4e28b0-ca6b-352f-bec4-e63a635c501a | -1.12236 | -54.14375 | 2025-09-22 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5040437d-40fe-3865-820a-3f8490d60303 | -2.64109 | -48.04465 | 2025-09-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a56214b-e348-38e0-beb2-071733669381 | -0.79849 | -47.60107 | 2025-09-22 04:36:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02969442-0641-36fe-ab3d-8909cb70c90b | -1.19923 | -46.15573 | 2025-09-22 04:36:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ed3f1b3-6538-33f6-af70-da5c37d91bf9 | 0.69161 | -51.46229 | 2025-09-22 04:36:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7daca4fd-2df6-37bc-b41b-b92f08037eb6 | -3.17215 | -41.06009 | 2025-09-22 04:36:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f55f6c59-0086-3b3a-a26e-3a480463dae2 | -0.9496 | -47.35522 | 2025-09-22 04:36:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d277b9d9-8814-3f15-8c27-140ba391a2c3 | -0.94682 | -47.35123 | 2025-09-22 04:36:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 286e41bd-1e2a-3077-a0b7-c0a6271dce7c | -9.1604 | -44.61848 | 2025-09-22 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beed34a0-bb07-3915-8bd3-c371041f6dcf | -8.00533 | -45.71779 | 2025-09-22 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7a99828b-eda9-37d6-be2b-7619bc09e374 | -10.25511 | -46.07045 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 164179d7-cea0-3987-ae51-7870a3006213 | -7.80082 | -46.18544 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c70af2ac-6c31-3929-9b2c-70cbb4739651 | -10.37089 | -46.05325 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 070bf1fd-57b2-3809-88af-f9089f9f5dcd | -8.90622 | -46.1077 | 2025-09-22 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8410f444-1649-3a77-a55e-3f75b4e3b71f | -7.51717 | -43.68825 | 2025-09-22 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6569edf2-7d26-365e-871b-4811137f3511 | -7.61426 | -44.48254 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87f76cb5-e714-33a7-b0a5-44e6f4ccdca3 | -7.22424 | -43.7467 | 2025-09-22 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d9c3579-3393-30ea-8b63-3a755028326a | -5.72949 | -47.47978 | 2025-09-22 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11199ce5-67f1-3793-bcd6-ca84222935cb | -9.6369 | -46.64238 | 2025-09-22 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e60e0052-25f5-35eb-8e39-bde9b89a29f1 | -5.62571 | -51.699 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README25.md)
