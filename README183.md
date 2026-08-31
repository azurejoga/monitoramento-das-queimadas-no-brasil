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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 519bde3d-90ce-3373-84fb-36695d07c1ec | -3.4652 | -65.0054 | 2026-08-31 18:10:00 | GOES-19 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 112.5 |
| ed61f73c-87a0-3d71-bbbf-ae5642171fc9 | -11.2107 | -45.0786 | 2026-08-31 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| d9bcd840-751b-35d3-9905-d20ea212c496 | -11.2482 | -45.1194 | 2026-08-31 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 11d7d395-9526-3d9e-8226-21b6f36018f8 | -9.4153 | -45.6726 | 2026-08-31 18:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 8815587b-760e-3007-a3ce-d0758990f303 | -3.1267 | -61.1811 | 2026-08-31 18:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 228.6 |
| b8b68688-aabb-3d31-a492-08590c4402ef | -6.8419 | -41.7032 | 2026-08-31 18:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| d97057de-55b6-34fc-836c-5cad52cafa55 | -10.5906 | -57.4936 | 2026-08-31 18:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 35.2 |
| f1090e9e-5b4e-310a-9486-eeb941724a30 | -14.5028 | -52.1913 | 2026-08-31 18:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| e40d6a0c-0ff8-3401-9efd-b21c8fbe0a3b | -13.3936 | -51.802 | 2026-08-31 18:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a4beb813-4878-36d7-a8f1-a357ffa37960 | -10.01 | -44.72 | 2026-08-31 18:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ce2da48-a842-398a-be5b-f34ffc1c5e59 | -10.31 | -50.06 | 2026-08-31 18:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c1eb3f1-f730-32fd-87e0-e0fb9e9dcd57 | -16.76 | -51.92 | 2026-08-31 18:15:00 | MSG-03 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 71ba9c35-721b-350a-839d-446ce5116d66 | -12.97 | -45.96 | 2026-08-31 18:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d2c9f7b-0c60-3e26-9cee-5de1d9c19b84 | -16.76 | -51.98 | 2026-08-31 18:15:00 | MSG-03 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 21fdd2fa-cf75-31e5-a83a-38d66ac4bbdd | -19.2 | -57.4 | 2026-08-31 18:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 67b57612-2f41-3b1a-bd57-2229fb8b6c94 | -17.32 | -42.7 | 2026-08-31 18:15:00 | MSG-03 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d68d481a-b935-35f3-aa71-cea023143480 | -10.31 | -50.0 | 2026-08-31 18:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90112763-2aaf-3afd-8bdd-54d0b839b679 | -17.32 | -42.74 | 2026-08-31 18:15:00 | MSG-03 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4ec0d922-83cc-36cb-a8b6-9dda4183d025 | -10.08 | -46.64 | 2026-08-31 18:15:00 | MSG-03 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a151a9d-8199-3b20-8ff9-9728cba2f4ea | -10.34 | -50.01 | 2026-08-31 18:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6155aee0-a439-3bbb-8ba1-e93a7b12843d | -10.01 | -44.67 | 2026-08-31 18:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cf0330cd-9064-3f6f-a2f7-4f78374590c3 | -9.67 | -47.94 | 2026-08-31 18:15:00 | MSG-03 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84a58f5e-9ac3-3f38-aa29-40bd9dcb6d53 | -19.2 | -57.33 | 2026-08-31 18:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 26780ce6-5b01-3c69-9186-96c0d61420c1 | -15.6139 | -56.4103 | 2026-08-31 18:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 1a680e9c-3644-3587-bb2e-ce9e42c5cffc | -10.8404 | -50.6499 | 2026-08-31 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 77fda3db-8e28-340e-9b37-aeac86f97857 | -8.9428 | -63.2797 | 2026-08-31 18:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 726cfec9-5835-3034-a1f2-eabc330d3f35 | -7.3119 | -60.5706 | 2026-08-31 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.0 |
| d7629efd-5c6f-3aab-bcc1-1fbfe34a5431 | -7.1435 | -72.864 | 2026-08-31 18:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 9d5cdce7-46eb-3839-a576-11670826a521 | -10.8436 | -45.3586 | 2026-08-31 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 07832c25-61c2-310f-8fb4-890783806c95 | -6.7648 | -59.4408 | 2026-08-31 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 35a61888-67a6-3d3c-9b41-8616ed22678d | -9.208 | -65.8044 | 2026-08-31 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 6c378bc9-357c-352c-95f0-b06e7b4b0f6c | -9.19 | -59.5783 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a570c8c6-4e64-32f0-b731-afe651c3b6c8 | -13.967 | -54.395 | 2026-08-31 18:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 01242028-da6e-3af5-a5bd-99a9f0bcbff6 | -11.0933 | -51.5345 | 2026-08-31 18:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 182.3 |
| ea520b83-26b4-37b7-9ef4-ce01bc414619 | -6.8608 | -41.7013 | 2026-08-31 18:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 1a6489d3-51ca-3b03-80d6-0eb779c34cfa | -8.9873 | -65.4379 | 2026-08-31 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 7b6fedff-5acc-342d-ba09-cf292d54086b | -9.2081 | -65.7857 | 2026-08-31 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 57568f2a-21ca-3650-a931-d15d5bec107a | -9.9896 | -53.9404 | 2026-08-31 18:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| a4a3a3ad-04b9-3385-99b8-c08dfcfd0ff4 | -4.85 | -55.8266 | 2026-08-31 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| eb65019c-dec3-3119-ae25-46d954584db1 | -8.6674 | -62.8179 | 2026-08-31 18:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 17d60e2f-eb7f-3d41-9316-f9446e944bcf | -5.2548 | -55.8907 | 2026-08-31 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a753dcd1-728f-3f1c-a3ea-9fa448a4685c | -13.1837 | -55.6682 | 2026-08-31 18:20:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1b6fe485-f87f-33a9-a657-3aad34487fb9 | -10.7081 | -50.6425 | 2026-08-31 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 30176210-cb57-39a9-b803-82e9cc7045c4 | -7.5104 | -61.3832 | 2026-08-31 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 7d3f3de2-aa97-38e1-932b-4f899a775f60 | -8.5924 | -66.975 | 2026-08-31 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 89a961d6-9b32-3649-9dd6-6192ea1e7249 | -8.3601 | -70.8458 | 2026-08-31 18:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 9df9a125-1eaa-3329-b89e-81b06d1e55ec | -10.9865 | -48.3869 | 2026-08-31 18:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 66ce80a9-9265-3253-b4c6-f2aed9ab283d | -14.2369 | -51.9498 | 2026-08-31 18:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 0a2495f0-b2b8-39f4-93c3-6bd0a5155176 | -6.3875 | -54.7646 | 2026-08-31 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 9a3c6614-0c31-376a-adb0-cd5cde958e21 | -8.87 | -66.9121 | 2026-08-31 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7b1a445a-4ff6-30ec-85d1-cc517d687e28 | -9.3958 | -51.654 | 2026-08-31 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f34801fd-1097-382b-99b9-59fdcdff6322 | -6.9521 | -58.9506 | 2026-08-31 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e139be96-b8be-3a2d-bdf1-331604f33bdc | -3.6216 | -60.547 | 2026-08-31 18:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 180.1 |
| e45a4a98-e5fa-312d-8d15-1274f2461e99 | -8.7657 | -71.0421 | 2026-08-31 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 086b8374-10dd-3a8a-97bb-ff117a237a41 | -8.5177 | -55.3039 | 2026-08-31 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 4bfd4838-f546-3444-b78f-6ac56a869de2 | -9.9708 | -53.9419 | 2026-08-31 18:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1b8ac0a5-50d8-3c8a-a86c-f51d3c99fdc0 | -9.1544 | -59.3669 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 798c6821-994f-3e63-abe9-6b72df4adb09 | -7.4735 | -61.3846 | 2026-08-31 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| f2ea12d2-aad1-3a83-ac34-a7bb25d3ee41 | -3.4185 | -61.3273 | 2026-08-31 18:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| bcf9e6c0-fc26-3520-8448-f02f7ee322ba | -9.2099 | -59.4027 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 7e3b53cd-b57d-3ed7-8ebe-c07a62c7149f | -14.2373 | -51.9284 | 2026-08-31 18:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 283eaf5e-b432-3fb5-965f-ebfebca1aaf9 | -14.1456 | -52.8082 | 2026-08-31 18:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f071a4e3-3174-346d-a151-9e488460a023 | -8.9138 | -45.0232 | 2026-08-31 18:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 07c530fb-d6cc-3e32-a6fe-1dfaad1b4852 | -6.1294 | -57.6833 | 2026-08-31 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 1ee8b7c5-b93f-3ae5-8388-9795824a0b79 | -11.1807 | -55.1024 | 2026-08-31 18:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| fad6bbaa-4ecb-33f0-a967-571d45bca0db | -9.694 | -65.0958 | 2026-08-31 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 1b30cb16-cef9-3ab5-8ca5-3908920f4f93 | -6.8193 | -59.5734 | 2026-08-31 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 09be35d3-5fba-33c0-b88a-806690fb9da8 | -4.9788 | -55.8417 | 2026-08-31 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 3b2ff41e-b5e1-3707-98f3-f958d1958837 | -7.6067 | -55.2798 | 2026-08-31 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6040f77a-dfbe-353f-8439-a929e6f3680f | -3.1083 | -61.2191 | 2026-08-31 18:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 27bc0f68-6982-369d-9ccd-2970d71e7465 | -4.1699 | -60.6874 | 2026-08-31 18:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| d50d2bc1-ed56-30e6-89f9-b34b974c9044 | -3.7931 | -65.1119 | 2026-08-31 18:20:00 | GOES-19 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 7ceb4c65-0c09-3895-9520-2b40e6c8c7d5 | -10.8046 | -50.5046 | 2026-08-31 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 208b337a-2b08-3e09-9af8-85ece97e3597 | -15.8649 | -56.4841 | 2026-08-31 18:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a755eb60-4943-3cc9-aaa9-305646792aed | -8.6555 | -70.7503 | 2026-08-31 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3af2011f-b584-3545-bebb-d22347e8b633 | -6.8569 | -59.4564 | 2026-08-31 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 8221ec75-dc24-3ff7-91f4-c17bfaceae3d | -13.471 | -57.0373 | 2026-08-31 18:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 07fd120b-2359-39f3-a14b-75071b7dd8cd | -12.0925 | -44.996 | 2026-08-31 18:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 69db9e78-1d94-3d33-ae70-26a199312e2b | -8.9314 | -62.067 | 2026-08-31 18:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 2ad7c226-e3ed-3626-a94f-d7c73c01acd3 | -9.196 | -64.4568 | 2026-08-31 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 7d9a38fc-c0f0-376a-ac77-a25e576bf07b | -8.9295 | -62.3712 | 2026-08-31 18:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 1250de37-f6de-383f-be98-f372c5f666df | -5.4876 | -57.1416 | 2026-08-31 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d5c6178e-21f5-30ba-afe9-5c33185b85bc | -3.4652 | -65.0054 | 2026-08-31 18:20:00 | GOES-19 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 719a11cc-78be-3415-ad88-f3b71449b086 | -6.77 | -55.6445 | 2026-08-31 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ccf1d74e-c203-356c-bf85-b6f137e43b6b | -8.4896 | -70.6243 | 2026-08-31 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 123.3 |
| bcac34fb-1610-3f56-9494-27e1e514af88 | -7.9425 | -44.2538 | 2026-08-31 18:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 4b340398-1d14-3947-91d0-04d19374b49c | -13.4707 | -57.0574 | 2026-08-31 18:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b1909c46-9507-32ac-96c8-56a70c05af53 | -9.12 | -61.6011 | 2026-08-31 18:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 7c5bf8c3-0016-3cce-82a8-e7a18629fd1c | -15.0244 | -48.1689 | 2026-08-31 18:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 96d2d3a2-6f29-3b70-95ef-47a5db04450c | -14.6145 | -53.59 | 2026-08-31 18:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 328.7 |
| 61dc91d0-a3dd-3273-88a0-2bbc69ddcd01 | -6.137 | -53.5259 | 2026-08-31 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7011cf59-0ad8-3b9c-b088-e71ccb2a02a5 | -8.3413 | -71.0291 | 2026-08-31 18:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bd06a624-1ce8-3f3d-b153-c33012e8acda | -11.2482 | -45.1194 | 2026-08-31 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 5ac64b6f-b330-38db-9f7a-0733b11c4d58 | -9.1719 | -59.5017 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 976f519d-56c7-3e9c-bf56-7974e5a28c83 | -9.1711 | -59.618 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 485951cc-3d8d-3797-9fac-6467081e0ce2 | -6.7699 | -55.6644 | 2026-08-31 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 683295ee-1c9c-363a-831d-58152bc1dfe6 | -9.0251 | -70.6901 | 2026-08-31 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 7af3d86c-5223-3c5d-82f5-5bb03a954343 | -13.4901 | -57.0355 | 2026-08-31 18:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 4f875627-3333-38d2-a7d1-2d45611fd0cc | -4.9604 | -55.8424 | 2026-08-31 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ab2d009b-77eb-3e88-81dc-9ac782d57b9b | -10.7271 | -50.6405 | 2026-08-31 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 250.9 |


[Clique aqui para ver as próximas entradas](README184.md)
