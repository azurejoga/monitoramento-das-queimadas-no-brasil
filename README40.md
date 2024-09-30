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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cff12c2-8243-328b-a70d-33ec4d326560 | -10.75502 | -48.75431 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 35bed56d-f150-3709-bf12-148c1e196717 | -10.75447 | -48.7578 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8b674c12-1f78-399e-81a7-4a3f6e17870a | -10.75171 | -48.75378 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ae41e392-77a5-337f-9dca-f8a495450827 | -10.75116 | -48.75727 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 977ad063-2aa8-3f73-924c-9ac5d5f7cc4b | -10.7484 | -48.75325 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4879d8fd-67da-35c3-879c-fedabccf3e06 | -10.74785 | -48.75674 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 404b7338-f188-335a-aec5-dd71b54fc86b | -10.74454 | -48.75621 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ab17dbc-16d8-3602-ba27-f42a6d02ece0 | -10.72175 | -48.72713 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 494045b6-bdd1-354f-ba10-64c80cb5ed09 | -10.7212 | -48.73063 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d0272a2-cc5c-35ba-8a74-c68759ac3180 | -10.71789 | -48.73009 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ba866566-4930-3cc3-980b-812702262fb3 | -10.71734 | -48.73359 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1413f60f-c220-3a57-b0ed-ef2abee1b25d | -10.71625 | -48.74058 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2db7fb3-ebe9-3b52-8968-d9f3d4b0a320 | -10.71349 | -48.73655 | 2024-09-30 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 037d5658-4626-3e87-a750-6bdd07952ded | -10.84573 | -48.15108 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 303ea2f2-fd77-3149-8aab-20c13c87288b | -10.84518 | -48.15459 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23c9a374-4284-3dc1-b075-21992c6d4a5f | -10.84241 | -48.15055 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db26b856-4169-356f-8275-3d7d18763c3b | -10.84187 | -48.15406 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 737a916e-f04f-36c5-82e7-aa8a5d64e715 | -10.84017 | -48.14304 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f855058-0656-356b-b282-2d4b5d97917b | -10.83963 | -48.14653 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 834d4c40-9e30-327d-b005-b28f9294c012 | -10.83909 | -48.15003 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 473ea355-d872-3ee4-a6a1-de53d232b7e4 | -10.83855 | -48.15352 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8344f7b1-57a4-35b0-b2a2-6c3ead718d4a | -10.8374 | -48.13902 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a8adf1c-0817-3104-8d34-6186b61b30aa | -10.83685 | -48.14251 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a9c7dbd-fbe0-31e2-a332-9ee4f5606ced | -10.83631 | -48.146 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb3e131d-3573-3e56-b1fa-1b612fd2eaef | -10.83572 | -48.12786 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e18fc7e-369c-37d0-9008-7bbcd84fddff | -10.83517 | -48.13141 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b4dfd0f-a47c-3ce2-bfd0-e68c07e027e5 | -10.83408 | -48.13846 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db57a92f-f27b-3b6a-b302-53c707c8dc18 | -10.833 | -48.14545 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 35601ab1-70f1-359b-8241-be324168e75e | -10.8324 | -48.12734 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9642332-3da9-36bd-a73f-eb161abbebf5 | -10.83131 | -48.13439 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ceb28e3-6c54-3a86-ae8c-5f7ce200e5c9 | -10.83076 | -48.1379 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b5c37c5-02ef-3f3d-a9b1-ea3249b94aff | -10.82963 | -48.12326 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93381a24-bbb8-36c7-a995-4bb3b35e83d7 | -10.82631 | -48.12274 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3006eb12-c37a-37f9-821f-8006a581ee64 | -10.82467 | -48.13331 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08f2a73b-ec8e-37e2-83bd-9763b0013ed7 | -10.82413 | -48.13681 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a64fb1d9-1bd3-3c22-90ae-91676199f9fc | -13.48971 | -48.58849 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7826c422-c225-3591-8567-39c7502e6b67 | -10.8219 | -48.12927 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85bafa89-5f5f-3151-8c38-0a0854f8b7fa | -10.82135 | -48.13278 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54d664b4-a3dd-3f4f-a5c5-7af9552ec366 | -10.82081 | -48.13628 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e6fae71-68b9-3871-9b70-b125ca814f0b | -10.81818 | -48.13198 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ada6b07-fc31-30ce-8045-bcfc33b28e85 | -10.81764 | -48.13549 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b4bf7c2-1420-347c-afd3-78f25e693a2d | -10.72249 | -47.98353 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08b2c32e-e3a5-389c-9088-b8a8246f84af | -10.71917 | -47.98299 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23dabb51-3be0-3c77-a3a7-2eeb64db31ba | -10.71863 | -47.9865 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5471b112-ca76-305d-8a53-453c8a6cad2a | -10.71808 | -47.99002 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdc7e39e-56e7-3f24-bea5-faad5078b80e | -10.71477 | -47.98947 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb5226e5-edf3-3eb6-97be-f5444234a295 | -10.71308 | -47.97837 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5eb9c257-50a8-3582-b1e8-261c67f3c404 | -10.71254 | -47.98188 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f327228c-707e-3d69-a6d1-36c75f7e7fa2 | -10.712 | -47.98539 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 208dab92-5909-3322-95df-e74f602c40e5 | -10.71086 | -47.97078 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b1f9579-06b4-3120-9928-bc71d0c47949 | -10.70977 | -47.97782 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ffb79fc3-e0da-374a-9bac-e6323eca891c | -10.70867 | -47.98486 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c6d2f15-b77f-350c-bcf2-c0867c920922 | -10.66538 | -47.93452 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35c7c230-6d7a-3518-bd95-73ecc57f5989 | -10.72195 | -47.98705 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1fb7caaf-0f42-3c75-873f-8f3ca7cb1227 | -10.71531 | -47.98595 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebf211be-b5b6-3c03-9c40-29bbcee6c3a2 | -10.71363 | -47.97484 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7afd307e-2668-323f-a97d-8c33dc5c77d8 | -10.66593 | -47.93098 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93b350c5-7e55-3629-8dd4-d531b919f9bf | -10.66284 | -48.03909 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf7dd83c-dc01-383e-a82b-758f801f4d3a | -10.6623 | -48.04258 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 997a9252-6fc3-372d-9fef-895dc90221ce | -10.66096 | -47.94112 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2398414d-0870-3845-8004-b97f794b18bd | -10.56625 | -48.04868 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 961f47df-f3d6-3255-b2c8-89fa1f5748c3 | -10.56239 | -48.05161 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ccc78751-f886-363c-849f-1acf5e675d5c | -10.55413 | -48.06105 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b84147fe-917c-3a9e-822f-7d9dc1494be6 | -13.48917 | -48.59203 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8a5ef651-1aa2-3e83-a98b-1b546ee3ef16 | -10.55299 | -48.04647 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03876767-7596-3afa-b7bb-35caf5ff2b02 | -10.54574 | -48.02736 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7a4df3d-3cc9-39f8-b3cb-73cde8a491ba | -10.5452 | -48.03088 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2324117-35c0-32a3-af6c-f659ac45dafa | -10.54465 | -48.0344 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 002a0f8b-c278-36f7-ac40-22c9a2842b4b | -10.53964 | -48.02287 | 2024-09-30 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec098310-2808-3b14-8fda-7c49e098ab37 | -12.07107 | -49.13174 | 2024-09-30 04:32:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e023de8-34c1-341d-b178-a0e25d5cf886 | -11.58372 | -48.42626 | 2024-09-30 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c30c1e2-1566-332f-8c83-7798d1220eef | -11.58317 | -48.42978 | 2024-09-30 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbfd9931-69f3-3d7c-9368-c0c714cf9555 | -11.58262 | -48.4333 | 2024-09-30 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc7f318d-1f6d-37fb-a147-dc8d5746bd1c | -11.58208 | -48.43683 | 2024-09-30 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26014d58-c308-3e1b-a64d-b3ef1d5ebae6 | -11.57986 | -48.42925 | 2024-09-30 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b6c7753-cfb6-32ba-86ee-f8506bd2a65a | -11.57931 | -48.43278 | 2024-09-30 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 197060f2-c1fc-3e73-817f-ea552bd4c3c9 | -11.25022 | -48.9091 | 2024-09-30 04:32:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06ff8c35-46c0-3421-b431-8c60353dec80 | -11.24746 | -48.90507 | 2024-09-30 04:32:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69edff16-ba4a-3730-8761-97caff50f040 | -11.24691 | -48.90857 | 2024-09-30 04:32:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 273e8b87-dc4e-30b5-bcdc-d70b6d74bc18 | -11.17859 | -48.49877 | 2024-09-30 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa3f1fa0-7637-3c9e-8824-c4756ca7c5bb | -11.17528 | -48.49825 | 2024-09-30 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccb47419-382c-31f5-9584-04d803c71d4e | -11.17473 | -48.50175 | 2024-09-30 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8de0d22b-21b1-32fb-98ab-3d71c29008fb | -11.17418 | -48.50526 | 2024-09-30 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdd47415-28e2-3f40-b944-9f28cbbf90b3 | -11.17142 | -48.50122 | 2024-09-30 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f90bc25-8de0-3e8e-a596-417b112d6b43 | -11.17087 | -48.50473 | 2024-09-30 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 808195f6-78c5-363b-bd3f-b234bcf11c42 | -11.05328 | -48.43211 | 2024-09-30 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62a3546e-3005-37ae-9771-6f9b7cb5372b | -11.75561 | -47.8382 | 2024-09-30 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c74f04e-0503-37dd-80db-416105b3e9e0 | -11.75507 | -47.8418 | 2024-09-30 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a4b51e3-2ee6-3676-a60e-2626bd45eaba | -11.75008 | -47.85205 | 2024-09-30 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 524b69f6-8b28-39ca-83d3-d4bdaf6ad6bc | -11.68245 | -47.83032 | 2024-09-30 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaee6486-1e1c-3dc5-9772-767a4b581259 | -11.65457 | -47.83333 | 2024-09-30 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf85c7bf-ec44-30da-b160-9c9d889a22e4 | -11.65068 | -47.83639 | 2024-09-30 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac3d0003-991f-3da4-90d2-ad49d0594087 | -11.64904 | -47.84716 | 2024-09-30 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6e913cb-caa2-3eb2-a6f5-93e88f3d4b32 | -11.52132 | -47.81619 | 2024-09-30 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 948a3443-aa39-344f-a805-32c869758b05 | -13.18565 | -48.51448 | 2024-09-30 04:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00f33b23-113b-3381-9496-7ffb036a4bcb | -13.1851 | -48.51807 | 2024-09-30 04:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f321aee-d618-32a7-a35d-123da06a372f | -13.18288 | -48.51036 | 2024-09-30 04:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e30d52f-c755-3178-bb2a-cf6964c8ad5f | -13.18233 | -48.51395 | 2024-09-30 04:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f898c4a8-59c4-33b4-9b9c-4e43c81bf171 | -13.17955 | -48.50983 | 2024-09-30 04:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25680ace-b10e-3b74-900b-4d65e3e7ded2 | -13.20901 | -48.56193 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README41.md)
