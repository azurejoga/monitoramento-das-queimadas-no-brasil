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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1ec0edb-5f97-37f9-a22b-3ae05897c9fa | -11.0953 | -51.3866 | 2025-09-13 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 132a75ca-ed87-3ca5-a484-690f14a1b355 | -17.4346 | -49.2258 | 2025-09-13 13:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 6db5b987-9925-3fef-bef1-211e707b5a81 | -10.8785 | -45.5597 | 2025-09-13 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 57504e91-6c16-3683-9a7d-6d69d2659037 | -17.1549 | -48.4908 | 2025-09-13 13:30:00 | GOES-19 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 362d176a-d35f-37eb-abe5-e5850a8fbb61 | -10.3701 | -50.4857 | 2025-09-13 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d57289b3-c74e-39ff-a329-cbec52fb4d36 | -12.8644 | -47.9432 | 2025-09-13 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d2e731e8-162a-3167-9354-da05c0508a55 | -10.8976 | -45.5572 | 2025-09-13 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 0fc8bda1-e3ae-3190-9d01-eebb2490ae8a | -10.7664 | -50.5299 | 2025-09-13 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 9da41463-fde9-3335-9b77-36475ced1ad0 | -14.4584 | -47.34 | 2025-09-13 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 51722eb3-0987-3483-87b7-4357f1f259b8 | -18.0071 | -46.9266 | 2025-09-13 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 80.8 |
| da28f79a-731f-3985-9dda-3f04c7ba7084 | -14.31 | -46.066 | 2025-09-13 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 124d6828-14cf-357b-8d5d-004c2f38cf57 | -15.4713 | -47.3256 | 2025-09-13 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 110.8 |
| b7bd6295-b8c2-38db-9851-ebaf33f6f353 | -11.7826 | -47.402 | 2025-09-13 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 18c484ae-0ef1-397d-9156-e3a6a113f0b8 | -10.8972 | -45.58 | 2025-09-13 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 40a0b41e-d37b-3c37-9798-f44f82b6d040 | -14.4199 | -47.3238 | 2025-09-13 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| f7d71f3e-0b06-3e45-b67b-b609a6ce2c3b | -12.9595 | -47.9963 | 2025-09-13 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 663ff694-a2e7-3702-b223-00aff762bc0e | -16.3422 | -51.5217 | 2025-09-13 13:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 133.3 |
| e3167b86-251b-3e2e-a0eb-21d1d599d9d2 | -12.9398 | -48.0213 | 2025-09-13 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 48117475-cf60-373f-bc05-518f0de275fc | -10.8567 | -48.1827 | 2025-09-13 13:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 134895ef-4c64-31c3-8469-8fec5ba960aa | -12.1236 | -47.579 | 2025-09-13 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 67ec09d2-496b-359f-b194-8f05050dc99b | -18.0466 | -45.418 | 2025-09-13 13:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| b5dd4f6f-8e17-391f-891b-2235396d02bb | -12.5787 | -45.7051 | 2025-09-13 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 319.5 |
| da4e4910-2e66-3330-b60d-1ae96fa61171 | -18.0065 | -46.9499 | 2025-09-13 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 96.6 |
| c936ab2f-1e30-343f-94f1-c882f85b0aab | -13.8979 | -48.2804 | 2025-09-13 13:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 32336687-565a-33b6-b79a-05846e9a6045 | -13.9172 | -48.2775 | 2025-09-13 13:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7fb28edc-5126-3883-bb1f-5d5ea9a382b2 | -8.19 | -45.5774 | 2025-09-13 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 877be320-4ac1-3bf2-b4f8-31d5f3a79213 | -10.7661 | -50.5513 | 2025-09-13 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c6582ae1-934c-35f1-a446-ff32b77cf6b1 | -13.9185 | -48.2105 | 2025-09-13 13:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 7baa5356-5311-305c-b9db-358b468f5b39 | -14.4588 | -47.3174 | 2025-09-13 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 499c2372-a2e3-3c97-8a9d-01552a48f5f8 | -12.1232 | -47.6013 | 2025-09-13 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| c7404c33-c20f-31de-a685-0194ee1994b1 | -11.3835 | -47.3206 | 2025-09-13 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| fd623adf-f914-3f9f-abe8-db664e7d938b | -7.3954 | -44.3539 | 2025-09-13 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| fa7f01b4-ba31-392e-8c7b-6b06a2946a34 | -15.4517 | -47.3291 | 2025-09-13 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 479f7483-1762-3492-bb4c-47b23798e2b9 | -12.5979 | -45.7021 | 2025-09-13 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 260.7 |
| 0bf2320d-48d8-3b7c-b630-80fb404196df | -11.7903 | -50.545 | 2025-09-13 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 92c8b56e-51aa-3209-bffc-b1eede233211 | -11.1152 | -51.3211 | 2025-09-13 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 638d5286-467d-3035-8076-14795f7d49e0 | -10.7472 | -50.5533 | 2025-09-13 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| fdbd4619-13f6-376d-a666-32630a49a071 | -12.1044 | -47.5816 | 2025-09-13 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 81942112-20c4-3fed-b695-f129fc739ed8 | -12.9591 | -48.0186 | 2025-09-13 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| a4c0c309-f6c6-3331-b5eb-f249e8f5d9b5 | -14.1917 | -46.1552 | 2025-09-13 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 7a80793a-2854-3666-9b61-a1a78ef11282 | -15.1601 | -50.1379 | 2025-09-13 13:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 7deef5a6-6ae7-3723-8b4f-5bcacc954022 | -15.1546 | -52.5291 | 2025-09-13 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| fa4393a4-5ccd-35e3-831d-5e7ab2c304e6 | -10.8785 | -45.5597 | 2025-09-13 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| b803a6db-5fd8-3b17-a7da-85344b1cfd0c | -16.2925 | -50.1121 | 2025-09-13 13:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| c56dc811-560f-352e-a44d-14847ba85be5 | -15.0436 | -50.1337 | 2025-09-13 13:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 40ef056f-dcc7-3dfd-be1f-5f7ec7b31fc2 | -17.4346 | -49.2258 | 2025-09-13 13:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 3f13be95-416e-34f7-b308-4384c543214a | -12.8452 | -47.9459 | 2025-09-13 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 75b0dcba-00bf-3498-9f0a-80255d881b94 | -14.4204 | -47.3011 | 2025-09-13 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1b9069b2-5770-31b2-873d-591cd3a71231 | -12.9591 | -48.0186 | 2025-09-13 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a71af871-709d-3e8f-b549-f6a8583d3fc7 | -10.7664 | -50.5299 | 2025-09-13 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f7f9e3f4-5eee-3537-aa11-4eee14df43f0 | -11.7826 | -47.402 | 2025-09-13 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 5138a5d9-c0c9-3a98-ac0b-b0eb5d0eff7c | -12.1236 | -47.579 | 2025-09-13 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 215.4 |
| 9b9be3ca-5b01-3c1d-af4c-8f3722a42c64 | -10.8972 | -45.58 | 2025-09-13 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 8449dff7-a5d9-3d5f-9240-49dcd9b17d48 | -15.1748 | -52.4839 | 2025-09-13 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 285.3 |
| df6cb98e-5339-35fd-8558-721b0a373ab1 | -12.8259 | -47.9486 | 2025-09-13 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 2090b191-15e7-3202-8a44-757bcbeb715b | -10.8781 | -45.5826 | 2025-09-13 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 33b28086-8d7b-31e9-a31a-e5abe65ecd3c | -10.3699 | -50.507 | 2025-09-13 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8f08e6dc-0aab-3ef2-aade-bf9832619755 | -10.7661 | -50.5513 | 2025-09-13 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 63ddd565-da96-398a-8420-dcc6c8f724a4 | -12.9402 | -47.9991 | 2025-09-13 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 91741310-8ca1-3221-9e74-b8ff52a8a638 | -12.1044 | -47.5816 | 2025-09-13 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 0c665112-0516-3f1a-853f-43967371cb1c | -14.2088 | -46.2669 | 2025-09-13 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 148.8 |
| f93e95d1-9777-3549-b703-fb4027792728 | -12.8263 | -47.9263 | 2025-09-13 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 82a7164e-65f3-3bdb-ad8f-260abf68857b | -19.3508 | -44.798 | 2025-09-13 13:40:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 66b3c8c7-79ce-341c-b331-4230931680b6 | -11.2882 | -51.1334 | 2025-09-13 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 003b8131-6562-357f-bdb5-b6558d062616 | -11.7208 | -46.5353 | 2025-09-13 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 262558b2-28c3-336f-b844-de8acf825d8b | -14.4588 | -47.3174 | 2025-09-13 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 839988fc-e0e9-3d10-98a3-a6c7a5dd9809 | -15.1363 | -52.4679 | 2025-09-13 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| f4e8dd94-4538-3008-9b34-0222cccf402c | -9.5324 | -54.6277 | 2025-09-13 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| b619fb53-2c36-3d14-bbeb-f6edb8df10aa | -9.5004 | -55.9788 | 2025-09-13 13:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 195.2 |
| 1dd22d7f-0a4f-317a-acbc-f90f86316fd9 | -11.1893 | -51.4401 | 2025-09-13 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| a80cd98b-9d8b-36f5-8425-3d080a1f6d7f | -16.6532 | -49.7649 | 2025-09-13 13:40:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f1546faf-41e3-3c9d-a028-e11d83d158e5 | -10.7472 | -50.5533 | 2025-09-13 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 25213f93-2b71-3222-86e5-95fccbfe2423 | -17.4142 | -49.2519 | 2025-09-13 13:40:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| dce2b1e1-53bc-3cd6-82ac-a9d7a791d6f1 | -10.3701 | -50.4857 | 2025-09-13 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 94755fc9-6372-3831-9895-9750dc7eb86e | -12.8456 | -47.9236 | 2025-09-13 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 641c6c86-1350-3fa0-8627-001f47eae7a4 | -11.8698 | -46.7627 | 2025-09-13 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| df3707f3-72d5-3e7c-8d3f-6bd5faf9a1f1 | -14.31 | -46.066 | 2025-09-13 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 12939c4d-7d90-3f55-a0e2-6615ea207400 | -13.2535 | -43.752 | 2025-09-13 13:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| b986ac74-8e3e-3cf5-9936-7138ff1cf60c | -15.1169 | -52.4705 | 2025-09-13 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 057a2d97-a9a7-3a2a-8e3f-6ab20062a6e2 | -10.7474 | -50.5319 | 2025-09-13 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| b290e1cb-bfe1-31ac-9010-646f511fdd08 | -12.9294 | -54.7333 | 2025-09-13 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 18296451-d0c1-3002-a86e-269da155aaeb | -10.8567 | -48.1827 | 2025-09-13 13:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 8600b40b-c96d-3c32-8a47-0242c296b59b | -16.4906 | -55.1276 | 2025-09-13 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 5c137fd7-2560-3f94-915f-76a389997b40 | -11.1896 | -51.419 | 2025-09-13 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 24649c38-0d79-3d75-9c4b-d6fb5daa0ce9 | -13.203 | -51.7406 | 2025-09-13 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 453d4f4f-3fd5-3674-805c-f401e1b9ab55 | -10.8757 | -48.1804 | 2025-09-13 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5112ec4f-3a43-39ec-8f68-a9952e80eeef | -7.3954 | -44.3539 | 2025-09-13 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 37270426-8dc3-30dc-85d2-51441374d306 | -15.4517 | -47.3291 | 2025-09-13 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 9aa0e1e3-57bf-372c-a91a-e2750f581728 | -13.937 | -48.2522 | 2025-09-13 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e935bb7c-d444-3260-8dac-73682e760952 | -15.8648 | -47.2322 | 2025-09-13 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| abacea46-699e-3514-a5ea-bb963216e705 | -13.9379 | -48.2076 | 2025-09-13 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c901ee7c-7941-3f4d-bd49-ef9068955a86 | -7.2131 | -43.8396 | 2025-09-13 13:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d5d1955f-b3a8-3a49-856f-1a6be3ad6bed | -14.4398 | -47.2979 | 2025-09-13 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 7281b33a-64c6-3f59-bb4d-7fc4bc328266 | -15.8845 | -47.2286 | 2025-09-13 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 9da94379-fe00-3628-8c14-e4f29254013b | -14.1917 | -46.1552 | 2025-09-13 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 84330233-13a4-3c5d-8e81-de33b577dd70 | -14.3095 | -46.089 | 2025-09-13 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 887ecca0-240b-3df3-bc73-34e67a4d4d8a | -12.9398 | -48.0213 | 2025-09-13 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 78d15091-7a43-3257-9c48-b1243928435b | -11.1066 | -51.9538 | 2025-09-13 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 2d93b8fb-628a-37a3-a750-45bdbacf7700 | -18.0071 | -46.9266 | 2025-09-13 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 5199b491-2e54-3842-a740-b4c0d980f950 | -16.3422 | -51.5217 | 2025-09-13 13:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 131.8 |


[Clique aqui para ver as próximas entradas](README129.md)
