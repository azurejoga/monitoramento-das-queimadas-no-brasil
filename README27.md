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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b42b85ee-abb1-3de6-b11a-f9d68a747445 | -3.33409 | -56.95638 | 2024-11-13 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d437cc0e-5684-32a5-8aca-a37fe84e4b51 | -2.92286 | -48.06952 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78b0ef90-b9a3-32db-a999-b9193b08ed25 | -0.23225 | -51.52734 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9bfe1a6-21d2-3d73-82c1-7aaab8938177 | -2.46478 | -50.38921 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c5d01e2-d8c5-3725-8da7-0818ff20519e | -1.55866 | -51.85102 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b13bbbea-ec65-31b0-937f-0bfd498a8228 | -1.82332 | -45.91949 | 2024-11-13 04:57:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 123f2c70-66cb-376d-909e-c50df1638d9b | 1.30856 | -50.87334 | 2024-11-13 04:57:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9615ce73-8aca-3598-b2ea-0a4b80517a9e | -2.98144 | -45.16306 | 2024-11-13 04:57:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b2ff2cd1-ff0f-38fb-a347-a6b88543be00 | -2.97721 | -45.15623 | 2024-11-13 04:57:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af6166c2-f7a3-334f-af7e-7dcaa28f49e3 | -2.44441 | -51.95255 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88750837-94a4-33dd-8274-f85f3417e004 | -4.5178 | -48.93198 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e890afd7-9ca9-3365-88d3-e08f991231dd | -4.0452 | -56.26315 | 2024-11-13 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c982eb5c-10c6-3d35-b926-84b7cc6ce628 | -2.60325 | -54.03749 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b35ea313-b9d4-370a-925a-0ec24f1ca8f9 | -0.65864 | -51.69504 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6236a702-df2c-3788-96ad-edb833c970d9 | -3.21821 | -50.38736 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d7b336f-cd82-3188-9587-333e7669c78f | 0.11999 | -51.33719 | 2024-11-13 04:57:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee88a745-4c1a-3565-9b5e-3506b05ca4d4 | -2.98464 | -51.34179 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ae2d269-d836-3feb-8bbb-8d20eb93a7e7 | -3.97962 | -56.03492 | 2024-11-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdcd99bc-0fcc-31f8-8a65-b5527a8e542d | -2.10067 | -50.37496 | 2024-11-13 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d46ba4d6-fbef-3a68-9fa3-eb759a845799 | -0.88529 | -51.7262 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8774795b-a1d8-37bc-8820-4b3949cc815f | -2.18375 | -46.99324 | 2024-11-13 04:57:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f333c75-af19-3a27-991e-1089f86968c3 | -1.28559 | -52.47174 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b98d93ca-2a54-3f0a-9d02-485b235d6102 | -2.55797 | -53.99869 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0f5a4e6-bed7-3fb3-b31b-e54c1532e4b3 | -1.55811 | -51.8546 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1087b7f8-f67d-36de-8745-de9ac8dd7001 | -2.8042 | -50.32599 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2202211-b74c-3f66-a993-7a36aad0c52a | -2.14513 | -46.40431 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 94a966f3-57c2-3215-82b5-a744131a2c0e | -3.09962 | -54.29881 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| af11e5f7-7902-39b5-a157-9f69a793cbc8 | -3.61523 | -51.36798 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| debe8d8c-d321-3570-965d-96b9c352e30e | -3.34773 | -54.19308 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b59ec4ef-272a-3820-9522-8628c7ac23a0 | -3.01196 | -51.43443 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5308d524-16ca-30b7-bae3-6545ac053064 | -1.38668 | -52.39103 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67933c78-ebc5-3ef7-a4d3-140ce2f1700b | -3.39644 | -53.68305 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67ff87a9-8922-363a-aa17-f3f4d8107b4e | -1.3491 | -51.43376 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d430f1f2-875b-3a96-a95a-0a0ed4fc0e78 | -3.45622 | -47.66484 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85b7e9d8-845b-33dc-bb21-21f89987ad63 | -3.20654 | -50.63213 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c9295a1-df5d-3c9e-8ef8-6a738ea4c23a | -1.55931 | -51.21082 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08e55ce8-e956-3d2c-a2cf-ca9539c6aabe | 1.05429 | -60.59793 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| bfbea54d-ee74-3587-80c3-d1745e492f41 | -1.40642 | -51.11196 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2493afb5-4826-34b0-a7c4-28c2fb7737a5 | -3.98022 | -56.03115 | 2024-11-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cc86143-72a9-31ab-859d-3c624238d3f0 | 0.82225 | -51.87419 | 2024-11-13 04:57:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b984c07f-bd5f-375b-b831-bef37bf9591a | -1.40052 | -52.3896 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd85cdcf-381a-38f6-be61-abf1f5076a98 | -3.16194 | -50.5875 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2f29c3de-2490-37ea-94b2-6ea7ef0f89c3 | -1.13665 | -51.94276 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35f10bf3-3049-34e9-bc94-a6d6033d0fd5 | -4.51315 | -47.58746 | 2024-11-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bdd18cb-3839-3380-a154-0acaedb3fa53 | -2.73138 | -49.38392 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90a40dc4-ee03-3fcc-a210-4bbde0e5f271 | -2.19604 | -48.38577 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65529426-9f18-3333-9b52-a3ccf4b3e725 | -2.31882 | -50.67904 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b70a485-5ca9-3287-a91c-e65aa2b6b50b | -2.39437 | -53.67366 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9be94bd9-a3d6-3057-b924-95f580af0f07 | -2.89109 | -54.17453 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 577dd89e-5759-3189-9eb4-3caa17a2abb6 | -4.68704 | -48.74536 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8432a18a-5331-3344-922c-e51c5b3f8adc | -1.84499 | -52.06625 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19117209-197b-328b-83d0-897eee8cdd12 | -0.49972 | -58.08868 | 2024-11-13 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e01d6048-6918-3231-85fb-46f053a6788f | -2.9855 | -51.24412 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab52213f-68df-38ec-a4b5-7dc5ce60b653 | -3.48973 | -59.61158 | 2024-11-13 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3920eb5-7b0f-329e-9717-0c5b77ad1cb7 | -3.9498 | -48.18068 | 2024-11-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 17c842cb-9dfb-3a40-bf8f-066b047abee9 | -1.41449 | -51.1055 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e5a0257-076f-3fdc-a505-c2395d7b1f69 | -1.65045 | -52.53179 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c7d2270f-c27f-38b7-a8e0-35cebb5ebdcf | -3.11717 | -53.70946 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecaca0e0-7907-3a77-9f14-eaa270527d7a | -3.17516 | -53.64108 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7cc33f96-e4b7-3bce-8a65-b755b815811b | -2.24305 | -53.66429 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aadb8893-3796-3ef7-b559-19c8ae0b0486 | -2.59274 | -54.01463 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc15947f-d5ae-3deb-83c5-6b9932562bcb | -2.97042 | -53.27544 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a24dae1-0ef3-3d66-a60d-d339e4507aaa | -3.1049 | -53.32792 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc828436-0cd1-3cf9-a081-19ee412aa2cc | -2.57714 | -47.28464 | 2024-11-13 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f74e5d32-2d8c-3edf-8fed-231d36b94855 | -4.25302 | -50.25639 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c485541a-c11c-3c21-890b-99fd775f9d16 | -2.43644 | -50.40599 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c107ae35-4039-313e-a803-f24b1a55d137 | -5.15137 | -48.1825 | 2024-11-13 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b357285-9176-31ba-9a86-888a4601aa3d | -1.78499 | -55.5493 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e4ecbd8-8b05-359f-962f-9cbf58048b95 | -2.78986 | -54.0382 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44b86267-f2d7-369f-aeea-7f42d8acbcfa | -2.98692 | -51.34999 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 15aaa8d4-5982-3877-be9c-a0bbaf370e7f | -2.96758 | -49.28372 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bdea6a3d-bdfa-3643-9d8b-0ac0f8348562 | -1.39114 | -52.0759 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3591e73d-1903-32c3-8d90-2fdf50d2c373 | -2.21366 | -53.74414 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1252d051-b3ee-393b-97ee-bc9d180f701f | -2.77557 | -57.52749 | 2024-11-13 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a473522-3a2c-38a5-94db-2e6d811694e8 | -2.62713 | -54.27476 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da6c1c0c-7f3d-32ee-848b-f8f30f46a1dd | -1.39702 | -51.60123 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad1b1328-04cc-3140-ba7e-ffe1a6591522 | -3.25751 | -50.39766 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 95dbff02-f2eb-319a-be3b-dbcf5cb897b8 | -2.75538 | -49.3296 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95c39ead-e01d-3b44-a780-afda0c12b1e5 | -3.26953 | -48.75209 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aad784e1-354b-379a-9f56-c4a02a3c2835 | -3.01874 | -53.24765 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 087bdb08-47da-3400-81e0-e5fb90552de4 | -2.72774 | -45.29241 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6603266b-b113-337f-836e-cc0fa4d70d0b | -1.38908 | -51.56282 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9d09def-4c57-359d-838b-6cb712d02db9 | -3.68048 | -51.30175 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60f4fa52-5f73-39ac-8da8-a4ee6e068c9f | -3.03026 | -50.97645 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b70f9996-7e60-3498-8c98-c9b7bf22a173 | -4.17527 | -55.09463 | 2024-11-13 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89f74292-cfc1-373f-af21-5e38b948bfcd | -1.68301 | -48.46475 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54099b60-fb7b-3818-baa8-eddc1dd75334 | -4.80036 | -48.76825 | 2024-11-13 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f4a451d-0957-35f2-b3f9-a4b66a0343b7 | -2.81668 | -53.99649 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c01de669-73c0-33ef-aa1f-0f6662cd0565 | -3.10507 | -53.98184 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f044538-53a3-3f7a-8128-d300d97dcf78 | -2.93879 | -48.31925 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7999aaa-7c6f-397a-a4f0-d8dc66fc9066 | -1.64327 | -52.53424 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b83523d3-8e83-30fa-b94d-2335262db433 | -3.01484 | -51.43875 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c4e00f0d-b4bb-3205-9766-2234f8f26610 | -5.15565 | -48.18312 | 2024-11-13 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a23e35e6-a838-377b-9c3a-46cb4d69f898 | -2.9524 | -54.28324 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46cab16d-c896-33df-b257-8264407204fe | 1.14017 | -60.60197 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abbe6950-7706-3c33-bafd-9d4640068152 | -3.34167 | -54.64331 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87382de1-ef23-3b4b-87b5-d24d0dbe9362 | -4.22927 | -46.87183 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f58e192f-c409-3494-92fe-b04d8a794667 | -2.71485 | -57.34466 | 2024-11-13 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b450a11b-cd12-35b8-9466-6d43cb08dd0b | -2.6623 | -51.68004 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88bcc35f-3c65-39a8-8f84-24702f6c1b62 | -4.12766 | -46.85657 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README28.md)
