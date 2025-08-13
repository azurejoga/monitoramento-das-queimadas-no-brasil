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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74682bad-159a-3f34-bd7b-26ea05c01250 | -9.05577 | -60.64742 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd6c170a-4d91-38dd-856d-796ac5c04635 | -9.18284 | -59.67387 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bae91b75-81d3-3806-888c-3574db110806 | -14.61089 | -59.67616 | 2025-08-13 05:08:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffa078b3-dea9-3220-8daa-bb336ccaccd4 | -10.96767 | -49.56853 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 68666247-189f-3edc-82b0-4bd10ceee0bd | -9.70364 | -56.09365 | 2025-08-13 05:08:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f75a661-6552-37fd-a2d8-bc4a098166fb | -16.31571 | -52.91299 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b1795b36-aa9a-3469-9483-1d5fb8c1fe90 | -12.57442 | -47.06013 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 728272a1-d9b4-336c-ab4c-3fb8965b9eaa | -9.18793 | -59.66586 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd031b90-db23-3f1e-a980-af04539b7e1d | -16.87157 | -52.16401 | 2025-08-13 05:08:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b43bf784-76dc-330e-bc20-24f293b59389 | -8.93395 | -60.73053 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09dc0467-b2e4-31d1-a26a-a76374a61745 | -12.57523 | -46.98114 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 264f1c8a-e44e-33d6-a57d-a34d75d89b15 | -16.30229 | -52.92127 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e69a911f-4420-30ea-9491-0490e9aee568 | -9.19301 | -59.65788 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 28737a24-906d-3b5d-8387-ba4fc5a9a250 | -16.30852 | -52.91387 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21974d69-c7c7-39cd-868b-ab638306f701 | -16.50952 | -47.84978 | 2025-08-13 05:08:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 600e980e-1fa5-3381-8e6e-361e3e3a91a3 | -10.05025 | -59.35885 | 2025-08-13 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2886aa19-57e4-32ce-8117-ccfcad327bda | -9.05801 | -60.65786 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d0ce025f-e6f1-36d1-8d3b-4b39be1fe3e2 | -12.67344 | -46.9668 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e48c68f0-dae3-3edd-ae9d-5b0316450978 | -8.93347 | -60.73214 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb46788b-774f-379c-826b-0ab3e740cbcc | -10.33857 | -64.46982 | 2025-08-13 05:08:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d4cbd23-4382-31c1-afb3-4f390d506376 | -12.58902 | -46.98474 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cacce336-ebda-3e58-900a-1cce544197d1 | -10.75283 | -69.08266 | 2025-08-13 05:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3552c865-485d-3f9d-af7b-f09847da6b68 | -11.9013 | -52.53355 | 2025-08-13 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed5b6ac8-cc72-3f14-8cf8-f4b34931cf81 | -16.30318 | -52.92341 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13398cac-8035-39cf-affb-29b0125796fe | -9.06113 | -60.6455 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d956b87-8ba0-3619-9f97-1e56abd85617 | -16.3103 | -52.92256 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e17ab5b6-aacb-3491-8d33-716af9d3e5bb | -11.54689 | -61.02462 | 2025-08-13 05:08:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 243b3521-6d01-3842-9b0f-be972c8e7c35 | -9.0635 | -60.64882 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b82a86bb-3169-3aa8-9646-465e8c804fd8 | -15.60525 | -48.2396 | 2025-08-13 05:08:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc9066a2-eb23-3d3d-81d5-5a0a55e965b1 | -9.18356 | -59.66956 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7ffcf9f-7b1d-3344-a7b4-6f69453ffa84 | -9.92674 | -65.2377 | 2025-08-13 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 767a530b-2c36-354d-a509-9a86479e35a9 | -12.58084 | -46.98235 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 601ae3e9-b68a-3afe-a5fc-4eb906fba2bf | -12.47175 | -46.96371 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5807ef9-ed74-3dad-b2a6-62c1af060866 | -10.96633 | -49.56511 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d1d1de1-68e5-3cb0-a461-0f4e1a285799 | -10.75931 | -69.08395 | 2025-08-13 05:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65723077-76c8-3238-babc-d36cda642491 | -15.08927 | -51.35762 | 2025-08-13 05:08:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e033e1b9-6026-36c6-820d-585ca802bd0d | -12.32212 | -46.06356 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b35836a-f359-3594-a2c9-f665aef668c0 | -9.06332 | -60.65588 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ba729581-1b0b-3203-9fa4-1f43682df0a2 | -10.34766 | -57.5976 | 2025-08-13 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8070641a-dd74-36b0-9359-8b3e7aeebeee | -12.49467 | -55.76101 | 2025-08-13 05:08:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8324d1f9-5885-3b72-9d31-547af148e32d | -11.63857 | -50.14605 | 2025-08-13 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00f8aa6d-1ceb-3407-8c64-983e20f7daa0 | -10.33594 | -64.47079 | 2025-08-13 05:08:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56a5f5c0-cede-317b-9f51-f96a6a6cc257 | -16.3943 | -50.8872 | 2025-08-13 05:08:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c09926c-b9b1-304f-950a-b31411972f20 | -9.17186 | -59.67206 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecc9bcca-df9e-3751-bf86-a1cd1f6707b6 | -9.82721 | -60.75975 | 2025-08-13 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfd3a822-0a81-3f33-914d-3ee32918c82e | -12.51919 | -46.96859 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 284c5b40-4e69-3e0c-8b48-8a94937040ea | -12.3281 | -46.06438 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b30423e-88d8-3634-9673-86d816cef09c | -9.50865 | -62.37354 | 2025-08-13 05:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62cf79a8-677a-3dd3-96bd-78a62227fcfa | -18.5499 | -46.0606 | 2025-08-13 05:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 729dd0fb-4486-3182-83e2-37de1b8a0163 | -18.5505 | -46.0369 | 2025-08-13 05:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 28ed348c-efaf-3735-8b50-77c7fc92710b | -2.9108 | -48.254 | 2025-08-13 05:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 987abe4c-9fe0-3bfa-bffb-02e37079a176 | -2.8923 | -48.2546 | 2025-08-13 05:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f68ca10f-cc98-30fc-9e2c-5ae0fe4dbd4f | -16.3153 | -52.9201 | 2025-08-13 05:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 946326f1-1957-3707-97d3-4804771af9d2 | -20.88757 | -55.90865 | 2025-08-13 05:10:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff50a38f-c725-3524-a5a4-de6075e9bb74 | -18.54507 | -46.06137 | 2025-08-13 05:10:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2dca3d63-2046-3f9e-b95f-fde470e50fb3 | -19.29698 | -48.42928 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db96c218-cd98-302d-8a46-6ad0d13b00f4 | -22.38225 | -45.46812 | 2025-08-13 05:10:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 904ff9a8-9636-3bec-b332-ce8a7af5cd13 | -19.87499 | -46.39481 | 2025-08-13 05:10:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 093e0013-ae44-3d1f-83fa-9d42f5fee32c | -18.86176 | -47.26883 | 2025-08-13 05:10:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d29486cc-182c-3dd8-834f-b6e3c583c3e3 | -19.29657 | -48.43313 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d1cb7b2-97dd-34dd-b1a8-47010e449768 | -21.75851 | -46.58971 | 2025-08-13 05:10:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9570f939-87c4-35dc-84d2-3b79ed884880 | -18.88088 | -48.31577 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d3ef5b6-3f8f-3ddf-86c2-a2d395dd635b | -22.3882 | -45.48153 | 2025-08-13 05:10:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c00fe67c-66b6-3ee1-93c2-12dd676f640b | -20.14111 | -57.0658 | 2025-08-13 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f25da28-b174-386a-a51f-7cb92537bc83 | -19.2996 | -48.43158 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab53f8aa-9df2-33d4-8f9a-d70a3955e15a | -22.38172 | -45.47285 | 2025-08-13 05:10:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1d2a4d36-956d-3d74-a8d9-4733c66b7e1c | -19.00252 | -57.62363 | 2025-08-13 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 0def463f-4cdf-39d1-9667-442511b9a253 | -22.38817 | -45.4801 | 2025-08-13 05:10:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 51cdbce4-0109-3332-b7aa-6da4471f7dee | -19.8859 | -44.61289 | 2025-08-13 05:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 64780703-cfc4-3a40-b2cd-0edd63aebc87 | -18.92132 | -48.22393 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b34c2493-6a9a-3ca1-94da-018855ca8186 | -18.05626 | -51.2986 | 2025-08-13 05:10:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a7cbbff-fbb8-3625-83c7-7725e248b109 | -19.8789 | -44.61104 | 2025-08-13 05:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4ae897b1-d8d0-393f-9afd-9470ca5ebbf9 | -19.08061 | -48.15123 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 185b26a0-aaaa-34e5-a105-49d7c4367d0a | -20.09134 | -47.44446 | 2025-08-13 05:10:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42d18a11-4418-389f-86da-cdfe31b3b79e | -18.54556 | -46.05577 | 2025-08-13 05:10:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| aa78ff95-74e5-3366-936e-d7fc770bab0b | -18.87807 | -48.31357 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed1c6c37-c51a-3600-9ca9-02f9df1b1c03 | -22.38214 | -45.46681 | 2025-08-13 05:10:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0d9de3f1-ff53-3374-a93c-9c1358b7af99 | -20.09089 | -47.44925 | 2025-08-13 05:10:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8197dc5-5c04-3db9-9bbf-d5cad71906b0 | -18.91606 | -48.21925 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb0eed35-9c23-3924-a3ba-5c90bee3c760 | -18.88129 | -48.31194 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab19532e-b05c-3eb2-ab8c-578ce8048f55 | -23.86317 | -55.43438 | 2025-08-13 05:10:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 302aaad3-021d-3b86-a1bd-1b0113ec143b | -23.75456 | -55.416 | 2025-08-13 05:10:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 468d03d6-5109-3a2f-9a43-566bd2e45328 | -20.47663 | -53.67519 | 2025-08-13 05:10:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69fd3f4e-036d-3ff5-936d-1c69070d5945 | -18.91567 | -48.22312 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fceb566d-6737-3592-b5bb-a55b3fed9880 | -18.86558 | -47.26808 | 2025-08-13 05:10:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca171267-4103-3274-b891-cde751c95da7 | -22.38868 | -45.47514 | 2025-08-13 05:10:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 613279b3-67a1-3e58-bdd9-e7514f3012ec | -18.92171 | -48.22002 | 2025-08-13 05:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9ade294-a350-3e6a-b589-f24a53ca920c | -18.86775 | -47.26982 | 2025-08-13 05:10:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6eb8dc51-8302-35cf-b996-295aa255b413 | -2.8923 | -48.2546 | 2025-08-13 05:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2ecdcf30-746e-3d3f-8a05-ce5756cc94f3 | -2.9108 | -48.254 | 2025-08-13 05:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 819fcf12-0424-3f9c-8844-54c9159febbc | 2.89687 | -60.2938 | 2025-08-13 05:25:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39438057-47bf-3ada-85df-659878447128 | 2.89633 | -60.29037 | 2025-08-13 05:25:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 646331d0-4cb7-32b3-9dc8-c0e2de60df7c | -7.13284 | -60.1228 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3bcc7ea9-0775-3927-92b0-38f6699fbe27 | -7.13631 | -60.12334 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4422d800-329e-3766-8491-bba0404a5079 | -6.89695 | -59.13021 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 48a5e2fb-b522-388a-bc04-97a6f30ed100 | -7.1369 | -60.11951 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb1665dc-7259-3ba3-ac79-a9f44a872454 | -6.09631 | -59.9353 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 684be25e-1719-3877-8396-3bb2308f76a2 | -6.09343 | -59.93095 | 2025-08-13 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 008fad16-5683-3ecd-85ab-66a71fa17bb3 | -6.90419 | -59.1313 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9feeab6c-d4ca-35df-9689-36bc80cb331e | -7.13225 | -60.12662 | 2025-08-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README30.md)
