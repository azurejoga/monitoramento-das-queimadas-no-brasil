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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67e8292f-6e9a-3388-98d5-71962c708b84 | -14.1254 | -51.7088 | 2025-09-06 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 5b6be3e3-7ec0-333c-b6b1-927ff3d773f9 | -14.1061 | -51.7113 | 2025-09-06 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 296.7 |
| 0989cb4c-bb09-3853-b470-4d3a2d98dd34 | -8.3649 | -48.2681 | 2025-09-06 12:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| d4c081b9-3bee-3841-acbb-d4c186b34f3b | -9.6843 | -51.0819 | 2025-09-06 12:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 247.2 |
| 7f163fac-a936-3d42-aa42-be378f7a2826 | -6.4021 | -46.0944 | 2025-09-06 12:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e4cd1177-9559-3ce1-9b63-8dae4dbd4dfe | -9.0951 | -47.0093 | 2025-09-06 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| a0f80a37-a5e1-397a-a362-af09a181fe7a | -6.8751 | -45.5851 | 2025-09-06 12:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 96aedea5-97d8-3ace-a0b3-87f66266fad2 | -7.1681 | -48.0861 | 2025-09-06 12:40:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 47bb2f31-a54e-3ebc-b6ab-a2c267bfb1ea | -10.3137 | -46.4248 | 2025-09-06 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| d069513c-ae72-3cca-b82b-78a85488470b | -10.6128 | -44.3284 | 2025-09-06 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 302.9 |
| 2da97690-4e63-3898-bd73-3f8c2679347d | -14.125 | -51.7301 | 2025-09-06 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e790b330-71eb-3ff5-9335-b1704c4d74c9 | -15.7186 | -53.5743 | 2025-09-06 12:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 46e9f8d1-68a8-3692-acaf-d9454728fa05 | -9.6841 | -51.103 | 2025-09-06 12:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 320.7 |
| 50742b5a-8b0d-3cdb-bd04-e98a18a567bf | -10.5937 | -44.331 | 2025-09-06 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e411e365-d1fd-3d89-b350-e1162abd1eac | -11.0249 | -45.9274 | 2025-09-06 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 8b6c3b87-5879-34b8-9a1b-5c107758bb92 | -10.314 | -46.4022 | 2025-09-06 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| d31efd26-47a2-306d-8a58-2c4f6fbb2faf | -11.2302 | -46.1949 | 2025-09-06 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 0ad85666-0707-3214-a8ea-23a2113867e1 | -5.7298 | -43.9189 | 2025-09-06 12:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2397c535-48f6-3110-b252-85733b2dada5 | -6.2036 | -43.3709 | 2025-09-06 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| bf32d4d4-df51-3f42-849f-0c311fbc4019 | -14.1057 | -51.7327 | 2025-09-06 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 8ea3a9c6-6743-3ff1-bf37-10ae25f894d6 | -12.8636 | -47.9877 | 2025-09-06 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 752e36f0-8efe-3811-81b7-85159a100c4c | -10.3327 | -46.4225 | 2025-09-06 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 01e62485-227d-3d94-8521-1117f7b209f8 | -11.0245 | -45.9502 | 2025-09-06 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 87b75c4e-b51b-3aa7-9b8d-35c29461288d | -13.9026 | -48.0347 | 2025-09-06 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 79dcf5f3-19fa-37e7-b08c-c0dfde6220d1 | -13.0161 | -48.0549 | 2025-09-06 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 2e006bbe-5e49-3a80-81be-0f6054cb4b2e | -6.2127 | -42.4532 | 2025-09-06 12:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 61fa2efc-5bf6-3e29-80a6-01c936aaa175 | -9.6841 | -51.103 | 2025-09-06 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 39f3a29d-c70e-3acf-a3d4-a276f85fdc9e | -10.3137 | -46.4248 | 2025-09-06 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 72dc8843-771c-34a7-b606-1751d7f1b8e1 | -5.7296 | -43.942 | 2025-09-06 12:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0de08daf-3aad-38e2-a69c-3dcfcc22e98e | -10.7794 | -48.2797 | 2025-09-06 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| a26aaba5-bba4-30f2-b412-12fabbaf4863 | -9.7031 | -51.0802 | 2025-09-06 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 48141dd2-6d31-3d88-a130-d87b511a7de7 | -10.6128 | -44.3284 | 2025-09-06 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 338.1 |
| 6e57a162-75d0-353d-986a-413e4f120f78 | -11.0242 | -45.9729 | 2025-09-06 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.7 |
| f7c04f5e-ab2f-3985-bf60-403e2268a375 | -6.2203 | -43.5791 | 2025-09-06 12:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 043c948e-c83a-3776-9237-e9ce8fcdcbfa | -6.4021 | -46.0944 | 2025-09-06 12:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f0a78eff-99f9-373f-8542-74e00a0c7694 | -9.0951 | -47.0093 | 2025-09-06 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 238f7062-41ef-3e46-a884-3a08aafb2cab | -11.0051 | -45.9755 | 2025-09-06 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| abaa1160-3fb8-332b-82ca-d1cdc2a0d165 | -5.7298 | -43.9189 | 2025-09-06 12:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| b47d64a0-1966-3fef-bcc2-861ff2ae0b0d | -6.2036 | -43.3709 | 2025-09-06 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4e1bbd4c-7b0d-3670-a8f1-78412b346436 | -10.5937 | -44.331 | 2025-09-06 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 4363d474-1c8d-345b-93e2-6044df9c77f8 | -10.3134 | -46.4473 | 2025-09-06 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 2d60b3ab-2aab-3c2b-8d78-0c511ee9f9c2 | -10.3324 | -46.445 | 2025-09-06 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 271.7 |
| eb2b046f-9887-3b77-a360-75022b47f228 | -13.0157 | -48.0771 | 2025-09-06 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 8ab15e80-223e-3d1f-9d9c-81834582f5f8 | -15.7186 | -53.5743 | 2025-09-06 12:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2192bc91-30ec-35b0-b2e7-c515c661d5b2 | -9.0948 | -47.0316 | 2025-09-06 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| dee06c6d-0833-3d18-b966-f43318fc1d39 | -9.6843 | -51.0819 | 2025-09-06 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 3bd89531-575e-3609-91e3-6b18eb1d229a | -13.0353 | -48.0521 | 2025-09-06 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| b3ae82a0-7a52-3575-bb93-fd0bd6eaea65 | -5.7298 | -43.9189 | 2025-09-06 13:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 193.3 |
| e80d6577-bd31-3d18-9918-fcbbee781e22 | -5.7296 | -43.942 | 2025-09-06 13:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a23b1556-1593-360a-b4e6-fb42da074b4e | -11.2306 | -46.1722 | 2025-09-06 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| dc61709f-4513-3731-987e-9283f4d9f2a1 | -6.2036 | -43.3709 | 2025-09-06 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b761281e-3d0b-36a4-9787-ebbca299e503 | -9.7029 | -51.1013 | 2025-09-06 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 8bb8438a-fd39-326d-83d9-ca55b5560b85 | -10.3134 | -46.4473 | 2025-09-06 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e5881ff2-38a9-33a3-a206-d77a9657fb18 | -13.0161 | -48.0549 | 2025-09-06 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 976528e9-71bc-3dc6-ad32-e65cda767cf2 | -11.0242 | -45.9729 | 2025-09-06 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 246f121b-f2c1-3175-9f2b-de1daa7a68eb | -20.5415 | -46.4648 | 2025-09-06 13:00:00 | GOES-19 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 8f8cb681-bf38-397f-9734-d4dfc338b15d | -6.3555 | -47.0965 | 2025-09-06 13:00:00 | GOES-19 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 431992c6-0b97-3b4e-b8b1-b2d64cf7f2f8 | -10.3137 | -46.4248 | 2025-09-06 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 0458a356-4759-3a5e-9c05-1d367edc321f | -9.6843 | -51.0819 | 2025-09-06 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 51f8500d-311d-3560-b67f-eecf921caa66 | -9.0951 | -47.0093 | 2025-09-06 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| d6c0e9aa-3780-3212-bbfa-baf4135280c8 | -6.4021 | -46.0944 | 2025-09-06 13:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| b42e31ba-2a45-3d47-a440-b70f4cfbd27c | -6.2203 | -43.5791 | 2025-09-06 13:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| d240282f-0ce7-3263-aa00-cebd7e2428a6 | -10.6128 | -44.3284 | 2025-09-06 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 217.8 |
| 4abd1374-8f63-3813-aed3-d052ca7aee3f | -6.1945 | -53.2381 | 2025-09-06 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| af1a1dda-5e29-3510-8c0d-0be9db8c82a2 | -10.3327 | -46.4225 | 2025-09-06 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 219.5 |
| 8ef56f3c-1b14-3345-8bbf-268616dc0e12 | -7.1681 | -48.0861 | 2025-09-06 13:00:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 16832cb3-e9b2-36b8-8392-322d6ec5978a | -10.7794 | -48.2797 | 2025-09-06 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| a5198d7a-66fb-3114-9ca1-b938ab5b321d | -10.3324 | -46.445 | 2025-09-06 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 153.9 |
| d3b32827-9dc8-3914-b400-3acff4de7070 | -15.7377 | -53.5928 | 2025-09-06 13:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a51a6074-f743-36c0-bc53-c986cd107e1e | -13.8006 | -52.7454 | 2025-09-06 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 55e8a3a2-9434-3cd0-9bba-d0e86fd4d74d | -11.2302 | -46.1949 | 2025-09-06 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.3 |
| a09af49c-4080-39ae-ac90-d342d49757fd | -7.6881 | -50.2991 | 2025-09-06 13:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 2882ee9e-2851-3aff-9753-3dd69c67d981 | -11.0245 | -45.9502 | 2025-09-06 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 0fee86c4-fb44-338d-867a-7e88b87017f4 | -6.2127 | -42.4532 | 2025-09-06 13:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 729cd83a-d75c-3ae5-8185-0fd32bf808ed | -9.6841 | -51.103 | 2025-09-06 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 37cf1454-fd4d-3c88-b569-6ca19d425158 | -13.0353 | -48.0521 | 2025-09-06 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5f126047-6899-362a-a290-6e8c92e799de | -9.8079 | -46.0118 | 2025-09-06 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| c4984d4f-a37a-336f-b3fe-345a0f047380 | -15.7186 | -53.5743 | 2025-09-06 13:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| ea41190a-0fa6-3f74-9ea9-1f36e23c273f | -10.5937 | -44.331 | 2025-09-06 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 68778f3d-9497-348d-8984-e6bcc5792d42 | -6.2127 | -42.4532 | 2025-09-06 13:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 147.8 |
| 01b5daa6-c6a2-3dac-b8b5-fc466af04dcf | -7.3322 | -48.5074 | 2025-09-06 13:10:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e4003067-9ee4-3684-ad8c-b3a9e4f534fe | -10.6128 | -44.3284 | 2025-09-06 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 241.6 |
| c81d92e0-cd1c-35a7-976b-7c46cb658cb6 | -15.3064 | -52.7208 | 2025-09-06 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| fe5e4927-cd4e-3fab-a976-48455f2ef292 | -11.0245 | -45.9502 | 2025-09-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 308.8 |
| 1a75607b-4029-30e3-a976-3b40e52f6945 | -7.8593 | -44.9053 | 2025-09-06 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| fa1d0b25-7c1e-3c69-a94d-0113f0925ec9 | -12.8028 | -48.1739 | 2025-09-06 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 75da86ac-d56b-3081-9d1d-2431f1e1bf6f | -11.758 | -47.739 | 2025-09-06 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 455e3b3c-223c-32d6-b162-48d623fe0500 | -11.0249 | -45.9274 | 2025-09-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| eff34470-6217-3ebe-be38-fbe0fe5beae4 | -5.7296 | -43.942 | 2025-09-06 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 0e61b9bd-de01-3108-be34-f807bb202a65 | -13.0353 | -48.0521 | 2025-09-06 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3542c50f-72cc-387c-8a3b-aadd68121e22 | -7.6351 | -44.7671 | 2025-09-06 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0c1f48d3-430d-3023-8ba8-76ecf8f3dbef | -14.1061 | -51.7113 | 2025-09-06 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 312.8 |
| 8a751666-e2f0-3f6c-a7d9-b7a9fd670d15 | -6.2315 | -42.4515 | 2025-09-06 13:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| e3c93804-2553-36bf-aba5-a992eea5599f | -15.7186 | -53.5743 | 2025-09-06 13:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| c82e8905-410d-33c6-9c7f-47e248aca3e8 | -10.5937 | -44.331 | 2025-09-06 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 7096af18-7872-32dd-a194-a86847bedbf9 | -13.0161 | -48.0549 | 2025-09-06 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 336d1479-29d4-3360-9eb2-83d4513e1589 | -6.4021 | -46.0944 | 2025-09-06 13:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b83eabd1-7179-3ed3-aa12-cf6ec4b30972 | -14.1254 | -51.7088 | 2025-09-06 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| ba1d16e7-b21c-3092-8ab0-6792a62ab3d3 | -9.6843 | -51.0819 | 2025-09-06 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 883bfae6-338a-38a0-9a25-2f95e1bc8b2e | -11.3567 | -50.3161 | 2025-09-06 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |


[Clique aqui para ver as próximas entradas](README92.md)
