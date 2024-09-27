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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4711427c-e591-3473-b46e-60da9563fe83 | -8.50541 | -63.50543 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53246762-3c1e-3d8c-8799-3a1a605a88ca | -8.50484 | -63.50899 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b313ed1-c700-3649-b269-efdd3acc891e | -8.50428 | -63.51254 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1fd37a14-b494-3f71-bf29-1bbc821ed792 | -8.50037 | -63.51556 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e5fc6d62-4933-3815-991b-1df4b27ec631 | -8.49703 | -63.51502 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c051f455-2448-34ce-873d-5561adc9091c | -8.49275 | -62.556 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccf1b752-e32d-3d58-88df-2269898b62ef | -8.47303 | -62.65968 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50962ada-195d-3b4d-93a0-6a33497d8354 | -8.47081 | -62.65221 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b38d45c1-e497-3ea6-8bb7-7c0415e801c0 | -8.46751 | -62.65168 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01b68782-1e5d-3405-903e-0ec253a6180f | -8.46696 | -62.65516 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66052594-6a85-37da-9908-83fb4daf5371 | -8.46365 | -62.65463 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c84ef810-b1de-313b-8a31-e1dc008964cf | -8.46224 | -63.41124 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa0d4267-80a2-307e-9021-ab3db36085c2 | -8.46032 | -62.63274 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad73a51f-6bfc-308e-a108-79b8e32ce2af | -8.45891 | -63.4107 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3735e8d0-f703-37cd-97c6-4f10a813f975 | -8.45834 | -63.41423 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e7364f7-4634-366d-aae5-91525484766c | -8.4477 | -63.43793 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cf28953-31e6-3f82-9ffd-763d674927f3 | -8.44713 | -63.44148 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69f2162f-824a-393f-932d-9aa1cf67ea77 | -8.44436 | -63.4374 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cc8b141-c1f4-3235-83f2-d58517516074 | -8.44185 | -64.03381 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c968c7be-ac4d-3128-b6c1-6e3d5f13c1eb | -8.44127 | -64.03745 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c027bdc1-0c46-3067-8ee9-11748ceb4b42 | -8.43847 | -64.03325 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af628290-8987-3d1f-90d4-c6456ead91ea | -8.43789 | -64.0369 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a802f30b-91ea-3011-8e84-c4a67a00c038 | -8.4317 | -64.03215 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e0df4e-feb8-302a-bdb3-98f6f32ac05f | -8.40967 | -63.4029 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fb0db06b-8b67-3215-85c1-ed13a8c4d3ca | -8.40633 | -63.40237 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 836eac22-36d9-3fbd-a827-a957ae9eb2e8 | -8.40577 | -63.40591 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 387488e1-99bc-3253-8b47-8a5ff0c37cb6 | -8.4052 | -63.40945 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74a7de3a-ee67-3c14-8f53-5b77efcb19da | -8.37193 | -62.65393 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5cc55e5b-4e2c-3495-947b-b0c0a45c88d9 | -8.36863 | -62.65341 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c62be06-96df-305f-9fef-796094777a34 | -8.36532 | -62.65288 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a0043c2-4ae0-3732-bc68-d77bc4def506 | -8.36477 | -62.65636 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbbcff9b-f06a-3d4f-954c-f586ed3a6687 | -8.34395 | -63.42863 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09023888-60ea-30f1-9af9-462332ba02fb | -8.31631 | -62.85547 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ea3c587-5c97-33ba-9244-60a233bb7340 | -8.31575 | -62.85896 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2f50152-c805-39f2-a55c-eb7c9f9ac74d | -8.31299 | -62.85494 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48119229-a7a2-3d0e-b44f-e66fdb82a886 | -8.27874 | -63.76959 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b8b5d80b-e093-3144-af43-9fbd5a718503 | -6.93237 | -64.24006 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc6ad512-7c3b-3325-9749-b8399179bfbd | -6.92892 | -64.23951 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fafb30a-4e23-3b2f-8cdb-39986bab2937 | -6.83472 | -64.30241 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 953adc59-432f-3fff-827b-48efda105d0a | -6.82818 | -64.32092 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a57f2ebe-2d30-39b7-918c-48d34d004ed8 | -6.82757 | -64.32474 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64e6c3c6-40f3-3c97-bc79-2e42bed30d80 | -6.82472 | -64.32036 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d722147-f4bb-31cd-a103-c94e09e037b1 | -6.82411 | -64.32417 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a05a4b5a-c257-3892-96c2-9b0750bf7f84 | -6.82126 | -64.31979 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11b18421-aebc-3fd0-856e-07abe2351aa9 | -6.82064 | -64.32361 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6232a19e-838f-3d9b-8e4e-01f9a4d480d8 | -6.8178 | -64.31923 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 047ea009-7493-33fd-8681-dde10a83998b | -6.745 | -64.33949 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ca84118-931e-37ad-b81f-ff3ffc6479c1 | -6.70886 | -64.36507 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97e422e8-2ea5-3f49-b771-20cd1b6c9067 | -6.70539 | -64.3645 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0d89b9b-a978-3cc9-9fe5-28e55d973f2c | -6.5333 | -64.51149 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa0d145a-ae70-35ab-aa94-69844e777815 | -6.52825 | -64.38023 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be9336d5-76b3-3fc3-8543-8c0413cc2f22 | -8.20743 | -64.07491 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e74ad78-b768-3e3e-a7a3-7009f668a6d2 | -8.20684 | -64.07858 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75d2f59e-d71d-3d9b-aed7-73cac3016b6f | -8.20626 | -64.08224 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a77298e1-a0d2-34ab-9ebe-3c368652eaea | -8.20404 | -64.07436 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c77b946e-687d-3531-9817-0056c5c6cd0f | -8.20345 | -64.07802 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2675189-ece3-32dc-93e5-8e6e45fbbe0b | -8.20286 | -64.0817 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a79cd5d3-8346-3ada-ad4e-7fec0bd20c2b | -8.20006 | -64.07747 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 72889d41-30d7-368a-ad1f-7d83c1d8ec0e | -9.4701 | -65.56665 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe1b683d-02e2-3a49-a37f-a0b8e89a05a6 | -9.38414 | -65.49509 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c1e9206-236d-3d88-b250-e34bbcf076a8 | -9.38059 | -65.49449 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| afe6735e-12d3-3d6b-8aba-306fc0a0c9b8 | -9.37993 | -65.49854 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 808f9609-c72d-39b7-be61-d7e859f37003 | -9.37705 | -65.49389 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| faaaf721-a2d0-34be-abd0-ed07d7d6dd0e | -9.37639 | -65.49794 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e8abc2c-d89c-38ce-86cc-a70ee3a1bf00 | -9.37506 | -65.50607 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20a1ff25-a243-3bed-8460-091c737dff92 | -9.37439 | -65.51013 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 741906bd-a9ed-3f82-8e96-18fea317c136 | -9.37372 | -65.5142 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fba7286-365c-3598-8e0f-f67818c43c26 | -9.3735 | -65.49331 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07a29471-01c0-355d-b446-404b0616c1cb | -9.37284 | -65.49734 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5423230e-e7f5-3ec4-a365-05e34b6b75e6 | -9.37217 | -65.50141 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91c403d5-c5d7-3d3f-a91a-376b72f41e8c | -9.37151 | -65.50548 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a704c9e-862c-3115-89ed-971f16ba6271 | -9.37084 | -65.50954 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23b9e1d0-3a9b-3a54-884d-5493620654cf | -9.37017 | -65.5136 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5107bb9a-8dcc-3fc8-877b-7106f09677f1 | -9.36929 | -65.49675 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca5f422c-981e-34a9-bcc3-2202e2ff0ac4 | -9.36862 | -65.50081 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c178cc7-b8dc-3929-a5d9-0c6a833261f4 | -9.36796 | -65.50488 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 394cdecb-3fd5-3822-b1f7-92ab9219071c | -9.36729 | -65.50894 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66464654-e7aa-3613-b3bb-3fdedf6b788e | -9.36662 | -65.51301 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 076c0494-f8da-3724-93b2-2938cdbdd062 | -9.36508 | -65.50021 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d2c264a-c249-3e1b-ab90-4517b84a2903 | -9.36441 | -65.50428 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba8dec26-fb15-3f3d-a049-0bc18d9bb341 | -9.36374 | -65.50835 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bc7363a-9e5c-338c-8964-7f5ac46289a8 | -9.36146 | -65.63375 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a3670cc-af12-381b-a77e-9c6aa05f99c1 | -9.35789 | -65.63316 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c8d5fda-6a41-3046-b21b-3d10134e6ae4 | -9.35431 | -65.63256 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1ba966f-52ea-3481-abe3-70d801d586a2 | -9.3423 | -65.7282 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b68d829c-86b7-3fa3-bfe4-716c3370e49f | -9.34161 | -65.73236 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f383056f-fb75-3221-abd2-2f190eca311b | -9.33871 | -65.72758 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 336d1dc8-fa19-3a7a-93f2-58a895222da0 | -9.33803 | -65.73174 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f6153af-1d1a-3cb9-8d21-97512744f568 | -9.33734 | -65.73592 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72bf5241-f669-3874-bdbb-3c3b754d4405 | -9.33512 | -65.72697 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6ec4009-cfb7-3946-b1f7-4c29a020368e | -9.33444 | -65.73112 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c7784a8-ee4b-349a-bbbc-11d1f55761ee | -9.33154 | -65.72633 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cc6067c-b168-31ba-87c8-6e95bf82575c | -9.32046 | -65.68188 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 212103e3-6f4a-3569-b322-7731f34247f4 | -9.31978 | -65.68601 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f94f0ea0-a6b6-36c3-9554-2bd35e1bcf77 | -9.3162 | -65.68538 | 2024-09-27 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a44cfa9-eff1-3de4-88ed-9f5fcd15a328 | -3.27229 | -69.04884 | 2024-09-27 05:27:00 | NOAA-20 | SANTO ANTÔNIO DO IÇÁ | AMAZONAS | Brasil | 1303700 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00e5f024-e74f-37ce-a912-70423d3b20cb | -3.70107 | -69.39658 | 2024-09-27 05:27:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b4c46ef-724e-3edb-a570-5d7208c92cf1 | -14.56582 | -50.35231 | 2024-09-27 05:29:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5999fd6c-d53e-37e4-88d8-60fc68d13144 | -14.85067 | -51.46054 | 2024-09-27 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1fed29fa-880a-39e4-ad15-b6f2a5c6bfe8 | -14.95106 | -51.44564 | 2024-09-27 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |


[Clique aqui para ver as próximas entradas](README126.md)
