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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cac5ffe-b288-3105-9008-5a8eb045a5a0 | -9.47482 | -48.74633 | 2025-11-09 03:49:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da39c344-e4f4-3543-9c0d-d333fa2a37d4 | -4.05446 | -46.43053 | 2025-11-09 03:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f3513877-d92b-33cc-a07a-70e66cebcf1d | -4.67895 | -45.69033 | 2025-11-09 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 420c92f6-f866-3fc3-b8fd-f8ace14166db | -7.08696 | -35.12749 | 2025-11-09 03:49:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 85d3fcbb-2a24-369a-9903-9edc1f688aa8 | -4.68544 | -45.84963 | 2025-11-09 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a3a58af-59ba-35b1-a41f-70ac8f2d835b | -4.39806 | -45.96968 | 2025-11-09 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1e81935-aabf-38db-925d-f356d09ad0fb | -19.761 | -58.1269 | 2025-11-09 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 7c729b0b-b7af-3bba-a3ee-69fc2fad9819 | -3.3369 | -44.3806 | 2025-11-09 03:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ffacba08-2d0f-350a-a960-d1930ac7b3f2 | -3.3369 | -44.3806 | 2025-11-09 04:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ba3feb18-08bd-3a9e-88ce-d5213aff1221 | -4.4534 | -44.6447 | 2025-11-09 04:00:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 91afd8dc-b1ca-3b62-8f4f-daaddea40309 | -10.3248 | -49.6341 | 2025-11-09 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6335b1d6-5cc2-3eec-831f-c1c70e7c6bf9 | -19.761 | -58.1269 | 2025-11-09 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 6b25753d-2cc5-380f-aea6-478782990d22 | -10.3437 | -49.6321 | 2025-11-09 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 311287e2-0668-3821-88ae-8748c672ff1a | -19.761 | -58.1269 | 2025-11-09 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 62cbf48b-a53a-3447-aec2-1f242696fbfd | -3.3369 | -44.3806 | 2025-11-09 04:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 6b4f14bf-30ff-3716-a645-92d6373f45c6 | -4.4534 | -44.6447 | 2025-11-09 04:10:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 70f618a5-e48c-34d2-b807-679a8f416239 | -3.45583 | -45.65228 | 2025-11-09 04:16:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bfdb2c3-1c38-3ec0-9f19-7c5ff1b76019 | -2.64207 | -47.30414 | 2025-11-09 04:16:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 446e8387-c0d5-32b1-a191-28f334c76a2a | -3.15605 | -50.59681 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af821229-fb68-3f90-9615-e3bd0c0015c2 | -4.14584 | -46.25953 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd7e03ef-2b37-3e55-8942-73c6e31b82f8 | -3.03094 | -50.27245 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f85ab2f8-504d-361c-b975-11ce733a16ae | -4.05344 | -46.42757 | 2025-11-09 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cc8f2bf8-bc0c-34f9-958a-7cf7061523da | -3.91955 | -51.0132 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c208b1-02ec-3d4b-b836-9594b6b74bf7 | -4.68326 | -46.40736 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 533ffd9e-ae3d-383f-aaf6-2a2661349a6c | -3.89438 | -47.18034 | 2025-11-09 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9dbacf1-cb7b-3cff-b0d2-e6bd8602510c | -2.97132 | -49.82844 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8940de73-cdbf-3047-b2db-4a3852bc5b31 | -2.83506 | -50.43916 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f24f9252-5b19-34e7-97c3-c40f68a98fb1 | -3.32086 | -50.10331 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fdeb0ac8-26b3-3b33-84e4-f476342d00aa | -4.26832 | -45.53795 | 2025-11-09 04:16:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0408692-1a81-3286-85ca-1a0c957d4d9b | -2.60818 | -49.21755 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a6c5b17-2dd0-34da-8abd-c9911501502a | -3.06954 | -50.28411 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfbddf45-bd78-39f6-a5fe-1d79470af8b3 | -3.09411 | -50.32339 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d685a8ee-0970-37be-b71d-fb9cce9f4d38 | -3.45598 | -49.97155 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f8c38ad9-a79f-3871-88c8-3fe7f9d200e3 | -4.70531 | -44.41383 | 2025-11-09 04:16:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 909b6c56-2b13-37b2-b511-ee38c950cb12 | -4.81028 | -38.69173 | 2025-11-09 04:16:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d7986c46-d58e-3cef-8265-d8a649f6ee7a | -5.60809 | -39.5484 | 2025-11-09 04:16:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c0d261e3-13d2-3987-af33-aec534eb39b3 | -4.13818 | -47.65602 | 2025-11-09 04:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb4558a2-b4b0-301b-858f-28c9ac981292 | -3.15102 | -50.59596 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5361a36-0bb3-33d9-bd1d-3324b5dda9a8 | -4.51926 | -48.83546 | 2025-11-09 04:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81b3bca4-6397-33eb-90b7-dc6040eda4b1 | -2.74073 | -45.15971 | 2025-11-09 04:16:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6862e577-83cc-320e-870c-bca21f74cf0f | -4.90962 | -44.6418 | 2025-11-09 04:16:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 709ee958-4f8a-3e74-974b-f96c26713293 | -4.89192 | -48.59601 | 2025-11-09 04:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f83a5194-7d42-3da2-a0ac-7f1e4d0bc3d0 | -5.4953 | -39.07509 | 2025-11-09 04:16:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c3c41658-7f21-337c-b2e8-738a376c3c4c | -4.59874 | -45.99347 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b150a2ae-ef8a-3f59-aa63-44eaf9442137 | -3.31965 | -49.13437 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d13537c7-532c-304f-9343-415b1fc821f2 | -3.31353 | -50.10128 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0eb4f095-2f53-3c66-84cb-cdeef1f76140 | -2.94682 | -49.35417 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 19516c91-7b5b-3702-ba29-22274ef43979 | -3.03545 | -50.30687 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b37ea5e-be13-349a-b593-f7d1f19e88fe | -3.335 | -50.0785 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e3927c9-19cb-3b4a-8e8f-54583cc4a2ad | -4.72165 | -42.93279 | 2025-11-09 04:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34d298ca-896c-39db-8ea9-c1b14a8d5d4d | -3.32418 | -49.13514 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cb06614-a503-338d-a79d-7c8d41a13595 | -4.54138 | -44.60702 | 2025-11-09 04:16:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e32f7ce6-67ca-3553-b553-d48029c8a82b | -4.29204 | -50.66259 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aa87e4d0-8a5b-3a2e-bb7d-a73ea9d26d8c | -5.28254 | -44.95229 | 2025-11-09 04:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 7148872d-c1e5-38ae-ba1d-d8cfc48614ff | -2.61123 | -49.22777 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b11ba6f1-9104-3761-b3dc-aebbe471beeb | -5.38802 | -44.73132 | 2025-11-09 04:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81bdc160-b926-3ed3-b0aa-eabde7ace7e4 | -3.8857 | -47.18398 | 2025-11-09 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5632a69b-168c-3b6a-930e-f70266ec607e | -3.75605 | -45.99305 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9560ad97-03d7-3428-856d-b5240ae5bf3a | -5.30668 | -47.2835 | 2025-11-09 04:16:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ba38f42-9acf-3de0-8d76-5710bf473be9 | -4.28604 | -50.66662 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ca2a3a5-5d97-35a5-bfe9-5976004c53bc | -4.5846 | -45.62529 | 2025-11-09 04:16:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b8d9882-094a-35f1-91c3-33f3dbbf8882 | -4.72023 | -48.30518 | 2025-11-09 04:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38e6c74f-3787-3fa4-8572-2049e2af21fa | -4.00724 | -44.7785 | 2025-11-09 04:16:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 910c10bf-77eb-323d-acc3-673031a8a1b0 | -3.50061 | -50.0595 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 176ed9b8-bcac-3bc3-bfdc-56ca70780e63 | -2.61584 | -49.22851 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e75950e4-bfa5-3d8f-bd2c-69dcee9b130c | -3.14175 | -50.28037 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a1791c9c-562a-3287-b78b-a31220c17c2f | -4.70197 | -45.88354 | 2025-11-09 04:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4dd704a-43bc-3708-9202-6f70d8dc4d00 | -3.84454 | -49.81318 | 2025-11-09 04:16:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bb3ff5b1-c3d6-3db2-a2a5-a4df29e97242 | -4.37996 | -45.49221 | 2025-11-09 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c853180f-9f01-3add-a312-7c3b42a83f93 | -5.13952 | -45.72175 | 2025-11-09 04:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 596dc268-7361-36b3-a6c1-8a12669c3f1d | -3.64433 | -49.86805 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4baf41f-2cba-3f5a-a3f5-9fb0822d8e62 | -3.09895 | -49.25451 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0952f0df-cd13-3f2b-88a9-3042a272cfdd | -3.30893 | -50.16076 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d2d73bb-3caa-3e2c-a1f2-bf0c9dbeba18 | -3.05661 | -50.21574 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21539559-a610-31fa-8aca-eab9447baee3 | -3.42903 | -52.89504 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57e6d92c-e972-3709-9a38-71b265a9c30c | -4.76145 | -38.67942 | 2025-11-09 04:16:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c6733c5e-683e-3d86-a4b9-e9910f1c5ea6 | -5.13595 | -45.72116 | 2025-11-09 04:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c13a1d73-d565-3df0-a545-2727bd8466c8 | -3.65784 | -50.22971 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f4ba714-fe6f-342d-93e6-651c5a6d155b | -4.67834 | -45.689 | 2025-11-09 04:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c058bbea-5c04-327f-9015-3234c1631ba0 | -3.06149 | -50.21671 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4498b072-9e06-3f11-b034-eecdd5b5e1d5 | -4.28697 | -50.66099 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12b6ac93-7a65-3db0-8496-76b5e9657448 | -2.60278 | -49.22157 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d46906e-5960-3e10-b6b8-b1e789662a3b | -3.15054 | -50.59886 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a2aebf9-c99b-3238-926c-bbe89a2268a6 | -3.86526 | -49.37954 | 2025-11-09 04:16:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8d9e8966-3d42-3f49-ab27-6c5896dc90f0 | -2.97674 | -48.70699 | 2025-11-09 04:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e73f8450-72e3-3e06-8a9c-e8b812d222e4 | -4.7583 | -47.52647 | 2025-11-09 04:16:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6f73388-5884-3c9f-9f47-f2896198943b | -4.84782 | -45.04846 | 2025-11-09 04:16:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 628f066d-5541-3021-b9aa-ac08ba3e99a1 | -4.80018 | -44.73939 | 2025-11-09 04:16:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdb85b27-0f1f-3e41-881d-57010eaafe16 | -6.76291 | -35.42942 | 2025-11-09 04:16:00 | NPP-375D | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1948ea59-f2b5-380c-b8a0-fb1e2ce94baf | -3.3166 | -49.12459 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fffe2fb3-0d9e-388e-8bbf-1af23c8719a4 | -4.12319 | -47.29552 | 2025-11-09 04:16:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 819901a8-34f9-3bb4-9979-3f5a34f33c3c | -4.2099 | -47.7778 | 2025-11-09 04:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8570156e-d5b5-3450-977f-6eef5bc60aab | -3.33563 | -44.3748 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| de3ebe2b-ae9a-34fb-9e28-5ac3afb26333 | -5.15841 | -46.13117 | 2025-11-09 04:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a580d44-7c47-3ecd-9a36-3daa029700e9 | -4.96236 | -44.94548 | 2025-11-09 04:16:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 2b65be9c-1b99-3927-9397-2f5ced207308 | -5.21642 | -45.14045 | 2025-11-09 04:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06d746b7-e1b5-34ff-98ae-933780a469db | -4.29283 | -49.73625 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ead01837-cc3d-3c3c-a77b-b8f08de798b2 | -5.80859 | -41.34523 | 2025-11-09 04:16:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 688e7b70-4ab5-3e65-b7da-d0ce9e423ea8 | -3.53726 | -50.85645 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e06bd2b-44d5-32f6-a305-1c2399c90424 | -4.76074 | -38.6841 | 2025-11-09 04:16:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README13.md)
