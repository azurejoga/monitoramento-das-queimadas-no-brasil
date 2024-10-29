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
| ed1df294-601f-3cb7-a3c7-957556558230 | -0.9815 | -53.7192 | 2024-10-29 00:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 91108265-78c1-3161-9d9a-c5c722d91858 | -0.9815 | -53.699 | 2024-10-29 00:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8af1e333-cd60-3fa9-ac5e-b207e81b377c | -1.0445 | -47.6455 | 2024-10-29 00:05:12 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 4bd19d64-cc44-3bf2-8773-4f1a46433708 | -1.714 | -54.5335 | 2024-10-29 00:05:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| f86de9db-1449-30f4-bb58-c894e1be88cb | -2.1903 | -47.9501 | 2024-10-29 00:05:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 360bab6b-eaee-3b25-b62d-53e4e01136c2 | -2.3353 | -48.9137 | 2024-10-29 00:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 7cd8357e-2cad-3dda-8659-175dc91eff71 | -2.3537 | -48.9133 | 2024-10-29 00:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a44cffa1-d3c2-3a46-ac07-e84b5ab030dd | -2.5251 | -47.442 | 2024-10-29 00:05:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3c5ae5ef-cdfe-3002-a66f-99265f2af4f9 | -2.6398 | -51.758 | 2024-10-29 00:05:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 781f574e-34cf-3310-8691-fa80ab9f9c26 | -2.8146 | -49.2206 | 2024-10-29 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 9667a9f8-ab2e-3768-9426-554fb64478f2 | -2.8555 | -53.3459 | 2024-10-29 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| d6813f7d-95a8-3872-8882-fa6ba0b63da8 | -2.8739 | -53.3454 | 2024-10-29 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 272ea8b7-f3a3-3e77-951b-d05c739eb66b | -2.9619 | -54.5304 | 2024-10-29 00:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b408c69d-1bc5-3ab5-990c-83d521e8b28a | -2.962 | -54.5104 | 2024-10-29 00:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 2be218ec-3eea-346b-aa07-2341f99fb6e8 | -2.9803 | -54.5299 | 2024-10-29 00:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c64fbc5a-cf2c-34b1-ac71-9daeaaa6cce5 | -2.9804 | -54.5099 | 2024-10-29 00:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 753062e9-3285-31e3-8cda-c61cf53cbfc3 | -3.0501 | -50.4171 | 2024-10-29 00:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 5ce02911-f886-395c-aef9-5cc466c27097 | -3.0913 | -54.287 | 2024-10-29 00:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| f462cf93-00fa-3f4b-8f2a-3263a1265ac9 | -3.1097 | -54.2865 | 2024-10-29 00:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| e3aea3be-8dd3-3970-9233-ad29f72cdb39 | -3.1098 | -54.2665 | 2024-10-29 00:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| f3d24c83-9534-3351-aaf8-cdc4712bfc05 | -3.2495 | -43.2547 | 2024-10-29 00:05:24 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| edec1250-d667-309c-b669-5319abd8b56b | -3.1281 | -54.286 | 2024-10-29 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f96502d6-67df-3139-b810-e0864a7a3947 | -3.1281 | -54.266 | 2024-10-29 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 5358dce7-e24f-3cfb-8507-42201fa444cd | -3.1794 | -50.3922 | 2024-10-29 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 2eab1289-a5ef-3c28-b971-497520ce80fa | -3.2548 | -45.9186 | 2024-10-29 00:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 6a089f85-7722-3a19-a2e7-91aa84e01dc2 | -3.6898 | -51.8513 | 2024-10-29 00:05:27 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 74149590-cdaf-3aa5-a0ee-5a97180475fe | -3.9289 | -48.3458 | 2024-10-29 00:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| cbc6d46f-d61d-326d-bd59-addf2ef2e0c5 | -4.3286 | -43.7801 | 2024-10-29 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5e34f487-da47-3e79-b413-46160d891d22 | -4.3473 | -43.779 | 2024-10-29 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 7d04c389-c722-3d90-83f2-153df09367cd | -4.3475 | -43.7559 | 2024-10-29 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 0d93de8f-4e5c-34a6-96fa-ce7fd6dd8df7 | -4.6432 | -44.1762 | 2024-10-29 00:05:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| af51b816-d9f9-3387-abb5-89c6d2f7fe2c | -4.6619 | -44.1751 | 2024-10-29 00:05:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 93f7d567-1901-368c-9456-9768d998d80f | -5.2661 | -43.4193 | 2024-10-29 00:05:35 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 8635a4e5-6cfd-3b63-9511-7f099bcf3fb2 | -5.2663 | -43.396 | 2024-10-29 00:05:35 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 5c4c26ff-6131-3bf5-bca8-87d5e90f7196 | -5.2848 | -43.4179 | 2024-10-29 00:05:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 63afa1b6-12ac-38a2-8b29-2352b2467de3 | -5.285 | -43.3947 | 2024-10-29 00:05:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 191.4 |
| a1a86753-79b5-3353-a721-cbd2c5c0205f | -6.0791 | -44.6276 | 2024-10-29 00:05:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 6fb206f0-8423-326c-9bb7-0821a0010f40 | -6.4534 | -44.6664 | 2024-10-29 00:05:42 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 90344831-21d7-39c0-81f7-7f2821b0d125 | -6.5054 | -47.0414 | 2024-10-29 00:05:43 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e15e7597-87e4-3340-b6ab-c4f38c2f2c3a | -6.5956 | -47.3867 | 2024-10-29 00:05:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 08bfeda6-92e1-3134-b390-08d2ed2edcc1 | -6.6143 | -47.3853 | 2024-10-29 00:05:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 98b44ba9-1031-34e0-9238-c7bdbb4d1bf9 | -7.3038 | -35.1761 | 2024-10-29 00:05:46 | GOES-16 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 157.0 |
| 43ee6dc1-5b56-38f0-a769-5a055060c3aa | -7.3042 | -35.1486 | 2024-10-29 00:05:46 | GOES-16 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 106.7 |
| 1241c127-b918-3cf6-bc7c-2ffe682005fc | -7.2637 | -46.069 | 2024-10-29 00:05:47 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 505b4cea-ec07-379d-8807-494a7a1febe2 | -9.8775 | -36.0262 | 2024-10-29 00:06:01 | GOES-16 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 111fabf6-792e-3879-92cc-a5813468f86b | -11.1378 | -55.5515 | 2024-10-29 00:06:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 62bd378c-4110-3d2a-a2c1-f782f1926e57 | -11.138 | -55.5313 | 2024-10-29 00:06:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 1daaa482-dbe5-362a-84af-6ad76aa55f62 | -12.0854 | -52.4803 | 2024-10-29 00:06:14 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e4cfd0c6-6ac6-34c1-9dd2-ec9d8d968ac5 | -12.4433 | -43.7242 | 2024-10-29 00:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 703cc84f-f71d-3a2b-84ab-59880a066f8c | -12.3334 | -49.9208 | 2024-10-29 00:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 5dfcba10-3e77-3619-a35d-a07a53229a46 | -12.3526 | -49.9184 | 2024-10-29 00:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| e48d00bc-bcd6-345c-b609-12991e6abc4a | -12.6725 | -43.8279 | 2024-10-29 00:06:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 0d206818-7881-3f79-bfe6-16915cf92213 | -12.673 | -43.8042 | 2024-10-29 00:06:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 69b3e20c-1df5-3e6b-9dab-0dfd04f6b633 | -12.4362 | -63.6882 | 2024-10-29 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9adcc356-b68c-37cc-b03d-526b314c114d | -13.6028 | -45.587 | 2024-10-29 00:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| ce71475a-dd05-3de5-a256-9e04ffd66256 | -13.6033 | -45.5639 | 2024-10-29 00:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b0b8a7cc-30dc-3a24-a784-8bc589a621b7 | -13.6222 | -45.5838 | 2024-10-29 00:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7aa88522-2b9f-3d7d-bd93-4b843bbb1ada | -13.6227 | -45.5606 | 2024-10-29 00:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4665ac76-bf9d-3826-99e7-423977faf3cd | -14.1386 | -44.09 | 2024-10-29 00:06:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| a4717a3e-a85d-39c2-8f3c-f441b447e59c | -14.1391 | -44.0662 | 2024-10-29 00:06:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2f7e055f-92b2-3630-8553-525d2291c2bd | -1.714 | -54.5335 | 2024-10-29 00:15:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| de193e3a-f023-3a51-9469-6cbb57e36fbe | -1.9166 | -46.6025 | 2024-10-29 00:15:17 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 1ba01767-379f-3991-9dd3-2940d6c481fc | -2.3353 | -48.9137 | 2024-10-29 00:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| b68d5a5f-404a-360f-8a5d-0f37a608ce92 | -2.3537 | -48.9133 | 2024-10-29 00:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| fe2fea24-8ea4-3175-8f9b-00bab0912907 | -2.5251 | -47.442 | 2024-10-29 00:15:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| bf315a9f-142b-3ea4-9713-f554aab53efc | -2.8146 | -49.2206 | 2024-10-29 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| efeb774a-c20c-357d-a464-3b79e626e85a | -2.8555 | -53.3459 | 2024-10-29 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 0b565cc1-37ae-314d-a509-2c07b4075a32 | -2.8739 | -53.3454 | 2024-10-29 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c4e1ef96-914c-38df-93a0-e3a7de2e695f | -2.9619 | -54.5304 | 2024-10-29 00:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 6dd85124-7131-31a2-bba4-56800c1de840 | -2.962 | -54.5104 | 2024-10-29 00:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 176.5 |
| b28d2a65-70eb-31e2-8e2b-40ec5f9a55d7 | -2.9803 | -54.5299 | 2024-10-29 00:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| e4c8df56-fa5b-3d00-82c1-a3819bc44739 | -2.9804 | -54.5099 | 2024-10-29 00:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 6780e71e-4e49-3ceb-b1e8-3457679f7e81 | -3.0913 | -54.287 | 2024-10-29 00:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 92dc404d-64ed-388c-b776-62564955650c | -3.1097 | -54.2865 | 2024-10-29 00:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 6cbe0b25-6b6e-3534-927d-3594703af1dc | -3.1098 | -54.2665 | 2024-10-29 00:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a4f95129-6ede-3be8-ae59-8bd590b99377 | -3.1281 | -54.286 | 2024-10-29 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0fbb28e7-44c8-3dde-a43b-9358371f325f | -3.1281 | -54.266 | 2024-10-29 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 212317d6-c59d-3c02-97c4-5e53a795dcc4 | -3.1794 | -50.3922 | 2024-10-29 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 69d42068-1eaa-36f6-a9b8-e372e6d18ce5 | -3.2548 | -45.9186 | 2024-10-29 00:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 97e9504d-ef16-33f0-a031-4bda43b3ad77 | -3.9289 | -48.3458 | 2024-10-29 00:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1130ea29-6380-3e02-a97c-18c9107f46e0 | -4.3473 | -43.779 | 2024-10-29 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 5ac95f67-c0cc-314b-8117-8ffc45826cd1 | -4.6619 | -44.1751 | 2024-10-29 00:15:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 52dd6d87-f8b2-30a0-80b5-b12007524f3b | -6.5054 | -47.0414 | 2024-10-29 00:15:43 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| b9a9d23d-0101-37d8-8392-e72303d2d594 | -6.5954 | -47.4086 | 2024-10-29 00:15:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| cb7fc31b-7039-3926-836c-c688e3fb53f5 | -6.5956 | -47.3867 | 2024-10-29 00:15:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 9a7220ce-9d64-39fa-9e87-8ad8eee12732 | -6.6143 | -47.3853 | 2024-10-29 00:15:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| fe99425f-5b6d-3653-8544-2749886b687f | -7.2637 | -46.069 | 2024-10-29 00:15:47 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 46ba100b-ebd3-3bd1-8dfa-cdd5b19d95ed | -9.8775 | -36.0262 | 2024-10-29 00:16:01 | GOES-16 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 994de075-0808-3f7b-bae5-5fab36bba39d | -10.2762 | -36.3327 | 2024-10-29 00:16:03 | GOES-16 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 202.6 |
| 69d63f41-6d8a-3ede-8708-451ec71bebba | -10.2768 | -36.3057 | 2024-10-29 00:16:03 | GOES-16 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 127.0 |
| 96bfa453-1d12-3a49-83a8-e2f1964f5b46 | -11.1378 | -55.5515 | 2024-10-29 00:16:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| da4d5e67-9c08-3f19-8410-33d6351aea35 | -11.138 | -55.5313 | 2024-10-29 00:16:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 6e9b28d0-1511-3b9f-b011-d874f3268ad5 | -12.3331 | -49.9424 | 2024-10-29 00:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e88b66f7-5dd9-3679-b1f3-05d26c51cd66 | -12.3334 | -49.9208 | 2024-10-29 00:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 22b9a6ab-3ec4-3afe-82fb-81271658fa0e | -12.3522 | -49.94 | 2024-10-29 00:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b7a705b0-e970-36a7-a9a4-29fcc2c67c81 | -12.3526 | -49.9184 | 2024-10-29 00:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 64b7814e-c4ca-3a28-9a8e-ef3838fc17bb | -12.6725 | -43.8279 | 2024-10-29 00:16:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 23f75217-cc50-3a2b-889c-5e6956cc010e | -12.673 | -43.8042 | 2024-10-29 00:16:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d2906ccc-f4d2-3337-ac87-3db2d8a80246 | -13.6028 | -45.587 | 2024-10-29 00:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 9adec173-c207-39c0-be73-322ec6d1dabf | -13.6033 | -45.5639 | 2024-10-29 00:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |


[Clique aqui para ver as próximas entradas](README2.md)
