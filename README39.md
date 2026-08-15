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
| ab1cad95-91a2-3d71-88fd-04da92f27719 | -6.62061 | -58.99734 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43f9a6a3-168a-3ec1-86f1-46de10e994db | -6.61891 | -59.05342 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 857f019a-4981-3fa0-88a2-ae7a7d0537de | -3.53225 | -59.02385 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cb8563b-776a-36cb-b2e2-af9bdcdbc07d | -7.68986 | -55.15644 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e1c2f0b-3afe-3c52-8bac-c47324282929 | -7.06069 | -56.5175 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf5142dc-15ab-3960-ae5f-f1f83b01c552 | -7.45828 | -55.30672 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a0294357-2823-3d32-86a7-28fad5df0693 | -6.61266 | -59.04873 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| beea4298-ae1d-379d-bf75-c752db05052e | -7.68712 | -55.15725 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ad53856-f315-34b9-b8c5-4626a8a29b89 | -6.62231 | -59.05394 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a1079675-8f6e-3dfe-a845-d3d3fd0730ea | -6.01638 | -57.83594 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7e49860-2ae4-3fdb-ad91-bdb4a6dd58ed | -6.85384 | -58.9566 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e05d649-df5d-3ff5-9742-1cf853092613 | -6.70857 | -58.94593 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ce11a8a-d164-331b-bd00-2d67cbdd5ceb | -6.14109 | -57.89546 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 275b6fbd-f550-343d-bf78-3ee7bee00016 | -6.79565 | -55.82699 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02da832d-50b3-365d-a783-bce9d891a71e | -6.82691 | -56.44757 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5514343-b235-3871-a4b3-8a950126615c | -3.23938 | -61.16516 | 2026-08-15 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7148571-637c-3f4f-bda4-d7c0345736ca | -6.77788 | -58.74679 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3e5eb3c-b9c6-3a58-ab10-6d2aa8e89c0f | -7.55224 | -61.16874 | 2026-08-15 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c965753-6cfc-310b-ac3d-8c0221d38600 | -6.71998 | -58.94009 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d1da1a1-d3e8-3878-b7b7-3f369a857c56 | -6.82377 | -56.4421 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87a4d4d9-1f00-3137-8a34-5ec4ac71d813 | -6.61662 | -59.0005 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80a8033c-f8e1-31e5-948a-49413a0d8ac8 | -6.59271 | -56.359 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b78d4749-b17a-3cec-9f36-760cea94a718 | -7.55368 | -55.57109 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de2d294a-8939-3694-bde0-d4cd1f7bed1f | -6.62004 | -59.04612 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d1b1af3-03a0-37d4-b0a4-e134ddff53ac | -6.84756 | -58.97457 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4b30ce2-7d5f-32dc-ac76-e4253189a4c2 | -6.58499 | -56.35759 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e73ac9b0-4545-3d4f-b5c1-9b163b8d62d4 | -6.78657 | -55.83276 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8d2b509-281f-3dc8-a8ab-2a1eb9e08234 | -6.59658 | -56.3597 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72da64f7-6667-3f51-ac46-bc4126c50da0 | -3.65913 | -60.74159 | 2026-08-15 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45c977f4-d952-38e8-b6cd-9d574c79f207 | -6.59502 | -59.00465 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 536b6f8a-1204-3dd1-a44e-fbe5dcfdbd0e | -6.96718 | -59.2855 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 459f845c-91a1-32fa-89e5-2d9950593108 | -6.81603 | -56.44091 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b41c50f1-9115-361d-ad1e-65eae58f2995 | -6.61663 | -59.0456 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 561dafc7-2fc1-3e1a-934b-5e85b5ec247d | -7.69355 | -55.16113 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 530b7702-eef7-3eaa-bfaf-e49cf22afd6a | -3.71978 | -55.96635 | 2026-08-15 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d3165b3-e9d6-3936-b660-54d0ba78a90d | -6.96491 | -59.27769 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de9025c8-7ff1-386d-8c6b-65c834731294 | -6.6155 | -59.0529 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d7d22f1a-affc-3ab2-b981-310fb8021d6d | -6.79357 | -55.84099 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2728644-93fe-3ff5-b0c4-7d5e224ba442 | -6.63544 | -56.25985 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f92ec05-6e45-3165-b767-35d478ef3192 | -6.84994 | -56.42631 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80c5eca2-b22e-3eb4-93cb-411bbf15fd30 | -2.64655 | -47.98081 | 2026-08-15 05:33:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fbd5df0-c740-39ad-adc6-d940671c6a8a | -6.61721 | -59.06438 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72e42316-f785-3bcd-8dac-f00f5e8214df | -6.96439 | -59.30365 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18553279-8300-3c3b-ae47-1be7724088f3 | -6.9596 | -59.28474 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 099400b3-dc54-36d9-a9d0-7554e05bdb6a | -6.02053 | -57.83252 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9899e40f-dc5d-3365-ab2c-9c5804bf9070 | -7.55501 | -61.17274 | 2026-08-15 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2fa82cf-e178-3345-b7ca-0523284fff60 | -6.79603 | -55.85205 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3ef6826-2ca7-3091-96e0-c6c246ea9db4 | -6.79305 | -55.84448 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8d11042-cc24-3154-b3d2-2624856ba863 | -6.7905 | -58.75644 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1f04785-7e7e-36b6-a816-f641a49d8047 | -6.85753 | -56.40249 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aac0f0ba-5f46-3d35-9318-4b2f35aa0399 | -3.18929 | -60.64939 | 2026-08-15 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89b2f020-5041-3b40-bd7f-a4f5b93da86f | -3.93447 | -56.25294 | 2026-08-15 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e1f47a9-3be8-3d88-bead-3d4d3947f016 | -2.79658 | -49.57931 | 2026-08-15 05:33:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53999a56-f3e1-36f4-9a4e-d648532ee5fb | -6.95846 | -59.292 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b4b2435-f742-3aa8-9c43-a424c8d191ed | -6.961 | -59.30312 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 344fb07f-3e45-33b4-8df1-a16e8be7c26f | -6.79907 | -58.76938 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a25b6a8-8a91-3a6f-8212-d9d71421e13e | -6.60192 | -56.35046 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d54200ed-46a1-3626-a94e-69b123d8bf07 | -3.51602 | -58.95272 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| adce3acc-cbc2-302a-a91f-7fbb9f0081da | -4.11076 | -50.99221 | 2026-08-15 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 605eb39f-8364-3766-90ea-605feb9b54f1 | -3.74397 | -59.3298 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5fbbaf9-ff2d-33ef-a2c6-1d2bcfc79540 | -8.02601 | -55.12083 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9825988-9a9f-3d4b-a378-9f4d117c1a90 | -3.5924 | -58.62192 | 2026-08-15 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 884625c0-2507-3573-b7e4-7ec83073c697 | -6.96128 | -59.29616 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0219be3-706b-3976-b1b3-4984371a09da | -6.83371 | -56.42873 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8d38977-88e4-3947-8258-20badd944204 | -6.61891 | -59.0759 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1873651-2817-3a7d-b496-d450476e213f | -6.02349 | -57.837 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04007148-d753-3f2b-adb4-7fa8102c727b | -4.31145 | -59.46815 | 2026-08-15 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12ce9dfa-9782-39f2-968d-f82207730806 | -6.71656 | -58.93956 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea922a45-d646-3e21-9ffe-8ac911db2db9 | -6.9734 | -59.2902 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1adcef30-5b31-3256-bd9a-6139f3b12deb | -6.70744 | -58.95333 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd2de1e8-c352-3e30-8d8d-8cf5918ee39a | -2.87522 | -48.85361 | 2026-08-15 05:33:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c2cf754-fd3a-3f62-83e6-21042e0696aa | -6.97057 | -59.28603 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d0515db-01b7-3fc0-8aaf-66653aa1caee | -7.05612 | -56.52174 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 814312de-11a4-32eb-80ba-c6fa2aa0afdb | -6.70687 | -58.95703 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6e98652-ff11-3268-9aea-10be38996110 | -6.61112 | -56.34205 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbc8c00b-ec2e-3072-bcfa-14afbb189729 | -6.74216 | -56.39748 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8eeab961-9e4e-3b40-8d20-d0e3b866d390 | -3.50588 | -57.02057 | 2026-08-15 05:33:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c2a8dc0-ff85-3f2b-887c-2449e108c756 | -14.08214 | -53.67598 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01bf7fd2-074d-30df-acf5-2b286d2b89ef | -14.10538 | -53.70764 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6300535d-e3cc-3e2b-9120-e1fde213302a | -14.49328 | -52.02779 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3335a123-731e-3a5b-b577-809b0b5fa14e | -8.26034 | -57.34318 | 2026-08-15 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 027d0219-c9aa-39fd-91fc-f4966060f2cb | -8.94967 | -60.5653 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54dd8dfd-27c2-3888-b814-89c31fb05d04 | -8.77932 | -63.96317 | 2026-08-15 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1d7bfbf-ffd7-30aa-a402-e5fc0049baf4 | -14.09111 | -54.52119 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84c6406f-95ab-31b6-adba-55576f48feb5 | -9.34608 | -62.35474 | 2026-08-15 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 448350ba-6d20-3973-8e90-17a8e81c069c | -8.61086 | -54.67239 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ddfa471-2aa3-37a8-aaac-602edc175580 | -10.42104 | -47.97507 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6bf48b7-992f-3864-ab2b-d3885a7440d1 | -14.72057 | -52.88685 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e0ee33d-1330-32fb-868f-b1964441954b | -14.43656 | -51.91053 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ef255615-8277-3395-bcbd-27b30c121c1c | -10.62684 | -52.07671 | 2026-08-15 05:36:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f53f15d6-91c7-3c65-aa76-4ead69b89b39 | -8.89443 | -60.55306 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 98eb5c65-1a46-3e63-a5e1-eadcd52f7461 | -11.98596 | -53.4552 | 2026-08-15 05:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43121297-988b-39bf-8ea3-d87cd1a2c85a | -8.96181 | -60.50945 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22dbff3a-7420-3693-aae7-d7a04b14f8e2 | -14.42884 | -51.92662 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2ac04d9-3f37-3d7c-ad5f-c9c3a8cf21f0 | -8.97852 | -60.53377 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2ad3d2a-d67e-31b6-a560-60391aeafb79 | -14.72096 | -52.8857 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1735398b-05a5-348b-8d4c-1544563a6ed8 | -8.78509 | -63.97241 | 2026-08-15 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a35e1077-0a14-3f8e-ad59-7cdc2f9fc082 | -11.11102 | -62.89302 | 2026-08-15 05:36:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35ab79a8-e923-3ca7-b668-895fbed07cb5 | -8.95125 | -60.51138 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eb115ef-35cd-3af7-8c41-133658eacfb2 | -13.42182 | -57.04678 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
