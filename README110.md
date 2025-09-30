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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f19c6114-69cf-3761-8e7e-8ac9ae167166 | -11.1735 | -54.1242 | 2025-09-30 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 73ee2ec4-d2a1-3613-99db-ae981815cec9 | -14.6798 | -46.963 | 2025-09-30 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 2abfc99c-b152-3a3a-9131-4d8ef214dee5 | -12.877 | -45.1974 | 2025-09-30 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 6e9a0960-b130-389d-a7d6-871a8fb72279 | -8.6668 | -46.608 | 2025-09-30 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 4342b2ca-6a81-361d-8777-79778fa3f0d4 | -18.2176 | -53.3177 | 2025-09-30 12:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 102.4 |
| e53df0aa-6859-394d-8d48-ab84c94cd6a8 | -12.2348 | -47.7863 | 2025-09-30 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a4679072-0a4e-35e9-9e83-7c350263055d | -20.6818 | -50.2054 | 2025-09-30 12:50:00 | GOES-19 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.6 |
| 5811a15e-68f4-3cd1-9eaa-3cf4ad761189 | -17.921 | -57.5952 | 2025-09-30 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 08a6217f-01da-30ee-94bf-dbe0f90dbf39 | -10.3058 | -48.2681 | 2025-09-30 12:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a861f35a-3b06-3472-9f63-ddbc25d08caa | -12.7022 | -45.2715 | 2025-09-30 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| efe2dbee-9b2c-37d0-af85-7eb310eace03 | -18.2176 | -53.3177 | 2025-09-30 12:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 107.1 |
| f6ae9784-1cbe-3b3f-b2f0-64794bea6fe4 | -11.1735 | -54.1242 | 2025-09-30 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 721754ab-3320-373a-ae5f-724272bb3a84 | -14.5141 | -48.4299 | 2025-09-30 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 0252f2c7-a41e-34d4-a932-281b718809b4 | -12.9712 | -48.4158 | 2025-09-30 12:50:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| bec3cb59-efff-3332-86b9-eb4594c6b877 | -14.5517 | -48.4907 | 2025-09-30 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| cdffec73-793f-32be-a5b9-3677729a6e5a | -11.1944 | -47.2334 | 2025-09-30 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c5aebd5d-e809-3635-9290-de32b3eadbba | -15.2654 | -49.7273 | 2025-09-30 12:50:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 4f728b66-94b7-3c19-8d28-921964c834ad | -7.8353 | -46.9764 | 2025-09-30 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a752fc2e-0b8c-31bf-b668-09b324d37434 | -11.6837 | -45.3563 | 2025-09-30 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5b227f9a-9cac-3d1e-b1ac-eb2393302ce3 | -7.8348 | -47.0207 | 2025-09-30 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 13bcb737-0fd1-399d-baf5-ed67335d9b9e | -13.4005 | -48.0657 | 2025-09-30 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4a06819e-094a-33b5-8288-5c4f106fd9ba | -10.1045 | -47.7851 | 2025-09-30 12:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c0eb85d4-6851-31f9-837f-daf2c486386f | -15.9268 | -46.2334 | 2025-09-30 12:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 5b2dc053-24fe-3938-834b-2b9f07526575 | -9.1248 | -47.6256 | 2025-09-30 12:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 30fdbc8d-15ea-3c3d-9737-fe45958e2f30 | -14.5964 | -48.1938 | 2025-09-30 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0c056498-1daa-3bfd-9ddc-5b28799d073c | -10.9586 | -46.5016 | 2025-09-30 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 37bcafab-ee48-3bfd-8045-cf710505e4f6 | -7.5146 | -45.4385 | 2025-09-30 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 7da95a38-a918-3ac7-b6a5-a2ad65668928 | -7.9191 | -44.6245 | 2025-09-30 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 46d335f8-ea1e-37f2-9d69-429f70a428b6 | -10.1851 | -44.8939 | 2025-09-30 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 25182083-a99c-359c-bd44-8cd4720e2687 | -15.9273 | -46.2101 | 2025-09-30 12:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 142.4 |
| ed25b08d-595a-3bc5-92b4-7308fa792821 | -7.8188 | -46.7783 | 2025-09-30 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5688dcd9-72ec-3ba1-b830-1a54919b81e8 | -15.2459 | -49.7303 | 2025-09-30 12:50:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c8f0adde-6f63-3f40-8d18-b4665eca4957 | -9.4007 | -54.6984 | 2025-09-30 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 20aef6a3-519c-32ad-a9df-dc2e282bca60 | -12.877 | -45.1974 | 2025-09-30 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| ca6b1e81-733a-3d8e-a245-5c04249ff4ab | -12.952 | -48.4185 | 2025-09-30 12:50:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 0bcdabfa-dd11-32f1-8464-d7e7c6da3085 | -6.7999 | -43.808 | 2025-09-30 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 8e5f36f7-aca4-38b2-a035-8a78b76c0535 | -10.8242 | -45.3841 | 2025-09-30 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 8574cb6e-c442-3311-bd1a-15f450a8c5ff | -10.8246 | -45.3611 | 2025-09-30 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b0b23acf-2d41-33ab-bd4d-b1a7d268121a | -7.8696 | -47.2606 | 2025-09-30 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 9ee0265e-6fff-3340-a391-fa9fc11c8bc3 | -8.2474 | -45.5037 | 2025-09-30 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| f0dc1f32-8d50-303d-b82d-e19f2daafc07 | -12.9524 | -48.3963 | 2025-09-30 12:50:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 1c926746-cf6e-3591-952a-7645c802a3f9 | -8.541 | -44.6515 | 2025-09-30 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 5b253ae8-239b-311f-b647-b1a2ff7397a2 | -7.835 | -46.9986 | 2025-09-30 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 231.9 |
| 8bb5b62f-fb98-327e-a291-233986e9fcae | -7.8378 | -46.7544 | 2025-09-30 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 358b6fd3-4012-3aea-b4c1-8bd9fafd1017 | -14.5323 | -48.4938 | 2025-09-30 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 71ba08c9-be35-3548-9461-b2889431fba4 | -8.8229 | -46.189 | 2025-09-30 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 536e2693-4f77-3576-a65e-67baf2ed0821 | -11.1546 | -54.126 | 2025-09-30 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 75bb624d-5298-33c2-82de-97a99e2ff580 | -7.0103 | -45.2116 | 2025-09-30 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 1f62050a-e978-3d20-902c-2dfa016958bb | -6.523 | -45.207 | 2025-09-30 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| a7da0659-c933-301d-8191-d6b0a983b7d5 | -16.7575 | -51.3482 | 2025-09-30 12:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 234.0 |
| e9404a17-f7f3-3345-8819-57f2872b8d15 | -8.2285 | -45.5056 | 2025-09-30 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| ce0d8771-80cb-36e6-968f-c0fad2dea9ca | -11.2707 | -47.2236 | 2025-09-30 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 1edaa9d7-bd90-32ff-833d-46f95f0b97ca | -12.2344 | -47.8086 | 2025-09-30 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 863ed599-ab3a-35a4-9173-e8520266fe04 | -6.5227 | -45.2297 | 2025-09-30 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 086dda94-00ca-3f95-83b1-a197dd7f686a | -12.8774 | -45.1742 | 2025-09-30 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 4d360e1b-1da7-32d5-b4fd-308392f366d0 | -3.50692 | -52.45971 | 2025-09-30 12:55:00 | TERRA_M-T | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 26f61dac-672a-376a-9bde-fb445252098f | -2.92336 | -48.71806 | 2025-09-30 12:55:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| efdd0f29-4a33-3ae4-8ab8-2503d56d57cd | -2.07133 | -56.88188 | 2025-09-30 12:55:00 | TERRA_M-T | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fbe010bc-9a0c-3c35-90ea-84dee1e10b46 | -2.24367 | -47.8835 | 2025-09-30 12:55:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 57d7d4f6-5a8d-33fc-ab4f-c8cb61090cbc | -1.28763 | -54.18409 | 2025-09-30 12:55:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ee0b3959-dfb1-3d7e-a8c0-363c4eb87323 | -2.68855 | -54.76773 | 2025-09-30 12:55:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c0a0dd68-9ca0-312f-9929-ac02a7302563 | -1.95118 | -54.05748 | 2025-09-30 12:55:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ffc83857-9dd3-3e1d-8539-8b32902c2e9e | -2.07264 | -56.87288 | 2025-09-30 12:55:00 | TERRA_M-T | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 191537dd-3904-370f-ae89-a7d0834337c1 | -1.94981 | -54.06707 | 2025-09-30 12:55:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| af016e45-ab13-34e1-8545-00432d7b9fe4 | -5.85463 | -50.0647 | 2025-09-30 12:57:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e10917c9-70c7-36e0-8031-c4747f8cf569 | -11.88769 | -48.04913 | 2025-09-30 12:57:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f4e5a67a-5756-335d-8ee4-9b6f52545ee0 | -6.58039 | -51.69825 | 2025-09-30 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 2aa2c080-f70a-3928-8a28-3123f054d8e4 | -8.22658 | -49.40215 | 2025-09-30 12:57:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 0f0566bc-64f4-379a-9be1-3a4b2ee511f4 | -6.57831 | -51.714 | 2025-09-30 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 53214bc6-1a67-3cff-a40d-856d1c174c9c | -10.64311 | -48.5999 | 2025-09-30 12:57:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| a85cfcc5-a6d3-3dff-aabb-ca1fc30fb5d4 | -9.13255 | -47.62929 | 2025-09-30 12:57:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 1759ca34-61db-3763-b082-3a3b44031975 | -9.44098 | -54.56733 | 2025-09-30 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 8f9cd3f1-457c-331c-b2bf-b714da4aac9d | -9.43951 | -54.57812 | 2025-09-30 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 02a63044-ca9e-3941-830c-43d50ecfa251 | -7.82072 | -46.75723 | 2025-09-30 12:57:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 9079609d-69bb-3ff4-b84e-9df5447f8363 | -8.85608 | -51.71289 | 2025-09-30 12:57:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 39e4392f-7e83-3e32-9a86-5300cde281ea | -11.02581 | -55.01288 | 2025-09-30 12:57:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bbfd2e8c-9ca5-3d65-aab1-57d4a63c93f9 | -11.17735 | -47.23623 | 2025-09-30 12:57:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 4b6a65a2-f142-3925-9327-8a5d30cf028c | -11.27015 | -47.21009 | 2025-09-30 12:57:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 98e7e870-5166-3963-b22d-93920e399ad6 | -11.8828 | -48.04343 | 2025-09-30 12:57:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d133542e-1238-3dca-96a7-c97f99b9bf66 | -9.06077 | -47.61427 | 2025-09-30 12:57:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| fe95cc51-570f-3b59-97c1-a7f231f8d67d | -6.43413 | -51.84736 | 2025-09-30 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| c92fa837-9d94-32d7-87d1-b6fe382abefe | -9.05526 | -47.60815 | 2025-09-30 12:57:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 2174ea6d-4a1e-359f-a132-57f656f0a72c | -7.84406 | -47.00116 | 2025-09-30 12:57:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 208.4 |
| f0dc409a-743d-30d0-ad4a-5283970593ec | -7.83466 | -46.96586 | 2025-09-30 12:57:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| c7678de5-7297-31a4-92c6-9c4d51eba0a2 | -11.30817 | -53.9542 | 2025-09-30 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 774068cf-0d2a-3101-b6e9-8d80720c87ce | -11.37714 | -54.83731 | 2025-09-30 12:57:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c7a8130f-2a01-37eb-ad6c-caaf451814c4 | -10.51463 | -53.49762 | 2025-09-30 12:57:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c3e51016-43af-3987-8e4f-c42ff432197f | -10.39064 | -48.14903 | 2025-09-30 12:57:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 2febcef2-e588-3c56-9265-ac77068353f8 | -7.81959 | -46.75026 | 2025-09-30 12:57:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 687674b5-c2d4-3990-a114-22c26e3309d2 | -7.84737 | -47.00649 | 2025-09-30 12:57:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 3c6f87fb-3941-3211-8fba-29cfd74d0d87 | -6.61413 | -48.60813 | 2025-09-30 12:57:00 | TERRA_M-T | ARAGUANÃ | TOCANTINS | Brasil | 1702158 | 17 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 6a95da61-eca5-321c-a7cd-e26bbaf8c96b | -9.51036 | -54.66036 | 2025-09-30 12:57:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2c17dcea-c39f-3193-b8de-c4acf27f1aea | -9.27245 | -57.14814 | 2025-09-30 12:57:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7d01f0af-18b5-32dc-9fb8-f93f23f4f839 | -10.82268 | -47.97115 | 2025-09-30 12:57:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| a26c61fa-5cff-3efb-b5e5-6ef68b5e20d2 | -8.85825 | -51.69578 | 2025-09-30 12:57:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| c4390e18-af24-34a3-b2b3-a530bc95127e | -10.45972 | -54.43935 | 2025-09-30 12:57:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f813e111-0849-37ee-863e-72cc2de9514f | -11.29347 | -55.00007 | 2025-09-30 12:57:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d6e72422-0aa0-3141-8462-91ee9552abc3 | -11.20682 | -55.91507 | 2025-09-30 12:57:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 82bc3838-abf8-306a-9c62-53df857f3c4a | -11.7828 | -54.23822 | 2025-09-30 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| e9cf4fd1-75da-3499-b053-558acede86b8 | -6.51542 | -54.88087 | 2025-09-30 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |


[Clique aqui para ver as próximas entradas](README111.md)
