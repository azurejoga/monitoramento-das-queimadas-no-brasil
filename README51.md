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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dca74b10-0212-36d3-b609-87e9dcc89920 | -9.68173 | -47.81548 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e2303f1-047a-3127-b557-0ab5e5f5692e | -9.68116 | -47.8186 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 25485cda-194d-3b8a-9da1-fafe9d652df5 | -9.68059 | -47.82172 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ca3b074-b665-364b-9d99-d3ca1d943359 | -9.68002 | -47.82485 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e57561b3-4e43-3426-9fa6-9b0bbbfd8d69 | -9.67655 | -47.81443 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0bd50ea7-9d0c-336d-97a4-3e050d0c9f24 | -9.67597 | -47.8176 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 163b4c8c-9e89-3e52-acef-8629c615731d | -9.67539 | -47.82077 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ce971774-b1d8-3173-b6ac-788cb15c89a3 | -9.67482 | -47.82392 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 685ce609-61ed-36a1-8238-9ff02517024c | -9.67425 | -47.82707 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b557184e-6c4f-3c48-878f-da9273eec8a6 | -9.67367 | -47.83022 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85b7a702-1e60-3e3d-ab01-6e3726416b0c | -9.67251 | -47.83659 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61b4c8f4-7372-3f46-a042-cbe8bbea78cb | -9.66846 | -47.82933 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ca03ca4-ed54-34b9-803f-b959f65733dc | -3.69583 | -47.61805 | 2024-10-06 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 951b21bc-27bf-349b-8d01-a6bf60c9abd5 | -3.6952 | -47.62182 | 2024-10-06 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8eff7591-76d2-39ad-a184-571b5b1529a9 | -3.46291 | -47.6615 | 2024-10-06 03:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1446dfb1-752f-37fc-ba5d-e2c78fe849d0 | -3.46227 | -47.6653 | 2024-10-06 03:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 306e8b9a-e937-3e4c-a067-79c7bc9432bf | -4.27916 | -48.06679 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcc43f82-c21a-3e8f-91cc-654cb80af4d9 | -4.27881 | -48.06953 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1ed7910-f0b4-3b47-88dc-b0363d037c4f | -4.27848 | -48.07082 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea9d750b-e929-321b-8c2e-1da808da29cb | -4.0789 | -47.95224 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 153aa9a4-3a5e-3ad1-9702-71319d08508f | -4.07449 | -47.94329 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a8a7803-5375-3134-86f4-255315ed37aa | -4.07383 | -47.94724 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5822b99-e56e-35db-b852-cf2e8e0aa48b | -4.07314 | -47.95126 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 739b355a-846b-3223-b996-708e48adacad | -4.06872 | -47.9424 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52a3dada-ccb6-3e15-bffc-54a859bce4fc | -3.90833 | -48.34872 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a21ba21b-654e-3f38-bcbe-ee706d28ecd8 | -3.90516 | -48.35067 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9024da0d-c6ff-386f-8f57-b9aa01824152 | -3.9044 | -48.35516 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 873d532a-d4a4-3952-9608-b4f24a43eb9d | -3.8985 | -48.35401 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7df1acad-9875-36a6-b72c-ccca694907bd | -7.72255 | -49.83407 | 2024-10-06 03:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dceb9b9-2f11-38ac-8e8c-3cb67d5cb19e | -7.7217 | -49.83876 | 2024-10-06 03:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ae7e511-4f29-3325-96c3-e9da82e415c1 | -7.72162 | -49.83482 | 2024-10-06 03:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47ef6c29-8297-376a-8f2d-91ec31da0a7a | -7.71644 | -49.83292 | 2024-10-06 03:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 241f2da2-31d1-3611-98be-062e3f01b72f | -7.72073 | -49.8395 | 2024-10-06 03:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 779622d4-5172-348b-aefc-8f6ebd60203b | -7.71559 | -49.83757 | 2024-10-06 03:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4af558b7-3b5d-3b1f-a846-daef1fbbff62 | -7.71551 | -49.83368 | 2024-10-06 03:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f731f170-5f62-3afd-b37f-3c58fd501385 | -8.66592 | -49.42192 | 2024-10-06 03:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77154ebf-ae1b-3674-9019-2b95de503b4e | -8.66516 | -49.42607 | 2024-10-06 03:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8ebf189-ba5a-3ae3-90d8-e7436fc42465 | -8.66368 | -49.42115 | 2024-10-06 03:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 943d0934-2acf-3031-97e0-40005b6c0991 | -8.66003 | -49.42093 | 2024-10-06 03:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebba0ba8-d767-3c3c-9c77-e194e63e3be8 | -8.65927 | -49.42511 | 2024-10-06 03:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0ffd0d6-d7da-3b0e-a8f3-2edd56162696 | -8.62836 | -50.03653 | 2024-10-06 03:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26127c7f-8ea2-395c-9d4d-e805c0c0afad | -8.62786 | -50.03893 | 2024-10-06 03:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6706262f-eca2-3c38-8b88-90ae822b2b58 | -8.62745 | -50.04119 | 2024-10-06 03:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ff31911-1bb4-30c9-a8f3-4349ad30eebf | -8.11995 | -49.52911 | 2024-10-06 03:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a888510-6c21-375f-8e6d-efa0bb7566e2 | -8.11784 | -49.52613 | 2024-10-06 03:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55809954-412b-33e9-bcf4-250c01579208 | -8.11704 | -49.53057 | 2024-10-06 03:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94df22c4-7d80-3323-b834-4fa96e5ca914 | -8.11483 | -49.52354 | 2024-10-06 03:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28636640-2c0d-3e11-916f-01c77f1bc520 | -8.11399 | -49.52798 | 2024-10-06 03:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f209185f-6aad-3898-915d-97c78701c524 | -8.11189 | -49.52496 | 2024-10-06 03:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 690891d4-45d7-37c1-82e8-79c67a2e03fb | -8.11109 | -49.5294 | 2024-10-06 03:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89828ce0-5d00-34f9-ab88-1cd6fc7d94a0 | -3.49966 | -50.27375 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f833fa0-30d8-38f0-864b-601617354e8e | -3.42721 | -50.13474 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8943f8ca-f853-36cb-9ee8-595654e2784b | -3.42617 | -50.14071 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 551b20fb-318d-3f16-b353-77bb20f0e7df | -3.42552 | -50.38335 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a80e764-3627-35ed-b24b-b3ab22fb6c88 | -3.42449 | -50.38934 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9520f39e-9735-32ff-8e72-99dc2acfec8f | -3.41772 | -50.38823 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df7fd541-aef0-377e-8618-3ad579f996a0 | -3.41094 | -50.38718 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88eaecbe-d8f5-34de-a41e-7bef7f56870d | -3.40414 | -50.38624 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f18c9ca-9acf-3f13-ae0b-65aa47f6f08e | -3.32028 | -50.46172 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b52325a2-3cde-38e4-8c79-3dd04daeacf8 | -3.3135 | -50.46041 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab9f0392-ffa8-3c50-84ea-110c719766a2 | -3.31245 | -50.46658 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cca91fd0-9680-3afb-aecc-555062bbb941 | -3.30669 | -50.4593 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb941cfc-bf1f-3e0f-a88e-bcc5d5b62538 | -3.30563 | -50.46548 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 890224b2-4b57-3094-9fd2-ca2ae04df108 | -3.30459 | -50.47152 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d519654f-dda1-3e59-b74a-065f6e36bf8e | -3.30097 | -50.45193 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae7255ed-cbc2-33ce-af68-4be249e35d07 | -3.29882 | -50.46436 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c35af07-74ff-30a6-b14b-e1f0c5750cc8 | -3.26351 | -50.13121 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75965ce8-0529-3a47-8997-dbedf329a8dd | -3.26253 | -50.13694 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19dab8ec-cdbb-3729-8f4c-006e9049d563 | -3.14832 | -50.22688 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b4744d7-2ad0-3567-85f1-d4922d607d16 | -3.14734 | -50.23269 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e0eb1b3-3182-318d-abcd-56df1207c0f4 | -3.1416 | -50.22573 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef2aaa08-138a-3a76-a4cf-33b723d34e2a | -3.31974 | -49.14055 | 2024-10-06 03:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08ed3f67-88ef-336f-a5f1-165b5517a7ca | -3.27361 | -49.12595 | 2024-10-06 03:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6918eb50-676e-3efb-845b-c0e66e8fcec4 | -3.27036 | -49.12697 | 2024-10-06 03:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4f5fa503-5696-33b8-8388-8a1cc859681b | -3.26952 | -49.13185 | 2024-10-06 03:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7d31fde6-9c5b-3e3e-ae8d-1c52f76a5114 | -3.26732 | -49.1249 | 2024-10-06 03:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 218c41c9-b4a1-3281-91fb-1a2477f8c018 | -3.26652 | -49.12972 | 2024-10-06 03:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3bdc2c5-1824-3ecd-95b2-0d1c07312d22 | -5.01398 | -49.76994 | 2024-10-06 03:53:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0615fecd-93e9-3b4c-ad48-b8a58c18a1d3 | -4.87064 | -50.77176 | 2024-10-06 03:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63e5d550-c210-3678-ac5a-e7328032eba9 | -4.86568 | -50.77123 | 2024-10-06 03:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6461b2b4-cfca-3214-80bb-f01201d0ba26 | -4.86391 | -50.77038 | 2024-10-06 03:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a63922c-67f9-3d8e-8485-502f308761b7 | -4.37598 | -50.81188 | 2024-10-06 03:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9f96532-6846-3f35-b989-61d1f09affb2 | -4.37588 | -50.81239 | 2024-10-06 03:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ec33214-e489-3043-ab6a-78feba243c90 | -4.37484 | -50.81824 | 2024-10-06 03:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 360fa28e-670a-308b-92f1-56a52c058aa8 | -4.37478 | -50.81878 | 2024-10-06 03:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0104612a-da76-3e63-9f31-8a802a9d1654 | -3.78934 | -49.46617 | 2024-10-06 03:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5715da40-b2fb-32b3-a420-571eb6e947ea | -5.01309 | -49.77497 | 2024-10-06 03:53:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c2ada0e8-49b4-3fb4-be22-ba3d2f35afca | -3.78848 | -49.47115 | 2024-10-06 03:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29a8fd0d-a744-336b-9575-b7c33a2ab9ea | -9.15188 | -50.56383 | 2024-10-06 03:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfef894a-c3f4-36ad-97f8-043b70764ef8 | -9.15091 | -50.5689 | 2024-10-06 03:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f68c9a1c-0cc0-3fc6-9d57-ef16a615528d | -8.23227 | -51.00596 | 2024-10-06 03:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed77d5d1-5e67-375d-a0aa-282ae5ce6a0d | -8.22602 | -51.00346 | 2024-10-06 03:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7541bfb4-e9eb-3081-8828-a2fe3ff3da3c | -3.23456 | -50.83659 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e161663-6bfd-30d9-987b-904459e4a880 | -3.2334 | -50.84325 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 57d9ad08-1edf-3056-bb07-6b114d9bfeb5 | -3.23225 | -50.84991 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 899e3877-f982-3750-a6ae-6aa9e3c2ea36 | -3.22763 | -50.8352 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fee0989e-c35f-37a3-8993-e7b5f5d2bf1c | -3.2265 | -50.84172 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1c22a30b-6454-3bf8-a590-c218b518115b | -3.22534 | -50.84842 | 2024-10-06 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bbb0e920-fcc0-3873-90c4-5203b6faaf7e | -4.10443 | -51.10438 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ae44109-a79c-3d17-ba4a-6b20c4d423ae | -4.10006 | -51.10116 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README52.md)
