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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac3934a7-4e92-3216-8703-300861530cb4 | -2.41 | -50.31 | 2024-10-01 02:05:14 | MSG-03 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf28f75-257a-3334-994b-79cbd3a35076 | -3.0282 | -51.3345 | 2024-10-01 02:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 8589d558-6e21-39a4-a43c-d389f2f2f22f | -5.9786 | -45.3847 | 2024-10-01 02:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2ddb6690-e2fe-37a1-85d9-df700df87c7f | -5.9788 | -45.3621 | 2024-10-01 02:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 383c5911-8a3e-3a2a-a071-b7a30a950719 | -11.6555 | -64.9991 | 2024-10-01 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 1dd07967-218d-3a48-8901-43fb39d22506 | -11.6556 | -64.9802 | 2024-10-01 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 26c3be6c-8c83-3633-8046-b41308655e42 | -11.6743 | -64.9983 | 2024-10-01 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 055aa0a6-80ca-3f9d-8f09-5e6525603017 | -11.6744 | -64.9793 | 2024-10-01 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 50d10611-a549-3181-bcd4-9bac6ab74aae | -12.1402 | -50.074 | 2024-10-01 02:06:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 666c533d-93a5-378d-89f3-75ea886ee7c7 | -12.1406 | -50.0524 | 2024-10-01 02:06:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 294dfaef-da39-31b0-8fbb-5442e52a8ce4 | -12.1593 | -50.0717 | 2024-10-01 02:06:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 1f2d3462-c86f-309c-bacf-d3e9e88ea4b4 | -12.6039 | -53.4879 | 2024-10-01 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| b0a1696e-6016-33c3-aaed-8bb739ef0c39 | -13.5761 | -51.2036 | 2024-10-01 02:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ff130a87-eb98-3b98-8275-5be40e05c8ef | -13.5765 | -51.1821 | 2024-10-01 02:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 185.8 |
| f62df864-57de-3fbf-9777-66b3f9848a93 | -13.5768 | -51.1607 | 2024-10-01 02:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 385b98c6-6733-3f1b-aaca-b06a34f3ab63 | -13.5954 | -51.2011 | 2024-10-01 02:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 14ec1f83-bf62-3c57-bf10-49cc8f53fb5c | -13.5957 | -51.1796 | 2024-10-01 02:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 212.9 |
| 361e0b9b-41fc-3e86-92ce-6f0a1c75aec7 | -13.5961 | -51.1582 | 2024-10-01 02:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d133ab99-85b3-337f-9505-32421993d3b3 | -13.6161 | -51.1128 | 2024-10-01 02:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1ae4b623-f93b-3ccf-b710-cceb0ffbde48 | -13.6353 | -51.1103 | 2024-10-01 02:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 972e3fde-464e-37a8-84e1-c0d9fd61057f | -14.7211 | -48.7529 | 2024-10-01 02:06:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 867f1304-87bf-35cb-8e3b-481297ad7bd2 | -14.7406 | -48.7498 | 2024-10-01 02:06:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| daba603e-6e13-3eb0-9ab7-d60a9f40c4c5 | -14.7596 | -48.769 | 2024-10-01 02:06:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| b3e6fcfc-1be6-3406-8d4e-a55930be600d | -15.9127 | -57.1733 | 2024-10-01 02:06:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 257bc207-0b68-39bb-8695-70d984d7f4a3 | -16.1856 | -58.4417 | 2024-10-01 02:06:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 38fed0cd-d494-35d5-abe7-c780ba6cf1bf | -16.1859 | -58.4215 | 2024-10-01 02:06:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 8b071f34-7ec2-314a-a553-dbdcf416cc54 | -16.6263 | -55.1934 | 2024-10-01 02:06:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 151b7d6b-461e-381d-9e55-0eb8463262b9 | -16.5134 | -57.3305 | 2024-10-01 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| be4e1265-b77a-3ee5-8cef-1e2506466894 | -16.5131 | -57.3509 | 2024-10-01 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| e0fa33eb-4681-32dd-98f5-2bf65e906f08 | -16.4939 | -57.3327 | 2024-10-01 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| c3f6aff4-53c4-308c-930c-429524fb4840 | -16.4935 | -57.3531 | 2024-10-01 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| d045b79d-fd8a-342e-b266-e8e40a6a5a7a | -16.4743 | -57.3349 | 2024-10-01 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| d1def7f6-b3bc-3f87-88b2-7365fcce3819 | -16.474 | -57.3553 | 2024-10-01 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| f0340332-67de-390c-93f7-61f2d5e834e2 | -16.7385 | -55.491 | 2024-10-01 02:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 146.9 |
| b1e34640-ccd1-3a2d-8be5-47575f8a30fc | -16.7382 | -55.5118 | 2024-10-01 02:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| b5f5922e-d712-3521-8658-13754cf0b278 | -16.7189 | -55.4935 | 2024-10-01 02:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 117.3 |
| ce644df6-b144-398c-b793-b896643dd62b | -16.7186 | -55.5144 | 2024-10-01 02:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 34554c2b-9bf4-3273-b58e-68332d180863 | -17.6464 | -53.1708 | 2024-10-01 02:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 3048f989-c2e9-3ecd-8c17-dafe82d3f1ac | -17.6662 | -53.1678 | 2024-10-01 02:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 70899fc1-d277-33a0-80cb-03fcadb4470f | -18.5231 | -49.4467 | 2024-10-01 02:06:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 61bb6176-0221-3eca-b83c-52c0c767af6d | -18.5236 | -49.4241 | 2024-10-01 02:06:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 6d80421c-bfa3-36f5-9868-69e9adc842b1 | -18.697 | -57.3538 | 2024-10-01 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.1 |
| a60d3b7e-3a16-3aa7-a097-5839133d35a8 | -18.6973 | -57.333 | 2024-10-01 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.6 |
| 9f3db7c8-500c-3de3-8605-0ae00c2514bd | -18.6977 | -57.3123 | 2024-10-01 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.6 |
| 3a37091d-cca2-3ddf-ae1e-b66e4e4e3166 | -18.7172 | -57.3305 | 2024-10-01 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.2 |
| aab5dbc3-d349-33e3-b547-06f67e19a352 | -18.7176 | -57.3097 | 2024-10-01 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.4 |
| a98f9bf1-2101-33d3-a849-1db269f5118c | -18.9085 | -49.2356 | 2024-10-01 02:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 206.7 |
| f8a408ae-8684-33c6-a645-a9129fd7cd6b | -18.9091 | -49.2129 | 2024-10-01 02:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 156.3 |
| dfbdae8a-48db-391b-8dee-ec2cde797912 | -18.9287 | -49.2316 | 2024-10-01 02:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 229.4 |
| 9d84f3d3-e352-35bf-b8a3-a905b203111a | -18.9292 | -49.2089 | 2024-10-01 02:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 182.7 |
| cda92ffe-0e60-38b9-95cc-11549a243d7e | -19.1329 | -57.4628 | 2024-10-01 02:06:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| c2250f8e-3932-3ecc-9eab-c2041ab8b6ce | -22.3498 | -49.3293 | 2024-10-01 02:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| d3e6ba0d-eb7a-33e0-8ac9-c1e978aa16a1 | -22.37 | -49.3477 | 2024-10-01 02:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| 432715a0-6a2b-36ca-a836-7802756511da | -22.3707 | -49.3244 | 2024-10-01 02:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 266.2 |
| a26565bc-3627-35f3-a5b5-99664a7d67e7 | -22.3713 | -49.3011 | 2024-10-01 02:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 142.7 |
| 436b90c1-25b6-3c98-a2a1-d8457122f4f9 | -22.3916 | -49.3194 | 2024-10-01 02:07:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.6 |
| bfd2d8f7-8e52-3718-a5c9-8cb4cb4d8bc9 | -22.3922 | -49.2961 | 2024-10-01 02:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.0 |
| c0af3c50-06c9-388e-bd7b-0947aa921dba | -23.0793 | -45.3951 | 2024-10-01 02:07:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| eaa01f68-3454-30d6-a854-93dd2ba87597 | -5.9786 | -45.3847 | 2024-10-01 02:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 611bccce-4c61-38d1-85d3-ca6ea097cbb1 | -5.9788 | -45.3621 | 2024-10-01 02:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 90675163-c73d-32d5-be99-99470476c996 | -6.2524 | -44.132 | 2024-10-01 02:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 5d616d17-ef24-320c-9441-19f1779fd19e | -6.9671 | -47.6215 | 2024-10-01 02:15:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| c916fdca-73d1-3b25-9720-991130153157 | -6.9858 | -47.6201 | 2024-10-01 02:15:45 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 539977b1-02bb-362a-bc75-ad038785c5d1 | -11.258 | -45.6682 | 2024-10-01 02:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| d35871d2-f29f-3153-88cc-fffbe285fd4f | -11.2584 | -45.6453 | 2024-10-01 02:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 452e7c41-ae09-367c-bbba-b6c46a9dac7d | -11.2771 | -45.6656 | 2024-10-01 02:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| fcc816bb-dc69-325e-9f14-16b2015229b0 | -11.2775 | -45.6427 | 2024-10-01 02:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| aa92dca7-6f3e-30a1-b69a-6860ae7bf931 | -11.6555 | -64.9991 | 2024-10-01 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 167.9 |
| aa1ba1fd-aca4-3a3e-816e-1b7994cd6844 | -11.6556 | -64.9802 | 2024-10-01 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 1b6112e3-78d8-36e6-b1a1-28a463e0206b | -11.6743 | -64.9983 | 2024-10-01 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 114.1 |
| b7aed8c1-4bdc-3fe0-a9d0-d855b401696f | -11.6744 | -64.9793 | 2024-10-01 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| e05e4d02-17e1-392d-865e-328ea492dce7 | -12.1402 | -50.074 | 2024-10-01 02:16:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| bde1eb63-677e-31fe-b439-5170afb77dc9 | -12.1406 | -50.0524 | 2024-10-01 02:16:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 35634a27-595c-35e2-a2f5-47689eae0609 | -12.9245 | -51.2002 | 2024-10-01 02:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d0e1e619-805e-3735-bbb3-ce3453994715 | -13.6161 | -51.1128 | 2024-10-01 02:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0192ad12-25c4-3820-a3d7-f9d0a6230f01 | -13.6353 | -51.1103 | 2024-10-01 02:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 88abb098-1434-3494-8f80-04844e8d4ff0 | -13.6357 | -51.0888 | 2024-10-01 02:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 21323ac1-034d-3d7a-82e3-fb7e9b6d38cf | -14.7211 | -48.7529 | 2024-10-01 02:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 0780fb8e-f324-375e-9f2b-cf925975d719 | -14.7406 | -48.7498 | 2024-10-01 02:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 425a4812-85cb-358e-a1c7-9abd87037095 | -15.0673 | -49.9115 | 2024-10-01 02:16:30 | GOES-16 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 5e671d92-1330-35fa-8f42-9b012d39f440 | -15.0678 | -49.8895 | 2024-10-01 02:16:30 | GOES-16 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8fc7ab73-c420-3865-9091-bfada6cbf6a6 | -15.2788 | -58.191 | 2024-10-01 02:16:32 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 09a4732f-210d-3398-9562-add67607a070 | -15.2791 | -58.1709 | 2024-10-01 02:16:32 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 3896b59e-fa36-3a66-bc74-0a516eac2dc2 | -16.1859 | -58.4215 | 2024-10-01 02:16:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 2f285c05-99d3-3920-8060-e8860303b665 | -16.1856 | -58.4417 | 2024-10-01 02:16:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 64fdc55f-2e41-318e-97f7-11e6ae3a5432 | -16.7385 | -55.491 | 2024-10-01 02:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 8882a2a0-9381-3f00-99b3-aa81fc8750d3 | -16.7189 | -55.4935 | 2024-10-01 02:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 5c72d841-8a0c-36ab-9234-4a5b9fd797ca | -16.8983 | -57.6949 | 2024-10-01 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 1d3ce86f-ae80-3756-af72-5142ec75b95c | -16.898 | -57.7153 | 2024-10-01 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.1 |
| f41a9a05-1b45-34f7-a979-0725b7ebe768 | -18.5231 | -49.4467 | 2024-10-01 02:16:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| b25be20e-7d05-3bff-b21f-828b498d282f | -18.5236 | -49.4241 | 2024-10-01 02:16:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 8eae076e-ed2a-3684-a768-5d0f702f06b9 | -18.6774 | -57.3356 | 2024-10-01 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.6 |
| e8d5e14b-b8c0-3def-ab5d-01b187e8a4d0 | -18.6778 | -57.3149 | 2024-10-01 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.1 |
| bf3a7269-b045-3181-bb5c-583c5cd1b1d4 | -18.6973 | -57.333 | 2024-10-01 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 296.6 |
| cec6796e-6543-3aa7-ae78-7c0c8be4d5e7 | -18.6977 | -57.3123 | 2024-10-01 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 209.1 |
| bd012ab1-6acd-39a3-8114-c8021e5c4cc6 | -18.7172 | -57.3305 | 2024-10-01 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 198.1 |
| 5e3dec13-b59d-35fa-a730-e60a3a42495d | -18.7176 | -57.3097 | 2024-10-01 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.3 |
| ebdedf5b-f97d-3e0d-893a-f878fff40137 | -19.1329 | -57.4628 | 2024-10-01 02:16:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 3dc4ed99-9259-3964-b47b-7a5db76c8e35 | -20.6393 | -48.7549 | 2024-10-01 02:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| fadd4812-3a4f-3ed9-9592-120ba24c25f6 | -22.3498 | -49.3293 | 2024-10-01 02:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.3 |


[Clique aqui para ver as próximas entradas](README31.md)
