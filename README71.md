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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5345e658-90e9-3f9a-a5dd-8c2f7d4f3af8 | -10.85455 | -47.90273 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ccd07d2-443c-3fc1-8721-bab3de01db92 | -12.69261 | -48.44131 | 2025-10-29 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b791432c-f8f1-3c1c-a240-9a70e28f29b9 | -13.64032 | -47.0425 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9af3ba3f-76e9-3f13-b210-76f5562c878f | -10.60254 | -49.62037 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e56efe0-b02a-39e1-8c5d-c54213f3c9ab | -12.87381 | -48.63226 | 2025-10-29 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f56179d-c682-3f39-ba9f-8faeecedb5e6 | -9.57823 | -46.93923 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e352b333-c72b-3a35-8d1c-41fdbcc06aa8 | -10.63832 | -45.24522 | 2025-10-29 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98b94a96-07a1-3740-8c7d-980b23fae6cd | -14.61189 | -48.43055 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9493f18a-67f5-3a67-9c25-e8d189867c5f | -9.91415 | -45.934 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3952c00-5b4d-3f6a-84e7-e057bff59ece | -14.26071 | -48.10649 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7ea71342-444a-30d2-8873-30322012669a | -13.66316 | -47.17433 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bc1ca292-2eca-3242-8d64-b594debefd40 | -10.91935 | -48.26259 | 2025-10-29 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e73eae3-a3ba-3cc5-9807-c4093364d8ab | -13.18754 | -48.43661 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df7d4c0f-f2a8-3358-aa0c-25ebde2b24bf | -12.14258 | -45.21177 | 2025-10-29 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6f55bf7-10bf-399e-9884-1ada959369c1 | -13.63999 | -46.49443 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be5d15bf-6d0d-3c72-8537-be043582715b | -14.54896 | -51.00063 | 2025-10-29 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80eaed25-5cd4-359c-b5f5-6524987241e5 | -13.63787 | -46.51084 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 794b8488-39e6-37e6-ac69-02c7e4807d96 | -14.59594 | -48.40377 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17c83f5b-3a57-3110-92e5-e9b1b1f5b547 | -13.69593 | -47.67495 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7b77b7a-b3d5-392f-bb7c-9b0ac700c37d | -11.02973 | -47.84019 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d30cd22-ea28-3a21-acfe-dc469e1aa939 | -13.54841 | -47.35101 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e73b250-71e4-3c9c-8fc5-93e0e02e15d4 | -14.30593 | -46.53501 | 2025-10-29 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59f91455-1bac-34fc-a4f6-1fa956353903 | -15.15385 | -47.23005 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71acacc7-d6de-3886-a935-066d2b1b3e00 | -13.42958 | -47.37288 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57a75fd5-7be9-36fa-8b91-f717aff32e08 | -11.78503 | -44.1679 | 2025-10-29 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d63721db-466b-31e0-8ba7-21fad3124169 | -13.21184 | -47.05429 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4686c67-b85d-3a76-b7a3-2129849a0c85 | -9.92933 | -47.67687 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e73c7d78-c73e-3794-a026-393b057ceab9 | -10.65506 | -48.00135 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 92ac3db5-a9ba-39f9-ab8a-07f2ad957f09 | -9.03308 | -47.7229 | 2025-10-29 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6847affc-6716-34cd-9fb0-a30abb82d57d | -13.30885 | -47.70618 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b633730-8878-3deb-b88a-882542dd52ba | -13.63897 | -46.48429 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6502109-88a7-3add-8ac8-795209911545 | -13.58171 | -49.59562 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| efc5bcc3-5f5b-37d6-a6a0-5c4ee833d90f | -9.90768 | -44.91576 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94f31ee0-ba21-35bb-a2fc-0a802cab25fd | -10.38286 | -45.30819 | 2025-10-29 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0115330d-30f8-31cd-8fa3-6c313f7cfbb8 | -9.23214 | -46.35031 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3e980e9-c8c2-36ee-be45-06e375a8cea2 | -12.15503 | -47.69406 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6a3b93e8-2e9f-3776-977f-03a992a53c18 | -12.85923 | -47.23541 | 2025-10-29 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a392b000-871e-3b84-8c02-b09fffe99b3a | -10.90648 | -47.80957 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 61f1d152-2528-32e6-a813-e1633ac63adf | -11.26905 | -47.5398 | 2025-10-29 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e00d542-1563-3ce1-9784-66995679868c | -12.40852 | -44.70706 | 2025-10-29 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38b473ee-47b7-38da-b51f-2e9d71316366 | -13.9154 | -48.47286 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ec7ffac-5617-3f40-b622-32f26f997346 | -11.58606 | -47.946 | 2025-10-29 04:46:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8959c796-c3d4-3f2a-8459-d3014e2b0114 | -13.63728 | -46.48148 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f689d33e-26fa-3e2a-b5d2-1e93db9e98e8 | -9.80161 | -47.75934 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bf2f1076-5965-3f89-bc51-b41bd781b566 | -13.22599 | -47.72947 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a73b39b8-5709-376d-b1f5-85a9621d2235 | -11.70486 | -46.70316 | 2025-10-29 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03bf96a5-c7d8-3b3e-a860-b8410470b21a | -12.15434 | -47.69888 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f1087b3-bb06-3bd2-a719-b7fd079f4f07 | -9.01943 | -63.5717 | 2025-10-29 04:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28ee9786-7b1c-3936-91b7-2c42dd2336c9 | -12.15927 | -47.91117 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b03a9114-7d61-35dc-8671-35e2b95bb874 | -13.36852 | -47.42153 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 282f1318-f248-3e80-aea8-cf4e5cf12d19 | -12.76679 | -46.65777 | 2025-10-29 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22feefce-125a-36d1-a48b-4d5b9b11fa01 | -15.30642 | -48.05506 | 2025-10-29 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6550ab78-b4cd-36b6-8d70-58b74b0f2496 | -10.96758 | -47.84056 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e140ab5-57eb-3310-8053-d727dcbf7804 | -13.17349 | -48.45446 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dd016f1-8d1b-392e-b3a5-e860e0ed8382 | -14.54204 | -48.00628 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ae0c20e-de8d-3d0a-b41f-c0f22fcd2e45 | -10.74742 | -44.75447 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e66858b8-d33f-3a52-ba1d-d916398b8027 | -13.64371 | -46.46562 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7179e841-f2a2-399b-988c-6466fb6061f6 | -14.26247 | -48.12241 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 48252ee2-44b5-3662-accd-1e1b03dbf013 | -13.5764 | -49.60709 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c74821d-5ba3-3beb-9d83-32dc1629e08d | -12.54318 | -49.58738 | 2025-10-29 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9c08423-541a-3fd5-b1e0-8341adfc628b | -10.85023 | -49.14149 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 16e394df-5ea1-364d-862b-414c4ecf18a3 | -12.771 | -46.65826 | 2025-10-29 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 945264fd-83f6-3bd5-9680-ecb9ccbd1eca | -10.84868 | -47.89052 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53779e90-ad0b-3736-afe3-1d077cd65c50 | -13.59821 | -48.42341 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4631dea-ec53-3173-b19e-48d63e59450b | -9.58841 | -50.78762 | 2025-10-29 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00431547-f669-322f-95bb-82e146d661d7 | -13.5435 | -47.32589 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d07d9d2-75ee-3ec4-911a-b82a7622fa09 | -13.62342 | -46.46971 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 28e42b1b-1603-39fa-a2d0-28d2e21444c0 | -15.20532 | -47.2272 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd653dc8-e9b4-35ba-85e2-2677538e2fbe | -15.19574 | -47.20264 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f58d77bb-c6f2-3bb9-b0d8-ea1c6b2a65d1 | -10.65314 | -48.01466 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c38f993a-c8d9-3d92-900c-b0e967cdd355 | -9.80456 | -48.38268 | 2025-10-29 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08236fa6-f8b4-3a95-9ac3-a01690579ef0 | -13.69668 | -47.66926 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c120d7e-a062-3053-acd1-d66960fdfaa1 | -11.25854 | -45.52929 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1e5dd3ae-453e-3ab9-a24c-a699c5b26258 | -13.568 | -49.58957 | 2025-10-29 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0f3c0b6-d947-3789-8ba3-e80f98d11889 | -12.85456 | -48.63406 | 2025-10-29 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8c844a2-f46a-31b5-af6d-6848b44c63e0 | -12.65568 | -52.62686 | 2025-10-29 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b62d7515-1ac1-37b5-a30c-bbe14cdd1ea4 | -13.15236 | -47.0912 | 2025-10-29 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a195ac7-570c-357a-b323-1937f65858af | -12.37251 | -50.1605 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e7c45ac6-aa02-31e8-8045-7abdd35fc5ca | -14.49618 | -47.87818 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e24ae38-23f9-37b2-8730-37d62e2c2245 | -13.35695 | -47.38606 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85d543fc-1379-3242-a51d-910e2b452610 | -14.51657 | -47.96423 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99a77cfd-cae9-35c6-b798-94410f1ed205 | -13.69389 | -47.69011 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d9c8bb1-f83f-3d3b-be45-9370bcecaeed | -13.41918 | -47.38895 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cb5291d-aeda-3324-8956-352b687fcb31 | -14.60167 | -48.41925 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 361e7f91-61d6-3049-a68b-c48be2c91c04 | -13.21491 | -47.06245 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49c35378-772b-3dcc-a5c3-308db863406c | -10.54867 | -45.04728 | 2025-10-29 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 414fe90b-e71d-3395-80e1-80d7ad76bd0b | -14.59528 | -48.40863 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1c58bdf-9dee-3553-9374-16e5416e233e | -8.71722 | -50.00914 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33a083db-5877-389c-ace8-b357ebb9c8ad | -9.11407 | -47.64996 | 2025-10-29 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 279f90bb-3b7f-3274-addc-28497eaeb7ac | -11.78311 | -44.16641 | 2025-10-29 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92e05492-a091-310c-a4da-6d310bd8290e | -10.52309 | -47.73812 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 341e3000-856d-35de-adbf-44be97f8fa35 | -12.00539 | -46.77845 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7dc0f9de-482c-366d-acd4-69a462590d9f | -13.41519 | -47.38181 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a08bf6a-45b0-39ba-adde-f2e7fa0bd1e6 | -13.69053 | -47.68494 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adf6f5d2-0c79-3c8a-a514-bfe9074ab9af | -15.15334 | -47.23405 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e014d1c2-9545-30e4-b5a6-5ad2e4a395b6 | -13.63946 | -46.49855 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0968d4bf-11db-329d-9f3b-a7c6246400e4 | -10.6513 | -48.00084 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bc241aed-27e8-3352-bf3c-f770628b427b | -11.64569 | -48.52971 | 2025-10-29 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81cfb7be-9602-3a8d-a1c9-25cea4916876 | -13.65039 | -46.46486 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5f45fae-c62a-3f8f-a4dc-6236f9011064 | -13.33149 | -47.48224 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README72.md)
