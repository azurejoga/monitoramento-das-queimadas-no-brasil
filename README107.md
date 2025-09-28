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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 801a0301-75f1-38d0-a537-3c28bb761ea1 | -13.6122 | -48.0787 | 2025-09-28 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 6f7f89e9-e6c1-3ba6-b462-3a92fb19aded | -15.8879 | -46.2177 | 2025-09-28 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 123.8 |
| dc9c84e5-db83-3f89-9436-c4783329b057 | -9.3013 | -45.7082 | 2025-09-28 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8581b7f2-2cdd-38de-ba6d-a941ae6052d6 | -10.9137 | -45.7375 | 2025-09-28 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.2 |
| 6cd9fe0b-ac12-3fe7-a5d3-c0467a72717b | -9.1102 | -45.8653 | 2025-09-28 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 34080315-ede4-3e5f-a4cc-e274e473e4bd | -9.0874 | -47.6074 | 2025-09-28 14:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 1028f1cc-10a5-3bab-96cd-a847768b7a32 | -5.7583 | -42.8447 | 2025-09-28 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| c93cee92-6046-3631-836c-3d458a9d9b0b | -3.2898 | -42.6918 | 2025-09-28 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| fb2678af-cc2c-3204-9e59-dc2baf5b89f7 | -6.6978 | -44.6003 | 2025-09-28 14:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b757a046-244e-3c0d-b8ac-6939fe629673 | -14.8263 | -45.5815 | 2025-09-28 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| e2699492-97dd-32c5-9215-d5ceaccd8704 | -11.4413 | -44.9998 | 2025-09-28 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 79fc894b-640c-3295-b835-9d5e3dc18efd | -5.6223 | -43.3701 | 2025-09-28 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d587f3a0-cd97-3351-8ff4-443afd489fd0 | -11.9986 | -47.0596 | 2025-09-28 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 66d7e50a-bd23-3028-b1d0-379910ae9880 | -11.9456 | -47.936 | 2025-09-28 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 17bbafca-bd1f-3c87-baa6-8699034cadcd | -7.3849 | -47.0157 | 2025-09-28 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| d6997184-c759-31af-8d70-dbd7eea6c8f2 | -11.3642 | -45.0339 | 2025-09-28 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 3943149a-8317-36eb-ac10-18a21a5bc022 | -8.2856 | -45.4545 | 2025-09-28 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 177.2 |
| df1804f3-9868-3286-aee3-f51ec0963457 | -7.8634 | -44.5612 | 2025-09-28 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 173.9 |
| c751f099-3d19-35cf-aa2b-75f984cdf791 | -9.3331 | -47.56 | 2025-09-28 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 7ae28fd2-483f-3486-8c45-744eec3afa35 | -5.6462 | -44.9102 | 2025-09-28 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 73cbee76-0c10-3b06-b139-dd7d00f4fb5f | -6.6181 | -45.0631 | 2025-09-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 27d28903-9910-37eb-a722-a8796cb8917a | -11.3842 | -44.9849 | 2025-09-28 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 5e308b71-aa75-3470-bec9-1a313d7edc1e | -12.9547 | -45.1618 | 2025-09-28 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 7f94e4f0-0523-3e6b-a181-1ad228953c4e | -5.3057 | -43.1599 | 2025-09-28 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 2e78f1d2-5757-33a8-b59f-82c8f6e12741 | -10.8242 | -45.3841 | 2025-09-28 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 429.2 |
| f66a4be1-eb0a-35e3-8e99-6aaf8be6ddf8 | -11.9794 | -47.0622 | 2025-09-28 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 499dd6cc-6626-3e7a-9533-067a4a484aca | -5.8885 | -45.0064 | 2025-09-28 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 2811789c-f147-3766-a583-aa864255ec88 | -6.3154 | -43.4548 | 2025-09-28 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 0cd73d2d-13c8-3860-8b40-d06282b436f4 | -5.8272 | -45.5985 | 2025-09-28 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 10273796-4edd-343a-9192-f0c4d7a740e5 | -5.9076 | -42.9268 | 2025-09-28 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 6371dde6-ff0c-37d1-bf28-2c9375770be1 | -4.1574 | -44.2726 | 2025-09-28 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a8c22be2-b2cb-339a-9854-7c4cd50d1fb4 | -12.7637 | -50.4921 | 2025-09-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b98aad94-f492-31bc-afe9-654da2787105 | -12.9354 | -45.1649 | 2025-09-28 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| a729a8bc-c307-3d57-8d1f-568cb14d812f | -14.885 | -45.5708 | 2025-09-28 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 34488d15-200c-333c-a44c-c5761fe7338d | -6.6986 | -42.741 | 2025-09-28 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 29503221-7509-374c-8c97-02a28aec787f | -13.6069 | -47.3408 | 2025-09-28 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6ea3e7e8-1e63-3ea5-a5ef-74a8a29c28a6 | -5.17 | -43.7276 | 2025-09-28 14:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 2e98f9c8-b252-3070-8765-3f4e520c2ca9 | -10.0373 | -48.5381 | 2025-09-28 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 28d901b3-b9a1-3941-b5ad-af97b9aca718 | -9.2824 | -45.7104 | 2025-09-28 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| edf31423-c6f6-3487-8dbd-b35136856e67 | -5.6275 | -44.9115 | 2025-09-28 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 2fbdbae3-8df8-3124-93f5-b7b324c9117c | -4.1391 | -44.2277 | 2025-09-28 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b4961eb4-3c70-368c-83d1-4ab925652342 | -6.5611 | -45.1359 | 2025-09-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 9881d99d-22a9-3fff-9e65-b4048ee4f193 | -9.9578 | -43.6222 | 2025-09-28 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 988c659b-5de3-34c3-a67d-2c371d1e9a97 | -6.3 | -45.0205 | 2025-09-28 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2a82b53c-472c-39e1-8421-8afd63bf8334 | -9.4196 | -54.6767 | 2025-09-28 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 296.1 |
| 9e29f795-94ed-3ed8-9b6f-d90b66b3357d | -9.1099 | -45.8879 | 2025-09-28 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b3a0372e-f434-3f8b-bb0f-86f2ac0decc6 | -11.9044 | -44.7928 | 2025-09-28 14:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| d8a883b0-0ec7-39d5-a48d-177586d2f7d9 | -5.1885 | -43.7495 | 2025-09-28 14:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| cf5eae01-573e-31b9-a3e5-ee8c27ad47c1 | -11.9644 | -47.9557 | 2025-09-28 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 71d30d94-9c6d-3227-8870-a10807d03194 | -8.2859 | -45.4317 | 2025-09-28 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 410d4236-4168-35d5-b236-1083bfeb4ef0 | -5.9041 | -43.3018 | 2025-09-28 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 327546ee-67bf-3345-8e6d-52c23f5c5d6b | -5.3693 | -42.3077 | 2025-09-28 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 6e63cacd-ce94-39c9-82c5-3625c0207113 | -5.7585 | -42.8211 | 2025-09-28 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 854a1ebc-738b-3c7a-813c-780198d03817 | -7.2605 | -42.9939 | 2025-09-28 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 34fcdc57-eca4-3689-9431-4c7f9bac9857 | -8.1611 | -46.4122 | 2025-09-28 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 360.2 |
| 7447bb16-bfa1-3225-87c6-c790f9b9f98c | -12.0218 | -47.9481 | 2025-09-28 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 173367b1-ab12-39bf-b588-86a2c81675f9 | -4.4013 | -44.0755 | 2025-09-28 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 257.9 |
| 896152e8-eb47-3bd8-b9f0-e893835585ba | -14.8845 | -45.5941 | 2025-09-28 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 15ccaf55-e6d1-3adf-8725-cb89d3746ece | -9.4455 | -47.6144 | 2025-09-28 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 125b78f9-63d8-3391-bbd6-39bf73522326 | -7.7555 | -45.7324 | 2025-09-28 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1d6392b3-3a5f-3182-bd60-33c894cb19f0 | -14.5955 | -48.2386 | 2025-09-28 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 2116dc56-a475-3134-be2a-c4b93216d792 | -12.9363 | -45.1184 | 2025-09-28 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 7d0d93e6-303d-3cc7-b851-5779e85d93c4 | -8.2668 | -45.4564 | 2025-09-28 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 151.3 |
| c763eb33-6f5f-3882-8333-c0bda2f23f5b | -9.4009 | -54.6781 | 2025-09-28 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 182.1 |
| 9bce7f70-f6ab-3e87-bd9d-741aae4cd269 | -5.8883 | -45.0291 | 2025-09-28 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| f323ae94-5f68-3e7d-a333-192969b3db01 | -10.0184 | -48.5401 | 2025-09-28 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 818e0018-a69d-39b2-9786-88aa760c1748 | -6.6192 | -44.9493 | 2025-09-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fa07ba79-898e-3f18-bb14-d82293dc7511 | -5.9006 | -43.6744 | 2025-09-28 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 9196a033-22f9-32dc-8f53-b5d641152d33 | -15.9076 | -46.2139 | 2025-09-28 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 3b4745f4-9d75-36e9-9b9b-447142e6a1f1 | -13.7893 | -47.8957 | 2025-09-28 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 9a8f9eeb-70a5-35e6-9fc4-ff61e4f882c9 | -5.7398 | -42.8226 | 2025-09-28 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| c9457454-6c8d-3d1e-892c-ca43d594b110 | -11.3654 | -44.9645 | 2025-09-28 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 1bfd886a-bf7a-314c-ad72-f3b74de96f0d | -6.619 | -44.9721 | 2025-09-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 240b2c43-fa70-3d0a-99d4-f96230484697 | -5.8187 | -44.4413 | 2025-09-28 14:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| d298ed52-d336-380c-ac85-616d634f1059 | -10.8051 | -45.3866 | 2025-09-28 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.8 |
| d351d1a1-fa81-3e7b-87d1-751136cc5260 | -6.6178 | -45.0859 | 2025-09-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 230f825c-25c4-3c7a-b712-8872f9339d7b | -11.4217 | -45.0257 | 2025-09-28 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7c99212c-7943-3545-88de-e5f9bea5c24a | -7.8634 | -44.5612 | 2025-09-28 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 3d2f6a61-26f2-3ab5-8777-65342dfa77f0 | -11.9828 | -47.9976 | 2025-09-28 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 55c4b1cc-13aa-36fe-a4c4-77c957a96fb5 | -5.2869 | -43.1613 | 2025-09-28 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 0a1b08e5-da10-3edc-be47-5e4c6ce2e605 | -6.3154 | -43.4548 | 2025-09-28 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 1ffe5887-c214-35fd-942e-c7a4a0d5ed73 | -6.9954 | -44.8488 | 2025-09-28 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 92e1c61b-bca9-3bfe-991d-3ae5c88ff62f | -5.1885 | -43.7495 | 2025-09-28 14:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 165.2 |
| e0d2d9ae-b0f7-33a9-abb0-23ab99d28038 | -6.619 | -44.9721 | 2025-09-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 8b9867cf-fde2-38a0-8db4-d7efea47e554 | -5.7583 | -42.8447 | 2025-09-28 14:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 9024973b-9543-3e26-b9b6-55cbc7969a23 | -6.6005 | -44.9509 | 2025-09-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 16fecb6f-c931-3690-88f1-b940add957b4 | -13.7898 | -47.8733 | 2025-09-28 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 3e641f6e-9bb5-3869-a706-702db4bb89f1 | -14.576 | -48.2417 | 2025-09-28 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 145.3 |
| e8f48895-596a-35d3-b4de-dc177e0d7651 | -7.8163 | -47.0003 | 2025-09-28 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5d27ea2a-17f5-32a7-bfd0-b8f1371837f5 | -13.6122 | -48.0787 | 2025-09-28 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 248.5 |
| e9c87e12-efd1-3cc6-9f4b-470047fdee2e | -7.8823 | -44.5594 | 2025-09-28 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 40337d11-5972-31b5-bd97-e1e263a19117 | -8.8407 | -47.7639 | 2025-09-28 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 9d57618b-f929-3abc-8053-0696479f033a | -11.3889 | -46.9847 | 2025-09-28 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 6856ae2d-6e31-324a-a0c8-b8971937356d | -5.9006 | -43.6744 | 2025-09-28 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| cecb6965-dc6f-3af6-a899-9627b4096a60 | -11.9456 | -47.936 | 2025-09-28 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 194.4 |
| cf42aba3-98b2-30ce-804c-178be9ab7af7 | -5.1712 | -48.4792 | 2025-09-28 14:40:00 | GOES-19 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 0aacc93f-6b2b-32e6-b84f-6ce993b4b6c3 | -9.7643 | -47.7786 | 2025-09-28 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3f3efb02-8b05-31c2-a544-8ceb17728026 | -17.7338 | -46.7056 | 2025-09-28 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 98.7 |
| a22cecd8-3357-3016-9e53-fbd4d62e83db | -11.3654 | -44.9645 | 2025-09-28 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 164.8 |
| b984e0da-590b-3dc6-b75f-f9a4b87fe8ce | -8.2665 | -45.4791 | 2025-09-28 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |


[Clique aqui para ver as próximas entradas](README108.md)
