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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b047a30-2554-377a-9f72-80ae449d2923 | -3.72025 | -58.86874 | 2026-09-15 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b45bec8-a5ee-3c1d-8f38-4a37e95aba5b | -5.16859 | -59.76501 | 2026-09-15 05:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 469c2b3f-d533-3fdb-bd09-e1c1c6cd7d9b | -4.38763 | -55.20567 | 2026-09-15 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ddfddb0-d2ea-3e29-aac4-edce1e9fbe11 | -9.5275 | -63.62442 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7850d1ab-1ddb-331c-9099-aa8dacdc7f83 | -3.54679 | -58.67926 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dae08664-6a3a-3ecf-acd8-648a38c61f45 | -3.42082 | -58.20941 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 933dab9e-959c-3a7c-8e39-3e64e91d8006 | -3.12791 | -61.25173 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5effcbb8-2c65-324c-9ad6-73f02285ef84 | -9.74519 | -62.36639 | 2026-09-15 05:55:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b960ff56-c729-31e6-ad06-1fea39bbd4e0 | -3.74718 | -61.75216 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c66c7907-132c-3602-bc70-c228bcf4923d | -10.67245 | -54.16373 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21372c96-aaf7-3451-9bf7-0c038c876716 | -5.12257 | -55.9445 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de9046e9-1d71-30a3-adb5-a1d1208324c1 | -13.40351 | -57.02285 | 2026-09-15 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 313ec3b9-a92c-3580-9552-fe2a18f231a5 | -11.26852 | -54.12537 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3436e5b1-695a-3562-9b59-3f0bcfacc8d3 | -4.541 | -55.61726 | 2026-09-15 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da123cf8-355e-37d2-8c7b-b1d8ddadf667 | -5.0736 | -56.24905 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11014207-a2c0-3e8b-a40b-cc6dc7fb492e | -5.11724 | -55.9435 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66804b04-f87f-3080-87a2-06e359be7363 | -9.71514 | -64.92083 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cfec9a9-15dc-345b-9400-19bf52e5e20c | -12.12243 | -57.18574 | 2026-09-15 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7691865d-1964-3a89-9088-9d3649395707 | -8.95552 | -63.90208 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d00e73c-25ab-38c7-9547-dd17ab7b7327 | -10.67696 | -54.18084 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28c3d3f2-3ed1-36c7-9529-9c5a5c76c214 | -10.30345 | -54.16869 | 2026-09-15 05:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0188244-58c8-3855-9a7d-e9222467591a | -3.74591 | -61.76037 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14f098a1-1bcb-31b7-89d8-4d856f303178 | -9.14022 | -65.82927 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf29b619-5bf8-3c4a-990a-b78f381f30b4 | -9.03905 | -60.52011 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bcce704-b2d1-3ba3-8db0-b6c26fb60372 | -5.3599 | -55.89182 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b0e1de7-a7df-3ec2-a59f-2b72c83dd152 | -10.66205 | -54.14059 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 96010045-9aef-3d41-b31a-af87330b6694 | -3.07583 | -61.01182 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d47496f2-aa51-30c3-8050-014b462fa7b9 | -10.66269 | -54.13527 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5dc0740-421f-3052-81cd-8358cfb18659 | -5.93421 | -53.54977 | 2026-09-15 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffdbcdbc-320a-38cc-8dd7-2169c4c55677 | -9.84857 | -65.18 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7123737-19e9-3262-b91e-d2ef74dbb099 | -9.71232 | -64.91671 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c7741c2-cb44-3134-86cc-c3fc4d8fd1bb | -9.03853 | -60.52384 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a70cb3c0-65f8-331f-a10f-d8925fd73879 | -11.26784 | -54.13095 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e8f8d97-d4fc-3e7e-8f72-5378ee4138e6 | -4.53507 | -55.61999 | 2026-09-15 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d63b6fa-1712-39fe-980c-5e1eac38fda3 | -9.67142 | -64.59513 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb5c664e-d1f2-32ac-80ab-7308ad6fc5f3 | -3.41503 | -58.21748 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e79ccd60-e6ef-3bce-98bd-86943dbba0ff | -3.12489 | -61.24691 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4de1e56b-cb95-344a-8624-13ce77914fe2 | -3.42461 | -58.21448 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79c6b5e3-dfc3-36a0-83d7-f839f9b8b88d | -9.10231 | -65.55802 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b625c79-85a2-326e-a649-afd7e4378b36 | -12.13375 | -57.18367 | 2026-09-15 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0bbfa7a-64cd-3b80-9bcd-e402ba7af23f | -5.1211 | -55.95477 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9323381-f751-32b6-8224-a15cb0129974 | -9.41373 | -62.70369 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6c6b7396-7c4b-3c8b-862a-3ec47784e7a3 | -3.59611 | -59.06773 | 2026-09-15 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e6c95eb-f850-3d96-b5f5-594973eada72 | -3.72625 | -61.74474 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0d241c1-d600-3d52-8ef5-c3d30bb83740 | -3.04705 | -61.2715 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b0a037e-f454-3176-b17e-af68ddf9c9fd | -9.45654 | -56.70921 | 2026-09-15 05:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6be73c50-a9e2-3ae6-9cd8-f82e632fcf6b | -9.7168 | -64.91006 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abfb6266-0396-315d-a8b4-3663795e05ad | -4.52918 | -54.92035 | 2026-09-15 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d817efd-4348-3b64-8d5c-da8dd45e511f | -3.17453 | -60.64707 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cdeced7-4158-3c87-8793-1349b625a973 | -9.85472 | -65.18462 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32ea137c-968a-33be-b63a-408f522e7880 | -9.67648 | -65.79662 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5904ec80-3477-3356-a85d-f47f269f703d | -9.25514 | -59.63949 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c172133f-c504-3597-9372-8e3e95ac5412 | -9.71569 | -64.91724 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0272e42d-acbf-334a-a6e8-adfc03096f16 | -3.72984 | -61.7453 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 707bd639-395b-3377-8d2b-03ca0addabc9 | -9.41309 | -62.70796 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 26ef66d5-f5e8-3e12-9c09-616055cd86f2 | -5.3545 | -55.8911 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecc088e4-7dc7-34c6-95c2-8e5c2b43bd24 | -9.41007 | -62.70313 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7acd8444-2df7-3b44-a6be-8badf032a74f | -10.68023 | -54.15374 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0416ca2c-87c1-3376-b386-b2e1644a14e4 | -3.7328 | -61.74995 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd27861b-7228-34fc-8083-9eba7cc97254 | -4.51587 | -54.97267 | 2026-09-15 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b65aa77c-baf3-3bee-833e-b728665c2c94 | -3.42528 | -58.21009 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7e0277f-8589-33fe-ab74-89e61702864f | -9.41611 | -62.71278 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84df8264-e155-3596-be5f-de97a358c143 | -10.66856 | -54.14129 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3fdaeec-0347-354b-8ded-1259a0ba1bd2 | -5.12306 | -55.94106 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 057e3982-0163-3400-b1e3-7bd3f3f134cf | -9.84801 | -65.18356 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 052451df-0d22-3078-b354-aed27379b7d1 | -9.12858 | -65.83815 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8d17d407-32ac-30bd-8462-a775b0d86233 | -3.37644 | -59.50857 | 2026-09-15 05:55:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4af2fb04-81b5-30ab-ba51-61696ee9edb0 | -3.55112 | -58.67993 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cea9831-e969-32a2-a729-43ca88cfd3bb | -3.12685 | -59.03916 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e42f2379-e2ed-3db1-a871-0f3c2d81a284 | -13.40304 | -57.02673 | 2026-09-15 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f2ac998-50d5-3155-9fa1-ab4f22381f4a | -9.45698 | -56.70578 | 2026-09-15 05:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98f9986d-81a7-30e7-9181-894ac7913367 | -9.26398 | -59.64073 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ee2922b-e4a3-31e3-b11a-28af0ee8482a | -5.81049 | -53.79813 | 2026-09-15 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fd7420d-ee8a-3746-8922-1c8040ad712f | -3.42328 | -58.22322 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a737608-52c7-37f1-a1b9-16f744cbf303 | -5.92858 | -53.54385 | 2026-09-15 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9fce713-5674-3e2f-b77d-d465887b61a6 | -3.55174 | -58.67583 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87a8099a-2bea-340f-9d70-9131bb493e04 | -3.17607 | -61.10974 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f5da3ee-5696-32bd-ad1c-76fedea76bd4 | -12.12155 | -57.19273 | 2026-09-15 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa0cf02d-0cdc-3009-bc35-55d9322c3df1 | -9.49689 | -64.09391 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d95d14bd-4c8c-3255-8dd3-f5037404638c | -3.10083 | -61.50083 | 2026-09-15 05:55:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59c6eb26-2d59-3d91-ab76-1f62f803b58c | -9.48738 | -62.98474 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92e83f98-bab1-38c7-a384-e0620f3e6244 | -3.1754 | -61.11407 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae2226be-3431-3a80-bbd9-8d2feacea6e8 | -5.13318 | -55.94672 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db674107-4cc0-33dc-aaf4-f12e903f8dfd | -3.17104 | -61.11784 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e345c1f4-d155-3fbf-91ae-c04b9c040460 | -3.12451 | -61.41942 | 2026-09-15 05:55:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e23dde6-7e9c-34e1-b504-dafa0a79115f | -9.41246 | -62.71223 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| ca2b537f-b96d-3b77-9e8e-c604969bc355 | -3.70371 | -58.86212 | 2026-09-15 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7700892-47a5-39c1-ae22-8c9e9d67d4ab | -11.2672 | -54.13099 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 787bfd85-5f56-3c6d-bf0c-65a20a5d9c76 | -3.73344 | -61.74586 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b07d70f7-633f-3314-aacd-019e20ba3a2f | -3.41123 | -58.21243 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b83d3a0-9dc9-352b-a5eb-44f2527953d7 | -10.67957 | -54.15919 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40ec53f2-0a22-33cc-be9e-df07ff67e83d | -10.30279 | -54.17399 | 2026-09-15 05:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f008fe6a-0cfb-365b-b17e-47c090413c2c | -9.54029 | -62.37227 | 2026-09-15 05:55:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05e5cd1b-7b7b-3545-b7ac-00c8b4d8a0fc | -10.03503 | -52.09813 | 2026-09-15 05:55:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8cdfe2d-ce4f-3818-b24e-0edbdab97ca2 | -3.72921 | -61.7494 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8be776ed-1c20-3942-9b39-8f96b28de8cc | -3.72561 | -61.74884 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f32f7e03-3a86-34b6-abe5-1cb49104b246 | -4.54051 | -55.62069 | 2026-09-15 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b7aa0e2-8070-3b58-9fd3-a2f4a34df2cf | -3.42773 | -58.22392 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81e6970b-8331-3c5f-a819-9ee119e9b6c6 | -10.67827 | -54.16998 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 058c91a0-b834-31c3-98c1-b6314538a04f | -10.2582 | -57.70105 | 2026-09-15 05:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README68.md)
