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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 869a2a48-0a03-361b-a45a-b6849dadbbff | -6.42801 | -44.49018 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d890e8a7-cd3d-376d-b996-73bd93b4225a | -7.84173 | -45.40314 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b81ba033-c5fc-39b0-a2f6-ef9df159b554 | -12.01372 | -47.58755 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ba2a0acc-783f-31ac-bd2d-a82002c2621d | -9.77963 | -51.09767 | 2025-09-11 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27fdd1e7-298a-3d8b-ae43-425b9157375b | -10.32464 | -48.81378 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e84c1907-085b-3814-9768-fdd0f61ff85d | -11.4787 | -43.65266 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ca804e4-4e96-3e05-9b56-a6b4df7a2e63 | -7.42842 | -45.87397 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a326888a-4ad4-3a76-ba10-f39148196faa | -12.05678 | -50.95028 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3dd0a7d-9541-34be-94fc-a2e4fb344de7 | -6.55308 | -47.50811 | 2025-09-11 03:55:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9d59d20-8bac-3f8f-bd91-9f67254678d2 | -6.40053 | -43.5054 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d0a67c9-e8c8-3481-9ded-afc3e713585e | -6.85341 | -44.89303 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f0a4e8f-bdbb-3ee4-8a6b-1e24e915de4e | -10.90099 | -47.76751 | 2025-09-11 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f3d1fae-53d2-3b5a-9c0d-0db57300e5bc | -12.05264 | -50.94012 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ee12964f-6d35-38f8-a92d-87f1e99ac312 | -5.40307 | -45.94234 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdf14bac-4e18-376f-8610-a9bf7cdb10b1 | -11.48167 | -43.65796 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9eb6f8e3-67fd-3892-b211-bfa5fd2ad5bd | -10.39461 | -50.51807 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c88509d6-ddc6-3593-b55d-eb6046baf785 | -7.81223 | -46.08146 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1c238d8-2d86-3d86-8bd6-7d7271d1ccc4 | -12.58705 | -44.78515 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46c6f2a2-1395-31c3-8cc8-a60f9a8c9ca8 | -7.50234 | -48.24614 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7964cb33-9ff9-3c85-86f0-0044f789c438 | -11.15777 | -45.31193 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bc4d94f-98aa-32f2-85d0-9d0dc48fb24c | -6.24415 | -44.80287 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7467e4b-eb12-32c2-9648-94da5ab3f3e3 | -11.47436 | -43.63276 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68a68cbf-f14f-3b9e-bfe0-357a7815a091 | -8.52582 | -45.69218 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eccb6efb-af1f-3bbc-b9fd-239c40acea3f | -9.72253 | -43.52343 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f0bd4e0-947e-3193-9ff6-bc891af8fbc1 | -11.45661 | -43.60109 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 42bf5c24-3b87-3d42-8c18-b5d4c3c1531e | -6.25691 | -43.49237 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dcdbec9-ab40-3fdf-b348-6e3fbb3d91e9 | -11.41806 | -43.54887 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f8e8f270-2490-3b3f-8c9b-8e83b559c029 | -8.5242 | -45.70159 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9389f545-2b87-3377-8e4a-e1ae0672dad6 | -6.59326 | -43.95327 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baa0a515-064b-3ec1-bb2b-6e7482a4201e | -9.08282 | -47.09251 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9f21304-9757-3481-8275-ce06c3fb1061 | -7.33446 | -49.60692 | 2025-09-11 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc23dcee-4809-39b5-bc96-5734da3dda45 | -10.7429 | -49.28443 | 2025-09-11 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fc3ab0e-2813-3e19-bfb5-9d818276e9ac | -6.36804 | -45.15899 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e4b5a35-16f4-30b0-8108-84ff0b6dfa2b | -11.47159 | -43.69452 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a19129be-cfba-3d4c-a984-cb146221773b | -11.04329 | -46.05257 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1ec203d-621f-3ece-9152-958bb796e365 | -6.56611 | -44.21376 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7d5166cc-c9e8-31b2-952c-a818d8f24fd6 | -12.30749 | -42.10315 | 2025-09-11 03:55:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f38e50b0-8014-3f12-a85d-fce11da330a9 | -11.48385 | -43.66788 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88e2e512-9d65-3626-a2e1-a3f33cac0903 | -5.97271 | -44.72192 | 2025-09-11 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a01ff72-28e0-3f36-a5d1-d215f642f0f1 | -12.53326 | -45.33157 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 253d3913-20b0-32af-872a-110f1924226c | -6.34647 | -44.07506 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32e52deb-ac4d-32b3-9870-d12a5f22e621 | -10.54195 | -49.88617 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70db4149-5c04-3f98-9d6a-661f60f27224 | -10.53623 | -49.88509 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbc6ba56-12ff-387e-8a46-bce334ae72c8 | -9.02484 | -49.52709 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e3d557d-b46c-3248-8867-0dab389967c0 | -8.51683 | -45.69075 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4478db7c-9bae-38ca-9a3c-d807a8826e03 | -10.55165 | -51.52123 | 2025-09-11 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 539881d9-a7e8-3773-9c30-d39bd82049d1 | -6.44091 | -43.0652 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1c93f5bb-ee40-3548-9e88-38df1c9eb2df | -8.43628 | -47.26637 | 2025-09-11 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c07dc4e-e155-3c59-a0ec-35412ddf76a8 | -6.64507 | -44.07506 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19ead887-6c3e-3654-b599-ccc642d1d902 | -12.07846 | -50.99667 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9a13e045-984e-3042-9345-0a9fc5f5b507 | -11.78608 | -47.32209 | 2025-09-11 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffdb8335-7837-3f95-8e2c-0089600add2d | -10.78426 | -47.78543 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca962bb1-f113-3de1-8b36-ac8e837dc3c3 | -10.54689 | -49.8913 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb374402-3c18-3137-a661-0fb384b98475 | -8.03875 | -49.05225 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 4c34b6dd-2543-37fc-b530-19f0b5b8c6ae | -11.46547 | -43.61695 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d96db522-e6e5-3eb7-8e05-6619150232cc | -6.24428 | -43.4938 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9382d69-692f-3729-bc3e-ed7d166fd5df | -11.17112 | -45.28529 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8004aeaa-587d-339c-9b56-593dccd95645 | -11.41212 | -43.53846 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be6d6d38-ccf9-324e-89fa-f5738ea565c4 | -9.60632 | -40.61801 | 2025-09-11 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 855df53f-36cc-3500-af13-99bcbab5eb35 | -6.45383 | -43.59035 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85d045f2-2eee-339b-b303-65e450e78688 | -11.35103 | -46.50112 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 53a5c90d-4b2d-30df-be72-93d77b753f2e | -10.54559 | -51.51873 | 2025-09-11 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0a6d5bf-581b-3f9b-bf62-6fc196154bdc | -8.16723 | -46.07558 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5994a4f-b8f3-33b1-a1d9-2c0ac3f4ca1f | -11.03237 | -47.61303 | 2025-09-11 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d760e83b-de15-3d0b-a738-89c2e8484658 | -11.10901 | -48.41142 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 562a07fd-195d-3058-b6c9-8bc842202ab6 | -8.17206 | -46.06871 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a66ca3b7-544e-3165-b5a8-524f95ef44bc | -11.30992 | -50.74431 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c89435e4-7336-312c-bac4-5e2e1c18b0f5 | -11.10694 | -48.43192 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d93a5b33-7aef-37da-bb99-ea13ad583b80 | -8.01458 | -48.65252 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00ec6b97-937e-36e1-a602-f335bf8d6b10 | -10.66878 | -48.62423 | 2025-09-11 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 325f73dc-6246-30a8-80f2-f18184c0c0cf | -11.47238 | -43.68986 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5e4bc99c-6450-390e-8a83-64f8338fee28 | -8.96525 | -46.07052 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc625afe-8fa8-3b8f-97d3-543af9a81a29 | -11.16237 | -52.03284 | 2025-09-11 03:55:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97957849-fd90-3879-a450-ff3c9fe3e9ab | -5.59679 | -45.35994 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b36275f4-f5e0-3846-ad04-994cdb859ea6 | -8.64252 | -45.72498 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0d2a89c4-7fb6-324d-96e4-8980f07591cd | -11.98777 | -47.59378 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61fa16b1-c370-3555-b1be-c6a51f62f42b | -7.46444 | -45.28476 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 862a35b5-e16b-3dca-86ad-0f272362f56f | -11.3669 | -46.54171 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| baeac789-7607-3820-bfea-a12f0c4f3bfb | -7.26245 | -44.90406 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7fe64f3a-7e34-3265-a652-22fcc3f6cefe | -9.84322 | -47.79017 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68c6b299-a4b6-32ab-b43a-75156e201b87 | -9.0667 | -45.70412 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70fd0cea-dce1-3505-8f86-d38afe59eb54 | -7.54073 | -44.66636 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 676d7620-b90f-3503-8377-15827cf09f70 | -11.65454 | -46.90759 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 72061a8f-3668-365a-ba2c-82603b20d1b4 | -6.3189 | -43.44136 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 65aa2b46-1f5c-3196-b6d1-8a8ec3fa1e61 | -19.88498 | -44.765 | 2025-09-11 03:57:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 662a9a24-b1c0-3a93-af5c-68a43463b834 | -19.99412 | -47.62832 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87c5a626-d9d0-360c-993a-765b1950a299 | -18.00033 | -47.10473 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b8843f4-b11c-3946-9e57-badd5eea600c | -20.00162 | -47.63433 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d82a8c27-8299-322a-bfac-f97b1e28f3ce | -14.5733 | -48.76442 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b801f095-a09e-38a8-943d-2404b43d8655 | -20.17165 | -44.62405 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b042895e-5490-37b3-b71a-1065670b8963 | -15.98381 | -42.98428 | 2025-09-11 03:57:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9802fd99-c9fc-39d2-8edf-8be058a69943 | -20.23992 | -43.57506 | 2025-09-11 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 064dc930-fa93-3523-a5f1-1a0a0e8d426e | -20.39804 | -46.27988 | 2025-09-11 03:57:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f771140a-d5a2-3366-b4f3-75fcf107219b | -20.91069 | -45.28999 | 2025-09-11 03:57:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 88f84a91-3dea-39db-8490-6f5e2e5c6b0a | -17.99844 | -47.10942 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2bd19279-1d3f-3606-81a7-591ca116b579 | -18.62478 | -44.26774 | 2025-09-11 03:57:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 068ab528-1b99-3fac-b042-acbf0a7aaa08 | -14.13406 | -45.40012 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efab7188-0a86-3d3d-9f19-1b5d1d0a77b5 | -15.80254 | -52.24439 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 14237fdf-9576-3e6c-b8de-18ad0c42c61d | -16.2846 | -45.6832 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1b12c3bd-ff4c-3a77-98b4-994e1004cb4d | -18.72958 | -46.87469 | 2025-09-11 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README30.md)
