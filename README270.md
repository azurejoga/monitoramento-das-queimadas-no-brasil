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

## Dados Diários - Página 270

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9157889f-37b4-37fc-a1fa-71120055dd5c | -8.60134 | -47.12749 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8f19b8f-955d-320d-87a5-1c08a4da01c2 | -8.28226 | -45.71561 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8f2f0e43-d322-3b01-ae92-378d2278b8d5 | -8.59081 | -45.08637 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d70e96e9-878a-3b06-afbf-3ed915a64713 | -10.07474 | -46.00801 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5d4a82fc-e9d8-32be-bf9b-d0e83c0c28bc | -11.21195 | -44.86444 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 82bf9dde-1db7-3536-8048-03f8a49dbf0d | -12.76628 | -44.87177 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 38f4e5a6-c96e-33b4-86ad-92ba4a885fd6 | -12.98696 | -47.06379 | 2026-10-08 16:18:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 38fe2238-48e3-3122-854d-7dca0e50871d | -8.28595 | -45.70757 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a0f6a548-99fb-3fef-8dcb-8a961bd18bdd | -9.81835 | -45.68575 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| da014bb4-7d04-3877-a800-0e4ab2cb8fc7 | -11.60598 | -38.98448 | 2026-10-08 16:18:00 | NPP-375 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| c18bf2e1-2a01-3989-ae82-16b6e475d6ee | -11.77739 | -45.58868 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 92b6bae3-ec8e-38c6-8132-f4e1cc5dbffd | -12.24612 | -44.73203 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc9b8eb6-8aa5-3565-af53-8ea12aa7e973 | -11.76052 | -44.931 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f7eeac1d-2cf0-39f2-8a4d-1bca72283628 | -11.76313 | -45.55376 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e1c8df41-5c02-3e2a-a42a-63b57a5001cc | -8.93906 | -45.18114 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.9 |
| b9f7da28-5ad9-332d-b50e-17753cdefcc0 | -11.76915 | -43.54197 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| f2c11dc4-5b59-3af5-a6f0-306438dbbff8 | -12.04509 | -43.43402 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 64ede2b5-b3c5-3bef-a859-111d932674c1 | -8.94303 | -45.14497 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| a2418284-52e8-39b3-999b-5b62a42cc44a | -8.79875 | -47.04628 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c999d167-28f8-3200-8ff8-41ed38c98eea | -10.76861 | -46.57862 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bf78affa-792c-3d85-9672-9f5b62a38b9a | -11.23314 | -45.24028 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 40705429-19c6-3769-84d1-09018891245b | -11.76917 | -44.68428 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 06cbda96-5b47-389c-9b87-60abbc003167 | -8.93139 | -45.19114 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 96c5cb4a-ce65-38e1-8d7a-e7968bbe28d5 | -11.11391 | -44.00059 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5dc7810d-4dbd-34f4-959e-6512ca7293be | -8.53802 | -46.91655 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bde81737-bcb6-3b14-845b-09e3e922ce7b | -10.45744 | -47.23588 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 87b4ba6e-0bd6-3048-b775-7b7fc91666e9 | -13.61367 | -48.1935 | 2026-10-08 16:18:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee9c2fd7-4cec-35a4-a6f0-c572219b037b | -10.08832 | -46.00027 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 567f492f-9bba-35a9-94d9-aca4258b0da4 | -10.44307 | -47.29065 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4c43f30a-61ee-3d06-8d95-be472f44e940 | -10.45321 | -47.28635 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5d103c2d-5378-30de-a452-5164e7495855 | -11.40622 | -46.69363 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2f58f6d3-ab06-371b-b2b1-dbef10756331 | -13.34219 | -38.98512 | 2026-10-08 16:18:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5ce45e71-6ae7-3c71-bf08-12defa9d4807 | -9.83288 | -47.46989 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 69cdb751-40cc-377c-bea8-94ed6f1025a0 | -10.98535 | -45.39863 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| eae42d65-abd3-349d-ba70-65c24e9f7cdb | -10.41518 | -47.28102 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f03f7af6-98b4-3298-81e8-109566851d9e | -11.40609 | -47.56319 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d433f194-67df-33ac-a2da-e495e34c042a | -9.53191 | -45.62432 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 03f4cc9d-5208-344c-9dcb-f203b883003e | -9.84701 | -47.85101 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 2d489301-4075-370e-a723-4981d721227e | -11.71519 | -43.657 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0952a34f-2ff4-337b-aadb-644919356580 | -8.52623 | -46.90878 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c987af2d-355e-383f-a3e8-853fbd511f8b | -12.23039 | -44.75309 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| b98eb183-db25-32f0-9381-e7d44e796abd | -11.40235 | -46.68056 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 38f96cc0-d492-3a3f-ac7d-f2b4e8ca5d86 | -9.88848 | -46.10447 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4a2813cf-1752-3683-a82f-1d77b091125d | -10.47396 | -47.24017 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 077276b6-b54c-3991-b2dd-5a9b9c96f2c6 | -8.18711 | -45.76743 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 930413b7-f750-3528-8bfa-186b7d7af18d | -11.11499 | -44.0085 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6ec12dc1-20c4-3dd1-b872-c9f6accd18c5 | -9.4405 | -44.60288 | 2026-10-08 16:18:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| af902178-7fd5-32b8-a9f1-5386dfdb7330 | -11.8534 | -48.03051 | 2026-10-08 16:18:00 | NPP-375 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 59369c0f-17ac-313f-ab2c-9daefb6ccbef | -9.89653 | -45.1927 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6b430d04-d48a-30f4-a45a-a7f8872c348c | -10.84367 | -48.12945 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9017d035-0c03-3d62-82fc-60f6b6651fc6 | -9.13881 | -45.84521 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 6ddc2c66-1eac-3782-abaa-71114ac8283b | -11.77469 | -45.56819 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d3dab0ac-a7e3-3d97-b559-8eee5b1b9ff1 | -11.31392 | -46.67881 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 32c7ef00-22cf-3e99-b1e9-bd78cf1a9250 | -11.08796 | -44.00005 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 0721748a-a5d8-3366-9ee2-1226285a9e92 | -11.62784 | -43.70769 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| b2648e74-2e30-3045-88c3-e0a2ed22cf52 | -11.73052 | -43.50509 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| f14fe3be-6966-33d7-8277-1b3803787888 | -11.48705 | -47.59364 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8e78bef-4ff5-31aa-9eae-472df0e6b724 | -11.85401 | -46.79103 | 2026-10-08 16:18:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c9b445b3-fd34-30ba-97aa-384b39ab06df | -14.00414 | -48.76268 | 2026-10-08 16:18:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 322b57fd-08af-3b25-b488-d44952d6b11f | -11.24715 | -46.27484 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 048aece1-c532-3c75-b2ed-bdd9737bd43e | -8.96658 | -45.12531 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a3d80779-e396-32b3-905d-d34e68b45d9a | -9.76094 | -44.79074 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bd44b4e0-4bdc-3df5-a5b9-78d36064d429 | -10.15607 | -40.53075 | 2026-10-08 16:18:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 38074b07-05a7-342a-a17f-4e1b0a26e867 | -8.94625 | -45.13573 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| ef959953-15e1-341e-b0fb-6bdada07b421 | -9.43996 | -44.59889 | 2026-10-08 16:18:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6374f7b4-a33c-33bd-a701-103d5230bc5d | -13.70332 | -49.1219 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| a877f790-929c-36d2-9b07-cf22ad9b61cb | -8.28977 | -45.73444 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 217f3b36-2d98-32f2-bb76-be14311ca0ef | -10.99197 | -45.41278 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 710ba8d1-b938-3efc-98ce-45ee598409ba | -10.07174 | -45.69643 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 49a0aa7b-757e-32d3-81ae-577eeb89db84 | -12.23473 | -44.71488 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d9a1d018-97c7-3099-b894-c64adcf3710f | -10.76475 | -46.57996 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 770f0eff-fe74-3af7-8c0f-493077a17562 | -14.58552 | -47.53205 | 2026-10-08 16:18:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b775e691-7f6c-3681-8c72-d5c34bcd8167 | -11.72547 | -43.4251 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6ef03c22-223d-3584-aa7c-0204681a391b | -10.04044 | -45.60512 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 563a2c56-28f7-3f46-8e51-2cbefdc8c542 | -11.40285 | -47.55253 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39dee570-7608-3489-b2bb-b9c4d1faf009 | -9.5352 | -45.614 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 6adeadc5-6a0f-3f70-b32f-d0df5020ea65 | -8.94547 | -45.16232 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a5406e7e-b448-3488-97d2-b417d06fd36a | -11.23384 | -46.24003 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e6f9fcd4-b784-3754-bddc-699f7e0c5ac7 | -9.10896 | -45.12069 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6ce877e9-0f28-3239-91fa-9b1919cece00 | -8.7554 | -44.14835 | 2026-10-08 16:18:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 77c1a596-2638-30ef-9548-f584c384899c | -10.68469 | -47.83429 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 87472b36-d4b3-3b74-9f85-fed99dff559c | -8.29136 | -45.71409 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 44d784a6-6df5-30f7-8be4-96a3812361d7 | -8.95933 | -47.54697 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ecd54c98-b63d-3711-8436-66db6002808d | -13.68263 | -49.10484 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9fe1519-5ccb-3772-8e11-61d41c1bc269 | -10.53618 | -47.26702 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7dc607e2-ec7f-3d66-a9b2-e03e639faf92 | -11.26253 | -45.17795 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82f42b81-6a96-3a9c-b8e3-2332c9119703 | -12.83957 | -45.58339 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 196fa425-ef39-318d-97bf-f8b1bdf4567d | -12.84588 | -44.62193 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef498b70-e53c-3eea-9666-fa05c59b53bd | -8.75487 | -44.14457 | 2026-10-08 16:18:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 10b45e48-1886-3a1d-94d5-c041b56ddaae | -11.97237 | -39.0476 | 2026-10-08 16:18:00 | NPP-375 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 2dfdb75c-be1c-3ea3-b998-8eead9fdb9eb | -11.10448 | -47.70933 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7485a16-a6bc-33d8-92f3-128b5663ee44 | -10.77783 | -46.57074 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f3160c5b-e657-353d-9527-d0fa3a3bab65 | -11.09116 | -44.02385 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 422bb935-3470-32fd-a597-c4330baee6ba | -9.01199 | -45.94677 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 262818a8-dc30-370c-bdb5-4b4ef3413182 | -9.8524 | -47.85015 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| de229ba2-9bb0-3efe-b5e4-c1bf7cecefd9 | -12.1895 | -48.42228 | 2026-10-08 16:18:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 263af0d4-5a6c-3e75-84bd-17b3dde6b9a9 | -8.24277 | -37.19983 | 2026-10-08 16:18:00 | NPP-375 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e611cd43-5d4b-30c2-808d-9f161ca05dca | -11.24198 | -47.73172 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 05bb291a-1b7b-33a2-b08f-aeb7003b5f96 | -11.48193 | -47.73096 | 2026-10-08 16:18:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e6ab602-a4c6-314f-925c-4f4cb188445c | -12.22508 | -43.93249 | 2026-10-08 16:18:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |


[Clique aqui para ver as próximas entradas](README271.md)
