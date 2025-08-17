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
| c8226999-619d-38f2-9c0b-41d37936ff41 | -9.64079 | -50.8923 | 2025-08-17 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 985ad6d0-9eb4-344e-bed5-7ad774da6a57 | -10.11698 | -57.76328 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48450496-55ba-3f2f-b97a-b9c9aa6f27c5 | -9.50264 | -60.55685 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5110a270-4abb-3091-86c2-cc33263fed17 | -9.28125 | -57.79923 | 2025-08-17 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 760551c0-aeb7-3a52-b916-81f7897349ab | -9.51541 | -60.5263 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5c76d829-0d10-3609-8213-84d81b2fad68 | -10.30424 | -54.14407 | 2025-08-17 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7ff1cea-e43d-35e3-a2a4-75aa2ee7f928 | -9.19104 | -59.65148 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f0f9b42-afd6-38f9-9780-62c57c275ef8 | -13.87506 | -45.55189 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f43d6604-a46d-3d0a-889f-1e9dd7ec1b6f | -14.18316 | -45.32196 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 758bada5-48b7-3d84-ab8b-7b179ef2b0c3 | -8.99614 | -60.4977 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca71f612-bcd7-3728-9bbc-060886da9041 | -8.98929 | -60.51171 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 642f31a1-be5a-3aa2-939e-579f462242f8 | -14.18965 | -45.32278 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7cba0a6-132e-3662-bfcd-356f69d00cbb | -8.98322 | -60.54853 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b9d2653-c3f7-31a9-ac01-d7ff49d949c6 | -8.1144 | -61.19311 | 2025-08-17 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73425915-611e-36d2-9fed-face6472dc2e | -10.82614 | -45.3343 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4860ac8c-f509-3bb2-ac5b-5fd5980f334b | -12.14043 | -47.91957 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ec5a80f-ea48-3038-badd-ee21db563a7a | -12.14159 | -47.91039 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1db8d62-8f18-38c8-8198-1226174c9e5f | -9.60869 | -65.37 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1993172f-7ba1-349c-ba2e-db8c487710e9 | -9.5087 | -60.52048 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4c5bcf3-137b-35db-aec5-22311d4cefc9 | -12.88985 | -46.12516 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88c34ca0-69e1-3f35-9ba8-57e63178ad85 | -9.18026 | -59.64986 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e5c8d344-8b7a-3fa2-a93e-eb042e19d004 | -10.86133 | -48.47336 | 2025-08-17 05:06:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d52e1eda-5ba8-3447-ab72-468d38360214 | -13.87565 | -45.54644 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1d08275-5f9c-36a4-8452-d23840447e43 | -9.16646 | -59.62223 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee576b4c-dbbe-3d02-9fad-f21aa1accb74 | -10.83414 | -45.32041 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7f181c5-b553-36d8-bb2c-1aa6d0e95d7f | -8.80945 | -52.02986 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ec55a40a-7dc0-30ec-865b-c4f1147f1646 | -10.36272 | -64.50615 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9828a4d4-4650-31e4-8bda-77b590ceb265 | -10.84159 | -45.3112 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06b41339-7d72-3641-8b88-bcd77e84324e | -9.14124 | -58.2976 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d303379d-3eab-32d2-9ce7-f917334cad79 | -8.79826 | -52.07161 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe0afd52-31ff-309a-82b8-b8eb36d4586f | -13.62946 | -46.91032 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b21ca249-594a-382d-b5e6-b6516bf56820 | -8.98399 | -60.5439 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60aa6c0e-4570-3130-a346-289d4baf7e70 | -10.84363 | -45.34671 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a8fa8867-959e-319d-89c7-2a507d7cb54c | -12.83975 | -46.02179 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d702e06-d071-3a8a-837e-17dac976a4f8 | -11.88774 | -50.94669 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5abb7c78-7c73-3439-9f7c-ab3741196e2f | -13.61977 | -47.75948 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c63f9a1-4549-337e-ad7d-0ba98710358c | -12.12022 | -47.90658 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b66580fe-8207-316f-be07-9f05b9f0457e | -8.98779 | -60.49738 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9be0a406-5770-338e-be85-a65068f82028 | -9.1622 | -59.62574 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3322ecd5-f542-37e8-be87-0ba9aca0e087 | -9.86059 | -65.26362 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6789878a-0258-3c30-8231-26ddf710f8a6 | -8.99155 | -60.49798 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 657ac1da-d9a1-3710-85f5-d5c90cc8f14d | -13.61258 | -46.90229 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c13aa391-d355-3324-83b2-bc5dd045fea9 | -13.61505 | -47.75178 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a9df27f-7d66-31df-a4ca-ba6b7289965e | -9.51088 | -60.55357 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 73fd36f7-915f-3448-a8d3-070b681140b8 | -8.8997 | -60.74598 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dc2abb9-f342-39bd-bdf2-c2067c45d56f | -8.9923 | -60.51688 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52d0c1a1-3d17-3495-9ae4-b5efcfbe166e | -9.16784 | -59.61401 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37703c94-9f87-32ea-8a5f-2c7c83d3597e | -13.58588 | -46.98093 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b712b285-6950-3663-a9ff-eca9e68620ba | -9.51689 | -60.54055 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| acf78c0a-f71e-34c1-a329-45a53b50d9b9 | -13.42881 | -57.0325 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f7271d4-d67a-39cf-a21f-d09dcffa7a6b | -10.84897 | -45.34269 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbcfea0f-79e3-3567-a294-93e141045d03 | -9.17989 | -59.69656 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b1ed75a-c7cd-3612-8efe-0d7344486e95 | -13.62891 | -46.91064 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b929725d-3108-3688-bee4-a2c953bcad3f | -10.86679 | -48.47109 | 2025-08-17 05:06:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b65e3708-e47b-3996-95b9-d0b59adb5d08 | -13.00578 | -56.86656 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96f444ae-56ac-30da-9a3d-26ec18bbe68d | -9.22459 | -59.64875 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00356722-5009-3304-87ee-b25dd903ebfa | -9.21589 | -59.63457 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf62ea9a-73f7-31a8-a5ba-31f661794f7b | -13.44585 | -45.88322 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 799c4cf4-466f-3fb2-aff4-fd2f9cb9132b | -10.43251 | -60.29209 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c5f32ff-85a9-3859-ad93-ae9cf12d206c | -13.56704 | -46.99099 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85b50e84-08ed-3adf-9253-c1fff5a762c3 | -13.60691 | -46.89999 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4b772f9f-e44f-3947-a174-65dbcccb4ea2 | -11.42969 | -52.21981 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 587a62e1-f2b7-395c-9a0f-327885e721c8 | -9.63285 | -63.09583 | 2025-08-17 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78886cc5-7122-3133-a11d-c183a8066ee5 | -14.59981 | -47.95599 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9572cbd2-7733-3d74-b44e-20499e626334 | -13.43322 | -57.02592 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 277a42d3-0983-3dba-a0a5-c33af12f1935 | -11.56539 | -47.2639 | 2025-08-17 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2026911f-9d48-3996-9ad6-fd4f5dbcb211 | -13.09404 | -56.17412 | 2025-08-17 05:06:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a3bf910-bcc4-3dd1-93cb-335028ad428b | -10.31243 | -54.16162 | 2025-08-17 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 14deba15-88ab-3f24-ac8c-c6e6ae3b67fd | -9.19511 | -59.62683 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 18991944-70bf-30d9-ba79-af93e2e4ec00 | -13.4364 | -56.93902 | 2025-08-17 05:06:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1ff95e4-ae8d-3b38-b210-f219f92695df | -12.55718 | -46.94132 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6ab2a7e-5831-3d92-ac2b-51bc061100ca | -10.32007 | -54.15874 | 2025-08-17 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ddb6a76e-a330-3862-925a-d2050c34261a | -9.15642 | -59.61633 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7da96ef-b36e-3a00-8a4b-4e79614d261f | -13.59122 | -47.76357 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3ac708e-0427-3f34-b772-89f8aabe98b7 | -9.38831 | -60.54409 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa7696c7-84a2-3988-9166-39b72f6ca0ca | -8.97501 | -60.50462 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 82e14f6c-b779-3b92-9130-ea0d8d4d8f6f | -14.19555 | -45.3292 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9509c9b-202e-3050-a2ab-d6c000177c32 | -9.19869 | -59.62741 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 79e21eb3-4a3f-3e06-94df-84a32020db11 | -8.87839 | -50.8513 | 2025-08-17 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5480dfaf-feb1-3ae5-a31a-1b7c0db27ba0 | -9.50639 | -60.55748 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55f89504-e2a1-3374-b95e-cf0a009c8138 | -13.42604 | -57.02841 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b52962df-1cef-3c7d-81fa-d5f077f20b51 | -11.36723 | -55.42052 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 864e3657-cb22-37f4-a4f9-e2f069ae3bdb | -11.37402 | -55.42155 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 430f2309-6faa-3f62-96cd-9577a9bb9f25 | -13.44118 | -45.88232 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9eb434cc-a363-356c-be50-cc89d8209824 | -9.19784 | -59.69959 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9beedc6-c9b5-3bf6-9422-850e220c35e5 | -11.37062 | -55.42104 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 757d3970-12dd-37aa-ba41-1c0f9d1f7c7c | -10.8664 | -48.47414 | 2025-08-17 05:06:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc70fb7a-a9bf-342b-8700-7c2f1427791e | -12.89093 | -46.1251 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09256c32-1a76-3391-a580-14fdc24c10be | -9.51239 | -60.54446 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0b55e26-3d65-38f6-93cf-7802cb785b84 | -13.56452 | -46.96073 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2adf0e8a-94a2-337e-951b-90c5f335ec65 | -12.89541 | -46.13042 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6005054-6c02-33df-88cb-876bd7baf6bb | -12.61506 | -46.90626 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e48865c-2d23-3d20-872b-07c9cb85506d | -13.43384 | -45.89153 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2014d128-27ac-3998-ba97-82c88264a127 | -9.16578 | -59.62635 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 248d69f7-8b61-3ebe-9956-f4ed5680bb13 | -10.01334 | -59.22237 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80f6afd1-d01d-36c4-be1a-754dbe6d3af9 | -10.83474 | -45.31543 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 383665f8-57a9-3719-893d-c07d32115f2d | -7.42149 | -60.59538 | 2025-08-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4892e821-7e92-346a-b34a-f58a0a0ca96f | -12.13546 | -47.91568 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34bceee7-7dcc-3223-ae4b-8397bd31b8b4 | -13.60387 | -47.75131 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5cfd74a0-cbeb-38ef-ab39-49027a2050a3 | -8.99443 | -60.53035 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README30.md)
