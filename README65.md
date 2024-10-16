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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dab5cd29-331e-380f-a429-13e33f99a944 | -20.99685 | -55.23796 | 2024-10-16 05:27:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 514eb0d4-e849-35ee-a557-02cee2651552 | -20.99654 | -55.24104 | 2024-10-16 05:27:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2bb53eb3-182c-3dd9-9a32-00e1b1c8dc49 | -20.99216 | -55.23647 | 2024-10-16 05:27:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| acddd7e3-ff20-3835-aee4-8c2c3ed885be | -20.99182 | -55.23957 | 2024-10-16 05:27:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b12a1569-b3ed-3e20-8003-91cf38fd5fa5 | -23.66445 | -55.2445 | 2024-10-16 05:27:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99d36a74-ced5-3b80-bc82-5f2edb186395 | -18.24534 | -56.3863 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fd871bec-2302-325d-8a20-4993be3d100c | -18.24984 | -56.38692 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c1968f6c-0793-39ff-8a42-f94f0acdc86a | -18.23692 | -56.38038 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 856881a4-3861-3f19-9404-51ed556b26f8 | -18.23242 | -56.37977 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| dd454a58-282c-3a8c-b7da-7c24f1a41261 | -19.60235 | -56.97092 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e1674135-4ba7-39dd-ae2a-778d80fe664e | -19.6018 | -56.97543 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ca467af4-ae52-3870-9c83-76e8d8aba3b3 | -19.60126 | -56.97995 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 3d044188-47c6-3a7e-b9ff-409fa0ce6b67 | -19.60071 | -56.98446 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 82f937e6-e54e-3ef3-8d31-e69a3be32496 | -19.60017 | -56.98897 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| c3cb80d3-0c70-34de-8db5-90165547a11c | -19.59849 | -56.96579 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6dbeb9e0-cc2c-3ad2-804f-cd4401b44c44 | -19.59795 | -56.97031 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 96478a67-18cf-30e1-b05c-140399533316 | -19.5974 | -56.97482 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ef72f976-865f-30b1-af25-df873e2d50fd | -19.59686 | -56.97933 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 96a7bd7e-013a-3cc5-961f-bbec650c5e3e | -19.59577 | -56.98835 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 98736eee-6a74-39d8-a841-784c07d47cca | -19.59409 | -56.96518 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0c95885f-6cc7-375a-a1a3-1df3efe5135f | -19.59354 | -56.9697 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 1df3f30c-5e8b-3c12-9ca1-c26b1a234020 | -19.593 | -56.97421 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| ccf16533-93c6-3d48-8c22-94e7c7cb9947 | -19.59192 | -56.98324 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| d4b0689e-dab4-3548-9bac-5a8a25ff1a03 | -19.59138 | -56.98775 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c981601e-fcc5-3152-b134-ee30349cf00b | -19.59083 | -56.99226 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1ed96f50-89ee-36a4-a867-9c706fa14563 | -19.59018 | -56.5332 | 2024-10-16 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f704d754-9808-331c-9135-28ea8ce90b2d | -19.58968 | -56.96457 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1739b518-51cc-390d-8d84-81c8f9352f6d | -19.58914 | -56.96909 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 3ab27000-f445-3e10-812f-d1e61e787be5 | -19.5886 | -56.9736 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 5b7840b4-3e85-32ce-8212-e05b52578054 | -19.58806 | -56.97812 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| b4c00b40-17ec-3a0f-b97a-cb0bf23e71a1 | -19.58752 | -56.98263 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| d887f6a2-ec04-30aa-bb75-4b9678072a81 | -19.58698 | -56.98714 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6d115891-cb6e-38eb-9778-c39f72aeca18 | -19.58644 | -56.99165 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 28b9a1dc-ecd8-303e-aaf1-475346fdac3a | -19.58565 | -56.53258 | 2024-10-16 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f7eb7315-41f0-31f9-9326-20347cfa22bf | -19.58528 | -56.96396 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| d34ce678-d4e5-33c0-ac45-e972cc1a5aff | -19.58474 | -56.96848 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 9fe76874-3558-378b-ac14-9c016c70b5c0 | -19.5842 | -56.973 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 9e30e40a-fafa-3f2f-8a3c-2b04c241db12 | -19.58366 | -56.97751 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 367128c0-bf1d-3bf6-8727-c30b3417fd4a | -19.58312 | -56.98203 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 2a026cb4-c3a4-3286-be3d-85701a207fe7 | -19.58258 | -56.98653 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.9 |
| 65019ed9-7df6-33ee-8aab-2c700afb5255 | -19.58204 | -56.99105 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.9 |
| 8258a979-bedb-3765-b708-89cae23f0c87 | -19.58112 | -56.53196 | 2024-10-16 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3cde73f3-1686-3cfc-b89c-e052ad18eee1 | -19.58088 | -56.96336 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| f7cb6900-38fe-3317-8e10-68723bd9001c | -19.57926 | -56.97691 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| e5b57e81-c89c-3483-9899-7f1c7bb7adef | -19.57701 | -56.95822 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| a21f89ff-56a2-3077-96fc-35f0712aa842 | -19.57647 | -56.96275 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| f4c35083-cd6e-3331-8a1d-c61cecb6fb68 | -19.57261 | -56.95762 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 0cdb7216-ca8a-3229-bd9f-8b946ea26e41 | -19.57207 | -56.96214 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 14d7f3e5-bb85-377b-a78f-6cab009d64cd | -19.54952 | -56.96361 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 26b4e45d-2911-347f-85dc-abd10ccd0202 | -19.54512 | -56.963 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5b7fb3c8-c348-33de-b89b-50387a9bad5d | -21.10246 | -56.13209 | 2024-10-16 05:27:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcf17b1d-eca8-39a1-a4b6-a18fa5af9da9 | -21.24384 | -57.49878 | 2024-10-16 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 749f888b-9c74-307e-9e20-eee33e4a8497 | -21.24662 | -57.51269 | 2024-10-16 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e7b942c-59e8-36b0-bc5a-f2715781a13c | 1.00979 | -52.21924 | 2024-10-16 05:44:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3fa0c229-a99a-3a95-aa44-1592050e790a | 1.0082 | -52.21962 | 2024-10-16 05:44:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d6cb3371-a7d8-3651-83d3-56a691ec2671 | -3.34077 | -53.54231 | 2024-10-16 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 38221d68-f868-322b-ab22-76fc56e85896 | -3.33744 | -53.54523 | 2024-10-16 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78761233-57f9-3b7a-8cca-2de28798e3a8 | -3.15295 | -53.93847 | 2024-10-16 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a50dba5-72f5-3d30-9384-a793d5a816de | -3.11696 | -54.22562 | 2024-10-16 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1172f64d-ac69-3a14-a1fe-9d1fb685fb07 | -3.11674 | -53.72854 | 2024-10-16 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebe36073-567c-31d0-bbe1-58b0a5edc4e6 | -3.11662 | -53.74526 | 2024-10-16 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79f4a07d-d1dc-31f2-bb21-751449c56c91 | -3.11621 | -54.2307 | 2024-10-16 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 82ee8b48-e50a-3e9d-8244-52f8d8a6bcfd | -3.11514 | -53.7397 | 2024-10-16 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7805fec-88e0-37f6-962c-21c727e08f49 | -3.11434 | -53.74525 | 2024-10-16 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8729865c-cc4f-3ede-aec6-2e2b5e723619 | -3.11128 | -54.21998 | 2024-10-16 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 505f3c80-a920-3e15-91ce-03dd75df5832 | -3.11088 | -53.73873 | 2024-10-16 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9c3d24bf-058a-334c-9d2d-d0830433dea0 | -3.11055 | -54.22488 | 2024-10-16 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae606133-7df0-3503-8b4d-7fff51b632f4 | -3.10982 | -54.2298 | 2024-10-16 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| efbad6b0-24eb-3e88-9feb-e7b1977e3fa5 | -3.10857 | -53.73868 | 2024-10-16 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13d9b90b-f6d8-3ebd-a9de-c2a18f35f653 | -2.25711 | -56.25644 | 2024-10-16 05:46:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 736094c6-0f1c-3599-93e4-cbd0857dae0d | -2.05682 | -56.64137 | 2024-10-16 05:46:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24d44d5b-ff2e-39a6-80e6-8bf67fec5a52 | -2.0535 | -56.6405 | 2024-10-16 05:46:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b192f94-034f-32bb-86f7-858d3937c3e2 | -2.05142 | -56.64075 | 2024-10-16 05:46:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c84efa5e-bb3b-3c57-9302-e3f03f6ce328 | -0.89904 | -57.17081 | 2024-10-16 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bc85c2bc-8449-323a-a814-5d34dda4dfa1 | -0.8986 | -57.17373 | 2024-10-16 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a63dfdc9-a73c-30aa-a19f-41e9dd8ca78b | -3.22492 | -58.01851 | 2024-10-16 05:46:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2d2fe9e-5d91-3f71-98b1-e859a72d707d | -3.5589 | -58.70345 | 2024-10-16 05:46:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5865cc94-45af-320a-8cf0-6d85e273ae75 | -4.38264 | -59.95541 | 2024-10-16 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1326802-5f2c-3128-ba11-882a88d231df | -1.41665 | -60.41032 | 2024-10-16 05:46:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 015fb5be-32ae-3c37-ac1a-92f7412c6fa3 | -3.99509 | -60.39374 | 2024-10-16 05:46:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 701e570c-250d-36bd-9000-40e155afd349 | 1.94343 | -60.86368 | 2024-10-16 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3654ca6d-e6e0-362c-a8e5-bca37cd5a41c | 1.11424 | -60.51647 | 2024-10-16 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df57cd26-9581-39fb-912f-b326f91ae243 | -7.78348 | -66.96064 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 022b3d2d-08b6-3905-a7b5-2baa207660f4 | -7.78016 | -66.96011 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a9075cb-9a9f-38df-be87-8aa43d315a99 | -9.20711 | -67.17518 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d433ea5a-4e1f-39f9-9409-fedc33847d08 | -9.19166 | -67.20854 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5168b951-ab31-3fe7-9723-c2aaa6c30f0d | -9.19112 | -67.21204 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a893c2d6-daed-3ea9-9e5b-f4f89aba0fd9 | -8.45882 | -66.96329 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 072d190a-1319-378f-97c6-48726c20bb4c | -8.45604 | -66.95927 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3cb2fa5-d7ab-3167-bc9e-01a137070b85 | -8.4555 | -66.96277 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afe181b5-0622-3745-ad36-453859a31827 | -8.45495 | -66.96626 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6f166d1-81ad-32be-a919-13f6e21609ec | -8.4537 | -66.95918 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f49ec402-25e3-361d-a13c-7aab17927adc | -8.45315 | -66.96267 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5d3712e-bd75-35c0-9bc3-fdad8c27dc55 | -8.45261 | -66.96616 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 859637dc-d1c1-3397-a8bd-46ea7031775d | -8.44983 | -66.96214 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea824a36-16be-3d38-83c3-0faa64edb9b0 | -9.99981 | -66.9047 | 2024-10-16 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8c0c34b-1440-3c65-9547-8c3b8d1a8903 | -9.99926 | -66.90824 | 2024-10-16 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3af002d6-79ca-333d-a65d-08bde9d0fbfa | -9.99357 | -66.85662 | 2024-10-16 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f15387c0-4d1f-3bba-8dd8-1d298bc553df | -9.99302 | -66.86015 | 2024-10-16 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46d8888c-6b06-39db-9778-8225e8e92a97 | -9.92414 | -67.325 | 2024-10-16 05:48:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README66.md)
