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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a782bf53-762c-3d61-84a2-89ab545be369 | -3.82179 | -48.88194 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8db30000-7faf-30f5-8eb3-abf835ceb944 | -3.82017 | -48.89223 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bdf53fa-c200-3598-a77c-e62b68189d21 | -3.81903 | -48.87799 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34a870d8-926d-311b-9f5b-a1a8ba01c3b7 | -3.81849 | -48.88142 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b38314ec-3eb7-379c-9d03-22724f926aa4 | -3.81741 | -48.88829 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a74b532-2fd0-3f87-9588-d8187844f7c3 | -3.81573 | -48.87748 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b1e5b1e-1e64-3c36-b406-6e73e79d7b18 | -3.81519 | -48.88091 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b69ac13-906a-3a61-a0ee-54d3b0918e4f | -3.81243 | -48.87697 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56205fa1-25ed-3c3d-beb9-efe8c4f9d035 | -3.81189 | -48.8804 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 103afddb-1ffa-3dcb-912e-d67ed76ce228 | -3.77332 | -48.90538 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85b52ee7-9a09-3fb3-841e-4bcf08c1f873 | -0.23682 | -48.5838 | 2024-10-29 04:38:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 028b8a3b-51c9-3b65-b6ee-d12f2e3e5361 | 0.09197 | -49.8573 | 2024-10-29 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bac897fe-a1d0-314a-acf4-dcfdf5d1313f | 0.08856 | -49.85782 | 2024-10-29 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82297555-5698-3ef3-9d21-8ba71fabbebf | 0.08403 | -49.87363 | 2024-10-29 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ade3cb02-a760-3466-9db4-f439a62633cb | 0.08346 | -49.86994 | 2024-10-29 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4745cd05-17b4-3f94-b693-905c78542a9f | 0.08062 | -49.87416 | 2024-10-29 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 297c2f03-1535-3885-95dc-4d50ac75ffbd | 0.08004 | -49.87046 | 2024-10-29 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 393a6d26-f7a0-3fe1-b504-4e90ea77d1d8 | 0.01089 | -49.44938 | 2024-10-29 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74814cb8-5676-36db-b8d6-ba9e806cfdf6 | -2.15474 | -48.83248 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77b8d4a9-97b2-3b56-ad79-76e5f1de7f36 | -2.06241 | -48.88158 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02504b7b-f694-3b7f-abfb-0d0cf93079cf | -2.06186 | -48.88502 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81760bd4-315b-3a73-979d-52f5acfcb55a | -2.05848 | -48.88094 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b02014b-7e83-363a-b321-a0a137bd935c | -2.05517 | -48.88043 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1434754e-07b1-36b6-98a7-f0a847938c01 | -2.00924 | -49.00037 | 2024-10-29 04:38:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89292fc2-8ebc-3f4f-9a87-c08f1fbbe7f2 | -2.0087 | -49.00383 | 2024-10-29 04:38:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ef8487a-abdd-3718-a9c7-13e097627c21 | -1.0679 | -48.71066 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5237b109-bb23-3c92-8486-8a1d82cba3c2 | -0.86571 | -49.06578 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a38d551c-edd2-34c7-a587-7f72f861232c | -0.86239 | -49.06527 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78e9b00f-0965-32b3-9d33-d2e14edfb1d3 | -1.02568 | -49.32405 | 2024-10-29 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac7c69d1-f0d2-3408-95ef-a4b141936a65 | -2.15436 | -49.31103 | 2024-10-29 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e9a80ea-9734-3afc-b3dd-497c1298ec2f | -2.15201 | -49.65171 | 2024-10-29 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8330d39b-e22e-389d-a9c4-90f7d4389033 | -2.15146 | -49.65524 | 2024-10-29 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 230b1ba6-076e-37cf-b8b3-81b63c4766b8 | -2.10072 | -49.69447 | 2024-10-29 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b4b5daf-80eb-31fb-848c-31c596ea4868 | -2.03911 | -50.08478 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80855b7c-950c-33da-b68c-42c4c971c850 | -3.60904 | -49.86236 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad432456-4abe-3ed2-9045-f01339a01bf7 | -3.60848 | -49.86588 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ca1837d-0273-3e26-9604-fc1228e588ba | -3.6057 | -49.86183 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 193b573e-f1ad-354a-8c62-014c0707eb9b | -3.37006 | -50.55289 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b59b75a7-227e-3ff2-9ac5-d7e55b9dfadb | -3.16746 | -50.58925 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4d2bd89-9fc5-391d-9b16-91b9c73e71cf | -3.16405 | -50.58871 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3df88d1-9546-3489-ac65-48eeba42933e | -2.68189 | -49.35459 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f480ff5a-bd13-363a-af16-37e0405a330e | -2.66802 | -49.31334 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8fd32e2e-db3d-3470-9782-6a99aee9dbb4 | -2.66479 | -49.39822 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5cb09410-a123-3e22-88a8-e1f43a24d018 | -2.66424 | -49.4017 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c8f3430-0b2f-3c19-a88f-786c0450a5fe | -2.66408 | -49.25238 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdbc210d-c857-3610-b2c0-f128004feae0 | -2.66353 | -49.25584 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4e548f7-bfaf-388d-aa0c-27dba3f58d27 | -2.66298 | -49.2593 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23f17ddf-63a0-3f22-bdc4-3244e6aca82f | -2.66021 | -49.25533 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e0017092-80e6-377b-bc46-bff99be05477 | -2.65745 | -49.25135 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff017575-1e47-3984-b136-4020ee8b92a0 | -2.65635 | -49.25827 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b778c082-d001-3219-8ce1-efeac4165dfc | -2.65583 | -49.28303 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 713fd429-5ff8-320e-a7c5-bd3fb3b4fe37 | -2.6558 | -49.26174 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0e0d300-a724-3004-97b2-684a6ecd4a09 | -2.64929 | -49.38868 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 075ffed7-fefb-37b9-9ee3-89dc0bb6b9dd | -2.64874 | -49.39216 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11b76820-23c0-347c-ab8c-dd7af1a9e3a3 | -2.64722 | -49.7038 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4c8b8a2-bd73-358d-b454-31aa7cc55121 | -2.64652 | -49.38469 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6d0f5b10-18e4-3239-911a-043e13a66570 | -2.63552 | -49.23728 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 690a7006-e9ab-31f2-ab30-ffa3669a068b | -2.63117 | -49.26498 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37170a5f-baf9-3b2c-a9f4-de941bfd2ade | -2.62785 | -49.26447 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95e9a267-8643-33fe-a313-5ae7ab97624e | -2.62708 | -49.42089 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d85c7aed-09d5-3641-85cd-90497c6fc833 | -2.62454 | -49.26395 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3df76b67-5168-382a-b315-4511b2141fcc | -2.62177 | -49.25997 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a274ee5f-1389-384f-93a6-13234d018a6a | -2.61627 | -49.27331 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f62d408-f995-302f-ade8-a2d5a210c627 | -2.6135 | -49.26933 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2daff61-0997-364f-96dd-b6a35b051f42 | -2.60684 | -50.02509 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 065c96c3-9631-3247-9c19-4d6616d97087 | -2.60347 | -50.02456 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35acffb3-a101-353c-ac27-9306b848d7fa | -2.6029 | -50.02815 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82e790fe-4338-339d-a9ec-27268f957df5 | -2.60036 | -49.33125 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c488c334-2310-33a6-a8ad-1084cc7d2715 | -2.59953 | -50.02762 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 362844d3-3399-3aed-b38f-006a0a3ffdb7 | -2.59951 | -49.48805 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9445143-b020-351b-9410-68600396c30e | -2.59704 | -49.33073 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 66d94b2b-fe90-3d59-bf62-b530677bf3e4 | -2.59213 | -49.66279 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f83d6e0-dfb5-3f32-a9d2-3b6af877516a | -2.58859 | -49.23354 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c001a57-80c9-338a-a501-c2295cf6059a | -2.58141 | -49.23598 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f431b47-4fa7-30cd-bc58-c54192a311da | -2.57755 | -49.23892 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76ce72a4-4d8e-3252-b1e5-e424dbc03abb | -2.57369 | -49.24187 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31b5acb6-ad24-33f0-b79c-aa06845ced39 | -2.56375 | -49.24033 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e154e20-f384-3895-be5f-4d681ff637d3 | -2.56098 | -49.23635 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f921147-9d1f-3f80-9d38-b0e8ebaff7f1 | -2.5566 | -49.26405 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ec3cc15-3b90-3717-a6af-d8f8b000d40f | -2.54531 | -49.81113 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c11768b-cd2f-3fba-8404-0aa08b0135b5 | -2.54251 | -49.80706 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 429cee79-f6ed-36b1-be5b-b7a55f13d948 | -2.52631 | -49.86638 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9e54229-2e53-3fae-acdb-aded28674cdd | -2.51519 | -49.71949 | 2024-10-29 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4554986f-348d-3721-8bc5-205938625121 | -2.50534 | -49.37335 | 2024-10-29 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28922ee6-3fbd-3be2-991c-6df7b1acd4d4 | -2.4863 | -49.23527 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cf7de92-5025-3a9b-8047-137f173d02a7 | -2.47158 | -49.37167 | 2024-10-29 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3d54f55-2eb3-3e92-83f6-c6f3870e478f | -2.46267 | -49.79103 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64ad28bd-256d-30dc-9fb1-c281658df15f | -2.46034 | -49.79065 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aeb50ae5-45a1-343b-b0e1-dc1a96126fe7 | -2.43298 | -49.76825 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d077ffe0-bd2b-3e72-913c-e1809e4c8083 | -2.41564 | -49.87836 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bab0a6d3-a32b-3abe-9bcd-8e280b57794b | -2.40504 | -49.81478 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aeacc837-72f2-3d24-a9dd-ea3c864e0a2b | -2.40448 | -49.81833 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7393eff0-ecb9-369a-9eff-d7d47267c17a | -2.39665 | -49.82439 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bdb1b26-393e-3f29-8545-13153ba23745 | -2.3919 | -49.38021 | 2024-10-29 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36bec435-2e92-3bb2-9fcc-e05ca49ce518 | -2.38777 | -49.23367 | 2024-10-29 04:38:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3cf3f12-e1f6-3a25-8cc9-71f5cf781b66 | -2.45823 | -48.95813 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d83665ea-a5b7-393f-add5-e98f3453063e | -2.45535 | -48.91187 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 99a74fa8-af13-3586-b15b-67b59e1498c4 | -2.45108 | -48.96055 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abdc9abc-703d-35bd-8708-d94dacf6cd47 | -2.44356 | -49.02994 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 824ca6f7-ae1e-3099-b9a1-07935875e63c | -2.43972 | -49.03288 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README43.md)
