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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca9353cc-f7f9-33d2-8f29-84db754d99f1 | -9.21548 | -59.77981 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 369c3248-5233-3a0e-95b5-63db63a9d7a2 | -9.21173 | -59.77509 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c78bef6-caf1-3c14-89b5-0a5ce3e6fae0 | -11.54341 | -60.29514 | 2024-10-11 05:42:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adf18b7a-8653-3d44-b480-fc5dbb2a0215 | -11.53911 | -60.29447 | 2024-10-11 05:42:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 80061035-9d6c-310a-a8c3-d2d4ffc0c385 | -7.94371 | -61.25891 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 618a3722-17fb-372d-acaf-e9e840b77c7e | -7.94301 | -61.26369 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a6404de-f8ce-342e-88c8-159ceb638ee2 | -7.93916 | -61.26311 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c8b6291-ba16-3e58-a2f5-2768c4ce4247 | -7.93393 | -61.27206 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec66f54d-76aa-3a8a-bda6-8277fbfa4002 | -7.93323 | -61.27684 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5184b145-f606-3992-a61d-7571b9854acc | -7.93146 | -61.26192 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8056adf0-2bc0-332f-8794-a66c73d59c5d | -7.93077 | -61.26669 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42e7c9ed-08a1-3654-bfc3-46e494676d10 | -7.93008 | -61.27145 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ed6f205e-88b9-399b-9306-d0f970fd1d2e | -7.92761 | -61.26133 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95618ae2-22e1-3715-a13c-ced63f326d79 | -7.92692 | -61.2661 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f24ea4f-2e9d-3891-b16b-a5fe9cad3512 | -7.9153 | -61.66387 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d28a75c0-9688-3009-84da-e723b128da42 | -7.83382 | -61.22116 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e86a571-75ea-31d2-bab6-5811ea88e317 | -7.82996 | -61.22058 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b91cec41-2b5c-3bde-bebf-16773dcb6752 | -7.82927 | -61.22541 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 846aea28-3363-34af-b070-b7da36ffb2e8 | -7.82216 | -61.16531 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b0c7c75c-da17-3b22-926b-c291a5bae97a | -7.82134 | -61.16228 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a3d7452-b6d9-39b0-8f00-69ff1c4761f3 | -7.82061 | -61.1671 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac509354-0222-366c-86d2-be33933081a8 | -7.81829 | -61.16472 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a5f1612f-cd4d-3a2a-a8f6-fbcb794e245d | -7.81747 | -61.1617 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 02f61525-2543-3de6-8f4d-df9b818ab608 | -7.81674 | -61.16652 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66c8c6c1-3229-3728-95cb-3f48c03a08ac | -7.81442 | -61.16415 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21c22677-059a-3669-abc9-61eba3fc5e65 | -7.78119 | -61.35086 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7d52ea9-663e-37c5-8f9c-1a2bea8dd90a | -7.77737 | -61.3503 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff512b7d-0d1f-338e-8dd9-aaa8d932ee8f | -7.77666 | -61.35498 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba1eb4de-149b-3e4d-a4fa-18c31e0d42a0 | -7.77354 | -61.34972 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa563624-98c8-3cb2-974f-0b93d1404496 | -7.77284 | -61.3544 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5147278-548b-398b-8806-5dfda1c39b3e | -7.64929 | -61.19846 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2702fb5a-c6f8-3f32-a4e4-74790b223ccd | -7.64858 | -61.20324 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 046b860f-a0b1-338e-bf76-96d6b5c2c146 | -7.64088 | -61.20209 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0da092e9-9d78-391e-b072-9de9680189db | -7.64018 | -61.20687 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 900fe197-02eb-348c-b198-9596c2ad86ac | -9.17079 | -62.6518 | 2024-10-11 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa98c42f-d596-3384-91f7-3d36b0da05aa | -9.17016 | -62.65598 | 2024-10-11 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eade0658-164c-3857-9aa8-358009908a38 | -9.11773 | -61.27555 | 2024-10-11 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b403415-be83-3f95-a54a-468b07ebfd2d | -8.23658 | -61.19526 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0127d49a-250a-31c0-ae21-38c60795fdb1 | -8.23545 | -61.1973 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68c38ece-5892-3b0e-b827-459f993b56f1 | -8.22279 | -61.5099 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e24959f-d987-31d0-8578-3277cac976bc | -8.21898 | -61.50932 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67fbd436-44ed-3a1e-82f3-387b520206cd | -8.16912 | -61.37889 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f92bac0f-0fba-3d14-8fbb-84200b323c90 | -8.16528 | -61.3783 | 2024-10-11 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2be09e7-f060-3d8a-9a07-bbab37ee8247 | -7.97681 | -61.50644 | 2024-10-11 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1dec572-0939-3796-819b-e56b5bab6af7 | -9.3876 | -63.41274 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32d24903-1a7f-3e2a-9671-a57a1e9c93df | -9.38701 | -63.41662 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c55c2848-f656-3b14-8904-e4353bb3c792 | -9.38351 | -63.41607 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 005056a6-8c36-3922-b327-9329daa827d6 | -9.3161 | -63.74452 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1320df1d-c0a0-3879-b461-4886407cc906 | -9.31265 | -63.744 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f382fb07-d5ab-308e-8367-1607dc074373 | -9.31037 | -63.82903 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df9ac6f2-b7b6-3b00-8e7e-12f7fadcda3f | -9.29715 | -63.48693 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33e846b6-3442-3003-98f9-b45c7182491d | -9.12085 | -63.58303 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e0562d9-0569-3fb0-a41b-37449a3940fe | -8.81225 | -63.00291 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e914f2f8-1ea9-353a-b1ba-63d18309b888 | -8.77969 | -63.26495 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a7baae5-39f1-3eec-9832-2abdd4a91626 | -8.77619 | -63.26442 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a26ba3c0-aa34-3714-85db-3dc4597671f3 | -8.76869 | -63.21923 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dc9f25c-6cd6-3656-9f72-43edc0c77df4 | -8.691 | -63.09179 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84c33175-b2ae-3db5-8c13-194ae4f76806 | -8.68687 | -63.09522 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b718ce1d-f44c-3151-975d-02ebe84edd09 | -8.67158 | -63.33715 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b4e4e67-fd9b-349a-8ad0-91d0990c9ead | -8.66809 | -63.33662 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d195fc1-2252-3dd0-9995-471aad0c0334 | -8.66749 | -63.34048 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 841b733f-f34e-3f14-80c0-495653eadb3c | -8.66459 | -63.33609 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 227ff89f-2d70-3423-808c-e4248a4d6f95 | -8.6611 | -63.33555 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b07a8307-ce9d-3175-86ef-0eb65b1f3fe9 | -8.64843 | -63.25413 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4cdad03-2303-37ec-a419-928dfa4723c3 | -8.628 | -63.24702 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29210a06-87bb-3bc9-acd9-d8a433d7b864 | -8.62391 | -63.25039 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1ed7832-ad5f-3298-8795-95f51fb1e5d3 | -8.62041 | -63.24985 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 247dde43-68a5-3189-8411-63f23f2f1ef4 | -8.61983 | -63.25375 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 057aa8cf-70f6-301d-81af-fcde98cb6cfe | -8.61691 | -63.24931 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdf1a59c-75c2-392b-8f2b-4aaf8f97cac7 | -8.61633 | -63.25322 | 2024-10-11 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d90f2d65-bd64-396c-aeee-9536015b5e40 | -8.55719 | -64.03588 | 2024-10-11 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 267785e2-2809-311e-9365-82c24e606d7d | -8.55662 | -64.03954 | 2024-10-11 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc8f4c09-6cb8-37eb-be15-e33a3a68021e | -8.19308 | -64.02158 | 2024-10-11 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55ea5741-26af-3006-ad5f-c5af0986c177 | -8.15162 | -63.92963 | 2024-10-11 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31b4a9b0-6313-3f85-a84c-bc3a56de8a17 | -10.26525 | -63.34343 | 2024-10-11 05:42:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd34b921-7a45-3393-87f1-782ba206d6bb | -10.26465 | -63.34744 | 2024-10-11 05:42:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b71e7e0-f7e4-39fb-a42f-5c62bcdf1fdb | -10.26171 | -63.34289 | 2024-10-11 05:42:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce62799c-21db-30fc-910a-9e2f3df0e98e | -9.84406 | -64.05824 | 2024-10-11 05:42:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fe580ae-1eab-3cd4-aef7-16501e1162d4 | -9.82804 | -64.0481 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de1daa66-fc6a-3062-9e93-82ea8fe1177b | -9.81831 | -63.63359 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cdf7cc4-568e-3f7e-8832-0c6de79035e1 | -9.58553 | -64.10677 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 117a7247-2da5-366b-83d7-163549e7e12a | -9.58211 | -64.10625 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e11c38b-d998-3c0a-969e-39273598e335 | -9.57526 | -64.10522 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 314b9f78-3d43-395b-99c8-152137ee7ff0 | -9.57183 | -64.10471 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 287ab0ea-3292-3027-a106-05a39e15a2a8 | -9.51682 | -62.93151 | 2024-10-11 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa508004-1b90-3f65-97d3-c4ed7c30f88a | -9.51619 | -63.49123 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc284bca-fde6-3fa4-b482-326c1f61316e | -9.51323 | -62.93097 | 2024-10-11 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03c16294-2d29-32d8-9b9a-faca3d7cef87 | -9.51269 | -63.49072 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f68aeb1-b35e-3655-a429-fba65216e047 | -9.50358 | -63.3853 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef8cda12-c0f7-3684-aa34-b064eb863519 | -9.50007 | -63.38476 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 628bf428-0c4a-3e5a-b503-f1f407deeb7f | -9.49656 | -63.38423 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 493d49f0-6848-3cfd-b050-f68f10af4ccc | -9.49305 | -63.38367 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb070fa9-a657-3173-9474-048de1e0b8b6 | -9.46717 | -63.14938 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e787686e-3be3-3108-b25e-eb50aea848d0 | -9.46676 | -63.14808 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a8d990f-3edc-36b3-946b-40ab64a21a5d | -9.46423 | -63.14485 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c752199-7151-301c-8fd3-6162fc4b8b41 | -9.4638 | -63.14354 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee05a1e9-e64a-3b1c-b6f6-715768f2fe38 | -9.46362 | -63.14887 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b1a401c-caca-3cb7-997a-8171b6b11462 | -9.46321 | -63.14756 | 2024-10-11 05:42:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5be97fa4-495b-3a1b-9c47-2b0457dedfc2 | -10.05574 | -63.25255 | 2024-10-11 05:42:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebf3cee2-2e93-3d08-aff4-ff007f682f2d | -10.64065 | -64.54984 | 2024-10-11 05:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README112.md)
