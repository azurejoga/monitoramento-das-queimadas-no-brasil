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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d391e9c-3f15-39a7-aaa2-e10eb9ba3173 | -6.1853 | -43.3257 | 2025-08-31 11:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 5c2deeea-f057-3c29-9444-fea0b86cd9e5 | -12.6294 | -48.2201 | 2025-08-31 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 29738469-c5ae-328e-a1be-e7353d65d86a | -6.1665 | -43.3273 | 2025-08-31 11:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 319.7 |
| b035aed1-b868-360b-817d-4d29d17209c1 | -14.8208 | -46.7337 | 2025-08-31 11:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 80e3cac2-1e5c-3d2c-8d42-14d723bed393 | -6.1853 | -43.3257 | 2025-08-31 11:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 9df041c9-c69e-3e1e-97df-5eab2ff06d4a | -12.3924 | -46.4399 | 2025-08-31 11:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 5e0ddfd0-ed9a-3ce6-bfbe-eaae80cc3303 | -6.1665 | -43.3273 | 2025-08-31 11:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 329.0 |
| 6e8bb7ea-acad-313b-855a-b5418550fa80 | -12.6294 | -48.2201 | 2025-08-31 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| b1402fa9-91b0-33b7-b210-f8a47168b27c | -12.6298 | -48.1979 | 2025-08-31 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 6720b1bc-87bb-37fb-a9d6-9ab6797c5763 | -12.6298 | -48.1979 | 2025-08-31 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c0554486-9ba1-30cf-b1fc-da3ef1308a33 | -15.7098 | -48.9702 | 2025-08-31 11:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 30d65400-5a05-3fc1-a8d0-c9ec758418b7 | -6.1853 | -43.3257 | 2025-08-31 11:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 58ea3b39-7636-3486-b7fc-4c931ba88991 | -12.6294 | -48.2201 | 2025-08-31 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| a33b87a4-c371-39bd-8765-9938e1d79a97 | -12.3924 | -46.4399 | 2025-08-31 11:30:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 168c33c5-facc-3caf-bdf1-5dd939a88297 | -6.1665 | -43.3273 | 2025-08-31 11:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 342.5 |
| 6a088e66-9104-32c1-9063-1158455b4cd7 | -12.6298 | -48.1979 | 2025-08-31 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 1c24441b-82b9-326f-a517-329e7616ebee | -6.1853 | -43.3257 | 2025-08-31 11:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 654543fe-1e98-36d6-a58f-076bed807d5a | -15.7098 | -48.9702 | 2025-08-31 11:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 209.3 |
| c91372c0-7a77-3383-a304-f03a83c04770 | -12.6294 | -48.2201 | 2025-08-31 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 01ce6627-33fa-3887-8304-2b03a97e3ce9 | -11.3308 | -43.6635 | 2025-08-31 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 0696ec2a-0645-3773-8906-0fb0b76bebf5 | -6.1665 | -43.3273 | 2025-08-31 11:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 334.8 |
| 9e79f669-4868-3864-9966-1f59ed13b657 | -12.6486 | -48.2175 | 2025-08-31 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c2db81bf-1a58-3d76-8c34-7f3cb6ccbd9b | -11.8357 | -46.5194 | 2025-08-31 11:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 62b1eb96-5ed3-3be2-98ed-35d2620dbd4f | -15.7107 | -48.9255 | 2025-08-31 11:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3ba444fe-3788-3192-ae9d-24b05fc2cab9 | -6.1663 | -43.3506 | 2025-08-31 11:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 944fe595-b1c2-399e-a69f-0990b31dd848 | -11.8181 | -46.4314 | 2025-08-31 11:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| ec3f4410-d662-3c7f-a1f1-39d0882bb1d0 | -12.6486 | -48.2175 | 2025-08-31 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 276adbe8-75a0-3d28-933f-2dfe55c21c02 | -12.6298 | -48.1979 | 2025-08-31 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| c23d032d-d33c-3048-8496-b40fa1d18181 | -15.7098 | -48.9702 | 2025-08-31 11:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 7efb11b2-3209-3ead-bf14-7b56317d3f27 | -15.7107 | -48.9255 | 2025-08-31 11:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 273ab6ca-e735-3a68-87a7-c25d59777c5e | -11.0288 | -46.8745 | 2025-08-31 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 9f4624e3-07d5-3bfd-8e08-35b0a5023c17 | -4.7346 | -44.4457 | 2025-08-31 11:50:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 5a3c2f7b-65bf-3eed-9bb6-524a6b855bfd | -6.1665 | -43.3273 | 2025-08-31 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 419.3 |
| 90840226-0daa-3d27-a453-8b9d58d9efb6 | -11.8181 | -46.4314 | 2025-08-31 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 144.9 |
| be22bc70-5d0a-3038-a6e1-816bb1a01f86 | -15.7102 | -48.9479 | 2025-08-31 11:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 114cadb8-2319-3591-9286-6061618e2f29 | -12.6294 | -48.2201 | 2025-08-31 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| ded19f24-0aa5-35ef-94f9-d2fb004c0a1c | -6.1663 | -43.3506 | 2025-08-31 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 19baff1e-af90-3451-8972-91d8c9b5b1b6 | -7.8543 | -46.9525 | 2025-08-31 11:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 3cf74fe5-9c48-39a0-95c5-449c1e342e41 | -6.1853 | -43.3257 | 2025-08-31 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 2e2e9598-579b-35a4-94e4-2613b56d0acb | -11.3504 | -43.637 | 2025-08-31 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 70f10537-e69f-3533-9509-3bed0784ae29 | -9.2453 | -47.0602 | 2025-08-31 12:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 9be3e33e-6d6c-3539-b6ba-8455281b271e | -14.8013 | -46.7371 | 2025-08-31 12:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 15fb484d-dc1d-3a9d-b456-734da247c584 | -11.3308 | -43.6635 | 2025-08-31 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 91fa2f59-30b6-31e9-9865-3d570bfe7176 | -15.7107 | -48.9255 | 2025-08-31 12:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 62956e1c-8e23-3a20-bf67-66863af2ee1a | -4.7346 | -44.4457 | 2025-08-31 12:00:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| f6bf5e1b-dd61-3670-928b-44f2cfa95c71 | -12.6298 | -48.1979 | 2025-08-31 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 7156116c-69be-3fec-9872-61994aa843d9 | -15.7098 | -48.9702 | 2025-08-31 12:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 121.7 |
| bbd1cd09-1eaa-3ba9-b9f1-c9dc54c798ac | -6.1663 | -43.3506 | 2025-08-31 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 502eba51-37ee-365f-b324-9bc6acbc4018 | -9.245 | -47.0824 | 2025-08-31 12:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 97c3fed0-97a0-37f1-8434-34d914bb883a | -6.1665 | -43.3273 | 2025-08-31 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 330.5 |
| 2d82c655-4882-3b7a-9c96-8a241063d236 | -7.8543 | -46.9525 | 2025-08-31 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 38bb8f2d-70d4-3101-a06d-8cc5951d98af | -9.2642 | -47.0582 | 2025-08-31 12:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f03ad80e-8299-36ab-bc02-f66ab0e6c9c2 | -11.3509 | -43.6133 | 2025-08-31 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| f4af42c4-086c-31d7-8496-a3717c00d4be | -15.7102 | -48.9479 | 2025-08-31 12:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| bf4e18eb-1120-391a-a02f-5eff999613d7 | -12.6294 | -48.2201 | 2025-08-31 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 176.0 |
| afef3c9d-9438-347b-9c97-bf6ad23b0fc1 | -6.1855 | -43.3023 | 2025-08-31 12:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| da368ee0-e0cc-3fe9-a6e9-506f0da39843 | -11.3312 | -43.6399 | 2025-08-31 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| d164a9e9-5a83-3e80-8dd8-7a6ac17f8c11 | -11.3701 | -43.6104 | 2025-08-31 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 62086cf1-2489-3da4-8305-da9b14c95b4f | -11.8181 | -46.4314 | 2025-08-31 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 7ccc6f4e-99da-36c8-8612-6901e83d64f6 | -6.1853 | -43.3257 | 2025-08-31 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| bc76472b-b583-3c5a-a466-5a70013cd5e0 | -6.1853 | -43.3257 | 2025-08-31 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 83519795-8aa9-3767-92b1-b83040e8b565 | -11.3304 | -43.6871 | 2025-08-31 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2f508a62-9bfc-39f1-a7c0-d93526150734 | -9.8488 | -45.8033 | 2025-08-31 12:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| f3365973-47b6-3876-8713-54adab894dd6 | -11.3509 | -43.6133 | 2025-08-31 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 5b03c014-af75-3f58-b5f3-26c5398eda4b | -6.1665 | -43.3273 | 2025-08-31 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 377.9 |
| 2f15605f-ff61-324c-b789-93663a94eee0 | -7.8543 | -46.9525 | 2025-08-31 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 46917b32-d592-3a09-8e1a-adf55ed525bc | -10.0205 | -48.387 | 2025-08-31 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 15cdce10-6310-3092-a222-7c8c447e2632 | -11.3308 | -43.6635 | 2025-08-31 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| db09648c-8e23-3702-b7d1-95e124f0de51 | -12.6302 | -48.1757 | 2025-08-31 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 36b051bb-9a48-3df8-a44e-b84cca7dec60 | -9.245 | -47.0824 | 2025-08-31 12:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 39587f6d-b6ec-3ee6-92ae-eee43b745f08 | -4.7346 | -44.4457 | 2025-08-31 12:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 2b554a14-0f82-3f88-bb93-4e288f092230 | -10.0208 | -48.3652 | 2025-08-31 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 63889132-766a-37a9-b956-933879a39bbe | -12.6294 | -48.2201 | 2025-08-31 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 208.0 |
| bd3946b6-cabe-378b-a706-a9554140d8bc | -7.2144 | -45.4203 | 2025-08-31 12:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9ce23a8d-6634-38e3-a907-ce9a51ee1da9 | -15.7102 | -48.9479 | 2025-08-31 12:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 119.4 |
| fe6f79b4-42c8-3a88-9896-dcfed5cd6304 | -12.6298 | -48.1979 | 2025-08-31 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 312.7 |
| 98d703a7-75c0-31d0-8e66-9aef6686a22d | -15.7107 | -48.9255 | 2025-08-31 12:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| dace5b17-8cf2-38bb-9e49-752c97246c20 | -11.8181 | -46.4314 | 2025-08-31 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 4e1117c6-a25e-38a6-866e-6caba27d8f8d | -11.3312 | -43.6399 | 2025-08-31 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 5986b226-0125-3f7f-97a6-3ee7bda10514 | -11.3504 | -43.637 | 2025-08-31 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.9 |
| e9f9c4ee-bede-3b9a-b328-25e6a7280df1 | -7.2142 | -45.443 | 2025-08-31 12:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 357d3c84-46c9-32a6-ab0e-528960d3e860 | -6.1663 | -43.3506 | 2025-08-31 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 2c017676-1398-3d09-8903-95824fc350cc | -7.8541 | -46.9747 | 2025-08-31 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 707bcbbc-8ecd-387a-a09e-9ffaa72ef1d2 | -15.7098 | -48.9702 | 2025-08-31 12:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 111.3 |
| e7552b95-53c6-3067-b59b-50689db5ee32 | -12.6294 | -48.2201 | 2025-08-31 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 207.8 |
| c288ebb7-b63c-39d9-8e3c-1e986c645f20 | -11.0104 | -46.832 | 2025-08-31 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 72933c16-acfc-3bd2-bca3-76a0eb3bfcbc | -15.7098 | -48.9702 | 2025-08-31 12:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 7b678a35-7127-371e-8196-07a91e882156 | -4.7346 | -44.4457 | 2025-08-31 12:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 248.0 |
| d36431d2-2b24-3675-b909-4bc5f0b01c3e | -12.8621 | -48.0768 | 2025-08-31 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 1e838137-bc9b-3789-895a-e2dc5de3c4cb | -7.8541 | -46.9747 | 2025-08-31 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| ed9b6c66-d42f-3fea-a256-0fa6ccbe7375 | -16.2417 | -52.675 | 2025-08-31 12:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| fb6b62f6-c061-3ba9-af50-9655b7dec664 | -12.6486 | -48.2175 | 2025-08-31 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 96e54286-3d9a-34f2-8874-c5cdd34622dd | -7.1954 | -45.4446 | 2025-08-31 12:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| fbfe07c0-6a4f-3fea-b1ad-840f2d839522 | -7.8543 | -46.9525 | 2025-08-31 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 94782733-8fc3-3019-99af-ace87a882079 | -7.2142 | -45.443 | 2025-08-31 12:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 1240be4b-e3af-38f6-b7f1-d29b3b06729e | -10.0205 | -48.387 | 2025-08-31 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 7f11c031-e98c-357b-8cd2-2b9d8a31741a | -11.8181 | -46.4314 | 2025-08-31 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f44c4005-104a-32b8-b0e6-5413b4a44ed7 | -15.7107 | -48.9255 | 2025-08-31 12:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| d5b808c8-0715-38f0-bb1d-b02991b5beaf | -11.0101 | -46.8544 | 2025-08-31 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 9c7c4a82-5cdc-3fc6-9410-d20e5be4c7c3 | -15.7294 | -48.9669 | 2025-08-31 12:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |


[Clique aqui para ver as próximas entradas](README86.md)
