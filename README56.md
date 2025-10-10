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
| 140e79d7-e421-33d8-8aaa-7b269fb7b511 | -8.4844 | -46.134 | 2025-10-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 46c17a48-b836-3df1-a15f-d3714e4a39b8 | -13.3488 | -47.7388 | 2025-10-10 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 79418110-b61d-32bb-9ade-4391b89bcdc2 | -7.1345 | -44.1478 | 2025-10-10 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 556e185d-0b1b-3b61-b1f4-738a5b2231a1 | -9.4677 | -45.9834 | 2025-10-10 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0f6e653c-8249-3610-a015-25b6b98155dc | -5.9516 | -42.2617 | 2025-10-10 14:40:00 | GOES-19 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 3011b47a-7df6-36f6-b327-b8325b504c96 | -8.1615 | -43.3465 | 2025-10-10 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 77a22ce6-b243-3c10-91af-83c322a24144 | -5.4766 | -42.8897 | 2025-10-10 14:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 1547f7b3-bf40-30b6-a80e-c45da5267e34 | -7.5275 | -44.3182 | 2025-10-10 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 96f0f521-f2a0-3f10-97fa-2678b3000f05 | -8.1804 | -43.3445 | 2025-10-10 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 168.5 |
| 4508adae-f5d3-30e3-8471-3dde3aeef4e0 | -13.3484 | -47.7612 | 2025-10-10 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a317a59b-9c2e-3639-af22-8a17f89671df | -8.8524 | -45.3721 | 2025-10-10 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| fa24426b-9d0c-354c-93d8-a4b657a784ab | -10.1707 | -44.5959 | 2025-10-10 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ebbaed20-6a9d-3251-aaaf-bc531eaf2796 | -12.4701 | -47.464 | 2025-10-10 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 39de4b6c-b3a1-3adb-8b2b-a078bf13a77a | -10.1714 | -44.5496 | 2025-10-10 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 0e06555c-6b7c-36fb-a8e3-96f757ebd778 | -11.6852 | -47.5263 | 2025-10-10 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 46933bf4-0850-3e67-834f-7f8b44da6803 | -5.8088 | -43.4724 | 2025-10-10 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| eff6447d-c5e5-34e0-8953-b8fad78699ee | -12.1559 | -47.9302 | 2025-10-10 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| a4f01c5a-86d8-3ec9-8777-6b3486f99bcb | -6.2644 | -42.9208 | 2025-10-10 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| aafd096b-8b02-3124-ab54-d6a005dd988e | -10.1901 | -44.5703 | 2025-10-10 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| aeafa57d-fe06-3677-af1c-69f230228e19 | -13.3295 | -47.7417 | 2025-10-10 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 0957cbcd-0c58-31f1-970e-b0fbaa6a657d | -9.4674 | -46.006 | 2025-10-10 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| ff35a982-0874-3c2a-aa0a-aa0279655060 | -6.2641 | -42.9443 | 2025-10-10 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 9d06b6b4-85d9-336e-bd1a-dca9fc1f6ede | -12.2876 | -49.2101 | 2025-10-10 14:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ef910cf5-2de0-301c-89ea-ddd55a2f9602 | -8.5052 | -45.9744 | 2025-10-10 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 29659e84-0791-36b7-93c0-328837f2275a | -10.1517 | -44.5984 | 2025-10-10 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5282bbbc-5873-3a72-91e9-1d3c374f16f4 | -7.7922 | -44.2229 | 2025-10-10 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| ca64ed76-d959-3a68-bd21-587816865b50 | -13.3026 | -47.1174 | 2025-10-10 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3c3df743-9d20-32b1-a8d1-782f450810a9 | -13.2967 | -48.4801 | 2025-10-10 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f8485ed5-c2fb-3984-a416-b5b7363a03a3 | -8.8729 | -46.6985 | 2025-10-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 4a578e3d-e0ce-316e-b8ca-a9d3090bd5c1 | -7.7924 | -44.1998 | 2025-10-10 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 9e9912a9-2147-38b4-9166-e953bdff9128 | -8.6106 | -45.102 | 2025-10-10 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| a881c0aa-6211-3bf9-bf4b-5203ad178a84 | -13.3681 | -47.7359 | 2025-10-10 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 10958b42-c589-36b5-8321-c1884100b205 | -16.7312 | -43.9931 | 2025-10-10 14:40:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 377.0 |
| c7e1d604-5fb3-345d-90d2-d624000c2ae6 | -13.8496 | -45.8223 | 2025-10-10 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 80831136-b92b-3990-a43c-56e1a667d6cf | -7.2959 | -44.8447 | 2025-10-10 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ca7ef250-a517-3abb-abeb-2050a8352f7d | -13.3057 | -47.9906 | 2025-10-10 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 5f2d5753-f10b-3c94-a51e-4645c389eeb5 | -11.7585 | -43.3374 | 2025-10-10 14:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b1cdcfb3-81d0-32d4-93e5-1e1c8491f354 | -12.5541 | -48.1419 | 2025-10-10 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 09025a61-f11a-341a-9199-a22027accd18 | -8.1618 | -43.323 | 2025-10-10 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 180.0 |
| 1b8ab8f5-10d0-3a6e-af9b-7a843ff0c013 | -9.486 | -46.0265 | 2025-10-10 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| be84ffdd-4bf9-38d8-8c33-678dab8f18eb | -14.8884 | -47.2226 | 2025-10-10 14:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 6229fdb8-1aee-340a-8d94-af45af4eb53e | -6.7352 | -42.832 | 2025-10-10 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 8d942a8c-ded2-36ee-9937-260641a82c5a | -7.1347 | -44.1247 | 2025-10-10 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 6c60ca9c-a8ce-3f2a-8540-938a4099f9fe | -7.8121 | -44.1285 | 2025-10-10 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 634c60dd-71f1-3c92-bc01-ac5967d59ac0 | -17.9026 | -57.5153 | 2025-10-10 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 93067773-8ccf-3ebc-86f1-99f3424513c6 | -4.4845 | -42.8631 | 2025-10-10 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |


