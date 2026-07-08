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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5860fb03-9df2-30bf-b12f-bb27c3dc1e60 | -13.95512 | -45.21545 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a49fe515-3099-35d1-b248-d491e0c89190 | -12.75267 | -44.4585 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a8d0f4e3-39cc-3118-8383-7541b543da90 | -14.14616 | -52.88324 | 2026-07-08 04:25:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 81d9b019-3c49-3282-bce7-8d3a8492527c | -14.14109 | -52.88652 | 2026-07-08 04:25:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bf3e31d6-5fd7-3ad8-ad41-606dac45d6b9 | -15.25351 | -43.10762 | 2026-07-08 04:25:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 77bd2cde-ba4f-33fa-af22-18ab0b1fefe4 | -14.14539 | -52.88741 | 2026-07-08 04:25:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8528a805-4229-3005-b1ff-0abf5edc4faf | -12.63743 | -44.64585 | 2026-07-08 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7a279d8-ff66-3fe4-acf9-68fa0dbdd425 | -13.27789 | -45.16889 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb5b9683-cca0-3c5b-abe3-5c157fd59b5a | -9.2332 | -50.14999 | 2026-07-08 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa8c4e7e-3c91-33e2-852b-648df8958f93 | -8.44674 | -45.8274 | 2026-07-08 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b662ff5-8fa4-3a50-af9c-abf2108853c4 | -13.95094 | -45.22983 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30ce7e3f-43d5-3d89-9a45-17b5f3df7be0 | -13.28068 | -45.17305 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88df9f86-8bcf-34dc-aae7-e9bdbeec9b80 | -10.9414 | -43.04916 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a4cb21f-5241-3fa6-8b12-71102445a37f | -13.28347 | -45.17722 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 721909bd-11cd-31b2-aacd-fea2788564ee | -11.38865 | -46.57916 | 2026-07-08 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6e0a9249-6ad1-329f-88a6-7937290234ca | -9.74209 | -49.02982 | 2026-07-08 04:25:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 808fa8e7-4fde-34fb-b41c-8b1a305aa7dc | -13.29807 | -54.40982 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 223406f8-10c2-3f28-b13f-e3839dc2d87d | -12.74927 | -44.45797 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ab6791c7-f13c-3b1a-9c1d-a3fc69b61029 | -12.64531 | -44.63954 | 2026-07-08 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46b3836e-49da-336b-8309-fe59a008cfa6 | -10.41466 | -46.8239 | 2026-07-08 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02fe5003-65b1-381f-b0a5-0016996c05bf | -13.28905 | -45.18553 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0335df9d-b0cd-371a-83aa-f74f51040e81 | -13.47951 | -49.91348 | 2026-07-08 04:25:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd9bff70-fe97-3996-bf6a-f998c6e2e59f | -11.04661 | -45.82577 | 2026-07-08 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 436b9aaf-260d-3141-b595-b6fa81726fc0 | -9.21719 | -48.57995 | 2026-07-08 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e4d4731-1020-357a-9b18-15141eed0625 | -13.76921 | -46.28727 | 2026-07-08 04:25:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70b4e699-c1fa-3881-9f4f-a9f25564d0ad | -8.2066 | -47.13472 | 2026-07-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2da01b5-0533-39fe-92ed-9a166b5ae482 | -12.77765 | -44.45835 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| acb4ad25-6e4c-37cc-88ef-c42962f363fe | -9.37308 | -44.71465 | 2026-07-08 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 142216e6-f3ff-3f92-9f64-9f63c753fdaa | -10.89426 | -44.31811 | 2026-07-08 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07902679-5c5c-32a9-be46-e4837e5a177e | -9.23047 | -43.15308 | 2026-07-08 04:25:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| bf5e9788-588e-358a-aec7-623f5bce25df | -12.11954 | -45.04557 | 2026-07-08 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6b03f139-a15f-373e-b343-c47feaa9bc79 | -12.75626 | -44.53144 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 3affcad4-e86b-383c-b64f-1f5adcbd262d | -13.32956 | -54.37612 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 307871d8-33cc-39e2-873b-be8f7b2a562c | -9.73771 | -49.03355 | 2026-07-08 04:25:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9e33679b-e2fd-3957-9939-9ab9a2c3f2cc | -13.28948 | -54.40216 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4cf9130e-75bd-38b7-ba77-441195b1b6ef | -13.44524 | -43.85022 | 2026-07-08 04:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f87b1e4a-7e6e-37d1-a815-d8b4b9215d10 | -13.28356 | -54.4068 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f065340d-1e68-3bdc-9719-7b8d63e30c84 | -13.29431 | -54.40318 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d97257e-23c3-3be8-b49f-cc808c4e3c8d | -10.94494 | -43.0497 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c99e2ac9-90ea-304e-ab7f-38b18e40678c | -11.04605 | -45.82927 | 2026-07-08 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e7998be-0776-3892-ad8a-cd85455d4ee3 | -12.74644 | -44.45369 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ee6f881e-3e3b-3846-85d2-f883bc4533e2 | -13.95623 | -45.20812 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 654092cb-46e0-3bf8-9b41-876669d60724 | -13.27957 | -45.18029 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eab702e9-e81b-35c1-af2c-d531c79a1b8c | -12.79184 | -44.45671 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c33f7634-19c0-36a7-95fb-a553163381ab | -13.33921 | -54.37812 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fbc0ff9-87da-350e-b3eb-53a6bb813d78 | -8.59466 | -48.0064 | 2026-07-08 04:25:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc8992ba-bfea-3732-9193-9301893e4ab9 | -12.7487 | -44.46171 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8ca29942-6920-36b3-a875-843c313eebbd | -9.30397 | -51.91605 | 2026-07-08 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd44c8b9-a96e-3288-8d4a-cbd41680fb71 | -13.14723 | -44.95417 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 130798f8-a089-3a04-88cd-668cfb46ba9f | -12.78166 | -44.47813 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3125d71a-d3bb-3363-b369-ae0231f69d64 | -12.78562 | -44.47492 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b56f51f-6b3b-39fc-9b3b-fcd9d5d44971 | -9.22148 | -48.57639 | 2026-07-08 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e41dfaa5-2622-3bcb-b3cc-ff6e5a81c922 | -9.23405 | -50.14493 | 2026-07-08 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 178bbbac-bd76-3b9f-9700-ff4b4c755fda | -9.33589 | -47.90956 | 2026-07-08 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5de74e79-8854-368c-bfd4-1e238f754559 | -12.54301 | -43.15628 | 2026-07-08 04:25:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8874b17-6c4e-3da9-967d-f9187e9fe933 | -8.59753 | -48.01099 | 2026-07-08 04:25:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| df02a4dd-ed5f-3847-aa99-24cb1852441d | -12.64137 | -44.64269 | 2026-07-08 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3d2bd42-fac3-3569-82a7-04108c37f2e9 | -10.76396 | -45.02882 | 2026-07-08 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b24d83a8-5a00-3917-8a29-52c69872c0f2 | -11.32097 | -54.48192 | 2026-07-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdf19406-b5e8-3a17-89cc-b3425b268e87 | -13.66726 | -52.19545 | 2026-07-08 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04e0a63b-139c-35bc-a465-718ede263f0e | -12.75543 | -44.53151 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ba1bfc0-73e8-3cec-8238-4ff4ffc5ab00 | -12.7591 | -44.5357 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 405b139d-97b0-3c16-a143-20fdf15fe757 | -9.37143 | -44.72522 | 2026-07-08 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2e1ca58-1138-362e-b906-ddec3f7272a6 | -13.95457 | -45.2191 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 96b4d885-0659-3be7-a935-9637c9889dc6 | -13.28627 | -45.18138 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c3c7546-bc5e-3158-b8e7-c1eb8520fc03 | -9.37475 | -44.72575 | 2026-07-08 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7d0e01c-5573-3bb6-aa73-4547896ccf56 | -8.45006 | -45.82794 | 2026-07-08 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b499bc9d-ea55-3761-8e16-e7a11b7ab9a6 | -9.22506 | -48.57707 | 2026-07-08 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0a4a0212-8ed8-3b6c-83c8-407805c44001 | -13.29607 | -44.6171 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35baa539-2705-3726-8c0b-ff8ce2a2218e | -13.29912 | -54.40429 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0844951-fc12-3224-b538-622c86465b04 | -13.53801 | -52.93818 | 2026-07-08 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| be676faf-bd56-337d-89b9-f7539b28e369 | -12.36128 | -47.41875 | 2026-07-08 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1dcd644-3606-35dd-add1-64ac9135d6ed | -15.81029 | -41.89909 | 2026-07-08 04:25:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 820f5251-b30a-3f07-9d5d-04cd12f1abbc | -8.372 | -48.23147 | 2026-07-08 04:25:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33314b8b-4ed4-3cac-b28d-70d0788bcc52 | -10.76341 | -45.03236 | 2026-07-08 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81a5270d-6fa0-34f1-b360-b8d63554297e | -13.28013 | -45.17667 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83d0184e-367c-3c05-aa40-ff7ee2849c6e | -13.27845 | -45.16526 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c679acfc-0d9c-38ba-a319-6a634fb838df | -8.73323 | -49.44661 | 2026-07-08 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 60fdf936-1d43-392b-a474-6acd45138c93 | -14.73661 | -47.14983 | 2026-07-08 04:25:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 105de95f-b994-3ac3-a6c7-2c55270bb4e2 | -11.99283 | -45.13932 | 2026-07-08 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60d3f329-4bb1-3255-a9c9-1e0bd7b88bc0 | -9.22009 | -48.58472 | 2026-07-08 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 76607c59-b77b-32c2-a1cc-03d510675b37 | -9.37253 | -44.71817 | 2026-07-08 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8193fff4-faf9-366b-9741-3df9474596fe | -11.69902 | -44.13704 | 2026-07-08 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 691c403f-4774-39d2-8708-21918fd3a01c | -11.99228 | -45.14289 | 2026-07-08 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f4d9711-2588-3316-8269-7a817acd18f8 | -13.28236 | -45.18445 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f818a885-1875-370f-a293-86f765b79425 | -11.69561 | -44.13651 | 2026-07-08 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 823b4d5d-7a4d-308e-897e-33b4daae8bfd | -13.44465 | -43.85421 | 2026-07-08 04:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f93ec3ed-4357-323b-8259-02682c0e676e | -13.94702 | -45.23295 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f6f7d0f-6744-39da-92e7-c667ef508779 | -13.27764 | -54.41142 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b66c183-e665-3c84-8717-64ffc6ed5f01 | -13.28463 | -54.40122 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14f6c109-addb-330e-874c-2b634b0bf97f | -9.21649 | -48.58414 | 2026-07-08 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ea2aedab-432f-3cfd-a974-02f255361498 | -13.53925 | -49.30475 | 2026-07-08 04:25:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2f90abd-8fb3-3974-8a5f-e320976ed119 | -9.3764 | -44.71518 | 2026-07-08 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c28dc936-66ca-3859-a48d-535865a37c1f | -12.79074 | -44.4872 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c3e92b5-89e1-36ac-ae23-d4809f84aa7a | -9.28505 | -49.58256 | 2026-07-08 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 520090fe-6aeb-332c-80af-70057ce14c2a | -13.33229 | -54.38823 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07d80e30-2473-355a-af27-9ecd52059475 | -13.28841 | -54.40774 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ad69eb8-cb8c-38ba-968d-d735e9afc811 | -12.74984 | -44.45422 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 4e5dc886-804a-3676-bd48-78c6510f71c9 | -13.34403 | -54.37917 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bef31b9-e357-330d-aead-6da8fb53013f | -9.37198 | -44.7217 | 2026-07-08 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README17.md)
