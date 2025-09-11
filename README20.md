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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0980e7c1-cd08-3f78-9cc6-a20aa803881c | -6.08945 | -44.78083 | 2025-09-11 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bd95846-cf63-3928-8e8e-7adc23979593 | -6.59262 | -43.95702 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 673fdcef-e067-346a-8618-3449168303e2 | -13.23222 | -40.95226 | 2025-09-11 03:55:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9b1df860-301c-3d26-90fe-e51c7ebc5c25 | -8.44126 | -47.26735 | 2025-09-11 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6790c5c9-75be-3b67-97b9-858176482cc4 | -9.0809 | -46.96602 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2c37b960-9bf1-345c-a2ee-5fada6e010ac | -12.43075 | -47.81272 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d56f252f-1c1e-354f-93ce-8adaecb4f840 | -6.90774 | -44.55431 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2339129a-d966-364e-aee3-96a3044eab68 | -7.33368 | -49.6113 | 2025-09-11 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8852d6e-bb28-363b-9dd5-44893e451f2f | -7.47774 | -45.28714 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28eca96c-f8e3-396d-871b-db0fe181a021 | -11.34545 | -46.49672 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8ac8aff1-771b-3588-bd2c-1178389951d6 | -10.38777 | -50.52141 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 695e4345-07a2-3616-840b-f671375e7631 | -7.88362 | -46.04628 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02437ae7-218e-3917-a34f-efee3952166a | -9.76058 | -47.84907 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7943873e-e5be-3a30-8db5-fd9ef147506b | -11.42902 | -43.58221 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cad5aff-2b39-3773-bcde-4787b76b3023 | -7.92698 | -44.87888 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74028352-a342-3d47-beec-a46e33f27d06 | -8.58532 | -45.58652 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5701d631-4f6b-3089-a157-7a4574fb55b1 | -11.47924 | -49.25576 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2e893c9-745a-37ac-b195-e5668478e942 | -8.07399 | -50.17937 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fbaabd48-7803-3e64-a566-a7c9d35c0b25 | -9.01339 | -49.52483 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5497e278-1989-385d-8714-4db1053f5a67 | -11.50705 | -50.39071 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da2de6f5-1a90-353e-b842-c0e1e6d1ce16 | -5.72941 | -45.41314 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66351399-0a51-3a29-a9ba-23c3f5c7f11b | -7.79201 | -50.7683 | 2025-09-11 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 51dc355b-0bdd-36bd-a4b8-ec152cc155bf | -9.05911 | -45.72144 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 27898197-6a03-3a3f-a0a5-aaeacdea30b4 | -11.71512 | -50.64812 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a903dfc3-2942-3d7b-8da7-3a498f46cd12 | -11.50046 | -43.66115 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 206948b8-3ac0-3b88-8b79-f5c197a2bc63 | -5.4292 | -45.87613 | 2025-09-11 03:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f12a04b-643c-324f-9967-0801e3031d9f | -11.41135 | -43.54302 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bdc9e24-b68b-3479-a784-cb81bdd2bfd3 | -7.78491 | -50.77124 | 2025-09-11 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ef52abde-b7fd-31c3-af86-5f8c05b423b2 | -7.91975 | -44.86947 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd8eddc3-49ac-3a7e-89e3-cac61a4c7f17 | -7.55911 | -48.20962 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88e13b04-03cb-3779-a8f9-84dd21582c51 | -8.79562 | -48.09325 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10dbe007-eba4-3ee2-bd66-f7e0d2f0e2e6 | -11.3428 | -46.49524 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a148e61b-b5b8-3d2c-935d-bbf77174f8ec | -11.0789 | -51.32976 | 2025-09-11 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 04412100-0c33-37b5-a473-59fb7508b4ac | -10.3164 | -48.79866 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d7312439-27e0-3758-99ac-d6ddded5f155 | -10.39373 | -50.52254 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9c8c3e04-78d7-3032-b28a-778560239c3e | -11.14524 | -45.28554 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a3881ee-4cc0-3f40-9113-ecbd45fa9274 | -10.311 | -48.7979 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aabc58fc-86a5-3213-9567-97c885ae7f0a | -10.56226 | -43.66362 | 2025-09-11 03:55:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2391da7b-8a6f-3cc2-abf2-6afa7d853986 | -9.46173 | -46.74189 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfcc068d-d008-3b79-a14c-cdc7f6a727ab | -6.41375 | -44.39322 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07d01955-d94b-30c8-9705-f477a259b337 | -9.15228 | -46.05595 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02706a6a-2f31-3398-84a6-b48391224639 | -6.44846 | -44.05364 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ced83bb9-0e96-392f-b3ed-54a154b50dfc | -11.42256 | -43.54495 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9df7078a-ad6c-34ef-913a-bc72bbdca689 | -9.06909 | -47.04089 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a188e869-cf9e-39eb-bbf4-2e6fef88c333 | -12.03737 | -47.5392 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fa248c0f-509b-3746-96f1-0bec16d932b2 | -12.14253 | -44.85893 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01d8c55a-50e1-363d-9fe7-942151d810c8 | -9.02758 | -49.77163 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f4dceafd-9eae-3123-a8a5-7d4fbcab80a5 | -7.3366 | -39.30899 | 2025-09-11 03:55:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 008517fe-d76f-3327-8cff-e4b6db79ac5f | -6.72928 | -43.02243 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b34cac9d-30fa-3b41-bba4-8ce44110e31e | -11.42608 | -43.57697 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5e4270c-a3ef-326c-8455-e0ea41dd46fe | -9.83818 | -47.78922 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9acb1ff7-9153-31ad-aed3-810852d6ae40 | -7.41919 | -45.87224 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c934ebef-f146-38c4-b252-866e9409e601 | -6.24854 | -44.80353 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2822f4f-4ebb-39b0-9851-979246524732 | -13.26464 | -43.77617 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e857bd0-5041-3cf4-a60c-667acec23d58 | -7.32401 | -44.38285 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa733141-80a0-3b3a-bce6-edfe2614d020 | -7.2348 | -44.47341 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0c3a487-061b-3557-b8cb-e96f10bac01a | -11.35468 | -46.50658 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8b92119e-71f6-387c-89e9-a21a719ea8cc | -6.63556 | -44.08096 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97259057-5dd7-3cf4-9227-4f5256746a1f | -13.34656 | -43.99889 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b20b7ecf-a7c5-3d61-86db-a5fc79cea0f2 | -8.35047 | -45.06194 | 2025-09-11 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2e7e32e-6df5-3940-8f39-8573261e49a3 | -12.13201 | -44.87194 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f2172c03-72c1-32f0-a781-aed92cb65ff9 | -12.13366 | -44.83901 | 2025-09-11 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8d6d4e1-48d1-33fa-90c8-7626331050ca | -6.83431 | -47.90769 | 2025-09-11 03:55:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cfc945a-2724-3db0-b360-50aec151c6f5 | -7.87678 | -46.72825 | 2025-09-11 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad83b1e6-abb4-3c9e-a3d9-18b2d3070f3c | -11.68473 | -46.89865 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 33154765-2f6c-3839-9cb4-d37d0e24cec9 | -6.90384 | -47.9062 | 2025-09-11 03:55:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fb3e2a4-fc11-370c-8487-7d0e28980d2f | -11.4714 | -43.62745 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e60236a1-98b4-3d3b-a091-37ddcc659b9c | -7.64162 | -49.81216 | 2025-09-11 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f3c0a9a-e7d6-3177-ae47-a0121cdf5fd6 | -7.48448 | -46.09531 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16301f2c-ab3f-3dad-bd5d-a47f3bdc158f | -11.49701 | -50.38132 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9062a45e-1802-3e13-b6b0-f5d9a26360a0 | -6.15708 | -45.81757 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 117b68d9-bfcf-34f8-a06c-b4e6a1a243df | -9.80236 | -47.76275 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df7f5d0b-6ba5-3d3d-91e5-fbb53456e7b5 | -6.25037 | -43.40863 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dcd1639-f8ab-3bb7-93de-ae277e6d6af0 | -7.5471 | -42.53257 | 2025-09-11 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 44e9bb35-c7bc-3af8-94b4-528aed4fb0d6 | -9.07895 | -47.08609 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d147d99f-4189-380c-9837-1f7da7ab93b7 | -7.04971 | -41.41771 | 2025-09-11 03:55:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 65dce8ed-dc16-32fa-b3c5-f226b0a02c27 | -10.4807 | -49.3721 | 2025-09-11 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ebaa71f-36f7-3629-bcbd-2520c2552c75 | -6.16348 | -45.80822 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03569d9e-f673-3228-ab8a-1c0eb8380cd1 | -7.11363 | -50.7635 | 2025-09-11 03:55:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09d78cbd-a52f-3eb0-8e95-6fff43d2d0ca | -11.36604 | -46.54643 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 737ac03d-73e3-36b9-9dd5-9f96effd236a | -9.75549 | -47.84821 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51ea47ce-6128-3096-a4bc-3b970d595b05 | -12.31094 | -42.10373 | 2025-09-11 03:55:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a321b409-3bb4-3bf8-8457-10b8a034cd53 | -8.73096 | -47.09729 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| cce8db40-122b-37de-9198-6fa304928b07 | -13.26852 | -43.75383 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70308819-b980-3609-a57c-c066d6928069 | -10.21793 | -39.05145 | 2025-09-11 03:55:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 291b29a3-c5e2-35dd-a711-0a9142f998ba | -6.17621 | -41.07687 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c46058d-e23c-3427-ac4c-eb59e12d041a | -11.47995 | -49.25214 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b2b95ca-e7bf-309e-8bf3-f1c256d6ea5e | -11.40838 | -43.53783 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 296c609a-a9a7-3a2a-85f0-508587fb4909 | -11.4507 | -43.59061 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f2dacad-5fc8-39a7-8a13-45d0d27914bc | -7.83835 | -45.40347 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0efc1c9-8521-36ec-acb7-dfa3781a50ad | -12.13854 | -44.85817 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4384bb6e-6dfd-34ab-b50e-f059ba313960 | -11.50201 | -50.38668 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 888239f2-a263-3b30-b7c5-ee51853fded9 | -9.06755 | -47.06586 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 743f8b56-efcb-3816-99fa-adfde9dd09bb | -12.47504 | -47.49458 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4c149ab0-fd1d-309e-82d0-2e3ab82923cd | -11.48902 | -43.68311 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 24fe9abc-3bdf-3c38-9fe2-78f595f43164 | -11.72184 | -50.64497 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| d11611ba-6ce1-3e7a-a4c0-ffbec04b68d4 | -6.44228 | -44.77766 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14988b1c-8653-344a-8495-acc343c2350c | -9.0555 | -46.97612 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 683a2a9a-4b7b-3613-bbde-2ef4675b3ade | -9.08481 | -47.08161 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8e45c04-c938-32c8-8bf6-ef6d7272a3b2 | -12.16404 | -48.4842 | 2025-09-11 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
