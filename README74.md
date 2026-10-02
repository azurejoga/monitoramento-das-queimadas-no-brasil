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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5c2d401-36a1-3a9e-a60c-422e755d7e71 | -3.13512 | -53.74629 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 108ede9e-de76-3d79-9db1-d62499ac2a3a | -4.27865 | -50.77693 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a02e679a-0ac1-3777-a60c-39dd18998b65 | -3.03425 | -53.87289 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6f6775f-afd0-3b9c-af16-e3ffee15ec99 | -4.28425 | -50.76777 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 453cf19c-a676-3ea7-84b0-183f8b9e4e97 | -3.73102 | -51.175 | 2026-10-02 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeac7a8f-5f3e-3591-898b-00e6d020e75f | -4.26571 | -50.74382 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 052b3a62-27dc-34df-ba79-90ca39fad2f9 | -4.28455 | -50.77427 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bca788bd-daf0-3a50-adaa-b84db3457de1 | -3.00366 | -53.87226 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2acaab12-7222-3e39-8a6b-627569081a8b | -4.44974 | -54.90305 | 2026-10-02 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ff4ed0c-d831-3104-8f18-9ae95601af82 | -2.05225 | -56.86924 | 2026-10-02 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a022073e-a549-3d18-9238-259f6d2c05f8 | -4.07458 | -50.32861 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53063e5f-05ff-3502-afc2-2723a940dc53 | 1.01099 | -59.53647 | 2026-10-02 05:33:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab9ba8f8-6b2a-3123-92dc-dd74ca64a368 | -2.05579 | -56.86974 | 2026-10-02 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a266b765-15c1-3e69-8ee9-a7e32163713c | -3.15719 | -54.07862 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9cb4d54-7630-3f47-9011-dd0504352521 | -5.87139 | -50.16182 | 2026-10-02 05:33:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fe905fb6-e4c2-3dd1-a8c4-2bb545a02768 | -4.2767 | -50.75185 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92780292-94fd-381d-a2ba-b2bac5a6fa75 | -3.29396 | -53.85594 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ef21321-36fd-31e5-aa04-0848bd09c66f | -2.9013 | -54.14947 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d20f7e78-96c8-3334-adfd-e959319ebae3 | -3.00305 | -53.87627 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1a836c71-e728-33cf-80e8-284d2ae7a3c2 | -3.47377 | -54.62464 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7287efe-326b-38be-9342-ce3cf56f9349 | -4.2758 | -50.78718 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 868ba5b3-3739-34e0-ab90-193d3d7c53f6 | -4.27341 | -50.76635 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e5cb860-a747-3d88-b4f7-ced409e0752c | -5.86784 | -53.48721 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b685b5a9-e706-33e4-a3b4-23faa0d48e07 | -3.01528 | -53.88225 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7192b439-c8f8-3558-b337-400d68dc94c5 | -5.90022 | -53.49054 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae5dcfd8-a3f9-3198-a729-74a6efd91ac4 | -2.57449 | -49.99965 | 2026-10-02 05:33:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 099693ef-6e97-3a83-8066-c1338a14149f | -3.2918 | -53.85619 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72bd29ee-c8e9-3ec8-b927-6e24e09bc081 | -4.29979 | -50.78352 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2903d990-d2ab-3e1d-9636-f2c74b1bf43d | -2.57503 | -49.99601 | 2026-10-02 05:33:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9682d7b3-38c0-3aa7-a19a-808ab8e6b967 | -3.29003 | -53.83937 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 8febc8b0-5148-3337-b5e1-652b247e567f | -3.1407 | -53.73876 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 07772af3-279a-3b5c-b150-135901cd125d | -4.28012 | -50.76662 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e509dce6-24b9-374c-a155-0144f2cda97f | -1.63179 | -55.13615 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 263a08b8-bcd8-3d5d-936e-c973b80cbbe7 | -1.6086 | -55.13256 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 437e2f20-a606-30f4-b744-230c8db767d6 | -3.28225 | -53.84579 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| c510a1b0-d27c-3888-b665-6140c48da3b9 | -4.28504 | -50.77084 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 767e5119-5d24-30a0-bfd6-afd78f628cfd | -4.38666 | -54.82772 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 208c055b-8212-36d5-bf04-ed45563611ae | -4.27882 | -50.76708 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4b7c3c7-9c1e-3c31-b3d2-280cf172d08c | -1.90982 | -55.04452 | 2026-10-02 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6a34e8f-3cea-3a57-987b-a8a799930c3f | -4.28406 | -50.77769 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3452f608-e11b-3d43-b896-b1bd8d28fec9 | -3.2299 | -54.31271 | 2026-10-02 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99198a22-1524-303d-ac03-6fe7774bdb5e | -4.27602 | -50.74894 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5ed0402-9f30-3543-8803-0d559f3533d8 | -4.27188 | -50.77652 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5038f536-26b0-3396-bc17-553265dee946 | -3.162 | -54.07538 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60df1bd9-f566-313f-843c-ae8cd777bde8 | -2.90184 | -54.09073 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8958406-cea5-3eeb-886d-57a274e5cfb1 | -3.0306 | -53.86814 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81ebc6e8-1d9d-31f7-a9cc-3fc3206e0a0d | -4.29869 | -49.09225 | 2026-10-02 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6d7b8e1f-1e17-3f9d-a9ef-fb2001f053f0 | -3.07797 | -54.37065 | 2026-10-02 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcea472b-9ec8-31e6-981e-175cc6d4ff61 | -1.48258 | -55.87169 | 2026-10-02 05:33:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e6f6ae2-acd6-3399-9c49-231aa051c6ee | -5.29697 | -55.8746 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| add97a8a-ecb6-3fa5-b246-c8f4b67a2a9b | -3.85264 | -55.80491 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82382160-3d94-3be7-a592-3182ae84ca03 | -3.84761 | -55.80238 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d5c6a22-6427-3e44-aca1-272edac3db6a | -4.27817 | -50.78027 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d6b4dda-22c3-391a-9f8c-b16d9431a02e | -2.4601 | -56.07811 | 2026-10-02 05:33:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 057d8116-8404-3c7d-882f-93b7b2ddb0bb | 0.58913 | -60.37798 | 2026-10-02 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a48384f8-9730-3d8a-ae91-a6513d67e90f | -0.25198 | -48.48916 | 2026-10-02 05:33:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b68cfd5f-a5a6-3a5c-a522-39a9d118642b | -5.8458 | -53.47735 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f67c98d4-9fc2-36ee-bd9a-e86cdb95523c | -3.29146 | -53.84312 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6f68c821-40d6-3b17-807a-a15bd1fb7e2d | -3.28965 | -53.85527 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3cfe7cb-efd2-32ad-8663-87f749331ebd | -5.37303 | -56.06027 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d4804ef-9fd8-3760-b60b-fa9c86a4c708 | -4.27651 | -50.74563 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5ba8496-7664-3cd7-b13d-b57e66a15336 | -5.00694 | -56.28745 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ecb33e3-8cbd-3631-967d-3c6c7d5df33a | -4.24897 | -50.74477 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75e8c704-d934-3dc0-95a1-8aba29088bcc | -3.61304 | -51.7977 | 2026-10-02 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff75f305-069a-3ddc-8052-75506c8dfc7f | -5.92449 | -53.48145 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 378b8bb0-fe37-32a1-9b30-df324aa84672 | -4.98895 | -56.14937 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24227188-2ac3-3698-af4a-563607b0446b | -4.29142 | -49.09441 | 2026-10-02 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 24a3d484-b163-3ba1-9ecd-3cd8a5ab0d0f | -2.04807 | -56.87272 | 2026-10-02 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 64e5639f-5b70-30cc-a71c-e9036d0ecf94 | -4.28862 | -50.77542 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18cbd83b-ab30-3a3c-a525-d80f5cfded38 | -4.293 | -50.783 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b77cc87-768c-36e1-8584-50d8ee7dc9c9 | -3.29336 | -53.85999 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd69b620-5baa-344c-9a65-1f3f99eeef62 | -3.01554 | -53.2099 | 2026-10-02 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da43e399-c8db-3338-b345-0cd74b3de42d | -4.68621 | -55.79407 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea2e5794-2041-3ae0-9edb-5c8abf54b1dd | -2.85212 | -54.13409 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f59bb13-45fe-357e-9264-231ffcd081c2 | -1.45403 | -48.91135 | 2026-10-02 05:33:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee77855c-0e03-35ba-b22b-8397fda40c6f | -2.95269 | -54.09336 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 619f8dab-adc0-32f7-b74a-e18eae003db8 | -2.8935 | -54.14433 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cecda36c-12d5-354f-b315-532a65ec902a | -2.89108 | -54.13228 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e42791d-1be6-333a-a7a1-8b0e8fe8c9ed | 0.30721 | -51.04116 | 2026-10-02 05:33:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c2c933d-01fb-3e87-92d0-492bade10343 | -4.27988 | -50.76007 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c1faff7-a6e5-3ad7-ad80-244e5144f505 | -5.92463 | -53.48444 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a1535a0-c341-3fc2-b605-fe47e9261b9a | -5.87438 | -53.50658 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77575ef6-f63f-3ea5-a6fb-6f7324546822 | -3.29117 | -53.86022 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a8cee71-a981-3659-8256-ec4b68f93776 | -4.26801 | -50.76546 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fcd9aff-cad7-300d-a7f0-f237bec07127 | -3.47599 | -58.45852 | 2026-10-02 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d74dccb-352c-3fbb-a03f-fad7e2eafed5 | -4.26699 | -50.7723 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f94e6c8-bb97-3080-a5db-aaabfdebd1b9 | -1.26163 | -54.56124 | 2026-10-02 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 5d037d35-1d52-37ad-b214-9dba40763926 | -2.8977 | -54.145 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| efc9c9f6-37b8-33c3-98b0-1342ef27083e | -3.61134 | -55.51117 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e66c717-2f36-3d67-a410-ebf9673e2870 | -2.89043 | -54.10871 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f17f404-6cab-3b42-8af6-61b784f7eea1 | -6.15141 | -47.46243 | 2026-10-02 05:33:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 021b5b89-805d-3ab8-a4d8-ad7ce28381ef | -3.16928 | -54.08459 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3997f7d2-2df6-3bd1-9ca5-e03ddf9c43ce | -1.45967 | -48.90594 | 2026-10-02 05:33:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e36e1a1-d633-3561-b9ed-c564aa93f99e | -4.29587 | -50.7724 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1851a1f8-4dcd-3e9e-a39d-883778b8e16f | -3.28876 | -53.84743 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d032970b-4265-3465-b2e8-091ecf57d2dd | -3.5735 | -54.62038 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 775e1599-669a-3bdd-b7b7-36bdca933ed6 | -4.02051 | -48.94527 | 2026-10-02 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd01acc2-49c6-388b-961a-50582eec516d | -2.04932 | -56.86481 | 2026-10-02 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 9f273d56-dd0f-3bf5-82d3-1cf5b30983ff | -3.13574 | -53.7422 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aeee4c40-9dd3-3063-aec0-29a4fb300d66 | -2.90847 | -54.13105 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README75.md)
