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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12c6cedb-d41b-3b24-97f3-b2b5413af38a | -17.13055 | -57.41117 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 009fb0eb-d512-3771-a96a-03c5ffaba1fa | -17.12997 | -57.41609 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| a38fa2d5-b9c2-3cc6-8e6e-6a69cd2a8a64 | -17.12939 | -57.421 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| b55303bd-321c-3423-8bcd-2c5d9b59fd70 | -17.12826 | -57.39088 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 500b731b-836f-3b26-a912-b527f86b4495 | -17.12789 | -57.39493 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 18187a0c-b5d6-34fc-8192-85a3fc2d6398 | -17.12768 | -57.39583 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d0133c4c-da77-3c32-ba61-0a558801c83e | -17.12728 | -57.39983 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 1d7249b3-d49b-3dc6-81e5-496d83482a70 | -17.12711 | -57.40074 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 014ebb13-2475-31ba-aea9-0cc1a6fb0c4d | -17.12667 | -57.40473 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 4f7b2fbb-e483-343b-819e-6551d2ba54b3 | -17.12653 | -57.40565 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| eb67a9d2-975c-3c47-b36a-da1187e6a4ce | -17.12605 | -57.40962 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| f178e515-ca76-392f-8aff-704dcad1809c | -17.12596 | -57.41055 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 280a22cd-b699-324b-a7a1-b1844905e492 | -17.12545 | -57.4145 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 769fecec-63f8-37d9-a810-eb82c824ced0 | -17.12538 | -57.41545 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| abbf9e95-779f-3265-aa84-9a6174ff847c | -17.12513 | -57.37954 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 42bf8a50-4829-3578-9c7d-46e1db321093 | -17.12483 | -57.41941 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 925c74a3-7495-3862-bd17-6163be804603 | -17.12481 | -57.3804 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f470a011-206f-33da-9c67-28ab83c542ed | -17.1248 | -57.42036 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 792835c0-bc0f-35b4-bd82-ee5fd1cb8d43 | -17.12452 | -57.38446 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 19cd5588-f09b-380f-a9ec-ba86d6c1d6f4 | -17.12424 | -57.38533 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 7d8dfc13-90a6-3b3b-9747-3d6cc43090ad | -17.12391 | -57.38937 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| c93672b0-fad2-3a5e-8af0-dd2703750777 | -17.12366 | -57.39026 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| e6d75229-c887-3d9c-beb3-48c9896c32e0 | -17.12329 | -57.39431 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| a697aa48-fad9-3542-8f2f-cedd9d38204e | -17.12309 | -57.3952 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 6e0cca89-cf3d-3ad0-aa06-5957b271f01f | -17.12268 | -57.39922 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 6f9f0dbb-c7d0-3ada-9381-4031799ec5b7 | -17.12251 | -57.40012 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 1002edf7-6871-3df6-872f-e3df6431940a | -17.12207 | -57.40412 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 25e5c03a-22c2-33ac-97b0-5818e8cadb8f | -17.12193 | -57.40503 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| c34fbf6c-1300-3f5d-90a6-f4cde01fe3ef | -17.12147 | -57.409 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 25b420f9-8144-32c7-be65-0d04f1c41e3e | -17.12136 | -57.40991 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 2495faaa-3581-3208-90b4-d6c2d615252d | -17.12086 | -57.41387 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 75d5c8a6-f92b-32b5-89ea-2074d53d6d34 | -17.12079 | -57.41482 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 8f339de9-a00f-3c73-abb4-1025ea7426a8 | -17.12025 | -57.41879 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 2f69a85a-2fdc-3468-92dc-1cf2497e3437 | -17.12022 | -57.41973 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 1c5b686f-7fe8-3d94-ad5d-b82b0aadcaed | -17.11992 | -57.38384 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 87965721-c5f7-3793-8647-613e38c3bdf0 | -17.11964 | -57.38469 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| a8972fa9-9166-3e94-865a-f69d64695f2b | -17.11931 | -57.38876 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 15ae6983-4101-3b58-95e3-de1e2f1673fd | -17.11906 | -57.38963 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 2c2cebdb-bfb7-3973-b2f5-baeb3fbc91b2 | -17.11809 | -57.3986 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a3e9581f-53cb-3f53-9764-e2be676f7480 | -17.11791 | -57.39949 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| c49d876a-f9c7-3340-8c6e-ee6160df486b | -17.11748 | -57.4035 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b2e45460-659d-343c-b5e3-cc5efc4c84af | -17.11734 | -57.4044 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| cdeb875f-7e71-3c24-a17c-aa3023e71e86 | -17.11687 | -57.40839 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 2805747a-5f52-34ad-8444-5834f8ddf795 | -17.11677 | -57.4093 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 8d84ffaa-0dd4-39c2-94ef-c12e2c08ee42 | -17.11626 | -57.41328 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 5b1cc50c-ef8d-3b42-9808-691e6aad5757 | -17.1162 | -57.4142 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 3b17bb52-0b64-3f8d-bd8e-962e973dccfc | -16.81264 | -57.37818 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d293b8a7-9ed3-30a5-935b-7805fdbb3cc1 | -16.81207 | -57.38306 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 46d03136-047e-362b-8d16-c8e64f4ce30d | -16.79715 | -57.3897 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 65b952f8-40b3-3f46-9105-7e090bae566b | -17.03732 | -56.70487 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a5df12b2-2768-34b7-a4df-09ca900a919e | -17.03188 | -56.70967 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| bf34af71-9639-3ae8-8b9c-649ba147b9d4 | -16.85581 | -56.71696 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 547923fb-07f5-333a-ae45-1afb6292b8f9 | -17.17884 | -57.3978 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6e4f4fa2-34c5-3dc5-a526-bef77c5c9600 | -17.1772 | -57.37254 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 52fe3b62-97b1-3737-97bb-db8a578ab12d | -17.17365 | -57.40209 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ad346a95-d97b-36c4-ba1e-006933d11f33 | -17.17319 | -57.36699 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 052d9e0b-3858-359e-948e-047a86a6b6df | -17.16905 | -57.40147 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 881d5b56-e0be-3718-848b-c3cccee2ee59 | -17.16858 | -57.36636 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d934d113-7eef-3c65-8752-49664825a2f2 | -17.16846 | -57.40638 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9462c129-7f09-3784-8f4c-70fa1720d957 | -17.16397 | -57.36574 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 347a19b7-3f86-3000-816e-987ff07b91bc | -17.16299 | -56.96708 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e2a20691-2305-30dc-9db5-ddbf4ac7c1ee | -17.16221 | -57.38053 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 392b768c-6114-3fb0-983a-8e8436bf6299 | -17.16166 | -56.96642 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 12c6382e-f9be-32b1-86ac-f83c9e047047 | -17.15937 | -57.36511 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2af9697f-be43-381e-b66e-7062b4f13592 | -17.15927 | -57.40514 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| f1cb09d5-4761-3e9c-ac20-3031f8c558d0 | -17.15826 | -56.96641 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3c025e2d-837a-3cc8-85d8-6d9796031beb | -17.15761 | -57.37989 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a87fafb1-2a09-350e-9f01-2cfc0cd5aab7 | -17.15693 | -56.96576 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2aced8b0-2c12-3500-8637-7bd6e86ea06a | -17.15526 | -57.39959 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| fefb5404-0119-302b-930b-d19b9583d27c | -17.15219 | -56.96512 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d652be17-2f70-315e-9144-8e7bcd7b55e8 | -17.15008 | -57.40386 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| a25d77f8-c893-3a9f-9c4c-a768d18f48fc | -16.92665 | -57.70596 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 97918785-ea64-3df4-b9ab-6c84055edc4a | -16.92331 | -57.69601 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9d3c1702-0df4-36ed-a7c8-de4a3e4a9c08 | -16.92274 | -57.70067 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| acc0ae9d-73ff-3e42-b9a2-25c20e01e7b1 | -16.91882 | -57.69539 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b66b00a5-5747-3790-bfaa-cea98cf506fe | -16.91489 | -57.69011 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| d7ac5bed-5e8f-3032-aca7-b0185dc22f1c | -16.91433 | -57.69478 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ba5e5087-4a34-3877-b40c-1c08361f0d4b | -16.89299 | -57.68234 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3d73e88c-ff19-3256-83bd-c4d0f02cf0db | -16.89243 | -57.687 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f93b1e3b-675a-3591-936f-7307dfc6988f | -16.89131 | -57.69633 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 77060491-39df-3829-819b-c49f799ec9c4 | -16.84903 | -57.46196 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| f68e0175-4823-3318-bda3-f4265cf20e21 | -16.83991 | -57.4607 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 62608150-fbf8-33dd-8afc-ad64e5580700 | -16.83536 | -57.46008 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e68ae6ba-f9a5-3b98-86af-19b6cb0db4c3 | -16.83303 | -57.47934 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 06f7e38d-4abe-3abb-9a24-746d3ce5d85e | -16.8308 | -57.45945 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 6ca5fc49-24ed-303b-8e27-ec62889c662d | -16.83022 | -57.46427 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 90061735-a1d5-3b3c-a923-b3f1359e4959 | -16.82868 | -57.81178 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e130f0f8-1aad-3cf8-8625-6259bb5137c3 | -16.82624 | -57.45883 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 41dd46a6-2ac1-3e4d-8a23-9f8f9c7bdec5 | -16.82566 | -57.46364 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| c709f3a3-bbaf-3113-b427-dd97f60261c0 | -16.82423 | -57.81116 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2d3d5f20-b427-3965-9c33-54a29c5e447f | -16.82168 | -57.45821 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 0365ccda-8192-36ac-ae74-8b61000db7e7 | -16.8177 | -57.45277 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f8f061c5-8f46-3679-9291-1db5e8cfe92a | -16.81713 | -57.45758 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 43ecf154-4855-3333-b683-1a68dc83044e | -16.81419 | -57.81906 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c5ba7199-a5bf-3438-bea5-72e0f4e8e8f1 | -16.81363 | -57.82362 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 80cac0f6-7021-3e25-b565-ec9a1fe7cbec | -16.80918 | -57.823 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| df98c22f-2c53-3323-84f1-e540453cda3a | -16.80861 | -57.82756 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| abd8633f-b523-3481-a115-d05baf5ed366 | -16.80136 | -57.84965 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3d4132b5-84d8-3e09-81cb-8f643b7e1c3a | -16.7986 | -57.83543 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ef2d108e-d1c6-39f7-b45a-9d8828bda8ce | -16.79416 | -57.8348 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |


[Clique aqui para ver as próximas entradas](README142.md)
