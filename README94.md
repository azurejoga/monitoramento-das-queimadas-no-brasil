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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58af7777-aa4e-316c-98f9-16ef00e8ee29 | -11.646 | -52.05424 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1378b3c2-4d50-3cc9-ae77-b27da2ee85f4 | -13.49293 | -47.0247 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8706ba19-f194-3d11-96af-45cba2db486c | -8.15186 | -54.69667 | 2025-09-03 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22e73ac4-7af9-36ce-8c45-6d95eb799dd1 | -9.63442 | -46.12769 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bc58d82-7477-308f-9a74-73f8c96f85ab | -14.3065 | -53.09212 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dffbf555-cc39-3928-919b-41744c7ac464 | -9.14628 | -49.66117 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72194853-b2f6-35d5-9038-7fdffa63316e | -7.34795 | -57.63681 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b579411c-8300-394c-89ce-b68b1f33c50c | -11.21776 | -55.06473 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 137b4244-c774-31a7-8c48-af1301549f7a | -10.96671 | -50.92505 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86813a76-a9a5-3608-8ef6-4e47d0ffce94 | -15.02791 | -50.04529 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d1bd453-6ff4-3446-b0f9-b58601e35d10 | -12.89457 | -48.05101 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f92d5efc-c24e-305a-bcba-268d745e90b4 | -14.57481 | -48.05265 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0c2df27-6c2b-31fe-829a-9caca13d65ec | -8.88768 | -45.82799 | 2025-09-03 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 74ead17c-5e39-3898-b23d-a7fdf6b06ca3 | -6.79838 | -59.87967 | 2025-09-03 05:14:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08abd93b-ad5c-3c55-9f53-295b3459b103 | -11.59855 | -52.11211 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 196616c5-48ff-3eaa-8714-2e960ea293e1 | -11.60824 | -52.13992 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6f05f443-4b88-3980-b2e0-aed8f040c735 | -8.05808 | -52.37082 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 899e0214-59a8-3bd9-940d-7bf1f9cffd05 | -7.70972 | -50.25169 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b6247e1-ccc8-3c26-840a-e6c99ad3799c | -11.60561 | -52.12633 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e5ed022-ddee-3636-a584-2c59a9577686 | -9.6536 | -48.07267 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e417a91-0ce4-3827-93a4-18b45c53605d | -8.12619 | -55.55855 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 481ddfcc-4580-3c31-9024-557785568e03 | -14.5465 | -51.94296 | 2025-09-03 05:14:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1df5ad0f-8aa6-3b84-8886-0ecc67d319ff | -11.85636 | -51.544 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1004d029-1658-3f61-bf32-1c3207d6f9bb | -11.60416 | -52.104 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bab8924-1f5c-3adb-a42e-a79c27911972 | -8.07618 | -47.60592 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93a769ef-117c-3118-87c4-f94f81357a91 | -9.63369 | -47.86377 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75dc90bc-2545-3c89-b0d7-834b51cee5c2 | -15.03322 | -50.04611 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e631e91-1e66-35fd-93e8-c2c38faed3ca | -9.42693 | -48.35898 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43db1252-f9f6-3322-85cb-790e19bab436 | -11.58412 | -52.11896 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4d218246-cc96-346b-b302-46ee40902c7d | -9.95374 | -51.64016 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74710dd6-bba9-31af-8ecb-99a387598550 | -11.60655 | -52.08647 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eb2296f-f6c2-3478-a1b7-da89b6563ab8 | -12.9769 | -54.7743 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d1259c3-e15c-3847-b28e-3a4c2469d6fd | -10.96738 | -50.91993 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 921ae516-941a-3dbc-b12a-788a20a7c568 | -7.70198 | -50.30875 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3ae046a9-37be-390d-942f-722cbcb2b954 | -12.89728 | -56.95223 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 667502ab-ec2f-3e4d-b12b-fa5eabdd055e | -9.25974 | -56.89465 | 2025-09-03 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8ff2a39-3ef7-31b5-acd2-1cd3196e35cc | -10.48799 | -53.65061 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1f987c32-8007-3a06-8b3a-17a277f28769 | -14.99069 | -50.06064 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 148b4bcb-224b-3fea-a3cf-1f531d166101 | -9.4012 | -48.04823 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01c84212-e1e5-3639-aa69-d81003b75ea2 | -8.81319 | -47.81155 | 2025-09-03 05:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac48e28b-e271-306d-bbab-edb18113f3d0 | -12.92476 | -57.0029 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46c2fbc4-369c-320d-beb6-271870648a52 | -13.09894 | -57.11789 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f6c89cf-7e2c-3605-9914-1e6bcb995b5b | -8.04746 | -52.35717 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f30ae9b-ce73-3520-96be-42ded7d1d835 | -14.61254 | -48.09871 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ef585c0-eb95-38c2-9bd6-99843fe87aaf | -11.60333 | -52.07703 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9cbaed2-45cc-3e96-983f-978d5454f34a | -12.96414 | -48.071 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79b0a5f1-f0b4-3253-a9c7-c572a9f57814 | -14.9801 | -50.19232 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23ace45d-2713-337f-a5f8-3da495be2a33 | -14.81427 | -48.34659 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7708f79d-2095-3d29-85f0-14b1ffc415aa | -11.31363 | -55.2215 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 494c06c0-c0b4-3d6e-8d41-e129ec8779c4 | -12.99304 | -48.11618 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd778f9c-10c5-3e1c-8876-727debadf7d4 | -14.97149 | -50.20874 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1413b76-451c-3a82-94e0-a9dc5e6f7e0d | -9.63511 | -47.03419 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46df121a-1670-3196-a2a8-ac2ee596f904 | -13.31261 | -51.77601 | 2025-09-03 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0defa6cd-f022-3daa-ad6e-4e93efd4f90b | -10.46457 | -53.62486 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e026d2a1-28ef-3033-8ba7-9a0c6acdb531 | -8.38151 | -48.31067 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 481dce2b-b774-3af4-b45c-662701582b6c | -10.94222 | -50.77843 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad850a1a-5ef6-3fcc-a5f8-ecc4c06f6116 | -14.30169 | -53.09552 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85af5a05-3024-3a6f-b933-3eb73cffaacf | -12.94359 | -56.9943 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4723767f-dcb8-3162-adcc-5b5e7503b4f5 | -8.54243 | -51.31278 | 2025-09-03 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8fd91f40-4927-3b51-8f7f-e0a76675daa8 | -13.28468 | -46.83263 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99e96d4a-1079-3bc4-8114-dca4d7ac2fb3 | -10.05899 | -48.08588 | 2025-09-03 05:14:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2185f6e7-6025-3c6e-8a6f-c2ffe3095be7 | -9.64664 | -47.85341 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 935c7827-c8dc-3752-9d5b-68955678f564 | -8.38487 | -48.28589 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cdfdadc-bb83-3b7f-a256-e3a939e134c8 | -12.50017 | -53.83631 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27a8bc0a-8cd4-30ce-b4d3-2ba032a5845f | -14.97364 | -50.20137 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f79eeadd-3693-3b9b-919b-96ef8e1bf14b | -9.95051 | -51.63077 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c077897-04e6-3f48-b129-4357b336befd | -12.94357 | -56.97117 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| caf4a830-39e7-3d25-be5f-0a4f56e4502e | -11.84685 | -51.4174 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a5fe81e-336e-3c1f-995a-ef4c5bb99181 | -7.72941 | -50.24905 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25fbe522-1843-3304-9922-7909fbe3e9a3 | -12.64251 | -57.00248 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a34c609-46e7-3f6a-95c4-4a00f9adbd3a | -13.00854 | -48.10021 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d574177-ee46-30fa-b19e-979a75163e9d | -10.47116 | -53.62763 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aa99bb6-a6a1-399a-b050-60420f3ee4b2 | -14.57822 | -54.55269 | 2025-09-03 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2f93ca5-6610-3c01-9332-b1a4f671a6d1 | -11.59443 | -52.14238 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 48fe88b2-aad5-346a-b0e3-a2437840554f | -12.48336 | -53.82708 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a4eee68-302b-335e-93e4-6101edc87aa4 | -11.80114 | -48.35921 | 2025-09-03 05:14:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d7de1a4-6e29-34d3-a19b-286999ad767c | -11.62783 | -52.06293 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95706cc3-1420-3f05-9de2-ef9faedb7b66 | -14.99361 | -50.06162 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8429a525-721c-3818-a224-226fafa4e7c8 | -12.91905 | -56.99428 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7103af64-edd4-3c16-9dcc-c4f56f987cd0 | -14.58018 | -48.04897 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7aa813c3-5635-3ed0-b215-7a866ab544bc | -13.0062 | -48.10555 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a36465e-feac-3294-8d0c-76bbfd1aac2e | -14.34338 | -52.80511 | 2025-09-03 05:14:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a83ed3a-f2dc-3884-a9ac-a21abeab170c | -14.58075 | -48.04394 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd3e7809-eb2a-34c5-85c9-3e4d1d52b642 | -8.09529 | -47.593 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ad2a997-761e-38b0-b709-ead76817acc0 | -11.66467 | -57.35695 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62498c62-e964-39f5-8e14-d3209582d714 | -13.27792 | -46.83513 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b8466e6-651c-3664-88b1-959001afa21c | -11.41586 | -55.18259 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db10f7cb-38a2-3913-b41b-ccd70a87c051 | -12.62713 | -56.98856 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed18bfb5-31b2-3e73-b689-086100642bf4 | -13.44771 | -58.07307 | 2025-09-03 05:14:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a197e5f6-57d0-3731-91d2-00b3e4ffe8c2 | -9.33361 | -55.22538 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4052e961-7044-361c-8d76-d597d03f6953 | -14.60908 | -48.01817 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 530fb6ab-e26a-3542-8797-4b28a1231144 | -9.94667 | -51.62571 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ab4c8ac-92c3-3a1b-bd06-3d3697959e1f | -14.58674 | -48.04505 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 86c75c51-36bf-31bb-890f-b27bc89225e7 | -14.56686 | -48.05873 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bfba9d9-e564-3b22-9458-f960fad8adeb | -14.06524 | -54.01593 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d777a37d-c028-34ff-b3fb-cf38ddbaba94 | -8.85831 | -47.92525 | 2025-09-03 05:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 449ecd74-35d0-3156-b204-d8bdd91fff78 | -14.78155 | -48.14605 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 083ba352-2dbf-3d3e-8f25-d2cd7304a3db | -9.42186 | -48.35471 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d0d8746-5cb9-3249-81bf-1a56d39967e7 | -12.62599 | -56.99606 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 715fec5c-2a9d-3b11-99a2-3220e97d6d5d | -11.1955 | -55.01285 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README95.md)
