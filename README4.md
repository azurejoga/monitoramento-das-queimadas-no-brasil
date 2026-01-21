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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acda3aa2-ebea-30de-a154-27a505a6ed95 | -19.44146 | -57.27295 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e500f553-c5d9-3ccb-8cab-3b762c44d795 | -18.59518 | -55.94558 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 632eb6ef-de16-3605-9c38-d4a4852bbbe6 | -16.17134 | -57.95114 | 2026-01-21 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ed8ecce1-ba55-3a41-8618-54f8f9925df4 | -19.44253 | -57.22451 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2e85a881-4c0e-33ae-b931-fcb2a9fb7bcd | -15.97229 | -56.27633 | 2026-01-21 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5af851e6-175d-3491-91b8-a66dd4fbeedb | -19.44818 | -57.23444 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 1d286e63-d735-3e68-8872-a680446c104a | -19.44445 | -57.25582 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7a38e957-c9c2-3205-bdf7-a45dc6cddd06 | -20.10245 | -51.24145 | 2026-01-21 04:53:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 45e5f4a3-ed4c-33f8-9922-6e193ed0262f | -15.97157 | -56.28049 | 2026-01-21 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f26a5447-e01c-3e19-8b45-26619f41387a | -19.38909 | -57.27603 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| cac127e0-cdee-3e39-a506-dcd10c5026a1 | -19.21192 | -53.44265 | 2026-01-21 04:53:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b30d670a-2cbc-313b-9e37-ed65d2782512 | -15.97003 | -56.27729 | 2026-01-21 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8d450b1b-f5fd-38da-b449-a3bb0a6f94d6 | -19.42975 | -57.2132 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 789f5b58-465a-32e5-9a5f-e61367c6e922 | -19.64493 | -56.93708 | 2026-01-21 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 02b19f67-6373-35b7-8770-f3f44ca0beae | -19.29501 | -56.50792 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e8665fc3-5b0b-38f4-8b6f-52fb1996d8a5 | -19.17314 | -57.54353 | 2026-01-21 04:53:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 85dbaf47-e238-33e2-9219-d8c23657804e | -15.97301 | -56.27219 | 2026-01-21 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7f35cbf8-d3a0-3b8a-8b88-2bf7bcd58f37 | -19.42696 | -57.2923 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e3f30ba3-9791-3c5a-a8c2-b45bd08c48d8 | -18.93811 | -53.39287 | 2026-01-21 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbae9dc4-ee4c-358b-b3df-25bdc1acc538 | -19.43788 | -57.27225 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 06f2f543-c8fc-3aaf-9e39-c7d90bd47fe2 | -18.59862 | -55.94622 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2b1fa1af-d338-3e53-b729-2d2d166ddbd8 | -19.42263 | -57.2959 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e35fe9f2-ae05-3ec6-aa2d-cec4c630edef | -19.44296 | -57.26438 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 825e3b34-24f0-3d08-b9e0-ca665273734c | -18.82019 | -51.6136 | 2026-01-21 04:53:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfdff3fc-4243-3ba9-8909-035262aca533 | -19.64141 | -56.9364 | 2026-01-21 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 4a6ae3e1-9e1a-3da8-8e22-45c71f039e6b | -19.17236 | -57.54792 | 2026-01-21 04:53:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 00dae849-a37a-37d8-9d7c-9e972a910243 | -19.44536 | -57.22948 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5b542c81-6655-3c09-ba41-acac9db5d6fe | -18.81436 | -51.6043 | 2026-01-21 04:53:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bc9b85b-ceb1-3886-8073-0624cd0e9aa7 | -19.43638 | -57.28083 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c7305b66-0da7-3284-bf68-f8cf37f4a531 | -15.96873 | -56.2757 | 2026-01-21 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c1a0a5a8-ccb5-3642-8b0a-c6f7036385b9 | -18.8237 | -51.61417 | 2026-01-21 04:53:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bac899a1-ef05-3226-ad0d-922e897139f8 | -19.21249 | -53.43897 | 2026-01-21 04:53:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 777e702e-2dea-3045-aee1-e4ded5c1ca79 | -19.1071 | -57.61805 | 2026-01-21 04:53:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| dc0a78ec-7394-3ba3-af1a-e2b86a81b126 | -19.4422 | -57.26867 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b7c50668-bf23-3073-a4f0-14e17aca6c46 | -19.43205 | -57.28442 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| fdf96dc1-ad13-3145-8f68-3d9405dc38b0 | -19.42772 | -57.28801 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 941c0f8b-29fd-3c6d-baa3-793246351260 | -15.97073 | -56.27314 | 2026-01-21 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3419c383-e2d8-3c67-952a-7554ba5c59eb | -18.93261 | -53.3964 | 2026-01-21 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f81ba91e-3dfe-3469-817a-95cd5396d8fb | -19.43971 | -57.21955 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f1367566-fd31-30cf-973f-604828953a52 | -19.38985 | -57.27173 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 09edf8c2-3a9d-3f74-add3-5f0ec0589cee | -19.41754 | -57.30379 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 53dc6fb0-093d-3740-9cc5-54b1acf59e26 | -15.97658 | -56.27283 | 2026-01-21 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a14c412d-f6ac-3725-8ecd-cac6f65c538a | -20.99271 | -48.84477 | 2026-01-21 04:55:00 | NPP-375D | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76312e79-7d97-3a36-839d-023c2bc7bc7b | -19.66336 | -56.95193 | 2026-01-21 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 44d3722a-4f88-3796-974f-a86b21127c9f | -23.60469 | -48.26095 | 2026-01-21 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 62ecb381-3b4c-3b91-9b94-c5db6403e6b6 | -20.32044 | -57.89384 | 2026-01-21 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 20a6d060-1e03-363f-8e0c-c5d10a78342b | -20.85584 | -53.75097 | 2026-01-21 04:55:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e674d1e8-0205-3742-a896-52137828f003 | -20.72854 | -55.15962 | 2026-01-21 04:55:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69e1c7c8-bd08-3d31-ac00-54dc667ff131 | -19.67069 | -56.88925 | 2026-01-21 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| aed0cea5-53c3-324e-b0de-3adcddc4e503 | -21.19787 | -56.92773 | 2026-01-21 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5c37a317-6d3d-348e-905c-92e687507a61 | -20.32772 | -57.89531 | 2026-01-21 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 09e36fe7-b034-330a-9b8f-4171a0fba85a | -22.01855 | -56.34245 | 2026-01-21 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50883de6-2b6a-3dd3-ade8-c603b33effe2 | -25.25569 | -50.20913 | 2026-01-21 04:55:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 47940cb8-2e66-397c-8195-08d038495625 | -23.6022 | -48.26311 | 2026-01-21 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7009fede-b6da-3c3c-aebd-fadebd40f01d | -20.7252 | -55.15901 | 2026-01-21 04:55:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f10f258-0a6f-3c99-aff2-f584d502cfe4 | -27.38327 | -49.25278 | 2026-01-21 04:55:00 | NPP-375D | LEOBERTO LEAL | SANTA CATARINA | Brasil | 4209805 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0711cfdd-4d3e-34fd-90f2-8a5d2baee6ed | -22.02129 | -56.34696 | 2026-01-21 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ab9220d-ef87-3012-9908-30cb697863a7 | -19.67772 | -56.89061 | 2026-01-21 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0c34147f-b409-349c-90af-144cce72d5d9 | -20.34671 | -57.8945 | 2026-01-21 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 9f525c8b-0dee-3621-aa20-a12b73c7f1e1 | -19.65912 | -56.95539 | 2026-01-21 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bf8e4f14-0e7a-327d-b636-f09f54fc9e3e | -19.677 | -56.89473 | 2026-01-21 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| da935c1e-cc94-3d4d-bf53-20bc1726b416 | -23.60668 | -48.26383 | 2026-01-21 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16d71276-89c5-34df-b36e-7aa1e84f1422 | -20.33579 | -57.8923 | 2026-01-21 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 5f34586b-63ab-341c-966a-b8526b131d2a | -20.90622 | -56.38622 | 2026-01-21 04:55:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1b4740b-c610-36e6-8acb-ba2d2b29d5a1 | -22.02194 | -56.34308 | 2026-01-21 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e348bf27-e904-377d-9320-9cf1b298c1f0 | -22.73182 | -49.34331 | 2026-01-21 04:55:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25bf2c41-6dd3-30f7-a8c7-0fcb1170c3ad | -20.33263 | -57.91022 | 2026-01-21 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ba1464ba-bf4f-3d09-87a0-321f1e810f88 | -19.66761 | -56.94847 | 2026-01-21 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c01e156d-e228-3010-9146-65c9b2184823 | -23.60273 | -48.25832 | 2026-01-21 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1ca5ed95-7592-3f96-ae3e-e7c312eed9ef | -15.35443 | -57.88789 | 2026-01-21 04:55:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54daa664-3c87-3063-99e1-2b74ea1fd958 | -20.34307 | -57.89376 | 2026-01-21 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e17a6185-be12-3ad2-a61c-1f2c04850d75 | -23.2916 | -51.20798 | 2026-01-21 04:55:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 296631f7-e154-3b98-8e2e-91769b97ec6f | -19.67421 | -56.88993 | 2026-01-21 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3b8469b3-c0d5-3ea0-99af-21d6ef0cbad0 | -20.84204 | -51.73967 | 2026-01-21 04:55:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e0d88d9c-1df0-3fd7-af07-6a9e9555ce00 | -22.83926 | -51.05991 | 2026-01-21 04:55:00 | NPP-375D | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e53a1402-a96b-340e-890e-95ca7bd30aee | -25.25974 | -50.20976 | 2026-01-21 04:55:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d273a5aa-598f-3580-b818-367dbf39c649 | -23.29225 | -51.20314 | 2026-01-21 04:55:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ef430868-33cb-38e7-bafc-f32ea43e2865 | -20.32408 | -57.89458 | 2026-01-21 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| feca380e-8018-320d-a39f-2951a45fb535 | -22.0179 | -56.34633 | 2026-01-21 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f75af0e8-61ab-3b15-ad89-ad8b58d46141 | -21.1944 | -56.92708 | 2026-01-21 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65d2b9cf-50d2-3b8a-87b1-4accbdc75852 | -20.33943 | -57.89303 | 2026-01-21 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ee4a8a41-b049-382a-a7b9-766aa0244b33 | -20.32898 | -57.90949 | 2026-01-21 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cd699f35-12c3-36f2-8930-763a6366baca | -20.34906 | -57.89721 | 2026-01-21 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c9112fed-5574-31bf-a4f0-e09866cc98f6 | -23.6072 | -48.25901 | 2026-01-21 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbca1ca7-166b-3998-8592-ca9f9ac3cc2b | -21.48719 | -56.13315 | 2026-01-21 04:55:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1101e857-6577-3541-ae88-9ed372f44dcf | -19.66689 | -56.95261 | 2026-01-21 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4a95c286-ae50-3e38-9b12-e31a19ea5829 | -30.13278 | -51.95892 | 2026-01-21 04:57:00 | NPP-375D | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 66b2ce7a-ab7f-3c45-9878-be844e7b278b | -30.90581 | -52.96474 | 2026-01-21 04:57:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| ba1758a3-c418-301c-9f4e-8dfd7683a4af | 2.90556 | -60.90079 | 2026-01-21 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d040e21-9cc7-3529-99ee-b991504c3f08 | 2.56682 | -60.38285 | 2026-01-21 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc541eb6-0fd0-3009-9cf1-92037745ad54 | 2.90726 | -60.9013 | 2026-01-21 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fcc01a4-1ad1-33f9-8759-e7b57100f597 | 3.34117 | -60.07656 | 2026-01-21 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8f1e89b-388e-3a24-8629-e79602d56ddc | 1.13652 | -60.52602 | 2026-01-21 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10206436-be9d-3d0f-910c-6d77608bae97 | 1.01917 | -60.54544 | 2026-01-21 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01cc1352-d8cd-3bac-bda0-ae092f8950c2 | -4.09953 | -47.30619 | 2026-01-21 05:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 325f89a1-977d-37ad-8703-6663c0cf8a10 | 1.0239 | -60.54988 | 2026-01-21 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6891279-ebfe-3f8a-9ed4-d3a93765e469 | 2.91877 | -60.9499 | 2026-01-21 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c18e7111-355c-3248-92fa-c6ca47940e83 | 1.02468 | -60.55495 | 2026-01-21 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50cc2918-dc33-3172-95b0-39c926aed638 | 1.01995 | -60.55051 | 2026-01-21 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54bcdd74-5c58-3ce2-9111-c87582969876 | 2.91934 | -60.9537 | 2026-01-21 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README5.md)
