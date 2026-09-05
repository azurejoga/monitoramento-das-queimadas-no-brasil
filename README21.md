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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a6b6209-4282-3dee-9b04-2936b51471ca | -5.43224 | -60.11844 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b581cb8e-dd90-36fb-818a-b6198ff57475 | -6.15066 | -59.93514 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dffdb91-0a24-3c8f-ba14-1deb03a2c7ce | -5.34085 | -56.01957 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d78a1af-af17-31fb-a708-ecdc04b8eb4d | -5.34254 | -56.03043 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f3239b68-91b3-313b-b69a-aae7e6431c2d | -5.65819 | -60.23527 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 22a1feee-eec5-3932-9693-d4137c03a0c8 | -4.36517 | -47.77544 | 2026-09-05 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2059db60-0d58-3571-a40f-fa4ec3add3eb | -5.35192 | -56.03543 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9765b690-a1b3-3019-a8be-a04df565a538 | -1.50492 | -54.96914 | 2026-09-05 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a0a03f8-d9ce-3709-9cf9-ac52f851c4dd | -5.76783 | -59.18019 | 2026-09-05 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b107032-ad3b-36e8-b417-895e4b068fe8 | -4.673 | -55.63527 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 68df2bff-f583-369b-a5ba-7fc66e33c3d9 | -3.17608 | -51.54838 | 2026-09-05 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 934cc09d-9e07-3029-a462-54cc9a1b7a38 | -3.58365 | -59.41241 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffdc8a00-3651-39b8-9d2e-7c02b6209ab2 | -2.91719 | -60.99555 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9ad4b14-28ed-3911-9710-232f8208d23b | -5.17497 | -56.05668 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 878407c4-a3ee-33a8-a0ad-907c9902db8f | -3.55627 | -54.48472 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3537ddc0-856f-3e11-8d85-b2039d19aa41 | -3.3831 | -61.3404 | 2026-09-05 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22a02970-1fde-36a7-ad9a-df6b72ebb359 | -5.17274 | -56.04925 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3614ad7-5e3c-385a-bad6-8d660f996fb7 | -3.77485 | -61.76715 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 84d109c0-cda6-3706-a818-63944942e6e6 | -1.83744 | -47.9303 | 2026-09-05 05:04:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa94ce5b-438f-363c-b4f6-bff3bceecccb | -5.35023 | -56.02456 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f5535695-0b4d-3b24-8acf-479a6b5718eb | -1.18714 | -53.82164 | 2026-09-05 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 154fa4bd-4d6d-3a33-86c8-fa9e6d1bee5b | -3.63639 | -54.75651 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bee8555-96fc-3cda-90dd-d7aeded0e962 | -5.29256 | -56.00124 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1225e563-f9ec-340f-87b5-eeae3120928e | -5.30363 | -56.01711 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 272519eb-1c6e-3a1a-afea-e288b39492d0 | -3.77927 | -61.76787 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b839a7aa-4f5e-3256-b996-3ec3e8d5a5d7 | -5.76944 | -45.07134 | 2026-09-05 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7e3768c9-c007-3869-8e15-4ee7ad2ae0e5 | -1.18381 | -53.82114 | 2026-09-05 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3c0d3bf4-ae4a-3539-8e91-86edc74d3d7b | -5.34476 | -56.03785 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ae2fc039-7bf6-30b7-b952-a3b3f62412fa | -5.33207 | -56.03234 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b23f6bae-bba8-31d6-a48f-994580d6d96c | -3.23039 | -50.56957 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3c52a2c-1673-332e-9f01-2d9a8b49b5cb | -5.43023 | -60.12082 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74e68097-fd38-3619-986f-8bef314f20aa | -5.29587 | -56.00175 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ace588f8-1587-34f6-83f5-35f1bb109f94 | -3.14402 | -60.63634 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a47ad6ca-e474-3625-8565-8ea3f70a570f | -5.92259 | -47.89027 | 2026-09-05 05:04:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 3561255e-d806-3e04-89e6-5e3c23b2bfa0 | -6.15746 | -59.94109 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d170e229-7c5e-308b-b0cb-c54f553b25bc | -5.32342 | -45.17125 | 2026-09-05 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e347981-c9f5-35b3-ad86-3fda47dcce37 | -5.32545 | -56.03131 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 760cccd5-ed94-3772-bc73-5e98c0b62054 | -4.37 | -47.77619 | 2026-09-05 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| abf883c9-3000-3f36-b6de-6a51c77649aa | -6.12133 | -44.68523 | 2026-09-05 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8bb37bb-cec9-3c35-b5af-7e2906096581 | -3.62914 | -54.60648 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02657f2f-a366-3e34-87f9-7809368abb02 | -1.66934 | -55.50557 | 2026-09-05 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| deb31246-1b2a-3322-8445-84f930a01298 | -4.09984 | -60.66079 | 2026-09-05 05:04:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcf4eade-da44-34dc-999b-95197cc9c38b | -5.7708 | -59.18504 | 2026-09-05 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4273deb-698e-31d5-8a56-7b4dcba09ed3 | -3.14342 | -60.6401 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| abf937f8-d206-3614-b32e-903860b64874 | -3.44387 | -43.2672 | 2026-09-05 05:04:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb576894-0c47-3395-975b-14c10afc7752 | -5.29978 | -56.02004 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 570aa69c-f3f4-33a8-9bd9-9f21b3a7d4fd | -3.27487 | -57.87274 | 2026-09-05 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fdbd86f-75e7-309f-8c14-877b9e51ae55 | -1.1866 | -53.8251 | 2026-09-05 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d6325567-493d-38e1-856f-5f39c51f3df3 | -3.77856 | -61.77218 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73390040-f282-3aff-93e7-54abfd9fde97 | -6.35274 | -46.11436 | 2026-09-05 05:04:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54973a83-6a99-3a28-b573-2d800e9e5ef0 | -5.16943 | -56.04874 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee1d977e-941d-35b9-9e10-71714c9e448b | -5.34861 | -56.03491 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 76318d76-90d3-30cc-a17a-3376c67e6f46 | -1.96281 | -54.05952 | 2026-09-05 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6c5f0b81-a4f2-3d1b-9b82-820d780e2907 | -3.85009 | -55.85141 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69cee445-4917-3752-9244-4e889e917f32 | -2.12765 | -49.52803 | 2026-09-05 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 704bf7c3-ea53-3668-b415-cc7a53749a1a | -5.77474 | -45.07679 | 2026-09-05 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c61e09c5-5d45-3f3d-9d2b-382ae3360605 | -3.2237 | -48.61427 | 2026-09-05 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c904dffd-f257-37fb-b41a-f687178189ee | -5.34747 | -56.02059 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 667aa2a1-e37d-3103-b8e2-7502999ca853 | -1.26483 | -55.7422 | 2026-09-05 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 535d39a3-c1c4-3a30-abde-d9ad7d5a7845 | -3.38376 | -61.33628 | 2026-09-05 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e07f27fa-60f6-3bb4-9de3-ee45e678b996 | -5.33869 | -56.03337 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17c6678c-0138-351d-aac3-bb9097044f5d | -3.766 | -61.76575 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3ac9ecb-3f51-3205-a6b3-594b88fe7150 | -5.29701 | -56.01607 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95739ab5-213c-3901-9aff-1b4332b3e95d | -4.68015 | -55.63285 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ea73319e-3031-3aaa-bd27-2f7aedfe6532 | -6.15292 | -59.94505 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d3602ca-d30a-359a-b34c-cd65b94652da | -5.30309 | -56.02055 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7cc68407-7568-35dc-b025-eaaf1dba579e | -5.92182 | -47.89577 | 2026-09-05 05:04:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| fc524e3f-cbfb-33e2-b181-4d64c7992302 | -5.17551 | -56.05322 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07291b4c-2552-3d48-9a05-8e0184a71e63 | -1.47968 | -54.25821 | 2026-09-05 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7145ce2d-740c-391d-b7d5-d6e5643a9b40 | -3.62582 | -54.60596 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 09203e0e-fe20-34d9-b505-134d76a02f86 | -4.09925 | -60.66443 | 2026-09-05 05:04:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e0db422-1a5c-34f5-95f0-f9efe8502feb | -6.14605 | -57.76034 | 2026-09-05 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be35dad9-e45a-327a-b4de-e2edb24dc8fe | -3.17166 | -61.14169 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5938b8d-ff6d-3551-9bfc-5ef84c4a10c0 | -2.94902 | -51.28967 | 2026-09-05 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51c5b8b6-458b-3790-b714-19571771516b | -3.7942 | -55.88166 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68585e39-4fce-39d4-b7f6-ad2cfa905b7a | -6.1295 | -59.92213 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60d0a8a4-2c5b-30ff-a605-61bce457bc8d | -5.55716 | -60.23669 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 015a9c38-7df3-3fa9-bd79-39a507669834 | -3.12183 | -57.69773 | 2026-09-05 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77b7336a-98e1-3dc5-a035-492284506d98 | -3.439 | -43.26569 | 2026-09-05 05:04:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5cce2dc1-6749-362b-b4dd-3179b98e5ce0 | -3.90591 | -55.88479 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5865191c-1d5a-3da0-b88b-e9bbbc0be21a | -3.79197 | -55.87424 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30cb4841-055b-3205-b018-d53507199339 | -6.34767 | -46.10972 | 2026-09-05 05:04:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc85b00c-dc34-3c2d-815a-5759949962d7 | -5.34807 | -56.03836 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 7aba9b72-8344-397e-a309-f4d1747312dd | -4.19749 | -59.93447 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c2c7e6e-6ed9-34a8-8acb-fa012ef95edc | -3.80745 | -55.88371 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4496dd6-405b-3c1b-b01c-b6bf9bafb0a7 | -5.17659 | -56.04631 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6bd3081-d85b-32aa-93f7-86ae0f0ca2a6 | -6.55433 | -44.77293 | 2026-09-05 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e205cea-16a8-3930-a71d-e9ad53b5d72d | -5.76884 | -45.07573 | 2026-09-05 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 818b5ac8-1546-3bad-a0ac-e46242f923b2 | -6.20407 | -57.7696 | 2026-09-05 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f6c0afd7-178a-303a-b6c8-beae70707d6e | -4.13102 | -56.33688 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 708c75a6-b1bb-3f1e-9919-33f6626a0322 | -1.39806 | -55.63068 | 2026-09-05 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb69f83a-be4c-32a0-b7c0-93d21ff9f18b | -6.12331 | -59.95932 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2652fb59-c60d-3184-8386-8c5ae87fe9d0 | -5.34801 | -56.01714 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8fc6ef7-1cff-3102-9a77-3594ebc333e9 | -5.17605 | -56.04977 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a04a677b-6e29-340a-8dab-63faea0a0eb4 | -4.64587 | -55.7439 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bb6b072-aa44-3c2a-911f-d848aee3df0a | -5.33039 | -56.02147 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76a62b6a-2367-3066-b39c-77a59269ce2e | -5.35246 | -56.03197 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fe38885c-8b68-3c1b-b746-a77e075319b4 | -4.67961 | -55.63629 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ab908ee5-bf17-3814-af20-347e8540e286 | -1.32372 | -56.1266 | 2026-09-05 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9134a858-b4ed-3918-815c-b3ccb2a81667 | -3.79143 | -55.87769 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README22.md)
