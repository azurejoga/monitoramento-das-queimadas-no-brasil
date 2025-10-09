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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25131f89-a536-3db1-afa4-64e61128e3b5 | -15.21142 | -56.79526 | 2025-10-09 01:30:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7d968952-f442-3a02-9fb4-ea86e2effb3b | -16.60513 | -58.15543 | 2025-10-09 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 052dfb97-7f97-3255-8e74-7befad8c0271 | -15.97447 | -59.53716 | 2025-10-09 01:30:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7dd475d0-2931-332d-b626-25a493938b22 | -16.59481 | -58.15725 | 2025-10-09 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 905db1bd-b3fb-3e7a-b339-0145cb76a3e8 | -16.60311 | -58.16315 | 2025-10-09 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.2 |
| 437ebe15-a84e-3a6d-951a-ec2a793cdc41 | -15.5449 | -55.96069 | 2025-10-09 01:30:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| a57194fa-9911-3a11-a5a5-07a78800388c | -16.59682 | -58.17017 | 2025-10-09 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| dd2aeab9-7a5e-3379-aa4e-2dc1857109a1 | -15.17214 | -56.82491 | 2025-10-09 01:30:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 54cd25aa-f708-3f3f-bead-57db00f0a6a6 | -16.01747 | -59.53428 | 2025-10-09 01:30:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9baa8c8-9e93-31cb-806d-785e4d2a5b83 | -15.17478 | -56.84115 | 2025-10-09 01:30:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5354a129-4ac9-352b-950f-e65ceb8c672c | -14.46774 | -52.90641 | 2025-10-09 01:30:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| e1a21bd5-d92d-31ba-b5ed-f8593f5ab354 | -16.00006 | -59.54845 | 2025-10-09 01:30:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a015a9dc-b27b-3321-83d8-d9babf7ae6e2 | -14.94277 | -59.42364 | 2025-10-09 01:30:00 | TERRA_M-M | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| abac7de8-4c7b-3e44-a8df-3bee0c7a97aa | -9.62622 | -67.51843 | 2025-10-09 01:32:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7b6ecd8-af7a-30b3-b029-c41baca1f6ad | -9.56828 | -63.21328 | 2025-10-09 01:32:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a5c04270-db79-3aa4-8a87-8f5beff19bf5 | -10.28527 | -62.47467 | 2025-10-09 01:32:00 | TERRA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f66e016f-ec8b-3e7f-a3cf-24a14a47630c | -9.43696 | -63.72496 | 2025-10-09 01:32:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e5af55e-5c2b-3543-bb7a-e69315352f8a | -9.58411 | -65.70585 | 2025-10-09 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 98ac8274-f30a-37a8-82e0-88c93ba27f6b | -12.09356 | -64.22703 | 2025-10-09 01:32:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a31815f-30da-3ec9-8c3a-9c8d3967066f | -9.37196 | -66.59733 | 2025-10-09 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0582ca62-73d3-3143-aa5c-7d5667a411ea | -12.08458 | -64.2283 | 2025-10-09 01:32:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c12d748a-2454-3a10-ae7e-1de065bb7ed3 | -9.58543 | -65.71592 | 2025-10-09 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 51ce802f-d865-3e48-a3c1-217b9488f1ee | -12.39763 | -63.88592 | 2025-10-09 01:32:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c617ef99-f966-3fe9-9790-ef5186fb3c27 | -11.87625 | -62.77181 | 2025-10-09 01:32:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d69aeaf3-52d0-3212-9c6d-25d1935f366e | -12.22125 | -64.35593 | 2025-10-09 01:32:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 94051c77-f555-38f7-9c6a-fc0837001ee2 | -12.21999 | -64.3465 | 2025-10-09 01:32:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a76ebbc3-3cfb-37d0-8992-54232b75659e | -9.79283 | -60.13838 | 2025-10-09 01:32:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 165107dd-6033-38dc-80f2-42f1431bf6b8 | -9.68796 | -67.45197 | 2025-10-09 01:32:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 75dd291d-4f42-349b-b535-28c56a186002 | -12.39639 | -63.87674 | 2025-10-09 01:32:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4b6167be-1648-38fc-8ed7-166562d5d2a0 | -9.41245 | -67.14651 | 2025-10-09 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3d506e7a-0edb-3a21-b5aa-0da88ece4fe7 | -4.9894 | -45.3159 | 2025-10-09 01:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8df30ed8-c7ad-3aaf-a594-a1104bce87dc | -14.4133 | -43.9911 | 2025-10-09 01:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 2a50e943-e934-3345-93a0-59a121068dc5 | -7.7569 | -44.0183 | 2025-10-09 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 3175ed4e-f077-3c9b-8cc8-2072355be20a | -11.666 | -47.5288 | 2025-10-09 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 61940214-22ba-351a-bf7f-e13958ab13fd | -10.4247 | -46.6135 | 2025-10-09 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 476295aa-e480-3015-bae6-d220c52768ab | -4.9908 | -45.1351 | 2025-10-09 01:40:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 49587728-621c-3971-8c74-a812c970c0fc | -4.9721 | -45.1362 | 2025-10-09 01:40:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| d98e3efb-39ab-3b63-a82e-56a7243f8761 | -4.2864 | -44.5171 | 2025-10-09 01:40:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 41511abe-9a98-3c71-8eb5-82e29f3ac97d | -6.6993 | -46.3169 | 2025-10-09 01:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 97caf30b-3249-3718-837e-cdf3ffceee57 | -6.6808 | -46.2961 | 2025-10-09 01:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 01839e78-8c5b-3343-ab61-ba7c1ed19a09 | -14.4334 | -43.9635 | 2025-10-09 01:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 00c433e2-d273-3710-8a3c-bee5f47cb5d3 | -5.3999 | -40.9856 | 2025-10-09 01:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 205.3 |
| 4307d46b-3d19-3e91-8f0d-1bf7f7b6444b | -21.4062 | -49.1338 | 2025-10-09 01:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.5 |
| 2fe20f1f-b321-3e42-942e-cdb9d6a14cab | -4.305 | -44.5161 | 2025-10-09 01:40:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| b35f2380-b2ea-3f78-8a11-bf7a027b27a4 | -7.7755 | -44.0396 | 2025-10-09 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| a7f9ebf8-b2e8-32f7-9ca4-160114609197 | -21.3862 | -49.1154 | 2025-10-09 01:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| 5c26b3d4-a599-3233-aaf2-4cc5e419a0f1 | -14.4329 | -43.9874 | 2025-10-09 01:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 0ca1f9a6-3c6b-3af2-bd83-b37737b257fd | -4.9708 | -45.317 | 2025-10-09 01:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cf299b38-289c-3aad-8b21-0779bd0a7891 | -10.8749 | -44.6172 | 2025-10-09 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 558.0 |
| fb667aae-dbf4-37f5-9429-02fc1472611f | -17.8413 | -57.6459 | 2025-10-09 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 6353f34b-510d-3eb9-b202-b8ac8cbb2384 | -8.1993 | -43.3424 | 2025-10-09 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 863b09cb-4696-3486-9a1b-f7567ee40a2a | -9.0829 | -47.9594 | 2025-10-09 01:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 0054c18f-4743-3cb9-a5c2-043f5904b1db | -4.991 | -45.1124 | 2025-10-09 01:40:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 5178139b-574a-3f8f-9f48-4d7581d5ff1d | -14.4717 | -52.8937 | 2025-10-09 01:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1fe7a25d-39a9-31f3-b1e2-e1954f0d6f55 | -10.8745 | -44.6404 | 2025-10-09 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 321.5 |
| 237aee38-138f-33d9-b4af-776e9573102b | -14.4138 | -43.9672 | 2025-10-09 01:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 203.9 |
| 27bf1e49-ff0f-3898-a983-9a30cc34b66c | -10.8562 | -44.5966 | 2025-10-09 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a1f922ea-7d8b-321e-b906-394d153c18da | -11.0469 | -50.777 | 2025-10-09 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9384c5e0-a8fd-37a5-b3ec-3ab078c57118 | -5.4001 | -40.9613 | 2025-10-09 01:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| 7ac60256-4090-37e8-b1e1-c44755eb6b74 | -6.6995 | -46.2946 | 2025-10-09 01:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 6a48a6d5-8117-3c54-b789-1644e3d4e819 | -18.4118 | -45.2394 | 2025-10-09 01:40:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 06ead597-972e-3339-add9-2fc682b2b841 | -12.8913 | -54.7372 | 2025-10-09 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 31efb563-d5fa-3900-ac36-a2c4ea588771 | -12.9297 | -54.7127 | 2025-10-09 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ace86355-ee46-3940-87cd-c10e3f950d59 | -10.4244 | -46.6359 | 2025-10-09 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 45a5c688-cce0-317a-be27-98c0ee8e31ed | -21.3856 | -49.1385 | 2025-10-09 01:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.0 |
| eb01b46d-bcbb-3796-a789-87e5dfdbfdc1 | -10.8558 | -44.6199 | 2025-10-09 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 726.5 |
| 0610e395-1eae-3572-afd2-24bd549e3b10 | -21.4069 | -49.1106 | 2025-10-09 01:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 131.1 |
| 1a5a595d-9711-392e-a2fb-5a997cbc86cb | -13.7909 | -45.8552 | 2025-10-09 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3bed38a2-fc9d-3b51-8138-a59e6cb9a75b | -6.6806 | -46.3184 | 2025-10-09 01:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 1dc43f34-e40b-3a04-b70f-a4bfc270a843 | -10.8753 | -44.594 | 2025-10-09 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 59f9d332-c2d4-35c8-a49d-4bc08db5ffb3 | -9.191 | -46.8881 | 2025-10-09 01:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 373ff3bb-48a9-3c4c-a4f1-71afe3dd37c9 | -10.8554 | -44.6431 | 2025-10-09 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 392.5 |
| 2423a7f8-1880-3581-bc69-1d404ff3e351 | -4.9723 | -45.1136 | 2025-10-09 01:40:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8dfe9951-11df-378a-8a18-c981218b039e | -7.7567 | -44.0415 | 2025-10-09 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| c51574a3-7d68-3566-b450-2cd5372e4ff8 | -12.9297 | -54.7127 | 2025-10-09 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 03bc8c40-8169-3384-8c98-faf539f0e399 | -5.3999 | -40.9856 | 2025-10-09 01:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 209.6 |
| 4417df79-ff44-3442-97ce-68a2383599f3 | -4.9894 | -45.3159 | 2025-10-09 01:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e7ddc4da-18d5-3499-8b28-db17f7af2317 | -6.6995 | -46.2946 | 2025-10-09 01:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| abfe9d21-d964-3327-98a1-ca0f32356bcb | -6.6993 | -46.3169 | 2025-10-09 01:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 130206e4-804e-3547-b8d6-94459972ade6 | -7.7567 | -44.0415 | 2025-10-09 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| f0bad1f6-9d8d-3da3-ba00-32bf5eb4c9d1 | -18.4118 | -45.2394 | 2025-10-09 01:50:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 4c21694b-dfc7-3e39-965c-25cfed1e7af2 | -17.8413 | -57.6459 | 2025-10-09 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| af5f329e-ee8c-3215-89b6-1766cd6e45e1 | -10.8745 | -44.6404 | 2025-10-09 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 258.3 |
| 2152b473-142a-3e91-9695-83b32b5e327a | -8.1993 | -43.3424 | 2025-10-09 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 5ebf7ab4-da30-3b49-a274-3fb361a8c31e | -14.4138 | -43.9672 | 2025-10-09 01:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 4d91d930-5e17-3eda-a02b-c09d7aefc2bc | -6.6806 | -46.3184 | 2025-10-09 01:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e9e45b7a-dfec-3e61-a1e0-e4d7c37b5f79 | -4.9723 | -45.1136 | 2025-10-09 01:50:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| fcd4fa82-6cfa-3f01-bee3-75267768e98f | -21.3862 | -49.1154 | 2025-10-09 01:50:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.2 |
| 1acef02a-d16c-3396-80a1-17641106f988 | -10.8749 | -44.6172 | 2025-10-09 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 370.9 |
| dd886b01-9eed-3310-a643-dd9c9a9fb486 | -12.8913 | -54.7372 | 2025-10-09 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 824e75e5-a912-377a-b004-5b4927405e58 | -21.4062 | -49.1338 | 2025-10-09 01:50:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.1 |
| 92c6592c-9b56-3c60-bc8b-4882b8d8404b | -4.991 | -45.1124 | 2025-10-09 01:50:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 266.8 |
| 497994eb-7963-397b-a4d9-7cb89095083b | -21.3856 | -49.1385 | 2025-10-09 01:50:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |
| 65213730-ba94-33f0-80b1-54eb00e212b8 | -21.4069 | -49.1106 | 2025-10-09 01:50:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.4 |
| 2c5d4b57-c7ab-33d9-bbf3-37e6d1f35810 | -14.4329 | -43.9874 | 2025-10-09 01:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 3f69d918-9890-3743-b7e4-8049cf6f8462 | -5.4001 | -40.9613 | 2025-10-09 01:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 4cf22278-391c-33d0-90f6-cd004748845d | -13.7909 | -45.8552 | 2025-10-09 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 230dcc2a-9daf-378e-b688-20dd688223e0 | -7.7755 | -44.0396 | 2025-10-09 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 243a51f6-9040-30cb-b43a-703d88a2e7b1 | -10.8562 | -44.5966 | 2025-10-09 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 04df24a3-172e-3725-833b-730d3583b1e9 | -14.4133 | -43.9911 | 2025-10-09 01:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 101.8 |


[Clique aqui para ver as próximas entradas](README7.md)
