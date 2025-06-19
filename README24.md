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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c940b3e-6c1c-3bb5-b325-4c83f90fd5ca | -9.49842 | -56.09099 | 2025-06-19 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 94096a72-5f4a-3b17-97d5-5f16d1c83514 | -11.94386 | -58.76332 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb2a7cd6-877f-3dab-82cf-b5c4766c0e3c | -11.13296 | -53.9365 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a90b813-0f2c-3ac6-88f0-9a8dbbf41069 | -11.62071 | -58.29071 | 2025-06-19 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 896a6ed3-425b-320c-ae9e-3f6d20cf4d6a | -11.14982 | -55.17613 | 2025-06-19 05:38:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68133921-3d6a-3edc-b656-db82531c5148 | -9.96668 | -64.95745 | 2025-06-19 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58ad0171-97a0-3fa8-a619-2dd3712e1e98 | -11.12645 | -53.94006 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1010086-7986-30d1-bd53-e4dbb4aaf394 | -11.08242 | -55.05313 | 2025-06-19 05:38:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8058ad0c-75c2-3462-8083-efe52b3771bb | -11.94618 | -58.74622 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9880964-6a4a-3153-8fa8-78bb61d3c9a1 | -12.02857 | -57.09364 | 2025-06-19 05:38:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69981e75-5652-3d4e-bb78-183312bc119e | -11.95055 | -58.7469 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 45dec63a-0d3a-3cb6-828c-25bd44acc21b | -11.96314 | -58.75288 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 81174cf3-b29c-38af-86cb-a390d36f6f99 | -10.84669 | -53.7797 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8814228-a3de-3e31-bf39-81f123cc0158 | -11.96109 | -58.73521 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7a5abb0-92a7-3734-bdab-468ae120e36a | -11.95874 | -58.7524 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9d70d478-c940-321c-8035-d6aefcd55724 | -10.86037 | -53.76784 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dcfd04a-d67b-3f1e-a92d-52c8d0cf720a | -11.82255 | -54.50385 | 2025-06-19 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a90dc34-05a6-342f-a287-9aa9d7dbede2 | -10.28238 | -60.53971 | 2025-06-19 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9ffcdb7-4e28-33e1-bbc9-3877bb3667d5 | -11.95376 | -58.75616 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| def81419-b916-3c43-8814-1ecf20964b8d | -10.09592 | -52.74094 | 2025-06-19 05:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 678a488a-9a49-3d81-a65f-d05f840ee464 | -11.95932 | -58.74813 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5893493c-dbe5-3922-98da-8ddb6145a7ee | -11.15077 | -55.16869 | 2025-06-19 05:38:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d71be01-7894-33eb-bd1d-14ff078f71c0 | -11.13059 | -53.93422 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79bd7bb1-9573-31a9-b3b0-1ca74c58611b | -10.08423 | -60.5016 | 2025-06-19 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed6f63e0-af13-30c9-a268-d84b2595a12c | -8.30834 | -55.10069 | 2025-06-19 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a1c2eb5-66f8-3a92-bc84-16e68c069134 | -10.08041 | -60.50103 | 2025-06-19 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae74a5df-08ad-3bf7-ba71-a0f09f42f83e | -10.09705 | -60.49388 | 2025-06-19 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee93e238-7d11-3c48-9da7-5c43e8691941 | -10.83665 | -54.01206 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2f377ab-470c-349f-851f-eacf619478bd | -9.45672 | -57.84757 | 2025-06-19 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbac5e13-0eb3-30b2-9377-9b6e5a05a9cd | -10.08864 | -52.73699 | 2025-06-19 05:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d4ddcd3-afbf-31db-931a-b7010fab5548 | -7.89375 | -61.47403 | 2025-06-19 05:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7eabb08-9a0c-3212-9815-e114f718b9b1 | -11.95434 | -58.75188 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c8a778f6-0376-36db-ab77-24db21ac9709 | -10.09502 | -52.73772 | 2025-06-19 05:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 58ed0513-cce9-3588-b1a6-ce7d1f86d936 | -7.92816 | -61.55608 | 2025-06-19 05:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a022d7a-647b-3335-9c08-c34727cb9985 | -11.13841 | -53.94173 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95317af2-7029-320e-b4bd-54ee3110a7eb | -11.08031 | -55.05514 | 2025-06-19 05:38:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11b4b92d-4ee0-3f69-a710-2d11baf5ad46 | -11.95291 | -58.72954 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a265447-d25c-3894-beb7-4bdf4f83241a | -11.06663 | -55.04388 | 2025-06-19 05:38:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fac412a6-9348-3eb9-9bf6-d410b313b763 | -11.95319 | -58.7604 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c626e222-749a-3b91-bf5d-6ced5e0648a2 | -11.15029 | -55.17244 | 2025-06-19 05:38:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0a631b5-2d41-3a87-b4db-b7924aea164e | -11.9488 | -58.75979 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70239df8-eb7e-31c8-a9fa-cf5178c111ac | -11.95789 | -58.72585 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb912664-9c96-386e-8397-a7a74c872db1 | -11.13244 | -53.94086 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2eb03688-4f02-373d-b263-f92e425ed2bf | -11.13601 | -53.93943 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52019b4c-d9af-3c26-a23f-1cb66a8be912 | -11.07685 | -55.05244 | 2025-06-19 05:38:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49c65431-255a-3fb3-ab73-c1de9470d9f1 | -11.94939 | -58.75549 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| eecafd40-287c-3077-a98a-b8391c5c3f7a | -10.84775 | -53.77092 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e54bda7c-c8a3-33a3-ae38-f6d4e6693689 | -10.85433 | -53.76719 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55568584-1663-3f0a-841b-a67ae5a96d32 | -8.72282 | -64.17699 | 2025-06-19 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed2fc11a-0ee2-3250-ad9f-7566b88cde86 | -11.96168 | -58.73086 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e49db6c5-353d-32b4-a573-e0d822178d6b | -9.33467 | -57.84359 | 2025-06-19 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74a9283c-7d83-32dc-a08b-1be2cf610bf6 | -10.83718 | -54.00778 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f59b40a-177f-3fc8-8512-458726968a5e | -11.82305 | -54.49968 | 2025-06-19 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a976a5f-3f23-3616-a49c-98176a4836c6 | -11.13656 | -53.93512 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45d9baa0-c1cf-38d4-a463-a6eea8b4f7a7 | -10.081 | -52.74635 | 2025-06-19 05:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d99cfe23-2b0e-3526-ae63-08147ba9f7f1 | -11.95552 | -58.74324 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 42f556ac-c95f-3843-ac6e-f474b1689e68 | -11.95114 | -58.74258 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b825220f-52c9-3add-bee2-b23f7c8bdd90 | -9.00237 | -61.52528 | 2025-06-19 05:38:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8256b049-c046-3912-ad42-9d3639a52f67 | -9.49373 | -56.08732 | 2025-06-19 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3ca7ad5d-823f-3452-a84d-b36407c04891 | -11.9605 | -58.73954 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20ca530b-cfab-31e1-a8ef-2a771af14a73 | -11.94997 | -58.75121 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ed319033-d74b-3889-a853-316da6103a60 | -12.43009 | -54.87679 | 2025-06-19 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59561909-ba0a-3f5c-8ce4-82cbac1c29b7 | -10.088 | -52.74208 | 2025-06-19 05:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61071181-1087-305c-9eaf-e8453cd0570a | -9.46122 | -57.84823 | 2025-06-19 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ffe528d-9daa-332a-8b56-fd46426c1f6f | -12.42485 | -54.87198 | 2025-06-19 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b233baa-7875-30ad-8481-c735f7991a40 | -11.9456 | -58.75052 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7bc2aa9d-53c9-3b32-af12-889b9ee66cea | -10.51004 | -53.58025 | 2025-06-19 05:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6028c4e-1b33-358d-8358-0b451360aaf6 | -10.0811 | -60.49631 | 2025-06-19 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f047019-152f-39b6-866f-9996caeeeea0 | -11.9395 | -58.76255 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b97d20b3-d768-3e56-a0e3-b5d9c562252b | -10.84172 | -53.77014 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16bfa99a-2327-3708-a426-21a77c3cb7be | -10.08257 | -52.74449 | 2025-06-19 05:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b42b81f-d250-3c85-8c42-acc418a721c2 | -9.48866 | -56.08658 | 2025-06-19 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 541ed6fe-8878-34d2-8755-462d50816224 | -11.64822 | -54.14191 | 2025-06-19 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e589f19-9219-3d4b-ae04-e6c8f7fcef71 | -9.07873 | -64.41293 | 2025-06-19 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e49e699c-c454-3829-b434-2f3576ddac1c | -11.52821 | -56.99211 | 2025-06-19 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bff4a195-653d-340a-8697-26f2fcc11b7c | -9.48827 | -56.08952 | 2025-06-19 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbc76217-c399-32db-b750-319f06a8a0c4 | -12.49891 | -55.7396 | 2025-06-19 05:38:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9aead04-96a8-3144-91da-e52691615348 | -5.14 | -60.3863 | 2025-06-19 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9858a88-ea6c-3690-ad0a-608faa42ebc2 | -10.27856 | -60.53916 | 2025-06-19 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 545eb496-ceb5-37f4-8849-8bd584cfe772 | -9.40025 | -63.13529 | 2025-06-19 05:38:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61455a4d-10b7-31d2-a735-0f88fc33b3d8 | -11.76946 | -54.3653 | 2025-06-19 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f80bcf9d-5ad9-362c-9726-449bbc4cd1cf | -8.0892 | -43.096 | 2025-06-19 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| ca001d80-34c9-30d9-92a0-89a9228710c6 | -8.0703 | -43.0981 | 2025-06-19 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 2d240adf-11e3-3394-83de-1a62784d9417 | -11.952 | -58.7376 | 2025-06-19 05:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 502d73ff-1466-3976-9192-0520fcb60466 | -11.9707 | -58.756 | 2025-06-19 05:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 390290df-e1ef-3796-b278-6cc61eefd5b5 | -11.9518 | -58.7574 | 2025-06-19 05:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| c1ac6d5f-f14a-3a5a-bd47-ecab50a03085 | -11.9709 | -58.7362 | 2025-06-19 05:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 56bce5f4-e90d-389e-93d1-caa5a79e5038 | -12.487 | -58.46897 | 2025-06-19 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ddc65bb-2ee0-33a0-8d2a-0eea4d93732b | -12.23459 | -63.59988 | 2025-06-19 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dae71e6b-2746-3b9b-b565-76f18db7419d | -16.30146 | -58.2613 | 2025-06-19 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 9573bd8c-bb1b-30a7-a29d-9bf2408a136b | -18.66152 | -55.74858 | 2025-06-19 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ed3d3cc4-37b9-3c32-a979-b81f8192db36 | -18.66067 | -55.75719 | 2025-06-19 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 56f86e48-9de9-3b44-8484-7875085afecc | -12.23064 | -63.60302 | 2025-06-19 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b205650d-ae83-30a3-ac98-d012688de51d | -16.30694 | -58.25658 | 2025-06-19 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5e8b679e-d320-303c-916e-464f66e779a0 | -14.02836 | -55.12788 | 2025-06-19 05:40:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75085109-03f5-382b-90c9-ea51c7388216 | -12.4668 | -58.46859 | 2025-06-19 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 115993e5-023c-3dca-9908-6bafe5dc66f5 | -16.30628 | -58.26192 | 2025-06-19 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 5497e731-b590-3d1f-b194-4529023a5878 | -14.30868 | -59.89205 | 2025-06-19 05:40:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7a329de-694f-3420-afe7-32b27a67421c | -16.32133 | -53.79269 | 2025-06-19 05:40:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3983d3a1-a88a-3474-a9db-3367522b2c93 | -14.06797 | -53.39591 | 2025-06-19 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README25.md)
