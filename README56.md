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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59013a5d-29a7-38ad-8e06-a62117827450 | -5.23197 | -45.11249 | 2024-11-23 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef64a914-67e6-3c64-b0b4-3b65bdb6e210 | -3.57843 | -54.68074 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 149e4aa0-392e-3eb7-8d51-86421f51aa71 | -4.25329 | -48.69972 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 222b80d5-7afb-3f02-8652-5392969ecd68 | -2.9625 | -53.88092 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18ade94b-93e7-339b-8be0-b4185f0321f4 | -3.21496 | -53.84145 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d143dcb5-9c4a-3ca3-989e-14377a93e6cf | -3.23426 | -54.23847 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5ea8a30-471a-3809-a3db-6fc6d8d41efe | -2.82358 | -54.03316 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 53e0a34f-d0f5-37d7-8ffa-2597167fd70d | -6.18046 | -45.45186 | 2024-11-23 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 494f026f-b95e-3f39-b9a0-857481507ce6 | -4.72246 | -45.49614 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a34c2368-c4a0-3abc-a464-0d32d560a7ee | -7.07513 | -49.212 | 2024-11-23 05:12:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8979e178-26e3-347c-9705-f266231fa57a | -3.23351 | -54.10062 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| db9496c0-54b7-3e32-9a77-4137b39d9084 | -3.2037 | -54.24628 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13858bac-655a-3cc1-9628-ffa9a09e6fea | -2.79023 | -54.15466 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65a27b53-763c-3398-9045-83011f97fd61 | -4.62271 | -50.5071 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddfa28f5-1b59-3747-9626-01686dff099a | -3.40766 | -54.02683 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad9b01a6-4a30-3b57-94a7-a948459d916f | -3.10297 | -53.742 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea26f19d-8068-3842-a837-88d7155118fc | -5.97129 | -46.30317 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15ca49c3-02f6-3c09-96df-b937b1cef58a | -4.15305 | -48.39868 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ca20c4f-f7fc-35a7-820b-f01424a6d463 | -4.72583 | -45.49646 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c3884024-d94c-3816-abd9-c2cfcfb04a31 | -2.85147 | -53.99255 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0745035-092d-3028-9c34-cee9e535a151 | -3.68043 | -54.58591 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba9b66d4-aaca-317b-8c68-0b340411fde5 | -3.03582 | -54.18562 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 151fc3d0-3bc1-337d-9012-e1a572b14616 | -3.29238 | -53.85287 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c482c3a-dd0f-333d-a5b8-02f8dc3b062c | -3.76011 | -49.93414 | 2024-11-23 05:12:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba767129-f475-3261-994c-0bb670f0c750 | -4.16029 | -54.58089 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 348f2633-3513-3974-b8fb-e966ca2a982e | -3.50841 | -53.81105 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c38a1aca-433f-3a51-be5a-684ba62c2611 | -4.72656 | -45.49133 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f74c96c-1676-3c5d-bdfe-4f3c1a0abd4d | -3.94646 | -47.96792 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d7ed207-ef9c-3825-9ea6-05d39a7caea7 | -4.27528 | -48.60451 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 143841bc-3132-39f5-87a3-2dc8cc505b26 | -3.70219 | -51.79201 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 64ab5fcb-2767-3c0f-92a4-ce60f9bbe642 | -3.2478 | -54.22041 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9927c14-c30d-3852-a113-cc993734dbbe | -4.15348 | -48.39571 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5168b388-278b-3e08-88eb-5414fc7f62bd | -4.63247 | -49.54193 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 864f0448-d2c6-3b5b-a131-892ac0df4b8d | -3.51502 | -53.81611 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d09ada1-38ed-3965-a275-782a28ca74b8 | -3.71124 | -53.75085 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e847d44-900c-3d7d-af2c-73b57d4167b5 | -4.24177 | -48.63642 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e94d08e-d665-38d2-bb64-9c45cb4ac411 | -3.06011 | -53.2815 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 941d63bb-1124-3779-a639-2a13a5a2ae18 | -3.46462 | -54.64421 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0640819-42be-3895-bb86-42a4d8c85689 | -3.52233 | -53.79194 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 525c8c29-f0b1-30c7-813b-84a8f44452ba | -4.1032 | -47.81263 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcb5158f-f380-3e2c-b3d7-67bf7ada66fc | -5.56466 | -46.29258 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c781f34d-6b94-33de-a19c-5affe9bf0ff2 | -3.24655 | -54.2524 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c66e940-828a-3026-8bec-4fb7bfb72370 | -3.2184 | -54.2444 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a5c12a6-b997-3f2e-8cc2-ca10c869e44b | -3.1811 | -54.3227 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a089e264-5e4e-3178-a7af-f8fa247034f9 | -3.28767 | -53.83536 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c995a9e3-3ab7-30d0-9d4e-58b99ccaf04a | -3.50598 | -53.81649 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3bce81d-3422-30b9-aeea-925880d14396 | -3.18291 | -54.31097 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adb16606-233b-3e14-8904-6e30c9302756 | -5.5737 | -50.94924 | 2024-11-23 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ec151a0b-6db6-312b-936d-e258905ec8dd | -6.50221 | -47.04314 | 2024-11-23 05:12:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 61e6b777-fe50-3021-887c-168ff01ad7bf | -4.60863 | -46.50327 | 2024-11-23 05:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 3d7e8d79-626a-3ada-a1fd-9d8633c40aa6 | -4.95027 | -47.80465 | 2024-11-23 05:12:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e6dfde9-4498-3ab7-9767-98439a1449d3 | -3.21136 | -54.24337 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2033c271-6b49-3e50-86e0-17cfd9f47232 | -3.75314 | -50.01134 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3abe5e3-cbd8-3582-b390-98c967c7d8c1 | -2.93043 | -54.28262 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfbb30fc-dbaa-387a-afb5-f9b1e32393e3 | -3.80961 | -51.99417 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b01fd55c-61ff-3c0b-84c6-0cd527d0939b | -3.1945 | -54.3288 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb47a42f-bc31-3f2c-ae74-d7c44073971a | -6.33123 | -46.03286 | 2024-11-23 05:12:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d3e3a008-3528-38ad-bee4-b13bfc190338 | -3.25663 | -53.27406 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ed5a122e-0848-38c0-9a13-fc61d4eca4ac | -4.69993 | -45.84603 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6112b416-944e-3cb1-afe0-14cf31ab1746 | -4.24947 | -49.68679 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cef4ca78-1928-3e9c-903a-20c39c204518 | -3.25777 | -54.22598 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15861a2c-753b-38ed-8fa6-764591a40aed | -3.76445 | -51.68198 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 659955ef-02e2-33c0-8a6a-4c4cb1216bd7 | -3.11392 | -54.2928 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99f72674-b5a2-31f0-a4a9-55c42ef81671 | -3.2031 | -54.25015 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7042ae31-4f90-37ab-b240-4aeb5566849a | -3.23133 | -54.23399 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec28cf99-fb3c-3c75-a705-7725df3d71a5 | -6.18697 | -45.4524 | 2024-11-23 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0a7eb87-328a-3f4c-8fb7-f25c7dbf1563 | -2.82598 | -54.01722 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f7db3e9-6adc-307e-87b0-64e9f8569e66 | -2.81406 | -54.02481 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 751e5b11-6ad1-322b-b1a4-e8718721a3ea | -6.50278 | -47.039 | 2024-11-23 05:12:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 40ea9f54-e70f-3a4e-ac9d-691b0f56d211 | -3.1846 | -54.32326 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 984c2f68-e17f-33ea-9d31-ef077679ba9c | -3.1036 | -53.73787 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcbbbe49-eb57-3554-bb81-b3947eac93e3 | -3.19161 | -54.32436 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 836b052b-a32c-377b-aa61-af51a9fb73b9 | -2.8455 | -54.00798 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd2ad0ab-520d-37b0-8b07-be277bdad339 | -3.22722 | -54.23737 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6632f8c-087c-3d63-b31b-28acc35817f0 | -3.11634 | -53.10988 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76a7b498-4f11-3747-8c4e-3508d028bbfe | -4.0024 | -54.42574 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fb044f9-e512-3035-b555-ea90375af6d8 | -3.28496 | -53.83989 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a24d7c-788e-37b9-a3db-c2a149a6088f | -3.28137 | -53.83934 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddb2c7ad-d326-37bc-aecf-8c62621715a9 | -3.23349 | -53.93583 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f5416a8c-a491-35ba-bde8-f3aa4716c03d | -3.50902 | -53.80694 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67fd3fa6-0228-3882-8167-481c1d33640e | -3.93639 | -47.1994 | 2024-11-23 05:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9d79777-999f-3615-87fa-5151f947f43f | -3.25133 | -54.22094 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1f2c927-90dd-3b21-940f-671265659211 | -5.75815 | -46.25422 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c2f5e9d-79dd-3d0f-8d85-339f3e28391b | -3.24541 | -54.2362 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 75d91390-2fae-34a0-b5bc-199c781edc06 | -3.46809 | -54.64472 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b530f026-c623-3193-8b59-077b0f96787f | -3.22546 | -54.24906 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9693e997-a7a9-3dd0-8f29-0ca2e12fe1da | -2.83721 | -54.01486 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f1f7832-20ba-3491-ab92-ff18b0535532 | -4.20251 | -46.81499 | 2024-11-23 05:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0e1a4ac-edcc-32c8-8277-df78a7376fbe | -3.12513 | -53.10222 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| de152a76-386c-3950-b0e0-6c683b447fe4 | -5.29269 | -44.86357 | 2024-11-23 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e368408b-36b5-3226-a1a0-ebefdb018bfa | -3.23308 | -54.24626 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83319c15-7b91-3f37-988a-9528f50a200b | -4.91332 | -47.85798 | 2024-11-23 05:12:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd0905d7-169c-3144-9c38-50b094acb319 | -3.30477 | -54.49102 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9492809-b4c8-3e5f-9d1b-53f9d1bd6ff1 | -3.29708 | -54.72795 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ed953fd-1347-373d-a695-41078c34aa21 | -3.05329 | -52.75787 | 2024-11-23 05:12:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa399829-2aaa-3d64-900e-b1bee0b5b5fd | -3.24363 | -54.24792 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 389ca7f5-9c41-3037-8bb1-1e5b8d5ab1f6 | -6.49691 | -47.03815 | 2024-11-23 05:12:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c3344e4-f183-3050-b2d0-d1412aa2c856 | -4.25746 | -48.69437 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 02c0dd50-a7fd-3db9-9f39-e3cc240c1515 | -6.15371 | -46.67445 | 2024-11-23 05:12:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 422306aa-12ce-34dc-93df-a4b11f54c279 | -4.90935 | -47.8594 | 2024-11-23 05:12:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README57.md)
