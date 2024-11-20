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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01386b1c-96e4-37bf-b0a2-76a1cc6473ca | -5.54415 | -43.89741 | 2024-11-20 04:27:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19329a29-406c-3503-a0ca-6ed3c755ed42 | -2.25468 | -53.6755 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac453c6b-a27a-30a0-b0e9-08f3169c1c53 | -2.92297 | -53.06986 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| eecb03c1-7e6e-35c3-8932-045dc02af74b | -3.44977 | -47.57153 | 2024-11-20 04:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd2af34a-b09f-3270-bb1e-b3af05f2441d | -5.15525 | -44.12403 | 2024-11-20 04:27:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f6b39b2-b634-308e-885c-1682f8497428 | -5.87601 | -39.62808 | 2024-11-20 04:27:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b025717e-de2e-34f9-98ef-c148bbe922f5 | -2.62149 | -51.81129 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a48b9cc7-7b2a-3db4-a1bb-119a5fbe92f9 | -4.13045 | -48.13149 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d2d5542-e40e-3b13-96db-6d6a60242e34 | -4.56161 | -45.6413 | 2024-11-20 04:27:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9cefed4-29d9-3a47-ac8d-960bba1fd4de | -5.63258 | -47.93833 | 2024-11-20 04:27:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45b56182-9158-3c61-a5ea-aa778943cb7a | -7.17959 | -48.7614 | 2024-11-20 04:27:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df01c050-2a95-37df-9215-2807ef4909cf | -3.87763 | -43.02093 | 2024-11-20 04:27:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 308254ab-1b61-3cab-b165-07a58333303c | -3.09101 | -54.67021 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b90ce321-d7bf-3f43-9821-d64b498c7255 | -3.70977 | -51.84194 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f36e30ca-eb16-34a3-a441-f2aa8864479c | -5.15468 | -44.1278 | 2024-11-20 04:27:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b07d77db-99d0-3830-8e07-1709e63518b1 | -4.43058 | -48.29801 | 2024-11-20 04:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 086885d5-17f7-3d9d-b7aa-412473212076 | -2.79531 | -51.79078 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60c11571-daaa-3b44-bb37-81634c089467 | -4.53061 | -38.57256 | 2024-11-20 04:27:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 387636c7-4eef-3b39-94e5-7b6b566a4e61 | -5.97741 | -45.36894 | 2024-11-20 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2046ecbb-d800-39a2-b4ea-6fb27091c7e4 | -6.59534 | -46.49472 | 2024-11-20 04:27:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0abc8645-eb2a-3fd7-abc1-e6d88bf84c9e | -6.01105 | -38.65855 | 2024-11-20 04:27:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 71be2f8d-9524-38ce-936b-dfb97c8fe262 | -4.15394 | -43.97536 | 2024-11-20 04:27:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 43274a19-4e62-33ef-9606-61882ae1ffb1 | -3.76538 | -52.1362 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0808adaf-2e9e-3bf6-8ba7-c768c0300c09 | -3.31799 | -54.09064 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09f0c1e3-ad09-38d5-af4e-a6ad12a77df1 | -3.88459 | -46.665 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f40b129-3e9c-3d94-83d4-a600ae9399dc | -10.92788 | -44.87933 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1da2735f-0d75-303a-bbe6-64b33c5904a9 | -3.08119 | -54.66442 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5053ed8b-2ffd-3fb3-b1bc-01ca9a1795f6 | -4.11228 | -46.57983 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4dfe1aa-fc21-39da-be7e-077b5b5b9a18 | -10.44613 | -44.88675 | 2024-11-20 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9316cf88-8063-354f-9f76-a631b08a1982 | -3.96043 | -46.72313 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbf6880a-5620-3eb0-8a34-8698444e3582 | -5.46586 | -43.94447 | 2024-11-20 04:27:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42016395-b8ff-31b2-9570-a5cb648baf20 | -4.12066 | -46.8516 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ceeacb00-a0f3-37ca-b6b1-1fa961b7421e | -5.16416 | -49.65557 | 2024-11-20 04:27:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4d76947-7e6c-34b4-acd6-0e30963fe004 | -2.92093 | -53.07228 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 534f5707-330a-32c8-b32d-19b34560281f | -3.31051 | -54.74426 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcc24d64-6f39-3f8a-8e83-9d1c79b9467f | -2.9272 | -53.0633 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c23aafb5-5b66-3e67-b4a1-97771883324a | -9.36881 | -43.28684 | 2024-11-20 04:27:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a15eb63-47dd-3157-b626-676594478d1c | -2.91663 | -53.07878 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc64e0ee-dfa3-3959-9762-955e38841389 | -2.95447 | -48.32598 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2b89b02-23dd-353f-b158-dd6f1101910e | -5.25605 | -43.83589 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f746b810-16cb-388a-9ed7-fdde5cf813d8 | -6.93677 | -41.19538 | 2024-11-20 04:27:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 3f25bdea-1383-394d-a6d1-bbc95bf24df2 | -3.14101 | -49.12814 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1d5e46e4-97e2-3848-b9c1-40f68e2b2770 | -4.38556 | -47.76139 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d77c57a-a44c-3d7f-b9ad-1111e60651c9 | -5.59411 | -46.17442 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fb59431-94d9-3631-8294-8fd836dff715 | -4.90348 | -44.00649 | 2024-11-20 04:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45ebc189-0311-33b1-82f8-9f88a5e8da4d | -3.11082 | -53.75268 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72cf656d-106a-33e6-b63c-570cf9ff887a | -2.28169 | -53.63392 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 622bc491-d3fb-3096-a1b8-ccb55cdfbc7d | -4.84057 | -43.4768 | 2024-11-20 04:27:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fc37dac-3551-39c9-b35f-f66b66947767 | -2.92684 | -53.07567 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 9962f0fc-1dc8-3faa-a3cc-ae6718f5deea | -5.59765 | -46.54201 | 2024-11-20 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ea3d23e-68b3-3106-9b8b-7c972f4cf2e9 | -3.05355 | -54.4108 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 780f0f63-79d4-3b60-9170-4ee125c477d3 | -3.75719 | -51.34443 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f12d6bc8-6a8b-3cab-af34-41d4735ac0ed | -2.93112 | -53.0691 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e797f628-bcb6-3ec5-9673-12a7ba7bbe61 | -2.20089 | -53.6613 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7daa4cf-d542-3313-99fc-8bb5e28ad505 | -9.17202 | -44.72011 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a54b276-960a-3abd-9572-9f7b42ad1019 | -3.36864 | -54.09643 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd0157cf-161d-3bd2-a410-9e57facddd08 | -7.56993 | -46.45725 | 2024-11-20 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fec15948-d5ca-3b81-b0f5-3435bd6eac9f | -9.49835 | -43.19068 | 2024-11-20 04:27:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 95ca5d31-ecdd-320c-8893-f90edfc51fb0 | -4.46504 | -46.58569 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ad10a64-69ab-3993-99d8-c7cf16a1ca46 | -2.90446 | -53.05435 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42ac23d2-894c-3779-98cf-aff464f85aaf | -3.81049 | -43.24876 | 2024-11-20 04:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ac80ff8-51e5-3f7a-a40d-a22e2842236d | -2.74339 | -51.7279 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 329afc59-659b-38f2-b575-87fe5a23772d | -3.87081 | -47.07888 | 2024-11-20 04:27:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c0fcb22-3667-3939-baf9-78675526ab3f | -5.97013 | -45.34975 | 2024-11-20 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c6a1dfa-ae6e-36c2-80ef-c354a2993b2d | -9.259 | -45.00779 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 316f2b21-2622-3d9c-8f12-610afac08616 | -4.99414 | -46.92163 | 2024-11-20 04:27:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7055a7f8-fd67-386b-b4f8-b709a36361c5 | -9.17145 | -44.72399 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3abc1d4-ecf2-3b3d-a5dc-8a64115219d7 | -6.18688 | -47.08219 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f16adfe8-096d-32fc-9ff0-60bb87289b0e | -3.61127 | -54.75057 | 2024-11-20 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80731eb1-2879-3fee-a00e-642f25eb459d | -3.11398 | -53.70219 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b9379bc-a2a0-3c75-8aef-aca6655938e7 | -2.92014 | -53.07724 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1017288f-9480-39af-84e3-fe3b4e53e846 | -5.38145 | -50.47256 | 2024-11-20 04:27:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 673999bb-2714-3b19-9a64-d58c5c6204cf | -4.55691 | -48.00968 | 2024-11-20 04:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d6bf121-b235-33bf-899c-12913494998d | -2.89519 | -52.43758 | 2024-11-20 04:27:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0787500-fb8c-3e50-98f0-89d08f32ad02 | -2.34324 | -54.79048 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74941840-0f3c-34db-94f0-060cbb9ad847 | -4.13737 | -47.73384 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4349c7dc-22b8-3799-b415-4f35ef57cedc | -2.7403 | -51.82898 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f422ccdc-1463-3ea5-9039-59ce3370d32e | -10.88026 | -44.41479 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ade20e83-3e13-3216-b7b7-e1adc082dece | -5.57332 | -46.35117 | 2024-11-20 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdb37c57-9442-3f11-b5a2-03715e8b2f6c | -3.77032 | -51.68428 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d858965-97d4-3d0b-9459-025353ceccfa | -5.94858 | -48.07009 | 2024-11-20 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a79ae2bf-dd7d-31cd-aca8-25fe44e5b093 | -2.2808 | -53.63953 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 09aa7b22-6034-379b-8427-bef45ffb50fb | -4.99082 | -46.92112 | 2024-11-20 04:27:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fabb367-ba70-314e-9202-938e338348ae | -3.72629 | -44.42741 | 2024-11-20 04:27:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fca13ea1-40fe-3cea-b306-4f45a0515f3c | -2.74396 | -51.83385 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f09c01d4-7bd9-3fbe-abcb-752bca870e0a | -3.79611 | -46.9477 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06545a44-349f-375d-a420-612ac585e9f0 | -3.54289 | -54.57505 | 2024-11-20 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 352f86c0-1eb7-3fda-ae62-bcd7636626e5 | -2.68496 | -51.80421 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14c3618f-4e76-3e47-b749-a7b6e92328e2 | -4.74352 | -45.41088 | 2024-11-20 04:27:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a0a330f-ecc8-359c-87ae-6dd3a8c883dc | -9.19232 | -44.72725 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c38b9df3-7d0f-35bf-9be8-cd2d23fe9344 | -3.85265 | -49.43693 | 2024-11-20 04:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8649b44-e35d-3901-a7f2-36b6fa43c157 | -3.13667 | -49.13184 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d73c48d0-98a1-323e-97ba-2b566acc0828 | -11.18886 | -40.89144 | 2024-11-20 04:27:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff88be67-4b3a-34df-971c-9b8704260262 | -2.78418 | -51.72169 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 43a19464-4225-36b5-8407-377186406437 | -5.94519 | -48.06955 | 2024-11-20 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1406244-8a32-37c5-9515-1fb85a2280ae | -3.7319 | -47.37079 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c776d98-a84b-324d-aa7d-d58c1838532f | -6.99951 | -39.27228 | 2024-11-20 04:27:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ab81cf4-8c50-3ee0-a807-e9b366763db7 | -2.74097 | -51.82479 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2d2cd7bc-71c5-398d-94e6-55e24bbe0c69 | -6.5277 | -47.272 | 2024-11-20 04:27:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed0eee70-699d-3b4c-95d5-2c305a6fc9d7 | -3.95043 | -46.70023 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README36.md)
