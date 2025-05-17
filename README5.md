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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4baaf157-51d0-3cac-9010-10990d0f691d | -6.70295 | -42.13034 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5c5dee6d-a6fa-3c83-bc94-4e4101b2e4c8 | -6.71976 | -42.13295 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 87e9a0e3-3eb9-388b-8e6b-e2a9526056db | -6.72032 | -42.12939 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ff87edcf-7553-3d80-9997-0dff0671e4c1 | -6.71585 | -42.13597 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d47a974e-c98d-36e5-bdd7-189472546ed3 | -6.71696 | -42.12887 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3141817b-5879-30d8-ba01-72768c2b262a | -6.72088 | -42.12584 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 80caa4fe-ded1-37a9-b063-57f8b431b9bb | -6.70351 | -42.12678 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5f6d5b64-b23f-32ef-b716-ccd6f5feba87 | -6.84289 | -42.79365 | 2025-05-17 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c17bb77a-856a-3fd3-aacd-492b481386c1 | -6.17421 | -48.06276 | 2025-05-17 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 602e9770-09cd-3857-885b-5a4187803876 | -6.17017 | -48.06213 | 2025-05-17 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f99c3b77-15cb-3e8d-b7fe-606fc924a66d | -5.10064 | -44.79793 | 2025-05-17 04:14:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 174987d4-8573-3625-8eca-efd17c3d09c8 | -6.84677 | -42.79068 | 2025-05-17 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 09957f1b-da3a-3a69-a565-a2221d70ac83 | -6.71529 | -42.13952 | 2025-05-17 04:14:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 444b116e-52e4-3a0d-8a35-3e88366991b6 | -6.7164 | -42.13242 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1f455402-b2a1-3812-a4eb-65c0274bc1d8 | -6.72368 | -42.12991 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b8498c8d-3499-31f6-834e-7e359e165722 | -6.7248 | -42.1228 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| abf6366c-2ad7-3847-9653-c9bd20b666b3 | -6.70687 | -42.1273 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| be62be63-b9bb-3e45-a6da-91dbbae7b736 | -13.31637 | -47.46479 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad5637cd-d2f4-3ba4-b380-9821c3b95ada | -10.63873 | -48.09087 | 2025-05-17 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| df173843-7491-3191-9c64-7a0e9c0dc9ef | -11.35784 | -52.95607 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19f41bc5-2c7e-3a75-b16b-c2bf5a7ede7f | -8.33622 | -48.01585 | 2025-05-17 04:17:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4928fa57-cbdf-3574-9ce0-ad0b9b48cd29 | -11.66451 | -54.93934 | 2025-05-17 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| debd933d-154f-3e39-a3f1-2ee36ed5f691 | -19.12352 | -54.45962 | 2025-05-17 04:17:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a22b8b2-5061-324e-928e-55754b6852e9 | -11.36352 | -52.95402 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f731aaa3-2054-34ff-8ffc-6ee01a458e2f | -13.31449 | -45.38453 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b71bc52-6422-3a40-83b8-b4e37d74fe62 | -13.31783 | -45.38508 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a0e23a6-fc8a-39d1-bf28-3b44d43914be | -13.39942 | -47.50381 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e524fe4-3753-3f25-a8b5-5039b321d9ca | -10.02657 | -48.69899 | 2025-05-17 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8e1da65f-8399-3da4-b313-c6487b84f546 | -9.3076 | -44.82714 | 2025-05-17 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68cf9978-d29f-3dc1-801a-5bd85f3f985e | -18.90134 | -48.32539 | 2025-05-17 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b93b3cfa-29bf-3c9b-9dd4-7ad185cb5f1b | -18.65866 | -47.85614 | 2025-05-17 04:17:00 | NPP-375D | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05df15c0-e780-3d3c-8441-0844183d1deb | -13.31287 | -45.37324 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93240518-547b-3ef4-b657-be3f0e9f94c0 | -13.06627 | -47.82409 | 2025-05-17 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d45443b7-e4cd-3625-9b69-d94e1c84c577 | -12.30096 | -52.46768 | 2025-05-17 04:17:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78dbc49b-297f-350f-be25-a77150368513 | -11.43855 | -44.71877 | 2025-05-17 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 282bfc01-7ff5-3a13-b035-10f6b81ad2e5 | -13.32278 | -45.39693 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1fb5a8a-2d1e-39cd-ba3a-50f65b54e5ab | -13.06462 | -47.82573 | 2025-05-17 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3b63e2a-0e00-381f-842a-80e521e7f901 | -17.26959 | -49.00801 | 2025-05-17 04:17:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 98dad9db-c191-3f06-8816-7753e1146770 | -10.47822 | -49.1426 | 2025-05-17 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30001059-9572-3663-b1e5-ffe302aaef43 | -8.33705 | -48.01091 | 2025-05-17 04:17:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2abe13c-8b75-3ff6-816b-4f85c6a880ba | -8.92273 | -36.70065 | 2025-05-17 04:17:00 | NPP-375D | PARANATAMA | PERNAMBUCO | Brasil | 2610301 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 315e38bc-e6ae-3557-a331-3d1df5c161af | -11.42138 | -54.31553 | 2025-05-17 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dac1143a-12bf-3aeb-b6c0-6ab9634428b9 | -13.0492 | -53.71734 | 2025-05-17 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae5e8a1e-8162-39e1-8dfb-ba5c788cee43 | -19.8607 | -44.92765 | 2025-05-17 04:17:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 71596ae7-132b-31c2-b228-c4eb14581a3b | -13.30953 | -45.37268 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba3e4a73-6b25-3d63-ace2-40375f9587a7 | -20.3117 | -45.58387 | 2025-05-17 04:17:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa5085a2-0375-382e-8736-684a2580352e | -12.99487 | -46.31897 | 2025-05-17 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71361e34-df47-326b-9ae1-4506cdb222e3 | -13.30009 | -45.36744 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3df63838-db46-3ea2-868e-39171f1a0c28 | -13.31334 | -45.39168 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1aeb655c-91e9-3c0a-b520-4a4770ad835e | -11.79555 | -44.28431 | 2025-05-17 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 335ecf30-c348-35e3-8ae2-006ed9aa4a98 | -13.50315 | -47.39767 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc762240-a859-3203-b4ab-908fa90081df | -10.03052 | -48.69973 | 2025-05-17 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 63faa88b-c1f7-3725-94e0-1d8fa8cb385c | -13.31068 | -45.36554 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| addcb3a5-ccd9-367d-9210-9ee291ea11a2 | -11.58419 | -47.61915 | 2025-05-17 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4616dd0e-99a1-3fed-aa7b-86d6cc5fd9d8 | -17.7787 | -42.80985 | 2025-05-17 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd8a9626-5aa6-3001-95ad-4f04808f36ed | -18.95512 | -52.24258 | 2025-05-17 04:17:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05633321-3244-3377-a67c-db113836b52c | -17.26596 | -49.00732 | 2025-05-17 04:17:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| df279e2c-174d-3643-8834-a2f7a69e7ef3 | -6.6264 | -48.01692 | 2025-05-17 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dbde126c-65f3-376f-9952-c79b9fe170bd | -13.04339 | -53.71937 | 2025-05-17 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 685d9051-5ac0-35f7-ba83-d118a5bbd299 | -11.58255 | -45.02195 | 2025-05-17 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8908598b-35f6-3a45-9ebe-d847c97763ab | -8.06695 | -47.12889 | 2025-05-17 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f924b00b-a8d7-3806-8df6-a970674ef3e8 | -11.78356 | -47.34911 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a3e24c1-a84c-3f74-8aae-fe35273d5f80 | -12.99531 | -46.31973 | 2025-05-17 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8a2d7e0-5182-3bb9-8606-72b3b5352b4c | -13.31277 | -45.39526 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50db03e3-d5f9-3d3a-982b-5735c4b17cc2 | -11.64119 | -48.02864 | 2025-05-17 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2670ca7c-d53e-3d38-a79e-455d01fcde9e | -11.78714 | -47.34976 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd7ffef4-4feb-3cb5-b4d7-cc2fd6fea342 | -13.32946 | -45.39806 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 997942d0-edde-3aad-8c7b-6464ec470ff9 | -13.4725 | -47.44981 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06d25538-f6e8-30bc-b734-a933fd3ec63e | -6.78738 | -47.59856 | 2025-05-17 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 038a6ec2-5c5f-3244-a839-967f2e70c018 | -13.061 | -47.82515 | 2025-05-17 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3d2a681-1e92-359d-839d-02c287a21b46 | -19.59746 | -45.01254 | 2025-05-17 04:17:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 811616c1-4fa4-30d3-bcdc-41e0a4e3cb0a | -11.15706 | -48.67923 | 2025-05-17 04:17:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e4ec823e-27da-3116-95ae-91a8d25a9c66 | -8.33316 | -48.01027 | 2025-05-17 04:17:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 641f5648-113b-3ad5-902f-bd9f3bae1083 | -11.64569 | -48.02479 | 2025-05-17 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97ebef3a-9ecb-34a6-b7ad-a99d53f69d57 | -10.50173 | -46.18753 | 2025-05-17 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65e7805f-beef-350f-82bd-89209704982d | -13.31115 | -45.38397 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c36314f-b97a-37e0-b28f-ab48e32e387b | -13.31553 | -45.39939 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9be5d074-2c0a-3451-9979-2ee3103479ac | -13.30838 | -45.37983 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2515b032-1dbe-3c50-a68f-f49d382aff86 | -13.31668 | -45.39224 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdf4af22-99dd-3173-954a-6970412beec7 | -11.57904 | -47.8689 | 2025-05-17 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfc3333a-d206-3a15-89d3-df52794c83d1 | -17.66399 | -46.68222 | 2025-05-17 04:17:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59c1ccbf-fd0f-3d36-bcef-8ea25debbb44 | -7.23346 | -44.71591 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fe0ecab-710f-356f-9ea6-fefb384fdd03 | -11.40224 | -52.94875 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e066e2b5-1cca-3cc3-a2d3-20c31cf1973a | -20.16789 | -47.84153 | 2025-05-17 04:17:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0acc45fb-2b16-337a-b104-252df42d8a1c | -19.24655 | -44.28347 | 2025-05-17 04:17:00 | NPP-375D | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2425e3fa-a803-3e90-82d3-79968c5e12e5 | -13.07133 | -52.01903 | 2025-05-17 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d99cd69d-2f13-37e9-b74e-f86662709a2c | -13.58571 | -47.37781 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5555cbb-8266-3d38-8218-256844e88236 | -10.63468 | -48.08859 | 2025-05-17 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 923f2121-b7a8-3690-bc60-24216cac9b1a | -20.41674 | -43.55143 | 2025-05-17 04:17:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4c88ce5c-d7b1-3b28-88de-f502a3fd063a | -11.78644 | -47.3539 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69c0e8d4-6468-349a-9abd-46a2272fe777 | -11.79957 | -47.4076 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a19e71c-4ea9-3a15-befc-f4ad13216020 | -13.32059 | -45.38922 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da142af9-0dff-3594-a325-929872cfa166 | -11.33768 | -46.51262 | 2025-05-17 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb6c9936-9317-336b-a598-adb96a9eb11c | -13.39518 | -48.45849 | 2025-05-17 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 641ddda3-e171-3257-902f-c98eba55f187 | -7.71604 | -46.29431 | 2025-05-17 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3b34db6-dd0a-3dc2-80ef-b3729f1d2632 | -9.42136 | -49.33983 | 2025-05-17 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a42137e2-3d11-3503-a471-a85d77a20ae4 | -10.89932 | -45.08999 | 2025-05-17 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 261f21e9-e82d-39cc-af65-67b761b2d8eb | -12.45678 | -57.2001 | 2025-05-17 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54b80ec5-5403-37ba-a9d4-96368614749d | -13.30228 | -45.37514 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a58d980-862d-3a10-9a5d-20934269b48c | -10.47418 | -49.14195 | 2025-05-17 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README6.md)
