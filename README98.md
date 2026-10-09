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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d04d41ea-1839-3610-989b-28f3437cf0a3 | -11.01072 | -45.42009 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23ee9fa2-04cd-3135-85ac-ac1cb82a684b | -11.31233 | -44.82872 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| d07af7a0-9db5-3223-9470-fbb34bb947d2 | -11.84748 | -43.59596 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 227a4f49-d4dd-3c3a-9fa4-0764ea315dc1 | -6.39322 | -55.26902 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c5c716c-3878-3761-ab2c-b18e62f9d9b1 | -13.17614 | -54.31004 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cae9f5f6-ac46-30dc-8dbf-c1ac157c79d9 | -11.78436 | -45.58871 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68429ebb-7e79-364f-9ee7-20896cfc4c75 | -7.8964 | -54.72004 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 204f426f-f976-393e-9712-128cc284c236 | -9.02052 | -44.36924 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e6d224f-c959-35d1-8f2e-100024f8d50f | -8.99628 | -45.90971 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62fdfa2f-eb00-3396-a8e2-66f0b8ff5715 | -8.04153 | -49.40113 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f892bcb-f164-3387-b680-1359150f7a62 | -8.07764 | -45.64433 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2782c18d-672d-3304-a477-b52315943042 | -7.3915 | -45.64313 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ca48dd-5cc9-3b33-b99f-c2015a912b93 | -9.28431 | -47.42945 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be2d24a8-908a-36f4-a0a3-45a96385884c | -9.30799 | -47.45103 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3724ee0-faac-39d6-85ef-805ce20409d4 | -10.9924 | -45.40171 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fa48d80d-f2e6-320f-a66e-bc60f9d70dc7 | -11.12455 | -47.78362 | 2026-10-09 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8594cc8-3e2a-3e85-a266-1ae6b345590e | -6.49113 | -55.96398 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99d11903-e6a8-3a3d-9655-c989897ca01f | -11.2277 | -44.83784 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27b505a2-bfab-3250-94f9-50c863ebc65d | -10.04518 | -48.21624 | 2026-10-09 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 935881c6-dd66-3f7a-96c6-9ec146a96b6f | -6.20229 | -52.86511 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7565e62e-0d4f-3986-bacb-10b302dcee63 | -7.0708 | -47.39548 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66857628-5c02-3474-91c9-0c14adcabcb4 | -13.9999 | -48.75376 | 2026-10-09 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9abebde0-6fcc-3873-ad85-26bf34953368 | -8.91376 | -45.16944 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b3fae92-165f-3fe7-adf9-1537adde76e8 | -8.14734 | -49.442 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfbc0a96-07fa-33c1-9efc-e17bc52c249c | -9.14266 | -45.81537 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 012f5cfc-3936-355e-8b71-facf496c0882 | -8.00517 | -47.18878 | 2026-10-09 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd56cc01-d318-3559-abf0-98f7a42444ea | -7.38216 | -55.21681 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e27eada-3013-32f9-8402-8ba76bb5918b | -10.29423 | -46.60134 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9272dde-b415-3119-ac17-30a12266a6de | -7.38991 | -55.2027 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f624d1b-fda8-356c-be00-bb0486777360 | -13.55462 | -49.15626 | 2026-10-09 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06a40904-4d43-308f-a624-aecd881429e1 | -7.50437 | -54.9958 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d3e1184-1a1b-3ce0-8599-d5940c3f7d50 | -7.18187 | -52.61761 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e5f0d48-2598-3db4-9daf-3ef8bbc7b9f4 | -11.86533 | -43.60563 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41d2f55d-158c-3e5a-9292-486d43cc8617 | -13.18455 | -48.14071 | 2026-10-09 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 533bee4b-25bb-31c1-a8d7-b876b2ca907d | -12.23314 | -57.08652 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 780dc120-168a-30d3-826e-425c1810b6a2 | -12.21061 | -57.09527 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6815ef35-fa42-3126-a259-6b3d05858d57 | -7.47477 | -42.84169 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 14c0a88e-6844-34d7-8385-37a382059fb5 | -8.73415 | -45.14981 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e8204601-1907-3b17-9f0e-a6eeaa1d30b2 | -9.90004 | -44.80923 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81efb888-e567-3de3-9b7b-68670409a4af | -9.91689 | -44.79187 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6420b88a-7455-3da9-9897-e5cef9d02989 | -8.32631 | -49.12246 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bb2c186-9f0b-347d-9dac-80b2537f0302 | -9.22648 | -60.88028 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38ea6cc2-f2ec-3f4f-b2c6-d6b14023fcf2 | -6.48669 | -55.29136 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8f09f51-84cf-3b8f-8e97-a3ef3cd6b63e | -11.25309 | -45.25224 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c71f5bbf-5756-39f7-bbf3-a3105f2031f7 | -7.49008 | -42.81594 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a33acac9-1ac2-3eb0-902d-34a82d20969f | -13.1605 | -54.34622 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0900fe83-bbfc-37c8-b8c1-ceba8b8c7a60 | -11.25382 | -46.30339 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4445c34-fb2e-37af-99b3-387617dd208d | -12.2253 | -57.09872 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 27f45ed9-c428-3aa6-aad2-f5f4433b6089 | -7.31214 | -43.97969 | 2026-10-09 04:27:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8983b9a0-6e34-3889-a7ab-18ae1872d0fd | -11.21679 | -45.25836 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d83e5f2d-0a7d-31b1-bcc8-1c270c9d17a1 | -11.33577 | -46.66011 | 2026-10-09 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c02b567e-c48a-373a-990a-cfa975adc1db | -8.99908 | -45.91375 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32c1233e-03af-3409-8fb3-6c1cddcda2c1 | -5.96021 | -55.3621 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47715034-92e6-3ed2-9c34-d54c78db2d5a | -7.75941 | -54.95416 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afff37fa-332c-3836-a203-d1af5285f95a | -6.25733 | -52.86086 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6abb80f-3b44-310d-bf11-5a6982aa122c | -8.49941 | -54.62035 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5be8e43b-f60a-3635-8adf-23e5886a848d | -9.01871 | -44.3812 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6751417a-a756-3e13-a7ac-0104510b94d5 | -6.45099 | -52.70356 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbc5af7a-b363-3a23-87b0-dde2f3e5d1d7 | -11.6507 | -43.67546 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7517827-f2f4-3c2e-bf33-f9dc69094430 | -10.87042 | -45.53789 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6874e904-d1ee-3c03-b023-49ac24566b79 | -9.88087 | -50.51939 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4719ba01-cfdb-3731-a626-1c7f4971a3f5 | -7.51199 | -46.09623 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5e7d674-35f2-3cf5-b0a0-f27c7cf60cad | -12.22395 | -57.11164 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f9fbfcfc-138b-3fdc-a4c8-ce6e7776495d | -10.32412 | -46.606 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90f4ab27-fe8b-3703-af91-2053e306a989 | -11.33299 | -46.65604 | 2026-10-09 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91ceabf7-bec9-334d-8634-31089fcc7160 | -7.06803 | -47.39148 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7fbe509-c5e5-332d-9b18-ac8b42cbafac | -7.27565 | -46.17292 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a44d4a9-b0f1-30ea-b7e4-4f05b4fd386b | -7.57244 | -45.19604 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8dc90ee-e144-3321-9c10-23d5d25d06e0 | -11.21332 | -45.25787 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de0515a2-019d-3f6a-885f-12285eac3f4b | -7.89733 | -54.71461 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7991420a-701b-3182-9360-f7286c55e3a9 | -6.12326 | -55.69498 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0394ae31-9363-3295-b8f2-aa3cdd741c23 | -5.96936 | -55.34067 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a084ff33-bd67-3987-8490-40e6f86eafb6 | -6.13088 | -53.50821 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5161a71c-5072-3a9d-bc71-102397625eb6 | -13.81822 | -39.9049 | 2026-10-09 04:27:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2d27a844-e0b2-3394-9051-e179ae877282 | -13.1708 | -48.14209 | 2026-10-09 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ab544b0-98be-3600-8480-94cc8f4657d8 | -13.50213 | -44.37014 | 2026-10-09 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0f2e20b7-90d6-3776-b1df-7d6e367fe47f | -7.37971 | -46.22526 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55e9e7a1-c92e-3835-b320-1f48ce232ccc | -8.32975 | -49.12301 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba91a2bb-4085-3d1b-a171-395a06c89b16 | -6.15489 | -53.3126 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa7b1b6b-2b08-3d89-895f-02121dae6255 | -11.78022 | -45.54494 | 2026-10-09 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d7d5e29-4ee8-33d7-a90e-53aee422ea7f | -11.77798 | -45.5603 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6137796f-0da9-32a5-9ced-ca120013d7e3 | -7.32598 | -45.29471 | 2026-10-09 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 431d0ff8-390f-30f1-8aac-45f0270b7b40 | -11.46228 | -54.29987 | 2026-10-09 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfa889cb-7170-3ceb-8acb-382d0765f892 | -5.95142 | -55.35061 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d69c8db-a403-3507-989c-306b1c4e17a8 | -12.22928 | -57.10638 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dbfc2a2e-30b9-372f-b819-7993bc0f7b43 | -7.75385 | -49.20479 | 2026-10-09 04:27:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87a442d8-0543-3015-9025-889fb0bbc03f | -11.2826 | -45.19711 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 194d4427-86a2-3805-be1d-8f23b5156498 | -6.49535 | -55.30266 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b1e10bf-f246-3958-9be1-1d7465501d1f | -13.21009 | -54.36853 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 555bd159-ff00-328b-99a3-a0bf89ebde53 | -6.1085 | -53.50502 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a296547-25c4-32a5-82ba-45f456c3793c | -11.83042 | -43.52582 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fe1aada-293b-3f21-997a-8d993686ab00 | -13.81589 | -44.19325 | 2026-10-09 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da0a6b3d-5bff-32fa-ab87-cefc3ce94e74 | -8.43515 | -47.03021 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a65059e-8c3a-3ec8-a79b-8381bd6439a5 | -8.06288 | -45.63429 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0369a7e4-1d05-33f4-8504-0dcb11fd9889 | -8.74493 | -45.14763 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f7e643d-29fc-30f7-9fc7-88c894b0b342 | -7.68879 | -45.43056 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a3ec0b62-002f-3881-9393-7d2a1dde1c55 | -11.75876 | -45.47992 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be809d42-5483-373f-9949-fce988324b49 | -10.88618 | -44.79785 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ecd53f3-fc03-363f-87b8-346eec08f6f9 | -9.27225 | -45.63195 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 370b85ce-0558-3758-abad-6a5c28a51491 | -7.65676 | -45.37827 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README99.md)
