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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 170acd8e-c682-3930-ba8e-cba1d6ca2ba6 | -3.03386 | -51.46364 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 431e2cf6-e047-30ae-b3f8-72fd3dbd53e1 | -3.0298 | -51.46265 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d302ad1-c511-319f-99d4-200e3e99b9eb | -3.02935 | -51.46559 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfc27b19-7d1b-37c1-9ccd-8c184451c7de | -2.92141 | -51.70623 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36b9f203-fcad-31ba-a35f-8d77a3056867 | -2.91322 | -51.76136 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3902947b-da2a-32d3-bfd0-8ad203bfc4fe | -2.8866 | -51.82936 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dcb693c-b82e-3067-a906-630c3bcb9f40 | -2.88361 | -51.75686 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10271fce-e804-3c8e-96ff-b64a0c91d231 | -2.88296 | -51.82979 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d224ff80-bf64-31b6-903f-1bc3cd04d1a1 | -2.88287 | -51.75596 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58ab8294-b370-3499-9e39-73a84599d947 | -2.88167 | -51.82875 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11af2e66-788e-3b85-be0c-33e164df1b7b | -2.88084 | -51.83411 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5c9c70ea-b781-3171-9b1c-e90d81238c99 | -2.87875 | -51.31007 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ece807-ca34-3112-b04c-6799e45c0474 | -2.87831 | -51.31304 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b608746a-1630-348e-87ae-c205ab6043c1 | -2.87366 | -51.3093 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 927caf09-2516-3303-a2ae-9b445e9417e9 | -2.87322 | -51.31225 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02841da8-a729-3ad1-937a-7755f4943deb | -2.84569 | -51.8013 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9eb35ba9-d0f8-3fa1-8590-3fcd6ffad7df | -2.84486 | -51.80676 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ebb31e95-f102-341f-aa0d-d01a741e7c9f | -2.84078 | -51.80054 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84292a04-2231-3134-ba35-148e97dd30bf | -2.83995 | -51.80603 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed601d54-7837-3d82-a0e1-69949336ba1e | -2.83912 | -51.81148 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a08ab4ba-2399-37fd-860c-5fde7d2147f8 | -2.83504 | -51.80525 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85b39097-818d-3b26-bf33-aa063552a48c | -2.83421 | -51.81073 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec21b74d-506c-3ea5-ae24-1cd79cbfada5 | -2.81554 | -51.59742 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eea08c8d-4ba7-3210-ac7d-64a12274c16c | -2.8147 | -51.60307 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef912794-4256-39c8-8f8b-ab8818918238 | -2.8143 | -51.60199 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab46016e-d8ac-380d-98ca-8dd6f579f4f8 | -2.81281 | -51.34468 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c176b473-e661-3ce0-93b6-6988cdd9934a | -2.81237 | -51.3476 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c9b6c8ce-defc-3833-97a3-839c1f06a855 | -2.79986 | -51.80531 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb3fd1bc-c98a-330d-be6c-ed18dd135a07 | -2.79496 | -51.80448 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a93ca32-dd89-32e2-8287-7598ba694093 | -2.64978 | -51.74558 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f4ebb06-5bdf-3557-a0bc-de02292d0423 | -2.64894 | -51.75105 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| af298947-afc7-3422-bb4b-d9ac9c945f50 | -2.64654 | -51.73388 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 378520d2-8e4c-383a-b5a7-5b827210e5d8 | -2.6457 | -51.73936 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 924ae21f-4053-3f96-9622-51dc51d9ee54 | -2.64486 | -51.74483 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49a9b71c-3a0d-3ce6-9af6-b45fd829f364 | -2.64402 | -51.75031 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31499592-1e34-3739-bb56-befd44fd521f | -2.64246 | -51.72765 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3aac0dea-ab06-3f31-831b-ffd17a089b74 | -2.64162 | -51.73313 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7153c210-3b43-3b2d-835c-73797bf330cc | -2.64078 | -51.7386 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf664d5a-5f54-32a2-b103-608a7df013f8 | -2.63994 | -51.74409 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 473e8f98-3624-3280-ba61-85ce9b663e6b | -2.63753 | -51.72689 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9a67edb-c3bd-3bfe-a32d-29bbae2e34a9 | -2.57376 | -51.85048 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8db32d95-4b15-3106-8534-a4acc52b60e3 | -3.71993 | -50.71295 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7296deb-e8e7-32d3-91a5-53fce9f6204c | -3.71945 | -50.71625 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb295a80-537e-3c01-a189-9c3fc910942d | -3.34121 | -50.75435 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8ef3041-4b7f-3b26-ae41-2a8df5ec9831 | -3.34072 | -50.75758 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17cf84d8-1d99-346f-83f0-e29da9bbf2b8 | -3.3354 | -50.7568 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b03962e6-5571-3155-8bae-6b61c9913fa9 | -3.33491 | -50.76004 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9923b593-a884-3b56-9ea4-ec542602abd2 | -3.25838 | -50.65042 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13c388ba-a056-3fe0-8cc6-b880793c6178 | -3.25789 | -50.65379 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa35724f-ff10-3ea1-85ba-1f5723e17b50 | -3.2574 | -50.65715 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44ebbc0c-afe9-3f73-ae3a-7a1f58c7f6b8 | -3.25697 | -50.64382 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c769e7a-387d-3203-bf29-dd19955900f9 | -3.25645 | -50.64719 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1996ae0-8a93-33b7-978e-216a66bbbd97 | -3.25594 | -50.65055 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03828f30-9f56-37f0-a28d-fb8b8ecc822e | -3.25543 | -50.65392 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca38eb0f-ca1a-38b3-ab53-af0bb6d18641 | -3.25399 | -50.64289 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0cbe522-5de8-3c83-a608-e423e6dc1463 | -3.2535 | -50.64629 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec8db874-d888-3519-aeaf-db2b1b45d714 | -3.25301 | -50.64968 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6661e317-685b-30f5-9b33-dd480391f17c | -3.25253 | -50.65306 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0067f9c-ebb4-3e3f-b4bc-27df4e2bc4b7 | -3.25161 | -50.64305 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3f10902-556b-35e9-95fa-3dd26664c604 | -3.25109 | -50.64645 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5b9beaa-8ca6-315b-b3e8-0bbbde296f2a | -3.12784 | -50.60746 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69fada01-5281-3c41-a933-b35cc42791af | -3.12297 | -50.6034 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dfe74f2-25a2-3e7e-bf92-06d85a7f6e7b | -3.12249 | -50.60663 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49868d44-5a39-3f06-a087-14fa6a8c2027 | -3.45621 | -51.64221 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33f784a6-bf75-3096-9d80-d22ac9cf6d42 | -3.40132 | -51.53094 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f34187a4-8261-3c17-a045-d1322e0e5652 | -3.34664 | -51.52817 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08998615-e00e-308e-884d-aaa8229c1d4a | -3.3449 | -51.52847 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5381964-1b2d-32bc-8225-021777830cd4 | -3.3416 | -51.52736 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37a05d30-c24b-3c9b-9f95-e979acbd24e6 | -3.33816 | -51.6171 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee184d0c-14ea-38e2-a2c9-b681c950c098 | -3.33316 | -51.6162 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85c88412-04d7-384a-b437-81a83fda0a82 | -3.33229 | -51.62191 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7ddcf57-1d98-3160-bbdc-90b20fb0dedb | -3.25804 | -51.56938 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4663657b-c641-3808-809e-527f7fe6cc06 | -3.24442 | -51.55708 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1c9b71a-c477-380f-af2d-b6f9e6c190f5 | -3.24023 | -51.55055 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 727b98a3-14f1-325d-862e-6adbc87c6cab | -3.23981 | -51.55344 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8edb1343-a1c2-393b-ab2a-3ca91f81337b | -3.16815 | -51.08762 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f511f396-d9fd-30ce-80c1-e058531b965f | -3.10123 | -51.32333 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70dcfb10-d557-358b-88e6-34202cc0e30d | -3.10036 | -51.25887 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8a79797-3abd-399e-bb6b-f3c39a97e1c0 | -3.09991 | -51.26186 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd102238-20af-3da4-87ad-52f6c158c790 | -3.08406 | -51.11904 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9d1c106-96fc-33ba-bec3-af1602682021 | -3.08272 | -51.12819 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4541c953-fbec-3ea4-b3b0-29c83bb78d38 | -3.08255 | -51.11863 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff82b7bb-d0c4-3811-b47b-6214babfdaf7 | -3.08209 | -51.12164 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 184db218-a17b-37bd-be9c-46ebe3b9f26c | -3.08163 | -51.12467 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5acdf512-2297-3d16-b812-10868ec38827 | -3.08116 | -51.12774 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75a928d9-01be-3cb6-af86-cf027e6a70f7 | -3.08096 | -51.1403 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9da9e7c8-21a6-3950-9b4f-9c2ddfd19e7b | -3.08069 | -51.13075 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd307c6c-af21-3885-8ca4-279882d670dd | -3.07977 | -51.13676 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ace7d854-6102-3201-9247-62b5d09b21bf | -3.0793 | -51.13984 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 923d4c5f-7adf-3215-92d4-eb76d55095b9 | -3.07889 | -51.11819 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8bae56b-ace1-3688-83d1-92782174f9b7 | -3.07846 | -51.1212 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70402d58-0041-3864-bc42-df380164adc7 | -3.07802 | -51.12423 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee7c508b-008a-3466-9b8f-480ef1780dfb | -3.07647 | -51.12382 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa390dc1-cc22-3fb0-80da-4b172837f128 | -4.52875 | -50.98392 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9027b3d-7018-389b-9de9-14cb04733011 | -4.52828 | -50.98721 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c39d5d35-24be-3e3e-a7eb-338c3eae0018 | -4.47595 | -50.99 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5015a1ec-4cfd-309a-82cc-eacf53057515 | -4.47547 | -50.99329 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72f7b9cc-45b1-3058-95ce-3ca964fdd0c1 | -4.47498 | -50.99659 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35f6f041-f451-3ae6-8a39-4c01051ac072 | -4.46966 | -50.99577 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17a8a757-4d7f-34f8-b281-36ea19206872 | -4.46917 | -50.99911 | 2024-10-28 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README81.md)
