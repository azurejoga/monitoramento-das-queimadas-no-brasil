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
| 1b2e6f5c-54d2-38fe-a73d-dd43d61fee50 | -13.98514 | -45.58346 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e5abd23e-012f-33da-854d-5087e9223bd2 | -13.9857 | -45.60202 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c76491bd-0415-3b5a-b07f-7b0d09e8f3ca | -13.98515 | -45.60562 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a5abf3c-4cf5-38f3-a640-3731b82035d7 | -21.23085 | -56.06542 | 2025-03-03 04:23:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac3afb4e-09da-3f1c-a8ff-520aea937baa | -13.9896 | -45.59895 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10e21c0a-0c05-35c9-9c64-bb4c72bac787 | -21.9626 | -45.40295 | 2025-03-03 04:23:00 | NPP-375D | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b744c6df-c1f4-3842-b914-e3bbe81e17dd | -14.4583 | -45.64322 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c081b1e2-0b52-3827-b53b-f0a63deed392 | -13.98625 | -45.57625 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0d9e22c8-f006-36fe-a5fe-89d8c27624c5 | -13.98905 | -45.60256 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dd08418-c05c-3af6-9205-9c0d74111fc7 | -14.13418 | -41.69235 | 2025-03-03 04:23:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d207c36-cb71-3991-8519-f6ad3f98ceb1 | -13.98179 | -45.58292 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbeada95-05a9-3937-883d-8dd3960a24a5 | -15.79976 | -47.99673 | 2025-03-03 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5a2505e-c9b3-34b2-838c-810a86a7714d | -14.00242 | -45.58255 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dea1145f-ea88-3f67-8a98-16f95995a2d4 | -13.98569 | -45.57985 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c30400f5-9e87-3147-af6b-31f8a6c926a7 | -13.95502 | -45.55641 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d08b14a-c807-3152-bbeb-f23391e921c7 | -13.96115 | -45.5611 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ea22d18-ad4c-37b6-95ea-8e06238f0341 | -14.00353 | -45.59751 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 635bd975-f394-3d43-b031-2a2ab1dc0530 | -13.96171 | -45.55749 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95bec2f6-2ae0-3a68-89c5-8475843cc57e | -14.44155 | -45.63002 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9599db5-90f8-383b-9c37-66f4327d99fc | -14.00911 | -45.58363 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cdde524d-5f47-3c86-b044-776c1b736fb7 | -22.91733 | -43.58907 | 2025-03-03 04:23:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8badaaea-0993-3a88-833e-11010b0d6cdc | -13.98737 | -45.59121 | 2025-03-03 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a886129c-55cc-3f41-ab0f-60a448b9f918 | -17.40016 | -46.56008 | 2025-03-03 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f560cf9e-8370-36b9-a636-b8ed9f90fe81 | -23.40551 | -46.5584 | 2025-03-03 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a4308bb5-1465-3d85-95ff-33a607fdc31b | -17.39682 | -46.55952 | 2025-03-03 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0df9dcf-6763-3a90-857f-3c43b2dc0dc4 | -17.39348 | -46.55896 | 2025-03-03 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55b1ccba-0138-370e-8483-3a625d7167a6 | -23.98523 | -48.9173 | 2025-03-03 04:25:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43ca1d59-2f63-3588-9c03-680cb8101f89 | -23.59175 | -47.43896 | 2025-03-03 04:25:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 46de382e-2e7a-3834-9ff8-90d1a7ea2cb5 | -23.5202 | -47.61032 | 2025-03-03 04:25:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 429efd4f-626e-3827-af51-c32947237cae | -27.38024 | -53.93418 | 2025-03-03 04:25:00 | NPP-375D | TRÊS PASSOS | RIO GRANDE DO SUL | Brasil | 4321907 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a9925311-3115-35af-acb5-813f9b796066 | -23.83256 | -46.86208 | 2025-03-03 04:25:00 | NPP-375D | EMBU-GUAÇU | SÃO PAULO | Brasil | 3515103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0c85c339-e61a-3299-a273-fc77baf9390d | -24.18442 | -52.79743 | 2025-03-03 04:25:00 | NPP-375D | JANIÓPOLIS | PARANÁ | Brasil | 4112207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8f7119c1-4ded-31f6-ab3d-eb0fcd95adae | -23.33751 | -46.77248 | 2025-03-03 04:25:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1e7aab2a-d665-3b63-b527-8066e881d5c7 | -27.38018 | -53.93252 | 2025-03-03 04:25:00 | NPP-375D | TRÊS PASSOS | RIO GRANDE DO SUL | Brasil | 4321907 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 890b52ad-1560-3488-8c55-67cf37f5426a | -28.58534 | -49.44086 | 2025-03-03 04:25:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f70fded1-7555-34c4-8895-95b0fdf70f72 | -23.44324 | -47.02483 | 2025-03-03 04:25:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5154f1ed-2434-3a9e-9a2d-24ab71531659 | -27.83841 | -50.32722 | 2025-03-03 04:25:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8afd5854-ec21-3ee8-bfe5-17401e9d2440 | -23.4061 | -46.55422 | 2025-03-03 04:25:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b4b14f1c-2a1b-3631-8e08-2ec61bbff237 | -17.3996 | -46.56373 | 2025-03-03 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 020109e5-dc8e-3154-9814-c26361a9b83a | -25.56758 | -49.36652 | 2025-03-03 04:25:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 251d53dc-11f8-37a9-a6ec-28e1d32fbb93 | -30.43119 | -53.51086 | 2025-03-03 04:27:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 6481461c-cee0-3d49-af89-26fb2ce3b432 | 1.76609 | -60.22638 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a06d3063-8cf3-3152-b4c0-d28e170161f3 | 2.39733 | -60.0029 | 2025-03-03 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cde0dd50-f9b8-380b-ab17-1c6568986f49 | 1.94132 | -60.39048 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 98bb7d98-2c76-3e9b-bbb4-b2fe6d13f099 | 0.61867 | -59.86556 | 2025-03-03 04:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94d28c36-369d-3406-8d24-e0e3493377c1 | 0.82849 | -59.9496 | 2025-03-03 04:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d5605fa-f874-36b7-8428-d78d7a559046 | 0.96454 | -60.23283 | 2025-03-03 04:42:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31753833-c8b5-3b2b-b1d4-c804c2dd2959 | 2.02105 | -61.43713 | 2025-03-03 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3494b472-1e51-36e0-a773-c8dc55d0e09b | 2.01067 | -60.5611 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cded689-9386-35f9-97ee-3c83697b6e5a | 1.77147 | -60.22098 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4585251-512e-3ab8-bb23-37f3bc642732 | 1.94191 | -60.39427 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ca25f04a-a2fc-3cd7-a4af-37a3a753a9ed | 0.82744 | -59.95041 | 2025-03-03 04:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4205b9e3-dd3c-3650-9136-6cef6f6a7783 | 2.01378 | -61.4333 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cb2a9b1b-ddd4-390c-8418-34a5790e8dbb | 0.83331 | -59.94945 | 2025-03-03 04:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f3f2dfd-573c-3719-860e-6903eadaa657 | 1.94262 | -60.39893 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5345e18e-a462-378b-af9b-76796f30f08a | 1.7654 | -60.22179 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b66018-2a2a-3c0f-827b-0faaae8eb68e | 0.82243 | -59.27256 | 2025-03-03 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f5c03d4-d204-317a-9670-2d758d70a4fd | 2.02684 | -61.43097 | 2025-03-03 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c02b2a6-058e-3a59-8ff3-14f06923ab4b | 1.76678 | -60.23096 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bfeb43d-f595-3bb5-8394-2a1df9c4f227 | 2.40268 | -59.99749 | 2025-03-03 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e114276-f10e-3b2d-8889-d91fa6ee5a68 | 2.02075 | -61.42765 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fc1b60a-bb08-3b67-a12b-1354c4c662a8 | 0.96216 | -60.23306 | 2025-03-03 04:42:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7582273-e257-3a3b-84f9-d6e1d9c870f6 | 1.77216 | -60.22554 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0869bf3e-f665-3fb7-be4b-38e499392949 | 2.01954 | -61.42697 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 28965376-afcd-3b08-bee3-3aaed68d91f9 | 1.90711 | -60.45508 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f940b00-adb6-3094-b43f-ddcb65380069 | 1.00408 | -59.43426 | 2025-03-03 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36d6964f-0320-3353-a040-92eb0485215f | 2.02806 | -61.43161 | 2025-03-03 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a4b6d42-a3d8-3045-a011-25c5417d5d83 | 0.99839 | -59.43521 | 2025-03-03 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e07ad5d0-9e63-3ee7-a111-277f776e2ec8 | 2.01501 | -61.4339 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3a6b7fb1-818f-3fff-ac3d-a7930f78a431 | 0.61931 | -59.86972 | 2025-03-03 04:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 410bda66-bbdb-3572-b61e-960847682efa | 1.90132 | -60.57566 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73fe8d30-f959-3bc8-8b5c-a4d76b36d9ef | 2.00444 | -60.56197 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27681820-e88a-3f91-af61-b99553c26b51 | 0.82183 | -59.26877 | 2025-03-03 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b815790-8fbc-3288-a536-3c3270b9e1d9 | 2.00582 | -60.5625 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffceebda-1da0-3b0a-b569-d5bdd22b5fdf | 0.96527 | -60.23769 | 2025-03-03 04:42:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41266992-b781-30e8-bcf5-d81da902a168 | 0.96291 | -60.23786 | 2025-03-03 04:42:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c1b3c81-1928-3867-a390-4cf5ce523d04 | 0.96527 | -60.53132 | 2025-03-03 04:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c35b57ca-6d94-38d4-a45c-5a77c04e13ba | 0.82575 | -59.27119 | 2025-03-03 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75287cfc-bbd8-3d8b-830d-1861bafb0ec2 | 2.01422 | -61.42879 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9970599e-39eb-3e6b-b62c-a98e60ec964e | 0.96141 | -60.22834 | 2025-03-03 04:42:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 532f8757-18bc-3102-9095-bd463bf7d3c1 | 0.82013 | -59.27206 | 2025-03-03 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a28028a-dab1-37bc-9706-f409f324488b | 2.02031 | -61.43214 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a104a2d-e736-3eb9-81cb-76950172da65 | 0.69907 | -59.77029 | 2025-03-03 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b747975-bbfb-34d8-a875-0ef430446155 | 2.02154 | -61.43276 | 2025-03-03 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e16e6229-6fd7-3771-b503-5357060f3d65 | 0.83435 | -59.94867 | 2025-03-03 04:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4004da3-b89f-3f95-84ab-19bde3c0f477 | 1.77285 | -60.23009 | 2025-03-03 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc28df51-e56a-3341-a91e-2a2e2f82fd44 | 1.02497 | -59.53204 | 2025-03-03 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf16a122-467a-3519-8ca8-3e60bc77a153 | 1.90783 | -60.45987 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ac0dd6c-bd03-3bca-993e-7f1435cf8fe1 | 2.00508 | -60.55772 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a673623a-99fa-37bb-beb7-5f3696167e83 | 1.936 | -60.39671 | 2025-03-03 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aa3c9fd-0af2-35f2-b87a-930778bfbaa2 | -7.25577 | -45.36877 | 2025-03-03 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3c42103-bfe7-3572-b38b-2d471ce7798c | -5.23778 | -56.06231 | 2025-03-03 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a48e32ee-fb5d-3726-a27c-754e34d77d9f | -10.50155 | -42.39902 | 2025-03-03 04:44:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3d119af0-c8b3-3a7c-ab3d-b6cc36a7cb59 | -10.50701 | -42.39975 | 2025-03-03 04:44:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a218e17f-6c52-3d9c-8e9d-2f62700b707c | -14.00342 | -45.59901 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1fd7857-afb8-3ba6-adf1-8209049438cf | -13.9822 | -45.58124 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1430b330-6cd3-35f1-be6c-eb8aa2a25aa4 | -13.98371 | -45.60624 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 377250e5-2ddc-3944-8eab-a53669166697 | -13.95754 | -45.5529 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b11d9052-7117-339f-bb17-130577d55913 | -14.00657 | -45.5745 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 30094be3-ff2a-307e-89d5-11e4e779a512 | -14.00258 | -45.56897 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README4.md)
