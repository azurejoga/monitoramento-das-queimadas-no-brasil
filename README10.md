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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d824b441-a3f9-33f4-85f0-2912005ee7a9 | -19.986401 | -55.4561 | 2024-10-01 00:49:53 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f31c7d2b-bbaa-32a4-879d-c194dc7a8b2d | -19.988701 | -55.468102 | 2024-10-01 00:49:53 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e939a15e-875a-3cd2-82d9-864ac1315199 | -19.976601 | -55.458099 | 2024-10-01 00:49:53 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2cc63210-149a-3c65-9677-5a14146af795 | -19.978901 | -55.4701 | 2024-10-01 00:49:53 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bd14d0cb-d182-3ca7-a75b-2ccb2e888a00 | -19.969101 | -55.472099 | 2024-10-01 00:49:53 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 94d4d32f-1d8e-32f5-b656-35e4c13d94fb | -19.9713 | -55.484001 | 2024-10-01 00:49:53 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 171ade29-fc49-38e6-a384-766e683ac96a | -20.028299 | -55.959202 | 2024-10-01 00:49:54 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 476ba010-a203-31b1-a03f-ff11189d04a7 | -20.030701 | -55.972099 | 2024-10-01 00:49:54 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 60abd124-554e-360e-b7fd-dbef07cfcf42 | -20.018499 | -55.961201 | 2024-10-01 00:49:54 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a2aa1846-32fd-3571-8a74-e901f3271702 | -20.020901 | -55.974098 | 2024-10-01 00:49:54 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c62e875e-43b2-39ea-9466-074941bf281d | -18.509399 | -49.417 | 2024-10-01 00:49:57 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8d0a6972-aa90-3c8a-b4fe-c7a3f28f7d6e | -18.511 | -49.424301 | 2024-10-01 00:49:57 | METOP-B | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 88d06fd4-5783-343b-8457-ab189937f5a9 | -18.5126 | -49.431499 | 2024-10-01 00:49:57 | METOP-B | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83a549bc-deb1-3f9d-b291-a19bc8c79717 | -8.66117 | -49.41649 | 2024-10-01 00:50:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e1809759-4ade-3ac6-a887-e7649fea32b3 | -8.55663 | -49.61973 | 2024-10-01 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 00c47924-d250-3866-afc2-877ce1d8ce88 | -8.55499 | -49.60722 | 2024-10-01 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| edf72437-13d4-33cb-87e5-a2472676fc8b | -9.58787 | -48.92511 | 2024-10-01 00:50:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 68e678bb-5bab-38b8-969a-50643d551943 | -10.04196 | -50.29407 | 2024-10-01 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9201dd1f-92ef-39af-8e27-d740a9e72bbb | -4.70269 | -49.81029 | 2024-10-01 00:50:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| cd744f09-e864-39cf-840d-81f31159a99e | -4.70114 | -49.79878 | 2024-10-01 00:50:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| ae9030ab-68d3-3975-87dd-cf7a31269414 | -3.94048 | -49.99283 | 2024-10-01 00:50:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 27d039de-6fde-314b-abc6-30ec7699f40b | -5.99213 | -49.67696 | 2024-10-01 00:50:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 09b733d7-5d8d-320c-95d3-d5e49b10a794 | -9.66545 | -50.92794 | 2024-10-01 00:50:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5827c30f-387f-3cc3-961f-c4fc7b0ef155 | -4.65179 | -50.99208 | 2024-10-01 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 742bed95-2d0a-370f-be08-8aa89a84331a | -4.64495 | -51.00058 | 2024-10-01 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7154efac-259e-3667-9714-6125d9b7914f | -4.64315 | -50.98682 | 2024-10-01 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8840e9ef-bc8a-39d5-bdea-d862c35ec9cf | -4.64088 | -50.99337 | 2024-10-01 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a235d4c3-a936-34e3-970f-3e85891929bf | -4.09751 | -51.13166 | 2024-10-01 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 3f5cd151-2f93-3d8b-aaf9-2d515fe12652 | -4.09563 | -51.11797 | 2024-10-01 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3e33b49e-9afa-3a01-b800-0ef774dfeb8c | -7.07907 | -39.14958 | 2024-10-01 00:50:00 | TERRA_M-M | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 51.5 |
| 42406d4e-a8e5-3946-9b3f-5a5c0a815a34 | -7.07056 | -39.15641 | 2024-10-01 00:50:00 | TERRA_M-M | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 30.6 |
| d8988d91-e0db-3225-8d5b-b8e27c9d2682 | -7.06724 | -39.13501 | 2024-10-01 00:50:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 905ad471-aaf4-322b-94cf-e04dbaa99a62 | -4.72175 | -42.6534 | 2024-10-01 00:50:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| f8eb29c9-5f73-340e-8097-586cc4748246 | -4.45054 | -42.90499 | 2024-10-01 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8406deec-1bf1-34b1-8315-18485408d0a3 | -6.24116 | -43.31886 | 2024-10-01 00:50:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5b674f5-af9a-3486-aa67-a09f858f875e | -6.23956 | -43.30767 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f24dc0b3-6b12-3410-bc23-5f42765d8683 | -5.95725 | -43.26601 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7322ca50-d697-35bc-944a-4eb376dc41bb | -7.87819 | -42.67813 | 2024-10-01 00:50:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 52d88c99-da20-3532-8583-73c729cb8716 | -7.85642 | -43.09027 | 2024-10-01 00:50:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| c7a08642-a117-300a-933b-c3bf15d831ae | -7.84825 | -43.10256 | 2024-10-01 00:50:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 612f5a26-ce1a-38f3-800c-cf3178b1de0e | -7.84668 | -43.09184 | 2024-10-01 00:50:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 5b5727a0-14a1-318c-9670-60aa985128a5 | -7.8451 | -43.08097 | 2024-10-01 00:50:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c584af43-b944-3bee-bc0a-97ebaffef482 | -7.83851 | -43.10406 | 2024-10-01 00:50:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f532b789-6e74-3d47-acf9-efdbeb728ec2 | -7.70037 | -42.99644 | 2024-10-01 00:50:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 27faa7a1-7717-38e4-87bc-02fb12d48ddb | -7.69052 | -42.99777 | 2024-10-01 00:50:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| c2ed3913-815e-3828-950a-9d0e00ab75de | -7.68889 | -42.98685 | 2024-10-01 00:50:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1e16a8ba-5f8a-30d0-bd9a-769fbb9892df | -7.65806 | -42.43419 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c7477745-4d07-3413-b77b-278f19026992 | -7.28395 | -42.25152 | 2024-10-01 00:50:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f0ba093d-19ee-3a47-82dc-14f2a1006305 | -6.7048 | -43.05245 | 2024-10-01 00:50:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8be59191-410f-302b-85a0-72a8301ca993 | -6.69488 | -43.05398 | 2024-10-01 00:50:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| ce768036-a871-335d-a9bb-d35f63e29ebe | -6.6932 | -43.04264 | 2024-10-01 00:50:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 501b08d7-2540-3b06-a9f7-c1a2ed64f027 | -6.68625 | -43.55436 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3aedd4bd-3b94-378c-9c2c-c5898d3095cf | -6.68471 | -43.5438 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f8b80c58-7a9e-3eaa-b2d4-93bc1e6d3d76 | -6.53944 | -43.04345 | 2024-10-01 00:50:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 2e7de8b0-248f-3ee1-a5d9-345640173cb4 | -6.53777 | -43.03198 | 2024-10-01 00:50:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| bb888a8b-ad05-3cc3-b8d5-ae74014b30b8 | -9.48034 | -44.06154 | 2024-10-01 00:50:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e66eaff9-4d1b-30c7-a0c4-c0431ef48ede | -3.47439 | -43.35899 | 2024-10-01 00:50:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e6f3085b-e85e-3884-8621-4ddb0227a1d1 | -6.24846 | -44.15045 | 2024-10-01 00:50:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6c375f53-68ba-37a4-aa69-4f8ae46085f8 | -6.24703 | -44.14044 | 2024-10-01 00:50:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 4d31480b-e33a-3ce1-8025-5377f983b516 | -6.24558 | -44.1303 | 2024-10-01 00:50:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e9dfe555-6c00-38f2-a858-2a91c30305df | -6.23766 | -44.14174 | 2024-10-01 00:50:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c015ce72-0ad8-332b-836e-d8846f69a758 | -6.12063 | -44.93682 | 2024-10-01 00:50:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 458120b9-0a6b-3c75-9083-2745ba6b8ef8 | -6.09731 | -44.71011 | 2024-10-01 00:50:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d457a6cb-d854-3201-834b-939c8c922801 | -6.08661 | -44.30744 | 2024-10-01 00:50:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2e9ac741-2f77-3118-8a68-e879241ef0e0 | -5.78705 | -44.14534 | 2024-10-01 00:50:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 37db8ac6-06b8-3a4c-8091-22c7d615c931 | -5.75267 | -44.35065 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 365188df-0880-3cdc-b5bf-294335c7d5d1 | -5.75128 | -44.34077 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 978e0484-e201-34d3-95ec-941f3b129106 | -5.74195 | -44.34205 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| cb1c1745-f767-3b9e-bf30-84fdf58b3990 | -5.89177 | -43.72715 | 2024-10-01 00:50:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4081aa09-6795-3746-b38d-b645554da362 | -5.89024 | -43.71656 | 2024-10-01 00:50:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7405952f-a9a8-3850-98a5-7bf65704ef3c | -5.40958 | -43.44133 | 2024-10-01 00:50:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 72bba69a-3bdb-3034-8d60-9d081ed6e2d7 | -5.39971 | -43.4427 | 2024-10-01 00:50:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7cefe0a7-8295-3fe5-8f40-d6b86600a712 | -5.3981 | -43.43155 | 2024-10-01 00:50:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b428de08-7814-3cec-ae4e-0eab9b30dac5 | -7.29658 | -44.97468 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 301e8f9c-87d4-31f5-aacc-ecbcfd086fe8 | -7.24532 | -45.00061 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 78787371-bd6b-3fd6-9c80-0f51f26a48d2 | -7.08795 | -44.54602 | 2024-10-01 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f11de0df-a987-39d2-93aa-05eddbc57428 | -6.6812 | -44.66524 | 2024-10-01 00:50:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0fabfd5b-f064-3686-b7ed-7469a7d0ed86 | -6.67986 | -44.65582 | 2024-10-01 00:50:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7c6ef599-f5d5-35c6-aec8-66b181190e7f | -7.59856 | -43.85796 | 2024-10-01 00:50:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15804ad1-a7a5-342d-aa7b-191e236363f1 | -7.59713 | -43.84802 | 2024-10-01 00:50:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0383c9bc-8916-36b7-bf0d-86d09d0fec94 | -7.30358 | -43.7966 | 2024-10-01 00:50:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c185927f-857a-3c79-be73-b8445de1292b | -7.30211 | -43.78638 | 2024-10-01 00:50:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a6d9d823-44ed-36f4-89ea-67818b696f6d | -8.75747 | -45.13494 | 2024-10-01 00:50:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ea4b5253-69ff-3e19-a770-64b2bba7ea8f | -8.53343 | -44.72662 | 2024-10-01 00:50:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c0dc4416-5b40-3f8f-a964-e384aa27d413 | -8.53213 | -44.71747 | 2024-10-01 00:50:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d927e314-986d-3342-8155-1a1132ab5449 | -8.53082 | -44.7083 | 2024-10-01 00:50:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 50a9e38b-25b6-3f2e-b728-4eb8e6cf2591 | -8.36998 | -44.80923 | 2024-10-01 00:50:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0246849f-0de8-3182-99b9-e8df026465d1 | -6.31071 | -46.08648 | 2024-10-01 00:50:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a9dfb44f-bb02-3064-b51e-ab8a84134440 | -6.2506 | -46.38027 | 2024-10-01 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e55c2b9-3a8f-347f-a934-96d3d91f4a40 | -5.57917 | -46.3208 | 2024-10-01 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c108e0e8-fc1e-33cc-a8c7-aca56c8de326 | -5.57793 | -46.31198 | 2024-10-01 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 002b7669-a583-3766-9cfb-43c96fb71b34 | -5.44881 | -46.12632 | 2024-10-01 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3362fd24-44b8-352d-9ce8-6242724ae6b4 | -5.98914 | -45.3768 | 2024-10-01 00:50:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3d48ebe1-16fe-3927-bfeb-dd959672e759 | -5.98786 | -45.36774 | 2024-10-01 00:50:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 30fa2649-d007-313e-b8b4-9c76c6336102 | -5.98019 | -45.37809 | 2024-10-01 00:50:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f10a16a2-3da6-35bb-8fb4-a648e8234aae | -5.97892 | -45.36902 | 2024-10-01 00:50:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| f75d8f74-8768-3e2f-97f4-460321358b79 | -5.77563 | -45.55785 | 2024-10-01 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1c1580c5-3297-3dca-9a8a-7b3c78c18754 | -5.77436 | -45.54886 | 2024-10-01 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 72bdaef5-fb0d-38aa-a59d-9087c973713f | -5.76672 | -45.55912 | 2024-10-01 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 75f21e42-adb9-3460-85f6-02581408ca2f | -5.76545 | -45.55013 | 2024-10-01 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |


[Clique aqui para ver as próximas entradas](README11.md)
