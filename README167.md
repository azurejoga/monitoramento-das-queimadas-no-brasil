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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c277f3a-4bb4-33e0-a600-3de28472866c | -8.852 | -66.7827 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 90c49cc7-2988-3915-b2d6-9c2d93f0142d | -5.9603 | -41.3749 | 2026-10-05 19:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 172.2 |
| d1facabf-cf30-38f4-a8cb-e11a118a7c0e | -9.3494 | -67.4374 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ee68774e-79e2-3738-a201-71618ab41ae4 | -8.537 | -66.9764 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 2ffcb26a-5435-3947-bc56-cdc7fe009cb1 | -7.4889 | -42.8059 | 2026-10-05 19:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 8371b5bf-4fa4-31cf-a748-982b34fe9930 | -4.8083 | -42.134 | 2026-10-05 19:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| f7b6d43b-e5d9-3b55-9c2c-aad2913d0734 | -8.593 | -66.8081 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 437d5893-d46e-3125-93a3-92b7a5e7b9d9 | -6.9328 | -43.6799 | 2026-10-05 19:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e448eb97-7805-364f-acd7-3139fcdb421a | -6.4279 | -43.4686 | 2026-10-05 19:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5fccc5a3-e57e-36ba-bec7-f59a2f3bd7de | -9.4751 | -64.3336 | 2026-10-05 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 5a49b262-2f49-38dc-b2d7-a93d471ebf82 | -9.2366 | -67.885 | 2026-10-05 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e7cfb792-2e19-35f0-82cf-f90d36a15404 | -9.4565 | -64.3344 | 2026-10-05 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 50467ff5-69d2-34d2-a8c6-bc1613c5373c | -8.852 | -66.7827 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 3309b68d-d192-308b-864c-7d24b5049f6b | -2.5353 | -65.8635 | 2026-10-05 19:30:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| a9fccc3a-9cab-30ff-966d-cbdb01fe0674 | -8.8526 | -66.6341 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| b696cf74-a758-330c-bba1-02d2351661dd | -2.5353 | -65.8819 | 2026-10-05 19:30:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 6cb0e5e1-e637-34d1-a4ee-02bd77f29c35 | -10.534 | -68.7055 | 2026-10-05 19:30:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 81.3 |
| fd4a6af3-1cb1-3e00-a076-d1caed5eab89 | -9.9728 | -65.1232 | 2026-10-05 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 792c920b-4a08-3e7d-8cb5-20c888d42934 | -9.9413 | -43.4599 | 2026-10-05 19:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| decc9225-8676-3422-babd-07389c494d61 | -5.8323 | -45.0105 | 2026-10-05 19:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 2d244c6d-a602-3f24-be0a-086e2397bea2 | -6.8952 | -43.6833 | 2026-10-05 19:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 28181ce8-b96e-3773-b34e-0266c55b8787 | -5.9606 | -41.3507 | 2026-10-05 19:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 161.7 |
| f0b0c73e-eda0-3d2d-8d5e-38f0564258fd | -9.6672 | -66.834 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| a05091f0-6547-3deb-b61d-fb88be55b511 | -5.8511 | -45.0091 | 2026-10-05 19:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 397d3a17-6414-373d-bb98-7c7e22f452b7 | -9.7126 | -65.0951 | 2026-10-05 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 5b4b7c19-6493-3a7b-aaa8-d4f65d5dbdef | -9.0429 | -65.4361 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.0 |
| f269d0c3-7ce6-3911-b220-c142f507037f | -11.257 | -43.5095 | 2026-10-05 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 01ef2f91-7db6-3e68-b10a-e4b6adc1b8b1 | -9.0982 | -65.4904 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 2c98d018-ca93-375b-a1d6-8b66f4c1aafd | -5.8321 | -45.0332 | 2026-10-05 19:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4df3046f-6ba2-3794-a165-aa1c0b0609ea | -9.0045 | -65.7174 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| ebe52d8a-7d2a-34a9-8ee2-0788087c5086 | -9.9175 | -65.0313 | 2026-10-05 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| d6f0b149-a40d-3908-a83a-49fd63a8da48 | -9.077 | -66.0881 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| b0e134ea-1ba9-3a5d-bc96-bb5b625706b7 | -8.6214 | -69.5026 | 2026-10-05 19:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 258cf966-9867-30c2-a1db-2b7d31bd188d | -9.7127 | -65.0763 | 2026-10-05 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 26c93aa9-b1f6-371b-8249-4d4cd5919712 | -6.8408 | -41.7994 | 2026-10-05 19:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 513b252c-3966-325b-84e3-139eb8f46a1b | -9.9604 | -43.4574 | 2026-10-05 19:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 38b05ec0-0e64-37e8-a29c-0a586b1217f0 | -4.8081 | -42.1577 | 2026-10-05 19:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 144.7 |
| de05f839-c761-3d1d-90df-f753a00c3e03 | -8.3341 | -62.8309 | 2026-10-05 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.1 |
| b59e6973-2538-3af3-8318-711580cd5cb4 | -9.7312 | -65.0944 | 2026-10-05 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 2ad1bfc6-68eb-356f-a6bf-f84e13994005 | -9.1334 | -65.9 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| d3041270-3f8d-3478-91ad-a120586d4091 | -9.1076 | -67.703 | 2026-10-05 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| a4cfc56f-c295-3e18-a196-e6d364978b8a | -6.914 | -43.6816 | 2026-10-05 19:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 4913bf92-daae-3be7-987f-9fe9180ff22c | -9.1243 | -68.2206 | 2026-10-05 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 4bf85723-1fe5-3f77-921a-41ce96d3ab8d | -6.8764 | -43.685 | 2026-10-05 19:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 0ed97dba-2f90-36bc-a36d-a7862c255985 | -9.0614 | -65.4355 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| fc64ef4b-ccf4-35f8-8c76-d851785f8273 | -8.8696 | -67.0049 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| f4cb8dd7-252b-3169-8c40-2a29a1076849 | -4.5091 | -42.0584 | 2026-10-05 19:30:00 | GOES-19 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 69a170ae-ebe0-3945-87eb-d8a15a0c5260 | -8.8525 | -66.6527 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| f55fa1db-be47-32bc-aa94-8c97bdd3fe11 | -5.8509 | -45.0318 | 2026-10-05 19:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 82db0d31-a941-3ac8-9aef-f0404a2fdf78 | -9.1244 | -68.2021 | 2026-10-05 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 88e33cd1-983f-397e-8de3-9affc04c03a3 | -9.9176 | -65.0126 | 2026-10-05 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 3a0ebf28-53ab-3375-a3cc-9d2e42770c6d | -8.5183 | -67.0139 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e1f88f21-32ff-3f2b-81ae-74b90bcc963e | -8.537 | -66.9764 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| df2c2360-1143-3dc8-9dfc-6e7942e43041 | -9.3431 | -64.7143 | 2026-10-05 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 2dcac22f-5196-350f-be66-31f7cd1ff800 | -5.9603 | -41.3749 | 2026-10-05 19:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 191.9 |
| 46c33a25-8ab3-3a43-a61f-5de60acc5135 | -8.8519 | -66.8012 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.0 |
| a0a3483f-640d-39bc-a635-166287edbb2f | -2.5535 | -65.8634 | 2026-10-05 19:30:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 80f68289-da41-35fa-9ca1-a5b91f369b6f | -9.3494 | -67.4374 | 2026-10-05 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4d5e01ba-f360-335e-a69e-e8834339bc28 | -6.8597 | -41.7975 | 2026-10-05 19:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 151.1 |
| 541fd15b-f9c6-3330-9695-02363f1343be | -9.1259 | -67.7581 | 2026-10-05 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 9a13e322-23f0-3391-b36a-de89ba72a4aa | -11.2566 | -43.5331 | 2026-10-05 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 85c0b385-ca99-3533-be58-5423aa3db54e | -8.871 | -66.6521 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 4884899c-b02b-3be5-af60-c64ee2feddaa | -8.5929 | -66.8266 | 2026-10-05 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 0a58a78b-3e5e-326b-8e50-f411e18db997 | -5.9606 | -41.3507 | 2026-10-05 19:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 147.7 |
| 4733e0f1-3568-3aa6-a394-0fa575d28243 | -9.6672 | -66.834 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| c9fc1d4d-7c1d-330b-9234-b44d682a2c1d | -7.47 | -42.8078 | 2026-10-05 19:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| af415d30-5358-3b14-baa7-6c9d95c3bc96 | -9.0982 | -65.4904 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 7fccc12d-9e8f-3755-af9b-a26a4ba811cc | -9.1257 | -67.8137 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| bb133f03-786d-39c9-9444-68fec02e5ab2 | -5.1303 | -44.0074 | 2026-10-05 19:40:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 910e73c4-dca2-3666-bd8f-83cf9b532a6b | -8.5183 | -67.0139 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 14c13f37-7ce6-3adb-95d9-447dd34c0ef6 | -9.1257 | -67.8322 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 4d6d40e9-27da-3540-8ade-602b60f42d80 | -4.8081 | -42.1577 | 2026-10-05 19:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 91e081fd-8306-3cbb-b24f-6e03e209751a | -6.914 | -43.6816 | 2026-10-05 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 451303f5-b308-3f5b-9bb7-2551d16e51ef | -9.006 | -65.4 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 57c43a92-6dec-33a1-9dcb-520183a88235 | -9.1334 | -65.9 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| f7312807-e6fc-3ea3-a0bc-d7631600de2c | -9.1244 | -68.2021 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 2f9b45c2-46e5-3267-a622-37b4b43c6501 | -5.0463 | -45.1995 | 2026-10-05 19:40:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e7d422e3-651c-385c-9f29-75f058c77b25 | -10.534 | -68.7055 | 2026-10-05 19:40:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ee1fabb3-778a-3351-8b45-f01285dc566b | -9.3494 | -67.4374 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8ce64e3b-4f0b-3b9f-b44b-30c7d0dec246 | -8.593 | -66.8081 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 179.7 |
| d5515a29-9cde-322d-8691-e6762660bfc9 | -5.8511 | -45.0091 | 2026-10-05 19:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 3af48378-3e1c-34d6-94db-02c50a8d55f9 | -8.537 | -66.9764 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 341e3ba0-e48c-3aa9-9f5e-12768ed3ef76 | -2.5353 | -65.8635 | 2026-10-05 19:40:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 5d9b0e90-637e-343e-93f2-41ec74d11f50 | -2.5353 | -65.8819 | 2026-10-05 19:40:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| e01f250c-5846-3959-82c8-c738b4476331 | -9.1076 | -67.7215 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4e34107a-8bf9-3cff-ae9a-589cd6007d84 | -9.077 | -66.0881 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 3a47ec35-bf4f-3a79-ab41-dbdf75a0b98f | -9.0889 | -67.759 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| cddda414-54fa-3ae7-aeda-0ebe42e06285 | -9.9604 | -43.4574 | 2026-10-05 19:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| dd6e7ae4-ef90-3df5-a605-47c4a8e349dd | -6.8597 | -41.7975 | 2026-10-05 19:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| a3d044e9-24c3-3fa8-95dc-edc21e2654e1 | -9.3259 | -68.8811 | 2026-10-05 19:40:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 31838784-2f7d-353a-8f62-64fa9405ad77 | -5.6668 | -42.5926 | 2026-10-05 19:40:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 6e707444-0428-33c6-9601-de8e9a94fe91 | -9.0429 | -65.4361 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 1db3a985-f6db-330a-a811-28cd7e00d85a | -9.1072 | -67.8326 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 87c7532b-6e7e-3b17-8c6b-7210cbe0d471 | -9.1075 | -67.7401 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| cd447a1c-d92b-32e1-b66d-442c6c979848 | -9.4751 | -64.3336 | 2026-10-05 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 1b9902ef-a6fd-3df3-afc9-049c48b2a1d7 | -8.852 | -66.7827 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 6f18f6c0-8252-35c0-a361-70fb4035a486 | -5.8509 | -45.0318 | 2026-10-05 19:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| fc3d5057-6ef0-3692-aa07-d72256727945 | -5.9603 | -41.3749 | 2026-10-05 19:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 219.5 |
| 1563f33e-46af-3566-ab15-316f7a53b410 | -9.2366 | -67.885 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9a71e30d-4e1e-39dd-8c7e-b5e94668b193 | -9.5425 | -65.6815 | 2026-10-05 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.9 |


[Clique aqui para ver as próximas entradas](README168.md)
