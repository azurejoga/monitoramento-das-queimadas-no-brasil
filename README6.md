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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7f6ac62-22bc-370b-9318-8f2f7f78c901 | -11.61526 | -48.05956 | 2026-05-05 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 533be831-0c22-350e-abb9-5bbb760032c1 | -11.13431 | -45.13685 | 2026-05-05 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7485a73b-88f6-3a89-9e41-87ad71db49ab | -8.20449 | -47.9892 | 2026-05-05 05:12:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 229282a1-b0d8-3947-b99c-f09b26f2dc0c | -10.59127 | -46.67332 | 2026-05-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 053f14c9-2d28-341f-97bd-46ce20bb8e64 | -12.33624 | -50.01063 | 2026-05-05 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b2e3cbf6-c1ea-3f8c-83cf-77e8c96bac1f | -12.3374 | -50.00153 | 2026-05-05 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 89f64829-00b2-3b3d-ad70-e0ab281de54c | -12.33701 | -50.00456 | 2026-05-05 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 583683a1-e5d3-311c-984a-08b2a1f5812f | -12.33443 | -50.00988 | 2026-05-05 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 05ec8476-f823-3fa8-9656-ceccf783c07c | -11.13356 | -45.14355 | 2026-05-05 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3161761a-201d-3272-a489-908238bc0fc8 | -12.33516 | -50.0038 | 2026-05-05 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb61d0b2-8457-346f-9bb3-a5cac3048659 | -11.37995 | -55.17867 | 2026-05-05 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92a86aaa-7cf2-35cd-a1ec-bac6a0992a09 | -9.56497 | -44.56876 | 2026-05-05 05:12:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8787ffc9-19ba-35b3-b4b7-0d80fbb21c3e | -7.52054 | -47.17199 | 2026-05-05 05:12:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e8dfa64-68ad-3dd2-b9b2-143b773f026d | -12.33552 | -50.00077 | 2026-05-05 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 83e0fb21-bc37-39f5-8155-969828fbac11 | -12.3399 | -50.00756 | 2026-05-05 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fc5f1b93-2350-32cb-8808-f98452c7fd7d | -11.12676 | -45.14229 | 2026-05-05 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f6b29143-ff63-3d93-8920-ee30511b4a29 | -9.24994 | -60.33594 | 2026-05-05 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 24815529-7d2d-32a9-9af4-57e137341a5e | -10.59199 | -46.67582 | 2026-05-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab19ece9-1eb2-32a8-99fd-fb17d50f8d60 | -7.52578 | -47.1768 | 2026-05-05 05:12:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9749bf05-ef98-34a9-a64f-6bf8ddbc1b03 | -12.33662 | -50.0076 | 2026-05-05 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 819e125d-8344-3548-a97a-c58616e94602 | -9.25058 | -60.33206 | 2026-05-05 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0f564cc1-d313-36fd-a63c-0132d450d78a | -12.33479 | -50.00685 | 2026-05-05 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9fb00a51-f15d-36ab-96eb-eabb50d94f87 | -10.59072 | -46.67809 | 2026-05-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccdb8914-f0f7-3594-9479-088e5e977fa1 | -18.6675 | -50.22922 | 2026-05-05 05:14:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| c85dd23f-e60d-37d0-8bd6-538df894d8b1 | -14.04093 | -47.62526 | 2026-05-05 05:14:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fd14819-f1a5-38d9-9750-d5096fa4ee17 | -14.05511 | -47.66499 | 2026-05-05 05:14:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 046ba128-4c07-3712-9e1f-54b6b64a3cab | -18.6628 | -50.2212 | 2026-05-05 05:14:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| ae3c9dfe-c19f-3df0-9510-754766f0e211 | -14.33357 | -57.72996 | 2026-05-05 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d382d18a-45dd-3067-a5e0-35447b1cd0e8 | -14.07703 | -47.63399 | 2026-05-05 05:14:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c47e3a7-65af-357f-95e6-29161f7fa093 | -13.69227 | -55.67799 | 2026-05-05 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 421b466e-3651-322e-b75b-132a83274935 | -14.07871 | -47.6269 | 2026-05-05 05:14:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b48e7ef-d976-325a-99f5-1f503950230c | -14.049 | -47.66451 | 2026-05-05 05:14:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7290f62a-a0dd-3a18-a67c-f4537115b1b3 | -16.38224 | -55.40112 | 2026-05-05 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a613396-4e4c-38f3-b15a-42edb0e7f3d1 | -14.07804 | -47.62483 | 2026-05-05 05:14:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82b67e23-3242-3854-ac59-01fc4289063b | -18.43287 | -54.70956 | 2026-05-05 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac9876ec-cca2-32c3-88d7-469432aadb4a | -14.07823 | -47.6315 | 2026-05-05 05:14:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7538aab6-31bc-394a-8232-7345263f96c6 | -16.15754 | -58.49209 | 2026-05-05 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8d2f5b7c-58d3-3338-9890-c7db4ddd3ded | -18.66827 | -50.22183 | 2026-05-05 05:14:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 8d2113e3-d270-3f19-ab88-e5ab07199989 | -17.79793 | -46.71102 | 2026-05-05 05:14:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bac40a60-801d-39fd-beab-6dae13324624 | -14.40973 | -56.31688 | 2026-05-05 05:14:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee86be3e-d131-38a0-aecc-dc00e6027c08 | -14.32239 | -57.73572 | 2026-05-05 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44615309-451b-317d-8a36-e8f6a5177b83 | -18.43741 | -54.70634 | 2026-05-05 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8d9b2db-768a-3300-ab7e-75bcf74bbf1a | -14.03481 | -47.62478 | 2026-05-05 05:14:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11ff4596-59cc-3e6e-93c5-5de50a665334 | -14.07755 | -47.62925 | 2026-05-05 05:14:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69bed562-8ba5-3906-8155-66693a9f7a43 | -14.32293 | -57.73206 | 2026-05-05 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a652a3ee-6f41-3e93-8295-64be98e0f50d | -16.1542 | -58.49155 | 2026-05-05 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9c615920-a979-3768-90f6-86c07af93dbe | -13.69288 | -55.67371 | 2026-05-05 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd9c9966-0ba2-36ed-a38c-4ab0b7378706 | -18.43645 | -54.71394 | 2026-05-05 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e32501f7-53e3-3294-971e-18626fd20920 | -14.07995 | -47.79118 | 2026-05-05 05:14:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 871086b3-116e-3b12-a8b1-5c0c72e9347c | -13.68443 | -55.68115 | 2026-05-05 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0e4ed5f-fb15-3b7c-862e-65209fb8e570 | -18.66865 | -50.21813 | 2026-05-05 05:14:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 93992d51-8d65-38d2-aafe-f6ad8d80fe4b | -14.08032 | -47.78773 | 2026-05-05 05:14:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2032ff3-2dc2-3139-b0b4-48b65c43f78e | -16.59708 | -58.23782 | 2026-05-05 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 649433b1-b283-3072-be94-15c95006cf0b | -16.59316 | -58.24098 | 2026-05-05 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b4fe838b-6872-3b09-8c46-93f1f166fbf1 | -16.59653 | -58.24152 | 2026-05-05 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fda2cf96-7e8b-3d45-836f-a03679b91d6b | -18.66788 | -50.22553 | 2026-05-05 05:14:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| eab9b315-eff6-3706-8f4d-2b6d1d71c19d | -16.15699 | -58.49575 | 2026-05-05 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a4690162-3896-35fd-9ed7-e18917eadcaa | -18.43788 | -54.70254 | 2026-05-05 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64e75bd7-b89b-30e4-b988-4b7b9d943df1 | -14.08408 | -47.79099 | 2026-05-05 05:14:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42d8a784-5943-31cc-b4a5-fc0b6265da1e | -18.4324 | -54.71336 | 2026-05-05 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae78189a-73ac-37fb-9fba-7ae949b6e2d2 | -14.31903 | -57.73519 | 2026-05-05 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ce9c359-71b5-38d7-a8a1-79b2a0438f24 | -18.23647 | -54.59145 | 2026-05-05 05:14:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 640bb665-0ca2-37b0-b5ad-b27b1fce40c3 | -14.07195 | -47.62405 | 2026-05-05 05:14:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6968afa1-ea97-3b97-b395-b114f1159f31 | -14.00281 | -56.62743 | 2026-05-05 05:14:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77aaa34f-9f0d-32c1-9a8e-7f2226b811cf | -18.43335 | -54.70576 | 2026-05-05 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d0498e0-cb4a-329b-9f8f-ca8b812f3b91 | -16.15365 | -58.4952 | 2026-05-05 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0e389328-6cb3-3705-b354-78e864a8578e | -16.75868 | -51.87121 | 2026-05-05 05:14:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da329b27-19b7-3e31-b362-f42a95b70e65 | -20.08882 | -57.21405 | 2026-05-05 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8919a7f9-25b1-3ff1-9d2d-28b06b1af736 | -22.80136 | -49.33876 | 2026-05-05 05:16:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecb2aba1-7314-33e2-8981-cfc176129d67 | -21.95434 | -57.59552 | 2026-05-05 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7250cc26-e29e-3504-992d-285aae1102df | -21.70201 | -48.41728 | 2026-05-05 05:16:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcc874af-f187-3398-bf94-be2d43a00096 | -21.95854 | -57.59169 | 2026-05-05 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3ea5e3b6-fc64-350f-9a52-78fe2c7c90be | -21.70789 | -48.42332 | 2026-05-05 05:16:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1dd8d2a-9cd8-3713-8c13-30a515037116 | -23.03678 | -47.74168 | 2026-05-05 05:16:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ab2aeab9-abe6-3557-9bbe-f82f31e321f2 | -21.70474 | -48.42003 | 2026-05-05 05:16:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7696b894-0695-346c-8306-35effba41a38 | -21.70432 | -48.42567 | 2026-05-05 05:16:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a2f29cb-b049-3048-a680-8b25bf08b1e0 | -20.71785 | -55.17856 | 2026-05-05 05:16:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10fecdaf-0adc-30e1-a3e9-5ceae4f318b4 | -21.70154 | -48.42299 | 2026-05-05 05:16:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76ba6b82-1e67-3d49-a344-51ca54b23262 | -23.04342 | -47.74266 | 2026-05-05 05:16:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2c307fdb-5f7d-34a6-b906-7da653346f80 | -21.23185 | -56.92718 | 2026-05-05 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a18325f-334e-3901-b803-a687555d3175 | -18.6643 | -50.2255 | 2026-05-05 05:20:00 | GOES-19 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| e81f36c3-c332-3743-be18-ae16b48b6e3c | 1.23124 | -60.57407 | 2026-05-05 05:42:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7df0a4f-bed4-3758-8fdb-f821edc079d5 | 1.23182 | -60.57769 | 2026-05-05 05:42:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b43c5251-e5c4-363b-a0b9-6ddebf838cff | 2.73111 | -61.35736 | 2026-05-05 05:42:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b28fae3-9bf4-3707-a945-a2acc6bddce4 | 2.73498 | -61.36029 | 2026-05-05 05:42:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5659dbc0-62c3-3dfb-a6f6-b85cda4da6bc | 2.35886 | -61.06058 | 2026-05-05 05:42:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b54b905-0120-37f4-bcc8-4b149586cb4f | -13.43704 | -43.83679 | 2026-05-05 05:44:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| a69d334e-e85c-30e8-8790-8f7d10e77e18 | -11.13059 | -45.13744 | 2026-05-05 05:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| a7d6f245-8bb2-35b6-af0c-ebdde2a48a46 | -12.26882 | -43.50391 | 2026-05-05 05:44:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8588a189-6d34-3829-8a19-1ad9b86871ef | -16.59505 | -58.24201 | 2026-05-05 05:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 3bcb6537-ef59-310a-a0d7-618d47608926 | -13.69001 | -55.67588 | 2026-05-05 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c10c8750-c227-3144-ab38-98ef84f054b3 | -14.00223 | -56.62994 | 2026-05-05 05:46:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8eefa3a0-de2e-35a5-ba28-37660ad96ab8 | -16.15342 | -58.49356 | 2026-05-05 05:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b785776e-9d70-318f-81a9-7d35231e465a | -13.69602 | -55.67287 | 2026-05-05 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c4fdeb0-d881-372e-807b-0763c25c9c90 | -9.24692 | -60.33619 | 2026-05-05 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 76ed9eca-7f7c-3fde-b1d3-9cf9b8cc1945 | -9.25076 | -60.33675 | 2026-05-05 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0d75e82e-fe65-31ce-aca8-a51461103fc1 | -13.68957 | -55.67967 | 2026-05-05 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db24b7ef-d8b2-3fd4-8e2d-daf6a60bfd13 | -14.0026 | -56.62675 | 2026-05-05 05:46:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f1e99e1-1d77-308c-b71a-10213f4db1c4 | -18.43484 | -54.70522 | 2026-05-05 05:48:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35ff7db1-d823-3ea0-881e-a3b1f2b06446 | -18.43175 | -54.71121 | 2026-05-05 05:48:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README7.md)
