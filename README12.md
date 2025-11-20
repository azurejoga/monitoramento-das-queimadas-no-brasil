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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39e35836-8011-323e-96a8-335dd1c310f1 | -10.36433 | -48.90627 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f7cf17e4-bf5b-388a-a27d-f10c04633047 | -14.53343 | -48.62326 | 2025-11-20 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4ea50ca-0e0d-3420-a1d7-08a09d4129c0 | -15.19389 | -48.09649 | 2025-11-20 04:33:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4e3cdbea-2445-3c93-8a9a-f7653da4313c | -13.7255 | -49.90625 | 2025-11-20 04:33:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6351ddca-3372-3ebd-b9ba-3afb4289d4d5 | -10.35827 | -48.90172 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1e4b951f-17d5-3eca-b9b7-bdcfcbc79c32 | -10.97579 | -49.29243 | 2025-11-20 04:33:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 601dd8e7-f1ac-3c68-b066-66c50f28e851 | -11.5616 | -48.46278 | 2025-11-20 04:33:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95c76707-92d2-3453-8fcf-d83a25acb8c9 | -10.84255 | -56.33517 | 2025-11-20 04:33:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 162f4274-c135-3e17-8f35-7f02ebae5814 | -11.37452 | -49.26376 | 2025-11-20 04:33:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c586c932-92f5-3d09-9e72-dd6aa81f907a | -10.66577 | -49.72216 | 2025-11-20 04:33:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7749d513-2f41-3330-af96-0a3aaac58683 | -12.61452 | -48.87429 | 2025-11-20 04:33:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4c8ab05-16e6-340e-a591-ebf3fc111218 | -13.94202 | -47.46112 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fa44c48-c0d5-3f61-a8fa-d25cd311c3db | -10.79293 | -47.96771 | 2025-11-20 04:33:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eab6cfb-9a9c-3435-8c53-24000405e82b | -13.94087 | -47.46891 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e4a0623-dbc4-3483-9ab6-333c33bc16df | -12.96337 | -49.97696 | 2025-11-20 04:33:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b35eb637-cc7d-3b15-afa9-c9f8bd9e9f94 | -9.34921 | -50.74218 | 2025-11-20 04:33:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79aa4050-23e1-3300-8171-cff1b1bac746 | -12.43284 | -47.88052 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aafd406c-574c-325e-bda8-9580eb07caaa | -9.70685 | -49.9397 | 2025-11-20 04:33:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec071b2b-d959-3d4e-bd5c-0cca00352b7e | -14.66412 | -46.52213 | 2025-11-20 04:33:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e582f158-6b34-3b57-bdd6-1a84ac1235b8 | -8.87507 | -48.80552 | 2025-11-20 04:33:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50b5ec5b-b0c8-3c1d-b018-69497895d47f | -11.49151 | -48.23778 | 2025-11-20 04:33:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| affe132e-5877-3b6a-9d9b-00722519e786 | -9.3962 | -50.68709 | 2025-11-20 04:33:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d284dcde-07ea-3c73-946f-992edf49308b | -14.06084 | -47.60326 | 2025-11-20 04:33:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 302f0644-3c16-3d03-b610-bb4929feb529 | -14.66775 | -46.52258 | 2025-11-20 04:33:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0edd027b-51d4-3b8f-abd2-5b27e062d773 | -14.53008 | -48.62271 | 2025-11-20 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66bd3265-e51e-383d-929e-b5648a9fc5f1 | -9.74166 | -50.33363 | 2025-11-20 04:33:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8354656-304b-3d86-8416-d81dd40371ae | -11.49096 | -48.24132 | 2025-11-20 04:33:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5510efe-6ee7-37bf-be2d-8d3ae3362198 | -11.55828 | -48.46225 | 2025-11-20 04:33:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a5c2ddd-e022-3109-9abf-1dc35c821b3f | -9.45994 | -56.64375 | 2025-11-20 04:33:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 07f09630-f760-3d32-b380-e3cce4601a69 | -9.39351 | -54.6049 | 2025-11-20 04:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bf0fd8a-606e-348f-8119-ebdfe60c9980 | -10.79067 | -47.96353 | 2025-11-20 04:33:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c4c7909-2255-3e79-80f2-76d125cdac69 | -12.32151 | -46.4964 | 2025-11-20 04:33:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28141d89-6833-3588-aa46-73d1664de048 | -13.36658 | -47.66055 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d8d5f66-31cc-3080-931a-665727045684 | -12.67774 | -46.77248 | 2025-11-20 04:33:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b38ddd86-3c9a-3ba5-96cb-687875855e0e | -11.26456 | -48.4946 | 2025-11-20 04:33:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e01bcb2-b949-33e5-9e2e-4db933286c9a | -14.5535 | -48.62653 | 2025-11-20 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5f48140-6eb9-3f4a-9c64-c5f8db1d6eb4 | -10.79012 | -47.96711 | 2025-11-20 04:33:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3442aef-430e-34fb-bf41-a7dbb4247a58 | -12.94499 | -47.71756 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7715cedc-9a53-3a6d-b41f-92dfadd08b96 | -9.74225 | -50.32995 | 2025-11-20 04:33:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d68ea38-9176-39c1-8b97-f56b91d62d56 | -13.92888 | -47.47857 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53b36fca-aa19-3768-91f9-14bd5ee9886b | -10.36488 | -48.90279 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a4ef131e-49a3-305e-943d-1b36c20dcaa8 | -10.48426 | -49.37023 | 2025-11-20 04:33:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6dc6e43-9958-30b9-a2f9-f9766b65cfe4 | -14.52952 | -48.62636 | 2025-11-20 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c3c2b55-c3ef-3bad-9089-2e1cc003e760 | -11.2607 | -48.49759 | 2025-11-20 04:33:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75c60ce8-a3db-3d33-be6a-461bc729d93c | -10.88532 | -47.63367 | 2025-11-20 04:33:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffadbf6a-6c1e-3b6c-bc40-56556f691fce | -12.5331 | -47.54837 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f7be1ee-9940-3a77-ac42-6c83b69e33f2 | -12.68006 | -46.78095 | 2025-11-20 04:33:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cedb9ce7-61e2-382a-8c14-0be0c1e71df0 | -10.17597 | -49.17312 | 2025-11-20 04:33:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8407026-086a-33ba-a44c-e37d5cc53e42 | -14.63535 | -46.54234 | 2025-11-20 04:33:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 667c586a-28cc-34b3-8744-39f9678b4b33 | -13.23808 | -50.82345 | 2025-11-20 04:33:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edd9cde7-f93e-301c-ac64-023f94ba3209 | -13.69372 | -48.43529 | 2025-11-20 04:33:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1da46d1a-9070-3ecb-bd2e-4e44e7a9b784 | -13.41767 | -49.05794 | 2025-11-20 04:33:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5a7cc0e-06db-3816-89c6-69e92d411b14 | -10.88467 | -54.14087 | 2025-11-20 04:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89a4a7a1-8b30-37cf-a3d3-c6526487fcf2 | -14.53677 | -48.6238 | 2025-11-20 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3130e21-2a82-324f-857d-7ec0d29b0bba | -10.38358 | -49.93149 | 2025-11-20 04:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff28b4ba-1e42-3b08-99ce-8cf7bd2c4e71 | -12.88006 | -50.15652 | 2025-11-20 04:33:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f2a13831-6d9f-3953-b2f4-52502f87d82c | -14.62926 | -46.50751 | 2025-11-20 04:33:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f19acc9a-1487-3130-b4cb-97700bf43d65 | -10.48482 | -49.36671 | 2025-11-20 04:33:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a4084b5-0d48-3f1c-86b9-da3240f1f779 | -14.5429 | -48.62854 | 2025-11-20 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9757cf7a-aaa9-3c91-ae55-b954b2768faf | -12.9844 | -49.80239 | 2025-11-20 04:33:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a362e499-ffb6-3eb8-9934-b1016f57a651 | -9.05743 | -48.83451 | 2025-11-20 04:33:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 421cbd3d-3e88-34e7-ac71-825341e50484 | -9.39557 | -50.69088 | 2025-11-20 04:33:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 415f3f94-844d-3aa9-a073-a8762bd54935 | -14.47117 | -46.97968 | 2025-11-20 04:33:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 670711ac-e274-395f-a26b-109fad43883d | -9.39281 | -54.60889 | 2025-11-20 04:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 31fd57d5-13c1-30aa-a027-462e039ca001 | -12.09001 | -49.61493 | 2025-11-20 04:33:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c056d1f7-7959-3b13-ae76-89a5edf1beb5 | -20.68084 | -50.12507 | 2025-11-20 04:36:00 | NOAA-20 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 73f119c0-3975-32c3-94ff-1b117ef55676 | -17.61749 | -54.1916 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d87d8171-4002-3480-b4f1-44834200de5c | -17.61667 | -54.19619 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8af73f6e-3e73-3eee-9072-3d34a5dae151 | -15.80112 | -52.39396 | 2025-11-20 04:36:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6acf172-b76a-3a54-86c3-48b2918886dc | -17.61625 | -54.17732 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bef57902-9942-397a-9cc7-892d998076ca | -19.47798 | -53.9537 | 2025-11-20 04:36:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4599fe16-5904-3621-a21a-dd0e1f7835af | -19.47071 | -48.92027 | 2025-11-20 04:36:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e137152b-6cc3-319a-bbb0-0223284dde45 | -16.32465 | -50.05359 | 2025-11-20 04:36:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52c1e2a1-1d60-33f1-9cea-8b90a10d3b52 | -17.66282 | -54.21424 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6411cddd-ebd3-3c2d-b5df-f5502a8a10e1 | -20.88457 | -52.34473 | 2025-11-20 04:36:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23ba3a54-390a-3a40-aa73-968d95d0bc22 | -15.90436 | -54.57761 | 2025-11-20 04:36:00 | NOAA-20 | SÃO PEDRO DA CIPA | MATO GROSSO | Brasil | 5107404 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f44a630-0460-3c7c-9d4a-e0c62edc7a2b | -21.33636 | -48.69175 | 2025-11-20 04:36:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ccdd452c-ebbf-31e3-8627-0c5f4317dd68 | -19.47519 | -53.94867 | 2025-11-20 04:36:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5b3b2a0-4a5d-3fc4-8bc8-866a63be25a5 | -16.47964 | -52.48939 | 2025-11-20 04:36:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f7e8bce-e852-3075-a187-6a8b1015ead1 | -17.53769 | -53.7051 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 56460245-f9a3-30d0-9dc5-af93da0981e4 | -20.7369 | -55.6979 | 2025-11-20 04:36:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6190ba2-9903-3dba-8acf-faaa6cce590a | -15.54177 | -50.66118 | 2025-11-20 04:36:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f1514bf0-903e-3ffb-ba8b-af19e9d29e8f | -18.91582 | -47.17432 | 2025-11-20 04:36:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be651d1a-5c8f-3f6f-8abe-d6e52c6390ad | -21.04245 | -48.5507 | 2025-11-20 04:36:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3b6bc6e6-fe72-3ccc-87bf-ff001c1644a6 | -21.14319 | -48.52684 | 2025-11-20 04:36:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e9722b7f-68ab-31c1-b234-7d6bd46109c7 | -18.15475 | -54.55677 | 2025-11-20 04:36:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ea90083-3e66-304f-a5a7-f6f07c348035 | -20.30016 | -50.96952 | 2025-11-20 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ae5a9c4b-eb5b-34f1-9313-42fa95d7b27a | -17.62035 | -54.19682 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2027649-b556-30f1-8cbc-863514d4bb5b | -20.73597 | -55.70293 | 2025-11-20 04:36:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91e578ad-ce3a-3fae-8e2f-5d3eda706545 | -19.47413 | -48.92083 | 2025-11-20 04:36:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4582ef6-dbd6-31db-8e7b-991a845d714b | -20.88728 | -52.34914 | 2025-11-20 04:36:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d97d8648-8ece-3e4b-b8a8-24d4901cd347 | -17.50319 | -44.9284 | 2025-11-20 04:36:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ea5be4a-7aae-32fd-aaaa-01791ee706eb | -20.29685 | -50.96893 | 2025-11-20 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 58c90903-24c2-3283-b4d9-3cc10959d071 | -19.08075 | -41.75615 | 2025-11-20 04:36:00 | NOAA-20 | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5a525e8b-958e-3900-80a6-e5daa0e9ba93 | -21.14673 | -48.5274 | 2025-11-20 04:36:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d43a1398-8d1b-3242-8367-30646ba4d568 | -17.62117 | -54.19223 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 076e8435-dad8-3856-bb5e-48b66d778a0b | -19.79668 | -46.07819 | 2025-11-20 04:36:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a429f84b-ca70-320d-a204-6c4d82434b64 | -17.17432 | -43.30284 | 2025-11-20 04:36:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97c4cc35-5326-3207-929c-6e323a97daf5 | -21.32991 | -48.68644 | 2025-11-20 04:36:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 64b27fde-9582-34d1-b8e6-5610c7b93199 | -18.12348 | -54.5168 | 2025-11-20 04:36:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README13.md)
