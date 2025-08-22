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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dba75081-a4f1-3562-9726-af28eaa1506d | -14.76558 | -45.41073 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2c564073-e34b-34c8-b0b4-e190283a9d77 | -9.82197 | -45.95627 | 2025-08-22 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b93654a-0def-386d-93de-7b9458a0ce06 | -13.38174 | -47.49493 | 2025-08-22 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e59e66c-9482-3978-a4c0-f109c86746cc | -12.44151 | -44.7042 | 2025-08-22 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9155abe-3e31-3ce5-a490-9d577146721e | -10.27035 | -46.76045 | 2025-08-22 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ed662cc2-f27d-3924-b257-c07bc2a213ac | -11.43701 | -47.30885 | 2025-08-22 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 051a2c60-36e0-3666-9f45-baba272d178e | -11.32847 | -48.33072 | 2025-08-22 03:57:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f51d2945-2e9c-3ba2-88b5-267384cf405b | -13.71622 | -42.68753 | 2025-08-22 03:57:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6ca83169-c189-32ec-aa5e-df850460411b | -12.52707 | -45.60422 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7a06d4c-dd03-3568-8cf1-33202ca850f2 | -10.71286 | -48.22254 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 200b5cba-c4b8-3822-8fa7-3ac54dc9d50b | -7.85898 | -46.98976 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efe84240-ff8b-3502-b9e7-168c8854e38d | -11.28398 | -44.9587 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f69989a5-7b0d-36fb-a218-18149eeac53f | -11.133 | -44.70875 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a364fbe-2f7e-3975-81eb-393e2470fba5 | -12.58806 | -47.08866 | 2025-08-22 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b628fb46-2224-3ec0-91f1-de6c39e95618 | -14.7649 | -45.41444 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d477590f-bb90-3b9c-a5bf-426c39f2953f | -14.97534 | -47.14175 | 2025-08-22 03:57:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aef9be00-aafe-326b-a781-d96ab7a25466 | -12.94857 | -46.28498 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a8520347-aeae-37af-9683-771d85ff0b25 | -12.67913 | -44.95869 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8663db8f-53c6-3b39-ae60-efd382607608 | -12.09284 | -43.34336 | 2025-08-22 03:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 602aa979-ad14-3273-862a-33ebd713f41c | -8.50045 | -44.74245 | 2025-08-22 03:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6129b7c-0b67-356f-b8c0-36117bd2da09 | -12.95214 | -46.29066 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50669a98-8c16-3e4a-bc2b-30234e23ffd7 | -12.98923 | -45.23296 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ee7ec41e-d234-3619-b70a-139e2e9a5435 | -10.85951 | -45.20855 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a79e96a3-4ff4-3112-a65a-62875af05d64 | -12.95721 | -46.28801 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc61b595-04b6-33e2-acc2-2279ce8b0edb | -7.8539 | -46.98887 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 127d436d-97c3-3918-8fdd-92b4498d234f | -12.43263 | -48.70383 | 2025-08-22 03:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e24b82ed-3c90-3a8f-909c-48a004f6e224 | -12.42738 | -48.70278 | 2025-08-22 03:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 681c4ca4-544f-3df0-9694-04912362803b | -8.90567 | -47.33341 | 2025-08-22 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18c2647c-ee9e-3d14-aeea-8e4a176c7f56 | -13.00089 | -45.21547 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f342f919-b541-343a-bbfe-a81f4bb3bc97 | -12.95321 | -46.27642 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff7e93e6-aa89-3808-b65a-2d920062f8b2 | -13.49603 | -47.04623 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b30e294-bcd1-38f8-bde0-c12e0616cffc | -13.37615 | -47.49656 | 2025-08-22 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba4bdec3-9309-3fba-ad4b-3630c3b4f26c | -11.11867 | -44.71761 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1986b502-6220-30a3-ba4f-42f209a28d4e | -15.08267 | -47.09747 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da9b880f-3f1a-34f2-9a56-264ad649ae9e | -13.45837 | -47.05189 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d09396d-0d8a-3851-bd53-a8f9b207c4c8 | -11.43601 | -47.3143 | 2025-08-22 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6491b527-b797-344c-9d08-62dc8bb113db | -13.39176 | -46.24973 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d40f2d69-aa23-3b0d-9123-108b1c97013b | -12.95508 | -46.27438 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e71bc1d-3fb5-3289-ae9b-dffc05c7ab7b | -9.58768 | -43.32756 | 2025-08-22 03:57:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 82256222-d216-38bc-b3f4-fe00f33d75a7 | -13.01997 | -45.17994 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bc885f7-511d-34c5-9459-51c0720a9edc | -12.00228 | -44.6671 | 2025-08-22 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c74bc5ae-f98e-351d-877f-fd8919b1f8d8 | -13.64773 | -45.71428 | 2025-08-22 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc60e965-048f-32d7-8458-6dcfbb5dbd2f | -14.76489 | -45.3915 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86e8fb8d-9c73-3f5f-950e-586638497f8c | -11.99758 | -44.67001 | 2025-08-22 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91acdf7b-dd7d-355c-8c06-d8d87b386b22 | -12.00633 | -44.66784 | 2025-08-22 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 53baaade-9d1a-37a4-bec9-71f02629db6c | -11.79103 | -48.78956 | 2025-08-22 03:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 763dfeef-9a60-3702-a797-ed0652a2c186 | -13.03298 | -45.17857 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9506d25f-ea26-3b93-ac55-77a18606511e | -13.02921 | -46.33738 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d3fc6684-4818-3f1f-a84e-2fc21bc8fdf9 | -14.72994 | -46.65693 | 2025-08-22 03:57:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c6bdeef-3bec-3cfc-9d53-bf77811d7c09 | -12.57207 | -41.27491 | 2025-08-22 03:57:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6114f2b4-f034-3213-9c61-0a3582ff4da5 | -11.27701 | -44.94943 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16ed6b70-9d85-32a8-8b6c-5388a5da13ed | -7.86107 | -46.99066 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cbcea499-74ec-3519-bcdb-a7581da4bd7e | -8.57853 | -48.55286 | 2025-08-22 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4283841-9c37-38e2-861c-e481e02ec0a7 | -9.06515 | -42.99971 | 2025-08-22 03:57:00 | NPP-375D | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6bc5a5ce-cb91-3696-8dd6-b8f65e9cee63 | -13.90787 | -43.88533 | 2025-08-22 03:57:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6e804740-424f-3171-a986-187f8c3fcb09 | -13.02487 | -45.20044 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc8f66e3-592f-3dba-98cf-e05f5e2c7108 | -15.54788 | -43.9875 | 2025-08-22 03:57:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20971017-befe-3fba-8b61-cc52a997d943 | -12.01039 | -44.66857 | 2025-08-22 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e9c75370-f7a4-3fd6-a346-e181ba2751e4 | -11.31245 | -44.94398 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7982aa4-c467-39b5-8bd1-22ba9c9bea05 | -9.13591 | -46.38684 | 2025-08-22 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 105373c6-da74-3280-8fd5-a5667feb72f5 | -12.95288 | -46.28659 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12f0f9ba-32cf-3e22-9c6a-4d3078b74670 | -12.94933 | -39.55833 | 2025-08-22 03:57:00 | NPP-375D | ELÍSIO MEDRADO | BAHIA | Brasil | 2910305 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f2c9e57-045d-3e86-8656-fd47f4f20958 | -10.97927 | -45.6043 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fb9430d-aa0a-3c52-95c9-a367dd9963f2 | -10.73217 | -48.23565 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 172f6dc5-e4d2-33d5-b58d-f57868901331 | -12.5867 | -47.09035 | 2025-08-22 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cc3a56e-20bb-3ae8-96eb-45499370c3c9 | -14.90989 | -49.4551 | 2025-08-22 03:57:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c006d2b-98b9-30cb-a064-9bdff7a1bd8e | -14.7656 | -45.43369 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07ea19b3-fd62-351f-85a5-669e40dd6492 | -7.58688 | -49.5727 | 2025-08-22 03:57:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dce87d51-da9c-3457-886b-c0438ecbafe3 | -13.63916 | -46.88482 | 2025-08-22 03:57:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7560716-62d9-3fd3-be42-557bba32a1ab | -13.36608 | -46.26877 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85cb9c4e-39b1-37aa-a415-1a42b7d9844e | -12.9921 | -45.2252 | 2025-08-22 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 60ebafbf-7900-395e-a3e4-4683d090a041 | -15.56045 | -50.32013 | 2025-08-22 04:00:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e91779b-3028-3924-8960-1a7e4a57dfb6 | -16.60987 | -43.36032 | 2025-08-22 04:00:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b581dd7-31e9-3ecd-9d74-7f9ac6a3b1bc | -18.93851 | -41.49032 | 2025-08-22 04:00:00 | NPP-375D | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e9e9f1d8-5f66-3fda-b318-bcdaf3bc8f55 | -20.36217 | -46.55425 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a3eba89-d9a7-3ffe-9da3-7f63d84e5a24 | -19.99107 | -46.23288 | 2025-08-22 04:00:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b49c889-bdc6-32c4-aa82-c8762a6da7fb | -20.24847 | -46.69595 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9330e999-24e7-3f72-8b2e-8c0ec58e91f7 | -16.48676 | -45.09585 | 2025-08-22 04:00:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed41d4ab-ff05-3020-a7fe-fdcc8a14ef6f | -19.73817 | -45.31628 | 2025-08-22 04:00:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bef99f5b-b37f-3a8e-9703-c25271c99c5b | -18.28668 | -45.52091 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 806d928e-c10d-38e8-a25b-56fe37a958e4 | -20.67531 | -41.41679 | 2025-08-22 04:00:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| f55a4054-66b5-3f57-b6aa-8d942c9018bb | -17.40034 | -44.2453 | 2025-08-22 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8294b877-b318-387b-9644-a7d42f1917dc | -16.7849 | -47.66047 | 2025-08-22 04:00:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fd3dd4d9-a504-3d57-ac13-d6f4b420222e | -16.48379 | -45.09006 | 2025-08-22 04:00:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc3c0836-bd5c-3d98-985a-26a2403fdb55 | -14.62002 | -54.86377 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6fe5b80-0ef9-304d-ab41-418689f85bc6 | -20.43074 | -46.50384 | 2025-08-22 04:00:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02b5134d-7eb9-3eac-9a50-305842ad670d | -17.88134 | -42.25611 | 2025-08-22 04:00:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 64ab97a4-d63f-379b-b2d3-60511e39fee6 | -18.27034 | -45.52274 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 175a2042-118e-371f-818d-d7456e3bbfd2 | -20.30328 | -46.62619 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f99a690-68be-3932-a275-6b3c4c12786f | -19.30002 | -48.92469 | 2025-08-22 04:00:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0719420-cc25-39b7-9914-53477b6137e6 | -16.284 | -48.73021 | 2025-08-22 04:00:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ca23673-ff1c-32a7-a574-4501c5d0afdf | -18.276 | -45.51353 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fa6fb26-61f8-3d30-8967-5610db2d2cec | -19.67202 | -48.98742 | 2025-08-22 04:00:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9d9eaa0-1f7f-36bd-9f64-a5173d1e0dcc | -17.60777 | -46.09395 | 2025-08-22 04:00:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2e1c5bf7-d048-33d4-a5f7-d076767bccd4 | -18.28961 | -45.52692 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81bf2ef3-9adc-3687-a9b3-b7d574f2be3c | -17.92303 | -44.48989 | 2025-08-22 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99a20e9d-ee48-3f2e-9240-9434e186de57 | -20.30629 | -46.61027 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3094ca29-5e6f-3a2b-be54-f45613244faa | -17.83294 | -44.42675 | 2025-08-22 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8740d499-cbec-36ad-a0e8-7804d664fd24 | -17.60374 | -46.09307 | 2025-08-22 04:00:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4633dc84-5092-3bcb-993a-3ba2c2435119 | -14.66664 | -54.86015 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README20.md)
