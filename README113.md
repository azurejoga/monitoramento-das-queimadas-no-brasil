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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb9d532a-9dc7-3406-a098-9ac127a94ec9 | -6.7911 | -52.796 | 2025-09-01 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 893eb8aa-b849-32f1-9984-81bf528ed32d | -12.5764 | -44.8047 | 2025-09-01 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 3787cfc1-ed43-3a34-a7a7-31aeb5cb28ba | -6.471 | -44.7792 | 2025-09-01 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 182.0 |
| fa70e7f4-8b55-34b5-a8b6-ad64a5c816ab | -6.8237 | -43.3402 | 2025-09-01 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 588cf40a-88f5-3ab3-942b-4db465ca51a2 | -10.0434 | -48.0998 | 2025-09-01 14:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ebe6686a-56ca-3071-98d4-d3b375f92b0d | -8.8437 | -47.5217 | 2025-09-01 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| b745b915-0bfe-3f4e-8573-f0ddbbf486a4 | -8.6673 | -62.8369 | 2025-09-01 14:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 99.4 |
| ed2517ca-a701-3b8d-bf7f-aa467369aef9 | -8.6883 | -62.4002 | 2025-09-01 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.5 |
| ee1663cd-e9f8-3a2e-bf99-3c6c1d3182d7 | -9.6505 | -47.8128 | 2025-09-01 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a1a7df0d-a244-34e5-9907-bf20330dc1bc | -7.6783 | -61.0908 | 2025-09-01 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.9 |
| e7a17f2e-3810-3411-884c-cf2c58f53a28 | -8.9671 | -48.1896 | 2025-09-01 14:40:00 | GOES-19 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 631ec319-093e-34f0-9c30-a70e734987ad | -8.9125 | -45.1147 | 2025-09-01 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| d3072f0d-3ecb-3ff1-a2cb-c5f825026b63 | -7.0572 | -44.3393 | 2025-09-01 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 56226850-3c04-32a8-9e4d-cd6d5a7470a3 | -11.8334 | -51.4975 | 2025-09-01 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| eacee594-aac6-3c50-9afd-52e11009fead | -11.7993 | -46.4114 | 2025-09-01 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 665842e7-3298-3665-a5e9-ff031c0d1785 | -12.9575 | -48.1076 | 2025-09-01 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| dadf15e9-7d7f-307e-ad2c-7437093ca8e2 | -12.392 | -46.4626 | 2025-09-01 14:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| fbe3fe0b-a6a4-3da2-9e3d-bcfcedc9522f | -9.4987 | -46.4749 | 2025-09-01 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e8405c68-8644-34dd-a57b-6b8fcfb31ff8 | -13.4982 | -46.9743 | 2025-09-01 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ea185eb0-21c4-3179-b12d-8cd3dacbc8b2 | -6.8281 | -52.8143 | 2025-09-01 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| d50b0515-51f0-37c9-90a0-88d840982c5c | -7.1089 | -44.7703 | 2025-09-01 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 2ea25d50-66a9-3ac0-9757-ec84a7bb37f6 | -6.7909 | -52.8165 | 2025-09-01 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| bbd61777-3ddb-3b71-90c1-e3e4af706f3c | -11.7985 | -46.4567 | 2025-09-01 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6fa4f519-d33c-37e5-980b-d817d7b0c081 | -9.2825 | -47.1007 | 2025-09-01 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c76b8531-f2eb-3f2c-8315-74c7fa810c28 | -8.6316 | -62.5921 | 2025-09-01 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 38ae3af4-044c-3acc-9e98-6246ea616b62 | -14.0508 | -44.5543 | 2025-09-01 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 4a5464e5-75bc-32e9-bb4b-fae641493446 | -7.9539 | -46.4542 | 2025-09-01 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 88b8c026-8994-3115-85d3-5f8f93059b13 | -9.6127 | -47.8169 | 2025-09-01 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| bf3f1e0c-d1c5-384d-a56f-f8ac1f27c7e6 | -7.4798 | -63.8204 | 2025-09-01 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 20957750-9a2d-3a3a-b539-d5d60eeaff35 | -6.8428 | -43.3151 | 2025-09-01 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| c4d6d166-f131-34cc-92d1-92ff80e7032b | -11.9619 | -45.8657 | 2025-09-01 14:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4d6ebf86-3b51-324f-bcda-f0ec28d72d78 | -6.8279 | -52.8348 | 2025-09-01 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| ccf83e93-bbbd-37b7-840f-f64e2c2027ec | -7.7839 | -50.0585 | 2025-09-01 14:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |


