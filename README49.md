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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf240453-143e-3fc8-bc07-936b31d04fe5 | -11.84364 | -44.99289 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd1d1122-ab40-36ad-82ac-cafc3f3c7210 | -11.38411 | -45.06276 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9577b561-7b48-3b62-8223-c7ace243d45b | -12.17946 | -51.42167 | 2025-10-01 04:21:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9fe527d-0d33-38a8-99a9-824d4cd5ce69 | -12.37281 | -50.19836 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91a98642-6245-3f34-87af-91ee1f0be77b | -9.40583 | -54.71502 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 991203fd-1bd0-39a0-abc0-15231059dadf | -14.90312 | -47.19099 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71b79551-19d7-345e-9ee1-790c5b7a18ea | -18.33263 | -41.80639 | 2025-10-01 04:21:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6dc447f1-47a3-3a83-99a1-6266c631a075 | -14.7009 | -48.13219 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af837ad5-01d3-311a-913a-58692d82e482 | -16.01345 | -50.89897 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3018939c-c5d8-32a6-b968-761028d4c285 | -13.32978 | -47.829 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c796589d-7aa9-3f20-b043-a0d8527ba5e5 | -14.89384 | -48.37048 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b33d709b-7f31-338f-9697-5b39d457e1c2 | -14.00769 | -44.99675 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e01d1cce-21af-3799-803e-8a7151e2a74a | -14.88149 | -48.31872 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34e8bf50-2052-3f8e-bf82-36227fc1fbc2 | -13.77702 | -48.32092 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d58e34da-b308-3d65-9b96-9b50ccf29e96 | -12.4477 | -44.66583 | 2025-10-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 902dab90-02ca-3cc7-903a-3db45dd26686 | -13.93307 | -48.09774 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 195550f3-4146-3d4f-a387-1af3ae8a83ed | -11.74072 | -46.86997 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c89b9550-a078-342a-bec8-24605312379e | -16.83414 | -48.85095 | 2025-10-01 04:21:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 926b6160-556e-3163-9abf-096a9412f3c8 | -13.66976 | -48.06924 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4aef0927-cbd3-36a4-8db1-50670b4158d2 | -13.33382 | -47.86792 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d76fd1a4-d5d8-3712-be91-7f61c3dd61d7 | -14.03158 | -47.99311 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18c5bd41-045e-37a4-a44b-25b52a9a458a | -15.77355 | -43.67815 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16152cd6-fac2-30cb-be53-ef347b61c59f | -15.25096 | -56.78102 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95b1b626-9673-3187-a54b-a0cce28ffd7a | -13.8279 | -47.46527 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54a42dc4-28d4-3277-82ba-71851107a451 | -14.19059 | -46.11409 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6e19405c-2745-3f92-bdd1-21b3932176f6 | -16.08702 | -51.03644 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f97f4855-cbc6-39bf-bbf1-7042381e96ed | -14.03494 | -47.99369 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d64d907-3680-3a19-855b-8b9ff6577e0b | -11.42782 | -43.49972 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6fcc03fb-7a86-3db5-a405-74242740cdc2 | -14.78543 | -46.96727 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8bb2bd4a-de3d-3643-8799-9f5d50968b72 | -14.66937 | -48.1348 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60ecfd12-0771-3e3f-9ae5-a88ebd17f41f | -11.38303 | -45.06984 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03b8a087-946c-3760-8938-00dfdcddf11e | -16.22139 | -48.81038 | 2025-10-01 04:21:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21fc47a9-31ab-3aa7-b79f-ad1a3532aed0 | -13.67194 | -48.07721 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc0431b5-ddaf-33b8-b949-4543389962ee | -14.58867 | -48.30053 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1c674e4-f285-3987-ad15-4b6250387125 | -11.66142 | -45.31616 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4de2c112-1f19-3198-b3ee-b5506ce2e86e | -15.48267 | -48.55656 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 616712ca-1bf8-33f9-9b43-1f35582dec92 | -12.78582 | -46.87119 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d9afc6c-36d7-3048-a821-d3aac9f8831f | -17.41023 | -47.15054 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c6b2d77-60a3-32b3-99b6-2f4dbf8734c1 | -14.71742 | -48.15802 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1aacff55-4afa-3ffa-8586-c601993f96ca | -13.72117 | -48.6368 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b71115e-aee8-3a60-99f6-eb1dfcdae94f | -13.32862 | -47.33112 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e512a03f-cbbc-3d33-9b1a-80bc84aa2179 | -15.25669 | -56.77769 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e64e6ec-04f9-3de8-b44c-be7657f2f8d0 | -14.44628 | -46.352 | 2025-10-01 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fd69bee-4a37-313c-9a01-641359418306 | -14.67551 | -46.95272 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad4d6f5f-09d1-3293-a94e-269afb69cac5 | -15.94593 | -48.12215 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d93a611-15d1-3ad6-a17f-4aa49e29db53 | -12.86993 | -46.76899 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dceb1338-abdf-3cc0-b3a2-7c73ac1c41db | -14.19224 | -46.10347 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01c3a768-35fd-3c67-8f9c-c16445762089 | -11.1357 | -43.3812 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9cb534fd-4da9-3834-8028-840cf37d9001 | -11.91985 | -48.00116 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e13857b4-bfc2-3118-ba3b-026166051b2a | -15.49022 | -45.9093 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a15714c0-fa68-3ca8-970a-e1dae62ded7c | -15.75623 | -43.72351 | 2025-10-01 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5d00c5b-6836-3327-b0cc-935f0d97b35b | -10.81494 | -46.63433 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b40ad0e0-78b2-3c34-a985-7c889eee1af9 | -13.41536 | -47.53322 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca8fba3a-02ac-341f-a363-6db4c5b6a5d3 | -15.61116 | -46.91126 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9ffc33b-18b0-34b4-be3d-690f7ba96231 | -11.64103 | -47.4896 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b180f6d-cabc-3d77-bf2d-9e5591f63db6 | -14.88088 | -48.32248 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 12cd7d30-727f-3c5a-971e-f1ee7604f1a4 | -12.78251 | -46.87064 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8886c7c-de6f-3fb6-8d54-a924f2e4405a | -11.52785 | -43.55768 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 742ad4b8-37fb-34a3-a56e-82b9f9c07cf1 | -11.60653 | -45.05368 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0858f8e8-f6e3-345f-b89c-aeaa5036ee89 | -13.359 | -48.105 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15f45168-3915-331c-9e2b-9ee301310f2a | -13.14852 | -47.41164 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4ba9a65-e97a-3811-a1f1-3e63840446dc | -11.46862 | -44.97754 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d814e10b-2f8a-3d98-9310-26b7665f9dee | -15.11994 | -48.00363 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3304795a-e597-3c12-a657-cdd9e8ed1148 | -13.39039 | -48.08349 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71bef8ea-6362-3528-8dc6-5207fa1d7955 | -14.71683 | -45.27248 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcbaf540-c3fa-3616-8fa1-a45bdc380b69 | -14.699 | -42.32841 | 2025-10-01 04:21:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 35895de0-877b-34d2-bc0f-2a3c743af91d | -15.13649 | -46.42116 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3261fcf2-cfe0-3e94-ae26-ec19ae79d116 | -13.30239 | -48.70298 | 2025-10-01 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12264802-b0ee-3369-af7f-579bd733e51d | -14.00381 | -45.02249 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05ef8556-3b55-37e2-bd36-30445eb630f5 | -11.12706 | -49.78969 | 2025-10-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71e37fcc-cc0a-3346-8425-150e6a3be1ae | -13.54094 | -47.25922 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6791a7b-3a5a-335b-bb51-9bc09dc02150 | -11.76451 | -46.87031 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1f3164f8-f25d-3a64-8798-02efc14f163f | -13.73346 | -48.81922 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 91fe9fb9-1578-39bb-a366-fa4c3546b817 | -11.38634 | -45.07037 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b57cfeff-0f65-3fe3-98cc-7d9d72b20c6b | -11.16222 | -47.2307 | 2025-10-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 922430de-ee99-3b08-b84d-8550b7485af6 | -11.66418 | -45.32022 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b7d6e6f-cd7e-3b6a-8d10-fb8051f1a0cb | -10.26124 | -51.70382 | 2025-10-01 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6a360d7-2254-365f-8eb2-ba67bce961f9 | -9.5525 | -54.59565 | 2025-10-01 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e982a97-5704-34ab-acc1-9f02364e6cdc | -14.66266 | -48.13363 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fb43bfa-5004-394d-b23b-590c6f11c3af | -15.60841 | -46.90715 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 44691597-87af-3944-8b25-f0bb83bc4703 | -17.80919 | -43.42277 | 2025-10-01 04:21:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92072330-22ee-3018-83c2-5abb16b4e7ee | -12.24594 | -47.81263 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00596ba3-d994-37d6-bdf5-b93408bd6f71 | -11.82296 | -44.92751 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 068388d1-9dbc-328d-9707-f903521f102b | -13.37594 | -48.10788 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09e53167-4bda-3817-8729-db557c24369b | -13.28931 | -47.23586 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e15c3206-e8f5-33f1-bd90-6800306f4d07 | -12.7656 | -46.91168 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69d9404e-96fd-31cf-bc40-6865ca34671e | -13.64818 | -48.03115 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0efe54b8-b058-3ecb-ad53-ddd93919bd13 | -14.70414 | -42.31945 | 2025-10-01 04:21:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9d411cd4-e5a5-3b3a-b7f6-944d203312d1 | -16.41287 | -53.54095 | 2025-10-01 04:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 98e5b834-2f93-3d22-badf-a1905b7e9b03 | -10.79502 | -45.35398 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6e9e168-35e3-3ec0-8357-03b8a59f5848 | -11.85363 | -44.99447 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 91d93d96-006e-35ad-94e6-524844531a31 | -17.41416 | -47.12539 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2485c66-60cf-3ff7-95f8-256a0f59f47a | -16.38017 | -47.01817 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17d55b41-e40e-3c8b-913e-67411cfb5cb4 | -14.92542 | -47.81719 | 2025-10-01 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d28e7b6f-851d-311e-9c36-3c1fb2dfd220 | -14.598 | -48.22197 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c83f82ec-d715-3037-b422-e3aa7afa7764 | -15.29696 | -46.19503 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dec5aac-8a64-3378-9962-d12551835145 | -17.28436 | -44.91869 | 2025-10-01 04:21:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a24f1f13-6d3a-3a99-9829-301e3790d682 | -15.34433 | -47.84016 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8a93d8e9-ace1-3db2-b550-63c6b918fbb5 | -16.25859 | -50.92994 | 2025-10-01 04:21:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5b0053a7-f804-3aba-97bc-15e7c7d8f47f | -16.40542 | -47.05173 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README50.md)
