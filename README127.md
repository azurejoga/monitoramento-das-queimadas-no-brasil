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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 090e0c1b-c194-31f0-a03e-769d944225b2 | -16.58485 | -57.25594 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 48ac7c37-af5b-386d-9893-f2962a2c36fe | -16.58031 | -57.25497 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ae16352f-0703-3184-9ac8-8060d663e613 | -16.57584 | -57.22909 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ccf0cd11-3366-342c-9f86-439de6a85e23 | -16.57575 | -57.25403 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ee9d0306-bbc1-36b2-af80-2ba598d08bc1 | -16.5683 | -57.29256 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cec257e4-56df-36f4-b900-7ef5806d70a5 | -16.56768 | -57.2224 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c2d5d6be-d0b0-39c6-9989-418ba8cfe8d0 | -16.56737 | -57.29739 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| fd500c5a-585e-3340-ae07-0f4d363cac5c | -16.56397 | -57.24155 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ab1baf82-8e3c-32f8-8f7b-8b42228c10cf | -16.56374 | -57.29161 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 22a6d1f3-3c5c-3b08-b956-4c1a8393e0f0 | -16.56304 | -57.24636 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1f30d08c-e712-3117-8eec-d9bcbba115e3 | -16.55918 | -57.29065 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0d61e449-067d-3320-bed2-acfeda82869e | -16.55556 | -57.28486 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e4e5d830-6972-304b-8da6-d2695774e07a | -16.55214 | -57.40075 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 524d231d-92e7-3778-954d-ff55619b5086 | -16.46913 | -57.29507 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fad4fb49-9cca-307c-b999-88fa282cfdb8 | -16.46549 | -57.28926 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| db78de7d-391a-3c18-b44a-796d4d8297b6 | -16.45905 | -57.29801 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f42ecbca-1576-3108-9c24-c388adaaa2ec | -16.45353 | -57.30191 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5fb3c2e1-26dc-3b59-a8b3-a0b33234390a | -16.4499 | -57.29609 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7ab61a8a-2b50-390e-812f-46c7549fe553 | -16.43187 | -57.38894 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6028af57-4ed5-3f48-af48-c4f94e83a959 | -16.42822 | -57.38305 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 80c6a261-3f46-3488-8107-9fceb29a8f4a | -16.4171 | -57.39096 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 685ff1f4-2cf2-3300-87b2-b230fb17f700 | -16.4125 | -57.38998 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| ca61371c-2b58-3c25-8399-a24888a8017d | -16.41153 | -57.39491 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 0cc8c779-c4f1-3322-9efd-1db834bb1e7b | -16.40982 | -57.38737 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d0a52874-5948-367b-b5ac-bfc40b6cab7b | -16.40693 | -57.39393 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 75713d7a-2af6-37b4-98d4-c18fc4e45d57 | -16.40522 | -57.38638 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b5469638-8cd0-3462-b22f-ffd708f80328 | -16.40336 | -57.39626 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c93567f5-44c2-3393-b19d-4a317813ee5c | -16.40233 | -57.39295 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4730a073-4b0e-328c-bf39-ece323b6a8cf | -16.39969 | -57.39032 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5e1dbfe2-6ffb-3fe7-b07d-e066d2e305c7 | -16.62762 | -57.18044 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8aaee237-cf04-31cf-a176-76121fcd31a0 | -16.61585 | -57.1928 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8560f4d6-3f17-3b25-9757-e1c3d0b095d7 | -16.61494 | -57.19755 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 11b4c473-4410-349b-bec0-59f0423a2b6c | -16.61134 | -57.16714 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b6ec72c7-ba35-3b47-bbbb-f84cd77d5266 | -16.61132 | -57.19184 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e19f34f3-6d45-348e-91cb-71b681079c7f | -16.61041 | -57.1966 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 25d5dbe9-e0fd-3465-9626-c0f52953e92e | -16.6095 | -57.20136 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 5f87d9cd-d5e0-3db1-ba68-4c4f75a85f5f | -16.60861 | -57.18138 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 28c8ff35-8b12-3696-9d24-9364e5df407f | -16.6077 | -57.18613 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| 600b32e3-48bb-3dd0-9fff-2e62a06e8bb2 | -16.60679 | -57.19089 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| 4a2df80c-88ac-378a-8c45-02c89217fa08 | -16.60588 | -57.19565 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.1 |
| d72ec5bb-825a-3596-92b6-6a738b01dc87 | -16.60497 | -57.20041 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 5eaa0984-8126-3acc-b801-39cc44954596 | -16.60408 | -57.18043 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d70b4ea8-a5be-3ec9-99b1-3c92aa8fcc35 | -16.60317 | -57.18518 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| 278e6afb-18c8-326c-96fd-d624ce6cd476 | -16.60226 | -57.18994 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| 844ed4bf-05c7-3598-b2cb-4ebfeb313476 | -16.60138 | -57.16999 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8335fcb1-4f8d-3524-8017-4d4f4749f211 | -16.60135 | -57.1947 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 1fdd9d92-e3eb-32ee-9bf8-35aabe759771 | -16.60047 | -57.17474 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 184e41fc-e305-37c9-9cbc-7e60c34bb953 | -16.59956 | -57.17948 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b2c46fb3-b442-31aa-b571-1b304fe64748 | -16.59865 | -57.18423 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.9 |
| 7c1dae0f-1738-3537-8a79-5aac658ed2e0 | -16.59773 | -57.18899 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.9 |
| 5c6e5057-0033-35b9-ae67-fe1b9590cc8d | -16.59686 | -57.16904 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4aa32ef4-9fb6-3f04-915f-c67135a036b4 | -16.59682 | -57.19375 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 667ed598-b7e7-31a0-a586-43cbb5104c45 | -16.59595 | -57.17379 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| df1a1df5-c146-36d1-9ce0-d87cdeddbf33 | -16.59581 | -57.24817 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8db618a8-5ef4-372c-a2e9-81a68f5055aa | -16.59503 | -57.17852 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 40f5c94a-38ea-344d-aeb8-4bcdec2aad43 | -16.59412 | -57.18328 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.9 |
| a6d6a205-a372-38cb-ab1b-8a4bf76d2c75 | -16.5932 | -57.18804 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.9 |
| 8d62905b-a76c-3ed4-b913-c6d19fa86636 | -16.59033 | -57.25208 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 824abf18-216c-3176-a2cc-3c2e90283f72 | -16.58941 | -57.25689 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c328215a-579c-3709-9ae4-898c1828d20e | -15.88869 | -57.15348 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98a9fa3e-8288-3395-b926-520a43eb566e | -15.88501 | -57.1478 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53cdfd85-fca2-3801-a12f-1a8927bb4e59 | -15.88422 | -57.15197 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30a59963-33a7-3a97-8dda-6d7f31dc4720 | -15.88134 | -57.14205 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d343ec6d-0971-3689-89b3-80dcf264aa2f | -15.88053 | -57.14631 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c66e7b71-28a4-3722-bc94-7c5d148e41c4 | -15.87974 | -57.15048 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9f24563-4080-372d-b855-087a57319731 | -15.87853 | -57.13179 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25190c2d-0d4c-3af9-b1d4-234609d3d956 | -15.87684 | -57.14069 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b787c6d-3278-350b-99ff-8230bf5f1723 | -15.8752 | -57.14931 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 783d8a94-5799-3494-9d20-28a31fd4762b | -15.70838 | -57.43036 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abd060ce-7f73-3558-b134-4efa6052f70a | -15.69379 | -57.40501 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb9a59f5-1308-313e-8924-91b044e03208 | -15.69185 | -57.41512 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1140cb15-d1ad-3f25-8fed-802ae3ceefc8 | -15.65183 | -57.39588 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5967b400-0e21-3ad4-b231-c68d95775952 | -15.64987 | -57.40002 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc85b9c0-9bf0-342a-b1b3-7070ed4f09d1 | -15.64882 | -57.40559 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c78addeb-a7ca-3199-8519-9f55fce880d3 | -16.59488 | -57.25302 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 03f81f33-e4a4-330a-8b85-9b19f889a421 | -16.5712 | -57.25307 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 707861ec-b2cf-3277-be81-38d8c1c62547 | -16.56012 | -57.28582 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2403ee53-88b9-3979-9eaa-560edf79ba00 | -16.55462 | -57.28969 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b34e0195-8f20-364e-a20f-f6347761f8bc | -16.4737 | -57.29603 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 25ab3607-3bca-3146-84fd-34bab10411f3 | -16.46456 | -57.29411 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3263d621-7d39-39d8-a2ac-0bf01fea3bfc | -16.45811 | -57.30286 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9caf1284-2b0e-378a-a098-1a5e2e173ca2 | -16.45717 | -57.30771 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ea839df2-3676-3a58-83b4-24ce0659b6b5 | -16.45623 | -57.31258 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| eb2b50ba-e902-3b52-be17-f736a8f075d6 | -16.45447 | -57.29705 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2ae32e90-a11c-3ad9-912b-a61f97595ddf | -16.45259 | -57.30676 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 33c04b97-0991-3d2d-95b0-26287954287e | -16.45165 | -57.31161 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 29c105b3-0c98-3e6c-90c0-9ff4f2358a96 | -16.44896 | -57.30096 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c6f62cb3-7119-35cd-b32e-c7025ab8c734 | -16.42727 | -57.38796 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ae6b2e5c-60d2-3af4-9b87-745ec86b528c | -16.41977 | -57.40182 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f64297ca-2116-3e5d-91f6-1c3c64cbb56c | -16.41613 | -57.3959 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 0ff1ed61-638e-365b-a4b4-d4e6bf7d7e88 | -16.40889 | -57.39232 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cc143f52-56b8-3f07-9aff-e457075bba4d | -16.40796 | -57.39725 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 08512b66-e66e-3b1c-a73e-8208b205338d | -16.4079 | -57.38899 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 7e999bf7-4b8c-3cd2-b3f5-abcd9f5d2edb | -16.40429 | -57.39132 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9f877caa-87c9-34da-9239-9e8aaa4c509b | -16.4033 | -57.38801 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c9b9a0b4-f5c6-37a5-b17b-b34c3d960333 | -15.79195 | -57.33377 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3c4071d-73fd-32b1-b394-3ee9cd3a8e54 | -15.79111 | -57.33813 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f8cdcf2-dc25-3226-9a37-4227970f7fc8 | -15.79029 | -57.34235 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfa9db1d-2309-32c4-9abd-f69b1875993f | -15.7873 | -57.35776 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2e57a55-2d46-3328-87fc-4f73cfd4b0d5 | -15.78617 | -57.36364 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README128.md)
