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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a16f346a-c519-3bc2-be5a-4b0b9adbfe33 | -1.2095 | -54.556499 | 2026-09-24 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1288968b-808e-3aa0-a97b-91db65c1e7d5 | -9.6798 | -46.700699 | 2026-09-24 00:38:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f80596e8-6b4d-33a8-a353-e04a6e2c1ee4 | -2.4483 | -49.2118 | 2026-09-24 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d245a93-baeb-3f73-8f07-aa2623ca5d2a | -11.9446 | -50.768002 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 026eb21e-bcc8-3bac-928d-ca5303f536b7 | -12.1632 | -47.3675 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 506ba086-78a2-32eb-b112-78cc5e5c3bce | -3.2282 | -54.311699 | 2026-09-24 00:38:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a460be7e-1974-3932-85eb-faf7f36bd907 | -6.7249 | -44.1465 | 2026-09-24 00:38:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2eb643cd-1cd3-347b-845c-0881bdda6f0d | -11.9623 | -50.754902 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85f03a93-588f-3261-a933-8dc9cebe49ca | -2.1286 | -49.526501 | 2026-09-24 00:38:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80edb4ae-8c54-3720-85a1-fd769b21162d | -10.717 | -48.724899 | 2026-09-24 00:38:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f371128-d4ae-3c2a-8c60-a3239c92e5ef | -13.7023 | -43.075901 | 2026-09-24 00:38:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 774fa60d-2b3f-3cb5-96fa-b27b4fdc83d3 | -2.5961 | -47.348801 | 2026-09-24 00:38:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce2c23d9-a019-3329-ab2c-5a251544688d | -12.1362 | -45.6287 | 2026-09-24 00:38:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52a0dfdb-1d04-3efb-9f11-e277f0793e0f | -8.901 | -46.8139 | 2026-09-24 00:38:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be7014c4-6fef-321c-b3b5-2798a201fc8c | -15.463 | -47.904999 | 2026-09-24 00:38:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c4403e4-6557-3923-97d0-ad594ec56287 | -3.705 | -54.196301 | 2026-09-24 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf485fa-6939-3f58-81d9-e186ba80c0df | -11.3513 | -43.364201 | 2026-09-24 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b899c5b1-02e7-31ec-b072-c9b719b3f058 | -6.4178 | -59.9282 | 2026-09-24 00:38:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aeab6a2b-7b9b-3cb7-94a2-dde82f46cb99 | -3.449 | -50.067799 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6556956c-f983-36cc-8752-3023e6e2c24c | -8.7458 | -45.836601 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9cbd848c-1196-384d-920c-2943f25f45ac | -3.0098 | -51.530701 | 2026-09-24 00:38:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3a857b7-4383-379e-91c9-5fc2b9a229b9 | -10.9313 | -43.8526 | 2026-09-24 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed351c72-37f1-32f9-ac01-e652999adfec | -9.2737 | -48.625801 | 2026-09-24 00:38:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 885960fb-26cb-365c-a65a-7821b7883bde | -7.6172 | -46.7967 | 2026-09-24 00:38:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4036f78-f7d6-3016-a17a-b5148d8c2ae5 | -2.4498 | -49.218601 | 2026-09-24 00:38:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 536637d6-eb30-3a54-8fd8-25bce04458e7 | -2.2975 | -47.8867 | 2026-09-24 00:38:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89b9d6b0-c756-376b-b701-2d7b5a2c3829 | -15.4597 | -47.890202 | 2026-09-24 00:38:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 429df8d2-cd00-3414-9a43-cbfe10dae164 | -9.2334 | -47.361198 | 2026-09-24 00:38:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c10ab5b5-01ca-31c5-8dfd-bcb9d1da799c | -3.2006 | -53.370201 | 2026-09-24 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 880974ba-7fe3-30ca-86e3-e7dfcef2ae00 | -3.2064 | -49.099201 | 2026-09-24 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f06ae145-36e4-3308-ad10-568c704c7a87 | -9.5748 | -45.232399 | 2026-09-24 00:38:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e8a37c0d-6b7e-3068-a726-13c0f0412e9d | -12.4091 | -46.951302 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f638bfc-c9a1-392b-8b33-1271e4f67d41 | -5.7738 | -45.096298 | 2026-09-24 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f443bc2-8ccf-3aa8-b5cb-08cf05af12f2 | -10.7565 | -44.811199 | 2026-09-24 00:38:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89c2a175-65f0-379d-b65e-84ab1350fbc8 | -2.127 | -49.519699 | 2026-09-24 00:38:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85f7f296-d689-3616-83aa-a46dd1d876ee | -6.2773 | -43.2686 | 2026-09-24 00:38:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99ec18eb-69cc-3026-821d-3707ed9e0f22 | -12.5099 | -46.986698 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e36a749-e6b3-3e67-83dd-7c1c797bf139 | -6.7809 | -48.677299 | 2026-09-24 00:38:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1590a0-d157-3e78-83b0-92f4e97f6fee | -4.2795 | -48.6073 | 2026-09-24 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c18b74ea-e84c-3ffa-9eae-9971845fe0b2 | -2.888 | -54.077702 | 2026-09-24 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5d58636-bd16-3346-87d4-96a10cee0b88 | 2.1593 | -50.8866 | 2026-09-24 00:38:00 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e5d92f15-666b-3569-bdc7-77782ba3206b | -5.783 | -49.183201 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9847abb6-668f-300b-9266-d619fa73248e | -2.8261 | -46.6954 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d99c6e8b-d5c6-3a0c-9ea6-35961087d1d5 | -1.2169 | -54.5439 | 2026-09-24 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bb1c6ce-3ca9-320e-873c-87e8146f2029 | -11.4901 | -47.353699 | 2026-09-24 00:38:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| caab7181-5834-3d49-806a-67ee416c25ae | -6.7794 | -48.670399 | 2026-09-24 00:38:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1207d659-634c-3ee2-9c8c-cca5b83fcc12 | -10.0945 | -46.0406 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac1a5e76-4584-3a88-b841-953cbd3c52d2 | -3.7074 | -54.2071 | 2026-09-24 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14d0989c-0bd2-311d-b4a8-6e7e308d7c3c | -5.5709 | -42.732399 | 2026-09-24 00:38:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4879c687-f8c4-3ee0-bf2c-8a074df74d86 | -10.0881 | -46.057301 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa269fb3-f306-3769-9a12-ed30bd3ceee9 | -3.1578 | -54.5914 | 2026-09-24 00:38:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fd5f0da-8f76-3bd7-834a-6564f5072cd3 | -12.1148 | -50.749699 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5560ecda-27b5-354c-99fb-f1e335f058ed | -8.924 | -45.9361 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d4537b4-d6d4-3b62-8c3f-cb249d0a673e | -7.1918 | -47.456001 | 2026-09-24 00:38:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96087a7f-6d07-3cf8-9052-564dadaea03c | -8.9073 | -45.908798 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f151ef6-854a-3251-bbc2-e920637fcff6 | -12.1648 | -47.3745 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 130a8c5a-14e0-3fc2-a1bf-f7ffc858d8f8 | 1.5768 | -55.931999 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 480b8c97-a124-3f89-ada6-6881c5905a7b | -7.4235 | -49.830299 | 2026-09-24 00:38:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 423e6c2f-b244-3dfb-b6d8-fd3840e23263 | -15.5685 | -42.362499 | 2026-09-24 00:38:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 24ca019c-17ab-3ca1-b6cd-fdb50f81af3d | -7.6793 | -45.472099 | 2026-09-24 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1377d07e-5936-30af-8843-f4557d7a106c | -12.6769 | -45.024399 | 2026-09-24 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 35bdf4dc-0b38-3be9-9886-5213282ee6f2 | -12.1085 | -50.816002 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c71b3f2-a5c8-3b49-93df-55f971f75d70 | -9.2382 | -47.382 | 2026-09-24 00:38:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1741a4d7-1989-364c-9095-5af09411f441 | -8.3537 | -45.617199 | 2026-09-24 00:38:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d8963b34-bbf0-367b-81b7-35e9d4cc1942 | -12.3495 | -48.199001 | 2026-09-24 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a279f8c9-19b1-338d-99b5-c23ff2ec4714 | -11.9642 | -50.763699 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32c4b8fa-174e-37e4-8552-613c11aa8999 | -6.5163 | -52.817699 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c8703b0-cea8-3964-908f-9a9e9be7b478 | -3.2104 | -53.368099 | 2026-09-24 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d411bebb-0821-38c9-b273-914b9259286a | -10.0976 | -46.0093 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec4e93c8-3a64-3e5b-afdb-1cdd85bfee13 | -4.2942 | -49.120499 | 2026-09-24 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5456b9a9-0a5b-3b14-867b-1c87402c0682 | 2.135 | -50.723202 | 2026-09-24 00:38:00 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 95a54ef0-37dc-3d56-9faa-c316d586fac6 | -1.6207 | -54.917599 | 2026-09-24 00:38:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef5944a7-1201-3dd7-9045-347f0eb89653 | -7.1356 | -48.424198 | 2026-09-24 00:38:00 | METOP-C | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77384cb1-1ce7-38ea-82a2-f06271679e78 | -5.3226 | -43.415001 | 2026-09-24 00:38:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b004937b-55a9-3186-a3ad-dfc759b49a35 | -6.4308 | -48.453499 | 2026-09-24 00:38:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3a982251-6c29-32f3-836c-d7d682ef6bd2 | -13.0667 | -43.271999 | 2026-09-24 00:38:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 207e77a0-fa82-39aa-a773-f06b272c5c9a | -9.235 | -47.368198 | 2026-09-24 00:38:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 217b9986-d42f-31e4-a1f5-7450cccae011 | -9.1486 | -49.952 | 2026-09-24 00:38:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48084799-6d19-3b0e-9f9d-78ab3f395b3c | -6.7175 | -44.158199 | 2026-09-24 00:38:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd285740-0a47-3b89-b480-74043d9a7ddd | -8.4559 | -48.699799 | 2026-09-24 00:38:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| dbc04bb6-b373-3783-9d4b-1826dbe01131 | -6.7152 | -44.1488 | 2026-09-24 00:38:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdc673cd-61a2-3002-b682-d68c3e63e896 | -8.7539 | -45.826801 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a07e4737-c1f2-335d-9ddc-1a1ceaae413a | -12.105 | -50.751801 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46d41073-25de-3865-8178-9d3906c5f6cf | -10.2078 | -44.155201 | 2026-09-24 00:38:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2718ba98-1c3d-32d7-9317-3bfdbcf20d38 | -3.4408 | -50.0769 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd9320de-608e-309c-9801-5d89c5ae677b | -4.0191 | -52.077499 | 2026-09-24 00:38:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd654cba-3092-39d6-8b09-998c29acfa24 | -9.407 | -40.304298 | 2026-09-24 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c86f8228-b7b8-35cd-80e9-eac7235c0617 | -6.5714 | -51.491501 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b26f5748-0cbe-35b4-ad97-0f6873e6e02b | -5.2573 | -49.2286 | 2026-09-24 00:38:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac7b2a67-a11e-34dc-9545-597920dac999 | -7.4643 | -44.563499 | 2026-09-24 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27e6b114-40f5-3fd7-b6ae-2424c1cafc52 | -14.0124 | -42.9034 | 2026-09-24 00:38:00 | METOP-C | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9cc95886-3f58-3fbf-9514-18bbc34ebbe2 | -6.5717 | -44.152901 | 2026-09-24 00:38:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 816d17ba-7a55-33e4-aaf0-7b4332eec14f | -5.7231 | -49.825802 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f15384e-e841-3e0d-a9cf-4854da5621c1 | -7.2687 | -45.526402 | 2026-09-24 00:38:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dbafc18-5114-342a-942e-be217c7bdb6a | -5.1926 | -42.959 | 2026-09-24 00:38:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 05449432-a107-393f-83e2-872084babdc6 | -10.4565 | -44.940899 | 2026-09-24 00:38:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| feecd83a-c6db-3670-a34e-af5c7e4ff152 | -11.7889 | -50.9505 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 148b6345-9cf3-3a3f-9934-83626b7cf87a | -13.0689 | -43.2808 | 2026-09-24 00:38:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0b6f9f8a-c440-3db3-89ba-2b95d8db64d0 | 1.5865 | -55.9342 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b506a50-fd21-3de8-a743-f94ac2e425bd | -7.4035 | -40.5797 | 2026-09-24 00:38:00 | METOP-C | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README14.md)
