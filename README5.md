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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24541fd1-0966-387f-bf75-42abe6d2b3f2 | -23.98329 | -48.91869 | 2025-05-11 04:32:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07a096c6-1816-3ece-8bbe-bbf39dcd16d3 | -20.47774 | -53.67491 | 2025-05-11 04:32:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b62c959b-8ab2-3f72-947b-606962eb640e | -20.16341 | -46.83139 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2bb2793-d9d2-3411-b7fa-065e7f82f323 | -20.12059 | -46.88107 | 2025-05-11 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55ee4508-8931-3476-91ca-013100eca487 | -20.17706 | -46.81147 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7671c988-52cb-305b-9630-17fa5d8e68d7 | -20.15869 | -46.8392 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c5481cc-1a84-33d8-88c7-0390b46fdad3 | -20.19428 | -46.71521 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3165a840-6dd9-3956-8b9b-1be8ff7b3a78 | -20.15573 | -46.83458 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| deb44c42-7931-34f6-9bef-aa42b6883ea9 | -21.7197 | -55.37396 | 2025-05-11 04:32:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32c54460-17c8-307c-985d-1f77b396ee0f | -20.19011 | -46.719 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8912b90-651c-3982-8597-36dc06662abd | -20.1723 | -46.81957 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3454a13c-611e-33b5-a776-0f3f5965b820 | -20.76455 | -46.76988 | 2025-05-11 04:32:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8bcd328b-60c1-32fb-a223-67dc73684fdd | -20.19488 | -46.71098 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c73a2a07-51dc-3c07-831e-0bd8a69f55be | -20.16282 | -46.83551 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c1d5f92-d2cc-3c48-a759-443573cf60b0 | -20.17647 | -46.81566 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 953e575e-d8c4-39a3-aa1c-2908fdfbe6d0 | -20.17587 | -46.81988 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c5e6b7a-ac2b-3577-b962-6c037aab425b | -22.04835 | -52.58006 | 2025-05-11 04:32:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c560cdd2-7ffb-3697-b24f-d5b47b1e3aff | -20.375 | -48.08215 | 2025-05-11 04:32:00 | NPP-375D | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc0f614c-2fbf-3b85-8f68-ce3d4ec49df6 | -21.71899 | -55.37775 | 2025-05-11 04:32:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5dbbc232-4f15-3669-8566-da04a9be75f3 | -20.17349 | -46.81116 | 2025-05-11 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 410bd1c7-b927-3f10-86be-657f8cdf0978 | -2.3836 | -51.89472 | 2025-05-11 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35e07d7a-2c32-39da-aa87-b374b13bce98 | -2.38691 | -51.89523 | 2025-05-11 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99ff1a99-03d1-312e-a34f-aac4a7579195 | -2.38745 | -51.8918 | 2025-05-11 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f74403a-f3a6-3309-8b85-e4da873203ea | -8.9029 | -44.78214 | 2025-05-11 04:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fbe9cb83-b87e-3b66-aa46-e5bf3939eded | -11.11559 | -43.33896 | 2025-05-11 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c68b0a0a-45ee-3ee8-a8b7-34987f134a8b | -8.89784 | -44.78148 | 2025-05-11 04:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f541c3ac-ba43-35fe-93ef-31f0b4670486 | -11.11718 | -43.33873 | 2025-05-11 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5aa7bc0e-0d72-3aa9-9ebb-65926bb3a635 | 0.71386 | -51.37348 | 2025-05-11 04:49:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91daad93-eca0-3858-98a8-cb212acf4daa | -9.5704 | -49.10574 | 2025-05-11 04:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22e43ba5-14d1-3ed1-b0ae-09c4fe336e63 | -6.66413 | -51.86504 | 2025-05-11 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 847c9d28-f736-3c97-9934-dd3a04c7a4fc | -8.46744 | -49.61493 | 2025-05-11 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97185f3e-aea4-3c9e-b5d7-d6a437cd4fea | -12.3291 | -45.6971 | 2025-05-11 04:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 8d7d6547-2826-3c48-aa8a-9b353a5e34c9 | -12.72322 | -54.97381 | 2025-05-11 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b2169c6-6ea0-3d54-9b2c-ec7bc885ad9b | -17.04465 | -49.05927 | 2025-05-11 04:51:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f015fea-c8a4-3689-a959-87c82ca42093 | -12.76407 | -47.98697 | 2025-05-11 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fb7c3195-38aa-3a1f-a32b-a9335e60b608 | -14.65959 | -45.13669 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5958eec1-ca01-32bb-b5c0-5bdeebb1216e | -14.65999 | -45.13326 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9599136a-1198-3c55-a201-c9b5162db1b3 | -16.49853 | -43.13797 | 2025-05-11 04:51:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63fb986d-1547-3cb2-b32e-c7c049c7d42d | -12.584 | -48.33397 | 2025-05-11 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88357543-c38d-3d66-8e9a-692fefa1ec82 | -13.47983 | -52.96542 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4515c907-b753-30fe-be77-a19c2a8a9181 | -14.66574 | -45.13047 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63cafe16-9530-38bc-91a8-46c83147cb54 | -12.68972 | -58.14989 | 2025-05-11 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60aed1be-57db-319c-b41e-a4302df61c6e | -10.8251 | -56.9584 | 2025-05-11 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b269971-7726-30db-bbc6-0306eda913e5 | -13.37332 | -54.26412 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03294ef0-7ca3-3901-a401-06331f312fb4 | -13.62225 | -54.87725 | 2025-05-11 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62582802-b541-3e38-8100-b4625504bd2a | -14.27961 | -42.69295 | 2025-05-11 04:51:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4bf1496d-2cb3-3eb3-88ff-dfde57359cab | -13.48544 | -52.97377 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aabc1118-0738-3449-a45f-fafc5cb402c6 | -13.97848 | -56.81084 | 2025-05-11 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8ef5f9cc-b93a-3350-a6dd-1d550232478d | -15.56683 | -47.85606 | 2025-05-11 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ca656f0-7927-397d-8c6b-ab4c39e3775d | -12.10709 | -47.98335 | 2025-05-11 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b29af38c-fb24-31a2-b31b-7fcd8422d58e | -14.22018 | -54.55653 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4220da62-fdaa-3fde-bf6b-a542af64c7ba | -13.3772 | -54.26113 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5947fd7f-c58c-38c1-a3f6-d5e35f99bd49 | -14.22075 | -54.55299 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0333b469-acb4-37eb-b942-7fb11daed595 | -17.52916 | -52.11811 | 2025-05-11 04:51:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e0c33e0-9a12-3f4b-8ed9-9095dcc1525a | -14.31816 | -54.64602 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d6a662c-5b9a-399e-9385-5fc0fdfd717c | -13.0411 | -53.72072 | 2025-05-11 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e48cb9f-5224-3287-8285-7d71c90e04f7 | -13.60174 | -48.94511 | 2025-05-11 04:51:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4372b444-905e-3271-891a-7fec8b22837b | -12.64745 | -54.06628 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff31a451-f131-3fee-b635-a2e717613a5a | -11.61273 | -48.00615 | 2025-05-11 04:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a25fb9a-45e0-39c4-8c1e-508de539b942 | -14.66533 | -45.13391 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e089d5a-0200-3749-8f33-fac31b35fc12 | -13.04054 | -53.72426 | 2025-05-11 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eece420a-6019-39ab-9117-533a70dc5af2 | -13.48208 | -52.97324 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd3dfc91-732e-38e5-99ad-1e98f95e1702 | -13.486 | -52.97012 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a855d189-cdd7-36a8-b8ab-29c0cbae8817 | -11.14144 | -54.22527 | 2025-05-11 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e676c15-7fb9-3e9a-8e93-2aa036657b0f | -13.97915 | -56.80683 | 2025-05-11 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cb193e0a-6e19-30ed-99d1-02b1f95b3396 | -13.37664 | -54.26467 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7662619a-c4c1-32c0-a3eb-0b44ee10b47b | -13.09468 | -52.29388 | 2025-05-11 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaffc622-c8d0-3a43-83a9-7ad49e732e73 | -11.13756 | -54.22824 | 2025-05-11 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b4f37ce-f798-3b07-925c-771ece36aace | -13.04718 | -53.72533 | 2025-05-11 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e398d76-55ac-3dc7-a8a4-77c94fec8452 | -14.31759 | -54.64957 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0e483c7-0245-30f8-81a7-a95ffde67b3c | -12.11135 | -47.98389 | 2025-05-11 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d839e00-7236-3981-8e63-773c4399699d | -13.04773 | -53.72179 | 2025-05-11 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b766a53d-415e-3684-83ea-25768834d550 | -11.39246 | -48.70153 | 2025-05-11 04:51:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdb217fb-37f7-3380-ae49-86cff8252cbc | -13.47928 | -52.96906 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5f8a1b5d-54b7-36a4-b08e-035a43561143 | -13.61893 | -54.87669 | 2025-05-11 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00e25986-fba1-3694-9e4f-694346c7f527 | -11.39426 | -52.93904 | 2025-05-11 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29096ca3-000b-388e-9558-b129baf5ec8b | -14.27915 | -42.69722 | 2025-05-11 04:51:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a61e0978-7d14-387f-b7a6-834b44b54662 | -11.14088 | -54.22879 | 2025-05-11 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb507900-9d58-3c83-a3d8-aa2991b3cb69 | -12.59235 | -48.33524 | 2025-05-11 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e477a914-b8b5-33f2-99a8-1f4e4ec7e280 | -14.67109 | -45.13107 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e76ef82-801e-362b-a604-d164696e9d96 | -16.10776 | -47.54778 | 2025-05-11 04:51:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2bfab66-bcd0-39c0-afd0-c28594a352a6 | -13.04828 | -53.71826 | 2025-05-11 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e46f41b-1803-3035-b8e2-0b1f38ad496c | -14.65465 | -45.1326 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b39e23ff-0f06-3c43-9d8e-92bc372ca9cb | -14.65505 | -45.12917 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e10b09c-1bfe-38e6-8e9c-3ffa53a1b623 | -17.0983 | -47.93544 | 2025-05-11 04:51:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dabd798-04e6-3cc2-a164-73c59907d2dd | -14.21849 | -54.56719 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03342549-174c-3f7a-8c9b-ed7ebb2b96b7 | -14.21793 | -54.57074 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2c35e14-bf23-3233-92aa-31c9b7c4a25c | -13.04441 | -53.72126 | 2025-05-11 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dea17771-e7fb-34a7-999d-a4ead47aa6f6 | -13.47872 | -52.97271 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dc6021d3-ef80-33e8-bdd6-a08f272cf9ab | -16.67991 | -43.88258 | 2025-05-11 04:51:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d709a3c-e323-3529-a4e1-8e0f1bd3b1b4 | -14.21962 | -54.56009 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19f14f33-f02b-3680-8c88-c7f90eae6320 | -14.6505 | -45.12164 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bae97729-7801-3006-9618-3b39b3bb85a7 | -13.48488 | -52.97743 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f87ce3a1-79e9-3262-a723-ae81cd636adb | -12.37421 | -54.5248 | 2025-05-11 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10777de6-3680-3176-9764-ed8f942cb1b8 | -11.915 | -54.40198 | 2025-05-11 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f855b60a-b16f-369a-9e46-453d80c6da41 | -12.11075 | -47.98246 | 2025-05-11 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bbcfe1b-bf88-32b1-bef7-119c57383111 | -14.6493 | -45.13193 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daaa17fb-cbdb-38f3-b630-7cc2cc8219db | -12.11019 | -47.98669 | 2025-05-11 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df2a6af8-d981-319f-999f-4cae0dca8c7b | -14.21906 | -54.56364 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbd537b7-e005-32de-b147-2368fbdfdbb7 | -14.64891 | -45.13535 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
