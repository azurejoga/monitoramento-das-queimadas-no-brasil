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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bdab499-c338-3899-861e-cd2211b07412 | -8.5198 | -46.3098 | 2025-10-07 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| ccfbe5df-5e80-3128-8bc5-2bc8197fd40f | -12.9103 | -54.7352 | 2025-10-07 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| b3035613-ef2c-3233-b9c5-585de711417e | -8.174 | -50.3035 | 2025-10-07 00:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| f18904ad-fbf1-3ed9-8549-4bc635592fca | -10.3913 | -50.313 | 2025-10-07 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 473d6ab7-f719-3239-aa48-c191ec18a507 | -5.494 | -43.0526 | 2025-10-07 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| bac8b6c8-a43b-3113-bf12-d28bb69458ab | -8.501 | -46.3117 | 2025-10-07 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9b0c6ebd-83e9-3c0a-b9c6-9692b7648f83 | -18.1574 | -53.3485 | 2025-10-07 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6ff50ec2-59af-3b79-8959-1f9aae981eb4 | -18.1176 | -53.3548 | 2025-10-07 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 5049ea7c-9e7b-3f13-8b68-233a742f887a | -15.6202 | -52.5501 | 2025-10-07 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| a2e47dfc-cd68-36b7-9e3a-730bf4073c02 | -10.3724 | -50.3149 | 2025-10-07 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 3424a84d-d071-368f-ac16-c0688c1564cb | -18.0977 | -53.3579 | 2025-10-07 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 9f725781-c9b9-375c-b4e1-65ae3237de0b | -4.6318 | -43.1816 | 2025-10-07 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 3e2b0442-13a3-3964-8554-c6fc65230664 | -12.4267 | -45.6136 | 2025-10-07 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 4abfb2cd-be73-3d5c-bc3e-c44c8be7c517 | -15.6588 | -56.0154 | 2025-10-07 00:20:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 083cd627-5189-36a3-9fd0-9ec339d786a2 | -8.6519 | -46.2964 | 2025-10-07 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e3d3046f-8d68-340d-bc0e-e8d7cd184f8a | -10.8922 | -47.093 | 2025-10-07 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| f1b325d3-e225-3818-bb48-f507d9e3418a | -14.9026 | -51.4534 | 2025-10-07 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| a46eef8d-cd39-39b5-a2b1-cd9ac09b78d7 | -10.8542 | -51.0308 | 2025-10-07 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| ab635c8f-45d7-33a5-a65a-44e6e3e48fa1 | -14.8641 | -51.4373 | 2025-10-07 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4c420c25-2aab-3f64-b7f6-597440fa5308 | -22.1627 | -49.3504 | 2025-10-07 00:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 20e520a6-1b56-34a9-b50a-10409571b4a8 | -5.5125 | -43.0747 | 2025-10-07 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 5758e13d-6875-300f-a3ee-48b5bc574807 | -22.3337 | -49.8867 | 2025-10-07 00:30:00 | GOES-19 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.8 |
| c34c5aca-24a8-39c4-8d67-24d7c0fc5f94 | -14.8832 | -51.4561 | 2025-10-07 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 9277d79a-955e-340d-a681-4920cdbb9a88 | -22.1822 | -49.3921 | 2025-10-07 00:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 992b0c8c-9352-35a1-b767-c7f1bde7b2cc | -8.6521 | -46.274 | 2025-10-07 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 23e26ef5-dd09-3e74-9afc-e7a792c52e6a | -22.0279 | -49.7274 | 2025-10-07 00:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 171.1 |
| 20e13839-06f0-3c41-85cc-e96034d4cf61 | -8.613 | -44.9189 | 2025-10-07 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| ad670cd0-9b45-342e-a048-81c669ca7859 | -8.501 | -46.3117 | 2025-10-07 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3d0b0b93-ddc6-3cd5-b60b-bd1f3dff69e9 | -17.284 | -58.0793 | 2025-10-07 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 4ab115f4-5153-30f2-a9aa-d1f2541f672b | -8.174 | -50.3035 | 2025-10-07 00:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 117d10c9-c69f-3b11-b74a-11d843183332 | -21.4993 | -46.005 | 2025-10-07 00:30:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| fbaeb099-02c0-3556-93d6-5eda4a23ea31 | -22.3128 | -49.8915 | 2025-10-07 00:30:00 | GOES-19 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.1 |
| 33a8b048-f629-33b1-a5d1-c59133e9f472 | -22.1621 | -49.3737 | 2025-10-07 00:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 173.9 |
| e3eb5385-860c-3ac1-9d76-24b39359e5df | -6.1485 | -47.2871 | 2025-10-07 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 7b94c7a7-42ed-3d2b-94c3-1a0f33841209 | -15.6202 | -52.5501 | 2025-10-07 00:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| d769325b-6f61-3944-bcfe-c8b7433a28ea | -18.1574 | -53.3485 | 2025-10-07 00:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 59.0 |
| d4798c7a-3d38-36b9-9c9e-d891fb72972d | -17.2843 | -58.0588 | 2025-10-07 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| ae2e170a-b9e7-384a-989f-40d2c1d2a6ca | -22.1829 | -49.3688 | 2025-10-07 00:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 228.6 |
| aafaad4d-e684-3f3e-959b-27ea0b4c72ec | -8.1927 | -50.3019 | 2025-10-07 00:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 80147906-57ce-3279-9828-8662565c727a | -4.6873 | -45.8504 | 2025-10-07 00:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 4de06d69-9074-3a58-88ce-d3e9a4a9c58c | -15.6003 | -52.5742 | 2025-10-07 00:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 8fc2334b-6e3e-3bdc-b99c-e2e13973b7ca | -4.4632 | -43.2386 | 2025-10-07 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 36855e94-ce0e-35ca-bf9e-f1dcc92f5856 | -18.1176 | -53.3548 | 2025-10-07 00:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a2ee49f5-0c10-3745-bd5f-52be193f9ed6 | -12.9103 | -54.7352 | 2025-10-07 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e30c5051-0639-3a00-b9ff-4f75a3c717d3 | -5.494 | -43.0526 | 2025-10-07 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| b3edf192-2bb8-3067-9bae-2d7c7407e72d | -4.4633 | -43.2152 | 2025-10-07 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 53b4bf15-3360-3b94-ae14-6daca0fb4fec | -22.1836 | -49.3455 | 2025-10-07 00:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 28063821-eec0-35f3-96ee-54df868ad27f | -10.8731 | -51.0289 | 2025-10-07 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 66e6bd8d-0a7e-3419-9c16-3288df14730b | -6.2609 | -43.2727 | 2025-10-07 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 1c37bab9-aaa9-3eb9-96b8-54b5fb0a0619 | -10.8728 | -51.0501 | 2025-10-07 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| d2d48963-0d7a-3af7-a9d1-3c5dbb96bce0 | -6.2421 | -43.2743 | 2025-10-07 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a71fb13e-a104-3d52-b07b-c8b7a968c36e | -6.1301 | -47.2664 | 2025-10-07 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3f16d0ae-b700-330c-8a3a-838d0ff61fb7 | -14.7199 | -45.9942 | 2025-10-07 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f8ca4dfd-669c-3982-ad9c-edcf49410beb | -18.1172 | -53.3763 | 2025-10-07 00:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3d2f4911-f6eb-363a-ae09-0ec20b813083 | -22.3343 | -49.8635 | 2025-10-07 00:30:00 | GOES-19 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| d3885fca-5940-3987-bb55-cfc44fe58d00 | -18.1769 | -53.3669 | 2025-10-07 00:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 6199e9d5-360a-3370-98f8-42bd3ee80b55 | -5.4937 | -43.0761 | 2025-10-07 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 197.1 |
| b5a70888-19ff-3279-b964-0608466ae16a | -21.4986 | -46.0292 | 2025-10-07 00:30:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.5 |
| 2d58e892-00c1-3a3d-82d7-45d7187bef5c | -4.4445 | -43.2397 | 2025-10-07 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| d999e671-2674-365b-9d1d-352382d68798 | -14.8835 | -51.4346 | 2025-10-07 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 303.7 |
| dd3e59d0-8b93-3a23-8ebe-59ce8a67f499 | -8.5007 | -46.3342 | 2025-10-07 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| e43933c8-d2b1-3849-93a7-9d36b90777ac | -15.6198 | -52.5715 | 2025-10-07 00:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 7ebd4b2a-d9d0-3419-b8fd-540a56158758 | -18.157 | -53.37 | 2025-10-07 00:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ae78c0c1-9e58-384a-8b39-e6fb0ce8d2e3 | -17.3037 | -58.077 | 2025-10-07 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 196fabb8-cc8a-399b-8c99-d9a27a08fa7e | -6.1483 | -47.3091 | 2025-10-07 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| bbcacdf3-5419-3000-b66b-d035e7738309 | -6.4543 | -44.5749 | 2025-10-07 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 38b4687d-4e44-3e02-b3c9-0929aaec4acf | -4.6875 | -45.828 | 2025-10-07 00:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| e28d5ef2-49a1-3a29-bbfa-b39fde918a6f | -10.2693 | -44.3745 | 2025-10-07 00:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d6798d42-316d-3ae3-9d07-91d3a723a367 | -3.0864 | -50.5835 | 2025-10-07 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| dcadd14c-6922-357c-b206-3e17be30ddb6 | -22.0071 | -49.7321 | 2025-10-07 00:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 329.0 |
| 7e5d70da-ca79-3382-9a1a-23d5720b83b5 | -11.7594 | -43.2898 | 2025-10-07 00:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 23be2d3c-f31f-3c62-b9d2-4c181e4588d1 | -11.7401 | -43.2928 | 2025-10-07 00:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 186.5 |
| 3e5c04c3-1b27-36ec-8f2f-199607a16298 | -22.0077 | -49.709 | 2025-10-07 00:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 140.7 |
| abf3f692-1e16-3a04-8471-32e4f2d405cc | -6.1487 | -47.2651 | 2025-10-07 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6662b7e9-508f-33a6-85fd-5708bd70a8ed | -14.8839 | -51.4131 | 2025-10-07 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 53484931-20fa-386b-bc32-da8d93bb2da8 | -4.4446 | -43.2164 | 2025-10-07 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 3cf7857e-70e1-37d6-8f6f-de3971091119 | -22.0285 | -49.7042 | 2025-10-07 00:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| 446f92cb-890c-33fa-865c-6f10d28dea13 | -22.1614 | -49.3969 | 2025-10-07 00:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 83.9 |
| f75a77b3-3913-3614-8e29-1558a35b584e | -6.1299 | -47.2884 | 2025-10-07 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 9a21f188-1090-3fdf-92b3-06904824a5fe | -6.5849 | -44.6327 | 2025-10-07 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 776b65f5-a343-33ac-99fa-ed38c4c2ee75 | -14.903 | -51.4319 | 2025-10-07 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 3ba6baf7-5d6b-3e16-801e-c6810fe3025a | -6.1297 | -47.3103 | 2025-10-07 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 8cc9fdca-47ba-3764-97b9-db3f040b106a | -5.5127 | -43.0512 | 2025-10-07 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 8c1ed2e5-7c86-3522-9927-8dad2be513c2 | -15.6007 | -52.5529 | 2025-10-07 00:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| e40ca365-5075-39d1-9941-35a698a392c9 | -18.157 | -53.37 | 2025-10-07 00:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 93.8 |
| e63da591-2228-32e7-aa0a-2e4570d47655 | -22.1829 | -49.3688 | 2025-10-07 00:40:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1c4e0bc6-501f-3f96-a048-34b0dda5091a | -4.4446 | -43.2164 | 2025-10-07 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 51bdb082-4d40-39a0-a2dc-2b88c43a145f | -8.6127 | -44.9418 | 2025-10-07 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| d1ea02c0-f484-3daa-983e-b43fed65e805 | -22.0071 | -49.7321 | 2025-10-07 00:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 278.5 |
| 75c9b8b8-baae-32f6-8c88-5f9965db0144 | -22.0077 | -49.709 | 2025-10-07 00:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.6 |
| d7dd5114-d16a-3711-9ee2-34f53a02ecd2 | -14.2759 | -45.8416 | 2025-10-07 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 8459ad1a-0467-3cc1-8ce2-c909fb22eea4 | -10.8731 | -51.0289 | 2025-10-07 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 87e2ec4e-a1cd-3cf6-8f61-d8b31a6b8df9 | -8.1927 | -50.3019 | 2025-10-07 00:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ad5c571c-a97a-3c45-9647-b31ad9e32e0d | -8.6521 | -46.274 | 2025-10-07 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0157278f-7b3e-3fb6-b10e-a39e23859326 | -21.4986 | -46.0292 | 2025-10-07 00:40:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| 18a5acaf-8422-362f-9348-44ef2b389d49 | -6.2421 | -43.2743 | 2025-10-07 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 544dd8eb-d85d-34d2-97e5-335ad9c95d3c | -6.4543 | -44.5749 | 2025-10-07 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 67d38bbd-d4b2-3e3f-b22f-bc43070c2f78 | -10.8539 | -51.052 | 2025-10-07 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 149.6 |
| c314cb06-d91a-3ab5-b432-a17008922100 | -18.1176 | -53.3548 | 2025-10-07 00:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 7ab5ecf7-d3e2-3416-99be-184b54800f1e | -14.9161 | -46.8312 | 2025-10-07 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |


[Clique aqui para ver as próximas entradas](README11.md)
