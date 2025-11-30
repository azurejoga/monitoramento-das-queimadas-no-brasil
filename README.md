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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62c220c3-bad0-37d1-85bd-7f2dd932d3b8 | -2.2086 | -48.0145 | 2025-11-30 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 571baaa0-0aa9-3e9b-8d3c-09077e71a0fc | -8.1822 | -43.2034 | 2025-11-30 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| cf2420de-25cb-3128-98c7-0dbbf16769ba | -3.377 | -43.8281 | 2025-11-30 00:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| edd69dec-71f8-354b-b12d-212c9aa06b6c | -3.5946 | -41.6577 | 2025-11-30 00:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| ddc8b3e8-a537-35b9-acd8-c2919417a917 | -8.0507 | -43.1472 | 2025-11-30 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.5 |
| fe2350e3-a9e7-34a4-a1a2-b91fe50fa947 | -8.0318 | -43.1493 | 2025-11-30 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 6f86e140-4ec3-3d63-a396-850987372036 | -2.2087 | -47.9929 | 2025-11-30 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 0aba3436-6817-3595-a6ca-41ccca2bb840 | -12.0195 | -49.2659 | 2025-11-30 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 3d78cde6-2606-32e5-a9e0-8d49beffb00d | -5.7309 | -39.8286 | 2025-11-30 00:00:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 2f595345-5693-34d8-a749-e196c3270a59 | -2.4523 | -47.0945 | 2025-11-30 00:00:00 | GOES-19 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| c0144020-437b-3744-93ab-c70aba5cadd8 | -3.3771 | -43.805 | 2025-11-30 00:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 06d033cc-2d7c-3ba9-a6eb-4df8163efcd8 | -3.4127 | -44.1255 | 2025-11-30 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| c3e1b18d-8e41-3192-aba9-621696d8824b | -2.6507 | -48.5414 | 2025-11-30 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 16b0b4bf-4e07-30d8-9dfd-0ab2b600fdae | -3.5477 | -43.3109 | 2025-11-30 00:00:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 2f8a2d77-85c3-3028-871b-488b53e4422e | -8.0513 | -43.1001 | 2025-11-30 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 14179c82-fa07-3142-864e-fab60b88e6d8 | -19.9138 | -57.4414 | 2025-11-30 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.3 |
| a5156f89-dcfb-39d9-bf56-b01f64ebc7ec | -2.532 | -45.5862 | 2025-11-30 00:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 330a8e9d-22a9-355a-af21-09da60646525 | -2.6322 | -48.542 | 2025-11-30 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 3f46814e-c52a-333a-8535-b2a931d0f84a | -2.4524 | -47.0726 | 2025-11-30 00:00:00 | GOES-19 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 6cee14f6-def4-3274-8ef9-b2de4459ec08 | -8.1633 | -43.2055 | 2025-11-30 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 2f32b8f9-dc14-31ae-8efa-daa3641687bb | -8.0324 | -43.1022 | 2025-11-30 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 8a6ed0b4-4761-3582-bd16-395394d47e15 | -12.0004 | -49.2683 | 2025-11-30 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| da72e9a4-9453-343a-8a8f-7b7fdca4336d | -2.6507 | -48.5629 | 2025-11-30 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 2d8ab2f3-5e10-3b0a-9a4f-19898bbcad79 | -2.5194 | -49.101 | 2025-11-30 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 440f2b3a-ccde-36fb-ad46-d59b4fc3dc53 | -7.5014 | -37.4242 | 2025-11-30 00:00:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 24bf896d-5c46-3bb0-98a4-65efd74721ce | -8.0321 | -43.1257 | 2025-11-30 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 252.6 |
| ed8b5dcf-842f-3731-9645-3794d50f8692 | -8.051 | -43.1237 | 2025-11-30 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 399.4 |
| 7fb0428a-e138-3934-8e53-ebfdde55548b | -23.6237 | -52.959 | 2025-11-30 00:00:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 88.7 |
| 077aff18-715a-3ece-91b6-0053f01869e2 | -2.7517 | -45.0872 | 2025-11-30 00:03:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99189301-bc65-3fc0-8205-41b68105287c | -4.5957 | -45.209599 | 2025-11-30 00:03:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50a0d025-51cf-3e90-abe8-77278f9a7bb9 | -4.4325 | -44.4771 | 2025-11-30 00:03:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e8f12a8-ef9e-3403-8e69-ff8ee9313d8e | -3.1513 | -43.169998 | 2025-11-30 00:03:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 970313d1-0623-33e6-bcb8-61ce1f63cbd2 | -2.593 | -47.342098 | 2025-11-30 00:03:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 955822f6-e54a-3efb-8032-388efdebc919 | -5.7235 | -39.842201 | 2025-11-30 00:03:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 534cd0ad-cefc-3384-bfcb-2350fbfd8781 | -2.4293 | -47.069302 | 2025-11-30 00:03:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbc23e76-f5a9-3636-9127-f629492104ba | -2.3462 | -45.611301 | 2025-11-30 00:03:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d720ce9-98b9-35f0-939b-21c342059b26 | -2.5458 | -45.267399 | 2025-11-30 00:03:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37b2a47d-dd38-34b9-9e3e-4ef31a0a6872 | -5.722 | -39.8354 | 2025-11-30 00:03:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cd8f5737-6b6c-3e3e-bc80-4f5a221b1ecc | -2.59 | -47.3284 | 2025-11-30 00:03:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e69433ab-f8e5-30b4-88a6-d4473f300fc6 | -3.2094 | -41.566399 | 2025-11-30 00:03:00 | METOP-C | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 814a4124-cea6-3902-a1c7-1eedd6f6b247 | -2.7366 | -42.613098 | 2025-11-30 00:03:00 | METOP-C | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ffc9648-7eb7-332c-b2e1-acbb2e987d15 | -2.8759 | -45.365101 | 2025-11-30 00:03:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2df24c2-4847-3cc5-9e16-8551f621212f | -2.3439 | -45.600899 | 2025-11-30 00:03:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91ac6daa-72d9-3e9f-ba03-f139e4cf76ad | -3.9705 | -42.5131 | 2025-11-30 00:03:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 188b4e1a-de2c-3ec7-8241-cfc4252dfc4a | -5.7302 | -39.826302 | 2025-11-30 00:03:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8ccb5cc1-f9c9-35eb-975e-83ae17a9fe36 | -4.4368 | -44.496101 | 2025-11-30 00:03:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9784a9a-3971-3d47-adc8-6bd76b5c7b90 | -8.0306 | -43.110298 | 2025-11-30 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c6b52cea-41a5-3a6b-a01c-c6aadba6ebf8 | -5.7318 | -39.833199 | 2025-11-30 00:03:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2945ef84-12a3-32e7-ae87-68b3c044dd74 | -3.5238 | -43.862202 | 2025-11-30 00:03:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd47549e-8705-3181-8b58-f9586446229f | -2.6355 | -45.482601 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6513677b-13a4-3d82-a2cf-71ed5f8e1629 | -3.3382 | -45.5495 | 2025-11-30 00:03:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0480a605-1319-374f-bfb7-f3faafff020e | -2.3999 | -45.621498 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a2e9fc1-0d06-3c79-b47a-af2a105faffd | -5.5491 | -39.665901 | 2025-11-30 00:03:00 | METOP-C | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3fa462c1-422a-334f-bb24-8f7fec70634a | -3.2078 | -41.559399 | 2025-11-30 00:03:00 | METOP-C | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 10c160c7-9bf6-32ba-9001-2d046c3e60b6 | -7.1611 | -38.241901 | 2025-11-30 00:03:00 | METOP-C | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| a6de365e-e1ef-3380-9a75-575e8d6d62c0 | -2.439 | -47.0672 | 2025-11-30 00:03:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7423b3-39a1-3771-89c3-946222ed1083 | -4.2713 | -40.662701 | 2025-11-30 00:03:00 | METOP-C | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 212e179d-ccd3-30fa-8468-f4755931ba2b | -5.7402 | -40.820801 | 2025-11-30 00:03:00 | METOP-C | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2122be4c-2b44-3ded-90a5-26240a90412e | -2.8443 | -45.361301 | 2025-11-30 00:03:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08f13611-359c-3924-a6dd-31a7f6a51681 | -2.6865 | -47.394001 | 2025-11-30 00:03:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e0be3b6-2c6f-37c5-8faa-28fefa3fb6a5 | -4.3641 | -43.1628 | 2025-11-30 00:03:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11ab45cf-8b1b-3951-86f6-1ebe6e4e49a9 | -3.4418 | -42.225601 | 2025-11-30 00:03:00 | METOP-C | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3b0f4799-5497-39d3-b0a5-a74cb8f58d52 | -2.6331 | -45.472198 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b45ee23-c338-3ff2-b949-32c96e422bad | -3.9355 | -45.835899 | 2025-11-30 00:03:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42be3770-4328-3a61-83dc-4ba290146f8e | -8.0325 | -43.119202 | 2025-11-30 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 64f5ed7b-45d4-3481-9a53-f07dc3def2d9 | -2.2904 | -45.137199 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 70ae214c-b45b-38a5-965c-2a41b85391c7 | -2.7273 | -45.206799 | 2025-11-30 00:03:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 738152cb-02dd-3126-a40c-04db0fafef4c | -2.7709 | -47.4048 | 2025-11-30 00:03:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 662b6034-068e-3607-9d36-cc0625b79083 | -2.412 | -45.629799 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a84134d7-40e4-301d-95e1-1d415eb330e0 | -2.4419 | -47.080299 | 2025-11-30 00:03:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ce73d2f-fff1-39b3-9ecc-d1b5e490c704 | -6.4411 | -39.688099 | 2025-11-30 00:03:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fc66eb48-c116-381d-bbbe-3e3b6f1c35ea | -2.4322 | -47.082401 | 2025-11-30 00:03:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c61c4de-fbe7-30e1-bda2-1968d1e221ab | -3.2596 | -40.838001 | 2025-11-30 00:03:00 | METOP-C | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| eb9ba7c2-1a31-3ef6-813c-2987bc2c651d | -3.1904 | -44.435699 | 2025-11-30 00:03:00 | METOP-C | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d16a35a7-a6ce-305d-bf0d-eeebf7d42ac6 | -3.1478 | -43.154301 | 2025-11-30 00:03:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ce99eac-fbbf-3399-8515-d189382b0275 | -3.3693 | -43.815601 | 2025-11-30 00:03:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbb6d02a-20e6-344b-86be-5d899e8498a5 | -3.5511 | -43.9375 | 2025-11-30 00:03:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5576d8b2-e9ad-319f-ada3-c449efaa1201 | -3.5829 | -41.667702 | 2025-11-30 00:03:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 98f34bbf-bd30-3d12-8703-e242e39c9c16 | -8.0246 | -43.130199 | 2025-11-30 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| addb4f42-df42-32b0-b994-b619a116841f | -2.4097 | -45.6194 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 669505f2-413c-3be3-be0c-3a4b3c028bdb | -6.4003 | -39.690201 | 2025-11-30 00:03:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0a2f86dc-a204-3a18-9250-638e2b659496 | -2.5126 | -45.574902 | 2025-11-30 00:03:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 900dd611-6dab-3abe-b171-6d45e9cf19cc | -3.5927 | -41.665501 | 2025-11-30 00:03:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e6b4e67-3dba-31f4-8f22-79b5985f89d4 | -3.3944 | -44.1091 | 2025-11-30 00:03:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e427051-eb74-3f21-8c37-d8dd593b7a0b | -4.3622 | -43.154701 | 2025-11-30 00:03:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c3bc795-1793-3e6d-ad1d-49b683303a8a | -4.3543 | -43.164902 | 2025-11-30 00:03:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd0aeb3-72d5-39a3-bda4-405e2e4a2cdb | -3.4435 | -42.232899 | 2025-11-30 00:03:00 | METOP-C | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2e35fd7f-ba4b-3512-9df7-65bca8b48d42 | -6.3988 | -39.6833 | 2025-11-30 00:03:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 794c88bf-60f7-3a99-909e-05d232b952e9 | -8.0227 | -43.1213 | 2025-11-30 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61fa56cd-a354-3a6f-86eb-a3e2e5375554 | -3.6872 | -42.2174 | 2025-11-30 00:03:00 | METOP-C | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cecd7740-2d11-3bc2-9eb8-0176d02cb201 | -2.8442 | -45.862 | 2025-11-30 00:03:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4aabb454-abc5-390e-ad51-26507bcc0912 | -8.0442 | -43.125999 | 2025-11-30 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 64257d8a-cf80-395e-8f98-bf98990cfd24 | -4.5127 | -44.744499 | 2025-11-30 00:03:00 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5ab1328-2593-3019-8eb2-3fdd240a76f9 | -6.4427 | -39.695 | 2025-11-30 00:03:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1185c93e-2775-308c-b68e-057647820a96 | -2.3415 | -45.5905 | 2025-11-30 00:03:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08910e1a-bb85-395b-9bb2-09d05e7ff2bd | -3.5412 | -43.301201 | 2025-11-30 00:03:00 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aae51d82-00f5-3968-99f4-5075f10add8f | -3.9706 | -44.02 | 2025-11-30 00:03:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b7ac770-5f3a-359b-9550-a1bbea3e85e2 | -2.7349 | -42.605701 | 2025-11-30 00:03:00 | METOP-C | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8db29837-63cc-3ba4-881c-ce157f1e64ff | -2.316 | -45.8405 | 2025-11-30 00:03:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 80b19fc9-ded0-35df-b563-b510744018cd | -3.654 | -40.893902 | 2025-11-30 00:03:00 | METOP-C | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
