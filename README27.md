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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24f9f74b-73e3-3931-9fc4-49ee55b6b816 | -12.3921 | -51.015499 | 2024-10-03 01:03:46 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79887cc9-0cea-3e25-9da3-eddd7181e56f | -12.3937 | -51.022598 | 2024-10-03 01:03:46 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7bc54abd-431e-303b-910e-4f94218c19f0 | -12.1594 | -50.049099 | 2024-10-03 01:03:46 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5220a2a4-d599-3f7d-b598-a9bb77f6b5ca | -12.1611 | -50.0564 | 2024-10-03 01:03:46 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c6a3a85-7167-3e7e-b572-7b11746d03de | -12.1628 | -50.063702 | 2024-10-03 01:03:46 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e054f0d2-6ba7-3a84-9d14-2f3590227eb3 | -12.1479 | -50.044201 | 2024-10-03 01:03:46 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99561109-b1a3-32b3-88cc-5406a81a7381 | -12.1496 | -50.051498 | 2024-10-03 01:03:46 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90c4d8e1-1c27-3cd8-937d-cfabf2f4e1fd | -11.2648 | -46.903999 | 2024-10-03 01:03:48 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12294dc4-2570-3693-b668-b51b00f730c2 | -11.2673 | -46.9142 | 2024-10-03 01:03:48 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45485abe-ae3c-32d7-af30-a506879fe34d | -10.6526 | -44.488499 | 2024-10-03 01:03:49 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6066efb4-810d-30b8-8d98-52207c6c7e96 | -10.6564 | -44.503399 | 2024-10-03 01:03:49 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c88b40b-043f-37aa-83ed-f981769f425d | -11.2551 | -46.906399 | 2024-10-03 01:03:49 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab622dc2-2dd0-3f96-8af9-d7b5d2c6f078 | -11.2576 | -46.916599 | 2024-10-03 01:03:49 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39040128-b92e-3c10-8140-870b3c92a15a | -11.2601 | -46.926899 | 2024-10-03 01:03:49 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 607c64ea-872f-36bf-aa2b-0fa324c6a334 | -11.2428 | -46.898499 | 2024-10-03 01:03:49 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b931c9a-6cb8-3245-92a9-ca979153edb4 | -11.2453 | -46.908798 | 2024-10-03 01:03:49 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 930232f6-850e-37c6-b1ea-1b0e0fcc42fc | -11.2478 | -46.919102 | 2024-10-03 01:03:49 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e97acbd-7f73-3f9a-8d71-527708b28fe1 | -11.2503 | -46.929298 | 2024-10-03 01:03:49 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb174abd-2c0d-3647-9174-e89ac7111a5c | -11.9724 | -50.177601 | 2024-10-03 01:03:50 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc3f9739-c76a-3668-9964-b6b33081be9b | -11.9741 | -50.184898 | 2024-10-03 01:03:50 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 687a5452-c811-38c0-845d-966e69047f8c | -11.9444 | -50.146 | 2024-10-03 01:03:50 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e966ed75-f550-3d52-8ff9-ea7f05903386 | -11.9461 | -50.153301 | 2024-10-03 01:03:50 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e25c95a-7539-30a8-9314-4d1ab1b77f23 | -11.9478 | -50.1605 | 2024-10-03 01:03:50 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e90d3fe-e071-3826-ab9c-299f17c7abf7 | -11.9347 | -50.1483 | 2024-10-03 01:03:50 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d6ca2f1-c228-319a-b3b0-0a405aac5c2e | -11.9363 | -50.155602 | 2024-10-03 01:03:50 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68e57764-661c-348f-bb6f-d0d2290dd990 | -11.938 | -50.1628 | 2024-10-03 01:03:50 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43afca69-d3ce-3fdc-9633-9a0e724332b5 | -12.5898 | -53.1399 | 2024-10-03 01:03:50 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edee9806-33ae-315c-8770-0999a419f4c4 | -9.4509 | -40.356998 | 2024-10-03 01:03:51 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2e3ebcf5-d854-3739-904a-f875c1a3bd68 | -9.4589 | -40.3867 | 2024-10-03 01:03:51 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1c16f9e7-ed76-3714-98ec-2a83b2774fab | -9.4413 | -40.3596 | 2024-10-03 01:03:51 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ea42edff-a2bd-307e-bd04-d3968c1f9b8a | -9.4493 | -40.389301 | 2024-10-03 01:03:51 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cb74b26a-d232-33e5-a1c4-7237279f153e | -12.58 | -53.142101 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 782b60db-84b0-3d69-b263-da2085a42e73 | -12.567 | -53.129398 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c49613c5-a13f-3600-b3cf-947a2e68a0f3 | -12.5686 | -53.136799 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 249e90d2-9b33-3a05-a364-3dcf03abed47 | -12.5572 | -53.131599 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 347a8dd7-8c91-399b-a9c9-c627216b8c51 | -12.5588 | -53.139 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa792631-e91f-3fdd-971d-61e3a3c918b6 | -12.5604 | -53.1464 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d77f4687-34b0-3ab1-aa9b-74f2e9e4a112 | -12.5409 | -53.104301 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d443933-1a90-38e2-9a9d-424e750adad7 | -12.5425 | -53.111698 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff4fb79d-6e68-3215-9bc2-a3c398178477 | -12.5441 | -53.119099 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| feb6774b-4280-3a41-9792-c7543a4428be | -12.5474 | -53.133801 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93931cdb-b65d-35a5-90b0-d7fcddab5815 | -12.549 | -53.141201 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec0bb77f-bc58-383d-82bf-3353e7341b42 | -12.5295 | -53.099201 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 123a2c1b-1e34-31e5-90ae-d2826c477f3c | -12.5311 | -53.106499 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5a2c4bf-7cfa-3725-9a18-02ac3cdcbf89 | -12.5327 | -53.113899 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a87ae64-1f1c-34af-b52d-4bd972259f97 | -12.5343 | -53.1213 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a59a6806-a7fa-3f0f-8a3f-a94bfde8d404 | -12.6049 | -53.4897 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bf5304c-905d-3e7b-84af-2696dcc62e65 | -12.6065 | -53.497299 | 2024-10-03 01:03:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5ace976-cd5d-3cf4-8895-2e320c10966f | -10.9115 | -46.3074 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9092beb2-c4d2-341d-bf67-217599ed807c | -10.9143 | -46.3186 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4e222c3-3fa0-3793-b198-d6deb8b4ad51 | -10.9689 | -46.540199 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 982297ed-7348-3bf4-bd62-9ad5e241da09 | -10.9716 | -46.551102 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24cc63eb-a9fe-3544-9d6b-2060079f0943 | -12.531 | -53.246399 | 2024-10-03 01:03:52 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7db99225-a4da-30cd-bd11-fbafdd9e8e10 | -12.5326 | -53.253799 | 2024-10-03 01:03:52 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01e9713a-2178-34dd-9225-e4b5782b9967 | -10.9017 | -46.309898 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8ec9c9a-d5a1-340a-ae40-0264817aead6 | -10.9045 | -46.321098 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 832b0321-15de-3efb-9dc9-28da3faaf98e | -10.9592 | -46.542702 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0cbcfff-3400-3685-8d56-8463d1cd2f46 | -10.9618 | -46.5536 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d48bcc5-bba6-32da-8e4c-eff9f42fc7af | -10.9645 | -46.564499 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85a5e92a-1d28-3a7e-8fb2-3f5fb45880f5 | -12.4968 | -53.137501 | 2024-10-03 01:03:52 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 696e169e-f9fe-334e-88e2-724f7769bdc0 | -12.4984 | -53.144798 | 2024-10-03 01:03:52 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7a4b59-746a-3acc-8c63-63e572212271 | -10.945 | -46.569302 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a71b4866-9ec7-35fe-a039-860a23371e03 | -10.9477 | -46.5802 | 2024-10-03 01:03:52 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf8c7b17-c51e-3f6c-a376-5d0437f29cce | -12.4821 | -53.163898 | 2024-10-03 01:03:52 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8a3889d-a45a-3ee3-be42-3033fee11f79 | -12.4838 | -53.171299 | 2024-10-03 01:03:52 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 644488f1-e000-3dfb-8a7c-c946448dbf5d | -12.4854 | -53.178699 | 2024-10-03 01:03:52 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1f754b2-407c-3db1-b416-fa2721bf902b | -13.7376 | -48.151402 | 2024-10-03 01:03:53 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f1e8e48c-2466-3924-8a32-262510fa8a0c | -13.7396 | -48.159698 | 2024-10-03 01:03:53 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fdfda42f-1c65-37af-95a5-d937670ac82f | -13.7455 | -48.314499 | 2024-10-03 01:03:53 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b98584b-0668-3817-a6e2-6a3f1e350a4c | -13.7474 | -48.322701 | 2024-10-03 01:03:53 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e8b32076-3f8a-3ed6-a044-a8582cd93418 | -13.7318 | -48.300598 | 2024-10-03 01:03:53 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b479323b-3fd7-39c0-8cdc-ee09ed0df966 | -13.7221 | -48.303001 | 2024-10-03 01:03:54 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37a71c28-4c49-3cf5-88ab-1ffe74957cf7 | -10.7203 | -46.160999 | 2024-10-03 01:03:54 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4519cf7d-9d9e-31fe-a63d-b79715611ec6 | -10.7232 | -46.1726 | 2024-10-03 01:03:54 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a1cb0d6-5fe0-37f1-a058-82e34c63bd08 | -10.726 | -46.184101 | 2024-10-03 01:03:54 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5cca85f4-26a5-33f9-945f-20d268053f60 | -10.7049 | -46.140099 | 2024-10-03 01:03:54 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be057473-ac6d-3bb5-b6aa-9994abea96c3 | -10.7135 | -46.174999 | 2024-10-03 01:03:54 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72c17284-8f58-39b9-86da-f1811c412a69 | -10.7163 | -46.1866 | 2024-10-03 01:03:54 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f108fd12-ccb8-3f8d-8e93-b9a7864b01af | -12.4545 | -53.459702 | 2024-10-03 01:03:54 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d32d7e85-68c8-39b4-962a-4ab46f4d2e65 | -10.7192 | -46.198101 | 2024-10-03 01:03:54 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9c32875-adc6-3ad7-9129-83e4bb52bd89 | -10.6922 | -46.130901 | 2024-10-03 01:03:55 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d74e4a9-8fa2-38dd-b2f8-b7eaa476b5f5 | -10.6951 | -46.142502 | 2024-10-03 01:03:55 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2341a6ff-4fbc-3a01-90d0-48989e24c3be | -10.698 | -46.154202 | 2024-10-03 01:03:55 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 42107e99-b5d9-326b-a546-e4f6bfd4360a | -13.9279 | -50.878899 | 2024-10-03 01:04:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5cb796ad-adbd-371f-9603-32de472af277 | -13.9295 | -50.885899 | 2024-10-03 01:04:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 655a647c-ccce-3d21-8b90-ec890ff296bd | -10.7447 | -47.697601 | 2024-10-03 01:04:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0eda2e26-35de-3c2a-accc-13b8aade06a6 | -10.7469 | -47.707001 | 2024-10-03 01:04:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1f5afb3-582a-3da4-bc06-ae3b8155d2ec | -10.7303 | -47.681198 | 2024-10-03 01:04:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c331103-b489-3461-9a43-eb63cf5a0c87 | -10.7349 | -47.700001 | 2024-10-03 01:04:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d12dfc98-0b3f-344e-85e2-3b87bbdfcf59 | -10.7206 | -47.683601 | 2024-10-03 01:04:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57afe6d8-72b5-3bd5-8e8a-a2ff7369aca8 | -10.7228 | -47.693001 | 2024-10-03 01:04:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21211d0b-400f-3ff8-bd35-96b48dfbd39b | -10.7251 | -47.7024 | 2024-10-03 01:04:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6350675-599a-3bee-87cb-4a3ae4beeda6 | -10.7274 | -47.7118 | 2024-10-03 01:04:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a66aa4de-f414-3c42-9c56-c54db485621b | -13.2211 | -48.630798 | 2024-10-03 01:04:03 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10b0a951-95c8-3ed9-b7d1-6b654238672b | -13.2113 | -48.633202 | 2024-10-03 01:04:03 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 53acc69b-7e30-37b9-b3d3-afa80adacb2d | -13.2132 | -48.641201 | 2024-10-03 01:04:03 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6a94ba43-67f9-3055-85e1-f0426bfde42f | -13.1842 | -48.605999 | 2024-10-03 01:04:03 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e922c21b-2dea-313d-8aef-bfd36bab8a27 | -13.1861 | -48.613998 | 2024-10-03 01:04:03 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f8e8d6a9-4be6-3536-bf47-8b22afc12dfe | -13.188 | -48.622002 | 2024-10-03 01:04:03 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4a041d71-69f7-3991-ab19-14c7fa8c684e | -13.1899 | -48.630001 | 2024-10-03 01:04:03 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README28.md)
