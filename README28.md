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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17046031-1320-3db1-bb67-c6dc2776fd14 | -7.77671 | -44.9991 | 2025-07-30 04:51:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d649571d-79ff-3b66-877f-aee9df0712f8 | -13.08215 | -47.31113 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4dc47ee-e4d4-3c59-90d6-66e4a0fee737 | -8.30258 | -47.35096 | 2025-07-30 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87233e29-e723-324d-9191-15cf64669157 | -8.33688 | -54.75354 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26d7f46e-1cd3-390b-9ad4-cf6cb59bfaad | -11.8158 | -44.2592 | 2025-07-30 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e7d965f-f8a3-324c-ae3b-6b0cf3d64eb5 | -8.33409 | -54.74935 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71f5efb5-a2bd-31de-a194-38a36601fe25 | -12.47517 | -47.27563 | 2025-07-30 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6825dfa7-aa63-3ab8-8c6c-2a12843fde1e | -6.52302 | -56.2146 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6df3d90c-7466-3106-9a6c-6ebe4812b61e | -8.95509 | -46.7353 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce6b771b-4a86-39e3-8812-ff5f4c82616f | -6.53104 | -56.18818 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 72224377-709d-3a7a-a923-9802506b777e | -8.95532 | -46.74671 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d73f97be-e229-3acd-8601-352a3b0876d7 | -9.15239 | -49.84728 | 2025-07-30 04:51:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67c80929-44bc-32c4-9ad7-a46e8546217d | -6.55435 | -56.18334 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a0a2302-0edb-3c22-95b2-a6ee220fb6cf | -10.61632 | -45.24669 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 09e21699-ff09-3b01-b865-cad5471e376b | -13.07293 | -47.38363 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 602a4fca-12a4-3d3c-83ae-f1488167996b | -7.77592 | -45.00471 | 2025-07-30 04:51:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee931dc0-79f3-3689-abce-9b0dcec31b5a | -9.01697 | -47.97594 | 2025-07-30 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a345b4c-09ce-3343-83df-67a45a71d4e4 | -8.95387 | -46.74436 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce258cec-d13d-3b23-bcb2-20ddf14e0c3c | -10.70273 | -48.86383 | 2025-07-30 04:51:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0358e8a5-13b7-336e-b776-d5ac892a2da3 | -8.0299 | -46.90662 | 2025-07-30 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cec3f60-b8a9-3474-b947-2d048179bad7 | -8.32835 | -54.76335 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 988158ec-93d9-3950-a3fc-e7164fb6a13b | -6.5258 | -56.19741 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2628686b-aa44-3dc9-ae85-b75a95cee6be | -10.70437 | -48.86278 | 2025-07-30 04:51:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2524778-6c3e-3187-8a14-f784ae407979 | -9.20656 | -59.6711 | 2025-07-30 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b07ada64-66a0-3ee3-8b88-8e13bf349c1a | -13.66584 | -48.77622 | 2025-07-30 04:51:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f1d292e-cfab-32ed-93ba-70ecd433b25d | -8.33629 | -54.75718 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7b85130-b20e-3b92-9442-ba6b499b95ab | -9.23857 | -50.04348 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba223dfc-49c0-35bf-b2f2-72be86df1ba4 | -12.95197 | -48.25887 | 2025-07-30 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42f35caf-f2d6-3e50-ae93-7cd42d7192cf | -6.49375 | -56.20974 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68071c79-b38a-3d1a-b36f-4d02a7ec99e3 | -9.26387 | -50.22767 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c7e063f7-0c0e-3666-be38-1de5981ac6c8 | -11.53447 | -44.2634 | 2025-07-30 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c65c204-212b-3fa7-b738-105143f49340 | -6.95706 | -58.37644 | 2025-07-30 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e92234a8-a024-3d73-a504-1911976a2b20 | -9.15909 | -49.8527 | 2025-07-30 04:51:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fb5aa3d-a820-3fb9-add8-34c25e03513d | -10.34818 | -57.50515 | 2025-07-30 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c30e3a6-c106-38a1-9a3c-a061651fa77c | -6.96022 | -56.3808 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b5102d8-0dce-398e-be18-dac5e0cfb59d | -9.29722 | -49.47455 | 2025-07-30 04:51:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 820d0125-69fd-3d91-97d4-5da073fa02be | -7.72573 | -51.10116 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 323b36bb-8bb1-317a-a718-4ca81e224bad | -9.62891 | -48.54783 | 2025-07-30 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d640be4e-e963-3776-ab97-2ad6dbb0b086 | -6.50317 | -56.19804 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d5cecbdb-32b4-3f85-b84b-e74118ac5041 | -6.50177 | -56.20666 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4d14bb0-65e1-3401-95ce-de3d08c975ca | -10.35191 | -57.50581 | 2025-07-30 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9860a953-3c3e-300c-92da-826a72c8e7f2 | -8.51529 | -43.31489 | 2025-07-30 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 33a7c2ad-c73f-3cb2-b702-6b0c59ddf305 | -9.23496 | -50.04603 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d285907d-3d6a-3e34-b31b-698111014afd | -7.73715 | -51.09517 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ce23ee9-fe45-3a71-9942-a15e5e4aec5c | -13.06354 | -47.3848 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c83c052e-5b0f-323c-b59a-63c94001ec4d | -11.92188 | -44.544 | 2025-07-30 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfe64e6e-7dc8-3623-98df-e48437ffddcc | -7.94083 | -44.08947 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6413e86c-80d4-3a78-8f8b-0085e6f42e81 | -10.61709 | -45.2408 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 225362e1-9f8c-33aa-aad3-ce0081044ec6 | -10.97192 | -47.39865 | 2025-07-30 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e7fde59-8035-341b-a682-581ff38505da | -9.27202 | -40.55821 | 2025-07-30 04:51:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1886ecda-2fa0-3bff-921d-eaa5d24cfdeb | -12.5496 | -44.73078 | 2025-07-30 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45d64cf4-8254-30ae-bb2a-7fb5687ea107 | -10.61087 | -45.24892 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2ade7d12-c5c8-3b18-bef4-74aa6116f5b6 | -6.50543 | -56.20727 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 803cb0b2-ed48-3213-8fc6-8b09a8e08ff6 | -12.81552 | -45.44001 | 2025-07-30 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2511151-cc12-3755-be46-6b96f3e66f9c | -14.73935 | -46.30487 | 2025-07-30 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e9d0f5d-4573-34c3-b536-9898074ae0e8 | -8.88614 | -47.33672 | 2025-07-30 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e5623e2-4501-3132-a1b2-8a878f0d9101 | -6.49882 | -56.20175 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33ba2002-2f3b-3e87-a1d1-d7abbce408a3 | -10.09431 | -46.96976 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 898f8d58-7575-3ca2-b4c2-8a34c3d504e4 | -9.22631 | -48.59563 | 2025-07-30 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75a028a9-32a2-3126-ab47-671ef894dbed | -8.88186 | -47.33609 | 2025-07-30 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 311b3d4e-58db-30c7-9474-5a93be3ac8d2 | -9.23922 | -50.04231 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32aec0d2-b73c-3e26-89c7-eb53104be7ee | -9.22496 | -48.59764 | 2025-07-30 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9e69019-b750-3493-bf4b-bca080a988e5 | -13.08156 | -47.3158 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88b1d8da-31fc-3961-8e50-d5b8bc2800a0 | -6.49967 | -56.21954 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8584228-5057-3cc7-b748-fa281a8644af | -10.6128 | -45.23413 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9c5aead-7eba-344a-9f85-aaa8b1ec1e9f | -12.61642 | -48.0644 | 2025-07-30 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b339d897-b187-3acd-b24b-ea4549309426 | -13.08989 | -47.3233 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed5de5ae-c9fb-3a4e-bec0-246ee4e7325d | -6.49516 | -56.20114 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce449665-6bb6-36b5-9a3c-447c6aabf442 | -13.08278 | -47.30618 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30b98b16-4619-3590-ab7c-084dd49ad8b1 | -9.14872 | -49.84673 | 2025-07-30 04:51:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1ce5aa23-f221-3b42-a187-c3baaa55756b | -10.62177 | -45.24449 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a5092e47-8a83-3afa-b2f1-e4ccddd3387a | -10.9713 | -47.40317 | 2025-07-30 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae0a2d5d-f8bd-36b4-9179-7ba49c42d88f | -11.81625 | -44.25552 | 2025-07-30 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5287c4f9-9342-3b93-9379-e1522903db2a | -11.46792 | -45.11417 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a7c3f2ac-06ca-3515-9591-9d7ad187a9b7 | -12.54709 | -44.72974 | 2025-07-30 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c154e49-ac11-34da-9859-7704ae45ceed | -8.95957 | -46.73591 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 441ace69-d703-3ab7-b71c-aff270013f35 | -14.09714 | -53.97668 | 2025-07-30 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe6ffdc3-4457-362b-9cd1-3d618b6a69d1 | -14.91389 | -45.14826 | 2025-07-30 04:51:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0251cca4-5da3-3d11-b75b-de41e769cd28 | -6.50387 | -56.19375 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c85242df-345c-33c1-aeaf-282115d61c3a | -11.33781 | -51.24596 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaac4a29-15c7-3bb2-924d-bd487c5e536a | -11.46234 | -45.1167 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 74c21eaf-c66b-3902-ac1f-55c03641aa35 | -8.62453 | -45.88047 | 2025-07-30 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4066d2cc-4580-30fb-bccd-0ce858cff7e4 | -12.73031 | -47.00085 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4c9bfa7-5e16-33cd-81b9-6c3ec2ec633a | -8.32556 | -54.75914 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ac975e8-d81e-3777-b7c2-42814aa7a0f8 | -11.32143 | -55.21639 | 2025-07-30 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29d46bbc-ee96-3bf0-9abc-029b64d55868 | -6.55364 | -56.18761 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5f1f79c-c222-31b2-8fed-2930e3684a2a | -8.01837 | -47.67646 | 2025-07-30 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a9484ed1-2b74-3aca-8fe6-2341ab761458 | -11.47275 | -45.11765 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dffc7271-8757-3fe7-81b6-5e2287190576 | -6.56824 | -56.19005 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9d49053-faaf-3d44-b978-af706014fbfb | -8.02196 | -47.68085 | 2025-07-30 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5144cc71-b82c-38ce-8d6f-bfe776a5d8e1 | -9.29345 | -49.47403 | 2025-07-30 04:51:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f04ec31-abce-3f2e-8411-f7a2ae9d43ce | -10.60736 | -45.23626 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6211d4a2-a0a7-38db-9959-fe3c579be915 | -11.32386 | -48.92027 | 2025-07-30 04:51:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ec1392a-5326-31f2-ad44-8c19c79eaddc | -8.61909 | -45.88498 | 2025-07-30 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f223c36-2b1e-39fd-95d8-0253058b585d | -11.34542 | -51.24304 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96da10e4-0d1a-3706-8b29-d27a7ae4c842 | -6.52006 | -56.20969 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1fbdd8a2-c8e2-3df6-b42f-d0aede3348dc | -7.94039 | -44.0928 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c027d30-1db7-3bb1-a199-b993572f484a | -11.99 | -46.69839 | 2025-07-30 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23fbf8e8-478d-3ad0-acd8-d03842b5c100 | -8.0225 | -47.67708 | 2025-07-30 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85bfef71-76bd-3c6f-89d4-9accdad72598 | -6.61965 | -59.97979 | 2025-07-30 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README29.md)
