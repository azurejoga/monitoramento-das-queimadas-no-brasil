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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f82e291-2be9-350d-85ad-df9180904f88 | -10.7108 | -69.415298 | 2024-10-02 02:12:18 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 134b554d-a0b6-3a37-af2e-83faa569ab4b | -10.6918 | -69.378197 | 2024-10-02 02:12:18 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad43911-8d12-3146-a5bd-6bd5449a83de | -10.6936 | -69.386101 | 2024-10-02 02:12:18 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 52de32cd-72cc-342b-b571-38a661e22fe8 | -10.5406 | -69.305298 | 2024-10-02 02:12:20 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d5327541-03ab-388d-9ab3-21d15f295158 | -10.5425 | -69.313202 | 2024-10-02 02:12:20 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e9c73649-fede-311a-81ca-dd47fcb05125 | -10.5309 | -69.307602 | 2024-10-02 02:12:20 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e90292ff-f6df-316d-8b51-b37b3203da72 | -10.5328 | -69.315498 | 2024-10-02 02:12:20 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ea3e1b58-d4de-3df0-867a-08d02cf89d92 | -9.9137 | -66.832497 | 2024-10-02 02:12:21 | METOP-B | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6ab49f24-7ef0-3cb7-a0e7-c88da55f2d43 | -9.9164 | -66.843498 | 2024-10-02 02:12:21 | METOP-B | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 34bf3831-8405-3331-b511-876da8a42f5e | -10.1256 | -67.890503 | 2024-10-02 02:12:21 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d6c49d16-709c-31dd-bc44-57d08dcfbbbd | -10.1038 | -67.885696 | 2024-10-02 02:12:22 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b85504ae-fa48-3ede-9b5f-0f95cf4d3ba8 | -10.2675 | -68.754402 | 2024-10-02 02:12:22 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 27dce9d7-7ac7-30e5-9dab-0444ec9df33c | -10.2695 | -68.762802 | 2024-10-02 02:12:22 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b041a7ec-73d5-3219-beca-56fbbe8f75ec | -10.0622 | -68.014999 | 2024-10-02 02:12:23 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c5bf2a42-5193-35bf-afa6-58ab24c972e0 | -10.0644 | -68.0243 | 2024-10-02 02:12:23 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4141004e-c47d-3619-9d6a-9c45493f8457 | -9.2004 | -64.592598 | 2024-10-02 02:12:23 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f13af7c4-f49e-35ba-b4a7-939366ff3ae5 | -9.5841 | -66.493202 | 2024-10-02 02:12:25 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e91af7fe-a36e-3a0b-8ec9-a86b2e252ba1 | -9.5869 | -66.504898 | 2024-10-02 02:12:25 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08a5afd4-47d7-3ae6-a0cf-b31acfd02a1e | -9.2901 | -65.330902 | 2024-10-02 02:12:25 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf9646b-075f-3838-9ca8-48a5b44b1202 | -9.2936 | -65.344902 | 2024-10-02 02:12:25 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e78e7f8e-5207-397e-a449-50fe423445fd | -9.5411 | -66.614304 | 2024-10-02 02:12:26 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33e980a7-fdbf-351f-90e9-51f27a693ac0 | -8.4604 | -62.709999 | 2024-10-02 02:12:28 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be1f6a2d-2117-32fb-83a2-7768aabe1bae | -9.631 | -67.460999 | 2024-10-02 02:12:28 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 74555526-71cf-32f1-9858-6e0c006840e5 | -8.4507 | -62.712502 | 2024-10-02 02:12:28 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c9ab6cf1-8de4-3543-8c15-d84ae63a01d0 | -8.4563 | -62.734299 | 2024-10-02 02:12:28 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65debe2b-0c79-38c6-89af-6a0a87f99763 | -9.4922 | -67.096802 | 2024-10-02 02:12:29 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcf6f469-8f51-34f6-a5df-74133d15c0c6 | -9.4948 | -67.107498 | 2024-10-02 02:12:29 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c50c5a6-404b-3be8-90dd-a2023550cf87 | -9.7581 | -68.519501 | 2024-10-02 02:12:30 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1b39f89d-5383-3d8c-ba2f-73ee7d410b84 | -9.5348 | -67.706596 | 2024-10-02 02:12:30 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b5c888bf-806c-3526-93e5-9c3faebea769 | -9.6688 | -68.797997 | 2024-10-02 02:12:32 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c7447098-7eae-3305-9e0c-c05fa127fb29 | -9.6708 | -68.806602 | 2024-10-02 02:12:32 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f8841ea2-4510-3734-83a4-622ba4fca95c | -9.6728 | -68.815102 | 2024-10-02 02:12:32 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e3e6e5ab-6079-3447-8a81-4b12967058b5 | -9.3062 | -67.656799 | 2024-10-02 02:12:34 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1f60fa2-42c3-3667-ab48-3786880cd3c7 | -9.27 | -67.591202 | 2024-10-02 02:12:34 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8caeb7f0-95d8-3937-b662-de210f361ee6 | -9.2724 | -67.601303 | 2024-10-02 02:12:34 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6ba4ff3-0783-397e-a258-4a54b1250e4d | -9.2602 | -67.593597 | 2024-10-02 02:12:34 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9b1d431-b347-3c21-8492-19076d35bf57 | -9.2626 | -67.603699 | 2024-10-02 02:12:34 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5a5bc0f-e93d-3f6f-860f-5c9b16b344e7 | -9.4797 | -68.520401 | 2024-10-02 02:12:34 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c87aba2f-4405-3439-928d-0c19be987190 | -9.47 | -68.522697 | 2024-10-02 02:12:34 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 31fc5eb2-985c-3fee-820f-12753170b2a5 | -9.456 | -68.507202 | 2024-10-02 02:12:35 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d9a5edf5-73e7-375a-8b08-8e2068150654 | -9.4581 | -68.516098 | 2024-10-02 02:12:35 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a46b5384-36a5-33fd-94e5-4b5e7ece8008 | -9.4602 | -68.525002 | 2024-10-02 02:12:35 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 33626245-1091-31d7-a405-38bd642b66d7 | -9.2829 | -67.819199 | 2024-10-02 02:12:35 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4db74b97-25d3-3b16-8594-abec6cbc33aa | -9.3842 | -68.246597 | 2024-10-02 02:12:35 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4bf2d235-43e5-34dd-9d71-ede0d1397293 | -9.3864 | -68.255798 | 2024-10-02 02:12:35 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| db1a7259-6c15-3ea3-8f53-0eefcd646f05 | -9.3951 | -68.292603 | 2024-10-02 02:12:35 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4b1d7727-0805-37db-8ba2-ca9f7d7ff4f5 | -9.3972 | -68.301697 | 2024-10-02 02:12:35 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 38fb8657-18e5-3da7-a436-fa2e1f45b00c | -9.2732 | -67.821602 | 2024-10-02 02:12:35 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 094f2c91-1c87-37fd-a1bf-29daef279542 | -9.2755 | -67.831398 | 2024-10-02 02:12:35 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a79a313-4b14-35e6-ad28-4052a6b525a9 | -9.2778 | -67.841202 | 2024-10-02 02:12:35 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa7224d5-ab7e-3df6-871e-62dab7742e56 | -9.3515 | -68.195702 | 2024-10-02 02:12:35 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ff9de6b5-5d83-374a-9f99-0ff7bb08cd3c | -9.3722 | -68.327003 | 2024-10-02 02:12:35 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f705458b-8cfa-3a01-8890-7ed3f3032408 | -9.3744 | -68.336098 | 2024-10-02 02:12:35 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9f2be01e-e9de-3bbb-b664-405ea145d2a0 | -9.3765 | -68.345299 | 2024-10-02 02:12:35 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ed1ee1ff-6734-3623-a1f7-1426b92851c1 | -9.2104 | -67.774399 | 2024-10-02 02:12:36 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dfc11953-9bcf-3406-9fdd-b30cd9ed4982 | -9.0945 | -67.547699 | 2024-10-02 02:12:37 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1492ac8b-885e-3d31-a3bb-808d955a9e3c | -8.9214 | -67.039803 | 2024-10-02 02:12:38 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 296af612-e816-33fd-98ad-f739245fcacf | -8.9937 | -67.341698 | 2024-10-02 02:12:38 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d3f93d2-eb00-3b2c-aed9-2e775edc14c7 | -8.9962 | -67.352203 | 2024-10-02 02:12:38 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee90c1a9-ce7f-374b-8968-4ea4639b73d9 | -9.1866 | -68.284103 | 2024-10-02 02:12:38 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ca079ed-9dc4-3011-84c1-33554170464e | -9.1769 | -68.286499 | 2024-10-02 02:12:38 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31d76a6f-07ed-3dd4-b7ad-7564ac31e2e3 | -8.7656 | -66.606697 | 2024-10-02 02:12:38 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 389b75f3-29a8-3bd0-a6d6-d463e0c49de5 | -8.7559 | -66.6091 | 2024-10-02 02:12:39 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 372d8e28-46e2-3cfe-95b8-cb27b81c07b4 | -8.911 | -67.383904 | 2024-10-02 02:12:39 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7756add9-fefb-32fe-aeac-fa12ca3fed5c | -8.755 | -68.905502 | 2024-10-02 02:12:47 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ee7c4df-1ea0-3ac6-bd17-448a589d6a39 | -7.6364 | -67.185097 | 2024-10-02 02:12:59 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53275526-375b-31ba-9357-5ed99048304e | -7.6391 | -67.196404 | 2024-10-02 02:12:59 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed888a7f-6977-3999-8e94-bf2e25eabbdd | -7.2163 | -72.3078 | 2024-10-02 02:13:25 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dec572f2-2a05-3f89-b1d4-2a608c9f7678 | -7.2178 | -72.314697 | 2024-10-02 02:13:25 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4279280-6bf8-3d66-b0b4-9365e023097c | -6.1301 | -47.2664 | 2024-10-02 02:15:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| bef31dff-f8d3-315e-ac6c-efccd241d35c | -7.1796 | -46.9444 | 2024-10-02 02:15:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fb162b9f-b1d8-3e22-ac88-9ea98e24dcc7 | -8.4642 | -62.7313 | 2024-10-02 02:15:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 1a621b9b-9329-3759-b8c8-07122261cde1 | -8.4643 | -62.7124 | 2024-10-02 02:15:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a6de3b5a-7f03-3428-bc06-d8d810e98acc | -10.0802 | -46.8337 | 2024-10-02 02:16:03 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| cb8074e8-f3af-31d0-bcf5-c4324662b559 | -9.9367 | -64.9179 | 2024-10-02 02:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 06e2d392-c2d5-3ed8-b4ee-34dfb3d52b4b | -9.9368 | -64.8991 | 2024-10-02 02:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| ddfb1b7c-fda9-3a7e-863a-69a28610fcc4 | -9.9553 | -64.9172 | 2024-10-02 02:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 0123eeb8-bddf-30a1-a67c-fecd9bf23fb3 | -9.9554 | -64.8984 | 2024-10-02 02:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 230ca39c-5861-36bb-9b8d-8ddb8d645d63 | -11.6742 | -65.0172 | 2024-10-02 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b11cba2c-b43a-3e76-8822-10201e19da3c | -11.6743 | -64.9983 | 2024-10-02 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 113.3 |
| a0276518-1fb0-3b8f-9bcd-6addac2a921b | -11.6554 | -65.018 | 2024-10-02 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 08f4eb8e-9892-30f7-9a4a-5aafab879f02 | -11.6555 | -64.9991 | 2024-10-02 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 51c013d0-47a5-3ce2-b89a-af71c0539bd3 | -12.4433 | -43.7242 | 2024-10-02 02:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| afc39e55-7c3a-31f3-bec8-cc36a6096785 | -12.2946 | -47.6446 | 2024-10-02 02:16:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b9f3819a-de3a-31a9-8dc4-f46dfc02ad88 | -12.7054 | -63.0798 | 2024-10-02 02:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d4a9e546-d757-3234-8b8e-22722f7f2b47 | -12.6486 | -63.1022 | 2024-10-02 02:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 41.7 |
| bc816c05-93d3-3107-905d-586bd25373ed | -12.6484 | -63.1214 | 2024-10-02 02:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.1 |
| d5d6b2fd-fd11-36af-8637-d9e37e5cdcdb | -12.8615 | -62.5129 | 2024-10-02 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 7b2acea9-7328-37b4-9a48-b21647568ab9 | -12.8614 | -62.5321 | 2024-10-02 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 2adaea19-33e7-35dd-8bcc-ab433de74cb0 | -12.8612 | -62.5514 | 2024-10-02 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e630088b-ac45-355f-9e8c-bb9f98ba3387 | -12.8593 | -62.7826 | 2024-10-02 02:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7aabfa07-1b7a-3791-bddc-16358b6406f5 | -12.8426 | -62.514 | 2024-10-02 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 11df57f8-3183-3522-8232-42ee859f21da | -12.8424 | -62.5333 | 2024-10-02 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 5970b930-bb9f-3130-9099-d59dc863d6bb | -12.8423 | -62.5526 | 2024-10-02 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 202b0506-23ef-3f3d-843e-d718858da7db | -12.9548 | -62.6806 | 2024-10-02 02:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 8ed542ad-9420-3598-9008-d4049530cc4c | -12.9546 | -62.6999 | 2024-10-02 02:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 218ae03a-1615-3660-9a75-7c778645bab5 | -12.9358 | -62.6818 | 2024-10-02 02:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b2e0818f-74e7-38df-b5ac-34dbeb7439ee | -12.9357 | -62.701 | 2024-10-02 02:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| e5793ced-3e78-3f2a-83d8-08ac678b3db8 | -13.5965 | -51.1367 | 2024-10-02 02:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ae84b590-3f67-38c8-840f-5353334e7222 | -14.5699 | -44.8351 | 2024-10-02 02:16:27 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 54.2 |


[Clique aqui para ver as próximas entradas](README44.md)
