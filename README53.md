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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35a07ea0-fbe1-3441-bc5f-b4269da3ee83 | -10.20334 | -44.56529 | 2025-10-09 05:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2c7a217d-8adb-3ef6-9b70-745d0ecad9bb | -2.1922 | -54.47649 | 2025-10-09 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b11be0e-7e3e-38fc-a22f-be501efa05c4 | -2.88966 | -50.72599 | 2025-10-09 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80065366-64b4-3c31-8e1d-2d7c49f602fe | -8.72063 | -47.10189 | 2025-10-09 05:10:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be0b0aed-584d-3e8f-bc58-dad5bb4bcaa4 | -3.53711 | -48.91983 | 2025-10-09 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb7147e5-b52d-3a95-9bf8-09a1bf441bd6 | -2.78808 | -49.59246 | 2025-10-09 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53ef096f-27a0-31b1-96fa-8efeecef9f3c | -5.31027 | -45.38002 | 2025-10-09 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aba4936-d339-35de-b21e-76aefc170c69 | -4.77264 | -45.59447 | 2025-10-09 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca3a0e0e-8c4b-32f2-849d-2c549ca30449 | -4.6939 | -45.83756 | 2025-10-09 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22f0c940-895f-389b-95db-d3978cb8d228 | -6.46082 | -44.58229 | 2025-10-09 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 200cc49a-3102-3e8e-9b89-1b0e6e25b9e0 | -5.45532 | -43.50344 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 41d91097-c9e6-3baf-97c9-26090d3fe70a | -4.3621 | -45.56893 | 2025-10-09 05:10:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1daeec48-fad1-34c4-ad67-60816ae1169a | -3.0968 | -51.1256 | 2025-10-09 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a3f19cd-0e6a-3bd6-89d3-976719ff9eac | -8.56156 | -44.62383 | 2025-10-09 05:10:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f26a698-a3b7-374c-989b-5ef9e4db616a | -10.1986 | -44.5611 | 2025-10-09 05:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1964b074-4cbc-3dd2-ae17-92c9b79e9a29 | -7.79926 | -44.2027 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7461deea-abe5-3f1e-ad88-cf911ce26f70 | -7.79835 | -44.19681 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eec4d7c6-6215-374f-9f48-fb0e18dd9caa | -3.10675 | -47.79963 | 2025-10-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80143ae4-b940-3f6e-9cca-1fcdbf5c3b5a | -8.56241 | -44.61696 | 2025-10-09 05:10:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 84e4d30e-cd84-3f42-a85f-2878b6c881ef | -2.19163 | -54.48019 | 2025-10-09 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14d80735-ef66-31bb-81e8-458ee4eea0df | -4.72549 | -43.35229 | 2025-10-09 05:10:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b6499648-69e8-3730-a496-0e4d39699023 | -3.10722 | -47.79644 | 2025-10-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79f6cef3-c2da-3ac3-8752-41b566eec51e | -3.15746 | -49.17626 | 2025-10-09 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65890042-55c3-3964-9b75-5cee58a6c58d | -6.69212 | -46.3054 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 302c8a37-bb39-3c96-83b6-45820ec8d74a | -4.50196 | -46.35142 | 2025-10-09 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b05c39a7-1636-373c-b43b-8453a3b0295a | -4.42985 | -47.7518 | 2025-10-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12687899-8407-3a18-a67f-4bf97654d256 | -2.8842 | -50.73332 | 2025-10-09 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b84503a-27b5-3e6e-9ad8-0f0b21be0e5f | -3.38758 | -50.14015 | 2025-10-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5b88160b-0f43-32e2-a110-3b817337d95b | -7.20526 | -45.92173 | 2025-10-09 05:10:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81bec670-b643-3699-a7f9-bbfe19c34a2a | -4.8217 | -47.34521 | 2025-10-09 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c09a74c-4632-315b-a091-9af741c2b21e | -7.63926 | -45.23165 | 2025-10-09 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9876ec6-8f0d-307d-8fef-5693aa2dda7c | -6.68513 | -46.30336 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| d0520f73-428d-32dd-9fc2-dd95d841a6b8 | -3.3869 | -50.14469 | 2025-10-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64169230-7f4a-3d9b-93b3-4d8417eaddc4 | -4.2552 | -48.55589 | 2025-10-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b290c81-06ce-3b0f-9607-65168f8c8361 | -9.67982 | -48.38691 | 2025-10-09 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce920d74-6630-3f29-b74a-259a0aa2815d | -6.16185 | -43.76245 | 2025-10-09 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 61531279-2d85-3d35-ba2c-23da7ffb2f9f | -4.1138 | -50.05032 | 2025-10-09 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a8fd033-456b-3375-bc35-e440381fa140 | -5.13791 | -46.25468 | 2025-10-09 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 320c6813-b69d-36d0-be30-336484a16d00 | -6.69274 | -46.30067 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d015f2f5-7b13-3b71-8a5b-2d4edae81422 | -6.15995 | -43.75972 | 2025-10-09 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e51585bc-321d-388d-9831-cb5e26c6c266 | -6.69119 | -46.30429 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 7f852fa0-3dca-336f-ad3a-2c24d03ee598 | -7.80532 | -44.19801 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1a9eb90-a24c-372b-843d-57e5be1ed23a | -7.45411 | -47.17907 | 2025-10-09 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd6fa0cc-3dec-323c-b379-7836709ccfbb | -4.77218 | -45.59209 | 2025-10-09 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6535cd8-e12b-3d17-a884-d161c4389150 | -6.16272 | -43.75599 | 2025-10-09 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9124a9f6-73d1-35bd-a9f3-4b4baddc12bd | -3.3965 | -50.14156 | 2025-10-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd4f157b-6f5b-3ba6-9915-2d0113b86b85 | -3.2644 | -50.11942 | 2025-10-09 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b756744f-87b1-3ec8-986a-23f75cc2d677 | -2.88906 | -50.72998 | 2025-10-09 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12dad777-f935-34dd-821e-175650f16ce1 | -3.07387 | -49.10976 | 2025-10-09 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66b26a75-c16c-3c54-a613-1919bd3f143a | -5.65259 | -43.6079 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9ca2929d-8c44-3993-aaa3-6b5beb187893 | -3.39204 | -50.14087 | 2025-10-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6ab9d88-af38-3932-94f6-cf0e27954653 | -3.51986 | -49.7227 | 2025-10-09 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64600062-28b2-3bfc-9925-d502059e922c | -4.68651 | -45.84585 | 2025-10-09 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aff555f1-adf4-3e31-9b86-f7bdf6f42384 | -7.75672 | -44.02939 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d52d1fbe-d241-30a2-8574-e3656fa919d8 | -4.36763 | -45.57436 | 2025-10-09 05:10:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7ae1aab-c851-303a-b7cf-8238478686d6 | -15.22064 | -46.37672 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6ea11b2c-a844-3a01-be73-322819ba1e06 | -10.15463 | -64.24925 | 2025-10-09 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b172d61d-ac9e-35fd-af4d-de214acab225 | -15.24307 | -46.35482 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 04398ca1-aa33-3115-82f3-3d428af3e274 | -13.67494 | -48.74544 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f77bfcc6-d95c-318b-be6b-48cc14de6615 | -12.26706 | -47.89544 | 2025-10-09 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6d025509-788a-36e0-8247-6a8eab34f8ea | -15.23061 | -46.37844 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc4e8465-652b-3e5c-bbce-524ad11014c2 | -13.6693 | -48.7442 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73e5cc53-2e1f-3c8e-a2e9-33ecf4aba3c3 | -15.74576 | -49.02718 | 2025-10-09 05:12:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b5a54790-d9cc-3202-a3f3-8824445cb43f | -15.2166 | -46.38282 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2d7373c-1659-375c-9f2c-29d1499e570d | -10.85562 | -49.93829 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a195e3db-4092-3914-bf34-b5f4656136d2 | -12.08628 | -64.2328 | 2025-10-09 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0080a1f-d80d-3aa7-bb02-5bceae8e15ac | -15.06683 | -48.0813 | 2025-10-09 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6eff473a-5b70-3b3b-a641-9687d2535bd3 | -15.24023 | -46.35045 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25a310ab-49bf-3f9d-86b0-70b331bf2228 | -13.2937 | -48.46331 | 2025-10-09 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0bdfbb6-1ceb-3e5b-8ec8-3472ba0de406 | -15.49522 | -47.9609 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f64e1fe-279e-373a-b0fc-518ef7d56fdb | -10.86215 | -44.63122 | 2025-10-09 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| b21400b4-e7d4-3f56-a3a5-08aa00a3c6c5 | -10.5512 | -50.04215 | 2025-10-09 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 137d9c6c-1f7b-37c8-9142-348bdbb1553e | -11.7512 | -45.14122 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c4a39b1-c39e-372f-a1a4-465838e4ba2e | -14.73593 | -46.09164 | 2025-10-09 05:12:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 068c4a3e-0021-3184-a386-2b1212a87cf4 | -15.48863 | -47.96453 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4883b2c6-ef92-30ce-ac81-b3f528dcc04e | -15.23231 | -46.36158 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d946c09-949c-3df2-ad16-654ec846ebea | -15.29592 | -46.15829 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23395120-4bab-3b43-958a-e7aedd04eb38 | -10.86416 | -49.91194 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c91febb-e1e0-3410-8209-da2cd5d07d94 | -15.40349 | -46.2721 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3580cabd-f211-3af0-9c62-f296bf4efdf7 | -14.07565 | -50.15454 | 2025-10-09 05:12:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31ef0a2f-abc2-312e-a652-675b404519da | -14.85264 | -48.45015 | 2025-10-09 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 461c3006-48b4-3035-9140-cf02d73f7967 | -11.90726 | -64.03474 | 2025-10-09 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04674c71-702c-3cc5-8671-e494cb0c0fb1 | -15.39428 | -48.04049 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e1ec86a-bf9e-3458-a372-ac2cdac6b352 | -9.29936 | -68.2491 | 2025-10-09 05:12:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 904c8174-f3fe-39b1-95dc-c4da1c047af9 | -10.52806 | -50.02404 | 2025-10-09 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4b8744c-1c7d-3e3b-af61-3451ad291c37 | -10.53345 | -50.02183 | 2025-10-09 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d94e0694-bab3-3686-9769-7387151bab14 | -10.86374 | -44.61711 | 2025-10-09 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| da25feea-5252-36bd-a9b7-b3dabf9c184d | -15.00609 | -47.53057 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c17855e2-530b-311a-9457-f62300e81a7f | -11.75049 | -45.14764 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba4e2fbc-7c07-3962-8272-9be4bd5988d6 | -15.75466 | -48.72505 | 2025-10-09 05:12:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb32bb74-517a-3e25-802c-8ff27d606737 | -12.39882 | -63.88765 | 2025-10-09 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b53b70b4-2839-3321-997c-bf1a348e7851 | -14.94988 | -47.70546 | 2025-10-09 05:12:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 19173e64-9a6e-373d-b1b5-b5bc544c9d95 | -14.93167 | -46.79019 | 2025-10-09 05:12:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0959649f-156b-310f-9211-577548737ac1 | -15.21714 | -46.37744 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e79a28a-7193-30a9-9736-520dd7feaa9e | -15.48976 | -46.8672 | 2025-10-09 05:12:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8304b43-657a-3c13-a55c-6867d7f6e707 | -13.79079 | -45.8605 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c84cb40-1d27-3a62-a6bc-dbc7f38c4ee7 | -10.60143 | -45.01302 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c06ba7c8-650d-3b62-8cd5-53dd35d07e20 | -10.86338 | -49.91796 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 118c142a-0f02-3446-9eeb-16aaa9439e2a | -10.73695 | -50.06678 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ea8bed8-e8be-3851-8336-cb422bc2c897 | -12.1522 | -63.06094 | 2025-10-09 05:12:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README54.md)
