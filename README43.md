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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b5e0a2e-b6c2-3d92-a47a-6d9d4aed8bed | -17.20384 | -46.06929 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b886f427-b745-3fb6-a535-5328907e33fc | -12.94754 | -48.09973 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a337e2a-d5c1-3abd-aff6-05679e8ed9fa | -16.16025 | -49.6352 | 2025-09-01 04:12:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 297bce22-6401-3522-b0f3-a1e2dc188c22 | -15.21888 | -53.79103 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccdb683e-18b7-37d6-982f-c4c5a862064e | -13.47959 | -46.98887 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2f51e06-53bb-3573-8686-3ccae04ba89d | -12.59673 | -48.22644 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 511a9729-db0b-3176-8e6a-62c76c65a0ae | -14.7901 | -46.72408 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 92629b32-7119-3713-9a02-2aaf1b5fa530 | -13.33342 | -46.96195 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 18b91e8e-74bb-39da-abed-ac908cea4014 | -12.84351 | -48.077 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7da1037c-d7ec-3ada-b79f-8dc11deb2a85 | -17.16709 | -46.08875 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 936bc746-f29b-3aac-8441-94da2b46691c | -11.92711 | -50.62738 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 617f7a1f-7160-3396-99ca-592bff9c02dd | -15.23123 | -53.80138 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed0102f2-928c-3f96-aebe-792f2e7bbb4d | -12.80104 | -48.08078 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b844286-8c19-304b-9c91-454b6adb41a7 | -13.17326 | -45.27958 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e675a3ba-0b20-3661-9824-837e049684bc | -14.64426 | -43.96024 | 2025-09-01 04:12:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 56d9e913-8938-3e8a-a4d1-347f255d537a | -14.84934 | -47.10141 | 2025-09-01 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94fff774-b467-313b-839c-213540ec58f3 | -12.57212 | -44.79137 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f217667-071b-31ea-a0df-4318e2d0da77 | -17.16087 | -46.08334 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a32e3df-c139-3e61-bac9-7c161cd7235d | -15.69726 | -48.89778 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0397b985-7afd-3df0-91f8-161e6d425e1a | -13.70445 | -46.89925 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afc2dac4-a336-3356-a455-017e658be0be | -14.744 | -46.75167 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| be96172e-822c-331e-ba0a-3eabf83e350d | -14.78717 | -46.71927 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6ab8eb4-d512-323f-9610-05671b28ca3b | -15.68922 | -48.94221 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f74d250-ae1d-3f0e-b72b-7a2c1788a399 | -13.3969 | -47.06299 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2caa3150-10f0-3b28-a5d1-9a866c3919b2 | -14.79004 | -46.74643 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 674b75a4-439b-3bcd-885e-6ca2a0636fec | -13.69198 | -46.8769 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a93960d-5853-35cc-9a9d-eefffa6248d3 | -13.68519 | -46.87175 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01c51d9c-7fe7-3254-a4c7-ed927a3f46db | -15.2237 | -53.79614 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1bd3286-b113-36bb-85f7-728a88f85d09 | -15.72532 | -48.99196 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 964ac659-0d01-35d9-9df5-2f9522a9f7d6 | -12.57429 | -44.79956 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c705aa11-53f0-3fd1-b52a-5d50f2257daf | -12.60059 | -48.21986 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| dabe0302-6062-3d07-9f42-9d46ebb0b969 | -13.69266 | -46.873 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6779cb46-40fa-3dfd-859f-acb7e48ca1d1 | -14.04678 | -44.58037 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10ee45d3-0974-38ae-85c4-d594dc45fb1c | -14.76148 | -46.75946 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6d2891a6-c730-3aca-aca9-bbbc18806c35 | -18.07606 | -45.94368 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fba253c-e473-3591-9786-b3b335d948eb | -12.87417 | -48.16262 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b9211d8-5996-3c83-a8bc-634240f638c8 | -13.53536 | -46.98006 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33668457-3a93-3c64-9f82-a4f690be849f | -15.70278 | -48.96059 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 318c00ec-fa8a-3708-966d-1755a694d1e4 | -13.69912 | -46.92527 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9f47815-8968-3aaa-a2f0-2af82ce240a6 | -13.65394 | -48.15739 | 2025-09-01 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aab02a11-f38b-37b7-a39f-096931201117 | -12.56521 | -48.21299 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fdddf155-bc8d-3628-a0d3-251142e62d62 | -15.70009 | -48.90537 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f97acab8-e45d-3e3e-aaeb-fa8f0ced9c47 | -12.87691 | -48.1708 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| afa72e18-62ca-3b60-ad71-eb12501c3044 | -12.14173 | -47.19607 | 2025-09-01 04:12:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 219b10ae-2bbc-3ed6-a250-b4a8c7060ad8 | -17.60653 | -46.67319 | 2025-09-01 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d5731d3-d245-375d-9da9-0e0dd8281d53 | -13.32574 | -46.84956 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0c6ba52-e668-31ed-a529-7f9cf4312f68 | -12.56868 | -44.79078 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d072a97d-5eea-3a99-a7bf-80b5de9b3504 | -12.78359 | -48.08482 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64fa5b02-69ae-3ccb-b1fd-aeedaf6ca356 | -16.29661 | -52.93912 | 2025-09-01 04:12:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc963a95-c455-3ceb-9ba4-74a659efffeb | -13.37127 | -46.94443 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c917c8fa-6047-3669-bc07-19ab0233ef04 | -17.71959 | -44.38342 | 2025-09-01 04:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 94520e27-ebed-3b5f-8d04-9847e3599863 | -18.07137 | -45.95074 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 355a86e1-448f-31c6-97dc-6a1329c8a245 | -15.70426 | -48.90556 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 76b23ea0-b8d9-3caa-afe3-dcdeb70fdf6e | -13.37886 | -46.94398 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 25faee2f-16ce-37e7-a856-77bbdbb1108c | -12.88165 | -48.1678 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dfc0b7c-ab13-34ea-81cf-029abd9557d7 | -12.8476 | -48.07725 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6fd24f67-3f38-314f-ad42-4bbdd41bdc67 | -18.12095 | -44.98606 | 2025-09-01 04:12:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1171601c-fb23-3fd1-a65a-9cbf62ad645b | -12.86916 | -48.07355 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6163b276-df66-36e3-b2cf-6bdd9e23357a | -14.75629 | -46.7677 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9204254c-c6ce-3e83-9c4f-a6ae3ff1b93a | -13.51883 | -46.98607 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1e74c9d4-ed7b-38e6-b46b-5d5e588c97f3 | -12.6394 | -48.16883 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18022438-d7f3-33f7-a2b5-f33658d1621c | -14.98643 | -46.71245 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc736031-bbe0-30c1-a7e1-c882d6c7c7e3 | -15.70145 | -48.92118 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 768aec8e-035a-3f70-a6a4-937fc39d60b2 | -15.70357 | -48.90941 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ccf42cf6-2102-36ff-bce5-d3bf6d59641b | -13.71153 | -46.92462 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18fd3f45-0078-3a3d-a686-d7e7d9469e0a | -12.8735 | -48.16638 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebe0b6b1-a55f-3edd-acb7-4623e5ac25b0 | -15.69194 | -48.95049 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91e109b3-50f4-3135-b619-ac9e2452d86f | -15.59835 | -48.35435 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d219486d-1b62-3185-a3f6-f5fd466b266d | -12.83893 | -48.07894 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c48ab491-e9aa-333d-8f01-ca19ff78ed20 | -15.72935 | -48.99306 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d5486a99-9053-392d-9f46-32e42362e780 | -13.17196 | -45.2874 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 110131cc-08e5-3066-835e-ae7655d688e3 | -13.31826 | -46.84824 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a83b378c-457c-3003-808d-de9a96d6dbbb | -12.82323 | -48.07351 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b196c02-1e0c-343a-b0f7-ddad4c837362 | -11.52242 | -54.47271 | 2025-09-01 04:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 789180c8-69fc-3dc4-afe3-c190c852364a | -14.04557 | -44.58775 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 247677b4-22be-31f8-8fab-6cccdb465621 | -15.59231 | -48.31958 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e42430f-199c-3299-8fb0-fc0190e797be | -12.78767 | -48.08538 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d9e09de-3b20-37f8-a51f-073146e62be5 | -12.39188 | -46.47297 | 2025-09-01 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 337c2eb4-2156-3e82-816f-ab22afc2c758 | -15.70019 | -48.92813 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75d2b68c-418a-35c4-857e-83706257e132 | -15.29776 | -52.79094 | 2025-09-01 04:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf5486bc-df76-3661-b54e-0ca9aecdfc5b | -14.75056 | -46.75727 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31d40bf0-846a-3eb0-a734-c8cf68813814 | -17.17193 | -46.08107 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e2dc3f0-0cb1-3121-89dc-c472ea182aef | -12.8706 | -44.75908 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35b24af3-570e-302e-b947-0b052cf885a3 | -13.99948 | -46.31891 | 2025-09-01 04:12:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0103e45d-f835-366c-8732-187a6bcdf057 | -15.71909 | -49.00271 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be46717f-5acb-3d2c-adbd-033265b7fedf | -14.75551 | -46.77227 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 506dccc3-b01b-3008-a00e-2b5437eda72d | -15.1066 | -48.17897 | 2025-09-01 04:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02d17666-6004-3366-9494-a62c41cde84d | -13.68893 | -46.87235 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb509574-d998-3123-9655-d82db41ab51e | -13.16848 | -45.2868 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ae2b3767-783f-3d03-969f-ed956588fcba | -12.59991 | -48.22361 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1ac5cf6b-dbde-3bd3-b575-a25d4e5fa26d | -12.63118 | -57.00175 | 2025-09-01 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c58928de-fe59-382c-bade-5d4649e5715d | -13.66599 | -46.93894 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 381881c5-d533-33bd-8041-7f47966ec66c | -12.86536 | -48.16492 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a44c2e8-51fc-3a6d-85fe-60e64619e62d | -15.70494 | -48.90179 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7d072690-e123-318c-a630-65b215466d1f | -15.16588 | -52.34555 | 2025-09-01 04:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69cf396c-398c-38b0-aa82-a3aa0cc1e6f6 | -14.98348 | -46.70781 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1332632-108e-33b3-bae8-4121a397226e | -14.74475 | -46.74736 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d047f7af-3b32-3c35-a111-2d2d0110dbab | -12.59935 | -48.21145 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f00a3cf8-59c1-3957-9660-4cca2f991e20 | -13.47174 | -42.47615 | 2025-09-01 04:12:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fcf5d494-570d-344a-8f09-541223947d13 | -12.77825 | -48.09127 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README44.md)
