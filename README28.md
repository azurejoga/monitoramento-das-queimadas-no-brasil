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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b418bcd-617d-3395-b55d-0ee6f448a2c8 | -19.54045 | -49.6669 | 2025-06-20 05:23:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d5473810-5fed-306a-bb73-86dfbbeec126 | -16.30022 | -58.26511 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 2fc112e4-946b-3f27-b9c4-68089abc4455 | -16.29303 | -58.26404 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e07ceac1-7399-3266-901b-44a2ab13160f | -18.9929 | -52.08652 | 2025-06-20 05:23:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5033a4e5-6af1-3b8d-b06a-c6a591762c6d | -18.65703 | -55.75199 | 2025-06-20 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c949629d-1080-31d9-ad1b-2c8406458b10 | -16.30861 | -58.25776 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 13427242-981b-3b56-8c67-047af83c5349 | -18.65755 | -55.74779 | 2025-06-20 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 77772dbe-3549-3a6d-861e-20e43e05f2bb | -16.30082 | -58.26087 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| cb9b5ec7-1f88-318d-8481-ab1875873934 | -16.29363 | -58.25979 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e06a8b2f-01fc-3bea-bb36-e694719bab08 | -24.24354 | -50.74124 | 2025-06-20 05:25:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f82dcffd-f9cc-351b-82b0-d94cb1400d06 | -16.3047 | -58.2676 | 2025-06-20 05:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| 1c2d006e-096a-3491-aba4-8c1c98f1a66a | -11.952 | -58.7376 | 2025-06-20 05:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 097a2088-30d5-3f5f-8185-b6b8cb78f1c7 | -14.0404 | -53.3669 | 2025-06-20 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 018d7f67-3252-3bfd-aefb-77e904e989cb | -10.4944 | -47.0302 | 2025-06-20 05:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| a25984b2-2f68-325b-82fb-6725928bc4e4 | -10.4947 | -47.0078 | 2025-06-20 05:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 9b902378-8e9f-3000-a548-e9d1d7db96f3 | -10.5134 | -47.0279 | 2025-06-20 05:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 71f2afa8-029a-3acd-b87b-c2083f16f7fe | -10.5137 | -47.0055 | 2025-06-20 05:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| c9c60799-2d63-336d-9996-bcec96b7b5bc | -14.0404 | -53.3669 | 2025-06-20 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| d0e2b4bd-d279-32d8-a1f7-a91e653654dd | -16.3047 | -58.2676 | 2025-06-20 05:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| b5181a35-789e-3f71-89ba-8a6c39554117 | -5.30506 | -55.97194 | 2025-06-20 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd52dffc-7614-339c-a990-30541da4ebe9 | -10.86611 | -53.76079 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cef163a-63bd-3e13-808e-403e83561465 | -9.49139 | -56.0815 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64d1f542-7ce4-3ec1-8b4f-7011dca60742 | -9.4904 | -56.08895 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c6e211f-4ac1-3dd0-94db-fcb149d34b1a | -10.86342 | -53.76719 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| baef53c8-ea4a-3386-81b1-730885bc3ddf | -10.82835 | -54.01374 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 414d0bb6-4498-3018-9884-9f2014a64304 | -10.83519 | -54.01348 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1912e17b-6043-308c-9d4d-b8b428861775 | -10.8287 | -54.0126 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39849768-751f-342b-ad23-e8589e4764ba | -10.86472 | -53.75591 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f05a5462-f7e3-3164-ad88-72f02e334ff3 | -9.45793 | -57.84545 | 2025-06-20 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2dee1b65-27aa-3e31-9354-1899b53ad304 | -8.72692 | -64.16315 | 2025-06-20 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c1b9413-4aaf-39b7-853b-dc47c7b40879 | -9.47968 | -56.08373 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ad32c222-3634-3fc9-9c26-ff47431830d0 | -9.4587 | -57.83979 | 2025-06-20 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 42be57d7-0fe6-3a06-a273-987e577d2d65 | -9.92615 | -59.90197 | 2025-06-20 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdba8331-6423-3001-94fc-4a9182bf194f | -10.08348 | -52.74875 | 2025-06-20 05:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99498018-de45-319f-9cdd-d8493de1cbd1 | -10.85151 | -53.77073 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6ca70c9-0c43-3b37-809c-362091da76db | -9.48578 | -56.08075 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3b7ffe2f-bcb1-33e4-b2a2-783618dab1b9 | -9.49422 | -56.08858 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 987c4a58-d25a-3f07-b518-04774721bbb4 | -10.37053 | -57.50711 | 2025-06-20 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cd0b44e-7d73-3e42-a019-40a159bf25f3 | -9.48529 | -56.08446 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ad9aadf4-4f54-3b07-9de7-b51752401635 | -10.86543 | -53.76642 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9581297-69eb-399d-a950-6f551c5e159c | -10.85744 | -53.76093 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca406c64-f4ab-3446-b115-24e5b1f45e4a | -9.45452 | -57.8333 | 2025-06-20 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e96dd6ae-6251-31de-b4e6-cd510529e5a8 | -10.0773 | -52.74142 | 2025-06-20 05:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 808b2c7b-5642-322c-b134-3c8d281c56f6 | -10.85881 | -53.76578 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e70d6d1f-8f41-30f2-ba14-bf7a0a4013f2 | -9.49089 | -56.08522 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a72c403-85ef-3f16-bd50-0652aeef7623 | -9.45948 | -57.8341 | 2025-06-20 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ba7726b7-0950-3c13-a48c-65e9959b04e1 | -10.36062 | -57.50259 | 2025-06-20 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6ea9750-fadf-34d5-aa8d-873516a97ca4 | -10.86018 | -53.75449 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7395ac51-50a0-3f54-9d28-25346175691c | -9.45717 | -57.85109 | 2025-06-20 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 356dff9d-1e31-3fdb-aa98-5f0b2c2d7518 | -10.85018 | -53.76588 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d3c0c1d-d4d8-3886-ac7d-acadcabbc30e | -9.38061 | -63.42608 | 2025-06-20 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7454fa8e-4d53-3d25-8e5e-dbf1231a8dbf | -9.45374 | -57.83902 | 2025-06-20 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e01a551c-8e4e-3ca0-85a2-e3acab409b24 | -9.48067 | -56.07626 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ba7f68fc-ce96-3813-9598-c0b8e33150cd | -9.49468 | -56.08485 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9940ec24-9d15-3f71-bc44-2ccb1a4b4616 | -9.38002 | -63.43002 | 2025-06-20 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40732a76-86fc-3acf-ac1c-bedabe160a2e | -9.48017 | -56.08003 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fd9a5575-2bc6-3896-a486-5ed9e3b60ca1 | -9.46367 | -57.84053 | 2025-06-20 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4480145e-c3d5-3095-a57b-3f333ab87c24 | -10.83485 | -54.01463 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fac640a2-baeb-3f8c-b6b1-c0ddb84462a0 | -10.86407 | -53.76158 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b5b4211-d960-3922-b6ee-96c9814387ee | -10.66964 | -56.55505 | 2025-06-20 05:42:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b790a4c0-d304-38a1-bbbb-bb17370da805 | -10.67011 | -56.55133 | 2025-06-20 05:42:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8122c03a-444e-36b7-b423-cc5c46ea62ca | -9.496 | -56.08973 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51ba97b2-6773-34ae-8d53-414247ef83a8 | -10.85949 | -53.76018 | 2025-06-20 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7edd494a-1a71-384d-9408-eff2dd3aab02 | -9.4965 | -56.08599 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da053e3a-add6-3faa-b1f6-aea4984e1634 | -10.07653 | -52.74786 | 2025-06-20 05:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b72923e6-141b-38e9-999c-12e44cb0a4e8 | -9.48628 | -56.07699 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 59f5f5ac-0974-3bcf-9aef-37607cc8fb7a | -10.36021 | -57.50568 | 2025-06-20 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1702bb5-490d-3757-8c77-92cea24ad005 | -9.46445 | -57.83485 | 2025-06-20 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9a60366b-65bf-313c-a94e-05356464b75b | -9.4848 | -56.08817 | 2025-06-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97c9d28f-8c8b-30d6-9e7a-4283790674ab | -13.14754 | -56.80796 | 2025-06-20 05:42:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d6fb5c8-16cd-39b1-bceb-f630bf696c59 | -9.93751 | -65.01065 | 2025-06-20 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| adb97dcf-d19e-3ab9-9993-4f631218d332 | -13.28882 | -57.08511 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b68b373e-d6bb-3120-9e94-c6528cc5c2ea | -11.95238 | -58.74987 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e5fb3da0-197b-3aaa-b14b-01472de23526 | -12.55659 | -57.70901 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5d6b71e-4a86-3282-9ede-3c1f1ebedec1 | -13.77667 | -54.19406 | 2025-06-20 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c19f9287-1731-307e-9c7b-cb9d988031f4 | -11.81459 | -54.50256 | 2025-06-20 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ec4ec82-087d-335d-9076-93765ce1ecc9 | -12.04151 | -63.77617 | 2025-06-20 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5bf3b26-4cb3-31bb-a2f9-364afbfc0c36 | -11.94918 | -58.74792 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0ba83990-b4cb-3458-a9d3-1714179253b2 | -14.03254 | -55.12522 | 2025-06-20 05:42:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe80e7f4-92f9-3f78-9a26-43518120f9a4 | -13.77854 | -54.20248 | 2025-06-20 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 237d06a5-47eb-3a09-83e6-89fa5c5ef751 | -11.9517 | -58.75529 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e2b8a3a-7fb3-3253-bf9c-498dd9cfaf0e | -9.95421 | -64.99133 | 2025-06-20 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17edab44-1ece-3b01-883b-726c9216e01d | -12.05215 | -63.77778 | 2025-06-20 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1137a532-9009-38d8-92f3-dbd2676f1243 | -12.42804 | -54.8784 | 2025-06-20 05:42:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32bedee0-8d33-3b5b-9e0c-8ec2fcedaf4b | -11.95588 | -58.76121 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 73a0a166-747d-3654-9cbc-e98111dae77d | -12.50682 | -58.34985 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b25026f-68c6-3ca0-a886-763aa3cf819b | -12.50719 | -58.34695 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf10e1df-626b-3a59-b5ef-7b76c9624ce7 | -12.02618 | -57.09294 | 2025-06-20 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66273a6f-6ab6-3f12-9f1b-791dd114a1cd | -11.81302 | -54.501 | 2025-06-20 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c20e5092-3604-3cfa-a5ce-1f21ca9d6482 | -12.05569 | -63.77831 | 2025-06-20 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c1e0b56-894f-38c9-a791-71353fa8b496 | -11.53097 | -56.98093 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd2b4624-9008-3a49-947f-d1d818dd4af2 | -12.5122 | -58.34766 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a46b8f0-ec70-33cf-826b-aaacd1f5aeba | -11.53394 | -56.98861 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f15f341b-37ea-318a-97b2-3a13ca5ba6a8 | -11.53012 | -56.98792 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 512e9959-8400-31b9-8d1f-ea3efe63bb9a | -12.50532 | -58.36144 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c4e62b2-3ef5-3e29-b7e4-753e22159348 | -12.0486 | -63.77724 | 2025-06-20 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c62b185d-b5de-38bd-8dd6-c4275bda4997 | -13.29436 | -57.08567 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3334bb7d-2a96-35e3-aa07-0423fb6db983 | -12.8976 | -56.98543 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8429c257-97c5-3531-b653-7b7b4ebbd469 | -12.55176 | -57.70498 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24088c28-0000-32b8-8d63-bba730d0268a | -13.14363 | -56.80764 | 2025-06-20 05:42:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
