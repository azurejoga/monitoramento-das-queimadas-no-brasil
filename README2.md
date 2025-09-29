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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b034c10-b6ec-32a3-9cab-6079ecce6d5d | -9.4192 | -54.7172 | 2025-09-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| af825baf-91c2-3b03-9f2f-b8e2f3884596 | -14.7841 | -45.7284 | 2025-09-29 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| df79f035-fac8-36da-be13-d514fd556628 | -7.7087 | -34.927 | 2025-09-29 00:30:00 | GOES-19 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 106.4 |
| 0e64555d-3906-3b7c-8c84-fc87e722e83a | -14.553 | -48.4237 | 2025-09-29 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 3dc6d916-bb18-3274-805f-2a80f435941d | -2.5773 | -48.3931 | 2025-09-29 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| e8258b98-3150-3c8b-999a-3ab27310d572 | -4.6971 | -41.9748 | 2025-09-29 00:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 9ea3c381-0af0-33d1-9033-75e3b56f4b55 | -2.5957 | -48.4141 | 2025-09-29 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4db702f1-be5e-31f1-9215-61e3f82f488d | -9.4194 | -54.697 | 2025-09-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 1c9a59d2-0c04-31c9-9e67-58a30e46bc28 | -15.2893 | -49.5035 | 2025-09-29 00:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 311.2 |
| cc24e449-26d4-3183-af13-eabec0e79d2c | -2.5772 | -48.4146 | 2025-09-29 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| ceba4fe1-d551-3ce8-90fa-31d059571bc8 | -9.4007 | -54.6984 | 2025-09-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ceeabccf-0323-3354-896d-6379e22d07e2 | -2.5958 | -48.3926 | 2025-09-29 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| fa1e0152-be36-3701-809e-17da351b3db2 | -7.5447 | -46.1115 | 2025-09-29 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1940383f-3151-3e44-8911-202dbc2d392e | -4.7159 | -41.9736 | 2025-09-29 00:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 158.3 |
| 2e04b7f5-bb7a-3b85-bbdc-e6e3e133b9ce | -10.8036 | -46.6787 | 2025-09-29 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 00a93349-7d2e-3ee6-897a-5caac0a3674c | -18.1782 | -53.3024 | 2025-09-29 00:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a0185dce-6235-33c6-bbd6-d65582c4ce15 | -6.1112 | -47.2897 | 2025-09-29 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 41f0f873-ab33-3678-a3dc-374b51537ce8 | -7.5635 | -46.1098 | 2025-09-29 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| dacead75-ff6d-3849-865c-0e1679ca594e | -4.4013 | -44.0755 | 2025-09-29 00:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| fd6211bc-4adc-3875-9e28-b81df9d1fb30 | -7.2214 | -44.783 | 2025-09-29 00:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 278.4 |
| f5068319-6147-3cba-8a4d-14d11bf88295 | -7.2211 | -44.8058 | 2025-09-29 00:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 275d39be-6535-37a6-a00b-1acd0953d03d | -15.2698 | -49.5065 | 2025-09-29 00:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f686368e-45d0-3f11-b4fb-7a9a5ef320b6 | -7.2399 | -44.8041 | 2025-09-29 00:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 3d8a8840-21ad-3c03-8be7-1baa11423df8 | -9.4005 | -54.7186 | 2025-09-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8731805b-1a97-30d6-bef4-e8b90c3edaed | -3.1013 | -47.0082 | 2025-09-29 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 56f9d78e-1554-3b19-bd20-7b0fcbf624cf | -7.5449 | -46.089 | 2025-09-29 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| daffc6a5-998a-34c9-86e1-4c44028fb60a | -11.2711 | -47.2012 | 2025-09-29 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| f20898b7-a816-3523-b30f-a3cb4ae35f77 | -9.4194 | -54.697 | 2025-09-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 35d159fa-8582-34ce-a9a7-30eed6103cf5 | -4.7159 | -41.9736 | 2025-09-29 00:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 52fba4be-db4d-36f9-8e1d-d06bb900bb14 | -14.5336 | -48.4268 | 2025-09-29 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 12ceef46-911c-3eab-8619-6cae75a082fb | -3.1013 | -47.0082 | 2025-09-29 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| b36d9eb0-f803-325a-a9ef-dc9ec8b5c31e | -20.0491 | -41.3251 | 2025-09-29 00:40:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.1 |
| fde54a07-3e0b-3663-bd9c-7dd51583a80f | -7.2214 | -44.783 | 2025-09-29 00:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 249.3 |
| 9011f523-d3c2-3610-96c0-01ab29d99e45 | -2.5772 | -48.4146 | 2025-09-29 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 94b254f4-025f-3a05-a4bc-e5087bdb7e8f | -14.553 | -48.4237 | 2025-09-29 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 3db3ed59-7bb2-3d7f-9652-9ee99d048b21 | -15.2893 | -49.5035 | 2025-09-29 00:40:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 345ed405-f6f2-3147-a48c-ae5611a5b978 | -3.1012 | -47.0301 | 2025-09-29 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| dbce31a1-28c8-34d6-a887-72e373e8fa2e | -4.4013 | -44.0755 | 2025-09-29 00:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c656cdc9-05a6-3fac-9e60-8d018a1cca4c | -2.5773 | -48.3931 | 2025-09-29 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| aa625952-4297-3056-808b-7e8883714644 | -7.2402 | -44.7812 | 2025-09-29 00:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 8c0d5a13-716a-33e9-8028-1cb4dae8932e | -9.4007 | -54.6984 | 2025-09-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 114fc8dc-9faf-390e-8e3d-c2f6f16e350d | -7.2399 | -44.8041 | 2025-09-29 00:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 3e2c86e7-320a-3542-b539-61be7195926a | -7.2216 | -44.7601 | 2025-09-29 00:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| c95f49af-4c2e-3f2d-858c-b674313f39ad | -7.2211 | -44.8058 | 2025-09-29 00:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| e80049cb-9c46-3360-b39f-c6a0ec11d6df | -14.5336 | -48.4268 | 2025-09-29 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 3ba1a592-680c-3ddc-8779-4a9a0e51388a | -20.0698 | -41.3189 | 2025-09-29 00:50:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 59.0 |
| 84ce7277-7728-31a9-a23a-3fd36ae127e5 | -4.6969 | -41.9987 | 2025-09-29 00:50:00 | GOES-19 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 46.5 |
| 919ae397-049f-38d6-b5d0-ad07ebec476f | -2.5957 | -48.4141 | 2025-09-29 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| aec3f94c-1598-31d2-9397-f27cf3bd014e | -4.6971 | -41.9748 | 2025-09-29 00:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 39a6fe03-8199-3ec5-9a31-5f03cb911e2c | -7.2402 | -44.7812 | 2025-09-29 00:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 155.9 |
| c7e78c09-e372-38cc-b3d4-869aea58de1f | -15.2897 | -49.4813 | 2025-09-29 00:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 1b2a515b-4e33-3b42-bdde-896d2fa74937 | -17.0938 | -48.5699 | 2025-09-29 00:50:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 7fcb3fdd-c55c-3a83-8e61-b15bb8d9fd4e | -4.7159 | -41.9736 | 2025-09-29 00:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| b3ac794e-59a3-3cc2-b006-375628f49aee | -9.4007 | -54.6984 | 2025-09-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ad46e75c-73f2-3d7b-a881-d2901b498ef2 | -4.7157 | -41.9974 | 2025-09-29 00:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| d0200ac8-58b7-32b5-99fe-863e9cfbfdda | -14.5526 | -48.4461 | 2025-09-29 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 8fbd1820-e70b-3a3f-a52c-bb47de052392 | -2.5772 | -48.4146 | 2025-09-29 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| e754e76f-8a26-3d5d-9b89-3fa71a89e045 | -9.4194 | -54.697 | 2025-09-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0c0fbe34-94b1-379e-8b73-4c7fa1792940 | -20.0491 | -41.3251 | 2025-09-29 00:50:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.8 |
| 02fbcd03-4360-39f7-9f08-3df0f70dffcd | -3.1013 | -47.0082 | 2025-09-29 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 57fb3b8f-af06-3c3d-8f8a-ce88fceb7498 | -7.2211 | -44.8058 | 2025-09-29 00:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| a89ee4ae-9f4e-3c58-95bd-7a0f47d2fda3 | -15.2893 | -49.5035 | 2025-09-29 00:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 172.8 |
| d5fb2eb2-5006-3d47-928b-d99d3e52d6c8 | -3.1012 | -47.0301 | 2025-09-29 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 01f89281-cb76-3611-9fe2-f6df852d96bf | -4.4013 | -44.0755 | 2025-09-29 00:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 80ed4d37-1992-326c-a0c1-b8cd27613436 | -20.0482 | -41.351 | 2025-09-29 00:50:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| 4b967380-3542-36de-893a-c7286425d313 | -14.553 | -48.4237 | 2025-09-29 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ea9e3fda-e393-3c13-961e-33dad0d4e0d1 | -7.2214 | -44.783 | 2025-09-29 00:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 228.7 |
| f635d810-443a-3a84-b7be-f0dac6817e6f | -2.5773 | -48.3931 | 2025-09-29 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 961ff0cc-94c4-3d81-b548-f01c495c385b | -7.2399 | -44.8041 | 2025-09-29 00:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9517182b-b77a-375e-a80d-d1ca0614f121 | -12.6913 | -46.8934 | 2025-09-29 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b54b7e0a-cbfb-3339-8e78-16f2dbc71325 | -4.6971 | -41.9748 | 2025-09-29 01:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 117.4 |
| ff2c7835-b61c-34c7-92ae-617dd1f51804 | -14.553 | -48.4237 | 2025-09-29 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 5727384e-cbc8-34de-a583-927dcc273d72 | -14.5526 | -48.4461 | 2025-09-29 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 10563c37-7c39-3304-9272-1c17d4b420c9 | -17.0938 | -48.5699 | 2025-09-29 01:00:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ffe5fad2-ad92-3be7-a726-36a904b87cf6 | -2.5773 | -48.3931 | 2025-09-29 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 7ac325bf-1b68-330b-80cd-dc8cf3fc9488 | -4.6969 | -41.9987 | 2025-09-29 01:00:00 | GOES-19 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 42853833-dd50-3efc-8adb-be1ec430be23 | -10.8238 | -45.407 | 2025-09-29 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c1b5031a-c960-372e-9ab3-7b8d6c1dc270 | -14.5336 | -48.4268 | 2025-09-29 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 165.2 |
| d261ae20-ec67-3a2f-b0eb-ad59c8a4b3af | -9.4007 | -54.6984 | 2025-09-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bb749ce3-9595-38d5-a904-654117a22251 | -20.0482 | -41.351 | 2025-09-29 01:00:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| 513d51bc-07fb-326a-aa6d-97c807682682 | -3.1012 | -47.0301 | 2025-09-29 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| bff3e7bc-ef51-3b83-b4ea-cb7cbec8b2c0 | -7.2211 | -44.8058 | 2025-09-29 01:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a477c980-a000-3b0d-8571-be9d30d145af | -7.2402 | -44.7812 | 2025-09-29 01:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 035285f6-18ba-35e3-8eff-ab707def930f | -14.5331 | -48.4491 | 2025-09-29 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 5c248bd0-0d19-3258-89e0-0836915bab64 | -9.4194 | -54.697 | 2025-09-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2e71fd20-8551-32bb-8761-5f0ecdf560b9 | -20.0491 | -41.3251 | 2025-09-29 01:00:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 168.9 |
| a070cf1e-ddad-3b82-9b40-17df9fa9dcae | -2.5772 | -48.4146 | 2025-09-29 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| d67ee1ad-75c4-3b77-8348-798596301d28 | -4.7157 | -41.9974 | 2025-09-29 01:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 086cd3b5-cee4-3b58-a199-a8ce96f50088 | -4.4013 | -44.0755 | 2025-09-29 01:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 1969de78-e599-30c2-be0d-db39d5f9c9e3 | -4.7159 | -41.9736 | 2025-09-29 01:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| b40bebef-f8b4-36a1-ac4f-e77ef3c9259e | -3.1013 | -47.0082 | 2025-09-29 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| a4b9e1ca-1b29-3919-8051-c3ec34c3400d | -10.8429 | -45.4044 | 2025-09-29 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 6244ed87-6c93-3111-82d3-0f6a423bfe5c | -20.0698 | -41.3189 | 2025-09-29 01:00:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 89.1 |
| 82ec1d17-5b8e-37d2-9cc2-62a4ce8f920b | -7.2214 | -44.783 | 2025-09-29 01:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 254.9 |
| a8534846-eacf-3fa6-bddd-bdf38553718c | -15.2893 | -49.5035 | 2025-09-29 01:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 4f847260-3144-3c22-a54b-576095c8ffc8 | -2.5772 | -48.4146 | 2025-09-29 01:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| d8d3e9a9-bd63-38dd-9a86-b787affb1c91 | -4.4013 | -44.0755 | 2025-09-29 01:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ad377c59-ec44-3a75-8611-1270a43f48f5 | -7.2214 | -44.783 | 2025-09-29 01:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 7cf66d05-8430-39b1-9b5e-867fad4d0750 | -3.1012 | -47.0301 | 2025-09-29 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c2d8261f-8866-3353-9083-78060eee32f3 | -10.0528 | -50.2192 | 2025-09-29 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |


[Clique aqui para ver as próximas entradas](README3.md)
