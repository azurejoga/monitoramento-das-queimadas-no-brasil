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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7967774-f8bd-3699-a951-60c2f2da8ba0 | -5.59096 | -46.33762 | 2025-08-26 04:21:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21013c39-711f-314a-a328-819932a1e1ec | -6.89325 | -44.41801 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a51fa556-da41-3142-9a4b-f65da439d9e3 | -11.1591 | -44.77304 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ab48e787-0894-33ba-bc9d-e190e6c842da | -8.37887 | -48.02582 | 2025-08-26 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a6e994cf-2ff5-3bf0-a841-5bd3a90c7921 | -6.92555 | -52.77511 | 2025-08-26 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 571ec3e2-41cd-3e9a-b0d7-76d5b97310ec | -8.11529 | -47.12632 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4d99529-3561-3c46-9212-13086be00d6a | -4.62815 | -41.40065 | 2025-08-26 04:21:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d840f453-3779-3871-8624-e63ab1ce90d3 | -5.4675 | -42.59024 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 41bfe54f-4fee-3708-b0b5-03d610fbf1e9 | -5.05969 | -45.46669 | 2025-08-26 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4bca9da-a9d9-3c3c-b82e-5e869d2f7d2c | -11.3121 | -43.28668 | 2025-08-26 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb5ad800-1a84-335f-a81d-327cd2e97c52 | -11.14902 | -44.74946 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbdb01c4-1c1a-3c67-af6b-d29fc80dbd41 | -10.7139 | -47.11048 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6223145f-98cf-318d-844b-49006b7bc57a | -6.89439 | -44.43241 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 459dcb65-0ab9-330d-bf6a-206e25b9a896 | -4.96281 | -55.8209 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4986d1f2-fcec-3fa5-91d3-72511ec8275c | -11.08898 | -44.77253 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6dea511-40f5-33b4-b2a1-779123b4cdb4 | -7.08193 | -46.06199 | 2025-08-26 04:21:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebd4ac2e-328d-3868-8fb6-15f5a3bebbdc | -5.70583 | -45.53227 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e375aff6-902a-3bbd-be50-fa4e57e2b776 | -7.21587 | -44.43301 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d115790e-7a4c-36ee-86df-bbf30c269d44 | -9.1045 | -46.0682 | 2025-08-26 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90329a4f-e059-38b0-b063-3f2e58545f00 | -4.64996 | -41.41898 | 2025-08-26 04:21:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 961fee73-ad27-33de-aa49-3289cb5415cf | -7.6311 | -45.22957 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da2d1ba2-f3bb-30ed-b9f6-ae3d12759f07 | -9.31008 | -48.2644 | 2025-08-26 04:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 735471d4-a031-36c9-beab-eea5ab8740eb | -5.78818 | -46.13395 | 2025-08-26 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7999768-5aa8-32af-962e-96a19144e32a | -4.485 | -47.66864 | 2025-08-26 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de39da0a-af74-3e25-85b5-7275c5bff12c | -5.7064 | -45.52872 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 293cf2aa-24d7-3857-8fc3-407b9a8e4c78 | -8.708 | -47.86701 | 2025-08-26 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 85fc69ea-0f40-3a9c-a967-e6758bbebcbb | -6.18419 | -44.15315 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99227706-071d-3714-a02a-5e8c74e4c3cd | -10.72248 | -47.10065 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 565f4765-326e-3399-b66f-d0eaf81ee10e | -8.1077 | -47.32699 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3a7b771-def3-3928-bed1-e13ab37a33d4 | -5.4005 | -45.15145 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 181f01ac-654d-3846-8e58-b1cd534f1993 | -7.66109 | -42.66339 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6657f821-fcd8-3475-98ca-e3510f23fd9a | -9.57681 | -48.63538 | 2025-08-26 04:21:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbcc7286-5ae6-3d1d-810e-c1f07dc43e15 | -8.39658 | -47.39234 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60288ea4-102c-3cb1-8915-36950b4d9b59 | -6.86773 | -45.65139 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fb18759-99dd-33b9-8569-1cdac6ec89dc | -5.86616 | -46.41183 | 2025-08-26 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3e23d3f-8e2c-3dee-a9ed-a07d54ae8f83 | -8.38734 | -47.42689 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a02c79c9-d199-3966-b1c7-f8ab92a62141 | -11.16186 | -44.75516 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 04372b4e-1643-3e1d-a1c6-3240fb12620b | -4.85248 | -42.89075 | 2025-08-26 04:21:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| cf973e46-a891-338d-a4d5-a93ec79c211a | -11.10513 | -44.75685 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2596855-35fc-35e9-8904-d01c19ea275d | -9.31437 | -48.26086 | 2025-08-26 04:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2c28053-f8ec-32fb-8c50-9ca0ad4afc9e | -6.51749 | -44.20567 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ece6f4b7-100b-3b5b-a5a2-bbe5b597c55a | -6.19416 | -44.15475 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59f41b51-fd86-386e-a072-f0e6e2c99abe | -6.2019 | -44.14887 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3942dc1c-ec4c-39a0-bf34-62ad6d1f0399 | -10.72588 | -47.10121 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d62b08a6-70fc-351a-b5ba-11314782c6f8 | -5.57115 | -42.62082 | 2025-08-26 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9a6f26c5-d9a4-3f15-b68d-0d13fa9bb8be | -10.81902 | -46.37495 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f42044db-44f4-3d75-b2a5-cf2c0e69eb19 | -6.34552 | -43.65907 | 2025-08-26 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb8f69d3-2bcf-342e-ae44-4e1145c1d6f1 | -9.32503 | -40.21397 | 2025-08-26 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c683150c-bc57-34c6-84e3-5d3a7378f617 | -7.66516 | -42.66006 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 79fa6833-5bf5-38ce-a5d0-f5fcc447d219 | -6.94482 | -44.17628 | 2025-08-26 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12bf699b-dd2c-3867-9f0f-aaaf001df45c | -3.54422 | -49.49309 | 2025-08-26 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2713f01b-5770-3ec3-9046-b2ac0d88a582 | -11.28467 | -44.99333 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec0c1976-21c1-34e8-9750-7d63fca8466e | -3.43185 | -49.0521 | 2025-08-26 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 906f642d-bf68-38a4-915d-fc2e2afbb686 | -9.2504 | -56.90403 | 2025-08-26 04:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1c224c5-9c33-32c0-ad72-b81bc3cab455 | -6.9487 | -44.17332 | 2025-08-26 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 158e1285-5c9f-3cd8-820f-9e376eede90e | -7.61114 | -45.22641 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33dc9e2c-6c1a-3858-be0e-10b67186d23c | -4.59678 | -43.31904 | 2025-08-26 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82d29381-5fdd-3a37-9921-d6608c03b9df | -5.10518 | -43.16673 | 2025-08-26 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e8bbd82-4d0c-3f86-9c10-6c50d768d19b | -6.88274 | -45.65343 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7e1db61-5fde-3082-8b33-54d4ba3af942 | -7.30929 | -44.52604 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 919ccfbc-1675-3a9c-998b-a3bcaa2c6376 | -8.24609 | -45.08842 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb21d7c0-8c0e-3daf-ae28-3099ace77c44 | -10.53891 | -46.78979 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06b71232-344d-3bdb-8ec3-0af8a759c775 | -6.88665 | -45.65048 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4e0c07c-2fc8-3441-be73-94c3aa445f40 | -5.10574 | -43.16318 | 2025-08-26 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 065617a1-c6c1-31c8-8274-e5d751befaa2 | -8.07183 | -49.6671 | 2025-08-26 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5cd808e2-75e7-32ed-8079-0d54efe2f20e | -6.29251 | -44.77431 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acc6dd7e-d195-308d-9adf-45f6624f85a9 | -7.73661 | -51.13983 | 2025-08-26 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e022ba2-800b-3da7-8c42-dec4456c8324 | -9.56615 | -55.37461 | 2025-08-26 04:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d557c25-fddc-34b6-9e0e-b78feace5a89 | -8.07434 | -44.99325 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11473c88-10e8-3b56-8a6c-de0bd7c8bc8b | -5.97651 | -43.33722 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5af5bcf1-30c1-31a0-be3e-ceb271433a49 | -7.87162 | -47.95175 | 2025-08-26 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c56eff05-75f0-3a59-8b20-8a461794c41e | -5.46465 | -42.60866 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6b644ef4-07a5-3d02-87dc-312b2ab16908 | -5.89359 | -43.39739 | 2025-08-26 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa499df7-0fd4-3081-af2b-ba8d8071300c | -4.78647 | -47.28191 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9060eea7-02bd-3763-a8ab-f5c2507e80e1 | -8.24554 | -45.0919 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d2f91dc-4e8e-3401-bd56-a6af5031dc3d | -5.78641 | -43.60825 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2652d79a-8567-3bb2-9e5c-cfdc2cbd5b5a | -7.58204 | -47.49392 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 782198d1-1cb5-307d-8dd3-1d0eb0fccc5d | -4.96367 | -55.81593 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0225f6cb-d13f-31ab-a2bc-1cbadaa3a074 | -6.36704 | -46.48645 | 2025-08-26 04:21:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1545ca9-746c-381c-9e9d-fc8b00dacec1 | -5.5944 | -46.33818 | 2025-08-26 04:21:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4140b08-ee16-315a-8d47-e2de60f0280a | -5.49995 | -41.41507 | 2025-08-26 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fb731aff-3c53-38f1-9aea-ecf3f8b4a511 | -6.29994 | -43.76371 | 2025-08-26 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b559939a-bf4a-3872-b838-2911c7fc333e | -6.52183 | -44.43764 | 2025-08-26 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| def2ce7b-4e06-3d57-8808-0dd83aebafbc | -7.01779 | -44.38063 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbeea7a7-29d6-368d-bf7b-5a2b5a74ba5c | -3.24963 | -46.90662 | 2025-08-26 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a81b4be9-8aee-3799-bcae-14535aaca7fd | -11.28189 | -44.98925 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 675b6628-7ce8-311a-8351-787896617db9 | -6.69936 | -42.97123 | 2025-08-26 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a8e33599-3eb4-39e3-8366-19fdd9f10af4 | -6.80961 | -42.82193 | 2025-08-26 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d8d3a626-cf77-3f6c-9831-82f97fa9b586 | -9.64735 | -40.59199 | 2025-08-26 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a3943f51-36d7-38ae-84dc-98a6df38d4f1 | -6.90541 | -44.40567 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8a09c98-50e4-3d8c-a688-6201bd34f9a3 | -8.07388 | -49.66953 | 2025-08-26 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 321fca70-1656-3853-a50d-21a505a53bce | -7.52951 | -50.54016 | 2025-08-26 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f23f8ab-2007-37dd-809c-d59e91cdb16c | -9.16868 | -40.6006 | 2025-08-26 04:21:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1affae3d-838f-31f9-9dc1-e3df3645bbae | -6.8817 | -45.64995 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a05cd780-d21c-361c-8de0-319de05248ec | -4.96812 | -55.82749 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 70a5b835-0fbf-32bf-bb17-83d990cd211d | -7.20868 | -45.31261 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f825be0d-1c13-3b94-af17-15bffc904f0f | -6.02866 | -44.00378 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccb70f1f-91d1-3b22-8126-32356289e8f9 | -6.6536 | -53.18662 | 2025-08-26 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69e100d0-e89f-3c11-921e-62b4f603c283 | -3.9795 | -51.05578 | 2025-08-26 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ea88ba1-0bdd-3dd0-a45d-ea0f6c279919 | -8.07768 | -45.0152 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README39.md)
