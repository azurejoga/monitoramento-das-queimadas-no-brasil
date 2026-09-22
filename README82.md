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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 424c732b-8ccc-36a3-a0ae-bf08bfb8cb8f | -13.32892 | -51.28529 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 792210b4-9407-3ee5-8c93-3e79c3af3e68 | -6.30462 | -57.739 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 706c4a74-8e76-3497-a9aa-784408cf133e | -6.7302 | -55.08737 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a76250e7-e403-3c74-b089-473cd1867279 | -11.01582 | -54.13548 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f97211b1-231a-3df4-8d17-cd7ac2992a00 | -6.4701 | -59.99683 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9655292-ef65-3a9f-ac4a-8e139fb80830 | -7.88409 | -54.72378 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3272c91a-cde6-30a3-aca7-2629a1d17c4a | -7.05015 | -49.91942 | 2026-09-22 05:23:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37ef9955-d8cf-3d00-ac2d-3dd5f60a8fa3 | -3.0605 | -54.40139 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 236cc07c-b6ac-392f-9834-2f294a10810a | -6.43195 | -55.61827 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbdbe9bb-9838-3570-9ca3-0f26001ea17e | -11.87242 | -46.84811 | 2026-09-22 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c803a6f9-0d3f-3ce4-8ec8-ff6604ef504e | -6.63201 | -59.93304 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 30a16bb2-dae6-3eb3-b090-90b16550e311 | -5.9134 | -51.95859 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78686c71-c655-3f06-9461-a715cb4cb37a | -2.86806 | -57.79984 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6aa3fe1f-fdf3-38b1-9c38-7f2a002bcd11 | -6.26651 | -53.1185 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33262c83-d6a9-3d1e-b69d-a2984a40eb7e | -10.8956 | -53.96954 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae990beb-bee8-31f0-bd2a-c5326827169c | -4.35132 | -55.6502 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 856ab983-0ab0-3ea3-b27e-e2c7c590920f | -1.20597 | -54.01704 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f9cb043-75c5-370c-880f-2aa4f5faa7e2 | -3.33991 | -59.87196 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 603a86ec-6d38-36a1-bf0f-1c7b643033e6 | -10.88073 | -53.96233 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d54f9a6-9fff-368a-a548-35d51e557fe6 | -5.76364 | -45.08437 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a8bc08a-f735-31d0-b82b-6aa22269b812 | -5.01551 | -56.09036 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 128efaf9-f0e7-3130-9781-0a0a89081b84 | -10.86597 | -57.16705 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c21df443-773f-3885-8735-7f7142c2f31e | -3.01637 | -59.15577 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0c7a681-6eac-31d9-939f-fbafb73be545 | -2.93058 | -57.82778 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1fbadc7-911a-3306-b9a5-e58d8c956a57 | -8.68043 | -70.02898 | 2026-09-22 05:23:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f24da0a3-5cb0-3d33-a789-c5bbd0fd68f4 | -6.465 | -59.98377 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 378de4db-263b-3b10-9df6-290a127eed40 | -3.46149 | -58.32848 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e833aac-5973-3d4c-a996-e21cfa01f06e | -12.13976 | -61.16655 | 2026-09-22 05:23:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c9a06f9-2096-317e-9d67-ba67fd8fb712 | -3.90529 | -60.59365 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ea744b4-3749-3bd2-8e2f-068fcb094078 | -10.89878 | -53.97507 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c8eacfc-3f51-3f0f-ab6c-b67fce854795 | -11.32809 | -51.3691 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 961743be-41a3-3baf-acb5-c53c0ce752bc | -9.55033 | -66.04944 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3058bb87-ddfa-3f04-97a9-3f8ab3f418d5 | -6.62487 | -57.98355 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2bc27e7-52d4-3ce5-a05b-4975824de7c1 | -10.14775 | -58.75981 | 2026-09-22 05:23:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8489ad1a-baa6-3da5-bc3f-bafb390706f9 | -4.96562 | -55.82867 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 959df82b-3312-3fca-9484-1c5f912440f2 | -6.81426 | -59.43486 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63d59993-4417-3f7f-a7b5-1ecd21edbe97 | -4.48426 | -55.49051 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 338416c6-8718-3084-a45e-5071137325f3 | -2.41539 | -58.27433 | 2026-09-22 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1b832e32-f321-3bd6-a727-0eab64140b1d | -6.29923 | -59.96231 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ac3d058-76e4-3eba-b40e-1e74a53411ea | -3.28488 | -57.85804 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ee588e1-5c5d-3b89-ae23-e4b7ede7031d | -3.01151 | -54.1829 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf600eea-9694-39f7-8d6b-de2778315c34 | -3.71483 | -60.55342 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c45dbfd0-0150-3636-96a4-d2d4ddc2862d | -7.24223 | -55.60656 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd784173-294a-3a90-9acf-6ff5b610a6fc | -2.17255 | -48.32153 | 2026-09-22 05:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| acc98681-8fd7-306b-bcaa-c239a5694183 | -10.86934 | -57.16758 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ae666097-c844-3e76-83b7-1bb1c15326bd | -6.64032 | -59.92635 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 5bf46cc9-2eb1-39c4-b8ee-d569b85be210 | -1.94276 | -56.59387 | 2026-09-22 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 41d85ad3-9146-32da-8ff5-bfb04e8a3e50 | -4.50835 | -56.07292 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 733f449a-c6c9-3907-8f03-ccb430704633 | -7.58312 | -57.67541 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bcfbf183-0dde-32c0-92fe-394e8165b3ee | -6.8855 | -59.8605 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21074c83-4ffe-3ed7-bbfe-a22f820dfac8 | -3.04888 | -54.40739 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f17cfeee-901b-372e-a934-c8c42da79a39 | -5.72925 | -53.45972 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1c25fa2-a99c-3074-a907-1430f937b140 | -3.33218 | -60.72281 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6fad3306-4f6e-3903-9e45-167ede635ac0 | -5.88027 | -53.63323 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7db787c6-594c-3ced-bdf1-0f326de144eb | -3.60095 | -59.44228 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9269805-0110-3a97-afc3-ee4e1773fb27 | -9.37327 | -68.65997 | 2026-09-22 05:23:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2e0ab9b-d7e8-39d8-a45b-57193ad88b7c | -2.54834 | -58.01106 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0ab9c19-5957-31b2-9cf3-60f1c24dd033 | -6.64799 | -59.92358 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 7376193a-44ba-3994-bfb5-c5131f127167 | -4.08797 | -62.0914 | 2026-09-22 05:23:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15f16d01-a952-355e-9ccd-c83276d2f0a8 | -6.44278 | -55.63877 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5697bddd-2ac2-3c16-8144-73de8bcd9e80 | -1.09453 | -54.20718 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edef2070-e908-3e46-bd21-0a22c7721a81 | -4.14016 | -50.2252 | 2026-09-22 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f8c634f-720f-3cd3-b4f7-656a4cc58b03 | -3.91311 | -56.21981 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3f85643-d21a-3983-8a7b-798d5581fabc | -4.93839 | -55.81739 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c93a96b-5747-31c7-9662-31c198990b27 | -12.14055 | -47.39311 | 2026-09-22 05:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96dfebf9-01e8-33da-ad60-78fc1c10f8d9 | -6.40045 | -55.26229 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 276d6667-b5df-353e-b53e-f90544817366 | -9.5611 | -66.04592 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f1451c-5f23-31b0-95db-c7fe6c0500ac | -8.7899 | -44.28542 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 64fe89d6-79d5-3a39-a447-72ef0b55ac78 | -3.08329 | -61.17091 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c4ced43d-467d-3cee-ab77-09e54c091bc7 | -3.73117 | -58.86362 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 733f725e-3036-3405-99a6-9f7158f5b39d | -2.92271 | -54.17704 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c15e24b3-20cc-3c77-ab57-1d3bb21e1083 | -12.1426 | -61.17111 | 2026-09-22 05:23:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cf56d9ca-fc18-3be2-8097-6320133a27d5 | -14.75428 | -48.43429 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 841d7b7a-05a5-3f3d-a5b7-cae238e25745 | -4.68216 | -55.63091 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50daaafb-7f20-3540-89b0-5f2e940224f9 | -13.27945 | -51.79002 | 2026-09-22 05:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 40ed9a39-ea4b-3476-8bda-9a1c80a05d61 | -5.37442 | -56.04844 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bec9e408-cdca-30bf-b6c3-0c6e9618fc7a | -3.04947 | -54.40358 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 817c4cb4-dc58-3186-9612-877700de24c1 | -13.87556 | -48.56712 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 66b39730-ae32-342d-b585-18bda24f294f | -6.49593 | -58.38124 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40d304fb-c599-3228-a32b-3d02bc172187 | -6.10442 | -57.67879 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4bd9b0f0-8438-3402-9ae4-9685bc07de3a | -4.25821 | -60.00515 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47cbb5d4-9e1b-3892-81d0-91c28caf36e5 | -6.10724 | -55.68935 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6e046fb-65bf-38f7-9f73-65401b2e09c7 | -6.07889 | -57.62485 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 785cc139-2937-3acd-bec6-a8ef8d835497 | -12.96326 | -50.98983 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb58e25d-5f6d-3c83-a95a-dc82608f625c | -10.91936 | -53.94296 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8ebcf44-105d-3c3c-b217-14186f802c21 | -1.93944 | -56.59335 | 2026-09-22 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdd20345-881d-3056-8e16-00b873cee69b | -4.53367 | -54.96879 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab4f95df-ea00-34d1-9a6f-9f39ceb33e54 | -6.1011 | -57.67826 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0c72802e-5c7a-3c3f-bff3-0b5b4b06fefc | -6.83123 | -55.5374 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bad4406e-3725-3dbc-af12-80016a21a7af | -3.68549 | -42.95531 | 2026-09-22 05:23:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ed74ba66-c1d9-3f4d-8e66-46e89a13baf8 | -3.45926 | -58.32066 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 932f6fd5-8ff4-311e-9864-1fd9aa1fb672 | -6.64735 | -59.92751 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| b45c0137-6f36-327a-b748-2b28ff96e070 | -9.55232 | -66.03855 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 352f7966-0883-30c3-99ec-94a3342b701a | -1.32685 | -54.66048 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd234a54-ae90-3240-8593-b42fd61f8490 | -3.23885 | -53.9514 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 68d91731-eeeb-39cb-9d39-2b9e08a98c84 | -3.42223 | -61.29589 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d404bf96-d855-31a9-9347-faacf392f22c | -4.30126 | -55.07384 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9b78ae2-7763-3d2a-8e45-4295c0f9e059 | -5.85031 | -53.52855 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38512bf4-3892-31ae-86b7-4f40de0274f0 | -7.51357 | -45.44673 | 2026-09-22 05:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f80f356-f63f-32bb-8306-a4d6cbb70f7e | -6.73603 | -55.09604 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README83.md)
