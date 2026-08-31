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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e20cde13-01f1-3dba-ba81-01b326f699e6 | -10.54465 | -46.20605 | 2026-08-31 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92b767f9-e545-3122-bb30-9acfbd95994e | -16.28038 | -42.56779 | 2026-08-31 03:55:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22a44146-5cf6-3157-a12d-3e3469123b55 | -11.32763 | -45.18935 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f11dc44d-1d37-31a1-86ca-c596cf2928ae | -11.49968 | -50.32937 | 2026-08-31 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a39541d0-7798-38c0-b0c8-df8d10245ede | -17.52619 | -40.23869 | 2026-08-31 03:55:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e438fa09-60c6-3676-937a-a9d87a70a2ad | -11.33172 | -45.16784 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 862947b2-4eeb-35a9-abf3-209992bbe7ec | -12.10747 | -45.03716 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d737eb40-d3e5-3f1d-ad1b-94d442f66b45 | -10.73125 | -50.64901 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6776236c-7b93-3150-b1c5-dcc583e919ee | -12.09858 | -45.05629 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45f2fda0-2719-3474-a6bd-6c9b4ff5fd24 | -9.43387 | -45.66898 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9fb09f6-39a8-3c68-a344-89f39895e94a | -10.83546 | -45.3158 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 118d2dbd-3dcd-3c6e-961c-2706e8b3f356 | -15.2037 | -46.23264 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d1952f1-2ed3-3372-9625-b70755ae470d | -10.83434 | -45.31527 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4fb2773-30df-36f5-9b16-329af6e58e39 | -11.92765 | -45.06775 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3a4b12b-e602-36a5-a8b7-f9e9fa225fae | -15.02633 | -48.16978 | 2026-08-31 03:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3179d70b-4dde-3ba0-90fb-7bce7a6cf56b | -12.0755 | -44.99202 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1491c38a-0e93-3762-aa11-c83e8211c947 | -14.19135 | -45.30851 | 2026-08-31 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe909dcf-b989-3db5-a9c4-9a0e2ddc5fb8 | -10.73359 | -44.88129 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3143588-2665-37af-b4f3-cc26e054dcd5 | -12.41967 | -42.88546 | 2026-08-31 03:55:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d6d80aef-fc51-3d49-8db0-876f6577ccea | -15.19217 | -46.23671 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02813521-6367-3cd3-9083-9b8e33c8610b | -11.34485 | -45.21126 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 6b5aa89f-d792-3504-8a95-248a7f5780c0 | -16.28343 | -42.57365 | 2026-08-31 03:55:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16985c4e-42ae-3db7-96ba-14af31a1742d | -11.35912 | -45.22071 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccb9941c-6fc1-3173-b730-d525d776bb68 | -12.9417 | -45.91694 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abdfe254-40e9-3a01-b202-0090b18dabf7 | -9.43797 | -45.67753 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f10bb5d-0fd7-31a0-b10b-d39df1ffc931 | -11.36316 | -45.19919 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e09f66dd-6763-36b3-a7d2-115ce84123bf | -12.89796 | -45.83997 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c4fc95a-ce7c-30bd-a1e1-9ecee479e58f | -11.32594 | -45.17017 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c47c339-cd8b-3d42-8e11-45c9fdfe08a9 | -11.79346 | -47.66998 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e204a04-76dc-3fe4-8096-1235b02512f4 | -10.73998 | -50.64321 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 303b7796-0af6-3123-8148-5b57fa72566f | -11.22549 | -45.10474 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8270ffb0-5a68-367b-a172-077fb97ff382 | -10.73721 | -47.96482 | 2026-08-31 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 37b4bde2-ea65-36e3-a947-56e7532992cc | -11.21803 | -45.08812 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7ee0750-df36-3464-8bc5-e27e53bd2629 | -11.36427 | -45.22175 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 891f396c-28fd-360e-be99-d2d1e09d75e1 | -15.19136 | -46.23644 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80e9d0b8-9f4a-3d35-9e6b-4144a4a3c61b | -10.82148 | -50.69175 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a6d3d5bf-cb74-3c8e-b6b7-1c4c85d9ab3c | -12.08116 | -44.98953 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e004a00-1db4-3008-873e-a76f4f800212 | -10.73396 | -50.64126 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9d8dfa78-448b-3f7b-851b-da12af0e3f2d | -10.1519 | -45.70368 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37e66817-173c-3ae6-b8d8-9a9c9a0953a1 | -12.13573 | -45.83904 | 2026-08-31 03:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8be28bcd-6463-3582-ad61-3ca1550eea81 | -10.15743 | -45.73406 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da566cdd-d0e2-37b7-813a-635bec13eb9a | -12.95361 | -45.93998 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 229a0605-4b1f-3f77-b51f-6b06c4488b2f | -11.36546 | -45.18696 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 651bf905-d977-3d31-8a56-48eb11bbfa3b | -12.10804 | -45.0342 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0a125ba-a788-3da4-a1b7-5ab956a4d429 | -15.63234 | -50.08965 | 2026-08-31 03:55:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 638929fc-4e78-346e-b83d-3974c361be7b | -11.36951 | -45.16534 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ac95273-e2ed-31dc-a5dc-67ba40f64843 | -11.362 | -45.23388 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a1f6110-2a07-3f63-aa82-975cf310dbf1 | -11.32876 | -45.18344 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8ce58f2-7eda-3a3a-9fbc-63f33e73013c | -10.15811 | -45.73048 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 106989ca-9bb9-3c21-8a15-7507b9425613 | -9.4202 | -45.65078 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06c0819b-9859-3e32-9f5f-0c301fd3a00d | -10.15259 | -45.70007 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cc83ebc-3c91-3225-9466-fe01cb28dc8a | -10.1471 | -45.75877 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0f2b9c44-3a14-3c20-aad9-05f377e4b10f | -12.91746 | -45.90147 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e70a9b4-e48c-3dc1-ba85-4e254d43fd40 | -9.58251 | -47.60909 | 2026-08-31 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbbfdcab-f15b-35e2-ac42-fec6773b5c35 | -14.19562 | -46.56715 | 2026-08-31 03:55:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ab3d66a-99d3-37dc-9933-6aa299bb10b5 | -11.37178 | -45.21019 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7492e8bf-8e3c-30a9-a634-93faeaba6f3c | -11.15443 | -45.04916 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a51fad72-bac4-368f-8013-2144e8e9c287 | -15.1909 | -46.24296 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3da1d94b-9ca9-376b-bea6-87315012893c | -16.98956 | -40.93764 | 2026-08-31 03:55:00 | NPP-375D | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 42625a2e-92f3-3999-8bc4-5d6818d831e4 | -12.92119 | -45.85468 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca8f039d-35b5-39c4-a08d-ccfae317086e | -11.49244 | -46.93459 | 2026-08-31 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbd33565-b608-3c39-a903-8532605b03a2 | -11.67742 | -47.61821 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f2f44e6-ab85-3108-8fd7-ba67dd478e24 | -10.54816 | -46.20646 | 2026-08-31 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5282466-bd02-3dfb-a4ce-327812859a31 | -14.19992 | -44.58868 | 2026-08-31 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51dbb508-1d7c-30bd-9fe6-661132ca2fed | -11.93015 | -45.05447 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14ad1800-2f64-3e0f-94dd-82da23deab9f | -9.58156 | -47.61399 | 2026-08-31 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c844165a-f169-328b-bba8-c2a3438c0012 | -15.66763 | -45.92747 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e616b31e-fb24-34f4-8df7-a2b70b0fca82 | -11.35343 | -45.2225 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d3ae54d-d7d9-397b-a425-84d2e17091f1 | -11.36543 | -45.2156 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6fca831-d965-3f0f-b1c4-4c4ffa94b7f4 | -16.27744 | -42.58393 | 2026-08-31 03:55:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55d15727-7425-3b5c-87c3-4309c2db5992 | -11.33678 | -45.19744 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc3a887c-68b9-3f70-be2a-784fc8e214e1 | -17.24646 | -42.80337 | 2026-08-31 03:55:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9353187d-399e-3af6-b8d3-102e5a1c92c9 | -13.38826 | -41.33026 | 2026-08-31 03:55:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| e5f1d1ed-4850-37da-9c4a-1f6b3d5d99a2 | -11.67858 | -47.61252 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dceaba5f-5f5d-3be9-a7d0-8839b1a6ae73 | -14.19729 | -45.30416 | 2026-08-31 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67eb0464-1124-32d2-b41a-52a08884870c | -11.33877 | -45.15883 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fc957b4-9fea-3af3-ac15-14641728d2da | -12.14032 | -47.258 | 2026-08-31 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b2c2b4b-2852-310f-84da-b0008d6fe17a | -11.7912 | -47.67191 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b086712-4da2-37e0-b06d-ff1f827b6744 | -11.36374 | -45.19609 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7955b7c-129e-3a0f-b4c8-64fd9b522704 | -10.75579 | -44.87561 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46392c46-e9c0-303f-9381-c91329550665 | -11.22492 | -45.10775 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64ebc530-b957-3a15-822d-2726d90ddca6 | -11.2097 | -43.38142 | 2026-08-31 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 75bf76d0-2e16-38e9-b8a2-9ed9ce2ad972 | -11.68923 | -47.62136 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f0e02a7e-b3cc-35f3-91f3-446ad34f12b8 | -11.37643 | -45.21388 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f07c68e6-65d0-3dfd-8024-f06a3079d548 | -10.83497 | -45.31205 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96b72a25-b4b4-3917-ba44-67ac3164a764 | -9.80581 | -46.45121 | 2026-08-31 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36d60925-f660-3e45-b498-641005d12c21 | -16.28647 | -42.57965 | 2026-08-31 03:55:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2aa4afc-3a2d-33ae-8898-298e43684a4a | -17.24865 | -42.80102 | 2026-08-31 03:55:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b465a5e-381a-3346-806a-c0c3693df9e2 | -11.36658 | -45.20942 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 136b160b-01d4-3293-8d44-d65362d38147 | -11.21058 | -45.0992 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8901029-900b-3486-9be8-a0e8399fce98 | -12.91683 | -45.9047 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cbb02d0e-cdbc-3916-bda6-c93437b90b97 | -11.6784 | -47.60546 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe03e8c9-0183-3036-a0af-262338727fa3 | -11.354 | -45.21951 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d6b7ca4-7361-3b78-9755-4acb5b344bbc | -11.19536 | -45.06775 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26d03fad-db3c-3731-85ae-c58804684592 | -10.823 | -50.68613 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ee18516-e821-31f5-9143-bf58f1c98ce6 | -14.20026 | -46.5718 | 2026-08-31 03:55:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9062c47a-a24c-3099-95ab-7977de1684db | -11.34942 | -45.21542 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5fb898e5-5a7e-3785-b96c-f84d13e39bb8 | -10.74889 | -44.88424 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60499772-234f-3d14-9b35-2c242310a654 | -11.21272 | -45.11586 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7285284-4e3e-3631-9735-3611373d18d6 | -11.35625 | -45.20755 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README21.md)
