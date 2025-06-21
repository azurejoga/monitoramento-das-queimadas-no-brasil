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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd7dcb20-4143-358f-ad3a-179769e855bf | -12.47409 | -57.19032 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a163a5b2-6a5b-3727-82c8-817abea2aaa4 | -14.50103 | -48.00626 | 2025-06-21 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 770bce00-ef16-3202-a801-e695d75043d0 | -14.03705 | -53.3638 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15bacfa6-9e4a-339f-8043-7de6f27f55fe | -18.19791 | -49.84482 | 2025-06-21 05:01:00 | NPP-375D | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5fff481-f315-3efb-b09c-0814f4f57fa5 | -13.23674 | -49.8368 | 2025-06-21 05:01:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f947bcbd-3597-3c4e-b304-c63b244a0429 | -11.86808 | -54.67794 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 541f1153-a5ed-3d2c-8bf2-455f2b53e55d | -11.53155 | -56.97026 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfeacbcd-3615-3036-a21e-798efd180a67 | -11.53315 | -56.9819 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1e07b35-b3df-3162-82c9-5d968aa982a7 | -12.42462 | -54.8754 | 2025-06-21 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcec8137-0041-3fe0-8ab1-2c071fb52b6c | -11.88033 | -54.66526 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 61065b79-cdd4-3a5d-8926-a18e9475ac3c | -13.0972 | -52.29489 | 2025-06-21 05:01:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3402ff1f-5357-3236-97eb-35ee6dd91d71 | -12.51103 | -58.3477 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4ccedbfc-6346-3200-beca-8908d0925ed2 | -12.29131 | -50.10081 | 2025-06-21 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6194b47-fb99-35a4-bcdc-09890799b825 | -11.91343 | -54.81989 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29c7abc8-4254-3a32-91ec-33f732caf6eb | -11.53495 | -56.97083 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e885d718-bc19-330b-994d-feb7e785c6b7 | -12.50964 | -58.35583 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e49ac9f2-a5da-3d35-af76-639ccad6e763 | -12.50895 | -58.35989 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8eff0dbe-4df2-3213-9c90-0a51690402a7 | -12.29079 | -50.10463 | 2025-06-21 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95ea5b5e-45bd-3203-9781-b44c9161f094 | -12.02413 | -57.1007 | 2025-06-21 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b0121ff-ef6f-385d-a246-ba096092d339 | -14.81167 | -48.46757 | 2025-06-21 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1ea1a1a-dc69-3f0c-8fef-c9c9e35e60cc | -17.57903 | -43.80052 | 2025-06-21 05:01:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0749e12-fa82-34a5-a110-23bae5ecd0c9 | -11.86863 | -54.67437 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 259b3f4f-8872-30c4-884d-56274bdb4b3c | -13.90184 | -54.61075 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ba2a734-e9a8-3b70-85fe-1c174c318eb4 | -10.88681 | -56.46667 | 2025-06-21 05:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5da67028-0f14-34ef-b26f-61b92b6ca852 | -13.89846 | -54.61022 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4adbe1dd-1a84-3b97-809f-82da11567070 | -11.94422 | -58.75485 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dff4124e-2d5d-378e-95d6-862428e83a2c | -11.62138 | -58.2958 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82013e0d-a35f-3a3f-a630-b68acc3eca00 | -11.83927 | -57.76199 | 2025-06-21 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 003ea637-381e-3a7f-9548-bc3eb276d07e | -10.89076 | -56.46362 | 2025-06-21 05:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b5778883-d310-3d35-ab82-40049a7c2d3f | -11.83863 | -57.7659 | 2025-06-21 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fee598c9-d605-3ced-b961-19fb9177448c | -11.79035 | -57.24902 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e97c185b-6e30-3dd3-8102-d64ce02dc600 | -14.07118 | -53.3761 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d986d505-3379-332c-a199-d601618d5be5 | -13.14495 | -56.80577 | 2025-06-21 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27be2ea3-b249-3a78-ba1b-2265b7336724 | -12.47528 | -54.42668 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| db58e5f6-8dfa-389a-b186-7d02a9817abb | -11.78025 | -54.3697 | 2025-06-21 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3d96661a-1e97-38dc-8943-72214c792ee3 | -11.79438 | -57.24585 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3876334c-e310-3a7a-817d-27d9915e136c | -14.81188 | -48.4759 | 2025-06-21 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f0eece7-fb1b-3469-a975-b861ecdf8af9 | -12.57484 | -58.37966 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7df5b726-1494-3656-ba16-8515baffd763 | -11.94566 | -58.74635 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a0d5b54-275c-31b5-80b7-86c0b0a2b174 | -11.57438 | -54.56935 | 2025-06-21 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e61e91c5-7b05-3450-be7c-3ef26441d6c0 | -11.08282 | -55.05352 | 2025-06-21 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f5b4373-0636-3c33-98e5-03f98be0d869 | -14.97067 | -46.2634 | 2025-06-21 05:01:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e3df4c4-b6c9-3ed6-b027-8694f0a791d9 | -11.87643 | -54.66829 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 9619a3d0-48a9-3982-bcde-522af30f1e56 | -11.87811 | -54.67953 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cb819c81-65d9-3b33-a469-b49d9226ba4c | -14.03292 | -53.3673 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bd60660-3484-3609-9126-a824537a74dd | -12.96946 | -54.68184 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 208d5ffe-4479-385c-b688-b6032f2ab9f6 | -12.47648 | -60.13835 | 2025-06-21 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aeb7ba4b-3b36-341d-b9c2-fe2ce94b43bb | -13.65722 | -53.94088 | 2025-06-21 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1548ed0-1373-35fd-9275-2edd092426df | -11.95872 | -58.75745 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c5aebb9-a51a-32fe-b4ec-33f350feaf3b | -11.87756 | -54.68311 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d82ccbff-5f9e-3a67-baf2-19f572f6c04e | -11.77689 | -54.36917 | 2025-06-21 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d83def95-7396-3b03-9563-b99e76b5faa6 | -15.39731 | -47.80249 | 2025-06-21 05:01:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 655b10ea-46c2-34bc-b200-c9460a0e8f55 | -12.42518 | -54.87183 | 2025-06-21 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3765d8d-84a1-34d2-807c-960a30381cbe | -11.87253 | -54.67133 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 297b1d4e-3ddb-35ff-888a-bbe838817a59 | -11.94638 | -58.74211 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d952dfb9-617b-3c66-afd9-0c6073e7bd27 | -12.16396 | -48.68837 | 2025-06-21 05:01:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06ee893c-ac5d-39ad-8800-5c02641a387c | -12.42573 | -54.86826 | 2025-06-21 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38f23ece-1165-3ca2-8254-dca82d4222c7 | -13.24103 | -49.83737 | 2025-06-21 05:01:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ac6fb349-c61b-3ac2-b09b-2f7d62d772c5 | -11.52636 | -56.98075 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7402a57-2819-312e-95d9-3a8de7ced15d | -11.95365 | -58.76534 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2dfb7019-c308-32aa-8efb-b183e9de6fb9 | -12.16001 | -48.68305 | 2025-06-21 05:01:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d8f2547-da9c-3d03-861e-d1e9fdae06e5 | -15.76972 | -43.2762 | 2025-06-21 05:01:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf045a56-53d6-3801-8b01-d6b75bc5aa09 | -11.91453 | -54.81277 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08179af7-0ac6-3b44-a686-b3fd0f800163 | -11.94131 | -58.74997 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 91384556-8ec2-3d9f-95df-54775a95fd32 | -14.22433 | -45.51247 | 2025-06-21 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12e68aee-0009-3209-add1-543b3a603eb7 | -15.08097 | -48.94674 | 2025-06-21 05:01:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed1b123e-0fce-3e1d-8801-34d3ddce201c | -13.39368 | -48.44849 | 2025-06-21 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1fbbab4-38eb-3eff-a554-96da147cb89b | -12.47247 | -54.42251 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ae4c87c-05f3-385f-91ec-298f8eefd48e | -12.16912 | -54.26311 | 2025-06-21 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7afd44a-8656-3c62-8ed5-54b237848b13 | -12.02473 | -57.097 | 2025-06-21 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9599af44-2267-3193-a317-17d5f02973fa | -14.22404 | -45.5144 | 2025-06-21 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff68f4c0-ee6f-34f1-ac0e-93b75b986ff2 | -12.48037 | -60.13902 | 2025-06-21 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 764ea0cc-531e-388b-8f11-58075c0f419d | -12.57349 | -58.38776 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fa3f11b-372a-30e1-a57c-8cacaae91bcc | -11.87142 | -54.67847 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 620298bb-64ca-312b-89f0-8e7df9513633 | -14.81664 | -48.47685 | 2025-06-21 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77604c80-7b97-3161-81e5-b4d6930d8bc0 | -11.70654 | -54.50197 | 2025-06-21 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 188bb17a-d0e9-3d9f-baaf-f0218d2b78aa | -19.54459 | -49.66383 | 2025-06-21 05:01:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6d96548b-fb70-3ecf-95fc-bf9be06c687b | -13.04273 | -53.71607 | 2025-06-21 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3e5dbacf-210c-3773-8fe7-2fedf76a34bb | -12.47865 | -54.42721 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c623198b-10f2-3739-8158-44f0201a5335 | -11.78694 | -57.24844 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 41b6e9c5-0c4e-3de4-a950-0b91aa329fac | -11.53375 | -56.9782 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcd15bb1-4247-34a6-95b5-1460946fa11b | -11.53036 | -56.97763 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a612a76-3c01-368c-916c-79d05a17f20d | -14.81534 | -48.47764 | 2025-06-21 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 186d252c-7a82-3617-967e-9348f86423db | -12.05496 | -63.77992 | 2025-06-21 05:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c391d941-366d-3a85-8d25-a90fbec5d35e | -14.86532 | -59.79859 | 2025-06-21 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8af6f88d-dff8-323a-8088-d00852bf8388 | -11.95003 | -58.76467 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 833a80f8-bfe9-342f-b27d-7c437df95e10 | -11.78413 | -57.24411 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| ebd22a88-6e55-3132-ae82-2d62ec24c6d6 | -13.14436 | -56.80938 | 2025-06-21 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29b818dd-8cb8-3f4b-b13c-4757cd71c420 | -11.79561 | -57.23835 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 1acef57f-296f-3474-8dbe-1a25798b5aac | -11.70319 | -54.50144 | 2025-06-21 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6582e3fa-0a6d-3cf2-98ef-b4f4d92a87b7 | -11.87588 | -54.67186 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 317db21c-2344-34f9-a767-1ce442655b21 | -12.5762 | -58.37156 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06c6b95a-e970-35a0-bc88-e6b9176e3377 | -11.79219 | -57.23775 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8b437dd3-df4e-3766-8322-76a3b28cc27b | -12.52278 | -57.21309 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| baa8edc3-58b1-384b-9720-5cb06184f371 | -11.87532 | -54.67543 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 63d23ebb-dfc1-3484-9545-04bae80ec401 | -13.38833 | -48.45271 | 2025-06-21 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 294f4278-4750-3685-ab2e-99831489276c | -11.94349 | -58.75912 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e46bca2a-aaa9-362f-ba47-7000e8653a05 | -11.88647 | -54.66989 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ac3af82-8548-3823-9b68-036a5e3f5186 | -13.29229 | -57.08364 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fff6570e-bc05-3017-ad16-c3d90edfe259 | -13.04619 | -53.7166 | 2025-06-21 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README23.md)
