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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cfc755f-8789-3b6b-8a80-9df42287006d | -14.7527 | -60.2321 | 2025-09-11 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| bfcc1f50-02b0-30a3-bd27-3a072210a84c | -22.6809 | -53.1309 | 2025-09-11 14:40:00 | GOES-19 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 121.5 |
| 1b435f63-98b0-3b33-9902-a7bd1ee77a02 | -6.5962 | -45.3822 | 2025-09-11 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 3726b101-3015-3e78-99ad-da74df0c31e5 | -11.4845 | -43.6402 | 2025-09-11 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 56f17b24-9fa1-30dd-a98e-096ae8a2379c | -6.485 | -45.2554 | 2025-09-11 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 3cdcf915-abe7-32f8-958e-f23093fbf58d | -12.9292 | -54.7538 | 2025-09-11 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 6c6ff794-4005-3e60-a52f-a7fec6bf426d | -7.4159 | -45.8761 | 2025-09-11 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 87226b3f-1284-3bc2-adf5-20b23a36b6c2 | -13.49 | -51.7688 | 2025-09-11 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 2c736c9e-d9d3-307a-af4a-63a717d71b40 | -9.0361 | -45.7603 | 2025-09-11 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e92c56d1-f664-3f3c-9bb5-659ddeae2b43 | -9.0358 | -45.783 | 2025-09-11 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 07d0a240-59aa-365d-864e-dbdcf8a30160 | -7.5215 | -48.2753 | 2025-09-11 14:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| b116214d-a247-3196-9e8b-bd7db4204823 | -12.1658 | -48.4811 | 2025-09-11 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| dce21a25-f5c7-381e-a908-7150247c07f7 | -5.414 | -45.8958 | 2025-09-11 14:40:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| f50e5f6d-4ff0-313b-a8a5-ea088f0779ef | -11.4281 | -43.578 | 2025-09-11 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.8 |
| 43a73529-e7fc-3a57-b277-53936957e473 | -9.976 | -50.3334 | 2025-09-11 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 163704cb-ae03-3e78-a9f2-97f9bbea1760 | -9.075 | -47.1002 | 2025-09-11 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 213.3 |
| fe1e0348-9663-35bf-a3b7-06098e34b650 | -8.994 | -46.0808 | 2025-09-11 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 245.5 |
| a13154fd-8c0d-3c4a-b84f-be0cb56c12b5 | -12.8448 | -47.9682 | 2025-09-11 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| caf4bc21-f79d-3ac4-8b56-5b59c0cdea27 | -8.9752 | -46.0829 | 2025-09-11 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.0 |
| ea8f915e-8af7-3374-86db-bf00261a7ac9 | -4.553 | -43.7439 | 2025-09-11 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 891c04e9-dd86-3311-b8aa-7756362353ef | -12.921 | -48.0018 | 2025-09-11 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| dd23e8c2-457d-349b-b8ad-147ce5cd0aa0 | -8.5086 | -45.7033 | 2025-09-11 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 49789bc7-84f9-37cc-9a1f-75e3ac320888 | -6.3801 | -44.4893 | 2025-09-11 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 116462c7-6e5b-3b22-a9b1-f3b122d6d083 | -10.0695 | -50.3881 | 2025-09-11 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 136.4 |
| ed3660be-3bbb-36f0-852c-083fb22230f2 | -9.0129 | -46.0788 | 2025-09-11 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 249.3 |
| bb8bb3c7-c0bb-3c65-9dac-e201b85f2abd | -12.8256 | -47.9709 | 2025-09-11 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 73113611-bec5-3323-a0d0-d873f57ffa32 | -11.7786 | -46.5047 | 2025-09-11 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 21c09a55-8a37-389e-b277-cac7c480dffa | -5.642 | -45.4087 | 2025-09-11 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9d56f884-29f3-39ec-91cd-c35cce46a2e5 | -6.3041 | -53.4562 | 2025-09-11 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 97d07995-009e-325e-9191-5f0f71b55b23 | -7.4636 | -44.9661 | 2025-09-11 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 2a54d683-be13-3a1d-9242-69a9341832f5 | -6.3735 | -45.1736 | 2025-09-11 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c96f1e69-d054-3591-9d92-ef5b24fbc08b | -14.7524 | -60.2519 | 2025-09-11 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| bfe058a4-92c5-3700-8c3d-a88a35660396 | -9.0565 | -47.08 | 2025-09-11 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| e0957439-dfb9-32ad-970f-325d1ea4974f | -6.3158 | -43.4081 | 2025-09-11 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 4628b900-347a-36fd-aa9c-b4bfeb04fa7f | -10.3885 | -50.5264 | 2025-09-11 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 153.9 |
| c832fcd2-4e8a-3154-a860-3747b5b68e6e | -14.5128 | -53.9158 | 2025-09-11 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| a4931b54-d63e-3086-a2d2-91b1b6dcc07b | -10.7366 | -46.1011 | 2025-09-11 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 3c0410d0-e5f7-31e3-a44e-0345e17a5b1c | -9.0567 | -47.0577 | 2025-09-11 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| fe014258-e31f-3cf8-b00e-03e05d952a1e | -8.1101 | -49.2634 | 2025-09-11 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 12dfe49a-8771-31cd-983f-f9cdb7d04dc9 | -11.4473 | -43.5751 | 2025-09-11 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 4cfa9d20-d571-3bef-a84e-294a1dd3e8ed | -13.9038 | -47.9675 | 2025-09-11 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 8c20d54a-eb81-3842-9c7f-71d668057cb5 | -15.8006 | -52.2687 | 2025-09-11 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 275.6 |
| fee9a596-8dba-3b51-adee-55f817900c73 | -6.5038 | -45.2539 | 2025-09-11 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 5decfa7a-b3b9-3087-b208-5b1ed1014396 | -9.7634 | -47.8447 | 2025-09-11 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| d2c0a99a-feaf-32e8-880c-82c4f2f15260 | -5.8582 | -44.2088 | 2025-09-11 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 0a160f28-ea32-31c7-9f82-016c3789fc59 | -9.0753 | -47.078 | 2025-09-11 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 44969b71-db60-39e3-97d4-a05d1055e57f | -11.4285 | -43.5544 | 2025-09-11 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 417.7 |
| 83283cfc-7205-3802-9b05-e022d6d6ff2c | -17.3372 | -46.6718 | 2025-09-11 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 72afad42-c298-3721-8643-a51c1ee0f11c | -9.0605 | -49.8014 | 2025-09-11 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 95135460-e61f-3ee9-8522-d8a0653fc171 | -12.9482 | -54.7519 | 2025-09-11 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 0acccc76-8cad-336e-8396-ae82d319ce37 | -15.5628 | -54.7453 | 2025-09-11 14:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 520485bd-09ca-36c9-9ec4-21a45be5199f | -16.6335 | -49.7683 | 2025-09-11 14:40:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 3efc2a2e-cba3-37f0-be9f-f7678ba9caa5 | -6.9131 | -45.5368 | 2025-09-11 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e7312563-9f0e-3dee-b58b-af467d6a9771 | -11.4661 | -43.5959 | 2025-09-11 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 1c3017e0-7973-3086-be37-e00dc62ef9c6 | -15.3423 | -52.8855 | 2025-09-11 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| d1780dd7-1362-3f41-b43c-9d25572b0d7b | -10.6606 | -48.6218 | 2025-09-11 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| e9a49ba9-f4f7-3e54-b373-da3e944c6cc6 | -9.8838 | -50.1719 | 2025-09-11 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 75e2c62e-74df-3220-9878-4d40ad6e5a8e | -14.7334 | -60.2337 | 2025-09-11 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 11340b56-ce2e-3581-9929-e05e9c711a2e | -7.4349 | -45.8519 | 2025-09-11 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4335c191-cb4c-3c06-baad-081941e6f890 | -9.0262 | -49.5261 | 2025-09-11 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 3d2f6de9-ff02-3cbe-bb66-92fe7498824a | -6.9451 | -44.2803 | 2025-09-11 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7164aaa3-fff1-3cda-82b1-3d6b0bce4523 | -17.3366 | -46.6951 | 2025-09-11 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 0860b7e4-1cb3-3539-8cbd-f0f288e31638 | -11.3718 | -43.5157 | 2025-09-11 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 258b8a99-4c38-3afc-838d-88ef26fca46e | -10.1657 | -46.1724 | 2025-09-11 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 9afcc78a-353a-34b6-85a7-78897e7c6767 | -14.3875 | -60.3015 | 2025-09-11 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 62f1d72a-6d4c-3080-a2f3-0584e01ab101 | -6.4364 | -44.4847 | 2025-09-11 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| afdfb8c0-f61a-317e-acfd-f1174fa91ea0 | -6.1705 | -41.0658 | 2025-09-11 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 743e2c99-336c-3bfa-a5d4-9d65136d09b2 | -8.3114 | -44.9052 | 2025-09-11 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 68a94726-0daf-3c4d-9023-37e236516eb9 | -11.0997 | -48.4392 | 2025-09-11 14:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| d63b75b1-3c51-321e-b6b9-c6fb20f39543 | -15.1211 | -50.1438 | 2025-09-11 14:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 1240a25f-c084-3a87-8854-7663f5cc0e24 | -5.4719 | -43.4278 | 2025-09-11 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 99466fce-fd8b-3d75-927a-78dcf81ea0a6 | -6.6652 | -44.1205 | 2025-09-11 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 037ed5d9-4f77-3fde-b500-c9a5e87b7cf2 | -5.858 | -44.2319 | 2025-09-11 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a81ace6e-9f40-326c-b410-dfd87c48a284 | -8.1103 | -49.2419 | 2025-09-11 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 00c87588-48f8-3d72-a982-f241437472eb | -7.5028 | -48.2769 | 2025-09-11 14:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5590c446-b31b-3f12-b94a-e47650d06642 | -9.1514 | -47.0257 | 2025-09-11 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| db3d2f3f-4467-3627-8f8a-a44776a573e9 | -9.0547 | -45.7809 | 2025-09-11 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 11da9019-1c33-3bf3-8dd7-e1511649f8a4 | -5.6607 | -45.4074 | 2025-09-11 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 680755a9-d58c-3561-b49c-98b770ace8eb | -8.8758 | -49.5399 | 2025-09-11 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| c5c9e054-00ca-3417-baa9-ad7f93dbfcd6 | -7.4161 | -45.8536 | 2025-09-11 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 5b6b5a80-293a-3ff2-a859-4a4effaefea2 | -9.7445 | -47.8468 | 2025-09-11 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 377a5693-b24e-3752-919e-1e125535b68b | -15.1697 | -56.3576 | 2025-09-11 14:40:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 2ea21420-7bc8-3e51-afbd-c4dd2788e245 | -7.5592 | -48.2505 | 2025-09-11 14:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 785c6a46-366d-325a-b5ee-27ee7331db0e | -13.241 | -51.7571 | 2025-09-11 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 07688ba9-6b1e-3bd5-9c0a-1f9482a9dcad | -13.2606 | -51.7335 | 2025-09-11 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 226.5 |
| a4151049-b66a-377e-92cb-d9f046c96315 | -11.4849 | -43.6166 | 2025-09-11 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 86856b4f-6483-35d7-bfcd-8c1f4fdaa2bf | -11.1689 | -45.2914 | 2025-09-11 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| f2aa7066-c55f-3f09-b1fb-533226e063af | -9.0976 | -49.8408 | 2025-09-11 14:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 269.7 |
| bb1d7b19-c8f8-39f5-96aa-bc6a9cc11067 | -9.5454 | -45.8389 | 2025-09-11 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 52adbdc8-c582-3da5-9854-3ab6ddb67835 | -6.9319 | -45.5352 | 2025-09-11 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 4a89166d-fb96-3606-8a88-03c2bc9d0e02 | -10.6793 | -48.6415 | 2025-09-11 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 3db0b96e-50fb-32de-902e-8a911789c55c | -22.3232 | -48.8249 | 2025-09-11 14:40:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 279.3 |
| c747211f-1ae0-317d-b7b6-b280b8843aac | -9.0979 | -49.8194 | 2025-09-11 14:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| f794615a-8844-3b25-a053-21c236efb42f | -10.1844 | -46.1927 | 2025-09-11 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| dbb83b34-41c8-3605-9783-c21387372b6b | -8.8755 | -49.5613 | 2025-09-11 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| e3a84817-1b65-3dba-80cd-f46c042bf614 | -7.559 | -48.2723 | 2025-09-11 14:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 270677a7-8f6b-34ba-ab8c-c225750a784d | -14.5125 | -53.9367 | 2025-09-11 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| ae3be64c-036a-33f7-9ee9-cfb50812bf7f | -10.203 | -46.213 | 2025-09-11 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 227.7 |
| efe63bf8-aedb-34a9-b542-4f8b7efc7224 | -10.8594 | -45.5622 | 2025-09-11 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.9 |
| c90e97c2-c5ad-3ae2-9f6a-27b997fa19e6 | -15.6929 | -47.0354 | 2025-09-11 14:40:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 102.1 |


[Clique aqui para ver as próximas entradas](README150.md)
