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
| f4d8d65d-a658-308c-88e5-7898a5832109 | -10.39892 | -61.21199 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63a86d06-b858-38ca-a6c1-c38498cc3cd7 | -9.3293 | -65.31731 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53ecfae3-cb98-3274-849b-6c21a34d6246 | -9.49318 | -63.46125 | 2025-09-18 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08f02a43-9bb6-3fc1-998b-3cf11cddb55d | -10.17675 | -63.05229 | 2025-09-18 05:33:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d006497-1e66-3dec-b789-32b789663a49 | -15.31921 | -59.41924 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54691db8-162d-3641-934e-19a1eec1a19a | -9.38204 | -68.77557 | 2025-09-18 05:33:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d329d207-7778-3901-a538-4b686968e4f7 | -9.76789 | -64.29484 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0942c4d-22fd-305f-96fa-803e33f279ec | -10.36693 | -61.26069 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47fd220e-aaf9-3d40-b6d5-249b15566096 | -12.40503 | -63.88718 | 2025-09-18 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63ffdfe3-8935-3abf-8750-e972b9827ecc | -10.07071 | -68.46912 | 2025-09-18 05:33:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8cf16bf-5330-390b-8af5-cf63cce49ca7 | -9.75714 | -64.2968 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb53293b-826c-3c63-b17e-f7d99e099c16 | -9.14691 | -60.35616 | 2025-09-18 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb20c90a-a512-3b5f-b352-d93466e8994f | -10.57937 | -63.4812 | 2025-09-18 05:33:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf731021-f966-3845-a7fd-19e0e7da9647 | -11.37127 | -50.84243 | 2025-09-18 05:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a0b91d17-f26f-34d4-9a85-b7558ee24bac | -9.59097 | -64.41615 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3355451e-ec29-3058-8261-bcdb43673d90 | -9.46974 | -60.48573 | 2025-09-18 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 729006dc-c8c8-3414-a8db-119779cf3744 | -9.21261 | -59.55757 | 2025-09-18 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdf79407-acc9-3cde-8a3a-01c2ba4ba6e0 | -10.57604 | -63.48066 | 2025-09-18 05:33:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69b5fe9b-af9c-3355-a928-cee76ec6b0a2 | -12.65657 | -54.70142 | 2025-09-18 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64387b9d-f69f-3df1-91cb-7783ab4192cc | -10.27055 | -67.2833 | 2025-09-18 05:33:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d71cf1dd-2497-3163-b2d4-d407a783e46d | -10.41552 | -61.19539 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5991c69f-15be-3850-8728-9496e262e542 | -9.49977 | -58.94012 | 2025-09-18 05:33:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 031e7f6a-53e7-31a9-b37e-c784a701002b | -10.41036 | -61.20609 | 2025-09-18 05:33:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c1276df-3115-3b5b-90b9-02eb401b6334 | -14.75159 | -60.20142 | 2025-09-18 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6efe6ecb-2c50-3dc7-a4ce-6c7740cd5999 | -9.7645 | -64.29427 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78a38acd-36c8-3a7c-8bd2-d5bd75c94b6e | -9.15041 | -60.35672 | 2025-09-18 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b64a46b-3510-3bdf-8dc0-41968eb9d481 | -13.29629 | -61.79601 | 2025-09-18 05:33:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5a9f0aa-a63d-303b-9697-395d940e54ce | -9.78707 | -65.05567 | 2025-09-18 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8d61db7-a69d-3e1e-b029-1170909b6227 | -12.4078 | -63.89128 | 2025-09-18 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0a541c4-f6ff-31c0-bdf6-f97c9a53a860 | -15.83267 | -59.38233 | 2025-09-18 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a41e4606-dfe2-3b50-b6ad-9d8918c30e8d | -11.38569 | -50.83292 | 2025-09-18 05:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bc579bf-831e-376e-ba72-cb4045e20d1e | -12.82116 | -52.98772 | 2025-09-18 05:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b9dd455-0594-3a14-bd13-6cc98eb92a5c | -11.59668 | -49.82306 | 2025-09-18 05:33:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d53ff570-cb78-3a64-83b0-712300bfdaef | -11.38505 | -50.83859 | 2025-09-18 05:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4911eab6-a64b-3e11-bfa1-73ad5bea1fc7 | -19.58732 | -57.76394 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 22a0912c-b23b-3988-8405-ea0e8d764412 | -20.5002 | -56.86914 | 2025-09-18 05:36:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bee7b36-cce0-3275-8740-df0cc3dbf8d5 | -22.96545 | -51.6022 | 2025-09-18 05:36:00 | NPP-375D | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 386a769c-27f3-3e7d-a6b3-01f3a1c4df4f | -22.95794 | -51.60799 | 2025-09-18 05:36:00 | NPP-375D | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| e8899a79-d21d-3ed5-b570-5a35c7bd1926 | -22.96652 | -51.58658 | 2025-09-18 05:36:00 | NPP-375D | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| a614d00c-7d9b-39ef-a67c-871a9ecb39b2 | -19.56095 | -57.78634 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 714476c9-23d5-3437-8d32-e4d95b5d6f09 | -19.56622 | -57.78186 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 15cbdf33-13af-3ac1-a4d4-716b5337a534 | -19.58694 | -57.78079 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e2198199-8b25-3e00-826e-98e869298f95 | -19.58672 | -57.76903 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bc34744f-6bef-39ed-8daa-0d9b04965709 | -19.56155 | -57.78125 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 74c14ef9-3320-3ba8-b098-a2836c84b4c3 | -20.05382 | -50.37752 | 2025-09-18 05:36:00 | NPP-375D | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 741c5dcf-dda0-3e10-955b-4df9ec1a06eb | -20.05285 | -50.37379 | 2025-09-18 05:36:00 | NPP-375D | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 10ac0bba-1fed-3b21-913a-ee9e58872c01 | -19.59334 | -57.76607 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 28297136-4fc9-3837-b792-0bbfc3f2181b | -22.13003 | -51.18479 | 2025-09-18 05:36:00 | NPP-375D | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8864e30a-4513-33f6-8bf7-1883bae3ed72 | -19.59276 | -57.77118 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1fbefc03-8321-3f68-a1cd-c0d169738476 | -19.58809 | -57.77057 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 38165f5e-bd6d-32da-b0d8-ffeff05fb294 | -19.58866 | -57.76546 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 53b5e408-9461-3208-b26c-31fca5b09476 | -22.95747 | -51.61496 | 2025-09-18 05:36:00 | NPP-375D | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 73c4a5e8-8bce-3e2f-8974-e4206570fbe1 | -22.1372 | -51.18579 | 2025-09-18 05:36:00 | NPP-375D | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1de1b4de-53bd-3173-a446-eaacdc8ee852 | -19.58638 | -57.78588 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5bd81d06-16cd-3678-86d9-06c10047d4a5 | -22.96499 | -51.60901 | 2025-09-18 05:36:00 | NPP-375D | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 33f9a7d8-1b8e-3a62-a0d2-01a9205173e2 | -19.592 | -57.76453 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 989cb8a4-4ae0-3ee5-a59f-04e160f60871 | -20.06178 | -50.37048 | 2025-09-18 05:36:00 | NPP-375D | GUARANI D'OESTE | SÃO PAULO | Brasil | 3518008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| da351431-6e4a-376e-a6d0-dc1671d20807 | -19.58489 | -57.78431 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fcaef9a7-8567-3836-b952-220b143816de | -19.56562 | -57.78695 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 0b0390be-7b41-3930-a71e-bf820b84ab47 | -22.95841 | -51.60101 | 2025-09-18 05:36:00 | NPP-375D | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 44c89f04-bf54-3fdb-bd3a-e562ee13258a | -20.06023 | -50.37451 | 2025-09-18 05:36:00 | NPP-375D | GUARANI D'OESTE | SÃO PAULO | Brasil | 3518008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2a4108e4-d1f2-3ef6-b9e0-0126e8a3e52f | -19.56036 | -57.79142 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 67d83b5c-6dea-3b4f-8e53-70c7d300f795 | -19.59139 | -57.76964 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 274a37ff-82e5-3126-a58a-45119f6e2f88 | -22.95893 | -51.59341 | 2025-09-18 05:36:00 | NPP-375D | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 051e942f-c052-3b87-90da-403043992c90 | -19.57943 | -57.80562 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 51cdd081-f6c0-39ce-a448-106b4b558a1b | -22.96451 | -51.61604 | 2025-09-18 05:36:00 | NPP-375D | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| fcd7b102-9a4f-3693-b834-143563738a06 | -19.56968 | -57.79263 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 932b339c-867e-36fa-9141-876fcf5fa530 | -22.96597 | -51.59461 | 2025-09-18 05:36:00 | NPP-375D | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 293868d9-bb75-3660-835b-ac2ec89c1f33 | -19.58956 | -57.78492 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cccdb339-18c2-3839-8644-4beffb8e5dde | -19.56502 | -57.79203 | 2025-09-18 05:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| fe07d060-8d02-3094-985d-3b6faaab3cdf | -22.9714 | -51.5902 | 2025-09-18 05:50:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| 455196fc-fc00-33a4-be4d-c00a66e36b41 | 4.30037 | -60.94861 | 2025-09-18 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89faacc3-cf25-362d-826b-1085fe80cd21 | -3.94164 | -55.8479 | 2025-09-18 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 669831ce-454b-3f9f-ae85-f2f7eea3c0c8 | -9.00308 | -63.6805 | 2025-09-18 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 207ddc38-6f31-3a1a-941f-8d5b19bde248 | -8.85036 | -63.53394 | 2025-09-18 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e26022bc-e100-31e1-8fcb-de6fb345314a | -2.70813 | -54.95418 | 2025-09-18 05:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ac5d67d-bc1e-361e-b48c-ae816dbc77a7 | -8.99948 | -63.67619 | 2025-09-18 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 503e5643-ac63-355b-a584-0e45865d6fa5 | -9.46435 | -60.48404 | 2025-09-18 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0119098-a868-3273-ae45-1396e9fec5c0 | -8.68136 | -66.57935 | 2025-09-18 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8abdd3d-e67e-3e82-9e2c-6158b8ece92b | -8.94621 | -63.04864 | 2025-09-18 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b48363-1e9d-3f26-bc02-ec4a4baca066 | -8.83243 | -62.37351 | 2025-09-18 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79520747-206e-3577-8819-5c0a368890a5 | -9.0309 | -67.45754 | 2025-09-18 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4579f630-66c7-3155-90d0-10be7ff49dad | -9.15439 | -60.36092 | 2025-09-18 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe3f4996-6531-3701-88ff-40b0b07f3cb8 | -8.67033 | -62.59415 | 2025-09-18 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1dead94-1569-3787-95ed-3b53d893ac0c | -9.14923 | -60.36015 | 2025-09-18 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b650e42-aebf-340f-819d-f2f679a4d153 | -6.28848 | -68.23931 | 2025-09-18 05:53:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b5907b2f-3db5-3d6c-8799-e9f944439beb | -9.49076 | -63.4618 | 2025-09-18 05:53:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56d5501e-b1d4-3ac6-a914-8559ae7fd46e | -9.46992 | -60.48165 | 2025-09-18 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58f96647-aa02-3643-ac8f-f9c25f1389d0 | -3.94812 | -55.84865 | 2025-09-18 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2aaa7d9c-e32a-3f5e-9fb2-2f3a42e8ce76 | -7.59768 | -67.42055 | 2025-09-18 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 258e14eb-d8bb-3877-a7ad-b1f1eda0befd | -9.46909 | -60.48787 | 2025-09-18 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2410a7e1-4fa2-38fa-b363-f67fb1dbef7a | -7.23921 | -60.64651 | 2025-09-18 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88ffd2ae-dda1-3642-9d9e-a2f8da883d3e | -8.96376 | -67.46583 | 2025-09-18 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b5dcfdb-345d-3a81-98c0-0b5dd46504cb | -7.24253 | -60.64639 | 2025-09-18 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c229159-9c9c-3deb-a398-2dee664df020 | -2.71483 | -54.95512 | 2025-09-18 05:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f69df198-e0b4-374a-ab08-c83ea87dde56 | -9.59083 | -64.4155 | 2025-09-18 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b412fda1-593a-3d4e-98eb-b2290aee3a26 | -9.46951 | -60.48477 | 2025-09-18 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b6488fc-16b5-3729-bee3-d7622d806da3 | -3.20045 | -54.97752 | 2025-09-18 05:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1671481-3306-3db7-95de-a06ec7a2b92d | -8.96659 | -67.47 | 2025-09-18 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1480b5cd-1bc6-38ff-bfe6-c4d2bc77aee6 | -8.9468 | -63.04457 | 2025-09-18 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README31.md)
