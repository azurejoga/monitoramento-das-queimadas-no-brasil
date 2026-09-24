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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99e86213-3d11-3154-86c0-44785cc65f3d | -5.9433 | -44.10185 | 2026-09-24 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef19614d-e98e-3ec8-ac0f-e8930935fd11 | -8.14956 | -49.54372 | 2026-09-24 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ac31bcd-2387-3152-b5b2-4cb97180c2e1 | -8.38923 | -46.28886 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c8c44ae9-947f-36c5-8372-44c3781f9198 | -6.65271 | -43.62341 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87a5827c-4961-3200-905e-fb264f2eaada | -8.79524 | -45.64325 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2adf2cd-cfda-31ea-9e86-0c67cd1f2781 | -4.83399 | -42.89584 | 2026-09-24 04:08:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51ef014e-a9dd-3e0d-9bf5-754d178b5583 | -7.46378 | -44.57083 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bb5959b-3cc7-3140-a9b4-51cfa8cdca44 | -3.45135 | -50.09026 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43013c34-c265-347e-bd60-0217ab05a10c | -6.40207 | -46.20316 | 2026-09-24 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27747c38-a63d-3340-b1ad-f2c039799713 | -2.89411 | -54.09257 | 2026-09-24 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d31ff413-ac31-3845-8b44-e68135b191c8 | -3.44715 | -50.08295 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| afe1aaba-9ebb-31f8-8b96-51233e9995ee | -3.44825 | -50.07647 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 589dfb60-79e9-322c-8020-e7d130be0622 | -3.35535 | -43.24514 | 2026-09-24 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b943c952-0373-39e3-9022-fad6b3cf09ca | -7.0303 | -44.64962 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1f28ad3-11d0-39c8-a231-562f1605b5ab | -4.11066 | -51.07858 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b93afa69-9a6e-3c39-acde-0b6a32c089bc | -6.51459 | -52.82465 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25a0a81b-b94b-32d3-8fee-623441be1375 | -4.52457 | -44.03049 | 2026-09-24 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a93395d-d1d1-35f9-9ba0-37cdf39744de | -3.5553 | -43.46729 | 2026-09-24 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 63a4bbcf-538b-33a2-88a9-3cf2e31b3cc4 | -7.76147 | -44.81726 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6c47a4a5-78fa-3b6e-bdea-dc18c9a878fe | -6.22109 | -47.50043 | 2026-09-24 04:08:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f587d41-7abc-3602-8423-ef7bfa2a7c6b | -2.83096 | -46.70476 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a79ce1b8-a02d-350a-ab07-2c10a13cc7de | -7.67387 | -45.47659 | 2026-09-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 574da132-0d27-3bed-879b-af938bb8aaee | -2.59921 | -47.35117 | 2026-09-24 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20d051bd-aecc-3584-9734-b1ee8fb2f347 | -8.24207 | -48.21502 | 2026-09-24 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f753413b-b9f8-36e1-9a4d-3f483b9c9191 | -4.11 | -51.08236 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 43907ef6-2203-3e05-8170-bc9983081395 | -4.98974 | -45.5544 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 14d90c34-b6b0-35ee-95b6-60d73428ed47 | -5.00569 | -45.55243 | 2026-09-24 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b697d06-5a86-3b4e-91a8-f9c4d324d47b | -6.89788 | -43.63172 | 2026-09-24 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d6a8173-eefa-301d-a40b-407232a0e76f | -2.6405 | -54.69251 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 5f8e0c14-5f0e-31fc-9d96-0885303edf1b | -8.23706 | -48.21836 | 2026-09-24 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3f92056-4f44-31ef-8ccb-1250363d0a13 | -7.41887 | -49.86586 | 2026-09-24 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a7827bc-a630-3f71-b5dd-c732c891a371 | -9.47734 | -40.33771 | 2026-09-24 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e5e32f8f-6860-3779-917c-067610436a3c | -3.67027 | -39.21049 | 2026-09-24 04:08:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 36b1c38f-fb6a-3cf6-a43b-187a8a80c92f | -9.14707 | -49.95655 | 2026-09-24 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7be8b448-4c3c-3df1-958d-2be09d2ad226 | -4.11634 | -51.07898 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 90edd1d5-0976-3c7b-9217-c3c42e24227b | -4.52798 | -44.03111 | 2026-09-24 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e4ad321-8db6-3701-9dbe-1f278a3f4b24 | -2.88833 | -54.08517 | 2026-09-24 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 400d4428-eb6f-3494-9866-192388dc0f3a | -6.31763 | -43.34839 | 2026-09-24 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adacf6dc-a8fa-3a5c-8214-f9ccf6c0cfc2 | -7.47431 | -44.57256 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11337218-10bb-3a87-a085-fa19859c6abd | -7.47782 | -44.57312 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d90a00e8-db0a-34fd-b462-d403a2325a6d | -7.02966 | -44.65361 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 397a06a0-1190-3311-b522-88309455fa81 | -5.77264 | -45.10088 | 2026-09-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 3605e512-1e1f-31d4-a664-829199eafd8b | -6.43448 | -48.4655 | 2026-09-24 04:08:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ce15a66-3c30-3ffe-b553-740594525228 | -8.00004 | -45.02363 | 2026-09-24 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a498ef88-cde6-3b41-a5fe-041d357a1e48 | -6.4261 | -43.48148 | 2026-09-24 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d70243d-bd11-3ac8-bbe6-ef7878164073 | -9.26235 | -46.24889 | 2026-09-24 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 117bcaba-2dbf-3944-b892-b270ce802f96 | -6.91896 | -41.69237 | 2026-09-24 04:08:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 47506a7f-de07-3219-a1eb-16a99468004d | -6.19098 | -43.35033 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a80fb2ce-4542-30ac-be68-903d913ebca2 | -6.26783 | -43.12862 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a3a1c99-5bea-3d3d-b754-4985ee7e29bc | -7.42542 | -49.82824 | 2026-09-24 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 08345eea-af6f-3529-ab7d-95f2219e8493 | -3.45572 | -43.36524 | 2026-09-24 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bce8b048-6929-3428-8550-fc418e2d4ab7 | -2.644 | -54.69337 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 678a7109-2d42-3c41-a887-5ef5be6884fa | -5.15109 | -45.65822 | 2026-09-24 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe519300-fe53-37d4-a56f-f18bff845afb | -7.60658 | -45.3835 | 2026-09-24 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6eca6619-501c-3dbb-91bf-c8afebce90f9 | -4.4205 | -55.07985 | 2026-09-24 04:08:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2df4706-955b-37d3-8743-14a8ef7b9f11 | -9.24772 | -47.3483 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 468a4dc4-af88-37fc-a451-b01ce976e6f4 | -3.55244 | -43.46289 | 2026-09-24 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 19cdbb58-e717-3ffa-9ac1-b9333b39af54 | -8.29564 | -50.85209 | 2026-09-24 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8610dcb6-7a77-37fa-837d-34b1b09e4539 | -9.2569 | -47.34275 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66357f86-ed55-316d-a176-b628eb0ae3bb | -4.52444 | -44.03054 | 2026-09-24 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 00381d49-a601-3b11-a89e-1055358af534 | -7.67979 | -45.48615 | 2026-09-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86fb3346-00be-39ef-880d-bcad9ec856ea | -9.26535 | -46.25401 | 2026-09-24 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6fdc440d-3c40-3ded-ac3a-880edcb80c47 | -9.46704 | -40.33612 | 2026-09-24 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 330b4ee1-b131-3ca8-99be-56931dcec656 | -7.50285 | -39.27535 | 2026-09-24 04:08:00 | NOAA-21 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 94af951c-d987-34ab-856e-8ef1658f7e54 | -6.21752 | -47.49569 | 2026-09-24 04:08:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f8352db-7ed4-3f87-8b44-7d3d8542a51e | -8.08995 | -44.34217 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fe2deac-b930-3aa3-ba6e-ddd49d61b433 | -7.42288 | -47.35529 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bacac484-6f62-39bc-8909-dfcfe97ecd9a | -6.54535 | -43.09166 | 2026-09-24 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f1443b9-38f3-37e6-a84d-4e5b89d4ce54 | -7.46729 | -44.57141 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d463b255-3825-3f76-b4be-7b46ea1db7a2 | -9.23489 | -47.37511 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96aa6330-fd9f-3b79-b8e3-609a9b4249c4 | -2.39101 | -48.52533 | 2026-09-24 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab627b2c-e2f6-36a2-87da-49e5da499648 | -3.76592 | -43.40107 | 2026-09-24 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a0d552a-185e-3786-84e7-75834c834f32 | -6.45879 | -55.0031 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82760461-b47b-3d91-8338-ca233d6caddb | -2.17924 | -47.10274 | 2026-09-24 04:08:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0089967c-2e34-34fd-8c9e-82ac9c164db8 | -6.52059 | -52.82575 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 700a56ff-4e91-362a-8922-e8f7febc8d87 | -6.20904 | -47.49429 | 2026-09-24 04:08:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f3f57a3-2547-3b28-96f3-9991b3da401b | -5.19808 | -44.68734 | 2026-09-24 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9e5bd22a-8013-3ff7-a11c-c7283add0a6a | -3.95807 | -45.80949 | 2026-09-24 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d604cbc-b93d-3611-9726-c57ad8d37256 | -5.33057 | -48.98318 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a0139deb-ad1e-3d10-8048-316343a8ac9a | -4.28511 | -48.60943 | 2026-09-24 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 975ceab6-a60c-3974-81c2-8493fafb9af3 | -4.95845 | -45.14734 | 2026-09-24 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8104727b-cc60-3465-a3d3-0dac6fa7b7cb | -4.98667 | -45.54919 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3be0d1a6-5f80-344b-94af-4f365cdf2b06 | -8.12815 | -54.8149 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0eecdaf9-7ecb-3aac-a55d-8258972153d4 | -6.21132 | -43.35353 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc01a703-edf6-3dc7-a923-27322c945005 | -3.16074 | -54.60736 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 8eb102a8-a73e-31c8-8779-7dc2834447a7 | -7.61935 | -46.8052 | 2026-09-24 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 77f7e8bd-7360-344b-b1c8-a84abd5838e8 | -7.78903 | -50.22513 | 2026-09-24 04:08:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0506268f-f8f1-3369-ac5c-e5751b96d2d5 | -7.0332 | -44.65419 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 136b1678-2f17-3de3-8542-8c57ed61f6e3 | -3.45408 | -50.07409 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 4a0f00bb-0b5b-3f7d-a7ac-c06dfa6a2ef0 | -9.15065 | -40.11179 | 2026-09-24 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ca89618c-86de-3a21-8ce4-410583ea4ed7 | -6.61115 | -43.73081 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccd0f0eb-c9c8-3bf4-9c31-8e5c0b6da741 | -6.92226 | -41.69288 | 2026-09-24 04:08:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 248faad9-f1bf-3166-bf09-b6adf11574de | -6.81548 | -44.65438 | 2026-09-24 04:08:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a723433-5c03-349b-b1c0-b13d870aaf72 | -9.26089 | -47.34344 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b106e1ca-7c4d-30af-9a37-3b5db64f0e39 | -3.66971 | -39.21416 | 2026-09-24 04:08:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f92c8226-c8a8-32d6-b617-fef1b431210b | -6.0045 | -42.72873 | 2026-09-24 04:08:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c267c443-fdb7-3f7e-aec3-30fe005e6f96 | -5.78807 | -49.1857 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 14cf2a49-2a08-3af0-8952-0808e4fb9f0d | -7.99852 | -44.94402 | 2026-09-24 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e7ea40e-479c-394e-89d9-af83680dd772 | -3.44075 | -50.08862 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2fa0a04b-f189-31d2-9179-665d47568f66 | -5.32226 | -43.42214 | 2026-09-24 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README34.md)
