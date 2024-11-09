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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8336d01a-313f-3423-a14c-3ebcc1cb53e7 | -4.2486 | -47.5729 | 2024-11-09 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 172fc0af-e76d-3c03-a70b-7cc6ea367a2d | -3.5818 | -47.3621 | 2024-11-09 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f6dd54c6-c0e7-39f0-91ed-e64453a88eb9 | -11.0881 | -43.3219 | 2024-11-09 04:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 730acb9a-a9cd-3b86-aac0-6aed90180c20 | -23.89697 | -54.05291 | 2024-11-09 04:40:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f1cabfd8-5051-3e7f-acb1-fd5f411ac749 | -23.88609 | -54.05489 | 2024-11-09 04:40:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6312fc47-4849-3176-a9c4-4829a33db499 | -23.88882 | -54.05956 | 2024-11-09 04:40:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e9edad9c-fd7a-3009-8270-402e9f8597f7 | -23.90856 | -54.06761 | 2024-11-09 04:40:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| b85b8b53-35af-3a4e-b4aa-98a1f87bf1d5 | -23.9099 | -54.05961 | 2024-11-09 04:40:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6fcef1d3-92dd-34d5-af95-6306e5d3deb1 | -28.38442 | -52.70657 | 2024-11-09 04:40:00 | NOAA-21 | SANTO ANTÔNIO DO PLANALTO | RIO GRANDE DO SUL | Brasil | 4317756 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6b6b45c0-a8b4-360d-ac1a-a51be566749d | -23.89563 | -54.06091 | 2024-11-09 04:40:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6598fd24-3230-356f-bbf5-40744f0ea31b | -29.87531 | -51.15596 | 2024-11-09 04:40:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 80b17cb2-2999-3bc5-95f4-aeb4df033d40 | -23.88269 | -54.05421 | 2024-11-09 04:40:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1e40304f-f882-3703-9e83-1a670fa56691 | -27.97797 | -50.6813 | 2024-11-09 04:40:00 | NOAA-21 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d3a16f5a-3c20-3700-95bf-e7e2c8b6115c | -23.91331 | -54.06029 | 2024-11-09 04:40:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8121e8f7-d985-3a1f-a8d2-bf552a0e0d1a | -23.89903 | -54.06158 | 2024-11-09 04:40:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cd7308bd-54a2-35da-b5b3-4a3cd57d6eb6 | -23.88542 | -54.05888 | 2024-11-09 04:40:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5f9e86de-f89d-3463-a94f-a0ce77f789c7 | -11.1068 | -43.3428 | 2024-11-09 04:50:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 073ec924-d0e9-3180-a8d6-c3944cd1fc95 | -3.0865 | -50.5625 | 2024-11-09 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 07fd7d69-f626-344e-a682-55a6ae3cfb76 | -1.5163 | -52.1901 | 2024-11-09 04:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| eae0522a-604b-3358-a394-b95d3eb1e1d9 | -3.5818 | -47.3621 | 2024-11-09 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a7eb599b-20aa-30b8-9a29-6aa3079d040b | -4.2484 | -47.5947 | 2024-11-09 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 51213ea3-2e3f-3d61-8b60-384d491c1237 | -11.0877 | -43.3456 | 2024-11-09 04:50:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 2d14f04f-542c-3770-b61d-c5337ac61def | -4.2671 | -47.572 | 2024-11-09 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3fbf72a8-a2fb-3cb8-af84-778be3360a16 | -3.9854 | -48.1708 | 2024-11-09 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| cc9f99e0-7d46-38e3-8701-ed71674e4be4 | -4.2486 | -47.5729 | 2024-11-09 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 3eff8758-3ea1-39b0-9e73-c87d9308d8a2 | -3.9668 | -48.1932 | 2024-11-09 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| fff55bad-f954-37e4-873d-c4e051265b98 | -11.0881 | -43.3219 | 2024-11-09 04:50:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| e8212123-5f32-3e96-8591-fc3434cb9e69 | -3.6004 | -47.3395 | 2024-11-09 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| d9376f1f-0b20-33e8-8f3b-5db055e4b9b9 | -3.9853 | -48.1924 | 2024-11-09 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ef561985-be2b-3cb7-952f-dcc447d4fe58 | -3.9669 | -48.1716 | 2024-11-09 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 886321ac-211e-33ed-b002-8cf09440f94b | -3.5819 | -47.3403 | 2024-11-09 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| e6590e74-e122-3a5b-adba-6d6add5e1769 | -3.6003 | -47.3614 | 2024-11-09 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 11a2b79f-e69d-33bf-93fd-fba77e405c30 | -3.1511 | -52.9731 | 2024-11-09 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 127c8dc2-e313-3d39-a697-3987ea7a2fad | -4.2058 | -48.5491 | 2024-11-09 04:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d3f10bc8-9784-3762-baa3-1d0524b4ced4 | 3.36874 | -51.27376 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5c06ecfd-db85-3e68-92c7-83ece988815d | 1.30675 | -50.73205 | 2024-11-09 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57ed1e87-b8e8-3687-88d3-b22a5fad8e87 | 1.30446 | -50.71751 | 2024-11-09 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 070fc709-fc42-3273-a2c3-094849733960 | 2.10235 | -50.85965 | 2024-11-09 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4e9f3cd-4650-3a07-a632-2e4c92625812 | 2.10291 | -50.86322 | 2024-11-09 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fb097e0-636e-3170-81c8-ce3035c3073c | 3.74533 | -51.62241 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7d51158-675a-35c8-9695-35e2a3e28b0a | 3.52552 | -51.43396 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbe4364f-7b5e-33fc-8e52-6cbc892d1352 | 3.35821 | -51.27185 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bd5521f-75de-3ee8-92e0-d7ab0c9fac1d | 1.71789 | -50.81311 | 2024-11-09 04:53:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9261f5bf-ae51-3316-8cf7-264454bb1084 | 3.18092 | -64.20247 | 2024-11-09 04:53:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf0afa44-81e2-3025-a147-ee44cafafdd6 | 1.32317 | -50.72577 | 2024-11-09 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 632ce80e-4771-3e40-926c-498fd401728f | 3.36983 | -51.2807 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3d83fbf0-fb54-37b0-a342-b3d20a777fe7 | 3.36928 | -51.27723 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8c0026ea-e62b-370d-9646-4aa795ea0ccb | 2.10516 | -50.85555 | 2024-11-09 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d6e9d281-d784-3df2-a4b5-23cf4829d643 | 1.30958 | -50.72789 | 2024-11-09 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d442fca-985d-3c56-a434-75899bea966f | 2.4803 | -50.83775 | 2024-11-09 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb5171c0-7e82-3cc4-9d9a-2a7e7884281f | 3.74479 | -51.61897 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bb9dd3f-81e8-30ee-bd80-533c38d804ea | 2.10179 | -50.85608 | 2024-11-09 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5a0edf2-42cb-3e82-9cb1-31bdfa314634 | 3.37316 | -51.28018 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4a643369-817e-3639-8a89-eaba93054361 | 1.44044 | -50.69284 | 2024-11-09 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74935c65-4b49-39e1-8335-f618f9e8e21f | 3.3737 | -51.28366 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 78edf0f4-1425-3efd-9720-bf88f65828a2 | 4.42179 | -59.76749 | 2024-11-09 04:53:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cf5fa7c-f9c7-30db-a48f-654470ac4665 | 3.74593 | -51.60465 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ab9a2f4-f42c-380e-980a-9d11f5fee3b7 | 3.36541 | -51.27428 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fac5c6b8-b670-3eea-a7f1-f3f1f7fc974b | 3.5222 | -51.43448 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3216dba4-e366-367c-8569-76c58e7c77f9 | 1.31977 | -50.7263 | 2024-11-09 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9ddaa20-f17c-3839-90be-27ef3de82bac | 3.74648 | -51.6081 | 2024-11-09 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d8fa322-ead2-3e5f-bda0-bb20561595fe | 1.30618 | -50.72842 | 2024-11-09 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 352630b9-6b43-3834-bd37-21967f5ba27b | 2.10572 | -50.85912 | 2024-11-09 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 888fe6c4-f7cb-3c81-8cd2-35bf867228bb | 2.1046 | -50.85199 | 2024-11-09 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c9216e4b-c4bf-30c5-a84c-41d2b0bcdca8 | 2.46327 | -51.06851 | 2024-11-09 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 812b2a04-3463-3cbd-aa0c-634f74fae03e | 1.19893 | -50.7112 | 2024-11-09 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9476e22-855a-3b9e-8bcb-85d5f1d689be | 1.32374 | -50.7294 | 2024-11-09 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88a4429a-3d3a-36a6-a448-d66ad5fc9c35 | 1.71846 | -50.8167 | 2024-11-09 04:53:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d547715d-9ded-3d50-948c-0e4abffa284a | -3.63682 | -50.75408 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af63c717-55aa-3ba7-8de3-7730bca6f414 | -4.25384 | -50.98449 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82278ad6-0849-3105-ac4f-8c494e5661f4 | -2.8443 | -51.35607 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bda223cf-f80a-3f86-954a-d97bafa43e0f | -2.23817 | -53.77383 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c1f58bda-7e25-3556-b6e5-f81b50026c7f | -2.11031 | -51.09412 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7df1ddd-4d16-3ca1-9822-42b5d992d130 | -3.25057 | -50.45238 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0f045aef-0261-3260-80ac-669b4a3e2be9 | -1.80916 | -52.26255 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2351e023-f8bd-398d-bfb8-99a5e2089251 | -2.32714 | -48.57649 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d285e4ab-37ad-3082-bdf5-894272d47e78 | -4.12742 | -46.85883 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16e1819e-8516-3e75-9591-ab450fd2d167 | -0.90675 | -51.76049 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6a46934-06fd-3597-bb69-18215e18a728 | -1.5078 | -52.15848 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f82106d-5f35-3396-9058-8259485abb21 | -3.24552 | -50.44874 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ef650f8-1054-3086-957a-b79c548112df | -3.25118 | -50.44834 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5433b00-aefe-3088-bd8f-6092e8bfc2a1 | -1.5224 | -52.21791 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49502ade-936a-36c8-bbf2-5198b326f42a | -2.23097 | -48.36859 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5856086e-bd58-3607-a87d-a69d2a816c64 | -2.8422 | -48.68016 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe8938ef-02b0-3e5a-ad3e-69dbadc694f6 | -3.55394 | -47.3825 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4b7f61b-6be5-3c34-86a6-ff33e41fbcc0 | -2.63423 | -46.03735 | 2024-11-09 04:55:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be621d82-b0b3-383c-ae4e-64d865c93b33 | -3.50081 | -51.03101 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77ac3dda-cef1-3fc4-89bb-e269350ba1c9 | -6.27058 | -44.54389 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cf70706e-d854-3a2d-9da7-14b3ef7b60a3 | -2.67435 | -53.02561 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7804494c-b678-3dba-a841-df6480d8134e | -2.25802 | -48.47333 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5befd2ea-e674-382b-a91c-f46f6c25310a | -3.30705 | -50.08019 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b0b327e-2b34-3ca7-93af-9f84fc85c0fd | -1.5947 | -52.48854 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 962d57a9-765b-318c-8184-13e2a400e750 | -2.5781 | -48.46557 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 748e76e4-cb86-38cb-825b-1e2f70aa2524 | -3.198 | -53.22369 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffe5c759-2faf-34f1-9c82-cc1e138b5a4e | -2.80916 | -51.80352 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f95d363-1bb6-3733-81b9-70266b7cacf3 | -2.2415 | -53.77435 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 91e720f4-af23-3754-a4b1-a6d62610f8c7 | -3.59885 | -50.24126 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27cacaf0-ded8-3edb-a1d8-c165444af9a4 | -3.3896 | -51.46489 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 287e7b6d-dcba-389b-a416-53a9822734a2 | -3.83896 | -50.03913 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2c689a6-eb94-38a5-a44e-be2364320b32 | -3.87457 | -52.38362 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README67.md)
