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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5410335-fa9f-3490-bd72-f06bef2fcfcf | -11.32889 | -45.4563 | 2025-06-12 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f42c5c3-2704-3c28-affe-934d8335f686 | -15.37072 | -47.87269 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64fd03ea-8d77-347d-9b7a-9c4c483e2340 | -14.0379 | -55.13538 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 388583d4-09aa-381a-983c-0273db71be5b | -12.27992 | -57.27256 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b4effe9-681d-3845-bc6a-73e12d96e797 | -10.11141 | -58.22355 | 2025-06-12 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81671113-c383-3e62-b98c-d4f95c60b89f | -13.29133 | -57.08345 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 90baf77f-6f2b-3fae-b494-e6a1bb7d75b6 | -11.99694 | -57.21399 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e956b0f-9c1d-3a42-8d1f-78f1bf876cdd | -15.36953 | -47.88177 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9fbd9bb6-0e6f-3e3e-8892-4d9af37fdd40 | -15.38169 | -47.87703 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8716b33-1748-3211-bbd8-fef67b98d952 | -15.17642 | -43.06524 | 2025-06-12 04:51:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e7e41e5d-3e45-3949-8ed8-6f804f76336a | -11.61181 | -46.99005 | 2025-06-12 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4eebdb51-3846-3c96-8a99-33668427a527 | -13.28848 | -57.07867 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b19f94d2-ecf3-39b9-a1e6-54036ba6b91c | -14.84735 | -48.31324 | 2025-06-12 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c6ba10f-144e-3ad1-ae7c-812f725e2158 | -11.56985 | -51.31332 | 2025-06-12 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4154fd99-5d6e-394b-a561-c45a184b617a | -12.82576 | -47.38141 | 2025-06-12 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 346e00f0-1d5c-3798-b7fd-fe65cc7a8ee1 | -14.82398 | -54.65916 | 2025-06-12 04:51:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adeb5974-7c75-30fa-8933-1f2e10f40659 | -11.60857 | -46.99243 | 2025-06-12 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25d7b795-ac52-3960-97a4-979b4fbea84d | -11.38242 | -56.54875 | 2025-06-12 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fab017cb-761f-3f23-9f53-0de605c3443f | -15.17586 | -43.06684 | 2025-06-12 04:51:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 56bb1130-c729-3219-bd62-e854eabb6622 | -11.58129 | -47.4417 | 2025-06-12 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64ca265b-6ba2-3297-8196-2e312eeabbe1 | -13.4678 | -56.85429 | 2025-06-12 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55a8f344-2351-3b71-848a-dde0a4bcf2f1 | -12.51857 | -57.23641 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9e93332-1817-32d2-8b7e-ce3bafe3c82a | -10.66143 | -49.4201 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5269477e-c42b-3f2c-9709-f758746fd477 | -11.9204 | -54.82066 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03d299f8-be25-3fab-b5d4-27044c357685 | -13.29272 | -57.07521 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 830b6060-aeb6-31ea-b216-96ee2a13b273 | -10.24152 | -52.23585 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1446ddd8-ee14-3a39-8af1-fb95b3fe4cc7 | -15.37521 | -47.87331 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09734628-23cd-3002-9db6-2650b916aa23 | -11.74992 | -54.71964 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ab8a7f1-6c97-3dc4-ba26-9f7dc0640636 | -11.56811 | -51.30094 | 2025-06-12 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01fe32e9-f4d2-3d4b-98f6-b75c0477becf | -10.36238 | -57.23489 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7f56741-1ad8-3a6a-814a-1f8ec46cbc16 | -11.37819 | -56.55222 | 2025-06-12 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d08cab7f-2508-321e-983f-94f7e2c9d6f1 | -14.03124 | -55.13425 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60eda98e-8514-3088-8e79-dedf25f27dc7 | -10.36466 | -57.49944 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4768c364-8196-3c05-904e-a0ac2c4254e2 | -12.70257 | -58.02629 | 2025-06-12 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5107dab2-dace-3af6-a823-1be39d312f87 | -12.51424 | -57.24004 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53d1c331-b9af-3a1a-8acc-ce4809b49a14 | -10.70309 | -49.50774 | 2025-06-12 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72e50513-b296-353d-ab26-cdcf6aeb631e | -11.57043 | -51.30938 | 2025-06-12 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28c401f4-4356-3f45-9c3a-8390109c4960 | -14.84592 | -52.28466 | 2025-06-12 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdb0b67c-b2ac-3ec4-aac3-e091681260ff | -9.25119 | -57.53455 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 61c428eb-cbee-3020-b96d-b1623d0cd0b9 | -11.06555 | -55.04654 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fec8155e-0d05-3cd6-be2e-6998418aab2d | -10.94602 | -55.31246 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a00f0e7-feb1-3e9f-b803-fa1eaf4e978f | -13.89571 | -54.64393 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 01dc7802-f938-3163-bdff-95a69aed72d3 | -10.33481 | -57.49189 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c0601cc-b3fc-31b8-867d-28c2a7926f88 | -15.38511 | -47.88625 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2a7c957-1b15-3731-bb86-e5d8484f3f3f | -11.0093 | -49.57919 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bb0232a-32cb-3618-afad-a5e35889d0c6 | -12.76855 | -44.40751 | 2025-06-12 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8577d0c-8cd7-3e33-83cd-ba1ab86aa76b | -12.43259 | -54.86868 | 2025-06-12 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b33677a-7fc6-3553-a698-cba11c52f23e | -9.87452 | -61.39932 | 2025-06-12 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5e292c7-57af-3e10-ba25-d04eea68aab9 | -11.76841 | -54.3697 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb392362-c3a0-32e6-80a5-8f405477fcb7 | -15.37664 | -47.88097 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e0d82fa-3b32-3bd7-822a-8be177359b67 | -13.48993 | -53.48702 | 2025-06-12 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa00d5eb-5121-31af-8f35-5c6dc5cb9a88 | -14.42306 | -47.89317 | 2025-06-12 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0451da21-1674-3cb7-97c2-10b69c97043b | -10.65001 | -49.41841 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e7e5e7f8-d875-3ced-950a-95efadee2904 | -10.70172 | -49.51708 | 2025-06-12 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ea5dcba3-877d-328d-b9e7-a4457830d45c | -12.52651 | -57.23343 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 933ea62a-0935-38cb-961b-c209502f6a3f | -11.80621 | -56.96548 | 2025-06-12 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44edaf9c-0d3f-368a-8219-286b989c4670 | -15.56925 | -47.85615 | 2025-06-12 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa005fd7-58de-36b7-8786-d4597e466bbb | -10.99741 | -50.76141 | 2025-06-12 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a5fcc65-7c3e-36af-a794-26e0cb236879 | -15.37214 | -47.88041 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2275b45d-ced5-3579-b2c6-4ce6740697d2 | -10.07149 | -52.74411 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e91b8bbb-c4a8-3b7a-99d3-dc3964b4fe62 | -11.9904 | -57.20845 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 05796bcc-3a74-3c42-b9d3-e605f7b7b0d7 | -11.83507 | -60.9183 | 2025-06-12 04:51:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbe37560-1396-3bf1-85b8-d368ad963ac0 | -10.40746 | -54.84581 | 2025-06-12 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d2a5ae73-e340-3f07-b5fe-bb2fa1d77012 | -10.94821 | -55.3204 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d842556-6bbd-3078-b7c4-84a37823f1a3 | -12.65123 | -54.07316 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09306979-472d-39d1-9a78-d5e9cfa55ec3 | -10.65806 | -49.36164 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f76a0a08-de58-35f4-b206-b7073cb5d6dc | -13.79667 | -54.3041 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ab7feca-0ba4-3062-97ab-b74190f6c82c | -13.7136 | -58.67571 | 2025-06-12 04:51:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64d3531b-5cb0-3a61-8d3f-bdcc9544d4b5 | -13.29063 | -57.08758 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cd6cf430-6d25-34d8-86c3-8629e69be6bb | -9.38978 | -57.52193 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26dc2e42-6550-39c9-abfd-e4b3c65e645f | -13.89126 | -54.65047 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 16ba3a70-892f-3839-974f-7d3c94f1d13f | -11.00864 | -47.76269 | 2025-06-12 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49ddeb3e-3b81-3d57-b672-dc613246b5d5 | -11.99113 | -57.20415 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c1eaed65-059d-3e1c-b0bb-0fbe0643a8e6 | -11.57451 | -51.30595 | 2025-06-12 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d8011a6-6f82-3b3c-8c2a-46c3410e9804 | -11.86648 | -52.25446 | 2025-06-12 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a45f2c0b-9a3d-36ed-a0df-e297b1fc9709 | -12.72494 | -54.97235 | 2025-06-12 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90fdd65a-7a50-311e-8aa4-05bb08a82ce8 | -13.29203 | -57.07932 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb3960c9-c1d3-3912-8aa5-045288cd767f | -10.88542 | -54.74994 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3ec7af2-c862-3ac0-a8b5-f082fb9ddebb | -9.18242 | -61.86481 | 2025-06-12 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3a081fa3-266b-3b23-b586-1c2f63e8f8fe | -9.24819 | -57.52908 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c085846-3534-3383-be96-4fd26f79f69a | -10.87845 | -54.30345 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ce68114-9604-31a6-a4f8-3e18057cd21d | -10.29831 | -57.14081 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32f9cca5-c912-30d2-a658-bf46097be889 | -10.88427 | -54.75713 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6183d5a9-b70b-32f9-b556-6e09bb5d1859 | -11.14052 | -53.91742 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 976b4ef2-0977-3ad4-81c2-23cbebbe1bc8 | -12.7085 | -58.0368 | 2025-06-12 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6cc2a11-52c6-349c-8ec2-92c7c7f27ae3 | -9.87735 | -61.39529 | 2025-06-12 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60752349-9aac-3f89-8894-6f923de923c9 | -11.1361 | -53.92389 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 280519ee-8b30-3d0f-a258-d41a8ec868af | -10.87873 | -54.74884 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 15d58831-23bc-3f92-8d05-3988a8ec63b9 | -10.99089 | -50.7562 | 2025-06-12 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 554a90bd-4542-3c54-a746-ea7b88f476b3 | -10.87931 | -54.74525 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9539a038-7384-3577-a40e-79810213cd20 | -11.77448 | -54.37432 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c68ffd7b-ee30-365b-9d21-5e88c3e76274 | -9.38896 | -57.52672 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00242d7d-c5c6-3251-90b4-32d1a6392a29 | -10.65873 | -49.3569 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0436b237-9897-3c8c-b288-e4fc11fcac61 | -11.84534 | -43.80072 | 2025-06-12 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ac93fa3-5b67-3677-85c1-aa81a20dbde1 | -12.23245 | -44.16501 | 2025-06-12 04:51:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30345c21-7bbb-3a2a-a4ed-55fbc169d326 | -12.10731 | -48.87263 | 2025-06-12 04:51:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e30401a1-a650-391e-b441-d6fb1f3510ce | -13.65364 | -53.93955 | 2025-06-12 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 829a6827-4bd0-3d08-a6d4-26a9004bc45a | -10.95099 | -55.32467 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db195052-e9f8-3836-81d9-680488a320e1 | -10.65695 | -49.42431 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 53b8cbcb-5f3f-3065-8560-dcee94917ae9 | -12.72827 | -54.97291 | 2025-06-12 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README19.md)
