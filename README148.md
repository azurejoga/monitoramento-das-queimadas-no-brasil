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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c94c5cc4-75af-30a3-943b-a1f8897a4f37 | -14.20299 | -46.13521 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 21b0079d-529d-32d9-bd88-7079d0ccde26 | -15.60805 | -46.90761 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f73456c9-1726-3fd5-ac3d-8b80d5a7cbed | -11.92664 | -47.86689 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 379.9 |
| 5525834c-dcb7-34fa-90c1-130a90143a87 | -13.0605 | -49.15187 | 2025-10-02 12:38:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9059d298-b7a4-3dcd-aae8-f4e34fb62285 | -15.22835 | -48.73412 | 2025-10-02 12:38:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ec05472a-2381-3a0a-a117-171393507e4c | -14.64957 | -48.12231 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 55f2ab35-7693-34dc-9325-74ba29f746be | -12.39556 | -44.99712 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f0386628-df7f-3fe9-801b-4704a131b7cb | -13.56033 | -47.29288 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ef914e7f-1495-3e69-9f46-71d02a0a4a74 | -11.67859 | -47.49514 | 2025-10-02 12:38:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| de084da6-2e4e-3978-ac52-22aadb9ccdc0 | -15.24831 | -47.8963 | 2025-10-02 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 1532b721-2559-3e1b-904c-dcb3e85cdaeb | -14.1924 | -46.66605 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 6385c22e-d38a-39cc-9594-257fbd2c65ce | -14.22234 | -46.08891 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 33352c3c-d640-3222-88d9-b3b06421160e | -12.67461 | -48.57486 | 2025-10-02 12:38:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 3d32db1b-9a90-320a-9bbd-8300107d6c67 | -15.32217 | -45.04875 | 2025-10-02 12:38:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 552696a7-fd93-35cd-9018-984d507b8ad8 | -14.69418 | -48.2488 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ca416211-e518-3a91-b8fe-1a886dc91665 | -11.91648 | -47.87545 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 153.9 |
| e06d33a0-2d0e-3c7e-8854-4d95156d45d4 | -11.59876 | -47.6539 | 2025-10-02 12:38:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| cb8d5c31-dc68-3f97-8926-383f68576538 | -13.57553 | -51.88084 | 2025-10-02 12:38:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ffec3c6b-90ee-38d0-a038-746dd4106a90 | -14.46838 | -48.40636 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 3c4d92e4-5c22-3112-900f-aee64f14aada | -13.79194 | -47.54618 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 130b23d7-7c55-3e48-8ce7-d791de16e9ad | -12.95147 | -46.36999 | 2025-10-02 12:38:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 07ea0f90-311a-3de4-94be-e39a172447ed | -13.79126 | -48.05943 | 2025-10-02 12:38:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| bd0cbd2f-87db-3a29-82ff-6d60995a0fd8 | -16.03413 | -50.85635 | 2025-10-02 12:38:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 1d8ac49f-9a39-3926-90ef-0c6a48ecbe8c | -13.79398 | -47.52863 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 346d7759-1647-3ecf-a8e3-abe030128554 | -13.52275 | -47.26582 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 49180e21-90dd-35ac-a550-1755970e9245 | -11.61627 | -45.04573 | 2025-10-02 12:38:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| eb3f9ce1-5672-3ade-aba7-2fc82b86bafa | -12.70776 | -48.57993 | 2025-10-02 12:38:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 56805da4-7904-38c7-9fed-79fdccbe0cec | -12.71901 | -44.94772 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| afda662e-36b1-31d1-ba14-99e0367247d5 | -10.68141 | -48.56931 | 2025-10-02 12:38:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ca097f50-c947-36c3-b39e-5a70e4ce5ef0 | -13.97325 | -48.13365 | 2025-10-02 12:38:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 47.7 |
| d1e9abd9-f392-3b6b-a73e-42cd0ca1d19b | -13.97753 | -48.12815 | 2025-10-02 12:38:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 448b53dc-96c2-3888-a7c6-569b4529d714 | -11.05898 | -46.62465 | 2025-10-02 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b9ec1313-4696-3d22-80e0-37fd5e40f31d | -14.48741 | -48.44203 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 39f8d520-5eac-38b0-b450-a9b6113971fe | -12.27891 | -45.38644 | 2025-10-02 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b355a18a-6265-3f09-a30d-b1e2437ae8d8 | -10.9754 | -46.66673 | 2025-10-02 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| c1e7cd7b-e33d-32ce-9b70-140a96766177 | -16.49837 | -46.62273 | 2025-10-02 12:38:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 831791b1-52e3-3399-8afa-a0698d07533e | -11.61847 | -45.05169 | 2025-10-02 12:38:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 9a8688b6-9413-316f-840b-92fb8eb82195 | -12.26698 | -47.81324 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 568b265c-4f7c-3a0d-b63a-7bf1879f9131 | -14.7692 | -50.53556 | 2025-10-02 12:38:00 | TERRA_M-T | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 38.5 |
| b47b272e-61b5-3cff-8842-f4bc59731ba7 | -16.00618 | -50.90561 | 2025-10-02 12:38:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c3fd4c92-8da7-3925-a8d1-796456d02dd1 | -14.30875 | -45.88128 | 2025-10-02 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| c25920d7-1f11-3bca-8725-396a5354f5d8 | -14.20689 | -46.16524 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 44.5 |
| b8766334-fdaa-362e-9f57-a9bf36dc366e | -12.81062 | -47.01118 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 801c3317-d0a5-3f90-90ab-6e9bdce55ef9 | -13.22718 | -47.34155 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| e4744206-1b01-3538-8610-70cb7af7f9ad | -13.77623 | -51.19994 | 2025-10-02 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3597f9cb-5daa-3abf-aef9-805ac270cbb3 | -14.48654 | -48.43161 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 00634c08-281b-3f5f-b28c-9c7cd8d7c7da | -14.47598 | -48.43988 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 296cba84-3ad4-3322-b69a-728a9f2ec052 | -14.19314 | -46.16343 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 143.7 |
| eca72e6a-d22f-3a3b-aed9-0bef3cacb99d | -11.60188 | -50.17007 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4fc3494d-0c86-3521-8176-0815f434a858 | -13.87094 | -51.25089 | 2025-10-02 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| e82b8c12-2b51-3e90-9008-7cbfa7407584 | -12.65646 | -46.88298 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| f5875498-3ef8-37b8-a60d-54f43be8355e | -14.18913 | -46.13418 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 9ba15d82-bd51-3e5e-8611-0e2e04952aee | -11.84554 | -47.68486 | 2025-10-02 12:38:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b97b9bdd-95fa-393a-93c2-cb617e2e3333 | -12.92901 | -45.09578 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 406e0b7b-d4b3-3569-8fd0-321497ae8856 | -15.24622 | -47.91418 | 2025-10-02 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 235d4fa1-b048-3a9e-b645-77f341d3d522 | -16.04946 | -45.73383 | 2025-10-02 12:38:00 | TERRA_M-T | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 401.4 |
| 512e370b-b241-3802-9ab8-f6be7714ff4e | -14.41406 | -52.13885 | 2025-10-02 12:38:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 717f58d9-0b14-342e-9eb2-42c78558ef39 | -13.36186 | -48.09512 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 2e1acc3b-03df-3dce-9e2a-b8461a2dcb93 | -13.16232 | -47.8726 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 4ef80620-5fc9-3284-a6f0-922cd0a03d1e | -14.81944 | -56.42686 | 2025-10-02 12:38:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 89af1123-7e40-34e1-89bc-16e0b5676bd6 | -15.15408 | -48.39176 | 2025-10-02 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8e2b2872-2183-3ee2-b5e3-d8201931b385 | -12.27514 | -45.38047 | 2025-10-02 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 2f32a2d8-9307-3688-b6c9-1b1849af0675 | -14.58328 | -48.3115 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 866276ac-da90-3d17-930e-96b2854b176c | -12.659 | -46.86214 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f4b3c78e-5a42-3012-a379-79727e594703 | -11.85993 | -48.0437 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 58100ac5-b6ba-347c-80d6-47fc06d88b49 | -12.94377 | -48.43349 | 2025-10-02 12:38:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6612dc27-973d-3430-8332-9b24c048d103 | -12.94887 | -46.39239 | 2025-10-02 12:38:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f91bd605-74ed-3a42-af61-cd810568992d | -13.3183 | -47.58965 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 556b76e2-42c9-36f0-8f92-285dc9dcc204 | -14.70421 | -49.62574 | 2025-10-02 12:38:00 | TERRA_M-T | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 5b8c85c4-bcda-3227-a394-46419389be71 | -15.26174 | -49.30426 | 2025-10-02 12:38:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8a6ed284-3f91-3a91-a910-5689629e92de | -12.91064 | -47.17056 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b1da07e8-1f7d-34f1-9ad1-ea1cade49e6a | -14.60063 | -48.33658 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| c41a6fd0-c71f-3c1b-9117-c072b740b374 | -12.86215 | -47.02302 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4d036fc2-a4a8-30d4-a67b-9f40b5239340 | -14.92206 | -47.22979 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 32a5c318-80ea-3c35-87dd-70d75a4c58fc | -15.60558 | -46.93014 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 9a49634f-773e-33b7-880d-730a68f5e445 | -14.68989 | -48.25317 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 919788cf-2101-384f-957b-8a6c8cef2a37 | -13.20207 | -47.84257 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 80bfe943-8114-3ea4-b25f-ff11b2fb7195 | -12.49882 | -50.26181 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 46a20204-cec6-3419-950c-bcf41093f3eb | -10.64536 | -48.50882 | 2025-10-02 12:38:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5c52646c-2a97-3880-97f0-a9357fab9cf9 | -14.65685 | -48.26221 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 188a978e-b58c-3b2d-bd0a-12a3d14001c9 | -14.6025 | -48.32052 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 0e7515c6-f698-3717-87d8-851e269cf92f | -13.87191 | -47.95259 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c2c2a416-368d-37c3-bc58-8eb9c93d8ced | -16.18731 | -45.13575 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 7ad2c7d3-eb62-3541-8c7d-192b7e1480ea | -13.21046 | -47.83322 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 618de845-3027-3153-8192-4ebedb474809 | -15.36679 | -47.08583 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 0cff8d11-6a8e-3bc5-9eeb-82be7e1ea85f | -13.80421 | -47.54748 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 79522fc5-e2aa-37dc-9628-ec08d6dd0f7f | -12.90871 | -47.16389 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ab7ef0e5-2265-3787-85e3-7abdd85e40c6 | -14.81723 | -45.82 | 2025-10-02 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 177da482-96db-3271-ba78-eeb311e3ef12 | -14.75928 | -50.53424 | 2025-10-02 12:38:00 | TERRA_M-T | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a06c468b-21e2-37ad-8564-749ae091a254 | -13.77964 | -48.05698 | 2025-10-02 12:38:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 27c5efb2-2c83-360b-bf58-897d8fea5d19 | -14.31299 | -45.88846 | 2025-10-02 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1968302b-ede4-3a24-bdef-fe6335d9565a | -14.92004 | -47.24329 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 4956cef8-3036-37eb-959b-396f65c31a71 | -10.93427 | -46.67418 | 2025-10-02 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a623de10-8c5e-3346-b54b-adfd8ea28775 | -13.23032 | -50.90171 | 2025-10-02 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8308f28c-6213-399f-a5ad-0ebb5e5e4f3c | -11.04035 | -47.82396 | 2025-10-02 12:38:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| fcd075a2-547b-38bb-93dc-8b68264f3de6 | -11.19448 | -47.77466 | 2025-10-02 12:38:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 526a9de6-34d6-3949-a2f3-06a23434654d | -11.27623 | -47.85428 | 2025-10-02 12:38:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 5c06d731-77b7-3afc-8ba1-e57389b3aca9 | -13.3436 | -47.34152 | 2025-10-02 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4fca1d1c-9793-3c34-ad85-37c66f0f7c75 | -10.86435 | -52.09882 | 2025-10-02 12:38:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dc744c24-f1a5-37d1-ab47-70e4369c55ad | -14.92246 | -47.22301 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |


[Clique aqui para ver as próximas entradas](README149.md)
