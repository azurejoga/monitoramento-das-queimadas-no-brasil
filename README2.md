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
| 91112420-f4ea-3ca6-bd1d-c8d7bf6985a4 | -17.00927 | -49.78097 | 2025-03-30 04:17:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f39e0220-5933-3ee6-a3b9-46bfda3be1ff | -12.51907 | -39.39564 | 2025-03-30 04:17:00 | NPP-375D | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0c4ea76a-9b78-315e-b957-e2d7223bd389 | -23.64764 | -47.13454 | 2025-03-30 04:17:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7a0c6aa1-12de-3d1f-8c59-d9e79b3e632c | -22.9094 | -42.74549 | 2025-03-30 04:17:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8a81c9e6-c894-30a1-abbd-bda74221cae1 | -20.99648 | -51.79224 | 2025-03-30 04:17:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0cf249d3-fbc2-380a-a644-6b2ba8ac1a2e | -12.51556 | -39.39149 | 2025-03-30 04:17:00 | NPP-375D | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1d61d6a4-fe6e-32a3-aba1-166424e4b178 | -16.34914 | -43.69642 | 2025-03-30 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd93ee83-38c1-32c5-880f-411bc726725c | -15.56878 | -42.61507 | 2025-03-30 04:17:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6102d8bc-d96c-34ba-9565-a44ef1bb09b0 | -18.57268 | -40.67445 | 2025-03-30 04:17:00 | NPP-375D | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0e40a6cb-6550-353d-8cc6-e629005a4abf | -12.61303 | -52.23359 | 2025-03-30 04:17:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4287706-d743-379a-9a66-6d5570f272c8 | -13.96324 | -41.48864 | 2025-03-30 04:17:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8147181e-6665-3568-901d-24ec8ba06333 | -18.27217 | -46.56728 | 2025-03-30 04:17:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c662fc4-dbba-365c-9015-4062257361ad | -17.59591 | -43.19625 | 2025-03-30 04:17:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b438936-5bad-3f44-a84c-20fc5feb9ecb | -15.56909 | -47.85429 | 2025-03-30 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edc96ea1-33aa-3eeb-8c19-3e55969ed899 | -13.95962 | -41.48806 | 2025-03-30 04:17:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3cf4c145-4ca9-3efa-8c95-a5a06e09be45 | -16.68027 | -43.88253 | 2025-03-30 04:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29235077-4d19-3dc1-82fd-5416c1f86c49 | -17.66367 | -42.52542 | 2025-03-30 04:17:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ca98e70a-c91f-31e3-9b76-558be38418f1 | -16.37081 | -39.25857 | 2025-03-30 04:17:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4aad5f86-5a3d-382e-ac01-f43d13e58d8e | -14.13528 | -41.69064 | 2025-03-30 04:17:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4b2f9a2-03d4-33de-a444-bd322cb32ecb | -19.07229 | -43.47544 | 2025-03-30 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6e51392e-1e97-365c-b595-4e135ce32c2f | -15.07994 | -48.94373 | 2025-03-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b647ff3-45e9-3490-9337-ec5ebe426c38 | -17.78055 | -42.80738 | 2025-03-30 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85f52097-0fd6-39e9-af12-3e0b32986ae3 | -16.32697 | -39.56124 | 2025-03-30 04:17:00 | NPP-375D | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b08d59bf-655a-3fc1-8ba0-3cfab5761987 | -12.60926 | -52.23251 | 2025-03-30 04:17:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c4e5bec2-7ba5-3728-9c2c-22d4dac0a6f3 | -17.72987 | -42.71488 | 2025-03-30 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| af132159-b69d-3afe-a72c-d930610d96cb | -23.59235 | -47.43882 | 2025-03-30 04:17:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 654265ae-52b7-3ce2-bfff-cfb6e5c34e36 | -18.39691 | -44.19426 | 2025-03-30 04:17:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0676c868-ec33-3b9c-8099-c86aacad4180 | -21.61735 | -46.92487 | 2025-03-30 04:17:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4290574f-e498-3cde-b525-c21fb96f67f7 | -12.60821 | -52.23265 | 2025-03-30 04:17:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31c7f034-dad2-3548-9b38-67d5c176664d | -13.96263 | -41.49292 | 2025-03-30 04:17:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 539a77f8-cbd0-30be-acc4-e7266f8b29b0 | -17.38538 | -42.65728 | 2025-03-30 04:17:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecdcb476-d298-3aae-87df-e1b710bed80a | -13.37703 | -41.32621 | 2025-03-30 04:17:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c2fee905-8d8c-3f5d-9eb7-0941961295dd | -26.25035 | -49.33548 | 2025-03-30 04:19:00 | NPP-375D | SÃO BENTO DO SUL | SANTA CATARINA | Brasil | 4215802 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0eba7e68-4ca4-3432-8f34-db9428457fcb | -30.58921 | -51.5642 | 2025-03-30 04:19:00 | NPP-375D | SENTINELA DO SUL | RIO GRANDE DO SUL | Brasil | 4320354 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 474d9129-8958-33a7-bbd1-9c36b1bbffad | -21.19458 | -44.93755 | 2025-03-30 04:19:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de68e976-d6cd-3ded-a996-5c146ca2438e | -30.46713 | -56.38457 | 2025-03-30 04:19:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 068cd204-2861-31a4-9a03-3f6ecb1748a2 | -20.17141 | -49.6824 | 2025-03-30 04:19:00 | NPP-375D | PONTES GESTAL | SÃO PAULO | Brasil | 3540309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cd51269b-5585-3e33-9431-a3276adf3037 | -20.37653 | -45.60271 | 2025-03-30 04:19:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1e6172e-0fe1-3f08-ac27-63a3a03459e6 | -30.46484 | -56.38586 | 2025-03-30 04:19:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 851569e3-2e40-333a-8df2-89bb62d4214d | 0.83122 | -60.59601 | 2025-03-30 04:34:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f0a0341-c0d9-3ae7-b864-0747d9f40a45 | 2.28113 | -61.23502 | 2025-03-30 04:34:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 840f9a22-f47a-3955-9fe5-0ea805a1db31 | 1.12446 | -60.52467 | 2025-03-30 04:34:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 332c5b2e-6e7e-3f24-b905-9225dafabe48 | 2.08226 | -61.26693 | 2025-03-30 04:34:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c7ef02e-7689-3cab-acdd-c0e798936ad5 | 1.13008 | -60.52614 | 2025-03-30 04:34:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09da13a5-dc51-3c46-adf8-9744b70ada35 | 1.12326 | -60.52714 | 2025-03-30 04:34:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56a819c6-3a74-39da-a53c-9128f8557d3e | 2.08119 | -61.25974 | 2025-03-30 04:34:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d4d7032-982c-39e4-8376-232547dd802b | 0.83026 | -60.58976 | 2025-03-30 04:34:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a92b2caa-2d0b-3a2c-ad18-7d5d687030ba | 2.27777 | -61.22958 | 2025-03-30 04:34:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 557f4d86-17fe-3f42-b911-e12da013d9b1 | 1.12541 | -60.5309 | 2025-03-30 04:34:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93da6875-1216-3ae6-b5ec-9663ca5c45e2 | 2.27888 | -61.23674 | 2025-03-30 04:34:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0afeb0e0-6b46-3c22-a163-7cb8780cffa6 | 2.27391 | -61.23603 | 2025-03-30 04:34:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 332f0922-0ee0-3995-9af4-fc92b7de1109 | -5.7919 | -43.6197 | 2025-03-30 04:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d934042a-627e-3cd6-8bb6-b8a3fb360019 | -5.79606 | -43.62031 | 2025-03-30 04:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbc8259a-a7bd-34e8-af32-7a81d6a9fbc5 | -15.56827 | -47.85654 | 2025-03-30 04:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1d958f5-6498-3fdc-af06-077216bd5740 | -12.37919 | -38.89672 | 2025-03-30 04:38:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f2a253d2-4d73-3c2b-ac5b-b4bcd87f7c36 | -15.07724 | -48.94364 | 2025-03-30 04:38:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8002231d-b10c-314f-937d-7e2aae4f7ace | -12.38911 | -38.89952 | 2025-03-30 04:38:00 | NOAA-20 | SÃO GONÇALO DOS CAMPOS | BAHIA | Brasil | 2929305 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dc43814a-35aa-35f8-b201-75f81870208a | -12.6132 | -52.11197 | 2025-03-30 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e832d759-ab50-3d62-938b-dbd85078edd3 | -12.61079 | -52.23231 | 2025-03-30 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 289df563-bdd8-3477-ace9-d1b5d0a8df6b | -12.60741 | -52.23174 | 2025-03-30 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b4f5cd1-4c09-3051-8b4e-9aa472f71789 | -10.3486 | -38.48393 | 2025-03-30 04:38:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5229d140-5a28-3d2b-becf-fcc5e3fa60a4 | -13.96336 | -41.48978 | 2025-03-30 04:38:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 82e6ed2d-8066-32cf-9f7b-26897d310004 | -13.95796 | -41.48901 | 2025-03-30 04:38:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f3fdc73f-fa23-358e-ba9b-467791de3bef | -12.38546 | -38.89738 | 2025-03-30 04:38:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| e39720ac-abe9-3da4-948c-3c391aece06a | -12.61261 | -52.11562 | 2025-03-30 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcc77166-6ae2-3d8c-93af-23be14abc7cd | -12.61201 | -52.11927 | 2025-03-30 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c3b36d7-d7b8-35ef-99ae-c17e27e3fd41 | -12.38341 | -38.89373 | 2025-03-30 04:38:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| f2d3a47d-6491-3747-a185-b99f817136ad | -12.38285 | -38.89874 | 2025-03-30 04:38:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| ccec9f29-3f03-3e29-8ecc-7004ced8f8bb | -12.61141 | -52.12293 | 2025-03-30 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6da2ff9-2f5a-3705-a455-a3b94a2c4a8d | -10.34918 | -38.47912 | 2025-03-30 04:38:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eeb9fded-aa0f-3389-9637-91e2a47f4ecc | -12.38605 | -38.89242 | 2025-03-30 04:38:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c8c9df76-ff81-3470-8c75-85d7e3162dde | -22.53848 | -48.81115 | 2025-03-30 04:40:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d48bdb6a-d774-3aff-b299-c581eded4b6d | -20.47828 | -53.67463 | 2025-03-30 04:40:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08602b60-da16-35f0-b981-6ce4bd73e6e8 | -17.17253 | -42.83521 | 2025-03-30 04:40:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0182d3c-ba76-3745-aa52-da8131472571 | -17.7771 | -42.80972 | 2025-03-30 04:40:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7d045fd-956f-3932-a2ac-bcc36f8b7eaf | -20.17379 | -49.6811 | 2025-03-30 04:40:00 | NOAA-20 | PONTES GESTAL | SÃO PAULO | Brasil | 3540309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 319e14c7-f9ab-37a6-bb0d-1531bb794d6c | -18.27118 | -46.56639 | 2025-03-30 04:40:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5466889-9f60-3bbf-b3ec-b1e1029fb5c8 | -20.20345 | -55.26877 | 2025-03-30 04:40:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0710fb9-d74e-320d-9f1d-eb87c452e88a | -17.68829 | -48.63792 | 2025-03-30 04:40:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7097d191-4ccf-3734-98db-8c59f41ed1bb | -20.56502 | -55.08727 | 2025-03-30 04:40:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f805cd45-06c0-3b65-bf81-0126bf4d98bf | -21.19519 | -44.93764 | 2025-03-30 04:40:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 966ae837-1b60-3309-b722-3827a63d8798 | -22.16216 | -51.34665 | 2025-03-30 04:40:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8903be91-b83b-3f68-9e89-a7b06010826c | -23.59129 | -47.43789 | 2025-03-30 04:40:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 27930c4c-276d-3ffb-86d7-40b7c5d010fc | -19.96898 | -44.21669 | 2025-03-30 04:40:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f3320bff-fcf5-382e-80a2-8eb6968f44ef | -18.27069 | -46.57016 | 2025-03-30 04:40:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bd1304c-646b-3489-8031-7fb9f504e7c6 | -20.20416 | -55.26464 | 2025-03-30 04:40:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a9cd72b-1762-3ca5-925d-762f3027c675 | -17.77744 | -42.80652 | 2025-03-30 04:40:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09cdd552-0e3d-3393-9771-796bcdb09d9f | -29.96459 | -51.67772 | 2025-03-30 04:44:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| fa323193-d8bf-3666-9ff1-32bfd6a0d338 | -30.58913 | -51.56511 | 2025-03-30 04:44:00 | NOAA-20 | SENTINELA DO SUL | RIO GRANDE DO SUL | Brasil | 4320354 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 12a67ff9-3964-3770-96a1-c0727a26a110 | -30.46621 | -56.38207 | 2025-03-30 04:44:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 5b39ff27-26a8-3910-b5df-31f567eb3eed | -30.46552 | -56.38616 | 2025-03-30 04:44:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| d6061a2a-5cce-3442-937d-66edf871b31d | -12.38349 | -38.89396 | 2025-03-30 05:01:00 | AQUA_M-M | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 44.1 |
| c9148415-662c-3995-b92e-deecf82de149 | -12.38485 | -38.88497 | 2025-03-30 05:01:00 | AQUA_M-M | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 6ef55c78-cef2-3bc4-84c4-330859bb363a | -12.39231 | -38.89532 | 2025-03-30 05:01:00 | AQUA_M-M | SÃO GONÇALO DOS CAMPOS | BAHIA | Brasil | 2929305 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| b727e072-dbf1-3af7-8a5e-7d520699328e | 2.9059 | -60.69353 | 2025-03-30 05:25:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| df222c02-5bca-304e-9732-b4cc19f1841f | 3.23983 | -60.15474 | 2025-03-30 05:25:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cdffba5-2569-307c-b0c3-3906f64e9411 | 2.94916 | -60.18563 | 2025-03-30 05:25:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 792c1974-faac-3fec-b0a5-f19ba32298f1 | 3.2393 | -60.1513 | 2025-03-30 05:25:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51ddc8d1-6afd-3934-a981-084fcd7e0c0c | 4.27628 | -61.32606 | 2025-03-30 05:25:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 473e2d39-4198-3b81-91fb-f2d9e2b2e847 | 4.27966 | -61.32554 | 2025-03-30 05:25:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
