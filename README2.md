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
| f48df98c-e5cf-3abc-b7a6-5ffd94293eb1 | -18.1041 | -40.34243 | 2026-04-21 03:49:00 | NOAA-20 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fa446790-af5e-3a20-8d3d-f2ea9d445753 | -25.11151 | -49.42865 | 2026-04-21 03:49:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fdfebb74-7ed6-3a63-b367-cbb60f91e938 | -21.95142 | -48.03431 | 2026-04-21 03:49:00 | NOAA-20 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5d739ad-ea9e-3ee2-b233-4113a6cfc645 | -21.9528 | -48.02791 | 2026-04-21 03:49:00 | NOAA-20 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ea89e3e-9eb7-3dae-a802-f9de0aa3a414 | -17.16819 | -46.83577 | 2026-04-21 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8727ea96-ad2b-3e38-958d-368a0995984e | -25.6373 | -50.41679 | 2026-04-21 03:49:00 | NOAA-20 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 22a5589f-4acc-3698-9477-129635cccbc7 | -25.10642 | -49.4271 | 2026-04-21 03:49:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7de4c2d5-5413-3696-a6d8-97569652660a | -11.90638 | -43.84658 | 2026-04-21 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c9af76b-a331-3cb7-a527-2e8e87a01179 | -11.99917 | -47.77345 | 2026-04-21 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d1f1763-1d23-3973-98b6-484d666de99e | -11.72686 | -44.73909 | 2026-04-21 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1dcaa2a-6c50-3fca-9d77-2bc6bcdc1fea | -11.95586 | -43.3818 | 2026-04-21 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1615661-29eb-327a-a702-7efcc31c64bb | -9.80288 | -37.47482 | 2026-04-21 04:34:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 12f171fc-79dc-35d5-b615-372c0eee2acb | -11.99582 | -47.77292 | 2026-04-21 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10038dcf-6efe-3b79-a93f-770bc625a34f | -12.24384 | -44.19537 | 2026-04-21 04:34:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 035ba42b-4e43-3bf1-be8a-46f7ef3f431f | -11.19272 | -43.56931 | 2026-04-21 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ae8cee6-8695-302d-9ae9-f4ca40b444b5 | -11.95637 | -43.37798 | 2026-04-21 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6220b976-9f90-385c-a086-eba96c578a20 | -11.18915 | -43.56503 | 2026-04-21 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7788732-bbe3-3e48-b13d-01034c17eb3a | -9.80342 | -37.47023 | 2026-04-21 04:34:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 999867f0-0c12-31e9-a10c-e5412d6f5f65 | -9.47107 | -47.80101 | 2026-04-21 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf597d8f-31ec-3959-b395-e62a90730e36 | -9.47053 | -47.80452 | 2026-04-21 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a2caa2f-ee1a-399c-98d3-ed2c86e479f3 | -12.24059 | -44.18964 | 2026-04-21 04:34:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6023c5bb-24ea-304d-a743-a4251319a412 | -12.28049 | -44.61993 | 2026-04-21 04:34:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9974071-c47e-324d-9212-9defb39e7e03 | -9.80655 | -37.47499 | 2026-04-21 04:34:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0072f2c4-4bec-38d0-85af-50580b050ede | -11.87035 | -43.8632 | 2026-04-21 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bafa0951-473f-354b-8a90-405b5c40be15 | -9.80054 | -37.47421 | 2026-04-21 04:34:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 543ae248-33dc-36fe-8a76-f23d7aee8e5a | -12.23986 | -44.19487 | 2026-04-21 04:34:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e2fe06f-a20e-3cb2-8e64-556b851a89e6 | -13.95656 | -45.33923 | 2026-04-21 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed03c560-fb20-393d-9491-73c256c999df | -13.34624 | -43.1997 | 2026-04-21 04:36:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3aa8d2b7-b0af-39b5-9b15-eed87375af72 | -17.16755 | -46.83424 | 2026-04-21 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8c16e461-f10e-3205-a080-80b5db7c429e | -13.95592 | -45.34393 | 2026-04-21 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5e52944-586e-3f78-a62f-1d0f2aa800e5 | -15.13136 | -41.83992 | 2026-04-21 04:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 021bfb21-349c-3fc0-a1ba-c9cd359b1ac0 | -13.58766 | -47.48079 | 2026-04-21 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a64388fb-9120-306c-bbd0-654effa1b945 | -13.95277 | -45.33863 | 2026-04-21 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fe6d5ad-f74b-34eb-b4e2-637f8ce7c23e | -14.55344 | -42.27771 | 2026-04-21 04:36:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2dbba94a-9ba1-3c33-a40b-65e792502982 | -16.42306 | -54.92532 | 2026-04-21 04:36:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce50c5b5-0dc4-34bd-9e99-f0c5647fde7a | -13.95251 | -45.34088 | 2026-04-21 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a76c9856-875a-36e8-a7f1-6b92a23b125f | -21.95309 | -48.03041 | 2026-04-21 04:38:00 | NOAA-21 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0cb65113-ad4a-33e3-af18-6dfb78f26e7e | -21.9561 | -48.03545 | 2026-04-21 04:38:00 | NOAA-21 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3694c4db-62ca-3378-8e73-5ad5a0e01c66 | -21.04042 | -48.55585 | 2026-04-21 04:38:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6ce1c836-4c8b-3cf8-8a26-a0a2f15a4752 | -25.64233 | -50.41393 | 2026-04-21 04:38:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1a3b7c73-275c-3979-a3af-c330d1ec4ab1 | -21.95671 | -48.031 | 2026-04-21 04:38:00 | NOAA-21 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3273a468-b73c-3d48-8d24-be20279ed358 | -21.96032 | -48.03159 | 2026-04-21 04:38:00 | NOAA-21 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cb054451-5a59-30eb-b7c1-1643de2d46ec | -25.10905 | -49.42757 | 2026-04-21 04:38:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6e12e811-d1f6-3c45-a284-02461abe0289 | -23.0367 | -48.43372 | 2026-04-21 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e94e6c1d-f8b4-3064-ad0c-cf032756f5ad | -18.85298 | -48.27467 | 2026-04-21 04:38:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbdf318c-3d9f-3aa4-a52b-348d130fb51f | -25.11082 | -49.38816 | 2026-04-21 04:38:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a7f783c5-a11f-374a-a463-5fd6cf55543c | -23.12298 | -47.69621 | 2026-04-21 04:38:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f2fd0b8e-4fb3-3584-bb27-4391dc30c1bd | -21.37383 | -48.72345 | 2026-04-21 04:38:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bfb4f32-9a0f-3d0f-887a-3778ef87da48 | -24.49793 | -48.96049 | 2026-04-21 04:38:00 | NOAA-21 | APIAÍ | SÃO PAULO | Brasil | 3502705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 618278c6-f45b-3faa-9a92-7a8512fac437 | -23.98002 | -48.13966 | 2026-04-21 04:38:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0bde3565-9a39-3e88-b4b2-b3c9404d21da | -18.85241 | -48.27866 | 2026-04-21 04:38:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bfa61a9-cb08-3ccc-a5c3-9ee1be766a97 | -21.9537 | -48.02594 | 2026-04-21 04:38:00 | NOAA-21 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 049c6aef-ef13-3082-9720-a0cbf567b131 | -23.64798 | -47.99918 | 2026-04-21 04:38:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef71d624-180c-35a6-8b5f-3a544a652036 | -21.37517 | -48.72277 | 2026-04-21 04:38:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfdc6c7b-0a0a-304b-b218-ea2c33f04098 | -23.03815 | -48.43568 | 2026-04-21 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36b9c979-7637-3134-8ea5-ebeac2217877 | -19.84235 | -45.01702 | 2026-04-21 04:38:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a42d360d-1794-3169-8028-fd8b6984cfe5 | -25.64175 | -50.418 | 2026-04-21 04:38:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8ecb9c28-8f5b-3c2c-8394-356fc853b06c | -22.49535 | -47.48559 | 2026-04-21 04:38:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d7668d82-7126-3fc8-bd27-e7e40bc58033 | -21.9573 | -48.02655 | 2026-04-21 04:38:00 | NOAA-21 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 04a6366d-4c2f-3620-8019-5670eb028ffc | -21.96092 | -48.02715 | 2026-04-21 04:38:00 | NOAA-21 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5bb96265-e27e-30a8-9850-787128236b49 | -27.44966 | -48.44576 | 2026-04-21 04:40:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e87cf611-1939-3ad2-b5f7-22ff85252ba0 | -28.34848 | -49.15657 | 2026-04-21 04:40:00 | NOAA-21 | SÃO LUDGERO | SANTA CATARINA | Brasil | 4217006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2c0a58e7-513b-3101-a711-867e496dbab6 | -27.95048 | -50.22131 | 2026-04-21 04:40:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bf3dac93-6d8a-3090-8ab5-470ecaf6ff8c | -27.9499 | -50.22559 | 2026-04-21 04:40:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a10d30bb-fa85-3e7a-aa50-003b11b7c940 | -28.34736 | -49.15793 | 2026-04-21 04:40:00 | NOAA-21 | SÃO LUDGERO | SANTA CATARINA | Brasil | 4217006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e3dd6272-e87b-357a-aeab-1440d0dc7350 | -2.75133 | -54.59238 | 2026-04-21 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10d41e61-d858-3300-bff8-1cbfe3e64096 | 1.94622 | -60.38073 | 2026-04-21 05:04:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 867b47fe-0458-398d-b5e2-2d4809afa964 | -17.16662 | -46.83468 | 2026-04-21 05:08:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1196696c-6804-38e0-974c-293547d4c766 | -13.95382 | -45.33991 | 2026-04-21 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 384b372d-312d-3d4e-bb33-feccf2e4be89 | -13.95333 | -45.34414 | 2026-04-21 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcdb8c16-9a74-3661-853f-1eef52138071 | -12.28006 | -44.62446 | 2026-04-21 05:08:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98e08ebc-3172-3d2d-9da0-a5fca27ff5ad | -12.24456 | -44.19515 | 2026-04-21 05:08:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 947713b6-38db-3a8c-b83a-959924e71e0c | -12.28171 | -44.62107 | 2026-04-21 05:08:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f4a5cf4-3919-3f32-a5f3-2570b554c6c3 | -11.99887 | -47.7765 | 2026-04-21 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7a0e0f9-0d26-3b3b-8d45-08fabb2192f0 | -11.99626 | -47.77346 | 2026-04-21 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6013e8e-d9a4-3047-9625-8c9e4b9fb711 | -12.28062 | -44.61993 | 2026-04-21 05:08:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cae165b1-ea7d-302f-8f10-2a884a6a096d | -12.23834 | -44.19469 | 2026-04-21 05:08:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35b81ada-84e3-35c9-b0bf-f189ce07f86f | -21.37133 | -48.7237 | 2026-04-21 05:10:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f01e0136-aa57-392f-807f-fcdf3420ffc6 | 1.28464 | -60.32419 | 2026-04-21 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69238a1f-0ee1-30ab-8a4c-24cdef7e017e | 1.94838 | -60.37821 | 2026-04-21 05:25:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66e21ec5-eb13-3385-be26-bdaf218f37af | 1.28378 | -60.32779 | 2026-04-21 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dc4c839-f4bc-3e4b-9cff-0a98746e42ee | 1.2852 | -60.32778 | 2026-04-21 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63de3cff-62a5-3238-85e2-930847fbda8f | -9.06471 | -59.86976 | 2026-04-21 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66bbc4fe-cde8-3fbd-8caf-06dcdd1ebd36 | 2.57707 | -60.30045 | 2026-04-21 05:25:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b884cf66-31d1-3037-8be5-bf85d68e26bc | 1.95178 | -60.37769 | 2026-04-21 05:25:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3f60967d-6a4c-3023-a1a2-b2547427a9b9 | -16.41932 | -54.92481 | 2026-04-21 05:27:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bed75b52-f62d-3d5f-8045-94f4542b99be | -13.35722 | -42.60499 | 2026-04-21 11:23:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4def4b8a-af3f-3faa-879b-19d904ff24bf | -11.8338 | -39.17502 | 2026-04-21 11:23:00 | TERRA_M-M | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| f4f82640-4015-3e41-a64e-8a47bb4ddcd8 | -12.5834 | -39.34305 | 2026-04-21 11:23:00 | TERRA_M-M | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0e22d26a-c014-33d0-8f51-6eb2bafced8a | -12.5834 | -39.34304 | 2026-04-21 11:23:00 | TERRA_M-M | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8d2fc3e7-b535-3120-8c51-edc869b9b24a | -13.35722 | -42.60498 | 2026-04-21 11:23:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| db12a7a3-dad4-319d-8979-3730d7a4adb3 | -11.83379 | -39.17503 | 2026-04-21 11:23:00 | TERRA_M-M | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| f9347c56-20f0-3cef-abcb-a546c9bdf3c2 | -13.96296 | -45.34749 | 2026-04-21 11:23:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8b584c9b-1be3-3780-892e-9ac503c49c17 | -13.96297 | -45.34748 | 2026-04-21 11:23:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3908aa89-9988-32e9-812d-fc1756a85714 | -18.64827 | -40.24511 | 2026-04-21 11:25:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| f19ae9d0-d39c-39bd-be91-36397ba85d83 | -18.65712 | -40.24648 | 2026-04-21 11:25:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 11c1c795-d6ee-35e8-9830-d07051fe98da | -18.64827 | -40.24512 | 2026-04-21 11:25:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| e1353b91-e9ec-35cb-9c14-60468ef6ec25 | -18.65713 | -40.24646 | 2026-04-21 11:25:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7e4f8d8c-a428-3c8a-9c82-a1e683cff121 | -13.9564 | -45.3417 | 2026-04-21 15:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |


