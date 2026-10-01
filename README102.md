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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4d3d30b-d572-381b-b652-ec376c130fad | -8.2992 | -54.7348 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b69095b8-712b-3ddb-a319-1506c924903b | -11.411 | -43.4625 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 6dd0bb37-3fb8-368f-81c2-8bd6d748f9b5 | -12.6832 | -47.3442 | 2026-10-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d183eecc-01ab-372b-ba37-50943f7e0265 | -10.776 | -47.2411 | 2026-10-01 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f8e5fffd-344f-309f-9da6-e036728b76de | -12.3356 | -46.4028 | 2026-10-01 14:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a34ee1fc-2ef4-31d8-aded-08e1003a4d01 | -11.3931 | -43.3942 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 3356aab4-1777-377a-9a8b-6fc632ee9df3 | -6.1386 | -53.2818 | 2026-10-01 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 365a3344-2048-3dfc-8d8b-45c2e6bc0941 | -9.8803 | -44.9553 | 2026-10-01 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 265.2 |
| 39cbd5e2-4d90-3375-b20b-3a5d36c5e24a | -15.5175 | -46.1257 | 2026-10-01 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 128.9 |
| dd93f678-2a81-3e7e-a19b-3b632fb79da6 | -10.7285 | -50.5339 | 2026-10-01 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4ce8a832-b5b5-37d4-9d77-f5a0ed054663 | -12.6267 | -47.2851 | 2026-10-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 2042c4d2-0222-38e9-8461-b6d46cce55af | -8.0166 | -42.8681 | 2026-10-01 14:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| e4367a98-4bf3-3db5-81b5-c9a0328a0d31 | -12.4548 | -44.123 | 2026-10-01 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 0ee5c65d-4331-3e83-996b-398939d56864 | -5.8412 | -53.4799 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| a78c8d9e-152f-32b0-889c-20198d56b5a5 | -11.3935 | -43.3705 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 236.2 |
| ce30d0a0-d5fd-3328-aab4-6b0e91c5e0ae | -12.7413 | -47.3133 | 2026-10-01 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 01bd2f1d-b477-3a2f-bb75-1f6716b6f203 | -11.4106 | -43.4862 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 73eb1e77-14a7-375b-ae4e-68d1c376504b | -6.1949 | -53.177 | 2026-10-01 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c53913a9-4f92-3d1a-a7fe-cf32201270f0 | -10.9262 | -43.8406 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.4 |
| 416855f3-6673-3186-9d4a-05be5983988b | -7.4156 | -42.6241 | 2026-10-01 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 2f384710-5f89-393f-a5f8-534db414b2be | -11.2246 | -44.2654 | 2026-10-01 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| e591aabf-f995-352f-b121-524aaa38a8f5 | -11.6789 | -43.4921 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 78e64cab-859b-3760-9e29-23f2961ee243 | -9.7687 | -44.8082 | 2026-10-01 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| db4ca835-615b-3612-b41e-db5a4fa18dd5 | -5.9152 | -53.4762 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| d5665fe0-74ea-319d-95af-c50413216562 | -9.8067 | -44.8035 | 2026-10-01 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 17443813-7b95-32aa-b482-c74f1e9e8cea | -10.907 | -43.8433 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| a3d1727a-2d39-3be6-b1a9-3108086345e7 | -7.7219 | -54.8114 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0b465331-2d49-3748-b106-ad3786ded7f7 | -12.6455 | -47.3048 | 2026-10-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 0f1916d2-f2ec-37d2-8057-76987ccdd07e | -10.0145 | -50.2657 | 2026-10-01 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ece79796-e96e-3d89-a9a4-ecade960ad1a | -12.7024 | -47.3414 | 2026-10-01 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e3a9c340-361a-3254-8959-1041a78fcd69 | -5.9887 | -53.5538 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4ec7cc62-8699-3607-ba38-cb43a1a337f1 | -12.4355 | -44.1262 | 2026-10-01 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| b6f0f58a-d5e0-3e08-ad71-a35794e15e35 | -9.88 | -44.9783 | 2026-10-01 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 2a3e32b7-92f4-3cfb-9b37-2e3b5693eaad | -11.699 | -43.4416 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 11b28ae1-0e11-3109-b520-8332e0fcc0f0 | -11.2438 | -44.2626 | 2026-10-01 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 441.5 |
| ec0b7cc0-a44e-3956-8a3f-714e2bb6947b | -11.6977 | -43.5128 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 84d55a32-4c58-3c6e-a286-163df6f64b76 | -12.9036 | -44.8217 | 2026-10-01 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| b356bcaa-87c8-3398-b078-ac58fde7731c | -5.8411 | -53.5002 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| a0237b76-d1b6-34ef-8d2a-4d1df403c4d2 | -12.4346 | -44.1733 | 2026-10-01 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 8be2beb5-4e8f-3088-a86e-56bac887b6fd | -8.3397 | -44.1658 | 2026-10-01 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 4bd9452c-3d0f-3703-b33b-1eb02966d07e | -10.2827 | -49.9606 | 2026-10-01 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| aced0947-54b6-3b76-a0fe-a67a6b298d8d | -11.2282 | -45.1682 | 2026-10-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 301e15c6-ba8a-363b-8d4b-2da637a22983 | -7.3965 | -42.6498 | 2026-10-01 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| cded1d68-c264-3451-9e30-3314cbb0687c | -11.4298 | -43.4833 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 18dc007d-01dc-3f40-84a3-4aa26f3bf6da | -11.6207 | -43.5248 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 0ef12eb3-082b-3a8a-9f56-d4a64cb85e5d | -14.5458 | -40.8417 | 2026-10-01 14:20:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 167.3 |
| 7ef66c15-0fd3-3cab-8d3f-934e0079588e | -9.9956 | -50.2675 | 2026-10-01 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b44489ae-4573-30bc-9b98-ec3f0e26f641 | -8.1212 | -43.5382 | 2026-10-01 14:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a70c47f0-511f-374d-9716-98be7bcf4285 | -8.6268 | -45.3054 | 2026-10-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 32ac43a5-2968-3151-a9a5-d31cee71d04c | -12.4539 | -44.1702 | 2026-10-01 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 362.0 |
| a8628be6-7ce9-3962-bfff-b6f8d82ef205 | -9.825 | -44.8472 | 2026-10-01 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 421.8 |
| 56bc2020-32ea-3d3e-8d39-252c569353ee | -9.8064 | -44.8265 | 2026-10-01 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 653.8 |
| e851502e-75eb-331d-9b2a-f9339dbdd7df | -12.3163 | -46.4056 | 2026-10-01 14:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 79c8c73b-7522-3e3a-9805-dffc1be6d6f6 | -11.1236 | -44.5823 | 2026-10-01 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 292.1 |
| 20629fdf-a2c3-3adb-b575-e61fb2def028 | -14.377 | -44.7534 | 2026-10-01 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 38e5dab5-f85d-3eec-83f1-1684dd2fb9f1 | -6.3665 | -55.1461 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| ef4e1dc7-d364-3392-b447-3faa10244a3e | -11.6784 | -43.5158 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 647f7cd0-4e9e-3497-bd91-36379c04ee4a | -14.3574 | -44.7569 | 2026-10-01 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 266.1 |
| f0c46724-0f3c-34cb-8627-509ee4042d5f | -14.659 | -41.0175 | 2026-10-01 14:20:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 19009156-3ac3-38bf-9d88-7bd9c14eff78 | -8.1684 | -54.7836 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c3a69227-0001-30d1-bac0-b5c34257e874 | -10.2637 | -49.9626 | 2026-10-01 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| aa260544-f9ba-3cbd-991e-87218e0990aa | -11.7187 | -43.4148 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| bd22ebd3-febf-334f-b4d4-11392c193b36 | -8.2619 | -54.7372 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d435b562-a28d-3cfe-87f7-6a08464a6d44 | -12.4544 | -44.1466 | 2026-10-01 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 7f557ab7-6d79-3428-b3b0-e06fc83cb649 | -10.2067 | -49.9898 | 2026-10-01 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9e48e323-e0cd-30de-a1e4-4f529709504b | -7.7221 | -54.7913 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 3475ef67-9eed-3cc6-b50e-010fa1853cdc | -11.4294 | -43.507 | 2026-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 675.9 |
| 7de0dae1-cb07-30f9-8b96-177c3ec5291c | -10.0148 | -50.2443 | 2026-10-01 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6172416b-b310-344b-9960-344a4ed8272f | -11.2278 | -45.1913 | 2026-10-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| fce77930-0456-3935-9cf9-2c055e22f11e | -10.1881 | -49.9703 | 2026-10-01 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 5af81a08-5ee6-3deb-ba4e-91d3fe3c386a | -8.1874 | -54.742 | 2026-10-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| ad9642f5-2a15-333c-8352-a32138c982c4 | -7.3967 | -42.6261 | 2026-10-01 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 0851495b-8e2b-3457-8942-60d9ca10efed | -13.3267 | -43.9523 | 2026-10-01 14:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 9f30686a-9167-32cf-a997-346157628c56 | -11.6977 | -43.5128 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 224.3 |
| b2d27c0d-a11c-3232-8b37-860b2a90fa5f | -10.2067 | -49.9898 | 2026-10-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| c4da2c04-c9b2-381f-858b-2728e3281393 | -12.6836 | -47.3217 | 2026-10-01 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| e4af58c3-8ec9-37b6-a6f7-db162c15b57e | -11.6981 | -43.4891 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 8d1d5c0b-9d20-325c-9e8d-63847e7bd202 | -11.4294 | -43.507 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 322.7 |
| a9391246-a336-3200-83d0-21342ca254a7 | -16.9909 | -45.4594 | 2026-10-01 14:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e8c84f6b-597e-3ee5-b25d-19fe36da0213 | -11.2438 | -44.2626 | 2026-10-01 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 209.1 |
| 27302a29-de1d-314a-bf79-f1406cf4790c | -11.1236 | -44.5823 | 2026-10-01 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 519.5 |
| cdcbf11e-452e-3f52-8e9b-c5e0c6e2c876 | -9.5087 | -45.7525 | 2026-10-01 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| ed48aad6-9d5f-385e-b5cc-9a5ee0190cd0 | -11.4298 | -43.4833 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 774fc67a-1b9e-3af0-9f70-1816fa45c9e2 | -15.6934 | -40.5804 | 2026-10-01 14:30:00 | GOES-19 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| 6f6c002e-fbbb-3899-9506-631bd26cb5a8 | -12.4539 | -44.1702 | 2026-10-01 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 556.3 |
| 1304278f-b512-33a4-b092-d7714c8b7222 | -11.2282 | -45.1682 | 2026-10-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| e2c3f542-5aad-356c-9660-963b464e5656 | -12.4351 | -44.1497 | 2026-10-01 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 0acdb419-b098-3987-8ef3-5b78f32915c2 | -5.8412 | -53.4799 | 2026-10-01 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| d0d990f0-c6f4-3f31-8cf1-198661add814 | -12.4535 | -44.1937 | 2026-10-01 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 287.1 |
| 5bbcb6a8-4a6c-310c-83aa-854bb7f33106 | -9.0783 | -49.8853 | 2026-10-01 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| de2b6b6c-2faa-32ed-beb7-39e99e041b3b | -12.7221 | -47.3161 | 2026-10-01 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| b09260f7-086c-3554-98ce-4d5bc50f6182 | -9.7877 | -44.8058 | 2026-10-01 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 355d584e-04f6-3017-89f7-ed2f00350367 | -11.3931 | -43.3942 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.9 |
| b1662a99-90ac-3349-8596-adf74d8ff26a | -11.2278 | -45.1913 | 2026-10-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 60f972aa-a53e-3566-8b28-f039fe02290d | -11.6207 | -43.5248 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.5 |
| d6d4f0c3-030c-3c93-a503-40db944f7bb4 | -8.1684 | -54.7836 | 2026-10-01 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 3bd4bdd3-3837-3768-9969-c3954fa3f450 | -6.3666 | -55.1261 | 2026-10-01 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 138abfab-0a1c-359d-8b7f-5eaa03d074c7 | -7.4156 | -42.6241 | 2026-10-01 14:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 22d91db7-36f3-3aa2-a201-bfed0e636702 | -12.904 | -44.7984 | 2026-10-01 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 522e6b1d-0636-33fd-b42e-1aa2d7a139fe | 1.7115 | -55.9221 | 2026-10-01 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |


[Clique aqui para ver as próximas entradas](README103.md)
