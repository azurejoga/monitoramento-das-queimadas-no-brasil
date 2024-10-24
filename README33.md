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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35c2a5f3-2119-39f5-bb26-da7e15d9ff6b | -3.21965 | -50.16684 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f92c9c5b-47b8-31b0-9a74-61122e7c6f5e | -3.21899 | -50.17091 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc65df88-c5f1-3dcf-aa90-66aa94bc9888 | -3.21832 | -50.17502 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0224a47b-28a4-385a-adfb-427680bbdd69 | -3.21606 | -50.16628 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee449245-477a-3566-b230-a4dfc4002b15 | -3.2154 | -50.17035 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c702b643-3410-3914-9ca2-e083544aa29d | -3.21474 | -50.17446 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07b417bc-d511-36ea-8b73-73f7fca4a067 | -3.20907 | -50.30046 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1e79fe9-26dc-3008-b12a-88fbb16f097e | -3.2053 | -49.62664 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe66c09d-1f77-3c06-b742-8c184b6766ba | -3.16658 | -50.37943 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdf4cb29-b86b-3194-b757-7706baa0a735 | -3.16543 | -50.38037 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ef0c48d-5e1f-3cc8-bec9-388ae1082b54 | -3.16372 | -50.46542 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e240682c-603b-33ad-b913-b99344194e8f | -3.16077 | -50.46061 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 171cbb3b-1333-3ce1-9186-b123f51cbf19 | -3.16008 | -50.46485 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9b8ee1e6-06a8-39f5-9de7-0cc24cd02753 | -3.16008 | -50.46172 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b1a26dc5-8925-3a93-bb1c-3bfbbcf4351a | -3.15942 | -50.46596 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 43f0198e-e5d5-36f5-a4ae-12217e280fdf | -3.15927 | -50.25539 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f371a771-ec47-3de2-af69-5cbe862b6fd8 | -3.15713 | -50.46004 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 95c032dd-c320-3002-b4f8-14ca32ebb54b | -3.15644 | -50.46428 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 05c6878b-3b0f-347a-ae8c-388587e2e3ee | -3.15644 | -50.46114 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c5060569-2d27-353d-98a3-dda91ab7a0d3 | -3.15578 | -50.46539 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 82506304-21d7-301a-9168-ca7b3286695c | -3.15349 | -50.45947 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 92ea9b65-46c7-3689-8db4-8fe47ddbd65d | -3.1528 | -50.46371 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ad16103a-1ce8-39c9-888c-f2a362566b80 | -3.1528 | -50.46057 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 04a52010-b9d3-3b59-9377-3de1343c677b | -3.15214 | -50.46481 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e387e59b-7154-3aeb-9af3-bebbe4b1bb01 | -3.15211 | -50.46795 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 436e3042-0181-3397-8e5a-ba459509c90e | -3.14983 | -50.45576 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| dbe9cdcf-761c-3537-966f-bcef3c3e71c4 | -3.14916 | -50.45999 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 58b6c6e8-f81e-3900-9d2c-74458107dd53 | -3.14619 | -50.45518 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 845fb115-a27d-3ae4-b67f-6362678f76ae | -3.07469 | -50.50504 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef17c9c6-fdbf-3459-a296-ecbec15f930e | -3.07241 | -50.49594 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b4adc32-8f45-35d9-9a5e-83e52a7c66dc | -3.07172 | -50.5002 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ed70660-c591-30c7-be35-290a3954e516 | -3.07103 | -50.50446 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ded0e57e-8133-35d3-ab71-034282a0a34c | -3.07034 | -50.50873 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54a7b6ec-d65f-3493-8595-f254e9245b42 | -3.06807 | -50.49963 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 649673cf-165e-36fe-8d0c-e893c25b367e | -3.04409 | -50.27211 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd250d3b-0537-3161-852c-554ba69e5571 | -3.00468 | -49.03703 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1915b654-1a44-3bca-9d07-2c5b1e3b9408 | -3.00409 | -49.04073 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c7b8d4b-2864-38cc-8874-e208666642d1 | -2.91358 | -49.4754 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c8082bb-0b09-36ec-b3aa-4d6fb9b1f259 | -2.90385 | -49.76172 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36db4276-e97e-375c-9a9f-30b3deab6eca | -2.85475 | -49.3405 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5f72f130-3033-3fa5-8f00-3569e7778612 | -2.80716 | -49.61766 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3a45ad9-91ca-34e9-baa1-a937345b39a9 | -2.80653 | -49.62157 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e1e8bfc-634e-3a66-9089-4383cc352795 | -2.80591 | -49.6255 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eea34bc4-e086-3bf0-966b-6630ea64a1bc | -2.80161 | -49.5848 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 368b518b-eb2c-3948-a010-6db7090465fb | -2.79749 | -49.58813 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef4524f9-1fdc-3e29-bbed-a942aecacf44 | -2.7624 | -49.30319 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56daccb6-03ee-328d-89b0-d61772c6083a | -2.75894 | -49.30265 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de8871df-5cea-3e09-808e-cfca1fd49d66 | -2.65855 | -49.27186 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e7fb3ec-1125-321e-b442-57a62f98652e | -2.6249 | -49.98668 | 2024-10-24 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f0ded25-27c9-3338-8546-6c6872676f29 | -2.62133 | -49.98612 | 2024-10-24 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21323b20-4c6f-3267-b813-d0fee1453003 | -2.58641 | -49.24112 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b4b92b4-5e1e-331f-a268-b864245921d0 | -2.58295 | -49.24058 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6050f022-81a7-3558-b0e1-9d4fa67c1cae | -2.49962 | -49.12352 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71be7340-17e9-3372-8d1a-d4598a25e48d | -2.49905 | -49.12302 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9650f6bb-b6f0-3c6b-9061-24fed2b2a292 | -2.49617 | -49.12298 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31950747-cdbd-3d94-a889-815b981547c3 | -2.47442 | -49.10417 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 179d2106-28ae-3fc8-a4a1-8872f6f4ab68 | -2.47157 | -49.09987 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aca6a9ad-5676-312b-9f6d-fc1c58bcd46b | -2.47098 | -49.10363 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43527695-0b35-3d0c-80a3-c72c7963a93d | -2.46813 | -49.09934 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44588b8d-5aed-3e19-bf89-542b155805f0 | -2.46754 | -49.1031 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10c0a9a0-0136-3167-953e-c5acd0a85c0b | -2.44174 | -48.99932 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf0cecf-9c0e-3b2e-b483-e27bdef59e58 | -2.23144 | -50.31261 | 2024-10-24 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68dfaa61-3a71-317c-a067-cc20ed717f10 | -2.2198 | -50.31517 | 2024-10-24 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1640b77-389f-374d-a57b-f37d3369ec27 | -2.9714 | -50.42414 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffb83a62-4536-3ee0-8647-b5b5f0dac3b5 | -2.97072 | -50.42839 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63a37fe2-0157-33d6-a9fd-287ae4051146 | -2.96844 | -50.41935 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2417d620-6cad-3b74-ad58-ff98981e5909 | -2.96836 | -50.4893 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae4086eb-6be5-3f27-a05f-bf7f1e98c5e7 | -2.96776 | -50.42358 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 85d18312-c175-3579-89b9-f3c4750babd6 | -2.96707 | -50.42781 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| dad6d07f-6da8-3564-9f0f-e20c80241971 | -2.9648 | -50.41878 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 72cd6f4d-3831-31ed-896a-5f087ea10eb4 | -2.96412 | -50.42301 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a66ea5ca-b584-3d0e-961c-5414e5ba8db9 | -2.96343 | -50.42725 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| bedad1ad-c47f-3862-8453-3ed871e516cb | -2.96286 | -50.52338 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f67e998-42b2-348c-b4ce-7f4f93d96751 | -2.96217 | -50.52768 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f7f0492-1b40-317e-bb02-d4a4b99f4911 | -2.96185 | -50.41398 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d6c2a68-63d1-3c2d-a6af-b5f2b34050a4 | -2.96058 | -50.51425 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa9215e5-3bb4-3fbd-a3f9-474521f044b1 | -2.95989 | -50.51852 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 007ec18f-7682-3db4-9517-7883158337d0 | -2.9592 | -50.52281 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72ba4518-4f2f-31b8-97ab-a8cada1ee340 | -2.9585 | -50.5271 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa6ca2db-4623-317c-8350-b4b997362716 | -2.95781 | -50.53139 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5412f08d-a54a-3f04-b8c4-d0dda8b2cc7b | -2.95692 | -50.5137 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d922231-d4e5-328a-81fd-70f2f8a226c1 | -2.95623 | -50.51796 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc1122b9-955b-3a60-8031-c9005218e4a7 | -2.95554 | -50.52224 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b2f41fb-88c4-35de-b814-a0ff8c90385b | -2.95484 | -50.52653 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76a9a828-b627-3d25-bef2-e1068280a69a | -2.95187 | -50.52167 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6e1b4ec-13ee-32e5-9f52-d4b68f743db6 | -2.95118 | -50.52596 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d4f5d82-623f-383b-82c2-eda78738c35e | -2.92852 | -50.48005 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beb903b4-6bf0-3754-9bdc-ec12a3021c84 | -2.8992 | -50.40559 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64489e1f-071f-3234-b21d-2fcb053b0c9d | -2.89556 | -50.40503 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1f97cb4-89b4-3c9e-b33b-f764314c26f4 | -2.82493 | -50.49461 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4471a554-d276-324c-a78d-8561135c446f | -2.82473 | -50.49614 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d73d509a-25c2-38e4-81de-dceff5320054 | -2.82126 | -50.49405 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a53b8dd-16c0-3863-909b-08dd85b9e564 | -2.82107 | -50.49555 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be3e0b5f-3a40-3618-ae82-ead2d4c4652f | -2.44656 | -50.37457 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b241dfc4-a5b0-382d-8492-23a2a00e0407 | -2.42314 | -50.28809 | 2024-10-24 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad0753e1-8f75-32ca-acec-afa4bbab7e8f | -2.4224 | -50.28872 | 2024-10-24 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc2debbd-353d-3d29-8d3c-759d53223546 | -2.41881 | -50.29177 | 2024-10-24 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f2ad991-ff1a-3bf1-8a17-9e4ee096bc20 | -2.40669 | -50.41232 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48c01da4-9e51-3cc3-846f-ce93555262b1 | -2.40668 | -50.41315 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcbbebe6-83b7-3962-a1a1-6641e453fbcc | -2.40369 | -50.40829 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
