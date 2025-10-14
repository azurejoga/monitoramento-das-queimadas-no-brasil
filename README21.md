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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33005d67-63b4-3c67-b29b-060084c0bd14 | -12.83129 | -50.67545 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd941a09-392d-308f-9ffe-11e29b93c197 | -10.80193 | -43.948 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 352c7645-b4fa-3838-9a77-70c3c04243b4 | -13.53431 | -43.01045 | 2025-10-14 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bb440831-3c83-316a-90b4-7a4b43d93f74 | -12.61647 | -48.3109 | 2025-10-14 04:06:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 16df4177-6d2d-349a-8dbd-1c6a7e983c19 | -13.53566 | -43.00702 | 2025-10-14 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 029072eb-6d8f-387d-8506-0d4ca5f642c8 | -13.90606 | -41.46159 | 2025-10-14 04:06:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e556b49f-bd16-3420-b414-4dc6aca453cf | -13.00069 | -43.9994 | 2025-10-14 04:06:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 554a1a78-feef-3511-a40e-5adf3811ea3e | -12.8339 | -50.6622 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e4342f2-7efa-3c6b-9763-6b38cd2693a7 | -10.03934 | -43.81113 | 2025-10-14 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e960679a-4b7f-3cf9-a906-53f7e8ca45f7 | -12.20442 | -51.03059 | 2025-10-14 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ea86997-677c-36ad-aea1-f907d7cfa242 | -10.80482 | -43.95271 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac65122d-1115-375f-8c25-8a0491a1cb95 | -15.37275 | -43.03733 | 2025-10-14 04:06:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 158e75a4-f66e-3a3b-a988-f9feaea74d33 | -12.20998 | -51.03286 | 2025-10-14 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 037d5876-0067-3405-b3d6-56a495bb2b68 | -12.82336 | -50.66005 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a4a6f5f-62f7-3ea4-a1c9-48b1f242c96a | -12.85025 | -50.63465 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3e0426ab-9c57-3802-81de-edd748c2ac8d | -12.82467 | -50.65344 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbb074bf-afe6-3863-b5f4-33e5b469bf38 | -11.74905 | -43.28881 | 2025-10-14 04:06:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| a0ca6ee1-5781-30ef-b4f3-92542497541b | -12.84435 | -50.63688 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6bbf28d7-c781-3512-9956-486a4358e97e | -11.7456 | -43.28822 | 2025-10-14 04:06:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 1a205087-9405-3a94-a106-1861d7a6a879 | -12.84241 | -50.64676 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4878751-984e-3bdf-a35c-48b78491de33 | -12.79257 | -50.6566 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10af0fb0-0817-367d-87cb-aa2238195c86 | -12.20988 | -51.03172 | 2025-10-14 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b48a28ff-e335-32ef-bba3-07e89205650f | -12.83851 | -50.66658 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4688170-402a-3116-94ce-cb00b8f32bb2 | -13.75389 | -42.43849 | 2025-10-14 04:06:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d7ea9b3b-b7ac-3dc4-836f-1561a8353725 | -11.29521 | -44.02894 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c647718c-7351-3793-9e31-f2417acdde92 | -13.84444 | -42.38738 | 2025-10-14 04:06:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fca5aab4-418f-3ba2-8f10-1a2d876c3083 | -10.1565 | -44.92037 | 2025-10-14 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce9f0dcd-eecc-363f-914b-dbc5f3057a0a | -12.02182 | -47.80547 | 2025-10-14 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 556e7157-8414-3b18-97df-f053e25df3d9 | -11.29232 | -44.02421 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 50fa2bc4-00cf-3eb8-9e04-ad4cb64dcad9 | -12.8148 | -50.64798 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25db47f0-947f-39d1-b31f-18fb28b2d0cd | -10.1527 | -44.91974 | 2025-10-14 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f5c4917-0360-3795-9bc8-24790a836076 | -14.02292 | -44.00326 | 2025-10-14 04:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fddc367-8d87-31ce-8877-8269ee09bc93 | -12.78731 | -50.65551 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76096e90-7fda-3f0d-ac34-42ca9f0cc5e1 | -12.61639 | -48.31437 | 2025-10-14 04:06:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1c862df9-1aa4-37aa-8c7e-087dae9e8405 | -12.82018 | -50.6554 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3eed25a6-60fa-3dfa-b3b2-be0d7b2a1f95 | -13.68067 | -44.37958 | 2025-10-14 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f20db696-9ec8-381d-af77-dd24bbc35cdb | -12.79321 | -50.65329 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9ceab93-1f1a-37ff-868f-55ea927c739e | -12.26882 | -46.76659 | 2025-10-14 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bfcbae09-6414-31b9-b480-3488999276c7 | -11.74277 | -43.28379 | 2025-10-14 04:06:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9d9cee9b-2467-3c0c-afd3-57e98503ee9c | -12.845 | -50.63358 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 532720a2-e9a2-3c10-83a1-7d061a1a0cd7 | -10.81774 | -43.9635 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 71eb9046-c342-37cc-97d0-204fca8fbbf1 | -13.63417 | -42.85021 | 2025-10-14 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c557e305-eec2-32a2-b979-43545093798d | -12.83123 | -50.64792 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b6c015b3-c0ca-37c3-9bcf-6dc1ca854496 | -12.23614 | -49.39053 | 2025-10-14 04:06:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b2ab118a-6fc2-3e58-a872-89e5fbb0c640 | -12.83786 | -50.6699 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68a7d7f5-c070-390c-9bbb-cfae5f8adc96 | -12.80501 | -50.64882 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6431fe4c-1146-37e7-95b4-699ad71a6afc | -11.33398 | -42.12747 | 2025-10-14 04:06:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1c4827df-515f-331c-940e-3071723bb823 | -12.84305 | -50.64347 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 41a0fe24-2b7f-39e6-a3f4-192bc7f87f97 | -12.84969 | -50.66544 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b85e0d46-d613-3d6d-8bb0-822b686201d1 | -12.81681 | -50.64438 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11be8679-6ca5-3274-a217-731ffecf096a | -12.82667 | -50.67107 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad72762c-b78c-3dde-962e-61c6d004f0f2 | -12.5843 | -43.41469 | 2025-10-14 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a273002e-2cf1-3a3a-b7eb-a577db1c3faa | -11.29589 | -44.02483 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3ff9768-b485-32bb-ad33-8aeb3b11a05c | -10.67336 | -45.15876 | 2025-10-14 04:06:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b48ab874-e620-3219-8f76-57d986377f7e | -12.80565 | -50.64551 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1f4adc99-5ec2-3292-a633-d0fbadce886c | -14.78414 | -42.60406 | 2025-10-14 04:06:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f113317b-d86b-31cd-a9db-5f0e3a9e7289 | -12.84111 | -50.65337 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0826c94c-4b99-393e-83f4-1f0892d137e4 | -11.56423 | -44.05497 | 2025-10-14 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7cf35f1-26f3-316f-b193-70737b7851af | -11.53062 | -49.28341 | 2025-10-14 04:06:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01b1e0d6-c0a4-3fba-896d-bd46bd1241d7 | -13.6842 | -44.38023 | 2025-10-14 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8273f044-e675-3326-a454-a8d20eb026b5 | -10.2369 | -39.95069 | 2025-10-14 04:06:00 | NPP-375D | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3fbc140c-6e70-3907-a643-8ff7d6cee550 | -9.11502 | -44.67739 | 2025-10-14 04:06:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a955470-1034-30ee-a699-a5f14aee58ca | -12.82733 | -50.64656 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bc02cc4-3231-3406-aa6f-486216917af6 | -12.88653 | -43.12682 | 2025-10-14 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c8aa2c0-40a3-3d67-ae40-32d543d3c112 | -12.83916 | -50.66328 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1dbb661-aed6-36b8-b8d3-e82907224007 | -12.63003 | -44.11811 | 2025-10-14 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc4ae0f1-9276-3156-9797-a1b938c0012e | -12.83058 | -50.65122 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6fd8087-6d84-3791-82fc-802d3b20bfeb | -15.37551 | -43.04155 | 2025-10-14 04:06:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 013a4c68-07bd-336a-8aa2-efabdd4ec5af | -12.85292 | -50.64893 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d21ac4d2-bd74-3123-9625-c80a9ffc63de | -12.80822 | -50.65351 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82c76255-ba87-3cd8-a64c-48bcd255cfb6 | -12.21067 | -51.02927 | 2025-10-14 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46d5bc18-631c-30dc-8218-8feb68aaa1ad | -12.85391 | -43.81682 | 2025-10-14 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 727ebd16-ec2d-3b05-a39e-5d7bdda3d6e0 | -12.61727 | -48.30968 | 2025-10-14 04:06:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ca9589ea-a3b5-304a-aa80-4d087af4863f | -10.36222 | -44.98477 | 2025-10-14 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f20f777-7679-3604-80b1-4a71c3ed6ee8 | -12.83974 | -50.6325 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10252dce-523c-34fb-a7ba-89eb55b1b567 | -13.32843 | -40.90383 | 2025-10-14 04:06:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7c2e614d-b7b3-3d90-a56b-f922ded9c1aa | -12.82797 | -50.66444 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88da17cf-75dd-3848-b62e-e45c2a39b91b | -10.81416 | -43.96285 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12f85fa5-8114-3707-bb24-8a57ae4ac7e9 | -12.68589 | -38.55283 | 2025-10-14 04:06:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fa5fd5ec-008c-3418-be84-146d0bb97629 | -9.08779 | -47.95858 | 2025-10-14 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 706b7752-8fcb-3fcc-a2c6-51ac44ea7f16 | -12.62935 | -44.12217 | 2025-10-14 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5da1611b-6254-30a0-9020-9ab840ce244a | -13.832 | -42.42213 | 2025-10-14 04:06:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 18f2296e-2ab6-3aba-be8b-e826c0ba3092 | -12.63447 | -43.44622 | 2025-10-14 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33e58c91-147d-3782-bf5a-c83e6e52a141 | -12.83259 | -50.66883 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 396387e4-3853-3e76-800d-cec0de54b3e2 | -12.24626 | -49.3638 | 2025-10-14 04:06:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8872b3c5-2231-3fbd-9565-7dbb7de3d1df | -10.81128 | -43.95809 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82bd09a4-33c7-35dd-8170-260ed90f6701 | -12.82271 | -50.66336 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f079e74a-5a7b-3ba6-bac5-c0cb7923a872 | -12.83715 | -50.64568 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5dd11cec-2f0b-3d63-ae45-78c990754cd7 | -11.56066 | -44.05436 | 2025-10-14 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90c85dbc-ecce-3860-a8cd-6b56634ed5e9 | -12.79385 | -50.64997 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6372048f-0784-3a17-bc36-f10566c25ffc | -11.29163 | -44.02833 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 814266f5-c307-3a9a-b923-cb1c143d48af | -12.65894 | -43.42687 | 2025-10-14 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d395341-42d6-3f8b-bec1-ef382de8b0cb | -11.52242 | -43.50866 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c914aa3-e5e6-3f82-b1a1-cae85b0e34c6 | -13.63753 | -42.85082 | 2025-10-14 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e20b7cd3-451c-3b15-86a5-57154b6201c9 | -12.61273 | -48.30567 | 2025-10-14 04:06:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d18ada05-4080-3132-8d16-37de458b3aae | -11.74623 | -43.28438 | 2025-10-14 04:06:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| bd1099f3-2687-3e53-a420-b3d4a9c61169 | -9.49106 | -43.06106 | 2025-10-14 04:06:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4742cf64-f99c-3c17-a829-db01b06c7dfb | -11.74215 | -43.28762 | 2025-10-14 04:06:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2101b8c0-d748-3110-b521-b02992a368e4 | -12.21059 | -51.02813 | 2025-10-14 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c52079c-65e5-3bf4-b0d7-546610de3c08 | -11.5246 | -43.51707 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README22.md)
