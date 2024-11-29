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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce0641b5-84f2-3801-aec2-b55775616964 | -4.4404 | -46.5975 | 2024-11-29 03:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 3b6729d4-385b-345e-b800-1fbb060ad1ca | -2.3419 | -46.8781 | 2024-11-29 03:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 84c68659-e61b-3260-bf7d-f2629c630995 | -1.5897 | -52.2915 | 2024-11-29 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 61beeb7d-6503-3769-aa86-9d1e1e25b4fe | -3.0028 | -53.2815 | 2024-11-29 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| a889aaae-4670-341c-8f45-aaed5dd0cc61 | -1.092 | -53.3954 | 2024-11-29 03:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 84222e18-6887-35e2-9985-f73a50f20d3f | -2.6499 | -48.7772 | 2024-11-29 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 57151ff0-c76f-310b-9a38-1852d75d4703 | -1.6997 | -52.4535 | 2024-11-29 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 5bee8b9a-61f4-3023-9a83-87c94f1ec68c | -17.6007 | -42.7434 | 2024-11-29 03:30:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| ac6d855a-f466-377f-96b6-2c7e687e50be | -4.2225 | -45.7634 | 2024-11-29 03:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7bb210ab-02fd-313f-b7e6-52b1b800e831 | -2.6684 | -48.7767 | 2024-11-29 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 250.7 |
| fbc8e417-3a7a-3499-9a36-861efe5db181 | -2.966 | -53.2824 | 2024-11-29 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 8680b848-59b7-39d0-9f10-6a359a201af2 | -2.9844 | -53.2819 | 2024-11-29 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 209.3 |
| 6f5e7941-bdd4-3ded-a9a5-a49c645daa59 | -4.4405 | -46.5754 | 2024-11-29 03:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 1412aabc-1a7b-3764-86f5-f657bf4730f5 | -2.6498 | -48.7986 | 2024-11-29 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| afb5c5c9-a2d3-3d8e-855a-1ff6cbd5147b | -17.5805 | -42.7483 | 2024-11-29 03:30:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9d2fc836-78af-3839-b5b1-a7fcb9fa71b0 | -4.2411 | -45.7625 | 2024-11-29 03:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 8644d3f1-89db-33dc-98ae-65cb3e00210c | -4.2411 | -45.7625 | 2024-11-29 03:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 8eebda46-26fe-3d47-96dc-dece6f0e9806 | -2.966 | -53.2824 | 2024-11-29 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 7f614cec-e679-3d48-9ed0-7e75d7889862 | -1.6997 | -52.4535 | 2024-11-29 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| bf5b3ff1-e91e-3360-aad8-cdfed66b3381 | -2.3419 | -46.8781 | 2024-11-29 03:40:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 200.7 |
| c0c152b8-a1e0-3bb1-a857-6640e4316d73 | -1.092 | -53.3954 | 2024-11-29 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| dd9b91fc-1822-33a1-9b66-85c145032aed | -2.6499 | -48.7772 | 2024-11-29 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 6a6d8500-60e1-3170-84a2-06f091cb0245 | -4.4405 | -46.5754 | 2024-11-29 03:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| d6d0fa98-5a16-3c7d-bc59-640d1b8f0999 | -2.966 | -53.3027 | 2024-11-29 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ef68b964-0905-3ef3-bbbb-8730c928ca2a | -2.6684 | -48.7767 | 2024-11-29 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 210.7 |
| 78e6c89c-ec7a-3d70-8965-9b47c1f7d932 | -2.6498 | -48.7986 | 2024-11-29 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 39ba058b-a7ae-3140-94a6-ff5d853b12b1 | -2.9844 | -53.2819 | 2024-11-29 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 246.9 |
| 3a9d3bfa-c979-32b2-bc3c-1bc23d606355 | -2.3233 | -46.8786 | 2024-11-29 03:40:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 85571eed-32ee-3cfb-b908-d21b6527259a | -1.6081 | -52.2912 | 2024-11-29 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| fc07b6b9-352d-3d4a-9f48-5c96433ab441 | -1.5897 | -52.2915 | 2024-11-29 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 49f3e3cf-cd6b-3ded-8904-c3d85b54ae48 | -17.5805 | -42.7483 | 2024-11-29 03:40:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 76ecf81d-afe6-3cd1-a795-91b3e6ddb7f2 | -2.9844 | -53.3022 | 2024-11-29 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 180.4 |
| 8f8cbdbe-44d6-3d52-9133-d51b9cd98c37 | -2.3419 | -46.8562 | 2024-11-29 03:40:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 38558ed7-d664-3505-9503-ac48a09a1674 | -4.2225 | -45.7634 | 2024-11-29 03:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 83198973-8fbe-3c24-bc36-82d98278e661 | -2.6683 | -48.7981 | 2024-11-29 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 201.7 |
| 4928f7af-390b-3728-9752-a7c8c81385af | -2.87434 | -46.86877 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2a82404-74e8-3ab2-84fc-48bdee414ffd | -4.43238 | -46.5813 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 4d51e89e-e595-39b9-a4f0-102db9dbcbb9 | -4.43076 | -46.58588 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 957817e6-a225-3a20-a0ca-00665a7d2455 | -2.86571 | -45.54634 | 2024-11-29 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 689f2054-5595-30a5-a0ee-09b14c7fdea0 | -3.19795 | -46.56819 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 04fd9cc3-2f7c-3058-af4f-2eea8a9576a7 | -5.88974 | -35.42595 | 2024-11-29 03:40:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 59ec7943-4e18-3650-a45a-1cf12bb69585 | -4.01579 | -45.96459 | 2024-11-29 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 902e46b9-8e0c-3917-af40-2e04eddb711d | -3.81149 | -44.04606 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5e680bb-e6b9-3306-a44c-4dcd12b12d6c | -1.67815 | -45.79979 | 2024-11-29 03:40:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59bb9e39-9492-30fa-bc0f-789a4e9d7fd6 | -2.32975 | -46.8699 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 921ce46d-0e58-3da1-86c2-1187fecb9c88 | -4.8425 | -41.26144 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ebae8053-9317-324f-812d-b98dc7a6b127 | -3.82424 | -44.03728 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48926fed-06af-386d-afdf-cd59202ed683 | -4.43879 | -46.58229 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 10085c1c-4f88-3722-8290-bd75e937b5a5 | -3.81698 | -44.04701 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c276120-b1f1-394b-b2bf-1d11feeec565 | -2.85361 | -46.82973 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5cef4793-5a84-3321-8922-dcdf258f5a31 | -1.96313 | -46.44299 | 2024-11-29 03:40:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 406bc62f-f2ff-3d5d-95d1-2ac859ce4d10 | -3.08934 | -41.14627 | 2024-11-29 03:40:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e4689cc1-7336-30e6-b254-7340b0b291db | -3.16917 | -46.30499 | 2024-11-29 03:40:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3a88a59-1329-30f8-8f4e-3bc319e8c843 | -5.14792 | -37.7432 | 2024-11-29 03:40:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44f15091-7d50-39b4-8b65-2c362edfb70b | -4.85668 | -41.25903 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3f8dcf8d-14fb-3cfb-b8fe-5efdf414e522 | -4.66662 | -42.38081 | 2024-11-29 03:40:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e2ed3d66-5dee-3220-aba9-df0eb98362e4 | -4.90995 | -44.02583 | 2024-11-29 03:40:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04cbac09-2014-35b4-aa32-92be63f96cd4 | -4.26255 | -40.70279 | 2024-11-29 03:40:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0834c436-7b19-3a5d-b77f-6bce7bdd39a3 | -3.17647 | -46.30088 | 2024-11-29 03:40:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2afc7c8b-1744-3be5-a4d5-b8557913446b | -2.84131 | -46.82176 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 035ea4ea-bbbc-3b51-b09e-cf621af71805 | -4.01662 | -45.95992 | 2024-11-29 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a738e06d-1163-3c6c-bdd3-63b6e0d6f7fd | -5.15686 | -39.36689 | 2024-11-29 03:40:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a851c2fa-0ec5-302f-9c40-7af52837d81b | -4.6427 | -42.40415 | 2024-11-29 03:40:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b48a8a14-37cf-3adf-9d9f-dad22013bf41 | -4.41464 | -43.75638 | 2024-11-29 03:40:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48c2a1d0-73f5-3465-9ea9-474f03d9cab2 | -4.23191 | -45.7718 | 2024-11-29 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 6728c7c5-81e7-3a98-a4a2-759adb61a305 | -2.86729 | -45.53699 | 2024-11-29 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f89a9374-0b60-3876-89f3-b337d11b344b | -4.2689 | -42.60815 | 2024-11-29 03:40:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3facaad6-85f5-37a5-b5f3-595521cdf6e7 | -2.8542 | -45.53967 | 2024-11-29 03:40:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 142262ff-d30d-3b20-86cb-d5e2b9c99638 | -4.22664 | -45.76598 | 2024-11-29 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bcc04d85-3e9f-31ba-ad79-6c77805f0f1e | -4.07502 | -47.03235 | 2024-11-29 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c69a107-acd7-3c75-9c5c-38922f6139c4 | -4.98691 | -41.31624 | 2024-11-29 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11cdeed1-a1d0-3a1f-aa31-dfde3ce9ea45 | -4.07603 | -47.02642 | 2024-11-29 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29393e10-38ea-360f-9a41-8f5e362238a4 | -4.42983 | -46.59128 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1e2655a6-40cd-31fb-a334-af3d7c28dd7e | -4.9147 | -44.03043 | 2024-11-29 03:40:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8acf2bd2-3005-37c1-8949-70eaaa3e9652 | -3.806 | -44.04512 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b24f3204-0931-38e9-a59b-4ab4410b5d69 | -4.43143 | -46.58653 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 8e4fd186-f1b7-3d88-ba32-ab1f9ef87bf1 | -4.50848 | -42.07326 | 2024-11-29 03:40:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a3fa851e-79d8-3040-afa1-2fc9b3d096d0 | -4.43718 | -46.58685 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 3d19788c-2264-3050-976b-dd1800a6482f | -2.83329 | -48.09327 | 2024-11-29 03:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 51294ad6-8972-31b1-a1d5-f4d0018ca3af | -5.89252 | -35.42995 | 2024-11-29 03:40:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f22222f3-8124-3ff9-8ae7-4887a93e6544 | -5.5631 | -35.52456 | 2024-11-29 03:40:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1bb79a79-cd88-3127-a9cc-30e0aee2a148 | -3.00405 | -40.23011 | 2024-11-29 03:40:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 325cfdc7-f6c1-331e-a423-207ebda58fce | -2.63955 | -47.12747 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49074d46-ccfa-382e-aaef-4c6bd697cb48 | -2.96173 | -45.234 | 2024-11-29 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14d596b1-3078-30d8-a536-aa503dbb96f3 | -3.8109 | -44.04963 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fde1d42-a040-38d6-95d6-d3d61cd9ff6c | -3.9642 | -48.09167 | 2024-11-29 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6dea076-0b36-3b68-b8b4-aa7ccf22776c | -4.79238 | -43.7817 | 2024-11-29 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8aedccb4-3de9-359a-a30d-c339f7f2311d | -4.92928 | -43.03483 | 2024-11-29 03:40:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbadd04c-177e-3d8c-b70e-b9b48d3103ba | -1.9622 | -46.44855 | 2024-11-29 03:40:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| bf0d41b1-9b6a-39dc-a349-421c3ce4e18f | -3.17559 | -46.30606 | 2024-11-29 03:40:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb6641b4-abdd-3f9c-8246-bcc8b36febe7 | -2.33075 | -46.86397 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 07b671b1-df02-3a94-abd9-96a12e4551cf | -2.8665 | -45.54165 | 2024-11-29 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b18d7091-9815-392e-9ef9-4d619637c3eb | -2.85458 | -46.8241 | 2024-11-29 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8dd8e67e-ceae-3d90-928f-0966193fc6b6 | -4.14812 | -43.81899 | 2024-11-29 03:40:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8327c0a3-904c-397b-9387-398e29363234 | -2.33549 | -46.87682 | 2024-11-29 03:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 10dc9089-d70a-38b7-9c7d-bf77bee7e2a6 | -3.82339 | -44.03974 | 2024-11-29 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b74e8c3a-7455-3379-b332-8baadd198cc5 | -4.26184 | -40.70042 | 2024-11-29 03:40:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c08b3c15-e088-3654-a1f4-de31eb29daf6 | -4.67146 | -42.38163 | 2024-11-29 03:40:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 2edd19d0-2b93-3673-94ed-3470c1d3b89e | -3.19885 | -46.56274 | 2024-11-29 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ec6432d8-bc37-39c6-90ca-0a530170de71 | -4.43785 | -46.58749 | 2024-11-29 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |


[Clique aqui para ver as próximas entradas](README18.md)
