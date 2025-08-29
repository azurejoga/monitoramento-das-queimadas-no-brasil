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
| 63be25a6-8780-373e-9367-ec2dbbc76ec6 | -12.9385 | -56.9655 | 2025-08-29 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| f181aaec-0341-3cc5-b1a9-89efe774f845 | -10.8483 | -47.4768 | 2025-08-29 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| fac0c631-0cbc-34c7-963b-e59136713071 | -11.3521 | -43.5423 | 2025-08-29 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 576a1093-62cc-3886-a778-507e3ae97dcf | -6.2741 | -43.8299 | 2025-08-29 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2bbdc475-a7e4-3a57-8f5d-b57b08d2aa90 | -13.5774 | -46.8714 | 2025-08-29 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 362f7b5d-af0c-3d3b-9d2d-51937f5017c5 | -12.8994 | -48.1381 | 2025-08-29 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| eefa8147-79fe-32c5-8d45-7b13db0eca6e | -10.848 | -47.4991 | 2025-08-29 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2b994594-01c3-324f-955b-4b04699fdc49 | -11.876 | -46.4007 | 2025-08-29 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 47246076-c88f-3065-bc35-e2855acfbd58 | -12.9186 | -48.1354 | 2025-08-29 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 7adadaf8-ae2a-30d8-9e12-5a7f32f5443e | -12.919 | -48.1131 | 2025-08-29 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| a2058cb4-531a-3977-b33c-d6515d397f3c | -9.462 | -60.549 | 2025-08-29 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 195.8 |
| c3696891-1bd0-3241-97e7-376b2786dc66 | -9.7728 | -64.2657 | 2025-08-29 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 88261ff0-f52e-37b4-8769-d6dab18570cd | -12.8413 | -48.1685 | 2025-08-29 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| e315f5b1-170e-3e0c-bde7-08e15507371b | -9.1155 | -65.7699 | 2025-08-29 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ed55f2f0-86d7-3675-88bd-e27b95539e15 | -11.3517 | -43.566 | 2025-08-29 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 245.6 |
| 5763f02b-cdab-37dd-b3a6-7ba1cc34e232 | -9.773 | -64.2469 | 2025-08-29 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 6555f318-176b-33a0-9451-b6c2ab4d013c | -14.3296 | -53.3318 | 2025-08-29 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 26460224-f41f-3578-807d-d534bec60ad0 | -12.8994 | -48.1381 | 2025-08-29 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 310cc3c9-38f5-33d0-8e21-ea5e60bfffb4 | -13.558 | -46.8745 | 2025-08-29 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 1dc40b36-305b-3d13-8c4e-ad1a5bd4900d | -13.5778 | -46.8487 | 2025-08-29 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| bca5d9f9-bb97-3495-baa7-3118535334d9 | -10.8483 | -47.4768 | 2025-08-29 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 187.1 |
| fc7b8cb6-d0c5-39f5-b381-67501249567d | -11.5714 | -46.3298 | 2025-08-29 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 8772d178-bff9-3a0e-9457-67ff286911d9 | -11.3517 | -43.566 | 2025-08-29 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 234.6 |
| 5c264e27-f1e2-380d-a51e-caeb16e02999 | -11.3521 | -43.5423 | 2025-08-29 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 214.2 |
| b563f805-1cfc-3cf8-bfce-b723a3d71c2f | -12.0553 | -50.6425 | 2025-08-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 93104437-5481-33ed-b725-1bdb88300ea8 | -9.1338 | -65.8067 | 2025-08-29 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 6842d7b3-5540-3df7-b42b-a734fa3c9415 | -10.848 | -47.4991 | 2025-08-29 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| dec1f835-8446-343b-8f6f-314410d6ea1b | -10.3812 | -57.8245 | 2025-08-29 13:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 49be7408-4afe-3780-9f09-573311c97d31 | -8.4599 | -43.6411 | 2025-08-29 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 939d51b8-3524-31a0-b8cf-780a5b16921c | -12.9182 | -48.1576 | 2025-08-29 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 39e5f868-bdac-3dd2-b80f-790c1a2a1783 | -7.6408 | -42.7192 | 2025-08-29 13:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 172.5 |
| ea8ed71b-8f99-3728-a182-3c6c67bcae81 | -6.2741 | -43.8299 | 2025-08-29 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| cbad0145-320b-3176-abf4-3d159bd5ac2b | -7.6222 | -42.6975 | 2025-08-29 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 36a1cf7e-d58d-3007-a73d-d6303a1f9a1b | -9.4433 | -60.5499 | 2025-08-29 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 567.2 |
| 093f0dd8-2a89-3237-a9e0-e69f0f0b56a2 | -9.773 | -64.2469 | 2025-08-29 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7fc3a479-9739-34cf-ad62-1942f4a7b382 | -9.1339 | -65.788 | 2025-08-29 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 84da55fe-3e08-344b-b696-023d125d54e5 | -7.1108 | -44.587 | 2025-08-29 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| fba22dc1-fe0b-39c0-81f4-b9ccf4e79de8 | -9.4618 | -60.5682 | 2025-08-29 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 0ec5450d-6403-3d2d-94b6-7b8a66cfe0c3 | -15.1225 | -48.1302 | 2025-08-29 13:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 489359be-d32a-3732-bb2c-80413211cab7 | -9.4432 | -60.5692 | 2025-08-29 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 136.1 |
| a4e550e5-bf1c-335f-bcd4-4675bf91ef13 | -12.9379 | -48.1326 | 2025-08-29 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| f2d90724-373c-3429-b2ce-e4c431e14278 | -13.5967 | -46.8684 | 2025-08-29 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 5f9175df-d4bd-3fbb-8a90-4264370200ad | -9.462 | -60.549 | 2025-08-29 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 521.1 |
| 38e3fe93-eb52-33b3-af10-126dca997c54 | -12.0362 | -50.6448 | 2025-08-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 12fb3656-b664-3d15-9100-202b531ed86d | -6.4103 | -45.2387 | 2025-08-29 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 30951b33-3e12-32dd-b861-e54782ef1ac0 | -12.0365 | -50.6233 | 2025-08-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d4621cfe-0bee-37e2-a61b-7358aebbde01 | -10.8607 | -60.8191 | 2025-08-29 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9ab2634b-a2e8-3cdf-9907-58a9cd6bfeda | -14.3299 | -53.3108 | 2025-08-29 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 139.2 |
| df89bc4c-455d-37ed-90df-d958f580e161 | -9.1155 | -65.7699 | 2025-08-29 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ef1eeea2-4068-324a-bc40-273a11063fb8 | -10.6413 | -48.6458 | 2025-08-29 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3e299ec1-9de1-3806-a47e-1a28756b057a | -13.5576 | -46.8972 | 2025-08-29 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c73fc5dd-252f-3447-bd3f-de2847434524 | -13.5774 | -46.8714 | 2025-08-29 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 240.9 |
| 68d36870-194b-39b0-a579-a235e1b7986b | -13.3543 | -54.38 | 2025-08-29 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0ba2e7da-c470-3a58-b07e-509b12d1184c | -10.641 | -48.6677 | 2025-08-29 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 20d4e091-df97-3088-a6bd-91a935b984ef | -7.1106 | -44.6099 | 2025-08-29 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 178.0 |
| b7753f4a-c441-3f9b-aa78-29e11697880d | -6.7074 | -49.4561 | 2025-08-29 13:40:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0e1eee54-5756-3ea4-96d3-c532acd9c4dd | -14.3296 | -53.3318 | 2025-08-29 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| a5fb2b31-d99c-3b48-bcd0-7e1de5f68fe4 | -15.0419 | -57.1852 | 2025-08-29 13:40:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0317c6be-0ef2-3cf4-a976-05524de87130 | -9.1154 | -65.7886 | 2025-08-29 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6204e0f1-214d-3c77-8761-e64d5240b095 | -11.8756 | -46.4234 | 2025-08-29 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| b1e8480e-5df8-3b36-a777-8656944095e2 | -12.9385 | -56.9655 | 2025-08-29 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| c9ca16ec-2c58-3134-971d-c4aab269d312 | -14.3303 | -53.2898 | 2025-08-29 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1f0fe46f-b5bb-33e3-8ac0-0322b7385574 | -6.2743 | -43.8067 | 2025-08-29 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| dc6c64d5-226a-30f4-b9e2-860be9d6e4a9 | -7.6219 | -42.7212 | 2025-08-29 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| f761f32f-94a7-36ed-bc99-6d22df830f02 | -11.876 | -46.4007 | 2025-08-29 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 7811c996-16bb-3848-9ac2-4f63216fca1a | -14.0328 | -44.487 | 2025-08-29 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 24a4f71d-7a97-3c62-8ace-23fbc3d09873 | -1.7507 | -54.513 | 2025-08-29 13:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| cbcdea4e-16a5-314f-9b9d-42caf6d8a13f | -9.7916 | -64.2461 | 2025-08-29 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 94773e58-b413-39ba-8a72-1db028ea69c5 | -14.3532 | -51.9132 | 2025-08-29 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| b6373e8d-6f3d-331a-99e1-e4d94489f0a9 | -9.7728 | -64.2657 | 2025-08-29 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 36974b20-8d7b-3245-8391-e618595e367b | -7.6183 | -46.2392 | 2025-08-29 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b95bc772-7b4d-32d2-8393-a5bb4dba2a05 | -12.9186 | -48.1354 | 2025-08-29 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 5bd5091f-6a0d-3915-9cd5-f8ef8e1a23a5 | -12.0635 | -46.6229 | 2025-08-29 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8b51c9d9-985e-31f0-81f2-0bb12543847f | -9.5447 | -45.8842 | 2025-08-29 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 8a2c431f-25d6-337a-b961-735a40805545 | -10.3812 | -57.8245 | 2025-08-29 13:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| cfb9d379-2dfd-3b61-9414-1fd2fe9e2b70 | -12.9182 | -48.1576 | 2025-08-29 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| eaf6ea13-2431-3303-8fa1-5d513cb2242b | -13.5576 | -46.8972 | 2025-08-29 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c81fc2f3-e162-3ca3-87ff-baa7abc16d3a | -6.9867 | -59.3354 | 2025-08-29 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 720786a0-9c2e-3ec6-8c01-b28943fe8608 | -7.6408 | -42.7192 | 2025-08-29 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 201.9 |
| 1764de9d-21e5-3261-9afa-94cef4855c1b | -6.3024 | -44.7699 | 2025-08-29 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 6508e5c7-b653-3faf-a404-53dbc6574e7f | -6.19 | -44.7788 | 2025-08-29 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| c6ff9485-6023-3d41-817a-07c168a9f11f | -9.1154 | -65.7886 | 2025-08-29 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0bc50fc4-9f6e-3007-9009-781b18af9e98 | -11.0826 | -44.7503 | 2025-08-29 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c016d155-46b4-388c-9f69-8ddd3832c237 | -11.5714 | -46.3298 | 2025-08-29 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8bdc9c5d-80e6-3cb0-9269-a513437a9e3f | -9.1155 | -65.7699 | 2025-08-29 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 53ae5f46-337f-335c-b56d-2b8f2278a499 | -7.6219 | -42.7212 | 2025-08-29 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 4a47dbac-bb8f-35f3-9268-28e7320ec55c | -12.8413 | -48.1685 | 2025-08-29 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ddb48d3a-60fb-3636-a3b5-95a2379b3ce3 | -10.829 | -47.5014 | 2025-08-29 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 444f49ef-9f16-3529-a5af-4529228f5f98 | -14.3296 | -53.3318 | 2025-08-29 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 180.0 |
| f4dac65f-8fd6-39e7-a8d9-921b7b1dfbc0 | -11.3517 | -43.566 | 2025-08-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 255.6 |
| c0768956-2717-3012-ad0c-8e3e2d66a62d | -12.9186 | -48.1354 | 2025-08-29 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 40850ae3-c6cd-37c3-8f7f-dd4f7aa5d78b | -6.3881 | -45.6018 | 2025-08-29 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 714d9f45-5efd-372b-b232-b6fc00bb8ce6 | -14.3489 | -53.3294 | 2025-08-29 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 4e033b79-31df-307d-8df8-8604e23fbe79 | -11.3325 | -43.5689 | 2025-08-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 406b02de-6efa-3afa-8ff6-7bb189000784 | -10.8483 | -47.4768 | 2025-08-29 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| c5231aad-d4e3-3a17-aefa-cd5c6bc4f4c0 | -10.848 | -47.4991 | 2025-08-29 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 28136243-c2ef-3e18-a75a-b9b10f70003d | -13.5778 | -46.8487 | 2025-08-29 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 77c45070-1c63-3333-8b75-c96ac5d18c55 | -7.1106 | -44.6099 | 2025-08-29 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 61f663d4-0c09-3fc5-b0f1-58a6ce3a6472 | -11.3521 | -43.5423 | 2025-08-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| ebb3f41b-9cdc-3cdf-afc1-c5c43f23a4e7 | -13.558 | -46.8745 | 2025-08-29 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 164.1 |


[Clique aqui para ver as próximas entradas](README96.md)
