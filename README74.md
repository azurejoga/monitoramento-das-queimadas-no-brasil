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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4caca40a-828e-30cd-86d7-8bf38b91f384 | -8.72142 | -70.54813 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 231bed6e-6c65-3d75-af16-3a243446c1d9 | -9.93647 | -60.51687 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd9f950a-ba39-33e9-8f70-a0e7cb480bd3 | -8.81066 | -70.77737 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43fab6d1-a9a4-3af1-a178-847c267afef2 | -8.96544 | -62.388 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 806b2c24-943a-325a-bd8a-085fe19d313b | -2.66704 | -59.37184 | 2026-08-31 05:55:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 337b00dd-2c4f-34b0-8c76-da018b11ee02 | -8.94547 | -62.38132 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f77a40e1-9f50-3c64-a2bc-a4b16723d8e8 | -8.86867 | -66.77597 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 887be630-4843-391e-8c4a-638cb8ef3d26 | -9.17449 | -59.63747 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 737e00f9-1cc9-3ae6-9821-3f6991643121 | -15.54992 | -56.2867 | 2026-08-31 05:55:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24a46d69-7612-3b90-8aed-fd86fbd4450c | -3.1148 | -61.23318 | 2026-08-31 05:55:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cf95b0c-1f22-3088-a484-e5315532afa8 | -9.04976 | -65.41252 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbfdf156-8e6f-321e-b7ae-b605c9dfe172 | -8.60381 | -70.20693 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49d8b840-6a8f-3cc7-bf6f-288374edc244 | -9.00403 | -60.59756 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32e55b62-23aa-32c6-a52e-403b1bf473fe | -8.0102 | -70.0687 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 669f776c-031f-3218-8931-7a9a4efeed77 | -9.16642 | -59.50999 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dc11127-2355-3aa2-978a-b80758973c76 | -3.6333 | -60.55437 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e795a57-222a-355f-bbef-d8d9accb84cd | -14.42839 | -56.27509 | 2026-08-31 05:55:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a49c9f14-0dd5-3464-a454-2d0e81c53e3a | -11.47659 | -58.51468 | 2026-08-31 05:55:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b0351b2-d0af-3ec6-a92e-c0143f6a835a | -9.04905 | -70.64983 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f804cfb4-ece3-3fdc-836d-62401df2813e | -3.6327 | -60.5584 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 126559ed-3cc9-3f0f-bba9-b30026b22385 | -8.3746 | -70.8306 | 2026-08-31 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b9892d6-312a-3e82-b10a-4054e13f039f | -8.67732 | -66.52136 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fbcff40-3e08-3a3f-ba66-31eafed1ade2 | -8.93882 | -62.36911 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3a6bc9f-4071-32f4-8265-6a485ee49221 | -8.96492 | -62.39165 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e45d09dc-0978-3d94-979e-e39ce0e6fb55 | -9.69858 | -65.06001 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fdee868-9601-33e8-9a46-76d8b52c6108 | -9.01408 | -65.40028 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dffb4aa-d419-31e8-b76e-5dd54581d258 | -8.70331 | -69.97457 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edce1ba3-3660-3c62-b31b-79f812458f12 | -8.83768 | -62.32205 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1c9236c-b3c7-3993-9623-b5af20414938 | -3.62474 | -60.55312 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4dbf110f-b0ba-3a46-8bd0-c833e3a470eb | -9.04861 | -65.44379 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 219882e8-8387-3bde-9a79-e41aca9da693 | -9.89171 | -60.27502 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ed4c434-ade1-3b34-bd9c-8f8db3cb51ae | -8.72431 | -70.78436 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e08ffeb-e2bc-37fb-ba96-7d5e78866137 | -10.17629 | -69.06904 | 2026-08-31 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1d7c6e5-0cae-3bf9-9176-db293d33a826 | -9.27619 | -67.51172 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e0aed1d-42e2-30ee-945f-5d0e296210b0 | -9.14987 | -61.10069 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3781c383-2c1e-3fb0-beeb-851ac67119bf | -9.13229 | -65.47627 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7123a499-4252-3062-928b-127820c59c87 | -8.7996 | -62.50225 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2f9da5a-e37f-30fb-81ac-6c12f4714683 | -9.51494 | -65.58004 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fec51f37-aadd-30f8-835e-34843204c508 | -15.67627 | -56.27836 | 2026-08-31 05:55:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c39f3604-577f-3641-a79c-c87ca2463876 | -8.79713 | -62.49086 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7be03b9a-cd50-36af-b11a-660631cd9061 | -9.06017 | -65.41412 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eca3aed-c569-33dc-a484-fb4b292e8dc0 | -3.88696 | -59.39944 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3d593ca-4484-319b-a849-8b40505a11d7 | -9.02914 | -65.39471 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53a4d034-0464-3e29-93ff-cfe51f729fcc | -9.85501 | -64.98357 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed56df9e-707a-3049-be2d-2b96f35ab865 | -15.67956 | -56.27944 | 2026-08-31 05:55:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ecf2062-fce8-3201-a1d0-b6b3e1f9028e | -8.60044 | -70.2033 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb7422c6-8dd0-30e7-a326-5d629990ea69 | -4.29099 | -59.94923 | 2026-08-31 05:55:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eab2edaf-78ed-3a8b-8d6b-e1af4f79bf9e | -8.59898 | -70.21423 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b54bbab-217d-3b38-a8d9-d879c6ab8626 | -11.49784 | -60.5865 | 2026-08-31 05:55:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0198ca8a-fca2-390e-8bfc-8f6b83c18e6f | -10.48417 | -59.61029 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c4996aa-ffd6-300d-ae88-904818652cb4 | -9.8903 | -60.28565 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7db32334-4a33-371e-bce1-2e28981c6d2b | -3.62414 | -60.55713 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 916215b7-e8b8-362c-aa82-511065ddd31d | -14.42655 | -56.27579 | 2026-08-31 05:55:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0fb7433-7573-329f-a557-519a422ebdcc | -9.93576 | -60.52193 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffa6b9d0-effc-38ab-9479-a278e3bf796e | -3.62962 | -60.54973 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e9da031-72b6-3c3a-b61e-98e4fba14041 | -8.94189 | -62.37706 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2da8d4a-d64d-329d-8a66-0dab3a261f6c | -9.06708 | -60.4161 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7a52996-d8e4-345e-9945-645916677cb7 | -4.28649 | -59.94855 | 2026-08-31 05:55:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c276b811-b85b-37ba-aba8-6ba9b326fcd8 | -8.83861 | -62.32221 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fe4ad36-2f96-3dce-9238-a041253981a8 | -3.63209 | -60.56243 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b23b9b72-8a59-3e78-8317-789ec0a0e2d1 | -8.52388 | -67.15635 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b21abf59-0fd0-3d87-b4cc-ff8595b42976 | -3.03376 | -59.36421 | 2026-08-31 05:55:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 190bbda5-e5a9-3505-986d-5c08ddf1703c | -8.65636 | -62.82375 | 2026-08-31 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aff9b52b-f1aa-341c-bb26-e920fe6008c3 | -4.85991 | -55.8352 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24cdd29f-8153-3ac6-ae92-0ed93fe98eb1 | -8.79307 | -62.49026 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2050befd-85da-35ec-a858-46999134079d | -4.1526 | -60.69275 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5349a368-ed6b-3980-bb57-c30c7318a18d | -3.62841 | -60.55779 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98af65ab-6e57-3ba2-922d-f82b55329044 | -9.93979 | -60.52758 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1468eb5-2f80-3e28-b635-073e42f97009 | -9.15276 | -59.53595 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d24188e0-ee87-3ac2-8231-b4445dad6835 | -8.68468 | -62.81401 | 2026-08-31 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d1c26fa-0555-3eda-8d06-82867941c1c2 | -9.43126 | -67.41167 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b0085dd-e519-38e6-a2d4-dc5467bddef9 | -8.39499 | -70.08548 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d48c2a8e-3823-331b-baad-eb701dd8dcd7 | -8.34907 | -70.10213 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11de4d03-bfa8-3d20-adb9-090cedb560cd | -8.60733 | -70.20753 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd0449dc-cc4a-3ffb-8848-b9fd702aa7b9 | -8.26119 | -62.75465 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02188a95-1cab-39d1-bc9a-800df3c262f4 | -9.85771 | -64.98277 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68a82521-da88-3839-a894-f86912324dee | -4.85454 | -55.82986 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef3d763c-29c2-3a53-bfc0-d1ad73199afc | -3.7654 | -59.3347 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed06da5e-7192-3fbc-b741-1d319218b994 | -9.71542 | -64.99647 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf2092aa-f248-3d90-bf91-c90fdab18748 | -3.11535 | -61.22961 | 2026-08-31 05:55:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4031bbed-f056-3893-9e18-0e8e3315840a | -9.00438 | -69.4413 | 2026-08-31 05:55:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f67b8cc1-05de-344d-88f2-d761b922b394 | -9.94592 | -60.51806 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fde201e0-1cb9-3ea6-83ab-8413f904e6d5 | -4.15447 | -60.70938 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d6a5fca-e4fd-37c6-842f-f85f44e87613 | -8.94702 | -62.3703 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cebbd69c-a7c0-3595-9c31-cd674aa189ef | -9.07107 | -60.42181 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4918ec2a-0469-3409-a233-e058977eac0c | -9.30682 | -56.80807 | 2026-08-31 05:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 171a6645-2a6c-33e3-b05d-a77265e40629 | -8.42171 | -70.14568 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f92f1593-457c-3a5a-9fd9-895b3121af37 | -9.94119 | -60.51746 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d10f9eb1-d3bf-304e-938e-6e59d534923e | -7.4468 | -73.07302 | 2026-08-31 05:55:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd7478ed-0554-3210-833f-9119068b9fe1 | -8.60096 | -70.20239 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dfd4d23-4e2b-3a8e-bb6b-b6d27a7fc7ea | -8.94261 | -62.3786 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 700bef75-c751-33fc-b108-f638ea4c246a | -9.15123 | -59.54736 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13e98c16-1bb9-3f98-8a62-20f94213686d | -10.48922 | -59.61105 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9cec2704-f3db-3a6f-b1d9-d8141965fdb4 | -3.88504 | -59.40194 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8334af3f-a6ce-3579-a0d6-56b88c71b1d8 | -8.92238 | -72.83715 | 2026-08-31 05:55:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ab192fb-d6e9-3129-996e-096085b3572f | -8.80119 | -62.49146 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1e72046-ae2b-35a9-a77c-771a615c0dca | -11.49307 | -60.58559 | 2026-08-31 05:55:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a78d2a07-e60c-3c12-8f0a-f8bdc0169171 | -9.06248 | -65.42234 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85c530cb-f62d-34ab-82f2-a46673857dfd | -8.60183 | -70.21878 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8741476-6538-3cba-af50-8601e6eb0171 | -10.19827 | -69.35021 | 2026-08-31 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README75.md)
