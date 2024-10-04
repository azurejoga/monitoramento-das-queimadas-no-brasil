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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed98621f-5d37-3635-a75b-349dafeac1e2 | -15.26548 | -47.50096 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cae1de6c-2edc-36ee-a298-e495b5e5bc2c | -15.26198 | -47.50053 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4e4802b-0f4d-3924-97ef-4c78a142b3bd | -15.2585 | -47.49998 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f82a7c0-9ade-37a1-a656-2027837650f8 | -15.25714 | -47.50091 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4245b84b-578a-3728-96f4-08cae80d2e50 | -15.25366 | -47.50037 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c0a4424-96a3-303b-bea5-cf629f1d19e1 | -15.25084 | -47.49543 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7496b695-d1d0-38a1-9a1c-85155a6e2f3b | -15.25017 | -47.49986 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ffbb6a2-4b60-35b5-9ad1-faefdae9668f | -15.24735 | -47.49495 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f11acbe-961f-36a3-8cca-24b0f632016f | -15.24321 | -47.49877 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b8b375e-d1b9-3276-a8b2-6c786f5062ed | -15.23974 | -47.49818 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be226775-275f-3fd7-9c64-37231d180125 | -15.23627 | -47.49753 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4ef92aa-74dd-3d49-8f3a-bc38df28defd | -15.22463 | -47.50397 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 047871f6-788e-3fea-a0f9-6e058262c698 | -15.22118 | -47.5032 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 988de116-f2e9-3357-9868-da4feb4fc941 | -15.21709 | -47.50679 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4102a9a-6725-34b2-84d7-34e5faa152f0 | -15.21646 | -47.5111 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fcd5c04c-119c-38ad-ae2a-f0155f686fdc | -16.69997 | -48.6342 | 2024-10-04 04:34:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a38b2eb7-0e6e-3410-a283-b53f5b4044bb | -16.69098 | -47.82779 | 2024-10-04 04:34:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 14b3cc69-d74a-32d3-8aa5-59d7821ddcad | -16.68749 | -47.82728 | 2024-10-04 04:34:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ac8624a3-7fef-3480-82ca-1604b9acd9a1 | -14.53117 | -49.28992 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68aa436f-6a51-3cea-8b6b-3c549f18da46 | -14.5284 | -49.2858 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f460bbc3-e657-3cc9-b6b1-97104cd4c82b | -13.214 | -48.65326 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1257305-df93-3627-a4d0-6762a2cec3e2 | -14.52507 | -49.28527 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f03bf361-7182-3e97-9e2b-4767d0314d71 | -12.12098 | -48.43949 | 2024-10-04 04:34:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4d35712-f2b4-3ff8-9bc1-195f644f14f7 | -11.90372 | -48.31366 | 2024-10-04 04:34:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32386e58-7f43-381c-bada-eb0346c4f36b | -11.90317 | -48.31721 | 2024-10-04 04:34:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c74017c-fab3-3cbb-82f7-6dee7f27aacb | -11.90038 | -48.31313 | 2024-10-04 04:34:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91806b38-11ee-33fa-ae1f-df70382cf00b | -11.68691 | -47.81314 | 2024-10-04 04:34:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7cdb9d9-288b-38fb-bc00-5d71fd0241b8 | -11.67344 | -47.81104 | 2024-10-04 04:34:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c3478fb-c65d-33ea-a19d-8fcffe833924 | -11.66897 | -47.81775 | 2024-10-04 04:34:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 693cb0d0-63ea-3afd-87d2-c56ae29373ac | -11.25769 | -48.84115 | 2024-10-04 04:34:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0a1b4fe-039f-38d1-8944-65e40877a8c4 | -11.25436 | -48.84062 | 2024-10-04 04:34:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec3557e7-fd72-37a5-9e2b-74a86d6bdb69 | -12.48903 | -48.01908 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 897b81bc-03af-3cde-8056-00749ccfed52 | -13.51754 | -48.60986 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4ff0cbb-150a-38e4-b1a3-737df004f1e7 | -13.51699 | -48.61345 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b68bd5c-88f5-304c-96d2-cddf4b8c2d97 | -13.51475 | -48.60571 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f2c6ee5-45ae-3fb6-b5bc-fd1150b1f9f1 | -13.51365 | -48.61289 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b58a71cb-0579-3baf-a44c-6bf1e4f1704b | -13.51253 | -48.62011 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb07b737-bebc-3358-b6bf-649845bfae3f | -13.51141 | -48.60516 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbc30b14-a077-309b-ac59-24b1b53afb85 | -13.50919 | -48.61955 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dfe490a-e88d-3bdf-898a-55bb6d544cd8 | -13.5031 | -48.63687 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b25270a-d114-3335-8485-728341c9ef49 | -13.49975 | -48.63634 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 494182d8-1a94-369b-92e0-50b24e17f29c | -13.4992 | -48.6399 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 588745f3-25da-3379-8546-3c62d1a6cc63 | -13.23457 | -48.63096 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7f3045b-db54-3399-ad54-83f3f2e4fad9 | -13.23291 | -48.64167 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94519156-b5b4-361a-8d12-191db1a89437 | -13.23236 | -48.64524 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d6bd66e-6e28-359d-aaad-6fa11b6879db | -13.23012 | -48.63755 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8833ecb1-618d-3de2-9508-e30e32526d9c | -13.22902 | -48.64471 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e030e683-7839-38ad-9d48-a358d95e17f6 | -13.22678 | -48.63703 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c60d472-bb2f-37cf-a352-92d2f2f14636 | -13.22567 | -48.64417 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54c16adc-0a12-3cdb-b966-6d27ad80bcac | -13.22344 | -48.63651 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c1a0b4e-277d-3bbf-9526-253c555d965b | -13.22233 | -48.64364 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c80518b-0364-3c75-a0e0-a2dabb85738c | -13.22178 | -48.6472 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a92f75d-bb7c-34d3-8098-42a02a336c0a | -13.21844 | -48.64667 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8da5560-3deb-32bc-8360-69696cd7c0f5 | -13.21789 | -48.65023 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9db6226-4bbd-3c7d-80f9-ce5a72942c3d | -13.21066 | -48.65273 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 131aad03-892c-3868-98e3-273a2206853e | -13.20787 | -48.64864 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4769f3d9-c977-3eea-82b8-a00951f81208 | -13.2077 | -48.51669 | 2024-10-04 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b061b2cc-725d-38a9-88e5-2ff3a282283f | -13.20659 | -48.5239 | 2024-10-04 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d62cc84-b6e0-329a-b2d0-0a88c32b4126 | -13.20324 | -48.52338 | 2024-10-04 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8376ceae-8ea6-3393-a644-172ef943baf7 | -13.19398 | -48.67204 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2b0a2f6-8302-337a-905c-62f5a904bad6 | -13.19287 | -48.67918 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe95f739-84bf-3467-8dc3-ab75b95093ce | -13.19064 | -48.67151 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25596986-67c1-3d8c-be02-18f543cbe927 | -13.18953 | -48.67866 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cbd9ca2-a5ea-3b45-af00-8ca040c75335 | -13.18674 | -48.67456 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0cd82a8-09f8-3b03-8894-269de8685061 | -13.18619 | -48.67814 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03d95147-e9e4-3ecf-b8b7-2b702fdbb28d | -13.18564 | -48.68171 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a84e35ac-fff8-3560-9cfd-90d97adfee74 | -13.1839 | -48.62653 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aff43c38-0179-3ced-9b13-19f11c84d81b | -13.1834 | -48.67405 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b9c4c14-c663-3740-b0bf-c74eebc1645e | -13.18285 | -48.67763 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8caf706d-4e74-3de0-a893-02899f75c7a0 | -13.1823 | -48.6812 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f4b11c8-dd3c-3b05-960b-a9fd1abfc8ba | -13.18175 | -48.68476 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e708aeb-604a-3289-a4a2-17850869b1a7 | -13.18061 | -48.66996 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d34dda3-ce05-3217-9f34-298ec4a7b745 | -13.18056 | -48.626 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54eec65c-5444-3e8b-b8c8-58c8fc8de048 | -13.18006 | -48.67354 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 588da265-ec65-3e94-b72e-5dd25cc20f4f | -13.18001 | -48.62959 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fb539272-0454-3a75-8ab2-a9597bb38da8 | -13.17786 | -48.68779 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6cf1256c-3b6b-3a27-89d2-3319d5c6e0f5 | -13.17728 | -48.66943 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f5988d7-9323-36b5-8e84-be74cc536431 | -13.17723 | -48.62545 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57ce4e38-18bc-359c-8aeb-b842312a1d8c | -13.17672 | -48.67302 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f19937ae-4fb3-3462-aac2-510f31f4da6c | -13.17667 | -48.62905 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4d84acc2-5101-322f-a0a7-e25c765accd8 | -13.17617 | -48.67658 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65e60ad7-4d47-3937-a56a-1f34f4653138 | -13.17452 | -48.68725 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 303cd9ff-a1a5-3f23-a008-1f2b506f9c06 | -13.17338 | -48.67249 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 36da6bf3-118f-3d8f-8157-589e2ef61562 | -13.17334 | -48.62849 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ade39cf-36aa-35b4-aab1-d2b1251751bf | -13.17283 | -48.67605 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47c92573-427e-3272-b059-9472aca5c8a4 | -13.17278 | -48.63207 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79eb9f42-51f4-3661-b340-27a0df3f8fd7 | -13.17168 | -48.63921 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb340c56-54ff-3e8e-9b57-c062b68d39c6 | -13.17113 | -48.64277 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce8de7a9-06c9-3625-bab6-8dae3c057757 | -13.17055 | -48.62434 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c12c3e1-f961-3ee8-872c-90bfce7f0067 | -13.17 | -48.62793 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a950096-3c5e-3146-912b-c383b55c6937 | -13.16949 | -48.67551 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71fd2377-4136-3554-929f-479809ab8fc0 | -13.16945 | -48.63152 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 58855525-0850-3733-9b73-9f06de24878f | -13.16889 | -48.63509 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| beb78a7b-d94e-3aa1-b5f2-3fb412f385dd | -13.16834 | -48.63866 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9a89318-39bf-3cd9-9d02-a0fe7e2eca33 | -13.16832 | -48.61662 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e40af42-c2e9-3642-bac0-119938731627 | -13.16782 | -48.6642 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14199475-f3c4-3a01-9fe6-8b40f12b1898 | -13.16779 | -48.64222 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc89ea5c-56ce-391e-816f-1e871cfe5723 | -13.16666 | -48.62738 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 839014be-d11c-3fab-a8f2-7b54264c747b | -13.16616 | -48.67496 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bd52840d-fc5f-3474-8c59-10a2f277798e | -13.16611 | -48.63096 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README120.md)
