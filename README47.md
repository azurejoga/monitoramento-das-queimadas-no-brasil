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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c9b0983-4f71-3475-9578-fb9499a62ef6 | -11.91683 | -50.51019 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ded35ec-1ad4-3de4-b991-b50838ed4cdb | -10.42391 | -53.79023 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95068e12-15f1-3c4d-994f-085706e717ee | -12.47529 | -47.48596 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d69a69b8-7458-31c0-992e-fc652bde29d9 | -10.02603 | -50.13946 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18f086af-727f-3726-a721-c595a45f6b45 | -12.70529 | -47.32286 | 2026-09-27 05:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9498f01d-b60f-3408-8c21-344d3bc513dc | -9.64195 | -55.13645 | 2026-09-27 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0006ecfd-6ae1-3bee-9928-082954fbaa6a | -11.94918 | -50.56614 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c87ec948-6149-3985-8eba-cc81bb6c2cd1 | -12.2839 | -50.28963 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0458c720-4fb8-3fde-b583-5f90bea4fa38 | -10.31045 | -54.264 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5689ba82-1735-38b0-90f0-09bbf562cf43 | -11.87783 | -50.50983 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 40d8539a-489c-3124-8c0f-cedb05c0251b | -10.11364 | -50.198 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9922c2f8-2f70-3843-823d-5902e1f7e5f8 | -14.1174 | -46.33097 | 2026-09-27 05:29:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fa6068d-749e-3cb3-b6ce-b92d269ec243 | -6.87634 | -55.55522 | 2026-09-27 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38dd1f19-5041-323a-8ef6-b824eb8a284f | -8.33893 | -62.85995 | 2026-09-27 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bdaa6ee-f95c-3741-8786-42d2c2689dfe | -13.37933 | -51.32039 | 2026-09-27 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1015cf96-a8f2-377d-8e5c-e466e50697c3 | -10.04059 | -53.77834 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaebfb5d-2592-32f7-a2cb-a4d2f4b43a3d | -9.07655 | -66.10014 | 2026-09-27 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98ebc27a-b785-3c21-8875-d77c58a4f83d | -8.83774 | -62.3921 | 2026-09-27 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3c1b13c-80bd-3a28-81fa-56cf9deb0ead | -11.7699 | -51.01392 | 2026-09-27 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3af62d15-f90f-3d09-a269-4225c71d2e05 | -8.33965 | -62.85559 | 2026-09-27 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 148b1232-1c70-3429-8371-0046c39709e6 | -12.20736 | -50.37795 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d4fa812-c5a5-320b-a3e0-4767e1ed6820 | -12.7121 | -47.32362 | 2026-09-27 05:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0e2145c-6f66-3be0-b992-3e4552241ec1 | -11.85482 | -50.51419 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 41c6609e-cc20-33cf-81a3-e7d4b3a2f0ac | -12.27687 | -50.30037 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 46222e2f-d85d-3b5a-b72c-59e102e65af4 | -10.81039 | -60.72781 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6043b878-3268-3468-8ec8-6619d452cd49 | -12.29099 | -50.37166 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 689f267c-c0af-3edb-a638-b23d391734c6 | -10.65212 | -58.77269 | 2026-09-27 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3eca6e56-ceb8-339e-ba10-ba2ceb7b1b04 | -12.02836 | -50.59904 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 84439c1d-3d72-38fb-b65f-f28a5ce4a6f5 | -11.03915 | -51.32877 | 2026-09-27 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da634831-5d53-3334-bff8-0e1d5ee8825c | -12.26985 | -50.31108 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01313205-50be-3e7e-b7bd-2bbb5871727c | -10.6804 | -57.63511 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95667a4f-60e6-3008-8758-34c3f473f4f5 | -11.80886 | -50.52291 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89b0ec2a-ca76-3243-80ac-c711585971cb | -6.87539 | -55.58618 | 2026-09-27 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5538b4c0-e80f-3de6-ac97-cb0fedbda5b5 | -6.87642 | -59.8811 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91ae9bca-1319-3e77-8fdf-e3c799d72e99 | -12.25551 | -50.70335 | 2026-09-27 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbf7510a-e9ac-34ac-befc-b5925f253a43 | -9.57081 | -62.70488 | 2026-09-27 05:29:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 922d7373-a40a-3735-ad3e-5bcdeba3907d | -8.34155 | -62.85865 | 2026-09-27 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 112fc878-f2f9-34d3-b4cb-53f5deb971bb | -9.39395 | -60.34443 | 2026-09-27 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d49cef36-be31-3061-a4a1-fd85698a8ceb | -12.28483 | -50.28197 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 81a64682-e642-3048-b653-c99df161d2c5 | -10.81883 | -57.1972 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23b6af84-2288-3728-a543-fe7f29da1c84 | -7.49708 | -55.0181 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 19927c77-80be-3407-ad58-31c63a1f39fb | -11.98187 | -50.56712 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7b7071fb-9281-3fa2-88ca-4ec8711d92e8 | -6.8742 | -59.87351 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ba662fc-100e-3881-8614-194306bca496 | -12.71048 | -47.32362 | 2026-09-27 05:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d8f9ba89-b690-36a3-8ca4-e28eb171b5a5 | -11.27873 | -54.43288 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e732801-ef82-3c79-a671-d76be8b684de | -10.8229 | -57.21858 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6895bdd9-3d3e-3fda-8d96-b0da6d4cf38e | -12.30034 | -50.29566 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd2a6429-05ad-344a-ad27-0030a083799e | -11.81064 | -50.50835 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2dd048a0-7022-3d03-9df1-09b3c2d0e969 | -12.30597 | -50.29639 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42bc61b5-f626-3243-8ef6-10cde29e038e | -11.94322 | -50.56902 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bccbee04-6b41-3828-b00c-000d6dc34315 | -11.27496 | -54.42952 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 587110a2-a8c9-3ba3-aa56-da04a1aaba87 | -12.13481 | -50.33519 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0736b8b9-c577-3be3-992e-81eca0adff5a | -9.07897 | -66.09974 | 2026-09-27 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7e09614-0543-3514-9667-1d0519f8df82 | -9.04747 | -66.10848 | 2026-09-27 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5d12965-f547-3bf4-b635-fc4e8f329c69 | -11.04393 | -51.32614 | 2026-09-27 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb877ded-0ec1-38fd-a61b-c861bce105db | -12.12228 | -50.29895 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faf2741a-a4e2-3dba-a933-b795aee2d43d | -12.27031 | -50.30727 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bdb0953c-c7be-38cd-903a-e897df169d8d | -11.89027 | -50.50035 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e30d29c-4b87-35e5-80e1-077eaf906880 | -12.28576 | -50.2743 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 45071f55-b138-3a22-969a-5bc1ea5e4a92 | -10.82351 | -57.21453 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10a246f1-711d-3d76-960f-72cba850b1f9 | -11.77074 | -51.00721 | 2026-09-27 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ec5e6cf8-a022-3e08-a2b0-72f6ab7bf9b3 | -11.27926 | -54.42897 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3b680f3-77ed-3cd4-9b40-b68afca3e1c1 | -11.84793 | -50.52436 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fdbea0f-9a29-3a96-a24d-595bbeacd323 | -8.60178 | -63.93204 | 2026-09-27 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b5b108a7-2e5e-392f-a7fd-6df106ecf3ff | -11.02403 | -54.03948 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e22cf051-3670-32d4-92b7-35e968314083 | -9.31015 | -47.6311 | 2026-09-27 05:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e71679ff-0907-3b58-9fca-f0de4b3ff80b | -7.47445 | -54.98562 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaa62059-6d40-352b-b1ba-19339f79fd3d | -11.93478 | -50.50139 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1f1e1e1-fd1b-3b43-9603-6e19685cad62 | -11.88366 | -50.50579 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1653dca9-b70a-3ddc-98e8-0359a8d56257 | -10.68388 | -57.63564 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdcfbac7-2c4c-39e3-a15b-8fed873fb73f | -11.96339 | -50.5422 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cd1aca01-b9ed-3d3b-a7cd-e32ab9cf1b36 | -13.34437 | -51.33985 | 2026-09-27 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a261602-2434-3dcd-821d-2899badc87b3 | -11.77438 | -51.02135 | 2026-09-27 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b765450c-f08d-30aa-a82b-e6c1f337e265 | -12.29611 | -50.28344 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 772d6465-fe1d-3cf3-908d-b72ffe7147a9 | -11.89534 | -50.50471 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d229ce4-3f85-3e81-9e80-e51ae0065546 | -10.02003 | -50.14231 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 027b2409-0705-3ba0-8257-9fd7249d31dc | -10.01953 | -50.14481 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bbdeb8f-1bfe-37a1-b390-dadfb0187d61 | -12.27078 | -50.30345 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0fd7460e-d750-3ff9-8645-28a46589f901 | -11.9394 | -50.50941 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23f86d73-1b7d-39b4-ae02-3bd444256ffc | -12.70366 | -47.32291 | 2026-09-27 05:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b68dafb-2611-3a12-be76-089d3de6088d | -10.81374 | -60.72836 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75de52b9-a831-3ec7-91fa-12b41627d492 | -11.88963 | -50.50288 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f58ce727-8bf5-3aa9-97b1-8d61842c91f4 | -10.45074 | -61.3088 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d495fab-cc96-34d0-af73-d9c6176701a3 | -13.37441 | -51.31632 | 2026-09-27 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be61fe45-1e6a-3a8a-bb50-8e3afcefe9ea | -12.8993 | -61.72136 | 2026-09-27 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2eb0759-2694-31d3-abe8-c9d0890e481c | -15.99025 | -54.93604 | 2026-09-27 05:31:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fbf82a1-0f2c-3dde-a243-a59126e62873 | -17.79258 | -47.1607 | 2026-09-27 05:31:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95d1042a-1e46-3824-b3a8-b27d5adbdb25 | -15.9946 | -54.9366 | 2026-09-27 05:31:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f68a726d-9f97-3f6a-a498-2fa18bf162cf | -14.50156 | -48.3388 | 2026-09-27 05:31:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e81ffb59-7534-344f-8d96-23d03cec83a9 | -20.85219 | -49.06929 | 2026-09-27 05:31:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c3b6074c-b832-373d-9997-71ac33f812e7 | -14.48974 | -57.02117 | 2026-09-27 05:31:00 | NPP-375D | SANTO AFONSO | MATO GROSSO | Brasil | 5107263 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ba7a1c6-d060-315f-9d4a-8e096eb088a3 | -17.04212 | -56.57429 | 2026-09-27 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ab3e98cf-fb68-30a6-940f-ce4e08d7dd6e | -14.4135 | -52.80568 | 2026-09-27 05:31:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c95c06b5-23bc-321b-a975-7bc50358d482 | -17.79303 | -47.16615 | 2026-09-27 05:31:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54dbd78a-0d1a-3acd-8ee2-31f88241f6e6 | -12.90606 | -61.72251 | 2026-09-27 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28ca8d6d-1863-3a36-96e3-5d49e37c79ca | -19.63663 | -49.69073 | 2026-09-27 05:31:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37c1d954-08c4-369d-8d64-ad05dcc2554d | -12.89592 | -61.72077 | 2026-09-27 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6fe74d9-4f99-32f3-a8ae-c4341da72c7d | -12.89652 | -61.71712 | 2026-09-27 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dff11bf-8aa4-35ee-ab3b-1e77981e3d3c | -12.8999 | -61.7177 | 2026-09-27 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b841602-c6b1-3f0b-9af3-97120e2d7441 | -17.79192 | -47.16822 | 2026-09-27 05:31:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README48.md)
