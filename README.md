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
| 81914130-48fc-36f1-a498-e67b3725c09e | -8.9368 | -47.6005 | 2026-07-19 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| fc983942-d248-31e1-ae16-6fae566a9a1e | -9.0887 | -50.6074 | 2026-07-19 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| be1caec8-0d9e-3308-a053-32d2a56a88f6 | -9.1075 | -50.6058 | 2026-07-19 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 1f19cf3b-5f76-397a-9379-d1fcfbbfb772 | -4.0351 | -49.2625 | 2026-07-19 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b5ea24ad-f3dc-3c19-b2d3-7773b638e49b | -9.0889 | -50.5862 | 2026-07-19 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5c45abcf-e470-321f-b463-865aeeedeef9 | -7.1029 | -47.1273 | 2026-07-19 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 86b27d7f-ae9d-3928-8e22-da0ff637309a | -7.1031 | -47.1053 | 2026-07-19 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7e446d48-cc7f-387d-b477-bad654c3730a | -10.8273 | -50.2244 | 2026-07-19 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 57f5f401-3789-3c9b-b093-21eb3d626416 | -8.9368 | -47.6005 | 2026-07-19 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 65f16075-88d3-3533-9ecd-57478308c705 | -9.1075 | -50.6058 | 2026-07-19 00:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b0be5f51-0f70-3e5f-893f-81900d090c7b | -10.8273 | -50.2244 | 2026-07-19 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 900d7796-a1e7-363a-b794-8f5f69e25bcc | -7.1029 | -47.1273 | 2026-07-19 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c676c218-be11-3e5c-8967-87535ea4869b | -7.1031 | -47.1053 | 2026-07-19 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 1ad6fa52-3d0b-30d6-8565-696677ee1acc | -11.6062 | -43.1161 | 2026-07-19 00:26:00 | METOP-C | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3f1d0e2f-1783-398c-ba87-7382df60669b | -10.8211 | -50.236599 | 2026-07-19 00:26:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd4edc29-061a-32c4-8988-cd28caeb06fc | -4.0284 | -49.248402 | 2026-07-19 00:26:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf2e3fee-0731-3a48-b2f9-bfe549ae41d0 | -10.6982 | -46.617298 | 2026-07-19 00:26:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcb1b514-750d-31e3-819f-04ff0f40a149 | -4.0382 | -49.2463 | 2026-07-19 00:26:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07e4694c-52b6-33a9-a5d8-61911dc23621 | -5.9307 | -43.645802 | 2026-07-19 00:26:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d00eaf0-1e27-3ea0-b45e-6e3e0bc6b713 | -11.9816 | -47.099098 | 2026-07-19 00:26:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0719ac7-daaa-364f-a828-a364e497ef89 | -7.1151 | -44.041401 | 2026-07-19 00:26:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ac251817-ef94-3f24-96fd-f7a0e3f9f7b4 | -12.6655 | -48.209599 | 2026-07-19 00:26:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 426f8a21-10f1-37b6-b39c-599e1cc0c04b | -11.6046 | -43.1091 | 2026-07-19 00:26:00 | METOP-C | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e28413e6-542d-3e95-a6c1-829fc50e426a | -12.6676 | -48.2197 | 2026-07-19 00:26:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22006d86-c9b7-34e3-9bb4-a34916f2a66b | -11.6295 | -47.948299 | 2026-07-19 00:26:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9978ccf-9565-35fa-b3eb-421e3ca00efd | -6.7344 | -44.360199 | 2026-07-19 00:26:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6dbaa91-8fdf-339f-855b-997a1521561e | -10.8159 | -50.211102 | 2026-07-19 00:26:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97c2b33f-9e7f-3683-b54a-cc319f938ba6 | -12.6578 | -48.221802 | 2026-07-19 00:26:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53ceb7ef-fadd-3b7e-86c6-f5bf383acb98 | -9.0924 | -50.594398 | 2026-07-19 00:26:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e4e8697-7c58-3d6b-bab5-01daaaa56a75 | -8.3602 | -45.393501 | 2026-07-19 00:26:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7326f321-2017-3a6b-bf2b-fbb75c33a8c3 | -10.6867 | -46.6115 | 2026-07-19 00:26:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 621375e3-f7f6-3276-89a3-7545cbbd2318 | -4.0149 | -48.958801 | 2026-07-19 00:26:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a428e914-87d8-3a70-bb61-cadbc33bbce1 | -11.6275 | -47.938801 | 2026-07-19 00:26:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70dbca9d-9d41-3fad-8430-d333eb520a15 | -4.0401 | -49.255199 | 2026-07-19 00:26:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5c39b96-0a48-3182-8823-1f209b227fbe | -8.3618 | -45.400501 | 2026-07-19 00:26:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0eacb584-157d-37e8-8e0d-a4b41c4b25f6 | -5.7118 | -45.663399 | 2026-07-19 00:26:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2495be38-cdbd-372a-94c9-06279458b43a | -7.2972 | -46.253899 | 2026-07-19 00:26:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00103a1d-e72b-3f3d-9dc5-d82056cdaef1 | -10.6965 | -46.609402 | 2026-07-19 00:26:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8657e035-4b54-340d-89dd-2a56d61293e1 | -11.9718 | -47.1012 | 2026-07-19 00:26:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d482773-6705-3872-915b-cf80f4c10d4e | -4.0362 | -49.2374 | 2026-07-19 00:26:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcc3cade-31ff-3336-82a1-5f0e65d4c3be | -7.0979 | -47.111698 | 2026-07-19 00:26:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf7e1184-273e-3cef-82f5-5de904514db0 | -5.7299 | -49.096199 | 2026-07-19 00:26:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99cf5a71-b949-3113-be1b-78b1c53ff90f | -7.1013 | -47.126999 | 2026-07-19 00:26:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1ac2224-0cb9-37f8-8273-50a1921a8e9a | -10.8185 | -50.223801 | 2026-07-19 00:26:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f01b132-d474-3f58-97f4-161dd53dd547 | -6.7359 | -44.3671 | 2026-07-19 00:26:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57ca9542-0767-394e-ad59-eb2b5343d3bf | -7.3038 | -46.2374 | 2026-07-19 00:26:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8309f16f-6fe3-3c32-8771-1d4f0d519039 | -8.9445 | -47.612999 | 2026-07-19 00:26:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c28778e6-bd92-39d5-af28-8fd645bd0ef5 | -3.8403 | -49.050999 | 2026-07-19 00:26:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f472c40-a741-358d-ac9a-1106e8394f43 | -5.53 | -45.271801 | 2026-07-19 00:26:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c01c373f-fbc3-3c64-93fa-17962a8d5b86 | -8.9427 | -47.604599 | 2026-07-19 00:26:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61823849-de74-3505-bcb9-029bb604673f | -9.1048 | -50.605 | 2026-07-19 00:26:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e10bb3cc-3187-31af-abbf-d74d33625262 | -7.294 | -46.239498 | 2026-07-19 00:26:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00a706de-e9f0-31a1-bd30-d110f94b2368 | -2.794 | -49.518101 | 2026-07-19 00:26:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1636804c-14a6-356f-b7f0-95e369e86843 | -7.0996 | -47.119301 | 2026-07-19 00:26:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf0df755-655a-3455-830e-998ae55f2c43 | -7.3054 | -46.244598 | 2026-07-19 00:26:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30a154ad-cac9-38a1-91b6-070b07b91016 | -9.0826 | -50.596401 | 2026-07-19 00:26:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac5e8fa9-9dd6-36aa-ab94-e2f702ec065d | -8.9311 | -47.598301 | 2026-07-19 00:26:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5e2287a-c443-3aa0-a021-94f6e14ddfc5 | -10.8087 | -50.2258 | 2026-07-19 00:26:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85202a5a-fd5e-3f23-80f2-447d0081a92f | -11.9736 | -47.109798 | 2026-07-19 00:26:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bac2920c-7514-3f3c-9ab0-548ae6426796 | -11.9638 | -47.1119 | 2026-07-19 00:26:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cefadac-04ba-3db2-b7c4-6e7357d8d9a3 | -20.080099 | -49.568001 | 2026-07-19 00:26:00 | METOP-C | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3c7c244-f9b7-3ab2-a538-c30c61cdf89c | -11.9834 | -47.1077 | 2026-07-19 00:26:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff0ea47a-b99e-3f57-8dc4-19687cb74c00 | -21.7363 | -41.362202 | 2026-07-19 00:26:00 | METOP-C | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 48a10884-0909-3183-b283-5ecc2482648f | -9.0951 | -50.607101 | 2026-07-19 00:26:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1fd283e-8b4c-3b4d-bb30-f34fa5427bcc | -8.9329 | -47.606701 | 2026-07-19 00:26:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17464356-f401-32c4-9fe9-2ebc778d36a6 | -4.0303 | -49.257301 | 2026-07-19 00:26:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b68760a-b13b-3b51-b190-d7e3824ec6e0 | -5.5284 | -45.264999 | 2026-07-19 00:26:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21cbfb3b-9d7d-35b6-b007-b881713511ef | -2.8319 | -48.8661 | 2026-07-19 00:26:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42388378-be80-3a5c-8e95-26c413229e5a | -7.4559 | -49.440102 | 2026-07-19 00:26:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca096675-6328-3515-9ad0-c1155149baa4 | -2.8301 | -48.857899 | 2026-07-19 00:26:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e577bfaa-895b-332a-a273-90a7bfa74d9a | -9.383 | -40.753201 | 2026-07-19 00:26:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 273beb5f-83a3-3390-bfe7-e11b0f11906c | -5.9291 | -43.638699 | 2026-07-19 00:26:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80d9bbe6-4f29-363f-862a-c875e3f4b3ab | -9.0978 | -50.619801 | 2026-07-19 00:26:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05311666-7a88-3d49-b083-f14bcc5b9423 | -9.08 | -50.583698 | 2026-07-19 00:26:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 979caee4-a1cd-3002-a4df-4b2613e0ff3f | -9.3928 | -40.7509 | 2026-07-19 00:26:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7239fbdb-f018-3364-a8b5-22fde0b32470 | -5.7103 | -45.656601 | 2026-07-19 00:26:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bac4712-3c20-34a5-92dc-accf773630da | -8.9409 | -47.596199 | 2026-07-19 00:26:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 778ffb83-8bc9-3343-8740-e453e61e310e | -10.6884 | -46.6194 | 2026-07-19 00:26:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8add912a-cc95-3ba4-8b12-1c493f54ba7d | -7.2956 | -46.2467 | 2026-07-19 00:26:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e054f02e-4161-37d6-a29a-5093d16ebfd5 | -9.0702 | -50.585701 | 2026-07-19 00:26:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 864c1235-d3ba-3a50-99b9-3a127670826a | -12.6557 | -48.2117 | 2026-07-19 00:26:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd2bdb95-d659-3968-9fe4-d08194f5f7ba | -10.8273 | -50.2244 | 2026-07-19 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| da541b8c-bd93-3da6-a5ab-fc9ba5db27b0 | -10.8271 | -50.2458 | 2026-07-19 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| d68b417a-7968-360e-9e6d-5baf49cc88e1 | -10.8273 | -50.2244 | 2026-07-19 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| e4fe2947-1476-3bef-9a60-ad1108ac92ec | -7.1029 | -47.1273 | 2026-07-19 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8ae19eee-83cf-392b-8ca3-cc9daccbaaee | -10.8273 | -50.2244 | 2026-07-19 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c13476f7-87d2-35d9-a230-4dbcf26c427e | -18.8004 | -51.2417 | 2026-07-19 00:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d8b3d642-8a54-377b-812b-1b4ea7e875cf | -10.8271 | -50.2458 | 2026-07-19 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 72de10fd-dac8-397b-b36c-8d6c139f22fa | -18.8009 | -51.2196 | 2026-07-19 00:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 32a30ac1-aa37-32df-8d46-4426a6ed86a7 | -10.8084 | -50.2265 | 2026-07-19 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| a58673dc-c795-355f-8c5b-8290ae93c3c2 | -18.8004 | -51.2417 | 2026-07-19 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 58a56091-1709-3e1d-b5d0-702aac662b7c | -10.8273 | -50.2244 | 2026-07-19 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 7589e918-bfeb-3c70-b614-0e1b2b9674a7 | -18.8205 | -51.2381 | 2026-07-19 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 74204c31-d7bc-3767-bb13-639ef3443804 | -18.821 | -51.216 | 2026-07-19 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a3595585-8857-3a65-aa23-c6967ccc112a | -18.8009 | -51.2196 | 2026-07-19 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 1727e0d9-0357-3630-984f-187bb7d23661 | -10.8271 | -50.2458 | 2026-07-19 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| ed7b29a0-4543-3220-8421-25380bf1e91b | -18.8009 | -51.2196 | 2026-07-19 01:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 180.9 |
| f0951e20-6719-3523-a55f-a999b03b8344 | -18.8004 | -51.2417 | 2026-07-19 01:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 393.1 |
| b34a8bb0-79ac-34a2-8a6e-b2dcb8072e09 | -18.8205 | -51.2381 | 2026-07-19 01:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 66a21ebb-e99d-3581-ab7b-78837f4ee1c6 | -22.2404 | -56.0079 | 2026-07-19 01:10:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 67.9 |


[Clique aqui para ver as próximas entradas](README2.md)
