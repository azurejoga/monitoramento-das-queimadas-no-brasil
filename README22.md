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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3890ff3-89d3-3cf9-a24f-ea53562363b4 | -9.85372 | -44.68354 | 2025-08-16 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7642c7d-c371-3c33-84ff-0ce6a0d6e476 | -12.61999 | -46.94365 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 093e63c9-004f-3528-bd9e-a14aa51ff843 | -11.99675 | -44.53799 | 2025-08-16 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d581abc4-a913-34ab-a03f-11c05f804960 | -13.11125 | -46.84878 | 2025-08-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51cb6837-cfba-3df4-896f-db3759a2ae83 | -9.50377 | -37.72179 | 2025-08-16 03:45:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 5f13803f-01fc-3422-b6f2-b16bda8b3537 | -12.5348 | -46.96366 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ba96c435-e603-36a0-a021-9e5373848cfb | -13.58176 | -46.98066 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2d5cf9c-73b4-3f08-a087-0cdcc488edc7 | -12.82254 | -46.02393 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e797f347-7e72-3296-a806-bf18e22f735b | -12.55725 | -46.96777 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 521ee581-9c3f-383d-a81d-baa241270c63 | -13.62359 | -46.91339 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bf5ca14-3b7e-3b26-bde3-fc90e97c8013 | -12.80122 | -45.96634 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c0e0828-9c26-34fd-96c2-20e821cd306b | -14.21376 | -44.77883 | 2025-08-16 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1adf44c-cdee-3184-b9b1-1461ab988c48 | -7.59504 | -45.20778 | 2025-08-16 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de45c340-e490-3a1f-a2c3-f2ceabf7341b | -13.49867 | -43.61212 | 2025-08-16 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 840ae52a-f228-3f91-847a-3c5f47b88690 | -12.57156 | -46.95405 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cff96c02-dfba-3e87-95ff-c15b30bab9eb | -12.23267 | -41.38863 | 2025-08-16 03:45:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8cdf2c61-9bb7-3a2f-a86b-9c66adef07ef | -13.57487 | -46.98515 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13cd92b8-72e5-3dbf-a621-3cd5e831e0a7 | -12.5677 | -46.94411 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d7511f5-790c-3050-994d-97eec3305088 | -12.54201 | -46.95661 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 191d0bea-f12e-3d1a-a47e-d8c9babff257 | -12.60096 | -46.95208 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 796e2ee7-dc61-3f73-b652-53c9ff933580 | -7.36425 | -43.83968 | 2025-08-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 487a1414-1457-3bd7-ae30-f9129322aa5d | -10.17463 | -49.51048 | 2025-08-16 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0085a1b-f1c7-3df1-99ff-1bac5aca6791 | -12.83965 | -46.0479 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aee7d458-498a-3b08-b121-ecd896e841db | -12.55805 | -46.96366 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 0985d290-228c-36eb-9e28-d9f76a369b77 | -13.57005 | -46.98074 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94c204fe-0dc1-3714-b50b-44a03687d039 | -9.8496 | -47.81337 | 2025-08-16 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad2b819b-bb51-3c1c-b9c4-1df4e5dad82c | -11.2616 | -50.48038 | 2025-08-16 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bd997182-32e3-36c0-9296-b1891c9ea32b | -9.85827 | -44.68727 | 2025-08-16 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e443699-bba8-3cb5-83b2-d232779b069b | -12.79658 | -45.96135 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f48925f-fde3-3a10-bae5-34c286f364de | -12.54119 | -46.96073 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9742416d-c428-3813-99a3-d50fbaed83dc | -8.19032 | -42.261 | 2025-08-16 03:45:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7019e5f-1334-357b-9bbf-1f6e9833554f | -7.42121 | -44.87953 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dfd6324-94ff-3098-94a0-5b4a4e3c1ee5 | -12.61043 | -46.9536 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| db81717e-ff73-3817-8781-3a97d193afe0 | -9.27064 | -44.54547 | 2025-08-16 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dd4a2aa-92fc-3968-8636-c79f8abf5342 | -7.14725 | -44.38713 | 2025-08-16 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36ddc5b0-7e7d-3d1d-9fd5-16d452a4cdbc | -13.58521 | -46.96242 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74af57c2-0be2-381a-b36d-4f446a3359d1 | -12.56697 | -46.94787 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b5f3ca08-86b1-34d6-850f-ad54c1b2c019 | -9.16719 | -45.32552 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5687099b-d7df-3955-be0a-90df1df640b5 | -12.59299 | -46.93342 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 04bdf212-215a-3c63-8469-e6e3bd3d213e | -12.82381 | -46.01737 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b24f096-8411-38cf-b381-85382e870359 | -9.20993 | -45.33342 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c0c650a-55ca-3b7a-8047-219b64acf967 | -12.29882 | -50.00893 | 2025-08-16 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 732bbe32-b690-3c8a-9d2b-95f7873fb45e | -12.60011 | -46.92661 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 77491ea4-9ef5-3e1c-9cd2-cac70ab8bb88 | -12.59621 | -46.94668 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 965ba110-7de7-3fde-98e0-b68fc87da813 | -13.4228 | -43.68166 | 2025-08-16 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 04ed2257-f730-32ed-b91d-582fcbf531d0 | -12.83632 | -46.03703 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 612d6050-d369-3495-b7ec-4167cd26f55f | -12.60236 | -45.23681 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6cd56dd-b614-3096-acc5-a6c466c2c278 | -9.85427 | -44.68055 | 2025-08-16 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5376385-f5a7-35c9-b2d9-3a4ebf537e7f | -7.07499 | -44.94063 | 2025-08-16 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d71b2c22-23b5-327b-9695-505234feb6d4 | -11.54825 | -47.27006 | 2025-08-16 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7b14b2b7-adf6-343f-8272-2e2fd079dec0 | -12.82967 | -46.01519 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b55acff4-bae8-326e-b4a6-979227875a55 | -12.68556 | -44.96364 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38daf335-b3c3-3a1f-bb49-ce7448cf8b00 | -12.60484 | -46.95251 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bbaf7ffe-ac04-3310-9382-4b93757f2b6a | -12.55982 | -46.95468 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| da007c3a-2bc8-384a-a422-29d3737ef1cd | -14.0621 | -46.29382 | 2025-08-16 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1b25bab-6401-30e1-9156-56141798b360 | -7.4029 | -44.88924 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0796624f-03f1-31de-8f3e-fe4b650d6665 | -8.94571 | -45.81255 | 2025-08-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca8e5bc6-75c3-30ce-8713-7a41716ed17b | -12.8265 | -46.03153 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc340120-9ded-3c1c-b80c-4abef6ddd6a2 | -12.60708 | -46.91258 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fe76cbc-81fd-3669-9ade-5f8d40a0ea45 | -12.80804 | -45.98676 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd418352-644b-3cf2-890b-7c5bb06ce6be | -9.16781 | -45.32216 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a90638e9-9d33-3542-ba7e-b61870345fbe | -11.41739 | -44.68657 | 2025-08-16 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ee3c9d1d-5726-3f7a-9eab-b1005bf595ae | -12.55569 | -46.97567 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 68245be3-13d9-386c-aa24-345a99027c41 | -9.69754 | -46.26961 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c11e9e9a-56e0-37c7-b2da-c15a53c1d603 | -12.59867 | -46.93402 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 8aa5d747-9962-3f32-8d79-64c35df0aede | -12.58523 | -46.94348 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4f37e72-dd47-3fc7-b0f7-ae9eec5c0518 | -12.48837 | -47.49878 | 2025-08-16 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58d71271-cf18-3ef8-9d9c-4944704bf2e3 | -9.16246 | -45.32124 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bad9dc88-277f-39bc-93d4-4351259e6e55 | -13.87538 | -45.55928 | 2025-08-16 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39dc323f-f474-3f63-a4f9-663157c84aac | -11.93443 | -44.12108 | 2025-08-16 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fa66c49-3964-3271-8db4-cfe782815291 | -12.60504 | -46.96103 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e90ef71e-24b4-3d83-beae-de0f704e13d0 | -8.34403 | -44.94538 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4065aa9b-0fe1-3dcf-9359-c4c79ccbe937 | -9.26307 | -44.55856 | 2025-08-16 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e23aa56-baac-3f97-ac64-dbbb6a9875f8 | -12.84364 | -46.05547 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3243d096-8c16-3f9b-89fc-6b0de0411b81 | -8.1951 | -45.02707 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2ae32e9-8006-3bf0-8a0d-cb3691f1610a | -12.60653 | -46.95332 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 44ff0193-4977-389c-b214-6bd616694b61 | -11.9335 | -44.12619 | 2025-08-16 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2fb222f-29c0-38bc-accf-1f4ce20cacf9 | -12.82694 | -46.00132 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef7e6e0b-ac89-3cae-ad23-6ecdc04f978a | -8.94631 | -45.81312 | 2025-08-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0f62520-7a99-3059-b783-5b3fadf3102a | -12.61465 | -46.93258 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 502a88e9-7f83-32a5-bd78-42d129638fe7 | -12.62082 | -46.93935 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 06dc1676-2fb8-3c54-a115-f4f9e874f1e7 | -12.82235 | -45.99699 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a588d89-8f93-3a5a-aece-fcb0a47a6f61 | -7.24351 | -44.78809 | 2025-08-16 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4455ffe4-bc08-3465-a189-931872f292b9 | -13.64932 | -44.20094 | 2025-08-16 03:45:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a8d86e9c-7115-3467-944c-6b62d3a78eff | -11.57366 | -44.85047 | 2025-08-16 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e33526f-ef18-3f5b-968f-70e439c7569e | -13.58364 | -46.97017 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fd5908e-eaec-3ddb-b4fa-1fdc7d055fa3 | -12.60019 | -46.97563 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c38f354b-001d-37a7-936e-e89035a21a45 | -12.83694 | -46.03379 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| baabbaf8-b1f6-3782-a916-5d666cb79ebb | -9.70159 | -46.26558 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| fe384372-4910-38e5-bc24-535c424565d2 | -14.19822 | -41.01604 | 2025-08-16 03:45:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86d25d3b-7c05-37be-816f-94b456726cdc | -12.82713 | -46.02825 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f07ec21-87e4-33f7-8500-b339f3e1a3dc | -12.58858 | -46.95609 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3834968-77f9-356f-8b61-372b8b13f65e | -13.60583 | -46.91675 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46b973a2-63ba-384d-be65-b2123fc2712e | -12.60147 | -46.91963 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6f4f3c9c-f88e-374b-9511-e12e9ba48ad1 | -8.34342 | -44.94867 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 756f403a-e817-38f3-aafc-e1d24f127fe4 | -8.19388 | -45.03393 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8398b4c8-1d42-31fa-967a-b9f114632772 | -8.34523 | -44.94498 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7c6e472-543f-3a78-9abb-263060d45fe8 | -12.29923 | -50.01651 | 2025-08-16 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2145db97-9344-31c9-844b-a6ea8fb9c565 | -9.70248 | -46.27437 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 14217822-a3cd-3b71-8569-be5bb1a8aec9 | -13.57229 | -46.97067 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README23.md)
