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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d220c3b-27d0-32b6-8811-183f4a5dd908 | -9.07887 | -50.60386 | 2026-06-10 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdc4e361-75ab-3f79-8544-759071ef0117 | -6.19387 | -45.16646 | 2026-06-10 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9493863-d0df-37da-a233-d54e9a1f10dd | -9.31513 | -48.97057 | 2026-06-10 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 777934c7-bc44-3a72-9198-d66f8838b3a0 | -3.8053 | -49.18327 | 2026-06-10 04:29:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f9d7f4b-bd4f-3488-b721-28ffa222b329 | -7.22286 | -34.82492 | 2026-06-10 04:29:00 | NPP-375D | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7825d24a-58b0-3c0a-adfa-7f3fb5e5121b | -9.75137 | -47.87831 | 2026-06-10 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ea4afac-0243-3d66-9562-eb4a6fecaebe | -6.39576 | -44.17119 | 2026-06-10 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 61041e90-7974-321d-bdca-1587addc8ee8 | -3.80128 | -49.18263 | 2026-06-10 04:29:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c84a6f8-3065-3b16-8648-4d7a981b1ce1 | -9.30487 | -45.47049 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71715e7f-3c8e-3f14-aa6a-6a0b7a4ff5bd | -5.82762 | -43.59039 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 93347988-0665-32b4-a229-d3bd3848bed4 | -7.1457 | -44.06417 | 2026-06-10 04:29:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35f00ab9-7b4f-34f7-a5a7-1e703a75f527 | -9.70122 | -48.61202 | 2026-06-10 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e31ba86-d1b6-326c-9107-af93b009f15d | -5.93478 | -43.48561 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6f72999c-a93a-3eb3-84a0-2467784148b4 | -7.22233 | -34.82894 | 2026-06-10 04:29:00 | NPP-375D | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 37fee4ae-2bb0-30b9-a21e-d473a70a2ca2 | -5.94098 | -43.46818 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb9b2632-a004-3101-821c-880871830085 | -9.30764 | -45.47452 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 90d2ceed-aac3-3e11-b0ed-3ade03b4c7ba | -9.31097 | -45.47506 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e08a677d-4327-3566-bff1-35c358cfd2dd | -9.34173 | -51.89001 | 2026-06-10 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8e4373f-2918-353d-b130-29bce4bd477f | -7.1625 | -44.06679 | 2026-06-10 04:29:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd93c513-f8c3-388b-8431-dde6718a3e56 | -5.3039 | -47.2444 | 2026-06-10 04:29:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19900112-80f0-30cd-b1b6-1ca066463030 | -5.72804 | -49.10201 | 2026-06-10 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf322080-015c-3dc0-b56f-ac4f51a195ad | -7.35661 | -50.81355 | 2026-06-10 04:29:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cbbe307-b1d3-37a7-9928-1761aa90fd11 | -9.30431 | -45.47399 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a3312f5a-0bec-3fab-9b24-69cd0d1457a7 | -9.07482 | -50.60315 | 2026-06-10 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bc010ab-8eaa-3a24-97ab-298bf1cf9b28 | -5.83099 | -43.59091 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 26a608cf-0236-3a90-9fd3-da5c4a2ef8f1 | -8.31963 | -45.39172 | 2026-06-10 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6b1b451-479b-3fb5-bc09-060bdcea5f26 | -9.29876 | -45.46592 | 2026-06-10 04:29:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e14d1256-e778-3805-a8c3-f52a2e560f14 | -10.01018 | -48.21401 | 2026-06-10 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31d2beec-f55c-387a-9403-a3f622481a85 | -8.97295 | -47.98079 | 2026-06-10 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8aea8876-948e-3398-b62e-8b1a55001710 | -6.39131 | -44.17768 | 2026-06-10 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa70bb83-6b01-3dc5-8bfb-438bd3f1a0c7 | -9.31264 | -45.48609 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 91d1cd0c-758a-3b9f-8dc4-88172e1aa4b2 | -9.30154 | -45.46996 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b93e61eb-3cdb-36d4-87bf-73fe43cf48c3 | -7.1653 | -44.07086 | 2026-06-10 04:29:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53422552-ddea-3f55-ae4e-955bea77b764 | -8.29701 | -48.2278 | 2026-06-10 04:29:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eba58f13-b46d-363a-aae1-b50edd73ee39 | -9.31374 | -45.47909 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 78734e7a-0ed5-3dee-b560-960d054463d6 | -9.62389 | -49.02334 | 2026-06-10 04:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebc85326-0a1c-3ed2-8112-5698ed81b3c0 | -9.31072 | -48.97429 | 2026-06-10 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76b64161-458a-3b17-b866-7f20c7efd310 | -6.43928 | -44.57916 | 2026-06-10 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3972cab-5de7-3a45-8ad3-44ddfca26ae4 | -9.26123 | -50.12606 | 2026-06-10 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f4badfe-bf18-3c69-9156-103ba054e5a8 | -9.14124 | -47.98758 | 2026-06-10 04:29:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d73113ee-4a35-3677-9538-7091f122fe01 | -9.30986 | -45.48206 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f602ebd6-13b4-3c59-aae7-8254b48eeb0b | -7.10222 | -46.51571 | 2026-06-10 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 988b2e26-b91d-37e3-b564-d7cd0264dc91 | -6.73595 | -44.36809 | 2026-06-10 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52adcfc6-702c-371d-aec7-ce272a61d497 | -5.60991 | -37.53304 | 2026-06-10 04:29:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c3d2bb2b-e6fc-319e-8fd5-111146161ca9 | -5.83436 | -43.59143 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 270dbe26-6e0c-3848-ac3c-e7d993b8564c | -7.16585 | -44.06732 | 2026-06-10 04:29:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd6ce424-cf4f-3de2-8099-fd1f1c9bbaaa | -9.30709 | -45.47802 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f9963804-02bc-3807-84d4-151a73db33a1 | -6.39521 | -44.17469 | 2026-06-10 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ac96d42-f21e-3ee4-8ebc-776660304a01 | -9.77103 | -49.74631 | 2026-06-10 04:29:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cc346cc-3f17-3199-b431-e5121abfc2dd | -5.82818 | -43.58683 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3dd6de52-e812-397f-918f-8555913cbfc5 | -9.41322 | -44.69429 | 2026-06-10 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b18ca63-91e1-3521-8695-8964e3f98224 | -7.19522 | -47.08718 | 2026-06-10 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b110b475-1f15-324f-9512-cb8cec60a512 | -8.9951 | -45.73595 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95cb9c21-d951-3733-b993-680572104788 | -7.20962 | -44.10675 | 2026-06-10 04:29:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cae21ef4-9a9a-3a2d-9ee6-fce5b00b57fb | -9.14577 | -47.98418 | 2026-06-10 04:29:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15658123-59a5-3f18-99f2-d92f9565c3a3 | -9.3048 | -45.4581 | 2026-06-10 04:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| bed1a958-840c-3f4c-9cf3-7c91cc6e7e7b | -9.3234 | -45.4787 | 2026-06-10 04:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 49b1b77b-98b4-37f6-869f-d8f8f2a8955f | -9.3045 | -45.4809 | 2026-06-10 04:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| ef467a93-80de-3e49-b3e9-385ed2f4704f | -14.37173 | -45.55872 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea6f9705-e6e3-3c4b-8acf-0644142f09b9 | -18.45227 | -40.34635 | 2026-06-10 04:32:00 | NPP-375D | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7b83a98e-7e5e-3719-b8b0-e082d4da48d3 | -13.90244 | -51.82685 | 2026-06-10 04:32:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7c6050c-ebb9-34e4-bcf3-8963897a3e7d | -13.76884 | -47.11048 | 2026-06-10 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 687761d8-df0d-30b4-b6ad-43a52120e2dd | -11.33742 | -51.40225 | 2026-06-10 04:32:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c659249-d896-370f-86e2-4bd8debe146e | -12.039 | -47.329 | 2026-06-10 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70d56b0f-c74c-3076-84e2-8940a516bb5f | -11.37907 | -47.82022 | 2026-06-10 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c6cc7f6-54b6-3d16-9945-f3b66a2f337e | -11.64669 | -52.8655 | 2026-06-10 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30162250-39e6-385b-b20b-b448969a87fd | -15.1814 | -43.85563 | 2026-06-10 04:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ece9624-982a-39e1-947d-5b26b5a909c9 | -14.41753 | -45.58059 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84bba2a8-820e-3ed7-bdb8-3c62126cff93 | -14.35151 | -45.53292 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c010b4b-0c1d-3873-b748-d45b3fef6c4b | -14.13162 | -49.8503 | 2026-06-10 04:32:00 | NPP-375D | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4e52f0a-2586-33a7-bcf8-117b04c10551 | -10.85068 | -53.74182 | 2026-06-10 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 554cd4fa-332e-382d-824e-1acf93318b24 | -12.85292 | -44.36969 | 2026-06-10 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2d5c9218-4ab8-34cd-9b0b-0875f778d3a1 | -11.65089 | -52.86325 | 2026-06-10 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b002e3e-bd89-3a97-846c-44f2d909d294 | -12.05408 | -49.76183 | 2026-06-10 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b972dfc9-0094-3bf0-b599-0f2b66ea22cd | -12.77752 | -46.81867 | 2026-06-10 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2eece97d-b892-30b7-877b-2e09c4518fd3 | -17.45314 | -47.18827 | 2026-06-10 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b94fe49d-971c-30bd-ac7c-75383327f184 | -15.17481 | -43.85028 | 2026-06-10 04:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2f0c941-f213-3856-9793-4ecaa95d6a24 | -16.8094 | -43.66801 | 2026-06-10 04:32:00 | NPP-375D | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfb1f46f-4193-3e1e-b195-be485786885e | -14.64847 | -47.99668 | 2026-06-10 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b36c809-9788-3b87-b036-4dcfceb05835 | -13.41552 | -43.73516 | 2026-06-10 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1929e8d5-1af8-3bde-8521-bc5396c3aec3 | -16.83749 | -49.29641 | 2026-06-10 04:32:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee028338-0ad7-3a46-a5d0-86c9041369e8 | -14.62034 | -47.9994 | 2026-06-10 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11849b59-fc8d-3f6c-a6a8-058d4a8df398 | -12.85234 | -44.37351 | 2026-06-10 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fc370297-fdbb-399c-88c5-8981f5225d06 | -14.36444 | -45.53876 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45fd96c1-f340-3ad8-8df4-1321c58933a4 | -13.96286 | -46.18882 | 2026-06-10 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c1cad91-269d-3ff6-b4a3-29aa67d04ec7 | -11.38311 | -47.81706 | 2026-06-10 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5131ffcc-b272-3dec-8b4a-4923e0eeead8 | -14.3987 | -45.56308 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a166fab4-4e69-3cf9-b8da-66a5d80ec737 | -15.75005 | -43.30729 | 2026-06-10 04:32:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15f27d71-0050-3546-b394-c9ce00c8ab23 | -15.43305 | -46.33883 | 2026-06-10 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c59620b-7708-3b05-8e66-a2455fec5b64 | -14.41416 | -45.58005 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16c3476a-0432-373e-b557-8377548cb224 | -10.18714 | -49.59633 | 2026-06-10 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4b30a6d-2521-35d3-a844-fada6a3656d2 | -12.85077 | -44.37229 | 2026-06-10 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 91dfe644-d377-3114-9c91-ebabe159483c | -10.51302 | -51.94308 | 2026-06-10 04:32:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c14b513e-7c9a-33f6-910c-450547f2260c | -16.80965 | -41.86108 | 2026-06-10 04:32:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f1d45f38-1513-3b79-b1d3-9149a2b90783 | -11.47173 | -47.33957 | 2026-06-10 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6390e1f2-74d8-3373-b69f-ba6b458a8187 | -18.45388 | -40.35043 | 2026-06-10 04:32:00 | NPP-375D | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c4c51f7c-4c3a-3561-93d2-469e83adf0f9 | -16.81003 | -43.66351 | 2026-06-10 04:32:00 | NPP-375D | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 415c0335-a3b9-3a6d-996b-c7a8dc6d7f7c | -13.95897 | -46.19184 | 2026-06-10 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e549a810-c7e2-30f7-94c4-d2405cd89da7 | -13.26714 | -45.57687 | 2026-06-10 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04ef2a6a-e785-3d2e-8556-69220102b1a7 | -14.69405 | -48.31581 | 2026-06-10 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README8.md)
