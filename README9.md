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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36166d71-c474-38ba-968c-a3f62c519b44 | -6.94071 | -43.70111 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15497ffe-fd12-389a-a3fb-06b2c076d714 | -8.13008 | -47.09298 | 2026-07-09 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d230b25-de92-32af-8e17-d63109385f79 | -6.92511 | -43.69969 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 959af6fb-6c34-3ccb-a385-74cfe74f087f | -4.34473 | -47.76693 | 2026-07-09 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 970f442d-f83d-39d4-92bd-28e2a9bc7f5b | -9.80222 | -48.92347 | 2026-07-09 04:51:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ffd0956-a9d2-3d37-bdb3-0cf1aa555832 | -8.72895 | -48.32253 | 2026-07-09 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a61beb7d-9929-3877-b7ed-63a9cd916bfd | -9.33723 | -47.90768 | 2026-07-09 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08063fa3-0ff1-3353-85a9-ba77899eba72 | -2.95991 | -53.15075 | 2026-07-09 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9e71c222-ce91-3975-aa0a-394b60733d4c | -8.3542 | -45.39795 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31c173f2-92e4-3dc0-82e5-13901ddc57bc | -9.56721 | -49.10888 | 2026-07-09 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 668f6398-ac96-34e5-a5fa-49cefafc2504 | -7.7067 | -45.16241 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73c34f38-75be-3700-a5fc-43faa54f53f5 | -10.86657 | -47.59576 | 2026-07-09 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b972257-1236-3c5f-8f4c-7fb82190974b | -6.91938 | -43.70227 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bba762b5-a4b7-3889-a44c-43baa1694d92 | -6.94618 | -43.70258 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba5164d2-7872-3eaf-aed8-fc94bd37d000 | -7.81826 | -49.26534 | 2026-07-09 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72fee889-993d-31b5-aef3-f0932cea15d5 | -11.65184 | -46.35994 | 2026-07-09 04:51:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e030cbdc-cd9b-370c-8bcf-d207e88d31ac | -6.42809 | -55.79829 | 2026-07-09 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f24bdb7-85f6-3c5d-b0ad-89a9183e3362 | -6.12708 | -55.80805 | 2026-07-09 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e35abb3f-b33b-3992-afff-fba2f0d2e87e | -5.48922 | -44.12074 | 2026-07-09 04:51:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 654053b5-cf44-3a55-bae2-72e20c759a7a | -6.42948 | -55.79737 | 2026-07-09 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bbc7838-74bc-3dfa-8c96-e25cf22aafd5 | -7.91783 | -55.40553 | 2026-07-09 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4a7a5c4-c2ed-3277-9e37-de6923684b40 | -9.22061 | -48.5852 | 2026-07-09 04:51:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3d08d5f-fed3-3eed-bef1-97ddb4278db8 | -8.72749 | -47.83794 | 2026-07-09 04:51:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71cbe5b7-1299-3a5b-8d14-2bab458b5a11 | -11.45412 | -47.59357 | 2026-07-09 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8b42793f-7dd3-36d5-a309-5be6c7c4f6f9 | -6.67185 | -47.52108 | 2026-07-09 04:51:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4808539e-2262-3969-817c-dbc44d518347 | -8.72207 | -48.34241 | 2026-07-09 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fe4a29c-d68e-3229-afa4-ed563d82e13a | -9.22525 | -48.58066 | 2026-07-09 04:51:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e38a5d79-453d-3c0c-ab52-01f16d1583fb | -6.94479 | -43.71245 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b6e66a7-fd49-3c5e-a273-f63f978463db | -11.4547 | -47.58938 | 2026-07-09 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bfb7c92-c1d5-3706-931b-bab3758f35ed | -7.28975 | -46.25583 | 2026-07-09 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7094f61a-1b21-39b9-bcf4-6e54d342f8c5 | -9.22133 | -48.5802 | 2026-07-09 04:51:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c174b3f-1a8d-35fc-8d85-860b164adc01 | -9.58174 | -49.1159 | 2026-07-09 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5fbd0f2-319b-34ec-8597-826adfdb79e4 | -6.94598 | -43.70182 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bbbc90f-1eb1-3490-987c-c0a340990cc7 | -8.96453 | -48.01485 | 2026-07-09 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bc21943a-6ed1-36e1-9eb3-6cc5621295d4 | -8.98111 | -49.88449 | 2026-07-09 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02d253ba-0492-3992-89d4-0c5f1502b8dd | -4.34545 | -47.76211 | 2026-07-09 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f54ae2-1c01-32ce-be74-2991d5aa0d6a | -8.11627 | -47.09888 | 2026-07-09 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02343713-7829-30e3-936d-84dd3cbcf6cc | -8.98412 | -49.88926 | 2026-07-09 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b9c8b17-feae-3f57-b6a7-268aead45edd | -5.34114 | -45.35261 | 2026-07-09 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b17e520-0779-376c-85bf-abca97676967 | -9.36766 | -44.72618 | 2026-07-09 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff374f0f-be09-3f52-ae59-b0e0bfe811fb | -6.94511 | -43.70843 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac903954-b84b-3530-9f5b-ee16ab806c65 | -9.37354 | -44.72072 | 2026-07-09 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d003b023-cd15-3b3f-af83-233e0e8dae69 | -8.12803 | -42.96853 | 2026-07-09 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0a9c4fe-40b5-391e-a006-45ad0627c952 | -6.94571 | -43.70587 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dc785c5-d4ba-39d9-921c-645f49f87467 | -9.52153 | -58.35917 | 2026-07-09 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d1a40fb-e2b5-331c-a8da-fae61be57521 | -4.34857 | -47.76754 | 2026-07-09 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2b25385-c0ae-3bfa-ba5c-222fd4f564ce | -8.70549 | -54.5401 | 2026-07-09 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ff8d795-1fe2-3053-b377-2dc59dc5b4fc | -9.36967 | -44.72344 | 2026-07-09 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46024d49-46f2-3821-8806-afdeea641d67 | -10.86231 | -47.59507 | 2026-07-09 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d1923cc-d504-3429-b158-ecb30e9a95f1 | -11.65588 | -46.36573 | 2026-07-09 04:51:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae1afca0-05bc-354a-8f46-fc2421e4575f | -8.71418 | -48.34128 | 2026-07-09 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fb31914-cbb1-3f34-bb16-253b17ebe6e7 | -11.45034 | -47.58918 | 2026-07-09 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d03cb360-1d6c-395d-afa6-4f7390a6d64d | -11.44979 | -47.59319 | 2026-07-09 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 650b967b-30f1-38bd-8b64-1ce216d2aeb4 | -6.91983 | -43.69902 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 994f817f-b9f9-3ad8-8c90-4178f380392d | -8.72281 | -48.33726 | 2026-07-09 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c01132e-f840-3918-996c-29d9e276cea9 | -10.61948 | -48.69483 | 2026-07-09 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bd5082e-9ba4-3641-bb1f-6e35d044b430 | -8.34878 | -45.402 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20e6d56d-ea2f-38d7-be92-3c3ddc5968fe | -5.9207 | -43.85879 | 2026-07-09 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed8e6030-9d54-34b4-91df-7174d0d3782a | -6.92465 | -43.70297 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8530ae8-4998-36bc-b1ee-cd058f2a9472 | -8.73289 | -48.32314 | 2026-07-09 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f87382a-407f-3a24-bb99-89865989211e | -7.71197 | -45.16263 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be16e473-7609-325b-b20b-3362bb36d569 | -6.64945 | -43.9095 | 2026-07-09 04:51:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9750215-2cd0-39f6-9a76-499d55cd5e78 | -9.71649 | -47.77317 | 2026-07-09 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f69d303-5f99-3d2a-a98c-2ffa717a288d | -9.36806 | -44.72307 | 2026-07-09 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cbb980b-acc5-3f3a-ab74-a964a4955b16 | -13.90578 | -53.89039 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8bd1b11c-a157-38eb-8baa-c8cfe7a19df9 | -13.27926 | -45.18507 | 2026-07-09 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e53bcc9-471b-329f-9b42-e8a95ddab0d9 | -10.06256 | -60.49979 | 2026-07-09 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf2eaf9a-f75b-3e6d-8eec-406e14ce402a | -13.28306 | -54.41533 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 648dfe2d-bcf7-3104-adab-953155db674d | -12.75878 | -44.53269 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f0597148-0193-3435-9d96-d5fcf817e85f | -13.95613 | -53.89553 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85b668e3-8817-3ba6-b75a-921bfe624fe3 | -13.28911 | -54.41993 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6b2a548-9de7-3efe-bacb-ad755187b9ce | -13.7705 | -46.29205 | 2026-07-09 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17cca809-603d-3362-8c54-378d7a72509a | -14.14711 | -52.88702 | 2026-07-09 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ce9ca86-746d-33e1-b871-1a95e6780793 | -11.46378 | -52.92452 | 2026-07-09 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 701aa7a8-1bd5-3d2c-80e3-cd4bc50e5202 | -12.9331 | -49.48537 | 2026-07-09 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c79ba37-6776-3304-b2fe-54871ed0793e | -13.28031 | -54.41126 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd67515c-3b9f-322f-b22b-2b3a60db16a8 | -16.7212 | -50.70854 | 2026-07-09 04:53:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1be5f8c5-f056-3ab2-9ae8-1be23fa2a944 | -14.44288 | -48.75981 | 2026-07-09 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ced1e984-cc48-33dc-808c-2e506f1f5d86 | -13.95558 | -53.89907 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9827adb-a07c-37da-8c0b-a337a0f3a133 | -14.44027 | -48.76485 | 2026-07-09 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e6707d4-8525-35bd-b9ef-5444bce113a5 | -12.13693 | -57.21178 | 2026-07-09 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69afe16c-3a0d-32f6-8463-8a795e69a646 | -11.85594 | -49.1904 | 2026-07-09 04:53:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7da46a9e-514b-3bc3-bbc1-c2886f094f62 | -9.01646 | -63.53658 | 2026-07-09 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 333dd6fd-de8d-32ef-aacc-1b4e9dfa1c78 | -12.93532 | -56.62632 | 2026-07-09 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 021bba90-e4d2-3cf1-87a8-811662e6fbaf | -11.8413 | -48.24026 | 2026-07-09 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0897003-a13b-37cd-a857-44b9ba0d5d14 | -12.93467 | -56.63031 | 2026-07-09 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb558ba4-16a0-391a-aa3f-8b48a5c4a83f | -12.35756 | -47.42278 | 2026-07-09 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3707bdb4-ba2d-3caf-9028-5d92db725529 | -16.72055 | -50.71336 | 2026-07-09 04:53:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 11a5ce26-ee02-39e2-9fbc-5f0623b6c004 | -14.03611 | -54.10413 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5b45ec5-63e1-380c-998d-0e1a98ea1f2a | -12.37951 | -54.16965 | 2026-07-09 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f17cc4f-6ba5-3aee-912e-906fe8f696d9 | -11.79176 | -57.01154 | 2026-07-09 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4dc69d1a-4bac-3637-a2cd-775f44a0442b | -9.0222 | -63.53752 | 2026-07-09 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 802c3f3a-4719-3205-b869-c5c24dbe62c9 | -12.93378 | -49.48033 | 2026-07-09 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b45c02c-8e9e-33b5-9b3e-334b012bb395 | -12.15726 | -57.22398 | 2026-07-09 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 461eeb21-6757-3e95-8c08-d317acb7d996 | -14.44337 | -48.75599 | 2026-07-09 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef90f784-619f-31b8-9bff-8474a4adfb33 | -13.77196 | -46.2921 | 2026-07-09 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e839072d-adfb-3a16-b849-6fa0fade5cd5 | -12.83982 | -44.37253 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ae61344-63f5-332b-8db9-32b085239d0c | -12.75919 | -44.52917 | 2026-07-09 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 73a856da-001c-3995-885e-c2a3fff9de7d | -14.0173 | -53.93813 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f698c6f-f205-3c09-8c24-d29158b5f40f | -14.01785 | -53.93458 | 2026-07-09 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README10.md)
