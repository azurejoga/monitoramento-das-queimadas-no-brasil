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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dad2e20-15b4-3d4d-b837-ca2db449753a | -4.96892 | -44.607 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6eae5bc5-6cdd-3f6e-b3d6-6e54ef8447e0 | -4.46058 | -43.23041 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| df6ec430-16fb-30af-85ea-67fdf5c5cfa6 | -6.37193 | -45.78063 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 527666ca-689f-36e2-867b-b348c5b5662c | -4.88148 | -46.70693 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 667ea50d-54b9-3458-ae95-c4de49cb7363 | -4.57128 | -48.39998 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a681ff0-2df6-39c1-b112-27738353969f | -4.40614 | -44.3629 | 2025-10-18 04:00:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0bc52ce2-d708-369f-b53d-0923f9be6bc4 | -6.18105 | -44.85821 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7fc5e028-ef50-33bc-b6b6-66b441e127d4 | -6.20668 | -44.43195 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9630714e-4464-3224-983c-fb1695fc4e6f | -6.23111 | -44.64601 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fcf69c24-97e8-3510-a334-5c27c7097bde | -5.63149 | -50.03267 | 2025-10-18 04:00:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7887be72-eea9-3d6c-93a2-177eb4706a7e | -6.5266 | -44.90134 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d5f56c1-a47e-328e-b55f-e0274bd5173d | -7.10272 | -41.46175 | 2025-10-18 04:00:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d63c2276-7281-3e3f-bb13-2367ec49ee35 | -4.45987 | -43.23486 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| bb0c1e2c-2220-325f-abcd-aaf3fd2d064e | -6.03448 | -43.4045 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a9355cb-cd29-32f4-a90b-6feafd1e7dae | -6.52378 | -41.49099 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9f86c970-211c-3f0a-9573-faacae320af0 | -5.34255 | -45.00048 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8c1ba9c-0a0e-3481-a75a-f132413df52b | -5.93653 | -43.92643 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0aa236ec-986d-3a82-8c0e-32d52a19a32a | -4.93655 | -41.5339 | 2025-10-18 04:00:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf98704a-c2b8-3c38-9bf5-072d33312168 | -4.30448 | -48.06296 | 2025-10-18 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1b77266a-f9ce-3e42-92a7-ce7d0f34bb11 | -4.9649 | -44.60637 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae224f93-bd4e-3cd4-bf53-5341ca692fb6 | -3.14356 | -50.2443 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f6fa236e-a21c-3c27-864c-a365b548a56a | -5.60013 | -47.49879 | 2025-10-18 04:00:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07d0365e-9b65-3397-818c-e23f3d75bb93 | -3.49462 | -42.72762 | 2025-10-18 04:00:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0fce6a0b-556a-3f5d-9c62-e138a0f74508 | -6.3279 | -44.30906 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8670601-1c71-3229-8d97-3e6ab251d874 | -5.22427 | -44.77957 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6881ff2-1bb8-3b57-863d-c20e37e2642c | -3.14883 | -50.24982 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8ef7afeb-f08b-3fed-b7a4-6a28086ac066 | -5.00889 | -46.02034 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36476270-fcd3-342f-b5d0-0d7d316355d5 | -5.9129 | -44.7667 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27184992-5af8-3127-a593-6373abcc3a7f | -5.8521 | -44.33631 | 2025-10-18 04:00:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 913bc470-62eb-3484-97b0-5a9ddd6d9c2b | -5.57903 | -44.18409 | 2025-10-18 04:00:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81c62c58-4e8b-3585-8d9d-6b67ff7679c2 | -7.22509 | -41.16716 | 2025-10-18 04:00:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 902aab24-9cc2-3b6d-ac2a-2ffd85cf5ef7 | -3.52008 | -45.98816 | 2025-10-18 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0e72b3e-96b3-30c6-b47a-0899866f7114 | -0.75617 | -47.76152 | 2025-10-18 04:00:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66530927-df20-3e65-bb47-97d852e9e7b7 | -4.91804 | -45.09243 | 2025-10-18 04:00:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1d5df90-d9da-35cf-b388-2a4154818730 | -6.97805 | -39.68703 | 2025-10-18 04:00:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89e24c2c-807f-3a17-b265-7523b076e827 | -6.52435 | -41.48737 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4d17a681-c7f9-3987-afd6-ecc8e53f6a94 | -5.88727 | -43.92011 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90b239ac-d0a4-32bc-a2ed-c13565ed4ad7 | -6.23249 | -44.64306 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca4956fa-f539-3ffd-9dec-8ce6eb6c3d33 | -6.52541 | -44.90834 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 673dc1d8-fd45-31af-a021-e0e01dd56e2a | -7.02392 | -38.50628 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 705b4858-1284-3dbb-b87b-bbe08d3c6935 | -4.44942 | -43.22865 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 41a1aa86-da15-33b7-adfd-b983586e3290 | -5.06252 | -45.85751 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 79e22bab-0c9f-33ca-bc9c-2b372370c5d1 | -5.28791 | -49.28563 | 2025-10-18 04:00:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6130bad-0f1d-30ac-ae95-82bdb4a9e70d | -6.76666 | -42.85894 | 2025-10-18 04:00:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 34effeee-b33f-3593-8254-f230c615e16f | -6.76311 | -42.85839 | 2025-10-18 04:00:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f2acc2a5-22e4-32f9-a02c-ee9b9e284ff9 | -3.85445 | -41.57805 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5fb04785-7c19-3c0b-8945-6adfab9079a2 | -5.91351 | -44.76308 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13dea4ad-16ad-3306-82a2-72dbcb5ae731 | -5.92536 | -45.43948 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3a541ef8-dc96-3278-8383-ad1cf7399a8e | -3.06096 | -43.21267 | 2025-10-18 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 329ff7c2-582d-399e-9376-dd2a3d0e01ec | -6.22389 | -44.42478 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b8be4c1-538a-39b8-8cf5-44d91ab1308a | -5.85103 | -44.33878 | 2025-10-18 04:00:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27091491-a7c3-3b17-a97e-33431f5b4e0a | -2.95136 | -49.33623 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d182fe1d-3f40-3663-9af4-a249cb782d39 | -4.97187 | -48.36539 | 2025-10-18 04:00:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e3d9a5a-6987-3cff-8049-715795de7161 | -6.22738 | -44.14094 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14cd9a65-06b4-379f-ba94-80c1af465de8 | -2.95261 | -49.33952 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ba27b0ed-f6f9-37e3-8ba1-77cf39f06f89 | -6.98135 | -39.68754 | 2025-10-18 04:00:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 564700a6-9017-336a-a84c-c873f00148ae | -5.71088 | -44.18853 | 2025-10-18 04:00:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aec756c8-423a-3c93-a615-cbbf2e74ef5e | -6.35082 | -45.75298 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd6da8f4-5dd1-321d-897e-29a37a054fa6 | -5.89943 | -44.24418 | 2025-10-18 04:00:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc8ec1e4-ed82-3ef9-901f-1b6a14a9a2f7 | -3.0678 | -43.21848 | 2025-10-18 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 501d15a4-ca65-3505-ad80-c78790465afc | -5.24784 | -50.96225 | 2025-10-18 04:00:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 946fd82a-5106-35f8-96be-4bc9c363147c | -3.79672 | -51.76439 | 2025-10-18 04:00:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4bbb676-cda3-3495-b117-6107ab10477f | -3.84936 | -41.56556 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5d8d8d8f-7fe5-3fb0-ab47-3307222bbd07 | -5.55642 | -44.14342 | 2025-10-18 04:00:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18127492-62f1-3321-b7f8-56de35c9b5e4 | -6.95545 | -41.55962 | 2025-10-18 04:00:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ee3cd2b1-8bad-327a-9685-59db42f9816f | -5.89107 | -43.92072 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cacbbb79-464e-3e0e-a4a7-0c85455ef556 | -4.45686 | -43.22983 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 24135f4a-14bf-34d1-96fa-1adeb4b1d5d0 | -6.31383 | -44.32199 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5970cac6-90bc-3c50-8560-f58b44236040 | -4.66544 | -44.80011 | 2025-10-18 04:00:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 032214f8-2cac-3773-87ec-ee7ab841e280 | -5.29452 | -47.93233 | 2025-10-18 04:00:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28aa8490-4506-3c76-a941-53363f466e6e | -4.41013 | -44.36354 | 2025-10-18 04:00:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e027384c-1bf6-3ceb-966a-a1ab6d89bc85 | -6.33889 | -43.9382 | 2025-10-18 04:00:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aab6cc4b-e932-3b7c-94a2-8687f65ac11a | -5.15713 | -46.26947 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 924a8118-ec67-32d4-ba0c-a838d9336aaf | -4.69038 | -48.62329 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3251c6c1-8893-32b1-8dad-4d8fcc1637cd | -6.37242 | -45.78068 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b133cd6c-8320-3db0-9773-40c3c534319b | -6.31932 | -44.31289 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4aabf8a0-f1f3-3dcc-9a87-dc40a2d48fc2 | -3.0617 | -43.20802 | 2025-10-18 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f96698f1-d7ad-35a9-a9fd-66bc9a9e969b | -6.97751 | -39.69051 | 2025-10-18 04:00:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c999e9c3-a637-3416-bd75-eca723c01f97 | -5.24789 | -50.95996 | 2025-10-18 04:00:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8e26159-3479-3dc0-8b0c-f5e3807e1402 | -2.65734 | -47.87054 | 2025-10-18 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 673930bd-c98f-3e19-ad08-651971350640 | -6.84121 | -42.42552 | 2025-10-18 04:00:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1e5742a8-ca3c-3913-b322-397b9dd775b9 | -6.36766 | -45.78005 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac7e6a62-fb26-3104-983b-00cb17704039 | -5.90951 | -44.76243 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebb72de2-2c06-3724-8bfd-bb296f8189ee | -6.3744 | -45.76863 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c895e956-d0ab-3176-92f9-50bee0412087 | -4.93939 | -47.30125 | 2025-10-18 04:00:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2baeacb-cf20-38bb-85c6-963dedec47c2 | -3.84918 | -41.58892 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d16b5b5c-e3f1-3d36-8faf-db9aa75d1ec4 | -5.35343 | -45.03648 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0e0d540-8d0d-34d5-bbf9-d2eeac0cd634 | -2.74002 | -49.39303 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bab2b824-188d-3217-bd55-7f189ca8fc50 | -6.1423 | -44.28346 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86199a7e-65be-3c3b-b952-39d14d583ef9 | -5.59517 | -46.38218 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2262fede-71c0-32eb-b3c2-a523c3e1fe63 | -3.53002 | -50.3035 | 2025-10-18 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61ce8225-645d-31af-bd0e-7338920f859e | -6.52026 | -44.90301 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ccd5c60-d242-3163-9061-8441ccabefc9 | -5.2569 | -50.90826 | 2025-10-18 04:00:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c219b443-6d99-30ba-be76-7c651bf59dae | -2.72145 | -48.83445 | 2025-10-18 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9693c6fa-5bf5-3d4f-894f-c261d896611c | -3.68041 | -45.63525 | 2025-10-18 04:00:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 195db9f9-1756-30de-9772-60d242707f8e | -4.93373 | -41.52963 | 2025-10-18 04:00:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d02de934-a5ac-3d4e-81b5-5df3844b57f0 | -5.8948 | -43.89777 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2d85ab2-bf35-3c2e-9ee6-2b8c68f6e835 | -6.33781 | -46.34598 | 2025-10-18 04:00:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8399ff29-9674-393e-a618-069c121d8e01 | -5.91537 | -43.93928 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f19974ca-aab4-3840-8ba8-29a32242db04 | -7.25312 | -39.18569 | 2025-10-18 04:00:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README17.md)
