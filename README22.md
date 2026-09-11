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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be4a98fe-dd6e-3a57-9af8-abacc543c2bf | -8.99094 | -65.41369 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b884fa2b-7e81-3552-8ce9-add81c1cb910 | -10.19489 | -54.25483 | 2026-09-11 04:53:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 947b0d75-b94b-330a-9f0b-a216d02d056b | -14.59479 | -48.85495 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 368f6530-eb90-3afd-8fca-64ddba3e553d | -8.98992 | -65.4189 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 093ef5ca-15fb-39ff-be0c-6bbe9cd3ad57 | -13.21957 | -61.62992 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0bcea5f-1143-30dd-8344-92f40b151a7c | -13.00051 | -44.11133 | 2026-09-11 04:53:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e516316d-013e-3c9f-a27c-3cd00b95b6ea | -10.70979 | -46.06491 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 185b05b3-4c06-306a-82c0-2802a2747c56 | -13.50467 | -48.55791 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd6c9c17-8ec0-398d-b67f-409149112a5f | -14.5901 | -48.85808 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2db52bbe-3e29-3e0a-bff7-7b41859a834e | -13.77241 | -43.64021 | 2026-09-11 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73db6532-e412-3bcb-a74b-70f270d029d1 | -15.60413 | -53.80937 | 2026-09-11 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dffed323-fe06-3fb0-bcb6-ea5ce7eeb650 | -9.02462 | -65.4092 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 164f6488-386b-34a7-a296-3b75156f7809 | -11.02133 | -55.81855 | 2026-09-11 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ea0f230-d86f-374d-abc8-a4daf6c0b541 | -13.49617 | -48.55714 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f405daf-9973-3640-b74b-2b32c284c51a | -9.39838 | -65.8716 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ac8ecfe-c93b-3221-b521-ab00cc36a36b | -9.21939 | -65.58228 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a48958c2-3559-3272-9dfd-8be0703683f1 | -10.98214 | -47.88696 | 2026-09-11 04:53:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa2dcbbe-d2e9-3355-8390-ce83436b717b | -10.47195 | -48.65331 | 2026-09-11 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f83f992e-5d24-3a6f-a2f6-1988f278b73f | -14.91434 | -44.66838 | 2026-09-11 04:53:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 017d3f98-73ab-3b02-b450-403bcc7a6987 | -13.21517 | -61.83583 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36d8ba9b-8795-376a-82f9-fd4dee11a630 | -13.24436 | -61.59916 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 320c2005-6c1e-3436-a5df-bbfb7cae42cc | -10.64226 | -46.13444 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e732a980-7716-383e-97d7-6bc9b910e8ba | -14.61268 | -48.84914 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a897566-a4f9-3ff6-ba90-421af43965a8 | -11.41407 | -62.12672 | 2026-09-11 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fbe5eba-4fc6-346a-b705-bdcaa2210169 | -10.48078 | -51.35254 | 2026-09-11 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d3c5408-0bbe-3e49-9a4d-79419cb36856 | -10.18198 | -59.63079 | 2026-09-11 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f27fc50a-db7d-30f4-9a63-8feb019bac64 | -10.52618 | -51.34664 | 2026-09-11 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc22f932-9d0e-3418-b393-6ef3a44f4381 | -13.36753 | -48.01503 | 2026-09-11 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f86b9a24-9daa-3628-ab5b-3ae55127e5c3 | -14.60844 | -48.8488 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d408f4d8-bbc4-3cf0-8852-af45594530d6 | -10.79 | -45.93826 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6f4b9efb-2cfb-34ed-8e1f-4bc9d0161d17 | -9.67732 | -55.11255 | 2026-09-11 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d3f4634-f898-30de-8dfe-e3238bdfa751 | -13.48717 | -48.56004 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7784caea-6918-3a99-a091-79246033dbdf | -14.61691 | -48.84959 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92425251-a3a6-3b88-8054-b66cb95bea48 | -10.6707 | -49.08214 | 2026-09-11 04:53:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 187bdeb2-71e1-3654-bf36-8a0ffbade0f7 | -10.78028 | -45.93699 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 242b4d97-22e5-369b-8968-0680c082c988 | -9.28969 | -65.80929 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23ed9f6d-4ca3-3e1d-b58c-9b81102ed7d3 | -8.8307 | -62.48139 | 2026-09-11 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 809c6074-8c68-3ec6-b2e3-d53f0c685950 | -10.10774 | -54.92949 | 2026-09-11 04:53:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 308f4990-2964-38d5-984b-7654e31f7c16 | -10.64495 | -46.1511 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aedffca0-0ba5-34fa-be1a-810ca45dacc6 | -13.49191 | -48.55678 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f265d3a-2430-3624-ab6e-cb62be52d7ec | -10.47248 | -48.64961 | 2026-09-11 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00631d06-2194-33ba-b123-055549e37e48 | -8.83597 | -62.48241 | 2026-09-11 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 30086067-d173-39ca-b449-ee21fb0ad9f1 | -10.75653 | -46.19389 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 112b2c12-356c-34ba-bd23-b945bea96060 | -13.24897 | -61.60004 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 057c60ed-72e0-3711-b286-a9918164e22c | -8.46318 | -64.05449 | 2026-09-11 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7810eb2-cf17-3f34-ba1d-ca86829ecd7d | -14.60321 | -48.85608 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3f20689-ac02-38b1-bb1e-4d2f91cb8da8 | -9.01729 | -65.41318 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdcd0a4a-b876-326f-89a3-dddb057d3063 | -13.25549 | -61.61647 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db1eaa21-2677-30ba-bad6-a30c7f394d0c | -12.15379 | -64.13985 | 2026-09-11 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7258b1f9-25d8-3e3d-95d6-d4a1b0127cbc | -13.34447 | -61.67267 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| adb7998e-be18-34a1-8e9e-bd8e6ef17bad | -13.49142 | -48.56047 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2f2dd4b-50e4-3912-a9be-d616b5c46674 | -10.54644 | -51.3539 | 2026-09-11 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 803a1db2-4a33-37a4-9aae-ed92a461ce6e | -9.03528 | -65.422 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c9d8b6a5-04fe-3b6e-93c8-02d56245a013 | -13.49566 | -48.56091 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a53c82e-cd71-380b-9476-adaacf5eb3f1 | -9.2341 | -65.57454 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dda0bfd-b51e-3bd3-bb94-8dd40854e2af | -13.47289 | -48.50575 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fee4d71-2913-3a93-bc6a-a2482ae73b1c | -9.07724 | -61.03089 | 2026-09-11 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 60e43e33-4f6c-354e-a7c6-765398d8250f | -8.99328 | -65.42284 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe5670b8-b623-3b98-a1fe-be1742a24071 | -10.64157 | -46.13977 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0078bea1-7bdb-3dba-8319-494bb2029fe0 | -9.39733 | -65.877 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e95246a8-4b68-3dfa-a9cd-db2a564990c4 | -9.71254 | -64.53898 | 2026-09-11 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d53f6bcd-99e9-311d-a293-fff40e36c23c | -13.31583 | -61.67227 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9757864-5032-30c8-aeba-9fa469287d11 | -11.81105 | -60.45728 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0503dc5-f0eb-3d8e-8403-76984cceb039 | -10.67533 | -49.07771 | 2026-09-11 04:53:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3122f69-1dec-3dd2-9d74-91477ba2bbf2 | -8.83009 | -62.48476 | 2026-09-11 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3265b9ec-f259-399d-9fa8-1058c7a7b118 | -11.81621 | -60.4537 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92da5019-a0ca-33a7-bf61-1db03a9a6db3 | -10.50211 | -54.35518 | 2026-09-11 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a0ff2fe-7f46-3219-89f4-e86addda7678 | -9.4274 | -65.8601 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ad999a5-8863-358f-917b-fa0360027a3d | -10.53312 | -51.34781 | 2026-09-11 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 041e6603-440e-3e55-8abc-bff4bb6311a6 | -14.60691 | -48.86048 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26c3e954-3f36-35ea-bb84-8d0a6d1d9743 | -9.67972 | -57.75546 | 2026-09-11 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ef17361-867d-3457-9327-90178ff6564b | -10.36129 | -48.13567 | 2026-09-11 04:53:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 006ed93f-2301-374d-b469-ca4f57a125c9 | -10.1863 | -59.63126 | 2026-09-11 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49830e40-9b91-39d7-a9fa-e13f3df4f758 | -10.73331 | -46.14815 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a1b0b429-59f1-3172-9421-6db8bd88933b | -14.89017 | -49.22967 | 2026-09-11 04:53:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 941dd3f2-aeab-3217-a215-239febdef4b7 | -10.36549 | -48.13593 | 2026-09-11 04:53:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff54c304-a95b-3aaa-9dfe-e02a70f1b76f | -9.4145 | -65.85756 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c02d1437-514d-3582-9bca-295e9a0f5e41 | -10.17769 | -59.63021 | 2026-09-11 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0bcd81e-feac-30fe-8a75-4d83483c7de7 | -12.88412 | -47.42762 | 2026-09-11 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d2a368c-b70e-3be9-baae-2853671774fb | -13.31491 | -61.6772 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7db734e-9971-3651-910a-8db02d9457c4 | -14.66257 | -44.12518 | 2026-09-11 04:53:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 645d64e6-13c7-3557-98f7-34386f8c52de | -10.78439 | -45.94338 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 49c7a0cd-0a39-3c72-bc0f-c29968c6ac6d | -11.39913 | -55.24034 | 2026-09-11 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 788e8acc-7a76-321b-9f56-b9b129e8df2b | -13.77372 | -43.63981 | 2026-09-11 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c63b54a7-7816-328f-a8de-334fa184e729 | -14.60741 | -48.85667 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31a9e001-2abc-3568-b076-e1f264caf2f2 | -9.42095 | -65.85883 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5e81a88-0005-38e7-b88f-b79fb078e20e | -13.35986 | -51.7714 | 2026-09-11 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cff8427c-8e12-3016-8f0b-308f76dd561d | -13.25728 | -61.60669 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d480d5c-cb89-3be2-9233-14c8dae93e89 | -13.50521 | -48.55392 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 034c972a-108e-31a3-9d3c-ba1d6d243dfb | -14.8593 | -48.1553 | 2026-09-11 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b53379cf-5eda-3152-a7a6-3a192ae2dd4f | -13.32787 | -61.68478 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e5f9a914-0f22-315f-b541-29a75906a677 | -12.15884 | -64.13839 | 2026-09-11 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ead1d41-d70f-3f8c-adde-3c43a8fde212 | -10.54062 | -51.34517 | 2026-09-11 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1555f05-f25e-3351-a752-b7a189e5ec17 | -13.6272 | -47.67693 | 2026-09-11 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5348a86-ff5d-3920-8755-9e5db9daa1fb | -10.77127 | -45.93021 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5432d2b8-f640-3c4e-8c75-24ef1663b593 | -10.48988 | -48.65165 | 2026-09-11 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd89cd58-3511-38ab-8f7d-f173bb783dcc | -10.51758 | -49.45821 | 2026-09-11 04:53:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41536946-85b2-30d1-be14-c04e8052934e | -13.25357 | -61.60092 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5be16ed2-5be3-39d2-ba0d-1e2ef37009c5 | -8.63961 | -66.5098 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a014a3bb-3e96-31ac-9934-57979ef4f6ee | -10.97902 | -47.87804 | 2026-09-11 04:53:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README23.md)
