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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bd091a5-8140-38ae-8960-71222586d936 | -13.21082 | -47.30263 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cab19f8-b6e0-3001-ac7f-e4f06b744270 | -10.71551 | -44.75118 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 78021f41-7a01-3093-b8bb-612831715831 | -12.81602 | -47.23547 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5fbb6af-2084-39ed-a3b5-a0dde94f0013 | -10.71319 | -44.74276 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c97534e4-6115-30e7-8a39-285054823578 | -10.35952 | -61.25712 | 2025-09-16 04:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80b66755-f3c9-301d-b63f-1c7c31b0247d | -10.71807 | -46.50847 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| fdfddf72-9a48-37e6-a963-d241f8d95ac6 | -8.60354 | -46.41302 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b5847a6-d3c3-32e7-82b9-e7ad1a55d3a5 | -7.38895 | -49.99731 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63abe847-beb8-3743-82ec-ba20ebbf5b03 | -12.11183 | -44.83891 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07d9f7c7-9ddb-3302-b431-3b0837928699 | -7.70785 | -45.31051 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7737fdba-ee2c-3497-b2fe-124a16337f56 | -8.60409 | -46.40953 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa487320-8807-3391-b1fc-bf0164b72810 | -9.09271 | -44.83789 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a93a682-04bc-3237-ad5c-7198adc0a792 | -9.05238 | -44.84734 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6800943-e779-3cd0-9e25-7007c69b4a49 | -8.87831 | -46.19366 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0c2ce783-575c-3752-9bbe-20d1416cf86c | -12.64438 | -47.95631 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2bad64ba-0c05-3c75-b3d8-b3864e807057 | -8.98089 | -46.24986 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 50313b0b-edd1-39ec-bedb-c04d93b0e0b2 | -7.84614 | -46.12823 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaeb94f4-dc09-3252-9817-e674fabf2fc7 | -9.05909 | -47.01889 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b6c8e85-8bd4-39d6-9eb7-0d7cd1c59022 | -9.04893 | -44.84681 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c01bea49-7a02-3ba2-9869-c750078e2a36 | -12.75375 | -47.19613 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4146065f-95e2-302e-9c3f-c6e6d9690f02 | -9.09885 | -46.93566 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a23c1e8a-7a6d-34d6-b8af-31473d21bc85 | -9.1349 | -46.94501 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e0269e8-fad9-362d-ab93-84998a678f58 | -12.80913 | -47.94306 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 978e7e42-33f0-3066-abc6-8427ef3ea946 | -9.86796 | -48.62239 | 2025-09-16 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 383b837a-2afe-3458-bb14-7d85eec9b362 | -13.82418 | -43.23239 | 2025-09-16 04:29:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7f5ea3d1-fc14-3914-aa93-bc7d109cad64 | -8.58237 | -46.35226 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fb39b540-adc8-3ddc-9a37-7cff0c58ea26 | -7.53278 | -46.72184 | 2025-09-16 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c430942a-856d-3d90-bb9e-0cc902ba6b20 | -9.17155 | -49.11552 | 2025-09-16 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a0bca0f-0953-32cd-8114-0d84d0cd9253 | -8.96381 | -44.20021 | 2025-09-16 04:29:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff6e1d61-e64c-385f-a0e5-930cf8d6cb01 | -8.65664 | -46.34947 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cf775a6-2be0-3c5e-beca-09dcf114666f | -9.46031 | -48.59434 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d554bfc-cb73-38c6-b121-1e8d246cdbd2 | -8.89619 | -46.15707 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1828c1cb-9e96-3431-b778-f59367256496 | -12.67199 | -48.01907 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cb5f2203-a038-3851-a903-566b67dfa74b | -8.12041 | -48.26212 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04d0ff1e-0654-3dd7-b805-a819dfa1af65 | -10.72252 | -44.75235 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e121251-b463-3ca8-982d-30832de9066d | -12.65831 | -47.93314 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8f6e0a3-5655-3ce3-8492-fbb9b4e013ef | -12.12064 | -44.81321 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 883939de-ec7a-34ef-b1f2-56d457ca8c51 | -12.98686 | -47.95053 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d44bf56-4ae5-3acf-b6a1-667f8fadd35f | -8.60464 | -46.40604 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9238a557-968b-3119-917d-80368b704b5c | -8.43265 | -47.213 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bca5496f-1cab-304c-a9d7-f8a0feab5286 | -9.85791 | -46.45314 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11687826-7087-31c6-9f93-10be9768319d | -12.66994 | -47.94596 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4c835c8-3b22-3898-9c8c-f57f9fa65f7f | -11.12946 | -45.34927 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0fa04afa-7910-30ec-a950-1230db2c87d4 | -9.04605 | -44.84251 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 92394fd3-72a7-391f-b3e3-560dd9f7d59e | -10.07222 | -48.17875 | 2025-09-16 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b55033b-947f-31b9-bc58-36e023a018d5 | -13.19361 | -47.30337 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1fd07ca-cde7-3913-90b0-fced38f0e6a3 | -12.92371 | -47.96889 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03470827-209b-3706-b002-591fc7782262 | -9.0495 | -44.84304 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a0b132a6-84e8-37ca-8afe-ac841af6bef6 | -10.96544 | -49.57536 | 2025-09-16 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60509d9b-79a7-3338-9b2e-0b6ce560deeb | -7.68231 | -46.28871 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4095c4a6-7c0f-32cb-93e2-c1cd7bd2d229 | -7.99919 | -45.66585 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0e543ec-07b1-37b0-9974-f731f25a6d0b | -9.07073 | -47.03151 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 757df689-097c-344c-999c-8497f0d1f3f3 | -7.40004 | -49.99913 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1763635c-5d74-3cf1-856f-54fc04f4ce34 | -12.65534 | -47.7147 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bb25e68-9081-31a9-9ec6-917604575cb9 | -7.98252 | -44.84472 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99e6419b-3097-3a69-be07-af47149008f6 | -8.59844 | -46.33688 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffa25c84-22b3-3eda-b35e-f08e2424ca22 | -10.71972 | -46.49783 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 949df95b-4cbe-3596-99ca-149ea9a5b3c4 | -12.96127 | -47.98267 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91e32884-6c5a-373a-a3e4-4c5fd9754bca | -11.71262 | -46.87014 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 565dbe57-95a1-3e35-ad6e-59c59187970a | -11.64602 | -46.60043 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c65b7f59-1868-3530-8388-3111911abe09 | -7.68037 | -44.67714 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d2a93bd-ce23-39c5-b2fd-ecc7b35eebd2 | -7.70897 | -45.30334 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c9fa4ba-a1bb-3a0b-a125-769f8eaf4db1 | -8.41724 | -45.73793 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45a6df62-9cd2-3278-841b-5620b304a6c4 | -9.06861 | -50.31071 | 2025-09-16 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f60f47c-7443-3c02-9dbd-fef2287c9d0d | -7.63126 | -46.55194 | 2025-09-16 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c01de476-18bd-38cd-bf9e-3769eb3178e7 | -7.66061 | -46.59936 | 2025-09-16 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57d3add6-8e63-3310-878a-aedeb3d6a6c5 | -8.58182 | -46.35577 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 11f29171-b3f1-3ce6-86f3-76df423aa33f | -10.43304 | -45.14066 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 818369db-5fad-3b51-9c45-1bfe66dd1e22 | -10.68834 | -46.24497 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 556b9a6a-16de-3c4d-a1df-7bda147fb05a | -10.41569 | -50.64868 | 2025-09-16 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8538a8c5-1618-3d9f-8bdd-e3f992ea074a | -12.79545 | -47.25766 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d7ec2354-36e3-39d4-95fc-5bb0b70c1930 | -12.62806 | -45.75508 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a300aaa-d078-33d7-a3cc-eea024c7511e | -11.72351 | -46.47693 | 2025-09-16 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8a01c51-e0ec-3b6a-94d6-70c96fa85158 | -12.67035 | -48.00787 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4081746e-afcb-33aa-ad9b-eb9d3b96aeca | -8.98144 | -46.24635 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3876d3b-a661-3ef1-bad5-efdcc87c0ff4 | -10.72227 | -44.75533 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c6d103df-9a09-3504-94bf-a89fd5effce2 | -10.72015 | -44.76797 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31788863-65a6-39a6-9aa8-09fdb4bb9ab4 | -10.826 | -44.09493 | 2025-09-16 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adf79eed-d16e-32e5-add6-e69a09c46361 | -12.66164 | -47.93369 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c2f52b71-4cf9-3819-b424-5bd8dd3dde8d | -10.64245 | -46.23037 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dadf4bb-d09d-3586-af94-4176a4cf133c | -7.90381 | -46.23456 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 797b59ad-e45b-356a-a158-959d952f92e8 | -10.17068 | -46.14229 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fe67bfd-a933-3b2a-a5fe-712804a124b5 | -8.11884 | -48.27381 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f59a5b8-6f05-36ac-b387-7a030465f446 | -8.93049 | -45.50481 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f48454c2-75d1-374d-97d1-a9a6f778cc2b | -8.95994 | -45.76736 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85631628-580b-3dd7-8d46-39a532ae2705 | -7.54382 | -50.48518 | 2025-09-16 04:29:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6ac63f6-5891-33d4-849a-61b330bf571a | -9.09219 | -46.93459 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 697c00d1-5277-3d4c-9b26-909525c67bae | -12.54057 | -45.87772 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8779fcbf-5c30-31e3-a2be-22371bbc6e6b | -12.6258 | -45.77026 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c996f95f-90b4-34d8-b8e3-924cd2d2c1ef | -8.6328 | -45.68739 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2479f875-6de6-30c6-8281-8e0ab7f5c146 | -7.90127 | -46.23359 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43b4cc1e-aa34-3e96-8c13-8ed122a2d83d | -12.61913 | -47.51658 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ea80b78-5aac-3d93-8cd0-ec9a1c05e00b | -12.66312 | -47.70871 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e39bfd17-b518-344d-adf0-a9ff8564c923 | -12.64381 | -47.95985 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d404cf4-0a8b-3bb8-8ed8-df226538c649 | -7.45838 | -46.14583 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab1d0a88-af10-3177-bc6f-51231b977cd8 | -12.83736 | -47.19842 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca62cf4b-4edf-3c03-a9dc-2df7cc4b2c4e | -8.59789 | -46.34038 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9fb136b-6654-30a5-8a02-97477b9e3ffa | -12.61553 | -47.94429 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8317fc57-8ce3-3231-8c30-1ed2ba8eec5e | -10.70969 | -46.49622 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 670d3988-c247-36a5-b0fb-d7f428d03404 | -10.7942 | -50.68134 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README45.md)
