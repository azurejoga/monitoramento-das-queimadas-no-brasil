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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81e61f29-b10d-3cff-81d8-b657011f11ed | -5.36923 | -48.91508 | 2024-10-08 04:32:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2cf954b-ba03-345a-b1ff-4d2e8026e4cf | -5.32943 | -48.22256 | 2024-10-08 04:32:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19ea0730-ab1a-3e56-8a1c-c8465ef0c8c8 | -0.70823 | -48.57851 | 2024-10-08 04:32:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d842db22-3c08-3d8e-b7fd-bdc243e525d0 | -2.14846 | -48.90964 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dfe141f-2b29-3b77-9339-81910ddac40a | -1.44751 | -48.87853 | 2024-10-08 04:32:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8bf155c-2425-3129-82b4-21b07bbdc1c5 | -1.44692 | -48.88228 | 2024-10-08 04:32:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92c92426-877f-3369-b4c9-8a8dbca3c827 | -3.50832 | -50.27145 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fc1f422-5380-3283-97c1-e9e187718175 | -3.50474 | -50.27089 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 702cc0e0-63a6-362f-bf35-c8fa8fccf99c | -3.50408 | -50.27499 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73cc3e18-5d83-3c8b-8890-68e7cca2fa04 | -3.50116 | -50.27031 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82f6ea0d-748e-3b83-8f8b-0c127cdccbde | -3.5005 | -50.27442 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cf6ce97-ab55-36a8-86bb-e9294cd5f12e | -3.49039 | -50.49878 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7553dba-edbe-31eb-b404-5321b57b9386 | -3.48289 | -49.95401 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dc15900-cdcc-356c-aaeb-071865c2b5a8 | -3.43156 | -50.32394 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a468298f-ac4f-3ad2-88ce-fd843a82f49c | -3.42796 | -50.32334 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd69251d-9468-3d20-b834-531f6d78812f | -3.41226 | -50.32933 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08d433c1-967f-330a-b4b9-845009c7f587 | -3.40866 | -50.32877 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e173071b-42ec-3fd5-9b5a-dc047984879e | -3.32792 | -49.13716 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1214e68e-8f77-3ee1-a3b3-46ab25abe3ac | -3.32674 | -49.14457 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e91e9e3b-e58c-3bb1-8382-693507682d1a | -3.32495 | -49.15571 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 971f8873-acc5-31f6-b062-69885aa26f05 | -3.30751 | -50.46762 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0f551f6-069e-3f5d-a232-b77b461aa816 | -3.30388 | -50.46705 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 481acbca-dd1a-3b3e-8a94-244247484c66 | -3.26861 | -50.13482 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe4c8d6c-92ae-359a-bcad-bd23494fdd43 | -3.26637 | -50.1314 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aedb73c9-c120-3225-85b1-77ab2f20f7ba | -3.26625 | -49.105 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d27c348d-b507-3e36-9a84-eaa4d7bb3570 | -3.2657 | -50.1302 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f6f3f18-3e84-3925-94df-c560b72b0662 | -3.26504 | -50.13426 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 810f9864-1137-3e85-8e12-dcddceede532 | -3.26224 | -49.10817 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74193128-8e2c-3a3b-a6ee-3603baa0e736 | -3.26147 | -50.1337 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5026e6d-6507-365e-b35b-9b1569ac58fa | -3.15975 | -49.75147 | 2024-10-08 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f72fb7e8-99ad-3e24-bd8c-f078003fbc38 | -3.10642 | -50.38699 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b587ca0c-dfc6-35dd-a9b5-e09acc4b4bd5 | -3.10575 | -50.39125 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 006c7b13-d4fe-3db6-8e97-8897ac9e961c | -3.1028 | -50.38638 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99c3296f-20b3-3669-8cb2-98eef0465b24 | -3.10182 | -50.46707 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a51f00f-cec7-3ace-8392-e6b926370f76 | -3.10108 | -50.46822 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46b7e71e-c52b-390a-8829-7b243c061d02 | -3.09887 | -50.46229 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 666cf164-aa1c-3d58-b541-29cff382499d | -3.09818 | -50.4665 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 746df2b2-ee6a-36e6-8379-9f358381a1a6 | -3.09811 | -50.46342 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ae4ad80-ab2c-308e-b143-c6b7ef5fcea9 | -3.09447 | -50.46284 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3be3eb8-0be0-31f6-b631-97a5f246279d | -3.06792 | -50.48912 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4c234be-5913-3f71-a606-fb79ab63a3e8 | -3.06427 | -50.48855 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b02fa384-e6c0-3bed-91e5-06cc8b414499 | -3.05403 | -49.61898 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b46e53b9-911d-3b78-adde-9b0a91819242 | -3.03894 | -50.43695 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc7d8804-0818-38fe-8994-0d1b6b94b738 | -3.0353 | -50.43641 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbc1b6d3-60a1-3e6b-a62b-9c6fa1249131 | -3.03463 | -50.44056 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acb6d865-0376-3ac3-af1b-f6c5bce19e36 | -2.98452 | -49.52946 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 195f58aa-92ee-3659-82dc-a3e045007564 | -2.98391 | -49.53332 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 571f4536-e81d-3c7b-95b4-fbb74c790d96 | -2.98165 | -49.52509 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 1738d768-913b-3517-9ff6-b534e7e365b3 | -2.98104 | -49.52893 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6ba6df5a-aa98-34cd-80cb-88f9929b203a | -2.98042 | -49.5328 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e841388-2ebd-3520-80b4-20c594551bb5 | -2.64248 | -49.26961 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b665e236-a5d0-3dff-ae77-fae0fac0d0dd | -2.6399 | -49.2697 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e1d7dde-cdc5-3439-b076-d33010ca0629 | -2.53637 | -49.29645 | 2024-10-08 04:32:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c465e17d-a25c-35b4-816f-b5d3570b4842 | -2.53463 | -49.02219 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7fa6bfe-bdcd-34ff-847f-446c8df51867 | -2.53121 | -49.02165 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c37aa4f4-584d-3d16-8f31-4d77184331aa | -2.45574 | -50.25711 | 2024-10-08 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1de3c2de-7b30-3b41-9954-5e2eed124edb | -2.45212 | -50.25654 | 2024-10-08 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd00fe60-b898-3098-992e-9920870959a9 | -2.45145 | -50.26075 | 2024-10-08 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e56d57f-bca8-3f14-bd4f-5018990de092 | -2.37981 | -49.09038 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6dc8f45-40fb-3656-91a0-07f50285b3fe | -2.35001 | -48.99041 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e738eb86-4a2d-3348-97b3-bc34a9f90188 | -2.34658 | -48.98988 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbd8ce64-ce60-380d-8d7f-4f85426236d0 | -2.89536 | -50.39767 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 598b2a81-150c-3582-80d7-6c7918aa9462 | -2.89467 | -50.40191 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21aa031e-f412-363c-bbf1-43a40f2b2c15 | -2.89448 | -50.39883 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffaab2d5-e891-385b-baeb-55b4f530f972 | -2.89172 | -50.3971 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5156c30a-dcbe-3791-94af-5ae2b0d9bd1b | -2.89103 | -50.40134 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d83d324-4bd3-38d6-b273-06b262b22cc8 | -2.89084 | -50.39825 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 222e1188-ac1d-3e87-bd1b-b2ddb0ce6fb8 | -2.89017 | -50.40251 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64775e80-b648-31b0-961c-2be531a9f319 | -2.85029 | -50.4659 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9aa8da2-9398-3d01-af70-e5d6a253d03e | -2.78925 | -49.52338 | 2024-10-08 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e11ff82e-c09b-3671-912d-f71c9580c52f | -2.72621 | -49.53736 | 2024-10-08 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d78bf0b9-08d1-35b4-bf8a-30597493188b | -2.72271 | -49.53682 | 2024-10-08 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b120f3ce-726b-3d22-8d0d-272d8681da54 | -5.00814 | -49.59287 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 00603c60-485b-3387-b953-daebfb6c411f | -5.00471 | -49.59234 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61acef86-f70a-3dde-bd1b-f3c2db6cf97c | -5.0041 | -49.59609 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 648f8774-a62c-36cc-8c4a-8278cc092bac | -4.95068 | -49.64561 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 717fb4b7-080a-3c1e-a9d1-38860881219e | -4.94724 | -49.64508 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bc33f2d-8b88-358a-a51e-069762cbdbc2 | -4.87315 | -49.9533 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d5ef16a-27a7-30de-b36e-435ae3436396 | -4.87253 | -49.95716 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26507089-e927-3e54-b00b-bd3cbfa2186f | -4.85415 | -50.76933 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 264e9498-f420-391e-b0aa-d8070fa1c107 | -4.85053 | -50.76873 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 519a6439-ac93-3e54-b968-988d6fd947e1 | -4.82869 | -49.81698 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9142d71-d8fc-346b-be5a-2541176dc92b | -4.82583 | -49.8126 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8383fcdc-57c9-38d7-ba20-e221b3ba35f1 | -4.82522 | -49.81644 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88d4bf53-134c-3b45-b88d-f92e3060b617 | -4.82353 | -50.82056 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ac7162e-010f-3612-bab0-74c0ebaa0141 | -4.8199 | -50.81997 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 085840f6-3208-3386-8105-933514858044 | -4.46541 | -50.50296 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 759e0a21-4ddb-3d74-a449-96e24bfcbba1 | -4.46183 | -50.50238 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ae3b461-2461-3bc7-a65b-fee8fdfa4230 | -4.42332 | -50.78783 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28a14a53-5a3e-37a5-901f-200a3ecb8a5e | -4.41967 | -50.78725 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17ec5e53-de94-33cf-a665-0974ff738a1d | -4.37405 | -50.81491 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaee369d-f492-30f1-90e0-ac83fbfe2b15 | -4.17067 | -50.74984 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a226639-8ff2-3113-8eb7-2cbce71babf2 | -4.16997 | -50.75414 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79fc2bcd-1a06-363d-80ed-6362b8710c32 | -3.95066 | -49.95926 | 2024-10-08 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3bddfe4-b6d1-3168-9a34-90dcfe8c2d14 | -3.94715 | -49.95866 | 2024-10-08 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1eb453c5-52a9-3727-9af3-cf832901598e | -3.94651 | -49.9626 | 2024-10-08 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5f66bf0-461e-33cf-8211-e0b4c306ebb2 | -3.94623 | -49.95939 | 2024-10-08 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f4f8eeb-42f7-301f-87a2-ef303781114e | -3.94561 | -49.96334 | 2024-10-08 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1711dceb-8cf8-3dfe-9c9b-8dd0e726340f | -3.7357 | -49.68761 | 2024-10-08 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9eaa552-394b-3607-b864-2e3e6c754669 | -3.73222 | -49.68707 | 2024-10-08 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README52.md)
