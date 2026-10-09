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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 938aee55-aa4c-3752-8988-cb8a6ece979a | -3.00835 | -54.09172 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7aa11fb6-ee17-3d33-9c73-b910b3e3e81f | -6.41195 | -55.19218 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 458ea67b-9508-3af0-96d5-691655e14321 | -7.18698 | -52.62838 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf60c0a8-adee-370f-bcdf-614759e0870e | -7.61808 | -46.53527 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4b19a579-09b7-320b-b42b-af4de56c2247 | -8.3019 | -45.72945 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f81fa1e-afdb-3cd9-bf16-f196c36de7d8 | -3.06222 | -54.38452 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f680c35-4f3c-33f2-8360-c9d3e12ace34 | -3.20349 | -53.86473 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5cd59b1-d61b-3003-a6a7-6ad93e5876d9 | -6.68213 | -41.75869 | 2026-10-09 05:04:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c92f355c-da37-3488-885c-69d9a1eabca0 | -3.26431 | -54.0249 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d4b6d23-1dc4-3b61-84ef-7cb4a2484166 | -3.10452 | -53.93861 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f6285e52-0953-3d41-b7dc-e78d5c8b2c54 | -2.49245 | -58.07706 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46211187-7761-305b-847d-233ecba00bd9 | -3.69915 | -53.67131 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0570747-6bad-303b-899d-74fcd77eabab | -2.95552 | -54.12779 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b8ab43d-a8a7-3f28-912a-1b3b2dde1d5d | -9.44984 | -45.8606 | 2026-10-09 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8618d550-359f-3afb-a42f-5f78fd7f3413 | -7.40646 | -44.76661 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d9f45d7-5c62-31bb-81f8-7dc581c4d575 | -3.96256 | -60.0029 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ba185bec-f955-3be9-9d2e-0bf59b51166c | -5.97151 | -55.34715 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9af9c75-e0ef-38ef-9419-4730eb7271ca | -3.4876 | -59.38597 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b25ab551-ae83-3776-aba7-761fcc5187f9 | -3.09105 | -53.95597 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8839f1e6-9afa-32ec-9c85-cf83c71553a4 | -4.12217 | -54.03299 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4175ce9c-23b3-3c10-88a2-cb541fcd427b | -9.05337 | -47.31798 | 2026-10-09 05:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 393ba8d0-fd26-3747-87e7-07f1088f5ba4 | -6.94251 | -43.66887 | 2026-10-09 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9691c47-e6de-35e1-bcc1-371d81ca4a93 | -3.94206 | -59.79381 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3ab99541-d384-38b2-93c5-89f6a9b8df5e | -2.92751 | -54.12325 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 695dae4e-7b6e-3d1d-bb22-612abd62daa1 | -2.54663 | -57.38569 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 86374e39-989a-37a3-b904-7d563b0e079d | -7.09205 | -47.73429 | 2026-10-09 05:04:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7b37e36-7ec8-32c6-9107-a2a716bbda42 | -3.83531 | -55.9744 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c11a7c3-d779-3196-b9bd-bcc5291cef3d | -3.77535 | -58.58612 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 187fce76-fe99-3919-9c08-3afe00a99cae | -3.28621 | -54.04402 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f1660b5-de65-358e-b543-a8fab1e25e68 | -3.08697 | -53.95921 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0e676d8-2b10-3590-b3b5-c5e6ea1e0a2b | -2.62906 | -57.73736 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a37def44-8176-3646-b2c2-e025507e8cad | -3.30213 | -54.01147 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ec59f56-8ed6-3fde-8aab-e6507a922c0a | -2.52579 | -58.06911 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34ef5856-7b33-31f0-9d18-de2b6be38b82 | -6.10799 | -55.71754 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1621ce4a-3a0d-3798-a9de-3dbc65db1029 | -3.5453 | -54.49775 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03bf7a28-f7aa-32e6-a10b-15cae8731f97 | -3.96941 | -51.86644 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5f55499-9376-3eaa-a72f-b1b49ae9837a | -12.01272 | -43.44824 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bc51e9de-7402-31b4-95a4-f55efdd95c99 | -8.27625 | -45.74187 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c3ffe097-4047-3ddd-aa45-6c1921881288 | -4.81924 | -54.74066 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aa7ede4-a075-3ad6-817d-66c369d12c23 | -4.34455 | -54.79717 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e6fa1ea-f064-32c5-b4de-03fc665a7cdb | -7.61871 | -46.531 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0de161a-261c-356c-8967-465afcedafc0 | -3.30116 | -54.06207 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 858633f4-024b-319d-82d0-6107b9bc2d3e | -11.19462 | -45.31178 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c89061d-b023-31d7-a2f4-59d80e67ee02 | -5.61542 | -44.84387 | 2026-10-09 05:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9aea3a47-a975-3480-8067-b6f75752d345 | -8.1747 | -54.71921 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4401b7e-be72-355c-b602-05cf1c544743 | -3.01313 | -54.23942 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb29d4f0-3371-3298-a862-0903e711c3a2 | -5.93362 | -51.83072 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c49aa8b5-07a7-345b-8984-564f2943c5d9 | -7.5078 | -45.75832 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16c4f65f-1330-3688-ba0f-ed2d4e62f9e6 | -5.59466 | -47.28254 | 2026-10-09 05:04:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82a18554-a6dc-38fd-82cc-4cb2625876a1 | -5.0866 | -46.21852 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36acafd5-16fe-3e13-9193-3c781ac6d031 | -9.86763 | -44.8709 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0910ff0a-0919-3889-aa13-b86de544a077 | -9.27721 | -47.43746 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbfae037-4e10-3617-a350-aacece53a40f | -4.82728 | -45.83062 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab421fe2-0b0d-3591-bed1-5b9abcafdb20 | -3.09861 | -53.95327 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b47eb1d6-da17-3fc9-9c8d-51d54bdd19c1 | -3.43703 | -59.53923 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f87084b-28b5-31e2-9082-3617e5256538 | -11.86905 | -43.56021 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ef1d34a-b1f0-33f5-a850-131a613c7432 | -3.01023 | -54.08018 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb1ad4d1-242d-3c4a-b3ac-6acf6c8da388 | -9.04923 | -47.73497 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41d9dcd0-295d-3084-bf8e-218c0e1ae9df | -3.47718 | -59.50793 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 721ff368-f528-3c06-8dcf-e9a3a5cf460f | -11.26495 | -47.74059 | 2026-10-09 05:04:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21d2dda4-d6ae-3e5a-9bfd-d434a635c756 | -5.9751 | -55.34773 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12da7e47-a231-307d-af89-1a849759adeb | -9.92751 | -44.79406 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 525d14ae-3359-361a-a790-02638fa654c0 | -6.99671 | -59.10857 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 601f52c5-5fdf-33ee-b931-596761ad5960 | -3.01754 | -54.21218 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e867a1f2-a0b3-36c6-b131-21f25ffa9d84 | -3.32389 | -61.26833 | 2026-10-09 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 175ead1d-3aad-3753-be18-9ca073d65b4c | -6.37806 | -56.22559 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac2c3269-8ab3-3b48-b74d-8ef3799b6f1e | -10.30404 | -46.59655 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0c2d916-78c6-38e7-bc6e-ba7e99e8b107 | -3.49208 | -50.49253 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48877856-c73e-3cda-88d9-82eacbd12bbc | -2.90302 | -56.9494 | 2026-10-09 05:04:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 137e1c51-63c7-3bbc-9462-d59ce0fff4ea | -3.66903 | -56.81315 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bd81d04-b574-3271-8678-ecdc6d51fc22 | -3.57722 | -54.65238 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bef4595-2bf8-309b-94d8-66aa419323c0 | -11.76824 | -43.52873 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f57b6c4-0d1b-3616-8fdf-5967682c314a | -6.485 | -55.30276 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5f6dd1a-09f1-338c-9d86-0a0862c7a4d4 | -6.10044 | -55.69599 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5268ccb-b137-3e9a-8a67-145792633c5b | -3.10746 | -53.76532 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ead9ef6f-592a-3f55-8c1b-a0500d40245f | -3.00584 | -54.10712 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f9d5feb-02cd-398c-9b41-8ea4850eccbf | -5.27374 | -47.91499 | 2026-10-09 05:04:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c71a101-918e-3e67-a575-578b0cc26b91 | -3.72168 | -54.22865 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e54e783-14e8-3a11-81ff-c1f84d455a7c | -11.82434 | -43.59259 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 81d8efbd-0a29-3c5b-bdcc-cc16f0a501a3 | -5.95361 | -55.34408 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7820667d-e885-3d6c-b293-cb9b26c9a27d | -3.54603 | -55.52508 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 268e7546-6dec-370e-b430-fde47e92057a | -3.08098 | -54.28936 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12079872-4a5f-3e07-beff-eccea94cd27a | -3.00961 | -54.23885 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf2ea7fa-c0d7-32a5-8a79-01a41b936fd6 | -3.07746 | -54.26572 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11bc6644-e1a4-384d-ba6d-d37e30301ade | -2.98638 | -54.06942 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fe05885-3137-307a-a850-c59ec787efbe | -7.51239 | -47.33557 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e75706dd-c1a2-3908-8ae6-bb500f5a21b0 | -3.52405 | -59.34442 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcfd2221-2102-3d16-b195-98f6b642ad0d | -3.06462 | -54.25572 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4450fbea-ef39-3891-beb4-da8a60e2d6f0 | -4.15484 | -55.13644 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8eae965-07dc-3b96-a35e-7edc169fc7dc | -3.79843 | -50.05003 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc3a327d-acee-3097-a810-f93a3c76ae29 | -6.0999 | -55.69872 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc6f894e-071c-31df-a9a0-c32b773212de | -3.00901 | -54.08485 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8df920d0-c2a7-3c5f-88e8-6224917f9bef | -6.96349 | -45.24725 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee8ae80d-41a9-3780-a289-25cc8aeee63f | -3.10504 | -53.78035 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41facb85-c824-3e5b-bc40-240872540eb8 | -2.97039 | -57.90349 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2a38c94-60f5-3886-970e-fa86972fead6 | -5.8858 | -53.62138 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9b11970-9c9f-3edb-b1ed-bb6b309a9f7e | -3.30275 | -54.00764 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c92906b-67fa-3bac-868d-4cfea7fc4716 | -6.99821 | -59.09981 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fed6cfce-6ead-3949-9715-9ce2e13b8cfc | -3.16342 | -58.63203 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff87be61-3d1b-3375-9b25-99259d006127 | -3.04 | -53.89731 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README138.md)
