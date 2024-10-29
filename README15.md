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
| ce9a48e1-9f6e-3f64-a5e4-27886783169f | -3.1086 | -54.282799 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f0103da-ddf1-3f80-b612-bf7b5703bc0f | -3.0694 | -54.157398 | 2024-10-29 01:13:24 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0b65ef1-f22e-3e70-8501-d54d1c6f5d01 | -3.0966 | -54.275398 | 2024-10-29 01:13:24 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec923504-f533-3ed4-94cf-3086239112de | -2.8643 | -53.315102 | 2024-10-29 01:13:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acc2b2ac-59e2-3337-9f07-430e621278c9 | -2.8669 | -53.326302 | 2024-10-29 01:13:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed8389d4-82c0-3c41-9005-67105d838519 | -2.8695 | -53.337601 | 2024-10-29 01:13:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b00f9f03-323f-3136-8267-9efe09838c49 | -2.8721 | -53.348801 | 2024-10-29 01:13:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9135fa39-aaa4-38d2-a057-ce4c6cd98eac | -2.8546 | -53.317402 | 2024-10-29 01:13:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdc46ff4-12f7-3980-b91e-e427a32b3016 | -2.8572 | -53.328602 | 2024-10-29 01:13:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d5a6b06-c226-3a97-b373-727e01611d84 | -2.8598 | -53.339901 | 2024-10-29 01:13:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd6c2db2-132a-37e6-9262-e2c30220f8ca | -2.8624 | -53.351101 | 2024-10-29 01:13:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38d9c798-5516-3b5c-ab96-622222c93c15 | -2.8474 | -53.330799 | 2024-10-29 01:13:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a757a55-7848-3e2d-b8f3-50d6f6bb1729 | -2.9844 | -54.503201 | 2024-10-29 01:13:27 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a805b8-b60c-3dea-a70c-6afbc830f021 | -2.9866 | -54.512699 | 2024-10-29 01:13:27 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ad3ae7a-f288-35e7-9a5d-3b4a01d1d1cf | -2.9393 | -54.352001 | 2024-10-29 01:13:27 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d36cf37-38c9-3787-882a-986cfd7c7010 | -2.9725 | -54.495899 | 2024-10-29 01:13:27 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b00d21c-d072-36be-8803-3d047514ba5d | -2.9747 | -54.505402 | 2024-10-29 01:13:27 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb7d6318-3100-3b7a-82c2-e8c006ce7f44 | -2.9769 | -54.5149 | 2024-10-29 01:13:27 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7753e34f-902b-3717-975e-520cbe3a2858 | -2.8324 | -54.200901 | 2024-10-29 01:13:28 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29b39ade-f72b-3682-8f40-012a09a8d89f | -2.8347 | -54.2108 | 2024-10-29 01:13:28 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5d4354c-39b1-3225-88be-46ddf0d05c67 | -3.5654 | -57.677502 | 2024-10-29 01:13:29 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b96155cb-7b99-3ecb-88c9-f7895b2f4de2 | -2.7884 | -54.725201 | 2024-10-29 01:13:31 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83c1ad05-3dc4-3de1-a1f3-65114e65312f | -2.7766 | -54.718102 | 2024-10-29 01:13:31 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33b3508d-9650-33a7-b5fc-1da351a4ef17 | -2.7787 | -54.727402 | 2024-10-29 01:13:31 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c0e1f74-7e6b-3458-ba8e-9e9b7e1ec526 | -2.5713 | -54.0051 | 2024-10-29 01:13:32 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53cce837-6069-37d8-940c-d94eed64b2d9 | -2.5591 | -53.997002 | 2024-10-29 01:13:32 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab6530c-e3b1-3526-b693-3a7da56985ac | -2.5615 | -54.007301 | 2024-10-29 01:13:32 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48b40d5c-0c27-3583-acd4-6f59f6963972 | -3.7542 | -59.4282 | 2024-10-29 01:13:33 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44ebef25-62d9-3ad8-a1b5-1baa6d5087a2 | -3.562 | -58.6656 | 2024-10-29 01:13:33 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 502e193d-a7f3-3162-8d96-8a636fa549cc | -3.5636 | -58.672401 | 2024-10-29 01:13:33 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b698dbe-8c0b-3668-a0d4-3d438ed4f8b9 | -3.5522 | -58.667801 | 2024-10-29 01:13:33 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 129026cd-3657-3cc3-8b78-eb6a6b5a30b8 | -3.5538 | -58.674599 | 2024-10-29 01:13:33 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3539b37a-2c76-38e5-87f8-ff823aa5e051 | -2.6857 | -54.950298 | 2024-10-29 01:13:33 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bac85a3-9f13-3edb-84f2-658534ed8d83 | -2.6878 | -54.959301 | 2024-10-29 01:13:33 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77a2062f-541f-3280-92f4-bcfecd39f088 | -2.2145 | -53.662102 | 2024-10-29 01:13:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac6468e6-d641-3d83-85e3-b6e819999b7e | -2.2073 | -53.675301 | 2024-10-29 01:13:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60ae8751-a785-3291-aed2-bbb412da310d | -3.4434 | -59.236801 | 2024-10-29 01:13:37 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2da88fe8-1435-3cfe-9c6f-276d51c920b4 | -3.4449 | -59.243698 | 2024-10-29 01:13:37 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d761c4ae-be99-377f-a8a1-e67419566325 | -3.5613 | -59.762402 | 2024-10-29 01:13:37 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83b37a62-c83d-384e-90f3-dfc64701260e | -2.3898 | -54.648102 | 2024-10-29 01:13:37 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f786776-e379-3d03-acfd-2119ec7f1849 | -2.392 | -54.657501 | 2024-10-29 01:13:37 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf634d22-c842-3fc1-960c-42b047f27fd4 | -2.1692 | -54.627998 | 2024-10-29 01:13:41 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b423a687-47c6-3c2a-a5a6-51959b193f27 | -2.8392 | -57.656399 | 2024-10-29 01:13:41 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5c6c25e-61e8-3149-acef-3e568fafbc1f | -2.1255 | -54.796902 | 2024-10-29 01:13:42 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b35c4a52-9f90-3b2d-81de-2865ea939e7f | -2.1276 | -54.806301 | 2024-10-29 01:13:42 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b515533-b90f-3232-8f81-ea206d788dcf | -2.4774 | -57.515099 | 2024-10-29 01:13:46 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96c10c42-b42d-3a36-8563-d7b19eb79f41 | -1.7523 | -54.4249 | 2024-10-29 01:13:47 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9b10cfd-4bf3-302b-a28e-126c90c5a2de | -1.7545 | -54.434799 | 2024-10-29 01:13:47 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 181fa0ad-ebf4-31a4-a0e9-c7f05276f87d | -1.7568 | -54.444801 | 2024-10-29 01:13:47 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c452b297-5b09-3245-8191-f038d941ce1e | -2.3503 | -57.1367 | 2024-10-29 01:13:47 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 015885db-f0ec-3bcc-9b60-439ebeb1aa47 | -2.3519 | -57.144001 | 2024-10-29 01:13:47 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7aa86ba0-e321-3c58-bc49-494065e50f25 | -2.5678 | -58.096298 | 2024-10-29 01:13:47 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06306503-19d3-3031-ba36-edf6a4ebc0f8 | -2.5694 | -58.103199 | 2024-10-29 01:13:47 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 394259e3-c600-3e63-8406-eecde480a684 | -2.0023 | -55.698399 | 2024-10-29 01:13:47 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db7d9fb9-932f-336a-ba73-11c2a34d5e06 | -2.0042 | -55.706799 | 2024-10-29 01:13:47 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89ab93fb-4a03-3c78-98e1-d01b00e0436e | -2.3307 | -57.141102 | 2024-10-29 01:13:47 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd2d0f8-addd-304b-8726-8611a901b1a6 | -1.7192 | -54.505299 | 2024-10-29 01:13:47 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a453f1c6-202f-393a-af4f-1300019b58f7 | -1.7215 | -54.515099 | 2024-10-29 01:13:47 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c967491b-4496-3af9-90b3-33e009046126 | -1.7238 | -54.525002 | 2024-10-29 01:13:47 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e03237d-e1ba-3847-af5f-e6e48f20c28e | -1.7117 | -54.5173 | 2024-10-29 01:13:48 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c201aa02-7d2b-3a82-886a-a44ba70c700c | -1.714 | -54.527199 | 2024-10-29 01:13:48 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18ceb018-073e-39b4-865f-51df3eba72a3 | -2.0448 | -56.110802 | 2024-10-29 01:13:48 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a387d09-61cc-341b-8948-3f083a6cbab2 | -2.035 | -56.112999 | 2024-10-29 01:13:48 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da30a957-e2a3-3d7c-bd15-4921f3ffcc80 | -1.9683 | -56.0009 | 2024-10-29 01:13:49 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9064c36c-9006-3d4e-a9b7-3d27357731b1 | -1.7682 | -55.2141 | 2024-10-29 01:13:49 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7466787-b5a7-3db3-9d6c-b83b36a6d257 | -1.7584 | -55.216301 | 2024-10-29 01:13:49 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffc4267c-d56e-3525-a49c-bf8923998f89 | -1.453 | -54.061001 | 2024-10-29 01:13:50 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09cd252d-9532-3c02-86ca-3320b39d6760 | -1.6137 | -54.763401 | 2024-10-29 01:13:50 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 629adbe0-a35e-3581-96f5-babbc7cf5fdb | -1.8066 | -55.6982 | 2024-10-29 01:13:50 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e3a6743-6866-3d3c-9ef6-92e61336fe90 | -1.7696 | -55.6264 | 2024-10-29 01:13:51 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aede903-82af-3280-ad2e-fea48989670c | -1.7715 | -55.634899 | 2024-10-29 01:13:51 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb78ad9b-9f8e-3d1a-8954-9777c94ec705 | -1.4353 | -54.208199 | 2024-10-29 01:13:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5639e2c1-7b8c-3c0b-99c2-a16d087940bb | -1.4376 | -54.218601 | 2024-10-29 01:13:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28c649ca-bb59-323d-aab1-9b976fb35a74 | -1.4255 | -54.2104 | 2024-10-29 01:13:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 402c0e47-8160-3b16-b75a-cbd2f6608246 | -1.4278 | -54.220798 | 2024-10-29 01:13:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd0c338e-852d-3b31-aa77-ebf929e6fe7d | -1.3498 | -54.5989 | 2024-10-29 01:13:54 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c786c4e7-ab1a-34f2-902d-737a3aede739 | -1.349 | -54.640301 | 2024-10-29 01:13:54 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 557932d9-9bc4-3176-be0c-4c07938e99fd | -1.3392 | -54.642502 | 2024-10-29 01:13:54 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59fc4d81-0590-347e-9eed-aa36588b2766 | -1.0812 | -53.648899 | 2024-10-29 01:13:55 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e77f02e-a015-3643-bce7-b828c08193f9 | -1.0688 | -53.639702 | 2024-10-29 01:13:55 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c077370-0597-3001-8579-43e1c7f7ef58 | -1.0714 | -53.6511 | 2024-10-29 01:13:55 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 536ac4d0-2494-3466-9ca9-1d6c08cefc5b | -1.1792 | -54.167099 | 2024-10-29 01:13:55 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20411c8b-05ce-31e2-8824-eae2a9a8bab5 | -1.3492 | -55.1371 | 2024-10-29 01:13:56 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 532fccc5-6811-3d66-af23-71c9dd37a01b | -1.3513 | -55.146198 | 2024-10-29 01:13:56 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afd2cd13-5114-323e-aff1-1287c7698886 | -1.4025 | -55.371201 | 2024-10-29 01:13:56 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 927a1b44-950e-3cfd-83d5-b8e3e2fa8a64 | -0.9887 | -53.6936 | 2024-10-29 01:13:56 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82f24d56-0209-3c7f-ae7d-6911f37c2809 | -0.9789 | -53.695801 | 2024-10-29 01:13:56 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 814cd516-8f38-302c-9009-86c925c19c72 | -0.9815 | -53.7071 | 2024-10-29 01:13:56 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79d2e1ad-0456-31d1-a0d2-7fca6ed01a2f | -1.3772 | -55.8475 | 2024-10-29 01:13:58 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8871637-d3ec-3737-8319-1fc7b88ed42d | -1.3791 | -55.855801 | 2024-10-29 01:13:58 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac51027-b05e-3992-8f1f-7e2d93e80491 | -1.3054 | -55.7127 | 2024-10-29 01:13:59 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae1f2d0-c4c5-3c07-ac35-0eaef0d09b51 | -1.2956 | -55.714802 | 2024-10-29 01:13:59 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86085136-c45e-3f51-a37e-ee950cf5fb56 | -1.2975 | -55.723301 | 2024-10-29 01:13:59 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e897389-0fbe-310d-9c5b-267f7bd5f579 | -1.2654 | -55.898899 | 2024-10-29 01:14:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56853e17-d56c-3428-9942-8c217fae56aa | -1.2673 | -55.9072 | 2024-10-29 01:14:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43c0ca3b-0d36-39ff-888c-2b4b23993d4a | -1.2126 | -55.893101 | 2024-10-29 01:14:01 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a3407f8-7c00-396c-8ccc-65a653195550 | -1.7251 | -60.116402 | 2024-10-29 01:14:08 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e26204c-1e51-3ad2-9d5e-a419d64a2e69 | -1.7266 | -60.123402 | 2024-10-29 01:14:08 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0d93b44-c7d6-3611-8e14-99bcfa319e12 | -1.4413 | -60.2742 | 2024-10-29 01:14:13 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 074641b2-eb69-3cda-868d-8c9f1fa4a5d4 | -1.4299 | -60.269402 | 2024-10-29 01:14:13 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
