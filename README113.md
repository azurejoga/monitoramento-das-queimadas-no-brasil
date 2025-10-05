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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28f72927-fe59-3097-a5fc-d40f995700c6 | -15.60768 | -52.46497 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6637b6b-650c-3451-a4fc-cd23c737e5e2 | -15.52697 | -46.87621 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8024a038-c846-3efe-8f61-150c91c80caf | -15.60935 | -52.49848 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beba0267-637d-3e03-955c-13ce5d7828e5 | -15.60273 | -52.49737 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 155b0122-135b-3a95-af30-f34a70407c72 | -15.76506 | -46.26934 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed4cfd62-2d1c-38ff-8047-b81c5ecf7c9c | -14.94211 | -46.84602 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7575a61f-764c-3a91-979c-6bb70410ef59 | -14.87976 | -48.2611 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 380fdb87-3c69-3ad2-b558-1f5b9c3fc48c | -19.0174 | -50.59966 | 2025-10-05 04:49:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 33a6cef6-2931-322d-84ea-03ff5f88cca2 | -16.04382 | -50.94442 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13ab60ee-e88d-39d0-ae91-4707f536d5df | -13.92493 | -48.16131 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96619fd5-5bdd-370d-bb40-f6add5b7e918 | -17.97126 | -51.14111 | 2025-10-05 04:49:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f2e7744-fbdb-3c51-b5c0-50e1af250895 | -16.01959 | -58.22092 | 2025-10-05 04:49:00 | NOAA-21 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 83ab1c17-dd76-37b4-b4ea-98faccf88faf | -15.58556 | -52.45398 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abd0a550-ff5e-3570-9e91-a3e9d0469857 | -18.25667 | -53.36677 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8ff26b90-2584-3b4a-b111-d1e204204c11 | -16.0831 | -50.91789 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0dd031c1-c4dd-3509-b082-d3a35686dda9 | -15.93286 | -48.9921 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e82f264a-4ab7-3a90-ad0e-76ca9e9b220e | -14.3332 | -47.67915 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 309d7bff-5aa1-3331-9234-8bf3c473b480 | -14.41124 | -56.23581 | 2025-10-05 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 041b9f26-7085-3ead-a04a-74fd9e53764a | -15.21254 | -46.38774 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e640fc8-3801-39b3-928b-b3c4f07833fc | -14.0856 | -50.15481 | 2025-10-05 04:49:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14ac372f-6818-3afb-a8fd-66dec5567946 | -16.35037 | -51.45919 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4489e6e-8d62-393f-82b1-9d8cd1f2c354 | -17.19984 | -44.44502 | 2025-10-05 04:49:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33f16f38-8990-3525-b111-928f4d1216b5 | -13.72762 | -48.08084 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7840ba0e-03e6-37b5-83bd-f733d14b57ae | -16.0473 | -50.94488 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c0f5d36a-dfdc-3a97-835d-c2ed190fc05d | -16.53648 | -47.77091 | 2025-10-05 04:49:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4206407-bb4e-39ac-8f6a-ab090f29f11d | -16.38106 | -52.15708 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 8bb9bcec-e143-37c2-a4f4-bd57b1cb703f | -17.89922 | -57.6435 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 51545f19-517e-311a-b478-f35d4a538de3 | -15.61267 | -52.49904 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b470286-4dac-3dc5-bd3d-1f1fc9d60e81 | -17.46016 | -49.76725 | 2025-10-05 04:49:00 | NOAA-21 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae0e1447-a517-3702-9a61-fe14127ffba2 | -17.94804 | -57.60543 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 7f0dbece-a267-320e-b74c-bea6d558815e | -13.74281 | -47.96747 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc854e10-3c80-376a-a4d9-2bb020098bb8 | -12.92055 | -54.72766 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3ee58c1-495c-3a96-87f8-9c015ee44d4f | -16.01253 | -50.8518 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2edf14e0-9b1c-3c62-861b-d2addc97fec4 | -15.50742 | -46.85619 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec5ee6a1-fe35-33ef-be09-33d72a315afd | -15.14361 | -45.74892 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 84c00263-6910-3f00-a585-2d0c7673e421 | -15.60163 | -52.50458 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28b07e5b-0508-31b4-aba7-b4eac178bcac | -14.67725 | -49.61284 | 2025-10-05 04:49:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3f2c8d1-91e9-3bdb-917c-beb830b7f94e | -17.95051 | -57.59146 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7c44a7b3-3b29-3415-9182-c129163220a9 | -14.97596 | -49.99185 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab8a05a5-6eb0-3015-a4e4-59109d1e9c02 | -14.3264 | -47.69939 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a80839f1-686b-3ec9-a0c2-b2a7b127e40e | -16.35143 | -47.05819 | 2025-10-05 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fee130ef-c627-33c7-8975-b3bedbc4c0bc | -14.68726 | -48.35342 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8396b797-f5bc-3aa1-b8f5-6a9d4ef7fff5 | -14.65436 | -48.33207 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 98a92ddd-356a-3e9d-a401-279acf3a2f68 | -17.87798 | -57.63391 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5d775a79-7605-37b9-8d48-3af0b91c7fea | -14.68269 | -48.3579 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| dfc0bb70-6da7-38db-ace0-9d4322d0b1a2 | -14.75529 | -54.66637 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f810c2a2-dc91-31dc-906b-204ac9cce3a6 | -15.35627 | -46.3013 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7add488a-747d-3193-8931-961dea9e3a3e | -13.69656 | -51.23601 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14535137-b4da-3a98-9ab9-474d34fb6a77 | -14.67027 | -48.36175 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2b9ec6c4-dd6c-3e99-99bd-5b7296806dba | -14.92775 | -48.34995 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee31dcb6-2619-3415-8743-57f32b3c6531 | -14.67257 | -48.31483 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 031ff901-f8cb-3fed-9352-3b4001cb1f08 | -14.44617 | -46.09993 | 2025-10-05 04:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ea8282f-64ac-3e41-8e09-bfd89df2f562 | -15.80717 | -46.27642 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9c2559a-4864-3570-8cb7-2e1b5a63479a | -15.90802 | -48.82971 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba474665-9e4e-3637-9430-6696e25b070a | -15.61321 | -52.47328 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fa57508-120e-30ee-bb3d-3d3fdb1c2e0a | -14.33083 | -47.69707 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89a2d30a-9d10-3548-86e4-522ad279b977 | -15.59942 | -52.49682 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d378ac01-323c-30dc-870a-35e0c9dc6509 | -18.18338 | -53.35802 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b4636ce-630a-3bae-98d7-d61f164496cb | -18.20374 | -53.37997 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a8b6a28-185b-3606-abe1-908d605e8408 | -15.60385 | -52.51223 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c8af866e-216d-3b1d-87a9-75c36584a83a | -14.69318 | -48.33908 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b229c14-66bb-38f3-a3ed-e0e20d963e56 | -14.66449 | -48.28183 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 098126f1-dc37-3595-830b-bbcac370eaec | -14.88768 | -48.26166 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39f41bd7-50b7-34f9-83da-b0e03a83d7cc | -16.95154 | -52.67942 | 2025-10-05 04:49:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12d89424-ee60-36f3-9c43-1f13eeb8b7c2 | -15.19374 | -52.78888 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0da78b4b-1f63-35fb-8043-d2500db9a3f7 | -17.94685 | -57.59058 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 6a1ef8ec-c0c9-3a5c-a87c-10600b53a271 | -15.59336 | -52.5142 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff67f854-3038-3185-b318-523ad9dd3c2e | -14.61926 | -48.26275 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7e09e53-dd35-381f-8e23-c86b3f6d1e03 | -15.59667 | -52.51474 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 080c1d29-9a43-3b76-bb2c-ee9cc2c07ad4 | -14.9555 | -49.9897 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ac82b04-7fcb-3e6b-b085-33e35ec90c4f | -16.07905 | -50.92132 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3471cf94-ef7a-3a67-9d8f-ccc5bfd772cc | -16.36117 | -51.45696 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e46c726-bd42-3dfb-817b-ffbcf07688a9 | -17.88303 | -57.59369 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bfc339ab-44a8-3134-aa21-d76354065048 | -18.19671 | -53.29343 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d39198e8-2949-3805-89dc-d87b1e417e96 | -18.25067 | -53.33968 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3f39a1d9-1f4d-3517-aa59-fea9dff84258 | -14.91498 | -46.85229 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ebfabe5-6f4f-340c-bb75-e55b81d7d72c | -14.68538 | -48.33793 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b78f166-9982-3faf-8c95-9c765ecd046f | -12.84148 | -58.76362 | 2025-10-05 04:49:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 578b153d-f398-3c57-b8ba-d504585460b5 | -18.17565 | -53.36419 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f6bef214-eb6e-3e7d-9287-c923114ece35 | -17.95501 | -57.58757 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a5998658-3c05-3373-92fa-3a08b13df178 | -15.59059 | -52.51007 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 88bcb818-5d3f-33da-b74e-33c97bf130cb | -16.29573 | -45.24312 | 2025-10-05 04:49:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66f5768e-a0a3-3334-87ab-79410e99eda1 | -14.68702 | -48.29611 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fc9b50f-add8-3f8f-90ae-6934ec589d7b | -15.23678 | -49.30248 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd54ee2f-40f8-39ee-9811-a82fe6a009ec | -14.25042 | -46.09277 | 2025-10-05 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af566d31-8ada-3780-95d6-f77efb775196 | -16.03942 | -51.04821 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 30aa4a25-5939-36c6-96b1-2b0ce8cf4a2f | -16.02018 | -50.96127 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bac70da-f0b6-31a0-8a93-8fbe72d1e350 | -14.62256 | -48.12015 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71a80c6b-ab79-3d86-a65e-ab275f0089cd | -16.3447 | -51.47395 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e409f309-eab8-393f-b755-ffdd0ed54336 | -15.36847 | -47.97998 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cc085bb-b894-3c40-8941-ea7d64371c54 | -15.34467 | -47.3276 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ade6035-3899-3adb-9cd0-6eb21dbbbcde | -17.56981 | -46.08162 | 2025-10-05 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a619c630-be44-38ee-8abf-048ac7430cc2 | -13.91833 | -48.20401 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8a92f27a-d573-3336-a90c-68d6fbad9c8d | -13.75067 | -47.96881 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3e1ad9d0-9cd2-3ce4-98a4-6f1142df58cf | -16.07453 | -51.07353 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6d12999-b592-3150-bbcc-f66f1a4e18f8 | -15.30454 | -47.95657 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 053171ae-2d43-3368-8c7d-411e8b7adada | -15.91253 | -48.82532 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 47d9445b-3d78-3130-b6d5-a23c82a51068 | -15.55595 | -46.95951 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79596fe6-973a-3da0-9829-ee29db5e064f | -15.8741 | -46.25748 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a16d38f-3328-3ee3-86be-1468063cbac6 | -19.24368 | -47.85535 | 2025-10-05 04:49:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README114.md)
