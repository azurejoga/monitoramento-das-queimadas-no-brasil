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
| 9b606f34-baf3-36f9-85da-a4f7ca6afac1 | -5.30355 | -56.01504 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eed7bbd6-a6c1-3061-b145-6b718715f28c | -9.6357 | -47.68723 | 2026-09-06 05:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 275956c5-8d4b-332c-ab9d-110fbc3a166e | -3.79243 | -55.88199 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac0a6a77-6aa8-380b-88ef-b2d88743ad61 | -4.29772 | -55.72514 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4519354e-33dc-35e7-a476-a9b928b8223e | -6.89626 | -62.9542 | 2026-09-06 05:23:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 94e6aaf4-1848-3f38-adf7-ca0635e39d67 | -10.74795 | -60.7174 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b954f071-ab7c-3ef1-8739-bb2b199fc2c9 | -1.49403 | -54.82081 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3283058-cbd7-357f-b5fc-1f067fa9a1fc | -3.78028 | -58.85233 | 2026-09-06 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8c5cb8c-f48f-3221-a284-97e9b15077bd | -3.22934 | -50.57595 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13ea2d99-0f75-32d0-a125-daa145df27bb | -4.66409 | -55.64226 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 729672ef-683a-3604-88d6-09f46d74db8c | -5.35897 | -56.02335 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d1bb9081-795a-3aa9-b2cc-b9b752257f3b | -2.87435 | -50.46189 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 937db4f7-1787-32fb-9f21-b1cf1170090d | -10.74923 | -60.70965 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 52ad66ca-9d3f-3514-b6b4-711657e71c60 | -10.74511 | -60.71292 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 48f6e612-5b70-32a5-b1b8-d9a21d60c02c | -5.33552 | -56.03095 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7e94eb7-1abd-301b-8d5e-58fd6a247d41 | -10.75644 | -60.77474 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad2afdbd-f235-3453-b70a-61280936f079 | -3.12043 | -57.69143 | 2026-09-06 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7eaeae1f-4d7a-324f-8235-1f84a90c9ae0 | -5.14144 | -56.27253 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6118b36e-95ce-3553-9b53-346c5bf8c6ab | -6.06286 | -57.80296 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a2d3659-b9ba-3241-b40a-27aaa3cf4e69 | -4.67819 | -55.64073 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07c4a64f-3b4e-3b4b-b10a-689c37ea9832 | -6.89977 | -62.95864 | 2026-09-06 05:23:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6c1e01af-ae25-342e-9e4d-f5c538181c3e | -4.87854 | -55.8765 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a3bfc49-5247-36de-82fe-5cc79e5ce807 | -6.0256 | -60.16805 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e3af3c1-5b28-355d-91c4-22932b1e6ecc | -5.34001 | -56.02436 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db575c2-0c10-33cd-b579-b6ac8461ec7c | -5.84623 | -52.04959 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 306e9b44-f281-34f5-a1c6-93b2d3bd0c44 | -6.56848 | -58.98082 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a251261-d7e9-3df8-a8e1-b22a45c2b79b | -4.35139 | -48.96822 | 2026-09-06 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58817e3e-a0b1-3755-93a0-9a6e192f6b38 | -6.9491 | -59.73396 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 957ca697-3b44-338c-8e91-5b184e2e9ad1 | -4.67254 | -55.63249 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1929eedb-99e5-3cb0-8b90-34e70b91c0d8 | -7.10597 | -56.51978 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 367ebe4b-cbc2-3427-879f-1a888648fe94 | -5.33216 | -56.03043 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e511101-c836-3a9d-9a78-84eb897c3b34 | -6.13049 | -57.74242 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33bbc96e-572f-3e0d-aa60-17b27f607c3b | -5.253 | -59.97594 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60a70e9e-cd8e-33cb-9325-4327c4bc14e3 | -6.87727 | -55.61329 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e07f21c-fd96-3fd8-b398-cc5767756e51 | -7.37435 | -47.02283 | 2026-09-06 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0ce00b2-beeb-3262-b52e-a180f36ba5f4 | -5.35786 | -56.03048 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| caa1875e-7316-358c-aa91-051feaeb7574 | -5.37021 | -56.03969 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c995ec5f-7bdf-3aeb-9b68-2caf6cd0fa0a | -5.37077 | -56.03613 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5aa84d93-5d7d-31e7-aa7c-73a15a0ee2ee | -6.10609 | -57.70292 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60fc5865-d15d-3da9-b55d-ccd98f9dedb0 | -7.45029 | -49.72982 | 2026-09-06 05:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 868eecce-c48d-3a6b-b757-9d96cbc631f3 | -1.57969 | -55.73384 | 2026-09-06 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb1bf3f0-cfbe-3a63-8c2b-131ce08e9aac | -5.25527 | -59.98452 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0461646-6dec-3bb8-aa8a-24b42fb0a8b8 | -3.832 | -60.76743 | 2026-09-06 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d8c2582-0e2c-30f7-b2aa-3c3159554251 | -2.46603 | -54.72244 | 2026-09-06 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66c6be09-d284-373a-921d-1de3e0d3a6ea | -4.09442 | -55.15629 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dadf1964-a35b-3146-ab5f-2245cc74b7a5 | -7.369 | -47.01778 | 2026-09-06 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35ca0ee6-4b93-3d39-bea4-d2e5d699d82a | -5.34505 | -56.03608 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bfc1104-9cb8-36fe-8293-a7eaf362a8fe | -3.37675 | -59.41643 | 2026-09-06 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec6bb2af-0f5f-3d32-85d0-96307fa1545c | -3.42357 | -58.31321 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2b8daae-0d29-30d6-9e6e-24704afe86fd | -5.92657 | -47.8924 | 2026-09-06 05:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d56a75e-1043-31fb-bfa4-02780ef642ff | -10.7479 | -60.76126 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e669470f-54d7-30d2-9907-78522077138a | -5.30019 | -56.01452 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 472479e2-e63f-3a7e-b886-9608a9442162 | -4.45237 | -46.13743 | 2026-09-06 05:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 62a48887-1f61-3f4f-b8ef-0df25306e3ca | -6.83454 | -59.43368 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fd5fa9e-f567-393c-9cb8-343da1a3889e | -3.54457 | -48.18471 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 34549948-c272-3005-af11-56a4ddb75b22 | -15.48863 | -50.36906 | 2026-09-06 05:23:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6219cc5a-0cc5-3664-a0dd-58b31f25a75d | -8.50226 | -54.65532 | 2026-09-06 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6803e549-0187-3cba-b4eb-b9a58921c594 | -3.08245 | -61.18056 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d64c36f0-f702-32de-815c-915cf39955a5 | -3.14456 | -60.64988 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d2043dd-41ac-30aa-82b8-90c60a60c0f0 | -4.67537 | -55.6366 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fb882e8-c17f-3dfa-b642-e2da4771e1b5 | -5.36348 | -56.03864 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69636c99-3edf-3bd0-aa44-020ae1b12b85 | -3.20592 | -54.58552 | 2026-09-06 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fea31423-d265-379b-9866-c170836e2e73 | -3.15058 | -60.6367 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32bd239a-ad81-3dde-9228-30ca46b34cdf | -3.38383 | -59.41756 | 2026-09-06 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb4f9ee6-7bcb-35cb-a50d-682fb841af59 | -3.71547 | -51.13876 | 2026-09-06 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d9321e0-85db-3d7f-99cc-237047f14982 | -3.97291 | -55.70736 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 205ec25b-ff71-32a2-bfc6-26bd4fbcf4f4 | -5.84649 | -60.25381 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 09d90b4b-d874-3237-be8b-7a17e5bc47ac | -15.49082 | -50.36699 | 2026-09-06 05:23:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 601f4b36-163b-3f6f-9f68-44d0f1608f48 | -6.02494 | -60.1721 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66d411f2-a9fe-3550-af39-d56a768555ff | -3.55582 | -48.18028 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8ff5e469-80fa-3caf-a799-55c6fa6d3f27 | -2.46104 | -57.91192 | 2026-09-06 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f7fb9d78-4ee8-3a15-af48-727974b3165e | -5.15208 | -55.96279 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d35fe9c-1eb1-31fa-811e-ffa2473fc800 | -6.44285 | -58.15719 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47134c72-1404-3413-b394-7be845f206b0 | -6.88013 | -55.61755 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99b226fd-f9c9-3fac-a820-aa5a79f0765b | -1.56423 | -55.7883 | 2026-09-06 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb0429dc-b724-3c38-ab3c-daa7afd3fe7e | -13.80863 | -51.65014 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8f919db-a8ba-3202-ba28-35aac30c26f9 | -6.20407 | -57.76902 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fc99d2c-8f8a-3fbb-8844-6270002ea289 | -5.34947 | -56.04012 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b408e4f6-dab9-394d-ba45-c5e171216642 | -7.9697 | -54.90502 | 2026-09-06 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c69113fe-a6d2-3b39-a748-998364b492e9 | -7.96612 | -54.90449 | 2026-09-06 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9cb9566-b03a-3499-a37a-f271f4065fb5 | -5.15319 | -55.95565 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cbb32b1-59fc-3175-9ffc-90b6db60f6ea | -2.86122 | -50.45987 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f003bc4b-e90a-36ce-8851-7602edfce09a | -6.44007 | -58.15316 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c3bef6c-c117-35e1-bbd1-0434b7d6e23b | -5.17467 | -56.06075 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68571857-44ad-368e-92b3-4a929a3cf24c | -3.62328 | -54.60539 | 2026-09-06 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a69363b8-2330-3600-a0a9-7a036afd5cbe | -4.44895 | -46.13387 | 2026-09-06 05:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f5c88ca-a460-30ed-8b29-2d4b2337ae94 | -6.0285 | -60.17271 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d62203cb-30fa-3775-885d-9a3711fc52df | -7.09981 | -56.51519 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48698696-26e5-3126-a44c-3938115faee4 | -4.66971 | -55.6284 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bbb241f8-2276-3ae8-9313-7e1ef5e5d2c0 | -5.20333 | -60.03407 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50ca9046-fcc9-3665-a9b1-01f6df65742e | -5.28125 | -60.12881 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de7db714-cbde-3b71-a2cd-8a6ec24244c5 | -3.07329 | -61.08866 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46ba4ba5-04ea-31c1-b97a-3dfd7f73518b | -6.18516 | -57.58808 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf5f724d-51a1-3616-9289-6b7b452a9718 | -5.83215 | -60.2515 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bddc7975-dc15-33d1-96bb-bedceb8f2742 | -3.41434 | -54.77415 | 2026-09-06 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cea96e3-c487-3f48-a53d-8e9cb88d7fd1 | -6.05454 | -57.79096 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85e3a8ed-adc0-31cd-8abe-b8440d49ec16 | -6.87325 | -55.6165 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31c1060e-c0dc-3d0e-b3a7-882559be4509 | -5.13806 | -60.36637 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddff9d13-8a26-305d-a411-bf5240f40462 | -11.42026 | -56.22201 | 2026-09-06 05:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 533101d9-b3a7-3db0-af90-234b74d807c7 | -3.23012 | -58.89043 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README28.md)
