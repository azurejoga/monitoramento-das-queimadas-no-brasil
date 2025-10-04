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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0335121d-12a3-3501-8432-6db677556788 | -20.06944 | -43.75066 | 2025-10-04 03:55:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5c02b88a-1986-3592-b387-4498249e0935 | -18.45577 | -49.44634 | 2025-10-04 03:55:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 876a1b01-8f33-31e7-bbc0-1a3df1ed18d6 | -18.45662 | -49.44234 | 2025-10-04 03:55:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a4509a3-41ee-33c7-9f75-ce1072cd3b6f | -22.36392 | -47.03858 | 2025-10-04 03:55:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e9560fe-b87f-3cec-ba15-e11964be1653 | -19.59984 | -44.86026 | 2025-10-04 03:55:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce3e83eb-ebab-3636-9a47-ccf95ae3ee92 | -19.75046 | -46.50524 | 2025-10-04 03:55:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ade33a9c-cd06-38a5-9124-4a5c4b375387 | -19.47105 | -43.64571 | 2025-10-04 03:55:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac9c1f5d-91eb-3948-9453-5a27f921b873 | -20.13866 | -46.41807 | 2025-10-04 03:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 366119fb-a51f-3cf0-86f5-319ed63fef50 | -18.18155 | -53.36111 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d9949231-c54a-3267-aade-6af630b21c2a | -19.51911 | -43.83254 | 2025-10-04 03:55:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc25ed11-7dd1-35e8-a808-f79b1ee0a446 | -20.10753 | -44.63675 | 2025-10-04 03:55:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21006097-db5e-3cd8-88e2-c1d95ddd63f5 | -19.71382 | -44.12831 | 2025-10-04 03:55:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d6b85e2-a931-32e6-b866-f0ec30ce5d45 | -18.17544 | -53.35671 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12a5a326-a679-3b87-9d06-5af5d68828a4 | -19.58655 | -45.90419 | 2025-10-04 03:55:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6d6136a-d72e-306a-a44d-293614620d3e | -19.84328 | -44.07708 | 2025-10-04 03:55:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7977f3ad-e428-30a5-be9b-a6832f158b80 | -18.82401 | -43.13946 | 2025-10-04 03:55:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dc4649b1-e0ca-3b20-87a6-7608e49a62dd | -22.28763 | -46.71992 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6f85536f-aaf9-333a-8916-793c6b69d22f | -19.57201 | -48.018 | 2025-10-04 03:55:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b65cf4df-f0b4-39be-ae10-057e3c3c42c9 | -19.96299 | -43.64305 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 81eb7926-3ea4-320d-9110-c3b4d1f7d359 | -22.28677 | -46.72434 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fae4b623-97fa-3acf-8769-386bf6385bbc | -19.85967 | -42.58904 | 2025-10-04 03:55:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f475fe01-5440-3cbf-8ade-f71a66dc5b16 | -19.80473 | -45.15318 | 2025-10-04 03:55:00 | NPP-375D | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3a5b586-1cf6-3508-bec5-e18e170f1334 | -20.10419 | -44.63318 | 2025-10-04 03:55:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0126710d-5b9f-3ad0-857e-4048919fb164 | -19.74704 | -46.49941 | 2025-10-04 03:55:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed3b12bb-6f14-3d3b-bb09-2c86b2ed6b85 | -19.68828 | -43.9472 | 2025-10-04 03:55:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f74b36d-d7f3-3860-9f65-ceb8d4377771 | -22.18724 | -46.78948 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a56843d-3be1-35f7-8eea-327c014c73f3 | -19.58734 | -45.90007 | 2025-10-04 03:55:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fa6a40a-472d-3855-84d9-a4999187c53e | -22.45462 | -43.18283 | 2025-10-04 03:55:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| aee9a1fc-068b-303d-9889-050513396cad | -17.29601 | -49.26811 | 2025-10-04 03:55:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9543fc95-aa58-388f-955f-f02d0500fbc5 | -18.42129 | -43.48805 | 2025-10-04 03:55:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0e0b4d94-c82d-33b9-a248-59813c7a8c6c | -19.79537 | -42.09588 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a6a41f21-5f50-3275-9f3c-7e1ab778c422 | -21.34411 | -44.99925 | 2025-10-04 03:55:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 02ca131f-2ad0-3ea9-9380-60655b293ca9 | -20.79518 | -41.1273 | 2025-10-04 03:55:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ffa20756-75fa-3897-80f9-cf81f03c58c2 | -21.18621 | -45.13345 | 2025-10-04 03:55:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 484af5fc-a13f-3c02-a3a6-34bf5e858f2d | -19.69616 | -44.44389 | 2025-10-04 03:55:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee0bd82c-63ec-3ef8-9bff-aa1c99066a74 | -19.72243 | -43.43253 | 2025-10-04 03:55:00 | NPP-375D | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53e4151e-d823-3747-ba3d-401f1edbcec7 | -18.38642 | -48.79451 | 2025-10-04 03:55:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 91c800eb-0cbc-3500-ac28-41e24260ce4b | -18.16982 | -53.34668 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4bcfa705-a3d0-339c-b332-9074138fe6df | -19.80403 | -45.15685 | 2025-10-04 03:55:00 | NPP-375D | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b020d59d-970b-3c15-ab15-ce925f617882 | -19.7995 | -42.09254 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4120f466-9e5e-311c-8963-aab23c19f5fe | -20.27213 | -43.78868 | 2025-10-04 03:55:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7638345b-68a2-3e93-b3e6-a18b89db70c7 | -19.65771 | -44.17725 | 2025-10-04 03:55:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c01170d1-ede2-36d1-a4b7-df738e2ff9a0 | -22.43083 | -46.88292 | 2025-10-04 03:55:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cfd6eeb-67e0-339d-ad4e-5edddef07fd4 | -19.57483 | -48.02025 | 2025-10-04 03:55:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ec408469-83b0-3318-9500-21a71bc86b99 | -18.58517 | -43.46334 | 2025-10-04 03:55:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad023cd9-c4d3-3067-b801-ae6cf617bdec | -17.29522 | -49.27192 | 2025-10-04 03:55:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 833d1592-eaa5-3e83-8931-88f4fe3414f4 | -17.70104 | -47.08703 | 2025-10-04 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0d8835f9-7c79-3eee-a12a-a4fb0a567971 | -22.07664 | -43.09611 | 2025-10-04 03:55:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f4a4fb7e-1afd-3997-93d6-28e753834a79 | -18.631 | -50.67496 | 2025-10-04 03:55:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7afc7b6d-cc80-3b0f-ba76-9d6600206375 | -18.68814 | -48.17945 | 2025-10-04 03:55:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cab991f9-1172-3dbf-a4c5-815a3ac7a456 | -20.02592 | -45.28659 | 2025-10-04 03:55:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c9a63ad-d5b6-3381-aefc-b02f04166aa7 | -19.10863 | -44.71152 | 2025-10-04 03:55:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a61c59b8-f5a6-3106-b488-fc061bab7ac1 | -22.07941 | -43.10106 | 2025-10-04 03:55:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9e1b6e7c-92c5-3b9a-bd9a-b7762ca85eb5 | -22.28351 | -46.71853 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8bd65c80-0b20-37d9-8595-bf624d43e9b0 | -20.41484 | -44.13254 | 2025-10-04 03:55:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e7d5d3ae-0616-35b5-ba8f-8e918262cf8a | -21.49387 | -43.89364 | 2025-10-04 03:55:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 30ef02ed-13f3-3fcb-9d9c-0b991e8abc92 | -19.73487 | -47.19146 | 2025-10-04 03:55:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54bb50a4-0c30-391c-aad1-b2b9a376de85 | -20.22489 | -44.17456 | 2025-10-04 03:55:00 | NPP-375D | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 931209ad-df7d-3b76-b672-8d852c6ceff2 | -19.79605 | -42.09188 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26381cd4-8cd3-3465-ba1a-0ef36463a824 | -21.62561 | -47.39923 | 2025-10-04 03:55:00 | NPP-375D | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec4619df-6089-3836-b3a3-98d7173cc079 | -18.41757 | -43.4873 | 2025-10-04 03:55:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ffee40db-e55f-39ef-9f5e-4ea50918cf58 | -20.84284 | -46.42332 | 2025-10-04 03:55:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38dfc344-ba9c-31b7-8662-cbdbf8b5db6b | -19.75025 | -46.50386 | 2025-10-04 03:55:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 618366c3-b7d2-37df-aab6-4b5993695cf4 | -18.66792 | -43.86443 | 2025-10-04 03:55:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be264b83-0ed3-377b-b09c-03cbd18c2fd3 | -18.64174 | -50.68129 | 2025-10-04 03:55:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e3b32da-d617-36a9-bd66-aaa4cec97aac | -21.19309 | -45.14019 | 2025-10-04 03:55:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9b15aa97-f806-3a63-b0fe-1f6e8c06f2fc | -18.23008 | -53.36774 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 860ed207-f41f-32ae-8147-8ff2c7da9a7d | -17.17115 | -53.03876 | 2025-10-04 03:55:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 383b466e-c195-394d-ae51-0a23b561b027 | -18.17494 | -53.35541 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5e400a2-beb2-3d95-b98b-db3c35e2a131 | -21.80931 | -45.6498 | 2025-10-04 03:55:00 | NPP-375D | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1160719e-dbd1-3fc9-a084-e3fe5b7434de | -22.28015 | -46.75821 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0c7d16a0-0047-34bb-8bce-ea96c9cbcdfa | -20.15901 | -44.19893 | 2025-10-04 03:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c377bbfe-e24a-3ffc-b71c-13eacc2ace1e | -19.7926 | -42.0912 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4742574f-651c-3ebb-920e-6f868de91215 | -18.23569 | -53.37429 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b7c6231-ed5f-3c23-ab88-ff8d18e7e333 | -19.96933 | -43.70497 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 212ab7e0-cc3e-3654-99cc-b766209d60a1 | -20.72029 | -49.61424 | 2025-10-04 03:55:00 | NPP-375D | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df106d92-35f8-3fc7-89e4-8308dc41a600 | -19.88909 | -42.62907 | 2025-10-04 03:55:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 810be66b-514c-3eab-a527-38e4aaf500ca | -19.79787 | -42.09119 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 12354994-aba0-3d2c-ac23-bd9b588dbf24 | -21.55452 | -45.27332 | 2025-10-04 03:55:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c9b906e1-d4de-3507-b67e-7432bf03af7e | -20.47646 | -44.81792 | 2025-10-04 03:55:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4c54f780-8b98-371b-a174-5cf371546bf0 | -22.28178 | -46.72738 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73da6da0-88f4-3a95-8e2a-4453506af867 | -19.7147 | -44.12346 | 2025-10-04 03:55:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b370aaf-8b67-349e-a9e7-6de1304e941c | -17.99264 | -51.63437 | 2025-10-04 03:55:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 342d2c5d-fae3-3748-b885-93dff1219866 | -21.19896 | -45.14861 | 2025-10-04 03:55:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8fc6d86c-209b-3fcb-9d05-b95bfea1cffb | -21.78797 | -45.33898 | 2025-10-04 03:55:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 232cdfb8-1851-35cd-8c5d-34086a86bac4 | -21.35138 | -45.79374 | 2025-10-04 03:55:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dfced2d9-9508-3405-bfee-3173318b622d | -22.49513 | -43.38801 | 2025-10-04 03:55:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 05f52eab-3cf4-30e2-ab26-7b664bec53ee | -18.97561 | -46.97348 | 2025-10-04 03:55:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd73ff20-7f7d-3eb3-b413-35edfc4d5d75 | -22.36165 | -47.03731 | 2025-10-04 03:55:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a653c367-b7fb-3d9d-995e-3a164863892c | -19.9675 | -43.639 | 2025-10-04 03:55:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 48bb401e-3c1e-3e01-8fd4-ea56b7170893 | -18.63686 | -50.67588 | 2025-10-04 03:55:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d72b09a-35fa-3d80-8151-bc6afedede79 | -18.17385 | -53.3634 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9656b592-f961-33be-b5d2-1a382b92c794 | -22.27512 | -46.76138 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2ce7f3d0-7f59-39ae-9d80-c99378eac470 | -19.89332 | -42.62559 | 2025-10-04 03:55:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eb8e56ed-5434-3196-8f6b-6da1db94d72b | -22.76488 | -45.30446 | 2025-10-04 03:55:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 08db0760-6eb9-3cd8-9ce4-8f259caad7e5 | -21.93168 | -46.60209 | 2025-10-04 03:55:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6edb26fe-5a00-3e6d-93ab-173f33ecc081 | -17.99885 | -51.63566 | 2025-10-04 03:55:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18873f97-19a5-33d9-892e-83fbb6d9b61d | -20.13511 | -43.98792 | 2025-10-04 03:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2fd93feb-87a8-3cf4-9d7b-8b4926a0643e | -19.96566 | -43.64114 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9e9c2890-3e5f-3290-a7b4-11e16613ca02 | -19.80017 | -42.08853 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README48.md)
