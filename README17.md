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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6aeae0df-cdae-3645-a15c-135bc24237f9 | -20.59562 | -57.26932 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1f3de1a-bc61-3cb0-a44f-b40241e7b3ba | -20.59231 | -57.27333 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7229d119-156c-34a4-8b2f-bd6caf752daa | -20.59099 | -57.27409 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f1522d5-2297-3021-a921-b45f08474e9c | -20.52052 | -57.16874 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af31fa4c-62de-3229-9a27-1110dc63dad1 | -24.49101 | -50.11836 | 2026-07-29 05:23:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e082b00-b18e-3166-8a42-93da842e9fcc | -20.82627 | -57.83941 | 2026-07-29 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 045ee9cf-473f-3fed-abb6-720cb907bdbf | -23.09777 | -52.6801 | 2026-07-29 05:23:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 6a662af6-5136-3d0f-bcd9-4174da709c0a | -22.3777 | -55.7392 | 2026-07-29 05:23:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2550995-4546-3443-805b-5f6c96433499 | -23.83969 | -52.86716 | 2026-07-29 05:23:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| a92ceff9-182c-35aa-bc4e-aa591ef3939b | -23.83453 | -52.8628 | 2026-07-29 05:23:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| fc936bcf-09f7-3d8e-948f-dafa1d8c2b8c | -20.91018 | -57.49944 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6b21ce8f-d0c8-3a40-b7de-b4ec494f501e | -23.02706 | -52.65753 | 2026-07-29 05:23:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| b6fbb7de-d709-3032-8ba5-1a19cc12282d | -10.3612 | -49.7378 | 2026-07-29 05:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ea3cf1a8-06b4-3759-be8a-d6f0d8e7d0c8 | -10.3609 | -49.7593 | 2026-07-29 05:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 3c97805a-f053-396f-9061-91c7fb8c0e47 | -7.3413 | -45.8377 | 2026-07-29 05:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| aeedc363-8383-385d-abe0-3046a001174f | -10.9397 | -43.0593 | 2026-07-29 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 014548b9-23be-303c-830b-278866f18889 | -10.3612 | -49.7378 | 2026-07-29 05:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 456781e3-1c5f-3380-b5bc-593f04d4ee2a | -10.9397 | -43.0593 | 2026-07-29 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 6991d938-d67f-3986-ae59-414bd9c56ec3 | -7.3413 | -45.8377 | 2026-07-29 05:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 4ddd200e-955e-31a6-9532-81359517bd1f | -10.9397 | -43.0593 | 2026-07-29 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 25262c4d-1a53-39e5-821d-2d5b3c9948e8 | 2.9487 | -60.18163 | 2026-07-29 05:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d14cec82-8d91-333a-925f-f647eeea0e7c | 2.94937 | -60.18577 | 2026-07-29 05:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d44f84cc-8d2b-3c91-a8fb-983173105f47 | 1.68028 | -60.13823 | 2026-07-29 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6990612-f6f2-3cba-ac07-2e591128e74f | -11.64045 | -60.4496 | 2026-07-29 05:53:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98912078-b89b-3daf-8924-7c1fb5ee06dc | -9.97203 | -64.94511 | 2026-07-29 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 048d408b-ac62-3f47-bb21-a85613524507 | -8.82415 | -66.75885 | 2026-07-29 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62d277b7-00a7-37be-b7b6-7c01997b6c87 | 0.92318 | -60.53801 | 2026-07-29 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e8e9a38-233f-3e29-a6fb-5b1dd832c1ba | -8.83943 | -65.04202 | 2026-07-29 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b42820f5-f9ee-3788-93fa-6ae83dc61ca7 | -11.42662 | -61.43055 | 2026-07-29 05:53:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b915debf-89c0-36b8-9ad2-38787051214b | -9.07048 | -68.69101 | 2026-07-29 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4fb91d3-c3aa-3dd3-ab03-ed3d23ce50ee | -8.82081 | -66.75831 | 2026-07-29 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17db16c1-72f7-3c23-a1a2-c13931332ad2 | -8.82471 | -66.75533 | 2026-07-29 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5eca3cfa-5c8e-316a-9a9b-c1c29736e769 | 1.67659 | -60.13881 | 2026-07-29 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d180e0ca-dceb-3042-9f63-2d12b79c1f17 | -9.91975 | -67.04567 | 2026-07-29 05:53:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e96002e-bc90-3fba-8b4a-3a87119a9d81 | -9.50144 | -66.7174 | 2026-07-29 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c13c280-3722-38cf-8a92-6e5535745197 | -9.47873 | -57.31977 | 2026-07-29 05:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5a30e3e-8714-3d52-a69f-c84fc33951d5 | -9.49532 | -63.30418 | 2026-07-29 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0aa7515-15e7-3d8c-ae48-71ac847e0509 | -9.47332 | -63.28003 | 2026-07-29 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f04424b3-cd64-3277-ba88-960d6e38f020 | -10.12716 | -68.05284 | 2026-07-29 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc64cbf4-5c9f-3cfc-9d4c-01211eea05dd | -5.23178 | -56.00915 | 2026-07-29 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 613a6a24-38cb-373d-94e1-006060fbddce | -9.47831 | -57.32297 | 2026-07-29 05:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bb36f04-55ca-30da-a6fa-73afe28c59ea | 0.92716 | -60.53888 | 2026-07-29 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4468e9c5-8227-38f9-93ec-22aadd75286a | -9.96921 | -64.94095 | 2026-07-29 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f1141b9-e086-3cba-935f-da79c807b3e5 | -5.23717 | -56.00994 | 2026-07-29 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e64f4f20-851d-3b48-b841-9a5a5aea440f | -9.48355 | -57.32374 | 2026-07-29 05:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7bcae125-01d2-3719-84c3-f396ecdc1c56 | -11.4307 | -61.43115 | 2026-07-29 05:53:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2eb039fa-e48d-3ba2-9aa0-2e4dc3379d04 | -9.074 | -68.6916 | 2026-07-29 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4e17f20-a89b-3a3f-825f-5704d445c36c | -9.19144 | -58.06696 | 2026-07-29 05:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 523619b5-ae4c-35d3-8cb3-3baa489abd80 | -9.49811 | -66.71687 | 2026-07-29 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f11186b6-211c-3b9b-acb6-69ff10ac7870 | 0.92351 | -60.53939 | 2026-07-29 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3986b7af-a7e1-331b-be6a-e06eb0a2221c | -9.73173 | -62.37785 | 2026-07-29 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dc4e346-0f93-3121-bdf2-9aae98d97ff8 | -8.82138 | -66.75479 | 2026-07-29 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8561e0ca-9ffc-3c4e-8966-2a820b7d344d | -14.34741 | -58.94659 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5484ac1-dc55-383c-98eb-08f0f491fa67 | -12.36409 | -63.44791 | 2026-07-29 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 906d4a75-db89-3ae6-8f68-ffd23eed1fe0 | -12.36043 | -63.44736 | 2026-07-29 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c7655bbc-d09c-3980-b07e-78aa60562c1b | -14.02395 | -53.97015 | 2026-07-29 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33d7ab02-84ef-3686-9825-37aa10bf1697 | -14.33734 | -58.94538 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a7b624a-b4ef-312b-b5b5-5cd1e42c9e98 | -14.21409 | -59.00469 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 246c483c-af33-3eca-9c2b-17d694239d55 | -14.32078 | -58.95984 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b657c06e-0eb3-396a-81f0-1553233d1ccc | -14.33236 | -58.94892 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a147825-d0fc-3f8a-926c-e389b6a903da | -14.03699 | -53.97829 | 2026-07-29 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5785f89b-1ca4-3718-8c02-c2e344aade85 | -14.35325 | -58.94546 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e1484d9-7d8d-3cdd-800c-450014e751d1 | -14.06034 | -53.96065 | 2026-07-29 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2030c331-4cd3-3e36-93de-967ba21d6377 | -15.40806 | -55.93878 | 2026-07-29 05:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0423e1c7-efc1-364d-97d9-432701a7f407 | -14.34317 | -58.94429 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2b268fa-b045-34c0-88e1-c0bd6af361ae | -14.30067 | -58.99862 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e47515f-6afb-3852-9da9-7a8283892d70 | -14.35245 | -58.9472 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14359d3e-e2a6-3413-9e30-19f98cf345b2 | -14.32658 | -58.95432 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16f01389-0868-3062-876a-225cddfc55df | -14.32731 | -58.94847 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 617ecb7d-3dce-3bf1-b518-96bdec5d4d06 | -14.34237 | -58.94599 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d37c4d9-df61-3912-a68e-e9c52b2a44d8 | -15.40189 | -55.93779 | 2026-07-29 05:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7090875-e7af-3a2e-9886-cae475956d1c | -12.36838 | -63.44412 | 2026-07-29 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 442c67b7-520e-38be-b1a6-96e164c1344e | -12.37205 | -63.44467 | 2026-07-29 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55d5039b-2a8b-3ca3-b710-b96615845eee | -14.05966 | -53.96128 | 2026-07-29 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d493f815-10b1-307d-b9e9-7c2f32a4249f | -12.36472 | -63.44357 | 2026-07-29 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b06fff01-e01b-3ea0-9e8f-8146e5ec060d | -14.05276 | -53.96077 | 2026-07-29 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7353ade5-ae74-330e-9f46-e1e680016ba2 | -14.21907 | -59.00553 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db54cbe1-7506-3ae3-9319-316e77ce16f1 | -14.33665 | -58.95116 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 612eb0d8-2c1a-336c-ab78-b112452e7f9a | -14.33741 | -58.94945 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9bace0fc-7dbd-3d44-aca6-cf7cd2cb9076 | -14.05344 | -53.96013 | 2026-07-29 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dd91aba-5083-325b-9b32-22e598b7ec45 | -14.34748 | -58.95067 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d606f88-9414-36e9-8050-ace997296462 | -14.03015 | -53.97731 | 2026-07-29 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bc875a0-71ef-3bac-a5c8-d6bf6a24051d | -14.0171 | -53.96921 | 2026-07-29 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaea7b00-c00a-3d18-9808-73ee5db72c67 | -14.34821 | -58.94487 | 2026-07-29 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1392172-3420-3c6d-91b2-dba767c74272 | -20.60488 | -57.25303 | 2026-07-29 05:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4e0e5de-6344-3d61-857a-922d23dc4b77 | -20.90548 | -57.48145 | 2026-07-29 05:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| cb65a31f-ee08-30cb-952d-61aa4df44abf | -20.59967 | -57.24288 | 2026-07-29 05:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bc33eb1-b58d-35b6-a708-443bba05de09 | -20.89948 | -57.48076 | 2026-07-29 05:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4fd49634-280b-3500-bdc4-684b6a682b2d | -20.60443 | -57.25797 | 2026-07-29 05:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5de00fb4-ea58-3a00-ac94-43a9e62cb828 | -20.90591 | -57.47675 | 2026-07-29 05:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8e603ad0-c909-3a40-b5f6-98739b9ba1f8 | -20.60532 | -57.24816 | 2026-07-29 05:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a85db6a8-951c-3573-a284-ec7e4ad53c9a | -10.9397 | -43.0593 | 2026-07-29 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 5e544dcc-939e-3179-b1d2-7b4265c2e9af | -10.9397 | -43.0593 | 2026-07-29 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 6a76d89e-9930-3bca-a296-1c0ab904c531 | 2.94783 | -60.18151 | 2026-07-29 06:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56c61d77-2714-3d4e-89a6-6a1f5259a47f | 2.94842 | -60.18499 | 2026-07-29 06:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86bb1c6f-d503-3ea9-8676-ff51ca16a174 | 2.949 | -60.18845 | 2026-07-29 06:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 574c70cc-9d09-36a9-9465-6aaf050ad767 | -8.82054 | -66.75461 | 2026-07-29 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f7e4295-c530-3eb8-b812-06abcce654bb | -12.35935 | -63.44902 | 2026-07-29 06:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 355712fd-62c8-3642-8300-46ff7fa6bb9e | -12.35949 | -63.44783 | 2026-07-29 06:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13bd2f77-8564-3e47-b30e-f2b08aade8a3 | -8.41962 | -72.78752 | 2026-07-29 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README18.md)
