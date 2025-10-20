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
| e080a38b-32ed-3786-9766-23909df365ca | -14.206 | -51.5059 | 2025-10-20 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1723f8c7-5fc1-358c-ac77-e7bc114745aa | -2.2527 | -51.9313 | 2025-10-20 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 519b8a8d-6979-3a44-a6aa-aed6450411a7 | -9.6401 | -64.7411 | 2025-10-20 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 3d5fd99e-1cf0-3697-bb7a-4cd427aee662 | -14.2056 | -51.5273 | 2025-10-20 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 309.7 |
| 85de6402-afb6-32ee-9522-2cce3552f93e | -11.6497 | -44.0384 | 2025-10-20 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 2726a126-bd73-3833-a4eb-0e60f42009c5 | -2.2527 | -51.9108 | 2025-10-20 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 3570024b-aea3-3b51-94a6-f062ff8be9f1 | -11.6501 | -44.0149 | 2025-10-20 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 7a67039b-25c6-3bc0-beb0-37834e943646 | -2.9128 | -52.7146 | 2025-10-20 00:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| da8019a4-c8e9-380d-94f3-d2fd18a90ec0 | -3.3279 | -50.2195 | 2025-10-20 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 097a05ae-5bce-3cea-97c1-dac52b186e8b | -4.4066 | -43.3118 | 2025-10-20 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 0381d8c1-75fe-3d39-99d6-b914350b0878 | -8.0676 | -48.0112 | 2025-10-20 00:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bc01ff7d-efab-3864-b3de-ab3adc8d912f | -2.2711 | -51.9104 | 2025-10-20 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f17c52c4-6101-32f9-ac16-e33fea284b3b | -8.4345 | -44.1324 | 2025-10-20 00:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 98909272-e197-39e6-8d0e-0c1551a6db62 | -14.1863 | -51.5299 | 2025-10-20 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 7fa53b9e-62ff-3bf9-9893-49588e6c803f | -13.0168 | -43.9823 | 2025-10-20 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| dd47344c-cc04-36f2-8670-2de3d329492b | 1.0763 | -51.2892 | 2025-10-20 00:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d2d4eaf3-09c7-3bbd-9651-032c3fd07f4c | -11.6305 | -44.0413 | 2025-10-20 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 4fa061ec-2a90-3e52-974c-2cdb2959eb7d | -10.8937 | -48.2442 | 2025-10-20 00:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b6307db8-f7b9-34d9-87b1-782e2452df88 | -14.2052 | -51.5488 | 2025-10-20 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a34692cd-5137-3399-b010-3a4e993bb5e7 | -13.0173 | -43.9586 | 2025-10-20 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 0102b448-ccae-3ddd-b2bd-10f4e305d064 | 1.0763 | -51.3099 | 2025-10-20 00:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 9594c8ec-f4d2-386b-954c-7a3dea7d9f50 | -2.2343 | -51.9111 | 2025-10-20 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 3a941385-d9b6-3612-9be8-ad77022b18dd | -14.2249 | -51.5248 | 2025-10-20 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 96f822ed-cc44-3098-8d2c-0487deb0180f | -13.0439 | -48.6484 | 2025-10-20 00:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 486977cd-be25-3969-9d6d-76b781afe304 | -10.0201 | -47.0637 | 2025-10-20 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| dde1dc8e-bf64-3a2a-85c8-0baefb9f15bc | -10.0011 | -47.0658 | 2025-10-20 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 5565ca46-7c26-3edc-90ad-04e3f1b8f9fd | -13.0173 | -43.9586 | 2025-10-20 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 22e3d627-84e7-3908-be65-0e40758e1e5b | -8.0676 | -48.0112 | 2025-10-20 00:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 0e547565-c905-3473-98c1-71ab6db79778 | -10.0014 | -47.0435 | 2025-10-20 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 8c3cefcb-85ea-39e0-a215-8ab84b33d47d | -9.6401 | -64.7411 | 2025-10-20 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c39aebba-c6a3-3d13-8b38-4f2647acf791 | -14.2056 | -51.5273 | 2025-10-20 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 8e19cc60-e29f-3e43-8a11-120736c61720 | -14.1863 | -51.5299 | 2025-10-20 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| f43c8e89-fc21-38de-a813-b8659dd2cc5d | -2.9128 | -52.7146 | 2025-10-20 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 7a3e7e45-8808-3aab-91c7-7dd91d190a55 | -4.4066 | -43.3118 | 2025-10-20 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5cefee15-2aac-3282-beaa-269d7591b0bc | -2.2527 | -51.9313 | 2025-10-20 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| cae94b51-b8c7-35fa-a45a-94a4724382fd | -2.2527 | -51.9108 | 2025-10-20 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 181.9 |
| fd5e7e8c-bcd7-3c72-bdc0-cfa2efabd1cc | 1.0763 | -51.3099 | 2025-10-20 00:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 82.9 |
| bcc39176-5f98-327b-9746-29d890366b0f | -13.0168 | -43.9823 | 2025-10-20 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 1b84a584-b51d-327b-9ada-a06782a2630e | -10.0204 | -47.0414 | 2025-10-20 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 17cc85d0-7571-368a-8903-22b401f0903b | -14.206 | -51.5059 | 2025-10-20 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| a364e71b-f35f-3663-9dfd-e0addea10193 | -8.0674 | -48.033 | 2025-10-20 00:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| fa3f1691-ee50-35e2-b8eb-b4685e772b0c | -2.2343 | -51.9111 | 2025-10-20 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f896c241-05c4-30ce-a9e4-aa0207f179a3 | -2.2527 | -51.9108 | 2025-10-20 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| fc638289-91ee-3076-9f9e-25ec97f721d2 | -13.0173 | -43.9586 | 2025-10-20 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| f24d0161-cdc8-36fc-9b7f-244cc56a7ca2 | -2.2527 | -51.9313 | 2025-10-20 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| e4a46167-2475-3a3b-bed3-7a0763ab6d1c | -2.2343 | -51.9111 | 2025-10-20 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| acd132e0-f4e9-3e6f-8b31-058d350bd65d | -10.0011 | -47.0658 | 2025-10-20 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b3c5d4e3-2060-3ad8-8190-f29dfcda4d06 | -4.4064 | -43.3351 | 2025-10-20 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 91ac8883-a5b4-3f97-acd7-22da0bfede0e | -8.0676 | -48.0112 | 2025-10-20 00:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a3e315dc-cb73-3a61-ad30-e8ff30ff66f6 | -4.3879 | -43.3129 | 2025-10-20 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 380086e0-b390-3cec-a9bb-ec1853eb52af | 1.0763 | -51.3099 | 2025-10-20 00:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c5f43e68-979a-3bb4-8d24-46d550d5d2e5 | -9.6401 | -64.7411 | 2025-10-20 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| af8464e8-df8a-3ed8-81ee-825037f0b5d4 | -10.0201 | -47.0637 | 2025-10-20 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 82edec8d-98de-385b-839a-94c29b994c04 | -4.4066 | -43.3118 | 2025-10-20 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 6158edb3-d531-3366-9482-2331994aeacb | -10.0014 | -47.0435 | 2025-10-20 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| cd2a1e62-c774-3b61-bff5-e7e4a90344c2 | -13.0168 | -43.9823 | 2025-10-20 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 4bf467e9-162e-3352-9bed-2201e294073d | -8.4345 | -44.1324 | 2025-10-20 00:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 90709182-b325-3bf5-b113-42875e62040d | -2.2711 | -51.9104 | 2025-10-20 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b7cf9646-b404-3a88-be8e-790552e5f8ec | -2.9128 | -52.7146 | 2025-10-20 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 7ba79569-2325-3a6d-965d-cd820a8f62af | -10.0204 | -47.0414 | 2025-10-20 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 9276a5ba-8c1f-3e6e-acf4-f8dad46cf40c | -3.3279 | -50.2195 | 2025-10-20 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 2a659a59-079e-34da-a40a-29a0bc842fb3 | -2.8644 | -50.7361 | 2025-10-20 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c74879c2-ff84-3096-815c-2eb71c828402 | -8.0676 | -48.0112 | 2025-10-20 00:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| e94f63e1-433b-32a7-89d7-31d15594a0a3 | 1.0763 | -51.3099 | 2025-10-20 00:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f0402a11-4b0a-3a52-b85c-58b68e42e5cd | -13.0168 | -43.9823 | 2025-10-20 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a0449262-f470-3b47-a8c1-b15825974e3b | -2.2527 | -51.9313 | 2025-10-20 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| dccbbddf-3250-34f6-8d99-e55d033fb2c4 | -4.4066 | -43.3118 | 2025-10-20 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 9eda087c-6a69-3a30-ace9-7c62df0f0fd5 | -2.9128 | -52.7146 | 2025-10-20 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a686c05f-5c2b-3666-93cf-dcde554d1add | -2.2343 | -51.9111 | 2025-10-20 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| dcd6c457-7471-34cb-9d86-043de9021b13 | -9.6401 | -64.7411 | 2025-10-20 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 8ac820c5-e378-36ea-ae42-82b19c41e3f4 | -4.3879 | -43.3129 | 2025-10-20 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| e447b0ec-2126-392a-80d3-b8899b60dcb8 | -2.2527 | -51.9108 | 2025-10-20 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 9328fa75-d5a7-30db-812e-92d2ff294f2b | -6.3866 | -45.7594 | 2025-10-20 00:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 7ed78749-f30e-335c-8137-da6558c8496c | -3.3279 | -50.2195 | 2025-10-20 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a23436bd-cb0b-39df-bd0f-41c77b9bbd84 | -13.0173 | -43.9586 | 2025-10-20 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 25369a30-f08f-36b6-a4c7-8ed9cf675d7b | -12.9979 | -43.9619 | 2025-10-20 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| aa5cf061-caa0-33f5-8dde-405a0f19c3ff | -17.96142 | -46.74887 | 2025-10-20 00:30:00 | TERRA_M-M | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d26c2eb-7718-30c5-a456-f402a8cc84ac | -17.96273 | -46.75814 | 2025-10-20 00:30:00 | TERRA_M-M | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d871c01d-1f2a-3049-8e3b-2577efd166cd | -21.64244 | -48.39534 | 2025-10-20 00:30:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 91fefaf2-9637-3083-b1db-6c73aae0e67a | -10.02063 | -47.04792 | 2025-10-20 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ed65a87a-5980-3f5d-b090-8e7c5289cd43 | -15.55481 | -41.62908 | 2025-10-20 00:33:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.2 |
| ced09edb-aca2-36fe-887c-48d24ee5b5f7 | -12.45719 | -43.01379 | 2025-10-20 00:33:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 28.6 |
| f2995c2f-a0a9-349f-97e4-89e2b063fae4 | -10.76158 | -47.33055 | 2025-10-20 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 12f485ac-6408-3b4e-be3c-b8c3ec40766e | -10.90112 | -48.24849 | 2025-10-20 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e6e10bd3-f9e5-3f16-a173-90dcf824d5e7 | -12.45464 | -42.99759 | 2025-10-20 00:33:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| d37e2b72-66d1-3804-aea9-76c96463811d | -11.61406 | -48.54045 | 2025-10-20 00:33:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7c304166-e057-3f1e-8892-b2f2e80d4d2f | -14.45128 | -51.51403 | 2025-10-20 00:33:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9010c6d0-bb6e-3fc4-b63b-e0d3f4206a56 | -10.75051 | -47.8979 | 2025-10-20 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f9863ad5-1c94-3df7-81e9-0fa3b926219e | -12.46422 | -43.00706 | 2025-10-20 00:33:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 47c640fa-16f8-3b2c-b607-78d7bd55704d | -10.55338 | -43.36168 | 2025-10-20 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 501f8674-345e-3f10-b2cf-95aec0f7cb9f | -9.59785 | -45.00763 | 2025-10-20 00:33:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 772fdc9b-fbd4-37fe-bef4-5f8d9beb2e9a | -10.0114 | -47.04939 | 2025-10-20 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ab221b9e-27f0-300d-8ab0-66d7f380394e | -14.0372 | -42.81535 | 2025-10-20 00:33:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 53ee3194-3aa8-3009-bab9-a7edfbe88e38 | -16.37158 | -49.06739 | 2025-10-20 00:33:00 | TERRA_M-M | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bdb4b58a-8826-3f03-8e24-31157d94d953 | -12.39681 | -43.158 | 2025-10-20 00:33:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2f73c330-dc06-31cf-87bb-9ea14e787454 | -10.76295 | -47.34002 | 2025-10-20 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7400128d-db64-306b-a45b-b6a440d398d3 | -10.65634 | -47.62656 | 2025-10-20 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 473ed350-aaa5-3536-8753-bf7ab87c5a21 | -10.66533 | -47.62523 | 2025-10-20 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 3c4a7d2a-8297-3676-98b4-937436913a87 | -10.65766 | -47.63587 | 2025-10-20 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34394e0b-0825-328f-988b-88d281f401ef | -11.00373 | -47.92572 | 2025-10-20 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README2.md)
