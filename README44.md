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
| f1459a2f-ccc9-33cc-9c87-85434e83d8dd | -17.89818 | -57.67385 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 91f4ab91-68bf-3b52-a30c-897d2bbb53be | -18.04322 | -57.56033 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c3bef5d2-08e5-3219-adb5-59d7a36e3a58 | -17.89673 | -57.66125 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 198e0522-4aad-3780-8d46-91f344583d16 | -20.56289 | -54.65613 | 2025-10-10 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a0c4478-a3ef-32ff-9988-704ea88e4fd3 | -17.89473 | -57.67321 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cbe8e1f9-a9b5-3f6c-8773-fd86244df607 | -18.3898 | -56.16792 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 13040796-fc2f-36d6-9c4d-fbde15fb17d0 | -18.04182 | -57.56854 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e1065bc3-d2c5-3651-aabd-65c254cc92e9 | -17.93118 | -57.61843 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| eb159337-6e67-313f-a3be-570d09fdabd7 | -19.58902 | -54.02457 | 2025-10-10 04:55:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3a96dbd-304c-374f-8d15-995031816e24 | -18.03131 | -57.55042 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1be7cbbb-c945-3f33-b14e-cb233475ecd7 | -18.04394 | -57.51711 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6bb721a3-1bd5-38a5-8c64-9d7755546c47 | -18.03202 | -57.54615 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 67bc7c44-c1e7-3584-823e-c82974f31a58 | -21.72316 | -52.42159 | 2025-10-10 04:55:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3db1fce6-269e-3f35-9c25-1e781d2ed979 | -17.90018 | -57.66188 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b6189fcd-1a12-39f4-9d93-6316054f202a | -18.02719 | -57.55394 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e86980e3-a0a9-3726-80dc-ed8e8fa6cc3a | -18.06719 | -57.54431 | 2025-10-10 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3cf2057f-3699-3190-8fcc-d6375c86ea7e | -30.06478 | -51.18974 | 2025-10-10 04:57:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 3a4ac221-cff3-354b-a177-96627baf57c0 | -30.06504 | -51.19246 | 2025-10-10 04:57:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| f9c6da76-a832-3430-aaad-efde5893db64 | -30.06555 | -51.18751 | 2025-10-10 04:57:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 59da4d32-6ef5-375b-95ed-22d20246eec2 | 1.55664 | -56.06812 | 2025-10-10 05:18:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a13cb25b-b32c-39fc-9039-648a152d2595 | 0.71376 | -51.37433 | 2025-10-10 05:18:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97d7adf9-cbc1-38a6-af1f-b10b7d6e4876 | -2.92194 | -48.31319 | 2025-10-10 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0da29d0-5a35-3e3e-92ad-9e3b3dfaaefa | -2.99861 | -48.73822 | 2025-10-10 05:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1816955c-e650-3685-baf5-46fdbc9c2c13 | -2.68524 | -48.39173 | 2025-10-10 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 525272b0-4882-3cd7-8fa8-0508fc6a33fb | 2.18843 | -55.84645 | 2025-10-10 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 075f5e2c-3d6a-3189-bcf7-5978777e7ece | -1.77121 | -52.15307 | 2025-10-10 05:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a06c4f0d-ac16-37bc-82d3-2a0efcb168a9 | -2.92365 | -48.30184 | 2025-10-10 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c72342e-7f02-30b2-b466-bf355dd00f15 | -2.68248 | -48.41006 | 2025-10-10 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34eb0473-d7a0-3d63-8c74-f98b3c177311 | -2.4899 | -47.5713 | 2025-10-10 05:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6a6b123-78b8-385f-8fc4-6bfa8b6ff42f | -2.99916 | -48.73466 | 2025-10-10 05:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f885a95b-0eaa-30d8-954f-312c37c6dc0e | -2.29584 | -47.99236 | 2025-10-10 05:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 392cdd02-f039-392e-a484-0c637f171cfc | -2.67688 | -48.40921 | 2025-10-10 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cae4eb6f-1c74-39bc-ac84-49eece9d77ef | -2.92251 | -48.30942 | 2025-10-10 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d9517f1-1df6-37d1-a661-ec7ef1334ff5 | -2.29524 | -47.99636 | 2025-10-10 05:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cddb463a-f50e-3adb-8b00-f676389b0751 | -0.43266 | -51.73057 | 2025-10-10 05:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 870d6abb-dbf8-3ee1-b267-41997ae65aa1 | -2.92308 | -48.30566 | 2025-10-10 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c109dde6-c740-33cd-9192-6f775319b2a5 | -0.43697 | -51.73122 | 2025-10-10 05:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2463e5c6-4a0e-366a-b405-bb0146bdf948 | -2.67632 | -48.41293 | 2025-10-10 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18a58954-61ab-3583-a7b9-ace1e4b78472 | -2.68581 | -48.388 | 2025-10-10 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 571ca3b9-06b0-3ef9-a114-2367cd576074 | 1.13237 | -51.40928 | 2025-10-10 05:18:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c27b451-3bc5-3ad6-934a-c0fc5303de7e | -2.4958 | -47.57218 | 2025-10-10 05:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e0b759c-2b1d-3485-9896-a0c9df3b23f1 | -1.54337 | -55.41187 | 2025-10-10 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7b6deaf-db25-3316-9163-4fcb0551e21c | -3.00389 | -48.7361 | 2025-10-10 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef69e633-c1da-3aee-9afb-d1967a6cc04c | -6.66434 | -47.74685 | 2025-10-10 05:21:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c11d5ab-c748-38a6-8ec9-eedbda43f6a6 | -6.66368 | -47.75156 | 2025-10-10 05:21:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9ef0ba6-cd8d-363a-bdc0-c0ff9f7f34de | -6.66259 | -47.75298 | 2025-10-10 05:21:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfa6fc6b-36b4-31d2-89b5-b11c61466592 | -7.24632 | -49.51769 | 2025-10-10 05:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49134622-d57c-3a81-9106-92ed3ef6f53e | -3.29299 | -52.61642 | 2025-10-10 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b38eff20-69ba-3999-9a7a-03851ec55818 | -3.17397 | -51.25238 | 2025-10-10 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d94ab44-b360-3700-b780-106143675c49 | -2.94242 | -49.34066 | 2025-10-10 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13b81feb-a5f4-3133-bd1c-ac016d7923a0 | -2.94869 | -49.33486 | 2025-10-10 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91452ea4-6117-39cd-9322-9d6611f5aa63 | -2.17202 | -54.47439 | 2025-10-10 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77490f50-7c1b-3041-8db7-a3f2b6aa6ae5 | -3.17325 | -51.25723 | 2025-10-10 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c298df2e-d81e-38d8-9c36-e6f71d0909f3 | -2.39708 | -57.23291 | 2025-10-10 05:21:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d7ffad3-ca1f-35f2-b2dc-2adf795ded8d | -2.9477 | -49.34147 | 2025-10-10 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 85df506b-a270-3399-b6a6-9f7c20dd681d | -2.99839 | -48.73525 | 2025-10-10 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f01cee7-04af-330f-8d04-56c87d9753d6 | -5.05479 | -45.85611 | 2025-10-10 05:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef780b1a-2597-3733-a7b2-4c7cbedf6448 | -7.24769 | -49.51513 | 2025-10-10 05:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ba9d969-0fa4-3eea-8f8b-507cd76b2ddc | -2.18619 | -54.48103 | 2025-10-10 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad8db2dc-34bd-34e8-a81a-b7b44ee9defc | -7.0218 | -59.45784 | 2025-10-10 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc54923b-e8cd-31c3-8e9b-ff64cf5b2190 | -7.40016 | -45.9236 | 2025-10-10 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 600dee59-0acd-307d-b18a-0c70f90efd11 | -3.5509 | -51.45118 | 2025-10-10 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 663b00f0-6918-37ac-93d7-1961d4450ddf | -2.94291 | -49.33736 | 2025-10-10 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad368c14-2d41-3191-9db8-63dfc7f65395 | -3.2924 | -52.62041 | 2025-10-10 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9ef7bfe-c6f0-300f-98f4-a9eb3a4dec96 | -3.55034 | -51.44944 | 2025-10-10 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67f971e5-ebe3-300b-a3f1-71ad61670a3c | -6.66321 | -47.74827 | 2025-10-10 05:21:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6b28518-88c1-3de7-bf5a-1dadd70e29bc | -5.05569 | -45.84965 | 2025-10-10 05:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3fa096d1-813c-3b31-a7fa-686850b4b0e7 | -7.40714 | -45.92453 | 2025-10-10 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 824d6d8c-0b9b-3c33-919c-63971488bb20 | -2.9482 | -49.33816 | 2025-10-10 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6af3337a-0a26-3512-bf35-7e6b0451b8a2 | -7.24681 | -49.51397 | 2025-10-10 05:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 311710c3-fdc0-389a-99c5-9d91c786bd38 | -9.28587 | -58.03625 | 2025-10-10 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8772941e-11d1-346a-bcb4-b07944b0d217 | -5.85126 | -50.07505 | 2025-10-10 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d95b7d78-51e7-3750-9270-e75581f7e035 | -7.24717 | -49.51884 | 2025-10-10 05:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3dd673a-4508-3743-b516-b969dcd70a0c | -7.05172 | -45.04902 | 2025-10-10 05:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f57dcdfa-9a71-3121-bb30-97a4b317fe61 | -2.18991 | -54.48159 | 2025-10-10 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7bbf62b7-3778-38fc-865d-3c6536c8c535 | -13.35637 | -47.75713 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9e5d3d0-6859-32c3-b5e2-92f992ce9972 | -14.69085 | -48.06898 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e0fdeff-b62a-3407-80ec-311b4dac0d1b | -15.74633 | -48.99112 | 2025-10-10 05:23:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab2b9445-e277-36b5-a772-ad561e94ade5 | -14.8577 | -48.47156 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2abfe168-2b6b-3f4d-afa2-cab82abcf0c4 | -10.21421 | -59.52263 | 2025-10-10 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54aa09c8-8101-39bd-8660-8387005e6e18 | -14.94838 | -46.78041 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2cc8e224-3451-3972-b987-c0e9e17ad0c6 | -15.08525 | -46.60252 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f99995be-3edc-33cc-ac13-a317cff5d5d0 | -13.32779 | -48.48325 | 2025-10-10 05:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 733aa093-f6c3-3206-86b0-c243c680e302 | -14.92588 | -46.78641 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a56f1de0-3fd0-3ff5-a8fc-ce910858ca50 | -14.42726 | -48.00426 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4ca4b68-f40b-35ef-aa5c-9a39376d4c0a | -10.08085 | -67.53732 | 2025-10-10 05:23:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a066f43-bb98-35d9-8c93-891755edd7eb | -14.88291 | -48.23296 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0bf10f92-8731-30f1-9ac3-76e782ee61d7 | -12.08852 | -64.23001 | 2025-10-10 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37d3c76f-b8df-36b3-a9e5-6a7f313501dc | -14.92662 | -46.77893 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d89f854-b14e-3160-a48f-ea4103bc8f5b | -15.09283 | -46.6001 | 2025-10-10 05:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51604201-d338-383e-827e-e3458a6c71af | -11.25824 | -61.46386 | 2025-10-10 05:23:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5505c30-997d-3092-a854-82d0314cb8b0 | -15.972 | -59.53604 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5656cc8c-75bd-3be1-ae3f-597754d74d04 | -15.74824 | -48.98648 | 2025-10-10 05:23:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 724dfac6-b4a8-36f4-853b-a0e8354dc5ef | -9.7917 | -63.17558 | 2025-10-10 05:23:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cced023-78fc-3d6f-b401-27a35f08ec67 | -13.37326 | -47.75504 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3428ee66-9dee-378c-8c01-b38ed4cf3c1d | -16.01183 | -59.55014 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0b231c8-c14e-3cfc-94aa-05f5635e2664 | -14.87554 | -48.23911 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8b30da5-94e1-365f-b540-0f4091195538 | -14.69149 | -48.06291 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0831a7e-4593-3406-9de6-c973293b0573 | -8.51972 | -66.99897 | 2025-10-10 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 817e9620-2c8a-304e-8469-e9160dfd92b8 | -13.3598 | -47.75372 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README45.md)
