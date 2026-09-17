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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98d0b972-efd5-309c-bf21-b4fe9006a59f | -9.3567 | -50.1796 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| fe777b29-b672-3020-94e6-8e546b58e08d | -4.5045 | -54.9646 | 2026-09-17 14:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 6450b098-6996-36d2-b403-a71ead7fea27 | -13.6531 | -45.97 | 2026-09-17 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 342.3 |
| 8718e77d-1fd3-39de-9c21-ae7fb1a3fde6 | -8.8644 | -45.8919 | 2026-09-17 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 179.0 |
| ee510de2-25e9-39a0-9226-128fbc5523cd | -9.4134 | -50.153 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d5a2eebc-cacd-3294-ad6a-d5c50b210d9f | -15.5711 | -54.2439 | 2026-09-17 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 8b5a0632-9b40-388f-8977-a17306557d7e | -9.1336 | -65.8627 | 2026-09-17 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 21f39c64-0208-3554-8c4e-c07ed7e1adc0 | -7.0112 | -43.393 | 2026-09-17 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 5740ea29-ff34-32cd-9a71-f42bcb2e20d7 | -9.3569 | -50.1583 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 29157cae-e6bb-3823-92cd-935ac884b7da | -9.4137 | -50.1317 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 125f4a13-b6dd-39be-8a19-6815134759ba | -10.458 | -50.9865 | 2026-09-17 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 8270d928-fef4-3cb8-a4a8-3d303e3de937 | -13.3758 | -51.7193 | 2026-09-17 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| dea6f942-99c7-3a3a-bde3-f2ffb405a213 | -9.3753 | -50.1992 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 18264af5-6ef6-3648-8afa-b9fbae9b50e9 | -4.5589 | -42.9289 | 2026-09-17 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 45fe267a-0048-3b16-b202-16facd732992 | -4.5228 | -54.9839 | 2026-09-17 14:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| b243dade-86e6-3b29-a451-14f87f9381e5 | -9.1711 | -49.9835 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d94a9ab9-3458-3983-b85f-84fa9bb28471 | -9.8322 | -48.3417 | 2026-09-17 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c357a71c-d8da-337b-8363-7c20bcbfbd7f | -13.6526 | -45.993 | 2026-09-17 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 240.5 |
| eaae0e22-1733-3dba-8267-9d59a7dbe771 | -11.5811 | -46.8919 | 2026-09-17 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| df735d6a-1b06-384a-996f-e35080dd627f | -9.3948 | -50.1334 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 1e9909eb-cd73-3c57-b827-130217535524 | -15.539 | -53.8502 | 2026-09-17 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 10e11ac0-0a95-345f-b6f7-f6315d0ca7c3 | -7.1192 | -42.1786 | 2026-09-17 14:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 78c83392-5130-325b-ac3d-73abb522c191 | -8.8647 | -45.8693 | 2026-09-17 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 51f4383c-607c-3600-9230-fcf5d434cf94 | -9.8697 | -48.3595 | 2026-09-17 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e55529a5-5f26-3f3f-8650-49e7e1f32dcc | -9.8508 | -48.3615 | 2026-09-17 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 1d067c19-d92e-3ebf-a35d-005741b53966 | -15.4813 | -53.8157 | 2026-09-17 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 3829d1ae-dbef-3580-aeda-e2180c92289d | -14.8376 | -59.5515 | 2026-09-17 14:20:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| ee73ba0e-2574-35d1-91d8-0d9c2e41ed3c | -7.8033 | -44.8651 | 2026-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 399d54e5-d5da-3244-8923-b6d9838bb1ce | -10.0422 | -45.5528 | 2026-09-17 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 224.8 |
| 07f9d537-d1a7-31e5-87c9-8d602fd377f5 | -8.4855 | -44.5655 | 2026-09-17 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 9aed213a-5333-3a83-beea-5501e51d60cf | -13.3754 | -51.7406 | 2026-09-17 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| eb191eb7-99eb-3be9-a3fb-a253c16010f5 | -11.3629 | -44.0112 | 2026-09-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| ce773f5e-af26-37af-9e9a-87a853c08865 | -9.8319 | -48.3636 | 2026-09-17 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 5dccc519-f9dc-312c-90cf-3bcf43abfd41 | -10.876 | -50.8163 | 2026-09-17 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7a9befff-ca21-3390-9104-968a756cabdd | -11.5811 | -46.8919 | 2026-09-17 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4574e0e8-086d-3f90-a1cd-4c45d79df956 | -8.4669 | -44.5445 | 2026-09-17 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 74df64b0-303c-3a38-a352-1e878b7550c3 | -9.3567 | -50.1796 | 2026-09-17 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 48c1e324-e6d2-32a7-9bc8-f6f846458554 | -14.5709 | -46.5941 | 2026-09-17 14:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 084758b1-a398-333c-a715-4460fc4f7fb5 | -13.3949 | -57.0242 | 2026-09-17 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| a76c4a98-17d2-3211-9f9b-c4792345d430 | -15.5008 | -53.8132 | 2026-09-17 14:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 725155a6-c88d-325a-a20a-95f211fb2d8c | -9.3954 | -50.0908 | 2026-09-17 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 2bc88a1b-fb1e-3ef6-882e-0bffd781d8a9 | -14.1937 | -45.1372 | 2026-09-17 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 9c1191a0-6138-34d0-8a35-bbc2b7310db3 | -9.0407 | -65.9215 | 2026-09-17 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 69ab3bfa-15f5-3c34-84c0-9322d6d97355 | -9.852 | -46.9046 | 2026-09-17 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 6bc7a2e3-d14b-381e-ab9d-60fe9fdcba97 | -8.475 | -46.8943 | 2026-09-17 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| ddf36726-6b14-3385-8d70-5ae9e46e6a82 | -10.8919 | -54.0062 | 2026-09-17 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| fadc4082-7595-37ec-a5ae-2d741b256201 | -14.1932 | -45.1606 | 2026-09-17 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 9d0e7a84-3de1-3376-afcc-4a392b84c3e7 | -7.0084 | -43.6497 | 2026-09-17 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 479d071a-84bc-3c92-82f0-04f463e1eb1e | 3.9353 | -59.6446 | 2026-09-17 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| b27e027f-100c-3aab-92d2-4fce51fbf2bf | -9.3569 | -50.1583 | 2026-09-17 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 4fdb07d2-6a44-3737-82eb-53cdc16158d3 | -10.8571 | -50.8183 | 2026-09-17 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 49b13b0d-f70c-3502-99e8-e3dc86e58baa | -9.4139 | -50.1103 | 2026-09-17 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 2988c83a-fff6-3ef1-98fd-802b1a04f10c | -10.0418 | -45.5756 | 2026-09-17 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 4b56efaa-59af-348f-8d80-c908739742a7 | -14.1547 | -45.1442 | 2026-09-17 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 7f4de2a9-36ec-3ded-af44-a8c31b45e91e | -9.3943 | -50.1761 | 2026-09-17 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8ae91d5b-01c1-3583-9878-d56dd19b4bc0 | -8.8642 | -45.9145 | 2026-09-17 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 64c25cb1-ee30-3eb9-ab9b-838e02bda304 | -9.0868 | -61.0095 | 2026-09-17 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| a0fc3b4e-26cf-3108-aca6-be45ec103d38 | -1.805 | -54.9309 | 2026-09-17 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 25ccd029-8204-3ff7-80bc-3721170be836 | -9.4137 | -50.1317 | 2026-09-17 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 4fd7f80f-d011-373c-ad5f-5c2d801a79cd | -11.8941 | -47.5876 | 2026-09-17 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| a02c1306-2141-38ea-a16f-fe542b35afaa | -12.6826 | -54.6763 | 2026-09-17 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4799d0a3-8d5f-3115-9ff0-a2cd3731a878 | -18.8899 | -46.8519 | 2026-09-17 14:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 70.4 |
| ac5b51ed-159d-3610-8270-0dae08e7730e | -7.6414 | -45.8556 | 2026-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 56c5d67c-fb97-33e2-8a11-7b2a07837486 | -10.8343 | -54.0933 | 2026-09-17 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0c8d5dc9-8caf-3ec5-878a-ca1a37e6eb67 | -11.8928 | -50.0608 | 2026-09-17 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 81f04988-3188-3455-9dba-c10d01452e38 | -11.3437 | -44.0141 | 2026-09-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 381.7 |
| 7a41a255-e5f8-31a3-becc-e928ddd0955d | -4.5229 | -54.9639 | 2026-09-17 14:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 213.1 |
| 5455f24a-5226-3467-abbb-9e0ec71f8c80 | -10.458 | -50.9865 | 2026-09-17 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| dcd30b9f-0a3a-31af-86e7-97a201db16cc | -11.738 | -50.2295 | 2026-09-17 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 0a26d0ab-4c70-30aa-98b8-cc8e6d13b9b4 | -11.3625 | -44.0347 | 2026-09-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 556cd84c-3f55-37f0-8165-5829f46381a8 | -6.9896 | -43.6514 | 2026-09-17 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 6f87c2af-05cf-3149-9fa1-ec397f762435 | -13.3755 | -57.0462 | 2026-09-17 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 7cd090b6-1e45-3ad0-ba2a-93b303c5d827 | -6.6515 | -43.6354 | 2026-09-17 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 815a5e4d-15b6-3424-b57a-2d534af1577b | -7.1381 | -42.1768 | 2026-09-17 14:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 5b852b1f-4cb3-3c4b-b5ae-419ee7e7c78e | -12.7243 | -48.2734 | 2026-09-17 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 5566d6f8-c9dd-3cc2-befe-09734b960008 | -9.1336 | -65.8627 | 2026-09-17 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 243.8 |
| 6da1370a-805e-35cd-b883-265b23b8726d | -10.8757 | -50.8376 | 2026-09-17 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ce806851-f5dc-3df9-a848-efc016f234e5 | -7.6381 | -46.1478 | 2026-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 392bcf70-1a74-335a-824e-6e196cfa3725 | -7.0804 | -47.5031 | 2026-09-17 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d10a0086-ca5c-3260-a297-6af9dea12004 | -9.7794 | -60.4551 | 2026-09-17 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| cc0fca91-c32b-3ae0-8a05-799ed927e6f3 | -2.908 | -54.171 | 2026-09-17 14:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 541e2f48-a802-3646-a1bf-3f5d2192c6cc | -9.8508 | -48.3615 | 2026-09-17 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f30b3d84-9b82-3582-9e21-affaae41f3a7 | -14.8376 | -59.5515 | 2026-09-17 14:30:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ec433cc7-0e65-32bd-9faa-3a61ae01f75d | -9.1337 | -65.844 | 2026-09-17 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 703621c9-ca0a-35e1-9cf7-001652f94824 | -3.2212 | -53.9422 | 2026-09-17 14:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 88b364fd-5aee-3475-954e-23ffc535b24d | -9.1057 | -60.9511 | 2026-09-17 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 45eaaf2a-6bc8-30de-8b95-dcd312a22f30 | -13.6531 | -45.97 | 2026-09-17 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 49ee7ee1-ca1b-3257-995a-8d1f1ec71311 | -13.2986 | -51.7501 | 2026-09-17 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 0cc44b36-8a44-34f2-aad6-c34155829581 | -7.8221 | -44.8632 | 2026-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c06601e1-fab0-3898-9b64-4402b0f80d42 | -7.0454 | -42.0427 | 2026-09-17 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 26079661-8027-3916-9a7a-ee954399fb34 | -9.7608 | -60.4561 | 2026-09-17 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| dff5c7b0-a436-3a0f-9475-9095b0fa4f81 | -9.4325 | -50.1299 | 2026-09-17 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 19079148-7e26-3edb-8d24-6b33ca96e2db | -14.1737 | -45.1641 | 2026-09-17 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 50513422-f138-3e30-b4ad-aa799b71b9ee | -9.8322 | -48.3417 | 2026-09-17 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1e300e44-597a-3dcb-b944-315902b7f8aa | -9.7793 | -60.4744 | 2026-09-17 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 2a9deec8-3a93-33d8-8814-6b4987d9fadd | -11.3442 | -43.9906 | 2026-09-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 33e87074-5460-3f44-a059-9150b47b61df | -9.1056 | -60.9703 | 2026-09-17 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 49375027-6b29-302a-8167-79a2471aadbf | -9.3564 | -50.201 | 2026-09-17 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 2f8d79b5-7763-3fa3-94d0-c8b9c13884a9 | -10.7999 | -50.8455 | 2026-09-17 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 6921f7a6-5064-3546-bf1a-7ecb3aefa081 | -7.1384 | -42.1529 | 2026-09-17 14:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |


[Clique aqui para ver as próximas entradas](README94.md)
