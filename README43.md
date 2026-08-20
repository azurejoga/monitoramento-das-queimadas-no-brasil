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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50747c64-f681-3e88-b580-dd14fb99642c | -6.37862 | -54.93999 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ce0f6cd-6b5d-32a3-ab90-9a4e7e9752d7 | -5.95217 | -52.2078 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 345300ab-41b2-3d73-b46c-2ecab068af1b | -6.13053 | -57.87337 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6b62042-c9bd-3d46-bb09-acfc498de34f | -5.80633 | -55.71439 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c303400-a7f6-315a-8868-5330d8f0f441 | -3.09802 | -61.19398 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05aa5830-89e1-3a32-8f0c-40ba0553fdbf | -7.01638 | -47.97141 | 2026-08-20 05:04:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 624a2b89-b730-38ab-8c4a-a9b0dd4bddf9 | -6.43844 | -52.73513 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebceb924-4ad6-3b69-b712-c1bd2a380ff4 | -6.24292 | -55.42265 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a7cc3ca-8e50-32bd-a6d2-4cbb9ca4c510 | -4.38584 | -55.46988 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a26a8753-bb6d-3ba3-a507-dfa6b2f18821 | -5.91225 | -52.45215 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 721938be-7d3e-30a1-9163-1372d07fced4 | -6.42687 | -52.76325 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 963d633b-22a2-35a5-98f8-85845b27cd59 | -2.59729 | -47.93896 | 2026-08-20 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a4010c1-6ca0-389a-943d-0f39ff9254f9 | -6.10308 | -57.71602 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9acc39-b8c8-3bc4-b8db-28fc95560a7a | -7.46092 | -45.14696 | 2026-08-20 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 650fa20e-842e-3a01-82fb-f2630c85113e | -6.38583 | -54.9375 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6599d18-dbf8-344c-9790-6845a411d5ff | -7.96976 | -46.9215 | 2026-08-20 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88dd63c2-d9e5-3b3f-bafc-902848c18f6c | -7.35643 | -45.81985 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 84095c58-4863-34b2-87ca-469a4ae64f26 | -6.37808 | -54.94351 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9efa9374-c059-38aa-890c-cfec6871fe43 | -6.5874 | -58.9712 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f33ebc73-11b1-3185-a5c1-a643f064c661 | -3.97756 | -49.19395 | 2026-08-20 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 656d81c5-0da7-3b58-8552-f98fcd2f9bb8 | -2.04806 | -48.03435 | 2026-08-20 05:04:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f7c3eec-10cc-3db8-b7bf-48aeb5586d7c | -6.35049 | -54.90344 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 222ad899-cf87-3b8d-be67-158098ed85a8 | -6.48791 | -55.15773 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85479636-5ef8-3c04-871f-3271d62044ce | -6.95437 | -52.81502 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4f318fe-7dba-3008-8699-fbfd5f347758 | -6.68777 | -59.09291 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3606eeb-848a-3cad-a0da-32ceb2c775dc | -5.80087 | -55.72767 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7acf0535-ce8f-3734-a0dc-a8dfb4907250 | -7.35488 | -45.8319 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ca5dd6d3-fab9-3a0d-9734-b243c2cda241 | -1.83422 | -54.4929 | 2026-08-20 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc0b2c08-7c22-3071-8d63-ec11ab16111d | -6.37916 | -54.93648 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddc65b9e-0df1-3be5-a5e6-a0accd397d1e | -6.71535 | -59.09209 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b90f96b2-cd25-3358-a732-abfd6397989b | -6.10697 | -57.7356 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c05b5dd-556b-3139-9f9a-b7e7244c599a | -7.02214 | -45.8877 | 2026-08-20 05:04:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 203f96c4-3061-30d0-a9a7-a8bbe3905697 | -3.68847 | -47.64967 | 2026-08-20 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5f2bb49-728d-3c2b-9d03-72906f4f036c | -1.78503 | -55.52771 | 2026-08-20 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22327f80-c0e9-3f95-8a1c-e1a46a2f6d92 | -6.89307 | -56.44274 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8d3d2ee-4e51-32d5-ba7c-1c2e7b4ad5bb | -2.59265 | -47.93822 | 2026-08-20 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e3ccaa9-c012-3780-9a92-b771eb8ae2b7 | -7.34861 | -45.83514 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6f646fab-a3a4-3217-b74f-087165661459 | -7.97339 | -44.65613 | 2026-08-20 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 326c4e44-e78b-393e-9971-4cfc2c0b7c24 | -2.76874 | -48.57209 | 2026-08-20 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75c8e084-dd56-3175-aa92-946fe15d670e | -3.68291 | -47.65417 | 2026-08-20 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9df97c25-b642-3603-8be7-b6dc3d136ab1 | -6.35103 | -54.89992 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2a79ab8-6e8a-3a61-a86d-97b62ac0aae4 | -6.62472 | -56.26864 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebbecb4c-dcc2-36a3-9685-ad6b593523ac | -6.24623 | -55.42316 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76c2e931-f3e7-39ef-b7a4-1893cb2ba374 | -6.43657 | -52.74764 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2709fd95-44c5-3e0e-a621-b8a38503c4b9 | -6.14791 | -57.85301 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc778c6a-3509-32b8-8bff-d06c5fe5512b | -6.78747 | -42.88657 | 2026-08-20 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe658401-1d7b-39c6-be84-7ff43869588e | -7.96653 | -44.66011 | 2026-08-20 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4761147d-71d1-38f2-8c36-8830051bd742 | -6.14387 | -57.8562 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccc8a863-242d-335c-97a9-177c1fed2da2 | -7.09836 | -55.45295 | 2026-08-20 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbee95c6-ea9f-31b3-be01-6e9e9ee62895 | -7.34913 | -45.83113 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 13ac12c8-a515-3928-b7a4-ee5bf42096f2 | -3.97816 | -49.18979 | 2026-08-20 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7407ede3-79fc-3237-8b1a-ed5664d4c98b | -6.87923 | -56.4228 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30585f08-4077-3b69-a9c8-4e047fa9c995 | -6.54943 | -56.55202 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5b965dc-ab87-3b41-80a1-bd2c609fd5f1 | -6.68338 | -56.15375 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0dccb85f-3b5e-32af-aa81-aa2cb7bb78e4 | -6.23375 | -55.61246 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66da7749-fba2-3756-bc34-b6379d669b88 | -6.42555 | -43.06831 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 42968f7e-755d-3554-985f-ab57ac2df571 | -6.69858 | -59.09462 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15fc0d05-8026-3fe6-8dbf-030ec51e132c | -6.25223 | -55.40634 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52567727-1d6e-3bdf-9fc2-9905cdf66357 | -6.43247 | -52.72568 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7cbb3f3e-d4bc-35b4-bdd4-bd1ecc59736e | -6.6996 | -59.09797 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a1d05c1-761f-3f88-8b6a-efc319f099e3 | -6.13963 | -57.88247 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17ffe264-dd61-3dbf-8ca6-cb4d81a6da0f | -6.71895 | -59.09267 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43f6593f-e7c5-3fb4-92a8-9a3b49ded215 | -7.02161 | -45.89175 | 2026-08-20 05:04:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09d93de3-0703-35b3-859b-4b3925d51e07 | -6.31195 | -55.91816 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ece0ea9f-0cdd-3fc1-8fb4-5c6bbeabd45b | -6.44205 | -52.73568 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c772102-e5f2-3ed9-8588-b43e95f3ebda | -6.41142 | -54.94863 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70920479-aa82-3145-b3ba-55373355a952 | -5.49395 | -60.13944 | 2026-08-20 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8743ef35-7e4e-3e81-a0da-773ab7897ade | -7.01559 | -47.9771 | 2026-08-20 05:04:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b069c59b-2af3-3704-8829-88707a734bc4 | -6.26452 | -43.2773 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| abdf480c-e6be-36c2-8c97-183eeb03ce77 | -4.9581 | -56.26784 | 2026-08-20 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc770ba9-f6f1-3e41-9f60-25dd111749f5 | -6.952 | -52.80605 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 945a556b-4bc0-3c5f-a8e4-4360062c47d6 | -6.0063 | -57.86153 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 207cd423-6b43-34f9-aceb-fe62ca29f7be | -6.00914 | -57.86587 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 430475a4-e0cb-3f07-b0e8-0b58db66f95a | -6.69659 | -58.94601 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5c830f52-b56a-303b-951e-c83d85214432 | -6.44512 | -56.15539 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6acc812-286e-373f-a783-b16b7b5ae3fa | -3.9031 | -55.88142 | 2026-08-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a59372f1-7ed1-3005-8743-af24a9bc8c82 | -6.43309 | -52.7215 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94de207a-c83f-3898-93de-167aa8471647 | -6.25277 | -55.40288 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7652546-c3e0-3f88-9bd6-286d636558f7 | -4.95315 | -56.27774 | 2026-08-20 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21877e5c-2da4-36d3-a6db-ba3ab1c34153 | -5.80418 | -55.72818 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e25a65c-b848-357c-8b63-1b7ec8696472 | -6.28968 | -43.63594 | 2026-08-20 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1fbcf656-2adb-307e-8183-83ad74f5ca3c | -5.79972 | -55.71336 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e67262c7-f325-36fc-8af7-538a57ce40e3 | -5.79757 | -55.72716 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82b4f89f-ffb9-3a52-8016-19405d557d9f | -5.36277 | -60.15528 | 2026-08-20 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7652f5e5-ccbf-35f1-bfd3-a6670d0d094f | -6.35695 | -51.74517 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1c79cf9-99bc-3633-92e2-9986fd6b22cd | -6.31249 | -55.91471 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 706d5a47-ac76-3768-9dea-14025dc451fa | -6.44552 | -52.76174 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33438e3b-2ddd-3925-b254-10a1f2a57cc4 | -3.53678 | -48.18307 | 2026-08-20 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce416b1a-7275-3482-b063-b32424472ec5 | -6.08526 | -57.91601 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60cc7fd9-9771-32fb-8b39-b304d8f74228 | -4.78751 | -62.92202 | 2026-08-20 05:04:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2c0a31e-9b94-30e6-af30-a545010dcd89 | -6.44094 | -52.71841 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efdec97d-4064-3330-abc3-7a1eb76a04b9 | -6.34365 | -44.08145 | 2026-08-20 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 325bc961-baba-39ef-a2cd-cca80190e50f | -4.44437 | -55.37674 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9761ada3-aad2-3005-82ea-f06f7abf2a16 | -7.35591 | -45.82388 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 312bfcb2-e883-3911-9fb4-d2964549ac7d | -6.24677 | -55.4197 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e43de7b3-eb77-33d2-8c92-89bc8be9f92a | -6.70251 | -59.10274 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 324dcd78-55c5-3df6-84c9-1ff0cfdc996c | -4.28023 | -46.51426 | 2026-08-20 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b8a4c10-5a96-3315-b670-cc309236f347 | -7.34965 | -45.8271 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6b138764-f566-3ca4-bfb6-77523a2cdf00 | -5.42945 | -43.43156 | 2026-08-20 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9f82491-8279-31c1-8975-33bdef3d0c24 | -4.45613 | -55.4562 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README44.md)
