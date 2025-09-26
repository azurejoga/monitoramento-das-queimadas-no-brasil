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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e708d549-29bb-34be-8926-5d7c6bdfcae2 | -5.63025 | -43.9263 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9eddf95a-2590-3ef4-9d18-b4915d4ecaae | -9.70584 | -48.948 | 2025-09-26 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77e48959-e6c9-3c45-b22e-42483dec316b | -6.95851 | -43.2407 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b0fd4f20-5ea3-3dea-8889-390464498101 | -9.6895 | -48.94175 | 2025-09-26 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85b5da08-b46a-3dff-9d6e-2500bf390e2a | -6.26078 | -42.48323 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 34ef7631-335b-3004-a494-79ecd70a0291 | -10.58433 | -46.28343 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1daababe-0ef0-3966-9b3c-6a3c8b29eecc | -7.31906 | -45.76624 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 593eae55-adbb-39ae-8df9-b214bfd575a0 | -8.14007 | -44.46641 | 2025-09-26 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e06deec3-f200-3e90-bded-e4587aedd3ac | -5.62969 | -43.93002 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ea4c741-38a5-309b-942a-b5d397328550 | -7.31667 | -45.75653 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7c9c757-5a92-3667-8130-7da7e64c31fa | -4.8179 | -45.64421 | 2025-09-26 04:42:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32e6ee7c-aaba-3040-a428-8d425c74dc64 | -6.61106 | -42.92738 | 2025-09-26 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed4a082b-fea3-38aa-a604-aa4752232d13 | -10.1184 | -45.30931 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9645988b-748d-397d-bbd2-929676354ce0 | -3.80998 | -52.08659 | 2025-09-26 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7a53080-9d3d-373e-b357-8e37025392a2 | -5.4587 | -43.0717 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f65dbdb0-2525-3953-ba65-ecdcbe9db48a | -5.7346 | -42.6374 | 2025-09-26 04:42:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ed254613-f8b7-3df3-a2e8-dfd87d265987 | -10.10177 | -45.3103 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7041ac0c-9939-34ee-a224-4d5cfde7f2d5 | -7.10251 | -44.48585 | 2025-09-26 04:42:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98c729bf-3973-3163-8a02-f56c551da475 | -5.24401 | -43.06961 | 2025-09-26 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6fd24e4-d52c-3c72-989e-f16ff4ac7119 | -10.00311 | -44.17903 | 2025-09-26 04:42:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9ee4fee-d0d1-3b6d-9946-e6ff219f4289 | -10.41 | -46.1735 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d91145b9-108f-37ce-b4bf-09f0dc96d306 | -7.68605 | -45.98873 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 666eb1e3-2909-3268-b396-0d81feb2ac13 | -9.11757 | -48.52966 | 2025-09-26 04:42:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65710086-8db6-3c52-83cc-06be04d7a1a7 | -9.61916 | -48.60211 | 2025-09-26 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 306a5705-bd01-36d6-8664-b721ce8bd48f | -3.68366 | -52.38846 | 2025-09-26 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0130c612-b877-38bd-9e69-d540561be9f0 | -7.6653 | -45.99932 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4a28287a-b78a-3a21-998c-c0162458c07d | -10.41068 | -46.16874 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff313116-4095-390b-9a55-6aa583b5d746 | -3.68435 | -52.38407 | 2025-09-26 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f40c0f88-a38f-34fa-b286-759f792af978 | -9.97993 | -49.25251 | 2025-09-26 04:42:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bcad189-3410-3773-98b4-27970f04059f | -4.74422 | -43.61054 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a331fb05-ac74-3d93-a930-57bcbb2bc689 | -5.34183 | -43.19914 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a294486-3c2c-3e18-ad1e-7262a6917ca7 | -5.46355 | -43.06726 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 18e14a98-bac3-3f26-b93a-5e906cad8d7c | -7.79368 | -55.01979 | 2025-09-26 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6126981d-ae4e-3ae7-8811-976e718647ec | -9.75462 | -45.95047 | 2025-09-26 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f280dd8a-15bb-34ed-8532-3dfa78fdc38a | -5.64216 | -43.93163 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0395264b-3e10-3091-b00a-f8720fc94b72 | -6.42298 | -43.07952 | 2025-09-26 04:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 266b9c0a-bb7e-310a-9702-f156ba79d1e5 | -7.31476 | -45.76783 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66b000b2-10c0-3539-85ae-6fab48db30b7 | -7.09895 | -44.48164 | 2025-09-26 04:42:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de90dfe0-6b83-3704-bfd6-8a97b429dfc0 | -8.44695 | -46.84449 | 2025-09-26 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 355f920c-2f6f-3865-a371-029bcfa16ed3 | -3.43747 | -51.61891 | 2025-09-26 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e887082-8075-3904-81d3-10446de85768 | -7.31298 | -45.75351 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 756f4b0f-1e16-3133-bdc5-4aeec4d02408 | -8.19432 | -46.38452 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9304d711-1f7f-3948-b151-fe22df4870d2 | -7.31543 | -45.76324 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98d0ba2c-35d8-3f8b-9bb2-c0fa7dafa1f3 | -5.63082 | -43.92255 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a08a59d-2724-3e2e-a4d5-95a93c786a47 | -4.50761 | -50.79921 | 2025-09-26 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 078cc8c9-4ebd-372f-afd5-d07d4c49a949 | -5.30089 | -42.76905 | 2025-09-26 04:42:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71e187b7-a19b-3eba-bad9-8107ca7b3d1e | -6.7549 | -44.71099 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7309831c-35d8-3385-bf1e-99c6e767f6e6 | -9.88579 | -45.737 | 2025-09-26 04:42:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07f4e7c3-8673-3361-bdd5-2f9fe6f49dc6 | -7.31609 | -45.75866 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19011d1e-e594-337d-9c1f-6750dd15857b | -6.25624 | -46.12011 | 2025-09-26 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00a1b8d7-f3f0-38d8-9c1c-f9a78620d789 | -5.7925 | -42.81246 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 869c91a5-66a6-3baf-aefc-1fd77c29866f | -5.37903 | -42.292 | 2025-09-26 04:42:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e00f6e13-3d58-3202-bcc1-657fd48d2cdc | -7.31854 | -45.76838 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b8b341c-25f8-3a86-810a-889cb1890518 | -7.67961 | -46.00612 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a7958ac-8560-3167-8d67-ef69418f388c | -4.56768 | -49.4115 | 2025-09-26 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91b5582b-64e2-344b-921d-b9d6456112f9 | -5.74231 | -44.98168 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| f8f4be65-d96a-3aa5-8029-baeea094fc3c | -7.81359 | -46.89983 | 2025-09-26 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b74abb8f-2599-3d9c-b332-02cf7afad2cd | -5.74129 | -44.96184 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 94fb9c2f-3112-3fbc-9ab2-20266f928873 | -5.63329 | -43.93426 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ca76ceff-8a95-3e36-a776-cb65087b9bad | -9.23985 | -44.26451 | 2025-09-26 04:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c734fa8-8875-3648-a18c-320adb61116e | -7.63599 | -45.99029 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 487608cd-ee5a-3024-a490-e52342a4cb01 | -5.73596 | -44.97096 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 61e88396-7f15-3660-a0e3-9aa4144dc057 | -4.66797 | -48.15565 | 2025-09-26 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fef3903-a1a2-38b4-aff8-6e3695bce153 | -10.28848 | -45.22181 | 2025-09-26 04:42:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0683f335-66c2-3602-b934-9ddd90e4775d | -10.10225 | -45.30686 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 90745012-b7e0-3f8f-81cd-117dea394df5 | -6.71682 | -42.746 | 2025-09-26 04:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d5c3ff51-7a05-3d96-a76c-09a54bcd90c9 | -10.39736 | -46.15195 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1a95f67-9bae-3d68-9d23-a0c7bfe4ed6d | -9.10906 | -48.89885 | 2025-09-26 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62269f0f-4a1a-31eb-82fc-165772541b70 | -3.83274 | -50.97744 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78741693-d3b8-387e-ab04-fb35a5ed0c87 | -9.85396 | -49.16664 | 2025-09-26 04:42:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bfe1800-4b8a-33d2-9206-a25756775cd1 | -3.8175 | -50.7953 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c8c7e734-62c7-3213-8838-7861474c4ad8 | -6.13124 | -43.45372 | 2025-09-26 04:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e19eae5d-5281-3adc-a7ea-e7fdd05b529f | -10.0224 | -49.13416 | 2025-09-26 04:42:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50e4b071-6975-35ca-9eb5-e40b0fc4e774 | -7.3115 | -45.76511 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad31ca02-1e45-311c-8411-8e5b2d015f0c | -7.30772 | -45.76451 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f07d3cf0-fb41-31fc-938f-e480c2c5a3d0 | -5.75122 | -42.55647 | 2025-09-26 04:42:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 84867adc-1f41-3d9f-a23c-99069a7c5e8d | -10.40506 | -46.15305 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd606210-6ad8-34f2-a65e-27eff0b51c66 | -4.48811 | -47.68073 | 2025-09-26 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59b4ef13-56e1-3ed3-840a-28b2328ffd27 | -5.73771 | -44.9859 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a863ab98-b9e9-3b36-9074-a49779c2f376 | -8.44943 | -46.84657 | 2025-09-26 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 728cce5d-2b67-3596-8de1-b112bf799b90 | -9.87125 | -48.87339 | 2025-09-26 04:42:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21c4cc49-d5af-3dfb-801c-775069944878 | -3.82928 | -50.97689 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c8e77e5-2398-39a8-b7d0-1ba0b3a858d2 | -5.73525 | -44.97577 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| ffcd3bec-c1f6-3f34-aaba-e01d3b84221a | -8.1355 | -42.38085 | 2025-09-26 04:42:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2db9e565-d0ec-399b-b239-2f492b8321d0 | -9.10961 | -48.89524 | 2025-09-26 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fce50aa6-3efa-3f0d-bd2e-36da1f8c2e0c | -9.47253 | -48.23339 | 2025-09-26 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f18621c0-93ad-3d33-8da9-70591a857b3a | -9.67668 | -46.02635 | 2025-09-26 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34a594c9-8e75-3986-b628-2c7630af5898 | -3.85126 | -50.97264 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b653e37-72ac-33a8-9990-b072c3f07516 | -10.58816 | -46.28399 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0b5f1fe-efe4-3992-bdf5-48813972b0c9 | -5.64273 | -43.9279 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2242e497-1c3b-3851-938a-a9b50d8ef74e | -8.08092 | -55.22253 | 2025-09-26 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7372224-e7cf-3610-90ed-2e56de17ef49 | -5.92362 | -43.80982 | 2025-09-26 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8150540f-aa48-3ab7-9eb8-441de019ae26 | -7.79755 | -46.01707 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7cdfb04b-9637-3541-bc2b-3d916969f50c | -9.86985 | -48.8773 | 2025-09-26 04:42:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09d41743-ea59-389b-afd6-cfa6506907ef | -8.73261 | -47.06688 | 2025-09-26 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee771d64-36f0-3ff9-a914-847f3460cb39 | -9.52297 | -43.07995 | 2025-09-26 04:42:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c29b6afa-d086-389b-a709-4c0804de07b9 | -7.6404 | -45.98634 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b066ddb-249e-349c-801f-cbc02c021ca0 | -10.40415 | -46.18704 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e20afc61-44e4-38f0-9d1e-47e8f0c66223 | -8.79118 | -43.06173 | 2025-09-26 04:42:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9ba48283-b3dd-3d1f-99cf-07c30880523c | -7.6984 | -47.80474 | 2025-09-26 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README31.md)
