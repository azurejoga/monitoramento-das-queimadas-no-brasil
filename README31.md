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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b5cbb9b-a4b1-3f4d-8c44-7a4739492434 | -11.7983 | -57.2231 | 2025-06-21 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 4e601116-2dfb-3966-934c-2fb94621237a | -7.8816 | -47.8745 | 2025-06-21 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 451bd68a-cda9-3d42-8171-6a7e44c2420b | -7.2163 | -43.5603 | 2025-06-21 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 9fe2b5f9-07b4-3cbe-8f63-abb99f5f8f55 | -11.7791 | -57.2445 | 2025-06-21 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 177.2 |
| 3afb893e-16bc-3f66-8b49-d9796572f1ea | -8.2015 | -47.7804 | 2025-06-21 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ff3f4cb5-00d3-3c53-89ec-fc52a391612f | -8.1827 | -47.7821 | 2025-06-21 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 53fa0e4f-c60d-3cac-b546-53d0d3b78c04 | -12.58 | -58.3927 | 2025-06-21 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| dd0ea413-3f82-3cb1-972f-872cf86da4fd | -11.5779 | -44.8413 | 2025-06-21 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 28b3abba-fcf7-37ac-adeb-ad25094fd7da | -9.4648 | -57.8449 | 2025-06-21 14:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| d47f58d1-2dda-34c9-acc0-17fa2bbcb967 | -10.876 | -53.7614 | 2025-06-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 765b9d98-dacc-355a-9881-6f4309e355f4 | -10.9018 | -56.4552 | 2025-06-21 14:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| c11b1133-e1e9-33da-acc6-a4300fc61ea8 | -10.883 | -56.4567 | 2025-06-21 14:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 222.1 |
| e92a1b92-82eb-302c-9491-3982d7918a27 | -12.58 | -58.3927 | 2025-06-21 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 637e0185-4aec-336d-86f7-0b43b9b205f2 | -11.7983 | -57.2231 | 2025-06-21 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 2fa314e5-7ade-3d1e-bf5a-c0ab17e7d1e0 | -10.5051 | -47.5845 | 2025-06-21 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 435e3976-0462-3243-ab5c-5e02341b0f2e | -10.8571 | -53.7631 | 2025-06-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 694bc1cc-61cb-3238-9224-bcd2c5ebf505 | -10.8568 | -53.7836 | 2025-06-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 9c3426f4-0a5a-33c9-8168-beaa2ac4b557 | -8.2015 | -47.7804 | 2025-06-21 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| c25cc214-76e7-301d-b8f8-3f436749e6d6 | -11.798 | -57.243 | 2025-06-21 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 309.4 |
| cfc2adcf-fc30-374c-b352-c3d731e942aa | -10.876 | -53.7614 | 2025-06-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 387cfc2b-fda2-3ac1-b608-4954f9dcd8ef | -7.2163 | -43.5603 | 2025-06-21 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 49c10139-5a34-32a8-af11-c2d9e7126885 | -7.8816 | -47.8745 | 2025-06-21 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 920b0899-0673-37a2-b87f-d3abe35a9241 | -9.465 | -57.8252 | 2025-06-21 14:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 1789c111-9c99-30ff-a736-d52ea03f66ac | -11.7791 | -57.2445 | 2025-06-21 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 157.4 |
| a125bdef-4c3e-3430-883c-ea2807bfb0c5 | -10.883 | -56.4567 | 2025-06-21 14:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 181.7 |
| 3362b842-5321-3e54-9c01-253b48bb0f20 | -8.1827 | -47.7821 | 2025-06-21 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| fca81677-7d8a-3a2f-9c37-9f97e1f91092 | -10.9018 | -56.4552 | 2025-06-21 14:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| b86b3992-c56c-3b9e-85be-062cabf545d8 | -9.4648 | -57.8449 | 2025-06-21 14:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| e5c249c3-6ea1-3558-b93f-d70fdec8e72b | -7.8814 | -47.8964 | 2025-06-21 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| be8c9de6-7776-37a9-98e4-4f7909681382 | -10.8828 | -56.4767 | 2025-06-21 14:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 262.4 |
| 53afc207-cd66-3765-be9d-ca3fbdc547a6 | -8.2018 | -47.7585 | 2025-06-21 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2c34e104-bc5c-3f8c-8ceb-75f82ec5c523 | -11.5779 | -44.8413 | 2025-06-21 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| f9988bf7-95e2-3f69-abb4-0882b35e70f8 | -10.9018 | -56.4552 | 2025-06-21 14:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 175.0 |
| 286c4065-638d-379d-8928-5d8c209ec443 | -10.8828 | -56.4767 | 2025-06-21 14:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 264.7 |
| 1da15776-d78f-3c30-bbde-566b2594f9a4 | -12.5802 | -58.3729 | 2025-06-21 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| e4373c05-58e2-31ab-a0f0-ba9001f5e26f | -11.5779 | -44.8413 | 2025-06-21 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 1a71121a-9d83-345e-b74c-30f8a9f106ac | -9.4648 | -57.8449 | 2025-06-21 14:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 3a74b421-8460-3b37-ad3a-26c2330a4b5b | -10.8568 | -53.7836 | 2025-06-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| ffd6996c-bb88-3778-b009-c5f095c01179 | -10.883 | -56.4567 | 2025-06-21 14:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 244.4 |
| 7073c3a5-8a64-3e5b-9129-41a32955fb7f | -8.164 | -47.7838 | 2025-06-21 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 5b54cdb9-3df5-358e-a0ab-b7d9d97a814e | -11.798 | -57.243 | 2025-06-21 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 283.4 |
| 6c44dd0c-d9d8-3ec9-8651-cd04450f0464 | -10.876 | -53.7614 | 2025-06-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 6e01b16a-216c-31ab-9b0d-75c582d2f13f | -7.2412 | -44.6897 | 2025-06-21 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| a1600efc-7818-3c0e-b2da-10b6b5b33cf0 | -12.58 | -58.3927 | 2025-06-21 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 28a50c9f-65c6-3e4c-b944-5d3952007ccf | -9.465 | -57.8252 | 2025-06-21 14:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9bad2941-b5d2-316f-94fa-a7871db35bce | -8.2018 | -47.7585 | 2025-06-21 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| bfaf941b-2b07-3161-b1e8-d370b4405072 | -7.2163 | -43.5603 | 2025-06-21 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| f440f0f9-4a2c-3bd4-8003-446a5f790c4a | -7.8814 | -47.8964 | 2025-06-21 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| c9e988a3-f120-39b4-ad19-fd554b72141b | -8.1827 | -47.7821 | 2025-06-21 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 0cda0bf3-bbb1-3acb-a95e-c003f88599be | -8.5911 | -51.5537 | 2025-06-21 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d84e8f8f-38a9-3997-ac53-6f319d08907d | -7.216 | -43.5836 | 2025-06-21 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c37dcf5f-bb5c-387e-8cc7-6a57e4e8fd90 | -10.8757 | -53.7819 | 2025-06-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 127af205-461a-35aa-9794-1a05e275cda1 | -10.8571 | -53.7631 | 2025-06-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 969e244c-f064-33f4-a26c-24c8901bb670 | -8.2015 | -47.7804 | 2025-06-21 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 9dd7eaef-4a42-3a47-aae4-dfe6e7659c7a | -11.7791 | -57.2445 | 2025-06-21 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 160.3 |
| f80353c4-fa08-344e-85fb-549e67e40821 | -11.7983 | -57.2231 | 2025-06-21 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| d0aba0da-1b7e-3487-ab98-86e37492f47c | -11.7983 | -57.2231 | 2025-06-21 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| f7b4484c-47a8-331d-97d6-b59f80ec92ab | -8.2018 | -47.7585 | 2025-06-21 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ac3949ee-8311-3ef3-9a71-f006fffa0feb | -8.2015 | -47.7804 | 2025-06-21 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| aedb79f8-5986-3f19-acf2-192190bbf37d | -9.465 | -57.8252 | 2025-06-21 14:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6f9a6f13-2982-3e62-a304-89de42a0ee1c | -8.164 | -47.7838 | 2025-06-21 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 12c354c6-edb2-39cc-aae4-022ed1e069d2 | -12.5802 | -58.3729 | 2025-06-21 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d20ee0d4-41dd-3702-8e42-2a9f8f468e6a | -7.8814 | -47.8964 | 2025-06-21 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| bb7a7972-cc62-30a2-bdd9-b4b2c1269b1d | -9.4648 | -57.8449 | 2025-06-21 14:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| a6908685-c2cf-36f0-a67a-d7b0a166b9bc | -12.5613 | -58.3744 | 2025-06-21 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 6affe700-83b6-3b03-9438-aeabf5aa1ae9 | -10.8568 | -53.7836 | 2025-06-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 473a8f30-7255-3b0f-892f-3b85e340f15c | -11.798 | -57.243 | 2025-06-21 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 320.9 |
| 1ee7bf9b-df97-3c8d-abbf-9f74e0ed6197 | -10.9018 | -56.4552 | 2025-06-21 14:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 152.7 |
| c6f35505-1e3b-367f-9792-8a54860a6659 | -10.883 | -56.4567 | 2025-06-21 14:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 225.8 |
| 224c844f-b667-39c4-8128-68e0d1025562 | -10.8571 | -53.7631 | 2025-06-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 7100d557-850e-301f-9479-dc6f1c69266e | -12.58 | -58.3927 | 2025-06-21 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 1e4200f2-73a1-3f7a-8c66-1ce5444c12af | -10.876 | -53.7614 | 2025-06-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 4d2294dc-9ca6-38f1-a88d-7fc7c1b49c55 | -10.8828 | -56.4767 | 2025-06-21 14:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 277.4 |
| 13fe8fb0-d734-35a1-ae9f-d66f97282236 | -8.1827 | -47.7821 | 2025-06-21 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 264d2b43-0514-30bf-8937-f96842367627 | -11.7791 | -57.2445 | 2025-06-21 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 195.6 |


