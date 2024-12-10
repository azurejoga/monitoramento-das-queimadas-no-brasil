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
| f4247cc4-c5ea-3a49-8e4d-f8f961debf07 | -3.00164 | -53.05205 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6c917e8-1cd6-373a-bb88-d65c5468b834 | 1.97963 | -60.91447 | 2024-12-10 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d575fabc-8825-3371-ab47-7cb7ce302e7a | -2.95411 | -53.72854 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbdece09-4591-3c1a-937b-52be91f7ffad | -2.96238 | -53.72733 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 909a55f8-eb9b-3781-90c1-74b5b8530c90 | -2.79107 | -53.24564 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2dc19ca-d6c9-3efb-a57d-bed9df3f3262 | -2.83102 | -53.06317 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6bba4af-c4f5-3235-bce3-6b42aa637acd | -2.30355 | -54.00133 | 2024-12-10 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d42a740-1ad3-3958-8e43-ac3008591ab9 | -2.94831 | -53.11572 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5cd1b02-e17d-30af-8959-780ecf4844d2 | -3.5274 | -51.48299 | 2024-12-10 05:37:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87c4378a-240b-3502-a7e1-8d0870a06b54 | -1.50008 | -53.4299 | 2024-12-10 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c32ff854-1ee2-359f-acd3-0cda335304a8 | -3.83327 | -52.35856 | 2024-12-10 05:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0da9e342-0c30-3147-95f1-526430f39724 | 3.21996 | -61.19594 | 2024-12-10 05:37:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be7532a5-b909-3545-8728-79998ba7bf99 | -2.99195 | -52.85761 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 40ce1624-27fe-3ea2-9aa3-5168398ae96b | 1.94329 | -60.86527 | 2024-12-10 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d628d1c-86a7-3482-92e0-bd3513cf346a | -3.0567 | -54.24503 | 2024-12-10 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd6ef590-7541-37ac-8201-8532f6be7bc7 | -3.05095 | -54.24438 | 2024-12-10 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b90fd8f4-4356-37f0-9301-a87c92cc2071 | -3.11168 | -54.07417 | 2024-12-10 05:37:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bb6239b-a446-3756-b17b-ae67b9d43b51 | -2.99313 | -52.86206 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 12e099cb-061d-39ba-85e6-89cfce871a66 | 3.22336 | -61.19542 | 2024-12-10 05:37:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9831786-5099-3547-965d-ea743c445e37 | -2.81186 | -52.98069 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f8903c0-944f-30e7-9515-bd93061cd890 | -1.69215 | -55.67407 | 2024-12-10 05:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c73b478-8df0-3b03-a223-f5de9fcaa7f9 | -4.03491 | -50.80703 | 2024-12-10 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5bc9cd0-ca3c-3434-a78b-2d6953d5c096 | -4.13742 | -53.67656 | 2024-12-10 05:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 542aa030-487b-3eb0-8bfb-2f39af4413e9 | 1.97616 | -60.91501 | 2024-12-10 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12c1ba1b-9246-3399-8433-bd44110c4d4b | -3.50916 | -54.68299 | 2024-12-10 05:37:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6c695dc-2c07-3fd1-b338-af7439c39281 | -3.27659 | -51.07887 | 2024-12-10 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0efc7e7e-1fc4-3568-ace5-372a22a2b631 | -2.03624 | -54.43659 | 2024-12-10 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b5ae2f0-23f9-343a-a597-3da5b4898832 | -2.31504 | -54.00308 | 2024-12-10 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf9c125c-e4d3-3766-90b1-34751f7bff99 | -3.53098 | -54.68996 | 2024-12-10 05:37:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e261c041-eb25-31bf-a416-142968725614 | -3.09377 | -54.07527 | 2024-12-10 05:37:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0579f053-6775-3178-8dea-1c416b72b541 | -3.2756 | -51.08543 | 2024-12-10 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e369cb80-8777-3634-95a2-1e3c0851fdd2 | -3.80897 | -52.25258 | 2024-12-10 05:37:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b793bcd-54ab-3819-a227-f2d1cc4859a6 | -3.27585 | -51.07723 | 2024-12-10 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d63540f2-62f2-3fdb-a407-45f67f484210 | 3.22676 | -61.19488 | 2024-12-10 05:37:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bce867ac-6bcc-3235-8605-eb889138fc27 | -2.79264 | -52.86321 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0d008ad-577b-31cc-9ab8-7f244f4d2aa6 | -2.96044 | -53.11889 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59019f75-a70e-372f-9f3a-963f58e55b0f | -2.96123 | -53.72099 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eefd968e-bf2d-3458-a9e4-fc317b80074e | -2.94823 | -53.11659 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a65d16c6-939f-36f0-9a06-7027b1b6f62e | -2.8187 | -52.97718 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| acddf2c4-1da7-32d7-b927-69ba98168fda | -2.99457 | -52.85254 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 15e77ad7-1644-376d-bcea-48880325bdaf | -3.81636 | -52.24782 | 2024-12-10 05:37:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b70993e3-4dfa-366c-8355-a5ad676edd7f | -2.81804 | -52.98165 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b64f6812-16bc-3464-be42-81319bcfa819 | -3.10351 | -53.25184 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6f60c24-f4ce-3b01-b590-31e3d14333d0 | -3.0901 | -53.21598 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| b45b0198-221e-3971-a219-39cc3209e956 | -2.92113 | -52.96069 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2fc5bdbf-5916-32fc-a968-787557a507a6 | -3.92519 | -53.5865 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 720ef4e6-d408-31a4-b6ee-552f46aa9eb1 | -2.79194 | -52.86779 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc7236a8-5e2c-3b9a-911c-5c18e0805f75 | 3.22958 | -61.19068 | 2024-12-10 05:37:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8eedea1e-4f58-3250-9dd6-8731dc62cdd1 | -2.96062 | -53.72522 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4128a9da-6a8f-38ea-af07-c2909427dec9 | -1.33409 | -52.23352 | 2024-12-10 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aeff2a50-d897-36ba-b509-79245bce98b8 | -2.99125 | -52.86243 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a8da8fff-941b-3232-9712-96feb17e9b62 | -3.11099 | -53.24352 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8934e295-ca98-3ea4-9134-14daa724a7e8 | -3.35287 | -53.81023 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afda2867-7bcb-320a-9cee-b41d100a494a | 3.29233 | -60.69975 | 2024-12-10 05:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e16555e3-615f-3f07-af9c-2f00b57ba02d | -3.46559 | -53.96472 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32229612-a301-3075-9486-cd33837d8e19 | -2.91427 | -52.96426 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6a46f785-e9b6-3989-8d12-42c34456d022 | -3.5206 | -51.48173 | 2024-12-10 05:37:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9965f085-1b66-3762-ba5e-4fd5cbdfb75b | -2.98689 | -52.86114 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0b958669-543a-3c5d-bcb5-a7e4248ad7c4 | -3.50971 | -54.67921 | 2024-12-10 05:37:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e371ee0-c2b0-3886-b6b4-3c08dd8eab80 | -3.09481 | -53.74464 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af635453-a6a7-3a04-ba79-a9c68dee0fa2 | -2.99548 | -53.05111 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c349101-ba6a-35eb-8a39-7bbda749814e | -2.91494 | -52.9597 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 13de3989-ffd6-3fb0-85ee-f3e1e57b9f9b | -3.34114 | -53.25775 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 659f06fc-0f9b-3521-bc97-2ebda6e5dc81 | -2.83717 | -53.06408 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b53065c3-8fe3-3108-80fa-da81fa70e0f8 | -2.99264 | -52.85279 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 18786180-bbf4-35d9-b7e9-ffb0c4ac6109 | -1.7019 | -52.61241 | 2024-12-10 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b22a2bd0-4a22-3589-a196-7252fd56beb0 | -3.06407 | -53.79971 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b1881ed-7962-3ec8-bcbf-f9dfeefb2c36 | -3.5248 | -54.69312 | 2024-12-10 05:37:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f682b852-066b-3bb0-96d1-433504d2584e | -2.98728 | -53.02525 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8984e31-d722-301d-af03-1cd2618c2a2f | -2.95442 | -53.11686 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91147619-d354-3cbe-ab47-e6e81fa44758 | -2.3093 | -54.00218 | 2024-12-10 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf5204be-2a9d-396f-a222-d992877cc9d6 | -2.79171 | -53.24137 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c02dbcd-4bb3-33c5-8fa2-e28f89844c83 | -3.10411 | -53.76354 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb6bf9c9-3834-31df-876b-7de4af7ee6a7 | -3.46502 | -53.96873 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1bf45da-65f6-3e56-b18b-1258895d198f | 1.12727 | -59.42812 | 2024-12-10 05:37:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76e681f2-6c61-386c-9b33-58fa8dadb6ff | -2.96302 | -53.72311 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 899dde07-0fa7-31c2-a242-155eb1c876b4 | -2.81121 | -52.98505 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21df28d1-d81d-3b47-ba5e-20fa3e24fc5e | -2.99385 | -52.8573 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c933b85f-6e87-310a-8109-d7ade02b6921 | -3.27491 | -51.0838 | 2024-12-10 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bff4757-bece-364c-a77b-af5e196455dc | -2.77894 | -53.24373 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 211b70af-fdd5-34ae-bd7f-d09394aa30fe | -2.95648 | -53.72645 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9828758-1fef-372e-9f38-5c7ac817de47 | -3.06872 | -53.7997 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ccf7635b-5a15-3f98-88c6-dea66fe5f71a | -4.03691 | -50.81403 | 2024-12-10 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11fe7be4-4c06-3c1b-a43e-5bef76c2bd16 | -3.83409 | -52.35308 | 2024-12-10 05:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe6cfd23-67ac-357e-875d-66117fc1d4a6 | -2.98763 | -52.85623 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a6d333b5-494b-3265-8bab-4ca372d5b4f7 | -2.92046 | -52.96521 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44122c57-262c-3f04-ac0c-141f57ec28b1 | -3.3011 | -51.63391 | 2024-12-10 05:37:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d2fd5ef-4ea1-353a-8e77-1b773fbb0c73 | -2.98838 | -52.85132 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 81afee66-2dbf-382f-aa46-5220894892c6 | 3.23016 | -61.19436 | 2024-12-10 05:37:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c01ebd3-11e4-3ad2-9d7f-10f812cb94b9 | -3.06995 | -53.80063 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71c2c6fb-b569-3134-b8d4-c9f198f133fd | -3.06183 | -54.24983 | 2024-12-10 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a939f0e2-8bb9-344c-aa10-6046987a30cc | -3.08944 | -53.22046 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 239378a5-bfb3-3ae4-a023-fbe38b51f6da | -2.99345 | -53.0219 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 613aa2d6-57f3-338b-8182-eb0ceaa92d90 | -2.21993 | -53.7253 | 2024-12-10 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31bd64b6-3b94-39c9-9120-6f3feef0066f | -4.04206 | -50.80811 | 2024-12-10 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be591ec3-ab99-3a14-a916-899b36c69809 | -3.52659 | -51.48235 | 2024-12-10 05:37:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 63827dfd-b630-362b-918a-db2822cc6fbe | -2.78501 | -53.24468 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b73742f-9dca-322a-999c-0615562bf970 | -2.22037 | -53.72591 | 2024-12-10 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcfc83d2-4b54-3386-90ad-40cffdc43f5d | -3.09673 | -53.25558 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ad8280d-6c85-3f64-bf74-7f0d104f211d | -3.10473 | -54.08103 | 2024-12-10 05:37:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README39.md)
