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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ea38ec2-b3fd-3232-bac3-dbb615d8598c | -11.94519 | -55.91713 | 2026-09-19 04:40:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ff021d6-0de9-38d7-8445-df5d92cf1c08 | -11.32468 | -47.35926 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a4f35d1-3256-3fb9-8242-7f4acf60c3aa | -10.52457 | -46.71077 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21a06227-ebaa-3fea-a42c-aaacfffff146 | -11.11182 | -49.46395 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e90750a-a23c-3be2-b024-93962d90d159 | -12.5949 | -50.8866 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 982c7b3e-e5b5-3946-a13f-0833e442a564 | -9.83526 | -49.23596 | 2026-09-19 04:40:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33e4e68f-242e-36d7-a10d-9412c8df9ec8 | -9.96684 | -46.60052 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b860bd9e-16a0-3a43-ba8e-2fda41667f89 | -13.68686 | -48.60629 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d6ffeb8-d935-3a46-9a1e-1d99e1b00262 | -13.24016 | -46.9124 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf03281e-0e1c-37d3-bf6c-511637bc7888 | -10.87683 | -54.06602 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9003250f-5d40-3714-b6b2-d7650129c1ba | -13.00614 | -46.93861 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06959a7f-b250-308f-b73f-34e68696ba98 | -11.04273 | -48.31187 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 743d3456-c76f-33cb-9d5a-9fcd50f51527 | -10.98271 | -48.29134 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33385724-7730-3103-95e1-24655d29a66b | -15.02815 | -48.57332 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e151d2e3-425b-3155-87df-5199ad4e94a9 | -13.6174 | -48.32315 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a116607-3cef-3375-b833-b60b095f8aae | -8.42445 | -54.72628 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b3274e3-dc0d-3510-aa7e-8faaac846aaf | -10.59179 | -46.60265 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4375266e-7432-3fab-838d-e90da0fda013 | -10.36344 | -48.89619 | 2026-09-19 04:40:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 863cc294-7aa7-3a3a-b75c-2dd5440ae380 | -14.95582 | -49.93426 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34c7d072-b54d-30b2-a068-98128d7c0306 | -9.02704 | -48.73227 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 533e72f7-c21d-3020-a280-fc741709e019 | -8.7736 | -48.68369 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57ca0e8d-d9b3-3761-9152-d12c80218def | -8.41928 | -54.73187 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9484667a-d691-3d45-a193-e848b599fdcd | -14.50912 | -49.61295 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52bde3bf-d4cc-34ca-9f0f-c645992f8ec6 | -14.95178 | -49.93743 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3466e2cc-3bb0-324d-8c92-98f807439156 | -10.62716 | -46.05548 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 795578fe-5e6c-3efd-8543-6591d5b55c4c | -11.49674 | -50.73248 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40cef5b6-38a1-3127-b1f7-f6e1900eb0bd | -12.27534 | -49.16928 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 038cf143-8190-37ce-b001-a1cde9d322ef | -13.74182 | -48.7887 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15645701-799e-3fe3-b56f-13a9448fd2e5 | -10.53469 | -46.74899 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bfc43cf9-daa9-325e-be0f-d52a5d3bc1c7 | -10.45286 | -51.23392 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7959cee2-153d-3f9d-af73-ec0583386c1d | -15.4562 | -52.81997 | 2026-09-19 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88b8c06d-be42-3eab-8a18-73c3544cbecc | -8.77201 | -48.67182 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f9df77cf-2852-3f32-abf4-8053ae3645e4 | -8.76858 | -48.67125 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2038ccc0-9628-3d0c-8390-ad1d52bd622e | -14.68807 | -46.67803 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf9fe18f-c656-355f-a9a3-87d4822e31b8 | -9.90819 | -46.50103 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b6256f2-8953-3689-8443-9d5a73af9640 | -10.91744 | -48.417 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 016bf872-d6de-38e5-87c6-601f877e1a1b | -9.19563 | -45.77708 | 2026-09-19 04:40:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51edf11d-2bac-317f-b20f-c1c8d841d49a | -10.17531 | -48.52921 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a2b51d4-f9cd-30e6-9035-2e9ffb36773b | -9.72692 | -48.14826 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 837273f7-4558-30f9-85bb-26a3164d92ee | -10.71821 | -50.60727 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5b0235c-0ace-3298-ba47-f658ce52ae14 | -7.60251 | -55.69921 | 2026-09-19 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3685cf6b-f0ac-3c41-b260-e6795cd35408 | -14.40097 | -47.27565 | 2026-09-19 04:40:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 490d21fa-b3fd-374b-91af-945ddbffcb9f | -14.79562 | -48.54506 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e17bd65-a342-31a4-9835-f2d981f5e106 | -9.03453 | -48.72964 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ae5d6f5-a031-35ee-bc45-7eaa67e77cd4 | -11.22302 | -42.82899 | 2026-09-19 04:40:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 92b6e6d2-a136-33d2-a8fd-59d8406a7321 | -9.32347 | -48.17876 | 2026-09-19 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b535d361-3df7-3846-b91b-5051171882cd | -11.33522 | -47.35737 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c904b18-6f03-3a3f-ae5f-40c3af829cca | -10.89521 | -53.98959 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fcf4501-9765-30bc-afd3-0ed6f390cd7e | -11.11446 | -45.2874 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78f422cb-a1f8-3e0c-861b-33ce8fd2c52a | -8.98773 | -50.17319 | 2026-09-19 04:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0102d304-9e1e-3e33-b070-58b5057fc236 | -11.7978 | -46.82672 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5c862a2-15ed-3675-a791-f0e08f4e7826 | -10.53412 | -46.73084 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37dfe287-1413-30dd-ab53-e500381fc5b4 | -14.68919 | -46.64762 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01768bec-fcc0-3d28-a64e-e2e3538429cf | -13.87406 | -48.59686 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 624806d1-b988-3817-900b-f5823acaa0e4 | -12.93003 | -44.55568 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 877d6ea7-b0fd-3fe8-9fbe-b2e843e5d3b8 | -11.04725 | -48.30527 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1252a0f0-090b-395c-8d09-4be5b328db32 | -9.99683 | -50.27928 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94b60fb7-7590-360a-8b0f-b3383e1bc9b0 | -9.56294 | -46.56863 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3062293d-ca9e-367f-9781-8e0a0ff9035c | -12.13031 | -46.98526 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2ccbdfa-a2a6-3e29-8610-9b5e63ab0cbb | -13.63024 | -48.30698 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e36e058c-eb52-3192-9052-b1940695b882 | -9.92016 | -46.57134 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4da3e74-fb9a-3e5d-8eaa-736ba7b78713 | -9.73144 | -46.13941 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6f15c66-127a-33c4-9860-63aa8419916b | -10.92688 | -53.96761 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7844a99-7940-3912-ba65-3491f91b806a | -7.7538 | -54.75052 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10aa40c3-f8a9-35e8-9bcd-765dbcaf3615 | -12.1331 | -47.01125 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a91d1f43-9c4f-305f-a9fd-11a0b61f36cd | -9.88988 | -46.55219 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d105073-e735-3f33-b39e-e0313735b686 | -11.10272 | -49.45451 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db634e46-3f91-3584-a12b-fa0ade71ac16 | -12.73838 | -47.01686 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f748c71c-1c64-3059-aa06-6acf647f001a | -13.58396 | -45.47169 | 2026-09-19 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9503a661-b4ad-3938-a38d-0814bc6e61de | -12.55131 | -47.08184 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0af6d6b6-12d4-372d-8722-b8f4cf4a2e65 | -9.74591 | -46.09077 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87e46c08-873e-3038-ae72-9e92c0d4df5f | -10.88504 | -54.07215 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88aa7d37-49a4-3d70-a294-d90549ad4d53 | -12.58744 | -49.10029 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2b7e02b-c361-35a5-b692-f6186132f352 | -10.31638 | -45.31546 | 2026-09-19 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c51cddf3-342d-3177-a95b-1a8b4a82846b | -13.7367 | -48.79911 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30a6be55-b525-33f1-a2c5-682528ddae3f | -11.82502 | -46.79786 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eed9008-e924-3fff-a903-da23c1eef99e | -11.08093 | -48.28868 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f30a5f82-faca-3558-8c82-bd5dd4f3d509 | -13.60797 | -48.31792 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0813539a-5778-3714-939b-b6425b3c0e54 | -10.52952 | -44.84563 | 2026-09-19 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1840444-6538-3b90-a604-083705ccb23a | -10.45156 | -48.67956 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b90f835-cd12-3473-900a-aa4d765106f6 | -10.82648 | -50.16026 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b44a3d2-4edc-3db7-acdc-c68eb14f0b1f | -10.93166 | -47.91399 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a955053f-5d60-3431-ba8d-18640d2e0e00 | -10.46026 | -51.25879 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 80ee3a57-3711-39f6-84b5-7ad778acbbb2 | -12.38752 | -48.47871 | 2026-09-19 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c25fc585-4478-330b-bc81-0d30ce9ba34e | -10.20188 | -46.59121 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76d2f1e6-07a6-316d-b250-de56a49a720d | -12.33417 | -50.72816 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be849a97-1b17-32c8-aadd-d8d2cc286d68 | -11.86619 | -47.59224 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94923f79-13bb-33db-9f37-0e14a60b4169 | -12.58067 | -49.09913 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 805fe4b0-fe73-35fe-83fe-ba658b91a035 | -13.68363 | -48.58369 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7565e56d-e267-3b97-9ad4-93a9effa986e | -8.76797 | -48.67503 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 484cb676-97f7-3f4d-b32e-b25932a87806 | -10.70062 | -60.73364 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| edd0ed3e-b5f2-3cb7-b33f-425464197b74 | -10.79809 | -50.88887 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a1cd576-5bdb-3e51-8a3f-ee2933887937 | -11.8056 | -46.84251 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68b9b906-0af2-36ab-98bd-3b241cc25034 | -14.50932 | -49.61233 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 098709c0-0b2d-3803-aed3-aa9a51faeb10 | -12.54631 | -47.09198 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20872674-62c5-343d-9427-c5d80c377c59 | -9.90767 | -46.56949 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae3cbaff-c4fe-3921-98c9-e54b45de1f26 | -11.06369 | -49.77468 | 2026-09-19 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b84c175-1fe5-3abf-94e6-b3753dd00f7c | -10.31466 | -49.96103 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 431158cb-bea8-3c69-b1ed-58e895a3ecfe | -7.83526 | -55.41672 | 2026-09-19 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcac076e-a915-37ad-9913-f3056bb35b7a | -13.72941 | -48.80168 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README66.md)
