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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97281a9e-1ec6-3b82-83bf-ec5b2edf7b4e | -16.70156 | -55.52593 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2fed8cff-a23b-33d0-82b1-876398a5bb85 | -16.70091 | -55.52985 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 908cbf2e-8cd2-377e-889d-895e74678a8d | -16.64831 | -55.91844 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ffdf3bbb-abca-3ec3-a4f7-a26749d2864e | -16.88094 | -55.91814 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 343795be-44be-3b04-8fb9-9f817877ca10 | -16.87933 | -55.84391 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 8225157e-1e3f-3eb1-9ae4-886115f4b84b | -16.87865 | -55.84789 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 630dca73-8b0e-3ce7-ac09-0659d2265cee | -16.87808 | -55.83971 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 39.1 |
| 7681f379-859d-3a51-a5e7-719aaac99a8e | -16.87331 | -55.92086 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| fdb013b4-b8fd-3ae1-aa15-d13531dd41e2 | -16.87116 | -55.83847 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 85d80d82-1b7f-3525-9240-e425e80d02af | -16.87053 | -55.91624 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 5e76ccef-9f43-387b-85c7-4e1982a719a9 | -16.86836 | -55.83387 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 47d8b1ca-a225-3a62-b637-725998d70463 | -16.86703 | -55.84181 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 544ed595-b3ef-3b2b-8fef-e47b48e36b93 | -16.86556 | -55.82928 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f470b3f1-2645-3e78-afcf-e8193b06d5b3 | -16.8649 | -55.83324 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1dafe6d4-91bc-3fbf-930f-bf9597fdb9f8 | -16.86358 | -55.91499 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 3bf68c75-92f8-3856-b375-1ba02f023e1d | -16.86357 | -55.84119 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3f86b222-5c05-32ce-927f-58e2d055144c | -16.8629 | -55.84516 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3f64c9f9-87c7-3cf9-9d4b-25ad9f5fba1d | -16.86197 | -55.91487 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e1c4d930-8248-371e-a6f8-d9aa853c4549 | -16.86184 | -55.89425 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 56eb9687-a879-3647-a951-4f84deb3d32b | -16.86143 | -55.83262 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 701201fa-3979-331f-b1df-0286ded9d861 | -16.8577 | -55.89761 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a757ab61-3afb-3383-8d20-232b498a5438 | -16.85517 | -55.8274 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 95a682df-6189-38e1-8dbe-34c5682c7207 | -16.85435 | -55.91762 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e393c47b-a15c-31ee-8b65-058d965dda52 | -16.85076 | -55.89635 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a9adbb4c-9abf-33d6-8d97-07402ab514fb | -16.84825 | -55.82614 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5d5084bd-6a4f-3e4c-b909-aab8093d7bb6 | -16.84595 | -55.90372 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8a2ae393-b2be-3724-b1b7-0ee9ba288ae2 | -16.84528 | -55.90772 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 87aee348-32cf-3120-be11-24400ebfa5b1 | -16.8446 | -55.91173 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4dc20a5c-522d-3d07-9e0f-1b9994fa5d74 | -16.84412 | -55.82948 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ab29bfc3-20c2-37c6-9d6f-b1387d495cba | -16.84247 | -55.90309 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ee69dd35-1b48-3ddd-a350-138c833e4cec | -16.8418 | -55.90709 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| def16806-bb1e-39cf-98da-91fec05b383d | -16.84169 | -55.88647 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 62c45f01-d3b8-3bd5-a61a-b316e4d2b825 | -16.84113 | -55.91109 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e958bbf8-af12-34be-a7f7-3882bae0b878 | -16.8392 | -55.81632 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d002fde2-06ef-3d2f-b683-4f7c9682d234 | -16.83833 | -55.90646 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2a531e0f-1a25-31c9-8ad3-43ad730ba6da | -16.83822 | -55.88585 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9c2f2d99-3872-3e8e-a611-d930448beba6 | -17.07735 | -56.38442 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 44e6d1b5-d918-3714-8d16-4d36de40c365 | -17.07523 | -56.37546 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2e93112e-57fd-374d-903a-30a874a1b24f | -17.07453 | -56.37962 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4aedb9f3-9e05-3607-8f30-995808d99052 | -17.07382 | -56.38377 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d244b1ae-8dbd-30d5-af5e-6b19460c5d98 | -17.07097 | -56.40041 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| af468244-7d70-3988-9e8d-d7d441948c1c | -17.06746 | -56.37832 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ddfd4d2b-2338-3420-a92c-13e577b2c419 | -17.06744 | -56.39977 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 24898b4d-52ca-3cad-82f9-3972d760f5f1 | -17.06675 | -56.38248 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| db36ce7a-f96a-3014-8923-80ff216ffe11 | -17.06604 | -56.38663 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4a70d66e-628f-3534-82f0-86a72adbafd9 | -17.06533 | -56.39079 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c76ddadd-86de-3bb0-93e6-b1f641c34a2d | -16.71879 | -55.96847 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1b147da7-baf1-3836-85ab-4e2f8a196c37 | -16.71531 | -55.96784 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e15467e6-eb85-3cc1-82c9-23d6850047f8 | -16.68592 | -55.92936 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fcd2bff2-83bf-3777-b5ab-707912fa4385 | -16.68455 | -55.93739 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1bc65fde-21f9-3a4e-990e-31f0d227713b | -16.68244 | -55.92873 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4965d19a-fdc4-347f-9cb5-930912fb4f06 | -16.68176 | -55.93275 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9dadf317-15d8-33ef-b07c-bcfbdc4cc7d7 | -16.68039 | -55.94078 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 3048bb00-674f-3633-93dd-fbe73e4ef534 | -16.67964 | -55.9241 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2624afae-26e7-35a8-954d-b8d9f1af4442 | -16.67896 | -55.9281 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0312e90a-c1a2-34c8-a03a-2598a40f552b | -16.67827 | -55.93212 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2ed8e9b6-0858-3603-a35c-d11fd57b7f25 | -16.67759 | -55.93613 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 12640e47-8fd8-39a6-939c-39d8e6b7b080 | -16.67691 | -55.94016 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 31fd1f3b-6ae5-3585-bf86-9f237c1e7da1 | -16.67411 | -55.9355 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 25ad5baa-2c97-354c-bc83-43d12be1c2c4 | -16.67342 | -55.93952 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1742b348-959d-371f-bbb4-87c0a78185b1 | -16.67199 | -55.92686 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cc6458e4-5d9d-3490-a4b8-8d2ecca30881 | -16.67131 | -55.93087 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fdc536b7-7b81-35a6-bbc5-582b9d802cff | -16.66994 | -55.93889 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 922036f4-8730-3dc5-9272-3bf0b04477cf | -16.66925 | -55.94291 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8a1dc49a-08b9-3874-a540-41b641385878 | -16.66857 | -55.94693 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 079a28f0-0d26-3822-b31b-ff64e22d2cee | -16.66503 | -55.9256 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ca3503c3-f766-3644-9732-70780b2f1486 | -16.66444 | -55.97109 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 23620818-40ba-31d4-b552-cda9d51ea9de | -16.66434 | -55.92962 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 27c7f17e-41d1-3570-be88-c499cbce3d82 | -16.66155 | -55.92497 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6228280b-50b3-3622-af36-099c15818aed | -16.66018 | -55.933 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f347cfaf-c262-34f3-b584-c4d54795fff2 | -16.65807 | -55.92434 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 22ee01a7-841f-3285-a093-7b24090c7316 | -16.65738 | -55.92836 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7af43035-b1a9-3ebb-a0cc-69ef4a005a69 | -16.65601 | -55.93638 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a75cfb8c-2d3c-3200-96be-a71df3f37983 | -16.65252 | -55.93575 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 34b47378-f73c-3b1a-83db-6ad525266505 | -16.65184 | -55.93977 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 58c3701f-5ef6-31ba-a51c-04bf0a07ec5c | -16.65179 | -55.91907 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2d1bfd28-ce42-3738-be87-c86b54ae8669 | -16.65111 | -55.92308 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3774c4cd-3b62-3b9f-8a02-0d956437cad5 | -16.64762 | -55.92245 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 22291470-2366-3ced-a4c5-4b2d7b4e5fd7 | -16.64694 | -55.92646 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2605bcba-fe17-3d28-952b-065acecb97fd | -16.64682 | -55.91901 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 59252eb5-364f-3fdc-ab5e-d07632f14435 | -16.64483 | -55.91782 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 98f224dc-704c-3fc1-ae6a-0b8d9fc82b4c | -16.6448 | -55.93107 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7f7ac4f8-2fbd-3255-93be-80e90467df59 | -16.64346 | -55.92583 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6b30822b-a430-3858-a326-ff8f43c0c307 | -16.64277 | -55.92984 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 77fd4cad-0be2-3c9b-ba00-9d77fcb9af2e | -16.64207 | -55.93387 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ac637e30-ecbe-337c-bff4-496ab990279f | -16.64199 | -55.92642 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e64f4bbc-78e7-3415-b087-96bb8931f428 | -16.64138 | -55.93789 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d5437bfc-6e01-3e92-b4c0-cbe0bccb2ee5 | -16.64132 | -55.93044 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 12a48dd2-5836-3cac-b5e2-677a157a95e8 | -16.63918 | -55.92177 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 43ad1ced-4fe8-33d6-8cc3-de043c48cef7 | -16.63582 | -55.94188 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 75d2aa9e-66b6-3302-8bc8-c982f7608798 | -16.63368 | -55.9332 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5186944b-ebbb-3b24-a6cc-3b251294b8f3 | -16.63155 | -55.92453 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| acb2bb50-3a11-30d0-8009-9c434fe1eb27 | -16.63087 | -55.92855 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 27064cee-5981-3150-9506-f6d5d3717bae | -16.6289 | -56.01045 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 42b47592-d036-3ca8-b552-a7212d397554 | -16.62885 | -55.94061 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5fd22193-1101-3e28-9b34-43244440948a | -16.62671 | -55.93194 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2da3fc17-c430-38ba-bf86-ee2fe78c906f | -16.61956 | -56.03888 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 27c9e8d6-239c-315b-a188-cd269c207b1e | -16.61907 | -55.9347 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f5f7a38a-b5d4-3584-9bb7-6e5425bbf315 | -16.61869 | -56.00115 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f5fd8101-58dd-3192-8cce-2d204391e7c6 | -16.61674 | -56.03419 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |


[Clique aqui para ver as próximas entradas](README107.md)
