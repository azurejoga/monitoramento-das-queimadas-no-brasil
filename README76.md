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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cefe6108-3f41-32c7-863a-78569dd4cb0d | -4.99621 | -42.72815 | 2026-10-05 15:56:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7a77264a-0bcd-329e-8eca-1dc1dec97985 | -4.96183 | -40.55972 | 2026-10-05 15:56:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3638d638-bba3-3b25-a0d4-12f422aba80a | -5.12377 | -42.76634 | 2026-10-05 15:56:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d80c991d-9c97-309d-9353-23a4d59836ef | -4.69647 | -44.20234 | 2026-10-05 15:56:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3a2e495-7ab6-38b7-8e4e-80f0e1630773 | -2.05531 | -48.22764 | 2026-10-05 15:56:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| f9517a61-846c-34a2-be6a-d3bb916360dd | -4.80729 | -42.1428 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| c19d5a47-e009-3606-8312-17a09f0bbeee | -5.3723 | -38.27335 | 2026-10-05 15:56:00 | NOAA-20 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1b3a5263-ee2e-3ca8-9c4c-6e8e12392e04 | -5.12478 | -42.76914 | 2026-10-05 15:56:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fd778d0b-47e2-303e-9a84-3cd5ec3624b2 | -3.6679 | -39.71709 | 2026-10-05 15:56:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 18d0a101-1e7f-3240-b23e-7771b58afd41 | -3.1374 | -42.66558 | 2026-10-05 15:56:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8ddc6f06-11f0-3766-aa28-d99fbaf4cec9 | -4.80339 | -42.14817 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 210.9 |
| 9be9d13e-ad2a-3bd9-94b7-9d99dbb5e472 | -3.97312 | -38.51099 | 2026-10-05 15:56:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 282853e4-53bf-3a60-84c5-169563c1b510 | -3.11742 | -44.29039 | 2026-10-05 15:56:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9dae9310-20f5-3fa0-bd79-40c1de969fd0 | -5.774 | -44.42024 | 2026-10-05 15:56:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d48fc03c-d621-36fc-8796-499b16ae6043 | -5.11578 | -42.6393 | 2026-10-05 15:56:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 783774ca-1597-33f8-b70a-5132682b6a2c | -3.32727 | -44.58455 | 2026-10-05 15:56:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 0a038c50-9677-3ebf-9c1a-e949a2ed43d6 | -6.18379 | -43.38025 | 2026-10-05 15:56:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 68ab6b21-fc07-3b7e-949e-2c52053598af | -3.31778 | -43.943 | 2026-10-05 15:56:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3ed4f20d-7378-3cd3-9da1-c14726e55ac7 | -3.91662 | -44.14743 | 2026-10-05 15:56:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 289fd7b3-0a8b-3d83-9d9c-3109c5c3adf6 | -3.57013 | -43.89149 | 2026-10-05 15:56:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d274e4cc-b7c4-349b-8ab1-f3d220ce8694 | -3.8465 | -40.49174 | 2026-10-05 15:56:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2f2cee61-fe32-32a9-9b3d-2312a4f921db | -3.30762 | -43.94452 | 2026-10-05 15:56:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c9a67403-035c-30ba-bb31-c27bf42b07dd | -5.44284 | -42.63929 | 2026-10-05 15:56:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 9d9df46e-6385-3f57-ba74-f010163a3954 | -3.77189 | -39.84795 | 2026-10-05 15:56:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 0e6f32fa-62f4-3047-9bb0-0d85397a6611 | -3.57056 | -43.89449 | 2026-10-05 15:56:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eed46f91-4281-36b0-a6c0-5f19455d18a8 | -2.05794 | -48.20949 | 2026-10-05 15:56:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 485d29df-9991-3019-b930-5548a1827e83 | -4.84314 | -41.81092 | 2026-10-05 15:56:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 0802ddd8-70a3-3d70-9141-3bc04fee88b5 | -4.62254 | -38.93577 | 2026-10-05 15:56:00 | NOAA-20 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8171fe57-6de4-32bd-a0b6-fe995da51d41 | -3.44187 | -39.29011 | 2026-10-05 15:56:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 58c662e6-d773-36d3-9882-99d4279c0efd | -3.53707 | -39.88391 | 2026-10-05 15:56:00 | NOAA-20 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 57.3 |
| c86f876a-7cf0-31a1-9d0d-c0642c82d912 | -4.2181 | -41.68757 | 2026-10-05 15:56:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 4fad3e53-5cfa-3026-a701-d9431f221b2c | -4.89483 | -43.4656 | 2026-10-05 15:56:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2ad0bbfd-b76c-3c3e-abcd-12d61f680b46 | -4.9083 | -41.73906 | 2026-10-05 15:56:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 3ce42150-162f-3e8f-bb53-57957514b035 | -4.91277 | -41.73845 | 2026-10-05 15:56:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 56a7159b-8b44-30f2-af92-0cd6ec65efcd | -3.41215 | -42.65878 | 2026-10-05 15:56:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f4a90e4-b59a-3f8d-aa0c-cd0459b40f37 | -5.35042 | -45.16569 | 2026-10-05 15:56:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 077d4418-613e-3e8a-9534-59a47974058b | -3.27312 | -44.66021 | 2026-10-05 15:56:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f02cd058-79ae-3c53-bc3e-5ef7460e656a | -2.92134 | -42.37556 | 2026-10-05 15:56:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 13b59ae9-e98e-3050-a2f4-0122a82e2ee6 | -3.94049 | -40.73233 | 2026-10-05 15:56:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 654b3ab1-c1b0-3cf6-9488-1517d7c110ab | -3.36458 | -43.38179 | 2026-10-05 15:56:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 40832ae9-dcd8-3c0d-af63-1ba6964ebefd | -5.87614 | -42.42156 | 2026-10-05 15:56:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1f03f4ae-0dca-39fb-98ef-f81a99170780 | -3.01653 | -44.73214 | 2026-10-05 15:56:00 | NOAA-20 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 804ccc96-681c-3ec1-93f9-0bbc8db55a29 | -3.73815 | -39.54214 | 2026-10-05 15:56:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| e80763eb-521a-31a2-affe-3b77229b4dd9 | -4.85241 | -40.40676 | 2026-10-05 15:56:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 078df24c-d932-3a53-bfb3-f8151203de8f | -5.9434 | -41.34953 | 2026-10-05 15:56:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| def25901-e39e-3225-9a70-8f4d652a1de8 | -3.61918 | -40.44328 | 2026-10-05 15:56:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f488fdb7-cb1a-3b9b-a868-fbb619a4605d | -6.32858 | -43.81303 | 2026-10-05 15:56:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 12456265-fbff-3c30-a51b-36ca8b2692eb | -4.36309 | -43.93121 | 2026-10-05 15:56:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| f3ff38a0-6e86-3da0-9d6b-ed786ad527e8 | -3.33889 | -44.58962 | 2026-10-05 15:56:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 3c216d1c-c145-33a6-a012-93804b647fb0 | -5.84483 | -45.01094 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a0f43d35-ee08-3db6-8ab6-01c70c2924a1 | -5.12271 | -43.99584 | 2026-10-05 15:56:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e4669491-1604-3d83-9331-ba0463c8cec4 | -5.71246 | -40.12159 | 2026-10-05 15:56:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 2709befd-eff7-3167-bbed-d8718da8ca72 | -3.74506 | -39.53642 | 2026-10-05 15:56:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| deb32b83-6d10-35cf-90d0-c090b3bafe90 | -5.9516 | -41.34381 | 2026-10-05 15:56:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 9e07bb1b-4839-3208-8f8a-3b24424a6b67 | -3.33121 | -44.58489 | 2026-10-05 15:56:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9eb2d28a-006d-3fe2-b368-94f6f5fda522 | -3.30297 | -43.94821 | 2026-10-05 15:56:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cd4416c3-1e89-3bf8-b378-eae2a08b973e | -4.3678 | -43.92732 | 2026-10-05 15:56:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| c99572d6-8e16-3010-8589-346ef93df392 | -4.89377 | -43.46405 | 2026-10-05 15:56:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3c879ee3-e6d1-3b59-8b5f-35db0dfa0408 | -3.49435 | -43.34632 | 2026-10-05 15:56:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b0717195-4c65-3d8f-837e-e13e706787cf | -4.57099 | -39.58438 | 2026-10-05 15:56:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 9a95a840-4f7d-38e9-b8a9-343c44d251fb | -3.74265 | -39.54626 | 2026-10-05 15:56:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 16bc7a5b-c1f4-3645-b157-0d16cd27e012 | -5.30298 | -43.21434 | 2026-10-05 15:56:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9cfc2c6-0233-313c-823a-3fec4bceb15e | -4.36396 | -43.93732 | 2026-10-05 15:56:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 0dddc1e7-1dbd-389e-a4fd-f866fe03cbb8 | -4.36824 | -43.93036 | 2026-10-05 15:56:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 5c14bd60-4f56-3591-a487-7e2089505b6d | -5.41056 | -40.35839 | 2026-10-05 15:56:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 118910f0-13a6-3c74-93fc-c0c50cc0b4bf | -3.17243 | -41.40258 | 2026-10-05 15:56:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 5923958d-76e4-3072-b361-3286536370b6 | -3.93582 | -40.72923 | 2026-10-05 15:56:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 134ee841-fd99-3214-a2a3-0400213f5ba6 | -5.95602 | -41.34312 | 2026-10-05 15:56:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 34219dbe-a116-397a-8e54-8fde0d21bfe7 | -4.802 | -42.13875 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 3930fa83-08b7-3743-9b03-e6d11162789e | -4.44296 | -43.41949 | 2026-10-05 15:56:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c805acba-fbfe-323c-8db8-17069a03e4e9 | -6.32375 | -43.81688 | 2026-10-05 15:56:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c995730b-23d2-3aef-b723-a648ce56087a | -3.30253 | -43.94523 | 2026-10-05 15:56:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e6e28cb5-5cf2-3353-92ed-63b69bdc541f | -4.79536 | -43.23617 | 2026-10-05 15:56:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3cf7995b-bb25-3604-bc41-7e08a6f7918b | -5.35354 | -38.24618 | 2026-10-05 15:56:00 | NOAA-20 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 2e337eb8-0f09-3bec-8ba6-abd516020e3d | -4.38012 | -42.99238 | 2026-10-05 15:56:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 06fef173-2d1b-36f6-9b13-7b0e1005800e | -4.49218 | -39.35909 | 2026-10-05 15:56:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a7b34190-2206-307b-b811-099b66bb4839 | -3.91725 | -44.1461 | 2026-10-05 15:56:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f3b83bf4-80df-3b5c-8f24-2e472ad845f6 | -5.94277 | -41.34514 | 2026-10-05 15:56:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| bcc61d48-6de0-3b9b-aa13-74df19df2e21 | -2.99465 | -42.04657 | 2026-10-05 15:56:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 2daf5af3-0800-31a8-b56f-c153d5d22bf6 | -5.55428 | -41.01381 | 2026-10-05 15:56:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c1861f71-f11e-3f0c-a160-fea241229442 | -2.49738 | -44.0665 | 2026-10-05 15:56:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a35c352a-86bc-3754-9b29-61a28af2d280 | -3.34371 | -44.58557 | 2026-10-05 15:56:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c7693e28-ca14-3378-b9db-eda93c1e3daf | -6.18461 | -43.3863 | 2026-10-05 15:56:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f37faa56-1dfd-37c8-9e8e-fc7a6090a971 | -5.84027 | -45.0197 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 92d5f590-5917-391f-a01a-0576019c2e2f | -6.32844 | -43.8144 | 2026-10-05 15:56:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| fa4a9c34-1a0c-37dd-abb9-8c5fed106625 | -6.04243 | -45.23398 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf248b58-0a9c-3eae-85d4-37f5035a6bf6 | -3.20758 | -42.44486 | 2026-10-05 15:56:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2215b0d2-0b38-36fa-8cc1-bdd4b1e21675 | -3.33075 | -44.58159 | 2026-10-05 15:56:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 516ee7c4-ec17-340d-a734-744f0fb6c7ec | -4.85595 | -40.40252 | 2026-10-05 15:56:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| d85c966a-88f4-3b25-90ec-71eb2ee41970 | -4.85648 | -40.40615 | 2026-10-05 15:56:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| d02c1e86-d7cf-317c-b6d8-ae7f6a231480 | -3.43442 | -44.44251 | 2026-10-05 15:56:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d07ec3a6-839e-3f30-b74f-9a2453bac855 | -5.03447 | -37.0351 | 2026-10-05 15:56:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 7ceef0fa-8d1b-3c7e-a88e-863a590694a6 | -5.47252 | -41.22775 | 2026-10-05 15:56:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 29.4 |
| e6d5688f-c40e-3bc4-9505-3cb9cf7ed37b | -4.8017 | -42.13665 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| d1b0b528-bbde-3158-b60e-4b55543f23bf | -3.11178 | -44.28803 | 2026-10-05 15:56:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 14b50f2f-e76c-37d4-b9ee-92ad5715b9db | -4.23862 | -42.1295 | 2026-10-05 15:56:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f2052c2b-74fb-36c3-9530-d6c58dfd17ce | -4.14487 | -38.58884 | 2026-10-05 15:56:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5ba8cb3e-59a3-39b6-b86c-1bd931f92321 | -4.29441 | -42.18983 | 2026-10-05 15:56:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 467418a4-4b45-3f03-b447-315c11a7cf41 | -4.29468 | -39.14801 | 2026-10-05 15:56:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4a97d7fa-2c9e-35eb-85cd-1e441a503558 | -3.13813 | -42.67043 | 2026-10-05 15:56:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README77.md)
