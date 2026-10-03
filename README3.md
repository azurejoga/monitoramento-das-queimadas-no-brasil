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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89a32ca4-c038-363e-bccb-3cee810bab81 | -11.7935 | -43.5215 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 44288bdc-6783-32e9-a6f0-78e7a15d0484 | -2.9265 | -54.1104 | 2026-10-03 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 544136b3-500c-317e-b6cb-63ee323af262 | 1.7671 | -55.6056 | 2026-10-03 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 0bb4d7b1-a5f1-3189-bf6a-e33c02565133 | -11.6977 | -43.5128 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 8ead6ab2-62fe-3e4d-bb34-e324d36e1d46 | -3.1655 | -54.0844 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 837d4d73-b1e1-399d-893d-603b28a18303 | -2.9042 | -45.3944 | 2026-10-03 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 56a79dbf-c015-303a-b513-25fe8de7395f | -3.1838 | -54.104 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| dae27d59-0b71-38ef-aeb0-855a674c93d9 | -5.7357 | -43.2682 | 2026-10-03 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 7df627a1-58bc-3c65-a849-7642f58e9a09 | -13.5365 | -44.1044 | 2026-10-03 00:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| de1b9281-6a78-3c37-b48d-47cd67d079e8 | -11.6391 | -43.5692 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 2322d4aa-13fb-376b-82dd-d4318a29b46c | -3.1116 | -53.7436 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c8566f92-19d4-3bea-a18b-43fe29a46d69 | -3.1299 | -53.7431 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 227.4 |
| 430e5251-fa45-3033-8f67-69816f9c4ccb | -11.8127 | -43.5184 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c42b6904-5b66-36c9-8975-55cc32d5dfaa | -2.9266 | -54.0903 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| b4af5155-1db7-382b-a0a2-f560ec7ab788 | -3.1116 | -53.7234 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0c592e70-4313-3c02-b8db-281ab6dfee44 | -3.1839 | -54.0839 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 9eec17bc-fccd-3119-b019-6a802d28d686 | -11.4123 | -43.3913 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 46ac2ab1-c069-39af-9086-c6d6f47ca25a | -2.9266 | -54.0903 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| abfd1ea9-f347-3331-b753-f653def80e4e | -3.1483 | -53.7426 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 201f8519-984a-3c9c-a058-cdd03b26ec2a | -2.8897 | -54.1313 | 2026-10-03 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 13caa955-80ec-377a-a811-ae1a488c78ff | -3.13 | -53.7229 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| df4232a7-62a7-390b-bdc3-4fcab42a25fb | -2.8856 | -45.395 | 2026-10-03 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 32598433-a0d1-35f1-8900-c88f991eec41 | -1.2107 | -47.7735 | 2026-10-03 00:30:00 | GOES-19 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 7d350dd2-0077-3a88-92d4-6724fe456705 | -3.2767 | -53.84 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 485e70eb-6b9f-3a61-bd31-433c36b6408f | -3.1116 | -53.7436 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| ba8ed9fc-feec-3ab7-8710-8ee25851349c | -11.7174 | -43.4861 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 6b1f0a5d-4732-3dda-b9f2-19b210e935f8 | -1.1922 | -47.7738 | 2026-10-03 00:30:00 | GOES-19 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| da73f6e2-7c62-3aa0-87a9-b53c8638a537 | -5.7378 | -45.1307 | 2026-10-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ec716025-ed34-3506-a2f0-3a074782f304 | -2.9042 | -45.3944 | 2026-10-03 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| a93b1882-1552-3cdc-ba49-f7b5ff466be8 | -3.1655 | -54.0844 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 8cdcf73e-276c-3407-9bed-97751f61ea1d | -3.1299 | -53.7633 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| fa36f75d-9578-36e7-af56-95f3d3e7e56a | -5.9569 | -43.67 | 2026-10-03 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a5273a2c-4d1a-36b9-8ecb-b81a1f29ae3c | -5.7355 | -43.2916 | 2026-10-03 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 578d7773-c8d9-3015-b4e3-8c91f8e91e5d | -6.7401 | -44.1371 | 2026-10-03 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b08316dc-2836-357f-9c44-118033584212 | -11.6981 | -43.4891 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 0a899ffe-91ee-35b3-8cdd-adfdef82dfe1 | -11.8127 | -43.5184 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 3bdea9f5-ba37-389c-841e-883ef5ef0d82 | -10.9879 | -59.1393 | 2026-10-03 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 50b8be5f-5be5-31f0-877a-447760b203a8 | -3.1299 | -53.7431 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 196.5 |
| 3d824e47-21cc-38a8-955b-c62032970701 | -11.7935 | -43.5215 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| bf97b06b-8eb7-38e0-99d3-3718f040e80c | -6.1295 | -47.3323 | 2026-10-03 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2dedccf7-f341-3531-8a16-314589b5c0f5 | -11.0067 | -59.1381 | 2026-10-03 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| f65f9957-11a2-3ede-a5e2-44e1603a1a7b | -11.793 | -43.5452 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.3 |
| fb042340-0694-3c0f-a9cb-34f11d78fd87 | -4.5706 | -46.5907 | 2026-10-03 00:30:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| adb419ae-4f44-3952-91c5-57775cb8ca24 | -3.2768 | -53.8199 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1711dee1-897d-3517-a020-d92e1290c955 | -11.6391 | -43.5692 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| e85db488-2362-383e-84ad-a560637ee3bc | -11.7187 | -43.4148 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 134337ab-73f1-3a63-b461-03072017aa98 | -9.711 | -57.4548 | 2026-10-03 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2daca988-f615-3117-ba7a-aa6e18f4fa47 | -3.4093 | -52.8436 | 2026-10-03 00:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1835fd7b-98c0-38b5-b7a0-2680477a0064 | -5.9571 | -43.6467 | 2026-10-03 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 285d6dac-28e7-3409-b282-da7ce8d5b098 | -11.4695 | -43.4062 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| f0cf1159-d546-3839-a424-5486d92e4ec9 | -5.9381 | -43.6714 | 2026-10-03 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ae4eee80-9a12-3836-a9ef-ad28f3d0d747 | -13.5365 | -44.1044 | 2026-10-03 00:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 1dc6b2f9-1d37-3fb1-9fb6-41428d3e6f46 | -5.7376 | -45.1533 | 2026-10-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 7b57c74f-df7f-3580-af8a-88e50163861b | -10.9881 | -59.1197 | 2026-10-03 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4d1dcaca-7001-33c9-80ae-8cc62baa52b7 | -2.9082 | -54.0907 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| bb4b5881-f2a3-3db2-a002-63ff8fbb3853 | -2.9041 | -45.4168 | 2026-10-03 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| f167141f-972d-30d9-9d78-d4eb21628aa3 | -11.6977 | -43.5128 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| e2b5330e-8b52-3574-9f0d-96ff29fc273c | -5.9384 | -43.6482 | 2026-10-03 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 67e9902b-f38b-39e4-b889-ea035eb98188 | -2.8898 | -54.1112 | 2026-10-03 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 1f635a12-2eac-3086-9eb2-1892429b6385 | -2.9265 | -54.1104 | 2026-10-03 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 852fbafa-3e5b-3444-a81d-0a97a75375f3 | -6.9297 | -49.6112 | 2026-10-03 00:30:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 4c4a5abd-2fd6-3a6d-b374-6d14828ffaae | -3.4093 | -52.8233 | 2026-10-03 00:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 698f9fa9-a564-3e2e-8530-607109b74115 | -3.2212 | -53.9422 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 61e88d79-c0df-37b3-b9ca-6eefaae585ed | -4.4507 | -47.9112 | 2026-10-03 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e77b7399-be2a-3fe4-9ead-61eedcf8a5d3 | -11.4887 | -43.4032 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 0ff82dd0-48bd-33db-b1e5-1d414106b9a2 | -2.8855 | -45.4175 | 2026-10-03 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 159.6 |
| a7ff0439-95d3-30db-9944-e7892717f2f8 | -4.7434 | -43.2679 | 2026-10-03 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 03893fe5-f330-31e0-b0ae-eee91dea6a1f | -11.4315 | -43.3884 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 9e8ad640-c3f6-35ef-b1bf-57012945b468 | -12.8676 | -44.6878 | 2026-10-03 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 7f5094db-b67f-3496-a38a-1d1c1590943b | -11.8123 | -43.5422 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| cc902931-c0db-3981-909a-7823ae768f5d | -2.8897 | -54.1514 | 2026-10-03 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 28362875-73a4-34e4-b85f-b38bfc2aa11f | -12.8681 | -44.6644 | 2026-10-03 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6fbcc058-4370-3af5-b3b7-8a8126e41df3 | -4.4506 | -47.9329 | 2026-10-03 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9c816e23-ac9a-3f96-87ad-16082b4c9436 | -8.852 | -66.7827 | 2026-10-03 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| fc449e93-24ed-39d5-9a30-a54ca1edc764 | -6.9295 | -49.6325 | 2026-10-03 00:30:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5323a495-ce21-3408-9018-1f6e2e9f2f8d | -5.6134 | -44.3876 | 2026-10-03 00:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 4ea26252-366a-363d-afe6-1739fc7dc1cc | -11.8118 | -43.5659 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 42c213a2-c16b-3baf-8010-cec51b9f0a95 | -3.2951 | -53.8395 | 2026-10-03 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 9858a521-dcd1-3cb1-b71a-986dbaa421a6 | -4.3588 | -47.7636 | 2026-10-03 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 84390802-6a0a-3090-adac-a4f18ccfcfba | -4.3587 | -47.7853 | 2026-10-03 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| d73f108c-1c10-3e07-86b8-676edb58d38f | -11.7169 | -43.5098 | 2026-10-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 7b1e7da1-916d-3110-9c20-8f2508aa3b48 | -5.6136 | -44.3647 | 2026-10-03 00:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 11036efc-7a74-3ccc-b032-99f732af0ba7 | -1.1045 | -54.1339 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 733e3d02-4cea-37a3-bc12-8c3a007bb794 | -10.9951 | -59.123501 | 2026-10-03 00:30:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e19cd078-d512-3c52-8d42-38ca58175a5c | -11.4671 | -43.380798 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c6be807-881e-3af8-aa5b-76fb49853e10 | -2.5426 | -57.394001 | 2026-10-03 00:30:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6911c3fd-0a26-35d6-8742-1a1ef3b06aee | -2.894 | -54.116402 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 154d80a4-732d-361b-9210-6095ab09a8fe | -1.272 | -54.554401 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b849047-f715-34a8-9c11-1d6ff6091ee1 | -11.4574 | -43.3834 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9716f9d6-e058-3b18-b7d8-8895928b5a23 | 1.7897 | -55.598499 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bbe1703-ee85-3282-87c6-45d4b55893b0 | -10.9929 | -59.112598 | 2026-10-03 00:30:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88da03e2-ba00-3e90-a7b0-217d06150b2d | -11.419 | -43.394001 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f29113e5-d0bc-32c1-a831-d4e3c70ec919 | -2.4597 | -56.0662 | 2026-10-03 00:30:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2972d54-d80d-3f3d-a593-a2bc8f2006b0 | -2.8842 | -54.118599 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 873faef4-606e-3229-bd5c-104c49abbc25 | -4.7902 | -55.7061 | 2026-10-03 00:30:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 056a043d-355a-3673-b36a-fd6fe9768600 | -2.4855 | -56.089001 | 2026-10-03 00:30:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17946e46-6d84-3754-9ce1-baa535287b67 | -3.1268 | -53.735199 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbe4967f-ceb1-3c1b-8450-7ace9e67d3cc | -5.7337 | -45.053299 | 2026-10-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28eee9cc-dcaf-33e7-a12f-dc10b3d4fa8d | 1.9059 | -55.814602 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e91efa5c-a251-3b66-8fe6-bc285b45e85d | -10.9854 | -59.1255 | 2026-10-03 00:30:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
