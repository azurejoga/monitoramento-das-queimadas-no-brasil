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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 491c6834-658f-3fd4-9a38-258d74d570bd | -5.62527 | -44.35778 | 2025-07-14 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a68d5b12-649b-3f70-8d77-9bf2cfcc5cb8 | -6.28652 | -43.41277 | 2025-07-14 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01023f56-84e5-34aa-9601-c2c5d87eb05d | -5.62447 | -44.36265 | 2025-07-14 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d2e5235-8af2-342f-adc8-aef30e35e21e | -10.28393 | -47.61181 | 2025-07-14 04:02:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 981c981a-dabc-3039-be9d-5b931e78cbf8 | -7.27273 | -45.31902 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cdbd805-1a01-32a1-be2d-c807ec03a333 | -6.81277 | -42.83966 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6916242-f6a9-336e-a402-fac510b187e9 | -8.51947 | -43.30115 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| a91b43da-b11e-31d4-9f59-75937b64f83e | -11.59498 | -43.20956 | 2025-07-14 04:02:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 16824b12-3875-3a55-bb17-dbbf49703522 | -7.28375 | -45.3028 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53d26267-988e-38b0-8f3f-f3a5e17e973a | -6.46934 | -45.37062 | 2025-07-14 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30c8996f-9614-38bc-892e-5c212870cbb8 | -6.94319 | -42.73082 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18cf3149-7fe9-3e8c-96d2-1a19e0b92240 | -7.29395 | -44.62324 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0025ed13-fece-3a45-aea1-4e6444f37c83 | -6.99122 | -44.48135 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf8cf814-f25b-38a1-8d9e-7487088581c5 | -8.51111 | -43.30798 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| b4fa1812-eda8-360a-b4b5-2645f9c72590 | -9.49154 | -40.38845 | 2025-07-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 86a041ec-3e0a-3476-915c-9f8320c24124 | -3.98398 | -48.41694 | 2025-07-14 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05d093e0-34ae-3316-b67e-bb2fc4108cc1 | -6.27495 | -43.4122 | 2025-07-14 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 402f7cdc-dd69-33d3-a6dd-434967e128c5 | -7.60122 | -46.26855 | 2025-07-14 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0c647a7-9c60-3ac1-bf64-a854db08b668 | -7.16847 | -42.97237 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2ee3de30-e52b-3537-8bd0-c7ce871ddb33 | -6.81212 | -42.84364 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9a8ea45b-9f59-3354-a144-c8b10143146e | -9.41424 | -40.46871 | 2025-07-14 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f45e7877-b274-3979-9fec-6e6e08a028cc | -4.53322 | -48.02325 | 2025-07-14 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a498ae73-ff0d-39bd-906f-0d3e2562db77 | -9.16629 | -43.34187 | 2025-07-14 04:02:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf47efb6-826f-3678-afaa-15961ac8d7da | -10.5557 | -45.11127 | 2025-07-14 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8130a165-e392-32c4-85d6-cd7c8b698b9d | -7.01995 | -44.37971 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2404324-b401-3032-afa3-b993b07cf2e7 | -6.82584 | -42.87018 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f023e7d2-2631-3248-8af1-a12a7a46ab91 | -8.8751 | -46.86922 | 2025-07-14 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d386cada-bcbe-3557-9b3f-4368cbcdac9a | -5.68829 | -41.40357 | 2025-07-14 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d479d6d5-0598-32ef-8c74-c890412ccf18 | -8.87433 | -46.89914 | 2025-07-14 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b2e8de2-3ff7-365b-861f-3b9897811f5b | -4.30258 | -48.10644 | 2025-07-14 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| dcf46b21-92ed-3982-a80c-f56788146ad3 | -7.33531 | -45.31496 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24a8b808-be1b-374d-b7e3-bc481f87414b | -5.7353 | -39.54675 | 2025-07-14 04:02:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e7de6466-c40f-39b8-b974-4bcfad130e9d | -9.49421 | -47.56582 | 2025-07-14 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8890d1cc-25fa-3beb-9687-9ba2d79e9658 | -11.03101 | -47.07978 | 2025-07-14 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce33d999-5e34-3f6f-b125-31957c35a888 | -6.75876 | -47.36407 | 2025-07-14 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e291c37-20dc-3304-b8f5-967e81bc9d4a | -10.27948 | -47.61106 | 2025-07-14 04:02:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 532432a5-bda7-3d35-9e50-cde075b9bb22 | -7.03527 | -44.35798 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8031b1ae-234a-3b57-b184-4d460514fb47 | -6.70617 | -43.89995 | 2025-07-14 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77aa59ac-8523-3858-b15c-1e6108e7b562 | -6.43627 | -45.34274 | 2025-07-14 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 235d70e3-0891-3160-af4c-0c3b6df0a64c | -7.24461 | -46.97932 | 2025-07-14 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2842ae7d-94fd-3f41-9538-00e34b6ed09a | -8.50824 | -43.30341 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 5b01ce57-c74d-3659-a85d-dfbe4f220ce1 | -10.65509 | -49.44245 | 2025-07-14 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9db750c-e794-30f2-ae33-8ff5e5dad5fb | -11.0324 | -47.07189 | 2025-07-14 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52c83b91-db9d-3d17-8e4f-36cebe98f400 | -8.44107 | -45.80269 | 2025-07-14 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1389e35f-d312-3bd4-a0ae-ebd5b27a8e13 | -7.15206 | -42.28966 | 2025-07-14 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b1399a7-ec0f-3565-932a-09efaaed5eb5 | -9.51221 | -47.56885 | 2025-07-14 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b869566-e08d-39b2-8f3f-ab2b211613bf | -8.50758 | -43.3074 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 8bd4ab26-5d5d-3ffc-8f86-22c06686eeb5 | -6.75088 | -50.92683 | 2025-07-14 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c56b2791-eeba-3521-b375-681c2adcde79 | -9.45533 | -40.37881 | 2025-07-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 22b17d21-4f13-3176-ac90-f04873f781c6 | -6.16337 | -45.88223 | 2025-07-14 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82b9dacd-18ac-32c3-8b59-5b302258af43 | -7.27051 | -45.30785 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09ce9656-1ea3-3caa-b697-280ae94279f4 | -4.57067 | -43.09387 | 2025-07-14 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f389d0a8-e252-36b7-8929-ed8a71284927 | -10.57313 | -49.12738 | 2025-07-14 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| caa595eb-5084-382b-8fa9-49b4ffe4e54b | -7.19091 | -42.96778 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01d5ec31-3f6b-335b-b31b-b58e1ac1dad7 | -7.26126 | -45.3136 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 562eb449-f5ba-3f67-969d-5439ec7aee95 | -4.01604 | -49.47149 | 2025-07-14 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1a0af9e-d684-358e-a349-9d2a63ad499f | -8.51882 | -43.30514 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 9444f4a3-6300-357f-a6ee-b6448cf009ec | -6.9844 | -41.4259 | 2025-07-14 04:02:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| facefbad-88a4-330b-8078-fe77e9afd3e7 | -7.02378 | -44.38017 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e36a567-c773-391d-8680-4233d3b4057d | -6.71061 | -43.89611 | 2025-07-14 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7edf650c-99a4-3a57-81e4-384e7854cdd8 | -8.91436 | -47.34159 | 2025-07-14 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e693e580-66a2-3bc1-b12c-0e701bd99115 | -7.53901 | -45.24994 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a6709d0-dd72-3906-9a7d-8661d37b8e10 | -7.04058 | -44.37309 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 362cbefb-8883-3476-918b-d69b4215ba69 | -6.13919 | -44.09066 | 2025-07-14 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6083489-1b7e-3f51-8048-d43f529fb5de | -7.22644 | -43.99857 | 2025-07-14 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67762e14-378f-3015-9101-364ace31ca30 | -8.59884 | -47.3093 | 2025-07-14 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c81d8b29-e207-3740-b9f9-e22395923cd1 | -8.04455 | -50.09047 | 2025-07-14 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 58ee756e-6185-3f29-a51a-5c8e526c4316 | -7.19443 | -42.96836 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7242ddf0-bab4-3811-aafc-b09b4701314b | -5.24179 | -40.87016 | 2025-07-14 04:02:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 85e01839-3dba-3259-93ea-f57795c84349 | -8.04562 | -50.09041 | 2025-07-14 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| dc7cdf87-d26b-3879-bbb7-95a4f829deed | -8.0439 | -50.09411 | 2025-07-14 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 51ac56d3-228c-33a6-b3fb-e5369059afac | -7.18671 | -43.01636 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5bb54232-628a-39e0-9260-4a696e7320dd | -5.46276 | -44.85923 | 2025-07-14 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e3cf37a-bd48-32f9-9776-422a516bf84d | -10.16525 | -48.30111 | 2025-07-14 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d83c69a6-594f-3681-8517-36eb044ff500 | -8.86647 | -46.86756 | 2025-07-14 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e96e540d-8f22-3c1a-a9cb-9c0bb3cd36b0 | -8.91358 | -47.34606 | 2025-07-14 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a695cc74-0d82-3bda-bc9a-733ff55ccfb4 | -5.51127 | -42.20378 | 2025-07-14 04:02:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e4efc1be-60ce-32ef-85a3-cbe495a29b49 | -8.50889 | -43.29942 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| dcb94082-a405-3691-abcc-48695768bd74 | -8.51176 | -43.30398 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 60cad0d0-20a9-35c1-a9eb-716b682da947 | -7.04212 | -44.36378 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c7e58e7-5317-3174-afae-0b6fc7b9c6d5 | -3.97876 | -48.41602 | 2025-07-14 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d59d2313-ed77-3f28-a219-28ac79d2945c | -7.18487 | -47.1629 | 2025-07-14 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78017550-500b-3d01-8e41-dbe0c19785bb | -7.31068 | -50.06565 | 2025-07-14 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d23785f4-096e-3f9a-8913-5123b0c940e8 | -10.99496 | -47.08565 | 2025-07-14 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baf912b5-1ac7-36fb-8b42-a89a83d6cf44 | -7.03145 | -44.35752 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad744b05-625a-3d01-bafa-d1931374a5a3 | -10.56822 | -49.12647 | 2025-07-14 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6d806d4-f049-386d-8dc3-23221e500302 | -7.26468 | -45.31778 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eeeb7c73-4773-3006-b27a-677bad15596c | -6.84604 | -42.76834 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d1d280ed-ec85-3b10-bd68-d250781883d1 | -6.81343 | -42.83568 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dcf4d85c-ab71-3291-8590-fc1a19ad45da | -6.91563 | -44.25963 | 2025-07-14 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56293d82-fbdf-3318-a43e-543bc99ead08 | -6.96289 | -42.74202 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c1929e0b-aa5c-3194-8ca5-881ea499ae6b | -11.71683 | -47.041 | 2025-07-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a03bfebf-9721-3648-bb2d-6d2a157025e9 | -11.71679 | -47.01671 | 2025-07-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6fe4764a-2d34-3abb-82ad-bba407137530 | -13.02029 | -47.81635 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44a0e5c6-1f7b-33d3-a312-ac3adfb6db3e | -13.03661 | -47.81272 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6a43993-0c0a-3b9e-8dd6-f89904298eb9 | -13.02607 | -47.80882 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61069309-96e5-3fd0-b411-a655c06892bb | -11.71609 | -47.02064 | 2025-07-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b4b3d23-ab43-3c07-827d-b53369fdb828 | -16.73167 | -51.76397 | 2025-07-14 04:04:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 52aaeac2-3558-36ad-a605-dd975cb3d130 | -12.13385 | -45.89369 | 2025-07-14 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5b9df35e-4d14-37ac-8919-b6961e9abe9c | -13.18691 | -47.2725 | 2025-07-14 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README6.md)
