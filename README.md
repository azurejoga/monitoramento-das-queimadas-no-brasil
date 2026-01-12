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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e54f258a-a97e-32e0-8f53-21cff04ef132 | 1.3586 | -60.046 | 2026-01-12 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 92ec6cd6-23c6-3fc5-89e7-49a2ff348883 | -13.3853 | -53.5683 | 2026-01-12 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d807dfa2-04b3-32fb-86b6-139c9576fedc | 1.3586 | -60.027 | 2026-01-12 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 89ab8294-48c1-3a7b-8f98-cf35d97c5f26 | -13.3857 | -53.5475 | 2026-01-12 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 802f58a7-1daa-3ac1-a1e7-a2983763f4ad | -0.0828 | -51.2738 | 2026-01-12 00:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e6542411-be3c-3c39-ad5d-1afa309be743 | -19.9072 | -40.941002 | 2026-01-12 00:18:00 | METOP-C | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 943a626a-0ade-3bc8-84dd-606b36c057fa | -9.3584 | -36.0312 | 2026-01-12 00:18:00 | METOP-C | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 344aa503-fc95-3095-98e5-613b307bb22e | -3.9335 | -38.3964 | 2026-01-12 00:18:00 | METOP-C | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8e7b14b1-d1ac-38fe-a16c-151ac9464448 | -10.4264 | -36.9375 | 2026-01-12 00:18:00 | METOP-C | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6930a1e1-8859-3bc0-b579-949532a8c042 | -17.282101 | -41.246498 | 2026-01-12 00:18:00 | METOP-C | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1053eec9-5e93-334a-94f1-993d61e2c92d | -2.4754 | -45.622002 | 2026-01-12 00:18:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e055d49-efc7-3595-9dde-01273f0b4a5c | -3.9433 | -38.394199 | 2026-01-12 00:18:00 | METOP-C | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 101b0a65-520d-306a-a462-6d202ad5d061 | -19.9088 | -40.9487 | 2026-01-12 00:18:00 | METOP-C | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0cfb48df-6fb6-3656-8c99-52d4561babfa | -6.6481 | -37.368301 | 2026-01-12 00:18:00 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| d536e85d-3312-3e1b-ab54-7dbb57dfbf8b | -6.0039 | -39.527699 | 2026-01-12 00:18:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e6493718-98c9-3d63-8007-99d4660b18d0 | -4.5043 | -40.440201 | 2026-01-12 00:18:00 | METOP-C | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 30b45ea9-eff3-320a-8baa-59bae9ec75ab | -17.274 | -41.2561 | 2026-01-12 00:18:00 | METOP-C | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57a9c2aa-45c8-324d-986e-1afb7acc0fcc | -2.5139 | -47.562 | 2026-01-12 00:18:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b26b1da-785e-320f-a2a4-f89a807ef296 | -6.002 | -39.5196 | 2026-01-12 00:18:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ef84c8cc-c2f8-3eb2-87a8-acc4041f9211 | -17.8342 | -40.146301 | 2026-01-12 00:18:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b7f653c-7cff-3cd4-8c8f-65d6feff5840 | -2.4605 | -45.601398 | 2026-01-12 00:18:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9577aa20-2e31-3d46-ab74-42c39e69e88f | -2.5161 | -47.571499 | 2026-01-12 00:18:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c414c3b8-b9b3-3edb-b549-c59d4e8fae4b | -3.5519 | -43.652302 | 2026-01-12 00:18:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84ba30ad-5b21-36d1-9eb3-27c3e2974c02 | -2.9405 | -45.8111 | 2026-01-12 00:18:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5ba2eaa9-f649-3a81-8634-d6701c558700 | -17.2724 | -41.248699 | 2026-01-12 00:18:00 | METOP-C | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0fb5a550-e2fa-3691-ad0a-a6a3f20d15c8 | -3.5535 | -43.6591 | 2026-01-12 00:18:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a6d92f7-8e67-37d8-827e-407ac2b06853 | -6.0706 | -35.278198 | 2026-01-12 00:18:00 | METOP-C | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3af8b317-1b8a-3f19-912b-669bb3da3e0d | -13.4367 | -43.845798 | 2026-01-12 00:18:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e87958b5-249a-3330-b27f-26d132caadbe | -10.4287 | -36.9473 | 2026-01-12 00:18:00 | METOP-C | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 948ea14a-e31f-3034-8422-082555139e8c | -9.3775 | -41.215599 | 2026-01-12 00:18:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0bdf81ed-1d46-3a03-aad4-8279e952e790 | -5.9673 | -39.679401 | 2026-01-12 00:18:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ec5b6efb-afd0-3dcc-90c2-f8b3380de028 | -3.5987 | -43.540901 | 2026-01-12 00:18:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0c81f7-aed9-39b4-90f2-11c78366ea1e | -16.313801 | -45.1096 | 2026-01-12 00:18:00 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95e66963-ba73-3aca-b674-cc85880ef4c7 | -3.9462 | -40.7024 | 2026-01-12 00:18:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9f446911-fd0e-32ac-9f8f-54c1bfc70c21 | -3.7933 | -41.602001 | 2026-01-12 00:18:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 828cdce2-4cd0-3c34-b9f5-dc9964c38f24 | -6.7667 | -38.5597 | 2026-01-12 00:18:00 | METOP-C | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| d4a2f17a-387c-3c44-a0f4-7c5ec2e85c95 | -17.8374 | -40.160702 | 2026-01-12 00:18:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2cb2d9df-3caf-3674-b252-74bf896329a4 | -4.5397 | -40.504101 | 2026-01-12 00:18:00 | METOP-C | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d23d6a9e-d9bc-3fc4-8e79-9b95fc172ee8 | -9.3556 | -36.0196 | 2026-01-12 00:18:00 | METOP-C | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2d49e209-930a-3033-9d7a-18ef20e082de | -2.4835 | -45.612202 | 2026-01-12 00:18:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7252e811-30cd-3ca0-a1e5-85dce953ee1a | -3.6003 | -43.547798 | 2026-01-12 00:18:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1cc3c7d-072e-3795-bdd0-a0dfabfd69f0 | -20.360399 | -40.9491 | 2026-01-12 00:18:00 | METOP-C | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d82865c-e7f4-30ea-bfbb-903c42028869 | -2.5769 | -45.842098 | 2026-01-12 00:18:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef19a793-c743-38f9-ae86-78d919b09bdd | -1.6517 | -45.442299 | 2026-01-12 00:18:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a44ce55e-7c43-356c-be53-4dc66cd95beb | -17.8358 | -40.1535 | 2026-01-12 00:18:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e360732c-7405-30e7-b874-83c5298f3c44 | -5.9691 | -39.687401 | 2026-01-12 00:18:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 07f34a5e-fc87-3f34-b044-8d8f19c74f5b | -4.5495 | -40.501801 | 2026-01-12 00:18:00 | METOP-C | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 25f746f2-8eed-35b5-8e72-7c73ef9ef953 | -9.9855 | -36.314701 | 2026-01-12 00:18:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4715b4ca-e6f3-3878-88b4-2067e13f52f9 | -6.7765 | -38.5574 | 2026-01-12 00:18:00 | METOP-C | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 9a514d63-e97e-3fc5-abda-8c423adc7d7c | -22.554199 | -42.181198 | 2026-01-12 00:18:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b545d26-0be3-3029-823a-6a71f51d0f49 | -5.191 | -40.732201 | 2026-01-12 00:18:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b7722f07-b2bc-39ea-a7a9-5ba96e34bfa5 | -10.5558 | -44.3274 | 2026-01-12 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff250b7d-7e29-36ad-8598-42e353aea479 | -2.472 | -45.6068 | 2026-01-12 00:18:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32da445f-08c6-33ad-84d8-364fd8533e50 | -0.0881 | -51.274399 | 2026-01-12 00:18:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4b90ac42-0e3a-3034-9660-925f8e3bc07d | -13.4385 | -43.854198 | 2026-01-12 00:18:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 300923af-8a7c-3a2b-85e7-e6bbb299e47b | -10.554 | -44.319302 | 2026-01-12 00:18:00 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55c4135e-34df-3573-b774-3ca7e983260d | -5.1927 | -40.739601 | 2026-01-12 00:18:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 897b38af-d8ec-32eb-aea8-6d9ae54f0d97 | -2.4737 | -45.614399 | 2026-01-12 00:18:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c47a654-eb82-3276-ae10-6e9215435472 | -0.0828 | -51.2738 | 2026-01-12 00:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8be33b11-61db-31a2-9e01-03b3ca34fd99 | -0.0828 | -51.2738 | 2026-01-12 00:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 60.5 |
| affe3bd2-1042-303b-8691-3ee54616cc27 | 1.3586 | -60.046 | 2026-01-12 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 9c958498-d2a0-38fe-8a52-d36f0f808551 | 1.3586 | -60.046 | 2026-01-12 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d8bf859d-473e-3140-92e9-01c2a4e7a3f2 | -17.3034 | -42.6678 | 2026-01-12 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 3969ac89-9d43-3948-8369-bee723dc606d | -17.3034 | -42.6678 | 2026-01-12 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 08d2c07c-e5be-379e-8e31-6e555d90b223 | -9.3803 | -35.8684 | 2026-01-12 01:30:00 | GOES-19 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| 72a48930-80ee-39f9-a163-bc41bea0e248 | -17.3034 | -42.6678 | 2026-01-12 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| afaabcf6-3988-3c57-a7be-93ae42c35299 | -17.3034 | -42.6678 | 2026-01-12 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 5e5096a5-324b-3015-b10a-05801e20e2fa | 1.3586 | -60.046 | 2026-01-12 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 5b756de3-f90a-3d3f-a424-23c4e94e0eab | -4.91558 | -37.49021 | 2026-01-12 02:57:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 982d7a46-5b70-30ac-943e-86fa4ca9729f | -4.90858 | -37.4889 | 2026-01-12 02:57:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bb858f5f-d869-3c30-bf8d-51edb475787b | -6.09916 | -35.26629 | 2026-01-12 02:57:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 8e31be00-a92d-33f9-b040-dce49daaf315 | -6.09835 | -35.27081 | 2026-01-12 02:57:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 4b64fc66-f6c4-3434-8bac-497889123fb1 | -6.60495 | -35.33514 | 2026-01-12 02:57:00 | NOAA-20 | CAIÇARA | PARAÍBA | Brasil | 2503605 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 78449f10-4c36-300b-81d9-bc9e08a83902 | -4.91095 | -37.48799 | 2026-01-12 02:57:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b2464122-f0c0-395a-87db-71c90876aa6a | -4.90977 | -37.49469 | 2026-01-12 02:57:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 76a77fe4-787e-341d-940f-4ab530a24650 | -6.60414 | -35.33961 | 2026-01-12 02:57:00 | NOAA-20 | CAIÇARA | PARAÍBA | Brasil | 2503605 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d6d63b0e-51d8-3a88-a612-9b07708f4ddd | -0.0828 | -51.2738 | 2026-01-12 03:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 8fbc70ef-bd1e-3148-b99a-303206d089e6 | -4.91473 | -37.4867 | 2026-01-12 03:46:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e3d585d1-6e27-35f7-8ff7-ab6dc9a823f5 | -3.94655 | -40.69872 | 2026-01-12 03:46:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c8d3987e-a2f3-3e35-8013-1b67dcf9ef04 | -3.9504 | -40.69938 | 2026-01-12 03:46:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0da85f03-9adf-340e-bf29-cdd094dba5a5 | -1.57604 | -45.62597 | 2026-01-12 03:46:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0fbc8ee-32d2-31d6-8f44-1cd93a7f1b02 | -3.72324 | -43.32349 | 2026-01-12 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 459ddc00-9fc8-333a-b995-7572fd98d848 | -3.94577 | -40.70348 | 2026-01-12 03:46:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| adb8c13c-0848-3dd7-ab4b-deed95c5481d | -0.84813 | -47.57122 | 2026-01-12 03:46:00 | NOAA-21 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 6df2ce92-41d6-3765-89f5-d43912fa9950 | -3.01594 | -39.9951 | 2026-01-12 03:46:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b3b2ab0-cfce-3b37-b66b-60a286c8149e | -2.87197 | -45.22839 | 2026-01-12 03:46:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc1ae69f-9ee2-33c8-9abb-f9341fdd2766 | -0.84964 | -47.57371 | 2026-01-12 03:46:00 | NOAA-21 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| baa2dfdf-dcc8-3f75-a8c1-9f0e0c97baae | -3.91646 | -38.46233 | 2026-01-12 03:46:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f6f2c91-db2e-3ecd-bed3-7684f8879f84 | -3.60122 | -41.86658 | 2026-01-12 03:46:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff78956b-3254-3514-9585-4f7431bb8d95 | -1.85523 | -47.48529 | 2026-01-12 03:46:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f80050d-7008-32ca-a4ee-3406a445c595 | -2.57978 | -45.85326 | 2026-01-12 03:46:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88c9b932-b839-3d1d-a9aa-17cfea672d90 | -3.94089 | -38.39707 | 2026-01-12 03:46:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 59e78d4c-878e-32d5-9293-10c85e5956ab | -3.79711 | -41.60603 | 2026-01-12 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e91e6e51-217b-32d5-8681-29699f5e302d | -2.57481 | -45.84871 | 2026-01-12 03:46:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| afe37361-6621-3fb2-abcb-e075db517c36 | -1.85368 | -47.48157 | 2026-01-12 03:46:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa8d83b7-b20c-3be6-950a-46ab9368e29a | -2.58039 | -45.84954 | 2026-01-12 03:46:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29a04c2d-3841-34cd-8477-d917bbe3fc35 | -3.94432 | -38.3976 | 2026-01-12 03:46:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a354f9b1-5a4a-3601-b222-d3565c8afba0 | -4.22111 | -41.77196 | 2026-01-12 03:46:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b22a3f0a-bf07-3718-a7d5-17deb3bff6a7 | -1.85603 | -47.48029 | 2026-01-12 03:46:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46c8e7e3-a8a9-3218-b0b8-46e6e5a8a48e | -0.85052 | -47.56847 | 2026-01-12 03:46:00 | NOAA-21 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |


[Clique aqui para ver as próximas entradas](README2.md)
