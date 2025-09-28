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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 871fe910-a3ec-36a0-9380-26fb71fc7819 | -9.41292 | -54.69751 | 2025-09-28 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e5ba7ec-3404-357b-80f3-b1d152b9b14f | -10.04782 | -65.20316 | 2025-09-28 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 006dffbb-6e08-32ed-a2b7-97cadb903598 | -10.21188 | -64.09496 | 2025-09-28 05:46:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7006a9d1-0520-31aa-84c5-c2655c03da7f | -9.43939 | -67.20154 | 2025-09-28 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6181cc56-e2f1-31b1-9d71-3e715134ecb4 | -10.19993 | -58.22193 | 2025-09-28 05:46:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c24a8c0-b8f7-3666-abb4-7971b6de43e3 | -9.77923 | -64.98542 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6cae6cd-2fc2-3805-b474-66a6e09fb187 | -11.61962 | -52.85448 | 2025-09-28 05:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7b8fb69-fc59-3247-8ab3-bfeb07be868f | -10.29001 | -67.27704 | 2025-09-28 05:46:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 675638b8-52cb-302a-9c6d-cfcae20e0864 | -11.14461 | -54.30942 | 2025-09-28 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 304c48fc-ba86-3f8b-a145-173e5d353f77 | -9.77372 | -62.50652 | 2025-09-28 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f82beae1-8b79-3d39-bd76-ba6a1e9c0a67 | -9.73801 | -62.3597 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77a6fc5a-32c8-391a-be17-b4fe52b14af7 | -10.81789 | -69.09231 | 2025-09-28 05:46:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff406297-8d0a-32d4-8c2d-68c8c7e813e8 | -9.64898 | -62.84809 | 2025-09-28 05:46:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 32.2 |
| d3a6d59a-d9ff-3a52-ae7f-15eb6b1412a6 | -7.91058 | -61.4224 | 2025-09-28 05:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf0d3888-453d-381b-b268-fe7e6c82e66f | -8.94397 | -65.92372 | 2025-09-28 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c04a5bce-2fb1-3530-92b2-163620544ca3 | -10.99571 | -57.06071 | 2025-09-28 05:46:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 570c3070-9997-392d-934c-eb2ebb076145 | -7.86515 | -63.31117 | 2025-09-28 05:46:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52492205-9838-3505-a616-e38bdb103662 | -9.91193 | -65.00607 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8944a42-f98e-353b-8e5f-7c1c3c715bfc | -9.6466 | -62.83914 | 2025-09-28 05:46:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8867bb9e-f1dc-33c3-8ea1-825bb652647e | -10.88346 | -68.80405 | 2025-09-28 05:46:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a10889d1-9b10-3957-ad01-cd0eebfc6b76 | -10.43156 | -67.52203 | 2025-09-28 05:46:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7258ece5-7e2d-3049-ae94-22b62b81f976 | -12.19032 | -63.66632 | 2025-09-28 05:46:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2a3be75-12a6-33ec-a337-21cf9241f954 | -7.86161 | -63.31372 | 2025-09-28 05:46:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1825d4f1-4712-3fee-b52b-e323f84fcc1b | -9.80629 | -61.49346 | 2025-09-28 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0ff5683-63ea-3440-8915-ff4f975ca75e | -9.91138 | -65.00967 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0dfd042-1e6d-3493-92e9-62b931298a44 | -11.14365 | -54.31124 | 2025-09-28 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ff72ab3-5d7d-36d7-a9e2-fdb5a232c3ba | -10.39541 | -64.92182 | 2025-09-28 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c58fe81f-0133-3b45-a0cc-f84f88a08bc5 | -6.59751 | -62.93679 | 2025-09-28 05:46:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81d697b6-a75b-32a1-aa4c-e2d8bccfa159 | -9.64962 | -62.84387 | 2025-09-28 05:46:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 32.2 |
| beb8e453-d479-347a-bc4c-0a99341602d7 | -12.89489 | -62.12666 | 2025-09-28 05:46:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 038d211c-02f6-3139-9cbc-3384c817d1fb | -7.86455 | -63.31504 | 2025-09-28 05:46:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b474fb7-2f74-32c3-b069-42181fd1a02e | -10.30205 | -65.21365 | 2025-09-28 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 320f47f5-c2e0-33f9-aac7-62ab65977efc | -9.73492 | -62.35458 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ee0819c-1e62-35a0-9941-d2386f3aba0c | -8.94342 | -65.92722 | 2025-09-28 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c060bd40-ce66-3a7d-8ddc-6b4ded91abf3 | -9.73786 | -62.35754 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 145eeb7f-6b7e-3ce0-bf21-f156e8ac82be | -9.74174 | -62.36028 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a5c27bf-ac7b-307b-b256-cc07e5f9a6b9 | -9.558 | -63.20819 | 2025-09-28 05:46:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7709b281-3b27-31d6-ae58-14dc2a5bfff9 | -11.52518 | -54.31276 | 2025-09-28 05:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aebc5209-9687-340c-8294-18c95943a8e6 | -9.76141 | -65.03408 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3242f4d6-8ba6-369c-8d1c-50654e501a46 | -9.92596 | -65.00459 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d07e4d1d-548e-3a62-8cd4-577de557dd22 | -10.04706 | -62.45171 | 2025-09-28 05:46:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cea54c8-36db-3e18-91ad-f800acaca446 | -9.76086 | -65.03767 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4b830e8-d20a-365a-9479-02864a64bb4b | -9.65025 | -62.83965 | 2025-09-28 05:46:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72afe49b-b060-3e80-be1c-4d5f951007f1 | -16.96002 | -53.68268 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 30f75e3c-443d-3291-be57-f3b9ffab7b04 | -15.92544 | -57.51458 | 2025-09-28 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d7c2d78-f591-3f8c-8ef6-6e0ede39699a | -15.26927 | -56.80515 | 2025-09-28 05:48:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf062f03-a022-38ef-a3f0-a66f940597b9 | -16.96852 | -53.66904 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 573059f9-55f7-3775-8b59-4aaa19959ccc | -18.17122 | -53.32485 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b59b84f9-06e0-3908-9b05-67105b393f32 | -16.96201 | -53.66161 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2a1a061d-ed47-32f7-a49b-91c3ca1b83ea | -18.19995 | -53.32364 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| aeb0c76e-16cb-3106-834a-eb933ffd9b54 | -18.19948 | -53.3297 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d48a428d-524a-3bdf-ba21-5fe2a0f26c92 | -18.17731 | -53.32853 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| edc482c1-7561-3592-b3ce-ca01aa9de5b1 | -15.94494 | -57.49192 | 2025-09-28 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c99fa7de-9a71-39d5-858e-445e4773e45d | -16.96074 | -53.62326 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 983b002d-74c0-3c2e-ad3d-daca4f5318c3 | -18.2008 | -53.32616 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e59c1e9b-be39-37ef-9540-b8cea273af0d | -16.96135 | -53.61629 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86af0eb7-aa6f-3064-be54-76500bfc0238 | -16.96669 | -53.61185 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64caee04-793f-33ee-abbc-946143d3a17f | -15.2696 | -56.80308 | 2025-09-28 05:48:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 339fd602-e8d3-3905-88b4-8d1045877f04 | -15.92582 | -57.51113 | 2025-09-28 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d63c3389-fd52-3495-a633-b84fe94b9727 | -15.95057 | -57.49243 | 2025-09-28 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7717e761-484f-37d5-894e-c324a98561af | -16.97125 | -53.64016 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59a33f59-e5d1-388e-842b-d2b1955c26b7 | -16.95936 | -53.68967 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8d707215-edb4-339f-a695-2f6d2b007771 | -16.97524 | -53.59787 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd3ad772-6195-3734-859b-a38e910d06b0 | -16.96652 | -53.69014 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 27e5580c-26ca-37d5-a3c9-df5926ed0e0f | -18.17682 | -53.3349 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6fd90247-079d-337f-8103-52b7ece533e5 | -16.95688 | -53.63933 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 514b5201-a702-3f49-a23d-c01efa5806ec | -15.98339 | -59.5011 | 2025-09-28 05:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0043aaf2-c58c-343c-8655-b284366c2049 | -15.94532 | -57.48846 | 2025-09-28 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 283dcf9b-d1b5-3ac7-bf89-2db33e30cfe7 | -15.95096 | -57.4889 | 2025-09-28 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 422302d2-52c4-3526-a3a2-e85d878598ce | -18.18511 | -53.32371 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 300e66d6-fb6c-3189-908d-0d496142e2d4 | -18.20132 | -53.32005 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d0d76c6c-eb07-3b4b-982a-495f9e80e215 | -16.95869 | -53.69677 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3ad162b8-609f-324b-a053-e431a3eefa8e | -16.96472 | -53.63283 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53acc1b9-c66f-35b4-9414-99c5d24c4dd3 | -15.2751 | -56.80562 | 2025-09-28 05:48:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0968da6-3c39-323f-a7b0-16cfd0b1ff63 | -15.27556 | -56.8017 | 2025-09-28 05:48:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cc0d5e3-0860-3159-87ef-d9d291295129 | -16.96921 | -53.66171 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66381baa-3151-33a2-80ed-c8a510fd8e9b | -18.19382 | -53.32085 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 045830d4-aa76-3b6a-a820-968c6624064b | -16.95885 | -53.61829 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f24539f-daff-3c50-83ae-191187e66991 | -16.96288 | -53.68094 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 56965e3c-d9c5-3b26-a707-a93a106eee11 | -16.96103 | -53.70196 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3e20782-36cd-38ac-9be3-ad58ace25cba | -15.99803 | -59.50378 | 2025-09-28 05:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e150c666-5711-3653-8b53-936b66d88194 | -16.96717 | -53.6832 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4ee4187b-59ff-3ea4-a81b-cc3ec7cb8b55 | -18.17858 | -53.32565 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7103b0be-0a9c-3c36-9d59-cb12bbdc8522 | -18.19335 | -53.32651 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e6ce5450-b56a-3ca1-9a67-01e482c89e56 | -16.96012 | -53.63036 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8584c397-39ec-3f2e-a597-43d265be588e | -16.9719 | -53.63321 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0d6b308b-220a-3a13-8fd7-7317f4f585cb | -18.1781 | -53.33139 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9b00b72b-d9e5-383a-8f75-6e8d93adcba2 | -15.4373 | -59.73196 | 2025-09-28 05:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebd6c94c-2b0b-39ef-86d7-b99f18b95726 | -16.96791 | -53.62391 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97cefe61-1fcc-326a-bd88-3ce7bba7ef84 | -16.96271 | -53.65416 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f96076c0-b1a3-3ec9-b896-0e313847b5de | -18.17754 | -53.33813 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 94157e9a-0403-3bc5-90fa-2a81c4b7e603 | -18.20046 | -53.31712 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8186c686-5b8b-3507-9bb9-d1ba3406ec8d | -16.95802 | -53.70382 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 21737891-7063-324f-aba8-e297cbc8a0f7 | -15.26971 | -56.80132 | 2025-09-28 05:48:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b9feaed-7502-3dc2-8b18-3c4f0967f573 | -15.81219 | -56.42054 | 2025-09-28 05:48:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24d3558c-d5e0-3ea3-9237-7b11ad842551 | -16.97635 | -53.61015 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1bfa4c7-1441-30cd-b17e-836f206782cd | -18.19251 | -53.32398 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 99fbc290-3b09-31bf-885a-08790dcf2fb1 | -16.96851 | -53.61701 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f56e4ab7-999b-3be6-b77b-d75c6ea0d15b | -16.96165 | -53.69495 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4d368cf8-fd33-3444-a9a1-3f9cddd3ba88 | -16.97388 | -53.61229 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README92.md)
