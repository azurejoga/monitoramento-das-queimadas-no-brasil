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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6f74a9a-e935-379b-9ef8-cdd8fd87a8ed | -3.8778 | -55.767101 | 2024-10-15 01:03:53 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec99d3f-5e99-3829-8d14-398d1746ac26 | -3.5839 | -54.651299 | 2024-10-15 01:03:53 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c80405e7-7493-36d6-9d30-c942e7df469a | -3.5855 | -54.658401 | 2024-10-15 01:03:53 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3efbe086-f6ad-31f5-9ca4-70f404d0ecef | -2.8982 | -51.924301 | 2024-10-15 01:03:54 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31714b28-5f9f-3615-afcf-d558731e02bf | -3.8228 | -55.980099 | 2024-10-15 01:03:54 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87114eb8-7624-30f6-b0de-9b1e95b9c673 | -3.8244 | -55.9869 | 2024-10-15 01:03:54 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c21c19-3f85-358e-ab30-adad914110cf | -2.173 | -56.203201 | 2024-10-15 01:03:54 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0781c603-4740-3659-a6e4-7ff2c2b4167f | -2.1746 | -56.209999 | 2024-10-15 01:03:54 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 020fdb89-f580-3778-8c70-9f9f09f27a2c | -2.1761 | -56.216801 | 2024-10-15 01:03:54 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17ec7827-2350-3f40-b0fd-3b5361d38046 | -3.0896 | -53.026901 | 2024-10-15 01:03:55 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0590cd-769b-3c09-90d4-7ebd3f65d4e4 | -3.2954 | -53.8372 | 2024-10-15 01:03:55 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05a4c40f-c6ce-3ba9-8645-54f54ac42d23 | -3.0915 | -53.035198 | 2024-10-15 01:03:55 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c10af1d-b2ac-3908-9f8b-0778cb1397f9 | -2.4323 | -50.219601 | 2024-10-15 01:03:55 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d43f086c-d7a8-32dc-8b58-296ef766ef7a | -2.4351 | -50.231998 | 2024-10-15 01:03:55 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee05a291-db87-3938-b8ed-408ebd624ad6 | -1.3946 | -53.089802 | 2024-10-15 01:03:55 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed9bf7c5-365f-38c3-bc48-790b7544c6ef | -1.3966 | -53.098301 | 2024-10-15 01:03:55 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b887635e-36ad-3949-a3b0-b92ca654b0c2 | -2.0152 | -55.915401 | 2024-10-15 01:03:55 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67897d8f-0bac-34ac-8880-795df7c9d777 | -2.0167 | -55.922298 | 2024-10-15 01:03:55 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d15886a-27f3-3b52-abcd-cca81ead6854 | -2.4226 | -50.221802 | 2024-10-15 01:03:56 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4286d4d-867e-34f2-8183-f34c0872a893 | -2.4254 | -50.2342 | 2024-10-15 01:03:56 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a6e535f-7dfe-368e-974d-2664632a12a2 | -1.8519 | -47.8139 | 2024-10-15 01:03:56 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66a7fcd2-4d60-3495-b01d-4b4ae5da4a06 | -1.8562 | -47.8325 | 2024-10-15 01:03:56 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20b2f197-8d43-301f-b2b9-905f09cad78d | -3.4205 | -54.658001 | 2024-10-15 01:03:56 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff0404d1-554e-35e9-9744-519ccd03b701 | -3.4221 | -54.6651 | 2024-10-15 01:03:56 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb7eaa68-c174-3fc6-aba6-351f7b054169 | -2.2028 | -56.883801 | 2024-10-15 01:03:56 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83b18455-a624-3e84-9c6f-d1a10777bc07 | -2.2044 | -56.890598 | 2024-10-15 01:03:56 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ec3ef2e-9f77-38d7-9572-2c633dabf691 | -3.0445 | -53.2351 | 2024-10-15 01:03:57 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87c18544-bc10-3513-8dc7-1bf89cb47e42 | -3.0464 | -53.243198 | 2024-10-15 01:03:57 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 799a8c42-4055-348a-86d4-fd1854ae6da0 | -3.0482 | -53.251202 | 2024-10-15 01:03:57 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64fc3362-3c76-340a-80d1-7bd7d39540c2 | -2.856 | -52.457298 | 2024-10-15 01:03:57 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6fb2b5e-f32c-3984-bba3-a05a78718047 | -3.0347 | -53.237301 | 2024-10-15 01:03:57 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54b8fe9e-7847-3b17-a9e6-710caa358f32 | -3.0366 | -53.245399 | 2024-10-15 01:03:57 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39afdcbd-7cc9-3b8f-a2cb-d8aed7cd7413 | -3.0384 | -53.253399 | 2024-10-15 01:03:57 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a644a4e9-2ec6-32d2-8ac9-9dfa58d0de20 | -3.5215 | -55.4216 | 2024-10-15 01:03:57 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 238d068a-c027-3f47-9da0-4e55a4987142 | -3.5231 | -55.428501 | 2024-10-15 01:03:57 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 423bd654-eb6a-3b05-9066-762db514f922 | -3.1135 | -53.7173 | 2024-10-15 01:03:57 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d80a4c2-c611-3cfe-a297-2e964b1e7d0c | -3.1153 | -53.724998 | 2024-10-15 01:03:57 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 810b4e0b-3d6d-3ea0-8ae4-9d66554a2e2f | -3.1171 | -53.7327 | 2024-10-15 01:03:57 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f68113a9-29d9-381c-8b58-142b82cc7365 | -1.5319 | -54.327702 | 2024-10-15 01:03:57 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04a16987-c9f6-3d90-ba96-5eac18ed6d91 | -1.5336 | -54.335201 | 2024-10-15 01:03:57 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 489b6516-8370-30dd-8b9e-a63b81f9fd06 | -1.5353 | -54.342701 | 2024-10-15 01:03:57 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8797d351-d203-365c-a48e-f3467176b538 | -3.1055 | -53.7272 | 2024-10-15 01:03:58 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4131aa7f-ed57-3241-80ce-b8aa4aed1f58 | -3.1037 | -53.719501 | 2024-10-15 01:03:58 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98c9ee0b-5884-37f6-ab9e-5758217e6f7e | -3.1073 | -53.734901 | 2024-10-15 01:03:58 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52a9c4e6-29a9-39a6-bf42-14945c02bcb9 | -3.3499 | -54.800701 | 2024-10-15 01:03:58 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2975862-4121-3564-80e1-c6a345fbd2ff | -3.1237 | -54.214001 | 2024-10-15 01:03:59 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd1c914-241b-35f6-a8e9-174f4bf8a67c | -3.1254 | -54.221401 | 2024-10-15 01:03:59 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cbdc30d-101b-38b5-9fea-62bafbc3addf | -3.1271 | -54.228802 | 2024-10-15 01:03:59 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20e52db0-86ee-3b7f-adba-242c7861c3aa | -3.1288 | -54.236198 | 2024-10-15 01:03:59 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3103430d-0f3a-35d1-a003-1db7a4128a76 | -3.1105 | -54.2015 | 2024-10-15 01:03:59 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2f6b71e-cd61-397b-9c68-b32a6b33210e | -3.1122 | -54.2089 | 2024-10-15 01:03:59 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f3feae7-b3c4-3bb0-8a5c-5b18bd8ae779 | -3.1139 | -54.216301 | 2024-10-15 01:03:59 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e8291cd-e8c9-3466-8b58-468739f1e630 | -3.1156 | -54.223701 | 2024-10-15 01:03:59 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68c2c673-86a4-3424-832f-baa6d8af45bd | -3.1173 | -54.231098 | 2024-10-15 01:03:59 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba78ff54-c813-3bde-8b81-4b6e8707b5cc | -1.9327 | -56.599701 | 2024-10-15 01:03:59 | METOP-B | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52f9f9dc-ac43-3c75-a694-5a56d90c5f20 | -2.6139 | -59.865398 | 2024-10-15 01:04:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a8c87b4-ff50-39bf-8b81-1d934e2ee017 | -14.08 | -46.21 | 2024-10-15 01:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e041341c-93d7-3f0c-9251-5a864cb08f31 | -14.11 | -46.22 | 2024-10-15 01:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8326f6b8-5b1b-33fc-acaa-39b4540723cb | -14.11 | -46.17 | 2024-10-15 01:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6bb174f-481f-30bc-996c-76483b983618 | -2.0969 | -59.299999 | 2024-10-15 01:04:06 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 297b5a06-fc2d-3a38-b6ac-f39ee8b4e5e6 | 1.0178 | -52.197899 | 2024-10-15 01:04:31 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 98ed1761-66c0-37a6-9c40-df6be379c79b | 1.0154 | -52.208199 | 2024-10-15 01:04:31 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 903dbb23-6c94-3f1b-ad3c-c9f438ea3d8e | 1.0131 | -52.218601 | 2024-10-15 01:04:31 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6e74b007-78c9-3169-8e56-74ef0740ac05 | 1.0016 | -52.2164 | 2024-10-15 01:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 772f150b-e0d2-3ce2-85fd-bad59f49429f | -1.8577 | -47.8493 | 2024-10-15 01:05:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7b91769f-1249-3b99-893e-d1767c70bbac | -2.1221 | -46.0663 | 2024-10-15 01:05:18 | GOES-16 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 102.2 |
| a551e775-bc3d-356a-a4a0-762ea6e8227b | -2.4418 | -50.2447 | 2024-10-15 01:05:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b9c05a8a-9df7-3f9e-8522-3a3b4adb26da | -2.4419 | -50.2237 | 2024-10-15 01:05:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 384e036f-9afa-3989-9dab-eed13461f8b3 | -3.0397 | -53.2603 | 2024-10-15 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| fc743a28-b18a-38c3-a679-e434885ea88c | -3.1099 | -54.2263 | 2024-10-15 01:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 8d93be53-c217-3e86-b58d-710d4b2519d2 | -3.1282 | -54.2459 | 2024-10-15 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ccbe2102-c010-38a6-a5bf-a9e81dabcc97 | -3.1283 | -54.2259 | 2024-10-15 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 00754ebb-ed7b-31a5-a471-3e1c63a5e8d5 | -4.3959 | -47.7618 | 2024-10-15 01:05:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 905e9844-b3a3-32d0-bb9d-38b37c1426de | -4.4538 | -50.5125 | 2024-10-15 01:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b7656731-bd96-34d4-a29c-1b3737345d97 | -4.4723 | -50.5117 | 2024-10-15 01:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c13542c4-3666-3409-ae06-77955f8bc7d8 | 2.2294 | -63.252602 | 2024-10-15 01:05:31 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7987f454-7868-3aa3-83dc-7d6e8caf92d9 | -5.1983 | -44.8497 | 2024-10-15 01:05:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| cfba50c9-a2ed-301e-ad42-43477f4b78bc | -5.217 | -44.8485 | 2024-10-15 01:05:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 06e82b0d-ab95-306f-96ba-fa9ef55722bf | -5.2172 | -44.8258 | 2024-10-15 01:05:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f91f6419-2340-3052-a098-79441c6ef0a7 | -5.5732 | -49.3995 | 2024-10-15 01:05:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 41cb0c3e-1722-35c3-bdbc-4b479646dae2 | -10.164 | -46.2853 | 2024-10-15 01:06:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e713a578-0c99-3fd1-bb94-6ecc6bebe584 | -10.1644 | -46.2627 | 2024-10-15 01:06:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 4f33b1c1-978e-31d5-b1df-2868368a1550 | -10.1834 | -46.2604 | 2024-10-15 01:06:03 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 399b32cb-2d63-3a15-bf6e-b351d7fa164a | -10.3711 | -61.1935 | 2024-10-15 01:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 49931181-696c-33c0-8e75-738054997545 | -10.3713 | -61.1743 | 2024-10-15 01:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| a2dc49f1-a615-3bce-af2c-91a47a1572e2 | -10.822 | -49.256 | 2024-10-15 01:06:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 7f4f2533-c059-3b43-9b9f-400ae00736a3 | -10.8224 | -49.2343 | 2024-10-15 01:06:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 0841b99d-a861-31f2-9cd1-35504ad942af | -11.6915 | -65.2432 | 2024-10-15 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 13982215-ae86-314f-914d-d6dde0047041 | -11.6917 | -65.2243 | 2024-10-15 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| af7ac5bb-6488-38aa-a356-44ed83e9b014 | -12.3793 | -63.7294 | 2024-10-15 01:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 43b722f5-f308-3f2d-b26e-2e4eb1ba353d | -12.3795 | -63.7103 | 2024-10-15 01:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| cef3aaa9-b3ae-377c-9c14-9818d9b0b5a5 | -12.3982 | -63.7284 | 2024-10-15 01:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| dea97f2f-46bf-3a04-8a45-ac20f2b6cf53 | -12.3983 | -63.7093 | 2024-10-15 01:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d5e2a2bd-d0de-3afd-9ec2-1100325dae87 | -12.4602 | -63.0361 | 2024-10-15 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 0ec330b3-9523-373d-9d9b-30758a65835e | -12.4603 | -63.0169 | 2024-10-15 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 7323ca3e-58c0-3f84-b95a-885add15fe02 | -12.4961 | -63.2641 | 2024-10-15 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0cebcd70-ddb8-3316-b064-330e0838b64e | -12.515 | -63.263 | 2024-10-15 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 4d75a770-03f9-34dd-a734-444e864461f6 | -12.9538 | -62.7962 | 2024-10-15 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ec9c0e56-ebba-38a1-b9d1-701ac4396d3f | -12.9728 | -62.7951 | 2024-10-15 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d99f7afd-50fa-369d-861b-d8de192742c3 | -13.1475 | -62.3215 | 2024-10-15 01:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |


[Clique aqui para ver as próximas entradas](README16.md)
