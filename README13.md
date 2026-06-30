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
| 81cf7583-c457-375b-a0fb-ca6611887b6c | -13.25626 | -56.80399 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5b3b945c-7a9d-37d3-9cb3-70fde0943ed4 | -13.26378 | -56.80541 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f31bd32c-895e-3945-aceb-31d29a2597a9 | -12.5448 | -49.92345 | 2026-06-30 04:57:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b501471b-aa92-3ca4-b014-a9fe71f5908a | -13.71 | -47.87429 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2569b1da-5a6d-3a65-a34f-4cadb2814e9f | -14.63464 | -54.46021 | 2026-06-30 04:57:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fb9f4d5-407a-37c2-8cb3-803e7eb93a56 | -12.85898 | -44.34464 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 076dae1e-82fc-31c6-a1b3-0ecb78d7f867 | -11.89496 | -57.13536 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 952d204b-85c8-37bc-b273-896b186ae94d | -11.31944 | -54.4645 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db125c18-4b5a-3c36-8e4c-bed00432b359 | -11.22107 | -53.83041 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e56cb210-5eda-342f-b901-5edace8576dd | -14.20226 | -57.43915 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5bdbe1b-7242-32bb-8781-5dccb76d201a | -12.67069 | -56.3815 | 2026-06-30 04:57:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 487ebab2-a58a-3ba1-a6a6-5c218a676676 | -11.90029 | -57.13378 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1134099b-ec5c-300c-b022-f3eda5a158e7 | -12.85934 | -44.34165 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8cf10a7-20dd-39dc-9d77-54a23f7c9e47 | -12.52558 | -48.2921 | 2026-06-30 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 142c3286-43c6-34bd-9ea5-937b237e56d2 | -13.25611 | -56.80123 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ab8d830c-6987-35d5-89a0-1d61cc1b1c08 | -13.69663 | -47.85146 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7ba5eb0-8b1d-364d-b72b-c954d15e2d5a | -11.88854 | -57.13165 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4500be4d-5e47-3dc0-9a7d-19ec5d1cfe0c | -11.05306 | -55.76506 | 2026-06-30 04:57:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ca46b88-6b21-34a8-ac35-dfe4f8921b8c | -11.89797 | -57.14113 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd75f0b4-6c93-3805-8ba7-c657cc523284 | -11.88462 | -57.13095 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b913f33-91f7-3129-ab42-70847ea18e90 | -10.04753 | -59.11141 | 2026-06-30 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 596ef9fc-fe3d-34ef-abff-2570b5448a08 | -11.90443 | -57.38001 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5534eae-03af-3788-8cf4-6556dfd7ef7f | -15.08208 | -59.90601 | 2026-06-30 04:57:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b828b4a-b560-3d1c-ae99-6f9974d26498 | -13.2766 | -49.76954 | 2026-06-30 04:57:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a15ac12-e5b4-36d6-83c8-3e9934f7ad41 | -13.71445 | -47.87186 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6491f9b9-66f0-38c9-8f15-00b3ac4049a2 | -10.04669 | -59.11621 | 2026-06-30 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dd67b5a-de6f-3000-8e04-8b5d9729e23d | -11.89586 | -57.13033 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ac79e02-4258-3a45-b3b3-6d22b5e04627 | -11.88767 | -57.13672 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97366ad2-9a17-3ceb-a85d-1b8f689901be | -10.05116 | -59.11018 | 2026-06-30 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28a14040-fd88-312b-ab08-3bd73546225e | -11.37823 | -55.80732 | 2026-06-30 04:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4ae6b0a-7c71-3e57-9411-42c7d316d327 | -12.84689 | -44.35958 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b011ee6-6082-3bcd-ad0c-6d811e9c9972 | -13.72056 | -47.85723 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a7868d6-5cc0-32d7-8bee-6f31b7f2051c | -14.62963 | -54.46363 | 2026-06-30 04:57:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef8bb237-69e8-3d39-8896-6a1e82598d63 | -17.91245 | -52.71962 | 2026-06-30 04:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 667bf0a6-8b86-376d-b203-b4e8f23c92f9 | -11.79304 | -57.35221 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e20dc6e-a9a1-38ec-8296-da9bb023ba84 | -11.38151 | -55.80597 | 2026-06-30 04:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db709e18-9db5-3654-989e-762ec5e7847e | -12.2198 | -56.55371 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5219763c-1106-3b4e-858a-52e3ae6e29ba | -12.03135 | -55.45623 | 2026-06-30 04:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c0cde9c-79d6-3973-9b63-d7b8dde09574 | -17.71101 | -46.78295 | 2026-06-30 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| edfead1f-a1c9-3dbf-bcc1-e991fdfd7fca | -11.92554 | -57.40002 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| baf68ae8-12b4-36fd-a603-da8b0b7177a0 | -11.89505 | -57.11734 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f33b22e8-9890-37cc-9807-9de81c547a11 | -14.95686 | -52.86216 | 2026-06-30 04:57:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13e5e12a-e01a-3b5d-905c-887848a8b3b0 | -12.44673 | -58.49151 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cb367a13-bc50-308f-8580-fc9a09c377fd | -13.25693 | -56.79663 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 98b424aa-a5d3-36b2-9d8d-7b151ea6a7ed | -17.12638 | -49.96733 | 2026-06-30 04:57:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b280163-610d-3ce4-b40f-432b9bea4eed | -12.22357 | -56.55437 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 005a6d89-cde5-3960-a2c2-8159ac90673e | -12.0842 | -48.42004 | 2026-06-30 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50b6719f-7389-34a7-81c5-47fc854bc4a3 | -15.37055 | -59.28674 | 2026-06-30 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a3f53228-3cd7-373b-9589-87f2d9bbfa3b | -13.72298 | -47.86971 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dc3fb02-b1cc-3d2b-90cf-267a6146b7a6 | -12.44747 | -58.48745 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b503ec34-e96b-3b96-bc36-fc99b8be3673 | -11.22047 | -53.83409 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1308f6fe-e2c2-3a69-b096-22bc958ab3f9 | -11.89638 | -57.13306 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9990fd27-0da2-3ab7-981c-dc94d07d0d19 | -11.89333 | -57.12733 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbaa989f-e6da-3d52-8a4a-dbc591faef8b | -11.90194 | -57.4174 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2fc48e9-b3cc-3162-9e88-66dcdca32bf1 | -11.89943 | -57.13884 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cd71a47-cfb9-3ace-a2d3-a4aa6e32e6bd | -11.90116 | -57.12875 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51cc1dd2-d908-3aaa-87a9-c8b007e49715 | -14.633 | -54.46421 | 2026-06-30 04:57:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4b1c48f-6084-3c80-a1c7-c0b3cc3bc11e | -12.22201 | -56.56358 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c4c647d-ab33-3b8f-a137-7bbdfb4cfa5e | -13.25328 | -56.79867 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c2ed5ce-01a5-3c69-9456-5d4b4ac8bdef | -12.85844 | -44.34909 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 56d09def-956f-3a4c-bd09-031c691b2112 | -11.22453 | -54.32043 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 759321fb-6663-3edc-bff0-d0d448eb888b | -11.05575 | -55.76335 | 2026-06-30 04:57:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0cfdd17-783f-39dc-9d5e-34671233b3c7 | -15.08007 | -59.90343 | 2026-06-30 04:57:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e62dd714-56c4-3cf8-ab1f-fda6705213c0 | -13.25988 | -56.80193 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a3b51b72-02ea-376c-9809-035e94b41abe | -13.25775 | -56.79202 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e59af39b-167b-3609-994b-32db78493741 | -12.5129 | -48.27018 | 2026-06-30 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 659afa9e-3c9a-3b32-b294-2a8ea89d80ec | -11.21451 | -54.33821 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad579eff-f470-3dde-84e5-a19b3fa51cff | -12.8547 | -44.34665 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 91e30215-e52c-343b-941b-1f1c66cbe0d2 | -11.92249 | -57.39399 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b504a4c3-daca-3b77-bded-01c8c2ed9af3 | -17.70986 | -46.7925 | 2026-06-30 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| de7afec0-8be4-3c2d-b94b-4f561d406d97 | -17.71159 | -46.7781 | 2026-06-30 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d4bfb6a-ad4a-3d01-bc8d-0f061a022011 | -14.55971 | -53.67659 | 2026-06-30 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 962c9e2d-e072-3640-b978-d8080489f107 | -13.26657 | -56.80804 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f26846e6-acf5-38e5-8647-c8ec3c9eed96 | -14.20311 | -57.43429 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4631c745-0bb5-3faa-a189-0b7f030f7629 | -11.21708 | -53.83352 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d03df0a-653d-3aba-bfe2-b42bac438994 | -11.89071 | -57.14251 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e811102f-4bcd-3bb7-b1b9-6422a425e4e6 | -13.47585 | -47.867 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64e81240-232d-39f7-b117-251d2d34f897 | -12.21506 | -56.55503 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aaf41986-8c9f-32ed-84de-26b1712f2608 | -12.85547 | -44.34072 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4b0b58fb-c7f4-337e-8990-8f5519f3a9a4 | -11.22923 | -54.31344 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59b0f766-816f-3a56-8e99-adf016cc6e70 | -15.37478 | -59.28762 | 2026-06-30 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a022fcc-badb-31d6-a55d-544bc07558c4 | -17.70187 | -46.78141 | 2026-06-30 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9efb5b4d-4d24-37bc-962b-99beec797381 | -14.19843 | -57.43827 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e065e831-9acb-3b3b-8a49-d550754ea658 | -16.17194 | -59.33908 | 2026-06-30 04:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5255294-48a3-30e8-8d9d-cd5590bb3107 | -13.7015 | -47.87632 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7be50298-84cf-372b-9b5a-c823f670b498 | -11.89418 | -57.12235 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5cab160-3978-3c81-8fa1-8b62c83d6a40 | -12.2226 | -56.55633 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d299d81e-5667-3f2d-8975-dd04c074407c | -11.9386 | -57.7057 | 2026-06-30 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7872fea9-ca47-355b-bbd5-ac12662719e3 | -11.22579 | -54.31285 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d57740c4-52b5-3533-92c8-31e938d18132 | -12.45096 | -58.49231 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45dcedb9-577c-3e24-9916-977f32410d4a | -12.19904 | -52.86538 | 2026-06-30 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e288cf22-c29a-386c-b13a-20095b0c2fae | -16.1909 | -59.33072 | 2026-06-30 04:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93aff0f1-1245-36b7-a774-8af0b0d144ba | -18.38021 | -55.72018 | 2026-06-30 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6f8e2418-9df0-303f-ad24-f94a673ad74a | -13.71848 | -47.87248 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04a57857-93e9-399b-82d8-3cf61257f640 | -11.87506 | -57.09296 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e52e0242-3124-35cf-a89a-96132795b6c7 | -14.63403 | -54.46391 | 2026-06-30 04:57:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fce3653f-5533-36c0-b9d1-83011f6e4d72 | -12.84785 | -44.39952 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c3e4006-9fb2-3ab8-a95f-51cd31465e10 | -14.63361 | -54.46051 | 2026-06-30 04:57:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a63765fe-b878-3928-9b64-8858556b2d3a | -16.00346 | -55.64636 | 2026-06-30 04:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 964c0b54-b113-3b65-95b8-fb741137b61e | -18.24486 | -53.8432 | 2026-06-30 04:57:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README14.md)
