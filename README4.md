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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e75dc44-7406-3c26-b719-82452eeeb3e7 | -9.51221 | -60.49541 | 2026-08-23 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| edb66f55-9044-3c53-9a9b-51e5b67207cc | -9.53314 | -63.56148 | 2026-08-23 01:07:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d4ff8a7f-8477-3dec-87b2-01c02bf56c3c | -10.06632 | -60.50105 | 2026-08-23 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| cc545c81-1c12-3040-b75d-5264d9b4afec | -7.07442 | -59.98081 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 654a44e3-c1d3-30df-9a8b-f361ceb1f2d0 | -6.89084 | -59.0292 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| bf1fc8bf-8129-39d6-bfec-3cc1c8281c84 | -6.7807 | -59.75095 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 305a18ea-466f-33a1-b74f-8ef2076ed085 | -8.71065 | -62.8996 | 2026-08-23 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 06e6fc4a-04e6-3563-80d9-0cfc6049a194 | -6.66395 | -58.75247 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b53caba0-fb58-3ead-aabb-5ef755f4323d | -6.79512 | -62.90531 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 8183201e-8ed7-38b6-9682-98b4ee26bb12 | -7.61259 | -60.97056 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ccb33f51-e34b-398d-b953-c1a63d0e8e14 | -6.60737 | -58.39046 | 2026-08-23 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 0a797070-7c15-32ee-b32e-d33ac84a8db6 | -6.66055 | -58.73062 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 354adec7-707d-3173-9cab-5127d64003a8 | -6.94728 | -59.05597 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 9e156ed4-cbca-3a99-ae97-a8ce7c9cbe94 | -6.77484 | -59.73872 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ba2a9ecd-10ee-3449-a508-1b5f20ec5028 | -9.13658 | -65.95492 | 2026-08-23 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 978e2743-f6ff-3973-bec3-de62e6fde793 | -6.79601 | -58.65749 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c2a6cef4-6c97-3eaa-b22f-f60d7be32383 | -5.76091 | -57.57743 | 2026-08-23 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 70df5091-ea80-38f2-beb1-9aac1c820598 | -6.97635 | -59.07226 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 23668827-f099-344d-b07b-d0f00e41f847 | -6.81771 | -58.64829 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 59d561f7-6cf7-35e5-9bbf-3d934e8cc64a | -6.83328 | -59.96582 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| f0f68680-3696-37db-93cb-940d2c362d53 | -7.61465 | -60.9846 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b64bf556-31e5-3b77-9ff5-9bee31a1f31c | -9.07985 | -65.40852 | 2026-08-23 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d9f9c229-77b0-3b25-9b3d-accd7b51325f | -7.68624 | -63.3424 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 61c2cb64-eb39-302c-bec0-4973910ab60a | -6.80622 | -59.67184 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| a9b1b185-b164-395e-bbb1-0725851020a1 | -6.96023 | -59.05396 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 8f1eecb7-499b-31ff-892d-62d0399ae228 | -6.77868 | -59.65729 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 74a01fe3-cf4f-30fb-b4c2-b82c52085104 | -6.80611 | -58.63337 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| d0520789-4acb-34bd-8ced-33a58575c2c3 | -7.78156 | -61.42413 | 2026-08-23 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0a75a7e2-e2c7-3ddb-b0c3-205e6b645028 | -6.96496 | -59.08038 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e7e5b377-29af-338f-9643-5c07727687bc | -6.93912 | -59.08443 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 46ff99af-3fa5-3905-9afd-f2919f86dc4c | -6.77169 | -59.44747 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 00a41e55-4136-3229-8e0c-0269fd89fd51 | -6.71268 | -58.73828 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 06322900-7b7c-3188-b416-bcbf8d90b58b | -7.97952 | -63.66121 | 2026-08-23 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cd2c293d-2998-3d24-8458-cab7a10aac10 | -6.88277 | -59.40375 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a2f94727-2398-31ca-ad4d-66f14ac30b56 | -7.55177 | -61.18475 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| c9f0e139-01c7-3f9d-909a-4e408df863a8 | -6.9505 | -59.07624 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 55cbbd51-36c2-3f75-9617-555d60084d59 | -7.56963 | -61.20404 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d02649b8-3a62-3a19-b91c-d32473d14bfd | -7.6676 | -63.34515 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e85432c3-9524-3907-85eb-ec568c99e6e6 | -6.79388 | -59.67375 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 09e635cb-62a1-3c33-94f4-ae9b9d8a40cc | -6.65747 | -58.79824 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8809fe6f-cadc-3a01-af35-d18e17a296d6 | -7.55678 | -61.19202 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 78390c72-6726-3ac1-a4d6-29e6d26bc1d5 | -6.7909 | -58.65258 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8fd18945-fc3b-319b-ac9f-f61afdde55dc | -7.4364 | -59.77533 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 905025e5-74de-330d-8254-bc198cfe4c6b | -7.56756 | -61.1904 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| e71d971d-8009-3d82-ac6f-b63dbd356081 | -6.86697 | -59.03885 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 039ca979-443d-3dd7-9fb5-af744c1b4cd5 | -6.97952 | -59.09249 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 38407f64-d289-3f1c-879e-edf44cb232bf | -7.61626 | -60.97803 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ec26e608-2019-359b-b931-31a63ba24313 | -6.70061 | -58.72424 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 7f0a03f1-88e8-3b8a-80dc-8d77206c5fe9 | -8.56642 | -63.18156 | 2026-08-23 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 29.1 |
| d8c56586-2c5f-312c-814c-ed5c5a7cadad | -6.83087 | -59.66777 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 94caf5a8-9a6a-37a8-b548-b4d61b1386ce | -8.55711 | -63.18294 | 2026-08-23 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 58237734-3939-3ea8-be6b-ecd090a65bf5 | -7.65685 | -63.33653 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e764dd8d-9ecf-348b-bb49-2c68db141f75 | -6.11106 | -59.94007 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| dac594a9-9725-3e59-ad59-b349c4211aa9 | -6.80429 | -58.65033 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 152.0 |
| d3380b11-4fbc-3417-ba67-e52732e952e5 | -7.5547 | -61.1784 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| e3d4a11e-c5ea-3e27-b6f9-0447db5b878d | -8.69827 | -62.88044 | 2026-08-23 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2fc79d67-142d-37ca-b81a-e10d21647342 | -6.81855 | -59.66983 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 11556fee-0320-3d67-88be-e219aa3aff5c | -8.25821 | -62.89246 | 2026-08-23 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9f8e82d5-d9b0-3a21-a6ed-94a72f0e8c5e | -6.80942 | -58.65537 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 002721af-1097-30f8-bffb-772ddbaab834 | -6.79104 | -59.65538 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 38636260-27bc-3b0b-b405-c25705fc1b21 | -6.1267 | -57.85719 | 2026-08-23 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| faca51eb-8aaf-328d-a80f-fc8596bf82e3 | -6.86057 | -59.42707 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 429850d0-a85c-3bfd-acaa-481aef310a52 | -6.75923 | -58.68605 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 26431503-3262-3cb7-bd85-c1f8bacf7c0f | -7.59522 | -61.22783 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 07ac3942-9f3f-350f-9861-624fc4328772 | -7.67692 | -63.34377 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 56df6f1d-2471-31ef-80e8-e491f2c837d5 | -6.82595 | -59.96149 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| bd46ce5f-b097-3e45-b9ab-6cdc26840fc1 | -7.56454 | -61.19675 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 2d314f07-dea2-3a36-83cc-fca68a4924bd | -7.97816 | -63.6516 | 2026-08-23 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9f792e0a-50f1-359b-bede-29eb0958ca3b | -7.86574 | -63.77173 | 2026-08-23 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a8c36362-50ef-345f-a75e-302d5961be69 | -6.83798 | -59.9595 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| df8402ea-4e00-348a-812f-b5c3d379eb85 | -6.69061 | -58.74818 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| e57a2b44-96a4-37c8-82f4-e893756e6255 | -6.94899 | -59.06215 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 8f35b28f-3139-34fa-8bd0-f734edbf0ca4 | -6.77624 | -59.6633 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 401a4226-5366-3fb6-9dff-9d547cc87041 | -7.44061 | -59.76806 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8cbce35f-f4cc-3a99-8506-9255a23a4014 | -6.12504 | -57.86302 | 2026-08-23 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 6f69e019-1cc6-3b89-bf28-1512a4c577f7 | -6.96193 | -59.06012 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 4546982f-c245-32e7-a2a9-4f5a6c5900df | -8.565 | -63.17157 | 2026-08-23 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a71fc928-2b85-359c-a7a1-7139a44f4f4f | -9.05073 | -65.45784 | 2026-08-23 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c8712a34-5d4d-387f-b0a2-c8ffe46f8f41 | -6.97316 | -59.05187 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 72a5ef71-78e3-3373-9abd-6d4e17cdff42 | -6.79664 | -62.91608 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| ad61758c-efe1-378d-a480-1b255ab78c42 | -6.83075 | -59.94855 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6fef45d3-7c7b-324e-9644-729407450974 | -6.55048 | -58.52423 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| e4890703-f205-3ba6-8b17-cd50dbbdde98 | -7.59746 | -60.94384 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| de50321b-8e3a-3e83-a131-2e48cd6fb137 | -7.68484 | -63.3324 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 6348f788-d95f-3a84-a15c-2379b5020329 | -6.8576 | -59.40786 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 601e8c5b-9fae-3187-b75e-50b06c412898 | -6.70917 | -58.71629 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| be08339c-d408-3134-bf7c-667c03e4ea48 | -6.7558 | -58.66395 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 0164ac18-e3dd-3b57-aa16-ef9af56c0b1d | -6.68724 | -58.72627 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4c80741a-4613-35f2-a948-7bbff1520a74 | -6.6617 | -58.80325 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7d463304-c027-36e8-9e07-60a7eae85e59 | -6.79918 | -62.90939 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| b9819ad0-64fc-3058-a2c3-2a1ad660580f | -7.65828 | -63.34653 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6fb27c89-1f88-3d1d-ac08-9f9b2cc0d64e | -6.95204 | -59.08241 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 125aba6e-571f-39ea-9016-bdb8a1fc23f8 | -6.8649 | -59.03343 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 27f5e01f-17f0-35e3-b4e8-9875f347ccb4 | -6.70395 | -58.74616 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| b4f9f5dd-8df2-3f85-a787-4ec163493017 | -8.70122 | -62.901 | 2026-08-23 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 080c14b6-4d8a-39d9-9c8e-73af11ff9d57 | -9.14544 | -65.95367 | 2026-08-23 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 93b84ca5-7425-3eef-9e6a-114889840d51 | -8.40501 | -62.69738 | 2026-08-23 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9041625b-a7eb-3613-889b-a05c8f98f5d0 | -7.43902 | -59.793 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 7a65ee72-72fd-341f-9cfd-10e6c1bdb455 | -6.7886 | -59.6614 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 7a7c3290-c84b-3e1a-9647-a8d3ec5403a2 | -7.67833 | -63.35376 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |


[Clique aqui para ver as próximas entradas](README5.md)
