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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71101a94-8cf3-3b63-b61c-5b4eb51b7dc4 | -3.32736 | -54.08922 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 415e8a80-3466-31ef-a08a-aad981648670 | -3.23039 | -54.24748 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0b174fbf-2563-332a-95e6-89a06f908ad6 | 1.40207 | -55.9237 | 2024-11-22 05:52:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8d6df1a-5ad1-3921-b91c-6cbe9f9cd4c0 | -3.23133 | -54.24132 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| eec0f833-b8fe-302e-8622-8e799384f647 | -3.24283 | -54.24231 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2657b1d0-0756-34be-9039-51df27424486 | -2.74088 | -54.1276 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20e4d170-862c-3207-b136-43a7ea85dcc8 | -3.1758 | -54.31081 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9938a986-447b-32fc-acc1-e4922b98ba8a | -3.18085 | -54.32536 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2865c91a-8ab4-3b30-8023-0807e23b526f | -1.26001 | -53.36591 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 95f9954d-9114-3dae-baa3-e31cca0405dc | -1.13649 | -53.40441 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29bcb153-565b-3f72-bcba-73e242a4acd5 | -3.50796 | -53.81305 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9bd9be4b-56bc-3ea8-ba4b-10ef3e0df4f4 | -3.23493 | -54.24736 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b126aa25-c406-37c6-82a6-64b4eefc2495 | -3.56883 | -54.22366 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e892a4d-41c3-3339-b8bf-4d3f95bf6902 | -3.32014 | -54.0891 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d222065a-8ce7-3e84-b26a-6b1d2c09b011 | -3.23229 | -54.23499 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| becb502f-a7ec-373e-8ce0-9dbc827da86d | -3.5163 | -53.80628 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d75b6f67-8ce5-3582-a604-98bf810cbfa8 | -3.27988 | -53.83613 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 505e2eb6-47d5-311c-bc21-13f3a2a292ac | -3.10951 | -54.29139 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4d5b552b-c412-3a9f-bf68-88f3d6836ae3 | -3.28391 | -53.84563 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dc2b81f9-c9ba-3afa-a1f2-223602439de3 | -3.18781 | -54.32653 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a93ec90b-a4c8-3598-b43c-25ee97c8ebde | -4.13718 | -54.6619 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9544427d-5180-336a-8137-3f2a51120582 | -3.56182 | -54.22234 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 050f9cd3-3a51-3e3f-9ed4-b0ba6a624f45 | -2.19452 | -53.65588 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f0b2132-74f7-310e-8b0a-2d147e1a9877 | -3.22528 | -54.23388 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 30932d04-1660-3599-a07b-5981838e4c02 | -1.14026 | -53.40649 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 211e82e9-5a61-31ae-99dd-f7a712648c4d | 1.37781 | -55.94719 | 2024-11-22 05:52:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 011b6e60-ad72-3a06-98cd-3b530ca3de07 | -3.27274 | -53.83471 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1464673b-2e41-3534-a633-6fbb09cb3112 | -3.241 | -54.25489 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b1e8b32d-ffc0-35bd-8d40-ccc9659826b4 | -3.50163 | -53.80579 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 271891c0-2522-344d-a093-956cbfa9d0fc | -2.2215 | -53.73666 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 445901ed-7065-3cbf-92c3-34dce4c42546 | -1.11998 | -53.3957 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5dbb30dd-fd51-39db-a0e5-fca46826ea11 | -1.12223 | -53.40186 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba1915e0-1215-3b51-878c-c1d475155852 | -3.50676 | -53.81128 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0a5186a1-799e-3ed7-98a9-ff44e462ca9e | -3.57187 | -54.68613 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2f4121d2-fac1-3460-955b-7ef40dad2dc3 | -1.26142 | -53.36786 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b229727a-2365-37df-8e7a-1feebe1bf983 | -3.31922 | -54.0956 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 826a0bd9-6889-3d93-90db-08c6d4bad61b | -0.14275 | -60.86898 | 2024-11-22 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6112ae65-8593-3249-b8a9-b8edc3a85c99 | -3.50051 | -53.8038 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a2df3b2a-3fdb-3f7f-b5c5-fe47450a0562 | -2.50523 | -54.15229 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 33e322be-1490-3119-991b-49903499abd9 | -3.20225 | -54.24407 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9048dea8-0713-35e0-872c-576de684e3e1 | -3.22841 | -54.26055 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 31b9fc62-f7e9-3f59-9f4e-a2c2e4aa3781 | -3.22944 | -54.25377 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 708d4bda-32a0-35ea-8c0c-f2d3e19301c5 | -3.21638 | -54.2454 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f379a03b-fc1c-3f26-8e23-2d7d6b85beee | -3.58262 | -54.51934 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4f99649-fd2c-3696-9d2c-39a27196b809 | -3.11161 | -54.28545 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17eb2b11-7a56-3b7b-bd69-fd9f31040290 | -0.1434 | -60.86485 | 2024-11-22 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba7a26b1-c79d-31b1-8431-e463aac34a01 | -4.1444 | -54.6608 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 392ebff5-aa28-3ae5-8822-2d58737a34b9 | -3.52835 | -54.64826 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96df26a7-11ac-3b4b-8e7a-1d54dd7f396a | -2.15855 | -53.79751 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 428a37db-f0dc-3488-82bf-24fb2ae0b97a | -3.17777 | -54.31223 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be12c9bd-102e-3c54-89c4-3d51736ad092 | -3.21213 | -54.25652 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 97b460fa-832c-3744-bf8f-eac1a9b8245f | -3.18969 | -54.32785 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 510ad74f-d95d-34ca-a696-47e783cbe2da | -3.24192 | -54.24857 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d12626bf-01f0-359b-aa95-b691127d0900 | -3.28198 | -53.8215 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 433b7f12-ea9f-3f0e-941c-b53a597a90b3 | -3.18178 | -54.31883 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ca4c71f-df57-3e27-a1ae-9659356d1b60 | -3.28702 | -53.83744 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42e00c12-a5f2-349f-9eb4-517684111ddc | -3.20133 | -54.25024 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 96770aa5-fa53-3df0-a74b-a1e5d182c1c4 | -1.11887 | -53.40273 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| eed67408-ca76-39ba-b5b0-556dea6f7cf1 | -3.50992 | -53.79939 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 008e68f5-40f6-3e06-ae50-a701e6caec2e | -3.32189 | -54.09649 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8bb40145-68b4-3600-a772-ab75f76cc464 | -3.2173 | -54.23926 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ab230729-c241-3136-ad36-61e0763ea8f7 | -3.1847 | -54.31356 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c8b5f34-3a06-3ae9-8822-d35adde92d11 | -1.58944 | -53.80925 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 25d2fda6-1a8b-3f05-bb48-f3d92180f11c | -1.11506 | -53.4008 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87422064-727c-31cb-af96-1dfd3252e5f2 | -3.57573 | -54.51802 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbc26a05-28d8-3158-832b-187812313628 | -3.22095 | -54.24504 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0256dbd9-4a04-361e-a0af-d40b923e91c2 | -3.22704 | -54.25245 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 33ccd8f8-b405-31aa-b548-da09bc301a57 | -3.57453 | -54.51638 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc783a08-357a-32e3-b712-a9f61e2a3d68 | -2.0079 | -54.51976 | 2024-11-22 05:52:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a3fd217-7e67-3594-9bdd-65e8f45273a1 | 1.94216 | -60.84997 | 2024-11-22 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08bf2881-6afa-3955-b529-d47bb7607d36 | -3.23584 | -54.24115 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 18ed81e3-662b-36bb-88db-205cea597ca1 | -1.59323 | -53.8117 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1febe810-0fce-3831-b260-7a18f65f2249 | -3.22004 | -54.25133 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 74052d1f-644f-3364-befd-4be6c42ab789 | -3.63809 | -54.31965 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bb13724-04d5-30db-9246-d03eecaa8598 | -1.77489 | -53.59851 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ecc9531-3552-304e-84ed-5d0fe80f95e1 | 1.94277 | -60.85382 | 2024-11-22 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edd2f122-dc89-332c-8797-64cd25574a8c | -3.27489 | -53.81974 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d8d76e72-2d4a-3110-8239-ff83d675d663 | -4.13819 | -54.65477 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0181e972-e2a4-39f6-b6bc-25f036a3c712 | -3.22432 | -54.24022 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1f41f5be-2d41-3825-b932-8aa00971d1ee | -3.57861 | -54.68594 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2305b722-b024-3bb5-add9-16cf145fac1c | -3.51504 | -54.6913 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbc5ed19-264c-3290-b97a-dc7a0408d077 | -3.22884 | -54.24 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 64817d00-46e6-34ca-ae76-30fc1e9afce5 | -3.25586 | -54.25121 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2e76e23-6877-3d57-b35d-f8576988a909 | -3.28003 | -53.82268 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 546d6d7b-215c-3271-bca8-668af9a15e36 | -1.20768 | -53.69265 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 195ef59e-8233-3487-ac9e-78f7e91a95c5 | -3.24889 | -54.24991 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c567585b-821d-3e71-acd1-9b0edbf3f14d | -3.28602 | -53.84442 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d219bc14-d6d5-3f50-9aa8-e05248bdae42 | -2.21955 | -53.73117 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 94185427-ebce-385a-a7eb-fb0623d48c8b | -3.10869 | -53.99625 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46560bdb-c9ce-3f57-8492-bd3ac4d7b78b | -1.77382 | -53.60549 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be00d573-2f1e-34c6-9b50-1cfbb40c413b | -2.00546 | -54.52282 | 2024-11-22 05:52:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 81ddb2fd-9d7f-3ec6-ac94-9468430bd1ae | -3.50894 | -53.80623 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4a2367b5-eed4-3388-8f0a-bf9b409af4af | -3.19661 | -54.32922 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b7b86de-e9db-3b43-8d05-d883bd0130d3 | -3.57266 | -54.67851 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c070c2a-23e0-3010-a255-9baa121cd300 | -3.29113 | -53.85973 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab5ee62b-bf87-376f-b2d9-4763e6d97b6f | -1.20596 | -53.68194 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b04d1847-e29b-33b3-9886-6f54c90f9974 | -1.26252 | -53.36069 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6e5b674-d829-30f6-98e1-1bb9fbe80522 | -1.25881 | -53.37341 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d93e3e54-281e-3311-8fcc-f4b8572ea8fc | -3.18369 | -54.32027 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b148539f-ee20-3d99-bf18-232e7bff21ba | 1.39802 | -55.92181 | 2024-11-22 05:52:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README64.md)
