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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72507b8a-42ea-3559-9ead-2ca4986a9654 | -10.74729 | -44.87983 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 057f0ef8-23ee-3e69-af90-c8bf0dfa8f26 | -12.08525 | -44.98306 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a294f39c-1385-3dbe-8e9b-3ce4cca935c0 | -7.9792 | -44.28514 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37f5902d-f7e9-31ed-8ed1-f09d0bf753c5 | -7.11341 | -42.76054 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b9b63221-2efc-3901-96e9-930a0f913698 | -12.10517 | -45.0332 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c7ac886-4b47-33ff-9092-4e1b70491880 | -11.34142 | -45.21003 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01a8fd52-8689-37cb-94c5-0733e4ed3fa2 | -10.83862 | -48.3407 | 2026-08-31 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| fe8561d1-f61a-35b0-ac8f-d53ba0de8b88 | -11.367 | -45.20655 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9da5a73a-445e-36c5-bfa7-973ff49b774f | -11.21299 | -45.10276 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a363a59c-1ddd-3a66-96c9-4d3f638e1237 | -7.76643 | -44.06068 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2de097d0-db50-3c61-aacb-c1080a21217c | -7.77675 | -44.06219 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcfcdf58-2445-3ac9-ae2e-f8f424a839f6 | -6.86729 | -41.70196 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa51a845-0d18-3f5b-88a0-37f1f2baa7b2 | -5.60132 | -44.00208 | 2026-08-31 04:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 299652d7-fd1d-3551-9dd3-3e9371db2c45 | -8.38143 | -45.76447 | 2026-08-31 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a649bc75-2c9c-3c79-8e5c-50447e4c5697 | -6.7713 | -55.64923 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 11303b65-dc3e-3226-a895-b367daccc78e | -5.59 | -42.32313 | 2026-08-31 04:14:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6fda2b74-e3b7-3704-903e-d46bf5318521 | -10.83038 | -45.31233 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f665b34-1a2b-363d-ae5c-95f3b0b51e4a | -8.85198 | -47.06583 | 2026-08-31 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa928109-169e-31ff-8448-6540d41effc7 | -9.80672 | -46.45671 | 2026-08-31 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44c35724-ed0b-37f1-a216-b3c5f09acd00 | -11.21016 | -45.09835 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 07b7a12f-a26b-3b03-baed-1a20e0b17096 | -11.32765 | -45.19633 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21a49cd2-f629-35c2-8617-0264234a2f87 | -10.73775 | -54.04525 | 2026-08-31 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25584fbd-b3bf-3524-ae68-ee93f7dfd947 | -11.61081 | -46.71763 | 2026-08-31 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39ac0114-74ce-3b47-ab71-80abc0879a3b | -10.56675 | -50.36402 | 2026-08-31 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceb157db-9a70-3a1a-8a1d-a2eaba5a9400 | -7.77614 | -44.06598 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb9b0631-f5b1-3b26-b435-1e12e735efff | -9.42045 | -45.65023 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a95c8b3-7de6-3cca-b597-f9cb185b160a | -11.21583 | -45.33034 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93364d59-0025-3786-ac84-4f2cff3081a3 | -10.97733 | -48.41328 | 2026-08-31 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29ff110c-06b6-362a-8ddf-9d44d25a2890 | -11.21489 | -45.09125 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| df9dfd60-52f3-3aeb-aa3a-f90cf09db4ac | -8.3842 | -45.00126 | 2026-08-31 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52d5beae-a894-324c-95cc-5e01b29e7e5c | -11.87688 | -45.82172 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 055d1341-1a83-3306-8d2c-f31b4be03fc3 | -7.52189 | -55.33659 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ce7ed88-c428-318a-926e-76f44834006a | -11.79147 | -47.66404 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e91c630d-e171-3f5c-8796-fe878d923ff7 | -11.66612 | -46.71606 | 2026-08-31 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffa3bb25-c4ac-331a-ac74-be43d7b3f4e1 | -7.61317 | -44.88355 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3af1f536-cfb2-332e-b7fc-056801f03666 | -7.11008 | -42.76001 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 20d357cb-e783-359b-bd99-7218507cc5a6 | -10.80253 | -50.65768 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6f5997de-9d40-3899-879e-7cc407cea527 | -6.91702 | -41.64642 | 2026-08-31 04:14:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c61af0b9-2e75-3454-b97b-a4a168dab941 | -7.37206 | -45.07033 | 2026-08-31 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30e53646-ed5e-3686-9388-b45878bb12c1 | -7.10951 | -42.76353 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7d8d863c-a0c9-3cfa-80e4-09e5b38d0a9e | -10.75458 | -44.85735 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d4f5894-9d93-341b-a462-416cb7fa7b3f | -10.15329 | -45.7337 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c37d0ad-957e-35e8-a8e4-856ebff32de6 | -9.41763 | -45.66684 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be7e0a5f-ee4f-310c-8d86-b8e2acf62612 | -7.96141 | -44.32893 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3db638b-2f48-3e4c-9a11-e42ea5460eac | -11.36247 | -45.23363 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0841cb08-5f3a-3524-a914-01f1985f6e26 | -10.74986 | -44.86441 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 52133f18-0b42-3af1-a6c2-a13f62f44ca4 | -11.87621 | -45.82579 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a35d563-eb1c-3dd2-bb17-678150e2664f | -11.22045 | -45.14401 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2e58c9e-3de6-3ca6-845f-9cdbe92a0d1d | -11.15082 | -45.04869 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbf481d2-019f-314d-bda9-95f587c3522c | -11.36983 | -45.21098 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b1aaa51-a31a-3e86-9e65-6b6caa5c146a | -10.73817 | -47.96316 | 2026-08-31 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ba2f51b-ff4b-3048-8a3c-a242480c3775 | -9.46588 | -45.62333 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39bad5a1-095c-361f-a10b-9af7988bbd89 | -10.1536 | -45.70045 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1fbb47c-b289-3187-91ab-d09c800420c9 | -6.84244 | -41.68746 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fabcdd2d-881c-3ee3-bd0a-509e54a2d7d3 | -11.21186 | -45.35392 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9133a856-c6c5-399c-9629-b46c34c4c992 | -6.86398 | -41.70144 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 562cac5c-942c-3157-988d-586edf2ae65e | -11.36287 | -45.20987 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eefbb06f-1eb5-35e0-b887-cb24f85110c0 | -7.11027 | -42.18425 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f62d7808-8c15-3ad2-8f8c-36963d582748 | -10.06249 | -48.70404 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deeb39c7-3acf-3c11-b946-a04df41c0e65 | -5.45536 | -42.65145 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9936be53-fae5-3532-b8b4-bf41d21fce10 | -10.81903 | -50.68845 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 863bd65d-2b4e-3d2a-83a2-0a6e80024911 | -11.33017 | -45.18101 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9f620c1-53ca-3ef5-8cb8-ddff1f8768d9 | -12.13137 | -47.26257 | 2026-08-31 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef35efdd-348b-3b3d-964e-63dae50ef34e | -11.23955 | -45.12562 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 368faf19-f507-3591-8c3c-c3face0a54ae | -8.08557 | -45.46933 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b887fea0-348a-3dbe-8bf2-cc7dc40b4e11 | -10.83607 | -45.32147 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 195b280f-3902-3b0d-941b-fd34e062d92c | -11.2165 | -45.32637 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e5d940e-6837-3fe9-b8ba-95ceb269adec | -11.07454 | -51.52051 | 2026-08-31 04:14:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70a2caa0-bf8e-3bbe-83fb-3605d98117fb | -11.92683 | -45.06915 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 325a2c65-1979-37bb-9e53-10e353cfbdba | -11.78664 | -47.66848 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6277b1b7-364e-3c8d-b0a0-e27b3778e1c6 | -10.8094 | -50.65826 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34108d7b-1f31-3a53-859c-ce85b51597db | -11.91427 | -45.05968 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf667f3c-2754-369d-be12-8c7fbf8513a4 | -12.07718 | -44.9893 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4ff8732-c978-357a-ad30-b4572ebedf33 | -10.0632 | -48.69996 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3357c35-4d2c-3300-9644-26f75e2996d8 | -10.74288 | -54.05102 | 2026-08-31 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aae73967-e839-3db8-bf90-1e345b3bcf0f | -8.17744 | -48.81239 | 2026-08-31 04:14:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40ce7afd-d1f0-3bae-9766-5144deb58fba | -8.3933 | -44.99022 | 2026-08-31 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2f847aa-5fb1-37fb-a7fb-4f469b13d1d3 | -7.06337 | -42.20167 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 89358a11-9252-3047-8027-e7e8cbc5e577 | -7.52063 | -55.34321 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d645c2e-83bf-3797-89c9-b894b7365f5b | -11.78655 | -47.67138 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e3e1e41-a15a-318d-b011-a1b7fb00d6bc | -10.15291 | -45.70465 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77662e7a-c5dd-351a-ac65-9192ef83bdd0 | -6.76881 | -55.64236 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b371b222-b561-364d-bd6a-0d2ebf652860 | -10.8168 | -50.68867 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 452807cf-9191-3593-8d7a-a8787033f009 | -8.33277 | -45.64876 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2b65aa7-4dad-3910-8076-a969e45db088 | -11.53858 | -45.48135 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be9ca28e-4a3b-3f0c-ac45-5757ef71801f | -11.37151 | -45.17952 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b312a152-943f-3553-9bd5-3c24c6f28ffb | -8.09065 | -45.46126 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43db41a6-626d-3065-b9dd-3c4d4ef1e396 | -7.07607 | -42.22858 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 268a3ae8-5411-3f8c-942e-86f41c6512d6 | -7.12063 | -42.7581 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 523ac2d8-fdec-35ed-af88-5d4cee57babd | -11.21993 | -45.10386 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d95b7dc-dabd-3b36-8d3b-ce22ce780a7a | -10.80069 | -50.65092 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b77c5516-d1ef-3f42-8bed-10123fe8f564 | -10.74793 | -44.87597 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3694fe2-e46b-3418-a940-ee0ea8a9d1e6 | -11.35117 | -45.21576 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12c35767-684c-3dc5-99c2-4e9162c70bc3 | -7.13508 | -42.75323 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c4b743a-82ba-33c3-bddf-eb27ca5a59c4 | -11.37693 | -45.16844 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c0d6722-1f36-3f09-8b76-31ca44857427 | -8.92178 | -45.0158 | 2026-08-31 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 572db1b5-9bac-3770-b785-91ef92281e40 | -10.83957 | -45.32207 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7808f543-6883-33a0-884a-4a80bf8d1082 | -6.86595 | -42.88342 | 2026-08-31 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 60d82d21-6272-34f7-8ebf-b45249adcb7d | -8.85045 | -47.06786 | 2026-08-31 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 479bdf75-f37d-3df1-9c67-1a01732922a0 | -11.15839 | -45.04593 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README30.md)
