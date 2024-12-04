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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a40d286c-5fe7-366a-8d68-8b46fb51aa02 | -4.32325 | -48.09874 | 2024-12-04 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1b998afd-de31-300d-85ee-55345755e99e | -1.65429 | -52.37922 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d2d0f7dc-4129-3a99-9af6-0d9800716d08 | -3.54819 | -51.33604 | 2024-12-04 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 810ca336-9b19-3b9e-be85-d955dbf324c2 | -1.87579 | -53.29554 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bb1fc2bd-ff32-38cb-b4fc-8cb4e3d1a457 | -3.7234 | -51.08067 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 01f29dd6-163d-310b-9f42-409315ce3f2e | -2.72679 | -51.82267 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 2042b434-e9a1-3730-8c51-051b26908ce3 | -3.57285 | -50.30862 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cd5f6903-ba1b-338a-a1a3-a57c4d1d1f59 | -1.68915 | -52.33514 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e72478ce-d89f-3a4a-8ade-4f1528b27145 | -1.69349 | -52.61027 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3445fada-b86d-3efd-ad1e-ea029a43d045 | -3.17484 | -54.32414 | 2024-12-04 05:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5fb268a0-34a8-345d-911f-83f1345de7cb | -3.11737 | -54.62703 | 2024-12-04 05:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| ffddcdcd-41c5-3ce0-be08-eaf12e4adfee | -3.86698 | -48.36067 | 2024-12-04 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5fbdd954-1c03-3eb8-a5a9-651c0ea1d847 | -3.92386 | -52.39487 | 2024-12-04 05:44:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ee0cedd6-0386-36d7-9a75-a0438a3f9b28 | -3.10697 | -54.62539 | 2024-12-04 05:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| bbbb35c7-8ed2-37ec-ac89-c73c7b5387ea | -3.09146 | -52.39794 | 2024-12-04 05:44:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d0071a4-20e0-3541-8a2f-bca01f28fad3 | -3.25349 | -53.62058 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 08ac9826-3eee-380a-9d3f-fb4d0a926e10 | -2.89192 | -51.57771 | 2024-12-04 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c6a63d78-8e3f-3b5b-8e9d-48c0b96c3924 | -2.79926 | -53.03788 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58a0d86f-8f27-3a02-9bf8-0e1f2fb369fd | -2.81657 | -53.05074 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| f8c8ff2f-c3e6-3c0b-b440-0593ceb2bb76 | -2.56974 | -53.99731 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fcbf891e-0ab3-32f9-b402-bcd9f10109d3 | -1.61668 | -53.52234 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cab57b8b-9ff7-3f92-912c-70f8d61d2ff2 | -3.173 | -54.33604 | 2024-12-04 05:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fe7b424a-b3d4-33e8-a82c-5c33650fb60f | -3.79097 | -46.69664 | 2024-12-04 05:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8c81b956-ce8d-33a6-b77e-015c05376768 | -1.75416 | -52.62584 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| f17c9668-b301-337e-8459-e4e5aa211fef | -3.18985 | -50.64266 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce7d16bb-bfe4-3f78-9011-17a3aeff79b1 | -3.06415 | -54.04408 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2a9c21cc-b3d0-3308-b4f0-0e67051695e4 | -3.21325 | -53.12413 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 106e107f-4023-3430-bc74-08c5ead060bc | -2.99654 | -53.82024 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aef2a7be-e664-3dd0-a251-19335bd5c61c | -3.11492 | -53.98731 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 171d496f-4470-3368-828b-64cba8ca0d53 | -2.44085 | -54.03753 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f0ca0df6-5ae2-3764-8be0-6a2e26b730f2 | -3.29047 | -53.70312 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5f4725e6-e4e0-3965-ae01-47f0a9be2ee5 | -3.37322 | -51.09114 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb4bb56e-cfd3-34a5-9bdd-3557a26c2738 | -2.82972 | -46.75351 | 2024-12-04 05:44:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9fc8ceba-3647-3890-ba44-9145d49098c9 | -2.87743 | -51.79593 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 53feff1f-3954-3bd2-9e41-a3b773c4681a | -3.2512 | -50.61251 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dcd22b68-e0a3-32dd-a8bc-7a1b19c5143a | -2.82236 | -54.14949 | 2024-12-04 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 66262951-d7c4-3b11-b766-6f69bd30da42 | -2.1963 | -47.24039 | 2024-12-04 05:44:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 36366c27-6a99-3d68-9eb3-a33d35283b98 | -1.65284 | -52.38887 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6e5abe02-cd14-3e29-8a45-59a90d743c6d | -2.82599 | -53.05214 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8cd035f2-209d-33dc-9cb5-b3db9b87b8d4 | -1.74634 | -52.6146 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c7788cb7-9acb-3202-aa8b-9588d8fa67dd | -1.89603 | -52.84274 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a39b10ef-8876-3a98-89d3-59a0308d5af3 | -3.11932 | -54.61446 | 2024-12-04 05:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 303.9 |
| 20cb046b-c4fa-36a7-8518-b4a391cdcd8a | -2.5756 | -53.68134 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4ee52770-48eb-3811-9e12-79b39104b1e5 | -2.25279 | -51.23127 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18cadbe1-b9ab-3124-b412-89ac51788870 | -2.69211 | -52.90708 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a3036ab0-a14f-35de-96e1-fc16eeae7b84 | -3.3719 | -51.09992 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 799d7e3e-f475-3f3e-ac4f-4c5f4401f69b | -2.62128 | -45.72645 | 2024-12-04 05:44:00 | AQUA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1b1b7887-7813-323e-9c41-71cea0998661 | -2.72541 | -51.83176 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 501e6bd5-672c-38da-967e-7d87352a8550 | -2.78583 | -55.34799 | 2024-12-04 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0e05f16b-a92d-322b-8e10-464c8b1675f9 | -1.2354 | -51.6014 | 2024-12-04 05:44:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3c1a5486-9fbc-31d3-91e5-86145ebb0d14 | -2.80713 | -53.04936 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 202570b5-1448-3693-9ed8-d9674a30e49b | -2.80559 | -53.05946 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| d04d5c98-de03-3c8b-a66b-0f8691ecc948 | -3.97428 | -50.51841 | 2024-12-04 05:44:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f783af2a-be21-3709-a867-997e642e1ed3 | -2.97826 | -53.87382 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| efa65859-b02c-3fd8-855d-9389026c6f23 | -3.09853 | -53.27759 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34deb2ea-fcc9-3124-92ef-a6230a613c74 | -2.94022 | -51.0153 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da48a974-26cf-307f-a611-a5f394d1aaa5 | -1.17093 | -53.4245 | 2024-12-04 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 575d12b1-a901-31fa-981c-58c8f76c1259 | -1.89448 | -52.85282 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 603938af-2876-30ce-bd76-fbf07520b23a | -1.67576 | -52.79117 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0babffd2-d28c-38a5-9f50-07c1131a8d8f | -1.89073 | -52.84557 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b80e3fb9-f0c0-378c-89f7-b2638b2f2ae6 | -1.74015 | -52.61713 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 37b634e4-fde9-3555-92c4-69f5cb209fd2 | -3.25988 | -53.64337 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 40485c84-8c6c-3c26-8d55-037648c7ac4e | -2.82419 | -54.13771 | 2024-12-04 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b3f15882-7187-3947-94ed-d2dd0f267dfb | -3.84797 | -52.16184 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b148c707-d6d0-393b-aebb-e547942ddaee | -3.1089 | -54.61302 | 2024-12-04 05:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f872fa34-f422-3293-94fb-240659ca118a | -3.28881 | -53.71407 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4775fc80-b054-3380-8a9b-aad798c6a5ca | -2.94803 | -51.40075 | 2024-12-04 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 69345a72-bcb6-3ef2-ba5e-a784909a18d3 | -3.60214 | -50.79614 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4cd57600-d117-35f9-9c4e-523c5850dafe | -1.64821 | -52.04811 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7425564e-d1d2-3b83-9826-b8bc029e3ea4 | -3.09856 | -53.75132 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 11434b91-00db-3f9d-a297-8de232340a91 | -2.88567 | -51.81216 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 870753aa-e684-37de-bcf7-68f3b200482c | -2.22473 | -53.69542 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ecd32dd5-10b7-3399-a9ed-14f9336d8310 | -1.72289 | -47.05146 | 2024-12-04 05:44:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 74f55c57-ba03-3d52-b1ab-f546131de7e3 | -2.87214 | -54.02629 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ef2f0f2c-aa20-3c75-a338-43428c132ade | -3.41167 | -50.27283 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 453fe98d-cae9-392d-8a09-d3ac461fe3be | -1.61496 | -53.53357 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 83e60bd7-3ae4-3922-90d5-fca80c99e187 | -3.54817 | -51.51683 | 2024-12-04 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8ce66865-fbc5-3d7c-b482-d4e1dc918b41 | -3.78031 | -50.9601 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7bc086a7-210a-3fbf-a180-74de5f42a4bf | -2.56848 | -54.80776 | 2024-12-04 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e35bdc0b-7fdf-3a33-b22d-89fc32cb9211 | -3.36835 | -51.06349 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c9d781d5-bf72-32da-b6bc-3f97e962d523 | -2.41302 | -54.15403 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b0d13a45-3c22-3196-a816-966d3dbd4da6 | -2.46829 | -48.03997 | 2024-12-04 05:44:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b3186267-f253-3319-bb29-0be669b85f08 | -3.259 | -53.659 | 2024-12-04 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| cc8ee861-cb5d-3a76-b39c-ec3ca44c5942 | -5.5882 | -45.1412 | 2024-12-04 05:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 52bc9abb-161d-3fa1-b873-bf8974b1fbdc | -3.1269 | -54.6263 | 2024-12-04 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 244.2 |
| 01ab04e2-3b34-3a5f-b28c-c89759ad3ebb | -1.7544 | -52.6363 | 2024-12-04 05:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 6f5b00f3-cd28-32aa-b9f0-172265bf8168 | -3.127 | -54.6063 | 2024-12-04 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| f7b41e9f-b526-34e8-a67c-9f22a2452d14 | -3.2774 | -53.6585 | 2024-12-04 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 361fc618-e382-395e-badc-be975e307c4a | -3.1086 | -54.6268 | 2024-12-04 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 7bfe2f44-d139-3585-9931-3fa410315c98 | -3.259 | -53.6388 | 2024-12-04 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e3180b1c-3838-3a4c-b5df-e3075245b677 | -1.7545 | -52.6159 | 2024-12-04 05:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 3c3247ba-638c-3420-be0a-43e7b0a40d72 | -1.7361 | -52.6162 | 2024-12-04 05:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9a2191fa-e094-30c5-b057-4b09407980f0 | -3.1453 | -54.6259 | 2024-12-04 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 282e7b79-4f6e-3aff-bcdf-e80ff9445ffe | -2.8196 | -53.0629 | 2024-12-04 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b0990e19-6c67-3bff-9ad6-c19b622f0dbc | -2.8197 | -53.0425 | 2024-12-04 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 90f67110-29b6-3413-87d4-863bcb80c6b8 | -3.1086 | -54.6068 | 2024-12-04 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 4bab4b1f-c1fc-3365-a74b-9436ca382300 | -5.5693 | -45.1651 | 2024-12-04 05:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 3a7a5dfd-b2c7-3ebf-aa25-758e5dd5b43b | -1.7728 | -52.636 | 2024-12-04 05:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 5f3b508f-28b0-367f-ad1b-516e0a6e8e33 | -5.588 | -45.1638 | 2024-12-04 05:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 526fcd9c-574a-3a2c-a1ec-9ce8d63fbd0f | -3.1269 | -54.6463 | 2024-12-04 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |


[Clique aqui para ver as próximas entradas](README60.md)
