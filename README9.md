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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f95f3dfe-c4fa-39c1-8d34-f5690443a4db | -17.34428 | -42.65436 | 2025-09-15 03:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 788bde99-25cf-353e-a4c2-bb508f38bc22 | -17.33438 | -42.6488 | 2025-09-15 03:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8bc103e-8200-33e0-8b6e-6506d996cc90 | -17.3485 | -42.652 | 2025-09-15 03:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 63f8899a-5dd5-3d9c-874a-16c2f855aca2 | -17.33886 | -42.64576 | 2025-09-15 03:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5986d6c3-a0be-3bdf-b306-9b9ba21816a0 | -17.34593 | -42.64727 | 2025-09-15 03:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 131c12fe-64ac-3c86-bc4e-6bfe15f2e766 | -17.34146 | -42.65031 | 2025-09-15 03:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 326186d1-9192-3720-9b07-398e616952a4 | -17.33976 | -42.65739 | 2025-09-15 03:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 397130ea-9f65-3321-b818-85d72d56c533 | -17.33723 | -42.65267 | 2025-09-15 03:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3b1fd977-5ef1-370c-b067-dd270d37dd3c | -12.006 | -47.7505 | 2025-09-15 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c93b33b3-3206-336e-b05a-0ea997fd70bd | -10.9365 | -45.5063 | 2025-09-15 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 60366b2c-baa8-3525-86e1-9426799925f3 | -14.9416 | -46.5525 | 2025-09-15 03:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 72d9ffae-21aa-3e9e-af6b-c71fbf50db98 | -12.9984 | -47.9685 | 2025-09-15 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 0422c17d-eefa-3701-9cfc-c703b07af7cf | -8.9787 | -45.8118 | 2025-09-15 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 7c81e389-c840-3b9d-be1b-04e95cf303b2 | -12.9791 | -47.9713 | 2025-09-15 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| b29e2a8f-070b-3757-adb7-2185b9336884 | -23.4754 | -47.37 | 2025-09-15 03:20:00 | GOES-19 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.9 |
| 02d34ea8-a77b-3ff9-8797-87e0fbbea59b | -10.9369 | -45.4833 | 2025-09-15 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 44c1572d-be3a-3d2a-aed2-61a07fa0713d | -8.651 | -46.3637 | 2025-09-15 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| cac150bb-f68f-3b11-91d4-500615c4dd6a | -6.17261 | -41.19962 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8292736d-f152-3f0e-9ad0-4ae42f91aca4 | -5.84495 | -44.16662 | 2025-09-15 03:28:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a01a785-859a-3138-afab-f93f01c80efd | -5.84559 | -44.16586 | 2025-09-15 03:28:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5eee21c-99f0-3e3d-ae3a-0542d8a356d4 | -4.66144 | -40.56317 | 2025-09-15 03:28:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0f5e8fa9-699a-3a89-995d-6a8fb170ef6c | -5.95413 | -42.79823 | 2025-09-15 03:28:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 34231c31-4f0b-3e2f-bb6a-a865f728dedb | -6.16726 | -41.19864 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2bf8962a-e073-302b-8c82-6df790eaa34c | -7.30232 | -43.96077 | 2025-09-15 03:28:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c9c22aa-c7e6-3570-8815-f67bf9fd32b0 | -6.97062 | -44.55346 | 2025-09-15 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2177b1f6-6021-3ccd-a5a2-1a2debe099bc | -5.74834 | -43.92367 | 2025-09-15 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9088e160-48c6-37d3-beb8-a6f265775140 | -6.42225 | -42.60725 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7eb1f760-e28d-3fc8-98c5-9af68969eec7 | -7.30326 | -43.95575 | 2025-09-15 03:28:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f7a2c60-dced-3ec3-b693-68c50535364c | -4.17263 | -42.03381 | 2025-09-15 03:28:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d5c666c3-49c6-3bf3-beeb-0d82faf2d2f5 | -6.18096 | -41.18367 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8eed26b2-5600-3e4f-b8c1-56b081482121 | -6.428 | -42.60879 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 234785f4-3425-31b9-adff-7e474fa04958 | -5.27995 | -45.25885 | 2025-09-15 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 658bc050-8ca3-3dda-ae7b-288390af1f81 | -6.96951 | -44.55939 | 2025-09-15 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f63deb06-8afa-358d-baaa-5627c79d8e06 | -5.74737 | -43.92913 | 2025-09-15 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08de7589-bfa1-330c-bc9f-8825fc8ce6b2 | -6.18036 | -41.18705 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c89c3768-27d0-3d58-9984-29735c2e9e91 | -6.17383 | -41.19277 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 16acf0e6-7d7d-358c-bf8e-722ab42ae505 | -6.05181 | -36.35341 | 2025-09-15 03:28:00 | NOAA-20 | CERRO CORÁ | RIO GRANDE DO NORTE | Brasil | 2402709 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 235ac7f0-55d2-32ae-b39c-912bd3dee3dd | -5.74903 | -43.9267 | 2025-09-15 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f7bee2bb-f6b7-3f74-b56c-42a3f33469d6 | -6.09903 | -43.72147 | 2025-09-15 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 36acc29a-3cdd-3d10-8077-276e83c7b689 | -6.17443 | -41.18937 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 302097a6-1e00-3e99-8f13-3fe34c1239f9 | -6.1556 | -41.18611 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9151f9a5-b158-3b16-bf18-e2d5c6d3d752 | -6.34463 | -43.1633 | 2025-09-15 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9faeb9a-656f-3851-9dc9-a71532c8f593 | -6.17322 | -41.19618 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d6d0591e-3a74-38a2-a3d9-a38b6935c314 | -6.16604 | -41.20554 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f1131438-d7a7-3512-9535-4568ccd53bee | -6.41495 | -42.61411 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| da9d472a-3647-3ef7-ac5c-290867a2b36e | -6.15901 | -41.18301 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1be6be52-99c9-39ea-ae7a-4586b0b0b8de | -5.47701 | -44.689 | 2025-09-15 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 031ca311-7e0d-3a39-920b-5abdbc82e6ad | -7.35305 | -44.29776 | 2025-09-15 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73965b3a-34e0-3d51-b574-be9b887a7fc8 | -6.16665 | -41.20209 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 52472bfa-e2ab-34b5-9744-cefaf4c96831 | -5.47592 | -44.69506 | 2025-09-15 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9d1ea115-3921-37f5-b000-d6a47db08ab9 | -5.92849 | -44.87004 | 2025-09-15 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e480d055-811d-3f1f-ab96-a0212d922808 | -5.95789 | -42.79367 | 2025-09-15 03:28:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a227a974-4ee1-3fe1-ba4a-3f25c6d6a9ed | -6.34942 | -43.16562 | 2025-09-15 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06f981a1-8b33-3f3d-b22e-ba585245ab57 | -6.15619 | -41.18266 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6a5682d-2760-3014-a411-57f7d20f53d9 | -6.41585 | -42.61486 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4100aa6b-87b2-392c-8a65-e2ed66acd8b4 | -6.34375 | -43.16812 | 2025-09-15 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c2c4173-b5f2-39be-8abe-f96f61c60524 | -6.35166 | -42.5411 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d626cb9c-86e7-3e90-9130-33543870c1d6 | -6.42885 | -42.6096 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 847aeb36-480c-3586-a8f9-d605652c7945 | -4.17409 | -42.03038 | 2025-09-15 03:28:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 943efe08-063a-3387-956f-a6af1442a87d | -6.42309 | -42.60803 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9d88c343-a616-38aa-8ef8-0b580a5c8595 | -5.93526 | -44.87116 | 2025-09-15 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2939792-d469-3fd8-8957-80458f63e931 | -5.6491 | -42.59847 | 2025-09-15 03:28:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 122bf8d3-e72d-384a-a206-ff20528afb29 | -5.28693 | -45.26012 | 2025-09-15 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e32f6c00-0c70-3ded-bd69-0cfa2c1c3f5a | -5.28115 | -45.26056 | 2025-09-15 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84fff4ba-01f0-30f8-b940-88ae8289f1d7 | -5.18328 | -45.1741 | 2025-09-15 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8f85e1d6-481a-3b64-b562-55e52f3a1e5a | -6.18215 | -41.17691 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 293e90ef-089a-3e28-89c0-bc1df85279a3 | -6.9157 | -46.17846 | 2025-09-15 03:28:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f130c37c-7f97-35c6-8893-03b7cadff552 | -6.97796 | -44.55033 | 2025-09-15 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 91cc7e32-ebe2-34a1-bcda-4d8e649300cd | -6.15962 | -41.17958 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43eeba4e-6792-33a5-9f4a-f619e11c82a9 | -4.63214 | -38.56885 | 2025-09-15 03:28:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cca7ec82-a185-3476-bb5c-199947f4bf2e | -7.07532 | -35.10468 | 2025-09-15 03:28:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b2739387-6b72-3d34-bd0c-bf0d32ea1c58 | -6.33769 | -43.167 | 2025-09-15 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16bf4a46-eb03-3ca2-9c9b-fe26d6eeac29 | -6.92041 | -46.17999 | 2025-09-15 03:28:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43792473-023c-3e4e-afd7-6cf7ea38025c | -5.67904 | -43.49466 | 2025-09-15 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9406ab69-acdd-3fad-a65d-ff312f2724c4 | -6.97165 | -44.54795 | 2025-09-15 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0994e78a-31c8-3de6-93a4-f455e9eb343c | -6.34337 | -43.16448 | 2025-09-15 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a1ddf0d-d601-3692-9c0a-91e34218d36c | -7.07343 | -35.1018 | 2025-09-15 03:28:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| d8965a31-f0f3-39ac-8ee5-07c64dda1e9d | -6.96401 | -44.55269 | 2025-09-15 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5f22cb1f-1ee3-32f7-b68a-956d531ab3d3 | -5.07465 | -44.10124 | 2025-09-15 03:28:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9c900ad-336d-32c9-b90f-5f3e9c5d322c | -5.1821 | -45.18064 | 2025-09-15 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c8f93d9e-fae2-3b17-bba1-26f2105286e7 | -4.17338 | -42.03463 | 2025-09-15 03:28:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8bcd1335-3fdd-3fe4-b12f-bd6f93a55706 | -5.47025 | -44.68798 | 2025-09-15 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28234efe-03d4-356b-b33a-72228e76c190 | -6.33856 | -43.16228 | 2025-09-15 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7dd9aa1-a3f3-3cb5-81a9-0501b87a48a4 | -6.41658 | -42.61073 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a1e8ca0f-2dff-3a8a-b522-a3f9e40cae6b | -5.82482 | -43.49401 | 2025-09-15 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c392f5b-e4d5-3410-b286-078e2fb83574 | -7.35951 | -44.29856 | 2025-09-15 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 009ddddd-88cc-3d87-b952-8b619dd0744a | -6.34594 | -42.53938 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0d5ef84a-b5d1-38f1-add5-37311e8795e9 | -6.91325 | -46.1786 | 2025-09-15 03:28:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00136a0e-2601-3fa9-90fa-0eece73e6a4f | -5.67279 | -43.49355 | 2025-09-15 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 810a566c-fa62-3808-a867-6371915c00b4 | -6.34252 | -43.16932 | 2025-09-15 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2724be80-319e-3f36-986f-8f3169a281ea | -6.97904 | -44.54456 | 2025-09-15 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6bcf27c7-a41d-3a61-8daa-228961d3cdae | -5.64837 | -42.60265 | 2025-09-15 03:28:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 28389a52-88c5-38d7-a1b6-1538cd0be741 | -3.34945 | -39.28115 | 2025-09-15 03:28:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce461df6-d189-3a2b-898c-6dbedc21d7cb | -4.17337 | -42.02958 | 2025-09-15 03:28:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ba96c5e-a7b8-3ad8-9465-14b8a01854b2 | -6.35077 | -42.54106 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ee3be90b-0db9-395d-9acc-2f043a0ad5d3 | -6.15242 | -41.18902 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55e7404b-9503-3461-a660-e99c86533b5f | -4.66199 | -40.55994 | 2025-09-15 03:28:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f27f3e5d-7cca-3386-b2c9-06a56f31113d | -6.15303 | -41.18557 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3d465016-9fbe-310b-b03e-34d47ac341eb | -5.46915 | -44.694 | 2025-09-15 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e0f6ea3f-a57c-3875-a937-c0bb39cdfc3b | -6.35069 | -43.16441 | 2025-09-15 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README10.md)
