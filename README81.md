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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be8c573c-68e5-3153-9c1d-f972350f6d58 | -12.18861 | -46.72215 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| c0e1d9cd-67bf-31ce-acfc-ed670bf3bc47 | -10.35668 | -47.57696 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 1547b83f-c86f-336a-87ca-ed925e3b34bb | -7.96676 | -46.74095 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b1f37206-29a7-3b2b-911a-4cd7dc86b09c | -9.53646 | -46.92084 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 90f5412f-72ff-388b-9b64-2130559ce59a | -15.31245 | -48.05424 | 2025-10-29 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| a00c3713-9bca-3757-8617-d25abb465d8e | -11.06315 | -47.53885 | 2025-10-29 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6f477569-45c8-3690-bec8-7cf0c47bcce9 | -10.64711 | -48.00266 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d2117e10-011f-35d5-a751-a8e619b2cf86 | -10.91336 | -47.81987 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8455a5a4-ade2-3a67-91fd-29ea30b295f0 | -9.28277 | -45.22002 | 2025-10-29 12:19:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9aa8871f-451b-362a-ade0-11cf6acf6669 | -10.35927 | -47.55872 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9d5d7667-fda6-31f9-826a-c55624d973bd | -9.90652 | -44.9082 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 7de407ef-04f8-33fa-9427-74dfe80d66f8 | -8.76477 | -46.50874 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2b775d8d-31c3-3b27-a083-6fa594cbea56 | -10.62828 | -47.88047 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0ca5ef09-584a-344e-bd8a-e119e1dc3498 | -7.70423 | -46.90683 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 06b36e33-2c7f-3a85-b838-ff58ddf227f0 | -10.96065 | -47.61224 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 66b84c02-a454-311d-bd33-dba87fdac399 | -18.04388 | -44.41852 | 2025-10-29 12:19:00 | TERRA_M-T | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 0360ae73-ea40-3b49-a677-3bcf949961cf | -10.28666 | -47.28983 | 2025-10-29 12:19:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 807acb55-ba8a-3ec2-86bf-37849b2f5390 | -13.21874 | -47.06162 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 9722e15f-948c-309f-a8a8-9723dfa082da | -9.23885 | -46.34823 | 2025-10-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 390.3 |
| 3e8efc4b-d838-3f0a-841d-ad6296d2c5f7 | -8.45692 | -45.87182 | 2025-10-29 12:19:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b618887b-5040-3fa9-a0bf-bc3199e7b0e4 | -11.30097 | -47.55361 | 2025-10-29 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| a17d186f-4b09-39f5-8b14-ef1a35d3e158 | -10.87003 | -50.09266 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 2544cbbc-9dfc-33a7-b3d2-1316f63e7711 | -15.07663 | -48.75628 | 2025-10-29 12:19:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8fe5419b-d898-3512-8f5c-5a3befa0011c | -7.63769 | -46.91908 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 58732039-8a59-3bbb-b6db-09f129a31aea | -13.73206 | -48.75399 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 919ee9d0-60c4-3cd5-b765-62eebb6d77b5 | -10.11063 | -46.56948 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d833921f-6050-38d7-be66-6d503f9b1302 | -11.30995 | -47.55479 | 2025-10-29 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2815075b-3d07-36e0-a93b-15ffe3392507 | -10.12121 | -46.56093 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5b7ebbb5-5fec-3714-9234-cea3feafe260 | -8.00163 | -46.68913 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b8c7b69d-a4d2-3f4d-9e89-6f68378cf121 | -7.78368 | -45.94001 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b84d5f61-7788-3515-9fd1-2f6fafa29d63 | -14.76151 | -49.67239 | 2025-10-29 12:19:00 | TERRA_M-T | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d5153d7b-83ab-3eab-b9b8-f8b35bb1a2a8 | -11.18984 | -48.59783 | 2025-10-29 12:19:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d3d017aa-147f-3529-a06d-20b2d2337895 | -13.13479 | -46.93012 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 929d1f0b-fe8b-36a2-9981-beacffba44cf | -7.62876 | -46.91785 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5a352c20-198f-3cfe-89be-e83d6ccc69d1 | -13.5685 | -47.33823 | 2025-10-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4be127ba-f66f-34e5-8e6d-9c0ab0a49e91 | -9.88978 | -44.88776 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b62c082e-17bc-30df-96ba-8bf22551fe6f | -10.95604 | -48.04356 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 224982d2-393a-3990-ab95-b69b74f94a1e | -12.32065 | -47.44196 | 2025-10-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4fa5185f-1e55-3f63-b2ea-b63afad617e9 | -9.49768 | -46.93454 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8309068b-3480-3da3-ad50-2c15cd3fe8b0 | -10.627 | -47.88957 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1076d589-2be1-3681-b78a-c47816c7265e | -11.52966 | -47.10087 | 2025-10-29 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 60c308ea-edc6-3f72-8aa1-bc9b70b5e27f | -9.16495 | -46.33813 | 2025-10-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 446ef58b-2dd7-3bf1-a5b3-55fdcdf75d41 | -16.86362 | -47.60536 | 2025-10-29 12:19:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 17a053c5-f9d9-3726-9112-0ff9467e9919 | -12.72441 | -42.02195 | 2025-10-29 12:19:00 | TERRA_M-T | NOVO HORIZONTE | BAHIA | Brasil | 2923035 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 30785f9e-ca3c-30e2-87a7-f2e730a244f2 | -9.88122 | -44.87437 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 57db4e03-ba04-3796-9ea0-644563c35de4 | -9.95419 | -47.16196 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| e79fc3bd-9d8a-3661-8077-96996ee4d29a | -8.554 | -44.33232 | 2025-10-29 12:19:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 37a95cce-bfc7-398c-ac03-2d7325ba116c | -9.81205 | -46.9934 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 4c2b43d5-992a-31e0-a5f8-ff3bb8ce2e11 | -12.35632 | -50.15618 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6d98d9a0-16d1-3018-9447-df2b95435bf4 | -14.41737 | -47.86606 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4fac3a7a-517b-3dca-a0aa-eee2b3e90329 | -15.7946 | -45.19115 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 48805167-6db8-39df-ba26-8b24194df0c7 | -7.69515 | -46.89919 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| a7478c9d-a028-37a6-8d96-207181a16903 | -13.21079 | -47.0502 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 705cf9f2-de1a-3fda-a9ab-213e5f30fe8e | -9.16534 | -46.28188 | 2025-10-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6dfa829b-29c2-34aa-a4eb-904f3153447d | -11.29969 | -47.56284 | 2025-10-29 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 6c72762b-bc5e-3782-b45e-c7a589063db1 | -8.8433 | -46.93372 | 2025-10-29 12:19:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 574da01e-e528-39be-a495-bee5b374b03a | -10.17313 | -52.03688 | 2025-10-29 12:19:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ae0bbb26-c213-31c6-b61f-6072c60e1c96 | -13.24566 | -46.53154 | 2025-10-29 12:19:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b122a941-8138-35c1-b467-8b6e2f88d7ca | -14.23651 | -48.10896 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 02f8ef8b-bfd4-3fa8-969f-9b13234dd046 | -12.31891 | -48.04618 | 2025-10-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 5e347df2-631c-3bbd-b4cb-1da6c5c8f0b0 | -10.38762 | -47.5598 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3142d254-e7e0-3d10-a3b1-1e45807bf8a7 | -13.64783 | -47.03179 | 2025-10-29 12:19:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a865dfc1-ccb7-3c11-9234-1ccc639d5d7a | -14.48143 | -45.2597 | 2025-10-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c05be4be-07a6-3873-bf75-d672f11487b6 | -11.57969 | -47.929 | 2025-10-29 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b5131d58-ead5-373c-a166-64f25ed8354a | -12.69256 | -46.3215 | 2025-10-29 12:19:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4efcd888-4e08-36bb-ab44-0bb572510cee | -8.02451 | -47.38042 | 2025-10-29 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b8c59a56-4181-367b-b3b6-1deda4872393 | -8.19358 | -49.71382 | 2025-10-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3fbeb603-2f8a-3e06-92fe-70002044da22 | -7.77754 | -46.51302 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 7138d712-21f4-325c-ad6f-6f5892c99f28 | -10.2269 | -45.93557 | 2025-10-29 12:19:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| feff2827-a1bc-3671-b497-7b2c19b71e81 | -13.03397 | -46.73743 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 39b7e0dc-ae54-3d26-8d31-bbcfae45ed9d | -12.10176 | -47.15453 | 2025-10-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| e05bd0ed-5f2d-3ff5-a165-717c9e5d73a1 | -10.21452 | -45.95498 | 2025-10-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 598ee331-28dd-3ae8-8d18-0811f98979cb | -13.94832 | -48.46239 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a7e27095-26ed-335b-87b6-c80ed4313b4c | -11.19865 | -48.5991 | 2025-10-29 12:19:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c39f8336-d551-3013-8ace-a92f0773a08f | -8.82585 | -40.99672 | 2025-10-29 12:19:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 45.5 |
| c043f901-321b-3368-b0d1-b2472700cf1a | -15.66023 | -41.29654 | 2025-10-29 12:19:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 0af9f71e-140e-3090-a398-63994cc8eadd | -13.7447 | -48.39576 | 2025-10-29 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ec538c0-e66b-3241-bd4a-09ac03742225 | -13.42004 | -42.33728 | 2025-10-29 12:19:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 27.5 |
| a35e9a2c-b452-3656-b197-2d543a57b335 | -8.26101 | -46.34972 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| fe6d15a7-12c8-3013-a9df-8d928ec3a235 | -14.46507 | -48.32196 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d1618c47-caad-31e3-81de-f0a1833a4550 | -12.00514 | -46.78744 | 2025-10-29 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| efed49ce-29c7-3cef-a73a-df5abb365873 | -13.62031 | -42.51097 | 2025-10-29 12:19:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 7a2e3488-5813-3bae-bc06-d60fb0a9a343 | -8.51208 | -48.28191 | 2025-10-29 12:19:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 22118da7-2842-3288-be60-c734cc7fe3f0 | -12.8811 | -48.63337 | 2025-10-29 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f3ab8f3d-bf5d-3489-899e-230ecf1b7129 | -11.57399 | -49.5796 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 9e6bb37a-1ba8-3264-a989-fe9db1c0de68 | -10.23042 | -45.94313 | 2025-10-29 12:19:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| cf2faee8-5d3d-34ea-b22f-5a833932408e | -15.11666 | -47.93542 | 2025-10-29 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f57a21b3-827b-3ef9-8bb9-7273cb9e650d | -12.28843 | -42.74039 | 2025-10-29 12:19:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 9646c8a6-e467-30c1-a78d-bcb6dce569a5 | -8.16244 | -46.9921 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6d222e19-19be-3513-b5f2-0a0349414ce5 | -9.24022 | -46.3384 | 2025-10-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| a5ac9f42-b354-3b40-8e42-0cadf07242ba | -7.9526 | -45.45211 | 2025-10-29 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| ffe01ef4-2e06-3123-aa36-91e2272d6be9 | -11.47854 | -42.76709 | 2025-10-29 12:19:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 34f5ca73-e58c-382c-b7f0-f3abb8bd8018 | -13.72949 | -48.77217 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 22f58924-083b-33da-a914-3d9eaee00114 | -8.25704 | -46.9092 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 146f55e8-e579-32e1-a93a-30576a12f49c | -11.9972 | -46.77617 | 2025-10-29 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 486ef0fc-74e4-36f9-8d74-9750894cf1bb | -12.11466 | -47.26449 | 2025-10-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3ab0902a-e144-33a6-8808-7fafd144f564 | -11.67327 | -47.25996 | 2025-10-29 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 15097513-3bd5-3a47-a7d5-c7fd3b4d75ba | -10.9249 | -47.60735 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 751d35bb-d0ef-39cc-8236-44b3b6a49d87 | -14.97073 | -48.19558 | 2025-10-29 12:19:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 99f9294b-fb9f-3777-b199-337565f8b5ff | -13.73077 | -48.76306 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |


[Clique aqui para ver as próximas entradas](README82.md)
