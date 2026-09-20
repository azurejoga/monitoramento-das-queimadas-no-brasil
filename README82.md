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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1eff0b7c-1669-3771-a328-1e79b6a6b582 | -14.91745 | -49.91593 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e85036e-f249-3604-b470-8535d4d56f01 | -18.37531 | -49.4012 | 2026-09-20 04:42:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 192c9cbf-6061-3dc4-9fcf-39f0958f5523 | -17.98832 | -49.20509 | 2026-09-20 04:42:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 969aa078-f4d2-3c82-b967-2b69b667f2a5 | -14.03136 | -52.09118 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43f19ed1-2a3a-3154-aefa-28b89029ad09 | -15.80761 | -48.18957 | 2026-09-20 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fd598c1-db1e-3748-b245-301063361a97 | -15.47321 | -48.41495 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6111d7b7-2b00-3b20-9124-722fc7fe0471 | -14.92907 | -49.90691 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4354324-bf77-3d38-afbf-b0eb0fc58246 | -16.31143 | -53.84923 | 2026-09-20 04:42:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37718d82-bfe9-376f-9fb3-e2d2ac381cd6 | -19.87363 | -49.00495 | 2026-09-20 04:42:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| cfe25ef8-32e6-3f39-a91a-cc6553f980b0 | -14.69323 | -46.68441 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d9a85c1f-9c8e-3e42-bab8-deb839b34351 | -14.60968 | -48.10758 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e17ad9b9-65c8-3a57-aa81-247d1ceb7c14 | -16.82732 | -47.64157 | 2026-09-20 04:42:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1337c6fd-f506-3d7e-9fcf-217210e258c9 | -14.91358 | -49.91894 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd4fffbe-ef20-3ebd-abd6-2f6a54d15937 | -14.6896 | -46.68385 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9a8d4969-5150-36a7-8d65-6f8ff4dba802 | -18.60671 | -48.2098 | 2026-09-20 04:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c33bfea-2823-3875-bd30-eff94a3c0296 | -14.95577 | -47.53683 | 2026-09-20 04:42:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7521a381-3fe1-3fee-92b4-9eb982490060 | -14.67627 | -46.69939 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8095c473-8501-3e95-855c-8b6def92a64b | -14.61024 | -48.10382 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cb228f5-8acd-3c43-b10e-61740c77c6a5 | -16.97596 | -48.63066 | 2026-09-20 04:42:00 | NOAA-20 | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52d75839-6bd9-36e5-8f74-d29846522ecc | -14.05273 | -52.09117 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0735f082-9b81-3d1a-a5fa-2bed92f9e7ea | -16.09588 | -49.29776 | 2026-09-20 04:42:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9c21f27-549f-3f85-acf1-7132f637574e | -19.32696 | -46.36686 | 2026-09-20 04:42:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74a212cf-33b7-3de5-8b8d-774b3e1663d8 | -18.55494 | -47.23803 | 2026-09-20 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2977c08-f31d-3e0a-a3d7-85b90c1b5385 | -14.59711 | -48.09817 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd5d9497-8923-3758-b492-7d405d9ec47d | -15.4789 | -48.42348 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9800765-46df-3d57-aa24-7f352a4b45dc | -16.58025 | -51.62307 | 2026-09-20 04:42:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85c6feb8-a458-33b6-84c7-e0c4a15b74c5 | -15.46986 | -48.43747 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9157b729-a530-3990-a3de-3c1e11c08251 | -15.46645 | -48.43701 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2004c473-ef75-3b5b-9024-6a3d8480b4b5 | -15.46805 | -48.42222 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b990ccdb-d014-31cc-a3fa-a4628b19aa1b | -16.32168 | -53.85444 | 2026-09-20 04:42:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d8c5a79-c6e0-38ed-a39a-326cbdaeac2b | -14.95988 | -47.53315 | 2026-09-20 04:42:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de4894dc-829c-39f6-89a5-b2374c03bcac | -15.4692 | -48.41468 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b665e3a0-93d1-348e-990f-f2131a4ed056 | -16.30779 | -53.84852 | 2026-09-20 04:42:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c981c5e9-5fa7-3a76-856b-8138807ae375 | -14.66786 | -46.68056 | 2026-09-20 04:42:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 93fc091b-8242-39cc-9d44-f7e21ed3012a | -14.9147 | -49.91181 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac688f60-3e85-389c-8080-15c88951aad3 | -15.46812 | -48.42577 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a91f9d0-4b72-3fb3-bc03-8d4863cead04 | -14.67148 | -46.6811 | 2026-09-20 04:42:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bd95ef2f-306a-3fe7-83d9-838c47a0a909 | -17.03494 | -47.28237 | 2026-09-20 04:42:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11aac014-013a-3a73-a924-8eb11c191c9f | -14.79297 | -48.53484 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a40f8181-cb70-3958-bafd-157da5bf3372 | -18.00038 | -48.03724 | 2026-09-20 04:42:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50aca03f-9309-3fce-bbba-308600d1fb12 | -14.05618 | -52.09182 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 43b6da56-6041-3b9b-ae8d-e63db0219a79 | -14.93238 | -49.90747 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a94ac341-a4a8-32cb-a1d1-867e7acd0c91 | -15.47041 | -48.43375 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2eb0d607-77fd-3ad3-b20e-382ef6893bb8 | -16.52621 | -48.73983 | 2026-09-20 04:42:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11b10d22-d83d-3cd7-8761-44d015824e0b | -16.53673 | -49.10527 | 2026-09-20 04:42:00 | NOAA-20 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 348b3083-1d0e-359e-bf7e-f07e37a20f51 | -16.59162 | -45.33086 | 2026-09-20 04:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b924788c-3065-389b-916c-6977d2be40db | -15.89813 | -48.07225 | 2026-09-20 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fba0922-b8e6-329d-9a13-6451f04ddc04 | -14.61366 | -48.10435 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51b0fb00-4e61-39d8-a605-d260bf8c6e5c | -14.66874 | -54.4636 | 2026-09-20 04:42:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf5f1730-291e-3d0c-ada9-8b853c850315 | -19.19242 | -46.84076 | 2026-09-20 04:42:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 637a10cd-6879-3113-98e0-be16407687ed | -18.00097 | -48.03315 | 2026-09-20 04:42:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfb7f502-158c-3221-acac-a72854f5b1e9 | -15.46924 | -48.41826 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2779d78-eafe-3b15-b2ba-9ee778f94701 | -14.92132 | -49.91292 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7852032-5cc2-39d4-9274-8fc5e9ee8ff0 | -16.33423 | -49.51583 | 2026-09-20 04:42:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a44beced-0090-3e61-82eb-6fb36650d8b1 | -14.5538 | -48.91657 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13f80466-7241-32a2-be73-279e9cfd3e73 | -15.0128 | -48.56171 | 2026-09-20 04:42:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e630e6a-36f7-3844-b84d-46adef4a3ed4 | -14.68837 | -46.69246 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8ea044d7-8e93-3797-9f76-5049f62595a4 | -19.02379 | -46.91951 | 2026-09-20 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7074d2a4-c541-34ee-8f7b-cc19a176302a | -14.04928 | -52.09053 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 62c54b4b-1248-33f5-9149-689939d5f9f1 | -19.32703 | -46.36518 | 2026-09-20 04:42:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10b66901-68f7-3b14-a750-d2793a3547bf | -16.89599 | -48.8133 | 2026-09-20 04:42:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80b6f8f9-2f25-3c97-8c15-bab822553415 | -14.05683 | -52.08796 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2e3b9a05-eae0-3310-956d-ed6d0faede2d | -14.66488 | -54.4629 | 2026-09-20 04:42:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcfbaf73-dd9f-3acd-88c1-1238d5c63d19 | -16.43647 | -40.5523 | 2026-09-20 04:42:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 774aa09a-bece-3ce1-a4e2-3199181c2278 | -14.68899 | -46.68816 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 005f0223-e80d-3cb2-b7e5-d300d653c327 | -15.86539 | -49.91224 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcce8ac1-7d94-3fc8-bc66-53df125235dc | -14.04302 | -52.08538 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bd4af045-b586-3a57-992e-f28abfe840fa | -15.46577 | -48.43721 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 862734ba-4d16-3fae-b9c8-dc04c2cfd137 | -15.87922 | -49.91083 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 799757b6-08e1-3a4e-988d-e9d89359731f | -15.45783 | -48.44367 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0850b50e-1573-36be-adba-6ca475a3cf31 | -15.47326 | -48.43798 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 24316d35-498b-3059-87a9-bca8611b5099 | -15.87146 | -49.91692 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c025fa2-bebf-3238-ae0f-a1ee12ac64d3 | -16.88516 | -50.59394 | 2026-09-20 04:42:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a483244f-e577-33e3-a28e-89c7aa9ead03 | -14.78622 | -48.53374 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a497763-2d9a-3072-a38b-1c65ec35f302 | -15.45549 | -52.82822 | 2026-09-20 04:42:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe1a60db-c91d-319a-a5d6-e496dee6f9e9 | -14.92795 | -49.91403 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92146a27-8fc8-3243-b5c2-e03096c1e12d | -14.92733 | -49.9395 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81a3483d-f975-3fd2-b5f6-15aa658f76d5 | -14.92076 | -49.91648 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 516cbcca-d9b2-3bc3-92e8-b48a6293721a | -14.6775 | -46.6908 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3b1b8231-b3f2-328f-babe-3c248ee383b8 | -17.01742 | -47.1462 | 2026-09-20 04:42:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8eb0b766-0a4d-3736-9514-173f65082d0e | -17.01441 | -47.14125 | 2026-09-20 04:42:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3ddb811-3af9-3f01-a0ab-071baa6c3b5b | -14.79125 | -48.5686 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed759fec-3e49-381b-9dfc-fd9a94f1ed2c | -16.73743 | -49.35994 | 2026-09-20 04:42:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8c3725a8-41c9-3846-a89e-11dce6df3d25 | -14.42844 | -55.57223 | 2026-09-20 04:42:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa63d735-6086-32d4-8bbd-41f8ecb0c2b8 | -14.05338 | -52.08731 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 673c7863-0ccc-3fc4-a783-6372f2d0a6c7 | -14.68112 | -46.69135 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6ffa004-f1c4-352a-bb92-11e5c27c8fd8 | -14.68598 | -46.6833 | 2026-09-20 04:42:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d264a3e1-3625-3bad-9666-94e8e2279f16 | -15.87202 | -49.91334 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28bba3c8-daf4-369e-a826-355c2b06c563 | -15.47382 | -48.43426 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| baf4f1a1-d139-3ee6-82d6-822a70352c27 | -14.68413 | -46.6962 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf8e7548-b4a4-3b2b-a607-6e441a988dc5 | -14.7597 | -48.41217 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e170f02-2fbb-30e0-b654-3533ad7b4cca | -16.32077 | -53.86055 | 2026-09-20 04:42:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4442f628-76d7-3640-b133-2c0cb79e3337 | -14.93569 | -49.90802 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca69f207-a57a-32de-be88-2976131c4d2f | -16.10059 | -49.64451 | 2026-09-20 04:42:00 | NOAA-20 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61d99584-1c03-3044-a240-4ad50130e460 | -18.67678 | -47.05784 | 2026-09-20 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b077a9e1-d873-3c70-882a-97819bd4413c | -14.60054 | -48.09858 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b46c7960-6578-3a40-88e5-9c2b85dd43ba | -14.67388 | -46.69025 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 67248086-ccef-3dd6-9e09-a0f640c7c120 | -14.95637 | -47.53268 | 2026-09-20 04:42:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65394a12-7f31-310a-80f4-9327321b98b3 | -15.17222 | -48.15883 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8845a5b5-cf32-3f4f-b41f-13f8d4281dd2 | -14.69261 | -46.68871 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |


[Clique aqui para ver as próximas entradas](README83.md)
