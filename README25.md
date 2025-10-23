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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3abb9c2-a2b8-35f8-875d-b8fe497c1354 | -11.07321 | -51.57223 | 2025-10-23 04:38:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9582c40f-6735-3567-a6f0-97aa6628899e | -12.2562 | -49.59137 | 2025-10-23 04:38:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14add515-c3a9-337c-8751-882d0c27d098 | -11.99897 | -46.76955 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2574126c-b2c7-3316-b783-388d507775b5 | -11.49519 | -48.4722 | 2025-10-23 04:38:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c38e75e6-1702-3558-b0f7-cca453e60848 | -13.48476 | -48.78522 | 2025-10-23 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abeb412d-6067-32dd-9531-e2dd33f451e7 | -11.99838 | -46.7735 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74b5d06a-4f57-387b-b18d-ce488972c1a3 | -12.70044 | -48.83562 | 2025-10-23 04:38:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3445bb21-bcc2-357f-9d7b-6d777ff3dd2e | -13.90697 | -48.37009 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 492f903f-9cdf-33b6-945e-b602968c79fb | -9.99546 | -49.14743 | 2025-10-23 04:38:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f47585a4-a7a2-30a0-b43d-25383f66568b | -11.0537 | -45.39691 | 2025-10-23 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 622137e7-b9bf-3e73-88e5-a1ffc4e34101 | -16.07925 | -51.40874 | 2025-10-23 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56257c08-ac3a-3a96-8133-7a87439fcecd | -14.87519 | -59.63203 | 2025-10-23 04:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c53c89a9-a4e0-3218-8cb2-dd1b6fff839c | -11.35851 | -49.78991 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ee140b6d-d44b-3792-b1eb-584f89f93260 | -13.32934 | -47.95184 | 2025-10-23 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60b35b8e-cd4f-3fdc-8eb6-9753a50fdf48 | -15.13876 | -49.65218 | 2025-10-23 04:38:00 | NPP-375D | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c78d4a8-4099-336b-92ce-ff7e6f7d0e31 | -13.89909 | -48.37648 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a0aa02a-f7d0-3589-99f9-ec8a29a1764a | -11.35876 | -44.88299 | 2025-10-23 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 154debab-5bd8-393a-8d1c-c1df50f9d264 | -12.67482 | -48.62702 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb089b0d-8cee-397c-9ceb-94ba7c8fdfab | -14.89798 | -46.24426 | 2025-10-23 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7556105-a8ec-379f-869b-aabbcccb3555 | -14.06433 | -47.05465 | 2025-10-23 04:38:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec65712a-75ac-3ce8-ba77-6eca81de246a | -15.13876 | -49.65217 | 2025-10-23 04:38:00 | NPP-375D | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf3a9ec3-58f9-3510-a3ab-7ea24a17d70e | -11.00217 | -47.79877 | 2025-10-23 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d39c90f-2c44-35bd-8741-7235631adca1 | -13.80148 | -54.82232 | 2025-10-23 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01f6d156-467b-39fb-9039-93a6ca6fa257 | -13.79197 | -52.77147 | 2025-10-23 04:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a059a875-c494-386d-b9e6-8651e6797268 | -9.56216 | -46.69114 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77b3b0e8-77ff-3c2a-9ba8-393634bba950 | -11.34647 | -51.45069 | 2025-10-23 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e359724b-dff5-374d-a984-f012d1f1bd39 | -10.03618 | -48.71895 | 2025-10-23 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fc4262e-b0b1-340b-84e0-171b6274fcad | -13.21134 | -47.7424 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dc349c7-37e4-3ffd-aea2-22ca4be3a8af | -12.55082 | -52.22029 | 2025-10-23 04:38:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f3c5a68-8166-3789-9b75-7861a81f1a5b | -12.25288 | -49.59082 | 2025-10-23 04:38:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97d679fd-82c4-3959-8e9c-aab7818007ac | -13.79485 | -52.77629 | 2025-10-23 04:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13c2a74a-082e-38f1-8ea3-b2aef1ea5921 | -15.5956 | -45.90797 | 2025-10-23 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e15ff480-59fc-3cfe-86b3-93ed83504643 | -10.90916 | -50.1577 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 929dc47f-980f-3708-9f95-6ab9e53b473c | -11.24828 | -49.87775 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f613b24-4402-3b62-9169-85e4db784b93 | -11.99078 | -46.77636 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1218499-14ca-37dc-a8f0-78912cf84338 | -13.29218 | -48.87576 | 2025-10-23 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c963de1-f0ea-3bf8-ae98-94fd8341fd51 | -11.78984 | -47.06792 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80c3e4a6-3c94-3e09-829b-4ac19917264b | -13.04155 | -47.23033 | 2025-10-23 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c31df71b-fc00-340f-94a3-64dd5648218b | -13.69908 | -47.88274 | 2025-10-23 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1670886-e59b-3b19-b896-c750ec98ceae | -9.86856 | -47.71319 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46c63fd2-1118-3b2f-97fb-9a2e168556e9 | -12.00597 | -46.77063 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e389bf60-d3c2-3ca0-95db-710bf2bc8a9b | -11.07388 | -51.56824 | 2025-10-23 04:38:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a319f95a-79e9-3701-b755-9d388544288b | -12.67203 | -48.62289 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffa3c034-dfc6-3535-9fb4-3045dab4283c | -11.35126 | -49.79236 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2290bb95-d7d1-379c-b37d-7e153b31e949 | -11.36457 | -49.78704 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62687d34-7abd-3fdf-8ed7-06036c8a52f7 | -16.4343 | -51.78091 | 2025-10-23 04:38:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 370072c0-85bc-3eba-b76a-d5ff824a5e5b | -12.77357 | -47.38657 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 007e346e-42a9-3438-a00f-ad495fa3111f | -11.86146 | -46.7537 | 2025-10-23 04:38:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 558e51d3-bf98-3f0e-8eaf-67a126593fbe | -12.13187 | -46.72486 | 2025-10-23 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b50c56a1-e8d2-3c8c-9be5-3b96d5688aff | -9.86521 | -47.71265 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18411bf1-f773-34ec-ab4c-63388013fb06 | -10.66533 | -47.33989 | 2025-10-23 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4bf362c-ad93-3c3c-9888-633a9a477100 | -10.96543 | -50.26334 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5cfd51c7-a73e-3036-a18b-de6212b7ce2a | -9.97209 | -47.08325 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee28578a-b167-371c-803f-cb03e1d622cf | -9.6814 | -47.6368 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b04a53e-b768-34c3-8283-9c84b6f3c33e | -12.2637 | -47.02402 | 2025-10-23 04:38:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2840f2e1-d41f-34c7-858b-181bf17ade09 | -13.21134 | -47.74239 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ed9adba-7aee-3161-9359-b99b9c9095b7 | -15.65889 | -52.87435 | 2025-10-23 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a670f156-bea1-3249-a43f-a9c33c7ad9d3 | -12.68652 | -48.63983 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81c6a370-3114-3010-8acd-9c1ed9631819 | -11.28739 | -45.5174 | 2025-10-23 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e5860d6-4073-32e4-aca3-f0eecdd2ce03 | -3.0354 | -49.4688 | 2025-10-23 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c4ffb976-382d-37a4-8b60-e83fbd5ef410 | -12.0032 | -46.7892 | 2025-10-23 04:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 84cf1b77-ff1e-3ba4-a048-015000c7653c | -3.0169 | -49.4694 | 2025-10-23 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f90fe02a-71b9-306e-b532-724e727f2a09 | -3.0353 | -49.4901 | 2025-10-23 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f57efe78-af79-3b22-b5e0-d3ea6624a570 | -17.61602 | -46.62308 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99863d03-a3d6-3e8c-a1d7-dd7257f7c6ff | -17.61486 | -46.60366 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 536d61f7-d444-3220-914c-3bddd076755b | -23.65408 | -51.68788 | 2025-10-23 04:40:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 893de727-4322-3c55-a69d-30ecabc1b940 | -21.67752 | -49.05786 | 2025-10-23 04:40:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fd764f8-afbf-3895-a0f9-8c66756bd3b9 | -20.48281 | -44.23657 | 2025-10-23 04:40:00 | NPP-375D | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 14d19021-ddb7-3ec7-929b-091e146a7ee2 | -19.26569 | -51.97859 | 2025-10-23 04:40:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7066c569-c4c4-31f2-a100-29a760c242d7 | -17.60424 | -46.59729 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d9ab2fc-4870-38c7-8f59-ebe1e4e3a665 | -17.64716 | -46.64684 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1e1ebc7-42c6-32d6-aa52-e1b8f822466c | -18.69773 | -47.05586 | 2025-10-23 04:40:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b90d5c25-458c-3dc1-a8b9-7ee7f7637f32 | -17.14688 | -53.30905 | 2025-10-23 04:40:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2714f652-1273-3ad4-8fc1-0c2f2eccbfd6 | -23.77333 | -51.72513 | 2025-10-23 04:40:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 60fd5d8a-9b5b-3b2c-b291-1db8b30b20a5 | -19.15462 | -49.13157 | 2025-10-23 04:40:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f4013f9-9df3-3d10-b5b1-872ec6fdd13d | -16.5292 | -52.77564 | 2025-10-23 04:40:00 | NPP-375D | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbc4cd41-c15f-3634-9cad-63c03c99aec2 | -18.23222 | -47.42167 | 2025-10-23 04:40:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32f1677c-44f2-3f3c-b88b-8bf4d8dc2117 | -20.98164 | -47.36265 | 2025-10-23 04:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a414182e-670b-364b-bdea-1ac02cb6193c | -19.26569 | -51.9786 | 2025-10-23 04:40:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6777d4c-8f6c-314d-b822-58689e4a6da3 | -18.18426 | -46.19546 | 2025-10-23 04:40:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ad1085c-784d-3441-acd4-c7c2bef2aba2 | -18.22982 | -47.41232 | 2025-10-23 04:40:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58fa30f0-93b4-3c1e-aa19-fdbf2bed26ba | -17.15043 | -53.30973 | 2025-10-23 04:40:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2514250-4fbf-3079-bc0f-3998e6f828ab | -17.62483 | -46.61475 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b97c7d1c-3314-33f0-98eb-2479e6de5569 | -20.13076 | -41.79824 | 2025-10-23 04:40:00 | NPP-375D | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3870eb86-0b74-3865-923f-396a432ae9ea | -17.61162 | -46.6272 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56ee961f-307a-3444-b5ca-681b365419d8 | -17.14972 | -53.31391 | 2025-10-23 04:40:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edfff978-e98c-38e1-90c7-9cf6f36cf8af | -19.76558 | -41.29677 | 2025-10-23 04:40:00 | NPP-375D | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e3bbc7b4-0a02-3fb5-9a87-ee63a5940a79 | -17.61356 | -46.61309 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b288a1c5-bd80-3608-811b-36159a61b16b | -20.69866 | -55.43392 | 2025-10-23 04:40:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1fd9114-69e1-348d-a624-b2ef1f33d6fc | -17.6036 | -46.60199 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| beedaf08-fa2d-3b9a-bc25-ba39a07f42c2 | -17.60851 | -46.62197 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60873575-33ad-3f22-ba44-1e2402b338b4 | -18.14017 | -52.97381 | 2025-10-23 04:40:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03858d02-3ab7-31ad-a7af-76421bcbdfd7 | -20.55565 | -54.55806 | 2025-10-23 04:40:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27271167-bbb5-3e85-b478-e0d9107e3ca9 | -17.61473 | -46.63244 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0ad0b45-e925-3db4-9a4c-d6dab3d2aaf2 | -22.21917 | -54.30404 | 2025-10-23 04:40:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8a0f1b2b-4f99-3f92-991d-30f833c3a1fe | -18.23283 | -47.41729 | 2025-10-23 04:40:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1742b3ea-e5f5-320c-89ca-1e2ef68cf6d5 | -21.95351 | -42.93355 | 2025-10-23 04:40:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 0ba11c03-c55b-31ac-adc4-5a6ab9eb0ae6 | -22.873 | -46.63554 | 2025-10-23 04:40:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 647834ca-7391-34e4-9cca-ba75dade3a5c | -17.61912 | -46.62832 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d07418a1-f268-3f1f-bc92-26369eeff780 | -17.62173 | -46.60948 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README26.md)
