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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0bb1f7d-35f1-3911-8aa5-c5a34c58f6c2 | -4.0153 | -46.1752 | 2024-11-09 01:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 6afed539-76ed-3e12-b32d-593733d92085 | -1.5078 | -47.1813 | 2024-11-09 01:50:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| e54f9868-a924-353f-8af1-0c63e6e11896 | -3.9668 | -48.1932 | 2024-11-09 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 6e382b9c-d7cc-3112-8da8-51040f82b2a9 | -4.2033 | -45.8538 | 2024-11-09 01:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 123.9 |
| b75ccb57-24d6-303c-9529-b29cedd58673 | -4.0152 | -46.1974 | 2024-11-09 01:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6f5bd28c-de0d-365e-ace3-71f9db0385ca | -2.2479 | -53.7627 | 2024-11-09 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7107d26b-bbfa-3724-9169-0b15c006dfc8 | -4.2484 | -47.5947 | 2024-11-09 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 2d1bea7e-4c13-3ad8-bd8b-6d5bbcd6504e | -2.2295 | -53.7832 | 2024-11-09 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 30e6c13b-277b-3024-9ec4-13f2de8d9687 | -3.5462 | -43.5663 | 2024-11-09 01:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 14ea0aa9-143a-3749-9b59-6d49cfd53873 | -3.9483 | -48.1724 | 2024-11-09 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 684f1176-6175-35e3-8277-c9ef6a84c7c3 | -4.2671 | -47.572 | 2024-11-09 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 03aeaa6a-fe73-3f54-8707-f9d0cea0191d | -3.0865 | -50.5625 | 2024-11-09 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| cffc4b6a-49bf-321c-994d-6f24c26d65ca | -4.2032 | -45.8762 | 2024-11-09 01:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e6b95898-a318-3429-958e-624a3ee3b443 | -3.1512 | -52.9527 | 2024-11-09 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 390d92f0-6e7d-35e8-b0da-10f672a0bb06 | -2.2295 | -53.7631 | 2024-11-09 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 7ccc1a36-a498-3b4e-a1df-13b00ecdd938 | -5.4701 | -43.6371 | 2024-11-09 01:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0ab01560-c46a-36ce-89ce-91f16320ffb9 | -4.2058 | -48.5491 | 2024-11-09 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| c926ebd0-0105-39aa-842f-84cd72760fe9 | -3.967 | -48.15 | 2024-11-09 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c25306b8-0a09-3d3e-b899-0ad8dacac734 | -1.5163 | -52.1901 | 2024-11-09 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3f9ae31c-114e-3ad7-b712-181657c94637 | -2.6764 | -51.8189 | 2024-11-09 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| e0cadd20-50f0-353d-9d39-3f23dd85ab06 | -3.5649 | -43.5654 | 2024-11-09 01:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 7c8836f4-3bff-315f-a14a-410492360ed1 | -3.9669 | -48.1716 | 2024-11-09 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 230.3 |
| d8132932-c57b-3f98-80b7-b094511c1b93 | -2.379 | -46.8552 | 2024-11-09 01:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 1199bbcc-abef-37ad-9242-5726f3ad432c | -4.0339 | -46.1743 | 2024-11-09 01:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| cb0fb123-1313-3988-a2dd-7481cc1b15de | -3.1511 | -52.9731 | 2024-11-09 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 414.9 |
| fbf7971b-3810-3878-9850-b552faf382d9 | -2.2295 | -53.7631 | 2024-11-09 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 98d49f72-5d27-32a0-aba5-ada01749aab6 | -3.5819 | -47.3403 | 2024-11-09 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 296.3 |
| b0f29ac8-c458-315c-b0b5-f3a8091b4530 | -4.2671 | -47.572 | 2024-11-09 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 17221c2c-f619-3a61-943f-b461fd2405c6 | -3.735 | -54.2292 | 2024-11-09 02:00:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 34cb7ac8-8782-370d-b204-858fe1566cb3 | -3.619 | -47.3388 | 2024-11-09 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6ef13172-23f2-3b75-a7d8-6324be419560 | -3.6004 | -47.3395 | 2024-11-09 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 730.3 |
| 84efd038-b8a2-3ba4-8d85-d0cf48642cde | -2.3605 | -46.8557 | 2024-11-09 02:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e56355d0-a824-3e1d-b07c-a826904a6ffa | -2.5747 | -49.1421 | 2024-11-09 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| fad79c3d-532c-3667-bb17-287a96544aae | -3.2353 | -50.2645 | 2024-11-09 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| fd3593bf-5302-3e89-9da9-1e4697c3de41 | -2.2479 | -53.7829 | 2024-11-09 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8f1e4bdd-f720-3deb-aae6-068c8b49088d | -3.967 | -48.15 | 2024-11-09 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 08277247-ee8a-3f3d-b980-855277a79224 | -3.0865 | -50.5625 | 2024-11-09 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c737cfb9-3dff-398d-8bf5-6f950c362231 | -4.2487 | -47.5511 | 2024-11-09 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d254f715-b29c-3beb-93ed-3f77cf080933 | -3.9483 | -48.1724 | 2024-11-09 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f03fb47c-5200-3d74-b551-aad76074936b | -3.5462 | -43.5663 | 2024-11-09 02:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c524669b-8052-3f1b-8c2c-715e9b3eee2a | -3.1511 | -52.9731 | 2024-11-09 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 286.3 |
| a8d69b75-5969-3c96-b5d3-2b8b2fad11f0 | -4.2033 | -45.8538 | 2024-11-09 02:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1626c42c-00d9-378a-ba6e-0fe750826449 | -3.9669 | -48.1716 | 2024-11-09 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 212.2 |
| 334dd59a-44ab-3989-89d4-23ec130e8007 | -4.2032 | -45.8762 | 2024-11-09 02:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| a0d2b6ec-d759-37ad-8ff1-bcbb04609851 | -3.1512 | -52.9527 | 2024-11-09 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 5afeefd3-742c-3bdc-85ba-32bbe9996608 | -3.151 | -52.9934 | 2024-11-09 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| b65c753e-91f6-386f-beea-bb167b24d1e1 | -4.2058 | -48.5491 | 2024-11-09 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 63639cd3-806c-3bb8-9b19-a5ea4bb8bffc | -3.5818 | -47.3621 | 2024-11-09 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 216.5 |
| c84fa778-a3c8-3d08-b02b-6114409c81fb | -3.9853 | -48.1924 | 2024-11-09 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c2df0f0c-1f43-358d-aa3b-b4801ef04f54 | -5.4701 | -43.6371 | 2024-11-09 02:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7c2b6d40-8a60-3744-923b-1de6226e23df | -3.9668 | -48.1932 | 2024-11-09 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 1c2e11ee-3ff4-376f-b485-02ada694a4b8 | -2.2479 | -53.7627 | 2024-11-09 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| bcb2253d-159f-32f7-bc7f-34a4a0b415b1 | -5.4699 | -43.6603 | 2024-11-09 02:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 9620a256-5e70-3f56-929f-70f28d0d8eae | -2.6764 | -51.8189 | 2024-11-09 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 625f513d-ecff-3ac3-9984-3bcf94423d43 | -2.2382 | -50.5217 | 2024-11-09 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 71fbeb5d-9945-30fc-957e-1dc0a5fd579d | -3.1327 | -52.9736 | 2024-11-09 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 58733011-1b4f-3874-aeda-82c3bd7f62b3 | -3.6003 | -47.3614 | 2024-11-09 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 433.8 |
| 057c4784-8bb3-3c52-9b0a-188c935bd702 | -4.2484 | -47.5947 | 2024-11-09 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| dced4152-8f03-38d6-b9de-78bedcb0f312 | -3.5649 | -43.5654 | 2024-11-09 02:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 35a3684d-2eec-339e-91db-13f343ab7718 | -4.2486 | -47.5729 | 2024-11-09 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 211.6 |
| 330609a6-b528-31f9-b78f-c2ef42be0cf6 | -2.2295 | -53.7832 | 2024-11-09 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 688b03f4-38d7-3656-a59b-13496094edda | -3.9854 | -48.1708 | 2024-11-09 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| bbb42956-33d4-30b7-9849-d3ceacd9e5eb | -1.5164 | -52.1696 | 2024-11-09 02:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 79132900-d92a-3837-a0e0-92e4089026ac | -3.61 | -47.3 | 2024-11-09 02:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6b987d1-99c4-3e9f-a396-a8ad8813d3ed | -3.61 | -47.35 | 2024-11-09 02:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab2d435d-5c7d-3f03-83b5-857e887021fe | -3.58 | -47.35 | 2024-11-09 02:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 282b5627-5e3c-3734-b258-08b5d07ad165 | -3.58 | -47.3 | 2024-11-09 02:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73b51a4b-2c5b-37db-a746-a9d86563c260 | -3.13 | -52.97 | 2024-11-09 02:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e046e2-9fee-3f7f-a601-e16753cc6c8b | -4.2486 | -47.5729 | 2024-11-09 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 252.5 |
| f406733c-a0f6-34bd-8f25-f7e5b3b1408e | -3.619 | -47.3388 | 2024-11-09 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 78618c51-ff65-3863-ac1f-cb20f3c24de2 | -2.2295 | -53.7631 | 2024-11-09 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d47c42f0-2f29-32ad-a3a9-15ccc76b0dde | -4.2058 | -48.5491 | 2024-11-09 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 2583206a-6d02-3a1f-8f69-0aee778861cd | -1.5164 | -52.1696 | 2024-11-09 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b935fde5-d324-3895-a6d8-a093b225f4ec | -2.2382 | -50.5217 | 2024-11-09 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 022ec39e-6886-3f36-abcd-79ded7665d74 | -1.1467 | -53.6573 | 2024-11-09 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 2e26dbc1-a927-3975-b39c-858d2989a8ef | -2.2295 | -53.7832 | 2024-11-09 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 6ea06ce6-dab0-31fc-8b38-15975ee8c8c9 | -3.5462 | -43.5663 | 2024-11-09 02:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 9539a78e-5576-31ac-a321-eb45c85b07fc | -3.9668 | -48.1932 | 2024-11-09 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| b03119ec-d8f0-34cf-90db-9b59cc3c10b3 | -3.1511 | -52.9731 | 2024-11-09 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 249.0 |
| 54c089c3-9a98-3178-a767-641245c5d165 | -3.6004 | -47.3395 | 2024-11-09 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 556.9 |
| d2bb588b-e648-3c3e-9d10-ad77aa3d08ec | -3.6003 | -47.3614 | 2024-11-09 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 375.8 |
| 6b64dc7c-55bd-3bca-896b-7171a5a8802a | -4.2484 | -47.5947 | 2024-11-09 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 3b0af264-7e71-3697-acd5-32febd0c54a0 | -4.2671 | -47.572 | 2024-11-09 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 96eadf2b-1a85-3f39-a4d1-1ec3ace71b75 | -2.2479 | -53.7829 | 2024-11-09 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 207aba40-e0c2-31d1-9c1a-a8460e68da28 | -3.9483 | -48.1724 | 2024-11-09 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b0301f5a-2567-3836-a820-09a908c914ef | -3.9853 | -48.1924 | 2024-11-09 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| ae0da4c8-40c6-3340-a437-9f4fbaeffc3a | -2.3605 | -46.8557 | 2024-11-09 02:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| efaaf8c0-8bde-305f-9367-811b87bb2f07 | -3.068 | -50.5631 | 2024-11-09 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6ecad74d-e1db-3a0f-b0b5-36aa51e6c82c | -3.5818 | -47.3621 | 2024-11-09 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 186.2 |
| d662cd77-e122-370e-9124-545bd8ccc487 | -3.151 | -52.9934 | 2024-11-09 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 95f47b23-7b82-362d-9e38-a27f743f8274 | -3.1512 | -52.9527 | 2024-11-09 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 44f7d102-6cae-38c4-9427-29fb938091e8 | -3.1327 | -52.9736 | 2024-11-09 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 5636fc08-f138-301c-8bfe-22566aa27523 | -3.9669 | -48.1716 | 2024-11-09 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 212.5 |
| 8875f006-8d0f-3d50-84d5-eeb740df3f1c | -3.5649 | -43.5654 | 2024-11-09 02:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 05706142-be67-3181-b9fb-181ea868b467 | -2.2479 | -53.7627 | 2024-11-09 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8696837c-9815-3c06-951d-a5d1394f1547 | -1.5163 | -52.1901 | 2024-11-09 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| e1284ece-7d82-35f6-aa78-f2440ed893af | -12.0122 | -44.1466 | 2024-11-09 02:10:00 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 73c309ba-feee-3074-b935-6c1bfe0197b0 | -3.0947 | -53.3196 | 2024-11-09 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 9663cf69-94e8-36c1-a664-eac342180b0f | -4.2033 | -45.8538 | 2024-11-09 02:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 94e1a518-5fd7-3dc9-a99d-49e439f2394c | -4.2032 | -45.8762 | 2024-11-09 02:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |


[Clique aqui para ver as próximas entradas](README15.md)
