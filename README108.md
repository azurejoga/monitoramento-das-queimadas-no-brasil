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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a2db202-84e9-3482-b91c-7a6075394980 | -16.85983 | -55.90624 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3196daf9-8289-35d9-bdfa-f2854d8db090 | -16.85877 | -55.84851 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b94a4750-4b78-3282-ab95-41ed271c2996 | -16.8585 | -55.91425 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d6e10ca5-83a4-3d8e-8b58-4f9bab29a4e5 | -16.85837 | -55.89362 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 55c5c343-61be-3611-a919-3c215c1a224c | -16.85797 | -55.83199 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 247ed70c-a7c6-3c68-bb3d-1372bac03e57 | -16.85783 | -55.91825 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 23e6c9ce-6862-3605-8b16-3d9147bf6060 | -16.85597 | -55.84391 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2517f074-d3e1-3f55-a310-0df9093124f1 | -16.85569 | -55.90961 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 65af80f4-28a1-3ddc-b477-2f4d1a7f7a5b | -16.85451 | -55.83137 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e7250568-e4dc-32d5-ae6c-f79a23f8591b | -16.85289 | -55.90498 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8d9af1b4-b62e-343d-8dd3-591118669105 | -16.85251 | -55.84328 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5c03f96a-7afc-387b-9bea-eccafb5ca11c | -16.85222 | -55.90899 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dd25d97c-96ec-3ad8-80f3-2de8e57f5161 | -16.8521 | -55.88836 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 01b340ea-bc32-3ce9-9fc8-74f76a661aed | -16.85118 | -55.85123 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 95a81716-a010-3f99-ac7e-ae4b36febb4a | -16.85112 | -55.95833 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 00949f6b-9bb7-3fd1-903f-b5d5a90b1854 | -16.85088 | -55.91699 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 395cc074-8f0b-3bab-9c0e-888892fabeb9 | -16.84863 | -55.88774 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 68e1814d-f597-3127-aaf1-d1b940fa7e16 | -16.84838 | -55.84663 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ef1f499d-c63a-3891-9d29-749e7225df98 | -16.84662 | -55.89973 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f4469707-77ab-3a46-9efa-cfd51b49c12f | -16.84516 | -55.88711 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 4014e584-96a8-38aa-b5ee-4e3fc3c7ef36 | -16.84218 | -56.0813 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fe39cff7-4dda-3013-b742-10a5eeedb0bf | -16.84148 | -56.08535 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8948d9c3-8732-3dc4-bb2e-d7b190e3fd9c | -16.84034 | -55.89447 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 66879a23-3798-34ab-b7d3-9c356cb24580 | -16.839 | -55.90246 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8dbdebbb-418e-35f9-a345-8cf04f0c0bd5 | -16.83868 | -56.08066 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| efefd2aa-f7d6-34c9-8351-76a6494c63fb | -16.83798 | -56.08471 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fc8241d3-865d-38b0-af7f-882286cf58da | -16.83711 | -56.08482 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8bc5100b-5037-3d11-b7c8-12dc49cdd971 | -16.8362 | -55.89783 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c4ca43ba-31b4-30ae-a549-c80d3895b641 | -16.83609 | -55.87724 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 66af30e8-1db4-3d96-8936-dba1718ccf7a | -16.83542 | -55.88123 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f2990c6f-9488-3974-83be-626d738ceadf | -16.83517 | -55.96786 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 94a4929c-26e5-3f28-9bfb-45b0f57f603b | -16.83486 | -55.90583 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5be2fafe-b416-356b-8e01-79fce7837343 | -16.8345 | -55.97189 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 73ee8d03-a2cb-387d-9117-609777d57e3f | -16.83408 | -55.88921 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f8c0ef0e-f651-30f8-b876-3cd0aaf0bae8 | -16.83351 | -55.91383 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 967b6ec7-d163-3aff-9b19-4a77ce9b5da0 | -16.83273 | -55.8972 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| aa40dc37-db32-3bdd-b5e1-20a276e134a0 | -16.83216 | -55.92184 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1373ea83-1dff-3416-ae99-2cd54acca447 | -16.83206 | -55.9012 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| cff67433-148f-3bcc-b0ad-23d1c0d3a6b7 | -16.83195 | -55.8806 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b5385c97-6426-3a5a-a4eb-75e5b9d5a3d4 | -16.82936 | -55.91719 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 75252e53-b6ba-3f6c-99dd-507adf493eae | -16.82781 | -55.88396 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 94a2482c-b716-39fe-92d0-8bf47fad95cd | -16.82714 | -55.88794 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ad5207a9-db5d-3f0f-9073-4c180cad9779 | -16.82656 | -55.91256 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 60e63707-3c87-3e02-8c91-4f9d9f556491 | -16.82647 | -55.89194 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4e4d41da-505b-3350-b4d2-7cd005eaddd9 | -16.82589 | -55.91656 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 83780776-2944-3d69-9aff-f033af4cbe66 | -16.82579 | -55.89593 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c128e613-fd0d-3f2d-ab8f-91fa6940c2e8 | -16.82299 | -55.89131 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4cf1413a-cd84-3f3b-8241-e84d76ae0769 | -16.82154 | -55.8787 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1628ae31-1c71-325f-a85d-5e4f6fcb6927 | -16.81952 | -55.89068 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| eeb70f34-1f71-35a8-8d02-a5ab2e46ebc4 | -16.81885 | -55.89468 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 42d2716c-2a5f-35d1-b387-0309b6201234 | -16.81875 | -55.87409 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 62c272f9-b4ea-3c04-82ea-1e32119386d1 | -16.81709 | -55.96872 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 80dd751f-a4a6-38d6-acdd-3b5a255627fb | -16.81528 | -55.87346 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 54c2e256-0a35-3608-b810-fed71eab02c2 | -16.81393 | -55.88143 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2046ca3c-abe9-3167-b364-1f9817a5c807 | -16.8136 | -55.96809 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1b1fa3b6-8d90-34b3-aad0-febc9935c047 | -16.81326 | -55.88543 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fa6e6368-989f-3a0f-ae35-2247485be475 | -16.81276 | -55.9307 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a76debb4-6855-33d5-a471-40f9bea77f97 | -16.80928 | -55.93007 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5426dfd7-ed94-384f-8ae0-a72055f989b9 | -16.80596 | -55.97085 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f5289ef3-a35a-38df-ad80-4ae4b2ef9785 | -16.79537 | -55.92756 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 13b27156-601b-3edf-b88a-2995ee458adb | -16.89454 | -55.83847 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 4813f58f-072f-3915-9635-5f8e5295eacc | -16.89386 | -55.84244 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 59334031-7e76-3256-a3a9-c34a8254c043 | -16.88415 | -55.83659 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7a5070b2-6b13-304c-beb0-0328c4342017 | -16.88347 | -55.84056 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f15ac578-8987-3b78-b440-c4b62e5d3df7 | -16.88211 | -55.84851 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 732fc602-0a4d-35fd-8b5b-8747331d4794 | -16.88001 | -55.83993 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| f973635f-8fc3-3fa2-b478-7a04f2a5508a | -16.87875 | -55.83574 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 39.1 |
| 0d68f5c8-945c-3ea8-bd8d-1b0632c211e5 | -16.8779 | -55.83138 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b597fa1d-5a3e-302e-a7ee-91ffa9e48f0f | -16.87742 | -55.8437 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 1a65cac8-0729-394f-ad55-47a12817f861 | -16.87723 | -55.83534 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| a3937950-7809-3c8d-b939-ca1b76301af3 | -16.87676 | -55.84767 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 8ab17aeb-e702-3efb-9430-7a82987bd693 | -16.87661 | -55.82719 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 065f7e9f-853d-36aa-a51d-f8c85212f94d | -16.87655 | -55.83931 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 96d62252-f3e5-3e9a-92bb-bd85a49817c4 | -16.87594 | -55.83115 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 32661ffb-0c90-35b6-8b34-f79dc8f6fa2c | -16.87587 | -55.84328 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 484763c7-0da7-339e-a98d-04bd9562b0e6 | -16.87528 | -55.83512 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 39.1 |
| 7416d1e5-c7fb-3603-97ab-3a3ae36384b0 | -16.87519 | -55.84725 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 753b5ad8-c3e3-3ae0-bf41-85c842f4c5d4 | -16.87396 | -55.84306 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 18f1070b-4c70-36b8-86ee-64f9094cc4f0 | -16.8733 | -55.84704 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| e97b9a6b-cc31-35d3-b814-dd965a535298 | -16.86902 | -55.8299 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2340c99c-9272-339b-bcc2-7a38f58c4268 | -16.86637 | -55.84578 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 72e82842-a217-30e4-8b2c-0478d8d86480 | -16.8657 | -55.84976 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 0f53f2f3-be0c-3ba1-91da-8fbe50d48f9d | -16.86077 | -55.83659 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 61e71a7a-9e02-3b4d-9f56-5b5ab82a62e9 | -16.85944 | -55.84453 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a6c7cefd-95a6-359f-9f2e-2988e2cf8ee8 | -16.85863 | -55.82803 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 80861324-50a3-333a-95cb-b9577292866a | -16.85717 | -55.81548 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 33e2e7ff-ccba-3581-9055-3e9db923f681 | -16.85531 | -55.84789 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3b6ee70b-44db-35f0-be00-903479a1e654 | -16.85184 | -55.84726 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2ea57b6c-5430-3596-a46e-4c92fcf53d6c | -16.85171 | -55.82677 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f4aa9422-5c34-3576-aafe-847ca875d8be | -16.85105 | -55.83073 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 78628c20-6bac-3ac0-92c6-7d0f22468c65 | -16.84759 | -55.8301 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b6996869-5438-354a-8909-551909bf99be | -16.8045 | -55.78962 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f2195b1c-d112-33dc-abd2-b690d49cd1b2 | -16.80257 | -55.82197 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 43004819-8847-35a8-85d9-33f618ed32d8 | -16.79758 | -55.78837 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a4ce1e00-c704-3315-860e-39fe859d6b57 | -16.78999 | -55.79108 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 15a80f14-4b04-31e1-9811-4a2ed2fec2cd | -16.78653 | -55.79046 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f088bb69-a803-3089-9ede-8753b2525f8a | -16.7851 | -55.77796 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b8f4a70d-d1d9-3e48-92c7-b6a47c4e8cf2 | -16.76137 | -55.77866 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d98a8c26-489d-3c4e-8295-1919134e652a | -16.72084 | -55.49274 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 482c3847-98d1-3845-9108-6b0adbf3c12e | -16.7123 | -55.50374 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README109.md)
