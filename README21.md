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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53d38fdf-08ea-3431-a2be-d3c074bd9b88 | -1.72359 | -53.31297 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41e85b94-5377-3383-941b-3a1d9d6855f1 | -4.0543 | -46.92305 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53801f92-b0d5-37cb-ab1f-195c0be462bd | -4.6756 | -44.042 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ce45e23-d828-3e5b-9b53-69bb903e90e0 | -3.04936 | -47.97318 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 872b3f34-30e2-3ea4-9053-919515999667 | -3.15142 | -53.18061 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d58703cd-8db3-3413-bb09-207de5930f31 | -4.25073 | -45.99464 | 2024-12-17 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1fdaf1e-e623-34cc-9d37-9efda9e06063 | -2.92282 | -48.9581 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7170377a-7751-31cf-99b6-5a46cc10c0fd | -2.14213 | -48.03733 | 2024-12-17 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1812b186-dc27-3579-9e61-711e1f2a826e | -2.05393 | -46.66069 | 2024-12-17 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0f3bca4-ede7-34d9-8598-31a75102ffe1 | -1.72724 | -53.31355 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1970627-73de-3d3a-b892-afcdcb4c9496 | -5.08713 | -43.90728 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3e1ea357-03f0-3359-8308-f75ffa57164d | -3.84336 | -45.86263 | 2024-12-17 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bf53dbd-c477-3593-8f62-eb8f53c9a62d | -4.33712 | -43.55177 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b68bbc49-bdde-3a85-a230-f0e87732f543 | -5.20676 | -43.30056 | 2024-12-17 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ca391a24-93e7-35af-8a7d-3844d1983730 | -3.02482 | -47.83051 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e7ee721-6ed0-3a55-8bdd-1b7287e04a05 | -3.84548 | -45.86053 | 2024-12-17 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64f6306e-4e3d-3a0c-b7ad-5fe8366fce0f | -1.06137 | -46.83621 | 2024-12-17 04:44:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 326668a5-4e9b-33f2-ba76-80c63b737c34 | -1.36956 | -53.4714 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b41c6beb-37f5-3268-88cd-47a2caceb441 | -1.37625 | -53.47696 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 160999e8-a85d-31b8-b8d0-2f495c1af49c | -4.09565 | -46.72811 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bec47d7c-5563-32d1-96e4-348f705775bc | -4.79718 | -46.39909 | 2024-12-17 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8944973d-629c-387d-b6b6-bce6ffa18b36 | -3.87732 | -47.03835 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ce2fb78-816f-3d60-abe5-3c00a2191855 | -4.96603 | -43.71593 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3511d4b-f803-3614-9135-d4851b8d6b9f | -4.2425 | -47.5913 | 2024-12-17 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6327bb4f-10f1-3e48-9aa7-4a9007018f76 | -3.44231 | -45.59995 | 2024-12-17 04:44:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c25fb2ee-2cbb-36bd-8361-fccbbe350f70 | -3.21532 | -53.10056 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de022a7a-4952-3518-afe0-6bfc0695826b | -3.87296 | -47.04207 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8492ecd-8e98-36bb-8fa4-6852e66845ef | -4.10217 | -46.71072 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9373993-5bc8-3f6c-9254-bed18649cd35 | -3.15369 | -53.18924 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b287f316-61ee-367d-94e7-415c3792ccca | -4.03398 | -46.90628 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f2123ff-7829-3a04-8f6f-268d399b3b4b | -5.08182 | -43.91133 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4df2bae2-32e3-3e1c-af97-47b5630ddd65 | -3.77026 | -47.17139 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f007253b-5c07-372c-bd34-c4d034de7995 | -3.55347 | -54.72335 | 2024-12-17 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bdad65b-1177-33a7-8004-97bceae64e1f | -2.51269 | -49.10611 | 2024-12-17 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4846b88b-1bd1-3156-8ea6-e91e397b0c27 | -2.57287 | -49.41428 | 2024-12-17 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfd76a15-f0af-3385-b3ca-c23127579752 | -3.43875 | -53.98428 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcfddaa4-cb75-3b1f-9ab5-9fcb03f1fdaa | -1.63574 | -45.85611 | 2024-12-17 04:44:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fad446a-3c1b-348e-8f3f-ec483bbcb4e5 | -2.03743 | -46.49789 | 2024-12-17 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afaaa0a1-d9b6-3001-bdc1-1d95165d01a1 | -4.76108 | -46.71264 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9da13ef-bc62-3db1-96c4-85a76c69960d | -3.99671 | -46.90071 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 232bd4c7-6091-3d7d-b8a7-41e3fc3bc8ab | -5.31788 | -46.49326 | 2024-12-17 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1fcb0dd-3528-3528-a9a7-ec93dd8bee28 | -2.77963 | -48.58016 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b335fbd-0364-3302-a925-1c0ff899525d | -3.83261 | -46.68367 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6048d3e6-0054-3cf5-bcc8-f32479172102 | -4.57362 | -46.57898 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec74293c-7045-3023-b340-b663d177e385 | -4.89445 | -44.17059 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abbe5c04-5d74-3b57-a216-a6c7d6ea686f | -2.5885 | -47.4849 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77810934-ab78-30b4-aff0-2bf146018e7f | -4.38567 | -47.77071 | 2024-12-17 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef8c2c92-4ded-3cdd-98de-26ba26e85346 | -5.36031 | -44.0486 | 2024-12-17 04:44:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc5568aa-66e1-31ee-b18f-aecb2e676fc7 | -2.14559 | -48.03786 | 2024-12-17 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| aaf5a32c-502a-37a1-9e38-3a1bacab1039 | -5.39439 | -40.66442 | 2024-12-17 04:44:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 90eabe07-4ab2-38b1-934b-572850ace92a | -3.23286 | -45.37441 | 2024-12-17 04:44:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82ccb8da-8618-3d36-b88d-e40f3bdf846c | -3.78978 | -46.84145 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d89f958c-8189-30e8-b760-d809f4315130 | -3.43916 | -45.60081 | 2024-12-17 04:44:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 826530cb-10a8-3510-a05b-0282c0ebcab5 | -3.15267 | -45.97178 | 2024-12-17 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34e002c2-7df5-324d-9f6d-2648ca4fe762 | -4.06972 | -46.5931 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a48ed232-a396-35b3-8e56-a4e2192cd869 | -2.55227 | -54.70129 | 2024-12-17 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| febab995-21b9-3eaf-945d-aa7d6e2c48d7 | -4.09942 | -46.72866 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e42baf2a-64ef-39a2-a8f8-a0c4d4db9ee8 | -3.22881 | -45.3738 | 2024-12-17 04:44:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5aa7dc1-b381-351e-bce0-bbabace41ff6 | -2.07889 | -54.23001 | 2024-12-17 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a835808-266a-342b-8b5d-6eb0064b88b1 | -4.02505 | -46.8644 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc1e0483-4c8d-3c85-9bb5-54c049104f7b | -4.52489 | -44.0463 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 792474a3-ae67-36f1-95cb-af95f20ace2d | -3.99452 | -47.28884 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 249e8334-2bfb-32d8-937c-72a80495d01b | -5.08966 | -43.91896 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b335231-0989-3037-94b2-584fe7cdf29c | -2.65268 | -42.71907 | 2024-12-17 04:44:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c543c9c-e341-3d11-bb66-2c816a2a91d8 | -4.09633 | -46.72368 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45f69dda-8002-39b6-a0e0-cd7715a23083 | -3.29878 | -53.37349 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7c57e5a1-4c93-3bcd-957a-f2fbdbc131b9 | -4.03319 | -46.86107 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e89dd0c-24a5-3af0-a915-308b690be5b9 | -4.0998 | -46.70104 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9733f5a-77bc-3f49-a8f5-d502d74fe9a7 | -3.93098 | -46.89718 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adc15a56-3686-31a8-a1ae-e37150838583 | -0.16831 | -51.35301 | 2024-12-17 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e5605cb-0845-37e2-9d94-dfd9b63a9368 | -1.60084 | -45.41182 | 2024-12-17 04:44:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4f0c23b-5a21-3d15-b2bf-b9a4a80e9ca4 | -3.66296 | -47.16527 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8d497cd-40e6-3fbb-b776-54cfbfb9a146 | -2.84523 | -52.56949 | 2024-12-17 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48821752-7f82-3254-b637-2056c13a2503 | -1.63117 | -45.86023 | 2024-12-17 04:44:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 894e9e34-03b4-329d-9ce3-ca0930b5b950 | -4.04685 | -46.92191 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c87bea4-57de-3590-9194-1dc5dbeee55f | -4.00043 | -46.90128 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76648232-a462-3059-95b9-d3ae17be605e | -5.93864 | -43.79189 | 2024-12-17 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77f7ec1b-488c-323f-a70e-5e27ff96e287 | -2.52294 | -47.072 | 2024-12-17 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d08a288a-bb24-3c66-851b-a0a1f6081e50 | -4.67175 | -44.03668 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2b12211-0b3e-3c86-b609-8c0a18c6ff7b | -5.38863 | -40.66358 | 2024-12-17 04:44:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9d76c22b-4d1b-3e56-87bf-d42d09ac9c25 | -5.09953 | -43.91556 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 446adfb1-e528-3334-9d09-ff9384b4a4d6 | -5.26112 | -43.76546 | 2024-12-17 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78867797-467e-3a69-9b08-c7d86000f0ac | -4.79791 | -46.39429 | 2024-12-17 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f54edf2-32ea-331f-9a6f-868920b91cba | -0.16821 | -51.35241 | 2024-12-17 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9a62090-231f-3cc9-9bf1-ff8204a38998 | -5.09493 | -43.91489 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b51eea1b-ac11-35db-a33e-fdb3a7149173 | -3.84807 | -45.8582 | 2024-12-17 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dccd4c8-dc30-36dc-9e68-d024f26fc08d | -4.06593 | -46.59253 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67ef6a8c-3e49-378b-88c4-38941b691e6d | -2.55261 | -54.69926 | 2024-12-17 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 17cd0e1d-0cba-3727-94a5-e6091c335e86 | -3.79319 | -46.83513 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21c39ded-de4c-3a1a-b883-1c064575ba2f | -4.06079 | -47.10242 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f6d3a08-c511-35d8-b8c3-d476318e239f | -1.46076 | -53.48414 | 2024-12-17 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b161e73-1a29-36ea-ac3f-32080383e384 | -0.75124 | -47.75647 | 2024-12-17 04:44:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22dbb4ee-3b4e-3ecb-a9fc-ae7a468b2db6 | -3.1424 | -48.60518 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c96e357d-8ea8-307a-8f84-97ad3cd4b0fe | -2.9344 | -52.71284 | 2024-12-17 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d90256dd-9919-39ea-b51a-7a132707a18b | -2.51316 | -49.05904 | 2024-12-17 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2143f41a-9312-32d1-b70c-06418544a995 | -3.18377 | -46.69304 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8df4c09b-1e58-3521-9ace-688ec5c7c632 | -2.87468 | -45.2477 | 2024-12-17 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49be3546-e8f5-34e1-8f1f-46fce36679f1 | -5.09104 | -43.91255 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 199eca15-822b-3626-b8ed-d2f78c3daa68 | -4.79329 | -46.39862 | 2024-12-17 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a5e43702-28bf-3208-8530-c87adc317b36 | -5.14302 | -43.23645 | 2024-12-17 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README22.md)
