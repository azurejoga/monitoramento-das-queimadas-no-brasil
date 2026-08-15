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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78570bcf-3800-3774-9d40-07afc07aecb2 | -6.78542 | -58.74539 | 2026-08-15 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cec00836-fbdf-3e7f-952d-17e918b984e1 | -6.60611 | -56.35106 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 668f92ff-3d9d-39d0-97bb-31d8373d599c | -6.82303 | -56.44321 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 825da57b-7fef-3a6d-8b77-cf8696e98b37 | -6.81394 | -56.43406 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13a6b093-62a1-3bcd-99e0-8a904847a6f0 | -7.27023 | -44.68228 | 2026-08-15 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a15c06a8-c0f7-3fe3-99e7-bddf997d6749 | -4.10574 | -50.44732 | 2026-08-15 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6795bb12-17dc-30b9-9de1-6955516822bb | -6.80075 | -58.77243 | 2026-08-15 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8baa82f-9e4e-31a0-92cf-bbaaed58d25b | -6.79167 | -55.69136 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c29a3d38-6a7c-346b-95d8-60b569ef33c6 | -6.85828 | -58.9607 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6216e79-5a9a-39e1-9a20-b46ba8eea72e | -6.5999 | -56.34671 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 924e950d-1012-3602-9a09-92360b611474 | -6.63424 | -56.26406 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fc992cb-7f21-3a34-912a-8984252e2de0 | -5.11638 | -41.10363 | 2026-08-15 04:57:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bd9907d1-1c5a-355f-84e5-72840f9b1cb9 | -3.62651 | -60.32336 | 2026-08-15 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eb37cf3-cf0c-3cc9-9d57-18d74314fa41 | -9.12335 | -46.40268 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e02c439e-9149-3deb-b30f-9e5fd401e704 | -6.6271 | -59.04171 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0255ad10-8131-3d19-85fd-6aac6a27e734 | -2.41204 | -51.83743 | 2026-08-15 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e50a650b-40b9-33d3-a1c5-8a66a42c7f7f | -6.86057 | -56.40693 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb7efbfd-8197-3f66-ab31-e8132ac53392 | -7.68867 | -55.15864 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3d9bc711-2326-37c5-ba66-dcb4112923ea | -7.8186 | -44.11352 | 2026-08-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 409ed8bb-d9fb-390d-ab56-e2c908c635fb | -4.36754 | -55.76966 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24be3bf8-aea7-33b0-84be-52549ba56f2f | -3.59439 | -58.62011 | 2026-08-15 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0e8542ca-e185-3a2a-8eb7-2d95dde25f6f | -8.49343 | -44.74352 | 2026-08-15 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1d7d09f2-c21d-3efe-8d4d-5a2ebe6881a9 | -6.93852 | -52.78602 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0058de9f-9b9e-3ba3-a924-94e6cdc89e4e | -6.99796 | -44.82807 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d194770-065c-3faf-9220-6521f21f0312 | -6.61752 | -59.05055 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 40ef85bb-8089-3b46-90d9-78c39c602003 | -5.49307 | -45.12343 | 2026-08-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83131c99-421f-3fa4-98dc-34471e43d0ba | -6.84607 | -56.43145 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c60c6f42-0083-336b-aa9d-91db0df45069 | -1.96402 | -48.36938 | 2026-08-15 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fedbba78-bf3c-37bf-a0ff-51a66fea9325 | -6.96957 | -59.28583 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fad3bd04-f448-328c-96f5-ee83b6a913ae | -4.10373 | -42.5013 | 2026-08-15 04:57:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 654086f4-de12-3e01-9e11-6fe2d9c2280e | -6.8295 | -56.42502 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 965630e7-78f2-38a3-b3e5-8696bbd42d82 | -6.79309 | -55.83525 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb82cac6-f7e5-3171-a50e-35c25a96845d | -6.54236 | -55.17997 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c4f1c39-5321-31a3-971b-0c78e5ed27a1 | -6.60038 | -56.36588 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8626ff9a-e1bd-391a-abaf-2d44f78346be | -7.01793 | -41.43908 | 2026-08-15 04:57:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 21fbecd9-ca55-3ba0-b293-39f8e731882e | -6.92263 | -43.64 | 2026-08-15 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6f4e4e50-5a64-38af-b262-36c318ee4bf6 | -6.70653 | -58.95159 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 03c813c3-c3aa-3176-98b3-2bee4d3d68af | -6.6037 | -56.36594 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ecb89c7-afc2-3c88-9681-18eeb9b563b9 | -6.79684 | -55.84372 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae272f5-184d-3a0e-8d41-d474d2d99183 | -6.02102 | -57.83936 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a5c1888-3bfd-3e49-bf24-c1c9b6618448 | -6.83698 | -56.42232 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25ab8bcf-e94f-35e2-878b-a6341df48847 | -2.62963 | -47.99801 | 2026-08-15 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6248f47-13aa-3f83-ac1e-7db6d8b99b94 | -6.7959 | -55.83939 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c61fa5f8-1619-3eb0-9162-d0a3cf2b3afe | -6.85745 | -58.96567 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0ab12ad-9fff-3e68-9c11-5a8e05eec7e2 | -5.93327 | -43.64052 | 2026-08-15 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7f91d9d5-a9ff-3f3d-9df7-43a2b6233367 | -6.96047 | -59.29143 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7f7f2dc-6c58-3260-9301-94a88a9b9616 | -6.969 | -59.28927 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebad55c6-ee93-3abf-9fed-654b14dc4d30 | -7.06084 | -56.51557 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db35eee4-8b4f-363c-b113-3de6c63bb395 | -6.61974 | -59.06144 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 146fb4b5-259b-3f5c-aea5-31e2bbb66b8e | -6.59635 | -56.36909 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90335cc3-42ed-3e4f-8cd5-42612b8873db | -7.40804 | -59.99512 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8becd3e9-5f11-3776-b8c3-b26dc49d0e84 | -8.02419 | -55.12292 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86e1fdfc-900f-3d66-acf2-61129da54f6c | -9.10806 | -46.40056 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf8f80cd-2f2b-3600-8620-1825b3157340 | -6.6148 | -56.3409 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af4bec2e-22b1-3d23-b254-3ba46d584f03 | -6.70734 | -58.94662 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 35d66d7d-3b1f-3dd4-9096-5040cfca8b33 | -2.68803 | -48.21769 | 2026-08-15 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6ec2257-e568-315b-b02f-76ed677629cc | -2.88107 | -48.85497 | 2026-08-15 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 412af4c3-c9ee-3971-9549-6d00a4e73dfa | -7.05619 | -56.52254 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7939aa8a-8e00-384b-b6c2-decb6c1dc4cd | -5.66936 | -43.57874 | 2026-08-15 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2dfb5bb-815b-3824-83ff-79b5ad25ffaa | -7.96786 | -46.78843 | 2026-08-15 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1d7d4ed-0f79-347c-9b95-bfc74f7a79ed | -6.5941 | -56.3611 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8326232-9f4b-3929-85de-549918ed6fcc | -6.85414 | -56.42505 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41159d67-d7b8-36e7-98c1-1bf9af9d7316 | -8.29819 | -55.10977 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0108337f-670d-3f9f-a528-92cfea5f8209 | -1.77964 | -55.53097 | 2026-08-15 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbeb1891-f19c-3e06-91c6-531c9960a991 | -6.85757 | -56.42561 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23b9771c-9813-3537-9f62-eae6ae19f193 | -6.92969 | -43.6325 | 2026-08-15 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d9d2afd5-14ee-3c74-a6da-0dcea1a6f66f | -6.85594 | -56.41385 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db41f53a-9966-3580-a142-064f8f9ebcda | -2.98267 | -53.21698 | 2026-08-15 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 987e90fd-2a75-3324-93b8-04244c9445de | -6.61255 | -56.33302 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b1f9221-dbc2-38fb-890b-833992dadba8 | -6.63055 | -56.3741 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d55636ae-9fce-322e-841b-197ecbe6ea60 | -6.70181 | -58.95586 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a72fec0-930a-3e38-8aa2-49963b2c94c1 | -6.85997 | -56.41067 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eefe9913-3c8e-32b6-a425-1bed72357b70 | -9.11909 | -46.39564 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d135983-a280-38bf-bf3c-b1e5bb3b360d | -6.60622 | -58.99904 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| dab4bfe5-f8b4-3351-90e3-6e19627dd5f6 | -6.61098 | -58.99458 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 475d4d09-82d0-3e35-a802-87a1fa6589f9 | -6.02173 | -57.83493 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98022b74-8d34-38fe-b342-cf08f2aa1522 | -5.69018 | -53.75704 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5853cef8-426b-328b-ad6e-2bff950550e5 | -8.71711 | -49.60894 | 2026-08-15 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd651dfb-142d-33d6-91c1-fae676c31fcf | -7.41984 | -60.0009 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4b578a5-fa77-335f-8056-fa2d7f9d97e6 | -6.96786 | -59.29617 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4be0836b-b35e-3817-9296-4e628e5a4ed5 | -6.60972 | -56.32877 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f267b34-1ef2-3dbb-abe3-fd33a09aaaec | -8.71827 | -49.60155 | 2026-08-15 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdbd1ab3-04ad-3bf2-a9cd-f3b5dd84eb1d | -6.62422 | -59.08303 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ca39aad-40ec-397d-8ccd-818c51d9ef91 | -9.57464 | -45.37123 | 2026-08-15 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79b4fd19-fe89-3b88-8271-8c231374b01b | -8.79452 | -47.92785 | 2026-08-15 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e7ac1c3-8012-3c8f-a5d6-976bcb9c9fba | -6.79224 | -55.68777 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1a3bae7-ddbb-3fca-89e0-f3ce2fae2bcf | -6.83436 | -56.46033 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f134806e-37c4-363f-bdf4-410b2031ce00 | -3.81997 | -50.63227 | 2026-08-15 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29a15356-64af-3cdd-879d-de653bee876c | -6.84796 | -58.97434 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5abb5308-6fc9-37b6-8c11-9a00637b2b1f | -2.85822 | -46.80182 | 2026-08-15 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d367957e-bd72-3843-9f55-e1c1d5815608 | -6.2687 | -43.28101 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8eb28179-871a-326c-9dc5-59ba62cc63ad | -6.96559 | -59.28518 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6609f70e-e433-355f-a0e4-7d00d35777cf | -6.94106 | -62.88018 | 2026-08-15 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae558cb6-34a8-3768-82c1-ab8b65c3a9b5 | -6.84788 | -56.42023 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed7643df-d5ea-3830-9f3c-e7c434e5b593 | -6.70571 | -58.95657 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c77274c4-de93-3808-907e-ebf5ad9b09fa | -6.99689 | -44.83167 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5d2c5a8-ecd3-3f8e-81ed-a9764c5d38bb | -9.16729 | -45.82787 | 2026-08-15 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f1a858a-9c12-3e21-b51e-df7fdbdf5d5b | -6.6158 | -59.06078 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b8093bb2-e859-3bfc-9543-6fd14a1071f9 | -6.65258 | -56.41234 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 936d6413-2d38-3cf7-b12b-7cbfcc717d23 | -6.71757 | -58.93309 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README26.md)
