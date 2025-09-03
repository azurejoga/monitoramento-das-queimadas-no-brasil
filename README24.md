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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2aeac42-d5b4-319c-b87c-bc58420dff08 | -5.74098 | -39.76346 | 2025-09-03 03:32:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd518590-466e-33a8-9bcf-798a164af21c | -6.19603 | -43.34375 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0fb68ad0-5b85-37b2-99b0-ac5f52f19c8e | -8.8825 | -45.833 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b7c78279-a587-3947-a650-852e51d30604 | -7.80012 | -45.44976 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d959a106-8cf6-38e0-87ef-c43adf78f074 | -14.06459 | -44.56496 | 2025-09-03 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95940e84-3c5b-316f-9aca-79983eae53f7 | -15.71985 | -47.66651 | 2025-09-03 03:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4815305e-f88c-3ccf-ab79-e7994dcd56ef | -13.30966 | -46.82286 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c816565-d239-31c2-bb20-ea98bc28e9ea | -11.38173 | -43.57022 | 2025-09-03 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| faf226ea-dbe2-3e69-bceb-2fefd9c178cc | -11.90016 | -46.6676 | 2025-09-03 03:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aded0ae2-d02e-3c63-a7ba-f42f82c47834 | -10.14096 | -46.29664 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8909754-0f63-39b5-98ca-e686f51b835b | -15.55086 | -48.32304 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e5660e9-e839-3fe6-9f50-275018ebfe4d | -11.11227 | -44.64657 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 427e7bca-a61e-3d30-8cae-6f77256fb593 | -10.14428 | -46.27562 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d36a64d3-1f7c-3b70-a4b2-87717305bc4d | -14.58712 | -48.04207 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2e9dd49-bb4e-3690-bd15-9a8bd0c00819 | -13.00209 | -48.10465 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36f2aa66-7984-3bc3-9e12-90de99d44927 | -15.57988 | -48.32561 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10c609bc-b027-3e8b-bdeb-d983e12f63a7 | -13.90887 | -48.107 | 2025-09-03 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80d9d7a6-2da3-3871-a012-57a56bdb81ba | -10.1395 | -46.30395 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b20b39e8-6d2f-3f93-b604-8e870193bb45 | -13.33618 | -46.83075 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02099129-2848-3def-ba51-2309b43db5cf | -13.35923 | -46.33476 | 2025-09-03 03:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0feb66c4-d784-3439-89d3-743e98a4e327 | -14.7979 | -48.20271 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3a1eec5-ebcd-3e48-845d-4df6875da603 | -15.55595 | -48.39901 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 05fb956d-44e8-3b69-b65f-94b7d5816207 | -13.31532 | -46.82475 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 614aa495-741b-303d-a460-4d7e1bb400ef | -13.30778 | -46.827 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0729f86-cfe0-3983-8fd1-63c1cd812474 | -13.49289 | -47.02985 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 974fefef-f90d-3c4f-97eb-968b2f847479 | -12.84936 | -48.03521 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d89058a5-bfc1-34a0-9841-fe0eccee33fb | -14.78355 | -48.15554 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f9f8c1d-9fbd-310b-910e-39405b48470c | -15.54709 | -48.32161 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6e65bfe4-e3f5-321e-937a-c1f449455989 | -11.1165 | -44.66589 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccd4719d-f75e-3bcd-bc86-89f132ae91c7 | -11.11845 | -44.64777 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 31fa031e-b9ed-34c1-b889-636ca3305802 | -15.58204 | -48.31594 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcfb2db1-1f35-3b6f-a6fb-8a6e0e4f8039 | -11.05283 | -45.40159 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 708ec872-497e-3968-8cfc-d1968ef587f0 | -13.49429 | -47.02326 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a211c51f-92d4-3ca5-83f2-16fe28a76a88 | -14.7764 | -48.15432 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97947600-439f-38ec-97ba-61f0e255a400 | -11.12457 | -45.1133 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8c5e242-0de6-32fa-9172-89401dbddf40 | -15.5499 | -48.36003 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b06da74f-8f46-3a08-919c-dc5a19d1c33d | -14.79047 | -48.15785 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffba8595-8de8-30d3-9fb1-1912b06a2fda | -13.35584 | -46.34102 | 2025-09-03 03:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 132ff832-840d-35da-9209-d4efc95ff351 | -15.55276 | -48.34739 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a1febef-5133-3244-93ab-a48af91d68bd | -15.56245 | -48.41537 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1b42a6a8-02c2-352a-b999-607ce9b48d3f | -14.56795 | -48.06189 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5501704a-2ae0-385a-b038-651150c78a57 | -13.29452 | -46.82294 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8262ae0-a406-3a1a-88d2-e8aaefef9b9b | -11.11745 | -44.66101 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11842367-0f7d-3d99-bacd-671f1e83dd4d | -14.56562 | -48.05251 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c4a6dd1-0d5f-3981-8f8d-77121078a9cd | -14.78919 | -47.5077 | 2025-09-03 03:34:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b8160f41-ff33-336c-bfcd-16e3381cf42c | -11.05379 | -46.89422 | 2025-09-03 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9dda189d-99ef-31c6-85ff-2df3d297b38c | -14.80628 | -48.23166 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9a4d8b6-06c1-32bd-a51a-88c82d5402cd | -10.13389 | -46.26003 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 999ee67c-eb6f-3cac-b3a0-7cb65697a418 | -15.571 | -48.4106 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e623864-3786-373f-b12e-af8c6284e0a2 | -13.90207 | -48.10377 | 2025-09-03 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee318ee2-99e5-3ee5-8e05-6ba025a40fa1 | -13.71192 | -46.94182 | 2025-09-03 03:34:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c104673-ac4c-3df7-9cfd-81509f9bd555 | -15.56636 | -48.41885 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 01303e1c-fdfa-3a17-8ca1-bf0ff8ebdd67 | -15.54519 | -48.31536 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aeac7673-9da2-340a-be21-e641fecfb180 | -11.14147 | -46.34306 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95cff7a8-0afa-387d-9fe8-46facb7093f5 | -15.55344 | -48.4221 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f8e22cdd-7a27-3f3d-a58e-09401e25fc02 | -15.08907 | -48.12364 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa3698a7-6e48-34c6-bb87-ccbc863a1e92 | -13.32206 | -46.82624 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7224122-e886-396f-b75c-958e8cd9e18a | -13.58099 | -48.14033 | 2025-09-03 03:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbd76f5f-b519-30a1-abd1-104c2a3b21eb | -15.56811 | -48.41105 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 69357e04-adc0-37aa-bc67-a885612e52ea | -16.30172 | -45.69083 | 2025-09-03 03:34:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a42e2d5c-09b3-33d7-9ab9-6a9e5aea70e8 | -16.3801 | -45.24219 | 2025-09-03 03:34:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e293de99-2ac7-3867-88ba-00ba09b59a30 | -14.78878 | -48.16557 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2b1664bf-dc90-31c3-b253-5e7950176c76 | -14.56958 | -48.05448 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7659c251-ccce-38b1-a6fe-97b7bfa3379d | -12.95455 | -48.0784 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65495ced-49fa-36ca-b499-498e42c5ccd8 | -13.36362 | -46.33675 | 2025-09-03 03:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3de5c3d9-57f5-3424-9807-86973f604680 | -11.11646 | -44.65765 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32de5870-4740-3513-a6c9-6c53aebf6fc7 | -10.12729 | -46.25355 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17bc3fd6-1903-3d03-9e1e-613af794e362 | -10.13437 | -46.254 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e119dbc-0543-3b92-af03-1b9f9cb3d600 | -12.95602 | -48.07181 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ecb306c-b814-3a75-8856-03e2d44cd519 | -13.4952 | -46.91937 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f88657ff-54c0-331c-9e73-31995259769e | -12.84006 | -48.04251 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 486cfdb3-8a32-3142-9ed8-0fd898821e4a | -15.54751 | -48.35164 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c4a0a4d-079c-340a-b0ec-bc6dd0bf4616 | -13.48866 | -46.91689 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e312f219-a839-3708-926c-40e6fa868c37 | -13.30111 | -46.82515 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 394255a9-a34f-3cae-897e-994bc85c34fd | -14.77055 | -48.14722 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| badec226-a17e-34d3-bb3b-d9c576e6e6a9 | -11.27834 | -40.45874 | 2025-09-03 03:34:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ff2a4cac-3eeb-3509-8ecf-4d3da64402fa | -11.12068 | -44.66859 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c09d4625-7480-31cf-b14c-ea7014585220 | -14.56191 | -48.06884 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6ba4c6d-fe3a-3254-a208-bdc9648acc9e | -12.83706 | -48.05687 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b0ad72af-58c2-3c1c-9b0a-e17f65b1f3ea | -13.70522 | -46.94016 | 2025-09-03 03:34:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61d9fc53-d16b-3562-a600-08eaee2451c3 | -12.84362 | -48.02652 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da23fecc-5a6a-3d81-886c-c3457b3dbcb2 | -11.05261 | -45.39903 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d572828a-55a0-305e-8d50-46512f60f837 | -13.90368 | -48.10291 | 2025-09-03 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cd38f4f-384e-303a-942d-78e212d698b5 | -14.78044 | -47.51498 | 2025-09-03 03:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80453f29-510b-382b-b861-a6926bf6f650 | -15.09449 | -48.13246 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee73584a-10f7-36a1-91d9-3db4fa980e32 | -10.7308 | -44.81034 | 2025-09-03 03:34:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcb67add-98df-3fb2-ab1e-af7801e1c92f | -13.90064 | -48.11028 | 2025-09-03 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53355102-8edb-3432-a4e3-13661284dd26 | -11.8934 | -46.66572 | 2025-09-03 03:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d31a543-32a9-3925-8787-7a59a067fa6c | -14.76046 | -48.13825 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dc88ddd-ba60-3323-a603-77a823329b35 | -13.49464 | -47.02194 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6b36ae69-94cd-3c36-ab6f-a7178382aeae | -13.00021 | -48.11322 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2ff978c-68aa-3ffa-a801-ad00dc15f7ec | -11.11665 | -45.11338 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b2f7b9f-e842-324a-8206-59ca652386c8 | -15.54599 | -48.35815 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0feaf79b-fa27-32fb-bf70-76da4d3ac0c6 | -11.44513 | -47.30284 | 2025-09-03 03:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 001c8ae5-b7ad-3c40-8aa6-5a9c76a41faf | -13.50135 | -47.02385 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 752cd2db-6e14-3fda-871f-4e9f1870604d | -11.11326 | -44.64167 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4d958b43-417b-35df-9d82-c6583b423f99 | -13.50161 | -46.92578 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9db11e2-5d8b-3551-85f0-d25c05184f37 | -17.5404 | -46.61614 | 2025-09-03 03:34:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3aa50f4e-5363-36bb-9b1f-5756891784e2 | -15.09302 | -48.12465 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0c21350f-2bed-35dd-b367-cfe0dbb9e50e | -11.122 | -45.11977 | 2025-09-03 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README25.md)
