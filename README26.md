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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f6605da-a6b3-3139-9ffe-64baebb06b91 | -2.88455 | -54.87816 | 2026-09-30 04:32:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eaf974a-b9c4-32a5-9d00-002fd7273e64 | -3.10814 | -50.27962 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cad9bd96-02d9-3f6a-8709-af9496d5aca7 | -6.43892 | -55.80468 | 2026-09-30 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ade5fa5b-94e6-34cc-ab54-a1019bd371d8 | -7.07619 | -41.75584 | 2026-09-30 04:32:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b9735f61-b403-35b1-94f7-ceee6ed996b9 | -6.10753 | -55.69391 | 2026-09-30 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e9fb123-d44a-3d85-857a-565d62c002c4 | -2.97318 | -51.05323 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7cfa13fc-8aae-3d78-86f7-1bd86b443c9a | -6.78803 | -55.82338 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff97f260-5218-352a-8baa-7d27d98f2600 | -2.44686 | -49.22132 | 2026-09-30 04:32:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e46383dd-0f4e-315a-b4ee-28094266cfbb | -6.16475 | -44.61503 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12b2b59a-14c4-39ec-a871-d367e7daed08 | -2.98576 | -51.0351 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 42de4511-c088-384e-ba52-aa1416077754 | -5.09471 | -46.04372 | 2026-09-30 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bc8aaaeb-d367-3d8b-a9c6-5c793a291a4b | -5.72554 | -43.28266 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b1e984b-b58c-3d49-8d55-6a1993a30ba2 | -7.82304 | -45.82251 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4043a741-8b4e-34ee-94d5-b01e66ea4f54 | -5.85343 | -51.79289 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37d8d4b6-38ee-369d-b3bc-a2ca4d2ea42a | -6.71745 | -45.57945 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a67fb4e7-e26b-3c14-87a1-78a2bf4681c2 | -5.97472 | -46.60955 | 2026-09-30 04:32:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c397416-412b-34d6-8dad-3d11f5666b31 | -6.71169 | -45.63649 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3046db7f-2204-3b5f-accc-03d33acf1eed | -3.2323 | -46.94124 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 62bd8472-0ba8-3447-872c-90c160e53f42 | -4.81181 | -49.4651 | 2026-09-30 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a612692e-dbfc-3fd1-afa3-d4a8ee3a617e | -3.18766 | -51.23878 | 2026-09-30 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d3047ba-7f96-3d5c-a2f8-782481c457e7 | -7.50059 | -45.80676 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49f006e2-cbf0-3cec-b41a-e05d1942e85b | -7.51892 | -44.54114 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 955c83ec-b2a9-3e18-85ee-72dfba79e73c | -9.12217 | -40.64085 | 2026-09-30 04:32:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 85d6f674-f78e-3c3a-80c6-8d64fa54105e | -7.48889 | -45.79394 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb621737-b718-353b-bb20-ee0d0e4e9c76 | -7.9236 | -45.44183 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48320658-fbd5-3773-bd3e-b43494b7d06c | -7.01248 | -45.30321 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe58fa9e-800a-330c-abf1-da14aa4b4063 | -6.12426 | -53.28595 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8960f0b8-4c01-3e74-becd-0bcd8304c982 | -5.87018 | -50.15945 | 2026-09-30 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b5fb22be-2830-351e-9fd2-a2104ebfe5ed | -3.56408 | -50.2585 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02b6a453-f631-3f2b-9769-b90eb9143fe3 | -2.90149 | -54.09682 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 63d401ab-af91-3a2f-91cd-52f4af1bdfd3 | -8.37464 | -45.39253 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b529c09b-b6d9-3bf7-be06-efa20a02f00f | -6.70647 | -45.98999 | 2026-09-30 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acb40f2d-f3fe-3581-89c6-9cd2f35f85e1 | -3.22665 | -46.94569 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f717f14a-f2e9-3df8-95a6-5d7cad294769 | -6.14253 | -53.0604 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ec3f291-5c75-38ad-9904-8218884cd344 | -2.98266 | -51.02456 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 40cd8425-730c-3cef-a99f-cba35987c2a6 | -3.24244 | -46.94707 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59570930-9e80-39c7-9eb5-3a2a2d450019 | -7.84092 | -45.81809 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f47eba43-664e-3e3f-af75-faf50c65416d | -3.38012 | -50.96058 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2db568f7-a7a4-36e9-8889-a36323100a23 | -5.78907 | -43.76398 | 2026-09-30 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4edb1b0-dcbb-3a57-8f07-9349c9023ce1 | -6.7056 | -44.70453 | 2026-09-30 04:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1c50dac-ebc3-305c-a48d-7d7f215fe1e1 | -5.987 | -53.54913 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7ef6414-a2a6-3653-92ad-bc8a77ee1078 | -8.38765 | -48.0686 | 2026-09-30 04:32:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15be80b5-29f7-3199-9461-acf598ca088c | -6.13848 | -53.26557 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9134c877-8cad-3d00-b08f-154d2bfbf136 | -7.13851 | -47.0261 | 2026-09-30 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9587301c-7b7e-3546-a8f4-fd6339b657c1 | -2.98497 | -51.04 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 206cff3e-c8f9-3b0a-99e5-0ce81754d1be | -6.8622 | -40.944 | 2026-09-30 04:32:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a6d17104-190b-3b9e-8cd7-f3e8b2f635af | -8.56119 | -47.78826 | 2026-09-30 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0014ff50-5c0b-3a00-9d9d-ba647595b27e | -3.60914 | -49.50124 | 2026-09-30 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d97a8c81-31ac-36d8-abcb-3faeae399c52 | -8.06096 | -48.1024 | 2026-09-30 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 355dfc38-9dce-3e66-a8c5-c9968566a291 | -7.82727 | -47.93092 | 2026-09-30 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b053904-13a1-353b-805b-7e17d7208aa6 | -7.01304 | -45.29971 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f60c1e82-3c6a-3ae2-a76a-6384cd5be103 | -3.23386 | -46.94688 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0e181e03-bcb7-3e9b-8705-85f7a992d18d | -3.24625 | -50.1208 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8573ed4e-3a78-3641-95b9-6e80cf044be2 | -7.48275 | -45.78936 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cf74609-f9b1-325b-a87a-cf1e1bdb8f30 | -7.42695 | -55.1803 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba894108-2e80-36ea-9978-bbfb2604416e | -2.97479 | -51.04337 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bc901888-bf18-3d3f-9c28-e40f28740051 | -2.89657 | -54.08879 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71b1ef5a-7ff2-3a15-bbc0-b92973f2d01c | -4.02915 | -54.20641 | 2026-09-30 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fb3fd84-e7c7-3d57-9ac2-f765de71f10a | -7.00915 | -45.30267 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d420ea4-f123-3e86-99fb-bdbfb0de4a58 | -2.48367 | -49.25847 | 2026-09-30 04:32:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5d4ea96-c835-3e59-afe9-b31f9872444e | -5.72789 | -43.50855 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 316cb57a-3cce-30d8-be16-3386f11e0cc4 | -7.53168 | -44.54675 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78ed5718-7bae-3e73-8fa7-09508158bae9 | -5.12654 | -56.0195 | 2026-09-30 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d174db5a-54ec-333a-9cec-e0cc9a2279a4 | -5.74443 | -45.17253 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 741fc78a-bcd0-367e-a34a-8e9297a97ce0 | -5.75835 | -45.17117 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4d8b3b86-771e-3c81-a63c-df58a7e8cea7 | -5.09503 | -49.0629 | 2026-09-30 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 96a33aff-7011-366e-9cb4-0c76ac4f5400 | -3.11187 | -50.2847 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9dd5af32-08dd-39f7-9624-1b4a63b96435 | -8.9819 | -44.17509 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 998f742c-21a8-3874-ba44-9fb9158ff80a | -2.98655 | -51.03024 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2c53dc23-4e62-3d6f-87e8-8026f091d7a2 | -3.25028 | -50.1205 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f551506e-51d8-3195-afa3-e61aabcdd5a3 | -2.901 | -54.09784 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c1aadab0-c5d6-3b01-8160-b163acbdba2f | -7.64263 | -45.51166 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd83bbfa-c31b-3f89-8cb6-e8f223ce6f7b | -3.01034 | -54.22755 | 2026-09-30 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ef2397e-ae3a-3a0b-afb8-ee710f1d7231 | -8.34513 | -45.98279 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba3f7855-a48f-35b8-ad5f-b5f54281a60a | -4.81344 | -45.64193 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b659e9f-00ca-33e4-87a2-1eb56e6cf5f4 | -8.33385 | -44.16165 | 2026-09-30 04:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a145c8b9-5f3c-30c2-8451-019fca198246 | -7.83309 | -45.82412 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eb5c675e-ccba-3f8d-845f-4d3e4172d582 | -4.44391 | -46.28506 | 2026-09-30 04:32:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ccae483-8384-3d29-a222-ad9b80429d3c | -4.28953 | -48.56021 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f899b504-88e9-3958-9e72-5cd5fd9dfcc0 | -5.40723 | -45.90285 | 2026-09-30 04:32:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d32f3f11-1244-36bb-a9c4-9e5122162cbb | -3.51122 | -50.30814 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b0fe471-3b98-35dc-af44-dc72088dd3b5 | -8.01933 | -42.83834 | 2026-09-30 04:32:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bc571789-2d27-3152-ac10-50f1ade02a42 | -7.83031 | -45.82003 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 14d5d811-e391-3093-b3f1-f8f0be94fb59 | -4.84656 | -42.87944 | 2026-09-30 04:32:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf4c5fe9-b646-3950-b006-913cad187e19 | -2.90742 | -54.09487 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43eb2689-8a10-3d03-92f8-88c75a8dd6a1 | -7.54175 | -47.12149 | 2026-09-30 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c94b17ec-338c-3695-bcaa-56bd0fc704be | -6.10949 | -53.09826 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a60140ed-8087-38fb-8903-da8d72101398 | -7.51281 | -47.33926 | 2026-09-30 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43564e08-ec43-3b24-b9bf-d19adea32b60 | -4.45753 | -47.91817 | 2026-09-30 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e72ed36b-1229-393e-8225-617e0e19c19b | -6.38331 | -45.80661 | 2026-09-30 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5db26647-8b2c-30ac-b8ec-5dc07f681cf0 | -5.81764 | -46.2179 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0372d568-e722-30d4-aaa0-3f98cf2f76d4 | -2.57588 | -50.7895 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b8f5bbd-efb7-3e42-9537-377eb337cf41 | -6.2138 | -42.51683 | 2026-09-30 04:32:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 98a11865-555c-351a-a316-d761c11dcba5 | -3.24706 | -50.80809 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 85e9a0c0-2d03-398e-81c3-f47f4e564b9d | -2.96862 | -51.02221 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ddef6bc6-ff68-33e6-afed-bae35b69f0d3 | -6.75227 | -55.08596 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6992f70-3f10-3da5-975c-1fc4d07aa9fb | -3.15719 | -54.0945 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34833f5a-751d-3d48-818d-e39d43819c4d | -5.69973 | -44.72964 | 2026-09-30 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 6a25ca15-5145-3ac3-a9f0-c4fdd156a853 | -2.37607 | -50.40792 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 546a9c6d-dea8-338a-b637-c6c1c98dda94 | -3.27007 | -50.13671 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README27.md)
