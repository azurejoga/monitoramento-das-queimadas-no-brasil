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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d0e4c24-a883-368d-88dd-ecb4017e0344 | -2.21243 | -50.78466 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93733f2e-8dd2-3d54-89ea-1a99f3a1fccd | -2.21182 | -50.78849 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b544e5ec-5e14-3675-8e10-1ecafb2406fe | -2.20119 | -50.593 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b54a4fc-489b-3785-a8c5-d49451297f88 | -2.19834 | -50.58871 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e86e334f-03b8-34c2-8fb2-fe32d4ec82d0 | -2.19775 | -50.59246 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0f8617e2-5703-3f40-b066-a229bc2ed6ee | -2.19716 | -50.59622 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa8df79b-762b-31b9-967c-3550536f7ddf | -2.1949 | -50.58817 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 42f94078-7d9d-39d7-9714-68536d24ac33 | -2.19431 | -50.59193 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a4eac890-ad92-353e-9d1c-f2b79e41a8ce | -2.19372 | -50.59568 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 54d9c1c5-7ac8-32f9-ab86-a60ad83a425d | -2.19087 | -50.59139 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5f8c2f9d-a8d5-37c3-afb9-75f47e74f590 | -2.19027 | -50.59515 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 59a90bb5-f19a-3e08-a63f-11b566a870c1 | -2.16133 | -51.01372 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3aadda0-1cd8-3de7-b548-58e4376bfae0 | -2.16013 | -51.01376 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b77f8558-51d2-3175-8d47-585906e4afb4 | -2.15783 | -51.01317 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71d2fb83-9cc1-3b3f-8649-cf1aaac4feb2 | -2.09066 | -50.38138 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0728ebff-1c19-39a2-b775-4c00f4ac9efe | -2.08203 | -51.39698 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e8d96e7-95d8-38e8-a964-0b69ed3ac192 | -2.08178 | -51.42192 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f029f10b-f065-3d03-8f49-d1051309a62d | -2.06918 | -50.877 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 95a473d0-b8ef-350f-8ab8-e7d4d41f7417 | -1.96421 | -50.7159 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d87c454-92ab-3288-9e12-e5b4b092ca5b | -1.87004 | -51.36178 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ca6ea4d-2846-3785-a61e-8673fe49e3b8 | -1.86491 | -51.04955 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b544d91-aacf-3adc-b8f4-c7129eb03cdb | -3.56294 | -51.5034 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 965dc9fb-bd26-36f6-8b65-369dd9098f5d | -3.43585 | -51.50453 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9b1a31b-aef1-301d-a90b-9e4e64882d3d | -3.43119 | -50.78593 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53704d8e-8de8-3a16-8737-485ba8d10ea7 | -3.41044 | -51.50478 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a851345d-12d2-399d-8872-f97fc4a693ff | -3.39884 | -51.53161 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7c05789-5c26-3583-bb1f-735fa7712b72 | -3.37207 | -51.42554 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 664ea125-9c55-39fd-a602-756d42e27f1e | -3.3451 | -50.75375 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 552eb4a0-d173-3ace-8bd6-83e0ee4b4f8d | -3.34167 | -50.75322 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec2d3b74-e540-35fe-a19f-f0497dbd1aad | -3.34108 | -50.75696 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fac7544b-6627-312a-968d-a4da4f899d18 | -3.33765 | -50.75643 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a59365c9-78a6-31d9-9742-d77964af078b | -3.33362 | -50.75962 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f138cf3-3208-3a3d-bc49-b795e22c9da5 | -3.30638 | -51.26724 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f29004ea-976a-3ae8-b0f7-49333f59a9d8 | -3.30576 | -51.27113 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd5f4aba-5cc8-34c2-9ec4-b4b9acdc0c72 | -3.29039 | -50.94171 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da277721-ad90-3ec9-b686-51d6bbb60115 | -3.27413 | -50.95469 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51e457e8-7a09-3631-a7f0-33d27db3ca89 | -3.2738 | -50.69349 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 473f3de9-fce4-308d-a7d9-27a6a7e5e371 | -3.27321 | -50.6972 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 852c1476-ff65-39aa-96de-57773f882f7b | -3.27262 | -50.70093 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 586e5043-8969-3d20-b0be-1aca52c02b93 | -3.26979 | -50.69667 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23582d03-f4a7-3154-8ffb-2f39ca88f158 | -3.26719 | -51.01991 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c54c90e-0a60-3e5c-90a6-867f5241da09 | -3.26476 | -51.57751 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4b4fc41-e155-3239-a224-e8d04fecc0bf | -3.26435 | -51.57652 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26085f7c-8f6f-325f-a591-3a3df518511f | -3.26434 | -51.01555 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 69296821-0d34-3a1a-ac6f-5c11cd69ab64 | -3.26372 | -51.01936 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c34e2fe6-d91d-3c4e-a11a-969b6b9badc7 | -3.2637 | -51.58055 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0be714c-eb2d-3251-ba89-6bdf6e2e6004 | -3.25892 | -51.56834 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5e3ceb6-7cbf-3bd5-9af4-5871ae10640e | -3.25406 | -50.64104 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 897adad4-ca68-3688-a18e-7b433db9c3e2 | -3.25348 | -50.64473 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb518df5-0c44-3a74-836c-6509412c9eaf | -3.2529 | -50.75896 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cd51306-1322-397e-9225-e29475ba9511 | -3.25065 | -50.6405 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52bd96ae-92a6-3c0f-b92c-1af1d3e040b6 | -3.25006 | -50.64419 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 080df522-6b18-3a2c-b7d8-078f09595c82 | -3.24307 | -51.55344 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81ee6c50-ea7e-3cc5-bd46-57f6a2bae65d | -3.24267 | -50.84583 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7c99e0d-acce-3586-b3aa-9f2a25d93227 | -3.24208 | -50.84959 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f0ac226-9d92-3a8b-9bd7-41027f9c1b72 | -3.23705 | -50.72594 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9b9ca57-afc2-3420-b94e-b8c96d763ca7 | -3.23646 | -50.72966 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4f763a79-8576-3d0d-875b-8c95715dc949 | -3.23587 | -50.73338 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 003ce08a-53c3-3139-9bd9-0c5075b2db09 | -3.23585 | -51.19238 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48890135-179a-33e6-b861-f523c2acf191 | -3.23362 | -50.7254 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a99152ba-0b77-3402-a32f-52a678997898 | -3.23236 | -51.1918 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8e32e25-2b91-387c-b926-8ff6bbb975be | -3.23173 | -51.19567 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c97f22e1-bfa2-3933-bbf3-9db840e29f5a | -1.29797 | -60.22607 | 2024-10-29 04:38:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94353172-0a93-3562-824a-8c53108747fe | -3.22887 | -51.19122 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10e39165-1a2f-31f4-b996-16427883f681 | -3.20569 | -51.03449 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9407d5a-2209-3e2a-b90d-e4c10612b0c2 | -3.18616 | -51.15753 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb585a6b-08f1-39b7-a30e-a7f8e8154b11 | -3.18267 | -51.15699 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0bf466d-1ffa-3650-97e0-8373a3dd4024 | -3.16346 | -50.59241 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 253dd89d-5e7a-3990-bc8e-89d35b9f7540 | -3.16005 | -50.59188 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1242e97f-b2f5-3054-adbc-1fbe05e72c34 | -3.15946 | -50.59558 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 449acafe-c617-348e-8dd2-54f0a6b4f24a | -3.15664 | -50.59134 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9dcddb0b-84ad-3d3e-a1bb-eaeea9d3d322 | -3.15605 | -50.59504 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9b98ebe-cc87-32a3-b658-df9a423922bb | -3.15354 | -50.87804 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f27d9c7e-f9ca-3160-962f-9c67de1b337e | -3.15322 | -50.59081 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 21abc421-0ad8-303d-b6ee-c9405878d5d3 | -3.15263 | -50.59451 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3fef8220-5f94-3eb4-b099-ee39c221c01f | -3.14922 | -50.59398 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01c6c2c6-59c2-3515-9067-2f566dc0ac32 | -3.07958 | -51.12112 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af1db398-e3ed-3d7d-8d82-dde966a2ea9d | -3.03487 | -51.44812 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8bce4c3b-0611-3ada-8eaa-bb18c64745cc | -3.02379 | -51.38111 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45a6e28c-2bd7-3070-99db-cc1d58220ea7 | -2.97112 | -51.43816 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42cc8ea8-1941-3fc0-931a-569c7617b6fb | -2.96757 | -51.43762 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2e777bc-80d2-317b-909c-9cb14204ee78 | -2.96693 | -51.4416 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51a0fcc5-6e81-3452-aa3a-53c90e285203 | -2.95723 | -51.00388 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 628a35c9-c197-33f9-966e-563772a894c3 | -2.95437 | -50.99953 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adbae295-efe9-3bbb-8c13-1f7030e3b208 | -2.89892 | -51.48112 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8a62737d-dd8c-3f16-b281-0d0081e95694 | -2.89828 | -51.48513 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8834927b-10c7-3dd4-b63a-e62452fdf588 | -2.54586 | -51.16839 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fefd6762-9cfb-325c-9d6e-c3975771d6a5 | -2.544 | -51.18018 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03a2dfa0-2191-3bba-aab7-dc0c5ea4b946 | -2.54234 | -51.16785 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66391aa6-a483-337b-9f04-68df65ea2bca | -2.54172 | -51.17178 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04400e5b-983f-37e0-a1ae-b2e3f4e0a2b4 | -2.5411 | -51.1757 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5661ba50-6637-3ca2-9e47-2dfecf3fb79f | -2.54048 | -51.17963 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f56612d-3da8-3292-acc7-5122acb8011b | -2.53986 | -51.18356 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d70842e-2131-37a2-873d-225baa6c70cd | -2.53759 | -51.17516 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f287bce-22ba-3010-b3a5-e1366e8982f7 | -2.53697 | -51.17909 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8863c0b0-9a81-321f-a399-d20a5690ee80 | -2.53635 | -51.183 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77bd3854-3bf9-370a-8ad4-300cec4b6e2a | -2.53573 | -51.18693 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34a9396a-8762-32c8-98f7-58b67665eb18 | -2.53511 | -51.19087 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c73ddcb2-3fb2-3971-8d91-b9c5e7c74352 | -2.53345 | -51.17854 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4386f651-2b34-32a3-b8ae-b81c415ee845 | -2.53283 | -51.18246 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README49.md)
