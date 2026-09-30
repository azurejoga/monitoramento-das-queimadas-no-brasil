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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e450fc9-3f85-3105-b203-2f3d528e1d97 | -18.49574 | -45.1436 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b728fea8-9f02-3850-abe1-a11f755d1eec | -18.23621 | -53.03334 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 150bc72d-3c3f-3a19-9e13-538fec912832 | -18.10301 | -44.41073 | 2026-09-30 04:36:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22feb1dd-13b5-3921-ba45-753b9b8b246f | -17.13159 | -52.1322 | 2026-09-30 04:36:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| eda85d84-7832-3f88-99ca-c512a99089e9 | -18.89708 | -43.80618 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| be2d2aed-ca89-3dcd-b032-48eb5bdd595f | -18.5935 | -43.44052 | 2026-09-30 04:36:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 43607f7b-6ef7-3828-8944-4fdc199c113d | -17.92019 | -44.40065 | 2026-09-30 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a55ede9b-b5b7-3edc-b51e-b064ad89d4a1 | -17.84237 | -44.34269 | 2026-09-30 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38b53f26-d103-3562-ac1b-0424228e8031 | -18.49225 | -45.14308 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f564b6f-d2ed-39e2-ab45-79909eab77e8 | -19.83962 | -45.01913 | 2026-09-30 04:36:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 876a479b-95c9-3d4a-b843-77d8bef3a5b2 | -19.34149 | -43.72878 | 2026-09-30 04:36:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39e8ccfd-1ed7-3030-8bdc-691d3480b388 | -18.59282 | -43.44563 | 2026-09-30 04:36:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3841e1e2-d86e-3797-9f92-f4e9eb279feb | -19.25051 | -46.68422 | 2026-09-30 04:36:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5273b274-8cc2-3d2b-a7bc-4089de4e82f4 | -18.07687 | -44.36322 | 2026-09-30 04:36:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e403c68a-2520-3906-a987-1f4e67feac7f | -17.34366 | -47.06144 | 2026-09-30 04:36:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4882a7c-f2dc-3739-af6c-48a653239232 | -18.27932 | -53.05441 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1e579521-bfef-3bae-ab89-3837240da263 | -19.2642 | -43.75801 | 2026-09-30 04:36:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7416e9eb-870e-3a5e-a9c8-3020cd7b2720 | -18.49865 | -45.14814 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc4dc936-eeae-3273-99bc-8f7b6ef4d5a7 | -18.49924 | -45.14412 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 662a1b6a-39ec-39a1-a9e1-b81b80808557 | -17.12762 | -52.1314 | 2026-09-30 04:36:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c186b9eb-bcbb-37f1-9e14-b2cad5261c4c | -17.58522 | -47.47454 | 2026-09-30 04:36:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef019f49-a376-30e2-bc99-1691200ca7cb | -18.51143 | -45.13395 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 807fce7c-8b41-3c29-89c0-d4da4d5fa151 | -18.26623 | -53.0557 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b9dad379-a7a1-3d88-9810-3c12d3db9f05 | -18.22625 | -42.3154 | 2026-09-30 04:36:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 19085bc9-7151-3f21-91bd-756a43525fd1 | -18.2752 | -53.05356 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 549090e3-c600-3389-ac22-0edfd512badd | -18.30358 | -43.31919 | 2026-09-30 04:36:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b6071434-a634-3f14-b970-bfd9f8e24fae | -18.78733 | -47.35813 | 2026-09-30 04:36:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afbbb904-13a4-3573-a4aa-0d13f2b3c759 | -19.24994 | -46.68794 | 2026-09-30 04:36:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddb53a6e-4d2a-3b30-a818-6aba063da407 | -17.79315 | -47.17114 | 2026-09-30 04:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 939410f4-648e-32c0-ac74-48ab66421a66 | -18.23357 | -53.02473 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4299a5b7-8ce1-32d0-8dfe-73138bf418ec | -19.53506 | -42.93178 | 2026-09-30 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 32730959-1ea8-3cd4-9334-da09620e73a0 | -19.26112 | -43.75264 | 2026-09-30 04:36:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a7d0228-c97a-39c6-aa99-7f2be8a15b59 | -18.28627 | -43.69624 | 2026-09-30 04:36:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c4c6cf72-63ae-3668-9067-2d21ac7c920a | -18.68305 | -48.6309 | 2026-09-30 04:36:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 554eaaed-3607-3cc4-b574-817862ccf762 | -18.50214 | -45.14866 | 2026-09-30 04:36:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 485792ae-587c-3571-88f4-6af5ff37e024 | -17.12364 | -52.13064 | 2026-09-30 04:36:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 47e43dfd-26d9-31d0-8a17-349b11810b81 | -18.10722 | -44.40696 | 2026-09-30 04:36:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6eec6188-1785-3b8d-9ece-27c1dd0b94be | -19.38769 | -44.70681 | 2026-09-30 04:36:00 | NPP-375D | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 174f6307-cbcd-3a19-a92e-8c7ffe367998 | -18.88084 | -43.81387 | 2026-09-30 04:36:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c60dd53-4b3b-3bbc-b3fa-54231b1ba82e | -19.38411 | -44.70619 | 2026-09-30 04:36:00 | NPP-375D | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2606a83-f686-300b-bd1f-471eda2dc7a7 | -19.25387 | -46.6848 | 2026-09-30 04:36:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4b09e16-2427-3e1c-a7bf-ba5ab6830113 | -18.23431 | -53.02086 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7bf6f07-b57e-3493-9bc6-06d28fe416b9 | -18.33704 | -53.07308 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 930e7cf8-1706-3da3-9089-757410d5cacd | -18.25195 | -53.04064 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3e5b98a-fb70-31a9-9c34-ae09a6dee032 | -18.27737 | -53.04195 | 2026-09-30 04:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 387873ee-9dec-33b0-b091-8678ed4e852d | -18.30565 | -42.21254 | 2026-09-30 04:36:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1e2562ed-ae51-3856-8110-a72ddb8d5614 | -18.68366 | -48.62717 | 2026-09-30 04:36:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b07845e-319d-33f9-96a5-6e48e020c938 | -19.86914 | -42.63889 | 2026-09-30 04:36:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 56d7f22e-0dfd-318b-9264-6e6a6267aed2 | -2.57735 | -50.78656 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9deb0aa7-4a1b-30a4-8866-e51f447ae05d | -1.73623 | -55.84457 | 2026-09-30 04:51:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbe1448e-e90f-3dcb-a6d3-31cd293a67cc | -3.22506 | -46.94872 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a79ed061-7356-39ea-8f37-7430a0a3e53c | -0.48471 | -49.13351 | 2026-09-30 04:51:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa08c992-b465-3f0c-b2ff-52387cfa239c | -3.22335 | -46.9351 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c8915f2-cf91-32cc-a72b-f7ecc9fc0b23 | -2.98585 | -51.03872 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| baf19550-1698-3fa0-b0f1-df1ce384fe00 | -1.11209 | -54.09741 | 2026-09-30 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abedbea4-c6be-3f21-8a55-1338cb3c7e5f | -3.03159 | -48.41827 | 2026-09-30 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 66acc939-0d49-3734-95d5-ed52374831ce | -3.10974 | -50.27826 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c6e113d2-2b16-3732-8240-ddf88f2e64e5 | -3.2331 | -46.94543 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4e5cc2bb-f0f3-3d39-8c64-2215ef1ce114 | -2.96926 | -51.03611 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5fa6045f-74ac-3bf6-a592-0f81b3979ed8 | -1.18366 | -48.81943 | 2026-09-30 04:51:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 340d8375-519d-3773-ab34-d2976639c3fc | 1.81764 | -55.62801 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47f9cfcd-9ceb-39aa-9c27-ad5455567fc0 | -1.48181 | -48.90873 | 2026-09-30 04:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 951f352a-17f1-3d91-b309-2e8ebae60bef | -0.92823 | -47.1236 | 2026-09-30 04:51:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc8c3b51-4ae2-3865-9253-bea554ce6723 | -3.23443 | -46.93671 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 95659fe9-45ea-3603-94a8-c3a246988f3f | -3.1877 | -49.24912 | 2026-09-30 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8e53eef-3277-39be-8bb6-01de7b77ccaf | -2.98418 | -51.02782 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75aab85b-8b04-33e3-b073-d4bead8f4284 | -3.15002 | -51.26713 | 2026-09-30 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51f9c950-7c3e-398b-a46f-004064dfde35 | -2.9748 | -51.04408 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ae909562-f3a6-38c9-8298-51ab020ad9f1 | -0.27046 | -48.40856 | 2026-09-30 04:51:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5beb6019-140d-38e3-9cc8-de02b4b9a90e | -3.23074 | -46.93615 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 50e3d1af-2bae-3a71-9a72-3ed6eaa70cd4 | -2.84579 | -51.57524 | 2026-09-30 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e00cb369-5177-31ec-9248-44784ce0fa30 | -2.98086 | -51.02729 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72cbb2c5-e1cd-39bf-8663-d209134f51c7 | -1.48517 | -48.90925 | 2026-09-30 04:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de22fb4e-20cb-38f4-a206-0101c92c7e23 | 1.8594 | -55.60625 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 77ea858d-ce45-3137-8e8c-1cf6dc8b2e8e | -2.97866 | -51.04114 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ca551e24-ad6a-3ff8-bb27-1c849b75facf | -1.04739 | -48.66716 | 2026-09-30 04:51:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 432345f7-25b2-3561-bb7a-25bba5177088 | -2.86835 | -49.63427 | 2026-09-30 04:51:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 906d37bd-9434-38fe-9b00-18dba25d193e | -2.40722 | -48.40071 | 2026-09-30 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1faff9b8-7edc-3b53-88fa-a44010eb46e6 | -3.24629 | -50.1233 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab2e7bc7-c928-36ca-9d5a-970cd8923055 | -2.98308 | -51.03474 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c51048e1-b1e1-3049-a640-d0646e84846c | -3.2681 | -50.13712 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a2b7188-ac7e-34de-9f83-07692316cc04 | 1.85959 | -55.637 | 2026-09-30 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1fccedba-82d8-345d-a83d-4986d492dea0 | -0.84516 | -48.72349 | 2026-09-30 04:51:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| daadb62e-f819-3804-9ff2-37a506db64f7 | -3.26756 | -50.14057 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c76eb0d-e257-38c7-a9b1-d86b5d7cce61 | -3.22136 | -46.94822 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a96c2cd3-eb06-36c0-bbc6-87f7e5c49e36 | -3.02873 | -48.414 | 2026-09-30 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 749537f5-2224-3b01-be56-fefadc8b0a5a | -2.49757 | -54.89074 | 2026-09-30 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 054d43e4-5800-3bde-b5bb-d7cb4e03be75 | -2.97414 | -50.40461 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 230e6db9-e019-39ad-8d52-21b03afa6747 | -3.2314 | -46.93178 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc2ab824-bf64-3865-9645-4d75f45d7cc9 | -3.14937 | -51.03593 | 2026-09-30 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c8435a8-bc36-38d3-beed-5b9efb4c7ea6 | -2.37957 | -50.40601 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4272a4b-fcea-39b8-a11a-f6e82bceae74 | -3.23679 | -46.946 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9d0191be-031b-3b46-8ee9-9cc5703764fd | -2.26618 | -47.87037 | 2026-09-30 04:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11b84d10-e000-311f-8fcb-528f32dd3da0 | -3.27141 | -50.13764 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e333f128-843b-3717-9dac-cb3731d56789 | -2.84522 | -51.57877 | 2026-09-30 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cebf07f3-f479-367c-b74d-5ad018b3f267 | -3.41595 | -48.33814 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae60c11c-688f-343f-b120-9698fc695c15 | -3.41941 | -48.33867 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d84c3e5b-0e1d-3d00-b7c2-e8778c95444d | -2.96704 | -51.02866 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc8144a5-0ee1-3980-8fcf-742ae84f4095 | -3.22345 | -46.94209 | 2026-09-30 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d0fa8b0c-1451-3784-b08f-38f382c5f5e9 | -2.97811 | -51.0446 | 2026-09-30 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README40.md)
