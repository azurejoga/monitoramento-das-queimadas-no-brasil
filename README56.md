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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcacd86c-5769-3991-aac0-fa96cf3c5ec1 | -12.53409 | -63.30441 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c915e6a7-210f-3e9c-abda-cd08e3f311ee | -12.53402 | -63.19626 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 739774b7-c33d-3106-99a8-932d689c7e98 | -12.53354 | -63.30793 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1719aa4a-4f04-3cfa-aab9-713dc62c850e | -12.53347 | -63.19978 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96a5029a-47eb-3e02-aa12-8194b1b4d296 | -12.5329 | -63.18164 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c89307e-ae8a-36f5-9e8c-a801187883d1 | -12.53236 | -63.18517 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9dab993-3307-3025-92bb-928a107c9302 | -12.53181 | -63.18867 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4a8df43-81ce-3056-b75c-58693d07fbe2 | -12.53126 | -63.1922 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f6f13e1-7bf8-375e-9751-130a0ac568c6 | -12.52905 | -63.18462 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16f7326d-e6b1-3b48-9bb7-dbd4d0c32bb7 | -12.5285 | -63.18814 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ddbc5d4-02fc-3efc-81f9-8c288b955806 | -12.52693 | -63.30686 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0526c80f-8097-3e22-bb3d-450b3657c925 | -12.5252 | -63.18761 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc298952-0c32-318d-88a9-5f60ecea194a | -12.52465 | -63.19114 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0c776d0-b1df-340b-969d-f5bdbb65918e | -12.52418 | -63.30281 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3110cb48-16b0-31c6-b286-13441597be00 | -12.5241 | -63.19465 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51daa7bb-82c0-338e-8330-1364efc7c742 | -12.52363 | -63.30632 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b246cb5c-9044-30ca-a09e-d5ec1eff3524 | -12.52308 | -63.30984 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a83dccb1-94fe-39b6-b148-1f8311aba36b | -12.52134 | -63.1906 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7509edcd-e9b5-32c1-b56b-82269d3e17dd | -12.52087 | -63.30228 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f702a25e-e6ad-3b73-9262-c47423cd5285 | -12.5208 | -63.19412 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 987b14b3-8f48-3ffe-9309-dbdd05e5331f | -12.52033 | -63.30579 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 73641e5c-6b1b-3530-9810-0319f6d9c504 | -12.51978 | -63.30931 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 844ba1b8-7c97-3751-89d2-e9fdcfd4ef7f | -12.96453 | -62.78654 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74be78f6-6fdb-3514-b4bd-dd57c078aa7b | -12.96124 | -62.80793 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70172204-c491-3d65-904d-98bb5386a669 | -12.9612 | -62.78601 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 233b7ddc-7c60-3399-aa58-d5bf18563822 | -12.95994 | -62.43635 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc832d29-17bd-3f49-a397-17b5f0e3d865 | -12.95671 | -62.17159 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac6cc340-fec8-360f-a758-89076e5261be | -12.95623 | -62.79618 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fe1dbc3-405d-3178-a135-9ce54c6bb280 | -12.95569 | -62.79974 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e88efe31-0922-3061-8e3c-b1a7ff9a4c2d | -12.95236 | -62.79921 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b302c2b2-6f5b-3d09-b609-6eaeff4fb3cd | -12.86388 | -62.44367 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166d0fc5-4c04-32c0-9701-aaf8ce93475f | -12.78288 | -62.28293 | 2024-10-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d25c7928-3ce9-3d9d-8c65-abda913499be | -12.7653 | -62.68945 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a3029bf-f23e-3be0-97e6-0750fa982fa2 | -12.76143 | -62.69249 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6a8284c-7975-364a-8463-24464cfd613c | -12.7581 | -62.69196 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3850d857-7106-3da9-bfa1-266bd155bd4e | -12.75755 | -62.69553 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29ba6957-ea9e-3ce9-836c-9a5949200173 | -12.75423 | -62.695 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7de3b496-9f35-3916-b5c8-f1f79066d4d4 | -12.75368 | -62.69857 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 249b044f-eaf1-3cb0-ad03-86774e446036 | -12.8393 | -63.0033 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b8272d2-ad93-38eb-9708-4f346d2ce103 | -12.83875 | -63.00684 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 555b390e-fa50-322d-9e24-4839d1269d54 | -12.83599 | -63.00277 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30119544-b987-38e6-b2e6-bd07ee5df817 | -12.83267 | -63.00223 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 893c71ca-279e-3334-841c-48c365247edd | -12.8321 | -62.98399 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66e4a46c-df53-30cf-84ab-4d0c6f393606 | -12.82879 | -62.98346 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8ba9283-4e53-3c98-b9b7-28114235a13f | -12.53492 | -63.03747 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc3832c2-c574-31ac-be0d-eec3a5381757 | -12.53438 | -63.04099 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 685649d7-caea-3611-88cf-3f2cf6f01bfa | -12.53325 | -63.02635 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a231162-5e8c-3559-abae-7258639e3901 | -12.53161 | -63.03694 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d019f8fa-c223-3cb3-8ecc-6768be61b694 | -12.53107 | -63.04047 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da2da27d-f192-3eed-bb2b-8565e657bbcf | -12.5296 | -63.02598 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4951c5c-18df-37af-8f54-37c76f379dc6 | -12.52905 | -63.02951 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f59937d5-781f-3e5e-bfe1-1cf8da446819 | -12.5285 | -63.03304 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d38f6b40-22af-3e95-98f2-69fdf670a6ba | -12.52795 | -63.03657 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe696ae9-52c0-3e8a-8021-3f4ae2d7b7c3 | -12.5274 | -63.04009 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e17e907d-baa2-38c6-bb07-896cd14a4cb7 | -12.52686 | -63.04362 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd290a5f-a8a6-38f8-b990-767541c16194 | -12.52631 | -63.04715 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8915d2c-a3af-320e-9ca4-92a07a09fa43 | -12.52629 | -63.02545 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 448a0053-1860-3e3f-8537-aeead2bec5b7 | -12.52519 | -63.03251 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 454b32b3-7e27-34f4-8527-dcbad8fdc17c | -12.52464 | -63.03603 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9eaabd6-0e23-36f9-a82c-3083bc10f1fa | -12.52355 | -63.04309 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0b04476-22dd-3ae2-8f5b-6e13b2ec4e17 | -12.52353 | -63.02139 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dafa874b-9dd5-3392-bc02-3d894028d672 | -12.523 | -63.04662 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6eb91e5e-22fb-3e09-87da-d52efe97fee3 | -12.52188 | -63.03198 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d369c358-7506-3011-95d6-01a7c5e7b174 | -12.52024 | -63.04256 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 59cf7799-81b4-3fac-a2de-3d811c65e106 | -12.52022 | -63.02086 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 638e1431-e543-3912-8f36-1b8499a5b200 | -12.51969 | -63.04608 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 22b2a9df-3bda-3035-ab6e-cc0dac57449e | -12.51693 | -63.04202 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 656003bf-6cbb-3c96-b7ba-b2a5bd0b0405 | -12.51638 | -63.04555 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 68349ebc-6d01-3de5-b6db-f069cb367619 | -12.51362 | -63.04149 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4261f04-95ab-3108-8b68-c17e42a1b4fd | -12.51307 | -63.04502 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cce3612-f6f4-3472-815b-ff583b37c668 | -12.47385 | -62.99172 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b242b81-852c-3607-afba-476387087ecc | -12.47331 | -62.99524 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56102cbd-65b0-3a40-b35a-f9fa655d868c | -12.46334 | -62.97194 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a639e5f4-08bc-3fce-9164-61f95b55a293 | -12.4628 | -62.97547 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ef954ea-76ca-3165-ba54-184f307a41f6 | -12.46125 | -63.05114 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e66e426-cc81-3af7-a093-04310e05f46c | -12.46003 | -62.97141 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 29ce78ba-2717-3fbe-92e7-f0efd5d87d4b | -12.45848 | -63.04708 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dad199ed-0b8b-3052-878d-2a601639bd6f | -12.45794 | -63.05062 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d37f9d8-3db7-3d9d-af1e-0e0ba27bbdd6 | -12.45739 | -63.05414 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47fca292-d91c-38ae-9fe0-a01e8a60e6cc | -12.45518 | -63.04655 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d7fc468-41dd-3bd7-9b5b-016c7b08eaf2 | -12.45463 | -63.05008 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efd2ac4e-2b48-318c-a8d3-7f0bee5cadc4 | -12.45408 | -63.05362 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be77763f-0bdc-31cf-852a-14ef5a280676 | -12.44027 | -63.03332 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4b24b84-3af0-37e6-a75a-9dc198b43bfa | -12.43751 | -63.02927 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddd4378e-60d9-352c-ab17-4744bb1eb43e | -12.43696 | -63.03279 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e03ffe0-e730-327d-bf82-b27d09cfc7da | -12.4342 | -63.02873 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59d4eb91-e481-37b8-b3a1-09274457bef6 | -12.42925 | -63.03878 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab1d5cee-8fd7-31eb-981f-075992d081b2 | -12.39317 | -63.00771 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd3d65af-0ea8-3945-938e-228c0318612b | -12.37931 | -62.94401 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b01fefac-b33c-3195-a189-22a1a3d23cb9 | -12.36667 | -62.98176 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 696cab1b-8d68-3423-941c-54ba5082e6e0 | -12.51757 | -63.30174 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0f0ac2c6-a8b9-3cd5-925d-271ae3ae8434 | -12.51702 | -63.30526 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4154cfb7-433d-3197-9d68-3a3aa3a3d930 | -12.51647 | -63.30878 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fc0300f1-1ad8-3b22-b959-cda4ea3ffaaa | -12.51481 | -63.29769 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 220983ab-0e7d-3620-bcf4-44e4e0f1c207 | -12.51427 | -63.30121 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f20e16c7-0ed7-3d46-b536-79d6de2872fd | -12.51372 | -63.30473 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 938f3fed-b148-3e35-a7c2-882fc50bc5df | -12.51317 | -63.30824 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41b50cb2-4c4d-39a2-a231-b36b1ed589ff | -12.51206 | -63.29364 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cf0b116-fa5d-3f51-9fdf-f81deeba5e97 | -12.51041 | -63.3042 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f981b73-21e7-3405-936f-34370d31dcf1 | -12.50986 | -63.3077 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README57.md)
