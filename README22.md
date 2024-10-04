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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c8b505a-ece4-31e8-8a5f-89995d64af6e | -16.5928 | -57.2397 | 2024-10-04 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 17230d63-eb09-3c6f-a93b-1bfc853e69ae | -16.5935 | -57.1988 | 2024-10-04 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 9623cb46-2584-37d6-9311-f8e7edaea9a1 | -16.5938 | -57.1783 | 2024-10-04 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 7cead2ad-5a7a-349d-b088-d3d721620377 | -16.9302 | -47.1224 | 2024-10-04 01:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| b23fc423-8a7f-31ab-8a88-67b78e678773 | -16.95 | -47.1185 | 2024-10-04 01:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 87.9 |
| c603e2ef-8cf3-3181-a1ad-80a0e8f9db8e | -16.613 | -57.1965 | 2024-10-04 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 2a29c938-8216-3365-9392-48bcfb698f5a | -16.6133 | -57.176 | 2024-10-04 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.1 |
| b2c5fc9f-d970-387b-a639-93aaeda0a66d | -16.679 | -55.5402 | 2024-10-04 01:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| a36d038a-2bbf-3674-95eb-d4fe9a22b6d5 | -16.7606 | -57.7512 | 2024-10-04 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| fa956a99-ea8a-347a-b8e1-bf2869f75490 | -16.779 | -57.8306 | 2024-10-04 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 042028d5-6876-3f1b-9695-bcb219b6ffc3 | -16.7856 | -57.4015 | 2024-10-04 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 6c3049a2-919f-3403-9b4b-65347f3876b3 | -16.7859 | -57.3811 | 2024-10-04 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.8 |
| 50a32314-cc33-3ff7-b04d-2d089f537fc3 | -16.7985 | -57.8284 | 2024-10-04 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| e4a5c34b-1cc0-33ac-8cf3-438f3e8dc209 | -16.8051 | -57.3993 | 2024-10-04 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.7 |
| b48bac86-8e2c-399b-9218-f21cc3b4aaec | -16.8055 | -57.3788 | 2024-10-04 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 5180263a-7b1b-310b-bcbb-4e066b32274d | -16.843 | -57.4767 | 2024-10-04 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 82a1bd32-547c-369b-a2b2-9f3fb1ddcd80 | -16.9084 | -55.8638 | 2024-10-04 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| ec67f91f-c813-3d81-bc3d-168973b86292 | -16.9087 | -55.843 | 2024-10-04 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 5f8f4c10-7455-3de8-b766-cda482a333f3 | -16.9283 | -55.8405 | 2024-10-04 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| a9232188-f003-3691-adb5-5e813c574dbe | -16.9287 | -55.8197 | 2024-10-04 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 98723e2f-0232-3c95-be70-0a1523b9a4d5 | -17.3844 | -42.6235 | 2024-10-04 01:06:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 898b0999-496c-36aa-8f41-8e96e1a10956 | -17.0616 | -56.0723 | 2024-10-04 01:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 3ceca4ee-ca35-3506-9e8d-6053bf45942e | -18.8413 | -42.8985 | 2024-10-04 01:06:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| fec2d656-8845-3008-a05e-20b1b5711af8 | -18.8609 | -42.9182 | 2024-10-04 01:06:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.1 |
| 44841379-8189-35e0-bc65-abe8c04d1d9d | -18.8617 | -42.8932 | 2024-10-04 01:06:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 150.5 |
| 67b1cb6a-244b-384e-bd4b-1599214fc159 | -18.8613 | -43.5837 | 2024-10-04 01:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.3 |
| a5f4a311-53e5-30fd-bbd5-156477bfc162 | -19.2794 | -43.795 | 2024-10-04 01:06:52 | GOES-16 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 6bbc81d3-75d2-3523-9328-13a9f5d2dd06 | -19.2801 | -43.7703 | 2024-10-04 01:06:52 | GOES-16 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 73b4bb5b-adbf-3f3f-99c6-ea8f8a285bfa | -19.3167 | -42.5724 | 2024-10-04 01:06:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| 83f9b2f6-7027-37d1-91d1-51f2adc458f0 | -19.3371 | -42.5668 | 2024-10-04 01:06:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 91b29629-d021-33b3-b31c-f19e81004a31 | -19.4899 | -42.8746 | 2024-10-04 01:06:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 130.4 |
| 463ef442-c603-3ce3-a6f6-0549d5d27494 | -19.5104 | -42.8691 | 2024-10-04 01:06:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| 4f249bf0-9f9b-3b57-a851-ba78b3485894 | -20.121 | -43.5219 | 2024-10-04 01:06:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 128.8 |
| e5d844ce-f915-3112-bf80-8c8171f9e4d5 | -20.1218 | -43.4969 | 2024-10-04 01:06:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.9 |
| 8d8e278f-31d9-35e7-9784-ff3fda52a179 | -20.1416 | -43.5162 | 2024-10-04 01:06:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.0 |
| 5967e920-6d06-3053-88cc-b6321cd55cda | -20.1424 | -43.4913 | 2024-10-04 01:06:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 8a8e67ee-cc45-3a17-a88f-9c17fbd46c22 | -20.4591 | -43.1795 | 2024-10-04 01:06:58 | GOES-16 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| 9e8e82fa-6102-3d21-82ca-b3943c672b44 | -20.4797 | -43.1736 | 2024-10-04 01:06:58 | GOES-16 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.0 |
| 39489e20-c34d-37f3-ab06-19ffe1062552 | -22.26704 | -51.4868 | 2024-10-04 01:07:00 | TERRA_M-M | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.3 |
| 330ac3bf-4171-33fe-ac06-4c1b767163ae | -22.2656 | -51.47496 | 2024-10-04 01:07:00 | TERRA_M-M | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 97295bb4-f91f-3d12-8aa7-a98c1bb5ca48 | -22.57225 | -52.00291 | 2024-10-04 01:07:00 | TERRA_M-M | ITAGUAJÉ | PARANÁ | Brasil | 4110904 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 46612e29-a619-316d-a37e-769f0f8ed746 | -20.18147 | -41.58649 | 2024-10-04 01:07:00 | TERRA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| d28b8a6b-f533-3a8e-b4d9-2fa5268c54eb | -17.91627 | -42.18855 | 2024-10-04 01:07:00 | TERRA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 1509e036-ca9e-310b-8e77-c4561da053e2 | -17.62166 | -42.01137 | 2024-10-04 01:07:00 | TERRA_M-M | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 0e7e877a-fc4f-3ea3-800a-a11d27ddff9f | -17.38651 | -42.62583 | 2024-10-04 01:07:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 258f341b-99a3-3c45-8af5-be9f0668fad2 | -17.37584 | -42.63363 | 2024-10-04 01:07:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 106.0 |
| bc5e9f59-9188-3d38-8d8a-e70d8dc7c018 | -17.37365 | -42.62847 | 2024-10-04 01:07:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 65d6495e-61d9-3873-a8f3-1df1b4f3d84d | -17.37217 | -42.61246 | 2024-10-04 01:07:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 43.1 |
| d1af6520-7299-3960-992c-d73e75d1f79b | -17.36295 | -42.63617 | 2024-10-04 01:07:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 40.2 |
| e0551b4f-83c1-3e87-8c78-97fec7cc3de9 | -17.35927 | -42.61509 | 2024-10-04 01:07:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 69616e2d-501d-3fb8-b4c9-00b3a6a742bb | -19.03025 | -43.20198 | 2024-10-04 01:07:00 | TERRA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 54d5d882-114c-3eb9-9dfd-b8313858b441 | -19.02738 | -43.18533 | 2024-10-04 01:07:00 | TERRA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| e987fa37-7920-334b-9489-fc8da15ca808 | -18.86407 | -42.92035 | 2024-10-04 01:07:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 82549f45-362f-3975-b419-d8b4a5847271 | -18.85175 | -42.92228 | 2024-10-04 01:07:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.6 |
| 10a83440-65ed-3d8e-939e-00bffbf4ae11 | -18.8485 | -42.90386 | 2024-10-04 01:07:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.6 |
| d5020af7-eb06-34e9-a97b-079b9abfbae0 | -18.83949 | -42.92455 | 2024-10-04 01:07:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| e6a5bbcb-926a-3a52-82c8-3f982370388f | -18.83609 | -42.90539 | 2024-10-04 01:07:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 69a39e35-4f75-3b04-835f-3e28ec5612b4 | -18.83357 | -42.91253 | 2024-10-04 01:07:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 83466fcd-ae19-360f-9764-3d76320706b4 | -18.82513 | -42.98559 | 2024-10-04 01:07:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 7daa76fe-3031-3884-9a31-f5df71414c7e | -18.82201 | -42.99242 | 2024-10-04 01:07:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 04e2e290-8e21-35ac-8343-a7332b008b2e | -20.52225 | -42.8891 | 2024-10-04 01:07:00 | TERRA_M-M | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 24ab1c2f-3393-30be-bb2c-0e5db493d154 | -20.50991 | -42.37149 | 2024-10-04 01:07:00 | TERRA_M-M | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| ffcd680d-8e4d-3f55-9fdf-0977e7d29b59 | -20.47097 | -43.19314 | 2024-10-04 01:07:00 | TERRA_M-M | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| daa42752-50b6-361a-aaac-c97689a2d60a | -20.46806 | -43.17655 | 2024-10-04 01:07:00 | TERRA_M-M | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.2 |
| 2d47fdf4-384f-3a7b-9710-4a8477f25f4f | -20.45938 | -43.19553 | 2024-10-04 01:07:00 | TERRA_M-M | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| 441b0978-ed95-3716-9e54-8f66f5daa3c2 | -20.45643 | -43.17878 | 2024-10-04 01:07:00 | TERRA_M-M | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.9 |
| 9c12108a-3358-3921-97c2-ac464396d336 | -20.43346 | -42.53049 | 2024-10-04 01:07:00 | TERRA_M-M | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 9ae99446-7c3b-366c-b460-e118f468e34b | -20.26411 | -43.53115 | 2024-10-04 01:07:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| bd8fbbc3-57ba-3c0a-b1a8-3077b80377ee | -20.25041 | -43.19668 | 2024-10-04 01:07:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 5da7f7ba-c143-3821-aff6-0504989d8883 | -20.24747 | -43.18013 | 2024-10-04 01:07:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| a7607f49-6e89-341f-8c56-7a98b8cc96d4 | -20.24075 | -43.187 | 2024-10-04 01:07:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 51f1c01b-1a53-3aff-b57a-04b4a8e1957d | -20.10006 | -43.44579 | 2024-10-04 01:07:00 | TERRA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 9c82e935-0a85-379f-95e8-f8b654dc978a | -20.09637 | -43.4239 | 2024-10-04 01:07:00 | TERRA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.3 |
| bc324d13-398e-3ea3-ba81-0df59f05977f | -20.08839 | -43.44675 | 2024-10-04 01:07:00 | TERRA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| 750fd60b-3a8f-3c62-8340-373848671749 | -20.08463 | -43.42461 | 2024-10-04 01:07:00 | TERRA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| aa80c392-c122-33c0-8509-8810684d6d3f | -20.07638 | -43.44574 | 2024-10-04 01:07:00 | TERRA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 53f4bda8-2fb3-38fa-9ec0-3fba725c6fb4 | -19.85169 | -42.38253 | 2024-10-04 01:07:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 1fc37eea-02ad-3604-b044-ebd896899259 | -19.85089 | -42.38882 | 2024-10-04 01:07:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| a8cfa259-03a2-32ce-8627-974daed54ddc | -19.84777 | -42.37098 | 2024-10-04 01:07:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| b0da6236-04c7-3257-b981-799eedd56519 | -19.8045 | -41.90369 | 2024-10-04 01:07:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 886068f4-adcd-30b1-91eb-cc9dcf216584 | -19.61769 | -42.26052 | 2024-10-04 01:07:00 | TERRA_M-M | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.4 |
| 6433aafc-ca80-3426-a3ff-4ec0e069884f | -19.61723 | -42.25429 | 2024-10-04 01:07:00 | TERRA_M-M | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.2 |
| d04e98bd-41cc-3902-8e90-ee9f82c50b92 | -19.57228 | -42.74374 | 2024-10-04 01:07:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 5cd99877-1585-3086-aa60-144324e84c85 | -19.56883 | -42.7242 | 2024-10-04 01:07:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| f4b682a9-6b0f-3c42-8c59-261212d3e25d | -19.49262 | -42.8884 | 2024-10-04 01:07:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 166.1 |
| 724b59c0-2789-37cf-8731-6fe97b1e4cdd | -19.48937 | -42.87004 | 2024-10-04 01:07:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.8 |
| 3b46b8ce-4448-3eac-8d4c-0bb46a6d0ec5 | -19.44787 | -43.08776 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 45a7b1a9-a49a-33e3-84d3-c4d588ef0014 | -19.44493 | -43.07096 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| 8b9e5221-1461-3a6f-a06c-ce395813ae5d | -17.73793 | -43.81674 | 2024-10-04 01:07:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 0531d9c9-67cc-3a3c-bf8b-af587b83cd8c | -17.73516 | -43.80037 | 2024-10-04 01:07:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 31.8 |
| ddca8d91-0f44-339d-a94d-cd2a3aa30bf0 | -19.29098 | -43.78589 | 2024-10-04 01:07:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| af11cf64-a120-3220-b00a-216f53a3523d | -19.2824 | -43.80428 | 2024-10-04 01:07:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 81899f9f-9225-3c6c-b826-34bd595b733a | -19.2796 | -43.78794 | 2024-10-04 01:07:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 83a6e2da-db54-3b55-b104-dfa3d578ed54 | -19.27682 | -43.77176 | 2024-10-04 01:07:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| af919ddf-7048-390b-a943-1fd25749a9d7 | -19.23419 | -43.38468 | 2024-10-04 01:07:00 | TERRA_M-M | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8db4bd76-f507-34be-97ba-234c3079af15 | -19.17595 | -43.51277 | 2024-10-04 01:07:00 | TERRA_M-M | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 31.9 |
| a15a88d1-5292-3fde-84e4-34ecd9274a2d | -18.87791 | -43.46149 | 2024-10-04 01:07:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| fb4b909b-9a38-351b-aad4-c8378903396e | -18.86674 | -43.60646 | 2024-10-04 01:07:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 459812bc-a5b4-3d05-89ca-47c01c8584e8 | -18.86407 | -43.59111 | 2024-10-04 01:07:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| d8dd4b3c-28b6-3f72-ad6a-d0d6426039fc | -18.8609 | -43.57286 | 2024-10-04 01:07:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.2 |


[Clique aqui para ver as próximas entradas](README23.md)
