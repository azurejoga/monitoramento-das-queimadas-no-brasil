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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d5f6713-5921-3c0b-bbf1-da361e2ac8c5 | -14.18924 | -46.46236 | 2024-10-02 05:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fe0bb35-524f-357b-b58d-52635092befb | -14.44035 | -45.71443 | 2024-10-02 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84fea839-509f-3ba3-b013-5ade5b8a55a7 | -15.34029 | -46.73437 | 2024-10-02 05:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd0cb6b9-83b8-3cae-8355-720240a88c05 | -15.33971 | -46.74003 | 2024-10-02 05:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d333e6e5-5e61-3e38-934b-877640c20c2e | -15.33372 | -46.73344 | 2024-10-02 05:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 590f0e04-1521-3047-9c52-e66555952991 | -15.33315 | -46.73905 | 2024-10-02 05:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7207dac-20b4-33c6-8f9b-dcccafe71ef0 | -13.48894 | -48.61524 | 2024-10-02 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae674725-1eb5-3ecc-b08d-85a8b4c0031f | -13.74786 | -48.1664 | 2024-10-02 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b0f8a35-768b-366c-9a07-487167ad7baa | -13.74512 | -48.16315 | 2024-10-02 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd320613-616f-3649-b4d9-6a42e1df9bf2 | -13.7447 | -48.16702 | 2024-10-02 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55f0bfcc-33a0-3383-887c-4633de13a898 | -13.74252 | -48.1607 | 2024-10-02 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d19fa483-57d8-3ee0-bf13-c148b6a5afe0 | -13.74205 | -48.1647 | 2024-10-02 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c8d1a86-adfd-3e97-8506-0d27cb183032 | -13.73978 | -48.15712 | 2024-10-02 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64ea7e94-cda7-36ce-829f-90ac41e6ef2b | -14.82622 | -47.68346 | 2024-10-02 05:12:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae5bcaf5-7486-3c13-9fc5-e1e9df0624d9 | -14.78914 | -48.0753 | 2024-10-02 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e01475c-9ebe-3ce9-a445-f726045e5469 | -14.78361 | -48.07008 | 2024-10-02 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9d4072d-a3b4-3f98-90c2-0debe3fb002b | -15.6221 | -48.10677 | 2024-10-02 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a5ac56b-9e6c-3ff0-8696-3cedc72a4c49 | -15.62157 | -48.11174 | 2024-10-02 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d1a34b7-0ad8-39fa-ac51-7eed749315ba | -15.55416 | -48.04935 | 2024-10-02 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da6e0e0b-201b-34a3-bba9-8dab9bc9beb9 | -15.55355 | -48.04841 | 2024-10-02 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b48caa6a-32f2-3e50-bd87-40d44cd2810a | -15.55315 | -48.05209 | 2024-10-02 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8bfb1e5-b421-3c1c-a8af-249df8253166 | -15.54762 | -48.05283 | 2024-10-02 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 501d75e9-87e5-330a-b8e0-ce47b6ce2fc5 | -15.5472 | -48.05691 | 2024-10-02 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 246c7d69-2faa-3511-bf77-d50ebafa2503 | -15.547 | -48.05188 | 2024-10-02 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6214bccd-0fee-3592-9020-bfb4ce393dba | -15.54657 | -48.05574 | 2024-10-02 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cbf46eb-49f0-36ea-8b7e-3e8bc4eb81a3 | -15.20686 | -47.93901 | 2024-10-02 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04adcdad-2ef7-3baa-8faf-7f4374a8d957 | -15.20633 | -47.94398 | 2024-10-02 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12db1f6a-98e6-364f-a6b2-f25dba9bec3a | -15.20533 | -47.95316 | 2024-10-02 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e900de34-ab93-3bad-a4f0-be2436114941 | -15.2002 | -47.94342 | 2024-10-02 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 233ed9e5-7b99-344d-8658-c8cfc1a11b33 | -15.19404 | -47.94302 | 2024-10-02 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 153de818-34f4-3fa6-8106-ef38dec18399 | -15.19355 | -47.94768 | 2024-10-02 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01478898-3e58-33e4-99ef-e181f2b1cf91 | -17.73294 | -48.44737 | 2024-10-02 05:12:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c890be6-aa08-33b1-b1d6-8d10aa40638e | -17.73276 | -48.45103 | 2024-10-02 05:12:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b532c8d4-953e-3aee-b83a-8e52877d2cd6 | -17.73249 | -48.45203 | 2024-10-02 05:12:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b7b8fdd-c0c1-319f-9914-5bc2b0b9e877 | -17.73226 | -48.45583 | 2024-10-02 05:12:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6668eec-52ac-33c5-bee3-a245da66780e | -17.73202 | -48.4569 | 2024-10-02 05:12:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02c13c11-fa38-3443-baf7-2c19aed66456 | -16.68996 | -47.82799 | 2024-10-02 05:12:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eb602762-527f-3260-88d6-6a6a49658d40 | -16.69042 | -47.8234 | 2024-10-02 05:12:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3bcc64e-a615-33ee-afe3-6d62f1075732 | -18.20799 | -48.658 | 2024-10-02 05:12:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 791216fd-5086-36ee-b28e-4dfab3a5b51d | -18.04614 | -48.60123 | 2024-10-02 05:12:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2d95a793-9f6f-3940-b191-495ab2dd2848 | -13.49532 | -48.61446 | 2024-10-02 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c4506d2-6ec2-315d-9587-566c3e0aab9f | -14.75363 | -48.80303 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e94be5f8-7816-3d4a-b1a5-cff98d0d97d3 | -13.75324 | -48.30531 | 2024-10-02 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6411b9fe-986e-3ad0-85e4-1d09e8795fbe | -13.75279 | -48.30931 | 2024-10-02 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddcb90db-1a77-3899-8578-e1bdcbdcce68 | -13.75235 | -48.31322 | 2024-10-02 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d16fff55-3233-3e57-a8d6-819e64a197d6 | -13.49487 | -48.61843 | 2024-10-02 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85e4835d-a1ae-31c7-864c-3606fce2e29e | -13.49464 | -48.61625 | 2024-10-02 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e22b485-86ab-38d1-bf13-af19c43b16e9 | -13.49416 | -48.62024 | 2024-10-02 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fef3b995-7ec0-3311-b267-be3c6454805c | -13.21939 | -48.61437 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d363ecdb-9124-3f62-b9ea-460c56697550 | -13.21515 | -48.6011 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4a16325-7919-3b97-9a91-fdf48d7432cc | -13.21321 | -48.6176 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a4adb56-3184-3ee3-b7a0-55104c3b6790 | -13.21275 | -48.62156 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fc410b5-681e-3a4d-b725-4812645ecda6 | -13.2123 | -48.62539 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aa8d6a90-c5b7-3465-bc6a-10bfecd926b0 | -13.21185 | -48.62923 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c95244d4-b583-3c0a-a04d-bc93f05732db | -13.2114 | -48.63306 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7a8e2fbb-af29-3e72-a2d7-2cb181076a95 | -13.20945 | -48.60011 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a553dd7-5ee1-3f64-a1d0-324a0d61b496 | -13.20843 | -48.60885 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5173e3b-f2ae-34fe-a88d-6df503fdf7dc | -13.2075 | -48.61682 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0600601-731e-3bfe-983d-3239cad91132 | -13.20706 | -48.62057 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80927171-80ca-3971-8932-04afc826ad0c | -13.20661 | -48.62444 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 617a56d0-0d28-3d1b-9e67-74aa2cf8b912 | -13.20616 | -48.62833 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cfd93ae4-e29d-3ab8-a7e3-a5fd962fe273 | -13.2057 | -48.63222 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fb0ade91-5c51-382e-b3e7-0054befd11bc | -13.20525 | -48.63611 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 33e83759-aaea-3d6b-9901-a6a1d98a9405 | -13.20273 | -48.60796 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30d289f5-d36a-3b81-8ebf-599d379240ed | -13.20222 | -48.61234 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95787d75-6ca4-3086-a4cb-3cb2e53caa72 | -13.20177 | -48.61619 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b05539a-f58e-349e-8c45-ae320c0e004e | -13.20134 | -48.61993 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da852429-0111-3a9f-8d77-67c32f85024a | -13.20089 | -48.6238 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fcd35271-fbf1-3a18-9093-d0e1ff572fec | -13.20043 | -48.62767 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bbc7f293-661a-396a-bb4d-c2b8396dc8b5 | -13.19998 | -48.63154 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9f341e4a-6cea-3832-9986-f81eda2ddccd | -13.19605 | -48.61551 | 2024-10-02 05:12:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2988913-4502-3888-8f1d-2d1243435d1d | -13.25885 | -48.58041 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6788c788-2cac-3c06-8990-c0b469bec794 | -13.25852 | -48.57851 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9627e11-e77e-3442-86c6-be9f821f8cab | -13.25843 | -48.58415 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e77bac0b-5ee2-3912-b697-6f46a3423440 | -13.25807 | -48.58232 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 09eb316b-5bb4-395f-9800-43fdccc93d41 | -13.25762 | -48.58604 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1e868fcf-8e84-3add-8a26-cce21689bce9 | -13.25284 | -48.57738 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16ee027f-bd9d-3b39-b986-03641b05853f | -13.25236 | -48.58138 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7d02c9b-7fd9-3c45-a44b-22828d74b567 | -13.2519 | -48.58522 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb61677c-a920-3aeb-a4a3-430d279ee02c | -13.24669 | -48.58017 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 898724d2-7f9c-3dd8-8f84-f57803f2f6c9 | -13.24619 | -48.58431 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27c94b60-84ed-3296-8804-f0fb808667ec | -13.24571 | -48.58837 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc5e6db5-676b-37c2-ad9c-aa44ee4d3a7b | -13.24145 | -48.57528 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcd1baaa-9236-3c5e-a234-e10546fc5a89 | -13.23956 | -48.59119 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7daafbf6-e5b8-326a-a22e-c6246841e740 | -13.23909 | -48.59518 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8250a4f9-0c11-379b-a054-22a30410bec5 | -13.23616 | -48.57077 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcf43ddd-3a8a-36c4-8368-25a272ce36f0 | -13.23572 | -48.57453 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06c9ad3a-f658-37e0-80cd-dd4d8ec8119a | -13.23045 | -48.56982 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4361680e-e89b-3a48-b680-6d871a07b706 | -13.23 | -48.57361 | 2024-10-02 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec43f822-94b8-3aad-8ef9-7df3fe191dbd | -14.81563 | -49.04481 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c673daec-17e5-3d74-a466-17805bd63fdf | -14.81339 | -49.04209 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cd25b63-c835-3650-8d0d-86bae16d0578 | -14.81292 | -49.04604 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e375dc26-55ca-374e-bc4d-33b78a16f99b | -14.81199 | -49.05401 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71ddde73-69a3-3636-90db-c5d6f00197cb | -14.81153 | -49.05792 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d8cd4bc-63a5-35b7-8b7d-16b5694e2aa0 | -14.80996 | -49.04409 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 863d1e58-ce27-376a-9061-302d2c067503 | -14.80951 | -49.0481 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e740dc99-1a4e-3a08-96bb-914a5c279336 | -14.80883 | -48.78002 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b41e744-9103-3a5d-902c-56c6fa3dbc77 | -14.80864 | -49.05609 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62dc27c1-694d-36b3-99f7-8ed823e75ec6 | -14.80821 | -49.05996 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 886cb2b6-d342-3c9e-b3ed-701d4d86be4f | -14.80678 | -49.0493 | 2024-10-02 05:12:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README137.md)
