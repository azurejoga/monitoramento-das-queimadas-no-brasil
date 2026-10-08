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

## Dados Diários - Página 268

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f76c666-24a6-3416-86b1-9a0bc082f88e | -11.85521 | -43.5433 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| eeb45afd-5441-3150-9897-951a27ecff50 | -9.46051 | -44.62091 | 2026-10-08 16:18:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 491ef283-cdfe-36da-8b68-6872b3efba74 | -8.97643 | -45.93082 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f73a420c-aef1-35cd-9db6-7cc8578b385b | -9.89478 | -44.85979 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 89661ea0-2161-3b38-90bf-514fadfbda23 | -11.77365 | -44.68369 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f5b13014-4f98-32af-84e5-fcc1e4a2aa71 | -11.11726 | -45.70007 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a1c32328-bba4-32e8-a9d1-9075542bb04d | -13.34738 | -43.96872 | 2026-10-08 16:18:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 8f00f6e1-fc9d-3abd-ba36-36713c064b46 | -10.51512 | -47.31262 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 37dd9e50-8649-382b-a749-f0e57e02a11a | -11.19663 | -38.22839 | 2026-10-08 16:18:00 | NPP-375 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 691b7815-4145-3ab2-a1c8-15c8d2ba8c3b | -9.89038 | -44.86046 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ac662159-a190-3223-b202-4da0c4e91245 | -10.84897 | -47.94191 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| d50a7295-5d82-356f-8bb7-890cc47861f2 | -11.59607 | -43.66178 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6cc82201-9a5d-3655-a3a6-c30ed49b4828 | -12.18245 | -44.81433 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b76da772-7f1f-3e91-b722-b4a603cdce67 | -9.43674 | -44.6075 | 2026-10-08 16:18:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| da3a53fd-57b0-3ed0-afa1-8f7e31e2be2b | -11.35597 | -43.14602 | 2026-10-08 16:18:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 33.5 |
| fa65890f-d073-3e44-b19d-a91b831ab571 | -8.39674 | -46.92599 | 2026-10-08 16:18:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 2de75619-db2a-32cb-a483-ab8bd1bf1592 | -11.74755 | -43.64483 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f051c5b7-41da-32fe-94cd-8c09592b7d29 | -12.23314 | -44.73851 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5dc09f62-cb0d-36c5-a0e6-0f9a4e2cfce4 | -12.61868 | -47.8903 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 941db845-63cf-3f50-858d-6b5690a2e4ea | -13.39011 | -43.47811 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 0e4533f6-066d-3893-b535-9c30620574e0 | -13.02238 | -41.0499 | 2026-10-08 16:18:00 | NPP-375 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1889f7c1-04bc-3b98-b184-55b0b17c0369 | -8.95792 | -45.16175 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 69909b7c-d432-3334-979f-67c14c9281c6 | -10.68906 | -47.82736 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cb33c97c-6a68-3b10-9062-8bd73179603a | -10.90493 | -45.52888 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ea8d17bd-cca2-3199-a88c-2fd45f0f47e6 | -10.4185 | -47.26099 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1ac05ac0-eca7-3398-ba30-f4471b2c26f2 | -11.62003 | -43.65068 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6875390d-b473-312d-b58a-82e3a5fed8cb | -12.22624 | -44.76147 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 1ba34c32-63ec-3364-a92c-2914d48fe482 | -10.84939 | -47.94532 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 46358e46-aeb3-390a-97da-97536fcf73e6 | -13.66407 | -40.34804 | 2026-10-08 16:18:00 | NPP-375 | LAFAIETE COUTINHO | BAHIA | Brasil | 2918704 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4b1d7445-ddc4-3237-bf9c-93c6704be86c | -11.31131 | -44.83889 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c152259f-c80b-3ac8-91e4-c19d4549551e | -10.93234 | -45.39095 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 859c6341-4e1f-356b-868f-a06ffca9d1ea | -9.84828 | -47.84964 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| db3a71c1-b013-32a1-b617-7c15e7a73129 | -9.38865 | -47.08745 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 47b735b1-c631-336b-8602-4dcad4203ef1 | -12.17851 | -44.81958 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| da9fd336-6e87-378b-9b00-dd1be31dcdc5 | -11.24375 | -46.27921 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9c17be22-60ba-3440-a5df-ab407d12f168 | -11.84946 | -47.35685 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 058fe7fe-fabd-35b9-ab86-9b20b2f61505 | -11.39608 | -47.57154 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f1324547-489c-3a08-999e-c8462f401f48 | -9.35118 | -46.58089 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 627fef43-36ca-316a-bcd1-02d63538af5d | -12.17995 | -44.6555 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9e3dbe11-6ddc-3d87-b9c1-41b1328bc140 | -10.35867 | -42.48648 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| fb1e4e22-7480-35e2-851c-e3e2bd2f7ede | -13.02204 | -48.51645 | 2026-10-08 16:18:00 | NPP-375 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7abf5214-7a0c-3643-8beb-24fdbb490d72 | -10.84387 | -47.94601 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f0686dd7-45bf-3966-a11b-6e7cff213312 | -7.03152 | -35.20864 | 2026-10-08 16:18:00 | NPP-375 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| 4958b02d-a1ae-39cb-9f49-c4f1e4da7b09 | -14.05558 | -43.82474 | 2026-10-08 16:18:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a684e1df-704e-3742-98fd-316b059a414d | -13.15353 | -40.47404 | 2026-10-08 16:18:00 | NPP-375 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f8af703d-42eb-3129-ab9a-9118509cd48b | -9.97972 | -39.53315 | 2026-10-08 16:18:00 | NPP-375 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| c83d8785-5839-3b04-9622-a66368652e3c | -11.61638 | -43.62405 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 7e2d66a5-41a9-3967-9466-27ecac76721f | -12.21593 | -44.67542 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e08db1b0-0cf1-311c-ad27-d8f38590448c | -8.95022 | -45.17186 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| dd0ff1c1-4f8f-3c76-8cb8-8b9b9d48e8f9 | -10.49941 | -47.31309 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f41f596a-c010-3c50-bd3f-fe6e0e6e0f0b | -11.22913 | -45.24561 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 8dcffa9b-6b4f-323c-99f8-eafaffc79374 | -11.90905 | -46.56309 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 861b711e-0aaf-3fc8-9e81-903c10b6abea | -12.38099 | -44.98566 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9bcccb50-310d-360a-80f5-894ede6cb976 | -11.64612 | -43.68123 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 008a5b3a-2bff-3cdd-b1b5-db73e2ee87c1 | -11.75357 | -43.42556 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5512df8e-20af-3a69-a849-166fd2bf600f | -9.36672 | -45.94569 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 24bcf729-774b-30bc-a27c-2e393d4f11bd | -11.33791 | -46.66342 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 252f6018-aaee-37ba-8286-32215de0c88c | -11.76789 | -45.55324 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 5e0306cd-5ace-3c14-a749-fb77f11f2db5 | -10.46792 | -47.23458 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| bb67f76b-0fbf-35a7-b264-d7f199a2f8b8 | -11.08638 | -44.02047 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 30372d63-a64d-392c-8566-549482ca7408 | -12.21613 | -44.82412 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 9439ca07-8bef-3360-8dda-b1586425b795 | -9.4362 | -44.60351 | 2026-10-08 16:18:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| abe4703f-2673-35b5-8ff0-96a52a5cacac | -10.76128 | -46.5923 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| feb1479a-2d99-3a0c-b2be-c311ccab37ce | -10.87069 | -45.55874 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 59c8ea3e-be3e-3fae-ba73-f26524ebd189 | -11.64666 | -43.68533 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 931a2592-57dc-3b78-810a-157d642b3160 | -10.16388 | -44.66992 | 2026-10-08 16:18:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| eb23cf47-b43b-3182-81df-a76e0d1b963a | -13.7028 | -49.12398 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 40.1 |
| ffd7e248-15ba-39a5-92f7-36c7d532a20a | -11.59292 | -43.66993 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 72657634-a1d2-361c-bcba-f4648af2d251 | -12.03367 | -43.44284 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ba3f54b6-7626-35c0-9bde-ec322777752d | -11.97572 | -39.04709 | 2026-10-08 16:18:00 | NPP-375 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| bf2ff929-f997-3884-8bae-fb415811392b | -9.80408 | -47.81677 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5c76e5b4-3e4c-3b2c-9847-b61e3bc1167f | -11.87739 | -47.40581 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d9aa8465-cafb-37d3-8d6e-3ed74ea1f2b6 | -9.4448 | -44.60225 | 2026-10-08 16:18:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 18b9627c-ba15-369b-96eb-2a8fe79d78e6 | -10.50382 | -47.30585 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 87e747d2-76d8-3678-9cfe-02532ccb73ed | -9.12809 | -45.83636 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0251f75c-0c52-31ec-91f1-7252215cc9c6 | -9.73418 | -46.9444 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 953e1a28-e97e-3e1f-8423-762f2069b69d | -8.29436 | -45.39917 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 55347df3-82a0-32dd-a615-a0f0cb37ef19 | -9.94345 | -43.56866 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 56dcd56f-fdd7-3ee9-8ab6-074941716494 | -11.40867 | -46.68916 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3b7d65db-26c3-3849-a991-ae5695d78226 | -9.82679 | -47.46416 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 87e7a118-a53c-3ebf-ab2a-1049236624af | -13.97739 | -44.83263 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 05dee78f-1c2b-3c8b-8022-b349bb907cd1 | -7.69576 | -35.22699 | 2026-10-08 16:18:00 | NPP-375 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e2bb39e7-7435-335a-bae7-7e6919ca33eb | -11.24234 | -46.26785 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4c7db13d-23ad-3861-95e8-e7b7227eb702 | -11.17864 | -47.72176 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 554eae53-24c8-3709-ab3a-aa8c0e2ce001 | -9.52004 | -45.60636 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 68b579e2-0d0d-3db6-9562-e5129b5aea12 | -8.28852 | -45.72564 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 419a601e-41a5-31f3-ab15-4daeaa81f592 | -8.94042 | -45.1586 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c95ed52e-5e4a-3f87-a1b2-51e5dcdce5a1 | -9.37067 | -45.93188 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 046bb035-3ac3-330d-95a9-7ea7ebfaec5c | -11.23879 | -46.23936 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9a8c6939-d49c-3c19-91b6-2f5610ad6827 | -11.82252 | -47.31488 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 565bb73e-df41-3171-98b1-89ade9d82e83 | -8.932 | -45.19553 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 178.5 |
| b6be02b4-59cb-38d5-84ab-27222d1c5ba3 | -9.88101 | -44.85746 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| ce7e9f04-250a-3ddd-9c84-7cef637d004c | -14.17382 | -43.66864 | 2026-10-08 16:18:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 1fc6222a-a8a2-3cb5-9677-202374d6d147 | -14.05504 | -43.82047 | 2026-10-08 16:18:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 0701c5d5-e008-3b5f-a0d1-d1285e089cff | -8.2395 | -35.83225 | 2026-10-08 16:18:00 | NPP-375 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2742d1d3-78c2-3710-887a-358757150685 | -11.09486 | -44.0193 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 53af854e-e39c-33ce-bda2-7017f923782a | -11.63879 | -43.69437 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| cca28b28-a44f-3adb-95a8-85d57defae1d | -7.61299 | -39.74854 | 2026-10-08 16:18:00 | NPP-375 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 9b4d4a22-3813-3974-a5f2-49caca439654 | -11.6357 | -43.70281 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 93741273-e5fd-37cb-a483-771d90458365 | -10.44144 | -47.2777 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |


[Clique aqui para ver as próximas entradas](README269.md)
