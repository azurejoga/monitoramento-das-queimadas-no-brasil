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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56d48061-033b-3d6b-9ff7-23a22a96e985 | -10.8269 | -46.4058 | 2025-08-24 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 98197568-24fc-33d8-9542-3467c62b5f68 | -10.8078 | -46.4083 | 2025-08-24 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 7caff863-ac44-3040-a234-3001b08f24b4 | -5.663 | -45.136 | 2025-08-24 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 12c8478e-3276-32f2-9461-ffb2037b69bb | -9.1536 | -59.464 | 2025-08-24 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| fc5af8b1-f1a5-384a-b9bd-a0c484f8416a | -8.0652 | -44.9989 | 2025-08-24 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| f85aa381-a974-341c-a95c-3bd514237aa8 | -5.6628 | -45.1586 | 2025-08-24 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 70e720e5-9ad5-346a-ba6d-d650a68a1a97 | -10.4777 | -46.8758 | 2025-08-24 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b000eec4-d659-3991-b273-31ca31da2c74 | -5.663 | -45.136 | 2025-08-24 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| a17b5d6e-4628-3665-aabc-693853703ea0 | -5.678 | -41.3987 | 2025-08-24 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 219c4c05-c110-31da-9621-442713402ba9 | -11.5251 | -50.4898 | 2025-08-24 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| cd6fa2df-70e4-3401-8f40-12b74a517077 | -8.0652 | -44.9989 | 2025-08-24 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| be5d4008-6c8e-3abd-bd1c-b955cc257549 | -7.9631 | -63.071 | 2025-08-24 12:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0b3ea11c-4cf2-37a0-98d4-cd2a635ea8bb | -8.0685 | -49.6524 | 2025-08-24 12:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 262f75d1-f185-34ed-83e4-ca7305ea87df | -6.7876 | -44.9807 | 2025-08-24 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d0b7f195-34a9-3d57-b58e-44ae46c735d4 | -6.1963 | -44.1134 | 2025-08-24 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 08bbe9e5-5ec4-374c-8a81-33498eaa0188 | -10.416 | -47.1955 | 2025-08-24 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2d631e58-d0ca-3723-9526-1be26678c238 | -11.6112 | -46.2337 | 2025-08-24 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 30ca18e4-a7c2-394b-a0e1-6f73c9a20a2f | -8.4833 | -49.4032 | 2025-08-24 13:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| ce492a21-c7c5-3011-a9e4-080187a1daad | -7.9225 | -45.9193 | 2025-08-24 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 38c7fb95-f4c4-39e0-ac9a-9829763cf4ef | -7.9631 | -63.071 | 2025-08-24 13:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6ae15ef9-666a-32bf-9547-6a24cba600d5 | -8.0655 | -44.9761 | 2025-08-24 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0ada8f17-f438-3429-805e-367b332b2f60 | -8.0464 | -45.0008 | 2025-08-24 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 58f5288d-6345-3bff-aa5e-c498860e9136 | -5.5858 | -43.2562 | 2025-08-24 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 6ebf19b8-aa9c-369b-899f-bf9f95ba1279 | -11.5921 | -46.2363 | 2025-08-24 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 73df9cc5-cb93-30a2-8447-db563f7691dd | -10.6006 | -50.2058 | 2025-08-24 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 12010dfb-02e4-3358-a9ad-3e9b982c2e14 | -10.4777 | -46.8758 | 2025-08-24 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 0d35064e-c863-3ef2-9dbf-190e8f7f9b12 | -10.8269 | -46.4058 | 2025-08-24 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1f8da341-0196-3af5-ae8b-f5a5bf9eafcb | -2.2646 | -47.8617 | 2025-08-24 13:00:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 13af6332-162d-39d4-8ded-0a90a8022b2b | -5.6628 | -45.1586 | 2025-08-24 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9121d34c-6b1b-333e-b272-f8982f759ae5 | -10.4784 | -46.831 | 2025-08-24 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d53c1714-b1a9-37ca-b53a-e37e3cb05d83 | -5.663 | -45.136 | 2025-08-24 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| f186e878-7d2e-3037-918d-d3a5400b5434 | -10.4974 | -46.8287 | 2025-08-24 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 78ed76e8-72f1-3817-a957-4e3817b47607 | -7.185 | -44.6719 | 2025-08-24 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 6ed20643-4fa9-3bd3-a31e-1bc048059361 | -10.478 | -46.8534 | 2025-08-24 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 239.0 |
| df5c6231-1de7-3dd7-a703-eb292bc93801 | -6.3698 | -45.5582 | 2025-08-24 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0ab03c63-5c6a-3824-92c1-f36bae64df80 | -8.527 | -48.8609 | 2025-08-24 13:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 78504668-88ad-3047-b92e-1c3bc6c7e3e8 | -11.6112 | -46.2337 | 2025-08-24 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a199580a-aef6-3a8e-b5dd-0a38511feb1d | -5.678 | -41.3987 | 2025-08-24 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| 5057f3dd-cd72-32ad-8b88-baad643f89c6 | -8.0652 | -44.9989 | 2025-08-24 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 206.8 |
| f931d403-91bf-38dc-a31e-e8890b98e825 | -11.5251 | -50.4898 | 2025-08-24 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| e623e9b3-e7e9-3019-b9f0-8704c581e938 | -10.8075 | -46.4308 | 2025-08-24 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4810dcf2-f76f-3431-94af-feee2dcc689a | -8.0685 | -49.6524 | 2025-08-24 13:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 3ed35f65-9f4a-3a17-8316-85bed7af2418 | -11.5921 | -46.2363 | 2025-08-24 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 02271fdc-7881-36b2-9a7d-1b81dc104789 | -8.4833 | -49.4032 | 2025-08-24 13:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| a34dba55-f6b7-3edf-bd95-1cdb4bb14086 | -11.6112 | -46.2337 | 2025-08-24 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 8f8b4bc1-8dd8-3871-a0b5-44fa7b11e091 | -13.5162 | -47.0393 | 2025-08-24 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 1e67f6a9-4283-39fd-abb1-b386041f97dd | -8.527 | -48.8609 | 2025-08-24 13:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 4b6cc816-a16b-3e52-b0ad-28a29352e94e | -5.663 | -45.136 | 2025-08-24 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ddae0677-f13f-3b98-9137-e236d6e50026 | -6.3431 | -44.4465 | 2025-08-24 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| d406ec61-deb1-3c2a-ba72-eb44955c4be0 | -10.8075 | -46.4308 | 2025-08-24 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 4aee70b3-1d4c-3ff6-aad3-5fb05e44ebc0 | -10.6006 | -50.2058 | 2025-08-24 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| bdd10f5a-9eba-3243-bb51-89e8517d02fc | -14.1462 | -53.9802 | 2025-08-24 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 9e531ac4-71db-370f-872a-f2866a04b4c1 | -10.4584 | -46.9005 | 2025-08-24 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| e7e76cdc-7561-316b-be73-9c600b8da7a0 | -5.6628 | -45.1586 | 2025-08-24 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 5cc57618-0d03-38ea-ba79-ac5890aab959 | -8.0685 | -49.6524 | 2025-08-24 13:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 8ff2d3e3-131e-3206-9c2d-1d489a9e4374 | -10.4774 | -46.8982 | 2025-08-24 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 7b7f6448-1b3f-373c-8e41-ea62929a8cb1 | -10.4777 | -46.8758 | 2025-08-24 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 33abc6e8-3ff2-36c5-854e-56ac9ba3014c | -10.478 | -46.8534 | 2025-08-24 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 421ab8eb-8998-3d14-9244-1dc1b67d1f17 | -11.5251 | -50.4898 | 2025-08-24 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| c8931ad6-4159-3926-bfeb-55772e93402a | -5.678 | -41.3987 | 2025-08-24 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 8b045855-1cf4-31ca-b136-965199732041 | -8.5458 | -48.8592 | 2025-08-24 13:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e0cbc854-436e-3add-b5ba-6cc778e420f0 | -11.5921 | -46.2363 | 2025-08-24 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| da640352-4ba4-335e-8304-4586aac7a15f | -6.3431 | -44.4465 | 2025-08-24 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 5ad5d711-707b-3aa9-bbed-da1e0e4112c9 | -6.4357 | -44.5535 | 2025-08-24 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 39f1c384-abe4-3c92-9d66-79159d57ee7a | -2.2646 | -47.8617 | 2025-08-24 13:20:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 408a9c21-6c3c-34b4-a68a-6662f9dfd563 | -10.478 | -46.8534 | 2025-08-24 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 88664ec6-ce28-3b5b-84d8-e4027480a5bd | -5.6628 | -45.1586 | 2025-08-24 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2623b599-089c-3c2d-9a5e-a4710ae649a4 | -11.6112 | -46.2337 | 2025-08-24 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| b4e9891a-1d93-3bf7-9771-25194c59156b | -8.546 | -48.8376 | 2025-08-24 13:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8641fa46-85ca-3307-8adb-d081482b3a27 | -10.4777 | -46.8758 | 2025-08-24 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 3ffcc674-6655-3f09-9793-553c7990ebe2 | -10.416 | -47.1955 | 2025-08-24 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 3cb6e300-b8db-35ea-a175-eaef8d224980 | -5.678 | -41.3987 | 2025-08-24 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 150.7 |
| a2ea3451-6a31-3eb6-b3cb-0f71388f889f | -8.4833 | -49.4032 | 2025-08-24 13:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 7241c98e-79c9-3ca6-a2fe-78e8d166e868 | -8.0652 | -44.9989 | 2025-08-24 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| f0406bf9-bf30-3bc3-bb00-212d2c3bc5e1 | -5.663 | -45.136 | 2025-08-24 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 73d2797d-4e41-3980-9231-9a032545c303 | -10.4164 | -47.1732 | 2025-08-24 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| ffe0d70f-7d36-3f88-ac59-1bdb600c78df | -10.4584 | -46.9005 | 2025-08-24 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 9a7fbb8e-352c-3b63-a678-544bdf2bab88 | -8.7378 | -45.4753 | 2025-08-24 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 04974418-450d-3e23-9601-7634c9c130af | -13.5162 | -47.0393 | 2025-08-24 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| bf749be7-2f9f-3b42-a656-1f9011fdbb7d | -11.5251 | -50.4898 | 2025-08-24 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 169.3 |
| d5bb78f2-9893-3540-b549-8ea81e93a730 | -10.6006 | -50.2058 | 2025-08-24 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 45c0fc0b-2697-3ea3-8598-d6062455cf85 | -8.5458 | -48.8592 | 2025-08-24 13:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 84419bea-b674-3c2b-a10f-f14e1421c8e0 | -12.6748 | -47.8143 | 2025-08-24 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 202ef305-0a86-35f0-97af-3e910c6a815c | -10.4774 | -46.8982 | 2025-08-24 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| c7997680-6a2a-3457-bf5f-202edf800e4b | -5.663 | -45.136 | 2025-08-24 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| df494494-bb54-3e45-84e2-26fcb6259fc9 | -10.416 | -47.1955 | 2025-08-24 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| d6bed943-a365-32e5-a692-277254ccec6c | -12.6745 | -47.8366 | 2025-08-24 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c40e7772-bd39-3321-93bb-c4361dc25e26 | -10.6006 | -50.2058 | 2025-08-24 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 3d98e1e2-c086-399d-b552-078fbda6da11 | -12.6748 | -47.8143 | 2025-08-24 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 49e2ab61-287d-382a-93bb-99f72e7fabdf | -13.4995 | -46.9063 | 2025-08-24 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 6648ce3f-9e51-300f-bc7c-6d361182cc4a | -5.678 | -41.3987 | 2025-08-24 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| 27b84df1-5b9b-3acb-a7a0-6f08f1c24a55 | -8.0652 | -44.9989 | 2025-08-24 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 71a1de0b-1b2d-3ed9-ae9d-d31a1380c2b9 | -8.7378 | -45.4753 | 2025-08-24 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 8a59abb8-b44f-334b-9ccc-567c5ec7af0d | -5.6628 | -45.1586 | 2025-08-24 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| d285aa26-b9b3-3505-b37b-1c16471bd964 | -6.436 | -44.5306 | 2025-08-24 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| fa387e9a-2e86-36ce-a6fa-5cca15c53ba9 | -13.5162 | -47.0393 | 2025-08-24 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| a8fc4750-e065-318d-a59d-04617a40ff60 | -11.6112 | -46.2337 | 2025-08-24 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 294.3 |
| 4da69394-3ee4-33cd-8810-73ad85aa3b2a | -12.0055 | -61.0201 | 2025-08-24 13:30:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 0881f210-b5a3-36e7-bbee-4c4b68a2b81f | -5.4364 | -60.1779 | 2025-08-24 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ff748807-f503-31bc-ae47-eef6bebeb50a | -9.0787 | -65.7151 | 2025-08-24 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |


[Clique aqui para ver as próximas entradas](README92.md)
