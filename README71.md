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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75aa2107-5435-3ea8-bb6c-919a8ccbf72a | -12.2938 | -50.0121 | 2025-08-22 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 9d5c2fe6-81b6-3d61-990d-673090326aa5 | -12.9921 | -45.2252 | 2025-08-22 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 3a121c7a-12c9-3876-a4fb-3770c03738bb | -12.3133 | -49.9881 | 2025-08-22 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| cb66c339-435e-368a-9d9b-0e16f2088396 | -7.6296 | -45.2464 | 2025-08-22 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 276dd286-547f-3947-bca0-2a5afdfbcd44 | -8.4776 | -48.2578 | 2025-08-22 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 230.2 |
| 478c458a-bd1d-3c41-852d-e0dec70a70b8 | -11.3275 | -44.9468 | 2025-08-22 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b29788c2-496b-3f6d-a33e-167545347478 | -7.2989 | -59.6307 | 2025-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| d77d9341-147c-34f1-a667-d6f8383267f0 | -14.7694 | -56.0335 | 2025-08-22 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 240.0 |
| 250cbbc2-a768-3b8e-ac6c-c198316df18f | -12.9925 | -45.202 | 2025-08-22 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 53b56b65-d2fb-3ae0-81fa-1fe2c27c1af5 | -10.8754 | -50.8589 | 2025-08-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 204.9 |
| da54e2f8-141a-3f7e-94af-57115e03bc81 | -13.3971 | -46.2177 | 2025-08-22 14:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 57ce9207-98f4-329c-972e-89fa61c56c3a | -8.6129 | -62.6308 | 2025-08-22 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| f8abb009-92da-3b1c-b696-e30b70596078 | -10.8568 | -50.8396 | 2025-08-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 215.4 |
| 362e1223-8f51-3db0-9f13-0f397ed9fefe | -7.6484 | -45.2446 | 2025-08-22 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 28011e87-672d-3a2f-be21-1920cd5786a3 | -14.596 | -54.7575 | 2025-08-22 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 5f618a8d-1dfd-396c-b8a0-9d8fdb5f9c9e | -7.6298 | -45.2236 | 2025-08-22 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 554e7dbd-738e-3fb2-8a15-605b8d3869af | -14.7717 | -45.4055 | 2025-08-22 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 402.9 |
| 3054e962-1ad7-3d81-8b44-4681eed2a04d | -14.6713 | -54.8728 | 2025-08-22 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 23aa7610-6bbc-3d55-9e80-eea4798267eb | -12.9963 | -56.9 | 2025-08-22 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| ea3ff44f-17af-3465-a1b3-eb208242d90a | -14.6523 | -54.8543 | 2025-08-22 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1dcf6dfc-fee4-35e2-8272-7c210510ae54 | -8.4588 | -48.2595 | 2025-08-22 14:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| ec166ec9-ab9e-3ad1-84b4-7d5142fded1c | -8.7785 | -46.7082 | 2025-08-22 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 160c53f7-9bf5-3349-b1a0-dcd15f7addcf | -6.5199 | -45.5238 | 2025-08-22 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e598eacf-1f66-30c6-b060-165b6c280e22 | -14.6519 | -54.875 | 2025-08-22 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 7ac5aa97-6ee4-35d3-8356-5e740a9a01f6 | -14.5956 | -54.7782 | 2025-08-22 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 12be3d02-2338-34fe-af95-9d50e22d7692 | -14.8348 | -47.9311 | 2025-08-22 14:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 72ed7f73-3ff0-3271-9132-7ef26a0ddad3 | -14.4478 | -53.1702 | 2025-08-22 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 6cdcb95c-69c3-3b74-8441-85b36444410c | -12.9773 | -56.9017 | 2025-08-22 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| c2b08e57-9523-33a4-a252-f86b4a42394f | -14.7501 | -56.0356 | 2025-08-22 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 5330f25b-5379-3de1-a23d-64cec26e4d73 | -14.3523 | -53.1191 | 2025-08-22 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 131.9 |
| f7a65ba3-81ef-318b-acf6-0667ec2cce8a | -10.456 | -48.3607 | 2025-08-22 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 78393454-8db3-37f7-888f-58c142fa6dd8 | -20.2492 | -46.7017 | 2025-08-22 14:40:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 279.6 |
| 4bdeb2d2-a922-38ec-aaed-d334a81585cb | -14.6716 | -54.8521 | 2025-08-22 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 38236d1b-43c4-3cb0-92b3-cd07645ea202 | -9.6865 | -47.9409 | 2025-08-22 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 33a520bc-c653-342a-bf12-759a93687be6 | -9.1526 | -59.5997 | 2025-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8a6d6d92-47d1-3e87-b6ae-6ea84d2f87f8 | -7.6366 | -46.2823 | 2025-08-22 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| aa6309ee-e40b-39f7-b6ac-10425469f977 | -8.8735 | -62.4305 | 2025-08-22 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a022d550-3ba3-37bd-a1b1-5e7fb7ac4a08 | -12.9921 | -45.2252 | 2025-08-22 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 43dbbf55-23d4-3447-812d-8d1a0aa5d2dd | -8.8736 | -62.4115 | 2025-08-22 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 61b026cb-85ca-3f40-8736-d031be40fb47 | -8.8921 | -62.4297 | 2025-08-22 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.9 |
| c9624e3f-021e-313c-903f-8c9ffa7ab171 | -12.3133 | -49.9881 | 2025-08-22 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 0fb7dca0-7dc9-36de-9997-a071919290f0 | -10.876 | -50.8163 | 2025-08-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 45d8bb52-5f0e-3a09-ac5f-318f7f4d895a | -14.7712 | -45.4289 | 2025-08-22 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 408.9 |
| 3eafdf61-5d17-3262-b85d-01db7ad6528c | -6.2716 | -52.8255 | 2025-08-22 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 83bfadbc-fe00-399c-bab5-dba170727290 | -9.6 | -55.3498 | 2025-08-22 14:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 114.4 |
| c72a0438-3372-3497-bacb-d7cee89cdbfb | -14.7562 | -45.2219 | 2025-08-22 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ce3e425b-8844-3639-a82e-e44887e6fa40 | -12.5042 | -53.8091 | 2025-08-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d96b3744-c077-3aef-9731-2d7cde40b206 | -12.3129 | -50.0097 | 2025-08-22 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 058fee8a-3468-35da-9a3d-a8626ae04bd1 | -7.6181 | -46.2616 | 2025-08-22 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 0375424e-357e-3600-bad6-86c6bec75c26 | -6.0252 | -44.3798 | 2025-08-22 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 2d36ac91-bfa9-3993-8c3a-bf2c7d3762d0 | -20.2287 | -46.7066 | 2025-08-22 14:40:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 02f39d3e-6e45-366c-bc4d-ea8a174f625d | -14.7308 | -56.0377 | 2025-08-22 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| ac8408c6-65af-32f7-afcd-e0a83d296fc9 | -14.7722 | -45.3822 | 2025-08-22 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 451368a6-298d-32ba-92b7-8a6370fa124e | -7.0354 | -44.6167 | 2025-08-22 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 4c1e7781-3095-3013-8e1c-d33a16c6e583 | -5.7782 | -44.787 | 2025-08-22 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 40d8210b-2dc3-325e-b7ad-dbb71c50a419 | -6.5781 | -59.871 | 2025-08-22 14:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| bb15e0bf-fbc6-3f17-840d-c0dffd8773c1 | -10.8757 | -50.8376 | 2025-08-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 383.5 |
| 1c106014-a61a-3a62-8fd5-5fce117fbf5e | -14.7694 | -56.0335 | 2025-08-22 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 3366ad70-7ef8-3f60-8759-311b0965cf39 | -7.6296 | -45.2464 | 2025-08-22 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 4e1f4127-3ae1-32e9-b068-1057804a502f | -6.4266 | -45.4861 | 2025-08-22 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| ebb2e644-b5b2-3cae-95df-bf01763816a4 | -9.2095 | -59.4609 | 2025-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 6b620d28-042c-303e-816f-8e0a0e428d7e | -14.7504 | -56.0151 | 2025-08-22 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 84dcb15b-3d32-3673-b047-8d999e54266a | -7.2989 | -59.6307 | 2025-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 711152a3-a09e-3517-bb5f-4880c2e08708 | -5.7784 | -44.7642 | 2025-08-22 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 2866a348-7566-36b4-8ce3-111df4c989ab | -8.613 | -62.6118 | 2025-08-22 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |


