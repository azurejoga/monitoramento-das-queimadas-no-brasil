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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 792556f3-3c15-3c34-ab93-e2f7ccf14f87 | -6.9444 | -44.3494 | 2025-09-02 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 07f3cef3-b644-3284-8397-a1d5e294674b | -9.4984 | -46.4973 | 2025-09-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| dc38c37d-da6f-3b63-aaa2-bf1013c94df2 | -9.1207 | -61.4864 | 2025-09-02 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d5e68eef-331f-3ba7-b2eb-7af5da100e7a | -12.5769 | -44.7814 | 2025-09-02 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| c0e16242-fa08-3281-813b-0259d4887025 | -11.3692 | -43.6577 | 2025-09-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 75d48397-7bbb-3d41-80d4-fcac8bf4beb5 | -10.7688 | -45.2769 | 2025-09-02 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2e799fb4-5fab-33b0-b00f-ab6854524b17 | -5.717 | -45.3809 | 2025-09-02 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 17bd6dcf-b2d7-3f1b-9b1e-500d56444d8e | -10.062 | -48.1197 | 2025-09-02 14:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 8abd074b-a5ef-3c65-8ff5-70cd265f9609 | -6.185 | -43.3491 | 2025-09-02 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 164.8 |
| a3934609-f96c-3f34-8f9a-68b45e6befc0 | -6.8281 | -52.8143 | 2025-09-02 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 9dfd75d9-68b0-36d3-86ff-8fed95a0028b | -11.4491 | -46.7973 | 2025-09-02 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 6cf8b07b-e886-3f05-8a00-a2685f8f6a79 | -7.5292 | -61.3254 | 2025-09-02 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 0420f7da-5215-382f-9537-3a6cf28cf9b5 | -5.6983 | -45.3822 | 2025-09-02 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3ee3f235-5a30-3000-ad9c-6c606ba0a228 | -9.7483 | -48.9814 | 2025-09-02 14:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 181.4 |
| e03b7de0-8cc2-36df-baf9-15ed9d9a60fc | -7.9351 | -46.4559 | 2025-09-02 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 44a114f2-3c3f-37db-8e29-c55402a403c3 | -6.982 | -44.346 | 2025-09-02 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f66e414a-7116-37b8-b724-182ff7610f68 | -5.8642 | -45.6408 | 2025-09-02 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 88fcd697-24f1-385b-8f38-a5972f8a2621 | -9.4794 | -46.4994 | 2025-09-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 2eec4585-92c6-352b-bdea-d9a6797e9b5f | -12.0069 | -51.3298 | 2025-09-02 14:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 3dcb47ab-af32-330e-ab63-47e4d1e29097 | -6.2036 | -43.3709 | 2025-09-02 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| e9456c5f-3561-36c4-97ed-ca252bcd83f4 | -7.484 | -44.8272 | 2025-09-02 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| dac527c0-a202-3727-900c-823a69d31c6c | -10.0623 | -48.0978 | 2025-09-02 14:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f33c74ee-cdca-364e-9089-5ff0f19d0a45 | -12.9192 | -56.9873 | 2025-09-02 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 188.4 |
| cd8bb9f1-5db9-357e-9ef3-2e157efaff0e | -6.2038 | -43.3475 | 2025-09-02 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 272.4 |
| e67b814d-69de-344c-ab56-bbf16bf5a1a1 | -11.9415 | -50.6131 | 2025-09-02 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| fab59510-2b36-339f-926f-c1bb3202d800 | -6.666 | -45.8946 | 2025-09-02 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2d642678-1e33-3e30-a14b-141d568295e6 | -8.6132 | -62.5739 | 2025-09-02 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| ac7aff08-38e0-3994-a507-59e76a13d77b | -6.3432 | -42.5602 | 2025-09-02 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| a96d19dd-a950-3944-8145-b8becd4d9c48 | -7.1091 | -44.7474 | 2025-09-02 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3d7a283b-1709-36ad-aef1-7a71f1bda923 | -11.9879 | -51.332 | 2025-09-02 14:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 63407ced-9c66-35e6-adb4-c8f7bfd44218 | -6.204 | -43.3241 | 2025-09-02 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 0bafc723-017e-3908-9a37-685d112585b5 | -5.8882 | -42.9988 | 2025-09-02 14:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 139.5 |
| 74c911f0-561e-3bba-b036-3ab90cf27f24 | -8.7438 | -62.4169 | 2025-09-02 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 3f0517de-45a9-3ef9-a7ed-b9bfcb59d00b | -11.6715 | -52.21 | 2025-09-02 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 6067398d-c133-34a3-9189-caa1969ecdc9 | -12.9197 | -56.9471 | 2025-09-02 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| e9a319c4-685c-399b-a9a3-a54570134b92 | -11.6647 | -57.3533 | 2025-09-02 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 924d3a02-b685-3c22-b180-3a79c3a389b6 | -8.6883 | -62.4002 | 2025-09-02 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 5a57b9cd-a0e1-3b4b-92cb-4eb023d0e3d2 | -8.2008 | -49.5345 | 2025-09-02 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 29b51501-ae4f-341f-825f-8c207c8b551c | -6.9817 | -44.3691 | 2025-09-02 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 84eb9a86-4c1b-3759-84a9-e1615ea97593 | -6.9629 | -44.3707 | 2025-09-02 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 9ac8a489-b770-3689-b48a-09a03f7920fd | -6.8095 | -52.8154 | 2025-09-02 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b7bfcfe4-d462-3137-8dbf-e5c4ca049852 | -9.7294 | -48.9834 | 2025-09-02 14:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 93815915-d42b-3f80-9b20-b0d78a6cfd66 | -8.7622 | -62.4351 | 2025-09-02 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 6d1384fd-1078-3160-bf57-0179a4c37466 | -4.9122 | -43.2103 | 2025-09-02 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 5377ff74-d4cd-3533-b0a0-13b6257a66c3 | -11.8053 | -48.3518 | 2025-09-02 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 4afda175-5598-3995-90b6-e545aa2feb68 | -7.9624 | -63.2218 | 2025-09-02 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 8609cef3-4bae-3890-b015-e70ac3915f5a | -8.6673 | -62.8369 | 2025-09-02 14:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 2ef9b9c9-04f3-36f0-8d70-1bcfc5829057 | -5.7357 | -45.3796 | 2025-09-02 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 1be20372-5715-32e2-a438-73ba825155fa | -6.3432 | -42.5602 | 2025-09-02 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| a8d31f08-215a-38b6-98bc-cd34d9f9f532 | -11.653 | -52.17 | 2025-09-02 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 9075631a-2b33-31cc-a978-7328b0362de9 | -5.97 | -44.2693 | 2025-09-02 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d62b6318-d5aa-3f8b-b24d-b2c8fc1f4031 | -6.2038 | -43.3475 | 2025-09-02 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 20751752-fd36-3b9c-b33a-03f8bd412bb8 | -11.6527 | -52.191 | 2025-09-02 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 5284a4c9-3973-3eb1-a3e0-ca2b75e62fa9 | -11.3893 | -43.6075 | 2025-09-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d06c8fd2-3fe8-3168-b1b7-cbeb4f267d91 | -6.1853 | -43.3257 | 2025-09-02 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ad711214-a36a-39d0-a5d0-75f16a95b03f | -5.8694 | -43.0003 | 2025-09-02 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 126.4 |
| 1f89310b-de8c-3adf-8197-3fdeb1e96e43 | -8.02 | -44.084 | 2025-09-02 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 05089a03-c5d7-31bf-9837-3ac9158ca0a1 | -6.666 | -45.8946 | 2025-09-02 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 46d094a5-b665-3701-bcbd-3f39c88f7eb6 | -7.5477 | -61.3247 | 2025-09-02 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 245.7 |
| 3635d565-c909-3936-b6e5-e5afe0b5a2a7 | -8.2198 | -49.5115 | 2025-09-02 14:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 7ffa5325-5a2e-319f-b7a4-5f6729137293 | -6.3504 | -45.6273 | 2025-09-02 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 7d0543ba-e8da-362c-827f-89b7f7fb4d20 | -8.2008 | -49.5345 | 2025-09-02 14:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| e31e4597-0828-36f2-b35e-a099e365ab62 | -11.3901 | -43.5602 | 2025-09-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 37db6bc2-421e-35a0-bf2c-d7d6886ded5a | -6.2036 | -43.3709 | 2025-09-02 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 63d23f4e-579b-38ab-b01f-7850fbad5cdd | -6.1848 | -43.3724 | 2025-09-02 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5d3851d8-187d-3739-a596-0bd18649d2ca | -6.3506 | -45.6047 | 2025-09-02 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 053adf61-e695-338c-876a-e546d9ae6257 | -11.853 | -51.453 | 2025-09-02 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ac6c75e1-5191-37b0-b4c7-0790d20ea9fe | -6.2794 | -43.2945 | 2025-09-02 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 51e3b905-0450-37ee-bc17-366690d9e8cc | -7.1089 | -44.7703 | 2025-09-02 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 703f74bd-6bf7-3f5a-b50e-946cebcef7cc | -11.672 | -52.168 | 2025-09-02 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0d507c4c-7670-3e6c-9810-af9de70e498e | -11.1037 | -44.6315 | 2025-09-02 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 181.3 |
| ce995e45-c868-3ac6-813c-db7a4eae3c19 | -11.9224 | -50.6153 | 2025-09-02 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| cbfba4d4-5f6c-3d14-acc3-efd17cfd6646 | -9.4981 | -46.5197 | 2025-09-02 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 31a4fa38-beb0-353c-b719-56fa0b6a1391 | -8.8854 | -45.7314 | 2025-09-02 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ee89ec8a-169a-3f4a-8998-fc14f6a14a16 | -4.9124 | -43.187 | 2025-09-02 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 641fba62-42c2-3412-8952-aa6a4ba7d73a | -6.3319 | -45.6062 | 2025-09-02 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 13c54db6-fad8-3bd0-8569-b87910362779 | -11.0841 | -44.6575 | 2025-09-02 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| f8be3961-f3b7-3f36-9d5d-568fc20e9005 | -9.7483 | -48.9814 | 2025-09-02 14:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 15c6c83f-2c04-3bcc-801a-6c480ad1e0a1 | -5.8692 | -43.0238 | 2025-09-02 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| c5fc90b4-9abc-3a52-b323-dcef2d83a45f | -6.982 | -44.346 | 2025-09-02 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| a8c3d69c-34b8-3ead-b5f1-bc957a3adf49 | -11.6647 | -57.3533 | 2025-09-02 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 86ba561c-3b3b-3c13-a326-d4e0d5198761 | -11.9415 | -50.6131 | 2025-09-02 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 6e4e7910-5c5d-3033-9572-e3fe85831759 | -7.9351 | -46.4559 | 2025-09-02 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a9413979-8d9d-3c48-802c-bcd2f03ae4ba | -11.1033 | -44.6548 | 2025-09-02 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 368.2 |
| b7b6bf8a-383b-383a-9890-d5bf6caf5fef | -8.6883 | -62.4002 | 2025-09-02 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.9 |
| e3b2fd22-6613-3861-b085-e1fcef3cee81 | -7.9163 | -46.4577 | 2025-09-02 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 5abbbf0e-1fb8-308a-b765-9f44387f309e | -10.8947 | -50.8356 | 2025-09-02 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| f1f327f2-4edf-3ded-929c-e7fa913b2e74 | -9.4794 | -46.4994 | 2025-09-02 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 18adab8f-9793-35e6-b3ac-8768afcdb689 | -9.4791 | -46.5218 | 2025-09-02 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 674.3 |
| 608eb078-d57d-3b10-a1f6-807f12c43af5 | -5.8642 | -45.6408 | 2025-09-02 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 21ff398c-728a-3fd7-83d1-bda9d695982a | -5.7866 | -43.8453 | 2025-09-02 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 275b820a-9db2-3da1-b8fe-d6b6cca0933b | -7.5476 | -61.3437 | 2025-09-02 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 214.5 |
| 019545c6-527a-3b5b-955c-5e7858141d21 | -8.3291 | -44.9948 | 2025-09-02 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 664a2f7b-f311-3c6e-999d-1ecf2e596798 | -16.2953 | -52.9443 | 2025-09-02 14:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0d42bc4e-d90e-37f4-af8f-b02526974fcb | -6.9629 | -44.3707 | 2025-09-02 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 4eccef18-2ad6-3463-b821-8a080ee0431d | -5.8644 | -45.6183 | 2025-09-02 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| e09dc7b5-6999-38bc-a1c4-667b2eb26c2f | -8.6169 | -61.9473 | 2025-09-02 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4b5544f9-047b-3b61-ad0b-0e7ec6ebdf81 | -10.062 | -48.1197 | 2025-09-02 14:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 2d8e6254-bc95-368b-8f0c-6a0a9a17b4f8 | -8.5943 | -62.6315 | 2025-09-02 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 91814b18-2e28-377a-9d5a-8f0632f5a536 | -11.3907 | -46.8724 | 2025-09-02 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |


[Clique aqui para ver as próximas entradas](README100.md)
