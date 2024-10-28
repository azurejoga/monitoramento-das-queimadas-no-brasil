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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e36e295-8bc3-3f7d-87d1-1c309426c931 | -3.13391 | -54.2759 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84cbe8a7-9393-35e0-9388-52ebac856073 | -3.13169 | -54.26844 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 430e5c4b-c5f5-3cb2-81bf-cb92e299ff8b | -3.13114 | -54.2719 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af7c8dfd-28ef-3cc0-bff6-6fae3e2a5ced | -3.13059 | -54.27538 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e0b927b-2173-39f1-8e90-0541ef715938 | -3.12837 | -54.26791 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46fea3e0-baf4-373e-8b6f-88aa3308e960 | -3.12782 | -54.27138 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53451cdd-c9ef-361d-9ea0-cc776af2f77f | -3.12727 | -54.27486 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 172bd374-7f14-36d1-8ba3-da984cadedb3 | -3.12672 | -54.27833 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 117f5e3d-df4b-383c-8f24-0d5fc56b1ec0 | -3.12031 | -53.71465 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e477b523-ec4f-3135-9155-76251f01b5c2 | -3.11977 | -53.71809 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3694854-3f4c-3f35-aaba-1b9848e16093 | -3.11621 | -54.28026 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 34c495c2-cb74-3d1c-8baa-87e6cdbe8ae4 | -3.11566 | -54.28374 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5c3b5abf-054f-3c14-8634-5bd2cfb4661d | -3.11507 | -54.24449 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c659ada-1c3c-3806-8ab2-7d50116b93fa | -3.11344 | -54.27626 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab7667be-d4fc-3d32-8973-9c83fd36f8b6 | -3.63499 | -54.68168 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efd2c606-34ac-3211-9bf8-b1c3149a3934 | -3.11289 | -54.27974 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df521513-9d0c-38d2-b124-dd5cc0087f6e | -3.11234 | -54.28322 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4c44706-f3e6-3fe0-a7d9-94480ee12418 | -3.10957 | -54.27923 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a46860f-e6e6-3986-82db-85c92ce9bd93 | -3.10902 | -54.28271 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01bc2e0e-77a7-3c86-a3f0-c435fdcbe363 | -3.10838 | -54.17938 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3a795dc-7cb5-3bdd-b88f-6b40789d11f8 | -3.10507 | -54.17886 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fbdfe2e-ebbc-36b7-91d0-b6effaefcb90 | -3.10387 | -53.73321 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54f208c8-26d6-32ad-b1bf-59fa217d1e32 | -3.10273 | -53.71896 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08abdf71-f962-3641-9c54-34349b070200 | -3.10219 | -53.7224 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d42f6bb-c12d-3512-b157-73fdea071056 | -3.09943 | -53.71845 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19e250a5-d3dc-369d-b379-e952c37709c7 | -3.09889 | -53.72188 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8921f4b-f41a-3db4-ac13-62a09d771229 | -3.09613 | -53.71793 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82b47745-9620-3bfa-affa-dd8c2eeab328 | -3.07954 | -54.16765 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0398175-0bb4-3213-a134-643b5809ef39 | -3.07899 | -54.17112 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9cda415-88f3-36dc-99f2-bde1b9712ecd | -3.07845 | -54.17458 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48e58214-c045-324c-ad72-5a9c1da4aebc | -3.07622 | -54.16714 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 45501ba8-3784-35d8-ab35-e6c331179d28 | -3.07568 | -54.1706 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e33c6b9a-4c3d-3b8a-a5c4-5cbc4a4622a2 | -3.07513 | -54.17406 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e7056639-7b53-3f32-b633-57b5fb4baaf8 | -3.07236 | -54.17008 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| b28ecb3b-8e5e-302c-8cd0-f3e3ed8507fd | -3.03199 | -54.14605 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8267bd5c-751b-353b-940d-5530caf96062 | -3.02922 | -54.14207 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5e9fa52-6e9d-332c-b6c3-873bf076d643 | -2.95378 | -54.68343 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01a08f39-5962-37a9-a03d-d0f832ecce62 | -2.95227 | -54.15433 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98d60954-4ce2-342c-9429-1e8b28837a96 | -2.95099 | -54.67934 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7603507-1979-31a5-8db2-a26fc4bf2f86 | -2.95043 | -54.68289 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc972fb0-49c7-3f07-8b6e-2ce9a44e32af | -4.5092 | -54.96078 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90a9b43a-76d3-3079-8921-4ff8889abf85 | -4.50586 | -54.96025 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 724bce4a-f194-389e-96a1-999acd736893 | -4.50195 | -54.96327 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba4c261e-6d09-33d8-bdba-3e0cbbb538c1 | -4.48893 | -54.87744 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30a68dc2-0edb-3178-915e-a74fc98abd15 | -4.46201 | -55.11318 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c3cf0b3-04a3-36a6-b29e-dcbedb55650b | -4.45865 | -55.11267 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5439d54b-346c-390c-9240-62221565b209 | -4.42284 | -55.09972 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fd5b52f-6017-386e-904e-35ca2ec2bdf9 | -4.42062 | -55.09206 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a78fb6b-d71e-3ef4-989f-efe5b39842fa | -4.41948 | -55.09919 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be7331af-af77-36e7-84b6-4ed5ccbbbc5c | -4.41891 | -55.10278 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58adb7f2-0d3f-3770-a11c-b50d973989e7 | -4.41834 | -55.10635 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f855527d-3356-309b-9219-791520198d0f | -4.41777 | -55.10994 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6f3f77f-7791-3ec3-8c27-551c907ca6dd | -4.41612 | -55.09866 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d50fd937-7ad2-30f7-b1a4-06ebcdb7ff9f | -4.40827 | -54.84665 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 638fa8cb-e2e4-37a8-ad4d-a873de6f7ee7 | -4.40544 | -54.84626 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0a1734c-0441-3ff6-b4ac-4c7d82264954 | -4.38954 | -54.98517 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 552c6ffc-df78-3830-b243-d06fd30ce0e5 | -4.33052 | -55.05994 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5ab5264-8951-3982-baa1-90e82577b31f | -3.73048 | -54.05452 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71e0fd9d-f8db-37b3-88f2-12d29ebf1a72 | -3.72345 | -54.46554 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c49d3bd-d282-3907-913e-6b42eb7d8b90 | -3.7229 | -54.46901 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c80803e6-7eb8-3072-be36-a0faa39581c3 | -3.72012 | -54.46503 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffae7d01-6ae7-3a8f-92dd-a6201e0c23e1 | -3.71957 | -54.4685 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc85fb14-ab1d-391a-a3b5-8ecf04591346 | -3.70132 | -54.06763 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c92f034a-6e44-3cb6-a4e1-d92d2a0a5de1 | -3.69801 | -54.06711 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84bd79b6-927f-3884-a890-8a1f9e156c67 | -3.68215 | -54.55584 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ab041ca-a7c9-323e-a595-936f23d69c9b | -3.67189 | -54.29699 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12803bfc-4386-335d-a067-c0cfd6c60332 | -3.67125 | -54.21517 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f6abd27-cbcd-3fca-9d5a-2321ce379a75 | -3.66915 | -54.31437 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4c98761-9344-31fe-a5cc-3ee76cedb0f2 | -3.66858 | -54.29647 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8594c08-b639-319a-ac38-a070fbbdad13 | -3.66805 | -54.32131 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c6deaa9b-7ffd-3c65-a821-87a28f32d443 | -3.66793 | -54.21465 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23900c38-02ea-3dc9-aecc-40ad5134af43 | -3.66739 | -54.21811 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 651b723a-94cb-3eb4-9b30-9afe34a1c0cd | -3.66638 | -54.31038 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9540236b-770c-3f7d-80dd-d98664d9174b | -3.66583 | -54.31385 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf395575-4cd3-39a7-8d6c-2d2c280fd0de | -3.63833 | -54.68219 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bad6f2e-38c6-30aa-8ca3-6e5f821c4a64 | -3.92706 | -54.51228 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0afa92b0-657d-300c-866b-01cdb960c48b | -3.9243 | -54.50827 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0665e355-6a14-3d66-8ef6-f882ab048d45 | -3.85371 | -54.76264 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 138ab881-fb08-31bf-a5eb-e7c17c747a35 | -3.85315 | -54.76619 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d33284b5-6610-3365-b91d-f53aba77d9a8 | -3.81257 | -54.11687 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25ea8d91-14e9-39a0-8e04-cbbc0a57f48a | -4.30529 | -55.0888 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30b12500-5dd5-3d0a-ad88-0008191d182c | -4.29521 | -55.08721 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61194f4c-04cd-3e58-b7dc-c69dda2a876f | -4.2814 | -55.19541 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63283fa8-6259-3879-ac66-2de1ffab74d8 | -4.24886 | -55.18293 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2285782-b2ef-3c07-a4b4-dc7f3c7e07b7 | -4.22458 | -55.31244 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae3289c7-304f-33eb-9233-62671f983c7c | -4.16497 | -54.14776 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e29da88e-fd5a-38f7-9c87-ebced55669c8 | -4.13916 | -55.15464 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e80c7ce5-2798-3d40-a5d9-1387301a74ac | -4.12556 | -54.84912 | 2024-10-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2fe76de-5d13-3803-bfc4-cfd4b15887ed | -4.11564 | -54.28872 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30bd7839-fa23-39fe-9530-cf35e4d3b4ec | -4.11234 | -54.2882 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afe9be53-3b4e-3d16-9ff3-e42c06f8acfd | -4.11179 | -54.29168 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c93d25b-b067-3a1c-a6dd-f341506c7c99 | -4.10162 | -53.94371 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6407f677-2acc-35ae-96df-5ca55165bb45 | -4.09832 | -53.94319 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f14a3fb1-26a1-318b-aaab-1afdfa7cba30 | -4.09778 | -53.94663 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ead760a-a0fb-320e-8d08-097396c10999 | -4.0961 | -53.93581 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d019596-fc62-35ce-83e4-2ac1d37c4bcc | -4.09556 | -53.93924 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17fe69a1-ae27-33ed-83bd-90602c0dc5fd | -4.09502 | -53.94268 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03f1a438-fc44-30c0-8ada-aa1d644a22c3 | -4.09448 | -53.94611 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84ab744c-0f60-39a8-bc56-03bf7132f11d | -4.0928 | -53.9353 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37c0ae18-f620-3504-a392-18657229d06b | -4.07218 | -54.43477 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README69.md)
