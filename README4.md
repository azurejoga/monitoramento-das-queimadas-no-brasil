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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b96d615e-8a5c-3607-a3ba-acac5bcd143a | -13.2863 | -46.962 | 2025-09-26 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 62d81510-7b01-339a-a756-12170bc1d548 | -15.9966 | -59.4851 | 2025-09-26 02:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| e881683b-0ff0-3b6a-b2fd-a6017e029e54 | -5.6361 | -43.9258 | 2025-09-26 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 4f879a0e-aff7-3874-839c-68c74cc0743d | -6.1487 | -47.2651 | 2025-09-26 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 5c3bb18a-0d05-3766-be8c-bd443f492f88 | -6.1674 | -47.2638 | 2025-09-26 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| efc68467-ca36-3c68-9f81-f6f7e1ebfe74 | -6.1672 | -47.2858 | 2025-09-26 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 34ab44a7-3e75-3ed6-b704-0905142d689e | -6.1485 | -47.2871 | 2025-09-26 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 360.9 |
| d8da84ce-c5cd-316f-b7e0-af8aafa4e1ee | -7.6772 | -46.0097 | 2025-09-26 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 1a683862-c993-302b-b8e5-4e8c402da472 | -15.9966 | -59.4851 | 2025-09-26 02:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e6ac1596-96eb-3073-a874-70175ff2a1ae | -5.6361 | -43.9258 | 2025-09-26 02:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| c35782cc-a19c-318c-9c8f-3850ddabac65 | -6.1299 | -47.2884 | 2025-09-26 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 6731c1f9-0c83-36c8-b0e0-6914c35db189 | -6.1301 | -47.2664 | 2025-09-26 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 63047ff6-8933-303c-ba80-87c6f34016c6 | -5.6361 | -43.9258 | 2025-09-26 02:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 0afb8a6d-977b-367d-9cda-d4f36adb9641 | -15.9966 | -59.4851 | 2025-09-26 02:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| fcabb1af-e0e7-3344-9e3e-67803804b39a | -5.4562 | -43.0788 | 2025-09-26 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 1d6416f3-0cb5-3c33-b850-b2fab123ee70 | -5.475 | -43.0774 | 2025-09-26 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 42f59fe3-57a0-3520-a6f7-7ae9852a4927 | -5.4565 | -43.0554 | 2025-09-26 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 8af5e285-9872-3749-8796-8d73216d1cb8 | -5.4752 | -43.054 | 2025-09-26 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 9fdfbef3-072f-3b80-8647-b506db780700 | -15.0673 | -49.9115 | 2025-09-26 02:40:00 | GOES-19 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 6a764890-28e0-3282-880c-f17ae098cb53 | -5.4752 | -43.054 | 2025-09-26 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| c159a94f-bf1d-3af4-8d41-b472b2854668 | -5.4562 | -43.0788 | 2025-09-26 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| ed1ca81d-c87a-3943-9c47-323581d389be | -15.9966 | -59.4851 | 2025-09-26 02:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| ebb0d660-9bdd-32dd-ab2a-3d16584a09ae | -10.4125 | -46.1647 | 2025-09-26 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 264.4 |
| b72255bd-3fa0-3f68-95f6-3cc13b48be40 | -16.8538 | -50.5026 | 2025-09-26 02:50:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 4d53972f-3827-382e-b146-2aae8a4fe174 | -10.4129 | -46.142 | 2025-09-26 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 8c0a7d85-2a88-3160-bf4e-9b820e620dec | -5.7579 | -44.9704 | 2025-09-26 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 177b4eb9-758e-3c4f-af5a-f62d8d364d4a | -10.3938 | -46.1444 | 2025-09-26 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 4452ff33-ee15-3a0c-b557-f97c1313caa6 | -5.7394 | -44.949 | 2025-09-26 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| fabf9281-f8d5-3591-bb42-18c83a93537f | -10.3935 | -46.167 | 2025-09-26 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| cbe5787e-d49f-3ab9-af37-07736107bbb3 | -5.475 | -43.0774 | 2025-09-26 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 67a5f029-3325-327b-87b1-b78128ce1532 | -15.9384 | -59.4907 | 2025-09-26 02:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 44578bdb-efb3-38b8-9871-936cf306d38e | -5.7392 | -44.9718 | 2025-09-26 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6a02d0df-dd6f-3eda-b05f-3e57cf159e1f | -5.4565 | -43.0554 | 2025-09-26 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 71bbf683-9c13-3d20-9f2f-a0f302e80500 | -15.9966 | -59.4851 | 2025-09-26 03:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4ab59c4d-bf87-3d99-85bb-4b511883a98c | -5.4565 | -43.0554 | 2025-09-26 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 5da53a3a-c949-3382-8057-2722488d4d7a | -10.4129 | -46.142 | 2025-09-26 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2da318de-4241-3078-a9d0-774d036c07f5 | -5.4752 | -43.054 | 2025-09-26 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 73aaab64-5313-3244-831d-d83a42f239ee | -5.475 | -43.0774 | 2025-09-26 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c928984a-22bc-355c-a358-56eaa3ae80f2 | -5.4562 | -43.0788 | 2025-09-26 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 7b8fab85-caf5-3c8a-9838-c263af665aaa | -10.4125 | -46.1647 | 2025-09-26 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 0f9ee4cb-ee17-32e9-9497-5e0c621ca4dd | -10.4125 | -46.1647 | 2025-09-26 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| bc9b67ad-b87d-31be-86b7-1f8207dfcdac | -5.7579 | -44.9704 | 2025-09-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 02fbf1e7-c9e2-370d-9368-d775e0c49a15 | -5.4752 | -43.054 | 2025-09-26 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e1d38eb7-5114-3050-b39a-5088663563e9 | -11.2412 | -45.5334 | 2025-09-26 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 133a74b2-d5d2-3be3-8187-8e755595d3ec | -5.739 | -44.9945 | 2025-09-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 24a20aca-e9c6-3cd4-b68d-3ca4e79a6496 | -5.475 | -43.0774 | 2025-09-26 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 1255d901-bdfa-33f3-9aec-423e626a3eba | -11.2217 | -45.559 | 2025-09-26 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| abc1e269-ac81-31a2-ab2f-45cc5b62a69a | -5.7394 | -44.949 | 2025-09-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 391c546f-b901-3b9c-be0a-d5a98eda6cc4 | -5.4562 | -43.0788 | 2025-09-26 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9450d1c4-9dc2-3d0b-8983-75d30e9af720 | -5.4565 | -43.0554 | 2025-09-26 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| e4892168-6634-3533-9d1e-23cd1056dc28 | -11.2408 | -45.5563 | 2025-09-26 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 50de535f-20f9-3419-ac87-7699b5e628b2 | -5.7392 | -44.9718 | 2025-09-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 8ccdf021-04b5-3826-9a13-d703d51642ef | -5.7581 | -44.9477 | 2025-09-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 67abed80-3f3b-31dd-9225-66e526aefbae | -15.9966 | -59.4851 | 2025-09-26 03:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 65c75adc-8d05-3641-a78e-22e25bd76656 | -5.7392 | -44.9718 | 2025-09-26 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 16e911d6-d680-3d50-8409-beb9fcf19c7e | -15.9384 | -59.4907 | 2025-09-26 03:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| a22e4efa-8620-3a4c-b4bd-b73d7263793d | -5.7579 | -44.9704 | 2025-09-26 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 3f9ab301-0670-38ea-9505-7983b6d8e214 | -15.9382 | -59.5107 | 2025-09-26 03:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 1ca0b844-530c-3422-83d7-5748d76e6f76 | -5.4752 | -43.054 | 2025-09-26 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 3bb7bfa9-33e7-36cf-99e3-2c9674a48dcb | -5.6174 | -43.9272 | 2025-09-26 03:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| f0574318-c1b6-37b1-88e6-ac2b28b2203d | -5.739 | -44.9945 | 2025-09-26 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| ae68fe93-5513-3135-86dc-306d824e07f8 | -5.4565 | -43.0554 | 2025-09-26 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| da014f90-fb85-3c42-b685-086abd81c98c | -10.4125 | -46.1647 | 2025-09-26 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 36a72a06-208d-3f52-b406-351d053688f9 | -10.4122 | -46.1873 | 2025-09-26 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| c53cb4df-7d47-3af3-8411-a741d320cbca | -15.9966 | -59.4851 | 2025-09-26 03:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 85628716-0763-3c95-839d-8fadf99dbba0 | -11.2603 | -45.5308 | 2025-09-26 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 45db6502-5ee7-32ea-a213-f945ed2d95c3 | -5.6359 | -43.9489 | 2025-09-26 03:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| b3ce4215-9f04-3a97-9e12-f60d7dc51236 | -11.2412 | -45.5334 | 2025-09-26 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8361824c-e9b4-3b69-8fb3-2d20c52092c3 | -5.6548 | -43.9244 | 2025-09-26 03:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 49228e6a-7c88-3e36-a9c3-34ba5485cbbf | -5.6361 | -43.9258 | 2025-09-26 03:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 59062be4-5dc3-3887-8edb-4f2c81bd2efc | -5.7394 | -44.949 | 2025-09-26 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 9d0bb2fe-530e-39ee-bc8d-36209656cd10 | -11.2408 | -45.5563 | 2025-09-26 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 428d1a49-8a5b-3b47-b77b-f0aa2b04d879 | -3.80674 | -41.56987 | 2025-09-26 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1ea8a022-0d9d-3759-b409-2501c05354ad | -6.96785 | -42.30304 | 2025-09-26 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| df2e269a-c86f-363a-af52-51a5a538c0c3 | -4.80747 | -43.54156 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 05dd3ea3-9622-398c-a14f-21628a29df88 | -6.26977 | -42.1973 | 2025-09-26 03:21:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 75d663ab-c642-39b9-aca2-edd8aa1b3425 | -6.25556 | -42.49591 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fb1bf96b-8b4e-382c-ab3d-7f9e368bf76b | -6.36485 | -35.21047 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 93adad3b-06cb-3ac2-8687-8e7b71b8f6d5 | -6.37566 | -35.21923 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 54.1 |
| ce0a53d1-cd46-3885-a1da-2ae2eb1a58ef | -9.44076 | -40.38246 | 2025-09-26 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a1a8be13-ba0b-3c17-ae10-d3c8ea0094e0 | -8.13381 | -42.38266 | 2025-09-26 03:21:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 173e4fe9-8df6-3966-93f1-fa4c025e3422 | -4.38495 | -41.93078 | 2025-09-26 03:21:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecdb5169-1fb3-35f0-ba54-a44da631ccee | -5.46055 | -43.07958 | 2025-09-26 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 181ef225-2ec7-3477-b1e4-06f14d697d2d | -4.73895 | -43.61291 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0948529-bbe0-35aa-8aef-91f433eb0aa9 | -4.75082 | -43.27068 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75ca7e70-495b-3122-a810-b62589ed04fd | -4.75183 | -43.62203 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae699e44-d9c1-35b6-a288-188200f82496 | -4.74392 | -43.26946 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb85405e-149d-3152-aeec-abe326356203 | -5.72856 | -42.63971 | 2025-09-26 03:21:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 266cd607-fa0c-37ff-aff5-cce1022fcd0a | -6.87474 | -44.50557 | 2025-09-26 03:21:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2a12cdb4-8164-3ef5-9d93-b4a70d59df40 | -6.25486 | -42.49736 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 0fa6c515-e74a-3b92-a66b-e27b8130613b | -9.98467 | -37.3597 | 2025-09-26 03:21:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 292b8475-7abc-32bf-aee2-815474833cb3 | -6.25457 | -42.50119 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 604b8665-167f-3c06-87ef-cd2a47bd5d58 | -4.74279 | -43.27588 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b6ccf06-3be9-32fb-8a3e-ff4e11fe6d1b | -3.80763 | -41.56478 | 2025-09-26 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 97c64068-86f0-3502-893e-1e7d53b0f42b | -4.74602 | -43.61393 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e24604a9-de58-3097-8757-ca31a3f72485 | -6.25682 | -42.48646 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cc9dcc08-a177-31dc-a328-3a4077cfe0e4 | -6.26211 | -42.49649 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8a9a5464-407f-3fd9-a426-a28a75d22532 | -9.44138 | -40.37907 | 2025-09-26 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 525c6538-7285-3f27-8666-03ed6640e1d4 | -6.36826 | -35.2145 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 56dbaaa2-c2f3-3741-98d4-58b83953956a | -6.87584 | -44.51437 | 2025-09-26 03:21:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README5.md)
