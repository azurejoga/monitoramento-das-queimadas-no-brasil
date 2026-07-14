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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 211bde7e-6270-3361-ab06-82150c15055b | -4.01544 | -48.06096 | 2026-07-14 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3ff4386f-7524-3982-b3c1-8e18cfb098e9 | -5.30757 | -43.05981 | 2026-07-14 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0e28f90-ce3e-3b1b-939a-6da96d2e83fb | -5.79444 | -45.11192 | 2026-07-14 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd265134-6627-3539-b08c-fbb65997ed81 | -4.36938 | -47.76752 | 2026-07-14 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9803a57c-31f7-3ac9-8b0b-23fd79e5c507 | -5.82655 | -43.47367 | 2026-07-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9f1db42-0c26-3f1b-856d-a0ffb732adc3 | -9.46997 | -40.4996 | 2026-07-14 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9d7a94af-7499-3b7d-9883-9123cca90d22 | -3.15622 | -48.57857 | 2026-07-14 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37b55487-b478-324a-96cc-51f107d7b63a | -5.82595 | -43.47739 | 2026-07-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 321ba988-6bb9-3e64-863a-bd0e391510e8 | -4.4944 | -48.29365 | 2026-07-14 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c99e701-766b-358e-a94e-d64e82de960c | -5.30448 | -47.24299 | 2026-07-14 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46803300-3ec3-3380-b262-4b07c862e1fe | -6.48813 | -42.22707 | 2026-07-14 04:12:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c362d2a9-9117-31fa-8587-65c54e1ee5ad | -6.48526 | -42.2227 | 2026-07-14 04:12:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d21aa898-a70c-3a70-aaec-8bb5211ac4f5 | -5.24347 | -44.9275 | 2026-07-14 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6c7a02d-f543-3381-91a3-e835a88ea207 | -6.48139 | -42.22565 | 2026-07-14 04:12:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d5e8c239-3813-335b-bf8a-b09e95b6f8d4 | -7.6992 | -49.34541 | 2026-07-14 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e108f61-3afd-3bdc-a6f1-c95b164237cb | -4.01526 | -48.06294 | 2026-07-14 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5762335-7165-39f0-9b1b-b5c6e67d8542 | -5.79654 | -45.11535 | 2026-07-14 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 474b56ab-f32f-3a63-a7c8-aa552836ff82 | -9.37648 | -40.74536 | 2026-07-14 04:12:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b11d6b7-2888-3761-9192-8ddc4a1a3473 | -5.82878 | -43.48165 | 2026-07-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf989985-fb90-3550-a55c-c85e555a8e5f | -7.74913 | -45.02831 | 2026-07-14 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea1dc3f7-3c5a-3daa-bcbd-62615e85195e | -7.766 | -45.51914 | 2026-07-14 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c821a831-4af0-36dd-a22b-38c422d3a2a6 | -8.82928 | -48.33287 | 2026-07-14 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8ab5d9a-cb02-3589-bdcc-e2f0429521ba | -7.29502 | -45.28366 | 2026-07-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7792449-c1dd-3282-b8a4-f0eb5629ee9f | -10.10022 | -47.98321 | 2026-07-14 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48dabe6b-ee6f-3032-a2b4-12ca565c699d | -11.49433 | -47.61488 | 2026-07-14 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a76ab02-98c0-3e62-b702-4c1895db4b7b | -13.54288 | -47.77216 | 2026-07-14 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 531662a2-b54c-3e6a-93c4-9f87a35d29a2 | -13.59891 | -43.43248 | 2026-07-14 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a451509-249c-3c04-9b30-45efc0d1502c | -10.09847 | -47.98278 | 2026-07-14 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e58cf6b-6639-3f7f-9841-b1eed9f1339f | -10.43373 | -49.77692 | 2026-07-14 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0846f326-027b-3d54-a31f-bad509eb8194 | -11.79482 | -49.5185 | 2026-07-14 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e58066ea-1f79-3b11-b61b-cfd550412804 | -12.45032 | -46.5246 | 2026-07-14 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cdeb886-c026-3faa-b66a-451898d4c2e4 | -11.69924 | -43.19897 | 2026-07-14 04:14:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7efd1d91-ac8d-36ad-9ea5-e41beb0d02d4 | -17.16458 | -46.83387 | 2026-07-14 04:14:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 253b519b-5887-3681-80b3-ddba6a743cfd | -10.75714 | -42.1087 | 2026-07-14 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e1bbfe0d-874a-34f3-8d77-d343a5c3a14e | -12.45578 | -47.80853 | 2026-07-14 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28bc78ea-6b60-35f4-9704-a930e3c752db | -15.34711 | -49.61563 | 2026-07-14 04:14:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b6dbdb03-dcd0-3cc8-8a83-56787111dff9 | -12.44843 | -49.58645 | 2026-07-14 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40330f25-61a3-36a7-8598-b14f13f39183 | -14.74774 | -48.20988 | 2026-07-14 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed7116c8-ede5-3cdc-882f-57c01b959b7d | -9.69693 | -47.70255 | 2026-07-14 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8615c3c4-ae29-35c6-8609-2d2eb907f366 | -10.82759 | -49.38258 | 2026-07-14 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a0c8332-97d1-3c2b-aa22-d63e4d24ccc3 | -12.45086 | -49.44837 | 2026-07-14 04:14:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08d55a7f-420f-393e-86f0-c51b5a55ff31 | -12.44924 | -49.58204 | 2026-07-14 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61025b02-2bff-3f8b-a3ca-447fc0f85b5e | -13.2625 | -43.53978 | 2026-07-14 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d6c5cac-9287-304c-a08a-39c9a1b9b453 | -9.70102 | -47.70321 | 2026-07-14 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 003383bb-86b5-3e7c-bd6f-011144a18ad6 | -11.65399 | -50.14725 | 2026-07-14 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8e9901e-5689-31df-b695-0fc8475fa36c | -11.94917 | -51.68615 | 2026-07-14 04:14:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f2f9ef3-0b50-3bb0-a8cc-1c9a8352a7ad | -13.39313 | -43.57229 | 2026-07-14 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a41d89c4-98aa-324a-8190-f13c5e7bc8da | -16.27016 | -48.96092 | 2026-07-14 04:14:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f92fa35c-9aa7-3c65-856e-a7bbd59f39b8 | -12.67769 | -47.67102 | 2026-07-14 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2a48ca7-299b-387f-ba09-fb2168bc1198 | -12.52538 | -48.28888 | 2026-07-14 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ac29a54-8217-3542-951b-8226745ba64f | -10.07493 | -50.1148 | 2026-07-14 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71f7dd74-1b5f-3420-9d33-2c586b853c8b | -11.25725 | -41.90623 | 2026-07-14 04:14:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7874f8ef-7532-32d8-a472-76a934b4c254 | -10.07397 | -50.12 | 2026-07-14 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffffa5a2-46f5-3bb7-8e0a-c0bd31ef37c8 | -12.45184 | -46.5158 | 2026-07-14 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3956506-d93b-3e58-94f6-18bc087baa1b | -10.4218 | -48.87626 | 2026-07-14 04:14:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fb91dfb-d3a5-33c1-830f-77b11d255dc1 | -15.34786 | -49.61168 | 2026-07-14 04:14:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f86ff929-375e-3338-a9c4-e360db49bd65 | -12.45108 | -46.52019 | 2026-07-14 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 244842b7-e4e1-36be-a201-21c5be1fce59 | -12.36986 | -47.88724 | 2026-07-14 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9bc592d-3ae9-39c4-9f5f-62da038b7936 | -16.19521 | -43.64022 | 2026-07-14 04:14:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b257672-6811-3c61-9d09-44f70cd38215 | -9.1795 | -50.88801 | 2026-07-14 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ace130fd-6409-3e08-b4c8-113c475d0034 | -9.80345 | -48.91963 | 2026-07-14 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39ba4ca1-1c42-3c5e-970c-1a9fcc0bc122 | -15.35203 | -49.61261 | 2026-07-14 04:14:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4e67e19-ff91-3723-b49d-0ab177483e50 | -12.45149 | -49.44732 | 2026-07-14 04:14:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| adc9c4fa-53c4-3fe8-bc0e-a772bc2ddd5a | -12.6609 | -48.23557 | 2026-07-14 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc2bbd83-11fc-3139-8803-f55fd35f9747 | -10.75328 | -42.11168 | 2026-07-14 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 89c49ee7-0f3f-3e33-98cb-ae9930375ad6 | -10.75659 | -42.11221 | 2026-07-14 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 53285984-ba2b-3c63-86e0-d41279b2ae76 | -10.43436 | -49.78061 | 2026-07-14 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bc8e946-9c34-3904-ad39-528b469d98d1 | -14.32887 | -49.93314 | 2026-07-14 04:14:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df24b4c9-17c2-3028-9245-c2f4655554ab | -16.1919 | -43.63967 | 2026-07-14 04:14:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c6da41e-e0a6-3b46-8806-08f8cb0e5120 | -11.581 | -48.39871 | 2026-07-14 04:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f90c1c65-01eb-377f-abc1-b2c40d7a9f32 | -9.18068 | -50.8816 | 2026-07-14 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63b653bd-88aa-3adc-a6f7-4161469a0690 | -9.10304 | -49.65495 | 2026-07-14 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84cdda20-cc2e-3b8c-b97b-d6b8ffa9e1f6 | -14.12484 | -46.47949 | 2026-07-14 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaab82fe-28b9-387b-b9d3-07e236521ad5 | -12.45473 | -46.52084 | 2026-07-14 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d35f8b8-b43a-3f2e-a43d-d90ea5f7c8ab | -10.75437 | -42.10465 | 2026-07-14 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d22a14c5-e38c-3207-b01d-9c4eb43596f4 | -15.34749 | -49.61275 | 2026-07-14 04:14:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 166f6c7f-0f9c-3823-8a36-4a05b5414667 | -9.69756 | -47.69889 | 2026-07-14 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d58d31f3-6a85-3d28-9751-e4b02024edce | -12.68157 | -47.67173 | 2026-07-14 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c149718-663e-37c8-a04c-75e7de64a233 | -10.43283 | -49.78179 | 2026-07-14 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 494f5142-4fcd-38e0-9286-d9d58bfefcbe | -13.29533 | -44.61585 | 2026-07-14 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6315928e-c282-346c-9200-556ffb826667 | -11.65059 | -50.14898 | 2026-07-14 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 806959b1-5457-300e-a6b1-9398c281f078 | -10.82843 | -49.37805 | 2026-07-14 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e65aa6f-ff62-37c6-be43-f868be411d58 | -15.35167 | -49.61368 | 2026-07-14 04:14:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 685564bb-ac29-3aee-b9be-9c4735c0cee2 | -13.45194 | -41.29321 | 2026-07-14 04:14:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| e6fb2cb5-8e2d-3dd2-b20d-7a41d4561f39 | -11.58032 | -48.40254 | 2026-07-14 04:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8eadd25-d8d6-318d-9edc-4039e86b0e56 | -12.45912 | -46.51717 | 2026-07-14 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65b5e460-c828-3905-9022-8233e751ce25 | -13.32554 | -42.46864 | 2026-07-14 04:14:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 01f7e611-8346-3946-9316-0bec02cdd6ac | -11.65612 | -50.14493 | 2026-07-14 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b5cd552-239a-3cc6-af2e-5f392cefd634 | -9.77045 | -48.74799 | 2026-07-14 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa89a9b1-b564-3fe0-a01d-3d642b423e1c | -12.45623 | -46.51209 | 2026-07-14 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 920b0c59-dccb-30cd-9d01-be159a2a529d | -10.83031 | -49.38073 | 2026-07-14 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9171dcac-7e03-3ad1-baf5-5b02f49271a4 | -11.49248 | -47.62537 | 2026-07-14 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6c31823-9bc2-380a-812c-5def11f331ce | -13.38651 | -43.57119 | 2026-07-14 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| df091d4b-464b-3d32-978b-fdbeff7b459a | -10.18133 | -50.12665 | 2026-07-14 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f527656-4eda-386f-bbd3-11ca11e63c77 | -12.52474 | -48.29252 | 2026-07-14 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f127fa63-0e78-3a6d-a01f-8b7dd7c05d20 | -10.18703 | -50.12236 | 2026-07-14 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4f80742-6173-3a3d-9bf1-b1a3a57b433f | -12.45397 | -46.52525 | 2026-07-14 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4af4bc0f-d554-31a9-8064-ccaadb973699 | -10.82584 | -49.37988 | 2026-07-14 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcb1ba08-e725-3194-ae12-67104b0f79e9 | -9.29667 | -48.5343 | 2026-07-14 04:14:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f5341eb-d0f4-36fc-86f8-c5911c938a14 | -11.95428 | -51.68715 | 2026-07-14 04:14:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README5.md)
