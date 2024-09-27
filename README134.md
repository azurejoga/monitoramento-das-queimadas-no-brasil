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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e6a277a-763c-3f73-8fad-0fdbdfcce71f | -11.0972 | -46.1673 | 2024-09-27 12:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 479.8 |
| 426e0766-8628-3512-bc1f-c9c652ef5d88 | -11.0969 | -46.19 | 2024-09-27 12:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 61977e55-4319-3c7c-ae1c-e48493b16131 | -11.2531 | -47.1366 | 2024-09-27 12:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| ff2f72dc-86fd-3960-83f3-3452b0914aad | -11.222 | -45.536 | 2024-09-27 12:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 8345a85b-3018-3a5e-8505-1ebf2323de68 | -11.333 | -46.9024 | 2024-09-27 12:16:11 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 14297e83-035b-30af-b926-0e8784b6ff91 | -11.6605 | -44.5041 | 2024-09-27 12:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 380.6 |
| 6bac3176-d366-3acb-a413-9b4e7d275d5d | -11.6409 | -44.5303 | 2024-09-27 12:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| c5db55d0-2b30-370a-8980-2b88076b2b18 | -11.6797 | -44.5012 | 2024-09-27 12:16:13 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 83613b26-e762-3459-9408-7dca1b31b647 | -12.2666 | -50.5317 | 2024-09-27 12:16:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8207e389-8438-3678-a5c3-106ddf4a8bd6 | -12.343 | -50.5225 | 2024-09-27 12:16:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 61ef542e-d6a6-3254-887c-29dd3a533e96 | -12.3242 | -50.5033 | 2024-09-27 12:16:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 02f1ec7f-f440-3c94-a30a-3e121854dbda | -12.3239 | -50.5248 | 2024-09-27 12:16:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d1fe4238-0c7e-37c4-ad59-cfd15c45169a | -12.286 | -50.5079 | 2024-09-27 12:16:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 44532729-bbc0-313b-a5ae-a32f147b7187 | -12.3434 | -50.501 | 2024-09-27 12:16:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 310.2 |
| 49c3f887-dc39-3edb-8e08-3224cfd9ab48 | -13.235 | -45.6245 | 2024-09-27 12:16:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 320.2 |
| ddfe4f5b-94c8-34a7-b93b-4063b0802214 | -13.2156 | -45.6276 | 2024-09-27 12:16:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 54c8f517-6411-31f3-aad5-77c6a61756bb | -13.2152 | -45.6507 | 2024-09-27 12:16:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| bb6781fd-c226-32e8-94c0-15566f3e639d | -13.2675 | -51.307 | 2024-09-27 12:16:22 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9a63ea29-7408-3c3f-b934-4d7ac2850fd8 | -14.7119 | -45.463 | 2024-09-27 12:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| d373cb3e-2e2b-34fe-87d5-9bf856464ab8 | -14.7114 | -45.4863 | 2024-09-27 12:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 06d009ec-c63c-3d89-95ad-3b031f1b5805 | -14.8832 | -51.4561 | 2024-09-27 12:16:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| be54a364-5f5b-3a9e-86d6-cbc68b9135a6 | -14.9026 | -51.4534 | 2024-09-27 12:16:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 5a4eab92-6444-362e-9214-68610b46af03 | -18.0553 | -44.3645 | 2024-09-27 12:16:47 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 5390466d-9ace-3f6d-95f4-7986714ebe15 | -9.417 | -51.4426 | 2024-09-27 12:26:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 8621404f-1d43-348f-bd88-309b0649525c | -9.4168 | -51.4636 | 2024-09-27 12:26:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a010cbb2-1b1d-33b0-b0a5-51d2bf6fd050 | -10.0136 | -53.467 | 2024-09-27 12:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 196.2 |
| d0179d57-caf5-3810-a72c-3ea205f89255 | -10.0139 | -53.4464 | 2024-09-27 12:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 404.9 |
| c76efb4a-9113-3ad5-bfd0-abfb430e9a64 | -10.0134 | -53.4875 | 2024-09-27 12:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 3aef8aca-37f9-3e57-978b-649f5aaea467 | -10.0322 | -53.4859 | 2024-09-27 12:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 237.2 |
| b24c094f-44d7-34a1-8c10-aed73e8e22f9 | -10.0324 | -53.4654 | 2024-09-27 12:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 614.0 |
| 9a848bb2-0a2f-379d-8908-d69940d1b8d7 | -10.6639 | -45.8838 | 2024-09-27 12:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 770bac46-12a7-329f-8c57-3dda2d1ff767 | -10.624 | -46.0023 | 2024-09-27 12:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 2e7c4835-c21a-3a1c-9057-883d36f2cbb7 | -10.6643 | -45.861 | 2024-09-27 12:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 0c409c76-95ff-35ae-aadc-e3851399d410 | -10.8334 | -45.998 | 2024-09-27 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 466fd6bf-3d55-327a-86e9-731e62e2e237 | -10.8146 | -45.9778 | 2024-09-27 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1c56e925-1aa5-3b13-b447-87b58046e9f1 | -10.8337 | -45.9753 | 2024-09-27 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| c475d192-9172-37a8-b979-06ffd8cfc881 | -10.8143 | -46.0005 | 2024-09-27 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 73da5e04-af4f-391a-927d-90787cdf64a9 | -11.0976 | -46.1446 | 2024-09-27 12:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| e9a244a5-2425-3eb4-826d-4be9685c063e | -11.2025 | -45.5616 | 2024-09-27 12:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.1 |
| d942a8d3-0ade-3170-bcdc-eff206ffe46c | -11.2029 | -45.5387 | 2024-09-27 12:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 54bca60d-0964-376f-bcf4-66d62dd09c58 | -11.0972 | -46.1673 | 2024-09-27 12:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 419.6 |
| fced9c81-d323-3cde-93a7-18d73a897799 | -11.2217 | -45.559 | 2024-09-27 12:26:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| f3ee4c7e-a59d-3918-a0a2-fa1855e8cd94 | -11.2534 | -47.1142 | 2024-09-27 12:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 174.1 |
| ebb5032b-ff2b-3bad-90b8-badabe93a20e | -11.2531 | -47.1366 | 2024-09-27 12:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 2d8c338c-6143-3138-ac77-1810cef41025 | -11.6605 | -44.5041 | 2024-09-27 12:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 4bbfc266-0dae-3f83-bb01-dff8d7c52036 | -11.6409 | -44.5303 | 2024-09-27 12:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 80872779-69c8-358f-9f71-ee00bde478a1 | -12.2367 | -45.5045 | 2024-09-27 12:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 01049f72-f573-37d2-9d34-48f3f2c89a61 | -12.3434 | -50.501 | 2024-09-27 12:26:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 6abedd9d-0722-3da5-9640-da2f946416b0 | -12.3242 | -50.5033 | 2024-09-27 12:26:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 6561b5c7-1c18-36f0-97ed-32b727ee0d15 | -13.2152 | -45.6507 | 2024-09-27 12:26:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 1aee30dd-e467-3d93-818a-15438a38e69a | -13.2675 | -51.307 | 2024-09-27 12:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 170.8 |
| f3257e19-5372-3f1b-a8fd-197a5e8f9bea | -13.235 | -45.6245 | 2024-09-27 12:26:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 3e8d801a-fe39-39eb-965c-379617d742a9 | -13.2156 | -45.6276 | 2024-09-27 12:26:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 97bdf82a-ac43-351c-b803-4dcb3d229683 | -14.7119 | -45.463 | 2024-09-27 12:26:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 225.7 |
| da7de124-84b8-3fa8-bf79-6303d042ade7 | -14.7114 | -45.4863 | 2024-09-27 12:26:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 82752055-5a47-3a4a-a18d-dae025922ff0 | -14.9026 | -51.4534 | 2024-09-27 12:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 6194e17f-3499-3f64-acda-4487d9ebdddc | -14.8832 | -51.4561 | 2024-09-27 12:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 2e9b8c6a-83ac-3bc0-b18c-e0866338db78 | -18.0553 | -44.3645 | 2024-09-27 12:26:46 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| cd983bec-f6f3-3a79-9738-135ce9a4eaf2 | -7.3606 | -44.1035 | 2024-09-27 12:35:48 | GOES-16 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 40596105-8184-3c80-b679-4db15d5a1e09 | -9.4168 | -51.4636 | 2024-09-27 12:36:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3caa73e0-ef84-393a-88ed-44b799b0e029 | -10.0136 | -53.467 | 2024-09-27 12:36:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 274.2 |
| 57c3b005-8d7a-3b8d-afae-d7dbefb5d14b | -10.0134 | -53.4875 | 2024-09-27 12:36:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| eea1a2ab-a508-3a59-9cc1-31a52e22e261 | -10.0139 | -53.4464 | 2024-09-27 12:36:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 573.6 |
| 6633a594-1c3b-30de-87d5-f0a9a024b968 | -10.0324 | -53.4654 | 2024-09-27 12:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 466.5 |
| 1f9ed35a-e89f-3823-8942-bbc561908a60 | -10.0322 | -53.4859 | 2024-09-27 12:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 5137e907-d802-3215-9df5-ccd26d0eeba6 | -10.6438 | -45.9544 | 2024-09-27 12:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 067a5aa9-d97f-39e0-89aa-ff0a1e74a5b5 | -10.6434 | -45.9772 | 2024-09-27 12:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 37de2a46-908e-3939-bc2d-f53742189565 | -10.6452 | -45.8635 | 2024-09-27 12:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.0 |
| af677b75-c02a-3653-a7ef-6c1112609036 | -10.624 | -46.0023 | 2024-09-27 12:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 7438d8c9-0366-3200-b469-b1aa320aba3c | -10.6449 | -45.8862 | 2024-09-27 12:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 471f3d60-2ab2-35cd-8730-7244f9fb871e | -10.6244 | -45.9796 | 2024-09-27 12:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 5d33fc0d-9b0e-3c2f-99be-8e00b7d304a7 | -10.8337 | -45.9753 | 2024-09-27 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 8baf4c55-7a67-33f4-ba7f-c426419de4ba | -10.8334 | -45.998 | 2024-09-27 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 8d7fdd5b-ab9f-3d72-8552-65384de11e99 | -10.6639 | -45.8838 | 2024-09-27 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| ab9f7bd4-0c28-3b6c-836f-233a1110d117 | -10.6643 | -45.861 | 2024-09-27 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 278.3 |
| 8eb13667-e0df-3078-927b-baf274af3419 | -10.8143 | -46.0005 | 2024-09-27 12:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| eeb44377-96e6-3580-9515-db4e16242e8f | -10.9148 | -45.669 | 2024-09-27 12:36:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 620c207d-3719-36fd-bf36-e08496308552 | -11.2025 | -45.5616 | 2024-09-27 12:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 5f328554-e665-3772-aa2a-9615055eb920 | -11.0972 | -46.1673 | 2024-09-27 12:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 430.5 |
| 925988f8-59a5-35d0-ae12-cbfd2189ebb9 | -11.0976 | -46.1446 | 2024-09-27 12:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 215.5 |
| b2f2a95c-a2ff-38ea-b997-61e3a37094d5 | -11.0577 | -51.3694 | 2024-09-27 12:36:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| fa302ab9-83a8-333c-a59b-6c6d9e141ddc | -11.116 | -46.1875 | 2024-09-27 12:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ad588be9-01ba-359f-a4d9-7e98ec9491f8 | -11.1459 | -45.5236 | 2024-09-27 12:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b095beee-f4ec-3172-b142-8a3fe1cbbd56 | -11.0969 | -46.19 | 2024-09-27 12:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 7a2c631e-d1ba-32f6-8ec4-2deb920f129a | -11.2534 | -47.1142 | 2024-09-27 12:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| c24c62fa-0163-3912-b0f8-4f69e66455d1 | -11.2217 | -45.559 | 2024-09-27 12:36:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| fb4ff32b-0d3e-323c-b52d-803176d6ea2b | -11.2531 | -47.1366 | 2024-09-27 12:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 286780f5-6093-3be6-a681-eee58a4c3bbd | -11.6605 | -44.5041 | 2024-09-27 12:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 224.8 |
| d6365711-b354-35f8-b54a-06d3fbd6c79f | -11.6409 | -44.5303 | 2024-09-27 12:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 602138cd-aab3-33e1-b83d-d09deab26b71 | -12.3242 | -50.5033 | 2024-09-27 12:36:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 271.7 |
| ba4be803-91fc-33bf-b474-d6aa54d708ff | -12.3434 | -50.501 | 2024-09-27 12:36:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| d8ce81b4-079c-3252-9372-8d0a3fc5893c | -12.4786 | -50.3986 | 2024-09-27 12:36:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 4c3ad13b-586c-381d-80ae-3fe8b9f15f7a | -12.4782 | -50.4201 | 2024-09-27 12:36:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| d7932474-4559-3b10-abff-f6ec89012c58 | -13.2482 | -51.3094 | 2024-09-27 12:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 9248fce9-7b60-300f-b667-21e7ecfe5e11 | -13.2156 | -45.6276 | 2024-09-27 12:36:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| eb101737-2eb8-38c4-88ec-7b940b071a68 | -13.235 | -45.6245 | 2024-09-27 12:36:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 333.5 |
| 3ea85016-15c4-34b1-8e6f-4a5f44dc05fe | -13.2675 | -51.307 | 2024-09-27 12:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 46fb7c6f-67f6-3c6d-8032-d7b99eb55a6a | -14.7119 | -45.463 | 2024-09-27 12:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 978f8349-33d1-3396-920e-a9591bf21c07 | -14.7305 | -45.5061 | 2024-09-27 12:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e5135014-6258-3881-90ba-da86aaa4712b | -14.7114 | -45.4863 | 2024-09-27 12:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |


[Clique aqui para ver as próximas entradas](README135.md)
