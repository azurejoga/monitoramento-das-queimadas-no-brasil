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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c302cf1e-1f06-3cec-859d-2f3a6787a59c | -6.25494 | -55.44363 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f535481-f8e5-3590-b962-63315411649c | -9.55601 | -66.04077 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fa1baad-8653-3185-aac8-bd6012ffdca4 | -5.87431 | -51.58487 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71d7ab41-75bb-38b3-bcf5-f2619b2ac556 | -6.44331 | -59.97136 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 406cef85-9d49-36e3-b653-d7ee1eaf3b06 | -11.03827 | -57.23535 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76b80e7d-14a0-34a1-9c42-a3aa98039935 | -10.66759 | -58.83358 | 2026-09-21 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 882bf2b8-70fd-3f5a-b3fd-02d427bfcc3d | -7.55874 | -61.33075 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb0f2a31-432f-37c5-8175-874fdc2a3ded | -8.17156 | -54.76469 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a356daf-4446-3ca3-a2ad-b79c50704df8 | -11.13476 | -54.00853 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 820ccf29-1955-3722-ab9c-31d75bfc16b0 | -5.22086 | -56.10319 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1035e85-7487-31c3-b802-4caa1861f105 | -9.70876 | -65.09204 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e175228e-38b5-3117-b6ad-8b5ea9b21557 | -9.40794 | -65.92101 | 2026-09-21 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98686838-b68c-3f4c-8ab3-93ebcb58735a | -9.55074 | -66.0052 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f10361f4-c636-3241-87e2-48dcb0fdce5b | -6.7212 | -55.07993 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00b03165-827e-31e0-9b57-caaa32b668f0 | -8.17976 | -54.77687 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c802237-2e9f-330c-b108-aeaaafca1698 | -11.1009 | -54.01734 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ea1896c-b31f-3407-8e47-b729baa76a93 | -10.90461 | -53.97543 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0fe7264-d8cc-3fb9-b882-3b82f7d34081 | -6.29219 | -59.91842 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2501163-854f-332f-81b6-070b401e47f3 | -7.24654 | -55.58754 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d36a5d9-b974-36cb-b8ea-11ea245a07e3 | -10.42168 | -50.24306 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e748aff8-cfe0-3877-a7e6-9898738c4536 | -5.76875 | -57.59248 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fedccf09-cd0c-3096-b286-c002a1b2bec4 | -11.03224 | -54.14059 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3df4c9e2-0fb6-37cd-be51-052ee38bf0f4 | -10.8029 | -50.83672 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6036eb93-4067-3e8b-8269-bcbe3f7fd35b | -10.89883 | -53.97794 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc0d24c6-e886-3132-9daf-8178a0b6cdb4 | -9.28072 | -68.36575 | 2026-09-21 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8189cf2-93d2-3014-a3e8-feb1d7ebb228 | -5.84399 | -53.53598 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bfaa678-9b64-3d44-8cef-8edc578f6fca | -6.15065 | -57.84101 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7623f8fa-985b-3f61-ad9a-911c641e2477 | -6.43926 | -59.97459 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 462ecad2-5a9b-3db8-b62e-f49af2a4f482 | -6.08634 | -55.54436 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5550c105-a8bb-3ff4-b813-e11536526680 | -8.65589 | -62.48394 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e78bf554-0e66-3ca9-a777-b600b29b84a6 | -8.609 | -54.62454 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f94333c-1a1b-3f06-816d-e11223ad2d45 | -6.68165 | -59.11007 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f020b061-c5e4-302c-b262-70163d9b5068 | -9.56186 | -66.05047 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11466dd7-e72f-3fe1-8ea9-1f52a84c3af0 | -6.65229 | -59.96447 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b62021aa-684d-31e6-8be3-0d66dff9b523 | -5.81717 | -55.69885 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c694ea72-d7b6-36a8-8bfd-54d6db0ce64e | -10.42096 | -50.24904 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca96e56a-4a06-3286-81dc-cc991ccddebb | -9.55671 | -66.03656 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67c6142d-7ffc-37b2-8d98-04a824e99f5c | -10.88856 | -53.9731 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a410976d-4004-3436-bd2a-490dac8daea9 | -6.31041 | -60.00681 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 936e2629-060b-3b3e-b09a-6825b6eb09e8 | -6.78321 | -58.90604 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2edfc06a-ecb2-3a5b-a195-1d9cb88229a6 | -7.60903 | -57.61377 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4bee257-b478-3193-bc27-17d92f4ff2a9 | -6.20752 | -53.56329 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 955d75a7-e67e-3e9a-8e90-ef5706c9dbd7 | -5.85088 | -53.52461 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 776e6f9d-3482-3f7a-b1e8-3899bd68b31e | -10.74216 | -50.78975 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 696839ba-70c2-3fa4-8b32-1c96c6716f6e | -7.5967 | -57.6696 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f2c740a0-ae2a-3971-867b-1c46c53222a4 | -6.29899 | -59.96622 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd73f3e3-99e9-365d-8701-e2a2740a7ccb | -7.57608 | -57.67175 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9cc582a8-82cd-300b-a316-48b895161e31 | -5.76096 | -57.59134 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ece515ca-8dd5-35cf-9594-65b4f2cffaa6 | -7.25564 | -55.58882 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4761dee4-5899-392f-beb7-3d7a1b3a76e0 | -6.72516 | -55.08573 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0f1a412-110d-3c96-b8de-f43f1a81b142 | -6.73497 | -55.0708 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1e70a59-8803-38f7-9d16-ae0d61b18951 | -5.93421 | -59.95442 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbbab348-4ff8-39e1-a778-f3de0bad02f9 | -11.01718 | -54.13198 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 747bfb41-6f51-3e33-b2f4-da3f3efd0cc8 | -11.03047 | -54.15384 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31c8bef4-b9b5-30fc-9663-a3c5600829ab | -5.84619 | -53.52083 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e4767b0-e235-351b-a16d-b9d39071570e | -6.77483 | -55.49237 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50808b02-7d02-389c-9b49-9cd7823cc846 | -7.68937 | -61.54014 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9ceece6-b790-3628-8a24-63d2dfeb55f5 | -6.29611 | -59.96189 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df92df8a-1eb5-376c-92a4-7492c2cd47b2 | -5.83931 | -53.53217 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa7aab0a-eff3-370b-a4c4-d9b4d7a72262 | -11.03171 | -57.23698 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe411109-746a-3d47-82ed-a56793e12e02 | -10.85308 | -50.15636 | 2026-09-21 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba697d1c-45c2-3ca4-91fb-b865fd37bbf0 | -10.75459 | -50.79696 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c868408a-a991-33f6-a4cd-2ded9ceedb31 | -6.46356 | -59.97836 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 544afca0-6ecc-3b16-8750-c62b7115d6b7 | -11.05064 | -54.15606 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5adc15b-7861-3246-8f7d-adc173bb92d0 | -10.48226 | -50.27438 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5bcce668-591f-342c-b9c8-fefc4b249096 | -11.25391 | -54.14404 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 920cb6ed-26f9-3845-ace7-38f198fe0e15 | -6.2916 | -59.92223 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06d5d618-e2da-362b-adfb-f05036df48da | -6.21897 | -53.57121 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0d086f8-5bc9-38ed-8c07-e71cf2a8b0e9 | -5.21602 | -56.10654 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e66bfd5-a3b9-330a-8ca3-93210b43710c | -5.83887 | -53.53521 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb10bfd9-beae-339f-90fa-7647eb04e89c | -6.25628 | -55.43467 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed8936a4-3a30-368b-86f2-1dacad892d3d | -6.45025 | -59.97243 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40c71171-7e8f-3906-b45b-462c0f74551a | -8.15748 | -54.82824 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1233cc25-53ec-3cb4-b9a7-d58be978be49 | -10.3165 | -50.55552 | 2026-09-21 05:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9745b221-aba5-315f-bfb0-124c831442d1 | -6.32624 | -59.95097 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ab751e3-b3c6-327e-bb72-95871bb4e1b2 | -6.77415 | -55.49697 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a61021ba-b032-386f-8c63-3079540aabc1 | -11.03136 | -54.14722 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d10ce4f3-e9fd-31a7-bd78-b89e431f1516 | -7.59348 | -57.66389 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 645bedbd-f88e-31ff-b98b-ee42dcedeebe | -9.56619 | -66.04686 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 511a49d7-b38f-3cad-8274-b9e05da278b7 | -10.91173 | -53.96261 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9b48d51-c346-39f0-affc-726d9d24493b | -7.58327 | -57.67806 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2213357a-0c41-3ced-9db5-6341f2a05e65 | -5.81666 | -53.50739 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b92347b-7504-316c-9bef-5b355f86201b | -10.45622 | -61.31381 | 2026-09-21 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f254805-d5ed-36ca-b7db-bebd8b72ba0c | -10.91886 | -53.94979 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8a6e970-fa14-3144-87c9-d2f7fb2bbab2 | -5.87397 | -53.633 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8863422c-ccab-32c4-903c-a1b53cae410a | -5.83428 | -53.49421 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68b22188-48b4-355d-bba0-10d479e42dca | -6.74288 | -59.41939 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4bb3840d-6e0e-3259-8b1d-ec364e9fbb27 | -6.7245 | -55.09045 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9afc57b6-5085-3f55-a0aa-15eb30b766e7 | -7.54977 | -61.32204 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6e5d1ce-08cc-3ac8-889d-be95f0d83a7f | -8.78992 | -64.14897 | 2026-09-21 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98e687a3-8974-308a-bfc3-37bd17fb9216 | -7.88878 | -62.54369 | 2026-09-21 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41e3e814-67dd-3021-91b1-ed7f07abd036 | -10.4665 | -61.31531 | 2026-09-21 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d32c0eee-2654-3063-bc17-d4e73dda35a1 | -6.30371 | -59.93583 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54fc7d3d-9cec-3606-a4a7-2086c602fa66 | -9.01945 | -49.82529 | 2026-09-21 05:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50e82c84-8939-33dd-9c70-f4a8a4b39fb6 | -9.55092 | -65.69479 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d62cc135-db6a-3851-83d5-286c8147df69 | -9.55824 | -66.04983 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47303c78-0c4f-3ea1-95f6-7c8c56f6d7c8 | -6.62167 | -57.98078 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b707fd9-9787-3fe6-bd49-5b0ab61ecb3d | -6.72979 | -55.08668 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 290498fb-8c1c-3edf-90ae-503053b4a51f | -11.015 | -54.14849 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 810246c0-7167-3a40-9b7e-a93fbfe3105c | -6.30982 | -60.01058 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README102.md)
