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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd403b7a-b260-3d21-8920-539e35830221 | -18.1956 | -56.5483 | 2024-10-12 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.1 |
| a0426f32-2d67-3f60-b2eb-d5b3ea6b60af | -18.1762 | -56.5301 | 2024-10-12 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.5 |
| eb6e33cf-7b0a-3301-a379-c1a0c3feb213 | -18.1758 | -56.5509 | 2024-10-12 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 094770f0-f8d1-34b2-ba8e-f823a33476a2 | -4.10762 | -48.24042 | 2024-10-12 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b0ae656-434f-3dbf-bd58-100609fd870a | -4.10643 | -48.2471 | 2024-10-12 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a096d504-55e6-3a89-9a45-64b2fcdbb50d | -4.10518 | -48.25409 | 2024-10-12 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c8c0901-12e0-3432-8566-f83fb78ee2f2 | -3.70329 | -47.92983 | 2024-10-12 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 094fa868-47b3-3113-9a3f-9cd4e5c1caf3 | -5.50854 | -48.08262 | 2024-10-12 03:40:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fdfc6cc-b6ec-373d-81f1-b2c61e125287 | -5.50742 | -48.08617 | 2024-10-12 03:40:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88662573-0937-3068-a033-c4b29e152718 | -5.50737 | -48.08924 | 2024-10-12 03:40:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af788843-3658-3ab9-9c9d-7937ecdfee4e | -5.50048 | -48.08792 | 2024-10-12 03:40:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3c412f7-cdc6-38de-bb12-8d09fdc420ca | -5.24722 | -48.03524 | 2024-10-12 03:40:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b4224815-20d2-31eb-9d76-21db84c19da9 | -5.24634 | -48.04241 | 2024-10-12 03:40:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 9ec560bd-0c9d-35a8-a7c0-434ab5e7a23d | -5.24602 | -48.04166 | 2024-10-12 03:40:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 93bd66ff-0118-3a8f-9dec-b5badf6d1779 | -5.24519 | -48.04883 | 2024-10-12 03:40:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f92ebce8-63c2-39fc-a7b6-67a0c06f8e0c | -5.24482 | -48.04809 | 2024-10-12 03:40:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| ad749c7a-589b-33ed-bfc9-de153016763e | -5.23828 | -48.04757 | 2024-10-12 03:40:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 404fff95-bad3-3e1b-83bc-b8edaa3a244c | -7.21626 | -38.98381 | 2024-10-12 03:40:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 79650055-467f-3e4d-ac96-a5839a32eee8 | -7.21551 | -38.98835 | 2024-10-12 03:40:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e06064a2-b532-387c-b3cd-35cf8ab9ea63 | -6.71867 | -38.46981 | 2024-10-12 03:40:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 814211db-1a90-3f14-8563-17a5d4813424 | -6.71537 | -38.47025 | 2024-10-12 03:40:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa61d66f-985a-353a-a2cf-4c718164ed29 | -6.6571 | -37.46188 | 2024-10-12 03:40:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 797facdc-1b62-3505-bd7a-cbddae8361e1 | -6.65648 | -37.46574 | 2024-10-12 03:40:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9266359b-27a7-3f1b-85d7-b947b038bed8 | -5.9346 | -43.34197 | 2024-10-12 03:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d71bc062-67e4-3309-8215-656a0acf70c2 | -5.92952 | -43.34103 | 2024-10-12 03:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd47014a-a8a5-3d92-b023-18c4b9ad5d74 | -5.92901 | -43.34396 | 2024-10-12 03:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 406c660f-7b2b-3215-a677-6279d97a9fc4 | -5.58408 | -43.25847 | 2024-10-12 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdecde14-4f28-379d-8c18-84c97d998b56 | -3.42115 | -43.34723 | 2024-10-12 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c475c8a9-0e5c-3b4a-8e19-35aee01e052a | -6.48607 | -43.69619 | 2024-10-12 03:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8fe1a75-f153-3f74-9b95-749971474d82 | -6.48596 | -43.87791 | 2024-10-12 03:40:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b292eb37-0e4a-3718-a711-2e7833e87658 | -6.4854 | -43.88112 | 2024-10-12 03:40:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ff7229a-67e5-3de4-a87b-b0e28157f90f | -6.48094 | -43.69512 | 2024-10-12 03:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95c1400d-b685-39bf-b2b7-46196bbc05cd | -5.86442 | -35.31572 | 2024-10-12 03:40:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2aa8a72d-31f6-32ac-9836-9d88fd3cd165 | -5.86109 | -35.31519 | 2024-10-12 03:40:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 36f192a7-07e9-383a-9fe3-d8196b8c3247 | -7.69455 | -34.88789 | 2024-10-12 03:40:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dab8d8bf-0a7e-310a-9cac-063f7adf1a61 | -7.69122 | -34.88737 | 2024-10-12 03:40:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08a07ab6-5655-3657-a11a-5716a48f86e0 | -7.44669 | -35.19547 | 2024-10-12 03:40:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 27909493-0308-37f4-a060-9fc2d7248c95 | -7.44336 | -35.19495 | 2024-10-12 03:40:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d3593b39-62b4-3f4d-82b0-7d75e9f310b3 | -6.09409 | -37.06839 | 2024-10-12 03:40:00 | NPP-375D | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63647179-c286-3462-bbe1-e470943ea28c | -4.82866 | -37.83832 | 2024-10-12 03:40:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4db83da3-9cc1-35d5-b0bd-72ea00ced2ca | -4.82503 | -37.83773 | 2024-10-12 03:40:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6824271-d7be-3d34-b6cb-4b00059921c7 | -4.72347 | -37.84435 | 2024-10-12 03:40:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 02408a94-c19c-3ae8-b507-9ae0f668d323 | -4.11973 | -38.42593 | 2024-10-12 03:40:00 | NPP-375D | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f05de09f-27a8-308c-8b3c-bc92bcc124e7 | -5.37232 | -37.77913 | 2024-10-12 03:40:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dcfdf932-a861-37bc-bab0-971e060de3cb | -5.36873 | -37.77853 | 2024-10-12 03:40:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0322c9ec-33dd-3d11-85af-bbae0e7dd35f | -5.27889 | -38.14666 | 2024-10-12 03:40:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 70116ddb-897c-3be3-bcb0-ec2a71f67625 | -5.20949 | -37.8853 | 2024-10-12 03:40:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f53b7531-5e7d-340c-8cc7-a5f3c3a2414b | -5.17779 | -37.98756 | 2024-10-12 03:40:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0bfe5ae5-eec2-3279-a532-93d3c420b17f | -6.60766 | -37.94397 | 2024-10-12 03:40:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 438e8387-de79-3a51-9628-0787f8fad5ae | -6.60406 | -37.94355 | 2024-10-12 03:40:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0571d299-7960-39c1-97fe-692352bb28c7 | -6.60342 | -37.94747 | 2024-10-12 03:40:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 17869b74-18ce-3764-ac93-956a4eebc1d4 | -6.45087 | -38.82093 | 2024-10-12 03:40:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43053163-62b5-3e97-b4a8-6035b53512be | -6.44712 | -38.82034 | 2024-10-12 03:40:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 74819542-594f-3757-8d72-1b767a0b7171 | -6.44681 | -38.81784 | 2024-10-12 03:40:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3938e7a6-c7f7-3823-8d1a-1ce769f25866 | -6.44337 | -38.81974 | 2024-10-12 03:40:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b60225c7-ba3e-37f8-a654-4e0cf9f98a28 | -6.44306 | -38.81723 | 2024-10-12 03:40:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1214708b-d4e6-3aba-823f-9712c4511cba | -4.7801 | -39.77598 | 2024-10-12 03:40:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9502ad93-7f5d-3698-b272-265c20e78c87 | -3.88229 | -38.51281 | 2024-10-12 03:40:00 | NPP-375D | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3bf75e51-ba4a-333d-a25c-63b1d22cca1d | -3.80526 | -38.6496 | 2024-10-12 03:40:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dbdd0326-689e-35b3-8884-67de72374868 | -6.3984 | -39.73719 | 2024-10-12 03:40:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 39bc86f8-031a-3d6f-976c-48cc58cb2754 | -5.6921 | -39.06239 | 2024-10-12 03:40:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ae9c4ecd-396a-33a7-b2f6-6e5718fa40bf | -7.1384 | -40.07164 | 2024-10-12 03:40:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 71de5ddc-d0b3-38c3-b39c-628e10a19201 | -7.13439 | -40.07103 | 2024-10-12 03:40:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6015e426-e5e2-37c6-856d-2126abcc457b | -7.09001 | -39.9346 | 2024-10-12 03:40:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 04b9d50f-eb0b-3d3c-bd29-cdb30d640eaa | -7.08604 | -39.93397 | 2024-10-12 03:40:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b00e55a8-4b5a-34b6-9b7f-5d17605d8bb7 | -6.51715 | -39.68971 | 2024-10-12 03:40:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8cecc279-794b-32ff-8c3d-6a707d064eaa | -6.51373 | -39.69147 | 2024-10-12 03:40:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c9cf4035-a91c-390f-ba6e-d1bec87adf10 | -6.51322 | -39.68899 | 2024-10-12 03:40:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a47f492-4300-3f77-995d-1e728065c284 | -6.51236 | -39.694 | 2024-10-12 03:40:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4003f95b-30cd-34a7-a255-6cb8cd24e7ad | -6.50978 | -39.69085 | 2024-10-12 03:40:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 66465cff-75b7-306a-bb22-e9590d62c49c | -5.39709 | -41.24453 | 2024-10-12 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 53670673-7a29-3fe2-9d29-81a632dbfb8f | -5.39591 | -41.24239 | 2024-10-12 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 02c48f5d-29a2-3fc9-a3d4-91a3d7663d9d | -5.39337 | -41.23935 | 2024-10-12 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f2ba56be-6533-323f-8034-5f2c861750de | -5.39222 | -41.23724 | 2024-10-12 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e86b082-df22-3c2a-8b9b-58e413a0b7ef | -5.39146 | -41.24165 | 2024-10-12 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae6126a7-792e-38ba-b53d-355565046fc2 | -5.19075 | -41.28749 | 2024-10-12 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51098513-cda4-3dd6-9d0e-3d5370a2076c | -5.11823 | -41.68578 | 2024-10-12 03:40:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 74c8ab18-a044-3815-8fe7-a7a5c19f8ff5 | -5.11742 | -41.69052 | 2024-10-12 03:40:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 0cdc6a96-f026-31f0-b905-3b0ef7067a42 | -5.11281 | -41.68975 | 2024-10-12 03:40:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d561e972-8858-3f99-ad43-b97acc35cc6a | -3.93309 | -42.40731 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d1ad8fbd-e9ad-3109-9762-45ddb7065c1d | -3.93216 | -42.41282 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 0d755ddc-4c73-3850-8d41-2929e12815aa | -3.93123 | -42.41833 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 96adb33b-ff68-322d-8406-3332966de1cd | -3.9291 | -42.40096 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 00ce730e-7822-3ff4-b0f8-75e5a2345853 | -3.92816 | -42.40646 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d3f7a80c-57d8-384e-9d66-2985cd112550 | -3.92723 | -42.41198 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1ebfa8dd-2766-3883-8859-301931e4f9a4 | -3.9263 | -42.4175 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 472f1956-8d54-3c0e-8d99-1b17736dc40f | -3.92536 | -42.42303 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c5ff5bbf-f3c5-35e2-b0b0-3a59693f858c | -3.92417 | -42.4001 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 129e5eda-e13e-3007-88a8-a8cd31388768 | -3.92323 | -42.40562 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9dc8b5a2-0488-3c17-9937-79a399a93de2 | -3.9223 | -42.41115 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 9af101eb-8e66-3c5d-b418-0c5d168a45b1 | -3.92136 | -42.41667 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 936f4a1b-886a-34be-977d-dbab754f6bbf | -3.92042 | -42.4222 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a92947ac-e2d8-378f-ad08-57fa4cc0dc31 | -3.9183 | -42.4048 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5579e737-d7ef-3790-9079-3e560b2e3288 | -3.91736 | -42.41033 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 39d76ed5-cd75-3b5d-b812-d7d3f1a0635d | -3.91734 | -42.40342 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9dae430e-7db1-3e33-bd81-7ed588af819e | -3.91644 | -42.40897 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b748b5ed-2ac4-39fa-b673-30794a60d8c0 | -3.91642 | -42.41585 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| ebf372cb-319f-3e75-ad85-46e8f7269916 | -3.91554 | -42.41449 | 2024-10-12 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7727a298-a8b7-32d6-9b6f-a812787d7065 | -6.16423 | -42.69514 | 2024-10-12 03:40:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1ba31f39-208d-303e-9b95-79a960f6997c | -6.15848 | -42.69949 | 2024-10-12 03:40:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |


[Clique aqui para ver as próximas entradas](README36.md)
