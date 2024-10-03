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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ccda4e5-a14c-3aed-a3d5-97412067d855 | -10.90607 | -52.40897 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c717ac2-066d-333e-90ab-8d4bec8a1807 | -10.9036 | -52.42324 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c67a67ff-6480-3f7d-80ce-eecb72b4dc0d | -10.90297 | -52.42686 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8df78937-1dd4-3c83-9c94-8887002a20b7 | -10.87542 | -52.4184 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56f6aa05-f516-3ad6-9429-e9a661d3a7e4 | -10.22847 | -52.72308 | 2024-10-03 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e87cfaa-c2bc-32dc-b338-183eb8675471 | -10.22346 | -52.70253 | 2024-10-03 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4ff5cfc-b8bf-314d-85cc-f718c1cf32e6 | -10.21932 | -52.70184 | 2024-10-03 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1395da6a-2dc4-33af-8800-2d9e1660c2f8 | -9.84167 | -52.07653 | 2024-10-03 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 746c5ad5-d939-3e51-a899-f67346ae83a8 | -9.83644 | -52.0829 | 2024-10-03 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f785e282-2c91-3a98-8c6d-d52f60d7467d | -9.58168 | -53.271 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94774dad-b813-369a-adeb-4e7b3f2e7fb0 | -10.66928 | -53.70946 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d83d2968-2958-3756-a14a-6ced0466f645 | -10.66646 | -53.69982 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a497b60-a7f8-309c-a771-8e4b58271deb | -10.6649 | -53.70858 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dabb3af-0c3d-3d88-839c-4b6ac6bcf53c | -10.66286 | -53.69462 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89c351e3-8813-3848-a3b7-4267701bf109 | -10.66208 | -53.69897 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2e02021-475c-3bde-8b54-f224837de765 | -10.65925 | -53.68944 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 399bb94f-9f0e-3f54-ae7c-ef0572a2096a | -10.65848 | -53.69378 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 488dad15-54f3-3314-8382-8dec590de46b | -10.6577 | -53.69814 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e2551ff-7daf-3c8e-ba7c-d3b3df349250 | -10.65691 | -53.70251 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae495fb2-9748-3fdb-bd9b-ed3b95fa40a3 | -10.65613 | -53.70691 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91f4a064-efb0-37f3-a52c-e431fb85fbbd | -10.65565 | -53.68424 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 248e756f-cc33-3919-b712-86515f4f7571 | -10.65534 | -53.71132 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd522ffc-1450-3a4b-91fa-35693fe74983 | -10.65488 | -53.68858 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a60ac79-7ea0-3928-8f25-38ad88dddf01 | -10.65456 | -53.71571 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be541022-748c-37b4-8074-86c2a277fb32 | -10.65331 | -53.69731 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cf01c27-aac8-3956-8e48-920504ff9b10 | -10.65253 | -53.70169 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a455be2-506c-34ea-8584-0a211af3a82e | -10.65206 | -53.67904 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 142ff0c8-d88e-3aa6-90e4-ea3a2da5da38 | -10.65174 | -53.70609 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66174ae3-d066-3a7f-8038-3d2468c89cea | -10.65128 | -53.68338 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97537619-408a-3893-a0c2-7120e8e4333b | -10.65095 | -53.7105 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b787755-6cd3-3b78-92d8-ca0a90b2b26a | -10.65017 | -53.71489 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 179f9633-c10a-3b80-8576-d4a31e3dcaed | -10.64972 | -53.69209 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d66a4c3b-9304-3542-8caa-86bd4c637fd1 | -10.64893 | -53.69648 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b2988c5-587b-3a1e-9eee-539466656e94 | -10.64815 | -53.70086 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7622f139-225c-33eb-8fa9-f74c3a21b9b6 | -10.64769 | -53.67816 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64641bd0-507d-3846-8e8f-514a30768496 | -10.64691 | -53.6825 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27d103a7-7b60-37bd-a25f-c898182fcd2b | -10.64534 | -53.69125 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14adb738-bd04-3b2b-a360-105190965506 | -10.64455 | -53.69566 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c37bd3a-4657-301f-a40e-cef5f55bf6ae | -10.64376 | -53.70006 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb34390d-623a-346e-b191-6443ad53e760 | -10.64296 | -53.70448 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3bccc7a-01d5-3ebd-bf68-cb9801fd795f | -10.64253 | -53.68166 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 564bf69d-4605-3407-84bc-8cff81fceaf9 | -10.64175 | -53.68603 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e26179b-8d11-3ba2-b8ae-aec899fcb765 | -10.64095 | -53.69044 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b977f9fe-909f-3a15-adee-b55ff898154a | -10.64016 | -53.69487 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5c12704-4302-3ffe-86cc-0215c6bb14f7 | -10.63936 | -53.69929 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dba8b4dc-7a92-3750-97ab-42cb410b91d9 | -10.63857 | -53.7037 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dc99607-0c69-3864-b9e3-27880576144f | -10.63737 | -53.68521 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5ad29a3d-5c83-383a-869b-4d3bd2b4e5de | -10.63657 | -53.68964 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4907185a-6ca7-3ee0-99db-3c055bf3c63b | -10.63577 | -53.69409 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 725a0807-fb37-332c-b7ae-78e516111fb1 | -10.63497 | -53.6985 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 50a20f5b-69dc-39b3-acb4-6f9b50ca48b8 | -10.63137 | -53.69332 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9190449f-3a48-36d3-805c-2957d8d7c753 | -10.63058 | -53.69772 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f9b9914b-5982-3d4c-a222-a6b586d6ea97 | -10.02415 | -53.41386 | 2024-10-03 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46e18645-a883-3d93-bb4e-536c8ba8bee1 | -10.01981 | -53.41304 | 2024-10-03 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 244f64d7-575d-3ebf-ae80-9712f8a9c357 | -10.01905 | -53.41725 | 2024-10-03 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df779914-6e96-36a0-9833-0bdc5747f503 | -12.23863 | -52.67414 | 2024-10-03 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 657f45b0-ea90-3f6c-af60-e3d13664302a | -11.72619 | -52.93805 | 2024-10-03 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 606f7d5d-f586-31db-8ce6-1c045df21815 | -11.08668 | -52.52709 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bf0518f-0f5c-3365-85eb-1003a2c96a33 | -11.08266 | -52.52632 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03b73245-c5df-3fdc-b841-c3bf9c58771f | -11.08202 | -52.52993 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d22b49d9-6595-3a1a-bf40-086b3878b57f | -11.07863 | -52.52555 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78e2f323-f141-3096-9ed2-e431fed6dbfe | -11.07799 | -52.52918 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58c94dca-f4a6-38ea-b022-da7e4abea6b4 | -11.07459 | -52.52483 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 559a47cc-e3e1-31a6-b0b3-7cc98891b382 | -11.07395 | -52.52848 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab0e5dd8-0e8b-3dba-9bb5-83bdf65df7ea | -11.07056 | -52.52411 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6c5d623-b87e-39b1-9249-d26f2d59c423 | -11.06991 | -52.52777 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd247cd2-d4c9-3043-aa60-07312bc20be9 | -11.06651 | -52.52343 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b195744f-5ad2-3cff-b44e-13eca95526ee | -11.06247 | -52.52275 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8a6053f-7521-3d10-b7dd-16a37fa623ba | -11.0576 | -52.50322 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d307e779-4c3c-31fc-8676-eef5e9dc0f35 | -11.05357 | -52.50251 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a25442d-2416-39c7-819c-3f6c9efc3433 | -11.04889 | -52.50546 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 230d5b81-c8ab-3f77-bed6-c64a1f268728 | -11.0455 | -52.50113 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 406270df-52f2-3c92-9d8e-674e77a52a07 | -11.0421 | -52.49683 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c365ee3-e7ea-39d7-a07f-cc24cf46f27c | -11.04146 | -52.50045 | 2024-10-03 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebaa5f46-1f27-3868-b47b-2aef812610d8 | -10.81899 | -53.73412 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c6bae54-a1d5-3f0c-8775-d373c340c379 | -10.8186 | -53.73561 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b61969f7-1749-35f8-91bb-b7fe8c63908f | -10.8146 | -53.73336 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37f7a72f-7792-3ca6-b418-e57ebfa0a49f | -10.8142 | -53.73484 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 163867e7-75d0-321d-9654-1d413913477a | -12.685 | -54.09871 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9845245-9ed1-39cb-ac5b-05037dcbeee7 | -12.68423 | -54.10305 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2b55298-d11d-3d12-86e0-72d4f8dd81d1 | -12.66084 | -54.05843 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 63bde63f-d01f-373c-aa20-2ca1d6a38aa3 | -12.66005 | -54.06271 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fdf84fe-6093-344d-aafb-15003af27175 | -12.65927 | -54.06702 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12b2a381-1439-329c-9f77-84442bf97e05 | -12.65571 | -54.06191 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b5f9a2e-2a1b-3858-ac7b-d5da7cf1414b | -12.65493 | -54.06621 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6998983e-c789-340d-b160-071d089db703 | -12.65414 | -54.07053 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af2dd295-f843-3b84-be29-5e24e898e5c8 | -12.65058 | -54.06542 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86722244-77ef-3e49-8e35-6e455cfa3845 | -12.33727 | -54.0911 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27d0b87f-6c53-35ea-bafd-dbe540f02e61 | -12.33649 | -54.09544 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb3e4aeb-5f35-3ba7-a41b-499300ad8fdc | -12.3357 | -54.0998 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1417de66-1154-3206-a0f8-79dda1a82a52 | -12.33368 | -54.08596 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9f514f6-67bf-3748-8096-8725723121fd | -12.3329 | -54.09029 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94c665ba-9dbb-372b-8884-aac34e9c8566 | -12.32852 | -54.08949 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f443e30-7ad4-3bb3-9c28-879d8e547a2a | -12.32773 | -54.09383 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a67f6ec9-d394-39ff-9057-3d3330d6188e | -12.32414 | -54.08869 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28d47ce2-d55a-3f99-b7a6-4d32c315a27e | -12.27203 | -53.99879 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3360d5f5-4613-34df-88ff-083184df0f8e | -12.26766 | -53.99805 | 2024-10-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ac20344-9830-37c3-9094-a76db90c1593 | -12.66892 | -53.1983 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5967f492-7d0d-3e48-83e7-060915496e02 | -12.65732 | -53.19217 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb066532-38c7-3b70-b02a-1ca346f9aa1c | -12.61036 | -53.15276 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README98.md)
