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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99570168-4e37-30aa-8743-4df7d524cb12 | -7.75438 | -47.61231 | 2025-06-20 04:00:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72c079a9-7ebe-3e8a-ade0-ff96069918a9 | -9.30935 | -44.83207 | 2025-06-20 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4d5a07af-ed78-3139-8b08-9e678e190280 | -8.2596 | -44.96094 | 2025-06-20 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82a3ec4b-c7b2-362e-9330-072e1a96eeec | -7.23971 | -44.68505 | 2025-06-20 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54f8efa6-d494-31c6-893c-8602300ed3c2 | -7.22011 | -43.06904 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 596dddb0-105a-327a-99ce-2d060f795501 | -5.60665 | -44.9167 | 2025-06-20 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeae0601-9c61-3074-81ac-e7536eb0bf0f | -8.72495 | -47.99363 | 2025-06-20 04:00:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 374b4538-879a-3926-9a5f-c94a4df0b057 | -8.26351 | -44.96162 | 2025-06-20 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5f14e6a-c869-3f82-8be7-240342b66673 | -9.95404 | -46.62941 | 2025-06-20 04:00:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fed45f0a-45aa-3d59-8d44-4fca58dce324 | -9.31102 | -44.82962 | 2025-06-20 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ee7f6ec-007c-3187-a0c6-a1e0895f95ce | -9.31683 | -47.79225 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 228f1a3c-4534-3e1e-ada1-ce012acfbd16 | -6.80314 | -44.74746 | 2025-06-20 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28f9801e-4a9a-3817-bf84-9d0171705e7b | -5.10028 | -44.79941 | 2025-06-20 04:00:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40c00059-cb82-383d-93eb-f4413e763fc8 | -9.30304 | -47.78911 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55e80b0b-f5a7-3ce1-b2e4-7dabd5adb2c6 | -9.33313 | -47.83581 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d17c5eac-deb9-313d-b756-557d26dabda7 | -4.37757 | -48.07426 | 2025-06-20 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 237c08a6-183e-3c0d-b593-a402c5b80c41 | -4.54232 | -48.01801 | 2025-06-20 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96c05fd7-03c2-357f-bc4c-f3f8f74ccaa9 | -6.97451 | -42.79397 | 2025-06-20 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 062b2034-a671-3090-96ee-9689bf06dfc8 | -7.21624 | -43.06336 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| d3757547-02c9-3ae0-8d85-af3e55226501 | -4.59295 | -47.8923 | 2025-06-20 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5084bb99-b280-3495-bfeb-a859e49edbae | -8.72587 | -47.98843 | 2025-06-20 04:00:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f424a5a3-2bb7-3b42-b7be-5aa9697ca471 | -9.83978 | -44.70813 | 2025-06-20 04:00:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45cdc186-e21d-37c3-851a-0cc8fae0a618 | -7.27183 | -45.36626 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57043088-e150-364c-bd5c-7d26ecf1e232 | -7.01932 | -44.60795 | 2025-06-20 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35089604-e4de-3e05-b49c-07daa0b31a8e | -9.95044 | -46.62498 | 2025-06-20 04:00:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cffcf77a-cfd6-3013-8b7b-2fed5a5fbd22 | -7.22134 | -43.07675 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 9e70c125-8853-3bd0-9f34-2bded9ec8d56 | -10.4339 | -46.71544 | 2025-06-20 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5e3a1b3-db93-3b46-bc40-067ead019d71 | -5.48569 | -42.14161 | 2025-06-20 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 166f3d4f-a3d1-3e52-98d6-4e7de851c050 | -4.81815 | -44.35344 | 2025-06-20 04:00:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a62fb48-6249-3317-ba1a-977c3f2d5401 | -7.21913 | -43.06802 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| be35ca7b-de81-3631-a55e-b348a58de4b8 | -7.26811 | -45.36544 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b71753ce-3bbe-3eb4-b589-18d2d41bac3a | -7.14888 | -44.06205 | 2025-06-20 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0957a4c8-c48b-3cee-93a4-9194a7452bf2 | -7.87134 | -47.89424 | 2025-06-20 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 387f28e9-9bb9-354e-a48e-7c89e6395356 | -6.17495 | -44.86539 | 2025-06-20 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f23b5bb8-244f-36f1-b473-22b185c2e915 | -10.42092 | -47.08949 | 2025-06-20 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef610952-b380-367f-8f48-63a794f01ead | -9.31404 | -44.83507 | 2025-06-20 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc2a4e94-059d-3499-bfdd-cd843b5a2397 | -4.77658 | -47.24911 | 2025-06-20 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d734739-fd0b-3716-a17d-f2dd251cdb6b | -5.7824 | -43.45493 | 2025-06-20 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42b471a3-03b8-38c7-9db8-26777a8708c8 | -8.88308 | -49.26173 | 2025-06-20 04:00:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b0f5f70-423b-315d-a7a8-c6106a23c837 | -9.84509 | -44.69959 | 2025-06-20 04:00:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 509f5efe-47f3-30b6-9214-ee27a6e0c0e0 | -8.25179 | -44.95957 | 2025-06-20 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 389c50a2-5feb-3d99-a84a-c83ccefd009a | -4.37706 | -48.07733 | 2025-06-20 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6277f63-07c5-3b0b-b72f-e0eb0b2c813d | -6.67178 | -44.25118 | 2025-06-20 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8a336672-c440-3678-89f0-2517ded471a9 | -4.85499 | -43.19372 | 2025-06-20 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4820bbfe-edf9-3ccc-bd06-2d3a39bfc875 | -7.7029 | -49.39245 | 2025-06-20 04:00:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b6b83f3-bc66-3aec-9e32-47e271de0b15 | -10.71754 | -45.16336 | 2025-06-20 04:00:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d557cf9-c0a0-36c8-9433-2346c05a6797 | -7.06174 | -44.14285 | 2025-06-20 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c456b3c-129f-37e8-bf5f-ba70b30c17ca | -9.84587 | -44.69498 | 2025-06-20 04:00:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8467f3a-bdaa-3c1f-875e-0c27be0c9620 | -6.49057 | -42.84736 | 2025-06-20 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 679b0126-892d-3506-81a4-2a9e0c5fa372 | -7.97113 | -46.22091 | 2025-06-20 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b6e908a-25e4-3e6f-84d7-6867e7280b7c | -9.8701 | -49.33537 | 2025-06-20 04:00:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b189f323-bc47-3a83-bcdf-54b2029e6e75 | -8.25893 | -46.3905 | 2025-06-20 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85956ce8-20fe-3db3-957b-5cb828e57d9d | -7.21879 | -43.07721 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e4bfe596-41e8-3aa0-b40f-5ac43a310b97 | -9.31309 | -47.78634 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7038544-3909-3d58-b64d-57ab41e1335f | -9.31231 | -44.72788 | 2025-06-20 04:00:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c1ddb90-678c-3010-a92c-16a746bc4450 | -7.39051 | -45.40483 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03298043-9c78-3a6a-9062-5dfa2c23ab9d | -7.75529 | -47.60724 | 2025-06-20 04:00:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d64592e5-b176-363d-b14e-1e72fdd0ff9b | -5.60723 | -44.91314 | 2025-06-20 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b058ccc-8d7d-3fa6-a01a-c9a4c9328c69 | -9.33002 | -47.84202 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e3771e0-8d85-3a7c-ba50-269054e72432 | -7.21488 | -43.07153 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ba13d82b-3822-319c-8d96-87835c0133f5 | -8.12729 | -43.12523 | 2025-06-20 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e9c75946-53f9-375a-9e22-976d6d7b421d | -5.78683 | -43.45114 | 2025-06-20 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6babae3e-e227-3398-91f4-98db5a6eba1e | -4.94927 | -47.47114 | 2025-06-20 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d65726a8-3c35-3d06-b936-ae436307c7ff | -7.60743 | -45.55391 | 2025-06-20 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0550429d-134f-3575-baee-0b761068e3fc | -7.75783 | -47.61034 | 2025-06-20 04:00:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0833ec8-f8c6-39f6-9895-5481297efcd5 | -4.94614 | -47.47406 | 2025-06-20 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 28b4b3c6-71fc-3dd3-ad6d-351269289027 | -7.15264 | -44.06271 | 2025-06-20 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95951251-dfec-38b1-8e8f-d2a235b07a63 | -10.4332 | -46.7194 | 2025-06-20 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15c98072-90d5-37f3-936e-09c9270ddd6e | -10.24288 | -47.45978 | 2025-06-20 04:00:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 988e47ab-f273-3276-989b-15898615dc6a | -5.49266 | -42.14275 | 2025-06-20 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9170d6cd-e611-35d4-a1e2-73735f8605c8 | -5.48856 | -42.14604 | 2025-06-20 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 23ae96fb-42d4-3878-94c5-85e195dc2820 | -6.49138 | -42.84874 | 2025-06-20 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4db0b478-478b-37eb-83ac-0d420c48219c | -7.21653 | -43.06847 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 9f9de2b2-365c-3fe9-9521-5b8a432218bc | -6.48782 | -42.84815 | 2025-06-20 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d1680c92-4eec-3584-8115-76c15fdf33d7 | -6.22279 | -37.43795 | 2025-06-20 04:00:00 | NOAA-20 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc80a4bf-6f18-3fa7-9cf1-ae02c041ecce | -8.16718 | -43.14836 | 2025-06-20 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2e11f893-a429-3479-a02a-a27cd063d16b | -5.49204 | -42.14662 | 2025-06-20 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd7dd1a1-c853-3ef1-bcff-178418a79baa | -7.26871 | -45.3618 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ffa2ff5-0745-3292-b59b-eed6b06eb760 | -6.66875 | -44.24563 | 2025-06-20 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b53b2786-4ad0-3c1b-bbfd-03a469d23d06 | -7.60681 | -45.55758 | 2025-06-20 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec06eace-c21b-326b-ada6-dd23c2243db2 | -6.32563 | -43.75875 | 2025-06-20 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02032071-cde0-33d5-9739-7b03bafb0a27 | -7.0148 | -44.58704 | 2025-06-20 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 46d3141e-969e-32ca-8b35-3924de026feb | -8.26825 | -44.95737 | 2025-06-20 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c911cb5d-98f0-331f-9cf8-c14b45b2ea5f | -8.07634 | -43.10505 | 2025-06-20 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e65d6309-45c1-39aa-abfa-151483941363 | -7.28295 | -44.37715 | 2025-06-20 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1d7535d-1255-3687-92ca-e140a3881234 | -10.97751 | -42.17699 | 2025-06-20 04:00:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4271bd02-d620-357e-8d90-c05b2b615133 | -7.2123 | -43.07198 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 73f72d44-7d50-3a15-81a9-f507e7b1ca8c | -7.26901 | -45.35826 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57095eda-71f7-3f01-a671-9f24f1049575 | -7.13718 | -43.28455 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e3e8df5-576c-30a0-bc03-f7e9400011b6 | -9.31223 | -47.79123 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| abecf4a3-9993-32c6-a28a-e796fc6842c8 | -11.05639 | -42.23452 | 2025-06-20 04:00:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63e70328-eb3d-3a20-9850-7b332751f776 | -9.37315 | -47.63326 | 2025-06-20 04:00:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5f4f9f9-841b-3ec9-93ca-1ecebf24dfbd | -7.22322 | -44.68768 | 2025-06-20 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cdc23ac-bf0a-36e3-a5da-a31737e60c94 | -9.94978 | -46.62879 | 2025-06-20 04:00:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3854354b-fe09-30da-a12b-dd71de9fa611 | -9.84432 | -44.70419 | 2025-06-20 04:00:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ce6ed6b-9b65-3b85-bfc6-ac8455bdcf85 | -7.39114 | -45.40116 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5821be0-7d48-326e-acdc-e060b532ce04 | -9.31309 | -44.72318 | 2025-06-20 04:00:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83186cf5-35cb-3cef-baea-cb745ba8396c | -6.84787 | -44.28564 | 2025-06-20 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28eff3b7-1bc9-3486-8aa8-63075f99aa4e | -9.98506 | -48.54488 | 2025-06-20 04:00:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd728590-cdc2-3aad-8b68-1d831a6771bd | -7.01625 | -44.6023 | 2025-06-20 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
