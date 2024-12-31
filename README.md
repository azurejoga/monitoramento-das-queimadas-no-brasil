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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2efa0d8d-3838-311a-9ecd-c8fbdff73fe4 | -4.312 | -40.075199 | 2024-12-31 00:14:00 | METOP-C | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f3877528-c98d-3827-89d5-41394016aa8a | -6.1351 | -39.7976 | 2024-12-31 00:14:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c37ea6da-e320-3e22-8771-4f1be6be6943 | -5.9415 | -39.6759 | 2024-12-31 00:14:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9b999b3f-9dcb-3ee2-80fa-10e172379e4b | -1.5705 | -46.049 | 2024-12-31 00:14:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef55d924-f27e-3bfc-b272-d6f779b906c5 | -5.8535 | -39.081402 | 2024-12-31 00:14:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| dbec0bc0-d618-3e50-8e20-180f9ce27642 | -2.3266 | -45.6157 | 2024-12-31 00:14:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b91b14c8-ad99-3deb-8d70-e607f4e4963b | -4.8939 | -39.916901 | 2024-12-31 00:14:00 | METOP-C | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 17bfae16-a0c9-3d78-844d-fdaa5ef26010 | -10.6394 | -40.214699 | 2024-12-31 00:14:00 | METOP-C | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2e0df42e-5b1f-32c6-8a2d-a49278a44c60 | -6.1234 | -39.792099 | 2024-12-31 00:14:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 69e35438-00c5-31a3-992e-0b067425ec51 | -4.9017 | -41.103901 | 2024-12-31 00:14:00 | METOP-C | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 54a0cdc2-027e-3e64-9257-e1bbbbdd8cfd | -4.9115 | -41.1017 | 2024-12-31 00:14:00 | METOP-C | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bb77a622-5b2a-3d49-a338-97ae36a34ff2 | -5.3843 | -42.934399 | 2024-12-31 00:14:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 6c78c2b0-a0a4-32ff-b11c-4965a9692c3b | -6.3816 | -39.3964 | 2024-12-31 00:14:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ece20bc0-0402-3e92-b495-93f011efca50 | -6.2723 | -41.768799 | 2024-12-31 00:14:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e7b343db-dd03-34c0-8835-ab451ffbf62f | -5.9434 | -39.683899 | 2024-12-31 00:14:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fec3b490-8e22-3765-8bf4-1103d575b375 | -1.5669 | -46.033501 | 2024-12-31 00:14:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 481ce865-82a5-321a-bb81-502e51d51cb9 | -4.914 | -40.7565 | 2024-12-31 00:14:00 | METOP-C | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 261a7031-f310-3890-b38d-6c13634ee5da | -2.5645 | -51.888699 | 2024-12-31 00:14:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a94070fd-a175-3602-aea6-6c895f48d73e | -4.6183 | -38.479099 | 2024-12-31 00:14:00 | METOP-C | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fbfa4fd5-d23c-34ef-9650-a648bbe60f68 | -4.9148 | -41.1161 | 2024-12-31 00:14:00 | METOP-C | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c0997fff-202c-35b3-8bb4-f16818db4e80 | -4.9033 | -41.111099 | 2024-12-31 00:14:00 | METOP-C | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8368fc7c-4f33-359d-9fb5-811acd250e11 | -5.2994 | -43.2854 | 2024-12-31 00:14:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36172565-1011-375b-b1ee-b9f2ffe17800 | -2.3248 | -45.608101 | 2024-12-31 00:14:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2d939a6-4d84-3d22-ba58-9a3169dbcae3 | -5.8515 | -39.072899 | 2024-12-31 00:14:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 65aa0a71-2e79-371c-b477-d3975fbb264e | -1.5157 | -46.486 | 2024-12-31 00:14:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c72e4187-6ea1-3ef8-8ebb-c2c162b23b83 | -5.7207 | -43.234901 | 2024-12-31 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef8eb4a0-837e-3c3c-b4a2-06d9827ed483 | -6.2769 | -43.825401 | 2024-12-31 00:14:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7570f4f4-0b23-38f5-8811-fe6e17ef64d7 | -4.2565 | -39.7052 | 2024-12-31 00:14:00 | METOP-C | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 03d45841-aa76-3487-a2d1-86df76d9f4b5 | -6.9561 | -43.002602 | 2024-12-31 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab8c310f-1e69-3c2c-9361-c406abacfe14 | -9.3699 | -38.934299 | 2024-12-31 00:14:00 | METOP-C | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2b7733e7-0be7-3c69-aaf4-d710dbfb3a4b | -2.8091 | -41.779499 | 2024-12-31 00:14:00 | METOP-C | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 201538aa-1d69-3166-b5ef-5ba6bb2ae08b | -6.2753 | -43.818199 | 2024-12-31 00:14:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ceb078e-e9dc-34f6-9477-f70281a4f1ca | -4.9098 | -41.094501 | 2024-12-31 00:14:00 | METOP-C | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 891484d7-b8c2-3768-a59a-4a7e114e5433 | -5.9099 | -39.497101 | 2024-12-31 00:14:00 | METOP-C | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 98636657-8050-37b1-b2b3-c04cd90a4109 | -4.2546 | -39.696999 | 2024-12-31 00:14:00 | METOP-C | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 09274fe1-a6f9-315a-ac0a-5868d3ef634f | -6.2737 | -43.8111 | 2024-12-31 00:14:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 609d3c5c-fc63-3792-bdaa-a3344ca6a90a | -9.3717 | -38.9422 | 2024-12-31 00:14:00 | METOP-C | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 10123207-b8b1-353e-ad21-b69e612d957f | -7.3578 | -40.039501 | 2024-12-31 00:14:00 | METOP-C | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fb826f0f-3698-3d2c-951a-6de53a2f5dcf | -2.7977 | -41.774601 | 2024-12-31 00:14:00 | METOP-C | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 64d43955-f93d-30c9-951d-9cd13e7c9b97 | -6.1253 | -39.7999 | 2024-12-31 00:14:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a57a9e6c-429c-346b-b0bf-d3c24cb703f0 | -1.5687 | -46.041199 | 2024-12-31 00:14:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c375e7e-f000-36e5-8842-af4a6ef9ff43 | -4.3101 | -40.0672 | 2024-12-31 00:14:00 | METOP-C | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 68fe6f9c-90f6-3701-823a-14d6a1d2001b | -4.9131 | -41.108898 | 2024-12-31 00:14:00 | METOP-C | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2ba2a1dc-f10d-3d6e-ab11-3ce0713d2506 | -6.0866 | -42.668999 | 2024-12-31 00:14:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 70cdfdfe-44fe-3010-9acc-63d069e16c50 | -6.2707 | -41.761902 | 2024-12-31 00:14:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 73ad8a28-8e70-3c2a-9ef7-e351e0ac224c | -10.6377 | -40.2075 | 2024-12-31 00:14:00 | METOP-C | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0f774007-ad9a-390b-86b9-c3e33d098e8d | -4.5262 | -44.236099 | 2024-12-31 00:18:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 768da7ca-43d3-32ee-ab46-e426b92eded2 | -4.5148 | -44.231098 | 2024-12-31 00:18:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0e33cfa-f2d0-3297-9435-518281628cb9 | -3.5479 | -43.560398 | 2024-12-31 00:18:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ed1fe5e-7084-3c2e-8ff7-459702214b36 | -1.6396 | -45.855801 | 2024-12-31 00:18:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 437af7ac-cd61-3065-a1cd-2cb9934cbec2 | -1.6529 | -45.868801 | 2024-12-31 00:18:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a311397-b0b4-3bdf-8801-153636a6af3b | -1.2444 | -46.6059 | 2024-12-31 00:18:00 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8df57f0d-9661-38bd-a5f9-f96ad1beb3c5 | -2.8365 | -40.293701 | 2024-12-31 00:18:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 827b1c1d-bd5d-3b16-b34a-de968f8ea464 | -1.6494 | -45.8536 | 2024-12-31 00:18:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e773e5c-9ffd-3694-b415-29a828357a4e | -4.5164 | -44.238201 | 2024-12-31 00:18:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68b14669-531a-3668-851a-9c6ef34b30ea | -1.6512 | -45.861198 | 2024-12-31 00:18:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51e98330-518b-3f66-8ef9-b424cdcfd362 | -2.4819 | -45.4389 | 2024-12-31 00:18:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 80943cc2-04b8-3505-b16a-2308f9a09c30 | -5.3076 | -44.549301 | 2024-12-31 00:18:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5270442-fb3c-3142-9d76-c7c8f7d64e8e | -3.91 | -40.7421 | 2024-12-31 00:18:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 85e0c254-3c93-3aab-9e3d-5861ef864e40 | -2.8384 | -40.301701 | 2024-12-31 00:18:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9f12e70e-48ba-3d90-b766-a1aa50aac47b | -4.5278 | -44.243198 | 2024-12-31 00:18:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8792730f-8794-3dd8-ae85-b2862cbf6f48 | -3.5495 | -43.567299 | 2024-12-31 00:18:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4ae0350-d265-3169-8742-93d6bc5c774f | -2.4836 | -45.4464 | 2024-12-31 00:18:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a0c1e4e-f9f2-39eb-9c61-f7d2fc5f4f50 | -4.5131 | -44.2239 | 2024-12-31 00:18:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfcd4e38-612c-30c4-8f59-d64e9d8f4b7b | -2.4917 | -45.436699 | 2024-12-31 00:18:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4cda5b5-69bf-3737-8263-ec8046054b0b | -1.6771 | -45.839401 | 2024-12-31 00:18:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28b889f3-0864-37d7-8a22-64b533a1c047 | -2.4934 | -45.444199 | 2024-12-31 00:18:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22c2e757-fba1-3b59-9c4b-f4e22a4ed3b1 | -1.2425 | -46.597698 | 2024-12-31 00:18:00 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 617d2527-f191-36c2-ac8a-52763190d7d1 | -1.6414 | -45.8634 | 2024-12-31 00:18:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5e42749-440a-3818-92a6-7762a3f8520d | -3.7617 | -43.9552 | 2024-12-31 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d1dbb49-4de1-3b63-87df-904a347e4429 | -2.7077 | -45.571301 | 2024-12-31 00:18:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d33042e9-1672-30fb-8e4b-89d25e3fcbb9 | -3.7601 | -43.9482 | 2024-12-31 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12af56d5-cb2a-3202-aea2-21b6615bb235 | -2.706 | -45.563702 | 2024-12-31 00:18:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36b80900-8f92-3950-b345-43cee2178d7d | -3.9117 | -40.749599 | 2024-12-31 00:18:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 098536c0-f0ec-31d2-af2d-a7e6b50f859d | -2.4853 | -45.4538 | 2024-12-31 00:18:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ede5cf5-625d-3fd7-9702-3395d47ae5ec | -4.5246 | -44.229 | 2024-12-31 00:18:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e83f141-5fe1-3345-b801-048c77210819 | -2.0918 | -45.580399 | 2024-12-31 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 035300ad-5ce1-38cf-a3db-9d64afc1f7be | -22.54615 | -48.3791 | 2024-12-31 00:43:00 | TERRA_M-M | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0cd59a92-f71d-3e9c-af61-fa46542c98a0 | -22.11684 | -51.46638 | 2024-12-31 00:43:00 | TERRA_M-M | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.2 |
| a6540cde-900e-3a6b-b6ee-59aa80eb2591 | -1.56916 | -46.03772 | 2024-12-31 00:49:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 016ed0b1-a263-32ab-adad-3627f931e3f0 | -1.86405 | -48.52799 | 2024-12-31 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 519df6fd-6743-3c33-87ec-a2174d8e3b66 | -6.95914 | -43.00602 | 2024-12-31 00:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| e872aa1a-534b-3049-83f2-777bec98ae11 | -3.5568 | -43.55932 | 2024-12-31 00:49:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d5d96618-e60b-3f8e-b951-defd4ec1bc43 | -2.09673 | -45.57993 | 2024-12-31 00:49:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9e831607-f09e-3159-92a4-065dd46ed066 | -2.49192 | -49.39447 | 2024-12-31 00:49:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 30217eff-e41b-332b-9589-92bffa0d52a4 | -4.31205 | -40.07361 | 2024-12-31 00:49:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 1c74dee4-d14d-3b96-a258-0874a7f8ea7a | -2.49747 | -45.44548 | 2024-12-31 00:49:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a79a78a5-8031-3b1d-b647-29a62a3fa323 | -4.52043 | -44.23491 | 2024-12-31 00:49:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3740a74b-2d41-3e2e-8f66-3b3f2ab35d55 | -3.76396 | -43.95137 | 2024-12-31 00:49:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d1aa54b8-bd0f-3469-ab62-aa0f042afe71 | -5.72789 | -43.23653 | 2024-12-31 00:49:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5aa92e8d-5eed-3af6-ba90-f6b68781e3d5 | -6.13222 | -39.79654 | 2024-12-31 00:49:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 19.3 |
| fb6bab0d-e8ee-3b5c-ac26-dd030e2e57c3 | -2.55185 | -44.08784 | 2024-12-31 00:49:00 | TERRA_M-M | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9fd7b1e1-005f-33db-bc30-c8edd5892fc5 | -2.70998 | -45.57293 | 2024-12-31 00:49:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4c791f9c-4e90-3b33-8aad-a6a28964ecae | -1.65659 | -45.86495 | 2024-12-31 00:49:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d80b1d87-8549-30ea-b9b8-647caf9e769b | -4.91435 | -41.11482 | 2024-12-31 00:49:00 | TERRA_M-M | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| c75a53bd-a03b-34c2-ae52-8d6941bb0e00 | -1.68287 | -45.83894 | 2024-12-31 00:49:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e0af5c5d-1cf9-3703-8540-999d9aa30c23 | -1.24598 | -46.59929 | 2024-12-31 00:49:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ffbdc8e-adf3-34b4-aaad-979cf954595c | -2.50084 | -49.39321 | 2024-12-31 00:49:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0dd1f9c0-cb2c-3415-9e1a-ac7987582105 | -3.76596 | -43.96502 | 2024-12-31 00:49:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 96c6918f-7483-33a4-b220-deaac765599c | -2.48753 | -45.4469 | 2024-12-31 00:49:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 30.4 |


[Clique aqui para ver as próximas entradas](README2.md)
