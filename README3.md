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
| 54daf7ab-d66b-34dd-ace8-8a5cc00afb50 | -10.7108 | -44.9081 | 2024-11-08 00:10:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ac71003-189a-38dc-ae7c-e1d003c2c4bd | -5.9805 | -45.363602 | 2024-11-08 00:10:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0977c2fe-11b3-3957-8374-0c808b86baa7 | -5.8453 | -45.3097 | 2024-11-08 00:10:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 728fdf48-56df-31e9-8c5e-54e6bf017a63 | -9.8495 | -36.1842 | 2024-11-08 00:10:00 | METOP-C | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ffa8075-4ef5-3b15-9cdc-1efb62d1b08e | -3.1583 | -45.796501 | 2024-11-08 00:10:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 663125b3-7b38-3cb0-8a4f-10ea32880ced | -2.0175 | -46.571999 | 2024-11-08 00:10:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52adb7f5-c513-361b-9853-6d1efad1ad02 | -5.6555 | -45.195801 | 2024-11-08 00:10:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| feafefe2-b009-313d-9151-7c2b0f0bb968 | -3.9686 | -48.172699 | 2024-11-08 00:10:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b78c1aa3-8da1-3060-badb-ecc550422ad9 | -3.3713 | -46.102001 | 2024-11-08 00:10:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fba126d3-a4cd-3b74-9461-c2e5271f81d5 | -5.5434 | -44.326401 | 2024-11-08 00:10:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 054bd38f-923e-3629-b8d6-067a6fdba267 | -2.666 | -51.804901 | 2024-11-08 00:10:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0892f082-c5bc-3b84-b551-8b7d330b5221 | -3.1598 | -44.394798 | 2024-11-08 00:10:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb1ad8f7-042a-34b6-96a3-75e595ec78d5 | -5.1716 | -44.229301 | 2024-11-08 00:10:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3de9c7a9-57d6-36fb-8c77-33d54e90fa89 | -4.8842 | -41.783401 | 2024-11-08 00:10:00 | METOP-C | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 600f2547-2edd-3f35-a17b-4542147071b9 | -2.7127 | -45.056599 | 2024-11-08 00:10:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fba58b88-fd1c-3239-a084-70c1010acb1a | -8.5666 | -35.116699 | 2024-11-08 00:10:00 | METOP-C | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7101cdb-76e9-3006-8bb2-4dcd22f6ee57 | -2.6919 | -45.9627 | 2024-11-08 00:10:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 80dac59b-5716-32d1-933e-37300a1b3695 | -3.27 | -45.7901 | 2024-11-08 00:10:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fcbfeb54-05f3-3d10-8833-bcf7e950a497 | -5.9767 | -43.369701 | 2024-11-08 00:10:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| d94cb0c9-30ef-353c-ac3a-d5a070ae020b | -8.5637 | -35.104698 | 2024-11-08 00:10:00 | METOP-C | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a38ed0ff-9840-3f5b-a083-5b040f11b65b | -8.5569 | -35.118999 | 2024-11-08 00:10:00 | METOP-C | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 614d4f9c-d691-3bc7-b868-c641c1ca904a | -3.2448 | -45.678299 | 2024-11-08 00:10:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6159dca-09c6-369c-af25-3110ede06244 | -3.0722 | -45.7342 | 2024-11-08 00:10:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46cfd4ed-1840-3043-99a2-522777bc1e8d | -3.0644 | -45.7449 | 2024-11-08 00:10:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b5f526f-7b61-336e-bc64-43ce3381c706 | -6.2593 | -39.381199 | 2024-11-08 00:10:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fbd12c91-5cae-30e2-88cb-979f65510725 | -2.7145 | -45.0644 | 2024-11-08 00:10:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f991330f-a26d-3765-8bc5-780a0b432cb9 | -10.2662 | -36.497398 | 2024-11-08 00:10:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 913e1ad5-63bf-35ca-8557-0fabb52b7581 | -9.0899 | -43.0238 | 2024-11-08 00:10:00 | METOP-C | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9c5d14d0-a2aa-3fc5-adce-de420c87eb7b | -3.5549 | -47.375801 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ec121ac-3c10-3538-8435-99fff475665f | -3.5573 | -47.3866 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c9a8a7-beee-3919-8a28-1bf6ceee121d | -3.3479 | -45.27 | 2024-11-08 00:10:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3ceaa5e-9154-37a8-a021-2c4d38b69381 | -3.7994 | -47.781502 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ed2aea-7a67-3d1e-8e0c-aabd5f525e2b | -3.3733 | -46.111 | 2024-11-08 00:10:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 108d7db9-8e0d-3d5f-bd6d-e81f586abf48 | -2.3979 | -45.9366 | 2024-11-08 00:10:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 75ac8be6-cd59-3643-b822-e36a217e4db9 | -2.3959 | -45.928001 | 2024-11-08 00:10:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93fb3e27-c14b-3633-b1c2-5f861e2b3396 | -3.5525 | -47.364899 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80b7a63d-5836-308a-947f-69753c5992b6 | -6.7474 | -39.260899 | 2024-11-08 00:10:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 32751b79-6c3c-3011-a5df-6ae9caeec010 | -3.0742 | -45.742699 | 2024-11-08 00:10:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35752864-2174-342d-a4ce-ea4181d35a6f | -4.2102 | -44.257301 | 2024-11-08 00:10:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbdfc300-0c0e-39dd-8f0c-c1efaea61a2b | -3.802 | -47.793098 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35828ce8-498e-3a32-8989-43e711761ce3 | -3.5402 | -47.356201 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb2b404-aef3-3b73-ac28-a643306d1ba3 | -3.0663 | -45.753502 | 2024-11-08 00:10:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e42c3431-abf6-37a7-a31d-0d8ee97b41f1 | -4.5166 | -45.663898 | 2024-11-08 00:10:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9e40621-e31e-3c7f-bad7-1cbc3b9d655f | -10.2685 | -36.506802 | 2024-11-08 00:10:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 13dbe0d3-75cc-3725-89e2-a4ccdfdbf301 | -2.7047 | -45.066601 | 2024-11-08 00:10:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e34d04a-f4e3-355f-afbd-747d3cd3ea6e | -2.0077 | -46.5741 | 2024-11-08 00:10:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f8d43fe-97f9-3ecb-8df2-8b1cc1ff9f5e | -6.4847 | -43.613899 | 2024-11-08 00:10:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5be58ad2-a965-3ec4-a299-d105e6928b68 | -5.9865 | -43.3675 | 2024-11-08 00:10:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 4ff15d5b-5d60-3387-841d-15e75b689c6d | -3.956 | -48.162399 | 2024-11-08 00:10:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 930fa63b-d4b1-3c8d-a683-809bdccffef5 | -3.5329 | -44.359402 | 2024-11-08 00:10:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0e240bc-c1b6-3bc3-b60a-0f9fb78aaf75 | -10.1696 | -36.311199 | 2024-11-08 00:10:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9b98141c-cb34-3ca1-b43c-865714bee334 | -8.5539 | -35.107101 | 2024-11-08 00:10:00 | METOP-C | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa6d5135-fd5e-3966-9055-b2e4829715d8 | -9.1478 | -43.146198 | 2024-11-08 00:10:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5694d360-9d55-385c-be81-f2198ccdca68 | -3.4378 | -46.0779 | 2024-11-08 00:10:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| deb10e73-70e6-3860-bec3-20460d6b8125 | -9.3702 | -35.784801 | 2024-11-08 00:10:00 | METOP-C | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c69bb8e9-725a-30f4-8d07-88c0eeb04c8b | -2.7163 | -45.0723 | 2024-11-08 00:10:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38801a41-e404-300e-bd5f-f1bd2ebaee83 | -2.5226 | -45.443199 | 2024-11-08 00:10:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dca0d83b-0d8e-354a-a3bd-0128c5f1c4fe | -9.7408 | -43.5989 | 2024-11-08 00:10:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f0073642-83b0-36e1-883b-9ff978cf4ad2 | -3.7169 | -41.686699 | 2024-11-08 00:10:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 30013f2a-e3a0-3d7e-bf1a-466847ec81b2 | -7.5467 | -44.0867 | 2024-11-08 00:10:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 01a4b312-421e-3164-8761-3b6453643eec | -4.3147 | -45.680302 | 2024-11-08 00:10:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d149943e-acbe-3223-ba0b-47099391c6a7 | -7.174 | -37.912201 | 2024-11-08 00:10:00 | METOP-C | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| b8ef363f-140f-30c3-80f0-fa75f69ee185 | -2.7121 | -45.688702 | 2024-11-08 00:10:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 457ec041-0e91-37fb-a276-f1decadb32ef | -9.1461 | -43.1385 | 2024-11-08 00:10:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cc5bfe17-7296-33c1-8fa2-ac94ae9933e6 | -3.9532 | -48.150002 | 2024-11-08 00:10:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95e5bf62-fd68-3845-89a6-7f185dc9bc51 | -9.7426 | -43.606899 | 2024-11-08 00:10:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bd55abda-8833-387b-ac3e-bc9b49cbc705 | -2.8747 | -46.771 | 2024-11-08 00:10:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c192460b-3f11-3255-937a-a2000a820cfb | -3.5353 | -47.380001 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53cb3bf6-25f6-305a-8833-8c05ed0483a0 | -3.91 | -44.751301 | 2024-11-08 00:10:00 | METOP-C | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb59d786-7a5a-3fe7-92e7-7e6eb1d36297 | -5.0697 | -47.9226 | 2024-11-08 00:10:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f92ce35b-e4aa-39e5-a50d-73a3154a877a | -2.9023 | -45.620201 | 2024-11-08 00:10:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bdb50dfa-a3b8-380e-af70-60978f5f608a | -3.3461 | -45.261799 | 2024-11-08 00:10:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe57694-4a76-302a-9cb9-ac939c3b8205 | -8.1215 | -42.9259 | 2024-11-08 00:10:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a2bce57a-faa3-3849-ac9b-e7918a45a642 | -4.2119 | -44.2649 | 2024-11-08 00:10:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ef9468c-6ea4-388b-94c9-548f1f7a8703 | -3.5329 | -47.369202 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8f80b16-955f-329f-b624-80a33c3502d3 | -2.0154 | -46.562698 | 2024-11-08 00:10:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 166a5ad4-9c64-3bcc-8fc9-276adc8450ab | -3.2461 | -46.458599 | 2024-11-08 00:10:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f83eac13-00c6-322a-8e4e-65aaf71a5483 | -2.6613 | -51.783798 | 2024-11-08 00:10:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e74850a-2d3f-3ff3-9745-017b447cbae3 | -8.495 | -42.112301 | 2024-11-08 00:10:00 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 142a848d-9456-3009-bb71-f914b71e02f0 | -7.0328 | -43.579899 | 2024-11-08 00:10:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3106778a-2d1e-3591-8f37-577a3dbc0e52 | -3.1994 | -44.433201 | 2024-11-08 00:10:00 | METOP-C | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0721d5a-694c-325f-b97f-2255fc73a647 | -6.2558 | -39.366299 | 2024-11-08 00:10:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1ac851bf-dedb-313c-8713-67cdabf7c45b | -10.0185 | -36.327801 | 2024-11-08 00:10:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| c21a1cc6-2959-3c74-a17e-8ffdc285adc3 | -7.0213 | -43.5746 | 2024-11-08 00:10:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c9fd706-7379-3bc1-a3b0-1bddbd847219 | -5.9785 | -45.354698 | 2024-11-08 00:10:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96772dd7-ccda-387b-a8b9-b6ce051d1b99 | -5.1699 | -44.2216 | 2024-11-08 00:10:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45bf15e4-ba0e-323d-9e2a-ad4c6a88e502 | -4.3069 | -45.691299 | 2024-11-08 00:10:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed29a7de-ef99-3ff1-81da-de0d1ddd2afc | -5.9825 | -45.372501 | 2024-11-08 00:10:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e1d0264-8401-34e6-b296-bdea17c3930b | -4.6958 | -46.373699 | 2024-11-08 00:10:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d8e532d-e7eb-3e6b-847e-f451b8eb5ef4 | -5.5749 | -43.141102 | 2024-11-08 00:10:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 1887e47b-1712-3f60-9138-956db0149704 | -8.1411 | -42.8755 | 2024-11-08 00:10:00 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a6a996d3-64f9-3672-9978-ee923855f3ec | -3.4358 | -46.068901 | 2024-11-08 00:10:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d81f1efa-a682-38a7-aedc-14c42334a9b8 | -3.5451 | -47.377899 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd2714e3-444a-3a52-a30a-86e6668572c8 | -3.7185 | -41.6936 | 2024-11-08 00:10:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 854f4b3f-2516-3738-8a7f-df72bdc93d26 | -5.0823 | -47.932999 | 2024-11-08 00:10:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a56087d-b14f-3225-878c-bc45efb341a1 | -3.5962 | -44.911499 | 2024-11-08 00:10:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 02b6699c-cbc9-33f1-a352-bfbd210465e6 | -7.468 | -43.547798 | 2024-11-08 00:10:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6973aae4-cb0e-3c3c-a383-a0a327938dfe | -3.7154 | -41.679901 | 2024-11-08 00:10:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49336962-5386-3e22-aa6a-78a14e12c63c | -3.9658 | -48.160301 | 2024-11-08 00:10:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca7065d-9c43-3194-bdfb-99547484bfd5 | -3.8661 | -40.765301 | 2024-11-08 00:14:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README4.md)
