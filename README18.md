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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c6f89be-b117-3268-9e8b-e2a215c06e48 | -14.4587 | -52.5151 | 2026-09-01 03:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 55106437-72fb-3a9c-a95c-e6c8cddd68b8 | -7.2821 | -49.8201 | 2026-09-01 03:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| eb606ee2-f575-3786-9b39-8c32f4370477 | -16.4773 | -47.9381 | 2026-09-01 03:30:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a62b56fa-b863-3186-b507-4ece88aa1983 | -14.6732 | -53.5408 | 2026-09-01 03:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 62d62b21-2e05-3e88-b894-25897b1fe7ed | -7.5895 | -60.4636 | 2026-09-01 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| df912766-54ea-3fe4-a5f9-e84f18ddd5e9 | -7.5709 | -60.4835 | 2026-09-01 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 866d6ce3-677d-39f2-8a75-6c197e3f947e | -7.5894 | -60.4827 | 2026-09-01 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 16225617-97ec-3821-b77b-7dfb7ac8f17f | -7.571 | -60.4643 | 2026-09-01 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 376ba2c5-6d7f-33df-bd7e-ca7d8bfc7323 | -6.6036 | -58.5972 | 2026-09-01 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 56a3a60a-7b34-3ee8-9692-687a7ed44301 | -14.4587 | -52.5151 | 2026-09-01 03:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a0104c3c-1a6e-39c7-aa63-fbf451f3a623 | -18.5089 | -50.8974 | 2026-09-01 03:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| d8e6e209-3e38-3f1e-b5cd-00307a6740fb | -10.3577 | -49.9957 | 2026-09-01 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 637c513e-96ec-3e3f-a5c7-537fe8adc5e4 | -16.4768 | -47.9608 | 2026-09-01 03:30:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 5799d9f9-a569-3df7-8621-a15d79f7489d | -14.478 | -52.5126 | 2026-09-01 03:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c9641123-dcf8-3629-bdc4-8082bca7b39c | -10.2025 | -50.3109 | 2026-09-01 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 3684c07c-51ec-3a5e-bc45-c92704aa771a | -17.3921 | -42.3495 | 2026-09-01 03:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 3b879480-ea94-371f-947b-a046b5dd7248 | -14.4777 | -52.5339 | 2026-09-01 03:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| a793b22b-2ce7-33b9-a460-ccf8e5aee06a | -6.20393 | -42.51834 | 2026-09-01 03:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2657276c-4413-3791-b99d-fe7e80efb2bb | -3.86388 | -44.08114 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0ffd0cc-0586-3652-9f48-fd9ba3c092f2 | -4.85215 | -42.96073 | 2026-09-01 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 57cbefcf-c6c8-3a98-b206-978a37a0be31 | -4.08887 | -38.65702 | 2026-09-01 03:34:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 56500f09-59bc-3f9d-914b-ec36b3fe3127 | -4.77343 | -41.80057 | 2026-09-01 03:34:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| fd4c0f6c-f03e-3a92-8cd9-a45157f1dd3e | -3.85661 | -44.07979 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 67a5c9b8-02be-3144-9eb4-788cf3b0ac29 | -6.21043 | -42.51908 | 2026-09-01 03:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6a44c855-bfde-3324-a1d2-75d0060b167c | -3.87248 | -44.07512 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e397e877-2c3e-3583-8629-2537dfea1282 | -3.86231 | -44.08494 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f7f2f595-2f5a-3316-8494-217afad582ba | -3.85629 | -44.07645 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4d55968-57fc-323c-b751-bb82816dd4e5 | -3.85791 | -44.07264 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c511be20-0fe5-3bda-b913-ff8efbddb59a | -3.8747 | -44.05707 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1baaad6-b38d-33fa-80f4-7fbf4327caa1 | -3.87602 | -44.0495 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 501e8756-4f9d-37ff-b5af-dc2b760cfa95 | -3.85924 | -44.06536 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac076a76-a0a8-33f4-b51b-5c39c83dc9f5 | -3.85423 | -44.04556 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02fed18e-9d13-3811-a785-c9bbfab3ffe7 | -5.58792 | -42.31532 | 2026-09-01 03:34:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 23095566-254f-35aa-883e-3d78d578d99f | -3.04797 | -39.931 | 2026-09-01 03:34:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 75a71847-512a-325b-91e2-dc325e68dea8 | -3.05371 | -39.93196 | 2026-09-01 03:34:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 696f27a6-f365-3f8b-9be4-d9b9b76c295d | -3.8506 | -44.07157 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50d014ec-c034-32e6-85d6-8c67de9701a7 | -3.86922 | -44.05177 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47c279e6-fae6-3889-a163-954bff41c5ab | -3.85602 | -44.04194 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5e377b6-4d45-3762-a6cd-0652c45b898c | -5.91273 | -38.7429 | 2026-09-01 03:34:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cbea5edb-4b77-3248-b9b2-f88d17e94466 | -3.85198 | -44.06403 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a97513c6-ad61-389e-aef9-f94c633f6c6b | -5.5806 | -42.31672 | 2026-09-01 03:34:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 41c3b378-4b00-3d70-ace7-58a3202d13b0 | -3.86326 | -44.04334 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ac3e984-d639-3d0b-b181-759db2e28b87 | -3.85756 | -44.06927 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bf3cac93-463e-3fa6-96a6-13219bc2592b | -3.84897 | -44.07539 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93eb3727-2ec8-311c-a675-e94c7673939f | -3.86355 | -44.07785 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ab0401f-bec6-3e7e-a7eb-0ffd553588c7 | -4.76625 | -41.80452 | 2026-09-01 03:34:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9e56bea0-d987-3021-a1c4-dd424d235d4b | -5.5805 | -42.3197 | 2026-09-01 03:34:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8953e69c-ee4d-3846-b32e-e260a1904313 | -3.85506 | -44.08342 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61f0ebb9-afe2-3d93-8740-da686039c2dd | -4.08941 | -38.65387 | 2026-09-01 03:34:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf6d138a-d9cf-3ac5-84b1-917187afff26 | -3.87055 | -44.04449 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e752da57-a64e-3697-8236-af672220c9f1 | -3.86874 | -44.04831 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c86bc018-4d08-32ce-a586-4bc90298e09f | -3.85475 | -44.04887 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd76b1b1-186e-3079-88c2-e933cb752135 | -3.04864 | -39.92704 | 2026-09-01 03:34:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9310688a-8803-3ad4-b80e-4f17ebdf8f05 | -6.5978 | -38.29399 | 2026-09-01 03:34:00 | NPP-375D | VIEIRÓPOLIS | PARAÍBA | Brasil | 2517209 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b6ac7e1-ac42-3d71-b243-aa4647a23805 | -5.90767 | -38.74204 | 2026-09-01 03:34:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c460318-ec33-3f96-82dd-0185893ec07f | -3.8738 | -44.06788 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10555374-aa80-392c-bb39-45effb8adbe3 | -5.58703 | -42.31776 | 2026-09-01 03:34:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a23aab4d-df74-3f3a-ba0a-005fad31fcfc | -3.8652 | -44.07388 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd87510f-4601-3713-95d2-d73dfb23e417 | -3.86148 | -44.04698 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bc4dad4-3ded-3922-ae47-fd6b674b2bcb | -3.0473 | -39.93495 | 2026-09-01 03:34:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 7bf666b6-f507-39c4-b25a-ed3f93a22b43 | -3.87211 | -44.07184 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9eb64f13-29e2-3ac5-a79c-d8571f7583fc | -3.87514 | -44.06052 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a26f6330-8bf6-3a90-839d-2d315eaff84b | -4.25409 | -38.6955 | 2026-09-01 03:34:00 | NPP-375D | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 70908e13-c1ee-3a77-9337-358be3bd4533 | -4.85783 | -42.96775 | 2026-09-01 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| ed889d95-b6c1-3883-8ef7-50bdd54fc9d2 | -3.8734 | -44.06451 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34248e9f-da86-32ed-98ce-4a4b6a3901db | -3.87648 | -44.0531 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 02f71030-20cd-3438-9364-6ad410ba8001 | -4.8589 | -42.96181 | 2026-09-01 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3da3e9b8-c4ab-3fa5-8b8c-f7ab0e4c251f | -3.86744 | -44.05569 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 786d5600-3b87-3f07-8372-d63aeabc77ac | -3.86272 | -44.03992 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 211f64c4-aaa4-39f6-88f2-f9007d7bc1e5 | -4.76715 | -41.79942 | 2026-09-01 03:34:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 84347d28-fb4b-3bfa-b19e-1e371a623b4b | -3.96469 | -38.31064 | 2026-09-01 03:34:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17853bb8-bdb4-3b55-b3d4-47671fd76cd2 | -3.87086 | -44.07898 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb4259f1-3879-35c9-9733-8d5dfb5b0a22 | -3.85886 | -44.06184 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0306fa33-63f4-3750-b4d8-945c497731f2 | -4.25356 | -38.69865 | 2026-09-01 03:34:00 | NPP-375D | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| eff4bf74-c49b-3f22-b771-da613deee48b | -3.87119 | -44.08226 | 2026-09-01 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9c86316-a9bc-366d-ae98-5b2a6c042a68 | -11.9086 | -45.07931 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae1749f4-4128-3ee3-96fa-df45cd1f706a | -10.16572 | -45.76184 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa828df0-17d8-36db-98f2-ad91ff4a7119 | -10.85908 | -45.37645 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac924dbf-fa1a-337a-9e27-aa81e68c28ce | -10.87179 | -45.37247 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67c8a1e6-3771-3932-ab76-b7d8f2a76dcd | -11.91129 | -45.06645 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a7efff3-f204-3c0f-8a7e-0d9dbee08444 | -11.31096 | -45.18041 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5206bc00-7af5-3430-b92d-2364b78d3311 | -10.82546 | -42.36938 | 2026-09-01 03:36:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 70b02e4c-dde9-3f42-af09-bf545b3e16ca | -8.48809 | -44.75236 | 2026-09-01 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0de95676-8be8-3cec-8900-2cd5f784d132 | -11.31049 | -45.21788 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17cd1fa5-44e4-38f0-a3c2-8e4e55e86882 | -10.02829 | -44.70058 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1bdfbdae-0317-3630-8d25-e9be08890320 | -10.02218 | -44.69236 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 43af2d0b-1e3a-3573-a196-0acdfdc3aa7f | -12.06844 | -44.9969 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5bf238d-b594-3ffd-bfbe-84e1e848cd4d | -10.02952 | -44.69436 | 2026-09-01 03:36:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3d29b849-6bec-3eaf-9091-b80edda4b7b3 | -11.31907 | -45.1759 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cb6d841-7e20-34cd-9c90-7994e72567fb | -11.93791 | -45.0745 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8599614f-2713-3ae4-bd86-f4c813dd4ffb | -11.49032 | -45.10319 | 2026-09-01 03:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6156ff32-53fe-31c6-a411-4a018b9e4f3a | -10.85673 | -45.30492 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 370e2591-ecd6-3501-abb7-b4c046c562b5 | -12.21313 | -38.98172 | 2026-09-01 03:36:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4c7b19f1-f31f-3300-b31f-94b876e409af | -11.31183 | -45.21131 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a687041-73b9-34df-8b6d-0038c31b40ce | -8.49131 | -44.75469 | 2026-09-01 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06682ff0-5edb-3e4c-99eb-da3516b9ffe3 | -12.09986 | -44.98084 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5659fb3e-347d-35f5-8e0f-38195c965b48 | -11.32032 | -45.16975 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2788b581-d45c-318c-8c47-4a6ff441e6f2 | -11.91202 | -44.81967 | 2026-09-01 03:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 607a7c0d-9481-33c7-83c7-e6237d719473 | -10.86197 | -45.36218 | 2026-09-01 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14b6bfca-b2f5-32f1-8853-4e591faaecb0 | -12.06954 | -44.9916 | 2026-09-01 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README19.md)
