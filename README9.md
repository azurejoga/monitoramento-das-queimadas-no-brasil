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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37c6fece-8183-3078-8400-c83f079a3b0e | -5.98542 | -44.59429 | 2025-12-14 05:01:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78066f6b-e62d-3b82-9379-8e526f1609f0 | -3.15226 | -54.60122 | 2025-12-14 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22c406a8-af12-3c34-8c6f-e030b67ea81b | -2.4402 | -53.8209 | 2025-12-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d614a6e-255d-3adb-8298-6ec43b1a90b9 | -4.33847 | -43.63587 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c7c7832-3f32-3526-ae4e-b6506541b50c | -4.95349 | -45.84819 | 2025-12-14 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f0abe38-ba9c-3078-bca4-9086c4ad560f | -3.1753 | -52.87161 | 2025-12-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5cd2d7c-6697-3e72-ad20-70b64604a8fb | -3.14376 | -45.36671 | 2025-12-14 05:01:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a255817d-09e8-3167-b291-8148ef495bf3 | -1.88059 | -54.68653 | 2025-12-14 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fce0fbfb-e54b-374e-be2e-a431a3e42605 | -4.69592 | -43.25156 | 2025-12-14 05:01:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de4acfae-5311-3728-add0-3653385b6e96 | -3.46344 | -52.59003 | 2025-12-14 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0f9226f-4989-37c3-9bd4-a7ef77a9f8fa | -4.93112 | -43.95713 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0661fe29-91e9-3d64-b750-2581884fa581 | -1.01613 | -53.55806 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 107e35b4-ac3c-30af-91b5-23f86bf4e9f6 | -2.11655 | -54.21566 | 2025-12-14 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8119db55-ea18-3df2-a264-9eb0d0f0db01 | -2.83772 | -46.72721 | 2025-12-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa3ebca5-73e2-3901-a7a2-49ff082aaa02 | -1.24986 | -52.63482 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e600f6d4-b50b-30b6-afbd-0fea22d16a8b | -1.53763 | -45.58581 | 2025-12-14 05:01:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04417dbf-c3f6-38b5-927d-ded541d25aef | -3.40486 | -54.59062 | 2025-12-14 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 316ba15a-c2d6-35a7-b433-520c3a56cd71 | -1.78476 | -54.15268 | 2025-12-14 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83cf02d2-c2fc-3346-bdb5-337f1664a646 | -4.69444 | -43.24424 | 2025-12-14 05:01:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27e546bb-79bd-3941-b9c0-d69eab4eee42 | -3.42889 | -52.89672 | 2025-12-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7f640293-983d-31bd-a23f-cf3f56266a8f | -3.1517 | -54.60475 | 2025-12-14 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95de5970-3d37-31ad-b3dc-d392c5aa7206 | -2.25283 | -53.67841 | 2025-12-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62052348-8b5d-317c-a3a4-19944407c0d9 | -6.71309 | -47.79441 | 2025-12-14 05:01:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2b1169e-c35c-3a84-a529-0c3c68e79feb | -3.42505 | -52.92107 | 2025-12-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f68c0dc-d72b-360e-a616-0bfd7dfd71d2 | -3.17057 | -54.972 | 2025-12-14 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3ade2cf-9b3b-3139-99bf-bc97f8cb9771 | -2.46539 | -44.17962 | 2025-12-14 05:01:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 06650328-8690-33b2-8dec-147d717f2634 | -3.43148 | -53.28786 | 2025-12-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fa4b7d4-ceda-384c-bbe7-483d5d0b825a | -2.97484 | -60.06997 | 2025-12-14 05:01:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b43f9bcb-4089-3892-8ab6-4a14a86f3501 | -3.43596 | -41.64676 | 2025-12-14 05:01:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 22ad107b-6c65-3a6e-a247-b803b90f3765 | -2.66615 | -46.89671 | 2025-12-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0970718-9361-3b97-beab-b18aead0a2ed | -1.7881 | -54.15321 | 2025-12-14 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2656ed8c-3895-3b5a-8832-ec5f53701c0c | -4.69656 | -43.24725 | 2025-12-14 05:01:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c46824c-aac4-337e-bb64-859092e8b9ec | -4.69384 | -43.24857 | 2025-12-14 05:01:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 810444ee-c6db-3e9e-b71a-74fdbe97c814 | -1.29249 | -52.88178 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5f2cdec-80e0-357d-b8b6-08f49c2bba9a | -2.77541 | -54.52755 | 2025-12-14 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d694e91-38aa-3a46-bdd6-51e5b1c598a9 | -2.47974 | -45.43712 | 2025-12-14 05:01:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c78a0aee-1a8b-32b3-9459-e84c8998991c | -4.34496 | -43.63124 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90362c97-2034-370e-a925-b21011efb6b0 | -1.64347 | -52.09867 | 2025-12-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6bfcb9f-3a5b-3cc0-8361-5948dcb61ab9 | -3.87884 | -42.5187 | 2025-12-14 05:01:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8c65c7ae-cb8b-375d-abc3-954d5ed07ef6 | -1.42844 | -53.47798 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42d58a0e-6c68-38d3-90bb-6cc2af638d03 | -1.62119 | -54.71635 | 2025-12-14 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a4a1835-a4cd-371a-9cd4-e64ec768918c | -1.432 | -53.47499 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c91b08d5-6589-319d-be93-39846f501d89 | -3.43526 | -41.64574 | 2025-12-14 05:01:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 92304a11-de62-30ae-ac1e-f01a47afaa5a | -1.49315 | -53.13176 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba4826ea-36b2-3d0a-aff8-2344164be1c3 | -2.66859 | -46.89484 | 2025-12-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36e99b33-05f9-363c-9c86-300af7f61858 | -3.53777 | -53.02414 | 2025-12-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae7087a6-ae08-3c27-a733-f1d986ad97bd | -2.21378 | -45.68925 | 2025-12-14 05:01:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 606e54a3-d1b6-321c-a233-8e0ba1a30ad1 | -3.57053 | -53.26399 | 2025-12-14 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b87cad93-e46d-3024-b884-95bfbf34f8d1 | -5.99097 | -44.59493 | 2025-12-14 05:01:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75574b94-6dfd-3279-aec5-a60210ee3aad | -4.9347 | -43.96173 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75c90127-87fd-3994-89e1-262b696e06d1 | -3.13242 | -52.45603 | 2025-12-14 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2495c2cf-8487-3c87-a1a6-3a8e7a0f9102 | -1.02277 | -53.55911 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a05d8ff5-98b0-3d47-9679-c4abf11e31a0 | -1.97331 | -46.48536 | 2025-12-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0c959c6-810c-3f91-8093-54524f051def | -3.13297 | -52.4525 | 2025-12-14 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a7f317e-94b0-39bd-bc53-eec4da7e0b96 | -3.46009 | -52.58952 | 2025-12-14 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8833b62a-0559-330f-bbc6-aabac777390c | -4.34377 | -43.63921 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f04ad78d-0680-3e61-8fbf-dd02df20e666 | -1.02941 | -53.56015 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aea5d9f7-4ae9-39b8-a53e-5e2ecfcd6011 | -3.30437 | -52.587 | 2025-12-14 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f4a5d18-ac1e-3e20-b0ae-51ad33cd1350 | -1.35902 | -52.63046 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b71c88df-2f0f-303a-81e3-b6487ff9d445 | -2.66793 | -46.89927 | 2025-12-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b77069c7-c8c2-37e2-95c5-6a9480d4e444 | -3.44171 | -41.64672 | 2025-12-14 05:01:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a14b19be-4257-3170-8c95-ba744aa627ee | -1.5723 | -54.32161 | 2025-12-14 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f83a9a6-dab2-321a-bbc4-aa595ecce026 | -3.43448 | -41.65096 | 2025-12-14 05:01:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 542ceb49-06fa-375c-958a-ddec3051f3ec | -4.33863 | -43.63424 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d77830a0-9d69-3a3b-b52c-018529a2133b | -3.16999 | -54.97561 | 2025-12-14 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad32aab3-4c09-3ccd-ba24-70d41526fc50 | -1.31723 | -52.53166 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fecb079a-2552-3c31-9db0-d503adeab242 | -3.51579 | -52.18973 | 2025-12-14 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6bc91f5-55ad-34f8-914c-6b93ffcf437b | -4.40404 | -44.08709 | 2025-12-14 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2246894a-3780-33d6-a4e5-ab293e364f4f | -3.42556 | -52.8962 | 2025-12-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 631b8055-8f2a-3dd2-99aa-6d21971e6d5f | -1.79698 | -54.05434 | 2025-12-14 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d7a4b4-30a9-3117-9d35-475b305223b4 | -3.8801 | -42.51784 | 2025-12-14 05:01:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4de9bb97-926e-3ff6-a80b-62c545654ee8 | -2.59774 | -54.576 | 2025-12-14 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ccb2b271-abd0-330b-96f0-a815b12f51ad | -4.34477 | -43.63292 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 012e8a3f-6471-3707-b269-caffdb4e81b0 | -2.25532 | -53.55515 | 2025-12-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0dfd822-32bd-3006-aa98-1c12c96712a0 | -1.01945 | -53.55859 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| deb7b1f5-31bb-3967-bf2a-0af01067e6fc | -3.12907 | -52.45552 | 2025-12-14 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f941db44-8bdc-3509-a9d6-5bb4a94334c1 | -3.4424 | -41.64776 | 2025-12-14 05:01:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c2e5968a-b246-3619-aef5-ae4049f17fbd | -1.62459 | -54.71686 | 2025-12-14 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8beb7c2-a0d8-3fc2-b3ae-f6c26df88c99 | -4.3442 | -43.63691 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f65afea-1855-3e47-bc13-1aa8e6cf12c7 | -3.14835 | -54.60422 | 2025-12-14 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 951100d4-35bf-306e-a2ea-9074bfd3b30d | -3.14333 | -45.36958 | 2025-12-14 05:01:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c37d9e38-9fd5-33bf-9d39-50b6a1ff7de8 | -2.1892 | -53.67198 | 2025-12-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 426168a3-8d23-3f3e-bb33-e424cc9f8984 | -3.15561 | -54.60175 | 2025-12-14 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fe26295-c294-3724-ba07-d141f106d6ae | -1.43146 | -53.47844 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ee7101e-18b6-347d-82d4-38cc8f0a0c41 | -2.97036 | -60.0692 | 2025-12-14 05:01:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e7f2981-933c-3f71-86b3-086283139183 | -3.40152 | -54.59009 | 2025-12-14 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8269eb38-7783-38b4-8170-b44ff3743251 | -4.40351 | -44.09076 | 2025-12-14 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2233d96b-2012-3b67-88a2-f32fb2036bb0 | -4.93055 | -43.96118 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c392aae-9690-3d4e-8d25-46f7e15bfe51 | -1.78531 | -54.14919 | 2025-12-14 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab339490-3f87-3f8a-b4bf-601baf613c5a | -2.88738 | -44.96531 | 2025-12-14 05:01:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| debd5d6f-9698-3785-adc0-806ee6e949d8 | -1.37223 | -53.57523 | 2025-12-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6cbf3ff-5b7c-35a1-ba86-da7e0f8024a2 | -2.972 | -60.07188 | 2025-12-14 05:01:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf5cd258-11d4-3f94-b787-c8d0945649c8 | -2.24951 | -53.67789 | 2025-12-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb0669d4-e016-337c-a0a3-3b01d9d6678f | -4.9353 | -43.95769 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c38a3b1e-2695-3b05-8616-be59e49e1757 | -1.42898 | -53.47453 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43febcaf-8049-3b86-a955-57320c2ea840 | -2.848 | -45.40007 | 2025-12-14 05:01:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bd425e0-3c15-35df-9d20-9c3a864b865a | -1.02996 | -53.55671 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29192160-afbb-35a5-b87b-86075459ae51 | -2.83703 | -46.73176 | 2025-12-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 269a6f72-b595-32a5-ae21-823718f8acb5 | -2.46489 | -44.18295 | 2025-12-14 05:01:00 | NPP-375D | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d1804e9b-46c5-37ce-9616-d516c9fcce21 | -4.9368 | -43.958 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README10.md)
