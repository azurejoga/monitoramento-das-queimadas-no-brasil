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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c8297cc-8c0f-3969-83ff-41dea45cb25a | -14.0512 | -45.01805 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99785a69-345b-3ad6-b6ed-eb6a7e9820ab | -11.81805 | -44.95966 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14b6f9f4-d52a-35b4-ace4-5a794bf4d09c | -12.82664 | -47.02012 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b38e94b-df22-3396-9cb5-fd00bb352848 | -12.95184 | -46.42118 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c44647e6-145d-350f-9b07-ae0c87e04c9e | -10.98295 | -46.54181 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18145b50-419a-31bb-9513-b0bdc11d3df3 | -13.67327 | -48.0771 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4ac3e282-5f9c-386c-ab61-3878518fd0dc | -10.91243 | -44.79187 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e9d603e-b44d-301f-a208-486b82ad2fe0 | -15.25058 | -56.81035 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d8220e6-3fb8-3a1e-bacb-4b179d5ae15e | -15.75923 | -43.72834 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e67cf208-1bfb-30b5-96b4-174ee11296c9 | -10.57346 | -57.81737 | 2025-10-01 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 076be3f8-b151-3ec1-aacc-7cfc26d46e21 | -13.15244 | -47.40859 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76e1c787-c990-3a99-8c61-a166f84f09ec | -14.00156 | -45.01458 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f817c88-970f-302c-9d12-94a05e1917b4 | -15.78316 | -43.68838 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fa64012-ede4-31f7-b7ef-471690db29a1 | -10.81438 | -46.63787 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2aa77af-135c-3fb5-9e03-9ddf3a833481 | -10.90478 | -46.56172 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fd7a948-6893-3ae1-9064-30e916b40a2e | -16.37514 | -47.05033 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b3e2929-e3ff-3c01-b09a-5f5fe9f6b255 | -16.19521 | -50.00362 | 2025-10-01 04:21:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22850ff0-561f-32ee-9a61-4be0da81c4cd | -11.79641 | -47.5977 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68c872a1-1a5b-3d39-a787-87e9cdbe7830 | -12.9316 | -47.21672 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92632e4e-a131-3653-98db-452d132001ae | -11.49547 | -43.51288 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2808ceb-8698-36f2-8755-8990f513e26e | -14.72139 | -48.15484 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b98adc18-5c56-30bb-aea2-5912e2623f08 | -10.82034 | -45.36516 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44ff3b8c-10b1-3120-92af-a43e29ab9410 | -11.44684 | -43.50552 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74b0ba20-aee0-3d86-a343-62ade3840146 | -14.54537 | -48.24708 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d81a96f-e541-3500-88f0-c92b0e9a0d8b | -14.02966 | -47.96264 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bcd74527-4c9c-300e-ae19-174c0a8aed1f | -15.17006 | -46.42295 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a8c69d4-6da8-3c62-9e37-edb3c232d31f | -14.50591 | -48.44416 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96a8119d-9476-37a2-bb1c-9e9aae58b7af | -13.71449 | -48.65565 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 171795c0-a621-3e74-8e38-cba69acb2856 | -11.38925 | -44.896 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d3e9b19-c534-32e2-927c-e6e9153105ea | -14.34817 | -45.90982 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 90cb090e-6c3a-35c5-ab96-257f278f3312 | -15.16198 | -49.08774 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 91f0608d-a82c-350a-98ec-77ea1db0d1ec | -15.23994 | -48.74776 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e854a559-19ae-3c5a-8712-26a1748911a4 | -14.35098 | -45.9358 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 072f7a9e-f6a0-3a5f-baf9-da9ba3da2ef7 | -10.10765 | -50.31831 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bfbff75-5e7e-368c-82af-e5a00418dd38 | -14.21633 | -46.10358 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70421885-562c-3539-8087-a8f3955f6b1d | -14.76303 | -45.75247 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85ed2188-04a0-30b6-b18f-89879e9f7be0 | -12.1583 | -47.76736 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fa7ffd63-e9d6-3aab-95d0-ace96514e103 | -11.98824 | -47.13078 | 2025-10-01 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ee71968-9c46-39bf-981b-6fc4006a2c84 | -16.4094 | -43.7246 | 2025-10-01 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f1468c2-722b-314c-a139-938eb2e3bfd5 | -12.88987 | -45.19766 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| feeafa9b-e206-3efc-9559-11dc0c211517 | -9.40521 | -54.71843 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5493dd41-806d-35d5-a1cb-5205a324eac9 | -16.2002 | -49.9959 | 2025-10-01 04:21:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2c08c4a8-c52d-3347-a69e-2afabff37f9e | -10.18888 | -52.55652 | 2025-10-01 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d33d1029-10b3-310a-b1cc-1c921ea0513c | -13.72718 | -48.81417 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26f9a75c-362e-3f2b-b7a7-5765350ee405 | -15.39619 | -47.06555 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a584c84-d17f-3e17-bc66-83528fd21f33 | -11.99562 | -47.10625 | 2025-10-01 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0485c7f-578c-3734-8295-615298695015 | -13.64481 | -48.03057 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c09f0ec-0780-3e53-83c0-30a37756bbce | -13.76659 | -48.4053 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71b54a6b-8fe3-31f9-bda0-7589dbeae163 | -15.99291 | -51.19545 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7789dbd7-b477-349d-ac08-3a0e2762138d | -12.39528 | -44.76211 | 2025-10-01 04:21:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88eeba50-7448-35ae-8383-fadaac855be5 | -13.7926 | -47.98286 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 753414a4-7165-39cc-9df7-e9e350153749 | -12.66909 | -46.87763 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b564279-0572-3137-8969-a9ecd7626085 | -15.12764 | -46.45279 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c27f035-9b47-31e7-b539-7c529c05f856 | -14.89768 | -48.13523 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a043c3f6-eb4d-3919-a21d-98253881c98c | -15.24681 | -50.08628 | 2025-10-01 04:21:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7218dcc2-3d52-3da7-88a5-d286e3b93ad9 | -9.42639 | -54.57407 | 2025-10-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 38701403-e14f-3c60-ac09-93247f1b1bc6 | -15.63533 | -46.24983 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57c8870c-f933-388c-ad39-be2e2b1089a2 | -11.38466 | -45.05923 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0399685e-3544-3444-80d3-92a9e82201b3 | -12.78675 | -46.90781 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 651a3efd-98f9-3a4d-9754-6f539e05418c | -17.40638 | -47.15358 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c5d42a03-fc65-3bf8-ad79-8c6d24486c39 | -11.69016 | -45.34963 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ec76348-f784-3057-9583-7f7aece92817 | -11.09404 | -47.71824 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 585b1c5d-8b5b-39b6-9219-1a8e76dea6cd | -13.61255 | -47.27926 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3840e790-002e-3c13-82d6-cecfc9d0900a | -14.96274 | -46.8804 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fc0a7ba-4316-3665-9ac0-6acb12de88a1 | -13.37495 | -47.31656 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8511eb0-21df-3512-9179-40388f04eac6 | -11.59433 | -45.04448 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f43af119-5177-36ac-950f-9f9029f1d777 | -12.88389 | -45.25911 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89977279-5422-31f6-9df5-7f0aa3c81698 | -11.46814 | -45.00296 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c697d4f8-0dec-3941-b41f-0c0e8db856bb | -13.33804 | -47.33632 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae294f76-18cd-3490-b3bb-33dcf48ee8fb | -15.13704 | -46.41761 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23495ccc-b617-3171-8c39-885387357f86 | -14.78964 | -45.7789 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8195adad-f45f-35d8-9e46-bea0b06f6605 | -12.88932 | -45.20125 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7eea2823-ca7a-3f30-b698-cc4fb1ad675f | -12.21155 | -47.8103 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd36bf15-66c7-3d94-ad8d-15157afcf377 | -11.46644 | -44.99182 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e7d38ac-99a1-37bb-a690-1d232dc7bd4e | -13.93644 | -48.09834 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d18ae7c9-ff1c-3d90-927c-e824a8872bf1 | -15.61445 | -46.91181 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 510e312c-3409-3a6b-9730-89be9ff049fc | -12.70657 | -46.89829 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4155df8-1bc1-35c5-9886-80c15c95b610 | -11.96898 | -46.59152 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80cc432d-61f7-317f-baeb-aecdcb0be4d0 | -12.01299 | -46.63486 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 758670de-83d3-3866-bd1c-ab7ed29789c5 | -15.28448 | -56.78398 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40c04e62-e0b2-369c-ab7f-69f8c9ae66b4 | -14.79019 | -45.7753 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f3e4e20-bddc-3010-93bf-dadaba7887f2 | -13.74785 | -48.68928 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8db2c262-e89f-3d58-82e6-dfb324bd118b | -13.97206 | -44.88889 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fcfcef5-77b3-38ee-9977-1a3b1f14a186 | -13.79199 | -47.98661 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef89d23b-02a0-321c-9fd6-c1ed2f810af4 | -13.53924 | -47.26984 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 120d8da7-5baf-326f-b64a-e22f1284d65c | -14.70298 | -46.97184 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac3657dd-9d06-32d6-8c89-602ff5d53034 | -12.77625 | -46.90972 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dea9f8b-2b7c-39f6-8ea8-daf22cb1d1a1 | -10.06293 | -48.19157 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fb90b97-8aa0-3aaf-9384-8c3263acf7ce | -15.25706 | -56.77903 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88c17454-9029-3130-aeb0-c362894784ed | -14.39473 | -46.22328 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d432f06b-5773-339b-8bf7-8581f46825f3 | -11.83524 | -44.95872 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9af62c08-8c4e-3bfe-8988-b63fc0acc700 | -13.36362 | -48.09809 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33e3378a-0856-3287-acc4-6a860493cfba | -10.35449 | -43.73889 | 2025-10-01 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab6dc70b-ead3-3d76-8968-718be24d8fdb | -12.8543 | -47.01737 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7906a39f-b69d-362f-af33-2c8d4776e92a | -11.6076 | -45.04669 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28d83264-6802-35c1-9cec-608710a5fe81 | -14.51944 | -53.12216 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0f6e4fb-a570-3d28-8bd5-d6672e391fa1 | -12.00801 | -46.6449 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2b2a4d6-d5c0-32a6-9427-020a7f291e7f | -9.80335 | -48.97296 | 2025-10-01 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7df1d0d0-4b12-3a07-be41-b4d131d48f22 | -11.37911 | -45.0511 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 312cd5b9-93cf-3f9e-87cd-fcc27c498b62 | -13.91554 | -48.09888 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README53.md)
