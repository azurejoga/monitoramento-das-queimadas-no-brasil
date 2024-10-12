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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3256b3c0-e81a-3dbc-bc91-0f7323e383e0 | -11.09219 | -60.71893 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbf1c901-069a-3f61-8c97-7c8e94bffb5a | -11.08779 | -60.74733 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10084566-f62e-359e-b670-27ed8ee82d39 | -11.08386 | -60.72853 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32ba1bcd-10ec-3433-81f1-3f26c2f4b520 | -11.08107 | -60.72445 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a60dead-2b88-3881-a701-4e17258da3da | -11.06994 | -60.72997 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5c9ed56-280a-34f5-9517-be76cec90732 | -11.0666 | -60.72945 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ed1bf79-2578-3479-a1f9-e7170b5a21a5 | -11.05947 | -60.77556 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cde617d-7b89-3c65-b10a-850c99aefca1 | -11.05558 | -60.77859 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d27b58f8-9b06-39ee-9ea3-c67130366fe5 | -11.00512 | -61.12526 | 2024-10-12 05:25:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8a602da-94cb-337e-81b0-cc1aa03689ff | -10.97411 | -61.088 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 740568c0-61a0-3eca-b9bf-4fe9cd673d27 | -10.97356 | -61.09152 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a0ea54c-6f71-3c48-a682-0e8b90c15f23 | -10.97193 | -61.12372 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d29be886-514d-396f-9724-96e052058d8c | -10.97078 | -61.08747 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3db02159-27b3-3ca9-a3a9-dd678e4e39fd | -10.97023 | -61.09099 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2fd66f5-7193-3ca1-8327-54318e70c856 | -10.9675 | -61.13023 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55912595-a60b-3c83-80a2-5fcf236aaff4 | -10.96746 | -61.08694 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a0755ba-b38b-3c76-87e9-67b1e909b14b | -10.96695 | -61.13374 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62eed2f5-a3d9-392e-96c2-f811f9a96fa0 | -10.96691 | -61.09045 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf088c9c-3b18-373c-b1e8-7b96ef462680 | -10.96636 | -61.09397 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bad19587-0b27-31a0-8224-1d03801f8fe1 | -10.96624 | -60.98557 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b5347eb-6dd9-3405-b685-92134e1b0dcf | -10.96413 | -61.0864 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 973bba4f-c7cc-38ba-8279-f340d5a2a9bb | -10.96362 | -61.13322 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9d3e31e-0f27-33de-949a-977002924fb1 | -10.96358 | -61.08992 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 456164cf-1670-3443-a090-e774f9fd42c1 | -10.96291 | -60.98505 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5e97aa7-760f-304a-be71-17f5ca1e42e5 | -10.96083 | -61.10752 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75000943-f15e-3bca-9dec-1cb29714080e | -10.9603 | -61.13269 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab312bcf-8f6c-3650-8ed5-ff9e54b75135 | -10.96025 | -61.08938 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09fbe5da-d78b-306e-b682-709f49658f91 | -10.95975 | -61.1362 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f657c3a-4587-31ee-ae11-a2e1af8fb314 | -10.9575 | -61.10699 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8fa2663-910c-3a8b-a0e4-77e323e634a1 | -10.95697 | -61.13215 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c0f0f74-329e-3208-ba4c-adb61e76a368 | -10.95642 | -61.13567 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a318a5d-604d-399b-ac32-b46d34e13043 | -10.95529 | -61.12107 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31932608-f33d-35c0-95b0-58753df95052 | -10.95474 | -61.12459 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7eed687f-88d6-3db1-84ac-efb221faea18 | -10.95472 | -61.10294 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb0eaff3-438f-32b5-b89b-0aa1b474cc93 | -10.9542 | -61.12811 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d55503c4-1d12-3aaf-aa00-98427667fd17 | -10.95417 | -61.10646 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d193fbb-4b92-3e9b-b9c3-7f48151a628c | -10.95142 | -61.12405 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02325f03-0a1e-31ee-8079-c8ac80f91c00 | -10.9514 | -61.10241 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c1bcfe7-aa71-3d1b-bab9-0194933ac682 | -10.95087 | -61.12758 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 263f1c3b-6b43-313d-b4c0-a91aff427eb5 | -10.95084 | -61.10593 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f0a9e65-9d5c-38c4-8e4e-d8b9bd8c921a | -10.95072 | -60.99755 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7993369e-285f-3de7-a581-3ef253c51957 | -10.95032 | -61.13109 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d89d1cc2-d40d-32cd-ba8a-f4835bbcb33a | -10.95029 | -61.10946 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73d83240-a585-38e3-9ab1-0848ed2e0847 | -10.94807 | -61.10189 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a185f21-d346-3e55-812b-1fcbd5db1875 | -10.94752 | -61.10541 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 710f4385-b8fe-3b35-8ca9-c631aaa60b03 | -10.94697 | -61.10892 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0359776-e99f-33d5-876a-c81b242103c6 | -10.94252 | -60.76448 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dbdfcc8-b055-364d-b6ae-7421eb74e6ef | -10.92987 | -60.82413 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17b47ddf-ba6f-379c-8e5c-d106ccb02750 | -10.92708 | -60.82005 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a115c4d3-88ef-3540-b6c6-a087cbcec5bd | -10.92013 | -60.95295 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c9a70483-77ed-3e3f-ace4-f45e127dcb00 | -10.91958 | -60.95647 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 417412d3-7f2c-3a46-85d7-52a1ecea1ab0 | -10.91679 | -60.95243 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 55470b30-b729-358a-97fc-b49e0c3ae2d9 | -10.91625 | -60.95596 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e0291992-6469-33f0-af9f-d541f4f3f37e | -10.91346 | -60.9519 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 85fd661f-9b32-30d0-ae8a-62c0bccb5c2f | -10.91174 | -60.91904 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55034ff9-2a3d-313e-9f16-f0618f0a6adb | -10.91119 | -60.92258 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef8606b7-c544-3c7b-bc5b-3aaca66c6e40 | -10.91115 | -60.90086 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57e6b1c1-a99f-33f9-9193-fae53e4b2835 | -10.91005 | -60.90792 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7858f25-1561-34b0-8268-a228b0b75ba2 | -10.90896 | -60.91499 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 132853ab-b80a-31b2-9312-232eddc00761 | -10.90891 | -60.89327 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c2daae9-675a-3aa2-bdc4-56205b4e8145 | -10.90841 | -60.91851 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b8d9c8-7dc5-338d-8df7-ee294a40d2fa | -10.90836 | -60.8968 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 606aeb86-dbf1-32b2-8a61-d4bcf2601f7f | -10.90558 | -60.89273 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2804246-d0c0-3332-8680-df7722cec2c2 | -10.90457 | -60.94324 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 414848d2-ed8d-3a81-b509-517f6a4e5088 | -10.90351 | -60.89274 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db2fa242-27d6-3c46-a854-238afb77ec5e | -10.90073 | -60.88868 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b506bdfb-0fd4-3334-bc1c-6ee996dc29e9 | -10.90018 | -60.89222 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59572ecf-5056-35ea-b761-6d0d60be7067 | -10.9001 | -60.92805 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05103fcd-0134-3b1b-b09b-7053e3b17224 | -10.89962 | -60.89575 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bc423f43-2ba4-333e-b61c-fd455d7b2a9e | -10.89684 | -60.89168 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7d0af4c-345e-302c-981a-643aaac5aa38 | -10.88957 | -60.8507 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21efe05f-d1f9-32a5-9dd2-147dec8680e3 | -10.88679 | -60.84664 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fe44458-a03a-3cc6-b623-426fb44c30e5 | -11.21536 | -61.33961 | 2024-10-12 05:25:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec2f429f-1000-3a35-ae24-99c360ade279 | -10.82192 | -61.41331 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b93b9f1-263a-3f40-b5eb-0e8c1e48486f | -10.81915 | -61.40927 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c255cad-b9c8-3719-8f62-e8d17e227d9e | -10.81859 | -61.41278 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f377bfa9-46d2-339b-9560-ea57b0265877 | -10.81804 | -61.41629 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9e79631-0a1a-3df8-a6c4-8ca9a8919c6b | -10.81749 | -61.4198 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06b8831e-a7eb-3551-84be-fb90d9d369e4 | -10.81472 | -61.41576 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5af938f3-4b0d-3353-8cfb-85c03d9b8bd0 | -10.81417 | -61.41927 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a1cdb5d-2051-31e8-b2db-08bba803d215 | -11.25357 | -60.55118 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9591de19-029c-3e57-9c69-e3c140c00dea | -11.25348 | -60.50723 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2132e83a-451f-3325-aff2-448d39a7c722 | -11.25067 | -60.50315 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db5ba0a1-f583-3efd-bd82-ebd8ff5954c3 | -11.25022 | -60.55063 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64804261-9ede-3b0a-bd97-4aafa771ef7f | -11.25012 | -60.50671 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb1630c7-888a-372b-82c9-67b0741a66c8 | -11.24966 | -60.55422 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a23b1a7a-68fa-3eb1-a0a4-637b015fd02b | -11.24857 | -60.56133 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6383268-b39d-320d-8a99-75cdff80c7a1 | -11.24631 | -60.55368 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be2a2387-874d-3756-b09b-00917f4e314c | -11.24577 | -60.55723 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d537294-6104-3f58-99d7-3fe845d2256b | -11.24522 | -60.56078 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41e6a627-24fc-3a7d-bfb5-3713ac0cd7ff | -11.24467 | -60.56435 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| decd6540-b2f3-3fbf-9808-340300f38cfb | -11.24447 | -60.45415 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4b94199-8a33-3540-be0b-e3fe1c27aecc | -11.24277 | -60.44284 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67b3111c-9965-3c85-a5de-e614006ed2fa | -11.24107 | -60.43153 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9b8a9b9-0051-32ba-8638-c56b105c2679 | -11.24051 | -60.43514 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c9b9b57-3ca7-3ab4-a564-58ce3d6fecd6 | -11.23996 | -60.43873 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f078e28-2ad6-33d5-bca2-de168c2c0ed6 | -11.2377 | -60.43102 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72030515-0aa5-32da-84cb-8552067675f9 | -11.23741 | -60.56687 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1f5b9ce-9e6f-347c-b2bf-cb4bb21be23a | -11.23715 | -60.43463 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a1994e1-1ca3-3dce-926c-b249ac4e7280 | -11.23614 | -60.48596 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README131.md)
