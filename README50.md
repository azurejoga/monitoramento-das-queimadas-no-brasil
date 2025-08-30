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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 663ba322-94b6-3e96-b867-67ab8055ef24 | -9.45108 | -62.34991 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cc083c33-b88d-3b04-bde0-de891fea4049 | -7.61607 | -42.72976 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d5a637fe-ee08-3b4e-a045-9aaed778887f | -9.78314 | -64.2504 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9430ab5-4aa2-33ce-91f3-a419efb1c400 | -7.77498 | -45.47591 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dd6f49a5-11fc-32ee-8379-99f5bb63f91f | -11.84823 | -46.39654 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac7fb448-b400-34d2-8851-0566b4a4f680 | -10.48872 | -51.6217 | 2025-08-30 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 684034d3-b476-381c-90bf-8f5306a19bc7 | -10.84324 | -53.76778 | 2025-08-30 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b98d77d3-01be-31d1-8cb5-69a76211fce1 | -11.83999 | -46.4579 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 8ea7a2f0-c18f-36b8-a3f3-721f6d0133f2 | -10.37385 | -59.20449 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 693fd637-89af-3011-9d9e-5345456312a4 | -10.07225 | -48.86509 | 2025-08-30 04:49:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f045d96f-884a-3570-865a-d9f1358dbd55 | -7.16994 | -44.15742 | 2025-08-30 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe6c2d24-764b-32e5-b5d1-4a8386bc5795 | -11.06441 | -52.04594 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76341d66-78e3-34ae-9d2e-98109da9c2b6 | -11.88173 | -46.37264 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a81a9b92-5fbd-37ea-8e34-d4d6f8f99dd0 | -11.86641 | -46.45358 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 71787259-72dd-301c-9c60-4176db9ac824 | -9.15086 | -59.56712 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2ac708fc-ec39-3326-93d6-e61687154f1a | -9.58861 | -54.49186 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2645e547-8d45-3fbd-8f90-e2d3ec95b1ea | -7.11335 | -44.5843 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d41dded-c70b-34e3-af65-89e961d17271 | -8.34372 | -47.41903 | 2025-08-30 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2004a161-1832-3076-b5a6-605321d5d271 | -9.69498 | -48.304 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac36eb75-1685-34a2-8bb4-51984f6c2360 | -9.43954 | -60.5624 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d814154-fd67-34d8-8e90-17fa543dba8a | -9.58285 | -54.48243 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b12a8141-44d6-3e91-9476-535622ec8aee | -9.17628 | -59.57485 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55a25de3-befd-308a-928e-1dfbf855d92e | -9.45952 | -60.57007 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea3b39ba-5d5c-3860-9bd2-48bee3f7e249 | -11.35977 | -43.54819 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41d78171-d64a-3e89-be0f-30ff58b4d16e | -10.99965 | -46.95986 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8c08375d-eadf-3804-882c-f1e9aa33a2d8 | -9.50566 | -45.3934 | 2025-08-30 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82e617b4-16ee-3f78-9ac8-0bb1b7549d08 | -7.37976 | -48.19183 | 2025-08-30 04:49:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f42eb6e-739e-3cb4-9ead-a4655cea19d2 | -7.15806 | -44.14162 | 2025-08-30 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9ceee02-f67f-3bc0-8b36-c78206ff6b38 | -8.287 | -61.40117 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf4aa444-f97c-38f0-b816-f0f7069726f9 | -7.15659 | -45.2367 | 2025-08-30 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b267b9f-0163-32ce-809d-0f9770c185f5 | -7.74499 | -50.26625 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a88490ac-d4f9-31d9-8f19-1355efaa22c7 | -9.44181 | -62.33488 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 902a4e94-7e53-3bdf-bcd8-feecebf7eb2f | -9.94033 | -44.0265 | 2025-08-30 04:49:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| debf426b-95a4-3bc5-943c-4d9a035f6682 | -8.87173 | -60.73201 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08169ac8-6a56-39ad-814b-acb30bdc106e | -9.44439 | -62.35305 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a5a0fc6f-02b2-3b0c-8a65-43438e52f899 | -9.50203 | -45.38617 | 2025-08-30 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc15e3c1-414e-32f4-87b1-3065a4c226c6 | -9.70383 | -49.47169 | 2025-08-30 04:49:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc4ee204-932a-3463-9b0b-47a1ed51ef37 | -11.36082 | -43.57949 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd4d20e1-bb56-3d96-9d1a-9f0d019fb15d | -8.54886 | -51.30899 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14566366-c780-3e3d-ad31-3f9c7839a69e | -9.43513 | -62.33801 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ef9a1682-c03e-3303-97fc-5b4732b3a703 | -11.30985 | -43.65196 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27295777-a46d-3d69-b1c4-61e078f92b00 | -9.57706 | -54.47318 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 685315a5-dae3-3f32-94ea-d11e8b3e0476 | -7.20511 | -43.70498 | 2025-08-30 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22a2005e-7ce7-372c-8024-156a8ea984b8 | -9.11559 | -46.04657 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 799063fe-6ce8-3261-b8be-f61dc1ccac9f | -8.18356 | -61.37843 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a7055a3-364c-3b20-b1e0-ec4f9f0bee4a | -10.4561 | -57.94806 | 2025-08-30 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2434859e-70fd-3d40-9028-02bb5981fba2 | -10.72052 | -47.00628 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 841ff835-ee24-33a6-b885-a34896f2c807 | -11.84299 | -46.38039 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9794740-3155-34ef-8b31-2f46cb4a86c1 | -8.71047 | -50.36087 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1effc51d-bf86-3525-8b62-14a7e40440bb | -10.70699 | -47.07334 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af33a3d3-3236-3151-a428-d8d60b792f49 | -11.83258 | -46.44895 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b7cc1bda-6e4a-3977-bee4-f25cde46459e | -9.44421 | -62.32241 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d049190c-4895-3fca-be43-dc50c87abedf | -9.50583 | -45.39093 | 2025-08-30 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f542fe1-3c13-3911-aae3-e491815678e6 | -11.88401 | -46.38766 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fefabe80-b056-3f36-8257-faa2e9706824 | -9.46098 | -62.32994 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 90156d96-d619-3c1c-8174-62a1c3dcfd12 | -11.86587 | -46.45758 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7028c13c-1c2b-3a9e-99a1-5213e5dd3e80 | -8.55091 | -63.02985 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b9c1f61-8da4-33e5-bef8-837e5631a778 | -9.44869 | -60.54119 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f7b7ee8e-1b41-3afe-aea1-10e936b05495 | -10.99119 | -46.84539 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65edf08c-ed2e-3a45-a1f1-05a928480220 | -7.60573 | -44.95125 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2fc4640-10ce-350d-9bc0-ecdb9f625b44 | -9.13223 | -65.81553 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af80047c-019e-3792-8908-9bc897b0aa07 | -9.10725 | -46.04532 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e1a2952-698f-3676-9b25-93c324f064f5 | -8.90194 | -62.10506 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6971c87f-9cd4-36a9-9017-08f6f5ad98a4 | -9.44945 | -62.35837 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ed8cf1cd-8c1e-3c7f-a261-36ef7acea171 | -11.32192 | -43.63866 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 63ded020-1b0c-3baa-828a-ed68c0a03745 | -9.45027 | -62.35412 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6ccaaad3-a952-3f58-aab6-7552727b4964 | -10.18689 | -48.91919 | 2025-08-30 04:49:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0df14245-d6f7-3525-961c-0499168374dc | -7.64703 | -42.65902 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 618d76e7-3168-3658-bd19-3cc45b4cbaca | -9.44687 | -62.34017 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b6e1adf7-bdbb-3bb0-b95e-2e95eb40e66a | -11.8316 | -46.46122 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 66d4e0ac-2ee2-365c-a57d-5e7b08dcc216 | -8.67515 | -62.43704 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06553271-b6bb-3ca1-a772-587cae49b45d | -7.17059 | -44.15285 | 2025-08-30 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bc51940-9eb8-32cd-bd9a-b0f85649fa3c | -8.05418 | -45.41452 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cab235db-1876-3e59-b01d-16f6413b2641 | -11.83186 | -51.48837 | 2025-08-30 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f26701f-772b-3613-a15d-bbf0757f6304 | -10.02837 | -46.02931 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5b1dcd0-eb5d-3c11-bb55-4bde4b3c1d66 | -7.7165 | -50.27289 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4bf42d86-a1af-3601-af19-faf6a2ff7cdb | -10.36825 | -59.20859 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ff51b4b-51e0-343c-85dd-48dd223f38a5 | -7.11976 | -44.60313 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 30cceb15-469b-314a-886f-1b9839cc29de | -9.21999 | -46.76302 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 632089a3-78d5-32e3-b2c2-bb0f766ef672 | -11.88773 | -46.3921 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6c85a6bf-3e48-3e0e-b4f3-ddc700dc2696 | -8.49452 | -49.40279 | 2025-08-30 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c86fa95-0fab-3406-9d9a-1b16137881b6 | -7.61389 | -44.95682 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4025af99-109f-3953-9221-3b5c1e0c7541 | -9.44879 | -60.54097 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6ccf0866-09e6-33a5-96db-c74cdffca34d | -10.64969 | -48.66379 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a01c8742-651a-3d0a-b018-d439d3befcab | -7.40272 | -44.29072 | 2025-08-30 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c857a23-bd52-3c47-a776-4706b31d7566 | -9.45272 | -60.54853 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e1ec82d8-aed5-3193-a258-bd1d3a2c746d | -10.02564 | -48.05006 | 2025-08-30 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 578ab53c-c26b-3d56-92d6-0fc6b8e90a16 | -9.44593 | -60.55689 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b070000a-cf47-33eb-9ab2-9cf4467d7ac3 | -9.7744 | -64.26031 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66a7d60d-82fc-378b-b87f-20cbd1a75a50 | -9.44451 | -60.56351 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa7c37d4-36b5-3d23-adb4-8cb784eb14bc | -9.44406 | -60.53706 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 61d21a96-573c-357f-884e-71eabb32ec1e | -11.06774 | -52.04648 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79dd1b76-6c90-3222-8c65-f25f9594770f | -6.9454 | -44.06332 | 2025-08-30 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e50fd0f-0ea3-3fc8-b1e7-27b8b0169f35 | -7.15544 | -44.91022 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cc11fdfd-a9d8-3ede-ac78-532942642745 | -7.17124 | -44.14835 | 2025-08-30 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c784159-f07b-3921-a3f5-20219fce1aff | -11.84132 | -46.38356 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3626119-ac97-31f5-8092-8f55118fa818 | -7.71985 | -50.2734 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28c12f92-9460-324a-8453-f9aad15c9dab | -9.7766 | -64.24906 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fed0c6b-eaaa-3e39-98d1-6888788355b8 | -11.87018 | -46.42581 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4c15b46-342f-30b8-af9f-e14591fc91dc | -7.09583 | -44.31787 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README51.md)
