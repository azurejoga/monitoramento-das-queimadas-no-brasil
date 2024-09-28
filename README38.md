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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc11ce65-e394-3e17-8f80-8e73aff40100 | -3.25838 | -43.05032 | 2024-09-28 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1ad16bf-fd8c-339b-ae15-212ea88018b8 | -3.25783 | -43.05381 | 2024-09-28 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb349b66-ca32-3f3b-8966-66fc9ad03b61 | -4.08332 | -43.34605 | 2024-09-28 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 935eec69-3937-3795-ae8f-7a36152928fa | -4.08278 | -43.34953 | 2024-09-28 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 809b8571-a374-3767-82a1-02fb1de0de15 | -4.07947 | -43.34901 | 2024-09-28 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ea16225-4fdd-3344-9b49-bb94fb399887 | -4.06149 | -44.04863 | 2024-09-28 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed7de742-de4a-3783-bca7-9c1cad430410 | -4.94253 | -43.68313 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71969418-44bc-3530-a8cf-4e6a4a1d4c32 | -4.92867 | -43.66325 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcf771b0-29fa-3f49-9e63-3ce4c65b27d3 | -4.78922 | -43.79394 | 2024-09-28 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f685f4cc-ca22-31f7-a4f6-423734a5dae5 | -4.78538 | -43.79688 | 2024-09-28 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6329156b-3695-3fef-8f8e-12b0555ff2c7 | -4.6588 | -43.75893 | 2024-09-28 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13902fc3-30bd-379a-8f64-d3cac9cffcfc | -4.65826 | -43.76239 | 2024-09-28 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 761fef2d-5516-3f1e-841f-2a37785ed78f | -4.63824 | -43.53961 | 2024-09-28 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 112cc496-0672-381c-835b-07485382210b | -5.03594 | -44.13284 | 2024-09-28 04:19:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74d77b52-0336-3e0d-b0e0-49db6ae6bc14 | -4.82042 | -44.35547 | 2024-09-28 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ee1f42a-820d-3e15-abce-4eafa11b2751 | -6.3905 | -44.78109 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5fd9d06f-7688-3a57-89c5-9f1ce4cb6697 | -6.38996 | -44.78453 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 97d986e2-e7fa-3e53-864a-71d7dd792da6 | -6.37442 | -44.73274 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7472f0f8-1341-3c86-a9c9-9a784e2c8af3 | -6.36177 | -44.72723 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ab2f91b-81d9-3c90-9b01-d019c7230f76 | -6.17059 | -44.29425 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d070dffb-23e2-35a7-9c41-379737018f3c | -6.17005 | -44.2977 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b44fcaa-4666-3d6b-b486-8b35fec2514d | -6.16675 | -44.29718 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aade54a3-45cf-38f8-b312-decc071469b9 | -6.03892 | -43.6332 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15f0bf3e-5de8-38d2-8c5c-619e14221345 | -5.98858 | -43.80423 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adde94c2-a091-3711-9c89-e64f67615403 | -5.98804 | -43.80771 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35982fff-0aa2-3aa1-9c00-67ae512998ef | -5.8808 | -43.86235 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12493b11-6b42-3c7b-b29d-982f85bd1a87 | -5.88026 | -43.86583 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe9d63ab-8fa3-3179-b2b0-119fb7b5aabb | -5.87972 | -43.86931 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23307353-033c-33ff-a733-3d40fd4f4233 | -5.87749 | -43.86184 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e243ab5b-3a10-3a9f-8a08-a15263f02f66 | -5.87695 | -43.86531 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ecd55f6-57cf-3d15-a3d4-f63ee8981bc5 | -5.87641 | -43.8688 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 321c79c2-cebc-303f-a6de-a2d56cf7a8f6 | -5.87587 | -43.87227 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3c335cc-cd9d-3f61-a699-172e41ce7fd8 | -5.87363 | -43.8648 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd6ccf3d-2bb4-3b99-ab5c-d434df14e61d | -5.83863 | -43.6525 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6468130-5e6a-3703-9717-4088a4d58f6e | -5.83808 | -43.656 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dd1a333-6746-3b73-a26c-d448afcfcf6d | -5.83531 | -43.65199 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f20adaa9-220f-37d3-9697-07dea7c50ffe | -5.83476 | -43.65549 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a3d4e15-db37-380f-9ceb-28b3678eba09 | -5.83144 | -43.65497 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2303c453-845b-3740-aca0-543e1b7400b8 | -5.80806 | -43.97883 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb2c5aa0-cf83-3d9d-a665-8f27b47465cd | -5.80476 | -43.97831 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e6b55b4f-9f91-32da-979f-94b7784b95f1 | -5.80422 | -43.98177 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab5dd841-4582-357a-a5fa-bfacdd3f8241 | -5.79797 | -43.73908 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 257b91df-b57f-3187-b627-def4f7a5f79b | -5.7952 | -43.73508 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eddd32f2-a71e-3111-a126-98dc6df7a8ec | -5.79465 | -43.73856 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 505702bc-a4d8-3f33-afc5-bfc5573def04 | -5.76789 | -43.82346 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce0e734a-bf7e-3f78-b5f7-55131d747272 | -5.76458 | -43.82294 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3b319bf-a5c0-3899-abc8-5f4407e510b5 | -5.71656 | -43.93219 | 2024-09-28 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbc93fac-9997-38ac-a692-5771dbdd6e15 | -5.63511 | -43.95498 | 2024-09-28 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a034e0a6-53ee-3544-97f1-bda09e949062 | -5.63457 | -43.95843 | 2024-09-28 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e699ee8-916d-3729-a74b-f18827455658 | -5.92699 | -44.00446 | 2024-09-28 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01f1a9c5-fa96-3838-bebc-91bc7f648441 | -5.8008 | -44.13697 | 2024-09-28 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52d294f1-c2b0-397e-ae22-837307cc7791 | -5.80026 | -44.14043 | 2024-09-28 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1051efa-dba3-3cf2-aac7-08dbcfc31558 | -5.7975 | -44.13646 | 2024-09-28 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eca9f84b-9415-37eb-a425-b7ccbfed66bc | -5.66953 | -44.23246 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5772db3c-bf95-3bd8-86df-0b75ce72e93a | -5.58001 | -44.08778 | 2024-09-28 04:19:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b5891f3-f3db-3f59-bc15-e8d3ddc2a4ca | -5.56166 | -44.20491 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 515117cc-61f9-39a3-8a25-6a0a9f804f6b | -5.56112 | -44.20836 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19702ef6-bcef-329e-8a17-03de0494a7fd | -5.55728 | -44.21128 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 149bff87-df4b-341d-a09a-9300d8515156 | -5.41683 | -43.36749 | 2024-09-28 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a680806-c541-3514-8daa-349113b30018 | -5.4135 | -43.36698 | 2024-09-28 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4136737-a9f3-3a7d-99f3-83ed85a27b85 | -5.40649 | -43.43428 | 2024-09-28 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5171125f-b1f3-327d-abe0-751de9cf8ae5 | -5.40594 | -43.43778 | 2024-09-28 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5aea2cec-1098-3b7d-9f2a-6f8320b6e4d1 | -5.40316 | -43.43376 | 2024-09-28 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac6b52b6-f900-354e-b867-b683ef85c56b | -5.40261 | -43.43726 | 2024-09-28 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57b9df0b-c9b6-3e51-90d4-e2fe32890bbd | -5.29522 | -43.84127 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db731686-d73f-3f4d-ad0d-f6ae899e5f0f | -5.39474 | -44.64404 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82de054d-c84f-3d45-b580-f11d43dc8896 | -5.39198 | -44.64008 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a6366c9-c7ee-3d3e-8faa-20694c49723b | -5.39144 | -44.64352 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f29b76d6-629c-307c-ab08-546ec6c4171b | -5.34565 | -44.4566 | 2024-09-28 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfd7f758-a3d0-3c3a-adbf-9654ef65f260 | -5.25894 | -44.72433 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f836fd8c-5805-38f5-bd0f-394a628a759e | -5.2584 | -44.72777 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b2b7a41-b810-3fb5-8457-016e2c6b99bd | -5.2551 | -44.72725 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18965fd0-082d-391a-81cb-c64dd5855ef7 | -5.24931 | -44.61351 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ce59880-f79f-3543-84ed-f4e95a0b9dda | -5.24602 | -44.613 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e46e677-55cf-36c6-a420-b0930b2f94d2 | -5.21876 | -44.48541 | 2024-09-28 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc71a1e6-94c9-3fec-9e4f-1dd946419ea2 | -5.21546 | -44.48489 | 2024-09-28 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3263d56a-ba84-3e07-bb81-7413260217f9 | -5.20843 | -44.52959 | 2024-09-28 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daf01633-e94e-331f-9353-26972866bf9e | -5.20789 | -44.53304 | 2024-09-28 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cf90b45-7ea8-35da-abeb-61ca64a07d06 | -6.1025 | -44.707 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa3ac16c-5f1e-36ef-8182-701b9e9f661f | -6.10028 | -44.69959 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01c48361-43df-31db-8962-8771faaf1167 | -6.09974 | -44.70304 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65128c4e-5309-3718-b02e-bf34574332b4 | -6.09644 | -44.70252 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3921652-1122-3f3e-bf5d-db42d3a3faaf | -6.09315 | -44.70201 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74921110-08d6-3c95-943d-d64c8d4e66ac | -6.0926 | -44.70545 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea14ddce-ad24-31d8-ab74-2bc16c547dd6 | -6.03972 | -44.54198 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d61e4598-21de-3f71-87de-df5f04bdb034 | -6.03588 | -44.54491 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89cebbb2-0212-321b-9cd6-0a1247423dc6 | -5.98208 | -44.56471 | 2024-09-28 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd405710-208b-3b1e-8934-974af2c50db1 | -5.98154 | -44.56816 | 2024-09-28 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3aff78a3-f183-385e-9c83-0f71e7dd3cbe | -5.97879 | -44.5642 | 2024-09-28 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9046a391-689a-3238-8f51-d9ba77a42c49 | -5.8159 | -44.38634 | 2024-09-28 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d2dcbda-01bc-33ca-9492-36012ec5d653 | -5.79421 | -44.85213 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd401860-7129-358a-9e39-3c0e05ef0b2b | -5.76942 | -44.46724 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4595b1bd-4785-386d-a147-45940b029493 | -5.76888 | -44.47068 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cacdac16-32bd-36c5-824b-01e56216a622 | -5.76613 | -44.46673 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f348043e-1b29-3299-8948-25c77ee34ef3 | -5.76559 | -44.47017 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 785205c5-a511-39ae-8f86-cdb1888d0230 | -5.76337 | -44.46277 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7db88a5-4376-3963-8fc6-efa3e34838b8 | -5.76283 | -44.46621 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 619ba221-41da-35d5-8c66-dbd4eb4ba6ff | -7.15426 | -44.42149 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d36ef082-a537-3faa-a28c-30cd7fb5f44e | -5.75953 | -44.4657 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c39ae5e-b83f-37db-8e33-444c5dbf1ee1 | -5.71862 | -44.81194 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README39.md)
