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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47340492-2579-3fd5-aab8-6988691ccb18 | -17.9203 | -41.47536 | 2024-10-24 03:45:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5ba2f1b5-d6fd-3c2e-b317-004457073c94 | -17.47162 | -42.45761 | 2024-10-24 03:45:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b93fe27-99d3-3ac0-90c6-6e35c4b0d673 | -17.20549 | -45.33084 | 2024-10-24 03:45:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d096bcf-a887-3d48-af20-60c41e976752 | -17.20444 | -45.33613 | 2024-10-24 03:45:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a3b4fc0-6ffe-3eba-8a74-cb1f8ba6607c | -17.20311 | -45.33416 | 2024-10-24 03:45:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 030978c5-855d-3338-ab86-b61c71f38200 | -17.19977 | -45.33511 | 2024-10-24 03:45:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5efc89d4-2740-372a-a62b-972da9959c76 | -17.19845 | -45.33315 | 2024-10-24 03:45:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91bff3fb-ab0b-3731-a287-fd9f8c2f281e | -16.81722 | -43.3261 | 2024-10-24 03:45:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9beee4c1-2b84-37ea-8f81-fd27941f3105 | -16.74528 | -40.78381 | 2024-10-24 03:45:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c082213a-c773-3924-8b68-66a371191aa1 | -16.63253 | -40.84849 | 2024-10-24 03:45:00 | NOAA-20 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a9b7f7b9-14a2-3cbf-a5ef-10b373c1dbf4 | -16.54102 | -41.63162 | 2024-10-24 03:45:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0b5947b8-8bab-37a6-8390-d1522099b72b | -16.34625 | -43.69678 | 2024-10-24 03:45:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 622284a0-a599-3e9e-a0b4-4ef67100ba18 | -16.33891 | -42.20301 | 2024-10-24 03:45:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b507ccb3-9a4b-34aa-aeaf-4871d4b83173 | -16.338 | -42.20813 | 2024-10-24 03:45:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 91110ba2-8107-3d9c-9cb6-386e970302a9 | -16.30701 | -42.04546 | 2024-10-24 03:45:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ee60a15b-a8ce-3721-aab2-1cddb3697ba2 | -16.22213 | -41.93441 | 2024-10-24 03:45:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f3331a3b-548c-39b7-89e0-56c0f2f6ee3c | -16.01076 | -43.39456 | 2024-10-24 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 43a97272-a8a4-3896-a8ad-978260ec75d3 | -16.01001 | -43.39864 | 2024-10-24 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 26dc427c-5746-3bd3-b855-fbec2ab73232 | -16.00655 | -43.39366 | 2024-10-24 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca47d20b-0a31-3662-939c-da130c9e36d7 | -16.0058 | -43.39775 | 2024-10-24 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8e8cf01-57f4-3005-b79a-d4d7f88c6292 | -15.89093 | -43.03287 | 2024-10-24 03:45:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cad43dcf-3109-3708-86d1-18d922786cc7 | -15.86397 | -43.5285 | 2024-10-24 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f6e93dd-a569-3e67-89a5-84f8afe55820 | -15.85971 | -43.52763 | 2024-10-24 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc05d724-8aed-3968-a18c-fbe133b6916d | -15.84313 | -43.40393 | 2024-10-24 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cee01517-7fe3-3928-a5ee-b3c16e0cc9f4 | -15.77438 | -41.2814 | 2024-10-24 03:45:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d097610d-f3c0-30ea-88b0-4edfd59430ce | -15.50045 | -43.80169 | 2024-10-24 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea36b52f-6546-373f-b582-3194c975f101 | -15.49857 | -42.86737 | 2024-10-24 03:45:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9c85a73-3828-3865-8c56-65580f30465b | -15.49444 | -42.86667 | 2024-10-24 03:45:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1edf0a7-f127-3aa8-ad12-d00a8383c2a2 | -15.41456 | -43.08312 | 2024-10-24 03:45:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 32cfe0d0-7aaf-33ce-adca-04262fb80e62 | -15.04851 | -46.20412 | 2024-10-24 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e1d7255-949d-347a-a4c4-9275842b8085 | -15.04787 | -46.20736 | 2024-10-24 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f9215dc-50ca-306e-9625-efc4c0b4f52a | -15.04274 | -46.20624 | 2024-10-24 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf335ce1-f26e-3173-985c-8a4441b63b59 | -14.94601 | -43.16997 | 2024-10-24 03:45:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9902ce73-742d-36c7-a86f-a514664d22a1 | -14.92224 | -45.11679 | 2024-10-24 03:45:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 76bd41c5-21c9-32c0-a902-5722a3157f8c | -14.92122 | -45.12214 | 2024-10-24 03:45:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 593933dd-5a7d-33ac-898f-57f3019368ff | -14.91641 | -45.12114 | 2024-10-24 03:45:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 06bf5da2-2c04-3d29-8996-cfebd3340725 | -14.91537 | -45.1266 | 2024-10-24 03:45:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a23f6f20-0b3b-364a-8b6c-fea6ce78b105 | -14.91205 | -42.80546 | 2024-10-24 03:45:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d316c21e-1c2b-3981-9480-be39699fb38b | -14.91056 | -45.12561 | 2024-10-24 03:45:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b2646f1-2057-31ec-a269-e68bf430c552 | -14.90951 | -45.13108 | 2024-10-24 03:45:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62a6277a-fe56-35a2-b16b-0c842517ed12 | -14.71607 | -44.18262 | 2024-10-24 03:45:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad484a54-efb4-3b63-9a5d-4d7e9e3f0666 | -14.5543 | -49.73071 | 2024-10-24 03:45:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc15c2f1-3999-3dff-8f82-1cea1af1a5f5 | -14.4815 | -45.52843 | 2024-10-24 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62aa1b26-ffd7-3c71-8012-bcaa0516129c | -14.47537 | -45.53332 | 2024-10-24 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a4011a6-2ed2-301a-bc29-a5ab1341b936 | -14.47479 | -45.53628 | 2024-10-24 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d1bac1c-8f88-3281-bca3-70bc0d7aecc9 | -14.47422 | -45.53923 | 2024-10-24 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9997c35-8eb4-3cb0-b1e9-86ba992efb5b | -14.47364 | -45.54218 | 2024-10-24 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aab1602c-e5a4-3cdd-bc26-5de00bd470c6 | -13.93584 | -48.15591 | 2024-10-24 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7c3d3c7-39a1-328e-a50d-fe34ae4d32a4 | -13.93507 | -48.15961 | 2024-10-24 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdeadb18-2b2d-3781-90c9-49b9d5012ca9 | -14.26511 | -51.13605 | 2024-10-24 03:45:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8dd3ede-85b2-3e9c-be30-91d53551d415 | -14.2613 | -51.13243 | 2024-10-24 03:45:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e26572f9-332a-3980-a51d-b5bd2b0583ab | -14.25978 | -51.13947 | 2024-10-24 03:45:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 232b47c0-25c2-36b3-a39c-c36e01141c72 | -14.25965 | -51.12765 | 2024-10-24 03:45:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ceb87a2-da14-3a57-96ce-145d432a283c | -14.25806 | -51.13475 | 2024-10-24 03:45:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6b9221e-eb48-3d72-a3ba-3e633d7e42bd | -1.5878 | -53.3089 | 2024-10-24 03:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| c6208616-d0e8-340e-82c4-d11b7dd631cf | -2.9763 | -50.4193 | 2024-10-24 03:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 1788120f-909a-3a1c-b399-f6a543bdccad | -3.1101 | -54.1661 | 2024-10-24 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2e9ae7af-6ab7-30bf-8436-f5eb50f63add | -3.1606 | -50.4766 | 2024-10-24 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| a0c1d705-0217-348c-be50-e986e9361afb | -3.1607 | -50.4556 | 2024-10-24 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 228890ab-4795-3724-af07-a0c985f830d5 | -3.9394 | -46.445 | 2024-10-24 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| a2bbf3e8-551b-3d12-bd29-3124302a5da0 | -3.9396 | -46.4229 | 2024-10-24 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 531bbb17-c7bc-3eaf-9f46-a97848f2b1e9 | -16.94 | -57.5268 | 2024-10-24 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| e14a78ee-86e9-3ec9-9aa9-4b2f48d2aff0 | -16.9596 | -57.5245 | 2024-10-24 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 3089e1b7-a900-3e47-9980-70f5959a782f | -16.9792 | -57.5223 | 2024-10-24 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 0cbad5fa-8396-3e6a-8637-6fdccf54c15a | -18.0837 | -57.3076 | 2024-10-24 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| a186b167-739a-3e54-baf1-3b65ff101d8c | -19.5071 | -56.6619 | 2024-10-24 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 3762c816-76c2-33d0-8e4e-464a74131dc5 | -19.5075 | -56.6409 | 2024-10-24 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| d61c4518-a9be-3dc2-9869-87b332b11e1c | -19.5465 | -56.6983 | 2024-10-24 03:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 1f8f8264-31e6-3663-8ae7-f123e06900d2 | -19.5469 | -56.6773 | 2024-10-24 03:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 147.0 |
| 15595e3b-0581-37a8-a422-706c6d6edb67 | -19.5473 | -56.6563 | 2024-10-24 03:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 47e249e9-b7c4-32ec-94bc-32bdd067f7a4 | -19.5666 | -56.6954 | 2024-10-24 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 379283ba-7616-31da-af3d-6ae12ab9f82d | -19.5669 | -56.6744 | 2024-10-24 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.7 |
| aa7b9a71-3af5-34d8-a155-6df44906d30b | -19.5681 | -56.6114 | 2024-10-24 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.2 |
| c7042cf3-b893-350a-af7c-7884e93fd3fe | -19.6438 | -56.8521 | 2024-10-24 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 2c16a259-22cc-34f7-9ff4-a52c4edb9a1a | -19.6442 | -56.8311 | 2024-10-24 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| cc7a4282-eb1b-38f6-9dc6-195050f4413f | -1.5878 | -53.3089 | 2024-10-24 03:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 893f7387-8b8a-33dc-a70e-89b03825872d | -2.9763 | -50.4193 | 2024-10-24 03:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 038c1555-7b12-32c5-90f5-8f24122feef0 | -3.1606 | -50.4766 | 2024-10-24 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f16a7607-586d-3ed9-acea-84852eb67d87 | -3.1607 | -50.4556 | 2024-10-24 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f61a3e64-f472-3602-a5b1-cc58cc0c3b6a | -3.9394 | -46.445 | 2024-10-24 03:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.6 |
| a4c7fef6-c52f-3319-9144-2710f4f16091 | -3.9396 | -46.4229 | 2024-10-24 03:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 106.9 |
| d2281974-bd2b-3ec5-8c98-5bba82429266 | -16.94 | -57.5268 | 2024-10-24 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 51cd74f3-11be-3d21-8ae8-5c033e6a3dc3 | -16.9596 | -57.5245 | 2024-10-24 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 4b2cdd56-3771-3a3e-86ef-fb2ad268bd2d | -16.9792 | -57.5223 | 2024-10-24 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| f5f4c282-8305-3d73-8698-c6b81cd8a597 | -18.0837 | -57.3076 | 2024-10-24 03:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| bb4e2bac-e939-3e7d-a43d-b5dd16458ee0 | -19.5681 | -56.6114 | 2024-10-24 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 27b55aa8-09af-34c6-9f80-db34945b675f | -19.6438 | -56.8521 | 2024-10-24 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 23084cb0-2932-32fc-a9d7-5e73f6f66a1e | -19.7262 | -56.7358 | 2024-10-24 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 114be1cc-1817-372e-b24e-0c8ec722c460 | -1.5878 | -53.3089 | 2024-10-24 04:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| e80dd255-461a-34c1-a2b5-e362d6ccaceb | -2.9578 | -50.4198 | 2024-10-24 04:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 822382cc-5725-3cf6-9492-34ca9ec99026 | -3.1607 | -50.4556 | 2024-10-24 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 739ad641-2f89-37a5-ad27-a774ebff239d | -3.9396 | -46.4229 | 2024-10-24 04:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |
| cc03b2c4-bebf-3fea-bca0-dafd6b3b365a | -3.9581 | -46.422 | 2024-10-24 04:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 52bd0fc0-77b9-3aaf-8dc5-e5d9902e721f | -16.94 | -57.5268 | 2024-10-24 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| b515d9de-682b-327b-9dae-6d73acb3592f | -16.9596 | -57.5245 | 2024-10-24 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 93a677a2-9f03-3b52-9602-d8f52688c7c6 | -16.9792 | -57.5223 | 2024-10-24 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 89635e74-6e51-3da4-b823-deae588426b6 | -17.2383 | -57.2462 | 2024-10-24 04:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 7d35892e-e715-33ec-a276-e09f05e5da71 | -17.2579 | -57.2439 | 2024-10-24 04:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 18f4c88e-843d-3b9a-93d2-0216df4a1ecb | -17.7834 | -57.5708 | 2024-10-24 04:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| f43ac9f6-7246-32c2-bd9f-f3e7a0909468 | -19.5681 | -56.6114 | 2024-10-24 04:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |


[Clique aqui para ver as próximas entradas](README25.md)
