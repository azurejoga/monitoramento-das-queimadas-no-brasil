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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6ef5a36-c706-3761-86de-cdd6011f12de | -25.90461 | -52.14027 | 2026-09-27 04:57:00 | NOAA-21 | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 285f1ad0-d1f5-38e8-83b4-095b25774b33 | -31.87193 | -53.32721 | 2026-09-27 04:59:00 | NOAA-21 | HERVAL | RIO GRANDE DO SUL | Brasil | 4307104 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 0bac4434-dbef-3ca7-b852-856cd9dde36e | 2.89097 | -60.27752 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3444620b-2fc0-3308-8af1-c1d080e8aebb | 0.69548 | -51.43325 | 2026-09-27 05:25:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 06503e75-f386-3fb7-873e-bf0bcbb91f26 | 0.69977 | -51.43255 | 2026-09-27 05:25:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2efc3740-4e67-3e02-99bd-c5c84672bb46 | 1.65366 | -55.94002 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e5531b5-c7b3-31a8-8b52-d396d70e1d06 | 2.64343 | -60.17301 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e1ed35b-6b59-38d6-8fdd-b92081455500 | 2.89465 | -60.27695 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 628e122d-70f9-3fbf-b2e8-c57fa2513661 | 2.63911 | -60.16934 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b47d3fc6-84e2-30d9-9491-adbb83b070fd | 1.65141 | -55.92585 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3eae534c-47d3-3542-9117-afeb310525fe | 0.70042 | -51.43659 | 2026-09-27 05:25:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61108e6a-71e0-373f-b6e4-c5659aa62aa8 | 2.89834 | -60.27639 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c568d6a-34ef-3ef6-b159-873a7e1484db | 0.32894 | -51.44229 | 2026-09-27 05:25:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d421cb7-a489-3995-9345-948c81e4a60f | 1.14336 | -51.17285 | 2026-09-27 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df1257ab-27b6-3af3-900d-31d1de6ea388 | 0.32828 | -51.43822 | 2026-09-27 05:25:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b87f0bb-dd5e-31dc-b1f5-2cf8608ced18 | 0.33242 | -51.44451 | 2026-09-27 05:25:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2efe5771-5f80-3b30-8f5d-d83ee9564e0e | 2.63546 | -60.1699 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1f44e63-31d9-370b-99a5-2c623a83d0b2 | 1.96974 | -50.8987 | 2026-09-27 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 211db158-b12e-306f-a1e0-ebb3d826b1c3 | 1.65646 | -55.93595 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db100b95-492c-351a-949a-308f6c813987 | 1.96607 | -50.90356 | 2026-09-27 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cf0df0d-e081-3c35-bcf5-557059ea3468 | 0.32747 | -51.4411 | 2026-09-27 05:25:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c356120-c578-3bda-8060-c2b4bdc9d1ce | 2.64774 | -60.17668 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05b118e8-e012-36ee-bca0-c78270dbdf52 | 2.63845 | -60.1651 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ece2527-27dd-37e5-b746-136af0296cc9 | 1.14674 | -51.17047 | 2026-09-27 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56e43478-5fba-37ee-bd99-52f2db1f6a0a | 2.63115 | -60.16623 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99b00de1-8785-353e-bd9f-0a08754650bb | 0.32684 | -51.43702 | 2026-09-27 05:25:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbe6a535-e7eb-391f-967d-fecba4bbf6b9 | 1.6531 | -55.93648 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6289c95e-2b4f-3317-8368-59b144ce05c5 | 1.65197 | -55.9294 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ac1364e-845a-34af-9adb-cd478f147272 | 1.1424 | -51.17117 | 2026-09-27 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7fc64f0-4d76-3fcd-98cf-3b5edcd1d926 | 0.32961 | -51.44637 | 2026-09-27 05:25:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 875d4818-d68d-30fa-afa1-9981f7a14804 | 1.65254 | -55.93293 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 468c72dc-3c1c-3e99-acf7-11f33e9a2b59 | 2.6348 | -60.16567 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3aab16d7-1634-3a32-9007-7e7579c4d063 | 4.22746 | -59.86411 | 2026-09-27 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36f62d64-fc7a-3731-888c-ca5963152854 | 1.96635 | -50.90582 | 2026-09-27 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57d7f3bb-bb91-319d-909a-e2d3d17d4e3d | 1.33426 | -50.9955 | 2026-09-27 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c9ccc7b-3f08-3c9f-9246-0e11143cd331 | 2.94086 | -60.31578 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70041a3a-0995-35c1-8a43-d843a965f018 | 0.48644 | -50.94563 | 2026-09-27 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a041b2af-9e3c-3045-8161-1a14c2657274 | 2.36229 | -50.77062 | 2026-09-27 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0312667d-2239-378f-ba36-a4f46fdaa979 | 1.96171 | -50.90426 | 2026-09-27 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 086975bb-606d-3cda-a070-36547c6ab3fb | 1.69269 | -50.87839 | 2026-09-27 05:25:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c9fa4b0-27d7-3086-a921-86a490a60710 | 0.49089 | -50.94494 | 2026-09-27 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ead3b7e-645f-31c6-8d63-6f3309091d96 | 1.88295 | -50.66645 | 2026-09-27 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b95039f-3b24-32b9-b782-316425ad5c35 | 4.32464 | -60.82516 | 2026-09-27 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1393fc8-ea26-31bb-bbbd-6b1b8e2a8310 | 2.26365 | -50.77296 | 2026-09-27 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 807fc262-077e-31e2-8e8d-7b8d6c315e9f | 0.48269 | -50.95068 | 2026-09-27 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac560e6c-d66f-3cd3-ae3d-33a7b33fcedd | 1.6559 | -55.9324 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3efaf11-8530-3221-a351-3533db7c6550 | 4.47329 | -60.35538 | 2026-09-27 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5620963-b129-39b9-b3a8-a2074c64c9c3 | 2.69024 | -60.16291 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ea8a220-fe38-3a8d-bff4-45cda56ae6de | 1.64635 | -55.91573 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6eb6d481-8a4b-36a4-bc9c-f8d4629c1758 | 1.96199 | -50.90652 | 2026-09-27 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a6e72dc-ce4c-31ce-a868-b312c0425148 | 1.64805 | -55.92637 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a07c244a-afa3-3807-9427-faf23166110d | 1.64692 | -55.91928 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3a4d4cf-b073-33e7-b7e9-42c774c70067 | 2.64409 | -60.17725 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58154ac0-a2a4-3eb3-b8cf-203e72c3694f | 1.66432 | -55.96372 | 2026-09-27 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84ff6bda-cec5-36e7-9d2b-e0edeb611c4e | 1.3344 | -50.99441 | 2026-09-27 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14b1e050-ca9f-3707-9aca-fd437474ae8e | 1.96569 | -50.90165 | 2026-09-27 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 197caf77-17e7-30c8-9781-84481005fcf4 | 1.14769 | -51.17213 | 2026-09-27 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 03a7ca8a-cc00-3c41-a1f9-ca1af15c4817 | 1.692 | -50.87415 | 2026-09-27 05:25:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5a69f7e-a85b-3914-ab3a-2c2d8334857b | 2.94152 | -60.32014 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7777f633-82f3-3171-825c-aae7bbcdd484 | 2.64841 | -60.18093 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e98c7c1a-788b-3492-8987-27d72820ef57 | 2.63977 | -60.17358 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a253b0cd-5b9d-3d19-913a-be29ef90836c | 2.94522 | -60.3196 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26d7225a-254a-39a9-8302-18f3eb915b3d | 2.63612 | -60.17414 | 2026-09-27 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8a9bc57-3d4f-336e-87ee-0d58f5304dec | 4.32074 | -60.82556 | 2026-09-27 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef920ba6-9c1f-37bc-8f32-2322a087028f | 2.26397 | -50.77358 | 2026-09-27 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9230557a-bb40-30ee-8c7c-7916d8aef223 | -2.83932 | -51.36147 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ce7cfa4-2bb5-3315-ba54-319e93753e19 | -3.10249 | -50.32287 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5abe0897-8dcc-3410-b128-e824562105a2 | -4.03072 | -55.48967 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd7b6c77-45e2-3d78-9e42-5419405a6199 | -4.25655 | -51.04738 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffd6c043-4f55-3762-97a3-c7a72928f96c | -3.84837 | -55.81032 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fa9449f-9b39-38f4-a9c7-02059c9c4809 | -3.01436 | -51.53326 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7a98554-5566-30f0-9bf6-500c82c97ff1 | -4.54384 | -54.98329 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af3de3ee-1162-3cd5-8c8f-30383e3e28d2 | -2.92016 | -54.16496 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fae292bb-93a5-3870-9614-20d2e18bc978 | -5.16919 | -56.00612 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a54adf96-9567-3e2d-9670-6b1acd85ff19 | -2.92 | -54.15853 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 687c1d82-d72d-3468-9819-d9f7c6a5fd74 | -3.86247 | -55.81255 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 21ceb43d-95cd-36f1-96e4-7779815ee90c | -3.83633 | -55.91233 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27939e2e-a113-305c-a7f6-ed4f926d33a3 | -1.04831 | -53.56301 | 2026-09-27 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 46ea318b-5096-3ac4-b0c1-9a1c183b08bb | -5.68048 | -50.09378 | 2026-09-27 05:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1c31194-57a8-3ed7-8d16-9c5528228092 | -2.99844 | -50.47029 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b21e2f-217c-3aa1-ac73-ac242044d7f4 | -4.17756 | -53.66748 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 023898f8-d84c-30f7-acae-5494dc91269d | -5.73556 | -45.0393 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f35b2c63-cf2d-3011-a478-c8b8a30cd09e | -4.56463 | -54.94641 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8635117c-e3cf-31b9-ab19-4da600eedfb0 | -3.96683 | -59.34587 | 2026-09-27 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b9de605-03ab-3a14-9b07-c3b01fcf1b92 | -4.4992 | -54.94299 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 21f80e52-a42a-3567-9a06-b070aceb633b | -6.05183 | -53.60248 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a50d7793-945c-39ab-9bcd-a6e74e6a8041 | -5.74437 | -45.06373 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a156b241-dd51-3db5-a5ff-aa31d49687aa | -4.28586 | -48.55772 | 2026-09-27 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c60b3140-e0b6-3d87-9f6e-d826114167e1 | -4.29592 | -55.24149 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ad13747-772a-3975-876f-bebeaaad521d | -4.26054 | -51.05314 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b06f590a-e887-39b5-848c-aa80c96d12b8 | -4.53709 | -54.97787 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30a0950c-b3a4-3539-be7b-9f2880c2abb1 | -4.18389 | -49.40791 | 2026-09-27 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ae6bd80-9084-301d-9cf0-325cb8aca55b | -6.07098 | -57.82996 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53995889-5b2e-3ec0-825a-b8e5867524fc | -4.36476 | -55.27777 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fbc67e5-46ed-3eba-ba6f-e2dd8e9dbd8a | -6.13621 | -53.05731 | 2026-09-27 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3151210-64ed-36bb-9469-da1643ddb774 | -2.06829 | -56.87321 | 2026-09-27 05:27:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bc1b3e1-66bb-350b-8002-8001c2c60738 | -4.25668 | -51.04353 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58ad8b9b-864c-3c4c-bf5e-04e0c93cf9fa | -5.74713 | -45.06179 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d9345ea-4829-3d34-948d-05cc5a885366 | -4.14131 | -48.21795 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e110ca6a-5423-3d15-ba2e-a1fcfb87f34f | -5.30434 | -60.08332 | 2026-09-27 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README39.md)
