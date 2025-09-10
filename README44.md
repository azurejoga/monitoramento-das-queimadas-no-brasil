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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b93ff7a4-49d3-3921-85ce-fdf6fd7083dc | -17.32406 | -46.7 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab633f73-c82d-3c04-8d9f-06987df03d37 | -17.74524 | -44.48743 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dfffdf6-11fc-399b-a86c-2c2d8b71cfe3 | -11.14608 | -48.35704 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ee5ecd3-1699-3db7-a04e-06ebc10cd15e | -13.01856 | -48.04098 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7005ee6f-38b3-3ef5-a325-e54495a0adf0 | -10.74393 | -48.18218 | 2025-09-10 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 455a9c23-88cf-30f0-9a13-0ada28ffd33d | -15.51741 | -46.98032 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2a4e476-8bd5-3df8-8d53-aea1840969d1 | -12.4123 | -43.21148 | 2025-09-10 04:17:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ebb85329-ceab-3b5c-877e-6a316591dc73 | -14.61775 | -46.35715 | 2025-09-10 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd1da33e-eff2-3b27-9cc8-7440bb9e883c | -11.45651 | -43.62044 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dfc0a740-cf0f-30eb-b9e0-f6d8c8d79333 | -11.45542 | -43.62752 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec1b9c7d-5efd-3a85-8816-5351d9be3946 | -11.44012 | -43.683 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a4f2290-2126-3a4a-a864-c1bb0f3aeec2 | -15.0205 | -49.25593 | 2025-09-10 04:17:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c164046f-9e5e-3eac-8615-0e0952ee4a1d | -11.56753 | -44.65609 | 2025-09-10 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5546332-aeed-3663-a6b8-310e105ab3a2 | -10.5844 | -52.04585 | 2025-09-10 04:17:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7777e94a-9b3a-38af-9e06-f5f39d3c90eb | -11.94116 | -51.07613 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae9d44e2-b76b-309e-80c0-0622e7fb3927 | -16.58104 | -49.2203 | 2025-09-10 04:17:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7000bc3-4fda-306c-9c91-12df0aa4eb9d | -11.45373 | -43.61638 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dbd73781-d8c8-3a3d-ad3c-f3ff475d0abb | -22.03106 | -42.89385 | 2025-09-10 04:17:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 3ed01a1f-4af9-3512-a1a8-5fd4faf89730 | -11.67456 | -46.89818 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c82b9c38-42a8-3b36-a265-4b70c1b93285 | -22.16053 | -47.682 | 2025-09-10 04:17:00 | NOAA-21 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1892c5d8-cc22-3ceb-be2b-6bcca6a27f84 | -11.73008 | -46.70384 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ddf88e1-cdc9-39c4-8bba-cc52c110968d | -20.94453 | -45.79904 | 2025-09-10 04:17:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e41d224-d41f-3dc1-a1f0-ac1ba371acf1 | -13.54225 | -44.13802 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ab1fb62-fb2b-3bf7-8cee-67edee99a6f0 | -17.72098 | -44.49858 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddafc9ed-3eab-3cc7-ba92-673d9c2a039d | -14.35475 | -47.31039 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7ceeeed-35ed-3952-9afb-5c59f89bef59 | -10.01515 | -51.69825 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 65169872-977d-3704-8b51-b91f10bd3918 | -14.37193 | -47.31358 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6eec5f76-65df-36ac-95bd-9a26c17a3883 | -10.01701 | -51.68802 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae1851a2-57e8-3911-b8ab-cf0155d5c415 | -13.19091 | -45.27937 | 2025-09-10 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac18ad9c-1b29-3d33-a3a9-82c6fe36b6f5 | -16.31252 | -42.9881 | 2025-09-10 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5423aea-5df9-3a0f-97d0-9ef723c863af | -15.27414 | -53.78445 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e8b55f6-7fe7-35d5-9903-6044f40b5063 | -13.76379 | -43.97883 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b92ba89e-73d7-3a7f-9c5b-c63a505d757c | -21.75934 | -45.36428 | 2025-09-10 04:17:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3ab7f050-50c2-32eb-b859-39ad5e35194d | -23.37087 | -45.38027 | 2025-09-10 04:17:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7823f022-8edf-3522-8d09-1c66610312ab | -12.83121 | -52.9418 | 2025-09-10 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9219c2a0-ae60-3425-b468-37cada6a5a16 | -23.29743 | -45.47464 | 2025-09-10 04:17:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ceb65d07-0972-3e87-b044-ec510a192948 | -11.44878 | -43.62647 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8a861615-83c2-3c6e-9a20-50c9bf801cb0 | -21.02693 | -48.41688 | 2025-09-10 04:17:00 | NOAA-21 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0a8a86b-bc52-34fd-be13-2b630ad08993 | -15.26103 | -53.7725 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86434bb9-f15f-3bce-8e20-fb669a8e2ea8 | -15.80304 | -52.25401 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f23237a-e233-3fe9-9a75-d899a39daa14 | -14.55567 | -48.75179 | 2025-09-10 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8b67c94-abf1-38c7-91b9-efe21961e2c8 | -12.19175 | -53.86647 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b807d42d-55bc-3e88-9721-8096183379c6 | -10.63949 | -48.6185 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0a322bd-fe96-3dfe-b6d5-7b8ca36133b3 | -14.38918 | -47.31638 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c1337eb-18f8-3c6d-8545-bad446105529 | -9.75765 | -51.05788 | 2025-09-10 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 96ce1cfc-7760-3f84-aa05-e437108f6451 | -14.88839 | -55.8632 | 2025-09-10 04:17:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5f95ac6-c03b-3d12-9412-7f85a287468a | -23.25171 | -45.97277 | 2025-09-10 04:17:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c14e60b2-f007-3355-bdc6-9330ac441a0e | -16.57659 | -49.22421 | 2025-09-10 04:17:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f81765e-8efb-3dde-97e4-042d3f794117 | -13.92988 | -48.25517 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 822920a2-0717-35c1-9f65-59fc12023b4f | -16.98673 | -44.06919 | 2025-09-10 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cfd5e43-a4c3-3df3-a639-19ad567cea51 | -15.02425 | -49.25661 | 2025-09-10 04:17:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f28b25b7-35fa-3b0f-91e8-217693877ad0 | -13.93991 | -48.26174 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f6c48a6e-5a75-3499-a786-c5b6422e42bc | -16.05637 | -49.97007 | 2025-09-10 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d35e77c-fa24-3c75-ba35-a30784cd699c | -15.51591 | -52.76774 | 2025-09-10 04:17:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd11c048-5a58-3ebf-9808-ba18ae51759d | -23.30026 | -45.47908 | 2025-09-10 04:17:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8feb5752-ea79-3ff2-b4ad-eaba79de6cd7 | -11.299 | -41.03435 | 2025-09-10 04:17:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3161ba31-0e7a-3445-ba18-1f1474c33fc8 | -12.8665 | -47.96596 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed03d84a-7878-3a32-932e-3f22ce909b06 | -15.25609 | -53.77137 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ce280c9-62d8-33f4-9f7f-cbd386015503 | -12.99696 | -48.03687 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48213c4e-5c2f-30b1-bd59-d4170747506e | -20.53714 | -47.61203 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7697f8f3-e65e-34f3-bfee-477c2972bd06 | -12.88084 | -47.96877 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 502161af-14a9-3d4c-a9c2-25a8899f195e | -20.9412 | -45.79849 | 2025-09-10 04:17:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0340f9e1-5e59-3e24-b040-1e9c59d27742 | -15.95318 | -48.10817 | 2025-09-10 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90ec8831-b500-3ad8-8acc-9b4af386e0a6 | -15.95084 | -48.10664 | 2025-09-10 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4eaf9d1d-1047-3055-b406-b2d0191b5258 | -14.60102 | -46.33955 | 2025-09-10 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82d0c30a-eb8b-3419-9ced-a7b78bb940c7 | -11.32013 | -46.52541 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fb1dab1-f5f2-37e5-8527-198b2b56c40b | -17.25195 | -46.08544 | 2025-09-10 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d999fb8-2d87-349d-ab25-2130f7e61ef3 | -21.92528 | -45.64212 | 2025-09-10 04:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f16dbb04-e34c-3474-812b-d4921afd8894 | -10.57642 | -52.02951 | 2025-09-10 04:17:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 19c56939-33eb-3adb-8b68-2260dcc6914c | -20.52865 | -47.62201 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d025b976-6820-340c-bc41-de74838c773b | -23.41258 | -46.50376 | 2025-09-10 04:17:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b82ea4cb-6c16-3b3c-834b-4ea327a3a609 | -15.22202 | -44.03864 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 974d29f8-d415-3ca6-95a1-4c214ecc6bfe | -14.33596 | -47.30016 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9af126fe-ca7a-3e73-821b-fc12f213b7c5 | -23.36117 | -47.19293 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cbbfce26-d13d-3c5c-b1f6-84d35e8729cd | -23.32214 | -46.87427 | 2025-09-10 04:17:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 9b213b68-6e0d-32b2-b0d0-36b91cdb0c33 | -10.16073 | -48.87931 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6fa03432-e56f-3a16-9f75-81f0a7fcc710 | -11.41926 | -43.57493 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8615a626-1607-3c4d-9ce0-ef6ad29654f3 | -13.977 | -48.2271 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c2050d29-e6f1-3855-919f-99283a3b715f | -22.87388 | -48.13544 | 2025-09-10 04:17:00 | NOAA-21 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca366b39-e12f-3c71-bf99-e743babb2cee | -15.22592 | -44.03551 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31c33a2e-8f47-361c-a5fa-65747bcbbcac | -10.18236 | -46.21947 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1d42081-bd95-3169-b9c1-c5e3c62e521c | -15.09508 | -50.08573 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b51a12d7-467b-30b0-aadf-32e369c321b4 | -20.38425 | -46.63268 | 2025-09-10 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 97f9b2f6-1f85-3553-81fa-991491456baa | -16.8886 | -45.75842 | 2025-09-10 04:17:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97d8ab17-458d-32e4-94ff-bd9600ec1759 | -17.33286 | -46.70907 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0895185-43d6-3ab6-bccb-2e3708552c27 | -16.63001 | -51.82458 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c810eb26-0738-3663-8a09-2c02e5a5a8e1 | -11.46206 | -43.62856 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 025252a5-0cb1-322c-84cf-e36b491b5f9e | -10.6544 | -48.6127 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9adc2d96-86b2-3430-bf84-db6a531a5cae | -9.99499 | -51.70097 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f037faa5-3144-386e-9fb4-8789e8c5fd33 | -21.50681 | -44.7895 | 2025-09-10 04:17:00 | NOAA-21 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 31c43e3c-4266-33f1-be0b-79e7c508f7d0 | -10.04315 | -49.16184 | 2025-09-10 04:17:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e6eb1fd-8781-3e5e-af49-d13036a951f3 | -20.16328 | -47.69494 | 2025-09-10 04:17:00 | NOAA-21 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf623c30-dcd1-38b4-8c49-4354dc912188 | -14.90411 | -50.11564 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91f7ebb4-7a03-3f0c-b631-65a38ba1e149 | -15.48068 | -49.38455 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 282c1a50-548b-3095-862d-dc185bdee60d | -15.85095 | -48.00277 | 2025-09-10 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1168bec5-d672-33e9-a671-bfe3fda0575c | -13.0079 | -45.20962 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c877e47-58af-372e-9c5f-8fd110da7676 | -17.73797 | -44.49005 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c50e769-f1f8-3bd6-a58a-0ff681c37ef1 | -23.03299 | -50.0992 | 2025-09-10 04:17:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 19fefd88-39ab-3537-859a-7a123c0e5a00 | -10.16078 | -48.87593 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e75d4551-c587-3d57-98ac-aa58587ad5a5 | -15.00509 | -48.02126 | 2025-09-10 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README45.md)
