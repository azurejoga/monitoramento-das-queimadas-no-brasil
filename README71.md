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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d990fffe-5531-30ef-8680-acf74d996bbb | -1.10331 | -54.17417 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1691e076-66e2-3eed-a835-4f7d267240ae | -1.77052 | -55.70009 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e8327e8-6f11-3a67-8f40-bae9a53ed9a6 | -2.2287 | -51.90855 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7e5e74d-7aea-3737-b2dd-d991a33a6f27 | -5.95203 | -40.92333 | 2026-10-10 04:44:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 22739bd0-9314-3f45-9b6a-2967e2f315da | -5.33321 | -50.95468 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04737a47-c27e-36e3-b3ee-718ab4dfb7d7 | -3.32275 | -54.04729 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bffe47ae-2665-30e0-bf6a-979726e08379 | -3.34326 | -50.41439 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 207cde31-170a-32f2-8b9d-67a4769b9a48 | -0.91271 | -52.43983 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5087235-20d0-3e69-9780-5c6a2258c03c | -4.84461 | -46.77933 | 2026-10-10 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4e1804e-e2c9-3d04-b515-dc8f0ebd1ab2 | -2.39423 | -51.30726 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9f0dfe4-b7dd-3f96-a221-249d998d770e | -3.11237 | -54.16613 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8110904f-792a-3201-a039-185884bbf0b1 | -4.10978 | -54.01333 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7bcdf84d-d745-328f-862a-f794a3625282 | -5.74914 | -45.12292 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8f976924-9e24-3f64-a3eb-1e94a04c1248 | -2.39039 | -57.8991 | 2026-10-10 04:44:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cd1e522-d7ce-3130-8b7c-3331f0ed1479 | -2.45641 | -58.029 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d06fb94-3085-3694-a9d3-b093e31a499c | -6.15635 | -47.96192 | 2026-10-10 04:44:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6c705c5-6586-34d0-8ed4-d1b7620506f4 | -2.79499 | -51.40275 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7db59fad-aa9e-3a56-843a-0646cb946f60 | -7.03342 | -44.3371 | 2026-10-10 04:44:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30826228-2a68-3e77-9f73-a753bd4fa289 | -3.18102 | -50.5853 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fdaa707-6253-3706-b18d-0ff29dc56703 | -4.82258 | -56.08399 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eda99b5-f621-38c2-89b6-31bcfd0570e3 | -3.25031 | -50.41459 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e5f0a63-b7f2-3ebd-a7de-d782b85cfda9 | 0.36197 | -50.94593 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddfe7f3b-e89b-3bc5-bf3a-c690e40d320d | -2.98531 | -54.76873 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08fb45b8-93d4-3c97-ac94-5cb0405b557a | -3.32678 | -50.78216 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cca565d-97b7-35ac-a357-63324e6f260f | -6.44855 | -43.82698 | 2026-10-10 04:44:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8f7d26e-20cd-3bff-8d6f-556077dc6339 | -3.19151 | -58.64965 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5895e7c-c4c9-361d-a52e-4d4b47d7c33e | -5.49633 | -43.97522 | 2026-10-10 04:44:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 003bb87d-fa22-30e3-ba7f-ef61a28757b0 | -3.2549 | -50.43296 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2517c73a-b694-3b39-9330-3a1e82cd3ae7 | -3.85673 | -44.05201 | 2026-10-10 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 921bb9b1-54f1-3451-9709-0e00097ef147 | -6.94815 | -46.13036 | 2026-10-10 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ee5d946-6a59-3bb6-8b73-d4d1ede2b544 | -1.33025 | -55.45199 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb161781-d000-32a1-934b-a63aef54a068 | -2.75083 | -54.10881 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1787c030-9bfe-3c76-ac34-57bf542d7de7 | -2.99882 | -53.90795 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 470885b7-a796-35d4-8366-971dcc711e37 | -0.88272 | -48.71326 | 2026-10-10 04:44:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 425bc3a5-14f9-3a98-9b7f-4c1082d2aada | -2.47599 | -56.06666 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8044125e-95da-3e0c-81fd-137b271709eb | -1.33206 | -56.39901 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de071df7-74cd-3883-bbf2-827a760f9f6b | -1.7674 | -55.69985 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7132fea6-5e24-3e01-b137-0bf8e786c502 | -4.6839 | -47.43325 | 2026-10-10 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2607a626-c96c-330c-a3c4-5951fdfe47f8 | -4.12398 | -46.86936 | 2026-10-10 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 575be5bd-500f-3b4c-9428-eb840f62969d | -3.01069 | -51.01196 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32aec4ae-d98b-3227-9909-7015f796603a | -6.07877 | -44.00288 | 2026-10-10 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63b48db7-b9bb-3fa8-9ce2-f3459835b518 | -3.38096 | -44.48065 | 2026-10-10 04:44:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a618857-fc71-382c-a7f3-6e57f0674d95 | -6.1949 | -45.43341 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1bc9757-0213-34a2-a04d-8f7ea40a831e | -3.43591 | -59.35693 | 2026-10-10 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff28264b-55a7-3e5e-ab22-754898440fd2 | -6.32057 | -55.34089 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85a00d32-e52f-3640-8709-a0a3645a05e5 | -11.39226 | -47.58562 | 2026-10-10 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ccb0f0c-caec-33cc-8086-657258b20755 | -13.37513 | -43.90442 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05a0b7d2-e142-3828-96f8-6475b738e512 | -6.93323 | -59.26222 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98020eb6-7605-32fb-96f1-a4dfa53bb404 | -7.06126 | -46.45858 | 2026-10-10 04:46:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e02e4027-b2b6-37df-a459-3ad02271a6d8 | -6.9271 | -59.26097 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0af1373d-96a8-3eaf-b48f-73a31189a802 | -11.60213 | -43.74843 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c25f7969-01b8-3685-903a-7cf2449dd5ba | -8.94177 | -45.12279 | 2026-10-10 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1cfc345-2f30-317c-b1f7-be7b2a6fd9a4 | -6.32732 | -58.30269 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 405a2251-527e-328b-86b8-f934cd70686e | -11.94907 | -43.47546 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bdabecb-fef6-312f-89b5-a4e78efa1ada | -8.76856 | -49.6053 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eabe53f2-4d24-319a-8dcd-d3122f70532d | -13.73062 | -49.12421 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87008a05-8631-3fa9-b181-f53724bfb0b9 | -11.17724 | -45.31844 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ed89e67-8fbb-351d-b344-3085f8913c0e | -7.77666 | -42.31569 | 2026-10-10 04:46:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2786293c-a336-3c7d-9593-845912826209 | -11.59743 | -43.72237 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cda10b5-273e-3c3d-8840-e5377a51389f | -6.12974 | -53.05505 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0febf660-2f96-3aeb-b4b9-4a3bbfe9e4cb | -6.9411 | -59.25423 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd899b55-9ab6-328e-8551-31d3c7ae9252 | -15.10493 | -43.64013 | 2026-10-10 04:46:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bf6c57cb-c023-3964-84da-7a6075dbbfac | -7.23949 | -55.15923 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cb12650-56c6-39a5-bbe3-1892e8bfd31b | -9.27119 | -47.40692 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25d6f925-7c10-378b-a88c-62ed9a44fcb4 | -12.36985 | -46.58302 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae5cf9f8-7c70-3437-a81e-b446d60c7a68 | -7.87956 | -49.80763 | 2026-10-10 04:46:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d43aa1ba-2e67-3701-9528-f31c3ba31c62 | -14.45443 | -43.94349 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 980a3258-003d-3b43-8a10-5d890c9e9299 | -7.42066 | -55.29945 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 818e9260-49a4-3128-9139-ea738eb963e9 | -12.07628 | -47.37797 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6c2c152-504e-3933-bb8b-5559ce1f4441 | -7.93156 | -54.72498 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 89d1716d-3d5b-3c9b-a026-7370a4d7606a | -5.99075 | -55.37987 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5ef3ee9-b535-3916-b77a-af1a0a651e6a | -6.01568 | -53.47869 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1f663e9-f95c-331c-a01b-d3c69a91b21e | -10.99921 | -45.39457 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d7e3ff4-8f58-3136-9e89-137dde8e27b8 | -6.61741 | -59.94436 | 2026-10-10 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d831098-8565-323c-bc0d-2774e1e8f0f6 | -6.47513 | -55.06577 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c16d15fa-58d8-3c15-8af0-776ac875525f | -11.3658 | -54.02868 | 2026-10-10 04:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1e74f83-72c2-3741-80c8-00774fdcfd31 | -11.87087 | -48.03082 | 2026-10-10 04:46:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 365ff22d-e8e0-38f9-8d16-ddeedd592af7 | -8.36027 | -48.14241 | 2026-10-10 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 445cdb8a-24cc-31c6-998c-753571e220d8 | -10.49527 | -51.94249 | 2026-10-10 04:46:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96132979-2dbb-3b1b-915a-acf1868207e1 | -14.03063 | -48.76538 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18bddd0d-09fe-3f13-b404-e509b5010e57 | -6.34991 | -51.7712 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46092ec2-cbe7-35d3-9508-d7ec00ccba48 | -8.58836 | -53.10424 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21aa1a43-3e46-32cd-9dd0-07a0031ef141 | -7.56715 | -45.64234 | 2026-10-10 04:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6386b42-bcb9-3375-87f6-cca6b618a5bf | -8.18999 | -46.3518 | 2026-10-10 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6eb4765-26c3-3cee-b472-f3e6020b08ed | -7.90838 | -54.72524 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ce09535c-d93c-3580-a8a4-d338767665ff | -5.88919 | -55.53037 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8e3d9f0-267d-3632-8e0b-3db5576e58f8 | -6.43479 | -55.27225 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fc0752c-0987-31d7-8ddd-870daa42f2e6 | -11.37365 | -47.57153 | 2026-10-10 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 485fd126-83c1-324f-ab0c-e66f13ead19c | -9.28799 | -47.38759 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c08a244-115c-3c4f-b3d2-5ea093294e05 | -8.99555 | -47.74068 | 2026-10-10 04:46:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57402a2e-2199-3086-95cb-11637fa5a0aa | -11.02056 | -49.11062 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2805e1f4-5e9c-3b74-b554-2d68b3bf06be | -6.92974 | -59.24701 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfe5f6dd-b88b-3d20-b58a-c973e6e20619 | -10.97751 | -47.7917 | 2026-10-10 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b00a64e-cc4b-34bf-8006-1dd110c57ceb | -7.18721 | -52.6312 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93a0c846-9c0f-3388-b528-b5ce550f0815 | -11.08627 | -44.09942 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68fbbafd-25cf-3369-9912-6744e116b81f | -11.01948 | -49.09599 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 398326fd-72ca-355d-9f2f-7312da033eda | -7.94989 | -54.75917 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83cbcfe8-92c3-3e3b-ba86-f9c2480606ea | -9.87375 | -50.49178 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1251460b-990f-3412-ace3-0e8727b5baa0 | -6.89448 | -55.55751 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5908c135-fe36-3464-93e5-26f77e23d4a4 | -6.36574 | -55.16301 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README72.md)
