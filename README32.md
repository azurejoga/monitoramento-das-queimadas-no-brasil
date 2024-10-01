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
| e0417ff0-2b92-3e18-9e19-621f683a9925 | -11.6555 | -64.9991 | 2024-10-01 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 106.4 |
| a9fc2101-3098-39dd-902a-c7b662c3b1dd | -12.1593 | -50.0717 | 2024-10-01 02:36:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 0248f31c-e1c4-382e-9fe1-8583cc09c498 | -12.1406 | -50.0524 | 2024-10-01 02:36:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 171.2 |
| a9fa0af3-659f-3397-9e06-5f97bc4f745c | -12.1402 | -50.074 | 2024-10-01 02:36:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 5c8a8888-f0e2-36ce-b30a-2dbe9baf1a0c | -12.6039 | -53.4879 | 2024-10-01 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 8559d083-ac2a-3eb5-bee9-adde02006f99 | -12.9588 | -51.4517 | 2024-10-01 02:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d21ae1e4-8c8e-34aa-b02d-ba31dc8ceac5 | -12.9396 | -51.454 | 2024-10-01 02:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 39231233-aeb1-359a-b418-f16e9a830820 | -12.9245 | -51.2002 | 2024-10-01 02:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.3 |
| ca469d7d-0492-3bc9-bd20-c358443003ca | -14.7406 | -48.7498 | 2024-10-01 02:36:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ce1f1896-19a2-3223-8355-2d27601704e3 | -15.9127 | -57.1733 | 2024-10-01 02:36:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| f5ea2098-6bce-3617-828e-58de85411257 | -16.1859 | -58.4215 | 2024-10-01 02:36:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| ced3263d-fc4a-3a22-8ae6-a1b761176a7e | -16.1856 | -58.4417 | 2024-10-01 02:36:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 68b30675-29b6-35a6-bda8-334a98eee5d5 | -16.5134 | -57.3305 | 2024-10-01 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 0745a6c4-e248-3cd8-92a9-1c861eeead4b | -16.5131 | -57.3509 | 2024-10-01 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 96e8c8b5-bed1-34bb-861e-7a57c416d810 | -16.4939 | -57.3327 | 2024-10-01 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 5e51b915-48db-3744-b41e-0f4432be1e45 | -16.4935 | -57.3531 | 2024-10-01 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 7d75c3b4-3386-3832-8e64-6df1edf53091 | -16.4743 | -57.3349 | 2024-10-01 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 04487047-2b5e-30d5-8c32-22aa9f4a2937 | -16.474 | -57.3553 | 2024-10-01 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 7d9c02c9-495c-3bf6-b14d-910652c60393 | -16.6505 | -57.2944 | 2024-10-01 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 91293a0e-06a2-32ae-ba2d-ea631091f5b2 | -16.6508 | -57.2739 | 2024-10-01 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| b83929c2-3d5d-392d-991d-8e2122998112 | -16.6512 | -57.2535 | 2024-10-01 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| 45052814-20ea-3bf4-bf41-0fa8510da74f | -16.6515 | -57.233 | 2024-10-01 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| c2e3d741-5365-34e8-af08-5ff8935df51b | -16.6704 | -57.2717 | 2024-10-01 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 982ccaf4-6246-33b2-b6ee-b79d2c273f0f | -16.6707 | -57.2512 | 2024-10-01 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.3 |
| cc9bd4f1-ab7d-3650-ba1d-e05aa796c8ff | -16.7461 | -57.4265 | 2024-10-01 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 3c836de2-4588-32da-8e63-0222d74d2ee2 | -16.7471 | -57.3651 | 2024-10-01 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 4c7f2644-47ef-376d-bca0-413da158f042 | -16.7464 | -57.406 | 2024-10-01 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 165e34de-8179-3e3f-873e-a88402bcc2d4 | -17.1098 | -56.7066 | 2024-10-01 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.6 |
| a88b19d8-faf9-318d-92fd-d5a2b8bd0d80 | -17.1095 | -56.7273 | 2024-10-01 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 956fb2e0-d99a-33d2-a3b9-20fecfc99c1d | -17.0902 | -56.709 | 2024-10-01 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.2 |
| 1d657574-4bc1-3f7e-b5dc-adade3513137 | -17.0898 | -56.7297 | 2024-10-01 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| f8d3839c-7329-32b4-a3fb-a159f6c2c551 | -17.0895 | -56.7503 | 2024-10-01 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| dadedffd-5fd9-3ffa-9b24-9354e31e662f | -17.0699 | -56.7527 | 2024-10-01 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |
| bdf1427b-baf9-3773-9a0a-1588e6f53582 | -22.3922 | -49.2961 | 2024-10-01 02:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| c27191c2-65c3-390f-a6d7-8fbb3a65976f | -22.3916 | -49.3194 | 2024-10-01 02:37:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 138.7 |
| 2235388b-fdac-37ee-8956-92ce68c81a9e | -22.3713 | -49.3011 | 2024-10-01 02:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 140.9 |
| d596ec76-66f1-3f69-90ce-55818f27490a | -22.3707 | -49.3244 | 2024-10-01 02:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 359.6 |
| bc127a62-4fda-3c5b-8c3a-bf708b36bda5 | -22.37 | -49.3477 | 2024-10-01 02:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.6 |
| de8c5016-7e08-329b-a2e1-d175bb5d1d4b | -22.3498 | -49.3293 | 2024-10-01 02:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.6 |
| 3fb02551-ac08-33fd-b291-8d8d4dbeb0e8 | -23.0793 | -45.3951 | 2024-10-01 02:37:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.8 |
| f9a4910b-ced0-3d87-b6b7-b5a78bc5ecb9 | -3.0282 | -51.3345 | 2024-10-01 02:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 057d8646-bfde-3db2-884a-f3f70c551ae5 | -5.9786 | -45.3847 | 2024-10-01 02:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 1fa5b95a-6900-3147-aed8-41cb47560d1a | -5.9788 | -45.3621 | 2024-10-01 02:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f3da0797-1b2b-3298-be28-a35b3abf055f | -11.1249 | -45.6407 | 2024-10-01 02:46:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 59acc6a2-e4b7-39d7-b465-d2364f5c679b | -11.2399 | -43.3938 | 2024-10-01 02:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 5370d058-384f-3328-991f-23b731ddc7b6 | -11.2591 | -43.3909 | 2024-10-01 02:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 460887db-b13a-3f6e-aed0-e098483c61b3 | -11.258 | -45.6682 | 2024-10-01 02:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 256.9 |
| 19bd9045-fb10-3f35-a9ba-4054c7618e1c | -11.2584 | -45.6453 | 2024-10-01 02:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 497c787c-dc3b-33c7-809f-995c76b3e70d | -11.2771 | -45.6656 | 2024-10-01 02:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.8 |
| 420608ae-74f0-30c8-9fb1-4a5293df6797 | -11.2775 | -45.6427 | 2024-10-01 02:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 0719c4d2-efd0-3afa-a5dd-681c0a3a293a | -12.1402 | -50.074 | 2024-10-01 02:46:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 1b358773-810f-334d-81b9-c52d2b118769 | -12.1406 | -50.0524 | 2024-10-01 02:46:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 06b52a03-b052-370f-a8c5-5e0590307eef | -12.1593 | -50.0717 | 2024-10-01 02:46:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8bfbf98a-bd70-3e02-8e85-7e07b16c1fd3 | -12.6039 | -53.4879 | 2024-10-01 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 306735fc-a2f2-39ce-91c6-5aed0d40a166 | -12.7636 | -62.9036 | 2024-10-01 02:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| afe77b21-d96e-306b-a030-2a8ba21c3d6e | -12.7826 | -62.9025 | 2024-10-01 02:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 3edf5a6f-8aa8-321d-b5e0-4f94a41a32f0 | -12.7827 | -62.8832 | 2024-10-01 02:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6989ab1e-38fc-3dbf-a5dc-95a28b505c50 | -12.9245 | -51.2002 | 2024-10-01 02:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| d8321c7c-0c9c-3cd4-a951-370cbd3e5425 | -12.9588 | -51.4517 | 2024-10-01 02:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 29dbfa85-8cfc-377b-9669-01fed4797388 | -12.9925 | -62.6976 | 2024-10-01 02:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| fdf0485f-2d8d-391d-bca1-6f719afa6346 | -13.2112 | -51.2287 | 2024-10-01 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 70f90881-3597-321a-adca-9f65e8194d19 | -13.2116 | -51.2073 | 2024-10-01 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 7dcbc325-409e-3ffe-a11a-654c788742ef | -13.2304 | -51.2262 | 2024-10-01 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 29dbbd0c-df1c-3733-803d-620b60eeea83 | -13.2308 | -51.2048 | 2024-10-01 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 45becd35-2dd6-36e8-8472-62b2f556d3c0 | -14.7406 | -48.7498 | 2024-10-01 02:46:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 56.7 |
| d25c3b0f-fffc-3664-96ef-e65d8511fab1 | -15.0483 | -49.8925 | 2024-10-01 02:46:30 | GOES-16 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| be902690-3dd4-3a35-be43-ecba742c72a0 | -15.0678 | -49.8895 | 2024-10-01 02:46:30 | GOES-16 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 85a4faae-5e34-33ee-b790-45dbd4f97c8d | -15.9127 | -57.1733 | 2024-10-01 02:46:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 3d0aab95-42a8-345d-b016-90e007102603 | -16.1856 | -58.4417 | 2024-10-01 02:46:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 372ed737-0b84-38b2-a07b-dd205ac65c5f | -16.1859 | -58.4215 | 2024-10-01 02:46:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| bb762bc3-eeff-3ec7-9dd4-c718578ef957 | -16.7076 | -57.39 | 2024-10-01 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| c9aaf46b-6cf5-307a-98e9-b3a9c55a918d | -16.7461 | -57.4265 | 2024-10-01 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| ce8c1b04-d803-380b-a799-42652eb440a9 | -17.0699 | -56.7527 | 2024-10-01 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.1 |
| c4759a81-2e40-3ebe-81bc-d9e8afde08e3 | -17.0895 | -56.7503 | 2024-10-01 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| a979a330-f8b1-3cfd-bc9f-1008ea159cfd | -17.0898 | -56.7297 | 2024-10-01 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 72e43a03-eedf-3358-93c4-546517f0fa08 | -17.0902 | -56.709 | 2024-10-01 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 97882f15-3f99-3e4a-9c3f-c6864e329c98 | -17.1095 | -56.7273 | 2024-10-01 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 8c65bdbb-2fe0-36e1-a780-d477a4b36a5d | -17.1098 | -56.7066 | 2024-10-01 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| e47395d8-ba92-32d5-aaea-00bee314f976 | -18.6973 | -57.333 | 2024-10-01 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| d7e6b893-0b12-3d21-bd61-7860342166ec | -18.6977 | -57.3123 | 2024-10-01 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.2 |
| e2bc68fa-3f74-35d5-b209-4b328e3aa5ad | -18.7172 | -57.3305 | 2024-10-01 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| ae0d1c10-9b6d-3dac-9289-bce0c2e27829 | -18.7176 | -57.3097 | 2024-10-01 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 9e3d47ff-35a9-3d11-b375-4a15f0487945 | -22.3498 | -49.3293 | 2024-10-01 02:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.5 |
| 83e395e8-5360-3570-ac5f-88b299fd124a | -22.37 | -49.3477 | 2024-10-01 02:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.8 |
| 9a24da42-c530-37f7-be9d-82f643fc2a77 | -22.3707 | -49.3244 | 2024-10-01 02:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 351.5 |
| e59e2681-5108-3cc6-bac3-10439e45cdb3 | -22.3713 | -49.3011 | 2024-10-01 02:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 122.0 |
| 0ac3a48f-1070-37ee-ae6b-dd7fe0f3d70f | -22.3909 | -49.3427 | 2024-10-01 02:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.5 |
| 46c46af3-134c-3849-a9b2-da273665127c | -22.3916 | -49.3194 | 2024-10-01 02:47:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.9 |
| a66523d8-cb9a-3dbd-9089-09c9df0473a5 | -23.0793 | -45.3951 | 2024-10-01 02:47:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.7 |
| a0913483-1409-3c45-a196-f2aaeb39b2f8 | -2.3863 | -50.3299 | 2024-10-01 02:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9364c605-8789-33a7-834d-a6e2da3e8e17 | -2.4047 | -50.3295 | 2024-10-01 02:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| f72a6b35-2d21-3b4e-a0f3-ce8e04614c2d | -3.0282 | -51.3345 | 2024-10-01 02:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 23413c39-56d9-39f3-aac6-2811b3394f5f | -5.9788 | -45.3621 | 2024-10-01 02:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 6fcb4e4e-52d9-3af6-8496-b5f14e8595fd | -5.9786 | -45.3847 | 2024-10-01 02:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 28096761-1cfa-3739-841c-da5f16b67a89 | -11.2591 | -43.3909 | 2024-10-01 02:56:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| a533f801-57c6-3cbc-ad2d-8d5c16645240 | -11.258 | -45.6682 | 2024-10-01 02:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 1de19a17-5ef3-3406-a891-03959b8c0763 | -11.2584 | -45.6453 | 2024-10-01 02:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 5800b965-0e98-378d-997f-9c2b486a3c0b | -11.2771 | -45.6656 | 2024-10-01 02:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c61e8b7f-e671-31f0-9938-41028309cd32 | -11.6367 | -64.9999 | 2024-10-01 02:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a5299d31-b6f3-3d54-9492-9e8e85bade72 | -11.6744 | -64.9793 | 2024-10-01 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |


[Clique aqui para ver as próximas entradas](README33.md)
