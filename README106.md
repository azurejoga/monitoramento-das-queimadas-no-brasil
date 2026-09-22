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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ae80625-9112-3d1b-8a0d-1d6227841750 | -6.34783 | -57.77368 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc92d916-f4f3-399c-b191-1f68721d892f | -3.71732 | -60.55586 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6430e1e2-7add-3cad-b40d-6d607f2e9e5b | -3.28984 | -57.86323 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1bded160-25ed-3bfc-9fad-9ab2d9f1b9c9 | -3.78852 | -60.74857 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 475f291e-b2f9-39a3-8c9d-4a791b4e7941 | -6.10109 | -57.68188 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9433b2e-1c9d-3871-8768-ae97afb73a6e | -7.7217 | -61.25417 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa65cc04-97ed-3363-85d0-868e6ed079d4 | -5.87064 | -53.64267 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a88592a1-05af-369a-a2cb-42cd26985e52 | -5.85126 | -53.5299 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fac3cdf-4021-3c8e-b6df-4c45bc9957a8 | -6.35839 | -58.29348 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25697149-f7b3-31aa-afb0-905da55e0197 | -3.39086 | -61.29192 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20bd4b13-d705-3c76-bc49-b4c9a05066e5 | -3.60997 | -60.57303 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2ffd9d2-3e89-3ce8-863d-df6e1547f9dd | -4.41163 | -55.2431 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6686ceae-3417-35cb-a380-10f269bb34d3 | -3.51871 | -56.9096 | 2026-09-22 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a788c352-f5a0-365e-995b-2172ac10951e | -2.86271 | -57.80023 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 618ec8e0-04a5-3f60-a0d3-2f20f30f13a7 | -3.2267 | -53.94814 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0c15683-c06a-336c-a1f2-c24963cedeb9 | -3.22076 | -61.05598 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88a87793-2afd-37af-9757-b7b80dba1836 | -2.95476 | -57.72331 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a2e4eca-c2c3-32b9-8a27-dd69b7b77d68 | -6.62083 | -59.92479 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 913687b0-e465-3975-8293-ddd1075d30d0 | -3.46614 | -59.55435 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 615850d7-fcbc-35cf-8e44-09dd5799c0a2 | -2.99905 | -60.79879 | 2026-09-22 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b69da07-f678-3093-a3ed-c0136f260e77 | -6.6239 | -59.92755 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| d869700b-83c6-3a83-84e1-bd60b25674aa | -3.75207 | -58.32951 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fca99a8b-3481-3776-930f-87df7817d533 | -6.62525 | -59.91831 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 472f1b99-97c7-31c3-be5a-1b19c55255f0 | -3.39984 | -59.52885 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 70774011-834e-322e-9364-639a38a8f004 | -6.15462 | -57.71102 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 757cdd49-d1c0-3afa-8440-ee50911539bc | -3.61058 | -60.56906 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a65d9a1b-d36c-33dc-a7b2-d4acb7015b59 | -3.08064 | -61.16965 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a162224c-a799-3ce0-8e3e-88350bb9b38d | -8.61774 | -54.61687 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4648dba9-38a5-350e-8996-63ce90734645 | -2.7904 | -59.88772 | 2026-09-22 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5c2ccc72-bf31-3bf0-b14e-1d12369f8c7a | -6.90111 | -57.6131 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7063f64d-bf3c-36d6-80f5-7d5c30ed57f6 | -5.43363 | -60.23064 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af155e9c-0f53-3d67-bddf-90e80cbf30c0 | -6.46718 | -59.9936 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 503cadf6-9fad-3489-a9d8-a15f3b63768e | -6.33679 | -60.01337 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c849110-ac81-37f3-8ab3-b8478c552757 | -2.56615 | -57.50489 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1beb0d49-9a13-3a13-9db8-0ad0cfab29bc | -6.71194 | -59.0003 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa9c1121-e9cd-30ed-9ff1-b1eb9dbfbff3 | -6.43944 | -55.63934 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b86efb1-7f57-3152-82f8-503d6c857295 | -5.8045 | -53.52257 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6451c82f-7734-33c6-b11d-263dd0631aa7 | -6.7848 | -63.13356 | 2026-09-22 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d294769e-6d1f-3a65-855c-141a57f04522 | -3.6871 | -60.58894 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37f4a81a-d982-3dc8-b94e-e1e6f4cc9108 | -6.1001 | -57.62247 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b73af6e0-6e3c-32ce-ba8a-bd30fc3ef1a7 | -5.93943 | -57.70731 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5befc590-49fa-3113-ae73-5ba50931a73f | -6.64043 | -59.92053 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4c64a6c3-3152-341f-a030-6b0f7b44d30d | -8.6107 | -54.62718 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 618c22d1-2f35-3b58-b0a1-08551295a66b | -5.72482 | -53.46159 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c628b6d-470d-36ce-ab58-e743e39aa2de | -8.60369 | -54.63735 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93c0b296-3c16-3873-9a09-b5a3b90aeef8 | -6.30425 | -57.73732 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0bfce2f-4af6-373f-9660-0581c855b4f5 | -6.75646 | -56.32727 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27f355a1-c64b-3b9b-a0e7-b92cfdd4bdf7 | -6.83045 | -55.53846 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cc2c5d9-f923-3116-bf03-87eeced06c7f | -3.93233 | -56.04913 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0324f6a-60c1-316b-a8d8-2f46a87c4a1e | -6.05966 | -57.8624 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7631412-84b3-355d-9e62-5be69b3f243f | -4.9403 | -55.8175 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dee7b0e9-e81d-34a2-b99f-f61902aea321 | -6.11695 | -57.75649 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7ecf86c-c44b-35a5-8474-c6d2f7bbfa1e | -6.16401 | -57.79718 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f8e7e6c-5fca-3545-9f59-6596aad2fc2c | -3.14288 | -61.39848 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad0b46a9-9e9c-3924-8b5a-0a622b90ab54 | -6.12238 | -59.94791 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edd873cf-fbb1-3741-aaa0-2ef18e94e39a | -6.79697 | -58.79128 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 160ae1e8-00f4-3f23-adaf-6b80086cebd5 | -6.34881 | -57.88754 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b77afde2-4c13-3a1a-bb43-cd7b3d7c39b1 | -7.45618 | -61.38143 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d010d698-a8fb-391f-ae1b-4ef450139c75 | -6.45863 | -59.97359 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10a1e735-f6d5-3a85-bde1-25fa4a12b379 | -6.51971 | -58.30854 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6788a1b9-35d0-3162-b693-c3215ff72e83 | -7.57536 | -61.16582 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6558f1ed-a1ee-3527-b9a8-ce5471d88003 | -4.10279 | -56.34763 | 2026-09-22 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62f6f600-bc1a-352e-bf32-ad16902a21f7 | -3.65879 | -58.5794 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eacb27f7-64bd-328d-aa1b-1c459acc0b0a | -4.26562 | -55.43942 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0e27b13-eefe-3b80-a93c-baa5a85ec3d4 | -3.12569 | -60.68342 | 2026-09-22 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5687c80-8de7-333d-a7b2-7f52f0a69208 | -6.09613 | -57.67852 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fc87a476-3c6e-34e7-9cdd-036877c125d5 | -7.6033 | -55.3589 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81367d8a-1a29-375c-94a9-45fd606b5f94 | -6.81604 | -59.43182 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f716767-6355-33e0-87b1-305b50ceee11 | -8.62282 | -54.62135 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e30c8d6c-c77a-32b5-beba-6bf38e77f3fe | -8.62693 | -54.63298 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28cc1fad-52cf-3ff6-99b7-ae59cb7f479f | -6.63906 | -59.92985 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| dd7f3580-4175-34df-8d5f-0b9efd106519 | -6.1354 | -59.96366 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1914553f-bc8d-3c51-9695-fac1498df5f0 | -4.07719 | -55.32201 | 2026-09-22 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffbb3f36-024d-3eaa-b2d5-fae2732337b9 | -3.07279 | -61.17622 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a07c2cd8-c3a0-3d57-a7b8-25fee5f2a3c8 | -3.74858 | -58.32537 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c98a0a9-c76d-3539-b4f6-8241970b084d | -4.34288 | -55.65046 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 080286f3-97c7-38cc-b2e7-273d98ff38d9 | -6.62462 | -59.92535 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 59cd4f9c-b5ab-3511-86ab-f24b895999a8 | -3.41827 | -61.29612 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f900803-b443-3f3b-974c-ddd2b39fee26 | -3.58416 | -59.06282 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ca803e2-9cf6-3e32-b42e-8a0bc1229d70 | -6.08573 | -57.62896 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 640b46aa-5536-3dc3-b78c-812e195e06c4 | -6.09672 | -57.68139 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1c66ef6c-faa3-3f18-9f4e-6049286006de | -3.82079 | -59.33534 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0860c44-8504-392a-bccc-1ed9cd69b51b | -3.34007 | -59.86561 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdf49bd9-c149-3f88-b4bf-1c2a99065a12 | -4.66358 | -56.03453 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 687a42bd-46bc-3fed-b8bd-d8ae449adb17 | -6.07502 | -57.73046 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bc6c40e-3f77-3ecd-8541-0266dcf79f01 | -8.6325 | -54.63372 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08623714-1f7b-3967-9174-b90aab44a576 | -6.75726 | -59.06388 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63464eaa-fe04-36cf-8680-c09c7632930b | -3.11809 | -60.68622 | 2026-09-22 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fded91f3-b04a-3877-8847-780ce81e9843 | -6.81193 | -59.43369 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e96958e-fbf2-396c-a37e-89e3f78f561e | -3.92213 | -56.05289 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56ffde0d-ad88-36e0-9469-9393fdc8afdb | -5.01205 | -56.09266 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1909c586-1c46-3986-8391-f1d5a39e8706 | -6.45485 | -59.97302 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64571bc5-368f-3dde-9bc8-993022858919 | -6.92335 | -59.62805 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d704c16-a51f-3213-bf19-0689f4ef3ddf | -7.6968 | -61.53376 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5241b4d5-fc28-3a2b-b236-66991ae03d51 | -6.81132 | -55.82734 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cc92083-24c8-3710-8f22-d98342818758 | -7.39732 | -55.22521 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e3bc55c-e168-3410-b2e5-dbec1305b128 | -4.68259 | -55.6318 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fd02d47-6a93-3690-a044-9efda771991c | -4.55941 | -54.92062 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96d832c5-669c-3a53-8ade-d154a8aae8b2 | -6.13164 | -59.96306 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c344676-d211-3119-b03d-a630182b2716 | -6.79082 | -59.95065 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README107.md)
