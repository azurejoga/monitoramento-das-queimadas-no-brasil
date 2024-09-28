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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c0c9147-62f6-34da-8f0c-abe7ff3691b9 | -8.34036 | -47.54658 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2da9be64-aff6-38a8-909b-78ece701a480 | -8.13362 | -47.34798 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9460ac1-d2cb-3e66-b3c9-58b381c7a19e | -8.13299 | -47.35181 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff75374a-6d3c-3a00-81d0-ae048193e00c | -1.94107 | -47.90043 | 2024-09-28 04:19:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d3c2c15-b2f2-37ec-bf20-165d05e99837 | -1.97461 | -48.6923 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b24a24bb-2e0f-359a-a8e6-74a69db0df4b | -1.97405 | -48.69584 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 625b6f8d-5a00-3d10-9c55-8a76ed3d487c | -3.22308 | -48.93018 | 2024-09-28 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d57be317-e5a1-3f28-80f1-c93d6861a3cc | -3.21907 | -48.92954 | 2024-09-28 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4810bf65-096a-312a-8cab-fe0370759282 | -2.90266 | -47.88707 | 2024-09-28 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b3f92c9-a240-3af4-bea9-6c78ea42d3ba | -2.89888 | -47.88644 | 2024-09-28 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e982304-52aa-3718-b413-a68145077b96 | -2.63534 | -48.0546 | 2024-09-28 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd1cd073-e7f8-3e40-a02c-c3dc7a8d092b | -2.63459 | -48.05935 | 2024-09-28 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7e2d9b5-f9ad-3e8e-bab9-9366f1c921cb | -2.63151 | -48.05401 | 2024-09-28 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e91904a-3247-3f37-acaf-8ffa8488918c | -2.63075 | -48.05875 | 2024-09-28 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4da4d9a0-7543-38f8-82e7-72f58349e569 | -2.62557 | -48.32251 | 2024-09-28 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 307db742-561c-3f9a-a593-6b73ebfa1dfc | -2.62505 | -48.32019 | 2024-09-28 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 905ff65e-49d2-307e-80bb-409074c6ea97 | -2.49573 | -47.56482 | 2024-09-28 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95176128-ce2a-3361-8407-199e9ba457fc | -2.47994 | -48.05201 | 2024-09-28 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 02eb6088-d08d-353c-b876-b489f1d209af | -2.47917 | -48.05676 | 2024-09-28 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b06e2a09-aed8-3242-9590-c93db2490b41 | -2.42058 | -47.60357 | 2024-09-28 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0543cb88-488a-3944-88df-865b5280721c | -2.41903 | -47.60518 | 2024-09-28 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d87fc7b-3086-30c9-b2c4-b1c79fad9c33 | -2.36591 | -47.98724 | 2024-09-28 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54bcc4d4-57f5-3f0d-a4bc-4c7082146746 | -2.36147 | -47.60528 | 2024-09-28 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 513aa76b-86b8-32d9-80b2-35d9d934e103 | -2.36074 | -47.60983 | 2024-09-28 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7be62787-2945-30e9-8efe-b3582ffef187 | -2.35845 | -47.60019 | 2024-09-28 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bda54e2a-179f-37ea-a216-4e008e8a033e | -2.35773 | -47.6047 | 2024-09-28 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 425df724-507a-3857-bfa0-ed1fedcd2645 | -2.357 | -47.60924 | 2024-09-28 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4761557e-2787-34d2-a4e8-b948bcbca378 | -2.35398 | -47.60411 | 2024-09-28 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 76971a4c-c2b7-3051-ae45-22741d1ecf5b | -2.34151 | -47.976 | 2024-09-28 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aea4d13d-7dd9-3c14-8a01-6a3d93049736 | -2.33768 | -47.97543 | 2024-09-28 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 131e1a79-28ab-3d23-bf7d-e6acb5b037f8 | -2.43614 | -48.47201 | 2024-09-28 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68f2c395-2d3c-39ea-935c-4d24159135e4 | -3.70274 | -47.61594 | 2024-09-28 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0af68d46-dd6c-36ea-9781-8b58faae2b56 | -3.46953 | -47.66719 | 2024-09-28 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5f4d1ee5-cefa-3151-a616-40e6eb3d3b30 | -2.92039 | -48.88825 | 2024-09-28 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73a58834-fd4a-32d5-b3c4-0f55064c32ed | -2.91982 | -48.89175 | 2024-09-28 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e268715-2ece-3343-bc4c-73d2b4f9b6a4 | -2.79359 | -48.57401 | 2024-09-28 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02026603-14e0-38d9-8ece-5079f1037aeb | -4.95448 | -49.25172 | 2024-09-28 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5213de09-31a3-3d97-8514-360a30cdc033 | -4.91756 | -48.61276 | 2024-09-28 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7272bb74-1717-3d52-8beb-95939f12f9e2 | -4.91373 | -48.6121 | 2024-09-28 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1854202f-2796-35d9-8e25-b23054531302 | -4.90989 | -48.61147 | 2024-09-28 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ac372be6-f504-3914-9c28-a7f18da373bc | -4.79602 | -49.35442 | 2024-09-28 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32a860e4-7b4d-364d-8e29-b8712daea28c | -4.79257 | -49.35029 | 2024-09-28 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1435fed0-9bd4-3d57-a90d-dcdf753eac12 | -4.73112 | -48.84362 | 2024-09-28 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 884142c4-af46-33a3-ade3-ef416b502cb4 | -4.63174 | -48.53411 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37e48b74-e21b-3b3e-9ba9-e0af537c0e24 | -4.578 | -49.30833 | 2024-09-28 04:19:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e1443500-f516-3d03-a322-0c59c04dad1b | -3.2363 | -50.01593 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 767603d2-7d3a-3b4d-a043-90003206e96a | -4.57742 | -49.31183 | 2024-09-28 04:19:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 98102fc7-2648-3002-83aa-197189bde19b | -4.57338 | -49.31124 | 2024-09-28 04:19:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a7c0a1df-e4ea-38ea-8dac-ee99e60e01c2 | -4.40228 | -48.71334 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bb7ccc4-6f7a-347b-a357-e38153f886df | -4.40179 | -48.71084 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c22cd6c1-b26f-38ec-a39d-5c763e2cfd41 | -4.97286 | -47.93074 | 2024-09-28 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a47edd4a-4531-3600-92fc-c54299802c74 | -4.97221 | -47.92908 | 2024-09-28 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 858619fa-3aed-3f5c-8dff-a1d6f23ab8ad | -4.58454 | -48.00871 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe6309bd-a6b9-3e0b-8708-15ea83f54324 | -4.58382 | -48.01316 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3427e86b-70f3-3247-bb60-bb1cbd3a3917 | -4.5809 | -48.03113 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c28d2f73-c124-3988-b837-df1a6bab8ac7 | -4.58081 | -48.00812 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 022fa5f5-fc6f-319f-8aec-e9e045c5b445 | -4.58009 | -48.01258 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d1c1f63c-e9c6-32a4-bf6a-fccf54acda36 | -4.57718 | -48.03051 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ea83ce0-bc89-399b-b2ae-2c6a18c094ba | -4.40896 | -48.08917 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9b804f4-9e94-3fb5-99ac-d9a92db06b3a | -4.40756 | -48.09019 | 2024-09-28 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e4cf710-469e-321a-ac8b-ccc6fe006365 | -4.28037 | -48.06192 | 2024-09-28 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d5e6c48-66fe-3f46-b044-1b513d2ecfc8 | -4.27965 | -48.06644 | 2024-09-28 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37bfcd71-9790-3f5d-9cf3-7d08de9fbcd2 | -4.18105 | -47.88336 | 2024-09-28 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19c7bee1-d605-3f9d-9c40-22972d1d78ba | -4.08697 | -48.27402 | 2024-09-28 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eb05165-01f9-3320-a5b2-67f881ac858b | -4.07631 | -48.07486 | 2024-09-28 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0738e20c-0b9d-3e8b-95a8-b4d42f87ad98 | -4.04927 | -47.93188 | 2024-09-28 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b4db535-eedc-391c-abc4-ddc959fd4bc9 | -6.54581 | -48.70741 | 2024-09-28 04:19:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 77b68c9c-3aa2-3e1c-a744-f12e26352a52 | -5.87567 | -48.09995 | 2024-09-28 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad7a0ea3-5b7f-3cc4-a02f-ee8a888e96ef | -5.4543 | -48.37456 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43e47e37-2ef5-333c-9b75-d27e8f998ebc | -5.37183 | -48.23818 | 2024-09-28 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d24e22f-e5d4-34ea-9f2b-1e67b9caf54c | -5.21124 | -48.35965 | 2024-09-28 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c43e869f-7373-35da-9716-0e5a042e31b6 | -5.20985 | -48.17831 | 2024-09-28 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e1c5db7-d996-3181-b98e-57742d632d2b | -5.20912 | -48.18279 | 2024-09-28 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bd7e1c5-6b2c-3e83-b6d2-04bd0d719f59 | -5.20747 | -48.35905 | 2024-09-28 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88cb04b6-5b25-3cce-b235-fbe26082c2af | -6.00188 | -49.34389 | 2024-09-28 04:19:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb728d65-2216-3319-ab20-3a545724c07f | -6.00104 | -49.34898 | 2024-09-28 04:19:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e88b7a0-b5f8-3141-9fe7-ab24b45562c8 | -5.99792 | -49.34327 | 2024-09-28 04:19:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03d4b811-8ab5-32a8-8c6b-4996113cde7e | -5.99708 | -49.34837 | 2024-09-28 04:19:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95208ced-6c2e-3fb9-956d-54232e6b04ad | -5.95006 | -49.19347 | 2024-09-28 04:19:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca03a4e3-e33f-3c1a-af42-e9c25f3f92f9 | -5.94304 | -49.18719 | 2024-09-28 04:19:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84e8eca2-d9d8-36ae-8b2b-059ccacf26bc | -5.94222 | -49.19221 | 2024-09-28 04:19:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5d9d2cdf-5141-377a-aa68-dd959fd477c6 | -5.93829 | -49.1916 | 2024-09-28 04:19:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6711cfd0-d966-3874-9ab8-ef4a9795002f | -5.93747 | -49.19661 | 2024-09-28 04:19:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7f74f8db-8de2-3114-ad25-dcc9be9351b9 | -5.51882 | -48.97484 | 2024-09-28 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7528adcc-80b1-3454-ad83-7e77c6111883 | -5.26364 | -49.22949 | 2024-09-28 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baa9e8ca-a2e4-3510-85a4-446f1d5481e9 | -5.20902 | -48.9728 | 2024-09-28 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0f690ba-3326-3d80-a1a6-417b71ee06f6 | -5.1408 | -48.90083 | 2024-09-28 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a155b39-18c3-3069-8329-d0d4d2327459 | -5.096 | -48.87591 | 2024-09-28 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb26fd67-f438-35a3-8627-7c7d191aafb8 | -7.82274 | -49.16739 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd36f3ed-8b40-397b-be1f-e87081cc3b80 | -7.82225 | -49.16586 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afa8104d-f6c2-3c05-91d7-5b7c8cbf8d03 | -7.82146 | -49.1705 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8456590-acf5-3681-b42e-06cfa504ded7 | -7.81163 | -49.15925 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e76f855-ee89-3b32-9854-976228bb9d0d | -7.76616 | -48.52124 | 2024-09-28 04:19:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60353b96-1c84-35cc-979d-f9679395e353 | -7.5933 | -49.19223 | 2024-09-28 04:19:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 54a78fbb-483c-363d-91b8-7771154ea2e4 | -7.59241 | -49.18977 | 2024-09-28 04:19:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d4267f0-1a0b-3b73-9147-4a9b014bcc09 | -7.59162 | -49.1944 | 2024-09-28 04:19:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61dbf1f1-807a-35fc-9cc4-e981b41c26c9 | -7.58875 | -49.196 | 2024-09-28 04:19:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2eefa7a5-b414-3fb6-a6c2-741e69e69f4b | -7.58784 | -49.19353 | 2024-09-28 04:19:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4020a41e-643b-3a60-b5f7-484e8772330b | -7.57724 | -49.19427 | 2024-09-28 04:19:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b52be3e-6792-3d69-a684-3892155db59c | -7.5742 | -49.18885 | 2024-09-28 04:19:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README45.md)
