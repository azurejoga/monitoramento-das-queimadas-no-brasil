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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fbc851a-8e82-3e93-8169-084477a24647 | -4.0476 | -50.95572 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fc46400-b3c2-3e7c-9ce4-01656fce3207 | -4.04732 | -51.02171 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94c0e9b5-7241-31bc-a9c0-cd90b24fb53e | -4.04716 | -50.95271 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 913d1016-11b9-3c69-9b9d-5b803f2f536e | -4.04712 | -50.95863 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f6c18b8-6db0-3fe6-875e-9b673248809b | -4.0468 | -51.02486 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59172e10-eff7-3af6-81ea-efeadb261a35 | -4.04667 | -50.95555 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b56676c6-f65d-3b64-b0d4-17cbaceb419a | -4.04247 | -50.95489 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4b58067-7455-3ade-90ea-375d28ffde9a | -4.04198 | -50.95785 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 406f190e-0546-3e9b-80ff-75a00cb90fd8 | -4.02789 | -51.01115 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 901c883a-55ff-3dba-9b73-6c7d46c720cf | -4.02317 | -51.00775 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e0e00e7-736e-3a2b-b1b7-eaac0b8e9293 | -4.02266 | -51.01081 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46a7324a-5096-3f81-acec-d8a06d503819 | -4.02216 | -51.01385 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2f5d8b3-e2a6-347e-be18-dce96a793051 | -4.01746 | -51.01027 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccebf1ac-aa3b-3797-a250-b2c22054386e | -4.01188 | -46.02405 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 802adee2-b12e-35bb-8842-9331b074e494 | -3.96243 | -49.89287 | 2024-10-21 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9eec8f6d-bc5c-39a1-b557-f9745200e8e2 | -3.91726 | -48.34682 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4618613a-b80b-30d6-9439-cc491be417d9 | -3.9166 | -48.35089 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93a3e723-3ed4-3288-9543-42517e1fb4de | -3.91496 | -48.3339 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c13857c3-d2f3-3ef7-8a39-1222cf17c75b | -3.91432 | -48.33783 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1399527-fa76-32e8-938b-9830431b0b59 | -3.91067 | -48.33321 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cca331d9-6c99-38db-bdfa-bc72c885514c | -3.91003 | -48.33711 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| be952e3d-48de-3f78-9214-e11de76e0660 | -3.90274 | -49.99296 | 2024-10-21 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffab2bb2-fd8d-3faa-995f-e5b8d45df88f | -3.90272 | -48.32793 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc24eb26-66a2-3da5-bf61-b49de9a18324 | -3.90208 | -48.33186 | 2024-10-21 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc3a3e91-536b-38f6-b275-2c3b8a73bbd1 | -3.90115 | -49.99387 | 2024-10-21 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10da84b9-86fc-315d-b023-1cdeac316d65 | -3.89794 | -49.99213 | 2024-10-21 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0488eb77-2eac-312e-aa7b-33e957deee4e | -3.88471 | -51.19422 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c5c3c06-fad4-382b-8373-f2355066f1cd | -3.88418 | -51.19741 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 618b1c20-6e77-37bc-ba24-dd46bf969bb7 | -3.88351 | -49.9897 | 2024-10-21 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40533ef6-e355-3619-a56d-bbd96141a871 | -3.88191 | -49.99068 | 2024-10-21 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73a3a9cf-8f53-3514-8bd3-6ffe4cacb055 | -3.87377 | -51.19545 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36dba367-0c7c-3cbf-b41c-d07490ac8052 | -3.87325 | -51.19855 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98052161-fd53-317c-95ae-a2e95816cc6a | -3.87231 | -46.45068 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb1a0623-062b-36e3-8c1a-0a6196bd9d5b | -3.86842 | -51.41482 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70553864-2131-36fa-9592-36aec510ff2c | -3.85133 | -48.98699 | 2024-10-21 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f324b9a-715c-3ab2-84df-cf6413a6216f | -3.85057 | -48.99153 | 2024-10-21 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 233bbe11-af4a-3ab5-840a-2590adc54e2e | -3.84953 | -48.98932 | 2024-10-21 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d98a5c4d-0d98-37e0-bd4c-00d00b36daba | -3.84338 | -46.48433 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 493f1383-17ce-3952-95b1-0470ee6a839f | -3.83987 | -51.90697 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 578f2eb6-4699-365c-92e3-666e5f72d749 | -3.83928 | -51.9105 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcb342f4-26c9-3358-9589-cc044782bec3 | -3.83868 | -51.91403 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4286aff-dd9c-361d-a392-7420289b2264 | -3.83523 | -51.29689 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 979f71d1-f049-366a-a35c-759d4015595e | -3.8335 | -46.47305 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e452378a-f3c8-3861-a592-84e45758827e | -3.82271 | -48.87131 | 2024-10-21 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c503c55-bbd6-3e43-bf36-aabadc80ef7a | -3.822 | -48.8757 | 2024-10-21 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b655a9b-7662-3ece-8d7d-547527c95658 | -3.81826 | -48.87057 | 2024-10-21 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ab73a7a-f5e8-3ae3-8ab6-08b066d87d66 | -3.81754 | -48.87495 | 2024-10-21 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f96af97a-2633-35f0-951b-db6278652f39 | -3.79479 | -51.80898 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80f937cf-fc9a-30c4-b418-8f9a1fc375c2 | -3.79413 | -51.80732 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6bdc6d3-44b0-3bbe-a460-92bdbaf40ddd | -3.79355 | -51.81083 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cef0f40c-7e2a-350c-83fd-66e5853dbc15 | -3.78996 | -51.80453 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e12aa799-b490-3b06-86de-82679f0ca517 | -3.78935 | -51.80804 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85bea777-5d86-3b16-a6ec-7e53a971c5e3 | -3.78869 | -51.80636 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cca7dd3c-b521-3981-ab8e-59722b51b231 | -3.7881 | -51.80989 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07bc275f-b93e-3818-8f92-92512217493f | -3.78314 | -51.9744 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05e08d93-597f-362e-8409-31cc3a634517 | -3.777 | -51.97709 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 676c4a24-73ad-366b-a5ce-e6b408aef266 | -3.77229 | -44.67296 | 2024-10-21 04:12:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2bf17fb-f536-3b73-bf08-c4ce30f921c2 | -3.77149 | -51.97618 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00504740-0c61-32c9-9e18-4158f8fc83ce | -3.74817 | -50.65963 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb4acf60-71f5-314c-b5a2-5704ed878757 | -3.74769 | -50.66251 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68518b87-b02f-3514-a5b0-667dff5dedc5 | -3.74363 | -53.41003 | 2024-10-21 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdaccc2d-44cb-3101-b3e2-e07d71f0e06a | -3.72719 | -51.3329 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7b9ed67-0d85-3dc9-9df1-3069b63f0c23 | -3.72223 | -51.63877 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6261a5b7-f19b-360c-ba6b-5e0ed578e546 | -3.72192 | -51.33195 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4e02527-d92e-3aa3-8f89-6ea276bff3dd | -3.71685 | -51.63779 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5b19f0e-306c-3e91-b80c-d51b7359c33b | -3.69239 | -52.00959 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2952642-8e6d-319f-ae5a-201dc7a47474 | -3.69213 | -50.19633 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 866d1f9f-0cfe-3f5a-a1a2-5aec906976a0 | -3.69178 | -52.01318 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22d8a7b7-fdd2-39e9-9c35-86a14db2499d | -3.68088 | -51.84587 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbae8cf2-6b2e-3f2b-8ab7-3197a1cad444 | -3.68087 | -51.84389 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| becf30d0-06a6-3f29-bcb7-e92931f21421 | -3.68029 | -51.84737 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb111aa6-7eef-3fd8-831f-3af772d40031 | -3.67539 | -51.84505 | 2024-10-21 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a43a84f0-a20d-3339-be84-654c4a0c4f0b | -3.63362 | -45.75791 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 989b70d3-7acc-3b79-9e38-c85744a7ca13 | -3.54356 | -53.02248 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81510c27-1623-3c56-bd9d-04e5dfa1c313 | -3.63293 | -45.76218 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6493d344-8bb9-3c10-92ad-ce5723b34ade | -3.62926 | -50.79311 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30534746-6a07-3393-8f30-be5804d2794e | -3.62877 | -50.79609 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5b25b81-61d9-3b30-8b61-a74c7740da8e | -3.62515 | -50.78628 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa94bf4d-08ce-32d7-922f-856bb859222a | -3.62466 | -50.78923 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9366ee28-860f-3cba-bf2d-ddb205dd2863 | -3.62416 | -50.79223 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff9ebff9-8e24-3220-a5a9-4b1efa5adb07 | -3.62367 | -50.79523 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51530dbb-2a4a-3d60-af9f-fd483f0c9149 | -3.61577 | -45.8211 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79a9e81b-9b7b-3a03-85b8-9846b23e3ef0 | -3.61209 | -45.82051 | 2024-10-21 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06d587e5-31b0-3811-ae2f-3fefd9836cc8 | -3.60782 | -50.5779 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b1f83fa-da4e-3a8b-98d4-8f65546569fa | -3.60733 | -50.58076 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8c349b7-71c0-3722-8e11-66d4f9501637 | -3.60685 | -50.58361 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b7c79df-9ca0-3511-88eb-9cd9eff3247a | -3.60638 | -50.58644 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50726a92-b84f-310c-8415-54594460ea57 | -3.60279 | -50.57703 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dba78e1-fdb8-34b7-9b74-a4d5b54a2272 | -3.60231 | -50.5799 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c642cdda-15ed-3c54-b0cb-fba50f418dc7 | -3.60184 | -50.58269 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97eaaf2f-3267-353e-aea2-63cacbcf9bf8 | -3.55214 | -50.30153 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86ecb6bc-7d5c-3322-9a6f-8f5eaeeb6297 | -3.55123 | -50.30699 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24b17436-54c7-328c-baa3-cc70e1528d86 | -3.55111 | -46.40702 | 2024-10-21 04:12:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89328fb4-304b-38eb-aafe-e8ff3b7f9c75 | -3.55031 | -50.31244 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3707920b-6b3c-34ee-8c97-3d67e5efd9ea | -3.54847 | -51.38273 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8511789-440f-34e6-b537-ebac6f483cd2 | -3.54795 | -51.3859 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df824e37-61b4-3989-8c70-22ae5c7686d5 | -3.5473 | -46.40641 | 2024-10-21 04:12:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8458567e-9169-32cb-86a0-ddaeba0f3227 | -3.54628 | -50.30617 | 2024-10-21 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad6db77e-cb54-3c58-86e7-10c52fd20811 | -3.54626 | -51.38305 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea1a9f71-51f7-3f70-8b0b-4df883fd245b | -3.54572 | -51.38619 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README27.md)
