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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 344e876e-75f9-3105-b9ff-9f51ddc844a2 | -6.92518 | -59.54016 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 843240b1-aaca-3fde-bb54-1ed7d0b7547a | -7.38791 | -44.88015 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75789975-e894-3313-a8ff-f337705d3eb8 | -3.95532 | -41.47736 | 2025-08-15 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 85adea6a-da44-3ada-beac-ee90e0c1b9ba | -7.28944 | -60.6242 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14dc7749-fa2b-3a40-bb2b-a0109fcdd6d5 | -6.97119 | -42.86996 | 2025-08-15 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9fe966d-531f-3b54-bcc8-5e91613d37a0 | -8.31194 | -45.02099 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06525cdd-10c9-374d-a440-8b325601ee20 | -6.10205 | -59.94953 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe195968-c5f1-3852-a717-a3a1eafdcf5b | -7.3943 | -44.86587 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c38da13-42ed-3f64-b0a9-e079b6d6a056 | -6.0679 | -59.95797 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 76deb4c2-8d14-3c94-9c44-8b6f5b2a534b | -6.87531 | -59.15815 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ece1758a-540d-3b6c-8f63-dc00b1d9fb5d | -7.26479 | -60.63498 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c61bdd8b-64c6-3e34-a405-c7dcbf6a3474 | -5.36902 | -41.23733 | 2025-08-15 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 83dfd523-89e5-3b18-ad1d-5117a133fc12 | -7.57211 | -47.0647 | 2025-08-15 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2e223ad-b352-3cc2-8745-01988c5f3f30 | -6.90707 | -59.63755 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e1327d1-d0d3-38e6-acfc-f5a6a4f52994 | -6.08916 | -44.61553 | 2025-08-15 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52ceb1e7-c117-36e2-a69d-96666675a2b9 | -3.82741 | -47.73944 | 2025-08-15 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6debaa7-f0d9-3862-930f-9b8e2986503f | -7.02072 | -44.30057 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42e47bef-2e6e-3f4f-a949-a246f3114e72 | -7.39714 | -44.87002 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad513529-0fc4-32b4-9654-6e65e24d7550 | -7.86005 | -48.23262 | 2025-08-15 04:27:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ccf3c23f-1829-31b7-8c1e-fecde310d6d8 | -7.86407 | -48.22947 | 2025-08-15 04:27:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 98b5d02e-daad-3860-b84e-e7b6f837caa2 | -8.31647 | -45.01419 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f22bc7b-cac8-31e5-abdf-09371f73792b | -6.27549 | -44.96382 | 2025-08-15 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 17821589-5245-3e9d-8a7a-3801ec5f4d0a | -3.49671 | -43.31283 | 2025-08-15 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0c56563-d825-3824-ba44-6cf8da46e743 | -7.59878 | -55.19679 | 2025-08-15 04:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dd92ebc-b239-3421-a4fd-93bd16774c61 | -6.9083 | -59.63097 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1aff10c-89d5-328d-a053-46d7c5d184ec | -6.54187 | -43.50197 | 2025-08-15 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 050e7c7b-3ef7-3c98-a7c7-41f1b7553ed0 | -2.88968 | -48.03062 | 2025-08-15 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b353817-c709-36d0-a0ca-1d8157716cab | -6.87442 | -59.83593 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4b0b9c3-6bb9-3480-919c-7dd0388d22a6 | -7.07785 | -59.2249 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ed75383-588a-3258-8071-883d96f1c41e | -3.80845 | -48.98979 | 2025-08-15 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffda5a2a-f8c6-34c3-873f-cd96192f08e6 | -6.33418 | -42.80029 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0df5fc3b-9d25-3dd7-93ce-1eaea768800c | -6.33356 | -42.80444 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4195c07f-5da9-3680-b8e1-0a267dfe0b79 | -7.14381 | -44.40303 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50774bac-f7a6-31c4-9f00-3eceaedfc32a | -6.9333 | -59.53015 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04290b87-e1f2-357d-ae33-3dcfe366c6ce | -9.83997 | -47.80591 | 2025-08-15 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 735b3884-97c7-344b-957c-37e9bf2363b4 | -7.07224 | -59.21783 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 56146d8c-71d1-31d6-aad5-e19096229ba8 | -6.71792 | -58.82119 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d85e6fab-eca6-3259-82bc-57516ff4f3e0 | -3.32138 | -48.72096 | 2025-08-15 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb149049-c973-3c89-b79a-5eb617c25b8e | -7.85945 | -48.23631 | 2025-08-15 04:27:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e162ce01-d32a-3a55-ae5d-b2c3b7e66c09 | -6.9087 | -59.14106 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d625999-df7f-3177-acfc-4a720b01336a | -3.48298 | -51.19021 | 2025-08-15 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44c7cebd-7fdd-3cbc-a192-33cac2730d56 | -6.93782 | -44.56547 | 2025-08-15 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 415e0bcc-a305-3bd4-a917-1841c59c413d | -6.11054 | -59.94374 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6d0200a-8fc2-3978-aeb6-a00cd68a3c09 | -6.55547 | -49.50873 | 2025-08-15 04:27:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 049ba426-ef83-3726-98fd-db785a4f6be2 | -9.03422 | -40.52769 | 2025-08-15 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c440c9e9-f195-3375-9d41-7dcfaf635da1 | -7.31581 | -44.69353 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdc9a509-6215-3bdf-986c-5a500ad90aa5 | -7.85663 | -48.23209 | 2025-08-15 04:27:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71bb5204-9547-36a3-baa3-82fd6e83ee18 | -10.53698 | -42.55293 | 2025-08-15 04:27:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 23191cb1-9971-3d16-85f5-37438c4ccc99 | -7.08012 | -59.21315 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6cf0bde-a9c2-3fb0-b4d0-e923e100e077 | -6.97055 | -42.87427 | 2025-08-15 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 68db8a7e-b189-3877-8d68-54e5fd034267 | -9.8394 | -47.80945 | 2025-08-15 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 137156cf-7801-39a8-a5f0-c28361fdd706 | -3.99177 | -47.83508 | 2025-08-15 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d9166d0-369a-3a0b-83a3-ed0224927111 | -10.18622 | -49.50533 | 2025-08-15 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2523869f-4bbe-3e78-9bf4-9682c438889f | -7.08572 | -59.22033 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ddc1099-85b3-3a55-92ab-b79d6c7ac197 | -6.06211 | -59.94942 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cde1909a-3331-3f76-b54a-e04b76fc20df | -3.31773 | -48.72038 | 2025-08-15 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5aba0be5-396e-3ca8-988a-1d755a2908d8 | -6.59155 | -44.64083 | 2025-08-15 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8b9e090-2826-3663-ae6a-89ba697b16a7 | -4.60254 | -43.31871 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 509f1696-37f7-3f53-b0f0-dca164735976 | -5.09322 | -47.71648 | 2025-08-15 04:27:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb0c4ac7-23ba-3ac6-92f5-73174776e6f7 | -6.10384 | -44.61034 | 2025-08-15 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb56d762-a16d-3cc0-8119-09f06f22ce69 | -6.90741 | -45.20685 | 2025-08-15 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4ebe793-17ef-3907-801d-adcc1001aaf4 | -6.89412 | -59.14443 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e77b3e08-d8df-3b13-a254-4cd0ca0c796f | -6.89986 | -59.13843 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ec2246b-6214-3897-8bad-07cd024ab429 | -9.72499 | -48.02882 | 2025-08-15 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ea50db28-6cdd-38cd-a465-80fdcff7856a | -7.31357 | -60.62053 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7901e8b0-baba-347b-8390-8260b1ec82fb | -6.07055 | -59.94374 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a218eccc-c1f9-37ab-a6b2-7b434507a286 | -6.93411 | -59.63776 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9657138d-9c77-3e2c-8ffe-ba023f68e090 | -7.07669 | -59.23093 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db56733c-a142-3f50-8b6c-133b83d78c3f | -6.07495 | -59.9598 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 247e114f-cf59-330f-bfbb-7adae5a768f3 | -4.29548 | -48.0618 | 2025-08-15 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aeca601-3b7d-3c5a-babb-06dc34b60e97 | -11.23397 | -41.50244 | 2025-08-15 04:27:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8f98388-ad8c-3d82-878b-33f0c1ad389e | -5.22483 | -43.18763 | 2025-08-15 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 424ab0ad-a75b-3234-8c94-2de17db98b43 | -6.87726 | -59.1596 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b28a6b67-5b82-30f5-a9d9-7f44cd55787a | -6.08467 | -59.94721 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 22ec00aa-8e59-3ac0-a674-aada8f3f6ea0 | -7.24089 | -57.68493 | 2025-08-15 04:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6cee0cfe-181a-3a43-bf6a-ceed00c2aee7 | -7.3783 | -44.89724 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15d14522-b00b-3ca0-9dfa-34b0e1911a93 | -7.38678 | -44.88739 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 062807da-fd81-3296-9e21-32fa775f39b9 | -8.29722 | -45.00372 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b47cb9b2-e86a-3ff3-8e5e-e8cea133672b | -2.77146 | -49.19807 | 2025-08-15 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce8957a5-329e-3ad1-a326-90c7803b3714 | -6.24352 | -43.23288 | 2025-08-15 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed0ea006-defd-319e-96b5-18a0255c579c | -8.33561 | -40.97945 | 2025-08-15 04:27:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 581bb872-44fb-37f4-a457-0b534517a3d6 | -6.91221 | -59.14694 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71aa1dd1-1c0e-3dd1-aabe-6b7decfc91ae | -4.24189 | -47.27155 | 2025-08-15 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e656021-b852-3dc0-b0af-fb01fb927cb4 | -6.72485 | -58.84148 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e4cb5d0d-f02a-3113-85ab-9cf18501a955 | -4.60544 | -43.32312 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 250ec971-41d7-36dd-a45a-8f462f4e7db8 | -7.56878 | -47.06416 | 2025-08-15 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d8e1082-3589-3f3c-894f-24dca56cb1fc | -6.95127 | -60.0068 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 57d5f73e-3cdc-34ca-81a3-e3f2660b7f5d | -8.31307 | -45.01367 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8700f4a-c493-32d2-aaa8-a4fbf3b84494 | -6.88627 | -59.14901 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28faf483-780f-3a77-84ac-a7208e9302a6 | -8.31477 | -45.02516 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62772011-cece-324a-ac24-3a4d9b383583 | -4.59615 | -43.31376 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e81225e5-e394-3b07-b101-9c95e73402e1 | -6.65626 | -58.82097 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d95f9f81-6cce-3141-9e17-8c64fe6638cc | -8.5148 | -43.32355 | 2025-08-15 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2208bd02-bc88-3d2f-982a-3d98fe3e1cb3 | -8.28986 | -45.00634 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9bfc37e-d6ee-3a1c-a33e-5287770d7a7b | -5.61405 | -43.46893 | 2025-08-15 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8075d4c1-f41f-37c5-8d55-bedb6ccf3b2f | -6.72907 | -58.83508 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 826a274a-bb12-3a7b-9bd4-5dbd5cb665ff | -3.44219 | -48.96652 | 2025-08-15 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edef7641-3809-3291-9e13-c9537f282a2a | -6.94235 | -59.82183 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcbfc08b-78dd-3b24-a21d-b02ff20b7274 | -6.22536 | -43.33896 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df756fa9-efb6-39a1-a63c-6501065c7b71 | -7.08459 | -59.22618 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README32.md)
