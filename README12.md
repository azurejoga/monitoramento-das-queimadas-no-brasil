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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0815c104-4f5b-35d9-8f5e-31862b589c1e | -8.65049 | -47.75788 | 2026-06-20 07:03:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b76d0641-47f3-3e72-9ca4-c3a7f1916b7f | -11.07098 | -52.47818 | 2026-06-20 07:03:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 272fa06a-8676-38bc-a288-4a1af8d16bb8 | -11.061 | -52.47682 | 2026-06-20 07:03:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 811f7ac6-cda3-3765-94b5-ec92fc979d95 | -13.2007 | -50.34217 | 2026-06-20 07:05:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 54884a3e-be8a-3804-bb85-dada44bc50d6 | -12.572 | -45.0376 | 2026-06-20 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 0b974cc0-b099-3fe7-9f43-c41a477e1d4f | -12.5724 | -45.0143 | 2026-06-20 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 912eeb12-fdd0-3941-82c0-d2cb2b3a9981 | -12.5531 | -45.0174 | 2026-06-20 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 256.4 |
| ae81b80d-1782-3b6a-893e-69d8e943f174 | -12.5527 | -45.0406 | 2026-06-20 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| a4dfb949-2295-3509-ab2e-047b5d633f2b | -12.5339 | -45.0204 | 2026-06-20 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| f234d0a7-82a0-35cb-82a3-7b034cf684d9 | -12.5724 | -45.0143 | 2026-06-20 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9e6a2c9a-ed38-3ffd-93d1-10f117caf843 | -12.5531 | -45.0174 | 2026-06-20 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 36346f51-4ee7-3521-9329-6329d13d7a48 | -12.572 | -45.0376 | 2026-06-20 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| ad0524cd-f187-36a4-8548-3507e7adaa17 | -12.5527 | -45.0406 | 2026-06-20 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| a3a13dc7-55a9-3c3c-8e71-a98046b99b8f | -12.5724 | -45.0143 | 2026-06-20 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f0381522-a327-3f5e-94d5-66857e2a4b11 | -12.5527 | -45.0406 | 2026-06-20 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 8e690cc1-fa55-3d36-ab9e-5d3c35ff6cff | -12.572 | -45.0376 | 2026-06-20 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 192286bc-829e-3cf7-9c34-2904f5e272e9 | -12.5531 | -45.0174 | 2026-06-20 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 276.7 |
| 03644450-6442-353f-9c33-36d314e4820d | -12.5527 | -45.0406 | 2026-06-20 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 216.6 |
| f7311c80-4c05-3545-9b1b-718bffb4a6d3 | -12.5339 | -45.0204 | 2026-06-20 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 0f7eeb19-4582-3e02-9d77-3d472c7d7736 | -12.5334 | -45.0436 | 2026-06-20 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| bb5af2a7-09cb-32e7-87de-aa76ab233b20 | -12.5724 | -45.0143 | 2026-06-20 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f1487865-2914-3688-b632-0ae4ab7e93ca | -12.572 | -45.0376 | 2026-06-20 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c03f0b77-a10f-3022-b2dc-abe62605cee7 | -12.5531 | -45.0174 | 2026-06-20 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 48b729c0-2688-3aa8-a2f6-6bc958d550a7 | -12.5724 | -45.0143 | 2026-06-20 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 29a40f30-5cdf-3f9a-8dc8-b4a4bdd7df2c | -12.5527 | -45.0406 | 2026-06-20 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 342.1 |
| 5c367c9f-9448-36f3-bf3f-dc6c2eef8793 | -12.5334 | -45.0436 | 2026-06-20 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 78530a46-f798-3b72-9248-98621c9e0fd8 | -12.5531 | -45.0174 | 2026-06-20 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 273.8 |
| e6f7f9f9-19db-3cb2-bf11-55662329a460 | -12.5339 | -45.0204 | 2026-06-20 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 4e819a48-09c3-3937-b086-9617107e4c75 | -12.572 | -45.0376 | 2026-06-20 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 545215ef-af29-38c1-b973-5c8c734d2435 | -12.572 | -45.0376 | 2026-06-20 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| b7a60227-a5d5-3ad6-bfe0-925092a07aec | -12.5527 | -45.0406 | 2026-06-20 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 287.9 |
| 0e32d7f6-35f2-3198-a24b-d2339b1d3e16 | -12.5724 | -45.0143 | 2026-06-20 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1e705723-6ead-3faa-94dd-47b8a9184a4b | -12.5531 | -45.0174 | 2026-06-20 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 217.0 |
| a2f89f0d-ca83-359c-96fd-57a393fd1449 | -12.5339 | -45.0204 | 2026-06-20 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 409f3599-8c8b-36c3-ba18-94c3aff3412a | -12.5334 | -45.0436 | 2026-06-20 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 54309b0c-b083-34d4-a23a-e42b79e6ef92 | -12.5527 | -45.0406 | 2026-06-20 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 363.6 |
| 032cf10e-01d1-38cf-86c1-1a9b9bc585b3 | -12.5531 | -45.0174 | 2026-06-20 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 213.1 |
| b932a226-c228-3079-9dd4-8b34457fb5b8 | -12.572 | -45.0376 | 2026-06-20 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c01e7af0-96b2-3cfc-adbc-1f7890ba4ea9 | -12.5724 | -45.0143 | 2026-06-20 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| b03b5518-d647-38ae-b699-a16c9b8eaed9 | -12.5527 | -45.0406 | 2026-06-20 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 354.0 |
| 6592a4e1-4efe-3439-9245-4e0cd35b2127 | -12.5339 | -45.0204 | 2026-06-20 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 0cab8d5d-395b-3039-ab32-08c213c98035 | -12.572 | -45.0376 | 2026-06-20 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 2ce9432f-8ef7-3504-82fb-185620e26048 | -12.5334 | -45.0436 | 2026-06-20 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 4edf2f6c-96d2-39a2-a531-ac4213017b22 | -12.5531 | -45.0174 | 2026-06-20 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| f62c4e21-73bf-3940-83e2-196d28ed6d55 | -12.5724 | -45.0143 | 2026-06-20 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 2a71c692-c252-343a-9244-fc8ed762a5d3 | -12.5724 | -45.0143 | 2026-06-20 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| f98895f5-b077-3e07-be77-bf62d78b43bd | -12.5527 | -45.0406 | 2026-06-20 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 283.9 |
| 54435562-6264-3196-a362-082c22a36ad0 | -12.5531 | -45.0174 | 2026-06-20 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 6343d3c5-3f46-3f15-87e0-40b4c9ca5373 | -12.572 | -45.0376 | 2026-06-20 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 2976c376-1529-3f34-9de0-fff8f58e97d6 | -12.5527 | -45.0406 | 2026-06-20 08:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 213.8 |
| db9c7b50-50a6-36b9-aa65-bbf6454f95b3 | -12.5531 | -45.0174 | 2026-06-20 08:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| a065d9b3-6031-3e96-b790-3fbee6303e23 | -12.5334 | -45.0436 | 2026-06-20 08:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| d40d41be-0948-318b-a053-0f6f476710bd | -12.5724 | -45.0143 | 2026-06-20 08:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d4df5f61-75b2-343a-a583-6cb1ea095a48 | -12.572 | -45.0376 | 2026-06-20 08:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 3916b3b2-97cd-3371-a7c6-af6d5bdb45e3 | -12.5527 | -45.0406 | 2026-06-20 09:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| ce402189-5fae-304e-80de-477aef2915a2 | -12.5527 | -45.0406 | 2026-06-20 09:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 25755cc0-f2a0-3096-94e7-98cbb7d2ff77 | -12.5527 | -45.0406 | 2026-06-20 10:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 0fc2498d-00df-3b23-a218-576137f5d912 | -12.5527 | -45.0406 | 2026-06-20 10:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 07cbc3cd-3bc9-3cdd-a01e-5feb228543f2 | -12.5527 | -45.0406 | 2026-06-20 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| dde465da-f20d-3678-aa0e-df6c2297f8b3 | -5.8187 | -45.07047 | 2026-06-20 11:10:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 82f6e313-99d0-34b6-95aa-6cd71bd5a059 | -8.49842 | -39.38579 | 2026-06-20 11:10:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 51aaf4c4-1e85-3dca-aa2a-26d9e86684e8 | -13.94711 | -42.03628 | 2026-06-20 11:13:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| c430cef1-1bd0-3f9c-a917-446de693bda3 | -13.76961 | -40.61982 | 2026-06-20 11:13:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d2ea5568-f1d3-337c-93cb-9ee6178099f3 | -13.76797 | -40.63052 | 2026-06-20 11:13:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| eafa9956-cd1b-3896-b47e-b8263540d76e | -19.43863 | -40.38517 | 2026-06-20 11:15:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 34cd83cc-19f6-3209-8924-1747fc4345e7 | 0.6059 | -55.39417 | 2026-06-20 12:46:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4b3aa066-be3a-3bab-9415-e5b46ecba1ab | -10.93584 | -56.83858 | 2026-06-20 12:49:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 50412c89-0039-35d2-9dc3-9c5f221ab9fd | -9.78607 | -56.95279 | 2026-06-20 12:49:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 2a6e1008-c8ec-3139-ac9b-0860f487a87d | -10.27885 | -60.54939 | 2026-06-20 12:49:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1fadbfe2-6cb7-3fa8-ad10-8a7175b8081e | -10.93395 | -56.84469 | 2026-06-20 12:49:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 7bc19dee-bfd0-37d1-a343-1ce1c8d494ae | -9.0246 | -63.54395 | 2026-06-20 12:49:00 | TERRA_M-T | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 907efcc9-130c-3986-9ccb-f793cadd38d1 | -10.57644 | -57.31322 | 2026-06-20 12:49:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fe45ec69-13b3-3eca-bdcd-488814d3f0b8 | -12.42472 | -54.18149 | 2026-06-20 12:49:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2d2843a5-7ed4-3acc-b935-baac8f935245 | -10.57463 | -57.32715 | 2026-06-20 12:49:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 89dfae27-2056-316c-baf7-bf303e0caa2b | -10.28013 | -60.54013 | 2026-06-20 12:49:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5addaaf1-2a14-3eb0-b4be-a7e4ffeadb5f | -10.93387 | -56.85383 | 2026-06-20 12:49:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 05ca0316-e741-3608-8e2c-0edccfdd9102 | -16.26806 | -60.01493 | 2026-06-20 12:51:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3e54d7ac-94fe-37cf-a8fd-66ee67f54fd7 | -11.2711 | -49.6808 | 2026-06-20 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 2ff55033-bebc-35d6-bf36-4b14be8cf4fb | -6.4973 | -42.2142 | 2026-06-20 13:50:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| cd586a89-49b9-3438-8857-b1e7e346d9eb | -6.4973 | -42.2142 | 2026-06-20 14:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| db9f0adb-470e-3b62-9d30-84e1548300d5 | -6.4973 | -42.2142 | 2026-06-20 14:10:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 985b89f4-a272-3fbd-a71c-af9a7bcaf867 | -6.4973 | -42.2142 | 2026-06-20 14:30:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 287deb59-860c-3d30-9f57-dfae9d23e957 | -6.4973 | -42.2142 | 2026-06-20 14:40:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 48f73928-9130-3ad3-b833-bd62851c0aca | -6.4973 | -42.2142 | 2026-06-20 15:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |


