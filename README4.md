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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cf52217-2260-31f0-8156-2473d3f60358 | -11.4397 | -45.0923 | 2025-07-09 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 53255909-b4af-3257-802d-6ae55299fdd3 | -17.3367 | -47.5011 | 2025-07-09 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 43012efb-a33d-35e4-84dc-55abd06ad6ba | -7.2408 | -43.0664 | 2025-07-09 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 161.7 |
| 1e4a318d-0c14-3b52-826d-2d9d484b66a2 | -11.4205 | -45.095 | 2025-07-09 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 74d6284e-e988-350e-8eb7-3525a43f3f64 | -11.4588 | -45.0895 | 2025-07-09 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 80e5bec8-8731-30ae-8002-a79f6f0b2cb8 | -8.5028 | -43.2614 | 2025-07-09 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| fa5dc2f3-14da-3dc9-bb1a-4c317db663b8 | -10.5779 | -49.1098 | 2025-07-09 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6f2d9027-6d86-382a-ada0-aa40c8ec373f | -18.6467 | -55.7351 | 2025-07-09 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 8cffeef9-3dd8-32e7-b1c8-7c8e84f7f403 | -7.2405 | -43.0899 | 2025-07-09 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| f96298fe-b1a5-37f7-a088-00b98f69361d | -5.2328 | -45.2102 | 2025-07-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 07349833-df38-3218-8c93-36cbf8b69910 | -11.4393 | -45.1154 | 2025-07-09 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 387e56dd-fc7e-308c-9049-39103f68e6f9 | -8.5214 | -43.2828 | 2025-07-09 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 258.1 |
| 31c6e8b1-40a4-3757-844f-de8bfde8bfdc | -8.5211 | -43.3063 | 2025-07-09 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 166.6 |
| d302d2ee-d47e-3729-9c7a-10a7572a8797 | -11.4584 | -45.1126 | 2025-07-09 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| ba79590c-562f-3315-af62-c3588bd97690 | -11.4201 | -45.1181 | 2025-07-09 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 84080075-636d-3a28-b485-979e9a3561c9 | -8.5211 | -43.3063 | 2025-07-09 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 3faba6dd-1143-3915-88a1-1428274491c8 | -10.5776 | -49.1316 | 2025-07-09 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a6c317cd-7460-37b0-8f5a-431be06e95f8 | -11.4584 | -45.1126 | 2025-07-09 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 26a91ad4-9342-3caa-aae4-87a169df253f | -11.4588 | -45.0895 | 2025-07-09 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| de97f350-20dc-3336-ada1-873f0a744021 | -18.6467 | -55.7351 | 2025-07-09 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 9d1f850b-23a0-3dc4-864f-94de7920a2ac | -7.2408 | -43.0664 | 2025-07-09 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.4 |
| 07ad56e8-f6f6-30cd-a5d1-617d73fe0631 | -11.6737 | -43.7762 | 2025-07-09 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| e2c7c3b3-ef55-36a3-b0cd-e8cebe1d26b8 | -8.5025 | -43.285 | 2025-07-09 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 276.7 |
| bae00cf4-ea84-36bc-a603-e5f6430801f3 | -10.5779 | -49.1098 | 2025-07-09 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 275c4c73-019c-3fe0-bf09-503ce86434fc | -11.4397 | -45.0923 | 2025-07-09 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| b65eb3f2-c371-32df-b394-453e17edc72c | -11.4393 | -45.1154 | 2025-07-09 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 182ffc12-3fdb-3ac6-bf1c-e18be0f80bde | -8.5214 | -43.2828 | 2025-07-09 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 227.4 |
| 511e7dc1-70b4-35a6-9256-25bd44382022 | -7.2405 | -43.0899 | 2025-07-09 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 715408a3-f371-33a0-abd2-46c501e0694f | -8.5022 | -43.3085 | 2025-07-09 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 192.4 |
| 62bc6022-9474-347d-9af8-07c1bdbcebd3 | -8.5028 | -43.2614 | 2025-07-09 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| ea9194e9-478c-31aa-823a-ef55b6c64e28 | -11.4201 | -45.1181 | 2025-07-09 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| b61ed6ce-0d7f-30f3-b042-d60e4ed8ad83 | -6.1792 | -48.0494 | 2025-07-09 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 8d95cef3-7971-3dbc-ad98-c237e5887ffc | -11.4205 | -45.095 | 2025-07-09 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 2bfed69c-baaa-3ad4-a817-0cd69bfb34a0 | -5.2328 | -45.2102 | 2025-07-09 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 46c00a15-4e66-3819-ab76-c7d1f9561d3c | -18.6576 | -55.732201 | 2025-07-09 01:25:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 82de1ae4-ef02-3214-8c32-e65b4ff7d0f9 | -18.646099 | -55.7272 | 2025-07-09 01:25:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c36b5bb7-9e06-395f-b2da-15ba70ece28b | -10.6339 | -49.4631 | 2025-07-09 01:25:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a49969d-5780-3b97-a0e8-b3a5eb65cbdc | -9.4155 | -58.902 | 2025-07-09 01:25:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd011c0c-cfca-3308-88a1-4b6b00977822 | -11.8771 | -58.710098 | 2025-07-09 01:25:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d28ff9a-fd36-3e9b-92d2-e11a1767f5d5 | -9.9271 | -59.930901 | 2025-07-09 01:25:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 548fe9c0-f244-3843-a71e-0c8488302a5b | -18.6542 | -55.7174 | 2025-07-09 01:25:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 38852e7c-0a2a-3bdc-b8ba-10367aaee0fd | -9.4171 | -58.908901 | 2025-07-09 01:25:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b36dd38-65f4-3cf7-beeb-1eb60dfc2cdd | -10.5896 | -49.137299 | 2025-07-09 01:25:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 188457e5-d33c-395b-90b9-1252c0931c00 | -18.655899 | -55.7248 | 2025-07-09 01:25:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6596b688-5b9a-306f-8498-33a9997c0f0d | -10.5743 | -49.118301 | 2025-07-09 01:25:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e707ecc-8c54-35d8-9772-d688527052df | -20.2325 | -55.666401 | 2025-07-09 01:25:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a01f4089-6541-3789-bdbc-22ddf678a7ce | -18.6444 | -55.719799 | 2025-07-09 01:25:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a599ccdc-6088-32d9-82b7-1372a2a8788d | -10.5839 | -49.1157 | 2025-07-09 01:25:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3d61d3e-f935-3265-909e-56e6d5fd699f | -10.6435 | -49.460499 | 2025-07-09 01:25:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d79470a-28ae-3e2a-a43b-c55d3870568f | -18.017099 | -50.487301 | 2025-07-09 01:25:00 | METOP-C | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 91bd650a-941a-370a-9685-1673d8c4d07a | -10.58 | -49.1399 | 2025-07-09 01:25:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 456a2cb0-55eb-3a68-be60-6cb4e5096ba0 | -11.8157 | -58.848701 | 2025-07-09 01:25:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10097124-e85a-3327-99b8-0adfc6541922 | -18.6478 | -55.7346 | 2025-07-09 01:25:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e6e21816-4199-32db-b04d-f060098ed136 | -10.6392 | -49.483601 | 2025-07-09 01:25:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62e013bd-954e-30e1-b470-2abe2c2c1e5a | -20.731501 | -56.6548 | 2025-07-09 01:25:00 | METOP-C | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 66a1eb31-a2d7-3138-ad41-546b1808e298 | -11.8787 | -58.716999 | 2025-07-09 01:25:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b44485c0-ea6f-3462-86d8-0bd9ad37b771 | -9.9286 | -59.938 | 2025-07-09 01:25:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b815e42-184f-3830-ad1e-877a49b878a8 | -8.5214 | -43.2828 | 2025-07-09 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 351.2 |
| 7099a519-476a-3a0f-897c-d5ba5ab6eb48 | -7.2408 | -43.0664 | 2025-07-09 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 153.1 |
| 114fed9a-e73b-3a97-a800-40e616b2f625 | -12.4932 | -43.1455 | 2025-07-09 01:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 2bb1eba2-0ca5-3cc4-9b76-55cb2dc444e6 | -11.4201 | -45.1181 | 2025-07-09 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| baa2aaab-95ca-3f81-9bef-cceecb12dd4a | -6.1791 | -48.0712 | 2025-07-09 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f1a062a2-2a3e-3105-8589-9d8c7e3d8396 | -8.5211 | -43.3063 | 2025-07-09 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 240.4 |
| acbb77e5-0258-3f85-90f2-d436463a8b51 | -10.5776 | -49.1316 | 2025-07-09 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 36a1cf9b-a227-3c31-9301-97dccff00964 | -11.4584 | -45.1126 | 2025-07-09 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 0322be66-a4fb-3f9b-97ac-836d0fcc2d31 | -11.4588 | -45.0895 | 2025-07-09 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 099d3cf3-0b86-33ca-b911-6894de8c6920 | -6.1606 | -48.0507 | 2025-07-09 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f35039e5-6cee-36dc-b058-7af546c766a6 | -11.4393 | -45.1154 | 2025-07-09 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 4f29b187-dbf2-313c-80ea-e63a29fb16f4 | -18.6467 | -55.7351 | 2025-07-09 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.6 |
| a99e1984-f190-36b8-b8f7-a4c92f5769d4 | -7.2405 | -43.0899 | 2025-07-09 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 39222ed9-0baa-38bb-9ba0-c6c9bf88fb8b | -8.5025 | -43.285 | 2025-07-09 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 330.8 |
| dbcd5c73-ab6a-3dab-856d-4ace71bc1b74 | -11.4397 | -45.0923 | 2025-07-09 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 77495993-1c29-3e5e-8942-9b1b7c4e7c74 | -8.5028 | -43.2614 | 2025-07-09 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 554ea9e7-c61c-33bc-8614-34dcabee5806 | -8.5022 | -43.3085 | 2025-07-09 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 218.4 |
| abef4849-e7b0-37b5-8eb0-65012e75dd7b | -6.1792 | -48.0494 | 2025-07-09 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 192.9 |
| bd9d086b-40ef-3234-bb9c-bb09ac064765 | -11.4205 | -45.095 | 2025-07-09 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f2561b66-da02-351a-8529-d317dce1eefa | -18.6495 | -55.73325 | 2025-07-09 01:39:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| dc81c10f-87de-3931-982e-bcbe6c96bbc3 | -18.64586 | -55.71276 | 2025-07-09 01:39:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.0 |
| be978d3c-f16e-3097-8b5b-63422b9ebb22 | -8.5217 | -43.2593 | 2025-07-09 01:40:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 4851abd8-4177-38d5-b8f5-d0053f077888 | -8.5025 | -43.285 | 2025-07-09 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 302.3 |
| 423f11c4-3601-3ca9-bfe5-e9774cb07f10 | -11.4588 | -45.0895 | 2025-07-09 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 596e5925-5004-3c44-bd8c-98c72bad3759 | -11.4205 | -45.095 | 2025-07-09 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 2cbd80eb-27e1-3ce3-a0df-ce01333eb5c1 | -8.5214 | -43.2828 | 2025-07-09 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 449.9 |
| 3a9b735d-9433-30cf-9278-7228378bdc8a | -11.4397 | -45.0923 | 2025-07-09 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| e8b7d734-e981-3c8e-af6c-a8716216c52a | -8.5028 | -43.2614 | 2025-07-09 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| adae6b4c-41e2-34a2-9bae-9bfebde64b7d | -11.4201 | -45.1181 | 2025-07-09 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 8128e6e1-969d-30f0-bced-7cc08d28ccf0 | -11.4584 | -45.1126 | 2025-07-09 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 77ebcddd-1d0d-3ea4-8dbf-ac87e9b3e278 | -8.5211 | -43.3063 | 2025-07-09 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 255.9 |
| dd1a8e6a-238f-3722-8bd4-d46e1f9fbfb2 | -11.6737 | -43.7762 | 2025-07-09 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 7ce655b9-da5a-3c1c-87d3-94149a9e1b53 | -11.4393 | -45.1154 | 2025-07-09 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 88aa65e2-e382-322e-818b-5d85634ca1f3 | -10.5776 | -49.1316 | 2025-07-09 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 8cb41200-a0e9-356a-a4d5-fbe4a49167da | -6.1606 | -48.0507 | 2025-07-09 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| a5bbfdb6-d49e-3889-ae4c-f3388b5d4634 | -6.1792 | -48.0494 | 2025-07-09 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| f6dd8f94-204b-3516-818f-8b9e27f43472 | -7.2408 | -43.0664 | 2025-07-09 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 118.9 |
| d36ddf39-5abc-3e36-94f6-570e2db4e265 | -8.5022 | -43.3085 | 2025-07-09 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 173.9 |
| f7a7708b-92b1-34d0-9980-95bbd9c88668 | -12.79844 | -62.00832 | 2025-07-09 01:41:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9d3301f7-1843-3571-b886-e6e7b2a9acb0 | -9.92354 | -59.93661 | 2025-07-09 01:41:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6e01f4c7-66e7-3f35-86fd-b6e25611861c | -11.87532 | -58.71654 | 2025-07-09 01:41:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4685f690-3d37-3c3c-8b4b-e18014df7f35 | -9.6071 | -63.4654 | 2025-07-09 01:41:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9907ef02-2e54-3998-8e3a-0eabd4f4bc95 | -8.5028 | -43.2614 | 2025-07-09 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |


[Clique aqui para ver as próximas entradas](README5.md)
