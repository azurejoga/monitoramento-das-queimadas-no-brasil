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
| 53a2e470-9fb2-39ea-a260-89b19c482a1a | -8.67285 | -49.94684 | 2025-07-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cb5dcc4-43ee-3863-8f08-44116c458fec | -13.16797 | -47.28494 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a0b35f2-c917-34b2-9406-d1e6c077fe0c | -10.5776 | -49.1316 | 2025-07-11 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 7ed7d291-a04f-365a-b14c-719e1fce6a4f | -10.6672 | -49.4895 | 2025-07-11 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8a90a69f-ccae-31a5-a6c1-e8f49fb2d7e5 | -9.9148 | -47.8282 | 2025-07-11 04:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 28934f79-e582-34e5-ae30-f786178984bc | -10.6862 | -49.4874 | 2025-07-11 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ec66a621-3477-3d81-8199-600fdc9d077b | -14.3109 | -52.74689 | 2025-07-11 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bed84c1f-fcba-3d24-a1d1-9ace167c9157 | -21.68744 | -49.49656 | 2025-07-11 04:10:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 5c5a28b3-1a17-303d-ae8a-49ebdb2f9343 | -14.31089 | -52.74358 | 2025-07-11 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d80a7a9-e7b1-3607-a8d4-695c794466cb | -19.43873 | -44.34016 | 2025-07-11 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 700aaf10-a6fa-345b-8cee-5c97bd1a33d7 | -21.26967 | -48.57094 | 2025-07-11 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b259077-fc4f-3ee1-aee0-fde121d48be7 | -20.87223 | -44.24189 | 2025-07-11 04:10:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b58065b2-5452-3738-a5c7-d9e3b40ff086 | -20.59733 | -51.61129 | 2025-07-11 04:10:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3e025271-39b5-3eaa-bf3a-e1d69a722c69 | -21.53351 | -49.52779 | 2025-07-11 04:10:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 31a94cbb-e132-391a-9224-b8525defb9ba | -21.687 | -49.49852 | 2025-07-11 04:10:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| e00d0ab2-52b2-3779-a158-7c7ab6314b70 | -21.27328 | -48.57169 | 2025-07-11 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be0f75fc-1710-3767-962a-5b728ce86126 | -19.59896 | -44.81295 | 2025-07-11 04:10:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dc110db-5fb8-3f38-aa32-61ea0593f78e | -15.797 | -41.96799 | 2025-07-11 04:10:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 465ec892-49ae-34d7-911a-c9227f1edd76 | -20.32314 | -55.00741 | 2025-07-11 04:10:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 896e52eb-6eb3-3a6c-8fd1-5e08c170afc2 | -18.88481 | -49.05382 | 2025-07-11 04:10:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1b9c6f7-04ab-3927-8408-8d106cd12ef8 | -19.59838 | -44.8166 | 2025-07-11 04:10:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22203021-d247-3a0e-a1b8-e895c4cf373c | -19.44518 | -48.53451 | 2025-07-11 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8606bd7d-580d-3a4d-bc09-af31f3fb6f5a | -21.30085 | -48.56354 | 2025-07-11 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b26fe4ae-6ee2-3bca-927d-f7c4194dc8af | -16.0496 | -43.80027 | 2025-07-11 04:10:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd3ec4b3-0aa6-34ee-bca5-596ec9a1b797 | -20.99404 | -51.79184 | 2025-07-11 04:10:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1857a8cb-9e51-3b26-bc3c-773e2936d570 | -16.03823 | -43.72137 | 2025-07-11 04:10:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3e01c32-d242-3791-94be-da6af55a41be | -21.32141 | -44.2329 | 2025-07-11 04:10:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bcc77fd5-1965-32b4-ae63-ac75293581cd | -14.88874 | -48.38384 | 2025-07-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28880017-a610-3aed-aba1-14c692ce4c3c | -18.04832 | -48.90034 | 2025-07-11 04:10:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fb4ff16a-f312-3d0c-8959-1c229dc892f6 | -19.97058 | -54.33918 | 2025-07-11 04:10:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b967f3f7-f689-3c60-8288-e0e378ae5e1e | -15.36136 | -49.48679 | 2025-07-11 04:10:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ce2dcea5-cd03-302f-82df-b58067cf55f8 | -14.31154 | -52.74359 | 2025-07-11 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89eb03b1-9092-30cb-be5b-fda7c1206f41 | -16.06002 | -51.55801 | 2025-07-11 04:10:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60027997-fda4-3f1c-aab5-eb17403cf967 | -15.36064 | -49.49078 | 2025-07-11 04:10:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 839fd3e5-da5a-37ab-9e02-4f3129a14516 | -16.94474 | -49.4361 | 2025-07-11 04:10:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 084c5890-53f2-3c99-aa20-0c0f68482b14 | -21.99956 | -46.80203 | 2025-07-11 04:10:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b0b65db-6127-3c7d-b815-66e37034c52f | -19.44885 | -48.53531 | 2025-07-11 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7d00ea6-5ff4-3c5f-97f7-454ffa9dbb85 | -20.77784 | -49.6133 | 2025-07-11 04:10:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 57f2c32e-4699-3374-a1c1-936319d9e9fd | -14.31613 | -52.74466 | 2025-07-11 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fe3cc84-709e-3581-8018-df9087a7fcdd | -18.96898 | -54.37865 | 2025-07-11 04:10:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97cf6561-7d1e-36cc-85b2-40e6030c95ad | -19.51301 | -44.27797 | 2025-07-11 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a6d90fa-7210-3db8-be49-326a174624a9 | -18.65483 | -48.21656 | 2025-07-11 04:10:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5e38a3ab-3d8e-34ac-9e6c-e46010ce0ae0 | -19.97076 | -54.3385 | 2025-07-11 04:10:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41846582-5c98-37ca-a877-22cfe3a8a931 | -18.64639 | -55.7333 | 2025-07-11 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e956b846-538f-35b3-a45c-2c03460eb2b9 | -20.62766 | -43.7756 | 2025-07-11 04:10:00 | NOAA-20 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 293ed69b-8000-3a13-ad7d-f02eb5b32a27 | -18.65986 | -55.72747 | 2025-07-11 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cd152565-8cab-376d-85ae-d8404a53a972 | -14.31023 | -52.74688 | 2025-07-11 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34b585d7-15da-3e8c-b016-1f00bb30cd8d | -16.59013 | -44.3984 | 2025-07-11 04:10:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2a1836de-46f7-3ed2-8d06-498b9a076bc0 | -21.68655 | -49.50148 | 2025-07-11 04:10:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c7fbfc64-0cf9-3bc3-a2e8-71db5f738969 | -18.79051 | -47.96068 | 2025-07-11 04:10:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 27485551-05d7-3fcf-b3c0-4c3c0a34c5a3 | -17.00698 | -49.78012 | 2025-07-11 04:10:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f402cb0-ecee-35c9-a044-36677e69c9fa | -19.08358 | -56.04721 | 2025-07-11 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c320578b-6077-30cb-bad5-92b7dbe5d27a | -18.6483 | -55.72457 | 2025-07-11 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 33283663-8850-33e6-83ff-c5db7390da2c | -16.03767 | -43.72495 | 2025-07-11 04:10:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40be5e64-0b1b-3906-b6a6-2fee3d91f79d | -18.66081 | -55.72313 | 2025-07-11 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 10408fed-e758-32eb-8966-44fc9cfb1945 | -19.46929 | -44.29671 | 2025-07-11 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5702fdc-4d68-3399-bbf4-c788596e06a5 | -19.44802 | -48.54004 | 2025-07-11 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22c7c633-035e-31eb-8e42-74606afe3043 | -16.13545 | -42.32845 | 2025-07-11 04:10:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ef3d3a5a-6652-36f0-8f51-a33a5f4b820b | -17.14986 | -44.72345 | 2025-07-11 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09a274d9-83c9-3ba4-8545-d5695b5dbedc | -16.06472 | -51.55898 | 2025-07-11 04:10:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1ad7702-34ee-32b6-8011-abb8534f4d8b | -18.68727 | -48.1202 | 2025-07-11 04:10:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d5ba86d1-2019-328c-8fdd-977efd872c1a | -21.68792 | -49.49361 | 2025-07-11 04:10:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 72065bbc-cd05-3ab3-89c0-2682d1da762d | -21.53728 | -49.52858 | 2025-07-11 04:10:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1f774e5d-c407-3a24-9d91-c1f680c9a66e | -19.08942 | -56.04871 | 2025-07-11 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2ff18bac-e095-3be2-814e-a4f7432c7981 | -18.2915 | -44.68147 | 2025-07-11 04:10:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 03c6b432-7395-32a6-a29e-03e6f3e0deea | -15.1878 | -43.68666 | 2025-07-11 04:10:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 31890585-c47a-3c95-8765-25a13c0c4ebf | -16.72227 | -49.22933 | 2025-07-11 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01d52a1b-46eb-31a1-ac35-1a494d292c28 | -18.6555 | -48.21898 | 2025-07-11 04:10:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1a911a4c-116d-393d-a901-0d1add6201f6 | -18.64926 | -55.72021 | 2025-07-11 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8ca176aa-0787-3651-95ba-1d3e25d811a0 | -18.68646 | -48.12471 | 2025-07-11 04:10:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a359cf53-f05a-306b-a285-844c95db20f4 | -22.87242 | -46.77052 | 2025-07-11 04:12:00 | NOAA-20 | MORUNGABA | SÃO PAULO | Brasil | 3532009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ce4a036c-b091-39ff-8f6f-b75eff81bed6 | -22.53927 | -48.81346 | 2025-07-11 04:12:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5a91764-497f-383f-962a-ac088089efbc | -22.27714 | -54.95668 | 2025-07-11 04:12:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5fef622f-1357-33c5-a88f-f7ac6d50913c | -22.27643 | -54.95993 | 2025-07-11 04:12:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f56ee4a-d003-3dba-847a-4d92397134e7 | -22.28522 | -54.94464 | 2025-07-11 04:12:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ed38f428-72d3-36e1-a9bf-19a64b2892b2 | -22.36682 | -47.70422 | 2025-07-11 04:12:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33840480-768a-3220-8e5c-56a17cd60c5e | -25.2571 | -52.23686 | 2025-07-11 04:12:00 | NOAA-20 | LARANJEIRAS DO SUL | PARANÁ | Brasil | 4113304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d19dff08-d77c-34ae-bcc7-298428fec9d9 | -22.27935 | -54.94664 | 2025-07-11 04:12:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 746beccf-e733-3816-8668-2fd0bec4705b | -25.253 | -52.23579 | 2025-07-11 04:12:00 | NOAA-20 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| db5bc087-9d6a-3d69-9e7f-9a4b1347e1db | -22.28374 | -54.95134 | 2025-07-11 04:12:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0668b544-248d-3108-bc3a-c094b7342cc3 | -22.28448 | -54.948 | 2025-07-11 04:12:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0bd38773-9241-3e7e-8ca8-02f61bfd5cf7 | -24.31617 | -50.85298 | 2025-07-11 04:12:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ac5391f8-1ca9-3daa-895c-7d0d279d30e1 | -23.33883 | -46.77089 | 2025-07-11 04:12:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c554189c-2418-3c73-9d23-d2436c172405 | -22.31127 | -49.13941 | 2025-07-11 04:12:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 678ff831-1874-351b-989e-2106040856c2 | -23.40412 | -46.55535 | 2025-07-11 04:12:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8d6bc1cc-9b05-385e-916f-32bf1f1afcd3 | -22.61122 | -54.95309 | 2025-07-11 04:12:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 73ec07ed-fcce-3799-b248-69e1e9f2b2d6 | -22.2823 | -54.95793 | 2025-07-11 04:12:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13584d9f-9dd9-3cec-94e6-6e037a66fbe5 | -29.8644 | -51.16592 | 2025-07-11 04:14:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| d9558598-a7e0-341f-ac13-887202798c60 | -10.6672 | -49.4895 | 2025-07-11 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 79220cc4-2ff4-35db-8946-95668982835c | -10.6862 | -49.4874 | 2025-07-11 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 790142e3-448f-39de-858a-ba70543c9022 | -9.9148 | -47.8282 | 2025-07-11 04:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b9f8c00f-6881-3e51-809c-099136eecbee | -9.9148 | -47.8282 | 2025-07-11 04:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0d3bfb91-ec74-3882-9abf-3a63a089641a | -10.6862 | -49.4874 | 2025-07-11 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 86eea7a9-de86-31b7-b240-774b82bc4ab7 | -10.6672 | -49.4895 | 2025-07-11 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6f59f874-675a-3fa4-ac47-c3ca3f09978d | -5.5427 | -43.9096 | 2025-07-11 04:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 9a53945d-625e-3087-bff9-092873abf447 | -5.5429 | -43.8864 | 2025-07-11 04:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 197f5289-88cd-3191-8323-a795177d9d51 | -9.9148 | -47.8282 | 2025-07-11 04:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a89c74cc-9226-35ca-82af-dbb5884ed5c1 | -5.5614 | -43.9082 | 2025-07-11 04:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6506ebe6-24b7-321a-8189-000ea4ac5fdf | -10.6862 | -49.4874 | 2025-07-11 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 0c8c3cca-62e3-331e-aab8-f13d23683470 | -10.6672 | -49.4895 | 2025-07-11 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |


[Clique aqui para ver as próximas entradas](README16.md)
