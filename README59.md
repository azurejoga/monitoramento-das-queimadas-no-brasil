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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1057ebc6-0a86-3ea2-aa3d-cc9c46240980 | -21.56164 | -48.0061 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfdd707b-eb6e-3d78-b836-71f09e6330a5 | -21.56106 | -48.0098 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9657ee1-4899-3ff0-86a8-b4f6ac59cbdf | -21.56049 | -48.01349 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57ede1e5-9350-3e08-a847-3ac45aa5a7c4 | -21.55991 | -48.01719 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 351ab927-4092-3488-970a-9cf1fbb1216d | -21.55934 | -48.02089 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c5d73445-7a76-34fa-a609-96e5463199da | -21.55877 | -48.02459 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ab234951-7065-318c-a3be-66a728f2c34d | -20.02019 | -44.59668 | 2024-10-14 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88f86a96-5fe6-30e7-870c-a408ceef3b41 | -15.56871 | -47.85434 | 2024-10-14 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bac6fe5-03ca-30b5-8c98-c4d2090ffde7 | -16.99821 | -48.07035 | 2024-10-14 04:23:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca9a8281-e5d8-3964-aea1-4b128b888dc8 | -16.92439 | -48.50316 | 2024-10-14 04:23:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e27f83d-028f-3e18-ac6b-d3c843c14269 | -19.22923 | -44.38404 | 2024-10-14 04:23:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1042562e-8a0e-3a84-8860-2c528c7d7b80 | -19.22816 | -44.3816 | 2024-10-14 04:23:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab822b54-0d6c-3a4f-8cc3-3eb7422020b4 | -19.22757 | -44.3858 | 2024-10-14 04:23:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d7a66f8-7219-350e-98ea-7fd59efbd4cd | -19.22563 | -44.38344 | 2024-10-14 04:23:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45c2f43d-9b03-32bb-a915-765d269d7739 | -19.06831 | -47.39959 | 2024-10-14 04:23:00 | NOAA-21 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba2b632a-c9bd-3f2e-9261-57aaeb3bb755 | -19.22462 | -48.95463 | 2024-10-14 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55f7f983-4edd-3799-b2c7-56d5e3ac5055 | -17.96071 | -57.31541 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 83be00ef-1026-3917-887d-c00208b6a5b4 | -17.96036 | -57.30784 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.9 |
| 60b85315-a07b-3a3b-8282-34587c5107cd | -17.96455 | -57.32386 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 22ab1393-9a29-3763-81d0-4d140bfcf48b | -17.96378 | -57.32747 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 01b78ee4-3bca-3a02-93ed-7368e4f627a5 | -17.96301 | -57.33109 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 60b975e6-6cf1-3441-b5d9-7eba7a705f63 | -17.96223 | -57.33471 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 8fb32f8e-7832-3a8e-9524-16a567f7c237 | -17.96186 | -57.30059 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| f2b0cc9d-2520-3d7a-ba7a-e20038bfdfa9 | -16.04367 | -43.95945 | 2024-10-14 04:23:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5466b130-681b-3ab2-bdb0-3a04c855d1ad | -16.63227 | -43.4836 | 2024-10-14 04:23:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5944698d-e604-34d1-9212-0b3f6011c84c | -18.32423 | -44.33434 | 2024-10-14 04:23:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10d69c71-851e-346d-9af1-42cd38e39375 | -19.98185 | -44.68839 | 2024-10-14 04:23:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 925cdc9d-912d-3ea0-8483-2283ce0ca3b4 | -18.75481 | -45.60026 | 2024-10-14 04:23:00 | NOAA-21 | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e7ee6dd-6308-3a2f-8ead-7b1469f960d3 | -18.73583 | -45.02578 | 2024-10-14 04:23:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 329f23c8-d16f-36c9-995b-ec52130b1f9b | -20.33859 | -46.62052 | 2024-10-14 04:23:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ae7a4a5-3ce2-3a61-b4ea-1bfd9fcaed3a | -20.33803 | -46.62427 | 2024-10-14 04:23:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e77b00b3-dae4-328c-8bf9-43c24db94058 | -20.33523 | -46.61998 | 2024-10-14 04:23:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbb61c9c-cdd4-31c4-b90b-df0ebe799e5e | -20.31097 | -45.58359 | 2024-10-14 04:23:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe355742-1d01-33fe-ad8a-3c5951f119ad | -20.95335 | -46.00453 | 2024-10-14 04:23:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4591fc5a-519f-3c75-9a49-4df5dc90bbea | -20.95011 | -46.00512 | 2024-10-14 04:23:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11ae100e-2d3f-3e54-b91c-0a27edf6fb1b | -20.94992 | -46.0039 | 2024-10-14 04:23:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b0a6c10-445d-3795-a7e0-cada6403193c | -21.1163 | -46.42833 | 2024-10-14 04:23:00 | NOAA-21 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0653d65b-6b41-3f9a-9627-0463e6a7c636 | -20.92902 | -46.48496 | 2024-10-14 04:23:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e54a33e2-3579-383e-a475-5549fa239296 | -15.81561 | -46.02876 | 2024-10-14 04:23:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e89befb6-7f0d-3d53-82ed-2c1698d07a8f | -20.32214 | -47.13847 | 2024-10-14 04:23:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5a2bd53c-d397-3ae2-b063-bf771c293786 | -20.32158 | -47.14211 | 2024-10-14 04:23:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e759386e-168c-3429-a078-d1fe153758a3 | -20.31882 | -47.13791 | 2024-10-14 04:23:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e573920d-5564-3566-bcb0-372614020ff8 | -20.31826 | -47.14157 | 2024-10-14 04:23:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8113ef2d-56f9-3463-8845-5f0c9b11fbc6 | -20.76448 | -46.77025 | 2024-10-14 04:23:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e0f545b2-dad1-366a-904f-1db16d315e65 | -21.55603 | -48.0203 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f6149c2-f19e-38ab-9fd6-9112fadc0323 | -21.55546 | -48.02399 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be9ae582-194e-3724-b7cd-622ba288a6df | -21.54827 | -48.02652 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1fd21798-18bc-37f8-aca6-6b33d1361490 | -21.54223 | -48.02164 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09a41efc-1937-38a5-831b-5debbbe7f7fe | -16.90175 | -48.22638 | 2024-10-14 04:23:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0a963c6-a602-3912-8ab3-f0a37c360f2f | -21.05079 | -48.61362 | 2024-10-14 04:23:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 015168dd-b430-3cc1-a87f-1f77fb350a8c | -21.0502 | -48.6173 | 2024-10-14 04:23:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 83a69507-8efe-3587-ad94-0b8b366f39bf | -21.04689 | -48.61671 | 2024-10-14 04:23:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3c571355-7742-33bb-bf97-1c53f5c2dcbc | -18.59179 | -50.2273 | 2024-10-14 04:23:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e4dc72b9-bc9f-30b6-807b-19d58eaf7f8e | -18.25691 | -56.50661 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7ff9f3e2-caff-3617-a64c-3a4f910d9335 | -15.32 | -48.78455 | 2024-10-14 04:23:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e03687f0-c0a7-3e66-a3e7-c4367c1eff0c | -15.31936 | -48.78837 | 2024-10-14 04:23:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68dd34f5-8ab3-33fb-b431-44c4bff938c0 | -15.30746 | -48.75444 | 2024-10-14 04:23:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5b506cf-b4c0-3e43-8910-85a8606f937d | -15.29737 | -48.77262 | 2024-10-14 04:23:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8160e4af-229f-391e-8b34-a82c71201684 | -18.5925 | -50.2232 | 2024-10-14 04:23:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 07106e6b-9ebe-3d6f-9811-42a5afa99eb8 | -21.08714 | -50.48063 | 2024-10-14 04:23:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f7ced44c-07da-30a7-ba70-3abc08d4d89a | -18.25625 | -56.50977 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 2632ceeb-4ef3-3ede-815d-c34c704e0b63 | -18.90304 | -51.84846 | 2024-10-14 04:23:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6334cda0-1d31-3c60-b4f7-20ea9e8ecc8b | -18.35389 | -51.01134 | 2024-10-14 04:23:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 492160d3-698d-3158-bbf0-11cc20a5a9ac | -16.75165 | -52.84311 | 2024-10-14 04:23:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52150fe9-7e75-3426-ac79-68f7d133f0a5 | -18.02699 | -53.67906 | 2024-10-14 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 171a577e-add7-316d-a0d8-d8762181f7db | -18.02398 | -53.67994 | 2024-10-14 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 59add3c1-d173-31eb-852c-2df08c6e7a8b | -18.02272 | -53.67822 | 2024-10-14 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| deba240c-8d71-3eee-a0b9-57b7cd8ef4c6 | -18.25559 | -56.51294 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| cca3f865-2ffe-3c12-87cd-4d431737423a | -18.25804 | -56.52676 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| d83088e5-c033-31d2-8cf4-41013b170f86 | -17.69368 | -56.24416 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 554189e4-ffc0-3b00-8652-e1b8e9debf28 | -17.68407 | -56.31739 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fc9cbe06-a470-36ad-bb9b-67a7ff21382a | -17.65108 | -56.29699 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 611a1b0f-2b47-3a9f-a5f2-a30c5f890c26 | -17.63714 | -56.28739 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3071f100-b602-309f-b2b9-968bd62e9810 | -17.08114 | -56.01351 | 2024-10-14 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3823ef33-e967-378a-a6e8-7dee143f57e0 | -17.07735 | -56.00622 | 2024-10-14 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5eed8cdb-6d87-3a90-ad06-4c7d1591fc9d | -17.0761 | -56.01241 | 2024-10-14 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 23676a5b-714c-3a51-9f78-25e15faa3291 | -17.02185 | -56.02002 | 2024-10-14 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3d3bdd3c-98c4-34bb-8cce-20a3d8c47baa | -16.90095 | -55.87814 | 2024-10-14 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| edd7c959-a9e2-3341-9343-1ceba6d9f5ee | -17.68471 | -56.31425 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7c19d4d1-1cbb-3f10-a241-84d48f63d01b | -17.67914 | -56.23775 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 34df12d0-4426-3940-8677-82b11fa4bcb4 | -17.65487 | -56.30439 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6e9bcc71-8c3d-3f39-bcc8-98d15d0d3c18 | -17.65422 | -56.30754 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8f3ef110-36d1-3a92-a52c-49b7b7e8db4c | -17.65043 | -56.30014 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 84c03045-aec8-315f-bb05-9af1745fdf13 | -17.64979 | -56.30329 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 54be598c-aed0-3bee-95df-97a7151d9c00 | -17.64849 | -56.30957 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 348e9297-a9fd-33c3-baf8-b89193d4c9b9 | -17.64666 | -56.29272 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 954b6883-c5fb-33c9-b552-5d6a348c4358 | -17.64223 | -56.28848 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 280f68bf-d3f2-3d6b-87dd-d5a770e77d91 | -17.64093 | -56.29477 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 447f4878-1f56-35ed-a569-f3e4bc778c97 | -18.26313 | -56.52791 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 097c977b-8726-3b1f-8e52-9cbcc30e34f3 | -18.26134 | -56.51092 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| db3204ec-d0db-33b3-a102-241135f50afd | -18.26068 | -56.51409 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| 8bca83d5-f2c9-3e70-b6f4-46cef98133de | -18.26002 | -56.51726 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| f27ec4c3-e336-3200-99c4-02fd1acbfdf0 | -18.25936 | -56.52043 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| dfdb9da4-3b4f-3638-81b9-b138c287b4c0 | -18.2587 | -56.5236 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 3ad6de65-eceb-3087-bcca-f946bc887218 | -18.25823 | -56.50028 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| eec46993-e164-391b-85a3-069ae9f5d29b | -18.25757 | -56.50344 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 6cac33b6-e13c-3a7a-aba0-fc6899eecbce | -18.25738 | -56.52994 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| c51d04ff-8b58-3337-9b6e-3a54107bda96 | -18.25493 | -56.51611 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| a48a7686-54ac-34a2-a438-263ff351c30f | -18.25427 | -56.51928 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 696cd95f-7f90-3177-a885-b8a35ac2e52c | -18.25361 | -56.52246 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |


[Clique aqui para ver as próximas entradas](README60.md)
