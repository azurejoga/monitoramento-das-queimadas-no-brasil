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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41f82531-9e44-3933-b119-98c0d3c27951 | -12.87671 | -53.47694 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2676e8d5-c84f-3a45-993e-9f86442513b3 | -12.8761 | -53.48171 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 791c98bb-2c13-30b2-bb27-54420d08bc62 | -12.87549 | -53.48646 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 05534b6d-7930-3444-b775-acb54ceabf40 | -12.87488 | -53.49119 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cb41c70d-bd51-335d-9e5b-17c0e0257376 | -12.87277 | -53.47153 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d7b1a133-745e-325d-a2fc-01afd2b31bce | -12.87216 | -53.47632 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1e9d9b77-620f-33be-838b-c7f2ee94a752 | -12.87154 | -53.48109 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| ee1057b7-5714-3f6f-9d99-8e24ab520461 | -12.87093 | -53.48584 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| dc85ac18-dcb2-3652-ac52-56a2682846e0 | -12.87032 | -53.49056 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 59559f35-b684-395c-83f6-98acfef24b2a | -12.86821 | -53.47091 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8e612485-b13c-321c-9151-703ecc60928a | -12.8676 | -53.4757 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bbcc5c8a-ad64-3bd8-ab05-a0eca7b07b57 | -12.86699 | -53.48046 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 244ce346-432d-3f43-8064-d92366ebbd9c | -12.86638 | -53.4852 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 9efa084e-e906-38fe-a055-9e1f71cd4859 | -12.86577 | -53.48993 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4920ad0c-5537-323a-9e9d-9b138b4a89eb | -12.86365 | -53.47028 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3d03e03a-7461-32a9-b113-f62ff1f9b906 | -12.86304 | -53.47507 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 41b472d2-b812-3f12-b91c-8c0c30a848fa | -12.86243 | -53.47983 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| f5f1413b-6c17-31e4-8e46-03b53f780345 | -12.86183 | -53.48456 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 9b57be78-bd3e-32a3-af8d-5557a7d8e15a | -12.86122 | -53.48928 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1255d37a-529f-3f25-a763-c053223631c5 | -17.70453 | -56.31025 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| c0eb666f-fac9-3e17-bb2a-c26f15c8a8ec | -12.12112 | -54.27691 | 2024-10-11 05:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc02617c-85f4-38d3-9f00-7a38123ca1c4 | -12.4408 | -54.56034 | 2024-10-11 05:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac2f7af-7785-334a-83c4-02c552aa2b17 | -12.44026 | -54.56435 | 2024-10-11 05:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89aa698f-555b-34fe-a8cb-66a62172d6eb | -12.43605 | -54.56375 | 2024-10-11 05:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06032a11-ca5c-3996-b2da-9be1fbc08cd4 | -12.40876 | -54.54352 | 2024-10-11 05:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0e53692-0d67-3ae3-b65e-0d0e82b19bf9 | -12.40822 | -54.54752 | 2024-10-11 05:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 981acd6d-442c-35d1-8747-699d94f830c8 | -17.71894 | -56.26315 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ace925f7-35eb-324d-838d-d6a4ab3dc52a | -17.71845 | -56.26688 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4ada1a36-d5f7-3bad-bda9-e881b8a524fa | -17.71537 | -56.25884 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5f34f02c-eccd-39e4-91fb-a565fa55dbe1 | -17.71488 | -56.26257 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5fb22d99-570d-3aae-8767-b1b1f3dfd6b3 | -17.71439 | -56.2663 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 044f9c25-5b7e-309c-ad03-cd55290a933c | -17.71131 | -56.25826 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 488478c7-78d1-3243-952d-1404d4220ae7 | -17.71082 | -56.26199 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5f8e5721-dd1d-3419-a32c-09a81277351d | -17.71051 | -56.29603 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5083b32b-62ab-3af7-87be-d2425b00a26d | -17.71003 | -56.29973 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e4f3bbdf-9e0c-3f81-81ac-3872031cabbc | -17.70955 | -56.30343 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 98e8648e-9de9-3d63-bfb3-3b35618c58a6 | -17.70906 | -56.30713 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 460918fb-f4ac-3332-8f36-c88163245a49 | -17.70858 | -56.31084 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| a307a8f3-a711-34a6-8ecc-247f3f92999d | -17.70809 | -56.31453 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4ccd3f07-d581-396d-854a-1a05bbebcb81 | -17.70598 | -56.29914 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8b8c0ed9-3db2-32d8-a301-9a5f6afd3cc8 | -17.70194 | -56.29856 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2dc06625-d042-32e8-bf89-2dce3734d8ae | -17.70098 | -56.30597 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9a2544d0-a31a-38b4-b360-f346a70343c4 | -17.70049 | -56.30967 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b41aadcd-871f-387d-a374-b4887cc0c4f6 | -17.69693 | -56.30539 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 91161103-327b-3e4f-aacc-e9556772fc40 | -17.69645 | -56.30909 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b72e5ae2-6206-34ae-bfe4-d2ef5d9ca91a | -17.69597 | -56.31278 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 90c11b64-c6ce-3a2d-b63e-b8d5b080c147 | -17.69549 | -56.31648 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| eaed763c-09c8-3d42-ad04-132f61753ff3 | -17.69501 | -56.32018 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ce5630a3-9a7b-3cd1-98f6-34aafe57ab8d | -17.69453 | -56.32388 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c47c0fe2-4b7a-394d-8aa9-da8aaf0145b3 | -17.69193 | -56.3122 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d59fdfc5-5fc1-386b-b1af-a4b89052dc80 | -17.69145 | -56.3159 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0cd71364-b813-38e4-8e5c-c49eb4570adf | -17.69097 | -56.3196 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 02dd5680-2156-344e-82e9-d027a52051bd | -17.69049 | -56.3233 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 96fd5399-bcbd-3d30-b78a-32c76464caae | -17.69007 | -56.26279 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2543342e-2f0a-3cb3-b2f8-d65bf7912058 | -17.68741 | -56.31531 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e901ee2f-ffd9-3c80-a4f9-c7df75fd2911 | -17.68693 | -56.31901 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| b2a4c391-ab21-3e86-bd79-52c7f0b6ab19 | -17.68645 | -56.32271 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 2d7924a2-445b-3792-afc4-25822c9393e9 | -17.68598 | -56.3264 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6a6cca4b-a2f3-3ddb-b604-b550ed863139 | -17.68554 | -56.26593 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| aabab43d-e862-31a6-8bfe-912267c44a4e | -17.68385 | -56.31102 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e07fb438-6320-33f6-bde1-1388ba50a56c | -17.67981 | -56.31043 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 18d5db98-5731-32ec-9c04-fd1ad5641902 | -17.67933 | -56.31413 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f80462e1-433b-3d83-a452-f57525f82519 | -17.67886 | -56.31783 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 504bc634-f967-3c8d-a7a3-b6902296c293 | -17.67838 | -56.32152 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 57cf3c9a-6c76-3ff6-b379-b80263a66588 | -17.67577 | -56.30984 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c3b5f057-b72d-3cb1-a337-2c2af6e60112 | -17.67529 | -56.31355 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8da41a22-13f8-3da3-a2cb-d5706cc2d52e | -17.67482 | -56.31724 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 029e5fc7-ef05-3a46-8195-f3934f4b3445 | -17.67078 | -56.31665 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b71a1a2d-3580-3664-addd-1bc28b53614e | -17.67031 | -56.32035 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4f66ba5f-4b21-3ca1-be41-edde8d45dbba | -17.66339 | -56.27787 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f32a8271-f774-3e24-8023-84fbd930c4a8 | -17.66292 | -56.28157 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7fa9cb9d-6e26-31e1-bce7-abdb9e8039a1 | -17.66129 | -56.32657 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 626e6c52-0f0b-38b1-99df-1a07214a55d3 | -17.65934 | -56.27728 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a66a44ec-136f-325b-adf5-ddfd50a58d38 | -17.65772 | -56.32229 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ac770d1f-ae84-302b-ba00-384508a89908 | -17.65725 | -56.32599 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b17c74d7-de63-3084-a248-d736e5b157d5 | -17.65678 | -56.32967 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| e38c669e-9eb8-38b1-8add-09c998d6c449 | -17.6551 | -56.31063 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 90173b59-e877-3ea7-9c5c-bf8b591d2988 | -17.65369 | -56.32171 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9c1ddddd-a33e-3f1a-b779-2e10a3fe61a1 | -17.65322 | -56.3254 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 44daa578-0c63-383a-8567-8975b976b523 | -17.65274 | -56.32909 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 12326c8c-0c99-302d-a489-fad7a1965b75 | -17.65106 | -56.31004 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f5be7d7d-b528-366e-9f7f-ca6533292570 | -17.65059 | -56.31374 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 94ad7158-4ae9-38a3-a999-0b4df59fa3f3 | -17.65012 | -56.31744 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6cb66901-5bc3-3e38-90b4-f2fad31ab4f4 | -17.64965 | -56.32113 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8e015881-cf13-3071-a6ca-8fe36e04201a | -17.64918 | -56.32482 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5127134f-56bb-38ba-b12a-82d725081034 | -17.64871 | -56.32851 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| deab9230-6271-393c-805d-2c9f9162021a | -17.64702 | -56.30944 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 04a0c7aa-e126-3a00-a5d8-1c1a6522222a | -17.64655 | -56.31314 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 064c5205-7fb7-31a1-8c2e-8c1cbe8e1d84 | -17.64608 | -56.31684 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c849644a-7aa7-3d0f-89ba-3b94a51fbd51 | -18.1961 | -56.45338 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a4d6b786-19a9-3d95-bb8f-cecf43c0dfcf | -18.19491 | -56.43058 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a0bec319-9e2b-364e-878f-4796230fea85 | -18.19444 | -56.43429 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e9b7a096-3127-3d55-9817-431815e3743d | -18.13961 | -56.43861 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 526801a1-162c-3c23-81f8-1d0b6c5a7b77 | -18.13558 | -56.43802 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6ca999d5-6e71-3a56-9268-a3d2a965260c | -18.10071 | -56.42171 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b0b5cc66-0512-37a3-bd41-d09821b4e713 | -18.10023 | -56.4254 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| aaf3bf7a-562f-3837-bbf9-f41eb1fc1a1d | -18.0981 | -56.41004 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cf4b6bbe-11e3-39d4-b7d2-ff5ddeb98942 | -18.09762 | -56.41373 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2ba8d1fb-fc8d-35e1-a22e-3a4abba73427 | -18.09715 | -56.41743 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b1ab5794-4e77-30cb-90e4-3f5f00c432d6 | -18.09501 | -56.40205 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README101.md)
