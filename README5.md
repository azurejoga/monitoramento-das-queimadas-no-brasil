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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34ea417a-8af0-39b5-81db-542a0a1aa3d1 | -4.60719 | -45.83883 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 027bb682-2c5d-3842-bb71-db21bab85dbc | -4.60435 | -47.54413 | 2024-10-23 00:48:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6267c40f-7190-37f0-8a41-9d0a481451e0 | -4.6033 | -50.92004 | 2024-10-23 00:48:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 399331a9-a85d-3a0d-905c-6c8b87f45881 | -4.60309 | -47.53502 | 2024-10-23 00:48:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e0696b48-4055-3bb5-8afd-553e42debad5 | -4.60182 | -47.5259 | 2024-10-23 00:48:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 13502e9b-6e66-395e-8d10-0112565473ef | -4.59282 | -47.52713 | 2024-10-23 00:48:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c779d224-1f69-3d50-8bd9-47374326c398 | -4.54071 | -48.83112 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bcbd675c-7ed1-31a7-b39e-333099391958 | -4.5338 | -46.63453 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 5aaa60b5-964a-379c-ae38-0002caf5b24e | -4.53257 | -46.62571 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 43.2 |
| db539f4d-1acc-3587-ac3d-1f2aa32cfbaa | -4.52496 | -46.63577 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 553ece31-74dc-36fd-aff4-c59a7eb5db19 | -4.52374 | -46.62696 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 43b36c5c-ea31-3dd5-ab1b-251cff9b5858 | -4.47411 | -45.48174 | 2024-10-23 00:48:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 228bcd9d-886e-34c3-a8da-e9026ba0fe72 | -4.47195 | -48.11913 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb2878c4-81b3-3707-ad39-d8567fe6263c | -4.42672 | -49.80094 | 2024-10-23 00:48:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e7c9f8d1-1c1f-3446-bca7-7073106c1547 | -4.40654 | -48.84062 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 8ec1d4fd-0b58-3f82-a279-3e879c9673e6 | -4.4051 | -48.83023 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0a37b8fd-ac63-3659-9836-7ca9ba3152bd | -4.39067 | -44.50248 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a57f3ea4-11f4-31dc-ae80-bd1196fd7dd4 | -4.3899 | -49.75789 | 2024-10-23 00:48:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| df893d57-c40c-3e01-8a5c-e8d99146aab0 | -4.38937 | -45.66462 | 2024-10-23 00:48:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6999ed44-b53d-308c-81e9-a806d5a0bf86 | -4.37206 | -48.47765 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1837e520-6983-391a-9f10-bb0951eec920 | -4.36528 | -48.47437 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ee189a10-c7f4-353f-bcf4-d743ab2f45e6 | -4.36179 | -46.78807 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2ee112db-b905-337a-afe0-3d0e13ebb604 | -4.34711 | -48.61962 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| bacb5e58-4542-3c91-b1c8-ca6adda412f4 | -4.34546 | -47.60191 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 439040b5-af8e-3e52-b6a1-2f0116fd4c08 | -4.33769 | -48.62088 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ffd9ce90-0762-371c-805f-e3178574c160 | -4.33565 | -47.6001 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 2fe5bcf2-3297-32be-a4d7-bea435b6628e | -4.28099 | -48.07024 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6775c07f-7d42-35e3-b6a1-49e98b56cdec | -4.27076 | -45.60526 | 2024-10-23 00:48:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 78dfa2bf-9b61-3166-80f4-78f018221057 | -4.2695 | -45.59631 | 2024-10-23 00:48:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 04f4005c-4511-302b-8151-e8d6ed951888 | -4.24591 | -48.34681 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| ef705b99-f60e-3678-a9a8-849880eaf68e | -4.23666 | -48.34823 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b4bd18e0-d7c2-30b6-aed7-7c619db6a36b | -4.19796 | -49.401 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7e8f9698-c022-3f02-b63f-eadda3ff1ea2 | -4.19272 | -48.03086 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5378ded-7d24-3202-8555-47b1763775f1 | -4.19139 | -47.95427 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 910a53d3-e0ea-312d-9deb-c6ecb87f7256 | -4.19009 | -47.94487 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 63118c90-5468-3c39-8f2f-46f49154a28a | -4.17858 | -48.59372 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a5a64669-cd19-3aac-ad7e-f530a0bb7c06 | -4.17837 | -47.9944 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e99c2c44-6d50-370d-a66a-d1b01f319963 | -4.17707 | -47.98498 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 8221a12e-b329-3643-89d0-1dffe4fe0dec | -4.17059 | -48.60514 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 70078eee-7c67-34bb-876f-dccf254ce69c | -4.16921 | -48.5951 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 071de497-3ba5-36c1-9fd4-e83638ac4235 | -4.16104 | -46.86461 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c32e43d5-9064-39d9-b707-4f4a85e9684c | -4.1168 | -48.49072 | 2024-10-23 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cd0cdb5e-beeb-3f04-bb57-4d2e176d7ead | -4.11122 | -48.24273 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9677d950-b64c-30ce-b02d-300f84ee6216 | -4.10535 | -44.24076 | 2024-10-23 00:48:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8a16190a-d72d-371b-91be-7cad4c8a0a19 | -4.10392 | -44.23069 | 2024-10-23 00:48:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 9bb34ddc-04ac-396a-9b77-7670629bdba6 | -4.10201 | -48.24405 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2342eaaf-46a6-3960-8342-e0b064706a21 | -4.07831 | -48.27694 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 526428e3-4a99-3121-9952-7521488f21b0 | -4.06515 | -48.24922 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a25c67cc-2064-3f35-9ab1-97e281f7ad08 | -4.04699 | -48.11517 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 66e9a8f3-ab53-3689-8098-f9a011c42b9c | -4.0457 | -48.10573 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 8728f2a4-bd20-3df6-ae2c-bb7bc2d26a38 | -4.01688 | -46.03762 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1bf14297-a5e6-34d0-825e-3fa4d31d2539 | -4.01565 | -46.02877 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d57b039d-b690-3986-bf08-22077fa6412e | -4.01244 | -44.75371 | 2024-10-23 00:48:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 606b8be4-22aa-3286-bf04-eef9f248efc8 | -4.00557 | -46.02121 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| ae265bb8-495d-3a23-9599-ab6d11dd7d66 | -4.00434 | -46.01237 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1a67bead-4eae-3879-9b39-65dbc1dbe552 | -3.99691 | -48.96402 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2b12f1ab-c058-32c8-a172-56376bf48bae | -3.9955 | -48.95364 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 14625de3-0edf-31eb-8da9-d5f74b53510f | -3.98498 | -46.47047 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5269bbaa-a61a-3da1-8350-a1eb07685b69 | -3.98162 | -49.02565 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 2ee42f90-d518-34d1-989e-5704f4938d13 | -3.98016 | -49.01522 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d829bdc6-a428-3a74-9be7-f2843fce15f6 | -3.97616 | -46.47172 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1bce0f72-a45e-3f33-864f-9ea94a686f37 | -3.97444 | -44.74946 | 2024-10-23 00:48:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| eed23a0e-0cea-3e59-a3dd-f99b662c0087 | -3.97202 | -49.0269 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c02a63ef-23ac-3ab7-9894-9c9620f82236 | -3.93091 | -48.33937 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 55fd3f41-4138-3fcd-bc90-211800abe6cc | -3.91642 | -48.37123 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 75fd5df2-bdcc-3cfb-9119-3e2584898d69 | -3.91509 | -48.36145 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dd738acf-25f8-3d23-9062-b260bfd5eeb2 | -3.91111 | -48.3323 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 94f6508f-fdc8-3ab7-95cb-af77fae3c509 | -3.90302 | -46.14103 | 2024-10-23 00:48:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7871b473-0294-393a-819c-a51ab6bd28dd | -3.90188 | -48.33359 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a09f4b84-7f4c-397b-8d30-ead1553b3e7f | -3.89233 | -45.66543 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5a20ddb7-de52-364b-aaf1-05690be70e63 | -3.89133 | -48.32524 | 2024-10-23 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d95473a5-38c8-3c53-890c-0272ae47574c | -3.89107 | -45.65648 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6b9a10a3-f69a-3f05-b3f9-369f68a041d3 | -3.88933 | -46.44508 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9c7699d5-6fc4-3840-8bed-cd0e16f7b4f7 | -3.88295 | -46.46391 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8661cdbf-ed8a-35ae-bfbc-5e3a4b94861c | -3.86209 | -46.63718 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 68891441-0822-3c8b-a44b-271bf34c1150 | -3.85155 | -46.10926 | 2024-10-23 00:48:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0e883336-6081-3001-92ef-7b3a5450316d | -3.85011 | -46.48648 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 41e78526-2124-31e8-bcbf-3ef3c18b5725 | -3.82956 | -48.87318 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| f7fe498d-464e-3855-8112-9de79ccf47c6 | -3.82812 | -46.92694 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 53122409-4605-3b51-a642-78f4b9cf5098 | -3.82147 | -48.88476 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b32aa51a-c2a6-3970-aafa-44ee22e9e7a8 | -3.82006 | -48.87449 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 202768ee-66ce-32c5-849c-afeddfb758a7 | -3.81805 | -46.91935 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1b18fa1f-47b5-316a-ba8a-978f4a23b16b | -3.80215 | -47.80529 | 2024-10-23 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2d8a0fca-e161-35f8-b1c8-9b78c81a9059 | -3.80087 | -47.79604 | 2024-10-23 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 5b96593a-0f30-3215-b733-e33cb7e2af60 | -3.79528 | -52.39117 | 2024-10-23 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 88c1b751-a2b3-35b8-bd6d-2c8a795667b2 | -3.78576 | -52.38667 | 2024-10-23 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 0afe1e04-8a91-3981-9d29-754d9fb59217 | -3.78475 | -52.18884 | 2024-10-23 00:48:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8edaa9ca-8483-3c41-af30-50a8262f3618 | -3.78294 | -52.39273 | 2024-10-23 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d3ee9706-b76b-37c3-b7ff-210aad4ff39e | -3.78244 | -52.17139 | 2024-10-23 00:48:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| dcd87d42-e4c0-3afd-8053-cb1a17eb411f | -3.77807 | -52.17775 | 2024-10-23 00:48:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 4c08c6d3-436c-31c2-ba05-7ab8aecf5641 | -3.76984 | -45.97659 | 2024-10-23 00:48:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 685adcd2-7189-3b09-8790-3390c0b1aad4 | -3.7299 | -47.81539 | 2024-10-23 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 081a8e6d-784d-3ae5-be92-2c66d48e0c12 | -3.69036 | -45.41198 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2aa83b8c-9fe4-3185-8720-b7b6c1367ca8 | -3.68954 | -49.05232 | 2024-10-23 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c88a7e08-d42f-3a8c-859d-4c587fa230ff | -3.68907 | -45.40288 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7b099c27-cb25-3c0a-8721-7ab164e7fc9c | -3.68663 | -44.40316 | 2024-10-23 00:48:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9962d728-b888-304b-900b-2a2ffa10bab6 | -3.68139 | -45.41325 | 2024-10-23 00:48:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| c2d26862-e38b-3281-85fa-54822c6a11d0 | -3.6801 | -45.40416 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 36feeef0-4360-3d0d-85a2-dbde13a1a86d | -3.65711 | -54.22433 | 2024-10-23 00:48:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6c0c3c3b-5c7c-3e4f-ad40-006ed9a12b93 | -3.65478 | -54.80043 | 2024-10-23 00:48:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |


[Clique aqui para ver as próximas entradas](README6.md)
