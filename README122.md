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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07e4be15-88de-384f-9293-b36b433393d2 | -12.10783 | -47.26929 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b4e45ef0-ed43-397d-96b2-ba8ee8152e3c | -11.07208 | -51.5172 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 3f36f606-cfa2-3a14-a31b-e7770f849109 | -11.19428 | -46.09964 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 62d1dad6-1680-340c-87cc-1b152b05a694 | -9.59815 | -47.61207 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 80c51b9a-8767-3c79-bf19-d007789b5e20 | -12.0959 | -45.06469 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| dd2db902-5714-337d-81fa-4c805e1c42c5 | -8.92353 | -45.03591 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d1b4d808-88ac-3ea9-98b6-32968d16e30a | -12.09572 | -47.18643 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d8589659-5871-3875-aa0d-835f4634ac85 | -11.94194 | -45.0621 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b887f77e-9a4c-34ad-a9a3-29be17fcbeb5 | -12.08601 | -47.14144 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6a051cce-2f4d-35b7-ae94-5da9e4ff0333 | -11.16028 | -45.04026 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 25bac901-6057-3610-b9bd-908481bcd12f | -14.54085 | -51.98497 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5a94abf2-1bce-34ee-be46-1a47ef4643b0 | -11.87436 | -45.81683 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 705f866a-91d3-308b-b2c1-d74c9799eb41 | -8.92476 | -45.019 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 571ab35b-2a2c-372f-a30b-57eeafd8cc83 | -8.76254 | -45.38981 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ef70dcc1-264f-3f0a-a8a8-dd1b179679a3 | -9.93242 | -48.34044 | 2026-08-31 16:30:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f046c2b7-a6f3-30a3-baac-5a36dfa29820 | -10.40512 | -45.0794 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e43afb97-234f-3e07-8837-8ec49155835e | -11.91364 | -45.08405 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 9a178dfd-b0e3-3c84-9617-9cd5c4e6ff19 | -11.52395 | -46.9491 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4a0ee4a9-95ba-311e-a26b-f370779737bf | -11.63167 | -50.17921 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79031db4-eeb8-3669-b3c6-0c15b2098dc5 | -15.275 | -53.8844 | 2026-08-31 16:30:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 4f9d7a9d-2881-3185-b3e0-76e11639e635 | -8.41677 | -44.98156 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 244cc33b-42b8-39c3-a73e-660711759c6c | -11.06344 | -51.44566 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bf4d9c89-ea5a-3c1d-a26c-612a4197e3c0 | -10.12982 | -45.83955 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 697acbaa-c8c9-38e8-b12f-a080fff9a7e8 | -11.0639 | -51.44942 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 18813bf9-8f51-33d7-8645-a97c45a7061f | -10.22661 | -46.68094 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 64f255f0-9ca5-3678-b993-ed57d8c24042 | -8.76526 | -46.45116 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 5c96ad61-530b-3545-8eeb-dfa6e9af7cc6 | -13.43135 | -51.70199 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 95dc2984-fcda-30b5-923f-fc2dc2950723 | -10.85139 | -45.34029 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 4183c1fc-22ef-3324-8134-609cc47b4f5d | -9.57004 | -48.32733 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 324f9efc-14a7-3e16-a632-635ee2d3d5f5 | -10.04353 | -48.68546 | 2026-08-31 16:30:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 515f5ca6-8254-3a23-a2ee-c4834f238a05 | -12.07401 | -44.99026 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fc127cd5-eb48-34c2-9791-e00e82d4ec93 | -10.82634 | -50.63044 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 9523266e-cc36-3833-8baa-8dfb0013030a | -9.97388 | -46.82615 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3a1a95b3-8d14-316f-8ca4-6bcde4c43a3a | -11.34273 | -45.1999 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ba19aa48-fd9f-309f-935e-abd35a203020 | -10.74742 | -54.02531 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| beade693-3c47-378f-9b8b-11877f8675a7 | -11.21004 | -45.10004 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9d86566c-537b-3e69-b8eb-8109b0c38ce8 | -14.96986 | -54.58472 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ba96f994-20bb-38ca-b13e-f42423594d6b | -12.08851 | -47.25531 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b6801b50-1a8a-3063-ba1f-f4afec30bada | -12.16992 | -50.53878 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e14d0416-41ba-3c23-b898-9cf1b140b7c9 | -11.228 | -45.147 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 1095d574-f455-3c73-a898-f138dfdce7a7 | -10.75255 | -54.06981 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a9f66599-3e97-3468-a4f5-994931d1f78d | -14.47178 | -52.2014 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 605d4a45-fd99-32bd-b5bf-93436a106af5 | -9.67424 | -47.94852 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2a4551ae-867d-31a2-be05-aea6a2c60d44 | -14.46616 | -52.20683 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b346a0b0-b9c1-3217-aa6d-dfa6dddddaf2 | -11.5436 | -45.48565 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1cbb2712-b3ed-37df-82af-56c4f4e2bfab | -11.35081 | -45.23028 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| aa5f2bb1-6f67-3fa3-8297-c02064f33233 | -14.96132 | -54.571 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 73fca4e4-79cd-381e-ac66-29352c4a1743 | -11.25071 | -45.09425 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5ea2f5af-812c-37cc-85e2-0de358bcee78 | -10.85319 | -45.32635 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c3656541-32c9-34bc-ac64-56e6403325a9 | -10.1214 | -50.32314 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b22695b-582e-3f29-9cc6-4360cadf991b | -11.20882 | -45.09137 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8aacb19f-e548-3ac5-9b6b-5d1ded13e0de | -10.40941 | -45.08319 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 358cbb91-c0cb-3d20-b4d9-0e165cf8a9aa | -12.90442 | -45.84127 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 08f632fc-4d5c-3cad-8356-857f76268454 | -10.74569 | -54.05037 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 51aaa162-4a87-3d82-9dcd-39a4ec60fbc1 | -10.15147 | -45.69299 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 8390d6da-93d7-3ad0-a52b-38a6a7f62db1 | -14.4824 | -49.04356 | 2026-08-31 16:30:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6ff08c9e-b990-3e68-b8de-c21f68b535b4 | -14.25857 | -54.65368 | 2026-08-31 16:30:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 25f9fe53-e186-36f3-90ec-8d27f49db909 | -13.43088 | -51.69776 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 068bcf2b-ca1e-373d-a74d-e95973e21dab | -13.39149 | -51.34875 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 45b243e8-5bb0-3c96-ae56-2d3df2ae2b44 | -8.91662 | -44.17194 | 2026-08-31 16:30:00 | NPP-375 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 594c397b-fd9c-3985-8e98-aa3d79165f41 | -11.19609 | -46.08429 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 06ad8553-858f-3703-8511-dc75971aecd7 | -12.1026 | -45.03152 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 011bc56d-05d3-34e2-a8a5-50eb1c27699f | -9.42235 | -45.67775 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| bc6d1501-4412-396c-b82e-c2a855cf28a8 | -9.68665 | -47.94272 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| efa99f58-e635-34f8-bbbf-aff48df2a951 | -11.19036 | -45.04043 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cd1d0ab1-1f25-36c9-a0e8-99282eb4b932 | -9.42302 | -45.68228 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a3881304-3ac5-36b1-b344-f242fe0dac9a | -12.09902 | -47.14524 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6fa8d31c-1ba9-3c16-8fac-63ee5c59895e | -11.2348 | -45.14159 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| a569f088-7ae3-3d4a-a9c5-53704397c383 | -13.55236 | -48.23574 | 2026-08-31 16:30:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| fa7cd322-5e93-3cbb-8116-0b3cc4606ffd | -14.94768 | -54.57805 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 92a97df3-1ef2-30b1-9fe9-d314e3b392a0 | -11.21435 | -45.10383 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fdc73547-a2d9-3a72-897b-0e2f469d5bbb | -9.70311 | -48.16105 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f8b7338d-e2a1-3367-9de2-d377c77d9d4e | -12.19163 | -43.12534 | 2026-08-31 16:30:00 | NPP-375 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 501550a6-7be5-323c-850c-394eb47c3a1c | -10.05654 | -36.52665 | 2026-08-31 16:30:00 | NPP-375 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 72e5d289-62ee-3f36-b25c-c067752858a9 | -8.738 | -41.2229 | 2026-08-31 16:30:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dacdbdfd-35af-3e3c-8288-947f979930c6 | -9.59868 | -47.61599 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d0647395-27a6-3666-9505-de4c9b66a833 | -10.17871 | -39.30353 | 2026-08-31 16:30:00 | NPP-375 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5bf40f20-3c51-3feb-9ffd-f878648180b3 | -11.16561 | -45.04297 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3e2ddaab-6456-3ebe-ab12-4ca1d67dcf5d | -10.49157 | -40.31363 | 2026-08-31 16:30:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a7e1c150-701e-39ca-b038-a3fb425af57c | -10.10489 | -50.27624 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5106991d-9003-367d-9308-4362a43d4cd1 | -11.67423 | -47.62022 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e6a7f7c1-64f0-340d-b279-1649b4baf962 | -10.84454 | -45.99586 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2a28f18c-f5e8-3e5d-b2c4-8b119576acf0 | -10.12336 | -50.29832 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 73a12ef9-b534-3a81-b07b-ff1f4ccf970a | -11.16885 | -45.0479 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 83809d31-7ed4-3a08-9005-d1946debd199 | -8.95133 | -36.92185 | 2026-08-31 16:30:00 | NPP-375 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 68b29e0a-f1cb-3f05-8e0b-810a3cb984ae | -11.54297 | -45.48103 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fe4330f8-ed9f-3fbd-8d96-dbdc2e3eb4e0 | -8.38181 | -44.99123 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 6d9bff01-5354-349a-a889-4ba42ad8a31b | -9.68066 | -47.93108 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0c839c9e-4182-3d0a-a281-9cc042825336 | -10.40209 | -45.08423 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a70b74b0-dcc0-311f-bd6c-0648d2948d47 | -11.2443 | -54.01104 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 8786e4c1-0cda-3a16-9871-f902b0067e0e | -14.09327 | -52.19798 | 2026-08-31 16:30:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 276b0fb8-0fb8-3314-bf57-38f48a504416 | -12.19505 | -43.12481 | 2026-08-31 16:30:00 | NPP-375 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ee1ab2fd-4b73-3b53-ad48-7d3796ea4521 | -11.93511 | -45.06755 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0f9a4902-fff1-33db-8bf1-d80b0d642116 | -9.19686 | -47.99473 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7037c3bc-675e-392c-bb1d-e56b6894a7ec | -8.87011 | -47.08652 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1e5153d8-69af-3b35-ad3c-a2e4ea4d876f | -10.04274 | -48.68251 | 2026-08-31 16:30:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 2457c82f-cfe9-3a91-afd2-79e2e34de748 | -14.95724 | -54.56919 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| e7baa7b8-880d-3a7d-b909-adc37d62e8dd | -11.37312 | -45.19998 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 359ffc56-8d32-36f2-b404-44e17c626853 | -10.82431 | -47.23202 | 2026-08-31 16:30:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b2da08b3-054c-3695-95db-3580cd9f1986 | -13.51259 | -43.5172 | 2026-08-31 16:30:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |


[Clique aqui para ver as próximas entradas](README123.md)
