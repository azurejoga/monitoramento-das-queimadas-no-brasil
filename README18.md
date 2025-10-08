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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2166e5b-b741-3fc4-b691-4054027fe5aa | -11.19164 | -49.77856 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05b5aa3e-8d59-37ee-964c-d44c0ecf0eea | -3.11161 | -47.79665 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c04a3d78-de41-3393-aedf-fbae0a679783 | -13.22298 | -47.17891 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f21c7a7-af90-3649-be16-1d75985a9a07 | -12.21811 | -44.26147 | 2025-10-08 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bca0b184-06ce-30fe-a5d1-5a797c82ddad | -11.7184 | -44.29666 | 2025-10-08 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfcf3c59-5ad5-3d9d-af13-9bb50b2f84f9 | -2.665 | -47.86632 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 068151c1-0625-3532-bfb2-6ae028f971fd | -8.58455 | -44.33678 | 2025-10-08 03:49:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32c83c9a-fb5a-32a3-9192-af260626f607 | -11.87171 | -45.74506 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6ab005b-46a7-358b-8959-38458a4fa6cf | -11.18541 | -49.77731 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 157c79d3-5112-3353-a689-c7f88fd610d5 | -8.52459 | -46.28362 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1232bf0f-84cb-3216-a701-4c2905ed531d | -14.71188 | -46.00518 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23bf8dd9-95bc-3a5c-84cd-955eb7a7091f | -15.42378 | -43.05315 | 2025-10-08 03:49:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 19392cff-79c0-3f65-bfd6-3f13b22ef74d | -8.22696 | -44.1661 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a2d6c61f-ce8e-3a85-b9bf-6dfa90f72dee | -11.46663 | -43.48495 | 2025-10-08 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9667020c-9bd2-3347-bb77-2dc0af0d6ba3 | -10.4219 | -44.49907 | 2025-10-08 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea9c0187-5116-3522-9cad-c369baba2d37 | -9.75959 | -47.68684 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 882c89ee-3a84-37d2-9352-22c66c5ed897 | -14.44934 | -48.79118 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43fdcc31-bef1-3c98-b897-bdc8bcff8197 | -14.14851 | -43.17447 | 2025-10-08 03:49:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2e05ebf4-0f1a-3512-911e-ec14c312d229 | -11.74009 | -50.94436 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 3a9bfe53-e36e-3ded-b311-135c336c7bda | -8.56608 | -46.23367 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e802a4aa-7cbb-37e1-9e70-025732f278ed | -14.89348 | -42.10345 | 2025-10-08 03:49:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e06954dc-7be5-355b-b635-ee7e181a6e70 | -8.20223 | -44.20061 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 436b5deb-7ad4-3ba9-b767-f49a83bab56e | -15.95047 | -42.60844 | 2025-10-08 03:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 6922793f-cdc6-3e02-8ecb-88eff7d4fa4e | -11.68469 | -46.37825 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa656369-ac4c-3adf-9bb7-c1b16b1e4b33 | -13.00006 | -46.78311 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ec028759-b785-3da8-bc73-ddd12c6a1744 | -11.99395 | -46.77364 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8cfb39f-f0e6-3d1f-9772-ac43122dee37 | -14.92019 | -46.80467 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f15cba61-5f3a-3398-9b8b-82ba2d2a2236 | -14.5307 | -46.64425 | 2025-10-08 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 008ee658-3f5f-313a-b0d6-b3272f0414c7 | -13.80534 | -45.78699 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07f63190-a053-3306-ac52-35b03ee4e87b | -10.36472 | -50.28852 | 2025-10-08 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1fa95a3-57d0-3039-89ef-a0d89b93dc45 | -9.25649 | -40.43863 | 2025-10-08 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e1060694-2f68-30b6-aaa5-51cc54181774 | -8.56748 | -44.62526 | 2025-10-08 03:49:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52af3134-31e3-37e2-ae3e-8d2202d17ce5 | -11.45016 | -50.20606 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9383785a-4fbf-39f7-b5ed-c4f3d30cea28 | -13.28636 | -48.03835 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cb92686-bb31-3c74-9cec-906a5b93a1c0 | -9.1889 | -47.80133 | 2025-10-08 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bc5d3b11-e8c6-3383-9913-22b168407061 | -12.9194 | -46.82571 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 643159de-8d85-3fc6-8b1a-685bbb67689a | -9.19043 | -47.79309 | 2025-10-08 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0e667825-8c73-3351-a2d0-07f43c7bfebc | -10.3887 | -50.23371 | 2025-10-08 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4388ab4-8f21-3dbe-a1cd-41ce3caacaca | -3.45083 | -45.59635 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b9540810-7994-33f1-86ea-e539748d39bb | -11.34091 | -44.88386 | 2025-10-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 82200daf-cb1b-32c0-b334-f3dffd272d88 | -11.1451 | -47.7458 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a758a176-4039-3052-9c0d-1861b1cd1dde | -13.22536 | -47.19381 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| afc61697-d982-35ab-9f2e-13b747c67002 | -13.80767 | -45.80431 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b2ff985-1d6e-345e-baca-5e1dd94d0bfa | -13.07511 | -47.92434 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fea6a9de-4c1f-3ab4-952e-04fc3abe004d | -3.24222 | -46.79336 | 2025-10-08 03:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c24459ea-1800-3af7-9747-f8837e0563dd | -13.8025 | -45.80179 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13a39a8a-3f20-30e7-ac69-7a86df4569ae | -13.07702 | -47.93032 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5f99a1c-2fb9-34f7-9fa3-b96883aedb2c | -13.22553 | -47.17923 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60736e90-9cc8-3e03-9860-30ced98547ed | -3.24004 | -46.79583 | 2025-10-08 03:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25204e64-2f7d-3998-8d6a-b90c29c5ed30 | -9.79508 | -47.74476 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 261d9d72-d533-30b7-bd07-9c15e5ad4f4e | -14.91418 | -46.80969 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b744b6a-6c31-3801-8407-b124fb5f5041 | -14.36584 | -45.23167 | 2025-10-08 03:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e28abe5f-f4e0-3db0-b33d-d9a4488a9edc | -10.881 | -47.09969 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70081080-1067-3508-bf59-a9fe88be40df | -14.74131 | -47.85957 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a503be71-a82a-398e-bd73-46e65a9c5e1e | -3.12057 | -48.78721 | 2025-10-08 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b3abcae-128c-3dfa-8ea4-d1bdacd905dd | -8.26655 | -43.82727 | 2025-10-08 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03772333-4c32-3e61-bbe5-d250fbe1d249 | -13.80306 | -45.80346 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a65fdc72-af13-3dee-b018-2ad8166e7740 | -9.97562 | -48.78387 | 2025-10-08 03:49:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09aba9d6-e2ff-37bd-adab-119d0dfd88f3 | -15.95201 | -42.59959 | 2025-10-08 03:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| a71000cd-c222-3524-a774-b58a2e1b2fb0 | -13.72678 | -45.70198 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 374f060f-6009-387f-87b2-ceb6c5b2d6f0 | -15.28131 | -45.33974 | 2025-10-08 03:49:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a7687e2-dbe3-3797-b59d-2b3d7658691f | -3.98323 | -40.39972 | 2025-10-08 03:49:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3b2a9e3a-7b92-34b2-81cf-a2633968283c | -12.37499 | -50.30138 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 96523292-d4f9-3f10-81a1-bdb2253553ef | -10.21851 | -48.17172 | 2025-10-08 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c05fa05d-ad91-3965-aedd-f49e5e141845 | -8.46233 | -47.20899 | 2025-10-08 03:49:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ce9feb1-794b-3f8c-9ecc-6f2d2a533ed1 | -11.68958 | -46.32479 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31b985ab-10f1-3ba6-a8c8-194701deab3e | -15.31121 | -46.1675 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d7f12d2-fd11-34af-88cf-ba3aca0cbf35 | -13.23127 | -47.7974 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e79b3816-7f55-3faf-94e4-b8b97745c828 | -4.93364 | -38.75302 | 2025-10-08 03:49:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44e6bc9b-d1ac-3cf5-9d81-787518ac9a80 | -4.00405 | -38.32727 | 2025-10-08 03:49:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 570b0c55-8248-310e-9aed-87ad1f9be0ae | -13.2855 | -47.15673 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2644cfb2-fdda-3285-844c-d80653878080 | -14.83265 | -48.41646 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eea6a999-9dd1-329f-a9c9-c5d9591e2885 | -13.06932 | -43.5917 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 011d957e-cf5b-3346-ac81-39b5cbf75f96 | -13.80396 | -45.79855 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e735eb47-1f61-3992-aba1-03235f2d4823 | -10.17311 | -45.5541 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1788413-c16a-30b4-9280-30c797150514 | -13.07425 | -47.92861 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff364daf-d833-30e5-9fa1-436fed6f1fbf | -9.18814 | -46.91249 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f107d3f-0563-34d3-ac15-303c42d00ef3 | -13.05707 | -47.88937 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e7bd667-d574-3084-ba00-f42179f6794f | -3.09393 | -47.01885 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf963ad6-a78e-3468-b125-b49f786c4e27 | -13.23179 | -47.18807 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46ff7fc8-cb65-3866-8e87-ddbe129d443b | -12.42715 | -45.62408 | 2025-10-08 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d68c7499-c970-3140-b8bd-f144ed8b5b1f | -9.39678 | -45.95119 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 549d0ad6-4cc7-3242-95fa-7385cabeb46f | -15.53448 | -42.33918 | 2025-10-08 03:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab849954-ce5b-3929-84c5-b28363411915 | -14.71728 | -46.02716 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15d8855b-4910-3dc1-997d-e7612f08e707 | -13.37764 | -47.24271 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54fc8d50-60f9-3826-ab0e-a7dedc8b0f15 | -13.22233 | -47.18221 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 758bbe68-94b2-3dac-a7b0-bd0bd06013dc | -13.79935 | -45.79765 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b361a99-59b9-3133-bfb3-f070d8954ae8 | -11.68127 | -50.96273 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e2e1dfc8-7d3b-3cbc-9219-8d719e91586b | -14.36874 | -47.73441 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bc5bb1a-f5dc-3955-ab94-13b95fe3ce93 | -11.87125 | -44.93326 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8682281e-dfbd-30cb-823f-30f0b82a48a0 | -13.80487 | -45.79362 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b0476e2-0f16-3f31-9933-fd94d08bff53 | -14.88929 | -42.26231 | 2025-10-08 03:49:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c833d9d-d16f-31a1-9e08-a3eb221cef09 | -13.80805 | -45.79773 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b42e068-0fe7-3c32-ad17-bcd79a6d0bea | -11.87167 | -45.74822 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce387407-621a-35cc-a97f-55995c676506 | -14.44858 | -48.7949 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdfc3929-9cc7-3bde-993f-61103610bcdc | -11.85119 | -44.91555 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 069a990a-47bb-3b78-9d18-59d58d3ee482 | -12.79159 | -48.82075 | 2025-10-08 03:49:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 223fb868-e493-328f-98bf-f89fbbf78e4b | -11.90397 | -46.20539 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 499be31e-809d-3764-bdfc-debdca1f0128 | -12.00016 | -46.76855 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| bfa43c5a-55d2-361e-9dd8-e5c9e5f23d1e | -12.01324 | -45.19428 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README19.md)
