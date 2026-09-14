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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a9027da-5e4c-39c2-badb-e2b3c6201341 | -2.90018 | -50.44949 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2547dbc-63e9-3f3e-a1c5-db40ac5d4399 | -2.92165 | -50.43032 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 60e464af-6428-3e5b-9ca1-ef206ecb8dc4 | -2.9292 | -50.44058 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0151b457-f0c5-3b63-aeb6-15df0e62c6b3 | -7.07843 | -43.54255 | 2026-09-14 04:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afef9f56-25c6-39c6-bbb9-ea46b5fc349c | -7.11882 | -41.78283 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| da1fc061-0110-38b4-adfd-efa1a24efcb4 | -5.49767 | -45.6062 | 2026-09-14 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f78215f-ed42-3826-9ff3-0c753d09f666 | -2.91622 | -50.41904 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 3c1c71dd-3061-3470-850a-9d275c74cbe8 | -9.33025 | -44.36475 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3c32c132-79b1-34aa-bbde-0e2ee852341c | -2.9207 | -50.44701 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e6dc0ccd-a0fa-3b7c-bcd4-8361f76e2425 | -7.42556 | -41.92312 | 2026-09-14 04:32:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4b84e745-0815-31d2-b5d8-70799dc49ada | -3.79991 | -44.11466 | 2026-09-14 04:32:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64dbdb60-29eb-309f-bd48-e9a92c69b5b8 | -5.80063 | -52.11278 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d0245af1-a952-3ced-9d09-6ecca76f021f | -2.96154 | -50.39488 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f713726-9863-3c17-bf79-4cb48a1fc4a8 | -7.8668 | -54.72015 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6b9a919-f2f5-3b06-8f83-c82d37418971 | -7.47954 | -42.12414 | 2026-09-14 04:32:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d503644-b3e8-377e-925d-9b780da62cbe | -2.93405 | -50.39487 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef093869-9a4f-3bd4-b5fa-47e2ca5c5f6b | -6.29713 | -55.27536 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 249a188c-13ea-34af-bcea-109863067d0b | -6.79641 | -58.79525 | 2026-09-14 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 057007b5-d039-38b0-9860-a0392a86f49d | -5.1271 | -55.96115 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2b1d32b-d756-3d5a-b9cd-b21ce5002a63 | -4.13447 | -54.01763 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44f4e1ed-766c-3796-b64d-5160089790a1 | -9.44916 | -50.12925 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d908575-78cd-32ee-9dad-877cab38ad1d | -6.3112 | -55.28934 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77592d72-50b1-394b-af30-ede6082ff682 | -6.37491 | -55.26112 | 2026-09-14 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39d7b576-2345-33ea-b0dd-497910907565 | -9.12591 | -51.58913 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c94ca574-6ff9-3f1f-ac9d-5e3bbb647dd5 | -2.92811 | -50.40295 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ad85266-0fa3-3a54-98ea-93afc3efe6c7 | -2.91323 | -50.43676 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 218b9ae6-75db-3812-af14-6e37e7537c88 | -8.53643 | -54.70371 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0487e489-cdad-3a73-b4a3-08440dd5f199 | -7.09196 | -41.81032 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3405b320-fefd-3d54-8f8f-a08db4600c51 | -4.13198 | -54.01037 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88c6c3b3-22da-3b40-bb05-11816ad3e33a | -5.49711 | -45.60975 | 2026-09-14 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7917d0e2-deb7-3497-962b-f70b31d30851 | -7.10834 | -41.79998 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 15ad42b0-9e58-3042-868b-288d5e60e0d9 | -2.93765 | -50.38767 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc669042-0f75-3636-bdda-a96b1d520356 | -2.67276 | -57.55481 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b19d83ad-518d-3a8a-b9ba-dd12603a839f | -9.31661 | -44.35567 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31081cc4-9285-3f95-8796-2facddffd4d1 | -6.37737 | -55.25735 | 2026-09-14 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99cef6ca-efaa-3fb1-b8c8-6c19119ca968 | -7.42195 | -41.9226 | 2026-09-14 04:32:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 05389ec5-bbcd-3471-91c8-b4a606aa4ec4 | -8.3778 | -50.72332 | 2026-09-14 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8f20171-4309-32c6-a487-7557542cb3e8 | -2.91923 | -50.45576 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 086aa950-f70d-3655-b2ca-264b53c65d19 | -2.93556 | -50.41323 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7285b9e4-caec-3935-beaa-08803ac38d31 | -7.11259 | -41.79639 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1e074098-c189-35bc-9709-8a8a6cd35b6d | -5.28428 | -45.26516 | 2026-09-14 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe70600c-6531-38ad-8fed-b381b59500dc | -10.04997 | -45.49088 | 2026-09-14 04:32:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2952603-5070-39f2-b5e2-a89e05597702 | -6.28925 | -55.28576 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cda23e5-8b05-30e8-b0aa-77f4e387689b | -2.92513 | -50.39342 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9fc810f1-f37b-31e9-b010-d6e13b1c91b8 | -5.88798 | -45.57384 | 2026-09-14 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f176d2c-aac1-3141-986b-bebaf47af2cf | -6.38072 | -55.26235 | 2026-09-14 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38ac1259-e11d-3de0-9108-ec69741dde89 | -2.9423 | -50.42781 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1639013b-4232-3530-8638-193878ad763b | -8.122 | -44.0526 | 2026-09-14 04:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b7dc76f-a335-3ede-b261-c619ea667f45 | -12.161 | -48.95983 | 2026-09-14 04:34:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5ba471a-9c5a-3b62-80bc-92e220202ed6 | -14.83082 | -48.14113 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56977aeb-b03f-377d-b47c-984546cfe5b5 | -13.58936 | -47.89032 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2dc7aca2-c6c4-32ff-9874-f8049650c079 | -14.19298 | -47.4273 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d4849cd-1cad-35b6-b92e-8d07c79a8fb6 | -9.70983 | -54.36991 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39a9f46a-c8b9-3ecb-9009-e6cbc48213e4 | -10.6801 | -54.15759 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b5ffcf06-08c2-3aba-9d9b-42c0a10e52b4 | -11.17551 | -46.38718 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcfd0efe-3ef9-3519-b0bb-9c9d0944a75a | -10.66444 | -54.15746 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b8ce9c89-45af-3607-8e4e-f364bc94fea3 | -10.96542 | -48.36191 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba2168a3-f3d8-3579-8e3b-b8416f2e7606 | -12.6897 | -54.67053 | 2026-09-14 04:34:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e31603ad-6d0b-3c11-bf05-d8f014112b30 | -11.51359 | -50.25949 | 2026-09-14 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1956cabb-28c3-31af-9909-0ee2953b0593 | -10.89693 | -47.79454 | 2026-09-14 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3198fe29-354c-3f09-9f1b-0012949e4904 | -10.68516 | -54.15848 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9b8ec7b5-e69e-33b3-8f9d-14e89f7d67cc | -13.61926 | -47.89951 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df6171c1-7877-3811-9b23-1a94e86d1e02 | -11.6304 | -54.5915 | 2026-09-14 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8ad01b6-9067-3c2d-8bd8-bdaae8ad6b17 | -10.10608 | -48.86835 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27af7978-4c7c-3fb0-bb06-7e98f2c33be8 | -11.22097 | -46.42371 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4793be45-df7d-3d93-ba72-99673e43ed74 | -10.10295 | -48.86126 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91bc0d0c-2827-35b1-977c-9d272061d386 | -9.59161 | -55.15172 | 2026-09-14 04:34:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3e12738-cd85-3b49-9f9a-230fc848e407 | -13.59397 | -47.88347 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d942fa8-ba0b-3763-ae2f-73d61035ba48 | -13.3767 | -51.73599 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42be1af2-6b56-396d-911c-4f425bf838ba | -13.29445 | -51.30947 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08f57500-c60c-39c5-bb91-6afd7d7c3257 | -11.78072 | -46.39577 | 2026-09-14 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7d8b6366-8fdf-3df8-a090-ec70325d2724 | -14.19633 | -47.42786 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79f969bf-5d96-3c73-804a-c19c08a4cf57 | -10.55134 | -51.31155 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a96895fa-2c65-30b7-b916-0a1ceb83bf97 | -13.4662 | -48.46344 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e9d30b1-40a8-3cea-9adb-e31c8d9815d8 | -14.83977 | -48.15017 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c60e4e18-4a76-39aa-ac1e-a8ca5b563d07 | -11.2104 | -46.42562 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c5e2faf-0ee7-38b1-b6e6-272e25677fc7 | -10.96612 | -48.3578 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 831bf076-9029-36ca-84b3-5933ff098961 | -10.54506 | -51.29844 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2aa84ba8-3b52-3fa7-bc27-ddf42281cbbf | -12.10486 | -45.78283 | 2026-09-14 04:34:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9151472-cc63-3bf9-91a9-f2ad87b6e987 | -13.28902 | -51.31669 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfe72fa7-8234-345f-8652-4f554438ca29 | -14.1806 | -47.43999 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16f66e65-0a8f-3413-8c36-5c602e463e72 | -12.39455 | -44.4132 | 2026-09-14 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cb06dd3-dc49-35d5-b5ac-c873cfe917dc | -13.58197 | -47.89287 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| acd1434c-c942-335c-bc26-85814e380ea1 | -10.96192 | -48.36122 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24ae50da-9f7b-3417-951b-f364d51dac63 | -11.21096 | -46.4221 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3468508e-f73f-3d8a-9121-f1340fc7fdea | -15.25439 | -42.77398 | 2026-09-14 04:34:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e47c689-1f35-3a6b-b936-2fc57dff879b | -15.55753 | -48.79356 | 2026-09-14 04:34:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 20321c0a-9b16-3c3c-a42e-a936a89d2079 | -10.6897 | -54.15061 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 676a9203-bc1c-3d20-8f76-4729f2bb6b1e | -10.67344 | -54.15361 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 183a7e60-91dc-303e-b73e-f78cbfd3107e | -10.57226 | -51.33958 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e0801f8-71da-36f9-8697-07c871bc4f9d | -10.67774 | -54.1419 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 598d6a6f-8bdd-33bb-a130-883c4d00c945 | -14.18454 | -47.43695 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1d5c13e-ad36-3561-b32b-fa3852e06dd8 | -13.55844 | -49.89933 | 2026-09-14 04:34:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e900d2e2-4624-390a-a79c-e325ae67a692 | -10.656 | -54.14654 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5e90f45-97c6-3775-a9a0-8aa5d9b15e9f | -14.17289 | -47.42392 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68ce127a-90c3-3b70-91e0-ff5f7a785d74 | -15.55 | -48.79628 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 327efb28-c3b7-3835-b4ad-375b2d106abb | -10.10659 | -48.86188 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32a8dddb-fc67-3ff6-9012-9a84dd394629 | -11.29394 | -47.67295 | 2026-09-14 04:34:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f86e7bde-a4be-3bcd-9b1b-7740cad0f054 | -10.69026 | -54.17529 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cb7bc6d-42ef-3c33-b02c-705bfb39cd00 | -10.67175 | -54.16248 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |


[Clique aqui para ver as próximas entradas](README27.md)
