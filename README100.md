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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5245703-b301-3f72-a156-7b1b13983504 | -10.7115 | -60.7312 | 2026-09-19 06:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b378f3bd-743b-375e-8981-c9021f651de4 | -18.0303 | -50.9385 | 2026-09-19 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 8b3fc5f0-0521-3f37-8a7d-9de3a6bf30fc | -18.0104 | -50.942 | 2026-09-19 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| d0dd5a88-efd3-3175-b4bf-c1fe2aa61664 | -18.0502 | -50.935 | 2026-09-19 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 9d8ee572-858f-369e-8ba1-d6d851d9e88c | -12.34 | -50.7157 | 2026-09-19 06:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b6569d6b-7c2e-3fae-ad71-465aefff5107 | -10.6944 | -50.26 | 2026-09-19 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 68c131ac-f43d-3d4b-bab7-4fc565cd7ded | -18.0502 | -50.935 | 2026-09-19 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b6af436c-8247-3350-adde-033094624ccd | -12.34 | -50.7157 | 2026-09-19 07:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0681d591-91c6-3f2a-81d5-a7f100450033 | -10.7115 | -60.7312 | 2026-09-19 07:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 35efc099-9483-3597-8a54-e10e0c96c2ad | -10.7133 | -50.258 | 2026-09-19 07:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ee117bb5-2112-3010-b942-c49c84bd21f1 | -18.0303 | -50.9385 | 2026-09-19 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 0ef44e10-1259-322b-9f92-6b900907259d | -18.0298 | -50.9606 | 2026-09-19 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 6b89d746-179b-3dd6-8175-77d6278cb923 | -12.34 | -50.7157 | 2026-09-19 07:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| aed8b200-6165-3512-bd17-d90a36729904 | -18.0303 | -50.9385 | 2026-09-19 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 833d5002-4996-3d84-8d7d-e942e33a4df5 | -10.7115 | -60.7312 | 2026-09-19 07:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| ebcda896-93cb-302a-bdd4-5edc18495d75 | -12.34 | -50.7157 | 2026-09-19 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8479628e-38fa-38e8-b922-4590fee70700 | -10.7115 | -60.7312 | 2026-09-19 07:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| b22a2546-f85e-3398-a386-84ed8cf5f746 | -12.3591 | -50.7134 | 2026-09-19 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| af490301-436c-3180-83a2-236ff31918fa | -10.6928 | -60.7322 | 2026-09-19 07:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| fdf44122-6b72-3c48-b842-ec9074b4b971 | -1.58505 | -54.4254 | 2026-09-19 07:22:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cf8ad7a1-34aa-328f-a840-bfb9edaa2f55 | 1.2262 | -50.99466 | 2026-09-19 07:22:00 | AQUA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 31b9114a-9ace-3769-92a0-fac1283a6160 | -12.34591 | -50.69802 | 2026-09-19 07:24:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 1864163c-dab1-34f8-83b8-a1b307e3af66 | -4.38242 | -55.25458 | 2026-09-19 07:24:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 014650a0-938d-3b99-843b-19435104a2be | -4.5321 | -54.92984 | 2026-09-19 07:24:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd6e99cb-a2cb-33da-ad2f-ee77d9b685ae | -6.44283 | -59.98016 | 2026-09-19 07:24:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 925c0e62-4ce7-3360-98bb-52174a59d695 | -10.86718 | -54.09895 | 2026-09-19 07:24:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4ee490e3-27d3-3816-b4c9-d88c8ad7f0cf | -8.60564 | -54.59705 | 2026-09-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 449622f3-462e-31b6-9fac-be04a16f12a2 | -6.37181 | -58.28908 | 2026-09-19 07:24:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 68b05ed8-fdfb-3784-993f-8b006d6ddce5 | -2.89257 | -57.82175 | 2026-09-19 07:24:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| c4f8a668-02b3-3c11-8f1d-d879a7b6e499 | -2.89548 | -57.80267 | 2026-09-19 07:24:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 0dba5a14-2112-37ef-b94c-0becb0c10281 | -3.73452 | -54.64359 | 2026-09-19 07:24:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2d3e012c-332c-32ac-82f7-3adf775e5879 | -4.50862 | -54.96409 | 2026-09-19 07:24:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d928b46-ff32-3974-bb6c-93c68ae86d12 | -2.82187 | -50.44903 | 2026-09-19 07:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d279ccd4-2636-34d1-b73c-5946c1f10cc2 | -11.94549 | -50.11797 | 2026-09-19 07:24:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| b6fb0ec6-3afa-3161-a562-0da17b7ff539 | -4.48778 | -55.48368 | 2026-09-19 07:24:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| d0a25fdf-dbff-37f4-9ce9-8b2b730fe48a | -10.70344 | -60.72788 | 2026-09-19 07:24:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| d45a6242-5f12-3e8a-9736-6c8d8180988d | -6.1309 | -59.93652 | 2026-09-19 07:24:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 75a0c22d-b016-3902-a60a-cc6494dd5bf8 | -3.69152 | -60.60767 | 2026-09-19 07:24:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2ca199ad-45e8-3d60-ae3c-538ea0bad62d | -3.33806 | -59.80997 | 2026-09-19 07:24:00 | AQUA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 87606587-4812-3dd5-b898-c26ce1d972d7 | -10.86839 | -56.18877 | 2026-09-19 07:24:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eed4722d-b642-33e9-9b92-71a328bb45c0 | -7.57622 | -57.68267 | 2026-09-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0ae12415-8043-3d90-8408-de0ecce776d0 | -4.48645 | -55.4926 | 2026-09-19 07:24:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 82a87b79-16ab-32d5-b396-4229d4c835f8 | -10.86426 | -54.10517 | 2026-09-19 07:24:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 63da0640-b71e-3632-8a65-529b50613db4 | -3.36028 | -50.45896 | 2026-09-19 07:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 81e6665a-378e-34e4-9f39-5b7a4049bb04 | -10.70526 | -60.71679 | 2026-09-19 07:24:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8319130e-c6dd-3e7d-9ed2-04d61822f8ce | -7.57485 | -57.69156 | 2026-09-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4089a901-ac9c-376f-ac87-d023b43b59c1 | -10.69949 | -60.73301 | 2026-09-19 07:24:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4277cb46-9513-34f5-847a-88188692e098 | -8.4992 | -57.624 | 2026-09-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 08ffa6e8-3401-3713-a8c5-e4cacdb7df11 | -10.68972 | -60.73145 | 2026-09-19 07:24:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ece43925-40de-3b20-8255-397912b159e2 | -3.68826 | -60.60151 | 2026-09-19 07:24:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 16377244-0684-383b-b979-83d6db6056d5 | -3.72549 | -54.64226 | 2026-09-19 07:24:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a2e6b79-7a63-3e0b-a9a8-79e21ee8980a | -2.81935 | -50.46587 | 2026-09-19 07:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 280f32f2-0fc0-37df-a3ad-8906724dc7be | -10.99995 | -48.32071 | 2026-09-19 07:24:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| d5e2fd86-62c6-3787-a9f1-02d70390e25c | -8.78314 | -48.68562 | 2026-09-19 07:24:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d9bbb2c9-4dd0-3667-9d0a-d8c088d197d8 | -3.36283 | -50.44167 | 2026-09-19 07:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ca362e53-6a64-3d9a-808a-e9192e106931 | -8.27477 | -62.73222 | 2026-09-19 07:24:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ad41f16d-d76d-3cff-95b0-1aa8389dcb7d | -7.55725 | -61.32325 | 2026-09-19 07:24:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7fa1343d-864d-334c-86b8-1433ebc8a7a1 | -12.3355 | -50.71542 | 2026-09-19 07:24:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 465e98c7-fbb2-3b2a-9a3c-ef4ba992ecab | -4.87992 | -56.06818 | 2026-09-19 07:24:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a69b9edd-65ee-3b27-87df-42de4120eb41 | -8.60715 | -54.58648 | 2026-09-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e410f30c-8558-3911-b805-d0ba921a1f62 | -2.8465 | -57.63467 | 2026-09-19 07:24:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cc15a785-2232-3bbc-a8f6-ffd2eb585ad6 | -10.70125 | -60.72186 | 2026-09-19 07:24:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 4d116b08-ad78-3c33-9e63-2d2556c9e8d0 | -2.82856 | -50.45537 | 2026-09-19 07:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6d5be4a5-00cc-3f1e-982d-8d4dcd8bfb58 | -10.7132 | -60.72948 | 2026-09-19 07:24:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| e2fe081c-029b-3be4-8e01-7a17a0ba6de8 | -2.89403 | -57.81221 | 2026-09-19 07:24:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 202.8 |
| 97e17a99-41a9-3d24-b983-d128f699fede | -2.8878 | -57.79178 | 2026-09-19 07:24:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b96a623d-be12-31ff-b028-e63478023388 | -6.36288 | -58.29081 | 2026-09-19 07:24:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8b3e4a9c-bf9b-35be-a551-e21491083e9c | -10.93764 | -53.9512 | 2026-09-19 07:24:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| badd2cfd-eead-36a2-b658-2ddd09bc2a16 | -10.71501 | -60.7184 | 2026-09-19 07:24:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 280c3970-28a7-393d-8b3d-8cbc4cf48654 | -6.12907 | -59.94801 | 2026-09-19 07:24:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b69e5f0c-ba45-3458-9a9b-55c71d0b3c2f | -12.34305 | -50.72156 | 2026-09-19 07:24:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f140df6c-ed48-31fe-853c-1a6d86b704ab | -11.14401 | -54.01781 | 2026-09-19 07:24:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| af66dba1-5cb7-367d-8ff6-a8040db6d870 | -4.49662 | -55.48496 | 2026-09-19 07:24:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70473368-b0f2-3a59-9ee1-01902baf58c2 | -12.27043 | -49.16532 | 2026-09-19 07:24:00 | AQUA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 5cbeaacf-989a-3670-be3d-5d52c1f24d4d | -10.86591 | -54.09298 | 2026-09-19 07:24:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 53f5916c-bf14-3900-b312-9a34f4a60c9a | -3.75788 | -55.95573 | 2026-09-19 07:24:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6063fb42-4017-3018-b8c3-acd3a801edc5 | -4.4263 | -55.51426 | 2026-09-19 07:24:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ec0b51ab-6dbf-3ba2-b6d6-e65e0c6e309c | -8.42163 | -54.72912 | 2026-09-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 139254f5-6f56-3abd-a460-332ad3046f6f | -4.50726 | -54.97322 | 2026-09-19 07:24:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d902c9c1-5c62-39e0-b24b-a8bebeb144d3 | -11.97888 | -52.45459 | 2026-09-19 07:24:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a270eff2-94a2-3539-8995-e1dcb32f221d | -10.52091 | -56.78904 | 2026-09-19 07:24:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 57b409d1-5d4a-3c16-a125-f89ae843b59b | -10.70873 | -50.25612 | 2026-09-19 07:24:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 9602bc8a-f6bc-32f8-86bc-cee4fdc55f71 | -18.01969 | -51.07166 | 2026-09-19 07:26:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 27c44316-0159-3937-b915-0a7d2d9dbd42 | -18.01545 | -51.09124 | 2026-09-19 07:26:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 78b42f3b-d85b-35ef-b7ad-c1fcd13b9db3 | -18.01848 | -51.06409 | 2026-09-19 07:26:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 90f4d3d6-e4ae-332b-9eb6-8f38d392c4e2 | -18.03436 | -50.9308 | 2026-09-19 07:26:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 9206a87b-f3ed-3b9e-897e-995bf666db76 | -10.7115 | -60.7312 | 2026-09-19 07:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| cde92080-ed1b-3fcd-bb19-028417535526 | -10.7115 | -60.7312 | 2026-09-19 07:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9400ba8b-64c3-3518-be9b-62f2b14066fa | -10.7115 | -60.7312 | 2026-09-19 07:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f21b34f5-551c-3eb7-a632-fe0cc58a97df | -10.7115 | -60.7312 | 2026-09-19 08:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c292e8b2-063c-3121-97fa-fc8731a0bf3f | -12.2692 | -49.1689 | 2026-09-19 08:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1671d9cb-6181-37c2-b700-fbfd29ef4400 | -10.7115 | -60.7312 | 2026-09-19 08:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 90851a1f-d2be-37d8-9d00-d1d56831c6d4 | -10.6928 | -60.7322 | 2026-09-19 08:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 501a084c-f587-3fac-b42a-3a8e140ec5c1 | -9.0358 | -48.727 | 2026-09-19 08:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 58.1 |
| cbfe3901-2077-3ef2-a027-e3385621f67a | -12.2692 | -49.1689 | 2026-09-19 08:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 8473e775-87e5-3047-ad0a-ca4133344e90 | -8.7731 | -48.6868 | 2026-09-19 08:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a4270e4b-41d0-3be1-a317-90bfe2150834 | -12.2692 | -49.1689 | 2026-09-19 08:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 2f89a865-6b27-315c-98a2-bbace71985d9 | -8.7919 | -48.6851 | 2026-09-19 08:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a822f126-91ca-342e-b9f2-9d67aff7d608 | -10.7115 | -60.7312 | 2026-09-19 08:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ef38aaba-dfcf-3594-9719-aedb45562edf | -10.7115 | -60.7312 | 2026-09-19 08:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |


[Clique aqui para ver as próximas entradas](README101.md)
