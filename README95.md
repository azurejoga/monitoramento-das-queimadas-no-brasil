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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54568908-00ca-35fe-834c-71acf24a47cc | -11.2278 | -45.1913 | 2026-10-01 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 50dc9471-554f-3496-8fec-8c685c22c551 | -8.3211 | -44.1447 | 2026-10-01 12:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| b15d7f76-ad40-321d-8fbc-cb2b8d10e3c8 | -9.9026 | -50.17 | 2026-10-01 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| fea3f922-9dd5-34d6-9c73-0ea5128c8e89 | -8.1401 | -43.5361 | 2026-10-01 12:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 72cbe442-134b-3297-8616-1df2578a98cd | -9.8064 | -44.8265 | 2026-10-01 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e57c20d3-57bf-34a5-8776-e52dfd34ba16 | -8.2099 | -45.4848 | 2026-10-01 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d4feb561-9ccf-384c-8f7e-78902653bab7 | -12.1857 | -48.4345 | 2026-10-01 12:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1a1837e3-9698-3e27-98a7-7d4d55751685 | -11.6203 | -43.5485 | 2026-10-01 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 5f56f91c-d978-3a5e-ba78-3579cfaf7faa | -8.3208 | -44.1679 | 2026-10-01 12:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 156.6 |
| c552bdc5-1aa4-36ff-868b-44c0428d5441 | -11.2087 | -45.1939 | 2026-10-01 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 08eb03ad-8cb9-3afb-bd4a-48be9600e12e | -11.2095 | -45.1478 | 2026-10-01 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| eaca10a4-e64e-3c7a-96fd-34ed9d2e78d9 | -8.3397 | -44.1658 | 2026-10-01 12:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 158.4 |
| f5321f57-eed3-3fab-b05a-c082f7c5faad | -14.3574 | -44.7569 | 2026-10-01 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| e7230550-eaa5-38a1-897a-4c1f7cb77e82 | -17.5069 | -45.4666 | 2026-10-01 12:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 301.3 |
| 14cef9cf-06b0-34c3-bd21-3cb443faffc4 | -10.6688 | -50.7529 | 2026-10-01 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2c64e78b-1447-34e3-b7f7-89c4cad668cb | -8.1908 | -45.5093 | 2026-10-01 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2037c78f-1ed0-3a79-ba8f-8179a532a755 | -7.0798 | -42.3255 | 2026-10-01 12:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 00f51993-a74d-315d-8168-7e59acc2b881 | -9.861 | -44.9807 | 2026-10-01 12:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2b4c1ad8-3049-3daa-930f-fe112185e774 | 2.16169 | -55.82461 | 2026-10-01 12:38:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 36a557b8-9c9c-32d3-8122-4385103dee76 | 2.15974 | -55.81152 | 2026-10-01 12:38:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 967b5c55-d6b4-334c-b4b0-d520abfedfc3 | -14.3384 | -44.7369 | 2026-10-01 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 9547df39-7e1e-3ef9-b116-b46b82139382 | -8.0166 | -42.8681 | 2026-10-01 12:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 2f52bf54-6513-38e9-a0b6-c7d36e3883b1 | -9.2054 | -45.8095 | 2026-10-01 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 8f28554f-4d2d-3444-b1c0-9ba7ff0ea2bf | -8.3263 | -46.7531 | 2026-10-01 12:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e68dde24-34cc-3a5f-9816-9292b897726a | -8.3397 | -44.1658 | 2026-10-01 12:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 153.4 |
| fe2d67e9-ee3a-3efa-ae11-434116588549 | -8.1215 | -43.5148 | 2026-10-01 12:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 489e6890-8d20-3f9f-916d-b4dc2039a947 | -7.6456 | -55.057 | 2026-10-01 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 334bed4a-474f-3a82-ad66-8880371ba882 | -12.1857 | -48.4345 | 2026-10-01 12:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 310b8837-1e99-3f8f-a0eb-4c6265d3011d | -9.9026 | -50.17 | 2026-10-01 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 30b27c7e-c5d0-3518-b0e0-84083598c3a4 | -8.1401 | -43.5361 | 2026-10-01 12:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 30fdd624-3fb6-3623-9973-5ea368dd4321 | -11.6203 | -43.5485 | 2026-10-01 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| d8a4ad47-a951-35ad-a1d8-d74c0cfb97c5 | -14.3574 | -44.7569 | 2026-10-01 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 7609ee0b-58cc-327a-9ab6-fcc83b4b4efe | -8.3208 | -44.1679 | 2026-10-01 12:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 143.9 |
| d8533ddc-b5c3-3671-92ce-1279644fce99 | -8.3211 | -44.1447 | 2026-10-01 12:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 5a6905c5-9f01-3de9-bc73-1be345f1ed16 | -7.6271 | -55.0581 | 2026-10-01 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 0323100e-eede-3328-83f2-c23b452d8f17 | -17.5069 | -45.4666 | 2026-10-01 12:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 277a8316-e2c0-32f8-81a3-d84648a7af4c | -8.2099 | -45.4848 | 2026-10-01 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 6952fb73-899d-35fb-8466-7f1dfa758e72 | -11.2278 | -45.1913 | 2026-10-01 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.8 |
| 5f174aee-de7c-3457-8e10-ef57cde63fd8 | -9.9973 | -50.1393 | 2026-10-01 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 477b7c29-14d3-3749-a1b8-7b1b32b86311 | -7.0798 | -42.3255 | 2026-10-01 12:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 37ddae3b-d78f-3dee-9398-56d52336d2da | -8.6259 | -45.3737 | 2026-10-01 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 77f841dd-9802-397b-87fc-cb8fab2c162b | -9.224 | -45.8301 | 2026-10-01 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ccca9c69-a760-31d7-af43-f7a824bfe947 | -15.2436 | -46.1303 | 2026-10-01 12:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| bfbbece0-af46-3bb5-8f78-2a5f7d0086ec | -8.1212 | -43.5382 | 2026-10-01 12:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 33ad2ede-932d-3e94-b746-4337d5453b9b | -14.9215 | -41.5086 | 2026-10-01 12:40:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 141.4 |
| b6d59cb1-7e1d-3628-bdfc-cc739c7e6d01 | -13.3835 | -44.0132 | 2026-10-01 12:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 59ce501a-98ea-30f3-a206-00503a21a05f | -8.3074 | -46.7549 | 2026-10-01 12:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| c46b2828-19ba-3d2f-b43a-ce72d52e0393 | -14.377 | -44.7534 | 2026-10-01 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7eec0f65-3553-3211-8b89-8df8645ba54f | -10.6686 | -50.7742 | 2026-10-01 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 56e910d3-9971-3bb0-b10f-4cd2d6397dec | -9.9784 | -50.1412 | 2026-10-01 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5b8497c8-1e81-3943-b46d-654879a42199 | -10.6688 | -50.7529 | 2026-10-01 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d03a2182-13a1-313d-8ed9-89de10d13e3c | -1.61622 | -55.13186 | 2026-10-01 12:40:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 58468548-40f0-3ac0-b69e-ef8b1e69941b | -3.68588 | -60.54194 | 2026-10-01 12:40:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 100759fb-8442-369d-b6ba-44cf3ddca128 | -3.70706 | -59.67982 | 2026-10-01 12:40:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0105df8d-6be7-3f3a-8395-32e9613b212a | -1.64265 | -55.11792 | 2026-10-01 12:40:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 08af5e49-ad1e-3bd6-ab78-67e59ad0c4f9 | -5.12411 | -56.01031 | 2026-10-01 12:40:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| d2063b04-d037-389e-ad0c-7814b26123fd | -4.08558 | -54.87069 | 2026-10-01 12:40:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| e55a11bd-0244-3031-a896-8ee945911677 | -1.6113 | -55.12456 | 2026-10-01 12:40:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7c369b58-5a90-3dfa-9808-33906d7ea3e7 | -1.60883 | -55.14176 | 2026-10-01 12:40:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| bfb195d5-6a20-3822-a1ef-32255fc98e93 | -2.48706 | -58.01569 | 2026-10-01 12:40:00 | TERRA_M-T | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 21f790db-67ee-3833-8803-cfa6795737ab | -1.64027 | -55.13519 | 2026-10-01 12:40:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6ed62e0c-ae3a-3b7d-9d56-638c3c40f6bf | -3.59109 | -58.54089 | 2026-10-01 12:40:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3030561a-7f87-3c9f-a3b4-6ae09d2512b7 | -3.59245 | -61.7164 | 2026-10-01 12:40:00 | TERRA_M-T | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1a6b24fe-fe9b-300f-877a-a52f1d8ba5f0 | -4.39229 | -54.82901 | 2026-10-01 12:40:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 2ce9bd87-d593-3fed-bbb5-4138b85c48cf | -9.09327 | -61.18252 | 2026-10-01 12:42:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 0e2f4c30-9071-3035-8fb9-6191df11c66d | -6.74725 | -59.17163 | 2026-10-01 12:42:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cde1b821-d538-305a-88f7-b35dc21b5b35 | -5.86724 | -57.75348 | 2026-10-01 12:42:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ac6836a1-666b-3959-96b7-8714aff38e45 | -10.546 | -57.76334 | 2026-10-01 12:42:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a449cbed-a890-3157-90e8-9273d2486867 | -9.07318 | -60.99452 | 2026-10-01 12:42:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7c667a3f-a1ec-3a74-b35d-dd4a77ad39b7 | -5.86742 | -53.48748 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e588570d-1acf-3aa6-8d64-0457e7722b6e | -5.85283 | -53.4841 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 3f2b2d6c-6db5-34d7-9a1e-16536e467813 | -8.65242 | -62.65842 | 2026-10-01 12:42:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d73ec9ab-d062-3c68-b91d-1a54d22f828b | -6.66717 | -58.86945 | 2026-10-01 12:42:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 164.1 |
| b5d1d517-0399-3761-8a2e-4c39bd685b87 | -6.84743 | -59.3578 | 2026-10-01 12:42:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 548cf7dc-1606-3fb8-bea6-fafa1d172a4d | -10.53338 | -57.7711 | 2026-10-01 12:42:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 21d118d3-5ea4-3316-b933-f7be69e54818 | -5.75321 | -55.72933 | 2026-10-01 12:42:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 58b6e982-b9a5-3c3e-8b30-ba3cca820c47 | -5.86723 | -53.48097 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6ef76358-152f-319b-a426-4fa94bf984bc | -8.15172 | -54.80801 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 6a568ad6-fef4-313d-8949-57d0a3781187 | -10.2654 | -53.58447 | 2026-10-01 12:42:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| f5acde56-f0bd-33d7-bd47-9dc7e59a3fb7 | -9.58258 | -54.6271 | 2026-10-01 12:42:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 8e0eb5a2-daf1-3f2c-a5d8-acb6e088adb5 | -10.51511 | -53.49944 | 2026-10-01 12:42:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 729885d5-dc65-3d70-93ee-83485efdcda9 | -9.17277 | -61.40406 | 2026-10-01 12:42:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 41ea2032-39d4-3769-af74-eb0a49092371 | -7.87005 | -54.70148 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 4afffcd6-29d3-3000-bdcb-81f4525bf249 | -6.93051 | -59.27974 | 2026-10-01 12:42:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c8d9c749-077c-3ff7-81df-ad7dee0f5ce9 | -10.5241 | -57.75458 | 2026-10-01 12:42:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 1ff21bef-ff3e-3e07-ac34-bb6b6dce4ff7 | -5.74746 | -55.74043 | 2026-10-01 12:42:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| cbbfc993-6bac-361f-9a0d-de09118c352d | -12.11944 | -61.14886 | 2026-10-01 12:42:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 58bd0bd5-7622-384c-87a3-b3bd9cc51078 | -9.16387 | -61.40284 | 2026-10-01 12:42:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e56bf88f-8f65-321a-a652-8e6d9e5611ad | -9.74576 | -54.01578 | 2026-10-01 12:42:00 | TERRA_M-T | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 38b9086a-4219-33fa-9388-affe5f500bac | -9.93235 | -60.71484 | 2026-10-01 12:42:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c61b435f-436f-3d1c-bd30-85d24a3b3bb0 | -6.65589 | -58.87914 | 2026-10-01 12:42:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 189.5 |
| a6629957-ff60-3af4-900e-0377454ecc48 | -5.84922 | -53.50386 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 67fa1352-322b-36b6-824c-61592d173d9d | -8.6436 | -62.65716 | 2026-10-01 12:42:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cb7b6474-d81f-3b0a-9d59-8f41e8267dcd | -7.4939 | -55.00204 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 67b8833e-dff5-390f-ae89-d0fd4356f151 | -11.12564 | -53.99493 | 2026-10-01 12:42:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 09c96464-e715-33bb-8e3b-05ab2ac9e986 | -6.66567 | -58.88044 | 2026-10-01 12:42:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| b0d8517e-c1d1-392e-b80d-44631c01d47f | -7.73864 | -54.79812 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 22c89ce2-3f87-39fa-b67c-eddac4d1b40b | -5.91199 | -53.49127 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 621e6894-fd91-30da-8829-4378f15b3825 | -6.9257 | -59.2833 | 2026-10-01 12:42:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0861fc7f-da60-37d7-93a7-d3b534f4ce9e | -7.64266 | -55.05492 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |


[Clique aqui para ver as próximas entradas](README96.md)
