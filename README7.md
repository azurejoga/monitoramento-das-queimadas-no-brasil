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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ced1f254-5b22-38a5-ae46-0106a10386c8 | -13.23832 | -49.83798 | 2025-06-22 04:17:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60109f33-6f86-331f-a47e-7c9c70e12b7b | -10.12543 | -51.66504 | 2025-06-22 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08d5c030-ab69-30b5-8712-b49ae02959c1 | -10.5691 | -46.93257 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed5fc26e-55b8-3ed3-b67d-9d9904c16d76 | -13.27679 | -46.83484 | 2025-06-22 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98deca1f-0027-3a97-b15f-93118de9d0f9 | -10.86494 | -53.76547 | 2025-06-22 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ecd455a-f841-322e-9079-7890e7ed3795 | -18.05976 | -44.49545 | 2025-06-22 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f349b09b-dbb5-3d46-9e3b-285db669545e | -11.83748 | -57.76655 | 2025-06-22 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a620f06-ff9c-3566-bdfc-b5295cddbaa8 | -10.23412 | -54.29326 | 2025-06-22 04:17:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3d72adc-7b4a-3ef9-84be-8a30aae4e489 | -12.13714 | -58.1817 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61b61fa6-fb4d-3575-82da-448a4ca2500f | -10.23008 | -54.29736 | 2025-06-22 04:17:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6ce1824-f190-3c0e-b428-d121855c7250 | -18.73957 | -43.00327 | 2025-06-22 04:17:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 90f73318-1980-31bc-9ae8-dc12820945e9 | -13.65086 | -53.94125 | 2025-06-22 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88efda61-34c6-3448-b072-b9055be66a28 | -13.26995 | -46.83368 | 2025-06-22 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 818cdffc-602a-3c30-8ed6-1df4a382395b | -10.86024 | -53.7608 | 2025-06-22 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 769fa8ab-eefc-34e7-a3d1-ab22a7eaa75d | -10.57372 | -46.92825 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f901bb7b-ca96-3a8c-8fc7-9a16847d0b2e | -13.49722 | -53.50021 | 2025-06-22 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e98e37e2-d1e9-30af-a80a-26a9d98710ba | -10.43304 | -47.03136 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a1bb8aa-b4b0-39af-a26c-eafb148e59ba | -13.27273 | -46.83817 | 2025-06-22 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5a1a027-2ad8-3a93-bfce-277b8d099371 | -9.46796 | -57.84743 | 2025-06-22 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dfe71626-8eae-3044-b3a7-9a071d81c927 | -17.53588 | -46.97084 | 2025-06-22 04:17:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 068a7871-bd72-3c68-9f8a-806031e3da27 | -11.61969 | -58.2959 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3d4df40a-4b59-3e2f-b1d1-fce728f55ddd | -17.65703 | -46.85207 | 2025-06-22 04:17:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf34589e-f9d5-33a7-a8ee-5830b0bbf5c3 | -13.79328 | -54.29867 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcd323bd-2f06-381a-ab64-6ca59a17223d | -10.99096 | -45.09142 | 2025-06-22 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d549ea1c-31a6-30e9-a22f-56fbac144786 | -28.31744 | -49.22283 | 2025-06-22 04:19:00 | NOAA-21 | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6d088372-f75d-3492-add1-d9fc3f8d0b1b | -30.14957 | -52.02532 | 2025-06-22 04:19:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| ff12f9f0-1f11-3888-ae46-095f9ba9c29d | -29.86806 | -51.1647 | 2025-06-22 04:19:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| b2f2da46-4fb3-34a2-b1fa-55bd2a9ea00e | -29.86465 | -51.16392 | 2025-06-22 04:19:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| a9b36998-1538-33d2-99f0-ab476d036cdb | -19.85221 | -43.84437 | 2025-06-22 04:19:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7500ce1f-3398-38be-b4e1-c3b0030f883f | -20.41726 | -43.55428 | 2025-06-22 04:19:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6605200a-12f6-34bc-bb1c-71202b0d3dfb | -19.63466 | -43.89837 | 2025-06-22 04:19:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 638a68d9-74fc-338a-8f43-f09e3a4bdeac | -18.4937 | -45.07134 | 2025-06-22 04:19:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58a6ea7d-027c-3757-bd2b-3ec522e27ff4 | -19.63407 | -43.90246 | 2025-06-22 04:19:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 926ad4bb-0d92-308d-8ee7-ad3495df80d8 | -18.48981 | -45.07444 | 2025-06-22 04:19:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3067ba5-d900-31d9-8ac0-e26832ef1b02 | -19.98386 | -47.18099 | 2025-06-22 04:19:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a449b1d1-4e9d-3c2f-8103-24e0e235e22d | -19.64054 | -45.19065 | 2025-06-22 04:19:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f078aa06-da1c-364d-8cd4-6f1a0646759c | -18.42065 | -54.86703 | 2025-06-22 04:19:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d94c8d2-98ef-3da4-b5d3-6a3fff15b0e0 | -20.48803 | -42.38342 | 2025-06-22 04:19:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c2012189-0b8a-3cd0-8265-c06ba91ea4ac | -19.79606 | -45.8218 | 2025-06-22 04:19:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7cc5411e-94a0-3fe4-b7d8-c9a8423fcaed | -20.4237 | -42.22845 | 2025-06-22 04:19:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f0cc4ed6-0980-37f4-a424-8739406cae87 | -19.45619 | -45.30798 | 2025-06-22 04:19:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f047dbff-dc76-3dde-a7f0-b889863141f4 | -19.62491 | -43.81798 | 2025-06-22 04:19:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ef2fa7b-353b-3316-9e19-27cfc5e71dab | -19.4617 | -40.38886 | 2025-06-22 04:19:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e07b3a4c-fa57-3c42-92a5-1b2c21d5373d | -19.46261 | -40.39124 | 2025-06-22 04:19:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 29fe985e-a91f-368b-a7c1-1102c8219d2d | -19.81503 | -44.29494 | 2025-06-22 04:19:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b0a012cd-0a4d-3c9b-8f28-f0e49976c222 | -19.62432 | -43.82208 | 2025-06-22 04:19:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5190f620-f74f-3b44-9ee6-3a603c251ad3 | -19.61045 | -44.93194 | 2025-06-22 04:19:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b2d024f9-5318-3cc4-a101-a04e7484ea86 | -19.43726 | -44.34153 | 2025-06-22 04:19:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2753a693-251a-38ba-88c5-322b62d7e99a | -19.73823 | -44.17135 | 2025-06-22 04:19:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49f3cd9b-53aa-364e-9bca-6ca33af2cb0a | -19.47193 | -44.29559 | 2025-06-22 04:19:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2c183b9-e682-3e76-8f51-408a825a5a17 | -20.73129 | -41.90928 | 2025-06-22 04:19:00 | NOAA-21 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a1864c7a-ff68-3e0b-a4dd-5658d024d651 | -20.31149 | -45.58274 | 2025-06-22 04:19:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8324163d-4e19-3a68-8236-0b5e5a2fdeb1 | 2.75365 | -60.37326 | 2025-06-22 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4dcad643-bd9d-312c-a4ce-4a6f56b8cc3b | 2.75271 | -60.36703 | 2025-06-22 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dabad65-a455-3d42-beb9-acceb5f91d53 | -9.18661 | -45.33064 | 2025-06-22 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69949774-5179-33d9-8655-e3e2d2013b78 | -7.14573 | -48.20794 | 2025-06-22 04:40:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 555aad5e-b101-3b16-997d-902b6c44f549 | -5.57357 | -45.21743 | 2025-06-22 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd197c19-17e4-341b-8464-b2211b79eeb2 | -8.03168 | -47.64106 | 2025-06-22 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31c096e6-fe44-3793-a967-b177011b199c | -7.27589 | -45.36718 | 2025-06-22 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 115d1132-9ef0-3b4d-bdb4-5481ba8d4031 | -8.0699 | -43.10416 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2b21bfe5-55a0-3359-876a-134c9746f922 | -4.5471 | -48.01455 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15339aa9-1e53-3d21-867e-52d5cbfc5976 | -4.64309 | -47.96009 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 721e2b70-862d-3c41-8d19-3c0ec012ebe4 | -7.10522 | -43.71183 | 2025-06-22 04:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e12874b1-9621-375f-b145-4f8ea6f936e6 | -8.10623 | -43.14411 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 318e9bdc-0a1d-3dbc-94d4-089ead48b528 | -7.22601 | -43.52583 | 2025-06-22 04:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b3ba09b5-80dd-330a-9784-adbe33853f29 | -8.00629 | -49.71617 | 2025-06-22 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c462bca8-792f-3619-9477-d2bef5a8ff86 | -3.60905 | -47.54272 | 2025-06-22 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c40f49d-5b0b-3bde-bf2a-b46239fd1cda | -8.06535 | -43.10352 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4ba53a03-e518-39c9-be26-b81037fe0482 | -8.09137 | -43.15128 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bfe0525d-9979-3a37-ad4d-e1d589dfbae7 | -8.42164 | -48.30104 | 2025-06-22 04:40:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d75391a-e43e-3cc3-85f8-cd8a43fdcad5 | -4.334 | -46.78146 | 2025-06-22 04:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac9df53e-3d41-318a-abb7-a1ce1cb7a5bc | -4.64253 | -47.96364 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ce7850f-f8f8-3586-ab2d-5317d0f510a0 | -8.09653 | -43.14737 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 63844351-51e9-3e34-b69c-1fad10fe8ea1 | -6.74276 | -50.96101 | 2025-06-22 04:40:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abfbf2e7-cdfb-3e4d-88ed-c5ef50afcd51 | -8.0823 | -43.14993 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf287c28-a512-337a-9f8e-7ec2db874873 | -8.41483 | -48.29998 | 2025-06-22 04:40:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31c1fe07-6249-3372-9783-538cb4ce79dd | -7.87147 | -47.88791 | 2025-06-22 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21a9e154-efa6-3550-a0d7-37e4fd483741 | -8.09199 | -43.14672 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 04be569d-0e93-33d7-a89d-f860deb5d24f | -8.08144 | -43.15257 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c8846e2e-8a0b-36c9-9a03-b7aacfe120ba | -4.42403 | -48.14319 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 868463d8-4be1-3697-8c6e-1ae654503c2a | -7.98364 | -46.20503 | 2025-06-22 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aa294a8-4d25-34fc-a636-fa514183cddc | -8.09116 | -43.14936 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fbea7165-6b16-350e-9297-a2576e648117 | -5.56976 | -45.21685 | 2025-06-22 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b9475ac-15f0-380f-8979-907e6e849909 | -7.87377 | -47.82682 | 2025-06-22 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b275cac-9016-3ed1-97a5-2e665a0113f5 | -7.97552 | -46.20859 | 2025-06-22 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59d8a4fd-3c98-3ff2-95e8-57182d4b2985 | -5.04382 | -47.65484 | 2025-06-22 04:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 554a733f-d817-3e19-adc7-607cc64c3bae | -3.61186 | -47.54681 | 2025-06-22 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f066a972-6b97-36be-b673-ddc828c49bc2 | -6.869 | -47.23535 | 2025-06-22 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ac753a2-ab99-3089-8de3-334993574fd8 | -4.30395 | -48.0747 | 2025-06-22 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c05fd54b-45ae-3840-abaf-b31ec6224db0 | -4.5376 | -48.00943 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfe9bc84-3ba7-3943-9c47-416cb52c0a9a | -4.59198 | -47.8904 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63b66fb8-8a34-39c9-ba0a-6a42080cdd06 | -8.00351 | -49.71217 | 2025-06-22 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adf81600-bc06-3e46-b6c8-08c78b64a226 | -3.61298 | -47.53967 | 2025-06-22 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f79156a0-7f2d-3f73-bd9e-69c78bf0c7ea | -5.63474 | -45.7998 | 2025-06-22 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5fb70386-991e-3428-9025-e0fb7311e53c | -7.9022 | -46.2304 | 2025-06-22 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 606353e0-f629-373b-b3f7-29b682ebeac9 | -8.79659 | -47.24564 | 2025-06-22 04:40:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 277de103-ad05-34c9-83be-cc3f298c24b8 | -7.26886 | -45.36124 | 2025-06-22 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31f44030-cbb8-3bcf-bfe5-49348e865ca1 | -3.60961 | -47.53915 | 2025-06-22 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5d57bc1-7f18-3ab2-8fdf-088e1e948c62 | -6.86841 | -47.23923 | 2025-06-22 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d713db7-2943-3611-8135-6a85ed67a18e | -8.07715 | -43.15378 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README8.md)
