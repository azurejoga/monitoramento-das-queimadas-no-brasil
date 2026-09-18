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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6fb8eee-1321-317b-b36d-ab2869c073b2 | -10.65053 | -50.24515 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fcd1425-1120-3e92-b70e-426efccbc459 | -8.74099 | -45.40859 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3429c4f6-4e4e-336a-9145-0ad777316f9b | -8.90358 | -45.01859 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7e6dabe8-b830-323a-8d47-3fc9e1b28bc1 | -9.75893 | -46.09644 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 961f18e6-7b6d-326a-88cb-11feb285f9b3 | -8.44288 | -45.70233 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc7fa0b8-704e-3b62-bda3-9511240e4fc1 | -8.7815 | -46.89504 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2be31a77-fee9-3657-88bf-25212192af0c | -8.56183 | -44.89633 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e06cff43-3070-3705-93b0-a14cfb6a1f69 | -9.62122 | -45.30341 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c44bb01f-7acf-39b3-924b-6df7dae9ed6f | -11.1066 | -47.10207 | 2026-09-18 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c150bb3-95d7-3e68-8670-3c020943b7fd | -12.21181 | -53.21664 | 2026-09-18 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| effb2b2c-a3ac-3740-8b12-44bc0249967a | -9.93466 | -46.53471 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 274b34e9-e2ad-31c0-a807-118f44fd9c51 | -13.24811 | -46.90271 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1beab21-eed7-3162-8bba-a5518d664eb6 | -10.88949 | -53.99653 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 41255e12-228f-334e-bd02-98b8fe4cc1e0 | -10.67039 | -50.26866 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| df1cd5bf-c70d-395a-8348-2fc6a678637f | -9.54236 | -45.45859 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af943be9-0754-332d-9059-863752f39212 | -9.93898 | -46.59361 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b002d7a-9654-36ae-a407-6d874d1892c8 | -12.38615 | -48.13785 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c1b877fc-905f-321f-bd7a-e9e7e3eafc2c | -12.56341 | -50.74015 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1086da6b-7285-3191-b374-fda335ae00c1 | -10.0279 | -45.57489 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4798b541-33fd-387d-82f4-4a457e296d85 | -9.54837 | -45.44173 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e66b49e-7405-3af4-89d9-ad33943c49ff | -10.54463 | -44.84768 | 2026-09-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa870ede-d2a7-3e89-811f-5aa8c82f39a3 | -12.32157 | -50.83067 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4e55ae1-a1eb-3571-90df-96e23a80ec6e | -8.48862 | -46.87819 | 2026-09-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 561e5b88-f067-33f1-af3a-eeff8eaf9624 | -10.61773 | -46.06619 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0a02268-af2b-3e19-975b-6618c8a83692 | -12.41152 | -50.70347 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd1f344d-59ea-39d4-98bb-f7fde1608492 | -10.03228 | -45.56845 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c634a23c-2f9d-32ae-a63c-96c6b759ced1 | -9.92515 | -46.5732 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9c13cec-3b6d-3b6a-b32b-140df3f9923d | -12.99991 | -46.92378 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad88e114-6388-376e-aa70-3583370be950 | -9.92572 | -46.56963 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ef815f5-322e-3330-8d8f-4b1352577c65 | -9.74073 | -46.12582 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af4d6ff0-61b1-3a7c-bf9d-9330164f1707 | -8.93164 | -51.45993 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a6b51c0-4877-3ddc-a136-39a9f3a14492 | -11.23107 | -43.43055 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 432f485f-89a9-3372-8a0a-75573ee75e15 | -9.95506 | -46.5998 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c2570af-6dba-3bb1-92e1-b02fe73fb29c | -12.4787 | -50.69245 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c21ef04f-9a20-3d35-92bc-fb343a0785b5 | -10.59939 | -46.54859 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cd102e0-df6e-38bc-a421-b4658dace11b | -9.71298 | -47.09058 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b600d40f-f3cf-3bc5-93e2-35d6cc75d111 | -8.43199 | -45.79336 | 2026-09-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66f1a3f8-b189-312b-b379-faedc67e8119 | -10.40387 | -46.62207 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b2dbdd20-d7d8-3b89-98a3-ec571ae2cc7d | -11.67326 | -54.45062 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58e34088-b28f-3a91-8d8e-d283ac1b1745 | -14.22315 | -48.50942 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c0cbe298-0584-348e-ba94-37fa496a7d30 | -13.74385 | -48.79876 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 332e17c8-18d2-3e8f-ab49-4c8e046280eb | -12.17536 | -46.97359 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81cf71b1-622d-3ec4-9aa6-04d534b0b75f | -13.52128 | -48.94681 | 2026-09-18 04:21:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0442121-183f-3c86-a0b0-f32913cb5129 | -8.48067 | -57.62571 | 2026-09-18 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c6c0d5e-c9d2-3bd2-9fa0-67ff56af9bfc | -9.70949 | -47.11233 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c0ed7c9-47b2-3813-9970-1c748075b117 | -11.52321 | -46.85913 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8045a58-408c-35d7-8ed2-1ada692a5324 | -10.52085 | -46.74281 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 889b308d-74a5-3c8d-add1-12830fa162d5 | -12.99659 | -46.92324 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68d3b75d-d72f-351f-b9cd-8a61a7502a0c | -9.91359 | -46.53859 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 09efebf5-2299-3726-922e-d285a2f00cd1 | -9.83296 | -49.22533 | 2026-09-18 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8813facb-9f4c-3ba4-a898-079ab0a6f036 | -15.33398 | -46.03728 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9308c3ed-e433-30ce-b9c2-d94201fa7fd1 | -11.80812 | -46.80056 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 868bb284-f633-30e9-8906-ca722db7a311 | -9.83627 | -48.34343 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f61914b-cea7-350a-86e8-4ce744b7c031 | -11.29757 | -43.39214 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7507257c-728d-373d-b6b8-3d1f1f1bf1c1 | -14.77217 | -47.1627 | 2026-09-18 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1272fd55-ee47-35be-8e82-92e102746cfd | -12.55656 | -50.73388 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aed8f674-562b-390e-83dc-9dc94e18ea93 | -8.45977 | -44.50109 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26cd1ee0-41e6-3daa-930e-63d4cd6f946a | -9.72168 | -47.14418 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec40bcbf-2cee-3192-9c4c-784b0b9340cd | -10.6589 | -50.48312 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4a1e61f0-0560-3ed7-8af3-41685ecd3c04 | -8.77755 | -46.89814 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ff24c55-6292-370c-8dd5-b7011dd8e919 | -11.07524 | -48.29112 | 2026-09-18 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c7dd2a4-e9a1-3d5c-ab3b-00966268cbb4 | -11.02547 | -54.152 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcdeb310-1253-3213-9946-0872cb2b3899 | -12.25498 | -50.74902 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e490275-676a-30fc-a19b-4485454b3fc1 | -8.8994 | -44.97799 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79794529-6dd9-326b-8a23-5fde8af13679 | -10.83121 | -50.83974 | 2026-09-18 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 554eaead-d574-30d8-8091-443a8af32e68 | -9.82771 | -45.39706 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 053e84fe-bc21-361d-a2c8-cadb7c64eea0 | -10.01934 | -51.10478 | 2026-09-18 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea835aaf-a1fe-3f00-a78c-02c0882280b9 | -8.69638 | -45.40873 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb213637-a292-3b48-a84b-c2e4385f714a | -9.71054 | -54.82288 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 02414a29-3541-3dd9-a7af-cfa654dd8fac | -9.94201 | -45.31511 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a3fbd48-c7a1-3dfb-af32-31ae9da8df04 | -9.3967 | -46.854 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7eed933-2c3a-30fe-9357-9d8392ac23f4 | -9.91303 | -46.54212 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a3ebfd1-5602-3261-a6b9-4a3a439cac31 | -8.56658 | -44.53554 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7fdc3fd-ab3f-3339-a023-523d1532d87c | -9.73797 | -46.12178 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f75559f3-5c84-3c27-8757-6ccd6a20b858 | -8.77782 | -45.91017 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53fe8bdc-4964-3105-b99d-1f15a349e91f | -10.00702 | -42.47923 | 2026-09-18 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 93f937b7-b2d6-315b-bcb7-dfedf01529e3 | -11.27592 | -43.51387 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 828adb16-6872-3dd0-82ae-d95c0eb95cc0 | -9.24347 | -46.19256 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3b169e8-bac4-30fb-8416-9ca7763c4093 | -9.94242 | -45.33664 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 723f2737-38c5-3db2-87f3-f80f1154ad4d | -9.15627 | -49.99939 | 2026-09-18 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d3879c9-1682-3212-bce0-28f90502bda0 | -14.93473 | -49.91891 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ccc8b10-ffa3-365a-8dc6-e8600040e057 | -10.66171 | -50.25955 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70f174e0-381c-30e4-9f44-ff1ec333be81 | -8.5709 | -44.50736 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa60c06b-660f-3385-8d81-20643196c6d7 | -10.57335 | -48.56384 | 2026-09-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3197fd69-ea2d-39c9-bd19-0d4c2c7252e7 | -9.94011 | -46.58645 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95b538ff-75db-344f-b3a9-bcdd9aa98a67 | -9.94411 | -45.34762 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d80e5af-7051-3850-a024-9476c1c20be8 | -13.68274 | -48.59037 | 2026-09-18 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2ee6305-549f-33cf-9478-cc0def1a560c | -10.61663 | -46.07317 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 902d8baf-bb2f-33e0-91e9-f99a517a6a85 | -11.16258 | -42.78604 | 2026-09-18 04:21:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b11772cf-8a0f-3e9f-88c6-1e50498f8da0 | -12.51657 | -47.09546 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b0efa1b8-f5b4-3fd2-b373-249bb9d40878 | -9.09308 | -45.721 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b9f3a92-5023-3798-bfaa-181070a50d44 | -8.25681 | -45.63017 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd766c25-8944-3327-9813-d8d12e27591b | -13.25248 | -46.918 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7af2514a-9b52-30b2-a924-4010a1b3557c | -14.33208 | -46.6935 | 2026-09-18 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e31a11f8-5735-3591-a884-5d48508def98 | -9.48028 | -54.4817 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e7a87cb5-d9d9-3c07-adf5-b5827c6a07cf | -8.94562 | -44.39192 | 2026-09-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a53faa4a-e15c-3fdc-8461-e6d72f70cf4c | -10.61319 | -46.56895 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b7ad338-0729-36ef-8e9e-62ecc6bdb465 | -9.04266 | -47.75868 | 2026-09-18 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8adad4e0-418c-3dc7-b249-212ad3b291c1 | -8.55853 | -44.8958 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38fda16f-e846-38f2-bbdb-8996b43831f0 | -10.87265 | -54.00515 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README48.md)
