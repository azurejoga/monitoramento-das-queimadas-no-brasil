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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3575911-bae9-3b31-9ddc-1eee4c60d891 | -11.373 | -43.4446 | 2026-09-28 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| df34293c-3cc4-392e-8620-5712a71cdb3d | -9.1871 | -45.7663 | 2026-09-28 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| b2a2856b-6f7e-36b5-8978-53ad7b246a9e | -11.1966 | -44.7805 | 2026-09-28 14:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 991.8 |
| 3476be7d-689c-38f4-93a5-913580f26c4b | -11.1771 | -44.8064 | 2026-09-28 14:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1163.6 |
| ff564822-59b2-3e10-8285-d3502f9a6e81 | -12.1866 | -50.7767 | 2026-09-28 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| ee990057-d38f-323e-b563-9bb5e89494a6 | -13.4325 | -57.061 | 2026-09-28 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 85aff765-6c69-3989-93b4-1a51c8bffaa7 | -20.1966 | -48.5773 | 2026-09-28 14:50:00 | GOES-19 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 718ec5a8-9b91-34f2-a31d-77ea97b92e8e | -12.6451 | -47.3272 | 2026-09-28 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 0afd8ff4-c712-39a2-90f9-db2c272d406e | -11.7316 | -50.6587 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| e4ee57b3-23ce-37cd-8c76-c75d5164cc5c | -10.2827 | -49.9606 | 2026-09-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 267c4abf-2791-314b-a589-5551b749cdf6 | -10.8106 | -48.7355 | 2026-09-28 14:50:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 6c1921a2-08c4-330c-8539-178d7717842d | -11.8856 | -50.534 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 52ddcc38-6eda-32f8-8d6b-0144518ab0ad | -11.8665 | -50.5362 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 28606bb1-1015-39bd-8003-01adb203f2ab | -10.6928 | -60.7322 | 2026-09-28 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| f3c9e7e4-d9c1-3d77-812a-e284cb135b0b | -13.161 | -48.5437 | 2026-09-28 14:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 4fc8fd8e-2cc7-3e80-80a1-8d9f1ddd7afd | -11.8662 | -50.5576 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| aaf222d3-dbbd-3339-a4bd-b70a8a8b2875 | -11.3436 | -54.1086 | 2026-09-28 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 2bf6a2a5-4f02-346b-94a2-5bce8c920b07 | -11.905 | -50.5103 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7811204d-0a2a-315c-8295-0c4614095da8 | -15.4003 | -47.9035 | 2026-09-28 14:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 25d2df94-2e07-39ee-bdbd-744daf2cfda7 | -10.0164 | -50.116 | 2026-09-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| bb6f3377-e629-3891-981a-475cd7cdf881 | -11.2307 | -54.078 | 2026-09-28 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 8137f517-0f9a-3c65-93a8-31d540ea5011 | -12.6836 | -47.3217 | 2026-09-28 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| ed78b7fa-85b4-3c14-a625-d91ecc42ac1e | -11.6945 | -50.5988 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 0cab0c45-05b2-3d82-b9a2-8950d3b2656a | -6.1599 | -52.8929 | 2026-09-28 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 55e3c4d3-969a-3aec-902c-d49c79d23c5e | -10.7114 | -60.7505 | 2026-09-28 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 7bcffc90-2778-3d47-a3de-dd149b451c5e | -10.6035 | -49.9913 | 2026-09-28 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 09b8c571-405c-3c3a-a196-a04391693c41 | -11.0424 | -54.0336 | 2026-09-28 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f958a9d4-0bc3-3164-b3f5-2cc5f2779008 | -7.5057 | -44.5733 | 2026-09-28 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 235.1 |
| 25598ea7-d0a8-307c-890c-6ce67dff67e5 | -11.5352 | -47.3678 | 2026-09-28 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| d57e4d03-72a0-3090-abf6-056bf40c26f1 | -12.2257 | -50.7079 | 2026-09-28 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 133c2c12-ba00-37e9-9f63-654e786ed84a | -11.7828 | -51.0578 | 2026-09-28 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 62cf6289-37a3-311e-a5e0-bb6f6bddd39d | -9.1337 | -49.9656 | 2026-09-28 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| b761215e-01d4-3e31-8121-4b53265d479b | -8.2293 | -45.4375 | 2026-09-28 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| fc7fc7a9-9b08-3471-80d3-a9c1515e82c9 | -12.2057 | -50.7745 | 2026-09-28 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| b97b9609-4bd5-336f-b62b-831cdc9534fe | -11.0241 | -49.7088 | 2026-09-28 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 3a2c35d5-8649-3a65-a385-2c4b4e87d634 | -11.497 | -47.3727 | 2026-09-28 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 3ad25000-1eec-32d6-b06d-54e2ec2b1d74 | -12.8658 | -44.7813 | 2026-09-28 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| c3d53da3-a2cd-305a-aeb8-9d98ded27d0c | -11.0241 | -49.7088 | 2026-09-28 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| c94145f5-e60d-382b-9df3-4d053ab72431 | 3.7503 | -60.2972 | 2026-09-28 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| ab83aeec-123d-3cb0-9b27-14460fb90c82 | -7.7037 | -54.7722 | 2026-09-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| a0c675c0-bdf0-3dfc-a4e9-b0fe33ca4750 | -10.8723 | -54.0694 | 2026-09-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 081260e8-09af-3646-8850-9ac5dc45e762 | -9.1057 | -60.9511 | 2026-09-28 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 26c5ea3b-4837-3b93-85fd-bed8e1a0f778 | -11.9593 | -50.6965 | 2026-09-28 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3f3eb6fb-fdb3-33dd-aedc-297837965682 | -10.6505 | -50.7123 | 2026-09-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 92ace419-c590-3334-a43a-9ad35bd92d4d | 1.6381 | -56.0411 | 2026-09-28 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 248f8406-1076-38d1-b4c2-f5cd25bd7c75 | 2.1266 | -50.8788 | 2026-09-28 15:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8b3072fe-5945-36c2-b961-4b78a03bef51 | -15.1847 | -46.141 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 111.7 |
| a7248b7c-9775-311a-b13b-7cd570da49b4 | -12.3088 | -50.2688 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 94c310f1-0517-37bc-90ff-8e60c6feb73b | -13.1803 | -48.5409 | 2026-09-28 15:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 12c338b0-5d8b-3108-a965-7848904a1299 | -11.3743 | -43.3734 | 2026-09-28 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| b51fdd0e-b929-311a-a7d0-74c892cc96af | -16.3585 | -41.6045 | 2026-09-28 15:00:00 | GOES-19 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.5 |
| 7b9ec1dd-d1cf-3df0-99d1-4057f99b810e | -10.9861 | -49.7131 | 2026-09-28 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| b8aefe8b-3427-3fdb-9426-be1126a24208 | -11.8824 | -50.7481 | 2026-09-28 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 81f607b1-e079-3134-af5c-3292f378c795 | -16.6424 | -48.4724 | 2026-09-28 15:00:00 | GOES-19 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 357e3e1f-6561-3872-859f-0bb59f49559a | -1.3008 | -49.0613 | 2026-09-28 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 45a00d4a-f2a6-3c3a-838e-c9d6892fa18f | -10.0164 | -50.116 | 2026-09-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| db63dd22-48d3-3a4f-a990-9be933c5c1c7 | -10.6928 | -60.7322 | 2026-09-28 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 410bf97c-95ef-3699-adeb-0b4756ec2986 | -10.9349 | -50.6612 | 2026-09-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 394fe915-306a-3ace-b5ae-b31a516ba8e7 | -11.8669 | -50.5147 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 0ec8d30c-426b-35a1-bbc8-69bedebcee13 | -11.7837 | -50.9939 | 2026-09-28 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 86d6ed5b-0c36-3218-b6d0-56e080ed8f15 | -15.3998 | -47.9261 | 2026-09-28 15:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 130ddee3-316d-3a2f-bb13-8a66eea04d7e | -10.6035 | -49.9913 | 2026-09-28 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| d28ac562-213c-3442-8e14-89824f9c85f9 | -1.0976 | -49.2127 | 2026-09-28 15:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 6c13f3d4-48d3-3e7c-b495-a6213157ad71 | -9.1337 | -49.9656 | 2026-09-28 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c1679ff5-00cf-3414-9fc7-ddf03aa304db | -9.206 | -45.7642 | 2026-09-28 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 400.9 |
| 05c079a6-b136-32ee-8cdd-c7d3b61e0ce1 | -11.3739 | -43.3972 | 2026-09-28 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 0fdd2abd-616e-301f-a2c9-3220ffbfcc31 | -10.8967 | -50.6866 | 2026-09-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| f0469323-4a01-3650-bc38-8d9ee7c95ccd | -10.2065 | -50.0113 | 2026-09-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 379.5 |
| 34bf7612-38bf-3833-add4-1fc3a1b1df1e | -10.7343 | -48.7661 | 2026-09-28 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 484fc4c0-1515-37bb-88e1-ab4cf97556c2 | -9.9266 | -60.7171 | 2026-09-28 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 33037aeb-047f-3b23-85a6-f54c8ec67d32 | 1.6383 | -55.9033 | 2026-09-28 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f07c4197-0bb7-309a-a1f4-4cd5bf684c06 | -10.8185 | -57.2391 | 2026-09-28 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2554e541-3a51-37be-8970-3b003464d85a | -11.6186 | -50.5861 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 8a5b784f-6826-3c53-821e-65bfc5f09541 | -11.7834 | -51.0152 | 2026-09-28 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 90d8d132-16a3-3cda-a6d5-2e354b1f9212 | -12.8513 | -50.9957 | 2026-09-28 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 492ec4ae-97d5-3716-a041-92b3b7aa5c41 | -12.4351 | -44.1497 | 2026-09-28 15:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 3dbb8161-876b-32f5-8449-ac075af33183 | -12.6271 | -47.2626 | 2026-09-28 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 0c09a8ad-652d-322d-bc62-fdd773886757 | -11.9968 | -50.7349 | 2026-09-28 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 89894753-fc03-3c31-8905-6c119593edc9 | -11.497 | -47.3727 | 2026-09-28 15:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| d49abbf7-aec4-3373-b5ac-f18f716c584f | -12.6643 | -47.3245 | 2026-09-28 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 58dd038d-2a37-3d44-806c-c69b729dffdd | -7.5057 | -44.5733 | 2026-09-28 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 374.0 |
| fd121fcf-888c-33d8-8ef5-e1503843021c | -15.0984 | -54.7189 | 2026-09-28 15:00:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 5f85ab32-7b07-333e-8188-c6cc268714e7 | 1.6748 | -56.021 | 2026-09-28 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| e8b2b267-1070-3886-8c81-9d2c44521a03 | -7.6264 | -45.5186 | 2026-09-28 15:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7c5282c1-d8a7-336a-af60-41af21201f2d | -10.8191 | -57.1795 | 2026-09-28 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a0e4c806-a6ca-34a0-8691-7eac5e77fe4b | -12.2123 | -50.3451 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7e080a99-8fb4-379e-aab4-e2f7b3db4d37 | -7.6852 | -54.7532 | 2026-09-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fbd4a32a-958e-3260-87d8-2c224de67cd9 | -11.0424 | -54.0336 | 2026-09-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f17e796c-760b-35cf-a68c-3a85c2aaca74 | -11.0422 | -54.0542 | 2026-09-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 53905936-8777-3e78-b348-5b90eccdb030 | -10.6889 | -50.6658 | 2026-09-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 9dd5e95f-48d1-3c46-b351-7fc2b061e6a3 | -11.1966 | -44.7805 | 2026-09-28 15:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 860.3 |
| c036b840-57c9-34cc-a200-0f4be7f0646b | -11.5352 | -47.3678 | 2026-09-28 15:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| b93a59fe-23b2-3f1b-b592-6d7a0898d1b8 | -12.2257 | -50.7079 | 2026-09-28 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e420cd8b-d1e5-382d-bec7-2c76821a00e8 | -13.3272 | -43.9285 | 2026-09-28 15:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 201.1 |
| b571f57d-9fff-3038-9315-8de385967d36 | -10.9346 | -50.6825 | 2026-09-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9673a15d-2d5f-361a-88a2-16b1c0b9ac09 | -11.8856 | -50.534 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| beadbd92-3643-3281-8850-21120b691a1b | -8.0708 | -55.3321 | 2026-09-28 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 344866a6-7504-3b95-aafe-4e66f06844a7 | -11.0991 | -54.0285 | 2026-09-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| dfe63ce1-5f52-3e30-bdea-d5c66e867f27 | -11.0235 | -54.0354 | 2026-09-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 481deb06-30c0-3b5a-b1d7-805571f7ac39 | -10.7064 | -44.4317 | 2026-09-28 15:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |


[Clique aqui para ver as próximas entradas](README83.md)
