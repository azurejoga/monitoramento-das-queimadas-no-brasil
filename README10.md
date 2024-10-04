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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70e74a1b-b14e-3841-907e-8cf89d09632c | -16.0786 | -50.264198 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a09aba2e-407d-3800-a52d-cc5558b6ccd9 | -16.0807 | -50.2747 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 50a6514e-ec16-374d-ae30-04062992bd1f | -16.082899 | -50.285198 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 527b6d32-9df5-3f0b-971c-1a812b99fe57 | -16.070999 | -50.276699 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 476602d5-c086-31a9-911c-c7613f6133c7 | -16.073099 | -50.287201 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d8372df7-37df-380e-9d31-44ffa04e5bad | -16.075199 | -50.297699 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4005e640-a57e-3b26-84dc-b52a9f69591e | -16.077299 | -50.3083 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 919f6d50-8fc9-30bb-8f80-0fa9ca22ca3e | -16.065399 | -50.299801 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af39fe58-5552-3fcf-8f92-7fa2e65b1961 | -16.067499 | -50.310299 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8078cc5d-9689-3e6e-b276-68999622cfad | -16.1127 | -50.433899 | 2024-10-04 00:42:04 | METOP-C | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a314c41c-975a-3413-b2fc-b4a32c5411c4 | -16.114901 | -50.444599 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4720f118-6bb9-3446-828e-23dc5bfbc009 | -16.117001 | -50.455399 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 789a4b1a-54b0-3579-89f7-901e641ceb66 | -16.0856 | -50.450699 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0ceb24e5-2d00-32d3-a43e-22d2d4b48ae6 | -16.0877 | -50.461498 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2f99f089-ee73-3658-90a3-67b638c6daa8 | -14.9041 | -45.121498 | 2024-10-04 00:42:05 | METOP-C | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b873d7b6-a057-3e0c-abdb-96525e250e27 | -14.9057 | -45.128601 | 2024-10-04 00:42:05 | METOP-C | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0993265a-cc53-3065-96a5-e03d79098524 | -15.4017 | -47.4128 | 2024-10-04 00:42:05 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| adfbf468-fe90-3491-b1b1-8d0388b3fed3 | -15.4033 | -47.4203 | 2024-10-04 00:42:05 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db7ca771-4a6a-3a6c-8cbd-bd554a0b1e10 | -15.3935 | -47.422501 | 2024-10-04 00:42:05 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8b1c31c8-ea5e-3328-a221-9cf4f81b93d0 | -15.407 | -47.6758 | 2024-10-04 00:42:06 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7277cf97-8837-3fc7-b77b-886b365614b2 | -15.4087 | -47.683498 | 2024-10-04 00:42:06 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9106c6ea-1224-39d4-b3a1-c14e774c371c | -17.0989 | -56.765301 | 2024-10-04 00:42:07 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa673de7-2bd5-3e9b-a791-801fc52394a6 | -17.084299 | -56.737701 | 2024-10-04 00:42:07 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aa48efe3-604b-305d-8f89-33d36c8475fe | -17.089199 | -56.766899 | 2024-10-04 00:42:07 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9f9591da-093a-3829-8464-18e3291e6090 | -16.9179 | -55.821701 | 2024-10-04 00:42:07 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b618c123-0593-3478-9337-8009641c6809 | -17.079599 | -56.7686 | 2024-10-04 00:42:07 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5c06d7d0-b485-3c2b-af3a-85db0d0921c6 | -16.9039 | -55.798401 | 2024-10-04 00:42:07 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1eff73b-5ecd-3072-8b81-0457b94db84b | -16.908199 | -55.823399 | 2024-10-04 00:42:07 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 23288b99-9a69-3d2c-a663-0f4a3cc12d1d | -15.5905 | -48.782101 | 2024-10-04 00:42:07 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3d5e4d02-d037-3a8d-bd62-ee5081f84888 | -15.5923 | -48.790699 | 2024-10-04 00:42:07 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| da683b92-294e-33ec-ac55-0f3d60e2724f | -17.157301 | -57.3535 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00c3865c-06ea-3928-bde2-d2a76db619df | -17.1626 | -57.385601 | 2024-10-04 00:42:08 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3298bd50-7d9a-309d-90ef-20727e9b9307 | -17.0506 | -56.773602 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1460af68-7a89-36fe-ac2c-a33333b00b05 | -17.1476 | -57.355099 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a0dda3a-8557-3abc-90d0-c7056263cc15 | -17.153 | -57.387299 | 2024-10-04 00:42:08 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f555cf5-f1b2-30bb-87c0-aa6ada42a983 | -17.040899 | -56.775299 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b5b6a7d1-f7df-3c53-9992-0a60450e33d9 | -17.138 | -57.356701 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b3ece89d-f174-3b1a-9e1d-f163d3f05bb2 | -17.143299 | -57.388901 | 2024-10-04 00:42:08 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b4a31ccf-f1b7-35fc-8a30-163bcb57b82b | -17.0264 | -56.747898 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c645ff0f-a60d-3e83-9d74-5336b69c80b3 | -17.0313 | -56.777 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| de324195-38a3-35bc-a9bc-7812c5c3f65e | -17.128401 | -57.358398 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c3f9a281-cce4-3f3d-b1b9-2943e64ad170 | -17.016701 | -56.749599 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7176ac55-f51d-33d9-9a92-cc6eb774e710 | -17.021601 | -56.778702 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9cbdaa0a-ddc9-3087-802c-51eea7a24605 | -17.002199 | -56.722198 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4eaacca-5247-372b-9689-f28a75c7b081 | -17.007099 | -56.751301 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 923a0e23-c6fa-36c6-aa2b-c80bb4c796aa | -17.011999 | -56.780399 | 2024-10-04 00:42:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 421b25bd-592d-3acb-9da1-7f2b531fe8ea | -15.2663 | -47.498901 | 2024-10-04 00:42:08 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bcf610dd-6eae-3089-a91d-7fe5b73504e1 | -15.2679 | -47.506401 | 2024-10-04 00:42:08 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2f5b2130-b4ea-3151-b821-1d74ae0e4098 | -15.2566 | -47.501099 | 2024-10-04 00:42:08 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b4bcec90-97ca-3763-b722-4b9629343a67 | -15.2435 | -47.488098 | 2024-10-04 00:42:08 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9b907a73-1e28-36df-a930-75d775c30557 | -15.2451 | -47.495701 | 2024-10-04 00:42:08 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 666adcc7-f990-3e8c-b5d1-1401d05b7439 | -15.2468 | -47.5033 | 2024-10-04 00:42:08 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6dbea44f-1a4b-3cd3-a081-b37e53c415bc | -15.2353 | -47.497898 | 2024-10-04 00:42:08 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 115d5ec4-301a-3996-9c41-7d83dae34e5a | -15.2255 | -47.5 | 2024-10-04 00:42:08 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff6e1916-49c5-3e03-9613-f3757e1560f0 | -15.7501 | -49.9506 | 2024-10-04 00:42:08 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bded6e19-bda2-3afa-ad72-9d7e773410c5 | -15.7521 | -49.960499 | 2024-10-04 00:42:08 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 35b3e159-c317-3c3c-91d0-8c6ec4443758 | -15.7541 | -49.970501 | 2024-10-04 00:42:08 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| da9351db-b6d5-3595-beb8-7064efd755cd | -15.7423 | -49.962601 | 2024-10-04 00:42:08 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 26b66b1a-1f07-3036-b8a0-39c924170511 | -15.7443 | -49.972599 | 2024-10-04 00:42:08 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 38092579-5dde-32a1-ae05-a079f993d609 | -16.9925 | -56.7239 | 2024-10-04 00:42:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8870ad6-465f-3fa3-b1e1-33a60ffd3259 | -16.9974 | -56.752899 | 2024-10-04 00:42:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6fcffff5-00f1-3aa9-9452-98d54b8b9465 | -17.002399 | -56.782101 | 2024-10-04 00:42:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1a56cca7-76a1-3105-b955-fddbf260d23a | -16.982901 | -56.725601 | 2024-10-04 00:42:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5de5f173-4b85-387a-9ab6-c8ed2eb7ecc3 | -16.987801 | -56.754601 | 2024-10-04 00:42:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c177fe4d-d224-3b46-b368-725f82993fe6 | -16.9928 | -56.783798 | 2024-10-04 00:42:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a35d7e60-251b-38fd-b9cf-4b40a306b1ca | -16.973301 | -56.7272 | 2024-10-04 00:42:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1031ba99-e69a-339c-980e-c19dcf4c17fc | -16.978201 | -56.756199 | 2024-10-04 00:42:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3fc9c6fc-fddd-3fc9-adef-e6936388851a | -15.2157 | -47.502201 | 2024-10-04 00:42:09 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d573c02e-4f23-39ec-a072-edcca8eabdbc | -15.2174 | -47.5098 | 2024-10-04 00:42:09 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b23c296d-df8c-3e9e-ae88-c83dd679e75e | -15.2059 | -47.504501 | 2024-10-04 00:42:09 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 57ee73fe-9903-3642-9a60-d1ddf38d0387 | -15.2076 | -47.5121 | 2024-10-04 00:42:09 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f9b4785d-5fbf-3b44-81f2-1f9036d7a898 | -15.1961 | -47.506699 | 2024-10-04 00:42:09 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fe16f9a9-76af-30d9-bbc0-ea7f5dda4c71 | -15.1978 | -47.514301 | 2024-10-04 00:42:09 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a77fd076-abe9-31f4-a7a8-39e1523f98ef | -15.1863 | -47.5089 | 2024-10-04 00:42:09 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 13d5d481-32ed-3e31-963e-6abf864d7e40 | -15.188 | -47.516499 | 2024-10-04 00:42:09 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9a4909b5-4a1c-3341-ac38-b95cb1f09f95 | -15.1896 | -47.524101 | 2024-10-04 00:42:09 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6de645bb-efb3-389b-b245-3690755ceb37 | -13.814 | -42.149101 | 2024-10-04 00:42:11 | METOP-C | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b021c316-0cf5-3a17-afc5-99e784c08a3b | -15.1641 | -48.074001 | 2024-10-04 00:42:11 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae98ed6c-4c3e-34f6-9151-eb5e41379c38 | -14.1321 | -43.701099 | 2024-10-04 00:42:12 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 314a6f35-2c19-372a-bff3-c277c0076f69 | -14.1864 | -44.243198 | 2024-10-04 00:42:13 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 592e383f-fe8e-3197-8884-abaccd47ad69 | -16.780399 | -57.352501 | 2024-10-04 00:42:14 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| af56b2d3-6c54-3ca2-9397-a5c61d8d98cf | -16.7708 | -57.354099 | 2024-10-04 00:42:14 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8846a6e7-5760-3846-a27a-9ca2a745a9b0 | -16.7761 | -57.385899 | 2024-10-04 00:42:14 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b2a20d2-167f-31fa-bccf-cd2738c59408 | -16.7612 | -57.355801 | 2024-10-04 00:42:14 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c94621b2-176e-3845-8ad1-0a2bef9c7f87 | -14.1551 | -44.643501 | 2024-10-04 00:42:15 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e2023b7-638a-3b05-8506-aa527cc3bfbb | -14.1649 | -44.641201 | 2024-10-04 00:42:15 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20068c38-493c-3134-86d3-50540ad4f71d | -14.1666 | -44.648499 | 2024-10-04 00:42:15 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a0f48b6-24db-33e8-8bc7-aa1828fd17c5 | -14.1683 | -44.655701 | 2024-10-04 00:42:15 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0dc0c61f-9694-3930-9fd7-d14644304f59 | -14.1568 | -44.650799 | 2024-10-04 00:42:15 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34a4ada4-1843-3ed4-8c8f-8c7e2fef79b7 | -13.9889 | -44.016102 | 2024-10-04 00:42:16 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76c7d8a7-c81c-3780-876e-ff46eee73a17 | -13.9907 | -44.023602 | 2024-10-04 00:42:16 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d7c4d9d-b2fa-3aa2-8db1-e4096359c4a5 | -13.9924 | -44.031101 | 2024-10-04 00:42:16 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5d0bf72-e729-3020-be73-ba4d8b9d55cc | -13.9942 | -44.038601 | 2024-10-04 00:42:16 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd56bf4f-758b-30a7-9235-23a408df194f | -16.5896 | -57.1614 | 2024-10-04 00:42:17 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5730aa2d-dd0d-32dc-9a87-882584919907 | -16.5711 | -57.227798 | 2024-10-04 00:42:17 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 095887ca-fdf9-334a-bd35-c826aa4d3716 | -16.5562 | -57.1987 | 2024-10-04 00:42:17 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f751068a-1444-3b2d-bb2b-05bb775f1276 | -16.561399 | -57.2295 | 2024-10-04 00:42:17 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b919a782-b803-31ec-8306-b22ff7f51049 | -16.5466 | -57.200298 | 2024-10-04 00:42:17 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b3744be3-cd94-3d41-b9a9-ff9cf0f7dc03 | -16.5518 | -57.231098 | 2024-10-04 00:42:17 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac7d8a84-995c-3a84-8748-9bdcf999f9ca | -14.7945 | -48.0242 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README11.md)
