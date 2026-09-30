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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8b483ee-f0e1-3fc2-8a77-f491d5693e89 | -13.38011 | -44.0173 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e44c0dd4-bd6c-34cd-8ee8-6db90a3afe3e | -11.80068 | -50.45058 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 84e516d2-7ae5-32b6-b264-25c6e45d804b | -18.23612 | -53.02737 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1be0ceed-4f10-370f-a5b2-674689cd081d | -18.28361 | -53.04655 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c5075fd-9bb4-3f31-b39b-f723d9ebb41b | -18.28083 | -53.0423 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 537998cb-84e9-3d21-a6fc-77e7ae02d964 | -18.48877 | -45.13309 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1c47eaf-deaf-3a93-819c-5482e49164a2 | -13.3279 | -43.96111 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72ffa815-26d0-325f-b46d-a3b08a9a30a9 | -16.86175 | -54.93409 | 2026-09-30 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3ee9a80-6c68-387b-b150-4112d1c93536 | -11.39921 | -50.97861 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88b65806-25c5-30ed-b92d-8d506cccfb81 | -11.79534 | -50.4433 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9ee9a2ea-5abf-3050-930c-20b148d2fbef | -11.36952 | -51.02604 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a5ffcc9-b8a7-36b8-81b6-fee8aca6b283 | -11.79191 | -50.44277 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a810e52c-4df0-3bfe-9829-e7464272210f | -19.21669 | -44.75789 | 2026-09-30 04:55:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0453157c-3313-3718-a37f-eda7f88635de | -11.79838 | -50.44246 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c41f4585-2d26-32d8-ac50-8688b5158f87 | -12.62899 | -47.24439 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1041c473-38eb-39cb-9e59-9a968d6598c0 | -20.5085 | -49.63042 | 2026-09-30 04:55:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f03c518f-0da9-3497-9b2a-01e7314cd8bf | -18.88643 | -43.81719 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cbc0282-3016-320b-a1c6-67412bb272cf | -11.37962 | -51.00531 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 156b2e9c-f6f3-3e87-9fed-36724ba8a0d4 | -13.33267 | -43.96499 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75e8fc1e-d553-30c7-bd48-0f49db0a1f17 | -9.784 | -59.01986 | 2026-09-30 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2457e8be-8f0a-391d-b4d9-53f871b6dad2 | -18.89523 | -43.80991 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8c39d73-a335-3d7d-bf52-ceb06fdc6b48 | -18.50898 | -45.13862 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf7e1682-61bf-360b-8155-463604a3f3d9 | -11.8184 | -50.42614 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 181ca7cf-a904-3730-9355-43565d928c10 | -11.81614 | -50.46464 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a82a4d40-d92c-325e-98bb-aa04e1699d48 | -11.39695 | -50.97079 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49ec9a05-bd81-320d-a457-2ed15851c6ff | -12.78469 | -54.0054 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d1eb834-75e8-3594-b0bc-92d82539dc21 | -12.62835 | -48.36037 | 2026-09-30 04:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aeabab98-c0cd-31e2-a8a3-89e1525fbb70 | -11.38469 | -50.9726 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2cb4f5a8-22c8-3f16-a640-ce402f98077e | -11.81783 | -50.42994 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9d09ae7-9783-3487-9e21-6f194eb0f2dd | -12.78409 | -54.00903 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a61081eb-07b3-3de8-a2ad-7a08efd8adee | -11.82358 | -50.46191 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6d604db-9c48-3ab2-b58a-11d5e95cbbea | -14.01093 | -42.91414 | 2026-09-30 04:55:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| cc77fa38-c1c3-3937-9a39-c977f0334a92 | -11.79994 | -50.43625 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8012812-c9b0-32d4-9629-2a9889ed6dca | -12.44133 | -44.16653 | 2026-09-30 04:55:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2353f371-4cdb-3b9d-a54f-df409c64f5eb | -18.51342 | -46.27235 | 2026-09-30 04:55:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a14b6ddf-175d-3cea-84d4-7154243e8a1c | -18.88335 | -43.81448 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72e1b5bc-c7cc-32e5-8aa5-04048b326625 | -18.89292 | -43.80915 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c2b8128d-6f62-3481-a5d3-01b6c873d8f9 | -18.29028 | -53.04768 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5fa72883-bab9-3167-a452-d4caff2bc8a3 | -13.06587 | -43.27997 | 2026-09-30 04:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3caa49f4-43e6-33bf-8194-3151f6017eab | -13.54297 | -49.17132 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2052f5a9-dbfb-3715-aef3-b15bc4c5d8f6 | -11.8356 | -50.47542 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c49e08cb-e62d-37bb-8b52-c9df8a63aa45 | -18.23499 | -53.03474 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d4cf956-3072-39c0-af58-eb7afac25c04 | -14.20149 | -42.07615 | 2026-09-30 04:55:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 4b943cc5-01fd-3c4b-8427-52b41fded36f | -12.74788 | -54.05202 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3d609d3-6fe0-3482-b516-e94ce0261a10 | -11.85129 | -50.97352 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 180c3d8a-5188-3ea2-94d9-65276d8108de | -19.6294 | -46.91566 | 2026-09-30 04:55:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4733412d-44dd-3255-b786-27d1cba70246 | -11.40092 | -50.99007 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6643fd07-90e7-3a61-8749-c4440fa8d4ad | -11.85634 | -50.96304 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80d64ba4-f367-3293-9503-790e37d4c367 | -11.35268 | -50.97873 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a553d665-a109-326d-acc1-ec370d06965d | -11.83944 | -50.96039 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d400695e-df29-3ef9-925f-d374928ac101 | -18.49321 | -45.13988 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23124efe-cc85-3dc6-a10f-e0123136f944 | -12.06756 | -46.46249 | 2026-09-30 04:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a37d60ff-8b46-30d0-a8f9-bca966d0f327 | -11.83274 | -50.4711 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a4b51dd0-d1e7-3b86-8caf-ee3b0b4c8cac | -14.11894 | -46.26232 | 2026-09-30 04:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39804d68-d408-3e8e-98c8-c6d20f28abf7 | -11.31451 | -50.98018 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ac7c3a7-60e9-35c8-b8a4-28b4e4e03b08 | -11.85185 | -50.96985 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7974019f-b43c-31c2-b310-3db67fa78eef | -12.78252 | -53.99755 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c9d60c0-7be7-3704-8976-99e7ddfc690d | -13.53493 | -49.17459 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f33b178-473c-3eb3-ad82-612e5b8891c8 | -11.84509 | -50.96879 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25392472-1a6f-305d-b599-15b9ac35b6f8 | -11.34706 | -50.97039 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06a687cb-0703-345c-b64a-28b261ef4155 | -13.54105 | -49.18476 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad8d9e14-65d6-34ff-839c-9d007a298d53 | -20.49666 | -49.62881 | 2026-09-30 04:55:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ff8ea4d-a994-3aed-9849-0a050eb9af5c | -11.37737 | -51.01984 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3778d20-c4e4-309d-bad3-8255091a8526 | -18.49802 | -45.14341 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a251d682-5056-355f-946e-bc8ba2e8ff80 | -13.54166 | -49.18048 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d00df1e1-e421-37ca-904e-edc450a26e68 | -18.48808 | -45.13925 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1592442-7eb2-36bf-a2dd-4bbb4c66ee58 | -10.06682 | -63.08694 | 2026-09-30 04:55:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ed58bd6-d4e9-39c5-82e3-74ccfb308949 | -11.32125 | -50.98123 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35f7f34a-384d-3ff4-ac21-4362612a1c95 | -11.32299 | -51.03727 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2c31b3d-703b-3e07-9653-5f18da925908 | -12.47565 | -47.48458 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10517bdf-3b9e-35ca-9463-cc7dfde8a32c | -20.50525 | -49.62457 | 2026-09-30 04:55:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ad233eb1-6bb1-3b7c-a266-d7ba4b6909df | -13.38394 | -46.82529 | 2026-09-30 04:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d5a708d-19f7-35d2-a8e2-cea9c783edf5 | -11.84565 | -50.96512 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaf35572-0dca-3b37-8463-f67bad4890af | -12.78745 | -54.00961 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c09f734c-6992-33dd-83ab-733146e37ecc | -11.34036 | -51.0363 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 908dc6a8-fc94-3094-ba31-2457d93f86d9 | -18.88607 | -43.82076 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14f48501-0f6c-333f-971d-441e907bd4e4 | -11.35998 | -50.97617 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 300efec4-bbca-3eac-ac2b-6f9b8aad8c50 | -11.38806 | -50.97312 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8e0e5ae4-1e45-3e13-81d8-ba1bab280e78 | -11.39533 | -51.00408 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1cfcac46-c4b7-33ad-99d2-60db79ffe0dc | -11.80355 | -50.45491 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0840f279-cfbc-3ed5-b739-aa10fcbf5ff5 | -21.38272 | -45.31607 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 83bf104b-58ab-3836-a028-b0ae4740a7eb | -11.35494 | -51.03117 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8af469c5-34c5-35d0-ad79-80e52a7e0546 | -11.30049 | -50.98168 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d5a12d4c-fefe-3380-8684-cd2e44e0144c | -11.37008 | -51.02241 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0da8f2cc-e30f-30c0-a165-b77cb1950b09 | -18.49286 | -45.14299 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| debda460-1f9a-3edd-9a38-266937af63e6 | -11.80125 | -50.44678 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cfbc1db6-6ae1-35c2-80f2-aaf65f5ffb4f | -12.77618 | -54.01518 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9de50406-8e59-3bb9-b007-016b1cf4477a | -18.51242 | -46.27565 | 2026-09-30 04:55:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2797c7d2-d510-3c90-9308-ba8f0d3392fa | -11.81885 | -46.89822 | 2026-09-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ed53400-b9e0-3f8c-a805-c0c90799d0d4 | -11.82757 | -50.43534 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db94dc2d-ad9a-386d-aafa-0a587f35cd82 | -12.76854 | -47.2565 | 2026-09-30 04:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9684f0aa-d17f-3107-abf4-bd10bd5a88a5 | -11.80582 | -50.43974 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb322c3f-a5f5-30b1-9682-ef874201c680 | -12.07727 | -46.4554 | 2026-09-30 04:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20d062d3-a398-3d7e-b165-9f2b0d91aaba | -13.32271 | -43.96041 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9effdba4-be42-3fa2-ac71-ff1ee7b45da5 | -12.03102 | -47.81139 | 2026-09-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a931007-6ff5-3753-908f-06de8fc7d859 | -11.38412 | -50.97623 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94646846-e16a-3b1b-8cb7-7fa210ee3f52 | -18.24746 | -53.0367 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fc122fb-66fc-3b9f-8050-fce88f56eefe | -19.96846 | -47.90474 | 2026-09-30 04:55:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fa567d3a-ffe9-3063-b3b6-568f0f8670a8 | -11.34373 | -51.03683 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 247b1c7a-c06d-300d-891b-dbe32c33e9a3 | -21.38241 | -45.31666 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |


[Clique aqui para ver as próximas entradas](README56.md)
