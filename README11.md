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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63bbb341-3c2c-31f8-9358-e4cbf0e34732 | -10.49132 | -53.66738 | 2025-06-08 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b4550a0e-bc7a-3aba-8ca4-dd098b2ca454 | -11.11604 | -54.6424 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b1ac99a-eec3-3a97-b2c1-0630ace82ab2 | -12.36278 | -57.40616 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43c3b5e9-80f2-3803-9bb8-9e4bd156c154 | -11.79742 | -48.08109 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1445b9e6-5c64-3c4d-a0e2-192b64557cc1 | -11.79961 | -48.08871 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 96e10365-bc0d-3878-9592-6a39652f7cd3 | -8.68892 | -47.14159 | 2025-06-08 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ef8247f-5362-3f6d-a7b2-92db437c5d72 | -10.75557 | -48.58092 | 2025-06-08 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba630737-fb32-30b3-aec9-947b841be331 | -9.4125 | -48.45212 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c83c026a-0f60-3956-a6ae-37b3ae060349 | -8.30908 | -55.1022 | 2025-06-08 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f27ac337-4a4a-39b2-8470-576c3ba35c85 | -11.75894 | -44.6535 | 2025-06-08 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 921664a6-d0aa-374c-98e3-4dda156b266a | -12.37509 | -57.40105 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b212980-0f0a-3602-9148-e124c9a46413 | -10.29727 | -57.13937 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37c9f6c7-f03f-39b1-ab3a-1a419b652eb6 | -9.93168 | -47.97614 | 2025-06-08 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ddf0a780-9999-32ed-8427-e98dae35344d | -12.6623 | -58.21695 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a6c450b-4f1a-34ba-8658-6e7f2e69dc9a | -13.06444 | -49.24731 | 2025-06-08 04:25:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e244c90-8350-3db1-b5ea-72ecf2738f7c | -7.81595 | -46.49695 | 2025-06-08 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce33788c-b773-3bbd-9030-f55b37df6a13 | -9.06882 | -47.1454 | 2025-06-08 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5af947e0-7a49-3e04-b44e-3651c961fc90 | -9.41032 | -48.44427 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b54ffc7-b274-36ea-90e4-38452e8324e4 | -12.29128 | -50.09846 | 2025-06-08 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89fa4442-8f10-3eb9-99a3-15a0235cc8cf | -10.4048 | -47.11673 | 2025-06-08 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df44c930-3a3b-3659-a3cf-50406bc0d477 | -11.79629 | -48.08816 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d6ccbb7-3a3b-32fa-abdd-568b26b537cd | -9.40281 | -48.43927 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52eb034a-cdd3-3a8c-b8c4-5e80c2ac8aeb | -11.37224 | -56.55418 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae8d66f6-2bde-302e-a8f6-86cad8dc7f0e | -7.86211 | -47.89841 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d13b9033-6a55-3436-92e3-4229858f33df | -12.97226 | -46.75983 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61b43ed5-cf23-38f1-9e72-86a0dc63b803 | -12.96667 | -46.75169 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94b4319a-2770-3274-b136-284d8085df8a | -9.02562 | -47.60831 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6229c64e-b9d5-39f7-98a2-ef908ec73586 | -11.12441 | -54.64928 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1f3caf9c-a535-3146-8142-9446fc79782b | -7.73704 | -44.17527 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62b9de0d-8b90-3d46-8791-359fbefba331 | -13.54208 | -44.1419 | 2025-06-08 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30cf3c71-f7e8-32d6-b6fa-b7430ff06075 | -12.98526 | -47.11698 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1b27212-9f86-3b5a-bbb4-62d2e7a570e0 | -13.49493 | -47.72221 | 2025-06-08 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fbc67b1-2488-3cb0-b59f-e2ed3bf91624 | -9.07158 | -47.14943 | 2025-06-08 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07c147e7-7278-3543-bc29-05f816e23ce7 | -8.57584 | -48.99465 | 2025-06-08 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aa67da5d-a5c3-305a-8fe8-a8df60318311 | -12.52468 | -58.36316 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5de7aa20-ab09-3a97-a9dc-b165f30de15d | -12.97056 | -46.7486 | 2025-06-08 04:25:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a061f36-e2fb-3209-a96a-88bb57b247bd | -12.96722 | -46.74807 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67428c03-2258-342e-96eb-83afba686a47 | -12.97451 | -46.76748 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c4f76eb-268b-3b1c-b481-3899f6980fca | -10.87577 | -54.30362 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 130f7a85-db3a-3103-89cc-c4e77a93e494 | -7.73823 | -44.16746 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51f91d9c-5580-3151-aa01-efddcdd26437 | -9.07656 | -47.13948 | 2025-06-08 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2683aae6-2e69-32da-a48a-735bd9f1777c | -12.98859 | -47.1175 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b8f6832-5c71-35c4-bcff-8feba56c19e0 | -7.95974 | -46.35925 | 2025-06-08 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c55161b-99c5-3b2f-8cfa-7cf38c6a4686 | -9.01923 | -47.88288 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d1758cd-4af6-32ca-ac1f-9bef9f423043 | -12.20803 | -49.63474 | 2025-06-08 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85e2b872-f186-3c6f-8904-4d30009048ff | -8.52783 | -50.02641 | 2025-06-08 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 97033851-6afe-3749-990f-c254de9ebfed | -11.78554 | -54.77809 | 2025-06-08 04:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7d765c6-9b22-3c13-b442-8ed8ba6805b1 | -13.87833 | -56.20217 | 2025-06-08 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95b2edba-3915-30fd-a32d-1848b2d6ec31 | -21.23167 | -50.83743 | 2025-06-08 04:27:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 559d744f-d8cc-3739-b83a-55a37f6891d9 | -20.47677 | -53.67432 | 2025-06-08 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fae617ec-00b8-34f3-b870-7ba5762ba053 | -17.83633 | -50.81234 | 2025-06-08 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa3d3256-855c-3571-90a7-b1b2f3010de2 | -21.70985 | -48.02628 | 2025-06-08 04:27:00 | NOAA-20 | AMÉRICO BRASILIENSE | SÃO PAULO | Brasil | 3501707 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1baf6e9-9f09-310d-89b4-7c03bb302591 | -14.03738 | -55.13535 | 2025-06-08 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10d0666e-8681-3d47-bccf-17ff4bbb1f49 | -16.26442 | -48.80831 | 2025-06-08 04:27:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4ad9083-aab6-3f26-98f8-8b072c8cb93c | -14.03006 | -55.12407 | 2025-06-08 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e6df929-ed07-3bc4-b7c4-c254bdf38f1a | -14.02826 | -55.13352 | 2025-06-08 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c1c81fd-9d1c-3f26-b36e-866c0c21ee6f | -15.52262 | -42.62054 | 2025-06-08 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6a8f315-1824-3b26-8584-21b5ce716545 | -19.83164 | -47.53598 | 2025-06-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bfd71185-70e9-3678-9b0a-b7d58aab324b | -14.04191 | -55.13638 | 2025-06-08 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8b7414e-3e36-30b5-a642-2994d9a624d0 | -13.87723 | -56.20793 | 2025-06-08 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 039e9c86-ab8f-3fd3-bc40-ce95ac67d41e | -14.8855 | -48.12084 | 2025-06-08 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2834055-f5ef-352b-aa75-9d6cdced3e9e | -17.78127 | -42.80952 | 2025-06-08 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34bc86ef-7ca1-376e-9871-a0ff789b1ada | -15.66556 | -50.83139 | 2025-06-08 04:27:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47457559-fd2c-3793-8cee-31205dbf3872 | -15.63014 | -46.81616 | 2025-06-08 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d496b7e-6729-30b9-8860-ef72b83016ad | -14.26263 | -52.45573 | 2025-06-08 04:27:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec0f2d31-ca89-3af4-a422-0bd67a35c778 | -18.14492 | -47.80013 | 2025-06-08 04:27:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b817b2f5-ab91-38f5-b220-6c09bc57d350 | -13.47114 | -56.85604 | 2025-06-08 04:27:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ebef3d8-c51c-3e31-9266-73ce030455f1 | -13.5037 | -55.65324 | 2025-06-08 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 034880f0-839a-3c2f-88a8-9c629cdbde0c | -14.42984 | -50.64657 | 2025-06-08 04:27:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94905c3e-29de-3fe1-bbf9-4905c4be799f | -14.87451 | -48.10442 | 2025-06-08 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97c8b272-1473-3d09-a968-dab40d3cbca0 | -13.46596 | -56.85513 | 2025-06-08 04:27:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f721689-83a9-3b30-bc3b-d6c84d2c174c | -14.43333 | -50.64719 | 2025-06-08 04:27:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd025c0e-e5d1-3a4b-9553-6982908737e5 | -18.7232 | -54.19355 | 2025-06-08 04:27:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48a17f47-7e10-3a59-ac0e-809698a69351 | -18.72025 | -54.18726 | 2025-06-08 04:27:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fc2c43a-c80a-3320-b194-18b51600b3b6 | -18.72419 | -54.18814 | 2025-06-08 04:27:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a828043e-28ad-3fdb-b661-9892a63d218b | -14.87507 | -48.10087 | 2025-06-08 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52567c6b-ac9c-354c-8731-ccdd88153314 | -18.71925 | -54.19267 | 2025-06-08 04:27:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83dfcdb5-df4f-3b3d-a7c7-abf6037a6be9 | -14.87065 | -48.10742 | 2025-06-08 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 242627f2-589c-3d1e-8b13-e44f1a804848 | -14.03647 | -55.14011 | 2025-06-08 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf841ea2-e083-3507-9bec-d69d8831067e | -19.97066 | -44.21503 | 2025-06-08 04:27:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d4761cab-d781-3002-8d56-f7b00072f9b6 | -16.79667 | -49.07216 | 2025-06-08 04:27:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a364775-5702-3696-851c-fb12f2b8c09f | -18.02209 | -47.38154 | 2025-06-08 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c50bf0b-831a-3d79-828b-b9d1ac2ec078 | -14.03461 | -55.12498 | 2025-06-08 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7537eb9f-0cd4-322e-b205-21bcaff25b72 | -17.80966 | -51.01125 | 2025-06-08 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2df9f911-ae98-33fe-aa0b-1bde71ba9c8b | -19.07809 | -53.46342 | 2025-06-08 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 685e1fb2-1a95-356c-bd36-fb3eced95dfb | -14.87228 | -48.11863 | 2025-06-08 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5580bda5-a65d-3784-ba43-a08baf476d83 | -16.67973 | -43.88257 | 2025-06-08 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55e78e1f-8d70-350d-acb3-680fd9ccb44d | -21.38844 | -48.63645 | 2025-06-08 04:27:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3790d44-b274-3da9-af63-81cd9fcb8831 | -18.23569 | -47.94019 | 2025-06-08 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d5d7700-628d-379d-a516-38249df63864 | -19.12504 | -52.73428 | 2025-06-08 04:27:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c058f667-9bf7-3d4a-b84c-9c2ac5c8a77c | -14.88275 | -48.11674 | 2025-06-08 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71e61fed-9c96-3880-a6fe-ee34e2d9e27d | -22.90135 | -43.7519 | 2025-06-08 04:27:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 25d84961-f5f2-3d93-83b8-2b7a81fb2b1b | -16.65943 | -46.24363 | 2025-06-08 04:27:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe6a320d-708e-35c3-a969-d0b164ad2fca | -14.88494 | -48.12439 | 2025-06-08 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5b03a67-5b1b-3055-9af0-b8048cf00057 | -17.68213 | -52.11132 | 2025-06-08 04:27:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eb2ef51-bcc7-31d5-ac66-c572f0ac4991 | -14.88108 | -48.1274 | 2025-06-08 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92ad07e5-d2f4-3b20-aa9f-408051e97862 | -18.02547 | -47.3821 | 2025-06-08 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62eeddfa-0c5a-3a1f-8029-d65a933029ec | -15.56859 | -47.85628 | 2025-06-08 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9daffe54-b60e-36a9-a592-c060b816d9b3 | -18.3871 | -44.33804 | 2025-06-08 04:27:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0768941-fd10-37dc-a1cc-9be4db129a4d | -13.47017 | -56.85554 | 2025-06-08 04:27:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README12.md)
