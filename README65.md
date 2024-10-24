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
| 02c58f25-9bb2-3588-b098-d2fb0ab9dd42 | -3.79614 | -50.16704 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22390355-3085-308a-9bea-70a5db4b403d | -3.7771 | -49.95452 | 2024-10-24 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e29be09-a6d6-3889-97cb-a746d7ec5386 | -3.76276 | -50.38572 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96e01e7c-aae3-3e76-ab68-8020b62f7290 | -3.76213 | -50.38987 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c723ef8-7cb0-314e-b645-0a291a84f8e3 | -3.75978 | -50.38104 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3275a603-c249-3a5c-b60f-6ce40beaf759 | -3.75914 | -50.38517 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a29e3f6b-8731-321a-9781-707d9c859c27 | -3.66299 | -50.11549 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f422c031-993d-3e71-982e-556b08007e0e | -3.66232 | -50.1198 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2ba48dcc-8717-3d1b-8296-c4b54a94ff94 | -3.66166 | -50.11774 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 746c0577-0769-340f-85ef-817011fd05c7 | -3.66165 | -50.12408 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2ff69238-e78e-3f22-a341-0a74a6a67d71 | -3.66101 | -50.12205 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e02677e2-d803-3ecf-8078-3ca10421ce32 | -3.65933 | -50.11491 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69d04e64-3423-30ec-8faf-34421da81723 | -3.65866 | -50.11922 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1acdb255-e103-3dc1-ad01-a80c0c6c75e9 | -3.658 | -50.11715 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bf0cfa69-7507-3d97-a489-62562406db95 | -3.65735 | -50.12147 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1da1317d-a3dd-36b4-ae3d-af90e4cd91d0 | -3.655 | -50.11864 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d48361e6-e17f-3121-88da-9dda39ee0f26 | -3.63535 | -50.1244 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24197dea-9bb4-375b-87c2-983723a65dfa | -3.60625 | -50.58125 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5057cf4f-a280-39d2-afb5-269433fbb398 | -3.6033 | -50.57664 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6c70b5b-0b88-3d49-8264-9b5b6e879ae3 | -3.57767 | -50.56594 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65bbfd3a-3654-38c9-8adc-9f62fdec2e22 | -5.00119 | -49.78942 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 962630cb-f14a-363e-a25f-0e227ba22234 | -4.55119 | -49.66243 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b58b5764-5312-3fa0-918c-1366c5ebba7e | -4.44838 | -49.65333 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ddb89a8-0be2-3513-898a-6cadcbd6448a | -4.44767 | -49.65795 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a805a9e5-1629-356f-845a-f4dd67d1c25a | -4.39382 | -49.75757 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe299e85-f136-3d98-a653-b3f493f31e06 | -4.39005 | -49.757 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d026b2e-bd1b-34a1-93d2-114764abd656 | -4.38937 | -49.76151 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 972453f7-1858-3f27-9b27-d8cf99f27ae0 | -4.37712 | -49.41531 | 2024-10-24 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 353e8c60-f9ca-3a33-827a-ebe6e1cf584c | -4.16886 | -49.26233 | 2024-10-24 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30513a52-8915-32bb-9ddc-d961e1c4311d | -6.10623 | -51.11613 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dbc306f-c0ff-3213-b354-cd579c234993 | -6.10216 | -50.96584 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d744c128-7863-3167-8888-c6ec9c506147 | -6.1009 | -50.97408 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cb04786-5096-35fd-a462-bfff6748fb48 | -6.09856 | -50.96526 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 990c7c0c-3416-3f9c-994c-b6aaff2ff1ae | -6.09793 | -50.96941 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c32e5e2-80b9-3623-a4e1-fc5e3032cf3e | -5.93101 | -50.99185 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43ff089f-0c5b-34b2-96c7-9575ae39dac2 | -5.93039 | -50.99599 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85b4a225-0683-32c7-9a91-b2edc5213108 | -5.9268 | -50.9954 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e93424a-a5e2-3037-8a0f-d9a911c2e3ac | -5.29859 | -50.98653 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caff4914-cc22-3fee-8150-0468435bccff | -5.29674 | -50.99867 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e00dfe56-cc20-3d47-882e-3202176705a8 | -5.79696 | -50.16359 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4973df32-2edb-3926-99e9-4455b6670786 | -5.79627 | -50.16812 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d97be019-2957-31b2-bf54-300f516340d1 | -5.7932 | -50.16304 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58d990a5-c38e-3ead-92d1-b321b7d725ab | -5.79251 | -50.16759 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41495bfb-474e-3800-a151-83048b4c5160 | -5.75747 | -50.22171 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70e2571f-f12c-3e4b-852c-aa160663d11c | -5.7568 | -50.22613 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbea1bf7-1d66-3a3b-8d8d-39790534d2bf | -5.75373 | -50.22112 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbf04faf-ffc4-346a-bc2c-e2154684c386 | -5.75306 | -50.22556 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b4bb58a-a329-3a6f-81fa-a7ed0359fc69 | -5.64729 | -49.7304 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bad3255-a1ff-37e6-9e69-81228e305b4c | -5.61672 | -50.00634 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70a6e745-0f00-3041-ba30-7a374a7f3296 | -5.59381 | -50.10532 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8ab4e1b-0523-36ad-a3ce-0b45dd4a62ec | -5.59005 | -50.1048 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eab31fe-b02f-3c57-8f0e-a0486d80bf79 | -5.34015 | -49.51618 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9102bf31-1e19-3213-8f5e-53668aae91c5 | -5.22034 | -49.94858 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6da5cd13-8ab2-3a25-8ec9-7b34b39c2375 | -5.21966 | -49.95313 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caa80e7d-955f-35f9-84ef-25af5a5bc516 | -5.21656 | -49.94805 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7ed284b-62c2-3937-bb20-cbfa57f20ba4 | -5.21588 | -49.95262 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fcd2189-4525-3152-be9c-23709205d290 | -5.19555 | -50.16543 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa777298-971a-3dde-99c7-6cec5c59d052 | -5.18271 | -50.07237 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 735e67f1-c1b1-3c70-9692-6471617e3be2 | -5.18205 | -50.0768 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22624299-4a9f-3843-885a-5d49599dec87 | -5.18192 | -50.07458 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b30174f1-acc1-33b5-98ae-9e939845ccca | -5.17896 | -50.07183 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8d1543e-208c-3d68-8522-ada11959d348 | -5.17831 | -50.07623 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3edc9cbc-56a0-32d7-b924-c60200bfd588 | -5.17817 | -50.07402 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c761387b-5319-3d40-bd67-3e7ccec2926d | -6.22969 | -50.88519 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c17a005-a88d-3ac5-878c-044641e131b0 | -6.22776 | -50.89775 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78865e41-65b8-3023-a60a-cafabce88a9a | -6.22669 | -50.88052 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea083f34-0802-3e49-a72d-3f783c66c19a | -6.22606 | -50.88468 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e276315c-8237-3490-9a45-7e2ab0111f98 | -6.22542 | -50.88884 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93c44bc1-fcad-358a-98b4-ebd767e7f96a | -6.22414 | -50.89721 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 357eefb2-c3d1-3ace-ba87-e18623367751 | -6.2237 | -50.87583 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 177245a6-080b-39f6-8290-081afa37860e | -6.22306 | -50.88002 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4c26c26-330e-3938-8d0a-a1e82b0df8d0 | -6.22007 | -50.87531 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 723bdef8-2adc-3d5f-87cd-f77aaef8bd01 | -6.21943 | -50.87949 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ee5a660-73a5-3d50-8574-08dd4fbe4b62 | -6.21047 | -50.86517 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9342108b-1021-36b9-b417-cfd019e47cfa | -6.20984 | -50.86934 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a3979c6-125e-3e27-a5dd-e2ca440dd90b | -6.2092 | -50.87353 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35727037-efc2-3448-93fe-394b3cadb201 | -6.20748 | -50.86046 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1c9b51e-eac0-302e-a543-2d14c25f8b6f | -6.20684 | -50.86466 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12f7c8c8-fd71-3f72-9f1a-34026ae267e4 | -6.20621 | -50.86879 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 664aadf8-2e23-38b3-a3d0-413a007513c8 | -6.20385 | -50.85991 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86bdef81-f2c0-3aaf-b87e-d0ae6e1a9665 | -6.20321 | -50.86412 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55e004b0-16ff-3c87-8ebf-275ecb192b05 | -6.19959 | -50.86349 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9fb39dab-8aeb-32a0-9d02-ac4e032b312d | -6.18871 | -50.86173 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d96cc74b-c47e-3af8-b33c-0ab55280f187 | -6.18508 | -50.86118 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b233c22c-9eeb-3190-af4a-df3c085228f3 | -6.18082 | -50.86482 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc004bac-34d4-3d73-8be5-feba7f4300ec | -6.17593 | -50.87266 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8a768b9-591d-39c0-b52c-1c7b62ccde9e | -6.1723 | -50.87212 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 356dad2d-2d61-35ad-9060-53d48cc0070f | -6.14477 | -50.93216 | 2024-10-24 04:55:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4463db15-914e-380b-9edc-cdfe06c21d79 | -5.94899 | -50.87237 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 601b64ea-d789-3300-8af2-a8acde5926e4 | -5.94838 | -50.87644 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e979ba26-b90f-3977-8ef1-5839bcebcab2 | -5.94535 | -50.87199 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b19a924-48c5-3ab8-a949-d3400d83227f | -5.94475 | -50.87593 | 2024-10-24 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29515cd5-be37-3d4a-bf2f-5b9e8c060e12 | -5.24193 | -50.89159 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc478995-4082-3c3b-a620-3ddaeec094b2 | -5.2413 | -50.89568 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 511b335b-8b27-36fd-aa84-1684e580e0c4 | -5.23834 | -50.89103 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc54a03f-ea86-3e7a-9d3e-4b8679e47538 | -5.23771 | -50.89513 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afd580ad-7d8b-308a-942b-6688cdca363c | -5.23476 | -50.89048 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5db2b85c-4496-35cf-821b-c88983da909c | -5.06443 | -50.44556 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e497bc7-d805-3ad6-a6f2-306bbb1871f1 | -5.06377 | -50.44988 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b6e55ea-d2d3-3892-9cd5-aaaa1e021c69 | -5.06011 | -50.44932 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README66.md)
