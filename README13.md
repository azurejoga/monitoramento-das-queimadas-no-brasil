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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20f86e2e-6d43-362b-9f5b-3e54d7235015 | -12.9655 | -53.5319 | 2024-10-12 01:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 4a6e2598-da11-3302-9f51-1e5a226a30c1 | -18.229601 | -56.514702 | 2024-10-12 01:16:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 950c780f-b209-31c5-96c3-c58f7644d23d | -18.2313 | -56.523102 | 2024-10-12 01:16:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6f1c4d58-d3e7-3af7-86be-c281af420244 | -18.219801 | -56.516899 | 2024-10-12 01:16:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 94848d8c-925c-377f-a76d-21046167b9fa | -18.2215 | -56.5252 | 2024-10-12 01:16:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c00ea6b9-96ab-3201-87ca-188692b926e4 | -18.223301 | -56.5336 | 2024-10-12 01:16:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fedae417-abc8-3136-bced-c81acbd79e50 | -18.209999 | -56.5191 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e48023ca-a562-3369-a437-32ed729745a9 | -18.2117 | -56.527401 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e848e457-fd78-34ec-adef-6ac38ccc9cb4 | -18.213499 | -56.535801 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ebfb5997-2f66-3a7e-999b-06d7cb2f8ad9 | -18.1985 | -56.512798 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f3608dc4-ed85-3923-86f3-6b4a7d74e8ac | -18.200199 | -56.521198 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 236d94a8-21f4-3195-9153-8c37814326f4 | -18.2019 | -56.529499 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 82921a22-86c0-351b-8293-7b07c276ddd2 | -18.203699 | -56.537899 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0112abf1-1e80-3f52-aeb5-6e4a6ea1514a | -18.1887 | -56.514999 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 21e383c3-95cd-3031-af01-2843dee0b3c4 | -18.1905 | -56.523399 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e2805ae8-2d47-3104-95df-84fa30c6693d | -18.1922 | -56.5317 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 24dfcc03-4c42-37b0-bb87-a9f53ff4c505 | -18.193899 | -56.5401 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5a76916c-91ed-3e1d-b75a-12a89169c757 | -18.143801 | -56.4468 | 2024-10-12 01:16:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 31143db1-96c8-3c52-9101-8da313bb033e | -18.0875 | -56.373001 | 2024-10-12 01:16:35 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bcac6ff5-7f5f-38e1-8c5c-8271c72368e5 | -18.092699 | -56.397598 | 2024-10-12 01:16:35 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 89176d9a-726f-3537-a149-b52c39f6ecb2 | -18.0944 | -56.405899 | 2024-10-12 01:16:35 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9ea712a9-26f2-395c-8e75-053ececc7e89 | -18.0961 | -56.414101 | 2024-10-12 01:16:35 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cb07ce04-e261-3bad-aafb-a4a3da6ba8e6 | -18.097799 | -56.422401 | 2024-10-12 01:16:35 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 244adc6f-a2ff-3cdc-8d5a-208190488d29 | -18.0996 | -56.430599 | 2024-10-12 01:16:35 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 83c1e91e-4218-3511-a5f3-37226d5cd726 | -17.993601 | -57.357399 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d4d2f9b7-b36b-3d6d-a6cb-567a79c8c39b | -17.995501 | -57.366501 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 249284cf-5e39-3c52-ba8f-0b6b03836e35 | -17.9839 | -57.3596 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 928654a6-86b8-39f0-bb7a-453f4dee7739 | -17.985701 | -57.368698 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 79f8fd78-3531-3c45-a39a-a789c2d98d5f | -17.9876 | -57.3778 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aedd571b-9edb-369f-b3c0-f66ca2877b4b | -17.741699 | -56.237598 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d089fac2-251c-391c-8d7f-219dac3bba0a | -17.743401 | -56.245602 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b8463997-f50c-3f6f-b06d-a0a3ef2f4c5a | -17.9741 | -57.361698 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 255f4782-b0d5-3bac-a42f-05ae4ec4a70f | -17.975901 | -57.3708 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4ea90f93-07fa-312d-b4d5-c8bf3308ff0c | -17.9778 | -57.379902 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 968a4d03-d905-35d2-8ba7-fb9fc677df1b | -17.7353 | -56.255901 | 2024-10-12 01:16:40 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eeb1e1a7-cbef-33ee-bea2-e4a362011f8b | -17.7187 | -56.225899 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e74e014f-d797-3bda-b775-68f6ebc79277 | -17.7204 | -56.233898 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4da1bee1-2a14-397c-ab1b-c225d479b330 | -17.722099 | -56.242001 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e93967f1-2380-394b-825a-3bbc7160cc15 | -17.7255 | -56.258099 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a822f99-d9d6-3a67-b697-5ad0ac873cbb | -17.7089 | -56.2281 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9ea6dff0-6aaa-3fec-8acc-850ccb3f09f8 | -17.7106 | -56.236099 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 22bbe22c-e1da-3103-9a39-ce2160dbe7f7 | -17.712299 | -56.244202 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 448945ee-182c-3d4a-8b4c-4a00fafd3597 | -17.714001 | -56.252201 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 78215882-8e55-37c9-8196-3781e68638af | -17.7157 | -56.2603 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 02c0fd72-b283-30a0-b4b5-57f02641edca | -17.7026 | -56.246399 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f9f61d36-5d41-3829-a01c-ada892cf59b5 | -17.7043 | -56.254398 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cf4708fa-50dd-340b-aa4d-693cc085afbb | -17.705999 | -56.262501 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5d27a329-9451-3da8-b3e5-6edf358ddada | -17.709299 | -56.278599 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9b047f55-40c6-3b2b-b224-b5de3b1d823d | -17.711 | -56.286701 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a007bb1a-85d1-3b6d-bd9a-5da9e17c7dc4 | -17.691099 | -56.240501 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8072ae02-14e5-314a-9ea5-fc08517385d3 | -17.692801 | -56.2486 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c927ed15-b0c2-3a53-a6f3-04d215b54f0f | -17.6945 | -56.256599 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f6344b3e-ed82-31b1-8f12-0409164c47d1 | -17.696199 | -56.264702 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a51ee81-0777-3a84-a073-c817ef83f9ca | -17.6796 | -56.234699 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fdc4b3e8-e824-33be-a6ce-d0ffbe4bd2e8 | -17.681299 | -56.242699 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dfc4a82b-24bc-3dfe-878e-5af4333392e6 | -17.683001 | -56.250801 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d2dca6fa-dac2-30fb-ac1d-112a054f4fa5 | -17.6847 | -56.258801 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 50f7dc55-ada7-3437-a36c-7a3539b7f59b | -17.9025 | -57.311199 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fb3e6c53-6a8b-32c0-8f32-531185a99423 | -17.9044 | -57.320202 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6c717780-a182-3911-8466-c93a81a377be | -17.9062 | -57.329201 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8709b11f-3cf6-3064-9869-0aea5ac892cb | -17.6681 | -56.228901 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f14f8a1f-d49b-3cf0-b149-9b93974cac16 | -17.6698 | -56.2369 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3a7df289-ed0c-3908-b405-4ece923c432a | -17.671499 | -56.2449 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 926f212d-a3fc-3ac8-92be-a803d465606a | -17.673201 | -56.252998 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 25584968-59d1-310e-afb3-a3ec691339c8 | -17.6749 | -56.261002 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cc678c0e-8272-3037-b3c1-eafb9378ab4f | -17.686701 | -56.317501 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cbd54668-68b6-34a4-ad54-0cb07e87b40e | -17.8909 | -57.304401 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3ea74102-6e93-38aa-a4c0-faffc4ec18a4 | -17.8927 | -57.3134 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ecd40f5b-54ae-315b-a590-a770db116ce4 | -17.8946 | -57.322399 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 741c1ffa-1f4b-331f-b6d1-ec52217dc930 | -17.8964 | -57.331402 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e09c1acd-2e9e-34ab-809b-0bbd6db91c7c | -17.898199 | -57.340401 | 2024-10-12 01:16:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ae8f6de0-7f6e-312d-ae45-2d9c5f1d36bc | -16.9802 | -57.4609 | 2024-10-12 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| b57c58ef-b796-3163-b16b-a677978d6b92 | -16.9805 | -57.4404 | 2024-10-12 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 67519504-1044-3e29-8d11-bf30ac12606f | -16.9998 | -57.4586 | 2024-10-12 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 883c603c-78c2-332e-a7a8-c01bb0ef7548 | -17.0001 | -57.4381 | 2024-10-12 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 8356b4ae-2fae-34d1-85b8-988b2e6b88bc | -17.661699 | -56.247101 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c05dcf42-d03f-3a67-94bc-9c6cbeed8db6 | -17.663401 | -56.255199 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 530db16a-bf57-3031-b6ac-d1ccee4c0f2c | -17.6651 | -56.263199 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c36112f2-d6c2-3f1f-8061-b1c8fc1fd2d4 | -17.6668 | -56.271301 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8709f4b9-7b36-3a89-b088-82c1ecc3914d | -17.8811 | -57.306499 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 37e0e0cc-822a-3c91-bcc4-55815a94e033 | -17.6493 | -56.334301 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7ea87003-43d8-3376-ac10-0bdb33f03a27 | -17.8829 | -57.315498 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9561b922-0248-3efc-8b4d-035293676ead | -17.8848 | -57.324501 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b31c1356-2373-3395-b647-3673b4e30884 | -17.8866 | -57.3335 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4d78aff7-acd8-3576-84a3-76f71dcf5232 | -17.888399 | -57.342499 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aa75b70f-28df-3d6f-81cb-cf1473e622e7 | -17.653601 | -56.257401 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dd7b38b5-0a89-3a3f-aaf6-8ce33ff76892 | -17.6553 | -56.2654 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6ba0b839-e53a-3f1e-bcb9-671e60cc7b21 | -17.8713 | -57.308601 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 217e48ce-0fa8-304f-b431-20d64b9c96a2 | -17.8731 | -57.3176 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9e30b93a-8409-36b7-9a13-d83c2661d0a7 | -17.875 | -57.326599 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a8ca4429-0f46-3ca6-a3fc-d1455b8c2584 | -17.876801 | -57.335602 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 27e19fd3-e551-3ddb-8833-9638a3fbc656 | -17.878599 | -57.344601 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 652a1e39-dd7f-313a-9962-ab323ed6c32c | -17.880501 | -57.353699 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dc9ab997-cd40-35fb-8536-8b4c30720952 | -17.653999 | -56.307899 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 07a498a4-dd37-3a91-8027-a8e90c608c9b | -17.655701 | -56.316002 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8180a9dc-50ef-35a0-b6c5-d510140d9ef8 | -17.657301 | -56.3241 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2cd4f01a-6bea-309a-86ea-f9a2a875a3e5 | -17.861601 | -57.310799 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 12bde6ab-6aa7-3de9-8f09-bb68edad7712 | -17.8634 | -57.319801 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9bc127b5-3eb8-3932-bace-084849dd4ba5 | -17.8652 | -57.3288 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1e607ff5-952f-31b7-b14b-ee476db3b863 | -17.8671 | -57.337799 | 2024-10-12 01:16:42 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README14.md)
