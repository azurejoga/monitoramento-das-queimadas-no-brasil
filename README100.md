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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5636245-192e-370e-b780-f080e55e0c84 | -11.0568 | -45.146 | 2025-09-01 10:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 766e54e2-112a-3648-b333-cf4e1585e3cc | -15.5862 | -48.3435 | 2025-09-01 10:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| c8dcdc57-48df-3017-b120-c8d05b7cd6c4 | -11.0377 | -45.1487 | 2025-09-01 10:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| bcfba606-bdfd-3868-95b5-c4f8411b52fa | -15.7116 | -48.8809 | 2025-09-01 10:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 46f51efa-d590-3ef8-b601-d2c772f9c212 | -7.076 | -44.3376 | 2025-09-01 10:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 36d80697-8d12-361d-8f65-193a8d757128 | -11.0377 | -45.1487 | 2025-09-01 10:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| c9ff8008-d148-3791-927a-c5d3d2fdf9a3 | -7.076 | -44.3376 | 2025-09-01 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 01c9e851-6daf-3422-be58-844a9a5e2360 | -11.0568 | -45.146 | 2025-09-01 10:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| c396aaef-8965-3666-bad0-c54aa3d8db87 | -15.5862 | -48.3435 | 2025-09-01 10:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 9d2bfc20-b445-3c5d-8e6b-07d9e5fe14eb | -11.0377 | -45.1487 | 2025-09-01 10:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 227d5911-9578-3a70-8e30-53b0c4b2a8e2 | -15.7116 | -48.8809 | 2025-09-01 10:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 137.6 |
| c671ba68-ef95-3cd4-ab02-42636a3ecb1f | -15.5862 | -48.3435 | 2025-09-01 10:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 204b5b08-9a28-354e-8c18-36f9407fda1f | -7.9539 | -46.4542 | 2025-09-01 10:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 46e08f71-c496-372f-bfdc-f565c33f0d69 | -11.0568 | -45.146 | 2025-09-01 10:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| d08d1e69-686b-3b08-aac7-a604ba17ebf3 | -7.076 | -44.3376 | 2025-09-01 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8370afbe-c582-365b-8470-7085c2597e71 | -12.5718 | -48.228 | 2025-09-01 10:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| dbe3cb89-b9b2-3b40-a4dc-3dbda802fe72 | -11.0652 | -46.9818 | 2025-09-01 10:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 3f532cd5-317f-36b8-ac3d-48d1e137aad3 | -7.9539 | -46.4542 | 2025-09-01 10:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| b26af1c7-992a-3f25-9ee9-68709fd7ff63 | -15.5862 | -48.3435 | 2025-09-01 10:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| a531786a-37ab-326c-a07f-619c1de68ee4 | -11.0377 | -45.1487 | 2025-09-01 10:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 3b7f1583-fead-3da4-a483-6a579999bc82 | -12.5718 | -48.228 | 2025-09-01 10:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 4361a4f0-b658-35fb-8147-18e62a96a77c | -7.076 | -44.3376 | 2025-09-01 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1b355b3c-c43d-3d88-a695-0637178fef04 | -7.9536 | -46.4765 | 2025-09-01 10:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 09f38957-684e-312a-a943-4775b80fc4ab | -15.7116 | -48.8809 | 2025-09-01 10:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 32f36f84-f148-35bc-a6ea-47fc06388968 | -7.9727 | -46.4524 | 2025-09-01 10:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 9f38011e-55ee-362e-851f-676ec47b312d | -11.0461 | -46.9842 | 2025-09-01 10:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 234ef1ee-569c-3df5-99b4-bff428e9b5b1 | -11.0568 | -45.146 | 2025-09-01 10:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.3 |
| a1bc8fe8-6ad7-3fbc-914a-56b5172f1115 | -7.076 | -44.3376 | 2025-09-01 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| a22beabc-4d90-3830-b6a5-cdf3561e2b4d | -15.7116 | -48.8809 | 2025-09-01 10:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 5aea6cd9-a512-3e34-9825-7ce180011d0f | -7.9727 | -46.4524 | 2025-09-01 10:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 968b057a-31de-3729-9455-e2688f267772 | -11.0568 | -45.146 | 2025-09-01 10:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 2962d291-903e-315a-a474-78291015dfbf | -12.5526 | -48.2307 | 2025-09-01 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 27954ce1-93f8-3bd2-8fb6-73fc462afa84 | -12.5722 | -48.2059 | 2025-09-01 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c48b0572-1dd2-39b5-a783-d23ac40aec10 | -7.9536 | -46.4765 | 2025-09-01 10:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 0db7b3cd-5e04-30b0-9129-249e958001d7 | -7.9539 | -46.4542 | 2025-09-01 10:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| cc7458e6-de19-37b1-bb4a-89eeca9d9ac7 | -11.0377 | -45.1487 | 2025-09-01 10:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| ee5536c8-1d6d-3377-aad0-c837e8b9d57f | -12.591 | -48.2254 | 2025-09-01 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 4d4d4918-e354-3e2f-8344-dd4871dadba4 | -11.0648 | -47.0042 | 2025-09-01 10:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 9521ad1e-9382-3532-a8bb-6357e1830836 | -12.5714 | -48.2502 | 2025-09-01 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 0c323b57-0c52-3f08-b0b1-31d00e66be20 | -12.5718 | -48.228 | 2025-09-01 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 283.2 |
| 753f4754-ad55-3c46-9314-e68e2ad3fee2 | -12.5718 | -48.228 | 2025-09-01 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 314.0 |
| abf81428-f817-3177-ab4b-39a3b959a78a | -7.9539 | -46.4542 | 2025-09-01 10:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 049b1698-2e7b-3dd9-bc8d-07095de6c887 | -11.0461 | -46.9842 | 2025-09-01 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 02b2b71b-3d8f-33b3-b620-21dc05bd1974 | -11.0377 | -45.1487 | 2025-09-01 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 63e80578-7024-3351-a23e-48eb94ca23cc | -11.0652 | -46.9818 | 2025-09-01 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 8baca623-ff54-3dd8-8136-ca2fa381c196 | -10.8935 | -45.8084 | 2025-09-01 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| eed0edc5-a54f-37f0-8d2e-809d711f313b | -11.0568 | -45.146 | 2025-09-01 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 42485329-d0d0-35cb-be3c-3230ca4a9917 | -15.5862 | -48.3435 | 2025-09-01 10:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 6726ae03-5343-31ba-bd00-61875a076e21 | -12.5522 | -48.2528 | 2025-09-01 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 2930d383-d14c-3fe2-ba22-7cca18d631e4 | -12.591 | -48.2254 | 2025-09-01 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 7b609916-53c8-3448-9ee4-1163ea08f8d6 | -11.0457 | -47.0066 | 2025-09-01 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| f81f443e-92ea-3604-87e2-54db5a6d10fc | -7.076 | -44.3376 | 2025-09-01 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 75c51623-f83b-3902-8c50-08a46bead555 | -12.5714 | -48.2502 | 2025-09-01 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 17ded22d-6c67-3731-be1d-a357ad528cc6 | -7.9536 | -46.4765 | 2025-09-01 10:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d2f3d9a4-dc18-309b-ab6e-e08cd90b1ef8 | -15.7116 | -48.8809 | 2025-09-01 10:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 3c1d658e-04b7-3a38-bfea-fdb09db3cfb3 | -11.0648 | -47.0042 | 2025-09-01 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 73278141-5545-3848-a064-025f7bc63e04 | -7.9351 | -46.4559 | 2025-09-01 10:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 715efec2-6d29-39c2-bfd6-d1e8eec90ab4 | -12.5526 | -48.2307 | 2025-09-01 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 280.7 |
| 2c72a5b8-9aee-37aa-a62e-a6c926b97d9e | -12.591 | -48.2254 | 2025-09-01 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| dc483786-6716-3dd3-8c81-63654e50d4f3 | -7.9351 | -46.4559 | 2025-09-01 11:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 84274428-036c-3c8a-9df9-65cba02039d2 | -7.076 | -44.3376 | 2025-09-01 11:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 8da29b7e-47d4-32dd-9671-3d6db24afa8a | -15.5862 | -48.3435 | 2025-09-01 11:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 8bc08450-107a-3410-9170-d5a4562942fe | -12.5526 | -48.2307 | 2025-09-01 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 358.1 |
| 6183a66c-4087-3387-83f5-6fd34e5adf73 | -7.9539 | -46.4542 | 2025-09-01 11:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| a8757e95-88b2-3fe9-b320-a8dd5d60c506 | -12.9768 | -48.1049 | 2025-09-01 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 09f41b24-5a6e-3351-9218-a1a55edd1aa1 | -11.0568 | -45.146 | 2025-09-01 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| d0a1178c-b93f-30c1-83bb-bd896087514f | -15.7116 | -48.8809 | 2025-09-01 11:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| e41c3e1a-846d-300f-a382-23131f410f02 | -11.0377 | -45.1487 | 2025-09-01 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| ff99cd51-c6d3-33a6-add2-8d84ab75abc7 | -11.3705 | -43.5868 | 2025-09-01 11:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| da34b225-bd88-3f5a-9a1a-e9187c04c67a | -12.5718 | -48.228 | 2025-09-01 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 356.9 |
| 6c98d213-72bf-3a37-b1c7-e1d6ee337d18 | -7.0757 | -44.3606 | 2025-09-01 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 1f772202-6d47-3872-b891-e4d201598adc | -7.076 | -44.3376 | 2025-09-01 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 05639b13-7a6b-3bce-a546-ec6a34f8b24c | -7.9351 | -46.4559 | 2025-09-01 11:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 1c695e19-1c04-3e53-875e-7d9c9b5f544e | -11.0568 | -45.146 | 2025-09-01 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.2 |
| f856e09a-e74e-3891-8a73-3ec600920357 | -11.0377 | -45.1487 | 2025-09-01 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a20e41af-6fda-364d-abf4-77ee9ba5d883 | -12.5718 | -48.228 | 2025-09-01 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 355.2 |
| 58568321-ace5-3382-ab67-f5eec8bef361 | -11.3705 | -43.5868 | 2025-09-01 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| e3487ee1-ef91-3283-8f22-c55a85b17288 | -7.9539 | -46.4542 | 2025-09-01 11:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| abf9c643-8c7e-3f77-bb23-7f666831ac13 | -12.5526 | -48.2307 | 2025-09-01 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 447.3 |
| 93dcad37-c9c3-3a00-8169-d2b249d34198 | -11.0845 | -44.6343 | 2025-09-01 11:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 3a54b7fb-6bee-3c07-8934-56ff8a6279d1 | -12.591 | -48.2254 | 2025-09-01 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 9aaa6b8a-5302-39be-bc9f-7f15fb3d7069 | -12.5718 | -48.228 | 2025-09-01 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 418.8 |
| d7d4e482-611c-3f1a-9f37-66660790da4c | -7.0757 | -44.3606 | 2025-09-01 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| b3d2dc70-1490-3319-9eda-8ec41a1bd044 | -12.9768 | -48.1049 | 2025-09-01 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 8ef39493-c59c-3283-98bf-4257a8cdd985 | -12.5722 | -48.2059 | 2025-09-01 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 0cf2cc5c-f229-32c1-a64f-4eba69f0ff5a | -7.9539 | -46.4542 | 2025-09-01 11:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 421174be-4f30-3410-97a1-81951a7a22c4 | -15.5862 | -48.3435 | 2025-09-01 11:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| d50277fe-9a4b-3503-9dca-1223f69e8280 | -7.0946 | -44.3589 | 2025-09-01 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| cc79862b-cb8b-3daa-b289-b1e77ccc8812 | -6.8426 | -43.3385 | 2025-09-01 11:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 257b4915-a4f9-3b51-b86e-02eb5e8cda86 | -11.0568 | -45.146 | 2025-09-01 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 84957859-8f30-3eb7-8ca7-04593f2612af | -12.5526 | -48.2307 | 2025-09-01 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 371.5 |
| 01ca0382-48fa-3c01-a61a-c764ce7d52cb | -7.076 | -44.3376 | 2025-09-01 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 8233d183-b991-35ae-8eae-e3f458c9f00e | -12.591 | -48.2254 | 2025-09-01 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d9fe8e5c-a0fa-344a-8a2e-ee4f6f220cee | -11.0377 | -45.1487 | 2025-09-01 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 8f84c37d-fea4-3b94-8e3f-01c15b245639 | -11.0377 | -45.1487 | 2025-09-01 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 33972eb6-268a-3bac-9390-695f41621761 | -7.076 | -44.3376 | 2025-09-01 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 479a1513-357e-3d36-bc6f-c13abcf523c9 | -7.0946 | -44.3589 | 2025-09-01 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 96e10301-3f18-3fed-98f8-313c80414cc9 | -12.5718 | -48.228 | 2025-09-01 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 293.2 |
| b6d5c438-2e37-3172-965e-ae075e168b0f | -7.9539 | -46.4542 | 2025-09-01 11:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 6212c0a0-2da8-35ed-ab1d-0518808873a6 | -11.0662 | -46.9145 | 2025-09-01 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |


[Clique aqui para ver as próximas entradas](README101.md)
