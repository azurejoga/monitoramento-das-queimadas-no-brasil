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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b17fd4d-f17b-3586-9ba3-0493292eef50 | -7.83572 | -61.34251 | 2026-08-16 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63d48d60-73cd-38bd-bd42-fb72a253ccfb | -6.82371 | -56.45859 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ec83811f-cdf8-3b9e-9498-079164fad424 | -6.6491 | -56.40891 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe99d2d8-7db6-3ae0-9f47-70f166db7805 | -6.82094 | -56.45459 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b29b6ed5-ae34-3494-9b72-df0cc731f2cd | -9.13854 | -68.19711 | 2026-08-16 05:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bb83bd8-e930-3c00-be6f-b14738b4c468 | -6.60709 | -58.98355 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5632e3b5-1323-3703-8f7d-5c9668adcb27 | -11.47996 | -46.59076 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 537c4a9b-558d-3439-a1d8-df93f4ff6f2c | -10.83793 | -54.03694 | 2026-08-16 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d9efb5f-c749-3ea6-a5f5-7b4ba3c6bc04 | -6.65129 | -56.41327 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9262b4fc-4784-3118-80ff-e9b775ca9a71 | -6.63087 | -59.06404 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 641ad4a7-84be-3379-ba98-11ef04af3314 | -9.25805 | -56.90326 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e37e59e-a3aa-338b-b89f-b5917171ddd6 | -8.97059 | -60.53707 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 595b5b53-733f-36cf-ac64-2dc6aa37f838 | -6.72441 | -58.93019 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 734e6aa5-edc6-3756-9ed1-935672fbed50 | -11.47892 | -46.59907 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05e5c382-5854-3293-8276-00184068f051 | -8.61571 | -54.67724 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccd76a1e-1506-3a47-862c-d8681ac3986c | -8.94486 | -60.52786 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57518be2-3b72-341f-a2d1-0c1ff9378fa9 | -9.49394 | -51.61537 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ccd5dc3-b4c0-388b-9727-5f77dd673b24 | -6.86866 | -56.40866 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82e194a6-4a3e-3cb9-8d97-34a933cdda99 | -8.81203 | -66.76869 | 2026-08-16 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06a523f5-3d9d-3553-9409-86f960cd5e03 | -6.27358 | -53.55381 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a4caa21-87eb-3200-8f47-70ea4d0cf2f7 | -9.37357 | -62.36073 | 2026-08-16 05:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bddf8633-9618-3393-8e50-1b4ac003e182 | -6.30648 | -43.62302 | 2026-08-16 05:16:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d42ea403-d4f9-30fe-826b-b4d27b37d834 | -6.8143 | -56.45354 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 992cb6b4-0f46-38af-ab14-9a9b1eeb0ab0 | -6.83091 | -56.43478 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 486463f4-2a60-34f9-9db0-a6587f7719af | -12.03122 | -46.43887 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5d537516-da8e-3a56-910b-c77ecc12b5e0 | -7.27946 | -44.71688 | 2026-08-16 05:16:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56e27283-6926-3981-b800-af8bfa4b20f9 | -8.26643 | -57.34182 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 994f599d-4a3d-31f2-a11b-b38e57275f0e | -8.90436 | -60.55928 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d719d8d7-83f0-30cd-aade-0ed174e7454f | -8.64523 | -54.71223 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c99615a5-8c96-312e-8262-c84d8834cc2b | -6.67184 | -43.99502 | 2026-08-16 05:16:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35081481-aa6d-3eff-8d25-1193dfa090f9 | -8.9843 | -60.52503 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af673774-20e9-307d-8547-d4382ad8091c | -6.62011 | -58.99416 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8b49f27-9961-344e-bab5-c1de938e36b7 | -5.13721 | -50.84878 | 2026-08-16 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85692243-cd16-3393-855a-b98b9be55d69 | -11.45498 | -46.6012 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1129ae5d-4448-39ba-9b91-cc7b172d3b78 | -9.29881 | -56.81285 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3da572a-ae54-3d4b-b137-7e81f64bc41e | -6.79526 | -58.7878 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7deb0021-bed7-35cd-a6cc-ce4ac5b9c247 | -8.66079 | -54.72543 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16c96566-ada7-3317-9f64-24ac940e94c6 | -6.84697 | -56.41952 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 234e7321-c788-3180-b738-4d2eec641eca | -6.70538 | -58.95638 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7aef1289-423b-3aa6-bc6b-1955ea4d3a7b | -8.97606 | -60.50457 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 999113aa-829e-3bd5-bfd0-8674b3723d3b | -8.61001 | -54.69149 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e63fecd1-6a81-3d84-9a47-5fc1dd3a0b72 | -9.27189 | -56.9019 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0160b695-7342-3c15-83e3-3ff63568f903 | -6.85281 | -58.96318 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5eba1ee2-e856-3c98-a518-78185b0aa0c4 | -3.14662 | -60.26234 | 2026-08-16 05:16:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ee60d20-9c86-36b3-8403-ee77231f5fe5 | -6.59067 | -58.9936 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caf2ca61-cb67-3e64-a2c6-4e1527f7ea63 | -9.08629 | -61.39958 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ff17049-41c3-305e-abd6-beba7d71f905 | -6.8525 | -56.42752 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8e6a172-418d-3418-b27b-9ecca887878b | -8.95101 | -60.51458 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9b520915-49e9-3c96-b163-a15e8fbd35b4 | -11.22348 | -54.82354 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 347fffca-ec63-3ec2-b9b0-522dd68b8db1 | -6.70673 | -58.9482 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c65205c9-c60c-319b-8467-4b1edd48e95b | -8.54105 | -54.59807 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c52e2008-f327-38c6-bb6c-4364ec268add | -6.97255 | -59.0071 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58819c29-b455-3128-952b-75932ea358f5 | -6.62816 | -59.08065 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 85dbf75a-24e2-3636-966a-e9e95a56a689 | -6.21921 | -47.73237 | 2026-08-16 05:16:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8776ef68-53c8-3d58-872c-2a34c5add158 | -8.59011 | -54.68457 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ee6ce40-3cf9-3cec-b901-1bcd15299b6d | -8.35497 | -45.98353 | 2026-08-16 05:16:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6be86f0-5c3e-37f3-9ab0-c9cfae79322b | -8.96916 | -60.52245 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 757754e5-83a7-38c0-9157-5d52e93468cb | -11.07456 | -47.27855 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e4f550d-922d-37dc-b53b-fea1c60221ca | -9.3981 | -65.96407 | 2026-08-16 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61da46c5-5525-333b-a0fc-9e8c2c03d3c1 | -8.64125 | -54.71537 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54cf763b-1746-3b01-acf7-758334c3c8ce | -6.70383 | -58.94348 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 8c6e545d-b5ff-3cae-ac12-7e5a056c4aa9 | -6.86644 | -56.42256 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9d2b215-3922-3f9a-8619-a84ecafb2d92 | -8.94723 | -60.51395 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| eb81e00d-7933-3423-97a6-2602a1f3f19a | -7.55222 | -61.17311 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48de6d7a-c99e-365c-ad76-ec95406e8bf0 | -7.42872 | -60.02322 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c160f82d-73d7-3888-9021-1ae5049fcddc | -6.97855 | -56.46163 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be1e71d2-8fe4-3e40-8adc-9ebf0876f627 | -10.58046 | -53.51305 | 2026-08-16 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 710cdd12-eec7-39e1-95cc-61528b6dfbd0 | -6.12003 | -57.70726 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 533e6630-2d50-39e7-aaa5-5c4ca346be90 | -3.74235 | -55.97544 | 2026-08-16 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 114846c3-4e63-3069-97cc-9ce1d61d75ab | -7.83856 | -61.35028 | 2026-08-16 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c272dc7-e9eb-3119-a749-c7d7acab65a9 | -11.3275 | -46.21429 | 2026-08-16 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4de45aca-e501-3961-af56-a8c440901c09 | -8.02702 | -55.1412 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25a36581-cab4-36fa-85ff-a42baba1bff6 | -9.26469 | -56.90433 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 660b1663-3f73-3df6-9bb5-d897c74559c7 | -9.14015 | -68.20016 | 2026-08-16 05:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4ed5ad6-4233-3167-bce8-36bc58cd80b6 | -6.20938 | -47.73039 | 2026-08-16 05:16:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cc10f1e0-0a97-30e0-a010-b42464da5e74 | -6.70112 | -58.95987 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 418ba327-1654-32eb-969e-91a12b59ca21 | -6.86196 | -58.95215 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 615fdeb5-081c-3397-8c95-b912104fd74e | -8.43802 | -62.68005 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 1fe9f417-54d0-326a-853d-aa4e2a2872cc | -6.6185 | -59.04911 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7acfec27-8bc0-3fe4-9840-2c07ab926908 | -6.83313 | -56.42088 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48f42445-6b6e-3b06-99b8-34ed4afc1f21 | -8.89544 | -60.5502 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c3f2265-ae4a-32ca-b7f3-d12033a98f6f | -6.83756 | -56.43584 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c71db4c-ed76-3107-a963-265209b23dd1 | -10.52908 | -44.84922 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fae6a53-d2fb-3092-b37e-147a83aca268 | -8.89676 | -60.55801 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6456a42-f13b-3acf-bb64-263ce8162732 | -12.01714 | -46.43121 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2df380f-8a9d-3585-b457-e2c1d4b3af3c | -11.22695 | -54.82408 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae8eb8e8-d704-33d2-a2c0-320d2ddff119 | -9.48459 | -60.47312 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 881f96b4-c0b2-3ed0-bb54-eef119580f5e | -7.44224 | -55.30792 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abea3180-4d69-383f-ad43-27d54e961e7f | -7.36472 | -46.8466 | 2026-08-16 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e220882-3998-3a86-b446-dd4c6f694bdc | -6.83202 | -56.42783 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd940c78-50b8-323e-b886-0c18b0792175 | -8.61855 | -54.68147 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06ebbff8-9004-3196-85f9-0f6ba65f0b14 | -6.60146 | -58.99534 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51465f5b-3eb9-3f41-bd90-dd4822c18caf | -6.68761 | -59.06363 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b0ea017-71a5-3272-8227-6f691ab2c1b5 | -6.62692 | -56.27008 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84eed513-fab5-3ce7-aa8a-ee9700cc7822 | -8.95544 | -60.53447 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 97758cbd-eff2-3de1-9557-a956e877c9f9 | -6.82261 | -56.44415 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4e4aadd-5ce1-3f72-9944-68184cb45ec6 | -11.1073 | -47.24376 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c329bbde-45c3-37ae-aadf-aa39107bcdbe | -8.26366 | -57.33772 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d0da6d7-fd5a-3572-905d-8a7e37de3c94 | -11.47946 | -46.59472 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a11d9c2d-0fa6-33cd-99ac-ef26d1816430 | -11.04415 | -47.25173 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README35.md)
