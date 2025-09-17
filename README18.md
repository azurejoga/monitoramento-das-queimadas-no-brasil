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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc6d7ca5-0af1-3930-9d3e-d42820f274d7 | -5.59849 | -45.3607 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 563e5b27-d85c-3e62-a8c0-19e3748d36b5 | -7.58349 | -44.56265 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe49eddf-55b5-3594-8811-ae394bdc959f | -7.67917 | -46.63655 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b36b4809-bd33-3f06-af55-52c9abfbfa46 | -5.61458 | -42.90818 | 2025-09-17 04:10:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 190191ea-5e05-3965-aead-bb1aa333043a | -6.41439 | -44.3615 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87e29eed-a801-34db-877f-af3f94adb698 | -2.95949 | -48.59275 | 2025-09-17 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28194cd8-3a68-30c6-ad37-dad5d6ef0447 | -6.87218 | -43.97067 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d21c409b-8bad-3454-b8d8-2ba904f178d1 | -6.92826 | -44.91212 | 2025-09-17 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8062fc39-9446-3b4f-af11-0a8a19699dd1 | -8.13394 | -43.63847 | 2025-09-17 04:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6557958f-592d-39bc-9541-fc49ffeea00a | -8.65668 | -46.40398 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f23dde1b-64ce-3b22-befc-612dc0b539db | -7.53136 | -44.73478 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b0b7363-5312-348c-9e6a-6b6e596d4fd2 | -6.96169 | -44.5497 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8df47c2e-3ce8-340d-89db-60d41889ec0d | -5.18854 | -35.86609 | 2025-09-17 04:10:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6b168575-5b6d-3f9d-a416-7ac50b81e57a | -5.52944 | -42.17219 | 2025-09-17 04:10:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9991e54b-fd10-3ddb-9860-5e3ebf458a0b | -7.52993 | -44.72973 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b55c41f3-88b2-3cd2-8831-f5be89788dc6 | -8.96492 | -46.33203 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b283b08a-2e01-364a-b972-4c2dfdbed182 | -7.57457 | -44.59436 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d95b28e8-cabd-3ac9-a4c4-6e17090a98e3 | -6.77418 | -44.71237 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6192cab7-e8ca-391a-a0b6-f057c11480e9 | -8.15697 | -46.75791 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08c2276d-3698-3fe3-9dd4-f3dfe8d2a080 | -8.15386 | -46.7519 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 48d039bb-e66d-309d-be9d-f0805b69d205 | -6.48917 | -45.72907 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d214e397-2a96-3a3e-95d3-e68ffcda98dc | -7.17153 | -44.34679 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f518ec40-83c8-3995-aa42-1ae789881d80 | -6.39308 | -42.65097 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 707c985e-58f8-3790-b72e-2923dfd9b167 | -7.33873 | -44.58788 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c80895cf-9c6e-3383-b5f1-3411c56191ca | -9.12781 | -48.10947 | 2025-09-17 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7ce39e2-89e6-3236-ae72-1e4ca4f0cd48 | -6.40876 | -42.66082 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 23f9cd89-d29c-35a4-9464-1ec16aad0dba | -6.38914 | -42.65398 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0d7923a4-3876-35d7-957b-03451a0814a7 | -6.8719 | -44.17029 | 2025-09-17 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a036117-cdef-3077-91e1-c0456b0cbeb5 | -8.15298 | -46.75721 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef851f4e-ffdc-352a-b46b-a5e1bc6476f9 | -9.05417 | -44.83757 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f12d6d0c-2488-328e-bbe9-04766c58c361 | -7.09022 | -44.5367 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7af0566c-543c-3b07-bfe9-d59361f12782 | -6.21545 | -43.90426 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd576b47-7a38-32ad-b8ee-43ed6eaca90c | -6.51291 | -42.51322 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2d06a125-57a1-39aa-ab73-ef6b8abbccfd | -6.96546 | -44.77563 | 2025-09-17 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac67c42e-4d4d-315a-8e6b-0a4a426a1ad8 | -6.8652 | -43.96949 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c2e6e40-0259-34ff-b2e9-cb2e3f50b27a | -6.25609 | -43.45607 | 2025-09-17 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeb8e1f3-f2d1-3dd8-9982-ef60bc93be8f | -8.68196 | -46.37293 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 67e0fb3f-23c3-33b5-8179-c5121683e749 | -4.05308 | -47.50206 | 2025-09-17 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4f166227-4fe6-354b-93c4-7a4d71994e28 | -7.50102 | -44.7173 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8663f47b-bf46-35cd-9aca-7a5bf54c400d | -8.90619 | -46.2824 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48112e35-22b6-390f-9659-0b77629f0406 | -7.34165 | -44.59249 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5813930c-dd7f-3da1-a396-e70725e9a69f | -6.92639 | -44.76429 | 2025-09-17 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50b0fa0d-61d3-3576-a2f3-22675089fa41 | -5.62414 | -44.83232 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2caa2d1f-f5aa-34e3-9998-29cd72f688e2 | -8.01155 | -45.65378 | 2025-09-17 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cdb66c27-23a4-3148-8334-d4a851d8e631 | -7.88839 | -48.16549 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b31c0f7e-e4a8-3c36-8ce0-d777751bbc5f | -7.83639 | -43.85593 | 2025-09-17 04:10:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb0986ba-d7d9-321b-9269-5c8ab81b6826 | -5.80398 | -45.71002 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb719b2d-eb65-30f5-a966-c8349e7e391d | -8.57046 | -46.34666 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 385985bd-32c0-3abb-b8f2-57866eb2847d | -9.11921 | -48.10809 | 2025-09-17 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dfefd22-770f-32bc-9e56-1b21670d1cd4 | -5.76766 | -45.9052 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9bc0bffb-62b1-3f18-963c-f62f62eb1827 | -3.42343 | -46.96882 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d961220-d459-3ee4-8f20-53f7216f197a | -6.39746 | -41.79421 | 2025-09-17 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 749ce037-a47e-3560-9117-6f2fab6db811 | -6.35372 | -43.15613 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d69231f6-5497-3bef-a1db-ec9a8c460022 | -5.7316 | -44.51662 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 159d2413-800c-360b-a742-68f5c88d91f6 | -6.15768 | -45.10857 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c6cb245-4072-3a6d-9b2a-8971e8e9ce0c | -7.68492 | -44.47102 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 071cfa90-2225-31bb-a117-23ca3a965835 | -6.48177 | -44.54276 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b45f5ca-468d-3218-a311-c1497a1009d2 | -8.95802 | -46.32605 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| feba3847-e8b2-3d62-a592-b6bb14493682 | -9.54599 | -46.29519 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35c03a1b-3532-3a7c-bb98-c7c7d451d267 | -8.63091 | -46.43717 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c20b78d3-2495-32de-b464-02603874a8bc | -6.87123 | -45.19049 | 2025-09-17 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a401b19-df85-395d-aad4-b5786b7cfe3d | -5.59575 | -45.36299 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3e6495f-aeb0-3348-8132-a9c790d9882f | -7.34229 | -44.58853 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77ec8741-ed7a-3032-9513-130da45d569c | -9.7559 | -47.33648 | 2025-09-17 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 38332dad-1a3d-32fb-9394-0b728b169cdb | -7.88473 | -48.16043 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 008ac308-9dbb-31ee-8039-92ca52b0fc49 | -7.82868 | -46.15907 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5ea18e6-d5af-3ed2-aa17-d341557164a9 | -8.91849 | -46.27971 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9698be5c-9156-3754-84e6-88b3476d777f | -8.79184 | -47.81035 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43335f3d-387f-301b-86d2-d435820b15c1 | -5.49041 | -43.98987 | 2025-09-17 04:10:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea61db1c-d204-37c7-a168-9893eaee3da1 | -8.62026 | -45.71262 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87b221d1-c975-3b5e-807e-85307fd49523 | -6.10148 | -45.94633 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d45c9c0c-592d-3d9a-9d0b-1c6071b9f90e | -9.59175 | -45.66283 | 2025-09-17 04:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 430d65d4-98ea-3721-823c-3fc964753894 | -8.24724 | -44.83333 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19682f50-6e5e-36e4-925f-ffc8aa44f9ce | -7.82754 | -46.16177 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ddf67875-3921-30de-adf0-8832e0d5029e | -6.5914 | -44.32315 | 2025-09-17 04:10:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69412da6-f580-3fce-b26c-1c08597eaf01 | -4.40541 | -42.15065 | 2025-09-17 04:10:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4a571914-f567-3297-9d4d-c0abf73f7f30 | -5.64121 | -37.4886 | 2025-09-17 04:10:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0767ced-4a02-36f2-a1f1-8322f7040838 | -9.75934 | -47.34069 | 2025-09-17 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 80de8d8c-7990-36f6-83be-ab69f05c8726 | -8.92391 | -46.27113 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0185aad4-c726-3f1b-aa05-415d3745e29e | -5.56791 | -43.44156 | 2025-09-17 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4b47d123-b51b-3cd4-b907-4e4eb0397ede | -5.06952 | -41.16853 | 2025-09-17 04:10:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ed3979d8-991f-37df-a2c7-f8d5998d1f7a | -6.16597 | -45.98967 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63c726a3-bdaa-3f39-ad80-3e0474796255 | -8.16097 | -46.75857 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93835b3d-8db2-388e-9f47-a3f32a6ca123 | -6.73996 | -46.99681 | 2025-09-17 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42174f95-35a6-3b25-b491-d2402f015864 | -6.98591 | -44.60431 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ef0e752-1b2f-3a96-b0b4-791814ffab56 | -3.03166 | -43.24524 | 2025-09-17 04:10:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb8deaea-4494-3189-8a79-140fa70541f1 | -9.1153 | -44.86496 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3edd9017-4b46-3308-9a65-1d384d39ff6a | -6.29432 | -35.20613 | 2025-09-17 04:10:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 705c95a8-1d21-3a78-9830-986427ee003c | -7.67223 | -45.13021 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0eb827c0-4c80-3cc6-a6e4-16914cfb9782 | -2.37848 | -47.63249 | 2025-09-17 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9bb486be-c1f6-3a44-b0a8-da464ecbb134 | -9.59615 | -45.65911 | 2025-09-17 04:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1154ee1d-577a-368b-ac74-31facdcef976 | -8.67651 | -46.35474 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43216bc1-c900-3fa0-a493-ba446e020d27 | -3.78222 | -43.35493 | 2025-09-17 04:10:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24e109eb-6e73-3a4b-b363-922ddd1d291d | -8.97953 | -45.03152 | 2025-09-17 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3535db48-6951-3ef0-9e1b-dc17f25c3a1d | -6.73932 | -47.00054 | 2025-09-17 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29eaf245-e9f0-37a1-b680-9c881e7f3d33 | -6.18026 | -41.22321 | 2025-09-17 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3fc67b3-2bc1-3557-8949-b2dc32937af0 | -9.11752 | -44.8737 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e56a49d6-2485-3f6e-b3ba-3d53005c421c | -5.80056 | -45.92576 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eaad59f-9a74-3a9d-bb7d-d552636017f3 | -6.40482 | -42.66387 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1dd426c7-05d4-3394-80fe-07b09c0102b9 | -9.95567 | -45.9156 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
