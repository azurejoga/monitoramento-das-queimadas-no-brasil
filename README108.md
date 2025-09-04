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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efadca9d-570c-3e9d-8227-4dda555226a4 | -13.8457 | -47.9764 | 2025-09-04 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| ae3ea3f9-77d6-3a65-abde-822c85398f8c | -8.3829 | -48.3317 | 2025-09-04 14:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 7881c134-b757-3b8d-aca5-c40a6233597e | -5.7 | -45.1786 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 58e51931-119a-3c24-b50a-d8ef6a0aacaa | -11.3897 | -43.5839 | 2025-09-04 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 5a14eb87-1b63-3c9a-b404-b3247e7a73b8 | -5.6813 | -45.18 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0b35867e-78b8-3a10-853e-45555c1af65d | -13.8453 | -47.9988 | 2025-09-04 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 53552b02-2333-36b5-a60f-9acc28e285d1 | -6.2773 | -43.5046 | 2025-09-04 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| aa67d1ea-d168-38d6-91f5-5d0105e7ee0b | -5.7187 | -45.1773 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 32808f4e-2820-3152-95d9-952494307d9f | -13.1079 | -57.1109 | 2025-09-04 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 761852b0-13bb-3409-be41-7b59e40854e8 | -7.0131 | -43.2291 | 2025-09-04 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 6b712281-f577-31b6-9ac5-d188a862faec | -5.7528 | -45.5587 | 2025-09-04 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| c48b600b-a28e-358e-838c-85afeb0d20d6 | -7.0128 | -43.2525 | 2025-09-04 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 2c28a4a0-fc7c-346a-baf1-11285d61f33b | -11.6525 | -52.212 | 2025-09-04 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 318ee72a-725a-336a-8e10-c392c6267a73 | -10.1457 | -46.2424 | 2025-09-04 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 71a21a89-e502-30d7-aa1b-1a0c78efe4fc | -8.0389 | -44.082 | 2025-09-04 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 5e7c8f3c-2b85-36bf-9512-e0bdab66f647 | -8.0417 | -45.3882 | 2025-09-04 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 105996e9-0a65-38a4-9800-bce45f924812 | -5.908 | -57.7311 | 2025-09-04 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| be593327-2ca5-330b-9382-e33c604415d9 | -11.7385 | -47.7637 | 2025-09-04 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| e1aa62ac-c40d-301c-87ff-7b54655ed09e | -15.4564 | -53.0183 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 3faaa4fe-534c-3e58-937a-554ab50b7439 | -11.5969 | -52.113 | 2025-09-04 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 141.7 |
| a5ba7c87-2b3b-3d93-9c07-a8fae598f7a1 | -6.2251 | -45.0264 | 2025-09-04 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 077d2570-055f-306d-a1de-446cdb1ce088 | -8.2001 | -49.5988 | 2025-09-04 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 0dfc5464-e921-3ff6-b403-2888ec91a1dc | -4.9951 | -56.256 | 2025-09-04 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 147.0 |
| baa505a4-c0ae-3f0d-a75d-b4d3ee6122ac | -10.5316 | -57.7747 | 2025-09-04 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3d2f26f2-7412-3df3-a82e-41cfc75cd98d | -8.02 | -44.084 | 2025-09-04 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 148.1 |
| b6b46b45-3021-3d4d-b26c-191629b683ea | -8.8842 | -45.822 | 2025-09-04 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 595b3476-fb5d-3916-be3b-f67801a8cb62 | -5.753 | -45.5362 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 196dda91-c9cf-3298-9a7c-02ee1efd0f41 | -11.6601 | -54.5093 | 2025-09-04 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| ff4937da-2c69-3852-b6cd-541953378000 | -4.8862 | -41.771 | 2025-09-04 14:00:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 155.4 |
| a2da3cbb-1c97-3628-a46f-0a96729c5dd2 | -15.737 | -53.635 | 2025-09-04 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 141.7 |
| f6a92a94-1914-3fd2-bebd-a89ca181a7aa | -6.2062 | -45.0506 | 2025-09-04 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| deeb3a8d-acae-30da-a487-6deddc0de88e | -5.6963 | -45.6076 | 2025-09-04 14:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| ee434d50-c96e-3850-8e50-b7b867604c93 | -10.4658 | -50.3907 | 2025-09-04 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 8d2f3832-5b30-386a-9fa3-3e6b6e8afef6 | -6.2315 | -42.4515 | 2025-09-04 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 306.0 |
| bda86397-fcfe-3a2e-adb4-bb3a4890c338 | -22.6558 | -43.7079 | 2025-09-04 14:00:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 111.0 |
| 846ffee5-756a-366a-904f-4bb5d6bce898 | -8.0985 | -45.3598 | 2025-09-04 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 265b8b46-2056-3984-980d-0d508a8d7b51 | -11.6599 | -54.5297 | 2025-09-04 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 230f1754-3b38-3971-8c08-e9accdf99dc7 | -6.2205 | -43.5558 | 2025-09-04 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 9aec076c-907c-320a-951a-31c53e949f07 | -17.0652 | -46.449 | 2025-09-04 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 98.7 |
| b62f871f-e09c-3a77-9a87-d5b427cc80ff | -4.9049 | -41.7696 | 2025-09-04 14:00:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 654e69e9-14b8-36d1-af82-4b7d34e76b1b | -10.9867 | -45.9325 | 2025-09-04 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| f58d988d-fc87-34b1-9212-382144f4c025 | -6.0232 | -46.6784 | 2025-09-04 14:00:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 78a580fc-d392-3534-afd9-24d457a95bc7 | -16.0474 | -47.835 | 2025-09-04 14:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 4ae5e54a-cbfb-37ae-907c-531faa82537a | -8.0796 | -45.3617 | 2025-09-04 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e1dfee11-7192-350c-be4f-f810b421cefd | -6.3692 | -45.6258 | 2025-09-04 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| ae41e504-44b5-378a-aa12-7c3a19a13b11 | -10.4486 | -50.2644 | 2025-09-04 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| b81d35a7-33ca-3188-8066-b156ec62d45d | -7.6854 | -48.717 | 2025-09-04 14:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 84.3 |
| c67c4d68-6edf-3272-8e53-6ab93daef00b | -6.7686 | -45.0051 | 2025-09-04 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 05a724fd-6e6a-33ea-a8f2-bacfb116cbd5 | -6.8944 | -45.5383 | 2025-09-04 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| dee7e492-92db-3f2e-8e2d-e50f7e4de2ea | -5.7002 | -45.156 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 7163fe02-30bd-31bc-b880-9e5ce1efe7fc | -8.0392 | -44.0588 | 2025-09-04 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 0cc7d41c-f0fc-366c-8d42-7cebfc8086f7 | -9.5023 | -57.8229 | 2025-09-04 14:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b7e41379-e43f-3577-9f75-e2492cf814c0 | -8.2004 | -49.5773 | 2025-09-04 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 2c7a73d4-f68f-3b16-b9d4-5e441c378ddf | -11.5972 | -52.092 | 2025-09-04 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| f1247c18-0de7-3ab6-b32b-6cd64eeb3fb2 | -6.2318 | -42.4278 | 2025-09-04 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 155.2 |
| a860349b-f22a-3f5d-87dd-98bbf43c8c9b | -6.1665 | -43.3273 | 2025-09-04 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| fec4c3a1-acc2-3c34-991a-4857fc78d7d5 | -11.0436 | -47.1409 | 2025-09-04 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| df4d06c7-621c-36bc-b6e7-a6e9e08e1e18 | -11.0062 | -45.9072 | 2025-09-04 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 56f99c7e-2e71-3063-8184-a96273ed9179 | -6.0419 | -46.6771 | 2025-09-04 14:00:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 106fa043-cf7e-3622-b0c1-dc2bbee47199 | -8.3832 | -48.3099 | 2025-09-04 14:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 7d44bd38-724a-307c-a223-0f56620d6e8f | -5.8206 | -46.3595 | 2025-09-04 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 4f80a285-f416-366c-96cd-b7704c8eb29b | -11.8343 | -51.4339 | 2025-09-04 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ac020d68-fce1-3c19-93d6-bcb6615ca345 | -11.3901 | -43.5602 | 2025-09-04 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 5ddce8d0-7a6e-3fdb-b057-3eca316236a9 | -15.0059 | -50.0739 | 2025-09-04 14:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 0fae0b3c-4c5b-36fb-8a31-c2698d479354 | -11.5782 | -52.094 | 2025-09-04 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 198.8 |
| f0410f1c-5ba5-3247-8701-177a9b920bc8 | -9.4376 | -46.7947 | 2025-09-04 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 15a0bb09-9933-3979-84cf-a460ac8d9cb4 | -8.9031 | -45.82 | 2025-09-04 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 1eb05caa-d120-3606-ab5e-7b37f75c6087 | -7.9117 | -45.242 | 2025-09-04 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 828eb550-2aa8-394e-8977-425a8f5ed457 | -13.8647 | -47.9958 | 2025-09-04 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 2b3afcc6-e512-3d0e-820c-35e6e3f27ac4 | -15.0449 | -48.1207 | 2025-09-04 14:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 92cd05d5-f53c-321d-b0b3-bacc0d90bb67 | -10.6577 | -51.5996 | 2025-09-04 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 216.7 |
| 01799260-ff90-3e76-97ce-4c0ea727df69 | -8.9025 | -45.8652 | 2025-09-04 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 044eebbe-4fa7-3b85-a1b4-804dd8f7d49c | -8.0203 | -44.0608 | 2025-09-04 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| be02b387-6eaf-3c1a-9ded-54e8bc88c15a | -11.5963 | -52.155 | 2025-09-04 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 93f51869-9e1a-35b3-bf96-5edcc566e37e | -6.8754 | -45.5625 | 2025-09-04 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 96499ce1-adf7-35b3-9dc4-b911d3fb54a8 | -7.7036 | -48.7587 | 2025-09-04 14:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 4ed5d88c-d6be-31c3-b3c3-d4fc416589bf | -5.6777 | -45.6089 | 2025-09-04 14:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| d319dca5-7138-3952-aeee-3ea8787baaee | -14.5852 | -53.0268 | 2025-09-04 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| b8d3b71a-3729-3b45-9a28-8123210ca2ce | -7.7039 | -48.7371 | 2025-09-04 14:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 6b12bec7-307a-30d9-a60a-42e8c626a883 | -6.8941 | -45.5609 | 2025-09-04 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 33401272-99c5-328d-8d3a-e7f9828d6c13 | -7.6851 | -48.7386 | 2025-09-04 14:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 163.3 |
| d8d2134c-111a-3ba4-a8d4-8fc26506b24f | -6.2952 | -43.5961 | 2025-09-04 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| a77d8912-43d8-3d72-8fd2-fdebb89d22cd | -5.8525 | -57.7722 | 2025-09-04 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 3c6f3b7f-be53-3a16-8aa8-16bc0b006038 | -8.3641 | -48.3334 | 2025-09-04 14:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 9e8d1eee-c6be-395c-ba03-9f7063d08797 | -8.3644 | -48.3116 | 2025-09-04 14:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| e1db2563-48d7-3742-ac1f-4c396c8a8ab0 | -15.4567 | -52.9971 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d657079d-17f9-3c85-b64e-687291fe7b7d | -15.229 | -52.7101 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2d3b1ea9-27a4-3894-a6b3-aa41ff1035a3 | -5.699 | -45.2918 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b8656eac-d3b2-36c3-8b76-4144db10b800 | -15.4567 | -52.9971 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 3f5e4f0d-5cb8-3867-8ad4-645c3fd030d7 | -5.6813 | -45.18 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 96ed7c8d-d6c9-3cfa-b884-d130be7cad01 | -9.6851 | -51.0186 | 2025-09-04 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 1ad916f5-9133-3a7b-ae4a-ab55c64f2a43 | -6.213 | -42.4294 | 2025-09-04 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 0ad51959-55a4-3f14-a901-bbec62dcb8b2 | -6.8754 | -45.5625 | 2025-09-04 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 6f13f656-e02f-3a3c-a33a-2516167c32a7 | -11.6599 | -54.5297 | 2025-09-04 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 63c3eca1-0a29-3297-8c8c-7a4077f35bc2 | -8.3641 | -48.3334 | 2025-09-04 14:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 7850ce54-c413-3929-8fe1-5ceb3d233bfe | -5.0135 | -56.2553 | 2025-09-04 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 747ef559-2078-35b6-9dcb-fed11c17b647 | -6.0234 | -46.6562 | 2025-09-04 14:10:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3b8773ae-934b-3942-ab3f-149f1f26fdbd | -6.1665 | -43.3273 | 2025-09-04 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| eee14f00-8346-3768-b315-2b8eb973cca1 | -17.1495 | -46.2458 | 2025-09-04 14:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 859ea305-a1fa-3b62-9957-bf5513dfe74b | -12.2344 | -50.1488 | 2025-09-04 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |


[Clique aqui para ver as próximas entradas](README109.md)
