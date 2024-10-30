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
| ff3fd9a0-195a-3352-b92c-9ca36d84a237 | -0.70458 | -51.99213 | 2024-10-30 04:44:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b76e0322-9d96-3389-8ca8-4620a6e482bf | -0.70397 | -51.99596 | 2024-10-30 04:44:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc82d2ba-662b-3ce1-84a6-9efcd4ca5fdf | -0.7017 | -51.98775 | 2024-10-30 04:44:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d49f0d6d-ee15-3b55-91e0-f017a1193d40 | -0.70109 | -51.99159 | 2024-10-30 04:44:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63127d5f-aa1b-3aba-b1ff-070db5349329 | -2.15306 | -52.36687 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa9724e6-1ddd-314e-ba8b-2c646aa528a2 | -2.15243 | -52.37075 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9031eea8-cd70-338e-a7ed-87c6d24ead2c | -2.01035 | -53.29687 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22d95ec5-a1d8-34e0-8c57-f6713d11e64f | -1.97863 | -52.08242 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66b33b2b-846b-3b58-b3f0-1e7ffb8fc59f | -1.89569 | -53.01038 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8456fdd-2abd-3760-b963-000248346bbc | -1.76511 | -52.30878 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8491c49-f3e9-3388-b0b4-f8eb89422b09 | -1.75811 | -52.30768 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c843da4e-3e33-36dc-be29-96cc9839a889 | -1.74492 | -52.34529 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82680735-11b6-34cf-8ffb-6f5f4830150f | -1.71821 | -51.96627 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5618275f-7980-3402-bf5f-a230b9c4fb80 | -1.69344 | -52.51044 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87aca077-2130-3c87-a739-473db213352d | -1.69269 | -52.51343 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b919441-b7a4-35da-9715-1b6a56e7509c | -1.59784 | -53.19379 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3506c0bb-33d3-345e-b5b4-08fadd9f75aa | -1.57833 | -53.1057 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3247fce-c303-39bd-bfc8-3acfddb3f05b | -1.57767 | -53.10992 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29e765fd-15d6-3eb8-9f59-4134605211df | -1.57593 | -52.95564 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60c06090-d597-35c1-b8b0-50c66984ffcd | -1.55615 | -52.03783 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76026ea0-442d-33e4-897c-3e4a49344ee6 | -1.54109 | -52.10948 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aeda283-c590-332d-959c-8e0d45292ab3 | -1.54091 | -52.13286 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 17b23af8-23db-3a06-b95f-b39459bd9a81 | -1.53959 | -52.10997 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2fe9974-ff66-3148-b074-67cdf92ee12a | -1.53762 | -52.10894 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42d461d1-1d57-3101-8b3a-a21526e91ff6 | -1.53611 | -52.10943 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9acf5c2-f0d5-3281-952c-114f693176d9 | -1.53302 | -52.01548 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53959b68-a3f8-3989-8be0-bec97f025819 | -1.52806 | -52.09253 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c0c219e-0f50-3286-83e8-bb4e102b2182 | -1.52746 | -52.09634 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c899cde4-2275-3be0-bfa6-5209a15551d0 | -1.52687 | -52.10016 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f92be66-ef51-3247-934e-2da25c70e008 | -1.52627 | -52.10397 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc46303f-5ff4-3921-bf2f-cf35c86519b0 | -1.23355 | -51.76664 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc9ae265-3844-3067-a69f-0d3ba90a66bf | -1.23297 | -51.77037 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0a49e5e-e4d0-34a9-b5a6-853182ba9524 | -1.23011 | -51.7661 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12b8a416-5d57-3718-92d9-a73fa556c340 | -1.76799 | -52.3132 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df791482-5a8c-39e1-ac70-037f7f392245 | -1.76449 | -52.31265 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8039ea86-28d6-39d3-b2ca-fee00e4ca181 | -1.76161 | -52.30823 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00bbefa3-10bb-3d77-a8cb-6d33e874414f | -1.75932 | -52.06553 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 343db7bd-f191-3c39-8f0d-5e09e9c0bd8d | -1.75461 | -52.30714 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a22b600-ced4-34cd-8e08-59f58e92d518 | -1.75111 | -52.30659 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c02f841f-eb9b-3b2d-912f-4de2a576691b | -1.7443 | -52.34917 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f789531-cee7-338c-ad33-bfd0f5c1ff9d | -1.74079 | -52.34862 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 54d8b829-554d-3c01-ace2-1354f273500e | -1.73564 | -52.33589 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d22a341c-5f4f-3e99-99d1-a702e7182c5d | -1.69282 | -52.51439 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4f25a37-9b60-3130-868c-1ef3f451e89a | -1.68428 | -52.72454 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 052ef430-cec1-3f7e-b7c3-535a628421b3 | -1.68071 | -52.72397 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee432318-ed97-3d6e-a22d-7f486d35484f | -1.63861 | -52.24221 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c534b25e-4a8c-3375-8743-5c42a3a5d094 | -1.63511 | -52.24166 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c43dee24-95d4-3e37-bb85-23ba6feb6b35 | -1.6296 | -52.04536 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4430d531-93c0-330f-bdee-5041ecb17867 | -1.58263 | -53.10209 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d6f5872-f607-3aea-a18d-84e7e3719d94 | -1.58197 | -53.1063 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9ce423b-8559-32f4-8858-d80c1967e0bd | -1.57468 | -53.10512 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 610f3d8c-231f-37e2-976c-9986316e0b0d | -1.57402 | -53.10933 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02ee505f-2ec2-3b7c-919e-886335547351 | -1.55329 | -52.0335 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec2906ef-0954-31ef-a236-b6c7f31af51d | -1.54439 | -52.13341 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6dd2a36e-741a-31c5-b181-0d2ac87f9dfc | -1.54151 | -52.12911 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ed362f93-e2b2-3982-acf5-18453061258f | -1.54048 | -52.1133 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 686c725f-6c1f-344a-8f92-017d3c62d4cc | -1.5403 | -52.13668 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90285cb8-ca87-3779-9cd6-7f34841a3dee | -1.539 | -52.11379 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b18bd30-8924-3892-86c1-6c4170d3d809 | -1.5384 | -52.11761 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35b2ba72-c769-3547-a6f2-0c0a22273f68 | -1.5359 | -52.01981 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6f326ba-60c5-30c1-a5af-a9c92110bd03 | -1.53263 | -52.10888 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a197a15-2ca8-3af3-affe-ee33d6e61658 | -1.53243 | -52.01927 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bc60fac-f4d5-38eb-b9a5-f0ff380d93a8 | -1.52975 | -52.10452 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 943ac884-357f-327d-8c02-71381ee1e3a0 | -1.52915 | -52.10833 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba1f7a00-4cd3-357e-9e4a-1f2111585cee | -1.50768 | -52.10884 | 2024-10-30 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb5ce4bb-e3b2-3223-9ed1-9b7020c3d326 | -1.4615 | -52.31084 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e9dd4f64-4bb1-3e17-b7f9-2be9b83776fb | -1.44684 | -52.85582 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01e98b6a-aca6-358f-bfb3-bdcd7361c935 | -1.40263 | -52.22718 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcf898ab-03ff-3145-b2ca-a04bb65fb74b | -1.40181 | -52.30146 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be14e5b5-5683-36d2-ad16-8ed3a2e5e013 | -1.40165 | -52.30255 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dd242bd-e1d3-32e8-888c-507302f02dd7 | -1.39912 | -52.22663 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee7dab76-6dd7-356d-a43f-2ff7cfcfbe97 | -1.30037 | -52.88215 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ab014ac-62cb-3c23-b748-2c3cbd92e022 | -1.28011 | -51.95406 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09c96308-4b4f-3a0c-b341-03190d868305 | -1.25992 | -51.94702 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55d183c3-e8ff-3893-afe8-df1dd559d38e | -1.10207 | -52.11865 | 2024-10-30 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d06c5112-868e-34ae-8b15-f784c32b5c56 | -1.08334 | -53.16903 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fb2bda6-7d62-3744-a054-7a874eae9181 | -1.07967 | -53.16842 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe18c543-2594-3593-8b06-2b60ada613b1 | -0.86443 | -52.30139 | 2024-10-30 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b77db6a-e889-36ea-9b57-d145cfb90a03 | -0.77567 | -52.33694 | 2024-10-30 04:44:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c1d8c54-b05d-3c5e-ad6f-9a8b21b2a4a1 | -3.67794 | -52.26923 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1e3a02d-9cae-3541-82fe-96f5198bf327 | -3.63027 | -52.30812 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5af94a4a-c111-386e-9b94-5513c7c839fc | -3.62742 | -52.30383 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7d4da14-65d2-387d-8088-bde3b1737898 | -3.16536 | -53.07528 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| ecd4663c-d601-30bb-ba48-bd2fa9ce6873 | -3.16178 | -53.07473 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 3f16c865-9fe9-3d36-ab38-289aaebe02ee | -3.10427 | -53.05412 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 844d9e7f-80a3-38b5-8284-03ec7296aa3f | -3.10362 | -53.05819 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f34e316d-5d70-33f4-ae30-1e833ad10f14 | -3.10261 | -53.04144 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21251a76-ea39-385e-8a6b-b38324efbd7d | -2.91358 | -52.59559 | 2024-10-30 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4531a35f-ef83-3c65-aa02-dee625d51d71 | -2.91296 | -52.59945 | 2024-10-30 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7bc108af-7ba0-37d0-b58f-38f521a3beaf | -2.90945 | -52.5989 | 2024-10-30 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c3911d67-a77a-37f7-9f28-73a5f003cabc | -2.86723 | -53.32969 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3594ca8e-878b-3f2b-a6f6-064455f3a484 | -2.86521 | -53.34214 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeafa103-1cd7-3d81-880a-f062e28e956d | -2.86382 | -53.35067 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6569bce-8bea-3afe-8d07-599a38017a0b | -2.86294 | -53.33318 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b43723ac-2d78-30e5-8d73-6a97b55f5149 | -2.86227 | -53.33733 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d4d2072-937c-38bc-945a-6a7ee493df04 | -2.8609 | -53.34571 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32dbf88d-eb6f-3021-bd64-abd1073a5837 | -2.86042 | -53.34635 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93bd266b-f49a-38ac-aabc-a10d2874f420 | -2.85932 | -53.33258 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6464a89c-0f9e-365d-8c78-9469c788ac02 | -2.85877 | -53.33318 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cfc3621-1f73-378b-9472-7306bcd06c5e | -2.85811 | -53.33735 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README66.md)
