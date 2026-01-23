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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c605df91-18a4-3671-9c7d-742a774c43d2 | -2.94829 | -39.90865 | 2026-01-23 04:12:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 16fa9cb5-3aa4-3e4a-a193-ff7a50185bf9 | -5.44767 | -35.61044 | 2026-01-23 04:12:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd15dee5-9c12-32e0-b66c-8068bdf3d47a | -5.03205 | -38.32454 | 2026-01-23 04:12:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de484955-359d-3734-8e58-28f6edb49542 | -5.61852 | -39.43985 | 2026-01-23 04:12:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4bad079-1dd4-3d74-981a-8ac2ce3cb937 | -5.31 | -45.17055 | 2026-01-23 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89d4188d-96a9-37fa-9e90-6e4b3922aa02 | -2.90485 | -41.82417 | 2026-01-23 04:12:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d96b193-b609-3995-bd7a-00afdd22025b | -4.77545 | -37.81479 | 2026-01-23 04:12:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 010f8bf7-896c-3b13-b8fd-91f9c39e9ffe | -3.3716 | -40.63512 | 2026-01-23 04:12:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9cdf1fa5-3ddf-3116-8823-a5168d34fdbf | -4.68393 | -38.04542 | 2026-01-23 04:12:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1a4ba531-8798-3bae-9ddc-802c15cb53d6 | -8.39006 | -46.237 | 2026-01-23 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb0a31ee-e2e7-34ab-85b1-b0eeff88fd03 | -5.61843 | -44.84027 | 2026-01-23 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d1e3a54-3870-30c0-8c6f-b9b7e6d4c103 | -6.26243 | -40.61393 | 2026-01-23 04:14:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d14657f-3405-32bd-b6a5-4fcb7a71c319 | -5.62577 | -44.84142 | 2026-01-23 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6b5bffda-8206-3248-adbc-6d49f98434af | -8.1165 | -48.02182 | 2026-01-23 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb47a745-6d6b-3da9-af69-95b45119421c | -8.8153 | -35.7415 | 2026-01-23 04:14:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f789cc5-2a6d-3d34-b906-6d13df997df1 | -10.00287 | -36.35517 | 2026-01-23 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 87de0684-9568-3f42-82ff-90cdea4cf4e9 | -8.12149 | -48.01848 | 2026-01-23 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc2b5c55-1b0a-34b3-8608-9702daed1b58 | -7.34722 | -37.69594 | 2026-01-23 04:14:00 | NPP-375D | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43409e73-bb6a-3799-b5ef-4ed2ebc22b44 | -6.99489 | -42.86681 | 2026-01-23 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fba4fb47-24f7-3b27-bbcc-50c22196d30e | -9.99794 | -36.35875 | 2026-01-23 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 9.3 |
| fbbdc828-d53c-3abb-a8ee-7f8526b2c2c7 | -8.75319 | -36.60562 | 2026-01-23 04:14:00 | NPP-375D | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a6dc76fd-73f6-305e-94ca-41fabf3de92b | -6.74834 | -37.94667 | 2026-01-23 04:14:00 | NPP-375D | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 69e58ba8-bd32-307c-ac7f-e042c53b7739 | -5.62141 | -44.84512 | 2026-01-23 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2db0568f-7753-3648-a078-7a50b7791881 | -7.45476 | -35.1771 | 2026-01-23 04:14:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d16c9636-af09-3c49-8e0b-656d2f41170e | -10.00172 | -36.36353 | 2026-01-23 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 538fd75f-e767-3fc7-85c6-eab9d3d57868 | -5.62715 | -44.83289 | 2026-01-23 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32534895-ea4a-3976-9d51-d11535103329 | -7.52103 | -35.16973 | 2026-01-23 04:14:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7ff55c13-8c73-380f-8349-1a4739082afc | -5.62944 | -44.84199 | 2026-01-23 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dbf0483a-8e39-3ab0-8464-ea9a578302be | -10.35503 | -39.06865 | 2026-01-23 04:14:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f1ef10c2-2e47-394c-b4d1-d52453bd87b7 | -8.15499 | -43.18854 | 2026-01-23 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7cad90be-0c79-30cd-a146-880f7234a3d2 | -7.45481 | -35.179 | 2026-01-23 04:14:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| da866409-efb1-319f-a55f-5b7061ae5d1d | -8.81147 | -35.73637 | 2026-01-23 04:14:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d0428e27-8536-3932-a7e1-87ba64d0f1f0 | -8.15163 | -43.188 | 2026-01-23 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 755c421a-fc1b-3c8b-8f53-e95bf0e9e019 | -10.92965 | -39.48667 | 2026-01-23 04:14:00 | NPP-375D | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 276882b3-ed68-3e55-93f5-b46d57588160 | -8.81593 | -35.73698 | 2026-01-23 04:14:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e7c5d6f4-6775-3ce0-9a3a-60b8d7b1c0c6 | -8.15836 | -43.18908 | 2026-01-23 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ee8dff00-76aa-34d1-893b-e28740fa690e | -9.99736 | -36.36294 | 2026-01-23 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 5.1 |
| bd53ea6e-4ed8-353e-8eff-7cc7167ccaa8 | -6.63927 | -38.45431 | 2026-01-23 04:14:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d02a2990-c064-382c-9bc3-4b3a8e453eb7 | -8.16173 | -43.18962 | 2026-01-23 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a490502f-f8fe-3366-952a-6c8b61370719 | -8.12079 | -48.02256 | 2026-01-23 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49ca9fa9-5c1b-3048-a4d3-134b0b8a13de | -8.38845 | -46.24657 | 2026-01-23 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f23c007c-c654-3408-a6cb-8f9299d9ef88 | -7.45409 | -35.1817 | 2026-01-23 04:14:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d9e5dbcf-feae-3a79-84bf-4d00cceb153a | -10.48662 | -42.50055 | 2026-01-23 04:14:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30d41e2f-91db-3b70-85b0-926d49e5cf04 | -10.48329 | -42.50001 | 2026-01-23 04:14:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e0a057b9-92fa-351c-99de-d8e352e1294a | -8.75335 | -36.60459 | 2026-01-23 04:14:00 | NPP-375D | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d6a5c8a-1ff6-3855-9bb6-e6459ed04c45 | -9.99852 | -36.35456 | 2026-01-23 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 72f7bcf6-6e54-338f-ae79-5071a0ac9f0a | -7.35105 | -37.69656 | 2026-01-23 04:14:00 | NPP-375D | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 79507e12-9650-3f1b-906b-b45c1b4a8c44 | -5.62508 | -44.84569 | 2026-01-23 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| af3fc9dd-d31d-31ee-b3af-371e0d0352f7 | -8.81083 | -35.74093 | 2026-01-23 04:14:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5ee1834c-961e-3e55-bd8b-2d65b116e8b0 | -12.68531 | -39.28343 | 2026-01-23 04:14:00 | NPP-375D | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| badbe69c-b5a7-36b9-8947-76ff79d7fdf0 | -10.9266 | -39.48372 | 2026-01-23 04:14:00 | NPP-375D | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d8ad6ca1-2a5d-3031-9713-cd18c83b6706 | -10.00229 | -36.35935 | 2026-01-23 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3b0ef839-edef-33bb-bdb3-e503e7e2c2fb | -5.6221 | -44.84086 | 2026-01-23 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5f9f1c06-cd73-39a1-ad04-d9af66f60597 | -7.5165 | -35.16896 | 2026-01-23 04:14:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 245560da-d1fc-3532-828f-0e6e7a3f3671 | -19.33018 | -54.02893 | 2026-01-23 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f9ad274-cfdd-3af8-bacc-a2b399fdb608 | -14.31389 | -57.5918 | 2026-01-23 04:16:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e12a7d5-691e-3cd2-a7c4-6239c491cfd4 | -19.32422 | -54.03119 | 2026-01-23 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea4e025e-a00c-3e49-bbff-d8e7954f06a3 | -19.77849 | -50.73625 | 2026-01-23 04:16:00 | NPP-375D | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 540a3365-362c-347d-9562-accb19218b62 | -18.31495 | -54.5801 | 2026-01-23 04:16:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a55103e-97da-3dad-b91a-30c2ae2ed929 | -14.30514 | -57.59806 | 2026-01-23 04:16:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0eeca377-6ab2-3cad-b135-a1dff55739c3 | -14.3122 | -57.59944 | 2026-01-23 04:16:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55b4e94c-18cf-3ae6-a937-e46f386a859f | -18.30951 | -54.57869 | 2026-01-23 04:16:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c3193c7-ce1b-3ae9-a8a6-4487ff422493 | -19.32424 | -54.03125 | 2026-01-23 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0361bd32-e302-3d3e-b9b1-9bfdf6a0bdaf | -19.77816 | -50.73753 | 2026-01-23 04:16:00 | NPP-375D | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d809c6a9-9301-3666-bf3d-311e7fb68f65 | -19.32491 | -54.02788 | 2026-01-23 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdf26e14-271a-3225-91b7-ef5e0c91b6cc | -19.45326 | -53.98525 | 2026-01-23 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f333e3af-6791-3f57-a443-a37503b71212 | -19.33014 | -54.02887 | 2026-01-23 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2d92f75-bc53-316a-a616-abf990219c79 | -14.30899 | -57.59663 | 2026-01-23 04:16:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1bc50d99-d89e-374e-b021-67b38cfe2856 | -19.32495 | -54.02795 | 2026-01-23 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 160aefeb-8531-3c22-aedd-a95721c4e8ab | -19.45839 | -53.98656 | 2026-01-23 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f05a63aa-4678-32a9-9b05-89db1bf94e64 | -19.17227 | -57.54281 | 2026-01-23 04:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e2d1a09c-e8a9-3f9e-913a-55068484c02b | -24.10461 | -51.41571 | 2026-01-23 04:18:00 | NPP-375D | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d0a86d06-e304-302e-9da9-9970c7ae77d5 | -20.34156 | -57.86079 | 2026-01-23 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5d457b1b-94c5-34d1-a78e-461210460bae | -20.34024 | -57.86632 | 2026-01-23 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e1d7ca97-2f4e-3a96-92bd-8928158e489c | -22.60906 | -49.56551 | 2026-01-23 04:18:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c8f98d4-3d29-357f-b984-7b7c984f8e00 | -19.68177 | -56.92695 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a64a7c01-356c-33eb-8a77-d6ae39be6ec2 | -26.78679 | -48.67025 | 2026-01-23 04:18:00 | NPP-375D | PENHA | SANTA CATARINA | Brasil | 4212502 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b6481fae-0565-3d70-adef-57ccdfe5d040 | -23.05466 | -49.06049 | 2026-01-23 04:18:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0d61bb3-de9a-3567-93bd-c9846ca1258e | -20.3479 | -57.86251 | 2026-01-23 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f5af3ac3-11e0-3932-a8c0-ad97b481ebf9 | -19.66894 | -56.87103 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 26533bb1-79a2-3187-b47c-2cbf92550e97 | -21.4348 | -48.78158 | 2026-01-23 04:18:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2882ea7-8451-35c4-ad34-fa0e32dcd91d | -19.67682 | -56.92039 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 00834ee0-850c-3167-a733-eb1e346fc4f6 | -21.5366 | -57.53609 | 2026-01-23 04:18:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 773821cb-02ea-3221-aae3-59dfd30ca929 | -22.61096 | -49.57613 | 2026-01-23 04:18:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 14cdaf5a-9216-37dd-a86e-ec54547b7265 | -19.6872 | -56.87579 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 371a1c0f-186a-3e5e-92ca-63be0950ffaa | -19.17885 | -57.5436 | 2026-01-23 04:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0f2c86ec-df76-3a5e-9490-7d5aacf860a5 | -21.78499 | -56.28392 | 2026-01-23 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24a24f83-1078-306e-9eb6-999e2d074932 | -20.38201 | -57.88957 | 2026-01-23 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6699ad34-7fb6-33d6-a674-ee10a6cf68e3 | -19.68263 | -56.93198 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 13036962-d22d-353c-beb6-363416795fdd | -19.6634 | -56.87419 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 74155e54-4c2b-37f1-a11b-433fbdbdd06e | -22.01975 | -56.33826 | 2026-01-23 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6b70e56-4065-3fe2-8cb2-64a87aedb074 | -19.68605 | -56.88074 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a763ae5e-b4aa-3d20-b34d-65d72315e280 | -20.35926 | -57.87152 | 2026-01-23 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 859d30f7-44c1-3d52-abad-a020b6291136 | -21.77894 | -56.28069 | 2026-01-23 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82fb36ff-c551-3e19-afc1-78a9747ae77f | -19.17802 | -57.54757 | 2026-01-23 04:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 682ae4e3-db53-3fb2-8984-7d162a7c6769 | -19.17141 | -57.54686 | 2026-01-23 04:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6994a86f-348f-3fae-812a-183284802e0a | -21.53561 | -57.54028 | 2026-01-23 04:18:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f4db6f48-c1ca-3b3d-9d29-c513920964d3 | -21.53766 | -57.53163 | 2026-01-23 04:18:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 597cda69-0d86-3e3d-af09-1fb8351d7ff2 | -23.60037 | -48.33728 | 2026-01-23 04:18:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07fb07ae-6b89-393b-9f72-ad37f5b7771d | -19.68375 | -56.92698 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
