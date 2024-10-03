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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1524dac7-1d22-3a6c-a563-4a14b4ed0647 | -8.95624 | -52.80128 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d333886-2658-3e47-8d6f-b60e9f4be7db | -8.95292 | -52.80076 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f0e20bb-f13e-3314-9d3a-54195d8818e7 | -8.94959 | -52.80022 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 409f1c98-747a-3d32-91d7-726b0abefb71 | -8.94905 | -52.80371 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a186445b-4645-3d8c-a738-325c07f320b9 | -8.93678 | -52.77312 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69245cef-c2fa-3f14-b857-462f21d95001 | -8.93624 | -52.77662 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1449c679-daf6-31ad-a620-da620f3bf635 | -8.93401 | -52.76907 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2976f33-9268-3505-b600-4f223e203110 | -8.93291 | -52.77608 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1a4199e-6538-31c8-ba24-ffe8c7cfab4e | -8.93177 | -52.76152 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ac43f55-df98-3c4d-bbce-0ca69653deb3 | -8.92526 | -52.82503 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfc448ea-0759-3cf4-9300-49463152a87f | -8.88404 | -53.00102 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 058fe59d-f31c-3824-9da9-fbf8286a7e4b | -8.88072 | -53.00049 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a67a581-2a18-3952-a0c0-96d9e2b4c95e | -8.88017 | -53.00398 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aad32c6-ceae-3c73-b18b-af0284ee544b | -9.46422 | -52.09533 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcdf5a8d-5077-36b5-9e20-889f0f1a9c79 | -9.46368 | -52.0989 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cb4e9f9-624e-3bf9-a479-7a045045c8de | -9.46086 | -52.0948 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c44b69d-a636-30c4-a652-d6d67af6ef27 | -9.46031 | -52.09837 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8388b062-dc51-3b4d-a694-3c2cfdc3874b | -9.0256 | -52.1116 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19a2c2b3-3335-3481-9742-68ff91c72d1a | -9.02506 | -52.11514 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2209bb8b-17a1-34c4-a162-167f5e6684e5 | -9.02224 | -52.11111 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8e68dd4-280a-339f-8709-b54daae2ff19 | -9.01944 | -52.10701 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef052ec6-4227-36eb-9823-cfdfeeed9207 | -9.01889 | -52.11061 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fa3a0bd-304b-36e9-92a9-db786c516430 | -9.01777 | -52.10647 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08f4caa7-d746-3535-95e9-06fa2d313cea | -9.01721 | -52.11007 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 036d232b-b6d2-36d4-bd75-0a6a3f19217d | -9.01225 | -52.14199 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9316c3b2-b9db-3ab9-af23-e6578c9760c4 | -9.00889 | -52.14148 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 420367bd-77e8-3576-bc70-f13f9e7dbf38 | -8.54688 | -51.79578 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98279996-9340-38f2-b348-043da5f27895 | -8.54462 | -51.78804 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 426fe1b6-b6cf-31e4-b1fc-2ed13c573c65 | -8.54406 | -51.79167 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 513f3f1b-d734-3ef0-8811-0ee228fc2489 | -10.91075 | -52.40997 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8947bc2c-716b-353c-811f-faca9ce99b49 | -10.91019 | -52.41357 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 007a2bc8-9ca7-3abf-bb4b-4b3ddc87118e | -10.90963 | -52.41719 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 84508915-ac7e-3342-89d8-0c041b845bc9 | -10.90907 | -52.4208 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 295651ae-8d6b-3e4f-bf8e-31b10dbfb80a | -10.90851 | -52.42439 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| adff88f6-a24e-38b2-918d-6c48112dfcba | -10.90796 | -52.42799 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8eec326c-ab04-36a8-93b7-6de743792984 | -10.90794 | -52.40583 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 325efb6d-4ed7-3930-941f-f22a5a189179 | -10.90738 | -52.40944 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43ec9add-90b0-345d-8210-68d4fab2887b | -10.90682 | -52.41305 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1aa2f992-bcd5-3986-b8a8-a8cafdee8edf | -10.90626 | -52.41666 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cefcbf54-5852-3d35-8515-ffda8a41d30f | -10.90571 | -52.42027 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9262bad1-ab41-3fe5-a859-c8df1bd1ab2b | -10.90515 | -52.42386 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d0850c5d-fa46-326f-b78a-dc2a852a7229 | -10.9046 | -52.42746 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d8fbe14-a2a3-3591-851f-313c9fc4afba | -10.90457 | -52.4053 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0de96a70-4efb-33eb-810d-b3f20f188b14 | -10.90401 | -52.40891 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9a98f5e-eed9-3f9a-a7cd-cf15d3a45559 | -10.90179 | -52.42334 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3451e8d-931d-3aa7-9e59-10292d2afd3f | -10.90123 | -52.42692 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29add0e9-0b5a-37ef-961e-960dbd319fcb | -10.90065 | -52.40839 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa2d4ea3-e373-36b4-a423-6976ccd687c9 | -10.89787 | -52.42639 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23fcf396-9e83-3c73-a56c-f0da847169fa | -10.89728 | -52.40786 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce0b1a07-bd3f-3fb1-b2b5-32fcce839c6f | -10.8945 | -52.42586 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 091da959-7802-34ba-ac4f-02f6c0cdca15 | -10.89391 | -52.40733 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 515cbe0c-98f0-3f35-a4f0-6c0fcd5ebfd2 | -10.89336 | -52.41093 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 878abe34-dff2-3ecf-9144-034aebcfaa8c | -10.88999 | -52.4104 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8456e8de-6819-31b1-bb16-3a8fbb8cb042 | -10.88215 | -52.41654 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c4df5e4-0c8e-3125-81ac-b41fd79a4330 | -10.88049 | -52.42734 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01a61d2b-2d57-3faa-85bf-4c7fcaafc9a2 | -10.87934 | -52.4124 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee7eef45-5c27-32a9-813a-c168447f4bb3 | -10.87879 | -52.41601 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14a53c0c-d1c5-312f-8b1c-741d693e0f43 | -10.87824 | -52.41961 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3071bc58-75ec-3075-bda4-20383b6c093c | -10.87768 | -52.42321 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c2088bb-eb79-395a-acfe-d26c2706f460 | -10.87598 | -52.41187 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 576af0de-f451-318c-bccc-bbd617607656 | -10.87543 | -52.41547 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0d29ecc-9054-3003-bb5d-b1e13ac1f3eb | -10.87487 | -52.41907 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbf3322d-34b1-3b84-89bb-24bc66c7270c | -9.84294 | -52.07571 | 2024-10-03 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81fe8203-5632-3c41-b0b8-6528b12ec505 | -9.84239 | -52.07931 | 2024-10-03 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d19937d-1fe2-38e2-9e2b-3caf8a8a1585 | -9.83957 | -52.0752 | 2024-10-03 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 64a214ab-2f55-3a8c-b379-97529b328c74 | -9.83846 | -52.08241 | 2024-10-03 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1eb9066f-8c96-36b2-986b-2958400f85a1 | -9.83454 | -52.08546 | 2024-10-03 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8582d202-fb78-3e4a-b4f3-d84306d57a12 | -10.65699 | -53.68561 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb36c886-8c7e-3602-9a62-2feb3d1ea313 | -10.65367 | -53.68507 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79ee1942-9812-3257-aac4-fb9e58892821 | -10.65145 | -53.67751 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79095803-5d98-33f1-adbe-2cbed869e4f6 | -10.6509 | -53.68102 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 867a4f54-ed40-323c-acd7-1d00193cac26 | -10.65035 | -53.68453 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f686d77-ce9f-3477-8616-50400596d2b5 | -10.64813 | -53.67697 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2b27aa9-462d-3d89-96e8-99b9b8705c1e | -10.64758 | -53.68048 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e341d49-d250-3c35-bdad-6263d3d9b899 | -10.64702 | -53.68399 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a9b1d99-27bb-3212-aaeb-d180def02c08 | -10.64425 | -53.67995 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09f1a579-55f2-3d00-a369-141750843e8f | -10.64314 | -53.68697 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81288c26-4806-36a8-82cf-75ae06a3dbea | -10.64037 | -53.68292 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8238bec4-63a5-3d10-836c-110722b09114 | -9.62204 | -53.18958 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b23dee52-2b7a-3788-a43f-91f11ddd2bb1 | -10.63982 | -53.68643 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e71f3da-8813-3bd9-8a0e-a053abe961a9 | -10.63705 | -53.66079 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b98ffaf1-6501-3f28-9427-150da0a35da5 | -10.63649 | -53.68589 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e8172781-64b3-3b8e-911b-76fc5252557f | -10.51705 | -53.19927 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac96c745-7cd2-3b77-bd3a-22708626340f | -10.479 | -52.97 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45ccdb04-25b6-3a78-b348-0a0d97cced3e | -10.47676 | -52.96243 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c885e12-5162-34e2-8569-0c5767d761bc | -10.47343 | -52.96189 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac1e2771-9db5-3b66-a9eb-1e2e55ace727 | -10.46788 | -53.31727 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8c073bd9-be30-3636-968b-9f2e87412c2d | -10.46733 | -53.32078 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01829dc1-06f9-37b0-a3e3-e05e465f8567 | -10.464 | -53.32025 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 372e9670-90e7-3863-91d5-55b299f60704 | -10.459 | -53.30865 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 258c91d2-7493-3b08-b710-646726b27032 | -10.44842 | -52.94708 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 122f3024-950a-349f-8d8d-4bbd3fb0a78b | -10.44618 | -52.93951 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46a02407-8c08-3fd0-8720-493e97d94f3b | -10.44564 | -52.94303 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afaf6a34-24ba-32a4-801a-d6e91212ffb8 | -10.44399 | -52.95359 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab31af70-1565-3686-9f70-e6d55956994e | -10.44344 | -52.95712 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8d47dea-829f-3a50-bc39-32a48421b11e | -10.4434 | -52.93545 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b44d44e6-4d1e-3b31-87d4-a24ad638e2cb | -10.43956 | -52.96011 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52d4009d-ad9d-3713-8045-edd1c13eeb5f | -10.43758 | -53.66132 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e553e637-bf17-3921-b5f0-4211716a01d2 | -10.4337 | -53.6643 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6b41205-943b-3f5d-a4a5-df6b8c00665e | -10.40532 | -52.92233 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README130.md)
