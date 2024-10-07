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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c4e8b4c-b2ac-3c5a-9995-2a234750bc6d | -21.5698 | -47.746 | 2024-10-07 03:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 135.7 |
| d9b2dddb-5735-3647-abb2-03d747b020fb | -21.5705 | -47.7223 | 2024-10-07 03:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d07020ce-eac3-3ec9-b934-7942c5920cf6 | -21.5906 | -47.7409 | 2024-10-07 03:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 4a6a213a-c30f-3295-96df-3aeefa458894 | -21.5913 | -47.7172 | 2024-10-07 03:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0c7dfed4-4920-3221-9415-d075872ce94d | -21.605 | -47.9485 | 2024-10-07 03:37:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 66.5 |
| cf5f0da9-0ac4-37f6-a7db-e9d10a3d159d | -21.6114 | -47.7357 | 2024-10-07 03:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 49eac945-9489-3d5c-bfd9-34fd44389b73 | -21.6121 | -47.7121 | 2024-10-07 03:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e8ec5169-4eaa-37e2-966a-e0b3a9c2db15 | -21.5691 | -47.7696 | 2024-10-07 03:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 66.0 |
| fbac5aca-266e-3bcf-a4d8-2ff3986ec4d0 | -14.61765 | -41.14203 | 2024-10-07 03:38:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc81b223-d6dd-37e5-bfe0-6f2993459098 | -13.83728 | -44.63639 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1a781524-e05f-3af4-93d8-3a6f3ae67b53 | -16.44025 | -43.46384 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1df1fc41-ca67-3dd8-b6a6-0faec7e6fd31 | -16.43954 | -43.4666 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4219825a-6aee-3fac-b18d-11a8fb2f2aba | -16.43921 | -43.46909 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87942dc6-dc54-3f08-b8f4-a63685d37a7d | -16.35009 | -43.69874 | 2024-10-07 03:38:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34b32c74-3046-3780-a021-2885be568d4a | -17.5627 | -43.71941 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f751e6a-421e-359d-bd9e-6d8c16d31c52 | -17.56172 | -43.72445 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a6e1604e-cdfe-332d-99b4-d2947c865187 | -18.6277 | -41.51026 | 2024-10-07 03:38:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2e901c23-fdbc-3f13-bbb3-890667c0678b | -18.62454 | -41.5048 | 2024-10-07 03:38:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 007a6961-eb16-3ce4-8433-2fdaff63d091 | -18.60778 | -41.50542 | 2024-10-07 03:38:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ce97e068-d508-32f6-a47e-89efaefe5459 | -20.19716 | -41.83253 | 2024-10-07 03:38:00 | NPP-375D | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 76cac9cf-9cac-3c3c-a70e-663ae574a8ee | -19.65025 | -41.48725 | 2024-10-07 03:38:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e6ce76ba-ac6e-3db9-b6f2-857bae9c323a | -19.64807 | -41.48806 | 2024-10-07 03:38:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ce0dc61b-a740-3c80-a43b-145e80206247 | -19.64633 | -41.48635 | 2024-10-07 03:38:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 570ecd83-bde5-3b74-a08e-da9299169aa7 | -21.54425 | -42.20311 | 2024-10-07 03:38:00 | NPP-375D | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3be81af7-f61b-3051-bc88-7ec417271814 | -21.54026 | -42.2023 | 2024-10-07 03:38:00 | NPP-375D | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d443930e-8b3a-3cbf-be98-186686ef5f14 | -21.53627 | -42.20152 | 2024-10-07 03:38:00 | NPP-375D | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7196cbc1-4204-3e6c-96b4-78304a392868 | -14.61838 | -41.1381 | 2024-10-07 03:38:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 822a1813-d670-3db3-a2e7-fb95fc7282b1 | -18.03741 | -42.07135 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7815a9d8-be49-34c6-bb01-dd71696bd0d9 | -18.03326 | -42.07028 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b5bb22d2-6473-3f08-a283-f5f5704934fc | -18.02759 | -42.07718 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 99b593a9-ef46-3f74-804b-9779ce8c9fe1 | -18.02343 | -42.07615 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6423b3b2-d8af-3250-908c-ca7f3ca968e0 | -18.02265 | -42.08022 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f23fa29a-e12a-3cfe-a14a-75cff27e0b45 | -18.01375 | -42.12668 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4a68ee17-b6e1-3e35-8a2b-238a5b16295e | -18.01117 | -42.11737 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8ac30f5d-fd20-300a-8a68-57efdab8cdbf | -18.01091 | -42.16442 | 2024-10-07 03:38:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c4bc9908-9591-3daf-a793-1b1bbbcfe24e | -18.01037 | -42.12153 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3b7b34e4-1d5e-3ff5-bbb6-66d644d40435 | -18.0096 | -42.12552 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 1e0dbb19-62be-3247-a84e-6557435828ee | -18.00753 | -42.11821 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5f7a1eb8-f8d3-33a2-8b99-ca9efc00914a | -18.0068 | -42.12219 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 14131043-b721-3fb6-8113-a561bbe3ac3d | -18.00622 | -42.12035 | 2024-10-07 03:38:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c781c3dd-8a61-379a-8909-272a6b64ac30 | -17.83886 | -42.22778 | 2024-10-07 03:38:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 161891ce-c0ee-3033-8951-9dbc49720035 | -18.63022 | -42.06002 | 2024-10-07 03:38:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1209c5f4-d662-3b2e-b096-b47cbd2d2672 | -18.47022 | -42.42654 | 2024-10-07 03:38:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5bac4586-cd90-360d-89e4-a700059405e4 | -18.46944 | -42.4307 | 2024-10-07 03:38:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0c503103-336c-3fe0-aeae-f54e7ba24d3c | -18.46865 | -42.43493 | 2024-10-07 03:38:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9fc1c02c-b78c-3d9e-a659-1f314b8f7919 | -18.46786 | -42.4391 | 2024-10-07 03:38:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4e8b6ac0-094d-3fd0-8dcb-30c41c5cf630 | -18.46749 | -42.41759 | 2024-10-07 03:38:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6421b1b1-ac59-3843-a426-7ea4371385a8 | -18.46671 | -42.4217 | 2024-10-07 03:38:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 74ea10e2-78ae-32e6-adc5-73cbf0e37643 | -18.46593 | -42.42585 | 2024-10-07 03:38:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d2d29008-a3c7-30d5-a5da-433af708359b | -18.18866 | -43.00079 | 2024-10-07 03:38:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 05e68410-0c2a-3c7d-875f-b4f879114636 | -18.18418 | -43.00011 | 2024-10-07 03:38:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 887d511a-3f54-30f2-859a-3d3ca798cd1c | -19.31123 | -42.57141 | 2024-10-07 03:38:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| df77f039-d48c-336f-89b6-df99d0e2e86b | -19.31057 | -42.57487 | 2024-10-07 03:38:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a75b8120-c581-310d-884d-6a7dd8b497a5 | -13.83469 | -44.62106 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4af8a241-d8a6-3e41-ba98-5a4b0e1b9b3b | -19.3069 | -42.57106 | 2024-10-07 03:38:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| bf3c65d7-1f5e-3580-8b73-f116e02772fc | -19.28913 | -42.57204 | 2024-10-07 03:38:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 74da907b-9518-3a9c-a1f5-c30c97c4fe74 | -19.28838 | -42.57595 | 2024-10-07 03:38:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d313dfd6-3dc6-355e-a630-b1c1337b10f2 | -19.28488 | -42.57125 | 2024-10-07 03:38:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ca12bbb2-24de-3045-9cb1-8136fd1245c9 | -19.28411 | -42.57526 | 2024-10-07 03:38:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 2d385ecb-d676-320d-b8b6-7e45b20ec8cd | -19.28336 | -42.57921 | 2024-10-07 03:38:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e511c492-6d0a-3338-9ed2-5c453ba49f18 | -19.20229 | -42.52806 | 2024-10-07 03:38:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 429f9c3b-6701-3b17-9d7a-19c8bda25c89 | -19.20141 | -42.53278 | 2024-10-07 03:38:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 303cbe0b-1967-3060-8c23-db0356246e7d | -19.19805 | -42.5273 | 2024-10-07 03:38:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 87ba4efe-29a2-33be-bd92-fa67e6cc3884 | -19.13743 | -42.72906 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| baf29b64-2f62-34f1-bb68-136f3cd98b94 | -19.13654 | -42.73368 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 34a921f3-b8d8-3522-9210-52140f8f1472 | -19.13565 | -42.73832 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3c632a2f-0dbf-3877-90fd-b0cc9078d692 | -19.13309 | -42.72842 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 226e96f4-dc59-3a87-b6ca-b8a6fb034a42 | -19.13238 | -42.75533 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c16f4f1f-8a78-3d95-938f-655ab4d32b5e | -19.13224 | -42.73285 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d9fa7c2e-f9a8-381c-ab34-3c3ec02f884b | -19.13139 | -42.73727 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e555e413-5626-36fe-b12e-1fcf86051390 | -19.13058 | -42.7415 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6ef6ff4b-5037-3c8f-8779-b679b53bf60c | -19.12793 | -42.73211 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 297857e6-0fad-3dda-bc41-0fb00bf04f7b | -19.12711 | -42.73636 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 992d5789-bd85-3ecd-8d9b-35ae0790e0af | -19.1263 | -42.74051 | 2024-10-07 03:38:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7caccc6e-509f-38f7-8a42-fc7aedbb2fa6 | -19.06829 | -42.54477 | 2024-10-07 03:38:00 | NPP-375D | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30efdd7b-b49a-30fb-96c6-c242ca37d1f2 | -19.06616 | -42.18914 | 2024-10-07 03:38:00 | NPP-375D | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b6c06ad7-6311-3cbc-98cd-db3d51cfec43 | -18.91035 | -41.98307 | 2024-10-07 03:38:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 037ccc13-17db-389f-a606-8778e4927d83 | -19.27494 | -42.85727 | 2024-10-07 03:38:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52fcc30d-5ea6-3ed8-a84f-bd86998352a8 | -18.8638 | -42.904 | 2024-10-07 03:38:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d96545a8-b067-373f-b13b-489cdfce6d3d | -18.8604 | -42.89818 | 2024-10-07 03:38:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 67ceba96-7a52-366e-94d9-973d362c7052 | -18.85952 | -42.90269 | 2024-10-07 03:38:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bae20eda-23ad-3531-a75b-4f947507641c | -20.86602 | -43.27088 | 2024-10-07 03:38:00 | NPP-375D | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b91d26c6-305d-3c5e-a21e-714c018891bf | -13.83424 | -44.63313 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 672e08a6-af6e-3fe6-88f1-5464633366a8 | -19.66284 | -43.19343 | 2024-10-07 03:38:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f4d74d27-de65-323d-bff4-3cf72fb3921e | -19.97919 | -42.46105 | 2024-10-07 03:38:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 80a73149-94fe-3d30-99e6-98898fc5e8d5 | -19.97582 | -42.45599 | 2024-10-07 03:38:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5faaa11b-e242-3ba2-851a-cc59420c5bd8 | -19.97504 | -42.46012 | 2024-10-07 03:38:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 77a01ece-1717-38a4-b99f-37bb7dec2c4c | -19.97167 | -42.45513 | 2024-10-07 03:38:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| eb848a0d-1319-36fc-9d86-b86fdb79b9eb | -19.9709 | -42.45921 | 2024-10-07 03:38:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 40dd25cd-a946-319a-be52-4aa0790521d9 | -19.96753 | -42.4542 | 2024-10-07 03:38:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 66691ced-450b-3b06-9321-4c8a2948b8a6 | -19.96675 | -42.45827 | 2024-10-07 03:38:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c28685f9-e519-3470-812a-6cb13f4ad8a4 | -19.96184 | -42.46142 | 2024-10-07 03:38:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 07b5ba5b-1f53-3102-8941-f24b7a8c72cc | -19.96107 | -42.46547 | 2024-10-07 03:38:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 130d071a-8b64-3deb-a0ff-6aa4aac5196c | -19.84765 | -42.40052 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e0b1a3e7-f7d6-388a-953f-558851411fc0 | -19.84762 | -42.37804 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e276bd6e-e91c-3f7d-9f4b-20761d40c6ca | -19.84686 | -42.40464 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 870eaf72-f796-34bd-8dc9-640cb7dae0a2 | -19.84677 | -42.38253 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| da17794a-98be-38ce-a0eb-e55255e9387a | -19.84608 | -42.40878 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0c5ff187-c742-3538-a846-9cad4fb326a0 | -19.84349 | -42.37712 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 3fe5e8dc-b571-3069-a59e-86483f73a0cd | -19.84262 | -42.38171 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |


[Clique aqui para ver as próximas entradas](README45.md)
