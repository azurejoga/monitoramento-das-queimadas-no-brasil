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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67a842f9-87f1-389d-a8b3-6c15f6103ba5 | -9.5025 | -57.8032 | 2025-09-04 14:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| a7d576b0-972d-3569-bc63-e18bcdda5a4f | -5.774 | -45.2639 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 9e3e2347-d3d6-3a24-a6cd-7e1ebf1e631a | -14.5852 | -53.0268 | 2025-09-04 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 7cb65222-2c72-3e22-81e2-162bad18a49c | -11.8524 | -51.4954 | 2025-09-04 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| fcb347ed-738c-3a2e-aaba-6720c5e7d1a2 | -9.6851 | -51.0186 | 2025-09-04 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 06025f64-f572-3578-b955-8d9147372fed | -5.6963 | -45.6076 | 2025-09-04 14:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b5a03607-c144-301c-b31b-40de20d56f91 | -11.5963 | -52.155 | 2025-09-04 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 92dbbab6-9bc3-3e10-9475-20345dbee0c1 | -10.5129 | -57.776 | 2025-09-04 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b82c2c8b-e164-3a82-800e-a081bbf58d7d | -11.5856 | -47.7836 | 2025-09-04 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 49faf312-0f8c-3322-83d3-91f6f206257f | -6.2315 | -42.4515 | 2025-09-04 14:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 202.2 |
| e63c4060-e4c3-3878-8435-122bcc92913a | -6.7928 | -44.4776 | 2025-09-04 14:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 85386986-927a-3b0e-8312-a3458ae8d190 | -5.6965 | -45.5851 | 2025-09-04 14:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 0b8a1c98-e359-30b6-b2fb-15e3fdbeeb8f | -5.7177 | -45.2905 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 80f55bd6-7e4d-3dba-a39d-bb85d4e3528f | -15.9703 | -55.9583 | 2025-09-04 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 09a06d8f-a765-3645-ac49-220b7e765e9b | -11.6601 | -54.5093 | 2025-09-04 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 39102a26-90ad-3d11-8c1b-22bb173f0969 | -5.7189 | -45.1547 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| a461b499-4989-32fa-aa37-ad5da7c01d2c | -16.0474 | -47.835 | 2025-09-04 14:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 80.2 |
| fcbeee7d-4c04-33f7-811c-18b229d2a7c0 | -11.3701 | -43.6104 | 2025-09-04 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.5 |
| cddb53ac-3644-3c2f-bc22-2f9724e08196 | -5.8108 | -45.3291 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| fe9aa5d0-d0b7-3382-a6c1-7f49f2ed497c | -15.0258 | -48.1014 | 2025-09-04 14:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 0a84b6f4-e832-3211-b9e4-ab3c83a3a99d | -5.6777 | -45.6089 | 2025-09-04 14:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 34eb5fee-7d3a-3035-a166-d5bef8e93807 | -4.9049 | -41.7696 | 2025-09-04 14:40:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 198.5 |
| cd5ad4ff-c3bf-3a2a-963d-65834464bb25 | -11.3901 | -43.5602 | 2025-09-04 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2ecfd81c-a9b7-367c-ab05-590ce575c85f | -11.5972 | -52.092 | 2025-09-04 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 34867240-02fc-30fb-8249-f5fa0a281b33 | -5.7736 | -45.3091 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 810f3108-f993-3a7f-bbd6-2a71869bb303 | -13.0886 | -57.1327 | 2025-09-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7c26005d-e7e4-3bb8-b74f-ff6a77b6804e | -11.5969 | -52.113 | 2025-09-04 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 5e24684c-6fff-3593-ba57-60e0806d7909 | -5.7528 | -45.5587 | 2025-09-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 53c89535-1360-3f4d-b3a4-a05dd710cc29 | -12.9859 | -54.7891 | 2025-09-04 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 164.5 |
| d2d00f6d-8708-38ce-810a-b40bce7e8577 | -11.7884 | -50.6735 | 2025-09-04 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8460ec23-3c75-3e9f-9678-3eb852e7003d | -4.9951 | -56.256 | 2025-09-04 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 56923d87-7f98-35ae-852a-9deef9640c77 | -6.0317 | -43.6873 | 2025-09-04 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 542c827e-af12-33e4-9d31-0476b259234b | -8.3644 | -48.3116 | 2025-09-04 14:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 2920f710-a4a7-3e0f-8a65-2c7f9b6337b9 | -6.2318 | -42.4278 | 2025-09-04 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 126.6 |
| cb61e12b-608d-3a0f-bf12-ffa0aa833355 | -11.3705 | -43.5868 | 2025-09-04 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 7c752954-0431-32dc-adbd-6fc31ce888e9 | -15.229 | -52.7101 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 276.1 |
| 1fff5e64-1383-33c9-8941-c2b80fc3384b | -12.5173 | -48.0584 | 2025-09-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 7f4da1d0-148c-3511-a2c1-bb2ef0453fa6 | -10.9867 | -45.9325 | 2025-09-04 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a7626085-45dc-3196-a3c7-b7c5ea02a63e | -5.6813 | -45.18 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 43c9d84b-5e47-3762-9705-3bd0fbbfe97b | -12.4593 | -48.0885 | 2025-09-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 7bcaa9ae-b841-3b02-852b-14bd38d5781a | -15.2026 | -48.027 | 2025-09-04 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f5c66cec-5fc6-3bf7-81ea-b0148cc843c9 | -12.9861 | -54.7685 | 2025-09-04 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ad115889-4129-3ac0-be27-cbc95796df28 | -5.7 | -45.1786 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 60c83e14-7c22-3128-a93d-03e2c5dfb284 | -8.0799 | -45.339 | 2025-09-04 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 136.5 |
| de7e631e-88b8-3190-8600-9261f321dca5 | -13.8457 | -47.9764 | 2025-09-04 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 19171f24-726f-3cca-907b-7ebff092990c | -7.6851 | -48.7386 | 2025-09-04 14:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 360.9 |
| a7dfb246-3cf9-3146-b2dd-f426ecc25019 | -14.9865 | -50.0769 | 2025-09-04 14:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 525c1beb-4bc4-3d3e-8e74-60dc155f5ad7 | -11.2005 | -55.0195 | 2025-09-04 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 3f23e237-8f64-396c-a1e7-601b383893b4 | -12.4985 | -48.0388 | 2025-09-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 5994dbac-3238-39c0-8d69-91bb15aa4cd3 | -9.3014 | -47.0986 | 2025-09-04 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 5b4b239c-3e90-38d8-8d5f-843f2458f35d | -15.7366 | -53.6561 | 2025-09-04 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 283.8 |
| fae584e4-f0f3-3825-a508-4cab862d88d1 | -8.1028 | -49.9481 | 2025-09-04 14:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 7d659370-4d9a-343a-bb2f-9631f6f53f6c | -7.7409 | -48.7772 | 2025-09-04 14:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 4eefe06f-b39f-3a4c-81c9-e3c386408cc2 | -11.3897 | -43.5839 | 2025-09-04 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 329.5 |
| 46dbe1ae-1e43-3440-9d76-26fd405c45bc | -9.5023 | -57.8229 | 2025-09-04 14:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| cc93cd59-ac25-3233-a061-59c64390f829 | -5.7341 | -45.56 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| e19829ba-7273-3b44-8110-5fd1acf87861 | -9.0141 | -45.9886 | 2025-09-04 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4f5b0af4-dfa0-3e1d-9678-7c2a34b8cca3 | -9.4376 | -46.7947 | 2025-09-04 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d0d274b2-f407-334e-9b03-648f6e0a3358 | -10.4655 | -50.412 | 2025-09-04 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 6515ebc7-1184-3917-bca7-1f7336ebd533 | -5.699 | -45.2918 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| a0035bab-9475-3794-a0be-db0ca2313847 | -7.5154 | -45.3705 | 2025-09-04 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 9c583343-501a-3317-a6df-7db309729a44 | -5.4391 | -42.8925 | 2025-09-04 14:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| e9f84b55-dfdc-3281-8520-779c5b97889d | -6.2127 | -42.4532 | 2025-09-04 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 238.5 |
| 4676f67a-fde0-38ad-ab9e-051c7d5ac0cd | -6.2249 | -45.0491 | 2025-09-04 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| dea3f8df-62d9-35e7-bf15-e538d4ffb77c | -5.7923 | -45.3078 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| ba9c60e8-fa5f-38d9-bf39-80d28b655037 | -10.5031 | -50.4295 | 2025-09-04 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| b42fd3f5-dd4e-3fc0-b68a-15ff7bc117fd | -11.6228 | -46.684 | 2025-09-04 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 462841db-ef32-30ae-9924-7434a1ef6f8d | -10.4658 | -50.3907 | 2025-09-04 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 210.3 |
| b5ee6877-ecd0-3bc3-adb3-5ce1933dc1ec | -10.4818 | -53.6321 | 2025-09-04 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 2812c50c-77bb-3a68-b821-949d86b9ae83 | -6.2773 | -43.5046 | 2025-09-04 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 3b8d1c8d-2a7b-3340-9e83-ee7495dd992e | -6.0234 | -46.6562 | 2025-09-04 14:40:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| d5baa479-2c03-339b-940e-1a554e0a4871 | -8.0985 | -45.3598 | 2025-09-04 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 59319adc-916e-3703-b27d-62a30de8a993 | -8.0796 | -45.3617 | 2025-09-04 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c6dade86-c03d-3f09-9d5b-5045070800c8 | -9.3017 | -47.0764 | 2025-09-04 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| f958f54d-59e2-331b-b064-68abc8a6935c | -9.9597 | -51.6454 | 2025-09-04 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 111c9b99-c209-383e-b131-8d51f7cda42d | -10.5316 | -57.7747 | 2025-09-04 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 41216740-cc29-300f-9e3b-63d7fff4765d | -15.9898 | -55.9559 | 2025-09-04 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| a0822a02-5721-3d29-8127-7c0bb956d43d | -12.9006 | -56.9488 | 2025-09-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| ec7d63cf-4192-3436-94d6-ef86a901a694 | -8.02 | -44.084 | 2025-09-04 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 212.5 |
| c3f509ee-9888-3da8-b9e6-94ddb5d5bd5a | -13.8647 | -47.9958 | 2025-09-04 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b9a7163a-0f32-3a87-a92b-83d72bf2b268 | -11.834 | -51.4551 | 2025-09-04 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 3d259c9c-f750-3087-9d7d-de5c560d489d | -5.6992 | -45.2692 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 0ecfe40f-e844-3ef8-8e71-aba2d0646cd8 | -11.7385 | -47.7637 | 2025-09-04 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 91c5772a-7194-3c38-a210-34e7ff5697ff | -6.2952 | -43.5961 | 2025-09-04 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 8288fc98-e948-382c-af10-a41f529fcb96 | -12.4785 | -48.0859 | 2025-09-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 2807bd50-b6e6-3aa0-ad47-0e677a3fb588 | -5.9175 | -45.9511 | 2025-09-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| adc00d11-55c9-3704-a996-92316549dc2f | -6.2205 | -43.5558 | 2025-09-04 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 35a8ee0b-f91d-3129-9a61-720702c4b314 | -5.7187 | -45.1773 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8fd7dfd7-c782-3e83-9149-e9782b5e14f7 | -8.9025 | -45.8652 | 2025-09-04 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 277d2c1a-14f7-3b5a-8bbe-b3fca10e77b0 | -5.811 | -45.3065 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 936268d1-8880-3d4e-a341-bd13cd44793d | -15.4564 | -53.0183 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 0b2e7ec8-1cc2-398f-9d57-0776b16384c6 | -13.1077 | -57.131 | 2025-09-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 8e29fbf0-b60c-3ee4-b2f4-df48779be9ef | -5.9257 | -51.9599 | 2025-09-04 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5e048cd3-61b5-3213-a534-5bef6b2c11f5 | -8.8851 | -45.7541 | 2025-09-04 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| b66005bb-353b-3beb-80e3-6e745134a3f3 | -6.8514 | -44.2656 | 2025-09-04 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| e554fbd0-4c2d-34f4-a94f-8fd1c84b9c4f | -9.4023 | -48.0365 | 2025-09-04 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 4ecb13bc-baf1-3fee-848c-374b3b30ac7a | -6.8754 | -45.5625 | 2025-09-04 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 61d3fa03-fd49-32bd-addd-dd6bf80dba0b | -13.1079 | -57.1109 | 2025-09-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 258.5 |
| 5aa66c50-05df-398c-b26e-1abc007a218a | -6.2062 | -45.0506 | 2025-09-04 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 2cf2ab7f-f378-3681-a712-5536a2d3c9ff | -12.967 | -54.7705 | 2025-09-04 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |


[Clique aqui para ver as próximas entradas](README114.md)
