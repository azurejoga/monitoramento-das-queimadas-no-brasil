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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8a7ead2-ddff-346a-b735-2c3038cc2321 | -12.00405 | -46.63328 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77e6706b-788b-31a2-ac74-ee773d1001c7 | -8.87955 | -47.63179 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd2b21a2-a5e8-35f0-9f9c-5264711212f8 | -14.54808 | -48.40674 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2a0a283-b95f-31b7-9065-f97b2d2b69ec | -11.83797 | -51.80407 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eddeccc4-f295-324e-b21a-28b056a3449d | -12.69819 | -46.9102 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6ff23662-2cc8-39d4-b368-64d58975400e | -9.09942 | -45.85326 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1a4305f4-0b8a-365e-afa9-ca7dbe9dd884 | -9.67436 | -46.37616 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f51b9a5c-1297-37b1-b2cc-6319b7f75ef4 | -10.93465 | -44.32543 | 2025-09-29 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64a2e621-8924-357f-827a-071aa3e10991 | -10.28763 | -45.19492 | 2025-09-29 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56c7066d-6aa8-3bb5-a2f0-bf41db3b68a0 | -14.84068 | -48.37922 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2626c4e1-e0e0-3a6c-aa0b-6158a4f57b17 | -15.72418 | -41.77504 | 2025-09-29 04:08:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7a99764f-5ae4-3b19-a9af-7487ab36b0d0 | -14.55206 | -48.40759 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6287371e-63be-39ab-bd11-f45cb9ddd66d | -8.84475 | -44.93497 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e14f807-58b2-3c42-8666-b505e0d091b7 | -11.10742 | -47.51888 | 2025-09-29 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea85d025-52d6-3b5d-87c5-90b4c98bfca5 | -8.82746 | -46.19584 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1afb8026-efc7-34f1-a016-dbc86c2b749b | -15.08104 | -48.33509 | 2025-09-29 04:08:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 109e1187-cf8d-34ba-8a5d-5a31530d09e2 | -12.94654 | -47.18297 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57f864bc-e2a9-3676-ba7c-d24468980584 | -10.82507 | -47.93478 | 2025-09-29 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aeae13e1-b664-30b8-aeb8-e4c5856e35f0 | -13.54606 | -44.16903 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 128f4b7e-9d61-30b6-ade7-c983a800fc1b | -14.64987 | -48.15765 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a9d3d78-b6cd-3200-b3dc-1242f1a255cf | -9.94249 | -48.80281 | 2025-09-29 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47b68272-d0bf-3bf4-84d5-a2fd53aa6763 | -12.86756 | -46.96466 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7af56816-2b7e-3efa-9eab-2591092a4905 | -15.33766 | -47.91297 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 039913f8-2eda-314b-872a-b2d54813ae2a | -15.86864 | -46.22169 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f401c1db-773c-3dfb-b781-347f1a6181fd | -14.62984 | -48.28487 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55b66451-1a55-3bc7-8927-2d23e3321089 | -15.27405 | -47.86977 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9633882-c606-3798-b565-653e1b0e53ab | -15.78127 | -43.85518 | 2025-09-29 04:08:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 821efa34-662d-30b4-87f5-de2afe338c50 | -15.23559 | -43.84819 | 2025-09-29 04:08:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a94b4e4-587c-3ade-9686-c73d1022da08 | -9.08695 | -47.63121 | 2025-09-29 04:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f413625-a168-35c7-870e-b1b83d01ad03 | -12.93985 | -46.76773 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1839f558-873b-3245-8067-9b5caa12824b | -13.79358 | -47.89319 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97c22837-7e8c-3b08-844d-308d516beea5 | -15.41879 | -48.23106 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ffb6758-a27f-34d8-aa6a-f6e8d106ba2e | -11.27269 | -47.19599 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecce50aa-37b4-303f-83d3-ac8f7b05e8f1 | -14.58601 | -45.0211 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f53b816-97c6-341b-99a7-dbc607ccb18b | -13.81901 | -47.4787 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df8b8841-9d89-302c-a893-3276dec7e5eb | -12.02924 | -47.91169 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6edc508-e897-3aeb-8f29-67ac5863626c | -10.17963 | -44.88598 | 2025-09-29 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ef190d5-35ae-36db-995e-04c4ec6ad121 | -9.99359 | -45.42049 | 2025-09-29 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a9f0ac9-c1d4-3120-b49e-374a54ab7ff1 | -10.04373 | -50.21284 | 2025-09-29 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e7be89e-6d57-3356-92ed-d8fd58dcc816 | -10.41095 | -48.1128 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d3c1446-ef2c-3e29-a0e1-48e7d4ae22a4 | -14.57895 | -48.23547 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 00745bfd-d1b1-359e-8c09-857397c8093c | -15.04658 | -46.97306 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11397891-460d-36c7-ae73-fb8c73a48a7b | -13.73864 | -47.88311 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd321f18-0e38-3799-a2df-2d36e3e94fc3 | -13.83422 | -47.48198 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 187d7911-967d-3d77-af5d-736b6c443978 | -8.84577 | -45.03988 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d0e02c6-bec6-3f41-900a-1c6f3c05f3dd | -14.52538 | -48.39512 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 00dcb7df-0e76-3196-9627-9646bd2d778e | -15.28072 | -49.51666 | 2025-09-29 04:08:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5ec123d7-1e9c-3f90-a703-4e94a839d7df | -13.17988 | -47.44352 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b1e1e081-65d2-32bc-af62-438e0a0aea7c | -14.54154 | -48.44295 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 161d12f5-ff66-3180-a4b1-f5927edfd132 | -11.69641 | -44.47364 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83c75e92-3b52-3194-b275-01573e1fd10e | -9.08759 | -47.6274 | 2025-09-29 04:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c2a9ade-1674-37f7-9a8c-13289c5b7df1 | -13.78762 | -47.88103 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3f4fefa-4106-35ed-b583-ba31fdb9347b | -10.60053 | -46.27361 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d22f3a25-4273-3986-811f-3878ef9eac95 | -12.84654 | -46.90691 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec7bc8e9-9b74-334f-a843-a9a6324299dc | -14.43464 | -44.87265 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2846e055-f717-34fb-bdf5-43ceb9d19ee0 | -13.40522 | -48.15036 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 058a6e2f-e89f-3364-8ff7-5d22722f6d88 | -8.88737 | -45.04541 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a726e5a-6910-3d8b-95da-3a74167901e8 | -12.97998 | -46.26466 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7fdba8aa-2933-302b-b7bb-092439ae8a86 | -11.80536 | -51.80397 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfe2f678-a3f1-3c38-bbd3-c26e00e0b6c8 | -13.81108 | -47.90895 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97bb522a-4277-319b-a629-7e9cfda70e3c | -14.57443 | -48.28336 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1a72509-f57f-37d8-a3a8-5651ed336f88 | -11.26402 | -47.19946 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9e9bc752-fec8-3e86-b774-fb4f4a79a3b4 | -15.47045 | -47.93497 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c11e49a9-7349-3e79-8c1c-80390ffd59c8 | -12.85053 | -47.61938 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d9492c7-2ac0-3b1a-9989-ca7661ebf6cb | -8.82284 | -46.19983 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d2bf115-1c47-3c59-b047-7ff741a2c89e | -15.29167 | -49.50519 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 935423a2-bb7d-3c39-97ee-e4ba65c8c536 | -15.86843 | -46.21843 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f856fd0e-9b1a-3b6b-9890-f9ff127cdb2d | -13.18374 | -47.44421 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 898daa91-7934-3883-bb53-b341b28df5b6 | -15.86995 | -46.21405 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cea62a2f-363a-3730-a713-9ceed74da22d | -12.02055 | -48.34678 | 2025-09-29 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4de19dd1-c81f-3b7c-ade3-e803455fb175 | -15.61498 | -46.25944 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2550562-bc0f-3eca-a10e-231c34cfb8b8 | -12.69874 | -46.90824 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7b82168b-9cc5-361e-b2d7-717ffb49c3f1 | -10.80787 | -46.67363 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9398c54a-6921-3507-b7f1-0ab650079456 | -12.9324 | -46.76639 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6dfbc30-d606-3df7-a3ef-f72953e90d41 | -11.92234 | -48.04437 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7277b6b-5d32-3b04-964f-e7f370ad8616 | -13.74745 | -47.90177 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fc678f2-834b-3c92-8804-eb1c9885a56e | -14.62107 | -48.29787 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b1f2b62-f3df-3ed8-ab75-fe1616698010 | -8.83505 | -46.1974 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f26e07f6-1e2c-30bd-bb03-40c82b6ada53 | -9.74984 | -47.79663 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e930f31d-3ecb-3223-963a-83b850ec4d39 | -11.44251 | -46.64398 | 2025-09-29 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 563043c1-a0eb-3c19-9c76-990289a0b6d9 | -13.83906 | -47.97578 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5126bc44-015c-3947-ac83-8e7642da7af4 | -15.26231 | -48.76365 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2507e1ba-5d51-3a69-9e63-30a1617e6288 | -15.25753 | -48.76695 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55742965-36e3-319e-a22d-a79ed4706d6c | -11.80757 | -47.62199 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ca02e4e-4f16-3777-b185-652d597e5a0d | -12.88686 | -46.98808 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cfe65d99-a4fb-3ad7-aad7-37b8feab138d | -9.47004 | -45.50389 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6949bb29-72d6-36c0-a527-f0822120fa9c | -11.42802 | -45.03438 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37904aba-5ab0-39ab-b261-77adbb788b9c | -12.94556 | -45.17612 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfdb8918-99a2-34ca-b557-69d882b7a6b1 | -14.5675 | -48.27632 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc7dbddd-959d-3298-886e-7bd2e25320e5 | -15.21334 | -48.04726 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03e9aa04-315e-39f5-8a3e-f4b44f43011e | -9.27629 | -45.69855 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20fffb31-9ce3-33a7-8718-7b88c5465f26 | -11.43338 | -44.95931 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73382c99-cdfb-34f7-abef-ee0bb4218197 | -10.82025 | -47.93794 | 2025-09-29 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca93f17a-f2c9-31d4-838f-6034e102e5d0 | -11.71361 | -44.43369 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e5a0d11-efd9-3d3c-bd03-358ae295c31f | -15.28784 | -46.41487 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe45adcf-2cb7-3b87-a01a-2efe7d70fd6b | -11.31943 | -47.78706 | 2025-09-29 04:08:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e38d66d-33b1-357b-8dac-72c6c3c5cf11 | -8.71494 | -50.05471 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5b0ed78d-ef61-303c-927c-fd7ae17e84dc | -14.57012 | -48.23906 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5fa6d71-141f-34fb-b6f5-a7b519a13831 | -12.99943 | -49.44171 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad10033f-8b4a-3e3d-852a-db0db03b6065 | -8.38491 | -47.99607 | 2025-09-29 04:08:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README49.md)
