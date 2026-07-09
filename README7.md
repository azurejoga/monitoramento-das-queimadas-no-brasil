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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c3add5a-244b-380d-91b5-2ba58cca3362 | -15.96095 | -47.76349 | 2026-07-09 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 603adbb3-57c4-36b1-9404-2e7b57b5a92a | -17.96176 | -42.85405 | 2026-07-09 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d45a09e1-7610-36ca-9584-a112d4029013 | -12.92665 | -49.48171 | 2026-07-09 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ab8424b-19c1-32cd-8035-061ffdda6165 | -12.63887 | -44.64479 | 2026-07-09 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c69b763a-73ee-3b73-8878-460cce0eb65a | -14.44369 | -48.75728 | 2026-07-09 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab017e5f-d143-3c01-98aa-fdd342f3b6d4 | -11.83641 | -48.24024 | 2026-07-09 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7164999-996f-3442-8cd7-8d59fdca21fc | -12.75893 | -44.53534 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca06d5d0-866e-3cb9-a7da-b4b3df8b1044 | -12.35545 | -47.42263 | 2026-07-09 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3542b9b3-cc5f-3756-8055-b05a257ab434 | -12.84697 | -44.36008 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 208d0a7f-cbb4-33cc-8444-67763482917c | -17.58909 | -44.49415 | 2026-07-09 04:08:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02f09210-9f3b-3115-b668-cb6fd6f53042 | -14.44456 | -48.75258 | 2026-07-09 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4536c127-6ef8-3a73-8fe5-4ca7e4326ac5 | -13.76366 | -46.27224 | 2026-07-09 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1291bbb-3d64-3f20-8112-ac993646d64f | -17.26115 | -48.28519 | 2026-07-09 04:08:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9560ffbd-d920-3081-9a9a-63613ee7e80a | -11.99053 | -45.14014 | 2026-07-09 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bfaf3b2-bdd6-368e-bb8d-4b9b39d7aca3 | -13.76783 | -46.29375 | 2026-07-09 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23f92e63-8a6b-308f-8d1a-ac8776372ba2 | -13.31196 | -43.7127 | 2026-07-09 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc967dc8-d201-3562-a085-018ab507e23a | -17.96506 | -42.85462 | 2026-07-09 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73f61d97-c005-39b0-8852-021479a291ff | -12.83351 | -44.35352 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51122de8-425c-3b62-9299-bbc24a1b70e8 | -14.44146 | -46.44962 | 2026-07-09 04:08:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70b538f8-b212-390e-b5a1-c401e275915b | -13.75536 | -46.29649 | 2026-07-09 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5ce8398-ff7d-3fff-9645-25563a13497a | -13.07453 | -48.17086 | 2026-07-09 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a93c4f3-d324-3b36-9b30-59075ed6c182 | -14.62981 | -42.52427 | 2026-07-09 04:08:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c4fbb2dd-ad0d-3e80-ae9f-24dde3f88634 | -12.17499 | -43.45637 | 2026-07-09 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b4b4c5c-9551-3d13-ae5a-67185e8805d2 | -14.62708 | -42.52013 | 2026-07-09 04:08:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ef1c475a-a3d9-3b5d-934d-5252b5f10232 | -12.92969 | -49.48373 | 2026-07-09 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 264ed092-e5b7-3d72-ad6e-68cc94962cf7 | -14.91118 | -43.42814 | 2026-07-09 04:08:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 14.4 |
| d4e3b334-5e30-365a-9580-f7b3ccd3122b | -16.71885 | -50.70721 | 2026-07-09 04:08:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3cde2d7-b4d0-3a36-a9ce-00ba30a509d2 | -13.27487 | -45.18203 | 2026-07-09 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39a46de9-c5d5-38c4-ac1f-82bf74f00e77 | -12.75537 | -44.53469 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9b5c28a1-af82-368b-8fd4-52bab12341b6 | -12.82997 | -44.35291 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d840c546-4c4b-3c72-8a56-7f5e1a936bcd | -13.47935 | -49.92657 | 2026-07-09 04:08:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f54a9879-8221-33b1-9611-c1ffd3d305ee | -15.24582 | -47.41592 | 2026-07-09 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b0a7b75-bd53-3834-8a40-c422cc0ea935 | -12.75607 | -44.53055 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9d19843f-566d-3394-9d91-6f99cbf87dfd | -12.84138 | -44.37173 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e60a608-372e-34c0-99f0-1764de5733ff | -12.93147 | -49.4827 | 2026-07-09 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 976ff1a5-a22f-3331-83af-9cc27dca809a | -12.84833 | -44.35191 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aa908cc-74db-3a19-bae6-ae17d506266c | -12.34697 | -47.42098 | 2026-07-09 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afa2a3d7-a0e5-36f3-91b8-ec09d8919a56 | -14.92128 | -43.42989 | 2026-07-09 04:08:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 86734477-bde1-3e12-a870-239e3baba2c1 | -10.80621 | -49.64806 | 2026-07-09 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39f88332-be06-3a18-ad6d-3ddcb8a2d80b | -13.77081 | -46.29945 | 2026-07-09 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f943189-9ea8-33fd-bd35-ec434953f65d | -12.84914 | -44.36887 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5aba3ce4-f68b-30a4-bd5c-19356edac782 | -14.4376 | -46.44887 | 2026-07-09 04:08:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 122964d7-05dd-3565-b008-f517c746ff5b | -11.83766 | -48.23785 | 2026-07-09 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5d04fe0-fc8a-3f23-bfbc-ea17b46c5299 | -11.64748 | -46.35674 | 2026-07-09 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cba50f29-5194-3be4-97c5-d57e393b46e9 | -12.35619 | -47.41859 | 2026-07-09 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c661019-1ad3-3a96-8d5f-02e26c8c06a2 | -18.53359 | -42.30334 | 2026-07-09 04:08:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7e623ffe-578f-3c01-95f6-5eee78436531 | -15.25592 | -43.1076 | 2026-07-09 04:08:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d2513d86-5dde-31d5-83ef-cfe9b94eca88 | -13.27565 | -45.17762 | 2026-07-09 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7001d406-8b51-30b6-a6d2-2122b3d101c7 | -10.80677 | -49.64502 | 2026-07-09 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dafbd200-2b27-3b0d-8983-efafe007dc78 | -11.83678 | -48.2425 | 2026-07-09 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b05508eb-8906-31f3-9c5e-5b0686a0f2fa | -13.76607 | -46.30367 | 2026-07-09 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7af0f007-d577-34b5-a53a-8d9b80751267 | -14.91791 | -43.4293 | 2026-07-09 04:08:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 453f13f9-9ff4-3c5f-8e1f-5469e25ddad2 | -13.76695 | -46.29869 | 2026-07-09 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca3ba02d-56a3-3908-b44d-8bc6e43e0edd | -16.71584 | -50.71057 | 2026-07-09 04:08:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 967a9406-3e90-3e3d-94c2-74719e7713cc | -11.45596 | -47.58544 | 2026-07-09 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a26b12c4-8ae7-36a8-8365-552f3f8d1909 | -12.63025 | -44.65196 | 2026-07-09 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8085e5aa-a8d9-3b36-8633-712d906a9e1c | -10.64251 | -50.09355 | 2026-07-09 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e78bb81-6c2d-3553-9de5-72177a49031c | -17.39984 | -47.3254 | 2026-07-09 04:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84b40e6c-3ad6-38c6-8033-fce2d4c8baa2 | -12.35195 | -47.41776 | 2026-07-09 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d920509a-368f-3575-ba5f-df65e95372c1 | -11.85859 | -48.03951 | 2026-07-09 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16965c97-8769-3338-b33a-457dfb190fff | -12.26976 | -43.51914 | 2026-07-09 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a81b23b-2970-3014-a22d-1fd687cb5305 | -11.65424 | -46.36528 | 2026-07-09 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bbaba8b-0028-3fee-ae78-7231a2a318c5 | -16.71769 | -50.71293 | 2026-07-09 04:08:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9f2e6599-53dd-3e88-b1eb-33d836627208 | -12.83283 | -44.3576 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ea2c4e7b-7d18-349a-bba3-76216ba08b5f | -12.67148 | -48.22171 | 2026-07-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ad7e2f9-e47e-3e40-a583-0bfda4253356 | -12.83922 | -44.36292 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 80934ea5-9772-32e4-8976-5ff222b57e38 | -14.43839 | -48.76087 | 2026-07-09 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f4b2566-1cc9-3dfe-99d7-a86cc1a44ba4 | -14.91455 | -43.42872 | 2026-07-09 04:08:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 6040dc1b-6c82-315c-83dd-341c2c8edbc3 | -21.4745 | -54.4769 | 2026-07-09 04:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 9ef09cab-0bc0-3b94-81a6-9061d2cf6c53 | -21.454 | -54.4805 | 2026-07-09 04:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 98b0b5da-6de6-3bdf-86b1-5519b03e4af4 | -7.7056 | -45.171 | 2026-07-09 04:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ca954ba0-ca56-3629-9e0a-123f1949ccd6 | -21.17805 | -44.70456 | 2026-07-09 04:10:00 | NOAA-20 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5b378039-21e5-3ade-bff9-7c3478553448 | -21.46765 | -54.48471 | 2026-07-09 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dbb956f4-3e0a-363c-abc2-69790db3b67e | -21.46859 | -54.48059 | 2026-07-09 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e72a7b88-183b-348d-9904-b02ca6a99172 | -21.89144 | -44.45508 | 2026-07-09 04:10:00 | NOAA-20 | SERITINGA | MINAS GERAIS | Brasil | 3166402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a895060-2237-3502-8c32-4c052bafa061 | -21.28695 | -47.80034 | 2026-07-09 04:10:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35361b85-f8aa-3c2e-8799-43a0c7e5664d | -21.76966 | -56.28859 | 2026-07-09 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3c8bec0-173c-34e6-aff0-448b40200e8d | -21.20531 | -49.21369 | 2026-07-09 04:10:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 80c54901-3ffb-33ed-b324-7caf97d3fc1e | -21.79766 | -56.27232 | 2026-07-09 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07c80708-8aee-3b01-b42c-27734493e36d | -23.81691 | -48.71154 | 2026-07-09 04:10:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 111cec9e-265d-30ce-b8ce-640de6c75880 | -19.85364 | -49.07167 | 2026-07-09 04:10:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fee41af8-930e-3908-b737-42029da28764 | -21.46494 | -54.48563 | 2026-07-09 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b806715a-fbcb-3f70-90ea-6e9c17dc1311 | -21.76838 | -56.29397 | 2026-07-09 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b23a2aaf-7f48-3437-ac66-58115f1ead1e | -21.88541 | -44.45012 | 2026-07-09 04:10:00 | NOAA-20 | SERITINGA | MINAS GERAIS | Brasil | 3166402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b089fc47-8e22-390a-9ca4-a76745e10067 | -20.66809 | -48.68127 | 2026-07-09 04:10:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 458058de-a123-3636-b061-2e33a1225613 | -22.28658 | -46.86079 | 2026-07-09 04:10:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d63b809f-7362-3125-b2c7-74ea264d5540 | -21.46586 | -54.4815 | 2026-07-09 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a84a087-31c1-3465-88a6-6fbd3cb67cbd | -21.89205 | -44.45135 | 2026-07-09 04:10:00 | NOAA-20 | SERITINGA | MINAS GERAIS | Brasil | 3166402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1eed6dfa-6613-3014-b867-a5215b6c7fbb | -21.46207 | -54.48323 | 2026-07-09 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad3f9ab5-d056-3bb5-b279-a6821bbca705 | -21.79292 | -56.2733 | 2026-07-09 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6800780-4487-3e0b-b874-c27576288e6c | -20.66741 | -48.68491 | 2026-07-09 04:10:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e47c901-21a3-30a8-b084-e2f87a8e6fcf | -23.8207 | -48.71236 | 2026-07-09 04:10:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9665e45c-b068-30fc-b5f8-0a29c46e66f8 | -21.46302 | -54.4791 | 2026-07-09 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6f4113e-93dd-39a7-afb7-d52c3312d460 | -21.74626 | -47.71601 | 2026-07-09 04:10:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97c8a1d6-7198-3f3d-ae0e-5145d2c52f31 | -22.92202 | -49.20367 | 2026-07-09 04:10:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1e85c3c-315e-35f2-9018-1e41f010f039 | -21.35276 | -51.04059 | 2026-07-09 04:10:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52d378e0-5c4f-3525-9153-bbcd3c31f000 | -21.28607 | -47.80521 | 2026-07-09 04:10:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7039966-a964-30f7-8738-91ea94916a97 | -19.49741 | -44.80316 | 2026-07-09 04:10:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8605deef-65a1-3bf9-99b5-b32463fb150e | -23.56311 | -47.51009 | 2026-07-09 04:10:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9970f807-200d-3264-bbaf-ab9fb22ccfde | -21.79893 | -56.2671 | 2026-07-09 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
