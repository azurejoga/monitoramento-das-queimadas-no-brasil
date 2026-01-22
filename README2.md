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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01148206-c2cf-3fde-8418-7e6879ccd96f | -20.35898 | -57.88239 | 2026-01-22 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e7abd98d-f2de-352b-b74e-3c1686a2fbbd | -19.21276 | -53.44278 | 2026-01-22 04:06:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6999d66-70d0-3376-95df-703dc6c21a4b | -19.21364 | -53.43874 | 2026-01-22 04:06:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 613d4210-1d14-3239-b40e-7d2aa5a7333c | -19.62333 | -56.98238 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dcc78e66-c830-3f2b-b52a-97698fd1dc6d | -19.66608 | -56.87965 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 042688e5-4fb6-3fad-89ee-17b0e36f9769 | -19.68225 | -56.88503 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2b872715-7b5b-33cd-a79b-921dc5f1b173 | -19.66461 | -56.88585 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7d29c66e-ffc4-3066-a6c5-5c87ac5dcead | -19.32275 | -54.02197 | 2026-01-22 04:06:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9152c3de-7c0e-3dd0-81da-7c1bcf295206 | -20.32337 | -55.92911 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e42da88a-e8dc-3fac-974b-4cd451fc868d | -19.62916 | -56.97606 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 486780b1-96c0-3819-9e66-adc9c692c531 | -19.64121 | -56.96701 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 1bf6f7a1-e96d-343e-b2e1-a13711a3392d | -20.61783 | -49.67304 | 2026-01-22 04:06:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5da873cc-d56e-36b0-81ff-9cd065073f86 | -19.63729 | -56.97153 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 6017f867-b6fc-3328-8b54-3d8f8e07d4af | -19.66985 | -56.99451 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6153f514-a544-3795-be85-07f5e3f8a233 | -19.13675 | -54.5415 | 2026-01-22 04:06:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f79c548c-1918-34cf-b109-bb696531a59b | -20.84326 | -51.73784 | 2026-01-22 04:06:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 01bbef08-424c-3003-b35a-10ee811aed30 | -19.67137 | -56.98824 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5ab79add-58f8-335a-8981-6759c190bfea | -21.94438 | -52.90866 | 2026-01-22 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 43a0f39a-b8b5-344a-8846-88af0d238f75 | -19.67564 | -56.8833 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2d8a80a2-6c19-3239-aa16-7ce2178a7e7c | -20.90624 | -56.38498 | 2026-01-22 04:06:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0842c19-7611-3bbd-94cf-7bfc7bf91ef6 | -25.5118 | -49.46545 | 2026-01-22 04:08:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 226f4976-ef63-3254-95da-b4e9c103ec36 | -27.03634 | -52.08596 | 2026-01-22 04:08:00 | NOAA-21 | LINDÓIA DO SUL | SANTA CATARINA | Brasil | 4209854 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8bde5447-c83b-3907-85f5-110a7cf77534 | -23.60572 | -48.26363 | 2026-01-22 04:08:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f1083ff-9d4c-3503-bed8-b15816aa479d | -22.73528 | -49.34743 | 2026-01-22 04:08:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 202cef8a-3b35-3783-9410-6fe263ab355a | -21.19661 | -56.93304 | 2026-01-22 04:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4ded838-0fb5-37a6-a016-b4e43dae2481 | -23.14266 | -49.06457 | 2026-01-22 04:08:00 | NOAA-21 | ARANDU | SÃO PAULO | Brasil | 3503109 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d8cacfd-42a9-367c-bf07-017737d56c71 | -22.65044 | -51.05504 | 2026-01-22 04:08:00 | NOAA-21 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9aa10fcb-3628-31b9-b7a4-0d33d555e68a | -23.29636 | -48.85265 | 2026-01-22 04:08:00 | NOAA-21 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db0db8f8-1aba-3d9a-8231-0d43312df52d | -23.05953 | -49.07612 | 2026-01-22 04:08:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fcd305a-7ef7-3120-85e8-b11e326a589e | -22.02266 | -56.33949 | 2026-01-22 04:08:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4947183-3dc5-3766-9176-259bd3bd44c2 | -27.44829 | -48.44438 | 2026-01-22 04:08:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b4149c45-90ee-32f8-b16a-e485fad9173e | -22.646 | -51.05405 | 2026-01-22 04:08:00 | NOAA-21 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8f8d7110-deaa-3773-ac18-92ed2df474b1 | -22.73131 | -49.34646 | 2026-01-22 04:08:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fc40162-6718-3fc9-b5bf-7084ac756ade | -24.0235 | -51.10767 | 2026-01-22 04:08:00 | NOAA-21 | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f0118376-2b80-35d8-89fe-f68f2b917ae5 | -26.97519 | -52.53053 | 2026-01-22 04:08:00 | NOAA-21 | XAXIM | SANTA CATARINA | Brasil | 4219705 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20ec8383-3728-35a7-9a9b-0bcadd190152 | -30.17222 | -55.29581 | 2026-01-22 04:10:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| dc990990-737f-33af-99c7-d7e7085195e2 | -30.90125 | -52.96236 | 2026-01-22 04:10:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 31f27b04-9ea7-354e-8616-d035b5be7c13 | -30.90547 | -52.96341 | 2026-01-22 04:10:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 6fe4036d-d771-319a-9013-6f0b034c8c87 | -2.14385 | -47.88029 | 2026-01-22 04:29:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 226c0b6c-dc74-33c7-a760-7a3a4d5970f9 | -2.14447 | -47.8764 | 2026-01-22 04:29:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 643f76a0-f3b0-3a70-ad02-a5e5141a1e54 | -1.67733 | -45.79794 | 2026-01-22 04:29:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f7fc489-825e-3181-8215-d906fc384746 | -1.67652 | -46.70515 | 2026-01-22 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 961df5b3-5eeb-3e80-a7db-d83cc8ad966b | -0.93364 | -46.76752 | 2026-01-22 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a4635fc4-dd92-3de7-ab4b-a196fa2cad2e | -1.67314 | -46.70462 | 2026-01-22 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4a5c995-d7f2-33b3-afd1-bf25644dd9a2 | -2.14736 | -47.88083 | 2026-01-22 04:31:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b9ef0cb-1cc5-345b-98d3-64a77b062438 | -4.86127 | -39.00531 | 2026-01-22 04:31:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a9046532-191d-3c27-a40f-b5e5d5bad880 | -9.76171 | -41.8821 | 2026-01-22 04:31:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 60888c29-4f30-3b8f-b2f4-b3aee61ac8f4 | -9.75759 | -41.88148 | 2026-01-22 04:31:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e1c8756-6dfa-3a21-9ccb-9f91c1ca3e31 | -15.85675 | -54.39975 | 2026-01-22 04:33:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0640272-036e-3778-9b1b-e90546b939af | -19.62771 | -56.97643 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f8e360b6-cf2c-334a-b29c-21be09d3b4c5 | -19.65062 | -56.93455 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 60893a6c-7689-3481-9b27-a27c6a985128 | -20.30764 | -57.8731 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 94cc7ac3-1506-3f2a-9a35-58c94e7ed640 | -20.35201 | -57.87772 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 40043faf-2789-39d9-a4a2-0d4ce70c63a1 | -19.32431 | -54.02285 | 2026-01-22 04:36:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0150abe8-59bd-3a09-b52e-1749105b5342 | -22.36757 | -48.3501 | 2026-01-22 04:36:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f9c0aee-6c7d-32ab-8297-b33a4180d705 | -20.91111 | -56.38687 | 2026-01-22 04:36:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af6057ef-b4a3-37e9-920d-df75ebf245ae | -21.94599 | -52.91061 | 2026-01-22 04:36:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6e2cdd5f-3238-32d3-9708-4f9dc2d54f24 | -19.62669 | -56.98145 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| c992c244-103a-3cda-8e65-d931474286a6 | -20.91166 | -49.13899 | 2026-01-22 04:36:00 | NPP-375D | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2fb40fb3-9302-360b-8cf9-21e9a50ed3b5 | -19.64144 | -56.93248 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9c91601d-a3f7-3a34-9ed0-20958974c1cb | -20.34721 | -57.87658 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1b1f8078-8ac4-310d-a7ab-0c24bd81d2dc | -22.73418 | -49.34386 | 2026-01-22 04:36:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4816904-dd8b-3e7f-abde-b5fd3a81a15f | -20.31244 | -57.87423 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 65c3c761-cfff-3a12-a9a8-67b621a6bd36 | -19.6662 | -56.88102 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| db2ddfc5-68b2-3dcb-8c3c-a18f014bc9b4 | -19.21355 | -53.445 | 2026-01-22 04:36:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee2db4a4-787c-3838-9441-80ac30670f7b | -20.90676 | -56.386 | 2026-01-22 04:36:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24c55d06-47b3-3a2c-9195-a76e0cf120e5 | -19.67077 | -56.88205 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 242f106f-0040-3a0a-ba15-e3516c0b3bcc | -22.65026 | -51.05162 | 2026-01-22 04:36:00 | NPP-375D | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a4cd51b9-aecb-3e5c-8599-f37c2236b0a4 | -19.2098 | -53.44422 | 2026-01-22 04:36:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee8c6040-cf5b-3862-a2ad-cd16bdd0ef28 | -21.94672 | -52.90642 | 2026-01-22 04:36:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d67d708f-f939-3440-93d8-98e7990e2730 | -22.64692 | -51.05099 | 2026-01-22 04:36:00 | NPP-375D | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f7f81c84-15ca-3a35-be32-de84f3c191b4 | -22.02017 | -56.33881 | 2026-01-22 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3477019a-6dd4-3516-a320-fd66c25a5ab1 | -19.63996 | -56.96349 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 14650a12-ae57-309b-981f-598dc43c130e | -20.32969 | -55.93 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 72feb10f-1cb3-32f5-b546-b48ed511fb8d | -22.7336 | -49.34766 | 2026-01-22 04:36:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d6cad27-5419-38ae-93cf-1a7278636aab | -19.67271 | -56.99191 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1c0f949a-3bff-39e5-a561-bf52161fb66a | -19.63435 | -56.96745 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d4ba3be8-6fca-314f-9cc3-85e633b0c61c | -18.02753 | -53.6816 | 2026-01-22 04:36:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01ff4e7e-d230-333e-a030-0a71eaa7c3f6 | -20.32543 | -55.92907 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 24cf7cc8-4f40-35a5-9dcf-a1da8d1fa86b | -23.36845 | -51.40396 | 2026-01-22 04:36:00 | NPP-375D | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| adb9cfbe-ffa8-35ae-9c98-2a46b96dd4bb | -19.67534 | -56.88308 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8e8f6ffd-297c-33bf-aa99-78c1e68f5d0c | -23.42065 | -47.10246 | 2026-01-22 04:36:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c95a7c48-0146-3505-ab63-f9b75f136239 | -20.35681 | -57.87885 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0fbbf03a-7cc4-31af-8821-5c656a1484ad | -22.02338 | -56.33786 | 2026-01-22 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 817ae79f-e2b1-39a7-9103-f2cb908e06a6 | -19.66611 | -57.00082 | 2026-01-22 04:36:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5d279e50-099b-3b4b-920a-954951368b78 | -19.4757 | -55.47067 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 98b5f668-ff46-3282-bffc-d9691014e993 | -19.64704 | -56.92854 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 61544f32-44d8-3115-bc18-3edb7d6fed97 | -18.29814 | -54.57341 | 2026-01-22 04:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07e29c96-3f83-3233-88df-99ec4129c4e3 | -23.29496 | -48.8556 | 2026-01-22 04:36:00 | NPP-375D | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6d07403-3ae4-3c58-8608-4077aca2623e | -19.68349 | -56.8901 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5249d04e-6c0f-3a49-9177-1ce615dd3b5e | -19.68448 | -56.88515 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a1e9552a-4100-3278-b978-16dbe95ed0bb | -21.19627 | -56.93392 | 2026-01-22 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43e59535-2839-3d1e-8359-1b94287c9279 | -19.32819 | -54.02357 | 2026-01-22 04:36:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a7265e0-c422-399f-b76d-adbd4be82057 | -19.21444 | -53.44016 | 2026-01-22 04:36:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b28c2112-8eae-39e5-aa3c-49da65c2a62f | -18.42098 | -54.56324 | 2026-01-22 04:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44c5fec1-66bc-3a34-a8c7-2145b5183be7 | -20.31841 | -57.8698 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 41014753-543a-3e99-a01c-eb7b25870c5d | -21.19725 | -56.92902 | 2026-01-22 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87a9b792-60f4-3d41-a399-5e79debfefe5 | -19.63895 | -56.96849 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 423314fd-fc88-3a0b-ad43-98ed56aaa1d1 | -19.34433 | -54.17602 | 2026-01-22 04:36:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 141afe76-4e98-3153-ba89-4de181f3cf90 | -22.03009 | -56.30436 | 2026-01-22 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README3.md)
