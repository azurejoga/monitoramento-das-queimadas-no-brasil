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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bcc076b-d488-3f2a-a47d-851ae2865b51 | -9.03679 | -47.1106 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d0b2b4a6-e67c-3708-8c38-5fd06b8f9b2e | -9.03293 | -47.09213 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7868b553-66ff-39c1-a6a5-3f0ebc01b1a6 | -10.39274 | -50.4957 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bcfdc09-33a4-33bd-b3a4-1161b6915655 | -9.68408 | -47.54811 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f196fcd5-414a-3c30-af7b-8ae31d9734a3 | -11.66876 | -46.58443 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 443cd79c-1cfb-3ade-a994-27b4e30bb8d9 | -11.07846 | -48.41078 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e59fc39-4a19-3a06-961b-f781d728c8a9 | -11.5325 | -50.40274 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8bf6cab2-559d-3a6e-872f-b550f360a7c9 | -11.85983 | -46.75318 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14b033fe-6104-3e82-8c89-18adc29e12f5 | -5.82936 | -39.65278 | 2025-09-12 04:25:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d4265d3c-0c99-3879-b544-f906a107f46f | -9.16194 | -45.56382 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 633f11a6-e556-379f-8360-21ed5af6ede5 | -10.68949 | -48.64982 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7f67c22-1f86-3d30-90a4-5c22278f4575 | -7.73499 | -43.90032 | 2025-09-12 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8777e5d-a57b-30f2-9aea-5042d1c42829 | -10.67425 | -48.65846 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4e50217-cd58-3cdf-a858-00e7a997bd5d | -7.83534 | -44.89308 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3c6784f-e6f4-3b0a-b543-5caa79206f68 | -10.74476 | -48.17974 | 2025-09-12 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 272229ef-e594-3e21-a238-70369ec182a9 | -9.00789 | -46.1262 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af25a950-4b93-31ce-99e1-1534d82e0237 | -8.1908 | -46.09855 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 862223de-a142-3fd8-b57a-840ad2b5aa5e | -10.77927 | -45.99428 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4b31cc4-8920-3b12-bf81-4a2f01ddfdea | -9.05445 | -47.04198 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 872824ec-6e2f-3ec9-ad48-6cdaea23becb | -11.67981 | -46.53509 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebcc3fe0-0643-35d2-8aeb-98e973451394 | -11.66546 | -46.60579 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d770da44-8a4f-3783-9b1b-6e81e66a9fb8 | -11.42348 | -43.54207 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f4aa22c2-983f-315a-a996-1b86414ed20c | -12.10132 | -44.87302 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 707ee6bd-230d-356e-bac5-3df01067017c | -10.33785 | -48.80697 | 2025-09-12 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 503f92fe-910b-3ac9-89c6-fd7bb8c18ef5 | -9.04838 | -47.05888 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e015570b-6e96-3896-968d-56e9dc482589 | -11.36495 | -47.31351 | 2025-09-12 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 013cfc47-4907-3f9d-982f-413c0a75a251 | -6.5594 | -43.14606 | 2025-09-12 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c6c13f5-70e3-3ea9-856a-e6f98431c9eb | -10.56014 | -51.48411 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fcbe1ed2-5a4e-33c7-9489-8d14105bc745 | -8.94891 | -46.09134 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df29e334-650a-3aeb-b945-cc1727ede75d | -10.43705 | -50.61195 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fff89a1-b3dc-3040-8115-073e9693e874 | -8.33142 | -45.40693 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd9f09f7-ee35-3164-a7db-ec3b2028fc9e | -11.69042 | -46.57696 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f273a69d-4f3c-3866-aed1-d53bfecadcde | -9.9895 | -51.71538 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cc03a89-9320-3ffd-89d6-15f60dfa510d | -11.17429 | -45.28163 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc7af142-0a26-3263-a914-76b19f79714d | -7.85531 | -44.80913 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab60967b-0d96-332d-877d-93fa12d1b0b7 | -9.71493 | -46.8798 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1bcac7e-fd58-30a5-9ec6-794bc149ceb8 | -11.69368 | -46.51166 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0bf1c7c1-9ab9-3fb9-8a46-9a8a384a3fec | -7.44951 | -44.39746 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6344b8b7-f233-3dec-9afb-73883dd0af70 | -11.53546 | -50.59491 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 39ee18ee-613f-3841-83a8-4bfc4a40c02a | -11.72708 | -46.51691 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d0a022d3-631b-32ca-bf2f-cc8acaf90acf | -10.67139 | -48.59099 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f0141a94-9f7c-3038-95e9-4f37371c3b91 | -6.18254 | -42.74808 | 2025-09-12 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 124889ea-e089-3dfa-b0b4-ef5d9994f2ad | -9.99562 | -51.72681 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31434c5a-9cbe-3435-8c0f-21e50c374636 | -10.18724 | -46.24623 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44b0e1eb-93fd-3760-b0e3-c91705081b32 | -9.10686 | -47.11827 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 324a0eb4-787f-33b6-85f0-29c26e77017f | -9.67524 | -47.5395 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2257bd5-cf76-307d-84f3-14cceb56659c | -10.88994 | -45.58881 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9d180aa-840c-3bf9-a19c-110cad428fa7 | -5.11892 | -47.52338 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bae4fc56-901d-3dbd-b97d-ebb9aad1a79a | -8.94504 | -46.09431 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ba026a5-cd8b-373c-8d5d-93febfd4d0dd | -6.1074 | -45.93746 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15e6caba-87a5-307a-ab31-cf54530341ec | -10.68158 | -48.65593 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f4b5ae2-af78-3b9d-955e-bf20c59728d9 | -11.52178 | -50.58821 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4ac83f63-04c4-3424-b167-5ee4402e0852 | -7.00022 | -44.78924 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e6471d7-f9ef-3195-bb55-3e4f28202074 | -6.81683 | -51.89224 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1031eb65-089c-35e4-8082-23795c90f750 | -9.03458 | -47.08169 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7bb0e553-4cb9-3179-baf0-49010528a46c | -7.44315 | -51.8354 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c99c49c-1ff6-31dd-9ca9-7ee39a74d3b6 | -6.60644 | -42.27215 | 2025-09-12 04:25:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fc3f14af-1461-351d-9a6b-a95f4a4a6d2c | -10.85704 | -48.15821 | 2025-09-12 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ff7049b-ffa3-36d9-9a76-901f4ecd25c5 | -11.41458 | -43.71169 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14411da9-60ea-359f-acb1-8ea83d61a2b5 | -6.30287 | -42.23298 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ea1dcccc-3483-32a3-9e18-71d08d386679 | -8.92822 | -51.07541 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf54103c-3cbc-310b-ac2b-e510227976ef | -9.72243 | -48.34398 | 2025-09-12 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 61e32468-10e2-3d4a-806a-4c326e6e1128 | -9.80166 | -59.10415 | 2025-09-12 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7332acb2-159a-310c-9471-f65cc89eb4a3 | -9.72054 | -48.08607 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73525ab4-c854-3f08-8977-c6f08acbe668 | -6.81841 | -45.64703 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 974bab8e-7362-335f-9b25-b83541faa118 | -11.97515 | -46.64398 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 284486e0-3822-3389-acb2-19546fda210b | -9.10907 | -47.12577 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb9ece85-108e-30a1-ac16-490e51b1841a | -9.95869 | -51.68358 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82edfbe1-e4de-354c-8c02-92c667859fe7 | -5.83118 | -45.27428 | 2025-09-12 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cca5c05-e75a-3356-bac5-97da09d68d6a | -6.67531 | -44.14747 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28ed477d-a36a-3695-9cce-5823dc3e8fac | -9.7426 | -48.34728 | 2025-09-12 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccc41503-6248-387c-8cfb-8a58ceeef2ad | -11.69763 | -46.57447 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ed19261-7c56-36a2-aaf3-93c3a71e8fda | -8.17976 | -46.10395 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c493800c-2a9b-306d-9bd0-789e028a705c | -9.81086 | -47.81712 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43294c19-acac-3253-ad24-7c061cd49077 | -7.85229 | -45.39565 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99a9abb4-0086-3c87-ab16-41f77f102a2f | -9.71765 | -48.30971 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 217ee01b-3119-3754-89cf-5bb8e0845e66 | -8.08613 | -42.56231 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9f0f5e3b-a5f4-3c70-a6f8-d5f12d26f269 | -10.73645 | -48.90224 | 2025-09-12 04:25:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00e45bb6-42a8-3d09-a0ce-969cca81d673 | -11.67545 | -46.60742 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0251d71-76ac-3f85-9752-b52d927a0cdf | -9.89314 | -51.87557 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea36aae0-139f-38c9-9aa8-25ef44ebe2d6 | -9.46089 | -47.64863 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fccdbe2d-f868-3f89-9202-bcd06f26b56d | -9.68466 | -47.52307 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3f4c9c3-1e19-3e2e-88fc-94bda8335256 | -10.08415 | -50.39079 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 391a0e9b-2477-3630-8699-fc81fcc039b4 | -9.06493 | -47.04009 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9215b7cd-b53e-3f29-9de9-fd171d5ecbc1 | -6.30192 | -44.23513 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c86f260-abbf-3fa1-becc-26f3b761068d | -9.99647 | -51.72179 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 729291e4-3a04-3413-a341-ce3fbd34ac7d | -7.39837 | -44.36248 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26b9e9fd-09d0-30c7-a806-0ea3fdff9139 | -7.36775 | -44.31582 | 2025-09-12 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d20a3ef-7966-3199-acd3-c2a9f7420921 | -11.36881 | -47.31054 | 2025-09-12 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01fa1475-5e0d-38c5-83b8-b2d35d53ba17 | -12.09351 | -47.58252 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dfe5ae1-db8b-3dcd-a9e6-99ee13e8ba13 | -11.49409 | -49.26695 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd19984f-7582-3334-b0f4-e5cdf1c4daed | -11.14851 | -45.31743 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 581caff3-edcd-340c-b379-c57ccf4c53da | -12.10837 | -44.87416 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cac9915-0539-3952-ad7b-0a8950fc64fb | -11.66433 | -46.59101 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48f5858a-4a88-369d-aee0-777826456915 | -5.54196 | -46.42152 | 2025-09-12 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c36e41ed-6c9c-3ae8-8163-c0bd9676ec33 | -11.70537 | -46.50247 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72e8d249-2997-399d-9922-175be837183a | -15.71892 | -42.19469 | 2025-09-12 04:27:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6f73e50-4072-3f5f-8d44-29b7069bff8a | -20.2633 | -42.12852 | 2025-09-12 04:27:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 5e0face9-6c00-31b9-8951-70608707e701 | -14.41366 | -47.31012 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c7805bf-986a-35cb-93cd-6cf00aa38b37 | -13.24703 | -43.77135 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README79.md)
