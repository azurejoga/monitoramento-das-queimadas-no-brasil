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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e149007-f6de-3920-8548-f11fd8eb86d8 | -12.85506 | -52.81951 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1518329-377f-315d-a866-8c1b737fef73 | -12.8545 | -52.82304 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c4784b-e407-3314-a762-b7a865966aef | -12.85394 | -52.82658 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee953f02-8b43-331a-8aef-9500e1707ac6 | -12.85175 | -52.81897 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 643f785f-a74d-3657-bfb0-1e9b64f23968 | -12.85119 | -52.8225 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f41ac05c-aa22-39ce-a573-82dfa86dfd24 | -12.84844 | -52.81842 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 263d7234-b732-3840-ba76-b648179a4c2f | -12.84788 | -52.82195 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bafc50b3-1e77-351e-9a77-aa69371f2c6c | -13.28653 | -53.75192 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4023829-f070-37d3-bc24-3e70d95cdf2c | -13.28378 | -53.74771 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c04fe36a-8bf7-3a81-8480-be30777c39af | -13.2822 | -53.73627 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75acdf0c-6ce7-32c0-bc55-bcba809ac1a7 | -13.28161 | -53.73989 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4dc4b05-645c-35f4-9fd8-3adce93d901e | -13.28102 | -53.74352 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12366d90-cae6-3427-a799-3bfc8c1ad979 | -13.28043 | -53.74714 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05313522-74db-3046-9247-fd7590cd93db | -14.79601 | -53.94113 | 2024-10-10 04:46:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f76b7f42-5ff3-3a1a-9be8-9dcae70acb43 | -14.15671 | -53.37269 | 2024-10-10 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d3089c9-f127-3da6-801f-ed4cdd5812ed | -14.15396 | -53.36856 | 2024-10-10 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4779a70c-5584-3abf-8ec5-e08b096e5ca8 | -14.15339 | -53.37213 | 2024-10-10 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13ef2d6a-7492-35cf-952a-f2c020893f68 | -14.1472 | -54.21468 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f246fd26-0358-33df-a9df-1848444b9d27 | -15.34089 | -53.7437 | 2024-10-10 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19ed9965-a003-3100-b5f1-4a1a38aa263b | -15.23983 | -53.75998 | 2024-10-10 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bbf17c6-4e55-3d93-9f36-33850533a36b | -12.34708 | -54.15169 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88a0d9b3-6caa-3d28-b78d-401c44789fdb | -11.60498 | -54.68771 | 2024-10-10 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29bf86c1-3af3-37e5-8f8e-1c9136be13f8 | -11.60432 | -54.69167 | 2024-10-10 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac10c697-18e5-3a1d-be7a-5fcca2d19341 | -11.60365 | -54.69563 | 2024-10-10 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff416172-54c2-3531-929f-91fc7d8b360a | -11.60149 | -54.6871 | 2024-10-10 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50cfa4ec-1df0-3376-b991-5684ec26aba6 | -11.60083 | -54.69105 | 2024-10-10 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88e52051-fed7-366b-a21b-cbc4e563ef2d | -11.59734 | -54.69043 | 2024-10-10 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a204e3e2-43f2-3189-88ff-d124cf4afb22 | -11.40604 | -55.17841 | 2024-10-10 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88a5587c-4ee8-3eb3-9967-a23a568be0d5 | -11.35726 | -55.42112 | 2024-10-10 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8ff164a-dc9c-3742-aab1-debf7c91490b | -11.35653 | -55.4254 | 2024-10-10 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd2fa5a6-9d4b-30a2-826f-294d9a30e301 | -11.35641 | -55.42262 | 2024-10-10 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19eef8fa-01ff-3e07-b204-a245250db708 | -11.3557 | -55.42692 | 2024-10-10 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9fae76a-9257-35a2-8b7c-d9b2db6e8ab1 | -11.32288 | -55.1141 | 2024-10-10 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b247e79e-9a67-3f0f-8d0d-ff785e58ccb0 | -12.67203 | -54.71807 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43d47604-49e9-32e3-b2e2-333da0164997 | -12.6714 | -54.72198 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a9a0a5f-8cc3-362d-a658-e5431f04be05 | -12.67138 | -54.71348 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a8bb001-da55-3aa5-beca-26a4659f6f4e | -12.67073 | -54.71737 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e779a8c9-f0ce-3fbf-8b5c-3ae26f698445 | -12.67008 | -54.72126 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 918d5d92-b3d1-3ab2-a2f6-9ba441b9bbc3 | -12.66985 | -54.70971 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e6e81a4a-d570-3397-a5e0-25d1f8c74da2 | -12.66921 | -54.71359 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5cebd3a0-a8bc-387d-ae1c-87d82aee90a6 | -12.66857 | -54.71749 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 140fb0ec-1c64-3d3a-ac63-109dbc5caff6 | -12.66794 | -54.72139 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b792ecdc-b619-3b62-bec7-430504d13aaa | -12.66702 | -54.70523 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f70144d-7803-3a31-9a88-f1ebacd17284 | -12.66575 | -54.71299 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d83064c-0469-3a67-bcc4-efe65c62f467 | -12.66511 | -54.7169 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1292d13-18e8-3afd-ad0f-d64d487c085a | -12.65509 | -54.69129 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c306a6b7-17cc-37fe-93df-cf21833cecaa | -12.65445 | -54.69514 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54638170-5e40-3d26-b66b-76c57e4426de | -12.60023 | -55.22029 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 70ec3eef-b06b-313f-8326-81acdd990203 | -12.59669 | -55.21968 | 2024-10-10 04:46:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 846dfc2d-9c37-3441-a0de-5bf656fb60c5 | -12.596 | -55.22375 | 2024-10-10 04:46:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a26203b-f3cd-313f-997f-269fe78f63f7 | -12.59316 | -55.21906 | 2024-10-10 04:46:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db1fc51b-2f02-351a-b038-7f45204cf39a | -12.59247 | -55.22311 | 2024-10-10 04:46:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d080f72-13d2-384b-a959-427d39e169c2 | -12.58975 | -55.21928 | 2024-10-10 04:46:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4767e1ca-65b0-37fc-a066-f69979c15e32 | -12.58908 | -55.22335 | 2024-10-10 04:46:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47606a3f-2329-3315-9de2-b2b222a6a585 | -12.43311 | -54.56689 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc759812-17f1-3ed3-9fa7-335be56077ae | -12.43247 | -54.57072 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baed465e-bb7a-3188-8655-176a045f06dd | -12.42966 | -54.56629 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5df2071c-e721-3687-9e1e-1924eacce529 | -12.40833 | -54.56664 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab8f7888-c3a3-3fe3-b793-1919bab31d8d | -12.40768 | -54.5705 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f409047-c193-30be-9326-fb6119ea7b72 | -12.40704 | -54.57436 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2b95377-1a47-36da-9150-64ff674d36c4 | -12.40641 | -54.57821 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 723cd4ba-aecd-3c49-bc60-de5ba931976b | -12.40359 | -54.57378 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58073cab-bc5c-33b7-90dc-6e51d10bbfb1 | -12.40295 | -54.57763 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9d145ce0-4852-3926-84de-a9965be38e2f | -12.88947 | -55.43975 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08e81771-61b6-3050-8050-ca206f2118e1 | -12.88591 | -55.43911 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9da39ef0-a02c-3053-8466-3da53818069a | -12.88165 | -55.44264 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66bab2c9-a18d-39d9-8cf6-04e9d3839aaf | -13.4339 | -54.69408 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87b389e2-f8ea-374a-b208-41c7f68e2594 | -13.43047 | -54.69347 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d793ed6c-ddb8-3840-8cc3-c14c9c27772f | -13.42891 | -54.68147 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9865cb47-4ca6-3d4e-af20-b16b6a263048 | -13.42704 | -54.69287 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e49505b5-469a-3c34-9e4c-74287c214883 | -13.4236 | -54.69227 | 2024-10-10 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45b5ff93-ae69-3a64-9543-e1df922112b1 | -14.57797 | -54.69352 | 2024-10-10 04:46:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 340bcb5b-5cb3-3ad2-875d-69c48daf85f5 | -14.57456 | -54.69294 | 2024-10-10 04:46:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42986cfc-25b2-3163-9346-aa404fe9da59 | -11.89329 | -56.21124 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ebd68d0-9ec0-31dd-8e21-d8db1ce9f629 | -11.89249 | -56.21585 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5c765fe-a00e-31c4-b57a-5866e74efc32 | -11.89114 | -56.20139 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38866483-3588-32d7-9439-49098161d8c6 | -11.89034 | -56.20599 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 172b72f7-03e5-3041-a820-b134a06cae9b | -11.88954 | -56.2106 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c8be6bb-f743-3cf1-a588-4af5bd531e5f | -11.88874 | -56.2152 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fca0644e-d2fb-32cd-b0f0-0f1f5d0c7a7e | -11.35761 | -55.63889 | 2024-10-10 04:46:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1e72a14-67b7-321e-ad44-dddec9e2f7e6 | -11.93425 | -56.97025 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 758a46e2-9eac-3ae9-b8a5-debb3a8d6181 | -11.93122 | -56.96438 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7891a8f4-2e74-3bb4-b5e1-94493d0cb15f | -11.9308 | -56.94344 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c05b17e-bab9-3945-a629-5f5d0967bbfc | -11.92864 | -56.93257 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29c89352-60df-341b-ab03-ea56547ebda5 | -11.92777 | -56.9376 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c26c9ad-042a-3dcb-8564-ec0d46ccb2c6 | -11.92647 | -56.92179 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e4615c1f-bf73-3d00-8d54-467a7976bc71 | -11.92473 | -56.93184 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1f6133c-fc8d-3a32-9eb4-0643764b4e2e | -11.92257 | -56.92104 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1c3455e-64bb-324d-aa9a-90d6948d98f2 | -11.92169 | -56.92608 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c01584e-d935-3183-8631-2762f38b4b01 | -11.91475 | -56.91964 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d923bd2-67ef-349a-ba27-ad1329047828 | -11.91388 | -56.92465 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b09616d-e2f5-3692-a312-d759f8c96efc | -11.91084 | -56.91895 | 2024-10-10 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c7c6eb3-e096-3b85-90bd-2ccacba051c0 | -12.29037 | -57.73389 | 2024-10-10 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef4657c0-1cbc-37fd-a581-3ff6048776aa | -12.28971 | -57.73756 | 2024-10-10 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9cb71b6-d864-3950-b64b-b2a407d97392 | -11.96364 | -57.59778 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2911f6e1-f89f-3c0a-9db0-cecc9f30c713 | -11.96313 | -57.59772 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ae48d15-57d8-3b5a-bc25-8dea9b55c354 | -11.96301 | -57.60149 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efc23a1c-bc48-3c27-bfec-b80251d7c2eb | -11.96246 | -57.60141 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64e0cecf-435e-3fe8-b690-5031afe18b6c | -11.95957 | -57.59707 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae1d549a-9aff-316c-afc7-992ab4c0e519 | -11.95905 | -57.597 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README123.md)
