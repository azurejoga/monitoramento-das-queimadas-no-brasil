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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2eaaa03-9122-31ba-bce6-6168e0fbc2ef | -4.148 | -45.7672 | 2024-10-13 00:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b572b87d-e029-3dfb-8f05-2617e15afa63 | -4.1665 | -45.7886 | 2024-10-13 00:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 05a6c867-ea7f-3fa7-bdef-ef997a7c9cb0 | -4.1666 | -45.7662 | 2024-10-13 00:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 37d14ea7-8352-3ec6-8b02-7a777eed5110 | -4.4026 | -49.7563 | 2024-10-13 00:35:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| de35f0ee-9425-394e-a085-a52606b74d69 | -4.898 | -47.6707 | 2024-10-13 00:35:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 1cd1b6a3-bc54-346e-a9f8-df381704410a | -4.8982 | -47.6488 | 2024-10-13 00:35:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 03279582-6aec-3783-a554-e3bb82ad4605 | -5.0713 | -46.8499 | 2024-10-13 00:35:35 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4ada4ff9-2cd7-32d5-8506-57e42523d299 | -5.1381 | -45.3969 | 2024-10-13 00:35:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 62f51bc6-0e51-3c4e-b838-093e9172a9cf | -6.1299 | -47.2884 | 2024-10-13 00:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 313ce7f0-dbda-3d2b-ac8c-38beef0219c7 | -6.1301 | -47.2664 | 2024-10-13 00:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9e80a4f3-b9e9-30a7-9dcb-432549614917 | -6.1485 | -47.2871 | 2024-10-13 00:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| ca56c65f-b95f-331c-900e-79cd5a5732ba | -6.1487 | -47.2651 | 2024-10-13 00:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 9e57ab1b-0484-30f2-8b08-35c745479d43 | -6.6925 | -62.8493 | 2024-10-13 00:35:45 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 778437db-44e7-3786-bc60-8d09aacbe6ba | -7.3823 | -47.2586 | 2024-10-13 00:35:48 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 54874ede-df23-3f1c-9946-05131cd5a5a6 | -7.3657 | -64.6656 | 2024-10-13 00:35:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| c9f93e95-1d83-364c-900a-be35f58c544d | -7.3841 | -64.665 | 2024-10-13 00:35:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 1199813f-76a2-3b96-a091-98f93f07dcd8 | -7.3842 | -64.6464 | 2024-10-13 00:35:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 6f325e9e-263e-339c-86c9-9273b335b042 | -7.6627 | -47.3229 | 2024-10-13 00:35:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 476d1c36-e285-30a0-90c2-fa53838702c2 | -7.6629 | -47.3009 | 2024-10-13 00:35:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 61c18578-bd04-38ea-b20f-3237ba91c9ce | -7.6815 | -47.3213 | 2024-10-13 00:35:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 26af5499-bf5b-3100-b37e-7edf0dc99242 | -7.6817 | -47.2992 | 2024-10-13 00:35:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 942c09b1-63a6-3f3e-86bf-17f1b3ece063 | -7.8713 | -54.7217 | 2024-10-13 00:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 47b5cb73-49d7-3193-b136-3fc4c84ea519 | -7.8715 | -54.7016 | 2024-10-13 00:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 0b151917-164a-3123-b20a-e8e68e1803d1 | -8.0675 | -44.8158 | 2024-10-13 00:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| eefde2a5-9cb4-36e0-b49f-d2afc794f2da | -8.2352 | -64.0961 | 2024-10-13 00:35:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 2825827b-7936-3d9f-abee-51027a39d26a | -8.2352 | -64.0773 | 2024-10-13 00:35:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| ff924887-c4a8-3500-9505-280332d0699a | -8.6856 | -46.6061 | 2024-10-13 00:35:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 66e9e057-afad-38db-8085-4fce3bd74b06 | -8.7042 | -46.6266 | 2024-10-13 00:35:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 941f2296-c30c-347f-9da4-b293460e9835 | -8.7045 | -46.6042 | 2024-10-13 00:35:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 294.3 |
| b7f2825a-83c3-321e-b60f-a6c5a037e71c | -8.7048 | -46.5819 | 2024-10-13 00:35:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 037f7bab-1070-3ddc-9447-91c3be68a654 | -9.7359 | -64.2295 | 2024-10-13 00:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3d884a6d-6f3f-35cc-b737-a183c3474120 | -10.9311 | -44.6789 | 2024-10-13 00:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 693e87e9-b399-3d8f-bd15-4897537a057e | -10.9315 | -44.6557 | 2024-10-13 00:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| aef80999-2e7e-377d-9472-84575635df1b | -10.9502 | -44.6762 | 2024-10-13 00:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c9078773-ab4b-34a4-ac27-d02c9c0f0b18 | -10.9506 | -44.653 | 2024-10-13 00:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2249f121-4c4b-3963-bffe-82baf9f8cf9d | -11.2722 | -50.9228 | 2024-10-13 00:36:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 9ee66b6f-75d2-3210-ba8e-7e7d88a473fb | -11.2725 | -50.9016 | 2024-10-13 00:36:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e2f57e4c-266d-33c4-bf74-f57474000f4d | -11.6334 | -48.3736 | 2024-10-13 00:36:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| bfbe3425-5d44-3543-b5b4-fdfd78c4d432 | -11.7479 | -48.3591 | 2024-10-13 00:36:13 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e0ee067b-cb18-3626-b850-b2165814d082 | -11.7308 | -64.9769 | 2024-10-13 00:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 33037deb-b100-3a55-a42f-5301446670de | -12.2751 | -47.6696 | 2024-10-13 00:36:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 297844be-a51e-3ef6-bc12-911d52e1b2fa | -12.2754 | -47.6473 | 2024-10-13 00:36:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 66955695-3ff6-31dc-a99d-cceb15fae035 | -12.3793 | -63.7294 | 2024-10-13 00:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 067aeaa7-600c-3431-889e-a2bc5a5c885c | -12.398 | -63.7475 | 2024-10-13 00:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 7e1bab1f-e49f-30b3-a905-89e7865bfea5 | -12.3982 | -63.7284 | 2024-10-13 00:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 171.2 |
| 23204c4a-0a04-3cb6-a4b8-998d3924c9c0 | -12.9182 | -62.5287 | 2024-10-13 00:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 5eac180a-a425-33ff-8921-952eb99b2847 | -12.9372 | -62.5275 | 2024-10-13 00:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 146.0 |
| 8ae603c2-3a10-3f7b-939f-fcdaf5c90fb0 | -13.1475 | -62.3215 | 2024-10-13 00:36:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 259fdb34-c2fb-3667-a692-3363ef38995d | -13.7155 | -60.6093 | 2024-10-13 00:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 0dec1ef1-b82f-3c11-b675-6db4a04c169b | -13.7346 | -60.6079 | 2024-10-13 00:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 3d6936f7-a189-3c5b-a249-fab2d24da491 | -13.7348 | -60.5883 | 2024-10-13 00:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 7eb66956-51f6-36f9-913d-b7b5b45ed521 | -14.7638 | -57.799 | 2024-10-13 00:36:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 2c2681ca-ef47-35a5-bfd2-c36e9dc9679f | -14.7641 | -57.7789 | 2024-10-13 00:36:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 032e60bb-6f5d-39e7-9b90-34225337757a | -14.7831 | -57.7971 | 2024-10-13 00:36:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a849b678-7c8a-3179-b921-9f325c9195c0 | -15.6419 | -59.9767 | 2024-10-13 00:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| a5f9e95f-1dbd-316e-9e24-60e65a750695 | -15.6421 | -59.9568 | 2024-10-13 00:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| e33ad6f6-d813-37db-84a6-627531d311a8 | -15.6612 | -59.975 | 2024-10-13 00:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 102bc399-f349-34e8-9db6-65c20b60605d | -16.9998 | -57.4586 | 2024-10-13 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 24ba85ef-9f5d-34b0-ab5d-33eeb4e47144 | -17.0001 | -57.4381 | 2024-10-13 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 9a862419-0125-3332-b8fd-d95b2a191a95 | -17.1758 | -57.479 | 2024-10-13 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.6 |
| 7755d579-bbe7-3f43-a62e-639a6813ddd2 | -17.1761 | -57.4585 | 2024-10-13 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 180.7 |
| 5027999c-6d25-3c74-af7d-77093fbfa1e5 | -17.1764 | -57.438 | 2024-10-13 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| c81e54ca-cc0d-34ae-956b-e15b9e0d3613 | -17.1954 | -57.4767 | 2024-10-13 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.5 |
| fb184a6d-6269-3130-a2c9-6661c414f2ab | -17.1957 | -57.4562 | 2024-10-13 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 152.1 |
| cf215ca0-6f9c-3f19-b962-62c740dcaa6b | -17.196 | -57.4357 | 2024-10-13 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| ae2c4bae-351f-3d58-96e8-8d38fea23366 | -17.964 | -57.3843 | 2024-10-13 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.6 |
| 1b4e86ad-0177-35f3-b4cf-b8c6ccc0fd7b | -17.9643 | -57.3637 | 2024-10-13 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.0 |
| 87608746-19d3-380d-a2d3-a51ddbbf0066 | -17.9837 | -57.3819 | 2024-10-13 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.6 |
| 5ebea422-f734-3207-8b7c-1105f1069985 | -17.9841 | -57.3612 | 2024-10-13 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 153.9 |
| 8e161ad0-cc4b-335a-b5cc-4e64fffa2c3c | -18.1953 | -56.5691 | 2024-10-13 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.4 |
| 42e99780-38a3-3f9c-9b7c-2fbde230f913 | -18.2147 | -56.5873 | 2024-10-13 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 171.3 |
| d5a41eba-f0f0-3900-a473-3bc10d698507 | -18.2151 | -56.5665 | 2024-10-13 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 323.0 |
| 16858f1c-511e-305b-bc8a-e362c137d63d | -18.2155 | -56.5457 | 2024-10-13 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| da19ca9a-c940-37c2-af5e-69ddffb67de7 | -18.2166 | -56.4832 | 2024-10-13 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.2 |
| b707bba2-8434-338b-bac1-1fe2c01f8a48 | -18.2364 | -56.4806 | 2024-10-13 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 44b25afa-9428-3ab8-8164-3199ca2b9b7d | -11.20622 | -47.8449 | 2024-10-13 00:37:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 805a8af0-f9c2-3394-b12a-ac6c05212d94 | -12.84038 | -48.57798 | 2024-10-13 00:37:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8ffdf760-be19-3695-886b-9c8ca324fcdd | -12.83817 | -48.55967 | 2024-10-13 00:37:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 85bcaefb-c498-3703-995f-0c70f7f37325 | -12.60004 | -48.62051 | 2024-10-13 00:37:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 441895be-b6cc-32ab-9f32-87ec2312a635 | -12.59784 | -48.60161 | 2024-10-13 00:37:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c107d6f8-7ec1-3002-b5ea-9bb110829f35 | -12.59509 | -48.60758 | 2024-10-13 00:37:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| abbce606-9cc0-3c4c-890b-afbb45b46936 | -12.55913 | -48.72653 | 2024-10-13 00:37:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4815f5f2-9351-31a1-ba19-0ca75bfe7b27 | -12.53041 | -46.81673 | 2024-10-13 00:37:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0f5b6454-f93b-3cb0-81ff-5a785a009cc5 | -12.52142 | -46.83175 | 2024-10-13 00:37:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e03b0860-72b0-3dfa-9b26-f8c72f6b3632 | -12.51971 | -46.81818 | 2024-10-13 00:37:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e7ac3aa8-3e5e-32c0-85cb-89896a2fd680 | -12.28247 | -47.66554 | 2024-10-13 00:37:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 830ec64e-53f7-36a4-b22d-156fc559f3cb | -12.28069 | -47.65987 | 2024-10-13 00:37:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 8143d9ae-4019-370e-97f5-387438b503d5 | -12.28051 | -47.65001 | 2024-10-13 00:37:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 136cf3d6-c957-3873-81fc-7f2b948669ac | -12.27886 | -47.64437 | 2024-10-13 00:37:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 9c50a3f7-80bd-3d10-bebd-9dd78b4e4ae9 | -12.27108 | -47.66703 | 2024-10-13 00:37:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ee9ae478-688d-3f88-a0c8-a934630e9ac4 | -12.26912 | -47.65137 | 2024-10-13 00:37:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 43db975d-6ae4-37a4-b740-2b623288b8ce | -12.26441 | -47.15113 | 2024-10-13 00:37:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9b3720d2-924e-3d71-8469-00c588904ace | -12.18146 | -46.74485 | 2024-10-13 00:37:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 94d91750-0785-3fd0-980c-06cfded084ba | -12.17984 | -46.73163 | 2024-10-13 00:37:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 42120397-a917-3e3f-991d-ab5f011bc0e9 | -12.17506 | -46.73792 | 2024-10-13 00:37:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 33920464-8abc-35bc-b8bb-cccd780c7c85 | -12.17335 | -46.72473 | 2024-10-13 00:37:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 53911985-e9f9-3d91-b2b5-f50c74fc33c5 | -12.17086 | -46.74623 | 2024-10-13 00:37:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f9baac24-e421-308e-be95-a9286801cf3a | -12.16924 | -46.73296 | 2024-10-13 00:37:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f5f72485-aada-3b1e-94cb-1474b1f514d4 | -12.16257 | -47.53193 | 2024-10-13 00:37:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e3b58516-6f1a-3217-92fe-6e2f69301e47 | -11.9929 | -46.53092 | 2024-10-13 00:37:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README6.md)
