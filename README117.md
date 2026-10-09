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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54595fb5-43e7-3939-a8a8-730dc519f891 | -14.43196 | -43.93015 | 2026-10-09 04:27:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e424c9b0-8de1-37c9-b5ea-52ff8f4c635b | -13.17102 | -54.35376 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 712e7f9e-aa6b-346e-bcef-d3e529352505 | -11.60232 | -43.713 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2ee5791-ddae-3bd6-9344-589e864c78dd | -8.32505 | -45.44684 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4207be51-af61-33ab-a326-a62c130af34e | -6.92913 | -59.26062 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e2d72d0-ba10-3ba4-996b-b5d7f60dade7 | -6.52951 | -55.26006 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cf33b6e-2b05-3211-9469-232ab41a5eae | -10.42238 | -47.28761 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1616ab6-1e04-309e-a520-7245b10d49a0 | -7.404 | -44.76137 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f0ed94b-8396-3999-9a9e-16e6b61fe7ce | -12.23455 | -57.10747 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 27528e7e-b93f-3bf7-91fd-2d39c28135fd | -14.1778 | -48.66288 | 2026-10-09 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10d8d434-9109-316e-8b27-9e8fb8d679a1 | -6.49074 | -55.29859 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 047c2660-915c-329c-be68-4ab2e2b09c06 | -13.15956 | -54.34284 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ba95331-24cd-3f44-b11f-c887859428a1 | -7.23708 | -46.00332 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 205a7459-d6a1-3491-9014-6fddd9a36808 | -11.07361 | -44.08396 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01c6bb89-d844-349d-a29e-12b924f9f11f | -11.78724 | -45.59304 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5ce6ed4-35d8-372b-8899-4f7a4be47575 | -10.30858 | -46.59639 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbd3b3fa-f093-3fa3-8f5f-c7185fd53d57 | -6.41727 | -55.19324 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d91092f9-ad26-3604-9609-b6f4162b93ab | -6.38741 | -56.2253 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5edbe418-e6c9-3e45-b8b1-2c2bbe0fdf28 | -12.2159 | -57.09622 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 121dbd94-14f3-3a96-a8cd-dd978fdac46c | -12.22333 | -57.10878 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 34f0f9c7-9423-34b5-b2ec-2564fe48638b | -10.85114 | -59.11713 | 2026-10-09 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19d7705d-c6b6-3cc9-b6ca-86c92f3d8b3e | -5.98282 | -55.35637 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec15cc09-5231-35eb-8959-48e67ffb5781 | -8.17524 | -54.72586 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 431fae8b-755e-3425-b7d8-4567e2fac832 | -6.49535 | -55.30265 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d0d7d8b-2979-340f-808b-723f3d1cab78 | -10.57954 | -46.29383 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39a0dc1b-2687-37c3-923d-d2a40a4447b5 | -11.61362 | -43.71432 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c3c2a186-baca-3caa-8362-862de91a2bd0 | -12.23519 | -57.10415 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cd311a85-051c-3d24-82c3-1f75a27004bd | -13.17923 | -54.30744 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c316351f-5144-3b7a-8960-7302d793ce98 | -7.79627 | -44.5766 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72843bf6-31c6-3bb7-a112-aeab4b370d1d | -11.74978 | -61.05938 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e0f7fc01-c04c-33f0-8184-00d205d4c22e | -12.20308 | -57.1352 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09b46bd3-ab89-35e7-ae05-8e71888b92e3 | -8.22226 | -46.38601 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c42b5508-4d98-3df4-8ded-d041b19bda67 | -5.95202 | -55.34723 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79efb6e3-8b01-3606-bccd-a50e1dd06c80 | -14.17449 | -48.66233 | 2026-10-09 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ff0d89d-e34c-3ef8-ab4a-33166837fe99 | -7.07411 | -47.39601 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6353441-ff24-37c8-8b5b-97fed0c506d5 | -5.85689 | -53.45785 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3fcdd08b-c03d-3b86-a036-f8c5dc8fe442 | -6.51696 | -51.12137 | 2026-10-09 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98d2de28-484c-3d02-872e-9d89e7c915ab | -13.16404 | -54.35129 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7203f29b-64fa-3b67-a28f-e1123e378659 | -7.18255 | -52.61368 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bfd38ee-4372-35a0-9a9d-9723ef75f375 | -8.78971 | -47.58924 | 2026-10-09 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a599cf41-6b47-3cfd-9fb6-478464e22146 | -6.11613 | -55.70418 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a4686cb-eb8b-3460-9992-23d9db7dac7d | -7.48971 | -42.79253 | 2026-10-09 04:27:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c98a822-d035-3c4a-b719-d6e6b8ec0f1d | -12.21284 | -57.13441 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7678bb7a-5b43-37b3-a5e7-68b3f2b507b4 | -10.27943 | -47.83284 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eeebb946-48f9-353f-941e-07dcfddb095c | -6.44367 | -55.04344 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d47dffe-41bc-39af-b7f5-470d847469ce | -8.93184 | -45.14178 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 578bc7e6-f123-3345-bf35-e6098d04497a | -11.75013 | -61.06672 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| de3b574c-7af3-3073-b1fc-9f868dd30d9b | -8.99016 | -45.9051 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3188e41-3ed8-3858-b078-3a84db22698b | -6.48962 | -55.30484 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 431f3e22-6578-36bf-b6d6-d2129f0f3806 | -6.51438 | -55.40725 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1196f885-bfcf-3138-85fc-a585c1933f29 | -7.81519 | -49.22254 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed9019f3-4e13-39fa-aa76-bb66f4e09bf9 | -7.51174 | -45.7667 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0c53db0-c841-395a-a4e6-b83bc9535f15 | -13.15674 | -54.3336 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c22fe235-ae27-3e01-b593-c0050133887e | -9.58439 | -46.83693 | 2026-10-09 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a42c860-5fdb-3830-80a7-fe16f2144d5c | -12.84527 | -50.58406 | 2026-10-09 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a30835b1-cd43-3db5-88dc-d2fe2b5959af | -13.20221 | -54.36268 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02a2a1da-2892-34ea-a423-7582550eddc4 | -10.50596 | -47.34078 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18676fd5-bfde-38ac-a6eb-3f97c774e818 | -12.20961 | -57.12966 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 572d38de-8cd4-3129-872e-ed1ab7c78965 | -7.09505 | -47.73493 | 2026-10-09 04:27:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e5c2e64-c701-3c83-a9ea-5277b98ff688 | -14.08275 | -43.78124 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f25de796-4caa-3276-a5ed-ab7fe45df5e9 | -11.6117 | -43.70755 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1fd0eef9-6e25-3779-836d-69e3c9925323 | -7.25426 | -48.06644 | 2026-10-09 04:27:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba5676f9-2b59-3994-9215-00637a4af1d0 | -12.22267 | -57.11216 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 01395f3b-393c-3dc1-bb56-83c9a25e6e24 | -9.3019 | -47.42512 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6077a69d-a834-3bbd-a934-67596745d8c9 | -8.49181 | -54.63544 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be357b95-f69d-3b97-b7fb-a288cc570009 | -13.16105 | -54.33442 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c78db973-2169-3c9f-a76b-f8399fe4175e | -6.47845 | -53.68371 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 348a51d5-42f4-3a7e-8d68-e7f2547a694e | -5.88796 | -57.72425 | 2026-10-09 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afe07f49-535a-39f8-8c11-5f8514dcb594 | -12.01974 | -43.44159 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 934c1090-a081-389e-9385-d62dc744bc04 | -8.97337 | -45.16702 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f2b1e08b-d6c4-3130-ad79-1bea8bb8323b | -5.86164 | -53.45782 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd7d93f3-ef38-3cdc-89ea-d77a62b03908 | -5.94732 | -55.34327 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89358b41-7447-33c3-bab8-538429004971 | -12.8176 | -44.6426 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3469a7fa-04e5-3a5f-bb40-39735a9badc4 | -8.96993 | -45.14369 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 818f9c85-b35d-3228-bc80-e9c39bd70793 | -6.38656 | -55.26733 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c121c6f-ac0f-3966-b56e-3086fe8de018 | -11.78695 | -46.79984 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 279fad9b-ec29-3dca-a1b6-cf1e3816383d | -6.31744 | -55.32734 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20f37240-e978-33a4-a157-0c5506655096 | -11.38683 | -55.09509 | 2026-10-09 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a60fd7e-06cb-3a01-b665-841ee11b383e | -7.39043 | -55.19978 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e9792d5-e214-313f-a8b9-7a0dd39d23b5 | -7.29005 | -45.41713 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0c33f27-fa81-3c32-902f-13b2bf9d55b9 | -12.22648 | -57.09816 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 271.4 |
| 586009b5-fddd-310b-823a-a26a49eb7062 | -6.45656 | -55.49029 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2694e172-9101-33b6-a86d-d843eadcb266 | -7.47477 | -42.84168 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 792bcbd3-1268-3591-9192-149b989af427 | -9.93739 | -43.56303 | 2026-10-09 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64d4edc0-df69-32a9-8920-660947a0c539 | -7.51561 | -45.76369 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae4a6351-5425-3261-9d6e-4275ea1a7ec3 | -8.97391 | -45.14043 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 420989db-ddcd-38a4-a1aa-d35fbfcf7d13 | -10.85191 | -48.13074 | 2026-10-09 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf76b373-d502-36a9-a039-81cb8ab8ed75 | -12.2253 | -57.09871 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 343e0639-ee2c-3529-9e45-6805e1f78a86 | -7.26636 | -45.34781 | 2026-10-09 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14d43b2d-600e-3eca-a4de-c679b8c448cc | -5.21677 | -60.04793 | 2026-10-09 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 546e2c77-0e94-3be9-9f94-a3ea22fd4751 | -10.91084 | -45.5248 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2660805f-9019-3abd-a375-9de7a7ed0c01 | -11.60985 | -43.71387 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d55a731b-31b9-38f2-bfbf-5f5bb8628e85 | -13.85155 | -42.64955 | 2026-10-09 04:27:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02a11bb9-f6b2-346b-a83f-01349ed60dcb | -11.74881 | -61.073 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| edefdf28-b414-3581-9d33-12b79a355887 | -8.79264 | -47.26491 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0da67d4-d930-33ed-8029-dcf8b42eb98d | -8.13198 | -49.44803 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9084e941-6904-3471-8d55-b1e6f39d1f2b | -12.20774 | -57.13958 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a64e8952-fc27-3343-8349-d27a0b3c1c5e | -9.12115 | -48.81599 | 2026-10-09 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 070bf2e3-3ec3-3a24-851b-83bfe3c4ab58 | -6.38676 | -56.22897 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 925b5a0b-f747-3213-8f80-3135825fad37 | -10.00705 | -48.57963 | 2026-10-09 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README118.md)
