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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c7fe56d-9286-31e0-b898-e72f1e85446a | -2.78533 | -52.87914 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f50c18e-4226-38ee-99d0-d55523e6c975 | -2.03666 | -52.10003 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8aa3696a-affb-3133-a9c1-afaaf1d8ce4c | -0.36056 | -50.02247 | 2024-11-24 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb193c65-2b7a-3c49-ab2c-388c8f671f5a | -3.251 | -54.21688 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0573b7aa-7e25-321e-9aee-c558157ae445 | -2.85262 | -53.96177 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a498df5-63d6-3102-b59b-96415b95df17 | -2.2683 | -50.46062 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a15d0de9-39c0-313e-8176-58ab6ec721cc | -3.11998 | -53.11022 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 879d5af7-6e7a-3a94-8cc4-6b105aa10b66 | -3.15467 | -54.95844 | 2024-11-24 04:53:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56f7c2e9-0e30-3476-8208-72f23b11a217 | -3.23771 | -54.23401 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b00c3fdb-b58e-3ebf-bd4d-0ec56dfceb33 | -0.75261 | -51.73719 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab7bd407-e804-3571-a8f7-982f2bf5c5ba | -1.25713 | -51.75331 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4ad1c06a-089a-3eb5-b5f9-61bbe4369f8b | -3.06502 | -53.22045 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d80bcdda-c456-3ef2-ad85-a6b3842ad32c | -4.44744 | -50.50686 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| feac5e7b-b721-3385-8074-e7709c496c66 | -0.94645 | -51.65189 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7edc43a4-9437-32f2-91d3-67e69ae133f7 | -4.35429 | -50.90656 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99561203-f090-316f-b759-0898df0c1bbc | -3.054 | -51.33192 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc266a22-84a8-3d90-b2d2-4e4b222604f1 | -2.09104 | -50.38974 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc07ba01-219c-3dc7-b823-5dd145f16c1d | -1.31039 | -51.73693 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21c87615-d869-31b3-9626-8f2e9f6069cf | -1.26543 | -51.76511 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e96ba47a-0081-3cc9-8485-d2a2b87ec862 | -3.25075 | -50.12355 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7fe8ef6-ffb0-3c5e-91ec-a3c3ec39d4b3 | -0.94289 | -51.71802 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c6aed9-0621-3243-99a2-9a0eac4b4499 | -1.69846 | -55.01626 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21d759ab-8667-3f00-aab5-40579ed87361 | -2.45781 | -53.70516 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4a4011f-0b82-33a6-98e2-e2c9452140a2 | -2.57825 | -54.22958 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 089991d1-87bf-39c7-8fe1-011a612588f6 | -5.44886 | -45.50822 | 2024-11-24 04:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97b96c97-309b-355b-be55-450a2be03697 | -1.61248 | -52.59214 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13d5a4ea-529b-32ef-b9cc-0f177b63ec8b | -0.2511 | -51.57068 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e00459d-0569-3289-b632-eec017169853 | -3.96204 | -46.90808 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3e25b0d-c693-3cd0-9d95-a7965fa6bea4 | -2.55676 | -46.55675 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 079a286e-8810-3b96-8242-ac075c9b9f57 | -2.20775 | -48.91456 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eac1041f-5113-3b5e-ba2e-5e18b193b43f | -3.10736 | -53.97042 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88269dfa-d5ea-363a-9101-3d11707833ea | -2.65644 | -46.61375 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f330d06d-68c4-3f79-957a-37045ff65931 | -2.27627 | -46.19983 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4057408-1850-3b34-bf2a-c8cc7113eb44 | -2.5926 | -54.05105 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61515a06-bcd1-3b80-be36-8539aa497473 | -1.21144 | -51.74278 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9b71d50-bb80-343b-9a42-7635a376f6db | -2.19449 | -50.78001 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86c8cbbd-87a1-336b-aac0-c6f68eeb21b9 | -1.9574 | -50.72892 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 932c55c5-6cb5-38cd-8edb-8fb5a60de998 | -3.27012 | -53.82674 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df7353be-f7c2-3e50-89a7-4bfbe3b6139d | -2.76828 | -54.07371 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ef4cce8-b6eb-3b3b-8fa7-63c2ed81fb2e | -3.25834 | -48.89445 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8546bfb8-57c6-3d0f-9caa-e3a714407908 | -3.22293 | -53.92801 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de1fe820-3c84-34b3-924d-b2bca66299b1 | -3.22575 | -53.93223 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a68ef345-bcb9-3f86-b061-84af37e86993 | -3.56374 | -51.64142 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18f1aa98-1d4e-3b94-8829-53539e9ddc32 | -1.31486 | -51.75165 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41f8ea0d-d1c0-3786-bd76-9c89c6ffed0b | -2.26325 | -50.47085 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b5a4316-a347-3097-9133-9da3ddab8993 | -2.13181 | -48.79554 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8d761c6-d56a-379b-98e1-56008013fbc6 | -3.95901 | -47.70673 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7d15544-51a9-3595-9aad-2b906608f471 | -1.13153 | -51.68763 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d536d5fb-5028-3e33-b69a-d580636cf37c | -3.51048 | -53.80084 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5577fb74-44d2-3557-827a-a08b78d52c42 | -2.6374 | -54.28153 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03d45584-c14c-336a-98dd-8da3f009cdde | -0.2861 | -51.503 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bafd6b70-4c21-31e5-975a-150e16e460c1 | -4.11031 | -48.50447 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9f3960e-0e58-3c2c-9c2f-9529a5cd9283 | -3.3246 | -49.89624 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5235a918-40ca-3fec-b37f-c2acb04b64cf | -0.95689 | -51.64999 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cefe00b9-4035-323e-ac81-7c42fafa5310 | -2.80502 | -54.01844 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87069626-e752-3696-91e6-755ec70bd1ae | -2.17245 | -50.1317 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d0063dd-5155-3bd9-905c-e49a71e27d9c | -3.70266 | -47.59633 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1426efc5-d9a6-332e-b720-3f931c378e33 | -2.50099 | -49.10524 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe9ac201-06c5-3a3c-8cbc-e7542b796455 | -1.69912 | -55.0121 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad7de2fb-a172-3ecf-9a07-3fd69adedc6b | -0.7713 | -52.48966 | 2024-11-24 04:53:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8db584c-e8e8-39de-83c4-d9a1f9af5a97 | -2.19949 | -50.54879 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4ef1537-47a7-305e-b5fd-5c92982cca04 | -2.37845 | -49.17363 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5bfa762-9348-30ed-bc21-cceb081b5663 | -2.99719 | -53.73652 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e4e1ac2-b753-3a2e-b02a-4ee86a2ecdd2 | -2.10313 | -46.36848 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99dfe2c9-b2a3-3e7a-b162-f3d1e42764a5 | -0.95742 | -51.64656 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83731cbd-17b3-3d9d-b86e-58dc1c0b43a8 | -3.86188 | -50.05257 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6147911c-1d10-3a29-a1f5-1ad0ea1d6920 | -3.08398 | -54.56062 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1934f28-7f41-3258-aacf-a2e6e519107f | -2.62021 | -54.25554 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afccf24e-a554-338c-8544-f59a6850b556 | -1.73729 | -52.79413 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bffc40d-f557-3ecd-8788-82d6ddbd0a69 | -2.21563 | -49.55325 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7c67599-49c3-345e-b736-674bb84b3065 | -3.84844 | -52.39158 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdbdbb9c-1618-319a-b3fa-1c9cdca44d47 | -2.65128 | -51.73589 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 241bb072-524a-3838-9346-f461f11e224a | -5.60683 | -46.2888 | 2024-11-24 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a70d4735-583a-3fdb-8c5c-a9012cec2843 | -1.1123 | -53.39746 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52bd95bf-863d-3334-b414-d7b67aeb021d | -1.1973 | -51.76442 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 680fce52-8b59-3d0c-9053-931e12305073 | -2.74452 | -49.12394 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc3318c7-fdee-33b7-8187-cf57e20d962f | -2.08457 | -49.60746 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 834c0cff-ca78-384c-bec6-de86eebc86ec | -4.21091 | -50.40366 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd13d580-a59e-3eef-96f7-b1621ddf6b36 | -2.87 | -45.83577 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cf0af169-20d3-32ff-b7dc-7658a85b25bb | -1.72772 | -54.99525 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00b3bed5-6e8a-36cf-8691-93685d161b83 | -3.08535 | -51.28336 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e02c495f-f330-34a1-8039-7fb4c545fa07 | -1.20657 | -51.74829 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ac9a579-ef38-3c22-96b1-1a1f18a358bc | -3.77721 | -50.98722 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a361608-8c41-3209-9745-232cac2f6f0f | -0.94315 | -51.65139 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4048506d-29d7-3b86-9d80-c7a8145334ed | -0.81696 | -51.61032 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd01c488-6217-3db5-babb-062e4017907d | -3.80546 | -51.26578 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9ac28d2-7762-39de-a414-fc2a5287f556 | -2.78201 | -52.87861 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2908930c-71f7-3efe-a75e-c5871694228e | -2.24923 | -50.47236 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e1ab065-e03f-3020-a86a-7be5a0a88dbf | -3.0167 | -51.24426 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d4db630-94b7-3d3d-a809-c283e5cd25e2 | -2.1655 | -53.77678 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ce8eec7-2d4b-35f4-8019-8d8e166b7bba | -3.8644 | -47.0611 | 2024-11-24 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb1df536-4930-3a2d-bd75-331da06d298b | -2.15744 | -50.49522 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef42c395-b808-38b4-8c67-646178c3f948 | -2.43576 | -49.36419 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd6a3582-e3b8-33a4-9ec3-759f5a0db532 | -2.75798 | -54.07212 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92339b70-de66-3f70-b3f5-662673ee0d0e | -2.59664 | -54.0478 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acbf6f6e-9798-3ec5-b92e-9061bac20397 | -3.31994 | -53.28864 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b82242ce-f820-3199-a903-44d6c22205ee | -2.00176 | -50.64184 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93e1bd53-a64e-3b31-a17e-576835eabef9 | -1.73606 | -52.04228 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 785313e3-85f4-3600-8ff6-993e6e8785ff | -2.3144 | -50.68626 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c343582-20ee-3d51-9a9b-ce87f6b95eda | -1.40804 | -54.47001 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README39.md)
