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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0218479-70e3-31a2-aa0b-c2f31abbab6a | -6.9868 | -47.5104 | 2026-09-22 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6ef3c2db-3eea-3677-a7fb-fe5d8ccdd8dd | -8.7919 | -44.2546 | 2026-09-22 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 65e403e4-2437-3b96-b783-694801859896 | -6.3135 | -57.7342 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f272bd45-eada-3b6e-917e-9e8c8f79e8d0 | -2.8791 | -57.8184 | 2026-09-22 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5e49732d-6490-3fa1-a357-bedabb666102 | -6.4302 | -59.9724 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 259a1198-3912-34bf-b8ab-4ac32ae2b9a9 | -2.8534 | -60.9206 | 2026-09-22 14:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 475daba6-ee05-3cac-b22d-c4833f24a157 | -6.3842 | -55.265 | 2026-09-22 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a827b485-c3d5-3ff3-b6b3-412d58e8b678 | -9.0286 | -44.9187 | 2026-09-22 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 7bff85c5-2f8d-32a5-989a-dd2d933410f8 | -7.1203 | -43.7323 | 2026-09-22 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 2b6bd25a-b033-3696-a8f4-2028414a6d60 | -11.4404 | -47.3355 | 2026-09-22 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 17dda573-5457-3bd1-a677-dca7a10aeecf | -13.2983 | -51.7713 | 2026-09-22 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 91d96292-fedc-3089-9743-7c91da58aaa8 | -6.3014 | -59.9579 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 87b6a243-2118-3164-bfad-7680526304c3 | -7.1273 | -48.4366 | 2026-09-22 14:30:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 967ea643-137d-3e40-bbf4-2d8e9340abc0 | -12.9081 | -51.0314 | 2026-09-22 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| e94ccda4-3d2f-351c-a343-19de60d0ae30 | -12.9276 | -51.0076 | 2026-09-22 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1efea22c-b540-3661-911d-4eb54d2872b0 | -3.2817 | -57.8685 | 2026-09-22 14:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 8f16cf74-e129-324a-bfda-f90ca67c2b23 | -12.9084 | -51.01 | 2026-09-22 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 4cbfc19f-e5fa-38c6-847a-e6f01e47a172 | -10.7262 | -50.7044 | 2026-09-22 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| bddd9140-d35d-3b61-bb7b-361811dc6717 | -8.2384 | -55.3017 | 2026-09-22 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fe098164-5206-3e79-a250-23700d6f57c6 | -6.9681 | -47.5119 | 2026-09-22 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 90b9ad5e-5114-3683-88cc-37792205cb11 | -12.853 | -50.8885 | 2026-09-22 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 8447589c-3ab8-3c2b-9088-76de13843595 | -3.6032 | -60.5853 | 2026-09-22 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d053c34c-dc31-3a65-9d9b-1be740e4fc11 | -9.5833 | -45.8345 | 2026-09-22 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| add0c813-6bb7-38e4-b6b8-2618cee78829 | -2.9525 | -57.72 | 2026-09-22 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 59ac81b1-4172-3003-9a74-513e09f36dc0 | -12.283 | -50.7011 | 2026-09-22 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 46743169-04f5-3b92-a421-81b9e8bcd8ac | -10.7466 | -50.5959 | 2026-09-22 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 119cd42a-4d50-36ea-be60-aebe20d4ad29 | -3.1901 | -57.8704 | 2026-09-22 14:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 947532ac-e9a7-309b-9f8a-bdd5b13ac257 | -3.3867 | -59.5415 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| bbc72048-7008-3df3-a069-0bdd6d5be694 | -13.4335 | -46.326 | 2026-09-22 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 158.7 |
| b659f469-d4d4-3878-82be-ef54f34e51b1 | -11.8559 | -49.979 | 2026-09-22 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 45a1b36a-b526-3f52-a3c6-88e22cc227da | -3.4781 | -59.5396 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 9cae6d3e-632a-3f27-80a3-5f83e4649c7b | -2.9997 | -60.8047 | 2026-09-22 14:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 0069babe-a12a-3ee4-84e3-943b4c5eb5ad | -12.0839 | -50.0162 | 2026-09-22 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 248.9 |
| ceffdb7b-ff76-353d-aae6-56d5169f149e | -3.3311 | -59.8101 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 51d8805f-dbfa-3061-ac54-cd717ebaa947 | -9.5353 | -47.9569 | 2026-09-22 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e09078e4-a1df-3c9a-ac5d-151fd151ecd1 | -12.6799 | -50.9526 | 2026-09-22 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| acfe4950-b37e-3199-a23a-3578c142fb95 | -12.9269 | -51.0505 | 2026-09-22 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| b804630e-0d9b-3fd8-ad90-c8e84e71d2c2 | -11.7079 | -50.9811 | 2026-09-22 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| c1ca4255-2e95-316f-888f-c3b527197364 | -10.4672 | -50.2838 | 2026-09-22 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 3ec5a66e-ffd2-39f9-a420-cd1e0e7cc4e5 | -7.1555 | -47.4751 | 2026-09-22 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e502921d-73f5-358a-8d58-3ca9419f6851 | -3.3867 | -59.5223 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |
| f68e61b3-440e-3aeb-ae2e-bf200f2a2553 | -12.3824 | -47.0057 | 2026-09-22 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 436ad033-42c8-33ae-ab25-3d8e27598c97 | -10.4539 | -51.3038 | 2026-09-22 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7a20a4b6-8dcd-3b1c-902a-d8f1374ccb1b | -3.1851 | -59.6982 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0c42b4c3-403b-3b46-a395-6d18584bfb26 | -6.0926 | -57.6652 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1c02befa-3373-3fd0-9c96-773832559eb5 | -6.8216 | -59.1686 | 2026-09-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1a6d8684-de7e-3403-afd4-55430e18ed94 | -11.378 | -44.2429 | 2026-09-22 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 57985b86-c5aa-33ee-8ce3-f97178870220 | -3.1901 | -57.8898 | 2026-09-22 14:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ad975d0d-1449-3952-8c69-3ad9c1aca69e | -9.5698 | -45.4501 | 2026-09-22 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 94ad3f8a-5ae3-3f0b-83bc-4db8f856cae7 | -3.2183 | -61.0472 | 2026-09-22 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| bf387a7d-db19-35d5-aeba-afd203bc4e36 | -12.8906 | -50.9267 | 2026-09-22 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| e5c93b39-5eeb-3802-87ef-6ec2631ab8c4 | -3.6398 | -60.5846 | 2026-09-22 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 72a0f1cf-0c61-387d-a366-cb434b2fc98d | -11.3255 | -54.0487 | 2026-09-22 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 095c6575-5e1c-32db-b217-0123bf2f34ba | -7.0352 | -44.6396 | 2026-09-22 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 3f8c67c9-a895-3cb6-96cb-89a5dd94ec7d | -3.2818 | -57.8491 | 2026-09-22 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 316f3179-129b-3304-aa32-10042e648d4e | -6.2396 | -41.6634 | 2026-09-22 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 145.8 |
| 3759ea3a-2028-3633-a195-c5b17a75596a | -8.8149 | -45.3534 | 2026-09-22 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| d10de618-385a-37dc-a7ae-660e4a56b57a | -3.331 | -59.8292 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 9f6299e5-e3f3-3757-8045-2ad5f7fb89f1 | -2.5687 | -57.5135 | 2026-09-22 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e9f21650-86e0-3c0f-b44f-4adf70aa0c1a | -6.2587 | -41.6377 | 2026-09-22 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| a177fb6b-8737-3a0c-940d-7cef7bae0718 | -8.8146 | -45.3762 | 2026-09-22 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 99edb40c-5810-3839-9e13-d0f38cb40af8 | -3.2016 | -60.4219 | 2026-09-22 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 3c2ab441-6347-3dee-9842-ea58064aa3c1 | -9.6961 | -45.8893 | 2026-09-22 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| de0568fa-3acf-326f-886d-c9526ccb0ec7 | -10.7437 | -50.8089 | 2026-09-22 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 5c868e77-3715-33e0-b99e-efe8a680a098 | -11.3229 | -51.3626 | 2026-09-22 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 7966d4ce-4d60-39b9-9302-58d3e3ca7eb0 | -5.9334 | -59.9707 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 178.6 |
| c91b8e2e-f77c-366e-b20e-ab8673c1dca3 | -6.0924 | -57.7043 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d64351af-fee3-335a-940c-a9f123ab904c | -6.815 | -47.8953 | 2026-09-22 14:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7b07c3ef-dd6e-36d3-bd81-beded1ce568d | -3.4049 | -59.5794 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c5998ea4-6e1f-3101-aeb6-18b703704c94 | -4.6589 | -42.0726 | 2026-09-22 14:30:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 137.7 |
| 60cc1888-c405-307d-8103-2a32e10aede4 | -11.3416 | -51.3817 | 2026-09-22 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| eef418b5-2a17-3d7b-a5a9-5887d1178f2e | -3.3492 | -59.867 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9b953a40-1b40-3ce4-915a-2547a7056784 | -11.269 | -54.0334 | 2026-09-22 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 4b1ec65d-7b66-3b66-beaf-a2328050a6a6 | -10.8909 | -54.0882 | 2026-09-22 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 1a08a020-b052-33e8-89cc-9ec1898c0dec | -6.4301 | -59.9916 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| dc66967f-f95e-3522-ad77-f7ef076d68ac | -3.3001 | -57.8487 | 2026-09-22 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| d70f855e-a3de-3184-ac44-ded22adc60ed | -8.7912 | -44.301 | 2026-09-22 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ced19b7b-3552-3eea-8908-1ef2b856e4bc | -9.6302 | -43.9219 | 2026-09-22 14:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 31235006-b33d-3571-8771-1ee4b7a55962 | -9.2759 | -46.1852 | 2026-09-22 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| eb29e066-48f2-30a4-b107-202d588c1f10 | -3.2395 | -53.9618 | 2026-09-22 14:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 199.6 |
| 30083f6e-270a-30d0-aef2-c11bc3af8ea5 | -12.2827 | -50.7226 | 2026-09-22 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| ab99f035-2134-3feb-8abf-80c7b017aa11 | -5.5717 | -42.7414 | 2026-09-22 14:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| ef16ab9e-57ae-359b-8129-7704cb736b90 | -3.4272 | -58.1945 | 2026-09-22 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 82c402dc-2fc2-31c7-a972-74f0e855acc7 | -7.0661 | -45.2521 | 2026-09-22 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e6df22ac-5856-3956-a2d4-0e1e8b40a6e2 | -8.4611 | -57.6292 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3cd84597-d967-3656-a760-ba6164be34a5 | -7.0046 | -45.7544 | 2026-09-22 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 54ac968c-cf61-34b2-ada7-4fb1f445d2ee | -7.146 | -48.4352 | 2026-09-22 14:30:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 313852e1-dc94-39bb-8d4f-26eea9801eca | -3.405 | -59.522 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 183.3 |
| 42509d6e-389c-35a7-a9e1-700185453968 | -10.0295 | -52.0991 | 2026-09-22 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 625daf34-7980-33e4-9f59-c0cd756315ee | -8.1874 | -54.742 | 2026-09-22 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9214446f-a4f5-3e84-8c04-f6e388ea3998 | -6.7464 | -59.4223 | 2026-09-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| e5dd2fdf-7565-3809-90a1-94fdbc4d527a | -6.0365 | -57.8235 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 49f4085c-89cc-3ea1-a7dd-f64163f99268 | -6.4486 | -59.9717 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 8268463c-b77e-3d3c-bcb6-fbc00f8d90f2 | -6.9174 | -41.6957 | 2026-09-22 14:30:00 | GOES-19 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 137.8 |
| 0b39d5ca-c527-3993-ae49-ba100573bce4 | -8.4983 | -57.6271 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 81ce5f03-2d31-3ffd-b21d-fac8e435eaa6 | -11.3976 | -44.2167 | 2026-09-22 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 189ec382-b392-3500-9161-dcebec2ef464 | -9.6111 | -43.9243 | 2026-09-22 14:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 355.4 |
| 4b0895ae-fdfb-3f48-b81a-9d2b22cd973f | -6.9948 | -52.8658 | 2026-09-22 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 6c567053-d4af-3d97-acc2-0f2e5ba5f9c7 | -3.7673 | -60.7339 | 2026-09-22 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 35e44ceb-3f85-3de0-8b67-b47ffaad1a7d | -11.3232 | -51.3414 | 2026-09-22 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |


[Clique aqui para ver as próximas entradas](README139.md)
