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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49bb0ac8-5241-3796-a38e-c1cb508799c5 | -14.16057 | -45.47923 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1144cd4e-9bc9-3f7d-ac59-be1cf1782c3e | -14.69234 | -45.10546 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57d140f7-3175-39f5-8471-d34d4b8f3ee0 | -11.36266 | -55.1253 | 2025-05-21 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da56292e-f5b7-3b61-abd4-3fc7515a050e | -16.04704 | -43.80599 | 2025-05-21 04:17:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf978784-6aba-393b-8795-7c157ea42608 | -14.17106 | -45.47731 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c90061e-10b2-3664-92d2-9e16f1934bfc | -15.07865 | -48.9432 | 2025-05-21 04:17:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4175e116-cbf1-3f5f-b31b-330bbd20fc2c | -16.03104 | -43.68089 | 2025-05-21 04:17:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38faa9f4-34e2-37fd-a286-6f801d835c92 | -14.16332 | -45.48333 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afa3f692-5a95-39c4-be8d-f685c57dccf6 | -14.04655 | -45.51106 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bec31c77-9fc2-3c84-98a2-6a79d82632b0 | -17.70443 | -47.50022 | 2025-05-21 04:17:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4db79c0-2de8-3d88-86c5-cfc37b19f18d | -13.58263 | -47.36173 | 2025-05-21 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6b7ba0d-47bd-3441-b854-d7b3296f5b37 | -12.47992 | -57.19125 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dda61b5d-d883-32bd-b518-80135a468007 | -12.72529 | -54.9772 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ce5e8b6f-cbe8-3343-b281-3cd4b525fa98 | -13.61647 | -55.46093 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fb5aed6a-583f-31b7-a6c6-d80603c3fe8e | -13.61731 | -55.45663 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cae1f0ac-cf96-3afe-9825-d1f03e44339e | -25.19038 | -49.32785 | 2025-05-21 04:17:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 79fe223a-e2dc-369c-81a4-c98226e5a679 | -14.04215 | -50.51982 | 2025-05-21 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf7db283-7530-3293-a4b1-795456bae3dc | -11.07635 | -54.77454 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5a17f3b2-fceb-3148-809b-077999c26cc6 | -14.16663 | -45.48388 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39d2ed86-5173-3f66-9465-f2128c681e17 | -12.43374 | -43.72759 | 2025-05-21 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f82de51d-c857-3ef8-8084-12316625c14c | -12.10595 | -44.76269 | 2025-05-21 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb51373f-1779-3451-b1b6-5fcb5b7bca20 | -11.35511 | -55.13287 | 2025-05-21 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7ad4894-38ea-3d88-b47d-08a39d2b1711 | -13.32196 | -45.40144 | 2025-05-21 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86040e4d-2986-3c6e-bdf7-2c795d020e80 | -10.82337 | -56.96077 | 2025-05-21 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d189313a-6494-367c-9568-38c2e0a2ac94 | -23.10263 | -46.21704 | 2025-05-21 04:17:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2d60a74c-6cce-37e0-b171-b2af686c3604 | -11.07556 | -54.77858 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a08956bd-9991-3f68-b100-d16ceca187d1 | -19.51232 | -44.27816 | 2025-05-21 04:17:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6146d11f-9031-3eef-ab62-5026288e9d00 | -14.33867 | -47.17891 | 2025-05-21 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 962b5954-9cf2-3e40-badc-823fac64042b | -11.6469 | -48.10756 | 2025-05-21 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 717f2619-5fe7-314e-869c-160a70f5e8f2 | -18.87499 | -50.15771 | 2025-05-21 04:17:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb24eafd-28f7-3765-92dd-2885c4376b00 | -14.02144 | -55.13343 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51d90471-ef5a-317a-b4ef-1b75abd3d5be | -11.57822 | -54.56999 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2be943ba-1b1e-382e-a21d-6b9bc2a7df3f | -12.72683 | -54.96929 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a76eef5-6dad-3ef2-b4af-404aece7230f | -18.87224 | -50.15491 | 2025-05-21 04:17:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ab874b4-72f1-3e8e-8a78-d4ff50d0f863 | -11.57898 | -54.56608 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22fce830-88e3-385a-b808-7dfb4b2a5943 | -16.10656 | -43.63904 | 2025-05-21 04:17:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76d6837c-ad2a-3cbb-b414-d26bb32d9e17 | -12.72328 | -54.96989 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b08aca40-c028-3375-9429-c8b0ad638aa8 | -15.27195 | -51.4691 | 2025-05-21 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 663f650c-170f-3731-a0ea-95b2503aca58 | -12.3407 | -49.96025 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| deda3dda-ceac-3ad2-a93c-a827d8a67ab7 | -14.16445 | -45.47622 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2cff246-2a49-34ec-bada-5818b52841a6 | -12.37015 | -49.97794 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ba96430-0c40-37d5-94c6-b1f2e5f50580 | -12.4811 | -57.1857 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fe39821-387c-3363-8880-e04ca1ff8b98 | -14.06024 | -53.37846 | 2025-05-21 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 216d6dcb-d040-3840-9bf4-57c736d7811c | -20.95523 | -56.61119 | 2025-05-21 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39a2d5dd-37a9-3768-bc02-492f4f210354 | -12.87357 | -43.18156 | 2025-05-21 04:17:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6a71a7ca-7127-3b69-b3f3-e992970c47d6 | -12.13392 | -54.66428 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60c46f83-833a-365f-b297-e119b13e49fa | -14.15452 | -45.47457 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74663e81-49fe-35fa-bda2-e2b58e3a91dd | -12.3366 | -49.95951 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5bbf7d1-73c5-3685-9056-5bf1c6d2260b | -17.23732 | -48.24121 | 2025-05-21 04:17:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25a1c635-6bd9-34f2-9bcf-b90c27a19619 | -13.32915 | -45.39898 | 2025-05-21 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0130baec-acaa-3547-8733-887bef2e2f78 | -15.19252 | -48.28585 | 2025-05-21 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cde15ba1-c967-3566-b0f0-018a7787b8cf | -23.35108 | -46.90359 | 2025-05-21 04:17:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e0a44489-88f3-37f1-ac15-d8847c6bdd2b | -12.12907 | -54.65939 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 387b7333-2c0a-3643-a4c2-2f935f95eb64 | -23.44755 | -54.17708 | 2025-05-21 04:17:00 | NOAA-21 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 48167f94-b3ab-3b6f-b37c-651d0df1caee | -17.14956 | -54.01414 | 2025-05-21 04:17:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 121c6264-016e-3fed-b3e1-622bc40e4985 | -13.99833 | -44.0315 | 2025-05-21 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d541868-1eff-32b4-a2b0-8d720197ab4a | -14.16775 | -45.47676 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d97375c9-df03-398e-a511-9326cd643c86 | -22.8606 | -47.61859 | 2025-05-21 04:17:00 | NOAA-21 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5066cfee-eda6-3889-80f4-722a3c447ba8 | -14.30937 | -41.76139 | 2025-05-21 04:17:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d97363bf-de87-3a8c-8b9d-4c38a91cb7ab | -15.04678 | -45.66447 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e7159fc-3a55-3eb9-9624-b0b837cec1cb | -23.98455 | -48.91659 | 2025-05-21 04:17:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 694734df-156f-3a6b-aa5d-f51d084e23fd | -14.67748 | -45.11391 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ab80d53-a6f8-31d7-b4b8-9fc354bc1d6b | -12.43097 | -43.72351 | 2025-05-21 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d102d8eb-4283-3fd0-9dbf-7187cb724452 | -11.29282 | -53.97567 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e17f99e1-5746-325a-bce6-5c380ab80cb7 | -12.87302 | -43.1852 | 2025-05-21 04:17:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c273493e-86a9-3481-82a3-1cc9bbad9df9 | -13.61327 | -55.4519 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 49e1972e-32ef-3781-95ac-0d47d1e53a2c | -12.30474 | -52.47762 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c55164ba-88f2-3e18-b9e2-0f5946624e7d | -15.79355 | -41.27964 | 2025-05-21 04:17:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 462727cd-192c-35e0-a38f-45d1049ab49c | -11.07477 | -54.78265 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9e5441e4-7992-301d-89d9-4578e0baa2fb | -14.69509 | -45.10955 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a43c278b-2c7a-3f18-a1d1-b642fcae5149 | -14.15896 | -45.46801 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8a8e9b2-e2df-3e1b-97cb-5e22006fa1e1 | -11.29829 | -53.97661 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75d38cf7-ad44-3de7-9c43-1e21f6a1ff77 | -10.82586 | -56.95944 | 2025-05-21 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d5b68efb-2b32-33a0-a3f0-e935c1e54673 | -12.293 | -52.48673 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 48abbdf1-bb8b-3e49-9728-1ffc111d2801 | -12.83912 | -47.39324 | 2025-05-21 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba3de7e2-e0e2-33bd-a092-e551443dc520 | -10.83 | -56.96185 | 2025-05-21 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d778937d-7f8d-3df3-b584-ce54a4925375 | -14.67474 | -45.10983 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79bf756b-f065-3562-8307-b02c14fb1a33 | -11.0879 | -54.77655 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9399664c-1b80-3f1c-bee3-20ae1c902c41 | -12.37083 | -49.97414 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d442a4ac-8b9e-3cd9-becd-7b52db84b1b1 | -14.17381 | -45.48142 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cf29851-b8db-38f0-a092-5f78d318d72c | -16.6801 | -43.88565 | 2025-05-21 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebcba9fa-56cb-37cb-852d-0ff9272d1053 | -14.15839 | -45.47157 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a4b6318-c0ab-367e-bf78-efcc7cf4c697 | -15.89372 | -46.00953 | 2025-05-21 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9eb584ff-67f6-3ac9-9582-47e3a75d0cf9 | -12.29402 | -52.48128 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d089678b-b1d1-39d1-bc99-30f8988e8289 | -14.68519 | -45.10792 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bbbb602-5809-335c-abca-0aa1a807b947 | -14.1617 | -45.47211 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe6023f3-5690-3458-9478-febe6c9aa2d9 | -12.30271 | -52.48857 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0fd096c3-3ff6-37f5-957b-048c6ad2d218 | -23.40789 | -46.5554 | 2025-05-21 04:17:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 961bb45d-78d1-3787-a464-afb2fa2faf4e | -20.95062 | -56.60649 | 2025-05-21 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a41b27d-96fc-3d72-9890-f9a7fab56802 | -12.33938 | -49.96783 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f00e2c1-866e-3e65-b315-b7d65553c06f | -13.66376 | -53.93338 | 2025-05-21 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 453ce4e3-7940-3a0d-a42c-b547760cf37e | -12.28712 | -52.49131 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 79ce7cb1-1fbb-3712-9f91-f7e9d69789b9 | -13.6124 | -55.45613 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| eab06bad-066d-37b5-b5a7-909ab163ca5b | -12.35785 | -49.97563 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57990408-a9d7-398c-8214-c7b1e28232b7 | -23.6067 | -49.01077 | 2025-05-21 04:17:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18802496-f110-3faa-b00d-db568110f045 | -13.61901 | -55.45301 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8e6b5237-6f0a-3105-af1a-64f14cd00479 | -14.69068 | -45.11609 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 316af3dc-fea3-3ee1-aab1-0e815e8f6259 | -11.29285 | -53.98123 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dd14d001-3741-3a34-8209-1f6a6314310b | -25.02257 | -49.40625 | 2025-05-21 04:17:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f7f5e27-b015-36dc-b82c-b0d705f1e1e6 | -16.73953 | -45.76262 | 2025-05-21 04:17:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README10.md)
