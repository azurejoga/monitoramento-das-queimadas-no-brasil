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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fc31bf2-5f0a-3911-a1ef-8eca3dc2ed06 | -10.46953 | -46.18698 | 2026-08-28 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2faefa88-306d-371c-a7a2-8a81087e60be | -10.9188 | -50.52917 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 852518af-1f4c-3861-9d64-4fd49993826a | -14.92382 | -52.60015 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51586274-35b4-3d6b-8f2d-76d39e6d57fc | -8.60135 | -54.78458 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61fe213e-5825-335d-bcd4-990f789ef439 | -13.45425 | -43.8434 | 2026-08-28 04:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f74fb05-b1eb-3c96-a406-33690c89ab71 | -8.75459 | -44.24503 | 2026-08-28 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a2d3290-ca9d-3cb9-8939-c74fca40c614 | -11.28171 | -54.0177 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf6d862e-00d6-3544-950d-eb86c93d205e | -10.77357 | -50.63182 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8faddacd-184d-3381-ac41-9f69eda4a841 | -8.24367 | -54.98695 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b562c458-e4f0-3333-b506-d2ec62c24ea6 | -6.75498 | -55.69041 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad097a63-f55f-3f0f-b693-8df562f3e133 | -14.39763 | -53.05488 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c327b5c4-67ff-3779-b2eb-c20dcd1051f4 | -9.61701 | -55.11589 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| b6446c61-28aa-3e7f-bce4-b95ce4b74d8a | -11.01819 | -49.65773 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 524505d4-b9f5-363c-8876-4b297a5a8c53 | -10.91216 | -50.5281 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c2634d8-2e0c-31df-a95d-afac701ca310 | -11.76925 | -47.65753 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efd99960-3b6d-3cac-94d7-b9ccf5b41cbd | -13.40934 | -51.41757 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e5764b7-d499-31fc-a613-545273143dd0 | -11.16677 | -51.21945 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ef2d82c-9779-3e86-9400-d65d2b618c9b | -14.39985 | -50.12632 | 2026-08-28 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85145a0a-a779-3452-bb86-38e0efd8d878 | -13.43109 | -54.01817 | 2026-08-28 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85f8c47c-3587-3e3e-ad64-b0a1a72996b2 | -9.46344 | -51.70118 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2737017-287c-3c52-b3e6-047a6df08353 | -9.15968 | -49.96998 | 2026-08-28 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e8069b9-2aa9-3526-8596-b9274fbe810b | -11.71577 | -54.53948 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d61e498-80be-3bb3-b469-ea0ccca2d039 | -8.59572 | -54.72101 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 272b592f-dad0-393f-be0e-dbe09592772a | -11.21793 | -53.99977 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bee411f0-3ac6-3b18-91f9-efc3ebb75e89 | -11.78134 | -47.65082 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c396946-4a4c-3662-b2ed-bf87220d5cb4 | -10.49295 | -64.50731 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7afe1e3-1ada-396f-831f-d3f11504edc6 | -10.92724 | -50.53393 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3a958fba-a935-3a36-9458-1f6038fbdf9a | -9.40477 | -51.63208 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 330bf3f1-ce22-3ef8-94ef-74a46e6e4c44 | -8.78504 | -50.07083 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 821d8496-d22f-355d-8ee9-757d2e3f67fd | -8.80719 | -50.08152 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34f9b7ee-c986-3458-a9ac-881341835f42 | -10.52933 | -43.98118 | 2026-08-28 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbbfb4a4-9cd2-3d10-99f3-8c3e43faf19e | -14.86709 | -52.60216 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1600bf0f-ef86-31f0-99bc-a9ff05a14c19 | -14.90522 | -52.60115 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70983da8-1c85-3494-8729-cedc29254a99 | -14.92778 | -52.59709 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54378d7b-daec-3a80-bd14-f325dac00703 | -9.22777 | -51.53666 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13c35d1f-09ef-3263-aaf4-b9ec46e0e361 | -10.84237 | -50.51678 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d093aaae-d292-3fee-a62d-6f7aa0fd6742 | -9.46105 | -51.71578 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43ca3f05-a0f4-325a-a141-2d3fba959a30 | -13.59037 | -45.78514 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fdfa0bf-0843-3410-90c0-16e14d0e9134 | -10.79651 | -54.01082 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 946598cc-0493-3a75-85b9-d8385ec28774 | -8.79599 | -50.50973 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7394ad37-844f-3d42-ba9e-dc8a7510f672 | -12.50113 | -43.81591 | 2026-08-28 04:51:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8302dd76-6248-3509-88b5-0b3503203b3e | -11.23865 | -54.00584 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4dd09b28-f858-3221-8b89-73f91aa31870 | -10.76525 | -50.64127 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2fc6c6c-42ee-3ceb-966d-8902b69069a4 | -14.42051 | -52.59783 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c256fee-095e-3008-89ee-9f41e652233c | -11.01767 | -45.0739 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9465265f-ce12-3410-ab18-f8d2b7d226f0 | -10.77025 | -50.63128 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8e8aa656-a20f-37c3-bbc4-226052662683 | -11.49005 | -45.07229 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d30a131-029e-3938-b586-086e56508440 | -11.75469 | -54.51389 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bc88538-8be9-36e2-adbf-f833cef6be54 | -11.57784 | -45.52952 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 645b91c0-bdda-384f-ac44-f9ae3406ad28 | -8.22659 | -54.9646 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8297300c-4f4d-3d19-888c-03db40ef2212 | -7.5102 | -61.39061 | 2026-08-28 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0fb9df48-206b-3606-8635-08778d4908f0 | -8.24429 | -54.98337 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9a38626-e98f-31c3-9bbd-59e62b1fc73f | -8.59429 | -54.77811 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 97b57d94-9fdc-3594-9daa-70427bc939b8 | -14.18349 | -52.82677 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 031a5729-4d89-3c03-86f4-46dd0d7de0d1 | -11.22229 | -53.9961 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0609b14d-23e1-3af3-a7c3-f551a9106939 | -15.62494 | -45.93274 | 2026-08-28 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1d90adb-5486-3dd6-b418-ac79fe387c41 | -10.77478 | -54.03611 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b29dc78c-f189-355b-a037-dafcda09b447 | -11.57579 | -45.51414 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47add373-acf2-32bc-98b5-0d8a5caa00b5 | -11.70741 | -47.80163 | 2026-08-28 04:51:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 844d02c3-d871-3e4e-b06a-0a1c9d4012e2 | -11.74199 | -54.52095 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 308eeca4-ce18-343d-b929-30ee4c26454b | -11.21901 | -53.98904 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc117874-80a4-3099-a6a0-3d1af0b47767 | -11.23063 | -54.00881 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3651fa6d-d9e7-3597-a624-cf96f742543b | -10.96163 | -50.29443 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b30bac1-de2c-3da7-8b0b-51ef9d3b76b3 | -13.48239 | -57.05032 | 2026-08-28 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a97c1ace-a8e1-3d86-802e-2d019bc4f432 | -8.77724 | -49.948 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c4e11ae-8c01-338b-80c5-c8be5bcd5fb4 | -12.25889 | -50.58675 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 776048ba-fd20-3f31-9c24-c85f3918e565 | -8.62056 | -50.01597 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 53d2703a-a7da-31ec-b93c-e3478ec1fcb2 | -10.06424 | -46.93694 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 609b551e-1a0e-35ba-8d7d-c4939be2c20d | -14.89574 | -52.59575 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 564aaa40-4065-3602-83ba-4588fdb9aaf7 | -8.02484 | -51.82098 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7eb51a2-307f-3c3d-8a30-a01dd59a7ffa | -15.14769 | -43.798 | 2026-08-28 04:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e03ec6a-805c-3935-ae21-683914aae921 | -12.76179 | -44.26658 | 2026-08-28 04:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a2a4155-c663-3bf6-bb79-b73a29a6704d | -10.78298 | -50.63695 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc07196f-6691-31d5-b20b-230b442148f0 | -14.8985 | -52.60001 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c21daf61-1a41-3e0c-873e-fab0dc12da54 | -11.65472 | -46.73665 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4179b0bc-35b9-3989-8a37-b423871a77ea | -14.86373 | -52.60159 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37e54021-5756-3026-a4b2-d44ca3bf697d | -11.2744 | -54.01647 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d77671d-09a8-3e6c-b8e4-23c45c8e31d1 | -11.724 | -54.53629 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 04db80c2-1e14-399d-b791-a008d68059b0 | -10.79067 | -54.00085 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7de3027-0b7c-37a2-88d2-e8a90f5d3387 | -9.28393 | -57.0756 | 2026-08-28 04:51:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6bc65cc6-9778-3dba-b2b8-25680fc08b98 | -13.43531 | -53.99333 | 2026-08-28 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c0cd204-cd17-374f-8caf-d24c65293199 | -11.22556 | -53.99458 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29f454e4-4f3f-3477-afe6-9bae9f412403 | -12.42733 | -43.4159 | 2026-08-28 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 37b0869c-3e19-363f-a231-7cebc0b4e7dc | -11.20405 | -53.99293 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20795f03-2356-3fff-8795-9e9df2a4921e | -13.59139 | -45.77753 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2f70229-481e-32fa-92a3-2a6604a1fd46 | -14.16655 | -52.82388 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8317f741-75ec-3c2e-8ac1-ce7c85e3a450 | -10.39027 | -61.23903 | 2026-08-28 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9706a975-15cd-3cfc-8ac8-91f1127d12ba | -13.86663 | -54.11528 | 2026-08-28 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f54c3d8f-1bfc-344b-877b-6faf40dc20ab | -14.90186 | -52.60058 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a2c2111c-16b6-3114-ab66-9132d952b260 | -9.4588 | -51.58096 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29e26520-b6c9-3756-83e6-ce5da05d4498 | -11.23575 | -54.00086 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 925092d2-af05-3f57-8adb-868464dab8fe | -8.94353 | -50.77055 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b97e7f3d-8ba4-3252-ba37-7ef57f55687a | -14.97715 | -52.59058 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95aeb377-a65b-3e14-bfed-6f9c11923672 | -10.77213 | -54.04251 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 072ba0dc-3356-3542-834d-95d000e4749e | -11.20449 | -51.24019 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 13eafef7-132e-3910-83c0-a35af3085acf | -12.26555 | -50.58783 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84f324ea-01b8-3af6-97d2-7a60d353629d | -9.22381 | -51.53971 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79b6a2ad-5ba2-3b7e-9295-4e414d3855c9 | -15.53129 | -41.92677 | 2026-08-28 04:51:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| f35936e5-9f48-30cd-84b2-9578c0e14643 | -10.76151 | -53.98001 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cf88b7a-e0c1-3ec7-bd5c-991714967c83 | -10.77364 | -54.03379 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README44.md)
