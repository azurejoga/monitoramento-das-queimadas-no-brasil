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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6e2a672-6581-3598-a341-09c08dcf5f12 | -11.2482 | -45.1194 | 2026-09-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 5544a16e-5b3f-3fd4-b220-5ab1e8566d55 | -7.2934 | -60.5713 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| ed10f99e-2507-381e-a799-d7049a08f3c0 | -5.5833 | -60.1924 | 2026-09-01 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c66f0466-627b-3791-bfb9-461ea02f009e | -7.9985 | -44.2943 | 2026-09-01 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 337e3565-19b8-3c2b-a869-a59fcbc07bb0 | -13.9474 | -54.4179 | 2026-09-01 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 932592b7-97b4-3ea2-99af-82ee36252f82 | -8.5792 | -54.6758 | 2026-09-01 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 431096e0-f159-3233-86f2-233df1d0795a | -9.4349 | -45.625 | 2026-09-01 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 96731cc6-c362-3bdf-87e9-13c8e21b5aab | -14.5214 | -52.2313 | 2026-09-01 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 00f731ca-2691-3083-8f9e-ead9fa0752f1 | -9.4606 | -67.4531 | 2026-09-01 14:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e1c88c07-a7ea-3696-87f3-2c65e0188b18 | -10.7856 | -50.5066 | 2026-09-01 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 7c33a5bc-6155-3d70-adb7-91290d38ea56 | -3.1083 | -61.238 | 2026-09-01 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| a21aa54c-59dc-3f56-bff7-54fc6bd88c31 | -7.3488 | -60.5691 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b8e0f15c-bca9-3b13-97a3-cea1affc622a | -6.1659 | -57.7403 | 2026-09-01 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| de233249-5bbc-38ae-833d-85fc43e98d0f | -8.9242 | -63.2804 | 2026-09-01 14:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 7d4f0f12-4c18-3302-84ef-50692921ad03 | -10.7407 | -54.0401 | 2026-09-01 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 5579402f-d187-3c0f-bec7-642a3cc6083c | -7.8716 | -47.0838 | 2026-09-01 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| bf415354-8a5d-3ce1-9b2e-351dd1a804c9 | -7.5289 | -61.3825 | 2026-09-01 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f5ca7ed0-5064-323a-b132-41f0749b3eb9 | -11.2478 | -45.1425 | 2026-09-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 1955e26c-e56c-3ba3-995d-b39f0494258a | -11.2829 | -45.3214 | 2026-09-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 9a243fbc-d499-3b29-be2f-65c689e74e92 | -3.5162 | -59.0405 | 2026-09-01 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 015120c6-1dbc-3415-865e-92c14142eda9 | -7.3487 | -60.5883 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 015437fa-e0d9-34c1-9cb7-89212c75c586 | -14.6535 | -53.5642 | 2026-09-01 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| eadce9fe-882b-31ec-991b-6414cd11befc | -10.2212 | -50.3303 | 2026-09-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| edbff079-847e-3913-bcc5-7c13532492bb | -13.4325 | -57.061 | 2026-09-01 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d3b5bce3-693f-3dd1-a557-82114ab5715f | -6.7699 | -55.6644 | 2026-09-01 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| fb353938-d530-3848-9aca-c361b3799631 | -7.5709 | -60.4835 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 1b3e850c-9307-32ea-8664-1826ecd87464 | -10.0364 | -44.6825 | 2026-09-01 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9358d938-ad25-3191-b1c8-02b5e626d406 | -10.7409 | -54.0196 | 2026-09-01 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 4e4d8bd2-89b4-33f3-9077-705e23d0a18e | -12.9032 | -45.8382 | 2026-09-01 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 480.3 |
| 721dd8a5-456d-38c1-a4e7-865c159a99cd | -5.5649 | -60.193 | 2026-09-01 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e60aeb99-33a1-30a6-84cd-b51af7c0eb4f | -7.5526 | -60.4651 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 46bc978a-72fa-321a-bab2-4e0d84f5bed4 | -8.5924 | -66.975 | 2026-09-01 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 6bd6bc5c-3a9f-35da-a784-638d451bd063 | -14.2599 | -52.8782 | 2026-09-01 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d4eeed27-3894-3d93-a6db-8df1be2b484c | -11.0623 | -49.6829 | 2026-09-01 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 96203926-aeb5-3d68-a4a8-ca233a1625dc | -10.3577 | -49.9957 | 2026-09-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 406.8 |
| 1f17f19a-e4d6-3b4e-bf11-d8b74c17f6fc | -3.6215 | -60.566 | 2026-09-01 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 79430bd2-b302-3d5e-a99d-db3e3708bd81 | -7.3118 | -60.5897 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 438b8569-5bc0-38ab-8933-f43faf6bfe60 | -13.4516 | -57.0592 | 2026-09-01 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| e00880af-1c0d-3cea-9842-ace5c88c0431 | -3.8792 | -44.0346 | 2026-09-01 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1c76b0e7-6db4-3658-bb63-65e4beca3aae | -14.6728 | -53.5618 | 2026-09-01 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| f8a6e854-0761-3816-bca1-f68a11faf62a | -13.4575 | -51.411 | 2026-09-01 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 8b26c8fe-1677-3b34-8b15-ca43cb270df2 | -6.6542 | -59.426 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 7411cf56-5e33-32cd-a9ab-a7f2a06d4d20 | -7.182 | -60.6904 | 2026-09-01 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0b663972-35e3-34ee-a964-d8743d0e269e | -6.8036 | -59.0921 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 82aead0d-a6de-3906-8c18-9dd3e782d656 | -6.6541 | -59.4452 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2a8222d6-4325-39c9-b768-66979c9267c2 | -6.8183 | -59.7658 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 05d21651-855e-3ad9-9a2e-50e54ff2740e | -7.1786 | -55.4837 | 2026-09-01 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 5a4fa6e7-700e-3de4-9d52-1205c31a3295 | -6.8009 | -59.5742 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| c6ddb4dc-9780-35b7-8d73-2815eed25bff | -9.9931 | -46.3057 | 2026-09-01 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 9a35d89a-043c-3675-922b-93ecc5573ced | -10.1542 | -45.6755 | 2026-09-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d4616b79-42bd-32cf-a75c-96126da381cf | -6.9367 | -55.636 | 2026-09-01 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d080e80c-611c-3c91-a430-692e7de4be4d | -11.2673 | -45.1167 | 2026-09-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 93113e4a-8d9d-34c7-aae9-845aec304e09 | -14.5021 | -52.2339 | 2026-09-01 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 35d8ace1-caa0-3e1f-bd1f-b1a827ea2947 | -13.471 | -57.0373 | 2026-09-01 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 9a4934ee-addd-31d5-be65-fea6e778a469 | -11.7216 | -47.6327 | 2026-09-01 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 4fceb438-962c-38b8-8c3b-265865413d91 | -7.2934 | -60.5713 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a548752a-c983-32ca-b9cc-99871527998a | -13.9667 | -54.4157 | 2026-09-01 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 2d11d53c-eee0-3699-bf00-28084f6a724c | -6.6727 | -59.4252 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| ba1c9795-ade6-315f-9e1b-80a8b6857a2b | -13.9477 | -54.3971 | 2026-09-01 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 245.9 |
| 7a7db1c4-543a-3b79-882e-e815ad7c7a47 | -3.8416 | -44.0824 | 2026-09-01 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 72158ac9-da78-3f7c-80f1-9b8ced81d61b | -11.2298 | -51.2456 | 2026-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 69f739e4-85d6-30bb-a409-05fed0c7a0f9 | -7.9797 | -44.2962 | 2026-09-01 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| e5d95cee-99b7-3a82-9c10-4f7ff1ef2492 | -10.7271 | -50.6405 | 2026-09-01 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 5ceef4e2-f472-3334-bc09-1e768354cae4 | -8.7817 | -46.4623 | 2026-09-01 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 262.4 |
| e9f96852-d418-3251-9f72-2af3ed830d46 | -10.3574 | -50.0171 | 2026-09-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 218.5 |
| 9b724b3c-f6d8-3d48-b1a2-0d7ecf551372 | -9.4339 | -45.6931 | 2026-09-01 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| b1d9336f-8aee-3e27-ba75-515fcdb48c2a | -15.2478 | -53.8666 | 2026-09-01 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 00fb2d8f-67a9-39ca-b624-d70f4aad63e4 | -15.4429 | -52.681 | 2026-09-01 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 323.4 |
| e6b5e64d-3e40-34ee-8153-79e0904e278c | -10.1525 | -45.7892 | 2026-09-01 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 174.8 |
| b5b8e5fa-f2b6-3893-9f9d-cfb95edf1381 | -9.4144 | -51.6733 | 2026-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b161c904-bf5b-3cec-ac9b-72498d51fcdf | -4.181 | -63.1543 | 2026-09-01 14:30:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 203.4 |
| 3e7651bf-cb80-3b6f-bf4b-782fdc81f589 | -6.7998 | -59.7665 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| bb307f54-2d20-38e2-b1fd-461a468a8007 | -16.1523 | -46.6749 | 2026-09-01 14:30:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 151.9 |
| b1a61387-44b6-3fc6-9d10-800cf7fbeeec | -11.2292 | -51.2879 | 2026-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 58c73392-1d62-3851-bf09-eba3ba66febe | -3.5161 | -59.0597 | 2026-09-01 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| edc006b8-dd85-302e-aa20-6d6f30f9353d | -7.2005 | -60.6897 | 2026-09-01 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| b3da558d-b282-3fe2-8a3d-2aaaf0b0c08a | -6.6036 | -58.5972 | 2026-09-01 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| ad0ab5f1-b8c0-3154-b4e7-7f8323e3403b | -7.571 | -60.4643 | 2026-09-01 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.3 |
| c3f585b9-ff97-348e-8db8-0f08d3591696 | -10.358 | -49.9742 | 2026-09-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| c6d1c9e0-5e95-3f12-82e8-5357f060f593 | -11.2482 | -45.1194 | 2026-09-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 2fe875cf-8ad8-32d1-a8b2-3ca7e6c5b79d | -7.2006 | -60.6706 | 2026-09-01 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 138.1 |
| b13ddb29-7e9e-3db8-8850-0a74b464fcb4 | -8.5739 | -66.9754 | 2026-09-01 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| b5b4018b-5075-3e5d-aa48-f62d53502a9f | -11.213 | -46.0839 | 2026-09-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 9eab82c6-d0aa-3e8f-ad2c-02509cf7f86c | -8.7628 | -46.4642 | 2026-09-01 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| fc57b9cd-3d69-3a43-b55b-0925e2896dd0 | -7.9236 | -44.2558 | 2026-09-01 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 2679187e-6add-39ed-ba05-22799b3fdcae | -11.2295 | -51.2667 | 2026-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 193.8 |
| ac54a5b5-5db0-3c3b-9b65-c645174ed301 | -11.7219 | -47.6104 | 2026-09-01 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| aa0e8a81-518b-3497-b3c2-0dbaddf41621 | -10.7274 | -50.6192 | 2026-09-01 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| da5cd003-fe47-361d-b591-f9f519502f15 | -14.6918 | -53.5804 | 2026-09-01 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f7244d22-e65a-3dfc-b176-5137585852e4 | -3.8605 | -44.0355 | 2026-09-01 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 34519e64-92e6-35db-9d71-23e6c06b99d2 | -15.6475 | -50.1062 | 2026-09-01 14:30:00 | GOES-19 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 45fc77b3-e56f-3661-b45b-7a32d9e62846 | -3.6216 | -60.547 | 2026-09-01 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| eaef7e5d-deb4-3ddc-82b8-34f4cc17d1eb | -3.4979 | -59.0409 | 2026-09-01 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7ee70832-4c30-341c-ac86-5342b499ea33 | -13.0897 | -45.163 | 2026-09-01 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 499.5 |
| f3e16134-c6a5-3de0-a22f-6cfcdbcfdc9c | -11.2485 | -51.2647 | 2026-09-01 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 18939b26-dceb-32fd-a226-79d5f92f5d45 | -3.1266 | -61.2188 | 2026-09-01 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ce447868-95b9-3cd3-bcd9-dd9b9f6f727b | -7.5659 | -61.362 | 2026-09-01 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| bb400344-94b0-35c2-90bc-41775a66905a | -7.2191 | -60.6699 | 2026-09-01 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 47b3631f-4503-3d77-9115-4faa581bef65 | -14.6732 | -53.5408 | 2026-09-01 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| bc418b64-6c8f-3231-a27c-e9da96bc123e | -7.9425 | -44.2538 | 2026-09-01 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |


[Clique aqui para ver as próximas entradas](README102.md)
