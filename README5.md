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
| 0e5deccf-803b-348c-a741-99d3ece4dd11 | -4.66264 | -46.33817 | 2024-10-18 00:41:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| a069ca0a-a2b4-3065-bd8d-4fb102b11f3e | -4.66141 | -46.32918 | 2024-10-18 00:41:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 21083488-674e-3176-9ac2-955fd19095e7 | -4.65369 | -46.33944 | 2024-10-18 00:41:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 260fc270-6f36-34cb-8c10-dfbc5be19c1f | -4.65201 | -44.54533 | 2024-10-18 00:41:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fffd0ae3-c2d7-31fa-93d0-ec77fbbb9c70 | -4.65076 | -44.53639 | 2024-10-18 00:41:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 945ce3b4-c9a0-31f1-8a2f-5cd01aa0a4f1 | -4.64187 | -44.53766 | 2024-10-18 00:41:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3434f760-fbc5-3bed-bbd7-1d5f3c6508de | -4.62593 | -45.61552 | 2024-10-18 00:41:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2bfadfab-c10b-36d2-a1c8-ac61a1239ecc | -4.60972 | -45.88851 | 2024-10-18 00:41:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 336ecac4-25a3-3a91-86cd-7f3cbbff20c1 | -4.60849 | -45.87962 | 2024-10-18 00:41:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a512a4e3-152a-3d13-aa87-7ebd40da16cb | -4.60825 | -45.618 | 2024-10-18 00:41:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 41285c85-5504-344c-8da1-95ace813d84b | -4.53509 | -44.96368 | 2024-10-18 00:41:00 | TERRA_M-M | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| df803c3d-4ff4-36b2-b469-83523d2d6cd9 | -4.5196 | -44.32237 | 2024-10-18 00:41:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8c4ab28f-4167-3f98-80a9-847339a905a8 | -4.51833 | -44.31332 | 2024-10-18 00:41:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 5bcdc8c4-ee92-3142-9dbd-9a297b594d37 | -4.49973 | -44.9687 | 2024-10-18 00:41:00 | TERRA_M-M | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3fda20ae-88b6-3d0a-b9bb-97240c524236 | -4.39423 | -44.21687 | 2024-10-18 00:41:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3e413a13-50b3-3b6c-b535-6a14d42b0578 | -4.13122 | -43.34432 | 2024-10-18 00:43:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0d700ad-93b5-3854-8909-ebff0bf303f0 | -3.79449 | -43.23445 | 2024-10-18 00:43:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c53e0a3e-8567-314d-a12c-108dd8746218 | -3.77895 | -43.90735 | 2024-10-18 00:43:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d1f9d461-4892-3bcd-ba0b-f7d06c723f53 | -3.53531 | -43.62313 | 2024-10-18 00:43:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 40f4026b-a4d7-3b5b-b5eb-100be9470290 | -3.53393 | -43.61346 | 2024-10-18 00:43:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 562233a5-de6e-3d69-bc32-90cb8fff9b4a | -3.51752 | -43.23113 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f54b8a3d-e36b-3045-90c8-acb97b6e1bbf | -2.96976 | -40.22794 | 2024-10-18 00:43:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 463a5d38-1d99-3845-9486-621954d06af5 | 1.12224 | -52.33587 | 2024-10-18 00:43:00 | TERRA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 36e29b4a-982a-33e5-a2d1-2e7b6c781c1b | 1.00932 | -52.22318 | 2024-10-18 00:43:00 | TERRA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 93826ddc-1eba-3afe-b82a-35c0f8291413 | 0.25414 | -51.00324 | 2024-10-18 00:43:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 286c0d8e-1d5c-305b-ac5a-a491c775d9c2 | -4.96243 | -49.94149 | 2024-10-18 00:43:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2c6a6f72-a678-3b35-ac59-55181a775d1f | -4.96052 | -49.92693 | 2024-10-18 00:43:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2bbe1461-79b2-38c5-bba1-4c6e36d3318d | -4.72441 | -48.29897 | 2024-10-18 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d0ad2789-7d0a-32d6-8a1c-af6292644bd6 | -4.66866 | -46.91893 | 2024-10-18 00:43:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| cea37190-0f30-360d-9b4d-1bdce1d1d225 | -4.66735 | -46.90938 | 2024-10-18 00:43:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 451ba232-6124-320e-bc91-18fee7d4efa7 | -4.65953 | -46.9202 | 2024-10-18 00:43:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a6f085e5-dac6-3ca6-a03a-cca14e4776ca | -4.65822 | -46.91064 | 2024-10-18 00:43:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 77568f08-517b-3242-9964-fb16a46b76dd | -4.59413 | -49.51808 | 2024-10-18 00:43:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ea95b2de-27a1-37a3-b5d6-252b0c9a3849 | -4.57384 | -48.0316 | 2024-10-18 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 8fa7820b-23a1-339a-803b-d860cc8c34c5 | -4.57235 | -48.02081 | 2024-10-18 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 81307435-f63c-3bc9-b11e-7e0f3aad347f | -4.5627 | -48.02221 | 2024-10-18 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ee4a31d0-2f85-3766-aa14-ea014c7609ab | -4.46235 | -45.89435 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22e13106-45f7-3b91-974c-2bc518014f7d | -4.42911 | -45.98058 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d93c10b8-94ae-32bd-879e-d6c9de90a501 | -4.42789 | -45.97175 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 41f4b4fa-59c6-3d5e-84f3-6e789ac8d9d6 | -4.42666 | -45.96286 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| c5bc5c58-0aab-3701-af00-647a37a1f165 | -4.42024 | -45.98184 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 139.1 |
| c9e57e28-905c-3956-a349-dea26b199955 | -4.41901 | -45.97297 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 230.0 |
| 1f02fea9-6ed2-3864-aa29-f68edd3b6c0c | -4.41778 | -45.96407 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 0076e6d5-f8ac-3fcc-b015-c6256251adc8 | -4.40605 | -48.07808 | 2024-10-18 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 402d6934-26bf-3f2c-b2fe-1ad9075d74e1 | -4.39158 | -50.8118 | 2024-10-18 00:43:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 8d54c9b8-f843-3019-83b8-e01ad07a1482 | -4.3899 | -46.10102 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5fe8779a-4a03-3ac1-8dfa-58e92a68ebf0 | -4.38866 | -46.09204 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 1edf8111-8d17-3154-9c84-b038b479492a | -4.37841 | -45.42035 | 2024-10-18 00:43:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 83278ee1-3a6b-3be2-9303-ef8d8621c5c4 | -4.35928 | -45.81544 | 2024-10-18 00:43:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| da7df310-5a16-3c6f-ac3b-ba86e2da395b | -4.33803 | -47.26291 | 2024-10-18 00:43:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| febe7a14-0e4c-3596-8881-a3b09b081874 | -4.33671 | -47.2532 | 2024-10-18 00:43:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 979b5cad-efe9-384b-bfd3-94af8e8373f2 | -4.30506 | -45.49047 | 2024-10-18 00:43:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ced02d0d-424f-301c-bad5-cef3ec1cf795 | -4.29623 | -45.49172 | 2024-10-18 00:43:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d994614d-5434-3dd1-b927-15dff420db17 | -4.29084 | -45.25925 | 2024-10-18 00:43:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b6327b50-9614-3cee-8ae0-b2f33f691e16 | -4.26915 | -46.28887 | 2024-10-18 00:43:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79cc625c-b982-3b87-b354-9cd1e85740a0 | -0.71936 | -47.8747 | 2024-10-18 00:43:00 | TERRA_M-M | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c01eef47-3655-3268-9ef1-54950933acac | -4.26626 | -48.01641 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d07e036a-d634-3066-8636-e77655c03cdf | -1.02257 | -48.07047 | 2024-10-18 00:43:00 | TERRA_M-M | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| da951d71-7878-3f9b-9093-1af0b8dbd99d | -1.14682 | -48.09682 | 2024-10-18 00:43:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 484c7309-db92-33ca-ba14-560ee05f0bde | -1.14819 | -48.1067 | 2024-10-18 00:43:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4800b1c0-277b-3cc0-9cba-821ede23e827 | -1.53169 | -47.28541 | 2024-10-18 00:43:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2808f4b9-183e-3bc2-a7ed-248967f38534 | -1.53298 | -47.29464 | 2024-10-18 00:43:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9eefda60-6c5e-3d2c-87b5-0cc1a2c9ff80 | -1.56786 | -48.01775 | 2024-10-18 00:43:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eabec4d0-6471-3bfc-92ec-54e8e5bafd32 | -1.61463 | -47.08418 | 2024-10-18 00:43:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 1df1bb8e-87a3-3a5b-bfce-9369454df014 | -1.61588 | -47.09331 | 2024-10-18 00:43:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 1d6ad722-bd95-3a05-80d4-6664fd806b33 | -1.6236 | -47.08291 | 2024-10-18 00:43:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8dd90e04-3cd9-349c-8113-47cc01649e42 | -1.62486 | -47.09203 | 2024-10-18 00:43:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| aea1d125-ca97-3686-8d89-b1ed59cd56d0 | -1.67094 | -47.16003 | 2024-10-18 00:43:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 67af1066-70f9-3548-894f-b2e32db78ba8 | -1.73605 | -46.17358 | 2024-10-18 00:43:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 107a01dd-b2d8-38ae-8f80-bdc46ff8a848 | -4.26484 | -48.006 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 48cbd0c6-47f8-3c61-87fd-c7f217c360f6 | -4.26371 | -50.29616 | 2024-10-18 00:43:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 644506c7-c63b-3dba-88df-d7378fd12854 | -4.25546 | -50.97966 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8563a2f6-285c-3a92-99c3-4835fe417219 | -4.25084 | -50.99131 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 5af585f4-c5d9-31d7-a588-efef32651969 | -4.24864 | -50.97429 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cc0f689e-afc4-31c6-b2f8-9c1217f0172f | -4.24734 | -45.73849 | 2024-10-18 00:43:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 93163bdd-1c9a-3387-8814-e7192f491989 | -4.24611 | -45.72966 | 2024-10-18 00:43:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7b1cd995-417f-39cb-94b7-2de1d61a618e | -4.2412 | -45.69437 | 2024-10-18 00:43:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3bee8cb5-56ba-39d0-b2cd-c238886b74b8 | -4.23997 | -45.68554 | 2024-10-18 00:43:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ec66c3a1-9579-35ba-a62e-fde0951b3094 | -4.2385 | -45.73975 | 2024-10-18 00:43:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f3435361-851b-3be1-94c8-2dbfe222907c | -4.23727 | -45.73092 | 2024-10-18 00:43:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 4b1daa73-b5f2-3b2d-a2a9-1130b4d6ca82 | -4.23236 | -45.69561 | 2024-10-18 00:43:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4054ad36-25c5-3d10-a595-88fb595e3e9b | -4.22442 | -47.85187 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ccf8f8ed-22ad-3c4a-ba08-23b5bc117839 | -4.22299 | -47.84135 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a9d45c82-4b19-3bcd-9cd3-c886e3f88625 | -4.19505 | -47.49484 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0fca8f50-28b6-3a9d-9dc0-26495d913176 | -4.19369 | -47.48492 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5bcf6f02-bc3d-3ce5-82b2-6a2c3475b4fe | -4.18573 | -47.49628 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0342bf43-a759-3a6a-84e7-d34533988043 | -4.18437 | -47.48629 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78433bd9-7f2b-3f04-af7e-c7dbc04db528 | -4.08992 | -45.3986 | 2024-10-18 00:43:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 03b0773d-3032-3ff4-8260-122224fe9bc1 | -4.08109 | -45.39985 | 2024-10-18 00:43:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9114c09d-c374-3c1c-aba5-5557e1499630 | -4.07987 | -45.39106 | 2024-10-18 00:43:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6bc5ab98-3a47-3593-8032-d0539e581d48 | -4.07223 | -50.9814 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e8e8b164-932e-35b4-84dc-f6c2f7282a16 | -4.06937 | -51.13988 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5e6aa213-f3bc-3fdd-9e1f-cd0406059fe3 | -4.06694 | -51.12202 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 60639550-0e6d-3dfa-a843-3c38f1b58efd | -4.06565 | -50.97566 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b7705f2f-2b08-3064-af62-98504eac95f8 | -4.04226 | -50.43718 | 2024-10-18 00:43:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0acfac1c-92af-3bc9-beea-405f866766f3 | -4.03658 | -46.94392 | 2024-10-18 00:43:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 89dd27ac-1165-3758-9de9-92b61a35a94c | -4.03617 | -48.95394 | 2024-10-18 00:43:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 04f33a75-6899-3590-b28c-d646532881f0 | -4.03529 | -46.93461 | 2024-10-18 00:43:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7e9d2515-e3d1-334b-a74b-1985353b222d | -3.99125 | -45.48159 | 2024-10-18 00:43:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c9da2dd3-614f-31be-b1f4-1c90ec7541ff | -3.9785 | -45.51926 | 2024-10-18 00:43:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README6.md)
