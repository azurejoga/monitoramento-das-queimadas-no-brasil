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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40aa6f05-6917-3b57-8007-1c983f7f4ce8 | -7.1147 | -47.84543 | 2025-07-25 04:21:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a30c79b0-9344-38ca-8c83-f2f66190d425 | -8.21076 | -44.93726 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e77c66d0-9369-334d-a077-4999c31c8c19 | -10.42621 | -47.2244 | 2025-07-25 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d6b4d0c-d59f-3edc-88b2-4655b30fd281 | -5.89405 | -49.34836 | 2025-07-25 04:21:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 025a4aaa-1fdd-31f9-bbb0-d36d07bff3bb | -6.90243 | -44.21685 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1801d0f6-d9d1-3776-9c41-f6982cb5e025 | -7.91487 | -44.0808 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d444335-1444-342b-b469-07454303788c | -7.85208 | -48.22148 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fccfef9-263c-3037-a8ea-687810198484 | -3.74543 | -49.04374 | 2025-07-25 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffa6eedc-fb5c-3633-8ddc-3c029898f4e9 | -6.22607 | -44.52737 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd8bc602-03b9-3161-b8b0-1a73ed67c98d | -6.76988 | -43.69961 | 2025-07-25 04:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8602ffa1-f0c9-3233-9f4c-4f6f2a350a12 | -7.10563 | -43.55117 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88640dee-6487-3479-b6fd-6bcfa017d405 | -8.89145 | -45.59949 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d620e00-1ebb-308a-b3aa-1e10f93321f2 | -11.45254 | -45.12509 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d0cf174a-661e-3573-8475-a5c72b108b38 | -4.29205 | -48.05752 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b66f8120-98b8-3efa-af7c-3bce68f413f5 | -7.86004 | -48.21843 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dafba8b8-4390-3f4a-b208-c485a0307e6c | -8.8449 | -45.59558 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8570aeb4-2f8d-3f0e-99cd-d7558daa2227 | -9.73359 | -48.01987 | 2025-07-25 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61c8ac22-6f38-3372-a77c-1e40cad573e3 | -6.91216 | -44.61011 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad52ad87-4929-36f0-9afe-a3438bdd7658 | -10.60972 | -45.24056 | 2025-07-25 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a6fda7d0-849d-3b84-9403-20618c366e5b | -7.4645 | -49.40298 | 2025-07-25 04:21:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e16c6203-cb73-367e-a782-a120a0706e17 | -8.36768 | -51.07528 | 2025-07-25 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a4abba35-460b-3da0-a5f9-d801ccf30494 | -8.09633 | -43.14971 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0dc5582a-8a82-3b01-b70b-065708e0a843 | -4.10708 | -47.93468 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 19582641-92c8-3c61-98fc-2f6006cda5eb | -6.22994 | -44.52443 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b90d6555-8b3f-3dfa-8d78-2b7ffb2b6a0c | -6.64706 | -43.04926 | 2025-07-25 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 830a141d-6d1e-3498-b93d-0780db99119c | -9.59056 | -46.33395 | 2025-07-25 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7720217-e341-3e10-aad9-47454efb1098 | -6.90768 | -44.97881 | 2025-07-25 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66b9e4f1-79b2-3954-8a40-3a217df4e3e3 | -9.11592 | -47.64631 | 2025-07-25 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a699748-0e69-3ee5-8501-0e74b2d912f2 | -9.42365 | -44.73195 | 2025-07-25 04:21:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e45e23c9-2387-354e-b524-c2ccb90bd305 | -9.02402 | -45.33788 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ca777cc-c6ff-30fc-b3f6-f54611d297c5 | -7.26371 | -43.07333 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5c7c64f0-7909-35e0-86b5-868bd63d354b | -9.01075 | -45.33576 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a18eee7e-ee39-327d-9eab-3f8bca2e2b67 | -6.95352 | -44.56338 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0405daf1-e479-3142-bddc-319d942f84f0 | -10.71276 | -48.38607 | 2025-07-25 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f994cb04-c9ed-3e90-89cf-d02ee2d1c8f2 | -10.42946 | -44.17984 | 2025-07-25 04:21:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c85b105c-1691-33d3-8077-557318c80837 | -7.86299 | -48.22324 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21e2c031-1b90-37ee-b1cf-5bdec8c8bdef | -9.42643 | -44.73598 | 2025-07-25 04:21:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d9eaf15-7b53-37c6-90e3-81bc080730f6 | -8.33436 | -44.94967 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1af98f1e-1d5d-3414-92dd-a7091626bc7d | -7.2047 | -45.32978 | 2025-07-25 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9cfc3be-9ac5-38cb-a7db-c108ff4511b5 | -7.16749 | -44.38685 | 2025-07-25 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4af7f642-c898-3b3d-9e60-b84db25bd488 | -6.91077 | -44.22887 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7450122c-9bff-341f-814f-2566d69b6274 | -7.34294 | -45.2907 | 2025-07-25 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcdc74a0-dd76-3afe-a5d1-2a71cb1db0de | -3.31044 | -51.66512 | 2025-07-25 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 202fff1f-7964-3463-b800-9feddb551171 | -6.93819 | -42.80807 | 2025-07-25 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a4983974-4bbb-3ccf-8ba7-49a41e1adb45 | -6.6304 | -49.74619 | 2025-07-25 04:21:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f20bcc5-bc2d-32ce-beb7-44efb3c4fa20 | -4.7794 | -45.33674 | 2025-07-25 04:21:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2682dc7e-6af7-32e1-a6c1-cd9f0421af56 | -7.88845 | -45.539 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b60129ba-9c9f-303b-a042-81ecf003f5a3 | -7.92605 | -44.09704 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dae000c1-299f-38ba-b92f-c95a21d21a63 | -6.98712 | -43.32693 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3a394cb5-a2bd-38d3-8145-d302107c0b44 | -6.20203 | -44.38193 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 242a1dbb-35e9-3acd-941b-47f472c0ed8c | -3.07459 | -52.43561 | 2025-07-25 04:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40f467b7-f724-3a67-a8ab-1297f90fe81c | -8.89368 | -45.5855 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d8366c7-bbe4-32fb-8d8b-d70bd46d7ec2 | -7.10619 | -43.54759 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75652135-306b-3ee0-8622-01fbac988346 | -7.3653 | -48.13755 | 2025-07-25 04:21:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d1cd056-00a1-3322-a67b-ca284f6e4e3c | -3.76211 | -47.50692 | 2025-07-25 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74aa80fc-1bbe-390e-9b75-bfda2c559600 | -7.88457 | -45.54196 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f43ccb01-449d-35ce-8b59-1b029f916890 | -6.90895 | -42.79215 | 2025-07-25 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 46c6a45f-02fd-33ac-bca9-7899ea113c89 | -6.98092 | -43.32225 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 33551666-c7b8-3d75-ad3f-c60d48073303 | -7.25461 | -43.06434 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 862ba50f-3813-3a07-8dca-6b10c1ce06dc | -7.85571 | -48.22207 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b37a408d-9d5c-3320-bc86-b08ac1b6ed25 | -4.31573 | -47.98267 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90e68405-6c94-3075-b095-ec679141cd4d | -6.95461 | -44.55644 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d3914561-cccf-33bb-a10d-e0db97e51814 | -9.65886 | -40.597 | 2025-07-25 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 605cf1a2-17d4-3aaa-9c43-dbed0128c613 | -6.49231 | -50.26596 | 2025-07-25 04:21:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca9d053f-b21e-3db7-b723-f4dc2d711aa7 | -8.89644 | -45.58953 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08178faa-9dde-36d8-95de-c07eb536910d | -10.61903 | -44.76452 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b519e216-0fad-35d2-9df8-ac25180a4ce6 | -6.82674 | -43.05659 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ef8723e-ff5f-39f8-9ba4-ea56f285f416 | -8.21353 | -44.94127 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e93f2c24-6a2b-3354-9991-119a418d8904 | -8.85989 | -45.60516 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9860ccb-b968-3697-9a53-2381a982c61e | -9.07525 | -46.62925 | 2025-07-25 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb99eaad-1505-3a6e-bdad-ecd542fe91d1 | -8.28881 | -44.98176 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07dd2c33-a0b9-3375-83af-d5afff4d36c3 | -4.53988 | -48.00582 | 2025-07-25 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c359f26-7081-3a8e-920f-26658fbc9e83 | -8.33049 | -44.95258 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72411f02-678b-3feb-a0f2-7e60f554223b | -8.21408 | -44.93779 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d5f2171-c32e-370b-845f-69e8b91d677b | -8.07122 | -49.72192 | 2025-07-25 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e57e3021-028e-329f-a8b7-b77e3feeae2c | -6.89964 | -44.21651 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6fdc2ce2-78bf-3842-8e20-a47ea971aed6 | -8.51413 | -43.31506 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| d140bebb-d167-3322-8d76-7af9660e3be3 | -7.08982 | -44.87983 | 2025-07-25 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5fe1904-4bbe-3015-89cc-322952c013c3 | -11.44477 | -45.13111 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d451b9-006e-3a51-ae07-fd4f80382f7d | -6.88096 | -43.11311 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b47db336-9ba3-3eb8-aef7-18eae3a12d12 | -11.46308 | -45.12313 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1b6352b8-c928-3e46-98cb-5a102352b620 | -9.05558 | -46.62235 | 2025-07-25 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4acbce0d-2905-365e-91dd-6b9cf77d4ea0 | -7.91268 | -44.09495 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c79276d-96e5-3c4a-9896-2130b6aa95b1 | -8.84324 | -45.60608 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 077d107c-4e88-3385-a67f-4dd941a02a57 | -8.28991 | -44.9748 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48df465f-97b5-3683-b304-845e54ad58dc | -4.78275 | -45.33728 | 2025-07-25 04:21:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95ece8f5-1cb9-389a-ba1b-5dd83282343c | -6.88323 | -43.12099 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b59fd6e-e887-32c7-821c-44130912e429 | -6.9843 | -43.32279 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 290f3d1c-5aed-3cd4-bfe2-2401d3a45883 | -7.86801 | -48.21535 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b14ca6d-7232-35ac-992b-3c738359082a | -7.20026 | -45.33622 | 2025-07-25 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22bfdac8-43f8-3308-8db8-19907ad105f2 | -11.05585 | -44.78216 | 2025-07-25 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81aa2a02-76f7-34ff-a6a2-01e50f90d799 | -8.12345 | -50.46423 | 2025-07-25 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5937dbbb-4a9f-3a91-a537-61488f4da38c | -9.07408 | -46.63654 | 2025-07-25 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d88b3b1-1eb6-3a13-969f-5a279f0ca706 | -6.58046 | -45.607 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 71e67be7-1ee3-3aab-a4f5-13cfe8f68e08 | -7.25745 | -43.06858 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0630785e-e8f1-3c0c-8a70-dc6283e8ee6d | -10.63628 | -44.76362 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a45c8ec1-19c8-3fa0-8a09-6f138d99301a | -7.99196 | -43.82701 | 2025-07-25 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b04c3006-3113-38c2-8b6c-3deabd836f72 | -8.33381 | -44.9531 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59219d51-bcad-36c2-b5f5-954935a4d43f | -7.08428 | -44.87184 | 2025-07-25 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b52a4640-7a40-3400-b4cf-4529f723909f | -11.4592 | -45.12615 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README14.md)
