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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cded104e-1381-3778-a393-560390352c8d | -2.50667 | -46.10675 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c326753c-8270-34be-9237-fc634d194815 | -1.38489 | -53.55707 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b14eff6-ef1b-3e80-b72d-778cc7b766f0 | -2.91949 | -40.44412 | 2024-12-02 04:23:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| dd522009-5814-30e8-b9dd-6546c0407ebc | -3.13538 | -45.98122 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a7852d7-a80c-3349-ab64-95194d3e60ac | -2.69099 | -48.85619 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 24d920c6-076c-3121-a5c1-6ff0af8bd1e6 | -2.86802 | -46.73383 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf815a77-fbbf-3dfa-b029-da30f8e5bc97 | -2.26656 | -53.60846 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bea395e-50d2-3640-a932-0988e11c98c8 | -3.30823 | -46.40768 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b7e708e-227c-380d-a36d-3ce30ada89f8 | -3.14148 | -45.98573 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a84bf622-f8ab-3750-a254-8c02ff7b5663 | -2.72644 | -46.23807 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 859fee94-8546-32cc-8a2c-51a3bcb9206d | -2.12032 | -50.33997 | 2024-12-02 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a8c31db-ff6b-3678-b3b0-2ac56a731231 | -2.67522 | -46.28028 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0332bb07-ff70-371c-8ec8-06043d553e3c | -2.46619 | -46.58001 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dff784a4-c5b4-3eaa-a72e-a95f4e845435 | -1.03496 | -53.55675 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f271d58-c1e1-383d-863d-7a259ddc39bb | -2.72922 | -46.2421 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 916a7681-e503-3863-af22-61c764eb4e3d | -1.52087 | -45.91686 | 2024-12-02 04:23:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e86ca2b-19f5-3ffb-a081-4347822ebec0 | -3.17419 | -46.31887 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6253e77f-59d1-32ee-abdf-406ee12033e5 | -1.59295 | -51.25019 | 2024-12-02 04:23:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d180b6df-054a-3e78-8afd-ebe9cc991b01 | -2.69029 | -48.86051 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b0f1df53-fe15-3692-88d2-d4a5c7af6db5 | 1.20612 | -56.02354 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8e759a37-5408-306b-a0d9-9e1450722af8 | -1.49635 | -51.94106 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a0360c8-042b-3d21-abe4-db50845d50ab | -1.83652 | -46.23554 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0135b46f-ca3c-3c82-b5cb-a59eae68fb16 | -1.4527 | -53.59305 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f179ab0e-1918-390f-a6be-1c93bcacbab2 | -1.23587 | -51.60743 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81cde628-eaa2-3b88-a89b-8111eaf328c5 | -1.07673 | -53.45857 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07c7f6f5-bee9-30db-a4c8-cafa62f28de1 | -2.16404 | -46.32638 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50029650-70ce-3567-a10f-b6cf949dd9fb | -2.68136 | -46.28482 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb5a2dcd-ace8-3bf8-9fb0-ab54d228ff45 | -1.29582 | -51.37104 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fc8db2e-fb7e-3022-98a5-e79f83addf03 | -2.47236 | -46.56276 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbf4a767-23e2-3843-a699-7c32bd72d654 | -1.47737 | -47.33691 | 2024-12-02 04:23:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c66fc863-2356-39cb-ac8e-e31aafa88d54 | -1.95194 | -53.34559 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e9579b6-9dff-320b-962b-92f2f48fd2bc | -2.57048 | -46.408 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fa89c16-29cb-34c9-94c0-0698d4d518a3 | -2.82962 | -48.48051 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83fd74b1-a982-3101-9075-5a1cbf58aca0 | -3.30767 | -46.41118 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6de596e-f5e2-3597-a39b-c39d8596f3e2 | -2.95575 | -49.58292 | 2024-12-02 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74edc195-1d12-344b-afdb-ee95cdd66293 | -1.69432 | -52.63127 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65e9105f-450d-3530-9d8f-545031b805ad | -0.87349 | -52.35586 | 2024-12-02 04:23:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4203266e-782a-371e-951a-fbbc50ee1964 | -2.26609 | -53.61135 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 307161c1-8b84-352e-998f-8a9ebcefd6e3 | -3.16715 | -46.54776 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8df7913-c49d-3a2f-8e20-91ab55a1dd8d | -2.59558 | -45.65181 | 2024-12-02 04:23:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0fccb116-909d-3285-8a70-c649c26ba942 | -3.14093 | -45.98919 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bd6dce7b-7cb9-35a2-82ea-949e35671b54 | -2.71135 | -46.18199 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09344148-b5c7-3cc0-a832-30c354761355 | -3.32867 | -44.05223 | 2024-12-02 04:23:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90211871-7baf-3082-911e-4d422a7b8f7a | -3.12155 | -45.98566 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ef2f806-6b5e-3037-af14-7f037080e387 | -2.21552 | -48.38118 | 2024-12-02 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee7c225e-bf38-33e0-9ada-7100658c1735 | -2.51072 | -46.23266 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddeec889-c276-37c4-beb9-98f339a741f4 | -2.75477 | -47.90268 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e076c92b-f18b-3621-98ac-44a95cc75b2c | -2.23193 | -46.38752 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d00d507-0970-317e-8120-7e6cffb46419 | -2.3849 | -46.78719 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3800007a-a94f-3fc3-b8bd-7bf79caf4699 | -1.73266 | -45.60904 | 2024-12-02 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f0c375d-af0a-35ce-8218-685d1120ff20 | -2.9557 | -39.96462 | 2024-12-02 04:23:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e2ae43ae-aaa9-396d-898a-42220613176d | -3.29198 | -46.04103 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd35979a-fd18-3a01-865f-43001e4202de | -3.18279 | -46.55743 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1a50596-75bd-39d8-ad30-014f34f5f834 | 1.12046 | -55.98867 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79844e15-d6cb-338b-bc0c-1c462fe9f2e8 | -2.21191 | -48.38061 | 2024-12-02 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17aad3ee-2999-3db4-948b-44498c1599ac | -2.59226 | -45.6513 | 2024-12-02 04:23:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ae7a4685-0f24-30d1-9969-45a31e8ac547 | -2.70487 | -47.74111 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed62dc5b-1c0e-3367-930e-363fdf98bffc | -2.64104 | -46.58203 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2017b719-fe17-31bf-8331-e3938f3c25f8 | -2.67801 | -46.2843 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3081d1a-2254-3140-be5a-8397368e6383 | -1.95834 | -46.45364 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 375fa8aa-3e50-3e3a-b5c8-261ead93926e | -2.66693 | -48.80045 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4213899d-f784-36ed-a808-f7a982f57bf5 | -2.23305 | -46.38046 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 779c0720-3667-3c98-9f75-0a78eba574e6 | -3.0529 | -48.52998 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22eb1693-7304-3759-b005-2936c7c3ed99 | 1.1095 | -56.00035 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86597784-ba9e-3f7d-862a-8481caf42f1e | -2.62366 | -46.95398 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76921c03-7e03-3e35-9811-0b4c13e6598d | -1.09567 | -53.65082 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38da267b-af4c-3485-a308-3a3869047094 | -2.66602 | -46.12846 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b388896f-b12a-3f7d-81ad-f3f76859b0f0 | -1.52366 | -45.92087 | 2024-12-02 04:23:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a44aad2-70f7-3978-b093-9de1d401ff92 | -2.56544 | -46.5703 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52573bd5-393a-3b84-b957-e9964a107382 | -0.2029 | -51.54244 | 2024-12-02 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99410a74-9c93-3f17-aeb3-a7484b19564e | -2.29863 | -47.2837 | 2024-12-02 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab4aa800-0801-336b-8c63-4c89029b493a | -2.71358 | -46.1895 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4773fd79-77da-3f33-aab3-755421d023d7 | -2.53835 | -46.10101 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11c94a6f-2b69-3dcd-aeb6-6a5b82233766 | -2.92234 | -48.02797 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acb9c4de-48e3-34c4-89dc-e81d9dad0cbe | -1.08064 | -53.45092 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 70619142-dd8c-3c88-98d1-b422bc77778b | -3.82058 | -43.03029 | 2024-12-02 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1337de7-f8ba-3613-8d89-0f517bc586f8 | -1.70546 | -52.47175 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d602a9b1-e300-3eb2-a6ab-05a3b546531d | -2.59196 | -46.01349 | 2024-12-02 04:23:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ec7dd4b-689c-35ca-8eee-62f5634b04b4 | -2.71973 | -46.21552 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 372d5597-0929-31d6-b63c-a3db0b1016cc | -3.19567 | -46.36855 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f586127-b355-3bfc-84c6-d8233211be14 | -2.05034 | -51.19682 | 2024-12-02 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3f723f2-3e06-33ef-a2dc-750d8955176a | -2.66986 | -46.10408 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c89a686-6438-33f0-b3fd-3cbcb3ca38cb | -2.59572 | -46.57507 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53106c17-cb12-3f1b-a487-2e20b2d1323a | -1.40052 | -53.6548 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 774ee4e7-2e5b-3daf-8410-2bf0c2936173 | -1.527 | -45.92139 | 2024-12-02 04:23:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e223f3c-a90a-3009-bc85-780982cdc5ae | -3.15804 | -48.36127 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32e7147f-cf4d-3dbf-94ef-553de5de5c9b | -2.68029 | -46.61731 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eb184828-8fc1-319f-8475-97bec5e64068 | -2.27162 | -53.60937 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d707f074-e1bc-3c40-a98d-c5543dbd91db | -2.80752 | -45.94046 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3b5670b-0cad-3014-941b-c88671cc01f5 | -3.48446 | -46.08525 | 2024-12-02 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3b3432ae-3731-3298-b5db-8f5035ecdb62 | -2.97731 | -46.94531 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ff2357f-e4a3-3c13-9ee9-f25ff76bf539 | -2.17189 | -50.1254 | 2024-12-02 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05ca9818-e38a-30fa-a973-cddf5bf2db31 | -2.59554 | -46.27143 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e5ca6af-236e-39e5-864d-c080489f415b | -1.40512 | -53.65905 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 94f08b90-fdef-3074-a99c-762a6a187c7d | -2.72391 | -45.07473 | 2024-12-02 04:23:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c9be89f2-9f57-3fbe-9b79-65e9d624a2ea | -2.5783 | -46.4237 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4b9e5d7-b02e-3dff-bce9-fac16447f206 | -1.64526 | -53.86569 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c1b70a-0467-36f2-8bb4-0c3ef8053023 | -1.24885 | -54.55134 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36826203-1834-39f8-8afc-d800ef4e4d1d | -1.35167 | -51.38324 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c42f4b0-e57a-329e-ac52-38de7e7e3187 | -2.04304 | -54.65517 | 2024-12-02 04:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README33.md)
