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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d73ddd1-04b5-3012-b9f6-c2c59972bb74 | -9.44806 | -62.33541 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 00079e73-5c4c-389c-abed-b44f6ce7e2aa | -10.37464 | -57.83883 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fc4c4dd-9081-3ac0-9078-bdedc24d0b14 | -8.24586 | -61.4511 | 2025-08-30 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 979b95fd-ff3a-374d-a6f0-aeef1fa96460 | -8.34979 | -62.93012 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73323572-ebfe-3780-ae56-d826e53f39ff | -9.15076 | -59.60027 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e63858d5-a125-3da9-8055-537259836d5f | -9.41428 | -60.57045 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cfb8677-64d6-3da1-8d30-ffcd449aa150 | -9.27422 | -60.45651 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6d29dd1-d560-35a2-8b11-b794039a94e8 | -9.45374 | -60.55644 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d52648d7-e59a-337e-80e2-f17b63a4a5f6 | -11.84651 | -46.43462 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f0ff4408-a681-3807-b65e-ed8257044486 | -10.64554 | -48.65643 | 2025-08-30 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd8a2b4d-c784-31de-8f53-27e7a4f257dc | -11.86499 | -46.44519 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 34783f7d-f25c-3f84-88e8-1d2dd275d20b | -9.70567 | -49.46961 | 2025-08-30 05:10:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 24993274-0c92-3b94-a60b-4e37fcc33ad6 | -7.42739 | -44.81129 | 2025-08-30 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f32c2d32-a270-3cce-a86e-ca1b2e8b6034 | -9.23419 | -59.77955 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dbabea7-8381-3cce-8cd1-102e094da2ca | -8.85086 | -64.15152 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42e09d3c-579c-3f59-bd33-9650f7461190 | -8.56508 | -63.01438 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45b2d4a1-3302-3ee9-9f06-e895a41c895b | -8.18684 | -61.37972 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e74f9c3d-2173-3df6-96d3-9a891f63b33f | -5.82103 | -46.36819 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 988483b0-ae95-3db2-a551-339924887a80 | -7.74299 | -50.26758 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8a851a85-1018-3718-9cd1-fc006485536e | -10.47844 | -57.93442 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73b4c95d-ff73-3546-a327-62443908cb05 | -10.48619 | -57.95004 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3a0dc22f-ea95-3be9-8674-9be07b68453a | -9.64859 | -48.33947 | 2025-08-30 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ecbdd73-4547-3a2d-8401-5ddde16a9aad | -7.39592 | -45.93086 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b206bc1d-36ca-3b68-b72c-89ec20357245 | -8.25324 | -61.45237 | 2025-08-30 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75ccca6c-0de9-3d4e-b1db-4afab11e53e9 | -9.2777 | -60.45708 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bcc3ccf-4801-3656-9c7d-c6c05ea46993 | -10.45916 | -57.97084 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ee2910a-0d84-3fb1-a980-97deb5bb9b78 | -11.78109 | -47.55909 | 2025-08-30 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f99254ab-67cf-3d9b-9f19-f096ee320fae | -7.35004 | -70.12234 | 2025-08-30 05:10:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ca13b3f-3bfd-34b9-ac0c-523a7c77cb5b | -10.66997 | -48.73074 | 2025-08-30 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1a83bcc-7506-3980-ae94-c284fb90e570 | -9.45309 | -60.56037 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 640bbf0b-c31c-38eb-87a6-3691bcacc579 | -10.46409 | -57.93932 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e734fa66-0291-302d-9cae-c18758fe58a9 | -7.90294 | -63.00431 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba4fcc69-2641-34a8-aa58-2d1f33271306 | -7.34849 | -70.12467 | 2025-08-30 05:10:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 521b7b21-a1ac-3576-b34e-472524dadfe9 | -9.44023 | -62.35862 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3fdfe10a-924f-3d34-854a-0891012e74eb | -9.57348 | -55.38771 | 2025-08-30 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf561f31-d264-37d5-9adc-15650400fd4a | -6.07397 | -57.9308 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3495e880-bde2-3ed9-80e1-cfe72800b842 | -9.41777 | -60.57104 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 287176a0-967c-3093-91a0-f19ffe31cdc3 | -7.77869 | -45.47667 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fde8ae32-6de2-37dc-9c69-3eece20fc582 | -7.77406 | -45.46174 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 412641a9-a028-3c3a-a76e-b8d902b454ac | -8.66379 | -70.04444 | 2025-08-30 05:10:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 418ce9db-f0cb-36e4-b2b9-1b92848a42ca | -10.37406 | -57.82074 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acd1dded-4250-3981-a227-ee4778139479 | -5.61308 | -45.00429 | 2025-08-30 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a336da58-91a0-3e3f-80d1-fc1219f18d43 | -9.438 | -62.34848 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 89ad8ee7-7f1c-370e-8d87-968513bba543 | -11.06822 | -52.04606 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 638c3e2f-a942-3ce4-9e60-08bc03308dff | -7.57707 | -45.13507 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42534f13-e069-305d-a583-3d114867c0bd | -9.16839 | -59.57687 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d3c540a-ac30-3901-872e-f880629c500a | -9.43554 | -60.54993 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15917167-eb66-39af-bae6-198108050741 | -7.15279 | -44.90796 | 2025-08-30 05:10:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 47913c67-0099-3d04-960d-b7d8e277de24 | -9.45504 | -60.54868 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d9b61d7-a406-3795-b3d5-9bf4c80b9b2c | -11.83641 | -46.45862 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 2a36dc03-feba-350d-96d0-a63d939b30a0 | -9.45139 | -60.54056 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f8a65ebb-db82-3148-ad69-fb168e73e3b6 | -11.84699 | -46.43027 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1395e8a1-901d-3d2a-9ea1-02fc88497e1a | -7.95414 | -46.39448 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ab8e7d2-e228-3b21-bc81-069666c445f1 | -11.94216 | -46.69642 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8654c2b7-d334-36d6-b205-aaa011974157 | -9.4522 | -60.5442 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dc62fb0b-d163-3b67-9d5a-4602522c1576 | -8.55817 | -51.30633 | 2025-08-30 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd8531f0-cf3e-330f-bfe6-8124100ab7a2 | -9.24778 | -56.9014 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d683916a-37b0-3a3d-a68d-2cb0a68decea | -9.45805 | -62.32265 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ed44ec94-6325-36ad-852e-2434d55f6576 | -10.0208 | -48.0606 | 2025-08-30 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 678bed6e-a129-3c5e-a1ef-3191c471f50b | -11.94032 | -46.69501 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d98f08cc-13fe-3b45-aee7-561a161f9ff9 | -7.09068 | -44.31188 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 06e96121-ac0d-36e9-9321-52ca951139db | -8.59718 | -60.58234 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 448ce74d-d916-3a7e-85da-f38b89e5f623 | -9.58838 | -54.48652 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce212796-5994-3e8c-bcd9-70787d972fde | -7.73192 | -50.27718 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0c3ba148-ea9d-3c10-b3fe-842bbd93b1d0 | -5.81993 | -46.36137 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 13fc6d52-e0be-3d0e-a608-89ed6497d68e | -9.44283 | -60.57122 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3696b297-a3d9-328e-a9e2-d986c500eb4b | -9.43782 | -62.37295 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b78bf2fb-260c-39b2-9cbf-0de54b3fb808 | -8.65547 | -63.29601 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9975da84-5220-3c8a-ae73-1732b0639ea5 | -7.10286 | -44.59232 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1078517d-1a8f-3d8b-818b-73181eb23a3e | -9.46689 | -60.31327 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22fb3777-cf84-3296-9c38-62f63a1bb74b | -11.86479 | -46.38806 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01c3e8d4-f4e4-3079-831e-cf4bda80b5d3 | -7.77978 | -45.46688 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9c0b3d6-f2cb-3928-a84d-d995b99eeaba | -7.11041 | -44.58773 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70ee4c76-6f95-3a38-badf-e4933b2d334b | -9.45091 | -60.55196 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df83ea8c-d4d4-3abc-8308-442d5465cda5 | -11.8505 | -46.39842 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 896e7d21-8ff9-3bd3-96d4-5fdb059eef74 | -5.61874 | -45.00664 | 2025-08-30 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ff8f1ac-3d81-35d3-ba54-cab11d063711 | -10.02279 | -48.09057 | 2025-08-30 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31eceff1-8c71-3610-a73f-9f585b76f8f8 | -11.07881 | -52.03415 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e4e2fc7-78dd-3226-8244-81fa436d07c6 | -10.07148 | -58.36404 | 2025-08-30 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0288ebb-6f8c-3e6e-99c2-afd7ee0445aa | -11.85182 | -46.38294 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e6403a5-789e-37c3-a33c-a88449281ecb | -7.39655 | -45.92598 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91e8ec70-5356-378c-a5e7-e8a2dc513cf9 | -11.83819 | -46.44332 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| be737147-33bc-3ed5-9cf9-85b12e6ef495 | -9.50319 | -49.09953 | 2025-08-30 05:10:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dbc89e5-2203-3742-a15a-119f1b1b58a7 | -9.45002 | -60.53584 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 556cf814-5738-3657-876a-b0a3d05fa7b8 | -8.6212 | -63.95743 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 209c9122-9f43-3231-8e4a-d59a4bf4295c | -10.45199 | -57.97327 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81c21c93-2be0-3b8f-8fc1-e218453caabf | -7.71794 | -50.30738 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b85fdf08-02dd-3437-a3ad-fe20595f0827 | -7.76015 | -45.46475 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35671d53-662c-387c-aae2-1df75473c124 | -9.21662 | -60.8694 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7bc24f2-b497-3bde-bf8b-db9174ff7a5d | -8.17581 | -61.37786 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 865d116a-4bc4-3538-be09-ee990987b85c | -7.74353 | -50.26978 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fb5161fe-7e3e-317d-9d6c-45618c7df091 | -9.44121 | -62.32943 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 04d9487c-8e48-32b7-b07f-972d65447e7c | -10.38292 | -57.82934 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b114d8b7-45bb-3654-8c68-6aa620a58194 | -10.36523 | -59.20741 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd033f2c-f3a8-3db0-a145-fd4fe389b640 | -7.11641 | -44.59473 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1dea4ec-7cf4-3a06-b512-716f23161f50 | -9.43744 | -60.53825 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 473bb2e0-ac1c-3791-ac4a-f543c97c8079 | -8.05778 | -45.41526 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6389a876-59c0-3479-90cc-650b4e8a1335 | -6.69009 | -51.96415 | 2025-08-30 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b5e2b80-0785-37b1-b854-90ca25e411f6 | -8.53038 | -64.01035 | 2025-08-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 07ae8f01-4072-3c3e-9b6e-458ae4384611 | -9.69167 | -47.05537 | 2025-08-30 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README70.md)
