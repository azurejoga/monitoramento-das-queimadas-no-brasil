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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66cb147a-4726-3afd-86f3-c1b6cd1b83ed | -7.0252 | -44.598099 | 2025-06-07 00:47:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d21b10e-70a4-3342-ae4a-17a2546d6392 | -11.2551 | -60.786999 | 2025-06-07 00:47:00 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| df0aff9f-405e-399d-b169-82934313149a | -7.0126 | -44.589199 | 2025-06-07 00:47:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 918c2c26-1333-3cae-b62d-ca0f7aeb4366 | -12.2825 | -50.100201 | 2025-06-07 00:47:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e482c9c-657e-3472-9371-f1f896725184 | -6.961 | -42.9011 | 2025-06-07 00:47:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6464a152-1cd0-39b3-a36b-7ffd1e23b1db | -9.3377 | -48.520802 | 2025-06-07 00:47:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0f10517-f41b-3d53-9b18-429b86e28b9e | -12.8841 | -52.204102 | 2025-06-07 00:47:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 085765ea-00f2-3d12-99d2-ff929c448477 | -10.492 | -53.6604 | 2025-06-07 00:47:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3a61cab-10bf-3f6b-a00e-62d612aea3f3 | -9.7453 | -46.9935 | 2025-06-07 00:47:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8262a612-7c1d-3ce2-a2b9-447b6d53e278 | -10.4646 | -47.950802 | 2025-06-07 00:47:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 203c98f2-ae09-3895-a182-6caf1aff5bec | -8.8725 | -50.1828 | 2025-06-07 00:47:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d76083ed-756b-3b4b-926b-3e9b86d5f182 | -11.7923 | -47.400902 | 2025-06-07 00:47:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9af25f3-ca12-34f7-b818-c420050eb2b6 | -3.0495 | -49.4319 | 2025-06-07 00:47:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 605268e3-2530-3d28-8424-dfced7d9918f | -6.9549 | -42.918201 | 2025-06-07 00:47:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d9493f62-2f89-3551-90b4-f1ca567a41a4 | -7.0224 | -44.5868 | 2025-06-07 00:47:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45242af0-cdef-31a8-8f92-b3894b92d1dc | -6.4502 | -45.724701 | 2025-06-07 00:47:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 733b2c72-68d1-38b5-a37c-0e272937cde6 | -5.6496 | -43.726898 | 2025-06-07 00:47:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49a8dc4a-0271-396d-aada-5f7d99e0ac0c | -12.2923 | -50.0979 | 2025-06-07 00:47:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9df3fab6-bf0a-33da-8e2e-3022995b3786 | -6.9416 | -42.9058 | 2025-06-07 00:47:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a83c6f3e-cf02-3d16-97d7-a20cc9ece983 | -11.2591 | -60.7556 | 2025-06-07 00:47:00 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0497d700-f356-3613-a3bc-626a9f0c68fa | -9.5446 | -47.766998 | 2025-06-07 00:47:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0c6d07-4b95-3248-87b3-f81fcf25c2f8 | -11.2648 | -60.785198 | 2025-06-07 00:47:00 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 996900da-d0bf-31f1-adaf-19fdd4127443 | -9.0783 | -47.1427 | 2025-06-07 00:47:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db2712f0-d7b2-38cc-8acb-619f73d92b03 | -12.5296 | -58.328701 | 2025-06-07 00:47:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3cf3c0d7-9eed-38eb-9432-a06359a1cb64 | -11.8177 | -44.261799 | 2025-06-07 00:47:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17b8be93-0481-3141-8295-07428ba2cbc4 | -6.5983 | -43.901402 | 2025-06-07 00:47:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09704dc3-3211-35c6-9dea-cdffea2eeb06 | -9.4111 | -48.436699 | 2025-06-07 00:47:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8dea736-5fdf-3e5d-a869-67d29d974c64 | -11.771 | -47.398102 | 2025-06-07 00:47:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 523f5d86-aa4a-372f-a35f-5467652b37d2 | -5.6463 | -43.713402 | 2025-06-07 00:47:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b104e993-1167-3d94-b6c3-adea44f68eac | -17.263901 | -42.671101 | 2025-06-07 00:47:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4122ae82-bf2c-3b13-ba7c-29b71df6b056 | -7.729 | -44.184101 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ef3b5b32-0ce7-365c-a50a-39af358e49ae | -6.6684 | -47.737801 | 2025-06-07 00:47:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cbb43d8-fe07-3d1a-af39-092cc51b296a | -9.1301 | -46.880901 | 2025-06-07 00:47:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22fb2c40-5cde-388a-9714-9a11b8bc123b | -5.6333 | -43.702099 | 2025-06-07 00:47:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3189063a-6160-3220-b3c9-ccb6c5357b19 | -7.0057 | -44.602798 | 2025-06-07 00:47:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4db4158-9558-34d9-8fd2-fb2b77b43ddc | -7.8624 | -47.901001 | 2025-06-07 00:47:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35e8c7b8-2504-31ca-8fd9-afede306be18 | -12.531 | -45.411999 | 2025-06-07 00:47:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c51d80cf-fe6c-3052-bc25-4e6305b7fe35 | -9.0666 | -47.137199 | 2025-06-07 00:47:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf928ec1-5d35-37d8-9b8d-94cf32765f95 | -12.2907 | -50.090698 | 2025-06-07 00:47:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e02dde2-d04c-3858-92b4-d2ccc8105f77 | -3.0512 | -49.439098 | 2025-06-07 00:47:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b0e9a0c-eba5-326a-aa31-c0071acdacd9 | -10.8868 | -54.3158 | 2025-06-07 00:47:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96d41f48-b3a7-3112-99d7-53cbc229128d | -7.8642 | -47.908401 | 2025-06-07 00:47:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b56e7edd-6929-3b6a-90cb-26865fd141e3 | -9.3361 | -48.513802 | 2025-06-07 00:47:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c650c4c-b60b-3ee9-8c72-1e826f9897fe | -11.8202 | -44.2719 | 2025-06-07 00:47:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46910361-fca9-3197-a856-1215514330f1 | -8.206 | -48.980999 | 2025-06-07 00:47:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f20463e3-46c8-3495-ad88-66c15e27f1f7 | -6.2983 | -48.495098 | 2025-06-07 00:47:00 | METOP-C | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe9ce5a0-dd13-34fa-af70-1a11532f8532 | -17.270901 | -42.657799 | 2025-06-07 00:47:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1ba6019c-d3d2-3a8f-9ad1-73452a476a04 | -7.7331 | -44.158199 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e2d4095-8f5a-38b1-9bec-2ab821f6b3d3 | -14.0372 | -55.1283 | 2025-06-07 00:47:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d95df2a7-9b6e-3977-b58c-489e517c19ec | -10.7074 | -48.780499 | 2025-06-07 00:47:00 | METOP-C | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4fee4ec7-2570-34ba-883f-124e79b62ee0 | -13.4732 | -56.845699 | 2025-06-07 00:47:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d961206e-c305-32db-a390-08abd06ebbaa | -10.6296 | -49.4342 | 2025-06-07 00:47:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23321e6c-1df8-3704-8618-825b07033bd7 | -11.381 | -56.558102 | 2025-06-07 00:47:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4bcd8ee-b0b9-302f-952a-2aede2229577 | -5.643 | -43.699799 | 2025-06-07 00:47:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1814e49-8f0e-3118-81a3-de01ccd0a133 | -8.8741 | -50.189701 | 2025-06-07 00:47:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4545fa2-c4a3-35c2-b87c-0babe6718f66 | -12.2896 | -49.5322 | 2025-06-07 00:47:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef5a729f-95ab-3ca2-aa5a-c8b660c3488a | -7.7359 | -44.169998 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 149501b2-f43f-3c8a-8730-a9b97188aebe | -6.9513 | -42.9035 | 2025-06-07 00:47:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 791a7821-9c0f-3b99-bfc3-617837cd8bc1 | -9.3996 | -48.431801 | 2025-06-07 00:47:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83bf283e-b6bd-3188-8890-e6358a40f2ed | -11.3779 | -56.5429 | 2025-06-07 00:47:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa998c8-f40a-3e22-876a-f841870f029f | -12.5236 | -58.3576 | 2025-06-07 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 27ba094b-9487-35ac-84d2-161f155f42ee | -6.9414 | -42.907 | 2025-06-07 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| dd686233-e9f5-3611-b16f-d9f1d5d3811c | -11.7826 | -47.402 | 2025-06-07 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| d4cba5bf-9d17-3ccf-b0fa-cfd03ae3f8d4 | -13.4733 | -56.8557 | 2025-06-07 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2645c332-16e9-322d-ae7f-741674858651 | -7.0169 | -44.5954 | 2025-06-07 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 766df7b5-c99e-32d7-b166-3b01a1b84ece | -5.6379 | -43.7175 | 2025-06-07 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 3f877689-49d4-3c3a-85aa-c842d906c2dd | -11.3716 | -56.558 | 2025-06-07 00:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 48900d22-8b94-36a5-afe5-0cbd747c9a83 | -6.9605 | -42.8816 | 2025-06-07 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.5 |
| cd7fc0ab-4ac3-3d9f-b354-f746910ef589 | -12.5238 | -58.3378 | 2025-06-07 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 4652de1d-5dd6-39c9-9da5-0be5d62954bd | -6.9602 | -42.9052 | 2025-06-07 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| fcc28307-38a9-3a75-914b-00ec54731975 | -17.284 | -42.6479 | 2025-06-07 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4161345c-187f-33db-a46b-7a01a499c415 | -17.2639 | -42.6527 | 2025-06-07 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 6ef471f8-b391-357b-be12-9a3ceb9fd505 | -11.2548 | -60.7957 | 2025-06-07 00:50:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 52420903-d23b-31b0-ba3c-3b418e37ffd4 | -7.7176 | -44.1611 | 2025-06-07 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 5a797bfa-4a74-379f-bfd6-b055e2b32d69 | -6.96 | -42.9288 | 2025-06-07 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 51.4 |
| c115eec7-7567-3bbf-8508-911c9cd57ed0 | -7.7173 | -44.1842 | 2025-06-07 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c891fc57-8673-3005-a5bf-606f576f3e33 | -7.7361 | -44.1823 | 2025-06-07 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 37adf2c6-6bd3-3af0-9396-31b61ee88e0a | -7.7364 | -44.1592 | 2025-06-07 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 20cf9a7f-8cd6-350a-9e2b-2272860a9a7a | -6.9602 | -42.9052 | 2025-06-07 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 63ad315a-df98-3ee1-9f70-1e6d49e3ba72 | -7.7176 | -44.1611 | 2025-06-07 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| aad95bdc-292f-30f7-8be8-7d278731b943 | -17.284 | -42.6479 | 2025-06-07 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 8f294655-75fd-3038-9229-b0e7afc040d3 | -11.7826 | -47.402 | 2025-06-07 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 30bef8d7-b101-364f-a28d-fd536186293b | -7.7361 | -44.1823 | 2025-06-07 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f4019b3a-9d80-3ead-b628-0c253ec7d68f | -5.6379 | -43.7175 | 2025-06-07 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| a704b55a-4800-33af-9eb5-e60a8c9bebe3 | -13.4733 | -56.8557 | 2025-06-07 01:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 1df85e81-d569-32de-bff2-e228ae097d3b | -12.5238 | -58.3378 | 2025-06-07 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 57a4af21-ed8c-38d7-a70e-b97072737235 | -7.7173 | -44.1842 | 2025-06-07 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| e111ef46-acef-3b1f-86b5-33d2a52cf738 | -7.0169 | -44.5954 | 2025-06-07 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 37cdaae0-baab-3389-8d6a-693d1dbcf7b4 | -7.7364 | -44.1592 | 2025-06-07 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 52969e76-d7d3-3ee6-bd1c-95dc96122544 | -11.2548 | -60.7957 | 2025-06-07 01:00:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 88d77d30-95dc-3b71-9a26-6806add4ff92 | -12.5236 | -58.3576 | 2025-06-07 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 09bf898b-ce90-3b6d-9640-ed639ca780a2 | -17.2639 | -42.6527 | 2025-06-07 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 34ec68e9-c632-3a65-b1e8-9d686426deb7 | -5.6379 | -43.7175 | 2025-06-07 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 532508ac-5389-3d86-a4aa-7bdee8f4af41 | -12.5425 | -58.3561 | 2025-06-07 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 4e1f3fb3-bc73-3d39-b4b0-6798e65cd212 | -11.7826 | -47.402 | 2025-06-07 01:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| fce9fe04-9936-3159-bab6-61dbfaa2c686 | -6.9602 | -42.9052 | 2025-06-07 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 163.0 |
| 3754759f-7520-3c53-b5e9-1b1f0ba938e9 | -12.5238 | -58.3378 | 2025-06-07 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 9dbff761-b85b-3d4d-9179-19d9486874d4 | -7.7173 | -44.1842 | 2025-06-07 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 888c7e53-9313-36d1-8fdf-191198742765 | -17.284 | -42.6479 | 2025-06-07 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 43.3 |
| f122431c-805d-3ac0-b3c1-27db200171de | -6.9414 | -42.907 | 2025-06-07 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |


[Clique aqui para ver as próximas entradas](README5.md)
