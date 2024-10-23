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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dee23e1-2496-3d88-86cf-997dbdcb0b06 | -2.57806 | -54.01528 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 76e1bc08-0cec-3bc6-a4a5-18d8533c9a08 | -2.56708 | -54.01747 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f068fad7-1964-3e51-af6e-36351043c4b2 | -2.5239 | -54.24284 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cf1a6a0-50d5-3175-aa4e-501f640043dc | -2.52041 | -54.24229 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 647bd272-cc89-3814-b124-e204d4e380ed | -2.62508 | -53.96436 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83120649-000a-32ce-beeb-e3c010b6afc7 | -2.62163 | -53.96382 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8484469-b880-31d0-83c4-850333e30bed | -2.57521 | -54.01095 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f3c2967-de0f-3e91-ac27-35f93ed8f10a | -2.56483 | -54.00933 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc1ea37e-8f17-3a6a-9a74-19889756250c | -2.56422 | -54.01313 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2766633-79ac-35df-b30f-800cdd61f6c5 | -2.56198 | -54.00498 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d128e4e-5b88-3e96-a4f8-b6d71b7483be | -2.51834 | -54.10877 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6991e1f7-0437-3aae-913c-5d4c158698f0 | -2.51762 | -54.1041 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa0575f5-9b60-3d46-b31b-66b4bfac25b6 | -2.51701 | -54.10789 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6cef927d-2a74-3488-97ea-0acb1ff9de50 | -2.51546 | -54.10443 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74ab7f00-1800-346d-b956-38113e699f1c | -2.51487 | -54.10821 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 002a615c-505f-34d8-b273-552f827e31da | -2.42528 | -53.89588 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 133ee021-0ec8-3d30-91b1-90a1ff8e3600 | -2.42183 | -53.89536 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cbd24135-7e2f-3398-b7a6-9f1d0a7a4e27 | -2.26872 | -53.64164 | 2024-10-23 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fda3d2e1-a8db-39e0-a5c9-8b6d733dbea2 | -2.16668 | -54.41092 | 2024-10-23 04:51:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e13eb3d-c8f2-37f8-b74b-05baabc2737b | -2.16604 | -54.4149 | 2024-10-23 04:51:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87db7e55-f390-3e50-856f-d77415a0ec6a | -3.59182 | -53.78186 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab2c715e-833a-3484-9eff-67414e9d5af1 | -3.59123 | -53.78555 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 451b6091-c727-30ab-aaf5-fe932f0ed3d1 | -3.58841 | -53.78136 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1248cfe0-6532-3d9a-9684-cd3c54682480 | -3.585 | -53.78088 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f3f4f9a-cc3b-38fb-b257-67764efda5b3 | -3.58441 | -53.78456 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a76d3ea-9775-3a73-bb98-31a1d82b375e | -3.581 | -53.78407 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 035f435f-15f4-3e86-8775-4be3098051a7 | -3.06715 | -53.83364 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8d3ed8a-d603-359e-979c-b9031cdbcb60 | -3.65615 | -54.21621 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b06f8b1-69b1-3a9e-9729-3d2048006cab | -3.6527 | -54.21566 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e3517f2-57d1-34e7-a308-7f3bd95d78f4 | -3.6521 | -54.21944 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 203f69b0-a32f-31c5-a517-313c9cd2f684 | -3.64926 | -54.21506 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 339ecb86-8224-32f0-b747-9f9ab3a3a262 | -3.63618 | -53.96683 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c684ba43-aed3-39ca-b234-0f0dfd992d84 | -3.63557 | -53.97057 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fe7bb42-32bd-3e2c-a68f-061696bb5993 | -3.63275 | -53.96632 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9c3b6cd-b2ce-3495-b9aa-ccf53c0922ee | -3.63215 | -53.97007 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4eff9c4-81c8-3f44-ad6b-4e88a9e0fda7 | -3.5437 | -54.74016 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 42578f9b-2e4c-3226-803c-21cbb628fd00 | -3.54306 | -54.74416 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f64907f-cdb5-357d-bf18-e1dced68ee97 | -3.54017 | -54.73958 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 2c356256-78cf-3175-8ff3-3b599bd9dfbe | -3.53952 | -54.74358 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 679a9d12-d69c-3163-bff6-653b19ddddcf | -3.53663 | -54.73901 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 45960e16-2d6a-394a-948e-506e2977789b | -3.50029 | -54.02621 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2a410b6-283d-338e-84eb-f1fa8fd2f7fa | -3.49107 | -54.15203 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b8f45a3-2908-3619-abd2-6e2c30500df6 | -3.49034 | -54.15146 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c258bcb6-974e-3cdd-8ed5-67f4eab14326 | -3.48762 | -54.15149 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b0204467-d304-38e0-8d4f-097a1e085f44 | -3.21962 | -54.86077 | 2024-10-23 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fb2312b0-84d1-3d4c-b615-4eab8339776c | -3.164 | -54.80251 | 2024-10-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef2fe549-67aa-3f67-ad3e-f4c478554d0c | -3.13711 | -54.28125 | 2024-10-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7db47629-8f09-3375-93f9-c42a272ebd41 | -3.10894 | -54.16697 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2188aa37-3476-32b1-8184-a7a5850e1ccf | -3.10834 | -54.17075 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e611467e-ca4a-3f49-a545-626966877e4c | -3.10773 | -54.17456 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26793275-b571-32b0-8836-ded33ea8d916 | -3.10668 | -54.15889 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| fa28c28e-87a1-3897-99c3-6f028deff635 | -3.10608 | -54.16266 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3704c564-120c-340e-ae60-fa962614550f | -3.10441 | -54.15082 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f834ab6d-d1a1-3808-930a-0e6e2453ac64 | -3.10427 | -54.17401 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa17b9d2-0bdc-3d1d-b782-45889defaa2e | -3.10381 | -54.1546 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a573c791-fe75-3acb-89c9-67ff6ec6f71c | -3.10366 | -54.17782 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eddc3b05-b9ce-36a9-a70a-2310946010a1 | -3.10321 | -54.15837 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| a16bb117-b105-33a9-972c-a80f22644ff8 | -3.10305 | -54.18165 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b55d798-18d6-38dc-87da-d4a66d007362 | -3.10141 | -54.16967 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 92b4b0c3-8ffc-35d7-879b-7c13ff054adc | -3.10095 | -54.15027 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9cea1b78-dfb7-393b-aa37-4df580852d12 | -3.1008 | -54.17347 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dffac897-1f81-30b8-8e88-cb2e0c29a4fd | -3.10035 | -54.15406 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a0d6981a-5e2a-323a-87fa-2fe524906ece | -3.1002 | -54.17727 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a7ff12a-0fa2-34f4-87ad-ceaf37aa592e | -3.09975 | -54.15783 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39e332be-360d-32eb-ae34-f04edb728ca4 | -3.09959 | -54.18109 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0c8278d-1c90-30f7-8a62-573e1290bc17 | -3.09915 | -54.16159 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ac4215a-01c7-37e7-9f7a-4b4737fa2757 | -3.09794 | -54.16913 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eda2470f-70de-3fd6-9fe5-6bab16c55770 | -3.09688 | -54.15352 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e07ed7f3-71eb-33c6-a085-a60c4d8d8d77 | -3.09673 | -54.17672 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aab06cb8-7d33-3206-8aac-89f254dd3c25 | -3.09612 | -54.18053 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38d39363-4c05-30d3-820a-5e6f5f322c18 | -3.09568 | -54.16105 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4ce0e99-0c28-346f-9ce1-e483d1bb5e73 | -3.09508 | -54.16482 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c3d0aee-7e91-3dac-85fa-340606083b3a | -3.09448 | -54.16859 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95fd0ffc-8183-371b-9cc8-fc698119de1e | -3.09327 | -54.17618 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e35d77a-bc01-3fd5-bb0e-41e2b8f4b00f | -3.09101 | -54.16807 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79136a40-a934-3822-92a6-526db6893b46 | -3.08815 | -54.16377 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b15d97b-0311-3f95-ab88-466f5e8ecd4e | -3.08286 | -54.17458 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b92fc95-7c3a-318a-995d-e6f899f2c43b | -4.30998 | -54.7588 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 192aa04e-07bb-30e0-a4a8-afc2227d742a | -4.13143 | -54.89871 | 2024-10-23 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5c20b97-9aa6-3c55-ac8e-b05fa56266ea | -4.11547 | -54.41489 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d751618e-5c55-3513-8c35-806433c5130c | -4.02718 | -54.3976 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fdf6880-6888-3644-ab37-6794df92c451 | -3.9298 | -53.86466 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28a98069-c3a7-3e36-802f-824aad1cd565 | -3.90328 | -54.1423 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 030e440e-e470-32f8-a47d-f72c0c4579d1 | -3.89985 | -54.14178 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d300560c-36e4-3866-b3f0-d0d892930b45 | -3.88953 | -54.14017 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2d67ef0d-f751-35a0-b570-d33fa02601e5 | -3.88893 | -54.14393 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 841ea517-1190-3183-90fa-f1c307418822 | -3.88609 | -54.13964 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07874354-26b0-3435-a5e0-eabd7a728548 | -3.87448 | -54.62453 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4e4d48c-8ecf-392f-96a3-f10c651c1872 | -3.85671 | -54.08123 | 2024-10-23 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d75eed1-c355-336f-823e-bd193fbb70e1 | -3.85156 | -54.76631 | 2024-10-23 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac11fb12-abc4-3664-ae96-b74f5766507b | -3.82909 | -54.23109 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 657ac391-a311-34cf-97b8-c65bcd681481 | -3.79816 | -54.44532 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 886eb9ca-8850-3e26-9126-ca302f61a155 | -3.78314 | -54.38382 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d948e3e-b9bd-3071-a857-218866f603e2 | -3.70229 | -54.25402 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86cba628-117d-3f85-ae87-3736bc5612f4 | -3.67945 | -54.55057 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b2f93cc-9e1f-34d1-8599-279d7004d20c | -3.67596 | -54.55 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dd3c9b3-628b-3581-9081-39f1a852cc7a | -3.66567 | -54.4257 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dc6ec25-81f8-37bb-9616-9002f76d379c | -3.66507 | -54.42954 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99b8ed37-7cae-35b4-8859-8493b490baa9 | -3.66393 | -54.42498 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86208942-e559-310f-bd2f-06e3f4fc4ea4 | -3.66331 | -54.42881 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README43.md)
