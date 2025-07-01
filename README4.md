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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcccaf79-5479-3668-86d7-31622538b46a | -10.8832 | -56.4367 | 2025-07-01 03:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 255d5ffe-1eb4-3d89-9db3-4a08863a26fa | -10.8832 | -56.4367 | 2025-07-01 03:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 2f6b31b7-0b34-3d0b-801e-e80e02fee859 | -6.2945 | -43.6659 | 2025-07-01 03:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 9d2f06f7-848e-3a82-a87c-2ed202249f4f | -6.2038 | -43.3475 | 2025-07-01 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| a6a22e70-7daf-39f0-b6fb-50caef159c84 | -6.2943 | -43.6891 | 2025-07-01 03:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 12319d97-717d-3eb6-ba6c-263d7812ca04 | -6.2945 | -43.6659 | 2025-07-01 03:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 864aa8d3-7112-331b-bb1f-46739485afdd | -10.8832 | -56.4367 | 2025-07-01 03:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 4f73e34b-e252-39f6-be50-5dc3749327c3 | -6.2943 | -43.6891 | 2025-07-01 03:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 71730e86-3ca5-3972-9bf6-ca9ebee596be | -4.38268 | -41.91895 | 2025-07-01 03:30:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd4bbe99-3a09-3176-a12c-6bb2931c3e4b | -4.38363 | -41.91699 | 2025-07-01 03:30:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30f2fcf7-f9cb-373b-8e7d-16b4bf395bfc | -4.38339 | -41.91492 | 2025-07-01 03:30:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9d628d3c-30cb-3c7e-b276-d4d90041f246 | -4.38433 | -41.91292 | 2025-07-01 03:30:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 78d7a02f-0a8f-35bb-aa16-d93502d0e9ac | -7.61998 | -45.74931 | 2025-07-01 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4ef74aa4-b3b3-36ca-beb7-427f0667b483 | -9.32019 | -40.20868 | 2025-07-01 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 838e3744-ebef-3d12-ba3e-66efc206e323 | -7.61854 | -45.74981 | 2025-07-01 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 94f94223-d573-3207-8c85-b7dc928e0c45 | -7.61721 | -45.75651 | 2025-07-01 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 68c0480c-5b5f-34c1-aaeb-00eb252d7579 | -10.68143 | -47.20893 | 2025-07-01 03:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9da3f9a8-6643-3c30-bfbe-34223695083a | -7.6242 | -45.75759 | 2025-07-01 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3198d9a6-c3c8-3caf-8bd5-d98e522dd237 | -7.61869 | -45.75608 | 2025-07-01 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| dd82331f-28fa-3e5c-958f-388634065a06 | -9.32113 | -40.20353 | 2025-07-01 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a0f70927-a180-3ebc-ba2f-a905e520884e | -7.61173 | -45.75486 | 2025-07-01 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d126fde4-0882-36d5-a9f8-33d058006660 | -12.80304 | -40.3493 | 2025-07-01 03:32:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a863982-ea42-39d7-8739-0ec70f14e4df | -6.48145 | -43.74339 | 2025-07-01 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d81c8ef7-d18b-3c0e-894e-4ae2814f5f19 | -10.68854 | -47.21068 | 2025-07-01 03:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70e843fd-956f-3be4-bed9-3308df95b06e | -5.57209 | -45.2216 | 2025-07-01 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bd117aa0-f924-34f7-9087-7295850586ef | -14.13326 | -46.34274 | 2025-07-01 03:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b321eac-7d02-39aa-9361-8b24eafbe958 | -14.20923 | -45.52274 | 2025-07-01 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91783af8-7708-3a18-9beb-2cb45fc13466 | -14.20564 | -45.51585 | 2025-07-01 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ff93468-1fec-32e1-9c9a-7876047f4ab1 | -15.92342 | -43.52242 | 2025-07-01 03:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd9b386d-6d2c-3576-b398-cd78267ddbb3 | -12.02524 | -47.77378 | 2025-07-01 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fe5d756-71aa-3002-8baa-269bbb987df2 | -12.01906 | -47.77012 | 2025-07-01 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 20073e9f-5bea-328b-92c1-abb0151ab300 | -15.91952 | -43.51457 | 2025-07-01 03:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b584c7ba-dcdd-3c22-801f-ca4b5dd3c829 | -20.22126 | -41.01081 | 2025-07-01 03:34:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f5e82388-9a15-3100-88f3-1164288103e3 | -12.01803 | -47.77217 | 2025-07-01 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a5154bd3-fbf2-3ccc-bc13-46418219520e | -20.59674 | -41.22431 | 2025-07-01 03:34:00 | NPP-375D | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6b616164-1a48-370d-902f-13709a215635 | -12.0165 | -47.77938 | 2025-07-01 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ec9d4708-c53b-3491-b113-7d3d0469f108 | -15.92279 | -43.51851 | 2025-07-01 03:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12016fbf-673d-3b26-96fa-88abbfc7cdb4 | -17.20137 | -44.3291 | 2025-07-01 03:34:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6df544f3-35b1-3af6-a3cc-0b590f7f0ae3 | -14.13226 | -46.34702 | 2025-07-01 03:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 412adacb-982b-36e8-a209-195e891872ec | -14.20311 | -45.52143 | 2025-07-01 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70aeaa4a-2dee-3f14-a836-4cb331e33c00 | -18.061 | -44.49629 | 2025-07-01 03:34:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5199e933-6714-34e1-88df-68ee2ac43ed9 | -15.9221 | -43.52185 | 2025-07-01 03:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 377459ef-4abe-34e3-80ba-b7ad51480a34 | -17.93837 | -48.91926 | 2025-07-01 03:34:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24199725-cf2b-321c-9edd-c5b6d2c1dbb8 | -18.28966 | -44.68501 | 2025-07-01 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 225b5d52-8b5c-3dc4-9e08-3248a348f42d | -14.20463 | -45.52071 | 2025-07-01 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9203bca8-1597-3bf5-88e8-bc25a80a9d4d | -16.43102 | -44.52402 | 2025-07-01 03:34:00 | NPP-375D | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d331aed-c0db-355b-80cf-df487d01c225 | -20.22387 | -41.01139 | 2025-07-01 03:34:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a6f4b6a5-a06f-3002-b855-eab23b4d49b2 | -14.20362 | -45.52559 | 2025-07-01 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d5950b-3176-3f0b-adbb-47ba7301a965 | -17.7548 | -42.89522 | 2025-07-01 03:34:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e11825dc-b18e-3ee1-8fc8-890c51c13b85 | -13.00932 | -44.10131 | 2025-07-01 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0088d1a2-2d1f-3e93-9328-ca0ece773029 | -18.2887 | -44.68598 | 2025-07-01 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5f14d64-c881-3c53-a8f9-866aed689acb | -14.20415 | -45.51657 | 2025-07-01 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1612ffb-5137-34b2-b692-b94f9d30d4d7 | -18.0557 | -44.49487 | 2025-07-01 03:34:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a2a4b47-d9a4-3282-9bb8-6dbbb150c337 | -13.54388 | -43.71047 | 2025-07-01 03:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a454d7ad-c0f9-3146-9564-5e66b984a26d | -15.92348 | -43.51516 | 2025-07-01 03:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54e7c441-ea80-3a60-96f3-3e30380a6f16 | -11.83909 | -47.5046 | 2025-07-01 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 487d8e00-9b55-3027-8cd7-62df767e81a9 | -15.92409 | -43.51906 | 2025-07-01 03:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9eb9b1cf-55c4-3d1b-94bf-831e4dd6c200 | -14.21075 | -45.52205 | 2025-07-01 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e06754b9-8345-3b9c-bda1-85da92575b14 | -14.13343 | -46.34148 | 2025-07-01 03:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 703b2c52-54ef-3608-b32a-d3295f92fa01 | -18.29413 | -44.68704 | 2025-07-01 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbbf155b-4d65-37d8-9719-c7290c47e8f3 | -17.9367 | -48.9263 | 2025-07-01 03:34:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80726153-61ac-3e7c-acdc-5896c75ca037 | -13.01508 | -44.10242 | 2025-07-01 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5f14caed-34bf-3c4f-a77b-52201004bfb0 | -18.45359 | -40.04061 | 2025-07-01 03:34:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 97f30db1-396f-389e-bc36-ebcc729eaecd | -11.83757 | -47.51179 | 2025-07-01 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcf7a515-7951-3d6c-94e7-58db0dbbac7c | -18.28886 | -44.68874 | 2025-07-01 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d131b65-5775-3fe0-a43a-b41eb45dec26 | -11.83049 | -47.50997 | 2025-07-01 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a716abde-547e-30db-bb72-5daa7bddd510 | -20.22538 | -41.01171 | 2025-07-01 03:34:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a9ca07e9-6e78-3396-9da3-fe950ab498a5 | -15.91818 | -43.52128 | 2025-07-01 03:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0ceb270-0e01-3f7c-8fb9-ef513e1d3a8e | -15.91885 | -43.51793 | 2025-07-01 03:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ee47fba-097a-3077-88fa-56e0c602fcd8 | -19.38264 | -40.21255 | 2025-07-01 03:34:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b307eadf-0038-3bfc-acd7-54d053a0c7a0 | -12.0175 | -47.7773 | 2025-07-01 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 964deb6d-59f2-3949-97b3-af16e44e5203 | -21.17908 | -43.97985 | 2025-07-01 03:36:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 31bec6bf-5a31-3524-90b1-dce56dd666eb | -20.80609 | -44.63231 | 2025-07-01 03:36:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a5ea5ea2-4f33-3350-afeb-386a6e55d62b | -20.80468 | -44.63179 | 2025-07-01 03:36:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 60804704-260a-3c0a-bed5-13b915a7d315 | -20.80402 | -44.63494 | 2025-07-01 03:36:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9779c9bc-fa74-3d46-b6e8-6b0610cb4f9f | -10.8832 | -56.4367 | 2025-07-01 03:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ab1969bf-9408-3581-9b23-3573452925ae | -6.2945 | -43.6659 | 2025-07-01 03:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 68fee9a3-d6a1-3d01-bef6-5d5affb171da | -6.2943 | -43.6891 | 2025-07-01 03:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c8a7fa49-aa7c-3e25-833b-6ba0de6b544e | -10.883 | -56.4567 | 2025-07-01 03:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 1bb35dd8-07ba-3071-95a8-c27dbf459574 | -10.8832 | -56.4367 | 2025-07-01 03:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c7b418e5-f717-3699-abdc-fd1132593e8d | -4.89964 | -37.38218 | 2025-07-01 03:51:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d479b54-b68e-3df4-929f-e3efe8e925f2 | -3.9927 | -43.2412 | 2025-07-01 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 76d8f349-7e40-3910-a259-41a1c6ed6c43 | -3.99682 | -43.24187 | 2025-07-01 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 949062d4-22ff-3019-9ce1-086dc7326be8 | -4.89578 | -37.38515 | 2025-07-01 03:51:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dba4f104-bc46-34ff-8480-a5a209118be3 | -3.20905 | -41.84118 | 2025-07-01 03:51:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b9e2893-61ad-39fc-a229-e793204ddef8 | -4.38466 | -41.91125 | 2025-07-01 03:51:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5b5be29c-609f-309c-bd94-b7b281bcdd91 | -4.38391 | -41.91582 | 2025-07-01 03:51:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 04b76f57-613b-3faa-b325-3d8fdb252979 | -4.31329 | -48.08208 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43833b01-bea2-381f-a864-e99190fde541 | -4.32047 | -48.08747 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95636a42-3446-3ef1-b265-88c4c2e4a6d3 | -5.6509 | -46.59658 | 2025-07-01 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb83ff1a-8992-3449-8fcd-3d002a3c4d0b | -6.29211 | -43.69073 | 2025-07-01 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e54cf11a-443e-3f6a-b28e-cd863a8c87e4 | -4.54539 | -48.01398 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e88755ee-7edd-3caf-af57-7152e4388aba | -6.4798 | -43.74038 | 2025-07-01 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e7321590-1923-30a8-ac3c-ba820ee52c3a | -4.31548 | -48.08254 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11e99584-242e-34a1-9590-28e01f7b3655 | -4.54947 | -48.00884 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d891011-6de5-3b55-8323-06ab803c8b62 | -4.31896 | -48.08316 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| baa8b926-2331-3995-8516-fe2921be01c1 | -4.80835 | -43.22857 | 2025-07-01 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7b5d305-920a-3922-bb76-73e3370f0a0a | -4.38196 | -48.07003 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a80d5b9-1ffb-3d25-82d5-a2f504e5f7ba | -4.5488 | -48.01265 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de235a2a-5b68-3f4d-97dc-941ab554f3f9 | -4.55014 | -48.00504 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README5.md)
