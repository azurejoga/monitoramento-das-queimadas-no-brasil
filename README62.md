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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 118f5178-98a2-370d-981e-f3f986bbd8ce | 0.08393 | -49.86303 | 2024-11-02 05:04:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 715c1add-fc41-389c-81bf-496d5ae1d520 | -2.10784 | -49.51066 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5ad7551-064f-3fbf-9e51-f12c54d585d4 | -2.07785 | -48.82129 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| be664e17-4876-3efd-bd1f-68f2e4b01d51 | -2.05955 | -48.85567 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 324c096a-00d6-3615-b0f2-2debc93d31e1 | -2.05895 | -48.85969 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38d1f367-3ae9-3d53-bff6-38435e843938 | -2.05526 | -48.855 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b39f63b5-f9c4-3c64-8f94-13babaa750d9 | -2.03964 | -49.71412 | 2024-11-02 05:04:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f31eec19-3aa7-3bc8-91a3-433096b62ed7 | -2.0356 | -49.7135 | 2024-11-02 05:04:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55722b34-16d3-3b96-ae8c-a1dc351fc4a7 | -2.02587 | -49.61034 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e077b583-090b-3ea5-8351-e8bf857e1e99 | -1.12326 | -48.7227 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2409a556-0c8b-33a7-9265-9f55945af204 | -2.22833 | -49.14613 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b242301a-cdc6-365a-846f-8cf5677ae03e | -2.2247 | -49.14158 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a31ba4d-5efc-342e-a8b6-e7b0a82dd03a | -2.22049 | -49.14093 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a5709ff-5b3a-35a5-b2eb-5ad274be8f52 | -2.21983 | -49.14214 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1196ea06-c15a-3b54-a1ff-0bf443c27f53 | -2.21628 | -49.14027 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e668b914-03e0-3b77-9818-406b479c652b | -2.21563 | -49.14148 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7399a8da-012a-3a20-af60-d095dc142834 | -2.21399 | -49.15576 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2e5504f8-f2ef-3cb3-8e36-1eeb69857ae1 | -2.21323 | -49.15693 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99900617-9265-347e-84fa-288c4ec3c049 | -2.20416 | -48.84723 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5b7256b-f230-377d-865d-bcb27b58a73e | -2.19704 | -49.17811 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c05610c-405e-33c5-a112-0d460490b649 | -2.19557 | -48.84591 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bc23695-fb03-3f59-a00c-deaf74912df6 | -2.19224 | -49.18134 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36025115-d3ef-398c-be03-cd5fba4889c4 | -2.18777 | -48.98435 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 464332c4-3f4f-37ba-9319-da0df283a814 | -2.1501 | -49.53591 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 762a4019-20ba-3eef-92c1-825b6c450fe3 | -2.14657 | -49.53164 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38ff781d-52de-3eee-9a86-3ca42a0fab3c | -2.14601 | -49.53527 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad674a83-9c36-3616-8778-f347147d7bee | -2.14466 | -49.12654 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0a724e51-bd6c-3426-856e-30da646bfb61 | -2.14304 | -49.52737 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 436c2fc1-28af-3c68-9919-43801f59c3d5 | -2.1395 | -49.5231 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0612e31e-3517-3c2d-b031-680b59ab6280 | -3.55634 | -50.30413 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dce410c0-af88-3af0-acd6-990a1d797ad7 | -3.55583 | -50.30759 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55efa4e0-7a52-34b1-81ee-985307f565db | -3.55224 | -50.31432 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fd922bd9-aa9c-3781-9c7e-1c90fb40d185 | -3.51165 | -50.28705 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16942130-3e55-3906-8ea6-0589391d1953 | -3.4669 | -50.28711 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc35e837-9a0c-3a21-a3fc-aff9c4dfc392 | -3.46292 | -50.28651 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 24730618-303e-3c9c-bf7d-956ab23e687d | -3.46242 | -50.16602 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d770e8f-7a41-3a9f-81ee-37ca06677a50 | -3.46241 | -50.28993 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 79a3115d-62f6-3192-ae57-5bdf039eddae | -3.46191 | -50.29333 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20197afb-5b56-362f-94d9-09d16fb60c38 | -3.46189 | -50.16943 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c8f41b1-aa48-3ba0-9d5c-8d12315e84d4 | -3.46038 | -50.30373 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e61abbbb-2036-37d5-bd94-42a677954d46 | -3.45988 | -50.30716 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d466db7-49ee-35a2-bf4d-d5fe8fcf6c89 | -3.45894 | -50.16194 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d589c93e-2d98-3390-8225-43874841cc87 | -3.45844 | -50.28932 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 84b5e26e-0175-3b00-95b9-9ae18c3bc661 | -3.45842 | -50.16537 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6482fa01-4333-3a03-8b69-87e8d44461f2 | -3.45793 | -50.29276 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8af19934-f6e2-3d44-8107-cf4c0535b49d | -3.4579 | -50.16877 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 977b83e2-68b8-3927-a476-6c5762e79108 | -3.45737 | -50.1722 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd8d9af7-65cd-30ef-bb5e-1b67d251489c | -3.45494 | -50.16127 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bf594c0-cc73-3d12-82b3-524551ee032c | -3.45442 | -50.16472 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a7f120a-89bc-3a0b-bd89-9f88a806b251 | -3.4539 | -50.16811 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e589e76-baad-3e2f-b8cc-08bd38249d28 | -3.45228 | -50.17868 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e14cca3-03c3-3c7b-ac31-8e56b8ab6ad0 | -3.45202 | -50.15358 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce65583a-0ca8-31a4-ad33-ca3854956e3d | -3.45175 | -50.18215 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0cd18a7-3eb6-38b9-960a-838edfa51e65 | -3.45148 | -50.15709 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc23a950-cb0c-3af4-936e-a05a65e934be | -3.45094 | -50.16063 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5dd6bf2d-eca2-3ef4-9099-495c1338133c | -3.44828 | -50.1781 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b039d3f-72eb-3595-beaa-49f9b6a66615 | -3.44775 | -50.18157 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccc8301b-ae39-3279-a221-6e8519b8589a | -3.44375 | -50.18098 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 688d6be2-4f76-31ad-8527-1700b8fafe7e | -3.42924 | -50.24947 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9be917a-78fb-34c6-8a48-fea6552873a0 | -3.42526 | -50.24884 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee28dfcb-2c05-3913-a265-d5379054cbeb | -3.41954 | -50.2865 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 679bb46c-3311-3fba-8ea7-f0225fe905a9 | -3.41902 | -50.2899 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a17b7227-0541-3e22-b957-b2317327ade5 | -3.41557 | -50.28589 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43646048-61fd-3a0c-b2fd-cb21081a9388 | -3.41505 | -50.28931 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d54991f-b1c8-350a-ad66-cc5f816e9c3e | -3.41159 | -50.28528 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dd17f22-d338-38c3-8151-dec11d80bb9f | -3.41107 | -50.28872 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e3fd23f-ac78-374e-b86a-eb138cb94362 | -3.37391 | -50.2655 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3f61e34f-7359-38e5-a9c9-614db017ac46 | -3.37341 | -50.26886 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f44c4a53-0aa2-3b87-8e60-85e0ed5f3039 | -3.37043 | -50.26158 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4efc3c59-7f8e-31d2-b367-b06f7f34a585 | -3.36993 | -50.26494 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1bf97bc2-68c8-3328-9b29-4f6f33cd1ef3 | -3.36943 | -50.26828 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b21ab26d-f810-323f-913a-d9f7924b01fa | -3.36477 | -50.16167 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f18b35b8-6f0c-35b3-b79e-b95ddc0450a3 | -3.36425 | -50.16518 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bf226dd-491c-3ca7-be3d-aa3df1085a0e | -3.36287 | -50.16186 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3cc297bc-b235-32a5-b226-c878126f5045 | -3.36232 | -50.16538 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76cf9746-198e-3539-80e9-2a55c2f11311 | -3.36077 | -50.16103 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 275e8557-3d1b-35fa-a86c-19297fdb66fa | -3.36025 | -50.16455 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2d6f418-c030-3824-a922-93dea2090882 | -3.34454 | -50.25434 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1267429a-bceb-31b2-8be8-7446e6dc5a75 | -3.34401 | -50.25778 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 49fe4bfc-13fa-311b-8c52-9edb525ef518 | -3.34057 | -50.25374 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e5981f0b-2bf4-3af5-bd43-edd6a8164716 | -3.32422 | -50.17377 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aab467a9-334f-39be-801a-1733786326ff | -3.31332 | -50.29909 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e928b751-564e-35a4-8898-16526c665b20 | -3.29441 | -50.23608 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7017cc57-344c-3e8a-8ffa-13a18ff2a5fc | -3.29097 | -50.23193 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1043ebe4-15d8-304e-91a2-ac576aa1a24d | -3.29044 | -50.23543 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcaa0135-7ffd-379f-af3a-a16660c88e0a | -3.28647 | -50.23478 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ce93291-bd56-3674-b7a7-4d3d182d4dfd | -3.28249 | -50.23414 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 52b85e0d-6fb3-32a9-8d54-e76c124fc5ef | -3.28197 | -50.23764 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0321fc16-edf5-38b6-8207-d1130234e348 | -3.27852 | -50.23352 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8cbe538-1bc4-304d-a917-88ea700c27fd | -3.25621 | -50.19165 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06fc52ae-5290-3806-9cef-036ad43604f4 | -3.25222 | -50.19104 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a6ae1f0-7f14-3554-aac6-442d02a95be5 | -3.24976 | -50.19134 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f80ca99-3c1c-3df2-8be6-1c9606209604 | -3.24824 | -50.19042 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adc0ee67-76c5-3f3c-ac69-bed8090034ef | -2.74872 | -50.44421 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19684181-5908-3856-9d75-14a44b59b93b | -2.68086 | -49.33058 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 761c1059-d411-3b87-b3f5-9b67971aa42d | -2.6629 | -49.83702 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff955f4b-decb-304c-9a51-a61c1eae5cc9 | -2.66237 | -49.84059 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 242ce0d1-baa6-321c-9a6a-6fc64628311d | -2.66184 | -49.84415 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd1495b9-a5e6-36fb-91aa-451eaccf32fa | -2.6578 | -49.84353 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c9d2790-51fd-3777-8783-f7aaf92ab39a | -2.65376 | -49.8429 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README63.md)
