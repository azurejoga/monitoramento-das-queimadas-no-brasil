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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b43f3c3-d16f-39b7-a28b-98a80a50020f | -12.85417 | -52.82246 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f3fc306-507a-3b8e-9a60-37294923e2d4 | -14.19702 | -54.42646 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 50bf4d10-0ef5-3c2f-a13b-d68d25238364 | -12.86354 | -52.82759 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4258e598-17f5-317e-b1ca-c2b074a25a32 | -12.5878 | -46.93179 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b355fa1-8169-330b-ad2a-f446680d917c | -11.19176 | -54.90224 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cb7b0f8b-9551-3c22-ad3e-890577d6081e | -14.26353 | -45.2947 | 2026-08-05 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 095fc6ca-e449-3d46-80dc-4d153bea5a46 | -14.18728 | -54.44365 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b74416d0-fa77-31f5-9de5-8bcfc9254914 | -11.17464 | -54.87444 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 640214c3-6326-38da-aef1-77da071f6d45 | -11.25014 | -54.83707 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d792f759-0fd3-30f7-93ff-fa202e0c466a | -11.20324 | -54.85461 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1861336b-ae6a-381f-a5e1-a375260c27e1 | -14.26156 | -45.30264 | 2026-08-05 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d160ceec-2bdc-335a-91ba-256ebc53bb13 | -11.92124 | -55.91153 | 2026-08-05 04:49:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccdc50ff-9440-3668-a3e5-d8cc71559c10 | -11.34345 | -62.21431 | 2026-08-05 04:49:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7fb9e623-6842-39ee-b8d8-190b658cc711 | -11.17616 | -54.8871 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4732c73-406a-30ef-be47-0f2ec7c27d5e | -14.19522 | -54.43752 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| de40b78b-71ec-3ed7-9064-d6dd50bfd93c | -16.92467 | -44.90609 | 2026-08-05 04:49:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc33711d-39e8-38ed-be37-80a09b3c5025 | -11.18824 | -54.90163 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87101374-4837-3994-a3ff-4caadeb306a3 | -12.59817 | -46.9175 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a4d3a88-a93b-30f1-86b7-614deb32a795 | -11.19136 | -54.86088 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2181f83-923e-3481-9ba5-8b93cae15a88 | -12.89581 | -52.84004 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 017995d8-6999-3f8f-abed-f6fba959040e | -17.45127 | -47.86604 | 2026-08-05 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a161b9c-0c04-301a-beab-a6f8c6eba333 | -13.43729 | -43.67651 | 2026-08-05 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f2a6aa20-72ab-3354-8458-42622d7bf7d1 | -11.21357 | -54.90181 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a98d2baf-677f-3bd0-99c6-7c646e2c0cce | -11.17415 | -54.89924 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17b7b157-1bc8-3a4f-a11c-7aa98ed8f35d | -15.4404 | -41.38393 | 2026-08-05 04:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 518c3c7f-4dc0-3d8a-af1c-5bd7dbed1e0f | -11.19615 | -54.91964 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a121e3f-2def-3149-b786-776872319b85 | -13.44243 | -43.85376 | 2026-08-05 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fd2593b-90c1-30b8-a808-46a9ca51ef2b | -12.59453 | -46.94474 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e11f290-9824-3161-99e8-fd208b30acef | -17.45544 | -47.86664 | 2026-08-05 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcaf6113-f1e1-34a3-9ece-f013a2909e00 | -11.1832 | -54.88832 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f6b563e-6715-326d-b6ed-9d258c8c78b4 | -13.44214 | -43.68052 | 2026-08-05 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1e55fa26-d02c-306c-b44c-1cd5c6bc9718 | -11.24933 | -54.83784 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e636d370-fef9-3472-b79a-3e52efc22896 | -11.16407 | -54.87271 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f825b577-73b2-3994-a13f-1fc37b050890 | -11.18186 | -54.8964 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60db7caa-f73e-34c2-b757-d2c83bb390af | -11.18053 | -54.90448 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adeda656-8e2b-33d3-9ba2-3a3bda949c60 | -12.58467 | -46.95526 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f4f5b2e-0c56-3907-8847-2597c0e13189 | -11.17549 | -54.89115 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99a70772-c575-3bac-9f18-f973e14bac30 | -12.4498 | -50.37611 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32ca0295-9b01-3ef1-8a78-22a89b7bf173 | -11.17112 | -54.87386 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dab2afbd-73bc-3a0b-a8b3-da3d5a6a8499 | -11.18204 | -54.91721 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 78616e32-81da-3ece-89f7-82cb4ba3e533 | -12.60336 | -46.91039 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5e80795-e11d-396f-ae2e-b5393f1170b9 | -11.20387 | -54.91676 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30ac2cee-3cea-34e0-b884-f2e6d29d992a | -11.18338 | -54.90911 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 15f337b8-1fef-3368-9cc5-83a6469eec29 | -12.59137 | -46.93678 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd8a2d26-8434-3422-800f-7d41c16e07ac | -17.33243 | -42.63122 | 2026-08-05 04:49:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 83900d73-4566-39af-82ab-5368bfd44b8f | -14.17246 | -54.40687 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be0f8906-cdd8-344a-ade6-b9474907a6dd | -11.18624 | -54.91375 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5c3e973d-cc87-3354-92c8-20320ded7f72 | -12.00741 | -49.2677 | 2026-08-05 04:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69ed7a3e-1a98-3f0c-bb1a-e3ff01c2afac | -11.20101 | -54.91211 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fea1757-186d-3c3d-ae88-33d2ec393458 | -11.16559 | -54.88531 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f87dab46-b7c8-3179-8398-e967288a5850 | -12.88313 | -52.83436 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e597f19-662a-3b88-9b1e-25f86bbbacfb | -11.19488 | -54.86147 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f74d1f8-f60d-3b2d-9809-16bd8668c3e7 | -11.20234 | -54.90403 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2554efc5-7868-352f-8310-fb6b3e63ef67 | -11.19815 | -54.90749 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9d2f7cc-2ad4-3955-8e8e-a4a1395b8994 | -11.16912 | -54.88589 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0d3366d-7cd3-337b-ad4a-dd97d348532b | -15.14394 | -42.15847 | 2026-08-05 04:49:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7fc3d0d6-a32c-3cee-a306-3d5571d8cb42 | -11.20034 | -54.91616 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e76a48f-c11b-3c66-9d8e-ba2375b48b90 | -11.16759 | -54.87328 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 157ad7eb-773b-3b8f-8d03-c602911dcd69 | -11.19396 | -54.91093 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10e293b3-22c6-3560-9cf6-4da99c2bed78 | -11.18102 | -54.87965 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a05769f-92f0-3157-acaf-c849651b16e4 | -14.03042 | -54.08915 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b6cf569-c629-3845-a74f-47d39edea7ee | -11.19376 | -54.89016 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e57f8eb-5ff3-30c3-a0cf-c8b2017536aa | -11.16507 | -54.91023 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| cdceb6fb-9a83-3cd1-8b01-4ec09557e52a | -11.16642 | -54.90211 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 50028b34-e2a8-3f20-9b82-bc4c19b06187 | -13.44293 | -43.67385 | 2026-08-05 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a688585d-2447-3362-b230-1367ebf09a25 | -11.19024 | -54.88954 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f4ed384-8405-3a79-ab09-ae247bb91146 | -12.59501 | -46.94114 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8d1f44e-a8d9-3b78-aa36-9669a73d9d0f | -11.18605 | -54.89296 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19ff562b-57bc-3d85-bd56-ae0042cd500f | -11.17145 | -54.91545 | 2026-08-05 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b3108a07-910d-30b2-a8c3-eadc24ed4a2c | -12.32902 | -48.54334 | 2026-08-05 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d48ed87e-5b8c-39bb-890f-0784773b8386 | -12.59922 | -46.90966 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b086d08e-3a65-371c-b37b-a27b8e3840f4 | -11.16693 | -54.87729 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b9091a3-9ada-356c-846d-0f31ece33862 | -12.60228 | -46.91845 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc49e8c9-885d-3739-b6fb-28de76d13f74 | -11.18035 | -54.88368 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0ce9cc3-277b-32d1-9692-4ae6a57040ce | -11.17213 | -54.9114 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d041ba7f-bb9a-38ae-adc1-c88d97557d4c | -11.17178 | -54.86986 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c1415b0-6d19-3497-887f-68e275ee2071 | -11.18168 | -54.87564 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc9fc58e-1015-3b1b-9d6f-f3255aff716c | -12.87954 | -52.83382 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88fadb74-e95c-3469-a11a-f4edc87ed07f | -11.2272 | -54.86277 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d7f9a71-b46c-302e-a7fe-a58d8deae9de | -17.99251 | -47.15365 | 2026-08-05 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6acdb8f6-a150-3b48-9c9c-3b51d60f96f6 | -11.34391 | -62.21812 | 2026-08-05 04:49:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 26336f82-3eec-3433-9cef-8044cf56a894 | -11.24145 | -54.04006 | 2026-08-05 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e50f6176-94f1-37f7-98f9-6b2b6a1b0097 | -11.18071 | -54.9253 | 2026-08-05 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04f09e19-03e8-3745-bb86-72f91b8cb2c9 | -11.18234 | -54.87165 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23e8ba2c-c14f-37c9-a101-6518c039aae9 | -12.88009 | -52.8303 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 407fcf4f-6f13-3368-8498-427f8c88bb06 | -11.21643 | -54.90645 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 54e89fac-6135-3af5-8f4c-c4729c1b8bd4 | -11.21159 | -54.91391 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3205cb5-1ed5-3213-a49c-af9ef9326d01 | -14.19642 | -54.43015 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 18650f4d-50f0-3e9e-99aa-ad7e8ea9523d | -12.43632 | -50.51395 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24b41301-bc09-3a6c-9aab-ccefbc1d6e43 | -14.19582 | -54.43384 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| daeffa30-500c-33df-9e43-8c295dc5cd81 | -11.2019 | -54.8974 | 2026-08-05 04:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9d73f893-992e-3668-a240-e13ebfd86670 | -11.1642 | -54.9007 | 2026-08-05 04:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 298e959a-75fa-34c5-b5ca-890bf965330d | -11.183 | -54.8991 | 2026-08-05 04:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7e05547d-208a-37c8-a2a6-836e7e21225b | -11.1828 | -54.9194 | 2026-08-05 04:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6f2da8ca-3663-3f44-824c-368dc4cf2e0e | -11.2017 | -54.9178 | 2026-08-05 04:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| fb3cfd33-afd6-36bf-b4d7-b40645acefb4 | -20.90612 | -44.08035 | 2026-08-05 04:51:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 17f0b7d7-71dc-37e6-8dd1-1eb4a0af8e76 | -20.90996 | -44.08386 | 2026-08-05 04:51:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5d968dba-410e-39b9-9ab4-88f2434f04db | -19.16232 | -47.32036 | 2026-08-05 04:51:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb2a56a2-a5fd-30ae-af81-c7407a18be8f | -20.3869 | -49.30883 | 2026-08-05 04:51:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 124f007f-6fca-3e25-892d-63b51bf051b8 | -21.67597 | -47.82335 | 2026-08-05 04:51:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README19.md)
