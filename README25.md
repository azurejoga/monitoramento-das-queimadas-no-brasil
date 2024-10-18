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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fb8182a-3db1-3f4d-8788-0dc6584e6ea9 | -4.36615 | -48.49326 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b68161a4-8f19-3d0e-8add-fa03c36b0c89 | -4.36541 | -48.48908 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fb15b7b-f6d6-3297-8f2b-0abfb4d4e825 | -4.36468 | -48.49323 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1644cf6c-329c-37b3-829d-3dcb929c6812 | -4.3615 | -44.57686 | 2024-10-18 03:51:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e12e96e-71a8-3cc2-824b-27e6918541ed | -4.36028 | -48.49226 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ca76050-0359-3835-b1de-f33262ca0f26 | -4.35959 | -48.49637 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ee0fdfe-5a49-384a-8063-00f945daf053 | -4.35882 | -48.49219 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b85e20b-8d44-3293-ac2f-da18104722bc | -4.3349 | -48.62809 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| debc0544-6b71-3d67-b59b-a6fea5f59830 | -4.33216 | -48.62307 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c4cd9e5-8818-3aa7-9a6f-6617e56f8542 | -4.33143 | -48.62741 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4083ec0e-a0bc-3afb-b1bd-d63d6860b242 | -4.32975 | -48.62275 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b31f9314-b45d-33fb-ba3d-cd44b3dffad6 | -4.32897 | -48.62715 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0510b754-1aa8-39da-aef4-3d3d7a11b8d6 | -4.303 | -44.51124 | 2024-10-18 03:51:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e85173c-5139-3434-95fb-8113a686d35c | -4.30062 | -45.49015 | 2024-10-18 03:51:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8018b2e5-b4ab-347c-8d93-14f8b71f007b | -4.29975 | -45.49542 | 2024-10-18 03:51:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03803b8a-d7e5-3c81-87c5-988adacbc185 | -4.27079 | -46.29028 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9040215-9b6d-371e-8f05-8c96dc68ec87 | -4.25014 | -50.98429 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 046b8c47-10ee-39a1-8aa0-73ea68c9a601 | -4.24903 | -50.99049 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d7c195b-2a63-39f3-93c4-0e8720ec6dd6 | -4.24858 | -50.9882 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 605686c9-c9fd-3a20-a667-8e8c2aa645f0 | -4.24227 | -50.98885 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 563bd3ad-f325-375e-9ceb-15d3ec71bdcd | -4.24036 | -45.73304 | 2024-10-18 03:51:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7511cd3f-bdd8-3b1f-97b7-57cc40c04dcd | -4.19703 | -44.22935 | 2024-10-18 03:51:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a898176-aaa7-3988-968a-3f3e91ec1fed | -4.19262 | -44.22858 | 2024-10-18 03:51:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1093a6e-d2d0-30c3-a3ee-fab25aa7b2b6 | -4.09739 | -50.7637 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b8ffa9f-aaa4-3dd8-8d98-002ea28384e9 | -4.09571 | -50.76139 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a300e153-150f-3e56-b78d-6214b284898e | -4.09461 | -50.76781 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66aa1670-b6be-30b7-a12c-2fd6e414ea8e | -4.09063 | -50.76249 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fee14597-a571-3ecf-9103-be5db38f7c80 | -4.05029 | -44.24212 | 2024-10-18 03:51:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b2ae37ef-b05b-3cdb-b380-01385c086ef8 | -4.03742 | -46.9439 | 2024-10-18 03:51:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1a10b00c-0829-37c5-b127-c83fd32221d0 | -4.03686 | -46.94724 | 2024-10-18 03:51:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 92f60717-ac58-342d-bf7e-5abca7f1ff83 | -4.03208 | -46.94307 | 2024-10-18 03:51:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 87784195-d90b-3b48-adfd-1a9a8d0767d7 | -3.93829 | -47.19247 | 2024-10-18 03:51:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52802e48-b7d0-37ad-bd50-daa24339a07b | -3.93773 | -47.19588 | 2024-10-18 03:51:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f43e79b2-3ba9-3b41-83d9-5fbb2f2eb2e9 | -3.93438 | -47.19146 | 2024-10-18 03:51:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 569f732d-14c0-33bc-806d-3cd735eb8d8b | -3.93378 | -47.19488 | 2024-10-18 03:51:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39418795-40fe-36fc-829f-7b934afd26c5 | -3.93287 | -47.19152 | 2024-10-18 03:51:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fe75515-96d8-3a2b-8623-85aae0a04acb | -3.91825 | -46.46484 | 2024-10-18 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b65be98a-269b-365b-abf0-4299826a4ac0 | -3.91766 | -46.46838 | 2024-10-18 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57d6a2f1-3105-331e-8630-0db0ed910881 | -3.90373 | -48.36992 | 2024-10-18 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 657f30b1-49e2-38a0-bce0-65061e68d074 | -3.90302 | -48.33868 | 2024-10-18 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd73cfc8-4b80-397a-9bfa-354764d6da0a | -3.90232 | -48.3428 | 2024-10-18 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf50a906-e12f-301f-82e6-bc4109c27b2e | -3.89861 | -48.36456 | 2024-10-18 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc21a4c5-fba7-37c7-be01-562a3b01dbeb | -3.89716 | -48.33774 | 2024-10-18 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bafee87-87c6-3644-ab6e-d618b108cb4c | -3.88379 | -45.7475 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db899b96-8e67-31ba-9289-d739a3dbe02c | -3.80873 | -51.31352 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae940311-4339-3bb2-be0e-c36f97f32c17 | -3.80285 | -51.3059 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c24323c-23da-30d9-88c8-f2795b0224f6 | -3.77945 | -44.77362 | 2024-10-18 03:51:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bdac6b1-9c07-3977-b6be-61ad20e867bc | -3.77867 | -44.77844 | 2024-10-18 03:51:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05885137-81f4-3eff-9186-717369b69899 | -3.7383 | -51.34332 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2d1c66d-2854-3790-a275-cec017562c20 | -3.73127 | -51.34205 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07eb96f2-5409-3c8b-becf-bf9f78bb9d49 | -3.71749 | -51.18594 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f07ef067-14e2-33b7-95cf-3e247efda5a5 | -3.70798 | -45.90557 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4602a91d-ad88-3390-880d-9d3ea68233f8 | -3.70752 | -45.90843 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b38d9d49-58ba-3c76-b112-d864a1041cd1 | -3.70707 | -51.08261 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad21d5e6-310e-357d-a51f-faca7d52206f | -3.70704 | -45.91137 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c013a503-9d69-3d9c-9efa-9f6119db496e | -3.70656 | -45.9143 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40475342-aa07-3b62-bcad-c7e668cb91c0 | -3.70589 | -51.08932 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2805114c-0486-3f4f-8f9f-a58e15bfd25c | -3.70348 | -45.90171 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37b8e218-a0a1-3639-9b58-81b65c0ae056 | -3.70302 | -45.90455 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 931d9207-73d9-378f-b3da-dc526e3899bc | -3.70254 | -45.90751 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 774995af-48f9-3ae1-936b-34585b535989 | -3.70205 | -45.91045 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 669ae69e-5759-3492-a29c-ca6aa5462b57 | -3.70157 | -45.91339 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 98f1b1be-6972-3f2f-8b7e-b0d2921b2b85 | -3.70109 | -45.91635 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 455c2fb6-4138-39b1-af12-8de49d44fd0c | -3.69801 | -45.90379 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f15470cb-8552-330b-8131-1c3536ec2c43 | -3.69754 | -45.90667 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c5fb4c73-10a3-3853-a13e-f210ec1db63a | -3.69707 | -45.90954 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b0f2d75a-dae0-3c93-9ca2-4b574130733c | -3.6966 | -45.91243 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c1bd88f6-99cb-374b-bf48-744d336e6b79 | -3.69254 | -45.90591 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a66b9c5d-eb8d-3859-8cf7-d8c6621a3926 | -3.69206 | -45.90879 | 2024-10-18 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 269b24d1-faf8-307e-95c9-2ae4bfcaae99 | -3.58971 | -50.58041 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da8d19b1-f766-3967-877a-d21b5b725a10 | -3.58759 | -50.57993 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 647a10e0-3058-3232-9368-efbfa120b9ac | -3.58296 | -50.57929 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e1c82ca-5df4-3242-bb7c-d0d9fcbb606b | -3.58085 | -50.57873 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeaf59af-0645-303e-ad7e-197fb947a50b | -3.57624 | -50.57795 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbe77c00-3efe-3684-88c8-0075dbcf1a78 | -3.57415 | -50.5773 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8139116d-cafe-3dd2-bab9-938a9c8ffa44 | -3.55987 | -47.3598 | 2024-10-18 03:51:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71505d6f-545f-310d-9e6c-124f4cc71c3f | -3.55924 | -47.36356 | 2024-10-18 03:51:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84efdcd9-d0f2-32b1-86f2-d4689dbb3c6a | -3.51376 | -50.32775 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01be9f92-b6b4-31cd-b6cb-afed4967e958 | -3.5071 | -50.32667 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf3bd895-686c-3073-823e-8187652926e9 | -3.50478 | -51.11259 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d906b0b2-1801-35d4-b0b9-4b92e8920e33 | -3.5035 | -51.11176 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 907ef341-b443-340f-97c9-999a2d02cd98 | -3.49783 | -51.11127 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1e51d70-f78b-362a-aabd-fab240722ae3 | -3.49654 | -51.11051 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6a18e74-0204-3273-b538-85b56ddda3a5 | -3.49483 | -51.68071 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aecf99c5-f945-3d13-b739-176a6e6fb2a2 | -3.49264 | -51.67915 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a1e19f80-e071-334d-8f26-4d1305821850 | -3.48763 | -51.67955 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f3e1826a-e7c7-3d1d-aea7-09726584174b | -3.45665 | -50.61292 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21771226-174e-3393-b2e4-f908b998d887 | -3.38631 | -44.33142 | 2024-10-18 03:51:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd19a7ef-dc62-3f86-a649-8edc365b669c | -3.36004 | -50.30072 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 36a686b0-52c2-3a94-b77b-dea8b244998d | -3.35903 | -50.3066 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 230e2c61-190a-3b02-a260-9cbcb78e3d09 | -3.35237 | -50.30547 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 73ae128b-a452-3412-83af-7367aba027c3 | -3.3445 | -45.3351 | 2024-10-18 03:51:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4f9783a-7610-34f5-ae6a-1a2d5d86aaa8 | -3.30534 | -47.02681 | 2024-10-18 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76f68931-b38c-3d91-b0a9-d8665c42d115 | -3.28161 | -47.12741 | 2024-10-18 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d690852-c092-3a70-856c-3b217cfeb7a4 | -3.28102 | -47.13099 | 2024-10-18 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d80974c-6c9e-378c-93ce-af4b6714bbfe | -3.27563 | -50.66998 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 71a0adb6-4208-3dbc-a6b4-0d7023260e55 | -3.27094 | -49.09206 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 402bae99-2624-376a-8d4e-67e054bbf737 | -3.27003 | -49.09023 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f48b96d-dfd0-3bca-b5a3-fff52c2c01e5 | -3.26919 | -49.09502 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d898ab6c-9984-3a04-98a3-4239878ba81d | -3.26881 | -50.66888 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README26.md)
