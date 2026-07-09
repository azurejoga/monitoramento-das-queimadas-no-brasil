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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb69750c-27c3-3fa1-9437-361de67f1c4b | -21.7617 | -56.301 | 2026-07-09 15:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 443946e7-e59b-32b8-874e-e4dce038d8b4 | -10.3382 | -50.0405 | 2026-07-09 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 637a091c-5a12-31a6-9752-a705493c8a72 | -13.2635 | -45.1575 | 2026-07-09 15:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 95212236-89dd-31c4-90a7-eec389413535 | -11.6664 | -46.362 | 2026-07-09 15:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| cedf9f76-18bf-3d7c-878d-63b8472b6f23 | -13.2978 | -54.3241 | 2026-07-09 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| d27eca57-9967-3703-8141-488ffbb959a9 | -13.2975 | -54.3448 | 2026-07-09 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 172.7 |
| 8107097a-8efb-3a3f-92a4-065fd43acb19 | -5.5907 | -42.7164 | 2026-07-09 15:40:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 140.9 |
| 52dc488c-25dd-3281-9b2a-a75da365bdad | -8.6923 | -54.5468 | 2026-07-09 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 5951b8d4-072f-342e-bb79-5b24e0728b20 | -5.5909 | -42.6929 | 2026-07-09 15:40:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 256.1 |
| 120cef02-d3fa-3eab-b9f4-0455eaaefeb5 | -6.0515 | -47.7314 | 2026-07-09 15:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| f2b01e54-996a-391d-95b5-e4c1a4357316 | -13.2635 | -45.1575 | 2026-07-09 15:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 7a3bb8ba-3e6d-35cd-a9f8-f6027ab62a85 | -11.6664 | -46.362 | 2026-07-09 15:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 771b53d9-4cc9-38d9-b1be-6c6ffdbc5a4f | -13.2975 | -54.3448 | 2026-07-09 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 299.1 |
| e0115c33-a39e-3827-b88c-e13344585458 | -6.0515 | -47.7314 | 2026-07-09 15:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a66806c9-e156-3488-93c6-44284314dd54 | -21.7617 | -56.301 | 2026-07-09 15:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 158.8 |
| d1914eff-aae2-39f1-844b-02c1be444f72 | -19.6562 | -47.5886 | 2026-07-09 15:50:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 857b188d-04fe-3cb8-afb5-0d3b09428a46 | -11.666 | -46.3846 | 2026-07-09 15:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| cadff410-e6c5-30a8-91eb-b74df461351d | -10.3572 | -50.0386 | 2026-07-09 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 1e98ff29-9896-3b53-803b-c98ae94116de | -13.2978 | -54.3241 | 2026-07-09 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 1474450c-bccd-319e-8d19-3c67298da0fa | -10.3382 | -50.0405 | 2026-07-09 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| a8b1965e-0955-3af1-9663-4f58d5c3673e | -19.6365 | -47.5698 | 2026-07-09 15:50:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 149.5 |
| c5bb2815-2661-338c-9a80-fe5885a83e5b | -13.3163 | -54.3634 | 2026-07-09 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 0dcc3c0f-d6a4-3ff6-918b-a049928d78ad | -11.666 | -46.3846 | 2026-07-09 16:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| df83973f-4a4b-3c8d-b238-4e49749747e8 | -5.5909 | -42.6929 | 2026-07-09 16:00:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 256.3 |
| de17b27b-3389-365a-96f2-ae7b864ac906 | -13.2978 | -54.3241 | 2026-07-09 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 6421e002-7fc5-3ea2-b0d4-416d995e701f | -21.7823 | -56.2976 | 2026-07-09 16:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 93629a91-1818-3141-8524-30e6ef03f81e | -13.2975 | -54.3448 | 2026-07-09 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 215.6 |
| fdebbd9f-d264-3781-a987-76f4a2e21a23 | -10.3572 | -50.0386 | 2026-07-09 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| bfd50007-c1a9-3233-a67c-cf55c05a04a3 | -10.3382 | -50.0405 | 2026-07-09 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 5a49d225-7c75-3477-9063-af9b070c488f | -11.6664 | -46.362 | 2026-07-09 16:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 15e1c62f-c5cd-34f9-81dd-7686f3c8cb3d | -19.6365 | -47.5698 | 2026-07-09 16:00:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 1f386448-b2d2-3094-8b57-eac3ee6ce22f | -13.2635 | -45.1575 | 2026-07-09 16:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| f726c8e6-6cd2-3dc6-b8db-cfe357294b86 | -13.2978 | -54.3241 | 2026-07-09 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 0c82aaf7-1acc-3f80-af6b-450e0f92c036 | -19.6365 | -47.5698 | 2026-07-09 16:10:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 0765e9a6-311b-321c-8418-fca361bd44f9 | -13.2635 | -45.1575 | 2026-07-09 16:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| ff02ec09-26c7-3a94-b964-403ae4f9acb4 | -10.3382 | -50.0405 | 2026-07-09 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 6fa3adc5-f982-30df-89b7-d9477a1f8a21 | -10.3572 | -50.0386 | 2026-07-09 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 3bbb9d40-7d7f-3b8e-98f8-75118b086683 | -11.6664 | -46.362 | 2026-07-09 16:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| fccc57d4-35ef-3a2a-9fa9-2e14537f6bc2 | -10.338 | -50.062 | 2026-07-09 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3f8299c3-730e-34c5-8cee-1118a764267e | -13.2975 | -54.3448 | 2026-07-09 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 180.1 |
| b8bf7138-57fb-3530-83f9-5a7f20eedb82 | -12.1387 | -57.2151 | 2026-07-09 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| eee3b2ff-425e-3988-af6a-ab8e7c42fd9f | -8.6923 | -54.5468 | 2026-07-09 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d2672575-a420-33d0-bf06-ab4e5f3b246c | -10.3572 | -50.0386 | 2026-07-09 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 95e682b7-eaec-3af9-a28d-9cf37f0403e4 | -10.338 | -50.062 | 2026-07-09 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 983835d0-c2e8-3c68-9c29-5330a1a447ec | -13.2978 | -54.3241 | 2026-07-09 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 74bb9f65-99b7-3a9d-a960-12989fa3d74b | -13.2975 | -54.3448 | 2026-07-09 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 0d3f7a87-46c8-3dfe-ba92-ec875b360ad9 | -10.3382 | -50.0405 | 2026-07-09 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |
| c292a12f-25fa-398c-ba72-95a8a54b200d | -21.7823 | -56.2976 | 2026-07-09 16:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2e063adf-54f1-342e-b3b7-04b7bd96b441 | -12.1387 | -57.2151 | 2026-07-09 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7115365f-5465-3d93-a003-f2b47587cafd | -13.2978 | -54.3241 | 2026-07-09 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| a3e4794c-b037-3452-94d7-c8c23ada48b8 | -10.3382 | -50.0405 | 2026-07-09 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 5e9e8006-cba6-3e2c-84df-ef239e514267 | -12.1387 | -57.2151 | 2026-07-09 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| fc975fb9-59f2-36d9-bb2f-79633170a0bd | -10.338 | -50.062 | 2026-07-09 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 7f0b688e-4b19-36b2-acae-8697834e0591 | -10.3572 | -50.0386 | 2026-07-09 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e5b3b7f4-7857-33a0-b556-e53d236e2cb3 | -13.2975 | -54.3448 | 2026-07-09 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 364ae675-10f3-3732-9d87-2e5525dc33b0 | -10.338 | -50.062 | 2026-07-09 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9423ed65-3fdb-3b9b-a8e0-496231715748 | -13.2975 | -54.3448 | 2026-07-09 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 154.1 |
| eec963c1-cc0d-3def-a070-d73102367d38 | -10.3382 | -50.0405 | 2026-07-09 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 95e58114-3677-3ccb-b041-ac72e122df4a | -13.9553 | -53.8984 | 2026-07-09 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 52a1cf10-6920-33ec-b5d5-51dd57675ca4 | -13.2978 | -54.3241 | 2026-07-09 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 62fd6fb2-ccb8-3db3-b63e-ebb3184045a4 | -12.1387 | -57.2151 | 2026-07-09 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |


