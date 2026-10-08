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

## Dados Diários - Página 220

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb9d614a-9717-32e3-8a16-c3270a26cb79 | -6.9535 | -45.2619 | 2026-10-08 15:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| fb1e4f36-098f-300b-b5d5-76f924cf88f6 | -8.1876 | -54.7219 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 6e39780a-4fd7-3cbc-932a-0014a230fc6b | -3.2761 | -54.0011 | 2026-10-08 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 8bc51103-6e53-3218-afe0-159a2f863413 | -3.0926 | -53.9254 | 2026-10-08 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| dc71dc85-31ed-37fd-b8f2-8a8a0389bcf0 | -11.6382 | -43.6166 | 2026-10-08 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 57072c0a-ee08-3f3d-a628-906af04cd067 | -10.4334 | -47.3046 | 2026-10-08 15:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| f3dd4786-e137-3caa-bc78-42eac3207ed8 | -2.0947 | -56.6239 | 2026-10-08 15:00:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7918fce7-fe46-375f-b341-10d6058d87fe | -12.1545 | -44.7547 | 2026-10-08 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| dbb34564-56af-3baa-ba04-af8c98bf5fb7 | 1.6568 | -55.8045 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 1ea2111b-ebbe-3237-9a6c-833c4d90ab8a | 1.7671 | -55.5661 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a2e49c0a-9439-33bb-a5c4-d0992c80695f | -1.8803 | -53.9701 | 2026-10-08 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 2fa12313-ad80-32b1-bf30-d263ab2feb49 | -7.8876 | -55.0023 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d6f2742b-d807-3e77-add6-a73a839a6f77 | -14.6701 | -51.4643 | 2026-10-08 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 694b09d9-a358-354b-a68c-fa2a16a36349 | -12.1922 | -44.7953 | 2026-10-08 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 201.3 |
| a11030b5-41f1-32f5-97eb-42b005e35eb2 | -6.7366 | -55.1274 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 75a9c2f3-cd7a-31a9-9a3e-5e95784bc69c | -6.2355 | -52.6841 | 2026-10-08 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 66f89c90-3202-30ea-9f35-64d61699f0a3 | -7.1998 | -55.1226 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 577f0a46-b559-3b9f-a1f5-51d698539789 | -7.2177 | -55.2017 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| cc950efa-d9e8-3bf3-ad75-09c0db0231d6 | -10.9575 | -45.389 | 2026-10-08 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 5f4ddbb3-308f-3a2a-b902-bf961d51be47 | -5.7321 | -41.6349 | 2026-10-08 15:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 174.1 |
| a0cc98f6-b78c-3068-ad7e-79cb37b4b3d3 | -11.4503 | -43.4091 | 2026-10-08 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| d2c8e3e8-7b3c-3972-bf66-d88f6e7cde93 | -7.1825 | -52.6283 | 2026-10-08 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9e39e1b1-b479-391b-a55d-aa0e8f29c298 | -8.8899 | -45.3907 | 2026-10-08 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 2efac590-e5e4-39fb-886c-8cf14ce8553f | -7.0706 | -52.6764 | 2026-10-08 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 844bda12-f513-387a-a537-eac3e591071f | -1.3277 | -55.4327 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 217.7 |
| 1baf581b-28ce-3443-bc17-4358a8dcca55 | -3.0741 | -53.946 | 2026-10-08 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 196.2 |
| 0246162f-a0cd-333a-a653-b338e7c90f67 | -1.1094 | -54.1601 | 2026-10-08 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 1f38fddc-ad15-3120-b09e-c207e6c07786 | -6.1952 | -53.1362 | 2026-10-08 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f12a534a-fe82-346f-b2c5-3280858f6476 | -8.5313 | -46.911 | 2026-10-08 15:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 4830b14e-1742-30b0-83d9-5c75d83e0b03 | 3.5448 | -51.2772 | 2026-10-08 15:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e584bf8b-84b6-3e64-8ec0-c8b901924eb4 | -6.3836 | -52.7169 | 2026-10-08 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 613f471c-69d1-3766-88ae-4c6e2d181c90 | -9.4819 | -66.7836 | 2026-10-08 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 2df306f9-b333-3c80-ab59-2393260f8bb2 | -1.4569 | -54.7562 | 2026-10-08 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 961b8a7d-5caf-393f-97a1-c00cffeda24b | -9.4492 | -44.6167 | 2026-10-08 15:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 5555f04a-7b61-37b3-9562-ffd5b9c6297b | -7.2 | -55.1026 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e3352d79-1550-3b53-9f58-857bdd891f75 | -10.4527 | -47.2801 | 2026-10-08 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 9fdd985f-8cca-3b39-929d-7e6625f4af66 | -12.1967 | -57.1103 | 2026-10-08 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 74116d93-0498-3ec4-a16f-47ad220562af | -1.494 | -54.5363 | 2026-10-08 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 6e38b578-2c5e-3339-8853-77d2fb60fca7 | -2.4988 | -56.1266 | 2026-10-08 15:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 9c0e315a-7b3b-3f0e-b442-7fef5c085ea9 | -6.7503 | -50.9543 | 2026-10-08 15:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9582265b-593f-31a5-9da4-10e2fc96431e | -8.6107 | -67.0116 | 2026-10-08 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 7580cbf5-8d52-3b21-adb0-fb1a94584022 | -10.9953 | -45.4068 | 2026-10-08 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e2279c27-e814-3cb0-8a2b-b4409ca3b35e | -11.8595 | -47.3694 | 2026-10-08 15:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 1f7f998b-dc96-3f56-943e-2bfab75e9e96 | -7.2184 | -55.1216 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 11a064e4-681b-3716-bce5-1ce595fa74ca | -3.2945 | -54.0006 | 2026-10-08 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 30b52c96-914e-3d40-bbcc-d4b96d80ff2d | -11.6374 | -43.664 | 2026-10-08 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 4ff54f90-aac5-339f-aa37-2b6c5d4873a3 | -6.1951 | -53.1566 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 3d4e6158-28fe-308e-8fac-9d8a612dcf6a | -3.1633 | -54.7253 | 2026-10-08 15:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| cfd5bfb4-e7c0-3298-8865-75fe02188cd0 | -3.0926 | -53.9254 | 2026-10-08 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f3770429-7a2e-379a-80fe-8ab26bb0bcfa | -12.1948 | -44.6554 | 2026-10-08 15:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 28eb4daa-6c5c-385a-9b28-a7be22ee82ff | -8.2433 | -54.7384 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 2416d25e-8f93-34aa-8294-6b4edb56530f | -1.4569 | -54.7761 | 2026-10-08 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 4d33a24e-84e9-3cdb-92af-5e17c5123037 | -3.5685 | -54.4746 | 2026-10-08 15:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 1da898b6-076f-3191-acba-a910afc149a0 | -2.3115 | -57.9829 | 2026-10-08 15:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 213.3 |
| 32923059-9b37-3fa1-9759-ae13ec830c10 | -11.3986 | -47.5635 | 2026-10-08 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 0c76fe15-1f78-31de-8972-768b2e07d21d | -14.3611 | -55.0114 | 2026-10-08 15:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 0a4c640d-6c7c-3d43-bc9d-ca15e50f5cc5 | 1.6568 | -55.8242 | 2026-10-08 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b3b83bc3-7d7f-3fc2-a32e-67078b87fa37 | -2.3298 | -57.9827 | 2026-10-08 15:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5b5f7ea4-5e2e-34a5-94ed-504b9d96920b | -6.1617 | -52.6471 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 308.7 |
| 37956138-63de-3c30-81c2-0d052ae60703 | -10.9953 | -45.4068 | 2026-10-08 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 80a25f11-14cc-36d4-bd6d-5e3dc163c9c5 | -13.1641 | -54.3178 | 2026-10-08 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 202.5 |
| db52960b-9b52-343a-b1c5-6a8545f5194c | -1.5301 | -54.835 | 2026-10-08 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 6847b115-8c5c-3bec-8b47-bf5471f45c63 | -12.2316 | -44.7427 | 2026-10-08 15:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 377.4 |
| a18ccc09-5fbf-3a7d-8d8a-1fb454d6bb5d | 3.5448 | -51.2772 | 2026-10-08 15:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 76.4 |
| df156f68-5692-3416-a07b-4c840e56465c | -2.2198 | -58.1196 | 2026-10-08 15:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 69186124-9df2-3aef-8cb2-20bc0e113b1c | -9.4492 | -44.6167 | 2026-10-08 15:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 1c5e5c39-4d83-3f0a-b9e5-2aa582d8a32f | -7.0706 | -52.6764 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 98564d28-6433-3e36-ab6d-7c2d5e50dc68 | -10.9575 | -45.389 | 2026-10-08 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 487c693f-6962-3257-abcf-d1ac2e927e7c | -2.2198 | -58.1003 | 2026-10-08 15:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5c6902ca-7cc5-348d-9753-bc6347f85848 | -12.1922 | -44.7953 | 2026-10-08 15:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 3d9f75e1-5105-32db-9114-77c9096e3569 | -14.3801 | -55.0298 | 2026-10-08 15:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 253e5b92-38ae-3652-8945-50ba88cceebc | -2.6079 | -56.4782 | 2026-10-08 15:10:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 68af20ef-2bb6-3ac2-916d-610198bb74a1 | -3.0447 | -57.4851 | 2026-10-08 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 1dc1d9a7-73f5-3fa3-8662-071be2750806 | -2.204 | -56.9155 | 2026-10-08 15:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 01ba63da-3a1f-3b3b-a7af-20ed3d4ea920 | -2.8347 | -54.1125 | 2026-10-08 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f741af19-2dbd-3624-bbb4-f225e6cb7512 | -12.4644 | -62.5173 | 2026-10-08 15:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d7ee91ca-8cbb-3522-a34d-b0847e0801bb | -10.6912 | -47.8278 | 2026-10-08 15:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9af40517-dab5-38a4-8833-612e2647a1aa | -7.47 | -42.8078 | 2026-10-08 15:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 130.1 |
| 27cb9836-aba7-3d47-927f-bb69d42eb155 | -2.9447 | -54.1702 | 2026-10-08 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 2eb2d134-c6f4-3d5a-8a8b-77a6a89149fb | -3.8786 | -44.1265 | 2026-10-08 15:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| aff5b335-a75c-374b-bb4e-1088347896b0 | -1.3277 | -55.4327 | 2026-10-08 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 642b7b2e-20a2-3236-9993-62e7d60bc775 | -1.5118 | -54.8153 | 2026-10-08 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 5aa7f708-b0d7-3e0c-957e-5737b6615f02 | -11.7738 | -43.5482 | 2026-10-08 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 28fe503f-e6fa-3be5-94df-9a4e67e54a2a | -1.5302 | -54.8151 | 2026-10-08 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 842981f8-afe4-3e16-a166-63b85b205254 | -2.572 | -56.1646 | 2026-10-08 15:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 3d55023d-8209-3e33-9f86-4645de1029d9 | -13.69 | -49.085 | 2026-10-08 15:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ec0bc0bf-e1d3-3766-b924-2d7d758426bd | -0.34 | -52.0359 | 2026-10-08 15:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5a9bca8f-9e2b-30e8-9776-40b50abc7518 | -3.0186 | -54.0479 | 2026-10-08 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 337.6 |
| fbb57c74-54f8-38d3-91bf-2878c0379cb9 | -6.2127 | -53.2779 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 47623311-823c-3314-9845-b768589b4524 | -11.4503 | -43.4091 | 2026-10-08 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.6 |
| e671abe2-8b77-3b5d-a21b-1d5662d6cb02 | -7.7579 | -54.9499 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b6e16b6b-106d-3c7d-8174-f3b352e8fedb | -3.1816 | -54.7448 | 2026-10-08 15:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 68608a5c-33be-3886-82aa-7eb60784265d | -1.4569 | -54.7562 | 2026-10-08 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 4a4ad811-d64c-3c8c-83e0-29c3ca8b9858 | -13.6896 | -49.107 | 2026-10-08 15:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 56194451-5401-33fd-8ff6-99cbc59f2924 | -2.8247 | -57.606 | 2026-10-08 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4c466aa7-155a-3b41-b659-ca30a6f79a6e | -13.1639 | -54.3385 | 2026-10-08 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 232.0 |
| 6ee0ea67-4965-34b4-985e-55c8771e2e75 | -1.4573 | -54.5367 | 2026-10-08 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9347506b-6f9a-3703-b288-6239f99ce10b | -12.232 | -44.7194 | 2026-10-08 15:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 210.3 |
| d3e6b971-73f9-309e-8910-ee0233ad279e | -6.2529 | -52.847 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 7422471b-2d77-3a9c-a574-5e177d55a974 | -8.9501 | -45.1334 | 2026-10-08 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 577.4 |


[Clique aqui para ver as próximas entradas](README221.md)
