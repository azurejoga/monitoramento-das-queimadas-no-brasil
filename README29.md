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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b477951-e336-3000-a509-238f94d5aba2 | -17.25016 | -57.46594 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 5596c54f-e985-36be-bb3f-e0aeb70615b3 | -17.65174 | -57.4627 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 1cf7df82-02b2-3729-a47d-5cc44837a131 | -17.65814 | -57.46783 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6dff453b-8bc8-3759-9611-fb89aa2fbfe3 | -17.59142 | -57.56008 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| bd4f4599-e000-3ff8-a65b-d6c56714cadc | -17.57956 | -57.43608 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4eab2c14-fae5-37de-aab7-8038cfe9332c | -17.24726 | -57.4614 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| c6d32dc4-8f00-326e-a59d-c927b8d24210 | -17.64417 | -57.53971 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8305d88a-9dcf-31ae-a8fb-5360f7976904 | -16.951 | -57.643 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e7f42227-908d-39a4-9009-440fa1ac35e9 | -17.25883 | -57.47956 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 47bffc27-fb25-3e8b-b849-5171a9c2404b | -15.45312 | -59.77241 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 576a4a5c-971e-360e-89d9-acb8afcf21d3 | -15.85396 | -59.29655 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ca45f01-db70-3628-801f-7262b11bf831 | -17.59998 | -57.47522 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1ca1849b-01a3-3a4f-8efb-3d240178b0bf | -17.58776 | -57.40429 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9ebf8c05-0652-3b61-983d-08bb837668c4 | -17.80176 | -57.32302 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9a3a70cf-f640-3c8d-abb2-f2c8d05168cc | -16.9579 | -57.64409 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 696d61d0-bda3-3aed-bdf6-d5fb1aa4ff8f | -17.58213 | -57.55044 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 09a2bdab-86bf-3107-b07f-6aa2c22b2d80 | -17.58623 | -57.57153 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| d08fa456-13f6-3c13-b60b-0c687d81bf59 | -17.59171 | -57.47509 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 64f80a51-6673-3101-a349-0a0a67f51e36 | -17.7027 | -57.56454 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 997cb6eb-9457-3eb0-aee5-3076cb117490 | -17.64358 | -57.4449 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e957e5c3-38fb-3652-aeb0-bce7b59eb5a9 | -17.72007 | -57.54264 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 67201319-682c-33dc-9aaf-14267be67545 | -17.83921 | -57.3903 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5bf24129-f2ba-3013-9326-c2cf831974e6 | -17.57818 | -57.56728 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 76c06e00-5e29-3d46-b6d6-6c7e04f13c84 | -17.70675 | -57.56108 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 57e86d40-45d7-3b58-aa33-85b86ba4213b | -17.577 | -57.57526 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 3f7ee4e7-9140-30b7-8c35-d1692ab7fc00 | -17.70208 | -57.54392 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0e801050-73fa-3ee2-9ee3-b3e9ea9ec2f0 | -17.26231 | -57.48009 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a7b250c0-8fe3-3bc4-9811-f48df4ea9474 | -17.57072 | -57.5211 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 61586fe8-4235-3fe5-87bf-0b7f25d26810 | -17.58447 | -57.55899 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| f9e4a482-3050-3a70-ac90-4a71088e38b7 | -16.95271 | -57.63125 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a6e5e976-6035-31b7-b491-3573e5a428a1 | -15.90669 | -59.11058 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28ba06c7-ec69-3d69-a74f-c01069ac6416 | -17.70147 | -57.52326 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a7c40e4d-9074-3fee-9209-955b8938f424 | -17.24437 | -57.45685 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 66600cc4-ad94-3919-bd4b-3e9c529779b8 | -17.79884 | -57.31837 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 53d6b866-3f62-3fcb-b378-688003b60c94 | -17.61865 | -57.54388 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4b876586-a3ac-343b-a07c-387cbea533c1 | -17.60289 | -57.47979 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a6ad21de-e188-3c07-abad-5bd0bff78f52 | -17.5949 | -57.56062 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 46a5e3ab-5c1f-32d8-a1a9-2d6e504dc4a9 | -17.55735 | -57.53948 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.3 |
| 94870d9f-c69e-327b-81d8-3bcb59045e1d | -16.94926 | -57.6307 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0185432d-14bf-305e-91c8-c81894e55951 | -17.59638 | -57.46759 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2383fab0-ba01-38da-83b7-7bfc9da54f0c | -17.58128 | -57.44874 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e39e7623-dad6-3d84-825f-c46ae867b3b4 | -17.72235 | -57.50185 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7d3ff5bf-6161-3c9e-8979-887393f092ce | -17.26696 | -57.47266 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1b080336-adbc-30dd-8125-80304d9389d7 | -15.91419 | -59.28104 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20cbccd6-47de-389a-8399-97193a021652 | -17.58881 | -57.47052 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 536375bd-cb0d-3399-8d9f-ca21d16db67c | -17.66158 | -57.54243 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5c585a03-e977-3919-a33b-e10e37e33ec9 | -16.10189 | -60.09429 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fd816718-27bc-3d4a-b9e3-8b869983bc2c | -17.59314 | -57.54807 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b62d256b-7478-35d4-96e2-dfbb2b28b3d1 | -17.2403 | -57.4603 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 8d0b0741-6fc9-3385-8686-438066be4c6c | -17.57838 | -57.44416 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 908961ee-bdf4-39e2-8a2f-041d4ced1a91 | -17.62793 | -57.55354 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9b646b24-aa7d-3d5a-99ba-adde33b0bc30 | -17.62213 | -57.54443 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b023ef1d-cc68-395d-9d8f-a135aefe4213 | -17.5724 | -57.5582 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 829cfa44-2677-332e-a00e-fef2d14e8651 | -17.56665 | -57.52456 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 31ae3a4e-58f3-32ea-9cd6-3210ca6fbde7 | -15.40988 | -58.61341 | 2024-11-15 05:12:00 | NOAA-20 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e8ef538-35e8-37d4-bc95-5fdae4332c89 | -15.85065 | -59.29599 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 258e97e4-1817-3dbf-b2d6-ff9515c60037 | -16.94411 | -57.64191 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c956e3ae-ff85-3aa0-aafa-42c3c4fd3d6a | -17.2345 | -57.47574 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a5318d7f-4340-3707-88bc-ebba39affafc | -17.58459 | -57.54785 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3c526bf7-9133-39c3-ad53-5d49272c9db7 | -16.94813 | -57.63854 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| f939ca2d-b79a-314f-802a-2c16fad28efe | -17.04506 | -57.4356 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8114f4f0-916b-3a3a-994f-73305918aab8 | -17.59763 | -57.4666 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f31d7d0f-2c03-32f6-8bdb-798d760dd5c3 | -17.81108 | -57.35797 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 47d314ce-cd5a-3e10-a854-661ab4e99090 | -15.15858 | -59.72269 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb456c75-b904-390f-bc66-7f2a8a85afbb | -16.95043 | -57.64691 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e4543434-a026-3656-bd65-d54c0f800ff3 | -15.40654 | -58.61289 | 2024-11-15 05:12:00 | NOAA-20 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9990b3d6-5009-3565-ba4f-d59def8ba8b2 | -15.53293 | -59.50385 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 522ed5b1-affc-3867-85ac-f4ef05bf5fde | -17.63663 | -57.54261 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| a0b9d4ad-5ab9-3ed6-8683-4a361769bb4f | -17.72351 | -57.49377 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 42b106b8-4466-3c35-9d9b-c26ee1e5504c | -17.56723 | -57.52055 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3d108f77-3f7c-34cf-bbf0-ad8acb9a0d0b | -17.58187 | -57.44471 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 85aa353f-0a5b-390d-b5b1-8d484c062cf9 | -17.84272 | -57.39085 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 08f1f9f5-b692-3ee3-8e35-6cc4bb7b2e94 | -17.59343 | -57.4877 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 11d9e8ca-4f67-321f-9dc5-76545af6bd0d | -17.28609 | -57.47493 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a8e58a26-b7f3-3070-a727-4007f2b592d3 | -17.57763 | -57.54675 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 2333dd26-536f-384b-88c6-708d3a3e8243 | -17.25766 | -57.48753 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3ba29520-ceb1-379a-b427-f9fab363412f | -17.55794 | -57.53548 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| f5bc68dc-5324-3b4d-9c80-dca5c1f2e661 | -17.25536 | -57.47901 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b24f21a8-185f-37bf-90d7-a3e8f1ecc4ab | -17.22455 | -57.19754 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ad970693-e3b8-3f44-8d5d-1300ccb97a99 | -15.24859 | -60.09433 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e99a766-05e7-323b-95b0-14cf81baa569 | -17.56954 | -57.52911 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 2c6919a3-4ccc-3b5f-8c9e-dfc6341f5391 | -15.29397 | -56.52232 | 2024-11-15 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39e9bea0-022f-3323-babe-8a8e3b64ea4f | -17.71544 | -57.55013 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d95da71d-14ee-32dd-aeb3-c7d5f6e32cbf | -17.25247 | -57.47447 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 9f334ad9-2214-3526-a105-28df8980cf4b | -16.94123 | -57.63746 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 5632c7d3-d2eb-332f-b8be-c3488c0fefb1 | -15.31527 | -56.52568 | 2024-11-15 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 460e4272-833a-3841-9400-03cbafc386b9 | -17.58042 | -57.56244 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 89f5fd35-2320-34ab-96a3-79334eaef43c | -17.57244 | -57.53366 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 03abc30b-c24c-37df-b8a8-46cad6be860f | -16.10132 | -60.09789 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ab58f764-e4ea-3e3a-8db0-064eb4796d13 | -17.57587 | -57.55874 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 04bb6bef-7b17-3b0f-a644-3a2174a02d34 | -17.643 | -57.44895 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5bcd837c-bfa0-3e3e-a0d7-867188f8b55a | -17.24495 | -57.45285 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 420e1e52-df00-3b7f-a4ea-9779971f779b | -17.64069 | -57.53916 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d284888c-5f94-3e37-b6be-4d611668ef22 | -17.57871 | -57.57444 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 7a78d36e-0f54-36c0-a66a-0f2dd171ea69 | -15.86169 | -59.2905 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4a73319-3c02-33ab-b4d6-ed7269b08db4 | -16.02151 | -59.39782 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc6e122a-8105-3717-9c97-c4f2c0b48d03 | -18.03261 | -57.34829 | 2024-11-15 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e23d8a49-2e03-3764-94da-e61a8f10ce05 | -17.28261 | -57.47439 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 42c8f3fc-b91b-3ba6-9540-d68f58686e10 | -17.69979 | -57.55998 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 7ba2e310-7dca-3052-aa6e-fbf91f5b2897 | -15.85009 | -59.29956 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README30.md)
