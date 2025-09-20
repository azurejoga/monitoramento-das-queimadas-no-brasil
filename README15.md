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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b9abe96-3e9c-338f-93ea-02906f3e89d7 | -10.67422 | -46.43632 | 2025-09-20 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0e7167b-72f8-3f9f-93af-9e9c4432c452 | -9.51216 | -54.66124 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2cfbafd1-0971-3421-86fd-f333bd7d07fe | -10.48612 | -42.414 | 2025-09-20 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d16864d-17a1-3ea3-9602-9dd338d3c7ca | -11.63909 | -52.85798 | 2025-09-20 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6430414-0857-3c5b-8ea2-47dc3a025970 | -10.87749 | -47.79615 | 2025-09-20 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58ea45cb-393d-38bb-8655-5ad91b74e3dc | -9.04261 | -44.95494 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa673e32-88e8-3407-8881-4c09c853c5d5 | -12.0795 | -44.84557 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f25a17ab-48d7-3b8a-b8e5-e7046653539f | -13.78517 | -44.38144 | 2025-09-20 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36dc0831-7fcf-3ae8-bd8b-6ad6a1d28a51 | -9.39435 | -54.68658 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7e54b83-07a7-3e77-ad8b-c33de3a595d1 | -14.34031 | -43.61067 | 2025-09-20 04:27:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 352cfbe9-a75f-3315-994a-e14338aec503 | -10.27484 | -36.33217 | 2025-09-20 04:27:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7e3df7eb-5d00-3801-a277-47d266db4537 | -13.24051 | -44.16338 | 2025-09-20 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbb2f7d4-41da-3b39-9bb5-6b12de4a74b3 | -9.02069 | -44.89075 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d5ecfc6-4a25-3873-b898-0ace4fc1edcc | -10.62637 | -46.43906 | 2025-09-20 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b28106ce-6a5e-375c-adfa-91797720ec5c | -9.39933 | -54.6895 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0104f58f-6912-3e25-8119-5289c1660ed4 | -16.31608 | -43.06866 | 2025-09-20 04:27:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e5336b9-0a6d-3465-942d-bf4369078b91 | -13.07032 | -42.14388 | 2025-09-20 04:27:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| ff60a6ba-bed6-331f-99ab-36250043ac02 | -13.8717 | -43.49232 | 2025-09-20 04:27:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb76a5ba-4aff-3607-ae04-ead13bc4c961 | -11.15912 | -45.33062 | 2025-09-20 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9af35738-b6a3-3d7b-829f-085392eeb85c | -9.48366 | -54.43853 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e9b3b32-7e3d-3731-9ab0-6f77125b15cd | -12.09493 | -44.81474 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 581cb69b-5680-30e0-8142-63fe00d8f32f | -10.3722 | -48.00126 | 2025-09-20 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 48a53a14-48ed-3b7c-9948-a628c076feb8 | -14.43158 | -46.50985 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15299dc2-abf9-357d-acdc-1e5d73263664 | -10.49016 | -45.16538 | 2025-09-20 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea0856ad-e4ea-3605-88fc-a38b45a8ad0f | -12.26278 | -45.27878 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f0708a9-0fe0-370e-9031-0398f3e2604d | -13.66371 | -44.31419 | 2025-09-20 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff3495ef-af2a-3143-abaa-771b9da0a851 | -12.07777 | -44.83282 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b77c3fc-2b59-3b8e-bf79-09aa1d1f2099 | -11.28828 | -47.41502 | 2025-09-20 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3621bf87-ddc9-364b-9cfa-9579ae117b44 | -11.63377 | -52.86454 | 2025-09-20 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4c493c8e-e5cb-3b93-b75d-8d06cabcd06c | -10.68364 | -46.44149 | 2025-09-20 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6090b846-23c6-32a3-b539-1d99d79567b1 | -12.15627 | -44.93906 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1c8627a-dfef-3dc2-bc51-75a6821c4791 | -10.60244 | -49.64457 | 2025-09-20 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dffe5025-a0a8-3af8-8738-bc83cc39f4d4 | -9.22943 | -43.31625 | 2025-09-20 04:27:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 878aa283-69ad-331b-b17f-8d9041d12f4c | -13.07509 | -42.14018 | 2025-09-20 04:27:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 59dc9dba-53c5-3ff7-88c9-72af9cab0b2d | -11.34245 | -43.4775 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 550f2213-b8d1-305d-bb6b-9d15799d8010 | -11.51139 | -43.62553 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4d7c099-0353-3467-ae54-539cc5202847 | -9.16873 | -44.63069 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d493697-9e70-3e03-8fa2-f46474d98703 | -9.02582 | -44.88009 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8853a86d-13cd-3d9f-a794-fb79709a8d52 | -10.23727 | -54.19047 | 2025-09-20 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8e9be7b-2ebd-327b-b6ae-23f15f24f060 | -16.32022 | -43.06921 | 2025-09-20 04:27:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e9f11f0-eb55-3f1b-9538-f0ad63a9176b | -10.68697 | -46.44202 | 2025-09-20 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76834af8-da96-34e6-96b2-90923fe51e21 | -12.27669 | -45.28101 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25909c1a-a95f-38b0-811d-72cdd9a1bd09 | -8.82723 | -47.24659 | 2025-09-20 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1693419-be18-3a9e-95ae-d1477e776aa4 | -9.12707 | -44.64807 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 819b1e2c-0588-3fc1-93bc-44c77474ddaf | -8.92196 | -44.4951 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6b00b17-9699-3275-bd12-60503d59e23d | -9.11958 | -44.67452 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e39aee66-e7d5-39ed-9853-0a6a6807b100 | -13.78433 | -44.37904 | 2025-09-20 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d0afb55-d51b-38ec-92ed-c1f507b2330f | -11.63441 | -52.86089 | 2025-09-20 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d43625eb-b85e-3150-bf0e-6a49b9fe178c | -9.35527 | -54.52162 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25fe9622-76ad-39ac-924b-9f5621c9dbbc | -12.08724 | -44.81774 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd3d5bb7-8869-30c2-a2b7-80c7220f42c5 | -10.60308 | -49.64072 | 2025-09-20 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e58efb59-da10-37e9-9c69-a7b3f119c32a | -9.01978 | -46.31619 | 2025-09-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2cbd5b1-c27e-31e4-a9eb-6188025dba6a | -9.02357 | -44.89489 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f541b820-b2f8-3012-8903-0112e8d76087 | -10.02074 | -46.24285 | 2025-09-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 252c4ebe-cb39-3bc0-97e3-aac119a9c337 | -10.48615 | -45.16866 | 2025-09-20 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b87e3b43-c777-3fae-9b49-9e07cd6cb21f | -9.02982 | -44.87683 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9754268-9e12-31d0-ab12-60abfbad3c13 | -12.7324 | -47.79264 | 2025-09-20 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be8eb619-b922-3db7-be21-b76295676eb8 | -14.4344 | -46.51419 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b8f617be-fcdb-331a-8006-5bce2b71486e | -10.23643 | -54.19508 | 2025-09-20 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a84b0505-3544-3ed2-a664-1997efe9091f | -14.67629 | -42.48745 | 2025-09-20 04:27:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2cb52607-2f3d-3b5b-9df1-63b73ec9d3a8 | -11.63504 | -52.85724 | 2025-09-20 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ec75112-e0b1-388d-817d-4981f2d2776e | -11.15856 | -45.33445 | 2025-09-20 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 710e45eb-8b9e-3a50-8268-05510d9bac61 | -9.03383 | -44.87357 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0edfcf6b-28d1-33fb-9000-228885a391f4 | -11.673 | -44.88174 | 2025-09-20 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 132db8ed-4785-386b-bc09-37f243cc9250 | -10.84751 | -42.80109 | 2025-09-20 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52c2eb7e-da7e-37ee-8c7d-a96bb865f97d | -10.33388 | -46.48391 | 2025-09-20 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dab4e0d0-30c0-3911-b261-f9f748bbfea5 | -12.1592 | -44.94365 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8959259e-7141-3f29-ae3c-a00ae2716479 | -10.23762 | -48.05542 | 2025-09-20 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 80ae0dcb-c286-37d0-b260-61174c349edc | -12.08014 | -44.81674 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fe565c6-75d8-314d-a586-e392c8e5feb2 | -10.01742 | -46.24231 | 2025-09-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f441dd5-26ea-36dd-92e7-914a2f937c48 | -11.3431 | -43.47285 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a683904c-b16d-3dfa-9930-22892ca34f67 | -10.87766 | -45.43264 | 2025-09-20 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f9bdc36-bf88-33dd-8c95-85614f278dfd | -11.45292 | -43.54425 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93bcfaf3-bd71-3152-8562-693962657756 | -12.07836 | -44.82881 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53a64d01-006b-3336-b089-5614509db16a | -12.086 | -44.85056 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9a28a63-ad04-3b98-a518-0383f8034070 | -9.40954 | -54.68385 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ddaa9eb2-5f36-3625-888a-00bf35ed127c | -12.26974 | -45.27988 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cbb758b-90af-3f38-b78d-776300738797 | -10.04811 | -46.24035 | 2025-09-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dbce6d3-8724-3fcc-b250-0aac14a609da | -10.24093 | -48.05597 | 2025-09-20 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e4b86b0-18f7-3282-af5b-07b4204cd3c3 | -9.4 | -54.68229 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69c07b8b-0945-3fab-ba6a-43746bd12406 | -14.4378 | -46.51464 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29b7d64b-e8c9-318b-9c64-ea619586fcfa | -10.87368 | -45.43594 | 2025-09-20 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0ab05a9-35ff-3311-b12b-d3cf57dee92a | -13.22827 | -57.12709 | 2025-09-20 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 505482af-21e6-3add-81da-b2bb4b9ebe3a | -11.27893 | -47.40995 | 2025-09-20 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3ae9b82-b50b-3997-8371-8e9de45edf4c | -12.08071 | -44.83743 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b532a63e-bc12-38d2-9c5c-2a0235d8c785 | -9.2844 | -41.05092 | 2025-09-20 04:27:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3db39888-bda2-3ba8-9aa8-614624abc696 | -11.47219 | -43.57079 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98658f66-1b45-3f23-aa12-8d273df31ece | -9.17102 | -44.63901 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e29ee55-f04f-344c-938e-52d36af7ad0b | -12.47601 | -44.75381 | 2025-09-20 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 925f6e20-42c3-396b-965d-8d5864095390 | -9.01096 | -48.0195 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a7184f-0674-30cc-bfff-1ec79098b44d | -14.44913 | -46.50852 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b6fd5c4b-2f16-3c61-a67f-c61213bd797f | -12.14457 | -45.01855 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f321bf2-b7a4-330c-9f7e-5065b240f743 | -11.63035 | -52.86016 | 2025-09-20 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2210b60-e817-35a5-bbb4-085fb0d08ba7 | -8.95054 | -44.20443 | 2025-09-20 04:27:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 953cfe19-c2b4-3bf2-bd5c-7e25c3579e05 | -10.11744 | -44.75228 | 2025-09-20 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f176de5b-760f-3967-a330-3bac9aa6591e | -10.87962 | -45.20768 | 2025-09-20 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8befd7af-68f0-35ab-8519-6f855c915300 | -13.53335 | -44.12104 | 2025-09-20 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dcdffe1-b531-3f55-b420-88addc2dd879 | -12.08305 | -44.84606 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 276db1c6-64d2-3f7e-a4f5-5f349cf2ecc7 | -13.53399 | -44.11645 | 2025-09-20 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4265e911-d6e7-3e9e-9023-d12a7f82f019 | -9.17161 | -44.63512 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README16.md)
