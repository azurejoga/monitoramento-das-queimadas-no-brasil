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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 739c8527-cdd6-32fd-a71f-70e854912d92 | -5.53742 | -42.94784 | 2024-10-24 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 64fa123d-3e98-374f-894c-b05394107767 | -5.40876 | -42.92421 | 2024-10-24 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bafc22c8-bbc5-33b5-88fe-9c2d47a05a7c | -5.40817 | -42.92567 | 2024-10-24 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c1e860ba-ab60-330f-97e9-0b3505cca5b4 | -5.32362 | -42.98366 | 2024-10-24 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 49482510-4bc7-39ee-9f89-46691797f264 | -5.46041 | -43.27153 | 2024-10-24 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb2d9b8d-090a-311d-b6ac-4f327b4b349b | -3.52829 | -43.61376 | 2024-10-24 04:32:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b1cd662-4084-3fcb-a66b-b5758408a02f | -3.52763 | -43.61807 | 2024-10-24 04:32:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 06efab02-6b3b-3a5e-9b63-f81891672b99 | -3.52516 | -43.98111 | 2024-10-24 04:32:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b5af281-888b-3ac1-a8b3-c0a04b18196a | -3.30031 | -44.08028 | 2024-10-24 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8d6c363a-9a92-3822-b6ed-0a135b16b2a0 | -3.29969 | -44.08439 | 2024-10-24 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59c52dc3-555e-3df5-b89d-5303d0c30054 | -4.85751 | -43.2572 | 2024-10-24 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 731c9b91-60c2-37b3-88c4-682728714bef | -4.75964 | -43.31652 | 2024-10-24 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5b82275-9af7-3e82-979c-7cbf62645c0c | -4.52579 | -43.42843 | 2024-10-24 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 996df205-cd22-3633-9794-b23a4855c161 | -4.52271 | -43.42327 | 2024-10-24 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1546365-1bcc-3775-838e-9fa0e2501a64 | -4.00528 | -43.25732 | 2024-10-24 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24fb5c39-e4db-33f0-bc78-ef34d9375c33 | -5.02714 | -43.60019 | 2024-10-24 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdbc6d6b-6bc6-377c-9c1d-76c6c84d0f66 | -5.02141 | -43.66406 | 2024-10-24 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6205cac-56c6-3446-80ac-04bb67c8d789 | -5.01835 | -43.65894 | 2024-10-24 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bca72c37-8eae-3d9a-a8a4-928561742b22 | -4.78418 | -43.64618 | 2024-10-24 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 012aecc1-f5ec-3630-8936-ffe7299b76ec | -4.42917 | -43.86847 | 2024-10-24 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77fc7ca1-0645-345e-b729-d12830c39dc5 | -4.35814 | -43.64392 | 2024-10-24 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cca27cd0-f6bd-369a-a8fd-cd17fa43726c | -4.81993 | -44.35415 | 2024-10-24 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19ac3be3-07ec-3e45-aa6e-066546012354 | -4.66862 | -44.61095 | 2024-10-24 04:32:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad88dfcf-42d1-3a16-812a-9eee3473dc7a | -4.66859 | -44.49131 | 2024-10-24 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a1350a8-add7-3535-8849-f03355be6372 | -4.66507 | -44.6104 | 2024-10-24 04:32:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2c7df1f-48ca-338d-add5-b1be896dacb9 | -4.66446 | -44.61442 | 2024-10-24 04:32:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c362bc46-3d42-3814-9a7e-3d75cb217dbe | -4.66153 | -44.60984 | 2024-10-24 04:32:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1166a36c-c97e-38a5-b27b-75e80e114d04 | -4.66092 | -44.61386 | 2024-10-24 04:32:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d838eca7-45f9-3e58-a72f-dd2dfa48b805 | -4.65738 | -44.6133 | 2024-10-24 04:32:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a15181eb-66ae-373e-a13d-6173f48e051a | -4.57005 | -44.00208 | 2024-10-24 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4313317f-02ee-38ea-8c80-c4fe5146838b | -4.56939 | -44.00636 | 2024-10-24 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e2a8752c-5b44-322d-a55d-9033ed3ce116 | -4.5664 | -44.00152 | 2024-10-24 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d0302f3a-a7ed-33e9-956e-cb10a44e45ef | -4.56574 | -44.0058 | 2024-10-24 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 80441cd1-d0ce-3041-83d7-9191f9efa0b6 | -4.56275 | -44.00096 | 2024-10-24 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb25b909-af91-3f78-9e3e-cd1850a10093 | -4.56209 | -44.00524 | 2024-10-24 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9ec8c7e-0493-31bb-a48a-38cd8072d76e | -5.51108 | -43.70248 | 2024-10-24 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcc1df1d-1e6c-362b-b13a-d23085bd1f17 | -4.22187 | -44.26611 | 2024-10-24 04:32:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3962145-50da-3400-83f1-50f8ce363915 | -4.22124 | -44.2702 | 2024-10-24 04:32:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e4aecba-32a6-3909-a12f-409d24d3db9c | -4.21829 | -44.26556 | 2024-10-24 04:32:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bc133fc-2ab8-3d75-90dc-133059e50410 | -4.21765 | -44.26966 | 2024-10-24 04:32:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf5dd683-9c31-32d0-8c9f-ebf3db592fd2 | -4.21407 | -44.26911 | 2024-10-24 04:32:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8bea240-639c-34c6-a3cd-4dd49589edce | -4.11029 | -44.23788 | 2024-10-24 04:32:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| caa668f0-c948-3d11-8b32-4bb2874d621c | -4.10543 | -44.2456 | 2024-10-24 04:32:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a8d7131-476b-3363-bba5-442cf2a63df3 | -3.90437 | -44.04366 | 2024-10-24 04:32:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d83a3cd9-edb6-33e3-9fe5-e65b460e913a | -5.26035 | -43.99562 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4e553871-d4e4-3896-b7ff-fb5063c9f83c | -5.25986 | -43.99348 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 18a689bb-7dd2-3fc1-b46d-f8f85f1f6cee | -5.25921 | -43.99786 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 35500978-be35-314b-8b33-244f58078549 | -5.25667 | -43.99503 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 64fad033-4441-3244-8bf0-3b569223ecc8 | -5.1318 | -43.75274 | 2024-10-24 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab9f1600-4b50-35ce-88f7-79131c103680 | -5.29995 | -44.74649 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44417052-27dc-3b29-a4bc-e01d30fdf967 | -5.21837 | -44.63983 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22bd28a6-d20a-3e0e-93c1-42d1f667ee19 | -5.16874 | -44.00382 | 2024-10-24 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 777fcc3e-e417-305f-b1f7-918f96580804 | -5.10633 | -44.80465 | 2024-10-24 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f14e7442-2d86-38a4-82bd-a7c028cd3027 | -5.91498 | -43.926 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f4f93248-3a44-3a75-a899-f2a3d2b93f12 | -5.89773 | -43.9642 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dd7d13e-7491-3f6c-90de-b8541813eeb3 | -5.71936 | -43.83536 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e339d0d-52ce-33ba-b1bf-599227930363 | -5.71721 | -43.83331 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac747f21-6bb5-3722-b0cf-6747b650589a | -5.71632 | -43.83028 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb9bf9d3-3004-34f3-8e99-6b1dec35f9c6 | -5.71563 | -43.83477 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aed10d21-148d-3e17-af8c-7e8c01627938 | -5.71413 | -43.82824 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 378a5423-4153-369d-8e78-c3ceef3ecbae | -5.71347 | -43.83273 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aff26f04-2498-392c-b27d-4490832fc82d | -5.71258 | -43.82971 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d341a70-5a33-3a6e-9861-e2efd4d17700 | -5.71106 | -43.82311 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b029177-38d8-3d1f-8b96-22753ac4d65e | -5.71039 | -43.82763 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d2015dc-cc6f-3612-9a0a-31dbdc03d007 | -5.70974 | -43.83213 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a449bbe0-e648-33e7-937c-0ff03dcb73db | -5.70954 | -43.82458 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7e1c89f-83c1-3c13-ab2b-11687a66f363 | -5.70885 | -43.82909 | 2024-10-24 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cef99b27-a250-3832-bb95-57752923a3d6 | -5.51039 | -43.70703 | 2024-10-24 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 989b0456-41a6-34f6-b0e3-513b78159cbe | -5.50802 | -43.69739 | 2024-10-24 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4a107de-ec48-38d9-8cb5-385ef0213fcc | -5.50733 | -43.70192 | 2024-10-24 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edac53da-f2f3-3b4f-8a37-de89d1eb1518 | -5.50663 | -43.70645 | 2024-10-24 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54b831d4-c413-38c5-8664-c227d65abff2 | -5.8103 | -44.48875 | 2024-10-24 04:32:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06717698-83d0-341c-b2df-73a6a1c435db | -5.80967 | -44.49288 | 2024-10-24 04:32:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73375264-18d3-34c3-a7e1-991d2b3b59f4 | -5.80904 | -44.126 | 2024-10-24 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aab03199-fa29-3d96-a612-3d9e22a54abd | -5.62344 | -44.83373 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7683d3fa-2e9b-3bb0-a6c2-0c815c2be2da | -5.62051 | -44.82914 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 087c8437-e566-3ecb-b984-379de385d63a | -5.6199 | -44.83316 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ea1452b2-ca82-3589-9250-1d340eafe0d2 | -5.61697 | -44.82861 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11e6cba3-71bc-3d5c-93df-64e3328d7e1f | -5.60907 | -44.88061 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 245abde9-faf9-33ec-9e7b-a72420fd6945 | -5.60554 | -44.88005 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a5cdb57b-ca37-36dc-b97e-ca2fa9171bbc | -5.60201 | -44.87953 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f8ff0c30-7b1e-3743-81f3-144965ffee75 | -5.58606 | -44.88938 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1e14a0dd-c71d-3e34-b633-41974155fbad | -5.58372 | -44.88095 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 560a1b74-a70b-3879-bfe1-0edc9f4ac254 | -5.58312 | -44.88491 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ed1bc65-78dd-3131-94a0-b41d67142f08 | -5.58252 | -44.88886 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c33410a-7e03-35b3-b229-dc2b46045f96 | -5.57958 | -44.88439 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a0573e13-0711-34a3-89bc-6118f1f8a8e7 | -5.57899 | -44.88834 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e67bc932-083b-3fe9-8ac5-c22e4623e5d5 | -5.57545 | -44.88781 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a065db46-9838-3068-ad50-0cd7a721646f | -5.44256 | -44.4239 | 2024-10-24 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87ce5345-a36a-3f6c-ba54-cf48b5f4e141 | -5.42679 | -44.79324 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33515304-4c30-3d4a-ba64-e08ea377e719 | -5.42617 | -44.79727 | 2024-10-24 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83541087-d999-3f95-9409-affb081880e3 | -1.85151 | -44.81755 | 2024-10-24 04:32:00 | NOAA-21 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07a3031d-7461-36b8-ae65-1947fc3ae4f8 | -3.10007 | -45.92379 | 2024-10-24 04:32:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 282c5a53-f761-3e1a-abb6-833c22fc821d | -3.09729 | -45.91975 | 2024-10-24 04:32:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0a4c9d6-7de1-3a00-bbdf-7be38b524d55 | -3.09394 | -45.91924 | 2024-10-24 04:32:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fc772ca-017a-3bbb-b4eb-fcdabe866625 | -3.08506 | -45.93229 | 2024-10-24 04:32:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6393afbe-f8f9-36fa-b21b-b9ce805c2c0a | -3.10697 | -45.22987 | 2024-10-24 04:32:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e7b988e-a136-382a-b1c0-6c05b236cc4a | -4.60671 | -45.63346 | 2024-10-24 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1304279-95ce-37c9-a22a-bca8d9589668 | -4.57949 | -45.60661 | 2024-10-24 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5cf93d4-3c30-3444-acd9-eda3093554dd | -4.57893 | -45.61028 | 2024-10-24 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README27.md)
