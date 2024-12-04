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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98c79cbd-0e4d-3e6f-b7e5-f0708c108b0d | -3.11296 | -54.61333 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6bf36ce6-5db2-3100-aff4-32582daaa734 | -2.98203 | -53.90611 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48b7eeed-b8e4-3f1d-94ac-2e2f941277bc | -1.26827 | -54.12046 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37f483c6-a359-36e7-82fd-0d73023f3f40 | -1.66157 | -52.75786 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b1c7d86-8ca7-33ea-8aa1-4487ab42083b | -1.65604 | -52.37995 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa2c2ad2-71dc-32c0-b025-7ae2b65931cd | -3.33345 | -51.20646 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cdb41e8-e550-3b82-b159-bda6cf3d1f22 | -2.85159 | -54.826 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce479140-b0df-3809-b9bf-643cef8c8f54 | -2.90326 | -51.81414 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5957a34-91d9-390a-a098-68b63ad37708 | -0.85737 | -52.70921 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 455d9d05-51ea-30dd-b5e0-833f3e51f961 | -2.80394 | -53.06278 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b29f608e-1b4d-34f8-bdaf-0060d63fbf02 | -3.11226 | -54.61786 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a12b8cd5-63f9-3201-b2bc-f326cf937b90 | -1.43706 | -55.20936 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70293e92-3348-3afe-9242-eebc1c0936fc | -4.19631 | -50.67606 | 2024-12-04 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2edf8d1a-13a5-3ed7-bfcd-e1211f97cb47 | -3.24706 | -50.41922 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63e0b65d-b4ee-3f89-86b9-57d048f735e3 | -1.72477 | -52.48547 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 078917dc-a4d5-38ad-9d4c-6365cc708670 | -3.20015 | -50.6436 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7afb1376-2075-30ea-a301-26054375f7b5 | -3.15191 | -54.48185 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8816f23-beda-33d1-9ad7-e2d5acad74de | -1.78528 | -52.75355 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4555d68-3127-34c3-bef8-98d6d065f2fe | -1.25563 | -54.53753 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 781e742e-f096-3486-ae19-40fd36a683bb | -3.12906 | -54.62978 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d4f443a-6a88-38d9-bd7b-687a2286ebe1 | -2.85915 | -54.23157 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 088f0a9e-f294-3600-8217-a74b162da9e0 | -3.33875 | -51.20945 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f54d9f25-df3f-33ac-896c-a635203abe6f | -1.07403 | -62.64181 | 2024-12-04 05:29:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e52cd13d-67aa-3175-bd84-e21757289171 | -2.54633 | -53.41174 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02c4a3fd-bc5f-3d56-87b9-d82a0d31bc1e | -1.23194 | -54.17307 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3ff58d8-f039-3c1f-b4e3-1c88128e07e0 | -2.52222 | -51.81025 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 768deb97-0faf-3fb8-baa7-212735ff02e9 | -2.80898 | -53.06356 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 084eea07-371e-3dd2-a7a8-3323f6722187 | -3.1273 | -54.61101 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71b2b0e7-4a7b-3a1a-9013-b74a64384f12 | -1.45764 | -60.1657 | 2024-12-04 05:29:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d3458d4-af54-32f1-a2b8-c99dff0a2ee5 | -3.73039 | -51.08171 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ff9f359-c30f-397b-add3-55ccc6398184 | -2.61411 | -60.02316 | 2024-12-04 05:29:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf58ac81-c9b4-341e-8fbc-fb7224736717 | 1.04748 | -59.52689 | 2024-12-04 05:29:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51fdc974-8414-3889-97cf-703737ec92c6 | -3.78945 | -50.96706 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64de356a-7a4d-3326-8ea1-b68b9529e7a9 | -1.76142 | -52.63739 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6b474474-80d3-3e65-8870-0c630722f172 | -2.52741 | -53.97871 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf6ea9ad-8bc8-304b-85b8-f8110ee59925 | -3.33406 | -51.20243 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26343ba0-c59e-3f46-adfa-03b8ad183dc1 | -0.85276 | -52.70792 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4a5275f-9e79-3b28-9f16-f4b320d00f4a | -1.33728 | -54.96245 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc88f1e5-5e63-363a-aae2-d5b287e8cd03 | -2.84248 | -53.96163 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a1f15dc-774e-3276-b6d6-8dba300aa1c6 | -3.1821 | -54.33744 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ba5f034-cfc1-33c2-8a52-68dcdc496976 | -2.78667 | -52.86679 | 2024-12-04 05:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10827d0f-34ba-3aac-adc1-6400400e91fa | -1.75813 | -52.62461 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 84575032-db49-3e2c-9af0-d300c372a3b8 | -1.69531 | -52.3316 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30c36366-f0bd-338b-8e48-b4c0a670970e | -3.18393 | -54.33603 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d29733e-8efb-3a3e-97bc-e26fb79eae28 | -2.79473 | -53.05538 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e547b072-17a9-3b57-ad83-f5c7bcb91cd3 | -2.57215 | -54.00161 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94186d10-236f-31da-85a8-e3bb9536d809 | -3.40024 | -50.22744 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19a04b8c-4eb7-354e-b35f-5fa443fb16eb | -3.48113 | -53.80249 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0beca849-f6a7-3315-b817-731947c6768f | -3.12494 | -54.63111 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a1c49b5b-4999-3055-8016-c4759dea7111 | -3.11662 | -54.05049 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 048706e1-743f-3b83-9d3c-9272334056a6 | -2.20244 | -53.77238 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90ef9c6f-3507-3504-8b8b-d56231d10faa | -2.55904 | -53.40329 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92ff6a26-3ef9-3482-9515-8df6aa0825b9 | -1.78721 | -60.78176 | 2024-12-04 05:29:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f1aa4b9-c365-3296-adb5-c9c3fd7b491e | -3.0875 | -53.37555 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00704bf2-70d7-3d2f-b3cf-b4cedaf64e39 | -2.41951 | -54.01602 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 146aae0e-11b4-3c93-8bcb-a3ddfa360971 | -1.65937 | -52.39321 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a414f43-a96f-3dd0-977e-ea008df25f65 | -2.57386 | -54.8034 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8be7e498-80fa-3876-b918-bc5f00e79ddf | -1.64565 | -52.37832 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 549b2a30-491d-3f48-8329-014e27ed5f15 | -3.21783 | -53.12312 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 968e86b8-20f6-3d98-adca-e3ed45a72b55 | -3.26868 | -53.62628 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 62c5d6a7-d99f-3227-84d7-8c872864cfa3 | -3.28855 | -53.71246 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 53eab0c6-22e1-3521-a5f0-127bf2c66253 | -1.66247 | -52.752 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6ae06df-81f3-39db-9d9c-10901239b0e6 | -2.99277 | -54.10017 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6fd0cf5-cecf-3b21-92d1-3614d87601ed | -3.55903 | -51.51751 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a00bfe0c-9f14-316e-abed-789d081a4d0f | -2.52665 | -53.98371 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 287610b8-324d-3dce-8a1c-d07c66f786fa | -2.85725 | -54.05609 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c77ab6c-3510-3ee2-a8c6-fd3a0ac32d7c | -3.12759 | -54.61301 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 129a4a2e-edd6-37dc-ba8e-d4a7ab6ae079 | -3.12066 | -54.62388 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d95d295c-fab9-3648-a553-be0cacacd60c | -1.26877 | -54.11726 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b205041e-07f5-3285-b7e1-fcadf19fad2e | -3.8516 | -52.15855 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9e090d42-31d3-394d-9751-6b8534983efa | -2.34103 | -65.30946 | 2024-12-04 05:29:00 | NPP-375D | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 517b2ce3-2bc0-3d93-9161-026100a47810 | -2.82086 | -53.05347 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8cfdeaf-bcfe-3fc9-8017-de4596495609 | -3.11036 | -54.05697 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1fe5142e-0050-3598-b576-e36b1f1a6c6e | -3.8373 | -52.33287 | 2024-12-04 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6db557b2-d630-39bb-b8fb-1263793da8b5 | -1.87895 | -53.30628 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21b3bd70-8f04-3a5d-a282-42e6e98c0bcd | -3.32808 | -53.54612 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ef7e311-c45d-3d99-b49f-c8628add774d | -3.2589 | -53.62481 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26c2e59d-841e-3821-b0f2-e80c3be562e7 | -3.09619 | -54.05464 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b6800f6-8104-3482-ba1a-d6b46b82a17c | -1.2326 | -54.16879 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba6bb4d0-68ac-33a0-adf1-bada56d4942b | -2.78985 | -55.37275 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ff0548d-9ed7-3a9e-9e84-61bb8f2754ac | -1.65902 | -52.39303 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c4ca315-d8b3-38f2-9799-4b119f71547e | -1.25496 | -54.54187 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ec2e799-ce30-325e-9db4-9f4b55dff87c | -2.82041 | -53.05639 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77546294-c773-32d7-983a-ad9eedf9d5df | -1.66202 | -52.75493 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b95a0139-d7da-3403-be41-05b97d7fedb3 | -2.63246 | -48.06499 | 2024-12-04 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9dde13bf-404a-3db7-b54e-a8b7ed86c06d | -3.44745 | -54.08916 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aec2ea0f-ef59-3bcc-a8da-50185d5ef14a | -3.18321 | -54.34069 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1b903c5-fb3d-3a61-8b81-70ae1290949d | -3.13281 | -54.60917 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05f382c5-3abb-335f-b7b8-e8858107fc38 | -2.57183 | -54.80177 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3479650c-c6c5-337d-a31e-d664d901386b | -2.46357 | -53.62817 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77745ea2-0e0a-35be-b3fe-8ae334579c8e | -2.81715 | -53.04396 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f70ea8de-4f2c-35a9-98c5-908006a63637 | -2.88033 | -54.12539 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ee4417e-d30b-3496-8de7-eae2c2880e2f | -3.78355 | -50.96622 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95e63be3-9b7d-3361-9bd1-baf9e35bd953 | -3.26711 | -53.65465 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80d68cfc-f57e-342f-8d55-e751c6d1e06a | -2.89112 | -51.81994 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f9ac14-35e0-3c5e-87d7-e1c0810beec4 | -3.27199 | -53.65534 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8cc7fa71-d2f9-3dcc-9638-486cd9f09e69 | -2.19638 | -47.24492 | 2024-12-04 05:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f0abd3a-3095-3023-9fc8-74799785f209 | -1.44686 | -60.0816 | 2024-12-04 05:29:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 813a8e6b-a867-3d39-bf9b-54884d368328 | -1.70806 | -52.7837 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb512b2c-8ed8-3a91-b141-d432f24e3a7e | -2.81907 | -53.06511 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README57.md)
