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

## Dados Diários - Página 196

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3aaf712a-0943-37c0-8a12-cade01e1b597 | -12.88902 | -62.45387 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e17db2f1-2af9-37b6-a7b6-1eb7e348c09b | -12.88922 | -62.45667 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 387e1332-b9d7-383a-ad6f-a707280df91e | -12.88979 | -62.55029 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df456102-9fec-344e-bbf4-532b3a12fb86 | -12.89025 | -62.54769 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8e2a40e5-766d-3860-bca9-19e2e2db8a48 | -12.8903 | -62.54612 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 890f9817-dae0-36c5-97c6-1c49857905b8 | -12.89072 | -62.54352 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e27d2286-1afc-32f6-9480-f579d31d47ce | -12.89391 | -62.46299 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 79d0c9dd-fa53-3691-9ed8-9541d2dbc28e | -12.89439 | -62.45879 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ba6f449a-2732-3671-bc26-085118cce81d | -12.89456 | -62.46157 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c3b3cb3c-ffb6-3b86-9c9c-c666c8826432 | -12.89486 | -62.45461 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1bb2285b-34af-37b2-a799-23bf013e19c6 | -12.89497 | -62.50596 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a6379112-b21a-3a57-b8e7-dbddab369665 | -12.89506 | -62.45739 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8b6abe6f-4570-3dc2-86c9-681569125901 | -12.89532 | -62.50442 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c69c27d3-3d47-37a6-b5d7-2d9c514116f1 | -12.89546 | -62.50169 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bd5186dc-1386-3c72-a887-e185286d1c9d | -12.89583 | -62.50019 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| adbd9ecf-f274-3d45-8fb2-e7062b6676c1 | -12.89652 | -62.54428 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 911d8bec-4293-3017-bca5-0aa9e87227cf | -12.897 | -62.5401 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab2a6621-2025-3ccc-a08e-9b40bb0a866a | -12.89927 | -62.46797 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 72f9e386-29b2-3500-b88d-71c3df5805c8 | -12.89938 | -62.47073 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a3bfc957-aa0c-359f-926f-bae310ecb33f | -12.89975 | -62.46375 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 546b484b-ac0e-3e78-b726-786d51f81bb0 | -12.89989 | -62.46651 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 04b14f71-6382-374d-807c-4971372c8a6b | -12.90022 | -62.45955 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1c068159-9c40-3963-88dd-0506133aac17 | -12.90039 | -62.46231 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 900c8525-1fb4-33b1-9d65-f89f08e5d41d | -12.90176 | -62.49823 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 60a11d3c-6794-3491-b38f-3e9cf65d2cc8 | -12.90223 | -62.49403 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 50c9a69d-1abd-3138-a7c6-5d37944fe25b | -12.90271 | -62.48983 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fc6ebccb-1771-389e-89d8-f16df47d51a2 | -12.90319 | -62.48562 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8a22cbed-74e3-3262-a5b1-654f709b3dab | -12.90367 | -62.4814 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c6c87cf9-2ecf-3cc5-8d18-4b1deb31b29d | -12.90415 | -62.47717 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1382577e-8bde-30b1-ad47-a9582229d784 | -12.90462 | -62.47295 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 9e1ad705-ef48-39fe-8524-b7ad5177c0d4 | -12.9051 | -62.46873 | 2024-10-03 06:10:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ec23fba5-9994-3979-ab1a-464392eb4e6f | -13.41424 | -61.92827 | 2024-10-03 06:10:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43ee42e5-7847-3635-97dc-66f7e4792f9b | -13.42032 | -61.92902 | 2024-10-03 06:10:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56e1fdd3-df56-3677-b269-33e8b3a55a90 | -12.05148 | -61.03499 | 2024-10-03 06:10:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4ce5758-87b8-3560-92fa-9957bacb194f | -12.0578 | -61.03572 | 2024-10-03 06:10:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dba1e62-660e-3453-bdb5-c29b04cd85ce | -12.09031 | -61.19394 | 2024-10-03 06:10:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fea2d2b-6ff0-3d58-a0aa-feb411ce4863 | -12.12326 | -59.78074 | 2024-10-03 06:10:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8dd4346-4f57-3018-a2f8-646fcba2f1e5 | -10.82336 | -68.66298 | 2024-10-03 06:10:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6203756-9d0b-355a-aa76-2caf8207b2ca | -10.86102 | -68.87791 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a2e6032-3da4-3420-9298-220d1acf859d | -10.86273 | -68.88097 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12d00337-9cfa-3e96-8454-cde2f97eab93 | -10.87787 | -68.24945 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e47578c9-8dbb-3ae7-82be-193a71c93832 | -10.90697 | -68.83703 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c747a0d5-ac7d-35b3-a43d-3ff7aa9b2fc0 | -10.91065 | -68.43187 | 2024-10-03 06:10:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cde59edb-4532-3928-aa23-990bb2da6d5e | -10.92414 | -68.2564 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3af7dbe-51ff-318e-947c-869a59b03ede | -10.98002 | -68.45934 | 2024-10-03 06:10:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c9960d6-7c20-39e6-8289-b0ec30b0c945 | -10.55529 | -69.15156 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6e7571b-749c-3ebe-b69c-064aed81811c | -10.14354 | -69.02621 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 607a227b-648b-3219-96ca-d088d4652948 | -10.14782 | -69.02247 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a74d22e1-5274-3259-9349-4fd69e62cc16 | -10.51336 | -69.00432 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78b9c869-7d86-37e4-b6ca-70f406455ca9 | -10.55591 | -69.14725 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa137f11-533d-3151-98fe-de9c97801339 | -10.61208 | -69.0446 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1a94e8d-78dc-3df7-a98d-e18760f6f003 | -10.63655 | -69.05505 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70b42ffb-9373-3b69-8c9a-bac29ab67da0 | -10.63718 | -69.05067 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12f78e06-16a0-3de9-a1b1-3dfdad780850 | -10.7372 | -69.10831 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18113dff-98a6-33b2-9b4a-cddb0c8b6e83 | -10.23452 | -68.63658 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f553b134-f376-332b-98cb-4bebc4be0a03 | -10.25201 | -68.76569 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad29d7a3-35ed-3b38-a0da-31937c1258b2 | -10.25265 | -68.76119 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfc9a792-35c3-353f-8ca4-eda96b2af76c | -10.25388 | -68.63482 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c10a3c6-af8d-3113-873e-aada424018a8 | -10.25572 | -68.63241 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58a070ef-2500-37d5-ac5e-eaa573c5fedb | -10.25572 | -68.76624 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e8626ee-8c3c-33de-a569-3873f70a5efc | -10.25589 | -68.62122 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a78f11c6-370c-3de9-8743-685ce3ba387e | -10.257 | -68.62332 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ede712f-1a69-3ab3-89e2-be6e4b081cd2 | -10.25727 | -68.2398 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a2aea59-022f-36ce-be8a-73b0990a7edd | -10.26686 | -68.76793 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 316b76f1-5c63-3095-8ef5-b47998e1b119 | -10.2675 | -68.76344 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 032d03b7-d470-3222-b613-f0910932a54f | -10.26992 | -68.77298 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64a8e9da-2866-3b14-b009-687ed1ea6ed3 | -10.27057 | -68.76849 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d086dd8-3032-3955-9078-686dd5f7c921 | -10.27121 | -68.76398 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00fac985-595a-31ac-bed4-476d28f7f5bc | -10.27816 | -68.74206 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcef70b8-81dc-351a-ac6b-4d83613cf537 | -10.28188 | -68.74262 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 643af418-7bce-347a-9af7-a140e8514c74 | -10.29587 | -68.27007 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44e13576-4b1c-3eb7-919d-dbfd54ebd7bc | -10.31752 | -68.7067 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21861aca-7e1c-383b-911a-ae903d0992c6 | -10.32059 | -68.71172 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b43b3589-f8e9-3c6f-91d7-8d78db8f89a4 | -10.32124 | -68.70724 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2283bb4-232e-3670-8c14-5cd7c11a2135 | -10.32215 | -68.67486 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cb1cb7a-d596-3c3e-a133-1e507147e45c | -10.36103 | -68.59216 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ed21754-4b55-37a6-b9d1-1eba523b450a | -10.36224 | -68.58983 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46facdaf-f63d-32fd-be14-e760d8e8b707 | -10.38333 | -68.22585 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e7cf747-dfa1-3890-bf6c-1ffc9ea5109d | -10.38782 | -68.16729 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15108a83-77b9-38a6-9f2b-6deae5eff42d | -10.39275 | -68.29584 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 624b90b1-ba67-3f08-848f-21df62e5085e | -10.3934 | -68.61337 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d3082d1-728a-33fd-a373-061775617f6b | -10.39435 | -68.6603 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1f8e73f-7bd5-38cc-a66e-5f60e3b4e093 | -10.40807 | -68.75023 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bc0b115-359f-3048-b2d7-b24f53c7d32f | -10.44288 | -68.31992 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cc87287-0325-3357-9707-2910b6a484e6 | -10.46457 | -68.24985 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97da98f3-7a1d-35d6-b03c-deef9016597c | -10.46931 | -68.53991 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8793ac99-d8a4-38f5-bc77-80e492a32fe4 | -10.4763 | -68.41228 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7accc15a-c416-390f-8bd7-4fe7282d25f7 | -10.47684 | -68.54108 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f7ed9d6-f2a3-3f3f-adac-1276852dc5d4 | -10.47731 | -68.37854 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf558095-4112-3186-aea0-056e3b2fc3a9 | -10.47753 | -68.53643 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a04f0b0-dfb2-3f97-8640-dc8a9bdb044e | -10.47776 | -68.53833 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60d96731-98c8-341b-8c28-81bfea445082 | -10.50082 | -68.67356 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 129f5aaf-6255-3d4c-834a-a105299d4cfa | -10.50147 | -68.66901 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f34d7d6-9c20-3f66-9b2a-fc57e5a8daae | -10.50457 | -68.67408 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a54b144d-c109-3b70-b33e-cbef6ec77698 | -10.50522 | -68.66953 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0ef8b01-a32c-393d-ae89-4b6a9eb60517 | -10.50832 | -68.67462 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fea12193-be8d-3c80-bdef-a3a7abae9bc6 | -10.56997 | -68.69757 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c4940e6-699b-3247-9203-4d7fbe801241 | -10.57111 | -68.77948 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46584752-d2b1-3dd3-ada0-01f4d08bd578 | -10.57483 | -68.78007 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 487065c6-e2ea-3455-8098-9cb7a749937b | -10.58629 | -68.40115 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README197.md)
