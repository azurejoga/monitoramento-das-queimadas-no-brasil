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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80670c7a-9d5b-32f1-b0b0-694ec1feabce | -13.99615 | -53.7072 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1f8a397-e106-3bda-9fff-183a6a6a621f | -6.85881 | -59.4607 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f5863b57-6388-3f2c-9e47-144648e58b69 | -6.77158 | -58.65839 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ce5a75d-94ec-3c1e-8b27-ee7905f39f45 | -4.52649 | -54.86259 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdc3e922-07ee-37b6-8434-894b9c625c20 | -13.9989 | -53.67505 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8bded08-279f-3a9f-a3f3-02349fb206da | -7.10525 | -59.76983 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9884a221-1737-36ca-b85e-7dcbbf9282be | -8.52815 | -54.80674 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3be3dbd0-6f34-30d3-b55e-48e71bd05a1d | -8.0297 | -54.01751 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9722b770-4a8f-3b6c-aacd-88d0cd6d22b9 | -7.05609 | -56.50861 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 040184c6-65f4-3e08-97fd-68f9e0c08be6 | -6.76566 | -59.14771 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12d2f3c4-9252-3c07-ac65-3bb50ad26350 | -5.99713 | -57.81409 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 04715677-7892-3381-8e1f-fe9ebd8cb38d | -14.40356 | -54.05208 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 96dd377e-e8b5-3207-908d-338a51f177d0 | -6.36857 | -62.90256 | 2026-08-22 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b5de0b2-f2ab-3c57-beae-37206d2e5ee5 | -6.6635 | -56.33376 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27124907-db1e-3a2c-8c28-99026b154022 | -6.727 | -48.11711 | 2026-08-22 05:23:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30ec6e70-76be-3e64-8d9d-00908d79b7b9 | -6.80005 | -58.62717 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a87b2a1-8a5a-3cf2-a893-61fa3cdbec2e | -6.89142 | -59.44818 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c68aea64-cf36-3077-a71a-eff4cb2e7ebd | -6.75444 | -58.65927 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f96420f-6bf8-3d6b-b4c1-c8fda175231c | -7.54925 | -61.17709 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e82e176-c329-3fe3-87b6-c9195057d035 | -8.53228 | -54.83378 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 43912ee1-a89a-386e-a07b-a4f0d5ccea8f | -13.98379 | -53.68269 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e5c9dfb8-e7e9-3308-b323-47f155a57440 | -14.11739 | -58.83457 | 2026-08-22 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6ee3138-085a-3739-b7da-e266417a1b50 | -6.12379 | -59.91695 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecd53609-b139-389f-9619-029c1e7f9d3a | -11.15869 | -54.01967 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2a1cfec-da8b-38ae-996f-0de5b531e542 | -6.74948 | -58.66919 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b4bb6a07-3130-3125-9787-ad1baf87b73b | -6.80916 | -59.41023 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3009dc7a-e9fc-3d72-a18e-9b63829f8660 | -6.10544 | -59.94637 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9020a671-a4f1-3337-8af7-5e757d12eb45 | -6.88597 | -56.43999 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a9e21f7-9e7b-3f1e-9b38-4fc3b5116530 | -8.59733 | -54.71002 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaced970-ea3b-3c97-b2fd-f92d6e7ad748 | -7.53568 | -57.65239 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b54a734-b4ec-34d6-a5ed-45237f8efc45 | -6.78153 | -58.65995 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ffc7c4c-2d70-3aa5-b052-502081fd1542 | -6.5693 | -58.97157 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92c1ef64-e49d-3faa-ad93-a8b3539742f4 | -6.81245 | -59.38947 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3d07a8ad-fc83-33a3-9fc4-678096e367b6 | -6.15526 | -53.70522 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 954b29a6-8053-386d-bb3a-1fb076636c15 | -8.02644 | -54.02415 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35f791f6-4adc-3220-9c21-3967cadbf705 | -6.85214 | -58.96665 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 474d577e-68f8-3f9e-833b-f7f1a520fd89 | -4.4657 | -54.95944 | 2026-08-22 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ea3f53d-95cb-3b21-977e-3f29ce4a4170 | -6.79759 | -59.41903 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| fdde6caf-c307-3579-a87e-ea2051a405b3 | -7.34649 | -55.66618 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dba95d76-2f26-39a3-aea0-295fba96189d | -5.80105 | -57.5452 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bcde0290-f184-3401-90cc-8272abf2d66d | -6.78381 | -59.44168 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef137aac-91eb-3521-9b44-14ff7048fb76 | -6.48601 | -51.60516 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94e55464-73f5-34b6-beaa-f3cf33c5102f | -13.82743 | -53.99288 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 841b2ef5-2808-3c26-8367-b92f44641a0e | -6.76107 | -58.66032 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 72705f3a-a4bf-3554-91d0-660b80683463 | -13.45619 | -51.76783 | 2026-08-22 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b5144ab-e0c3-3279-846e-1eb04b8074ed | -8.55296 | -54.85827 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59a72305-1980-3012-91f8-97c47cfa7397 | -6.54101 | -58.52616 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ef1e453d-ce43-32da-a620-bf037c6da061 | -8.14984 | -46.71981 | 2026-08-22 05:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 579c954d-5f2b-3fea-ad76-499c112bd1e6 | -7.34584 | -55.6706 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ab4a566-1043-3fce-9e32-106393a6aeb8 | -6.95029 | -59.31211 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0b05076-7295-381a-9ea4-c81e19fbcb68 | -7.37515 | -59.95277 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b65b9da6-668f-3416-8817-5bf7e2829f05 | -6.76165 | -58.67824 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e8993ea-bb4f-3054-9c40-14c4824a7a2c | -6.22014 | -55.48585 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7999aff8-9e42-3f3c-8cf8-f9e29427cd6b | -7.60385 | -60.94583 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd7db377-66f5-3872-a254-a95ab8856754 | -6.84337 | -59.45114 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55d01a90-11c5-3eed-a29c-aece5c551dce | -7.34332 | -55.6987 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 602e25c3-fa29-361c-8b0b-0558571ae2d3 | -12.72296 | -48.41777 | 2026-08-22 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 438ad232-701d-3b41-8985-c86d5de6001f | -6.69361 | -58.93771 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24febd23-889b-3dd4-b891-5428a00f6704 | -6.2574 | -55.41475 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b47efa2e-5c25-39f1-a5ff-e73487cd76b7 | -6.76217 | -58.65334 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89bbd0d2-3e35-342c-953e-6a6b391e4afb | -6.79594 | -59.42941 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| be597339-7960-3eed-959d-d5475c5d05df | -6.85218 | -59.43835 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa1edf87-958d-3d8a-bbd4-03379bb46f84 | -7.00141 | -59.59023 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f1dd9be-080d-3b7c-bad0-90cb099356ec | -6.7896 | -58.65049 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3011bde-8b20-39f5-afda-968ef1ae4fe9 | -6.6723 | -59.07267 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fac2dfc-3222-3e0c-8cc1-9977ed47e9f3 | -6.96043 | -59.05479 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c3d0cef4-336a-3792-9622-71ec0857601f | -12.71734 | -48.41811 | 2026-08-22 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58c2b57c-a95c-3b6d-8907-0653857dc862 | -6.81799 | -59.41872 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89253033-4f86-3d64-ae80-b8b6a4fdb49f | -8.53496 | -55.33397 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d091d4b7-1cde-3741-92a1-376734ec789b | -7.17867 | -60.64848 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4553185c-3e3e-3cd1-a081-3dff6ecd030b | -12.72377 | -48.41888 | 2026-08-22 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f50cb78e-4825-3e8e-a11c-30f5fbf99dc3 | -6.77105 | -58.68328 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ae27e8d-9d3b-3616-975f-c809b92fe7b9 | -3.15163 | -51.09575 | 2026-08-22 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6925bd62-2fe4-3e86-8f8b-9bfebbd05aea | -6.86825 | -59.03664 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1769187c-85a9-31d9-9b18-4fe41ff859b3 | -5.99997 | -57.8619 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57e6dce0-06e8-3b66-9df1-39ba067046d5 | -6.91726 | -59.34942 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 133f2b37-008d-3514-9514-40c313225fae | -8.53381 | -54.82345 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e580fa41-e19f-3180-85c8-be33f25e49c3 | -6.99755 | -59.59317 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 687b5ce5-a3ff-3e30-a902-2fa086a9b81b | -6.81521 | -59.39345 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d92cc4da-c48a-378d-9579-15c19fb51409 | -11.16304 | -54.02032 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e335c5eb-d7a7-3995-9ede-b55ed2160473 | -11.20564 | -55.04832 | 2026-08-22 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8334d178-abfa-3ec2-ad7d-a561ac12b54a | -6.87148 | -59.44497 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79e32bef-417c-30aa-a0b4-4ef4aa92298c | -13.92907 | -58.25985 | 2026-08-22 05:23:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f171b1f-aa60-3c72-a2a4-2978b556dd89 | -13.93259 | -58.2604 | 2026-08-22 05:23:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10a8f490-e235-3be1-9aa8-e20531753dd5 | -6.6073 | -58.38614 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e104743-360a-3b4e-9435-540cab5346c3 | -7.01408 | -59.55323 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 566ddac7-a006-3eaa-8089-eba7493297c4 | -14.00697 | -53.68599 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96968e67-59ba-38cd-b9b0-a1139a15e00b | -8.03058 | -54.02484 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5fb6e69f-93d0-3d63-ae0a-34d7443e0e40 | -7.55606 | -61.1782 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a667d47-1447-3958-abf5-4294b8ade745 | -7.61116 | -60.97317 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f67dc3e-316c-3175-b730-309d51c08c0a | -6.86487 | -59.44392 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b430ad1-d20a-38be-913d-0f0c12b9e793 | -8.52867 | -55.32323 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6030aa8b-9bd9-3d21-a338-efbe89189eb2 | -6.8053 | -59.41316 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d51577e-1e2f-331e-aeae-bd127dcb68c2 | -8.99205 | -50.73365 | 2026-08-22 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd9ea6bf-8039-3ab3-86b6-c02dce848674 | -13.42112 | -57.07956 | 2026-08-22 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43f16f09-5ee5-3faa-b933-981c40d53db3 | -6.95414 | -59.30918 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4e7b661-feba-3962-9f93-81518fa4b69a | -13.98482 | -53.68585 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07921e26-9fc1-3676-b439-03f332eb342f | -6.66898 | -58.74914 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e982aa4-c0ca-3d50-880c-16be1b2bc9e1 | -6.87479 | -59.44549 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7759c323-a3c7-3c60-9ccf-9ed71dbf82dc | -5.69448 | -60.23948 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README68.md)
