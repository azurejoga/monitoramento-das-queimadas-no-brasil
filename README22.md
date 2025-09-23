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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddbd25cd-4086-3a2a-9f24-082aceef96f9 | -3.16148 | -60.96608 | 2025-09-23 05:38:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35d9b312-9425-3517-bb23-da009959cde4 | -6.34613 | -56.18887 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b4ca037-e030-3285-b621-cd218ddf7423 | -3.24117 | -58.84976 | 2025-09-23 05:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efc02bc4-c375-3688-9752-4ae01fc7b567 | -6.33985 | -56.19852 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e458187-b4ed-33c8-864c-8d55ce291a77 | -3.52196 | -49.44987 | 2025-09-23 05:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7acb1a6f-3bf5-3b00-a2ee-c63f3542af98 | -6.33505 | -56.19778 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 406ae3ca-0ae5-3c68-ab18-24ccf98f7763 | -4.47975 | -55.58032 | 2025-09-23 05:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60073462-1240-3bfb-a3fc-bb1b237c0abd | -2.52492 | -57.85974 | 2025-09-23 05:38:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b05dfa8-2a8a-3107-a25e-55418f2a7371 | -4.48238 | -55.58178 | 2025-09-23 05:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0390b3b8-83e5-3705-8c6a-6eac83e2a65c | -3.24501 | -58.85035 | 2025-09-23 05:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0908468d-342d-38c4-93da-a0a889181756 | -3.766 | -65.13619 | 2025-09-23 05:38:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 538f319b-5181-3b15-b360-f7bed5861458 | -3.64475 | -51.9052 | 2025-09-23 05:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c6da1b2-dc2c-351e-8eaa-75bb7b6ea83e | -3.36467 | -59.43271 | 2025-09-23 05:38:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1179685b-794d-3874-80df-77685a2e72e5 | -3.51483 | -49.44889 | 2025-09-23 05:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be5a5923-31e7-3ca4-ac55-82339f1561f6 | 0.15717 | -60.67601 | 2025-09-23 05:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b095c305-4836-3c57-802e-e56967398e85 | -6.3487 | -56.20519 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c091503-27bb-3637-9c02-7770e6e98e06 | -2.69395 | -59.42315 | 2025-09-23 05:38:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f894cfe-5ec8-34e9-9605-6aa16ad84bf6 | -3.76255 | -65.13566 | 2025-09-23 05:38:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aac0e552-75d0-3baa-b3c7-89fb3ddd5fbd | 0.15774 | -60.67963 | 2025-09-23 05:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2885afb5-4bb1-32d8-96ba-b266001a5b68 | 0.15831 | -60.68325 | 2025-09-23 05:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfca2ed6-9cfd-38e5-b124-2b13b19e1de0 | -3.90249 | -63.78201 | 2025-09-23 05:38:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c96790b-3f2a-3add-b414-6215d11aec18 | -6.34059 | -56.19334 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a591cd7d-cee1-3795-9c9b-66f3732b8fc1 | -1.12455 | -54.14456 | 2025-09-23 05:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ea3b53c-6687-397b-9aba-9af159b2ce01 | -6.34132 | -56.18816 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aad44680-eedc-38a2-b378-f93e4f6ea9b1 | -3.62616 | -51.91133 | 2025-09-23 05:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2409706d-3e8b-3691-be3f-fb7a388c09ed | -3.35285 | -59.43537 | 2025-09-23 05:38:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1dd71fc-b260-350e-8a3a-561ec86818b7 | -3.62486 | -51.91253 | 2025-09-23 05:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cbac9ce8-a4cf-3eb1-b244-d1aed074594e | -3.36029 | -59.43654 | 2025-09-23 05:38:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42e2b75f-ac33-3221-aeb2-79802ce51477 | -1.08312 | -54.10812 | 2025-09-23 05:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da36dad9-2852-3c1c-aee3-b3e6cd4e9308 | -2.26664 | -57.09111 | 2025-09-23 05:38:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e41bcba5-332b-35a6-b5c8-e1fe9511bb33 | -3.57949 | -58.56673 | 2025-09-23 05:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f8d8b47-cadd-3fb6-8fd3-2b78d4eb2983 | -6.33911 | -56.2037 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b65148ba-2ccf-32e0-a3e8-f86ee125541d | -6.34944 | -56.20003 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7397a709-fe6f-310b-b14e-507cbe92e00f | -6.35018 | -56.19487 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3655b210-d840-3922-beda-7ffdf4a9acb0 | 0.16057 | -60.67548 | 2025-09-23 05:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 491a322d-bf44-37a7-ba2f-2f4a6b7893aa | -6.34464 | -56.1993 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 294986ea-0bac-3dfb-acd0-42d0fa00e325 | -3.63104 | -51.91317 | 2025-09-23 05:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0928ad1c-361b-3294-be50-b597cd54e6b8 | -3.35149 | -59.43663 | 2025-09-23 05:38:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27dbf8ab-e38a-32fc-a5d8-fb0f1b72ae95 | -3.63925 | -51.90786 | 2025-09-23 05:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbb749f1-ea4b-3dad-a8c2-33daaabf677a | -6.34538 | -56.19411 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b860d2f-c5fe-38c7-9f83-386515e71022 | -3.19922 | -54.97945 | 2025-09-23 05:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7628f9ee-273e-34b8-8740-ab20a1b46d13 | -3.6379 | -51.90913 | 2025-09-23 05:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51a124e5-e8a1-3bdc-b21f-f60ee6436a4b | -6.34317 | -56.2096 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 287c29b8-696b-328d-a705-0ef4064139d7 | -3.51382 | -49.45582 | 2025-09-23 05:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0cacec4-2127-3638-8942-5bcb31ac1788 | -6.34391 | -56.20446 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f95e994b-1fc4-3e9f-af43-d1c56e8949bf | 0.16114 | -60.67909 | 2025-09-23 05:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3088845c-78f0-3bbf-8d6d-9611bc19c3a4 | -9.45023 | -67.66871 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0775fdd9-420d-3bff-8cd8-fcbe8277d0a4 | -15.28361 | -59.41918 | 2025-09-23 05:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7e67f28-7e4b-3766-b7ca-bb6117c82803 | -9.94513 | -64.75829 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72904a85-deae-3eb8-a7f3-92f10e1bd2d4 | -9.47462 | -67.13562 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7bd01d2-e175-3359-9668-53553de42951 | -10.81917 | -61.41538 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e3602a3-ce17-3e4a-aeb1-dd0651390053 | -6.42172 | -67.91681 | 2025-09-23 05:40:00 | NPP-375D | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02771b1f-76cb-3f26-9499-b4d377a1a883 | -9.89125 | -64.83951 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afa37a6f-d2ea-334e-933a-628ae2b806ab | -10.81907 | -61.42184 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d378169b-9557-3a48-95cf-dcfea707ab5c | -9.93293 | -64.74912 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7336c617-9ad5-3cdc-86cb-9e3fa5d42a9b | -9.88459 | -64.83844 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d91e94f1-0ea2-3207-92da-9ab1f12c5254 | -9.44781 | -67.14352 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85198e9e-ebe3-3f38-a1fd-ae8003023685 | -8.89378 | -71.28645 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccc44e41-1f8d-34b1-abd3-5ed50384879c | -9.19385 | -67.57185 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a2372eb-793a-3b14-92d6-2c7ff52614ce | -9.88792 | -64.83898 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbab430a-ab8e-32a0-9c26-40e49de150d2 | -8.07248 | -70.33274 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a4363c3-d99f-33de-acfd-74802159661b | -8.69301 | -67.05724 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca344627-d7e8-377a-ac4a-48d05032392c | -8.81013 | -67.07135 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fdfe560-c2fc-3132-9933-aba3aee4e6a6 | -8.20237 | -69.86821 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c62d329e-194a-3f1b-b71c-bac1703cdefa | -15.3632 | -59.18187 | 2025-09-23 05:40:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c458842-4559-3ed3-9b34-ee148b084da7 | -15.35256 | -59.19405 | 2025-09-23 05:40:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af3ca2ca-9a91-3458-9bdd-51118e2e5ffe | -7.9696 | -70.88177 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32d91e61-2fe7-3083-91ea-77facae72c41 | -9.44126 | -68.93159 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5005cb12-8de7-39fc-a38d-f715cf732757 | -15.35199 | -59.19855 | 2025-09-23 05:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f94f2b7c-f0e3-303c-a16b-dff70df5f4c6 | -9.45491 | -67.1447 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de299311-261a-3571-88c4-bf6d9f12ffba | -9.13659 | -68.17805 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa0b87f5-b3a7-35e9-b49b-869dcf78c3a5 | -9.44847 | -67.1395 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05f67935-9e26-3465-a18d-292c93322f6a | -9.49929 | -67.15504 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4facb65-471c-3f63-ab56-b2709645424e | -11.86671 | -56.87586 | 2025-09-23 05:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33fed0bb-84e3-3e56-b1ae-83d62768aa18 | -10.81855 | -61.41968 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2592f156-3fb6-393d-ae66-8670539a1da5 | -14.76899 | -60.22543 | 2025-09-23 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83129331-5d15-366a-b4de-8e95adccd3d1 | -9.11712 | -68.31596 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a67047cf-4a33-3b83-9ae5-3765788b2b9f | -7.56053 | -70.00964 | 2025-09-23 05:40:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf8eec29-16fa-3638-b634-68036bb9fd06 | -9.45202 | -67.1401 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b6f2046-95e8-3af5-9aa2-4335e88e5df3 | -15.35759 | -59.19022 | 2025-09-23 05:40:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bdc0052-6ecf-3ceb-96b1-ae5d7b9c4531 | -10.81972 | -61.41755 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e93e4e1a-029e-3bb0-88c2-a05c4ecb6c4b | -9.91905 | -64.75048 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5b5ebb1-7fa7-3668-99a0-8afa594c0ca2 | -11.92273 | -55.911 | 2025-09-23 05:40:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fded20f-fb43-302b-a31e-826a9db0f0d2 | -11.86682 | -56.87522 | 2025-09-23 05:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 066959ca-126b-33e8-b48f-9bb41fb2b909 | -9.00878 | -69.41366 | 2025-09-23 05:40:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6bacb14d-9585-3ddd-8f6c-0abced14b93b | -9.1655 | -67.5636 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48a13864-c713-3368-b852-e904b6ae874f | -15.35816 | -59.18575 | 2025-09-23 05:40:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ab7e522-5a07-3737-a4df-c90a160fcf0e | -9.10299 | -67.42081 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed0f773c-d53b-3a1e-8620-526e3b292a57 | -9.45846 | -67.14529 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a80995b-1231-3d47-b8f0-331548bd7a9b | -15.35312 | -59.18966 | 2025-09-23 05:40:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efd6bc13-b91f-31c9-a412-6033a935b200 | -9.94621 | -67.22636 | 2025-09-23 05:40:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c1d771f-a4c7-3e0e-9ab9-f4af32330357 | -8.2066 | -69.86894 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecf38a2b-2ffe-3ee9-a64f-40e429b34511 | -6.39087 | -67.9604 | 2025-09-23 05:40:00 | NPP-375D | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b97a289b-54b5-3d32-bc19-bef9d24965ec | -8.78359 | -71.8093 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 826d1a13-5c7e-312a-99a7-3370ac7df541 | -9.65185 | -68.71233 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 990d7563-a9b6-3441-b003-dc1d586e9195 | -11.92231 | -55.91435 | 2025-09-23 05:40:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 963d3e75-ad01-3c07-ba5a-20f498c31ab0 | -10.81979 | -61.41107 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a6b2c81-831e-3468-8d36-657b2728cbc3 | -10.81551 | -61.41485 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 726e2577-227a-342b-8d38-dd56d2ab2286 | -9.94266 | -67.22578 | 2025-09-23 05:40:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2343d96b-a66d-3dae-b77e-bea60eddb28d | -8.74733 | -69.1434 | 2025-09-23 05:40:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
