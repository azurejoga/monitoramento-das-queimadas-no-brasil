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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9a1fc54-b8dd-3986-a83f-7531e159c39a | -13.3247 | -51.3211 | 2026-09-13 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 9963a646-14d4-3142-b261-39146371b902 | -13.4507 | -48.48 | 2026-09-13 15:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e594b757-528c-3993-81d0-859ba8478ce0 | -10.8223 | -50.5879 | 2026-09-13 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| db1d902c-223a-3709-8348-61e14936ae6d | -10.7535 | -46.2347 | 2026-09-13 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 95e0ba34-1473-3a74-8fa2-53b7b5e0fe10 | -7.2091 | -45.9167 | 2026-09-13 15:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| e4c52efe-983e-320b-a275-b1ef0f867877 | -9.3768 | -50.0712 | 2026-09-13 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 5438f5e0-b6ec-3fd5-b5bf-3547b3638e9a | -3.4058 | -59.2347 | 2026-09-13 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3716ce6b-6d6a-35c6-bb56-45715af29551 | -1.2268 | -49.1899 | 2026-09-13 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b3f02e2f-ec6a-3418-8290-a620926eeeee | -5.2723 | -56.0483 | 2026-09-13 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 4b7dc429-6f8d-32ed-8641-65990ea6ccce | -6.0255 | -59.9484 | 2026-09-13 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 914047bf-0286-3c1f-9186-a092e907df22 | -8.0586 | -45.5451 | 2026-09-13 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c6ae4a29-688d-34cb-8432-967f6afe491c | -7.8715 | -54.7016 | 2026-09-13 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 7c472ae2-ca5e-33d0-950f-dd97e196ab96 | -8.0583 | -45.5678 | 2026-09-13 15:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 2cadeb94-406d-30d9-a510-ed76b2d85a5f | -8.131 | -54.8061 | 2026-09-13 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a5c80605-1923-3659-b7be-54ccbe967974 | -7.1903 | -45.9183 | 2026-09-13 15:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 86a00580-c770-36a7-8387-a405d48998be | -9.3763 | -50.1139 | 2026-09-13 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| da82ae28-f0f0-375c-8cbc-4a958f1d2c00 | -11.4905 | -50.2581 | 2026-09-13 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 2ea9f38a-11d0-3cf7-bff4-5396b6edfdb3 | -3.1697 | -58.6437 | 2026-09-13 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| fc28ab7c-0850-3ed8-a130-c8ff8190718f | -2.6602 | -57.5313 | 2026-09-13 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 37b957ff-2c65-36e8-a381-47aa6eb58d0a | -7.5394 | -44.9133 | 2026-09-13 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| d916160a-ca99-3077-948c-42aa6c7faf54 | -6.0256 | -59.9293 | 2026-09-13 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 97e353e0-f301-3818-9745-fa900251c443 | -6.9474 | -59.7607 | 2026-09-13 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 455c6587-8508-301c-a1ae-176edd7944ec | -3.5893 | -59.0773 | 2026-09-13 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 8bce4b14-eaa3-3371-b0a2-8cfa0c774126 | -3.1514 | -58.644 | 2026-09-13 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b94da8d6-804d-31f4-9006-a2181c3516f8 | -6.0314 | -52.736 | 2026-09-13 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 30340fa7-358c-3ee1-b0b6-a7eca087823c | 1.0951 | -50.957 | 2026-09-13 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 27d006c8-fa9c-37c2-8a65-2bea44809c85 | -3.8096 | -58.8994 | 2026-09-13 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d26c2d16-12a6-3910-8afb-0088de367eb1 | -6.8445 | -55.581 | 2026-09-13 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 289.5 |
| cbba5b4b-df91-3dbc-9632-715b51843e98 | -3.8461 | -58.9178 | 2026-09-13 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 75794a1b-9420-35b2-af48-17480156d781 | -13.3055 | -51.3235 | 2026-09-13 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| cfa15e72-bcbe-3df9-b432-10e8f3447633 | -7.1009 | -42.1327 | 2026-09-13 15:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| 40ca129e-9478-3ea9-a346-3ae7172f7822 | -4.1223 | -54.0158 | 2026-09-13 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 100d33f6-f47a-36a6-9962-72834f5f67ea | -9.3949 | -57.2975 | 2026-09-13 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b610b23b-6460-3232-8245-a21031696626 | -2.7149 | -57.5886 | 2026-09-13 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 6f00d69b-a606-3e27-a413-1ac6d0c93163 | -7.12 | -42.107 | 2026-09-13 15:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 246.5 |
| 1bd64d74-f3b1-3d24-89e2-953b588f03a5 | -12.6636 | -54.6782 | 2026-09-13 15:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| a6ec239e-3dee-3ea8-b0c7-4d1da5185392 | -3.354 | -58.1961 | 2026-09-13 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 124.8 |
| a0bea987-e570-31a0-9455-98e67f3bc97f | -9.3765 | -50.0925 | 2026-09-13 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| d80ce9b1-4e90-35aa-897a-21eae0780f6c | -6.2243 | -51.6949 | 2026-09-13 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 3952aa8e-9d2b-3fae-95ac-a3eeb87b728a | -7.8713 | -54.7217 | 2026-09-13 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a4cdc256-dbae-385b-8a90-8d02fe845e29 | -3.4058 | -59.2538 | 2026-09-13 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 48b5af43-7126-3a8c-b613-078daaa59c2e | -10.8413 | -50.5859 | 2026-09-13 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 9bf908b4-261a-3810-a173-41a5bb873a87 | -2.6785 | -57.5115 | 2026-09-13 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 38b3f417-1c1a-31e3-bd94-3672b5dcd09f | -1.3007 | -49.1464 | 2026-09-13 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 2bd8df3b-b332-3a8d-9c3b-a8381910dd1c | -2.6602 | -57.5119 | 2026-09-13 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 7baf0ba6-754d-3fa9-bebf-f2fd31081dd0 | -3.3688 | -59.4079 | 2026-09-13 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4988f5b0-f27e-3504-9dbb-a813de010a39 | -2.7149 | -57.608 | 2026-09-13 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 867b9eb4-ab9f-3192-a1ce-429c11c011d7 | 1.0952 | -50.9363 | 2026-09-13 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 325c5921-8cee-3fd7-a05b-a52a03aa3a4c | -6.6334 | -45.4018 | 2026-09-13 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| d07dd717-a096-3a5c-8f99-4e91c2e9295b | -8.9868 | -49.6797 | 2026-09-13 15:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| e047d531-d26d-31be-aac3-d831ca85b96b | -3.6077 | -59.0577 | 2026-09-13 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| e1549f46-e2cd-39dc-b7f5-017e013cf094 | -9.376 | -50.1352 | 2026-09-13 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 550b774f-4fa0-39bc-b014-c72858fdb0a4 | -5.1255 | -55.955 | 2026-09-13 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 229.8 |
| 980758ff-53c5-3107-b99d-8f6d0ef7e079 | -8.6881 | -49.5353 | 2026-09-13 15:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 4eab9537-03f6-30f5-957c-2482fd86df07 | -6.8632 | -55.5601 | 2026-09-13 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| eb4a34ab-746a-39a8-b7a6-fe664b6c364a | -5.2023 | -49.3348 | 2026-09-13 15:30:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 1694ed2b-3b19-30cf-a54b-15eb0111157b | -6.7172 | -50.4733 | 2026-09-13 15:30:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 184b3d2d-f75d-3a99-aa0a-5940a6dbe116 | -10.7018 | -54.1458 | 2026-09-13 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| edf1ca94-9638-33e9-94ce-bcb72fcdc919 | -9.7041 | -54.3303 | 2026-09-13 15:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8f75444f-2cd6-3f62-9a48-377a4ef53726 | -9.4137 | -50.1317 | 2026-09-13 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| fa880a82-e7de-3297-9d37-fcbee291e11d | -6.8632 | -55.5601 | 2026-09-13 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d607bc5d-7f9a-34ab-a737-515ed2b9ddbc | -2.7149 | -57.608 | 2026-09-13 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e186e3dd-6bd3-3564-9467-4540c98c68ce | -3.8461 | -58.9178 | 2026-09-13 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 06a7896b-4c59-300b-b7d6-e6f1e5935324 | -3.3687 | -59.427 | 2026-09-13 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d711e8ab-8af1-3a9a-a8ab-f2b1c646f043 | -10.7018 | -54.1458 | 2026-09-13 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 164.4 |
| 316f8956-c0a2-3f01-b94e-60e9c41df9cf | -1.2268 | -49.1899 | 2026-09-13 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8d58bcf8-2228-3b5b-a855-725dc658b210 | -10.2926 | -45.3161 | 2026-09-13 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 48.8 |
| e5051de9-c71c-39cd-9062-6d453810a141 | -11.4905 | -50.2581 | 2026-09-13 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 8483d351-2d71-314d-9b4f-700f79a1d26e | -7.5394 | -44.9133 | 2026-09-13 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 78037d37-78ed-3dd9-87d1-deac91e07d9f | -12.6636 | -54.6782 | 2026-09-13 15:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f654d727-ec3e-3d54-8488-93a6d78d09f0 | -5.2723 | -56.0483 | 2026-09-13 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 827ed5bd-05a7-31be-b3dc-2016a9b97088 | -3.3688 | -59.4079 | 2026-09-13 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f90c3f32-6d9a-37b0-8c20-390f196cffe2 | -10.6829 | -54.1475 | 2026-09-13 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 366.5 |
| 34ba1e91-2bb3-3644-af47-5852398d9a25 | -9.7041 | -54.3303 | 2026-09-13 15:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 90cc3362-d214-3ac9-b5e9-b501deca5b03 | -3.1697 | -58.6437 | 2026-09-13 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 20f38bf8-7ab3-377a-ba04-d98f5350deeb | -9.3763 | -50.1139 | 2026-09-13 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 8658b288-e94b-3027-a710-ee957bb16edd | -3.4058 | -59.2538 | 2026-09-13 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 9a229e33-19f0-3ebf-9aec-7eb2c71616f0 | -10.5295 | -51.2964 | 2026-09-13 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 93492726-cb79-327a-8197-e641be71c527 | -7.12 | -42.107 | 2026-09-13 15:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 162.1 |
| 5428cef6-d361-34e4-8675-ba5037b5b66b | -2.9723 | -57.214 | 2026-09-13 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a657d7c9-765f-3ce3-ace0-2202245127a6 | 1.0951 | -50.957 | 2026-09-13 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f7c24393-5675-3652-868c-e4812268aa51 | -3.8462 | -58.8985 | 2026-09-13 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a10afc00-fef6-38da-aead-c62a7176234c | -6.3434 | -55.8442 | 2026-09-13 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 400b3100-a7a7-39c9-9512-416c1f6cf4af | -3.5893 | -59.0773 | 2026-09-13 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 203.6 |
| fcb9b692-5398-332d-a915-f01061b8ab1a | -10.5664 | -51.356 | 2026-09-13 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 09ca503e-5af9-3258-ae48-c76b95eba61e | -9.495 | -48.1584 | 2026-09-13 15:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 7bdba60d-8db7-3711-a7d1-b9c350253d1c | -7.8715 | -54.7016 | 2026-09-13 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| c5f6d845-5b9f-3450-9f47-9bb2cccccaa1 | -3.4058 | -59.2347 | 2026-09-13 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 17458b89-4ad8-385a-95e6-824d1ead6cbe | -7.8713 | -54.7217 | 2026-09-13 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 4ecd41b4-e449-3378-87f5-761459291f70 | -8.0583 | -45.5678 | 2026-09-13 15:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| c26c96df-3959-3365-b3df-f48aeaf15673 | -6.863 | -55.5801 | 2026-09-13 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| abb4b966-78be-322a-b6c4-edd0c772d51f | -2.6785 | -57.5115 | 2026-09-13 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 5548764d-4cad-3d23-8dde-77e60663619a | -6.3433 | -55.864 | 2026-09-13 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9f2ac755-1ff1-3d78-82ca-53db77c98e92 | -9.376 | -50.1352 | 2026-09-13 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 79f78239-1063-30d6-ab2e-9257265f0261 | -3.6077 | -59.0577 | 2026-09-13 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| eb0441e7-979a-391d-8ba9-0e75d2f759fe | -3.6076 | -59.0769 | 2026-09-13 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 220.5 |
| 9ac45454-7ebd-34d8-9bcc-f27d616c1c61 | -10.8223 | -50.5879 | 2026-09-13 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 201.5 |
| bfa0cca4-47da-32c9-bbc2-975f38ea3d04 | -2.7149 | -57.5886 | 2026-09-13 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 672a2171-b4a1-35b0-a0d1-1be5804f6094 | -6.8445 | -55.581 | 2026-09-13 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 445d3139-e5e5-3e75-bf88-c6d68c8ee13c | -9.1523 | -49.9853 | 2026-09-13 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |


[Clique aqui para ver as próximas entradas](README70.md)
