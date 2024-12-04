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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6ebc470-0593-35c0-b35e-739e8652b035 | -3.2153 | -50.6423 | 2024-12-04 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2cae694c-7600-354e-8396-d27baddbddb7 | -1.7361 | -52.6162 | 2024-12-04 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 841640b0-7408-31b5-8ad2-b1f4e94f7b7f | -2.6428 | -45.7394 | 2024-12-04 02:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 7fc930c1-4d95-3072-bd98-7d80f3b9c745 | -4.1222 | -43.9529 | 2024-12-04 02:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 7ec435ad-7d84-374a-af28-780e2256fb9f | -4.1225 | -43.9068 | 2024-12-04 02:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| f4a74c91-418c-329c-a26b-1af853831d68 | -1.7544 | -52.6363 | 2024-12-04 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 6e9a9a34-1ca6-35e5-975c-b26b6dc8d3a9 | -5.6281 | -44.8433 | 2024-12-04 02:00:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| be682d91-aaef-31e8-896d-568200efa4e4 | -6.0862 | -48.0339 | 2024-12-04 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| e9c4e410-5b30-3abe-ae90-fec89dd9f0b2 | -2.8975 | -51.8133 | 2024-12-04 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 27df90f5-a4fe-368c-ace0-6a0a646511b3 | -3.259 | -53.6388 | 2024-12-04 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 359aefbc-8795-3b3f-8321-53be39073147 | -9.6637 | -36.1448 | 2024-12-04 02:00:00 | GOES-16 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 122.8 |
| 7820f275-5e5f-3aa2-ba19-fad55969cf4e | -6.1047 | -48.0544 | 2024-12-04 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 6eae239b-09b4-3a9d-b070-e39b7bd57588 | -1.7361 | -52.6366 | 2024-12-04 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 0cb40eef-ef89-3582-b921-34cc081b811d | -2.211 | -47.254 | 2024-12-04 02:00:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d9bcd51b-06cb-3187-9a8b-fca5e9965482 | -9.683 | -36.1415 | 2024-12-04 02:00:00 | GOES-16 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| 915a7f27-891f-37ad-a58d-92ebd598c0e0 | -9.6632 | -36.1719 | 2024-12-04 02:00:00 | GOES-16 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| 318e00c0-30c3-395b-8d6c-a83e97169cbb | -2.6242 | -45.7399 | 2024-12-04 02:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 217cb34d-f7b1-3232-88e9-e7e2cf56d194 | -4.1225 | -43.9068 | 2024-12-04 02:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 0353aa96-7be5-31c3-abf8-34ef83404b8c | -1.7545 | -52.6159 | 2024-12-04 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 0f091a52-b6df-3568-9a29-76628dd45931 | -3.8065 | -46.9584 | 2024-12-04 02:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 2cad08d8-7cad-3739-adab-d55e67f56955 | -2.6428 | -45.7394 | 2024-12-04 02:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| d7662701-43ac-3b30-9c7f-356e5526189c | -5.588 | -45.1638 | 2024-12-04 02:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 164f6aca-fb14-344e-91c2-997e87b21eb0 | -2.8197 | -53.0425 | 2024-12-04 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0a19b581-ee69-3f57-a1ab-77180f0511a7 | -6.0862 | -48.0339 | 2024-12-04 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b9a576aa-2601-340c-bf3d-23a5b64cbd3c | -5.5693 | -45.1651 | 2024-12-04 02:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| ac0798e1-9599-34f5-81be-100095bd493e | -3.259 | -53.6388 | 2024-12-04 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d0f706d5-83bc-3145-b8c5-dbe8797c554e | -6.086 | -48.0557 | 2024-12-04 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| a7c9953a-6c90-33e8-bd33-bb2cb25d8ed1 | -3.127 | -54.6063 | 2024-12-04 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| d31b9f27-1415-3038-9567-6f0e91ff890c | -4.1223 | -43.9299 | 2024-12-04 02:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| b46b29e3-255d-398a-888c-e53248702d68 | -2.8012 | -53.0633 | 2024-12-04 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 53eaee23-5cdc-3364-93f9-812b8b256590 | -2.8196 | -53.0629 | 2024-12-04 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 1fcf46c5-fc96-3d1b-84c5-977cfd5bcc8e | -2.6242 | -45.7399 | 2024-12-04 02:10:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 7283bf7b-7fce-3bcd-bd5e-4e28e2c0c70b | -1.7361 | -52.6162 | 2024-12-04 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ef543117-46ae-3617-bc57-e3ee1b3eaad0 | -1.7544 | -52.6363 | 2024-12-04 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| b36ff6d2-2bc7-3b50-b839-30329ffeb1f4 | -2.8013 | -53.043 | 2024-12-04 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9a979943-9a1f-3d39-826e-7f907d45cda0 | -6.1047 | -48.0544 | 2024-12-04 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e3a055a7-be05-3234-b704-3d7fddc2dea5 | -3.1454 | -54.6059 | 2024-12-04 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 9c37bd6e-d3d7-3ffe-a7b2-dd61d9b04dd0 | -1.7361 | -52.6366 | 2024-12-04 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 16646021-5520-3f54-a89f-c1ba85887348 | -3.1269 | -54.6263 | 2024-12-04 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| b5e1208e-dbe8-3993-ac16-29cead902a4a | -1.663 | -52.3927 | 2024-12-04 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 54152b16-6de8-3818-8c38-f198e1a9b912 | -2.211 | -47.254 | 2024-12-04 02:10:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e7af8247-26a8-39e8-91df-5811e78ffb3e | -3.259 | -53.659 | 2024-12-04 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| c6a0f56b-cc6a-3c26-8bbf-bbd665fb7596 | -3.1086 | -54.6268 | 2024-12-04 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 45b83932-6165-3bc7-92cc-737d3cb1a701 | -4.1037 | -43.9309 | 2024-12-04 02:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 27fecb06-88d5-340c-9dcf-5e99eccfda5c | -1.6446 | -52.393 | 2024-12-04 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| df70738b-fa75-3b5a-b0cd-e34487a750bd | -2.8196 | -53.0629 | 2024-12-04 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 64fa7bd5-c84d-32ad-b1c5-9b0a119a0d2b | -2.6428 | -45.7394 | 2024-12-04 02:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| d8f5e54f-8036-3d52-bef3-3e50e2c602eb | -2.6242 | -45.7399 | 2024-12-04 02:20:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 6c274bc4-1f07-31c1-9dc5-77dd1c700c8f | -2.8012 | -53.0633 | 2024-12-04 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 67495ddc-5202-3108-9c3e-a44088dfbb53 | -1.7544 | -52.6363 | 2024-12-04 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| f8cc5c87-0ee6-3a21-99d9-55d2e328f119 | -1.7545 | -52.6159 | 2024-12-04 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| df4cda67-f19b-3fbd-98e8-f62940cbfc3d | -5.6281 | -44.8433 | 2024-12-04 02:20:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 0f84d49b-61b3-3157-b359-7ebc458b7250 | -3.259 | -53.659 | 2024-12-04 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 4e7cca39-927c-312c-902f-4c0992ca97f8 | -2.211 | -47.254 | 2024-12-04 02:20:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 0cb9f275-0a3c-3a9f-b7ec-5c13e9e4ef67 | -1.663 | -52.3927 | 2024-12-04 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| de02cefa-d323-38de-97f9-99464510a13a | -2.6243 | -45.7176 | 2024-12-04 02:20:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a2d8c363-1140-3d74-b1e5-d443f8c8573c | -1.7361 | -52.6366 | 2024-12-04 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9b3b3254-4ed5-3675-ba7a-e611f1742281 | -1.7361 | -52.6162 | 2024-12-04 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 7a242b99-7295-379e-9ba2-5f945888fed6 | -4.1223 | -43.9299 | 2024-12-04 02:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e87a5832-c289-3d77-96e3-911035c4d439 | -1.7728 | -52.636 | 2024-12-04 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2f5dab2a-4b2b-35b5-b489-87f130de52d2 | -2.8197 | -53.0425 | 2024-12-04 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 16388c61-f2c1-3322-b857-881d8d88ef21 | -1.6623 | -52.7599 | 2024-12-04 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 91fd1515-9225-3d26-92b3-8eed9fc99a43 | -4.019 | -48.8147 | 2024-12-04 02:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 65de87ce-262d-31ac-92d5-f3facee0a397 | -4.1223 | -43.9299 | 2024-12-04 02:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 50269558-2f2e-35d4-8a53-67ddd1736a51 | -3.0738 | -54.0465 | 2024-12-04 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f42998de-a905-3db2-9527-86df13e9bac1 | -2.8012 | -53.0633 | 2024-12-04 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| ffc7f919-107e-393e-b4eb-bbadb84884a6 | -3.259 | -53.6388 | 2024-12-04 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e24b306e-df12-3191-86db-decbe95dd7c8 | -1.6446 | -52.393 | 2024-12-04 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 24c07ac8-462b-32b5-9f0c-da34ed915f92 | -1.663 | -52.3927 | 2024-12-04 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 0450e4f2-5afe-3169-952e-91b67b55be92 | -2.8975 | -51.8133 | 2024-12-04 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 05e89da5-5d68-3b7b-8f06-d658dff67d5e | -1.6631 | -52.3723 | 2024-12-04 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 90fc8ca2-cc56-3fab-b5db-94084bc61e62 | -2.6428 | -45.7394 | 2024-12-04 02:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 94d3f691-4f9d-3139-a23f-6415f65b6658 | -2.8197 | -53.0425 | 2024-12-04 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 700b5b16-fc95-3cc5-a483-86a51646d8b0 | -3.259 | -53.659 | 2024-12-04 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| fc076317-a43d-3986-908f-42107bf00798 | -1.6241 | -53.5308 | 2024-12-04 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| c5913663-18bc-3d15-a904-3072e688ed10 | -2.1925 | -47.2544 | 2024-12-04 02:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b8d45cc2-0ca2-34ab-8719-4922497f0c7e | -2.8196 | -53.0629 | 2024-12-04 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| ec2a3c24-2293-32a0-adf3-094a8b4cd0e1 | -2.6243 | -45.7176 | 2024-12-04 02:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2934e4e9-677e-3a08-9591-824d3d21b4b7 | -1.6447 | -52.3725 | 2024-12-04 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 0d3cc8c8-ca55-3e88-8236-54ed7672b704 | -2.6242 | -45.7399 | 2024-12-04 02:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 35bc806f-a2bb-337e-87fb-f3164f5d601c | -3.2153 | -50.6423 | 2024-12-04 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e1e8de0f-442e-3b49-bca1-bb3c117eecc8 | -1.6446 | -52.393 | 2024-12-04 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| b735cf34-0894-3371-b100-55c9cf0c34d7 | -1.663 | -52.3927 | 2024-12-04 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| edd87b07-018c-3174-a2e4-6e2ef63d0168 | -3.259 | -53.6388 | 2024-12-04 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 081968a7-b71d-3f2b-934b-f7987119f113 | -1.6623 | -52.7599 | 2024-12-04 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 3724b1fb-81d8-354c-be70-5f5700c97a64 | -2.8012 | -53.0633 | 2024-12-04 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9d9c8874-3b27-39af-86d7-e656f16af72f | -2.6242 | -45.7399 | 2024-12-04 02:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 476e0e27-8ac8-3903-b97f-7db2848ad6c9 | -2.8197 | -53.0425 | 2024-12-04 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fe1f2d70-d818-3f79-b00b-b37cf6b862d0 | -3.259 | -53.659 | 2024-12-04 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 10f74d9e-d7af-3d88-9545-795f85b6092b | -1.6447 | -52.3725 | 2024-12-04 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 4ffb38ef-7378-31f2-8a2c-8cfcbc10cf1e | -2.7564 | -45.197 | 2024-12-04 02:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 88e5877f-5b43-36d7-ae98-72bcb39891f1 | -2.7317 | -51.8176 | 2024-12-04 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 000da05a-bc2d-3198-87e1-3580e48ded11 | -4.1223 | -43.9299 | 2024-12-04 02:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 34a76892-883b-31ce-a4c5-256fc8b9bc9e | -2.8196 | -53.0629 | 2024-12-04 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 804861ee-ce18-3df2-9598-523cbe348bcc | -2.8975 | -51.8133 | 2024-12-04 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a75365af-f59c-313b-b377-102e2617b021 | -2.6428 | -45.7394 | 2024-12-04 02:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0eeb4b92-2d90-3b48-aab1-51451e63a7d1 | -2.6242 | -45.7399 | 2024-12-04 02:50:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 9eaf2847-7874-32d1-b89e-213ca22c6ffe | -2.8975 | -51.8133 | 2024-12-04 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 18aae711-3efb-3bda-b96e-d0c704653a7a | -2.8197 | -53.0425 | 2024-12-04 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d7d34556-1ed9-3fd8-a707-8a65db3a1346 | -1.0461 | -46.5954 | 2024-12-04 02:50:00 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |


[Clique aqui para ver as próximas entradas](README18.md)
