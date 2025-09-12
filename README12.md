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
| 8bd4d2b0-2269-3498-a8d0-de400b068d63 | -20.0192 | -47.6459 | 2025-09-12 02:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 8f723952-adaf-3dbb-af81-03fd7296bf4c | -20.2681 | -42.1278 | 2025-09-12 02:10:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.6 |
| 3cebe89e-e042-3bb1-9ca1-0412013ca270 | -11.5235 | -50.5968 | 2025-09-12 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a8ab809a-02ff-3e80-b7b7-2fad1968c765 | -22.7014 | -48.6852 | 2025-09-12 02:10:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 73.4 |
| bdd18b98-561c-33be-bce6-edc2fe2a6b21 | -21.9679 | -47.5525 | 2025-09-12 02:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 147.3 |
| f9b9f36a-4f2b-3cda-99f8-2e79ce597b55 | -19.2409 | -48.0265 | 2025-09-12 02:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 35.6 |
| eeded63f-ff8e-3541-be8b-6acf47838042 | -8.4893 | -47.2694 | 2025-09-12 02:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 93b55f73-749d-312e-8783-7353d0294bbb | -17.3566 | -46.691 | 2025-09-12 02:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cead5044-e268-306c-8ea2-8bc68c1a6d8b | -21.9463 | -47.5816 | 2025-09-12 02:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 5e6033c2-b5eb-3baa-80fb-0ee411ee552b | -20.2689 | -42.1022 | 2025-09-12 02:10:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| 134d0fab-ca63-3ae7-86c7-771d69e81f90 | -22.7007 | -48.7088 | 2025-09-12 02:10:00 | GOES-19 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e1c6db35-728e-39fa-8898-8f8dba8f8902 | -11.8757 | -58.8221 | 2025-09-12 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| fd1b5221-ce1a-34aa-86b3-dc0cf552dbe2 | -12.9292 | -54.7538 | 2025-09-12 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 0fc9ee49-e162-3e95-9943-5066d28329e7 | -21.947 | -47.5578 | 2025-09-12 02:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 65e7f914-bf62-33a2-a59d-114bc9870a8e | -11.0201 | -51.3521 | 2025-09-12 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 832f9534-7360-34b0-bb17-e9381bd1c81c | -21.947 | -47.5578 | 2025-09-12 02:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 342.7 |
| 83538913-9ed9-3ed5-9b78-15b5d90eab23 | -12.9101 | -54.7558 | 2025-09-12 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| bd3d9c1f-47d5-39e8-8e14-5f11dce99bf6 | -11.8757 | -58.8221 | 2025-09-12 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| c6bf9866-38b1-30cc-957a-27452bc788a2 | -21.6496 | -53.9886 | 2025-09-12 02:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 137.5 |
| d25f6870-c8d1-378e-a9a6-aeaff7382ab9 | -18.0661 | -45.4373 | 2025-09-12 02:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5b3510d7-d98a-346a-aef8-0d0f493792c9 | -21.6502 | -53.9667 | 2025-09-12 02:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 04766977-0139-356f-8a63-5d50da71e709 | -21.6296 | -53.9704 | 2025-09-12 02:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 64.7 |
| a3b4a402-6d49-3a2c-86c6-35fe22d2e3df | -21.9686 | -47.5287 | 2025-09-12 02:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 0a6e409a-7cdb-36bd-a55a-fc5b1c2bf55d | -21.9463 | -47.5816 | 2025-09-12 02:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 4355910f-6fe9-3a1b-8116-3e512763a1f8 | -17.3566 | -46.691 | 2025-09-12 02:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a329a5aa-3bfa-3dac-be6f-4e46de0962b2 | -11.0391 | -51.3502 | 2025-09-12 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 306fd803-2e53-39c6-ba48-7cf4ef8640d0 | -21.6291 | -53.9923 | 2025-09-12 02:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 83fab321-2403-3a50-be34-0b885a1117d8 | -14.1907 | -46.2012 | 2025-09-12 02:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| d35c2d25-a01b-362b-95c9-8369be45f9e8 | -21.9478 | -47.534 | 2025-09-12 02:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 719f31c1-7365-3258-b24a-990bbb6e3e0b | -6.309 | -42.2311 | 2025-09-12 02:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| b537f7aa-93e4-397c-8136-8de89da5c4f1 | -11.857 | -58.8038 | 2025-09-12 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 0622d7f9-cdfe-3fc6-b8ce-1ab8841aba3e | -21.9679 | -47.5525 | 2025-09-12 02:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 9522893b-f292-3cbd-9931-876c38f37681 | -11.5263 | -50.404 | 2025-09-12 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 25619ca5-ee07-3655-a95d-5f24381559e3 | -11.8759 | -58.8024 | 2025-09-12 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| d29817be-f0ec-38ae-b054-23e4cc7d8e7c | -14.1713 | -46.2045 | 2025-09-12 02:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 1a47fd0d-8d8d-3f30-8518-72f0caf4839d | -12.9292 | -54.7538 | 2025-09-12 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 168.6 |
| ff1f2b5a-dcac-3b84-aa60-64e91ceffb0a | -11.8757 | -58.8221 | 2025-09-12 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| d0fd0782-9b9e-38df-a5cd-c533f7857a91 | -11.8759 | -58.8024 | 2025-09-12 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| ef5abc5e-c962-33a5-8a12-ad5303a0730c | -6.1672 | -47.2858 | 2025-09-12 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| dc628fb4-9035-396d-8cb8-ea23b71e4ec6 | -11.4285 | -43.5544 | 2025-09-12 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| d60ec063-4658-3aad-9fff-f54a8599337a | -11.6817 | -46.5858 | 2025-09-12 02:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 346.1 |
| 5ef49300-f79a-3d60-8137-fa5b150ade30 | -11.6626 | -46.5884 | 2025-09-12 02:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 3a300a58-11fd-37c1-ae4c-a7219ac28023 | -11.429 | -43.5307 | 2025-09-12 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.2 |
| a1aad6ef-4e38-302c-a39a-56ccc945439e | -11.6813 | -46.6084 | 2025-09-12 02:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 793ea0f1-2725-345e-8398-503893a047f2 | -12.104 | -47.6039 | 2025-09-12 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| b1adb1b0-6a85-3bbc-8626-c587d82a2456 | -11.5263 | -50.404 | 2025-09-12 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ef51b64b-dd4f-3f42-a565-add1fc40f3df | -17.4828 | -39.9188 | 2025-09-12 02:30:00 | GOES-19 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 59.8 |
| e903d73b-d576-383c-b916-cef277324e97 | -17.3566 | -46.691 | 2025-09-12 02:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 41891c33-ed83-37c8-b9ab-be31825498b6 | -11.7016 | -46.5379 | 2025-09-12 02:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| bda2c7e8-b0fe-3153-811e-b80062fe38b3 | -12.9292 | -54.7538 | 2025-09-12 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| daf93658-a354-3fd9-b1ba-80bac4c96fc2 | -18.0661 | -45.4373 | 2025-09-12 02:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d9fb0a2a-31ac-38f9-8e29-876ee77b49aa | -12.1044 | -47.5816 | 2025-09-12 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 2734f703-8bc0-3d75-a5fc-ca8307bb70f7 | -11.7012 | -46.5605 | 2025-09-12 02:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d745016d-aade-338f-a9da-42d1101c4c69 | -11.9211 | -50.7009 | 2025-09-12 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 184.9 |
| c74ce55d-10e9-397e-ab52-2bf0d025660e | -6.1674 | -47.2638 | 2025-09-12 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 12f6255b-6a05-3567-ba73-5d5eb7704b72 | -11.6821 | -46.5632 | 2025-09-12 02:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 66279565-f3e2-39d6-9a00-01c5cdb6fe4a | -11.9208 | -50.7223 | 2025-09-12 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| f8d7a436-7d79-3e4c-a679-7fb1efa4509a | -12.0852 | -47.5842 | 2025-09-12 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 4ad3990a-a703-3f4b-a20b-86f23c358afa | -12.0849 | -47.6065 | 2025-09-12 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| bd3a3b82-b9b5-3f19-99a9-a7c73a16af9e | -11.8759 | -58.8024 | 2025-09-12 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 72f1027f-16e2-34f8-8389-060002ed0fde | -20.2681 | -42.1278 | 2025-09-12 02:40:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| f84bb6d8-9168-3a91-80f4-ae593eec37e0 | -19.2409 | -48.0265 | 2025-09-12 02:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 4eb63092-5b80-3b38-b12c-96d1b16032f8 | -11.8757 | -58.8221 | 2025-09-12 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 06adb05b-d337-3fce-aa04-4395fba642e7 | -20.2689 | -42.1022 | 2025-09-12 02:40:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.1 |
| 072600ae-1cf1-3cdb-b88f-f25617c9e52a | -11.6821 | -46.5632 | 2025-09-12 02:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| f2624f04-6401-3795-a478-d5d750078f1d | -11.4285 | -43.5544 | 2025-09-12 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 703159ee-4bbe-35db-b793-3663614371a4 | -9.3394 | -65.4638 | 2025-09-12 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 31853887-e515-325c-ba25-28ee787a6983 | -11.6817 | -46.5858 | 2025-09-12 02:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 474.5 |
| c0e77538-315f-3478-8405-fffd1940c38e | -21.3247 | -45.0104 | 2025-09-12 02:40:00 | GOES-19 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 59ecbe82-c6f3-3207-a20e-7c1bb18eb3db | -9.5137 | -54.6292 | 2025-09-12 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9d1d4547-d820-32e6-8d09-9603a42dcd68 | -11.9211 | -50.7009 | 2025-09-12 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| dac648e3-4406-3d93-8ca9-e22569162ed6 | -11.6813 | -46.6084 | 2025-09-12 02:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 1a782b16-ab94-3569-bd13-fb9612e5238b | -11.429 | -43.5307 | 2025-09-12 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f7c65562-b529-38c5-940f-7ec31e6b9b42 | -11.6622 | -46.611 | 2025-09-12 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| aab2937f-22f2-39c7-a716-382102bf4f22 | -11.6629 | -46.5658 | 2025-09-12 02:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 9f73ba4a-26d3-3113-8acf-3442fbc0020c | -12.9292 | -54.7538 | 2025-09-12 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3b58cf98-d6e4-3781-8592-c26195c4b2bc | -11.6626 | -46.5884 | 2025-09-12 02:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 2171c8ae-89a2-3a90-b28a-25f8f97dd057 | -19.2409 | -48.0265 | 2025-09-12 02:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 0e6792e0-b9ef-3162-81e8-649fe9f9ccd7 | -11.9402 | -50.6987 | 2025-09-12 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3121d839-8804-3151-986b-f0654c6d375b | -11.8757 | -58.8221 | 2025-09-12 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 3b022b71-615c-315a-afae-3f8f8be1fd19 | -12.9101 | -54.7558 | 2025-09-12 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f8c525c5-4890-3424-bdb7-622b10369da2 | -14.1503 | -44.4421 | 2025-09-12 02:50:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| befe0dc0-c4ea-364b-959f-104fffde4122 | -21.947 | -47.5578 | 2025-09-12 02:50:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 301.7 |
| 8105b75f-ddb7-353a-be52-ee1572584a94 | -21.9686 | -47.5287 | 2025-09-12 02:50:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 44037848-e3c8-354e-b91c-bd0df47c8c49 | -11.9907 | -51.1405 | 2025-09-12 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 0fa312e6-c1f1-30e0-ad3f-b2f5c67d0007 | -12.0852 | -47.5842 | 2025-09-12 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 549d29b8-a525-375f-b963-b054e12e8b78 | -8.8899 | -49.945 | 2025-09-12 02:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 64add576-b918-309e-ad0e-9fe082d9418e | -13.8983 | -48.2581 | 2025-09-12 02:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| d85df474-7da6-383b-9cb4-0431b0c554b0 | -21.9478 | -47.534 | 2025-09-12 02:50:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 84.5 |
| f1c947b6-e524-3c92-a55c-bd3232956045 | -11.9211 | -50.7009 | 2025-09-12 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 1ea66516-b856-37ac-99fd-bd7b3edc6556 | -12.0849 | -47.6065 | 2025-09-12 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| c7bdebe7-e3b3-3735-bd04-de8a9f7c1654 | -20.2681 | -42.1278 | 2025-09-12 02:50:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.2 |
| 79e21d20-dc57-3961-8b7e-fc9efadba374 | -11.5235 | -50.5968 | 2025-09-12 02:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 43a9c1b8-4646-3894-933d-a257824c2d67 | -12.9292 | -54.7538 | 2025-09-12 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 9df04673-65e2-340d-95a8-57ab86a9aee0 | -12.1044 | -47.5816 | 2025-09-12 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 1e3de19d-345b-336d-8682-e8a733fc34df | -9.5137 | -54.6292 | 2025-09-12 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 444f2a3a-0af3-32e7-84ff-ec9d4fd6ebac | -20.2689 | -42.1022 | 2025-09-12 02:50:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.7 |
| 2a8afde3-bf7b-327e-b664-aad6e4b6c8af | -11.8759 | -58.8024 | 2025-09-12 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 28431fd7-df44-3bca-9bd7-1ce4d057027c | -21.9679 | -47.5525 | 2025-09-12 02:50:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 203.8 |
| a3cf1de7-bb6d-3e16-98ac-d5ca155a3804 | -9.3017 | -65.5959 | 2025-09-12 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |


[Clique aqui para ver as próximas entradas](README13.md)
