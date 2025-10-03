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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0761b5b8-f75a-3f90-b204-68a655163408 | -13.19365 | -47.78933 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a42575dc-0dc2-3afb-928f-3a683e535fec | -19.59047 | -45.89443 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbdcb1f3-6108-3fb5-96cd-f318447a921b | -13.96514 | -48.17576 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05fe0847-6815-3e28-9a2a-adfd3f497e7c | -14.89691 | -48.3454 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| acca84b3-8ee5-31bc-991e-3ae2394275c4 | -13.38669 | -47.29692 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f4c740c-544e-3585-807a-04285478218f | -18.68039 | -47.83078 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3189be2e-7f92-3937-beee-d60ab7b3a22b | -18.58567 | -51.04912 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| afd1dda7-0692-3899-93ec-65dfad9ba1cf | -14.19001 | -46.11923 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92b06fcf-3a53-3a98-857b-4f3d3bc0da16 | -19.4554 | -44.28769 | 2025-10-03 04:34:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8d6554b-5350-3eeb-8a9d-114ff0f32051 | -15.28453 | -49.30839 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d95f94a8-2498-3c26-8346-cb7bb1ca123b | -15.33904 | -46.29633 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5a8224b-6aef-3dcb-a581-033d99a236b7 | -10.89284 | -56.20039 | 2025-10-03 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae8c0963-7464-3546-9a20-af326b1ccba3 | -12.6967 | -48.5541 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3eced1c-cbf8-3512-a95e-39ef79959761 | -16.25374 | -48.02662 | 2025-10-03 04:34:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc70be2c-84f0-3aaf-8d99-cc4a47071344 | -13.38969 | -48.13079 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6c3b532-ae23-3b70-af06-7e2950fdbbd2 | -12.62738 | -46.96823 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e657524b-6280-3b80-8ba5-b6f847b953a2 | -12.8478 | -46.85909 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bb71955-04df-307a-bf27-782f05dcb12b | -18.51205 | -44.037 | 2025-10-03 04:34:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e94b410b-15ed-392c-841e-b0f0ae5dc210 | -13.96049 | -48.10497 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f30ce146-14c8-354d-8cc5-064b5691a93b | -12.62508 | -46.95982 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5db1f79a-308b-3679-a9b3-04920e9a7522 | -14.64525 | -48.25608 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ac3c8e6-798f-3e69-81ad-816b2e73cea6 | -13.30111 | -47.26123 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9373037-c93d-3310-9fab-49c25dea52db | -15.28082 | -47.91443 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2d1768b-0bf6-3072-9a24-bdb2a905331d | -19.73503 | -45.88821 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2763e41-d51f-3810-a1ee-354bb9a80c55 | -13.19362 | -47.81237 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfe44e0c-a104-35a5-ab26-e9b4e009e161 | -14.44275 | -46.38104 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 373c1927-18b1-36e8-99f3-107f14fbe4bf | -18.2414 | -53.32242 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f4e1bb2c-f24e-394a-a784-41d06929f90c | -12.91484 | -47.15641 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be396e68-e142-3648-a84d-bfc2eb984ead | -15.58737 | -46.93876 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed9a1d8d-c0a5-3aab-ad15-0e7635220889 | -12.60976 | -49.89825 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca0d30dc-565e-377a-a863-4f3e8ecd11c8 | -14.93512 | -46.90923 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bfef7e3-9ed6-313e-a6ce-8b3bed9e42f0 | -13.93868 | -48.08983 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6e77955-2001-3a1a-a051-bf2b35cf541e | -13.96678 | -48.16496 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40336c60-85b9-3099-aa80-4c3f52af17b0 | -13.87031 | -47.9392 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e3511ab-20be-3ba2-b940-f73c2a725af0 | -13.76575 | -47.54507 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98bda987-ca24-3756-b690-04cf06dbd835 | -13.64802 | -47.30521 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 501f7da9-8e9a-36d6-964b-fb24e7458e42 | -18.44032 | -43.71642 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2896c6b5-da41-3ec0-aabf-eac8c965dff1 | -12.38309 | -46.51622 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dbdc19e-b2c7-321d-9358-a58ab430d4af | -14.59634 | -46.71021 | 2025-10-03 04:34:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 149da546-e6a5-3354-8b5d-c7c1f5bd3d1e | -12.19665 | -47.78888 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89d9e90d-2204-3af4-8ad5-60761fabb668 | -19.94259 | -45.72435 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fa861302-d1e6-3d2c-b99a-446f7e7d0238 | -13.54424 | -47.25036 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aec4695f-f073-30ef-be9c-cbcdba7174f6 | -13.29997 | -47.26878 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efa86fb4-2217-3159-a705-7c31f94bcff7 | -15.84361 | -46.23656 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b08bb84-6603-36f2-9b0b-e237850fc70a | -12.85963 | -47.00664 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3e5757e-c101-337b-8241-08e92659bb24 | -14.63739 | -48.26245 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed87a76b-7f0c-33bc-89ed-e091a23062d2 | -14.44948 | -46.34122 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b3848c5-871c-3305-a284-15eb63e3a9e2 | -13.83764 | -47.92642 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d6b799e-cd2b-39d4-a66c-ad0a6e2dad23 | -17.84867 | -46.84104 | 2025-10-03 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f56c57e-88a7-3c11-b9b0-777a14868a21 | -14.92871 | -46.90349 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d4f22f33-9c91-3769-9f7d-51fd75b695d2 | -18.15959 | -53.33331 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c8d0cd5-5b63-37a7-a14d-0d43e9728c8f | -13.1287 | -47.84429 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d97c65c-4c5f-3260-b187-a9d4ff31a8e5 | -13.68012 | -48.02275 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c098c99-39cd-3005-9afa-3505bcb4996c | -12.92607 | -46.38437 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf7311d6-6499-31c5-a5d6-69cbcfcd3945 | -15.99077 | -50.87189 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a2a132df-7eea-307b-a33e-cb4d23d90952 | -14.64974 | -48.29461 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42e40b78-f93c-3c4a-ae59-3fd4c3267f37 | -12.49424 | -50.25868 | 2025-10-03 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09614dcf-3ff2-3a43-89e6-8924b390d8ad | -13.80719 | -51.307 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b558868b-3db1-3dc3-94ae-ff2751250c28 | -15.26184 | -49.32302 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bfeefab-8815-3839-a185-8f80444c7d79 | -14.37833 | -45.95069 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 828d7139-84c9-3458-9cd0-84519883eea0 | -18.66603 | -46.58152 | 2025-10-03 04:34:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74d959a2-e432-307d-b727-47c8631f29fe | -13.77823 | -47.53176 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee0deb5-66bd-304b-90f9-605bbff79565 | -18.45425 | -53.20323 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3addfcbc-2a3b-394b-8e25-7cba44624257 | -14.73065 | -48.10325 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fb87d69-5523-305a-92fa-0a5901fb289c | -14.43298 | -46.11518 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cd10214-457c-3f0a-b021-1488ae7abb4d | -17.3227 | -49.38089 | 2025-10-03 04:34:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d993ba5-3570-3916-9528-fb200767b0af | -15.23992 | -50.08753 | 2025-10-03 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47c0c5b4-3a53-3eb5-a77d-095a5da87382 | -14.89971 | -48.34965 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6da38ef-1372-3bbb-a8dd-c18459427c16 | -13.34883 | -48.10571 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a42fc05-9a93-3c61-8450-f1ea2906fb35 | -14.91829 | -48.32964 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f8fbafa-a066-3f01-acc0-bcd03da5f737 | -12.90738 | -47.1592 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd7815f6-19dd-3dad-a284-b733b8d81970 | -13.97622 | -48.12522 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 697ba3f4-590c-34bd-844b-ea45917fb39a | -15.35606 | -46.28163 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2575d41d-cd90-31d5-9713-463e6a060671 | -14.90419 | -48.34284 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a19b0b97-8653-31a6-bbaa-530b29efa908 | -15.64642 | -46.25515 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a14c137-aa3c-3301-9c20-cea8654157e1 | -15.70777 | -46.27366 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a43cdf8-aa5b-39a2-aaaf-37deca8e9b02 | -18.20392 | -53.35111 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb873752-3200-331a-a640-eceb795e2c27 | -15.03126 | -48.06192 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb8e98f5-7b32-3f0e-b06f-addedeac2995 | -15.29938 | -45.09597 | 2025-10-03 04:34:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0415ae60-9dfe-33e1-a611-fda8596d6597 | -13.45929 | -47.22885 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 560ae03d-3fa2-334f-ac19-dc8f6ed635ae | -12.37548 | -46.51918 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97cafd6d-1bcd-3f18-bec1-f1119946f734 | -13.15654 | -47.82912 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 876ae32d-2485-3f0b-8445-79a5ff79af7f | -15.35548 | -46.2858 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7d155f1-f15e-3031-a557-3edc35fe9b9f | -14.4602 | -48.40733 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 012938c4-50a5-3889-9534-d9536246a8b7 | -13.1259 | -47.86259 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01942dc4-0bdd-3a71-896f-fc058b4f6333 | -15.98939 | -50.90157 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32cc0b31-873b-33fb-b061-0cd59ba1b70c | -15.85946 | -46.2577 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c08090f6-1b71-3ce4-8da9-c046be0c698e | -19.71967 | -45.91365 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3966570-fde3-34c8-84f3-77a8f72854db | -12.60372 | -46.99294 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbbf453c-9874-34db-9ae3-d4f80529f5da | -12.62553 | -46.96541 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a637859-89ab-3b7b-b119-1e0b6c292477 | -14.20964 | -46.08612 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a928ccf3-fc42-3231-a7fa-b1b2e705bce7 | -13.31536 | -48.74432 | 2025-10-03 04:34:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e604058d-be87-3fc4-ae0b-8aacbf9c791b | -16.07165 | -51.00208 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| daad2278-e7c2-3d0d-b5ee-0af785c362f9 | -13.15117 | -44.5378 | 2025-10-03 04:34:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c01c1569-329a-3e38-a92a-c333cdcc4431 | -14.6771 | -48.09104 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1780c073-8d7b-3696-bd41-92a8b087aeae | -14.35927 | -43.83609 | 2025-10-03 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dc784c0-9e12-3426-ab23-d0b275310218 | -12.62033 | -46.97641 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 18b47fba-63d4-331b-b0c9-ecc4a6958934 | -15.37324 | -48.60006 | 2025-10-03 04:34:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc752101-e974-3caa-9bd7-4bc7bd0fdf46 | -14.58147 | -52.45792 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec0e3b6d-0603-367d-8cab-a9ba31235a98 | -13.55257 | -47.59049 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README126.md)
