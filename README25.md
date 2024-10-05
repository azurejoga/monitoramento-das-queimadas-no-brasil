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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5d44a21-5c92-3560-a8af-dcd927c9e449 | -19.1365 | -48.21782 | 2024-10-05 01:47:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 58589249-1f48-374c-b462-c1453e3aefbf | -19.13543 | -48.22522 | 2024-10-05 01:47:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 41.4 |
| f06b17f1-fa26-32d8-8589-895dfbdb9311 | -19.08415 | -48.23793 | 2024-10-05 01:47:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| b0df4fa1-d687-3125-b0c7-0679a79eb429 | -19.08303 | -48.24316 | 2024-10-05 01:47:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| a4a9d058-0842-3006-a469-4c15f6b058bc | -20.93239 | -49.03052 | 2024-10-05 01:47:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.5 |
| 6a035f2a-0362-37a5-a374-3548ee342e62 | -20.92554 | -49.02686 | 2024-10-05 01:47:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| 0a30e3c5-9062-36bb-ba00-c83285bcbda9 | -21.81068 | -48.75266 | 2024-10-05 01:47:00 | TERRA_M-M | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 2b3daf75-bf19-3981-89c5-43fc8ddff034 | -21.80211 | -48.76042 | 2024-10-05 01:47:00 | TERRA_M-M | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 13317165-770b-37b9-a97f-040d58916b61 | -21.52116 | -48.74071 | 2024-10-05 01:47:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 3f9ff8c1-a1ca-3480-878b-d43ffceb9f9b | -22.65638 | -51.53193 | 2024-10-05 01:47:00 | TERRA_M-M | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 127.6 |
| fe2c0205-3457-3363-bd99-475178954a46 | -20.58234 | -51.39179 | 2024-10-05 01:47:00 | TERRA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 01209f65-6670-34b5-b84f-3a70f7fb1264 | -18.50441 | -52.82222 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 3ffae6a6-3bda-37fe-8f7f-1a3f29dd57c5 | -18.50089 | -52.80242 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 228.9 |
| d0c613f3-8236-3a54-ac0c-6c000edc4d74 | -18.49893 | -52.86396 | 2024-10-05 01:47:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4ceff663-20f0-3ec1-a99f-d1a0763a5d57 | -18.49735 | -52.78254 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 585.5 |
| 81402b2d-8072-318b-86d5-1769d7582ec2 | -18.49542 | -52.8443 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| bed790ba-cdd4-39c9-a223-2194e2f055d4 | -18.49461 | -52.85007 | 2024-10-05 01:47:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 02ea73e1-799e-385f-aa37-2f0653247383 | -18.49189 | -52.82459 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 640.3 |
| ae07105a-0e4b-3a69-8be6-d3b3db86ccf1 | -18.49123 | -52.83035 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 249.9 |
| 63635fdd-cc2e-3c78-9267-0210a9531523 | -18.48784 | -52.81054 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 599.2 |
| 849002c2-ef77-32f6-86fa-46b90cdbc682 | -18.48444 | -52.79074 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 322.0 |
| 7ad453eb-5eea-3df5-aee8-9c48be413673 | -18.47587 | -52.80743 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 28.4 |
| cf188c94-2c6b-3eb7-971d-6e1bd24b0e8d | -18.47534 | -52.81314 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a4157f08-33c2-3c7b-a5e0-a137b5adc169 | -18.47194 | -52.79341 | 2024-10-05 01:47:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1c473cdd-de86-3db0-b6a9-7c2fea0c1d5e | -18.89231 | -54.53318 | 2024-10-05 01:47:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3351cb5f-a157-3db7-b08c-3fde1daac1fd | -18.88134 | -54.53484 | 2024-10-05 01:47:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ec59ead6-e90a-3f8d-90c9-23145a170b30 | -18.87277 | -54.55071 | 2024-10-05 01:47:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9a4c0f95-b3e6-3c2b-b377-79addb0e0285 | -18.87045 | -54.53697 | 2024-10-05 01:47:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 361805c3-153c-31f0-862d-324f1be35bf3 | -18.86899 | -54.54317 | 2024-10-05 01:47:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 40597b0c-fae1-3ffc-a4bd-f212bfa12d10 | -18.86667 | -54.52886 | 2024-10-05 01:47:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7443c765-f90d-325e-b1e7-a5aed301bc91 | -18.85937 | -54.53807 | 2024-10-05 01:47:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8ab6666d-7142-3bfc-b102-f1fa788e07a0 | -18.85801 | -54.54473 | 2024-10-05 01:47:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4db149db-6a98-3016-b431-1380e50da0b9 | -18.8579 | -54.46294 | 2024-10-05 01:47:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3e2e818b-cac7-3732-a3b8-03e5f6cf10fa | -18.85702 | -54.4694 | 2024-10-05 01:47:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 0792c3ed-8cc8-3957-884b-36e9b226d6ed | -18.85685 | -54.52325 | 2024-10-05 01:47:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 33778869-bfcc-386c-9a9a-24eef653d3fc | -18.8556 | -54.52999 | 2024-10-05 01:47:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 79d9f47e-891d-3975-be4b-8bca41211c02 | -19.66466 | -56.45675 | 2024-10-05 01:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.0 |
| af8facac-adce-30fb-85ba-32545709cf18 | -19.65513 | -56.45844 | 2024-10-05 01:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 082b3cab-3b93-396d-b711-01dc08c8710e | -19.64121 | -56.49454 | 2024-10-05 01:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| e25f52e2-3740-3b78-858f-8b42e0ad1617 | -18.70415 | -57.29302 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 45ca39db-ad24-389b-b931-d3567a550f6e | -18.69489 | -57.29459 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 8ffe4463-0241-31c9-848a-ef4e3835011d | -18.69336 | -57.28437 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 6bff6892-af28-3fb3-8719-b108aaaab703 | -18.69181 | -57.27413 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 43b0198e-d166-3648-af90-b69698078528 | -18.68718 | -57.30639 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| f1202429-0eb7-35c6-8afe-c4d85409a3d4 | -18.68564 | -57.29617 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 3414ac9b-7a1d-3bab-baae-bff6109bdf77 | -18.68409 | -57.28594 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.9 |
| 1a21ffa5-4c6f-307e-872e-51d6daa24aff | -18.68255 | -57.2757 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 85cbd502-c4f4-37b5-af2c-33f6a1f316f5 | -18.67483 | -57.28751 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.9 |
| fab09ee8-5714-31c6-926b-b80d5ac390a0 | -18.67328 | -57.27728 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.7 |
| daa65de9-c5b8-3cd6-b10a-4e13b2ffae9e | -18.66713 | -57.2993 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 309b9b95-0b22-35c8-a1b7-fba2912e3d7b | -18.66557 | -57.28909 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.5 |
| 0d2e304b-f1ee-3afd-90f0-b63ee68fe6fa | -18.66402 | -57.27885 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 224.7 |
| 27c2190a-4ce6-330b-8b39-d31a2572ff8e | -18.65631 | -57.29065 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 5ab0194c-cd92-318b-a773-9e159cbd8675 | -18.65475 | -57.28042 | 2024-10-05 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| c3ed6dc8-f6a0-35fb-87ad-c462fffe5c2d | -22.6613 | -51.5223 | 2024-10-05 01:47:11 | GOES-16 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.5 |
| 336c8150-d3de-3da3-904d-df963b64a101 | -13.61943 | -51.27594 | 2024-10-05 01:49:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2fab3004-ad4d-3140-8085-0ebcce4bbadb | -13.61428 | -51.27164 | 2024-10-05 01:49:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 1ce9e5d7-fd96-3e60-8928-aa09cff41b0f | -13.14717 | -51.19879 | 2024-10-05 01:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 2cf0a774-66df-3320-b605-bf7f298e58b4 | -13.14042 | -51.19333 | 2024-10-05 01:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 32359feb-d94d-33a8-9fa7-9922d831d239 | -12.82121 | -50.54585 | 2024-10-05 01:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 71c39e1e-43b5-3d18-9b5f-419f5157fafb | -12.81686 | -50.55364 | 2024-10-05 01:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a472144f-fdf4-380f-9ab8-1a5c94608ae8 | -12.80028 | -50.5569 | 2024-10-05 01:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 79287cd1-f78b-3b5d-abf6-f6ba6499baa3 | -12.77386 | -50.60039 | 2024-10-05 01:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 4375d4c8-53d9-3f14-9860-ec255e1dff4c | -12.76711 | -50.5634 | 2024-10-05 01:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 355.7 |
| f166102f-97f8-3ba1-80e8-7f57202aa7fa | -12.76245 | -50.56933 | 2024-10-05 01:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 6f631086-4c4a-36f3-98f9-7f02a0b8db57 | -12.65726 | -54.07511 | 2024-10-05 01:49:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7de9ac46-92ec-3d21-96a3-983be665996b | -12.63351 | -53.12984 | 2024-10-05 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7f16ac08-8b11-3d89-80e5-000bea00c0b5 | -12.62954 | -53.10596 | 2024-10-05 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 9d3a1401-e7e7-31bd-8320-a8a811e3cccc | -12.62546 | -53.1257 | 2024-10-05 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 748.4 |
| e2bb2310-7d8f-3423-bf8e-1594827ccfbd | -12.62132 | -53.10201 | 2024-10-05 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 522.3 |
| 176e773f-7207-3648-9588-c5e0b8da9b4c | -12.61976 | -53.13235 | 2024-10-05 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 537.0 |
| f904445e-f706-3220-9d16-5c2cb235150b | -12.61577 | -53.10849 | 2024-10-05 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 876.5 |
| 4bda4a75-423c-3117-9233-68c0502ca185 | -12.6117 | -53.12815 | 2024-10-05 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 529.5 |
| fcc277ea-d270-328f-abff-ec4c58b6e12a | -12.60755 | -53.10449 | 2024-10-05 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 282.1 |
| a2931fd0-7e9a-3490-b972-f02f3fe52dfc | -12.60601 | -53.13478 | 2024-10-05 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 227.5 |
| 8a0c37fa-a67d-3ebf-9b79-03d8527a0bf6 | -12.602 | -53.11102 | 2024-10-05 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 180.3 |
| 4074a3de-ebb3-3587-9ddc-10664c07ffee | -11.10614 | -54.24089 | 2024-10-05 01:49:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| b09e07b3-72b8-3e36-92a0-021c9310e2d4 | -11.10276 | -54.22032 | 2024-10-05 01:49:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 440efb64-618e-3444-b711-071dc3175623 | -11.07648 | -54.77991 | 2024-10-05 01:49:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| daa46389-8692-3f3a-8681-0ca4eb9625e1 | -11.07495 | -54.78577 | 2024-10-05 01:49:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 40334d03-13e1-3240-8b5b-66f5a5bdee56 | -16.6616 | -55.50439 | 2024-10-05 01:49:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 1940ae0b-7730-3c0e-9698-147ed425dfb6 | -16.65761 | -55.54703 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 481b6362-84e2-3768-8ea3-07e3c8ab9b45 | -16.6555 | -55.53399 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 53cda852-b78c-3b92-bf57-8d930a50946c | -16.651 | -55.50624 | 2024-10-05 01:49:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 6448eeef-5820-3d05-ace2-626a93221123 | -16.64261 | -55.52167 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 051fb611-ed49-3529-b9bd-7658dc965fc6 | -16.6404 | -55.50812 | 2024-10-05 01:49:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 778a3f04-19b3-3b37-b764-10c3e335e4ad | -16.63202 | -55.52352 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| d6319dbf-fc2a-30f4-8829-c8b78d5e89cc | -17.08412 | -56.67808 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| f099ede6-641c-308f-a8ec-ff2e9e36b413 | -17.08281 | -56.6842 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 6ca30dc1-af67-3d49-8ae0-cdeb2736d2fd | -17.07307 | -56.68588 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| fc20f8c3-7917-3da2-a588-56835bcf87b6 | -17.06126 | -56.07754 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e6e55ea4-450a-3a97-afa1-749e3ad35403 | -17.05934 | -56.06524 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.4 |
| 229b315f-3222-3896-9a64-936b6ad90392 | -17.0456 | -56.70222 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 2a038378-c254-33bd-a4aa-da728a3f86a5 | -17.04385 | -56.69092 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 252.3 |
| 57cd5599-e2d1-3f63-9600-e1d6df2f15b6 | -17.0421 | -56.6796 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 796ae3c9-da43-3e34-9dbc-c4a44099759d | -17.03411 | -56.6926 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 180.2 |
| 3b440527-abb7-313a-ace5-99dd0df05962 | -17.03236 | -56.68128 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 995d6d3d-8cb8-3790-a59b-22d788ae4c92 | -17.0306 | -56.66994 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 0cc76c0a-1250-3505-bf5a-aae44037a3a9 | -17.02884 | -56.65859 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 1923ba42-5769-3bda-adf9-d4c2d584bf0c | -17.02437 | -56.69428 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 178.0 |


[Clique aqui para ver as próximas entradas](README26.md)
