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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 977acd57-1f6b-3b5f-b7f0-89fa0321f376 | -11.94237 | -58.76477 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4a1dbcd-51e6-3951-bce2-9718f2118703 | -11.61508 | -58.29149 | 2025-06-19 06:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f9fe705-7b17-3d31-b833-241b0df60c1a | -16.30965 | -58.25097 | 2025-06-19 06:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4d6366c4-a885-33a3-9c1f-1be91906153d | -11.95872 | -58.73805 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a81d1f43-1f58-388f-a51e-f5034975c080 | -11.95266 | -58.74833 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 9a387afd-b2c4-39e3-b3fb-1a512917a72a | -11.96343 | -58.75561 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d388faa-f316-3683-80f3-cad542d08459 | -11.95678 | -58.75538 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 50221338-c1dd-33b0-aa16-68f854517c37 | -13.57908 | -59.20527 | 2025-06-19 06:01:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23dfc4f2-3285-33a0-b30a-da4ff4cb436d | -11.95082 | -58.7489 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| d7b79d84-3aa6-3011-9500-14be854995a2 | -11.952 | -58.7376 | 2025-06-19 06:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| e4fe4419-1a21-3c66-9835-a9485ef62806 | -11.9709 | -58.7362 | 2025-06-19 06:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 4ba1e12b-8fef-3ed3-b653-1cb5c6afa952 | -11.9707 | -58.756 | 2025-06-19 06:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| ed6c0a2b-0f72-3bc3-9544-56b76cb2717c | -11.9518 | -58.7574 | 2025-06-19 06:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 88bafa02-42b0-3095-b5e4-b6c787e630ef | -8.0703 | -43.0981 | 2025-06-19 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 9114d9bc-8465-3cdb-835e-491ad72dc086 | -11.9709 | -58.7362 | 2025-06-19 06:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 92cbea80-af5b-3d34-8708-28678dcf8628 | -11.9518 | -58.7574 | 2025-06-19 06:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 82b6dc62-f44b-3d02-bc85-9d7965b99568 | -11.9707 | -58.756 | 2025-06-19 06:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 99de9c88-ed42-3b2d-97e9-9428d73b079d | -11.952 | -58.7376 | 2025-06-19 06:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 9c9b24f6-3320-3a69-801e-3f6039298a8a | -8.0703 | -43.0981 | 2025-06-19 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 062e22b4-4d99-39d7-8225-9dfba0682242 | -11.9518 | -58.7574 | 2025-06-19 06:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| a861f3be-67a6-3a5a-bcae-1cfefb0925ac | -8.07 | -43.1216 | 2025-06-19 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| f76d15eb-d57c-313c-b159-b96e5d7ea189 | -11.952 | -58.7376 | 2025-06-19 06:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| c2112dc9-33a6-306e-8a74-517afaba832c | -8.0703 | -43.0981 | 2025-06-19 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| aecec81e-411c-30f5-974f-cd3684b8468e | -11.9707 | -58.756 | 2025-06-19 06:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 465303be-b129-3a6f-be2d-e5f714e76e1a | -11.9709 | -58.7362 | 2025-06-19 06:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| dcd370ba-ce37-3940-9c92-6cca942d7333 | -8.07 | -43.1216 | 2025-06-19 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| ec2a909c-bf23-3e24-8886-5996f9bdc2e6 | -11.9707 | -58.756 | 2025-06-19 06:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 03e20cde-8a95-3c19-98cc-b7fff38687a8 | -8.0703 | -43.0981 | 2025-06-19 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 843abe9b-cde7-3bf1-80b5-baa1570ce32d | -11.9709 | -58.7362 | 2025-06-19 06:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 89bec8fa-8887-3564-95d2-a0977172e139 | -11.952 | -58.7376 | 2025-06-19 06:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 4ea4b50e-4dfc-3d35-8cf6-255ad7b66ff2 | -11.9518 | -58.7574 | 2025-06-19 06:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| ba76eac2-e245-37ec-9f87-0011c2c67196 | -11.9707 | -58.756 | 2025-06-19 06:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 38551a4d-9bf8-3443-9e3d-c6ac868013cf | -8.0703 | -43.0981 | 2025-06-19 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 624b22b3-c256-31ef-80c6-0e53e4f16316 | -11.9709 | -58.7362 | 2025-06-19 06:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 7b76b6a7-e679-3ced-9235-4f750e57f79f | -11.952 | -58.7376 | 2025-06-19 06:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 56d43961-b670-3ab3-87c2-eb9daacd5417 | -11.9518 | -58.7574 | 2025-06-19 06:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 65b5aa6b-8113-32ba-94a0-bd03a0c8ddc2 | -11.95975 | -58.74923 | 2025-06-19 06:52:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 904b0730-a4e8-30cb-bb63-c42d59187df2 | -11.94825 | -58.74769 | 2025-06-19 06:52:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 168.0 |
| b66d3672-6b13-31a0-980f-2c3e33d07ba3 | -11.95031 | -58.73166 | 2025-06-19 06:52:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1aca36cb-edbe-360b-8f61-f087f23f60ed | -11.93802 | -58.75513 | 2025-06-19 06:52:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| af932820-6f5d-357e-b103-0528aecb21c6 | -9.49313 | -56.08959 | 2025-06-19 06:52:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 14e68c36-a49c-3ccb-bfd5-9760c87cf4ed | -11.96182 | -58.73326 | 2025-06-19 06:52:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| dd5e53d1-eb08-38eb-9eaa-28d16168f6ab | -16.30396 | -58.25246 | 2025-06-19 06:52:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| bb9b36c0-5c2f-3e73-b7e1-1af7f0ba9dad | -16.30381 | -58.25757 | 2025-06-19 06:52:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 419ed25e-f4ff-3e67-a680-e246b6e2c889 | -11.9709 | -58.7362 | 2025-06-19 07:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 18f40094-9bfe-3adb-b896-c194dfbdda05 | -11.952 | -58.7376 | 2025-06-19 07:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| cbd5a55c-6d50-3ebd-ae31-6995750ff81d | -11.9518 | -58.7574 | 2025-06-19 07:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2d07d623-9534-32f7-971d-13aba0e59e6b | -8.0703 | -43.0981 | 2025-06-19 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| e6451d75-02cf-3f8b-8e29-b66c1b181cce | -11.952 | -58.7376 | 2025-06-19 07:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| fbe786f6-8a8f-3404-a30a-f5126dd97442 | -11.9709 | -58.7362 | 2025-06-19 07:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 5dc680c8-57d0-394a-b686-581421ddc21a | -8.07 | -43.1216 | 2025-06-19 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 08815878-e987-396e-9af2-9d578849cf4b | -8.0703 | -43.0981 | 2025-06-19 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| dda349e6-5b4b-3183-975c-e33f1852cb65 | -11.9518 | -58.7574 | 2025-06-19 07:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 18067618-0c1a-371b-a3fc-39b0b74fd312 | -11.9707 | -58.756 | 2025-06-19 07:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 3d9679e2-dfb3-3b0a-b4a8-e950015c5d24 | -8.0703 | -43.0981 | 2025-06-19 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| ec5a5358-e118-356b-8db8-8de26b1173c2 | -8.07 | -43.1216 | 2025-06-19 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 5e20c89d-93ad-3ecf-9039-64b5826ee613 | -8.0892 | -43.096 | 2025-06-19 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| ead50226-c5ff-3c02-8601-be3b12eeffbf | -11.9518 | -58.7574 | 2025-06-19 07:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 59acc2e7-1131-32d3-b38f-bd1a1db56fee | -8.0703 | -43.0981 | 2025-06-19 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 559ca0fc-16d4-3c5d-8420-da3a1bf995b5 | -11.952 | -58.7376 | 2025-06-19 07:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 90cd5ad6-709b-39d6-87dd-adfeb780caab | -11.952 | -58.7376 | 2025-06-19 07:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 42c5a50b-b6d4-30d9-9fe2-eb1de8992200 | -11.9518 | -58.7574 | 2025-06-19 07:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b57cd5cd-37ed-39cb-8e7e-b63a56912a3f | -8.0703 | -43.0981 | 2025-06-19 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 77b16bbf-fab7-3cb0-b5ef-e021666b5d65 | -8.07 | -43.1216 | 2025-06-19 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 8a20f9bc-04bd-35e5-9b51-a2ce030cceda | -8.07 | -43.1216 | 2025-06-19 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.4 |
| 6a9e1bb1-350e-3739-91ff-b98507d52ffb | -8.0703 | -43.0981 | 2025-06-19 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| 897059d0-7f45-3ef7-9920-090daeb5a4f3 | -11.952 | -58.7376 | 2025-06-19 07:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f8a2a6ce-51db-3fe1-bff6-57d9b607883b | -11.9518 | -58.7574 | 2025-06-19 07:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| ccbede07-39b9-3119-bbb2-d85e4182a8bb | -8.0703 | -43.0981 | 2025-06-19 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 44b8e6c7-3222-3688-91c6-ac8230046063 | -11.9518 | -58.7574 | 2025-06-19 08:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4b0526e5-1149-3572-8481-7063764676ca | -11.952 | -58.7376 | 2025-06-19 08:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 3804e882-617a-3601-986d-c442cce44843 | -8.0703 | -43.0981 | 2025-06-19 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| d687b260-8fb5-3861-a4d1-f7cf50712b27 | -11.952 | -58.7376 | 2025-06-19 08:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 7bbff559-259f-319b-868e-b56220d9b58e | -11.9518 | -58.7574 | 2025-06-19 08:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 54e2a4cf-8612-3a96-898b-5c9d0b909342 | -8.0703 | -43.0981 | 2025-06-19 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 9f72d760-6454-354d-a166-6625241ea150 | -11.9518 | -58.7574 | 2025-06-19 08:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| d231360a-2d2e-385b-bc54-4aa2f02f7137 | -11.952 | -58.7376 | 2025-06-19 08:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| d7f1e5fb-ddd0-3850-8322-5518d3116dd2 | -8.07 | -43.1216 | 2025-06-19 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.3 |
| 6bb32200-b442-3313-b3b5-4f2b5bd86887 | -11.9518 | -58.7574 | 2025-06-19 08:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 27bf721f-bb8f-3ed1-8432-415715991614 | -11.9709 | -58.7362 | 2025-06-19 08:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 3013715d-fc5f-3dd3-ae8f-270b69862ec2 | -11.9707 | -58.756 | 2025-06-19 08:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 8c3a9665-fe8d-3a0f-857f-71f0af78bb31 | -11.952 | -58.7376 | 2025-06-19 08:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f0124d1d-7804-3e03-b463-32b3258d1df3 | -11.9518 | -58.7574 | 2025-06-19 08:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| fa143f1b-9567-397e-85ce-24c813037b3c | -11.952 | -58.7376 | 2025-06-19 08:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 4905b412-719d-348a-b9ed-bcedd6780ae9 | -11.952 | -58.7376 | 2025-06-19 09:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 4933c411-de6d-39b6-9cd9-4ef1e0bda490 | -11.9709 | -58.7362 | 2025-06-19 09:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| f9fe9b5a-9a50-3055-aa79-83b97025ee11 | -11.9518 | -58.7574 | 2025-06-19 09:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 847d70a9-adb5-3b80-9fbf-78956955e72f | -11.9709 | -58.7362 | 2025-06-19 09:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 62dc5040-4397-329c-8e9b-c2fa3f37abef | -11.952 | -58.7376 | 2025-06-19 09:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b0e744b8-c812-3502-b10a-9732ae086828 | -11.9518 | -58.7574 | 2025-06-19 09:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 334d0c4d-56f7-3ccb-b1e2-31225d0038fa | -11.952 | -58.7376 | 2025-06-19 09:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| cba175d1-939c-385f-bb9d-17bb2b003d72 | -11.9518 | -58.7574 | 2025-06-19 09:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 20c51af6-e7f5-30a9-8144-7f5bc1984879 | -11.952 | -58.7376 | 2025-06-19 09:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 535a91d7-4e61-37ff-a886-5e33a1818ecf | -11.9518 | -58.7574 | 2025-06-19 09:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| b3c321fe-e2a6-3bde-ba2e-584d5b8910e9 | -16.3185 | -53.8094 | 2025-06-19 11:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| c2b98e2e-1b21-3b1b-88bd-10976ce17a3f | -8.5911 | -51.5537 | 2025-06-19 11:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 74b667ff-b8c7-3f4c-b255-3f4ac3fac581 | -8.5911 | -51.5537 | 2025-06-19 11:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a2333674-ada8-38cc-b448-e988c4e3b364 | -16.3185 | -53.8094 | 2025-06-19 11:50:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 7f7c559d-e23b-31c3-83ef-30b4ac758e4a | -4.8375 | -43.1919 | 2025-06-19 12:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| a17160fa-16bf-355e-9a61-fa58834b1490 | -16.3185 | -53.8094 | 2025-06-19 12:00:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 172.2 |


[Clique aqui para ver as próximas entradas](README27.md)
