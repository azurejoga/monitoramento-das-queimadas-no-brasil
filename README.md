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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83bb25d9-e06a-30bc-bc66-cc721b346808 | -20.9845 | -47.3955 | 2025-06-18 00:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 1fc8f4e2-076d-302f-8004-9f519ee15182 | -11.1382 | -53.9223 | 2025-06-18 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 236.0 |
| 605a92f6-2dfa-312f-ad6b-2d24e82bb36f | -10.669 | -49.3597 | 2025-06-18 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 0bf1f179-d544-3644-ac3c-3d774f77f0ab | -11.952 | -58.7376 | 2025-06-18 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d74897df-64dd-37cb-b618-3616e37c549c | -9.4993 | -56.0988 | 2025-06-18 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| fba9c039-692e-38f7-876f-3aee4b4aea8f | -14.4467 | -48.9063 | 2025-06-18 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 141.2 |
| f22b9594-8c28-3236-a0cf-8999e5447a17 | -11.1379 | -53.9429 | 2025-06-18 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 397.0 |
| be68e1c2-19e2-377c-81ef-813145458fba | -11.1571 | -53.9206 | 2025-06-18 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c4da1a12-80e8-3691-bd20-5e2ecf88d1e3 | -8.7129 | -49.0168 | 2025-06-18 00:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a9b1eb09-10bb-3693-8158-148b6aca1349 | -11.119 | -53.9446 | 2025-06-18 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 68753df3-df3f-323c-bb74-2dfcbc0b6b27 | -21.0058 | -47.3668 | 2025-06-18 00:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 62d5a7ee-d3cf-3efa-8e6e-b6e93274a964 | -11.1568 | -53.9411 | 2025-06-18 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 52d687ec-cd86-3fa3-9968-8241703fb15e | -9.4994 | -56.0788 | 2025-06-18 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1050ca3e-fd74-381a-9ce0-52f7073a44c8 | -14.4273 | -48.9093 | 2025-06-18 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a0486858-d9a6-34ac-a5c2-284cc1e52f1a | -21.0051 | -47.3904 | 2025-06-18 00:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 18de797c-2e0a-31e6-afbe-16593b4c7c70 | -8.7317 | -49.0151 | 2025-06-18 00:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| eb0d2016-4947-3c8f-8976-6b584c6fe9ac | -6.118 | -42.5323 | 2025-06-18 00:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 6094bfc2-e7ef-3138-8377-62bbd9383b6d | -9.4807 | -56.0801 | 2025-06-18 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| c9c3b68a-bdd2-3646-8580-d9a71d6e82ec | -11.1193 | -53.9241 | 2025-06-18 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2a711ac6-9a62-3f1c-91e5-6c28d3c6cd20 | -9.4806 | -56.1001 | 2025-06-18 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 45f3e9e6-2dec-39d4-8f2f-a6bc857e7459 | -20.9852 | -47.3718 | 2025-06-18 00:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 40.0 |
| bce739a7-3255-3bc1-9cdd-35697672559f | -6.118 | -42.5323 | 2025-06-18 00:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 63df9638-93e0-31eb-8d71-933d61c49642 | -11.119 | -53.9446 | 2025-06-18 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 0535777f-1d56-3ce5-860a-f73eefb87a3e | -21.0051 | -47.3904 | 2025-06-18 00:10:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 72.1 |
| fd68bafb-cd44-30dd-af7c-6430902c2749 | -11.1193 | -53.9241 | 2025-06-18 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 6c1c0165-81a4-36fe-813b-8c96a5de6070 | -10.9167 | -56.8336 | 2025-06-18 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 9a507c3e-1211-3acb-97a3-6bed4e51299d | -11.9709 | -58.7362 | 2025-06-18 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 7e977304-992a-37a0-a77e-184446b2bede | -11.1382 | -53.9223 | 2025-06-18 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 252.7 |
| 4983eb73-bdc6-38ea-ae08-70dff7b1d1b8 | -14.4273 | -48.9093 | 2025-06-18 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ae65c6fa-6257-314d-ad84-ce05272a35e0 | -20.9845 | -47.3955 | 2025-06-18 00:10:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 108.5 |
| e11cb675-04e9-38cb-9aae-4a35b9d54fe0 | -14.2052 | -45.507 | 2025-06-18 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 59c239e1-988d-3593-84df-b8925451ebf5 | -11.1571 | -53.9206 | 2025-06-18 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 77e0d714-3961-3b1e-9721-35c0490a4478 | -11.1379 | -53.9429 | 2025-06-18 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 335.4 |
| 26d16791-87c6-308b-9fc9-4d09999ee4dd | -10.9164 | -56.8536 | 2025-06-18 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 07f229ec-6d8f-32a7-989b-ff871d64c261 | -5.9028 | -43.4418 | 2025-06-18 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 59111977-4277-31d9-a865-6762055490be | -14.4467 | -48.9063 | 2025-06-18 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 9c695a32-3746-3532-b08e-a7ce4f8d074e | -8.7129 | -49.0168 | 2025-06-18 00:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9f2c23a9-952b-3438-b046-f34a6cb54e46 | -20.9852 | -47.3718 | 2025-06-18 00:10:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f1e786c5-02e9-3b5d-bee9-7600da13885a | -8.7314 | -49.0367 | 2025-06-18 00:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 22bb8014-b30f-3560-8c5b-8bd0c5fb6d14 | -11.952 | -58.7376 | 2025-06-18 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| bbd83f48-ea20-3904-80d0-bbbc9a9d8252 | -11.1568 | -53.9411 | 2025-06-18 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 076a33dd-5457-34cc-8ac4-51ebb622fb40 | -8.7317 | -49.0151 | 2025-06-18 00:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 572506a5-c1cd-3099-a57e-c2602255e892 | -12.3465 | -49.285801 | 2025-06-18 00:17:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3031f4f-9190-3dfe-bd25-ac17f870af66 | -8.7196 | -49.008701 | 2025-06-18 00:17:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| faeeb450-2b45-328f-a0ff-6832380c7adb | -5.0762 | -43.729 | 2025-06-18 00:17:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a85c584-db91-3d6e-b708-d4f2c89d8f03 | -11.7848 | -48.318802 | 2025-06-18 00:17:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b42dc7a-e8c5-34be-8564-ab87f3eb94fe | -4.5501 | -48.003502 | 2025-06-18 00:17:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd3c0b1a-0031-35d7-bf7b-4eec4e397a6d | -6.1199 | -42.526001 | 2025-06-18 00:17:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f61e5474-a841-380d-be1b-ada7a52a4c51 | -8.7294 | -49.006699 | 2025-06-18 00:17:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0af95850-f1b8-3d3d-a836-a58733104b54 | -6.2407 | -43.366699 | 2025-06-18 00:17:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86a8f1d5-36b0-3c30-a6b3-bc4c8e6e7457 | -5.0746 | -43.722198 | 2025-06-18 00:17:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84e84438-04ff-3ff9-a207-b6789bc3a5aa | -22.778799 | -49.310398 | 2025-06-18 00:17:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| be910459-99df-38ef-91ae-f3b0dd3acedf | -7.2597 | -44.633499 | 2025-06-18 00:17:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a6f6285-353f-3834-8e6b-f672d8ea2e03 | -20.982 | -47.377701 | 2025-06-18 00:17:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 75cb3e22-178c-381d-bd69-bae2a1e8a885 | -9.2591 | -50.024502 | 2025-06-18 00:17:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0937f8f0-6764-3128-8d86-4e155426c206 | -11.335 | -45.2164 | 2025-06-18 00:17:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a118795-4d87-3560-9ed8-5285df69c740 | -4.3782 | -48.060902 | 2025-06-18 00:17:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15aa4dfc-ab9d-3605-86d6-26d0f58429b5 | -10.9904 | -45.094299 | 2025-06-18 00:17:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 16b2df8a-464f-3c6f-ba43-250af2c1ab54 | -6.6846 | -43.685501 | 2025-06-18 00:17:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a49de81-722a-34a7-8d92-9cc94b243d06 | -6.1221 | -45.9361 | 2025-06-18 00:17:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b7567bc-c7a8-3aa4-b970-dc7bd74447cb | -7.5466 | -45.639702 | 2025-06-18 00:17:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b13e296e-35cf-36e0-9647-b54968ab99fe | -14.4381 | -48.898899 | 2025-06-18 00:17:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a872fa4e-401a-3de7-93ac-a079f27eea3b | -6.3806 | -43.7537 | 2025-06-18 00:17:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d9d2352-03bb-3c4f-b6c6-2606072e1b34 | -6.6808 | -43.217201 | 2025-06-18 00:17:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| a3e20458-22dd-3c96-907e-37aeabe33891 | -6.6729 | -43.182899 | 2025-06-18 00:17:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 5543248f-3f4b-357c-8a6a-00ff268551fa | -18.136101 | -43.962101 | 2025-06-18 00:17:00 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f831a3d3-15bf-3877-98c2-8172da5078b3 | -14.2039 | -45.512798 | 2025-06-18 00:17:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7107d144-3583-3d3a-ad41-cec0db66649d | -10.726 | -49.551998 | 2025-06-18 00:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13717374-1708-3eb5-81d4-7562b76ce818 | -6.1215 | -42.533001 | 2025-06-18 00:17:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ad7cc502-6247-31a3-bdfa-0d6c08d7d915 | -11.139 | -53.9333 | 2025-06-18 00:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a47df74-f49f-3a26-b890-6134db47a2c7 | -6.6615 | -43.178299 | 2025-06-18 00:17:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| d3390a12-4ee8-338d-bc67-a00cabd05091 | -8.7169 | -48.996101 | 2025-06-18 00:17:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1f48263-e43d-3ac2-b63c-3cfe4cee25e5 | -6.0371 | -44.055302 | 2025-06-18 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a076a12-1894-3dca-9296-7d3fb2729c40 | -4.8186 | -47.3218 | 2025-06-18 00:17:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 666f2c5b-c6a1-33d3-b9a4-378c033210b9 | -8.7223 | -49.0215 | 2025-06-18 00:17:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61b669eb-6504-3f21-99e8-4cb8c51a1c29 | -11.1333 | -53.903099 | 2025-06-18 00:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02ecd673-e1f4-3cc2-9d4c-ecabf8fbc457 | -5.6162 | -45.973801 | 2025-06-18 00:17:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3888e6fd-9f09-3564-9f6a-9b0aef84e41b | -10.723 | -49.537201 | 2025-06-18 00:17:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c559271a-1d04-3edc-972a-f3a4a6458079 | -14.4314 | -48.916199 | 2025-06-18 00:17:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 12bca5e0-f7a9-3955-90c5-aac75dda2654 | -7.5484 | -45.647598 | 2025-06-18 00:17:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63430891-7ec9-3d3c-b459-2ddae4f1aa91 | -6.1398 | -42.9715 | 2025-06-18 00:17:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 22dcbbea-fb86-3c4f-8564-0187ef66eb94 | -21.670601 | -41.941101 | 2025-06-18 00:17:00 | METOP-C | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0bbdfbde-fddb-34fd-8fc7-8d6b6d138263 | -22.775299 | -49.288502 | 2025-06-18 00:17:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1f817acf-d4f3-3460-86cf-cece70aa1dd7 | -5.9105 | -43.455399 | 2025-06-18 00:17:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 918e7bf6-fc00-31da-bd69-84c103b7e7a0 | -6.6631 | -43.185101 | 2025-06-18 00:17:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 5a2bac03-8444-3ec6-ab91-11250fd9ec3f | -11.1294 | -53.935101 | 2025-06-18 00:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6598e1e9-9b34-36ed-894a-6d5748ed2971 | -3.0312 | -49.4203 | 2025-06-18 00:17:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d34d8367-4f16-3313-9093-247906a20354 | -5.9188 | -43.446301 | 2025-06-18 00:17:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c5bcadc-7c3a-369f-9efd-dd590c8fec4f | -6.3693 | -43.749001 | 2025-06-18 00:17:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e10aa733-94fb-3c7e-aa19-b80e58316562 | -20.994499 | -47.391201 | 2025-06-18 00:17:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1961ab09-4782-3b76-8811-1ebe2e8c7ff5 | -11.7822 | -48.306099 | 2025-06-18 00:17:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d461167-80cb-3708-81c6-086943730918 | -10.9806 | -45.096401 | 2025-06-18 00:17:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 08d87b2a-19d9-3624-9186-0941cd798d9d | -7.5386 | -45.6497 | 2025-06-18 00:17:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ac7e9e4-fae5-3ae1-a132-efff79c111ce | -4.835 | -43.172001 | 2025-06-18 00:17:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cea9d60a-0d6b-3292-aa30-ae11540f88dd | -4.3803 | -48.070499 | 2025-06-18 00:17:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cfe84ed-c42b-3be8-ab40-cf253d46d748 | -10.6518 | -49.339199 | 2025-06-18 00:17:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c9ca1d2-6191-3e9c-b7bb-ad2d1a000206 | -5.9074 | -43.4417 | 2025-06-18 00:17:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68bef2c6-dbda-31cb-a88e-10ac0e339e4e | -11.1236 | -53.904999 | 2025-06-18 00:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76f15de6-85a4-3c27-ba0f-cdddd993eabc | -6.0469 | -44.053101 | 2025-06-18 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ebe6541-307b-3232-a8fa-1dbf16bb31b8 | -20.9918 | -47.375801 | 2025-06-18 00:17:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
