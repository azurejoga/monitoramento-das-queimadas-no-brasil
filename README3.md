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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df129247-8a0e-3cf2-9499-fb3aceef3923 | -21.44544 | -57.14514 | 2026-03-18 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 92f12eaf-8501-34f6-a70e-9941fc801dbd | -21.98034 | -54.62598 | 2026-03-18 05:16:00 | NOAA-21 | DOURADINA | MATO GROSSO DO SUL | Brasil | 5003504 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0f68f4ce-903d-3773-8eb3-02c71c9f6f4a | -20.00013 | -57.11318 | 2026-03-18 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1832545d-674f-394f-ac49-f99a59ec2af0 | -30.4763 | -56.3948 | 2026-03-18 05:18:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| f372c2cb-6448-37c6-8b99-64bf583c84d5 | 1.07709 | -60.68637 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e4e56f5-ff67-3d29-abe7-33c10a321873 | 2.66213 | -60.1069 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87a9d78f-0b03-3fcd-b7cf-79e063fb40fb | 1.73442 | -60.53711 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6b208d5-bd41-3f57-80aa-ddb12c27d927 | 1.41381 | -60.75788 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 471869ad-d857-325f-a6b2-30fe110c2726 | 3.2037 | -60.32584 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71e4b671-82c0-382d-a96a-5d376f8d1867 | 3.05709 | -60.76587 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1ced716-5ae2-35d3-922b-ce407866625c | 0.52484 | -60.26436 | 2026-03-18 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cb1df01-abc8-3b71-995e-4b4a39354e0d | 0.95554 | -60.22839 | 2026-03-18 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56968d62-a65a-3af4-b54c-d4cecd458dd2 | 0.83582 | -60.13416 | 2026-03-18 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef8f1842-647e-37a3-94f4-885cec2152b7 | 1.87915 | -61.32102 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91432c76-d58d-320e-a9e6-b57852741609 | 1.54998 | -60.40462 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 364f9227-be0b-31dc-ad1d-a05f76bb9ebb | 3.41037 | -60.17672 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c19f82c-410e-3480-8f07-4dc5fcff696c | 1.87489 | -61.22952 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2edbc129-4451-3b5d-9c40-459d0f216d77 | 3.16685 | -60.11651 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b26ff43d-f1fd-3211-be42-c9dc1cd78799 | 3.20314 | -60.32229 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2f347b9-4ae2-3a15-98de-20565234ea05 | 3.20258 | -60.31875 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44323e82-bc77-3c39-a544-454e11332a5b | 2.30942 | -60.23978 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fb88f3b-a75f-3633-a261-790d5abc439a | 1.62367 | -60.27863 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b0ec8da-8ada-3a17-90a7-b196a728be4e | 3.08096 | -60.76568 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de882e0e-f066-362a-accb-94f5472d3c4f | 2.24566 | -60.30054 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9f74679-d8a5-3732-9bdd-c418a84b8c60 | 0.42351 | -60.00233 | 2026-03-18 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c219cf0c-1233-3eda-8e46-0468a7f4a64c | 1.22356 | -60.46269 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a3760512-3bba-36b2-8476-2a94daef5078 | 1.41045 | -60.7584 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 354b4f88-a87f-3553-bf61-b7429a4808ac | 1.07653 | -60.68281 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39493ce1-c26c-3e1b-a523-c85db939d8b4 | 0.77284 | -59.86854 | 2026-03-18 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2986bfe7-f335-3466-9e69-b5d746725be7 | 0.95997 | -59.54662 | 2026-03-18 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b17f0c0f-3d3f-303a-afce-bd1e3a9d99b2 | 3.20288 | -60.14747 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f209d2af-aad5-3c76-af17-2da5c31d352e | 3.4171 | -60.17566 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b5910af-9b2c-30c9-9f57-bc155e707e05 | 1.5466 | -60.40516 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7c540ef-c955-38b6-a617-b8fce5294d2f | 1.98673 | -60.89102 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fab176a9-a86d-3104-89ec-cbfa7428f5c9 | 0.9752 | -60.00264 | 2026-03-18 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8911058-3f14-32b9-984c-5e3472aff789 | 1.22018 | -60.46322 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b558ef96-fc8e-33ca-8ad0-93ebfc097469 | 3.78568 | -61.30322 | 2026-03-18 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 349cd632-8805-3103-984c-2c48371f3e28 | 1.07429 | -60.69045 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22124307-3385-3b7b-9f1d-8b82982286f6 | 3.20569 | -60.14336 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08ae2edd-5438-3e3b-8eb4-3747861f3a39 | 0.51743 | -60.26175 | 2026-03-18 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6936b3c7-d9b5-37d8-86f8-ad77c72c5db6 | 0.96408 | -59.54994 | 2026-03-18 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d27fee69-b2a4-30f6-ad67-22fcdbbc8cf8 | 1.87821 | -61.229 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f37f884c-55eb-3c32-a526-68df5db88a76 | 0.94737 | -60.39749 | 2026-03-18 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70aced60-4242-332c-9d99-126c4c3cf0e1 | 0.77343 | -59.87231 | 2026-03-18 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e05223f-e0c7-36ca-9dca-cbbd196838d1 | 3.12357 | -60.73757 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82b8adfc-bdba-348f-a4d6-65d576df7517 | 2.34636 | -60.12297 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3d7202a-2511-385f-8111-fe60e4b1573a | 0.95612 | -60.23204 | 2026-03-18 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42178f80-4f2e-3f8e-8ccf-d4910499de9f | 3.05375 | -60.76639 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d73e1fe5-11b9-380c-a871-a25212ef18d3 | 1.58277 | -60.19591 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d240f099-7a25-34e0-a1f4-48162ab949bf | 1.57176 | -60.32376 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e170451-05a4-3d00-b09b-ef4f76a028d9 | 0.95213 | -60.22892 | 2026-03-18 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 81921cce-627c-3fcf-845e-3787ab057b2d | 3.78236 | -61.30373 | 2026-03-18 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18a6da3b-5e76-3862-9646-ac555e1a81fe | 1.15653 | -60.32836 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84b967ff-5d4b-346f-81a0-be29cfbfea61 | 2.43952 | -60.24436 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2301d33e-8752-35b2-bf76-b134da14c047 | 3.41767 | -60.17921 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d561eda0-a727-379e-9419-0c819d0dd7a5 | 1.1571 | -60.33198 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eafddc28-83f5-36a7-be1d-2c8388657bb0 | 3.42439 | -60.17814 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3baa1473-7a60-30c0-9cfe-5d131ebb8880 | 0.51401 | -60.26229 | 2026-03-18 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0069fd05-ccfc-3b86-9c9c-d3c374650237 | 0.76937 | -59.86907 | 2026-03-18 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db57febc-50c1-3456-89aa-7b285cb95ebb | 3.05653 | -60.76239 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cbfeafa-fb81-360c-9ae3-7e64beac01bf | 1.08046 | -60.68585 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1582e7a-80fb-3d44-b23d-5a3a65d9b180 | 1.13034 | -60.46944 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5aaf83f-55a7-397c-9978-3f20e3f3fa38 | 1.07989 | -60.6823 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f9fe8d84-433d-3fe6-adc6-65c3b7b041c1 | 0.96058 | -59.55049 | 2026-03-18 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0e0b553-465e-313b-9426-1d2fe980c847 | 3.73615 | -60.75524 | 2026-03-18 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba9256e6-ef15-3845-9392-a3ecf20fefbd | 0.76997 | -59.87284 | 2026-03-18 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd79ec2d-b1cb-37a6-a8ab-fb77534db25f | 1.08663 | -60.68124 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c03bd807-3f6a-39a1-9d95-e046f30d2ebf | 3.07707 | -60.76272 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9e9672f-c4dc-36a9-8036-af2a66e758ac | 2.44289 | -60.24382 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0da6c9f-3860-3c68-9a8e-e32acc4022b3 | 2.41746 | -60.57236 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67aef2b4-12da-3f3d-b05a-24ae48685a35 | 1.72008 | -60.29356 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0264dff-220f-33f4-8d6a-65be2ac62856 | 1.17065 | -60.30756 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ecdd4be-224b-3473-a71d-2b757b8a693e | 0.97176 | -60.00317 | 2026-03-18 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d63a3b1b-b323-37a2-8344-54ba97eaf38e | 1.72065 | -60.29716 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e022c95-5505-3aad-bad9-ddc9c75bd819 | 0.52085 | -60.26121 | 2026-03-18 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5578ea0b-e2ff-373e-9b4e-3de13d7f79df | 0.53625 | -60.27007 | 2026-03-18 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89c08af8-4282-3e9d-a39f-7e9699a68287 | 1.98618 | -60.88753 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ba319058-0ac2-3424-a25e-ca9445bf018e | 3.40814 | -60.18437 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0e8b14b-a229-3cb0-87fc-325008af21b0 | 3.11248 | -60.77499 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a326c5d3-6191-3e91-ac65-88c93b957fc6 | 0.89347 | -59.81093 | 2026-03-18 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b9455c4-8f4d-36a7-a20f-35ad0efb2bf5 | 3.13356 | -60.71455 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e865db18-c714-3402-9975-2b72d30c150d | 2.83358 | -60.59351 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b8acbb9-db26-3499-8b33-b0ef29408582 | 0.42696 | -60.00178 | 2026-03-18 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fe562f02-6251-3370-b7f8-d631ec04c726 | 3.41094 | -60.18028 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23c0cc4d-3053-3faa-b53b-04b3cacf5570 | 3.11192 | -60.77152 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a0e4ae-ff7e-399c-9248-3fd80ffa64e4 | 0.73478 | -59.513 | 2026-03-18 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1093e4f3-7f2a-312f-bcce-21c0edfc2089 | 1.07766 | -60.68992 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a334dbd-7ccb-3338-ae61-65d825d6f0e0 | 1.96269 | -60.5668 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82045b5a-4bde-3748-9dd3-f75b15a6f7c0 | 3.05986 | -60.76186 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f2297e5-163d-3f89-a194-06ea7918e71b | 2.66551 | -60.10636 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ea39735-6bee-3e62-bee7-e02e33abca92 | 1.17008 | -60.30394 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63e5c56d-c2c8-3428-b50a-88a57ea59fc6 | 3.12413 | -60.74105 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31d4e9ad-c959-3c78-8550-29862489967c | 0.96511 | -59.55066 | 2026-03-18 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ded36a2-f840-3059-a93e-d6a65c92a749 | 1.62396 | -60.27901 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c3dcbd8-1081-306a-b806-d966f0ab098c | 2.31337 | -60.24284 | 2026-03-18 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7267af2e-eddd-3f3c-8280-d58ebaaee16b | 2.82922 | -60.0362 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53fd6b23-259a-3402-b67f-c5edd27589a3 | 3.42046 | -60.17512 | 2026-03-18 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dcdbd98-1285-3dbe-84e0-d35ecaa53e24 | 0.96468 | -59.55381 | 2026-03-18 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6043648d-26c6-3161-b040-2049c530bf76 | 1.72404 | -60.29662 | 2026-03-18 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bd1746b-6f00-38df-8b02-89e4d656b59f | 3.0804 | -60.7622 | 2026-03-18 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
