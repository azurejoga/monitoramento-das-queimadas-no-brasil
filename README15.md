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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 478b4257-4df0-30da-8fc3-d7ab318716c7 | -4.67369 | -46.33147 | 2024-11-07 00:56:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 869b641a-024c-3b66-9972-ecef2b23f50a | -4.99113 | -49.89489 | 2024-11-07 00:56:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6bae029f-531e-3513-af08-4d6643fcb053 | -3.21432 | -50.3031 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 675c10f5-1cd5-373b-8bd6-c38b54208eff | -2.61199 | -51.73067 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d748c5f-682d-3c46-b346-0e70c8522d09 | -2.05539 | -46.34047 | 2024-11-07 00:56:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d55208ad-9173-34b0-92a4-ff6d47855c3c | -2.82092 | -52.9285 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 996cf381-8bfa-3c36-9412-15983f1f4acf | -4.73321 | -43.24944 | 2024-11-07 00:56:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ae2c2138-3423-3e7f-8b75-cb5f7f93a7b1 | -4.603 | -48.68937 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 27810062-9d3a-33d0-94a1-15338c7e5665 | -3.53261 | -50.33482 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 656fb19c-cff8-35e5-98b1-d79931ab2cd6 | -2.08423 | -52.04538 | 2024-11-07 00:56:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| b94d7c5f-3adb-35f9-9344-0ee0db8cea1d | -2.052 | -52.0914 | 2024-11-07 00:56:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 47121e84-85ae-3acc-a9a3-41fecabaaf62 | -3.20409 | -49.22907 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b857516-e6b6-3a2b-940c-f5a7c58640c9 | -3.97211 | -48.40271 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b64e32dd-aca7-33e0-8bb9-e8e1d5f15329 | -4.80515 | -50.8215 | 2024-11-07 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7ff74982-3568-3c0f-9233-764ccd5d73c8 | -4.4837 | -48.10804 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 10771234-2641-3551-860d-01c169048a86 | -3.96845 | -49.03596 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 59aae9bd-a658-3f9f-823e-b57084c954f8 | -2.72333 | -54.14962 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 7166393e-52b7-367d-9656-aff53a9c5ec0 | -8.68414 | -47.96404 | 2024-11-07 00:56:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f38734b-7516-3660-aa67-5dc7131a38fa | -1.92198 | -46.47884 | 2024-11-07 00:56:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 269406e4-92ab-3ef9-9ce0-3c83c5acca6d | -3.02448 | -54.08958 | 2024-11-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 807be7eb-0aad-3b52-8bb5-7110c6a4037c | -5.38001 | -46.25614 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8006a979-6fcc-3852-b6bc-e2e4833934ff | -2.20644 | -48.36066 | 2024-11-07 00:56:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a673ce96-88dd-3364-8e1b-d0ee35c61784 | -6.47878 | -39.75465 | 2024-11-07 00:56:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 3db0847c-9a2a-3b59-943f-e6c429ebd63d | -2.20626 | -51.94407 | 2024-11-07 00:56:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ee43fc7b-b2e6-34c2-b22b-7e58a310829e | -2.20721 | -48.83092 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c418176-3338-3430-924b-ec170fafdddc | -3.01517 | -53.44229 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f8a0b2ee-7ec0-3ef2-8e8e-e7f9759c7ea4 | -5.54319 | -47.05827 | 2024-11-07 00:56:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 448372b3-a052-35b2-b6b5-c1a6226d4835 | -3.31735 | -51.5737 | 2024-11-07 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e80d3fca-9385-321f-a683-afe832c68d21 | -3.19218 | -53.39271 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f0fbf4db-dc7b-352b-bb79-68c2a2400cb4 | -3.22307 | -53.1035 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 5c99081a-0155-37f3-9a56-03474e57a4bb | -5.79062 | -49.27634 | 2024-11-07 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de76a8be-4826-3969-bbbc-35d367ff0a1a | -2.22315 | -48.48029 | 2024-11-07 00:56:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1156b6fc-e0e9-3252-af50-ea676b9f7160 | -3.98105 | -48.40144 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 78b09d50-71cf-3542-b555-9fae44f7356f | -3.96822 | -48.17484 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| f2b1523b-3a68-36fc-bed8-af89e0a59138 | -4.32071 | -48.6484 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c1c2a46b-ebdc-3017-87f1-4d1696bec480 | -2.50519 | -49.11564 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ad6222b2-fa2e-3c8b-af2d-1ca9cf4ab61e | -4.57965 | -48.06939 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 970258b0-6289-3bd3-b05b-016331a17df0 | -3.09228 | -53.91749 | 2024-11-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6ba950b5-b00f-38dd-a833-a6ce8401bdc9 | -3.58312 | -49.30369 | 2024-11-07 00:56:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85942f2f-5b44-3ecf-a143-30e72e143105 | -2.85551 | -51.76969 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 93d8bc55-29e8-3655-b2f9-7da771350ad7 | -4.27562 | -48.66065 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6fe92b3f-ad80-3240-8353-707f0c6b2a67 | -2.9682 | -48.73185 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c61e30e0-9374-310c-89b6-1532d4123e42 | -5.14518 | -47.70082 | 2024-11-07 00:56:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 195.0 |
| ece84650-4e2b-34f4-9cab-cc1895e3e620 | -5.36119 | -49.24166 | 2024-11-07 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7cf025b1-69ab-3044-bd7d-75f2f436bcd0 | -3.19713 | -53.14434 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d3a7d651-9bdc-39a4-b47f-e3073bcd5261 | -1.94842 | -47.03605 | 2024-11-07 00:56:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e1db6f6f-4516-3acf-a34f-e282b294794e | -3.96563 | -48.15657 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 78c6643c-2aed-3e45-9f7c-3139f78e50ef | -3.67339 | -50.22659 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e2ced1c2-9d02-34d9-86da-19896c3b46a6 | -5.11221 | -43.96484 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 97b7c4a6-63e4-30e7-beee-2ae733ea5733 | -4.7198 | -47.23347 | 2024-11-07 00:56:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1ec93cc0-a3f4-3414-9458-830077bce019 | -5.97773 | -45.37585 | 2024-11-07 00:56:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 547a19b9-4367-3dc0-92ad-2b8d512053ba | -2.81561 | -52.96508 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| a6c673b9-c3a2-3ca3-b5c5-134e5fc8f328 | -5.05398 | -46.85608 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 92cd294b-bf55-34aa-96e0-69da81d5dde2 | -5.15424 | -47.69946 | 2024-11-07 00:56:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff984b4b-f162-30c6-85c6-6b8565de4109 | -3.45568 | -50.37947 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 01d9e47e-31b1-3e72-a07f-ccb6a78f9947 | -7.04253 | -47.62616 | 2024-11-07 00:56:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bc5ffff6-e0c7-3215-933f-c3018ccb0d89 | -6.68906 | -46.18365 | 2024-11-07 00:56:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5cbd726a-ff64-30ea-abaa-98f73cd78a5f | -2.94467 | -52.71136 | 2024-11-07 00:56:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3b3cc313-6278-33fb-a71f-5e65be245f72 | -3.53384 | -50.34381 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e7927adf-a29b-39dc-a9f0-048e3406944b | -5.04457 | -46.85756 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a2d7abfd-0fe2-32e1-b715-1789ccd5996b | -3.58266 | -50.23615 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e579101e-ccf7-319b-b1e8-b1fbdf9beeaa | -2.75709 | -53.21087 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6055b7aa-35f1-3e53-9d27-09d0c45581d4 | -2.03493 | -46.99553 | 2024-11-07 00:56:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 15621862-6312-3113-8cfd-3b16861efad6 | -6.04696 | -46.60645 | 2024-11-07 00:56:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 82cd8162-646b-3f5c-86ec-63f9975eb27e | -6.54133 | -44.46413 | 2024-11-07 00:56:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cf17a166-8566-3de6-b017-fa6d6f21cecc | -4.68149 | -46.38583 | 2024-11-07 00:56:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e363ac11-88aa-383e-9db2-85310011d563 | -4.09534 | -51.01732 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| e35497d1-62c6-3525-bf28-5d0169a2d628 | -6.0425 | -46.61301 | 2024-11-07 00:56:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 94417159-e499-3989-a792-63a073581529 | -3.57144 | -50.55119 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4433b1c7-405b-35d6-88d1-bec2a83e3e3d | -4.42707 | -44.47331 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8f6152f1-621d-3513-939f-4d8248df7177 | -3.30445 | -50.09347 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 99f7ac6f-c084-3668-91e0-3fd3f6eed025 | -5.03373 | -46.8489 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| d63d98a2-4726-3438-abe1-5f6a8833829c | -3.22553 | -50.3839 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 631b40cd-210a-3f42-ab24-5e5b1c2ea226 | -2.93793 | -54.11603 | 2024-11-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 56bf3e92-c479-36d3-a663-6ca949a4b0db | -3.626 | -49.61173 | 2024-11-07 00:56:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b29a1cb1-58c7-37f2-a764-74b3c7ffdf44 | -4.2632 | -50.69381 | 2024-11-07 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bb41014e-bb1d-37b0-9b72-2d9d30ee12ba | -7.90542 | -46.70482 | 2024-11-07 00:56:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7b0bbbd8-0cf6-399c-a257-fcfc63abb9eb | -2.60542 | -51.75185 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e2779f53-5f4c-37d4-a8f5-39319c3b259d | -8.1212 | -44.4174 | 2024-11-07 00:56:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 35c09542-a9f9-3b89-b3b4-334ad159e6aa | -3.61495 | -50.19828 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 8d51cf4d-3fa5-3bc9-91dd-f871cbee8f29 | -3.52556 | -52.17265 | 2024-11-07 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 97173d13-f230-3cc1-84fd-23dc3f2f2d43 | -3.95579 | -48.15493 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 29679e4d-f58b-3bde-97f4-a12c90fdb948 | -4.42877 | -47.26379 | 2024-11-07 00:56:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 005031a4-2732-3c16-ae10-bcda3daa15b8 | 3.35708 | -51.29422 | 2024-11-07 00:58:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ea5ddc3d-67a5-3fd5-b9a9-84a0aade9de6 | -1.42845 | -52.24181 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ad029f58-0c17-32eb-ac12-64beea09ef37 | -1.39442 | -52.20499 | 2024-11-07 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| b201256a-21cc-38b6-82b8-b0b77748b10f | -1.15233 | -53.73059 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| e2c7055c-6a87-32a6-b45f-952426288174 | -1.76521 | -54.18586 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a2a5fef8-a55d-37f7-84aa-9f88b3c29cb8 | -1.2186 | -46.35822 | 2024-11-07 00:58:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bdad9e78-110d-37e3-809f-3efd6dd4cdc7 | -1.15063 | -53.71811 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| bb41725b-41de-34b9-99b7-aa899b1ee0e0 | -0.99628 | -47.61082 | 2024-11-07 00:58:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 82671b79-46ee-3345-a37f-21f237ab162b | -1.02039 | -47.05312 | 2024-11-07 00:58:00 | TERRA_M-M | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0b79247e-84a6-308c-acaa-50a9629b67e4 | 0.04586 | -49.52021 | 2024-11-07 00:58:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 789439a7-3b71-31d6-8b7f-1575345d2943 | -1.13415 | -53.72568 | 2024-11-07 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3f378306-6a26-375e-ae00-6b201586cfe7 | -1.11354 | -46.83569 | 2024-11-07 00:58:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e31d81fc-a41f-3022-8164-91980b81ad05 | 1.35957 | -50.93426 | 2024-11-07 00:58:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e24c2e66-6b3a-3a7c-a4e0-fd3a05fc73e4 | -1.32925 | -54.61243 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6d4666fe-3d0e-334b-b6d4-3f7ec8917175 | -1.52696 | -52.14946 | 2024-11-07 00:58:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 360c7e13-0cc4-3c33-a82e-fca603bfe22e | -1.52978 | -52.16975 | 2024-11-07 00:58:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e691819b-3125-3856-b1bb-7574d5343a16 | -1.19577 | -53.89151 | 2024-11-07 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |


[Clique aqui para ver as próximas entradas](README16.md)
