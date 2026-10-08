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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06e87290-0ee5-3f83-aec8-b05224e5fea9 | -10.71885 | -56.04893 | 2026-10-08 04:49:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a241e77a-f5ba-3570-90f8-27a82eebd459 | -13.55196 | -49.158 | 2026-10-08 04:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0820e05d-10b7-3586-872a-ac0706604142 | -13.19246 | -47.87836 | 2026-10-08 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d6312ad-529f-3f3e-b534-9395c972fc79 | -12.16935 | -53.23536 | 2026-10-08 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6eeb477-0c67-33ad-a9b3-8a2202c33f32 | -15.10918 | -43.63205 | 2026-10-08 04:49:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df4c87a6-8973-3545-9a7b-79479901caf1 | -10.88107 | -57.07966 | 2026-10-08 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc1cc989-d134-3c0d-8be1-db6133a05f85 | -16.36076 | -55.33824 | 2026-10-08 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72a111d2-2257-3456-9afe-a5344b2f7789 | -12.18741 | -51.45303 | 2026-10-08 04:49:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 765d2573-f247-3681-bf93-0e12da695167 | -13.786 | -52.79926 | 2026-10-08 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbb8cb67-e2a5-3454-bb17-a6e4bbf325da | -11.77494 | -46.77018 | 2026-10-08 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35f412e5-eeb3-39b8-9576-5f1fa6deade8 | -12.22968 | -44.71231 | 2026-10-08 04:49:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc9ce0d6-b3b4-31cf-825a-2c3d3fbf6084 | -16.36202 | -55.33065 | 2026-10-08 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34dbb76e-a0ed-325c-9d29-8cf3597a01b8 | -11.7537 | -61.05899 | 2026-10-08 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c5beae71-9292-3818-b558-fd723a498ae9 | -11.35146 | -51.87293 | 2026-10-08 04:49:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 630845b3-4d07-3482-a65f-afe96daff4de | -13.50733 | -44.37211 | 2026-10-08 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd7d6ca9-8d6f-39cb-a179-77c4cc8b662c | -16.90564 | -40.89503 | 2026-10-08 04:49:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 655aee84-b411-38ee-91bc-779d29a97512 | -16.89407 | -40.88998 | 2026-10-08 04:49:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dbfd4d84-f60c-3c3e-8282-43f2f89b1dfa | -11.34485 | -51.87188 | 2026-10-08 04:49:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a567633-8b34-3b13-aef3-63210d2d6d07 | -15.56219 | -44.51987 | 2026-10-08 04:49:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dce4fd2-6aac-3392-b887-302a8f948b0b | -10.36094 | -56.43872 | 2026-10-08 04:49:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf975685-0f7c-35c8-92ca-cf5acdfaae2f | -10.61525 | -60.485 | 2026-10-08 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f53bd6e1-dbd2-3bf6-b318-56044ee8ee53 | -10.85876 | -59.11367 | 2026-10-08 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6b3aa75-ccdb-355b-bbfd-efebf777a675 | -11.01992 | -65.21255 | 2026-10-08 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 98719bb8-fd34-3d5a-9208-7113ab8ee988 | -9.47178 | -64.3548 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c12e55ed-3c51-399c-bcd1-718babeb41d9 | -13.1571 | -43.28124 | 2026-10-08 04:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| ca4e05ad-6c5e-303f-a3ee-e699cf634f13 | -12.19792 | -48.42126 | 2026-10-08 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d6f46c7-767d-3014-acf0-23dc1076a078 | -14.93491 | -48.10368 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d65ecff-458f-3c3c-8a26-73812f174171 | -16.90765 | -40.88674 | 2026-10-08 04:49:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 4096e14e-82ad-3b63-b888-a873f9e30368 | -11.62294 | -48.4911 | 2026-10-08 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8957eee-094b-35bf-8b0a-bf3619230678 | -15.92212 | -43.52577 | 2026-10-08 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 946429dd-c5c5-31ca-84be-e96f744df443 | -13.16251 | -43.28189 | 2026-10-08 04:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 59456787-58c5-34b8-9975-027c96d6cf13 | -13.7893 | -52.7998 | 2026-10-08 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d52abdc6-3e4b-320e-a51a-2b9f8bb0a30b | -18.26003 | -42.17506 | 2026-10-08 04:49:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 2f980040-df1b-3e12-8fee-cc944b8b3ef1 | -14.36061 | -55.03215 | 2026-10-08 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 910990d3-22cb-374b-8cd7-f5feedb40289 | -12.23312 | -44.72385 | 2026-10-08 04:49:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aef54051-cfb7-3247-8202-2be4c5b7b454 | -9.48989 | -64.36584 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0475fb6e-de90-3af6-bcd9-3655bece042b | -9.48364 | -64.36283 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cebb662c-bbd7-39bf-8013-c1f92e4aa795 | -11.90712 | -46.56108 | 2026-10-08 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55885079-c76e-3eeb-bb2a-17a374a7b1c8 | -14.67006 | -51.46304 | 2026-10-08 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf78488f-3787-3ff9-b3fd-2e752dc5b888 | -10.62022 | -60.48586 | 2026-10-08 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e781ff9f-cf66-34b0-b0ff-b6707ef86eb3 | -12.83655 | -45.57863 | 2026-10-08 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c38ae20-7cbe-360a-8fc1-9f165a459144 | -11.75312 | -61.06201 | 2026-10-08 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f57bb20f-7871-3370-9213-70502bbf3839 | -14.93754 | -48.11435 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 02d2339a-606e-3a3c-9a33-a5585f88067f | -11.34816 | -51.87241 | 2026-10-08 04:49:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82cc8d5f-2f87-3ec6-8786-8eacc3939c07 | -9.97493 | -57.52729 | 2026-10-08 04:49:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44d685c9-0383-3366-8948-df90de757739 | -11.78773 | -46.7789 | 2026-10-08 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 62e5e1b7-1189-3671-9039-957aa3cc0b21 | -14.93444 | -48.10714 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f34397f3-da4a-3ead-809d-2284e6df5a66 | -18.106 | -42.54805 | 2026-10-08 04:49:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c861dec5-55e0-32d3-bdc4-5ec58cd0656d | -13.17594 | -54.32243 | 2026-10-08 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2edc033b-332e-33a9-9820-a671436ec587 | -16.90602 | -40.89085 | 2026-10-08 04:49:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| f1a1b23e-1f8d-389f-920d-02cd60fd9c39 | -14.25675 | -57.03274 | 2026-10-08 04:49:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36c7b266-3f4f-362a-8ae3-ce477638897b | -14.93041 | -48.1067 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc156db9-aef5-3a72-91e4-d435c112faa5 | -11.8379 | -47.36389 | 2026-10-08 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64148e1a-54ad-3298-a604-856f3114b4f6 | -11.35803 | -51.87727 | 2026-10-08 04:49:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccb382ff-c17d-3723-a688-0dcfcc73e426 | -14.36931 | -55.02198 | 2026-10-08 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59689113-1a81-3d56-a4c7-a0dab2efbba2 | -15.55236 | -42.97935 | 2026-10-08 04:49:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 86d036aa-5c1d-37a4-b04e-047c67bea2c6 | -9.47929 | -64.35057 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 908477ae-c02f-350f-a745-5e967ddb6c93 | -9.48671 | -64.34814 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a71c19b6-4290-3974-9c36-d5f091ff4dcb | -15.68155 | -50.56829 | 2026-10-08 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccf8fa24-7b04-34c1-a5ab-2b1528940772 | -16.76075 | -53.37657 | 2026-10-08 04:49:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64b88bd8-ef23-3f14-8305-ef78a368190c | -11.63605 | -49.83641 | 2026-10-08 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7090340a-ad68-35b5-a419-75e51a2f25eb | -13.16294 | -43.27839 | 2026-10-08 04:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 517acffb-10da-3211-a1db-00baed55d8c7 | -10.61969 | -60.48874 | 2026-10-08 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c139bbff-045c-30ce-bde0-4aed1a6bb4e6 | -14.9358 | -48.11085 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3af5a430-ccf2-3647-b99e-128106148cf8 | -14.36124 | -55.02837 | 2026-10-08 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a51e1273-2200-39d1-8542-e39e1cfb69be | -10.36477 | -56.43935 | 2026-10-08 04:49:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93eeb562-e34f-3419-ae9c-19321ff3cbc6 | -14.93352 | -48.11384 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e7dc8100-3c39-3a94-82be-5aa7efc43888 | -16.12929 | -46.88502 | 2026-10-08 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d1ccdc13-086f-339d-b2e9-35b4f63db3e3 | -13.81076 | -52.79243 | 2026-10-08 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3f1d3b4-69b9-38f9-a6e2-d0aab8737cb2 | -9.48343 | -64.36458 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea37d75b-a58f-3597-94de-7dc4849a8abf | -16.89321 | -40.89897 | 2026-10-08 04:49:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 46f75dd2-ee2a-3f6a-92f9-da3c56142517 | -14.92138 | -48.11306 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ac8b23c-0a16-3c32-8e0b-243be167d6df | -9.47071 | -64.36031 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af6a3d52-5a56-3ef4-8686-f5a8618b29cf | -9.49208 | -64.35486 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a113ca2-4896-3d27-8c28-96d69f3e8f2b | -14.91832 | -48.10557 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a775ff5-28c8-3189-a0a3-7791dc24fa7b | -10.66624 | -58.92218 | 2026-10-08 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fcbfb07-2adc-33cf-95a3-50e215d672ac | -16.01494 | -43.60187 | 2026-10-08 04:49:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e91c0bef-2d5b-315e-be38-0a421c24feba | -13.80636 | -52.79895 | 2026-10-08 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c518c4b0-aaec-301d-b574-4337e85d8994 | -11.76905 | -46.78184 | 2026-10-08 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 37e0fe8e-737e-37da-b0a1-4935b0926c77 | -16.75689 | -53.3796 | 2026-10-08 04:49:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee6cc3c3-2e6d-3f45-aece-50e52d7e99f8 | -13.17257 | -54.32187 | 2026-10-08 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99cb256f-97e9-3947-8d1d-6f83a1443523 | -12.46032 | -52.48978 | 2026-10-08 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e1ff284-f17b-38bf-a2cc-ede4b7cb7e2e | -14.67683 | -51.46411 | 2026-10-08 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 466fbbf6-2f40-3a8f-ab22-60145d416c57 | -13.17255 | -48.13948 | 2026-10-08 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87465b22-af43-312a-8141-67af1bd1c3f0 | -9.48452 | -64.3591 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49347754-22ce-3df8-ba9e-d08f7e3a47b1 | -12.06229 | -58.0432 | 2026-10-08 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbd6d2ff-30f9-3d9f-bb2c-330b9523fa9c | -17.76384 | -42.42968 | 2026-10-08 04:49:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b9c0040d-caa4-3511-b853-92f133286d49 | -11.77046 | -46.78054 | 2026-10-08 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f68a0191-d2de-3b47-9c4c-6a234cde705d | -14.63063 | -54.25829 | 2026-10-08 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ee7d9ed-c6a9-3230-88c3-1556bd136783 | -13.50262 | -44.36869 | 2026-10-08 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7e2b896-673d-3b98-9249-82e0a3186b2f | -16.41579 | -50.48913 | 2026-10-08 04:49:00 | NOAA-21 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4f3e08e-f68c-3743-85b6-0a6b3ba0dfae | -13.23377 | -43.39589 | 2026-10-08 04:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b08ae19f-21b6-3989-b269-37cdad493bce | -14.93624 | -48.10746 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e56bb4c0-9185-3bce-8d5e-76cd4fa09680 | -11.80713 | -47.34835 | 2026-10-08 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faba0d9e-41db-3e3e-9efa-c3d6e31ecde9 | -9.49009 | -64.36412 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a0f725d-ba84-38e2-925b-d115e9c0c91e | -14.93087 | -48.10333 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e94f95c-8926-3dfc-920f-7b2d592dacd2 | -11.78722 | -46.78275 | 2026-10-08 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cba97e41-4cb6-3c39-aef4-00e3bd9dd6ba | -9.4716 | -64.3566 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2119c633-497f-3356-b19e-e5357c2b25d0 | -17.12007 | -41.34031 | 2026-10-08 04:49:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 1a45401d-ce19-37bf-8f3d-430f52b37d14 | -16.35995 | -55.33854 | 2026-10-08 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README121.md)
