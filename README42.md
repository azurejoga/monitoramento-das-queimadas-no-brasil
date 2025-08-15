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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3eda153-2cac-3c35-9c73-228470518558 | -9.16932 | -59.66726 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eefd8972-5ef9-3376-ac67-22d1e1199380 | -11.93983 | -58.76318 | 2025-08-15 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffd080ee-0a28-311e-b1e9-036295291965 | -7.86799 | -61.81294 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60e5f030-d578-37b9-aa36-b6131414f063 | -7.45252 | -60.40674 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c48c1b2-5c86-3f3f-9cab-48542415f9cf | -9.49914 | -60.52349 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 26a62d95-880d-301d-8808-f2faceea5751 | -7.24384 | -57.67546 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfd603c3-00e7-3dc3-98ec-f204dcd35b41 | -6.93505 | -59.63521 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccc96ead-88b8-3fa7-820f-016cfdb19d57 | -9.18382 | -59.68747 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f27aebe-3d71-31fa-8b61-4ac67220c9ec | -12.76489 | -44.41475 | 2025-08-15 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 33ccd2da-5a99-3c2c-b984-0d5cee47a578 | -6.92813 | -59.53953 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 73dd425e-c65b-3a7c-9327-2999dced9a21 | -7.13269 | -60.12769 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f47ad8e6-e0cc-3938-986e-24b559640531 | -7.94325 | -61.74981 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7333424a-a6db-3a38-8594-031bb27ce2ce | -10.35624 | -64.45035 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81bad45b-cf4b-3547-98b4-26d10dd72772 | -6.93663 | -59.81924 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89894da0-b36a-3d55-86c0-b73e59670b3f | -9.15968 | -59.69645 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2724f318-ed7d-3579-8269-5182fc28f9a7 | -7.07869 | -59.24039 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad8ff5b0-eb89-3aa3-bd6b-1238e8c335ab | -10.00373 | -59.21827 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc2306e5-c7e3-35a4-b4fa-270111e98dcd | -7.29584 | -60.63106 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d58ba97-848c-3692-a4cd-2d218712bf08 | -6.93583 | -59.63061 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ded24632-eafb-3532-a19a-ad6b21b87291 | -9.19266 | -45.32899 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 66d16591-d35b-3100-96f2-91da589d6849 | -9.39087 | -60.54339 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5de93821-2b24-395d-b94a-97d9bd8c7f51 | -9.05978 | -60.65252 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d96a4ef-1662-3aac-9b87-fdac5fd80ec4 | -7.33228 | -60.61567 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 719a6049-676c-3961-9c0d-89f478a16e4f | -7.0692 | -59.21665 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6748f5d4-e894-33cf-9f37-72412fa01c54 | -13.32684 | -45.229 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 631dace4-5d6f-3604-b7ce-28718da8e87b | -6.65752 | -58.81656 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 524a230b-fd59-3e38-b197-09ede7fb0864 | -11.3548 | -55.42664 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f073fc7-5897-3e5d-b56e-4624724ef12a | -7.87248 | -61.80909 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a19fde37-d038-38d6-976a-871437ea092b | -7.24557 | -57.66513 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c45af6dd-28fa-383b-b7f2-9e492017316c | -7.07218 | -59.19936 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4f31966-3cd7-3ea9-8573-5a227c80cd20 | -7.42372 | -60.02794 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85c7972a-f60b-3fb6-b61d-177691849ffc | -6.88133 | -59.15313 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c13a5cce-3132-3c41-9109-1c82b789dcc5 | -9.90131 | -60.43491 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4023bf44-1faa-365a-86d6-9341f7a17ff3 | -10.96418 | -49.56741 | 2025-08-15 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab1a9ba8-5f16-30ec-b4ea-440d966d6562 | -9.15338 | -59.6555 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42e4f6a5-194f-3a25-aff5-69d547d41215 | -9.5101 | -60.53646 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 784669e5-0ac5-3d6f-a90c-4b37540b273b | -7.95646 | -61.76497 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 504fc7d0-28c3-3450-b62b-723ff0ce9657 | -14.23893 | -44.58833 | 2025-08-15 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28a7af77-a2a6-3cdd-b9c8-9d454de5faa8 | -9.03455 | -40.5243 | 2025-08-15 04:51:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 559720f8-21b3-37c4-bf02-c6ae9979316c | -6.96021 | -60.12373 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc1f49cc-7da8-3ba2-a980-4b4fc9ce0101 | -8.30719 | -45.01705 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 879cdd3b-755f-3d57-9d86-c6e658ec9d51 | -7.53907 | -63.48766 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 026ca81b-2f92-3ff0-9547-e2a60e1a1c91 | -9.1737 | -59.66801 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2c602b2-c914-3333-89e3-dc723d1fb88c | -8.67054 | -62.4475 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c45a1be-3ef2-33e7-9097-28193ecf938d | -6.48019 | -62.93561 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| be106c87-de54-3d60-bd2b-83567ce23bc7 | -7.32657 | -60.62545 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7b742e3-0036-34be-b5ad-e22842b9a488 | -9.15186 | -59.66412 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bacebc4-1f43-3ae3-97f0-9247053dd2ca | -6.89591 | -59.14697 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bab29f9-3bda-3cba-a28d-9e6267a34924 | -7.08164 | -59.22314 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84f8dc35-7c7f-35df-8bc0-08b730f6371e | -13.31551 | -45.2342 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee22980a-0c4c-332f-8e3a-d8887deff2d4 | -14.07065 | -46.32345 | 2025-08-15 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6604a32d-157e-3545-bf78-d6ce2df141d6 | -8.60297 | -62.66384 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 241eb781-4f30-3cca-a168-30a9525bf2c6 | -6.94715 | -60.00421 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9e08002e-dfa7-3373-b2b3-a5564581cabd | -8.10434 | -61.18863 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6239b694-f9cc-35f9-81ea-fa5efcbadbaf | -11.92832 | -63.24516 | 2025-08-15 04:51:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70e7f6a4-f1f8-3221-ac55-069478cd2035 | -10.09746 | -59.65577 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fbd006e-250f-319d-8445-e5de2ac4b717 | -7.12888 | -60.12198 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53d51c65-7770-31c8-b4f8-a75a692005f2 | -8.55506 | -63.91423 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fc7a1e4-54fc-3ef2-ae6d-5f805366b576 | -6.90977 | -59.14501 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21870145-800f-3d0f-91e0-80b199196ec7 | -7.09042 | -59.22469 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ffb17c0-e350-3c07-9d70-0b12adf39501 | -9.15622 | -59.66491 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2b025b0-d128-37e3-8606-13162b12b974 | -6.66975 | -58.82285 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbba8057-ca23-358c-bd0a-ab3d757a0dc4 | -14.02056 | -52.03642 | 2025-08-15 04:51:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eac3f27f-0f75-3c72-a32f-2d4f25b6f229 | -9.51123 | -60.53584 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b4ad5bf-c38e-397f-a46f-37b8062913ae | -13.05223 | -56.84203 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7e830d8-b169-359d-ac8f-00a89c381fa6 | -10.33197 | -64.44993 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd71cba1-2687-364c-a823-d122625397b1 | -9.5018 | -60.52985 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3b19ab35-6ea6-3808-ac74-871d91b13350 | -13.11691 | -46.85106 | 2025-08-15 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebd4693b-e718-342f-8749-5de6d622c51f | -7.46159 | -59.88835 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdffbe09-fee9-3dd4-9295-d23b07d58e86 | -6.66115 | -58.82135 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2c73d7c9-4a25-3b7a-8362-5c7a9357563e | -7.5262 | -61.37837 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b5a3b2d-3e8b-3bcf-90f6-7424eba5ef31 | -8.11313 | -61.20297 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7dd02355-455b-3e68-9429-79fb37f27413 | -7.60473 | -63.52116 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ee05f19-34df-33be-b9f7-5ba95088a92a | -6.89885 | -59.15625 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 133205bb-b3c9-31ca-872b-05a5451d8d84 | -11.9251 | -43.44262 | 2025-08-15 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3710f4ab-a32e-3090-aed4-3c3d966b15fc | -7.39392 | -60.00792 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41fa713a-b5f8-30b5-81bf-0fa5f14f66bd | -9.5055 | -60.5356 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| ac7c0bc8-41cf-3887-b9e1-7800d8dfbb13 | -7.60198 | -63.50358 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 99d230e6-cb68-335e-8ac6-8fbfd31efae9 | -9.20499 | -59.66936 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d19c30c-6da0-3e24-85fd-8c77e8e11eea | -7.30639 | -60.62743 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 171071ed-defa-3c0c-9933-5b7f96bdcff6 | -6.9358 | -59.82397 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5b39b3d-2383-3b0d-a028-25f20a3b1101 | -6.70314 | -58.848 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e88151d-1077-31d6-9a95-f414825054ad | -9.4995 | -60.54857 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 61437e06-f727-3b99-bd8c-d2ca4a6eba66 | -9.38778 | -60.5401 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8088fef-7835-366c-a333-3d647f6d939a | -13.11146 | -57.16067 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc593e99-b4f8-3bd0-b078-6506621a3072 | -11.20872 | -55.91329 | 2025-08-15 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b41cef35-e249-3f01-aa70-3e4ce60598a6 | -9.38694 | -60.5449 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 02a23655-9f58-3b2d-be89-b2767d586105 | -6.88495 | -59.1319 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cb4a613-bef4-3f1b-889d-1231d82cdd6b | -7.46079 | -59.89306 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9c8277a-8809-3ab7-a6f1-65574e17edb3 | -7.60397 | -63.52526 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9eb60400-dc29-33de-9943-8405d7cdf1f5 | -6.9087 | -59.62576 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75931855-3dd7-357e-bc03-d8e1c974c412 | -14.79013 | -42.72247 | 2025-08-15 04:51:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7d96895-7498-34c3-8c91-ef4c0875d897 | -6.94445 | -60.13131 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7c8a17a-25ee-3e1a-a028-7a35e455c7e6 | -9.20434 | -59.64715 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0bd43929-f2cf-323e-bc20-a17e4a3306a2 | -10.32199 | -63.62183 | 2025-08-15 04:51:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 589eca8d-706b-306e-8974-366d201468e5 | -9.02941 | -59.76781 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e575a1fe-4535-3153-86c6-2dfc3f5655d2 | -7.13128 | -59.64549 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e938d4e2-3858-352b-a122-e5032bfe004c | -10.315 | -63.62829 | 2025-08-15 04:51:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29d4cab4-854f-302e-8b98-f004dbdcdbd9 | -13.1157 | -57.15715 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52218fbb-4f7e-3e03-a19a-6d404a4d7991 | -9.9104 | -60.43657 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README43.md)
