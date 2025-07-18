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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2cdb9b3-546d-3679-abfa-726f839329ae | -11.74036 | -48.52653 | 2025-07-18 04:53:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffa6dfcb-1275-377f-ae06-b6cd6a74c17c | -6.61956 | -47.19256 | 2025-07-18 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4785157b-0392-366a-9f34-f60a93420273 | -10.05745 | -59.1029 | 2025-07-18 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67cceb55-22b9-38ff-bb67-4301eb84efaf | -12.5743 | -44.75083 | 2025-07-18 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d94ec0ff-380a-3c6f-97a0-655362e049ce | -10.09209 | -47.24767 | 2025-07-18 04:53:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5584526-727e-314e-b7cf-4e046a560d02 | -6.62016 | -47.19543 | 2025-07-18 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15cedce5-37ff-3a5c-9bc1-354f56d291d4 | -11.55778 | -47.08569 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d683cd4f-3339-3873-a945-fc705f7a2552 | -8.04371 | -50.07909 | 2025-07-18 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f78a5c8b-2df2-34ad-af48-d00f656deb74 | -9.86071 | -44.70863 | 2025-07-18 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a5ad7e0-dee0-3dd7-873e-96b73963d8be | -7.60656 | -46.3195 | 2025-07-18 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bad3e5f-5875-3b92-93c0-23081bee9e58 | -11.55841 | -47.0811 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f89e4674-e53a-3c19-b75a-bc8768bfae21 | -9.74975 | -48.60626 | 2025-07-18 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0e0a382-85ec-3643-a448-d6a1396d2cbd | -10.81988 | -49.29076 | 2025-07-18 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d297304-8500-3b29-a75c-2363b83937d9 | -8.04432 | -50.07498 | 2025-07-18 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d95d003b-ac71-373a-89f8-15d673864c99 | -9.86262 | -44.70591 | 2025-07-18 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43538726-4021-3333-83ff-655389918afe | -12.48668 | -46.92221 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a041eb03-1024-34ed-b545-cd2df7d25188 | -8.37955 | -44.03374 | 2025-07-18 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a37e9f3-b658-3e74-9782-514626a1bc3f | -7.58845 | -46.30573 | 2025-07-18 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87d8b057-ec0b-3dba-8918-f9d9ce3645df | -9.27269 | -49.63497 | 2025-07-18 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29fea297-65ba-3467-807b-4305907018bd | -7.47662 | -49.21589 | 2025-07-18 04:53:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b0c8ea7-9e25-3d0e-9aae-0215a5658af3 | -8.9697 | -61.51515 | 2025-07-18 04:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f729978e-7b07-3a1b-824e-d87134fd4ea7 | -11.56551 | -47.0962 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9f990d9-eeb6-3e0e-a030-8c73e4ec3659 | -7.19136 | -44.07494 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1a5a16f-cae2-324f-8b44-21c295e475aa | -6.97183 | -43.73452 | 2025-07-18 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 787dd77e-1527-3e11-856c-85c8065d0413 | -7.2591 | -44.50832 | 2025-07-18 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1ee0cec-ebec-3c10-b956-983664f2015b | -12.48731 | -46.91739 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd368fc5-56ca-33b7-996e-77fdf466442e | -9.27464 | -49.63744 | 2025-07-18 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0d16d73-8c44-38b4-9663-8cd741de4df5 | -9.46809 | -62.20147 | 2025-07-18 04:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67ca4ec1-e555-3865-9f1b-a900fdb34e9d | -11.99371 | -45.30648 | 2025-07-18 04:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bf928cd-cd72-3450-969a-c9a43b451202 | -12.3935 | -50.3745 | 2025-07-18 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48af2264-f9fa-33d3-b3cc-ca9149ce7052 | -14.01143 | -51.21222 | 2025-07-18 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2830527-d192-32b8-b674-1fc050f7f211 | -14.1526 | -51.03026 | 2025-07-18 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab29f734-8b32-3382-8498-77a306a61691 | -16.41863 | -53.16252 | 2025-07-18 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5694d5cf-d327-38ba-83b9-eb1ebddac87c | -18.22366 | -54.54951 | 2025-07-18 04:55:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a77d0dda-1bba-3836-a11b-f38aaeae3f93 | -20.04278 | -41.66794 | 2025-07-18 04:55:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 15b2d2fe-a053-3b3d-8618-3656565a7975 | -18.87871 | -47.98689 | 2025-07-18 04:55:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 72c565c4-3ab6-3366-8f96-50f7bd855691 | -15.34215 | -49.42422 | 2025-07-18 04:55:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cad08b68-239e-3c79-98e4-1d37c51ca7e1 | -12.42741 | -50.03705 | 2025-07-18 04:55:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b7c3f4f-2954-32f3-86df-03dace34e2ac | -16.52117 | -50.90836 | 2025-07-18 04:55:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6ab5980-699e-3c45-ba22-a362f5cd404f | -15.1825 | -43.53827 | 2025-07-18 04:55:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8babe205-1791-3eef-ba85-26f7b4bdd091 | -14.71718 | -45.10626 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7748b642-dd8b-3630-86aa-270311c52188 | -11.88382 | -58.71515 | 2025-07-18 04:55:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3242b31d-09fb-38a1-be1b-8546471db75c | -12.3922 | -50.38337 | 2025-07-18 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8dd047e-ff97-3b2d-8f63-192ee0ef2a56 | -14.2076 | -45.33719 | 2025-07-18 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b51f198-6aeb-336b-be6f-1293177b2535 | -16.41861 | -53.16331 | 2025-07-18 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90986ad7-838d-3038-b8d4-9e96f19c014a | -12.57983 | -56.97407 | 2025-07-18 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acdae4d5-14fe-34de-b341-690fd9fd676f | -18.58254 | -52.3976 | 2025-07-18 04:55:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 37e95253-87b4-37de-b8d0-f02191ebf420 | -9.8833 | -65.17042 | 2025-07-18 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a384789b-9a0c-30a4-87db-af7af18d7e82 | -18.57895 | -52.39711 | 2025-07-18 04:55:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00eeb6d1-2ccb-3b79-badb-73a12fdf7984 | -14.71313 | -46.17727 | 2025-07-18 04:55:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 616a0ba2-5c28-3d32-8a7e-0b9369a434a9 | -15.72198 | -47.04374 | 2025-07-18 04:55:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d68bdc2b-04ca-36bf-b752-040cd4d713da | -14.71242 | -46.1832 | 2025-07-18 04:55:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbfabe44-3d7a-35e8-a6a1-d433830a6d42 | -12.58053 | -56.96995 | 2025-07-18 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 29fcaa88-9b7f-3871-bc29-deec451763b1 | -14.2072 | -45.34052 | 2025-07-18 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78ff3b84-9f78-3b3f-9038-13370033ae63 | -12.43735 | -63.69982 | 2025-07-18 04:55:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d75e368-694f-3b1b-a4c2-16c00282ad0e | -14.72177 | -45.11386 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30d6f001-1aa0-32de-ab67-06c211d45226 | -15.15821 | -46.18355 | 2025-07-18 04:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f38c87a-5491-36c9-b7dc-1d057065fa32 | -18.65743 | -55.73035 | 2025-07-18 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 864cbb71-3ec9-3769-9748-a51916466eed | -14.20272 | -45.33331 | 2025-07-18 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f518bf1f-8eee-3d18-911e-76758a2fa42d | -14.72665 | -45.07139 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e81141b-c6bd-3557-95cd-ca4d96ea2c52 | -14.70672 | -46.18829 | 2025-07-18 04:55:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12450e7d-3cfd-30bb-87df-750f6133afd6 | -19.5698 | -51.92268 | 2025-07-18 04:55:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd7712b2-04ef-3463-866e-4e4186b46987 | -14.14895 | -51.02968 | 2025-07-18 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bff0c554-5b42-3557-8284-ff10b50f4ff0 | -14.72259 | -45.10672 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0de4dd9-0156-32fe-a385-3525cdd08626 | -18.227 | -54.55008 | 2025-07-18 04:55:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a81ffdfc-69f3-35e2-b40b-4b519dd0837c | -17.68123 | -46.81705 | 2025-07-18 04:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41479415-5284-3eff-a4c5-1a0acf71ae8a | -12.42698 | -50.01335 | 2025-07-18 04:55:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2c5cc3c-549f-3eb2-a5a1-a801b44deb8d | -15.15746 | -46.1898 | 2025-07-18 04:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd2575fe-ca2e-3ca9-95e8-e54f3c7befd8 | -14.51483 | -48.57228 | 2025-07-18 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 187f8097-1e8c-35f6-bdbf-7964a0356f43 | -14.72758 | -45.11084 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b6c0352-7b54-378d-b9ed-3f6e9169649c | -18.61256 | -44.26484 | 2025-07-18 04:55:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 658ee879-7c26-3ac0-a65b-d69f4a4dd220 | -18.42249 | -53.03151 | 2025-07-18 04:55:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2b0a02e-97b6-3117-9786-720e0c77a8ad | -14.14956 | -51.02534 | 2025-07-18 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 801ed592-0828-3611-bc33-bcbe096054c6 | -15.18098 | -43.53691 | 2025-07-18 04:55:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5cc75ab8-2a3f-3e1a-a8c0-0a51ef7853db | -16.70905 | -49.35537 | 2025-07-18 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c0fe981-88fd-3845-9c5c-f7529928d6da | -14.20153 | -45.34319 | 2025-07-18 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d457ce6-c2c4-3126-8152-c387ba458919 | -14.73164 | -45.07561 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0521d245-68c0-3c58-bb39-bb2649779a89 | -13.59819 | -51.80713 | 2025-07-18 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 115220ad-53b3-3d16-a997-7c8eb2ac0f3d | -14.71171 | -46.18907 | 2025-07-18 04:55:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff0069b8-4ed4-3e62-b605-3d5cd69e6296 | -15.37465 | -52.75831 | 2025-07-18 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68d26911-9646-3c7a-a368-298af7925c16 | -20.03573 | -41.66718 | 2025-07-18 04:55:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 60e9e75d-e812-38ca-b8e6-82f07e2efafb | -14.70602 | -46.19409 | 2025-07-18 04:55:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03b7dbac-5753-390c-b639-1b6c02f4ac32 | -18.4213 | -54.5589 | 2025-07-18 04:55:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e8b79cb-bba6-32a6-be9c-c130f5b70e14 | -14.09225 | -52.19503 | 2025-07-18 04:55:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eed759d0-a295-3222-98f9-d501cc20cbf9 | -14.72123 | -45.07089 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f362bf0-cb7f-3459-a7b8-a3ae02f941e7 | -14.75427 | -48.27486 | 2025-07-18 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 227b47c9-7e64-3ec3-b2be-0af7e10a9e04 | -12.98905 | -46.92859 | 2025-07-18 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1671d75-9509-3bb3-b5ca-78ecd045e49a | -14.20193 | -45.3399 | 2025-07-18 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7da60357-656e-3559-9e69-e63981d771a4 | -14.73663 | -45.07986 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f60d8c07-9717-36de-b507-9c68ed5fd3db | -14.77132 | -50.53237 | 2025-07-18 04:55:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f190e1c6-32ee-3c85-9fe9-c2dee8af0f58 | -12.37518 | -50.34451 | 2025-07-18 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 822978e1-e67d-3fb1-a9b4-5987ae8f23b2 | -14.72717 | -45.11442 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a1d869e-f09e-327c-83ad-1d0042341b94 | -18.34751 | -52.532 | 2025-07-18 04:55:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 634901ad-12db-32e1-a71a-82f10577047b | -13.61735 | -47.92461 | 2025-07-18 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7b99a9c-1351-3664-ab03-b22508d88149 | -18.34993 | -52.53054 | 2025-07-18 04:55:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f552a2f-c850-3533-8218-a723081279e6 | -17.26838 | -49.0078 | 2025-07-18 04:55:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69f6167b-8044-33f6-bd5f-e7dd81784521 | -14.71677 | -45.10987 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09410a06-5c80-3c2c-a0ba-edd325609c48 | -14.72082 | -45.07447 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad1da2f7-eff6-3cca-ab1f-444f62df3804 | -12.37824 | -50.34951 | 2025-07-18 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc02b915-8d63-362e-9701-fd8b27d280f6 | -12.26066 | -63.82166 | 2025-07-18 04:55:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README25.md)
