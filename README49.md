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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9819db88-f4ee-3bcf-afda-b19f35387c8b | -8.7231 | -45.1583 | 2026-10-09 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 187.9 |
| dea66e01-f8bc-3872-920c-0dc1c4393199 | -2.499 | -56.0675 | 2026-10-09 01:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| da4c6ec4-4926-3e4e-8f2a-9baae2f82cf7 | -8.742 | -45.1563 | 2026-10-09 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 288.4 |
| 82c334ce-b217-3e25-9461-51b0bd152fa4 | -6.8719 | -45.9003 | 2026-10-09 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 4436706a-2f29-336a-850a-9e594aae16d7 | -12.2156 | -57.1087 | 2026-10-09 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| cf7077c0-9231-32c3-a300-e1a26edc7427 | -13.1827 | -54.3571 | 2026-10-09 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 4a216b23-cbf4-37f7-9519-0b3c0cd68562 | -7.5649 | -61.5523 | 2026-10-09 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5fa7d7b2-4732-3ca2-bf54-badb1397629b | -12.2158 | -57.0887 | 2026-10-09 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e3f50b6f-5a13-3cca-ae56-57338b002714 | -3.0925 | -53.9455 | 2026-10-09 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 2bab4820-52b7-3c63-99e6-a6e09c898000 | -3.364 | -50.4072 | 2026-10-09 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 015d7e3f-f0c0-3adf-98c3-d7565ecd49ee | -3.1971 | -50.5801 | 2026-10-09 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6c0bd099-4754-3f15-8632-44df2e244c48 | -6.8907 | -45.8988 | 2026-10-09 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 68cbff36-391f-3f97-9547-84f3f249fd6d | -3.5676 | -54.6946 | 2026-10-09 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| c8cce3cb-5d7c-35e0-b634-95625dd7434f | -5.6934 | -53.4667 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 45f63c1b-9c5f-3f15-8508-5d487632f5c7 | -6.021 | -40.9577 | 2026-10-09 01:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| eaa7a6e6-0241-3de1-942e-9098f4b9f9cf | -5.7117 | -53.4862 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 83ca7cbe-5acf-361c-8f88-5b0c15f99ae0 | -3.11 | -54.1862 | 2026-10-09 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b34bc032-a876-3e06-b959-a5b678f08aab | -7.2367 | -55.1406 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c6948495-ae72-30ec-a55a-44ac4846c5c9 | -4.6282 | -49.2147 | 2026-10-09 01:40:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 7e40c166-ba82-3e3c-bf6b-4c695dc6927c | -3.1879 | -58.6433 | 2026-10-09 01:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3a158bc6-a0cd-3ab3-9431-fc59fb9286a5 | -7.2179 | -55.1817 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| dc6ea4b4-92ca-35a8-8ee4-e5592854054a | -12.2535 | -57.1055 | 2026-10-09 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 4865fb23-e296-3544-888b-ccc108847380 | -6.0024 | -40.935 | 2026-10-09 01:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| f41d026c-2c5b-326e-a44a-8aefc9bbe90b | -3.5493 | -54.6752 | 2026-10-09 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 70e02e65-1d60-319a-ac7f-a5492736ba64 | -6.7365 | -55.1474 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ef5fbf93-f289-3f77-bd42-e83cf8eecd5e | -6.1402 | -53.0574 | 2026-10-09 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 8bca3797-d17d-34c5-b13b-51891828dc08 | -1.1094 | -54.1802 | 2026-10-09 01:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 43fba317-2ca2-3585-8998-a3768ca9c568 | -3.5493 | -54.6951 | 2026-10-09 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| f581759f-514e-3e03-9ef8-3c201e82a65d | -3.1114 | -53.7839 | 2026-10-09 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| e8e4030e-b495-3de7-bf26-778182117691 | -10.9953 | -45.4068 | 2026-10-09 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| dbfcf2ce-862f-3287-a2d4-a2247a957e9b | -5.9587 | -55.3448 | 2026-10-09 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ff4af871-1942-310b-9cd2-bce958ffadb1 | -3.4396 | -54.5382 | 2026-10-09 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 896fc60e-3a3e-333b-8865-45ee8fbe4968 | -7.1994 | -55.1827 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 341b7e2d-ced8-386f-b4d2-8f9c9f87a48c | -7.2182 | -55.1416 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 17a875a1-3b21-3e51-8016-8394da91bc7d | -5.6932 | -53.487 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 3a2cc2c8-490a-3faa-ae86-c1e03e4ac278 | -3.1284 | -54.1857 | 2026-10-09 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 38e3182a-c25c-33a3-a35f-0c7b9a5fc6a7 | -12.0058 | -43.464 | 2026-10-09 01:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| c33b1cc0-b2bf-3a47-beb9-897265597158 | -3.9912 | -59.356 | 2026-10-09 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 93604f23-d329-366d-9662-e6531f032278 | -8.7612 | -45.1314 | 2026-10-09 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 2dee4914-d0e7-3f3a-8873-703d6d5a5335 | -3.0007 | -53.9075 | 2026-10-09 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 076bd7ff-c364-3cfd-abc5-0cd7f59ea223 | -12.2346 | -57.1071 | 2026-10-09 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 1834d47e-b8b1-35f6-a393-cfb4d1f80357 | -13.1668 | -43.2673 | 2026-10-09 01:40:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 67fd61f2-324d-3d26-8c91-95ec7234fadf | -8.7234 | -45.1355 | 2026-10-09 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 119b9aab-5cc2-3b46-a291-583855a67490 | -12.2154 | -57.1287 | 2026-10-09 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 02035a39-ffd0-3471-9031-287ea259e6c9 | -13.1663 | -43.2913 | 2026-10-09 01:40:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 22b68f1f-abd6-3850-bd6d-6a6c0d5e2f1a | -3.1101 | -54.1661 | 2026-10-09 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 769f35f0-2390-3f3d-b904-9c22533a14de | -13.1639 | -54.3385 | 2026-10-09 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 3bf451d0-a35c-3b80-ab0d-b311f27ba949 | -7.218 | -55.1617 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 592205ce-178c-3e00-ba45-ff9cc300fa7d | -3.1787 | -50.5807 | 2026-10-09 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| e8c0e7fa-09ad-3ad0-967b-e258600468f4 | -11.014 | -45.4272 | 2026-10-09 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9b572e3b-4dc9-3a05-b919-c036b1a6d7f0 | -9.7054 | -58.0854 | 2026-10-09 01:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 53c56e82-673d-32c6-9670-d668e136496c | -13.1636 | -54.3591 | 2026-10-09 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b3be1b28-9280-3764-918b-2801e26bd32e | -7.1995 | -55.1627 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 161.5 |
| d5668d49-1968-398b-b83f-a64f19b07eb9 | -6.0019 | -40.9837 | 2026-10-09 01:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 231.7 |
| 87c94862-d877-3d3e-b396-179978c5e68a | -6.0021 | -40.9594 | 2026-10-09 01:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 364.6 |
| 6e9853f6-a096-376f-ab8a-9256155a0c01 | -11.6173 | -43.7142 | 2026-10-09 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 8d77fcef-15ec-392d-a28f-0f6b12d194f7 | -3.3455 | -50.4078 | 2026-10-09 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 25c487af-83d5-38f6-a14a-0f3fe6672cb0 | -6.4903 | -62.8554 | 2026-10-09 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| b9211e7b-cd61-3770-9510-9944684cbd45 | 2.4216 | -50.8307 | 2026-10-09 01:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 2e5e8f67-f8b9-3dad-ad11-f12a06e8567b | -3.0002 | -54.0684 | 2026-10-09 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e2f1fa9e-e351-3306-b452-c96c82f39f0e | -11.47 | -43.3824 | 2026-10-09 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 46805198-59be-38a8-806e-b886a49bdbf2 | -5.7119 | -53.4658 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bf4f0b7a-765b-32f3-9f8a-c87d7ff08ddc | -13.2018 | -54.3551 | 2026-10-09 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| a78a9b3f-fdcb-3356-a691-fc4ce09ddd6a | -6.0207 | -40.982 | 2026-10-09 01:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 0059ee30-656b-3419-8093-14f0aa56f70b | -3.1285 | -54.1657 | 2026-10-09 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 142.9 |
| f24f29c9-b2f5-3f46-91e8-bf116596b528 | -7.2187 | -55.0815 | 2026-10-09 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a902f308-aabd-3291-a3be-56210817e12d | -12.2348 | -57.0871 | 2026-10-09 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| dfa9a07e-47b5-3c56-8947-77dcb54d6b23 | -8.7423 | -45.1334 | 2026-10-09 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 493.3 |
| f53e08bd-e745-3557-9177-86dba4646763 | -3.1109 | -53.945 | 2026-10-09 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| da97282b-b743-3adc-8ff4-d57e5eb5170a | -11.7603 | -61.0549 | 2026-10-09 01:40:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6dcbe066-7676-3cd4-b307-08ffc123a597 | -3.5677 | -54.6746 | 2026-10-09 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 5ab71c55-c5d3-3cd0-a108-15109c7edd03 | -8.7423 | -45.1334 | 2026-10-09 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 447.7 |
| 9ed64d1a-67eb-353d-a9d6-60d3bf4b77cd | -6.0207 | -40.982 | 2026-10-09 01:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 220.7 |
| 2efc3854-dc75-303a-83d6-0f77fb2d65a8 | -8.7234 | -45.1355 | 2026-10-09 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 0d28b617-0b13-3203-9734-41c252b2f8ed | -3.1109 | -53.945 | 2026-10-09 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 194f0a6c-412d-307b-a4a8-055b03acb541 | -6.0024 | -40.935 | 2026-10-09 01:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 205.1 |
| d3aec2b0-ccb7-3415-ac2f-8499143f46c2 | -8.7231 | -45.1583 | 2026-10-09 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 84468267-6a2b-34dc-9845-d997a184c293 | -7.218 | -55.1617 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 2380fb30-e65e-324b-a54d-f60443bb54a1 | -5.7117 | -53.4862 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| cf278112-07aa-304c-93ab-53317d1c9064 | -3.5493 | -54.6752 | 2026-10-09 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 22faf4f3-c25c-3b7f-a4d2-e2e5d491db44 | -3.1114 | -53.7839 | 2026-10-09 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 41388aa8-78b2-3011-9101-a4be8ef40b95 | -3.9912 | -59.356 | 2026-10-09 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| f77d22ee-7cd6-3111-99c6-be2a37408b65 | -13.1663 | -43.2913 | 2026-10-09 01:50:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 68.5 |
| fe418a77-654a-3f6f-a9aa-d8c79555d6b7 | -6.7365 | -55.1474 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 565a619e-88d3-3c65-8fd4-5846acaa1bea | -1.1094 | -54.1802 | 2026-10-09 01:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e7bcb379-eb18-3d5b-90fd-0ed3d0b05d03 | -7.4442 | -63.5589 | 2026-10-09 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| a69a91a5-d0a7-32a6-8095-b733af76aab3 | -11.6562 | -43.6846 | 2026-10-09 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 0a5031a6-3a5a-3e22-bb32-c721f83ee38f | -3.1285 | -54.1657 | 2026-10-09 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 22221339-160e-360c-a890-beb7a8b29291 | -7.5649 | -61.5523 | 2026-10-09 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 593e68c0-a137-396b-b606-eed564c98e93 | -3.11 | -54.1862 | 2026-10-09 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1bebf375-6b01-399b-a875-d5ace5d6f1a6 | -7.2187 | -55.0815 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a917abb2-8135-3836-95b5-fdf308235976 | -2.7428 | -54.1146 | 2026-10-09 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 13a751f2-df45-3278-82a6-773167a3a862 | -3.1101 | -54.1661 | 2026-10-09 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 1b6b8a54-ec94-3fb7-811a-196d1142cc89 | -3.5677 | -54.6746 | 2026-10-09 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| bd5a5cd7-a210-35c6-bb61-29057751de9e | -3.5676 | -54.6946 | 2026-10-09 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 56ee3b0f-bd81-36dc-a418-283d3790a464 | -3.1284 | -54.1857 | 2026-10-09 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 2ebe29a4-586e-3b57-9dc8-5d0a9555b701 | -3.0007 | -53.9075 | 2026-10-09 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 2156dcb6-11d8-3aad-b92e-490416f6b320 | -5.9833 | -40.961 | 2026-10-09 01:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| c434f41c-37a9-3bf3-96ff-6a9396fcb2bd | -5.6934 | -53.4667 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 12c59654-5297-3d5a-be7e-388308c6210d | -4.6282 | -49.2147 | 2026-10-09 01:50:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |


[Clique aqui para ver as próximas entradas](README50.md)
