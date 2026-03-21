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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d335d6c-7dfd-3a33-b71b-ed87f36cbfaa | 2.72833 | -60.4504 | 2026-03-21 05:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f82e3e00-2582-31e1-9beb-89be90f3f62a | 3.32923 | -60.19696 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a367648-96d0-3e18-9859-f3e35d29672a | 3.33287 | -60.19212 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48370f22-1b49-3dce-9c70-f4ef2982d1c0 | 1.97961 | -60.57056 | 2026-03-21 05:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39566269-3abd-31af-81f3-2a83a3c5094a | 3.36538 | -60.1739 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 916cc3bd-0d37-3fa3-ac21-024684d38177 | 3.34083 | -60.18655 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f236160-7e0e-36f3-b3b6-142f34dd07ce | 3.23133 | -60.12604 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0c194698-137f-388a-80e0-e9d7efa450ce | 3.23568 | -60.12535 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0dcb3b07-778d-31c0-bf89-759d8897675a | 3.23983 | -60.31461 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34f655aa-25ba-358c-8dfd-fd81adb0d9f5 | 1.81167 | -60.42205 | 2026-03-21 05:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a47ebb6b-0b5b-38c1-b7b3-61677fcd8700 | 3.10531 | -60.52745 | 2026-03-21 05:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1aeb6e2-7180-32da-9ee2-a3ad3bf567fb | 3.23636 | -60.12956 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 007f255f-0bb4-38cb-928c-00bf606cc17c | 3.33718 | -60.19139 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0fc332b-a982-367e-ba3b-d099b71cbfd9 | 3.36106 | -60.17464 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7aaf6b1-0271-374a-b641-b930c6e45ed6 | 2.59377 | -61.30091 | 2026-03-21 05:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7e8570c-b492-30d9-b4b2-0dbbdb80b136 | 2.12229 | -61.22228 | 2026-03-21 05:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bee58060-36f8-3d00-9dc0-0a20cb6f2693 | 3.33651 | -60.18728 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca6f7bf1-8959-36b9-8b84-320b883753d3 | 3.2359 | -60.3443 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8acd8cdd-5099-313d-a198-2b9eb5918903 | 3.23201 | -60.13025 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6760e16a-1b48-3a27-aa68-d2d3cce064cb | 3.23524 | -60.34026 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9979b285-fc0e-3880-9262-32e12e0dcbb2 | 3.3697 | -60.17318 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 646cc004-f7f8-34be-a6c6-77da6f3b7153 | 2.05419 | -61.81164 | 2026-03-21 05:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d8042c0-ebc0-3827-a0d9-e8d0b2a64b04 | 2.25009 | -60.28554 | 2026-03-21 05:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 953c972d-650b-3a8c-9dc7-96fe1e4c3833 | 2.73261 | -60.4497 | 2026-03-21 05:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 398b1b83-c469-3f3b-9d9a-841b1855fac4 | 1.9955 | -60.5596 | 2026-03-21 05:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53f9fcdb-1378-346c-883d-94aa3a58a78c | 3.20967 | -61.58979 | 2026-03-21 05:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b96edf7-c38b-3a4e-83b2-7fe9c8da9e6d | 2.59432 | -61.30087 | 2026-03-21 05:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8224df3f-e4a9-3441-8c3e-7fff39799816 | 1.91915 | -60.56615 | 2026-03-21 05:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd774367-c647-3efe-ae7b-d18fda5eb57d | 3.3163 | -60.19917 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e5f129e-ac5d-3e6a-901d-5e5dbe2c3a2c | 2.04941 | -61.80715 | 2026-03-21 05:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3825644a-01d3-3351-b87e-fa677dc0c936 | 2.59782 | -61.30023 | 2026-03-21 05:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91593491-fdf9-3673-b1b3-8b54aed8c55c | 2.05814 | -61.81097 | 2026-03-21 05:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28f1f8bf-ef70-3c34-a323-245683f14e6b | 3.31802 | -60.20401 | 2026-03-21 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9451f81a-cb40-3d9a-ab78-6f6bd253dff8 | 3.92562 | -60.94984 | 2026-03-21 06:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6a66c65-cbe2-3318-9e83-93290f880c60 | 3.32956 | -60.20107 | 2026-03-21 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70414593-5e41-3c9f-9f2d-ca6c5a31a7aa | 3.34171 | -60.1931 | 2026-03-21 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f453646-0fd2-3d50-99ac-197e081394fe | 3.91941 | -60.95094 | 2026-03-21 06:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b09e933f-2951-32cd-8839-a12757da342a | 3.32457 | -60.20277 | 2026-03-21 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 631256d9-18c6-3aae-8bd0-6e2f19c33fe3 | 2.0513 | -61.8143 | 2026-03-21 06:25:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd880c86-abff-39c9-aa83-aeed49f5914a | 3.37258 | -60.17591 | 2026-03-21 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 638f9188-75d1-3674-bd95-772d38043176 | 3.32301 | -60.20228 | 2026-03-21 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 349f50ce-940f-352a-b7ef-ae32e25fd470 | 2.59934 | -61.30276 | 2026-03-21 06:25:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 939f3ca3-a4a8-331b-aa11-057ce8cd50ad | 3.33515 | -60.19431 | 2026-03-21 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7ba0a12-c9df-3258-b8be-bef40f8ee880 | 2.05053 | -61.80963 | 2026-03-21 06:25:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79378ad5-bcca-3f78-b3c9-1871737aa995 | 2.05733 | -61.81305 | 2026-03-21 06:25:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9411e537-8e94-3efe-801a-b6ca67461d76 | 3.31646 | -60.2035 | 2026-03-21 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d61418c2-9959-33f0-8b8a-be803a5c13b4 | 2.59314 | -61.30389 | 2026-03-21 06:25:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fd69d1e-2e82-3a4b-9daf-32b8f0f8b26c | 2.05811 | -61.81776 | 2026-03-21 06:25:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b01999ab-8f63-345d-b65e-59b48010b9aa | 3.36601 | -60.17711 | 2026-03-21 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 573e68aa-a771-372a-8a0e-0bbc6e19b436 | 3.23785 | -60.13168 | 2026-03-21 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| deec9398-adbb-3222-a50a-1e81367e6f20 | -10.6905 | -54.30235 | 2026-03-21 06:37:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 790832ac-e643-3943-8688-c4381340e5ca | -11.33311 | -55.2938 | 2026-03-21 06:37:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c2954cdc-898e-3037-b37e-64b0415e8cbc | -11.33502 | -55.28215 | 2026-03-21 06:37:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cd4b8a49-8cb1-369c-9831-776fd2d6d5d9 | -21.95829 | -57.31918 | 2026-03-21 12:32:00 | TERRA_M-T | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c10b3b58-6e1a-30f8-81f7-5a8e0026a242 | -22.98056 | -52.13064 | 2026-03-21 12:32:00 | TERRA_M-T | CRUZEIRO DO SUL | PARANÁ | Brasil | 4106704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| effeb096-a1d0-3b1c-b021-4dba9e347271 | -21.78879 | -57.52528 | 2026-03-21 12:32:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 550fa1e1-0a03-35c5-a966-e8db2c963a0a | -26.93669 | -49.52245 | 2026-03-21 12:32:00 | TERRA_M-T | IBIRAMA | SANTA CATARINA | Brasil | 4206900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| d61af970-f3b9-3a19-a3b1-08e434939e64 | -30.62987 | -52.72964 | 2026-03-21 12:34:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 26.6 |
| 581e1817-f19c-3561-bb02-2a091487ecc7 | -30.62808 | -52.7477 | 2026-03-21 12:34:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 12.3 |
| 4386e5a7-6fb1-3000-a5aa-f49246e59343 | 3.913 | -60.9584 | 2026-03-21 13:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f7c8105f-b7a3-3d9e-a424-5c4113a7f530 | 3.913 | -60.9584 | 2026-03-21 13:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 0bf3d092-5fd8-30bc-adb5-39685a1c0712 | 3.913 | -60.9584 | 2026-03-21 13:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f10aa72b-4bd3-3f03-bada-22bdd825b2a8 | 3.6752 | -60.9821 | 2026-03-21 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bdb20f19-cc51-33ca-96c6-268951e64e57 | 3.4747 | -60.7775 | 2026-03-21 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 99aeb9c8-2bb2-3a10-82b8-3e4fb8203e7e | 3.4747 | -60.7775 | 2026-03-21 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |


