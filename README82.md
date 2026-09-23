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
| 1ba6e383-7308-30e2-950a-b4d1e3b92c89 | -4.15902 | -60.77327 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5cfc827-d188-31a8-8beb-a0f1d626b437 | -3.18205 | -61.10658 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d566d59-69e5-3566-b4e8-3786b87d1221 | -5.80742 | -52.08683 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0862d71d-d645-3280-a17f-c35bffd0b684 | -5.87049 | -51.94691 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ac871ca-9126-3665-87e8-a1175321ef6a | -5.87335 | -52.0758 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac4d6ae0-2d99-3764-aa92-3d688c81b038 | -10.27464 | -49.97843 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 46764830-18f8-3975-86f1-523078e51350 | -10.69992 | -48.71819 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d772d24f-063d-3a45-b1bb-8b20415b6acd | -7.04531 | -62.93959 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 082fa30f-85aa-3d70-928d-ea47a2994e60 | -7.54906 | -48.69087 | 2026-09-23 05:04:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b28b6c73-90e3-3d86-bd19-592e52754221 | -6.23214 | -55.43533 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60b368ea-9574-3111-be98-d81484044e96 | -9.04136 | -65.40923 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d8a2257-8433-38af-b6d6-1f4758ce44ca | -3.85861 | -58.81716 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 81797211-f326-3251-9550-ab99cbdf3e7b | -3.65092 | -60.60945 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 881e9787-09b7-3bd8-9413-18b092abe92f | -7.56362 | -57.67584 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68ea580b-8481-3494-9cdd-1e8512f2c389 | -5.85338 | -52.03351 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aed9f772-187c-39c3-8693-0239da5c2bb8 | -3.69168 | -60.55648 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c60541b7-86ac-3311-bcd3-d8b5369cd321 | -6.02752 | -55.34131 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52ce2296-6622-3e48-9cc9-1fe87a2dc710 | -6.67258 | -58.5758 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b5592e71-8bb1-36bb-bcb0-ebfefbb29c75 | -3.6809 | -60.58926 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e54418ad-5b1d-360f-bfef-ecc66a1bc2ea | -6.12999 | -52.76416 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8763f9db-67c7-3abe-8c73-35026e01e90c | -11.63219 | -50.95016 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d535aab-8ffe-3f5b-bbb6-b30f193eb5ab | -6.30382 | -56.04407 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad7c223d-4678-3971-bda0-1d12c7ba5b20 | -10.04491 | -50.2208 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f066dd71-ca04-3063-aed6-cbab6d81dd15 | -5.74847 | -51.92731 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a24b0778-672f-36ea-bd01-7355b7116b30 | -6.44526 | -59.96816 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a121848-82a1-36c4-b5a2-444acbfb06cc | -5.82998 | -49.95535 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e099335b-c1f5-3489-b96f-ae1fdabcdd2e | -6.03042 | -55.34594 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a341057c-4fc5-3ca5-8d74-7546735dc99a | -8.08601 | -48.85932 | 2026-09-23 05:04:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b649c58c-aec2-3f2d-9365-2600a0a07c65 | -6.61462 | -59.9547 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c3c57e8-3bc6-3225-b8b4-1a8049b1f429 | -6.67165 | -55.06433 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 161aee44-d7d2-3269-9b01-e7abfe0f11d4 | -5.69757 | -47.39297 | 2026-09-23 05:04:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de956e1d-228d-3483-866d-fe47cc3d1c8f | -10.89881 | -53.96067 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c64ebc0-5a2b-3bb4-bcd6-b410b955022f | -5.15064 | -60.31039 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7603fa57-cc20-39f0-ac37-ce022659b100 | -9.56868 | -47.96379 | 2026-09-23 05:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7b05dc1-0cd8-3607-873e-e8878f07a48a | -4.17676 | -53.66337 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f65d64d7-919f-3462-8f64-1c34d0c8229e | -6.89514 | -46.54611 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d22c821f-e04a-35cf-bf68-6e8d7fab3ea9 | -5.83344 | -52.05175 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11f71f74-5880-3d03-976e-1db3ee465400 | -9.93463 | -48.46717 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b889fceb-141d-34c1-97ea-c04262889c60 | -5.18043 | -56.1826 | 2026-09-23 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aa6cb75-9362-3537-a448-cc322c902957 | -5.74113 | -53.46608 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2e94dba-0a4e-3f09-9467-d4904c4201e0 | -6.16556 | -57.72362 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8ec80df-903e-3351-b82b-eb416e40ac82 | -6.85701 | -63.02226 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a05f7e8-67b6-365d-a71d-8a515b9fef30 | -11.47628 | -47.36292 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 621fb742-0c5d-3b8f-adfc-8d515615d116 | -6.66608 | -50.88404 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03ef6f5d-f085-3b57-a887-ff23906450eb | -6.17288 | -52.04768 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1f11a67-055b-30ec-9e91-d32358033f86 | -5.87499 | -52.06538 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed0f7603-35fa-32a6-a75e-b2704919876b | -9.84138 | -46.37971 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b87325b3-739e-3a06-9f71-65695d1b4ec0 | -5.81053 | -57.73222 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa074775-6f3a-3c0b-b36d-5b6c18efd8f9 | -6.8995 | -46.5468 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ee9ed89-710d-3cef-ad3d-5c58fc5e90ab | -2.85902 | -60.9146 | 2026-09-23 05:04:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 489c245c-c903-39cb-83d3-da1b7239baea | -5.89446 | -52.09341 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4a157d82-442c-3cd1-80c1-8625603bd96d | -5.88835 | -53.62006 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ba44672-f9d4-367d-9bb9-d9f5a8273042 | -6.67398 | -58.56766 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 827a0b1b-a481-3382-a3fc-06e9ceaadef2 | -3.10826 | -60.70665 | 2026-09-23 05:04:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39bf9ea4-344e-324a-8105-20901997d2af | -4.0045 | -52.08993 | 2026-09-23 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f04fe3aa-8638-3a2d-ab49-d87b3ae69ccf | -3.78753 | -60.75126 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6ba088f-9e6a-3d32-a078-ea6d0ba82c67 | -9.06898 | -46.52166 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32776ace-45ba-3a91-add3-7814623338ab | -8.86001 | -62.42387 | 2026-09-23 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 88cce40e-57ad-3780-ab4a-8961096aadf4 | -10.04536 | -50.21914 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d82b8c21-3986-3845-ae08-6d25b2266151 | -5.91889 | -52.11152 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f998b1e8-39de-3f95-8f0c-1a6402060f99 | -8.20524 | -54.71517 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fcf72fe0-d2da-3427-8d67-f938fab419fe | -4.53391 | -54.9693 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 815d38ba-3df4-3ef8-8aa5-2c875b4b6aa5 | -3.81744 | -59.0077 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9363e1ce-677b-3390-b0ef-943bb972c422 | -9.48989 | -51.90567 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9b9e2b6-28c5-3e8c-83e0-97833d9bf362 | -6.18044 | -52.78995 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 971a8ca2-5abf-32d8-b9af-bbc2f67d34f8 | -10.9027 | -53.95769 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbfdb98d-4a48-3d14-8643-5641648f6171 | -7.02777 | -44.65189 | 2026-09-23 05:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| be4ef3e4-6835-3842-b709-b867b02cf8da | -9.15523 | -61.18557 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1f3ddda7-7ee9-34ef-a23b-31de65af38e2 | -7.41367 | -49.85622 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b73cc912-5239-32de-8c19-eeb76d9ee852 | -11.65623 | -43.47 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c198b8c-9588-3526-9a63-7ae077132975 | -6.62086 | -59.91325 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 394df606-9bd2-3c00-82bc-c79d9c55ddbc | -3.65012 | -55.47855 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7c71850-d8a4-3f4e-be61-78802b2c1f7b | -8.20123 | -54.7183 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b8c8ea75-acfa-356f-99b8-7b85f097b74d | -3.69124 | -58.92141 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e13837e-f315-3757-b86d-a8e9999d165c | -5.70779 | -52.18456 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c917fb76-22e2-3d30-bf53-6950debfa392 | -6.12666 | -52.76363 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f3a9d98-dcac-36e7-9a06-e45019d0775a | -5.83062 | -52.02637 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ad827be-268b-34b9-950f-eaa54280fb48 | -9.04777 | -65.41055 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d6ae4684-1add-3cfb-9f9f-bd841a093939 | -5.81748 | -57.74095 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ffe3741-8462-3e35-be02-9521caf5737a | -3.81798 | -58.89151 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d88a70eb-e60a-3571-81df-ae94ef5a7be2 | -10.29649 | -50.52809 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 63ef0c99-9121-3f05-a69e-f24fb2aaa2e3 | -6.61434 | -59.92902 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 326ebc80-902d-3546-9695-a411ad0adb1d | -4.4513 | -55.07225 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beac5fa5-d8eb-3549-878b-159dc737c4d2 | -7.04677 | -62.93176 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a979fc7-dacb-3113-aef6-ea6efd4b11a5 | -11.01525 | -54.14614 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f78e81ec-4e6e-325f-969d-853aabedece9 | -8.3099 | -50.80915 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eee453c7-7b6a-3f0d-897d-539cdb4ff205 | -3.2894 | -57.85468 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ca2e411-07ae-31b3-8e72-2ef13764e6f4 | -6.73402 | -55.08244 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c575614-ba67-3807-80bd-9a59b645911a | -9.96828 | -50.26107 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a21f047d-aa99-3d29-bdab-786e4a644cbe | -10.04598 | -50.21489 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c718cd2-95bd-39de-9b19-34b7b4f56163 | -11.35813 | -44.20591 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e037c1e9-34c7-3072-a988-3b9e9d11ad90 | -11.12963 | -42.79087 | 2026-09-23 05:04:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8cb3eaa7-f932-30b7-a032-315e7e193c13 | -6.89872 | -43.63643 | 2026-09-23 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 493be902-4341-36d5-947d-742b21233112 | -7.15806 | -59.59042 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb5e1159-1abc-3857-9051-96d5391f80bd | -10.91217 | -53.94116 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebfa538e-7ea6-344f-8183-4469b1927021 | -5.83289 | -52.05523 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 418008ef-8de7-379d-a8dd-d46320e05b07 | -6.94059 | -52.60428 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80726e7a-2f41-329c-a51f-4ca9703e7f81 | -10.91771 | -53.9493 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ead2b3b-9b1f-384f-957b-8ad8f0ab89c4 | -5.87112 | -52.02922 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe3c783d-18eb-3280-9e26-34db827db489 | -5.89531 | -52.28219 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README83.md)
