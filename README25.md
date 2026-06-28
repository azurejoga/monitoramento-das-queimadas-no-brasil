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
| 3a510e36-e6cb-32dd-a94e-6c69893c6a6c | -10.93388 | -56.85539 | 2026-06-28 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46fbbb70-5843-30a6-8438-798296a04e93 | -11.22076 | -54.30584 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e622ef2-c37d-355b-bfb0-6e650ce74783 | -10.054 | -59.11424 | 2026-06-28 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16697076-adea-3c5c-bde1-b2dfdde17844 | -10.0618 | -59.11035 | 2026-06-28 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1fbf501-012b-3ce0-a0a2-35a1fbb24a28 | -10.29634 | -57.13821 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ee4a5c0-e626-32f3-b879-eff3760db15d | -9.09077 | -59.40467 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b8b7edcf-0af9-3359-a7c8-2bf7e099bd61 | -11.20875 | -54.31143 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3a8a2d47-9a1d-340e-8b8d-f14e35a877ed | -12.194 | -52.8657 | 2026-06-28 06:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b67a08e8-0e49-329d-afd1-4be424110741 | -17.3442 | -42.6333 | 2026-06-28 06:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 49.2 |
| cbf356c2-f858-3efa-a89b-b6e5fa97d76d | -11.209 | -54.3053 | 2026-06-28 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 52c1bce9-59ef-3139-89ba-853abce3bf4b | -12.1937 | -52.8866 | 2026-06-28 06:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 5e3a7cfc-6283-31c1-b1d8-5d2b9482da86 | -11.2279 | -54.3036 | 2026-06-28 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f1a6846f-0c3f-354e-9f97-f71c08cad109 | -12.194 | -52.8657 | 2026-06-28 06:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a6f21b17-48b1-385b-ade3-46fb269e0e76 | -12.1937 | -52.8866 | 2026-06-28 06:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| cbcdf2df-46e1-35e0-984a-6d94eb5e5f71 | -11.209 | -54.3053 | 2026-06-28 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c1f1319f-5a31-31ed-b4b9-2c417fe5bdd5 | -11.209 | -54.3053 | 2026-06-28 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| ace795d1-f821-3f81-9b88-0ef3e9b300cd | -12.194 | -52.8657 | 2026-06-28 06:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f30cbaf7-d7a4-33bb-9166-5e249bd557d4 | -12.1937 | -52.8866 | 2026-06-28 06:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 36b3a7b4-269f-3e61-9227-1f97e94807fc | -17.3442 | -42.6333 | 2026-06-28 06:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 46.6 |
| ec6d5e90-c2af-3b36-b969-6a85c2ebb0cd | -17.3643 | -42.6284 | 2026-06-28 06:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 67acc915-997d-348e-afbe-f61ad5f20c59 | -12.194 | -52.8657 | 2026-06-28 06:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| fa5ceba1-994f-3c60-a52c-7bb05e2ad60f | -11.209 | -54.3053 | 2026-06-28 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6c4ab31f-6411-33da-8b4e-ad66f6758f0d | -12.1937 | -52.8866 | 2026-06-28 06:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d7b8792a-583b-30ba-b4a7-4f869473fd61 | -17.3442 | -42.6333 | 2026-06-28 06:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6eb38dbb-0af8-3c83-b450-9d12dd20d1f5 | -12.1937 | -52.8866 | 2026-06-28 06:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 27cb46ed-6bd4-3b44-a051-283915eada2c | -11.209 | -54.3053 | 2026-06-28 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 67209c67-a57a-3eb8-b9ad-568533678fb0 | -12.1937 | -52.8866 | 2026-06-28 06:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9d6a06a7-4a0d-3734-b729-f79ee5933f9f | -17.3442 | -42.6333 | 2026-06-28 06:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 1cf41491-e523-3cf8-b895-53390c52864b | -11.209 | -54.3053 | 2026-06-28 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e23116fe-e416-3880-a41e-978052cafbe4 | -12.1937 | -52.8866 | 2026-06-28 07:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| bac2d7ff-c90d-35ab-9138-68e554842304 | -12.1937 | -52.8866 | 2026-06-28 07:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5510ed5e-a33c-36ec-ab7a-adc28d33c605 | -12.18148 | -57.15102 | 2026-06-28 07:14:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c2594ac3-dac5-3bbb-b4bf-66986e929398 | -12.79388 | -54.88542 | 2026-06-28 07:14:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 471bd1ac-28a4-3a10-98e8-d3606af5520f | -12.19621 | -52.87413 | 2026-06-28 07:14:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 9052dc20-bc9c-3d9b-807d-863eff566640 | -11.9258 | -58.66943 | 2026-06-28 07:14:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78ac0e6d-8d16-31ed-9b8d-43220397bfc0 | -11.20693 | -54.30849 | 2026-06-28 07:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 437b6e5b-22a0-389b-9dc4-9ce32485473d | -12.45847 | -58.4996 | 2026-06-28 07:14:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4bfeda15-48ff-35bc-82e2-9d01be7e9054 | -11.52931 | -54.79272 | 2026-06-28 07:14:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 20aff507-3257-3e24-b205-886f29fd4995 | -12.19832 | -52.85802 | 2026-06-28 07:14:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 7ff9dc6a-a668-3a3a-b212-d38d320884c6 | -12.20775 | -52.87569 | 2026-06-28 07:14:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 5ba6e236-a485-350e-9732-aac2b56e5349 | -12.23293 | -56.54963 | 2026-06-28 07:14:00 | AQUA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| da519394-f368-3683-a0e9-c3c01d95a9ba | -12.1826 | -52.8886 | 2026-06-28 07:14:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 246b6f09-89ea-376e-9770-85f66e463fdd | -12.62539 | -57.89199 | 2026-06-28 07:14:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3916a225-4830-3eab-bb89-511cdc6dd741 | -11.21881 | -54.29773 | 2026-06-28 07:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 40b9cb01-01e8-391f-8851-b3f4e9a78e56 | -11.52657 | -54.79817 | 2026-06-28 07:14:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 56faf25d-5cdb-3fa0-97d7-5d7b1d69a532 | -12.77238 | -59.00274 | 2026-06-28 07:14:00 | AQUA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f4c73382-86c6-3373-88d5-7b41634540dc | -11.90701 | -57.12909 | 2026-06-28 07:14:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f1418007-9c27-37a1-be9f-9aa128d47101 | -11.21709 | -54.30994 | 2026-06-28 07:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6f102a06-9d9a-3896-a986-2cf33778df9c | -10.36013 | -50.17778 | 2026-06-28 07:14:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| acd3bbf9-7ace-3ef7-8c6a-4441521bc70c | -11.20864 | -54.29633 | 2026-06-28 07:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c728800f-d1e1-3071-8693-6d1ccd80be22 | -12.19203 | -52.90614 | 2026-06-28 07:14:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0dfa26bc-0f4a-31a0-abe4-7ccdd5e675e6 | -12.45242 | -58.48035 | 2026-06-28 07:14:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9887d6b8-55a5-30d7-839e-c5648a14dffd | -11.914 | -57.40421 | 2026-06-28 07:14:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f0924502-507d-382a-96bc-6a614fb68c37 | -12.08759 | -52.00379 | 2026-06-28 07:14:00 | AQUA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 45d5228e-f749-3f3e-8a16-da7049ae3841 | -12.16643 | -57.13007 | 2026-06-28 07:14:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3ff35e9f-32c2-35f6-881c-00f23d469f89 | -11.65834 | -57.25546 | 2026-06-28 07:14:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| abd3f5d1-e9b7-3c4f-b753-32a4d4de4790 | -12.45106 | -58.48929 | 2026-06-28 07:14:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9b8c1c16-0417-3eb0-9698-d85471e70bef | -11.66716 | -57.25679 | 2026-06-28 07:14:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5d58c5b0-d16c-3368-adfd-441cce247438 | -12.6004 | -57.87902 | 2026-06-28 07:14:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ee6ec88a-2eb3-3179-ad24-65b1f71f707c | -12.44365 | -58.479 | 2026-06-28 07:14:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 15d594c5-ff0b-3024-81b5-005467eaca4e | -11.21057 | -53.82034 | 2026-06-28 07:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| b6a9adbc-6149-3982-a2ef-bbfd99cca095 | -11.2211 | -53.82187 | 2026-06-28 07:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 8bffe7f7-d3db-39da-8950-471b1657601f | -11.90837 | -57.11996 | 2026-06-28 07:14:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bac6e09d-c05e-36d3-8267-ad7c343531d9 | -12.20987 | -52.85956 | 2026-06-28 07:14:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7696c8f8-585d-306a-bea7-b82e43f903a3 | -12.59906 | -57.88796 | 2026-06-28 07:14:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1cc7d835-e7d5-3cc9-a133-8f86334288aa | -12.45983 | -58.49065 | 2026-06-28 07:14:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 5c40efa9-116f-3aa9-a10f-1e0f9637f753 | -11.52821 | -54.78669 | 2026-06-28 07:14:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 802531cb-910a-379d-94d2-e169beefde25 | -12.18052 | -52.90461 | 2026-06-28 07:14:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 53a92bec-c5d7-300a-b714-1bb783a94cb5 | -11.92718 | -58.66045 | 2026-06-28 07:14:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 34938020-884a-32f4-8635-0eb2f29f5233 | -18.47797 | -54.0957 | 2026-06-28 07:16:00 | AQUA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 23.5 |
| bdbebbdc-471a-3341-8175-40bead6f0c1b | -12.1937 | -52.8866 | 2026-06-28 07:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3e22c417-300b-3356-bfb7-8015831b63cd | -17.3643 | -42.6284 | 2026-06-28 07:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 40cad76f-abfd-32cb-bbfe-15327cbb78e6 | -17.3442 | -42.6333 | 2026-06-28 07:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 8fb632d2-b2f3-3225-8d36-415c5f2e2632 | -17.3442 | -42.6333 | 2026-06-28 07:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 4bc91d9c-525b-3dd9-afbf-a62bbb97ef19 | -17.3643 | -42.6284 | 2026-06-28 07:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 46.3 |
| c4138825-29bd-3225-a6c7-f25878566e98 | -17.3442 | -42.6333 | 2026-06-28 07:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 929ac11f-f48a-391c-8c23-90ebf17c06b6 | -17.3643 | -42.6284 | 2026-06-28 07:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 053c594b-f4f5-3076-845e-b636a3235a47 | -12.1937 | -52.8866 | 2026-06-28 07:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| eaf95b0a-4b74-3c17-b566-a3d4012c1916 | -8.3088 | -48.2514 | 2026-06-28 10:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 5d7e8a49-5c90-3272-8cf0-8de57ed28948 | -8.3088 | -48.2514 | 2026-06-28 10:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 5bbd54a5-6db0-391e-8903-bc6666dc71fa | -8.3085 | -48.2731 | 2026-06-28 10:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 5a8b6aeb-7a29-3df4-9091-9bc891840ea0 | -8.3088 | -48.2514 | 2026-06-28 10:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 156.0 |
| bdd6b0b1-6a96-3f4f-8b68-2967d846b4c6 | -12.19658 | -52.89861 | 2026-06-28 11:30:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 5ae5b391-d40a-308f-b375-3728180c5850 | -6.98658 | -42.89246 | 2026-06-28 11:30:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 266e7ba4-be80-3aa7-aa85-8ca7802826a9 | -12.6964 | -45.47156 | 2026-06-28 11:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 81890e7f-ffb0-3c4e-a391-9fcd8731328f | -15.34104 | -43.77627 | 2026-06-28 11:30:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 578c4a7f-3a88-366a-ba3d-688036ba74ca | -8.29967 | -48.26619 | 2026-06-28 11:30:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 140a93af-c99f-3e97-bd79-1c196945dcec | -8.31643 | -48.24689 | 2026-06-28 11:30:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 204.8 |
| da9dc645-9309-365a-94ba-32e9df66afc5 | -8.30413 | -48.25998 | 2026-06-28 11:30:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 98ea586a-364c-3d40-88bf-b8932109a9aa | -12.19622 | -52.89302 | 2026-06-28 11:30:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 4f8e6b7b-1a0f-3c4d-bf9a-bf97b9ebbeb3 | -6.9774 | -42.89113 | 2026-06-28 11:30:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| a68097e1-e17a-38fd-b593-d91b4eed88c2 | -8.95531 | -45.6617 | 2026-06-28 11:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| fd09ce19-e3ce-33b2-b74e-816c447793aa | -8.95735 | -45.6483 | 2026-06-28 11:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| aa8de1ba-b827-37d2-a66c-5a4fc484f628 | -9.80804 | -40.59525 | 2026-06-28 11:30:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 206f7193-e6e1-3d47-a66b-bc6c6bb7ce2d | -8.31296 | -48.26822 | 2026-06-28 11:30:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 42b7a0c2-12df-317c-a996-a09d81f28017 | -8.3032 | -48.2446 | 2026-06-28 11:30:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d2760a2b-6c3e-37e5-ade1-5fdbac5f29ce | -12.26867 | -43.51372 | 2026-06-28 11:30:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f888b96-cb55-3bc0-811e-8a77a8890e6e | -21.24696 | -45.72603 | 2026-06-28 11:32:00 | TERRA_M-M | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 787ae7dd-a79b-360e-a6cb-4be75935a246 | -17.70715 | -46.77946 | 2026-06-28 11:32:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dbb5930a-2f89-3d28-9df8-d47cb282fa53 | -10.3443 | -46.9142 | 2026-06-28 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |


[Clique aqui para ver as próximas entradas](README26.md)
