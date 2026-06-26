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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35423e6f-c4ca-3b25-883d-2a49a6e8c58f | -8.14032 | -47.88136 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90e0a79b-855d-3f6c-b515-5b9ddb01b9dc | -7.62773 | -47.30109 | 2026-06-26 04:51:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58b145f1-fba3-3f00-9ac0-5ff95d0419db | -7.74397 | -44.61687 | 2026-06-26 04:51:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c78b4c74-e1a7-3b57-954b-a02c9cab0498 | -10.36425 | -47.34365 | 2026-06-26 04:51:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1e2466a-dc95-33b3-8449-3026bb866599 | -7.62462 | -47.29582 | 2026-06-26 04:51:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 300588ac-e95f-3558-81c3-873358381f0a | -8.13227 | -47.88464 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 465a2e06-0feb-304c-9382-3dd8e8127600 | -12.86886 | -44.33449 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 444db7d8-656b-3216-af2b-0f0eba8f5b58 | -9.91166 | -45.52791 | 2026-06-26 04:51:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9050d41b-f559-3e17-9a22-07f08156aba5 | -9.89447 | -57.39793 | 2026-06-26 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 776ffeef-be22-3bcf-8d75-9b1fbdff1a1a | -8.13965 | -47.88578 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 22aacb01-60f5-3afb-ab18-853f8778bdd7 | -6.93554 | -43.67447 | 2026-06-26 04:51:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 699c5468-4c1c-39ca-b4c8-8906dabd0cf8 | -11.51564 | -54.25459 | 2026-06-26 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 227baf24-5334-3089-ae20-2e15c2e72ecc | -11.54385 | -48.26549 | 2026-06-26 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62b055b5-16f1-3096-869c-a920805c9d66 | -10.39054 | -56.76128 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 833df5fb-7efa-39d1-8b42-df684b2806b8 | -9.59393 | -56.91974 | 2026-06-26 04:51:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b349a38-5d21-35bb-ae60-5d6b133f3005 | -10.83631 | -49.38696 | 2026-06-26 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0e0c81f5-9dc1-39a8-90e0-eda55c5ec39e | -8.1353 | -47.88958 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b3923beb-c324-3184-b0a9-3ed5a8d0d620 | -11.77727 | -46.44328 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e81d5f13-c961-3711-95c0-278dd795b8c2 | -10.78233 | -54.10229 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3f438c1-ba19-3055-965e-4b430e265462 | -10.38965 | -56.76641 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92159c6f-5d28-3b1f-9238-9286c2f3dff2 | -9.89569 | -57.40274 | 2026-06-26 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4422daa-3ddf-330d-b465-d6de779b115d | -9.48212 | -57.31864 | 2026-06-26 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba9596d8-de6a-34d0-b590-ad1b6d6f47d3 | -11.00911 | -55.08538 | 2026-06-26 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1c21ae64-f626-359f-b6d1-bc828a6762df | -10.39535 | -56.75687 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 31f13eae-ab80-3fc4-8bc4-4247a4d13dde | -10.36104 | -47.33806 | 2026-06-26 04:51:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad302a6b-b1ef-3799-81dd-6d1adc1af214 | -9.91146 | -45.52915 | 2026-06-26 04:51:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8fccbbcb-72eb-3971-88e1-fa0d7305dc82 | -7.73511 | -44.17835 | 2026-06-26 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fec27539-cd1a-3f21-8d4d-46350a727ca1 | -8.85639 | -46.92397 | 2026-06-26 04:51:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 883a6e1c-c2c2-3a90-a27d-5d01f516573a | -11.91067 | -43.77885 | 2026-06-26 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62f6164a-c73d-3635-b231-98be78a6a1de | -11.21044 | -54.33689 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e0fb0ef-98e5-3613-ac96-1e5dab3ca62d | -9.59331 | -56.92333 | 2026-06-26 04:51:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 395c54c3-2e67-355e-9e86-914b234c08ac | -9.91207 | -45.52485 | 2026-06-26 04:51:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aef8264c-6d29-354a-bee4-34f226514e87 | -12.51862 | -48.28055 | 2026-06-26 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12a89878-2f35-3680-83cf-b5229a9a8df4 | -10.62104 | -47.14499 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3f32886-e80d-30a3-8d0f-46a8bae2e7d0 | -10.27175 | -48.30487 | 2026-06-26 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 261e779d-0ccd-3690-80c3-695a9d0e3574 | -10.39447 | -56.76197 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| dfd26e55-b516-323a-88ce-cbce622468c6 | -13.08589 | -48.1761 | 2026-06-26 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16183ffa-f115-3f56-b98d-7b8eb1e2ee2f | -6.50742 | -42.22088 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 70ddeb99-726f-3d46-b318-63a39c42fa3c | -12.52175 | -48.28588 | 2026-06-26 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e19c1758-16b6-3b7a-ab58-75215ed19926 | -5.43309 | -49.2998 | 2026-06-26 04:51:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98f435d3-6320-36ee-b4c9-5ff486e7c9d8 | -10.13034 | -52.11058 | 2026-06-26 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a8cd4a7-f083-3dfc-9f3a-5375434ba095 | -9.18729 | -45.32033 | 2026-06-26 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6781aa0-605c-32e3-bea7-cf2899f667aa | -11.38065 | -47.81794 | 2026-06-26 04:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0f4bb7b-501f-35a2-ac94-c3e63fae291c | -7.7485 | -44.61758 | 2026-06-26 04:51:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38782f59-da67-38e9-9912-8a443191231b | -9.40761 | -50.67608 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a6ed7d2-601e-303e-a884-5c650b5e5bee | -12.8719 | -44.34505 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a4947de-8eb8-374a-881a-f6dc45f54c11 | -8.85924 | -46.92684 | 2026-06-26 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c406f1ed-cf4a-3867-b417-da46a153c3b4 | -8.23052 | -47.12089 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 285e9eaa-eb3c-3c44-a314-4ba7ef91ddaf | -6.25493 | -49.88121 | 2026-06-26 04:51:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3194caa2-a8a6-3b78-8581-658efc511460 | -12.76217 | -44.493 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c805d12-cb4d-34d2-9dd5-e4ff24920647 | -10.90533 | -54.12253 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec02dadf-26d8-3af6-9e81-bb6708c818f8 | -12.44039 | -49.58066 | 2026-06-26 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2cbdadc-bae4-3ddb-9d34-01c71b5bed30 | -7.56919 | -45.87907 | 2026-06-26 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8116baac-c805-3250-93dc-2ae963a71c80 | -10.82015 | -53.52826 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8593422f-b5ff-3444-a22f-76fbb2b962ef | -13.08976 | -48.17667 | 2026-06-26 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e1c7083-b666-3513-8482-0efe372b7fd3 | -12.75725 | -44.49234 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 77495cfb-0e2f-3485-9f65-74b730c120f9 | -7.7398 | -44.17897 | 2026-06-26 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0b9b97a-4816-3708-8969-0a1fa291a333 | -10.93759 | -56.85822 | 2026-06-26 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2135ad18-2d2b-3b0f-a950-ce08c834fe14 | -9.40817 | -50.67251 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40fe4e32-4e6e-3cae-a3f0-a8a9c01c4a44 | -12.04651 | -55.45335 | 2026-06-26 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eed67604-eacd-3bb3-b5bb-cacb3345339b | -11.89202 | -51.72964 | 2026-06-26 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6df0845-fb7a-35e0-991b-e78d6effc65e | -9.07502 | -44.76551 | 2026-06-26 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9260070e-daaa-3eac-a911-f2bcf39b4780 | -10.1602 | -56.60237 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 535a40a5-61bb-3ece-8135-448e1384de80 | -6.94107 | -43.66984 | 2026-06-26 04:51:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50034364-2733-3e44-8cf6-02052d845904 | -11.51886 | -54.25452 | 2026-06-26 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 808c7885-5af2-36f4-bead-164aa0275bea | -9.78675 | -56.94213 | 2026-06-26 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c9c45dc-3093-3b20-8652-c7c004b52a10 | -11.51543 | -54.25395 | 2026-06-26 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a93727c-5d1d-3eff-8cb5-2563f039d8ae | -6.50785 | -42.21776 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a861f0d4-3ce0-30b6-b462-ec1e1a2695f8 | -10.57785 | -57.31969 | 2026-06-26 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c08dc7b8-9fff-32c7-9a55-d27cae46ce78 | -10.77832 | -54.10637 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2cbfbd0-539e-31b8-ab97-3c60b2ba8d0f | -8.44257 | -51.48295 | 2026-06-26 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 821abce5-e54b-3142-8d4a-0f1512834bd3 | -12.87168 | -44.35268 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6a2caca-8d81-3ad4-ab68-d6bb5ca91884 | -10.77894 | -54.1026 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bba5388a-2448-33b8-9ce6-6d9f103395a3 | -11.38594 | -47.80863 | 2026-06-26 04:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6dd2961-0261-3712-aad7-d308f5f9c5b4 | -11.80762 | -56.9983 | 2026-06-26 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cff8f9ba-d6d9-3758-a131-b2415d3491ce | -11.80552 | -56.98754 | 2026-06-26 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7246f548-1e29-3ef3-95d9-6b43a9394b6f | -10.16323 | -56.60814 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1303ef6-e0cb-35ac-bf6c-70527e82b618 | -10.75496 | -49.10974 | 2026-06-26 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c56be534-d5c6-35f6-8137-678cfb981591 | -11.25331 | -43.31739 | 2026-06-26 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b8d8f133-00fc-3232-87e8-c1aa6384f567 | -12.7474 | -44.49099 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 80936789-9521-376d-b291-a0e7eeb92867 | -9.40427 | -50.67555 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 336064c9-10ea-37d4-85ce-27e1a7d1e98e | -10.39271 | -56.77218 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19456e98-8fb9-3283-9078-2be28ccfcaad | -12.86844 | -44.33278 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcd5996b-0ff4-3bf6-bb38-62ddd33e124c | -11.77781 | -46.43935 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb39828-6a0e-3280-b62a-e2bfd92e123d | -10.38587 | -56.71803 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcfe4f60-4c02-3da2-9a5b-b66708c777e4 | -8.67857 | -47.85234 | 2026-06-26 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3026c194-c95f-3164-be7e-9d8913d4b5d0 | -7.74225 | -44.17659 | 2026-06-26 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11642294-87cb-3967-86ea-c2e18d723522 | -11.47647 | -47.34676 | 2026-06-26 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b72c465-6922-3a31-88d3-0a4df335fa9f | -11.36534 | -52.95291 | 2026-06-26 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 41ff3828-7984-3619-865b-2d178fba18eb | -9.36389 | -50.54454 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| feffb978-00c9-3e86-85a4-bac8a8e97a88 | -6.98149 | -42.89344 | 2026-06-26 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0285128a-3ce3-3dd0-bf75-071d163acee8 | -9.01067 | -47.99511 | 2026-06-26 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43ca6f0a-b577-3348-9597-c9d0261c5515 | -10.27382 | -48.3027 | 2026-06-26 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32ab4d9b-c971-3623-9f9c-7659f8657c25 | -5.72335 | -49.10389 | 2026-06-26 04:51:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7443b8d6-fa7d-31b5-a92e-310fc12c7f8d | -10.80401 | -55.86233 | 2026-06-26 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76215a05-a9b9-3d18-857b-a889ec7e1b71 | -7.7405 | -44.17383 | 2026-06-26 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0ab1672-c5c8-3fd1-80b1-9c1df528f16f | -10.82352 | -53.52881 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6db8cbb-53fa-38f3-8859-ea804ddfad85 | -10.12372 | -52.10951 | 2026-06-26 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12396072-f4a6-3c6b-93af-6ec352257681 | -8.01063 | -49.64895 | 2026-06-26 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e5a289a-be72-39d5-a0ab-d5028ed19106 | -9.49517 | -57.3171 | 2026-06-26 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README14.md)
