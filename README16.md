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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07cb920b-441f-310c-b77c-2d536e8105c9 | -10.75558 | -68.32699 | 2026-06-04 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdac09bf-3976-3d4c-ac4a-25944a56658d | -12.45323 | -58.47483 | 2026-06-04 05:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee43fd47-ea6b-3f7a-9f0d-0222409833d8 | -12.22907 | -57.26987 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8e479649-acc2-3119-88be-d994feb22e41 | -11.6075 | -55.33251 | 2026-06-04 05:50:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c78e0c1-b29b-3f5e-85a3-11d7912de1cf | -12.17557 | -54.54251 | 2026-06-04 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8d554ab-68f9-39a1-ba37-671242bf742c | -12.45414 | -58.46727 | 2026-06-04 05:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ffbfb41-6a1b-30a8-b13b-520069dcb9cd | -12.23497 | -57.27074 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8abe407d-f5f0-31e6-bd4e-b7aab66e037d | -11.89151 | -57.82909 | 2026-06-04 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c06da7-2962-399b-ad33-0a0750ca46e0 | -12.43782 | -58.41718 | 2026-06-04 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2a3258e-bc39-3416-b6ac-adc044f5cafc | -12.21017 | -57.29081 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e05329d3-5eac-3a0a-b1b7-fbe3565d9478 | -11.60089 | -55.33168 | 2026-06-04 05:50:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 129fc696-3588-35a8-8b92-7a49243d9546 | -8.39948 | -70.48367 | 2026-06-04 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30238b0c-028c-3400-9ce5-1f80aec94890 | -12.22301 | -57.28372 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| a54cf4f2-bfe6-32a5-a2c8-36439067d334 | -12.22807 | -57.27867 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ec7c60fc-949b-3da3-96e8-ff4681cb459c | -12.2148 | -57.29 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 6935ebc4-ceaa-38de-a7b3-1732f50d52f8 | -12.7409 | -54.1958 | 2026-06-04 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ec1ee3e-64bf-3cda-8e6a-80a0fe474b41 | -12.21577 | -57.28145 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| a60f2e2d-be55-397c-88fa-fbcb09ba74b1 | -12.18254 | -54.54334 | 2026-06-04 05:50:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fb7fd92-9fcd-3b9c-b832-75d3a8db9418 | -9.6056 | -67.15266 | 2026-06-04 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24b4e890-ba24-38f2-bfaf-89514f5a1e28 | -11.63551 | -55.18614 | 2026-06-04 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5bcbd87e-2341-314d-aa60-2ced1320040d | -12.22353 | -57.27943 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 819f4e87-dd65-3bce-b8d8-cef70a9f05ad | -12.73621 | -54.20603 | 2026-06-04 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1ae66b3-4d84-3601-a4c7-647b9a406a86 | -12.22459 | -57.27065 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 19aaddfa-4593-3cc9-a4da-eb665559af64 | -12.22217 | -57.27786 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c46b39c2-7f05-390b-abd1-185fcf88c26a | -7.94462 | -71.45872 | 2026-06-04 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8c66a5d-58dd-3be9-9e67-d8e52533f8d1 | -12.43956 | -58.40252 | 2026-06-04 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8fb69fb-f48e-3edb-9065-803dd5b52e73 | -11.60683 | -55.33824 | 2026-06-04 05:50:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0924bcd7-68d3-3783-9667-2a701fcb5b87 | -12.21816 | -57.27427 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 08ad8135-0e45-3b8b-839c-1c80ba5f0daa | -12.22406 | -57.27505 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0c38f535-83d2-30f9-b3f2-6f0f552c23da | -12.21607 | -57.29155 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a9f424cc-863d-397c-867b-5afc5319116a | -12.46419 | -58.47631 | 2026-06-04 05:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e366e38-d89e-3d1b-9d3c-069207506b1a | -11.89104 | -57.83302 | 2026-06-04 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 652737bf-0fa4-3835-a32a-6def9c06c2d3 | -12.2089 | -57.28925 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b0340fe4-650c-3771-b81e-cace5609c910 | -11.62819 | -55.19118 | 2026-06-04 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c4b5664a-ced1-3c2f-bfb0-a39525f02ce6 | -12.2212 | -57.28646 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 56f7bb1e-51a6-3995-bfa4-6ec2b1c6bf61 | -10.57531 | -57.3186 | 2026-06-04 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4537e4f9-9381-3e54-8f1a-2e9cd332ddae | -10.57481 | -57.32264 | 2026-06-04 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 006629d3-1d91-314f-9cad-14dcd7dad790 | -11.62459 | -55.18641 | 2026-06-04 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 340a136c-ad95-302e-98eb-6eb623ded26d | -12.21711 | -57.283 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| cd77ce5b-f102-32e7-b691-0566379abeca | -10.57431 | -57.32671 | 2026-06-04 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e8a56b4-74ca-3314-a806-0988cb35b336 | -12.21529 | -57.28572 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| c5cc9982-268c-3282-a186-418895a03130 | -10.56853 | -57.32601 | 2026-06-04 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60959e23-aa93-3cfe-94d4-47b27d2497e3 | -11.88535 | -57.8324 | 2026-06-04 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee90389a-dd7f-3400-84a2-bc878f5cf4c9 | -8.19052 | -70.07928 | 2026-06-04 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77e3d248-c1df-302d-ab9d-7825d1f8b4f7 | -12.22759 | -57.28294 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c2aa5bd7-fb1f-375c-918e-e2b0419f126f | -11.60543 | -55.33662 | 2026-06-04 05:50:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 639e4b17-323b-30ee-9341-c5d337784a35 | -12.73695 | -54.19897 | 2026-06-04 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 96e4ac5d-a1a2-3031-9e30-a52f29546fee | -12.45916 | -58.47185 | 2026-06-04 05:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3745b49c-b7d2-3dd3-86dc-bec6762e97c0 | -10.0316 | -59.33973 | 2026-06-04 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9a1b98c-f027-3dce-8453-dd10bae6c16e | -12.22267 | -57.27343 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5ac71bce-e83d-30d4-bd05-15054902a2a1 | -11.61203 | -55.33746 | 2026-06-04 05:50:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6912407-b60b-36d2-b915-6662479f37c2 | -12.2271 | -57.2872 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf9db4c2-064a-37b6-bc6c-a99d2b290091 | -17.4629 | -55.196 | 2026-06-04 05:53:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 207cf0d8-6726-38b9-8ce0-181d56b68395 | -16.59683 | -58.23828 | 2026-06-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fc410c83-ac6e-3f30-9c3b-817590e8e3ac | -14.09487 | -59.38507 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adca8480-3544-30cb-9d9e-c7c741382bd0 | -16.12774 | -58.50442 | 2026-06-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 78b3ae5d-5a4e-3678-9394-9db1423dd64c | -14.08878 | -59.39118 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 764dc2b6-2729-30b1-b772-c8fc21a1ec00 | -14.09364 | -59.39524 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbc004bb-1b5b-3d46-a6da-0a4f09716d46 | -14.0896 | -59.38434 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2891b43e-a998-3122-88c0-ecac834b181d | -14.08988 | -59.37975 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1aadae1-cf43-3f0b-8e3e-e226359db688 | -14.09437 | -59.38735 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c40df6c-c95e-37d8-887b-dee98c5bb033 | -16.26951 | -59.72527 | 2026-06-04 05:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 985f27b5-95f6-34cb-b9cb-42755582cceb | -16.59055 | -58.24169 | 2026-06-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 95774c27-5742-3b3e-a5f5-8a83a3325022 | -14.09515 | -59.38046 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74bdb90a-ac28-322c-a4d2-4d7f87cebeb3 | -14.08919 | -59.38777 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed519b59-890d-36f6-9d54-d010c4d9897c | -15.81349 | -59.09252 | 2026-06-04 05:53:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84c92a32-7bcd-30db-8187-591b7fdf899c | -16.60182 | -58.24749 | 2026-06-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| cc00f96f-58ab-3258-b76e-926f27ecdc88 | -14.09476 | -59.38392 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19dfc2c2-f374-3438-b4b6-cdbf539bad8e | -14.14654 | -59.00141 | 2026-06-04 05:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e0794e5-1192-3085-a01a-29f5396e10be | -14.08949 | -59.38318 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d569b217-ce8d-363e-9f57-9aa540524566 | -16.12042 | -58.50218 | 2026-06-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0ff507b2-efb7-36ae-ad1b-4867b6e26762 | -16.12244 | -58.49949 | 2026-06-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 019a0301-e8b7-3516-bf65-6fc06b125823 | -14.08911 | -59.38662 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94ab20a2-fd85-34dc-b68e-caf0cbfb3915 | -14.09446 | -59.38847 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2d9d380-762a-3469-90b0-ccb43a623110 | -16.26913 | -59.72864 | 2026-06-04 05:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c954a48b-bdd4-3e5f-8269-d1f96e6bdc88 | -14.09044 | -59.37745 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c60990c-7ba1-32e7-ad89-c2ae2655c5d1 | -14.14697 | -58.99783 | 2026-06-04 05:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45fb0a18-d7a0-38ae-bdcf-9deea837092d | -14.09405 | -59.39187 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70b4bcd5-54f8-34fb-adf3-8439081be5cc | -17.46701 | -55.20007 | 2026-06-04 05:53:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3074508b-68f6-3ced-867a-19352bff25c9 | -14.0936 | -59.39414 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 650ff8fd-945f-34a9-a7dc-145bc300d242 | -14.09529 | -59.38162 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b96ef3b6-912a-39ea-9d75-42c52f40f55c | -14.09002 | -59.38092 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2188a7ca-4472-3697-89e4-31d714ac3672 | -16.1895 | -58.47021 | 2026-06-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 0b43b17f-840b-3091-82a4-034b266fd8b9 | -16.1326 | -58.51342 | 2026-06-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f5aeadef-06ce-30ea-abaa-c7fe64cd2d79 | -17.45995 | -55.19896 | 2026-06-04 05:53:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5976901b-bc3d-3a33-bdb3-f78d4cb6bbea | -17.46229 | -55.20305 | 2026-06-04 05:53:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f36f69f6-504a-36c2-8a73-9ffe7fc93953 | -14.09399 | -59.39075 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e72be90-4409-3f2f-8769-2c180cea401a | -15.81308 | -59.09624 | 2026-06-04 05:53:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ce931fa-82ce-33b0-a029-c3bff33f5fc1 | -16.12201 | -58.50362 | 2026-06-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ff080c3a-6491-3a45-a316-a918f311226f | -16.18906 | -58.47433 | 2026-06-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 9b22b9ce-eeb4-33d8-9656-19686e5466da | -14.08872 | -59.39003 | 2026-06-04 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e4651e5-ef39-301b-b11d-7d9f512c7f54 | -12.2138 | -57.2688 | 2026-06-04 06:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 6090edf0-39d1-3a21-aaf8-3bb871cd2991 | -12.2136 | -57.2888 | 2026-06-04 06:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6d7d781c-8754-39ce-9841-e9892cbb8e4e | -12.2325 | -57.2872 | 2026-06-04 06:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 825b6e51-0291-3256-927d-fe5052201280 | -12.2327 | -57.2672 | 2026-06-04 06:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| eee31f79-440c-3ef7-863d-fc0b04585c57 | -12.2136 | -57.2888 | 2026-06-04 06:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 0d84d465-adfc-321d-8ef2-4079dcea8671 | -12.2327 | -57.2672 | 2026-06-04 06:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 4e49e1b2-5f09-3972-9bc7-76cdf468a760 | -12.2325 | -57.2872 | 2026-06-04 06:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b56c2bd1-f6ee-3165-bc83-9139edb8cd94 | -12.2138 | -57.2688 | 2026-06-04 06:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 0e0176d8-8d9b-31ea-8a60-4d302c2853b0 | -10.3839 | -49.4554 | 2026-06-04 06:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |


[Clique aqui para ver as próximas entradas](README17.md)
