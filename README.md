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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f33891d4-a8ba-3c56-9371-c90e40fbdddc | -12.3432 | -49.312 | 2025-06-17 00:00:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b2328460-6a19-373b-b925-4740eb344b6d | -11.1571 | -53.9206 | 2025-06-17 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b91803a2-52b8-3de6-af3c-422816be92cb | -10.3014 | -60.5421 | 2025-06-17 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 2cfcdcf3-2ff7-35e4-ae9e-84f104d6ca90 | -5.0764 | -43.7339 | 2025-06-17 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 992068fe-fc91-3ad3-8868-827f2230d311 | -7.2405 | -43.0899 | 2025-06-17 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 845ebc8a-1671-3b19-a34b-fee37170c917 | -10.9353 | -56.8522 | 2025-06-17 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 4c6a8290-49b5-3329-80d0-71f30309863f | -11.1382 | -53.9223 | 2025-06-17 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 9bc7977e-b431-3092-83d8-ab5ce41a5af1 | -10.9167 | -56.8336 | 2025-06-17 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 3ffc8e27-1e07-3911-b4f4-2ad5d28569bb | -7.5499 | -45.6387 | 2025-06-17 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6998cceb-d414-349b-a2af-669165bbaf75 | -10.2827 | -60.5432 | 2025-06-17 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| ecfa198f-1c5c-36ed-8977-fed7db26356b | -10.1384 | -46.7374 | 2025-06-17 00:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 4110fe95-c154-38ab-b434-13204d430ac5 | -11.1568 | -53.9411 | 2025-06-17 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| f5da05cf-023f-39bb-b5a3-ec46652cf6c1 | -11.1379 | -53.9429 | 2025-06-17 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 250.7 |
| 73c2aa90-1afc-3d20-8531-e3c1f202fe93 | -10.9355 | -56.8322 | 2025-06-17 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 82535120-3de5-31e0-9090-aafffd3a35ee | -10.9353 | -56.8522 | 2025-06-17 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| f0b38224-baf5-39df-9e02-6acc8d8449b8 | -11.1379 | -53.9429 | 2025-06-17 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 200.9 |
| e85a112e-21aa-3533-bfb9-05d39e14fa4a | -10.1384 | -46.7374 | 2025-06-17 00:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 57356378-cab6-361b-983d-cc62e9fed9e2 | -11.1571 | -53.9206 | 2025-06-17 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 84c82651-694d-3c0b-ace8-73120632fccd | -10.1387 | -46.715 | 2025-06-17 00:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b3545afc-4f9c-3f42-8c97-c7f381d1b70e | -10.9355 | -56.8322 | 2025-06-17 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 146.8 |
| a8ed866c-433d-3994-ace2-98632eb18154 | -10.3014 | -60.5421 | 2025-06-17 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4041c0bc-dbf9-35ff-9521-61b0169759fe | -10.1574 | -46.7352 | 2025-06-17 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8e93c0d0-1871-3e73-a9a2-2562730e8264 | -10.2827 | -60.5432 | 2025-06-17 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 45d86453-4f2a-3508-9d13-8c19c5e8b973 | -11.1568 | -53.9411 | 2025-06-17 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 875fa84c-e3e7-3659-a3c0-1bbe734476dd | -7.5499 | -45.6387 | 2025-06-17 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| dc7d37d8-a940-389e-b64f-08bd86bcabf4 | -11.1382 | -53.9223 | 2025-06-17 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 60b6918d-ac28-3f2c-a383-7cb758d98560 | -11.1571 | -53.9206 | 2025-06-17 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 590aba2c-ce62-32ff-b64c-ac62cfc5cd32 | -10.2827 | -60.5432 | 2025-06-17 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 387172ff-766f-362d-8f0c-ede5b695e1ca | -17.4342 | -52.925 | 2025-06-17 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| cb24b7fa-ba85-3f38-929c-deb2aa5ec24c | -11.1382 | -53.9223 | 2025-06-17 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| ef80488f-7a57-3556-9959-2640534b2f71 | -11.1568 | -53.9411 | 2025-06-17 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 2ceb6561-8dba-3244-be18-2727f2d416da | -10.9353 | -56.8522 | 2025-06-17 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| af0c528a-addc-398a-a746-6cce07a9f1a2 | -10.1387 | -46.715 | 2025-06-17 00:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| fd837dc0-8b53-3e10-915f-c6b058aa2720 | -10.9355 | -56.8322 | 2025-06-17 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 6313bc2c-dc17-3cd5-b58e-bbd31bea5fff | -10.1384 | -46.7374 | 2025-06-17 00:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 60b0485e-c955-3ab0-b7de-deae1303e6b8 | -10.3014 | -60.5421 | 2025-06-17 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d24f9808-2368-3228-96c4-e98232c638fd | -11.1379 | -53.9429 | 2025-06-17 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 184.3 |
| 6aa48d4a-a0ca-31ce-98ec-2cc90a46d93d | -10.77642 | -44.68986 | 2025-06-17 00:20:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 42229446-94e0-3507-b31c-72bb54b731e9 | -19.29085 | -48.46661 | 2025-06-17 00:20:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| eba8c62b-9412-3ae9-b52b-99135270a843 | -10.35979 | -47.00618 | 2025-06-17 00:20:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| af3edd7c-257a-3c4c-9a12-9d442010d37b | -10.14076 | -46.72614 | 2025-06-17 00:20:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| a6aa15f8-42cb-3ec5-bcb7-fb9752eb5bd2 | -10.36134 | -47.0185 | 2025-06-17 00:20:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0d045aa2-978d-3c02-901c-f1d1dc73d9a9 | -11.0282 | -44.64295 | 2025-06-17 00:20:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 923ca4e8-972d-38fe-afbf-c87b75ec48e8 | -10.72795 | -44.8789 | 2025-06-17 00:20:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a8dcfa61-b752-33b1-b2dd-1f8d094ef34d | -17.20134 | -44.33034 | 2025-06-17 00:20:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 17a7ebea-b953-34f1-9d26-451c40b8d0b1 | -12.23273 | -44.22332 | 2025-06-17 00:20:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 87fad022-ef7c-3c29-9069-7ff56e4f4c9b | -10.15088 | -46.72489 | 2025-06-17 00:20:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c61a39b7-26ad-3e75-b063-669facd66a0c | -10.7495 | -48.58346 | 2025-06-17 00:20:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 522eb411-bf0a-31da-a34c-e32c6951bc16 | -12.20659 | -49.64429 | 2025-06-17 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| e491d7ec-2224-39f6-ad3f-21d9adc9da56 | -12.35007 | -49.31572 | 2025-06-17 00:20:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9e4114c2-e507-33c6-b063-05ff796dc0c4 | -10.14381 | -46.75004 | 2025-06-17 00:20:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 69228bd8-90a0-31b6-802a-fed46b4a7a25 | -20.14948 | -45.21253 | 2025-06-17 00:20:00 | TERRA_M-M | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 53629c1f-2cf2-3174-91c7-cbac52cb7b00 | -13.38514 | -48.46183 | 2025-06-17 00:20:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 19c5c51f-e4d7-3b99-b86e-f8f3f1c43ced | -12.204 | -49.63893 | 2025-06-17 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| da40a586-4cfc-3330-ac37-1c0c8f755575 | -15.92532 | -43.98579 | 2025-06-17 00:20:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 04af232e-7c30-35c4-ae82-220202ff56d1 | -15.80128 | -42.03141 | 2025-06-17 00:20:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 961729a2-658e-3754-ab43-50d968796634 | -12.23147 | -44.2139 | 2025-06-17 00:20:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 93195007-7099-3c4b-b261-4852b854d0c8 | -12.34807 | -49.30112 | 2025-06-17 00:20:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 0c899c1c-c069-3181-8c8b-b68bf1b9742e | -18.32609 | -49.88784 | 2025-06-17 00:20:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| e024613d-db08-350b-b0ef-7c42b53caf9b | -13.47585 | -46.25365 | 2025-06-17 00:20:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 75dda806-39fb-3077-b9b4-48cc7990a514 | -10.96162 | -45.11251 | 2025-06-17 00:20:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e3c2beff-c8e3-3f6e-93f3-2b7fc3bb8add | -10.13925 | -46.71425 | 2025-06-17 00:20:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f54a56ab-5412-394b-b8bf-5edcdffe1527 | -12.35047 | -49.32115 | 2025-06-17 00:20:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 3a509b7c-0c5f-36b7-8b4e-3e8a5cd1d2fc | -11.03857 | -44.65115 | 2025-06-17 00:20:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5418ea6f-b5a9-3750-be25-a3835502ba2e | -9.89943 | -44.80659 | 2025-06-17 00:20:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| af2bf664-6035-3d6a-9afb-c2a2a7b4355d | -10.74751 | -48.56715 | 2025-06-17 00:20:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9be54251-89db-33ea-ba11-3a018a471277 | -12.34783 | -49.2957 | 2025-06-17 00:20:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a3786367-122b-303c-b901-e7c17b28c048 | -10.35823 | -46.99384 | 2025-06-17 00:20:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1b92d2b8-9c92-34ca-892e-5253667cadfb | -13.27414 | -49.8923 | 2025-06-17 00:20:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4eb2aeb2-f0f5-360e-bd75-bebf9f9d4c1c | -12.20405 | -49.62298 | 2025-06-17 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 8b8849b3-bb65-33a3-ba23-b81749e2166f | -18.13516 | -43.9573 | 2025-06-17 00:20:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 06ed1154-7ae8-3535-9724-14d56ac95160 | -11.02949 | -44.65245 | 2025-06-17 00:20:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 5f52cf0e-2453-3f2b-b360-2f61940d1966 | -10.72923 | -44.88855 | 2025-06-17 00:20:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 45b87698-1a2a-3072-94d3-5d794a149952 | -10.14229 | -46.73814 | 2025-06-17 00:20:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c439e555-906b-3c9a-ad8d-b45c7e935a85 | -13.39726 | -48.46011 | 2025-06-17 00:20:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 17adc617-8db2-3e88-ad89-a90a7d696bf9 | -15.80255 | -42.04052 | 2025-06-17 00:20:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 809afc91-811c-3ef7-8e8f-26164c59307f | -2.44798 | -47.49937 | 2025-06-17 00:22:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| eb19e95f-20ab-3683-b2d7-a5d298a6b683 | -6.29483 | -46.99813 | 2025-06-17 00:22:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c73d4669-d097-36b9-905e-69c14ca47300 | -9.1984 | -45.33837 | 2025-06-17 00:22:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b690e5f5-b9c2-3058-925b-3a6b28939828 | -7.1134 | -47.84139 | 2025-06-17 00:22:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 96c17942-7fe6-36e2-bd10-c876da56ed21 | -5.0688 | -43.71833 | 2025-06-17 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 99a3de7a-6850-3609-8773-84e19260a3c3 | -8.07247 | -43.10696 | 2025-06-17 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.8 |
| 1869aa33-ac04-3e5a-b9bf-53639cbfa529 | -7.20112 | -45.34689 | 2025-06-17 00:22:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 57ea7d81-55ed-340c-8da3-01f066629795 | -7.67587 | -44.57358 | 2025-06-17 00:22:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9f2633fc-1334-3f7e-889f-5e53e73648bf | -7.22132 | -44.75079 | 2025-06-17 00:22:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fd6d8c21-4ea9-3780-bf48-befb685a13bb | -8.08259 | -43.11462 | 2025-06-17 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| f888f04b-87c7-398e-9b8f-531321f048a0 | -7.11511 | -47.85423 | 2025-06-17 00:22:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4237ecdd-88eb-3753-8d41-114a4a8adf8a | -8.08133 | -43.10566 | 2025-06-17 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 88e1e51e-a984-30e3-9056-65ab52afe6e0 | -6.83658 | -47.83226 | 2025-06-17 00:22:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7a94fb3f-951c-3e43-8562-6c8abfdde117 | -7.26625 | -44.53735 | 2025-06-17 00:22:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 21374f72-880a-3b69-9531-53d776539480 | -4.81337 | -46.82864 | 2025-06-17 00:22:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 290f8f12-263e-3d53-98f0-a1d283926b0d | -7.26959 | -44.62788 | 2025-06-17 00:22:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e3ba597c-c7ca-3f74-a0f7-127a0151a786 | -6.06261 | -46.11394 | 2025-06-17 00:22:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 51329576-365a-32cb-a84d-d96d64d9ab87 | -7.68474 | -44.57233 | 2025-06-17 00:22:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 951018b3-1ad7-3764-a860-f71232d8c4c1 | -8.611 | -45.01447 | 2025-06-17 00:22:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3b48bcf3-4930-3235-b967-3192fa757c42 | -6.11836 | -42.52615 | 2025-06-17 00:22:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| c42830a5-7110-31b1-bfbf-edfaa74ab21b | -3.77695 | -41.60587 | 2025-06-17 00:22:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2ec40315-bab8-3547-bca5-5cd9bcca00ba | -8.60014 | -48.06256 | 2025-06-17 00:22:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ad82b539-7600-39e3-9179-bd80d550afd4 | -7.23145 | -44.75854 | 2025-06-17 00:22:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d1ea3d92-7a11-3dc4-a724-e51ae017c824 | -4.24856 | -47.58504 | 2025-06-17 00:22:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |


[Clique aqui para ver as próximas entradas](README2.md)
