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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5926a5e8-0b14-312e-965f-42c07c7594f5 | -19.64038 | -40.13146 | 2026-10-01 11:06:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 9cdc3aac-699f-3d97-9317-3603928d07d6 | -20.14006 | -42.17169 | 2026-10-01 11:06:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 04bb7f6e-33d1-3b0f-a08e-c5ba10d4d2db | -19.40917 | -40.45455 | 2026-10-01 11:06:00 | TERRA_M-M | MARILÂNDIA | ESPÍRITO SANTO | Brasil | 3203353 | 32 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 3fc383a1-6ff3-39e3-9475-35616be8c7b0 | -20.0012 | -41.81152 | 2026-10-01 11:06:00 | TERRA_M-M | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 41d5aaa4-ea04-3028-ab4f-841b0070b064 | -17.44032 | -44.78584 | 2026-10-01 11:06:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5dbe9365-bba4-345c-9f8f-1bd3407824f4 | -17.95199 | -40.01223 | 2026-10-01 11:06:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 04538ed9-54ad-30c9-aa6e-7af4a3a80403 | -18.73366 | -43.96319 | 2026-10-01 11:06:00 | TERRA_M-M | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3cc7d1c4-1a8d-38e3-9c8a-77209bb647e6 | -19.64172 | -40.12215 | 2026-10-01 11:06:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a255af85-c8fe-3b46-93e1-329a0f4307a4 | -11.2278 | -45.1913 | 2026-10-01 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 22bb3318-0abf-3fb2-af07-664e7c401336 | -11.4503 | -43.4091 | 2026-10-01 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 22d524f7-bf1c-30df-aaf4-b193ed8af182 | -8.3397 | -44.1658 | 2026-10-01 11:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 836bb7d3-9b1d-3305-8492-d2f61dbf3778 | -8.3208 | -44.1679 | 2026-10-01 11:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| fc35b706-62fb-3cf1-8fd1-41194a07efb6 | -8.3397 | -44.1658 | 2026-10-01 11:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 201.6 |
| d62aa570-7cea-3ce9-93c0-474c7cb7d633 | -11.2278 | -45.1913 | 2026-10-01 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 1eda81a0-76d9-3129-8206-4f00a0d5539a | -11.4503 | -43.4091 | 2026-10-01 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| fa5d3488-af52-3fe9-9792-a4f3dabeabf7 | -11.2087 | -45.1939 | 2026-10-01 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| d35da876-3f85-30c8-b2c6-88df1de0720d | -8.3211 | -44.1447 | 2026-10-01 11:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 01741f0f-fd98-30b4-80a5-9677a5a6f1fa | -11.2282 | -45.1682 | 2026-10-01 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4ea4f8b1-2c59-3324-851d-4d15f347fcd7 | -8.3397 | -44.1658 | 2026-10-01 11:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 3810a5bd-4608-3d27-8def-175fdc109e32 | -8.3208 | -44.1679 | 2026-10-01 11:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| c74507e5-2f23-32df-aaa4-2fafcc18dc79 | -11.2278 | -45.1913 | 2026-10-01 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 251.9 |
| 6043a167-8d67-3eea-822f-45f47ae949b6 | -11.4499 | -43.4329 | 2026-10-01 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 69a1e35e-c446-39dc-aa86-2ee9b8e3df0f | -8.3208 | -44.1679 | 2026-10-01 11:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b2f711ea-97b2-36a7-a202-a2c6ba6f2a0a | -8.3397 | -44.1658 | 2026-10-01 11:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 222.1 |
| a9003cbd-b146-39e2-a9d4-94def45372c2 | -11.4503 | -43.4091 | 2026-10-01 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 257.5 |
| a0aeba9d-9644-3892-ad83-c69bd214e22f | -11.4311 | -43.4121 | 2026-10-01 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 9a4ff62b-0cd1-3c3c-83b4-2eac98ce6d75 | -11.2278 | -45.1913 | 2026-10-01 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 064e1b44-6196-3258-a486-608e1f061f6f | -17.5069 | -45.4666 | 2026-10-01 11:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 131.0 |
| d4d1cf94-d2df-3c78-8d96-871d757c62d0 | -11.2282 | -45.1682 | 2026-10-01 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| dcd3f194-321e-3216-a262-3351c7365567 | -8.3397 | -44.1658 | 2026-10-01 11:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 012e6c36-bcc6-34ec-8a5e-e21681955621 | -8.0162 | -42.8917 | 2026-10-01 11:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 25ca618f-9d0f-3ea5-b738-907f25fd2d85 | -8.3211 | -44.1447 | 2026-10-01 11:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 8276c5f1-5b52-3716-95be-08089effbcbc | -11.4499 | -43.4329 | 2026-10-01 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 71ae77bb-f6bc-35c0-bdae-dc6c7f909076 | -9.8064 | -44.8265 | 2026-10-01 11:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 2d51747e-758c-3373-8170-a895da2a2968 | -8.3208 | -44.1679 | 2026-10-01 11:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 46b076be-5aff-3678-8ad8-5df1bda37f38 | -11.2278 | -45.1913 | 2026-10-01 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 5aaeecdd-437e-323e-a807-9186d3aa9eb9 | -11.4503 | -43.4091 | 2026-10-01 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| a7a050b0-f912-38d4-ad41-2a3d3c57d4c4 | -11.4311 | -43.4121 | 2026-10-01 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| b7199b9c-8cac-3225-8a45-a15a4a277067 | -11.4499 | -43.4329 | 2026-10-01 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| cfb90565-7c86-363f-bcc3-2155269c2734 | -12.1857 | -48.4345 | 2026-10-01 12:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 0d08f3de-4690-38d2-8667-4afd06622df3 | -14.3574 | -44.7569 | 2026-10-01 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 1e514755-97bb-3d6c-9bdc-09a25908bdb0 | -14.3764 | -44.7769 | 2026-10-01 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 8e6bc823-f718-35dc-bd34-2d6e99d32435 | -11.4311 | -43.4121 | 2026-10-01 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| ec806eff-42f0-31f2-af25-b018a790461f | -9.224 | -45.8301 | 2026-10-01 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| d0aae658-1ba0-3a19-8fdd-6f00af43ffe7 | -17.5069 | -45.4666 | 2026-10-01 12:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 1397d1ad-0d04-35b4-986e-57d2b0ee290a | -8.3211 | -44.1447 | 2026-10-01 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| bbf80301-9b29-3c3e-a4f1-9fe143ae3428 | -11.4495 | -43.4566 | 2026-10-01 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 4be429a5-6b9f-3748-9021-f3f573c78f79 | -11.2278 | -45.1913 | 2026-10-01 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| ad9ae58f-dcda-3979-b645-c86bbf755162 | -14.377 | -44.7534 | 2026-10-01 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 41de5ad5-0bf2-3762-90e6-54e8ed9624e7 | -11.4503 | -43.4091 | 2026-10-01 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| b542968c-052d-30d0-8bda-c66728bf9048 | -8.0162 | -42.8917 | 2026-10-01 12:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 179.5 |
| eaa89c5c-b897-3cd1-9b73-4f126184e41a | -8.3397 | -44.1658 | 2026-10-01 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| b8d6a36e-bb8f-3ea2-8183-fd1838d67b1d | -8.3208 | -44.1679 | 2026-10-01 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| eb1522ef-b4ab-3c45-bf85-c860b3d66c66 | -14.3965 | -44.7498 | 2026-10-01 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b10aabb6-7efb-396e-bcaa-ece4438c2da7 | -9.9026 | -50.17 | 2026-10-01 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 59cda734-b240-3c89-8e3a-89de9ff29606 | -11.4119 | -43.415 | 2026-10-01 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 1d4123e3-898e-3b67-98d3-356ee3287e85 | -8.2099 | -45.4848 | 2026-10-01 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| dbed3011-6ed3-32f1-b0ed-2c9c4b5376ef | -8.0162 | -42.8917 | 2026-10-01 12:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 5a31b1d1-5935-3e85-a8da-95627d9f7429 | -8.3397 | -44.1658 | 2026-10-01 12:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 325.1 |
| ea0a6b31-74dd-3259-9396-af7a1c67553d | -11.4123 | -43.3913 | 2026-10-01 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| a33bb4f1-91ce-3218-8670-5e2bf936de2f | -8.3211 | -44.1447 | 2026-10-01 12:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 8961529c-9714-3b25-b25f-1ce2e40e6b13 | -12.4535 | -44.1937 | 2026-10-01 12:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 6a5be3fd-ecc3-36fd-89a8-333bcf3ebece | -14.377 | -44.7534 | 2026-10-01 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 2b8152ea-bd8b-39a8-adab-df2e708af4f4 | -14.3574 | -44.7569 | 2026-10-01 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 6f92cd98-e983-305f-b842-a6b2963a28d0 | -11.4499 | -43.4329 | 2026-10-01 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| cba48eb2-8f57-3302-afeb-217d17d1fd8b | -11.4311 | -43.4121 | 2026-10-01 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 3ae7fc61-6c76-3647-b3ba-c1909fbe01a0 | -8.3208 | -44.1679 | 2026-10-01 12:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 48774d2f-afe8-3d40-b82b-29f4b961ccd2 | -10.5388 | -45.3759 | 2026-10-01 12:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 60f7bb39-51dd-3b8e-8326-2606056e25af | -11.4503 | -43.4091 | 2026-10-01 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 3668999b-a6b4-36de-b749-7a2743991b14 | -12.1857 | -48.4345 | 2026-10-01 12:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| bd37d6a9-5d48-3960-9151-da1692f6abff | -8.3074 | -46.7549 | 2026-10-01 12:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8e97c550-b477-33f4-947f-e9ee798ed372 | -11.2278 | -45.1913 | 2026-10-01 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| fa9bd07c-21c5-343d-9b0a-3c6012cb804a | -9.9026 | -50.17 | 2026-10-01 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| bdc51751-2b89-39d9-8f2a-fdef2cf6ca3e | -17.5069 | -45.4666 | 2026-10-01 12:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 110.6 |
| bb0c0142-654d-3368-941b-34fa49a62b40 | -17.5069 | -45.4666 | 2026-10-01 12:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 164.7 |
| c17f8717-dd09-3daf-9354-aef6bb5ff047 | -8.3208 | -44.1679 | 2026-10-01 12:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 170.2 |
| c20afa72-21a6-3c2a-9349-5b5e8354b27a | -12.4535 | -44.1937 | 2026-10-01 12:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 9ef4bcaf-6d9d-3784-817a-ba3044496168 | -12.4539 | -44.1702 | 2026-10-01 12:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| ebe9973c-2fa0-3f46-acab-5b8540803b54 | -8.0162 | -42.8917 | 2026-10-01 12:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 13336951-72ea-3868-a4b2-6f43f30b4535 | -8.3397 | -44.1658 | 2026-10-01 12:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 240.9 |
| bc331679-d710-3be9-93e5-3628f26f671f | -9.2243 | -45.8074 | 2026-10-01 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 3bf85e39-e96c-3739-954a-a59fdd8bcd93 | -9.9026 | -50.17 | 2026-10-01 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| beb99f14-2dd1-33e4-847a-164b5594b6e3 | -8.3074 | -46.7549 | 2026-10-01 12:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5e1f9861-1557-323a-92a3-d43405c520e9 | -8.2099 | -45.4848 | 2026-10-01 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 828e1848-e643-3a35-a659-d797cb1afcbc | -11.2278 | -45.1913 | 2026-10-01 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 63620969-1bd8-3443-bcdb-301a23b16062 | -9.224 | -45.8301 | 2026-10-01 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| f5ce4844-542c-3a13-a153-b8d46c09167e | -14.377 | -44.7534 | 2026-10-01 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 8a04188d-126a-39c2-aa16-40e726eaa1de | -11.6203 | -43.5485 | 2026-10-01 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 15f18857-974a-3dda-b065-81c9967dfb64 | -14.3574 | -44.7569 | 2026-10-01 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 447c38ac-0e4b-3fdb-8dab-2f8b25e608f8 | -8.3211 | -44.1447 | 2026-10-01 12:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 142.1 |
| f47b068f-69e5-31cb-8499-3a15c9c7fc86 | -12.1857 | -48.4345 | 2026-10-01 12:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8efcdb2e-00f1-3dd5-9f60-e28b4f493d6c | -8.2097 | -45.5075 | 2026-10-01 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 72c7283c-b6a4-3950-952d-fd135b48e6d3 | -9.224 | -45.8301 | 2026-10-01 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| ba518dd4-51a4-39fa-a0e8-1fbb8447a739 | -8.1215 | -43.5148 | 2026-10-01 12:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 3b343572-e63d-3aa2-9a49-6c0c295a1cbb | -8.0166 | -42.8681 | 2026-10-01 12:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 9efa6df3-c11e-35c1-a723-f229a3501d04 | -8.3074 | -46.7549 | 2026-10-01 12:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 11e8e990-2570-3bf9-9620-c67f253ffe1c | -9.88 | -44.9783 | 2026-10-01 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 1af477bb-78b0-30b9-94db-bee8fb84c370 | -14.377 | -44.7534 | 2026-10-01 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 7d5ef40f-8b89-306f-81da-4e40d84557cb | -8.0162 | -42.8917 | 2026-10-01 12:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 267.3 |
| 06e622a3-ed83-321c-b92a-3b849674db09 | -8.1212 | -43.5382 | 2026-10-01 12:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |


[Clique aqui para ver as próximas entradas](README95.md)
