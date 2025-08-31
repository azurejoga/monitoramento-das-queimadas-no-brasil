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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9e53df5-c4a6-32f0-8d7f-740f112815ce | -13.67127 | -46.93107 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcd52ff5-41c3-3585-a630-80a9ab87028e | -11.02137 | -46.88107 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9f7e58c-ad63-3c8e-8c2b-08cea8080de1 | -10.02798 | -48.09257 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eea0e079-5d5d-3396-ab6a-3255786d35c6 | -11.86781 | -46.50648 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 160922fd-422d-33e9-8e0e-84d3883ad4a0 | -13.3504 | -46.95381 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ef6119c-79d7-37e8-b10d-3abab98dca85 | -12.3999 | -46.47174 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 589252f4-e040-3bb3-ae4f-e885966f11b9 | -13.69655 | -46.91306 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4487d38-5305-3ee0-8af0-d1d8f2e4157d | -10.70805 | -49.00741 | 2025-08-31 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99ba80c1-031a-39c5-8bdd-1833480376b3 | -12.63725 | -48.21197 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 643680e5-afd1-3709-affd-51b587a002d5 | -11.89794 | -46.46718 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 583a3959-dcfd-3557-9434-18653afbf4dd | -14.22638 | -48.07212 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2368fb9-3271-34ff-af0a-27d83b502186 | -13.35542 | -46.94358 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7660f14a-c0be-301a-8b16-ff9d3fbb5cfa | -11.88545 | -46.34761 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2985d370-b569-3768-a391-ecf502df1a01 | -12.56249 | -44.79468 | 2025-08-31 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 274a93cf-b6f1-33cd-b1a9-a8642952d3ef | -13.54193 | -46.95826 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b8123e0-ac44-35e2-9559-13e08f74502b | -14.83002 | -46.74626 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e80bd71-18ff-3498-bcd5-0fe29dadf1c8 | -8.96262 | -50.01057 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 677fa377-d1d6-36fd-8a12-65f33419887a | -11.08498 | -44.74034 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6febf67e-03f1-31a7-9339-361183a5c2e7 | -13.30408 | -46.92056 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85de2b44-954c-3625-a4da-b6f9c4bf335f | -13.48666 | -46.96073 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 761beab3-444a-3dfc-9909-f8e6ea64c2cd | -14.82321 | -46.7455 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06c5525f-5632-332c-a556-7a6d88505753 | -14.83398 | -46.74304 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6eda1a93-a727-336e-be60-5e46877ad4e3 | -13.5128 | -46.83522 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c435c110-2530-3611-b966-31073527b25f | -14.2297 | -48.07267 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0285cf91-cce8-3e10-9a44-902c111430e7 | -11.07522 | -52.04538 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bde2950-9863-3943-bdae-e0cade3e8d7b | -14.23139 | -48.06199 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a4fbaaf-d33f-377d-8371-1c4f7f446af7 | -11.06022 | -52.03763 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bbfd872-fd12-31f6-82ea-863dd4aba890 | -11.82542 | -46.53646 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b4c644b-f99e-3b62-8822-703faad60a82 | -13.35652 | -46.95854 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 488118dd-6cdf-3a98-8c0b-c7f31599fb78 | -11.81909 | -46.44369 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 39f9049b-a4b5-3bc8-8d0a-1d4c11bb7671 | -14.2756 | -51.88476 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af92960d-bcd1-3264-9f48-0c5077d50806 | -11.91047 | -46.70683 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9fef227-bedb-3393-b86f-1c123a2f80d2 | -13.35866 | -46.95475 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1328c7b-3974-3540-b751-f04852eab83b | -10.95727 | -50.85691 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 3948db6f-247b-37a7-8e3b-ad4a30abb528 | -11.36159 | -43.60782 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 366e701f-22bf-3392-8f83-a5eef59d9d0e | -14.03806 | -44.56761 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 84375753-649f-3e67-9789-8b1cb9f322aa | -13.35922 | -46.95115 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7b0357a6-02ad-373a-ada7-a5743162d6dc | -12.09352 | -44.72816 | 2025-08-31 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| e1c0f4d0-5a45-353e-8b71-70403181e642 | -15.94753 | -41.39677 | 2025-08-31 04:29:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| afb666f8-e0e7-395d-b1bd-f39fc384e1da | -10.03922 | -48.08693 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 95329675-d14a-3a24-bdb7-a3ac8ea3e623 | -13.32414 | -46.87958 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f4fef1d-5235-34d9-a814-aca5c08c9a9b | -11.8358 | -46.42444 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1f08d33-3454-3aca-aea4-2bff03c2e70d | -11.33662 | -43.62225 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39ce264b-fa82-34ad-8914-ee6e473e2e08 | -12.31508 | -45.7247 | 2025-08-31 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 096837d0-e496-3205-a043-9ee9d810615d | -11.0186 | -46.877 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8504b77f-7aa0-34c5-b515-2e032c779b47 | -10.48575 | -51.62606 | 2025-08-31 04:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd0b4fdf-c779-3335-a78c-b02029e330c4 | -11.34209 | -43.63691 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 85b2bd25-c339-3bdb-8186-e169f329d783 | -11.81107 | -46.439 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ee33cf67-2226-3043-9db4-51037552072b | -12.07423 | -50.63443 | 2025-08-31 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1ea9d7c-cced-387e-80c6-d90e81cd94a2 | -13.99826 | -46.32487 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1739088-e173-3b6c-bcf4-05000aa0c954 | -11.33092 | -43.63521 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b63f3339-801d-35be-b8ae-663806a02b7a | -13.47333 | -46.98033 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 70c51f14-361c-3bb9-8e7a-f441bc7a2d45 | -9.65938 | -48.34484 | 2025-08-31 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce8e3209-935a-32eb-a425-d682d6a275a9 | -10.03306 | -48.08237 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a40e92e7-09b9-39c0-bc87-b7fefa6c7d86 | -14.82662 | -46.74586 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b538adef-66a4-3d65-b73f-825b53cd30ed | -11.07706 | -44.62514 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e2220d1e-b861-3d31-b4c6-67ed921d2093 | -11.84744 | -46.79201 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e59fee22-98df-3565-8d77-d566f4c2ef30 | -11.83464 | -46.7863 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec888618-2070-3656-9523-8f1ba1241705 | -14.03441 | -44.56704 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f09f0db-d20c-3745-8fc3-bd5821d3bf23 | -13.67463 | -46.93159 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de5a5ed4-e62e-308e-93b5-a5f4677366cb | -9.43407 | -48.33445 | 2025-08-31 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfcc3740-7e19-3bbc-9edb-43a0f7646698 | -11.89278 | -46.36706 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6950bc7b-b02a-3a72-851f-97e5ece4b036 | -14.33249 | -51.86886 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 28422c1c-9456-3c2c-b3ff-0bc657bbbecd | -11.91102 | -46.70327 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0af3f9b0-ea58-3e90-999d-d1b689c79bce | -11.32638 | -43.66633 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df3bf53b-5b86-3cbb-8f27-49bd2bfb2511 | -11.77875 | -47.39652 | 2025-08-31 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 916a90bd-542c-35bc-926e-c6fddae58f01 | -11.31879 | -43.69234 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 361b6f2a-539d-3ccb-9e5e-3ea691af58ec | -13.49266 | -46.83206 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5f11f33-47ce-3a37-b796-879b42b3b9ab | -15.95146 | -41.40241 | 2025-08-31 04:29:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d8fe82ad-e78b-3f3f-af90-d0d1a8de66e6 | -11.90319 | -46.68751 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee1444f8-0945-37a7-bc8c-c0405585234b | -11.42137 | -46.91608 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 481e7ce3-67de-322b-a561-2caa53a26252 | -11.80293 | -51.45545 | 2025-08-31 04:29:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88fbb491-b78d-3f0f-abb3-d03a67ca20da | -12.07352 | -50.63866 | 2025-08-31 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91723eaf-8955-39aa-ba5c-e8bd40b4777c | -11.34275 | -43.63237 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| af6af9c6-6b78-3ffc-9ee0-2bec5e0825a0 | -13.54137 | -46.96188 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50d5183e-9683-3b8e-b085-6a42cbb5614c | -13.48945 | -46.96482 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2d5c9504-9d4d-32c8-954b-2e3791195ffe | -10.04008 | -46.02681 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21a9234f-1b62-3052-9fb2-83952d3182ba | -11.83131 | -46.78576 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4706cc44-1ecb-3293-aa4a-e6f250729dc7 | -13.31355 | -46.90367 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91905020-3a5f-3e14-976d-60e92db17309 | -13.14443 | -42.00097 | 2025-08-31 04:29:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ff8facf9-9fa8-30ed-85df-90d095fcd39e | -10.9484 | -50.84163 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9415e30c-95b6-3ff1-9641-85ac82729d00 | -11.07784 | -45.1244 | 2025-08-31 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc304deb-0cf9-32f2-9efb-2d25958011ad | -10.02855 | -48.08901 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3309ca06-d535-3a31-a618-517c3646c7cd | -13.50944 | -46.83471 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04f24660-6e28-36d5-b969-a25738841995 | -13.02825 | -56.90271 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f538a48-2d10-3a2e-b8bf-b331f3085a7c | -11.2953 | -43.56544 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9cb2647-c4eb-33c2-9831-2c529824d133 | -12.10408 | -47.22508 | 2025-08-31 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fed8db55-8000-3355-96b5-86661552147f | -8.96706 | -50.00877 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 635b1296-f368-35f1-9a44-6c4fe4749d47 | -11.41914 | -46.9085 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4125749-239b-3c2b-ba5a-11d1c4547fc2 | -8.9532 | -50.00214 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec9cb377-63a1-375e-8f84-572173dfe8b6 | -11.886 | -46.73217 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9be990a2-a960-3a24-aa3f-1e6fee5a369d | -13.46183 | -46.97519 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d35c7e3a-4b73-3714-ad88-5c9212f4c1c5 | -13.68513 | -46.88575 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5163c04-151f-3ea3-9848-8e469ff76aa4 | -13.53689 | -46.96861 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 495d11ac-fbe9-3b07-94d5-8d19ec7d382c | -12.91977 | -56.98046 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9577547f-3c16-346f-961c-61410ceff4b2 | -11.0688 | -44.63203 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbd79c61-9a5f-320c-a0bf-170291020375 | -13.02763 | -56.90597 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dc9d4c5-f5bb-31c6-9157-17d12afaa1b6 | -11.02303 | -46.87048 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bffbc3b-7336-32e6-98e7-085184989b00 | -11.90987 | -46.68855 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 98e18e73-42e4-3153-bbfe-2f8e26fda58e | -12.63637 | -57.00234 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README49.md)
