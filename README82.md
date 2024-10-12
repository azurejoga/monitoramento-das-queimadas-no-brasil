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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d93b9457-f47a-3021-8167-a1acb20a6661 | -11.54871 | -60.15314 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4c0ee5e-c846-3575-833d-6e86cee9c35c | -11.54806 | -60.15495 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e05ae1d-9443-3c68-9adf-eac4eb416fc4 | -11.54477 | -60.15252 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74c16571-0572-38fa-aa47-f4db3e373194 | -11.54411 | -60.29247 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9177d5b4-8580-3f45-9430-ef04b22b5f8c | -11.54014 | -60.29183 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6073a16-1d26-3ea6-8227-d310f12b40e3 | -11.53936 | -60.29621 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e58d038-d03c-3dc7-ae68-0dedc1b61c4f | -11.53874 | -60.29971 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7b74d7a-0dfc-3634-9413-56890b9e35ff | -11.52032 | -60.15342 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee882d38-7f97-3079-95bb-a9255d9221bf | -11.41781 | -60.46046 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb989774-5ede-3af6-93e7-835ebcc12b46 | -11.41443 | -60.45612 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d522e785-291a-3e1f-abb2-a9cb0362a695 | -11.41186 | -60.40054 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f11318ca-5ff9-342c-81e6-c50d93b605d9 | -11.41124 | -60.40406 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c21225fa-68ee-31ae-ad0c-62920ecd3ace | -11.40849 | -60.3963 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70199c9d-8254-36c0-a861-67eb079d952e | -11.40787 | -60.3998 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dd0fcd9-3014-37c4-b364-8b46827c7606 | -11.4066 | -60.40696 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a801a0c7-8d44-3c07-b6bb-9be6d61b56af | -11.40594 | -60.41064 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 31e45341-5018-362e-a79c-ac5afb42b8db | -11.40467 | -60.4178 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82f64c49-9203-3453-bc30-5590285498a1 | -11.40449 | -60.39559 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30c8904f-1694-33f3-9300-6c71bdd62ebc | -11.40404 | -60.42135 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51deb2b1-d7d4-345f-880f-52e68055ea34 | -11.40068 | -60.41705 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3350067-abc4-3319-a6c3-47e576457c5d | -11.40048 | -60.39496 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54ca1fcf-335b-32bc-bb71-3546f5b3d622 | -11.40004 | -60.42065 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b54fe5c7-f0f8-3aee-a975-ed34d625dfdc | -11.30484 | -60.43663 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3720d5fc-c126-3b52-8d68-a30cfe9d4741 | -11.3042 | -60.44023 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78686bbd-e7fa-3a10-8d5b-62290ddb3cdc | -11.30147 | -60.43229 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9dc49abf-8128-3c50-b130-ea3db369ef4f | -11.30081 | -60.43598 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d9ad593-d477-39e6-9ad5-5a2832dbf126 | -11.30018 | -60.43956 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fd46610-c54e-3423-848d-3d4d14909f1d | -11.29742 | -60.43176 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95435032-e87b-3028-8697-de8cf34184dc | -11.29546 | -60.33809 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 282e2c43-0a63-3377-bdfa-9b8f5eda7e00 | -11.29487 | -60.34156 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8312aaf-1fca-38af-9d73-4cf061ef2527 | -11.29391 | -60.33529 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cd1da53-48a2-39fd-9333-6f141ddc0606 | -11.29331 | -60.33872 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 35771103-7f30-3904-b7e6-21953a67fce0 | -11.29146 | -60.33744 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c65d85f4-d06c-3a94-be11-116f9215b818 | -11.29085 | -60.34101 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0622b0fe-cdfb-3297-9f9a-af0f5db55f6b | -11.28461 | -60.4807 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c56ce5f-a333-3731-a31f-cbb5e6f45708 | -11.28395 | -60.48441 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ba76d52-1a90-3d1e-8e6b-0f39d8489ed6 | -11.28353 | -60.44006 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f2bcb40-65c4-3d85-8714-5c1819b32af6 | -11.28294 | -60.44336 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efad79c4-f35b-30a9-8085-531f36d19905 | -11.28137 | -60.49892 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b323e345-351e-3560-bd56-e682bc5a8d72 | -11.28127 | -60.47609 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be59d76c-037d-3a82-ae2d-a56effaf1edc | -11.28063 | -60.47971 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ed8482d5-7932-346e-b1cd-ee4d18164850 | -11.27998 | -60.48335 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8558621b-7a8a-3ac1-847b-42717d4f0f2f | -11.27952 | -60.38319 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6bd4d297-ff6a-313d-9c8e-99f58072577c | -11.27892 | -60.44269 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e6f8ae3-2864-3d81-b88e-c344fdacf241 | -11.27777 | -60.44173 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 399e4508-ccbe-3375-84f1-95408bd0b9d6 | -11.27737 | -60.49802 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8fe01d89-dcaa-3237-9d3c-9f0131010afd | -11.27723 | -60.47547 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8d363550-9ef3-318a-8bf2-cfe30410ccae | -11.27719 | -60.44516 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be35c4b7-f47f-36e5-ad43-753add986d3b | -11.27669 | -60.50182 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fff09431-6610-3f1f-928d-82f33ff0e7ef | -11.27658 | -60.47911 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c281bf51-91ab-3714-9186-adfff7aaec18 | -11.27603 | -60.50557 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99d4d0d4-ca84-33a8-9589-ca2556f1c482 | -11.27593 | -60.48275 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 092ff139-8b29-3fde-a069-267cf4969b57 | -11.27546 | -60.43881 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 27d183e0-405c-3509-a108-b27927cc79ac | -11.27484 | -60.4423 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e594786-5443-3dee-b89c-d6547ef7203f | -11.27402 | -60.36719 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85d481ca-5b6b-382b-929d-5fd7db95753b | -11.27371 | -60.44132 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bbcf32e-09ed-37c8-a4dd-d5188b547232 | -11.27341 | -60.37072 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15866218-cff7-38e6-bf17-8fd1337bf5b0 | -11.27269 | -60.50093 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18b5a534-f748-314f-be56-dfbc7b0aff99 | -11.27203 | -60.50465 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6aa6a45-ab84-3af7-8a7c-b31b77c340d8 | -11.27135 | -60.50848 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4cacb8bb-f66d-3c50-8c78-1c792b1f53e8 | -11.27123 | -60.4858 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c27d9b9-8b3e-3fd8-babe-282c2764dfcd | -11.26999 | -60.41472 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 246b1538-254f-3fa8-9d0b-014be6a3a3e6 | -11.26804 | -60.50373 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3506461-4bbd-30bc-a6df-ccfc0e657fe9 | -11.26735 | -60.50757 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2730740d-d6f9-38f7-a7a1-2474f29856fa | -11.26734 | -60.50277 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db47e010-20d2-3e70-af8d-f953332cc19d | -11.2667 | -60.50653 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ed004a9-a14c-3fe5-a3ca-d598a715ac91 | -11.26605 | -60.36558 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2682cbcc-f8b9-3079-a109-8f3549955a40 | -11.26595 | -60.41417 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe598eb5-2074-382d-9866-6b70f5728cd4 | -11.26191 | -60.41361 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ef4c463-f266-3500-969d-f8977892657d | -11.26145 | -60.36838 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2eab9faf-859f-360f-970f-e16aca7d91ce | -11.25851 | -60.40939 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30cc8f5c-12ac-3983-9ea5-e80a9ace1783 | -11.25788 | -60.41304 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e1b7802-2126-33c0-b982-7d2e23af6376 | -11.25065 | -60.50314 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5539e292-39d4-350f-9462-934ed3504a76 | -11.23812 | -60.43153 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f0ce278-2f99-35bf-b6df-bbc17a3acc56 | -11.23751 | -60.43508 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c0f98d0-55b3-3f76-b3e0-7d80b41039ef | -11.22686 | -60.49637 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36bffb52-9e1f-384c-be80-c4c42aac75ca | -11.22219 | -60.49934 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de6192ce-62fa-3327-92a3-f4049c7bff04 | -11.1886 | -60.50094 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81c5b20e-550b-3bc8-9bd2-4dba4c2470c9 | -11.11911 | -60.46609 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e828f57-2e3f-3edc-9c0b-93c41a1e870b | -11.11445 | -60.46898 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b3211ad-feb1-3d22-ac19-7c79d763479f | -11.06174 | -60.43765 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7ae8914-3154-375e-abeb-84ae12471e49 | -11.06083 | -60.43753 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b8956a7-3f6f-37f9-b26f-2e6d7104ceea | -11.06021 | -60.44113 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f5282ac-9410-33bc-8b11-95513e105f41 | -11.33808 | -60.53134 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e743332a-0aa1-33eb-8693-72d7e4b7a466 | -11.33744 | -60.53501 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdb4265f-eafd-380e-9ee9-4f2aec7ed4c0 | -11.33406 | -60.53054 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9500c05a-ff52-3a58-94bf-9c0aea117d01 | -11.33003 | -60.52979 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3a6a202-3927-316f-86de-8dd96f5cdfa7 | -11.32066 | -60.53575 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ebe0a7e-fef4-3ae9-ad9a-440d88b516ef | -11.32002 | -60.5394 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ca4b00-7f15-3f3c-8e2b-e9b1b02abb34 | -11.2505 | -60.55247 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3d81acd-6d16-396e-91d2-3445b7713b4e | -11.22019 | -60.55878 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e5b763f-3c0c-359d-965a-63034e9d3481 | -11.1796 | -60.62328 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0375c0b7-f3ac-3bdc-9601-cc926b051ee5 | -11.17896 | -60.62691 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84c91abe-e59f-3719-a52f-3d779f625532 | -11.17832 | -60.63058 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a4804c9-7086-3998-a5fb-4931e6fc930b | -11.17554 | -60.62249 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02a6b3b8-c33f-3679-b455-cec26061733f | -11.1749 | -60.62614 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83c880ed-3966-3465-ad99-f0ea97ef1d40 | -11.17425 | -60.62982 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6dd9c863-4396-3a80-9741-3b1a834fcecb | -11.17083 | -60.62536 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fecd5d1e-706e-31e4-ab26-172af154a6d9 | -11.15793 | -60.62708 | 2024-10-12 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b40b1a2-acb1-3e55-a16d-70ef60fbe5f0 | -10.97161 | -61.08601 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README83.md)
