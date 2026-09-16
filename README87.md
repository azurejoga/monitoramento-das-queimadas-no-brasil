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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd14a5c1-c98d-3578-9bc3-d8d1b99a977d | -14.1942 | -53.3692 | 2026-09-16 16:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 6fdb126c-feb9-3b24-b419-ed1f2b8120b3 | -8.6178 | -44.5511 | 2026-09-16 16:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 8f29c322-db50-31f3-895b-85a1a634408d | -11.7357 | -54.5227 | 2026-09-16 16:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c5e44e6c-2843-325c-b5fe-06d0be568b3c | -2.6601 | -57.5507 | 2026-09-16 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c8393239-7c12-3f53-8f1a-46182071d16f | -8.5428 | -44.5132 | 2026-09-16 16:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 409.7 |
| 4a3ceb8e-0990-32a9-9312-4dd8f1ea453f | -8.5989 | -44.5531 | 2026-09-16 16:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 760.9 |
| ac2322f7-7561-35f1-98e8-42cbe238a9da | -10.8114 | -46.182 | 2026-09-16 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.2 |
| cdc15824-ae7c-3bd6-8668-9d9d18adca20 | -8.6311 | -66.5287 | 2026-09-16 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 9fad9141-f216-3749-a62a-7343c5f39f75 | -1.2268 | -49.1899 | 2026-09-16 16:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 42b56df2-9609-3b50-8289-6abf5010788a | -13.3949 | -57.0242 | 2026-09-16 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 7ce65f31-78df-3406-b49a-670e6a8e4480 | -9.189 | -65.8983 | 2026-09-16 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| b33e7fab-d9fd-3953-b5e9-bd453122fb18 | -3.4278 | -58.0009 | 2026-09-16 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 7a860427-6bdc-3a3c-a87c-bf541fbb7a5e | -10.0985 | -45.5913 | 2026-09-16 16:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| fdfddec5-3f69-302a-8fe7-3d00fb806ac0 | -10.331 | -45.2883 | 2026-09-16 16:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 2dc8dbf6-2262-3ffe-8c6e-955a003bb8b7 | 2.2186 | -50.9185 | 2026-09-16 16:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 952594fa-ab39-3559-9c81-f115981842ee | -3.3871 | -59.4075 | 2026-09-16 16:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| fd94d3b5-cefc-32e7-bd52-71e3099f79a4 | -9.1614 | -68.2198 | 2026-09-16 16:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 0d149a6b-32a2-30ee-8782-3879c5ad6bfc | 2.2186 | -50.9393 | 2026-09-16 16:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b7a72bef-a195-3324-9c37-e22a6a61ba35 | -3.4278 | -58.0009 | 2026-09-16 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| f406fa72-ca5e-3804-8368-a1836fed3297 | -3.4462 | -57.9812 | 2026-09-16 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 135.5 |
| bedbbfc0-4be2-3a30-b50c-38f97e1498c0 | -8.5428 | -44.5132 | 2026-09-16 16:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 298.3 |
| 3090e0e2-43b9-3aa3-a235-4ebc656a17d9 | -12.6821 | -54.7174 | 2026-09-16 16:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| eb14ae50-11e5-3858-baf2-c4234f5db291 | 2.2187 | -50.8977 | 2026-09-16 16:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 61.2 |
| f568ceee-2e3a-3cdb-b4d6-92c4e0d26be7 | -9.1337 | -65.8253 | 2026-09-16 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ae6327ab-1e8e-339b-875f-f7ce36d76c2a | -12.6826 | -54.6763 | 2026-09-16 16:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 24491a19-a486-38bd-94e2-275f4f10a227 | 2.2003 | -50.8981 | 2026-09-16 16:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 3b46a247-edc9-3802-ba76-118f5d97b637 | -10.8114 | -46.182 | 2026-09-16 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| ff05c20b-346a-3ee4-b838-4530ad7fd2b3 | -9.1337 | -65.844 | 2026-09-16 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 482.1 |
| 603c7f65-1926-3bef-9cc8-1d0bfeebb688 | -9.189 | -65.8983 | 2026-09-16 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 044f7303-b666-3d7e-b1a0-b4d7a00671ab | -8.9239 | -63.3371 | 2026-09-16 16:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 46f68b82-e3de-3a4e-a386-12fffa3bb246 | -2.6601 | -57.5507 | 2026-09-16 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 90b03b31-25b4-35d6-9ed1-a30bbb098ae6 | -1.2268 | -49.1899 | 2026-09-16 16:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 3fbede22-db37-37d5-ae86-570706710a13 | -10.8305 | -46.1796 | 2026-09-16 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| c7e0aadf-8d0d-30e3-bc70-c5b699cb423e | -13.3949 | -57.0242 | 2026-09-16 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b0d1a92f-e7c7-3e92-b34b-6208ca103b9a | -3.4279 | -57.9816 | 2026-09-16 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 5093e283-fd93-3464-b170-dabf15c16d75 | -7.6511 | -67.164 | 2026-09-16 16:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| bdac03d9-d9fa-3e83-a60a-0173ab6d3303 | -12.6636 | -54.6782 | 2026-09-16 16:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 6e31a48d-57f8-34f3-b8b0-9cf50e4706ec | 2.2186 | -50.9185 | 2026-09-16 16:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 3e992bcb-268e-3ef2-92a1-ad31662e343b | -8.6311 | -66.5101 | 2026-09-16 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 564b20a9-64c6-3539-b9ef-ec743b970982 | -8.6188 | -44.4819 | 2026-09-16 16:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 886fa7a6-e733-39dd-9cf7-b7fe815b6603 | -3.4279 | -57.9622 | 2026-09-16 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| c9445e75-599f-331e-9385-de5c28a9f4e9 | 2.2186 | -50.9393 | 2026-09-16 16:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e1f69631-8725-32c2-aa62-b1c48c3d0a84 | 2.2002 | -50.9189 | 2026-09-16 16:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 83.8 |
| d982275f-ef18-338b-b8c8-a7ac08c4f215 | -9.3572 | -50.137 | 2026-09-16 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| c0dd3a6f-d399-30be-81be-20369b49a4c6 | 2.2186 | -50.9185 | 2026-09-16 16:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b89e1ab5-239c-38ac-8c08-7183e5b870f7 | -7.6511 | -67.164 | 2026-09-16 16:40:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 6f6f64c9-a6de-3d4f-beb4-c383fada46dc | -12.6636 | -54.6782 | 2026-09-16 16:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 7a7e882a-e1aa-3357-9340-de79b0ec5330 | -1.227 | -49.041 | 2026-09-16 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b079899d-9a04-3282-9086-73db4cd24b09 | -9.4139 | -50.1103 | 2026-09-16 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 20f63596-957a-30cc-9fc7-260580f8a71a | -3.4279 | -57.9816 | 2026-09-16 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 5f4fdaf3-ac39-3375-8e02-51d2203eae8e | -8.6311 | -66.5101 | 2026-09-16 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| aa193fb7-89b7-3e81-b4b4-c259b290e801 | -9.3763 | -50.1139 | 2026-09-16 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 146621e3-2432-316b-9ef2-91d051fe8992 | -9.3765 | -50.0925 | 2026-09-16 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| bed86517-3095-3346-aaa2-939bb551c8cc | -8.5989 | -44.5531 | 2026-09-16 16:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 282.8 |
| 5a213f3d-38c1-3073-98ba-7e0502da10a5 | -10.8114 | -46.182 | 2026-09-16 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| a3f199fb-8999-3a12-bc12-f8a09e1c02f1 | -10.8421 | -60.8009 | 2026-09-16 16:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 585e743f-d194-3594-992c-1ee9033b114b | -12.6826 | -54.6763 | 2026-09-16 16:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 526d0b2d-dd20-303b-bc0b-d55a0670a5f3 | 2.2003 | -50.8981 | 2026-09-16 16:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 7e62b55b-1dba-359d-97f7-96115a9898ea | 2.2187 | -50.8977 | 2026-09-16 16:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 052cd1da-3fb2-364c-86d6-ca4c1812a914 | -10.8419 | -60.8202 | 2026-09-16 16:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c752aba7-9f1c-3823-bc96-e6fe0b85cad6 | -12.6821 | -54.7174 | 2026-09-16 16:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| e5582f97-16aa-34e2-bfbd-c977ac09bbb6 | -8.6188 | -44.4819 | 2026-09-16 16:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| b25cfb8b-0030-3dca-9f97-369ea261accc | -7.1198 | -42.1309 | 2026-09-16 16:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 168.7 |
| b23a6953-a358-34df-9dbf-ec5af9d51779 | 2.2186 | -50.9185 | 2026-09-16 16:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6945ab47-29bc-33ea-ad1f-81a8f45488bb | -3.4279 | -57.9622 | 2026-09-16 16:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| a3c6bf49-ca3c-31db-bd9c-8ab0d279643c | -9.3569 | -50.1583 | 2026-09-16 16:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 6f36b66e-077e-34e9-9f4e-2bbec35a2e9d | -9.3758 | -50.1565 | 2026-09-16 16:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 5aa99114-68b1-31a3-8782-abb5ad47095f | 2.2002 | -50.9189 | 2026-09-16 16:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f52d1792-3240-3d60-b818-70c41e516c16 | 2.2186 | -50.9393 | 2026-09-16 16:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 887abdf4-a4be-3e64-9085-828ab1ac6cad | -9.7687 | -46.1067 | 2026-09-16 16:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 313a1e29-5f65-36ed-94c2-63e4f29cbf17 | -10.8419 | -60.8202 | 2026-09-16 16:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c3df39a2-20ba-39b7-aa89-1ad3b433f0b3 | -12.6826 | -54.6763 | 2026-09-16 16:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| c01f9bea-e87c-3317-953a-df473d9d4db5 | -1.2455 | -49.0407 | 2026-09-16 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 991cfcd4-2c6f-3f8c-8df0-3a6e44cc672c | -8.5989 | -44.5531 | 2026-09-16 16:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 929929c9-bb72-3716-9af1-38c0ae22b981 | -9.3572 | -50.137 | 2026-09-16 16:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 4d342d11-65c2-30e7-8e87-ef2468c5f65c | -7.6511 | -67.164 | 2026-09-16 16:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 0c7d08fd-da11-32a0-9078-6a42411deef0 | 2.2001 | -50.9397 | 2026-09-16 16:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 49dc2a07-f1c1-3821-a127-24921464fde3 | -10.8114 | -46.182 | 2026-09-16 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 0cd1c3aa-e887-3f44-99a1-c8f0295befdb | -9.5725 | -46.601 | 2026-09-16 17:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 4eb2ab9b-a76c-36ae-adad-6be3feef114c | -8.5989 | -44.5531 | 2026-09-16 17:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 21333dd8-ed01-3ff5-b683-3d0770e990b4 | 2.2186 | -50.9185 | 2026-09-16 17:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1a157510-ac7f-374c-a9dc-d023d867a902 | -3.4279 | -57.9622 | 2026-09-16 17:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 45edf43e-7b16-309e-a700-236c36ec24d3 | 2.2002 | -50.9189 | 2026-09-16 17:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 83.9 |
| ea999a57-9d57-3850-b177-94a32e52bc71 | -7.1198 | -42.1309 | 2026-09-16 17:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 175.4 |
| 2a3fde24-7e29-36dd-9a80-bfca985dae75 | -10.8114 | -46.182 | 2026-09-16 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 244.4 |
| 0643a65d-90cc-399e-a16d-357d1f907b81 | -12.1265 | -44.199 | 2026-09-16 17:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| d870d410-f3e3-3189-bd40-63685c56a847 | -3.4279 | -57.9816 | 2026-09-16 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 81d993c9-8a55-3c41-9a43-ef0745541914 | -2.6968 | -57.5112 | 2026-09-16 17:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 341501ef-cb00-3d3e-a11a-37405d6491da | 2.2186 | -50.9393 | 2026-09-16 17:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d3b4b871-5ff3-3d2e-b068-2b4e6b3b1b3d | -3.4645 | -57.9808 | 2026-09-16 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 0c34fcaf-0096-3ff1-9cee-753022529838 | 2.2002 | -50.9189 | 2026-09-16 17:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 83.7 |
| f3f5b1d0-a032-36ad-8508-624208de55d3 | -3.4279 | -57.9622 | 2026-09-16 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 3f854a7c-59af-36aa-af7f-e7511f74417a | 2.2186 | -50.9185 | 2026-09-16 17:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 323c81fa-85b1-3177-a48f-166c1f036e49 | -12.6826 | -54.6763 | 2026-09-16 17:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 1bb8d706-2f6e-3b06-8495-da5a2a2d3168 | -9.51 | -46.03 | 2026-09-16 17:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f70df7cc-bdab-37dc-bf30-8cd94aed2ae8 | -14.55 | -46.57 | 2026-09-16 17:15:00 | MSG-03 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83698aea-794e-33b7-be3f-9e9c0500fd51 | -6.68 | -58.83 | 2026-09-16 17:15:00 | MSG-03 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3802f8c-f4ea-3872-82bf-420d343be107 | -9.51 | -45.98 | 2026-09-16 17:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c8d2746-25c0-3433-a2e8-261dee9b36fd | -3.4279 | -57.9622 | 2026-09-16 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 148114bc-0681-359a-af80-b866bb735bb4 | -2.6601 | -57.5507 | 2026-09-16 17:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |


[Clique aqui para ver as próximas entradas](README88.md)
