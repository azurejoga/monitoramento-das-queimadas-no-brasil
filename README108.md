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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3675c35b-4b12-3d6f-9a83-8cebea95aeb1 | -10.8227 | -46.6763 | 2025-09-30 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 7797336d-b7e5-3a87-8be1-3a320fa243fa | -8.8734 | -46.6539 | 2025-09-30 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ad85bc0c-f115-304b-ae09-62ca48064922 | -12.2344 | -47.8086 | 2025-09-30 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 839be794-29b0-3009-80d1-3631afa0853f | -8.8732 | -46.6762 | 2025-09-30 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 2aa92ae6-dd06-3f16-815d-bef198cbb0b0 | -10.0717 | -50.2173 | 2025-09-30 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| aaa9ce30-bcd1-3d45-8c75-feda0e05b26d | -14.5137 | -48.4522 | 2025-09-30 11:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 54c1f417-1db8-3a03-bc90-97794e75266e | -10.0531 | -50.1978 | 2025-09-30 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 595077ce-8600-36df-84f0-8ff9cc1ff4aa | -14.5517 | -48.4907 | 2025-09-30 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ae7306fb-3dde-3097-aa4d-99026d0af46e | -12.2344 | -47.8086 | 2025-09-30 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 5c011268-fa68-387c-ae06-47dc9acc1a3f | -14.5137 | -48.4522 | 2025-09-30 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 71c7b8e0-3af0-365b-9ebd-f29397adf730 | -12.6829 | -45.2746 | 2025-09-30 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 36dbf035-c51b-34c7-815f-9eae0d31e7cb | -10.0717 | -50.2173 | 2025-09-30 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| e60c6852-8a82-3d35-8b11-6342f6035fb2 | -14.5323 | -48.4938 | 2025-09-30 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a0d88965-5e53-301d-93b7-e648a6829497 | -14.5141 | -48.4299 | 2025-09-30 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 2d2a2666-6bd8-3bfe-b2b3-ca26d5345ec6 | -10.1045 | -47.7851 | 2025-09-30 11:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 201c4049-b9d1-304f-b23e-e0864b681db4 | -8.8732 | -46.6762 | 2025-09-30 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 53d71226-0c2c-3686-81da-17f4030ce5a9 | -13.162 | -47.4309 | 2025-09-30 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c56bb67c-0df9-342b-ade3-ea7e2582e5af | -7.835 | -46.9986 | 2025-09-30 11:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 5606bc69-6e22-310f-a413-ec0ca400decb | -8.8734 | -46.6539 | 2025-09-30 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8ac63ba0-a874-3cf1-90fe-3a2fa7d17a83 | -14.6603 | -46.9663 | 2025-09-30 11:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 83726498-b95a-30af-90d0-8356a49cfa2f | -7.9191 | -44.6245 | 2025-09-30 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 60c551d4-2eb3-3fc6-b7ed-3482f880a654 | -10.0528 | -50.2192 | 2025-09-30 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| bd24d456-9049-3494-8bf7-b23a1fbc2f21 | -11.1546 | -54.126 | 2025-09-30 11:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 438d05ca-164b-31a7-8464-c758a32aff8e | -14.6603 | -46.9663 | 2025-09-30 11:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 166f69d2-d5ea-3281-93d3-6c3a978671e7 | -8.8734 | -46.6539 | 2025-09-30 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 53b28b74-5132-31c2-8f64-4b6913baf119 | -14.5327 | -48.4715 | 2025-09-30 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f6f3710d-7d3e-3bdb-b336-c1827b38c7b1 | -10.0528 | -50.2192 | 2025-09-30 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 624dc799-8bcf-328d-90e5-8e16c20e680b | -14.5141 | -48.4299 | 2025-09-30 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 69d94e66-6652-358f-a940-4082f67e7bd9 | -10.0717 | -50.2173 | 2025-09-30 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 2952e99b-4479-3bcf-93d8-a5bb6c2b8cc0 | -8.541 | -44.6515 | 2025-09-30 11:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 28e5bdf8-c4c8-3a83-907d-459dfb3801d7 | -12.8774 | -45.1742 | 2025-09-30 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 449a6aca-ad26-326a-98d8-371a7d4a9ef5 | -14.5133 | -48.4745 | 2025-09-30 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 2ece4a18-20bb-33aa-b4dc-cdfb650661bc | -10.1045 | -47.7851 | 2025-09-30 11:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| a1f835c5-b1d0-311f-b696-b0bbe7063fd5 | -14.5323 | -48.4938 | 2025-09-30 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 45c1fb27-5df9-3be6-bc76-7a9d49eba9be | -10.1234 | -47.783 | 2025-09-30 11:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 4182681b-b445-3676-9552-eeab1ed586a6 | -8.8732 | -46.6762 | 2025-09-30 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| b3aad94c-dc70-34fc-bbec-8e41b5b864b4 | -14.3847 | -47.1486 | 2025-09-30 11:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b88484eb-44e6-3678-9f82-4a9012ab32f4 | -14.5517 | -48.4907 | 2025-09-30 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 131e016c-6ee3-3af2-8b45-7590cba8ed06 | -15.9273 | -46.2101 | 2025-09-30 11:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 5abfcbb4-9bef-322f-a463-9757d52c8755 | -14.5522 | -48.4684 | 2025-09-30 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 93ec70ef-e772-3a69-8b6f-7a86c9be18b7 | -7.835 | -46.9986 | 2025-09-30 11:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c399e3d8-1927-3b41-8e03-c8ec0c700968 | -7.9191 | -44.6245 | 2025-09-30 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| c7d83e33-1342-3634-b6d0-f28833be0745 | -13.1624 | -47.4084 | 2025-09-30 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3073a7a9-b943-3f81-b7d5-49282df6e4ff | -12.2344 | -47.8086 | 2025-09-30 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| aa582224-26d9-3c31-96b3-0c42391de884 | -10.1234 | -47.783 | 2025-09-30 12:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f579fec9-423d-390b-a96e-748eb44c51bb | -14.5141 | -48.4299 | 2025-09-30 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 169c7b1a-c272-3082-996c-f756adc54d6b | -10.9586 | -46.5016 | 2025-09-30 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| aa660bec-8994-397c-99e5-975a79596b2a | -8.5407 | -44.6745 | 2025-09-30 12:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9bace254-659f-341e-83f8-e0640a5cde6e | -12.2344 | -47.8086 | 2025-09-30 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 7407a2bb-81fe-38a9-afcc-5acae2fe0fb2 | -14.5323 | -48.4938 | 2025-09-30 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| cb787ed3-5e19-3f5c-a24a-3ed540e3f611 | -10.1045 | -47.7851 | 2025-09-30 12:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 1a474e72-158e-30f7-9685-cdfbd0d98d0e | -12.6829 | -45.2746 | 2025-09-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 1586fd68-2c2b-3bee-b7f6-f8e4dfb1dafc | -14.5517 | -48.4907 | 2025-09-30 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 116.1 |
| eac6cd59-3563-3363-8bd3-7c8cd6638293 | -10.9395 | -46.504 | 2025-09-30 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 8cf1bcef-8bf3-3c23-9656-fb4db0006b58 | -7.8163 | -47.0003 | 2025-09-30 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| c82e2091-6ffb-300a-88fc-57d026f4ae51 | -11.6837 | -45.3563 | 2025-09-30 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 32c119f7-c9ab-335e-99ed-f431c3b373b7 | -8.8734 | -46.6539 | 2025-09-30 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5f9b7807-549e-3d56-95cd-29c14a7bf25e | -7.835 | -46.9986 | 2025-09-30 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| e0c1889d-4e43-3ca8-b0e3-57bd60b414c7 | -7.8348 | -47.0207 | 2025-09-30 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| f3949b11-c0eb-3713-856d-65c777ce4f59 | -11.1546 | -54.126 | 2025-09-30 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1682a02f-d92e-399a-8f15-8830c19e48ca | -14.6603 | -46.9663 | 2025-09-30 12:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 4f9362b3-c20e-304b-ad2f-3c2daa1ecafb | -7.9191 | -44.6245 | 2025-09-30 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 376377b3-b111-3811-92e2-31b1cbad80c9 | -9.1248 | -47.6256 | 2025-09-30 12:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 13e2e467-fe77-39c0-8cba-b88fb3183845 | -13.3812 | -48.0685 | 2025-09-30 12:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 480705f5-2e0d-3f28-9800-5771d9de194e | -8.541 | -44.6515 | 2025-09-30 12:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 80b62820-59bc-370a-b534-3ae6854f1491 | -8.8732 | -46.6762 | 2025-09-30 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c4b4d8fa-a0a1-3a89-ba2d-7ad3b7cb8ad8 | -12.8774 | -45.1742 | 2025-09-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| b93bd282-d20e-316c-bc66-4abe8752fe31 | -8.874 | -46.6092 | 2025-09-30 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 900e2855-e385-3576-9dd4-5080a63932cd | -16.7575 | -51.3482 | 2025-09-30 12:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0a55c34d-6260-3a44-a121-f39a409a1420 | -9.1246 | -47.6476 | 2025-09-30 12:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 65e3ed0f-29e5-314a-92a1-b8d034928041 | -8.541 | -44.6515 | 2025-09-30 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 87ee776b-7def-35f8-9381-53c369ad4cf1 | -15.9273 | -46.2101 | 2025-09-30 12:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| da8a7d1b-2df9-31cd-a9cf-f5fbbac3634f | -10.1045 | -47.7851 | 2025-09-30 12:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 5184b809-babc-3627-824d-d1f52c79b1e6 | -12.2344 | -47.8086 | 2025-09-30 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 918bb7b7-70f1-33ee-aaa5-f87753d7be3f | -14.6603 | -46.9663 | 2025-09-30 12:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 12548bee-b5b0-3d95-89e5-d6f029fe2285 | -13.3812 | -48.0685 | 2025-09-30 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 7b290c4a-7fd6-3a11-8477-897e88779d42 | -8.8732 | -46.6762 | 2025-09-30 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 5d90b287-9873-3aca-8d87-00811c876252 | -7.835 | -46.9986 | 2025-09-30 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 57718c4d-c642-343e-b888-38d35b00c374 | -8.8737 | -46.6315 | 2025-09-30 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1cdc68e3-2ee8-32bf-aa25-94a489b39dbb | -10.0717 | -50.2173 | 2025-09-30 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 360ab7cf-9212-33c4-86b4-0bf183e8288f | -7.9194 | -44.6016 | 2025-09-30 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 884e7501-661c-3fe8-a436-c25165888138 | -8.244 | -45.7754 | 2025-09-30 12:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 2a821197-6882-34fc-ba46-474298cbf812 | -14.5141 | -48.4299 | 2025-09-30 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c5a4e7af-43b6-3df5-80ed-37e063b2f3c6 | -8.8734 | -46.6539 | 2025-09-30 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 76116997-bc67-3e95-a930-403c55eb3bf9 | -13.4005 | -48.0657 | 2025-09-30 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4e98d3d0-7e07-3d26-9d4a-e0b9baa69f3e | -11.1546 | -54.126 | 2025-09-30 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 42293d43-09b1-3fcb-8bfc-8a0d51c70edc | -10.9586 | -46.5016 | 2025-09-30 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3391c524-1689-34fc-9a9d-4a050ae1f862 | -14.5323 | -48.4938 | 2025-09-30 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| bcbba464-5699-3b3d-8486-cb05f2b0a5eb | -14.5517 | -48.4907 | 2025-09-30 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 6f92c148-2e52-3a59-a63c-ed3215c97aad | -7.9191 | -44.6245 | 2025-09-30 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 2c11dbde-55c9-3bd3-8761-d46a3e4278cb | -9.1248 | -47.6256 | 2025-09-30 12:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 6c584a64-8ead-336a-8cbc-68d69effa9c1 | -7.8696 | -47.2606 | 2025-09-30 12:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 445d60d1-a4e9-37bf-ab95-353c699fd9c6 | -9.1248 | -47.6256 | 2025-09-30 12:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 18ad5491-1211-3a46-b5e6-09e844eed58b | -7.835 | -46.9986 | 2025-09-30 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 6869c328-8376-3cdb-b313-0cc92a8b5fab | -7.8348 | -47.0207 | 2025-09-30 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 179.1 |
| cfea1bf1-1911-320f-bd29-453a53fbdef7 | -14.5323 | -48.4938 | 2025-09-30 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 482bca61-f624-3653-be8d-99a366dbb2f3 | -10.1045 | -47.7851 | 2025-09-30 12:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 2f69822a-32d6-3f2c-a568-67fc16050eba | -8.244 | -45.7754 | 2025-09-30 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 8ad7aaed-476a-3bb1-8dac-8bc509be5ed6 | -9.1246 | -47.6476 | 2025-09-30 12:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| da50acb4-32ab-34ab-98e3-895b628a17d5 | -8.8357 | -46.6578 | 2025-09-30 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |


[Clique aqui para ver as próximas entradas](README109.md)
