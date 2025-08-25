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
| 3b775a5e-08ab-36e5-94a2-6b60b8b1b8b1 | -10.39958 | -47.15788 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6573b84f-9de8-368b-9b50-42d964482b39 | -19.72606 | -48.97851 | 2025-08-25 04:17:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c65650e7-a528-3133-b604-17451c77dc4c | -20.38028 | -46.7371 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 183802e4-ee83-3325-bec3-c2648db236da | -17.18872 | -46.8392 | 2025-08-25 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b3d67b4-0a54-36fd-831e-6fa1bd83ffcd | -10.10284 | -57.76991 | 2025-08-25 04:17:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79b0e9d8-5aef-3043-b379-b6d202637c8e | -10.61845 | -55.04779 | 2025-08-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad476bd0-f798-3346-9033-8db7e3f3e365 | -10.60274 | -44.32909 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bdf74649-3959-31e8-8428-2b08e6f1b9bb | -20.6152 | -45.02327 | 2025-08-25 04:17:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 708fbf30-e5a3-3cc8-9685-713ae04bd24b | -13.49559 | -46.89107 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc5cf09c-fc84-397f-964e-a40d387d0e2c | -15.14226 | -48.64167 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7698bfe-b874-3748-ab69-a21b9b94a4a1 | -21.63265 | -44.0139 | 2025-08-25 04:17:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1f3f1482-c907-3d9a-84f9-f6318a41b0f9 | -14.37585 | -53.42023 | 2025-08-25 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc55c001-6d7b-3ee7-9fc1-5ed61b44ff96 | -14.76765 | -47.51268 | 2025-08-25 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3fc50e16-10ac-369a-82ac-1a36bec0c3b8 | -11.59096 | -46.26579 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3408deb2-1038-3154-8d8f-17e03e055cc9 | -11.18285 | -55.0182 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51fd04f8-2f17-3c90-b60b-cb549c82b5df | -21.63207 | -44.01815 | 2025-08-25 04:17:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| aeea515b-a849-3d44-8df6-96c646d63c53 | -13.62812 | -48.15574 | 2025-08-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a86b6a4-44f3-3510-aadf-abd00dbc5264 | -10.8197 | -46.38657 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b34b9e1b-2563-3022-9f64-ef3a965629a4 | -22.69531 | -47.34885 | 2025-08-25 04:17:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a08fe48a-acdb-39b3-8b03-8e94c282a360 | -10.71604 | -47.13263 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e252be3-0a80-3d2e-b7ec-b7ec15c1d470 | -11.27082 | -44.99076 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6acbe28c-3695-3c4e-960d-9d149f42500c | -11.14546 | -44.75072 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be219279-0620-3805-8ca7-dfb7e22c4aa6 | -14.2306 | -58.62612 | 2025-08-25 04:17:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3553d090-9b14-3472-90b6-4de290e0567d | -14.43148 | -56.46447 | 2025-08-25 04:17:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c93518cf-4416-3a0c-b51a-ead0da8bf741 | -12.74202 | -48.10679 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34780879-a77f-3a1c-b837-0ebdac93d6a0 | -14.43056 | -56.46886 | 2025-08-25 04:17:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 048a1ddb-a7cd-3549-b241-1680f5bd4494 | -13.44461 | -46.90184 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 152dcf43-04cd-3748-b3c4-2e6663b380da | -12.74791 | -48.11611 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7f8f85af-0b2b-3391-951a-43c6ecbeccff | -13.05756 | -46.32568 | 2025-08-25 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c72d6495-9807-372a-a3cf-2805b88f3b81 | -13.21669 | -43.14795 | 2025-08-25 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e4a35a06-e5bb-392c-8e57-6c7d45068f2d | -13.44919 | -47.02494 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1a8d877-2c3b-370c-a4da-b1fadabb9b73 | -14.09974 | -53.9915 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0dbbdd4f-2046-35df-82f4-8012a67f74ca | -21.94665 | -45.58498 | 2025-08-25 04:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc549f5e-51af-3913-8964-8befd3d9cde3 | -11.6162 | -46.23912 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 107f1f33-1ac9-3d23-ae51-0d5cef272797 | -13.28674 | -47.51017 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77218b88-fa49-3bd5-953a-391b478ba3c9 | -13.48939 | -46.88607 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 718680ea-3c3e-3b52-a468-7a0a84f158b1 | -13.50866 | -46.89712 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d84c2137-de6c-31ca-8ef0-a02c1a775e15 | -13.47477 | -46.91066 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc31b8db-f952-3360-937d-b0a7b3a19dd8 | -13.43034 | -46.90307 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e88eb62-ff5a-3749-bf6b-330d918fcf43 | -16.81917 | -49.29959 | 2025-08-25 04:17:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dce79f95-b893-33b0-b215-b05c65b7a50e | -10.60219 | -44.33258 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9ac33c78-443f-30dc-aafc-269ed22504f9 | -13.5089 | -46.91696 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daaa13db-1dca-383e-8273-79dbb42c0b1a | -20.38201 | -46.72611 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fdcf459-bd3c-32c7-a275-6bdd58b5328b | -13.46255 | -46.87814 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d2c3c9c5-f849-37ad-90ad-6aa64f5ba5bc | -16.4222 | -49.93989 | 2025-08-25 04:17:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e139b196-7f43-3ca6-853c-2a61c39e1329 | -13.45509 | -46.88074 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba3c6144-aa6b-3a76-93bc-e811efeeb5f0 | -11.60537 | -46.35229 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0ecfe355-c83d-37f3-be69-9d1ed6b5b2af | -20.29619 | -47.17958 | 2025-08-25 04:17:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a710b39-dec5-3906-95f6-5677f25bbed4 | -20.38474 | -46.73037 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc51c7dd-6ac8-35d6-83b4-33872f2c0960 | -20.11031 | -47.25673 | 2025-08-25 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 23c36b6f-815a-3b64-b463-5e90681a0725 | -20.61799 | -45.02778 | 2025-08-25 04:17:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| d1ab4538-5d24-34d3-8f2e-70487d5a98be | -10.60193 | -54.88638 | 2025-08-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b55de38b-fc66-32b5-ae0d-18e46fcdb09b | -12.74567 | -48.10731 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6f1b976-8074-312c-a606-edf3494c1c17 | -16.6373 | -49.35245 | 2025-08-25 04:17:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b212991e-d800-33d5-aaf3-6c0016152502 | -10.03095 | -45.2951 | 2025-08-25 04:17:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7378d5ed-9154-31e2-9c11-a8fa7dde6d15 | -13.48319 | -46.88108 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f8e4243-fb1a-37a4-ab1a-9d247a3baa65 | -12.41481 | -46.4939 | 2025-08-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbd48b35-9f4a-37a2-a5f8-689f2c363d38 | -10.9848 | -47.39989 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a1f561e-99f5-3a2c-bb70-49d11946a903 | -21.42342 | -47.59845 | 2025-08-25 04:17:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15b37848-42a8-33cf-87f7-af6a88ca5400 | -14.74195 | -55.93274 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28b5ab93-867c-3a76-8001-888ce67c85cd | -12.75079 | -48.12116 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9d899b39-7e68-3b10-924f-9fdcadba0254 | -11.86661 | -45.11736 | 2025-08-25 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec531c6f-ef20-378d-a095-5927b25847ba | -15.13985 | -48.63942 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc3a27c6-44fc-3d79-8ffd-4136a28d893e | -11.93056 | -46.72621 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 065b2c4b-e8bf-36a6-8312-3ad5360b938d | -21.59006 | -43.90475 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ec3cb9b-761f-3035-8c46-5e976b61dced | -11.61987 | -46.24303 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7f1896f-e1ce-3b6e-938d-60fe56341389 | -10.77606 | -46.39449 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a86613bf-de3f-3ffe-ab1e-f097b73ac46f | -13.00606 | -56.89323 | 2025-08-25 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 572e5945-641b-3893-935f-750978fa6359 | -13.61655 | -48.1801 | 2025-08-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05d5501d-7c30-3623-ae59-32cd0a2dc12b | -10.61185 | -55.05057 | 2025-08-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc1daa01-5a95-371c-9c8c-854f4fab0831 | -15.0826 | -48.68507 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82acc812-18dd-3c29-adeb-661c38da0f61 | -14.26517 | -48.04096 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b00c904a-3745-3e1f-88f3-fd5cec952ac9 | -13.43478 | -47.02665 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6df12cc0-0f58-3e1c-9a6c-d388de48d1ed | -15.65126 | -52.72291 | 2025-08-25 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8d9cce0-6493-3630-9ca0-6fada232557e | -12.74046 | -48.13775 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e91ff2ba-16db-3625-b553-fab15bb7471f | -15.0804 | -48.54605 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36e8cb2d-6515-3f14-b9d0-ad2676f7947d | -13.51144 | -46.90161 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bf02ad5-27f1-35c7-8f45-d33b7f203179 | -12.29835 | -49.14687 | 2025-08-25 04:17:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12f9f6fd-b7be-336b-9547-08b926cdb235 | -9.47232 | -57.81699 | 2025-08-25 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2fc58fd3-10e2-3f3d-81a0-8297d322b5b4 | -12.74848 | -48.13463 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23d1a7fb-be90-3f45-a4a8-2a2213690b1e | -20.98417 | -45.48478 | 2025-08-25 04:17:00 | NOAA-21 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af3e960b-7f51-39cd-bf94-721e882c2f89 | -15.04457 | -48.50883 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbfa02b0-ebdd-32f8-bdc0-fd4e62d19c1b | -11.26751 | -44.99022 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3246ebef-3a9c-32e7-905e-49077653b59d | -20.37175 | -46.76955 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 057a37b9-972d-35b1-8e05-5360e3b1109a | -11.09746 | -44.77536 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76f045e6-761a-3e8a-acd7-e7267b8a35d9 | -10.47061 | -48.32334 | 2025-08-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 990899a3-23a6-3c87-bc89-3c71c25070f8 | -21.2817 | -43.78595 | 2025-08-25 04:17:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d677dd02-3337-3337-9a54-3d3af4785d39 | -11.16967 | -55.02425 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6743f78-4cc6-339d-83f5-dc29a2b493ea | -11.63128 | -46.23727 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41e806bd-0408-3ed5-834d-5e4084c10662 | -20.3797 | -46.74077 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4e6a101-e581-36c8-9d2c-bab932950e3a | -19.7337 | -49.01812 | 2025-08-25 04:17:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5227308-c455-3849-93ec-e53a30ab8694 | -20.52839 | -41.87409 | 2025-08-25 04:17:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4340dd8d-cb47-3e2e-83d3-ef9bb4f94f1b | -12.76315 | -48.11446 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d81672b-41f7-3f73-a20a-fbdd18eb3dd4 | -20.27224 | -46.64617 | 2025-08-25 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a61b2bb4-45ea-3d84-8e35-a5949c388128 | -15.03517 | -48.52063 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1093ee2d-29f0-36c7-9a31-f2e91d40dbb4 | -11.14268 | -44.78984 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98b1b203-21f1-3ff9-aa47-5854f19a3354 | -13.65446 | -46.88639 | 2025-08-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 836f0209-cf4c-3751-bb28-109ada6974ae | -10.42962 | -47.17559 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbd14143-c9c6-3a93-9147-98accde3f1e9 | -11.91079 | -47.11533 | 2025-08-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15e5e77c-db3c-3df4-a29d-b101769482af | -13.42846 | -46.91451 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README30.md)
