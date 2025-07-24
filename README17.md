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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9139beb-674b-3a7f-9de5-a7204d6aa45c | -13.7053 | -45.67687 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 287c93a5-a87f-3678-ba9d-b4fa18c15a0f | -12.42298 | -45.3872 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 334afec8-9cb8-34c5-9d43-1972d0497f9d | -10.66971 | -47.79625 | 2025-07-24 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a2bd721-3533-38a4-a31a-d4b0328a6353 | -12.65974 | -45.03992 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fd002c3-8bb9-3f43-83c9-b4d672fc1744 | -10.63031 | -45.23073 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11ba2c37-f8b2-3d1c-ab73-813121b66d7f | -13.65384 | -45.71533 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c7a955f-4da9-3a5d-9945-10e5f59b7b6c | -14.17214 | -45.34278 | 2025-07-24 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92cee7be-9cf0-31a0-a24c-8907a8ad3504 | -9.26722 | -48.55796 | 2025-07-24 04:42:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88afcaef-5626-31f4-bb0e-545559fc8867 | -14.17866 | -45.35025 | 2025-07-24 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fb81a30-88e1-34df-ba63-90d78cb8673a | -7.46189 | -57.66848 | 2025-07-24 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9977a08-1eb9-39a8-83f5-71b5cbe36859 | -9.52559 | -63.62669 | 2025-07-24 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0fe3d45-3a92-3222-b851-9b4da708ccd0 | -14.38299 | -47.76327 | 2025-07-24 04:42:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5632f90a-bbe2-3dfe-8ec0-3a0280fdc8f8 | -11.52241 | -54.68554 | 2025-07-24 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7f781d1-7781-3b2a-8bc0-a340b6e73286 | -12.6592 | -45.04387 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a95c799c-569f-3c8f-aa38-e17a1f651225 | -10.04008 | -59.09695 | 2025-07-24 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 615cacf2-cb22-3bd1-9d86-0e4fdd5e621b | -11.97094 | -49.10151 | 2025-07-24 04:42:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5fe2253f-1f34-3bcd-b411-a718a2eb6117 | -8.93111 | -47.34132 | 2025-07-24 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18497073-9dd0-38c4-8c86-d5854855e9d7 | -9.16897 | -60.83034 | 2025-07-24 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90953db0-e93d-3e29-908c-96b6f006e7c1 | -13.7032 | -45.69191 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 754ffc7f-cca6-3639-9803-22f08d3bf5e3 | -12.42868 | -45.37647 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79b75fdc-9c03-3aac-a9e3-034d0f17d852 | -13.70425 | -45.68439 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bf04a10-ebc8-3eb0-9095-9af0e5404736 | -10.65661 | -47.26151 | 2025-07-24 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91203f02-d61c-34a9-ae20-24b41e16a477 | -14.18008 | -45.34793 | 2025-07-24 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b467a551-2b0e-3153-a614-1c68ae629406 | -10.71451 | -48.85703 | 2025-07-24 04:42:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e02759b8-18c6-3591-897b-3f8855122297 | -13.21969 | -51.08065 | 2025-07-24 04:42:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2733714-56bd-3efa-9fdc-2d8ad2b52627 | -8.47997 | -49.5521 | 2025-07-24 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 20e86405-9d1f-3d31-85fd-67ee7f468512 | -10.04587 | -59.09474 | 2025-07-24 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05c4682a-2044-3a3a-bfa2-92ed623ad781 | -13.09628 | -52.14269 | 2025-07-24 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aca62c2-2873-338e-95ef-79ca5208790b | -10.17784 | -50.22305 | 2025-07-24 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7687c0c0-6f64-3822-9f72-55bb7a18e785 | -12.57704 | -56.97209 | 2025-07-24 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff0fe50d-5abe-3a64-b864-580c3536f4b9 | -8.29609 | -55.10235 | 2025-07-24 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e373481-2d05-32bc-bcdb-0aa680e4dd88 | -13.70952 | -45.6918 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a5e5926f-3908-316e-b4db-b1ab17ec2296 | -10.62979 | -45.23437 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d7ccdd6-09d8-32ba-ba70-aa96839228f5 | -13.71302 | -45.66538 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 733de9af-7855-36d8-9552-ea892616edcf | -10.62165 | -45.23326 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 25b684c5-a3cb-3783-9dfb-4ddaa01a3026 | -9.53248 | -63.62823 | 2025-07-24 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2079484-8bd1-3b66-a8e5-688d0df53e37 | -13.70328 | -45.67553 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2a28530-c5fb-3e9b-b4af-f1adced48df3 | -9.53122 | -63.62656 | 2025-07-24 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c87c19b9-1556-3c53-874b-37f9d116a7d6 | -13.71002 | -45.68804 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05f0380c-2632-3c18-9c99-8897176f6282 | -10.96627 | -49.57614 | 2025-07-24 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52c9757a-b192-332c-b5b1-1b6d072d96e4 | -13.70278 | -45.67931 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb76ff54-26d2-3675-a7e5-7d328a92ce73 | -13.70541 | -45.6912 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e0b6b69f-775f-34e4-9672-d01039a315ef | -8.49717 | -47.23452 | 2025-07-24 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 364823ea-cc90-3af9-8805-2e0fc23e6f4e | -9.32578 | -49.11161 | 2025-07-24 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03fdb926-d837-3fbb-a525-aa98f769427b | -12.57983 | -56.98119 | 2025-07-24 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 195a613b-1d05-3454-8136-9c2a9b6485d2 | -8.30341 | -49.03564 | 2025-07-24 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3280137a-6aee-3279-b554-b8608dd2f404 | -9.32347 | -44.84986 | 2025-07-24 04:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b491b04-0ef5-341a-90bc-c862639d8281 | -13.70065 | -45.68004 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d40d4c65-5eca-356b-ac55-f7f34067141d | -12.49508 | -57.77174 | 2025-07-24 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d880de6d-1e9e-3e2f-8baf-237c5dfa1139 | -12.49423 | -57.77641 | 2025-07-24 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b84042b0-6f72-3607-bb90-fc90f1900e10 | -9.32756 | -44.85046 | 2025-07-24 04:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58c297ae-f14d-3720-9363-87c0b1e2fa58 | -10.0395 | -59.1001 | 2025-07-24 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cee74a45-7fe7-39f9-ac61-af9cdb890a73 | -14.38342 | -47.76527 | 2025-07-24 04:42:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 506fa207-81fc-355b-b343-f8c888fbf45c | -7.45209 | -57.66634 | 2025-07-24 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b61135b-4ad0-3399-97bb-d2c35767473e | -10.6252 | -45.23743 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0dc4b47a-c9c5-3f4b-9604-cdb68d31ca9d | -10.19878 | -48.89824 | 2025-07-24 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21b7aebf-a393-342b-97c9-48e00d18b98a | -12.25272 | -44.7823 | 2025-07-24 04:42:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9804261-22a3-3819-b6e9-ddb57c0cbd96 | -8.48051 | -49.54862 | 2025-07-24 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e866e6d3-9dbc-34f9-ba55-26cf2fa4aeb6 | -14.17813 | -45.3543 | 2025-07-24 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 417eb3d8-761b-3fe0-ae4e-07e45830a58e | -13.70635 | -45.66933 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7da37120-a762-3a1b-a74d-4481afc80c8f | -11.46494 | -48.1596 | 2025-07-24 04:42:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b4c26ed-3476-3674-8486-0883b4f894ee | -8.48329 | -49.55263 | 2025-07-24 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 07582936-7fc9-3bfe-943f-66c26815d3aa | -12.58058 | -56.97705 | 2025-07-24 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4ea15bb-5c58-3cc7-8fbc-55fdeafc4572 | -12.42816 | -45.38025 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59ec8567-0dfe-366f-9b6a-7bebf3a6ffa5 | -9.58654 | -46.32098 | 2025-07-24 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9e2a0f5-fe8e-31d6-aab8-31c62f1e659a | -9.59791 | -43.87161 | 2025-07-24 04:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c4275b06-bcf2-303d-82d5-0a47ff37df64 | -7.27083 | -60.17843 | 2025-07-24 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c81f0ad7-612a-3acb-9991-89af3ad62885 | -8.36502 | -51.07662 | 2025-07-24 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6567c25f-703a-371d-8cf2-b65cc0abac53 | -14.20812 | -43.95073 | 2025-07-24 04:42:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6ae34a4-95b1-3e23-959d-aa797444598c | -14.30553 | -43.80135 | 2025-07-24 04:42:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32f89e84-097c-3f61-a8c8-ddac9ca23929 | -10.84833 | -61.9678 | 2025-07-24 04:42:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62060eae-791c-30eb-ad94-38936c95409e | -9.66654 | -48.52507 | 2025-07-24 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bcefe841-d078-3a7f-80e0-fbcdb4527dc0 | -10.11805 | -57.77137 | 2025-07-24 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2a839e5-c1da-329f-a676-63eb25a73af9 | -13.64924 | -45.7184 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78cb8009-41f7-3e03-bb91-e728cd96750b | -13.70372 | -45.68815 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9f13c74-6669-364e-b218-f57d4718a65b | -7.45645 | -57.66634 | 2025-07-24 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e024608-caee-33ba-92b0-c5fc6008736d | -15.26828 | -42.25466 | 2025-07-24 04:42:00 | NPP-375D | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 293406a3-2e0c-39b8-bd8e-f3f1c3f91478 | -13.7079 | -45.67237 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5090df1e-f4ae-37d4-94e9-cb293d11ec80 | -9.0614 | -45.0634 | 2025-07-24 04:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 703d3d80-ab21-3121-9e2c-d8fe8bba333c | -10.1228 | -57.77225 | 2025-07-24 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81a01008-0168-3b69-853a-36446edb06db | -10.71507 | -48.85336 | 2025-07-24 04:42:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91dbfa47-f8e3-303b-b5f7-4a1466db79bc | -10.71112 | -48.85649 | 2025-07-24 04:42:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a61f164e-0acf-3036-8ba5-917ea4dbd15b | -11.81227 | -44.27124 | 2025-07-24 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de0c260f-420a-3c2a-8465-400c9bb9dd78 | -13.70582 | -45.67311 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4cdb86a2-e2ea-31f1-bfa9-8c69e369e775 | -10.06793 | -49.69569 | 2025-07-24 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 067fce02-ab53-360d-adcf-144c96771b88 | -13.7069 | -45.6799 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 792f55c6-6546-31bb-a646-e8561dcf93a2 | -13.7017 | -45.67251 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27bc7609-3ee5-3c66-a0ef-9444c4874a75 | -11.87502 | -55.4553 | 2025-07-24 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41b5bae6-4425-3ca5-bf3c-c03095431e41 | -14.10058 | -46.34083 | 2025-07-24 04:42:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c5f9656-886e-3277-a253-9d598ba733a7 | -13.7084 | -45.66858 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81f41955-0bac-34f4-9c56-544aa5364ca6 | -8.36781 | -51.08074 | 2025-07-24 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab19eba4-a1fc-363f-aedd-c7ff7e278f0b | -8.49777 | -47.23057 | 2025-07-24 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02f2dd9c-8450-3c74-97ab-5c25682604ff | -13.70118 | -45.67628 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd414f3d-55cd-3dc0-857e-3b6594065057 | -9.32523 | -49.11516 | 2025-07-24 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87d2e230-12d7-3be7-95b6-cc9a57ece59c | -9.16823 | -60.83424 | 2025-07-24 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e3efea4-2bf6-3ea2-ad49-f42af931570d | -9.73232 | -48.02169 | 2025-07-24 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e09e0f44-0d22-377c-ace3-37a5e731d127 | -10.847 | -61.96955 | 2025-07-24 04:42:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be01dc63-29ef-3802-a681-8f23fb3233aa | -10.62468 | -45.24103 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dedb3cf2-d90e-3379-b706-1b12c7b03d1a | -11.80787 | -44.27061 | 2025-07-24 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad6f09fd-6c83-3734-a7b8-8041000e1d01 | -12.41938 | -45.38283 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README18.md)
