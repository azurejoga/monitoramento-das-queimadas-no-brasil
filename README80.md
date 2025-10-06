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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f1bfc2a-febd-3938-a1d4-4a8ec5e6e18e | -4.65569 | -43.18928 | 2025-10-06 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e234f9eb-be35-3fa3-8f75-e6a931283b8b | -6.63865 | -41.98751 | 2025-10-06 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 8d514b32-f4aa-3a12-9911-a247fa8d51bc | -5.85798 | -42.78471 | 2025-10-06 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 23d2b9d4-aa2f-3ba5-a774-5618ed5a5608 | -6.06672 | -42.55433 | 2025-10-06 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 2e81c199-b4bd-37a9-a1bb-3fa153d40834 | -6.63659 | -45.72237 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| be350c9e-c01c-350d-9d13-cad215a23c84 | -7.4244 | -41.12293 | 2025-10-06 11:57:00 | TERRA_M-M | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| db511efd-4e3c-378c-bbb2-f5714d04416e | -3.6225 | -42.16949 | 2025-10-06 11:57:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 06cdd314-5062-30b6-910e-b135125129ca | -5.86428 | -42.80387 | 2025-10-06 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 1f39d696-afe2-37f6-b3e4-01a5868ef0ce | -5.28334 | -43.31285 | 2025-10-06 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| da9ed8a3-b6ab-373c-afc8-006929d93c8b | -3.98173 | -42.36258 | 2025-10-06 11:57:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 2a81b283-32c0-3a31-b8c3-9ce3b53b640b | -6.45353 | -44.56612 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 747318ba-fd9d-3806-ba29-5154906c251c | -4.44626 | -43.23266 | 2025-10-06 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| ba0ae1bd-0079-3e72-bdc9-22a9ace1e917 | -5.85856 | -42.53055 | 2025-10-06 11:57:00 | TERRA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 129dec5f-452f-3443-8d81-30ae37e91505 | -5.835 | -42.81813 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 533e2df8-8b58-3bb0-a073-50a90e832dc4 | -5.50459 | -42.23944 | 2025-10-06 11:57:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| f93913fa-01ce-35fb-b203-798b9407c9fb | -6.068 | -42.54546 | 2025-10-06 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| efb504a1-2475-35a1-89ba-8d66ad03eca8 | -7.14048 | -40.78342 | 2025-10-06 11:57:00 | TERRA_M-M | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| f378bf04-23c4-3e45-baaa-2f4f11d72336 | -6.07685 | -42.5467 | 2025-10-06 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 7bf86fce-4b42-32d0-809d-47ef2b4d28fb | -5.93149 | -43.2977 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c765e498-3958-33e5-af93-40466647d0e4 | -3.49784 | -43.34486 | 2025-10-06 11:57:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 9cbb0b27-19bb-32fa-8b31-347fc511aa56 | -7.00556 | -42.82855 | 2025-10-06 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 7f8881b4-f649-39dd-97de-a3d9f034db49 | -6.62094 | -44.3191 | 2025-10-06 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 572fdc27-feb2-308b-a17e-c111eaa4c2b2 | -7.00297 | -42.84637 | 2025-10-06 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 7f5c2ef8-45e6-3ac9-9bec-265f840ede18 | -5.76818 | -42.96479 | 2025-10-06 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| e36d1db8-bad8-3f83-869a-22986f75221c | -6.13445 | -42.66096 | 2025-10-06 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| b806f896-2cd1-3fb2-851e-34b503ed61bf | -5.84887 | -44.29003 | 2025-10-06 11:57:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 22a6b1d4-6a38-3bb1-b58b-9aba1f2eaec3 | -6.60575 | -44.84587 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0bc93f69-ba7f-3dea-a733-4cd242958a3c | -6.24956 | -44.2706 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 3b83a59f-3d63-3090-b72b-d86a6e3a856c | -3.2291 | -41.96326 | 2025-10-06 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 57d25320-a0d3-367b-b042-e7c51fc903bb | -6.108 | -43.10246 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 807e67f3-04c3-3c9a-95dc-188155a48ae6 | -6.72309 | -42.8059 | 2025-10-06 11:57:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 93e131b5-876d-3e34-aeeb-f583aafa4592 | -5.65358 | -42.73433 | 2025-10-06 11:57:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 33b75a7c-237a-3941-89b4-f8ceb94cff20 | -3.68965 | -38.84157 | 2025-10-06 11:57:00 | TERRA_M-M | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 6735c9ad-d5e9-3646-8a55-0abb5a1eecac | -6.26073 | -43.25144 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e23e1568-2441-3c22-8165-0079c2751ff3 | -7.14181 | -40.77399 | 2025-10-06 11:57:00 | TERRA_M-M | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| d62c03a0-0b3f-375e-b542-1d94fe8b44fc | -6.20217 | -44.09564 | 2025-10-06 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| b7acc97d-0bea-3a1d-9ec3-98ced25d757e | -4.64528 | -43.19729 | 2025-10-06 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1a0ec669-503e-381f-b87f-0436f95fd863 | -12.4464 | -45.5876 | 2025-10-06 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 26e70c26-f6e9-32f2-bc49-c3e5fb7b6cf0 | -10.7281 | -46.6433 | 2025-10-06 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e803a2bc-b514-3323-9c2a-469622f0b5ec | -8.6139 | -46.3227 | 2025-10-06 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e382d73b-3ab3-31ec-92c8-03a8df79e5b0 | -8.6144 | -46.2778 | 2025-10-06 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| cdcce441-42e8-3fce-b53d-1746fb947674 | -15.3541 | -47.3235 | 2025-10-06 12:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 1db359b6-e3af-34e0-9fb1-4f3bb148c1b9 | -17.9748 | -44.3835 | 2025-10-06 12:00:00 | GOES-19 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e496ee5d-0a90-3ed8-b305-71e4a61b5f7a | -14.863 | -51.5019 | 2025-10-06 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| a4626b60-6a50-3ad8-a8d9-7f18a8de1109 | -12.4468 | -45.5646 | 2025-10-06 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 8b196a25-e699-3f13-8ac5-ed77b85c74c1 | -12.3796 | -47.1633 | 2025-10-06 12:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 10b81749-192d-3c20-8c0a-a7ed8dd1ea64 | -15.3546 | -47.3007 | 2025-10-06 12:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 1b4d9c75-964b-317e-b5b8-71f2993ab7eb | -14.6893 | -48.4021 | 2025-10-06 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 05a9f3ca-6ce8-3bc1-ae36-904c45cd5b8e | -13.3237 | -48.0547 | 2025-10-06 12:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| a873483e-a221-3c44-ac6c-5611741bab6a | -10.3643 | -48.1519 | 2025-10-06 12:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a2013556-037c-39c4-af53-4694ea4d09fc | -18.1371 | -53.3732 | 2025-10-06 12:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 4fc34b2a-aa4f-3a26-bf86-680e36f8e058 | -14.8626 | -51.5234 | 2025-10-06 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fceae272-ba6d-3f36-9fa3-7546b0295ca2 | -17.8417 | -57.6254 | 2025-10-06 12:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 9113bb5a-bc6d-3aab-9cae-0f2bb3d5541e | -14.882 | -51.5207 | 2025-10-06 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d17f11d9-38d1-39f7-848b-d5b8b9486d68 | -14.5438 | -46.9633 | 2025-10-06 12:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 495731e8-258f-3626-a392-c8df7921108c | -14.3161 | -52.9764 | 2025-10-06 12:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d1a731a6-9876-305e-8a0b-0c571c30db5d | -8.6141 | -46.3003 | 2025-10-06 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 3ec38921-2dd1-31fc-8db3-b2ff4c669844 | -18.2773 | -53.3082 | 2025-10-06 12:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c2c248aa-8422-3d0b-875f-d941cd4d2ae5 | -8.5196 | -46.3323 | 2025-10-06 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 392b7340-257e-3ed5-8989-7b9dc4fea92e | -14.6897 | -48.3797 | 2025-10-06 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b0cdfaad-df79-3662-9f0d-5cbbfba0f971 | -13.7256 | -48.07003 | 2025-10-06 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e8e4c6ba-ad6d-3f4f-8e2d-05ad9a220172 | -9.48528 | -45.99964 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 41e9bb5b-3305-3071-8e1e-3fa7456905ef | -7.46919 | -43.06207 | 2025-10-06 12:00:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 482a1c10-0837-365a-91c2-9342849affe1 | -8.15932 | -44.2694 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| c8d2c67f-7b47-35cb-bc6e-afffd75143b5 | -9.84822 | -45.76403 | 2025-10-06 12:00:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a3ff4e9e-ab4e-37ea-9eaa-5fbb9b05788b | -7.68739 | -42.57945 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 57f65db7-c281-35fb-820c-133f2280972f | -7.27147 | -46.96302 | 2025-10-06 12:00:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 859b03fc-5c9c-3145-847e-19983dab0a11 | -16.34877 | -47.05012 | 2025-10-06 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 89c36713-52ec-3cf9-9c49-830ab321345d | -9.91349 | -50.17482 | 2025-10-06 12:00:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 27080d00-f641-3da3-b938-afe094b051db | -11.07462 | -47.91964 | 2025-10-06 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c23fc941-ef7f-3d4a-ad42-f0bd899082e4 | -17.29841 | -43.89476 | 2025-10-06 12:00:00 | TERRA_M-T | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9639c0aa-b304-3c39-853d-165cb925f2ab | -14.91587 | -46.82743 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 666f9506-b7fc-37d5-a8ac-744901162149 | -11.70491 | -45.43073 | 2025-10-06 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0408cfe2-2587-3775-b076-36903d5747f8 | -11.94263 | -46.42073 | 2025-10-06 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7e1b4564-a78c-3e51-853f-9ff3fd961bc1 | -8.50695 | -46.36059 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| a2463f35-a5b7-39a9-bdfb-5eaa89d559d8 | -14.6901 | -48.38587 | 2025-10-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 37.7 |
| f4563e00-ecf9-3e70-97e3-567c579137fb | -8.88669 | -47.61938 | 2025-10-06 12:00:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 5c768506-7669-329e-823a-d8c3613cac38 | -14.54576 | -46.96146 | 2025-10-06 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 3118ea38-f496-331a-8fa6-0f85874352e3 | -14.51968 | -42.15653 | 2025-10-06 12:00:00 | TERRA_M-T | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4b1a336b-ff2e-3aec-a6c4-df4b71843549 | -15.57223 | -52.44032 | 2025-10-06 12:00:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 0c40066f-0909-3003-a2f5-3f8f14814480 | -15.17219 | -45.75967 | 2025-10-06 12:00:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d836ec95-c682-3bc4-95ea-d1103987c28f | -7.87564 | -44.13484 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| aa870980-af25-3d4a-b5ac-f5d89cdf3bb2 | -8.87378 | -46.79499 | 2025-10-06 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 7002b4ca-2965-33b2-999b-9881d4f611bc | -7.68612 | -42.5883 | 2025-10-06 12:00:00 | TERRA_M-T | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 42.0 |
| f9ba3fad-4288-353e-9d21-90d6a77c8cc0 | -14.27189 | -45.85976 | 2025-10-06 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f562be84-30a8-3cdd-b38e-fb925c57d7dd | -13.27015 | -48.46799 | 2025-10-06 12:00:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| da1ab0a5-0da0-3f2f-b988-06019887a077 | -16.74444 | -44.23317 | 2025-10-06 12:00:00 | TERRA_M-T | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86d0f90a-9827-3cb8-9535-b51908ef35e0 | -10.62796 | -48.68768 | 2025-10-06 12:00:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 656a32f0-66fa-3b49-bb87-ac33be71ab36 | -13.21684 | -46.53732 | 2025-10-06 12:00:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 806a65bd-23f5-306e-a65d-2c5ef174bc60 | -12.86315 | -43.20123 | 2025-10-06 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| fdebadf3-7d90-39e1-9618-9da7547ee2eb | -17.85395 | -41.97956 | 2025-10-06 12:00:00 | TERRA_M-T | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 1197cfb1-9bd5-3311-8c5b-30e982d101bd | -8.19815 | -44.19698 | 2025-10-06 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| bdadc43e-c02c-3841-b8b0-65447f81175e | -13.6788 | -47.32872 | 2025-10-06 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 66abf11a-e4af-32de-ab22-24cda42e3f9f | -14.34522 | -47.72112 | 2025-10-06 12:00:00 | TERRA_M-T | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 42d06bca-876f-311d-b739-e0ec81011b2b | -15.50786 | -46.83718 | 2025-10-06 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| aee51d35-b1fd-318e-8f84-b4797729790e | -15.34235 | -47.31212 | 2025-10-06 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9822d805-537b-3147-8e15-162d5d249476 | -17.5535 | -42.57045 | 2025-10-06 12:00:00 | TERRA_M-T | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 98a4606c-eac7-3b5a-9e60-22e148d5124f | -11.04013 | -47.77963 | 2025-10-06 12:00:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 14a70ca7-2a97-32cc-a761-88392798da3d | -13.37929 | -47.58812 | 2025-10-06 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 5d241f74-5ce5-3a05-83a7-27179909a82d | -9.14289 | -41.15661 | 2025-10-06 12:00:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |


[Clique aqui para ver as próximas entradas](README81.md)
