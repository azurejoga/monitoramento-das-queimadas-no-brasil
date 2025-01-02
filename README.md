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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 365a6360-5b81-3126-a3b3-2c01cbaeca18 | -10.6115 | -44.315399 | 2025-01-02 00:18:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 239fd3ca-41bb-39b2-91fd-a25fdf24b5ef | -4.6945 | -47.038898 | 2025-01-02 00:18:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81da2371-f8b2-35c1-9763-324a4e7a631f | -7.6564 | -35.181301 | 2025-01-02 00:18:00 | METOP-B | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f2db9fb7-a624-3386-9ec9-bdd2fcfcf5f7 | -4.693 | -47.032101 | 2025-01-02 00:18:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a2381b25-0bd6-3cf0-b652-928cb8a94a4f | -10.6017 | -44.317699 | 2025-01-02 00:18:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5715784-d619-3734-9223-d9c61a811acd | -10.6131 | -44.322701 | 2025-01-02 00:18:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3bb1a61f-c387-35e3-90b7-e15b5ed7c56a | -10.6034 | -44.325001 | 2025-01-02 00:18:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed98659c-23e6-37fc-af22-ef8457fb4bf6 | -13.1342 | -41.757999 | 2025-01-02 00:18:00 | METOP-B | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b0b8f02b-3339-3c76-b5a6-46ba2533ec0a | -10.6 | -44.310398 | 2025-01-02 00:18:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76be828c-04a8-34bc-9c27-88f7b13fd99d | -1.7422 | -45.877201 | 2025-01-02 00:18:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 851b47c9-bf33-3463-ab85-540594d24a28 | -14.87433 | -40.77814 | 2025-01-02 00:26:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 08385a6d-f2f4-397b-a7bc-414df8451922 | -14.87562 | -40.78727 | 2025-01-02 00:26:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| b01e994d-9a82-3171-9ad7-7d8e383267d0 | -7.14483 | -35.05365 | 2025-01-02 00:28:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| 529a632b-b4b4-3daa-a18d-931cfcb92dcf | -10.11436 | -36.50773 | 2025-01-02 00:28:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 90966642-9557-34c1-9868-07de5446c763 | -9.16983 | -42.99175 | 2025-01-02 00:28:00 | TERRA_M-M | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 00a52748-462b-3b48-81f7-fa8b4a5045ae | -9.00813 | -35.98857 | 2025-01-02 00:28:00 | TERRA_M-M | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| d88c6143-037e-394e-9455-941d97bd99f6 | -8.43669 | -40.53965 | 2025-01-02 00:28:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b46e01ec-6f15-3aef-a99c-bd2755f51baa | -13.13372 | -41.7714 | 2025-01-02 00:28:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1a08a255-74e9-3e20-a2d6-1a26bdb430a8 | -10.60218 | -44.32949 | 2025-01-02 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 47e34683-289e-3110-aac6-044d121e399c | -10.61155 | -44.3282 | 2025-01-02 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| a99c53e3-6700-3e58-b7d4-142ae7b15734 | -9.87033 | -37.07426 | 2025-01-02 00:28:00 | TERRA_M-M | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 369a4f5c-77ab-3966-b71a-3a94bab0e698 | -10.55554 | -45.21302 | 2025-01-02 00:28:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b504c0f5-acb1-33d5-a000-64ba963845bc | -7.14701 | -35.04681 | 2025-01-02 00:28:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| a62bfcd5-4bbc-30de-a212-a862e505e994 | -10.61291 | -44.33831 | 2025-01-02 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ce911807-b029-3afd-9e84-6c4c766ff034 | -10.6102 | -44.31812 | 2025-01-02 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 88987a0f-1dc6-36bf-8216-eb85b7a97422 | -4.26043 | -40.66618 | 2025-01-02 00:30:00 | TERRA_M-M | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7691fee9-6140-397d-935f-03ead537d412 | -5.99906 | -43.58018 | 2025-01-02 00:30:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e1e197d0-be4a-3f79-8151-cc02ed8b973f | -4.69603 | -47.04697 | 2025-01-02 00:30:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 7edf74e2-636f-3036-885b-f4695dc7bacd | -4.98444 | -44.16923 | 2025-01-02 00:30:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0349aa06-4222-38ce-9869-f5d642413e46 | -1.73975 | -45.88473 | 2025-01-02 00:32:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5afacfcb-318a-373d-a757-df50177b6c91 | -1.74898 | -45.88346 | 2025-01-02 00:32:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4a3c0a0a-73ff-3c24-9664-1bbf45f88450 | -19.767 | -55.4277 | 2025-01-02 01:15:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 86cd227a-4c7e-3051-b332-a391b6a5fb5c | 4.0856 | -61.130501 | 2025-01-02 01:15:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ca32326e-2e9f-3ec9-bb0b-b84d050c2523 | 4.084 | -61.137699 | 2025-01-02 01:15:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd5f8b7-8cdf-316e-9396-56cc7cdb7605 | -19.338301 | -54.167198 | 2025-01-02 01:15:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ccc012da-6807-325d-bc8c-b85f557567f4 | -19.3367 | -54.16 | 2025-01-02 01:15:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d62b54c4-4e05-398f-a357-10803d06e5fb | -19.7768 | -55.4254 | 2025-01-02 01:15:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e877f298-c10a-3048-bfbe-d087685dbaac | -19.339899 | -54.1745 | 2025-01-02 01:15:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fe7b05a6-edf7-374c-9b12-3112e4390892 | 4.0873 | -61.123402 | 2025-01-02 01:15:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fe377d49-6d86-3817-b4fc-2a7176d42f87 | -6.63478 | -38.73766 | 2025-01-02 03:04:00 | NPP-375D | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fbc760a8-e846-3ecb-9ccf-f0ca239a9f5b | -5.242 | -36.18965 | 2025-01-02 03:04:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0d9c836-86dd-3d6f-8801-a4d22b8dd49d | -6.73093 | -34.97013 | 2025-01-02 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fb2d3530-93aa-36c2-9c03-6d8580eeec78 | -6.73149 | -34.96689 | 2025-01-02 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7d31b210-95ff-3de0-aa1c-5ea4a9ecc540 | -6.72931 | -34.96844 | 2025-01-02 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 010c024f-be95-3359-97fb-9048be2a6c8a | -7.90756 | -35.23434 | 2025-01-02 03:04:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2330a0b6-0604-3706-b5c0-71aec8a86b7f | -7.91285 | -35.23536 | 2025-01-02 03:04:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b2eb600b-5d3a-351e-8025-6367236f5caa | -5.24273 | -36.18539 | 2025-01-02 03:04:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee518015-2046-353b-99b0-4d52ce395742 | -7.03576 | -39.20889 | 2025-01-02 03:04:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 126d425f-57bc-3b76-be1c-c974080d7db0 | -6.73465 | -34.96924 | 2025-01-02 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a1350bbf-7f25-375b-9a09-25f8e32b5199 | -7.03463 | -39.21479 | 2025-01-02 03:04:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5f59a379-98e0-37e2-86ca-7ea3ff4c9f6d | -13.1332 | -41.77027 | 2025-01-02 03:06:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f1a0c9e-1276-3155-b645-2028b74278fd | -10.14861 | -36.55317 | 2025-01-02 03:06:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c64144c6-25a3-3b3c-8581-0b2b9106b29f | -10.14787 | -36.5571 | 2025-01-02 03:06:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b9670bce-8c19-31d2-b532-44d90914f3ee | -13.14028 | -41.77223 | 2025-01-02 03:06:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4ccf1b15-23cf-33c6-82fe-5f36586da28b | -10.14936 | -36.54919 | 2025-01-02 03:06:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 3.8 |
| abc79ee7-56c6-3894-aebe-bb5f56286964 | -14.97747 | -40.42039 | 2025-01-02 03:08:00 | NPP-375D | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74f4bf6c-a752-3d44-9ecd-be7c77cbc695 | -14.97095 | -40.4193 | 2025-01-02 03:08:00 | NPP-375D | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e8add173-3c90-3aaa-8682-f20d4b5255d4 | -14.97849 | -40.41567 | 2025-01-02 03:08:00 | NPP-375D | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bc2839ab-7f2c-3563-b68a-7a237bfd49c3 | -22.67367 | -42.85432 | 2025-01-02 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2dcc9fd4-f893-3b69-ba62-156f0eb27492 | -22.6723 | -42.85997 | 2025-01-02 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c8c73f15-923b-36d1-8535-653e3dd625c3 | -22.67862 | -42.86193 | 2025-01-02 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e46e4465-a629-3a93-a7ce-eb79f8e18d2b | -22.672 | -42.85985 | 2025-01-02 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ccf907c0-e057-34c1-9366-bbc32e055208 | -22.6734 | -42.85422 | 2025-01-02 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eb76372b-f884-3af9-a85f-2e0cdd8763ba | -22.67832 | -42.86178 | 2025-01-02 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4727e954-1732-332e-8efb-044685005ec4 | -22.67971 | -42.85615 | 2025-01-02 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8d7d21dd-c317-3a37-bbf5-73913096254a | -10.14888 | -36.55283 | 2025-01-02 03:27:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 11.7 |
| ee564839-5d87-33f5-bb4b-6b03bc83f729 | -10.50229 | -42.42841 | 2025-01-02 03:27:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c332253d-801f-3762-83f4-2a192a09833e | -6.63595 | -38.73742 | 2025-01-02 03:27:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 45e1d534-bf5b-36a4-b8d2-1557e7b5a686 | -7.91207 | -35.24135 | 2025-01-02 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2a76cd76-9d44-3ece-9e3a-4bdbfd55975f | -7.14207 | -35.05082 | 2025-01-02 03:27:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8a078760-945d-389d-a03d-2205b6db6c13 | -7.91339 | -35.23324 | 2025-01-02 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 33ec2aa8-20c4-3e3a-bd66-26ad7ffd0ce1 | -5.99027 | -43.58064 | 2025-01-02 03:27:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e286d458-51e7-3794-8d31-57c9443b8b55 | -4.39776 | -43.3824 | 2025-01-02 03:27:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe541ab2-39da-3eb9-a747-768731899f5e | -10.32571 | -36.72352 | 2025-01-02 03:27:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d3ddb82b-8981-3352-a6e4-307f12132fd3 | -7.14854 | -35.05603 | 2025-01-02 03:27:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| de46166c-761e-301f-9be2-bea2c7ea7cab | -5.99653 | -43.58175 | 2025-01-02 03:27:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2a3adb8-0731-3812-85ff-1587120ded1b | -7.9163 | -35.23788 | 2025-01-02 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ebef5b36-8714-3fbd-b4c2-c1cc3eff2c9f | -7.91696 | -35.23381 | 2025-01-02 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 639fc89b-3207-361d-b505-ad505756f423 | -7.90916 | -35.2367 | 2025-01-02 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 97757027-26e7-33d0-96fc-b4738531b4cc | -10.50163 | -42.43184 | 2025-01-02 03:27:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd118efe-8ff9-3ed0-88f6-360f6678da24 | -7.42566 | -35.11608 | 2025-01-02 03:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e4718253-44d4-3463-89f0-084034e594b5 | -7.94762 | -35.2933 | 2025-01-02 03:27:00 | NOAA-20 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 768e7d97-abce-30e9-8b9e-02cea39741a5 | -6.80233 | -35.29144 | 2025-01-02 03:27:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6e616b5e-72c4-39a7-b9a7-d25e5bcca36e | -7.94646 | -35.29111 | 2025-01-02 03:27:00 | NOAA-20 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c203ac44-b359-382a-8693-b273bac9a4fe | -7.94828 | -35.28919 | 2025-01-02 03:27:00 | NOAA-20 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 28f41ab6-f06b-3c7d-9cf7-3432f5ec5ab0 | -7.91273 | -35.23731 | 2025-01-02 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 017836fb-e9a5-318f-8aa2-66c78c157da6 | -10.49986 | -42.4308 | 2025-01-02 03:27:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9edae18c-301e-36fc-9124-35d6dd74a8e3 | -6.80594 | -35.29207 | 2025-01-02 03:27:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0bf13278-9ccf-38ba-8bd4-1e29f62e176e | -12.86046 | -38.3657 | 2025-01-02 03:29:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5a9486b1-8477-3922-ac60-30b61217aff0 | -13.13611 | -41.77305 | 2025-01-02 03:29:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0f60f139-f5ab-3a1d-8510-b57873d757b7 | -13.13734 | -41.76659 | 2025-01-02 03:29:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7099d31f-4230-3b46-a92c-8f15d65a2d8d | -14.8737 | -40.78539 | 2025-01-02 03:29:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5346c2ac-e4bb-3fb5-a860-058cf01e0de1 | -22.78265 | -43.75891 | 2025-01-02 03:32:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 772f6573-ec23-35a6-8ea2-a3490731d087 | -22.67636 | -42.85991 | 2025-01-02 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1fc31de4-1580-30eb-be67-7f213585b453 | -22.6773 | -42.85521 | 2025-01-02 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ac2fac1-5ca0-3e49-9a3a-daa9e189819b | -3.07024 | -41.88259 | 2025-01-02 04:21:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0be2908a-cf2f-382a-ad59-68ea3b134c55 | -6.80786 | -35.29283 | 2025-01-02 04:21:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 1abcbff8-27c2-37d9-ac73-088e28ddd39f | -3.72836 | -43.35561 | 2025-01-02 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80343ffa-8f8c-3c8a-b1a9-9c0430c63a33 | -1.79818 | -46.3263 | 2025-01-02 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2cd7ce0-733e-38c1-82a9-166036fb337b | -1.69267 | -45.89933 | 2025-01-02 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README2.md)
