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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e9df52e-165c-3a85-9663-56aaa06c6b24 | -4.5046 | -54.9446 | 2026-09-27 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| ed045714-afc6-30b3-99e8-d939df1229ae | -5.162 | -56.0129 | 2026-09-27 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| a811211f-c7e3-37e4-a077-35e789ed100c | -11.264 | -54.4434 | 2026-09-27 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ea92925e-8e59-3304-84c4-39a4b5230850 | -2.9223 | -45.506 | 2026-09-27 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fc112a93-231f-3447-9618-a0d962b78f34 | -12.0369 | -50.6019 | 2026-09-27 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| e241f8da-6094-3882-a495-78b1c4ed1dfe | 2.6541 | -60.1836 | 2026-09-27 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 3efb6095-a9e0-3b1b-925f-05ce7d6e2707 | -6.7339 | -52.9837 | 2026-09-27 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 54311c1e-d196-3483-b742-8d3dcd88f798 | -11.2829 | -54.4417 | 2026-09-27 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| a78a526a-848d-361f-978f-e176d6f2e895 | -4.2476 | -51.0435 | 2026-09-27 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a2d22b19-677a-39e4-9247-8138b9666c6d | -5.7551 | -45.2879 | 2026-09-27 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 694e4b6f-19b5-382a-9f1d-79d2cd2f74d5 | -8.0374 | -54.8724 | 2026-09-27 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 83eec97f-f64b-3aac-aca5-15d93c26b9f1 | -8.0371 | -54.9127 | 2026-09-27 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 8b7d5a24-184f-306d-bd7b-1ce075fb0b33 | 2.6359 | -60.1648 | 2026-09-27 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 16c2b7b6-5f79-3aa1-8634-d53454a1d8b5 | -12.288 | -50.3789 | 2026-09-27 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 829ed94c-3b25-3fca-a5d4-8144d74ca9d5 | -1.0551 | -53.5573 | 2026-09-27 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 433cb37a-c627-3379-a5ca-440bb7ab0d38 | -12.2877 | -50.4004 | 2026-09-27 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| bf87cf7d-9178-3f38-a46d-227d36f9d683 | -10.824 | -60.7246 | 2026-09-27 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| bed93c64-2e07-3820-80ec-547d684d6a6b | -3.9672 | -48.1067 | 2026-09-27 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b15ddb36-64ac-371a-8ef8-afd17a8b9388 | 2.6358 | -60.1839 | 2026-09-27 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 4abd63ac-e1ab-33b7-bf15-348f35918d95 | -4.266 | -51.0427 | 2026-09-27 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ade4c027-60a0-3512-a596-7d6fba6d7729 | -10.8052 | -60.7257 | 2026-09-27 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| dc4571ca-5186-3340-b065-b7040e22561d | -4.5413 | -54.9633 | 2026-09-27 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a09c7e9a-6c86-30fa-880c-1a403e6a30aa | -10.9278 | -43.7464 | 2026-09-27 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1eacc54d-7d31-34d6-83bb-8fabf0e19d27 | -3.1953 | -51.039 | 2026-09-27 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 085472c6-623b-3749-9617-099fff9eb7e6 | -5.1621 | -55.9931 | 2026-09-27 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 47ff639b-3ae8-32ca-a585-428ca88436f3 | -6.0733 | -57.822 | 2026-09-27 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| fe46afe3-42c4-3acb-bf5e-33cf4c679086 | 2.6541 | -60.1646 | 2026-09-27 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 14b49360-735a-3fb8-ad01-886e47c231fa | -6.0919 | -57.8018 | 2026-09-27 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e2565a44-5a67-395f-9c39-442fac474c03 | -8.0373 | -54.8926 | 2026-09-27 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| c52168bb-093e-3ee5-9990-c7af3d6ae65c | -8.0373 | -54.8926 | 2026-09-27 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 6ccc4556-4b72-3e71-a9f7-3a20e70c4bec | -5.162 | -56.0129 | 2026-09-27 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d67fbe3a-b489-30a3-a65e-b5adf24544da | -11.8856 | -50.534 | 2026-09-27 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a783a266-cf6f-3ae0-9a86-9e6267628861 | -12.6643 | -47.3245 | 2026-09-27 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c01978df-c728-3de6-825f-78f276c0e64e | -12.6836 | -47.3217 | 2026-09-27 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| bf320705-a1b3-345a-9552-37bf71c66e48 | -12.288 | -50.3789 | 2026-09-27 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 14d8a014-0f1e-3e26-a776-af35c6465377 | -10.8052 | -60.7257 | 2026-09-27 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 0dd188a8-4e99-33a1-ac81-7d58e0445152 | 2.6541 | -60.1646 | 2026-09-27 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 55f8bdfc-1a1d-3512-b152-d6dc0dd63cef | -11.9421 | -50.5702 | 2026-09-27 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1117891e-6ce5-3970-91ec-e615be982093 | 2.6541 | -60.1836 | 2026-09-27 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 4336aaae-4869-32ff-9475-6091105c3705 | -3.1953 | -51.039 | 2026-09-27 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 3f9457c6-874e-3934-bbdb-f68c3a5ffb7a | -11.2829 | -54.4417 | 2026-09-27 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 9ebf0969-6973-34bb-a9d4-4e0ebae99788 | -12.2639 | -50.7034 | 2026-09-27 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 6c2e628d-1e3a-3964-8e90-ca5f3330a765 | -10.824 | -60.7246 | 2026-09-27 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 8298813a-ac65-3d28-a17a-cbb3b9493cd1 | -11.9234 | -50.551 | 2026-09-27 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 6532db1a-b9b1-3ed7-996e-36f14d4f4337 | -11.9047 | -50.5317 | 2026-09-27 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 765ecbb9-fd9d-32ef-9e83-55b2ec311a57 | -11.9043 | -50.5532 | 2026-09-27 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 333d5eb9-f445-3cb0-90fa-a016228e6be7 | -6.0733 | -57.822 | 2026-09-27 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 0cd339f3-2580-34e0-917d-8b4c11066957 | 2.6358 | -60.1839 | 2026-09-27 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 95.6 |
| d5ca851a-2d7c-3aea-b59d-4a74f9642b10 | -10.9469 | -43.7437 | 2026-09-27 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 0bd45d82-01d4-3639-9948-d5b56e5ad4d1 | -2.9223 | -45.506 | 2026-09-27 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9b76312f-7a7e-3173-9612-5bc08f200b44 | -6.7339 | -52.9837 | 2026-09-27 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 48cdc5c9-56fa-350f-87ba-836164dd4c14 | -11.9237 | -50.5295 | 2026-09-27 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 04428c80-ef54-3cec-97d9-9ec2626c1939 | -5.7551 | -45.2879 | 2026-09-27 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| aafabcfd-ca21-3c60-a08c-3d0a29534498 | 2.6359 | -60.1648 | 2026-09-27 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 091d2488-44a3-3965-bb04-0684c4c9e777 | -12.2877 | -50.4004 | 2026-09-27 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 3bccd2e3-4fd4-32e1-9be1-ffeeb7aa1ed3 | -3.9671 | -48.1283 | 2026-09-27 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| cfe99a3d-d6ad-3c59-9aae-5814f1f83615 | -8.36 | -44.2 | 2026-09-27 00:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aae903d2-9fe2-3072-af1e-2e0dd0e2f8ff | -8.36 | -44.11 | 2026-09-27 00:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d9d917d0-fbf2-3034-8d6b-3b10f3d59366 | -8.33 | -44.15 | 2026-09-27 00:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c87e5d8a-e5e0-3624-83a5-d2b8df08559b | -8.36 | -44.16 | 2026-09-27 00:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa795854-3903-3ae2-9eeb-6a7317edaacc | -12.288 | -50.3789 | 2026-09-27 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| a1d9c1f3-0c3c-389d-a1b0-9dd68d008884 | -1.0551 | -53.5573 | 2026-09-27 00:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 4b01112b-fbed-3c74-9e7a-02766027255b | -10.824 | -60.7246 | 2026-09-27 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| a8490c5d-a560-3b47-8e64-6ccd4f58f6b8 | -3.9672 | -48.1067 | 2026-09-27 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 084f6792-0e64-3edc-987c-b23914f5f82d | -6.7339 | -52.9837 | 2026-09-27 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e5667988-0dce-3c51-928d-3fdd58409a99 | 2.6359 | -60.1648 | 2026-09-27 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 8735f549-8e9d-3554-ac44-0e3b860f16aa | -2.9041 | -45.4168 | 2026-09-27 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 25a01aea-1729-3f3c-8c3d-e50cc6991a81 | -4.266 | -51.0427 | 2026-09-27 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 40d6efad-5058-3230-b16b-fad6029485bc | -11.264 | -54.4434 | 2026-09-27 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a76340e6-cc10-39e0-b99c-3ff34c06a2d5 | -3.9228 | -43.0123 | 2026-09-27 00:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9f1772e7-fe40-30ec-a711-ce8f7e033fe4 | 2.6358 | -60.1839 | 2026-09-27 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 95.4 |
| a878c036-16b9-382c-a128-35dee7ea5034 | -2.9223 | -45.506 | 2026-09-27 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e0757623-9100-3870-9f31-222079e455a3 | -11.2829 | -54.4417 | 2026-09-27 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 5501960c-6990-3427-af52-1645d744387b | -5.1621 | -55.9931 | 2026-09-27 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 36ea012e-2c84-3b45-bae4-2b9bce879d11 | -10.8052 | -60.7257 | 2026-09-27 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0b49aa15-0c7f-39df-bb28-4954257db4c6 | -12.2877 | -50.4004 | 2026-09-27 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 0263accc-2f62-3318-9138-4fb24b804d1d | -11.0396 | -51.3079 | 2026-09-27 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| dd33abfa-e603-32d6-84c1-ff10ce8f0419 | -5.162 | -56.0129 | 2026-09-27 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d939c008-dd39-311a-b176-c9ca6c9278bb | -3.1953 | -51.039 | 2026-09-27 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 57543db1-8530-3112-9cdc-c8b08165ef87 | -2.9041 | -45.4168 | 2026-09-27 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| b5eff290-495c-3722-a207-eebe5c28b00a | -10.8238 | -60.744 | 2026-09-27 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 3caa9d32-2ce0-3d53-a841-39a5daedb65a | 2.6359 | -60.1648 | 2026-09-27 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| bbf00993-7d70-3a86-9645-6e082d81cab4 | -1.6035 | -54.8142 | 2026-09-27 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4abfc061-1a5f-3f56-9f9e-fa4dcaebe699 | -10.8052 | -60.7257 | 2026-09-27 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| aedf9663-fa2f-38d8-9694-d0618e717049 | -5.1621 | -55.9931 | 2026-09-27 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ac1a7745-52fb-3551-8345-5b29b2638620 | -1.6035 | -54.8341 | 2026-09-27 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 2c6116a6-e09f-395f-bf35-b957cb69b722 | -5.162 | -56.0129 | 2026-09-27 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4d8b8b45-95ad-3c1b-9af0-89be6dd1be16 | -6.0733 | -57.822 | 2026-09-27 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| dca0ef60-c9ce-3d8a-96dd-8201ace37c31 | -3.9228 | -43.0123 | 2026-09-27 00:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4c2d0b73-f3c9-3ed4-ae95-b8d3cf6827d5 | 2.6541 | -60.1836 | 2026-09-27 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ceb95dbf-1cf2-3d31-9643-1957c8c3dcda | -11.264 | -54.4434 | 2026-09-27 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 32b010f5-5108-369e-87d0-46a3120b4e9c | -9.2745 | -67.6433 | 2026-09-27 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| cae5855d-b6c4-3b98-afcd-b51cca6f2084 | -12.288 | -50.3789 | 2026-09-27 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| fd335b20-8084-3972-a2de-d1b9f2b513cf | -12.2877 | -50.4004 | 2026-09-27 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| e551ac8e-560f-3ad3-95f7-163e4210cf85 | 2.6358 | -60.1839 | 2026-09-27 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 9701eba1-f8cf-3ca4-92f4-9fdbcc28d6b9 | -11.2829 | -54.4417 | 2026-09-27 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 26ace6d6-ece2-3152-9567-3ee4b48d9767 | -3.9227 | -43.0357 | 2026-09-27 00:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 22d51a9f-c290-3766-a676-cc0867f6c3a4 | -4.266 | -51.0427 | 2026-09-27 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| eae81e1e-e8d3-3a80-9e55-62de098e27e7 | -11.0393 | -51.329 | 2026-09-27 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| ee540c91-f348-307d-87b2-7968a10e6bb4 | -10.824 | -60.7246 | 2026-09-27 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 138.2 |


[Clique aqui para ver as próximas entradas](README2.md)
