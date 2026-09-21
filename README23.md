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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea0fbdde-6707-3ef5-bf6a-07eb3ba2d3ed | -10.09116 | -50.26137 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| bb1d2a22-7e97-3d70-8030-b76f1b7eb5cf | -10.45472 | -50.28727 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c51db54e-d71e-304a-b35e-e56de734d755 | -11.09671 | -51.06304 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ed21d1e-125c-36a3-9d1c-03fcf26ae7d8 | -7.43925 | -44.78111 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6d97c397-8629-34a3-a2b3-19443aac982c | -10.45809 | -50.27035 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 40f86c41-f3c2-39f9-8910-59164dc58fbe | -8.7906 | -48.743 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5db1fa7-1158-3d2d-aaa4-2674d2511978 | -9.8313 | -48.44108 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6c3f86e-b70d-3ab7-aa8b-45647c5311c2 | -11.40697 | -47.33916 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b660618e-4740-397a-8ac9-e88d5d746226 | -11.11186 | -47.51626 | 2026-09-21 04:02:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01a9124a-d521-3aad-bbc4-e887009ff645 | -12.19225 | -47.04209 | 2026-09-21 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfd129e6-ecde-3f22-9943-f079b43872d6 | -9.45051 | -45.43053 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cdbd65ec-9261-35e8-9ddc-66fa4912371a | -11.32224 | -47.30512 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31d48d2c-e479-3b93-bf7a-c0344d9148fe | -9.44187 | -45.44436 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e6cb255-c6ee-3c6c-8d02-0cb2ac96424a | -10.42656 | -50.25777 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47d4915b-90fd-3284-93d6-0857003f1cba | -7.82099 | -45.26893 | 2026-09-21 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1fbdc42-93bd-36f4-81ae-44a0a15297aa | -11.93793 | -46.50405 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85727c24-9964-36c3-a198-c3384da3fbe5 | -10.49061 | -50.31264 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e10cdfac-01ab-33b9-9e6a-bcb4d89fa990 | -13.93722 | -47.84063 | 2026-09-21 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a35c230-d4ff-37f6-9dee-312edbda5646 | -9.03014 | -44.92268 | 2026-09-21 04:02:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 937abfd9-d68d-3f5a-87a1-8cd14be38d60 | -10.70157 | -50.7703 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 444c3b8f-3c28-383c-888d-49dbc42100e2 | -10.3676 | -50.22058 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 34f63de0-780d-3383-8caf-72ff2b37c813 | -7.42463 | -44.77868 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b5ced3d-e806-3a23-ae0e-538b26d395e3 | -10.68979 | -50.74774 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ad131c2-dc33-3eb8-8638-954eb1775db5 | -11.31753 | -47.30063 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6ba2d13-cc50-3884-89fd-4524c7b40e28 | -9.43727 | -45.41357 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 117ca01f-734b-3eb9-ad36-e00624f70b21 | -10.37884 | -48.90733 | 2026-09-21 04:02:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3b747668-20e0-3f2d-89a9-363bd5e09d81 | -9.37073 | -40.31477 | 2026-09-21 04:02:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d6725619-c70a-3550-8c47-7531ea6740f6 | -10.37795 | -48.9119 | 2026-09-21 04:02:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 48e4a2fb-57ae-31cd-a109-fd16ffd8b247 | -10.79457 | -50.75909 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91d83821-260b-307f-8d0b-ac573d6ad4a6 | -11.09543 | -51.0692 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3719fe38-24e9-3e39-9c08-0acaac6f966a | -11.11157 | -47.51659 | 2026-09-21 04:02:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b2d3371-63bd-3b37-8276-4fcf403c15b7 | -12.02896 | -47.81311 | 2026-09-21 04:02:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73e6dcab-e9b5-3beb-8d4e-2812e901b4a9 | -11.95458 | -46.49879 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51a3aa96-8c66-3ee7-81df-be099eaf0e04 | -10.48407 | -50.31123 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 529245ab-495f-3726-98dd-68cff46125d1 | -8.77789 | -44.29647 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b70d445f-3d31-39cf-96ec-889cb6ef5fe0 | -12.41565 | -47.03308 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 815aa194-99d5-3ee3-a0c5-5ca9d832468c | -11.65073 | -47.77623 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f17c5164-f9a3-3dec-830b-985e3d488c6d | -10.46487 | -50.29261 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4f144e9a-5fd6-3abe-8a62-b4f30d0795cb | -11.93739 | -46.50691 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 558ec0ef-eb80-303c-8155-a61e9b9bca55 | -12.76711 | -52.85119 | 2026-09-21 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 921c1042-ef98-3972-a933-5712971bff8c | -10.75691 | -50.80729 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f28eb23a-1411-3562-872d-0222041561f2 | -11.32405 | -47.29566 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5c63739-e034-3866-bd1d-3f2ccfc27056 | -8.79152 | -48.73817 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3e001c3-924b-394e-a8f0-7426b7fdfac7 | -10.73391 | -50.71486 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bf369b6-21aa-3ad3-a1aa-9db4505a312f | -7.43732 | -44.77628 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 81d14a9e-b3ee-3896-8df7-552e8fa1a759 | -11.78949 | -49.8099 | 2026-09-21 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18c34467-7cd2-3943-84f6-9d263e19d56e | -13.89426 | -48.56964 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 039951c9-2422-38f6-800a-7a5cb71dc156 | -9.44717 | -45.38665 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8f943ad2-4284-3640-89e9-905b9867dc99 | -10.48016 | -45.09358 | 2026-09-21 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 642081be-1083-3ace-a8ed-11404684af2d | -9.61183 | -40.6202 | 2026-09-21 04:02:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 30123b06-ef50-34c4-9711-938a6fe6e6d5 | -12.53755 | -50.08043 | 2026-09-21 04:02:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de4ff63e-bfd7-3d02-b177-f5bb31fa6c7a | -13.8887 | -48.56854 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6ee81995-a0b7-382e-af50-47e0deec5620 | -9.26025 | -46.18398 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba9f8c0e-6b60-3174-80b5-338c7404bf72 | -13.00494 | -46.9177 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ada7546e-0a2f-391b-82fe-f0370ae5a868 | -9.44616 | -45.39222 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a3db25da-140c-358d-86c0-07f11c849355 | -13.00542 | -46.91527 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1c1746e-46e2-3808-bc8a-dd2e4ec83227 | -9.44901 | -45.40452 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| ad6f84b9-ea5a-388d-8f19-c495395e39e4 | -8.33351 | -50.83571 | 2026-09-21 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce8d0ba9-8ac1-3c80-b51d-78c241740f24 | -7.76748 | -44.82535 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04a645c3-8f8a-3416-b8a4-3b492d072f85 | -10.7405 | -50.7849 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98829ac7-66a9-3f9b-aef9-b3fdb1668334 | -9.82025 | -48.43464 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7cd2e44-9129-313d-bc4d-ea50ab67de4d | -10.80125 | -50.76054 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ef7de76-e825-3497-92e6-c8f82a7ba55a | -10.80432 | -50.77997 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77af5974-9957-3e96-9bab-4f1b81907e65 | -9.26999 | -46.18921 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7917adb0-a3d8-32df-ab7d-f221a67d0f95 | -7.43985 | -44.7485 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 09eaa647-72d3-36b3-86e1-bfde57eb5e23 | -10.43309 | -50.25916 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a6229a5-1edb-376c-9f1d-de8212092118 | -10.70383 | -50.78216 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16d25b99-43df-38ca-afbd-dfc8c25d97f1 | -11.94403 | -46.49934 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ca6b5ec-e726-3228-8e7f-f4d9fe2ebf62 | -10.46064 | -50.27999 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7fb8eda5-0e27-3a43-aa4f-4d54b08fcb8b | -9.45789 | -45.39106 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 07a734ab-b7b9-3d4b-8544-6db42b73ad3d | -10.49609 | -50.34044 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c8512a9-947f-3021-9c0f-96d5c191b626 | -11.88042 | -38.74235 | 2026-09-21 04:02:00 | NPP-375D | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 83d3a49d-258e-3a3d-8fca-43b287b9c79b | -10.57425 | -46.53415 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2aa696e8-ce26-3b8a-9443-e330c884d73e | -10.37237 | -50.22298 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 678aaa30-33a6-3f91-ab64-f0e6d73cbf54 | -11.47153 | -47.76667 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17a22a3a-4040-33c6-a1ea-dacf7a772871 | -10.40272 | -50.24103 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a8a332f7-0eb6-390b-81a5-0c2ea391ce51 | -10.80795 | -50.83931 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efa7bf10-b92d-3e4c-843f-bbf69fab141d | -10.47342 | -46.29033 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a290fc0b-f827-3d64-b55b-4bd61cca01d9 | -9.45594 | -45.3941 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fd295323-33fd-3b25-bfdf-f5fec2275dc2 | -10.46668 | -50.29571 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f83f69de-af29-3669-8ef7-e74fb4ff68a4 | -10.37889 | -50.22435 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49110c93-86ab-3164-be14-44ca6ddd1661 | -7.2962 | -46.76447 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c13694ba-cdb8-33ed-8819-51130e8b15a8 | -8.42017 | -45.8639 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa1902b4-984d-30e6-9049-d7e64f185470 | -10.41577 | -50.24379 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e26093a7-088f-303a-9a51-900586553ffc | -8.313 | -46.00449 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f3c009e-aa3d-3b45-b337-19a61543d5fe | -10.77442 | -50.83207 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12b3f46c-6f09-35a6-9fef-8596f7ab3d7e | -11.94851 | -46.5033 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeb0a4cf-e4e9-3e20-989e-bdee395886a3 | -7.4208 | -44.78444 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d651d7eb-43f6-3f3a-8eb1-98e9055b919e | -9.46573 | -45.39584 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f6cd5580-fe73-3019-b8ad-52664a236064 | -11.95796 | -46.50054 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92dbd967-7dbf-3385-8a96-16a281974c1a | -8.41895 | -45.86115 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c6aad70-d187-3f91-83e9-19e51cf42c02 | -10.38218 | -48.92238 | 2026-09-21 04:02:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07414904-64d6-370e-8625-7c37514167c7 | -8.78042 | -44.2821 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4832647-900a-396a-8c16-452ffd1035fc | -9.2648 | -46.18831 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc61e4e0-08be-371a-9271-26ae48ec8c69 | -9.67276 | -48.97403 | 2026-09-21 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 424d8ba1-621c-395b-8542-82d3b5e08fc5 | -10.93098 | -47.87247 | 2026-09-21 04:02:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acd94294-870b-3d6d-b9c7-b1e259595798 | -14.17776 | -47.87168 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8d48f8f-29ff-3100-b868-eba50ba8931f | -10.34917 | -50.21071 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ec9ab2d-30c5-3dd7-924e-3a8e5c5c39da | -10.76482 | -50.80273 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae0aa12e-1685-33cc-a2e3-244866cd56df | -10.67435 | -50.73326 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README24.md)
