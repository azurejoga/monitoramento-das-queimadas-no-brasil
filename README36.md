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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b082df67-c4a0-3062-83d0-97165d935e00 | -1.8369 | -55.35458 | 2025-11-18 04:48:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe58e47a-6190-3893-926e-46a856ef012d | -6.6721 | -42.03878 | 2025-11-18 04:48:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 897f081f-1a32-3255-8988-f17446f49146 | -4.60026 | -46.53424 | 2025-11-18 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1b98ab2-e423-3480-8780-5d210d918f12 | -3.76118 | -51.06903 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afd29cad-db02-39a5-99e7-5354f02e81c7 | -3.16323 | -50.16702 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1584d6a3-bcf1-30d6-9695-5fcb5a4ea0ca | -2.31755 | -48.58951 | 2025-11-18 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb7268c7-d45c-3ae8-bc87-41142546d6d4 | -3.24764 | -50.682 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b00df82-1d4f-3f2b-93bf-6f0c878f5410 | -3.13249 | -50.25402 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f2b296f-4e06-30ad-af3f-0ff7007ec083 | -3.74384 | -51.39232 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14893a21-0968-3175-9bd1-9ede1ed140fc | -4.23348 | -46.34009 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30b6e12c-7e8c-3311-ac5a-54248a64a0c7 | -3.67109 | -50.21159 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7f73291-9cda-3816-88bd-29e8ff2a6056 | -2.85888 | -49.60919 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d1ba38b-a9b1-3300-8eb2-5f79cdb5cb47 | -1.33017 | -49.32079 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9bd6de7-3e59-369f-9328-3fa83ba915da | -3.09352 | -51.37284 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e33d035b-7246-37d9-a2eb-6c2c9006ff02 | -2.53216 | -51.1839 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 90eaa6e2-f486-3301-8105-2de206df51f2 | -4.97505 | -41.85475 | 2025-11-18 04:48:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 868a8c03-c209-37b9-961a-83ca200aaf7f | -4.19363 | -44.23771 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc4e86e0-8274-3245-a345-944a8e38f78a | -3.239 | -50.50019 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b9bace4-fc76-3816-aae4-db5a5da3e7a2 | -5.40546 | -49.80884 | 2025-11-18 04:48:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e831f694-b049-3ffa-be22-f165dab31725 | -3.08122 | -51.09386 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 567bec08-99e9-3e54-8715-9e7566dc2bb2 | -2.49501 | -49.34212 | 2025-11-18 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a84126e-859c-3255-af5f-53a6f0ea690c | -3.67377 | -50.2543 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d92a81c4-e4b5-34b5-b96a-2aa049934dd1 | -4.05038 | -47.50411 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38376440-2aa1-36f6-b3f7-8d213e330c43 | -3.07467 | -50.23424 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6880580-5b8e-385b-a933-298f3b5fe4ca | -5.56853 | -51.20138 | 2025-11-18 04:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8440aaf-b947-3a85-9d05-217259da5bf7 | -2.47491 | -50.23902 | 2025-11-18 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4db30f5-da4a-33a7-a8a0-d6b78d3478c3 | -3.5621 | -51.45378 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e29afb8-d30c-3ab6-9c92-519a283a5345 | -3.32945 | -51.51184 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fed7f94-5c8e-3df1-a151-dfd535ad8911 | -2.77492 | -48.65592 | 2025-11-18 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14227fb8-cc53-3367-8489-2c50eedf693c | -3.17379 | -49.80054 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fcf5a88-3c69-3829-a4d8-12595fa0f29b | -4.67375 | -45.79961 | 2025-11-18 04:48:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c45f5256-3158-3f7a-af68-3cc1304f5ef1 | -2.52442 | -47.80861 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a37d56ff-c44f-32e1-a197-86c59366ca54 | -2.33921 | -55.79848 | 2025-11-18 04:48:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c9b8a9c0-e4da-3d57-9e9a-41616ed63a40 | -2.47471 | -48.22811 | 2025-11-18 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e2dbaf88-4363-3b90-a68f-18d767f0a786 | -3.17325 | -49.804 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6737c5c-70a9-3e11-a49a-c438d316e998 | -4.98077 | -41.85232 | 2025-11-18 04:48:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b69e1811-2c72-3e4e-9c6e-154704fec2df | -1.86934 | -50.96127 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f635b30-175a-3891-8d82-88fd677b874a | -3.18395 | -50.6543 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 244b7600-1d40-3f5c-89d2-4dbec0069c47 | -1.34015 | -49.32234 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 360f8f14-6cf7-38e6-b452-9973a5113722 | -4.18042 | -44.23566 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd3899f6-fc66-3782-9195-9b9d6de745a0 | -4.97552 | -41.8515 | 2025-11-18 04:48:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92865766-efb9-393c-9637-e6fe477311ae | -6.30272 | -43.79038 | 2025-11-18 04:48:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8cf7a8e6-5030-3646-875f-b8a3967dec65 | -3.80189 | -50.1299 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c04725d-d279-3b68-8b7b-4a8be638c849 | -4.18859 | -44.24134 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53ea4280-680c-3470-a55c-3a2b8b6548c9 | -5.95735 | -44.72843 | 2025-11-18 04:48:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a15adadb-155b-320d-b517-de3794072d5f | -3.41747 | -50.35919 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6ae1fb9-bcb4-37a3-8a6b-1d4696d86ca3 | -2.86692 | -49.47149 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd655e56-a926-308d-b628-746576d6ca49 | -4.35238 | -44.34499 | 2025-11-18 04:48:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7696edfd-17de-30de-8a2f-e8f81b1b0f4f | -3.40658 | -50.19144 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27658b6d-aae2-353c-926b-064ef2699403 | -4.27403 | -44.23989 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd2d88f2-ebd4-3129-a69d-0389171e2771 | -6.15613 | -46.10934 | 2025-11-18 04:48:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee340e13-1f33-3a25-bfbe-2b4a61e1ffb9 | -3.64398 | -45.44571 | 2025-11-18 04:48:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8feaa8b-768b-3d1b-a6d2-28622e36c84f | -6.40986 | -47.20441 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b29e6dd-a5b6-3406-ad5b-d2065d777d00 | -3.27058 | -52.47598 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8a14960-b32a-3721-a607-89d50b759453 | -2.91561 | -47.84653 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71001d2a-c737-3d21-9490-d3f3fa191f64 | -5.03396 | -46.82641 | 2025-11-18 04:48:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18eeb88f-e2e9-3584-ba40-d5abb7996f54 | -1.32963 | -49.32425 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1e0ea3e-22f1-3093-b250-96f33edcd4c9 | -3.05202 | -46.99525 | 2025-11-18 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb3fd70f-599f-312c-b917-76704b37eb10 | -3.48049 | -49.59245 | 2025-11-18 04:48:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b6496d5-ddc3-367d-b0dd-a20678fb9cda | -5.21547 | -50.1768 | 2025-11-18 04:48:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4447102f-8d47-3333-99c2-c665cda11eb2 | -3.56257 | -47.30535 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5debe1a0-5b8d-3cdd-9f03-a24821daab62 | -2.91501 | -47.85038 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2033d97-a6e2-31dd-b609-4eafbad15d97 | -3.77165 | -52.39506 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3110361f-7ddf-34a5-8c32-960f18df2a48 | -3.24143 | -50.03788 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 069a8c3d-3489-3a19-9d43-c05b5c997171 | -3.8737 | -51.27972 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89b14db6-97c3-32b7-b8a0-d4c6f02d65bd | -3.49017 | -54.04961 | 2025-11-18 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6365e3f3-2f14-3edc-94f2-ef718a8b478e | -4.64977 | -46.54221 | 2025-11-18 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94a20ca1-05b4-30e6-b45b-aecfc9f0d8be | -4.13981 | -46.34739 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 42080a6f-cd8e-37c0-acd7-c0b9b0a29392 | -3.49089 | -50.34228 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91690e54-a59c-3e03-ad14-d95bdd8be2b9 | -2.51155 | -47.8223 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c2eb842-4318-3de7-8f06-c4b2cb70061a | -3.33578 | -50.27515 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcc18631-6f61-3442-b9ef-d211805c1506 | -4.0198 | -47.41541 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8575f090-f917-37f7-9ff9-29578d1c670a | -3.51742 | -50.34644 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d08e13a4-f1aa-3d87-aa7d-10bcf24906dc | -4.70516 | -46.31538 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4257b26-8de7-32f2-8ce5-1cedb0c51a3b | -4.71476 | -50.94945 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ba725ab-70d5-3210-ae18-e7bbaae090b6 | -2.99479 | -51.06229 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a741e12b-eb04-3ba7-9b57-081f78568587 | -1.8023 | -54.71696 | 2025-11-18 04:48:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24cabfab-7e19-31bd-9e67-369c92ab4c7d | -3.43031 | -50.17041 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38e817f1-dc3c-33f9-983c-7ac940c16b2a | -3.60514 | -43.61079 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f221e17f-51fc-3303-82a9-e4bfd3d76cf7 | -4.70547 | -46.30872 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9344f9b-6e1a-3d46-8a9b-bbae5e27508f | -2.51852 | -47.82339 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d9e0eee-5c70-383d-83f6-5db75df02cf9 | -3.25689 | -50.02615 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eff54b42-bbcb-3c54-85a2-016696609df3 | -2.93855 | -50.38971 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d113cf1-3e53-37d5-815c-c7fdc93b003e | -3.65177 | -50.22624 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f496792-9f50-3771-994d-e9a83903eeab | -3.19658 | -51.00455 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b25093d3-2485-362f-84a6-e8fe2827091a | -4.49862 | -46.69565 | 2025-11-18 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48c5c01d-e2ff-3bd3-b8e9-cc781bc41f35 | -3.49198 | -50.33539 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a97f3ad-3a5a-3901-a56f-43cb93607664 | -2.52477 | -58.02821 | 2025-11-18 04:48:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dde6a886-1cf2-36a6-ac36-88061f202013 | -3.25493 | -43.03729 | 2025-11-18 04:48:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 827e02a4-df9f-33e2-b195-b26e22ceb2fc | -2.5316 | -51.18742 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c968ff80-bd3c-3d1d-b4a2-45c5969c6c8f | -1.80628 | -54.71758 | 2025-11-18 04:48:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 030b227d-2eed-33bb-9885-ca6f09314566 | -3.14443 | -52.17336 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab84f3a4-3245-3d6b-9ade-6be061496d62 | -2.86053 | -45.23103 | 2025-11-18 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6342e44c-9a31-322c-9e8b-1668ed32dc1d | -1.41818 | -48.9133 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b11f97f7-5e2c-3f92-bbcd-92dcc0285e91 | -5.36356 | -44.85915 | 2025-11-18 04:48:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27c8ba3a-7134-395e-9b34-ff85d9eb06dc | -2.47437 | -50.24247 | 2025-11-18 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 304c75dd-b055-3980-b7dc-85cd2f6457ef | -2.8802 | -52.61542 | 2025-11-18 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5df6b9c-f39e-3a6f-aaf2-e0b0949b6cc9 | -4.22892 | -46.34423 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb9e1c48-d56c-3cf4-b4de-d3d6cb62acad | -2.68775 | -49.16784 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c9ea8719-4fa1-35d6-b126-def5069ef538 | -1.97726 | -56.4696 | 2025-11-18 04:48:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README37.md)
