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
| 40ef0a6a-08f3-36f0-a961-582983584625 | -3.16562 | -51.49351 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0835c53a-e7a3-35e2-8ddf-0d5f62eac6bd | -4.13908 | -46.35205 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 83f0f204-8734-3b7b-bd3b-a8a80506f2f2 | -3.27049 | -50.02108 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fd62fc4-fc03-379d-a8ad-495bf50186a9 | -3.20327 | -51.02703 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 844eb6d9-33c1-3c4e-a772-777588b74640 | -3.65552 | -50.79957 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d67d1b76-f6db-3501-bb88-2f8cf0edf0bb | -5.45989 | -40.97904 | 2025-11-18 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e4ac411a-a287-370c-b9cd-b9290fcbe8d8 | -2.82657 | -48.54869 | 2025-11-18 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62820f99-4379-30f6-97d3-7ec1f1161a21 | -3.30325 | -50.07219 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14035ea4-99d2-320a-8f2e-9e2045780dd4 | -1.42653 | -48.90381 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bedbe7d3-aa37-32c4-9b9d-8e09205c6772 | -4.27366 | -44.24505 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27e04fea-3672-3287-9995-2763127d33a7 | -5.18571 | -46.0719 | 2025-11-18 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f2b0936-7299-33f2-8106-67068a3c707b | -3.4802 | -51.57886 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da808d95-8f8a-34a6-931b-506270e0c123 | -3.20979 | -50.9211 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fc546b3-7806-3f47-9860-8d562e18fc73 | -1.9213 | -48.79593 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 732e8908-1db4-33a8-911f-a70028f4c57c | -0.99159 | -47.07666 | 2025-11-18 04:48:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bc6461ba-00cc-3d43-876b-d43159e202fc | -2.82047 | -48.45427 | 2025-11-18 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b42ecae4-d7e3-3211-9180-916f492a0131 | -3.49884 | -50.44245 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b880b91-ec0b-307b-a5f5-d0bb30f7e42c | -3.23513 | -50.50312 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bb84b8a-30d2-3f0c-975a-e6c9ab988cf6 | -6.32644 | -46.12653 | 2025-11-18 04:48:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c59672f0-c204-34ca-b854-9aeb6883de5c | -3.23622 | -50.49622 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8914022f-8664-31e4-bbbb-2046c357740e | -5.03774 | -46.82694 | 2025-11-18 04:48:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ceb86921-a061-37cd-988d-d4e24698804b | -2.82735 | -45.42196 | 2025-11-18 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b6c16020-2ec5-39e8-9b94-40afe3b053f9 | -5.46757 | -40.96554 | 2025-11-18 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 30647b78-8632-3aa9-8e5c-292df7def4dd | -3.53673 | -45.25618 | 2025-11-18 04:48:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0108e18-b1cb-3b89-ba1c-d399ad8f4307 | -4.67225 | -45.79782 | 2025-11-18 04:48:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2db7674-0fe8-373e-9346-8d04001c6dbe | -2.52774 | -58.03154 | 2025-11-18 04:48:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62da86e7-1c67-3e89-bb89-d744b79eae45 | -4.97026 | -41.85066 | 2025-11-18 04:48:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 877fa843-db76-3eea-83ef-1ae7299297ca | -2.51182 | -54.8165 | 2025-11-18 04:48:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c1e9fb71-e7e6-36a4-835f-a49a831ffd97 | -3.79006 | -51.1021 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee753198-a727-3be0-a888-332d612a3dc3 | -3.24177 | -50.50416 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58ffb1c6-0f8f-3451-b485-b67d5b373307 | -3.35023 | -44.39064 | 2025-11-18 04:48:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3b035880-c6f6-38b6-95d4-768affa987d0 | -1.76614 | -47.26196 | 2025-11-18 04:48:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7aebe53-efc4-3cbe-b100-e80e65fcc4cd | -3.00027 | -51.00592 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1dc63d1-c630-382e-bdb6-7b27be192fc0 | -2.32545 | -50.90381 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33a8e16e-5976-3578-a51c-6eff0af88159 | -1.9241 | -48.8 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 125986ee-8ae4-3daf-a3a1-820d1d79f6bc | -6.44389 | -43.81818 | 2025-11-18 04:48:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b98749d3-3380-3f5c-97d9-52f728123301 | -6.41741 | -47.43981 | 2025-11-18 04:48:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| befa88f4-d9b6-335f-bcc3-bcdc5601efe2 | -2.88485 | -51.43108 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2cc2990-ac7d-390c-9878-031d71a54480 | -3.07991 | -50.35159 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6c04fb8-9efc-364c-a166-b4dc82e54f41 | -4.27236 | -44.25351 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60b65214-c171-3d96-97c7-b0311323fe66 | -5.51712 | -49.56422 | 2025-11-18 04:48:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54962dfa-7fab-39d0-ab5f-7dde3ee51a04 | -4.19804 | -44.23835 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdf865b2-1520-3ac1-8c53-0e1e4413269b | -1.32685 | -49.32027 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9fe1871-741d-3943-84d1-b00f173933b7 | -4.01553 | -44.26198 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5ce76d3-5df3-3cd3-961d-0e2bc87dfa4e | -6.41056 | -47.19988 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d38363fe-edde-3b86-8a31-270ce7f667a7 | -3.52515 | -50.34058 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 836f1887-facb-32a9-a64f-825fffe572ed | -1.09147 | -54.20778 | 2025-11-18 04:48:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f19234db-5ac0-3e81-bc6c-49da65791abb | -3.18063 | -50.65377 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab925dc0-7f25-3866-a218-146ec2d2183c | -3.14665 | -51.31971 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ced0e92e-bd08-33c8-bc4c-13a94aac8a54 | -1.91738 | -48.79895 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 396a68e4-0c65-3ed1-ad39-19d1f19a3f69 | -1.6144 | -55.85186 | 2025-11-18 04:48:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 098512d8-b4c6-3377-880b-2104368e026c | -3.59214 | -43.60427 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4843831f-b0ec-38d8-84d3-6f14091af798 | -4.5296 | -46.416 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c721e3b4-7de0-3c95-ab88-c4fed12e49d8 | -3.07244 | -50.22683 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 538c58a9-2acb-34f9-a141-f4f6c612cdd8 | -3.14188 | -49.89481 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dd71662-3c64-38c3-b5b8-2871a05b6c77 | -3.49252 | -50.33194 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a088be8a-30eb-3bfa-ad2f-9bc3a578f2ac | -4.02332 | -45.54254 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d2ba8e2-92b3-327e-8ad1-6e04a17c1f99 | -0.9766 | -52.44573 | 2025-11-18 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7a1cb7a-b282-39f7-998a-03be5c1f1ee9 | -2.47546 | -50.23558 | 2025-11-18 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cf3bd20-e3af-38c6-a350-41f32d47b1b9 | -2.51684 | -47.81139 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 360f2457-e0ec-3707-85fd-73a392f901a6 | -3.30657 | -50.0727 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4d53dbb-abfb-3d96-ad1e-e6767be87a43 | -2.47748 | -50.24296 | 2025-11-18 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82548b39-be6b-33d1-bf41-36888d73f229 | -1.33682 | -49.32183 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3557cbfa-f247-369e-9f31-8a739f79244b | -3.58827 | -43.59908 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa3b4cd3-f6a3-30bc-b1f1-a876908d4bf4 | -1.59556 | -55.83228 | 2025-11-18 04:48:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0be33156-8de6-3c28-a968-ec60366929df | -4.70657 | -46.30589 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afaf0b9e-d878-3262-b68c-2afef51ba7a3 | -2.4716 | -50.2385 | 2025-11-18 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e5f2451-fb39-3dc7-b621-7e4739171150 | -2.94576 | -48.58912 | 2025-11-18 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7809ebc7-fd62-326f-ad89-8a3dae56eb65 | -3.89677 | -47.93485 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 112108e6-24ab-33ba-aa4d-3afb3fe3e777 | -3.67045 | -50.25378 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0921e203-9565-336c-8e44-2a39f0af7fd1 | -3.26945 | -50.7782 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b873b0e-dc22-3199-bfa6-804b2ed94120 | -3.40713 | -50.18799 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8422e538-4b3a-3de2-a28c-b252fad124a5 | -3.04562 | -51.14563 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a71603f-347a-3314-9710-5a9d01c52db0 | -2.6911 | -49.16836 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 775c834a-a149-3f6b-8fcb-bfb0e05c53de | -3.40472 | -51.12339 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0cdedfd-57d5-3450-b1af-68948a15a4dc | -3.40049 | -50.18695 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27bf98c0-60c9-384e-8691-718e04ac47c2 | 0.12805 | -51.42142 | 2025-11-18 04:48:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a998e72f-5e73-3fad-97a8-d4df3e65526c | -4.13382 | -52.12339 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cc4441c-f99c-3818-a9e2-d10fd9de8bb4 | -4.9698 | -41.8539 | 2025-11-18 04:48:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 27275862-4345-33fb-8fad-c499b3a821d5 | -3.897 | -50.10936 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af82fa52-dc58-3265-b547-13dc3775d0c1 | -2.53552 | -58.02438 | 2025-11-18 04:48:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c702386-3e04-32ec-ab5b-9458687e0b8c | -6.31352 | -43.78191 | 2025-11-18 04:48:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f7e3e36-071a-3a3b-85fb-04dd907f0b05 | -3.02777 | -47.84315 | 2025-11-18 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0dfe72a8-64af-3cfd-84ac-ef1cf7b27d81 | -1.6742 | -53.19463 | 2025-11-18 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a1e8f6c-235b-3937-9d2e-f870145bc443 | -2.83274 | -46.72402 | 2025-11-18 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa882039-d71a-352d-8631-64f331d4ef86 | -2.99639 | -51.00888 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e3491fc-67e2-3ad3-b9bd-6e1626a6a624 | -3.438 | -52.19171 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f3aadb4-2da7-35f7-936d-a489523762a4 | -4.6169 | -47.25908 | 2025-11-18 04:48:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8011bac3-272c-3459-9489-f1175f093cb8 | -3.43821 | -52.73672 | 2025-11-18 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 890cf83c-aed3-3886-ac21-969a75108494 | -3.69864 | -51.67554 | 2025-11-18 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98634c69-43ae-333d-a150-3614970d86cf | -3.06981 | -49.47127 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3ed663c-5ae7-3934-b16c-270e778fdf4a | -4.45249 | -44.21656 | 2025-11-18 04:48:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a88d9c05-92c3-3983-b7bf-87506913ebc9 | -3.60542 | -43.60818 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ab6deca-10dc-3544-8ed4-3e080df7b5f1 | -3.309 | -50.16498 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a1268c6-3a59-3959-b4fe-cb0121d914b9 | -4.72361 | -46.37724 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e79024d9-bdc8-366e-88b0-8c6ac58c06a5 | -3.02748 | -44.47536 | 2025-11-18 04:48:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb862597-a7d1-3ab0-8878-c72b02645e35 | -3.08359 | -51.26288 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 015c95d3-c862-3ba8-9a9d-e143bb51ba3d | -2.91851 | -47.85093 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db2f5152-85d6-3ed3-9913-f049e3ea293f | -2.51458 | -54.81337 | 2025-11-18 04:48:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 74a8b7ca-f931-3b83-9d22-558a8cc22883 | -4.1316 | -52.11556 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README40.md)
