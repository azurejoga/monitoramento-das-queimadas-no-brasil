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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98a7ab6d-225f-3d1e-8175-fa15de9ece10 | -2.42989 | -51.95771 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bd6c858d-3352-39f5-8a5d-da25cc09f78e | -3.2602 | -53.70678 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1579081-2315-38a9-8363-474fbdcc918a | -2.84645 | -49.43582 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26767342-b868-323c-8d98-3843509d7c7b | -3.92255 | -50.25126 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d74d9f43-f9b3-3f2f-9410-b2f247685e18 | -2.4225 | -51.95654 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 300d8acf-2d7d-394f-b156-569233ecdd62 | -2.57105 | -48.26126 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa0090cb-d37c-325b-b474-9b794fcdb0c5 | -2.40262 | -49.83813 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 244d8cb4-b6db-341a-89b1-bb95fef8914a | -4.11642 | -48.50242 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36278f28-f8ec-3da2-bd4a-9d7dffe68647 | -3.18789 | -54.31932 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5af1769-19a6-36e2-9fb2-75898fed7a76 | -2.42249 | -50.48259 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64062972-88ca-3c42-95d6-a7ff92f0f26e | -2.87844 | -49.37607 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 835f64f0-4f5d-3933-aeb7-f3308594e01c | -2.95741 | -48.02007 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87702024-68c3-3dc4-bb1e-94a5b9a6876a | -2.14301 | -50.81084 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3905862f-c139-359b-b673-2507e5d8a8d8 | -5.37066 | -48.62074 | 2024-11-10 04:38:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a8401d2-ed7b-37e4-97cf-8a467849df64 | -2.609 | -48.19296 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 405a3508-7e7e-3cf6-9dcb-912450c3b6a6 | -8.42328 | -44.13437 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f48d1ad2-40ad-3330-8134-2d790d6bfcfa | -4.27784 | -50.67661 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec1450d8-416e-36c9-856b-4d9c99661c17 | -5.56987 | -43.97566 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d74db172-1963-3e95-9e01-daec224827ef | -3.95201 | -48.14671 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b6c0b31-e778-3c02-ba87-f7e32e46d649 | -8.39211 | -44.1151 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f916e7f-2f7d-3d77-b3df-b25641143c51 | -2.24439 | -53.66846 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 13f0275c-effb-3afc-b567-b4fd6a7b482e | -4.5898 | -48.48426 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 084f8ab8-bff7-3ba1-b692-10f5ced1d0b3 | -3.14137 | -52.96918 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 349a53a6-225f-377a-b039-0e5a86c31fe5 | -4.53406 | -47.88581 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15507d26-0795-3907-b027-89d8c6ff4b06 | -4.37528 | -48.57882 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59719414-18d0-3009-b064-515b742db3e0 | -3.07241 | -50.57079 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb31d5e9-8467-3f0b-955b-9ffe17755abe | -5.25502 | -48.07553 | 2024-11-10 04:38:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1af0a2c9-e644-3498-8d6c-badb51acbb75 | -2.21173 | -50.33601 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf69db70-f35e-3a81-9d08-db3c43a3676b | -6.73437 | -46.38022 | 2024-11-10 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cc1577f-06d1-3a6d-958e-cefa1db9c599 | -2.24433 | -53.77451 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 521b3bfb-0b71-3fe7-9a69-90cdba486090 | -3.27255 | -50.34369 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 367e1687-7c53-3f87-88f8-c6c9be5d1276 | -4.11355 | -46.88292 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76c7ba74-3406-3371-86c4-c326f7aab1d2 | -2.46483 | -50.39362 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5342e705-3485-33a1-a6f8-67e6eb517aea | -3.25826 | -51.01078 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4cbdece-4eef-332a-849a-d54b7de789c3 | -3.35442 | -53.40684 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3988d715-1e3c-39b0-a325-4d745ac4be95 | -2.59674 | -51.22009 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b0eea27-f78f-30e1-b82a-5340394318ea | -2.4864 | -50.27936 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea2f3af3-985d-3763-b956-9a4a07ec18c7 | -5.16259 | -49.61731 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21a46786-6405-3c71-8933-a67ff92f7dca | -3.25998 | -48.74289 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b3e101e-fb31-3b09-a5ce-c57e3870a356 | -2.9944 | -49.52343 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1731cfd-6c47-354c-ad5a-6d76b1516535 | -3.39788 | -53.80266 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9fd051d-d5d0-35f3-bbc5-fa7c1bdf7645 | -5.42133 | -47.70036 | 2024-11-10 04:38:00 | NPP-375D | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21dac3f5-3001-3b10-a5bd-6a5c535a1f77 | -3.29073 | -51.57057 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2f427e3-e773-3512-bd6b-c7f021a8e388 | -2.94473 | -51.39558 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f25b4007-f471-36e1-821b-26f37457e37f | -2.81217 | -48.468 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd89e2d-b63b-316e-b786-4108f51f2a8e | -3.07586 | -50.57132 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02a9dc1b-e69b-31a6-aa1c-5d05160da2e1 | -2.17298 | -50.46778 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19dc643e-33f5-33f2-b252-c9c58df40e46 | -3.16071 | -51.12662 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a356259-4979-3e96-986a-4129f60a108c | -3.18957 | -48.65447 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6a4fafd-72ba-3aa6-bb0e-07f27a597679 | -4.10494 | -49.13746 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53409ff5-af98-3fc3-8167-db0ca4c4b729 | -8.41374 | -44.1144 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e86d39f8-787f-3940-9a08-87fbda9ea873 | -3.07991 | -49.55797 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ed3c755-3785-3f14-8e57-675c25fca455 | -4.48936 | -44.48284 | 2024-11-10 04:38:00 | NPP-375D | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4f5211e-771f-3e43-b42e-bcc2a741d46d | -2.58448 | -48.13258 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a56706a-a994-3939-9641-e3628bf281c4 | -2.27784 | -50.66552 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fa62c4d-df94-3ad0-94a4-a406a3eff863 | -6.25281 | -43.56586 | 2024-11-10 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0239ba0f-aa9f-3ac4-8fcc-b3bbf9c31e1b | -4.74916 | -48.91342 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 367e72ef-2a2c-3c3a-947c-bff44cbd4c64 | -2.58339 | -48.13948 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33491f71-ea7a-3e37-b4f2-5330e083d1d0 | -2.58394 | -48.13603 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75f1c6c0-8b67-3227-b957-5dc60e99680b | -4.2756 | -50.66866 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ba1191b-fba8-3041-93a1-356109e095f2 | -2.24218 | -50.03566 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec041c4e-0d84-3c32-b56f-d34d83e4b56b | -2.81262 | -51.80204 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de388c2f-6e84-323e-af22-998c6a8f69a4 | -2.88681 | -48.29595 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e821a9de-1ee8-34f1-b9bf-f4f67c4e1238 | -3.59746 | -47.34932 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 66f4ef98-5e24-38e7-8b4e-d64976c82e17 | -3.13965 | -49.11705 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed93c5e3-29f9-3c0b-9f20-32e565d31efc | -2.92026 | -49.81617 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6b84d8f-84ed-34df-99f6-4587321df422 | -2.91527 | -49.51112 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92059908-f8f1-39c7-b997-133fd6644e27 | -4.16872 | -48.60258 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 480efe2d-a693-3676-b542-e86ad5371cf3 | -2.91293 | -49.35282 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5157224b-f459-3688-9377-44c68c530432 | -2.79784 | -48.2823 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ea22da8-8e21-38c2-a056-b9287dfe948d | -4.10162 | -49.13694 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07ff9f39-2665-38d8-8b93-60cd70c0d575 | -2.88627 | -48.2994 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8925c59f-d033-349f-8dd1-9c409795e3d4 | -5.21897 | -48.28588 | 2024-11-10 04:38:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42efa4ff-c13f-3fb4-83bb-8376029f67b6 | -3.02889 | -48.03886 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4121000c-949b-3e09-8def-6e6a68d4240d | -4.61099 | -45.96942 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ccf846b-ba4b-3a6d-8b7c-024e8ba2db34 | -5.56578 | -43.97507 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 870a981c-c3de-3902-82dd-30a47b083e75 | -2.4652 | -53.69072 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 126b9ee9-4a0c-3556-8678-acb6150a94fe | -3.80335 | -44.68187 | 2024-11-10 04:38:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5bb1fe3-4efa-35f8-b1c4-129067f774ed | -6.40893 | -42.49162 | 2024-11-10 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2f336d55-7a8e-3f09-ab01-31414dec4be8 | -5.36745 | -48.2485 | 2024-11-10 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e797c452-2879-346a-8a57-0141ffaed63b | -2.88959 | -48.29992 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8da08bef-651c-301c-a860-d08fa06d1904 | -8.41238 | -48.30293 | 2024-11-10 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 382b26d8-02e8-3f27-83ad-51a6de2a0cfc | -3.92215 | -45.01285 | 2024-11-10 04:38:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bb86e5a-4919-3843-92de-5aa95de286b8 | -3.35606 | -49.03791 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfa6e484-c716-360f-8533-20f492be61c0 | -2.67892 | -48.50016 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eebeb9f1-863e-306c-add4-ec2b7d122bc4 | -4.08014 | -48.32671 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc0c895c-7dbb-32f0-b879-f590cbf264c9 | -4.11364 | -48.49845 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 18aa059c-c8d5-3dcb-aeac-017b2f994c10 | -2.89729 | -49.25746 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52ef941a-eafb-3f4b-bf7d-d16422f343c6 | -2.99216 | -49.51588 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb0be333-92f6-39ce-8db3-b52f418a9a14 | -4.92827 | -48.24498 | 2024-11-10 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 069771d8-9134-3257-9023-850ea4aae650 | -3.96248 | -48.12338 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c01b5525-6b6e-33d1-95eb-03606d9f6b14 | -8.40136 | -44.14042 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a6262de-b343-384d-99a7-cf91c6768db7 | -3.24571 | -46.48938 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d18be6a6-cbe0-399e-a543-337ba1509806 | -5.90694 | -50.21196 | 2024-11-10 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14074776-1fa9-3251-8662-d82b562b84cd | -4.62628 | -48.90067 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d08cabb-fc2a-34d7-b600-d3c4b5c65cb5 | -2.94857 | -45.46327 | 2024-11-10 04:38:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f264d8d8-7660-37f5-b325-9ad95b92792c | -3.11914 | -50.14513 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fbd1760-94f6-3b27-a2f8-79ec5a3e4e62 | -2.79971 | -46.64442 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f9eda18-ff08-3c2c-8aa1-40a81ebad57d | -3.95925 | -48.98731 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d8b64d8-cdfe-3549-968f-cf40a4c59df2 | -4.17906 | -46.57703 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README87.md)
