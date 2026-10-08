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

## Dados Diários - Página 385

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8db0b972-a2a6-3e24-8859-4fa19b0e407f | -15.3419 | -42.7704 | 2026-10-08 17:50:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 236.9 |
| 07993b4d-520c-354d-946e-dbc23acd8f3a | -11.8503 | -43.5598 | 2026-10-08 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 407.4 |
| 10ae0f2e-5981-33da-98d4-0b21631f02d2 | -3.7239 | -57.1384 | 2026-10-08 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3549d21b-f529-3149-9ecc-be71dedfa4bd | -5.9586 | -55.3648 | 2026-10-08 17:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 5dbddd7f-b380-33fb-b591-54de51f63a4c | 1.6937 | -55.6263 | 2026-10-08 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 65cf7815-ce52-3580-88e6-ef01e626a9c7 | -11.47 | -43.3824 | 2026-10-08 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 430f18c2-9d92-3a68-8b42-42e3d70f11fc | -9.8253 | -47.4629 | 2026-10-08 17:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7e149e1a-53ba-3c54-b2e3-d8ecf710595d | -9.1253 | -67.9432 | 2026-10-08 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| ee51390e-01f3-3a8e-867f-f49d2abfe4ab | -5.7509 | -41.6333 | 2026-10-08 17:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 7918f694-025d-3299-8b32-929cc79e266b | -11.7742 | -43.5245 | 2026-10-08 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 269.9 |
| c2925bd3-f9f2-3eac-8853-00e4429c540b | -11.7935 | -43.5215 | 2026-10-08 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 61c1815f-d86f-3737-afa5-955e6b9adde3 | -2.9271 | -53.9295 | 2026-10-08 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 01773752-3d14-3488-94df-8a4cf4db1979 | -2.8897 | -54.1514 | 2026-10-08 17:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| dfd44ccc-aad1-37f1-b8d6-3263545faa31 | 1.6938 | -55.6066 | 2026-10-08 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| fd1ede0a-acc1-3abc-a5e5-8a77216c26a3 | -12.2123 | -44.7457 | 2026-10-08 17:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a8e8e0d8-2729-36a8-88c8-2ed41aaee6fe | -3.4095 | -58.0013 | 2026-10-08 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 519b7817-95a1-3f14-854d-0f0ad426c111 | -1.1991 | -55.7106 | 2026-10-08 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 04cd4c6b-7b86-3fba-8749-cb9cc393b8e9 | -9.1486 | -45.8158 | 2026-10-08 17:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 807afaa2-fc6e-35bb-ab6b-18db12205058 | -14.3608 | -55.032 | 2026-10-08 17:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2afc7206-c6dd-3eb0-9c89-27a51d055af0 | -11.2482 | -46.2604 | 2026-10-08 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 7c59ebbc-8d0a-3743-bd6b-0c36dec5501b | -11.7335 | -43.649 | 2026-10-08 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 0c02a2cb-9b30-31ca-b279-e7864d43b323 | -6.4568 | -55.4609 | 2026-10-08 17:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 0edfcbc9-59f8-3f14-be4e-2eb4d0fa2ad4 | -12.2316 | -44.7427 | 2026-10-08 17:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 7ec75ddf-842d-3045-b2fe-984162a5b58e | -9.9398 | -43.5542 | 2026-10-08 17:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| c770d81e-53ae-3274-bab7-01b76362c782 | 2.0047 | -55.8786 | 2026-10-08 17:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| aa07ebf3-5ce2-39d5-8282-d29c0ff1dff5 | -12.8303 | -44.6239 | 2026-10-08 17:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 0b460db8-7577-3071-b56f-ed3b4981976c | -12.0444 | -43.4578 | 2026-10-08 17:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 250.0 |
| a1200764-e542-37ab-9f27-ca512a4dd937 | -5.7489 | -53.4641 | 2026-10-08 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4e15fb18-a1e2-3ec5-a6af-a0c4e3fd8399 | -6.1974 | -52.8295 | 2026-10-08 17:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 93b296ae-65d4-3a45-ba41-7b265b1a5988 | -7.4694 | -42.8551 | 2026-10-08 17:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 171.8 |
| d002c01a-89cd-3c83-9552-a3e199fe5b10 | -10.7936 | -47.328 | 2026-10-08 18:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| cc7ea7a0-e49d-3cb9-8eef-669ecf04ecd7 | -9.4819 | -66.7836 | 2026-10-08 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 958683c0-2ddf-368d-a5ed-b39c82184733 | -11.6562 | -43.6846 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 5d5b6b7e-b2e7-37e6-b64a-0fcdffd8742e | -4.1025 | -44.1149 | 2026-10-08 18:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| df3d135f-cdd1-3c8d-9f26-994debcb3bd0 | -3.7809 | -41.7913 | 2026-10-08 18:00:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 8e1cf86a-5f4f-3ac9-bb4b-fef24ff685e3 | -11.0953 | -44.0037 | 2026-10-08 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 94b3458c-e889-33f2-b340-94ea674e4baf | -6.1977 | -52.7886 | 2026-10-08 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 9bbbeaa0-95a6-320a-8a6c-5ae96e2f1ada | -2.7152 | -57.472 | 2026-10-08 18:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 02421dfa-17ef-310c-b343-cb4210f6d5d9 | -11.2816 | -41.1194 | 2026-10-08 18:00:00 | GOES-19 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 161.4 |
| 48be7d48-1339-3022-9a6e-6ae119f18d61 | -5.5146 | -42.8399 | 2026-10-08 18:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 152.1 |
| b2131f39-4381-3bfd-b59e-4c563e026c35 | -3.6105 | -58.171 | 2026-10-08 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a794f872-c43a-3e5f-96ac-4d1484e0e399 | -12.0448 | -43.434 | 2026-10-08 18:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 96c9f23b-6409-3b1c-a827-4effe23b4fb9 | -5.3718 | -44.1981 | 2026-10-08 18:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 214.8 |
| 75957251-1754-389d-9516-2151d32b6032 | -13.3671 | -43.8742 | 2026-10-08 18:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 1ef4e199-a011-36a9-806f-a45d2a9b434e | -12.1554 | -44.708 | 2026-10-08 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 327.6 |
| 91eaa4a8-0099-327e-93ad-999d03a5ce4b | -9.4506 | -45.8498 | 2026-10-08 18:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 264.0 |
| 2992b5f4-ba74-3334-b012-1d3a2918ca12 | -12.8303 | -44.6239 | 2026-10-08 18:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| e4784caf-1189-3b1c-b21c-d6d16bc65a9a | -5.3615 | -43.2027 | 2026-10-08 18:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5d670efe-fab7-3254-97de-50fd3017838f | 1.6938 | -55.6066 | 2026-10-08 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 3626bcb3-7810-3086-9d7a-22b27603577b | -11.1358 | -46.1396 | 2026-10-08 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| a6e52294-8ece-3336-b5eb-358da2d4d24c | -7.2 | -55.1026 | 2026-10-08 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 90ded3a6-ad48-3fe6-afc5-b1ad4aac3500 | -11.6186 | -43.6433 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| fcfc150f-3c18-3b7e-a308-f8f622875647 | -8.9308 | -45.1584 | 2026-10-08 18:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1047.4 |
| 90a0bf56-03de-3534-bbc5-9faf897e0074 | -3.7239 | -57.1384 | 2026-10-08 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6916f227-dcf2-3d8b-89de-9b1dbbe236ae | -11.7742 | -43.5245 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 384.9 |
| c1417be5-52e1-380b-8415-da192f5c0e09 | -6.7187 | -55.0483 | 2026-10-08 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 9a447528-92d4-3dac-9e2a-0a00346f1c93 | -11.1354 | -46.1623 | 2026-10-08 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 3f42eb39-75c3-3d44-9945-2e48a7c69c81 | -3.7817 | -41.6718 | 2026-10-08 18:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 84047a7c-998a-30df-927a-fb73b72cf245 | -13.395 | -43.4652 | 2026-10-08 18:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 79adfb74-9f8d-3500-b89b-bca49ba574c7 | -7.1813 | -55.1237 | 2026-10-08 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 2c42fb8e-48d2-3695-a07a-7256f69e155f | -6.1402 | -53.0574 | 2026-10-08 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| f908447a-3af7-368e-8c54-e20872a327ca | -2.8713 | -54.1518 | 2026-10-08 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 9cc98d38-524a-398d-9ab5-8838b7bdd6ee | 3.5448 | -51.2772 | 2026-10-08 18:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c4af487b-efc4-3e6f-9e7f-63b2738ce639 | -11.47 | -43.3824 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| a22b4d0b-374e-305d-a05b-5a0bb331a596 | -11.8696 | -43.5568 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 284.0 |
| acce14fe-0502-30b9-8fdc-77d0de951f4d | -3.7622 | -41.7924 | 2026-10-08 18:00:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 3e1cfb9d-33c2-3d6f-8a58-49078a81584e | -2.7153 | -57.4526 | 2026-10-08 18:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 0e4094e1-e81e-3171-8a2f-cd62f3f8cbef | -2.9082 | -54.1108 | 2026-10-08 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8c7525d4-3d1d-3e71-9643-a572f6772144 | -1.801 | -57.1161 | 2026-10-08 18:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c135fbc6-ab82-332f-978f-133403cb270b | -7.1627 | -55.1247 | 2026-10-08 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 55d73941-080d-3f45-aa2d-ee3f79afddf8 | -7.2185 | -55.1016 | 2026-10-08 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| a45de145-2d05-3b19-bc54-85c70aa47147 | -11.776 | -45.5495 | 2026-10-08 18:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| e6f09b39-a1db-3d2b-9033-5aad7608c289 | -12.1545 | -44.7547 | 2026-10-08 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 19e241ff-02f4-3078-919d-d33a17718f93 | -11.6369 | -43.6876 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 321.2 |
| bd7257db-9384-32f5-80e4-75330986412e | -2.0447 | -54.3085 | 2026-10-08 18:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 13cbfadd-e58f-3240-b577-bd0ae94d6948 | -3.188 | -58.6241 | 2026-10-08 18:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| f54d712e-1247-361e-b934-d17591d4f8c8 | -9.0065 | -45.15 | 2026-10-08 18:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 403.8 |
| cbf46898-5e0b-3ea4-8ce1-5713829da1a3 | -7.7025 | -45.4436 | 2026-10-08 18:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ae793d6f-33c2-3c85-bc40-a40a08a8e568 | -6.9331 | -43.6566 | 2026-10-08 18:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 7d7402f9-6aae-30db-81b9-104da4333843 | -6.1431 | -52.6481 | 2026-10-08 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 67d50ef8-0c88-32a3-bdc1-0cb7c882f647 | -9.4818 | -66.8022 | 2026-10-08 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| ae315b99-fd88-37e9-8183-e7dcece455de | -12.2508 | -44.7397 | 2026-10-08 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 04813e28-cd91-39a7-8c41-7c2db65d5ba2 | -2.572 | -56.1842 | 2026-10-08 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 548.3 |
| 61960b07-6a3e-35bb-9368-53064b8bf43b | -12.62 | -44.5414 | 2026-10-08 18:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| e1013c71-2d52-30f6-a59f-d62457b69f53 | -3.8004 | -41.6708 | 2026-10-08 18:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| e11b2683-a531-38e5-9549-2a7701b0a1fb | -6.0423 | -42.5859 | 2026-10-08 18:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 978c577b-d16d-3878-ba38-cb8e0ac1f3b6 | -6.8762 | -43.7083 | 2026-10-08 18:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 203.4 |
| af16c935-2e12-3766-80de-8957be7ab2cd | -5.9587 | -55.3448 | 2026-10-08 18:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 589392be-19b2-399f-a0e9-b908dbdb0cc0 | -2.4623 | -56.0682 | 2026-10-08 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 98bc2e24-43ea-3264-b00a-abd9c7ffbc50 | -6.6027 | -37.8944 | 2026-10-08 18:00:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 217.8 |
| a2a57d77-82ec-3a09-b007-dc1f9bba2b0f | -2.4942 | -58.0768 | 2026-10-08 18:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 7c9f635f-cf25-384d-b951-5a599f8d225d | -10.9766 | -45.3865 | 2026-10-08 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 872ab36e-68dd-3892-b104-7f0efc642c8a | -6.0075 | -53.5122 | 2026-10-08 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 4b8cd4a5-3368-34d8-a254-ef46912b471f | -9.8442 | -47.4608 | 2026-10-08 18:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| e683d138-881e-3420-9327-16bf3cfe6c93 | -3.1874 | -58.8358 | 2026-10-08 18:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| f51e6857-6d17-397d-9a6a-900aa871bb1d | -3.095 | -59.1832 | 2026-10-08 18:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 952dd626-8be6-3688-b712-ee4d9b2c2bc3 | -8.9311 | -45.1355 | 2026-10-08 18:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 283.4 |
| aba09533-7520-3b0a-8028-315f14808b2d | -6.1951 | -53.1566 | 2026-10-08 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f771d2f1-1141-39be-81e6-c87a4bfc849f | -5.7469 | -42.0643 | 2026-10-08 18:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 126.8 |
| fc4c3e71-84d9-3f41-bff1-d027a9a93e8c | -11.6382 | -43.6166 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.2 |


[Clique aqui para ver as próximas entradas](README386.md)
