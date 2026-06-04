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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43c25f58-2962-396b-94f0-744624ea4218 | -16.438 | -57.26983 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1d228e58-2515-36ba-8fca-5c0b841e5b0c | -19.72631 | -54.65238 | 2026-06-04 04:46:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50aedf0d-c516-3374-af84-e1a5ddba3819 | -16.18608 | -58.46798 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| eb73734d-f6e6-3536-9197-f39517f7a8ae | -18.23632 | -54.59566 | 2026-06-04 04:46:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05f010f1-2490-32fb-a359-0e38de8d6991 | -19.74049 | -53.54851 | 2026-06-04 04:46:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3238bbf-3711-30de-9ed9-807531ec3f35 | -16.12151 | -58.50413 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| db20ed67-653e-36d0-a7f4-e86b300bf10c | -16.80121 | -54.17337 | 2026-06-04 04:46:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff3fe143-fc1e-36a3-8f27-26f30ac3c8e4 | -16.5925 | -58.23712 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 957adee0-d10a-3ddf-8073-ed3c42a6d8cc | -23.54611 | -47.63627 | 2026-06-04 04:46:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8db5988b-277e-330f-9475-cbe000d6c37d | -16.26819 | -59.72578 | 2026-06-04 04:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6f1b7f2-1086-34da-989f-b4e98c872929 | -16.18382 | -58.47914 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 741933c1-ddbf-38f0-a980-8330e940bf38 | -21.55591 | -48.59445 | 2026-06-04 04:46:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3779d3cf-faf3-35be-ad12-b84e56d3f8a2 | -19.1672 | -55.18324 | 2026-06-04 04:46:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ef95d491-9878-301d-834a-ea771db3f945 | -20.49631 | -54.67789 | 2026-06-04 04:46:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f5c8006-01bb-3d0a-a975-b205b4328278 | -16.18981 | -58.47463 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 817bd2cb-63d3-3f97-85ef-b298043d8702 | -17.46384 | -55.19664 | 2026-06-04 04:46:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a16e6e79-1748-3bad-b9fa-0b3d6b1bfd97 | -16.802 | -54.16892 | 2026-06-04 04:46:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80c612b4-40e4-3ac3-9cde-9e914cedfed3 | -16.18872 | -58.47201 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 706fd08e-7fce-3cda-8740-032568769a71 | -18.39752 | -51.45299 | 2026-06-04 04:46:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29087c2f-0a2e-31ef-91fb-cbbe2843e43c | -18.23723 | -54.59745 | 2026-06-04 04:46:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ce85f23-5903-3046-a4a0-f550de09dba9 | -17.45937 | -55.19914 | 2026-06-04 04:46:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| bda66a42-bfad-3dda-a816-6d49781cca91 | -16.60093 | -58.24453 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1481b221-ea25-3703-a36b-3a13f66effda | -16.60463 | -58.2509 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9590cb53-02ce-39e4-9963-92fbda68e6ac | -20.49656 | -54.67639 | 2026-06-04 04:46:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47202345-2d8c-3bee-9fb1-dcf2093f1d28 | -20.02542 | -48.19016 | 2026-06-04 04:46:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edca7800-33f7-336f-bd02-fe4f91ae0931 | -21.55184 | -49.86786 | 2026-06-04 04:46:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ec7e30bf-a7ea-36bf-9eee-ea787f80de22 | -18.46573 | -54.70475 | 2026-06-04 04:46:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cea5c599-c3f3-355c-9af7-d89898b028d6 | -23.07272 | -55.18204 | 2026-06-04 04:46:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8e07d4ed-c1b8-3168-8be6-3a0cd3799bc1 | -16.43929 | -57.26844 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0d366a5d-864b-3455-b33d-1f4b9135671a | -21.95303 | -57.5967 | 2026-06-04 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cdcc8e8-d695-3f41-ace0-cf1be958654f | -23.50961 | -50.04387 | 2026-06-04 04:46:00 | NPP-375D | GUAPIRAMA | PARANÁ | Brasil | 4109005 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5ea9a8d1-b099-32c4-b241-502f4aa80450 | -16.14324 | -58.49706 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 09fb5e3a-7a17-33f6-9900-6835c18719ab | -18.39693 | -51.45667 | 2026-06-04 04:46:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f0d645c-19f1-392a-9f38-159c03173d0c | -19.73631 | -53.55188 | 2026-06-04 04:46:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc94fc25-7310-3e37-bc3c-b732920b0b0b | -17.46325 | -55.19988 | 2026-06-04 04:46:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 466fbed8-323e-382e-b43a-47a105088837 | -18.86921 | -47.64584 | 2026-06-04 04:46:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f5e052b4-0b4a-322b-ab20-1dbf2e5963ad | -16.59987 | -58.24988 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7d76a544-147f-34ba-84f1-f9d846f2e573 | -17.96394 | -44.3518 | 2026-06-04 04:46:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eba6c4fb-f0f0-303b-973b-bdc9eb222c37 | -22.97162 | -52.69428 | 2026-06-04 04:46:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| becd8aa0-41e4-3449-a5c0-8537f6af1fb7 | -21.55171 | -48.5982 | 2026-06-04 04:46:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2f439656-fddd-36d8-86d2-68e59e73d880 | -20.02483 | -48.19445 | 2026-06-04 04:46:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aadf168b-e3b9-306f-81fa-43eca63aa7de | -16.19093 | -58.46907 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 032d673e-875e-3393-80e1-36c96fe86a03 | -16.13017 | -58.51176 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 79127f25-5eed-3546-b499-438ea1a241d6 | -16.74772 | -49.93507 | 2026-06-04 04:46:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a7b96d36-ab78-3dc6-b4a8-1ea2682b4a31 | -17.46415 | -55.19482 | 2026-06-04 04:46:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| bdd3e132-3440-343a-9e00-96b70d8ad6f4 | -12.2136 | -57.2888 | 2026-06-04 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 1c33d095-03ea-37f6-813a-8d9ea539f6e4 | -12.2138 | -57.2688 | 2026-06-04 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| cf916b4c-110d-38ef-a98f-e2a373ce5395 | -12.2325 | -57.2872 | 2026-06-04 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 114cdc1a-7f56-3121-b03f-46feaea7c64f | -12.2327 | -57.2672 | 2026-06-04 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 33afccf8-30a0-321c-96ce-d01758ba675a | -6.9835 | -42.88715 | 2026-06-04 04:59:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a1787985-589f-3a58-92a1-06d70e9be334 | -0.08954 | -51.27949 | 2026-06-04 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daeb5c18-baff-334c-aa68-4b9c2ee98b07 | -3.98927 | -47.92958 | 2026-06-04 04:59:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce93121c-725b-3ddf-82c7-fd06331f992b | -3.98448 | -47.93273 | 2026-06-04 04:59:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 126215bf-4e5b-370b-ab25-8d7fbe4f61eb | -3.98506 | -47.92883 | 2026-06-04 04:59:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad93851f-825c-3b24-b83f-6e8ae1b81168 | -3.98869 | -47.93344 | 2026-06-04 04:59:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8487354b-0333-3aaa-858c-9bcf40b43a1a | -5.72408 | -45.03693 | 2026-06-04 04:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c79c86d1-ee4b-3b4e-b6ba-2d63d4e3850d | -6.99104 | -42.87813 | 2026-06-04 04:59:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 261f3f2a-e2de-394d-8a28-3355b4d9081f | -6.98971 | -42.88795 | 2026-06-04 04:59:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8fe47635-16d5-3d7a-b5b7-6c57c6fffa22 | -2.16689 | -52.75549 | 2026-06-04 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e49ec2f9-fba1-3a94-b421-acf7c54da1ad | -6.99172 | -42.87318 | 2026-06-04 04:59:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ac99470a-9112-3bf3-a390-8dd22752c6ce | -6.99038 | -42.88305 | 2026-06-04 04:59:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4022feb6-0d9a-38d2-9c8c-5dc68ca62f6b | -12.2327 | -57.2672 | 2026-06-04 05:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4d652d00-f6e7-35a4-aeec-f59433e54636 | -12.2325 | -57.2872 | 2026-06-04 05:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 6a061438-ccc6-3445-9baa-8529c62c2d42 | -12.2138 | -57.2688 | 2026-06-04 05:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 81ac1484-2f94-3be0-8dd6-5127c62403e1 | -12.2136 | -57.2888 | 2026-06-04 05:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 44a06fc1-f7a4-3b05-a7fc-aef27ba7036a | -10.81766 | -56.59336 | 2026-06-04 05:01:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72c4c75a-aa58-3174-a130-ccc83cc09ba6 | -9.52746 | -47.75512 | 2026-06-04 05:01:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dd074b6-adc2-37cf-aecf-2c949bf8c752 | -12.20976 | -57.28782 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d4931012-213b-3c56-a94b-efb093516aa9 | -14.04876 | -46.33982 | 2026-06-04 05:01:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d68114a-1182-3336-8252-eb4c8b63fcd6 | -8.57714 | -45.99985 | 2026-06-04 05:01:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d570c43f-6c66-3808-8032-25668954bd37 | -12.22921 | -57.27579 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d3f1aa5-0feb-3fc9-bf89-f641f5dfb754 | -9.18188 | -58.05587 | 2026-06-04 05:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 688f8329-22f9-3d04-a223-cf0cc292c92b | -12.21316 | -57.2884 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8612aec8-530f-3738-bc1b-79ae0e3dacd6 | -12.17586 | -54.5402 | 2026-06-04 05:01:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07014560-50f7-39f3-901e-e1aad4047a23 | -11.54989 | -52.78666 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2ab92f6a-77db-3143-9b62-0acb06504c63 | -12.22119 | -57.28209 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 89a68e89-626b-32ef-873d-bb1fa8948cba | -11.63068 | -55.18597 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0f5b530-5db4-3300-9734-bf6760c1f8df | -10.86114 | -53.74371 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 446c9f40-79ff-3752-988b-919bf13efeaa | -9.80592 | -48.23991 | 2026-06-04 05:01:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ebce74c-1bb7-3dfa-853e-0b5a35f910c7 | -12.45518 | -58.46976 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| efed590a-991b-31c9-9474-f111a9907878 | -11.54227 | -52.78952 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 31f88f49-2527-3095-8914-12eb21ac10e2 | -10.38628 | -49.44213 | 2026-06-04 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 245d25f8-287d-32ce-9abf-f3b620912324 | -10.53295 | -46.61956 | 2026-06-04 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 713ab7eb-b2eb-3449-9b17-e42ea02907e3 | -12.23199 | -57.2801 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9af64ba7-66fb-333c-b7c9-ab399a8c0679 | -9.89017 | -52.43788 | 2026-06-04 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6c4347c-e881-38ae-b3d7-f7d1a8e05940 | -12.55235 | -57.18879 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1e261f9-8059-3a39-95c6-e1ee2bd7bc62 | -11.75704 | -47.078 | 2026-06-04 05:01:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff7a8e4b-9b93-3bfa-83ad-897ceebc49bd | -11.6234 | -55.18815 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9c1624f-9712-34f8-ad9e-42f07988fa26 | -11.2606 | -53.96904 | 2026-06-04 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6a3a2f5-4e65-31fe-886f-aabeeafa05e9 | -12.45736 | -58.47849 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c88baa60-5d64-3ded-8943-aafbcf149218 | -10.39412 | -49.44722 | 2026-06-04 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15a7f3b0-d427-3327-aba2-bedf032a1253 | -10.138 | -52.12854 | 2026-06-04 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72cd143e-2521-31b2-a790-7bdb5286dd86 | -9.17826 | -58.05526 | 2026-06-04 05:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32627a16-8a56-3fcb-acc9-5db03d6edacb | -13.53695 | -49.90255 | 2026-06-04 05:01:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da01287c-9fca-37a3-a143-fe95feb41f93 | -8.28634 | -48.23124 | 2026-06-04 05:01:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a03723f0-f868-372a-b219-6a9b7a9c4a57 | -12.43651 | -58.40756 | 2026-06-04 05:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e93b3b5-bf17-31b3-8fe8-ec14f990ab17 | -11.78633 | -52.51087 | 2026-06-04 05:01:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1812c88d-b849-36b1-b365-182048e1d9e9 | -12.3074 | -47.90299 | 2026-06-04 05:01:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ab9274d-fe1b-39a7-98fc-5e323312120d | -12.3026 | -47.90247 | 2026-06-04 05:01:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe0ecbf0-0f16-35bf-a418-14fb18a8c415 | -9.53211 | -47.75574 | 2026-06-04 05:01:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README12.md)
