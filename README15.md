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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f38bbf35-773a-3d8c-91b7-8e5514c6e3d2 | -16.607901 | -57.273102 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58410574-cb85-3d50-822e-b70d9f65975f | -16.6105 | -57.2869 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| feb42dad-37b5-3cc5-a7b9-025a9013a77e | -16.5931 | -57.247601 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0ceda941-0546-3fbc-84f5-384065c6269d | -16.5956 | -57.261299 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e489a52-ef23-3077-9ae7-52e3432a7849 | -16.5982 | -57.275002 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74ab3b86-7a42-35af-9015-1c80026f4be0 | -14.7879 | -48.748001 | 2024-10-01 00:50:55 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 33466d40-dc8f-3d72-a0c2-492f53bc2f90 | -14.7683 | -48.7528 | 2024-10-01 00:50:55 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fe0e9fbd-1837-3d46-b172-4c81d012c61e | -14.7701 | -48.760502 | 2024-10-01 00:50:55 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4da9f52f-624c-3716-9a6b-c1c5656e7714 | -14.7719 | -48.7682 | 2024-10-01 00:50:55 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c47f4f86-97f4-3e6f-ae69-4f6e227b6b61 | -14.7604 | -48.762901 | 2024-10-01 00:50:55 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09b87c15-6dbd-376c-8edd-d722453a859b | -14.7622 | -48.770599 | 2024-10-01 00:50:55 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9b2cb213-a305-39f7-847b-79a4357a09eb | -14.7488 | -48.757599 | 2024-10-01 00:50:55 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e2e81665-5f7b-35f1-87f1-fae90124a0db | -14.7506 | -48.765301 | 2024-10-01 00:50:55 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1a716ad4-e446-357a-81e6-4c6f94764215 | -14.7524 | -48.772999 | 2024-10-01 00:50:55 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 968e150f-14b6-3637-93b3-65bace844e06 | -16.5858 | -57.263199 | 2024-10-01 00:50:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5573463-1336-38b7-8b4b-ff493c6e8343 | -16.5884 | -57.276901 | 2024-10-01 00:50:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89b69070-ba85-3440-953e-33564603a0ce | -14.1806 | -46.445099 | 2024-10-01 00:50:56 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd883ef0-edae-3caa-abca-6d4a76f00590 | -14.1709 | -46.447601 | 2024-10-01 00:50:56 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ca339897-7863-330b-9f28-8debe653a028 | -14.1587 | -46.440102 | 2024-10-01 00:50:56 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 04eca68c-4072-3cff-ac83-e01610f89850 | -14.1611 | -46.4501 | 2024-10-01 00:50:56 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a0acb438-7a41-3cbb-bfe2-9173d11ec5bc | -14.7319 | -48.729099 | 2024-10-01 00:50:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 905bfa53-55a9-3d26-b035-8e2231970838 | -14.7336 | -48.736801 | 2024-10-01 00:50:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ced3829f-e147-306b-bdb6-0756bb0f1f48 | -14.7354 | -48.744499 | 2024-10-01 00:50:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 23321b3f-8fc0-3440-a393-307c06aa7672 | -14.7372 | -48.752201 | 2024-10-01 00:50:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 14a87f2c-e662-33c2-bdc6-d2da08487cb9 | -14.739 | -48.759998 | 2024-10-01 00:50:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93817035-85d5-38bf-9fda-034c3d0f4227 | -14.7238 | -48.739201 | 2024-10-01 00:50:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b61fc077-3e46-3a8e-a09b-f365d50715eb | -14.7256 | -48.746899 | 2024-10-01 00:50:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f0b7a77-b019-3225-a7f9-985db1b6934d | -14.7274 | -48.754601 | 2024-10-01 00:50:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a5177561-668b-3879-a250-d8b0b1f51adf | -14.7141 | -48.741501 | 2024-10-01 00:50:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 26da1bb2-e12d-358e-85c9-1aead9f1c8d3 | -14.7159 | -48.749199 | 2024-10-01 00:50:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 52436447-7009-39ce-b471-b164b06156c3 | -16.522699 | -57.304199 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b9cf697-28da-38db-9043-7dc60db21b87 | -16.525299 | -57.318001 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 66236e88-d12f-3795-acc4-03a0df4920b4 | -16.512899 | -57.306198 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c798fe1-4e35-3b2d-a60e-1c18245c1f66 | -16.515499 | -57.32 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c81c2ff-9af1-34c1-9455-c16f9f962f94 | -16.500601 | -57.294399 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 804420eb-ca01-3a45-abbf-d86e03aa063f | -16.503201 | -57.308102 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a220d1e2-29dd-326a-afa4-c569df4703be | -16.5058 | -57.321899 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45ab9708-d26b-3372-a6c5-905e6a3a4a55 | -16.488199 | -57.2826 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 99429b25-9431-3fdc-9158-216bb3a5f5df | -16.490801 | -57.296398 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6739da70-da44-3a08-a7cb-9e488b56cf3c | -16.493401 | -57.310101 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c47713b6-f29a-3d0f-bf5e-7e1e3fd1ff8d | -16.496 | -57.323898 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ee8a9ede-1ec8-345e-84f9-c0594c9f6b6f | -16.4986 | -57.3377 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46e546d7-4ae4-3cad-97f8-8d0aeaf41cc3 | -16.4811 | -57.298302 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5348eb07-f738-3966-acff-cf6cdb6ab143 | -16.4837 | -57.312 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 534cf7a5-fc6e-3f82-8071-955fe61a3adb | -16.4863 | -57.325802 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a15b86a-1855-3fe0-941a-574fba70aace | -16.488899 | -57.3396 | 2024-10-01 00:50:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed92c4f2-0b90-365e-b911-8f1f56e3cfdf | -16.4713 | -57.300201 | 2024-10-01 00:50:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| df12e235-ef4a-37cc-a640-f6536ebbae85 | -16.4739 | -57.3139 | 2024-10-01 00:50:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a214291f-1afd-3e29-803e-58c3a67e4eec | -16.4765 | -57.327702 | 2024-10-01 00:50:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0ebabf23-4c88-34a4-a0fa-64a6c4412b25 | -16.479099 | -57.341499 | 2024-10-01 00:50:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6570545-0465-3f25-b7f8-54713d6bf88f | -16.4615 | -57.302101 | 2024-10-01 00:50:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| babb7701-2ea9-3ffb-aae5-ed5a13d2b39e | -16.4641 | -57.315899 | 2024-10-01 00:50:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9fd4cadd-caab-3c65-9758-8a0e3bf20e02 | -16.4667 | -57.3297 | 2024-10-01 00:50:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38a5bf40-1442-3ad1-ad84-3e483c39b15d | -16.451799 | -57.304001 | 2024-10-01 00:50:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b4ec4c2f-b2b4-36b4-a81a-fe6b0566f967 | -16.457701 | -57.389 | 2024-10-01 00:50:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b126d8f9-b82d-38d4-a29e-ac3d17250da8 | -15.6891 | -53.9035 | 2024-10-01 00:50:58 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| efc2a3a9-61e7-3f67-92a1-a6ba5864c386 | -15.4847 | -53.362701 | 2024-10-01 00:51:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ef87e58-16ce-3d08-ba54-f95c5c107244 | -15.4864 | -53.370701 | 2024-10-01 00:51:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbe9fc12-43da-3d00-b066-3ca688b02707 | -15.2506 | -53.762699 | 2024-10-01 00:51:05 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad8336a0-a1e2-3351-8551-44adada8a07d | -15.2523 | -53.771 | 2024-10-01 00:51:05 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bca61b7c-07ee-3f90-aeed-5af5f91fe34a | -15.2391 | -53.756599 | 2024-10-01 00:51:05 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 251dc7f2-165a-32ea-8acf-92a5a2009058 | -15.2408 | -53.7649 | 2024-10-01 00:51:05 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8fcaa856-78a5-33fc-aef5-2f18eaa67b1d | -15.2425 | -53.773102 | 2024-10-01 00:51:05 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5591342a-4b42-35ad-82d7-5abf8a9762f6 | -15.9055 | -57.148102 | 2024-10-01 00:51:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 04f83c02-6346-319d-afd9-d5f4f68caa4a | -15.9081 | -57.161301 | 2024-10-01 00:51:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b70e28a-63b9-3964-96f2-f427d73bcebd | -13.7362 | -48.135101 | 2024-10-01 00:51:09 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3fe93545-8b4d-322e-adf8-62d769be828b | -13.7381 | -48.143398 | 2024-10-01 00:51:09 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a609e5a7-cbfb-344a-aed2-9f4ba8918540 | -13.3108 | -46.739399 | 2024-10-01 00:51:11 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| facfd6a3-527b-390d-ba08-1258622d02ee | -13.1583 | -46.323101 | 2024-10-01 00:51:12 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a68e51a9-7db5-3da8-9d5a-df3d375b93d9 | -13.1609 | -46.333698 | 2024-10-01 00:51:12 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 76b4e5b1-d94a-374b-922f-7c8abc6e3685 | -13.1185 | -46.756199 | 2024-10-01 00:51:14 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9543b930-2ab6-3df7-88ed-8826f36f6c28 | -13.7214 | -49.4058 | 2024-10-01 00:51:14 | METOP-B | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 690b04ae-df01-3cc0-a953-b5b1e624e3b7 | -13.7231 | -49.4133 | 2024-10-01 00:51:14 | METOP-B | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9f6161d1-bed6-3680-8c4a-8a0fe5df4918 | -13.4977 | -48.572498 | 2024-10-01 00:51:15 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d435fb66-20be-3eea-92bf-a9f780980e40 | -13.4428 | -48.602798 | 2024-10-01 00:51:16 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fcf6e4ba-96ec-3502-b0bf-9f2a06ca790b | -13.4446 | -48.610699 | 2024-10-01 00:51:16 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 49e2bacf-cbc3-353c-8a64-1164fccd30ab | -13.4465 | -48.618698 | 2024-10-01 00:51:16 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8f302949-2c7e-3c1b-a0b1-1acb8ab0baff | -13.9262 | -50.858601 | 2024-10-01 00:51:16 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f72c5f86-8d81-3589-aadf-2b8dec4080b3 | -13.9278 | -50.865601 | 2024-10-01 00:51:16 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d8a32a7-6210-3dc8-9a36-291958dc7a95 | -13.2229 | -48.545898 | 2024-10-01 00:51:19 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 560a56da-2918-314f-b9a5-5b125313ff4e | -13.2113 | -48.540199 | 2024-10-01 00:51:19 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 90ca59f4-0cff-3206-b3b3-2a90558d5674 | -13.2132 | -48.548302 | 2024-10-01 00:51:19 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df5ec1ac-6a18-3bb4-b0cf-b6253508d42f | -13.6541 | -50.334 | 2024-10-01 00:51:19 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d7ba5592-dca0-3931-96e2-9cad4419badb | -13.6557 | -50.341099 | 2024-10-01 00:51:19 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aeaab9ae-de5b-3fcc-aa4c-48c47c445756 | -13.6411 | -50.322102 | 2024-10-01 00:51:19 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| beac4619-b122-33a9-b879-74dd9811e091 | -13.6427 | -50.329201 | 2024-10-01 00:51:19 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fbbdeb36-28b9-3ab4-9184-80887955c2f4 | -13.6443 | -50.3363 | 2024-10-01 00:51:19 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e0ba994-0002-3ce1-8ae9-1eb38a09089f | -13.6459 | -50.343399 | 2024-10-01 00:51:19 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a4f90966-7678-30a9-b930-6f80e4b48816 | -13.6475 | -50.350601 | 2024-10-01 00:51:19 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e8bcbc2b-8f16-33da-af83-35953acaddc2 | -13.6296 | -50.3172 | 2024-10-01 00:51:19 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c09764d2-16cd-334f-9317-2c3a71bd3b9e | -13.6313 | -50.324402 | 2024-10-01 00:51:19 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f0d5b99e-eb74-3584-b27c-c7243c306f9f | -13.2151 | -48.556301 | 2024-10-01 00:51:19 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 939d0e5b-42c5-3a25-b674-f5ce8e95331e | -13.217 | -48.5644 | 2024-10-01 00:51:19 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3dfd83e9-3077-3f9d-9167-670875ba12db | -13.2188 | -48.572399 | 2024-10-01 00:51:19 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0aed5c2a-ba9b-390b-ad1d-fcfd0f1a97f2 | -13.2072 | -48.566799 | 2024-10-01 00:51:20 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae1272f3-9999-3a59-98e7-46ba2ca86667 | -13.1129 | -48.208401 | 2024-10-01 00:51:20 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42f1cdc4-872c-3283-9975-978c16dc169e | -13.1898 | -48.5368 | 2024-10-01 00:51:20 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c15b537-15a9-3491-8426-2d115bb93729 | -13.1917 | -48.544899 | 2024-10-01 00:51:20 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6687d699-2156-3e2e-8dd7-cedb0b3b2710 | -13.7089 | -50.946098 | 2024-10-01 00:51:20 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be2447c4-f3ef-3059-bfe5-4d14787f9fc9 | -13.7104 | -50.953201 | 2024-10-01 00:51:20 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
