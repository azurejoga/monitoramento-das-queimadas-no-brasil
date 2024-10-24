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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1931188-27cc-3c58-b16f-4df34e34bd8f | -5.92979 | -44.96328 | 2024-10-24 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1c1adf2-c32e-33e6-b744-1e3c7f375c00 | -7.42926 | -44.73124 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d1a8e763-30a1-300d-bf0c-5001bc2e02ac | -7.42883 | -44.72873 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df6dc2fb-b069-38a0-800b-545518792a2d | -7.42864 | -44.7355 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02e045be-b91e-358f-95f7-97feb4e6e083 | -7.42818 | -44.73299 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dd3a4fc-9bb7-3226-9b9c-3653722a8cf4 | -7.42501 | -44.73491 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 327d4bc9-6d88-3fb0-9a23-358553e6f740 | -7.42391 | -44.73663 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1155c134-1829-3b59-8a08-3b925e3beb71 | -7.4143 | -44.72652 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 80237748-5e64-3306-b648-d296b5e90453 | -7.20926 | -44.13949 | 2024-10-24 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c50b5a7f-dbff-3331-9e1e-669790f1de6b | -7.20551 | -44.13893 | 2024-10-24 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29c49785-dee5-3db2-bccd-1bae19f3577a | -7.20232 | -45.02295 | 2024-10-24 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec34e90b-c581-337b-807f-a4fd02a3f45c | -7.19348 | -44.72606 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e87c90a6-fc2e-32e7-88a1-421734a50c31 | -7.17866 | -44.92051 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ee9f73d-ab66-3a02-9ae9-b512dc06d55e | -7.17677 | -44.99814 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dccb99e6-99b8-3340-bc5c-a3ad79a22c34 | -7.1732 | -44.9976 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 960b4e3e-888f-3bfc-a1b2-ff54837b006a | -7.1536 | -44.81878 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9a4d7e8c-01cb-385d-a109-63a72842803f | -7.15 | -44.81822 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 328112d3-c6c5-34dc-9cc0-6217fad2ceea | -7.1144 | -44.982 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbe51a65-20f1-33f4-8fdb-7270566f7915 | -7.01314 | -45.03062 | 2024-10-24 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 85a17c59-b0d0-377d-9eb7-9422d1ed0b0d | -6.9987 | -44.57802 | 2024-10-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33c1dfd0-fab4-37d7-99d2-13262aeeae61 | -6.96656 | -45.12287 | 2024-10-24 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d268325-79fc-38fa-b664-6d65b7b60a23 | -6.87972 | -44.32324 | 2024-10-24 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b79449d-1be6-3b02-a1f7-ef2b32ba01f8 | -6.83995 | -44.38856 | 2024-10-24 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e67e185-b4c0-3e0e-ac16-0728b8af15cf | -6.82965 | -44.38484 | 2024-10-24 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7da5fe06-ea16-30b7-95e2-071f91ddd0ba | -6.82954 | -44.38265 | 2024-10-24 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2b622d3d-9c0a-3a35-8103-767e3b09d19f | -6.82891 | -44.38698 | 2024-10-24 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7612021c-d28e-3788-982b-3217f42823bd | -6.82596 | -44.38433 | 2024-10-24 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 06f583b5-69ed-309b-8cea-758176c6828d | -6.81702 | -44.46754 | 2024-10-24 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16caed05-fe99-3c9d-81f3-4056fb1c9756 | -6.81679 | -44.46981 | 2024-10-24 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4c0a9c8-5233-3406-8658-1d47b7047116 | -6.81313 | -44.46927 | 2024-10-24 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9bb203d-811f-38bc-a11b-a09560476bbe | -6.81271 | -44.47127 | 2024-10-24 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5622822a-77d5-38ce-a970-1400c41c3a6d | -6.80905 | -44.47073 | 2024-10-24 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd8f5e22-4e11-37cb-a326-cc195b287f45 | -6.80885 | -44.47301 | 2024-10-24 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ffbcb9a-eb05-31d2-b349-88da8572a1da | -6.72433 | -44.68709 | 2024-10-24 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 881b8c21-7d0e-321a-a885-503c4f9a645e | -6.72134 | -44.68235 | 2024-10-24 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7fa85b87-ceae-3d42-86ef-3f999bacfecc | -6.72071 | -44.68653 | 2024-10-24 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 069f8abf-0c71-3891-a1c9-b8da8abfccfb | -7.72192 | -44.62335 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf335ddb-4120-3b55-b902-0d7868d2767c | -6.58724 | -44.1773 | 2024-10-24 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 534fcf7d-25cc-3e6e-98b1-e5d3e9dc9bbd | -6.58658 | -44.18172 | 2024-10-24 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c778b90-89f2-33ba-bd0c-04785c4b2829 | -6.52971 | -44.5617 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15523b0c-7ba5-3229-92c3-5c9766494a6e | -8.79391 | -44.73521 | 2024-10-24 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67d23ddb-7222-3555-9620-a79945f3377c | -8.38229 | -44.48187 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a418e89-a64e-3efa-ae44-081de27e7c00 | -7.92558 | -44.88711 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70a0769e-1d54-3723-827a-a75cf8debf87 | -8.7989 | -44.72698 | 2024-10-24 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54a6538d-7c81-3636-94b8-5abc03f569cb | -8.7976 | -44.73579 | 2024-10-24 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f70cc8e-cbde-3689-948d-2deabf0ff733 | -8.79326 | -44.73962 | 2024-10-24 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e2be5a2-fd58-3a9b-bca0-c6007546f38f | -8.79825 | -44.73138 | 2024-10-24 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ee128c3-26be-3b02-960c-6b3d68c9c3e2 | -7.92856 | -44.89189 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f603ca6d-ef51-3166-bea4-3f4c9feaa3c5 | -7.92195 | -44.88658 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 973a928b-846c-339e-b66f-ef1fe9f2dd0f | -8.79955 | -44.72257 | 2024-10-24 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eaba9c72-7d3a-3742-a1cd-b1ceaacec461 | -8.79261 | -44.74402 | 2024-10-24 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 633cca6a-ed82-39e0-9f71-99081ec899ae | -7.93219 | -44.89244 | 2024-10-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7590681-f0dd-339b-95cb-1cc1d116c044 | -10.88752 | -44.60435 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e087454-a651-3840-bdb2-07a7df378a33 | -10.87537 | -44.60746 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f502ccc6-a9e8-3025-bc01-a63f938f11c6 | -10.72101 | -44.87397 | 2024-10-24 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43c8b125-0c3e-3166-b82a-f46803ee2ad3 | -10.59695 | -44.76878 | 2024-10-24 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 939fba47-2e47-30bd-a828-16b6c10c6a85 | -10.56162 | -45.1475 | 2024-10-24 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31e58d0b-d07a-3b2e-ad0a-8e81a9d013e8 | -10.5072 | -44.90692 | 2024-10-24 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7d2c130-fa8b-3885-8362-16989e0ecea1 | -10.49688 | -45.10736 | 2024-10-24 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82cf94e7-3e84-331b-b4c0-4b13a7229aeb | -10.49643 | -45.16162 | 2024-10-24 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa6136c4-a9f5-3b97-9516-ddf77163f1f3 | -10.37623 | -45.08732 | 2024-10-24 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1696f7d6-25d0-38aa-aa59-05dd35ca0801 | -10.37558 | -45.09177 | 2024-10-24 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 309ac731-33b7-300c-a99a-8d9c472e281c | -10.37254 | -45.08673 | 2024-10-24 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0994c257-5541-3ab2-af40-b7e1723079b8 | -10.36773 | -45.06796 | 2024-10-24 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e109f49f-b669-3bae-96df-fdf88ba6d891 | -10.36708 | -45.0724 | 2024-10-24 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 034edffd-318f-3e2f-a603-ca04430bc5f9 | -10.34365 | -44.69984 | 2024-10-24 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86290e83-5d1a-3025-8567-20537100235c | -10.11983 | -45.67023 | 2024-10-24 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b5f4510-856d-315a-b9e0-376cc98aad0f | -12.16996 | -45.1833 | 2024-10-24 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90356b07-e20f-36f2-8722-142fc1a6f046 | -11.82681 | -45.17738 | 2024-10-24 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d54ae10b-68df-3915-a269-9ade353f162e | -11.62804 | -44.96885 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b65352ce-607a-3b89-99b5-fac919e313f4 | -11.62705 | -44.92047 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 422844c6-edc5-330f-b9cd-caea79b8bcc4 | -11.62679 | -44.92335 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 635e2ba8-5efc-3d67-89d0-ddcc6865000d | -11.62638 | -44.92525 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4de2e5a1-9f0a-337d-b179-e42f729e612c | -11.62326 | -44.91988 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e13dca5a-6b81-3b23-8ae5-adfbb6b28f73 | -11.62301 | -44.92275 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 488a9176-e646-3aae-840b-5232b61aaab4 | -11.6226 | -44.92465 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4bce7ea-7457-3078-94bb-98daf6008f9b | -11.61923 | -44.92215 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd51e0be-9c0b-35dc-88c7-6f405502bbda | -11.61882 | -44.92404 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bdb1c7ab-ed23-3e50-8ea6-d604f44afa15 | -11.55661 | -44.84513 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 482dc84e-f9b5-3bb7-931d-37698597f0bc | -11.39632 | -44.96851 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80f0201b-cbd1-365a-96cc-37a9c4ea1e13 | -11.3961 | -44.9663 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7fdbe60-4bf8-3d3b-8958-b1764bbc73df | -11.39539 | -44.97114 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08ee6136-4c79-3197-94b0-718b1fdbd1b6 | -11.30118 | -45.01251 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 814f8e60-c0ba-37e2-b216-f63d3e265524 | -11.13194 | -44.9495 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49fdbcbe-15fa-3653-9f83-56d58df729aa | -10.95957 | -44.61252 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6db62b97-ab9c-33fd-b508-2b4c52d1c13b | -12.95038 | -46.44342 | 2024-10-24 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59df53fe-173f-3afe-a44e-ae2056e24ca4 | -6.03019 | -46.5469 | 2024-10-24 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db52d2df-c052-3527-bc05-800944589be9 | -6.01488 | -45.96568 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 752b0afd-8760-3e04-8202-f725e190b8a0 | -6.01147 | -45.96519 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d61866f-8bd0-37bb-a401-d33d946da728 | -6.01091 | -45.96883 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04cde699-159f-39bf-b5ec-949b1962efd2 | -6.00807 | -45.96471 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7985299-e5dc-36ac-a77b-93724688f86f | -6.00751 | -45.96835 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 159563c4-72ab-3a4e-a3a7-562f9da4f476 | -5.74419 | -46.46306 | 2024-10-24 04:34:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d9c44ea-ae94-3287-9082-d1794ae94245 | -5.68373 | -46.36638 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad5d327e-48cd-3bee-9d95-4d88a2d2bd78 | -5.67393 | -46.45224 | 2024-10-24 04:34:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d332f48-8489-3b1d-9142-498aa380694e | -5.84335 | -46.237 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6dee3f86-2312-33a9-b1dc-6bd0a32b84a5 | -5.7663 | -45.55246 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de6ea0de-d549-3b3f-8ac5-2191a5c13bf6 | -5.66858 | -45.80068 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b020b9b8-72d0-31e5-ad75-1e1d672536c3 | -5.66802 | -45.80438 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb585999-e413-3108-9e07-577dfdaef21e | -5.66461 | -45.80385 | 2024-10-24 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README42.md)
