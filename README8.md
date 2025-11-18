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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41c190f2-72ee-3f59-a2fc-3174a1fd8ba7 | -9.1661 | -50.1278 | 2025-11-18 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8af32bca-147e-30b9-b56d-d8119cd3ba5b | -4.9075 | -45.133301 | 2025-11-18 00:11:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7a8bc3a-9e49-38c4-a969-4fc9dcfbb67c | -4.0129 | -44.257599 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c7db4cf-f178-3441-a0c3-8e9463df9c10 | -13.9196 | -44.179501 | 2025-11-18 00:11:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b68da3c1-9ba0-37ed-b721-98f8ac047ae8 | -3.0438 | -47.009701 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 422d3c05-76c8-34fa-bf58-e7947cfd0723 | -5.4555 | -46.427898 | 2025-11-18 00:11:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d674d7fa-f6e1-330c-a773-1ea9d89cb605 | -3.6669 | -50.198299 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9606fed-3d85-33fa-8f23-6b8657112baf | -12.8355 | -41.447498 | 2025-11-18 00:11:00 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ed6cec00-7f06-30fe-ac0b-285aa137667d | -12.7262 | -45.393799 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dca93cb3-5ddf-3427-b47c-bb85482a5d06 | -3.8898 | -49.09 | 2025-11-18 00:11:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a0300ea-550d-3e57-9aba-fa352c5baf09 | -6.6656 | -43.7575 | 2025-11-18 00:11:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ced2c5ea-46af-33c5-9e80-411f0c770562 | -0.9866 | -47.067299 | 2025-11-18 00:11:00 | METOP-B | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b7d29d8-d990-32a0-9c10-5e76d433a6c5 | -3.174 | -49.795399 | 2025-11-18 00:11:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0329da81-be66-3c80-9546-8a0087dba6de | -7.5078 | -43.054001 | 2025-11-18 00:11:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0df91380-0bcb-39e7-a6fd-d34aa4a299be | -3.67 | -50.212101 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83c64f48-b03d-3560-8b10-aba58852827a | -6.42 | -47.438599 | 2025-11-18 00:11:00 | METOP-B | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36799cb6-6fc5-3572-8455-1f69309dd8e7 | -9.6803 | -46.9077 | 2025-11-18 00:11:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96f4e2a7-dfd6-3bdc-a51b-b62999baf533 | -6.5442 | -46.901199 | 2025-11-18 00:11:00 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26ac0330-3c7d-3c91-b2b4-89c404bf029c | -7.1003 | -48.708199 | 2025-11-18 00:11:00 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4dc24ac2-1c18-3bcd-8043-eaa97fb342f8 | -3.3769 | -46.129398 | 2025-11-18 00:11:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb256d88-8b0e-343e-84cf-a1f56c11b9ef | -11.6648 | -44.737202 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5bfc4708-04fa-37d0-8699-3bc9d8404a38 | -11.2954 | -48.5 | 2025-11-18 00:11:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5f9c6ec-becc-30c6-acab-71256fd0055a | -9.3962 | -48.429901 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0642356b-a38b-3913-a457-c6b67dfb9d6d | -8.4705 | -47.978699 | 2025-11-18 00:11:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b28cbeb9-86a6-3237-a753-687bbc71531c | -8.2228 | -48.296001 | 2025-11-18 00:11:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2af00fcb-d7d4-314f-9b8f-5ffdeb293c29 | -2.7989 | -45.143398 | 2025-11-18 00:11:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8dda78b0-945f-3b29-8b5d-82fe44262976 | -3.7517 | -50.940601 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdb0663a-94c9-33b9-a1ab-00d8a99d8e14 | -7.8292 | -47.154099 | 2025-11-18 00:11:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4df8b59-3587-3677-b223-8765578933ab | -4.1677 | -50.181702 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7709b4e2-173e-33ef-ab74-836743046f8e | -10.8503 | -44.086399 | 2025-11-18 00:11:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4685594c-84eb-364f-bc3f-e5c3795a6272 | -13.7795 | -43.718102 | 2025-11-18 00:11:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2a7d8c9-4b39-32a9-a12e-5f34404c1aeb | -10.8024 | -47.629101 | 2025-11-18 00:11:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aeed61da-41c5-3fa9-a683-710abca04d46 | -3.6787 | -50.799198 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89aaee70-32d1-312d-8672-3bf1243bda82 | -10.3593 | -48.918598 | 2025-11-18 00:11:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c589b0c-ec62-3dc3-a2bd-68f0864822c0 | -2.987 | -51.064701 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d677e1b-ee3f-3560-a638-3812221da5a2 | -3.7789 | -47.743801 | 2025-11-18 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25917e80-e586-3889-92b1-2b058719b9a6 | -2.4752 | -48.2178 | 2025-11-18 00:11:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5d47d1f-2813-3edd-b2bc-2ff5c02eca54 | -3.803 | -50.117199 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45368c70-c457-35f5-9c06-f62e06ac4b8d | -5.8799 | -49.874199 | 2025-11-18 00:11:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af83da26-055c-3fb2-8d72-6c1f1c581f3a | -4.1791 | -50.186401 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd81f22-26ed-3a08-98e4-ebdf1137ae59 | -3.6299 | -50.765202 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a993061-e6dc-3d48-a98a-53a12579c6ba | -4.2668 | -44.243099 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8099dd8a-9998-3344-9722-73f3d08229f1 | -10.7555 | -44.165298 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1b37c72-5473-3391-a51e-f9079f4a98a8 | -10.348 | -48.9137 | 2025-11-18 00:11:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 971ca164-944e-38e0-86c2-ae56b4b19322 | -3.0746 | -50.221199 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96f081d9-80db-3d22-84d9-d9dbdb4e4a8d | -9.3993 | -48.443802 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 060b98b8-b098-349a-a14d-4a5caaa984ad | -7.4384 | -48.928902 | 2025-11-18 00:11:00 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 60de8cb7-b460-3edf-a453-afcece9a41e2 | -6.9419 | -49.652599 | 2025-11-18 00:11:00 | METOP-B | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e42d913d-a514-32bb-9050-c6837ec51201 | -3.722 | -52.046299 | 2025-11-18 00:11:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7da0400-0574-32ef-83ac-9b517d855393 | -8.2935 | -44.012501 | 2025-11-18 00:11:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 61308554-d229-3804-831f-12155d6a1ce0 | -3.7581 | -51.794102 | 2025-11-18 00:11:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5e2eab1-4ac0-3392-a2b4-bec84f03cd78 | -3.0829 | -48.126099 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e8c4104-d3b1-3bcc-8302-d4fc674d1bca | -4.4418 | -47.9837 | 2025-11-18 00:11:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f25a61f3-55bd-371b-99b7-80d613b18bc7 | -3.5493 | -51.413502 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7679f25-af5a-3238-9b56-5b0bd2e6fd80 | -4.3938 | -49.768398 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef445fc1-695d-399e-80fa-7585162f3706 | -4.4933 | -46.680599 | 2025-11-18 00:11:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e4b8323-d9de-3467-9136-010062f9cb59 | -13.3611 | -44.045898 | 2025-11-18 00:11:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53cb6f16-5aeb-3052-8f8d-d86e4dba91c7 | -3.0239 | -47.822899 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8228b3c0-3df2-3cbb-91f9-307ac8a771dc | -4.2643 | -44.232601 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb793353-32af-3584-aa74-68afaceb5e23 | -3.2369 | -50.483398 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51e265f6-9ceb-32b3-9c25-0199e9428e49 | -10.5085 | -43.9515 | 2025-11-18 00:11:00 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34dd4a56-28fe-3e74-ae5b-df47169231f9 | -3.4719 | -49.973701 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2198c69-07c2-3e07-b99f-9f51e92e32ad | -8.4674 | -47.964901 | 2025-11-18 00:11:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b449f0d-c459-3b1d-bf6d-ff723060c1ec | -12.7447 | -45.429001 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75c8a3ef-dbe7-35de-84a3-266df0c2439d | -4.418 | -43.398399 | 2025-11-18 00:11:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f1aeb01-4202-3ce8-9c36-906c3a40cf3f | -3.0256 | -47.830101 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10910b9c-fc0a-37cb-9868-4d43cb58b929 | -10.7461 | -45.1348 | 2025-11-18 00:11:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5632ffce-703c-362b-923d-bb91d40fc0a7 | -8.2014 | -45.021198 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a5b70cf6-b6a6-3600-9782-6240345deddd | -3.9449 | -50.2896 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6af85a01-fbd4-3d7d-8c8b-26cf1b977dec | -10.7926 | -47.631401 | 2025-11-18 00:11:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45a3bcf3-b518-31e6-be51-c8c09a97c5ed | -4.1716 | -44.231899 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c67e6470-0b53-39c8-8152-6ad07c3e46c0 | -4.1397 | -46.354 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| acc14c39-49e8-32f7-8410-af744a4b05b4 | -5.8711 | -48.240398 | 2025-11-18 00:11:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4e5875a6-7fbe-3d97-8d15-f71b4657f2a6 | -4.6477 | -47.937302 | 2025-11-18 00:11:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18632ecd-54ac-3026-a1f6-ef167fd9fb8f | -9.0969 | -44.310699 | 2025-11-18 00:11:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a8c7c8fc-3c8c-3ebd-8d40-f638147465a0 | -15.9048 | -43.221001 | 2025-11-18 00:11:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 43e89bea-b2c5-36f0-8ccd-7beb169d73d3 | -12.7147 | -45.388599 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8848679d-519c-3e81-9b1c-36559f413632 | -3.4205 | -43.441299 | 2025-11-18 00:11:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 291353cd-128d-3b5f-9453-f1b18d536ff5 | -10.1667 | -48.146099 | 2025-11-18 00:11:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afe244bc-1f78-3871-95a4-16ea2d6749f3 | -5.4159 | -43.050201 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89eff292-8b39-3556-b570-edd0c567b90f | -4.2297 | -46.341999 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ef01fa4-46af-3b9f-8687-ad628ff04b45 | -4.1343 | -52.096699 | 2025-11-18 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff93510-2d0b-3e26-8ed1-963435b20a46 | -10.8993 | -49.456501 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f72bf4de-339a-3d69-acb8-ece8b036f3e9 | -11.9276 | -44.8013 | 2025-11-18 00:11:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68b1858c-b2eb-3afe-a070-ccd3779862de | -9.3978 | -48.436901 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8363f06-b963-3d0b-b665-7ef6126e9e88 | -4.7189 | -50.9394 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eaacddc-cfc4-3a51-8a47-69294b4f033d | -2.3381 | -55.775299 | 2025-11-18 00:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11fcb542-6700-3b04-82c2-15b1a7210810 | -9.4107 | -48.448502 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2dff4e2-7a2f-373b-8609-d22e08ab5804 | -8.4689 | -47.971802 | 2025-11-18 00:11:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56f3ee26-f905-3cae-a531-42e6c417c35b | -2.2842 | -51.920101 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6656d776-d9c7-3a70-b6b0-824c5a956c3d | -4.5358 | -48.395901 | 2025-11-18 00:11:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75de6ee4-3632-36e0-93ab-878b833a6f23 | -4.6462 | -46.5392 | 2025-11-18 00:11:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e1a75e6-fbe7-3765-8659-b154b67c6cd6 | -9.9672 | -44.762199 | 2025-11-18 00:11:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 65b61fa3-5e6b-376c-8d35-e111b9c5ff30 | -3.4636 | -49.9828 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caffef8c-598a-305a-9fca-8427d530cc6a | -10.5415 | -47.980701 | 2025-11-18 00:11:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 974f4e46-4525-3466-ac2e-a26ec8cfaeaf | -2.8229 | -46.720798 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1f23edf-41d6-329a-8286-91ad2144a69d | -17.9202 | -40.0572 | 2025-11-18 00:20:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 3bca394d-873e-3667-a0ce-3d7a065ad34b | -3.477 | -46.0656 | 2025-11-18 00:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 278.2 |
| 42407fb2-78cb-3a7d-b3f5-d180a857237b | -5.4377 | -43.0568 | 2025-11-18 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 1f4df723-5154-3d03-80be-c0797af63887 | -3.0714 | -45.4107 | 2025-11-18 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |


[Clique aqui para ver as próximas entradas](README9.md)
