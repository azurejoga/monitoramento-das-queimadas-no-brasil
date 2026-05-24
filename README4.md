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
| 913101b6-14a9-341a-9f0c-8923cdd32be5 | -12.89122 | -58.18097 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3569b3dd-0270-3859-96e9-ba0a9316a864 | -11.44902 | -52.92812 | 2026-05-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b48bc22-9817-375c-abe7-81669eddf4a5 | -4.43011 | -47.72854 | 2026-05-24 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8734abe6-d62e-3efc-a9c0-fa0968f1cfa6 | -11.43863 | -52.92635 | 2026-05-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b071e418-d462-39b8-85e8-7264444639ae | -11.40021 | -57.54449 | 2026-05-24 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 452c6597-d1cd-3f6b-b0e8-a727216cd517 | -11.92397 | -45.0066 | 2026-05-24 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36862480-b733-3e78-b933-2c32afee3477 | -13.9854 | -53.85421 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 359bd007-6d5b-386e-826b-ed3c6c18543b | -14.01936 | -53.36362 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cb7e40b2-2e10-3310-9e0a-e475eb747f74 | -11.5585 | -56.94363 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a0e6e44-fdc5-387f-8a35-fc867fdc8f3c | -12.53795 | -57.18517 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c47861f-1ef6-35fe-8486-4b45ca37ae8d | -10.64954 | -49.728 | 2026-05-24 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7904f19c-de94-321f-ab53-4fc39b300c36 | -10.53425 | -46.47185 | 2026-05-24 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7653d5f-7ab4-34a7-a117-d15f5dd84d5c | -12.89302 | -58.1713 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90d57fa0-1fc5-30c9-9534-ad37ffde0e11 | -10.91738 | -54.12043 | 2026-05-24 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef512f75-f187-333e-ad41-3a4ddfd12248 | -11.55385 | -56.32892 | 2026-05-24 04:49:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c19b58c-0e76-3766-9512-b23e601aab60 | -12.5431 | -54.61858 | 2026-05-24 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5a13002-4321-3c64-93c5-ed69b55bb8f8 | -13.98422 | -53.88262 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1342d8bc-ad6a-3b43-a166-1444b0771b21 | -14.02518 | -53.36396 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc88567f-0a13-364a-9c0d-a43b4132b3d4 | -11.95047 | -49.29773 | 2026-05-24 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebad5b3f-2824-3dfa-ac5c-cef3bba1845e | -11.54684 | -56.95857 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38a89b84-f64b-37fa-83d5-b3e611e6a305 | -10.77601 | -44.95617 | 2026-05-24 04:49:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 694d9445-e9ae-35f4-8a51-f2d1d9bba09b | -12.53644 | -57.19344 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3683a8e-13ef-308e-8b93-2598e0afca8c | -12.0469 | -47.33786 | 2026-05-24 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3134fb3-8beb-31dc-b142-f5b6987d2c22 | -11.04644 | -49.59596 | 2026-05-24 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c6d8abe-0841-305f-8d8f-6c9cc0cdb48c | -14.01374 | -53.35477 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd0b876a-edeb-33e1-8518-946fa3cb892c | -12.54599 | -57.16541 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dd4b3ff-1d3d-3f6e-a347-53e0528d47d7 | -14.77173 | -52.67018 | 2026-05-24 04:49:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97844a8a-108b-3ad2-bca0-5684e11087da | -11.54082 | -56.96251 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a1d2d8b-4ab9-38d9-8676-2df972e0e784 | -11.04925 | -49.60009 | 2026-05-24 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f457b0c-e855-331d-94a1-9efe744ea302 | -10.65289 | -49.72853 | 2026-05-24 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78336376-db0a-3c04-bb1f-d01f356ed40a | -12.53945 | -57.1769 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e3559b9-a7f3-33d3-9c38-2582e558b48f | -14.01894 | -53.35894 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9a1bcc1-499c-3e10-892e-f3d9c61fb849 | -12.89579 | -58.18186 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9944c788-42fe-3e84-80db-20f479cad876 | -11.9499 | -49.30144 | 2026-05-24 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c16a225f-a5fe-36c4-9428-a05812945786 | -12.5387 | -57.18102 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98f0389f-1dec-3134-b3d1-f5e798817d17 | -14.02174 | -53.36337 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d76a377-7bdf-34f0-9544-1070c56a0d56 | -11.17842 | -55.91754 | 2026-05-24 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0311bdfe-287f-3713-a64e-407db3a7ba5b | -11.54881 | -56.94252 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3484c33a-f333-33a4-9df3-655268a189a3 | -16.14757 | -51.7226 | 2026-05-24 04:49:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff82f94b-e19f-34c2-ace3-49970e0ce7f9 | -3.95968 | -43.12927 | 2026-05-24 04:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e74eb1ba-70c1-36b9-bf22-b3b183b58966 | -15.0904 | -57.63511 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b098390d-eee6-37b4-bd57-bc53e5533d6a | -14.77845 | -52.67136 | 2026-05-24 04:49:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d1c7b79-b922-3f60-93f5-e0b4162e284b | -11.5445 | -56.94167 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a4ad2be-f9bb-3b59-b9fa-b38a64f0649f | -12.04382 | -47.33283 | 2026-05-24 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad91b7b8-e95e-30a5-8be1-dc20139b3f2b | -12.05124 | -47.33397 | 2026-05-24 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bad2e13-fe9a-38d7-839c-9f8afa4750a8 | -11.94706 | -49.2972 | 2026-05-24 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b828fb4-cac6-31f6-b2ca-f90d3d15905d | -12.04753 | -47.3334 | 2026-05-24 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b6d6440-d652-3ce2-aab5-089361a4cf0b | -12.89311 | -58.19623 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03b4f986-87fc-362f-b2cf-04445c44c40d | -10.72357 | -51.59252 | 2026-05-24 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 579382e4-d574-3a46-8d62-efd375fd98ea | -11.5499 | -56.94193 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d7389f6-fcb5-3d1d-a2b8-310e9ca4ebbd | -15.08117 | -57.63749 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8270185-4733-3038-a72e-82117a12fd6a | -12.55029 | -57.16621 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8fb0696-2e18-3dcb-95f0-0545d2077ec1 | -14.01718 | -53.35537 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d306a081-ac5e-3fea-8a61-255b2f42f04e | -11.55742 | -56.94424 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d6cbb6d-6b05-31fa-a744-ba0b5d5bedba | -14.77509 | -52.67077 | 2026-05-24 04:49:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bace978-e1e0-3e51-9ea5-ab5cc0dd9e24 | -14.01655 | -53.35919 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b035ccc8-c477-37c0-8e9d-84f0094ae730 | -15.09686 | -57.62382 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a26cf2b-047f-3e81-b2b1-462804fe6da7 | -11.91126 | -57.0357 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10005edb-c230-304b-931c-728f7d7e0dd8 | -11.95006 | -57.04301 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15e06a29-479b-3c2f-9221-78dd225be4b3 | -15.09465 | -57.63595 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfbc19a5-76ef-30d6-b5ed-21c9d39fb527 | -11.21696 | -53.82743 | 2026-05-24 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ae539ac-6b31-3470-9faa-081ede269119 | -9.40946 | -49.40214 | 2026-05-24 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5522ce49-3284-32c6-8f51-355b72ce7e1f | -12.55385 | -57.17114 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 582e0062-7f80-35c9-a9fa-b44954b9d0b9 | -12.54955 | -57.1703 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38a3297f-0095-3a14-ad9d-e426944e1706 | -10.64899 | -49.73157 | 2026-05-24 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2881778c-1031-36d3-849c-b2c1eb72a25c | -11.04251 | -49.59903 | 2026-05-24 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e18254ce-c249-3426-b9a1-48ef403765d2 | -15.08191 | -57.63345 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd43cf07-afcc-39d1-b87b-5127dfe39eeb | -9.577 | -48.56833 | 2026-05-24 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e5b952d-2ea8-3600-8bf6-bc6e38513415 | -11.54376 | -56.94586 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 465c8520-4398-3072-996a-deef96d8286c | -12.88665 | -58.18008 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ffa002ae-c296-354c-86ce-4c814cf552ed | -15.08541 | -57.63833 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18ddfe81-d694-350b-b026-cdcc08425bcd | -11.55067 | -56.93775 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5045b97d-a431-3d17-9522-fb73f9620b1d | -11.63861 | -47.87886 | 2026-05-24 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 810cd0ce-3f30-3081-8dba-a9875896686f | -14.73333 | -52.69353 | 2026-05-24 04:49:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ddd65da-55d3-33b8-b5ba-299e0e7820fb | -11.54807 | -56.94671 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d7e44cc-b95f-3fbf-9f08-cec0b7565a04 | -11.54155 | -56.95837 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7e8f311-37b1-3814-a0b8-0ab5d5fb87eb | -14.32385 | -49.84437 | 2026-05-24 04:49:00 | NPP-375D | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31ed4010-e845-38af-a312-f9c5bce95127 | -11.92825 | -45.00717 | 2026-05-24 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 869108c2-b58e-3655-bef1-e9e3ebf773fc | -11.63502 | -47.87831 | 2026-05-24 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e7309a0-af99-3071-8d64-3e4f38ec3b0b | -16.13188 | -52.25234 | 2026-05-24 04:49:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b646c035-3c45-3098-9f99-09ead084c342 | -11.54587 | -56.95919 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bae88df-a00f-31fc-b1fb-86db96ca9619 | -11.94575 | -57.04216 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 987853e9-17f3-3bef-9edc-b7216f39d513 | -11.04588 | -49.59956 | 2026-05-24 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a1b65a6-0607-32b1-9669-a45987f80996 | -12.56159 | -54.75531 | 2026-05-24 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 891a7048-437d-31d6-84cb-135ad380576a | -12.88844 | -58.17045 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f3ae2d54-982a-32c4-a1b0-8a68b4dd5b67 | -12.53719 | -57.18931 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04a4226f-df6e-335b-9848-933d69803e3a | -11.5476 | -56.95443 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6d1a926-bf88-3d83-898d-33ea2b5ce39d | -3.95596 | -43.12458 | 2026-05-24 04:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3df9385-cf85-3501-bfa4-1a9f04166de2 | -11.63342 | -47.87884 | 2026-05-24 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be55e495-5761-312f-aaa3-b6c884dcebcd | -4.42954 | -47.73217 | 2026-05-24 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 821a7129-d6e6-3c16-a8d2-e0cc1aa816fd | -12.89668 | -58.17704 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b8e06ba6-f8ac-3a3c-8c27-7dd0ff88194b | -10.13277 | -52.11406 | 2026-05-24 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 900e32c5-29ce-3188-9b47-641a5ff7d9df | -11.27941 | -53.96679 | 2026-05-24 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6526be45-810a-3c2b-9831-953ed5b769f0 | -11.54303 | -56.95004 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0378b6fd-4f45-3d24-80a4-db4951a5176a | -14.73869 | -52.66066 | 2026-05-24 04:49:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77109dd8-f2db-3e05-b0be-23f998a4b661 | -12.04223 | -47.33485 | 2026-05-24 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eee51610-3b82-309b-80f5-34678d93451d | -11.44934 | -55.11239 | 2026-05-24 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 994a4b18-367b-38d7-bb87-e26bc41135a2 | -11.54229 | -56.95421 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e980c8ec-fa30-37fc-861e-0931435296b3 | -12.88754 | -58.17527 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 89492366-4cc9-3e11-94f0-5402a4776872 | -11.1778 | -55.92112 | 2026-05-24 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |


[Clique aqui para ver as próximas entradas](README5.md)
