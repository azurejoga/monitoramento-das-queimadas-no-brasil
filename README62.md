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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6bd8d9b-acf4-3532-9bbd-b894333cace8 | -10.80589 | -48.80541 | 2025-10-08 04:38:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d3f6503-6b15-3f24-84dd-802c42043266 | -10.41699 | -48.09626 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2666f463-1f0b-344f-9447-80e7e8d2197d | -6.29009 | -45.32999 | 2025-10-08 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8df78a31-3585-3f74-b01e-4eb9a3ca186f | -10.64931 | -47.80132 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 478dfa89-5c4d-37bc-890c-18a42944ead7 | -3.59571 | -48.98591 | 2025-10-08 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3efd2cd6-7ff5-36de-aee6-cf27e2f70879 | -8.41002 | -46.80744 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42418387-7bf0-3f75-9298-799a8d245d53 | -8.39903 | -49.74107 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad4c7561-b0c3-3444-a1d9-7d94f9b5ed64 | -11.78135 | -45.14417 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02f1f628-0409-3604-af88-e3cf906b4c14 | -5.13592 | -44.95558 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4bbfbf0a-f457-325f-bfbb-df2d8409221a | -7.2458 | -44.14933 | 2025-10-08 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4069961e-fae1-333d-969f-7bec6da377cd | -8.22799 | -44.19277 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 21ecf0ff-28de-304d-a2e1-dc39fa95c254 | -11.21658 | -47.7745 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 411033cb-fbc1-3a0d-a340-03c161f9ba5d | -10.04619 | -48.2824 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b26a7a49-ada2-3963-9f49-97eb35415747 | -5.61 | -45.19621 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98ad166c-982e-3a25-a090-a69cc478fee4 | -8.4697 | -46.29233 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ded1b47a-d97e-3e84-855b-4f8cde97e44b | -5.39941 | -45.64026 | 2025-10-08 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a584d25a-9152-3470-ad68-f2a1942e88cc | -4.43587 | -48.00764 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 152727b5-b1dc-3ab9-8fe7-09f3218835e3 | -5.59312 | -45.84039 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da92b3fa-dddd-3628-8eef-687da1e788a7 | -10.46906 | -47.81962 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10cf1605-3f38-39f7-b9f9-055dd730d1b8 | -9.11908 | -48.75956 | 2025-10-08 04:38:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f3182f9-eaab-35ab-8257-9ffbdb57e105 | -9.77617 | -48.28395 | 2025-10-08 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c81163d8-53d3-3a20-9f4d-8c4999bc616a | -6.66584 | -41.38294 | 2025-10-08 04:38:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 98524de8-ffce-3227-8453-1f431ef8f333 | -5.487 | -44.61592 | 2025-10-08 04:38:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79dbf6ba-7afb-33a2-8d0c-95da39a08800 | -5.39197 | -45.20451 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78e47fdd-b038-3e85-a919-2f3f103e8d83 | -11.8023 | -45.04342 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f2afe13-611d-3697-b097-f3a43e136dfd | -5.45396 | -45.87264 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3874b26a-2626-3e1b-82e0-82599dad206e | -4.68683 | -49.49874 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5352e957-b5b9-3cf6-9244-2b2fea0132e6 | -5.76028 | -45.7492 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e97ec46d-1cc1-3aa1-9b27-d5e6461a64f5 | -7.24609 | -48.47325 | 2025-10-08 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a1b261de-d7bc-3cd0-bbf5-b75a98f28b06 | -10.0451 | -48.28958 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 215b578e-647c-36df-90a5-5fed71f8c872 | -9.77449 | -48.29492 | 2025-10-08 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66387442-ab7b-3d32-8b7f-38d589926c33 | -5.61405 | -43.94239 | 2025-10-08 04:38:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c70b3195-6b6b-35b0-984c-7d684dae15ba | -7.76138 | -44.19984 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be91cb82-f1c2-37a4-a028-120f6bd7c251 | -4.43974 | -48.00466 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7965179-24ea-3c62-9e31-446fb9856211 | -6.42427 | -47.24127 | 2025-10-08 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8ddbb10-1169-36d9-ad15-b29d6b924a8a | -11.78993 | -45.05386 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93595c14-33e1-3256-8528-383ebdaf9ea9 | -5.13455 | -44.96478 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a97556e7-da11-339f-a43d-8a6fe72922a2 | -4.48315 | -49.71305 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 91e70918-341c-371e-9f94-790fe045c11f | -6.72553 | -58.58929 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cad13f98-3724-37a7-9ef0-8ccc075adace | -7.47405 | -43.13276 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f3e1d5e6-dc1d-3c2f-9335-8bb5869e624a | -11.76956 | -45.13865 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06192c38-947b-3246-967e-9f3da8f0b48b | -5.39301 | -40.9855 | 2025-10-08 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 848926c4-29a5-3d70-9d5c-e3f7861ed319 | -11.05946 | -47.92601 | 2025-10-08 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90caa478-19c6-317c-a62b-279ef658defa | -9.08718 | -47.95999 | 2025-10-08 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e8a1e05-69de-3785-985d-570a7f46da0d | -4.78046 | -45.73196 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65e06941-abbd-394a-8303-8d38676ff1e3 | -7.80092 | -44.21758 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f789e13-8a79-37e2-aeae-a08f6a836774 | -8.51872 | -46.23564 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85bf5ece-1c3e-3f1b-9c13-9129dee6c599 | -7.80944 | -44.2454 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cfe7711-9c0e-399b-902e-a62f65620b6f | -10.41114 | -50.22796 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a3020fc-b22b-375a-803a-8d55eb8a4f3b | -11.22068 | -47.77104 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6e90d56-92d3-3eed-89e1-64cfaba8ffcd | -8.37544 | -47.05701 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c22ff13-700d-36a1-83e8-a6447a4076e2 | -4.58211 | -47.70651 | 2025-10-08 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33cbba9d-8276-3371-ad83-cc742822e245 | -7.68432 | -42.40446 | 2025-10-08 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7719d810-f56e-3b2a-b331-9b8072083bcb | -7.81886 | -44.18179 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 31ff9bad-8f4c-3375-9086-b075160ed538 | -8.53833 | -46.23021 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa98c342-7bf6-3d39-a97b-32a43a82070b | -9.93517 | -47.4496 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b98d3e17-ac1e-3001-8499-e7bfa1fbadca | -9.79481 | -47.74114 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 05fe80aa-cf55-3d12-9532-c3a1f3b422ca | -11.22137 | -40.47087 | 2025-10-08 04:38:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b88afe7-ed70-336d-a920-8483214e7d91 | -7.01421 | -49.71237 | 2025-10-08 04:38:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58919f09-4601-3dbe-a5c7-960b0498d7f9 | -10.8081 | -48.58735 | 2025-10-08 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fdc6776-e74c-3d92-ad1b-560119c6b5ca | -4.50425 | -46.36218 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 61b64ba1-8a4c-3660-b0ed-60666902823f | -4.87449 | -46.82388 | 2025-10-08 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bce41297-4760-3541-9e3c-58e121943eb7 | -8.52671 | -46.23249 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9aaf1fd-2da5-3849-8c74-6d3627e71d2e | -4.85385 | -45.75993 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71776d14-201f-3bac-86f1-d9df24352749 | -3.69791 | -49.41354 | 2025-10-08 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27d01d19-2963-3eab-8186-907863696aef | -9.97582 | -48.30654 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64b21512-23e5-36e2-a7e8-e4058e83244b | -10.61239 | -48.69699 | 2025-10-08 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 479b5ed3-8730-3415-a756-a97a65c9a805 | -7.76609 | -44.19639 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6a8fded-5fd6-365d-8cd3-867455769a53 | -8.1736 | -43.32711 | 2025-10-08 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3ab2037d-399a-3658-b732-24efa18f0749 | -11.77315 | -45.14289 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b272d4d5-7ee0-3ebe-9cc7-ac19a667340d | -9.17795 | -47.82243 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6a1ff91-707d-3435-8e6d-248b2cfe353e | -6.36956 | -41.61671 | 2025-10-08 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| baf5c764-9a83-30ac-a1d0-baae69d06e5b | -4.50016 | -46.36547 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| befa62fc-d53d-398e-9636-19e5e33b0e84 | -5.40745 | -46.22613 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3da48f13-0b8e-306b-ae96-ad28bb5e0b54 | -6.71452 | -42.86263 | 2025-10-08 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 41f7f66f-3f0d-3418-8878-7dafcfd5bb56 | -5.81909 | -46.74438 | 2025-10-08 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b836629-0616-3ed7-acd6-a77b4ec1425a | -9.54753 | -48.22297 | 2025-10-08 04:38:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01a76a4f-aa8a-396d-a52b-25772ed0ef85 | -5.74219 | -44.40387 | 2025-10-08 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88994e54-0c06-30c6-bf3d-3d7a836c5cdf | -5.73045 | -43.61187 | 2025-10-08 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4fb40195-78f6-32c9-953e-705e57dc3cef | -4.40599 | -49.76903 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 022741a3-bfdf-3574-9943-f60ab0e10a58 | -8.51968 | -46.28028 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e52695a-a9e2-3f69-9cb1-7f40a2f86b2d | -4.68027 | -49.6045 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61ecb4f2-70c0-3640-9fb4-e20fb1653fe9 | -4.00752 | -46.97061 | 2025-10-08 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77c3d12d-b26e-35c2-a031-160a5ab9ff44 | -3.83694 | -49.15891 | 2025-10-08 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d50badca-8d1e-307c-b88e-75797fcc0769 | -5.86537 | -44.3008 | 2025-10-08 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19a56447-b2a5-3c8f-836d-63da9439187a | -9.09061 | -47.96051 | 2025-10-08 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dbdf562-e008-31b0-a3d3-a0dbaa731b1b | -11.47442 | -43.48733 | 2025-10-08 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2e109d3-3c0e-3806-b8ff-82ca5af597af | -8.46952 | -47.20295 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37a705c5-852a-3000-8b9f-ca888db92c9e | -6.45869 | -44.57426 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82b03e6b-0c0a-395b-973d-a6474c4e8da7 | -10.40831 | -46.58338 | 2025-10-08 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63b0192d-58c1-36ef-b2e7-6b743aaf70e2 | -10.37641 | -48.13667 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 248f6f0f-c973-3c81-8fe8-a1d9bfab59be | -7.78556 | -44.20745 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a14d69b-d9e3-3948-96ea-66fd3246dd5a | -10.04907 | -48.28642 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 782e82af-25a4-3977-9785-8a506dd79b3d | -9.19403 | -47.80946 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abcc5781-760f-3cd3-8ac1-9d14ff915d24 | -5.34288 | -45.8652 | 2025-10-08 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cc855a9-e75a-3421-a424-96077c613ffd | -7.59213 | -49.64462 | 2025-10-08 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4ef566d-c89b-38cc-8943-7b6bd8aabdcd | -11.79366 | -45.11651 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e177a70f-c70e-32d6-84c7-890e11c392f0 | -8.22409 | -44.16116 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82c914b2-5f80-31ec-aa3d-5f42a7ed1678 | -7.38023 | -47.03808 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3437dd66-cc64-31e8-b47f-8a77fe87dcdb | -5.40685 | -46.23004 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README63.md)
