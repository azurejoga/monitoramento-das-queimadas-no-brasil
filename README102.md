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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0427f056-cae5-35c5-9e6a-dd70ee650f5c | -20.5048 | -57.0861 | 2025-08-30 14:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 970d6da1-c4d2-3c6a-9ce1-c606a32ed35c | -12.8605 | -48.1657 | 2025-08-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c481b03a-e65b-3adc-a5b7-297677bc916c | -6.7814 | -43.7865 | 2025-08-30 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 7803b9aa-7844-3a2d-beec-4673c4c7db17 | -6.2096 | -42.7607 | 2025-08-30 14:00:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 157.9 |
| e606e517-9207-3b3f-a5b0-88761ff9f3aa | -6.185 | -43.3491 | 2025-08-30 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 3ce4e922-cb01-3819-832d-6b7ba84ec462 | -14.0328 | -44.487 | 2025-08-30 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| ea06f11e-681e-3889-b3cf-dd7103073448 | -8.8665 | -45.7335 | 2025-08-30 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a1abfaf1-941d-3e39-9d56-1a042bf3176e | -10.3812 | -57.8245 | 2025-08-30 14:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 59ec3493-8a92-35cd-baf4-918bc2b6ebe0 | -7.6028 | -42.7468 | 2025-08-30 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 6a7f3741-01c4-3c3a-8063-116ecc369c69 | -6.4068 | -45.6004 | 2025-08-30 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1a492017-2259-3f76-a651-a1bacf171d2e | -6.1975 | -43.998 | 2025-08-30 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 65395fa7-53ee-3074-8104-8d08fc31b0c1 | -14.0313 | -44.5578 | 2025-08-30 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 56e251a7-46af-39ab-9a3f-73f45426b718 | -7.603 | -42.7232 | 2025-08-30 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 199.9 |
| dc26bc32-960d-3fe3-83ac-2fee1b81533c | -13.4986 | -46.9517 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| fd7698f0-9f44-3d7b-958e-b82e5aaf0584 | -13.3258 | -46.9107 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 145.7 |
| cb591fba-7b7c-3682-afa6-d87337d51c0c | -14.4674 | -52.0046 | 2025-08-30 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| b6af7279-69c8-3ab5-a82a-5adb88197c16 | -8.8843 | -60.7315 | 2025-08-30 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 7cb7555b-4241-3c8c-babe-aca6df2b1089 | -9.1155 | -65.7699 | 2025-08-30 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.3 |
| dcd38e3f-d684-367d-8e81-12d4781d768a | -10.8161 | -47.1024 | 2025-08-30 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| c2a7f5d7-89a0-3a40-b0a0-ab937a94f98a | -9.4433 | -60.5499 | 2025-08-30 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 5061b1ba-44d2-3833-a826-937bd7e2ab21 | -11.7712 | -44.7432 | 2025-08-30 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d408ddbd-0210-3d7c-9c88-3f6c5b8cc8a4 | -9.0799 | -65.4349 | 2025-08-30 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 96800d83-f07a-3464-bb14-91fdf26d4a4d | -7.2147 | -43.7001 | 2025-08-30 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 148.4 |
| f0f3f8b8-b16c-3830-9308-443b92fefb49 | -7.7257 | -50.2751 | 2025-08-30 14:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e8a9b7f9-89f1-3e28-bf3f-7b60a3118f5a | -14.0118 | -44.5614 | 2025-08-30 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| b10f8ec6-fb30-345d-8012-8ceed9195475 | -7.5844 | -42.7014 | 2025-08-30 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 6419e29a-4142-32b4-abd7-bf6863020821 | -13.4014 | -46.9894 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| cb51fc5d-9cb3-38b4-beb5-ae154572fb54 | -6.407 | -45.5778 | 2025-08-30 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 2ca34df4-d21d-3149-b411-be5717d4a28f | -12.6686 | -48.1704 | 2025-08-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 340.1 |
| 89b2854e-09b8-3d4a-8720-035a38d7cd00 | -9.0614 | -65.4355 | 2025-08-30 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 0e0f5d66-70df-3905-8141-2ac5dae64ba6 | -6.1665 | -43.3273 | 2025-08-30 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 223.7 |
| 002e78e4-57d4-397a-8954-69d75a8fe4cb | -12.8601 | -48.188 | 2025-08-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 911b316d-beb0-3b6b-aa9e-d2fa64b82a08 | -10.8164 | -47.0801 | 2025-08-30 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 223.5 |
| 95f4322c-f1f2-32d2-8e7c-d59e088f54bf | -9.1524 | -65.8061 | 2025-08-30 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 97afd2c4-b25d-3399-bb2f-d3a9b3a5c6ce | -9.0613 | -65.4542 | 2025-08-30 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 19fec2a9-a93f-34e2-8081-29769a339e4f | -9.1378 | -49.623 | 2025-08-30 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8c7c4d56-9414-3221-801f-d53003df4601 | -9.6986 | -47.0555 | 2025-08-30 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 4acd71bc-7a31-3d9a-942a-36deb8859f65 | -6.1785 | -44.0226 | 2025-08-30 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 52f45402-43e8-3589-987a-5287bc66d196 | -8.0818 | -48.4237 | 2025-08-30 14:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| fcf8ed1a-2bb8-3dc0-a50b-a334eb926c8d | -7.0951 | -44.3128 | 2025-08-30 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 30ea6f25-51e2-3a20-a5c9-f17ba836fefa | -6.8237 | -43.3402 | 2025-08-30 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 70e9a02d-7ba5-3988-a450-c1073b614d05 | -6.7724 | -44.6397 | 2025-08-30 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 984ea815-9f13-3058-8a45-4cdd83fb994c | -14.4481 | -52.0071 | 2025-08-30 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 81f25343-bc10-3164-8276-3646471299df | -6.4255 | -45.5989 | 2025-08-30 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 46203c6d-b9ac-35da-adba-aee82c988945 | -14.4484 | -51.9858 | 2025-08-30 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 84f0c716-9c3d-33a7-8beb-2ca94eecd010 | -13.3645 | -46.9047 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 121.3 |
| b94b1b92-0703-3d6f-b4f9-564c4e4878ed | -13.3452 | -46.9077 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 5a2babf6-87cb-3695-962e-2e1f45a923cf | -7.6033 | -42.6995 | 2025-08-30 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| 39aab6a1-0ea7-3a1b-b268-a52d420df54d | -14.105 | -51.7754 | 2025-08-30 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 60c1e92f-446f-3692-97fc-f53d5812a784 | -7.1108 | -44.587 | 2025-08-30 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 07b06c97-ee54-3cac-a2af-7b1c31b98197 | -6.7816 | -43.7632 | 2025-08-30 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 4a02754a-20ac-33ef-bc4c-a6966a82ea52 | -13.346 | -46.8623 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e2824aea-585b-3274-8106-0cb1a16d3144 | -14.0113 | -44.5849 | 2025-08-30 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| a9caa15c-66b0-3d9a-9957-0f3e79e9e144 | -9.4432 | -60.5692 | 2025-08-30 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ae674d3e-772f-3726-991f-9742299248ba | -8.082 | -48.4019 | 2025-08-30 14:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 7525885c-cc43-3d24-b639-c5275fed6e4c | -12.6682 | -48.1926 | 2025-08-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 01768ca3-d2fb-3ff8-879d-6093f2ede134 | -9.1337 | -65.8253 | 2025-08-30 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.4 |
| bbd251ca-530b-3931-985d-c728a0e339aa | -9.462 | -60.549 | 2025-08-30 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| a1b97bcc-893b-3b41-a3ec-ec1381383a2a | -13.3628 | -46.9953 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e0752482-3f64-3e98-8c48-13125a82199c | -11.3705 | -43.5868 | 2025-08-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 7cdddffc-5d3b-3068-9aa3-88944162a8cb | -11.8952 | -46.398 | 2025-08-30 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 48a83576-bef9-3a78-a2d2-d30341d5860a | -11.3521 | -43.5423 | 2025-08-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| b57f4f0c-54cf-3385-b423-d1a58f42ed4a | -11.3713 | -43.5394 | 2025-08-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 78946fc5-48a3-3cd8-ae67-28f2081b5388 | -11.8948 | -46.4207 | 2025-08-30 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| c02b8c03-d823-3d30-9066-1f9eed044880 | -11.8956 | -46.3753 | 2025-08-30 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 73ade508-e15f-3f92-b132-a1c35ac0e360 | -11.3321 | -43.5926 | 2025-08-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 2d17abd1-30c0-3c32-aa05-4d3d243fc309 | -11.3709 | -43.5631 | 2025-08-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 8775f92f-1292-3f9a-ac95-a7022694bcc4 | -9.1338 | -65.8067 | 2025-08-30 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| c1cb54bf-38e7-3c4a-82ad-ea8115fa2325 | -6.1853 | -43.3257 | 2025-08-30 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 219.1 |
| aecc424a-db46-3f0e-b775-0c31b7288ecc | -13.3649 | -46.882 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d59bc867-73ee-3627-8abb-84a28428fa1b | -7.1959 | -43.7019 | 2025-08-30 14:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 849e3c2b-c6df-3f3a-a015-85e062c98a16 | -9.1156 | -65.7513 | 2025-08-30 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| e9d0aeb7-0ce7-3056-aed5-55df141fba82 | -11.0658 | -44.6137 | 2025-08-30 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 7613c050-a2f8-3560-8bb5-d853febef930 | -14.0123 | -44.5378 | 2025-08-30 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 0867c31f-6690-3064-b375-29404bf7da94 | -10.99 | -50.783 | 2025-08-30 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 3bd52c92-7958-3fdd-b152-6fddefe39813 | -13.3623 | -47.018 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ff3c8bc4-1f4d-3bc1-949c-b3c1c76e5410 | -11.0849 | -44.611 | 2025-08-30 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| bc29f4cb-1586-3df0-90ed-960cc6c63ef9 | -13.3817 | -47.015 | 2025-08-30 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 3a976504-361d-31e3-9002-a76d8c12d60a | -11.3517 | -43.566 | 2025-08-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 7ef00c6e-24b0-387d-bf31-2917ca248396 | -7.4466 | -44.8079 | 2025-08-30 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2220ba0b-3f9a-3991-bd1c-69ee9931a7ca | -14.3153 | -51.8756 | 2025-08-30 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5c505938-c293-3d08-a52d-6d13e82fbe1a | -11.0662 | -44.5905 | 2025-08-30 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 47fc2de1-1144-35d2-91ad-06b67b29d851 | -14.0118 | -44.5614 | 2025-08-30 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 255.7 |
| 8d0e5a0c-395c-345e-bafc-74fd9d15df83 | -20.5048 | -57.0861 | 2025-08-30 14:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 090bb446-474d-3afe-b490-c682e5c5be34 | -7.0951 | -44.3128 | 2025-08-30 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 57c63c28-748d-3201-b921-7a5e4d81552d | -7.1108 | -44.587 | 2025-08-30 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 7fe37953-ef38-3036-9f48-c9afed7adaae | -9.462 | -60.549 | 2025-08-30 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 4e54d117-342a-322f-b174-d050e66f66ac | -8.0818 | -48.4237 | 2025-08-30 14:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 5a46f2f1-f4ca-383d-8f07-e0867c37550b | -13.3628 | -46.9953 | 2025-08-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 3a131428-fa97-3b49-bc2b-c0498147ea6e | -6.7816 | -43.7632 | 2025-08-30 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 27b22b4a-f760-3ce6-8403-34bcd217225c | -11.3517 | -43.566 | 2025-08-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 2a82255b-3c8e-360a-89ed-b0785b4a1d42 | -9.4433 | -60.5499 | 2025-08-30 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| dcf13f19-1e63-33f6-aa62-69ebf67d9f95 | -13.4793 | -46.9547 | 2025-08-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| bb403c42-a9f0-3624-bbfa-9b3b186c199c | -6.3817 | -44.3285 | 2025-08-30 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| ddd50111-deab-3f91-9925-13716d4be481 | -9.134 | -65.7694 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 0d272102-b1e3-3e8e-8ca7-8ab28b60c19a | -6.185 | -43.3491 | 2025-08-30 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 5fde06d8-d96c-39ab-b526-aa6cd15abd0d | -11.3521 | -43.5423 | 2025-08-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| e6dd7feb-4c58-3549-ae18-5a487fdf03ba | -9.1338 | -65.8067 | 2025-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 144.9 |
| e095f0d7-e648-3cf5-b116-cf116461d995 | -9.4432 | -60.5692 | 2025-08-30 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 0c74c5e1-1ea8-35a1-bcbb-496e9fcdd1e6 | -11.8764 | -46.378 | 2025-08-30 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |


[Clique aqui para ver as próximas entradas](README103.md)
