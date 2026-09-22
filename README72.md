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
| 7bb3a2ec-4aef-37e0-99a8-fb73aacf5ab0 | -13.30397 | -51.79741 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da533d7c-62a1-3768-8718-22881758acf2 | -11.74018 | -50.79598 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 189c2562-c27f-37f4-b5de-e86a5387eb2d | -11.50976 | -51.50812 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98d72340-29b2-3a59-a4db-a33ee33c0c65 | -10.91499 | -53.94563 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f8adc54-d72d-3312-89ad-d6f2c59956f6 | -9.56238 | -66.01353 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afb1e07b-a762-327f-a6b2-f3065532c4af | -15.74998 | -43.30369 | 2026-09-22 04:49:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a3f39ab-2a85-3acb-80b9-b1c223f29168 | -11.41888 | -47.34064 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff6da3ac-2cae-33e7-9e18-f3f3bf9844dd | -11.32979 | -51.37391 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d00e649b-aedd-3356-997d-8938716df6a0 | -12.93508 | -50.9358 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a5088fd-6b4d-3bec-9d65-49f50716e6dc | -14.755 | -48.43913 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edf85acf-4151-39c8-be30-779d0280d175 | -14.76535 | -48.45122 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfff7ea4-52ee-3fa2-90ef-d4fa04e3af5c | -13.86482 | -48.5738 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c124c5e3-b4e1-33a8-9545-59b47dbcf91a | -12.68547 | -50.9662 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 209ad5b9-8453-35c0-92fa-549dc8c331c6 | -13.71975 | -48.78894 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db694168-8abe-38a2-875c-35f5198b66e7 | -10.60609 | -53.98645 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 1167b3de-75bd-3170-9a50-49aa7396a83a | -11.84593 | -46.8194 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a3491d9-4f21-3d14-8c0e-b5c217753015 | -11.20197 | -55.03248 | 2026-09-22 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7782f1a9-5429-343c-b57c-48b5a9f11914 | -9.55486 | -66.03106 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 785ac526-5323-3165-99d6-1bda95e3fa8f | -11.46234 | -47.75526 | 2026-09-22 04:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ab4491f-ab5a-37ab-aaa6-98638d9c7800 | -14.76207 | -48.44599 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 40b7c741-82d7-3b4f-9eb5-434cd55addad | -11.4716 | -47.74632 | 2026-09-22 04:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb6a3eb0-be64-31e0-a46a-cbfb4e86b1a1 | -13.92634 | -48.5819 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5c2027db-de0c-3338-95c8-cdca4ea7e9af | -13.85745 | -51.84416 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a3e50e4-a792-39a8-b6a5-d85bc8f70952 | -14.05012 | -52.05203 | 2026-09-22 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6705af66-784a-3583-8895-845b6cd872de | -13.50028 | -51.86918 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2655428-e571-3ec8-97d5-94a778570be3 | -11.80329 | -49.80861 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 837eb393-937e-30b9-a4c7-904c5bc0e21d | -10.9132 | -53.95674 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0de9c42b-f72b-3f60-a081-71c0ed339c45 | -11.98667 | -50.01239 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f5e20f0-2d0b-3f8f-85c9-ea27f5d4e5ea | -11.49917 | -51.48825 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7199b1b9-06d7-30d2-866c-3b9a16ad2fab | -10.61229 | -53.9913 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17bb3b32-f632-3250-8fe5-48a96e363555 | -15.35395 | -46.53637 | 2026-09-22 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fe2d3ff-fff7-3dd5-8a1a-a1fc3a65662d | -11.96385 | -46.52074 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f750b50a-a5b5-3a59-937b-eefa64b6f9e4 | -11.8553 | -46.81291 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0741800d-0401-31ac-9597-c14775e00a2b | -11.44441 | -47.33329 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 60d2e16d-3deb-3c70-9393-ff892551eeae | -10.97864 | -50.59399 | 2026-09-22 04:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a337cbd8-e8cb-3d84-adee-034cbc6d2e1c | -11.25823 | -54.14657 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7de6fdb9-01d0-3659-89f3-87122e8f2ed2 | -12.57114 | -45.97496 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 273395f4-8c99-325d-9a3e-47ae618bcca8 | -11.33197 | -51.35965 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0386b509-4034-3218-aea3-2a840e079c50 | -10.90801 | -53.96725 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f0df9b0-9600-360c-a153-01d5af7a21e6 | -12.02255 | -47.8176 | 2026-09-22 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af358895-f437-30e9-a2db-7a988af6925c | -12.89004 | -51.02791 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf8e697b-34a7-380e-9fea-0f2e95df35be | -10.14902 | -58.75993 | 2026-09-22 04:49:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59e15c50-3938-3c83-a640-c20e27157a34 | -13.36778 | -51.3046 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b8a1f9f-1bb3-330c-87a5-62f50b60ef26 | -12.77718 | -52.85205 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f78d67b0-1038-330f-9ba7-446b4cffd1cb | -12.14098 | -61.16648 | 2026-09-22 04:49:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bb785ad1-a47e-386a-9570-b4da89c6def3 | -11.75715 | -50.82127 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d673aabd-8f7f-392e-b476-146fca8b2f82 | -12.84245 | -44.34463 | 2026-09-22 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 58cc0cc3-a938-3d2e-88ba-488dcef47487 | -13.27784 | -51.78954 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| becef975-fadb-3dac-abc9-20778ee5bfae | -12.77112 | -52.84746 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40c3d4da-bb99-38a8-b97c-3af89075eb1e | -10.60389 | -53.97845 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| a51db363-9e56-350b-9fda-d8bdb659b064 | -15.8587 | -49.8933 | 2026-09-22 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9af0ba6b-1e67-3675-9a2d-b5ed65c1b238 | -11.4304 | -47.34618 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee8f5216-dfc3-3a18-8964-9c5c22201b9d | -12.30026 | -50.70605 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d7108f8-acaa-3d4c-a949-3b920ae1415b | -10.60209 | -53.9896 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d18bf0f-3990-36ad-a6d2-cda0121258c2 | -14.68035 | -45.67677 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 456db3f9-4363-3053-81d5-f2104d387eb5 | -11.15956 | -51.10914 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b5e870d5-0ce4-3b5c-80de-cb51a5255e56 | -10.87184 | -57.16807 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31508424-4d29-374f-85ba-fd2bde19d970 | -11.68341 | -50.98985 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecb0d1c3-44ca-3c68-9f81-ae91dde5f8a1 | -14.75819 | -48.44514 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 88479ead-f719-3690-a603-c1c71e0e0947 | -11.32002 | -54.04967 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 317f8610-511a-34b5-aa0c-cbcf40e88068 | -14.16457 | -51.78834 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94df35d4-ad0c-3c53-8297-d179ac6b8830 | -14.17761 | -47.8795 | 2026-09-22 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 400facbc-959c-39e4-9ba3-e7b1a0c233ea | -12.56774 | -45.97634 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| fa6690e4-6213-397e-a5c0-013d1169704b | -11.41627 | -47.3475 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 158664d0-762d-3bf0-83f9-3a76c57bfcf7 | -11.04779 | -54.1469 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c7b72e6-c12b-3632-b220-f524fd1d0400 | -14.58831 | -52.17785 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82dc6c47-43e3-346b-9cf4-838f0c67d84a | -14.16792 | -51.78888 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76c65f39-3b48-3dad-9bb0-0b1616064f1d | -13.21936 | -46.93184 | 2026-09-22 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cf412bf-1d4c-3f64-b676-40403904bb5f | -13.43186 | -46.32485 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e2ca188-4ef5-384d-a0de-e1dffe1b397c | -14.16511 | -51.7847 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d7da08b-fd25-38a4-a4fb-4036dd83263d | -11.44292 | -47.34429 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e50d60b-6bd0-3402-909b-902bd004765e | -15.44167 | -48.4484 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b4f9b98-2c6a-3520-9fb2-1e0f49911e68 | -12.89565 | -51.01358 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06c5824b-6950-3857-8d00-8f628f75a3ff | -12.60264 | -45.09121 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23161c0c-db82-3a81-a4b7-d78fb481419f | -13.28219 | -51.76073 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36ad54ac-2a1c-3a0b-be8a-addf55808268 | -12.3132 | -50.18763 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c31cafe-d543-3b21-ba06-e0874ac86321 | -11.15621 | -51.10862 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ce65b80-5ba1-35c7-b3da-53b2efb36879 | -11.4253 | -47.35379 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2377ee14-e8a2-394a-8ebe-fdd0b3d6c941 | -9.28468 | -60.63453 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57804e23-6b94-36e2-a632-ab14e4be3d7e | -11.95581 | -46.51602 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0bf2d968-f671-32b2-85ff-1619b4133227 | -12.14547 | -61.17047 | 2026-09-22 04:49:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6426e85d-d3c7-3bd9-8368-087e6a6e4dde | -12.43979 | -47.01198 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b28752c2-940e-3f75-9a67-532095cc7e88 | -11.31663 | -54.04911 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71a669f6-bf5d-3c96-975d-79d3d2b73337 | -11.41731 | -47.34015 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2443c11-040b-38b4-970f-739c4e9840c9 | -10.58508 | -53.9868 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b8533e8-304c-3b68-b001-62a063802884 | -11.25544 | -54.14226 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 767cac21-b24b-3f18-8936-a6bce18ce9ef | -12.29405 | -50.72426 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4712d0a1-3676-3d5e-9562-99b608ad3c2e | -13.93219 | -48.56808 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a64ba26-abe9-33bf-b935-d22ac7032fb0 | -14.58776 | -52.18143 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9c20e82-2cc0-3a68-b45a-048fcd62d8ee | -14.93707 | -49.88654 | 2026-09-22 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b103c89b-a692-34ef-a1e7-32e8a92fcfb7 | -9.2841 | -60.63765 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd46cbab-a395-3daa-95f0-fa68dd6ae0a7 | -11.87927 | -46.85562 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8517ceb-4547-35dc-81f2-3b68ba58d18c | -11.70251 | -51.0003 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 73ba0c18-447a-37ab-be6b-77de1ebad688 | -15.98403 | -42.99987 | 2026-09-22 04:49:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e69219df-1a8f-3b8e-8bde-96f90185cc27 | -11.69014 | -50.9909 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 865b5a74-3125-3ad9-a2a2-8fc5a72887e3 | -14.04679 | -52.0515 | 2026-09-22 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0595a866-a95b-3f5e-9f58-f54a8ed2108b | -14.34866 | -49.04696 | 2026-09-22 04:49:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90510fc1-dc0c-3bd5-a18f-e1c88f99b6d2 | -11.04935 | -54.15869 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc6aca86-663c-3e5d-bc04-ccf635931419 | -13.30282 | -51.78247 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95f0e847-945a-34fb-8059-030dca2a07b6 | -13.5192 | -51.5238 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README73.md)
