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
| 1b5c9ead-622a-3169-94b3-d10c7b8b3ad6 | 2.3789 | -60.9082 | 2026-04-11 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 648f3e4b-d22a-37ea-92da-7d47d4332125 | 2.3789 | -60.8893 | 2026-04-11 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 467881e7-8ef6-3059-9c84-d16d6ff08719 | 2.3789 | -60.9082 | 2026-04-11 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 30cd1c67-99e1-37ec-b70f-e3b559dde519 | 2.3789 | -60.8893 | 2026-04-11 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c4e61b43-03ee-345b-84e7-f6936cdab5b7 | 2.3789 | -60.8893 | 2026-04-11 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b060e6f4-bc93-3c52-a0c0-6947c3df9eba | 2.3789 | -60.9082 | 2026-04-11 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e37344d6-44b4-3645-b13b-540d322d354d | 2.3789 | -60.8893 | 2026-04-11 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 51b619b4-30e9-3654-8f15-d01f1f67bd62 | 2.3789 | -60.9082 | 2026-04-11 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 927fee73-8ec6-3ad2-97de-c26dec38992e | -21.05023 | -54.30676 | 2026-04-11 00:35:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dfdb7149-7e0f-38f0-b235-06fb1feeac9a | -21.49647 | -47.1811 | 2026-04-11 00:35:00 | TERRA_M-M | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3b6b15d7-ace5-3b92-ac84-7e2ff4ad67d0 | -13.24648 | -53.29021 | 2026-04-11 00:37:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f77b6a7d-c86b-3b95-bf8f-a5875fa81ccc | -13.24774 | -53.29925 | 2026-04-11 00:37:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| fc1b0890-d0fb-3c2f-b172-f48e5958aef2 | -11.59977 | -55.32578 | 2026-04-11 00:39:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3b5f437-0858-3bce-8eb8-07c9d9f8ac79 | 2.3789 | -60.9082 | 2026-04-11 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 9662668e-7cff-30a3-8f3c-cbb674db5e3a | 1.8269 | -60.866699 | 2026-04-11 00:41:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0218f73c-34fb-34a3-beb4-2b3cedcecd95 | 3.6902 | -61.5051 | 2026-04-11 00:41:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7b32e567-2331-3c99-81c2-0127d1fe1dc7 | 1.3667 | -60.670799 | 2026-04-11 00:41:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e95ed282-3f03-3ee3-bd1d-e90b454d160c | 1.3684 | -60.663399 | 2026-04-11 00:41:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| be412e00-766c-31c6-9a96-7f1eeef53b1d | 2.3747 | -60.903702 | 2026-04-11 00:41:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3e79c455-e3d8-3f78-95cc-6913269ea304 | 1.8286 | -60.859299 | 2026-04-11 00:41:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cd8bb52c-948e-38ee-8d57-008201b13059 | 3.6919 | -61.497501 | 2026-04-11 00:41:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 38cd8d81-5bce-3059-bf4d-cac444390f25 | 1.3701 | -60.656101 | 2026-04-11 00:41:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 44369d18-5a13-3235-9102-f389bc51a2f0 | 2.3781 | -60.889 | 2026-04-11 00:41:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ef0854f5-c06f-3206-9dc7-17e3ef0447f3 | -11.6059 | -55.322601 | 2026-04-11 00:41:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a66b7976-1ec1-3590-a96a-1e02471538ad | -13.244 | -53.2855 | 2026-04-11 00:41:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 228e6329-6991-3b9e-9532-fa503695d2a5 | -13.2458 | -53.293098 | 2026-04-11 00:41:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83c8d3e4-0f63-3df7-b798-d337cb292c62 | 3.6884 | -61.5126 | 2026-04-11 00:41:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 520564cf-b6f9-314a-806d-3286d475c6b1 | -21.051901 | -54.298401 | 2026-04-11 00:41:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d407b46d-88b6-3e54-8724-1b2cbbdb45db | 2.3764 | -60.896301 | 2026-04-11 00:41:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e595ad7e-b465-33be-9805-26f845961a59 | 2.3862 | -60.898499 | 2026-04-11 00:41:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fe57c511-37d9-364d-820e-7d0dd945a3bb | 2.38253 | -60.90827 | 2026-04-11 00:41:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 3ac84b63-47c6-33a9-833f-1928c1d4d5d4 | 1.27826 | -60.32887 | 2026-04-11 00:41:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7662f6fa-a60a-361b-b165-a1388663a360 | 3.69891 | -61.51106 | 2026-04-11 00:41:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 832548dc-6cf7-3408-bbb7-3db06eb418d8 | 2.372 | -60.90678 | 2026-04-11 00:41:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 92a11b0f-405f-39ac-b9c4-7433279522bd | 2.3658 | -60.80189 | 2026-04-11 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1753c154-010c-39ff-92da-8fc93169b067 | 2.38437 | -60.89544 | 2026-04-11 00:41:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 569f8e84-ea69-318b-9f5f-57b47fc96f19 | 1.37116 | -60.67163 | 2026-04-11 00:41:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b095d1f3-b653-3f19-9364-153b2a9f7f0f | 1.82445 | -60.87171 | 2026-04-11 00:41:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 25e804ed-4017-399a-9556-dc36c76a7895 | 2.3789 | -60.9082 | 2026-04-11 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 83.5 |
| c26f170d-2af9-3126-bff4-56d84c167356 | 2.3789 | -60.9082 | 2026-04-11 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 5c82888f-6991-333d-bde2-da229db3ceba | 2.3789 | -60.9082 | 2026-04-11 01:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1c1b4c3d-541c-3a35-89a5-2c019038ab81 | -13.2443 | -53.291302 | 2026-04-11 01:11:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dbe4b36a-2c66-3d3c-8ed4-05f84c3ba415 | 3.6943 | -61.5075 | 2026-04-11 01:14:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 51d8a7c9-64ee-3d50-877f-4868f68dee49 | 2.3819 | -60.890499 | 2026-04-11 01:14:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6e56176a-0c3b-3351-8a51-49efaa6bd01d | 1.8288 | -60.873299 | 2026-04-11 01:14:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0158ddf8-d6ee-3b73-b989-5f2266bbf737 | 1.8305 | -60.8661 | 2026-04-11 01:14:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 50250094-51e5-39be-a000-70559055c255 | 2.3624 | -60.795502 | 2026-04-11 01:14:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6edc4355-50c5-3b89-bfdf-7a416d9b3e73 | 1.2847 | -60.323002 | 2026-04-11 01:14:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| eb2ad389-9526-331d-b705-3c2022da9c08 | 1.2749 | -60.320801 | 2026-04-11 01:14:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 18da2926-38ff-3292-9b31-985da383c4e6 | 2.3769 | -60.912201 | 2026-04-11 01:14:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3f9b0e8e-e1b8-34e3-8f58-1fc28e189900 | 2.3803 | -60.8978 | 2026-04-11 01:14:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5364e51d-5982-3a6d-a177-d6d566afbb1c | 2.3786 | -60.904999 | 2026-04-11 01:14:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f4eb26ca-ee83-39f8-a31d-dc2fd0852f46 | 2.3789 | -60.9082 | 2026-04-11 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9811b7e3-1b95-3e52-8dcc-b71ddbaaa6b0 | 2.3789 | -60.9082 | 2026-04-11 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b9908010-d6b6-3fc4-98a1-13514f867405 | 2.3789 | -60.9082 | 2026-04-11 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 661b2448-2b30-3a81-af7c-f0c61dc2427b | 2.3789 | -60.9082 | 2026-04-11 01:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 757e18c1-01bb-3bcb-a431-27b1fc9db61f | 2.3789 | -60.9082 | 2026-04-11 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 3a5dd01f-5c36-3160-89b5-77b204adb9d1 | 2.3789 | -60.9082 | 2026-04-11 02:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 4b93ce5b-23b0-30dd-8943-1e9f60b008bd | 2.3789 | -60.9082 | 2026-04-11 02:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f6c24e3f-fc81-3050-98e3-8a4cc049237e | 2.3789 | -60.9082 | 2026-04-11 02:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 6a01ed6d-8193-3596-960b-6e617096fdba | -8.57335 | -37.00346 | 2026-04-11 03:10:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f25a2757-2828-3505-a52b-69da0849f27a | -8.56748 | -37.00222 | 2026-04-11 03:10:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 719e0075-0f1c-3525-bf20-24f65ff28afd | -8.57012 | -37.00465 | 2026-04-11 03:10:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 717f915a-1df3-36eb-914b-1da5bdabc335 | -8.5667 | -37.0064 | 2026-04-11 03:10:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f372cabb-c52d-337f-8de9-7651f3db13a7 | -8.63195 | -36.25985 | 2026-04-11 03:32:00 | NOAA-20 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e73b865f-988a-3c61-9854-7dfca53f1d9f | -4.36105 | -37.90114 | 2026-04-11 03:32:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd31ae36-5d01-3286-87de-c9d1fa0e4dfe | -10.58223 | -36.67757 | 2026-04-11 03:32:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cd545841-f72f-32dc-8f5e-38d0256e4c68 | -6.00012 | -35.33255 | 2026-04-11 03:32:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 42d64e30-b6be-368a-8f2f-5e7fc03edb7f | -8.56902 | -37.00463 | 2026-04-11 03:32:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 331e95bb-4e15-3e09-bd68-5bbe8bdec1f6 | -9.47125 | -37.21064 | 2026-04-11 03:32:00 | NOAA-20 | OLIVENÇA | ALAGOAS | Brasil | 2706000 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c0941f7-2fa7-356e-b994-10749def9b96 | -9.47277 | -37.20791 | 2026-04-11 03:32:00 | NOAA-20 | OLIVENÇA | ALAGOAS | Brasil | 2706000 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f9ec272-2531-3c58-9282-0cbd9b6413ff | -4.36076 | -37.90267 | 2026-04-11 03:32:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 442317c3-f4e0-3542-8d21-b510371e69d2 | -12.1075 | -38.26458 | 2026-04-11 03:34:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3d96ba7f-8ecc-3903-ac60-cb7b4f4a98e5 | -15.28267 | -43.07094 | 2026-04-11 03:34:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b0a5c409-5489-3f8d-b705-2945d1bfe2b0 | -12.10557 | -38.26244 | 2026-04-11 03:34:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3cb439e3-1cab-3c8c-a357-0fb84b9ec695 | -12.45965 | -38.35092 | 2026-04-11 03:34:00 | NOAA-20 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0b93c4e9-66d5-3004-92ca-b5ad1ad5c03b | -15.28331 | -43.06776 | 2026-04-11 03:34:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c207f441-3387-3d6a-a42d-08e65339e97d | -23.27846 | -46.60265 | 2026-04-11 03:36:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 67b505f1-8843-3662-8a4b-133c8d353218 | 2.3789 | -60.9082 | 2026-04-11 04:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 39.2 |
| a9c29a68-a7b6-38dd-979d-2a3dda2b2f66 | -4.36374 | -37.90026 | 2026-04-11 04:19:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0ee5d6b-6e60-360a-a8b4-cedf071491f0 | 2.3789 | -60.9082 | 2026-04-11 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 0424dc64-c6fb-3a83-808f-07b05e47b76f | -11.86709 | -43.86326 | 2026-04-11 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93b4adeb-22cb-3751-a60f-e3a42a78ed38 | -13.33731 | -43.40574 | 2026-04-11 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e0524a11-7090-3aa1-9a52-dd77c6e6e927 | -11.79604 | -43.63483 | 2026-04-11 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f9495939-5349-37a3-9c0a-a9bf4458f0f4 | -6.87105 | -50.37846 | 2026-04-11 04:21:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e74be371-a0a0-3dc8-96ef-08c5d1b1f488 | -11.04257 | -37.38486 | 2026-04-11 04:21:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b5dc0f0c-5511-3337-831b-01d06ba9177b | -11.79373 | -43.62659 | 2026-04-11 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a2a4551-8faf-3ad7-aaee-221eeae5a5b4 | -6.87025 | -50.37885 | 2026-04-11 04:21:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d97a73ba-7360-333a-81fa-bc1fc3254171 | -11.60557 | -55.32833 | 2026-04-11 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 609ed1d3-054d-3a0a-b81d-2124c6fdabc4 | -11.98793 | -47.14985 | 2026-04-11 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73839f28-3688-3f56-8c64-bf343cfcdf64 | -11.79259 | -43.63429 | 2026-04-11 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2136c60e-1932-3c7c-b071-d9ee5d6f7b00 | -11.79316 | -43.63044 | 2026-04-11 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 678fd147-3ce3-38b8-a623-e24db1b7dda9 | -7.35663 | -50.81364 | 2026-04-11 04:21:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a359e063-234a-30fe-a119-1b9e7143c36a | -10.20951 | -42.05436 | 2026-04-11 04:21:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 203c0676-0ebd-3200-b560-e24b7152c8af | -11.04294 | -37.38197 | 2026-04-11 04:21:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 53f3132e-9961-3796-922e-43f3e88f7827 | -11.79661 | -43.63098 | 2026-04-11 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3cb73469-da7c-3429-b047-dc00446df309 | -13.67972 | -41.0177 | 2026-04-11 04:21:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 250e24ce-fde6-3ac4-976b-2d41988daca9 | -8.56978 | -37.00281 | 2026-04-11 04:21:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| abc3bd9e-6112-3f57-be78-51647abe9d77 | -8.79228 | -44.82426 | 2026-04-11 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77b3d6fa-3009-384b-a89e-bde085b81779 | -14.1269 | -43.41745 | 2026-04-11 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
