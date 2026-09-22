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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3e1db43-0464-3ea6-8fed-a59484f8e65a | -6.7138 | -58.996101 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3335b1fc-7c87-3866-b4d9-56890dfe06a2 | -6.1977 | -57.7845 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a197eb6-b38c-3cf2-877b-733ee079973b | -3.7163 | -60.587299 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 011a0b31-878c-392c-b354-a9c3ecd8370a | -5.8057 | -57.740299 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be642022-787b-3898-8a1b-a06d14d10938 | -7.5663 | -57.678501 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc132d72-22b7-3338-93ab-0d9c389f30ba | -6.0409 | -53.278599 | 2026-09-22 01:19:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef1767b0-668f-360e-ae22-12383aeceab0 | -8.8273 | -50.487999 | 2026-09-22 01:19:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19126203-4bbb-32cb-ad5f-071a98f0d837 | -6.5224 | -55.3787 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cd5c3a2-5460-3799-bbd6-93e3465d1bfd | -6.1379 | -59.952 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79984ab2-32fb-395b-826f-266e8158d69c | -6.7491 | -59.4216 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04ac5c66-1bf0-3a72-b236-255fca806395 | -4.5182 | -55.762798 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8899600b-e1be-33c1-8319-f8df050bd64c | -12.1389 | -47.3965 | 2026-09-22 01:19:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b36c37a5-da53-3a68-a387-2ca9ff1e5cb0 | -7.6113 | -55.3559 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbf9801f-a853-3ec0-96cd-e9e5494e7eb8 | -6.4394 | -55.6394 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 862fceb1-786a-346f-9e42-d6f97a877f08 | -12.7943 | -54.035599 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40671f05-4915-340e-a2f2-911c64e7daea | -6.0425 | -57.827301 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3b6e982-bf55-3bea-8af5-2e36e7435376 | -3.4016 | -59.259998 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fc8a45d-5181-33d0-992c-b8385a8115f5 | -10.5999 | -53.984001 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb3048c3-c9bf-3fb5-864e-9918cc581a31 | -6.1281 | -59.954201 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c759f649-b2e1-3232-87c9-82ca487ff8d8 | 0.7903 | -59.197399 | 2026-09-22 01:19:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c3be8935-2b89-3716-8dec-d190d50a724a | -6.4316 | -59.974602 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d937c7f5-3d1c-3196-a295-2048e82d631b | -4.2843 | -56.260399 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcb5c9b2-19f5-3a5c-91f5-a731139fe9d3 | -2.8622 | -60.909901 | 2026-09-22 01:19:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9afb910b-144a-39db-821c-26f08c37045e | -2.8771 | -57.792599 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 409e8fcd-daae-301b-9f0a-1780ad20dbfd | -3.2351 | -53.951199 | 2026-09-22 01:19:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a09f9418-c141-39dc-a15c-04b7957d14da | -6.3657 | -58.2883 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32d58e29-a91e-3894-aaae-64e6401142d4 | -6.0719 | -57.865002 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8ac306-b48c-3996-af93-df72cf5b017c | -3.0854 | -61.1647 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f56a6524-ee47-3c22-a0a7-f5875b4f1a64 | -9.5507 | -66.025597 | 2026-09-22 01:19:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3c80ad2-c461-3025-981c-e0f38a0aa334 | -6.1297 | -59.961102 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33362be8-4dae-3a15-bcf9-c778c5a6c12f | -10.4774 | -51.301701 | 2026-09-22 01:19:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47bed889-f0bf-37f9-920f-5f30d78132b3 | -4.3084 | -49.139 | 2026-09-22 01:19:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aecfd04c-987f-3d97-9b91-edec5a0867ea | -6.2996 | -59.937801 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47bb5e26-1ff0-3f6d-a6b1-ffa539812708 | -3.0673 | -61.266499 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd0d62c2-323c-3b1f-97a3-a4408e961c38 | -7.6991 | -61.540298 | 2026-09-22 01:19:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aebc1394-89c2-3f0b-8add-3c782057c359 | -2.4198 | -58.268398 | 2026-09-22 01:19:00 | METOP-C | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c06ec3a6-abb4-3acc-924d-e22a45df2d23 | -2.5644 | -57.511799 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92e52027-ea8f-39ed-8321-7539973edd64 | -11.3279 | -54.044601 | 2026-09-22 01:19:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8000a3dd-3277-384d-b4af-39367432a4e5 | -3.0543 | -54.405998 | 2026-09-22 01:19:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e028fc8e-c50a-3889-85ac-9945544161f7 | -3.3618 | -61.291801 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fdc83a6-e608-38f9-910e-c08e2318a7f9 | -7.7236 | -61.2341 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4733ed6-bf04-3322-9219-6f562b26b68d | -6.4658 | -59.988998 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| caa302f9-4d23-33b3-b1f3-bcf050c03197 | -6.0915 | -57.637798 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0262e831-42e3-390a-9e23-f372bd7e67d3 | -5.9413 | -57.7019 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5737e293-ace8-3320-b4f3-c00fb1e1d680 | -12.9158 | -53.895699 | 2026-09-22 01:19:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 163dc48b-f954-3767-a1a9-8332b2082947 | -3.0119 | -54.182999 | 2026-09-22 01:19:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 379b80fa-fc2b-340f-9e17-afc5edf3cc5d | -6.1266 | -59.947201 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51dc6c03-f2c4-3618-bde5-b0a0db5a7b75 | -8.2669 | -55.289501 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b95c5f19-2b4e-35b0-9517-ba8f25d9045f | 0.7821 | -59.188202 | 2026-09-22 01:19:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0691fbe4-a12a-3e67-b800-a893c2604df8 | -6.461 | -59.967999 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4dedb7eb-d3e7-3a3f-9beb-40d873056e3c | -13.2946 | -51.769299 | 2026-09-22 01:19:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ee5752e-9c59-37e5-8a29-1795f010dc05 | -3.9025 | -60.589901 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28830dfa-f2a1-3af1-94ba-f86a4cba9328 | -9.1317 | -58.885399 | 2026-09-22 01:19:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 766327d3-daf8-3a5a-88be-28ca35c746e5 | -12.8117 | -54.022202 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5be39f2f-3f7e-39c6-8d85-7e84900ba99f | -3.7534 | -58.324501 | 2026-09-22 01:19:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d7ee5d56-a22b-301d-bddf-4cc0d92f80d2 | -10.5901 | -53.986401 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c67f2b3-6dc0-3927-bd96-acf67488c732 | -9.8892 | -48.480598 | 2026-09-22 01:19:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23c94ae7-1fbf-3a31-b829-410ee5088021 | -1.2981 | -54.199902 | 2026-09-22 01:19:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a5af53d-a3d9-30be-a0e9-f979390a2972 | -12.9327 | -51.030102 | 2026-09-22 01:19:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8886ec2f-e82f-3307-947c-7ff3155d5095 | -3.4866 | -59.584801 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff6b506-194f-30f7-a67f-61312bf8017c | -5.8155 | -57.737999 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 991c0002-611b-3b9b-9e6b-988372c25895 | -6.0703 | -57.724602 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80bcda8d-0e6f-3a88-98c0-fe981240219b | -3.1965 | -60.433399 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4899683-a78c-34ca-9fce-6975697a2231 | -6.3905 | -60.020599 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10937561-2cd0-303c-83cf-370866f97289 | -3.9242 | -56.044102 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 226ab7fd-2135-3120-aec8-52de06334a49 | 1.5338 | -55.909698 | 2026-09-22 01:19:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d239f3-5abc-3e7b-b0cf-3c175d0dfdb0 | -3.6512 | -58.865398 | 2026-09-22 01:19:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab51d54c-6f27-308c-9f8e-8cc79a732c6c | 0.7789 | -59.202301 | 2026-09-22 01:19:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| abc5e0cb-31ae-316e-bebc-e01102d82185 | -4.8795 | -55.895401 | 2026-09-22 01:19:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3ea4960-1e72-3643-a844-167dd114c188 | -6.6148 | -59.9189 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c7494c5-43f7-31b6-992c-f276035f9864 | -6.2942 | -57.755199 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 203fff15-37c9-3f6b-a06f-0113a1379495 | -6.1395 | -59.9589 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d57536b4-3be3-3c92-a356-934fe82b55a9 | -6.7424 | -59.076199 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 866c7570-b3c7-3a93-9b7b-de1908e73189 | -4.3463 | -55.646099 | 2026-09-22 01:19:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e7e9552-53ee-3021-bde5-1428fcca679b | -7.2882 | -59.526299 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 832157bb-50bd-3407-af4c-1ba2cb9bf336 | -6.9187 | -59.6236 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d85b5cea-8354-3963-b05a-336be32f2692 | -6.7486 | -59.465199 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 738faaf7-37ae-3263-b727-bcd79e621369 | -6.3462 | -57.8909 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6785a353-9690-38c1-8ec5-1a151ae7343d | -4.2127 | -59.9175 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99c1f71a-d237-3134-baf0-3a8912f2c6a9 | -8.1085 | -55.3619 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e101da2f-aa88-340e-a351-efc578e9e74e | -6.3012 | -59.944801 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 381f7f01-3135-36fe-818f-292d3f7b33ca | -3.3437 | -59.8605 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2df86309-f22c-3f22-82de-8e67d5dbe57b | -7.5876 | -57.681 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afcdecb9-3f59-3f34-aef7-2be5efc46e67 | -9.8801 | -55.7341 | 2026-09-22 01:19:00 | METOP-C | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee4f5e4f-35e7-311e-acd7-9eaec0b2da2f | -6.4674 | -59.995998 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c924803a-8c97-33fb-b2a1-80f0974fb689 | -9.6734 | -54.342999 | 2026-09-22 01:19:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 283fe2cc-04c0-3afa-9949-79633faef8ec | -10.474 | -51.2883 | 2026-09-22 01:19:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f5184a7-967c-35e8-8096-da745f264c25 | -12.1442 | -61.1717 | 2026-09-22 01:19:00 | METOP-C | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ed880ad8-c015-3ae5-a766-36576ca7a7af | -9.0988 | -65.3685 | 2026-09-22 01:19:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5da28caa-d463-348c-83cc-7ec3240efb65 | -3.1526 | -60.646999 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48942f47-c562-371f-a3d8-675ae27a74b4 | -6.0931 | -57.644901 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7cd9cfa-2cf7-3d54-980d-cae72904b42d | -8.841 | -50.501598 | 2026-09-22 01:19:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 588c1790-e56e-3e77-8651-9c97917e24e4 | -8.6073 | -54.6367 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f6b401b-8633-3d1d-b152-b077c368f4b3 | -3.9009 | -60.582901 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9223c390-6e71-3a0a-ba31-c197c19a2f28 | -7.3376 | -55.595402 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bec40cd-4354-38ae-accf-ce2e6e523a8c | 0.7887 | -59.204399 | 2026-09-22 01:19:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e08b2ca6-cddf-35ec-83d2-69c231f46af7 | -2.41 | -58.270599 | 2026-09-22 01:19:00 | METOP-C | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1b5191-1885-3ac6-9303-6745eedb31bb | -8.6366 | -54.6297 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a50a040d-6490-3df9-84dd-f913ea70b2fe | -6.2639 | -55.421001 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d25aa2c4-46c0-374e-ae28-14373de4414b | -2.9516 | -57.713902 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README21.md)
