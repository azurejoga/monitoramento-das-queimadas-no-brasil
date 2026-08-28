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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5573a2a-be5c-3a9f-89c9-e6d1de008b78 | -11.38506 | -45.14405 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 424045f6-c6ab-3081-9f85-580a626e723f | -11.28536 | -54.01832 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99d5ac28-80f9-38a4-b09a-77cad0e942a9 | -8.01335 | -48.0183 | 2026-08-28 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b97579dc-5ee0-3541-9efe-a65ff478ee88 | -13.31957 | -48.21324 | 2026-08-28 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e8ae72c-6b8e-382b-99cf-6410e3b85900 | -11.48528 | -45.07574 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d044bedb-4be1-33ed-95f2-e5d6b0d4622f | -14.39929 | -50.12999 | 2026-08-28 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de35e780-630e-3ae3-817c-6d491e30c465 | -11.75765 | -54.51907 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4dffe3f-930a-3eac-8581-33a33b2ec7f5 | -8.20527 | -47.51645 | 2026-08-28 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6842e442-2501-3589-9130-d861f016a51c | -13.595 | -45.782 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 535d0312-9d3e-32d9-83da-d2b3cc22742b | -8.834 | -49.60961 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd36360c-9cd3-3e44-b5f0-7577f1da9b71 | -14.85917 | -52.60835 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9049d4b3-f574-34e1-9493-02ffb03b2fdf | -8.59255 | -54.77972 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01907d04-f87f-3257-b5b5-27945b11f950 | -11.01596 | -49.67202 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04c34d1e-172c-312a-96e3-2ab6fecc50d6 | -12.28051 | -50.60114 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcd60343-7d50-3aaa-90f1-c6041fd46fde | -12.21666 | -54.23456 | 2026-08-28 04:51:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfed0a3c-d54f-3fe8-bc74-0a63b698b2f5 | -8.80544 | -50.49331 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b01e6e72-8fbd-3d71-8bef-34cdb9966fc6 | -14.87848 | -52.63815 | 2026-08-28 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75432a45-37fd-326d-8ef8-fde13d523c63 | -9.60969 | -55.12356 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d67b9bc-9682-3538-a6f8-5b0511fe5722 | -11.28098 | -54.02201 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9ec87af-78c8-34cf-bd6b-bf5773f73ce3 | -14.86253 | -52.60892 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86ae8019-ee2c-3445-8ac0-b79ba0d31ff8 | -13.37366 | -41.34882 | 2026-08-28 04:51:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3ed8c4f-27f1-3f08-a782-ee22ac94d112 | -9.87637 | -60.25365 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d40e2e1-54b5-312f-8232-b260fee728cf | -15.53145 | -41.92169 | 2026-08-28 04:51:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 48321be3-34ab-35f1-ac49-f9c5e6c4c251 | -11.19286 | -51.22739 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4d517b1a-3f3a-3001-9f25-c3603bbc4a04 | -13.45599 | -54.02258 | 2026-08-28 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b110f4b-fbc6-33f4-8546-536ba672a367 | -14.93783 | -52.59888 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7f1a077e-02fe-3617-b2ab-b1ed66093d1a | -13.60788 | -45.78014 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c880e97-76dd-3faa-8883-864cc7a608de | -11.47067 | -46.94575 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7bbd75b-32c2-338b-86de-532e3b6dfecc | -12.25058 | -50.57452 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f8b80ae4-7516-362d-a9b9-29be4225376f | -14.59798 | -53.15458 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19bd8410-d046-32da-89ec-c8e8448b65a7 | -11.57376 | -45.52891 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9328c89-585e-3a41-960f-3cd7ddfaf373 | -11.28973 | -54.03695 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8af03893-d8fb-33b8-b881-ed44b4a07ccd | -8.58859 | -54.77905 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f215860b-4663-36e6-b759-a09028a4ac9d | -11.28316 | -54.0313 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 71fce2d5-0f34-36f9-af1c-4695b342d6c6 | -11.01484 | -49.6572 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db186748-de15-365f-b150-c1037406f4ea | -14.11774 | -44.38939 | 2026-08-28 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d730ecee-9b8a-316c-a8d5-1d0857b80a07 | -14.59673 | -53.16216 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb1a7d3c-88bd-313a-933f-8478a77fc3ba | -11.72028 | -54.53562 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7dde8c38-6441-3d77-9305-21a670b594b8 | -9.22528 | -51.57359 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 306b2dd8-8fd4-300c-802c-0a3df85862fe | -8.80387 | -50.08099 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 238dba68-b42a-34e6-9cf0-bba106cdadd4 | -14.15116 | -52.83267 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3254d07b-ec00-391c-b6dd-6ebd405a19bf | -13.32138 | -48.20106 | 2026-08-28 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 999282bb-af0d-3e72-8611-116dfcceabca | -8.6123 | -54.73635 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4e632b6-b422-3a5f-aeae-b7355a19f989 | -9.45209 | -51.70679 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f94811e-4b2c-3af3-80c6-7e5f2a4b19bb | -10.01298 | -46.41312 | 2026-08-28 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a141ef3b-646a-37cf-83fe-69fa9115b2d4 | -13.61252 | -45.77696 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59548399-ed8d-3b9a-ac7f-d33be6487bb9 | -10.88281 | -50.51973 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a296177f-d38b-3143-9390-aa0f8ce608ee | -10.78022 | -50.6329 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2722d1f2-1856-30c0-b835-98c0c9e65c11 | -11.48949 | -45.07626 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf4e9a40-183b-32f7-a100-2d9bde0aaae3 | -11.72478 | -54.53178 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c9e755e-6384-3b58-a38a-6175d18587d8 | -10.93998 | -50.53959 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 827b8021-b812-3a93-bba6-9058f973200a | -8.59655 | -54.78893 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 337dd80b-c78d-341e-ba75-2faf74393386 | -9.15635 | -49.96944 | 2026-08-28 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67c3f95b-c54d-36d1-85dc-3848716eb994 | -14.19305 | -52.83221 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23cedef5-aebf-3045-8b15-29d583cd479a | -11.5717 | -45.51361 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3400c17c-2e02-3ce0-b3c3-addf88efcbaf | -9.97256 | -53.93599 | 2026-08-28 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2f5ab153-17cd-3a57-aa4b-9b9af670c28a | -11.22989 | -54.01312 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 62575421-7c0f-3a7f-8ce3-e227b89d1eb8 | -8.61811 | -50.0158 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b46a0e9e-7878-3d30-bde1-6ce5a0516434 | -11.53951 | -45.50949 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58c3f8f0-f282-3a5a-9992-996842b1469b | -11.21827 | -53.99332 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afc96386-369e-3c7f-8db1-e0eee5355b65 | -14.8991 | -52.59633 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 374e2424-d652-33b9-95de-fc5b6a8878ba | -8.76718 | -50.49791 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a90d192a-eb41-370b-88df-0d08ae79a8be | -13.42184 | -51.86563 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 652c1352-547f-359a-aa4f-79bc4d3251ee | -11.83443 | -47.21786 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5d30296-7077-31bf-bc46-7722417c955f | -11.72914 | -54.55119 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85633867-c381-336e-b8c2-51795727d531 | -13.32199 | -48.19696 | 2026-08-28 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31a826d7-f8a7-3307-a470-711e0cc57b8d | -14.90738 | -52.60907 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 233aa6a8-7863-37c7-b8f0-8855b8d4195e | -14.87104 | -52.59907 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03aa35f7-b8e6-3245-bcd2-ba4fc0c9131a | -14.86133 | -52.61626 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 588c52a7-158b-3dbe-aea9-39169ebc3ba5 | -11.49062 | -45.06827 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88bf1c95-d7f9-3651-9a37-34a720e50985 | -10.98771 | -51.09201 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8df78a3c-c294-3173-8766-b0ea511d5747 | -11.83508 | -47.21348 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3fd17e4-2c11-3520-a868-95f97787a507 | -8.80663 | -50.08501 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd898598-5efb-3ff5-b478-82fc24481b63 | -9.96887 | -53.93535 | 2026-08-28 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 57e60dad-1212-3d88-a67f-81b86e478852 | -10.79284 | -54.01018 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d0ea3f9-0ccb-3acc-8bcb-f823c80a1e9a | -6.82128 | -55.61333 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 511e8ad6-4915-3957-b881-93dfd826084e | -11.2766 | -54.0257 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 07e0834e-ada7-3a21-85b9-d91107505dd4 | -12.63566 | -48.407 | 2026-08-28 04:51:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e24b085-1d3e-3335-b85c-3dfa81b57949 | -10.50574 | -64.51704 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 7bb1c9dc-dee4-3a42-84af-8197a0b3bfa9 | -10.98551 | -51.08441 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6def0e1a-a09b-32a6-bafe-a809083e3eed | -11.19669 | -51.24617 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5720991e-887c-3bd0-9e24-138c820f6d56 | -10.93721 | -50.53554 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 97d25774-b98c-3476-a6cd-13bbfcc96e0a | -13.60015 | -45.77504 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3b77fbd-840f-35cc-a5af-a1637daf7bba | -10.31856 | -49.97932 | 2026-08-28 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52e17df2-2403-34dc-83a5-c386e3e09b59 | -10.90883 | -50.52756 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab00ea6a-e15a-331c-be9b-01d78b975c34 | -11.19896 | -51.23202 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a56f13b5-b0ab-3be5-9608-25efdcb504bb | -14.86529 | -52.61318 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 93b36a2b-2feb-3e5d-9d54-692fb0400008 | -10.02916 | -46.40324 | 2026-08-28 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea2df43c-35c0-3fdd-a1f9-5f12956d0bfe | -6.76362 | -55.69192 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5857cda4-b016-3def-9884-d8bd7ab4580b | -11.27002 | -54.02016 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45465edd-f138-3e83-b466-3e02a112a610 | -10.98714 | -51.09554 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2bc6b63-a766-3505-82ec-7561149f911c | -8.1871 | -47.54157 | 2026-08-28 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad5d724c-3d92-3e09-b0ad-36603a466b8d | -10.8385 | -50.51975 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f9474aa-d40b-35d3-a0e0-82a599735fe9 | -13.47817 | -57.04947 | 2026-08-28 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a54260b5-0127-301c-ad25-263b22df8a20 | -9.45601 | -51.57681 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b41b6b69-ecb4-305d-99f3-bc9a0d9809ea | -9.21193 | -51.54889 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 999ce2d7-2fc8-3b1f-91d3-4ab785dd4bb8 | -12.01567 | -47.16777 | 2026-08-28 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abe2f5cb-f3fc-3ef6-8159-8ffc23af2bc1 | -9.87721 | -60.26085 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88160798-3fce-37d0-9eb4-5d7b792455ea | -13.60839 | -45.77633 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f25edb48-efe7-39c8-9741-e608eb37201f | -7.51213 | -61.39517 | 2026-08-28 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README40.md)
