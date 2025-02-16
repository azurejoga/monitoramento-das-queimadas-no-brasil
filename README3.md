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
| 615c95dd-ed08-30ea-aa6c-f1cfffa50120 | -20.36201 | -40.89168 | 2025-02-16 04:06:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6723f028-4296-3ec6-adba-3d67a09611a8 | -20.91442 | -56.53512 | 2025-02-16 04:06:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c515d43-d646-395c-b663-7741b4953147 | -23.40635 | -46.55497 | 2025-02-16 04:06:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fe50b0a6-7f61-32fe-a083-b2eb608dde4d | -22.54045 | -48.8119 | 2025-02-16 04:06:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2322a2e1-fbdc-35f9-9d7a-84d55085d145 | -20.34822 | -40.36198 | 2025-02-16 04:06:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8dc469d1-1f31-32cc-8dec-481b6f00cc35 | -21.17985 | -44.27439 | 2025-02-16 04:06:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| eccf9cb6-a8a3-3bd2-bd43-54143d5169e2 | -19.97013 | -44.21646 | 2025-02-16 04:06:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b73de96-78e1-3233-b067-e252feb12ff3 | -29.32424 | -52.39543 | 2025-02-16 04:08:00 | NPP-375D | BOQUEIRÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4302451 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bbfa4e5d-6cf4-366e-8cb9-2579a4d372dc | -29.32851 | -52.39635 | 2025-02-16 04:08:00 | NPP-375D | BOQUEIRÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4302451 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a9135a9a-e962-3307-8195-e68e3a79e084 | -5.00433 | -42.93559 | 2025-02-16 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8f05ee2-eb08-396d-b29b-e5733a567af5 | -4.95452 | -43.88597 | 2025-02-16 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b501f90-4e0b-39ab-94ae-fcc9966f66bd | -6.23818 | -44.83366 | 2025-02-16 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4efba51-2f4d-3a3f-b764-ccde46788db2 | -5.25819 | -45.24437 | 2025-02-16 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89fd5fc3-3e44-3087-b49c-245d7efdd383 | -5.43293 | -45.36465 | 2025-02-16 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6de6c62f-d682-303e-b382-9c267d82a5e0 | -8.40168 | -37.03614 | 2025-02-16 04:23:00 | NOAA-20 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ced5bb4f-742b-3971-9622-98fa22fe447c | -5.36319 | -46.26328 | 2025-02-16 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78d1abeb-effc-3796-ab08-979c22955499 | -5.092 | -45.82862 | 2025-02-16 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 803ed5a1-6934-3989-b086-8fbf942b5c67 | -7.0859 | -44.37481 | 2025-02-16 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29e25f5d-d4d1-3d0a-a54c-da58c80daaec | -5.67697 | -45.23764 | 2025-02-16 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 025bce0f-e0a9-37a2-9654-d6b2f465c1ae | -7.23672 | -44.71746 | 2025-02-16 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c6eb9ab-0208-3b4e-b7d5-a216c6fb91b7 | -4.80926 | -43.00891 | 2025-02-16 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84a63b5f-24b3-352e-9292-9b6a4aa89fde | -4.69274 | -44.38094 | 2025-02-16 04:23:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 585ff02f-3481-3d8b-b58e-4ac0ba32f002 | -5.15905 | -45.13923 | 2025-02-16 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 482edd03-b2c3-36e0-941c-b3a0289299ad | -15.82936 | -42.62723 | 2025-02-16 04:25:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2a0bb7b8-bd72-3a05-a3c1-f66152953711 | -10.73542 | -37.60386 | 2025-02-16 04:25:00 | NOAA-20 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 441ba869-6a88-303f-b322-426681190cf4 | -9.87807 | -41.80278 | 2025-02-16 04:25:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 149f5351-5f21-3932-9c9d-290100f196c9 | -15.82569 | -42.62257 | 2025-02-16 04:25:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 414c8971-8445-3d46-b768-27f472fccc91 | -10.47449 | -42.4653 | 2025-02-16 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c45b2709-d06b-3053-a95b-e6ff2ee2c834 | -14.13485 | -41.69252 | 2025-02-16 04:25:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e5dfc27b-9bc2-30af-b29e-bd6350e39f72 | -11.8888 | -41.76694 | 2025-02-16 04:25:00 | NOAA-20 | BARRO ALTO | BAHIA | Brasil | 2903235 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 04c91bf2-1c4c-3441-82be-61b228d64aa8 | -10.4752 | -42.46021 | 2025-02-16 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 443e3c36-2bb0-3ede-a55a-5940710771ff | -9.49773 | -42.99044 | 2025-02-16 04:25:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3c693c51-115b-32ed-80db-8f3c0d68ac70 | -10.33092 | -41.80145 | 2025-02-16 04:25:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a6188f4-f0dc-3e54-9a98-c81739602664 | -15.82989 | -42.62323 | 2025-02-16 04:25:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b6ea2cdd-8153-3dea-bac2-d92ae68d4d46 | -14.23162 | -41.60218 | 2025-02-16 04:25:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7c470ef6-f66f-3b9e-813e-a2cc7469bc96 | -10.47186 | -42.46309 | 2025-02-16 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 31181bc9-f060-3cb9-8ce8-3736412d0229 | -14.11839 | -41.67799 | 2025-02-16 04:25:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4fe5a6e8-df34-3bef-88e4-72abf438222e | -10.73503 | -37.60692 | 2025-02-16 04:25:00 | NOAA-20 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6940fec1-c415-33de-93e2-f76a21649f47 | -14.22774 | -41.59755 | 2025-02-16 04:25:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0cf262ef-a992-3071-9023-aeda4da7196b | -10.47581 | -42.4637 | 2025-02-16 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 52d89b58-f3d0-3abd-b338-0a867a822393 | -15.82966 | -42.6261 | 2025-02-16 04:25:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9426bff9-53ac-3578-ad48-78dc95861ad6 | -12.60065 | -45.05684 | 2025-02-16 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53fddd1f-11ee-346b-b4db-78034fd65a81 | -14.2233 | -41.59713 | 2025-02-16 04:25:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9a79eda-f133-3529-8004-44bba3e347ec | -10.73583 | -37.60064 | 2025-02-16 04:25:00 | NOAA-20 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a7c160da-cd0c-332c-8ab7-aac77b6daee2 | -3.23552 | -42.07682 | 2025-02-16 04:25:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ea5c82b-e50a-33cc-b703-5660e6c6b482 | -3.2392 | -42.07736 | 2025-02-16 04:25:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87b01e24-4c1c-3cb8-8a9d-597f0ea9ab73 | -18.51772 | -39.93238 | 2025-02-16 04:27:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a4ef666f-5a44-317f-a22e-1d5bcf1df213 | -20.91512 | -56.54111 | 2025-02-16 04:27:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ab06176-b0e7-3167-9b65-ea5903409b28 | -22.6774 | -42.85373 | 2025-02-16 04:27:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9b61fec4-d7f2-3849-a58f-17b80d6e4f94 | -18.52295 | -39.93303 | 2025-02-16 04:27:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 99490416-3c92-39a6-a1ee-f4c3b35b1013 | -20.33009 | -55.01119 | 2025-02-16 04:27:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b60649c3-876e-35eb-b214-08516509165b | -20.9195 | -56.54208 | 2025-02-16 04:27:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e387ea16-8205-3457-8c7b-75bfb7c8e16d | -21.03737 | -48.28257 | 2025-02-16 04:27:00 | NOAA-20 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 351e344f-6b19-3e39-ae60-5beaf0d3a6ba | -16.80935 | -42.52102 | 2025-02-16 04:27:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3853a000-05f4-3a55-bffb-64b262450660 | -16.81366 | -42.52153 | 2025-02-16 04:27:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00ee94f9-46fe-3b00-a73a-390fc7ac8e72 | -18.5174 | -39.93394 | 2025-02-16 04:27:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 23d2950e-5a1a-3336-b3db-06d16488e578 | -17.1176 | -39.50527 | 2025-02-16 04:27:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 15746862-1870-3942-841f-4d6d4f789267 | -22.58613 | -43.63976 | 2025-02-16 04:27:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f3cd8500-e6f4-3d3b-bdc7-f868be5ae489 | -21.18235 | -48.69461 | 2025-02-16 04:27:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 61f9a11c-74b6-39c7-bc07-d6b5838b01b9 | -20.3308 | -55.00747 | 2025-02-16 04:27:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35520134-5af6-360f-8b1e-b22ce6ef574f | -17.09386 | -43.806 | 2025-02-16 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91c19cd4-a143-3f5c-a5f3-1358b910355b | -22.78708 | -43.75615 | 2025-02-16 04:27:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6c46b787-d6cc-34f6-a8fe-2cfbc5568fdd | -16.80987 | -42.51676 | 2025-02-16 04:27:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f97bbad4-e804-303e-8389-73884836f3ef | -20.916 | -56.53671 | 2025-02-16 04:27:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8beff8a8-67d7-39f8-ae57-a54d835b363e | -20.92036 | -56.53773 | 2025-02-16 04:27:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecd7251d-781f-3892-afd0-670cb135fc29 | -16.80304 | -42.5169 | 2025-02-16 04:27:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbb7fe5c-4ca1-309e-aba0-39b0625830cd | -16.34532 | -45.68957 | 2025-02-16 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca90e74f-9e09-3295-8b96-2c7bf980162b | -16.80359 | -42.51265 | 2025-02-16 04:27:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 781ee7b2-9a68-35e9-927f-a882fd755b2f | -20.41418 | -43.55529 | 2025-02-16 04:27:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c75d8e2f-33a9-30c1-991c-e43ff579484f | -20.41468 | -43.55124 | 2025-02-16 04:27:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 790a7c44-ac93-37f5-bf78-aa2d5a9789dc | -16.81165 | -42.51808 | 2025-02-16 04:27:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7aa3c08c-b352-3722-8975-5d56c0a245ea | -16.4648 | -58.17549 | 2025-02-16 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1e59a0ce-9c79-3c10-8ffc-ebcc0766163f | -15.0796 | -48.94673 | 2025-02-16 04:27:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d404612-91fd-36c8-a77c-5adf439f9b16 | -16.4595 | -58.17438 | 2025-02-16 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 21a03bf0-397b-34eb-a373-ef6d157c0eab | -22.78492 | -43.7579 | 2025-02-16 04:27:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7ca1afc4-1852-3411-b930-2e4b8f783b32 | -18.51777 | -39.93063 | 2025-02-16 04:27:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| af2b39c1-6730-36ec-9376-aca35b683475 | -16.80734 | -42.51751 | 2025-02-16 04:27:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 465c69b9-6298-3039-9c83-afdfdb10fc41 | -17.00822 | -49.78069 | 2025-02-16 04:27:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1987793-ca1d-3659-a094-54d352a74ec7 | -22.53878 | -48.8111 | 2025-02-16 04:27:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d764e01-9224-3e79-b5f5-f14375ac474e | -16.79932 | -42.51184 | 2025-02-16 04:27:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32da93bb-2be4-3ba7-b690-3824d31c4f2c | -18.51737 | -39.93569 | 2025-02-16 04:27:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c9eeb3ed-89ac-3c86-83ef-d7cb9df79ae5 | -20.89383 | -44.21405 | 2025-02-16 04:27:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 67407d0a-d2ea-3cd8-9e5a-cd829765f34e | -17.6754 | -42.7449 | 2025-02-16 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 151fc19d-03dc-343f-bde1-92c26a475448 | -17.11722 | -39.50866 | 2025-02-16 04:27:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5c579386-b3d0-3bf9-960e-efa6661ea808 | -19.71643 | -40.35529 | 2025-02-16 04:27:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| de6699ad-ae45-3037-8fe4-862bdeb74290 | -22.53986 | -48.81438 | 2025-02-16 04:27:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e8a1a58-b28f-31cc-b64b-835cd8acd5ed | -16.34757 | -43.6963 | 2025-02-16 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7e936cb-79dc-3a46-93f7-d0618b2dfda0 | -21.19477 | -44.93797 | 2025-02-16 04:27:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5a012c77-4076-379b-a0e9-29b05edea882 | -21.034 | -48.28198 | 2025-02-16 04:27:00 | NOAA-20 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3271097f-0446-3a75-946c-78b9b6543893 | -23.33974 | -46.7721 | 2025-02-16 04:29:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8e5e3e5e-563a-37dd-8241-ba0198f977a1 | -23.4052 | -46.55793 | 2025-02-16 04:29:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f6271d7-09e6-3006-88ee-f7245d7e36bd | -21.24547 | -57.77567 | 2025-02-16 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2e5ac879-e026-344f-9db3-797d55decd88 | -29.32543 | -52.39396 | 2025-02-16 04:31:00 | NOAA-20 | BOQUEIRÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4302451 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 35c47cf1-6285-34db-986b-4c02723c8eea | -31.04816 | -53.35017 | 2025-02-16 04:31:00 | NOAA-20 | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| ba964769-c0ba-3b8c-a40f-aefdbe9da041 | 1.30849 | -60.40855 | 2025-02-16 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60279904-2b3f-3713-8cfc-5d58c4d81938 | 1.30666 | -60.41003 | 2025-02-16 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 482cb52c-ffca-3ec8-9c44-ef4ec00366bb | -20.91991 | -56.5353 | 2025-02-16 05:20:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 379c3493-e809-373b-b6ad-831ee4a66c87 | -17.7463 | -56.31169 | 2025-02-16 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4b498d8f-eaae-3305-a0e1-57c6aafb8140 | -20.91941 | -56.53941 | 2025-02-16 05:20:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88ddfd4a-d32c-37bc-bc9d-5db625f7ff7c | -20.91575 | -56.53472 | 2025-02-16 05:20:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README4.md)
