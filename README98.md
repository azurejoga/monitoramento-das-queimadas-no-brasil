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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53292622-4306-3097-bfc8-f4aaf4091c49 | -14.377 | -44.7534 | 2026-10-01 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 21677957-4d03-3813-8759-26d8fea6e04f | -9.806 | -44.8496 | 2026-10-01 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 1cb87621-ed6a-3e10-a2d7-06b9c75332f5 | -11.2282 | -45.1682 | 2026-10-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0b2210dc-9314-35ea-b3e0-a6904b1c6782 | -5.9151 | -53.4965 | 2026-10-01 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 7b6dbdae-e722-3069-9509-827a8ec55380 | -8.3397 | -44.1658 | 2026-10-01 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 521caf46-65fe-3570-8efb-d4447c36cd53 | -11.2278 | -45.1913 | 2026-10-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| a78c056b-679f-3766-808f-f87b7fafd81e | -9.8064 | -44.8265 | 2026-10-01 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 29af47f7-9f28-3bfe-98fd-ca6e57df4e3d | -9.8613 | -44.9577 | 2026-10-01 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 2e835b3b-0f98-3fb8-8c53-b4f18ce2a3e8 | -5.8597 | -53.479 | 2026-10-01 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 3f58b60c-ba43-3048-83b0-72de80f9cc10 | -9.8803 | -44.9553 | 2026-10-01 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 230.0 |
| 0f71e7ad-c350-39c8-926e-4f566f4eee0d | -15.6481 | -44.7217 | 2026-10-01 13:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 105.1 |
| e5f65087-cd80-37a1-9fc2-fb5b07ae7d7a | -8.34 | -44.1427 | 2026-10-01 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 86d50a4a-63bb-39a5-a4c6-7fd0ba2efed3 | -6.7334 | -55.5867 | 2026-10-01 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| f33fa44b-6fd5-3278-9f1f-43de5b02288d | -8.0162 | -42.8917 | 2026-10-01 13:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 262.5 |
| df7e2bb4-5470-321f-8727-cf6961a63841 | -9.1342 | -49.9229 | 2026-10-01 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 0933b9d2-1ebc-3c8f-9efe-100503fd5ecd | -8.6268 | -45.3054 | 2026-10-01 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| e79ac9f7-ae0b-3784-937a-de2c5ad55a8e | -6.9419 | -42.8598 | 2026-10-01 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 7cc24186-fa96-38c8-92f7-6463f38c9d2b | -12.4539 | -44.1702 | 2026-10-01 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 65b82187-6843-3fa9-8d4d-4291fff77dd2 | -9.3881 | -49.1473 | 2026-10-01 13:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 339c5139-693b-3683-acb7-82d14dbee9ab | -8.1215 | -43.5148 | 2026-10-01 13:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2b55fac0-a65d-3de2-8582-212d1d05fb09 | -7.1266 | -43.1714 | 2026-10-01 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 61138c76-0428-38fe-b0ea-b88f36ca71b4 | -8.3208 | -44.1679 | 2026-10-01 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 3ce7d7c6-75d5-3e99-a5d5-b8c65ba01d2c | -11.7182 | -43.4386 | 2026-10-01 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 0ebd8109-8bc5-36df-ad98-b18bbf5cc739 | -6.7002 | -55.0493 | 2026-10-01 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 56ddc0ed-9389-360f-ba62-7fb84f06f25e | -9.8617 | -44.9347 | 2026-10-01 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 530e7d81-30f8-3bbb-b563-b8ef0aeb7f78 | -9.7877 | -44.8058 | 2026-10-01 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 86d42f91-3b72-3c6a-9682-14a4338e54bf | -9.825 | -44.8472 | 2026-10-01 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 08cc4beb-6274-39c6-8ef1-4e3465214b0b | -14.3384 | -44.7369 | 2026-10-01 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 38674319-aa7f-394e-bb84-399060dba8a8 | -8.6262 | -45.3509 | 2026-10-01 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8a24b6ab-2210-3937-a55e-efbbb0532565 | -13.3835 | -44.0132 | 2026-10-01 13:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b17264e8-8944-3d1e-add2-aa9d62ffedaf | -9.9215 | -50.1682 | 2026-10-01 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 6df7780c-eec5-3ac2-a50d-a5fa6a06cd64 | -9.8064 | -44.8265 | 2026-10-01 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 8b613613-d292-316c-8e3e-e08212693b5b | -8.3211 | -44.1447 | 2026-10-01 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 3e5d3e0b-a933-36fe-8450-1e19fc69770e | -7.0359 | -42.8744 | 2026-10-01 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 1af49a02-f77f-3d1b-b4d9-5be81a8ccddc | -12.4535 | -44.1937 | 2026-10-01 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 218.5 |
| 9a04fcb3-365e-348e-b548-4dd2f6717d19 | -9.9026 | -50.17 | 2026-10-01 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| b990cfbf-ee99-30a1-9653-d46225554e84 | -11.2083 | -45.217 | 2026-10-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| b1f6114f-7ed0-3287-9856-e6d1afa0f83e | -12.7806 | -47.2628 | 2026-10-01 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 0cd90148-0805-330c-b2ad-0778ffa3a54b | -8.34 | -44.1427 | 2026-10-01 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 848b5ca9-dd28-3116-ae6d-bb639a030dd3 | -7.0612 | -42.3035 | 2026-10-01 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 6a747e53-0eed-3e60-9954-a17c4b50672e | -9.825 | -44.8472 | 2026-10-01 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| ddfdc971-af07-3b14-918a-2d26b88273cd | -10.5388 | -45.3759 | 2026-10-01 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 181.6 |
| a2f3f1a6-e3fc-3553-8b35-ddc2c4dceba5 | -9.2243 | -45.8074 | 2026-10-01 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| e631e13e-ef55-330b-8c57-ba7318292f87 | -7.0451 | -42.0666 | 2026-10-01 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 5c7e2a88-7adc-35d8-bcbd-e06c2b84225d | -6.7333 | -55.6066 | 2026-10-01 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 24e388ed-ec2d-34e6-8992-ac3630cc5421 | -8.6454 | -45.3261 | 2026-10-01 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 41d8552d-32fa-301d-b282-a8b8de7baf2b | -8.6259 | -45.3737 | 2026-10-01 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 1fe037a4-97f0-368b-9a8d-4f3ebebfca7d | -11.2275 | -45.2143 | 2026-10-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| aa784166-bc30-33fd-8d50-6afca929e68e | -12.4728 | -44.1906 | 2026-10-01 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 9d69198f-e1ff-328c-944f-09c4e9fada12 | -11.2087 | -45.1939 | 2026-10-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.4 |
| f4d3a8de-aab3-3210-bddd-3001f11c82d2 | -10.9337 | -50.7465 | 2026-10-01 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 59661826-c573-3a3d-bf9b-d29d144d10e9 | -13.3835 | -44.0132 | 2026-10-01 13:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| a68f7e67-daf8-3909-a700-efd7c5d67ac9 | -8.3397 | -44.1658 | 2026-10-01 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 83fef835-5caa-3bf3-a935-f10d63e199a9 | -6.7334 | -55.5867 | 2026-10-01 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| a376afa3-ee94-329c-b1a0-f5e62bc9d819 | -8.1683 | -54.8037 | 2026-10-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ff2e857b-34bd-3d27-8aa1-0b6f4ed817e1 | -16.9909 | -45.4594 | 2026-10-01 13:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 57b0c397-66a6-3b83-8774-22cfb47540e6 | -6.7519 | -55.5857 | 2026-10-01 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 44057a07-f29a-37a6-90d8-ce68e7b23b78 | -5.8412 | -53.4799 | 2026-10-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 42f48da2-0867-393d-9fbe-deeb4e4fba77 | -8.6268 | -45.3054 | 2026-10-01 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5a9b5f0c-d18f-3654-b5b0-0faf004daa09 | -12.4732 | -44.167 | 2026-10-01 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 94d0ada4-f82e-335b-bcab-7e29e65714f4 | -9.224 | -45.8301 | 2026-10-01 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d3845296-d620-35fa-acf1-8fa71db32006 | -8.1496 | -54.8049 | 2026-10-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 746dd674-6ef1-3829-9bca-b967c0a996fe | -7.055 | -42.849 | 2026-10-01 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| bbc1dae3-0409-334b-9ec2-2d0af8ed1d64 | -9.8807 | -44.9323 | 2026-10-01 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 36878b6f-b7fb-3530-8db0-7ca2a3bcac2e | -7.0798 | -42.3255 | 2026-10-01 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 4da1417e-22f5-3021-a92b-3fb1520707db | -7.7407 | -54.7901 | 2026-10-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7500fc46-73ba-3ff4-bef5-4917b8cc3d06 | -7.0736 | -42.8708 | 2026-10-01 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 20da2d0e-876a-3889-83d8-9d705416f251 | -14.377 | -44.7534 | 2026-10-01 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 35314cff-39d1-3d05-804b-489dcd08f55b | -9.806 | -44.8496 | 2026-10-01 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| a864a85f-1cd9-33de-8fc2-01a805f7fb50 | -9.8803 | -44.9553 | 2026-10-01 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 3cabdd90-cc39-3998-9e0a-500274ae3adc | -7.0609 | -42.3274 | 2026-10-01 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 98f9bf00-eab9-387c-a677-90be898602b1 | -5.8597 | -53.479 | 2026-10-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| ab420a69-39c2-3f97-af9a-a4c5644d43cf | -11.2282 | -45.1682 | 2026-10-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8dad93d2-4b87-3200-b2f7-00ba0bcf88c2 | -5.9151 | -53.4965 | 2026-10-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| f52db0e0-5036-3c74-8e46-847720408f7b | -9.8067 | -44.8035 | 2026-10-01 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e4a42503-5338-3a68-abc3-a0f84b2c53f1 | -11.2278 | -45.1913 | 2026-10-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 1f6a3f55-80dc-3c61-81ee-d1e8e821ff25 | -8.0166 | -42.8681 | 2026-10-01 13:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 28c9dfd3-4915-355c-932f-5d7f7f9b84e2 | -7.0738 | -42.8472 | 2026-10-01 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 8b7c3dd9-3aee-3b89-823d-123c8088d003 | -12.4539 | -44.1702 | 2026-10-01 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 226.5 |
| ebe6c963-ff66-3b2a-8c86-68c58c796e13 | -6.7002 | -55.0493 | 2026-10-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f1628548-a8c9-344e-9bf1-8b25a6051f75 | -14.3574 | -44.7569 | 2026-10-01 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 8b73540e-0db7-3a78-b7a1-1b853b61f099 | -5.9152 | -53.4762 | 2026-10-01 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 7099a1ca-fa89-3e31-bb28-ffc2deff79a7 | -11.2442 | -44.2392 | 2026-10-01 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 212.5 |
| fc311cae-7a05-3686-bd5d-555a47530286 | -7.0361 | -42.8508 | 2026-10-01 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 2a3ae676-4f68-3650-96bf-1b0b6aa6aae1 | -11.7182 | -43.4386 | 2026-10-01 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 305.0 |
| 6f66a020-e1f0-34a5-8572-42eadc6fb61b | -7.3967 | -42.6261 | 2026-10-01 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| d27725a7-9f76-3b03-81e5-deecb0799c4b | -9.7877 | -44.8058 | 2026-10-01 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| bf6330d8-6381-3497-8c27-90bdc710a10f | -13.3297 | -43.8097 | 2026-10-01 13:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| d007ac40-e4e0-3026-8656-7b35e758c55a | -8.3208 | -44.1679 | 2026-10-01 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| b7c1ff34-4158-3be0-a8e6-d65369f191f8 | -14.659 | -41.0175 | 2026-10-01 13:30:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 132.0 |
| 9c50222e-1cce-3759-be46-3660d17eabb6 | -11.2438 | -44.2626 | 2026-10-01 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 304.4 |
| 352d8395-b7de-38bc-9f9b-b9aba6572f2c | -11.7187 | -43.4148 | 2026-10-01 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 658d10d7-8622-333e-b8c2-a006efe71193 | -8.0162 | -42.8917 | 2026-10-01 13:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 226.5 |
| 39547ed8-8935-3884-8363-edd3effc8d11 | -12.4728 | -44.1906 | 2026-10-01 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 47b05002-0dde-30c3-996b-d5a638b81844 | -9.7877 | -44.8058 | 2026-10-01 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 67ff6017-0534-3e39-9efe-0b0a73210bff | -12.5518 | -47.1837 | 2026-10-01 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| aa387b47-4246-3634-9ca0-879f2c7d551f | -10.9151 | -50.7272 | 2026-10-01 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 920bdf09-e15f-30ca-818f-cbcb25120d01 | -12.4535 | -44.1937 | 2026-10-01 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 245ee86e-0292-325e-91de-1c0613531326 | -9.8067 | -44.8035 | 2026-10-01 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 49201ee8-3044-31d8-a273-c14161561a98 | -11.2275 | -45.2143 | 2026-10-01 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |


[Clique aqui para ver as próximas entradas](README99.md)
