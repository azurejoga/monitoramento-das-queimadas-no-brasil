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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ab20073-8c6b-39fe-8e06-b3dbee8ed008 | -15.27363 | -47.85593 | 2025-09-30 06:16:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 661a7ea9-8a01-3323-859c-e43ee1e20adb | -11.24175 | -47.2342 | 2025-09-30 06:16:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3d36a380-83bd-3376-8557-f64f16a61f30 | -12.96311 | -48.41586 | 2025-09-30 06:16:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1bbefe6f-7984-3f58-8983-7c0d9c90af74 | -13.21169 | -47.3237 | 2025-09-30 06:16:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| eb236d6a-3ebb-3585-960e-f677ccfe6806 | -11.18717 | -47.21097 | 2025-09-30 06:16:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 8a1deb66-4c45-3222-b26e-143ada571dd5 | -11.87703 | -48.05545 | 2025-09-30 06:16:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 36243be1-bc7b-3294-aeef-341a19b8604e | -12.95811 | -48.40822 | 2025-09-30 06:16:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0a2ece75-6ea2-38f2-bb52-a232cc7f0f51 | -14.52228 | -48.37309 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0fb700d3-8e8c-3523-bb53-f9f240b91a55 | -10.62034 | -53.691 | 2025-09-30 06:16:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9a3c6976-0a6c-30c9-a37d-28424f5bf98b | -8.14425 | -46.38015 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 7fac125b-7b22-30d1-9159-e0d2deeaa9b7 | -15.38203 | -47.0802 | 2025-09-30 06:16:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 50619fc7-5fa7-34ae-a538-ecdcc61a5b44 | -14.51326 | -48.44454 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 147a8b4e-2aba-3fb6-910c-1feff1885d47 | -10.18736 | -44.89589 | 2025-09-30 06:16:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e48e39e6-ea9e-315b-87f5-aead5f1207a7 | -14.50838 | -48.45236 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 37.6 |
| ada2709a-3c5a-3d95-843b-adccc874366a | -14.51784 | -48.38147 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| da92dd2a-4a57-39ce-8e48-bc5c2e6cacaf | -11.25516 | -47.22015 | 2025-09-30 06:16:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| a12b8f1d-14a8-3970-b2f7-c9a12fbbe5e6 | -11.8896 | -48.04337 | 2025-09-30 06:16:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d53153c1-ed7e-3a33-87b4-105f5c694e47 | -10.82505 | -47.95602 | 2025-09-30 06:16:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 2256a792-9166-3e2a-8241-5ba913cb5dd9 | -13.20533 | -50.92942 | 2025-09-30 06:16:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8411c8d7-834f-3c40-bf6c-d0c96a291b61 | -15.24696 | -49.70876 | 2025-09-30 06:16:00 | AQUA_M-M | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 93ed711e-746b-3309-9d30-12594dad4516 | -15.24095 | -48.7483 | 2025-09-30 06:16:00 | AQUA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| eb56e543-7c9d-3eb0-a9b5-e22ae78304dd | -8.53483 | -44.64006 | 2025-09-30 06:16:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5e2e592c-aab5-34a8-a1c9-eacaf498b67c | -13.56406 | -48.05085 | 2025-09-30 06:16:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e2171bff-dab7-33f2-8369-7f1aca5835a9 | -10.40263 | -48.158 | 2025-09-30 06:16:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 34ee4ad1-47fd-353f-8ac7-290168f73a17 | -11.14608 | -54.11454 | 2025-09-30 06:16:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| f68d5600-f9ba-397c-ae09-659c3b90a061 | -15.46934 | -47.94133 | 2025-09-30 06:16:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 55a8cfd3-2c04-342a-8a38-682156ae902d | -9.95372 | -48.80091 | 2025-09-30 06:16:00 | AQUA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a710e72e-6f07-3e35-b77d-cbf86caaaa86 | -11.18583 | -47.22088 | 2025-09-30 06:16:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 32abed21-6629-3352-b380-bc30fb7b4648 | -10.38377 | -48.14117 | 2025-09-30 06:16:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5d60fd3a-773e-3831-9dec-00ffa5bcac4e | -12.22481 | -47.78519 | 2025-09-30 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| cbe4e274-9546-3503-8e77-8eef9c4c2253 | -14.50656 | -48.46603 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c7ae29a2-0195-35b6-b012-e8bcc1444b89 | -8.87591 | -46.65573 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f88ad637-5e59-3466-8444-60eadb670614 | -10.19029 | -44.87325 | 2025-09-30 06:16:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 681c9e63-b556-3f2c-af28-7619b49e3cf5 | -8.24512 | -45.54755 | 2025-09-30 06:16:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9796f7aa-77b7-348b-9a0e-b1a9c2c29368 | -14.54609 | -48.25343 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| cdc14501-7be1-3ca4-b057-6c3dcb8c1e1c | -15.71664 | -47.59048 | 2025-09-30 06:16:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 2765b959-ad9e-332e-a6ed-b0eebf94e8ef | -12.83154 | -46.99128 | 2025-09-30 06:16:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c3784436-68b6-3507-8537-be91dad1830e | -13.37942 | -48.05828 | 2025-09-30 06:16:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 94362a03-48ee-3342-b64b-7bd81e6137f0 | -8.24765 | -45.52867 | 2025-09-30 06:16:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 824e525d-5d6a-31df-9c85-cd93ca54f0d4 | -11.06131 | -47.80768 | 2025-09-30 06:16:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0eb95ef1-b5ca-3a34-800e-df2df632fa4f | -14.68873 | -48.13385 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 34.4 |
| b6aa0a7c-54fe-30ac-83b7-6309e8184a8f | -9.3968 | -54.70881 | 2025-09-30 06:16:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| add70f1f-945a-3e11-ad28-bd7969f90f9f | -11.15374 | -54.12582 | 2025-09-30 06:16:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| ac86f1db-25b3-3b45-ba36-f6ef371ade2d | -11.24381 | -47.21877 | 2025-09-30 06:16:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| c73b0e08-ef4c-3862-87c1-5719f9e6e849 | -8.86667 | -46.63858 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 461b363c-d310-39f6-9af7-a0c6db91660b | -11.74784 | -44.71878 | 2025-09-30 06:16:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 14ca7faa-56e9-3b75-bee6-8b1961d9a8de | -10.82326 | -47.96944 | 2025-09-30 06:16:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cea4abbf-c991-33e4-b7d3-ff3bb5e92e07 | -10.40108 | -48.16916 | 2025-09-30 06:16:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2332ec98-1b76-3c63-8587-f37d7fade6be | -14.54217 | -48.47743 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 7e0ebdba-c50f-39ad-bb7a-c3ddea553de1 | -11.87887 | -48.04185 | 2025-09-30 06:16:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1d261d81-5418-3eab-91fc-f132a66965b9 | -14.51504 | -48.43048 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a003813b-3f02-314c-874d-d80a5ebce787 | -10.18581 | -52.55099 | 2025-09-30 06:16:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b5989f9a-4c54-37ca-9dde-8dbd7782c9dd | -13.72093 | -48.68378 | 2025-09-30 06:16:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4fc87882-614e-393b-9b7f-6eb5f746c54a | -14.51876 | -48.48801 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5f810f9e-7e12-32ac-b88c-0f5d77f0d760 | -15.9164 | -46.21094 | 2025-09-30 06:16:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 30.4 |
| ba12528d-74b8-3543-9d60-f0b5338cdc55 | -14.51978 | -48.36695 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| aa08efd4-fb8d-3364-bf93-4c8ed1f89a2a | -8.66356 | -47.70846 | 2025-09-30 06:16:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 782dd38d-37bf-3641-9828-21b8f0a5b94c | -14.53142 | -48.47526 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7ca047f4-4722-3e76-b905-3041ccb6ec12 | -10.94651 | -46.51104 | 2025-09-30 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 94431890-943a-3651-b11a-393103720fb5 | -14.52957 | -48.48964 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 07d0ee8b-177f-3f05-b405-976857dc5a9f | -13.63638 | -48.02438 | 2025-09-30 06:16:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4b14b662-60ac-3c01-8170-1be6e8185e72 | -11.15529 | -54.11599 | 2025-09-30 06:16:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 835717cb-ace7-30d2-b719-be05ff4baab4 | -14.38161 | -47.13909 | 2025-09-30 06:16:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| f3e74f9c-f58e-35bb-a7d4-3b59de77d467 | -12.88665 | -46.75342 | 2025-09-30 06:16:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 395d7774-b28f-382e-9acc-a3fa5f00a0d1 | -11.17249 | -47.23426 | 2025-09-30 06:16:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ea70104c-a396-34ee-97b8-7e948f1367c2 | -11.13687 | -54.11312 | 2025-09-30 06:16:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 69af4fa5-7a2a-302a-97ce-246a1161d3b7 | -11.74482 | -44.74323 | 2025-09-30 06:16:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 07473c3a-e9a7-31f1-9b65-2c9bc3ed9d0a | -14.68638 | -48.23972 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 193801c7-5610-3f6b-91ed-af755b4c383b | -10.94872 | -46.49397 | 2025-09-30 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| d12afce6-84af-3326-a4b8-0c9d5a29d0b0 | -8.15018 | -46.25064 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9d8c6dff-2035-3333-a666-20c4924df801 | -14.51546 | -48.48191 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| d24e2b81-7c5d-34bd-a266-ef8a6303bedd | -11.19454 | -47.24301 | 2025-09-30 06:16:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a6c4cc01-ba5a-31ee-9dae-d789f937e9ed | -13.7227 | -48.6706 | 2025-09-30 06:16:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 785d3252-d094-3ca8-a0b3-09f88a0f6beb | -11.15683 | -54.10619 | 2025-09-30 06:16:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 00eb5fa4-9513-38b1-a2ec-15a18ed101ee | -14.55491 | -48.46421 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 58761481-5e41-3c55-9f9f-49398428a809 | -11.19652 | -47.2278 | 2025-09-30 06:16:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 03de806b-398c-35d5-b895-a015e7627bfb | -14.53866 | -48.24282 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ece58a14-34e9-3bf5-9b52-4a56ea8c7c87 | -9.05242 | -46.70763 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e21e970e-72fb-35bc-8524-769b27c9f6d6 | -8.86241 | -46.66938 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d0daad2c-c147-3699-a7ef-2175a30038bd | -15.91918 | -46.18678 | 2025-09-30 06:16:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 62c1e16e-1cb1-3d7a-ba5f-639d67ddc0e4 | -14.69974 | -48.13643 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d431726c-914c-38d0-904d-06593cbe53a3 | -15.27607 | -49.26051 | 2025-09-30 06:16:00 | AQUA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1d0777a1-6270-31b7-a81c-5026f4ef6cf6 | -9.05329 | -46.69775 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 54aaa071-4013-396f-a6dd-e2c6e7da6717 | -12.74403 | -46.8695 | 2025-09-30 06:16:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 87514e63-1fa3-3d8c-824a-cc59103aa76c | -15.26964 | -47.8877 | 2025-09-30 06:16:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 18026250-c4c1-34b0-8211-31b4072ca131 | -13.77496 | -47.9347 | 2025-09-30 06:16:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e82cfdbe-c848-381e-ba38-d3094a2487a5 | -8.87467 | -46.66098 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| f18bcbad-a84b-35e2-a3b7-0f809adaa83f | -14.53512 | -48.25153 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 3c5a2cb8-a5df-346f-b263-427db5a7803e | -13.82981 | -47.50133 | 2025-09-30 06:16:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 519a36ef-363e-3fea-8805-0c92db3cf23d | -15.26732 | -49.24699 | 2025-09-30 06:16:00 | AQUA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 69f0797f-bdc9-393b-a74b-0307c918121a | -12.22289 | -47.80003 | 2025-09-30 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 23da238b-7a03-301a-902a-a2b24735b305 | -11.21193 | -47.1979 | 2025-09-30 06:16:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 90e28f0b-8cd4-3a10-9075-a5f622aea07a | -15.3844 | -47.06084 | 2025-09-30 06:16:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| b2233a58-bdfc-3954-8e98-712871ef8aac | -14.56458 | -48.21556 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c770b563-2c4e-3e0e-a9d1-45fa5bae0847 | -13.56458 | -48.05799 | 2025-09-30 06:16:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 805b02c8-60ab-3e3f-848d-c7625935d811 | -11.05946 | -47.82143 | 2025-09-30 06:16:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| cefd2b04-0998-3679-b960-d775967b39b7 | -9.44551 | -50.89563 | 2025-09-30 06:16:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 02c9d24b-9962-30cb-b3c5-ce23d69a67f0 | -11.25308 | -47.23564 | 2025-09-30 06:16:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| d5256a56-05a1-3917-9a7f-07e51fc8bfec | -12.40757 | -50.19289 | 2025-09-30 06:16:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 14b56106-dbf3-3e4f-a92b-dfb56d53b3a9 | -12.89183 | -46.75964 | 2025-09-30 06:16:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |


[Clique aqui para ver as próximas entradas](README107.md)
