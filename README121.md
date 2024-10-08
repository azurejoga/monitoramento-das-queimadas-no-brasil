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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2279bd6-8219-36f1-8f96-b4e9bc4d9cdc | -7.15863 | -59.35616 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4adbb84f-4096-3099-a909-3396bf2b1226 | -7.15757 | -59.38521 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1562508-957c-3943-b190-92bb300ac9b6 | -7.15527 | -59.35563 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb901c44-6f4e-3167-b633-6a769f2aa353 | -7.15477 | -59.38112 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9308220-64e5-36a2-bf02-6c1a65e32132 | -7.15472 | -59.35919 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0ab33e3-1195-3fcb-96c8-32e8138a1aee | -7.15421 | -59.3847 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9ce8277-6d3c-3dbe-9698-af72c183ec05 | -7.15348 | -59.30034 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a267ada4-3afc-3506-9727-0e8150365008 | -7.15141 | -59.38062 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5909ffc9-82eb-38f6-b08e-178b133284d5 | -7.15012 | -59.29981 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb5d5436-2b28-3f96-90a0-037ef26c3c33 | -7.13948 | -59.30185 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78a82a2e-ce3a-3bd1-bbf3-1c4ea4eef4a3 | -7.13331 | -59.29721 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d662e9c8-3162-307b-b770-ad0813d5fea6 | -7.13276 | -59.3008 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96b42f8c-04a2-3b9e-953b-56cfb4d51d4b | -7.12131 | -59.21809 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6197702-ed73-3e07-a093-0d92f80fd3a3 | -7.11966 | -59.2289 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e41d120-f2b8-3612-935f-e3ff8d8d9237 | -7.08022 | -59.48636 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1c45d50-e5d3-372b-8f44-06e949600ff7 | -7.06753 | -59.52438 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 421ebbfc-6f89-3e0b-a323-29676dda52af | -7.06606 | -59.45122 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69da128f-5269-397e-b6e9-fd98281cfc37 | -7.06551 | -59.45477 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1059677-d95a-3515-8805-9976b253525c | -7.06271 | -59.45069 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09effda5-ef22-3f82-bd91-62e214f7c7d7 | -7.06216 | -59.45425 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adc4c686-5e2c-3b89-b3c6-3e055199e47b | -7.06161 | -59.45779 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7735be30-dbae-36c0-9b76-fd10140c73b5 | -7.05116 | -59.23663 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69a1007c-f712-3e21-8e3b-8ce7411ef222 | -7.03863 | -59.40689 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 715c0a47-8124-32d8-b70a-15619ece434b | -7.03583 | -59.40281 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 893491e1-3012-3995-aba1-27793182401b | -7.03528 | -59.40637 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 409e1d6f-9796-34f4-931e-e4b9052f92b6 | -7.03248 | -59.40229 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c850c11c-630a-323c-8357-8739667d3bd3 | -7.02522 | -59.40481 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a84ba9e-b226-3bd3-8d9e-9f628af4d610 | -7.02467 | -59.40836 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 854466c3-f816-3b96-82f4-00698b7d05b1 | -7.02187 | -59.40429 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fda05f7-b56b-35d1-8858-b698c5420e9e | -7.01797 | -59.40733 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b16ce4a-c61d-3e04-8b53-7d185b70478e | -7.01742 | -59.41088 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be15b0dd-e69f-3600-8ffd-777fdfab4a89 | -7.01627 | -59.39614 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be392cbc-d64d-30ad-b8df-f5b13e9e9f66 | -7.01462 | -59.40681 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc43c574-c308-3739-9cde-17a43d6f3311 | -6.80217 | -59.30892 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56e08097-1fbb-3daf-9bd2-2d1c844f8469 | -6.7347 | -59.6356 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0ef32cc-f2cd-34f4-921b-b8dcf8835c9a | -6.72873 | -59.67424 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d029a76-80d5-314b-9067-713ddbfd368b | -6.72533 | -59.08032 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54fb27dc-fef1-3c9d-9f5d-246a4e7b1c3a | -6.68384 | -59.48347 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2552ec1b-c51f-3fb8-a8c2-efdaac8b04b1 | -6.6805 | -59.48296 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d9a12df-338f-36e5-9c8e-9b41ecc387c4 | -6.67935 | -59.46825 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af0ffc7e-04a7-31b0-a791-7e319237a77f | -6.67881 | -59.47179 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8304ad36-00eb-31be-b420-fa05b870f07d | -6.67771 | -59.47889 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 301313c4-4082-3d2f-a08b-bdf8fade6d76 | -6.67716 | -59.48243 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d95d61cc-4492-3bc6-b971-b3f2ac29f32a | -6.67601 | -59.46775 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf38bf3c-a43b-36db-8951-a356efcc21b1 | -6.67546 | -59.47128 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deb6f15d-bf6c-33d1-99c1-8f8c431e5adf | -7.2033 | -59.61395 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e06f3387-c4b2-3654-ac82-40de6fe1b6c7 | -6.73524 | -59.63208 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f0e37ac-74e8-35bc-b793-92ad754f3b04 | -6.66241 | -59.77522 | 2024-10-08 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 789b6f1a-5032-3191-9669-75f577017576 | -6.65854 | -59.7782 | 2024-10-08 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c3dcf13-468d-31b6-9469-d478361142a1 | -9.2414 | -60.46105 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dd23b91-0df7-3ce4-99ff-da6a61979273 | -9.24135 | -60.43946 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 642909ef-d237-362a-921b-2253a8c3e059 | -9.14364 | -60.65366 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91724558-b0cd-3cc8-85df-a2c9aa6c5a0b | -9.13978 | -60.65663 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9984e488-8c53-3fa3-a8ff-b5efe9e2918a | -9.12203 | -60.39923 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a380aef4-3b2d-313c-9ea2-c373b9a48a2c | -9.00851 | -60.73566 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 05aa3514-61a9-384d-b34d-06a21881c4aa | -9.24195 | -60.45754 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4994b182-37d3-32e5-810f-89e19d07c1d2 | -9.23966 | -60.42841 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 110b4e1e-7eb3-34bd-b665-be84415b7ebe | -9.14696 | -60.65418 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aee6f91b-1a4c-31f2-9e66-2c73a0ee020d | -9.14641 | -60.65767 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aebef3d-1567-3762-8698-743e278ffce5 | -9.12149 | -60.40275 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6d46441-4624-3a08-9a70-f5d78ac287d3 | -9.12094 | -60.40625 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c565045-4a54-3489-93a3-8656d24a0afb | -9.07072 | -60.62072 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8cdf24a-5e73-3257-84a1-ea481e41f0c6 | -9.0482 | -60.45929 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed0d40c5-9492-3726-807b-d897b03c8c2a | -9.02492 | -60.43409 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74d1e962-2a8c-31d0-8ceb-4bc7b28b22b2 | -9.02437 | -60.43759 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecb3ffa5-33ff-3207-a8d2-d27f545bbd13 | -9.02214 | -60.43007 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c19eea3c-28fc-3951-b04a-8940ab45565b | -9.01128 | -60.73966 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 752b500d-fdc4-38ba-ac2a-089ddc207bab | -8.78368 | -60.15209 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4045077-c41e-38c3-9c29-38b23c53f98f | -9.81144 | -60.46414 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66642246-90c4-36fb-9f2f-26d6487ba769 | -9.8086 | -60.43842 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b15ca4cc-5165-39ea-994e-a64e76e76286 | -9.80751 | -60.44548 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 174385b6-0e21-3ae0-bf7c-141fd77213f8 | -9.89188 | -60.42545 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab1c5c37-71a8-3fd9-9acf-b5b32efb53bf | -9.87778 | -60.80143 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c1906b0-2aa4-3938-9f13-204108d52f72 | -9.87447 | -60.80091 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f47ebaf-fea0-33d4-9808-d6ac434b1dbe | -9.85118 | -60.75419 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51aea036-898b-33b6-ab66-eb60add11cf3 | -9.81198 | -60.46062 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 539aaf08-ce11-3704-889a-fecd47cb1337 | -9.81089 | -60.46767 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 213b1c17-5a58-3abc-be7a-7597315b366f | -9.80806 | -60.44196 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37df5d4d-d2a3-3221-8fb1-9829f656c5d8 | -9.80756 | -60.46714 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13404789-830e-3a26-a405-7d4edb69c88b | -10.42589 | -60.98888 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab88f4ef-862d-3df5-82f1-f94acf35c081 | -10.42258 | -60.98834 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13f48d91-4855-3abc-be5b-553fe8f3c24a | -10.42204 | -60.99186 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08674270-d981-3fce-9e20-3c8d4090beee | -10.41928 | -60.98786 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f746281e-a6f8-3fd1-9d6f-95a06927e39e | -10.37982 | -61.17511 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4c32784-a215-3334-bd83-a2c8bb0fc7c6 | -10.37706 | -61.17109 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a0dee67-4027-350e-94be-4be2ca1844be | -10.37652 | -61.17459 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cbc3ba3-1ff7-3843-9b17-d4dfaa20deae | -10.37597 | -61.17807 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 803bba6c-9129-3ce2-a66e-da9a4d210750 | -10.07262 | -61.11905 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78b2c9b5-2a00-3cd2-8938-b1ff61333f3d | -10.06986 | -61.11504 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c1c353f-8774-3b9a-bdcc-ea1c5b813484 | -10.06931 | -61.11853 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cec241ce-cb84-315a-aa3e-b12fd59ec455 | -10.06655 | -61.11451 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39d28e30-7a08-3a93-a5ae-e155d2116b40 | -10.066 | -61.11801 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3b3e143-6395-3d36-a116-db0f2d250c41 | -9.96048 | -59.84232 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c056f5a-e9d3-3166-984c-eea4fc392b2e | -9.95656 | -59.84544 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 648427ed-4b21-3b34-9867-6c4c10606638 | -9.95304 | -59.80022 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad5dde96-e223-32cb-a708-6496d73cce88 | -9.95264 | -59.84856 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78d791b2-d0ad-3db6-b1af-4549af564a23 | -9.94954 | -60.13947 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edd9e602-911f-3320-9d6e-0ac00641cbfe | -9.949 | -60.14305 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6508f817-6d3c-3508-b5b0-8cbca736d279 | -9.92362 | -59.93755 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7c873237-a54c-3114-8017-38600c4ef64f | -9.91005 | -60.17359 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README122.md)
