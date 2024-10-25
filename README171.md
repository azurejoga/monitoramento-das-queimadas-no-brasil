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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 060056af-331f-31ac-bddd-21760457ec6f | -6.20787 | -44.37819 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 7aff1e2f-fc87-3e61-946a-69935ae0d219 | -6.20438 | -44.91361 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0371985-813d-32ed-90c7-8e1687a2e7bb | -6.19316 | -44.31597 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b0975d0-7734-3d0a-95eb-2b2a384a0bca | -6.18984 | -44.29589 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 559cf27f-1dab-3228-b6eb-c37f3f2d8834 | -6.18794 | -44.73196 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 81329f3a-b7c4-371c-974d-8694f82133f2 | -6.18775 | -44.73229 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88d93218-23a1-3777-b83a-6cb8a262743f | -6.18547 | -44.29656 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a03cd49-d672-3733-a879-150d5eec3753 | -6.18394 | -44.52765 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5b3369c8-cf7c-3f14-966d-fac7a42c67a5 | -6.11657 | -44.92818 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 61d37afd-9ca6-3545-a49c-ebdab448532c | -6.08384 | -44.70831 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c81b18fc-7cd0-3388-b43f-5a65cc03a360 | -6.08091 | -44.71682 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 90925476-0f00-3c9f-bc66-6418a114b018 | -6.08025 | -44.71291 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 10111519-1a4f-336d-bde3-387d8c921652 | -6.07088 | -44.70619 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8f8754dc-703e-3793-af41-300c67a338ba | -6.05284 | -45.01777 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 244ef89d-ce3b-3a7f-b3b7-d4d568e09cd3 | -6.0486 | -44.57784 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 06f0325f-aee4-31a1-a9a0-cff51cddcac9 | -7.85038 | -45.1481 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2053430c-cbfe-3b0b-97a3-e229e4c0b8f9 | -7.84579 | -45.14527 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a821d037-0dbe-397c-9b96-38719e9ed14d | -7.66061 | -45.36478 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 81c63f09-11c6-3850-ad2e-3b4cbc269a5e | -7.05451 | -45.21044 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e017e289-0c07-360b-a3d0-f0bfa1a21c3e | -7.02663 | -45.1931 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 7b16b2cb-824a-3577-922a-cf9b1ee74d80 | -7.02319 | -45.19739 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| ecb188a1-564e-3074-9d97-461161e7e8b7 | -7.02258 | -45.19377 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| f288bf13-ac1b-34ef-acd1-2716376d7997 | -7.02206 | -45.19342 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 7430cfd5-c32c-3b70-b992-cdba215396c2 | -7.02197 | -45.19017 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| c80f382a-ffa3-3e75-a234-e248ca945434 | -7.02148 | -45.18981 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9fe025dc-5fe4-3d9c-80ac-c47460053885 | -7.01853 | -45.19446 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| a7d3497f-9c73-3261-9b0f-edcf1d213055 | -7.01802 | -45.19412 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 85353df9-6844-350d-93dc-d20eec1795e9 | -6.58552 | -44.2007 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e144a92f-1df5-3991-a90e-dee99e1aa213 | -6.53799 | -44.23737 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fab0ad57-e6b3-37bb-afb3-e950f8e7997e | -6.53732 | -44.23344 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f3a82ef9-2364-3c7f-bd61-ed0c5db015f8 | -6.53667 | -44.23564 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 70f0a2fa-2b7e-33a7-9a23-679b303e2244 | -6.53603 | -44.23177 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| f896cc3f-cd99-3f25-b693-ed7dc9ae2ca8 | -6.53365 | -44.23816 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 70696d1c-549c-3a45-af4a-04ceb0c198a7 | -6.53299 | -44.2343 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| b92e1088-44dc-3c3e-83d9-be47872bc65b | -6.55234 | -44.2952 | 2024-10-25 16:52:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 69ae3028-3a67-3702-bffe-7ce2f0793f5e | -6.55057 | -44.29348 | 2024-10-25 16:52:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9e298bbf-0ac0-3f55-8d35-557f7833478a | -6.50194 | -44.55937 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e4baf3e4-aaa4-3642-a689-1b6290180ec3 | -6.46452 | -44.67258 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e79066b1-51de-3bbe-ac34-3613c6f93539 | -6.43312 | -44.87267 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 1117ee34-e3e0-3883-843f-a6c372a1f2a6 | -7.79028 | -43.88761 | 2024-10-25 16:52:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f3fbbf28-9412-3414-be85-f640308e2981 | -7.61616 | -44.06019 | 2024-10-25 16:52:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 62d8fef4-6748-395b-9932-134ea0d5252e | -7.54016 | -44.04173 | 2024-10-25 16:52:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b6a36a87-f489-3235-80dd-d7786d70671d | -7.53946 | -44.03758 | 2024-10-25 16:52:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cc1f8b8e-6cf4-3f9a-b399-b19c3e4f4f32 | -7.32872 | -43.88698 | 2024-10-25 16:52:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 503cd305-66dc-3854-a32e-3d50928e4aaf | -7.15657 | -44.0958 | 2024-10-25 16:52:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76d2254d-ef31-300c-91be-c6631f155d73 | -7.15514 | -44.09404 | 2024-10-25 16:52:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 05f0347c-6098-30f6-aedc-d8229948eec7 | -7.15435 | -44.08297 | 2024-10-25 16:52:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d7c9f7ef-74f9-31f4-b3d1-794a194f670d | -7.15371 | -44.08538 | 2024-10-25 16:52:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 76e6585d-b015-393d-8eb5-99af94b040b1 | -7.13648 | -43.89894 | 2024-10-25 16:52:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5e9e804-288f-3afd-96ac-e75ba90318d0 | -7.13573 | -43.89689 | 2024-10-25 16:52:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5881da0f-6719-314e-9856-01844391277a | -7.1036 | -44.10682 | 2024-10-25 16:52:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2a6a6fbe-48a2-3d4f-8e54-cc9d54ce8705 | -7.10267 | -43.88654 | 2024-10-25 16:52:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 8e3467aa-1c26-3a29-aa9b-592bdef0d426 | -7.1 | -44.11196 | 2024-10-25 16:52:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0cf8dc6c-1713-34ce-b173-b30fab8489a3 | -7.09563 | -44.11258 | 2024-10-25 16:52:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eaa5d0e2-1558-3bdf-b1eb-5b79b92503e9 | -6.9601 | -43.87385 | 2024-10-25 16:52:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1afba8e4-484f-3cfa-a104-1a87c4c72c65 | -6.83638 | -43.70157 | 2024-10-25 16:52:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 54eded9a-3dbf-3d4b-8d44-553ae3f237f4 | -6.81494 | -43.76548 | 2024-10-25 16:52:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7bc37bc-cfd1-32e3-b8a1-b91424f7bf26 | -6.70352 | -43.95834 | 2024-10-25 16:52:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| dcb61d5b-18d9-3079-b07b-132d2c3683da | -6.70281 | -43.95403 | 2024-10-25 16:52:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 45a799f3-e4be-3e41-b491-9475108e1afb | -6.6984 | -43.95487 | 2024-10-25 16:52:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 8bca498d-2601-3e9e-bfb4-3dbce8c83613 | -7.73505 | -44.78305 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 2993d22a-8d27-3113-9e61-cdeb530c50a4 | -7.73441 | -44.77929 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 38a31950-e590-3d41-bc4d-edabac5aa569 | -7.64488 | -44.69078 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 89a90ba4-2113-36f5-91c4-348b7870fb5f | -7.4444 | -44.73989 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b2197ff3-6888-3737-be93-47d31fd7c649 | -7.44024 | -44.74051 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3b516db9-4a78-3777-818e-6eee25f97e7b | -7.42108 | -44.72797 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bd70df94-38a0-3f96-8754-2ca43dfce2be | -7.40506 | -44.73417 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cd2375ca-3f05-3396-951f-7a6ccd259be9 | -7.23085 | -44.29615 | 2024-10-25 16:52:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3e2ed84e-f4cb-37a4-af0d-84866e645266 | -7.06178 | -44.26682 | 2024-10-25 16:52:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f3bf761-d1bb-3351-bb03-27c141f9686a | -7.03523 | -44.26689 | 2024-10-25 16:52:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3dca97e-21b9-3d99-975b-f1d39b50ccfa | -7.36471 | -44.76036 | 2024-10-25 16:52:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f33afd36-da13-3c48-9ace-18d255ca2a3d | -7.36121 | -44.76497 | 2024-10-25 16:52:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 21746973-2c89-345b-ae84-161ca145ac4f | -7.34539 | -44.97528 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fb73568e-c089-3acd-98f3-861f55412b7e | -7.30391 | -44.97427 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c5fd92c9-641e-3688-a187-a5d72c9f6970 | -7.29923 | -44.97131 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 90093090-0281-378a-aa00-2293cca6edfe | -7.29453 | -44.96828 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f6efae84-e06f-3282-b869-9edba87be32b | -7.29104 | -44.97266 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e6e4eb53-297b-3882-a351-91298a3eb05c | -7.28693 | -44.97329 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 4759f800-4b3e-3ffd-9ee8-99d8658b9330 | -7.28283 | -44.97394 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c86944ae-b2a1-3167-8fb1-e9cefdb7462c | -7.2039 | -44.97571 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5eab24ac-5896-37bd-8c37-db311ad84803 | -7.20308 | -44.97532 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 409bae91-76ee-35f6-9b83-25182f235443 | -7.19981 | -44.97644 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 153d6bcf-8ca6-3e20-8255-a24a058947a9 | -7.19899 | -44.97604 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 30253cbc-ff15-3a9e-8555-2398e6848596 | -7.17821 | -44.99876 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 218584e7-bf17-3fe0-a4a1-d52956948ffd | -7.17352 | -44.99581 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9718238a-1b75-3bdd-9dd8-9a6ddf65dc63 | -7.16887 | -44.89046 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0b4106c6-d465-35f5-b2f5-79d6413f6859 | -7.12067 | -44.98197 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e3ee77f5-5e1d-305e-add4-5473be5ea29e | -7.12005 | -44.97828 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 3d4747d6-5b93-392d-8406-efc256419a27 | -7.0984 | -44.46184 | 2024-10-25 16:52:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5384ed23-148a-36cd-91cc-8cc91b3bb2a1 | -7.04537 | -44.68841 | 2024-10-25 16:52:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 35b9d008-529e-3674-89c3-d7f8e0aaa5c5 | -7.04444 | -44.6885 | 2024-10-25 16:52:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 62345d43-d7b3-339c-9fac-2fbc623d2c0c | -7.03479 | -44.68206 | 2024-10-25 16:52:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9e534311-aa21-3d34-951c-b97e4b5b3c16 | -7.03093 | -44.86656 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 124a1851-cec9-373a-9367-c56d03d35b06 | -7.0004 | -44.65654 | 2024-10-25 16:52:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a5c61f9-3ba5-3758-8e9c-38ebdcf073b7 | -6.99973 | -44.65249 | 2024-10-25 16:52:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4b6ad76b-e038-326a-8529-513ac07a0783 | -6.99957 | -45.03306 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e70fb9a8-15c9-3434-8c24-ecb30191b27e | -6.99611 | -45.03302 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 899cabcc-511b-308f-8975-55991536a9c6 | -6.99548 | -45.03377 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 20cac10e-b75d-3d5b-9b40-465d6268c68a | -6.98436 | -44.53364 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ab61cf0c-3463-3563-a56e-3908ab51cb9b | -6.98022 | -45.01296 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README172.md)
