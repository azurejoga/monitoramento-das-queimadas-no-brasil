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
| 981ca143-b64d-37a7-af1c-b9cc2824078d | -6.6993 | -46.3169 | 2025-09-18 01:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d121155b-2664-3b1f-be56-c062b6d2f4c7 | -18.5499 | -46.0606 | 2025-09-18 01:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b82a2dee-1870-3c62-bde8-b04f7ae8c10e | -6.6127 | -45.6066 | 2025-09-18 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| cf8b630e-99a4-3772-90d4-e01762a7542b | -22.3457 | -46.7406 | 2025-09-18 01:20:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| 29441bd6-9cd7-3d45-a933-f23147abfdd8 | -15.8955 | -43.4523 | 2025-09-18 01:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 8bb48085-c0b7-3f2f-873f-2053cafb340a | -10.4084 | -61.2108 | 2025-09-18 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 100af836-e07f-3899-9e39-8d1335cf4a06 | -3.5201 | -52.7588 | 2025-09-18 01:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a9ea6828-60c6-34d9-9f31-3fa8619d68e5 | -18.5303 | -46.0414 | 2025-09-18 01:20:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 3be71d81-6806-3745-87fb-c9cacde13680 | -6.6122 | -45.6517 | 2025-09-18 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 154.1 |
| f020af0f-a463-3e92-bbfc-def67a7ca00f | -6.5937 | -45.6307 | 2025-09-18 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 75aebf7c-9cfa-37df-a98c-7869eabdf361 | -15.8955 | -43.4523 | 2025-09-18 01:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b3a0110d-cfd8-31f3-9f27-a5beeb73725f | -21.5584 | -51.8659 | 2025-09-18 01:30:00 | GOES-19 | PANORAMA | SÃO PAULO | Brasil | 3535408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 74cd743e-a431-307e-aa97-4dc392aec068 | -18.5505 | -46.0369 | 2025-09-18 01:30:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 9371b088-ab21-3a74-b2cb-85a8d8495132 | -6.6124 | -45.6292 | 2025-09-18 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 86e39257-c3b3-3701-9a56-22417ff4a650 | -19.5869 | -57.7765 | 2025-09-18 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 4d097dda-cedc-3367-8d67-5262716f9a9f | -7.3847 | -47.0378 | 2025-09-18 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 99a22ce6-e1a6-3bbe-896a-457d00fc61cc | -18.5303 | -46.0414 | 2025-09-18 01:30:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9b0a81f1-ac3e-3a29-bbd9-47868b21b6e3 | -20.3504 | -47.4294 | 2025-09-18 01:30:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 66ef1f03-9928-3c31-8261-e7c6f3350683 | -22.3449 | -46.7648 | 2025-09-18 01:30:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 18d5e602-cdc2-3d7d-903f-c0881d390a62 | -10.4084 | -61.2108 | 2025-09-18 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f1301782-fe53-3493-b339-7fc7e9589431 | -18.5499 | -46.0606 | 2025-09-18 01:30:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 88096140-8502-3036-95e7-a7841c7ca717 | -3.5202 | -52.7384 | 2025-09-18 01:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| d5baffb7-0d68-3194-a6ba-92bebdbaad66 | -6.5935 | -45.6532 | 2025-09-18 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4607f6cd-dcc6-3d1d-855c-eb7f1bd0ef31 | -10.4085 | -61.1915 | 2025-09-18 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 90900325-5235-3d32-aa91-430615d4d2d5 | -6.6127 | -45.6066 | 2025-09-18 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 90a978e4-4ece-36f3-974b-045542c0bdc9 | -3.5201 | -52.7588 | 2025-09-18 01:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 964744d6-b4dd-3b7b-8c39-b0043eeb398a | -22.3457 | -46.7406 | 2025-09-18 01:30:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| 76ef684b-157d-3481-9b37-d5ef5882f2e7 | -21.579 | -51.8618 | 2025-09-18 01:30:00 | GOES-19 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| 29cf1448-ebe3-3068-89a1-d77273fccd68 | -12.9068 | -44.658 | 2025-09-18 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 3527653e-0324-3c78-a9f9-f1baa89f1de7 | -6.6122 | -45.6517 | 2025-09-18 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 8c2e2161-97b9-30fd-bbf9-ab0c71869579 | -21.579 | -51.8618 | 2025-09-18 01:40:00 | GOES-19 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| 4183054b-0084-3381-b648-e10a8a830e70 | -3.5202 | -52.7384 | 2025-09-18 01:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 7abe05b7-7962-30cd-aefe-d62178e75a9c | -6.6124 | -45.6292 | 2025-09-18 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| da36b767-f998-36f8-a942-c30f8b328f20 | -7.3847 | -47.0378 | 2025-09-18 01:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 79bcd195-e3c5-3ac3-89c7-49ff843c6e38 | -6.558 | -43.597 | 2025-09-18 01:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 12a98b75-7c14-30ab-8458-c4bd05af6a95 | -18.5505 | -46.0369 | 2025-09-18 01:40:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d612a12d-9147-3331-b6a5-c94293e0d382 | -18.5499 | -46.0606 | 2025-09-18 01:40:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| d0511cc0-ae70-3eff-a990-34729ca8800b | -3.5201 | -52.7588 | 2025-09-18 01:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 2a001533-1a1c-35ac-8da9-66be1d302be3 | -6.5937 | -45.6307 | 2025-09-18 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 3da51a15-804b-395b-945c-03b980fea88b | -6.5935 | -45.6532 | 2025-09-18 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c1dfa982-c1f3-3c1f-8ec7-502502363382 | -22.3457 | -46.7406 | 2025-09-18 01:40:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| e04ca992-6d37-3f5a-a7ba-df3b12bf5e7d | -6.6995 | -46.2946 | 2025-09-18 01:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ac1dbf35-8bc5-3ddf-b0a4-0db59a8fdead | -6.2242 | -45.1173 | 2025-09-18 01:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| ffa1e285-45bf-35f3-80ba-597622642a70 | -6.2055 | -45.1187 | 2025-09-18 01:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 263.1 |
| c104bd2b-06f3-3a83-b1ed-141a85bc8798 | -22.3457 | -46.7406 | 2025-09-18 01:50:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.8 |
| 7e9fd2ea-3431-3bfa-87d6-8eda87002d73 | -6.2057 | -45.096 | 2025-09-18 01:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 54e0a706-35c2-3630-a737-231c4c8898bf | -22.9714 | -51.5902 | 2025-09-18 01:50:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 125.5 |
| 9a25da8b-9923-3e15-8ee6-2ec600502edb | -15.8955 | -43.4523 | 2025-09-18 01:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 0a7748c7-1c90-3b66-aed8-00df11c07942 | -3.5202 | -52.7384 | 2025-09-18 01:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 8b11fa90-47ef-3d6b-9676-c59e5549f9e3 | -13.3042 | -61.7887 | 2025-09-18 01:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6e40150f-b78c-3241-92df-cdf84c5ae827 | -6.1868 | -45.1201 | 2025-09-18 01:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ec04790c-7112-3eae-97cf-56c95c0f1731 | -6.6993 | -46.3169 | 2025-09-18 01:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b41b49f5-8a22-359c-a7ef-c81f97f925ad | -7.3847 | -47.0378 | 2025-09-18 01:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 0ff2ca78-edf3-36d7-bdfb-aa6562256a18 | -3.5201 | -52.7588 | 2025-09-18 01:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 8560b7cc-715e-3aec-8854-632383888197 | -6.6808 | -46.2961 | 2025-09-18 02:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0a40252e-add2-3758-b35f-6e20c76e8b25 | -13.3042 | -61.7887 | 2025-09-18 02:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ef1d4f19-6333-3816-b939-185dae6ffbed | -6.2055 | -45.1187 | 2025-09-18 02:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 631170dd-fe8d-3d61-91c7-cc432f1e494d | -9.01 | -46.3039 | 2025-09-18 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 0c9c2b7c-6ad1-3243-b4ce-99cf580e8b13 | -22.7165 | -47.5256 | 2025-09-18 02:00:00 | GOES-19 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| 1d118e1e-d8e6-308b-a5a2-96cc0c74bc72 | -7.3847 | -47.0378 | 2025-09-18 02:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 86d675c0-74cc-314f-8055-983244d314d6 | -22.6954 | -47.5311 | 2025-09-18 02:00:00 | GOES-19 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 334.6 |
| bdf79103-fa25-3a26-85ae-2c15a157d794 | -22.9714 | -51.5902 | 2025-09-18 02:00:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 106.2 |
| a9e4372c-ea9c-3463-a041-2f3c9f59f70f | -22.6962 | -47.5071 | 2025-09-18 02:00:00 | GOES-19 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.5 |
| 19b2439c-b018-3b81-be24-36f5b684c409 | -3.5202 | -52.7384 | 2025-09-18 02:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| d0ea957b-5229-3706-801b-d5c74eedcfaf | -15.8955 | -43.4523 | 2025-09-18 02:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 17f3238c-ee7b-31a6-9238-64bc9109798b | -22.6947 | -47.5551 | 2025-09-18 02:00:00 | GOES-19 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 1e9993bf-a434-3659-95b7-53381a2da947 | -6.6806 | -46.3184 | 2025-09-18 02:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c510f317-b101-30ac-a018-280e2dea66f7 | -20.3504 | -47.4294 | 2025-09-18 02:00:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 97.2 |
| fdfef3ef-a691-3414-b8f6-72a51e172e27 | -3.5201 | -52.7588 | 2025-09-18 02:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 41acd2be-6666-37d8-ab2f-b9551e24c173 | -6.6808 | -46.2961 | 2025-09-18 02:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ebe25da0-58e8-3bd4-aef3-78ba14df5562 | -3.5201 | -52.7588 | 2025-09-18 02:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 1ba60e42-2f08-367a-bad2-a099128cc47b | -10.4084 | -61.2108 | 2025-09-18 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 3482e57a-7597-3aa3-8805-380c1b8475fd | -22.6954 | -47.5311 | 2025-09-18 02:10:00 | GOES-19 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 341.1 |
| 06bc245d-bfc7-35ee-bc22-36a9f9dd4d67 | -22.6962 | -47.5071 | 2025-09-18 02:10:00 | GOES-19 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.1 |
| 632c6043-d8d5-3110-9823-1d2525c89aa2 | -22.6767 | -47.4647 | 2025-09-18 02:10:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9f7f17a5-f856-3cfd-8e32-a002b5a04830 | -22.7165 | -47.5256 | 2025-09-18 02:10:00 | GOES-19 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| 84e8ff24-c242-34f6-ae68-2add6bc10104 | -11.3871 | -50.8465 | 2025-09-18 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| df43bfe2-2584-3100-a735-21750b91cb54 | -10.4085 | -61.1915 | 2025-09-18 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f198c0f4-625f-37ab-86d5-5f51851e5cd8 | -6.6806 | -46.3184 | 2025-09-18 02:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c97ef426-9853-3b24-8d07-519f3667af69 | -22.9714 | -51.5902 | 2025-09-18 02:10:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 120.0 |
| 3e10af80-5889-3881-80e7-4a1817be1b58 | -22.6774 | -47.4407 | 2025-09-18 02:10:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f1e8e230-e6ad-35e5-b89a-6b121e2a3402 | -8.1424 | -44.854 | 2025-09-18 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 64035ded-31cd-37e1-87a8-035c56ad09c8 | -3.5202 | -52.7384 | 2025-09-18 02:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| b5eff5b9-1e8a-3b91-86cf-d1c3dcc4331b | -11.3681 | -50.8486 | 2025-09-18 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| af6ceb9d-9119-391e-a674-e2b0aa7cf181 | -15.8955 | -43.4523 | 2025-09-18 02:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 894a1f86-6fc7-3171-9ffc-03acb7413061 | -22.6947 | -47.5551 | 2025-09-18 02:10:00 | GOES-19 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.9 |
| c7c4927f-0076-3d81-84a3-97b757c1419f | -7.3847 | -47.0378 | 2025-09-18 02:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| fd966cef-df91-346a-8b46-83b07970dfa7 | -21.579 | -51.8618 | 2025-09-18 02:10:00 | GOES-19 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.1 |
| 1b8513da-fa1f-3ccf-8f87-13d6fe3473cd | -11.3868 | -50.8678 | 2025-09-18 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| cda390c4-f57e-3286-9a81-080a6ff3ddaa | -7.3847 | -47.0378 | 2025-09-18 02:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 61cabeb2-acb1-31bf-911b-038c7f2f7a17 | -22.9714 | -51.5902 | 2025-09-18 02:20:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 119.2 |
| 0c7419fd-92e0-399e-b8e6-cc2266df78a3 | -10.4085 | -61.1915 | 2025-09-18 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 23c84709-6bab-39ed-b3b2-401bf194b2ec | -3.5202 | -52.7384 | 2025-09-18 02:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d4f2906e-dbb4-3cfd-83a5-16085bcbed9e | -6.6995 | -46.2946 | 2025-09-18 02:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 7fce1de8-fefc-314f-91f8-b16740f80b05 | -9.01 | -46.3039 | 2025-09-18 02:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 62a11e3d-ea35-324e-baee-c194e5fbae9f | -14.9173 | -51.7087 | 2025-09-18 02:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ea139d3c-6b6e-303b-bb32-1a538d2ec712 | -22.7165 | -47.5256 | 2025-09-18 02:20:00 | GOES-19 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.5 |
| ca13be3e-b437-35d6-bbff-414d8e784794 | -14.8397 | -51.7194 | 2025-09-18 02:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1fc24652-329e-3674-87fd-7d19269a3cb1 | -14.9368 | -51.706 | 2025-09-18 02:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 2b3ce30a-6620-3ef1-9dfa-5660b025ad7d | -11.3871 | -50.8465 | 2025-09-18 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |


[Clique aqui para ver as próximas entradas](README6.md)
