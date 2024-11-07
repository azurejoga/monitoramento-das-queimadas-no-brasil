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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b47d054e-1942-33ea-baa9-5a53366520b5 | -2.0306 | -46.987801 | 2024-11-07 00:31:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d09286ed-84cb-32c7-ae5a-a359e3ae6e29 | -3.0244 | -53.258801 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64d07f71-d2b4-3663-8390-f4af6d5037c5 | -2.2421 | -53.654701 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5182717-ac2c-30c9-b229-806c2b10208d | -2.1724 | -46.437901 | 2024-11-07 00:31:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5faf873f-56ea-37a7-bfd7-6499db57273c | -3.3202 | -51.562199 | 2024-11-07 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55e35958-4517-3567-ba37-dc3651f839b1 | -2.8228 | -52.9557 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee4716d6-e653-3e74-bf3e-b70c67c0940f | -2.6021 | -49.257801 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 809609aa-dd88-3b3d-835a-5768186ae0ea | -3.9596 | -48.1581 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe5f9cc2-8c21-300d-97c0-50cd2caa5a5e | -3.287 | -53.104 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc45ca73-4369-327c-8e5a-e021cec5400b | -4.089 | -51.004799 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7595c46c-3295-3ab5-9bac-54b465ba81f0 | -6.0789 | -44.724701 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c6aa135-e504-3afa-87f7-d40013133d97 | -1.9801 | -47.172001 | 2024-11-07 00:31:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e9b64a3-4501-3bd8-a86d-d87c10e7dd02 | -7.8553 | -48.209099 | 2024-11-07 00:31:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01594d21-b496-33e3-86d3-3d7df3d69b7e | -4.6763 | -46.379002 | 2024-11-07 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 998a634b-b083-3282-83df-c6380eef30eb | -3.9627 | -48.171902 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e64e011-ae6a-358d-a0c4-ee9015e06fbf | -8.3063 | -43.610199 | 2024-11-07 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c56529c-5e75-31ae-846e-c8cfd2b01650 | -2.8121 | -48.551701 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50d9652e-38af-3d42-84b4-39d4edb45f47 | -3.5262 | -50.333302 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ba42b8f-f2b7-3db2-9a69-27e12207043f | -2.3984 | -53.620399 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f7f42ba-04d3-3944-bead-d0b1f2b80cf2 | -5.9774 | -45.354198 | 2024-11-07 00:31:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c96b7ab-f951-3987-ba6b-108227c5c52c | -5.0299 | -46.84 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 919e09e9-7d25-3d24-8548-f2a664fc615d | -6.9527 | -39.825699 | 2024-11-07 00:31:00 | METOP-C | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b2d4b851-cb87-3c62-93b4-7b161abfd08a | -2.1102 | -49.090099 | 2024-11-07 00:31:00 | METOP-C | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f67b6817-f853-33e4-8bea-d043ff6a2c3c | -2.4959 | -49.108601 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc37e1a7-5461-3706-91b1-97e18d729be1 | -5.3978 | -46.9151 | 2024-11-07 00:31:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2720ff29-88c4-3e0e-bf22-0eb3698d67e8 | -3.5183 | -50.343601 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13c61f5b-929c-398c-8a29-4446e6db871b | -4.6652 | -46.330601 | 2024-11-07 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52a90c75-da5c-3869-9e83-2f7473e8d8bd | -2.0 | -46.944 | 2024-11-07 00:31:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12849d3e-668e-30b6-bb48-a99849426c53 | -5.5495 | -43.697102 | 2024-11-07 00:31:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1abea505-5d9a-3eac-a555-4a7e3dd634ee | -3.2412 | -50.438499 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac54039d-a4b6-3182-87f4-9d5da8516b1b | -7.4861 | -44.649899 | 2024-11-07 00:31:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6403fa70-3f7a-3c27-b43d-f627a532280a | -3.2449 | -50.4547 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b84127fc-bc05-3451-b906-52fa57e45d4a | -4.4237 | -47.255501 | 2024-11-07 00:31:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d11a43ad-553c-3d2a-8316-b04b67cd1724 | -6.5337 | -44.4618 | 2024-11-07 00:31:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ee4a54a-ea50-3e8a-89bb-f2f3a6853008 | -6.229 | -45.326801 | 2024-11-07 00:31:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c15544c-293c-3bd5-bc5c-6a37ac4bd263 | -3.0003 | -53.425701 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f73dfc57-da49-3845-9272-e6dbc2c4d734 | -5.9791 | -45.361401 | 2024-11-07 00:31:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7d44978-1c02-3872-80ef-5d724e591eb1 | -3.6588 | -50.2369 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e1db133-e516-35f6-9685-be9377e177df | -1.7224 | -45.783901 | 2024-11-07 00:31:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8c4ae2-7e5b-3753-99cd-5ad22d904286 | -2.8129 | -52.911499 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85239543-2cb4-3f48-9693-da31d8d8b2ad | -2.6519 | -48.572701 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17cd03ae-3d0e-3826-85ec-5fcf8d908669 | -3.6606 | -50.2449 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f083e6b-8a5b-3d13-ba58-73025dbf6a15 | -1.0244 | -47.0536 | 2024-11-07 00:31:00 | METOP-C | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18390742-b6d2-3946-baa7-3c2d92bcc65a | -5.2264 | -44.919899 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db6d7c3e-65d9-3257-957a-de71344a0d4d | -2.5996 | -51.739799 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5fecb9d-1fcf-30bc-8896-93107eed3015 | -2.3957 | -53.608299 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e02185bc-a366-3832-b9a0-a09120608c5b | -4.091 | -51.013599 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cecbcc2-a194-3ab8-a9a0-5c5aea7237c5 | -6.5509 | -39.6572 | 2024-11-07 00:31:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d99dbaab-3972-3cbc-8cbc-c0011dbfcd05 | -4.6766 | -46.3353 | 2024-11-07 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c64f1858-dac6-387b-8ca9-3d20ec1c000c | -6.5008 | -44.674702 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38681f8a-5868-39d9-a84b-216330cae649 | -5.0185 | -46.8354 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7db4244e-0d86-399f-8076-e499107f3f8f | -2.4032 | -48.431999 | 2024-11-07 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e745e4c8-a457-3ca4-b51e-19108b0c5e99 | -2.7359 | -51.887501 | 2024-11-07 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a63f100d-3a4e-3329-b623-62235251c137 | -4.6779 | -46.385899 | 2024-11-07 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51a96cf5-528d-34e1-bc60-ad206b12c639 | -2.6087 | -49.196098 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10f9cda8-4325-3527-b344-ff6eaaa86641 | -3.0199 | -53.421501 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64c34a86-92c7-3953-b245-185b9dfa112f | -2.5073 | -49.113602 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9ed3ce5-8593-355d-b0ff-47ef613bd69e | -7.4844 | -44.642601 | 2024-11-07 00:31:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3506804d-7a20-3cb0-848c-9bb68b9251d7 | -7.9039 | -46.689602 | 2024-11-07 00:31:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28ff37a0-4ccd-367c-9d4b-e5401bd576b3 | -8.0861 | -44.433498 | 2024-11-07 00:31:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af8e7d61-6267-3f68-a8f0-e3aff9478a2b | -5.3693 | -46.251598 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a77199b8-9430-3ae3-8922-267e6a4ed852 | -4.5773 | -48.064201 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d960a34-3d64-3621-a7d9-728f60a54431 | -1.4836 | -47.211201 | 2024-11-07 00:31:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d34ae508-075a-397b-a162-61462f48705b | -2.6087 | -49.241299 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c793b6d-1b5a-3a3d-87cd-2b591b3dd4ee | -2.6774 | -51.811001 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 150b2687-ac88-355f-a904-19a0cbe83762 | -2.8131 | -52.957802 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7fe6bf6-6c70-3f28-b4ea-9a3073442674 | -10.3671 | -49.160099 | 2024-11-07 00:31:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29a7a79d-83c5-34cd-9fd1-2d18cea52d66 | -4.5758 | -48.057201 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb758425-96c2-3447-b255-7fe0c01754c6 | -7.6213 | -43.551701 | 2024-11-07 00:31:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 037cb07d-9fe7-376c-9969-bf9b70cbb8bb | -2.2605 | -46.462399 | 2024-11-07 00:31:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c24b12b-ed05-30c0-8502-8897905ddc72 | -14.0686 | -44.141201 | 2024-11-07 00:31:00 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee0070b8-eceb-39cd-9464-474b25c06720 | -5.1143 | -43.954102 | 2024-11-07 00:31:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dbd5f88-1469-30f7-be1a-afe79bb0b1a5 | -3.9647 | -48.135201 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77ba7568-6a15-3b87-8711-b77036844cda | -5.0511 | -46.8424 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b005234-d6ab-3425-8b98-45aea225b75a | -2.8178 | -52.933601 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10b6497a-6313-33b0-9e70-2c9bb64cdde9 | -3.0075 | -53.411598 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16b22744-41cc-393c-8fcd-fa7d7747e3b0 | -5.3245 | -46.1017 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d0b6eb1-6736-35cb-b9f2-3218f3e65f4b | -2.781 | -45.142899 | 2024-11-07 00:31:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f174bb50-5580-3380-a374-94ad45ef08f1 | -2.8713 | -49.5345 | 2024-11-07 00:31:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59330318-c7fe-32b1-b6a8-50d4ef41638c | -4.2217 | -48.5396 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9be1bef9-a938-30b1-b357-f9214bb4e3be | -2.9462 | -53.275799 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4d60029-bea0-3c5e-b255-9c34170a6851 | -7.4072 | -44.798901 | 2024-11-07 00:31:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0d1a96f-46f6-3ff7-ba60-f8ce4326c1a3 | -2.3999 | -46.171501 | 2024-11-07 00:31:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca56c60a-cda0-37f9-a0b4-706380609872 | -3.295 | -50.084999 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 715266a1-78dc-3f32-9f00-dfbbdd14f51c | -6.4581 | -44.6688 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e593a0ba-fc7e-3289-94cd-0a5754e331da | -2.9588 | -54.153198 | 2024-11-07 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b8c6b4d-04fe-38f0-b3b3-f71fa4de7b8f | -5.4083 | -43.316399 | 2024-11-07 00:31:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed8fc00b-d233-3a83-ad0a-485cefa7b4cc | -3.7964 | -50.618301 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75ac3a44-b04b-3318-b7e4-f34ef3ee49b6 | -8.0256 | -49.6245 | 2024-11-07 00:31:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb662bf5-5444-3163-95c3-1def9345f873 | -11.6081 | -44.126202 | 2024-11-07 00:31:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f387dc6f-c218-3656-a7eb-b1f5904c84bd | -1.4195 | -46.797699 | 2024-11-07 00:31:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87864a35-57d8-34d8-892c-18e387944fde | -6.0469 | -46.596699 | 2024-11-07 00:31:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e5ff8f1-7be4-394d-96dc-72ba65d3b791 | -5.1163 | -43.962299 | 2024-11-07 00:31:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e90d4570-3186-3581-b79e-4c21531e07c8 | -2.6038 | -51.7584 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0be6a1cf-80a4-3f25-a276-55d9572b1ddb | -3.7799 | -50.134998 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2395c173-afc3-3649-95b2-501134940541 | -2.5285 | -45.656502 | 2024-11-07 00:31:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 476d837b-80f8-36c4-9f00-aaf0e15aa3ef | -5.5448 | -47.0616 | 2024-11-07 00:31:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4baddd4-b892-3a44-a092-e9f0050745b6 | -4.8082 | -50.819901 | 2024-11-07 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5a32c2-fa0d-3416-a5ad-17693bf9648d | -5.5173 | -46.536201 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c840ca85-abb6-374b-8f61-2774c90873f7 | -5.4396 | -45.127201 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
