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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 170fa35d-ea80-3aba-93e1-65af38fdfb3f | -4.11283 | -48.24792 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 91c615fa-0fa8-3147-bd2b-521894263767 | -4.11255 | -48.27207 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ff6267b-5d2c-3a9a-be9d-4863dc57eedf | -4.11221 | -48.25182 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a1ad6c4e-e8e2-3b3b-a784-b147ca131685 | -4.11192 | -48.27601 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98792ca6-9235-3e1e-817a-1cb360d16542 | -4.11158 | -48.25574 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 7311ced0-0208-3a3b-aff0-5920183b9d6c | -4.11095 | -48.25967 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0c28d349-efe6-3928-a2a7-6ccb9efed75f | -4.11032 | -48.26361 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a140ded-3536-38e2-8c6b-eafd5fb19325 | -4.10995 | -48.24349 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 5ea3d692-f6e7-328a-a783-a0728804e969 | -4.10968 | -48.26756 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e4fa8de-3f7b-3723-97a9-9ab09ab97423 | -4.10933 | -48.24737 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 5a0535ae-a224-3cda-a558-b588607e0dfa | -4.10905 | -48.27151 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 840921f6-8bc0-3897-948f-348ab9bd51a1 | -4.1087 | -48.25127 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| c397a546-3209-3406-8d5b-16e40e51bc1b | -4.10842 | -48.27545 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 721b455c-f59a-3e6d-9dbd-3efec80629e9 | -4.10808 | -48.25518 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| dd4e3d16-35fb-30d0-9191-1d86c9b8bdf0 | -6.08358 | -49.32124 | 2024-10-11 04:23:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3066061e-5a62-3845-b055-fc7af55905a4 | -5.75065 | -49.24905 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed23a49c-d511-338e-9395-aa39923a7a64 | -5.74985 | -49.24615 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 022bfe69-f47d-3d63-b13b-b2a0be96786b | -5.74919 | -49.25029 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fd41f1d-2eec-3bb4-b579-718017d380aa | -5.74704 | -49.24847 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8292ab92-c102-3f60-a279-06f1339e42b1 | -5.70889 | -49.31656 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9da2b7b1-fa14-38ea-9ddf-7d04e25e5f10 | -5.70752 | -48.60402 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33dbba91-333c-3eef-9955-37dea4db001f | -5.70402 | -48.60345 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9a86dac-6ff5-39d3-ac64-46ffe5f236bb | -5.43106 | -48.33944 | 2024-10-11 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87b2f28e-0079-3cfb-af8f-407b27bef8f1 | -5.40213 | -49.15104 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da40e153-2027-327d-a554-228360eb4d33 | -5.23926 | -48.45533 | 2024-10-11 04:23:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 57e0759e-da57-35c8-aa2e-37fdfa064ecd | -5.23863 | -48.45922 | 2024-10-11 04:23:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bf4b6fd8-96e1-3d29-bec3-99d62f34e03b | -5.19238 | -48.2282 | 2024-10-11 04:23:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56e395e5-281c-3295-a267-d082bc8764ee | -5.19177 | -48.23202 | 2024-10-11 04:23:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bef5d39-4a89-3947-9cd6-5e102a25643c | -5.17334 | -48.28001 | 2024-10-11 04:23:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd2ca0c5-f893-37d5-ad82-4056dfeb1e64 | -5.17272 | -48.28385 | 2024-10-11 04:23:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae492ee3-d2d0-33c2-bd45-12393ec37ad0 | -5.16988 | -48.27945 | 2024-10-11 04:23:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d67d6c46-ddb7-3201-87dd-9c6956d36682 | -5.16925 | -48.28328 | 2024-10-11 04:23:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 27.6 |
| d89c8aaf-8e4a-3326-a05b-f3c537a36c1f | -5.26719 | -48.0041 | 2024-10-11 04:23:00 | NOAA-20 | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1d5916b-235a-30a2-bbbf-834c8de11e86 | -5.26659 | -48.00784 | 2024-10-11 04:23:00 | NOAA-20 | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73c5c0d9-fa47-3ee3-a73e-001ec1c56d0e | -5.24688 | -48.0431 | 2024-10-11 04:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 97dea6ee-764b-38a7-af7c-6227af487d36 | -5.24628 | -48.04685 | 2024-10-11 04:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 941de791-5af2-3185-8334-3119599d7684 | -5.24284 | -48.0463 | 2024-10-11 04:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ffe0e08-48a7-34d0-b436-872e9f03dcc0 | -5.24224 | -48.05005 | 2024-10-11 04:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0036f5b8-c0b8-32e2-a46a-686d061a2ec8 | -6.08755 | -49.36471 | 2024-10-11 04:23:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09b2cd01-63ea-3c61-a8c9-d53a7023a087 | -5.7814 | -49.04834 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 570500cd-bd7d-3266-9902-79412fbae25e | -5.78037 | -49.04688 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4ab2b4e-29f8-3a84-9d6b-12e2e23e754e | -5.74558 | -49.24972 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51625fe9-456a-3375-b8de-a0324ce8f1d6 | -5.59756 | -49.03666 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 129b3db1-c5f2-33c0-9a57-a775b54d1980 | -5.58885 | -49.02264 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bedc44a1-ca6d-3b99-97cb-20e91d26d168 | -5.53606 | -49.29899 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0089e9c1-075d-379e-8db4-9f866d73d6b0 | -5.52935 | -48.96832 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| daa09c8d-a7f0-3a51-80d7-f0c6715b6ac1 | -5.50795 | -48.96495 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a518bade-b8e8-3a60-811b-5977515f1fac | -7.23591 | -49.34992 | 2024-10-11 04:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fa5aaf7-001e-34a7-bb5e-ae98736bd883 | -6.85844 | -49.13009 | 2024-10-11 04:23:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c612ca91-c480-33ae-a874-833ad718104c | -6.85756 | -49.13294 | 2024-10-11 04:23:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0fbb9bc6-930d-3848-99c8-148de46dafe2 | -3.89965 | -54.16787 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c57d317-96c0-3508-8802-4ccc52d6f269 | -4.08975 | -54.60686 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21603b06-31ec-3434-9b8b-082abb1e7f1d | -3.97442 | -54.09519 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27ca551c-899c-3bc2-a3da-06cf3cc4e1e0 | -3.90527 | -54.16568 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f40ce7f8-5319-399c-8005-219bccc9ae63 | -3.77573 | -54.23289 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd40fa66-27d9-36e7-9e44-591403a81847 | -6.17106 | -55.51191 | 2024-10-11 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 66495e82-4036-3365-9e1c-9fc452870650 | -6.17046 | -55.51532 | 2024-10-11 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| b108fde7-f1cc-30ae-b083-961bdbab6a44 | -5.80234 | -55.74031 | 2024-10-11 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bc5b4394-a162-32d5-82f5-92b27e039d39 | -5.80171 | -55.74393 | 2024-10-11 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d8ceaa8e-6764-3a88-bd60-f8fe5531d137 | -5.80108 | -55.74757 | 2024-10-11 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 46079dc6-2398-396a-9909-36c4a6824211 | -5.80044 | -55.75125 | 2024-10-11 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 64f73ac9-420e-3f95-90aa-490b86029ab9 | -2.0585 | -55.21948 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0ea638d-3d5c-3a34-b635-39635af1fc5c | -2.05538 | -55.2189 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08e5832a-3706-35a3-9701-a305435c7d7c | -1.75237 | -55.33302 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0290c17-c55d-359d-886b-3b59e63311ae | -1.75173 | -55.33689 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcc28f15-2c72-3ff9-b867-0249bb65f313 | -1.52372 | -55.41891 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff3a09ff-d1e0-398d-8f34-61fc302b90b9 | -1.52306 | -55.42293 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da1bf82a-3139-39aa-b6c8-73f50505571a | -1.52238 | -55.42702 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f93293d-f7a1-3710-a5b4-ae5094b14267 | -1.51795 | -55.418 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23b51baa-9754-3cbf-ab79-9ceb55b5fe78 | -1.5173 | -55.42199 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d035c45d-0225-3386-89ec-129f8c2faa1d | -1.34165 | -55.47557 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fd742ec-e7ee-3b91-b864-3f17af5b0901 | -1.34098 | -55.47974 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e80cee8-f467-3fd6-ada2-8f407f23069f | -1.25128 | -55.71098 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 912e798c-90d9-35b5-8502-f3f37d5a0d4e | -1.24973 | -55.70848 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7272595a-849c-3da3-94b1-5a009a1434ad | -1.24679 | -55.70108 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56fa5c8c-169c-3aca-9553-96c9d3daeaad | -1.24525 | -55.69899 | 2024-10-11 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44d94a93-4ac8-3c23-bfbc-86b983335ff5 | -4.83142 | -56.20607 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39618ef3-8c80-3961-a19b-4da2c97e10ec | -4.7991 | -56.22118 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d83a77e-1b59-3f91-ba9f-22f9b88cedb8 | -4.7984 | -56.22515 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8025ce7d-05b4-34ed-a752-9ad686e5cefe | -4.79833 | -56.22273 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac689170-b49e-3361-930d-e3300716dcbc | -4.79765 | -56.22672 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91df8140-a196-3a32-9582-a6407d174998 | -4.79264 | -56.22413 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 217e5358-a9bc-35fc-81c8-42eeec7b09b5 | -4.78991 | -55.89468 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5243e9ee-73c4-346e-a2ab-cdb3fd26ebc5 | -4.78428 | -55.89362 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28b8d04d-e67b-3851-847e-118bc7d2aa2f | -4.78363 | -55.8974 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caf723dc-8ee0-379e-8fe1-ca73f6f74cf3 | -4.5343 | -56.12947 | 2024-10-11 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f8f3c7b-7df4-3653-900f-3f5e120c03ce | -4.52903 | -56.12568 | 2024-10-11 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64b59a8d-e3c1-3f35-9718-b213e905ab51 | -4.52838 | -56.12943 | 2024-10-11 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40e62dc5-ceee-3a72-9037-ee1deb12e9ab | -3.99258 | -56.08688 | 2024-10-11 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e2be3a9-f5eb-3069-8abf-7ced003bc5dc | -3.77531 | -56.7981 | 2024-10-11 04:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a76b31c-0696-363d-b770-a0e7f22eb27b | -3.77448 | -56.80289 | 2024-10-11 04:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dffe981-1b8c-36d2-983b-db70ddedcbad | -5.27572 | -56.02573 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1c3a784-7413-3512-9de6-666a54f68757 | -5.27352 | -56.02249 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd985b8b-4176-382c-8a01-64756442ad88 | -5.27287 | -56.02636 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 169c952b-4c8e-3275-a3b7-4cf5cb1d7418 | -5.17851 | -56.00031 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d010381-bb38-36ef-8bcd-5de92a59d451 | -5.1778 | -56.00436 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41e011f9-aab1-3142-9da9-5bea95984a09 | -5.10832 | -56.23089 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fa7644c-4618-34e0-9170-b0e6e4e3056b | -5.10759 | -56.23494 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d517960-62b5-304c-afce-75facdde6235 | -5.10713 | -56.23065 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b66cde45-e74c-3aef-a9fb-c782d83b04d3 | -5.10644 | -56.23471 | 2024-10-11 04:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README62.md)
