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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc643b88-8de9-30b5-b416-4c7825cb6661 | -17.02459 | -57.43261 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6df533e4-ca20-3728-a8df-25fbf28d8f88 | -17.02345 | -57.44057 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7c3a8301-7177-39b2-a4cc-ddd7c7432cde | -17.02169 | -57.42808 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 823bfa26-6669-30d5-944c-d03f2962100e | -17.02112 | -57.43206 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a3a445ec-479a-3308-bb69-5bd9082ba16d | -17.01997 | -57.44002 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cf24814e-c993-37ad-81c9-f4fd1b927c18 | -17.01822 | -57.42753 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f16370ae-66d0-39db-82ce-58bf81147ac5 | -17.01707 | -57.4355 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 21359e54-cda8-3548-963b-f265b3fdc2b5 | -17.01588 | -57.41902 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 9bc31e51-15f0-36c8-ac2d-55832ba0194a | -17.01531 | -57.423 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1c3627d2-95c2-3152-b34f-01ada93d1a4c | -17.01474 | -57.42699 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f30373a3-f0d6-31d0-b542-e3f718a4f70f | -17.01452 | -57.41614 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2e8f5502-cf5e-37f8-aade-51f67c65392b | -17.01393 | -57.42013 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bbe1f1ef-c935-3395-ba80-97de66165d37 | -17.01335 | -57.4241 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 32bb9f40-c60c-3377-b3b5-7901a379d28f | -17.01298 | -57.41448 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8a8dca3c-f2b2-396d-9730-ae7df6bee3ef | -17.01241 | -57.41848 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5e7324ee-cbfe-3775-baa2-9ef75af4c6d7 | -17.01189 | -57.44688 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7273c86c-e972-3def-8b67-54e657a8bca1 | -17.01105 | -57.4156 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 41f8d2f7-450f-3733-95a5-54fc78974456 | -17.01046 | -57.41958 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d38996dc-d8bb-3630-a614-cb9dc7287f1f | -17.00987 | -57.42356 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7e84d30f-8d2a-321c-8b12-710a2c7605d4 | -17.00983 | -57.44795 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b57f0b1f-841f-3185-acc7-72e62e682e58 | -17.00924 | -57.45192 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7a2cfa97-0bee-35e1-9da8-403856b3ad3d | -17.00812 | -57.43549 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5a9cf0a7-439d-3f5c-ba8f-eb50061ed628 | -17.00785 | -57.45032 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 80fb376f-ba7f-3b50-8cdc-f6aeb8817286 | -17.86621 | -57.37095 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 84831cef-6429-3185-b9d2-8eefad6f2b78 | -17.00757 | -57.41505 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 17b14b05-15ba-3c50-8f80-de39a7c8266c | -17.0064 | -57.42301 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b470ab22-2b61-31d6-ac5d-35dfe3ee4b89 | -17.00582 | -57.42699 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8b661301-07f7-3c52-b081-ac606e56a01b | -17.00577 | -57.45138 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 42dc95f9-e306-330e-bb5c-bcfb4ab0317d | -17.00468 | -57.41053 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b4ba9a01-bf04-3a55-9e4a-aadd0eba39e2 | -17.00461 | -57.45932 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6f9d5434-93bd-3d8f-a187-5aa6b29113f3 | -17.0041 | -57.41451 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 641f0337-6400-333a-920f-73c2f3c26abe | -17.00351 | -57.41849 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5881483d-fe33-38ac-8831-211043ac2399 | -17.00293 | -57.42247 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a826a40e-ca14-30ef-a2e3-24d27699bb3b | -17.00227 | -57.47517 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e3d77d7a-7040-3b1d-8c58-715b557df456 | -17.00172 | -57.4548 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 23c4051e-33df-39e2-b9a6-5c0b7fd19c9e | -17.00062 | -57.41397 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 53b55db1-0d77-37b7-82f4-a4b43757bbc0 | -17.00055 | -57.46274 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3e022e94-bd38-3409-b6ed-6129fa772161 | -16.99945 | -57.42192 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| af725c99-1510-318e-ad72-08ad8915d930 | -16.99938 | -57.47066 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 08930303-9de9-3671-8c7e-4f694a0b8878 | -16.99887 | -57.42591 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 10fd4df4-eac7-3e8e-9d89-ecf096d2dc62 | -16.99715 | -57.41342 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c06d7343-661b-3af3-98f6-e81103befba8 | -16.99708 | -57.46219 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 58bd1cfe-2cab-34b3-8ea5-6d8185df6cd0 | -16.99598 | -57.42139 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 93516ce4-331d-3840-9a8f-2ae0e68318bc | -16.99592 | -57.47012 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b06a8c1b-f5ac-31f4-85f1-51e475a8ad0e | -16.99533 | -57.47408 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 16562769-fb16-35cd-b0c2-2c09beef6832 | -16.99475 | -57.47803 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c7117720-07bc-32ea-9ba1-358a2e7c7daf | -16.99426 | -57.4089 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8d00ab21-88f8-37f2-9e96-190f8fe0ce1e | -16.99367 | -57.41288 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 05b4c4a9-5033-3acf-87cd-7b543f4068c7 | -16.99306 | -57.44126 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ec00d48f-3161-357c-bcf2-4ebec1d2fd4d | -16.99129 | -57.4775 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0b713022-aed6-38d8-878e-a54ee51a202e | -16.98724 | -57.48092 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 104ea753-8258-3854-8888-e7eaeff2cfa3 | -17.86562 | -57.37503 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c73e6d4e-00c1-37d2-aa46-410def5d0b70 | -16.98607 | -57.48883 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5dea68a8-3cbc-31fe-afb0-61d5c1b00fca | -16.95201 | -57.5037 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bcb570d1-5164-3f47-935f-645a802a4153 | -16.95086 | -57.5116 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0bfbe31f-8356-3659-a451-449448ec1f8a | -16.94798 | -57.50711 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 286b68be-435a-31b9-82cc-13c97fd57a5f | -16.93765 | -57.69791 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| eb36f495-96d6-3930-b47e-fae650cdbaed | -16.85009 | -57.43613 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1fc81a16-9ad4-3d1a-80c7-ff8a28773b9a | -16.7624 | -57.5599 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f8264603-017e-376b-a012-9ca403612d67 | -16.65882 | -57.45622 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5583c29b-ce2c-367e-9d15-9d82be7b0777 | -16.65536 | -57.45568 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 32fd5891-b8c7-31e3-b3bb-ca2c3f13657a | -16.60585 | -57.50415 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 79ee842a-55ee-32e5-9f41-f41bb56be611 | -17.88198 | -57.38591 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8e8a04c1-901d-3989-aae7-7af4312bc71d | -17.87847 | -57.38537 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.9 |
| de2939d1-7670-37a3-bc59-84118cc5c2ab | -17.87788 | -57.38945 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 0f86099f-a3fd-3648-999a-465128ad6c81 | -17.87496 | -57.38482 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 26af3f2c-49bd-362b-bd38-e7896b830b3a | -17.87442 | -57.36386 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b31ab1ce-de0b-3c33-8bad-31d3e30e4753 | -17.87437 | -57.38891 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 4397ac35-4adc-3abc-b1ea-dcc3702fa0de | -17.87383 | -57.36795 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 68016c0f-dade-3f97-8109-0ea0397469c6 | -17.87378 | -57.39299 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| da9d2ac0-c766-35bb-a570-7ec5e8d19f4b | -17.87323 | -57.37203 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ec14c0fd-3590-3ccf-b9d4-ccf8abc3e920 | -17.87264 | -57.37612 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.3 |
| 9c7a6823-d3a8-3d90-be10-1f876fe88aa7 | -17.87205 | -57.3802 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.3 |
| 019d2061-3fec-3945-a158-c894a11db9e5 | -17.87146 | -57.38428 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.5 |
| f49dde06-8149-3f2e-83b3-5539b6840dab | -17.87086 | -57.38836 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.5 |
| 6e96dab2-dc1a-3dc1-9f3c-e231aaa2eda5 | -17.87031 | -57.36741 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 287c2802-357e-3957-92b6-52d1f1c83fe2 | -17.87027 | -57.39245 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 42720c4e-8320-3471-92fd-022bd2767562 | -17.86972 | -57.37149 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d4936e02-405f-3fae-8791-333e1767abd8 | -17.86913 | -57.37558 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.3 |
| f0464a02-2263-3662-94e8-5fead5ce5d54 | -17.86854 | -57.37965 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.3 |
| 94060c52-59c3-365f-9ee0-70dbf388760d | -17.86795 | -57.38374 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.5 |
| 8297f826-5195-3da4-86e3-e8ad3c01515f | -17.86736 | -57.38781 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.5 |
| 7a214224-68b6-3fdc-a686-9c7634b10874 | -17.86503 | -57.37911 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 53b53ea8-8f3e-3523-9822-245296cf06fb | -17.86444 | -57.38319 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a85e6e3c-110e-34b4-854c-9f37ce66d70a | -17.86385 | -57.38727 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 28c8a53f-bbbe-3836-b320-f9a970b44189 | -17.86326 | -57.39135 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| af0f47cb-24ac-35dc-8bd5-c02bcbc6aaa4 | -17.86271 | -57.37041 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b42ba7cf-670f-3ea0-96fc-37fa3bad680a | -17.86212 | -57.37449 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6d3882ee-d292-30d2-b8e1-2de2d4932df2 | -17.86152 | -57.37857 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1de1b66b-b04f-324b-9f91-04fb0817247a | -17.86094 | -57.38264 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 46ff1c8a-caf2-3402-b899-13a848adc2e7 | -17.86034 | -57.38672 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7b3d5333-5baa-3bba-9a3a-1305775823ff | -17.85975 | -57.3908 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 2031dbf2-a76f-3b7f-853e-553e52c0346c | -17.8592 | -57.36986 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0dcc4092-b1b7-3e75-ad6e-4691e289644c | -17.85861 | -57.37394 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 36289f21-5365-3e3f-9aeb-0106e0892b6a | -17.85802 | -57.37801 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4addb04b-0139-3e32-b7f8-2ca4f0283448 | -17.85743 | -57.3821 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 73d20010-15c5-3874-8581-4eacea70c869 | -17.85684 | -57.38618 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c5317fb6-4cfc-33d7-94f5-4e892c7fef1f | -17.85625 | -57.39025 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| efcc56a8-005f-3aed-8cd4-25ae223707cb | -17.85566 | -57.39433 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| aba5151f-2083-3fce-bc23-45fa5a158c84 | -17.85333 | -57.38563 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README128.md)
