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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45de3172-aa81-3cf2-8286-03c76c14c449 | -13.5422 | -46.97026 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 191e9dfc-dcb9-36c7-84bc-83cc7a429b0b | -13.3382 | -46.98114 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ac948fb-a48a-3c71-af9a-4bb34b1585fa | -18.11896 | -48.53648 | 2025-09-01 04:34:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d98d412e-1bf6-349f-a6a2-7fdecac13a07 | -11.48705 | -46.80087 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f377f5b-6e4e-3692-8d86-2152f842a52f | -12.38764 | -46.47692 | 2025-09-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e836b1d8-944f-301c-8a87-e309406b85a8 | -14.31664 | -60.34734 | 2025-09-01 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acb5dde9-21d0-3590-a3cf-72ab24ae2c23 | -12.02438 | -49.70967 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 718ebdec-b49c-3dbe-a065-af95fea5cb4c | -12.83386 | -48.07162 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c520a68e-c847-32e5-8e1f-73b60449758b | -10.24284 | -51.11382 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e5647d6-9e15-3a8a-8fe3-30c95cd78304 | -15.59958 | -48.3417 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4d25ba4-6995-392b-b59c-08288f69c22a | -11.45244 | -46.81907 | 2025-09-01 04:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e107a10-2563-3a53-b255-099af4187759 | -11.89457 | -46.68814 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 463beada-de28-3dac-b108-ada144bb1ddd | -12.63205 | -56.9962 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45ba0146-5f7c-3776-a932-32e776202047 | -13.59272 | -48.14389 | 2025-09-01 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f156d31-11be-3062-8080-50544e96c562 | -16.13666 | -49.04757 | 2025-09-01 04:34:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffb31995-2a56-337f-a39c-fe1eefe1808e | -10.72682 | -49.58071 | 2025-09-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4ea8c88-ec3d-3535-9852-c6cd8096d8be | -15.69723 | -48.92539 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d0d493d-e774-307c-829c-2ce64a805c5a | -15.21818 | -53.78636 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ad7378c-5399-3bff-977f-1b04f97f91f6 | -12.60923 | -57.01317 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 458d056f-732b-3cff-889b-1a10c8d38f31 | -16.11692 | -46.8245 | 2025-09-01 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff06b58b-e4f0-3c01-8567-eff8805d8f15 | -12.55617 | -48.22056 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71352910-9ff0-319a-8382-8d139ea39b1f | -12.60448 | -57.01223 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d923239-dc6c-3804-811f-d0857c0ffc6d | -10.72187 | -49.56902 | 2025-09-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5e3bf93-3e1a-3577-aaf2-433cf111b9a8 | -11.89464 | -46.73606 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5ae240c8-e7e9-3fd6-8be2-ea0953fc9eab | -15.69778 | -48.89917 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed5992dc-ae2c-33bc-a7b0-0847af5a9446 | -16.61432 | -49.4045 | 2025-09-01 04:34:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6b05e9f-6378-32b1-a25d-8231d5bad7eb | -13.49479 | -46.97565 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55bfb53c-4823-3837-be97-3f2a35906fb9 | -13.69697 | -46.92648 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96bdc8fd-ea8f-3208-a5e2-2d41589f5541 | -13.16611 | -45.2831 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 522bbd63-3ce2-3208-a539-c6a97337800f | -13.65597 | -46.93425 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d666069f-c106-3b82-86f5-5d0f0c1bd7f3 | -15.69893 | -48.95929 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ada15088-c926-36ae-a660-aae790e631d8 | -12.97871 | -48.11572 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7c10597e-dbbc-358f-a529-b8d3e33d7d79 | -13.51822 | -46.9869 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7e66dc23-450a-392f-a6cb-3d05ba3e5c76 | -14.22473 | -51.65293 | 2025-09-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8480209-bf61-3b50-ad40-6b2f1b18b2dd | -12.81592 | -48.07631 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c5de64c-4d4c-36fb-9af3-e2bb36072ac4 | -11.80808 | -46.41656 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 74ce854d-b2a3-3b25-ad80-fc1f20e99dcc | -14.78849 | -46.74535 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4da331a-4865-33a7-9e4e-e0f2ee63e481 | -15.58879 | -48.32092 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04ab596c-7eb4-3c53-aaa7-961c9d5b1641 | -17.1407 | -46.08991 | 2025-09-01 04:34:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4db81d56-c974-38de-9bee-404c0165d5e2 | -15.59397 | -48.35592 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e648171-2b3e-366f-badb-10c7b4fea3ba | -15.70278 | -48.91142 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 3f29dc8d-738e-35be-b56f-a0cd4087025c | -13.29215 | -46.90488 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2b1ff19-d365-36cf-bc7a-09a3267516a7 | -10.62166 | -54.91957 | 2025-09-01 04:34:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08a4941f-2842-37cb-a194-a6760ef6bd92 | -8.6137 | -62.59235 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f1c9965-1059-3c48-8af3-eab21eb80101 | -10.36921 | -52.28788 | 2025-09-01 04:34:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 349d6530-e18c-3bce-a777-e592b9cfc966 | -13.52339 | -46.97616 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d294b5f-b868-3b36-bc56-dea389f90028 | -18.07585 | -45.94492 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef3b1fba-d0ed-3bc8-825c-98b2d2b014ff | -12.56897 | -44.79082 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6e771a1-a632-3647-bd17-93facd842796 | -15.72905 | -48.98654 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| aebd8571-7215-313e-ba94-635032e135ff | -14.79164 | -46.72394 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 970c28ca-2004-35e4-bb77-bc4bd0706987 | -10.28269 | -54.24689 | 2025-09-01 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cef76dc-80de-31e5-b8b3-8c63d9aa2c92 | -16.29449 | -52.94241 | 2025-09-01 04:34:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6cc52edf-6fbf-35ec-af64-65981c221a35 | -13.50471 | -46.98127 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 510a57bd-f494-3a1d-a18d-f236acd17cda | -15.69504 | -48.96232 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0c622740-af6d-3eab-89b9-5605819a3ec1 | -13.19327 | -50.57731 | 2025-09-01 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1b7251d-640c-3612-ba17-9f3fce50e449 | -11.91612 | -46.44279 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48b68449-91e9-3dd6-9a4e-5590a899181d | -15.69945 | -48.91078 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2bb663b4-cfda-37f2-9791-2a754e54fac7 | -11.42722 | -46.91721 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05b59216-4856-33ba-b80c-8481cbe522ca | -17.1711 | -46.08686 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6d63762-5fb4-340b-bf72-6c49de0bb4f5 | -15.30165 | -52.78488 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97cbac90-5242-329a-8063-61ef401d9281 | -14.79174 | -46.73479 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e29e504e-4674-3a15-91b3-06d8ed081ea5 | -13.31966 | -46.86435 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bdcd9d7-a6f7-3159-919b-b0a99f75641a | -10.36555 | -52.28727 | 2025-09-01 04:34:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf7e018a-2985-384d-839c-ef6078e12a5b | -13.37393 | -46.31712 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5cf6eb8-d81f-3744-bb3a-eefdf47d6e3c | -14.78486 | -46.74506 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fbf3e81-c186-324a-a076-d4f6ff8d4a09 | -12.58794 | -48.19239 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0f21e2b7-8dd2-39ec-bd5b-9af961815ae4 | -11.34038 | -43.67548 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5dd4d6b-2cf3-3a77-8dbf-d61797c03f8a | -13.52694 | -46.97641 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06be597d-2b18-34fc-baf7-e784f716b30c | -11.37014 | -43.64177 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 314b1437-53e3-3c43-a3f6-b3fcfae576e8 | -13.49056 | -46.93102 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4abe920c-39ea-300c-a775-c91d58ffc014 | -13.48496 | -46.99379 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4b81f69-8249-3010-b162-22de5d49c060 | -14.78575 | -46.71402 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 106590f6-62f8-3f99-9968-74d6402d50e1 | -15.22691 | -53.80216 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2363c8a2-a26b-3211-b3f5-53c50b67541f | -11.38043 | -43.62803 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96baea01-7645-3baf-9458-99c5105a1d76 | -15.72961 | -48.9829 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c7c199e3-90a7-3a6c-ab38-5bbbf1c04fd4 | -11.85001 | -46.78575 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f23cf10-ec86-39ee-a5b7-1b3d90cb9da8 | -12.09494 | -44.72404 | 2025-09-01 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ef6e49f-0233-3951-9e22-96712eb1c381 | -11.83724 | -51.46891 | 2025-09-01 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e3b9fd1-aa71-3fa5-87a2-74e523b9b446 | -12.87942 | -48.16768 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f933860-f91c-37ab-8ff2-a864592dd1c1 | -12.79409 | -48.08405 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92fe7892-9822-3f74-9d6e-6d6f50962e71 | -11.04537 | -46.97005 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6774d502-2080-3338-9a7a-b35c9120d1bb | -8.72383 | -62.40755 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d24e84e3-58a1-3fd6-b997-6eadb85cf5d7 | -15.08612 | -48.12697 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e0d1a1c-e243-3152-ada4-3b08f450d49e | -17.1452 | -46.08557 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28800131-2978-3e5a-bec5-2cb87b60a657 | -13.31438 | -46.90014 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98c1c7e6-8252-3ef7-bb4d-7c2e02cf49c6 | -14.01272 | -54.05399 | 2025-09-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bba2548-7a58-33de-ad52-cdd0744ee44c | -12.73859 | -44.80959 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac51a60b-b739-34ac-aaa0-ced7f3eb1951 | -15.70834 | -48.89743 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44434fbd-b277-3bb1-b474-16d7f7609a91 | -12.85515 | -48.06758 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| da0fd613-d51f-3a0d-a074-c63cad9853fa | -14.48553 | -52.99194 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2f6da3f-7537-3919-ad81-2ade3aebd5be | -12.09883 | -50.64212 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd20c0d1-f73b-3b61-af9a-14851cf1be2b | -15.22561 | -53.78771 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2336e4d9-dc0f-3b54-aad6-1110fa2f6086 | -13.71153 | -46.92529 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 498858f1-9e8e-3bef-afed-de1848b0c9ec | -10.28204 | -54.2506 | 2025-09-01 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a046461-288f-3f92-9ae7-63cce4551f6b | -12.41192 | -46.45974 | 2025-09-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b726a10b-3c3f-355d-b5e3-1d69493d5c91 | -12.64023 | -48.20046 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67efc8ad-ce19-33c2-a049-2d4a2f11f277 | -12.97668 | -54.75658 | 2025-09-01 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ffb8831-d6ad-33b9-b9bf-0e5a11ddb51c | -11.91102 | -44.88514 | 2025-09-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94235634-4c09-3151-ae19-74a876f43906 | -12.598 | -48.21618 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e7864a50-c1f7-32a0-b848-ae1c8f7dd9b0 | -15.32332 | -46.10186 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README73.md)
