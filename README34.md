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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| caecab0d-3b22-3513-a498-c937b6372c9c | -11.9418 | -50.5916 | 2026-09-26 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 558470a3-606c-308b-a7c8-1f3ac6d30e80 | -12.4981 | -46.9666 | 2026-09-26 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 68b148a3-d8c2-31de-8a8c-828c26a46379 | -10.7115 | -60.7312 | 2026-09-26 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 46918736-c8a7-3776-aae3-84c59ba430d2 | -3.8604 | -44.0585 | 2026-09-26 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 07c4cb0c-2fc8-3b33-925a-081e69fa5275 | -11.9641 | -57.6081 | 2026-09-26 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| e6a6a90e-b099-3c45-babe-a742552710ef | -13.8154 | -51.834 | 2026-09-26 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 45e24f51-036e-36fd-80a5-a35f2856720a | -6.2401 | -41.6153 | 2026-09-26 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| 8dcb2735-b680-3423-98c9-e52977421bc5 | -13.8343 | -51.8529 | 2026-09-26 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6c40baf5-cf09-35be-9ed2-03ca11c5ca0d | -11.9418 | -50.5916 | 2026-09-26 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 946705a3-53a6-30a7-ac9e-59097449e144 | -12.5173 | -46.9639 | 2026-09-26 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| b0e981f0-9763-344a-89a8-2a5285e7d636 | -11.7297 | -50.7869 | 2026-09-26 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e4286508-14ca-32dd-ac27-09a4a7b3496c | -13.2057 | -51.5703 | 2026-09-26 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 428510ff-4d1e-3e76-a860-88fe61dd2057 | -12.723 | -50.6475 | 2026-09-26 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 842b8355-57bd-3d7b-b81a-430046ae66ce | -12.4973 | -47.0118 | 2026-09-26 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 2fa06a28-dd37-3f47-a16e-ddc10243c3c9 | -11.7107 | -50.7891 | 2026-09-26 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 00e7e4f1-ec42-320a-a99e-cb84c5c5aaee | -11.1524 | -50.0172 | 2026-09-26 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 211c4fd8-c9d3-37e2-b213-4af8b6506d4f | -15.4322 | -41.5199 | 2026-09-26 14:00:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 153.5 |
| 3c1ea05b-1781-3b45-b5b4-cd385dbe2566 | -11.8014 | -49.8129 | 2026-09-26 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| ef91a860-55fc-33db-9ead-5012f9c46077 | -7.2758 | -43.2975 | 2026-09-26 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| e00d74ae-0c08-3b50-b48d-877bdf1e9e84 | -13.5484 | -52.9227 | 2026-09-26 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 28071358-c3d4-3d18-b349-4126f8b2956e | -13.5487 | -52.9016 | 2026-09-26 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 0e5c1a23-76f2-38bb-8623-02d6d064039a | -12.7514 | -47.8257 | 2026-09-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 4f4c5c42-ffed-32f7-922d-9bbc1ef651ff | -11.1714 | -50.0151 | 2026-09-26 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| e22e2237-12d2-388a-980d-b286b47fcbea | -12.4788 | -46.9694 | 2026-09-26 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| af6bf1d5-fd3b-37ca-a530-1af10eed5070 | -12.0556 | -50.6211 | 2026-09-26 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b2e24afa-bf0c-3523-b908-3621d08606dd | -12.9457 | -51.0695 | 2026-09-26 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| d8afb685-af6f-36da-82dd-206496508ceb | -13.8151 | -51.8553 | 2026-09-26 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 09a05b3c-a63a-34fd-9bcd-0139cde19bab | -13.5295 | -52.9039 | 2026-09-26 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| efae6e06-5430-3d5e-b553-896c58108f3e | -12.0365 | -50.6233 | 2026-09-26 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 4dcb529e-eb57-3b20-b3d6-5408e52c8994 | -14.2223 | -48.4975 | 2026-09-26 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 9eeb8117-e054-3194-bc28-9f4008a56660 | -10.9358 | -50.5972 | 2026-09-26 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7704e1ff-f207-3a5d-b7a4-95eeb71107f9 | -11.118 | -54.0268 | 2026-09-26 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 7d8f6c25-2049-3ef9-a901-be25311a3194 | -17.5445 | -46.3266 | 2026-09-26 14:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 89.8 |
| b771b301-3448-3a75-ae71-98936ddb6aa9 | -12.4977 | -46.9892 | 2026-09-26 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 515adfc1-18ef-359a-bb65-80ef27635e0c | -11.1183 | -54.0062 | 2026-09-26 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| da08e76b-59da-3ce9-a513-3751a68eefa5 | -11.9643 | -57.5882 | 2026-09-26 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e6d1c63b-5350-3818-bedf-0527e520eccb | -14.747 | -45.6424 | 2026-09-26 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 662612ce-0b23-3f39-9a28-2e91b38e1594 | -13.2057 | -51.5703 | 2026-09-26 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 05614c51-89dd-3c1d-bff1-52be9735f45d | -6.2401 | -41.6153 | 2026-09-26 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 148.2 |
| 3b076d41-7150-38c9-ac48-341b7905376d | -13.5295 | -52.9039 | 2026-09-26 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 2d24bff9-fff2-3e80-b26c-045d7ed93ab0 | -10.7115 | -60.7312 | 2026-09-26 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2b5842d7-83be-3c66-a1d7-2149ec523fc8 | -12.723 | -50.6475 | 2026-09-26 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 283.5 |
| 1fbca95c-78e8-3571-86b6-5477b461c7fa | -13.8154 | -51.834 | 2026-09-26 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 254c6f70-cd44-367e-ba4d-0cc73d1c343b | -6.2213 | -41.617 | 2026-09-26 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 202.6 |
| d70e42eb-d1c8-3964-81e4-b3ecccfa8618 | -10.9358 | -50.5972 | 2026-09-26 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| c6ea845a-c097-3c1a-8af5-f2f54238238a | -14.0425 | -52.06 | 2026-09-26 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 90c8e4b0-5872-306f-a0bd-99ffe421cbc0 | -14.7475 | -45.6191 | 2026-09-26 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 9de890e7-ff81-3383-a919-ec97f6cb50cc | -6.2587 | -41.6377 | 2026-09-26 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 130.9 |
| 8386399b-4957-3a63-af02-793622249cd4 | -13.5487 | -52.9016 | 2026-09-26 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 7a4d8091-66a1-3b09-b147-8c069fc15a73 | -14.7671 | -45.6155 | 2026-09-26 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| ff220824-dc58-35e3-b008-0c4d8ae2f26a | -3.8604 | -44.0585 | 2026-09-26 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 93ca275d-b192-32af-9a83-0d3d415368ce | -12.4784 | -46.992 | 2026-09-26 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 9122c663-d3c5-3cce-b525-267725cac195 | -12.4788 | -46.9694 | 2026-09-26 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 85e24475-326a-306f-8372-277957187e9d | -11.7104 | -50.8105 | 2026-09-26 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e6fd4bf0-2377-3650-aaf2-56b59eccc4da | -11.8014 | -49.8129 | 2026-09-26 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| b9d49ac6-ac82-3b88-a6fb-be8c3baf6e41 | -12.9457 | -51.0695 | 2026-09-26 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 4497420b-0f45-3b14-866b-eea08ed6303e | -11.118 | -54.0268 | 2026-09-26 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 0a615ffe-dbdf-3c77-91fa-a88fe4ccf47d | -12.7226 | -50.669 | 2026-09-26 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| d54f0437-7eff-3384-bfc6-61ffcfc8e885 | -14.2223 | -48.4975 | 2026-09-26 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d815fd5f-a021-351e-8a76-f583b3e4687f | 2.8913 | -60.275 | 2026-09-26 14:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 7d7dfd79-de86-3458-8a3c-1b250bda1bb9 | -14.7665 | -45.6388 | 2026-09-26 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| bf70347d-7568-36be-8ca8-45458a1739d6 | -11.7107 | -50.7891 | 2026-09-26 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| dbc800f9-6cd1-37a4-9763-a21fb2f5d825 | -13.8151 | -51.8553 | 2026-09-26 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| da42985a-c4f0-3422-afd6-b9ff1597e31e | -12.0556 | -50.6211 | 2026-09-26 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 868b6d50-836a-3460-88a7-85acf47ca95b | -10.872 | -54.0899 | 2026-09-26 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 24b15a00-c3f8-3549-a7e8-6ac1d1afb0e8 | -12.4596 | -46.9722 | 2026-09-26 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| fad08bd8-cdb9-33e6-ba7d-83ab5390dbe2 | -17.5665 | -44.7172 | 2026-09-26 14:10:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1dba21a5-8c79-37f2-9fe8-203c0225d375 | -13.5484 | -52.9227 | 2026-09-26 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| ef529521-1f03-3966-af3e-7b6a00e57340 | -11.7297 | -50.7869 | 2026-09-26 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 97ac20c6-98d9-339d-b752-ace05173085e | -14.6497 | -45.6367 | 2026-09-26 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| d7381e9f-69b8-3ce4-a807-44addb5ed4c5 | -15.33 | -42.13 | 2026-09-26 14:15:00 | MSG-03 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88ec692a-f936-3146-bc05-abe5047e7ff9 | -14.73 | -41.12 | 2026-09-26 14:15:00 | MSG-03 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2280e33a-0796-342c-ad25-0ec66072d1d4 | -6.84 | -43.46 | 2026-09-26 14:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a83000d-2757-3f28-bcd1-dad88d200654 | -6.81 | -43.5 | 2026-09-26 14:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd15bf97-138a-32e5-b536-c8b4a5169666 | -8.36 | -44.16 | 2026-09-26 14:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 744ee243-c974-3781-afd0-902d803eb606 | -12.68 | -47.31 | 2026-09-26 14:15:00 | MSG-03 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1def7931-175e-3cfd-87ec-fac8688a4b77 | -6.84 | -43.51 | 2026-09-26 14:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 30fb5173-d5ca-3abb-9775-936cfc8c227c | -8.33 | -44.15 | 2026-09-26 14:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dff04665-f751-3ae1-945e-d7626626e3e2 | -14.73 | -41.07 | 2026-09-26 14:15:00 | MSG-03 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 16329757-f97e-3222-a737-38b910c82b06 | -6.84 | -43.55 | 2026-09-26 14:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a748dd5-6739-36da-bbaa-487a97a621da | -14.7284 | -45.5993 | 2026-09-26 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| eabdd7d6-2564-3038-8d50-b6df697f4423 | -13.5295 | -52.9039 | 2026-09-26 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| e009f9f9-2ea8-3786-8301-90742e8ae9e2 | -14.2223 | -48.4975 | 2026-09-26 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| cfb98ec8-1c0e-356b-b5f8-55e6e002e07c | -17.5665 | -44.7172 | 2026-09-26 14:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 176a3589-8c4a-3fea-8d66-c4b2ad58f2e6 | -14.6111 | -45.6205 | 2026-09-26 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 352e0017-8257-305b-85b3-ecb421e107a4 | -13.8151 | -51.8553 | 2026-09-26 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| d4bf954c-8f87-31ea-9aff-2e97244c70e3 | -11.118 | -54.0268 | 2026-09-26 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| d77f6d00-caa4-3e5e-a82b-69a16373c671 | -14.748 | -45.5958 | 2026-09-26 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| fbeecb5d-158a-3209-b017-35f7bb62383c | -14.6893 | -45.6064 | 2026-09-26 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 54253ca2-c01b-3e3e-a2a0-c8ffb3787cc6 | -13.5542 | -40.6497 | 2026-09-26 14:20:00 | GOES-19 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 405.1 |
| 80d0255f-3d6b-3da2-9d5e-67ebe518a8c8 | -12.0365 | -50.6233 | 2026-09-26 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d5d70676-cc54-3bbf-aeb3-fa07fc3044cb | -14.7676 | -45.5922 | 2026-09-26 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 21d359cc-b48f-309b-9486-dfd9f8635f6b | -11.1524 | -50.0172 | 2026-09-26 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| dcc56ee9-2429-338a-a419-8e27962e5c59 | -12.723 | -50.6475 | 2026-09-26 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 27a27ef0-7e2e-3293-ac91-111bf5ebdc09 | -11.9643 | -57.5882 | 2026-09-26 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| fa340fe5-eeb9-35cd-8586-29aa7dda0eaa | -12.6844 | -47.2767 | 2026-09-26 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 9da7147d-9e60-31e5-83a3-75eabc861ed7 | -14.6898 | -45.5831 | 2026-09-26 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| c9783bc3-caa1-389d-821e-0b3bad2cb2c5 | -7.1274 | -43.1009 | 2026-09-26 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 0b504a2e-4ad4-3c8b-a912-2d314d7a276f | -13.5484 | -52.9227 | 2026-09-26 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 6be61934-2c9d-376a-822f-fde73a3791fb | -10.7115 | -60.7312 | 2026-09-26 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |


[Clique aqui para ver as próximas entradas](README35.md)
