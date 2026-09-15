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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 617d085a-c6a9-3a18-9f3b-c52696c3f9e8 | -15.2827 | -42.783 | 2026-09-15 13:50:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 20fde849-9c23-32cc-94a0-ed31257df50d | -9.3577 | -50.0943 | 2026-09-15 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 678944af-b6d3-3c13-8059-fb4d77266f31 | -12.3085 | -47.9539 | 2026-09-15 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 0aa857a9-b78d-3afb-b60d-9f5f22d1e9a6 | -11.9033 | -43.8112 | 2026-09-15 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 8412d49e-7a6e-341f-957f-a6b3b9787d53 | -10.7916 | -46.2298 | 2026-09-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 6fec839b-1021-3147-b89f-1af0d0f153d7 | -5.144 | -55.9345 | 2026-09-15 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 36fbc7a1-00fa-3a5e-966d-ba9dbe3afb40 | -9.3569 | -50.1583 | 2026-09-15 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 963942c5-f209-3339-a57b-f8dc914ac4b1 | -9.1337 | -65.8253 | 2026-09-15 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 0946a2ed-3022-318b-b5a5-e27aca13d0c7 | -7.0166 | -44.6184 | 2026-09-15 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 4d41b20c-aba6-34ca-951e-f5f0b5224321 | -9.4234 | -47.8588 | 2026-09-15 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 70152603-795d-33fe-8038-718f60412fc2 | -5.5286 | -43.3771 | 2026-09-15 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0d68b651-ec43-3b6d-adc9-5323be1910fd | -9.7687 | -46.1067 | 2026-09-15 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 93272592-6360-30bf-86d9-c032e7608dc3 | -9.5918 | -46.5765 | 2026-09-15 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 360c2369-07f1-3031-90da-4ee23181101d | -11.2304 | -54.0985 | 2026-09-15 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 1e4758ec-531e-3234-a77c-8e5bbe752acd | -7.0823 | -42.1107 | 2026-09-15 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 9509dbe3-e5f9-3c81-a448-97248467bfa1 | -8.8459 | -45.8713 | 2026-09-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 426c5f94-b0d8-39d5-b2a7-58a3dfa0bfea | -10.8661 | -46.3331 | 2026-09-15 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 9b11cb77-b0d5-3fe9-af77-ded2463125cc | -13.2678 | -51.2856 | 2026-09-15 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 43305376-f8bc-39fa-8d5a-2d78fdab9443 | -10.3113 | -45.3366 | 2026-09-15 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 361.2 |
| 50995659-4526-3ab3-b85c-f4eaf2379f5a | -2.9579 | -50.3988 | 2026-09-15 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1547cdb3-c8bb-3266-818d-49ec3c948702 | -13.3949 | -57.0242 | 2026-09-15 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 68675b8d-59b7-3f7c-a724-a16aafbcedb1 | -13.3062 | -51.2808 | 2026-09-15 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| afe76086-1a5b-3a32-86f7-ea2161b6f781 | -12.3081 | -47.9761 | 2026-09-15 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| cfd6c52b-d272-3c60-b088-1c72b291f8ed | -13.7002 | -51.8274 | 2026-09-15 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| edf7e0e3-e751-3acb-88d2-a82f1c1d1e02 | -10.6827 | -54.1679 | 2026-09-15 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| e1c357a4-4add-3fb0-805f-4d5e2af3182f | -9.4266 | -60.3003 | 2026-09-15 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 73033e98-9393-3df8-a3ad-f4105f8bb0b3 | -10.3116 | -45.3136 | 2026-09-15 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 3d25f7bc-e340-329a-80ed-d3f6d7c3d7f7 | -11.5041 | -45.7939 | 2026-09-15 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 79c73b62-6c88-382f-8211-88b22a8140ad | -18.1709 | -51.7685 | 2026-09-15 13:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 96e74497-2175-31a8-a47a-9c6be3b70de6 | -12.3277 | -47.9513 | 2026-09-15 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 202.2 |
| d21f407e-8242-3c8a-b760-9463b23dd5e2 | -10.8665 | -46.3105 | 2026-09-15 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 9622bc7e-f7a0-3388-befb-ed6346e17df6 | -13.7722 | -48.8087 | 2026-09-15 13:50:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 49.6 |
| e5979cda-253c-3c6d-a74b-99c61acb8408 | -9.4139 | -50.1103 | 2026-09-15 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ce66bc1f-7761-32bc-bce5-024661cbd43b | -14.1666 | -47.3876 | 2026-09-15 13:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 085bd0d3-b2dd-3714-ba44-3ab37289ef85 | -8.5468 | -50.4423 | 2026-09-15 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| f2dc5d66-b5d4-3d21-a6e9-37ce606b02fb | -8.638 | -44.4567 | 2026-09-15 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| e0cc537b-3d85-3a78-ad48-6a3edf1bb906 | -10.9685 | -48.3232 | 2026-09-15 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 76ae2633-c40c-380d-8820-d84efba5a6ff | -11.5045 | -45.771 | 2026-09-15 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| bffcabc7-4cf9-3d0a-9432-e60cb812540e | -2.9025 | -50.4004 | 2026-09-15 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| a0196ee1-cd80-38e7-baae-2e10c145e044 | -4.5229 | -54.9639 | 2026-09-15 13:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e94059f1-766e-3b2b-96d7-6650916f910d | -13.3059 | -51.3022 | 2026-09-15 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| b3057a35-1dab-3392-a2ec-1b755e50c3f9 | -7.1708 | -44.2598 | 2026-09-15 13:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 0429f4f7-c4bf-3a77-a5c2-517bbda7b446 | -10.792 | -46.2071 | 2026-09-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| bcfda781-9f49-336b-97d8-cf925568ed31 | -13.382 | -48.0239 | 2026-09-15 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 9bd316bc-6f49-3eac-ba71-6802f9281400 | -13.7529 | -48.8116 | 2026-09-15 13:50:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 43.7 |
| ec5d6e0e-33d9-3fb4-abd6-0c1564fff6b8 | -2.7768 | -49.4553 | 2026-09-15 13:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 282fd2b7-a3cd-34a0-9969-7a4c8a570832 | -13.2675 | -51.307 | 2026-09-15 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 0d0f680b-c6a8-3614-b6ad-d5b2372f4277 | -8.8134 | -46.9272 | 2026-09-15 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| cc11d788-9e46-36ac-830e-dd1aa1fb47ea | -8.8137 | -46.905 | 2026-09-15 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| b72d152a-4627-39db-a236-5b5adddbf3b6 | -9.3575 | -50.1156 | 2026-09-15 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| c93b0db8-4e75-3441-957c-8686b61fc4f0 | -9.6104 | -46.5967 | 2026-09-15 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 3637457b-e30f-3f19-975f-a1133d436b5d | -11.2113 | -54.1208 | 2026-09-15 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 302.8 |
| 48df8f86-ac4b-3e21-bf20-be03bff9e555 | -2.9025 | -50.4214 | 2026-09-15 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 31345935-2592-39b8-a8c8-180fea681e8b | -7.1525 | -44.2154 | 2026-09-15 13:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 275.4 |
| 299279d7-cb6f-32cb-9442-5640f1f17efe | -10.8855 | -46.3081 | 2026-09-15 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 412.0 |
| fd3c054d-f707-33ee-95f6-c2d02f8b8944 | -5.1255 | -55.955 | 2026-09-15 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 68e0592c-c35e-37b5-a6d6-b396031c5e90 | -2.921 | -50.3999 | 2026-09-15 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 2f9614cd-5126-3ef2-8871-e6f70df7b3e6 | -8.6191 | -44.4588 | 2026-09-15 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| aa30a027-9d2d-312c-98a0-01293fc77dee | -15.0208 | -41.4621 | 2026-09-15 13:50:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 18b88b6f-673b-334a-b02f-43ff6986e29c | -10.6641 | -54.1491 | 2026-09-15 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| da62eaf7-2ba3-3615-8046-82a0d1a5465d | -10.9875 | -48.3209 | 2026-09-15 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3ad998e4-60ea-394b-bf55-c8c3bdc673d3 | -7.082 | -42.1346 | 2026-09-15 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 150.6 |
| 23c68eca-fd87-3da0-be8c-d30b4810ad59 | -9.7358 | -47.0958 | 2026-09-15 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 1f3b2bdf-30bc-3b92-9054-5548fa463290 | -10.3109 | -45.3595 | 2026-09-15 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 298.7 |
| 929a8a2c-6bd3-3117-829c-35585d923c8e | -18.1714 | -51.7466 | 2026-09-15 13:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 252cdbe7-7fc8-32bb-a2e9-b48b76931922 | -13.4018 | -47.9987 | 2026-09-15 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 6ec94ee4-0e8c-3d1c-bca1-3db77ed25f4b | -2.884 | -50.4219 | 2026-09-15 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 29147320-ccc0-31c1-8139-fd2fcc1b7c9f | -12.3273 | -47.9735 | 2026-09-15 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 197.7 |
| f8c66835-9cf5-3c92-9533-0f3bfe1cc1e0 | -9.3572 | -50.137 | 2026-09-15 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 3670d42c-0382-300f-be88-c6ecc7a5d020 | -15.539 | -53.8502 | 2026-09-15 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9d2696ba-1b31-3804-8274-841645945515 | -11.2302 | -54.119 | 2026-09-15 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 7c79ddde-a868-3400-af7a-cf3e37bd9aaa | -18.1714 | -51.7466 | 2026-09-15 14:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 122.8 |
| a131d6bb-04fa-3783-a3cf-b71a8705bfb1 | -10.6641 | -54.1491 | 2026-09-15 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8e839acc-07e7-36b2-861a-b86d378c81a8 | -13.7002 | -51.8274 | 2026-09-15 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| b5aaf9bd-505d-33cf-87db-65cdf0405a43 | -12.3081 | -47.9761 | 2026-09-15 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| d5071e0a-d11d-3184-9614-5902d0ff7a52 | -11.5041 | -45.7939 | 2026-09-15 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| d119b18e-d10e-33ef-a1ff-3b722f9bc90a | -9.3569 | -50.1583 | 2026-09-15 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 6f2185be-0ceb-300c-80c3-edc31ea5057c | -2.6966 | -57.5889 | 2026-09-15 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b8a9ff26-e3a8-31d3-8c94-fedcc6269136 | -8.638 | -44.4567 | 2026-09-15 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 131.4 |
| c31bd218-e979-3027-8292-41fd2417e335 | -2.921 | -50.3999 | 2026-09-15 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| cb1fe577-87f5-3389-9150-2a5d1e694a3c | -11.2113 | -54.1208 | 2026-09-15 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 197.4 |
| d3a1b663-7a46-3c9d-80b9-ddff2a054b1d | -9.3946 | -50.1548 | 2026-09-15 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 84950a41-d70d-36b4-bad1-0c29c2c66623 | -8.5415 | -54.7187 | 2026-09-15 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| e6bbea23-32e7-3171-b106-b7a4323b2084 | -2.6602 | -57.5119 | 2026-09-15 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 38f6769c-b640-3e80-b337-263e8d6a75fb | -13.2675 | -51.307 | 2026-09-15 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| abd2280f-a5a2-39fe-850b-914abd67cfcb | -12.3273 | -47.9735 | 2026-09-15 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 0bf58db0-37be-3bd9-9e9f-4bdbf2dc6ada | -8.8078 | -45.8979 | 2026-09-15 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 53ae4cbd-1b2e-3fb6-b922-b88b2bdcbd5e | -9.3572 | -50.137 | 2026-09-15 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 69b1908c-7b07-3f78-a8b5-95f383b38468 | -2.6785 | -57.531 | 2026-09-15 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 42ca478a-84ce-364e-84c8-26760cd1b3f3 | -9.4137 | -50.1317 | 2026-09-15 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a91bd9eb-d9ac-347f-8035-1e919747c059 | -9.1337 | -65.8253 | 2026-09-15 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| c0c448d9-ec7d-3181-8b44-cefface31fb2 | -9.7358 | -47.0958 | 2026-09-15 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 0b7f2139-b32e-3dc1-a5dc-b784fce42828 | -13.7006 | -51.8061 | 2026-09-15 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4168e68d-17cb-37e7-91b1-1d7e1e125df1 | -15.5202 | -53.8106 | 2026-09-15 14:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| e418898b-015c-3ed1-a077-dc447137d535 | -4.5229 | -54.9639 | 2026-09-15 14:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1fb18ddc-10dc-3bb8-a7ba-081011babca7 | -9.7687 | -46.1067 | 2026-09-15 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 8b94e411-16b7-37b7-8cae-e8e9149305c9 | -9.3575 | -50.1156 | 2026-09-15 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| fb54043c-24cf-3954-865d-58ae0ba08b3b | -9.4139 | -50.1103 | 2026-09-15 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| bb74bd10-c36f-3ba9-909e-a142486d8091 | -11.5045 | -45.771 | 2026-09-15 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 81c55a97-d3f1-3caa-a508-78b3213d3e95 | -7.1525 | -44.2154 | 2026-09-15 14:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 252.1 |


[Clique aqui para ver as próximas entradas](README78.md)
