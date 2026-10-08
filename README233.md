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

## Dados Diários - Página 233

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33039934-8d8d-3a23-976d-37b2be7b0836 | -13.74329 | -41.10723 | 2026-10-08 15:39:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 2f013f10-008b-3f5a-ad13-4f7d9241c508 | -15.52492 | -39.31388 | 2026-10-08 15:39:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| b8df925e-8ea6-3213-9921-a8d557830586 | -12.18454 | -44.82623 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 88e6cb02-5ad3-3aaf-8082-4e9e704ae729 | -14.02514 | -39.0308 | 2026-10-08 15:39:00 | NOAA-21 | CAMAMU | BAHIA | Brasil | 2905800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b1d87b4e-bbc0-3f70-bab2-d6534b79f521 | 1.7672 | -55.5463 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ee0c848b-2ac8-3413-b3bf-76255a57dedf | 1.5283 | -56.003 | 2026-10-08 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| fc985db5-abb0-3c47-8e88-ffe1a4e435dc | -3.426 | -58.5999 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8a1d3837-3bb1-357a-b2c7-340f89f1ee99 | -9.077 | -66.0881 | 2026-10-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 56b9a658-dcba-3f87-994e-22a3924020cc | -7.1998 | -55.1226 | 2026-10-08 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 358f5b81-df46-36f7-b4d3-fd3c09bed164 | -2.3115 | -57.9829 | 2026-10-08 15:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 176.6 |
| b31e03d4-26c8-31fb-a444-af84359376d8 | 1.7304 | -55.5863 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 36945cec-ef54-3c1f-a4af-93ba4eda8d7e | 2.0047 | -55.8786 | 2026-10-08 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| d5cd8629-ce34-363a-9580-ecd565423ce4 | -3.0448 | -57.4657 | 2026-10-08 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 130d449e-9258-3753-b697-6e43e0956a83 | -1.3264 | -56.4176 | 2026-10-08 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| aaeeaf49-c656-354c-9c87-fc12bbfbfbe7 | -2.6052 | -57.5711 | 2026-10-08 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 73ee54a8-4562-34ea-b726-0d2c597fd147 | -3.7718 | -59.246 | 2026-10-08 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| dd3e1a77-50a1-3a51-b7c8-b8ae17dd870b | -2.7332 | -57.6077 | 2026-10-08 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 3958f4b0-3721-3b3d-9466-245357c023ee | -2.8897 | -54.1514 | 2026-10-08 15:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 46f1a18f-63b3-3f3c-8b7e-d7c1cf3400d0 | -6.6899 | -45.3746 | 2026-10-08 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 6840c5b2-b66c-3d0e-a58a-2a0980f03511 | -3.0982 | -58.0273 | 2026-10-08 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 37b8b54f-db4b-3409-a030-f2eb42897231 | -2.4942 | -58.0768 | 2026-10-08 15:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 1111fdbb-1b98-3c2e-99dd-92218e8524f9 | -1.3264 | -56.398 | 2026-10-08 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 47a50f2f-2f4a-3080-94c5-8302a15ed3a5 | 1.6937 | -55.6263 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 63c93399-e24f-3624-b4c0-6e2c7c2fdf35 | -7.2 | -55.1026 | 2026-10-08 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| ff8e3208-4b45-3c30-9748-b18efea69e88 | -11.2295 | -46.2403 | 2026-10-08 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 305.6 |
| a80ade65-b38e-34e4-a922-052bba07ebfc | -12.1738 | -44.7517 | 2026-10-08 15:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 07147456-0450-3e1e-b8c0-d3115cf23518 | 1.7121 | -55.6063 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 90ce505d-9752-3b80-a2ad-7a223c96beba | 3.5448 | -51.2772 | 2026-10-08 15:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 89.3 |
| d0a2bda4-76fa-39a4-915e-3bda15701058 | -3.1633 | -54.7253 | 2026-10-08 15:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7e3f2f2a-8a88-3266-a7dc-9d3ed5d911ef | -9.1407 | -64.4024 | 2026-10-08 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 58adad3c-48c9-3067-a66f-70214e572f5e | 1.6568 | -55.8242 | 2026-10-08 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 684a316c-3fe8-3d04-b5f8-f95c6f766878 | -3.0447 | -57.4851 | 2026-10-08 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| db6e5b87-eeea-3b15-a8b2-11dafdcb3cf7 | -2.4806 | -56.0875 | 2026-10-08 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 083a1f21-7451-392e-aacc-28ac8424d6af | -1.3277 | -55.4327 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| fcf09185-8143-3c50-95b4-b827bcaf5db8 | -1.383 | -55.1944 | 2026-10-08 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 632a6619-dda1-3cbb-8612-8c73853a51c6 | -8.5921 | -67.0491 | 2026-10-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 06917aeb-7ac7-308c-a659-90a28fa17200 | -3.9729 | -59.3373 | 2026-10-08 15:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 3b780cae-b7d8-3834-b156-113337d1087e | -2.4804 | -56.1466 | 2026-10-08 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| ab7396d4-239a-3d9c-9fa6-d9f2d9c250e7 | -2.8434 | -57.4696 | 2026-10-08 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 95aad328-e1c8-3299-ab39-2809c5982c81 | -8.9501 | -45.1334 | 2026-10-08 15:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 220.2 |
| a18e7fed-3db5-3654-8270-844ea0c660f6 | -2.4428 | -56.5399 | 2026-10-08 15:40:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 321b2b0a-8834-3959-874d-adda75eca249 | -1.4301 | -49.0382 | 2026-10-08 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5a5c272b-e578-3fa3-aaa9-3317f197fede | -3.8155 | -57.1751 | 2026-10-08 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4bcff098-a06f-3d8d-95a0-90189be23aab | -2.853 | -54.1322 | 2026-10-08 15:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 1ad08a9d-8fde-3da3-93e4-41f58b5d6dc3 | -2.8938 | -59.206 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 782cec23-0964-3af9-a5c2-4ec110eb2a30 | -12.1922 | -44.7953 | 2026-10-08 15:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 328.5 |
| 9f9380c8-4eb2-3088-857d-af63b23ab65e | -1.1345 | -49.1911 | 2026-10-08 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| cdc36120-4cbf-3dc4-8e3e-17485912522a | 1.6385 | -55.785 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4e29b1e7-d38e-3e60-a2ca-76840b79e699 | 1.6385 | -55.8047 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 04b4eb95-7cab-3dfe-95dd-dc28a9d2e9ee | -3.1697 | -58.6437 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 369.3 |
| 2bcc8a62-a815-32bc-8190-1ab4c4faa561 | -3.188 | -58.6241 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 2ba0891c-4688-3410-953e-72f11b068dad | -9.4819 | -66.765 | 2026-10-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a4792844-aa1c-39ab-af66-43b676172d7d | -3.4095 | -58.0013 | 2026-10-08 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| e82aaa53-3eef-3ba4-ab50-029bd04e237c | -8.5922 | -67.0306 | 2026-10-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 549819be-862e-3dcf-98f0-2c4af54f24e0 | 1.6568 | -55.8045 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| b386b722-a788-3a01-8e89-c508a44c036e | 1.6937 | -55.6461 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3c68e129-3c29-3ae0-bce0-d681a55321f7 | -2.0447 | -54.3085 | 2026-10-08 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 88bfb9c6-a09d-3901-8e16-4ac1afa98555 | -3.0992 | -57.6589 | 2026-10-08 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d9eba7c7-a188-3928-821f-856243311d65 | -3.1697 | -58.6244 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 213.4 |
| bfd86804-0560-35b3-84a4-0cdc47e16a81 | -2.9819 | -54.0488 | 2026-10-08 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 1f7660c8-daba-37f2-9618-982687553d33 | -6.8574 | -59.36 | 2026-10-08 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0f3344e9-993e-306c-982d-12ddb7eb7b32 | -3.4096 | -57.982 | 2026-10-08 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| fc550fd7-c1ec-331f-9dcf-ec4ffa1cac89 | 1.5833 | -55.9827 | 2026-10-08 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ad473f66-5b85-3b43-b8fb-1366fc4befc9 | -3.3503 | -59.4848 | 2026-10-08 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 8afcf098-9f19-375d-8b46-5eec5f4c48a2 | 1.5466 | -56.0028 | 2026-10-08 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3f264112-918d-3601-a905-525ec9176c25 | -12.1742 | -44.7284 | 2026-10-08 15:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| cd5c7b7a-6273-30bf-bdbf-cfcd911bb0cc | -8.6106 | -67.0486 | 2026-10-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 388.5 |
| f5e1feb1-8724-3e51-99eb-9bad20324e2d | -2.8938 | -59.2251 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 510d948f-3bca-3b9c-b6b8-d40031e2917b | 1.7488 | -55.5861 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| edd981d2-5ef7-3b4e-aff2-dfa4bece47d5 | -2.7979 | -54.1134 | 2026-10-08 15:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 86c8ec16-2622-34f8-b3de-0b547ff1d2e1 | -3.3358 | -58.1578 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8421d82f-85f5-3a8a-bd06-de4957edd6a9 | -9.1408 | -64.3836 | 2026-10-08 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3b319c60-a0be-387c-8278-ed901d804542 | -3.1879 | -58.6433 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 391.1 |
| 1513d0fb-8588-37a6-bd96-77e16f1c9a35 | 1.5832 | -56.0024 | 2026-10-08 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4d286492-3720-3016-ab49-2925372b5e66 | -2.8347 | -54.1125 | 2026-10-08 15:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 0d76ddfa-30ad-3038-9b96-3c92849f1d28 | -3.095 | -59.1832 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 1c48622b-e214-37c1-a814-abfb082f528e | -2.788 | -57.6261 | 2026-10-08 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 97eb0e8f-f83b-3fd4-a154-975b0f732458 | 2.7641 | -60.0106 | 2026-10-08 15:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 140.5 |
| cf2366bc-ecb4-3a38-8ce2-b760cdc211d6 | -3.3172 | -58.2355 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ef53c606-bd62-368a-a8f3-c5f14e4ccc6f | -9.519 | -66.7639 | 2026-10-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 328bab30-a84c-3bfa-921f-9ac48148fa2e | -9.5003 | -66.8017 | 2026-10-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 218.7 |
| 5b40e817-fbc3-3e27-8b0c-4b70ca642a88 | -1.5307 | -54.5159 | 2026-10-08 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 7265026b-c53c-3a54-8d7c-5647bff7d4cf | -1.6396 | -55.1319 | 2026-10-08 15:40:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 739a4e50-7671-3a94-ab9d-d823cb538257 | -3.0799 | -58.0083 | 2026-10-08 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| fcf6d000-84f3-3adc-ba67-29f0ccc7dd8b | -1.3277 | -55.4525 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a10b6e42-3ea0-3615-8106-c15d5398d443 | -3.8566 | -55.9967 | 2026-10-08 15:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f4a32d63-d266-349a-b2d1-6684d7fef8cc | -3.0559 | -53.9062 | 2026-10-08 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c6baad6d-4449-38f0-b066-55188b16a785 | -2.4805 | -56.1072 | 2026-10-08 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 016dc5e4-350c-3362-ad74-0f856734338b | -3.3912 | -58.0017 | 2026-10-08 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ac4a5167-1700-3cdc-8351-981c59e8cc73 | -6.6901 | -45.3519 | 2026-10-08 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 88c19f1a-6bcb-37b8-b92e-d9f8174a9c2c | -9.4819 | -66.7836 | 2026-10-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 141.7 |
| b64e3d94-ddfa-3049-87ad-d2544364cd2b | -3.2268 | -57.8696 | 2026-10-08 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 5d25f2ff-6730-3491-adb6-5908ed805e8b | -3.8567 | -55.9769 | 2026-10-08 15:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c4f4c5f1-4150-3f6a-bb88-6b6058078157 | -2.6079 | -56.4782 | 2026-10-08 15:40:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 0e8923b2-05a5-3191-81c3-8ed1d4ce1e4b | 1.5649 | -56.0026 | 2026-10-08 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cd0cec18-4142-3e5e-9d7c-0f6947f1d7dc | -9.479 | -67.4897 | 2026-10-08 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| fc383b48-7bf2-33b7-b2a6-44146ed35de3 | 1.7304 | -55.6061 | 2026-10-08 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b2889f23-087d-3057-baa5-fba425ce8249 | -2.572 | -56.1842 | 2026-10-08 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 111e6375-b4a5-3d12-922a-7d0881d7ec17 | -3.3355 | -58.2351 | 2026-10-08 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 738143da-fffc-38e4-b582-58241346e25c | -2.9082 | -54.1108 | 2026-10-08 15:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |


[Clique aqui para ver as próximas entradas](README234.md)
