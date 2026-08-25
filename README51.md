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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b16b0a2-0aba-33b2-98ee-f4fe5c3be14f | -6.62771 | -58.48647 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 651c4be2-8551-37e2-a057-ca3cf9b96851 | -6.63215 | -58.5016 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a0742608-be13-3cfc-90d8-02bd275b61ce | -12.84431 | -48.49675 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 003a9a01-26b6-3eb5-a0c6-94f57765e6a2 | -8.22201 | -54.99246 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b0b1d2b-640f-3743-9672-4c5e96f6bb81 | -6.14574 | -57.69976 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 532a6088-4e56-3af6-b815-4111cd376bd5 | -6.70823 | -55.58777 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7e0a7e1-f226-35a7-a059-29e69056c9af | -6.35474 | -54.75411 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c2f10f1-ba0f-335d-9172-f8e3db5ac304 | -7.38763 | -55.1767 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4aeca7e-ec6c-3ccf-ac63-b19b3a6f02ca | -8.56037 | -54.71868 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0cc2497-8d4b-3b83-8300-16bd540a410f | -6.63827 | -58.50617 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14f7e480-74d1-3555-90f3-7e2f9fcd1e8f | -9.16644 | -59.39906 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64a115a9-326c-32d2-b879-1bce30bc1c32 | -9.537 | -49.27388 | 2026-08-25 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8259e74a-7888-3c15-8f4e-f0b6f5dc6a79 | -6.54238 | -55.09037 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0241a5b-0b92-3569-98e0-5625848d0f70 | -6.71165 | -55.58831 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69f481cd-700a-3412-b42b-7fd6ddf98f6c | -7.20802 | -60.61909 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e278db5c-f978-329c-83dc-8a6d52a05843 | -6.89442 | -55.69949 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7761a294-bb4d-301d-b014-6fd9f51565e8 | -6.65152 | -56.43668 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57fd1f54-738e-39d3-8970-14b244a76a7c | -6.14615 | -59.91611 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2298d2f3-6b67-3606-a270-2b491a91fadf | -6.44579 | -54.96503 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01649774-b14a-315c-b01e-3f19d738437c | -7.54462 | -61.36614 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0722f5b4-1cf6-3f72-bc3f-845bd81603cf | -7.34058 | -55.6701 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05576b97-b2ab-3f84-bb74-b9ea31e01271 | -6.81538 | -59.60272 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be2d2b56-c034-3963-a531-cf9cb69e6f91 | -11.99721 | -45.93241 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3ff150b-9b7f-3d0e-8efd-a5c1d67e62b9 | -6.13067 | -57.81786 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b21e2456-00aa-3a7c-a633-94d2b10216d7 | -9.67999 | -55.08992 | 2026-08-25 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fe87095-53d1-3361-9bdb-eda7add7971e | -8.59547 | -54.73924 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42743fc7-4755-3a2a-bd3f-3a470a3d7129 | -7.23668 | -60.63954 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c43ac2fe-08c8-34c9-a281-8da5e8018acc | -7.63779 | -63.38604 | 2026-08-25 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 157324e7-8a9b-366a-9a0a-b859e114268a | -7.49144 | -55.36126 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38aefd44-5c03-33d5-aef2-4667e3021ffb | -10.92011 | -51.07956 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 36f7ddcd-c510-3897-b71a-8069d6496cb1 | -6.35233 | -54.77002 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e10ceda-55a9-3577-8994-d85583a45f2f | -6.79507 | -59.64181 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9615851f-77b6-3d3a-9fa6-891f6509f9b6 | -12.14401 | -50.60021 | 2026-08-25 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c67ed4fd-18d7-386c-956d-2d5362addd27 | -9.97459 | -48.32928 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| acbe0611-5d16-3757-b5c7-26aae4de50d6 | -11.1624 | -54.00176 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 778bbc31-e369-3d42-a14c-441288ff81e0 | -9.21242 | -50.10146 | 2026-08-25 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a84096ce-395c-357b-ac8f-b203501c5b93 | -9.20438 | -59.5717 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 061493e4-5e62-3ac5-b1cf-ede42ea474ea | -6.80001 | -59.58879 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f6478649-f6e6-3175-a4a1-159c6de9ac2e | -10.93561 | -51.07135 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea8f797e-e731-3aeb-9565-0f0cb7345005 | -6.15236 | -57.70078 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29e1d95a-c8a4-3964-85df-b082a5878429 | -6.15059 | -57.93093 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ecc89c6-15a7-3515-bda4-960cdbe00e2d | -7.21159 | -60.61968 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cbdaf52e-614e-3e05-a5ff-4e52d2ab5847 | -8.62282 | -54.70435 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24c2d0b8-345d-332c-962d-af4cbafff5c6 | -6.86425 | -59.40801 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a624e85f-f5fc-3aef-8ae2-6aa9f3391967 | -8.21486 | -54.99159 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a948c06a-6a53-3db6-8b00-ac7f9bd37da4 | -6.80461 | -59.40643 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5744e087-c216-392e-bd78-0bf6eeb6545f | -6.85973 | -59.41137 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 92435127-dc77-386c-9426-9af2cd2020e3 | -12.74111 | -46.48294 | 2026-08-25 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d0ad474-2873-3a91-b84f-a26f67124e7d | -6.82162 | -58.65844 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6130d541-92fc-3c78-902d-2783138cf98b | -10.78259 | -50.93142 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8dfba44a-9512-37fc-a6f6-63bb95b1cf77 | -6.62937 | -58.49757 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8fe817f0-a7b8-360b-915b-dda9d261ca61 | -6.8643 | -59.40454 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f22ec8e8-2d9d-36d6-94fb-eea5f7b06c82 | -10.42917 | -61.2228 | 2026-08-25 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8f195b0-983e-3818-98e5-c4bfb99a9bfa | -6.88924 | -59.02769 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 914cac02-a819-39c9-9c98-9de1b202acad | -10.36803 | -45.0664 | 2026-08-25 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ca9afcbf-ef8b-3a11-91a2-a74af703df3b | -12.86775 | -48.49658 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2147a9a0-9a34-3eb2-a0a7-aa6589a8161d | -6.17928 | -57.70492 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 794dd11f-3999-3411-9aea-3c3d97a48677 | -6.82218 | -58.65491 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ae98b4a-dbfe-3e7f-bc2d-62c73bc73ba3 | -7.01121 | -59.25872 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ff187e0-0ec8-3935-8e3d-7648691b3a7d | -8.80744 | -62.31882 | 2026-08-25 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd4fa7e3-3f42-34dd-a2c5-86c6acca436f | -8.80885 | -62.33377 | 2026-08-25 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f68bd7ba-40a6-3e90-96cb-3ee95b07a5e5 | -9.97168 | -53.944 | 2026-08-25 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 590a99c6-46e4-36a0-9a69-b1632a60f845 | -6.72479 | -59.44333 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7dab12d7-401a-3f8d-8f1c-74e76265c51a | -9.97687 | -48.32734 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dbdaf51f-da55-3879-9d87-3504df64e82f | -6.3612 | -54.75915 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95181ade-a501-324c-8ea8-df15646663fa | -12.70802 | -48.39578 | 2026-08-25 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 348fd8f5-4293-3159-ac48-aa9c0b103cc2 | -6.99709 | -59.25246 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| a6f07803-a965-3580-ac29-6d0a093e055c | -7.01017 | -59.24361 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 454f8a16-2a8c-3284-aa60-bcfff88ccd37 | -6.01093 | -57.67148 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edce3911-1b73-3ecf-81db-b2e4038703a9 | -9.94629 | -48.34314 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2df1528d-a63b-3be4-9e1a-f13f8b1ae113 | -7.00164 | -59.25346 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f56f923d-9510-370f-b5ef-3b913503004c | -7.01694 | -59.24468 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a04fd900-6a05-39fa-bf21-d5aa9b20df0f | -6.18217 | -57.75139 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39e786e1-cf65-38ff-88c0-233c50625d8d | -9.4542 | -60.528 | 2026-08-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86f55961-c505-3014-8b41-07e584f2a747 | -7.76185 | -46.1531 | 2026-08-25 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8046428b-91a5-3f5f-96f0-17cd8c3d987e | -6.80628 | -59.5936 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 97c54478-91fc-32bb-93e3-8ef92de4119f | -9.65696 | -48.3245 | 2026-08-25 05:12:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba93ea39-9622-3f43-87a0-c8a8ba15842c | -10.77851 | -50.92556 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 277f6f0d-a295-3f2c-8843-e2ad602bd5cf | -7.35201 | -55.66419 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49389bb1-741b-3fb2-ba92-c1c7b1f375f8 | -6.63938 | -58.49913 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b4d9852b-0d51-3a82-9b10-ccf66c4255d3 | -10.3758 | -45.05928 | 2026-08-25 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 43cdaffc-f3c8-34ee-8633-26a4d6100eb3 | -8.08072 | -44.64458 | 2026-08-25 05:12:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| da7ebeab-c331-3ab5-960e-e3b5c41fb289 | -5.97278 | -57.63373 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 31e24832-0188-3116-8283-993dd3ef7136 | -8.81208 | -62.31469 | 2026-08-25 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28dcc6be-21d9-3b19-9a26-34e9c320f08e | -6.99088 | -59.24777 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a3c2d2cc-293d-382f-bf9b-bf94a8cf4b9b | -6.5389 | -55.08982 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfae6688-a6c4-3598-b618-673261266eaf | -6.12386 | -57.75301 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb2d1bdb-ddf4-3b05-afa8-4c18b222d2ef | -12.85579 | -48.49882 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f7dee2d-8f6f-3e77-a154-c926f35a9b0b | -6.8194 | -58.65087 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e2644e8-7658-38b1-b78c-d77cfcc91624 | -8.62634 | -54.73087 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78c8a0d1-8a80-33d9-8569-00f2f273dafe | -6.86365 | -59.4117 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2da10773-5565-3f6f-9ef6-69ccd7085967 | -6.8206 | -59.59198 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8964a724-69e9-32af-8cd8-d68b8a8bf920 | -9.44905 | -51.58633 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 932c323b-b4d8-3607-8380-deb783545d1b | -9.16308 | -59.39852 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cc6ec23-366b-3417-947e-f4ea14716018 | -6.74495 | -59.66848 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0459cba3-3eff-369c-ae5b-b6139e18adec | -6.43872 | -54.98796 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82bd3546-292b-3949-a71e-fa4c3b56f031 | -6.87068 | -59.03582 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12a6d579-1eba-3789-a6d0-061d16414e5c | -8.15998 | -46.70351 | 2026-08-25 05:12:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc642261-67bf-3da5-90ff-215de9c4d678 | -6.35758 | -54.783 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79aa8511-11cf-34b4-917d-c78737f57e85 | -11.98236 | -45.91326 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |


[Clique aqui para ver as próximas entradas](README52.md)
