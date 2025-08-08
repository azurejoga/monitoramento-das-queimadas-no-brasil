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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39e0a490-b42f-353f-a108-867b5d07634b | -7.0429 | -59.198 | 2025-08-08 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| bdde221e-7abe-3361-a290-32aeff323fcb | -3.66886 | -41.75692 | 2025-08-08 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b579d12b-0c6c-3cff-83f1-e2efa17e55a4 | -3.26652 | -42.64272 | 2025-08-08 03:40:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd802098-30f4-3e36-90b1-cc25141255f0 | -3.59211 | -41.65304 | 2025-08-08 03:40:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 39fd3959-7e30-33e2-8cdc-3e23c74904b0 | -3.65962 | -41.75521 | 2025-08-08 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 296ca558-77bd-3805-862a-deadbf0b0c53 | -3.81942 | -41.55612 | 2025-08-08 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 557666a5-fdb8-30ae-bb64-2f2b38d03fb5 | -5.36861 | -37.33366 | 2025-08-08 03:40:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 020eec07-397a-3bd1-a479-c07bc6c24814 | -6.04881 | -35.2371 | 2025-08-08 03:40:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1697b282-1bb2-3a38-a294-d171d573174d | -5.36922 | -37.32984 | 2025-08-08 03:40:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e10d27ee-30b6-393d-96e5-4eb8e0d5e200 | -5.15886 | -37.98385 | 2025-08-08 03:40:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e4a854d6-e093-3ce6-8605-0302514c3e01 | -3.94904 | -41.48106 | 2025-08-08 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ad659dd2-79ab-367f-b7ef-2762caa7ed87 | -3.95357 | -41.4818 | 2025-08-08 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| edfef22d-016d-355f-b6b4-bd6bf1713956 | -3.65883 | -41.76006 | 2025-08-08 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 79efe67b-3c8a-314a-8b30-b9a006940132 | -3.33144 | -39.68741 | 2025-08-08 03:40:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e8d95bba-a582-3abd-a361-5a69635d86bb | -3.26156 | -42.64193 | 2025-08-08 03:40:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca0bae6a-48a6-3c2d-94dc-25c2f7d547ca | -3.66425 | -41.75605 | 2025-08-08 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b85ca7fb-b4b2-395e-aa08-5eeb7d995264 | -5.50004 | -35.48592 | 2025-08-08 03:40:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4d0b6337-b227-373c-b0f3-b772786053fe | -3.59671 | -41.65385 | 2025-08-08 03:40:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fcd22c60-51b8-315f-a4f6-39e5abdaab53 | -3.66346 | -41.76086 | 2025-08-08 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5736bfc8-d344-31fc-9654-9fed3111f505 | -5.51226 | -35.58008 | 2025-08-08 03:40:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f73a074-bcdb-318e-bbfa-85bce5fde75a | -3.24735 | -43.26447 | 2025-08-08 03:40:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd66e956-da6a-3c9a-a04c-e38154a95ee0 | -3.24684 | -43.2676 | 2025-08-08 03:40:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb38ba5d-328c-304b-a8da-e06cce699f5f | -3.24855 | -43.26608 | 2025-08-08 03:40:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4472e92-1d31-353a-81be-367461bb4260 | -3.58673 | -41.65702 | 2025-08-08 03:40:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2e0953a3-74c6-3253-ac67-eae9e318fb36 | -3.24802 | -43.26921 | 2025-08-08 03:40:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 945547a4-e538-3f54-95c3-d28e20e02155 | -6.26324 | -45.25987 | 2025-08-08 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 481d42ae-acd7-3cfc-a0ca-ade81317c0a7 | -10.63115 | -44.75901 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 80539541-f041-3ba5-bc0b-71e80e756369 | -5.60248 | -42.28213 | 2025-08-08 03:42:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 714c1666-4f3e-32be-8a29-e0fd6ee6abda | -7.10934 | -44.20965 | 2025-08-08 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61c616da-498b-3a3c-bd4c-9f61ead29945 | -7.03202 | -42.56139 | 2025-08-08 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| af7e7621-3f3e-32fd-b9e7-c8627a72ed59 | -8.24447 | -45.07059 | 2025-08-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efee30c3-3aaf-3e5a-b875-65f2e55fe8d3 | -7.91393 | -45.54795 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52cd0974-0261-3acb-9e32-bd4a49f63811 | -8.24921 | -45.07501 | 2025-08-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19b2a67e-1d68-369c-9d1e-0a0c47b165ad | -7.91314 | -45.54306 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11157e4f-373f-395d-8dd7-8d3544366928 | -9.55086 | -47.88372 | 2025-08-08 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44a6065b-d69b-345e-b315-724b3be25961 | -5.99063 | -40.38696 | 2025-08-08 03:42:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80bb2d48-95f4-3345-b51c-9dc176971a48 | -9.06347 | -45.05744 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dce42ea-fc51-31b5-a7bf-4f82604f35eb | -9.62159 | -40.59692 | 2025-08-08 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 032bc3e9-78e9-3cb0-a8fd-03f7a9478ac7 | -10.63891 | -44.74503 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7c77b51-be32-3891-b7a0-34fb3f6e5ef1 | -10.60988 | -44.76109 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2378a7ee-18a3-3184-9429-cea94b557c52 | -8.52381 | -43.30774 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 197c5c94-9838-31b7-a1d6-7aadb48c9558 | -9.06701 | -45.06813 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13e32566-4393-3bca-8c67-326bbc6c4476 | -7.73737 | -47.39302 | 2025-08-08 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8283be5f-75b4-3676-9d83-584b8c1fc786 | -10.62502 | -44.76399 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 792864ae-6cc7-35c2-ab7b-3c1e56de0db3 | -6.25761 | -45.25892 | 2025-08-08 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aadd4568-e1fe-3e73-99af-eea8e36e8915 | -7.91591 | -45.53681 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e01e3a2d-dbab-35e1-b02d-5c1a6b197791 | -9.06114 | -45.07029 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00993f6a-74b4-388c-94df-7fa36d9b92a6 | -8.85837 | -47.27757 | 2025-08-08 03:42:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d0d74ca-ec62-3e9e-8f69-8dd8f330be12 | -7.91176 | -45.55048 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34d930ef-8ed4-399d-8b88-aaee818de211 | -8.1982 | -46.98985 | 2025-08-08 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9491db9-5e00-3d83-a518-ecbd43fb773e | -5.99045 | -40.38652 | 2025-08-08 03:42:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| febd954b-6c27-303b-9cea-6508de8ab568 | -8.00667 | -43.14094 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d4da6a26-e1c1-32ae-8fe1-fadc9f33f0d7 | -7.91519 | -45.53201 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2383f052-7f76-310d-b053-e8353500d59f | -9.0708 | -45.06915 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7ee510cc-d0c9-398e-9e61-30b04c59812c | -10.62556 | -44.76101 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0a19ea2e-0834-3bff-96d1-094035f50365 | -8.86539 | -47.2739 | 2025-08-08 03:42:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68efce8a-a115-3c66-bdd9-409671b90fdf | -7.38327 | -44.24341 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c74012e4-6cd3-3be1-9868-2ff40adc9cc0 | -7.38932 | -44.2487 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 859c331a-3960-3b52-94b9-8bfb8f4ffcef | -7.8569 | -39.70871 | 2025-08-08 03:42:00 | NOAA-20 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1838bd68-0048-38fe-b6fb-6660ada21282 | -7.37565 | -44.65498 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee51edda-6db9-36ed-b4f6-bda38e201b43 | -8.92683 | -46.74799 | 2025-08-08 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32387ff7-0e6e-358f-876a-9e5347783a38 | -10.43334 | -44.34807 | 2025-08-08 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8be666bc-9496-32ce-b80e-2d30702f3a87 | -6.95908 | -41.58089 | 2025-08-08 03:42:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 47d34675-da78-3657-8962-b258791d4421 | -9.06681 | -45.06126 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3e6b8a9-d2a4-37b1-8310-8fc61868a9bb | -7.32354 | -44.70083 | 2025-08-08 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0904d33-3f0a-39e9-82b0-7523eb26b369 | -6.84321 | -44.30965 | 2025-08-08 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2603e2e0-5a8e-3c63-9921-c2b6cb75faef | -10.53036 | -42.54747 | 2025-08-08 03:42:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 65f4aac2-5ee0-3155-b9a6-79120711394d | -10.57769 | -45.25685 | 2025-08-08 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 15b9d737-5d8b-3788-a9f7-d5b248520391 | -6.15067 | -44.54546 | 2025-08-08 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d9cfd3a-3760-3b9d-9ff4-4ef48b6cbad5 | -8.52776 | -43.3154 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 02e67b1b-ae13-3f7b-b26f-928a2c697ea7 | -6.23063 | -37.42519 | 2025-08-08 03:42:00 | NOAA-20 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2009985e-8792-3a6b-a511-b1db2357205a | -10.63006 | -44.76496 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 27547274-848f-3297-b378-404dfe45d59a | -8.21227 | -45.06461 | 2025-08-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcc80750-3dd5-3d56-91b6-3bbf69114e83 | -6.12549 | -42.95679 | 2025-08-08 03:42:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 4693a2ed-04b6-3346-9b8a-1cdf49a43a6d | -7.02151 | -42.54668 | 2025-08-08 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1e67f03c-54c7-387b-8703-be97e6a41c4a | -7.91525 | -45.54052 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77c07a73-bca9-30ba-81a7-35bffa2b2bed | -8.21292 | -45.06112 | 2025-08-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8519cca-90e6-372b-b414-a7cd7d8686ec | -8.00755 | -43.13584 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8280cb2a-d3b5-3f45-9e11-b93c9addebc2 | -9.07146 | -45.06565 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 864b9e06-0741-3e9f-a73f-7fdbf77926b0 | -9.06576 | -45.07503 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc4422c8-a5fc-3666-bb54-4573edb937c2 | -6.46308 | -44.57499 | 2025-08-08 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4ddd369-f4a5-36dc-a1bc-a057ba1f9121 | -9.4767 | -46.30472 | 2025-08-08 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e08a2518-42eb-3974-83fe-59029e1833cd | -7.38093 | -44.65603 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52baa236-a54b-3bb6-9da2-a122eac430fb | -7.03456 | -42.55401 | 2025-08-08 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 06d53b13-c274-3657-a7a3-8209c09a3684 | -7.37805 | -44.64151 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8587a8ec-1a88-3f7f-80e5-739e52533a83 | -8.85926 | -47.2728 | 2025-08-08 03:42:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ab9b1dc-5166-364d-bd3c-fc6b8c721af1 | -6.55734 | -39.01019 | 2025-08-08 03:42:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6b461712-6ba9-30ee-94f9-ac69a427fec4 | -8.15984 | -42.42213 | 2025-08-08 03:42:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a59ed456-99cc-3aa3-9337-406508a67a34 | -10.63836 | -44.74805 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58131118-116c-3255-9b23-d3f4ae723a14 | -8.00808 | -43.13834 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 29c71519-4614-3bd2-9ed9-8ed452167af4 | -9.0688 | -45.05819 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a48128cf-81c5-3bb6-a1bd-48b4750afbbd | -6.23002 | -37.42898 | 2025-08-08 03:42:00 | NOAA-20 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 432bb828-cb3b-3dae-8bde-12214264aff2 | -10.47742 | -44.38578 | 2025-08-08 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0cbbeccb-b04d-3122-b7ee-2f2c9378a382 | -6.26396 | -45.25585 | 2025-08-08 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be1cf4b9-f236-36a6-93ef-e91c55e6e01f | -8.52767 | -43.31372 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 152dc1dc-48cb-33c8-8e7b-6ad3d8e62503 | -7.10132 | -44.22474 | 2025-08-08 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41bd674d-22a4-312a-a982-46beb1bd6d65 | -9.07161 | -45.07295 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aceceb6d-e4f2-30c5-a1f9-d3f9487335bb | -7.25502 | -44.33337 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64c3474b-4e1b-36cb-9b77-bda225a086cd | -7.1469 | -44.48328 | 2025-08-08 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1367502d-57c0-39dd-92fd-241079d57c8d | -6.46049 | -44.57535 | 2025-08-08 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
