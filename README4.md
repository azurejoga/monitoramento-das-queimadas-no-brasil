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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67fc8cd6-dff1-3977-9bfc-6914e743ad4c | -19.5414 | -56.9708 | 2024-10-16 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 7a279bab-4c83-33f8-b5ab-963fff8ba858 | -19.5615 | -56.968 | 2024-10-16 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 168.6 |
| cbe9389b-6e2f-34e2-a44f-62f5789ca2bd | -19.5619 | -56.9471 | 2024-10-16 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 37a0444b-d6d8-3a3b-afa1-38df33bd1443 | -19.5812 | -56.9862 | 2024-10-16 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.9 |
| 87ee3c58-4298-3d73-86b8-8db21bec3ef7 | -19.5816 | -56.9653 | 2024-10-16 00:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 189.0 |
| f9971556-45e5-3706-b0c3-ab660404911f | -21.1448 | -47.521 | 2024-10-16 00:37:02 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0c12ad34-571a-30bf-88f1-1dc2b6dd4e3a | -21.1455 | -47.4973 | 2024-10-16 00:37:02 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 5c240f8b-5cbe-3e19-a98b-6103c3baa406 | -21.1655 | -47.516 | 2024-10-16 00:37:02 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 340cf26b-8842-3d62-82c2-6cc235d6917f | -21.1662 | -47.4923 | 2024-10-16 00:37:02 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f49f0dad-5fd1-3eb3-a39d-c8cf24a86825 | -22.4559 | -44.035301 | 2024-10-16 00:37:20 | METOP-B | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d661ec70-cd86-3d03-bffb-fd64161ce312 | -22.4578 | -44.0434 | 2024-10-16 00:37:20 | METOP-B | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c8149e9-2b9b-3bb2-a096-8120353d401d | -21.4767 | -45.314201 | 2024-10-16 00:37:41 | METOP-B | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36b66c35-9e10-328c-bfd5-1a0a67b7d14b | -21.478399 | -45.3218 | 2024-10-16 00:37:41 | METOP-B | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 062c5089-fb32-3d3d-885f-80178aaee885 | -20.679899 | -42.320702 | 2024-10-16 00:37:42 | METOP-B | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e722b43-c1a0-3314-b717-44daf81c7047 | -21.1497 | -47.492901 | 2024-10-16 00:37:54 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| af4b1dfa-9948-354b-b1fe-55aba0c8b0b5 | -21.151199 | -47.500301 | 2024-10-16 00:37:54 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e7bfd33a-5c28-3a0c-9681-af16d2176462 | -21.1528 | -47.507702 | 2024-10-16 00:37:54 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9e437d0b-2a95-30b3-bade-7c7d6525fef1 | -21.141399 | -47.502701 | 2024-10-16 00:37:54 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c2f60267-2726-32d0-b306-24ca9df43c75 | -21.143 | -47.510101 | 2024-10-16 00:37:54 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5105d66c-7867-337a-9f69-28f315e67f08 | -21.003201 | -47.048698 | 2024-10-16 00:37:55 | METOP-B | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2a94a999-775f-3cf0-b2e0-f1f68a51b351 | -21.004801 | -47.056 | 2024-10-16 00:37:55 | METOP-B | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 21c7dac7-4275-3e88-8d98-2169efbbcf92 | -20.8571 | -49.856098 | 2024-10-16 00:38:07 | METOP-B | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd79bfbe-0ac1-3528-8166-35e6ce739d8b | -20.858801 | -49.8647 | 2024-10-16 00:38:07 | METOP-B | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa604add-57fb-3a19-b6ac-b55aa3216795 | -20.849001 | -49.866798 | 2024-10-16 00:38:07 | METOP-B | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| adee13e1-e884-329f-b19e-69bfd17d09c0 | -19.6982 | -46.775101 | 2024-10-16 00:38:15 | METOP-B | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7c32db32-6fc1-3360-8ac7-c7e6d396ad23 | -19.6998 | -46.782398 | 2024-10-16 00:38:15 | METOP-B | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 978ba4e1-999a-3e91-8680-75583e83c5f3 | -19.580099 | -47.223999 | 2024-10-16 00:38:18 | METOP-B | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1981e281-e96e-30c1-b088-68f3421adfdc | -18.2896 | -41.718399 | 2024-10-16 00:38:18 | METOP-B | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71b2385b-e750-3bc3-beab-77573ccae97a | -18.292601 | -41.730202 | 2024-10-16 00:38:18 | METOP-B | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33e2bf15-7650-3f09-a2ce-a5f67eb3a3ee | -18.2829 | -41.732899 | 2024-10-16 00:38:19 | METOP-B | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0582edc-dddb-32cc-8c07-01aa559a8fca | -17.5529 | -42.297501 | 2024-10-16 00:38:33 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c22d21a2-6d9c-3b5a-86c0-fdf93c200ca8 | -17.555599 | -42.308498 | 2024-10-16 00:38:33 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1dc51de6-04f4-312a-b86c-2f854d67454a | -17.5459 | -42.311199 | 2024-10-16 00:38:33 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce823e9-2423-3b2d-85a7-c87dd55124d0 | -17.255301 | -42.644699 | 2024-10-16 00:38:39 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c7fa03cd-bbc3-3289-9e9e-dd18d0aca9ca | -17.243 | -42.6366 | 2024-10-16 00:38:39 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b4c97a3-ff90-3293-a70f-08de064db36f | -17.248199 | -42.657902 | 2024-10-16 00:38:39 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5a664800-84cf-34aa-aebc-c97cb4eeebf3 | -17.235901 | -42.649899 | 2024-10-16 00:38:39 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 640b4759-5218-3296-b3d9-f337545a88e2 | -17.5515 | -45.000198 | 2024-10-16 00:38:43 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ce7d57f1-669d-3c66-8660-417436e9a8b7 | -19.5816 | -56.920601 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 43b60e6a-9297-320f-ab40-e99c8fce87c4 | -19.585199 | -56.942299 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 320603a1-020b-3747-b398-e1a920b8e245 | -19.5718 | -56.922298 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 46efec71-8784-3d8a-a88f-effdae6ea1c0 | -19.575399 | -56.944 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 131686ef-9b84-3cce-baae-d4dc45b460d9 | -19.579 | -56.965801 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 287752c4-a8fe-3107-817b-3f9b0c7ae94a | -19.5585 | -56.902401 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 025878f1-6d69-32d9-b6c1-cb16696ce466 | -19.562099 | -56.924 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 600773ab-25be-3118-80ce-4808fe05338d | -19.565701 | -56.945801 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4586f013-e71e-3d9c-a1a5-7c7c0240f5b4 | -19.5488 | -56.904099 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 27f81617-2678-3f7f-ad9b-f46678f0d180 | -19.552401 | -56.925701 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aa56aae9-a095-3e13-9283-7eca24bcf33a | -19.539101 | -56.9058 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6c18a283-c565-3b0b-aef6-ea1d9bf2de0f | -19.5427 | -56.927399 | 2024-10-16 00:38:49 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 515f890c-3bac-3720-ad9b-98065e8fabc3 | -19.533001 | -56.929199 | 2024-10-16 00:38:50 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9d8a954e-c680-3afa-a9a9-d7e519621bfb | -18.278601 | -51.729198 | 2024-10-16 00:38:55 | METOP-B | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a11006a1-6acd-35ad-89ea-194e825519bb | -18.249599 | -56.387199 | 2024-10-16 00:39:09 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0aabc7c3-09b5-3ef7-992f-fb5a79f200d6 | -18.2633 | -56.523998 | 2024-10-16 00:39:10 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 10503bae-5192-3382-9b94-3c6d71db27e6 | -18.266701 | -56.543499 | 2024-10-16 00:39:10 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fb427818-a5a3-3d8b-b728-e76793c453b2 | -18.27 | -56.563099 | 2024-10-16 00:39:10 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b10e0d0b-3940-3d41-a5f5-9d408ea6588e | -18.253599 | -56.5257 | 2024-10-16 00:39:10 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3c6368c4-a85a-3284-9d71-e47c94c58505 | -18.257 | -56.5453 | 2024-10-16 00:39:10 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4492f8c8-e7b9-32da-8696-c9c2d7e0946d | -18.2603 | -56.564899 | 2024-10-16 00:39:10 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e9cea5e7-cf3d-305b-900e-496e9a67f81c | -18.2472 | -56.5471 | 2024-10-16 00:39:10 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0356bbf-1f9f-3afa-9e82-432b83fe95b5 | -18.055 | -56.364399 | 2024-10-16 00:39:13 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 627b97a9-5184-3eea-a7b5-1f15b999430b | -17.854 | -56.824299 | 2024-10-16 00:39:17 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ffa2dfb7-0924-3120-ac2f-60a64b5d856b | -17.9515 | -57.393398 | 2024-10-16 00:39:17 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c24c6bbb-efe2-3a84-81c2-19b5ddffa263 | -17.941799 | -57.3951 | 2024-10-16 00:39:17 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fc1e9a58-06a9-3b1d-98cc-5bce969e58b6 | -17.9284 | -57.374802 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9bbe21f9-6fc3-387a-a95a-9faa2c741045 | -17.9321 | -57.396801 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ba391ce7-a45c-38df-ac3b-3459e0573462 | -17.915001 | -57.354599 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 627b814c-1c67-3a3a-915a-ea2bf90c391b | -17.918699 | -57.376598 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7d33b493-c7ec-368c-9011-324302438cf4 | -17.9224 | -57.398602 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5ac9eae6-53f1-3fcb-9643-de2454c75eb9 | -17.909 | -57.378399 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2ffa7dd3-9456-3ed2-a4a3-da5c08e92f44 | -17.9128 | -57.400398 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aba7bb25-1875-36c4-ae8e-e75a1b0b6881 | -17.869699 | -57.2066 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 65f8c0ee-6247-3bce-8947-672d72869586 | -17.8993 | -57.3801 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0572f6f6-8359-361e-a26a-da6a113d538f | -17.903099 | -57.4021 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ee092777-e72e-328d-9a7c-635410f8971e | -17.8599 | -57.208401 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 70e9a312-40e9-34c8-aeed-df60a162873e | -17.889601 | -57.381802 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 52c8bc89-eed0-32f8-a034-4163489125ea | -17.8836 | -57.405602 | 2024-10-16 00:39:18 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f125fa2d-7775-315b-9eb8-0f013b9fc1ef | -17.870199 | -57.3853 | 2024-10-16 00:39:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 47be2aa2-2106-3fac-bde8-008219eda568 | -17.873899 | -57.407299 | 2024-10-16 00:39:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1bb320a0-721c-34dd-ae97-f040019706dd | -17.860399 | -57.3871 | 2024-10-16 00:39:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d3ae0623-7e3f-32e5-851d-4b739c2537f8 | -17.864201 | -57.4091 | 2024-10-16 00:39:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8e25e0a8-29e0-3f33-9481-580056162cd1 | -17.8507 | -57.388802 | 2024-10-16 00:39:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 19a497b5-246f-35fe-8666-31b6d838b480 | -17.8545 | -57.4109 | 2024-10-16 00:39:19 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5836f62a-4360-3d82-8f10-6549fb84da0e | -17.841 | -57.390499 | 2024-10-16 00:39:19 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00d9eb9c-04d8-3d38-961b-075425a8ac3f | -17.844801 | -57.412601 | 2024-10-16 00:39:19 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0abfad05-c73b-3f92-b3bd-420a985680f0 | -17.8486 | -57.4347 | 2024-10-16 00:39:19 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e61b449b-b25a-335c-9ace-90da98864ced | -17.8314 | -57.3923 | 2024-10-16 00:39:19 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84f1f606-c7b4-389b-a8f8-700ca6d52694 | -17.8351 | -57.414398 | 2024-10-16 00:39:19 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5a3a9ba4-9d5b-3f30-a159-ec2607a610b1 | -17.8389 | -57.436501 | 2024-10-16 00:39:19 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f4e2c042-cf61-387a-bbac-724455368b38 | -17.8179 | -57.3722 | 2024-10-16 00:39:19 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 04351bc7-33f3-36fb-9174-8e5159e01ef5 | -17.821699 | -57.3941 | 2024-10-16 00:39:19 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b786a45-217f-3ec1-96ee-0a00b496a99e | -17.825399 | -57.4161 | 2024-10-16 00:39:19 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 378c4c9d-0fe3-3e61-96cd-d94ad3434e85 | -17.808201 | -57.373901 | 2024-10-16 00:39:20 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bbc213bb-44bd-3390-91f7-0b6c3c99f40c | -17.812 | -57.395901 | 2024-10-16 00:39:20 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b76312e2-3222-3ced-8a17-d95e36a6842f | -17.815701 | -57.4179 | 2024-10-16 00:39:20 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 365997ca-eaa0-3f22-a639-f5b6b52c3b74 | -14.5475 | -43.127899 | 2024-10-16 00:39:24 | METOP-B | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 636be94b-3750-3628-9e82-1e22666f9f83 | -17.217899 | -57.2598 | 2024-10-16 00:39:29 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38cec5fa-226a-3cbd-b4f2-700a863bee2a | -17.2216 | -57.280899 | 2024-10-16 00:39:29 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 599ac1aa-eb58-3afe-a630-8c42ee1c1400 | -17.2083 | -57.2616 | 2024-10-16 00:39:29 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77535e69-e012-3e4e-a852-a8f1b72980ab | -17.211901 | -57.2827 | 2024-10-16 00:39:29 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README5.md)
