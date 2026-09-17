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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c7bc41f-275d-3888-9740-4f8b9d589004 | -9.94696 | -45.30082 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f892448b-38f2-306e-a4a6-96f4c2b9dca3 | -9.77457 | -46.09577 | 2026-09-17 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43f57453-5cac-3712-8d85-cecdbb959a51 | -7.07803 | -47.49069 | 2026-09-17 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bf1e841-8411-346a-a495-c4a883ae3944 | -14.56005 | -39.63299 | 2026-09-17 03:55:00 | NOAA-20 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 54e5cda9-369f-3281-b132-836217f8b7a3 | -9.95119 | -45.30831 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d334f42e-5a66-3f82-8f30-40396a5f2db1 | -11.98021 | -52.47151 | 2026-09-17 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42a7d77e-a87e-393c-845c-6a212c3e259d | -9.45753 | -45.45128 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a4e41ff-c4f4-3145-b9d3-3ce1fc8fa25c | -12.45007 | -50.80999 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 29e2fcc1-d519-3680-a62d-a0e5a88d6fa2 | -12.43562 | -50.84674 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59e6432a-7e90-3355-88ed-37c771813d0a | -10.53734 | -44.86507 | 2026-09-17 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f9acbc4-f168-3f1b-aa57-773a73c2d574 | -7.12811 | -42.16212 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ebe68d15-e820-370e-9d90-cb729302f38e | -6.95973 | -42.58076 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9e1377a-fc5f-3148-8f65-7238f52c9640 | -7.58193 | -44.92882 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f277f37b-9ca3-39d3-9d2b-5218f3fdf57e | -9.56812 | -46.57726 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62df85ac-d821-3f47-ac0c-0247006b6bae | -12.45945 | -50.82917 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| e98a5b74-d1cf-366e-bd6d-a680b3df51c2 | -7.12934 | -42.15504 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9bcb027-30c6-3256-ab74-d5f37e3e8270 | -12.46928 | -50.81426 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa97a4e5-9956-3a75-9f5c-f84c23fa78df | -12.45254 | -50.82774 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| e3979023-8aff-36c9-a68e-a4cffdd7ef68 | -7.03892 | -42.03961 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fe9236fa-a530-36a4-873f-a70f581016c0 | -7.18653 | -41.80179 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab1363f4-0081-3293-997b-ba347f737231 | -8.25546 | -42.16306 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f038dfda-1837-3ade-8350-0f3d906b4630 | -11.88835 | -47.59116 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| db1bd60e-67ba-33cb-89da-6866b82d1cf2 | -10.78728 | -46.19732 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 06c31eca-e537-3fab-987f-c743cc799fcf | -8.8514 | -46.92191 | 2026-09-17 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a5dec9e-4500-3bcc-a49e-52654fcc7c90 | -11.32905 | -46.77325 | 2026-09-17 03:55:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f10feaba-4670-3657-9457-787bd6a85b8b | -11.56689 | -46.88513 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e863994-4672-3704-b558-341f25042cdb | -8.78223 | -46.90524 | 2026-09-17 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e984635-b706-3571-b4a1-ee65aaca7e35 | -7.5861 | -46.33385 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c9d9bf7-66ed-3f2b-bfcb-96b02b3d9095 | -12.44835 | -50.81537 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 259b5072-655c-3eff-b50f-162c73a3fcd6 | -12.49376 | -50.8254 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ac2db3a-d4e2-36f3-a393-4defc3b3f15b | -12.47042 | -50.80882 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8386a71f-1070-3263-b50e-85b8a3b35311 | -11.13139 | -38.55602 | 2026-09-17 03:55:00 | NOAA-20 | CIPÓ | BAHIA | Brasil | 2907905 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 1e7a1802-a1dc-3c7d-acb6-ccf912be2614 | -11.32267 | -46.77908 | 2026-09-17 03:55:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96cc5074-306f-3660-a982-a024683fa5c9 | -12.52213 | -45.96313 | 2026-09-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba263236-fa59-3024-8a89-cdbafdd5e0f1 | -11.27479 | -43.47589 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf972f5c-80aa-3074-bbbf-3154ef179f88 | -8.29359 | -45.65211 | 2026-09-17 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5637cad2-b219-3635-88b6-a9a32f154e6d | -9.59153 | -46.65562 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 610fccc7-094c-32f9-a68b-80d883faf5cd | -8.69366 | -44.87358 | 2026-09-17 03:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01005fd6-5490-3539-a5d7-1ebb503cc807 | -12.45075 | -50.83866 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d3394217-aaea-319e-8d91-a59b4c3a742e | -7.03604 | -42.03218 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 811b0a2a-709e-3247-a027-2cb11928f45f | -9.89014 | -48.38858 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3089cc4d-004e-3401-9979-e1e21636845d | -11.89875 | -47.58277 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 350a8c35-8125-332a-ac3b-9a10db55da64 | -12.45784 | -50.83466 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3c3bf3d2-98d9-3aeb-a1d4-be4e6e0d7a33 | -8.9022 | -43.8854 | 2026-09-17 03:55:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 69f2e009-5dea-318c-aaef-b2ac364186b2 | -6.87881 | -45.46921 | 2026-09-17 03:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c95a7b5-7cba-3159-a933-9ad3c0c3fc82 | -12.46885 | -50.84841 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 96899b34-767b-3052-9dbc-93fdef6db977 | -8.56235 | -44.54935 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ed82e13-5980-32b5-bdf7-d7a080d5034e | -7.04272 | -42.05056 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f598e137-a86b-31ae-a111-47c6762a3444 | -9.60484 | -45.34254 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 129dbb3d-99e3-3301-9379-785f4749622b | -7.96703 | -44.83876 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1fa78664-79bb-3545-9ee5-5f2c3d689c07 | -8.78293 | -46.90148 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 647758e4-e3e6-319a-8d40-c4e7db04e97b | -9.89935 | -46.51157 | 2026-09-17 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9544d13-caab-3119-a109-5e8fa58e9780 | -9.61288 | -45.35218 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12eecea8-6729-387b-9ff9-0e6b4836123a | -7.72273 | -42.49253 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ca4fb2e1-178e-33eb-8832-6d93d8131777 | -12.44778 | -50.82087 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 863c182e-9377-3725-8268-3746f8319efc | -8.13963 | -44.862 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df72a967-9034-397a-a3e0-c11c480ff258 | -9.04063 | -47.7592 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37e93d60-09f1-321c-9fa7-a09a2f002aaa | -12.48655 | -50.89255 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7cbf07d9-aafd-3cab-972a-e4518067678f | -12.45853 | -50.89782 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 41d77d02-7ffd-3eb5-a93e-0a63314b44eb | -7.11864 | -42.08854 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b33031a6-1448-3e21-a2e2-c7798d575839 | -8.85744 | -45.86615 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76d9b44b-38c2-3b02-bc01-57d3504748ed | -12.84968 | -44.39164 | 2026-09-17 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d1ddc45-dc6a-3db4-88cc-8861dfdf6cde | -12.46447 | -50.80191 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 72180a35-b6d4-3815-bac1-d5b03a197335 | -7.38508 | -44.5007 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d3d8fde-e2b0-3905-805f-735b8be92ff9 | -9.79157 | -46.48003 | 2026-09-17 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cf691d6-e474-387a-b1fe-0e17c90f9936 | -10.80234 | -46.17145 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78e14240-d12b-3cfc-b1d9-5c8b49b86abb | -9.94992 | -45.31171 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f8c4181-9f7c-3249-aa30-417eb2322f9c | -7.19277 | -41.81295 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 85a7b844-9730-35fc-9131-851dcc19c139 | -8.78466 | -46.91003 | 2026-09-17 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 83720d6a-6b65-30d1-88d9-23165a32f144 | -12.45716 | -50.84009 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| c692ee7d-ad00-38e3-bfd8-fd462a564581 | -11.2624 | -43.45062 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44655a60-7465-3443-9fbf-00f67a637fe2 | -12.85391 | -44.39243 | 2026-09-17 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 811909c9-d1f4-3fa2-b174-1079a07d823c | -7.0006 | -43.33303 | 2026-09-17 03:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c5e97685-cfda-3d4a-9c08-f6b6c5e1aff4 | -6.1174 | -47.18003 | 2026-09-17 03:55:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 089f52f6-e249-30fd-8d10-c4d9e46eda4f | -11.02222 | -47.56802 | 2026-09-17 03:55:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be73c510-6ab0-3347-837d-6d1be9aacadc | -9.21224 | -44.44106 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30030ad0-4c71-35ab-9044-523caecc2436 | -13.60495 | -46.94389 | 2026-09-17 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 43ac3ef0-157f-3b61-b5eb-e9271c83def9 | -8.27124 | -42.16601 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b08b4643-070b-3d36-944e-580b6560ff1f | -9.11542 | -45.72611 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8b7222a5-fc23-3146-b0fb-b3a7d6068952 | -8.55575 | -44.50141 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f94cbf29-1bd7-39c1-8f45-a859523b04f7 | -8.39351 | -42.20502 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 6bf6518b-a82c-38b2-993b-027f10fba0fa | -12.47412 | -50.85532 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 8bceb607-8c0b-37a1-b2ba-d5b5176569fc | -12.46226 | -50.81281 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 47297688-effe-381f-8022-5c4cd9c6b084 | -12.47981 | -50.82801 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 53d49f7f-5bb7-3a9f-a494-bd361a203c99 | -7.10258 | -43.11073 | 2026-09-17 03:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e223d609-30c8-3c1a-ae6e-c2f61562de03 | -8.50279 | -36.27567 | 2026-09-17 03:55:00 | NOAA-20 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a573cb63-f231-338a-93ea-adf426b8abd9 | -7.30044 | -42.34965 | 2026-09-17 03:55:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9911a535-7e06-3d80-a144-af0cbbb014b4 | -8.20088 | -43.68317 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 792132bf-51ae-3549-8b1f-9a518fb80446 | -7.27371 | -44.21295 | 2026-09-17 03:55:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47be1846-f299-34f5-9817-c987e18ca7b9 | -7.12348 | -42.165 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 12b2c860-335b-3cdd-b312-66aa5dc5b076 | -9.61148 | -45.3608 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 03c748b2-9f15-3984-9ea2-3acf0400bf60 | -12.44139 | -50.88263 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30c09775-590c-34b3-bc8e-d9a4adc0b6cb | -7.18966 | -41.80733 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6294b7e0-fc93-371a-a98f-409a3595ed7d | -12.43742 | -50.87011 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b6dbc0c8-06e2-3bcf-842f-9bdcb2c3a9e6 | -7.14765 | -42.0967 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 10996f60-ff00-3471-8c71-cc084b22e9c9 | -12.50564 | -50.70391 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 803ba0e3-4e10-35c2-ab93-6d8c32a5d2ab | -12.50519 | -45.92254 | 2026-09-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 682ec501-b32b-3ce9-aa25-4bdb983d0665 | -9.61187 | -45.35767 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28de5e0c-e9e5-30e0-a832-db0afd6118bb | -7.04331 | -42.04713 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ed2613f-a595-31eb-a1ca-a6bd75fd7571 | -7.03032 | -42.06676 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README23.md)
