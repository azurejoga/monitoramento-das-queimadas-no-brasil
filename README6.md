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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2c03540-62b8-3267-870f-8c0fa6c1ac35 | -10.14788 | -36.41465 | 2026-01-06 04:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4c90db37-9d61-3bc8-983a-10dfbcaf9ade | -4.14664 | -43.64688 | 2026-01-06 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65cd8b14-8cc9-3998-9d6c-9d517f3a7edb | -9.5117 | -36.06978 | 2026-01-06 04:01:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b0c62af5-e8db-3bc3-a6d1-4d1c361bc671 | -2.52291 | -47.83014 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2420e9e0-5bc9-3984-b59a-bfa8cd71035a | -2.6719 | -49.85133 | 2026-01-06 04:01:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf62f1c9-7670-37b6-bf66-bb8597104ab2 | -4.93781 | -37.79609 | 2026-01-06 04:01:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d9046041-dcb8-3358-8153-1b3655981323 | -10.93187 | -38.8162 | 2026-01-06 04:01:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 88068ba9-406f-39cc-8317-4b1c26e687e1 | -4.1459 | -43.65149 | 2026-01-06 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a5e6d733-8247-3eb6-aff7-75f7c065a206 | -5.18415 | -37.5835 | 2026-01-06 04:01:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 521c3831-23db-3c18-8150-ec38bde15e84 | -8.43608 | -35.58093 | 2026-01-06 04:01:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2e7d45f9-68b2-386b-9e3b-be0600f400c2 | -2.98497 | -48.59139 | 2026-01-06 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 337038a2-584d-3c05-acc3-64e7474fb90e | -3.70291 | -43.43774 | 2026-01-06 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 9dfb8987-96a5-3591-8c44-fd0c25372a80 | -3.48111 | -47.68539 | 2026-01-06 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5c51c4d-cece-34cd-8247-eab237ff2fd0 | -4.35075 | -46.32866 | 2026-01-06 04:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34d805a9-fd55-3332-aea1-49a7f9276c5e | -3.67688 | -45.2317 | 2026-01-06 04:01:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57c0d8cf-f9fe-3e6c-80f2-047a586ae722 | -3.70138 | -46.97865 | 2026-01-06 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73e71a43-7ad5-3e17-9604-0acc8986ac2f | -5.2052 | -40.5999 | 2026-01-06 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| caf581fe-5f7d-3295-bb0b-774d858d9234 | -4.1497 | -43.6521 | 2026-01-06 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ad99077b-32a9-3b2e-9cbb-8561e4985328 | -5.94789 | -35.61869 | 2026-01-06 04:01:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 71bbd6c0-24eb-34d2-bce4-d1265a776d0c | -6.95976 | -46.21937 | 2026-01-06 04:01:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cd58945-670f-3ade-8ea8-b284463dbb55 | -2.18181 | -48.13796 | 2026-01-06 04:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4c35945-cc9d-3cb7-8070-f52bb409aa2a | -3.87182 | -42.51278 | 2026-01-06 04:01:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 004bb37f-b1e8-3ced-8d47-9c4e540abd98 | -2.98439 | -48.59483 | 2026-01-06 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7d83d08-cfd0-3b83-b869-cc60f62d0045 | -3.00232 | -44.37119 | 2026-01-06 04:01:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd2b0a2e-83a9-3795-8b54-84f7478c41ae | -2.53045 | -47.8292 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff7ac8f0-d867-320d-b92d-134be6a0e007 | -3.70223 | -46.97349 | 2026-01-06 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f5e5674-c002-3017-84f1-90e812ccf4b7 | -2.53321 | -47.83187 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98afee36-9840-3af8-ab19-d55af43190e6 | -7.3657 | -41.1384 | 2026-01-06 04:01:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e379c110-af53-32e4-be28-94855498873e | -3.33214 | -50.22781 | 2026-01-06 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21ff5dc6-15f4-3c54-9d07-29bfa0663bbc | -5.78075 | -40.16542 | 2026-01-06 04:01:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a01c9b23-4ccf-3eab-a4e0-5e525e749824 | -7.7812 | -35.18956 | 2026-01-06 04:01:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 63023beb-7869-3ed8-ac66-f33b306a5636 | -6.33643 | -39.61394 | 2026-01-06 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 279ec3ae-a16c-3d26-ad8e-544be4ab0302 | -4.34625 | -46.32784 | 2026-01-06 04:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53f3d3c3-5584-382f-8852-f70f4a6974e3 | -2.36597 | -47.67882 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b9c3178-6b93-33b1-92bf-ae4df6b34726 | -3.18263 | -51.09282 | 2026-01-06 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e80c7e29-21bd-3293-838a-0d158ceb703f | -3.37025 | -50.49404 | 2026-01-06 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75bdbdd7-decf-389a-b082-36caf67d0798 | -3.18179 | -51.09789 | 2026-01-06 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28e846bb-2759-3fe9-9f1a-ea7c5f599e91 | -9.94888 | -36.03555 | 2026-01-06 04:01:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 712ecba0-3f13-34aa-828e-13cecf659bda | -5.47851 | -36.62425 | 2026-01-06 04:01:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 73357397-5dd9-357f-b9ee-347754cce4ec | -13.10913 | -38.77692 | 2026-01-06 04:04:00 | NOAA-21 | VERA CRUZ | BAHIA | Brasil | 2933208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 18d8a29c-884f-3597-97fb-aea64cc3a0da | -22.49448 | -46.94388 | 2026-01-06 04:06:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c815f95-072c-387f-a18b-690aec47da1a | -22.03711 | -55.51897 | 2026-01-06 04:06:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31fe3f08-6bcf-3b85-9fcb-9137acd5c87b | -21.53825 | -57.53234 | 2026-01-06 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 44c49f0a-a239-3d23-aac8-1c81deea5823 | -22.55271 | -46.82177 | 2026-01-06 04:06:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2a275245-b5f3-38be-a960-2d480e62e2ad | -22.49526 | -46.93954 | 2026-01-06 04:06:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9527f365-fd94-339f-abfb-620cbf19819b | -22.49879 | -46.94029 | 2026-01-06 04:06:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38be7d18-aaba-3331-9e46-4c8cece2cdc0 | -17.65471 | -56.44627 | 2026-01-06 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 03a1384b-c571-373d-b600-485787f4720f | -21.77343 | -47.68364 | 2026-01-06 04:06:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41bf99b4-2b20-3484-a95a-2e7557048d79 | -20.52063 | -58.00999 | 2026-01-06 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4020ce29-bdf9-30a1-92cd-838e011ad7d6 | -20.53615 | -58.00681 | 2026-01-06 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3da6fec6-c56b-38ed-b1fb-d2ad356779bb | -21.54008 | -57.53887 | 2026-01-06 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9689bb3f-01fa-3d3b-81db-5b069df2fa66 | -21.5414 | -57.53363 | 2026-01-06 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f0ee3e2d-1527-3008-8b4c-0c3e75eff5ac | -20.52752 | -58.01191 | 2026-01-06 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 389fd353-75e3-311c-86a9-0e75189e2146 | -22.98706 | -47.1286 | 2026-01-06 04:06:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 57412263-b294-3b82-86ed-8b7433996b07 | -21.53693 | -57.53771 | 2026-01-06 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b2f7d444-61d2-370b-b941-65885141c27e | -17.65324 | -56.4526 | 2026-01-06 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| af221681-731f-3a91-84da-1ae2545cbcc1 | -26.20187 | -53.14996 | 2026-01-06 04:08:00 | NOAA-21 | MARMELEIRO | PARANÁ | Brasil | 4115408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 250e30d0-34ff-31d4-a1b6-1a96c5cdc7b7 | -23.69915 | -55.2713 | 2026-01-06 04:08:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 70a22088-f751-328e-817b-5401a81e08e7 | -26.20042 | -53.15222 | 2026-01-06 04:08:00 | NOAA-21 | MARMELEIRO | PARANÁ | Brasil | 4115408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 26c5dd68-ab45-377f-9d1e-431354b4bd94 | -23.69821 | -55.27531 | 2026-01-06 04:08:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1e50698a-dbbd-3673-9a0f-f4d416f2133d | -31.75525 | -52.98484 | 2026-01-06 04:10:00 | NOAA-21 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| d46085e4-8b79-39cf-bd00-10e7d8defe88 | -32.03263 | -53.54732 | 2026-01-06 04:10:00 | NOAA-21 | HERVAL | RIO GRANDE DO SUL | Brasil | 4307104 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 7f73c688-6686-3199-9c72-30048461e419 | -3.6962 | -43.4432 | 2026-01-06 04:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b2e8eab6-69cf-3468-ac2d-921f1dfe9477 | -2.36609 | -47.67762 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88c6c003-6a75-3df0-881c-f0e7c75f8443 | -2.51953 | -47.82593 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf3a27fe-4c55-389e-8782-482f7d075bd5 | -2.34217 | -45.83251 | 2026-01-06 04:29:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 49de38d3-54a8-3b8e-ae85-ee7163b2999a | -3.69636 | -43.43582 | 2026-01-06 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5bc4bc6a-ff23-346c-b99f-745ef2e9b519 | -2.1101 | -49.00454 | 2026-01-06 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 953a8b1e-ae3d-33ea-a52b-8ab150728734 | -2.07409 | -46.92498 | 2026-01-06 04:29:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19cb3152-9d64-3e08-8cac-be5eaab7cfea | -2.52798 | -45.38407 | 2026-01-06 04:29:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 286debfc-dfbf-3330-992c-36a700a5e724 | -2.52015 | -47.8221 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dac46c59-87c3-3a00-a0dd-a369236652b4 | -3.67588 | -45.23052 | 2026-01-06 04:29:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f6411ffa-17c9-3a1f-9e56-831422ec3193 | -2.9247 | -48.22158 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5563e939-1526-3836-84e1-2410546526e7 | -0.9804 | -47.1968 | 2026-01-06 04:29:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74d5aca3-90c2-37fc-9571-30e6db93d473 | -2.48408 | -46.30284 | 2026-01-06 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f856d43-1720-3507-b19c-0fc8dc6e59c3 | -2.17499 | -47.83311 | 2026-01-06 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4c9a56e-769a-30a5-ae77-c7c04af48a8c | -1.3626 | -49.41395 | 2026-01-06 04:29:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e138ee9e-6d37-38a4-8882-d972472d2d06 | -2.47076 | -48.06017 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5d5ca3c-5643-3bb5-91f0-a8f2c12e1e1d | -2.89185 | -50.23077 | 2026-01-06 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdb9e22f-5970-3802-9572-9cdd015154de | -2.92407 | -48.2255 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9f87bd0-2cf4-371d-a5ab-bfb956297a52 | -0.36347 | -48.44448 | 2026-01-06 04:29:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47f5469e-cfb4-3c01-b9a7-618a21cdd5a0 | -2.52302 | -47.82648 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e393927-65c7-34dd-b20a-09e7a2db6f5d | -3.69576 | -43.43969 | 2026-01-06 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9b5ba1c9-8f2a-3341-aa92-d713f8c76400 | -0.28909 | -50.42619 | 2026-01-06 04:29:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b56b932e-2f9e-350a-8388-b1b54f0e51fb | -3.49481 | -47.17273 | 2026-01-06 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60e66784-7260-37a7-8da6-24e896c8432e | -2.11181 | -49.00276 | 2026-01-06 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5e764af-5049-34f0-963c-d6e99125f4c5 | -1.30499 | -53.91879 | 2026-01-06 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf1e6e9d-4ece-3e6d-b138-4be9517129e2 | -2.5265 | -47.82704 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55695bf2-927e-3c3d-a990-0769d58ccd98 | -2.00494 | -53.21594 | 2026-01-06 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d0840bcc-20e7-3d3d-9d59-086fe0e560ea | -0.36714 | -48.44506 | 2026-01-06 04:29:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fa69c08-f4cb-3e8a-a45e-113497c3f41f | -0.36783 | -48.44078 | 2026-01-06 04:29:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c547882-2a10-3909-a993-dbd1994d7688 | -2.53634 | -47.83256 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7a0d786-a3b5-3f1a-928f-2e7e8fb7c4a8 | -2.09342 | -53.51716 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37c04493-f1f5-31bd-8a6e-bbd7fe8b0114 | -2.13679 | -48.00658 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3da80a3-8f03-3302-a2ad-cb7f3476dc31 | -2.02465 | -47.14827 | 2026-01-06 04:29:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cdf6353-2674-34a1-a2c9-8b97281f7245 | -4.06408 | -42.53008 | 2026-01-06 04:29:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a995765-d8cc-3ba3-906f-8cf6635c51e9 | -2.1611 | -47.89837 | 2026-01-06 04:29:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72c21b2a-bf37-32b2-9239-e1718ce325b9 | -2.93114 | -48.22659 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5ae1611-3a3c-34a6-a7d9-8365675074aa | -1.14519 | -48.09949 | 2026-01-06 04:29:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14599985-d0da-37b9-b94c-2d7efb4aa7c3 | -2.53347 | -47.82816 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
