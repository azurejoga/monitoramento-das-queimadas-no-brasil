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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02764dcc-8d3f-38b5-967b-a307f764df54 | -2.65433 | -49.99364 | 2024-10-23 00:48:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 1876590a-8596-3135-874d-ab2df4bc9dd0 | -2.64031 | -46.08089 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d9f78c55-3455-3185-98b1-5977b46abf27 | -2.62342 | -49.99253 | 2024-10-23 00:48:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc2cd337-18e4-3d33-b644-6df8956c58d7 | -2.62182 | -49.981 | 2024-10-23 00:48:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8de4999e-ce1b-3dde-a7af-958231f2c550 | -2.60821 | -51.77698 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 518ff5ca-1ca1-3d7e-ab85-2a112010a3c0 | -2.60556 | -51.77155 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a32bb70f-e6ea-30eb-a8a7-b1737eb78c0e | -2.60216 | -46.13156 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a88d91ec-a02a-3fdf-a81b-001d969fb463 | -2.60091 | -46.12268 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf9ca293-7bc9-3ae9-8d4d-760fc209baf0 | -2.58977 | -49.82355 | 2024-10-23 00:48:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c35a315a-27fc-3d9b-8639-91cdb563f6ba | -2.58442 | -46.13408 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4571a025-c186-38ad-80f7-9cd645559c01 | -2.58242 | -49.24707 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 1020241d-3c39-33fd-bdf1-c99eba4d4d63 | -2.581 | -49.23669 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 452c2add-a141-3f13-ba5b-29e3aecd85a6 | -2.57793 | -54.02188 | 2024-10-23 00:48:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| e1b35fe9-daff-3276-9b23-42cc6cd362c9 | -2.5768 | -46.1442 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e99bf99-cb50-3d83-9a8c-28ca1736ff5c | -2.57556 | -46.13533 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 19ca61f7-3639-33f3-a878-a559e05209f0 | -2.524 | -46.16668 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4f1ffeb6-8ed7-33ff-a362-b851690b9e95 | -2.51513 | -46.16792 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5f2dad6-840f-396c-996b-3a2bb95ed7cf | -2.51272 | -54.10947 | 2024-10-23 00:48:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 157.2 |
| b29fff53-16ce-35a5-8e0f-4795ca792df6 | -2.50814 | -45.92357 | 2024-10-23 00:48:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 66a06a01-2d61-3e45-a54f-a3a0da853fa8 | -2.48464 | -46.28677 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0516cdbf-d9e1-343e-bd14-e3209203432f | -2.48254 | -49.1206 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 24115021-b12c-3301-9cf4-94ee77fcba47 | -2.48113 | -49.1104 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8ebe2a8f-e3d6-3dde-b6bb-fc48bf1d95a9 | -2.47026 | -49.10154 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7f85d142-855e-3371-96ea-acd425654f5f | -2.46886 | -49.09139 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 65d0cfdf-2cae-32df-a508-b010878e0a56 | -2.46852 | -49.01926 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 22004474-3953-355d-8001-9195e7ff0736 | -2.4633 | -51.96886 | 2024-10-23 00:48:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6db76fd7-3d34-319a-9e5b-1addcfe7daa2 | -2.4217 | -50.37492 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 07d91cd8-6287-3db9-8e7c-b3e5e5c7a747 | -2.41919 | -50.29582 | 2024-10-23 00:48:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c204475e-5277-3035-b5f3-b4eead21aa59 | -2.41868 | -50.3695 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e3d7c7b6-4326-3fcd-9924-078428d9433f | -2.41652 | -50.48767 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5432e576-bc7a-3313-b8fa-1120fd3a127d | -2.40626 | -50.41423 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f33ac646-1ab5-3e20-96d3-b20cb3c1d2ba | -2.37573 | -48.55219 | 2024-10-23 00:48:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 752f2143-c88e-3728-b599-f19f4b7b31f9 | -2.36652 | -46.16492 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fef6dc14-eff1-3902-8420-26a3ab3bbaa7 | -2.36521 | -46.54318 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7e166ecd-b6ea-32c4-8d60-bff36b53fc06 | -2.35578 | -48.9387 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e5285b28-aff4-39de-9fc7-81e24886b993 | -2.33253 | -46.51822 | 2024-10-23 00:48:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7501d704-975a-3929-bfe4-ea4aca2189a3 | -2.33211 | -46.2421 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 919065e0-5f23-38f7-a625-bf7426d2abef | -2.32607 | -46.13442 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3cbcd054-3525-3234-8ddc-a31841d00445 | -2.30186 | -46.62114 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9f6be33f-3d13-34f1-a0c4-aca2d9caf818 | -2.28614 | -46.44398 | 2024-10-23 00:48:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 98f70e95-d51c-3652-8f91-82cd55f95ede | -2.28491 | -46.43517 | 2024-10-23 00:48:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 348d758a-fc66-3302-9928-4b9fd6716b33 | -2.28298 | -46.61485 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9538d44d-e238-39fa-8e01-9dd48ce456fe | -2.27961 | -47.92015 | 2024-10-23 00:48:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e215133b-d496-3cc9-b5b7-2c1507c1f263 | -2.27836 | -47.91104 | 2024-10-23 00:48:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7c267b05-02bb-3f7e-af86-b81a70acb1db | -2.27236 | -46.74765 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ec7f56e2-6caa-3bd2-bbfd-5b8c19eb9c5a | -2.27114 | -46.73887 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5461d62d-97b6-3f68-bc99-8607fec26416 | -2.26992 | -46.73009 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7ef4616a-8b18-3bb0-9280-0c882f16ee76 | -2.26721 | -46.77522 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1c7c10b0-5f60-3c35-aeb8-7bfe2b6162c9 | -2.26476 | -46.75767 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 75fe3406-6667-3c3b-8cb9-0a00dc4dd178 | -2.26231 | -46.74012 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ad20bec1-b572-337b-bafc-f27905ced056 | -2.25838 | -46.77647 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 7f2a4f73-eb4f-3aed-8723-e28203b09478 | -2.24956 | -46.77771 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6305ea28-55d5-3558-8a49-13aeadedaa47 | -2.24196 | -46.78773 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| dddd8746-42f2-308e-8e9f-50739bcd3626 | -2.237 | -48.4095 | 2024-10-23 00:48:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 848459c5-46da-3625-97ce-e6776ffaaead | -2.22696 | -50.31032 | 2024-10-23 00:48:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4e672a8d-9708-31e6-95c4-2e9d6aabe48b | -2.21305 | -46.77392 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 71f7fb1a-c10b-35da-9725-09aeeea66925 | -2.20177 | -46.43493 | 2024-10-23 00:48:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d1e3d36d-72f1-3164-b762-8f119f84c924 | -2.18548 | -46.72147 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2833dd85-cf4f-36b1-a58d-6f0a38b6c327 | -2.18372 | -46.83806 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 45cf1691-2f37-35bb-8f47-e18e98eb6dae | -2.1825 | -46.82928 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5c7bdb75-ee93-3bb4-81d3-ec462137dae6 | -2.18032 | -46.74905 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 50f2077c-311c-3982-bc69-30097d950bc7 | -2.1791 | -46.74027 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 394e0bca-ab38-30de-a192-f392e8f2bdc9 | -2.17647 | -46.05885 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0c793af1-5e6b-3c33-9557-bed65e1f8ee7 | -2.17522 | -46.04993 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f82879bb-d004-356e-9e26-8d8ecd5eb081 | -2.16633 | -46.05118 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f7431b7e-9401-3133-b48d-52e22b1c8e58 | -2.16508 | -46.04226 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1d3c17b8-ba97-36e7-9939-d0e1c331e1a1 | -2.14153 | -47.92382 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 728ef5d4-e483-3b34-b597-8fb4b564e142 | -2.14027 | -47.91477 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1bfba16b-5004-303d-8603-f710a3ff7a07 | -2.12222 | -47.38195 | 2024-10-23 00:48:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e28710bb-227b-346f-b430-37729741d1a5 | -2.121 | -47.37311 | 2024-10-23 00:48:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 25da170f-c3c6-3eda-a31c-afc44fbd42f9 | -2.11484 | -48.26091 | 2024-10-23 00:48:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9472c6f3-4d39-3c47-b698-badf9f8f1c09 | -2.11336 | -47.3832 | 2024-10-23 00:48:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ed0aa31a-0ab6-3be9-a4eb-2becb3e2c59a | -2.11214 | -47.37435 | 2024-10-23 00:48:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0b4c85fc-35a7-3362-b0f4-5bda4a048899 | -6.67146 | -43.06472 | 2024-10-23 00:48:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d9df52df-37a8-3bc8-9b1f-f8fc3aa4a9d3 | -1.89931 | -47.03942 | 2024-10-23 00:48:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c10dbcec-338a-3375-bb25-892eeea0bdfd | -1.87702 | -47.81339 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 312fb851-33e0-35d5-995b-44ecfd7b3923 | -1.87577 | -47.80441 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4577f8ac-0280-3ed1-8b8b-d4f5f93605b1 | -1.6823 | -47.07958 | 2024-10-23 00:48:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| a670a4ef-e695-31a0-86c8-a90221659604 | -1.68107 | -47.0708 | 2024-10-23 00:48:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d99b3766-a2a1-395d-812c-b16db75e86e2 | -1.59563 | -47.84399 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 95170def-2d57-3a9f-a069-673379c9384a | -1.55421 | -52.20355 | 2024-10-23 00:48:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 74829e60-e6cf-3157-82f8-2596abeba815 | -1.4904 | -47.15459 | 2024-10-23 00:48:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0f07c1ff-840f-399e-883e-713cd823c2c7 | -1.38594 | -51.99367 | 2024-10-23 00:48:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| b14921db-d8b7-3663-9dea-897ad972e7d8 | -1.38225 | -47.83129 | 2024-10-23 00:48:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6124a647-0442-311c-a380-084b9ac84b0e | -1.38101 | -47.82234 | 2024-10-23 00:48:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 196470d8-b21f-3da6-8cc0-42e4ce7ea450 | -1.27549 | -48.05386 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 659215b3-0597-3de5-923e-baba4bfedd65 | -1.27425 | -48.04481 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 96dbf81a-a622-30f3-8233-43f4d2c760ca | -1.22071 | -46.54192 | 2024-10-23 00:48:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a43a20a7-769f-3b8e-b5ef-8f6bd1b1f79d | -1.17483 | -48.85438 | 2024-10-23 00:48:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 49e5cbf6-d81c-34ef-ba19-553ddd5ca930 | -0.37397 | -49.92222 | 2024-10-23 00:48:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4e5c6d67-a75f-3e89-817e-7dc427e76251 | -6.678 | -43.04157 | 2024-10-23 00:48:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 6bb33d94-b01e-38e5-be64-afc249780ee2 | -5.22282 | -43.17572 | 2024-10-23 00:48:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3a863957-7e50-3dc5-be8c-f574eade2b89 | -6.72588 | -40.5034 | 2024-10-23 00:48:00 | TERRA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 97c2200b-f7cc-396c-bee0-a8b9124d45d6 | -6.72101 | -40.49846 | 2024-10-23 00:48:00 | TERRA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| dcb1193c-2d22-37f5-8518-781ce35569c0 | -6.67959 | -43.05244 | 2024-10-23 00:48:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 479a57b7-e1b1-3ef7-82ee-061624601742 | -6.66987 | -43.05389 | 2024-10-23 00:48:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 691de849-08e0-3a2e-b4d7-7d470f1d04c5 | -6.66826 | -43.043 | 2024-10-23 00:48:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 934c8372-882a-384e-abdd-4ead6922e8cd | -6.28629 | -43.38198 | 2024-10-23 00:48:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff17dd81-f9f7-3af3-9754-56a4a6e1b678 | -6.28477 | -43.37141 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 733e7242-7a02-392b-9181-9704d57fe1d1 | -6.26421 | -39.60482 | 2024-10-23 00:48:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |


[Clique aqui para ver as próximas entradas](README8.md)
