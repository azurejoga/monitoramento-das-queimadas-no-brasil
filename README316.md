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

## Dados Diários - Página 316

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48a25889-242d-31a6-87ef-ceb080af8da0 | -10.42138 | -47.54491 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8fa3bf81-bf27-338f-9797-0596ca0ecfca | -9.94347 | -50.14983 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c35e1e2d-cb32-3492-b4f0-30ea78c03c9e | -8.21167 | -46.41173 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| af9a7a9d-274d-3b48-acb3-4da5ba80fa0a | -9.84278 | -47.48545 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7c4440de-e580-398d-92ec-9c8d00bd86ec | -6.69429 | -45.29279 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| abaa4b3d-902d-34da-8db8-46f2fccd8933 | -11.79504 | -46.77676 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 78586c73-f0d4-3d32-8332-cdbb3d9a6725 | -11.59261 | -43.67181 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 65c95673-e4c0-346d-9f77-6aa9b95eb0df | -10.98996 | -45.40294 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 5011f742-3053-33b7-9f9b-59fe85769e83 | -10.82119 | -47.33837 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 32bcba89-0ee7-34c1-a2e0-c926cb63c701 | -7.1646 | -47.78802 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ac2c25c-d6c6-335a-89d0-92226e27e9ce | -8.97039 | -47.55817 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 34334bf0-ee47-3e72-94ad-6ae666fd0931 | -11.10947 | -39.42007 | 2026-10-08 16:37:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 17b9667f-4e55-383a-87c9-788f19dfac71 | -12.94024 | -39.58206 | 2026-10-08 16:37:00 | NOAA-20 | ELÍSIO MEDRADO | BAHIA | Brasil | 2910305 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 7cc93468-3fbf-302f-bd52-ad831466b2a3 | -6.34691 | -43.38737 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d29cfab0-bf16-3eb6-8262-f7ea7823a158 | -18.05567 | -44.59767 | 2026-10-08 16:37:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8ebc4961-928d-3f56-bbc5-39000036ee59 | -11.82424 | -47.31377 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d75403cf-10ce-3db0-a98b-f82613a11a39 | -8.94195 | -45.18866 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1294ce7d-7c8b-35ee-9540-606ae2de7b56 | -5.83082 | -42.42623 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 56073493-80c4-395d-af2c-723b1d622216 | -8.77896 | -47.25962 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0fe7280c-d5b6-352a-883a-fa70dab5d20e | -8.55563 | -46.91429 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 4a407395-3a5f-3d34-b113-a18dd110ce32 | -7.87931 | -54.98099 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 36e2531b-deeb-3f2d-bdac-5f8b3d543669 | -11.20281 | -45.21803 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 5b6df621-a223-33e0-9ac0-9e14587ded9b | -18.05176 | -44.59448 | 2026-10-08 16:37:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d1a73dd4-ef34-3097-837e-9e8372a29b57 | -6.88504 | -43.69329 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 5c0a33dc-d082-3361-83d0-f3997141ca27 | -12.70907 | -45.81101 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8aba0d70-ea62-3327-b950-7e5a3aedbec6 | -11.40697 | -47.54868 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 84af527f-56ca-3800-b29d-ccd618991edb | -8.58709 | -45.68734 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7e14069-48fb-3cb4-9fd1-7403668ed6a2 | -11.11234 | -41.31927 | 2026-10-08 16:37:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 0601169c-ece3-3b0e-a135-4cd36cbd3136 | -9.76623 | -44.78674 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2c1aed23-3cc3-3d12-be4e-0fc8ea1f08e5 | -6.95209 | -44.41167 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8c038026-5668-33c0-8c36-3054006de77f | -10.94382 | -47.91448 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7d8f08c9-cf79-3d82-844f-41a7596b58f3 | -6.86101 | -39.1539 | 2026-10-08 16:37:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6c2d7a51-0704-3985-b264-9faa6d71cc24 | -6.89925 | -38.53673 | 2026-10-08 16:37:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 44886f6c-bdc3-3b1a-841f-c02b1110d2d0 | -7.23282 | -37.94756 | 2026-10-08 16:37:00 | NOAA-20 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 12.7 |
| ede5ef24-2d34-37bd-8bbb-7ae151d4e30b | -7.73946 | -45.44566 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| dc09f093-26ee-30b2-9ee6-56129a90485f | -8.9475 | -45.18067 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| ccb10731-7219-378a-ac70-27dc285c9822 | -5.75275 | -41.62704 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 2fdd2b8e-c28b-3fed-b6a6-9cea430f6635 | -9.88609 | -44.86037 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6d8a8dff-1c50-3939-8e64-fa92dc547772 | -6.61874 | -37.89801 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 20809a45-23c9-388d-b136-4a4ba6ab3415 | -8.04324 | -49.40148 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fc9c8cf1-bd56-3c51-9453-7892f36581ca | -9.52803 | -45.60476 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b2d2bcde-1793-33d2-b024-d64d07d61ec7 | -18.64278 | -43.26208 | 2026-10-08 16:37:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bcef7fcc-be64-3772-9935-eed7c5c3594a | -10.60693 | -43.84148 | 2026-10-08 16:37:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 40c30cfb-06c4-3b41-97e7-d4a6fa8d1e12 | -11.77661 | -46.76747 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 207c7edd-6fa2-35e6-bfc8-56c75b532492 | -11.11247 | -44.0108 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1d5a4af7-db74-381a-892c-fb550263c771 | -6.1957 | -37.86228 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 0bdc3339-5d1a-3ca4-bf61-d6fb27427ba2 | -6.15596 | -39.44216 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 517502cd-92b6-3b74-b15f-167ac94bb5cf | -9.03421 | -44.37591 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 013c1849-c882-3e7a-8cf3-836a99c5e0a5 | -11.24872 | -45.25281 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1efbab2a-a5ec-3918-a567-8885e42ba1cb | -18.97037 | -45.59279 | 2026-10-08 16:37:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7b206b84-dfc8-34a5-beae-8ae1ed16074e | -11.52486 | -48.22116 | 2026-10-08 16:37:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cd53a7f9-5a96-333f-bfd5-9c6d57955202 | -11.70815 | -40.58546 | 2026-10-08 16:37:00 | NOAA-20 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 6f1f5596-e238-3663-9e23-1780849091ad | -8.29897 | -45.73257 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 176.4 |
| ecb91759-fe74-3ea2-a511-a8dc7f6df845 | -6.04293 | -42.6037 | 2026-10-08 16:37:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 0f6d98cc-3917-367e-992e-dd1c5edd7bcc | -8.07584 | -45.60448 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7773540e-cfbd-3b87-ae4e-4f77d9e3ccc7 | -9.69357 | -58.10847 | 2026-10-08 16:37:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| da5f0a4f-6d3a-381c-bc10-a3dbd6704de3 | -10.51702 | -47.31064 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 16a8765f-fd57-3141-937c-375404a8e4df | -6.97581 | -47.67129 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2fa7b89b-e7dd-3caa-8bcb-83760ab822f3 | -5.81336 | -42.5054 | 2026-10-08 16:37:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c4a61103-4e9a-3623-afc7-3a4d124d1635 | -9.83014 | -45.76397 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 889f9684-7ef8-306c-a9eb-3ff532aa2dcd | -13.02054 | -47.20048 | 2026-10-08 16:37:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2ff85e08-31ba-3bdb-8baf-3ae9f3694a5d | -6.81158 | -44.18473 | 2026-10-08 16:37:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9a83f368-7783-3644-b059-f20dfe9d6da7 | -11.13838 | -46.11907 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6bfe918f-9b0b-312a-825e-720cdb2c3959 | -10.47389 | -47.85994 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 7e54d857-64ad-34a1-bd77-e6f2433c934f | -9.84404 | -47.84657 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2a5a560e-149e-334b-99b1-cebc5f56feb3 | -7.21609 | -44.28088 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b19b7e6a-782a-3d87-af75-9606d326bfa9 | -6.50693 | -46.08522 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d7d8ad00-7f54-330d-971e-d36c397e1062 | -18.97094 | -45.59686 | 2026-10-08 16:37:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 09d30c82-b448-39a5-9e9e-dab4832bd41f | -11.8499 | -47.39188 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1e3a666f-cec7-3d26-a6e9-33214a577394 | -6.60385 | -37.89966 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 45.8 |
| cde9331c-3d64-30df-b1e3-2e4d7feab59e | -8.51082 | -50.2567 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bdac96ca-a42c-3e9d-945b-34c370264712 | -11.14444 | -46.13659 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 46448316-b917-3960-912d-87e06549be06 | -11.95711 | -47.76678 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1f2e8c64-5d1a-3ca2-ba7e-cdce0de69315 | -18.98551 | -44.45261 | 2026-10-08 16:37:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25f478f8-883f-3ab6-b4d2-fa742c0d9457 | -9.434 | -48.1561 | 2026-10-08 16:37:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b18f15f7-f75b-30e7-979d-08ae35ca839c | -6.95489 | -45.24374 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b10d18f0-ff3d-3316-8a2d-582ced2b6fb0 | -12.15592 | -44.72516 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| e5ee2ca7-865b-30f5-a7db-e26a1330cdc1 | -9.85097 | -47.46837 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 336a66fd-6c0d-31dc-bed2-fb6845f55aab | -9.23767 | -46.46686 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 15c964f0-41e0-3d67-a43b-00db54e0a241 | -12.94214 | -39.58548 | 2026-10-08 16:37:00 | NOAA-20 | ELÍSIO MEDRADO | BAHIA | Brasil | 2910305 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| f15f83a5-00dd-3adc-8bed-5bceb461b5c6 | -7.71731 | -44.73018 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| ae054e47-22d8-393d-91fa-872103ea9afb | -6.90544 | -45.8947 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c40f21e9-a083-39c1-a20b-412bcc80f5d4 | -8.19601 | -46.35296 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dd8d680e-eeb9-385a-8c19-1b9f880f09ca | -12.1726 | -44.81256 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ab177384-e151-3447-b58a-98234ffb1b50 | -8.59369 | -44.86542 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 99131cf9-84e8-33d3-9913-71995d8670e5 | -8.9773 | -47.55714 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a72bda18-9e82-3d63-9578-c14043c61417 | -11.76903 | -46.78767 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6d50d12-ef74-36d2-bd1f-a7834691f3d6 | -5.18481 | -38.44865 | 2026-10-08 16:37:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 6fbc8295-ba1c-3fcf-8a9d-33ae2fc4944a | -9.54506 | -46.85619 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0a1ec83b-ffc4-3793-ab68-909182512b86 | -11.22747 | -41.58326 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 6ee391cd-d240-31f6-ab30-81a677f9acdf | -13.69267 | -48.63875 | 2026-10-08 16:37:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ee460604-4288-3201-acc1-d8329182a8c0 | -11.82886 | -43.52974 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| bf33196b-78d7-3aaf-8172-eda6ffc70e16 | -8.19239 | -45.76738 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 57e4fa66-a173-3395-b1ed-64aa8026102c | -11.85521 | -47.37877 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5cdf4ec7-165f-3116-a5b6-a6bcbb42a540 | -14.67153 | -51.44954 | 2026-10-08 16:37:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acfd8c63-9929-373c-8f23-b541cf4c152b | -13.59549 | -48.20579 | 2026-10-08 16:37:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 36aedcdd-d688-3a0f-845f-22536b4c982c | -9.13838 | -45.83163 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cb5c3dfa-4e46-3cad-8ea5-0be887eb82d4 | -6.22284 | -44.96652 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f94cfe9-9720-3c1e-8920-988987b149be | -11.58094 | -43.68481 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f7076fa9-04fa-3ecb-a394-018921602b64 | -5.9855 | -40.92254 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |


[Clique aqui para ver as próximas entradas](README317.md)
