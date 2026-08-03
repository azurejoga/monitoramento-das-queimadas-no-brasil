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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4889ab97-dd24-3e53-87e6-7ed3659474c7 | -8.5885 | -45.3549 | 2026-08-03 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 06021a91-ddaa-3600-9c5b-9ca48e7aab53 | -6.5512 | -55.1769 | 2026-08-03 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 232.3 |
| 57122b51-0b52-35be-843c-596b26a3ac6d | -3.1158 | -47.9232 | 2026-08-03 15:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 866f32f2-7725-33b8-8f10-7115f2b720e0 | -6.5512 | -55.1769 | 2026-08-03 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 253.7 |
| 72e3d963-efed-3584-b6d8-3c1e8f39ba4d | -6.5957 | -45.4275 | 2026-08-03 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 3ed10a91-3d49-3489-9989-a78f396b95a7 | -2.9581 | -50.3569 | 2026-08-03 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 59ae3471-9810-31be-a9e0-f2f78415c910 | -5.4762 | -45.1262 | 2026-08-03 15:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a744de75-4edf-3778-8dfd-857d7d423286 | -2.9581 | -50.3359 | 2026-08-03 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 614a562d-c23a-3834-b8d7-c1b6151fd916 | -8.9302 | -45.2041 | 2026-08-03 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e0c0f395-28b5-3c16-9838-cb0d5822f354 | -11.6047 | -50.245 | 2026-08-03 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| bd701204-af69-31fb-ae39-dd3c1333b224 | -7.9721 | -44.9169 | 2026-08-03 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 426.8 |
| abc56848-a5c7-3d31-88e5-5c754c25c6ee | -6.5514 | -55.1569 | 2026-08-03 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 4e29e2a8-6a3d-322e-b630-6e35958515cc | -6.1485 | -45.2137 | 2026-08-03 15:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 175.7 |
| e64c6e50-3797-3b50-8c41-4a2080c83765 | -6.5699 | -55.156 | 2026-08-03 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 1da3d786-4ebc-3e51-9f33-6095977d525a | -7.9532 | -44.9188 | 2026-08-03 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| e17eff2f-e0c3-3e1d-84f0-92671939331c | -6.5699 | -55.156 | 2026-08-03 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 227.1 |
| 46960f2e-2fc3-3950-a046-12d31780d8e3 | -6.5514 | -55.1569 | 2026-08-03 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 220.8 |
| 521ec5e8-0bba-37e8-b2f1-f6dd82f749f1 | -2.9581 | -50.3569 | 2026-08-03 15:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| edccd44d-39c6-3534-9485-67d0cd257ed0 | -9.9375 | -46.2222 | 2026-08-03 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 5d16e66b-88e5-35c0-b6ef-1c0e051eac94 | -5.4762 | -45.1262 | 2026-08-03 15:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 3467b848-7801-3fe1-87c1-11506325b6bf | -7.5286 | -45.8659 | 2026-08-03 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 5509e95f-6b2b-314d-976c-6fd2e3cba7d6 | -3.1159 | -47.9015 | 2026-08-03 15:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 183c76d7-d9d3-36e2-86b3-aaf185704150 | -9.9568 | -46.1974 | 2026-08-03 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 9ca0859e-12cd-3986-8f52-57a1489aadea | -6.5957 | -45.4275 | 2026-08-03 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 234.1 |
| 7104c498-3af2-3a6a-897b-adc941c51104 | -7.5289 | -45.8434 | 2026-08-03 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 5f3e87ce-1797-3432-9b6a-a5e603c1d73f | -3.1158 | -47.9232 | 2026-08-03 15:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| cd6ef11a-021f-3b05-a681-ce0152e5fb0e | -9.9565 | -46.22 | 2026-08-03 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 385.6 |
| a27a5e5c-485e-3c44-85df-15ef001664ed | -11.6047 | -50.245 | 2026-08-03 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c37382da-ca18-37c3-9419-1864919a9c43 | -9.9565 | -46.22 | 2026-08-03 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 8f814852-b92f-3ff0-be22-26247ec6763d | -5.4762 | -45.1262 | 2026-08-03 15:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 201325dd-f4d6-3347-99fe-4b4c7ac164c6 | -11.7771 | -50.1605 | 2026-08-03 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 87eaaaef-0190-33db-b797-4079751ff4c5 | -11.7774 | -50.139 | 2026-08-03 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 540ffc2b-0f7f-3016-997d-3ea903aa98b4 | -1.6591 | -54.4543 | 2026-08-03 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| f9f8690d-7200-3de6-b176-6321e9bff052 | -2.7582 | -49.4771 | 2026-08-03 15:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5bbb5329-36fc-331b-9e62-368934f39e00 | -6.5514 | -55.1569 | 2026-08-03 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 258.3 |
| 06716e57-5066-32fa-96bc-2f27b6179a3b | -11.5853 | -50.2687 | 2026-08-03 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 1a931228-deb9-3f85-9d73-9f7369d0cf2a | -9.9375 | -46.2222 | 2026-08-03 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| e50d25f6-0677-3f81-9015-1ad0886a6743 | -6.5697 | -55.176 | 2026-08-03 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 182.9 |
| 83550a3b-36dc-36c4-96da-859a387373cb | -2.9581 | -50.3359 | 2026-08-03 15:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3912bd24-d7e4-3173-bfcd-0feb28475892 | -12.251 | -51.5564 | 2026-08-03 15:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 25bfe3a2-85d6-3bf6-8886-ab9279909fb7 | -6.5699 | -55.156 | 2026-08-03 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 215.9 |
| ab715784-4a2a-3fb3-97d6-ba8027cd9f47 | -11.6047 | -50.245 | 2026-08-03 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 958e2ab2-c6f9-3b28-bf7a-453803a98f32 | -7.4832 | -44.8958 | 2026-08-03 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 70c8f4eb-f6f1-3b01-9469-2ba7b493de66 | -9.9565 | -46.22 | 2026-08-03 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 356.1 |
| a314e169-b217-30f5-af38-d5cea491055d | -11.7771 | -50.1605 | 2026-08-03 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 0b3e7eb2-ebd5-31c5-abc9-f173956d3729 | -9.9568 | -46.1974 | 2026-08-03 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| d5380737-7245-3b08-9eb0-efa6a6662e1d | -9.9375 | -46.2222 | 2026-08-03 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 299.2 |
| 68e437e2-fb64-389d-9ada-4a1ac2721a18 | -2.9581 | -50.3359 | 2026-08-03 15:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ed9af870-60d5-3704-8257-dbc927b04361 | -11.5853 | -50.2687 | 2026-08-03 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 549440f9-6a45-3390-8af9-74228740a3a5 | -6.5514 | -55.1569 | 2026-08-03 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 261.4 |
| c9cfe646-86b5-32a4-88ec-73020bfc052b | -11.6047 | -50.245 | 2026-08-03 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 5a493636-b1a8-3449-bffb-6259bea35535 | -11.7774 | -50.139 | 2026-08-03 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| f56f82b7-aebd-3e0f-9d75-ef1b404c7ce8 | -6.5699 | -55.156 | 2026-08-03 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 214.9 |
| ed441407-b048-3fc2-9a97-22a4e073f543 | -6.5697 | -55.176 | 2026-08-03 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 219.3 |
| a073ad30-1dcd-322d-94ff-4065986736a9 | -6.5512 | -55.1769 | 2026-08-03 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 230.8 |
| df39c4ba-e838-356e-b8b7-8dcf5f7f3a6e | -10.6312 | -46.7675 | 2026-08-03 15:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 71dcb693-cd12-3919-9c9d-35242247e064 | -9.9378 | -46.1996 | 2026-08-03 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 189.5 |
| a1658459-a836-33c1-81a0-4f44dfbff4a4 | -9.9565 | -46.22 | 2026-08-03 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 508.8 |
| 77c09053-33dd-391f-b3e8-42194a9a886b | -6.5514 | -55.1569 | 2026-08-03 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 278.7 |
| 24c69eb2-75be-370f-8b13-be0802fdbe37 | -6.5957 | -45.4275 | 2026-08-03 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| f60271bc-6bcd-3aa8-b9cd-428c527077da | -9.9568 | -46.1974 | 2026-08-03 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 35f8271d-f4bd-35b4-b88f-fdd389a1572c | -6.5699 | -55.156 | 2026-08-03 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 284.7 |
| 504b9cc7-0f48-332f-94e3-a7f10876ac1d | -9.9375 | -46.2222 | 2026-08-03 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 591.2 |
| 52595495-8ed3-361e-b9c1-08352e82b6c1 | -7.6502 | -45.0852 | 2026-08-03 15:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 69ec0c1a-cb7f-3bb7-bf1a-a8dac8e04cc3 | -11.5856 | -50.2472 | 2026-08-03 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e9fc8c18-f4ee-374e-82fd-8d384f0725cc | -3.1158 | -47.9232 | 2026-08-03 15:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 4a6245ea-2de5-3333-a2e1-896021e25824 | -6.5608 | -56.5266 | 2026-08-03 16:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 91f5e9e0-d69c-39a2-9352-0f49906eaeab | -2.9581 | -50.3359 | 2026-08-03 16:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d51294e0-9222-3fb4-ae92-259e611f7424 | -11.6047 | -50.245 | 2026-08-03 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 212e7798-13d7-339b-bd9b-8af42098deb7 | -9.9565 | -46.22 | 2026-08-03 16:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 90daf570-06d6-36d3-a232-be563bdc735a | -5.4762 | -45.1262 | 2026-08-03 16:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9d5a10a5-b1ba-3755-aa9a-13902d1a31f9 | -7.6502 | -45.0852 | 2026-08-03 16:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3b2b5385-1ae7-3f1b-a046-4738897054e4 | -11.5856 | -50.2472 | 2026-08-03 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 4854abab-6414-3dce-b975-ebcd911cf905 | -2.7582 | -49.4771 | 2026-08-03 16:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1e955e14-224a-355d-a552-2a215c726760 | -6.5955 | -45.4501 | 2026-08-03 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 65aa490b-d348-300c-8ed1-98c9fcfa3440 | -11.7771 | -50.1605 | 2026-08-03 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 3a297388-a015-3d19-b3fa-ffd976af4f63 | -12.4594 | -50.4009 | 2026-08-03 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ca997fef-4233-3c34-a124-498caba957d9 | -6.5957 | -45.4275 | 2026-08-03 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| f99b619f-f5f2-3999-beea-fd0180e1dcd8 | -5.4949 | -45.1249 | 2026-08-03 16:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| b286664e-d5c5-3b52-a9ab-07c4d5f26d56 | -3.1158 | -47.9232 | 2026-08-03 16:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 99328bd0-2da1-301a-a42c-c13674d81dc9 | -3.5125 | -60.3401 | 2026-08-03 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| e06d3e21-bf78-3865-9755-10866ea390cc | -2.7582 | -49.4771 | 2026-08-03 16:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f4ae0bf1-c860-3b3d-88b2-bae715c6195a | -6.9579 | -52.827 | 2026-08-03 16:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7fd39add-4b14-36e7-814b-e54e81d2d56e | -2.9581 | -50.3359 | 2026-08-03 16:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a4ac438d-0352-326e-82d4-3ce80db922bc | -11.6047 | -50.245 | 2026-08-03 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d6e2a4d4-fa2e-34ff-a72e-2f7b63ef622e | -6.1485 | -45.2137 | 2026-08-03 16:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| cf924d56-73e7-3094-9e9b-b2a0f80a7606 | -6.5957 | -45.4275 | 2026-08-03 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 798c884f-1c41-34b0-9b65-21c926a4047e | -11.7771 | -50.1605 | 2026-08-03 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 9422f9d9-1d91-3526-93db-40312809d146 | -9.9565 | -46.22 | 2026-08-03 16:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| e2735bef-de91-36a9-add9-f732cce933ba | -9.9375 | -46.2222 | 2026-08-03 16:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 85cd28ae-995e-3b52-b5e5-6b3bc1d0334b | -5.4949 | -45.1249 | 2026-08-03 16:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| adaa978d-94f7-321f-a96e-a5a5265e2766 | -5.4762 | -45.1262 | 2026-08-03 16:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 37be3719-f805-3dea-b9ab-46f14c290e14 | -6.5608 | -56.5266 | 2026-08-03 16:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 08e33441-fd2e-39a0-941c-43fe661cc69f | -2.9581 | -50.3569 | 2026-08-03 16:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 088654c0-54a4-37bd-802d-0fa9ba318531 | -6.5699 | -55.156 | 2026-08-03 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 348.8 |
| c28a065b-70bd-3d65-9681-f68d241cd1a4 | -9.9375 | -46.2222 | 2026-08-03 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 253.3 |
| 9413d758-0ddd-3477-9cae-0df956102eed | -11.7771 | -50.1605 | 2026-08-03 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 06420fcc-b499-3aca-acaa-e13d60642796 | -6.5957 | -45.4275 | 2026-08-03 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| c82337c0-53eb-39f7-9452-b98558d7ac6d | -6.9581 | -52.8065 | 2026-08-03 16:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4eb1f97c-9262-37ab-8484-c32ba771e93f | -9.9565 | -46.22 | 2026-08-03 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 266.6 |


[Clique aqui para ver as próximas entradas](README13.md)
