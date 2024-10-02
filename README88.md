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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5ca74bc-552a-3f30-80c0-b8b256db93d2 | -6.95126 | -47.66169 | 2024-10-02 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95f221c2-c0e8-3749-9b23-415f5e1e6c84 | -6.95101 | -47.66391 | 2024-10-02 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bcba363-3c4e-3730-b0d6-f2eb7fa143d6 | -6.94857 | -47.65502 | 2024-10-02 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 448e25ea-9317-3781-b3fd-a91f73fa714a | -6.94823 | -47.65706 | 2024-10-02 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 97a47c2c-f480-3fad-9077-fa3fe9eba55f | -6.94796 | -47.65921 | 2024-10-02 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b78b1ac-d93e-39ed-b333-d48167bb3224 | -6.82544 | -47.97987 | 2024-10-02 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2628f3d6-2020-36c2-b527-4571be90b9ca | -7.25298 | -46.84326 | 2024-10-02 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7f563da-4443-3d9e-8b0b-baf9da6e33a2 | -7.1825 | -46.94947 | 2024-10-02 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6e62d129-78f6-3eb9-ac9b-4bca80a4f97e | -7.18179 | -46.95435 | 2024-10-02 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 688604c9-6fa5-396b-8d0d-a176cd03dc7a | -7.1811 | -46.95914 | 2024-10-02 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3045c2e2-c6f1-3bdf-abeb-a560762af6ed | -7.17866 | -46.94899 | 2024-10-02 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bee10640-ee85-3805-a93c-f2a76dbfa4a2 | -7.17796 | -46.95383 | 2024-10-02 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ecd81266-742e-33dd-9178-775338050c30 | -7.17728 | -46.95854 | 2024-10-02 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6172553b-a0b1-3e51-8081-5c2dca7d5790 | -9.17153 | -48.75269 | 2024-10-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 52eb0909-1779-3cc2-abba-0360832fa8f3 | -9.1715 | -48.75099 | 2024-10-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 85477b8e-7802-3941-8b76-d313c0f2982d | -8.96661 | -48.15064 | 2024-10-02 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9365f93-1c31-33eb-a46c-854422e2036b | -8.96599 | -48.15493 | 2024-10-02 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1ccd747-6de1-33cd-a478-8117ab0eef68 | -8.9593 | -48.14954 | 2024-10-02 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c59c1973-7354-3c3f-81b8-d03c37c53de8 | -8.52149 | -47.32487 | 2024-10-02 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bf4b4f6-1cb4-3b8d-aaba-21eaa48205e0 | -8.52081 | -47.32657 | 2024-10-02 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b746c3a-d3ed-3403-a31e-13bd175cae73 | -8.51769 | -47.3243 | 2024-10-02 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02bbd682-ce26-3646-8430-f2ecc4df0957 | -8.517 | -47.32599 | 2024-10-02 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a56d4c5f-15fb-380f-b2da-22ebb5e8fcd3 | -8.51699 | -47.32893 | 2024-10-02 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecd67c66-f780-3144-970f-796991f357b2 | -9.70839 | -48.01763 | 2024-10-02 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0555765a-3820-3bfa-94c5-a7df40323abb | -10.77853 | -48.75 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6983cd27-11fc-36e7-96ae-99ea7c9926b6 | -10.77367 | -48.75791 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95bb1393-a4c6-39eb-92cc-f49f35ed6113 | -10.74514 | -47.97408 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8208477-0f80-3c3d-b3a4-907571e45b16 | -10.74471 | -47.70237 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af8a39cf-99ee-37b8-9c49-066427e6a69d | -10.74446 | -47.97887 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d1872d7-9a23-3de1-95e0-e7e9e25655fe | -10.74252 | -47.70024 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cf4bca4-4b8e-33c7-ba88-8fcf2fb515cc | -10.74155 | -47.69697 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c749d9f-da7e-3118-949a-dce3dc89a5c6 | -10.74135 | -47.97369 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 841383f5-9386-3809-98e3-2f1e3fd99da4 | -10.73867 | -47.69976 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3e9efec-8456-366e-b752-ec99aa923ea5 | -10.7377 | -47.6965 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a17fde44-44e4-39bb-85e0-49df40257606 | -10.73555 | -47.69437 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3f33c0c-9237-3474-8dc7-2a26e03470ce | -10.73386 | -47.69597 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd4301f1-e353-3577-9665-3fd751d388ed | -10.73171 | -47.69384 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6f00461-467e-3323-8334-f4e11b9ee265 | -10.73071 | -47.69052 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cbe7acd-b6dd-383c-afab-9c76a292158d | -10.7293 | -47.68349 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36707c71-3ef1-3917-8063-10066132da86 | -10.72858 | -47.6884 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa0e74cf-496a-35bf-9f34-68e00c405eee | -10.72787 | -47.69329 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 687f47fc-e94e-3740-b27b-56c01e34d4c5 | -10.72616 | -47.67808 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00fe068e-2240-338d-81b7-e3b05b86acfe | -10.72513 | -47.65818 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98aabf21-5fcb-3d54-b066-de34eae4ba46 | -10.72185 | -48.70773 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9e5d07b-9985-3931-bda6-e7ad74050a6f | -10.72128 | -47.65766 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a383d31-3dfb-350d-b2fd-51dd9c31657c | -10.72124 | -48.71198 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6fe14cf-450d-37ca-84c5-b6e64e890e4e | -10.71848 | -47.67703 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acda71e9-2795-3a05-907d-921d5c1b7fc0 | -10.71813 | -47.6523 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1436e622-40d9-3914-a912-c8af1b5261ae | -10.71702 | -48.71563 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00473b00-fccc-3cff-af09-2dcd651b71dd | -10.71641 | -48.7198 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4df4a12f-66ce-3cdd-83a7-c09ef6fcb959 | -10.70802 | -48.72666 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d9df3dd7-dc3a-3bc7-af1c-a0a5387af25f | -10.70744 | -48.73069 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 601d3140-6772-3a7a-bc82-49af61dcef8a | -10.70499 | -48.72208 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ff73579-6cc9-376b-b711-2a1b0adcde6a | -10.70441 | -48.72607 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72d5448e-88c3-31fd-85c6-1ab358d2cc27 | -10.70411 | -48.36425 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7be6b657-6ccc-37a8-9106-c609b8fe8058 | -10.70347 | -48.36863 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1d2a234-10cd-3490-a735-00fce556709e | -10.70196 | -48.71741 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e6fe170-a967-3124-964a-397e220645c1 | -10.5937 | -48.06215 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6980b199-39a2-3615-83df-18bf72d2426a | -10.59056 | -48.05729 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 64c0771d-b0fd-3b1a-94f5-f9cabb2db80d | -10.58932 | -48.06604 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d5bb1027-36a9-3a30-aa51-eff5db6d7f88 | -10.58869 | -48.07048 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c663d741-cb65-3fae-bc30-973d529ac910 | -10.58808 | -48.04787 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69e4e8b3-5208-33fb-95d7-9d9b5ac4bf50 | -10.58683 | -48.05666 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a7b7d96-5143-3a6e-8160-e037541eef61 | -10.58621 | -48.061 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eeddb8b9-85c5-3d66-ae49-3e028060a5ee | -10.58558 | -48.06547 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 69f59cd0-5f29-3e18-a773-db491418b776 | -10.58493 | -48.07005 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 52449b2f-6651-30f1-b184-dbd6537f1e56 | -10.57107 | -48.02463 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bfce8468-0205-3365-9a94-9f27f23c5250 | -10.57039 | -48.02924 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a397a19-4c81-3b44-9f46-124d036996cf | -10.56665 | -48.02862 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c56ab02-c305-3b4a-8a29-044938167f12 | -10.56601 | -48.033 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| adde9dc9-7680-3786-9671-0a2e994bcc44 | -10.55989 | -48.02248 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a0673f0-7b36-3733-963a-b0d0c504403d | -10.55921 | -48.0271 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 087cae6d-36df-39b5-91a0-fdb18e5eccbb | -10.55729 | -48.04026 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3818172b-f615-3038-9ac8-73fd22557e21 | -10.55485 | -48.03074 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d2b770a-0e53-3074-ae55-285bd5bb8709 | -10.55294 | -48.04387 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8343b071-1665-3d7a-945f-c4af0fabde13 | -10.55124 | -49.01047 | 2024-10-02 04:46:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d53f5647-51f1-3bf8-b98a-66be75f6d7d5 | -10.55047 | -48.03451 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03136a6e-e978-36d9-93fe-842d354f69e2 | -10.54982 | -48.03896 | 2024-10-02 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e163253-0738-3ed5-b855-284a9c42fcc6 | -10.4661 | -48.19713 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a186319d-5432-397a-89a4-85fc90b1c1ca | -10.46411 | -48.23754 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 866d62cc-d286-383e-813f-6208f7cead1f | -10.46236 | -48.19681 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a1132867-5a6e-3d06-a599-2cf0a81b130b | -10.45978 | -48.2414 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8029ba6b-e121-3a50-a0a7-b39cecd47c8e | -10.45922 | -48.19227 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c4dc2200-aa79-3cf0-b6ef-e40c64e0bc93 | -10.45607 | -48.24086 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d98d814-9521-3f75-a9a1-108877c09089 | -10.45546 | -48.19212 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff2dadd5-e05d-3b97-9962-96b7a4eace49 | -10.4348 | -48.16312 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5546d01-e4c0-35f2-b940-ada203ba4508 | -10.4311 | -48.16244 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d67c5c20-9287-31d8-b933-1f63a0db4c55 | -10.43045 | -48.16685 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d2712a0-111a-32fe-9166-68f3272bc227 | -10.32677 | -48.51754 | 2024-10-02 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d110b96-ea18-3040-a190-6027a37c3d2c | -10.23723 | -47.68544 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 28b9691e-5bb7-3d88-bfd7-9a13f7403bc8 | -10.23655 | -47.69018 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 38a7bacf-e82a-3aee-aec0-e7d92a5ffb37 | -10.22579 | -47.68375 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81f219d1-80d5-369d-9590-3e5c6ead72aa | -10.22512 | -47.68851 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24a3f57b-3e59-3d5a-9e9d-effff08cb654 | -10.22131 | -47.68794 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1564d8f2-30a7-37e0-9e7d-43265b511f66 | -10.03276 | -48.22305 | 2024-10-02 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d308970-62f2-3a27-a33d-82d78498f3ca | -10.01138 | -48.84853 | 2024-10-02 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8edacdc4-7c81-357a-8004-96fe1ab70eae | -10.01076 | -48.85268 | 2024-10-02 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53251a35-998f-3fbc-8791-0fd187d162eb | -10.00721 | -48.85209 | 2024-10-02 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fc3838e-84e5-32eb-8bc0-0b2456e771bb | -11.67466 | -47.83184 | 2024-10-02 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e001d2ba-2223-3a8a-b3c2-3700ef8bdc6d | -11.28003 | -48.41761 | 2024-10-02 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README89.md)
