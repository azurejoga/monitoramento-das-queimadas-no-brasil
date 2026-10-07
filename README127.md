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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f24f889-4ea8-3b5e-826f-a5f8191c7d80 | -11.62818 | -43.63049 | 2026-10-07 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ec261173-6d3e-3c03-8402-3bc54095769f | -8.71149 | -45.18934 | 2026-10-07 11:42:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 779ce2e2-2c48-318d-80eb-6f8ce86e949f | -11.79225 | -46.70656 | 2026-10-07 11:42:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 6ea265d1-392d-37a6-88b1-123fcc2f8489 | -12.17756 | -44.73189 | 2026-10-07 11:42:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 13fd635f-48f6-3b57-8c5e-1a857b54536d | -9.27261 | -50.65963 | 2026-10-07 11:42:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3e1815a6-56a4-3805-894d-f0f4d3268b91 | -9.90799 | -44.80206 | 2026-10-07 11:42:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 76dbb6aa-328a-3507-852c-98e086a24843 | -18.32104 | -52.01728 | 2026-10-07 11:45:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f8c80114-b3d9-3e7d-b9f7-cabb8c4e640b | -17.51226 | -45.45791 | 2026-10-07 11:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f8c5fee3-b92c-37a4-8ec9-423036a5dc37 | -17.5224 | -45.45933 | 2026-10-07 11:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3adcba53-aa68-306e-8126-0f8fbec65bd8 | -16.98019 | -45.47427 | 2026-10-07 11:45:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 47.8 |
| b7510675-0cd5-3f70-ac9e-3a6a58f91ea9 | -16.71388 | -43.7293 | 2026-10-07 11:45:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3a06dc86-60ed-37cf-a349-9f8c1e8e090d | -17.11881 | -41.34861 | 2026-10-07 11:45:00 | TERRA_M-M | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| e4401ee5-3771-3e4d-8b26-87d4dc9e689f | -16.86253 | -41.59288 | 2026-10-07 11:45:00 | TERRA_M-M | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.5 |
| 052dc5e5-f8b2-38ee-a5eb-3f229aab916c | -16.98174 | -45.4621 | 2026-10-07 11:45:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 905008f4-d576-3e36-a2d0-1458b5276b32 | -17.52087 | -45.47158 | 2026-10-07 11:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| c73c11e8-bb67-303d-9f37-b450e24444f3 | -17.93038 | -45.21265 | 2026-10-07 11:45:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 47a99f2d-2b2f-3586-8a9f-7a9a2dd66e2b | -17.10502 | -41.34614 | 2026-10-07 11:45:00 | TERRA_M-M | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| f35a6538-b65f-381c-869b-6555b7726f8e | -17.50919 | -45.48255 | 2026-10-07 11:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8f01e97b-e6b5-350d-a7b6-fd87ef2e59f4 | -17.51072 | -45.4703 | 2026-10-07 11:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 87a54410-3cfe-35df-adbb-792ab4438469 | -17.11289 | -41.34228 | 2026-10-07 11:45:00 | TERRA_M-M | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| d237f52c-aee7-39ea-a22a-b94164144f74 | -30.44375 | -52.68891 | 2026-10-07 11:47:00 | TERRA_M-M | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 26.5 |
| 811f5d06-f0d6-3bd1-a3b0-449bca67b2b7 | -11.7751 | -46.7082 | 2026-10-07 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| c23047e4-cde0-30f3-b852-20dcc845aaa3 | -11.7947 | -46.683 | 2026-10-07 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 5b8d1abb-bba1-3128-8a65-c15044176f8f | -11.7943 | -46.7056 | 2026-10-07 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 41ed7afc-30a9-3a5d-bfcb-89d2824edc99 | -11.7755 | -46.6856 | 2026-10-07 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| baa5acf5-303d-3f0e-9c31-6499e0a3c560 | -11.3745 | -46.6948 | 2026-10-07 11:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6b918385-dc63-3c64-a4da-2c783a2b82d1 | -11.7943 | -46.7056 | 2026-10-07 12:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| cb45e684-77f3-3049-a795-f6956a6abf61 | -11.0867 | -45.6459 | 2026-10-07 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| b49421c6-ba7c-3201-ad0d-a1208ed97fa0 | -11.7947 | -46.683 | 2026-10-07 12:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| c6865281-087e-3ec0-ae5f-a00f19a5cbc4 | -11.3745 | -46.6948 | 2026-10-07 12:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 5c225058-6490-38a9-b9d3-0780d9e80d1d | -11.7943 | -46.7056 | 2026-10-07 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 62bd8292-729f-33f4-978a-80e78fd0591b | -11.7755 | -46.6856 | 2026-10-07 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1a699848-a64e-3fbb-aa81-a103050275a1 | -11.0867 | -45.6459 | 2026-10-07 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| beb41197-2a80-37fa-bc03-a6725b0152be | -11.7751 | -46.7082 | 2026-10-07 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| bfb95e31-72b3-3ac8-8d62-9db66bd5c5e1 | -11.7947 | -46.683 | 2026-10-07 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 428b79b7-7fb1-3673-a985-421bd8a8bb6c | -11.3745 | -46.6948 | 2026-10-07 12:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| af432df7-bda8-340c-9666-608a6391ad87 | -11.7143 | -43.652 | 2026-10-07 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9bd84336-362f-3d2c-b877-22320b150627 | -11.7943 | -46.7056 | 2026-10-07 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| c196bc65-51c3-3c47-8299-9186b5310f1f | -11.7751 | -46.7082 | 2026-10-07 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 5ac7d3ee-ede3-3dcd-a2a9-48e6e21d4f5c | -11.7755 | -46.6856 | 2026-10-07 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 7d76bcba-5554-3a7e-8627-14df7d197a12 | -11.7335 | -43.649 | 2026-10-07 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 5b9b4750-90a3-309f-9288-a9e92637a008 | -11.3745 | -46.6948 | 2026-10-07 12:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 82d87c5a-3bc4-3653-974b-00a4027f7df9 | -11.1051 | -45.689 | 2026-10-07 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d2144df3-a3b4-33fc-aba9-6ada6b2236f0 | -11.7947 | -46.683 | 2026-10-07 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| aa20928e-2c96-3d96-aec0-167ec5fcd1e9 | -11.0867 | -45.6459 | 2026-10-07 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 9fbe1598-1c31-32d4-830b-319dde537bd9 | -11.7755 | -46.6856 | 2026-10-07 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 84b79aa3-b87a-3f83-a9ee-0a1a488b3cc0 | -11.7751 | -46.7082 | 2026-10-07 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 32cc6815-09a4-3081-a660-fdedd936196b | -11.7143 | -43.652 | 2026-10-07 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 5f313d12-05fa-3874-9026-c93722f09ddc | -10.9762 | -45.4094 | 2026-10-07 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.9 |
| d23678c3-a224-3e60-8990-8e570987850f | -11.0676 | -45.6485 | 2026-10-07 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| ade795b2-45b5-393b-86f8-28623d02a77a | -11.0863 | -45.6688 | 2026-10-07 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 38139d22-dcee-3c20-b66e-8a6ba722b3f6 | -7.8789 | -72.3492 | 2026-10-07 12:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 70c699d0-1137-3b82-9e14-8496666ae4ef | -11.7943 | -46.7056 | 2026-10-07 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| daf257d6-60f1-3c12-9829-a809b0169127 | -11.7335 | -43.649 | 2026-10-07 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 0f755f53-f0a1-38f7-9958-25243c008b83 | -11.7947 | -46.683 | 2026-10-07 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| a4291aaa-b981-3bae-93ed-69b1ce2a5c36 | -11.3745 | -46.6948 | 2026-10-07 12:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| a70cbd35-2518-3ab4-a497-6a8b53e2ac65 | -11.0867 | -45.6459 | 2026-10-07 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 247.2 |
| d6e5c050-88f2-3958-9bd9-233d00868a04 | -11.3745 | -46.6948 | 2026-10-07 12:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 1954ee1d-3186-3061-bd66-b9cf72a3afd7 | -11.7755 | -46.6856 | 2026-10-07 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| b0e1614e-5eb3-34e3-88d7-72b645d509fa | -11.3742 | -46.7173 | 2026-10-07 12:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| f26f0774-cd05-309d-b8cc-5aa7a7f65ef3 | -7.8789 | -72.3492 | 2026-10-07 12:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 0ac5c4f4-2a84-31fc-9e63-74ca46f954ed | -11.7751 | -46.7082 | 2026-10-07 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 0f2abb13-3b85-3a26-ab2b-77db3898bb2b | -11.1051 | -45.689 | 2026-10-07 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ca54fcd3-6035-34f3-95b4-eb9190374a23 | -11.0867 | -45.6459 | 2026-10-07 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 7ee1bac8-74d6-3d26-9b90-3b8ef27d0217 | -11.0863 | -45.6688 | 2026-10-07 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| e0aa1255-1932-31d5-99b7-6ef04fe96ca7 | -11.7943 | -46.7056 | 2026-10-07 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 37e8ca52-fe9a-3971-a3ec-98e03903858d | -10.9762 | -45.4094 | 2026-10-07 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 7911efd1-5d1b-3658-bc11-be35bedc4c93 | -11.7335 | -43.649 | 2026-10-07 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ad17ce38-e11d-3107-bc9b-c1ad76e4e4a6 | -9.432 | -45.8293 | 2026-10-07 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 8394b395-10f8-306c-b209-506cd79de535 | -11.7947 | -46.683 | 2026-10-07 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 226.4 |
| 474eb0bb-72a9-3cd6-b38b-8c88e3513b9b | -9.4509 | -45.8271 | 2026-10-07 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| d32c45c1-2fa6-387d-afaa-4a8caa432817 | -11.0676 | -45.6485 | 2026-10-07 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 6e056684-fb17-3ceb-af96-1967a94a77ea | -10.3738 | -46.2146 | 2026-10-07 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 89e728c6-1e16-3f20-b596-1c01d710d673 | -8.5356 | -55.383 | 2026-10-07 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fe812bc5-4758-373a-8cb9-e17ff7916ba8 | -11.7335 | -43.649 | 2026-10-07 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| dff2ada7-2453-38b2-b50d-8b34f5e872c9 | -11.3745 | -46.6948 | 2026-10-07 12:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| dc2f05d2-e36f-3b58-bed2-4f3f31cb7e72 | -8.2184 | -46.3396 | 2026-10-07 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| baa66ab8-2e98-3c42-a535-eb04707b069e | -11.7751 | -46.7082 | 2026-10-07 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 33638547-07ff-34f4-b365-f0e9e51c8101 | -17.5069 | -45.4666 | 2026-10-07 12:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 185.6 |
| 9d075962-5317-357e-84a2-a157a27c1e1a | -9.432 | -45.8293 | 2026-10-07 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 182.6 |
| afa36756-53ad-33ca-9da2-4adfc7a90d44 | -11.0863 | -45.6688 | 2026-10-07 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| b7f38fca-c624-36b4-96ef-4821da9f7afc | -7.8789 | -72.3492 | 2026-10-07 12:50:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 100.6 |
| d53c87f5-28a1-3eda-8e26-dab0599517c2 | -9.4317 | -45.8519 | 2026-10-07 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 25780807-bf34-3d54-b48f-e944c0d423a6 | -11.065 | -45.8084 | 2026-10-07 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| f1f83fc0-866b-350e-982c-99aeed71af16 | -11.0459 | -45.8109 | 2026-10-07 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 7860d52e-950c-31e0-8701-7d3cae62a4d2 | -10.8054 | -46.5662 | 2026-10-07 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| ae32b371-9a34-368a-b94b-826814085d60 | -11.0642 | -45.854 | 2026-10-07 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| aa5c640d-7c7b-39e7-b869-fd886434fbad | -11.0867 | -45.6459 | 2026-10-07 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| faa96783-166e-3e6b-97f7-18056b886f5d | -10.3735 | -46.2372 | 2026-10-07 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 680a9bf1-31f9-3d27-a8ca-92ac1fc520bb | -9.4509 | -45.8271 | 2026-10-07 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 28faa573-249d-3f6d-b427-5c04ac4cd756 | -11.7947 | -46.683 | 2026-10-07 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| cdab3f3c-2747-351c-b38f-4d806c4b1869 | -11.7943 | -46.7056 | 2026-10-07 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f9da6eaa-5751-353f-92b5-8b083ef71cfa | -11.7143 | -43.652 | 2026-10-07 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| cdeb3faa-8a63-3f68-9722-e48c43567efa | -11.7755 | -46.6856 | 2026-10-07 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| cd9668f0-ffee-3be9-bedc-01291fc0e783 | -9.4509 | -45.8271 | 2026-10-07 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 302.7 |
| 0665fb68-a79b-3675-b7ed-beca3d5a3ce7 | -8.5844 | -45.6729 | 2026-10-07 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 39700de3-2bd4-379f-983c-b7b7213c8bd5 | -11.7947 | -46.683 | 2026-10-07 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 196.5 |
| c981633a-a3a6-356f-b3ba-763d4dc692f3 | -11.0459 | -45.8109 | 2026-10-07 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 93f94a0e-9328-36c0-9300-aa38ed8a10e4 | -10.9949 | -45.4298 | 2026-10-07 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 08a50b20-7232-33eb-a04c-6e2e5dea8d66 | -6.4413 | -55.0224 | 2026-10-07 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |


[Clique aqui para ver as próximas entradas](README128.md)
