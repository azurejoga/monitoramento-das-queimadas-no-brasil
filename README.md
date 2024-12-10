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
| 16f80775-b3e4-30c8-93a6-3cc80ae7062d | -5.9183 | -48.0667 | 2024-12-10 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 9abca23a-c6fc-3f43-8747-ef3cbb32fd99 | 2.4159 | -60.6426 | 2024-12-10 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 3f369e4a-e047-3ab9-8289-614b342807f3 | -3.631 | -52.6737 | 2024-12-10 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| e85aeae0-8099-345a-b75f-0983397ecdb2 | -13.9383 | -44.3628 | 2024-12-10 00:00:00 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| d74e0047-8c78-3a61-ab81-92b5e9a59a82 | -1.6404 | -45.899 | 2024-12-10 00:00:00 | GOES-16 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| bd8d593d-f57c-31c0-bf25-bcea2e71a34f | -3.843 | -50.6627 | 2024-12-10 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 151ddf13-dde3-3ddc-8d38-da3d830a02a9 | -5.9371 | -48.0437 | 2024-12-10 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 925e6175-104b-3aea-a52b-cc42cf459d54 | -13.206 | -56.8807 | 2024-12-10 00:00:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 185ac974-2578-3862-8725-2d60ff6ec56e | 2.4341 | -60.6613 | 2024-12-10 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ba1660b4-71d6-329b-9c6c-e92381c92679 | -3.0921 | -54.0662 | 2024-12-10 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1ca11fdf-3eec-3aa9-92b6-104e08da8e8d | 2.4341 | -60.6424 | 2024-12-10 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| b942bf35-0bbd-3db4-8df4-bd529f34eeb9 | -11.5426 | -56.4438 | 2024-12-10 00:00:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 6687125e-2e64-3c03-af23-79149c8b0773 | -2.219 | -44.8068 | 2024-12-10 00:00:00 | GOES-16 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| b9fa7c0f-73b9-37c8-b6a4-51ed63fb5894 | -4.2726 | -46.6723 | 2024-12-10 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2cfc577f-c855-3a9f-b5bc-75a1d264f5b4 | -2.9859 | -52.8554 | 2024-12-10 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 326fc7a3-798c-3214-a901-b797973eee15 | -3.0043 | -52.8549 | 2024-12-10 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| d29617fb-21e4-3da7-9750-5fe0e0d57d35 | -2.8199 | -52.9816 | 2024-12-10 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 83e77452-ad75-36a8-a51a-fde08bcb7c2f | -2.986 | -52.835 | 2024-12-10 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| ad7acb19-90e5-3f5c-9fed-9ae90d99a37f | -2.0872 | -45.3519 | 2024-12-10 00:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 21897212-a0b6-3dde-a7c0-aac2fc16f90c | -2.82 | -52.9613 | 2024-12-10 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6904acad-be10-3086-8a86-805b3aa2a6a3 | -3.1105 | -54.0657 | 2024-12-10 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 310c7952-cc39-3ebd-b07f-1daa5546ded7 | -2.9119 | -52.959 | 2024-12-10 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| dda92887-67c8-3894-8dd4-90d57f39907b | -5.9185 | -48.0449 | 2024-12-10 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 4529268e-e1eb-39ae-b3a9-c4b2da88e505 | -3.0547 | -54.2478 | 2024-12-10 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| fb0619dc-5a3f-35c9-8034-2747ffe26078 | -3.1104 | -54.0858 | 2024-12-10 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c008768c-2755-3329-9802-c7569338ce9b | -13.9389 | -44.3392 | 2024-12-10 00:00:00 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| cf71f7ad-5b14-382a-aa41-8cb8350506e7 | -3.5837 | -43.5413 | 2024-12-10 00:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 8c9217a3-e186-30f5-b4ed-5bb2542929ab | 2.4341 | -60.6613 | 2024-12-10 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5501c71d-766f-39a1-aa9c-fce8e5b1501f | -3.1105 | -54.0657 | 2024-12-10 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0b769d5e-81b0-348c-8f30-10f3c90ec47b | -3.0547 | -54.2478 | 2024-12-10 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| e5100bce-03b2-3060-87d9-fb745fc9f620 | -2.9859 | -52.8554 | 2024-12-10 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 262.0 |
| 0652c6ce-fd46-3bb1-8234-30639e039182 | -3.0921 | -54.0662 | 2024-12-10 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bdf0ac41-cb4c-38cf-9a9b-556fe7e4f517 | -4.2726 | -46.6723 | 2024-12-10 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c423b52d-85d0-329a-9129-2d2aca123f98 | -13.206 | -56.8807 | 2024-12-10 00:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 98612afc-a7e5-32a8-acac-48c22fbe08ee | -2.986 | -52.835 | 2024-12-10 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 6e57fb48-c41f-3f22-9243-31e7a67b1a7f | -5.9183 | -48.0667 | 2024-12-10 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| f83a27ff-d0c6-3c6b-8267-df111e69b9ae | -4.2725 | -46.6944 | 2024-12-10 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e4ec3099-9763-39cf-a637-10c183dcbbf8 | -13.9383 | -44.3628 | 2024-12-10 00:10:00 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d2182114-1b27-3446-8463-21013b6ff813 | -6.9158 | -43.5185 | 2024-12-10 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6e8a4551-ac73-3902-ae49-88446cb8196d | -3.5837 | -43.5413 | 2024-12-10 00:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 2a141b30-22b5-3ab1-9065-193d67508234 | -2.8199 | -52.9816 | 2024-12-10 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| a996400c-c88a-3542-95a7-3176b82174c7 | -3.0044 | -52.8345 | 2024-12-10 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 3f886880-ee2f-33a6-b598-bdbd28d4de24 | -2.9119 | -52.959 | 2024-12-10 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| d00d7079-494c-368f-8628-1b3ad81bfa43 | -5.9185 | -48.0449 | 2024-12-10 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| e7f46845-f4e7-3459-98ad-75de0aa7a71c | -12.8667 | -58.2106 | 2024-12-10 00:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f0601e2d-aa73-3edc-9892-f7c68349ca6e | 2.4341 | -60.6424 | 2024-12-10 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 03e79a76-8f37-3688-ba82-ac1da85d0f34 | -5.9371 | -48.0437 | 2024-12-10 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 58bd05ad-7d13-3069-b11c-d0b2798f8d2f | -3.0043 | -52.8549 | 2024-12-10 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 182a8716-0bcb-3c6f-95fb-c1a4f24dbaec | -3.0547 | -54.2478 | 2024-12-10 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1c25767e-f77c-3a46-b824-6defcb977feb | -5.9183 | -48.0667 | 2024-12-10 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 6afdf0e0-8fd9-3167-9910-fcb0309cc537 | -3.5837 | -43.5413 | 2024-12-10 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| c117fe13-a547-3117-bc11-f807ba8418a0 | -5.9371 | -48.0437 | 2024-12-10 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| f9ecedfb-091d-3bf5-b431-73391f4355a6 | -3.1105 | -54.0657 | 2024-12-10 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9be16186-bcea-30d2-94be-35ec00d5e05d | -2.9859 | -52.8554 | 2024-12-10 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 231.1 |
| 19234519-a29e-34cb-b47a-c81eba39b95c | -3.0043 | -52.8549 | 2024-12-10 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| debc14ab-74bd-3e4e-ab4a-af372c1adbc6 | -3.0044 | -52.8345 | 2024-12-10 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 84d6ef34-62cd-3333-9f81-20f6aae160c3 | 2.4341 | -60.6424 | 2024-12-10 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c4678664-5970-3a44-a20d-76100ed37370 | -5.9185 | -48.0449 | 2024-12-10 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 01ecae6e-db9f-3db2-ab43-80d5b5dc558c | -2.986 | -52.835 | 2024-12-10 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| c8d853f9-af37-3f78-aeb0-bab539d6c2f0 | -6.9158 | -43.5185 | 2024-12-10 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 312818e8-f9f0-33fa-9f8a-131cfc667832 | -4.3959 | -47.7618 | 2024-12-10 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 65b56efc-37c5-3516-b6e1-88c1e6c219d3 | -2.8199 | -52.9816 | 2024-12-10 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| f9fde6ec-c63d-3140-af56-4db7907aa768 | -5.8998 | -48.0461 | 2024-12-10 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a4e54436-9691-318f-9e7f-b237e5ee0ab9 | -2.9119 | -52.959 | 2024-12-10 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 33513cca-3f2b-3df6-8e4a-041d4c85c99c | -2.9303 | -52.9585 | 2024-12-10 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 41df4fda-5194-36f1-a617-2aee52e75d8a | -4.3961 | -47.74 | 2024-12-10 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4a760396-6937-39f1-8bff-7ddb0774d065 | -6.9158 | -43.5185 | 2024-12-10 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| bad262c2-f836-39f3-8b37-ffad2886bcf1 | -3.5313 | -54.5957 | 2024-12-10 00:30:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d540f6dd-368c-366c-a908-d23f7e727676 | -5.9371 | -48.0437 | 2024-12-10 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 8e05387c-ae7f-3d0f-a384-21d0ad475f1c | -3.0043 | -52.8549 | 2024-12-10 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| df61b70c-cd5c-3ec9-a61a-3b9e1e5fff33 | -4.3959 | -47.7618 | 2024-12-10 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 422cf070-eb82-3ba0-ae85-38586daa5b23 | -2.986 | -52.835 | 2024-12-10 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| f4fc073d-1c09-3b92-bb57-f25733903255 | -2.9119 | -52.959 | 2024-12-10 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| f40e884f-aafe-3bc5-bd42-6601e651efa8 | -3.0044 | -52.8345 | 2024-12-10 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3f521527-3e04-3748-8f1c-12d90ed3de00 | -6.9161 | -43.4952 | 2024-12-10 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b77a5c88-dcfb-3806-9b66-6a539f52d9f1 | -5.9183 | -48.0667 | 2024-12-10 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 9efba962-b3be-3bee-9efb-927f37e55e79 | -5.9185 | -48.0449 | 2024-12-10 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 665c955a-135b-32ed-a4ee-40cae8a1520e | -2.8199 | -52.9816 | 2024-12-10 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| aa59a049-162d-3cb0-9918-89c1d7968891 | -3.0547 | -54.2478 | 2024-12-10 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| be75175a-6a7b-30d8-83fa-bcca26e3b0b2 | -2.9859 | -52.8554 | 2024-12-10 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 172.7 |
| 19b240ab-d656-3a14-8689-d26ed547504e | -12.3664 | -54.1534 | 2024-12-10 00:30:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9fa5923c-3cec-3cb9-b915-7970c0e46bf0 | -5.9183 | -48.0667 | 2024-12-10 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e379bc53-535f-3a87-b7e0-94d68f39b1eb | -2.9119 | -52.959 | 2024-12-10 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 039ea710-5779-3e33-aa61-451bb6e3c362 | -3.0547 | -54.2478 | 2024-12-10 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4fa66343-b719-3ece-9e6a-54c15bbc0447 | -3.1105 | -54.0657 | 2024-12-10 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 910c5747-bc33-3ee0-b0cf-5aa12d1f3228 | 2.4341 | -60.6424 | 2024-12-10 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b0b1ea6e-336e-3012-9b07-adf0b3f525b9 | -3.5313 | -54.5957 | 2024-12-10 00:40:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 76234e9a-6707-30a9-9488-9870939323ff | -3.0044 | -52.8345 | 2024-12-10 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 3e485b06-1fd1-39d0-9d01-0964d4a8df6c | -3.0043 | -52.8549 | 2024-12-10 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| e0eef2a5-5e7f-3bb7-90f1-ef9b87383458 | -6.9158 | -43.5185 | 2024-12-10 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 800fd966-a239-316e-a0b1-526649aadf26 | -2.9859 | -52.8554 | 2024-12-10 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 191.0 |
| 64008d93-46d6-392c-b8ba-fff2afacbd95 | -6.9161 | -43.4952 | 2024-12-10 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 058e4dc3-8ab2-39ae-8159-149616b492c7 | -11.5426 | -56.4438 | 2024-12-10 00:40:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| af52e414-d59f-3a55-87bf-b6e3407fd6ac | -5.9185 | -48.0449 | 2024-12-10 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 0bef5b99-bb16-38ed-bd22-f2c0bff8fef9 | -5.9371 | -48.0437 | 2024-12-10 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| f322fdcc-8b7e-3df5-9356-0cc7c3e922ba | -2.8199 | -52.9816 | 2024-12-10 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b6d32990-e1ef-38d8-9eb6-391446469ead | -12.3661 | -54.174 | 2024-12-10 00:40:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| bc27ed7a-2408-3a45-8caa-a0d8e9eb9e63 | -2.986 | -52.835 | 2024-12-10 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 932857f4-8898-38b2-a2d6-73516fab4e68 | -2.986 | -52.835 | 2024-12-10 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 02a29a41-f5fe-3729-b117-c16a59274398 | -2.8199 | -52.9816 | 2024-12-10 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |


[Clique aqui para ver as próximas entradas](README2.md)
