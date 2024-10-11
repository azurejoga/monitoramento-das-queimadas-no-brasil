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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23af8db8-7647-3ad5-ae0e-aa21c89d68dd | -12.86277 | -53.45271 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74c92975-d10a-3cc7-b833-90596f119955 | -12.86206 | -53.45659 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e4f4a017-f971-38c1-ad66-197037cc56de | -12.85789 | -53.45578 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8cb4bf38-4c4b-3222-ba5f-9d328977f2c5 | -12.85698 | -53.45657 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1bc293f8-6ae9-349a-a7d4-8079ed02fe01 | -12.85281 | -53.45578 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1d1b3c71-6b5e-332b-af6e-5ccc868538d2 | -12.84863 | -53.45501 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f79c6b68-c818-377e-8b64-9c5723efb69e | -12.41978 | -53.15499 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 259832a7-a242-36ac-ba06-a809f74aa285 | -12.41912 | -53.15874 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fdbe1b53-8639-3e84-82e3-4a6fa54d6b16 | -12.41431 | -53.16179 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7bef0ac0-671a-330a-82f3-ceb7d1ca9d33 | -13.02932 | -53.63782 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2aa9000e-dff4-39cb-bf94-d1c7898ed6f2 | -12.96609 | -53.50709 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ce88dc3-bdfe-3b43-aca1-72926ba8c827 | -12.96538 | -53.51101 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23f98d21-f141-3d3e-858f-aa0a7b146295 | -12.96508 | -53.50837 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f9dfd90-43e1-3c16-a5cc-71c5d85e4346 | -12.96439 | -53.51231 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0c02da5-a8a2-333a-ab63-0159ba2b7b77 | -12.96192 | -53.5063 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c34e0bc1-8130-3a6d-a42a-422c87ca3ef2 | -12.9612 | -53.51022 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c6569ee-b6c2-368f-9c8b-bc019c947510 | -12.9609 | -53.50758 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0436f793-3dd5-3fce-997c-171332e26513 | -12.88143 | -53.49263 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aec6007e-4c36-3c28-b6b3-452651bb0b10 | -12.87796 | -53.4879 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fb8b3b8d-be0b-35c5-a726-495c690a01ae | -12.87725 | -53.49183 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f3bda36-e150-3146-a4b6-ccb2423cf089 | -12.87378 | -53.4871 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b416d602-8749-354a-82b8-360f2cef8f0a | -12.87307 | -53.49103 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 75f9baaa-0d7a-3b81-a469-1554f3b0b630 | -12.87163 | -53.49891 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1850b63b-95cb-3ed0-b85e-b84d3eff31d7 | -12.86745 | -53.4981 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21a8e2a6-0466-32d9-8e26-3e13dde8b0ec | -12.86673 | -53.50206 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f80fe28-96fd-389c-adad-4c18a79c8f2a | -12.86471 | -53.48944 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c7db6674-2bce-3002-a5a7-d159cfbefa2f | -12.86327 | -53.4973 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d9c14ea-a5bf-367c-9610-a0d32bdad50f | -12.86255 | -53.50125 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34e420c5-56bc-35aa-a21e-ca5364b5046a | -12.86183 | -53.5052 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a622b8b5-0c3d-3de9-8467-13984b5786f8 | -12.85981 | -53.49258 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 78c279a8-4065-3b5e-a58f-52ee428aeb88 | -12.85909 | -53.49651 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27551b62-5588-3b97-ae40-19c80d93e004 | -12.85837 | -53.50045 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 573e7932-c107-3fb9-869b-0d476b5f3f05 | -12.85765 | -53.50439 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22391b0e-7e46-3c11-b7fa-85c6d58ab15f | -12.85707 | -53.50532 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ed9d1dc-e2b7-343e-9a11-1ede09994a1e | -12.85692 | -53.50835 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcf02eed-b7b4-3026-9435-fd647446b3c5 | -12.8562 | -53.51231 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eae3b5a2-f359-3f1a-8576-61c9412d9353 | -12.85565 | -53.48875 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d8a58199-c483-31bc-b227-150e231e3d17 | -12.8549 | -53.49572 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2be97949-5ecf-38f9-b945-c08ee5e3557a | -12.85418 | -53.49966 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 80844aa0-f543-3bda-8207-d99ec52e9698 | -12.85358 | -53.50057 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83016b2d-ec42-3924-ab4a-c242c8ab6ccc | -12.85201 | -53.5115 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66fc112e-da6f-379a-b917-838deb57ed17 | -12.85147 | -53.48796 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| f7357c1e-8cb7-3735-91df-7a36f13ade82 | -12.85129 | -53.51548 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a84a5bd-e4c2-3659-aff1-24693cbadfb9 | -12.84927 | -53.50282 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26e80b57-1840-3b2e-8ec2-4f963687d4fd | -12.848 | -53.50769 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9d077ea0-4fb2-38d2-887e-e882439d7017 | -12.84782 | -53.51072 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d4f2018-9db1-3c70-b487-bd6312640444 | -12.8471 | -53.51469 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4c75a67-2481-3a87-b839-4da64e3e9b83 | -12.8466 | -53.51564 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe5c084b-c948-3142-a1d0-c3d4dd0d57ff | -12.8459 | -53.49505 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 5249c87f-f0ae-3629-be07-6dff7d1f92f4 | -12.84451 | -53.50294 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f54ab534-f21f-3650-b4b1-6a60f496b0ca | -12.84381 | -53.5069 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a2d063c-26d8-3d83-878a-1fef991b81d5 | -12.84171 | -53.49426 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b0c3d08a-77ba-3e58-ba63-729fd38d9087 | -12.84032 | -53.50216 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b1a7e8d0-3f76-3f08-b842-c20a0951d9b9 | -12.83892 | -53.51008 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da8b603c-220c-343c-bae9-b43450a58245 | -12.83752 | -53.49348 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 55dce242-9174-3104-b75d-276e8f6dbdb9 | -12.83682 | -53.49742 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 09be9fb2-c044-3223-9e35-a377e66fbd9c | -12.83473 | -53.5093 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91e40244-e515-3655-a1b3-ebd46844c2f3 | -12.83403 | -53.48877 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 82b731da-180d-3ba3-804f-d60d2b4969d0 | -12.83333 | -53.49269 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78f75159-c39a-36c6-b863-73336b3c2a9a | -12.83264 | -53.49664 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e228292-888c-3a14-aea8-03f0466f271b | -12.83194 | -53.50058 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8b7f053-229c-34e9-8053-be42e3dcae87 | -12.83124 | -53.50455 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 118468f3-38d3-313c-a1de-a118d71851f1 | -12.83053 | -53.50852 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8601586-de14-3705-aa6e-13de905104cc | -12.82983 | -53.5125 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31c4b543-7249-307b-a15c-152aef049f98 | -12.82565 | -53.48721 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b45a0233-96ee-3b01-887c-28f658a723de | -12.82426 | -53.49509 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 793c26f5-7018-3338-8472-3d9dc8b1e88b | -12.82355 | -53.49903 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32729b62-6bb9-31e1-8475-9477118adc3d | -12.62617 | -53.50885 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86d868a0-107e-3883-aa81-39cbd2af0cf3 | -12.89262 | -53.47857 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acd093cd-ad10-3210-aee7-0dbae9b345f7 | -12.89191 | -53.48247 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b72c451-91dd-3430-933f-f0f00600648b | -12.88355 | -53.48091 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efc441be-1250-36ac-8bd2-596efcb7cd0b | -12.88285 | -53.4848 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d9ce4e20-b882-34aa-be6d-8c69861a5516 | -12.88008 | -53.47621 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6b333f6-7ecb-373e-a24d-51c5c07b537a | -12.87938 | -53.48009 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2be38698-f52e-3b85-8bda-15549d9cdce8 | -12.87802 | -53.46379 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d61f59d-2973-3685-abf6-b18468718083 | -12.87661 | -53.47152 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11409034-1a34-3b68-ace0-62a914375c1a | -12.87449 | -53.48319 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c5655664-bf7f-322c-946a-cd1ecfa10a20 | -12.87244 | -53.47072 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52a84332-661b-35ec-95b2-848ce5b4382f | -12.87103 | -53.47848 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7156d144-83f3-3078-ae81-8d692fd509be | -12.8696 | -53.4863 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1742ce2e-757f-3ab9-a8f4-7e72d632227c | -12.86897 | -53.46603 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 60cac9bc-71a9-3272-a337-05a1750c8461 | -12.86756 | -53.4738 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7cfa1460-fbcf-3abe-bec6-4e1a07708b51 | -12.86481 | -53.46521 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f7569855-232c-3c26-9987-96570d436eaf | -12.86464 | -53.46212 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b18e8d7c-d315-3c00-bb2b-7c2c726bd905 | -12.86409 | -53.46911 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8cb2ab80-0d4f-3cd1-ad17-4a2de52762dc | -12.86396 | -53.46602 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2f926eb5-e088-3cfe-8eab-1fad7bc2d331 | -12.86338 | -53.473 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1ec3d656-180d-3b12-8930-b7b33105b08d | -12.86267 | -53.47689 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 926be4bb-7488-3c93-9988-cfeac57c12fd | -12.86196 | -53.4808 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ee101ae9-57e4-3fa3-a037-1ee60eaf632e | -12.86135 | -53.46049 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6f0e27a2-9ba2-3ad5-8a8c-01f4c51b3dbb | -12.86064 | -53.46439 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 070c143b-d616-3761-a8ce-4baafa703084 | -12.85992 | -53.4683 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d5d97737-deb3-3be8-9b99-a2005be98f0d | -12.8591 | -53.46912 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b140e151-219d-3719-9f3f-d1d0cd40166b | -12.85849 | -53.4761 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b5f85080-30ec-34e6-9ee8-208a4685c453 | -12.85706 | -53.48394 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 225887c3-5cb5-34f5-aa09-b85739817331 | -12.8563 | -53.46048 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 45de4b13-3a43-3f78-a596-b93ac7871c00 | -12.85575 | -53.46749 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b62d1723-84f4-3736-aed0-8cf2b7379692 | -12.85561 | -53.46439 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 3de68fce-c181-35df-ac5f-33520187c26f | -12.85423 | -53.47223 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 2fd58f48-9625-3fa6-ab1e-d23626556625 | -12.85288 | -53.48316 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |


[Clique aqui para ver as próximas entradas](README66.md)
