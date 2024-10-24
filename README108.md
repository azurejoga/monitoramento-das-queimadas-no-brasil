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
| 8951a8be-b99a-3318-907a-b9f9f26f52f7 | -19.65637 | -56.76705 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 623e033c-788b-330e-8346-7cf578d44e6c | -19.65633 | -56.74529 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 7ed03bb9-7a28-3cc3-a7c2-451ad57e7714 | -19.57719 | -56.68233 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6a5dd105-b509-3e0c-80f1-ccea63eeae7b | -19.57664 | -56.68705 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ede838ed-6776-3626-ab65-8b53ef5b44ad | -19.57269 | -56.68174 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 34e89744-22e5-350e-8c80-3b81f3038773 | -19.57255 | -56.64328 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 72189f6f-65d9-31aa-a4be-8e2b328d9bfa | -19.57215 | -56.68647 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 6a93e83e-0989-34b2-a1f5-c83853722524 | -19.5716 | -56.69118 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| f796e248-4465-3686-a4db-8166a3bbd80d | -19.57054 | -56.64581 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 7336590c-3fe2-3279-a29e-7abb3a702348 | -19.56913 | -56.63317 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ea27d649-d9b7-3a7a-a70f-d2f70cfeaec1 | -19.5682 | -56.68114 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 790c9e79-dd51-3a19-8b23-9ca066be7f22 | -19.56804 | -56.64268 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 91b4d28d-55cb-3d0f-af1f-64568eaf3ab9 | -19.56765 | -56.68587 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.6 |
| fdf6919e-87d4-3212-92fe-e78f113d43f9 | -19.56711 | -56.69059 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 84ac1787-e722-39be-be71-28b89b370cf9 | -19.56604 | -56.64521 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| fe7d9ce0-504a-3373-8a70-59387467ca9b | -19.56592 | -56.6836 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 58cc4f69-e6d1-35a7-ac89-ec094a6a1874 | -19.56534 | -56.68832 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 630209a1-37d9-3e96-80cd-be34344d4f55 | -19.5637 | -56.68055 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8f4d44df-68a4-3291-b3d3-4c1f91e50aa2 | -19.56354 | -56.64208 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2ffb7319-087d-3e57-adae-4eafa7983e52 | -19.56316 | -56.68528 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e864db44-148b-369c-9503-b6c01957d1fc | -19.56315 | -56.66886 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 692ed6ab-e714-3fc1-9002-bcb8787a35ae | -19.56299 | -56.64683 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d2682571-b120-399b-aa8f-9c187b6a2bfd | -19.56258 | -56.67358 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1c48c605-9bb1-3422-a178-a3d73d536bf1 | -19.562 | -56.6783 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| dad692ae-066d-30f4-ae3c-205ceb6e4379 | -19.56191 | -56.6563 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f4415cc0-c1d5-31fe-995b-39eae0102ec8 | -19.56153 | -56.64461 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d9759a42-a01e-37ed-ad7c-21fd1dcc4526 | -19.56137 | -56.66104 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| aa300367-601b-36fc-8f78-c7391b938b81 | -19.56096 | -56.64935 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2eeb2dd5-6b00-3911-af19-936f2ebd5849 | -19.56083 | -56.66577 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 59e476ad-f913-3a57-8c53-28f0c463d2d3 | -19.56038 | -56.65408 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5999ebf0-7d3b-39d9-bed2-ce5bdda028d2 | -19.56029 | -56.67051 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| aff1778a-2357-35f6-b5ae-40a0a2e45068 | -19.5598 | -56.65881 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7928570d-aa7a-3372-847b-3d612220e865 | -19.55974 | -56.67523 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 73079092-07e0-3d9a-a78d-343c70c889c8 | -19.55957 | -56.63672 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1f1b4f91-b482-3309-87b2-925400c24f49 | -19.55923 | -56.66354 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 44e1062e-51ca-3da6-829f-f1839958c29c | -19.5592 | -56.67995 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c0f05069-f908-3e8e-81af-7a49206074d4 | -19.55903 | -56.64147 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 703ede92-b1a3-3185-a3a9-727106c40093 | -19.55865 | -56.66827 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 43bbe41a-cd33-3415-b998-92859b5bd3db | -19.55849 | -56.64622 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 56238e1c-ce59-3910-83dd-149c213c7e63 | -19.55808 | -56.67299 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| dec713c4-54c8-3289-9ccb-9941d04496d3 | -19.55795 | -56.65097 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d55a1448-6ae3-378d-8438-6cee9358349b | -19.5576 | -56.63927 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 2e15f316-2667-3955-8704-61024d4f101a | -19.5575 | -56.67771 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 607dbaf5-e2cf-39eb-922e-a7fc5dd3186b | -19.55741 | -56.6557 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 861df6ce-4d11-348e-aaf6-66c30d6cf678 | -19.55703 | -56.64402 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6610fe44-0578-30ee-ab9c-3a30ddc29be4 | -19.55687 | -56.66045 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d0b333fb-9ce4-30ef-b297-d71a786ee759 | -19.55645 | -56.64876 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 670802f2-b85d-3056-80be-79a046c3eaf5 | -19.55633 | -56.66518 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 835cd1ea-6a27-32e9-a50e-aa2b21314f9e | -19.55588 | -56.65349 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bd754e2a-e2fe-30be-bcdd-44658e34048e | -19.55579 | -56.66991 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 78217b39-84c4-3543-8a15-dbc3ee432748 | -19.55578 | -56.69184 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 116583e4-be82-3cd9-9c62-d2fc93d5d1ab | -19.5556 | -56.63137 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9b8912bc-90aa-3dd9-9b0a-7cdc044b860b | -19.55525 | -56.67463 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cd57ab71-dc03-323b-a85d-1772303bcc4e | -19.55471 | -56.67936 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b2ce3f21-59e8-3b36-a227-41194f92bfc2 | -19.55452 | -56.64087 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ad1316c9-afa3-3631-8a72-60d79688151e | -19.55416 | -56.66768 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 01936102-bf93-3bc8-8a6f-a6d125ed5258 | -19.55363 | -56.6888 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| debaf867-c5c9-30b4-abf4-6bbe5ecad0cf | -19.55358 | -56.6724 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e666896e-903c-352c-8b6e-ca1efe767c67 | -19.5531 | -56.63868 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 07ebe17e-8f8f-320c-8c46-740a1f76672f | -19.55309 | -56.69352 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 31ae5b60-34fa-38ac-97d0-573dd8061738 | -19.55301 | -56.67712 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3b36e3a6-288f-3631-a9b6-c1bd2308f6a4 | -19.55244 | -56.68184 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4f76506c-a977-3cde-8806-41467546f770 | -19.55186 | -56.68655 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c346031f-b28f-39f9-a05c-4089f12bea55 | -19.55129 | -56.69125 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 79bb249b-a1d1-39fc-8c4c-0b07734841a1 | -19.55129 | -56.66931 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 41ef128d-bd3b-36ac-b4eb-55cbc73db3af | -19.55075 | -56.67403 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7a39bc53-682f-3563-a105-ccd5296ab635 | -19.55072 | -56.69596 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 646fbdb3-616b-35e1-9307-f4015ea4c77a | -19.55021 | -56.67875 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e3f0d971-087a-3726-81a9-55b7611b6279 | -19.55015 | -56.70065 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4d2f40f6-693d-375e-bda6-ec4108f207c1 | -19.54967 | -56.68348 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8f422dae-c8a4-3791-ab95-9566abf6710b | -19.54914 | -56.6882 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d70ed23e-b847-3bed-a112-a186371bf6f4 | -19.54909 | -56.67181 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 290f38b3-4e7a-3be1-95c8-1df591201975 | -19.5486 | -56.69291 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1abbc195-83e2-3e49-9a70-aaff293bd43b | -19.54852 | -56.67652 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| dfc8e930-78a8-32db-99c3-db1012225e90 | -19.54806 | -56.69762 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 47e8e81e-b3a9-3efe-a286-4b8dc8ec4653 | -19.54794 | -56.68124 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| fe80b78f-2fcf-3921-877b-10e1d7d26bab | -19.54752 | -56.70233 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d3ff2596-7f0f-3407-9085-88fbd3a3ce34 | -19.54737 | -56.68595 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 04f8a2c3-ac23-334b-a34c-776e0fd3a8dd | -19.5468 | -56.69066 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d6371ad0-2e23-3f22-ba45-43711ea4671e | -19.54623 | -56.69536 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2313a95c-1db8-3eca-8167-81c8decb7fa9 | -19.54573 | -56.66177 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 03b985fe-bcb0-364b-804c-3f3b5ebb78c3 | -19.54566 | -56.70006 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| cea70481-15cd-3157-8a5d-b3a998de48c4 | -19.54516 | -56.66649 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7f82f9d1-e590-3c6c-850d-c8c6085efa5a | -19.54509 | -56.70476 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 216ed042-f604-3a42-94bd-5fefc3928778 | -19.54459 | -56.67122 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f977f39d-ed6b-354e-90c1-b990ee1ad52d | -19.54402 | -56.67593 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 684be69b-2f40-3140-a10b-fb33659cb6f6 | -19.54345 | -56.68065 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a9698e58-58d3-3509-8f07-e63e4a0a7de8 | -19.54288 | -56.68536 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 297a9352-ed29-3f42-8d99-e03809d8afe9 | -19.54231 | -56.69007 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 82461ce8-85a2-3733-a41b-0ff4e1572469 | -19.54174 | -56.69477 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 86c3881f-7bd6-3ca8-ac7e-5052a97b1fa4 | -19.54123 | -56.66117 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e81ed22f-a49a-3bae-8b17-54de50bec05e | -19.54117 | -56.69947 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 49666c3e-8e39-3b68-9f1b-68aaa75f6ca5 | -19.54066 | -56.6659 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4759cbae-5502-3313-8262-8c387d96419e | -19.54061 | -56.70417 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3ae33712-25c7-30e4-b7de-61382239f6c6 | -19.54009 | -56.67063 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ed68b60d-e1c7-322d-a911-d2c98e0de1da | -19.53953 | -56.67534 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ce3f76d8-b424-3137-a21f-dae3131ac27a | -19.53896 | -56.68006 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| a24dce1a-0a71-3436-bd64-bd3caff3a2c5 | -19.53839 | -56.68477 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| c6fb3356-c545-3847-a95f-60cc6ae61799 | -19.53787 | -56.65113 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 0c821579-bbc8-30c5-b046-2b474d675e89 | -19.53782 | -56.68948 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |


[Clique aqui para ver as próximas entradas](README109.md)
